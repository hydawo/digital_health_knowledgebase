#!/usr/bin/env python3
"""Regenerate the data block and header stats of explorer/kb-explorer.html from the repository.

Run from the repository root after any profile, PDF or literature-folder change:
    python3 explorer/build.py
It rewrites only the region between /*DATA-START*/ and /*DATA-END*/ and the four header stats.
The M1, M2 and M3 arrays (one row per write-up) are edited by hand in the HTML.
"""
import os, re, json, glob, subprocess

P = 'explorer/kb-explorer.html'
REPO = 'https://github.com/hydawo/digital_health_knowledgebase/blob/main/'

def label(f):
    parts = f[:-4].split('-'); year = parts[0] if parts[0].isdigit() else ''; rest = parts[1:] if year else parts
    author = rest[0].capitalize() if rest else ''; journal = rest[1] if len(rest) > 1 else ''
    title = ' '.join(rest[2:]) if len(rest) > 2 else ''
    return (f"{author} {year}" + (f", {journal}" if journal else '') + (f". {title}" if title else '')).strip()

papers = {}
for mod in ['module-01-wearables', 'module-02-digital-phenotyping']:
    for d in sorted(glob.glob(mod + '/literature/*')):
        if os.path.isdir(d):
            papers[os.path.basename(d)] = [[label(f), d + '/' + f] for f in sorted(os.listdir(d)) if f.lower().endswith('.pdf')]
d = 'module-04-methods-and-reviews/literature'
papers['methods-and-reviews'] = [[label(f), d + '/' + f] for f in sorted(os.listdir(d)) if f.endswith('.pdf')] if os.path.isdir(d) else []

# Which literature folders and which Module 3 filter keys belong to each Module 1/2 write-up.
M1MAP = {'apple-watch-healthkit': (['apple-watch'], ['apple']), 'oura': (['oura'], ['oura']), 'whoop': (['whoop'], ['whoop']),
         'fitbit-google': (['fitbit'], ['fitbit']), 'ametris-actigraph': (['research-accelerometers'], ['actigraph']),
         'axivity-geneactiv': (['research-accelerometers'], ['axivity']), 'garmin': ([], ['garmin']), 'samsung': ([], ['samsung']),
         'withings': ([], ['withings']), 'movesense': ([], ['movesense']), 'empatica': ([], ['empatica']), 'polar': ([], [])}
M2MAP = {'beiwe': (['beiwe'], ['beiwe']), 'radar-base': (['radar-base'], ['radar']), 'mindlamp': (['mindlamp'], ['mindlamp']),
         'aware-framework': (['aware-framework'], ['aware']), 'avicenna-research-ethica': (['avicenna-research-ethica'], ['avicenna']),
         'metricwire': ([], ['metricwire']), 'm-path': (['m-path'], ['mpath']), 'lifedata': (['lifedata'], ['lifedata']),
         'carp-mobile-sensing': (['carp-mobile-sensing'], ['carp']),
         'legacy-and-adjacent-platforms': (['legacy-and-adjacent-platforms', 'mindful-moods', 'vaping-health-study-app'], [])}
# Any literature folder not claimed above is reported so it is not silently invisible.
claimed = {k for v in list(M1MAP.values()) + list(M2MAP.values()) for k in v[0]} | {'methods-and-reviews'}
for k in papers:
    if k not in claimed: print('WARNING: literature folder not mapped to any write-up:', k)

# ---- citations from the catalogues ----
CAT_ORDER = [('deployment-profiled', 'Deployments profiled in Module 3'), ('deployment-folded', 'Same-cohort papers folded into a Module 3 profile'),
             ('applied-unscreened', 'Applied studies not yet profiled'), ('applied-rejected', 'Applied studies screened out of Module 3'),
             ('validation', 'Validation studies'), ('methods', 'Methods and analytics'), ('platform', 'Platform papers'),
             ('protocol', 'Protocols'), ('review', 'Reviews and commentary')]
