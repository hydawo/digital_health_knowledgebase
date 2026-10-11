"""Shared helpers for the vendor fact records: loading, fetching, text extraction, quote matching."""
import difflib
import glob
import hashlib
import html
import json
import os
import re
import subprocess
import tempfile
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
import urllib.robotparser
from html.parser import HTMLParser

import yaml

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
FACTS = os.path.join(ROOT, 'facts')
UA = ('Mozilla/5.0 (compatible; digital-health-kb-fact-monitor/1.0; '
      '+https://github.com/hydawo/digital_health_knowledgebase)')
TIMEOUT = 30
PAUSE = 2.0  # seconds between requests to the same host
# Hosts that answer automated requests with 404 even for live pages (they work in a browser).
# A 404 from these is reported as unreachable, never as dead. Cite a machine-readable route as
# fetch_url where one exists (for FDA records: https://api.fda.gov/device/510k.json?search=k_number:K...).
FALSE_404_HOSTS = {'www.accessdata.fda.gov', 'accessdata.fda.gov'}
# Hosts whose website terms forbid automated collection without written consent, even where robots.txt
# allows it. Never fetched automatically; their sources are listed under "check by hand" instead.
TERMS_BLOCKED_HOSTS = {
    'activinsights.com', 'www.activinsights.com',  # website terms, 2026-10-11 (facts/_drafts/activinsights-geneactiv/judgement.md)
}


def load_schema():
    with open(os.path.join(FACTS, '_schema.yaml'), encoding='utf8') as f:
        return yaml.safe_load(f)


def record_paths():
    return sorted(p for p in glob.glob(os.path.join(FACTS, '*.yaml')) if not os.path.basename(p).startswith('_'))


def load_record(path):
    with open(path, encoding='utf8') as f:
        return yaml.safe_load(f) or {}


def load_records():
    return {os.path.basename(p)[:-5]: load_record(p) for p in record_paths()}


def field_specs(schema, kind):
    """Yield (group, field, description, recheck_days) for the fields that apply to a company kind."""
    for gname, g in schema['groups'].items():
        for fname, spec in g['fields'].items():
            if isinstance(spec, dict):
                if kind not in spec.get('applies_to', []):
                    continue
                text = spec['text']
            else:
                text = spec
            yield gname, fname, text, g['recheck_days']


# ---- text extraction and normalisation ----

class _Text(HTMLParser):
    SKIP = {'script', 'style', 'noscript', 'template', 'svg'}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts, self.skip = [], 0

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self.skip += 1
        elif tag in ('br', 'p', 'div', 'li', 'tr', 'h1', 'h2', 'h3', 'h4', 'td', 'th', 'section'):
            self.parts.append(' ')

    def handle_endtag(self, tag):
        if tag in self.SKIP and self.skip:
            self.skip -= 1

    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)


def html_to_text(raw):
    p = _Text()
    p.feed(raw)
    return ' '.join(p.parts)


def normalize(text):
    """Lower-case, NFKC, straight quotes and hyphens, collapsed whitespace."""
    t = unicodedata.normalize('NFKC', html.unescape(text or ''))
    t = t.replace('‘', "'").replace('’', "'").replace('“', '"').replace('”', '"')
    t = re.sub(r'[‐-―−]', '-', t)
    t = t.replace(' ', ' ')
    return re.sub(r'\s+', ' ', t).strip().lower()


def match_quote(quote, text, threshold=0.9):
    """Return ('exact'|'reworded'|'missing', best ratio)."""
    q, t = normalize(str(quote)), normalize(text)
    if not q:
        return 'missing', 0.0
    if q in t:
        return 'exact', 1.0
    # slide a window of the quote's length over the text, comparing on word boundaries
    words = t.split(' ')
    n = max(1, len(q.split(' ')))
    best = 0.0
    anchors = [w for w in q.split(' ') if len(w) > 4][:3] or q.split(' ')[:1]
    for i, w in enumerate(words):
        if not any(a in w for a in anchors):
            continue
        for j in range(max(0, i - n), i + 1):
            cand = ' '.join(words[j:j + n])
            r = difflib.SequenceMatcher(None, q, cand).ratio()
            if r > best:
                best = r
    return ('reworded' if best >= threshold else 'missing'), round(best, 3)


