#!/usr/bin/env python3
"""Generate the comparison tables and data files from the vendor fact records.

    python3 tools/facts/generate.py          # write outputs
    python3 tools/facts/generate.py --check  # exit 1 if any output differs from what is committed

Outputs:
  facts/_generated/research-and-access.md   one table per field group, a row per company
  facts/_generated/facts.json               flattened facts, for explorer/build.py and the atlas
  profiles: the text between "<!-- facts:begin -->" and "<!-- facts:end -->" in a company's profile,
            only where those markers exist (a profile opts in once its record is fully researched)
Never edit generated text by hand; change the record and re-run.
"""
import json
import os
import re
import sys

from common import FACTS, ROOT, field_specs, load_records, load_schema

OUT = os.path.join(FACTS, '_generated')
MARK = re.compile(r'(<!-- facts:begin(?: [^>]*)? -->)(.*?)(<!-- facts:end -->)', re.S)
CONF = {'Verified': 'V', 'Corroborated': 'C', 'Reported': 'R', 'Unclear': 'U'}
STATUS_TEXT = {'not_public': 'Not public', 'unclear': 'Unclear', 'not_applicable': 'n/a', 'unresearched': '·'}


def cell(entries, md=True):
    parts = []
    for f in entries:
        st = f.get('status')
        scope = f'**{f["scope"]}:** ' if f.get('scope') and md else (f'{f["scope"]}: ' if f.get('scope') else '')
        if st in ('stated', 'conflict'):
            v = str(f.get('value', '')).strip().replace('|', '/').replace('\n', ' ')
            mark = CONF.get(f.get('confidence'), '?')
            date = max((str(s.get('retrieved', '')) for s in f.get('sources') or []), default='')
            tag = ' (conflict)' if st == 'conflict' else ''
            parts.append(f'{scope}{v}{tag} [{mark}, {date}]')
        else:
            date = max((str(s.get('retrieved', '')) for s in f.get('sources') or []), default='')
            parts.append(f'{scope}{STATUS_TEXT.get(st, st)}' + (f' [{date}]' if date and st == 'not_public' else ''))
    return '<br>'.join(parts) if md else '; '.join(parts)


def build(records, schema):
    order = sorted(records, key=lambda c: (records[c].get('kind', ''), records[c].get('name', c).lower()))
    lines = ['# Research programs, pricing, data access and compliance', '',
             'Generated from `facts/*.yaml` by `tools/facts/generate.py`. Do not edit by hand.', '',
             'Each cell gives the value, then [confidence, date retrieved]. Confidence: V Verified, '
             'C Corroborated, R Reported, U Unclear. "·" means not yet researched; "Not public" means searched '
             'and not published as of the date shown.', '']
    flat = []
    for gname, g in schema['groups'].items():
        for kind_label, kinds in (('Wearables and intermediaries', ('wearable', 'intermediary')), ('Phone platforms', ('platform',))):
            comps = [c for c in order if records[c].get('kind') in kinds]
            fields = []
            for c in comps:
                for gg, f, desc, _ in field_specs(schema, records[c]['kind']):
                    if gg == gname and (f, desc) not in fields:
                        fields.append((f, desc))
            if not comps or not fields:
                continue
            lines += [f'## {g["label"]}: {kind_label.lower()}', '',
                      '| Company | ' + ' | '.join(f for f, _ in fields) + ' |',
                      '|---|' + '---|' * len(fields)]
            for c in comps:
                rec = records[c]
                by = {}
                for f in rec.get('facts') or []:
                    by.setdefault(f['field'], []).append(f)
                row = [f'[{rec.get("name", c)}](../{c}.yaml)']
                for f, _ in fields:
                    row.append(cell(by.get(f, [])) if f in by else '')
                lines.append('| ' + ' | '.join(row) + ' |')
            lines.append('')
    for c in order:
        for f in records[c].get('facts') or []:
            flat.append({'company': c, 'name': records[c].get('name'), 'kind': records[c].get('kind'), **{
                k: (str(v) if k == 'recheck_by' else v) for k, v in f.items() if k != 'sources'},
                'sources': [{k: str(v) if k == 'retrieved' else v for k, v in s.items()} for s in f.get('sources') or []]})
    return '\n'.join(lines) + '\n', json.dumps(flat, indent=1, ensure_ascii=False, default=str) + '\n'


def profile_block(rec, schema):
    by = {}
    for f in rec.get('facts') or []:
        by.setdefault(f['field'], []).append(f)
    out = ['', '*Generated from the fact record by `tools/facts/generate.py`. Edit the record, not this block.*', '']
    for gname, g in schema['groups'].items():
        rows = [(f, desc) for gg, f, desc, _ in field_specs(schema, rec['kind']) if gg == gname]
        out += [f'**{g["label"]}**', '', '| Fact | Value |', '|---|---|']
        out += [f'| {desc} | {cell(by.get(f, []))} |' for f, desc in rows] + ['']
    return '\n'.join(out)


def main():
    check = '--check' in sys.argv
    schema, records = load_schema(), load_records()
    md, js = build(records, schema)
    targets = {os.path.join(OUT, 'research-and-access.md'): md, os.path.join(OUT, 'facts.json'): js}
    for c, rec in records.items():
        prof = rec.get('profile')
        if not prof:
            continue
        p = os.path.join(ROOT, prof)
        if not os.path.exists(p):
            continue
        # a profile shared by several records is updated cumulatively, not re-read from disk each time
        text = targets[p] if p in targets else open(p, encoding='utf8').read()
        # a shared profile (for example data-intermediaries.md) can hold several blocks: <!-- facts:begin fitabase -->
        def repl(m, c=c, rec=rec):
            tag = m.group(1)
            if ' ' in tag[len('<!-- facts:begin'):-4].strip() and c not in tag:
                return m.group(0)
            if tag.strip() != '<!-- facts:begin -->' and c not in tag:
                return m.group(0)
            return m.group(1) + profile_block(rec, schema) + '\n' + m.group(3)
        new = MARK.sub(repl, text)
        if new != text or p in targets:
            targets[p] = new
    stale = []
    for path, content in targets.items():
        old = open(path, encoding='utf8').read() if os.path.exists(path) else None
        if old != content:
            stale.append(os.path.relpath(path, ROOT))
            if not check:
                os.makedirs(os.path.dirname(path), exist_ok=True)
                with open(path, 'w', encoding='utf8') as f:
                    f.write(content)
    if check:
        if stale:
            print('Generated files are out of date or were edited by hand:\n  ' + '\n  '.join(stale) +
                  '\nRun: python3 tools/facts/generate.py')
            sys.exit(1)
        print('Generated files are current.')
    else:
        print(f'{len(stale)} file(s) written.' if stale else 'Nothing to change.')


if __name__ == '__main__':
    main()
