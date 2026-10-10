# CARP Mobile Sensing (Copenhagen Research Platform)

## Quick Facts

| Field | Details |
|---|---|
| Organization | Technical University of Denmark (DTU); Jakob E. Bardram's group |
| Category | Open-source cross-platform mobile sensing framework for digital phenotyping |
| Current status | Active; carp.sensing-flutter pushed 2026-10-09 and carp-portal 2026-10-07 (GitHub API, checked 2026-10-10); `carp_mobile_sensing` distributed via pub.dev |
| Platforms/devices | Android and iOS (cross-platform via Flutter). DTU's reference app "CARP Studies" is on Google Play (`dk.cachet.carp_study_app`, updated 2026-10-06); no App Store listing was found on 2026-10-10 (Unclear). Teams can also build their own app on CAMS |
| Open source | Yes, MIT licence |
| Hosting/deployment | Three documented routes: the DTU-hosted CARP service on DTU Computerome (CAWS page: for DTU-affiliated researchers, best effort; "Three ways" page: email info@carp.dk for an account), a self-hosted CARP instance from the open-source components (CAWS backend, Web Portal, Studies App), or a custom app on CAMS pointed at any server (Verified 2026-10-10) |
| Pricing model | Free/open source (MIT); no price stated for the DTU-hosted service |
| Last verified | 2026-10-10 (hosting routes, data roles, JSON export, portal stack, app-store listing) |

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
| GPS / location | Yes | Yes | Unclear | Yes | Location sampling package. |
| Accelerometer | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Gyroscope | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Magnetometer | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Barometer | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Ambient light | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Proximity | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Device motion / activity recognition | Yes | Yes | Derived. Activity package. | Yes |  |
| Screen state | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| App usage | Yes | Unclear | Unclear | Yes | Apps package. |
| Battery / charging | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Network / connectivity | Yes | Yes | Unclear | Yes | Connectivity package. |
| Wi-Fi | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Bluetooth | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Calls (metadata) | Yes | No (OS) | Metadata. Communication package. | Yes |  |
| SMS (metadata) | Yes | No (OS) | Metadata. Communication package. | Yes |  |
| Keyboard | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Audio / microphone | Yes | Yes | Raw. Audio package. | Yes | Video and image packages also exist. |
| Notifications | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Device information | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |

**Verification.** Verified 2026-08-25 from carp.dk/cams, which names the sampling packages. CAMS is a Flutter library, so cross-platform support is a stated design goal, but per-stream parity was not checked and the iOS column follows OS restrictions where they are known. Sampling is configurable by construction, since the study app is written against the library.

### Notes from earlier verification passes

- **Materially expanded 2026-08-25 (second pass, Verified via direct fetch of `carp.dk/cams/`).** The wearable-integration catalog is substantially broader than the first pass's generic "ECG monitor" reference. Confirmed named integrations:

- **On-board phone sensors** (via CAMS "sampling packages"): apps, connectivity, communication, location, activity, weather, audio, video, image, survey data.
- **Health-platform integration**: **Apple Health and Google Health Connect** are named directly as supported data sources, a HealthKit/Health Connect integration that was not previously documented in this profile and is a genuine differentiator (few other platforms in this module have confirmed HealthKit/Health Connect integration).
- **Named wearable devices**: Movisens (Move4, EcgMove4, EdaMove4), the eSense earplug, Polar (H10, Verity Sense), Movesense (MD, Active), and the Dexcom G7 continuous glucose monitor, a far more itemized and diverse list than "ECG monitor," spanning cardiac, EDA, activity, audio-wearable, and continuous-glucose sensing.

- Because CAMS is Flutter-based and explicitly cross-platform, iOS/Android sensor parity is at least a stated design goal, but this session still did not independently verify parity for every individual sensor stream, and CLAUDE.md's instruction not to assume iOS/Android parity still applies even to platforms designed cross-platform from the start, since underlying OS constraints (especially iOS background execution limits) apply regardless of the app framework used.

## Derived Metrics / Analytics

- Data-transformer components support standardized-format conversion and privacy-preserving transformation as part of the core framework, per the project's own materials, implying at least some built-in processing capability beyond raw pass-through, though a Forest-comparable derived-metrics catalog was not identified.

## Active Data Collection

