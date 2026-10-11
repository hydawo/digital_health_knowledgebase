# Module 2: Digital Phenotyping Comparison Matrix

**Rebuilt 2026-10-10 from the profiles.** Every cell below was rewritten from the current profile in
`profiles/` after the 2026-10-10 independent-review corrections, replacing the matrix last rebuilt on
2026-08-24/25. Each cell restates what the named profile says; where the profile says Unclear, the cell
says Unclear rather than guessing. Dates in cells are the date the profile records the fact as checked.
Vendor statements about a vendor's own certifications are Corroborated at most unless a certificate or
registry entry was read; none was read for any Module 2 platform.

**Updated 2026-10-11.** The Beiwe and RADAR-base cells were corrected against their committed vendor
fact records (`../facts/beiwe.yaml`, `../facts/radar-base.yaml`). Those cells carry the records' dates
(facts checked 2026-10-10). See the change list at the end.

Scope: ten current platforms with full profiles (Beiwe, RADAR-base, mindLAMP, AWARE Framework, Avicenna
Research, MetricWire, m-Path, CARP Mobile Sensing, LifeData, Evidation), plus Purple Robot and
StudentLife from `profiles/legacy-and-adjacent-platforms.md` where a row is useful. LifeData and
Evidation sit at the edge of scope (EMA/ePRO and a participant network respectively, not phone sensing),
which their rows state.

Multiple tables are used deliberately. Do not read any single table as a ranking.

---

## Table 1. Platform identity and status

| Platform | Organization | Type | Current status | Licence |
|---|---|---|---|---|
| **Beiwe** | Onnela Lab, Harvard T.H. Chan SPH | Academic open source, plus a paid managed service (Beiwe Service Center, BSC) | Active: beiwe-backend pushed 2026-10-06, beiwe-ios 2026-10-07, beiwe-android 2026-09-08, forest 2026-10-06 | BSD-3-Clause (backend, iOS, Android, Forest) |
| **RADAR-base** | King's College London and The Hyve | Academic/consortium open source; managed hosting sold by The Hyve | Active (ManagementPortal pushed 2026-10-05). The iOS passive app is dormant (last commit 2021-01-19) | Apache 2.0 |
| **mindLAMP** | BIDMC Division of Digital Psychiatry | Academic, source-available; hosted and supported through the BIDMC mindLAMP Core | Active (server, dashboard and both app repos pushed 2026-10-08). `LAMP-portal` and `LAMP-app` archived 2020-11-17 | Mixed: LAMP-dashboard AGPL-3.0; LAMP-server, LAMP-core-android, LAMP-core-ios no licence file (all rights reserved by default); API clients BSD-3-Clause; LAMP-toolkit MIT |
| **AWARE Framework** | International academic collaboration (originated University of Oulu) | Academic open source, plugin-extensible | Active: aware-client pushed 2026-08-07, AWAREFramework-iOS 2026-02-17 | Apache-2.0 (aware-client and AWAREFramework-iOS; not every repo checked) |
| **Avicenna Research (formerly Ethica)** | Avicenna Research Inc. (Canada) | Commercial SaaS | Active (iOS app released 2026-10-07) | Closed source |
| **MetricWire** | MetricWire Inc. (Waterloo, Canada), founded 2013 | Commercial SaaS | Active ("Catalyst By MetricWire" updated 2026-10-07 on both stores) | Closed source |
| **m-Path** | m-Path, KU Leuven spin-off | Commercial SaaS with a peer-reviewed methods paper | Active (apps updated 2026-09-08 and 2026-10-05) | Closed source |
| **CARP Mobile Sensing** | DTU (Bardram group) | Academic open-source framework, with a DTU-hosted service and web portal | Active: carp.sensing-flutter pushed 2026-10-09, carp-portal 2026-10-07 | MIT |
| **LifeData (RealLife Exp / LifeData+)** | LifeData, LLC (Marion, IN, USA) | Commercial SaaS, EMA/ePRO; not passive sensing | Active; two app generations in parallel | Closed source (no GitHub organization or SDK) |
| **Evidation** | Evidation Health, Inc. (San Mateo, CA, USA) | Commercial participant network and real-world-data platform; edge of scope (wearable plus survey intake, not phone sensing) | Active (apps updated 2026-10-02 and 2026-10-04) | Closed source |
| **Purple Robot** | Northwestern CBITS / PHI Data Lab | Academic open source, Android only | **Dormant since 2016**: last commit 2016-04-11, last push 2017-04-07, lab page removed (Corroborated) | GPL-3.0 (`LICENSE.GPLv3` in repo root) |
| **StudentLife** | Dartmouth | Historical study and dataset, not a platform | Dataset only; the dataset site refused connections on 2026-10-10 | `studentlife` R package GPL-2.0 (Zenodo 3371922) |

