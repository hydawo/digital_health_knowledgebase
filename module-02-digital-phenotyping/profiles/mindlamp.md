# mindLAMP (LAMP Platform)

## Quick Facts

| Field | Details |
|---|---|
| Organization | BIDMC Division of Digital Psychiatry (Beth Israel Deaconess Medical Center / Harvard Medical School), led by John Torous |
| Category | Open-source digital phenotyping and mobile-intervention platform, mental-health oriented |
| Current status | Active; LAMP-server, LAMP-dashboard, LAMP-core-ios and LAMP-core-android all pushed 2026-10-08 (GitHub API, checked 2026-10-10). Two old repositories archived in 2020 (see below) |
| Platforms/devices | "mindLAMP 2" app on Google Play (`digital.lamp.mindlamp`, updated 2026-05-17) and the App Store (seller John Torous, v2023.5.2, last updated 2023-05-26, although the LAMP-core-ios repository is still pushed in 2026); web dashboard. Checked 2026-10-10. |
| Open source | Partly. Source is public, but LAMP-server, LAMP-core-android and LAMP-core-ios carry no licence file (all rights reserved by default); LAMP-dashboard is AGPL-3.0; the API clients are BSD-3-Clause and LAMP-toolkit MIT (Verified 2026-10-10) |
| Hosting/deployment | Through the BIDMC **mindLAMP Core**, "the supported deployment pathway": self-hosted in the partner's own AWS account, a separate instance hosted and managed by BIDMC, or the shared BIDMC instance (lamp.digital). Self-hosting the unlicensed server outside that pathway needs BIDMC permission (Verified 2026-10-10) |
| Pricing model | No licence fee identified; source public with mixed licences. mindLAMP Core services and hosting are priced in a tailored proposal after a free consultation; no published figures (Verified 2026-10-10) |
| Last verified | 2026-10-10 (mindLAMP Core, licences, app-store listings, dead links) |

## Summary

- mindLAMP (Learn, Assess, Manage, Prevent), built on the "LAMP Platform," is an open-source digital phenotyping and mobile-intervention tool from Harvard-affiliated BIDMC's Division of Digital Psychiatry. It is explicitly positioned to support both **research and clinical use** of patient-generated health data, a dual orientation that distinguishes it from research-only platforms like Beiwe or RADAR-base. It combines active data collection (surveys, cognitive/behavioral tasks) with passive smartphone sensing, and is used by clinical research teams internationally (the search evidence names teams in Canada and Australia running adapted versions of the platform).

