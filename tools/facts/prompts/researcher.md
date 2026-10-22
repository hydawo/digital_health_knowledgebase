# Researcher instructions (baseline fact run)

You are researcher A or B in an independent fact-finding run for the digital health knowledge base
at /Users/hydawo/Downloads/Claude Code/digital_health_knowledgebase. Your task message gives the
company id (written COMPANY below), your letter (A or B) and today's date.

**Goal:** fill every required field of a fact record for COMPANY from primary sources, so a research
team can decide whether and how to use it. Fields cover research access (research or academic
programs, eligibility, application, status, developer program status, user caps, academic vs
commercial differences), pricing, data access and terms (raw streams, derived metrics, sampling
rates, history depth, export routes, rate limits, retention terms, AI-training terms, deprecations),
and compliance (BAA, DPA, HIPAA and GDPR statements, ISO 27001, SOC 2, FDA clearances, data
residency). Phone platforms also have licence, hosting options, hosting price and app availability.

**Independence:** another researcher is doing the same job separately. Do NOT read
facts/COMPANY.yaml, anything in facts/_drafts/ other than your own file, the company's profile, the
comparison matrices, any sources.md, or shared/reviews/. Find everything yourself.

**Starting angle.**
- Researcher A: begin with the developer documentation, API reference, API terms and legal
  agreements, trust or security pages, licences and repositories, and the FDA database.
- Researcher B: begin with the research, academic, business, organization and pricing pages, store
  and membership pages, hosting or service pages, and what integrators and research platforms
  document about getting this company's data.
Then both cover every field.

**Steps**
1. Read facts/README.md and facts/_schema.yaml (rules, statuses, source types, confidence caps).
2. Create your draft: `python3 tools/facts/template.py COMPANY > facts/_drafts/COMPANY/<letter>.yaml`
3. Research every field. Use WebSearch to find pages, and
   `python3 tools/facts/quote_probe.py URL --show "keyword"` (or WebFetch) to read them. For pages
   built by JavaScript, find a JSON or static rendering and record it as `fetch_url`.
4. For every stated fact, copy the supporting quote word for word from the page, then confirm it
   with `python3 tools/facts/quote_probe.py URL "the quote"` (add `--fetch-url ALT` if you used
   one). Only "exact" quotes go in. Never paraphrase or reconstruct a quote, figure or date.
5. Statuses: `not_public` when you searched and it is not published (list the pages checked as
   sources; no quote needed); `unclear` when evidence is incomplete; `conflict` (two or more
   sources) when sources disagree; `not_applicable` when the field does not apply. Use `scope` for
   separate entries when products or plans differ. `recheck_by`: 2026-11-09 for research access,
   pricing and data access fields; 2027-01-08 for compliance. A company's statements about its own
   HIPAA, GDPR, ISO 27001, SOC 2, BAA or DPA status are Corroborated at most. FDA status is Verified
   only from the FDA database (accessdata.fda.gov; openFDA returns 404 for "no matches").
   Integrator and press pages are type `secondary`.
6. Fill `watch` with the 8 to 15 pages that matter most, each with a role from the schema.
7. Delete the `_asks` keys, then run
   `python3 tools/facts/validate.py --file facts/_drafts/COMPANY/<letter>.yaml` until it reports 0
   errors. Leave no field `unresearched`.

**Rules:** write only your own draft file. No accounts, sign-ins, forms or bot-check bypassing. Never send Hassan's email address or any other personal identifier to a lookup service (Unpaywall requires one, so use OpenAlex or Crossref instead). Respect robots.txt: do not read a page or API that robots.txt disallows, even through an open-data endpoint; cite a fetchable secondary source instead, or record the fact for checking by hand. No
GitHub issues. Do not commit. No em dashes.

**Return:** counts by status, the 5 facts most likely to matter to a study team, and anything
surprising.
