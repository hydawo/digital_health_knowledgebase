# Avicenna Research (formerly Ethica): judgement (baseline run, 2026-10-11)

Inputs: `A.yaml`, `B.yaml`, `gaps.md`. Output: `facts/avicenna.yaml`. Every quote in the final record
was re-run through `tools/facts/quote_probe.py` on 2026-10-11 and returned `exact` (94 quotes).
`validate.py --file facts/avicenna.yaml`: 0 errors, 34 of 34 fields researched.
`weekly.py --only avicenna --no-state`: 48 pages, 0 quotes missing, 0 reworded, 0 dead links. One
"page changed" (the security post), which is only the first fingerprint against old state. The
`/pricing` 404 is marked `expect_absent`. Neither script needed the scratch-copy fallback.

UKAS CertCheck was not opened (CAPTCHA). No account, sign-in, form or GitHub issue.

**Documentation location.** Avicenna's documentation now lives on its Discourse forum
(forum.avicennaresearch.com); learn.avicennaresearch.com links redirect there. Forum topics get
renamed and recategorised (Product Ideas cards move between To Do and Done), so these URLs are less
stable than a static docs site. The record's header says so. Expect more reworded or moved quotes in
the weekly check for this company.

## Status counts

| Status | Count |
|---|---|
| stated | 22 |
| not_public | 8 |
| not_applicable | 2 |
| unclear | 1 (baa) |
| conflict | 1 (data_residency) |

Confidence among stated facts: Verified 16, Corroborated 6 (program_eligibility, history_depth, dpa,
hipaa_statement, gdpr_statement, iso27001).

## The points the coordinator asked me to settle

1. **On-premise and white-label.** Settled as `stated`, Verified, under hosting_options. The
   white-label page offers "from eventual in-house storage to full on-premises installation". The
   REDCap and mEMA comparison pages, the product card for on-premise subdomains (t/1009) and the
   2026-09-22 Garmin post ("an institution's own Avicenna infrastructure") show on-premise
   deployments exist in practice. **One gap-hunter source I did not use for this:** the security
   post's "on-premise servers running Rocky Linux 9.x" sits in a list of Avicenna's own internal
   systems (Proxmox, GitLab, Mattermost, Zammad, Keycloak). I read it as Avicenna's own
   infrastructure, not customer installs. It is noted, not cited. This is vendor-installed closed
   software, not open-source self-hosting. Price and terms are not public.
2. **Export API.** *Documented:* a how-to article (t/1496, posted 2026-02-09) describes a Data Export
   API for **sensor data**: key on request from support, header `Authorization: ApiKey
   USERNAME:API_KEY`, POST `/api/study/export/create/`, poll GET `/api/v1/filter/export/`, download.
   The endpoint the gap hunter found in NiDB is therefore in the vendor's own documentation as the
   status-polling route. B was right and A ("no API found") was wrong. *Inferred:* NiDB also POSTs a
   JSON `"filter": "PARTICIPATION"` body to `/api/v1/filter/export/` to export survey participation
   records. The vendor does not document that, so it sits in a note. The roadmap card "Export Data
   with API" (t/1406, 2025-09-29, "to follow OpenAPI Compatible APIs") predates the how-to and is
   still under To Do. It most likely means a fuller, OpenAPI-style API, but the card does not say so.
   developer_program_status: `stated`, Verified. rate_limits: `not_public` (no request limit is
   published; export size caps go in the note).
3. **Data residency.** `conflict`, Unclear. I confirmed four vendor statements that do not agree.
   The security post says all data is in Canada with Canada-based staff. The privacy policy says data
   may be stored "in our servers in Canada". The privacy policy's children's-data section says UK/EEA
   data stays in the UK/EEA unless safeguards are in place. The legal page claims an
   "infrastructure-agnostic approach" to residency. The security post also lists AWS EC2 with no
   region. The Server Region card (t/1031) is under To Do but reads "Closed epic: OP-9223", so it
   settles nothing. A recorded `stated`/Canada and B recorded `conflict`. B's reading is right.
4. **ISO 27001.** `stated`, Corroborated (capped as a self-claim). "Through UKAS", with no
   certification body, certificate number or certificate. UKAS accredits certifiers and does not
   certify companies. A third vendor source was added: the 2025-11-18 release notes on the
   surveillance audit.
5. **ICO and DSPT.** Both quotes are confirmed. They are used under gdpr_statement for what they
   establish. ICO ZC009135 (registered 2025-10-07, expires 2027-10-06) is a fee-payer registration.
   DSPT AVRESC001 shows a 2025-26 self-assessment marked "Standards met" on 25 November 2025. Neither
   is ISO evidence, and neither proves GDPR compliance. gdpr_statement therefore stays Corroborated
   even though the validator would allow Verified with a regulator_db source. ICO is typed
   `regulator_db`. DSPT is typed `certificate`, since the schema defines that type as a registry
   entry. The security post calls the DSPT entry a "certification", which overstates it.
