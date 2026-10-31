# Module 2 — Sources

All sources accessed **2026-08-24** unless otherwise noted. "Retrieval" records how the source was
consulted, because it determines the confidence label a claim can carry.

**Academic literature note:** for the subset of sources below that are peer-reviewed papers,
conference papers, or preprints (as opposed to vendor docs, GitHub repos, or news/blog posts), see
**`literature-library.md`** for a dedicated index — full citation, open-access status, and a locally
stored PDF where the paper is legitimately open-access. Several entries below that were Search-summary
retrieval here (e.g. the RADAR-base JMIR Mental Health 2024 paper, RADAR-IoT, mindLAMP's JMIR mHealth
uHealth paper, AWARE's Ferreira et al. paper, m-Path's Frontiers paper, CARP's Bardram et al. arXiv
paper, and the Purple Robot systematic review) now have a Verified-status full-text PDF via that file.

- **Direct** — page fetched and read in this session (supports **Verified**)
- **Search summary** — established via search-result summarization of the named source (supports
  **Corroborated** at best)
- **Secondary** — third-party reporting about a primary source (supports **Reported**)

**Note on this module's retrieval mix**: this was a single research session (contrast Module 1's two
deep passes). A larger proportion of sources here are Search summary rather than Direct fetch —
several primary documentation sites (LAMP docs, AWARE Framework's detailed pages, individual vendor
pricing pages) either returned errors on direct fetch or were not directly fetched due to session
scope. This is recorded plainly rather than smoothed over; see each profile's own Sources section for
per-claim retrieval detail.

**Second-pass update (2026-08-24):** a follow-up session direct-fetched primary sources for AWARE
Framework, mindLAMP, MetricWire, Koa Health, and attempted Purple Robot's lab site, specifically to
close Tier 10 unresolved-questions items #87–92. New Direct-retrieval sources are marked below with
"(2nd pass)". MetricWire's own site and Purple Robot's lab site remained unreachable even on this
second, deliberate attempt (HTTP 403 and domain-wide HTTP 500 respectively) — these are now recorded
as **repeated, confirmed access barriers** rather than single-session gaps.

**Third-pass update (2026-08-25):** a follow-up session direct-fetched primary sources for the five
platforms not covered by the 2026-08-24 second pass — **Beiwe, RADAR-base, Avicenna Research (Ethica),
m-Path, and CARP Mobile Sensing** — bringing all eight profiled platforms to second-pass depth. New
Direct-retrieval sources are marked below with "(3rd pass)". Major resolutions: Beiwe Service Center's
actual rate figures (previously methodology-only); RADAR-base's managed-hosting offering (The Hyve)
and itemized Android sensor catalog; Avicenna Research's ISO 27001:2022 certification; m-Path's full
public pricing structure; CARP's expanded wearable-integration catalog and `carp-portal` dashboard
repository.

---

## Beiwe

| ID | Title | Org | URL | Type | Retrieval | Establishes |
|---|---|---|---|---|---|---|
| S-BEI-01 | Digital Phenotyping and Beiwe Research Platform | Onnela Lab, Harvard T.H. Chan SPH | https://hsph.harvard.edu/research/onnela-lab/digital-phenotyping-and-beiwe-research-platform/ | Lab page | **Direct** | Data types, iOS/Android support, architecture, BSD-3 licence, self-host vs BSC |
| S-BEI-02 | beiwe-backend README | Onnela Lab (GitHub) | https://github.com/onnela-lab/beiwe-backend | Open-source repo | **Direct** | Django/AWS architecture, encryption design, identifier hashing, BSD-3, related repos |
| S-BEI-03 | forest repository | Onnela Lab (GitHub) | https://github.com/onnela-lab/forest | Open-source repo | **Direct** | Forest's purpose and relationship to Beiwe |
| S-BEI-04 | Beiwe Service Center overview | Onnela Lab | https://hsph.harvard.edu/research/onnela-lab/beiwe-service-center/ (the beiwe.org overview URL cited on 2026-08-24 is dead as of 2026-10-10: HTTPS times out, HTTP redirects to a 404) | Service page | Search summary | BSC service scope, pricing methodology |
| S-BEI-05 | onnela-lab GitHub organization | Onnela Lab | https://github.com/onnela-lab | Org listing | Search summary | Recent commit activity used for "Active" status |
| S-BEI-06 | beiwe-backend repository structure and README (3rd pass) | Onnela Lab (GitHub) | https://github.com/onnela-lab/beiwe-backend | Open-source repo | **Direct (3rd pass)** | `data_access_api_reference` directory confirmed; precise HIPAA-applicability language quoted |
| S-BEI-07 | forest README (3rd pass) | Onnela Lab (GitHub) | https://github.com/onnela-lab/forest | Open-source repo | **Direct (3rd pass)** | Subpackage structure: `jasmine`/`willow`/`sycamore` |
| S-BEI-08 | Beiwe Service Center overview (3rd pass) | Onnela Lab | https://hsph.harvard.edu/research/onnela-lab/beiwe-service-center/ | Service page | **Direct (3rd pass)** | **Primary/Verified.** BSC rate figures: $1,937/month + $6/Active Participant Month; worked examples $24,144 to $27,564. Resolves unresolved-question #85. **Superseded (2026-10-11):** this is the FY24 card; current FY26 rates ($2,640 + $8.40) are on S-BEI-15 |
| S-BEI-09 | beiwe-backend `data_access_api_reference` directory and forest `src/forest` package listing (re-check, 2026-10-09) | Onnela Lab (GitHub API) | https://github.com/onnela-lab/beiwe-backend/tree/main/data_access_api_reference ; https://github.com/onnela-lab/forest/tree/develop/src/forest | Open-source repo | **Direct (2026-10-09)** | Directory holds `download_data.py` and `other_api_reference_script.py` (last changed 2026-03-10); Forest still ships six subpackages (bonsai, jasmine, oak, poplar, sycamore, willow); forest.beiwe.org returns HTTP 200. Confirms the 2026-09-03 answers to unresolved questions 101 and 102 |

## RADAR-base

| ID | Title | Org | URL | Type | Retrieval | Establishes |
|---|---|---|---|---|---|---|
| S-RAD-01 | About | RADAR-base | https://radar-base.org/about/ | Platform page | **Direct** | Purpose, architecture, hosting models, data sources, KCL/The Hyve maintainership, Apache 2.0 |
| S-RAD-02 | Publications | RADAR-base | https://radar-base.org/publications/ | Listing page | Search summary | Published-use record across disease domains |
| S-RAD-03 | 2026 RADAR-base Symposium announcement | RADAR-base | https://radar-base.org/2026/05/28/%F0%9F%9A%80-radar-base-symposium-2026-innovation-impact-the-future-of-mobile-health/ | Blog/news | Search summary | 2026 activity, named industry partners |
| S-RAD-04 | Digital Phenotyping of Mental and Physical Conditions: Remote Monitoring of Patients Through RADAR-Base Platform | *JMIR Mental Health* 2024 | https://mental.jmir.org/2024/1/e51259 | Peer-reviewed | Search summary | Platform-use description across clinical domains |
| S-RAD-05 | RADAR-IoT: An Open-Source, Interoperable, and Extensible IoT Gateway Framework for Health Research | PubMed | https://pubmed.ncbi.nlm.nih.gov/39066012/ | Peer-reviewed | Search summary | IoT gateway extension, open-source status |
| S-RAD-06 | Phone Data Sensors (3rd pass) | RADAR-base | https://radar-base.org/docs/4048-2/ | Docs page | **Direct (3rd pass)** | **Primary/Verified.** Itemized 17-stream Android sensor catalog; "substantial differences" + "more sparse" iOS language |
| S-RAD-07 | Passive App (pRMT App) (3rd pass) | RADAR-base | https://radar-base.org/docs/prmt-app/ | Docs page | Direct (3rd pass), limited yield | General passive-app description only |
| S-RAD-08 | RADAR-base GitHub organization (3rd pass) | RADAR-base | https://github.com/RADAR-base | Org listing | **Direct (3rd pass)** | **Primary/Verified.** Confirms `ManagementPortal`, `radar-prmt-android`, `RADAR-Questionnaire`, `RADAR-Schemas`, Kubernetes/Helm deployment repos, all Apache-2.0, active through Aug 2026 |
| S-RAD-09 | RADAR-base as a Service (3rd pass) | The Hyve | https://www.thehyve.nl/services/radar-base-as-a-service | Service page | **Direct (3rd pass)** | **Primary/Verified.** Managed-hosting offering: GDPR-compliant cloud, 2–4 week setup, ~200-participant single-server guidance, no published pricing. Resolves unresolved-question #86 |
| S-RAD-10 | "Sensors per phone type" comparison chart on the Phone Data Sensors page | RADAR-base | https://radar-base.org/wp-content/uploads/2019/09/iOS_pRMT_App_Android_Sensor_Comparison.png (embedded in https://radar-base.org/docs/4048-2/, page updated 2026-05-28) | Docs image | **Direct (2026-10-09), image read** | **Primary.** Per-stream Android vs iOS availability for the pRMT apps: most iOS streams "foreground only", significant location changes and known-peripheral connection available, app usage and call/SMS logs not available, steps read from HealthKit in the foreground. Image uploaded September 2019 |
| S-RAD-11 | `radar-prmt-ios` repository README and commit history | RADAR-base (GitHub) | https://github.com/RADAR-base/radar-prmt-ios | Open-source repo | **Direct (2026-10-09, GitHub API)** | README calls the iOS pRMT app "work in progress" that "only records location data without sending it to a server"; last commit 2021-01-19. Conflicts with the 2019 chart |
| S-RAD-12 | `RADAR-Questionnaire` (aRMT) package manifest, README and `health.ts` | RADAR-base (GitHub) | https://github.com/RADAR-base/RADAR-Questionnaire | Open-source repo | **Direct (2026-10-09, GitHub API)** | Current iOS data route: a `healthkit` questionnaire task reading 17 HealthKit types (steps, flights, distances, energy, heart rate, resting HR, SpO2, respiratory rate, sleep analysis, workouts, glucose, blood pressure, weight); Firebase messaging and local notifications |
| S-RAD-13 | `RADAR-Appserver` README and `RADAR-Backend` README / `DisconnectMonitor.java` | RADAR-base (GitHub) | https://github.com/RADAR-base/RADAR-Appserver ; https://github.com/RADAR-base/RADAR-Backend | Open-source repos | **Direct (2026-10-09, GitHub API)** | App server schedules FCM notifications and data messages for questionnaires; backend `DisconnectMonitor` emails configured researcher addresses when a source stops sending (example timeout 5 minutes). No participant-facing server keepalive push found |
| S-RAD-14 | RADAR-base GitHub repository listing (iOS-relevant repos) | RADAR-base (GitHub) | https://github.com/RADAR-base?q=ios | Org listing | **Direct (2026-10-09, GitHub API)** | `radar-sensorkit-cordova` (Apple SensorKit plugin for the aRMT app, last push 2024-11); `radar-base-app` (new React Native app kit, active October 2026) |

