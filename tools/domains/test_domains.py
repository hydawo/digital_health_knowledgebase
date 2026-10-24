#!/usr/bin/env python3
"""Tests for the Module 5 domain tools. Run: python3 tools/domains/test_domains.py"""
import os
import tempfile
import unittest

import build_hubs
import known_dois

CATALOGUE = """# Test domain

## Consensus and guidance

| # | Title | Authors | Venue / Year | DOI / URL | OA status | PDF | What it establishes |
|---|---|---|---|---|---|---|---|
| T-001 | A guideline | Smith A | *Journal* 2024 | [10.1/abc](https://doi.org/10.1/abc) | **Verified OA** | none, not stored | Consensus and guidance. Text. |

## Metrics

| # | Title | Authors | Venue / Year | DOI / URL | OA status | PDF | What it establishes |
|---|---|---|---|---|---|---|---|
| T-002 | A metric | Jones B | *Other* 2021 | [10.1/def](https://doi.org/10.1/def) | **Paywalled** | none, not stored | Metrics. Text. |
"""

PAPER = {'key': '10.9/xyz', 'kind': 'paper', 'module': 1, 'file': 'module-01-wearables/literature-library.md',
         'row_id': 'L001', 'title': 'Device paper', 'weight': 'secondary', 'reason': 'one of several outcomes'}
PROFILE = {'key': 'module-01-wearables/profiles/oura.md', 'kind': 'm1-profile', 'module': 1,
           'file': 'module-01-wearables/profiles/oura.md', 'row_id': None, 'title': 'Oura', 'weight': 'primary',
           'reason': 'core capability'}


class Hubs(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        os.makedirs(os.path.join(self.tmp.name, 'test'))
        with open(os.path.join(self.tmp.name, 'test', 'literature-library.md'), 'w') as fh:
            fh.write(CATALOGUE)
        self.old = build_hubs.M5
        build_hubs.M5 = self.tmp.name

    def tearDown(self):
        build_hubs.M5 = self.old
        self.tmp.cleanup()

    def test_rows_keep_their_section(self):
        rows = build_hubs.catalogue_rows('test')
        self.assertEqual([(r[0], r[1]) for r in rows], [('Consensus and guidance', 'T-001'), ('Metrics', 'T-002')])

    def test_counts_and_sections(self):
        page = build_hubs.render('test', 'Test', [PAPER, PROFILE])
        self.assertIn('| Module 5 catalogue | 2 |', page)
        self.assertIn('| Device and platform profiles | 1 |', page)
        self.assertIn('| Papers in Modules 1, 2 and 4 | 1 |', page)
        self.assertIn('[Oura](../../module-01-wearables/profiles/oura.md)', page)
        self.assertIn('[doi](https://doi.org/10.9/xyz)', page)

    def test_overview_link_only_when_file_exists(self):
        self.assertNotIn('overview.md', build_hubs.render('test', 'Test', []))
        open(os.path.join(self.tmp.name, 'test', 'overview.md'), 'w').close()
        self.assertIn('[`overview.md`](overview.md)', build_hubs.render('test', 'Test', []))

    def test_primary_listed_before_secondary(self):
        a = dict(PAPER, key='10.9/a', title='Zeta', weight='primary')
        b = dict(PAPER, key='10.9/b', title='Alpha', weight='secondary')
        page = build_hubs.render('test', 'Test', [b, a])
        self.assertLess(page.index('Zeta'), page.index('Alpha'))

    def test_no_blank_line_runs(self):
        self.assertNotIn('\n\n\n', build_hubs.render('test', 'Test', [PAPER]))


class KnownDois(unittest.TestCase):
    def test_jmir_url_becomes_doi(self):
        m = known_dois.JMIR.search('see https://mhealth.jmir.org/2020/9/e18694/ for details')
        self.assertEqual('10.2196/' + m.group(1), '10.2196/18694')

    def test_doi_stops_at_markdown_link_end(self):
        m = known_dois.DOI.search('[10.1016/j.sleep.2025.106506](https://doi.org/x)')
        self.assertEqual(m.group(0), '10.1016/j.sleep.2025.106506')


if __name__ == '__main__':
    unittest.main()
