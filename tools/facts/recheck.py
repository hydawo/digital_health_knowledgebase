"""Roll a fact's recheck_by date forward when this week's check shows its evidence is unchanged.

Used by weekly.py. A fact qualifies only when all of these hold:
- status is `stated` (absence, conflict and judgement calls are never confirmed by a quote);
- it falls due within DUE_WINDOW days, or is overdue;
- no source is an Internet Archive capture (archived text never changes, so it proves nothing);
- at least one source has a quote, every quote matched exactly this week, and every source page was
  reachable (or, for an `expect_absent` source, gone as expected);
- a person or agent read the sources within MAX_UNREAD recheck intervals (the latest `retrieved`
  date), so the monitor can extend a fact about twice before it goes back to a real re-read.

The new date is today plus the field's recheck_days from the schema. Only the `recheck_by` line of
each fact changes; the file is otherwise left byte for byte as it was, and the edit is verified by
reloading the record.
"""
import datetime
import re

import yaml

DUE_WINDOW = 14
MAX_UNREAD = 3


def _date(v):
    try:
        return datetime.date.fromisoformat(str(v))
    except Exception:
        return None


def source_key(s, fetch_url):
    return (s['url'], fetch_url(s))


def eligible(f, recheck_days, today, page_ok, quote_exact, fetch_url):
    """Return the new recheck_by date for fact f, or None if it does not qualify.

    page_ok(key) -> bool, quote_exact(key, quote) -> bool, where key is (url, fetch_url)."""
    if f.get('status') != 'stated':
        return None
    due = _date(f.get('recheck_by'))
    if not due or due > today + datetime.timedelta(days=DUE_WINDOW):
        return None
    srcs = f.get('sources') or []
    if not srcs or any('web.archive.org' in str(s.get('url', '')) + str(s.get('fetch_url', '')) for s in srcs):
        return None
    read = [d for d in (_date(s.get('retrieved')) for s in srcs) if d]
    if not read or max(read) < today - datetime.timedelta(days=MAX_UNREAD * recheck_days):
        return None
    if not any(s.get('quote') for s in srcs):
        return None
    for s in srcs:
        key = source_key(s, fetch_url)
        if not page_ok(key):
            return None
        if s.get('quote') and not quote_exact(key, str(s['quote'])):
            return None
    new = today + datetime.timedelta(days=recheck_days)
    return new if new > due else None


def write_dates(path, updates):
    """Set recheck_by for the facts at the given list indexes. updates: {index: date}.

    Returns the number of facts changed. Raises ValueError, leaving the file untouched, if the
    layout is not the one the records use or the reloaded record differs anywhere else."""
    with open(path, encoding='utf8') as fh:
        text = fh.read()
    before = yaml.safe_load(text)
    lines = text.split('\n')
    try:
        start = lines.index('facts:')
    except ValueError:
        raise ValueError(f'{path}: no top-level "facts:" line')
    starts = [i for i in range(start + 1, len(lines)) if lines[i].startswith('- field: ')]
    if len(starts) != len(before['facts']):
        raise ValueError(f'{path}: found {len(starts)} fact lines for {len(before["facts"])} facts')
    bounds = starts + [next((i for i in range(starts[-1] + 1, len(lines)) if lines[i] and not lines[i].startswith((' ', '-'))), len(lines))]
    for idx, new in updates.items():
        hits = [i for i in range(bounds[idx], bounds[idx + 1]) if re.match(r'^  recheck_by: ', lines[i])]
        if len(hits) != 1:
            raise ValueError(f'{path}: fact {idx} has {len(hits)} recheck_by lines')
        if re.search(r'[&*]', lines[hits[0]].split(':', 1)[1]):
            raise ValueError(f'{path}: fact {idx} recheck_by uses a YAML anchor or alias')
        lines[hits[0]] = f"  recheck_by: '{new.isoformat()}'"
    out = '\n'.join(lines)
    after = yaml.safe_load(out)
    expect = yaml.safe_load(text)
    for idx, new in updates.items():
        expect['facts'][idx]['recheck_by'] = new.isoformat()
    for f in after['facts']:
        f['recheck_by'] = str(f.get('recheck_by'))
    for f in expect['facts']:
        f['recheck_by'] = str(f.get('recheck_by'))
    if after != expect:
        raise ValueError(f'{path}: reloaded record differs beyond recheck_by; not written')
    with open(path, 'w', encoding='utf8') as fh:
        fh.write(out)
    return len(updates)
