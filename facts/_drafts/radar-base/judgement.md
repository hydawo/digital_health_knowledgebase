# RADAR-base: judgement, 2026-10-10

Inputs: `A.yaml`, `B.yaml`, `gaps.md`, and the starter `facts/radar-base.yaml` (all `unresearched`). Output: `facts/radar-base.yaml`, 39 entries (28 stated, 9 not_public, 2 not_applicable, 0 conflict), 15 watched pages. All 84 quotes matched "exact" with `quote_probe.py` on 2026-10-10. Validation and weekly-check results are in the last section.

## Fields where A and B disagreed

| Field | A | B | Decision and reason |
|---|---|---|---|
| program_eligibility | Verified | Corroborated | Verified. The page does say who the service is for; the value states that no eligibility rule is published, which is a dated observation, not uncertainty. |
| academic_vs_commercial | Verified | Corroborated | Corroborated. "No difference" rests on the absence of separate terms. |
| subscription_price | not_public, scoped to The Hyve's service | not_applicable (no consumer subscription; hosting price under hosting_price) | not_applicable. Avoids recording The Hyve's unpublished price twice. |
| quote_required | Verified | Corroborated, "inferred from no price plus inquiry route" | Corroborated. Read the page: no "contact for pricing" sentence exists. |
| rate_limits | not_applicable (no central API) | not_public, with repos checked | not_public. Each deployment does run APIs (REST API, gateway); no limit is documented. A's point kept in the note. B's Fitbit connector poll interval (150 s) confirmed on the REST-Connector README and kept in the note. |
| history_depth | Verified | Corroborated | Corroborated. "No platform limit" follows from self-hosting, not a statement. |
| ai_training_terms | Two entries (Google Health stated; platform and The Hyve not_public) | One entry mixing both | A's split kept; B's demo-service point added to the not_public note. |
| deprecations | Two entries | One combined entry, plus HDFS and iOS dormancy | Three scoped entries: the new Fitbit route (gap 1), deployment and export (RADAR-Docker, HDFS), device integrations (Faros, Biovotion, Pebble, Garmin OAuth 2.0, iOS repo). |
| app_availability | Three scoped entries | One combined entry | A's three scopes, with B's sources, plus the Play data-safety declarations. |
| app_availability (iOS pRMT) | "last pushed June 2023" | "no push since June 2023" | Both used the GitHub `pushed_at` date. The API shows last commit 2021-01-19 and last push 2023-06-20; the record gives both. The profile's 2021-01-19 is the commit date and is right. |
| derived_metrics | "No built-in behavioural feature library" | Adds radarpipeline | Merged: not built in, but a companion package exists. |
| user_cap, program_application, program_status, developer_program_status, export_routes, licence, hosting_options, retention_terms, data_residency, gdpr_statement, iso27001 | Agreed in substance | Agreed in substance | Merged quotes and detail from both. |

## Gap hunter findings

| Finding | Decision | Why |
|---|---|---|
| 1. Fitbit route mid-migration; no released ingest for Google Health | Accepted, as its own `deprecations` entry (Fitbit route), Verified | Checked with the GitHub API. PushEndpoint PR #92 is open and unmerged (updated 2026-06-05); newest PushEndpoint release is v0.4.0 (2025-06-19). I also checked the pull side, which the gap hunter did not: RADAR-REST-Connector's latest release is v0.7.5 (2026-03-25), its README shows the Fitbit connector calling `api.fitbit.com/1/user/...`, `google-health-library` on `dev` is a stub (one build file), and its Google Health converter PRs (#199, #201, #202, #215) are open. Released so far: auth (Rest-Source-Auth v4.4.16, 2026-07-03, "Added new Google Health authorization") and schemas (RADAR-Schemas, `commons/push/googlehealth`, PR #424 merged 2026-06-25). So the claim holds: no released component ingests Google Health API data. |
| 2. Google User Data Privacy Policy (AI ban, London residency, token deletion, scopes) | Accepted (ai_training_terms, data_residency) | Quotes exact. Token-deletion and scope list not needed in the record. |
| 3. The Hyve ISO 27001:2022 | Accepted, Corroborated | Article quote and the homepage "ISO27001 certified" both exact. No certificate found, so Corroborated is the cap. Hyve Managed Hosting (UK) not cited. |
| 4. aRMT policy: 60-day deletion, Firebase to developers, developers cannot delete | Accepted (retention_terms, gdpr_statement) | Quotes exact. |
| 5. Audio collected; camera PPG plugin | Accepted (raw_streams) | Quotes exact. |
| 6. Wider wearable catalogue; Dexcom | Polar, Oura and E4 accepted with quotes; Dexcom in the note only (Reported) | The Dexcom post describes an internship project; the Supported Devices page does not list it. |
| 7. Garmin OAuth 2.0; Huawei in progress; no Health Connect | Accepted | Garmin quote exact and in deprecations. Huawei schemas (v0.9.0) and auth (v4.4.16) are released but connector PR #204 is open, so it is not shipped. Health Connect issue title quoted. |
| 8. radarpipeline | Accepted (derived_metrics) | Quote exact. |
| 9. Self-enrolment portal, app kit, RFC process | Note only (hosting_options) | No schema field; neither is presented as a released product. |
| 10. Export formats and support channels | Accepted (export_routes, developer_program_status) | Quotes exact. |
| 11. RATE-AF cited in UK 10 Year Health Plan | Rejected | Evidence of use, no schema field. |
| Lead: KCL job posting on SaMD / ISO 13485 plans | Kept out of the record | Page returns 404 and no archived copy was read. Not checked further, as instructed. |
| Lead: Onsentia Limited | Note only (aRMT app_availability) | Seller name is on the App Store listing; who they are is unknown. |

