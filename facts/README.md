# Vendor fact records

**Built 2026-10-10.** One record per company (35 of them) holding the facts a study team decides
on: research programs, pricing, data access and terms, and compliance. Every fact carries the page it
came from, the exact words that support it, the date it was read, a confidence label and a re-check
date. Built after an independent review found 140 wrong claims, most of them vendor facts that had
gone stale.

## Files

| Path | What it is |
|---|---|
| `facts/<company>.yaml` | The record: `watch` (pages to monitor, each with a role) and `facts` (one entry per field, per product where products differ) |
| `facts/_schema.yaml` | Required fields, statuses, source types and the confidence rules |
| `facts/_generated/` | Tables and JSON built from the records. Never edit by hand |
| `facts/_reports/<date>.md` | The weekly check's report |
| `facts/_monitor/state.json` | Page fingerprints (hashes only, never page text) |
| `tools/facts/` | `validate.py`, `weekly.py`, `generate.py`, `seed.py`, `common.py`, `test_facts.py` |
| `.github/workflows/facts-monitor.yml` | Runs the weekly check on Mondays, and validation on every push |

## Writing a fact

```yaml
- field: retention_terms
  status: stated            # stated | not_public | conflict | unclear | not_applicable | unresearched
  value: API data may not be kept beyond the duration strictly necessary
  confidence: Verified      # Verified | Corroborated | Reported | Unclear
  sources:
    - url: https://cloud.ouraring.com/legal/api-agreement
      type: vendor_legal     # see _schema.yaml source_types
      quote: "...exact words copied from the page..."
      retrieved: 2026-10-10
      # fetch_url: optional, for pages built by JavaScript (for example Apple's JSON docs)
  recheck_by: 2026-11-09     # 30 days for access, pricing and terms; 90 for compliance
  scope: Ring 4             # optional, when products differ
  note: optional context
```

Rules the validator enforces:

- **stated** needs a value and at least one source with an exact quote. Copy the quote from the
  page; never paraphrase or reconstruct it.
- **not_public** needs the pages that were checked, so "not public" is a dated claim.
- **conflict** needs at least two sources.
- A company's statement about its own HIPAA, GDPR, ISO 27001, SOC 2, BAA or DPA status is capped at
  **Corroborated** unless a source is a certificate, a registry entry, a regulator record or a written
  vendor confirmation.
- FDA status is **Verified** only from the FDA database. openFDA returns HTTP 404 for "no
  matches", so cite the accessdata.fda.gov search page for a negative result.

Run `python3 tools/facts/validate.py` before committing, then `python3 tools/facts/generate.py`.

## The weekly check

Every Monday the GitHub Actions job:

1. Fetches every watched page and every cited source, honouring robots.txt, with a pause between
   requests to the same site.
2. Checks each quote is still on its page. A 90% match is "reworded"; anything less is "missing".
3. Compares each page's fingerprint with last week's. A page that changes three weeks running with
   every quote intact is marked noisy and watched through its quotes only.
4. Validates every record and lists overdue re-checks.
5. Commits `facts/_reports/<date>.md` and opens one issue labelled `facts-monitor` (or comments on
   the open one) when there is something to act on.

A bot-blocked page is never treated as dead. Two weeks unreachable moves it to "check by hand".

## Re-check loop (the fact keeper)

When the issue arrives:

1. Work the report top down: quotes missing, then reworded, then pages changed, dead links, check by
   hand, overdue.
2. For each affected fact, read the live page, update `value`, `quote`, `retrieved` and
   `recheck_by`, and change `status` or `confidence` if the evidence changed.
3. Run `validate.py` and `generate.py`, and update any profile prose the change contradicts.
4. Log the changes in `shared/research-log.md`, commit, and close the issue.

## Profiles

A profile opts in to a generated facts block by adding `<!-- facts:begin -->` and
`<!-- facts:end -->` (or `<!-- facts:begin <company> -->` in a profile shared by several
companies). Do this only once the company's record is fully researched, or the block will show gaps
the hand-written section currently covers.

## Status

- 2026-10-10: 35 starter records; Oura filled as the pilot (18 facts, every quote confirmed on its
  live page). The other 1,076 facts are `unresearched` until the baseline research run.
