# Group A worked, 2026-10-31

Fact keeper pass for Evidation, Fitrockr, Verily, Ultrahuman, Zepp (Amazfit) and Circular. Two inputs: the
facts due by 2026-11-10 that the automatic extension could not confirm (31 Evidation, 23 Fitrockr), and the
items for these six companies in `facts/_reports/2026-10-31.md` (Quotes missing, Quotes reworded, Dead links,
Check by hand). Every quote written today was copied from the live page and probed as exact: all 89 quoted
sources in fitrockr.yaml, every Verily source citing security-trust, privacy-policy and terms, and the edited
Ultrahuman, Zepp and Circular facts. `python3 tools/facts/validate.py`: 35 companies, 1340/1340 facts,
0 errors. `generate.py` not run (the coordinator runs it).

The headlines:

- **Fitrockr's firewall is down.** www.fitrockr.com answered the project fetcher all session. Every quote from
  researcher B's unconfirmed live reading of 2026-10-21 is now confirmed exact on the live page, and every
  Wayback-backed quote still on the site was moved to its live URL (help articles now sit under
  `/help-center/`, the old `/research/help-center/` paths 404). 23 of 28 researched facts went up in
  confidence; values changed for two.
- **Verily removed Study Watch from its Security and Trust page.** The SOC 2 product list no longer names
  "Study Watch & Hub", and the ISO 27001 card no longer lists products at all. That removes the vendor-side
  half of the Study Watch status conflict.
- **Circular's $299 copy is gone.** The shop page now says $349, matching the product page, so device_price
  is no longer a conflict.
- **Evidation was not touched.** Its site terms forbid automated collection (`TERMS_BLOCKED_HOSTS`), and
  every due fact rests on evidation.com pages. All 31 are listed for a by-hand check below.

## Items

### Quotes missing

| Company | Field | What I found | What I changed | Confidence |
|---|---|---|---|---|
| ultrahuman | academic_pricing | Heroes page reworded its verification line to "By purchasing, you consent to provide ID or proof of eligibility if requested." Meaning unchanged; still no discount amount shown | Quote replaced, all three sources re-read, `recheck_by` 2026-11-30 | Verified (unchanged) |

### Quotes reworded

| Company | Field | What I found | What I changed | Confidence |
|---|---|---|---|---|
| zepp-amazfit | subscription_price | Helio Strap product card now reads "...with no required subscription." App Store in-app list unchanged ($9.99 monthly; yearly $29.99, $34.99, $39.99, $49.99) | Helio quote replaced, App Store quotes re-probed exact, `recheck_by` 2026-11-30 | Corroborated (unchanged) |
| circular | device_price (2 quotes) | Shop page hero now "$349 one purchase", HSA/FSA line now "a $349 ring closer to $245". Product page still $349.00; Ring 3 page still "up to 30% off" and December 2026 pre-orders | **Status changed from conflict to stated**: Ring 2 lists at $349 on both pages. Old $299 quotes moved into the note as history | **Unclear to Verified** |

### Dead links