---

## Table 2. Apps, app stores and iOS/Android parity (parity NOT assumed)

| Platform | iOS client | Android client | iOS client maintained? | Parity |
|---|---|---|---|---|
| Beiwe | "Beiwe2" on the App Store (v2.5.11, 2026-09-30) | APK sideloaded from each deployment's download link; no Google Play listing (Not Found in a browser and in Play search, 2026-10-10; Unclear) | Yes (beiwe-ios pushed 2026-10-07) | **No, Verified 2026-09-03 from the Beiwe wiki.** Calls, SMS (lab-distributed Android builds only), Wi-Fi and Bluetooth are Android only; power state is Android only per one wiki page and conflicting on iOS; magnetometer, proximity, device motion and reachability are iOS only |
| RADAR-base | No maintained passive app: `radar-prmt-ios` is "work in progress" that "only records location data without sending it to a server". The questionnaire app "RADAR Active RMT" is on the App Store (2026-08-24) and reads HealthKit when opened | "RADAR passive RMT" (2026-06-18) and "RADAR active RMT" (2026-09-09) on Google Play | Active app yes; passive app no | **No.** Android passive catalogue of 17 streams Verified; current iOS phone-sensor capability Unclear (2019 chart and dormant repo conflict); platform docs say iOS sensors are "more sparse... due to lack of background collection capabilities" |
| mindLAMP | "mindLAMP 2" on the App Store, last updated 2023-05-26 | "mindLAMP 2" on Google Play (2026-05-17) | Unclear: LAMP-core-ios pushed 2026-10-08, but the public App Store build dates from 2023 | Unclear (streams named without a per-OS breakdown) |
| AWARE Framework | "AWARE Client V3" (v1.7.0, 2026-07-23) and "AWARE Client V2" on the App Store; needs the study's server URL | Not on Google Play; distributed from GitHub (sideloading) | Yes | **No, Verified 2026-10-10.** Website catalogue: 19 of 33 modules iOS-available, 14 Android only. The iOS repository also runs proximity and calls (call events only, no history). App usage, SMS, keyboard, light, screenshot and screentext are Android only |
| Avicenna Research | App Store (v1065, 2026-10-07) | Google Play `com.ethica.logger` (2026-09-05) | Yes | Unclear (most streams unverified; one study found Bluetooth beaconing unreliable on iOS) |
| MetricWire | "Catalyst By MetricWire" on the App Store (2026-10-07) | Same app on Google Play (2026-10-07) | Yes | Unclear |
| m-Path | "m-Path" (2026-10-05) and "m-Path Sense" (2026-09-08) on the App Store | Android supported per the pricing page; Google Play listing not located (Unclear) | Yes | Unclear |
| CARP Mobile Sensing | Flutter framework builds for iOS; DTU's "CARP Studies" app not found on the App Store (Unclear) | "CARP Studies" on Google Play (2026-10-06) | Framework yes; reference app on iOS Unclear | Not verified stream by stream; calls and SMS are No (OS) on iOS |
| LifeData | RealLife Exp (2026-04-06) and LifeData+ (2026-10-10; needs iOS 18.0+) on the App Store | Both generations on Google Play | Yes | Same single stream on both (GPS captured with a survey response) |
| Evidation | "Evidation" on the App Store (2026-10-02) | Google Play `com.achievemint.android` (2026-10-04) | Yes | Not applicable: no phone-sensor streams documented |
| Purple Robot | None (Android only) | Not maintained since 2016 | Not applicable | Not applicable |

