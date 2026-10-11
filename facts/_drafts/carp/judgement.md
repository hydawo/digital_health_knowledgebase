# CARP judgement, 2026-10-11

Inputs: `facts/_drafts/carp/A.yaml`, `B.yaml`, `gaps.md`; previous `facts/carp.yaml` (every field
`unresearched`, so no old record claims to override); profile
`module-02-digital-phenotyping/profiles/carp-mobile-sensing.md`; matrix
`module-02-digital-phenotyping/comparison-matrix.md`.

Final record: 34 fields. 24 stated, 7 not_public, 1 conflict, 2 not_applicable, 0 unresearched.
Every quote re-probed "exact" on 2026-10-11. `validate.py --file facts/carp.yaml`: 0 errors.
`weekly.py --only carp --no-state`: 0 quotes missing, 0 reworded, 0 dead links (the 2 "pages changed"
are because there was no stored fingerprint to compare against).

## Where A and B disagreed

| Field | A | B | Decision and why |
|---|---|---|---|
| program_eligibility | conflict (hosting terms vs docs "Whoever you are...") | stated, hosting terms bind | **stated, Verified, B's reading.** Read both pages. carp.dk/hosting/ is the service's terms page (modified 2026-08-23) and says the service is "only provided for projects where we (DTU Health Tech) are an active research partner". The newest post (2026-09-28, new-carp-studies-app) says the same. The docs line sits in a list of three "ways in" between "DTU researchers can use the CAWS server hosted by DTU Health Tech" and "Run your own copy"; it is an invitation to make contact and does not say an outsider gets the DTU instance on other terms. Contact can end in a partnership or self-hosting, both consistent with the terms. A conflict needs the sources to disagree on the fact, and these do not. The docs quote is kept as a source and the reasoning is in the note. |
| minimum_commitment | stated, Corroborated (yearly invoicing, partnership) | not_public | **not_public.** Neither page states a minimum term or amount; yearly invoicing and the partnership rule are recorded in the note. |
| api_platform_fees | hosted setup fee placed here | no licence or API fees; hosted fees under hosting_price | **B.** The software carries no fee; the setup fee belongs to the hosted service and is in hosting_price. |
| academic_pricing | staff rates in value, quotes only for overhead and table label | no staff rates | **Merged**, with the staff rates now quoted from the table (student assistant and senior researcher rows). |
| hosting_price | 1,250 per study per month plus setup | same plus staff range and Computerome fee | **B, plus the column heading.** Checked the page: the table's price column is headed "Price pr. month", the setup row says "45.000 (one time)" and the hosting row "1,250 pr. study", so 1,250 DKK per study per month is right. "Price pr. month" is quoted as its own source so the monitor catches a heading change. |
| derived_metrics | CAWS Python pipeline exists (carp.dk/caws) | "No server-side analytics pipeline is documented" | **A.** carp.dk/caws says "A Python-based library allows researchers to program analysis scripts in Python and deploy these to the data processing pipeline" (exact). B's sentence was wrong. Gap hunter's carp-dsp repository added. |
| sampling_rates | defaults for light, heartbeat, upload | adds 200 ms (5 Hz) IMU default from code | **B**, plus the gap hunter's coverage finding in a source and note. |
| history_depth | Corroborated, no documented limit | Verified, historic sampling default one day; "kept at least five years" | **B's lookback, A's foreground-only quote.** Dropped B's five-year line, which is retention, not history depth. |
| rate_limits | not_public | stated: self sign-up 20 per minute per IP | **B.** The CAWS repository doc says "default 20/minute) guards against a single client hammering the endpoint" (exact). It is the only documented limit, scoped to that endpoint; A's pages checked are listed in the note. |
| retention_terms | conflict; Play quote from the data safety page; export retention 7 days | conflict; Play quote "Data can't be deleted" | **conflict, both Play quotes and the export setting kept.** Confidence Unclear (A) over Reported (B), since the two sides are both DTU's own statements. |
| deprecations | Firebase not on 2.x; namespace; API 2.0; repo move | API 2.0; legacy DataPoint and consent endpoints; Google Fit dropped in health plugin v11.0.0; namespace | **Merged.** Repo move (cph-cachet to carp-dk) dropped: no quote for it in either draft. Added the "Three Ways" post's stale "HealthKit / Google Fit integration" line as a source. |
| licence | MIT, seven repos named | MIT, five repos named | **Seven, verified on the GitHub API 2026-10-11**: carp.sensing-flutter, carp-webservices-spring, carp-portal, carp_study_app, carp.core-kotlin, carp-gardener, carp-cli all report MIT. |
| app_availability | China TestFlight, three languages | unlisted, iOS 15.0+, two languages | **Merged.** iTunes lookup API: seller Danmarks Tekniske Universitet, 5.1.0, current version 2026-10-06, first release 2025-03-21, languages DA and EN. Language discrepancy with CARP's post noted. |
| program_status | API 2.0 and v5 | carp.dk "WE WELCOME NEW PROJECTS." and v5 | Merged. |
| raw_streams | Studies-app subset, AWARE watch | SMS quote | Merged, plus gap findings (screen and battery from the v5 post, AWARE package, Gardener). |
| fda_clearances | four searches, no expect_absent | three searches with expect_absent | Merged to four searches, all with expect_absent. |