| Company | Source | What I found | What I changed | Confidence |
|---|---|---|---|---|
| verily | `privacy-policy`, `security-trust`, `terms` (`_next/data/1y9FmmHH1nlmtBVxwLMlY/...`) | Build id changed to `CZzunCZyuKLSZCczoF5ca`. No stable route exists: the page HTML carries the text only in its `__NEXT_DATA__` script, which the fetcher strips. Privacy policy (effective 2026-04-14) and terms (last modified 2026-04-07) unchanged; searched again for AI, machine learning, training and processing-agreement language, none | All `fetch_url`s and the three `watch` entries moved to the new build id. Notes now say to read the current id from the page's `__NEXT_DATA__` "buildId". retention_terms, ai_training_terms, baa, dpa, hipaa_statement, gdpr_statement (both) and data_residency re-read, `retrieved` 2026-10-31, `recheck_by` moved | Unchanged |
| verily | program_status [Verily Study Watch] | security-trust no longer contains "Study Watch" anywhere. Press quotes (HIT Consultant, MD+DI), the Study Watch page 404 and the Quipment K182456 listing (openFDA, created 2026-05-12) all re-confirmed | **Status changed from conflict to stated**: discontinued by press reports, with Verily's own audit scope now dropping Study Watch; the Quipment listing kept as the only contrary sign | **Reported to Corroborated** |
| verily | soc2 | SOC 2 card now reads "for our enterprise and the following solutions:" Lifelong, Lightpath, Verily Me, Verily Pre, Viewpoint Site CTMS and Workbench | **Value changed**: Study Watch & Hub no longer in scope. New quote | Corroborated (unchanged) |
| verily | iso27001 | ISO card now ends "...information security management." with no product list | **Value changed**: no product scope stated (Study Watch no longer claimed). Product-list quote dropped | Corroborated (unchanged) |

### Check by hand

| Company | Source | What I found | What I changed |
|---|---|---|---|
| fitrockr | all www.fitrockr.com pages (listed in the work list) | Reachable all session (HTTP 200) | Worked in full; see the next section |
| verily | massdevice.com Study Watch launch article | 403 to the fetcher and to WebFetch | Nothing; raw_streams [Study Watch (historical data)] is not due until 2026-11-21. Listed below |
| zepp-amazfit | `upload-cdn.zepp.com/tposts/8192` | robots.txt disallows | Nothing; listed below |
| zepp-amazfit | sec.gov 20-F | 403 (sec.gov needs a contact address in the user agent, which this project does not send) | Nothing; listed below |
| evidation | 34 evidation.com and help.evidation.com pages | `terms_blocked`; not fetched by any route | Nothing; listed below |

### Re-check list: Fitrockr (23 due facts, plus the 5 others in the record)

Every researched Fitrockr fact was re-read today and moved to `recheck_by` 2026-11-30 (access, pricing, terms)
or 2027-01-29 (compliance). The record header comment was rewritten to describe the 2026-10-31 re-check.

| Field | What I found | What I changed | Confidence |
|---|---|---|---|
| research_program, program_eligibility, program_application | Grants page live, all capture quotes exact on it; Garmin release unchanged | Sources moved to the live page | Corroborated (unchanged) |
| program_status | Live page still "New grants will be announced soon." and "Applications closed on March 31, 2026." | Value wording updated to the live reading | **Reported to Verified** |
| developer_program_status | Pricing page now quotable for the separate Wearable API product: SMALL EUR 150 (0 to 20 users), MEDIUM EUR 500 (21 to 500), LARGE EUR 1000 (501 to 1500) a month, 12-month subscription | **Value changed**: Wearable API product added (B had reported it without a quote). Duplicate old-pricing quote dropped | **Reported to Verified** |
| user_cap | Pricing page (per device, unlimited users) and help article ("based on user numbers") both live and both still say what they said | Archive duplicates dropped; note updated | Conflict, Reported (unchanged) |
| academic_vs_commercial, academic_pricing | Help article live, quote exact | Moved to live URL | **Reported to Verified** |
| api_platform_fees | Every figure B reported is on the live page, including live streaming and surveys at +20% (previously unquoted) | **Value changed**: now "as read live on 2026-10-31", adds GPS +10%, self-reported data, food tracking and clinical assessment +20% each, on-premise "EUR 5,000 setup + 20%", and the Wearable API tiers. New quotes for on-premise, live streaming, surveys, historic import and Wearable API | **Reported to Verified** |
| minimum_commitment, quote_required | Live pricing and 2026-09-19 terms confirm; the superseded 2025-11-09 terms quotes (10.1, 4.2) and "Get in touch to receive your custom offer." are gone | Superseded quotes dropped; terms definition of "Order" (quotation, order form) added for quote_required | **Reported to Verified** |
| raw_streams | All live except the "Raw BBI ... Each beat" line, which was in the old pricing table that is gone from the live site | Capture kept for that one quote (re-read today); rest live | **Reported to Corroborated** |
| derived_metrics | Old dictionary wording gone; live dictionary has "Lf/Hf LF/HF ratio, calculated by the Fitrockr platform" and the MET calculation-type line | New live quotes | **Reported to Verified** |
| sampling_rates, history_depth, export_routes, retention_terms, ai_training_terms, deprecations | All quotes exact on live pages (or live help-centre URLs); the per-stream sampling table is confirmed gone; old iOS app still 404 | Sources moved to live URLs; "researcher B's reading" removed from values | **Reported to Verified** |
| rate_limits | Still not published. Terms confirm "materially exceeds documented API or usage limits"; the API article only recommends fetching hourly or daily | Sources moved to live pages; note updated | not_public, **Reported to Verified** |
| baa, dpa, hipaa_statement, gdpr_statement, iso27001, soc2 | All quotes exact live; no SOC 2 text on any live page | Superseded terms quotes (5.1, 5.2) and the quote-less old privacy-policy capture dropped, with history kept in notes; GDPR re-cited at the live DPA clause | **Reported to Corroborated** (self-claim cap) |
| data_residency | Live hosting page, help page and privacy policy confirm; on-premise quote replaced by the live wording | Added the privacy policy's "may be processed in:" quote (EEA, US, other countries) | **Reported to Verified** |
| fda_clearances | openFDA still NOT_FOUND for all four queries | Dates moved | Verified (unchanged) |