Two platforms have a documented, itemized gap: Beiwe (per-stream OS split from its wiki) and AWARE
(per-module catalogue plus the iOS repository). RADAR-base documents the gap qualitatively, and has no
current iOS passive app. Every other "Unclear" is an unverified question, not a claim of parity.

---

## Table 3. Open source, hosting options and what you need to run it

| Platform | Source and licence | Self-hosting | Hosted or managed option (who; price public?) | Capacity needed |
|---|---|---|---|---|
| Beiwe | Open source (BSD-3) | Yes, AWS only; "moderate AWS and Python expertise" (README); open-source version provided as-is, paid help from contract developers (Zagaran) | **Beiwe Service Center**, run by the Onnela Lab on its AWS account; separate US and EU login portals; **rates published** (Table 6) | AWS and Django capacity, or none via the BSC |
| RADAR-base | Open source (Apache 2.0) | Yes; Kafka-based backend; RADAR-Kubernetes for cluster installs ("used in few production environments") | **"RADAR-base as a Service"**, The Hyve: single server, "Studies with a maximum of 200 participants are ideal", "best suited for small-scale and short-term studies"; client owns the data; **quote only** | DevOps and data-engineering capacity, or none via The Hyve for small studies |
| mindLAMP | Source-available: server and apps unlicensed, dashboard AGPL-3.0 | Technically yes (LAMP-server, Docker); the Core's own model is "Full mindLAMP stack in partner's own AWS account". Self-hosting or modifying the unlicensed code outside that needs BIDMC permission | **BIDMC mindLAMP Core**, "the supported deployment pathway": a separate BIDMC-hosted instance or the shared instance at lamp.digital; **priced by proposal** after a free consultation | Own AWS capacity, or none via the Core |
| AWARE Framework | Open source (Apache-2.0) | Yes (backend); the only deployment path | **None found** | Server administration, plus Android sideloading |
| Avicenna Research | Closed | No | Vendor SaaS only; data on servers in Canada (vendor-stated) | None |
| MetricWire | Closed | No | Vendor SaaS only; data in the US on Google Cloud Platform (vendor-stated) | None |
| m-Path | Closed | No self-hosting of the software; a custom-priced **"External servers" add-on** saves data "on your personal server" (scope not stated) | Vendor SaaS | None for the default SaaS |
| CARP Mobile Sensing | Open source (MIT) | Yes: CARP Web Services, Web Portal and Studies App, with Keycloak and PostgreSQL, in Docker or Kubernetes | **DTU-hosted CARP service** on DTU Computerome: "Researchers affiliated with DTU can use this service" (CAWS page), while the "Three ways" page invites researchers to email info@carp.dk; best effort; DTU is data controller; **price not stated** | Flutter capacity for a custom app; container capacity to self-host; none for the hosted service if an account is granted |
| LifeData | Closed | No | Vendor SaaS only; US servers, Microsoft Azure named in the privacy policy | None |
| Evidation | Closed | No | Vendor runs the studies on its member base; sponsors deploy nothing | None (sponsor model) |

**Practical read.** Three postures remain: self-hosted platforms with public source (Beiwe, RADAR-base
and AWARE under open licences; mindLAMP source-available, with the server and apps unlicensed), fully
managed commercial SaaS (Avicenna Research, MetricWire, m-Path, LifeData, Evidation), and a framework
for building your own app (CARP). The hosted picture changed: **four public-source platforms now have
a documented hosted alternative to self-hosting**: Beiwe (BSC, the only one with published rates),
RADAR-base (The Hyve, quote only), mindLAMP (BIDMC mindLAMP Core, priced by proposal) and CARP
(DTU-hosted, stated for DTU-affiliated researchers, price not stated). AWARE has none.

---

## Table 4. Active data collection (EMA and surveys)

