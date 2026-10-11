#!/usr/bin/env python3
"""Weekly vendor-fact check: page fingerprints, quote checks, validation, report, issue text.

    python3 tools/facts/weekly.py [--only oura,withings] [--no-state]

With --only, the report is printed and no report files are written.

Writes facts/_reports/<date>.md, updates facts/_monitor/state.json (fingerprints only, never page
text), and writes facts/_reports/latest-issue.md when there is something to act on. The GitHub
Actions job (.github/workflows/facts-monitor.yml) turns that file into an issue.
"""
import datetime
import json
import os
import sys

from common import FACTS, fetch, fingerprint, load_records, match_quote, source_fetch_url
import validate

TODAY = datetime.date.today().isoformat()
STATE = os.path.join(FACTS, '_monitor', 'state.json')
REPORTS = os.path.join(FACTS, '_reports')
NOISY_AFTER = 3        # consecutive fingerprint changes with every quote intact
CHECK_BY_HAND_AFTER = 2  # consecutive weeks unreachable


def load_state():
    try:
        with open(STATE, encoding='utf8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def main():
    only = None
    if '--only' in sys.argv:
        only = set(sys.argv[sys.argv.index('--only') + 1].split(','))
    keep_state = '--no-state' not in sys.argv
    records = {k: v for k, v in load_records().items() if not only or k in only}
    state = load_state()

    # every URL to fetch: watched pages plus every cited source; remember who cites what
    urls = {}  # url -> {'fetch': fetch_url, 'roles': set, 'quotes': [(company, label, quote)]}
    for company, rec in records.items():
        for wch in rec.get('watch') or []:
            u = urls.setdefault(wch['url'], {'fetch': source_fetch_url(wch), 'roles': set(), 'quotes': [], 'cited_by': set()})
            u['roles'].add(wch.get('role', 'other'))
        for f in rec.get('facts') or []:
            label = f['field'] + (f' [{f["scope"]}]' if f.get('scope') else '')
            for s in f.get('sources') or []:
                if not s.get('url'):
                    continue
                u = urls.setdefault(s['url'], {'fetch': source_fetch_url(s), 'roles': set(), 'quotes': [], 'cited_by': set()})
                u['cited_by'].add(f'{company}: {label}')
                if s.get('quote') and f.get('status') in ('stated', 'conflict'):
                    u['quotes'].append((company, label, s['quote']))

    missing, reworded, changed, dead, by_hand, unreachable, noisy_new = [], [], [], [], [], [], []
    for url, u in sorted(urls.items()):
        r = fetch(u['fetch'])
        st = state.setdefault(url, {})
        st['last_checked'] = TODAY
        st['last_status'] = r['status']
        if r['status'] == 'dead':
            dead.append((url, r['error'], sorted(u['cited_by'])))
            continue
        if r['status'] in ('unreachable', 'robots_blocked'):
            st['unreachable_weeks'] = st.get('unreachable_weeks', 0) + 1
            entry = (url, r['status'] + (f' ({r["http"]})' if r['http'] else '') + f': {r["error"]}', sorted(u['cited_by']))
            (by_hand if st['unreachable_weeks'] >= CHECK_BY_HAND_AFTER or r['status'] == 'robots_blocked' else unreachable).append(entry)
            continue
        st['unreachable_weeks'] = 0
        text = r['text'] or ''
        # Some sites vary their markup between requests; before calling a quote missing, fetch once more.
        if any(match_quote(q, text)[0] == 'missing' for _, _, q in u['quotes']):
            r2 = fetch(u['fetch'])
            if r2['status'] == 'ok' and r2['text']:
                text = text + ' ' + r2['text']
        quotes_ok = True
        for company, label, quote in u['quotes']:
            res, ratio = match_quote(quote, text)
            if res == 'missing':
                quotes_ok = False
                missing.append((url, company, label, quote, ratio))
            elif res == 'reworded':
                reworded.append((url, company, label, quote, ratio))
        fp = fingerprint(text)
        old = st.get('fingerprint')
        st['fingerprint'] = fp
        if old and old != fp:
            st['consecutive_changes'] = st.get('consecutive_changes', 0) + 1
            if quotes_ok and st['consecutive_changes'] >= NOISY_AFTER and not st.get('noisy'):
                st['noisy'] = True
                noisy_new.append(url)
            if not st.get('noisy'):
                changed.append((url, sorted(u['roles']), sorted(u['cited_by'])))
        elif old:
            st['consecutive_changes'] = 0

    val = validate.run()
    if keep_state:
        os.makedirs(os.path.dirname(STATE), exist_ok=True)
        with open(STATE, 'w', encoding='utf8') as f:
            json.dump(state, f, indent=1, sort_keys=True)
            f.write('\n')

    def cites(c):
        return ('; '.join(c[:6]) + (f'; and {len(c) - 6} more' if len(c) > 6 else '')) if c else 'watched page, no facts cite it yet'

    lines = [f'# Vendor fact check, {TODAY}', '',
             f'Checked {len(urls)} pages across {len(records)} companies.', '',
             '| Result | Count |', '|---|---|',
             f'| Quotes missing | {len(missing)} |', f'| Quotes reworded | {len(reworded)} |',
             f'| Pages changed | {len(changed)} |', f'| Dead links | {len(dead)} |',
             f'| Check by hand | {len(by_hand)} |', f'| Unreachable this week | {len(unreachable)} |',
             f'| Overdue re-checks | {len(val["overdue"])} |', f'| Validation errors | {len(val["errors"])} |', '']
    if missing:
        lines += ['## Quotes missing', '', 'The cited text is no longer on the page. Re-check these facts first.', '']
        lines += [f'- **{c}: {lab}**, {url} (best match {ratio:.0%}). Quote: "{q[:200]}"' for url, c, lab, q, ratio in missing] + ['']
    if reworded:
        lines += ['## Quotes reworded', '', 'Close but not exact. Confirm the meaning is unchanged and refresh the quote.', '']
        lines += [f'- {c}: {lab}, {url} ({ratio:.0%} similar)' for url, c, lab, q, ratio in reworded] + ['']
    if changed:
        lines += ['## Pages changed', '', 'The page text changed since last week. Facts that cite it:', '']
        lines += [f'- {url} ({", ".join(roles)}): {cites(c)}' for url, roles, c in changed] + ['']
    if dead:
        lines += ['## Dead links', ''] + [f'- {url}: {err}. Cited by: {cites(c)}' for url, err, c in dead] + ['']
    if by_hand:
        lines += ['## Check by hand', '', 'Blocked to automated fetching. Open these in a browser.', '']
        lines += [f'- {url}: {err}. Cited by: {cites(c)}' for url, err, c in by_hand] + ['']
    if unreachable:
        lines += ['## Unreachable this week', '', 'Will move to "check by hand" if it fails again next week.', '']
        lines += [f'- {url}: {err}' for url, err, c in unreachable] + ['']
    if noisy_new:
        lines += ['## Newly marked noisy', '', 'Changed three weeks running with every quote intact. Now watched through its quotes only.', '']
        lines += [f'- {u}' for u in noisy_new] + ['']
    if val['overdue']:
        lines += ['## Overdue re-checks', ''] + [f'- {m}' for m in val['overdue']] + ['']
    if val['errors']:
        lines += ['## Validation errors', ''] + [f'- {m}' for m in val['errors']] + ['']
    done = sum(c['researched'] for c in val['coverage'].values())
    tot = sum(c['total'] for c in val['coverage'].values())
    lines += ['## Coverage', '', f'{done} of {tot} facts researched across {len(val["coverage"])} companies.', '']
    report = '\n'.join(lines)
    if only:  # a single-company check prints only; it never touches the weekly report files
        print(report)
        return
    os.makedirs(REPORTS, exist_ok=True)
    with open(os.path.join(REPORTS, f'{TODAY}.md'), 'w', encoding='utf8') as f:
        f.write(report)

    actionable = len(missing) + len(reworded) + len(changed) + len(dead) + len(by_hand) + len(val['overdue']) + len(val['errors'])
    issue = os.path.join(REPORTS, 'latest-issue.md')
    if actionable:
        with open(issue, 'w', encoding='utf8') as f:
            f.write(f'Vendor facts: {actionable} to re-check ({TODAY})\n')
            f.write('\n'.join(lines[2:]) + f'\n\nFull report: `facts/_reports/{TODAY}.md`. '
                    'How to work this: `facts/README.md`, "Re-check loop".\n')
    elif os.path.exists(issue):
        os.remove(issue)
    print(report)


if __name__ == '__main__':
    main()