## mindLAMP

| ID | Title | Org | URL | Type | Retrieval | Establishes |
|---|---|---|---|---|---|---|
| S-LAMP-01 | BIDMCDigitalPsychiatry GitHub organization | BIDMC Division of Digital Psychiatry | https://github.com/BIDMCDigitalPsychiatry | Org listing | **Direct** | Repository inventory incl. "[Deprecated]" labels on `LAMP-portal`/`LAMP-app`; current `LAMP-server` |
| S-LAMP-02 | Digital Psych — mindLAMP | Digital Psych (Torous lab) | https://www.digitalpsych.org/mindlamp1.html | Lab page | Search summary | Platform framing, research/clinical dual orientation |
| S-LAMP-03 | Enabling Research and Clinical Use of Patient-Generated Health Data (the mindLAMP Platform): Digital Phenotyping Study | Vaidyam, Halamka, Torous — *JMIR mHealth uHealth* 2022 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8783287/ | Peer-reviewed | Search summary | Platform-description paper |
| S-LAMP-04 | mindLAMP publications | docs.lamp.digital | https://docs.lamp.digital/about/publications/ (dead link, 404, checked 2026-10-10; publications page removed, docs root https://docs.lamp.digital/ returns 200) | Docs site | **Attempted, HTTP 404 (both passes)** | Not retrieved — confirmed documentation-access gap |
| S-LAMP-05 | LAMP-portal repository | BIDMCDigitalPsychiatry (GitHub) | https://github.com/BIDMCDigitalPsychiatry/LAMP-portal | Repo | **Direct (2nd pass)** | Archived by owner 2020-11-17, read-only |
| S-LAMP-06 | LAMP-app repository | BIDMCDigitalPsychiatry (GitHub) | https://github.com/BIDMCDigitalPsychiatry/LAMP-app | Repo | **Direct (2nd pass)** | Archived by owner 2020-11-17, read-only |
| S-LAMP-07 | BIDMCDigitalPsychiatry current repository listing | BIDMC Division of Digital Psychiatry (GitHub) | https://github.com/BIDMCDigitalPsychiatry?tab=repositories | Org listing | **Direct (2nd pass)** | Current successor repos (`LAMP-dashboard`, `LAMP-server`, `LAMP-core-android`, `LAMP-core-ios`, `LAMP-activities`, `LAMP-app-gateway`, `LAMP-js`/`LAMP-py` BSD-3-Clause, `LAMP-toolkit` MIT) |
| S-LAMP-08 | docs.lamp.digital landing page | BIDMC Division of Digital Psychiatry | https://docs.lamp.digital/ | Docs site | **Direct (2nd pass), landing content only** | Passive-sensor list, "flexible hosting" framing, `/api` nav reference |
| S-LAMP-09 | `LAMP-app-gateway` README and `LAMP-kotlin` notification channels | BIDMC Division of Digital Psychiatry (GitHub) | https://github.com/BIDMCDigitalPsychiatry/LAMP-app-gateway ; https://github.com/BIDMCDigitalPsychiatry/LAMP-kotlin | Open-source repos | **Direct (2026-10-09, GitHub API)** | Gateway sends APNs/FCM push, email and SMS; no keepalive or heartbeat mechanism found in code search of the organization (search for "heartbeat" returned nothing) |
| S-LAMP-10 | mindLAMP community forum threads on notifications and battery | LAMP Consortium | https://mindlamp.discourse.group/ (dead link: host no longer resolves, checked 2026-10-10) | Forum | Search summary (2026-10-09) | Onboarding advice to set "Always Allow" and avoid low power mode; no server-triggered keepalive described |

## AWARE Framework

| ID | Title | Org | URL | Type | Retrieval | Establishes |
|---|---|---|---|---|---|---|
| S-AWR-01 | AWARE Framework official site | AWARE Framework | https://awareframework.com/ | Project site | **Direct (both passes)** | Platform framing, Android-primary/iOS-port distinction, app-store distribution constraint, Configurator/RAPIDS references |
| S-AWR-02 | AWARE Framework GitHub organization | AWARE Framework | https://github.com/awareframework | Org listing | **Direct (2nd pass)** | 97-repo inventory, Apache-2.0 licence confirmed on `aware-client` and named plugin repos, commit activity through Aug 2026 |
| S-AWR-03 | AWARE Framework — Open Collective | AWARE Framework | https://opencollective.com/aware-framework | Funding page | Search summary | Community-funding model |
| S-AWR-04 | AWARE: Mobile Context Instrumentation Framework | Ferreira et al. | https://www.researchgate.net/publication/275349654_AWARE_Mobile_Context_Instrumentation_Framework | Foundational paper | Search summary | Historical/architectural origin |
| S-AWR-05 | AWARE Sensors documentation | AWARE Framework | https://awareframework.com/sensors/ | Docs page | **Direct (2nd pass)** | **Primary/Verified.** Full per-sensor Android-vs-iOS availability table (~33 modules); resolves unresolved-question #88 |
| S-AWR-06 | Continuous Silent Push Notification (SPN) on AWARE iOS | AWARE Framework | https://www.awareframework.com/continuous-silent-push-notification-spn-on-aware-ios/ | Tutorial | **Direct (2026-10-09)** | **Primary/Verified.** iOS server-sent silent push to check sensors and request reopening; off by default (`status_push_notification` false, server field blank); App Store build needs a server URL from the developers, custom builds host the Node.js `aware-push` server. Posted 2020-02-14, updated 2025-02-06 |
| S-AWR-07 | aware-push | Yuuki Nishiyama (GitHub) | https://github.com/tetujin/aware-push | Open-source repo | Search summary (2026-10-09) | Node.js APNs relay for AWARE-iOS silent push commands |

## Avicenna Research (Ethica)

