# mindLAMP (LAMP Platform)

## Quick Facts

| Field | Details |
|---|---|
| Organization | BIDMC Division of Digital Psychiatry (Beth Israel Deaconess Medical Center / Harvard Medical School), led by John Torous |
| Category | Open-source digital phenotyping and mobile-intervention platform, mental-health oriented |
| Current status | Active; LAMP-server, LAMP-dashboard, LAMP-core-ios and LAMP-core-android all pushed 2026-10-08 (GitHub API, checked 2026-10-10). The newest LAMP-server release is still 2023.7.27; the authentication rewrite merged on 2026-09-30 is unreleased (Verified 2026-10-11) [23]. The LAMP Consortium was retired in October 2025 and the Core interest form is the only intake route [27]. Two old repositories archived in 2020 (see below) |
| Platforms/devices | "mindLAMP 2" app on Google Play (`digital.lamp.mindlamp`, updated 2026-05-17, Android 8+, WearOS companion) and the App Store (developer John Torous, public build 2023.5.2 from 2023-05-26 plus an Apple-made watchOS 27 rebuild, iOS 14+, Apple Watch companion). Newer iOS builds (2025.4.2) go to testers through TestFlight only. Both apps work only with credentials from an enrolled study or clinic. A web version runs surveys and games but no passive sensing (Verified 2026-10-11) [11, 14, 16, 28] |
| Open source | Partly. Source is public, but LAMP-server, LAMP-core-android, LAMP-core-ios, LAMP-activities and LAMP-worker carry no licence file (all rights reserved by default). The docs privacy page says the platform has "no licensing restrictions for intellectual property", and an outside request for written terms (LAMP-platform issue 943, opened 2026-07-22) had no reply on 2026-10-11, so reuse rights for those components are Unclear. LAMP-dashboard is AGPL-3.0-only since 2026-08-05; LAMP-cortex, the SDKs and the gateway are BSD-3-Clause; LAMP-toolkit is MIT (Verified 2026-10-11) [9, 22, 24] |
| Hosting/deployment | Through the BIDMC **mindLAMP Core**, "the supported deployment pathway": self-hosted in the partner's own AWS account, a separate instance hosted and managed by BIDMC, or the shared BIDMC instance (lamp.digital). BIDMC hosting runs on AWS (ECS Fargate, DocumentDB); the region is not published. Self-hosting the unlicensed server outside that pathway rests on BIDMC's informal statement, not a licence grant (Verified 2026-10-11) [10, 17, 30] |
| Pricing model | No licence fee identified; source public with mixed licences. mindLAMP Core services and hosting are priced in a tailored proposal after a free consultation; no published figures (Verified 2026-10-11) [11] |
| Last verified | 2026-10-11 (vendor fact record) |

## Summary

- mindLAMP (Learn, Assess, Manage, Prevent), built on the "LAMP Platform," is an open-source digital phenotyping and mobile-intervention tool from Harvard-affiliated BIDMC's Division of Digital Psychiatry. It is explicitly positioned to support both **research and clinical use** of patient-generated health data, a dual orientation that distinguishes it from research-only platforms like Beiwe or RADAR-base. It combines active data collection (surveys, cognitive/behavioral tasks) with passive smartphone sensing, and is used by clinical research teams internationally (the search evidence names teams in Canada and Australia running adapted versions of the platform).

