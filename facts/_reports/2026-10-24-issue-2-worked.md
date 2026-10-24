# Issue #2 worked, 2026-10-24

Fact keeper pass on the 2026-10-19 report (`facts/_reports/2026-10-19.md`), sections Quotes missing,
Quotes reworded and Dead links only. Pages changed (295) and Check by hand (89) were not worked.

Every quote on every flagged fact was re-probed today against its live page (or `fetch_url`). Most
items had already been worked on 2026-10-21 (commit be1e5ed, "Fact keeper: work the 2026-10-19
weekly check"); those were confirmed exact and left alone. No fact value, status or confidence
changed today. `python3 tools/facts/validate.py`: 35 companies, 1340/1340 facts, 0 errors, 0 overdue.

## Items

### Quotes missing (15)

| Company | Field | What I found | What I changed | Confidence |
|---|---|---|---|---|
| withings | fda_clearances [Transtek BPMs] | Root cause found: openFDA `registrationlisting` returns one result by default (`limit=1`) and the order varies, so the quoted listing appears in some weeks and not others. K223374 has 3 results, K240102 has 8. With `&limit=100` both quotes are exact (K240102 was missing again today without it) | Added `fetch_url: ...&limit=100` to the K223374 and K240102 listing sources; `retrieved` 2026-10-24 on both. Same `fetch_url` fix applied to the K201456 (2 sources) and K230812 listing sources in withings.yaml, which carry the same risk | Verified (unchanged) |
| withings | derived_metrics | Already fixed 2026-10-21 ("96 biomarkers across 9 device families"); exact today | None | Verified |
| withings | export_routes | Already fixed 2026-10-21 (SDK line gone from llms.md; plans-page quote added); all quotes exact | None | Verified |
| fitbit-google | program_status | Already fixed 2026-10-21 ("Like what you see? Get started now"); exact | None | Corroborated |
| fitbit-google | developer_program_status [Google Health API] | Already fixed 2026-10-21; exact | None | Corroborated |
| beiwe | raw_streams | Already fixed 2026-10-21 (ambient audio removed, migration 0150 cited); all quotes exact | None | Verified |
| m-path | data_residency | Already fixed 2026-10-21 (privacy statement now names Azure in Germany); exact | None | Verified |
| apple | research_program [Investigator Support Program] | PMC13438180 quote exact today; last week's 0% was a fetch glitch | `retrieved` 2026-10-24 on the PMC source | Verified (unchanged) |
| fitbit-google | device_price [Pixel Watch 5 (US)] | Already fixed 2026-10-21 (list from $399.99); exact | None | Verified |
| lifedata | hosting_options | Already fixed 2026-10-21 ("a web hosting service such as Microsoft"); exact | None | Corroborated |
| lifedata | gdpr_statement | Already fixed 2026-10-21 (EU, UK, or Swiss residents wording); exact | None | Corroborated |
| lifedata | data_residency | Already fixed 2026-10-21; exact | None | Verified |
| withings | retention_terms [Inactive participant accounts] | Already fixed 2026-10-21 (13 octobre 2026 date; US 5-year clause); exact | None | Unclear (conflict) |
| withings | api_platform_fees | Already fixed 2026-10-21 (2018 fee-reservation quote dropped, moved to value text); exact | None | Verified |
| withings | retention_terms [API partners and own retention] | Already fixed 2026-10-21; exact | None | Verified |

### Quotes reworded (4)

| Company | Field | What I found | What I changed | Confidence |
|---|---|---|---|---|
| avicenna | program_status | Release-notes quote exact today; meaning unchanged | `retrieved` 2026-10-24 on the 2026-10-06 release-notes source | Verified (unchanged) |
| fitbit-google | device_price [Pixel Watch 4 (US)] | "Google Pixel Watch 4 From $349.99" exact today; price unchanged | `retrieved` 2026-10-24 | Verified (unchanged) |
| lifedata | retention_terms | 30-day quote exact today; the other four quotes also exact | `retrieved` 2026-10-24 on the 30-day privacy-policy source | Verified (unchanged) |
| lifedata | gdpr_statement | Already refreshed 2026-10-21; exact | None | Corroborated |

### Dead links (3)

| Company | Source | What I found | What I changed | Confidence |
|---|---|---|---|---|
| oura | `v2/docs` read via `openapi-1.41.json` | Already moved to `openapi-1.42.json` on 2026-10-21; 1.42 live and all 17 quoted facts exact; 1.43 not published. The versioned file name will break again at the next spec bump | None | Unchanged |
| apple | deprecations [HealthKit (iOS 27)], `earliestauthorizedsampledate(for:)` | Already replaced 2026-10-21 by `getearliestauthorizedsampledate(for:completion:)` (JSON `fetch_url`); quote exact | None | Verified |
| avicenna | derived_metrics, forum `t/1460` | Already handled 2026-10-21: topic removed, source dropped, GPS mobility features moved to a note as unclear. No source in the record cites t/1460 | None | Verified (fact value no longer claims the feature) |

## Profile and matrix lines that contradict the record

None of today's edits changed a value. These lines contradict values changed on 2026-10-21, which
the profiles were not fully brought into line with:

- `module-02-digital-phenotyping/profiles/avicenna-research-ethica.md:69` states platform-native GPS
  mobility features as fact; record says whether they still exist is unclear (t/1460 is 404).
- `module-02-digital-phenotyping/profiles/avicenna-research-ethica.md:160` same claim, in strengths.
- `module-02-digital-phenotyping/profiles/avicenna-research-ethica.md:297` reference 24 cites t/1460
  as Primary/Verified; it is now a dead page.
- `module-02-digital-phenotyping/sources.md:241` (S-BEI-16) says "optional Android ambient audio
  stream, off by default. Verified" and cites `study_models.py`; the backend removed it (migration 0150).
- `module-02-digital-phenotyping/profiles/beiwe.md:386` reference 20, same stale description.
- `module-02-digital-phenotyping/sources.md:270` (S-MP-13) says the m-Path privacy statement names
  KU Leuven as host (conflict with Azure); it now names Azure in Germany.

Checked and consistent: Withings profile (lines 140, 181, 307, 321, 372), Fitbit/Google profile and
Module 1 matrix lines 34, 50, 406 (Google Health API and Pixel Watch 5), Beiwe matrix line 118, m-Path
profile line 122, LifeData profile and Module 2 matrix (the policy still names Microsoft Azure in its
onward-transfer section).

## Check by hand (not worked; for the manual sweep)

| Company | Pages |
|---|---|
| evidation | 34 (site terms forbid automated collection) |
| activinsights-geneactiv | 29 (site terms forbid automated collection) |
| whoop | 9 (7 cited, 2 watched only; whoop.com and whoopunite.com return 403) |
| empatica | 7 (academic-support.empatica.com returns 403) |
| withings | 4 (3 support.withings.com pages, 1 accessdata.fda.gov PDF for K201456) |
| samsung | 2 (news.samsung.com timeout, techrepublic.com 403) |
| oura | 2 (accessdata.fda.gov PMA and 510(k) applicant searches) |
| lifedata | 1 (help.lifedatacorp.com 403) |
| FDA watched page | 1 (accessdata.fda.gov K221774, no facts cite it) |
| **Total** | **89** |

The accessdata.fda.gov items are expected: that site answers scripts with 404, and the README
already routes FDA quotes through an openFDA `fetch_url`.

## Follow-up suggestion

Other records cite openFDA `registrationlisting` or `510k` queries without `limit=`; any query with
more than one result can flicker between "exact" and "missing" from week to week, as Withings did.
Worth a one-off pass to add `&limit=100` fetch_urls where a quote depends on a specific result.
