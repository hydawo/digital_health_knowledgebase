# CARP Mobile Sensing (Copenhagen Research Platform)

## Quick Facts

| Field | Details |
|---|---|
| Organization | Technical University of Denmark (DTU); Jakob E. Bardram's group |
| Category | Open-source cross-platform mobile sensing framework for digital phenotyping |
| Current status | Active; CAMS API 2.0 released April 2026 and the rebuilt CARP Studies app version 5 in September 2026 (iOS 5.1.0 on 2026-10-06) [22][28]; carp.sensing-flutter pushed 2026-10-09 and carp-portal 2026-10-07 (GitHub API, checked 2026-10-10); `carp_mobile_sensing` distributed via pub.dev |
| Platforms/devices | Android and iOS (cross-platform via Flutter). DTU's reference app "CARP Studies" is free on Google Play (`dk.cachet.carp_study_app`) and on the Apple App Store as an unlisted app reachable only by link (id 1569798025, seller Danmarks Tekniske Universitet, iOS 15.0 or later, version 5.1.0 released 2026-10-06) (Verified 2026-10-11) [23]. Teams can also build their own app on CAMS |
| Open source | Yes, MIT licence on all seven main repositories (Verified 2026-10-11) [34] |
| Hosting/deployment | Three documented routes: the DTU-hosted CARP service on Computerome (only for research projects where DTU Health Tech is an active research partner; research use only; no SLA) [21], a self-hosted CARP instance from the open-source components (CAWS backend, Web Portal, Studies App), or a custom app on CAMS pointed at any server (Verified 2026-10-11) |
| Pricing model | Software free/open source (MIT), no licence or API fees. DTU-hosted service has a published 2024 rate table: 45,000 DKK one-time study setup, 1,250 DKK per study per month, staff time and a Computerome operations fee; actual cost is agreed per project (Verified 2026-10-11) [21] |
| Last verified | 2026-10-11 (vendor fact record) |

## Summary

- CARP Mobile Sensing (CAMS) is the sensing component of the Copenhagen Research Platform (CARP), an open-source family of components from DTU for building mobile-health research apps. Unlike most platforms in this module, CAMS is explicitly a **cross-platform (Flutter-based) programming framework and runtime**, not primarily a hosted dashboard product, it is distributed as the `carp_mobile_sensing` Flutter package (available on pub.dev), meaning research teams build their own study app on top of it rather than configuring an existing app through a web portal. This is a materially different adoption model than Beiwe, RADAR-base, or the commercial platforms in this module, closer in spirit to a software library than a product.

- **Added under CLAUDE.md's "starting point, not a closed list" clause**, CARP was not named in the module's initial scope list but is a genuinely active, distinctive, peer-reviewed open-source competitor and was included on that basis, mirroring how Module 1 added Axivity/GENEActiv beyond its own starting list.

## Products / Platform Architecture