## Checks the coordinator asked for

- **Fitbit shutoff.** The Fitbit Web API turns off on 2026-10-30 (Fitbit's intraday page, exact quote). As of 2026-10-10, a study collecting Fitbit data through any released RADAR-base install will stop getting new Fitbit data on that date unless a Google Health ingest release ships first, or the team deploys unreleased branch code. Participants will also need to re-authorise through Google, because Google Health authorization is a new grant. Data already collected is unaffected. The Google Health API is closed to new projects (`facts/fitbit-google.yaml`), so a self-hosting team without its own Google Health project may have no route at all; the radar-base.org Google User Data Privacy Policy suggests KCL has one for its own deployment. The Hyve's managed service page still advertises Fitbit training. RADAR-base's own tracking issue said "by September 2026", earlier than Google's 30 October date. Record re-check set to 2026-10-31.
- **Play data safety.** Confirmed exact on the passive app (`org.radarcns.detail`): "Data isn't encrypted", "Your data isn't transferred over a secure connection", "Data can't be deleted". The active app (`org.phidatalab.radar_armt`) declares "Data is encrypted in transit" and also "Data can't be deleted". The encryption declaration contradicts the platform docs (radar-commons sends data "using HTTPS requests") and is probably a wrong form entry. RADAR-Kubernetes uses TLS by default, but it has a `disable_tls` option, so encryption in transit depends on the deployment. "Can't be deleted" fits the privacy policy's model (developers cannot delete; the deployment owner does). Recorded under app_availability (pRMT) and retention_terms.
- **ISO 27001.** The Hyve B.V. only, Corroborated, no certificate found. Hyve Managed Hosting not cited anywhere.

## Statements in the profile or matrix that the record contradicts

| File | Line | What it says | What the record says |
|---|---|---|---|
| module-02-digital-phenotyping/profiles/radar-base.md | 18, 26, 123, 138 | Fitbit presented as a working REST integration; Huawei named as a partner for wearable integration | Fitbit route stops on 2026-10-30 with no released replacement as of 2026-10-10. Huawei connector is unreleased (PR #204 open) |
| module-02-digital-phenotyping/comparison-matrix.md | 108, 185 | Garmin, Huawei, Empatica named as partners; "The Hyve trains on Fitbit and Garmin" | Same Fitbit and Huawei points. Oura and Polar integrations, listed on Supported Devices, are missing |
| module-02-digital-phenotyping/profiles/radar-base.md | 51 | Audio / microphone row all "Unclear" | Android audio collected as openSMILE features (plugin), and the Get Started page lists audio among pRMT streams. Camera-PPG plugin also exists |
| module-02-digital-phenotyping/profiles/radar-base.md | 67, 155 | Built-in feature catalogue "not independently verified"; open question | No built-in catalogue; feature generation is the separate radarpipeline package |
| module-02-digital-phenotyping/profiles/radar-base.md | 104, 132, 153 | No ISO documentation located | The Hyve states ISO 27001:2022 certification (Corroborated, self-claim, scope does not name RADAR-base) |
| module-02-digital-phenotyping/comparison-matrix.md | 147 | "No HIPAA, SOC 2 or ISO statement located" | As above for ISO; HIPAA and SOC 2 still not published |
| module-02-digital-phenotyping/profiles/radar-base.md | 104 | No retention or deletion term | Active-app policy: deletion including backups generally within 60 days, via the deployment owner; developers cannot delete |
| module-02-digital-phenotyping/comparison-matrix.md | 147 | Residency only for The Hyve | Google Health integration data held in AWS eu-west-2 (London) or university infrastructure; no AI training on that data |
| module-02-digital-phenotyping/profiles/radar-base.md | 79 | Export covered as Kafka streaming only | AVRO, JSON and CSV export, restructure tool, REST API, Upload Connector |
| module-02-digital-phenotyping/profiles/radar-base.md | 102 to 105 | Nothing on encryption in transit | Passive app's Play listing declares data not encrypted in transit (contradicts docs; flagged) |
| module-02-digital-phenotyping/comparison-matrix.md | 191 | RADAR-base reads Apple HealthKit (implying no Health Connect) | Consistent: Health Connect is an open feature request (issue #488). No contradiction, noted for completeness |

## Validation

`validate.py --file facts/radar-base.yaml`: 39/39 researched, 0 errors. `weekly.py --only radar-base --no-state`: 48 pages, 0 quotes missing, 0 reworded. Four "dead links" are the openFDA negative searches in fda_clearances, which return 404 for "no matches" (expected per facts/README.md). One "page changed" (radar-base.org/) is the first-run fingerprint with no prior state.

## For the coordinator to check by hand

- Re-check RADAR-PushEndpoint, RADAR-REST-Connector releases and PR #92 just before 2026-10-30. A release in the next three weeks would change the Fitbit entry.
- Whether the passive app's "not encrypted in transit" Play declaration is a form error. Only the developer (The Hyve) can answer; worth a line in `shared/unresolved-questions.md`.
- The Hyve's ISO 27001 renewal (a 2023 certificate would lapse around late 2026) and whether its scope covers RADAR-base as a Service.
- KCL SaMD / ISO 13485 lead remains unconfirmed and out of the record.