- Not verified in any pass to date.

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
- **Conflict on who can use the hosted instance.** The CAWS page says "Researchers affiliated with DTU can use this service", on a best-effort basis with no uptime or data-integrity guarantee unless a contract says otherwise. The "Three ways to use CARP" page invites any researcher to email info@carp.dk for an account. Both are recorded here; neither states a price.
- **Assessment.** The portal is a real, actively developed study-management dashboard covering protocols, deployments, participants, consent, data visualisation and export. It is not a configure-everything-in-the-browser product like Avicenna's. It has no versioned releases, no end-user documentation, and nothing found about adherence alerts or audit logs. It sits between "build it yourself" and a mature commercial dashboard. **Corroborated**: the page inventory is Verified from code, but feature depth was read from page names and vendor descriptions, not from running the portal.

## Data Access and Export

- Standardized data-format output and privacy-preserving transformation are named framework features.
- The CARP Web Portal lets researchers "download the collected data in JSON format" for offline analysis in R, Python or other tools (Verified 2026-10-10, "Three ways to use CARP", posted 2026-07-14). On the DTU-hosted service DTU is the data controller, and CAWS provides a Python library for writing analysis scripts that are deployed to its data-processing pipeline (CAWS page, read 2026-10-10).

## APIs, SDKs, and Extensibility

- This is CAMS's core identity and its clearest differentiator in this module: it is, by design, a programming framework/SDK rather than a configured product. Full MIT-licence source access (copyright DTU) allows unrestricted institutional modification. Real-world use spans mental health, cardiovascular disease, and diabetes mHealth applications, per the project's own "About" materials, evidence that multiple distinct research apps have been built on top of CAMS rather than it being single-study tooling.

## Deployment and Infrastructure

- **Three routes (Verified 2026-10-10, carp.dk "Three ways to use CARP", posted 2026-07-14, and the CAWS page):**
  - **DTU-hosted service:** runs "on DTU Computerome", and the managed environment "handles infrastructure, security, and data storage on your behalf"; the Web Portal lets hosted users "upload protocols, create studies, recruit participants, deploy studies, and manage ongoing studies". The CAWS page says "Researchers affiliated with DTU can use this service", on "a best-effort basis", with "No guarantees ... for system uptime or data integrity unless specified in project-specific contracts". The "Three ways" page tells researchers to email info@carp.dk to set up an account. No price is stated.
  - **Self-hosted:** "deploy your own instance of CARP using our open-source components" (CARP Web Services, the Web Portal and the Studies App).
  - **Custom app:** build a Flutter app on CAMS and the other packages.
- For the custom-app route a research team integrates the `carp_mobile_sensing` package into its own Flutter app and stands up whatever backend/storage infrastructure it needs. This requires genuine mobile-development capacity (Flutter/Dart), a different and arguably higher technical floor than configuring an existing dashboard-based platform, though lower than standing up a full backend like Beiwe's or RADAR-base's if the study doesn't need custom backend infrastructure.

## Participant Experience

- Not verified in any pass to date.

### Background keepalive (added 2026-10-09)

- CAMS has a `heartbeat` measure. It is a **client-side** data point that the phone records on a fixed interval, so researchers can check sampling coverage afterwards. The CHANGELOG says every 5 minutes; the current device sampling package sets a 15-minute default. It does not wake the app.
- No server-triggered push that reopens a stopped CAMS app was found in the CAMS, CARP Web Services or portal materials checked. Any such mechanism would sit in the app built on CAMS. m-Path Sense, which embeds CAMS, has one (see the m-Path profile).
- Status: **Corroborated** absence of a built-in server-side keepalive, from code and docs, not from a statement by DTU.

## Privacy, Security, and Compliance

- Privacy-preserving data transformation is named as a first-class framework capability (allowing e.g. on-device or pipeline-stage anonymization/aggregation before storage), which is architecturally notable, few other platforms in this module document this as a built-in framework feature rather than a per-study custom implementation. - **GDPR roles are documented (Verified 2026-10-10, "Three ways to use CARP"):** for the hosted service "DTU acts as a data controller", "DTU cannot act as a data processor" for a non-DTU controller, and data "stays within the EU/EEA by default". For self-hosting, "your institution is both data controller and data processor"; for a custom app the team carries the regulatory responsibility. No certification, HIPAA or SOC 2 claim was found.

## Pricing

