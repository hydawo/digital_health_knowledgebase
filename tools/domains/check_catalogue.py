#!/usr/bin/env python3
"""Check a Module 5 domain catalogue against Crossref: title, first author and year for every DOI row.

    python3 tools/domains/check_catalogue.py sleep cardiac   # named domains
    python3 tools/domains/check_catalogue.py                 # every domain folder

Prints one line per row that does not match and a summary. Rows without a DOI (standards sold by
their publisher) are skipped. Sends no personal identifier to Crossref and waits between requests.
"""
import difflib
import json
import os
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
M5 = os.path.join(ROOT, 'module-05-measurement-science')
UA = 'digital-health-kb-catalogue-check/1.0 (+https://github.com/hydawo/digital_health_knowledgebase)'
PAUSE = 1.0
TITLE_MIN = 0.85


def norm(s):
    s = unicodedata.normalize('NFKD', s or '').encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9 ]', '', re.sub(r'<[^>]+>', '', s).lower().replace('-', ' ')).split()


def rows(domain):
    for line in open(os.path.join(M5, domain, 'literature-library.md'), encoding='utf-8'):
        if not line.startswith('| ') or line.startswith(('| #', '|---')):
            continue
        c = [x.strip() for x in line.strip().strip('|').split('|')]
        m = re.search(r'10\.\d{4,9}/[^\]\s]+?(?=\]|\))', c[4])
        if not m:
            continue
        year = re.search(r'(\d{4})\s*$', c[3].replace('*', '').strip())
        yield c[0], m.group(0), c[1], c[2], year.group(1) if year else ''


def crossref(doi):
    url = 'https://api.crossref.org/works/' + urllib.parse.quote(doi)
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)['message']


def check(domain):
    bad = n = 0
    for rid, doi, title, authors, year in rows(domain):
        n += 1
        try:
            w = crossref(doi)
        except urllib.error.HTTPError as e:
            print(f'{domain} {rid} {doi}: Crossref HTTP {e.code}')
            bad += 1
            time.sleep(PAUSE)
            continue
        problems = []
        ct = ' '.join((w.get('title') or [''])[:1])
        ratio = difflib.SequenceMatcher(None, ' '.join(norm(title)), ' '.join(norm(ct))).ratio()
        if ratio < TITLE_MIN:
            problems.append(f'title {ratio:.2f} vs "{ct[:90]}"')
        first = (w.get('author') or [{}])[0].get('family', '')
        ours = authors.split(',')[0].split()[0] if authors else ''
        if first and norm(first) and norm(ours) and norm(first)[0] not in norm(ours) and norm(ours)[0] not in norm(first):
            problems.append(f'first author "{ours}" vs Crossref "{first}"')
        years = {str(p['date-parts'][0][0]) for k in ('published-print', 'published-online', 'issued')
                 for p in [w.get(k) or {}] if p.get('date-parts') and p['date-parts'][0][0]}
        if year and years and year not in years:
            problems.append(f'year {year} vs Crossref {sorted(years)}')
        if problems:
            bad += 1
            print(f'{domain} {rid} {doi}: ' + '; '.join(problems))
        time.sleep(PAUSE)
    print(f'{domain}: {n} DOI rows checked, {bad} flagged')
    return bad


def main():
    domains = sys.argv[1:] or sorted(d for d in os.listdir(M5)
                                     if os.path.exists(os.path.join(M5, d, 'literature-library.md')))
    sys.exit(1 if sum(check(d) for d in domains) else 0)


if __name__ == '__main__':
    main()