| Platform | Surveys/EMA | Notable documented features |
|---|---|---|
| Beiwe | Yes: written, audio and image surveys | Absolute, relative (to a per-participant date) and weekly schedules; branching from NOT/OR/AND blocks over slider, radio and numeric answers; randomized question selection (disables branching); survey resends tracked server-side. Verified 2026-09-03 |
| RADAR-base | Yes: PROM/questionnaire delivery through the aRMT app | Scheduling, branching and event-triggered EMA not verified (Unclear) |
| mindLAMP | Yes: surveys plus cognitive tests (LAMP-activities) | Clinical "Assess/Manage" orientation; EMA scheduling and branching depth not benchmarked |
| AWARE Framework | Yes: a native ESM/EMA module on Android and iOS | Scheduling and branching depth not benchmarked |
| Avicenna Research | Yes: surveys, cognitive and behavioral tasks, TeleVisit | Clinical-trial-style outcome assessment (vendor feature pages) |
| MetricWire | Yes: mobile diaries; "contextualized trigger-based survey deployment" | Context-triggered surveys and electronic consent (vendor-described) |
| m-Path | Yes: the platform's core | No-code EMA/EMI design with published JITAI support (Frontiers in Digital Health 2023) |
| CARP Mobile Sensing | Survey data is a named CAMS sampling package; a Research Package is used in DTU apps | Scheduling and survey features not verified (Unclear) |
| LifeData | Yes: the platform's core | Fixed, random (with minimum spacing), triggered and event-based schedules; branching; a trigger that starts a whole new schedule; display logic, piped text, scores; 13 question types; offline collection; right-to-left languages (vendor pages) |
| Evidation | Yes: in-app survey cards, daily, weekly or event-triggered | Branching, randomized timing, cognitive tasks and audio diaries Unclear |

---

## Table 5. Passive sensing and wearable integration (as documented, not bench-tested)

| Platform | Phone streams documented (OS split where the profile gives one) | Wearable and health-platform integration |
|---|---|---|
| Beiwe | Both OS: GPS, accelerometer, gyroscope, device information. Android only: calls and SMS (lab-distributed builds only; the Google Play build has not collected them since 2.5.0), Wi-Fi, Bluetooth, screen and power state (power state on iOS is conflicting documentation). iOS only: magnetometer, proximity, device motion, reachability. Audio through audio surveys; Android also has an optional ambient audio stream, off by default, set per study | None documented in the profile |
| RADAR-base | Android: 17 streams, including relative location, acceleration, gyration, magnetic field, light, step count, activity recognition, sleep events, lock/unlock, app usage, call and SMS logs (hashed), Bluetooth counts, battery, weather; audio features through an openSMILE plugin. iOS phone sensors Unclear | Shipped: Polar Vantage V3 and H10 and Empatica E4 (Bluetooth via pRMT; Empatica has retired the E4), Garmin and Oura (REST). The Fitbit REST route ends 2026-10-30, with no released Google Health ingest as of 2026-10-10. Huawei connector unreleased; no Health Connect. iOS reads 17 HealthKit types through the aRMT app when opened |
| mindLAMP | GPS, accelerometer, gyroscope, screen time and calls named, without a per-OS breakdown; everything else Unclear | Steps, sleep and heart rate from a paired wearable (devices not itemized) |
| AWARE Framework | 33 catalogue modules; 19 iOS-available. Includes location, accelerometer, gyroscope, magnetometer, barometer, battery, screen, network, Wi-Fi, Bluetooth on both; light, app usage, keyboard, SMS, telephony Android only | Fitbit module in the iOS framework; an Apple Watch (watchOS) framework; Android plugin coverage not itemized |
| Avicenna Research | GPS on both; Bluetooth beaconing on Android (unreliable on iOS in one study); the rest Unclear | Wearables integrated per vendor; Garmin Health SDK (wrist-status stream) confirmed in the notifications reference |
| MetricWire | GPS on both (vendor-named); "Passive Sensors" named without a list; the rest Unclear | Not established |
| m-Path | GPS, Bluetooth, pedometer/activity and noise context via m-Path Sense (vendor-named, Reported). Sensing Lite (€3,000) collects only when a questionnaire is completed; Sensing Full (€10,000) is continuous | Smartwatch integration add-on (€3,000; Fitbit, Garmin, Apple Watch named) |
| CARP Mobile Sensing | Location, activity, connectivity, audio on both; app usage, calls and SMS on Android; other streams Unclear | Apple Health and Google Health Connect; Movisens, eSense, Polar, Movesense, Dexcom G7 |
| LifeData | **GPS captured with a survey response only**, not continuous; every other stream No | None documented |
| Evidation | No phone-sensor stream documented (device identifiers only; geolocation mentioned in the privacy notice, Unclear) | 20 or more connected consumer apps and devices, including Fitbit, Apple Health, Garmin and Oura |