- **Status note, resolved in second pass (2026-08-24, Verified via direct GitHub fetch, resolves unresolved-question #87):** `LAMP-portal` and `LAMP-app` are not just labeled deprecated in their descriptions, **both were formally archived by their owner on Nov 17, 2020**, and GitHub reports each as "read-only." Direct inspection of the BIDMCDigitalPsychiatry organization's current (non-archived) repository listing shows the successor architecture clearly:

| Deprecated (archived 2020-11-17) | Current successor |
|---|---|
| `LAMP-portal` | `LAMP-dashboard` (the mindLAMP researcher/clinician web dashboard; TypeScript, actively updated as recently as Aug 21, 2026) |
| `LAMP-app` | `LAMP-core-android` (Kotlin) and `LAMP-core-ios` (Swift), described as "core scaffolding for digital phenotyping apps," rather than a single monolithic app repo |

- Other current, actively updated repositories confirmed in the same fetch: `LAMP-server` (backend, updated Aug 20, 2026), `LAMP-platform` (docs/issues), `LAMP-activities` (cognitive tests, updated Aug 19, 2026), `LAMP-app-gateway` (push/logging gateway), `LAMP-js` and `LAMP-py` (API clients, BSD-3-Clause licensed), `LAMP-cortex` and its successor `LAMP-toolkit` (analytics, MIT licensed). The organization hosts 32 repositories total; only the 10 most-starred/most-relevant were enumerated directly. **A prospective adopter should build on `LAMP-dashboard`, `LAMP-server`, and `LAMP-core-android`/`LAMP-core-ios`, not `LAMP-portal` or `LAMP-app`.**

## Products / Platform Architecture

- **mindLAMP app** (iOS/Android), participant-facing app for surveys, cognitive/behavioral tasks, and passive sensing.
- **mindLAMP dashboard**, researcher/clinician-facing web portal for study configuration and data review.
- **LAMP-server**, backend server component (TypeScript), actively updated (Aug 2026).
- **LAMP-dashboard**, researcher/clinician web dashboard (TypeScript), successor to the archived `LAMP-portal`.
- **LAMP-core-android** / **LAMP-core-ios**, mobile app scaffolding (Kotlin/Swift), successors to the archived `LAMP-app`.
- **LAMP-activities**, cognitive-test library.
- **LAMP-app-gateway**, push notification/logging gateway server.
- **LAMP-js** / **LAMP-py**, official JavaScript and Python API clients (BSD-3-Clause).
- **LAMP-cortex** (legacy) / **LAMP-toolkit** (current successor, MIT licensed), analytics pipeline.
- Legacy/archived: `LAMP-portal`, `LAMP-app`, both formally archived by the owner on 2020-11-17 (Verified, direct GitHub fetch, second pass).

## Sensors and Data Streams

- Every Module 2 profile uses the same table so platforms can be compared row by row. Rows are the passive streams named in `CLAUDE.md`. "Yes" and "No" are used only where a primary source says so; "Unclear" means nothing current was verified, and "No (OS)" means the operating system does not expose the stream to any third-party app. Confidence and sources are stated under the table. The convention is recorded in [`../../shared/profile-table-conventions.md`](../../shared/profile-table-conventions.md).

| Stream | Android | iOS | Raw or derived | Sampling configurable | Notes |
|---|---|---|---|---|---|
| GPS / location | Yes | Yes | Unclear | Unclear | Named in the documentation. |
| Accelerometer | Yes | Yes | Unclear | Unclear | Named. |
| Gyroscope | Yes | Yes | Unclear | Unclear | Named. |
| Magnetometer | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Barometer | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Ambient light | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Proximity | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Device motion / activity recognition | Unclear | Unclear | Derived. Steps, sleep and heart rate arrive from a paired wearable. | Unclear | Wearable-derived, not phone-sensed. |
| Screen state | Yes | Yes | Derived. Screen time. | Unclear | Named as screen time. |
| App usage | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Battery / charging | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Network / connectivity | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Wi-Fi | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Bluetooth | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Calls (metadata) | Yes | Unclear | Unclear | Unclear | Named as calls. iOS exposes no call log to third-party apps. |
| SMS (metadata) | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Keyboard | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Audio / microphone | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Notifications | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Device information | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |

**Verification.** Corroborated 2026-08-24 from docs.lamp.digital landing content, which names GPS, accelerometer, screen time, calls, heart rate, steps, sleep and gyroscope without a per-platform breakdown. "Yes" in both OS columns for named streams reflects the platform's dual-OS claim, not a per-stream check. Everything else is Unclear.

### Notes from earlier verification passes

- **Second-pass update (2026-08-24, Corroborated, direct fetch of docs.lamp.digital's landing content):** the documentation names passive streams including **GPS, accelerometer, screen time, calls, heart rate, steps, sleep, and gyroscope**, stated to flow into "one consistent format, enabling comparison across projects." This upgrades the general claim from Unclear to Corroborated, but the fetch was of general marketing/landing content rather than a full sensor-by-sensor reference page (unlike the AWARE second-pass result), so **exact iOS-vs-Android parity for each stream remains not independently verified**, still an open question, and one that matters given the platform's clinical-use orientation where data completeness has direct care implications.

## Derived Metrics / Analytics

- Not verified in any pass to date.

## Active Data Collection

- Surveys, cognitive tests, and behavioral tasks are core to the platform's stated "Assess" and "Manage" functions (per the LAMP name itself: Learn, Assess, Manage, Prevent). This is a materially more clinically-oriented active-assessment design than Beiwe's simpler survey model, per the platform's own framing, though exact EMA scheduling/branching sophistication was not independently benchmarked this session.

## Researcher and Study Management Features

- A dashboard/portal component exists for study and participant management, per the platform's own architecture description; specific features (multi-study support, role-based access, adherence monitoring) were not independently verified against current documentation this session.

## Data Access and Export

- Not independently verified against current documentation this session, flagged as an open question. The platform's dual research/clinical orientation implies data governance considerations (e.g., a clinician using the same platform for patient care) that are distinct from a research-only tool, and this distinction should be confirmed with the maintaining team before use in any protocol involving clinical decision-making.

## APIs, SDKs, and Extensibility

- Source is public under the BIDMCDigitalPsychiatry GitHub organization, but **not uniformly open-source licensed (checked 2026-10-09, Verified via the GitHub API and each repository's root):** `LAMP-dashboard` was relicensed to **AGPL-3.0** (its LICENSE.md says earlier copies stay under BSD-3-Clause), and `LAMP-server`, `LAMP-core-android` and `LAMP-core-ios` carry **no licence file at all**, which by default reserves all rights. Forking and modifying the server or the apps therefore needs permission from BIDMC; a modified dashboard run as a service must publish its changes under AGPL. All four repositories were pushed on 2026-10-08. **Second-pass update (2026-08-24, Verified via direct fetch):** licence terms are **not uniform across the codebase**, `LAMP-js` and `LAMP-py` (the official API clients) are **BSD-3-Clause**, and `LAMP-toolkit` (the analytics successor to `LAMP-cortex`) is **MIT**. The licence covering the core `LAMP-server`/`LAMP-dashboard`/`LAMP-core-android`/`LAMP-core-ios` repositories specifically was not confirmed (GitHub's org-level repository list did not surface it in this pass), narrower open item than before, since the client-library and toolkit licences are now settled. An `/api` section is referenced in docs.lamp.digital's navigation, consistent with `LAMP-js`/`LAMP-py` wrapping a documented REST API, though the API reference content itself was not fetched this session.

## Deployment and Infrastructure

- **Resolved 2026-10-10 (Verified):** the BIDMC **mindLAMP Core** is "the supported deployment pathway for the mindLAMP platform" (digitalpsych.org/mindlamp-core). Process (docs.lamp.digital/get-started): interest form, a reply "within a few business days", a free consultation, then "a tailored proposal including scope, deployment option, and pricing", then configuration and staff training. Deployment models (research.bidmc.org/mindlamp/services): "Full mindLAMP stack in partner's own AWS account", a "Dedicated instance managed by BIDMC team", or "the main mindLAMP instance at lamp.digital". The Core "requires a business agreement (established after Phase 1)". Its five phases cover a free design consultation; protocol optimisation; privacy-aware configuration, including "standardized language and configuration patterns for IRB and security review", role-based access controls and audit logs; hosting, uptime monitoring and software updates; and study support including shared analytics pipelines such as Cortex. The digitalpsych page names clinical research studies, grant-funded projects, clinical care programs and multi-site deployments as good fits and claims 50+ active sites. Eligibility criteria, fees and data-ownership terms are not published (the FAQ answers on cost and data access did not render for automated reading).
- Self-hostable server component (`LAMP-server`, Docker-deployable per its README, actively maintained). Because LAMP-server has no licence file, running or modifying it outside the Core pathway needs written permission from BIDMC. **Second-pass update (2026-08-24, superseded 2026-10-10 by the Core finding above):** docs.lamp.digital's own content advertises "flexible hosting and complete data access" as a platform capability, which is suggestive of a managed-hosting option beyond pure self-hosting, but the fetched content did not state whether this is a service offered to outside research/clinical teams, under what terms, or at what cost, **the managed-hosting question is upgraded from Unclear to Reported, not fully resolved; still requires direct BIDMC contact.** The earlier "clinical research teams in Canada and Australia" framing remains Reported only, not independently traced to a specific citation this session. Infrastructure requirements for self-hosting were not independently benchmarked.

## Participant Experience

- Not verified in any pass to date.

### Background keepalive (added 2026-10-09)

- No server-triggered keepalive like Beiwe's was found. `LAMP-app-gateway` sends Apple and Firebase push notifications, email and SMS, but its documented role is logging and notifications. A code search of the BIDMCDigitalPsychiatry organization for "heartbeat" returned nothing.
- The Android client runs a foreground service with low-priority notification channels. Community onboarding advice is to set location to "Always Allow", avoid low power mode and keep the phone charged, which puts the burden on participant behaviour.
- Status: **Corroborated** absence, from code and forum material, 2026-10-09. The official docs site did not answer the question. Sources 7 and 8.

## Privacy, Security, and Compliance

- **Checked 2026-10-10:** the Division of Digital Psychiatry privacy page (digitalpsych.org/privacy.html) makes no HIPAA, SOC 2 or GDPR claim and links only to BIDMC's general privacy policy. The mindLAMP Core page describes role-based access controls, audit logs for data access and changes, and IRB and security-review language as part of its configuration service; these are service descriptions, not certifications. No compliance certification is documented.
- Given the platform's explicit clinical-use positioning (not just research), HIPAA and comparable clinical-data-handling documentation would be a first-order question for any team considering clinical deployment, and CLAUDE.md's instruction not to infer compliance from institutional affiliation (Harvard/BIDMC) applies here as directly as anywhere in this module.

## Pricing

- No licence fee identified. Cost is either self-hosting infrastructure and staff time (with BIDMC permission for the unlicensed server and apps), or a BIDMC mindLAMP Core proposal covering services and hosting; figures are not public, and the first consultation is free (Verified 2026-10-10). No separate academic or commercial rate is published.

## Research Evidence and Validation

- mindLAMP has a substantial published research record centered on mental-health digital phenotyping, including the platform-description paper "Enabling Research and Clinical Use of Patient-Generated Health Data (the mindLAMP Platform): Digital Phenotyping Study" (Vaidyam, Halamka, Torous; *JMIR mHealth and uHealth*, Jan 2022) and subsequent studies on digital-phenotyping correlations in larger mental-health samples, EMA validation in schizophrenia populations, and COVID-related neuropsychiatric sequelae research in college students. This is a strong, mental-health-domain-specific published record, though this session did not attempt an exhaustive publication count.

## Strengths

- Explicit dual research/clinical orientation, distinguishing it from research-only competitors, potentially valuable for teams bridging digital phenotyping research into actual care pathways.
- Strong, mental-health-specific published research record from an established academic digital-psychiatry group.
- Public source code permitting inspection and institutional self-hosting; modifying the server or apps needs BIDMC permission because those repositories carry no licence (the dashboard is AGPL-3.0).
- A supported hosted route, the BIDMC mindLAMP Core, with a shared or dedicated BIDMC-hosted instance for teams without infrastructure capacity (priced by proposal).
- Combines active clinical assessment tools (cognitive/behavioral tasks) more deeply than some passive-sensing-first competitors.

## Limitations

- ~~Some component repositories are explicitly marked deprecated... this session could not fully map which components are current successors~~ **Resolved 2026-08-24**, `LAMP-portal` and `LAMP-app` are formally archived (2020-11-17); successors are `LAMP-dashboard` and `LAMP-core-android`/`LAMP-core-ios` respectively (Verified, direct GitHub fetch).
- The core server and apps carry no licence (dashboard AGPL-3.0), so the platform is source-available rather than open source end to end (Verified 2026-10-10).
- Exact per-stream iOS/Android sensor parity, full data-export mechanics and compliance posture remain not independently verified against current documentation, even after this second pass, docs.lamp.digital's full reference documentation (as opposed to its landing content) is the next direct-fetch target for a third pass.
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
- ~~What open-source licence governs the core `LAMP-server`/`LAMP-dashboard`/`LAMP-core-android`/`LAMP-core-ios` repositories?~~ **Answered 2026-10-09:** dashboard AGPL-3.0; server and both apps unlicensed. New question: does BIDMC grant outside teams written permission to self-host and modify the unlicensed components?
- What is the exact per-stream iOS-vs-Android sensor parity? (The general passive-sensor list, GPS, accelerometer, screen time, calls, heart rate, steps, sleep, gyroscope, is now Corroborated, but not broken out by platform.)
- What HIPAA/GDPR/compliance documentation exists, particularly for the clinical-use pathway as distinct from pure research use? (Still open 2026-10-10: the privacy page makes no such claim.)
- ~~Is "flexible hosting" a managed service for outside teams?~~ Resolved 2026-10-10: yes, via the mindLAMP Core (separate or shared BIDMC instance). Still open: fee schedule, academic vs industry rates, eligibility, and data-ownership terms for BIDMC-hosted studies.
- Why does the public App Store build (v2023.5.2, 2023-05-26) lag the actively pushed LAMP-core-ios repository? Is a newer iOS build distributed another way?

## Key Links

- Digital Psych (lab site): https://www.digitalpsych.org/mindlamp1.html
- Documentation: https://docs.lamp.digital/
- GitHub organization: https://github.com/BIDMCDigitalPsychiatry
- LAMP-server repository: https://github.com/BIDMCDigitalPsychiatry/LAMP-server
- LAMP-dashboard repository: https://github.com/BIDMCDigitalPsychiatry/LAMP-dashboard
- Publications: https://docs.lamp.digital/about/publications/ (dead link, HTTP 404, checked 2026-10-10; use https://docs.lamp.digital/)
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
8. mindLAMP community forum (mindlamp.discourse.group) threads on notifications, battery and onboarding (accessed 2026-10-09, search summary). **Reported.** The host no longer resolves (DNS failure, checked 2026-10-10), so these threads cannot be re-read.
9. BIDMCDigitalPsychiatry repository licences, checked 2026-10-09 via https://api.github.com/repos/BIDMCDigitalPsychiatry/<repo> and https://github.com/BIDMCDigitalPsychiatry/LAMP-dashboard/blob/master/LICENSE.md. **Primary/Verified.** LAMP-dashboard AGPL-3.0 (previously BSD-3-Clause); LAMP-server, LAMP-core-android, LAMP-core-ios no licence file.
10. BIDMC, "mindLAMP Core services." https://research.bidmc.org/mindlamp/services (accessed 2026-10-10, direct fetch). **Primary/Verified.** Three deployment models, five phases, business agreement after Phase 1; no prices.
11. mindLAMP documentation, "Get started." https://docs.lamp.digital/get-started (accessed 2026-10-10, direct fetch). **Primary/Verified.** Interest form, free consultation, tailored proposal with scope, deployment option and pricing.
12. Division of Digital Psychiatry, "mindLAMP Core." https://www.digitalpsych.org/mindlamp-core (accessed 2026-10-10, direct fetch). **Primary/Verified.** "supported deployment pathway"; good-fit users; 50+ active sites (vendor claim).
13. GitHub API repository metadata for LAMP-server, LAMP-dashboard, LAMP-core-ios, LAMP-core-android (accessed 2026-10-10). **Primary/Verified.** All pushed 2026-10-08; licence None for server and apps, AGPL-3.0 text in LAMP-dashboard/LICENSE.md.
14. App Store (iTunes lookup id 1495947054) and Google Play (`digital.lamp.mindlamp`) listings, direct fetch 2026-10-10. **Primary/Verified.**
15. Division of Digital Psychiatry privacy page. https://www.digitalpsych.org/privacy.html (accessed 2026-10-10, direct fetch). **Primary.** No compliance claims.
