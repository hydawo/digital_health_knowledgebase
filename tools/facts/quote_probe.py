#!/usr/bin/env python3
"""Check that a quote appears on a live page before writing it into a record.

    python3 tools/facts/quote_probe.py URL "exact quote" [--fetch-url ALT_URL]
    python3 tools/facts/quote_probe.py URL --show "keyword"   # print text around a keyword

Prints exact / reworded / missing. Only "exact" quotes belong in a record.
"""
import re
import sys

from common import fetch, match_quote

url = sys.argv[1]
fetch_url = sys.argv[sys.argv.index('--fetch-url') + 1] if '--fetch-url' in sys.argv else url
r = fetch(fetch_url)
if r['status'] != 'ok':
    print(f'{r["status"]}: {r["error"]}')
    sys.exit(2)
text = re.sub(r'\s+', ' ', r['text'] or '')
if sys.argv[2] == '--show':
    for m in list(re.finditer(re.escape(sys.argv[3]), text, re.I))[:5]:
        print('..' + text[max(0, m.start() - 300):m.start() + 300] + '..\n')
    sys.exit(0)
res, ratio = match_quote(sys.argv[2], text)
print(res, ratio)
sys.exit(0 if res == 'exact' else 1)
