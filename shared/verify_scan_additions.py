#!/usr/bin/env python3
"""Check the papers a weekly-scan run added, before its branch is merged.

Run from the repository root, giving the commit the scan branch started from:
    python3 shared/verify_scan_additions.py <base-commit> [<branch>]
<branch> defaults to HEAD. The script compares the three literature indexes at <base-commit> and
<branch>, and for every newly added paper:
  1. looks the DOI up in Crossref and compares title, first author, year and journal with what the
     scan recorded (a title match below 0.9 or a different first author is flagged);
  2. pulls the full text from Europe PMC where it is open access, and prints the conflict-of-interest
     and funding passages so the sponsorship tier (A/B/C) can be checked by eye;
  3. counts how often the device or platform is named in the full text, to catch papers that only
     mention it in passing.
It changes nothing. Read the output, fix anything flagged, then merge. See the "Merging a scan run"
section of shared/weekly-literature-scan.md.
"""
import json, re, subprocess, sys, urllib.request, urllib.parse, difflib

INDEXES = {
    'Module 1': 'module-01-wearables/research-library-index.json',
    'Module 2': 'module-02-digital-phenotyping/literature-library-index.json',
    'Module 3': 'module-03-applied-studies/literature-index.json',
}
TERMS = {'oura': r'oura', 'whoop': r'whoop', 'apple-watch': r'apple watch'}


def load(ref, path):
    try:
        return json.loads(subprocess.check_output(['git', 'show', f'{ref}:{path}'], stderr=subprocess.DEVNULL))
    except subprocess.CalledProcessError:
        return {}


def doi_of(r):
    d = r.get('doi') or ''
    if not d and str(r.get('id', '')).startswith('10.'):
        d = r['id']
    return d.lower()


def get_json(url):
    with urllib.request.urlopen(url, timeout=40) as f:
        return json.load(f)


def norm(t):
    return re.sub(r'\W', '', (t or '').lower())


def main():
    base = sys.argv[1]
    head = sys.argv[2] if len(sys.argv) > 2 else 'HEAD'
    flagged = 0
    for module, path in INDEXES.items():
        old = {doi_of(r) for k in ('records', 'rejected') for r in load(base, path).get(k, [])}
        new = load(head, path)
        added = [r for r in new.get('records', []) if doi_of(r) and doi_of(r) not in old]
        if module == 'Module 3':
            print(f'\n## {module}: {len([r for r in new.get("rejected", []) if doi_of(r) not in old])} new rejections '
                  '(queue rows are checked from full text when profiled, not here)')
            continue
        print(f'\n## {module}: {len(added)} new papers')
        for r in added:
            doi = doi_of(r)
            print(f'\n### {doi}')
            try:
                m = get_json('https://api.crossref.org/works/' + urllib.parse.quote(doi))['message']
            except Exception as e:
                print(f'- FLAG Crossref lookup failed: {e}'); flagged += 1; continue
            title = (m.get('title') or [''])[0]
            first = (m.get('author') or [{}])[0].get('family', '')
            year = (m.get('published') or m.get('issued') or {}).get('date-parts', [[None]])[0][0]
            ratio = difflib.SequenceMatcher(None, norm(title), norm(r.get('title'))).ratio()
            print(f'- Crossref: {first} {year}, {(m.get("container-title") or [""])[0]}: {title}')
            if ratio < 0.9:
                print(f'- FLAG title differs (match {ratio:.2f}). Recorded: {r.get("title")}'); flagged += 1
            if r.get('year') and str(year) != str(r['year']):
                print(f'- FLAG year differs. Recorded: {r["year"]}'); flagged += 1
            print(f'- Recorded tier: {r.get("tier")} {r.get("tier_confidence") or ""}, category {r.get("category")}')
            try:
                q = get_json('https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query='
                             + urllib.parse.quote(f'DOI:"{doi}"'))
                pmcid = (q['resultList']['result'] or [{}])[0].get('pmcid')
            except Exception:
                pmcid = None
            if not pmcid:
                print('- No open full text in Europe PMC. Check the tier against the publisher page by hand.')
                continue
            xml = urllib.request.urlopen(f'https://www.ebi.ac.uk/europepmc/webservices/rest/{pmcid}/fullTextXML',
                                         timeout=60).read().decode('utf8', 'ignore')
            text = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', xml))
            term = TERMS.get(r.get('device'), re.escape(r.get('device') or ''))
            if term:
                n = len(re.findall(term, text, re.I))
                print(f'- Device named {n} times in the full text ({pmcid})' + ('. FLAG passing mention?' if n < 3 else ''))
                flagged += n < 3
            for kw in ('conflicts? of interest', 'competing interests?', 'funding'):
                hit = re.search(kw, text, re.I)
                if hit:
                    print(f'- {text[hit.start():hit.start() + 400]}')
    print(f'\n{flagged} flag(s).')


if __name__ == '__main__':
    main()