Fields where A and B agreed in substance and the better-sourced entry was kept: research_program,
program_application, developer_program_status, user_cap, academic_vs_commercial, device_price,
subscription_price, quote_required, export_routes, ai_training_terms, hosting_options, baa, dpa,
hipaa_statement, gdpr_statement, iso27001, soc2, data_residency.

## Gap findings

| # | Finding | Decision |
|---|---|---|
| 1 | Hosting page publishes prices | Accepted (academic_pricing, hosting_price, quote_required). |
| 2 | Hosting eligibility, research partner only | Accepted; decides program_eligibility. |
| 3 | iOS app on the App Store, unlisted | Accepted (app_availability), checked against the iTunes lookup API. |
| 4 | Novo Nordisk grant post names Geneva as a user | Not a record field. The quote holds, but it is a vendor claim about adoption; flagged for the profile below. |
| 5 | NNF DKK 5 million grant | Accepted into research_program. |
| 6 | CAG DIGITAL clinical academic group | Rejected for the record: a DTU-internal research collaboration, not a program outside teams can join. Profile candidate. |
| 7 | Reverse-direction DPA, joint controllership, research only | Accepted (dpa, academic_vs_commercial). |
| 8 | Five-year retention, service-improvement use | Accepted (retention_terms, ai_training_terms note). |
| 9 | No SLA | Accepted (hosting_price, hosting_options). |
| 10 | CAMS API 2.0 | Accepted (deprecations, program_status). |
| 11 | v5 data catalogue | Accepted in part: screen and battery quote into raw_streams, weekly cards into derived_metrics. |
| 12 | CARP Gardener | Accepted (raw_streams, licence, watch list). The v5 post calls it for "future studies", so it is recorded as existing code, not a live route in the Studies app. |
| 13 | AWARE Apple Watch package | Accepted (raw_streams). |
| 14 | carp-dsp | Accepted (derived_metrics). |
| 15 | Coverage tests, Android 14 and iOS 18 | Accepted as a sampling_rates source and note. |
| 16 | Upload bug, issue 623 | Not a deprecation; recorded as a note on export_routes. Read only, nothing opened or commented. |
| 17 | UbiLife study | Rejected for the record: evidence of use, not a fact field. Module 3 candidate once published. |
| Watch list | hosting, both privacy policies, App Store DK, Play, docs.carp.dk/carp-mobile-sensing/, carp-gardener | All added. |

## Statements in the profile or matrix that the record contradicts

Profile: `module-02-digital-phenotyping/profiles/carp-mobile-sensing.md`

