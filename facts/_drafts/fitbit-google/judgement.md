# Judgement: fitbit-google (2026-10-10)

Final record: `facts/fitbit-google.yaml`, 44 facts (37 stated, 7 not_public, 0 conflict). Confidence:
31 Verified, 12 Corroborated, 1 Unclear. `validate.py`: 0 errors, 0 unresearched. `weekly.py --only
fitbit-google --no-state`: 57 pages, 0 quotes missing, 0 reworded. Every quote in the record was
confirmed `exact` against its live page. For FDA records the accessdata page is the `url` and the
openFDA query is the `fetch_url`.

Housekeeping: `weekly.py` overwrote `facts/_reports/2026-10-10.md` and deleted
`facts/_reports/latest-issue.md`. I restored both from git, so only the two permitted files changed.

## Where A and B disagreed

| Field | A | B | Decision |
|---|---|---|---|
| research_program | Policy designation plus Google Health Enterprise | Policy designation plus the "Research Application" form on healthapp.google/published-studies | Merged. Both quotes are exact. Added gap 6 (the enterprise contact form lists "Researcher") and gap 7 (the 2021 Health Equity initiative) as a historical note |
| program_status | Policy in force but no intake open | Old researcher pages redirect, and a research form is still linked | Merged. B's form is real, but what it leads to is unknown, so the status stays "not onboarding" with the form mentioned |
| developer_program_status | Split by scope (Google Health API / legacy) | One combined entry | Used A's split. Added the 24 March 2026 launch date (gap 4) and Validic's description of the new-project requirement. Added closed legacy registrations (gap 16, one integrator, flagged in a note) |
| academic_vs_commercial (Google Health API) | `stated`, no academic tier, citing the Developer and User Data Policy | `not_public` | Used `not_public`, because the field asks for a difference and none is published. A's policy point went into the note |
| device_price, Fitbit Air | $99.99 from 9to5google, Reported | $99.99 from the Google Store, Verified | B wins: the store page shows the price |
| device_price, Pixel Watch | Pixel Watch 4 from $349.99 | Pixel Watch 5 from $349.99, list $399.99 | Both are on the Google Store, so both are kept, scoped by model |
| subscription_price, annual | $99/year (Google blog) | $99.99/year (droid-life) | Google's own blog says $99. I used the vendor figure and noted the press figure. I did not record a conflict: one side is the vendor and the other is press repeating an earlier price |
| api_platform_fees confidence | Corroborated | Verified | Corroborated. The fee range is Verified, but "no API fee" is inferred. Added the CASA Accelerator and annual renewal (gap 13) |
| minimum_commitment | `stated`: Premium can be cancelled anytime | `not_public` for enterprise | Kept both, scoped (consumer Premium: stated; Google Health Enterprise: not_public) |
| quote_required confidence | Corroborated | Verified | Verified, since the contact-form text says it directly |
| raw_streams | ECG raw waveform samples are a raw signal | No raw signals at all | A is right: the Vitals guide lists "raw waveform voltage samples". Merged with B's sync-path quote |
| derived_metrics | Release-notes list | Longer data-types list | Merged. Added the Pixel Watch step-count incident (gap 11) as a data-quality note with two status-dashboard quotes |
| sampling_rates | HR 1 s, steps 1 min, legacy 1sec/1min/5min/15min | Same, plus sync every 15 minutes | Merged. B's sync quote no longer matched the page, so I replaced it with the current wording ("every 15 minutes if Bluetooth is active..."). Added the newsletter's intraday claim (gap 10) |
| export_routes | API only | API, self-export, Device Connect, Fitabase | Merged, then split into three scoped facts: cloud and self-export; intermediaries; on-device (see gaps 1 and 2) |
| retention_terms | Developer obligations | Same, plus "kept until the user deletes it" | Merged |
| ai_training_terms | `not_public` | Split: Google's own use stated, developer terms not_public | B's split. "60 million hours ... used to train Google Health's AI models" is an exact quote on healthapp.google/our-research |
| deprecations | API dates, token re-consent, May 19 login cutoff | API dates, Friends endpoints, Ace unsupported | Merged, then split into an APIs fact and an accounts, Google Fit and devices fact, with gaps 3, 8, 9, 14, 15 and 17 added |
| baa | `stated`, Corroborated | `unclear` | Split by scope. Google Health API: `stated` (the terms say no HIPAA obligations and require written consent for PHI). Google Health Enterprise and Device Connect: `not_public`, Unclear, because only 2015 and 2016 press mentions an enterprise BAA |
| dpa | Fitbit controller terms plus Google Controller-Controller terms via the Google APIs Terms | Fitbit controller terms only, "no Google Health API equivalent found" | A is right. The Google Health API terms say "By using this API, you consent to be bound by these terms, the Google APIs Terms of Service", and those terms bring in the Google Controller-Controller Data Protection Terms |
| data_residency confidence | Corroborated | Verified | Corroborated, because "no residency option" is inferred |
| academic_pricing confidence | Corroborated | Verified | Verified, the usual confidence for a dated not_public |

