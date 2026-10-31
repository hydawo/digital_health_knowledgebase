# Group C worked, 2026-10-31

Fact keeper pass for Empatica, Oura, Samsung, Apple, Fitbit/Google, Withings, Labfront and MetricWire.
It covered the 54 facts on the group C re-check list (due by 2026-11-10 and not extended automatically)
and these companies' items in `facts/_reports/2026-10-31.md`: quotes missing, quotes reworded, dead
links and check by hand. Every quote written today was copied from the live page and probed exact with
`tools/facts/quote_probe.py`. Every source re-read got `retrieved: 2026-10-31`. Every re-verified fact
on the list had `recheck_by` moved to today plus the field's interval (2026-11-30 for the 30-day groups).
`python3 tools/facts/validate.py`: 35 companies, 1340/1340 facts, 0 errors. `generate.py` was not run
(the coordinator runs it).

No status or confidence changed. Four values changed: the MetricWire Catalyst release dates and three
Google Store prices. The three prices are sale prices recorded next to list prices that have not changed.

Two routes were found and used for pages that block scripts:

- **Zendesk Help Center API.** academic-support.empatica.com and support.withings.com answer
  `/hc/` article requests with a Cloudflare "Just a moment..." page (403). The public
  `/api/v2/help_center/articles/<id>.json` endpoint returns the same article (robots.txt allows it).
  Each article was read that way and its body converted with `common.html_to_text`. All 26 Empatica
  support quotes and all 3 Withings support quotes were exact. No `fetch_url` was added: the monitor's
  JSON path flattens strings without stripping the HTML inside `body`, so the quotes would show as
  missing. These sources will keep appearing under "Check by hand" until `common._body_to_text`
  handles that case.
- **Europe PMC REST.** `https://www.ebi.ac.uk/europepmc/webservices/rest/<PMCID>/fullTextXML` was
  added as `fetch_url` for the two PMC papers (the same pattern as in avicenna.yaml and fitrockr.yaml).
  Both quotes are exact through it.

## Items

### Quotes missing

| Company | Field | What I found | What I changed | Confidence |
|---|---|---|---|---|
| metricwire | app_availability [Catalyst By MetricWire (current participant app)] | iTunes lookup: version 6.10.0, `currentVersionReleaseDate` 2026-10-27T21:46:03Z, still iOS 15.0+. Play: "Updated on Oct 29, 2026" | **Value updated** to v6.10.0 (2026-10-27) and Android 2026-10-29. Both date quotes replaced. Note added that these date quotes break with every release | Verified (unchanged) |
| apple | research_program [Investigator Support Program] | PMC13438180 serves a bot check to scripts. The Europe PMC full text has the quote, exact | `fetch_url` set to Europe PMC fullTextXML. Retrieved updated | Verified (unchanged) |
| fitbit-google | device_price [Fitbit Charge 6 (US)] | Store shows "$129.95 $159.95 or make 4 payments of $32.49": a sale price next to the struck-through list price | **Value now** "List $159.95; on sale at $129.95 on 2026-10-31". New quote, plus a note that it breaks when the sale ends | Verified (unchanged) |
| fitbit-google | device_price [Fitbit Versa 4 (US)] | "$159.95 $199.95 or $13.33/month with 12-month financing": sale price next to the list price | **Value now** "List $199.95; on sale at $159.95 on 2026-10-31". New quote and note | Verified (unchanged) |

### Quotes reworded

| Company | Field | What I found | What I changed | Confidence |
|---|---|---|---|---|
| metricwire | app_availability [Catalyst] (Play listing) | "Updated on Oct 7, 2026" is now "Updated on Oct 29, 2026" | Covered by the row above | Verified (unchanged) |
| fitbit-google | device_price [Pixel Watch 5 (US)] | "From $299.99 $399.99 Save $100": list price $399.99 unchanged, on sale at $299.99 | **Value now** "List from $399.99; on sale from $299.99 on 2026-10-31 and from $349.99 on 2026-10-10". New quote | Verified (unchanged) |

### Dead links

| Company | Source | What I found | What I changed | Confidence |
|---|---|---|---|---|
| oura | `cloud.ouraring.com/v2/docs` read via `static/json/openapi-1.42.json` (404) | The docs page now loads `openapi-1.43.json` | All 20 occurrences (facts and `watch`) now use `openapi-1.43.json`. Every Oura quote was re-probed and all were exact, including every quote from the docs in the 12 facts that cite it. Retrieved set to 2026-10-31 on those sources | Unchanged |

### Check by hand

| Company | Source | What I found | What I changed | Confidence |
|---|---|---|---|---|
| empatica | 7 academic-support.empatica.com articles (403) | Cloudflare challenge. Read through the Zendesk API instead (see above). "Available Features" was updated 2026-10-20; package prices on it ($2,332.80 EmbracePlus = $1,166.40 device + $1,166.40 3-year subscription) agree with the record | Retrieved and recheck_by updated on 17 facts. No values changed | Unchanged |
| withings | 3 support.withings.com articles (403) | Read through the Zendesk API. Withings+ FAQ updated 2026-10-27, still "$99.95 per year". Terms still say $99.95. US store still says $99.50 | subscription_price conflict kept. The FAQ date in the value was corrected (it said 2025-10-14, the article now says 2026-10-27). Route noted. export_routes support quote exact | Unclear / Verified (unchanged) |
| oura | accessdata.fda.gov PMN and PMA applicant searches (404 to scripts) | openFDA `510k.json?search=applicant:oura` and `pma.json?search=applicant:oura` both return "No matches found" | `fetch_url` added to both sources per facts/README.md. Retrieved updated. recheck_by left at 2027-01-08 (not due) | Verified (unchanged) |
| withings | `accessdata.fda.gov/cdrh_docs/pdf20/K201456.pdf` (404 to scripts) | No script route to the PDF. The fact is not due (90-day field) and its other quotes are on openFDA | Nothing changed. Listed below | Unchanged |