| ID | Title | Org | URL | Type | Retrieval | Establishes |
|---|---|---|---|---|---|---|
| S-AVI-01 | Avicenna Research official site | Avicenna Research | https://avicennaresearch.com/ | Vendor site | Search summary | Current company identity, rebrand from Ethica Data |
| S-AVI-02 | Avicenna Research (Ethica Data) product docs | Avicenna Research | https://avicennaresearch.dev/ | Vendor docs | Search summary | Named feature areas |
| S-AVI-03 | Data Access & Analytics | Avicenna Research | https://avicennaresearch.dev/features/data-access-and-analytics/ | Vendor docs | Search summary | Export formats (CSV, JSON, GEXF, KML), latency claim |
| S-AVI-04 | App Store listing — Avicenna (Ethica) | Apple | https://apps.apple.com/us/app/ethica-avicenna/id1137173052 | App listing | Search summary | Naming continuity |
| S-AVI-05 | Google Play listing — Avicenna Research | Google | https://play.google.com/store/apps/details?id=com.ethica.logger | App listing | Search summary | Package name continuity (`com.ethica.logger`) |
| S-AVI-06 | Ethica/iEpi academic project page | Univ. of Saskatchewan | https://www.cs.usask.ca/~osgood/iEpi/iEpi.html | Academic page | Search summary | Academic origin as epidemiological sensing/EMA system |
| S-AVI-07 | Avicenna Research company profile | CB Insights | https://www.cbinsights.com/company/ethica-data | Directory | Search summary | Corroborates Ethica-to-Avicenna continuity |
| S-AVI-08 | Third-party pricing/trial listings | Capterra, SoftwareAdvice, SoftwareWorld | various | Directory | Search summary | Free-trial characterization — **Reported, not vendor-verified** |
| S-AVI-09 | Avicenna Research homepage (3rd pass re-fetch) | Avicenna Research | https://avicennaresearch.com/ | Vendor site | **Direct (3rd pass)** | Re-confirms no public pricing, no developer API, no self-hosting |
| S-AVI-10 | Avicenna Research: Legal Documents (3rd pass) | Avicenna Research | https://avicennaresearch.com/legal/ | Legal page | **Direct (3rd pass)** | **Primary/Verified.** ISO 27001:2022 certification (Nov 2024, zero nonconformities; surveillance audit Nov 2025, zero nonconformities), AES-256 at rest, HIPAA/UK GDPR/EU GDPR/PIPEDA language for minors' data. Resolves majority of unresolved-question #84 for this platform. **Superseded (2026-10-21):** the ISO statement is a vendor self-claim (Corroborated), not an audited certificate; no certificate, number or certification body is published (`../facts/avicenna.yaml` iso27001) |
| S-AVI-11 | Data Access & Analytics (3rd pass re-fetch) | Avicenna Research | https://avicennaresearch.dev/features/data-access-and-analytics/ | Vendor docs | **Direct (3rd pass)** | Re-confirms export formats; no developer API found |
| S-AVI-12 | Participation (reference) | Avicenna Research forum/docs | https://forum.avicennaresearch.com/t/participation/1280 (redirected from learn.avicennaresearch.com) | Docs page | **Direct (2026-10-09)** | "In Operation" percentage, Last Recorded Data Time, Reload Devices message to devices; no automatic participant notification when the app stops. Dated 2025-06-16 |
| S-AVI-13 | Notifications (reference) | Avicenna Research | https://learn.avicennaresearch.com/reference/study-setup-and-deployment/notifications | Docs page | Search summary (2026-10-09); **Direct (2026-10-10)** via https://forum.avicennaresearch.com/t/notifications/1277 | Notification triggers: participation (invited, joined), activity-session (released, completed, canceled, expired), appointment (scheduled, started, canceled), and "Sensor Data Gap Detected", checked every 15 minutes and limited to the Garmin Health SDK wrist-status stream. Corrected 2026-10-10; the 2026-10-09 summary omitted the last two types |

## MetricWire

| ID | Title | Org | URL | Type | Retrieval | Establishes |
|---|---|---|---|---|---|---|
| S-MW-01 | MetricWire platform characterization | MetricWire (via search aggregation) | https://metricwire.com/ | Vendor site | **Search-summary only — direct fetch blocked HTTP 403 in both passes (homepage, /pricing, /site-licence/, /contact-us/)** | Platform features (consent, diaries, passive sensing, trigger-based surveys, dashboards) |
| S-MW-02 | MetricWire company profile | PitchBook | https://pitchbook.com/profiles/company/89864-11 | Directory | Search summary | Founding year (2013), HQ |
| S-MW-03 | Third-party software directories | Capterra, SoftwareWorld, SoftwareSuggest, TechnologyCounter, SourceForge, Visualping | various | Directory | Search summary | Trial/demo availability; no pricing figures found (both passes) |
| S-MW-04 | EMA study figure referencing MetricWire | ResearchGate | https://www.researchgate.net/figure/Select-screenshots-from-the-EMA-study-smartphone-platform-MetricWire-EMA-ecological_fig2_354098947 | Peer-reviewed (figure) | Search summary | Evidence of research use |
| S-MW-05 | MetricWire GitHub organization | MetricWire | https://github.com/MetricWire | Org listing | **Direct (2nd pass)** | **Primary/Verified.** Exactly one public repo (unrelated forked ADR template); no public SDK/API client — corroborates closed-source characterization |
| S-MW-06 | m2c2kit integration guide — MetricWire | m2c2-project (GitHub) | https://github.com/m2c2-project/m2c2kit-integration-guides/blob/main/docs/metricwire.md | Integration guide | Search summary (2nd pass) | URL-based identifier-injection integration pattern with MetricWire |
| S-MW-07 | `zeolite`, unofficial Python client for MetricWire's "Catalyst" system | Univ. of Wisconsin-Madison Center for Healthy Minds (GitHub) | https://github.com/uwmadison-chm/zeolite | Repo | Search summary (2nd pass) | Evidence an internal/partner API ("Catalyst") exists, though no official public API docs located. **Superseded (2026-10-21):** zeolite is built on MetricWire's published Consumer API spec (S-MW-12) |
| S-MW-08 | Missing Alerts Troubleshooting | MetricWire knowledge base (Atlassian) | https://metricwire.atlassian.net/wiki/spaces/mwknowledgebase/pages/6750210/Missing+Alerts+Troubleshooting (dead link, 404, checked 2026-10-10; the current MetricWire help centre should be cited instead once located) | Help page | Search summary (2026-10-09) | Force-quit stops prompts until reopen; iOS 64-notification cap; periodic background refresh added in app 2.2.3/2.2.4, which participants can switch off. No server-triggered keepalive described |

## m-Path

| ID | Title | Org | URL | Type | Retrieval | Establishes |
|---|---|---|---|---|---|---|
| S-MP-01 | m-Path official site | m-Path | https://m-path.io/ | Vendor site | Search summary | Platform framing, m-Path sense, JITAI/EMI support |
| S-MP-02 | m-Path: an easy-to-use and highly tailorable platform for ecological momentary assessment and intervention in behavioral research and clinical practice | *Frontiers in Digital Health* 2023 | https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2023.1182175/full ; PMC: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10619650/ | Peer-reviewed | Search summary | Platform-description methods paper |
| S-MP-03 | m-Path: Research page | m-Path | https://m-path.io/landing/research/ | Vendor page | Search summary | "250+ Universities" claim, Reported. **Superseded (2026-10-21):** the page now says "Institutions 150+" (`../facts/m-path.yaml` research_program) |
| S-MP-04 | m-Path homepage (3rd pass) | m-Path | https://m-path.io/ | Vendor site | **Direct (3rd pass)** | "Compliant with GDPR and HIPAA" (vendor self-declared — Corroborated, not audited) |
| S-MP-05 | m-Path — Pricing (3rd pass) | m-Path | http://m-path.io/pricing/ | Pricing page | **Direct (3rd pass)** | **Primary/Verified.** Full tier structure (Free/Essential/Standard/Comfort) and add-on pricing. Resolves unresolved-question #93's pricing component |
| S-MP-06 | m-Path manual — "Welcome to m-Path" (3rd pass) | m-Path | https://m-path.io/manual/knowledge-base/welcome-to-m-path/ | Docs page | Direct (3rd pass), limited yield | No sensor-level or API detail on this specific page |
| S-MP-07 | Mobile Sensing (full) | m-Path manual | https://m-path.io/manual/knowledge-base/mobile-sensing-full/ | Docs page | **Direct (2026-10-09)** | **Primary/Verified.** App contacts m-Path servers every 5 minutes; after a researcher-set "Remind after app is closed (in minutes)" period of silence the server sends a reopen reminder (example 30, 120, 360). Page updated 2026-10-05 |
| S-MP-08 | Live Activity background sensing | m-Path manual | https://m-path.io/manual/knowledge-base/live-activity-background-sensing/ | Docs page | **Direct (2026-10-09)** | iOS 26+ Live Activity to keep sensing alive in the background; switched on by the participant. Updated 2026-08-03 |
| S-MP-09 | Combining Experience Sampling and Mobile Sensing for Digital Phenotyping With m-Path Sense: Performance Study | Niemeijer et al., *JMIR Formative Research* 2023 (PMC10031448) | https://doi.org/10.2196/43296 | Peer-reviewed | **Direct full text (Europe PMC, 2026-10-09)** | m-Path Sense is m-Path plus CARP Mobile Sensing as a plug-in; a 5-minute alive signal with server notification was "currently being implemented" in 2023 |

## CARP Mobile Sensing