---

## Table 6. Pricing, service model and academic access

| Platform | Software cost | Hosting or service cost | Academic program or pricing | Pricing public? |
|---|---|---|---|---|
| Beiwe (self-hosted) | Free | Own AWS bill | Not applicable | No licence fee |
| Beiwe (BSC) | Free (same code) | **$2,640 per month fixed plus $8.40 per Active Participant Month (FY26)**; examples $8,760 (N=100, L=1, T=3) and $73,440 for-profit (N=100, L=12, T=24), both reproduce from the formula; rates revisable on 30 days' notice; no minimum published; FY24 card ($1,937 + $6) superseded. An FY27 card may exist but was not published on 2026-10-10 | One rate structure for university and for-profit use (Corroborated, from the arithmetic); no separate academic rate published; "not a scientific collaboration" | **Yes** |
| RADAR-base (self-hosted) | Free | Own infrastructure | Not applicable | No licence fee |
| RADAR-base (The Hyve) | Free (same code) | Subscription, quote only (Corroborated: no price and an inquiry route); no minimum term published | No academic tier or price published | **No** |
| mindLAMP | No licence fee identified | Self-hosting costs, or a BIDMC mindLAMP Core proposal (free first consultation) | No academic rate published; the Core names grant-funded projects as a fit | **No** |
| AWARE Framework | Free | Own infrastructure; Open Collective donations | None | Not applicable |
| Avicenna Research | Licence, non-public | Included in the licence | No academic rate found. A free trial exists for testing only (data wiped monthly, study deleted after one year) | **No** |
| MetricWire | Non-public; demo by request | Included | **Academic Site Licence** for institutions ("cost effective", unpriced; page copyright 2023) | **No** |
| m-Path | Free tier (€0, 50 participants/year); Essential, Standard, Comfort €1,599 to €5,338 per year excl. VAT (300 to 600 participants) | Add-ons by contact: Sensing Lite €3,000, Sensing Full €10,000, API €5,000, Smartwatch €3,000, Cognitive tests €4,500, white-label €10,000 plus €2,000 a year, and others; add-on billing period not stated | Only "research plans"; no academic/commercial split; basic version free for individual practitioners | **Yes** |
| CARP Mobile Sensing | Free (MIT) | Own development and infrastructure, or the DTU-hosted service (price not stated) | Hosted service stated for DTU-affiliated researchers | Not applicable / not stated |
| LifeData | Non-public; formula (researchers x duration x participants) described | Non-public; ten named paid services | Separate academic and commercial pricing; graduate-student discount (vendor-stated); no trial | **No** |
| Evidation | Non-public sponsor pricing | Not applicable | No program on vendor pages; academics can obtain the Evidation-built American Life in Realtime data through USC's Understanding America Study Data Use Agreement | **No** |

Beiwe and m-Path are the only platforms with published prices. Among the public-source platforms, the
BSC is the only hosted service with published rates.

For Beiwe and RADAR-base, the generated, quote-backed version of this table is
`../facts/_generated/research-and-access.md` (built from the vendor fact records; it covers batch 1
so far).

---

## Table 7. Privacy, security and compliance