led = json.load(open('module-03-applied-studies/literature-index.json'))
prof = {r['doi'].lower(): r for r in led['records']}; rej = {r['doi'].lower(): r for r in led['rejected']}
hand = {k.lower(): v for k, v in json.load(open('explorer/paper-categories.json')).items()}
VAL = re.compile(r'validat|accuracy|agreement|polysomnograph|bland|criterion|reliabilit|concordance', re.I)
REV = re.compile(r'\breview\b|meta-analys|scoping|consensus|perspective|opportunities and challenges|new dimensions|harnessing|commentary|implications|realizing the potential|busy psychiatrist|digitally connected|methodology and reporting|limited evidence|bridging boundaries|decision models|machine learning and the digital', re.I)
METH = re.compile(r'imput|algorithm|recogni|classif|step count|sample size|statistical|anomaly|movelet|walking|gyroscope|estimation|inference|missingness in digital|acoustic feature|causal effect', re.I)
PLAT = re.compile(r'\bplatform\b|new tools for new research|framework\b|infrastructure|software', re.I)
def category(title, doi, struck):
    d = (doi or '').lower()
    if struck: return 'removed'
    if d in hand: return hand[d]
    if d in prof: return 'deployment-profiled'
    if d in rej:
        r = rej[d]['reason']
        return {'duplicate-cohort': 'deployment-folded', 'validation': 'validation', 'review': 'review', 'no-cohort': 'applied-rejected',
                'protocol': 'protocol', 'unobtainable': 'applied-unscreened',
                'architecture': ('platform' if PLAT.search(title) else 'methods')}[r]
    if REV.search(title): return 'review'
    if METH.search(title): return 'methods'
    if PLAT.search(title) and not VAL.search(title): return 'platform'
    if VAL.search(title): return 'validation'
    return 'applied-unscreened'
SECTION_FOLDER = {'Beiwe': 'beiwe', 'RADAR-base': 'radar-base', 'mindLAMP': 'mindlamp', 'AWARE Framework': 'aware-framework',
                  'Avicenna Research (Ethica)': 'avicenna-research-ethica', 'MetricWire': 'metricwire', 'm-Path': 'm-path',
                  'CARP Mobile Sensing': 'carp-mobile-sensing', 'Legacy and adjacent platforms': 'legacy-and-adjacent-platforms',
                  'Oura': 'oura', 'WHOOP': 'whoop', 'Apple Watch': 'apple-watch'}
cites = {}
def add(folder, c):
    cites.setdefault(folder, []).append(c)
for lib in ['module-01-wearables/literature-library.md', 'module-02-digital-phenotyping/literature-library.md', 'module-04-methods-and-reviews/literature-library.md']:
    top = ''; mod4 = lib.startswith('module-04')
    for l in open(lib, encoding='utf8').read().split('\n'):
        if l.startswith('## '): top = l[3:].strip()
        if not l.startswith('|'): continue
        c = [x.strip() for x in l.split('|')]
        if len(c) < 6 or c[1] in ('Title', '#') or set(c[1]) <= set('- '): continue
        idrow = bool(re.match(r'~*(L|M4-)\d+~*$', c[1])) or (mod4 and re.match(r'~*[LM]', c[1]))
        struck = c[1].startswith('~~')
        title, authors, venue = (c[2], c[3], c[4]) if idrow else (c[1], c[2], c[3])
        doi_m = re.search(r'10\.\d{4,9}/[^\s\)\]|]+', l); doi = doi_m.group(0).rstrip('.') if doi_m else ''
        if not doi and 'http' not in l: continue
        url_m = re.search(r'\((https?://[^)\s]+)\)', l); url = url_m.group(1) if url_m else ('https://doi.org/' + doi if doi else '')
        pdf_m = re.search(r'(module-0\d-[^)\s|`]+/literature/[^)\s|`]+\.pdf|literature/[^)\s|`]+\.pdf)', l)
        pdf = pdf_m.group(1) if pdf_m else ''
        if pdf and pdf.startswith('literature/'): pdf = lib.split('/')[0] + '/' + pdf
        oa = 'Verified OA' if 'Verified OA' in l else ('Paywalled' if 'Paywalled' in l else ('Preprint OA' if 'Preprint' in l else ('OA, not obtained' if 'not obtained' in l else '')))
        cat = 'review' if mod4 else category(title, doi, struck)
        rec = {'t': title, 'a': authors, 'v': venue, 'doi': doi, 'url': url, 'pdf': pdf, 'oa': oa, 'cat': cat,
               'profile': prof[doi.lower()]['slug'] if doi.lower() in prof else ''}
        if cat == 'removed': continue
        if not mod4 and 'module-04-' in pdf: continue  # moved to Module 4; its catalogue is the source
        if mod4: add('methods-and-reviews', rec); continue
        folder = ''
        if pdf: folder = pdf.split('/literature/')[1].split('/')[0]
        elif top in SECTION_FOLDER: folder = SECTION_FOLDER[top]
        if folder: add(folder, rec)