- Free and open source (MIT licence); no vendor licence fee. Cost is the adopting team's own development and infrastructure effort, or, for DTU-hosted studies, whatever a project-specific arrangement with DTU sets; neither carp.dk page states a price (checked 2026-10-10). No academic program beyond the hosted service was found.

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
- MIT licence, one of the more permissive open-source licences among the platforms profiled in this module. **Re-confirmed 2026-08-25** across multiple `carp-dk` repositories (`carp_study_app`, `carp.sensing-flutter`, `carp-webservices-spring`, `carp-cli`).
- Built-in privacy-preserving data-transformation support as a first-class framework feature, not a per-study bolt-on.
- Demonstrated reuse across multiple distinct disease-domain research apps, evidencing real framework maturity rather than single-study tooling; a 2025 ACM UbiComp demonstration paper indicates continued current engagement.
- **Materially expanded 2026-08-25**: named wearable integration now spans Movisens (ECG/EDA/activity), eSense, Polar, Movesense, and the Dexcom G7 CGM, not just "ECG monitor", plus confirmed Apple Health and Google Health Connect integration, a genuine differentiator versus other platforms in this module.
- **New 2026-08-25**: a `carp-portal` repository exists, indicating a researcher-dashboard component is part of the broader CARP ecosystem, not solely the adopting team's responsibility (see Researcher and Study Management Features above for the appropriate caveats).

## Limitations

- Using CAMS for a bespoke app means building a custom Flutter app, which requires real mobile-development capacity. The DTU-hosted service with the CARP Studies app and Web Portal avoids that, but is stated for DTU-affiliated researchers, on a best-effort basis.
- ~~No researcher-facing web dashboard/study-management product was identified~~, **revised 2026-08-25**: a `carp-portal` repository exists, but its feature completeness, documentation, and production-readiness were not independently verified this session, treat as "exists, depth unconfirmed" rather than "absent."
- Full sensor-parity (iOS vs. Android, stream-by-stream) and compliance-certification detail were not independently verified this session.
- Smaller apparent ecosystem/community footprint than Beiwe, RADAR-base, or AWARE in general digital-phenotyping methods literature, GitHub signals checked this session (84 stars / 31 forks on the core Flutter sensing repo) are modest relative to the module's larger academic platforms, though this was not systematically benchmarked star-for-star.

## Best-Fit Use Cases

- Research teams with in-house Flutter/mobile-development capacity that want a proven, MIT-licensed sensing engine to build a fully custom study app on top of, rather than working within another platform's dashboard constraints.
- Studies needing genuinely first-class cross-platform (iOS/Android) sensing architecture from a single codebase.
- Studies needing wearable (e.g., ECG) integration alongside phone sensing within a unified framework.

## Poor-Fit Use Cases

- Teams without mobile-development capacity who cannot use the DTU-hosted service (stated for DTU-affiliated researchers) and need a configure-don't-code study app.
- Studies needing an existing, ready-to-use, well-documented researcher dashboard for participant/study management out of the box, `carp-portal` exists (see above) but its maturity relative to Beiwe's or Avicenna's dashboards was not established this session, so this remains a caution rather than a confirmed absence.
- Rapid-timeline pilots where standing up a custom app is not feasible before enrollment.

## Open Questions

- *(Directed to: CARP / Jakob Bardram's group, DTU, via https://carp.dk/)*

- ~~Does a companion researcher dashboard/study-management product exist?~~ **Resolved (existence) 2026-08-25**, `carp-portal` exists. ~~How feature-complete and documented is `carp-portal`?~~ Largely resolved 2026-10-09, see Researcher and Study Management Features. Still open: whether non-DTU researchers can get accounts on the hosted instance (the two carp.dk pages conflict), and at what cost.
- ~~What is the full current wearable-integration catalog beyond ECG monitors?~~ **Resolved 2026-08-25**, see Sensors and Data Streams above (Movisens, eSense, Polar, Movesense, Dexcom G7, plus Apple Health/Google Health Connect).
- ~~What GDPR/compliance documentation or guidance exists?~~ Partly answered 2026-10-10: controller and processor roles and EU/EEA residency are documented (see Privacy). No certification is claimed.
- What export formats and backend-storage patterns are typical/recommended for CAMS deployments (the portal exports JSON, Verified 2026-10-10), and does `carp-webservices-spring` represent the standard/recommended backend, or one option among several?
- ~~How many independent research groups outside DTU have built production studies on CAMS? Does the 2025 UbiComp demo include non-DTU authors?~~ Partly resolved 2026-10-09: one confirmed (KU Leuven, m-Path Sense); the demo authors are both DTU. An exhaustive count would need DTU's own list of adopters.
- ~~Is DiaFocus built on CAMS?~~ Resolved 2026-10-09: yes, per CARP's own DiaFocus pages.

## Key Links

- Official site: https://carp.dk/
- Three ways to use CARP: https://carp.dk/three-ways-to-use-carp/
- CARP Web Services (hosted service terms): https://carp.dk/caws
- CARP Studies (Google Play): https://play.google.com/store/apps/details?id=dk.cachet.carp_study_app
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