| Platform | Documented security design | Compliance statements (confidence) |
|---|---|---|
| Beiwe | On-device, in-transit (RSA-AES) and at-rest encryption; PBKDF2/SHA-256 identifier hashing with per-installation keys; production-study setting (Verified). Portal locks an account for 10 minutes after 10 failed logins (current code, Corroborated) | HIPAA applicability acknowledged ("may interact with laws covering PII or PHI like HIPAA"), not a compliance claim. No GDPR, SOC 2 or ISO statement; no BAA or DPA published. BSC EU portal exists; EU storage location not stated |
| RADAR-base | Self-hosting for in-hospital data custody; The Hyve hosts in "a GDPR compliant public cloud infrastructure located at the choice of the client"; DPA when The Hyve keeps managing or accesses data. aRMT policy: deletion through the deployment owner, generally within 60 days. Google Health data in AWS eu-west-2 or university infrastructure, not used for AI training. The passive app's Play listing declares no encryption in transit, which contradicts the docs | **Corroborated (vendor-stated):** The Hyve states ISO 27001:2022 for The Hyve B.V.; the scope does not name RADAR-base and no certificate was found. No HIPAA or SOC 2 statement (2026-10-10) |
| mindLAMP | The Core describes role-based access controls, audit logs and IRB/security-review language as part of its service | No HIPAA, SOC 2 or GDPR claim; the Division's privacy page makes none (checked 2026-10-10) |
| AWARE Framework | Not established | Not located |
| Avicenna Research | AES-256 at rest, TLS 1.2+ in transit, full-disk encryption; data in Canada (vendor-stated) | **Corroborated (vendor-stated):** ISO 27001:2022 stated (Nov 2024, surveillance audit Nov 2025), "through UKAS" with a CertCheck link that could not be read; HIPAA/GDPR/PIPEDA language; BAAs required for covered transactions. No SOC 2 or Part 11 |
| MetricWire | AES-256 at rest, TLS 1.2+ in transit, MFA for production, US storage on Google Cloud Platform (vendor-stated) | **Corroborated (vendor-stated):** "ISO 27001 certified and SOC II Type II compliant"; claims compliance with 21 CFR Part 11, HIPAA and GDPR. No certificate, auditor or BAA terms published |
| m-Path | Separate privacy policy for m-Path Sense | **Corroborated (vendor-stated):** "compliant with GDPR and HIPAA". No SOC 2, ISO or DPA template located |
| CARP Mobile Sensing | Privacy-preserving data transformation as a framework feature | GDPR roles documented: DTU is controller for its hosted service and cannot act as processor for outside controllers; EU/EEA residency by default. No certification claimed |
| LifeData | US residency, Azure hosting; retention figures (180 days, 30 days, 12 months) Verified from the legal documents | EU-U.S., UK and Swiss Data Privacy Framework self-certification; GDPR processor role. HIPAA claimed in marketing only, absent from the legal documents (Unclear). No SOC 2, ISO or Part 11 |
| Evidation | Corporate privacy notice (identifiers, device data, geolocation, CCPA opt-out); US data centres | No security or trust page (evidation.com/security and /trust return 404); compliance Unclear |

No Module 2 platform has an independently confirmed certification. Three vendors (Avicenna Research,
MetricWire, m-Path) make specific compliance statements, and The Hyve states ISO 27001 for itself, not
for RADAR-base by name; treat them as vendor claims to be checked
against a certificate or audit report before relying on them.

---

## Table 8. Study operations and management

| Platform | Researcher dashboard | Monitoring and management documented | Background keepalive | Multi-study / multi-site |
|---|---|---|---|---|
| Beiwe | Yes (beiwe-backend portal) | Per-stream data-volume dashboard (an archived wiki page says it is being replaced by Tableau feeds; use the newer Tableau endpoint path); per-participant heartbeat, token and notification history; study and site admin roles | **Yes**: server push when the app has not checked in (default 1 hour), on by default since 2024 once servers are updated | One backend hosts multiple studies |
| RADAR-base | Yes (ManagementPortal, maintained) | `DisconnectMonitor` emails researchers when a source stops sending | No participant-facing keepalive; researcher email only | Consortium origin; multi-site by design |
| mindLAMP | Yes (LAMP-dashboard) | Core service includes role-based access, audit logs, uptime monitoring and study support | None found | Core claims 50+ active sites; multi-site deployments named as a fit |
| AWARE Framework | Study configuration through AWARE-Configurator; no researcher dashboard confirmed | Unclear | iOS only, silent push, off by default | Unclear |
| Avicenna Research | Yes ("Study Management") | Participation page with "In Operation" percentage and last-data time; server-side "Sensor Data Gap Detected" notifications for the Garmin wrist-status stream only | No phone-app keepalive | Unclear |
| MetricWire | Yes, real-time monitoring dashboard | Participant Activity events (for example repeated app launches) | None found | Unclear |
| m-Path | Yes, no-code web study builder | Unclear beyond the builder | **Yes** (m-Path Sense): 5-minute server check-in with researcher-set reopen reminders | Unlimited projects and accounts on the Standard tier and above |
| CARP Mobile Sensing | Yes, CARP Web Portal (MIT, active): protocols, deployments, participants, consent, data visualisation, JSON export; no versioned releases or end-user docs | No adherence alerts or audit logs found | Client-side `heartbeat` record only | Unclear |
| LifeData | Yes: engagement and response-rate dashboards, smart reminders, response/score/event alerts | Roles and permissions; audit trails as a paid custom service | Not documented | Institutional master subscriptions with department sub-accounts; multi-site on the Clinical tier |
| Evidation | No self-service console; sponsors work with Evidation staff | Not documented publicly | Not applicable | Cohorts across 20 or more conditions (vendor) |