def fingerprint(text):
    return hashlib.sha256(normalize(text).encode('utf8')).hexdigest()


# ---- fetching ----

_last_hit = {}
_robots = {}


def robots_allows(url):
    parts = urllib.parse.urlsplit(url)
    base = f'{parts.scheme}://{parts.netloc}'
    if base not in _robots:
        rp = urllib.robotparser.RobotFileParser()
        try:
            req = urllib.request.Request(base + '/robots.txt', headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
                rp.parse(r.read().decode('utf8', 'ignore').splitlines())
        except Exception:
            rp = None  # no readable robots.txt: allowed
        _robots[base] = rp
    rp = _robots[base]
    return True if rp is None else rp.can_fetch(UA, url)


def fetch(url, retries=1):
    """Fetch a URL and return a dict: status, http, text (visible text or None), error.

    status is one of ok, unreachable, dead, robots_blocked, terms_blocked.
    """
    host = urllib.parse.urlsplit(url).netloc
    if host in TERMS_BLOCKED_HOSTS:
        return {'status': 'terms_blocked', 'http': None, 'text': None, 'error': "site terms forbid automated collection"}
    if not robots_allows(url):
        return {'status': 'robots_blocked', 'http': None, 'text': None, 'error': 'robots.txt disallows'}
    wait = PAUSE - (time.time() - _last_hit.get(host, 0))
    if wait > 0:
        time.sleep(wait)
    err = None
    for attempt in range(retries + 1):
        _last_hit[host] = time.time()
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept': '*/*'})
            with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
                body = r.read()
                ctype = r.headers.get('Content-Type', '')
            return {'status': 'ok', 'http': 200, 'text': _body_to_text(body, ctype, url), 'error': None}
        except urllib.error.HTTPError as e:
            if e.code == 404 and host == 'api.fda.gov':
                # openFDA answers a search with no results as 404 + {"error": {"code": "NOT_FOUND"}}: a valid negative result
                body = e.read().decode('utf8', 'ignore')
                if 'NOT_FOUND' in body:
                    return {'status': 'ok', 'http': 404, 'text': body, 'error': None}
            if e.code in (404, 410) and host not in FALSE_404_HOSTS:
                return {'status': 'dead', 'http': e.code, 'text': None, 'error': str(e)}
            err = {'status': 'unreachable', 'http': e.code, 'text': None, 'error': str(e)}
        except urllib.error.URLError as e:
            reason = str(getattr(e, 'reason', e))
            if 'nodename nor servname' in reason or 'Name or service not known' in reason:
                return {'status': 'dead', 'http': None, 'text': None, 'error': 'DNS: ' + reason}
            err = {'status': 'unreachable', 'http': None, 'text': None, 'error': reason}
        except Exception as e:  # timeouts, resets
            err = {'status': 'unreachable', 'http': None, 'text': None, 'error': repr(e)}
        time.sleep(PAUSE * (attempt + 1))
    return err


def _body_to_text(body, ctype, url):
    if 'pdf' in ctype or url.lower().endswith('.pdf') or body[:5] == b'%PDF-':
        with tempfile.NamedTemporaryFile(suffix='.pdf') as f:
            f.write(body)
            f.flush()
            try:
                return subprocess.check_output(['pdftotext', '-layout', f.name, '-'], timeout=120).decode('utf8', 'ignore')
            except Exception:
                return ''
    raw = body.decode('utf8', 'ignore')
    if 'json' in ctype or raw.lstrip().startswith(('{', '[')):
        try:
            return json_strings(json.loads(raw))
        except Exception:
            pass
    return html_to_text(raw)


def json_strings(obj):
    """Flatten every string in a JSON document, for JSON-rendered docs (for example Apple's)."""
    out = []

    def walk(o):
        if isinstance(o, str):
            out.append(o)
        elif isinstance(o, dict):
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
    walk(obj)
    return ' '.join(out)


def source_fetch_url(src):
    """A source or watch entry may name a fetch_url (for example a JSON rendering of a JS-only page)."""
    return src.get('fetch_url') or src['url']
