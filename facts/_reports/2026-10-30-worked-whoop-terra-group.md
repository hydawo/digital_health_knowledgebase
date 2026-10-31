# 2026-10-26 report worked: WHOOP, Terra, Thryve, Ultrahuman, Fitrockr, LifeData, 2026-10-30

Fact keeper pass on part of `facts/_reports/2026-10-26.md`: WHOOP's 15 overdue re-checks, and the
flagged Terra, Thryve, Ultrahuman, Fitrockr and LifeData quotes. Every quote written today was copied
from the live page (or its `fetch_url`) and probed exact with `tools/facts/quote_probe.py`. The Thryve
Fitbit deprecations fact was not touched. `python3 tools/facts/validate.py`: 35 companies, 1340/1340
facts, 0 errors, 13 overdue (all WHOOP, listed below). `generate.py` run afterwards.

## Items

### Quotes missing and reworded

| Company | Field | What I found | What I changed | Confidence |
|---|---|---|---|---|
| terra | api_platform_fees | Prices unchanged. Wording changed: credits are now "Unified API credits", and the Streaming add-on page now says it is available "on its own or alongside any Terra plan" (it used to say "an add-on to any Terra base plan") | Three quotes replaced with the new wording; value now says the Streaming add-on can be bought on its own or with any plan; `retrieved` 2026-10-30 on all 5 sources; `recheck_by` 2026-11-29 | Verified (unchanged) |
| terra | user_cap | "20,000 credits" now reads "20,000 Streaming credits"; meaning unchanged | Quote refreshed; `retrieved` 2026-10-30 on all 3; `recheck_by` 2026-11-29 | Verified (unchanged) |
| thryve | hipaa_statement | Certifications page rebuilt; the per-certification blurbs are gone. The pricing FAQ still says "100% GDPR and HIPAA compliant" | Dropped the missing quote; the tokenization quote extended to the full sentence naming HIPAA Safe Harbor; `retrieved` 2026-10-30; `recheck_by` 2027-01-28 | Corroborated (unchanged, self-claim) |
| thryve | gdpr_statement | Same rebuild | Missing quote replaced with the page's tokenization sentence naming GDPR data minimization; `retrieved` 2026-10-30; `recheck_by` 2027-01-28 | Corroborated (unchanged, self-claim) |
| thryve | iso27001 | Same rebuild; the page now says "Thryve is independently audited and certified" and the footer "ISO9001 & 27001 Certified" | Missing quote replaced with those two; `retrieved` 2026-10-30 on all 4; `recheck_by` 2027-01-28 | Corroborated (unchanged, self-claim) |
| ultrahuman | subscription_price | Cardio Adaptability still $2.9/month (spacing only). **Price wording change:** Ultrahuman Max no longer "Starting at $9.99/mo"; the US buy page now offers 3 months $29.97 or 1 year $99.99 (3-month rate still $9.99 a month; annual works out lower) | Max quote replaced with two new quotes; value and note updated; `retrieved` 2026-10-30; `recheck_by` 2026-11-29. Prose fixed in `emerging-platforms.md` (Quick Facts), Module 1 matrix and the atlas | Verified (unchanged) |
| fitrockr | raw_streams | PMC12975902 quote exact today; last week's 0% was a fetch problem | Added Europe PMC `fullTextXML` as `fetch_url` (probes exact); `retrieved` 2026-10-30 on that source. `recheck_by` left at 2026-11-04 (the fact rests mostly on Archive captures; manual sweep item 1) | Reported (unchanged) |
| lifedata | gdpr_statement [DPF certification] | **Status change:** the DPF registry no longer shows "Re-certification under Review"; EU-U.S., Swiss-U.S. and UK Extension all read plain "Active", dates unchanged (next due 2027-04-28). Registered privacy policy still the June 12, 2024 version | Two quotes replaced, Swiss-U.S. quote added; value and note updated; `retrieved` 2026-10-30 on all 5; `recheck_by` 2027-01-28. Prose fixed in `lifedata.md` and the Module 2 matrix | Verified (unchanged, registry) |
| lifedata | app_availability [LifeData+] | Android listing now "Updated on Oct 20, 2026"; iOS now v1.0.18 of Oct 17 | Quote refreshed, iOS version quote added, value updated; `retrieved` 2026-10-30; `recheck_by` 2026-11-29. Prose fixed in `lifedata.md` | Verified (unchanged) |

### WHOOP overdue re-checks (15)

www.whoop.com answers scripts and WebFetch with 403 on every page tried, and the Internet Archive has
no capture newer than those already cited. Archived text cannot change, so re-reading it does not
confirm the live page.

| Field | What I found | What I changed | Confidence |
|---|---|---|---|
| device_price | developer.whoop.com trial line and trackervs exact; Archive membership capture unchanged | `retrieved` 2026-10-30 on the two live sources; `recheck_by` 2026-11-29 | Reported (unchanged) |
| fda_clearances [IHRN] | openFDA `applicant:whoop` still returns only K243236 (ECG); staff reply exact | `retrieved` 2026-10-30 on both; `recheck_by` 2027-01-28 | Reported (unchanged) |
| research_program, program_eligibility, program_status, academic_vs_commercial, academic_pricing | Each cites /research/, /unite/, whoopunite.com or /bulk-buy/, all 403. whoopunite.com does still 301 to www.whoop.com. Other live sources exact | Nothing; needs a browser | unchanged |
| subscription_price | Vendor membership page 403. trackervs and Tom's Guide quotes exact, and a search found third parties still listing $199 / $239 / $359 a year | Nothing; needs a browser (Verified rests on the vendor page) | Verified (unchanged) |
| minimum_commitment | Terms of sale 403; other quotes exact | Nothing; needs a browser | unchanged |
| history_depth, export_routes [Member self-export] | API quote and community quote exact; the CSV export claims rest on an Archive capture of a 403 page | Nothing; needs a browser | unchanged |
| dpa, gdpr_statement, data_residency | Rest on an August Archive capture of the privacy policy (live 403) and a 2023 FAQ | Nothing; needs a browser | unchanged |
| soc2 | 2022 deck exact; privacy policy (the page checked for a current claim) 403 | Nothing; needs a browser | unchanged |

## Needs a browser (13 WHOOP facts, already manual sweep item 2)

research_program, program_eligibility, program_status, academic_vs_commercial, subscription_price,
academic_pricing, minimum_commitment, history_depth, export_routes [Member self-export], dpa,
gdpr_statement, soc2, data_residency. Pages: /us/en/research/, /us/en/unite/, /us/en/membership/,
/us/en/bulk-buy/, /us/en/terms-of-sale/, /privacy/full-privacy-policy/, and the Locker data-export
article.

## Left for the coordinator (outside this pass's files)

- `module-02-digital-phenotyping/README.md` line 130 and `module-02-digital-phenotyping/sources.md`
  row S-LD-02 still say LifeData's DPF status is "re-certification under review".