### Re-check list: Evidation (31 due facts)

Not worked. Every one rests on evidation.com or help.evidation.com, whose terms forbid automated collection.
The few third-party sources still match: ClinicalTrials.gov NCT06207929 (research_program [Outside
researchers]), apis.io (developer_program_status), the App Store listing (subscription_price, deprecations),
and the evidation-health GitHub organisation, which still has 0 public repositories (licence). That is not
enough to move any `recheck_by`. All 31 stay due 2026-11-09.

## Prose fixed

None. Every profile these changes touch is a shared file: `emerging-platforms.md` (Verily, Circular),
`data-intermediaries.md` (Fitrockr). The generated facts blocks in both update when `generate.py` runs; the
hand-written lines are listed below.

## Shared-file edits needed

**`module-01-wearables/profiles/emerging-platforms.md`**

- Line 115 (Verily Status row). Current: "| Status | **Conflict.** In use across clinical trials since 2017. ... Against that, Verily's Security and Trust page still lists "Study Watch & Hub" in its SOC 2 and ISO 27001 scope, and a third party, Quipment Inc., ... | **Conflict, Reported** (2026-10-22; was Unclear 2026-10-10) |". Replace the "Against that" sentence with: "Verily's Security and Trust page no longer lists "Study Watch & Hub" in its SOC 2 scope or any product in its ISO 27001 claim (checked 2026-10-31). The only contrary sign is a third party, Quipment Inc., registered as a repack or relabel establishment, which added an FDA device listing for Study Watch (K182456) on 2026-05-12." Change "**Conflict.**" to "**Discontinued (press reports).**" and the confidence cell to "**Corroborated** (2026-10-31; conflict, Reported 2026-10-22; Unclear 2026-10-10)".
- Line 122 (Verily Compliance row). Current: "Verily claims SOC 2 Type II and ISO/IEC 27001 covering Study Watch & Hub and Workbench, among other products". Replace with: "Verily claims a SOC 2 Type II audit covering its enterprise and Lifelong, Lightpath, Verily Me, Verily Pre, Viewpoint Site CTMS and Workbench (Study Watch & Hub dropped by 2026-10-31), and ISO/IEC 27001 with no product scope stated".
- Line 163 (Circular row). Current: "Price conflict: $349 on the store product page, $299 on the shop page." Replace with: "Ring 2 lists at $349 on both the store product page and the shop page (the shop page said $299 until at least 2026-10-22)."