### Re-check list (not public, unclear, conflict, not applicable, and stated facts with blocked pages)

| Company | Facts | What I found | What I changed |
|---|---|---|---|
| empatica | 17: research_program, program_eligibility, program_application x2, user_cap x2, academic_vs_commercial, device_price, subscription_price, api_platform_fees [Enterprise], minimum_commitment, raw_streams [EmbracePlus], derived_metrics, sampling_rates, export_routes, rate_limits, deprecations | All quotes exact (support articles through the Zendesk API, PMC11644628 through Europe PMC). llms.txt still says Enterprise pricing is by contact. No rate limit is published on cloud-api or in the S3 and keys articles | Retrieved, recheck_by. `fetch_url` added for PMC11644628 |
| oura | 6: academic_pricing, api_platform_fees [Enterprise], minimum_commitment [Organizational], raw_streams [Enterprise] (unclear), history_depth [API], retention_terms [API] (conflict) | Research page still says "raw data to CSV or JSON" with no definition. No price, discount or minimum on the research page, business terms or partner support. OpenAPI 1.43 still advises one historical request with no lookback limit. The API Agreement and FAQ quotes behind the conflict are both still exact | Retrieved, recheck_by |
| samsung | 6: program_eligibility, program_status [Research Stack] (unclear), user_cap, academic_vs_commercial, academic_pricing, rate_limits | GitHub API: S-HealthStack repos still last pushed 2024-10-24 (starter-app 2024-08-20), none archived. No eligibility, cap, academic terms or limits on the developer pages. The education offer is still a consumer discount (an extra 15% off Galaxy Watch9) | Retrieved, recheck_by. The program_status note records the 2026-10-31 GitHub check |
| apple | 2: raw_streams [HealthKit ECG] (conflict), rate_limits (not applicable) | Both conflicting Apple quotes are still exact. HealthKit and SensorKit are still on-device only | Retrieved, recheck_by |
| fitbit-google | 4: academic_vs_commercial [Google Health API], academic_pricing, minimum_commitment [Enterprise], ai_training_terms [Developers] | The Google Health API policies still have no academic tier and no clause naming AI or ML training. No minimum order or pricing on enterprise-solutions | Retrieved, recheck_by |
| withings | 4: subscription_price [Withings+ (US)] (conflict), history_depth, export_routes, retention_terms [Inactive accounts] (conflict) | Conflicts unchanged (3 vs 5 vs 10 years for inactive accounts, $99.50 vs $99.95 per year). No lookback limit in llms.md or openapi.yaml | Retrieved, recheck_by. Note on the subscription_price route |
| labfront | 3: rate_limits (not applicable), ai_training_terms (conflict), deprecations | Privacy Policy still dated December 30, 2025, with both machine-learning sentences. Still no API ("does not currently provide an external SDK or API"). No deprecations announced | Retrieved, recheck_by |
| metricwire | 12: program_application, program_status, developer_program_status, user_cap, api_platform_fees, minimum_commitment, hosting_price, sampling_rates, history_depth, rate_limits, ai_training_terms, deprecations | Site sitemap unchanged (site-licence lastmod 2019-09-20). No pricing page (`/pricing/` still 404, expected absent). SwaggerHub ConsumerAPI still versions 1.0.0 to 4.0.0, none newer. No AI terms. Knowledge base still 404 | Retrieved, recheck_by |

## Prose fixed

- `module-02-digital-phenotyping/profiles/metricwire.md` line 10 (Quick Facts) and line 22 (Products):
  Catalyst v6.9.0 / 2026-10-07 replaced with v6.10.0 (2026-10-27, iOS) and 2026-10-29 (Android).
  The check dates now read 2026-10-31. The generated facts block refreshes when `generate.py` runs.
- `module-01-wearables/profiles/fitbit-google.md` line 264 was left as is. It gives the 2026-10-10
  prices with their date, and the list prices have not changed.

## Shared-file edits needed

- `module-02-digital-phenotyping/comparison-matrix.md` line 38, MetricWire status cell.
  Current: `Active ("Catalyst By MetricWire" updated 2026-10-07 on both stores)`.
  Replacement: `Active ("Catalyst By MetricWire" iOS v6.10.0 released 2026-10-27; Android updated 2026-10-29)`.
- `module-02-digital-phenotyping/sources.md` line 224, row S-MW-11, notes cell.
  Current: `Catalyst updated 2026-10-07 on both stores`.
  Replacement: `Catalyst updated 2026-10-27 (iOS) and 2026-10-29 (Android), checked 2026-10-31`.
- `tools/facts/common.py` (tooling, not prose, for the coordinator to decide): in `_body_to_text`,
  strip HTML from JSON string values, or special-case Zendesk `article.body`. With that change, the
  Empatica and Withings support sources can take a Help Center API `fetch_url` and leave "Check by hand".

## Needs a browser or vendor

- **withings fda_clearances [ScanWatch, ScanWatch 2]:** `accessdata.fda.gov/cdrh_docs/pdf20/K201456.pdf`
  (510(k) summary, SpO2 indication quote) returns 404 to scripts. Open it in a browser before the
  2027 re-check. recheck_by left unchanged.
- **Vendor questions still open (unchanged):** whether Oura's Enterprise "raw data" export means
  sensor-level signals. Apple: whether the HealthKit ECG waveform counts as raw. Withings: the
  Withings+ annual price ($99.50 or $99.95) and the inactive-account threshold. Labfront: whether
  study Experiment Data is used to train its models.