| ID | Title | Org | URL | Type | Retrieval | Establishes |
|---|---|---|---|---|---|---|
| S-CARP-01 | Copenhagen Research Platform | DTU | https://carp.dk/ | Project site | Search summary | Platform family overview |
| S-CARP-02 | CARP Mobile Sensing (CAMS) | DTU | https://carp.dk/cams/ | Project page | Search summary | Framework architecture, data-transformer features, ECG integration |
| S-CARP-03 | About — CARP | DTU | https://carp.cachet.dk/about/ | Project page | Search summary | MIT licence, DTU copyright, application domains |
| S-CARP-04 | carp_mobile_sensing Flutter package | DTU (pub.dev) | https://pub.dev/packages/carp_mobile_sensing | Package registry | Search summary | Active distribution confirmation |
| S-CARP-05 | The CARP Mobile Sensing Framework — A Cross-platform, Reactive, Programming Framework and Runtime Environment for Digital Phenotyping | Bardram et al. | https://arxiv.org/pdf/2006.11904 | Peer-reviewed / preprint | Search summary | Architecture paper |
| S-CARP-06 | CAMS feature page (3rd pass) | DTU | https://carp.dk/cams/ | Project page | **Direct (3rd pass)** | **Primary/Verified.** Named wearable catalog (Movisens, eSense, Polar, Movesense, Dexcom G7); Apple Health/Google Health Connect integration confirmed |
| S-CARP-07 | `carp-dk` GitHub organization (3rd pass) | DTU (Bardram group) | https://github.com/carp-dk | Org listing | **Direct (3rd pass)** | **Primary/Verified.** Confirms `carp-portal`, `carp-cli`, `carp-webservices-spring`, `carp.core-kotlin`, `carp_study_app`; MIT re-confirmed; 42 total repos |
| S-CARP-08 | "The CARP Mobile Sensing Framework — Demonstration" | UbiComp/ISWC 2025 Companion | https://unpaywall.org/10.1145/3714394.3754442 | Peer-reviewed (demo paper) | Search summary (3rd pass) | Evidence of continued 2025 academic engagement; author affiliations not confirmed |
| S-CARP-09 | `carp-portal` repository (README, CHANGELOG, `src/pages` tree, contributors, commits) | DTU (GitHub API) | https://github.com/carp-dk/carp-portal | Open-source repo | **Direct (2026-10-09)** | React 19 / MUI 9 web app (package.json, corrected 2026-10-10 from "React 18"), MIT, created 2024-06-20, about 230 commits, last push 2026-10-07, four contributors, no tagged releases, CHANGELOG "2.0.0 [TBD]". Needs the CARP Web Services backend plus Keycloak; deployed as a Docker image. Page set listed in the CARP profile |
| S-CARP-10 | Three ways to use CARP | DTU | https://carp.dk/three-ways-to-use-carp/ | Project page | **Direct (2026-10-09)** | **Superseded in part (2026-10-21):** the hosting terms and 2024 rates are on carp.dk/hosting/ (S-CARP-18). Hosted service on DTU Computerome (contact info@carp.dk, no price stated), self-hosting of web services + portal + Studies app (Docker or Kubernetes, PostgreSQL), or custom Flutter app on CAMS. Portal uploads JSON protocols, creates and deploys studies, recruits participants, downloads JSON data |
| S-CARP-11 | CARP Web Services (CAWS) | DTU | https://carp.dk/caws | Project page | **Direct (2026-10-09)** | DTU-hosted instance "Researchers affiliated with DTU can use", best-effort with no uptime guarantee; narrower wording of the partner rule on carp.dk/hosting/ (S-CARP-18), not a conflict (corrected 2026-10-21) |
| S-CARP-12 | DiaFocus project page and "Clinical Validation of DiaFocus" post | DTU (carp.dk) | https://carp.dk/?p=1533 ; https://carp.dk/clinical-validation-of-diafocus/ | Project pages | **Direct (2026-10-09)** | **Primary.** DiaFocus "makes use of most CARP components"; "built using several CARP components, including CARP Mobile Sensing and the Research Package", backed by CARP Web Services on DTU Computerome. Post dated 2025-09-05 |
| S-CARP-13 | DiaFocus pilot (Lind et al. 2025, *JMIR Diabetes*, PMC12377514) and design paper (Bardram et al. 2023, *ACM Trans Comput Healthcare* 4(2), doi 10.1145/3586579) | Steno Diabetes Center Copenhagen / DTU | https://doi.org/10.2196/63894 ; https://doi.org/10.1145/3586579 | Peer-reviewed | Pilot: **Direct full text (Europe PMC, 2026-10-09)**; design paper: abstract via Crossref, full text HTTP 403 | Pilot never names CARP; design paper abstract says DiaFocus "is built using a generic data collection framework for mobile and wearable sensing" without naming it |
| S-CARP-14 | Literature and citation pass for CAMS adoption | Europe PMC full-text search; OpenAlex citing-works API; pub.dev dependency search | https://europepmc.org/search?query=%22CARP%20Mobile%20Sensing%22 ; https://api.openalex.org/works?filter=cites:W3036631247 ; https://pub.dev/packages?q=dependency%3Acarp_mobile_sensing | Bibliographic databases | **Direct (2026-10-09)** | 4 Europe PMC full-text hits for "CARP Mobile Sensing"; only the m-Path Sense paper (KU Leuven) has no DTU author. CAMS arXiv paper cited 3 times, Sensors 2022 paper 4 times (OpenAlex). All 16 pub.dev dependents are CARP's own packages. 2025 UbiComp demo authors both DTU (Crossref) |
| S-CARP-15 | `carp_mobile_sensing` CHANGELOG and device sampling package | DTU (GitHub) | https://github.com/carp-dk/carp.sensing-flutter | Open-source repo | **Direct (2026-10-09, GitHub API)** | `heartbeat` measure: a client-side periodic data point (default 15-minute interval in the device package; CHANGELOG says every 5 minutes) for retrospective coverage checks, not a server-triggered wake |

## Legacy and adjacent platforms

