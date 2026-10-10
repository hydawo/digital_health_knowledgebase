#!/usr/bin/env python3
"""Create starter records (facts/<company>.yaml) for every company, without overwriting existing ones.

    python3 tools/facts/seed.py

Each starter record lists every required field with status "unresearched", and a watch list built
from the URLs the company's profile and sources.md already cite on the company's own domains. The
baseline research run then replaces "unresearched" with researched facts.
"""
import os
import re
import urllib.parse

import yaml

from common import FACTS, ROOT, field_specs, load_schema

M1, M2 = 'module-01-wearables/profiles/', 'module-02-digital-phenotyping/profiles/'
# id: (name, kind, profile, domains)
COMPANIES = {
    'apple': ('Apple (Apple Watch, HealthKit, SensorKit, ResearchKit)', 'wearable', M1 + 'apple-watch-healthkit.md',
              ['apple.com', 'researchandcare.org']),
    'fitbit-google': ('Fitbit / Google Health API', 'wearable', M1 + 'fitbit-google.md',
                      ['fitbit.com', 'developers.google.com', 'support.google.com', 'store.google.com']),
    'garmin': ('Garmin', 'wearable', M1 + 'garmin.md', ['garmin.com']),
    'samsung': ('Samsung (Galaxy Watch, Health Sensor SDK, Research Stack)', 'wearable', M1 + 'samsung.md',
                ['samsung.com', 'github.com/S-HealthStack']),
    'withings': ('Withings', 'wearable', M1 + 'withings.md', ['withings.com']),
    'polar': ('Polar', 'wearable', M1 + 'polar.md', ['polar.com', 'github.com/polarofficial']),
    'oura': ('Oura', 'wearable', M1 + 'oura.md', ['ouraring.com', 'apps.apple.com/us/app/oura']),
    'whoop': ('WHOOP', 'wearable', M1 + 'whoop.md', ['whoop.com']),
    'empatica': ('Empatica', 'wearable', M1 + 'empatica.md', ['empatica.com']),
    'ametris-actigraph': ('Ametris (ActiGraph), a Signant Health company', 'wearable', M1 + 'ametris-actigraph.md',
                          ['ametris.com', 'actigraphcorp.com', 'github.com/actigraph', 'signanthealth.com']),
    'axivity': ('Axivity', 'wearable', M1 + 'axivity-geneactiv.md', ['axivity.com', 'github.com/openmovementproject', 'github.com/digitalinteraction']),
    'activinsights-geneactiv': ('Activinsights (GENEActiv)', 'wearable', M1 + 'axivity-geneactiv.md', ['activinsights.com', 'geneactiv.com']),
    'movesense': ('Movesense', 'wearable', M1 + 'movesense.md', ['movesense.com', 'bitbucket.org/movesense']),
    'ultrahuman': ('Ultrahuman', 'wearable', M1 + 'emerging-platforms.md', ['ultrahuman.com']),
    'sensor-bio': ('Sensor Bio (formerly Biostrap)', 'wearable', M1 + 'emerging-platforms.md', ['biostrap.com', 'sensorbio.com']),
    'ringconn': ('RingConn', 'wearable', M1 + 'emerging-platforms.md', ['ringconn.com']),
    'circular': ('Circular', 'wearable', M1 + 'emerging-platforms.md', ['circular.xyz']),
    'zepp-amazfit': ('Zepp Health (Amazfit)', 'wearable', M1 + 'emerging-platforms.md', ['zepp.com', 'amazfit.com']),
    'verily': ('Verily (Study Watch)', 'wearable', M1 + 'emerging-platforms.md', ['verily.com']),
    'fitabase': ('Fitabase', 'intermediary', M1 + 'data-intermediaries.md', ['fitabase.com']),
    'labfront': ('Labfront', 'intermediary', M1 + 'data-intermediaries.md', ['labfront.com', 'labfront.io']),
    'fitrockr': ('Fitrockr', 'intermediary', M1 + 'data-intermediaries.md', ['fitrockr.com']),
    'terra': ('Terra', 'intermediary', M1 + 'data-intermediaries.md', ['tryterra.co']),
    'thryve': ('Thryve', 'intermediary', M1 + 'data-intermediaries.md', ['thryve.health']),
    'beiwe': ('Beiwe and Forest (Onnela Lab, Beiwe Service Center)', 'platform', M2 + 'beiwe.md',
              ['beiwe.org', 'github.com/onnela-lab', 'hsph.harvard.edu']),
    'radar-base': ('RADAR-base (and The Hyve hosting)', 'platform', M2 + 'radar-base.md', ['radar-base.org', 'github.com/RADAR-base', 'thehyve.nl']),
    'mindlamp': ('mindLAMP (BIDMC Division of Digital Psychiatry)', 'platform', M2 + 'mindlamp.md',
                 ['lamp.digital', 'digitalpsych.org', 'github.com/BIDMCDigitalPsychiatry']),
    'aware': ('AWARE Framework', 'platform', M2 + 'aware-framework.md', ['awareframework.com', 'github.com/awareframework', 'github.com/tetujin']),
    'avicenna': ('Avicenna Research (formerly Ethica)', 'platform', M2 + 'avicenna-research-ethica.md', ['avicennaresearch.com', 'ethicadata.com']),
    'metricwire': ('MetricWire', 'platform', M2 + 'metricwire.md', ['metricwire.com']),
    'm-path': ('m-Path (KU Leuven)', 'platform', M2 + 'm-path.md', ['m-path.io']),
    'carp': ('CARP Mobile Sensing (DTU)', 'platform', M2 + 'carp-mobile-sensing.md', ['carp.dk', 'github.com/carp-dk', 'pub.dev']),
    'lifedata': ('LifeData (RealLife Exp)', 'platform', M2 + 'lifedata.md', ['lifedatacorp.com', 'lifedata']),
    'evidation': ('Evidation', 'platform', M2 + 'evidation.md', ['evidation.com']),
    'purple-robot': ('Purple Robot (Northwestern CBITS)', 'platform', M2 + 'legacy-and-adjacent-platforms.md',
                     ['github.com/cbitstech', 'phidatalab.org']),
}