- **Status note, resolved in second pass (2026-08-24, Verified via direct GitHub fetch, resolves unresolved-question #87):** `LAMP-portal` and `LAMP-app` are not just labeled deprecated in their descriptions, **both were formally archived by their owner on Nov 17, 2020**, and GitHub reports each as "read-only." Direct inspection of the BIDMCDigitalPsychiatry organization's current (non-archived) repository listing shows the successor architecture clearly:

| Deprecated (archived 2020-11-17) | Current successor |
|---|---|
| `LAMP-portal` | `LAMP-dashboard` (the mindLAMP researcher/clinician web dashboard; TypeScript, actively updated as recently as Aug 21, 2026) |
| `LAMP-app` | `LAMP-core-android` (Kotlin) and `LAMP-core-ios` (Swift), described as "core scaffolding for digital phenotyping apps," rather than a single monolithic app repo |

- Other current, actively updated repositories confirmed in the same fetch: `LAMP-server` (backend, updated Aug 20, 2026), `LAMP-platform` (docs/issues), `LAMP-activities` (cognitive tests, updated Aug 19, 2026), `LAMP-app-gateway` (push/logging gateway), `LAMP-js` and `LAMP-py` (API clients, BSD-3-Clause licensed), `LAMP-cortex` (analytics, BSD-3-Clause) and `LAMP-toolkit` (MIT). LAMP-toolkit's repository describes itself as Cortex's second-generation successor, but the current docs, the Core page and the 2026 AWS blog all present Cortex as the analytics layer, and Cortex was pushed on 2026-05-18 (Verified 2026-10-11) [20]. The organization hosts 32 repositories total; only the 10 most-starred/most-relevant were enumerated directly. **A prospective adopter should build on `LAMP-dashboard`, `LAMP-server`, and `LAMP-core-android`/`LAMP-core-ios`, not `LAMP-portal` or `LAMP-app`.**

## Products / Platform Architecture

- **mindLAMP app** (iOS/Android), participant-facing app for surveys, cognitive/behavioral tasks, and passive sensing.
- **mindLAMP dashboard**, researcher/clinician-facing web portal for study configuration and data review.
- **LAMP-server**, backend server component (TypeScript). Commits are active (pushed 2026-10-08), but the newest release is 2023.7.27 [23].
- **LAMP-dashboard**, researcher/clinician web dashboard (TypeScript), successor to the archived `LAMP-portal`.
- **LAMP-core-android** / **LAMP-core-ios**, mobile app scaffolding (Kotlin/Swift), successors to the archived `LAMP-app`.
- **LAMP-activities**, cognitive-test library.
- **LAMP-app-gateway**, push notification/logging gateway server.
- **LAMP-js** / **LAMP-py**, official JavaScript and Python API clients (BSD-3-Clause).
- **LAMP-cortex**, the documented analytics library (Python, BSD-3-Clause, maintained) [20]. **LAMP-toolkit** (MIT) calls itself Cortex's second-generation successor in its repository description; the current docs present Cortex instead.
- **LAMP-worker** (no licence file) and **LAMP-raphe** (created 2026-09-29, no licence file, a phenotyping framework that can run Cortex as one feature engine; not otherwise checked) [20, 22].
- Legacy/archived: `LAMP-portal`, `LAMP-app`, both formally archived by the owner on 2020-11-17 (Verified, direct GitHub fetch, second pass). The docs label LAMP-app "DO NOT USE" [17].

## Sensors and Data Streams

- Every Module 2 profile uses the same table so platforms can be compared row by row. Rows are the passive streams named in `CLAUDE.md`. "Yes" and "No" are used only where a primary source says so; "Unclear" means nothing current was verified, and "No (OS)" means the operating system does not expose the stream to any third-party app. Confidence and sources are stated under the table. The convention is recorded in [`../../shared/profile-table-conventions.md`](../../shared/profile-table-conventions.md).

| Stream | Android | iOS | Raw or derived | Sampling configurable | Notes |
|---|---|---|---|---|---|
| GPS / location | Yes | Yes | Raw latitude and longitude, not hashed or anonymised. | Yes, through the API at the sensor-spec level (default 1 Hz, maximum 5 Hz); not in the dashboard. | OS throttling means background GPS often arrives at about 0.1 Hz or less [16, 20]. |
| Accelerometer | Yes | Yes | Raw | Yes, through the API (default and maximum 5 Hz). | Named among the nine device sensors [16]. |
| Gyroscope | Yes | Yes | Raw, inside `device_motion` | Unclear | The old `gyroscope` identifier was superseded by `device_motion`; old data stays in historical records [16]. |
| Magnetometer | Yes | Yes | Raw, inside `device_motion` | Unclear | The old `magnetometer` identifier was superseded by `device_motion` [16]. |
| Barometer | No | No | Not applicable | Not applicable | Not a mindLAMP stream. Not among the nine documented device sensors [16]. |
| Ambient light | No | No | Not applicable | Not applicable | Not a mindLAMP stream. Not among the nine documented device sensors [16]. |
| Proximity | No | No | Not applicable | Not applicable | Not a mindLAMP stream. Not among the nine documented device sensors [16]. |
| Device motion / activity recognition | Yes | Yes | Raw (`device_motion`); Event (`activity_recognition`, the OS classification). Steps is its own phone sensor. | Unclear | Sleep, heart rate and other health types come from HealthKit or Health Connect, not from this stream (see below) [16]. |
| Screen state | Yes | Yes | Event, as `device_state` | Unclear | `screen_state` was superseded by `device_state` [16]. |
| App usage | Unclear | Yes, iOS SensorKit only | Derived, app usage categories | Unclear | On iOS only on enrolled research devices in an Apple-approved SensorKit study [17, 20]. Android not documented. |
| Battery / charging | Unclear | Unclear | Unclear | Unclear | Not separately documented; may sit inside `device_state`, not checked. |
| Network / connectivity | Unclear | Unclear | Unclear | Unclear | Not separately documented. |
| Wi-Fi | Yes | Yes | Event, inside `nearby_device` | Unclear | `wifi` was superseded by `nearby_device` [16]. |
| Bluetooth | Yes | Yes | Event, inside `nearby_device` | Unclear | `bluetooth` was superseded by `nearby_device` [16]. |
| Calls (metadata) | Yes, call-state events only | Unclear | Event, as `telephony` | Unclear | The Android manifest requests READ_PHONE_STATE but not READ_CALL_LOG, so there is no call log [18]. iOS exposes no call log to third-party apps. |
| SMS (metadata) | No | Yes, iOS SensorKit only | Metadata (`text_number`, `text_degree` features) | Unclear | Text features depend on SensorKit `messages_usage` [16]. The Android app requests no SMS permission [18]. |
| Keyboard | No | No | Not applicable | Not applicable | Not a mindLAMP stream. Not among the documented sensors [16]. |
| Audio / microphone | No | No | Not applicable | Not applicable | Not a passive stream. Voice recordings are an active task (see Active Data Collection) [16]. |
| Notifications | No | No | Not applicable | Not applicable | Not a mindLAMP stream. Not among the documented sensors [16]. |
| Device information | Unclear | Unclear | Unclear | Unclear | The `analytics` sensor is documented but its fields were not checked. |

- **Health platform data.** Ten HealthKit or Health Connect types (sleep, heart rate, HRV, respiratory rate, blood pressure, blood glucose, oxygen saturation, body temperature, workouts, nutrition). mindLAMP "does not connect directly to wearable devices"; wearables are reached only through HealthKit or Health Connect [16].
- **SensorKit (iOS).** Adds app usage categories, text message metadata and location visit types on enrolled research devices [17].
- **Removed identifiers.** `distance`, `flights`, `weight` and `height` were removed [16].
- **Web version.** Collects no passive data [16].

**Verification.** Verified 2026-10-11 from the vendor fact record (`raw_streams`, `sampling_rates`, `deprecations`), which reads the docs' sensor reference pages and the Android manifest on master [16, 18]. The docs list nine device sensors for the mobile apps without a per-OS split, except for telephony and the SensorKit extras. "Yes" in both OS columns for the other listed sensors follows that list and was not checked device by device. Rows marked "No" rest on the docs' complete list of nine device sensors. The AWS blog (2026-09-29) says call and text logs sync from the phone, which overstates the Android permissions [30].

### Notes from earlier verification passes

- **Earlier table verification (superseded 2026-10-11).** Corroborated 2026-08-24 from docs.lamp.digital landing content, which names GPS, accelerometer, screen time, calls, heart rate, steps, sleep and gyroscope without a per-platform breakdown. That version marked steps, sleep and heart rate as coming from a paired wearable; the docs say wearables come only through HealthKit or Health Connect.
- **Second-pass update (2026-08-24, Corroborated, direct fetch of docs.lamp.digital's landing content):** the documentation names passive streams including **GPS, accelerometer, screen time, calls, heart rate, steps, sleep, and gyroscope**, stated to flow into "one consistent format, enabling comparison across projects." This upgrades the general claim from Unclear to Corroborated, but the fetch was of general marketing/landing content rather than a full sensor-by-sensor reference page (unlike the AWARE second-pass result), so **exact iOS-vs-Android parity for each stream remains not independently verified**, still an open question, and one that matters given the platform's clinical-use orientation where data completeness has direct care implications.

## Derived Metrics / Analytics

- **Cortex (Verified 2026-10-11)** [20]. The open-source Python package `lamp-cortex` (BSD-3-Clause, maintained) turns raw events into features.
  - Primary features include significant locations, trips and screen-on bouts.
  - Daily secondary features include home time, location entropy, trip distance, screen duration, step count, call counts, HealthKit sleep duration and data quality.
  - Text, unlock, app-time and visit features need iOS SensorKit, which "require[s] enrollment in an Apple-approved research study".
- Researchers run Cortex themselves against a LAMP server, or the Core runs default or custom analysis [20].
- Some Cortex features were replaced (for example `sms_number`) [20].
- Earlier passes called Cortex legacy, with LAMP-toolkit as its successor. The current docs present Cortex as the analytics layer; LAMP-toolkit's own repository calls it a successor (see Products).

## Active Data Collection

- Surveys, cognitive tests, and behavioral tasks are core to the platform's stated "Assess" and "Manage" functions (per the LAMP name itself: Learn, Assess, Manage, Prevent). This is a materially more clinically-oriented active-assessment design than Beiwe's simpler survey model, per the platform's own framing, though exact EMA scheduling sophistication was not independently benchmarked.
- Active data types are surveys, cognitive games and voice recordings [16].
- **Survey branching does not work at run time (Verified 2026-10-11).** Branching settings can be configured in the dashboard but are inert when participants take a survey, a known issue in dashboard release 2026.08.05.3 (2026-09-21) [19].

## Researcher and Study Management Features

- A dashboard/portal component exists for study and participant management, per the platform's own architecture description; specific features (multi-study support, role-based access, adherence monitoring) were not independently verified against current documentation this session.

## Data Access and Export

- **Export routes (Verified 2026-10-11)** [17, 21]:
  - REST API (`api.lamp.digital` on the hosted service; OpenAPI spec at docs.lamp.digital/api).
  - Python SDK (LAMP-py, "the primary and most actively maintained SDK"), JavaScript SDK, and R via reticulate.
  - JSONata queries run on the server, so data can be filtered without downloading raw files.
  - Cortex for features.
  - The dashboard Data Portal for ad-hoc queries and CSV export. The docs call it "an older feature that has not been actively updated".
  - Self-hosters also have direct database access.
- **History depth (Corroborated).** No look-back limit is documented. Queries take arbitrary from and to timestamps in Unix milliseconds. How long a hosted project's data is kept, and how far back HealthKit or Health Connect history is read at first sync, are not documented [21].
- **Rate limits.** No request-rate limit is published. The only documented limit is 1,000 entries per request for sensor-event queries, so long ranges are paged by time window [21]. Unreleased server code merged 2026-09-30 sets a cap of 1,000 requests per API key per rate-limit window (Reported, not in a release) [23].
- Scripts that sign in with a username and password will stop working when the authentication upgrade is released (see APIs, SDKs, and Extensibility) [23].
- Earlier note, kept for context. The platform's dual research/clinical orientation implies data governance considerations (e.g., a clinician using the same platform for patient care) that are distinct from a research-only tool, and this distinction should be confirmed with the maintaining team before use in any protocol involving clinical decision-making.

## APIs, SDKs, and Extensibility

- **Licences by component (Verified 2026-10-11)** [9, 22, 24]:
  - LAMP-dashboard is AGPL-3.0-only since a relicensing commit on 2026-08-05. Copies obtained earlier stay under BSD-3-Clause. Anyone running a modified dashboard over a network must offer its source.
  - LAMP-cortex, LAMP-py, LAMP-js, LAMP-swift, LAMP-kotlin, LAMP-app-gateway and LAMP-protocol are BSD-3-Clause.
  - LAMP-server, LAMP-core-ios, LAMP-core-android, LAMP-activities and LAMP-worker carry no licence file. The docs privacy page says the platform "does not have any licensing restrictions for intellectual property". An outside team asked which terms apply in LAMP-platform issue 943 (opened 2026-07-22); it had no reply on 2026-10-11. Status is Unclear, so ask the Core team for written terms before self-hosting or modifying these.
- **Developer access (Corroborated).** No registration-based developer program. The REST API, SDKs and server code are public, and anyone with credentials on a LAMP server can use the API [17, 21].
- **Authentication upgrade (Verified 2026-10-11)** [23]:
  - Phase 1 (the dashboard picks the server by button) went live 2026-07-29.
  - The next phase moves from Basic auth to server-side sessions, makes 2FA or OAuth mandatory for all staff users, and replaces username and password in LAMP-py with API keys. Pipelines that sign in with a password "will stop working after the release".
  - The server code was merged on 2026-09-30 (LAMP-server PR 284) but is not released. No release date has been announced; the blog's "later this summer" has passed.
  - Self-hosted servers are unaffected until upgraded, and the upgrade is offered through the Core.
- **Superseded sensor identifiers.** See Sensors and Data Streams. Old data stays in historical records [16].
- Earlier licence notes, kept for provenance. Source is public under the BIDMCDigitalPsychiatry GitHub organization, but **not uniformly open-source licensed (checked 2026-10-09, Verified via the GitHub API and each repository's root):** `LAMP-dashboard` was relicensed to **AGPL-3.0** (its LICENSE.md says earlier copies stay under BSD-3-Clause), and `LAMP-server`, `LAMP-core-android` and `LAMP-core-ios` carry **no licence file at all**, which by default reserves all rights. Forking and modifying the server or the apps therefore needs permission from BIDMC; a modified dashboard run as a service must publish its changes under AGPL. All four repositories were pushed on 2026-10-08. **Second-pass update (2026-08-24, Verified via direct fetch):** licence terms are **not uniform across the codebase**, `LAMP-js` and `LAMP-py` (the official API clients) are **BSD-3-Clause**, and `LAMP-toolkit` (the analytics successor to `LAMP-cortex`) is **MIT**. The licence covering the core `LAMP-server`/`LAMP-dashboard`/`LAMP-core-android`/`LAMP-core-ios` repositories specifically was not confirmed (GitHub's org-level repository list did not surface it in this pass), narrower open item than before, since the client-library and toolkit licences are now settled. An `/api` section is referenced in docs.lamp.digital's navigation, consistent with `LAMP-js`/`LAMP-py` wrapping a documented REST API, though the API reference content itself was not fetched this session.

## Deployment and Infrastructure

- **Resolved 2026-10-10 (Verified):** the BIDMC **mindLAMP Core** is "the supported deployment pathway for the mindLAMP platform" (digitalpsych.org/mindlamp-core). Process (docs.lamp.digital/get-started): interest form, a reply "within a few business days", a free consultation, then "a tailored proposal including scope, deployment option, and pricing", then configuration and staff training. Deployment models (research.bidmc.org/mindlamp/services): "Full mindLAMP stack in partner's own AWS account", a "Dedicated instance managed by BIDMC team", or "the main mindLAMP instance at lamp.digital". The Core "requires a business agreement (established after Phase 1)". Its five phases cover a free design consultation; protocol optimisation; privacy-aware configuration, including "standardized language and configuration patterns for IRB and security review", role-based access controls and audit logs; hosting, uptime monitoring and software updates; and study support including shared analytics pipelines such as Cortex. The digitalpsych page names clinical research studies, grant-funded projects, clinical care programs, international and multi-site deployments and first-time users as good fits, and claims 50+ active sites. Adoption figures vary by source: 65 sites, 42 projects and 17 countries in an AWS blog co-written by the BIDMC team (2026-09-29); 36 projects in 16 countries, 9 active, in the docs project gallery [12, 30]. Fees are not published. The Get Started FAQ answers render by JavaScript and were read from the page's source file on 2026-10-11. They say "Your institution owns its data" and that individuals can use mindLAMP only by enrolling in a project or clinic that runs it [11].
- **Audit logs (caveat, 2026-10-11).** The Core's audit-log claim is not borne out by the code record. Request-level audit logging is an open work item (LAMP-platform issue 910, open since 2025-06-09) and its pull request (LAMP-server PR 264) is unmerged. It may exist at the infrastructure level on BIDMC hosting, which only the Core team can confirm [26].
- Self-hostable server component (`LAMP-server`, Docker containers). Commits are active, but the newest release is 2023.7.27, and the public self-hosting guides are unpublished drafts in the LAMP-platform repository [23, 31]. Self-hosted teams stay on that release unless they upgrade through the Core. Because LAMP-server has no licence file, running or modifying it outside the Core pathway rests on BIDMC's informal "no licensing restrictions" statement, not a licence grant [24].
- **BIDMC hosting stack (Corroborated).** AWS ECS Fargate with Amazon DocumentDB as the primary data store; the AWS region is not published. Teams with data residency requirements are steered to self-hosting [17, 30]. No third-party managed hosting was found. **Second-pass update (2026-08-24, superseded 2026-10-10 by the Core finding above):** docs.lamp.digital's own content advertises "flexible hosting and complete data access" as a platform capability, which is suggestive of a managed-hosting option beyond pure self-hosting, but the fetched content did not state whether this is a service offered to outside research/clinical teams, under what terms, or at what cost, **the managed-hosting question is upgraded from Unclear to Reported, not fully resolved; still requires direct BIDMC contact.** The earlier "clinical research teams in Canada and Australia" framing remains Reported only, not independently traced to a specific citation this session. Infrastructure requirements for self-hosting were not independently benchmarked.

## Participant Experience

- The mindLAMP 2 app is free in both stores and usable only with project credentials. People outside a partner study or clinic "will not be able to access the app" (Google Play listing) [14].
- iOS 14+ and Android 8+, with Apple Watch and WearOS companion apps [11, 14].
- The public iOS build is from 2023; newer builds reach only TestFlight testers [28].

### Background keepalive (added 2026-10-09)

- No server-triggered keepalive like Beiwe's was found. `LAMP-app-gateway` sends Apple and Firebase push notifications, email and SMS, but its documented role is logging and notifications. A code search of the BIDMCDigitalPsychiatry organization for "heartbeat" returned nothing.
- The Android client runs a foreground service with low-priority notification channels. Community onboarding advice is to set location to "Always Allow", avoid low power mode and keep the phone charged, which puts the burden on participant behaviour.
- Status: **Corroborated** absence, from code and forum material, 2026-10-09. The official docs site did not answer the question. Sources 7 and 8.

## Privacy, Security, and Compliance

- **HIPAA (Corroborated, self-claim, 2026-10-11)** [24]. The docs privacy page (docs.lamp.digital/privacy) says LAMP offers safeguards "in line with the HIPAA Security Privacy Rule". It lists access control, audit logs, integrity controls and encrypted transmission, with AES-256 at rest under a per-site key and TLS 1.3 in transit. Get Started says the platform "supports HIPAA-compliant workflows" [11]. This is a self-description, not a certification.
- **Penetration test.** Echelon Risk + Cyber tested the mobile and web apps in July 2025, in a BIDMC test environment [24].
- **Audit logging is not confirmed in code.** Request-level audit logging is an open work item (LAMP-platform issue 910, open since 2025-06-09; LAMP-server PR 264 unmerged), and the released server (2023.7.27) shows no request-level audit log. It may exist at the infrastructure level on BIDMC hosting; ask the Core team [26].
- **GDPR (Corroborated, self-claim).** The architecture docs say AES-256 and TLS 1.3 allow storage and transmission "in a HIPAA, COPPA, and GDPR-compliant manner" [29]. No GDPR-specific policy (lawful basis, controller and processor roles, transfers, EU representative) is published.
- **Not public (2026-10-11).** BAA for Core-hosted projects, DPA, SOC 2 and ISO 27001. The only BAA mention is in the unpublished draft deployment docs, telling self-hosters to sign one with their own cloud provider [24, 31]. Core projects run under a business agreement whose terms are not public.
- **FDA.** No 510(k), PMA or registration found in openFDA (2026-10-11). The docs make no FDA claim, and the privacy page says LAMP is not an electronic health record system [24, 32].
- **Data residency (Corroborated).** BIDMC-hosted instances run on AWS; the region or country is not published. Teams with residency requirements are steered to self-hosting [17, 30].
- **Deletion and retention (conflict, Unclear, 2026-10-11)** [14, 24, 25]:
  - The live privacy page promises a 90-day soft-deletion period (restorable on request), then permanent deletion. Participants can delete their account in the app. Aggregated usage statistics "may be kept for an indefinite amount of time".
  - The Google Play data-safety label says "Data can't be deleted".
  - The maintainers' own rewrite (LAMP-platform PR 939, open and unmerged since 2026-03-16) fixes "inaccurate data deletion claims". It says deleted data stays in the database until a site administrator removes it by hand, and that event data (survey responses, sensor readings) cannot be deleted through the API.
  - A consent form should not rely on the 90-day wording. No retention period after a hosted project ends is published. Self-hosters control their own data.
- **AI training not addressed (2026-10-11).** Nothing in the privacy page or Core pages covers AI or model training. The privacy page says research data is shared only in aggregate and never used for marketing or commercial purposes. The AWS blog says the division is building AI navigator agents on mindLAMP [24, 30].
- **Earlier check, 2026-10-10.** The Division of Digital Psychiatry privacy page (digitalpsych.org/privacy.html) makes no HIPAA, SOC 2 or GDPR claim and links only to BIDMC's general privacy policy. That finding still holds for that page; the claims above sit on docs.lamp.digital instead. The mindLAMP Core page describes role-based access controls, audit logs for data access and changes, and IRB and security-review language as part of its configuration service. These are service descriptions, not certifications.
- Given the platform's explicit clinical-use positioning (not just research), HIPAA and comparable clinical-data-handling documentation would be a first-order question for any team considering clinical deployment, and CLAUDE.md's instruction not to infer compliance from institutional affiliation (Harvard/BIDMC) applies here as directly as anywhere in this module.

## Pricing

- No licence fee for the code, API or SDKs. Cost is either self-hosting infrastructure and staff time, or a BIDMC mindLAMP Core proposal covering services and hosting. Core pricing depends on participants, sites, duration and custom development; figures are not public, and the first consultation is free (Verified 2026-10-11) [11, 24].
- No academic rate, minimum commitment, user cap or academic versus commercial difference is published (2026-10-11). Participant count is an input to Core pricing [10, 11, 12].
- **Self-hosted AWS estimates (Reported).** Unpublished draft deployment docs estimate monthly AWS cost at about $35 for a small clinic (~15 participants, active data only), about $100 for a small study (~50 participants, active and passive) and about $1,500 for a large study (200+ participants, active, passive and ML). These are infrastructure estimates paid by the institution, not a BIDMC fee [31].
- The Core offers letters of support for grants, and custom development is available under a Core agreement [11].

## Research Evidence and Validation

- mindLAMP has a substantial published research record centered on mental-health digital phenotyping, including the platform-description paper "Enabling Research and Clinical Use of Patient-Generated Health Data (the mindLAMP Platform): Digital Phenotyping Study" (Vaidyam, Halamka, Torous; *JMIR mHealth and uHealth*, Jan 2022) and subsequent studies on digital-phenotyping correlations in larger mental-health samples, EMA validation in schizophrenia populations, and COVID-related neuropsychiatric sequelae research in college students. This is a strong, mental-health-domain-specific published record, though this session did not attempt an exhaustive publication count.

## Strengths

- Explicit dual research/clinical orientation, distinguishing it from research-only competitors, potentially valuable for teams bridging digital phenotyping research into actual care pathways.
- Strong, mental-health-specific published research record from an established academic digital-psychiatry group.
- Public source code permitting inspection and institutional self-hosting. The server and apps carry no licence file, so reuse rights rest on BIDMC's informal statement until written terms exist (the dashboard is AGPL-3.0).
- A supported hosted route, the BIDMC mindLAMP Core, with a shared or dedicated BIDMC-hosted instance for teams without infrastructure capacity (priced by proposal).
- Combines active clinical assessment tools (cognitive/behavioral tasks) more deeply than some passive-sensing-first competitors.

## Limitations

- ~~Some component repositories are explicitly marked deprecated... this session could not fully map which components are current successors~~ **Resolved 2026-08-24**, `LAMP-portal` and `LAMP-app` are formally archived (2020-11-17); successors are `LAMP-dashboard` and `LAMP-core-android`/`LAMP-core-ios` respectively (Verified, direct GitHub fetch).
- The core server and apps carry no licence (dashboard AGPL-3.0), so the platform is source-available rather than open source end to end. The vendor's "no licensing restrictions" statement conflicts with that, and issue 943 is unanswered (Verified 2026-10-11).
- The newest server release dates from 2023-07-27. The authentication upgrade is merged but unreleased, and will break password-based scripts and require staff 2FA or OAuth when it ships [23].
- Published deletion terms conflict with the Play label and with the maintainers' own unmerged correction [25].
- Survey branching is configurable but inert at run time [19].
- No call log or SMS data on Android; text features need iOS SensorKit in an Apple-approved study [16, 18].
- Per-sensor iOS and Android parity is not documented beyond telephony and SensorKit. HIPAA and GDPR statements are self-claims, and the audit-log claim is unconfirmed in code [24, 26].
- The clinical-use positioning raises data-governance questions (patient-care data vs. research data) that a purely research-oriented platform doesn't have to answer, and this session did not establish how mindLAMP handles that distinction.

## Best-Fit Use Cases

- Mental-health-focused digital phenotyping research, especially where active cognitive/behavioral assessment matters alongside passive sensing.
- Teams wanting to bridge research findings into a clinical-facing tool built on the same underlying platform.

## Poor-Fit Use Cases

- Teams needing airtight, independently-verified compliance documentation without further due diligence, this session could not establish that documentation.
- Studies where component-level maintenance status is safety-critical and cannot tolerate the ambiguity flagged above around deprecated repositories.

## Open Questions

- *(Directed to: BIDMC Division of Digital Psychiatry / John Torous lab, via https://github.com/BIDMCDigitalPsychiatry or https://www.digitalpsych.org)*

- ~~Which specific mindLAMP repositories are current/production, and which are the successors to the repositories explicitly marked deprecated (`LAMP-portal`, `LAMP-app`)?~~ **Resolved 2026-08-24**, see the repository table above (Verified, direct GitHub fetch).
- ~~What open-source licence governs the core `LAMP-server`/`LAMP-dashboard`/`LAMP-core-android`/`LAMP-core-ios` repositories?~~ **Answered 2026-10-09:** dashboard AGPL-3.0; server and both apps unlicensed (LAMP-activities and LAMP-worker too). New question: does BIDMC grant outside teams written permission to self-host and modify the unlicensed components? Asked publicly in LAMP-platform issue 943, unanswered on 2026-10-11.
- What is the exact per-stream iOS-vs-Android sensor parity? Partly answered 2026-10-11. The docs list nine device sensors and ten health types; Android has call-state events only, and text features are iOS SensorKit only. Other sensors are not split by OS.
- What HIPAA/GDPR/compliance documentation exists, particularly for the clinical-use pathway as distinct from pure research use? Partly answered 2026-10-11. docs.lamp.digital makes HIPAA and GDPR self-claims and reports a July 2025 pen test; no BAA, DPA, SOC 2 or ISO 27001 is published.
- Which deletion behaviour applies on BIDMC servers, the published 90-day soft delete or the manual administrator removal described in PR 939? What happens to a hosted project's data after it ends?
- Does BIDMC hosting log requests at the infrastructure level, given that request-level audit logging in the server is an open work item (issue 910)?
- When will the authentication upgrade be released, and does BIDMC sign a BAA for Core-hosted projects?
- ~~Is "flexible hosting" a managed service for outside teams?~~ Resolved 2026-10-10: yes, via the mindLAMP Core (separate or shared BIDMC instance). Still open: fee schedule and academic vs industry rates. Eligibility answered 2026-10-11 (research groups and clinical programs; individuals only through an enrolled project). The FAQ says the institution owns its data, but the business agreement's terms are not public.
- ~~Why does the public App Store build (v2023.5.2, 2023-05-26) lag the actively pushed LAMP-core-ios repository? Is a newer iOS build distributed another way?~~ **Answered 2026-10-11:** newer builds (2025.4.2) go to testers through TestFlight only, during dev testing of the authentication upgrade (LAMP-platform issue 944) [28]. Why the store build has not been updated is not stated.

## Vendor Fact Record

<!-- facts:begin -->
*Generated from the fact record by `tools/facts/generate.py`. Edit the record, not this block.*

**Research access**

| Fact | Value |
|---|---|
| Formal research or academic program (name, what it offers) | mindLAMP Core (also called Core Services), run by the BIDMC Division of Digital Psychiatry: the supported deployment pathway for mindLAMP. It covers study design consultation, protocol optimisation, privacy-aware configuration, hosting (shared or dedicated BIDMC instance, or support for self-hosting), onboarding and training, data monitoring, Cortex analytics support, troubleshooting and optional custom development. It is a paid service under a business agreement, not a free access program; the team offers letters of support for grants. The code itself is public, and self-hosting outside the Core needs no program (but see licence). [V, 2026-10-11] |
| Who can join the research program | Research groups and clinical programs; the Core page names clinical research studies, grant-funded projects, clinical care programs, international and multi-site deployments, and first-time users. Individuals cannot start a project; they use mindLAMP only by enrolling in a project or clinic that runs it (or a limited Self Help mode), and the store listings say people outside a partner study or clinic cannot access the app. No sector or country restriction is published. [V, 2026-10-11] |
| How to apply, and any approval or review step | The Core interest form (a Notion form linked from docs.lamp.digital/get-started) is the only route in. A Core team member reviews it within a few business days and books a free consultation call; BIDMC then issues a tailored proposal with scope, deployment option and pricing. A business agreement is required after that first phase, before configuration, onboarding and staff training. [V, 2026-10-11] |
| Whether the program is active, paused, renamed or closed | Active as of 2026-10-11. The Core takes new projects through the interest form, the docs site carries a running updates blog (posts to July 2026), and the server, dashboard and both app repositories were pushed on 2026-10-08. The LAMP Consortium pages were removed from the docs (LAMP-platform PR 930, merged October 2025) and the community forum was archived; mindlamp.discourse.group no longer resolves (NXDOMAIN, 2026-10-11). The Core interest form is the only intake route. [V, 2026-10-11] |
| Whether the general developer or API program is open to new applicants | No registration-based developer program. The REST API (OpenAPI spec), SDKs and server code are public on GitHub (BIDMCDigitalPsychiatry); anyone with credentials on a LAMP server can use the API (api.lamp.digital for the BIDMC-hosted server). Access to the hosted service follows from a Core agreement and the credentials issued for a project. [C, 2026-10-11] |
| Participant or user limits before approval or by tier | Not public [2026-10-11] |
| How academic access differs from commercial or consumer access | Not public [2026-10-11] |

**Pricing**

| Fact | Value |
|---|---|
| Device or hardware list price | n/a |
| Consumer subscription or membership price | n/a |
| Research or academic pricing or discount | Not public [2026-10-11] |
| Fees for API, SDK, platform or data access | No fee for the code, API or SDKs. Using the BIDMC Core (hosting, configuration, support, custom development) is priced per project by quote, depending on participants, sites, duration and custom development; the first consultation is free. [V, 2026-10-11] |
| Minimum order, term or commitment | Not public [2026-10-11] |
| Whether pricing requires contacting sales | Yes for Core-hosted or Core-supported projects, including hosting; pricing comes in a tailored proposal after the interest form and a free consultation. Self-hosting the public code involves no quote. [V, 2026-10-11] |
| Price of managed hosting | **BIDMC Core hosting (shared or dedicated instance):** Not public [2026-10-11]<br>**Self-hosted on AWS (infrastructure estimate from unpublished draft docs):** Estimated monthly AWS cost borne by the self-hosting institution: about $35 for a small clinic (~15 participants, active data only), about $100 for a small study (~50 participants, active and passive), about $1,500 for a large study (200+ participants, active, passive and ML). Not a BIDMC fee. [R, 2026-10-11] |

**Data access and terms**

| Fact | Value |
|---|---|
| Raw signals available to researchers, and by which route | Raw, timestamped sensor events from 9 phone sensors (GPS as raw unhashed coordinates, accelerometer, device motion, device state, steps, nearby devices, telephony, analytics, activity recognition) and 10 HealthKit or Health Connect types (sleep, heart rate, HRV, respiratory rate, blood pressure, blood glucose, oxygen saturation, body temperature, workouts, nutrition); wearables are reached only through HealthKit or Health Connect. Apple SensorKit adds app usage, text message metadata and visit types on enrolled iOS research devices. Text-message features come only from iOS SensorKit; the Android app requests no call-log or SMS permission. Active data: surveys, cognitive games, voice recordings. The web version collects no passive data. Retrieved by REST API, SDKs, Cortex or the dashboard Data Portal. [V, 2026-10-11] |
| Derived or processed metrics available to researchers | Cortex, the open-source Python package (lamp-cortex, BSD-3-Clause, still maintained), turns raw events into primary features (significant locations, trips, screen-on bouts) and daily secondary features (home time, location entropy, trip distance, screen duration, step count, call counts, HealthKit sleep duration, data quality and more). Text, unlock, app-time and visit features need iOS SensorKit, which requires an Apple-approved research study. Researchers run Cortex themselves against a LAMP server, or the Core runs default or custom analysis. [V, 2026-10-11] |
| Documented sampling rates or temporal resolution | Accelerometer default 5 Hz (maximum 5 Hz); GPS default 1 Hz (maximum 5 Hz), but OS throttling means background GPS often arrives at roughly 0.1 Hz or less. Rates are set at the sensor-spec level through the API; the dashboard Sensors tab only turns sensors on or off. Other sensors are event-driven or interval-reported. [V, 2026-10-11] |
| How far back data can be retrieved | No look-back limit is documented. Queries take arbitrary from/to timestamps (Unix milliseconds) and return up to 1,000 events per request by default, so long ranges are paged by time window. How long a hosted project's data is kept, and how far back HealthKit or Health Connect history is read at first sync, are not documented. [C, 2026-10-11] |
| Export, API, SDK or file routes | REST API (api.lamp.digital on the hosted service; OpenAPI spec at docs.lamp.digital/api); Python SDK (LAMP-py, the primary and most maintained), JavaScript SDK, R via reticulate; JSONata queries run on the server; Cortex for features; and the dashboard Data Portal (ad-hoc queries and CSV export; older and not actively updated). Self-hosters also have direct database access. [V, 2026-10-11] |
| API rate limits | No request-rate limit is published. The only documented limit is 1,000 entries per request for sensor-event queries; larger pulls use from/to time ranges. [V, 2026-10-11] |
| Terms on retaining, storing or deleting data | Three sources disagree. (1) The live privacy page: deleted content has a 90-day soft-deletion period (restorable on request) and is then deleted permanently; participants can delete their account in the app; aggregated usage statistics may be kept indefinitely. (2) The Google Play data-safety label: "Data can't be deleted". (3) The maintainers' own correction, open as LAMP-platform PR 939 since 2026-03-16 (lead engineer, not merged): it rewrites the page to fix "inaccurate data deletion claims", saying deleted data stays in the database until a site administrator removes it by hand, and event data (survey responses, sensor readings) cannot be deleted through the API. Self-hosters control their own data. (conflict) [U, 2026-10-11] |
| Terms on using data to train AI or ML models | Not public [2026-10-11] |
| Announced shutdowns, deprecations or migrations, with dates | **Authentication upgrade:** Phase 1 (dashboard picks the server by button) went live 2026-07-29. The next phase moves from Basic auth to server-side sessions, makes 2FA or OAuth mandatory for all staff, and replaces username and password in LAMP-py with API keys; scripts that sign in with a password will stop working after the release. The server code was merged on 2026-09-30 (LAMP-server PR 284) but is not released: the newest LAMP-server release is 2023.7.27. No release date has been announced. Self-hosted servers are unaffected until upgraded, and the upgrade is offered through the Core services process. [V, 2026-10-11]<br>**Sensor identifiers and legacy components:** Sensor identifiers superseded (old data stays in historical records): gyroscope and magnetometer into device_motion, screen_state into device_state, calls and sms into telephony, bluetooth and wifi into nearby_device; distance, flights, weight and height removed. Some Cortex features replaced (for example sms_number). The v1 app (LAMP-app) and v1 backend (LAMP-portal) are deprecated and archived. The Data Portal UI is no longer actively updated. No dates are given. [V, 2026-10-11] |
| Software licence of the platform's components | **LAMP-dashboard:** AGPL-3.0-only since a relicensing commit on 2026-08-05 (previously BSD 3-Clause; copies obtained earlier stay under BSD 3-Clause). Anyone running a modified dashboard over a network must offer its source. [V, 2026-10-11]<br>**LAMP-cortex, LAMP-py, LAMP-js, LAMP-swift, LAMP-kotlin, LAMP-app-gateway, LAMP-protocol:** BSD 3-Clause (each repository's licence file and GitHub's licence detection, 2026-10-11). [V, 2026-10-11]<br>**LAMP-server, LAMP-core-ios, LAMP-core-android, LAMP-activities, LAMP-worker:** These public repositories carry no licence file (the GitHub API reports none, 2026-10-11), so by default no reuse rights are granted. The docs privacy page says the platform has no licensing restrictions for intellectual property. An outside team asked which terms apply in LAMP-platform issue 943 (opened 2026-07-22); it had no reply on 2026-10-11. (conflict) [U, 2026-10-11] |
| Self-hosting and managed-hosting options | Three models, arranged through a Core agreement: (1) the shared BIDMC-hosted instance; (2) a dedicated, isolated instance hosted and maintained by BIDMC; (3) self-hosting on the institution's own infrastructure (its own AWS account or elsewhere) using Docker containers, with Core documentation and support. BIDMC hosting runs on AWS (ECS Fargate, DocumentDB); the region is not stated. The newest released server is 2023.7.27, and the public self-hosting guides are unpublished drafts. [V, 2026-10-11] |
| App store availability on iOS and Android | **iOS (App Store):** "mindLAMP 2", free, iPhone, iPad and Apple Watch, developer listed as John Torous. The public build is 2023.5.2 (26 May 2023) plus an Apple-made watchOS 27 compatibility rebuild; newer iOS builds (2025.4.2) go to testers through TestFlight only. Usable only with credentials from an enrolled study or clinic. [V, 2026-10-11]<br>**Android (Google Play):** "mindLAMP 2" (digital.lamp.mindlamp), free, developer listed as John Torous, 1K+ downloads, updated 17 May 2026, with a WearOS companion app. Android 8+ per the docs FAQ. The listing says only people in a partner study or clinic can access it. A web version runs without passive sensing. [V, 2026-10-11] |

**Compliance and regulatory**

| Fact | Value |
|---|---|
| Whether a HIPAA Business Associate Agreement is offered | Not public [2026-10-11] |
| Whether a data processing agreement is offered | Not public [2026-10-11] |
| Published HIPAA statement | BIDMC states that LAMP offers safeguards in line with the HIPAA Security Rule (access control, audit logs, integrity controls, encrypted transmission; AES-256 at rest with a per-site key, TLS 1.3 in transit) and supports HIPAA-compliant workflows. It is a self-description, not a certification. A penetration test by Echelon Risk + Cyber was run in July 2025 on a BIDMC test environment. The audit-logging claim is not borne out by the code record: request-level audit logging is an open work item (LAMP-platform issue 910, open since 2025-06-09) and its pull request (LAMP-server PR 264) is unmerged. [C, 2026-10-11] |
| Published GDPR statement | The architecture docs say AES-256 and TLS 1.3 enable storage and transmission in a HIPAA, COPPA and GDPR-compliant manner. No GDPR-specific policy (lawful basis, controller and processor roles, transfers, EU representative) is published; the privacy page is US-oriented. [C, 2026-10-11] |
| ISO/IEC 27001 status and evidence | Not public [2026-10-11] |
| SOC 2 status and evidence | Not public [2026-10-11] |
| FDA clearances, from the FDA database | Not public [2026-10-11] |
| Where data is stored, and residency options | BIDMC-hosted shared and dedicated instances run on AWS (ECS Fargate, DocumentDB); the AWS region or country is not published. Teams with residency requirements are steered to self-hosting, and the AWS blog says each site runs its own instance and keeps its own data. The docs say the institution owns its data. [C, 2026-10-11] |

<!-- facts:end -->

## Key Links

- Digital Psych (lab site): https://www.digitalpsych.org/mindlamp1.html
- Documentation: https://docs.lamp.digital/
- GitHub organization: https://github.com/BIDMCDigitalPsychiatry
- LAMP-server repository: https://github.com/BIDMCDigitalPsychiatry/LAMP-server
- LAMP-dashboard repository: https://github.com/BIDMCDigitalPsychiatry/LAMP-dashboard
- Publications: https://docs.lamp.digital/about/publications/ (dead link, HTTP 404, checked 2026-10-10). The consortium and publications/users pages were removed in LAMP-platform PR 930 (October 2025) [27]; use https://docs.lamp.digital/ and its project gallery at https://docs.lamp.digital/projects
- Updates blog: https://docs.lamp.digital/blog ; authentication upgrade: https://docs.lamp.digital/blog/authentication-upgrade
- Privacy and security: https://docs.lamp.digital/privacy
- API reference: https://docs.lamp.digital/api ; sensor reference: https://docs.lamp.digital/sensors-data/
- mindLAMP Core: https://www.digitalpsych.org/mindlamp-core ; https://research.bidmc.org/mindlamp/services ; https://docs.lamp.digital/get-started
- Google Play: https://play.google.com/store/apps/details?id=digital.lamp.mindlamp ; App Store: https://apps.apple.com/us/app/mindlamp-2/id1495947054

## Sources

1. BIDMCDigitalPsychiatry GitHub organization. https://github.com/BIDMCDigitalPsychiatry (accessed 2026-08-24, direct fetch, first and second pass). **Primary/Verified.** Repository inventory; second pass directly confirmed `LAMP-portal` and `LAMP-app` were archived by the owner on 2020-11-17 (read-only), identified current successor repositories (`LAMP-dashboard`, `LAMP-core-android`, `LAMP-core-ios`, `LAMP-server`, `LAMP-activities`, `LAMP-app-gateway`, `LAMP-js`, `LAMP-py`, `LAMP-toolkit`), and confirmed BSD-3-Clause (`LAMP-js`, `LAMP-py`) and MIT (`LAMP-toolkit`) licences.
2. Digital Psych, mindLAMP lab page. https://www.digitalpsych.org/mindlamp1.html (accessed 2026-08-24, search summary). Platform framing (Learn, Assess, Manage, Prevent), research/clinical dual orientation.
3. docs.lamp.digital, documentation landing page (**direct fetch, second pass**). https://docs.lamp.digital/ (accessed 2026-08-24). **Corroborated** (landing/marketing content, not a full reference page). Passive-sensor list (GPS, accelerometer, screen time, calls, heart rate, steps, sleep, gyroscope), "flexible hosting and complete data access" framing, `/api` navigation reference.
4. Vaidyam A, Halamka J, Torous J. "Enabling Research and Clinical Use of Patient-Generated Health Data (the mindLAMP Platform): Digital Phenotyping Study." *JMIR mHealth and uHealth* 2022;10(1). https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8783287/ (accessed 2026-08-24, search summary). Platform-description peer-reviewed paper.
5. mindLAMP publications listing. https://docs.lamp.digital/about/publications/, **fetch attempted, returned HTTP 404 both sessions**; existence and framing corroborated via search summary only. Still flagged as a documentation-access gap.
6. International/adapted-deployment claim (Canada, Australia), search-summary corroboration only, not independently traced to a specific named study or primary source in either session. **Reported**, not Verified.
7. `BIDMCDigitalPsychiatry/LAMP-app-gateway` README and `LAMP-kotlin` source via the GitHub API, plus an organization code search for "heartbeat" (accessed 2026-10-09). **Primary/Direct.**
8. mindLAMP community forum (mindlamp.discourse.group) threads on notifications, battery and onboarding (accessed 2026-10-09, search summary). **Reported.** The host no longer resolves (NXDOMAIN, checked 2026-10-11), so these threads cannot be re-read. LAMP-platform PR 891 (March 2025) says the forum was archived for lack of use [27].
9. BIDMCDigitalPsychiatry repository licences, checked 2026-10-09 via https://api.github.com/repos/BIDMCDigitalPsychiatry/<repo> and https://github.com/BIDMCDigitalPsychiatry/LAMP-dashboard/blob/master/LICENSE.md. **Primary/Verified.** LAMP-dashboard AGPL-3.0 (previously BSD-3-Clause); LAMP-server, LAMP-core-android, LAMP-core-ios no licence file.
10. BIDMC, "mindLAMP Core services." https://research.bidmc.org/mindlamp/services (accessed 2026-10-10, direct fetch). **Primary/Verified.** Three deployment models, five phases, business agreement after Phase 1; no prices.
11. mindLAMP documentation, "Get started." https://docs.lamp.digital/get-started (accessed 2026-10-10, direct fetch). **Primary/Verified.** Interest form, free consultation, tailored proposal with scope, deployment option and pricing.
12. Division of Digital Psychiatry, "mindLAMP Core." https://www.digitalpsych.org/mindlamp-core (accessed 2026-10-10, direct fetch). **Primary/Verified.** "supported deployment pathway"; good-fit users; 50+ active sites (vendor claim).
13. GitHub API repository metadata for LAMP-server, LAMP-dashboard, LAMP-core-ios, LAMP-core-android (accessed 2026-10-10). **Primary/Verified.** All pushed 2026-10-08; licence None for server and apps, AGPL-3.0 text in LAMP-dashboard/LICENSE.md.
14. App Store (iTunes lookup id 1495947054) and Google Play (`digital.lamp.mindlamp`) listings, direct fetch 2026-10-10. **Primary/Verified.**
15. Division of Digital Psychiatry privacy page. https://www.digitalpsych.org/privacy.html (accessed 2026-10-10, direct fetch). **Primary.** No compliance claims.
16. mindLAMP docs, sensors and data. https://docs.lamp.digital/sensors-data/ ; https://docs.lamp.digital/sensors-data/configuration ; https://docs.lamp.digital/sensors-data/reference/gps ; https://docs.lamp.digital/sensors-data/reference/telephony ; https://docs.lamp.digital/sensors-data/data (accessed 2026-10-11, vendor fact record). **Primary/Verified.** Nine device sensors and ten health types, raw unhashed GPS, sampling defaults and API configuration, no direct wearable connection, SensorKit-only text features, superseded identifiers, no passive data on the web version.
17. mindLAMP docs, capabilities and architecture. https://docs.lamp.digital/capabilities/collect ; https://docs.lamp.digital/capabilities/configure ; https://docs.lamp.digital/developer/architecture/components (accessed 2026-10-11). **Primary/Verified.** SensorKit extras, hosting models, API and SDK access, LAMP-app "DO NOT USE".
18. LAMP-core-android AndroidManifest.xml on master. https://github.com/BIDMCDigitalPsychiatry/LAMP-core-android/blob/master/app/src/main/AndroidManifest.xml (accessed 2026-10-11). **Primary/Verified.** READ_PHONE_STATE requested; READ_CALL_LOG and READ_SMS absent.
19. LAMP-dashboard release 2026.08.05.3. https://github.com/BIDMCDigitalPsychiatry/LAMP-dashboard/releases/tag/2026.08.05.3 (accessed 2026-10-11). **Primary/Verified.** Survey branching configurable but inert at run time.
20. Cortex. https://docs.lamp.digital/capabilities/analyze ; https://docs.lamp.digital/developer/cortex/features/secondary-features/ ; https://research.bidmc.org/mindlamp/about ; GitHub API metadata for LAMP-cortex and LAMP-toolkit (accessed 2026-10-11). **Primary/Verified.** Feature catalogue, SensorKit requirement, Core analysis, background GPS rate; LAMP-toolkit's description as Cortex's successor.
21. mindLAMP docs, data access. https://docs.lamp.digital/developer/api-sdks/python-sdk ; https://docs.lamp.digital/api/query-sensor-events-for-a-participant ; https://docs.lamp.digital/dashboard/data-portal (accessed 2026-10-11). **Primary/Verified.** SDKs, 1,000 entries per request, from and to timestamps, Data Portal status.
22. Component licences. https://github.com/BIDMCDigitalPsychiatry/LAMP-dashboard/blob/master/LICENSE.md ; https://github.com/BIDMCDigitalPsychiatry/LAMP-cortex/blob/master/LICENSE.md ; https://github.com/BIDMCDigitalPsychiatry/LAMP-py/blob/master/LICENSE ; https://github.com/BIDMCDigitalPsychiatry/LAMP-js/blob/master/LICENSE.md ; GitHub API licence fields (accessed 2026-10-11). **Primary/Verified.** Dashboard AGPL-3.0-only from 2026-08-05 (commit 8e6ad0f0); SDKs, Cortex, gateway and protocol BSD-3-Clause; server, apps, activities and worker unlicensed.
23. Authentication upgrade and server releases. https://docs.lamp.digital/blog/authentication-upgrade ; https://github.com/BIDMCDigitalPsychiatry/LAMP-server/pull/284 ; https://github.com/BIDMCDigitalPsychiatry/LAMP-server/releases ; https://github.com/BIDMCDigitalPsychiatry/LAMP-server/blob/master/src/service/ApiKeyService.ts (accessed 2026-10-11). **Primary/Verified.** Staff 2FA or OAuth, API keys for LAMP-py, PR 284 merged 2026-09-30, newest release 2023.7.27, unreleased API-key rate cap.
24. mindLAMP docs, privacy and security. https://docs.lamp.digital/privacy (accessed 2026-10-11); LAMP-platform issue 943, https://github.com/BIDMCDigitalPsychiatry/LAMP-platform/issues/943. **Primary.** HIPAA safeguards self-claim, encryption, pen test, 90-day soft delete, "no licensing restrictions", no commercial use; open licence question.
25. LAMP-platform PR 939 and its draft privacy page. https://github.com/BIDMCDigitalPsychiatry/LAMP-platform/pull/939 ; https://github.com/BIDMCDigitalPsychiatry/LAMP-platform/blob/docs/update-security-privacy-policy/docs/07-privacy.mdx (accessed 2026-10-11). **Primary, unmerged.** Corrects the deletion claims. The draft branch may disappear when the PR merges.
26. Audit logging work item. https://github.com/BIDMCDigitalPsychiatry/LAMP-platform/issues/910 ; https://github.com/BIDMCDigitalPsychiatry/LAMP-server/pull/264 (accessed 2026-10-11). **Primary/Verified.** Both open.
27. Consortium retirement and forum. https://github.com/BIDMCDigitalPsychiatry/LAMP-platform/pull/930 (merged October 2025); LAMP-platform PR 891 (accessed 2026-10-11). **Primary/Verified.**
28. LAMP-platform issue 944. https://github.com/BIDMCDigitalPsychiatry/LAMP-platform/issues/944 (accessed 2026-10-11). **Primary/Verified.** iOS 2025.4.2 builds distributed through TestFlight for dev testing.
29. mindLAMP docs, data flow. https://docs.lamp.digital/developer/architecture/data-flow (accessed 2026-10-11). **Primary.** HIPAA, COPPA and GDPR encryption self-claim.
30. AWS for Industries blog, "From cloud to clinic: how AWS powers digital psychiatry at scale" (2026-09-29, co-written by the BIDMC team). https://aws.amazon.com/blogs/industries/from-cloud-to-clinic-how-aws-powers-digital-psychiatry-at-scale/ (accessed 2026-10-11). **Secondary.** ECS Fargate and DocumentDB stack, per-site instances, adoption figures, AI navigator agents.
31. LAMP-platform draft deployment docs (unpublished). https://github.com/BIDMCDigitalPsychiatry/LAMP-platform/blob/master/docs/06-developer/05-deployment/index.md (accessed 2026-10-11). **Reported.** Self-hosted AWS cost estimates; BAA advice for self-hosters.
32. openFDA 510(k), PMA and registration searches for mindLAMP and Beth Israel Deaconess, https://api.fda.gov/device/510k.json?search=device_name:mindlamp and related queries (accessed 2026-10-11). **Primary.** No matches.