for k in cites:
    seen = set(); uniq = []
    for r in cites[k]:
        key = r['doi'].lower() or r['t'].lower()
        if key in seen: continue
        seen.add(key); uniq.append(r)
    cites[k] = uniq
print('citations per folder:', {k: len(v) for k, v in cites.items()})

profiles = {}
for mod in ['module-01-wearables', 'module-02-digital-phenotyping']:
    for f in sorted(glob.glob(mod + '/profiles/*.md')):
        profiles[os.path.basename(f)[:-3]] = open(f, encoding='utf8').read()

s = open(P, encoding='utf8').read()
block = ("/*DATA-START*/\nvar REPO='" + REPO + "';\nvar PAPERS=" + json.dumps(papers, ensure_ascii=False) +
         ";\nvar M1MAP=" + json.dumps(M1MAP) + ";\nvar M2MAP=" + json.dumps(M2MAP) +
         ";\nvar PROFILES=" + json.dumps(profiles, ensure_ascii=False) + ";\nvar CITES=" + json.dumps(cites, ensure_ascii=False) +
         ";\nvar CAT_ORDER=" + json.dumps(CAT_ORDER) + ";\n/*DATA-END*/\n")
s = re.sub(r"/\*DATA-START\*/.*?/\*DATA-END\*/\n", lambda m: block, s, count=1, flags=re.S)

pdfs = len([f for f in glob.glob('**/*.pdf', recursive=True) if not f.startswith('.git')])
docs = len([f for f in glob.glob('**/*.md', recursive=True) if not f.startswith('.git') and not f.startswith('.claude')])
total = int(subprocess.run(['du', '-sk', '.'], capture_output=True, text=True).stdout.split()[0])
git = int(subprocess.run(['du', '-sk', '.git'], capture_output=True, text=True).stdout.split()[0])
s = re.sub(r'<div class="stat"><b>\d+</b><span>papers stored</span></div>', '<div class="stat"><b>%d</b><span>papers stored</span></div>' % pdfs, s)
s = re.sub(r'<div class="stat"><b>\d+</b><span>documents</span></div>', '<div class="stat"><b>%d</b><span>documents</span></div>' % docs, s)
s = re.sub(r'<div class="stat"><b>[^<]*</b><span>on disk</span></div>', '<div class="stat"><b>%d MB</b><span>on disk</span></div>' % ((total - git) // 1024), s)
m4 = len(papers['methods-and-reviews'])
s = re.sub(r'Module 4 &middot; \d+ papers', 'Module 4 &middot; %d papers' % m4, s)
open(P, 'w', encoding='utf8').write(s)
print('papers:', {k: len(v) for k, v in papers.items()})
print('profiles embedded:', len(profiles), '| pdfs', pdfs, '| docs', docs, '| page bytes', len(s.encode('utf8')))
