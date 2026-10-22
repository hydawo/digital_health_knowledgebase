#!/usr/bin/env python3
"""Print the "what we have on record" part of a vendor confirmation sheet, from a fact record.

    python3 tools/facts/confirm_sheet.py COMPANY

Lists every researched fact except not_applicable ones, numbered so the vendor can answer by number,
grouped as in the schema, with status, confidence and the first source. The cover note and the
questions only the vendor can answer are written by hand around this output. A written answer goes
back into the record as a source of type vendor_confirmation (facts/README.md).
"""
import sys

from common import field_specs, load_record, load_schema, FACTS
import os

STATUS = {'stated': 'Published', 'not_public': 'Not found in public sources', 'unclear': 'Unclear',
          'conflict': 'Sources disagree', 'unresearched': 'Not yet researched'}


def main():
    if len(sys.argv) != 2 or sys.argv[1] in ('-h', '--help'):
        print(__doc__)
        return
    company = sys.argv[1]
    rec = load_record(os.path.join(FACTS, f'{company}.yaml'))
    schema = load_schema()
    by_field = {}
    for f in rec.get('facts') or []:
        by_field.setdefault(f['field'], []).append(f)
    out, n, group = [], 0, None
    for gname, fname, text, _ in field_specs(schema, rec['kind']):
        for f in by_field.get(fname, []):
            if f.get('status') in ('not_applicable', 'unresearched'):
                continue
            if gname != group:
                group = gname
                out += ['', f'### {schema["groups"][gname]["label"]}', '']
            n += 1
            label = text + (f' ({f["scope"]})' if f.get('scope') else '')
            value = ' '.join(str(f.get('value') or '').split()) or 'Nothing found.'
            src = next((s['url'] for s in f.get('sources') or [] if s.get('url')), None)
            out.append(f'{n}. **{label}.** {value}')
            out.append(f'   Recorded as: {STATUS.get(f["status"], f["status"])}'
                       + (f', confidence {f["confidence"]}' if f.get('confidence') else '')
                       + (f'. Source: {src}' if src else '') + '.')
            out.append('   Your answer: correct / correction:')
            out.append('')
    print(f'## What I have on record for {rec["name"]}\n')
    print(f'{n} items, from the public record dated {max(str(s.get("retrieved")) for f in rec["facts"] for s in f.get("sources") or [] if s.get("retrieved"))}.')
    print('\n'.join(out).rstrip())


if __name__ == '__main__':
    main()