---

## Table 9. Differentiators (checked against the profiles on 2026-10-10)

| Platform | What sets it apart |
|---|---|
| **Beiwe** | The only public-source platform here whose managed hosting has published rates, offered by the lab that builds the software; a separate analysis package (Forest) with documented daily mobility, communication and survey metrics; and a server-side keepalive on by default |
| **RADAR-base** | Kafka-based streaming architecture built for multi-site, multi-modal (phone, wearable, IoT) consortium studies, with a shipped wearable catalogue (Polar, Empatica E4, Garmin, Oura, HealthKit through the aRMT app; the Fitbit route ends 2026-10-30) |
| **mindLAMP** | Explicit dual research and clinical-care orientation, cognitive tasks built in, and a builder-run hosted pathway (the mindLAMP Core); source-available rather than open source |
| **AWARE Framework** | One of the longest-running, most plugin-extensible open-source sensing frameworks, with contributions from many academic groups; iOS on the App Store, Android by sideload |
| **Avicenna Research** | A clinically oriented commercial feature set (TeleVisit, cognitive and behavioral tasks) and specific export formats (CSV, JSON, GEXF network graphs, KML location data) |
| **MetricWire** | Context-triggered survey deployment and electronic consent, plus an institution-level Academic Site Licence |
| **m-Path** | Published JITAI support with a peer-reviewed methods paper, and the most itemized published price list in the module (tiers plus priced add-ons) |
| **CARP Mobile Sensing** | The only framework-shaped option, a Flutter library a team builds its own app on; also the only platform with documented integration with both Apple Health and Google Health Connect (RADAR-base reads Apple HealthKit through its aRMT app) |
| **LifeData** | Detailed, specifically documented EMA scheduling and triggering with essentially no passive sensing; audit trails sold as service work |
| **Evidation** | A recontactable member base with wearable connections and claims/EHR linkage at a scale no self-run platform reaches; the sponsor operates nothing |

Superlatives removed in this rebuild because the profiles no longer support them: Beiwe as "the only
platform with both a free self-hosted path and a documented paid managed-hosting alternative" (mindLAMP,
CARP and RADAR-base now have hosted routes); Avicenna as "the only independently audited compliance
certification" (its ISO statement is vendor-stated, and MetricWire states ISO 27001 and SOC 2 too);
m-Path as "the only platform with a dedicated peer-reviewed methods paper" (Beiwe, RADAR-base, mindLAMP
and CARP all have platform papers); CARP as the only platform with "native Apple Health and Google
Health Connect" integration, now qualified to "both"; LifeData's "deepest scheduling engine in this
module" and Avicenna's "broadest" active-assessment set, which no benchmark supports.

---

## Table 10. Choosing by research need