| ID | Title | Org | URL | Type | Retrieval | Establishes |
|---|---|---|---|---|---|---|
| S-LEG-01 | Sensing Apps and Public Data Sets for Digital Phenotyping of Mental Health: Systematic Review | PMC | https://pmc.ncbi.nlm.nih.gov/articles/PMC8895287/ | Peer-reviewed | Search summary | Purple Robot Android-only coverage claim; platform-comparison context |
| S-LEG-02 | Purple Robot Android Apps | Precision Health Informatics Data Lab, King's College London (NIHR Maudsley BRC) | https://phidatalab.org/software__trashed/purple-robot-android-apps/ (dead link, 404 since 2026-10-09; use https://github.com/cbitstech/Purple-Robot) | Lab page | **Direct in 1st pass; 2nd-pass re-attempt (this page + `/software/` + domain root) returned HTTP 500 across the whole domain** | Page existed in 1st pass; URL slug still an unconfirmed retirement signal; 2nd pass adds a domain-wide server-error signal, itself inconclusive. **Corrected 2026-10-22:** this was KCL's page on its own Purple Robot "Passive Sleep Monitor" configuration (Wayback 2021-02-25: https://web.archive.org/web/20210225233643/https://phidatalab.org/software__trashed/purple-robot-android-apps/), not a CBITS page, so its slug and outages are not retirement signals |
| S-LEG-03 | studentlife R package | Zenodo | https://zenodo.org/records/3371922 | Data package | Search summary | Continuing secondary use of the StudentLife dataset |
| S-LEG-04 | Koa Health — Research | Koa Health | https://www.koahealth.com/research ; https://koahealth.com/legal/complete-research-papers/ | Company page | Search summary (1st pass); **Direct (2nd pass)** for the `/research` URL | **Primary/Corroborated (2nd pass).** Confirms internal-only digital-phenotyping framing; page contains no platform-availability, SDK, or API language for outside teams |
| S-LEG-05 | `cbitstech/Purple-Robot` repository and organization search | Northwestern CBITS (GitHub API) | https://github.com/cbitstech/Purple-Robot | Open-source repo | **Direct (2026-10-09)** | Last commit 2016-04-11 ("Dependency updates and cleanups"), last push 2017-04-07, 43 open issues on 2026-10-22 (count includes PRs), not archived; README build targets Android 5.1 (API 22) and Gradle 2.2.1. Companion repos `Purple-Robot-Django` (last commit 2016-12-27; audaciouscode fork 2020-06-22) and `PurpleRobotClient` (archived). Development continued in audaciouscode/Purple-Robot-Android to 2019-01-30 (v3.0.13, API 28); maintainer declared the app archived 2023-12-20 (issue 282) |
| S-LEG-06 | Precision Health Informatics Data Lab site (re-check) | King's College London | https://phidatalab.org/ | Lab site | **Direct (2026-10-09)** | Site back up (root HTTP 200), but the Purple Robot page and `/software/` return HTTP 404 and a site search for "purple robot" returns "Nothing found". Not a CBITS site, so not evidence about Purple Robot (corrected 2026-10-22) |

---

## Evidation (added 2026-09-03)

| ID | Title | Org | URL | Type | Retrieval | Establishes |
|---|---|---|---|---|---|---|
| S-EV-01 | Evidation home page | Evidation Health | https://evidation.com/ | Vendor site | Direct | Member, study and publication counts; cohort list; 2026 leadership news. Reported |
| S-EV-02 | Evidation research page | Evidation Health | https://evidation.com/research | Vendor page | Direct | Case-study framing, wearable near real-time measures. Reported |
| S-EV-03 | How Evidation works | Evidation Health | https://evidation.com/how-it-works | Vendor page | Direct | Connected apps (Fitbit, Apple Health, 20 or more), points, programmes. Reported. **Superseded (2026-10-21):** the help centre lists 12 connected apps (S-EV-13) |
| S-EV-04 | About Evidation | Evidation Health | https://evidation.com/about | Vendor page | Direct | Founded 2012; Heartline, BUMP and American Life in Realtime descriptions; counts that conflict with S-EV-01 |
| S-EV-05 | Evidation privacy notice | Evidation Health | https://evidation.com/privacy | Privacy notice | Direct | Data categories, sharing, CCPA opt-out; app notice is separate and not fetched |
| S-EV-06 | Goodday et al. 2024, six-cohort engagement | *JMIR* | https://doi.org/10.2196/57827 | Peer-reviewed | Direct, PDF stored | Median retention 77.2 percent; device-level adherence. Verified |
| S-EV-07 | Cho et al. 2025, adherence and retention factors | *Lancet Digit Health* | https://doi.org/10.1016/s2589-7500(24)00219-x | Peer-reviewed | Direct, XML stored | 89,479 participants, 2,080,992 daily surveys. Verified |
| S-EV-08 | Harry et al. 2025, BUMP recruitment | *JMIR Form Res* | https://doi.org/10.2196/68093 | Peer-reviewed | Direct, PDF stored | 524 women; channel-level enrolment and retention. Verified |
| S-EV-09 | Angrisani et al. 2025, American Life in Realtime | *PNAS Nexus* | https://doi.org/10.1093/pnasnexus/pgaf295 | Peer-reviewed | Direct, PDF stored | Probability sampling, provisioned Fitbit Inspire 2. Verified |


## Sources added 2026-10-10 (independent-review corrections)

All accessed 2026-10-10. "Direct" means fetched and read in this session; vendor statements about the vendor's own certifications stay Corroborated at most unless a certificate or registry entry was read.

| ID | Title | Org | URL | Type | Retrieval | Establishes |
|---|---|---|---|---|---|---|
| S-BEI-11 | Beiwe Service Center rate page (re-read) | Harvard Chan / Onnela Lab | https://hsph.harvard.edu/research/onnela-lab/beiwe-service-center/ | Service page | **Direct** | $1,937/month fixed + $6 per Active Participant Month; "FY24 Example Pricing" ($24,144; $25,044; for-profit $27,564, which does not reproduce from the formula); 30-day notice; not a scientific collaboration; interest form. Verified. **Superseded (2026-10-11):** the page's own label is FY24; the current FY26 card is S-BEI-15 |
| S-BEI-12 | Beiwe research-resource page | Harvard Chan | https://hsph.harvard.edu/research-resource/beiwe/ | Service page | **Direct** | US (studies.beiwe.org) and EU (eu.beiwe.org) BSC login portals; AWS-backed; no storage location stated. Verified |
| S-BEI-13 | Beiwe2 App Store listing; Google Play probe; beiwe-android build flavours | Onnela Lab LLC; GitHub | https://apps.apple.com/us/app/beiwe2/id1312962738 ; https://github.com/onnela-lab/beiwe-android/blob/master/app/build.gradle | App store; repo | **Direct** | iOS v2.5.11 (2026-09-30); `org.beiwe.app` not found on Google Play (Unclear) |
| S-BEI-14 | beiwe-backend issue #391; survey_push_notifications.py; beiwe-ios #13, #30, #59; beiwe-android #8, #21, #27; repo metadata | Onnela Lab (GitHub API) | https://github.com/onnela-lab/beiwe-backend/issues/391 | Issue tracker; code | **Direct** | Heartbeat on by default once servers are updated; iOS alert vs Android data pushes; notification-reliability history; pushes to 2026-10-07. Reported (developer tracker) |
| S-RAD-15 | RADAR-base as a Service (re-read) | The Hyve | https://www.thehyve.nl/services/radar-base-as-a-service | Vendor page | **Direct** | Client owns data; DPA conditions; single server; ~200 participants ideal; small-scale, short-term fit; no price. Verified |
| S-RAD-16 | RADAR passive RMT and RADAR active RMT store listings | The Hyve; Onsentia | https://play.google.com/store/apps/details?id=org.radarcns.detail ; https://play.google.com/store/apps/details?id=org.phidatalab.radar_armt ; https://apps.apple.com/us/app/radar-active-rmt/id1483953055 | App store | **Direct** | Android pRMT (2026-06-18); aRMT Android (2026-09-09) and iOS (2026-08-24); no iOS passive app |
| S-RAD-17 | RADAR-Kubernetes README; GitHub API for ManagementPortal, radar-prmt-android, radar-prmt-ios | RADAR-base (GitHub) | https://github.com/RADAR-base/RADAR-Kubernetes | Repo | **Direct** | Cluster install route "used in few production environments"; repository activity |
| S-LAMP-11 | mindLAMP Core services | BIDMC | https://research.bidmc.org/mindlamp/services | Service page | **Direct** | Three deployment models (partner AWS, separate BIDMC instance, shared lamp.digital); five phases; business agreement after Phase 1. Verified |
| S-LAMP-12 | Get started | mindLAMP docs | https://docs.lamp.digital/get-started | Docs page | **Direct** | Interest form, free consultation, tailored proposal with scope, deployment option and pricing. Verified |
| S-LAMP-13 | mindLAMP Core | Division of Digital Psychiatry, BIDMC | https://www.digitalpsych.org/mindlamp-core | Lab page | **Direct** | "supported deployment pathway"; good-fit users; 50+ active sites (vendor claim) |
| S-LAMP-14 | Repository licences and activity; mindLAMP 2 store listings; privacy page | BIDMC (GitHub API); app stores; digitalpsych.org | https://api.github.com/repos/BIDMCDigitalPsychiatry/LAMP-server ; https://play.google.com/store/apps/details?id=digital.lamp.mindlamp ; https://apps.apple.com/us/app/mindlamp-2/id1495947054 ; https://www.digitalpsych.org/privacy.html | Repo; app store; lab page | **Direct** | Server and apps unlicensed, dashboard AGPL-3.0, all pushed 2026-10-08; Android app 2026-05-17, iOS app 2023-05-26; no compliance claims on the privacy page |
| S-AWR-08 | AWARE sensors catalogue (icons parsed from HTML) | AWARE Framework | https://awareframework.com/sensors/ | Docs page | **Direct** | 33 modules; 19 iOS-marked, 14 Android only (corrects the 2026-08-24 reading). Verified |
| S-AWR-09 | AWARE Client V3 and V2 (App Store) | Yuuki Nishiyama | https://apps.apple.com/us/app/aware-client-v3/id6781949744 ; https://apps.apple.com/us/app/aware-client-v2/id1455986181 | App store | **Direct** | iOS client on the App Store (V3 v1.7.0, 2026-07-23). Verified |
| S-AWR-10 | aware-client and AWAREFramework-iOS repositories; AWARE homepage "How to get AWARE" | AWARE (GitHub API); awareframework.com | https://github.com/awareframework/aware-client ; https://github.com/tetujin/AWAREFramework-iOS ; https://awareframework.com/ | Repo; site | **Direct** | Apache-2.0; pushes 2026-08-07 and 2026-02-17; Fitbit module in the iOS framework; Android client not on Google Play |
| S-AVI-14 | Frequently Asked Questions (trial terms) | Avicenna Research | https://forum.avicennaresearch.com/t/5 | Vendor forum | **Direct** | Free test-only trial, data wiped monthly, study deleted after one year. Verified |
| S-AVI-15 | Security and Compliance | Avicenna Research | https://forum.avicennaresearch.com/t/security-and-compliance/1267 | Vendor forum | **Direct** | ISO 27001:2022 "through UKAS" with a UKAS CertCheck link that sits behind a CAPTCHA and was not read; GDPR processor; servers in Canada. Corroborated (vendor-stated) |
| S-AVI-16 | Legal Documents (re-read) | Avicenna Research | https://avicennaresearch.com/legal/ | Legal page | **Direct** | ISO wording with no certification body or certificate number; no SOC 2 or Part 11. Corroborated (vendor-stated) |
| S-AVI-17 | Export Data with API (roadmap topic) | Avicenna Research | https://forum.avicennaresearch.com/t/1406 | Vendor forum | **Direct** | Export API filed under "To Do". Verified. **Superseded (2026-10-21):** a Data Export API is documented in a 2026-02-09 how-to article (S-AVI-19); the card likely refers to a fuller API |
| S-AVI-18 | App Store and Google Play listings | Avicenna Research Inc. | https://apps.apple.com/us/app/ethica-avicenna/id1137173052 ; https://play.google.com/store/apps/details?id=com.ethica.logger | App store | **Direct** | iOS v1065 (2026-10-07); Android updated 2026-09-05 |
| S-MW-09 | Data Privacy & Security Summary | MetricWire | https://metricwire.com/data-privacy-security-summary/ | Vendor page | **Direct** (site no longer 403) | US storage on Google Cloud Platform, AES-256, TLS 1.2+, MFA, "ISO 27001 certified and SOC II Type II compliant"; no certificate linked. Corroborated (vendor-stated) |
| S-MW-10 | Academic Site Licence | MetricWire | https://metricwire.com/site-licence/ | Vendor page | **Direct** | Institution-level academic licence, unpriced; Part 11, HIPAA and GDPR compliance claimed; page copyright 2023 |
| S-MW-11 | MetricWire homepage; Catalyst By MetricWire store listings; PubMed search | MetricWire; app stores; NCBI | https://metricwire.com/ ; https://apps.apple.com/us/app/catalyst-by-metricwire/id1585123028 ; https://play.google.com/store/apps/details?id=com.metricwire.digitalhealth | Vendor page; app store | **Direct** | Demo by request, no trial; Catalyst updated 2026-10-07 on both stores; three PubMed records, none a methods paper |
| S-MP-10 | Pricing (re-read) | m-Path | https://m-path.io/pricing/ | Vendor page | **Direct** | Sensing Lite vs Full; External servers add-on; First ESM study support €800; white-label €2,000 annual update fee; add-on billing period not stated; no academic/commercial split. Verified. **Superseded in part (2026-10-21):** add-ons attach to the one-year subscription, from the Standard plan up (S-MP-12) |
| S-MP-11 | m-Path and m-Path Sense (App Store) | m-Path Software | https://apps.apple.com/us/app/m-path/id6733243074 ; https://apps.apple.com/us/app/m-path-sense/id6520394129 | App store | **Direct** | iOS listings current (2026-10-05, 2026-09-08) |
| S-CARP-16 | Three ways to use CARP (re-read); CARP Web Services | DTU | https://carp.dk/three-ways-to-use-carp/ ; https://carp.dk/caws | Project pages | **Direct** | Hosted, self-hosted and custom-app routes; DTU controller, EU/EEA residency; JSON export; DTU-affiliated, best-effort hosting; no price. Verified. **Superseded (2026-10-21):** best-effort hosting for research-partner projects only, with 2024 rates, on carp.dk/hosting/ (S-CARP-18) |
| S-CARP-17 | carp-portal package.json; CARP Studies (Google Play) | DTU (GitHub); Google Play | https://github.com/carp-dk/carp-portal/blob/main/package.json ; https://play.google.com/store/apps/details?id=dk.cachet.carp_study_app | Repo; app store | **Direct** | React 19, MUI 9; CARP Studies updated 2026-10-06; no App Store listing found. **Superseded (2026-10-21):** an unlisted App Store listing exists (id 1569798025; S-CARP-19) |
| S-EV-10 | Angrisani et al. 2025, Data Availability and Acknowledgments | *PNAS Nexus* (Europe PMC full text, PMC12501968) | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12501968/fullTextXML | Peer-reviewed | **Direct** | ALiR data via UAS registration and Data Use Agreement; minute-level Fitbit data; Evidation built the study app. Verified |
| S-EV-11 | Evidation Everyone Registry (ISPOR 2026 abstract) | Evidation staff | https://www.ispor.org/heor-resources/presentations-database/presentation-cti/ispor-2026/poster-session-4-3/inclusive-health-research-in-the-palm-of-your-hand-the-evidation-everyone-registry | Conference abstract | **Direct** | Launched 2025-12-22 to 5,800 selected members; 3,800+ consented by 2026-01-08. Reported |
| S-EV-12 | Evidation app store listings; security and trust page checks | Evidation Health | https://apps.apple.com/us/app/evidation/id793039965 ; https://play.google.com/store/apps/details?id=com.achievemint.android | App store | **Direct** | Both apps current; evidation.com/security and /trust return 404 |
| S-LEG-07 | Purple Robot README, build.gradle, licence file | Northwestern CBITS (GitHub) | https://github.com/cbitstech/Purple-Robot | Repo | **Direct** | API 22 SDK in README instructions; target SDK 23; GPL v3 or later; other licensing by contact |

## Sources added 2026-10-11 (vendor fact records, batch 1)

Read for the committed records `../facts/beiwe.yaml` and `../facts/radar-base.yaml`, facts checked 2026-10-10. The records hold the quotes; IDs continue each platform's sequence.

| ID | Title | Org | URL | Type | Retrieval | Establishes |
|---|---|---|---|---|---|---|
| S-BEI-15 | Use Beiwe (BSC rates, FY26) | Harvard Chan / Beiwe Service Center | https://hsph.harvard.edu/research-resource/beiwe/use-beiwe/ | Service page | **Direct** | $2,640 per month fixed plus $8.40 per Active Participant Month (FY26); examples $8,760 and $73,440 (for-profit); 30-day notice; service scope incl. raw data and summary metrics; open to for-profit investigators. Page modified 2026-07-23. Supersedes S-BEI-08 and S-BEI-11. Verified |
| S-BEI-16 | beiwe-android `app/build.gradle` and beiwe-backend `database/study_models.py` | Onnela Lab (GitHub) | https://github.com/onnela-lab/beiwe-android/blob/main/app/build.gradle ; https://github.com/onnela-lab/beiwe-backend/blob/main/database/study_models.py | Repo | **Direct** | Call and SMS logs only in lab-distributed builds (Play build none since 2.5.0); optional Android ambient audio stream, off by default, later removed from the backend (commit 2026-07-31, migration 0150, on main by 2026-10-19). Verified |
| S-RAD-18 | Supported Devices | RADAR-base | https://radar-base.org/docs/supported-devices/ | Docs page | **Direct** | Polar Vantage V3 and H10, Empatica E4, Fitbit, Garmin, Oura; Faros, Biovotion, Pebble 2 deprecated. Verified |
| S-RAD-19 | RADAR-REST-Connector, RADAR-PushEndpoint PR #92, RADAR-Rest-Source-Auth releases | RADAR-base (GitHub) | https://github.com/RADAR-base/RADAR-REST-Connector ; https://github.com/RADAR-base/RADAR-PushEndpoint/pull/92 ; https://github.com/RADAR-base/RADAR-Rest-Source-Auth/releases | Repo | **Direct** | Fitbit connector uses the legacy Fitbit Web API (off 2026-11-02, moved from 2026-10-30); Google Health ingest unreleased as of 2026-10-10. REST-Connector v0.7.6 (2026-10-30) releases the Google Health converters; PushEndpoint PR #92 still open on 2026-10-30. Verified |
| S-RAD-20 | radar-commons-android audio plugin; Health Connect issue #488 | RADAR-base (GitHub) | https://github.com/RADAR-base/radar-commons-android/tree/master/plugins/radar-android-audio ; https://github.com/RADAR-base/radar-commons-android/issues/488 | Repo | **Direct** | openSMILE audio features on Android; Health Connect an open request. Verified |
| S-RAD-21 | The Hyve ISO certification article | The Hyve | https://www.thehyve.nl/articles/the-hyve-iso-certified-2023 | Vendor news | **Direct** | ISO 27001:2022 for The Hyve B.V. (2023), scope not naming RADAR-base; no certificate found. Corroborated (vendor-stated) |
| S-RAD-22 | Active app (aRMT) privacy policy; Google user data privacy policy | RADAR-base | https://radar-base.org/active-app-armt-privacy-policy/ ; https://radar-base.org/google-privacy-policy/ | Privacy policy | **Direct** | Deletion through the deployment owner, generally within 60 days; Google Health data in AWS eu-west-2 or university infrastructure, not used for AI training. Verified |
| S-RAD-23 | RADAR passive RMT data-safety section | Google Play | https://play.google.com/store/apps/datasafety?id=org.radarcns.detail&hl=en_US | App store | **Direct** | Developer declares data not encrypted in transit and not deletable; contradicts the platform docs. Verified (as declared) |
| S-LEG-08 | studentlife R package (Zenodo 3371922); StudentLife dataset page | Zenodo; Dartmouth | https://zenodo.org/records/3371922 ; https://studentlife.cs.dartmouth.edu/dataset.html | Data package; dataset page | **Direct** (dataset page refused connection) | Package 2019-08-20, GPL-2.0, open access |
| S-LEG-09 | S-HealthStack organization repositories | Samsung (GitHub API) | https://github.com/S-HealthStack | Repo | **Direct** | Last pushes 2024-08-20 to 2024-10-24; v2.0-beta release commit |

## Sources added 2026-10-21 (vendor fact records, batch 2)

Read for the committed records `../facts/{mindlamp,aware,avicenna,metricwire,m-path,carp,lifedata,evidation}.yaml`, facts checked 2026-10-11. The records hold the quotes; IDs continue each platform's sequence. LifeData had no rows here before, so its IDs start at S-LD-01.

| ID | Title | Org | URL | Type | Retrieval | Establishes |
|---|---|---|---|---|---|---|
| S-LAMP-15 | LAMP-platform issues 910, 943, 944 and PR 939; LAMP-server PR 264 and releases | BIDMC (GitHub) | https://github.com/BIDMCDigitalPsychiatry/LAMP-platform/issues/943 ; https://github.com/BIDMCDigitalPsychiatry/LAMP-platform/issues/910 ; https://github.com/BIDMCDigitalPsychiatry/LAMP-platform/pull/939 ; https://github.com/BIDMCDigitalPsychiatry/LAMP-server/releases | Issue tracker; repo | **Direct** | Licence-terms request unanswered; request-level audit logging open; unmerged deletion rewrite; TestFlight builds 2025.4.2; newest server release 2023.7.27. Verified |
| S-LAMP-16 | mindLAMP docs: privacy, sensors and data, architecture | BIDMC | https://docs.lamp.digital/privacy ; https://docs.lamp.digital/sensors-data/ ; https://docs.lamp.digital/developer/architecture/components | Docs pages | **Direct** | "No licensing restrictions" statement; HIPAA Security Rule safeguards and GDPR-compliant encryption (self-claim, Corroborated); 90-day deletion; nine sensors, ten HealthKit or Health Connect types |
| S-LAMP-17 | LAMP-dashboard licence and release 2026.08.05.3; LAMP-core-android manifest | BIDMC (GitHub) | https://github.com/BIDMCDigitalPsychiatry/LAMP-dashboard/blob/master/LICENSE.md ; https://github.com/BIDMCDigitalPsychiatry/LAMP-dashboard/releases/tag/2026.08.05.3 ; https://github.com/BIDMCDigitalPsychiatry/LAMP-core-android/blob/master/app/src/main/AndroidManifest.xml | Repo | **Direct** | AGPL-3.0-only since 2026-08-05; survey branching inert at run time; no call-log or SMS permission on Android. Verified |
| S-LAMP-18 | Self-hosting deployment draft (unpublished) | BIDMC (GitHub) | https://github.com/BIDMCDigitalPsychiatry/LAMP-platform/blob/master/docs/06-developer/05-deployment/index.md | Draft docs | **Direct** | AWS estimates about $35 to $1,500 a month. Reported (draft) |
| S-AWR-11 | AWARE Support, Team and Use AWARE pages | AWARE Framework | https://awareframework.com/support/ ; https://awareframework.com/team/ ; https://awareframework.com/use-aware/ | Project site | **Direct** | University of Melbourne team; paid support and hosting by contact, no price; MySQL and AWARE Micro server requirements. Verified |
| S-AWR-12 | AWARE privacy policy (2019) and ecosystem-changes post | AWARE Framework | https://awareframework.com/privacy/ ; https://awareframework.com/changes-to-the-aware-ecosystem/ | Policy; news | **Direct** | GDPR section (self-claim, Corroborated, partly stale); AWARE-Light renamed the main Android AWARE (January 2025); old dashboard retired |
| S-AWR-13 | AWARE Client V3 listing; iOS sensor-module repositories; RAPIDS | Yuuki Nishiyama; AWARE (GitHub) | https://apps.apple.com/us/app/aware-client-v3/id6781949744 ; https://github.com/awareframework/com.awareframework.ios.sensor.keyboard ; https://github.com/carissalow/rapids | App store; repo | **Direct** | V3 streams (HealthKit, Apple Watch, AirPods motion, own-keyboard only); some module repos unlicensed, calendar MIT; RAPIDS AGPL-3.0. Verified |
| S-AVI-19 | How to export study data using the API; Raw Data reference | Avicenna Research | https://forum.avicennaresearch.com/t/how-to-export-study-data-using-the-api/1496 ; https://forum.avicennaresearch.com/t/raw-data/1241 | Vendor forum | **Direct** | Data Export API (key from support); raw-stream catalogue and export formats. Verified |
| S-AVI-20 | White-label solutions; Garmin Health SDK; SensorKit; SMS cost | Avicenna Research | https://avicennaresearch.com/features/white-label-solutions ; https://forum.avicennaresearch.com/t/garmin-health-sdk/1261 ; https://forum.avicennaresearch.com/t/sensorkit/1290 ; https://forum.avicennaresearch.com/t/how-sms-notification-costs-are-calculated/1540 | Vendor pages | **Direct** | Vendor-installed on-premises option (price not public); 25 Hz accelerometer, 32 Hz gyroscope; SensorKit ECG and PPG on approved studies; SMS at Twilio cost plus 30%. Verified |
| S-AVI-21 | UK ICO register entry ZC009135; NHS DSPT entry AVRESC001 | ICO; NHS England | https://ico.org.uk/ESDWebPages/Entry/ZC009135 ; https://www.dsptoolkit.nhs.uk/OrganisationSearch/AVRESC001 | Registers | **Direct** | Fee-payer registration; 2025-26 DSPT self-assessment "Standards met". Neither is an ISO or GDPR certification |
| S-MW-12 | MetricWire Consumer API (SwaggerHub, v3.0.0) | MetricWire | https://app.swaggerhub.com/apis-docs/MetricWire/ConsumerAPI/3.0.0 | API spec | **Direct** | Published REST API, OAuth2 client credentials; 31 phone stream types, Fitbit and Polar data; sensor operations suffixed "Enterprise". Corroborated (tier access not published) |
| S-MW-13 | Penn State SRC MetricWire licence | Penn State Survey Research Center | https://survey.psu.edu/trace/metricwire | University page | **Direct** | Enterprise sub-licence at reduced cost; no cost for pilot and thesis work; no prices. Reported |
| S-MP-12 | Subscriptions and billing; storage; research page | m-Path manual | https://m-path.io/manual/knowledge-base/subscriptions-and-billing/ ; https://m-path.io/manual/knowledge-base/storage/ ; https://m-path.io/landing/research/ | Docs pages | **Direct** | €1,599 to €16,593 per year (300 to 3,000 slots); add-on terms; Azure Frankfurt storage; "Institutions 150+". Verified |
| S-MP-13 | m-Path and m-Path Sense on Google Play; Terms (DPA, Annex 1); privacy statement | m-Path Software | https://play.google.com/store/apps/details?id=io.m_Path.kuleuven ; https://play.google.com/store/apps/details?id=io.m_Path_Sense.kuleuven ; https://m-path.io/data-processing/ ; https://m-path.io/privacy-policy/ | App store; legal | **Direct** | Both apps on Google Play; Article 28 DPA published; privacy statement named KU Leuven as host until an update between 2026-10-12 and 2026-10-19; it now agrees with the manual (Azure, Germany). Conflict resolved |
| S-MP-14 | Mobile sensing full; wearables; Garmin direct integration | m-Path manual | https://m-path.io/manual/knowledge-base/mobile-sensing-full/ ; https://m-path.io/manual/knowledge-base/wearables/ ; https://m-path.io/manual/knowledge-base/wearables-garmin-direct-integration/ | Docs pages | **Direct** | Sensing-full stream table with Android-only streams; Thryve wearables; direct Garmin 1 s heart rate, beat-to-beat intervals, 25 Hz accelerometer. Verified |
| S-CARP-18 | CARP hosting terms and rates | DTU | https://carp.dk/hosting/ | Project page | **Direct** | Hosted service only for projects with DTU Health Tech as an active research partner; 2024 rates (45,000 DKK setup, 1,250 DKK per study per month, staff time, pay as you go at cost plus 44%); no SLA. Verified |
| S-CARP-19 | CARP Studies (App Store, unlisted); new CARP Studies app post; available sampling packages | DTU | https://apps.apple.com/us/app/carp-studies/id1569798025 ; https://carp.dk/new-carp-studies-app/ ; https://docs.carp.dk/carp-mobile-sensing/sampling-packages/available-packages/ | App store; project pages | **Direct** | iOS 5.1.0 (2026-10-06), unlisted; v5 announced 2026-09-28; per-package Android-only marks. Verified |
| S-CARP-20 | CARP app privacy policy; CARP Studies data-safety section | DTU; Google Play | https://carp.dk/privacy-policy-app/ ; https://play.google.com/store/apps/datasafety?id=dk.cachet.carp_study_app | Policy; app store | **Direct** | Retention conflict: at least five years and erasure on request vs "Data can't be deleted" |
| S-LD-01 | USAspending awards to LIFEDATA LLC (VA San Diego) | U.S. Treasury (USAspending) | https://www.usaspending.gov/award/CONT_AWD_36C26224C0205_3600_-NONE-_-NONE- | Federal award records | **Direct** (API) | Three VA San Diego awards, actions of $3,480 to $7,160. Reported, not list prices |
| S-LD-02 | Data Privacy Framework list | U.S. Department of Commerce | https://www.dataprivacyframework.gov/list | Registry | **Direct** | LifeData active under EU-U.S., Swiss-U.S. and UK Extension, "Re-certification under Review"; self-assessment. Verified |
| S-EV-13 | Evidation help centre: currently available apps; Google Fit changes | Evidation Health | https://help.evidation.com/hc/en-us/articles/360008060493-Currently-available-apps ; https://help.evidation.com/hc/en-us/articles/50630998040211-How-to-Earn-Activity-Points-After-Google-Fit-Connection-Changes | Help centre | **Direct** | 12 connected third-party apps; Google Fit withdrawn on iOS and web. Verified |
| S-EV-14 | Our solutions; non-profit page; Our Future Health announcement | Evidation Health | https://evidation.com/for-customers/our-solutions ; https://evidation.com/for-customers/non-profit ; https://evidation.com/resources/evidation-selected-by-our-future-health-as-participant-platform-for-uks-largest-health-research-program | Vendor pages | **Direct** | Compliance badge images without statements; no separate academic tier; licensed Research & Engagement Platform (Our Future Health, 2023) |
| S-EV-15 | Member Privacy Notice (2026-07-13); Everyone Registry page; WAVE study record; GLP-1 cohort release | Evidation Health; ClinicalTrials.gov | https://evidation.com/members-privacy ; https://evidation.com/blog/shape-the-future-of-health-research ; https://clinicaltrials.gov/study/NCT06207929 ; https://evidation.com/resources/growth-potential-and-uneven-adoption-in-the-glp-1-market | Privacy notice; vendor pages; trial registry | **Direct** | Primarily US data centres; AI use for certain services; registry shares coded data with unspecified research partners; WAVE individual-data sharing undecided; GLP-1 cohort data via partner@evidation.com. Verified |

## Sources sought but not obtained

| Target | URL | Outcome |
|---|---|---|
| mindLAMP publications listing | https://docs.lamp.digital/about/publications/ | **404 (confirmed again, 2nd pass, and 2026-10-10)** |
| AWARE Framework detailed sensor documentation | https://awareframework.com/sensors/ | **Resolved 2nd pass — direct fetch succeeded**, full sensor table obtained |
| MetricWire official site (homepage, /pricing, /site-licence/, /contact-us/) | https://metricwire.com/ | **HTTP 403 on every path tried, both passes** — bot-protection, not a retrieval-effort gap |
| MetricWire GitHub organization | https://github.com/MetricWire | **Resolved 2nd pass — direct fetch succeeded** |
| Koa Health research page | https://www.koahealth.com/research | **Resolved 2nd pass — direct fetch succeeded** |
| Purple Robot lab page / phidatalab.org (all paths) | https://phidatalab.org/... | **HTTP 500 domain-wide, 2nd pass** — still not obtained; new signal (server error, not 404) |
| mindLAMP core-server/dashboard/app licence text | github.com/BIDMCDigitalPsychiatry (individual repo licence files) | Not directly opened this session; org-level listing didn't surface it. `LAMP-js`/`LAMP-py`/`LAMP-toolkit` licences ARE confirmed |
| Vendor pricing pages (Avicenna Research, m-Path) | various | **m-Path resolved 2026-08-25 (3rd pass)** — full pricing found at `m-path.io/pricing/`. **Avicenna Research remains non-public** — a dedicated 3rd-pass search still found no pricing page. |
| Beiwe API endpoint documentation (`data_access_api_reference` contents) | github.com/onnela-lab/beiwe-backend | Directory confirmed to exist (3rd pass); its contents/endpoint list were not opened this session |
| RADAR-base iOS-side itemized sensor list | radar-base.org docs | Android list itemized (3rd pass); the referenced iOS comparison chart's contents were not extracted |
| CARP `carp-portal` documentation/feature detail | github.com/carp-dk/carp-portal | Repository's existence confirmed (3rd pass); its README/feature set was not opened this session |

---

## Link check — 2026-08-24 (1st pass) / 2026-08-24 second pass

- **Direct fetch succeeded (1st pass):** Onnela Lab platform page, `beiwe-backend` README, `forest`
  repo, RADAR-base "About," BIDMCDigitalPsychiatry GitHub org, AWARE Framework site (partial
  content), Purple Robot lab page.
- **Direct fetch succeeded (2nd pass, new):** AWARE Framework sensors documentation
  (`awareframework.com/sensors/`), AWARE Framework GitHub org, BIDMCDigitalPsychiatry current
  repository listing, `LAMP-portal` and `LAMP-app` repos (confirming 2020-11-17 archival),
  `docs.lamp.digital` landing page, MetricWire GitHub org, Koa Health `/research` page.
- **404 (genuinely unavailable, confirmed in both passes):** `docs.lamp.digital/about/publications/`.
- **403 bot-protection (confirmed in both passes, MetricWire specifically):**
  `metricwire.com/`, `metricwire.com/pricing`, `metricwire.com/site-licence/`,
  `metricwire.com/contact-us/`.
- **500 server error, domain-wide (new signal, 2nd pass):** `phidatalab.org` and every path tested
  under it (`/`, `/software/`, `/software__trashed/purple-robot-android-apps/`) — the domain that
  succeeded on a single-page direct fetch in the first pass could not be reached at all in the
  second pass.
- **Not directly fetched after the first two passes (search-summary only), now resolved in the
  2026-08-25 third pass:** Avicenna Research (homepage, legal page, data-access page all directly
  fetched), m-Path (homepage, pricing page, manual landing page all directly fetched), RADAR-base
  (About page was already Direct in the 1st pass; sensors doc, GitHub org, and The Hyve's managed-
  hosting page newly directly fetched), Beiwe (backend repo, forest repo, and BSC overview page
  re-fetched/newly fetched directly), and CARP Mobile Sensing (CAMS feature page and `carp-dk` GitHub
  org newly directly fetched). All eight Module 2 platforms have now had at least one Direct-fetch
  pass on their primary vendor/maintainer materials.
- **Still search-summary-only even after the third pass:** RADAR-base's Publications page, 2026
  Symposium announcement, and the JMIR/RADAR-IoT peer-reviewed papers; Avicenna Research's homepage-
  adjacent pages (S-AVI-01/02/04–08); m-Path's core methods paper (S-MP-02) and research page
  (S-MP-03); CARP's `carp.dk`/`carp.cachet.dk` project pages (S-CARP-01–03) and the Bardram et al.
  architecture paper and 2025 UbiComp demo paper (S-CARP-05, S-CARP-08). These remain candidates for
  a future pass if a specific claim from them becomes decision-relevant.


---

## Onnela Lab publications page (added 2026-08-31)

| ID | Title | Org | URL | Type | Retrieval | Establishes |
|---|---|---|---|---|---|---|
| S-BEI-09 | Papers — Onnela Lab | Onnela Lab, Harvard T.H. Chan SPH | https://hsph.harvard.edu/research/onnela-lab/papers/ | Lab publication listing | **Direct** | **Primary/Verified.** The lab's own complete publication list, grouped under exactly two headings: "Digital Health and Phenotyping" (114 listed entries, 113 distinct papers) and "Network Science" (out of scope, not pulled). Establishes the Beiwe/Forest originating lab's full digital-health publication record and its scope boundary |
| S-BEI-10 | Europe PMC REST API (search / `resultType=core`) | EMBL-EBI | https://www.ebi.ac.uk/europepmc/webservices/rest/search | Bibliographic API | **Direct** | DOI, PMID, PMCID, journal, publication year, `isOpenAccess` flag, and abstract for 107 of the 113 papers. The remaining 6 are items the lab page itself labels *Submitted* / *In print* with no DOI |

**What this pass added.** A complete catalog of the Digital Health & Phenotyping half of the Onnela
Lab's output is now in [`literature-library.md`](literature-library.md) — 91 papers filed to this
module, 22 to Module 1 (wearable-primary and Apple-ecosystem). 54 Module 2 PDFs were newly obtained
and verified; 2 were already in the knowledge base (the 2016 Torous *JMIR Mental Health* Beiwe paper
and the 2021 Onnela *JOSS* software paper) and were not duplicated.

**What this pass deliberately did not do.** No claim anywhere in this module was re-labelled on the
strength of these papers. `profiles/beiwe.md` and the comparison matrix are unchanged — the catalog is
now available to support a later evidence pass, but adding a citation is not the same as reading it
against a claim, and the confidence markers throughout this module still reflect what was actually
verified in the 2026-08-24/25 passes.

**Access barriers encountered (2026-08-31):**

- **Europe PMC PDF render service, HTTP 500** — a repeated, non-transient failure for a cluster of
  older PMC author manuscripts (roughly 2015–2022, chiefly *Annals of Surgery*, *Clinical
  Psychological Science*, *Molecular Psychiatry*, *Harvard Review of Psychiatry*, *Current Psychiatry
  Reports*). Retried against `pmc.ncbi.nlm.nih.gov/articles/<PMCID>/pdf/` with a browser
  User-Agent; still no PDF. Recorded as an **infrastructure barrier, not a paywall** — Europe PMC's
  own metadata marks several of these `isOpenAccess: Y`.
- **PMC direct-PDF route returns HTML, not PDF** — consistently for the JAMA-family articles
  (*JAMA Network Open*, *JAMA Surgery*).
- **medRxiv, HTTP 403** — the 2025 circadian rest-activity biomarker preprint.
- **Genuinely paywalled, no OA route located** — *Annals of Surgery*, *Neurosurgery*, *Behaviour
  Research and Therapy*, *Psychiatry Research*, *Annual Review of Clinical Psychology*, *Biometrics*,
  *Statistical Methods in Medical Research*, *IEEE/ACM TASLP*, *Psychiatric Annals*, *AJOB*.
