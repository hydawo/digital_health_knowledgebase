#!/usr/bin/env python3
"""Write the dedup list for seeding a Module 5 domain: every DOI already anywhere in the library.

    python3 tools/domains/known_dois.py <domain>

Writes module-05-measurement-science/<domain>/_seed/known-dois.tsv, one `doi<TAB>where` line per
DOI, lowercased. Sources: the Module 1, 2 and 4 catalogues, every module's sources.md, every Module 5
catalogue and any lane files already in a domain's _seed/, and the Module 3 ledger. JMIR papers cited
only by URL (jmir.org/<year>/<issue>/e<id>) are converted to their 10.2196/<id> DOI. Seeding agents
also grep the repo by title, because some papers are cited without either.
"""
import glob
import json
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
DOI = re.compile(r'10\.\d{4,9}/[^\s)|>"\]]+')
JMIR = re.compile(r'jmir\.org/\d{4}/\d+/e(\d+)')


def sources():
    fixed = ['module-01-wearables/literature-library.md', 'module-01-wearables/research-library-wearables.md',
             'module-02-digital-phenotyping/literature-library.md', 'module-04-methods-and-reviews/literature-library.md']
    return (fixed + sorted(glob.glob('module-0*/sources.md'))
            + sorted(glob.glob('module-05-measurement-science/*/literature-library.md'))
            + sorted(glob.glob('module-05-measurement-science/*/_seed/lane-*.md')))


def collect():
    found = {}
    for f in sources():
        text = open(os.path.join(ROOT, f), encoding='utf-8').read()
        for m in DOI.finditer(text):
            found.setdefault(m.group(0).lower().rstrip('.'), f)
        for m in JMIR.finditer(text):
            found.setdefault('10.2196/' + m.group(1), f)
    ledger = json.load(open(os.path.join(ROOT, 'module-03-applied-studies/literature-index.json'), encoding='utf-8'))
    for d in ledger['dois_seen']:
        found.setdefault(d.lower(), 'module-03 ledger')
    return found


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    out = os.path.join(ROOT, 'module-05-measurement-science', sys.argv[1], '_seed')
    os.makedirs(out, exist_ok=True)
    found = collect()
    with open(os.path.join(out, 'known-dois.tsv'), 'w', encoding='utf-8') as fh:
        fh.write(''.join(f'{k}\t{v}\n' for k, v in sorted(found.items())))
    print(f'{len(found)} DOIs written to {os.path.relpath(out, ROOT)}/known-dois.tsv')


if __name__ == '__main__':
    os.chdir(ROOT)
    main()