- **CARP Core**, the underlying study-protocol and data-model framework.
- **CARP Mobile Sensing (CAMS)**, the Flutter-based sensing runtime, providing a "reactive and unified programming model" for collecting from on-board smartphone sensors and attached off-board wearables (the project's own materials name ECG-monitor wearable integration specifically).
- **`carp_mobile_sensing`**, the distributed Flutter package implementing CAMS, on pub.dev.
- Data-transformer support for converting collected data to standardized formats and applying privacy-preserving transformations is named as a first-class framework feature.

## Sensors and Data Streams

- Every Module 2 profile uses the same table so platforms can be compared row by row. Rows are the passive streams named in `CLAUDE.md`. "Yes" and "No" are used only where a primary source says so; "Unclear" means nothing current was verified, and "No (OS)" means the operating system does not expose the stream to any third-party app. Confidence and sources are stated under the table. The convention is recorded in [`../../shared/profile-table-conventions.md`](../../shared/profile-table-conventions.md).

| Stream | Android | iOS | Raw or derived | Sampling configurable | Notes |
|---|---|---|---|---|---|
| GPS / location | Yes | Yes | Raw location; derived mobility features | Yes | Location sampling package. |
| Accelerometer | Yes | Yes | Raw, with and without gravity; derived higher-order features over a window | Yes, per measure; default every 200 ms (5 Hz) | Sensors package [24][25]. |
| Gyroscope | Yes | Yes | Raw | Yes, per measure; default every 200 ms (5 Hz) | Sensors package [24][25]. |
| Magnetometer | Yes | Yes | Raw | Yes, per measure; default every 200 ms (5 Hz) | Sensors package [24][25]. |
| Barometer | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Ambient light | Yes | No | Derived light summaries | Yes; default 10 s every 5 min | Marked Android only in the packages table [24][25]. |
| Proximity | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Device motion / activity recognition | Yes | Yes | Derived. Activity package. | Yes |  |
| Screen state | Yes | No | Event (screen on/off) | Unclear | Marked Android only in the packages table [24]. |
| App usage | Yes | No | Unclear | Yes | Apps package; installed apps and app usage marked Android only [24]. |
| Battery / charging | Yes | Yes | Unclear | Unclear | Battery package; battery level listed for the Studies app v5 [22][24]. |
| Network / connectivity | Yes | Yes | Unclear | Yes | Connectivity package. |
| Wi-Fi | Yes | Yes | Event (SSID and BSSID of the connected network) | Unclear | Listed for Android and iOS in the measure-types table on 2026-10-30; the 2026-10-11 table marked it Android only [24]. |
| Bluetooth | Yes | Foreground only | Event (BLE scans) | Unclear | Connectivity package; iOS scans only in the foreground [24]. |
| Calls (metadata) | Yes | No (OS) | Metadata. Communication package. | Yes |  |
| SMS (metadata) | Yes | No (OS) | Metadata. Communication package. | Yes |  |
| Keyboard | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Audio / microphone | Yes | Yes | Raw audio; derived noise level. Audio package. | Yes | Video and image packages also exist. |
| Notifications | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Device information | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |

**Verification.** Rows for accelerometer, gyroscope, magnetometer, ambient light, screen, app usage, battery, Wi-Fi and Bluetooth Verified 2026-10-30 against docs.carp.dk's measure-types table, which marks ambient light, screen events, free memory, installed apps, app usage, call logs and SMS as Android only and Bluetooth as foreground only on iOS, and the sensors package source for the 200 ms default [24][25]. Other rows Verified 2026-08-25 from carp.dk/cams, which names the sampling packages. Barometer, proximity, keyboard, notifications and device information remain unverified. Sampling is configurable per measure in the study protocol. Data uploads to CAWS every 10 minutes by default. Wearable sampling rates are set by the device SDKs and are not tabulated in the CARP docs.

**Achieved coverage.** CARP's own 2025 coverage tests on Android 14 and iOS 18 found that both OSes pause or kill the app without user interaction, unless a BLE wearable keeps it running, so nominal rates are not achieved coverage [31].

**Wearables and health records (Verified 2026-10-11) [24][29].** Polar accelerometer, gyroscope, magnetometer, ECG, PPI, PPG and HR; Movesense HR, ECG and IMU; Movisens (Android); eSense; Apple Watch via the AWARE watchOS package (iOS/watchOS only); Apple Health and Health Connect records, which are read only while the app is in the foreground, and on iOS only while the phone is unlocked. CARP Gardener, a server-side component, pulls Fitbit, Garmin, Withings and Dexcom cloud data; CARP's 2026-09-28 post describes it as for future studies, so it is existing code, not a live route in the Studies app [22][29]. The CARP Studies app collects a subset of the CAMS streams.

### Notes from earlier verification passes

- **Materially expanded 2026-08-25 (second pass, Verified via direct fetch of `carp.dk/cams/`).** The wearable-integration catalog is substantially broader than the first pass's generic "ECG monitor" reference. Confirmed named integrations:

- **On-board phone sensors** (via CAMS "sampling packages"): apps, connectivity, communication, location, activity, weather, audio, video, image, survey data.
- **Health-platform integration**: **Apple Health and Google Health Connect** are named directly as supported data sources, a HealthKit/Health Connect integration that was not previously documented in this profile and is a genuine differentiator (few other platforms in this module have confirmed HealthKit/Health Connect integration).
- **Named wearable devices**: Movisens (Move4, EcgMove4, EdaMove4), the eSense earplug, Polar (H10, Verity Sense), Movesense (MD, Active), and the Dexcom G7 continuous glucose monitor, a far more itemized and diverse list than "ECG monitor," spanning cardiac, EDA, activity, audio-wearable, and continuous-glucose sensing.

- Because CAMS is Flutter-based and explicitly cross-platform, iOS/Android sensor parity is at least a stated design goal, but this session still did not independently verify parity for every individual sensor stream, and CLAUDE.md's instruction not to assume iOS/Android parity still applies even to platforms designed cross-platform from the start, since underlying OS constraints (especially iOS background execution limits) apply regardless of the app framework used.

## Derived Metrics / Analytics

- Data-transformer components support standardized-format conversion and privacy-preserving transformation as part of the core framework, per the project's own materials, implying at least some built-in processing capability beyond raw pass-through, though a Forest-comparable derived-metrics catalog was not identified.
- **On the phone (Verified 2026-10-11) [24][30].** Mobility features from location, accelerometer higher-order features over a window, OS activity recognition, noise level and light summaries.
- **Participant-facing.** The CARP Studies app shows weekly cards for steps, heart rate, sleep, mobility and task progress [22].
- **Server side.** CAWS lets researchers deploy Python analysis scripts to a data processing pipeline, and the `carp-dsp` repository provides a data-science pipeline framework [30]. No ready-made catalogue of clinical digital biomarkers is published.

## Active Data Collection

- Surveys and cognitive tests are CAMS data sources and are collected by the CARP Studies app (Verified 2026-10-11) [22][24]. Scheduling, branching and EMA options were not verified.

## Researcher and Study Management Features

- **Updated 2026-08-25 (second pass, Verified via direct fetch of `github.com/carp-dk`), this materially changes the prior "not a dashboard product" characterization.** The `carp-dk` GitHub organization (42 repositories total) includes several components beyond the CAMS sensing runtime itself:

- **`carp-portal`**, a JavaScript-based repository whose name and presence indicate a researcher-facing portal/dashboard component exists as part of the broader CARP platform family, distinct from the CAMS Flutter sensing package. Its feature completeness and documentation quality were not independently verified this session, its existence, not its depth, is the confirmed finding.
- **`carp-cli`**, a terminal client "with a native protocol editor," suggesting a command-line route to defining and managing study protocols without a GUI.
- **`carp-webservices-spring`**, a REST-based backend service (Kotlin/Spring Boot), implying a maintained server-side API layer exists for CARP deployments generally.
- **`carp.core-kotlin`**, described as an "infrastructure-agnostic framework for distributed data collection," i.e., the underlying study-protocol/data-model layer CAMS itself sits on top of.
- **`carp_study_app`**, a reference/example study app built on CAMS.

- **Revised conclusion**: CARP is still fundamentally a framework/library-first ecosystem rather than a single polished turnkey product, and a research team should not assume `carp-portal` is a mature, feature-complete, documented dashboard equivalent to Beiwe's or Avicenna's, that was not established. But it is no longer accurate to say study-management tooling is "not offered" or "entirely the adopting team's responsibility to build", CARP's own organization maintains portal, CLI, and backend-service components alongside the sensing library.

### `carp-portal` assessment (added 2026-10-09)

- **What it is (Verified from the repository).** A React 19 and Material UI 9 web app (package.json on the default branch: `"react": "^19.2.8"`, `"@mui/material": "9.1.0"`, version 2.0.0; corrected 2026-10-10 from "React 18"), MIT licence, created 2024-06-20. About 230 commits from four contributors, last push 2026-10-07. No tagged releases; the CHANGELOG's only entry is "2.0.0 [TBD]", which adds a Research Assistant role.
- **Pages in the source tree.** Studies; study overview; study settings, with researchers, invitations, self-signup, study status and study data; protocols and protocol versions; participants, including add, bulk import and new deployment; per-deployment pages with devices, informed consent and data visualisation; per-participant pages with data cards and visualisation; recent-data and participant-record views; exports, with download and delete; study announcements; resources and translations; account management.
- **What CARP says it does.** CARP's own pages describe it as the researcher interface for uploading JSON study protocols, creating and deploying studies, recruiting participants, managing running studies and downloading data as JSON. Protocols are written as JSON, or with `carp-cli`'s protocol editor, rather than built in a graphical form editor.
- **Hosting.** It is not part of the CAMS app. It needs the CARP Web Services backend (`carp-webservices-spring`) and a Keycloak identity server, and ships as a Docker image built by GitHub Actions. Self-hosting means running all three, plus PostgreSQL, in Docker or Kubernetes. The alternative is DTU's hosted instance on DTU Computerome.
- **Documentation.** The README covers developer setup and deployment only. No researcher user manual was found on carp.dk or in the repository.
- **Who can use the hosted instance (resolved 2026-10-11, Verified) [21].** The hosting terms page (carp.dk/hosting/, modified 2026-08-23) limits the service to research projects where DTU Health Tech is an active research partner, meaning DTU helped initiate the study, secure funding and define the protocol, and takes part in publication. Non-DTU researchers can use it only through such a partnership; teams that cannot accept this are pointed to self-hosting. The 2026-09-28 Studies app post repeats the rule [22]. The older CAWS page's "Researchers affiliated with DTU" wording is a narrower phrasing of the same rule, and the "Three ways" page's invitation to email info@carp.dk is a route to that conversation, not separate access terms. The page also publishes prices (see Pricing).
- **Getting an account [35].** No form. Email info@carp.dk or support@carp.dk, or ask on Discord. The CAWS team creates the study and registers a custom app for sign-in; a test server (dev.carp.dk) is used while testing. The earlier docs said researcher accounts were by invitation; the rebuilt docs (October 2026) no longer say so.
- **Assessment.** The portal is a real, actively developed study-management dashboard covering protocols, deployments, participants, consent, data visualisation and export. It is not a configure-everything-in-the-browser product like Avicenna's. It has no versioned releases, no end-user documentation, and nothing found about adherence alerts or audit logs. It sits between "build it yourself" and a mature commercial dashboard. **Corroborated**: the page inventory is Verified from code, but feature depth was read from page names and vendor descriptions, not from running the portal.

## Data Access and Export

- Standardized data-format output and privacy-preserving transformation are named framework features.
- The CARP Web Portal lets researchers "download the collected data in JSON format" for offline analysis in R, Python or other tools (Verified 2026-10-10, "Three ways to use CARP", posted 2026-07-14). On the DTU-hosted service DTU is the data controller, and CAWS provides a Python library for writing analysis scripts that are deployed to its data-processing pipeline (CAWS page, read 2026-10-10).
- **Export routes (Verified 2026-10-11).** Hosted or self-hosted CAWS offers Portal Export (JSON), the `carp-cli` command-line tool and its Python module, the CAWS REST API and the `carp_webservices` Dart client. A custom CAMS app can store locally (SQLite or zipped JSON), send to any endpoint through its own data manager, or use Firebase, which is not yet on API 2.x. Transformer schemas map data to Open mHealth and FHIR [28][36].
- **History.** Collection is prospective from enrolment. Probes that read stored phone data (app usage, calls and texts) look back one day by default, configurable [24].
- **Rate limits.** The only documented limit is on the public self sign-up endpoint, 20 requests per minute per IP by default and configurable by the server operator. No limits are published for upload, export or the rest of the REST API [27].
- **Known upload bug.** An open issue (carp.sensing-flutter #623, read only) reports that one rejected measurement can make an upload batch retry forever; a fix is proposed in PR 624.

## APIs, SDKs, and Extensibility

- **Deprecations (Verified 2026-10-11) [28].** CAMS API level 2.0 (2026-04-14) redesigned the architecture and restructured the packages. The CAWS legacy DataPoint upload endpoint and the old informed-consent endpoint are deprecated but still supported. The `dk.cachet.carp` data namespace is to change to `carp.dk` at an unannounced date. The CARP health plugin dropped Google Fit in version 11.0.0, though the 2026-07-14 "Three ways" post still lists a Google Fit integration. CARP Studies app version 5 (2026-09-28) replaced the earlier app.
- **Custom apps on a CAWS server.** Whoever runs the server must register the app and issue a clientId and redirect URI [35].
- This is CAMS's core identity and its clearest differentiator in this module: it is, by design, a programming framework/SDK rather than a configured product. Full MIT-licence source access (copyright DTU) allows unrestricted institutional modification. Real-world use spans mental health, cardiovascular disease, and diabetes mHealth applications, per the project's own "About" materials, evidence that multiple distinct research apps have been built on top of CAMS rather than it being single-study tooling.

## Deployment and Infrastructure

- **Three routes (Verified 2026-10-10, carp.dk "Three ways to use CARP", posted 2026-07-14; hosted-service terms re-verified 2026-10-11 on carp.dk/hosting/):**
  - **DTU-hosted service:** runs "on DTU Computerome", and the managed environment "handles infrastructure, security, and data storage on your behalf"; the Web Portal lets hosted users "upload protocols, create studies, recruit participants, deploy studies, and manage ongoing studies". The hosting terms limit it to research projects where DTU Health Tech is an active research partner, exclude clinical treatment and commercial services, and give no SLA or service guarantee of any kind (Verified 2026-10-11) [21]. Data is stored on DTU servers at Computerome in Denmark [22]. Prices are published (see Pricing). No commercial managed hosting is offered.
  - **Self-hosted:** "deploy your own instance of CARP using our open-source components" (CARP Web Services, the Web Portal and the Studies App), on Docker or Kubernetes with PostgreSQL. The self-hoster is data controller and sets its own SLAs [21].
  - **Custom app:** build a Flutter app on CAMS and the other packages.
- For the custom-app route a research team integrates the `carp_mobile_sensing` package into its own Flutter app and stands up whatever backend/storage infrastructure it needs. This requires genuine mobile-development capacity (Flutter/Dart), a different and arguably higher technical floor than configuring an existing dashboard-based platform, though lower than standing up a full backend like Beiwe's or RADAR-base's if the study doesn't need custom backend infrastructure.

## Participant Experience

- **App (Verified 2026-10-11) [23].** CARP Studies is free on Google Play and on the App Store as an unlisted app reached only by link (iOS 15.0 or later). Version 5 was rebuilt from the ground up and announced 2026-09-28. The App Store lists English and Danish; CARP's v5 post says English, Danish and Spanish.
- **Enrolment [22][35].** One protocol serves any number of participants. Participants join by email invitation, one per person, or by self sign-up with a study code, where the researcher sets the maximum number of participants and can turn sign-up off.
- **Background operation.** See the coverage note under Sensors and Data Streams: without user interaction both OSes paused or killed the app in CARP's 2025 tests [31].

### Background keepalive (added 2026-10-09)

- CAMS has a `heartbeat` measure. It is a **client-side** data point that the phone records on a fixed interval, so researchers can check sampling coverage afterwards. The CHANGELOG says every 5 minutes; the current device sampling package sets a 15-minute default. It does not wake the app.
- No server-triggered push that reopens a stopped CAMS app was found in the CAMS, CARP Web Services or portal materials checked. Any such mechanism would sit in the app built on CAMS. m-Path Sense, which embeds CAMS, has one (see the m-Path profile).
- Status: **Corroborated** absence of a built-in server-side keepalive, from code and docs, not from a statement by DTU.

## Privacy, Security, and Compliance

- Privacy-preserving data transformation is named as a first-class framework capability (allowing e.g. on-device or pipeline-stage anonymization/aggregation before storage), which is architecturally notable, few other platforms in this module document this as a built-in framework feature rather than a per-study custom implementation. - **GDPR roles are documented (Verified 2026-10-10, "Three ways to use CARP"):** for the hosted service "DTU acts as a data controller", "DTU cannot act as a data processor" for a non-DTU controller, and data "stays within the EU/EEA by default". For self-hosting, "your institution is both data controller and data processor"; for a custom app the team carries the regulatory responsibility.
- **GDPR basis (Corroborated 2026-10-11) [21][26].** DTU processes hosted-service data under the GDPR and the Danish Data Protection Act, on the basis of GDPR Articles 6(1)(e), 9(2)(j) and 10.
- **Data processing agreements (Corroborated 2026-10-11) [21].** The hosted service cannot be subject to a data processor contract with another organisation. Outside partners can receive selected data under a short disclosure contract, or become DTU's data processors under a full DTU-standard data processor agreement; otherwise only aggregate anonymous data is shared. Joint controllership is possible only rarely, in large funded projects. The setup fee covers a data disclosure agreement but not fuller data processing agreements.
- **Retention, conflict (Unclear, 2026-10-11) [26].** DTU's study-app privacy policy keeps data as long as relevant to the study and for at least five years, and lets participants request erasure; on the phone data is kept only until upload. The CARP Studies Google Play data safety section, filed by DTU, says data can't be deleted and that there is no way to request deletion. Both are DTU statements, so this stays a conflict until DTU corrects one. Self-hosted CAWS keeps export files 7 days by default.
- **AI training.** Not public. No AI or machine-learning training terms; the app policy allows use of personal data to improve CARP applications and services and says DTU never sells or donates personal data [26].
- **Certifications and US regulation (not public, 2026-10-11).** No HIPAA statement or BAA, no ISO 27001 claim and no SOC 2 report was found for CARP; the hosting page says only that data management follows DTU's research data management principles. openFDA returned no matches for DTU or CARP on 2026-10-11 [32]. CARP's own guidance says the EU MDR may apply to custom clinical apps built on it.

## Pricing

- Free and open source (MIT licence); no licence or API fee. Self-hosting and custom-app cost is the adopting team's own development and infrastructure effort.
- **DTU-hosted service (Verified 2026-10-11) [21].** Follows DTU's co-financed research price model. 2024 prices in DKK:
  - One-time study setup 45,000, including a data disclosure agreement but not fuller data processing agreements.
  - Hosting and maintenance 1,250 per study per month.
  - Staff time per month: student assistant 16,700, research assistant 68,100, researcher 78,000, senior researcher 105,000.
  - A monthly Computerome operations fee.
- Normally the cost is a budget line in the joint project budget; smaller projects may pay as they go at actual cost plus 44% overhead. Invoicing is typically yearly. The actual amount is agreed per project, since the service is only available through a research partnership. Prices are labelled 2024 and may have been indexed since.
- **Minimum commitment.** Not public. No minimum term or amount is stated; the partnership requirement is the effective commitment.
- **Funding.** The hosted service is funded in part by a DKK 5 million Novo Nordisk Foundation infrastructure grant (2023) [33]. No grant or membership program for outside teams was found.

## Research Evidence and Validation

- CAMS is documented in a dedicated architecture paper ("The CARP Mobile Sensing Framework, A Cross-platform, Reactive, Programming Framework and Runtime Environment for Digital Phenotyping") and has been used to build multiple distinct mHealth research applications across mental health, cardiovascular disease, and diabetes domains, per the project's own materials. **New 2026-08-25 (second pass, search-summary):** a follow-up demonstration paper, "The CARP Mobile Sensing Framework, Demonstration," was presented at the **2025 ACM International Joint Conference on Pervasive and Ubiquitous Computing (UbiComp/ISWC 2025)**, evidence of continued, current academic engagement with the framework at a major venue, five years after the original 2020 architecture paper. This session did not confirm the authors' institutional affiliation for the 2025 paper (i.e., whether it demonstrates DTU-external use or is authored by the same DTU group), so it should not yet be read as resolving the "adoption outside DTU" open question, it is evidence of currency, not external adoption. This session also did not attempt a systematic count of downstream published studies using apps built on CAMS.

### Adoption outside DTU, and DiaFocus (added 2026-10-09)

- **External adoption, Partly resolved.** A literature and code pass on 2026-10-09 found **one** confirmed production deployment of CAMS by a group outside DTU: **m-Path Sense**, built by KU Leuven's m-Path team by adding CAMS to m-Path as a plug-in. It is available in both app stores and was evaluated with 104 participants in Niemeijer et al. 2023, *JMIR Formative Research*. That paper thanks the CAMS creators "for their technical contribution", so it was built with DTU's help. Verified from full text.
- Every other paper found that names CARP or CAMS in its full text (Europe PMC) has a DTU co-author: DiaFocus, SLEEPINESS (2024), the ambulatory ECG study (2025), episodic future thinking (2024) and the 2025 UbiComp demo. The demo's two authors are both DTU (Crossref), which closes the earlier open point about that paper.
- The CAMS architecture papers are rarely cited: arXiv 2020 three times and *Sensors* 2022 four times, per OpenAlex. All 16 packages that depend on `carp_mobile_sensing` on pub.dev are CARP's own. A Münster psychiatry app paper (ReMAP, 2021) cites CAMS, but its abstract does not say it was built on CAMS.
- Reading: external adoption is real but narrow. It amounts to one confirmed independent product, which has since become a widely used commercial EMA platform. Citation counts undercount use because a library is often not cited. **Corroborated.**
- **DiaFocus is built on CAMS (Verified from the developer).** CARP's own DiaFocus page says the system "makes use of most CARP components". Its September 2025 post on the clinical validation says the app "was built using several CARP components, including CARP Mobile Sensing and the Research Package", connected to CARP Web Services hosted at DTU Computerome. The 2023 design paper's abstract says only "a generic data collection framework for mobile and wearable sensing", and the 2025 *JMIR Diabetes* pilot never names CARP, so attribution rests on the developer's own statement. DiaFocus ran a 6-week feasibility study with 12 patients (2023) and a 6-month clinical pilot at Steno Diabetes Center Copenhagen (2025). Both involve DTU authors: the 2025 pilot is led from Steno Diabetes Center Copenhagen (first author Lind), with DTU co-authors Bækgaard and Bardram (author affiliations checked in Europe PMC, 2026-10-10). So this adds a second CAMS deployment, not external adoption.

## Strengths

- Genuinely cross-platform (Flutter) by architectural design from the outset, rather than an Android-first codebase with a later iOS port (contrast with AWARE).
- MIT licence, one of the more permissive open-source licences among the platforms profiled in this module. **Verified 2026-10-11** on seven `carp-dk` repositories via GitHub's licence API: `carp.sensing-flutter`, `carp-webservices-spring`, `carp-portal`, `carp_study_app`, `carp.core-kotlin`, `carp-gardener` and `carp-cli`, copyright Technical University of Denmark. Some newer repositories (`carp-docs-starlight`, `carp-dsp-portal`, `carp-app-site-ts`) declare no licence [34].
- Published price list for the hosted service, unusual among academic platforms in this module [21].
- Built-in privacy-preserving data-transformation support as a first-class framework feature, not a per-study bolt-on.
- Demonstrated reuse across multiple distinct disease-domain research apps, evidencing real framework maturity rather than single-study tooling; a 2025 ACM UbiComp demonstration paper indicates continued current engagement.
- **Materially expanded 2026-08-25**: named wearable integration now spans Movisens (ECG/EDA/activity), eSense, Polar, Movesense, and the Dexcom G7 CGM, not just "ECG monitor", plus confirmed Apple Health and Google Health Connect integration, a genuine differentiator versus other platforms in this module.
- **New 2026-08-25**: a `carp-portal` repository exists, indicating a researcher-dashboard component is part of the broader CARP ecosystem, not solely the adopting team's responsibility (see Researcher and Study Management Features above for the appropriate caveats).

## Limitations

- Using CAMS for a bespoke app means building a custom Flutter app, which requires real mobile-development capacity. The DTU-hosted service with the CARP Studies app and Web Portal avoids that, but only for research projects where DTU Health Tech is an active research partner (helping initiate, fund and design the study and taking part in publication), research use only, with no SLA [21].
- ~~No researcher-facing web dashboard/study-management product was identified~~, **revised 2026-08-25**: a `carp-portal` repository exists, but its feature completeness, documentation, and production-readiness were not independently verified this session, treat as "exists, depth unconfirmed" rather than "absent."
- Several phone streams are Android only: ambient light, screen events, app lists, app usage, calls and SMS; Bluetooth scans on iOS run only in the foreground [24]. Barometer, proximity, keyboard, notifications and device information were not verified. No HIPAA, ISO 27001 or SOC 2 claim is published.
- Retention terms conflict between DTU's privacy policy and its Google Play data safety label (see Privacy) [26].
- Smaller apparent ecosystem/community footprint than Beiwe, RADAR-base, or AWARE in general digital-phenotyping methods literature, GitHub signals checked this session (84 stars / 31 forks on the core Flutter sensing repo) are modest relative to the module's larger academic platforms, though this was not systematically benchmarked star-for-star.

## Best-Fit Use Cases

- Research teams with in-house Flutter/mobile-development capacity that want a proven, MIT-licensed sensing engine to build a fully custom study app on top of, rather than working within another platform's dashboard constraints.
- Studies needing genuinely first-class cross-platform (iOS/Android) sensing architecture from a single codebase.
- Studies needing wearable (e.g., ECG) integration alongside phone sensing within a unified framework.

## Poor-Fit Use Cases

- Teams without mobile-development capacity that cannot take DTU Health Tech on as an active research partner (the condition for the hosted service) and need a configure-don't-code study app.
- Clinical treatment or commercial services on the hosted instance, which its terms exclude; such teams must self-host or build on the open-source packages [21].
- Studies needing an existing, ready-to-use, well-documented researcher dashboard for participant/study management out of the box, `carp-portal` exists (see above) but its maturity relative to Beiwe's or Avicenna's dashboards was not established this session, so this remains a caution rather than a confirmed absence.
- Rapid-timeline pilots where standing up a custom app is not feasible before enrollment.

## Open Questions

- *(Directed to: CARP / Jakob Bardram's group, DTU, via https://carp.dk/)*

- ~~Does a companion researcher dashboard/study-management product exist?~~ **Resolved (existence) 2026-08-25**, `carp-portal` exists. ~~How feature-complete and documented is `carp-portal`?~~ Largely resolved 2026-10-09, see Researcher and Study Management Features. ~~Whether non-DTU researchers can get accounts on the hosted instance, and at what cost.~~ Resolved 2026-10-11: only through a research partnership with DTU Health Tech; 2024 rates are published on carp.dk/hosting/ (see Pricing).
- ~~What is the full current wearable-integration catalog beyond ECG monitors?~~ **Resolved 2026-08-25**, see Sensors and Data Streams above (Movisens, eSense, Polar, Movesense, Dexcom G7, plus Apple Health/Google Health Connect).
- ~~What GDPR/compliance documentation or guidance exists?~~ Partly answered 2026-10-10: controller and processor roles and EU/EEA residency are documented (see Privacy). No certification is claimed.
- What export formats and backend-storage patterns are typical/recommended for CAMS deployments (the portal exports JSON, Verified 2026-10-10), and does `carp-webservices-spring` represent the standard/recommended backend, or one option among several?
- ~~How many independent research groups outside DTU have built production studies on CAMS? Does the 2025 UbiComp demo include non-DTU authors?~~ Partly resolved 2026-10-09: one confirmed (KU Leuven, m-Path Sense); the demo authors are both DTU. An exhaustive count would need DTU's own list of adopters.
- ~~Is DiaFocus built on CAMS?~~ Resolved 2026-10-09: yes, per CARP's own DiaFocus pages.

## Vendor Fact Record

<!-- facts:begin -->
*Generated from the fact record by `tools/facts/generate.py`. Edit the record, not this block.*

**Research access**

| Fact | Value |
|---|---|
| Formal research or academic program (name, what it offers) | No grant or membership program. DTU Health Tech runs a hosted CARP instance (CARP Web Services, the CARP Study Portal and the CARP Studies app) on Computerome for research projects in which DTU Health Tech is an active research partner. The service is funded in part by a DKK 5 million Novo Nordisk Foundation infrastructure grant (2023). Outside the hosted service, all components are open source for self-hosting or building a custom app. [V, 2026-10-11] |
| Who can join the research program | The DTU-hosted service is only for research projects where DTU Health Tech is an active research partner, meaning DTU helped initiate the study, secure funding and define the protocol, and takes part in publication. Non-DTU researchers can use it only through such a partnership. Teams that cannot accept this are pointed to self-hosting. [V, 2026-10-30] |
| How to apply, and any approval or review step | No form. Email info@carp.dk or support@carp.dk, or ask on Discord. The CAWS team creates the study, invites a test participant or turns on self sign-up, and registers a custom app for sign-in; a test server (dev.carp.dk) is used while testing. The hosted service charges a one-time study setup fee that includes a data disclosure agreement. [V, 2026-10-30] |
| Whether the program is active, paused, renamed or closed | Active. The site invites new projects; CAMS API 2.0 was released in April 2026 and the rebuilt CARP Studies app version 5 in September 2026 (iOS 5.1.0 on 2026-10-06). Core repositories were pushed in September and October 2026. [V, 2026-10-11] |
| Whether the general developer or API program is open to new applicants | Open. All components are open source (MIT) on GitHub and pub.dev with no application step. To connect a custom app to a CAWS server, whoever runs that server must register the app and issue a clientId and redirect URI. [V, 2026-10-30] |
| Participant or user limits before approval or by tier | No platform participant cap is published. One protocol serves any number of participants; with self sign-up by study code the researcher sets the maximum number of participants. Email invitations are one per person. [V, 2026-10-30] |
| How academic access differs from commercial or consumer access | The DTU-hosted service is research only; clinical treatment and commercial services are excluded. The open-source components carry no such restriction, and CARP points teams building commercial or clinical-grade products to the Flutter packages. [V, 2026-10-11] |

**Pricing**

| Fact | Value |
|---|---|
| Device or hardware list price | n/a |
| Consumer subscription or membership price | n/a |
| Research or academic pricing or discount | The hosted service follows DTU's co-financed research price model. Normally its cost is a budget line inside the joint project budget; smaller projects may pay as they go at actual cost plus 44% overhead, with staff time billed monthly, plus a monthly Computerome operations fee. Invoicing is typically yearly. Staff rates (2024, DKK per month): student assistant 16,700, research assistant 68,100, researcher 78,000, senior researcher 105,000. Self-hosting and the software are free. [V, 2026-10-11] |
| Fees for API, SDK, platform or data access | No licence or API fees: the framework, server, portal and app are MIT licensed and free to use and self-host. Fees apply only to the DTU-hosted service (see hosting_price). [V, 2026-10-11] |
| Minimum order, term or commitment | Not public [2026-10-11] |
| Whether pricing requires contacting sales | Partly. A rate table (2024 prices in DKK) is published, but the hosted service is available only through a research partnership and its cost is normally set in the joint project budget, so the actual amount is agreed per project. Self-hosting needs no contact. [V, 2026-10-11] |
| Price of managed hosting | DTU-hosted service, 2024 prices in DKK: one-time study setup 45,000, including a data disclosure agreement but not fuller data processing agreements; hosting and maintenance 1,250 per study per month; staff time per month from 16,700 (student assistant) to 105,000 (senior researcher); plus a Computerome operations fee. Pay as you go invoices actual cost plus 44% overhead. No SLA or service guarantee. [V, 2026-10-11] |

**Data access and terms**

| Fact | Value |
|---|---|
| Raw signals available to researchers, and by which route | Via CARP Mobile Sensing sampling packages (own app) or the CARP Studies app: accelerometer (with and without gravity), gyroscope, magnetometer, step events, ambient light (Android), location, activity recognition, Bluetooth and Wi-Fi scans, connectivity, microphone audio and noise, battery, screen events (Android), and on Android only call and SMS logs, installed apps and app usage; calendar; surveys and cognitive tests; Apple Health and Health Connect records. Wearables: Polar accelerometer, gyroscope, magnetometer, ECG, PPI, PPG and HR; Movesense HR, ECG and IMU; Movisens (Android); eSense; Apple Watch via the AWARE watchOS framework. The CARP Studies app collects a subset. CARP Gardener (server side) pulls Fitbit, Garmin, Withings and Dexcom cloud data, which CARP describes as for future studies. [V, 2026-10-30] |
| Derived or processed metrics available to researchers | On the phone: mobility features from location, accelerometer higher-order features over a window, OS activity recognition, noise level and light summaries. The CARP Studies app shows participants weekly cards for steps, heart rate, sleep, mobility and task progress. Server side, CAWS lets researchers deploy Python analysis scripts to a data processing pipeline, and the carp-dsp repository provides a data-science pipeline framework. No ready-made catalogue of clinical digital biomarkers is published. [V, 2026-10-30] |
| Documented sampling rates or temporal resolution | Configurable per measure in the study protocol. Defaults: accelerometer, gyroscope and magnetometer every 200 ms (5 Hz); ambient light 10 s every 5 min; app heartbeat every 15 min. Data uploads to CAWS every 10 minutes by default. Wearable sampling rates are set by the device SDKs and are not tabulated in the CARP docs. [V, 2026-10-30] |
| How far back data can be retrieved | Prospective collection from enrolment. Probes that read stored phone data (app usage, call log, calendar) look back one day on their first run by default, configurable, and later runs continue from the last run. Apple Health and Health Connect measures also read back one day on the first run by default (getHealthMeasure() sets 30 days), then continue from the last data read. Health data is read only while the app is in the foreground, and on iOS only while the phone is unlocked. [V, 2026-10-30] |
| Export, API, SDK or file routes | Hosted or self-hosted CAWS: Portal Export (JSON), the carp-cli command-line tool and its Python module, the CAWS REST API, and the carp_webservices Dart client. A custom CAMS app can store locally (SQLite or zipped JSON), send to any endpoint through its own data manager, or use Firebase (not yet on API 2.x). Transformer schemas map data to Open mHealth and FHIR. [V, 2026-10-30] |
| API rate limits | **CAWS self sign-up endpoint:** Only one limit is documented: the public self sign-up endpoint is throttled per IP address, default 20 requests per minute (configurable by the server operator). No limits are published for data upload, export or the rest of the REST API. [V, 2026-10-11] |
| Terms on retaining, storing or deleting data | DTU's study-app privacy policy keeps data as long as relevant to the study and for at least five years, and lets participants request erasure; on the phone data is kept only until upload. The CARP Studies Google Play data safety section declares that data can't be deleted and that the developer gives no way to request deletion. Self-hosted CAWS keeps export files 7 days by default. (conflict) [U, 2026-10-11] |
| Terms on using data to train AI or ML models | Not public [2026-10-11] |
| Announced shutdowns, deprecations or migrations, with dates | CAMS API level 2.0 released 2026-04-14 with a redesigned architecture and restructured packages. The CAWS legacy DataPoint upload endpoint and the old informed-consent endpoint are deprecated but still supported. The Firebase data manager has not been updated to API 2.x. The dk.cachet.carp data namespace is to change to carp.dk at an unannounced date. The CARP health plugin dropped Google Fit in version 11.0.0, but the 2026-07-14 "Three Ways" post still lists the health package as a Google Fit integration. CARP Studies app version 5 (2026-09-28) replaced the earlier app. [V, 2026-10-30] |
| Software licence of the platform's components | MIT for all main components: CARP Mobile Sensing and its packages (carp.sensing-flutter), CARP Web Services (carp-webservices-spring), the CARP web portal (carp-portal), the CARP Studies app (carp_study_app), CARP Core (carp.core-kotlin), CARP Gardener and carp-cli. Copyright Technical University of Denmark. [V, 2026-10-11] |
| Self-hosting and managed-hosting options | Three routes: (1) the DTU-hosted service on Computerome (research partner projects only, DTU as data controller, no SLA, best effort); (2) self-host CARP Web Services, the portal and the Studies app on your own Docker or Kubernetes infrastructure with PostgreSQL; (3) build a custom Flutter app with CAMS and send data to any backend. No commercial managed hosting is offered. [V, 2026-10-11] |
| App store availability on iOS and Android | CARP Studies is free on the Apple App Store as an unlisted app, reachable only by link (id 1569798025, seller Danmarks Tekniske Universitet, iPhone, iOS 15.0 or later, version 5.1.0 released 2026-10-06, first released 2025-03-21) and on Google Play (dk.cachet.carp_study_app). Version 5, rebuilt from the ground up, was announced for Android and iOS on 2026-09-28. [V, 2026-10-11] |

**Compliance and regulatory**

| Fact | Value |
|---|---|
| Whether a HIPAA Business Associate Agreement is offered | Not public [2026-10-11] |
| Whether a data processing agreement is offered | On the hosted service DTU is the controller and will not act as a data processor for another organisation. Outside partners can receive selected data under a short disclosure contract, or become DTU's data processors under a full DTU-standard data processor agreement; only aggregate anonymous data is shared otherwise. Joint controllership is possible only rarely, in large funded projects. [C, 2026-10-11] |
| Published HIPAA statement | Not public [2026-10-11] |
| Published GDPR statement | DTU is the data controller for the hosted service and processes data under the GDPR and the Danish Data Protection Act, on the legal basis of GDPR Articles 6(1)(e), 9(2)(j) and 10. DTU's data protection officer is at dpo@dtu.dk. Self-hosters are their own controller. [C, 2026-10-11] |
| ISO/IEC 27001 status and evidence | Not public [2026-10-11] |
| SOC 2 status and evidence | Not public [2026-10-11] |
| FDA clearances, from the FDA database | Not public [2026-10-11] |
| Where data is stored, and residency options | Hosted service: DTU servers at Computerome, the Danish National Life Science Supercomputing Center, in Denmark, so data stays in the EU/EEA by default. Self-hosted: wherever the institution deploys. [V, 2026-10-11] |

<!-- facts:end -->

## Key Links

- Official site: https://carp.dk/
- Three ways to use CARP: https://carp.dk/three-ways-to-use-carp/
- Hosted service terms and prices: https://carp.dk/hosting/
- CARP Web Services (CAWS): https://carp.dk/caws
- Documentation: https://docs.carp.dk/
- Privacy policy (study app): https://carp.dk/privacy-policy-app/
- CARP Studies (Google Play): https://play.google.com/store/apps/details?id=dk.cachet.carp_study_app
- CARP Studies (App Store, unlisted): https://apps.apple.com/dk/app/carp-studies/id1569798025
- CARP Mobile Sensing (CAMS): https://carp.dk/cams/
- CARP Core: https://carp.dk/core/
- GitHub organization: https://github.com/carp-dk
- Flutter package (pub.dev): https://pub.dev/packages/carp_mobile_sensing
- About: https://carp.cachet.dk/about/

## Sources

1. Copenhagen Research Platform, official site. https://carp.dk/ (accessed 2026-08-24, search summary). **Primary.** Platform family overview.
2. CARP Mobile Sensing (CAMS) page. https://carp.dk/cams/ (accessed 2026-08-24, search summary). **Primary.** Framework architecture, data-transformer/privacy-preserving-transformation features, ECG wearable integration.
3. About, CARP. https://carp.cachet.dk/about/ (accessed 2026-08-24, search summary). **Primary.** MIT licence, DTU copyright, real-world application domains (mental health, cardiovascular disease, diabetes).
4. `carp_mobile_sensing` Flutter package. https://pub.dev/packages/carp_mobile_sensing (accessed 2026-08-24, search summary). Confirms active distribution as a Flutter package.
5. Bardram J. et al. "The CARP Mobile Sensing Framework, A Cross-platform, Reactive, Programming Framework and Runtime Environment for Digital Phenotyping." arXiv. https://arxiv.org/pdf/2006.11904 (accessed 2026-08-24, search summary). Architecture paper.
6. CARP Mobile Sensing (CAMS) feature page (second-pass direct fetch). https://carp.dk/cams/ (accessed 2026-08-25). **Primary/Verified.** Full named wearable-integration list (Movisens, eSense, Polar, Movesense, Dexcom G7) and confirmed Apple Health / Google Health Connect integration; no researcher dashboard mentioned on this specific page (see source 7 for the dashboard finding).
7. `carp-dk` GitHub organization (second-pass direct fetch). https://github.com/carp-dk (accessed 2026-08-25). **Primary/Verified.** Confirms `carp-portal`, `carp-cli`, `carp-webservices-spring`, `carp.core-kotlin`, and `carp_study_app` repositories; MIT licence re-confirmed across multiple repos; 42 total repositories in the organization.
8. "The CARP Mobile Sensing Framework, Demonstration." *Companion of the 2025 ACM International Joint Conference on Pervasive and Ubiquitous Computing (UbiComp/ISWC 2025)*. https://unpaywall.org/10.1145/3714394.3754442 (accessed 2026-08-25, search summary). Evidence of continued academic engagement with the framework in 2025; author affiliations not confirmed this session.
9. `carp-dk/carp-portal` repository: README, CHANGELOG, `src/pages` tree, contributors and commit count via the GitHub API. https://github.com/carp-dk/carp-portal (accessed 2026-10-09). **Primary/Direct.**
10. CARP, "Three ways to use CARP." https://carp.dk/three-ways-to-use-carp/ (accessed 2026-10-09). **Primary/Direct.** Hosted, self-hosted and custom-app routes; portal functions.
11. CARP, "CARP Web Services (CAWS)." https://carp.dk/caws (accessed 2026-10-09). **Primary/Direct.** DTU-affiliated access wording; best-effort service terms.
12. CARP, DiaFocus project page and "Clinical Validation of DiaFocus" (2025-09-05). https://carp.dk/?p=1533 ; https://carp.dk/clinical-validation-of-diafocus/ (accessed 2026-10-09). **Primary/Direct.** DiaFocus built on CAMS and the Research Package.
13. Lind N. et al. 2025, *JMIR Diabetes*, doi 10.2196/63894 (full text via Europe PMC, PMC12377514), and Bardram J.E. et al. 2023, *ACM Trans Comput Healthcare* 4(2), doi 10.1145/3586579 (abstract via Crossref; ACM full text returned HTTP 403) (accessed 2026-10-09).
14. Niemeijer K. et al. 2023, "Combining Experience Sampling and Mobile Sensing for Digital Phenotyping With m-Path Sense," *JMIR Formative Research*, doi 10.2196/43296 (full text via Europe PMC, PMC10031448) (accessed 2026-10-09). **Verified.** m-Path Sense built by adding CAMS to m-Path.
15. Adoption pass: Europe PMC full-text search for "CARP Mobile Sensing", "carp_mobile_sensing" and "Copenhagen Research Platform"; OpenAlex citing works for the CAMS arXiv and *Sensors* papers; pub.dev dependency search; Crossref author record for doi 10.1145/3714394.3754442 (all accessed 2026-10-09).
16. `carp-dk/carp.sensing-flutter`, `carp_mobile_sensing` CHANGELOG and device sampling package source (accessed 2026-10-09). **Primary/Direct.** Client-side `heartbeat` measure.
17. CARP, "Three ways to use CARP" (posted 2026-07-14) and "CARP Web Services (CAWS)", re-read 2026-10-10. **Primary/Verified.** Hosted, self-hosted and custom-app routes; DTU controller role and EU/EEA residency; JSON export; DTU-affiliated, best-effort hosted terms; no price.
18. `carp-dk/carp-portal` package.json on the default branch and GitHub API repository metadata (accessed 2026-10-10). **Primary/Verified.** React 19, MUI 9, version 2.0.0.
19. Google Play listing `dk.cachet.carp_study_app` ("CARP Studies", offered by Copenhagen Research Platform @ DTU Health Tech, updated 2026-10-06), direct fetch 2026-10-10. **Primary/Verified.**
20. Europe PMC record for PMC12377514 (Lind et al. 2025), author affiliations (accessed 2026-10-10).
21. CARP, "Hosting" (hosted service terms, modified 2026-08-23). https://carp.dk/hosting/ (accessed 2026-10-11). **Primary/Verified.** Research-partner eligibility, research-only use, 2024 rate table, no SLA, data disclosure and processor terms, DTU as controller, GDPR legal basis.
22. CARP, "New CARP Studies app" (2026-09-28). https://carp.dk/new-carp-studies-app/ (accessed 2026-10-11). **Primary/Verified.** Version 5, Computerome storage in Denmark, collected streams, weekly cards, enrolment, CARP Gardener described as for future studies.
23. CARP Studies on the App Store (id 1569798025, DK and US storefronts, plus iTunes lookup API) and Google Play; CARP, "CARP Studies app published in the Apple App Store"; CARP, "Join". https://apps.apple.com/dk/app/carp-studies/id1569798025 ; https://carp.dk/carp-studies-app-published-in-the-apple-app-store/ ; https://carp.dk/join/ (accessed 2026-10-11). **Primary/Verified.**
24. docs.carp.dk (rebuilt October 2026): measure types, domain model, sampling configurations, health package data collection. https://docs.carp.dk/docs/mobile-sensing/measure-types ; https://docs.carp.dk/docs/mobile-sensing/domain-model ; https://docs.carp.dk/docs/mobile-sensing/building-sampling-packages/sampling-configurations ; https://docs.carp.dk/docs/sampling-packages/health/collecting-data (accessed 2026-10-30). **Primary/Verified.**
25. `carp-dk/carp.sensing-flutter`, sensors sampling package source (`sensor_package.dart`), 200 ms default interval. https://github.com/carp-dk/carp.sensing-flutter/blob/main/carp_mobile_sensing/lib/infrastructure/sampling_packages/sensors/sensor_package.dart (accessed 2026-10-11). **Primary/Verified.**
26. CARP privacy policies (study app and service); CARP Studies Google Play data safety section; `carp-webservices-spring` `application.yml` export retention default. https://carp.dk/privacy-policy-app/ ; https://carp.dk/privacy-policy-service/ ; https://play.google.com/store/apps/datasafety?id=dk.cachet.carp_study_app ; https://github.com/carp-dk/carp-webservices-spring/blob/develop/src/main/resources/config/application.yml (accessed 2026-10-11). **Primary/Verified.**
27. `carp-webservices-spring`, self sign-up documentation. https://github.com/carp-dk/carp-webservices-spring/blob/develop/docs/ws-self-signup.md (accessed 2026-10-11). **Primary/Verified.** 20 requests per minute per IP default.
28. CARP, "CARP Mobile Sensing API 2.0 released"; `carp_webservices` backend README; docs.carp.dk data managers; `carp-health-flutter` README. https://carp.dk/carp-mobile-sensing-api-2-0-released/ ; https://github.com/carp-dk/carp.sensing-flutter/blob/main/backends/carp_webservices/README.md ; https://docs.carp.dk/docs/mobile-sensing/data-managers ; https://github.com/carp-dk/carp-health-flutter (accessed 2026-10-11; data managers page 2026-10-30). **Primary/Verified.** Deprecations.
29. `carp-dk/carp_aware_package` and `carp-dk/carp-gardener` repositories. https://github.com/carp-dk/carp_aware_package ; https://github.com/carp-dk/carp-gardener (accessed 2026-10-11). **Primary/Verified.**
30. CARP, "CARP Web Services (CAWS)", and `carp-dk/carp-dsp`. https://carp.dk/caws/ ; https://github.com/carp-dk/carp-dsp (accessed 2026-10-11). **Primary/Verified.** Python analysis pipeline; data-science framework.
31. CARP, "Coverage analysis on Android 14 and iOS 18." https://carp.dk/coverage-analysis-on-android-14-and-ios-18/ (accessed 2026-10-11). **Primary/Verified.**
32. openFDA 510(k), PMA and registration searches for Technical University of Denmark and CARP, no matches (accessed 2026-10-11). https://api.fda.gov/device/510k.json?search=applicant:%22Technical+University+of+Denmark%22
33. CARP, "Funding from the Novo Nordisk Foundation." https://carp.dk/funding-from-the-novo-nordisk-foundation/ (accessed 2026-10-11). **Primary/Verified.** DKK 5 million infrastructure grant.
34. GitHub licence API for seven `carp-dk` repositories; LICENSE files in `carp.sensing-flutter`, `carp-webservices-spring` and `carp-portal` (accessed 2026-10-11). **Primary/Verified.** MIT.
35. docs.carp.dk "CARP Web Services" and "Introduction" pages (the "Go live" page cited on 2026-10-11 was removed when the docs were rebuilt). https://docs.carp.dk/docs/data-storage/caws ; https://docs.carp.dk/docs/introduction (accessed 2026-10-30). **Primary/Verified.** Account process, participant sign-up, app registration on a CAWS server.
36. Export route sources: CARP "Three ways to use CARP" and `carp-dk/carp-cli` README. https://carp.dk/three-ways-to-use-carp/ ; https://github.com/carp-dk/carp-cli (accessed 2026-10-11). **Primary/Verified.**
