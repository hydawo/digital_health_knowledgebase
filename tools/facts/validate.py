#!/usr/bin/env python3
"""Check every vendor fact record against facts/_schema.yaml.

    python3 tools/facts/validate.py            # all records; exit 1 on errors
    python3 tools/facts/validate.py --json     # machine-readable result (used by weekly.py)
    python3 tools/facts/validate.py --file facts/_drafts/oura/A.yaml   # check a draft

Errors break the record (missing required field, bad status, a stated fact with no quote, a
confidence above what its sources allow). Warnings are coverage or housekeeping (unresearched
fields, overdue re-checks, no watched pages).
"""
import datetime
import json
import os
import sys

from common import field_specs, load_records, load_schema

TODAY = datetime.date.today()


def as_date(v):
    if isinstance(v, datetime.date):
        return v
    try:
        return datetime.date.fromisoformat(str(v))
    except Exception:
        return None


def check(company, rec, schema):
    errors, warnings, overdue = [], [], []
    e = lambda m: errors.append(f'{company}: {m}')
    w = lambda m: warnings.append(f'{company}: {m}')
    for key in ('name', 'kind', 'facts'):
        if key not in rec:
            e(f'missing top-level key "{key}"')
    if errors:
        return errors, warnings, overdue
    kind = rec['kind']
    if kind not in ('wearable', 'platform', 'intermediary'):
        e(f'kind "{kind}" must be wearable, platform or intermediary')
    if not rec.get('watch'):
        w('no watched pages')
    for i, wch in enumerate(rec.get('watch') or []):
        if not wch.get('url'):
            e(f'watch[{i}] has no url')
        if wch.get('role') not in schema['watch_roles']:
            e(f'watch[{i}] role "{wch.get("role")}" is not one of {schema["watch_roles"]}')
    facts = rec['facts'] or []
    by_field = {}
    for f in facts:
        by_field.setdefault(f.get('field'), []).append(f)
    statuses, types = schema['statuses'], schema['source_types']
    cap, reg = schema['self_claim_cap'], schema['regulator_only']
    known = set()
    for gname, fname, _, recheck in field_specs(schema, kind):
        known.add(fname)
        entries = by_field.get(fname)
        if not entries:
            e(f'required field "{fname}" missing (use status unresearched or not_applicable)')
            continue
        for f in entries:
            label = fname + (f' [{f["scope"]}]' if f.get('scope') else '')
            st = f.get('status')
            if st not in statuses:
                e(f'{label}: status "{st}" not in {list(statuses)}')
                continue
            if st == 'unresearched':
                w(f'{label}: unresearched')
                continue
            if st == 'not_applicable':
                continue
            if f.get('confidence') not in schema['confidence']:
                e(f'{label}: confidence "{f.get("confidence")}" not in {schema["confidence"]}')
            srcs = f.get('sources') or []
            if not srcs:
                e(f'{label}: status {st} needs at least one source')
            for s in srcs:
                if not s.get('url'):
                    e(f'{label}: a source has no url')
                if s.get('type') not in types:
                    e(f'{label}: source type "{s.get("type")}" not in {list(types)}')
                if not as_date(s.get('retrieved')):
                    e(f'{label}: a source has no valid retrieved date')
            if st in ('stated', 'conflict') and not any(s.get('quote') for s in srcs):
                e(f'{label}: status {st} needs an exact quote in at least one source')
            if st == 'conflict' and len(srcs) < 2:
                e(f'{label}: status conflict needs at least two sources')
            if st == 'stated' and not str(f.get('value', '')).strip():
                e(f'{label}: status stated needs a value')
            stypes = {s.get('type') for s in srcs}
            if st in ('stated', 'conflict') and fname in cap['fields'] and f.get('confidence') == 'Verified' and not stypes & set(cap['independent_types']):
                e(f'{label}: a company statement about itself is capped at {cap["max_without_independent"]} '
                  f'without a source of type {cap["independent_types"]}')
            if st in ('stated', 'conflict') and fname in reg['fields'] and f.get('confidence') == 'Verified' and not stypes & set(reg['verified_requires']):
                e(f'{label}: Verified FDA status needs a regulator_db source')
            due = as_date(f.get('recheck_by'))
            if not due:
                e(f'{label}: recheck_by missing or invalid')
            elif due < TODAY:
                overdue.append(f'{company}: {label} (due {due})')
    for fname in by_field:
        if fname not in known:
            e(f'unknown field "{fname}" for kind {kind}')
    return errors, warnings, overdue


def run(files=None):
    schema = load_schema()
    out = {'errors': [], 'warnings': [], 'overdue': [], 'coverage': {}}
    if files:
        from common import load_record
        recs = {os.path.relpath(f): load_record(f) for f in files}
    else:
        recs = load_records()
    for company, rec in recs.items():
        er, wa, ov = check(company, rec, schema)
        out['errors'] += er
        out['warnings'] += wa
        out['overdue'] += ov
        facts = rec.get('facts') or []
        out['coverage'][company] = {
            'researched': sum(1 for f in facts if f.get('status') not in ('unresearched', None)),
            'total': len(facts)}
    return out


if __name__ == '__main__':
    files = sys.argv[sys.argv.index('--file') + 1:] if '--file' in sys.argv else None
    res = run(files)
    if '--json' in sys.argv:
        print(json.dumps(res, indent=1))
    else:
        for m in res['errors']:
            print('ERROR  ', m)
        for m in res['overdue']:
            print('OVERDUE', m)
        unres = sum(1 for m in res['warnings'] if m.endswith('unresearched'))
        other = [m for m in res['warnings'] if not m.endswith('unresearched')]
        for m in other:
            print('WARN   ', m)
        done = sum(c['researched'] for c in res['coverage'].values())
        tot = sum(c['total'] for c in res['coverage'].values())
        print(f'\n{len(res["coverage"])} companies, {done}/{tot} facts researched, {unres} unresearched, '
              f'{len(res["errors"])} errors, {len(res["overdue"])} overdue.')
    sys.exit(1 if res['errors'] else 0)