**`module-01-wearables/profiles/data-intermediaries.md`** (Fitrockr section)

- Lines 151 to 157. Current: "**Confidence for this section: mostly Reported.** fitrockr.com blocks scripts (an HTTP 403 firewall), so its fact record rests on Wayback captures (latest 2026-10-07) and on one researcher's live reading of 2026-10-21 that could not be re-checked. Every Fitrockr-sourced fact below is **Reported** unless marked otherwise, and the record is due for a by-hand browser check by 2026-11-04 (`../../facts/fitrockr.yaml`)." Replace with: "**Confidence for this section: mostly Verified.** fitrockr.com blocked scripts when the record was judged (2026-10-21), but answered on 2026-10-31, when every quote was re-read on the live site. Self-claims (HIPAA, GDPR, ISO 27001, BAA, DPA) stay Corroborated, raw beat-to-beat access is Corroborated, and the licensing basis is a conflict (`../../facts/fitrockr.yaml`)."
- Lines 163 to 170, Confidence column. Change "**Reported** (`../../facts/fitrockr.yaml`, raw_streams, sampling_rates)" to "raw_streams **Corroborated**, sampling_rates **Verified**"; history_depth, api_platform_fees / minimum_commitment / quote_required, retention_terms / ai_training_terms, deprecations to **Verified**; Hosting and compliance to "data_residency **Verified**; HIPAA, BAA, DPA, ISO 27001, SOC 2 **Corroborated**"; Grants round status to **Verified**. Line 165 (Study tooling, "**Reported** (vendor)") can stay unless re-read separately.
- Line 164. Current: "up to 2 years can be imported (EUR 500 setup, researcher B's reading)". Replace with: "up to 2 years can be imported (EUR 500 setup)".
- Line 166. Current: "Add-ons as read live on 2026-10-21: accelerometer and gyroscope +25% on licence, API access +20%, live streaming +20%, surveys +20%, on-premise hosting €5,000 + 20%, historic Garmin Connect import €500 setup". Replace with: "Add-ons as read live on 2026-10-31: accelerometer and gyroscope +25% on licence, API access +20%, live streaming +20%, surveys and notifications +20%, all-day GPS +10%, self-reported data, food tracking and clinical assessment +20% each, on-premise hosting €5,000 setup + 20%, historic Garmin Connect import €500 setup". Add a sentence: "A separate Wearable API product (no dashboard) costs €150, €500 or €1,000 a month for up to 20, 500 or 1,500 users on a 12-month subscription."
- Line 649. Current: "- Fitrockr pricing (moved from /research/pricing/; site blocks automated access): https://www.fitrockr.com/pricing/". Replace with: "- Fitrockr pricing (moved from /research/pricing/): https://www.fitrockr.com/pricing/".
- Line 680 (source 9). Current: "(judged 2026-10-21; mostly Reported, site blocks scripts). Sources include https://www.fitrockr.com/pricing/ (live reading 2026-10-21) and Wayback captures of ...". Replace with: "(judged 2026-10-21, re-read live 2026-10-31). Sources include https://www.fitrockr.com/pricing/ , https://www.fitrockr.com/research/research-grants/ , the help-centre articles under https://www.fitrockr.com/help-center/ , the 2026-09-19 terms and privacy policy, https://www.fitrockr.com/features/ and one Wayback capture of https://www.fitrockr.com/research/pricing/ (2026-07-13)."

**`module-01-wearables/comparison-matrix.md`**