ROLE_RULES = [
    ('regulatory', ['accessdata.fda.gov', 'api.fda.gov', 'fda.gov']),
    ('app_store', ['apps.apple.com', 'itunes.apple.com', 'play.google.com']),
    ('repository', ['github.com', 'bitbucket.org', 'cran.r-project.org', 'pub.dev', 'pypi.org']),
    ('pricing', ['pricing', 'price', '/store', '/plans', 'membership', 'shop', '/product']),
    ('terms', ['terms', 'legal', 'agreement', 'privacy', 'license', 'licence', 'policies', 'policy']),
    ('trust', ['trust', 'security', 'compliance', 'hipaa', 'gdpr']),
    ('research_program', ['research', 'academic', 'organizations', 'grant', 'science']),
    ('developer_program', ['developer', 'partner', 'program', 'onboard']),
    ('changelog', ['changelog', 'release', 'whats-new', 'news', 'blog']),
    ('docs', ['docs', 'documentation', 'api', 'sdk', 'guide', 'reference', 'wiki']),
]


def role_for(url):
    u = url.lower()
    for role, keys in ROLE_RULES:
        if any(k in u for k in keys):
            return role
    return 'other'


def urls_for(domains, texts):
    found = []
    for t in texts:
        for u in re.findall(r'https?://[^\s<>()\[\]|`"\'*]+', t):
            u = u.rstrip('.,;:')
            host_path = urllib.parse.urlsplit(u).netloc + urllib.parse.urlsplit(u).path
            if any(d in host_path for d in domains) and u not in found:
                found.append(u)
    return found


def main():
    schema = load_schema()
    sources = {}
    for m in ('module-01-wearables', 'module-02-digital-phenotyping'):
        p = os.path.join(ROOT, m, 'sources.md')
        if os.path.exists(p):
            sources[m] = open(p, encoding='utf8').read()
    made = 0
    for cid, (name, kind, profile, domains) in COMPANIES.items():
        path = os.path.join(FACTS, cid + '.yaml')
        if os.path.exists(path):
            continue
        prof = open(os.path.join(ROOT, profile), encoding='utf8').read()
        urls = urls_for(domains, [prof, sources.get(profile.split('/')[0], '')])
        watch = [{'url': u, 'role': role_for(u)} for u in urls[:15]]
        facts = [{'field': f, 'status': 'unresearched'} for _, f, _, _ in field_specs(schema, kind)]
        rec = {'name': name, 'kind': kind, 'profile': profile, 'watch': watch, 'facts': facts}
        with open(path, 'w', encoding='utf8') as fh:
            fh.write(f'# Vendor fact record. Schema: facts/_schema.yaml. How to work it: facts/README.md.\n')
            yaml.safe_dump(rec, fh, sort_keys=False, allow_unicode=True, width=110)
        made += 1
    print(f'{made} starter records created in facts/')


if __name__ == '__main__':
    main()
