#!/usr/bin/env python3
"""Tests for the vendor fact tools. Run: python3 tools/facts/test_facts.py"""
import copy
import unittest

from common import html_to_text, json_strings, load_schema, match_quote, normalize
from validate import check

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


if __name__ == '__main__':
    unittest.main(verbosity=1)