| If your primary need is | Consider | Be cautious of | Why |
|---|---|---|---|
| Full data custody, algorithmic transparency, willing to run AWS | **Beiwe** (self-hosted) | Vendor SaaS platforms; mindLAMP if you need to modify unlicensed code | BSD-3, self-hostable, Forest analysis package |
| No in-house infrastructure, still want an open-source lineage | **Beiwe via BSC** (published rates) or **mindLAMP via the BIDMC Core** (priced by proposal) | RADAR-base via The Hyve above about 200 participants (single-server setup); CARP's hosted service if you are not DTU-affiliated (access terms conflict) | Each offloads infrastructure; only the BSC publishes rates |
| Large multi-site, multi-modal consortium study | **RADAR-base** (self-hosted) | The Hyve's managed tier, pitched at small, short-term studies; Beiwe's single-lab default scale | Kafka streaming, IoT gateway, EU consortium origin |
| iOS passive phone sensing | **Beiwe** or **AWARE** (itemized iOS coverage) | RADAR-base (no maintained iOS passive app); platforms whose iOS columns are Unclear | These two document per-stream iOS coverage from primary sources; elsewhere the iOS column is Unclear or conflicting |
| Bridging research into clinical care | **mindLAMP** | Research-only platforms | Dual research/clinical design; Core service covers IRB and security-review language |
| Sophisticated no-code EMA/EMI/JITAI | **m-Path** or **LifeData** | Sensing-first platforms with thin EMA modules | Published JITAI support (m-Path); detailed scheduling and triggers (LifeData) |
| Context-triggered survey delivery | **MetricWire**, **LifeData**, **m-Path** | Schedule-only EMA tools | Each documents trigger-based delivery (vendor-described) |
| Clinical-trial-style assessment plus sensing, fully managed | **Avicenna Research** | Its test-only trial for real data; self-hosted platforms if no engineering capacity | Broad active-assessment features, fast data availability |
| Custom app on a proven sensing engine | **CARP Mobile Sensing** | Any team without Flutter capacity | MIT, cross-platform by design, wide wearable catalogue |
| Population-scale wearable and survey cohort, or secondary data | **Evidation** (sponsored) or **American Life in Realtime** data via USC's UAS Data Use Agreement | Expecting phone sensing or a self-service console | Member scale; ALiR is the academic route |
| Historical comparison or dataset reuse | **Purple Robot** (comparison only) / **StudentLife dataset** | Treating either as live for new data collection | Purple Robot unmaintained since 2016; StudentLife is a completed study |

---

## Cells changed in the 2026-10-10 rebuild (summary)

- Table 1: mindLAMP licence column filled (was "Not confirmed"); AWARE licence filled (Apache-2.0); Purple Robot status and licence (dormant since 2016, GPL-3.0); Evidation and an updated StudentLife row added; activity dates refreshed.
- Table 2: rebuilt with app-store columns. Beiwe parity changed from "not verified" to the wiki's OS split; RADAR-base iOS changed from "Yes" to no maintained passive app; AWARE counts corrected (19 of 33 on iOS, not 14) and App Store availability added; mindLAMP's stale iOS build recorded.
- Table 3: hosted-option column added. mindLAMP Core, CARP DTU-hosted service and m-Path External servers added; "Beiwe and RADAR-base only" replaced by four hosted routes; AWARE "not app stores" corrected for iOS.
- Table 6: academic-access column added. Avicenna trial now vendor-stated and test-only; MetricWire "trial offered" removed and Academic Site Licence added; mindLAMP Core pricing route added; m-Path add-on periods corrected (no stated billing period); Evidation row added.
- Table 7: Avicenna downgraded from Verified to Corroborated; MetricWire changed from "Not located" to vendor-stated ISO 27001, SOC 2 Type II, Part 11, HIPAA, GDPR; CARP GDPR roles added; mindLAMP privacy-page check added; Evidation row added.
- Table 8: keepalive column added; CARP portal assessed as a real dashboard; Avicenna gap notifications added.
- Tables 9 and 10: superlatives removed as listed under Table 9; Table 10 rows corrected for hosting and iOS sensing, and rows added for Evidation and iOS-heavy studies.

## Cells changed on 2026-10-11 (vendor fact records, batch 1)

- Table 2, Beiwe: Android column now says the APK is sideloaded from each deployment, Play listing still Unclear; parity cell notes SMS and calls come only from lab-distributed Android builds.
- Table 5, Beiwe: call and SMS build caveat and the optional Android ambient audio stream added. RADAR-base: "named partners" replaced by the shipped device list, the Fitbit cutoff, the unreleased Huawei connector and no Health Connect; openSMILE audio features added.
- Table 6: Beiwe BSC moved to the FY26 card ($2,640 + $8.40), FY24 marked superseded; RADAR-base (The Hyve) minimum term added; pointer to `../facts/_generated/research-and-access.md` added.
- Table 7: Beiwe lockout, BAA and DPA added. RADAR-base now shows The Hyve's ISO 27001 self-claim (Corroborated), retention, residency, AI-training and Play-declaration details.
- Table 9: RADAR-base "named wearable partners" replaced by the shipped catalogue.
