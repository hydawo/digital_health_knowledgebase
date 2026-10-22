#!/usr/bin/env python3
"""Tests for the vendor fact tools. Run: python3 tools/facts/test_facts.py"""
import copy
import datetime
import os
import tempfile
import unittest

from common import html_to_text, json_strings, load_schema, match_quote, normalize
from validate import check
import recheck

SCHEMA = load_schema()


def record(**over):
    facts = [{'field': f, 'status': 'not_applicable'} for g in SCHEMA['groups'].values() for f, s in g['fields'].items()
             if not (isinstance(s, dict) and 'wearable' not in s.get('applies_to', []))]
    rec = {'name': 'Test Co', 'kind': 'wearable', 'watch': [{'url': 'https://example.com', 'role': 'pricing'}], 'facts': facts}
    rec.update(over)
    return rec


def stated(field, **kw):
    f = {'field': field, 'status': 'stated', 'value': 'x', 'confidence': 'Verified', 'recheck_by': '2999-01-01',
         'sources': [{'url': 'https://example.com', 'type': 'vendor_page', 'retrieved': '2026-10-10', 'quote': 'exact words'}]}
    f.update(kw)
    return f


def with_fact(f):
    rec = record()
    rec['facts'] = [x for x in rec['facts'] if x['field'] != f['field']] + [f]
    return rec


class QuoteMatching(unittest.TestCase):
    def test_exact_after_normalisation(self):
        self.assertEqual(match_quote('It’s  “FREE”', "it's free!")[0], 'missing')  # quotes differ in punctuation kept
        self.assertEqual(match_quote('It’s  "free"', 'Plans: it\'s "FREE" today')[0], 'exact')

    def test_reworded_and_missing(self):
        page = 'API applications accessing more than ten users require approval from Oura before launch.'
        self.assertEqual(match_quote('API applications accessing more than 10 users require approval from Oura', page)[0], 'reworded')
        self.assertEqual(match_quote('Membership is free for researchers', page)[0], 'missing')

    def test_html_and_json_text(self):
        self.assertIn('visible', html_to_text('<p>visible</p><script>hidden()</script>'))
        self.assertNotIn('hidden', html_to_text('<p>visible</p><script>hidden()</script>'))
        self.assertIn('deep', json_strings({'a': [{'b': 'deep'}]}))

    def test_normalize_dashes_and_space(self):
        self.assertEqual(normalize('A—B  C'), 'a-b c')


class Validation(unittest.TestCase):
    def errs(self, rec):
        return check('t', rec, SCHEMA)[0]

    def test_complete_record_passes(self):
        self.assertEqual(self.errs(with_fact(stated('device_price'))), [])

    def test_missing_field(self):
        rec = record()
        rec['facts'] = [f for f in rec['facts'] if f['field'] != 'user_cap']
        self.assertTrue(any('user_cap' in e for e in self.errs(rec)))

    def test_stated_needs_quote(self):
        f = stated('device_price')
        del f['sources'][0]['quote']
        self.assertTrue(any('quote' in e for e in self.errs(with_fact(f))))

    def test_self_claim_capped(self):
        self.assertTrue(any('capped' in e for e in self.errs(with_fact(stated('soc2')))))
        ok = stated('soc2')
        ok['sources'].append({'url': 'https://registry.example', 'type': 'certificate', 'retrieved': '2026-10-10'})
        self.assertEqual(self.errs(with_fact(ok)), [])

    def test_cap_does_not_apply_to_not_public(self):
        f = {'field': 'soc2', 'status': 'not_public', 'confidence': 'Verified', 'recheck_by': '2999-01-01',
             'sources': [{'url': 'https://example.com/trust', 'type': 'vendor_page', 'retrieved': '2026-10-10'}]}
        self.assertEqual(self.errs(with_fact(f)), [])

    def test_fda_needs_regulator(self):
        self.assertTrue(any('regulator_db' in e for e in self.errs(with_fact(stated('fda_clearances')))))

    def test_conflict_needs_two_sources(self):
        self.assertTrue(any('two sources' in e for e in self.errs(with_fact(stated('device_price', status='conflict')))))

    def test_platform_only_field_rejected_for_wearable(self):
        rec = record()
        rec['facts'].append(stated('hosting_price'))
        self.assertTrue(any('unknown field "hosting_price"' in e for e in self.errs(rec)))

    def test_overdue(self):
        _, _, overdue = check('t', with_fact(stated('device_price', recheck_by='2000-01-01')), SCHEMA)
        self.assertEqual(len(overdue), 1)

    def test_bad_status_and_watch_role(self):
        rec = with_fact(stated('device_price', status='maybe'))
        rec['watch'][0]['role'] = 'gossip'
        e = self.errs(rec)
        self.assertTrue(any('status "maybe"' in x for x in e))
        self.assertTrue(any('role "gossip"' in x for x in e))


class RecheckExtension(unittest.TestCase):
    TODAY = datetime.date(2026, 11, 2)
    URL = ('https://example.com', 'https://example.com')

    def new(self, f, ok=True, exact=True):
        return recheck.eligible(f, 30, self.TODAY, lambda k: ok, lambda k, q: exact, lambda s: s.get('fetch_url') or s['url'])

    def test_due_and_intact_is_extended(self):
        self.assertEqual(self.new(stated('device_price', recheck_by='2026-11-09')), datetime.date(2026, 12, 2))

    def test_not_due_yet(self):
        self.assertIsNone(self.new(stated('device_price', recheck_by='2026-12-30')))

    def test_quote_changed_or_page_down(self):
        f = stated('device_price', recheck_by='2026-11-09')
        self.assertIsNone(self.new(f, exact=False))
        self.assertIsNone(self.new(f, ok=False))

    def test_only_stated_facts(self):
        for st in ('not_public', 'conflict', 'unclear'):
            self.assertIsNone(self.new(stated('device_price', status=st, recheck_by='2026-11-09')))

    def test_archive_source_never_extended(self):
        f = stated('device_price', recheck_by='2026-11-09')
        f['sources'][0]['fetch_url'] = 'https://web.archive.org/web/2026/https://example.com'
        self.assertIsNone(self.new(f))

    def test_stale_read_goes_back_to_a_person(self):
        f = stated('device_price', recheck_by='2026-11-09')
        f['sources'][0]['retrieved'] = '2026-07-01'
        self.assertIsNone(self.new(f))

    def test_write_changes_only_the_date(self):
        text = ("name: Test\nkind: wearable\nfacts:\n- field: a\n  status: stated\n  sources:\n  - url: u\n"
                "    quote: q\n  recheck_by: '2026-11-09'\n- field: b\n  status: stated\n  recheck_by: '2026-11-09'\n")
        with tempfile.NamedTemporaryFile('w', suffix='.yaml', delete=False) as fh:
            fh.write(text)
        recheck.write_dates(fh.name, {1: datetime.date(2026, 12, 2)})
        with open(fh.name) as fh2:
            out = fh2.read()
        os.remove(fh.name)
        self.assertEqual(out, text.replace("b\n  status: stated\n  recheck_by: '2026-11-09'", "b\n  status: stated\n  recheck_by: '2026-12-02'"))


if __name__ == '__main__':
    unittest.main(verbosity=1)