| Line | Says | Record says |
|---|---|---|
| 10 | "no App Store listing was found on 2026-10-10 (Unclear)" | On the App Store, unlisted, id 1569798025, seller Danmarks Tekniske Universitet, 5.1.0 released 2026-10-06 (app_availability) |
| 12 | Hosted service "CAWS page: for DTU-affiliated researchers ... 'Three ways' page: email info@carp.dk" | Hosting terms: only projects where DTU Health Tech is an active research partner (program_eligibility) |
| 13 | "no price stated for the DTU-hosted service" | 45,000 DKK setup, 1,250 DKK per study per month, staff rates, cost plus 44% (hosting_price) |
| 36 to 38, 40, 43, 45, 47, 48 | Accelerometer, gyroscope, magnetometer, ambient light, screen, battery, Wi-Fi, Bluetooth "Unclear" | All documented in the available-packages table, with Android-only marks for light, screen and Wi-Fi (raw_streams) |
| 74, 117 | Active data collection and participant experience "Not verified in any pass to date" | v5 post documents surveys, cognitive tests, QR or code sign-in, battery-optimisation exemption (raw_streams sources) |
| 95 | "Conflict on who can use the hosted instance ... neither states a price" | No conflict once the hosting terms are read; price published |
| 110 | "No price is stated" | Price published |
| 131 | "neither carp.dk page states a price" | Price published on carp.dk/hosting/ |
| 142 (and 139) | One confirmed outside deployment | CARP's 2023 grant post also claims Geneva as a user (vendor claim, unverified) |
| 156, 169 | Hosted service "stated for DTU-affiliated researchers" | Open to non-DTU teams through a research partnership with DTU Health Tech |
| 177 | "Still open: whether non-DTU researchers can get accounts ... and at what cost" | Answered: partnership required; rates published |
| 189 | Hosted service terms at carp.dk/caws | Terms are at carp.dk/hosting/ |
| 105, 148 | MIT licence | Consistent; now verified on seven repositories |

Matrix: `module-02-digital-phenotyping/comparison-matrix.md`

| Line | Says | Record says |
|---|---|---|
| 54 | "CARP Studies" app not found on the App Store (Unclear); reference app on iOS Unclear | On the App Store, unlisted, 5.1.0 |
| 76 | Eligibility contrast between CAWS page and "Three ways"; "**price not stated**" | Partner-only per hosting terms; price published; no SLA |
| 118 | Integrations list | Omits CARP Gardener (Fitbit, Garmin, Withings, Dexcom cloud, described as future) and Apple Watch via AWARE |
| 137 | "DTU-hosted service (price not stated)"; "stated for DTU-affiliated researchers" | Price published; partner rule |
| 220 | "CARP's hosted service if you are not DTU-affiliated (access terms conflict)" | Not a conflict: outsiders need DTU Health Tech as an active research partner |

Also `module-02-digital-phenotyping/README.md` lines 152 to 153 ("Hosted-service prices are unpublished
for ... CARP's DTU service" and eligibility "contradictory on its own pages").

## For the coordinator

- Open question 131 in `shared/unresolved-questions.md` can be closed. Suggested text: "**Resolved
  2026-10-11 (Verified).** carp.dk/hosting/, the hosted service's terms (modified 2026-08-23), limits
  it to projects where DTU Health Tech is an active research partner: DTU helps initiate, fund and
  design the study and takes part in publication. The 2026-09-28 Studies app post says the same.
  Non-DTU teams can use it only through such a partnership; otherwise they self-host. The docs line
  'Whoever you are ... we'll find a way to support it' is an invitation to get in touch, not an
  alternative access route. The same page publishes 2024 rates: 45,000 DKK setup, 1,250 DKK per
  study per month, staff time at cost plus 44%, no SLA. See `facts/carp.yaml`."
- Q105's annotation repeats the old conflict ("one page restricts ... another opens to anyone") and
  could be pointed at the same resolution.