6. **Pricing.** /pricing 404 recorded with `expect_absent`. Free Trial (data wiped monthly, study
   deleted after a year). Paid licence by email with the study ID. SMS at Twilio cost plus 30%, off by
   default. The Capterra figure is left out, with a one-line mention in academic_pricing's note.
7. **Retention.** At least two years after contract termination. The quote is confirmed.
8. **Forum documentation.** Noted in the record header and above.
9. **White-label apps and the JMIR paper.** iTunes lookup for seller 1137173051 returned 34 apps: the
   main app, Avicenna Keyboard and 32 study-branded apps, so 33 besides the main app, 13 of them first
   released in 2026. The JMIR mHealth 2025 paper (10.2196/67519) quotes are confirmed through
   Europe PMC: a customised Android app (Sesikhona), and "95.3 out of the expected 336 points
   (28.4%) weekly". Both go under app_availability with a note.

## Fields where A and B disagreed

| Field | A | B | Decision and reason |
|---|---|---|---|
| program_eligibility | stated: open sign-up, no academic rule | stated: privacy policy defines Researcher as academically affiliated, 18+ | Merged both. Corroborated, because the sign-up flow and the policy definition point different ways. Both are quoted. |
| developer_program_status | unclear: no API found | stated: Data Export API, key from support | B. The how-to article is live and documents endpoints (see point 2). |
| rate_limits | not_public | stated (export caps scoped as rate limits) | not_public. The field is API request limits, and none are published. B's export caps are kept in the note. |
| history_depth | stated, Corroborated (Fitbit exclusion, inferred no backfill) | not_public | A. The Fitbit pre-start exclusion is stated outright. The broader no-backfill reading is inferred, so Corroborated. |
| derived_metrics | Corroborated: "no platform-native features" (security page) | Verified: no built-in feature pipeline | Both overruled by gap finding 11. The GPS mobility-features reference (t/1460) documents a nightly batch computing distance, radius of gyration, entropy, time at home and clusters. The Analysis page was added 2026-03. Verified. |
| export_routes | dashboard, Kibana, database on request; no API | adds Data Export API and "database access only if self-hosted" | B, plus NiDB as inferred corroboration. Both database-access statements are kept, since they come from different forum posts. |
| api_platform_fees | single stated entry | split into licence not_public and SMS stated | Single stated entry, A's shape with B's content plus "SMS not enabled by default". |
| licence | Verified | Corroborated | Verified. The terms state ownership directly, and the company GitHub holds no platform code. |
| hosting_options | value names Canada servers | value without it | B's wording plus four on-premise sources. Residency belongs in its own field. |
| data_residency | stated, Corroborated (Canada) | conflict | conflict (point 3). |
| gdpr_statement | ICO and DSPT typed certificate | both typed regulator_db | ICO is regulator_db and DSPT is certificate (point 5). Corroborated either way. |
| hipaa_statement | security-page quote | adds SensorKit-approval quote naming Part 11 | B's quote kept. It is the only source naming 21 CFR Part 11. |
| deprecations | includes GraphQL-to-REST | without it | Union, plus WHOOP v1-to-v2 from gap finding 8. |
| app_store URL | /app/avicenna-research/id1137173052 | /app/ethica/id1137173052 | Same id. Used A's slug, which matches the current title. |
| recheck_by | 2026-11-09 / 2027-01-08 | same | Recomputed from today: 2026-11-10 and 2027-01-09. |

## Gap findings

| # | Finding | Decision |
|---|---|---|
| 1 | On-premise deployments | Accepted, except the Rocky Linux line (point 1). |
| 2 | Export API in NiDB | Accepted. Narrowed: the vendor documents the sensor-export API, and only the participation-export use is inferred (point 2). |
| 3 | Residency: infrastructure-agnostic, Server Region card | Accepted into the conflict. |
| 4 | White-label app volume | Accepted (point 9). |
| 5 | Avicenna Keyboard app | Accepted as a note in raw_streams and counted in app_availability. |
| 6 | DSPT entry | Accepted under gdpr_statement as a self-assessment. |
| 7 | ISO surveillance audit release note | Accepted as a third iso27001 source. |
| 8 | Oura, Mira, Buzud CGM, WHOOP v2, Garmin SDK rates | WHOOP v2 went into deprecations. The Garmin HR/SpO2 1 s to 1 h rate went into sampling_rates. Mira went into the raw_streams list. Buzud CGM was not added: the quote is fine, but I did not confirm a matching data-source entry, so it is left for the profile pass. |
| 9 | SensorKit per-study approval | Accepted into program_application. |
| 10 | iOS Screen Time app usage | Accepted into raw_streams. |
| 11 | GPS mobility features, Analysis page | Accepted into derived_metrics. |
| 12 | SMS pricing | Accepted (both researchers had it). |
| 13 | Retention, AI chatbot | Retention accepted. The chatbot is mentioned in the ai_training_terms note only. |
| 14 | Android foreground notification | No schema field. Not recorded. Relevant to the profile's keepalive wording (below). |
| 15 | Papers | The Sesikhona paper was used. Stoma QoL and Texas A&M are evidence of use with no schema field, so not recorded. |

