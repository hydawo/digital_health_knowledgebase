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

profiles = {}
for mod in ['module-01-wearables', 'module-02-digital-phenotyping']:
    for f in sorted(glob.glob(mod + '/profiles/*.md')):
        profiles[os.path.basename(f)[:-3]] = open(f, encoding='utf8').read()

s = open(P, encoding='utf8').read()
block = ("/*DATA-START*/\nvar REPO='" + REPO + "';\nvar PAPERS=" + json.dumps(papers, ensure_ascii=False) +
         ";\nvar M1MAP=" + json.dumps(M1MAP) + ";\nvar M2MAP=" + json.dumps(M2MAP) +
         ";\nvar PROFILES=" + json.dumps(profiles, ensure_ascii=False) + ";\n/*DATA-END*/\n")
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