- Line 63 (Verily Study Watch). Current: "Study Watch status conflict, R (device program wound down 2025)". Replace with: "Study Watch discontinued, C (device program wound down 2025)".
- Line 237 (Fitrockr). Current: "3-month minimum (Reported, 2026-10-21; site blocks scripts)". Replace with: "3-month minimum (Verified, 2026-10-31)".
- Line 272 (Verily compliance). Current: "SOC 2 Type II and ISO 27001 claimed for Study Watch & Hub and Workbench, reports possibly under NDA (C)". Replace with: "SOC 2 Type II claimed for Workbench, Verily Pre and other products (Study Watch no longer listed); ISO 27001 claimed with no scope; reports possibly under NDA (C)".
- Line 348. Current: "Device program wound down 2025; **status conflict (R)**". Replace with: "Device program wound down 2025; **discontinued (C)**".

**`module-01-wearables/README.md`**

- Lines 228 and 229. Current: "the Verily Study Watch's status is a conflict (Reported): press reports Verily wound down its device program in August 2025, while Verily's trust page still lists Study Watch & Hub." Replace with: "the Verily Study Watch is discontinued (Corroborated): press reports Verily wound down its device program in August 2025, and by October 2026 Verily's trust page no longer lists Study Watch & Hub."
- Line 222. Current: "Circular's Ring 2 price ($349 or $299)". Replace with: "Circular's Ring 2 price ($349; a $299 figure on the shop page is gone)", or drop the price clause.

**`module-01-wearables/profiles/_inventory-and-scope-decisions.md`**

- Line 56 (Verily Study Watch). Current: "Status a **conflict (Reported)**: press reports the device program was wound down in August 2025, while Verily's trust page still lists Study Watch." Replace with: "Status **discontinued (Corroborated)**: press reports the device program was wound down in August 2025, and Verily's trust page dropped Study Watch from its audit scope by October 2026."

**`shared/unresolved-questions.md`**

- Line 354 (question 47). Current: "**Fact records 2026-10-22: Reopened, status is a conflict (Reported).** ... Verily's Security and Trust page still lists "Study Watch & Hub", and Quipment Inc. ...". Replace the bold lead with "**Fact records 2026-10-31: discontinued (Corroborated); was a conflict on 2026-10-22.**" and the trust-page sentence with "Verily's Security and Trust page no longer lists "Study Watch & Hub" (2026-10-31)." The question itself (can Study Watch be supplied to new studies) stays open for Verily.

**Artifacts.** The Wearable Data Atlas (`module-01-wearables/wearable-data-atlas.html` lines 527, 789 and 874), the KB Explorer and the KB Map carry the Verily conflict and the Circular $299 conflict and need a resync after the edits above.

## Needs a browser or vendor

- **Evidation, all 31 due facts** (every field in the work list). Site terms forbid automated collection, so
  these need a person in a browser by 2026-11-09. Pages: the 34 evidation.com and help.evidation.com URLs listed
  under "Check by hand" in `facts/_reports/2026-10-31.md`. Add to `shared/manual-sweep.md`.
- **Verily raw_streams [Verily Study Watch (historical data)]**: massdevice.com returns 403 to scripts and to
  WebFetch. Two quotes ("electrodermal activity", "up to a week's worth of raw data") need a browser read by
  2026-11-21.
- **Zepp `upload-cdn.zepp.com/tposts/8192`** (ai_training_terms, data_residency): robots.txt disallows. Not
  due until 2026-11-21 and 2027-01-20.
- **Zepp 2025 Form 20-F on sec.gov** (data_residency, hipaa_statement, iso27001, soc2): 403 to the fetcher.
  Not due until 2027-01-20.
- **Vendor questions.** Verily: can Study Watch still be supplied to new studies, and what does the Quipment
  K182456 listing cover. Fitrockr: is pricing per device or per user (the user_cap conflict), and does the
  every-beat raw BBI export still exist now the plan table is gone. Circular: whether the "up to 30% off" Ring 2
  offer has a published price.
- **Watch for:** Verily's Next.js build id changes on every redeploy. The current id is
  `CZzunCZyuKLSZCczoF5ca`; when the three Verily fetch_urls 404 again, read the new one from the page's
  `__NEXT_DATA__` "buildId".