## Statements in the profile or matrix that the record contradicts

Profile: `module-02-digital-phenotyping/profiles/avicenna-research-ethica.md`. Matrix:
`module-02-digital-phenotyping/comparison-matrix.md`.

| File, line | Says | Record says |
|---|---|---|
| profile 12 | "Vendor SaaS only ... No self-hosting." | hosting_options: managed by default; white-label up to full on-premises installation on customer infrastructure (vendor-installed, closed source). |
| profile 85 | Vendor-hosted SaaS; no self-hosting option identified | Same as above. |
| profile 128 | "vendor-hosted only, no self-hosting" | Same as above (the "closed-source" part stands). |
| profile 142 | Self-hosting or full data custody "not offered" | On-premises installation is offered. Source-code auditability is still not offered. |
| profile 154 | White-label availability "still open" | White-label is a working service with 33 further iOS apps under Avicenna Research Inc. Cost is still unpublished. |
| matrix 73 | "Vendor SaaS only; data on servers in Canada" | hosting_options as above; data_residency is a conflict. |
| profile 76 | "No export API exists yet" | export_routes: Data Export API documented 2026-02-09, key from support. |
| profile 80-81 | No developer/public API; roadmap card "confirms the absence" | developer_program_status: API exists and is documented. The roadmap card is still To Do but predates the article. |
| profile 130 | "No researcher-facing export API exists yet" | As above. |
| profile 143 | Documented public API "not confirmed to exist" | A documented (how-to level) export API exists. There is no full reference. |
| profile 151 | "Answered 2026-10-10: no" export API | Wrong; see export_routes. |
| shared/unresolved-questions.md 294 (#90) | "Avicenna has no export API" | As above. |
| profile 63 | Derived metrics "Not verified in any pass to date" | derived_metrics: nightly GPS mobility features, Analysis page, phone and wearable derived metrics. |
| profile 34-53 | Most passive streams "Unclear" | raw_streams lists accelerometer, gyroscope, magnetic field, light, pressure, proximity, Wi-Fi, battery, screen state, app usage (iOS via Screen Time), keyboard and more (Raw Data reference). |
| matrix 51, 115 | Most streams unverified; Garmin SDK wrist status only | Same as above; Garmin SDK raw 25 Hz accelerometer, 32 Hz gyroscope, BBI. |
| profile 101, matrix 73 and 158 | Data in Canada (vendor-stated), with the UK/EEA line "recorded as found" | data_residency is a conflict that also includes "infrastructure-agnostic" and AWS EC2 with no region. |
| profile 105, 131; matrix 158 | 21 CFR Part 11 "not mentioned anywhere read" | hipaa_statement: the SensorKit approval guide claims Part 11 compliance (vendor-stated). |
| profile 101, 107; matrix 158 | ICO registration only; DSPT not mentioned | gdpr_statement: NHS DSPT 2025-26 self-assessment "Standards met" also exists. |
| shared/unresolved-questions.md 314 (#84), 367 (#93) | Avicenna has an "independently audited" ISO certificate (Verified) | iso27001: self-claim, Corroborated, no certificate read. The profile already corrected this on 2026-10-10. The unresolved-questions rows still carry the old wording. |
| profile 93, matrix 180 | "No phone-app keepalive" | Not a schema field, but gap finding 14 (Android's permanent foreground notification keeps the app alive, t/1574) makes the flat wording misleading. Worth a qualifier. |

## For the coordinator to check by hand

- **UKAS CertCheck** (link in the security post) is the only route to independent ISO evidence. It
  needs a human to pass the CAPTCHA. If it names a certification body and scope, iso27001 can become
  Verified with a `certificate` source.
- **Rocky Linux reading:** I read "on-premise servers" in the security post as Avicenna's own
  infrastructure. If you read it as customer installs, it is one more source for hosting_options and
  changes nothing else.
- **Vendor questions:** whether BAAs are signed; where UK/EEA data is stored and which AWS region is
  used; whether the participation-export use of `/api/v1/filter/export/` is supported for all
  licences; white-label and on-premise pricing.
- **Buzud CGM** and other new integrations (gap finding 8) are left for the profile's sensor-table
  pass.