The two drafts agreed on program_eligibility, program_application (merged both sources), user_cap
(added Validic's 100-user report), history_depth, rate_limits, hipaa_statement, gdpr_statement,
iso27001, soc2 and fda_clearances.

## Gap findings

| # | Finding | Decision | Why |
|---|---|---|---|
| 1 | Unified APIs (Thryve, Validic) need each customer's own Google project | **Accepted**, Corroborated | Thryve quote exact. I also confirmed it independently on Validic's status page (trust.validic.com, exact): "It requires a new Google Cloud project, credentials, OAuth verification from Google", and the 100-user cap applies to "your production Google Health credentials". Two independent integrators agree, but no Google page addresses intermediaries, so the confidence is Corroborated. Nuance: Validic's customers are opening new projects now, which suggests "not onboarding new projects" may apply only to developers without legacy access. Google does not say so, and the record marks it Unclear |
| 2 | On-device route through Apple Health and Health Connect | **Accepted**, Corroborated | The Apple Health direction is Verified from Google's own help page (support.google.com/googlehealth/answer/17037331), which lists the types Google Health writes. HRV and skin temperature are not written. The Health Connect write direction and the "avoids credentials, OAuth verification and CASA" framing come from Thryve only. That fits Fitbit's Health Connect support since 2022, but I found no current Google page for it. Density and fidelity compared with the API are untested |
| 3 | Fitbit-account cutoff 19 May, deletions from 15 July, no Workspace accounts | Accepted, Verified | All four quotes exact on Google's help page |
| 4 | Launch 24 March 2026, not late May | Accepted | The release notes entry is exact |
| 5 | FDA records | Accepted (already in both drafts) | Verified through openFDA fetch_url. Whether Body Temperature Software runs on a wearable is left in the note as unchecked |
| 6 | Enterprise form lists "Researcher" | Accepted into research_program | Exact quote. It is a sales lead, not a program |
| 7 | 2021 Health Equity Research Initiative | Accepted as a historical note only | Exact quote. One round only, so it is not current |
| 8 | Turn-off moved to 30 October for CASA delays | Accepted, secondary | Exact quote |
| 9 | Fitabase reconnect by 31 October, brown-outs, new export columns | Accepted | Exact quotes. Google's 30 October date governs, as the note says |
| 10 | Newsletter: intraday data for all relevant types | Accepted into sampling_rates | Exact quote. It agrees with the about-page quote |
| 11 | Pixel Watch step-count incident, 95 days from 20 March 2026 | Accepted into the derived_metrics note | Exact quotes on Google's status dashboard |
| 12 | Thryve: no published lookback limit | **Rejected** | Google's endpoints page says the API "imposes no limitations or restrictions on the amount of historical data". The vendor's statement wins over the third party's. Thryve's point is about recovering data after a gap, and is noted |
| 13 | CASA renews every year; accelerator for ISO 27001 or SOC 2 holders | Accepted, secondary, in api_platform_fees | Exact quote |
| 14 | v4beta channel; webhook retries for 7 days | Accepted | Exact quotes |
| 15 | Google Fit sunset on Google's own pages | Accepted, Verified | Exact quotes |
| 16 | Legacy registrations closed | Accepted, noted as one integrator's report | Exact quote. Moot after 30 October |
| 17 | Device update policy (two years after last sale) | Accepted | Exact quote |
| 18 | Google's own R&D use with user consent; nothing in the developer terms | Accepted (same as B) | Exact quotes |

## Statements in the profile and matrix that the record contradicts

Profile = `module-01-wearables/profiles/fitbit-google.md`; matrix = `module-01-wearables/comparison-matrix.md`;
intermediaries = `module-01-wearables/profiles/data-intermediaries.md`.

| File, line | Says | Record says |
|---|---|---|
| Profile 26 | New-study routes are "an intermediary that already holds access (Fitabase, or a unified API)", self-export, All of Us | Unified APIs (Thryve, Validic) need each customer's own Google Cloud project, verified app and CASA, so they are not a way around the freeze. Also missing the on-device route through Apple Health and Health Connect, which needs no Google Health API project |
| Intermediaries 212 | "An intermediary that already holds Google Health API access (Fitabase or a unified API)" | Same as above. The Fitabase part is plausible; the unified-API part is contradicted |
| Intermediaries 20; matrix 350-351 and 376 | An intermediary already holding access is the main way to reach Fitbit data | Same. Also needs the on-device route as an alternative |
| Profile 213 | Health Connect is a separate Android path (and there is no Apple Health route) | Google Health writes to Apple Health (since August 2026) and to Health Connect, and that route skips Google Health API credentials |
| Profile 38 | Google Health API "Opened late May 2026" | Launched 24 March 2026 (release notes) |
| Profile 39 | 19 May 2026 given only as the app rebrand date | 19 May 2026 also ended Fitbit-account logins; deletion of unmigrated data began 15 July 2026; Workspace accounts cannot be used |
| Profile 44 | Google Fit sunset "Corroborated" | Verified on Google's pages; no new sign-ups since 1 May 2024 |
| Profile 13, 87-100, 174-180, 266 | Intraday "Unclear, leaning negative"; intraday "gated case by case and can be refused" | In the Google Health API, intraday data is available for all relevant types through the list endpoint (about page, August newsletter). Case-by-case approval was a legacy-only process |
| Profile 104 | Fitbit Air $99.99 "Corroborated ... not read from Google's store page" | Verified from the Google Store page |
| Profile 240; matrix 217 | Premium $99.99/year (Reported) | Google's blog says $99/year, $9.99/month |
| Matrix 217 | Fitbit Air $99.99 (C) | Verified |
| Profile 294; matrix 157 | Historical and backfill depth open or "Unclear" | Google says there is no limit on historical data; rollups are capped at 14 or 90 days per query |
| Matrix 243 | Regulatory column "Not itemised in the profile" | Five FDA records: K200948, K212372, DEN230050, K243778, K242967 |
| Matrix 385 | "AI-training terms not covered" | Google trains its own Health AI on wearable data, and users can opt in to sharing; developer terms have no AI clause |
| Profile 188 | "no first-party research console" (no research route mentioned) | Still true for a console, but a research application form is linked from healthapp.google/published-studies, and Google Health Enterprise takes "Researcher" enquiries |
| Profile 231 | "No BAA offer is published" | Consistent for the API. Enterprise BAA status is not public (not a contradiction, but the scope is worth noting) |

## For the coordinator to check by hand

1. Whether the "not onboarding new projects" freeze stops a new Validic or Thryve customer from creating
   its own Google Health API project. Validic's customers are creating projects now. If they can, the
   unified-API route is open but costly (CASA). If they cannot, it is closed. The record marks this
   Unclear.
2. The Health Connect write direction from Google Health: I found no current Google help page. Thryve
   and 2022 press support it.
3. Fitabase: whether it can add new customer studies under its own Google Health API project.
4. The healthapp.google research application form needs a Google sign-in, so I did not read it.
5. The host device for Body Temperature Software (DEN230050, K243778).
