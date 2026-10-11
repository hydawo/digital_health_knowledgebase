#!/usr/bin/env python3
"""Print a blank record for a company, with every required field set to unresearched.

    python3 tools/facts/template.py oura > facts/_drafts/oura/A.yaml

Researchers start from this rather than from the existing record, so their work stays independent.
"""
import sys

import yaml

from common import FACTS, field_specs, load_record, load_schema
import os

cid = sys.argv[1]
rec = load_record(os.path.join(FACTS, cid + '.yaml'))
schema = load_schema()
out = {'name': rec['name'], 'kind': rec['kind'], 'profile': rec.get('profile'), 'watch': [],
       'facts': [{'field': f, 'status': 'unresearched', '_asks': desc} for _, f, desc, _ in field_specs(schema, rec['kind'])]}
print(f'# Draft record for {cid}. Fill every field; delete the _asks keys when done. Schema: facts/_schema.yaml')
print(yaml.safe_dump(out, sort_keys=False, allow_unicode=True, width=110))
