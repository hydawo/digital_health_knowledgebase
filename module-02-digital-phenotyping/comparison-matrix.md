# Module 2 — Digital Phenotyping Comparison Matrix

**Last verified: 2026-08-25.** All cells reflect what is established in the individual profiles. Where
a profile records a fact as Unclear or not independently verified, the cell says so rather than
guessing. All eight platforms in this module have now had a second, direct-source-fetch verification
pass (AWARE/mindLAMP/MetricWire on 2026-08-24; Beiwe/RADAR-base/Avicenna Research/m-Path/CARP Mobile
Sensing on 2026-08-25) — a number of cells that read "Not independently verified this session" as of
2026-08-24 have since been resolved or materially narrowed; those are marked below. A residual set of
cells remain genuinely unresolved even after two passes (mostly non-public pricing and formal SOC 2/
Part 11 compliance detail) — those still say so rather than guessing.

Multiple tables are used deliberately. Do not read any single table as a ranking.

---

## Table 1 — Platform identity and status

| Platform | Organization | Type | Current status | License |
|---|---|---|---|---|
| **Beiwe** | Onnela Lab, Harvard T.H. Chan SPH | Academic open source + optional managed service (BSC) | Active | BSD-3-Clause |
| **RADAR-base** | King's College London + The Hyve | Academic/consortium open source | Active | Apache 2.0 |
| **mindLAMP** | BIDMC Division of Digital Psychiatry | Academic open source | Active. **Verified 2026-08-24: `LAMP-portal`/`LAMP-app` formally archived 2020-11-17; current successors are `LAMP-dashboard`/`LAMP-core-android`/`LAMP-core-ios`** | Not confirmed this session |
| **AWARE Framework** | International academic collaboration (orig. Univ. of Oulu) | Academic open source | Active (2026 commits) | Not confirmed this session |
| **Avicenna Research (Ethica)** | Avicenna Research (rebrand of Ethica Data) | Commercial SaaS | Active, renamed from Ethica | Closed source |
| **MetricWire** | MetricWire Inc. (Waterloo, Canada) | Commercial SaaS | Active, founded 2013 | Closed source |
| **m-Path** | KU Leuven-affiliated team | Commercial/academic hybrid SaaS | Active | Closed source (methodology published) |
| **CARP Mobile Sensing** | DTU (Bardram group) | Academic open-source framework/library | Active | MIT |
| **Purple Robot** | Northwestern CBITS / PHI Data Lab | Academic open source | **Legacy — maintenance status Unclear** | Not confirmed |
| **StudentLife** | Dartmouth | Historical study + dataset | **Discontinued as a platform; dataset remains in use** | N/A (dataset only) |
| **LifeData (RealLife Exp)** | LifeData, LLC (Marion, IN, USA) | Commercial SaaS | Active (app updates Apr–Aug 2026; new *LifeData+* generation shipped 2025–26 alongside the original) | Closed source (**Verified** — no GitHub org, no SDK) |

---

## Table 2 — iOS / Android support (parity NOT assumed — see individual profiles)

| Platform | iOS | Android | Parity confirmed? |
|---|---|---|---|
| Beiwe | Yes, native app | Yes, native app | **Not independently verified this session** |
| RADAR-base | Yes, but **Corroborated (2026-08-25 second pass): platform's own documentation states "substantial differences" exist and iOS availability is "more sparse... due to lack of background collection capabilities"** | Primary platform; 17-item itemized passive-sensor catalog Verified 2026-08-25 | **No — platform self-documents a gap, though the exact iOS-side item list was not itemized this pass** (see `profiles/radar-base.md`) |
| mindLAMP | Yes | Yes | **Not independently verified this session** |
| AWARE Framework | Port exists, but **Verified (2026-08-24 second pass) at only ~14 of ~33 documented sensor modules — Locations/GPS, Applications, Communication, Installations, Keyboard, Screenshot, Screentext, and Telephony are Android-only** | Primary platform, full ~33-module catalog | **No — quantified and Verified, not just self-described** (see `profiles/aware-framework.md`) |
| Avicenna Research (Ethica) | Yes | Yes | **Not independently verified this session** |
| MetricWire | Yes | Yes | **Not independently verified this session** |
| m-Path | Yes (mobile app) | Yes (mobile app) | **Not independently verified this session** |
| CARP Mobile Sensing | Yes (Flutter cross-platform by design) | Yes (Flutter cross-platform by design) | Design goal stated; **not independently verified stream-by-stream** |
| Purple Robot | **No — Android only** | Yes, most complete Android sensor coverage cited in literature | N/A — no iOS |
| LifeData (RealLife Exp) | Yes, native app | Yes, native app | **Not independently verified.** Two live generations; *LifeData+* requires **iOS 18.0+** |

**Two platforms in this table now have a self-documented iOS/Android gap, both Verified/Corroborated
via direct fetch rather than just self-described: AWARE (2026-08-24 second pass) and RADAR-base
(2026-08-25 second pass).** AWARE's gap is the more precisely quantified of the two — **location data
is Android-only**, ruling AWARE out for any iOS-inclusive study needing GPS. RADAR-base's own
documentation names the same underlying cause (iOS background-execution limits) but without an
itemized per-sensor iOS list, so it is Corroborated rather than fully Verified at the per-stream
level. Every other "not independently verified" cell reflects a genuine research-session limitation,
not a claim of parity — a future pass should verify each remaining platform's developer documentation
stream-by-stream before this table is used to make an iOS-heavy or Android-heavy study design
decision.

---

## Table 3 — Open source, self-hosting, and deployment model

| Platform | Open source | Self-hosting | Hosting requirement to run it |
|---|---|---|---|
| Beiwe | Yes (BSD-3) | Yes, on AWS (own account) | AWS + Django/Python expertise, **or** pay for the BSC managed service (now with published rates — see Table 6) |
| RADAR-base | Yes (Apache 2.0) | Yes, Kafka-based backend, **or** a confirmed managed-hosting alternative, **"RADAR-base as a Service" via The Hyve (Verified 2026-08-25)** | Institutional DevOps/data-engineering capacity for self-hosting — likely higher floor than Beiwe — **or** no infrastructure capacity needed via The Hyve's managed service (best suited to studies of ~200 participants or fewer per the vendor's own guidance) |
| mindLAMP | Yes | Yes (`LAMP-server`) | Not independently benchmarked |
| AWARE Framework | Yes (**Apache-2.0, confirmed 2026-08-24** on `aware-client` and named plugin repos) | Yes; distributed via GitHub, **not app stores** (permissions exceed store policy). No managed/SaaS hosting option found. | Sideloading/enterprise distribution needed for participants |
| Avicenna Research (Ethica) | No | **No** — vendor SaaS only | None — fully managed |
| MetricWire | No | **No** — vendor SaaS only | None — fully managed |
| m-Path | No | **No** — vendor SaaS only | None — fully managed |
| CARP Mobile Sensing | Yes (MIT) | N/A for the CAMS sensing library — **but a `carp-portal` repository (Verified 2026-08-25) indicates a study-management portal component exists within the broader CARP ecosystem**, of unconfirmed maturity | Flutter/Dart mobile-development capacity for the CAMS app itself |
| LifeData (RealLife Exp) | No | No | Vendor SaaS only; **US-only data residency**, hosted on Microsoft Azure (named in the privacy policy) |

**Practical read:** the module splits cleanly into three deployment postures — (1) self-hosted
academic open source requiring real infrastructure capacity (Beiwe, RADAR-base, mindLAMP, AWARE),
(2) fully managed commercial SaaS requiring none (Avicenna Research, MetricWire, m-Path), and (3) a
build-your-own-app framework requiring mobile-development capacity rather than backend/DevOps
capacity (CARP). **Updated 2026-08-25:** two platforms in this module now offer a documented
managed-hosting alternative to self-hosting — Beiwe (via the Beiwe Service Center, with published
rates) and RADAR-base (via The Hyve's "RADAR-base as a Service," pricing still non-public). This was
previously described as "except Beiwe" only; RADAR-base's managed-hosting option was resolved this
second pass.

---

## Table 4 — Active data collection (EMA/survey) sophistication

| Platform | Surveys/EMA | Distinctive active-collection feature |
|---|---|---|
| Beiwe | Yes, scheduled, incl. audio-recording items | Simpler EMA model; branching-logic depth not independently verified |
| RADAR-base | Yes — PROM/questionnaire delivery | Not independently verified in depth |
| mindLAMP | Yes — surveys + **cognitive/behavioral tasks** | "Assess/Manage" clinical-assessment orientation baked into platform identity |
| AWARE Framework | Yes — **Verified 2026-08-24**: a native ESM/EMA sensor module, on both Android and iOS | Framework's core identity is passive sensing; scheduling/branching sophistication not benchmarked against Beiwe/mindLAMP |
| Avicenna Research (Ethica) | Yes — surveys, cognitive/behavioral tasks, **TeleVisit** | Broadest clinical-trial-style active-assessment feature set in this module |
| MetricWire | Yes — mobile diaries, **context/trigger-based survey deployment** | Documented sensor-context-triggered (not just scheduled) survey firing |
| m-Path | Yes — core platform identity; **explicit JITAI support** | No-code EMA/EMI design; the most EMA-sophistication-forward platform here |
| CARP Mobile Sensing | Not a core framework feature; would be built by the adopting team | N/A — sensing-first framework |
| LifeData (RealLife Exp) | Yes — **the deepest documented scheduling engine in this module**: fixed/random/triggered/event-based with configurable minimum inter-prompt spacing, branching, display logic, piped text, computed scores, 13 question types, offline collection, RTL languages | A trigger type that activates an **entire new schedule**, making it EMI/JITAI-adjacent without custom code |

---

## Table 5 — Passive sensing breadth (as documented; NOT independently bench-tested this session)

| Platform | Named passive streams | Wearable integration named |
|---|---|---|
| Beiwe | GPS, accelerometer, gyroscope, call logs, SMS logs, Wi-Fi, Bluetooth, screen/power state, audio samples | Not identified |
| RADAR-base | **Itemized and Verified 2026-08-25**: 17 documented Android passive streams (relative location, acceleration, gyration, magnetic field, step count, light, Bluetooth device counts, activity recognition, sleep events, phone lock/unlock, app usage, call log, SMS log, contact-list changes, battery, local weather, connection monitoring) — see profile for iOS-availability caveat | **Yes — Garmin, Huawei, Empatica, and others named as 2026 partners** |
| mindLAMP | Not independently itemized this session | Not established |
| AWARE Framework | **Itemized and Verified 2026-08-24**: ~33 documented sensor/plugin modules (accelerometer, barometer, battery, Bluetooth, gravity, gyroscope, light, locations, magnetometer, network, proximity, rotation, screen, temperature, WiFi, and more — see profile for full per-platform table) | Historically device-agnostic via plugins; no specific wearable integration itemized |
| Avicenna Research (Ethica) | "Wide range of smartphone sensors and wearables" (vendor framing, not itemized) | Yes, per vendor framing — not itemized |
| MetricWire | Passive sensor + geolocation capture (vendor framing, not itemized) | Not established |
| m-Path | GPS, Bluetooth, pedometer, environmental/noise context (m-Path sense module — **confirmed 2026-08-25 as a separately priced add-on, €3,000–€10,000/year, not included in base subscription**) | **Yes — "wearable triggers" named explicitly; a distinct "Smartwatch Integration" add-on (€3,000) was also found 2026-08-25** |
| CARP Mobile Sensing | On-board phone sensors + attached wearables; **confirmed integration with Apple Health and Google Health Connect (Verified 2026-08-25)** | **Itemized and Verified 2026-08-25**: Movisens (Move4/EcgMove4/EdaMove4), eSense earplug, Polar (H10/Verity Sense), Movesense (MD/Active), Dexcom G7 CGM — materially broader than the prior "ECG monitor" reference |
| **LifeData (RealLife Exp)** | **Response-linked GPS only** — captured *with* a survey response, not continuously. **No accelerometer, screen/app usage, communication metadata, Bluetooth, Wi-Fi or audio.** Corroborated across 5 vendor pages, 2 app-store listings and 2 Play data-safety declarations | **None documented** — no wearable, HealthKit, Health Connect or FHIR integration anywhere |

---

## Table 6 — Pricing and service model

| Platform | Software cost | Hosting/service cost | Pricing public? |
|---|---|---|---|
| Beiwe (self-hosted) | Free | Own AWS bill | Infra cost not public; no licence fee |
| Beiwe (via BSC) | Free (same code) | **Verified 2026-08-25: $1,937/month fixed + $6/Active Participant Month variable**; worked examples total $24,144–$27,564 | **Yes — actual rates published**, resolving what was the module's clearest "methodology only" gap |
| RADAR-base (self-hosted) | Free | Own infra | N/A |
| RADAR-base (via The Hyve, "RADAR-base as a Service") | Free (same code) | **Confirmed to exist 2026-08-25**; GDPR-compliant cloud hosting, 2–4 week setup, best suited to ≤~200 participants (single-server) | Offering confirmed; **rate figures no** |
| mindLAMP | Free | Not established | N/A |
| AWARE Framework | Free | Own infra; community-funded via Open Collective | N/A |
| Avicenna Research (Ethica) | N/A (SaaS) | **Non-public**; free trial reported by third-party directories (re-confirmed non-public 2026-08-25) | **No** |
| MetricWire | N/A (SaaS) | **Non-public**; trial offered | **No** |
| m-Path | N/A (SaaS) | **Verified 2026-08-25: fully public, itemized tiers** — Free (€0/50 participants), Essential (€1,599–€2,958), Standard (€2,099–€3,616), Comfort (€3,099–€5,338), plus separately priced add-ons (Sensing Lite €3,000, Sensing Full €10,000, API Access €5,000, Smartwatch Integration €3,000, and others) | **Yes — the most granular published pricing in this module** |
| CARP Mobile Sensing | Free (MIT) | Adopting team's own dev + infra cost | N/A |
| LifeData (RealLife Exp) | Not public — no `/pricing` page; the *formula* is described, the figures are not | Not public; heaviest paid-services menu in the module (10 named services incl. protocol building, UAT, site training) | **No** |

**Updated 2026-08-25: only two of eight active platforms now have entirely non-public commercial
pricing (Avicenna Research and MetricWire).** m-Path's pricing, previously "not established," is now
the most granular and fully itemized in the module (base tiers plus per-feature add-ons). Beiwe's BSC
rates are now public (resolving unresolved-question #85). RADAR-base has a confirmed managed-hosting
offering but its rates remain non-public (resolving the *existence* half of unresolved-question #86,
not the pricing half).

---

## Table 7 — Privacy, security, and compliance posture

| Platform | Documented encryption/security design | HIPAA/GDPR/SOC2 documentation located this session |
|---|---|---|
| Beiwe | **Yes — specific**: on-device, in-transit (RSA-AES hybrid), at-rest encryption; SHA-256/PBKDF2 identifier hashing with device-specific salts | HIPAA-*applicability* language found 2026-08-25 ("may interact with laws covering PII or PHI like HIPAA") — **not a certification claim**. GDPR/SOC2 still not located |
| RADAR-base | Self-hosting emphasized for "in-hospital" privacy control (design framing, not a certification); managed-hosting option (The Hyve) commits to "GDPR-compliant public cloud" **hosting infrastructure** specifically (Verified 2026-08-25) | HIPAA/SOC2/ISO **not located** even after second pass; the GDPR language found is about the hosting environment, not a RADAR-base compliance certification |
| mindLAMP | Not established | **Not located**; clinical-use orientation makes this a first-order open question |
| AWARE Framework | Not established | **Not located** |
| Avicenna Research (Ethica) | AES-256 encryption at rest, stated on the vendor's legal page (Verified 2026-08-25) | **Materially resolved 2026-08-25**: **ISO 27001:2022 certified** (Verified — certified Nov 2024, zero-nonconformity surveillance audit Nov 2025); detailed HIPAA Privacy/Security Rule and UK GDPR/EU GDPR/PIPEDA language for minors' data (Corroborated — vendor-stated, not independently audited in what this session accessed). SOC 2 and 21 CFR Part 11 status **still not located** |
| MetricWire | Not established | **Not located** despite stated CRO customer base |
| m-Path | Not established | **Corroborated 2026-08-25**: vendor's own homepage states "compliant with GDPR and HIPAA" — a specific, findable claim, but self-declared rather than independently audited (contrast Avicenna Research's dated ISO 27001 certificate, which this session treats as the stronger evidence tier). SOC2/ISO/DPA-template **not located** |
| CARP Mobile Sensing | **Yes — named framework feature**: privacy-preserving data-transformation pipeline | **Not located**; DTU/EU base makes GDPR a likely (not verified) design consideration |
| LifeData (RealLife Exp) | Partial — US-only residency and Azure hosting named; **no public data dictionary, export schema or permission model** (help centre entirely login-gated; the worst documentation opacity in this module) | **Unclear — a real conflict.** Marketing asserts "HIPAA & GDPR compliant" on 4+ pages (one misspells it "HIPPA"), but the privacy policy and terms **mention HIPAA zero times** — no BAA, no Security/Privacy Rule language. **SOC 2, ISO 27001 and 21 CFR Part 11 appear nowhere**, despite a marketed "Clinical" eCOA tier. What *is* documented: **EU-U.S. / UK / Swiss Data Privacy Framework self-certification**, FTC jurisdiction, GDPR-processor role. Retention/deletion terms are **numeric and Verified** (180 d / ≤30 d / 12-month inactivity) — the most specific in the module |

**Updated 2026-08-25: this is no longer a uniform "not located" table.** Avicenna Research now has
the strongest compliance evidence in the module (an independently audited, dated ISO 27001:2022
certificate), and m-Path and Beiwe both have specific, sourced language distinguishing a vendor's own
compliance *claim* (m-Path: "compliant with GDPR and HIPAA," Corroborated) from mere legal-applicability
acknowledgment (Beiwe: "may interact with laws covering... HIPAA," not a compliance claim at all).
**Every remaining "Not located" in this table is still a vendor/maintainer question, not an inference
of non-compliance.** See `../shared/unresolved-questions.md`.

---

## Table 8 — Study operations and management

| Platform | Researcher dashboard | Study-management depth | Multi-study/multi-site |
|---|---|---|---|
| Beiwe | Yes (part of `beiwe-backend`) | Study/participant/survey configuration confirmed; adherence monitoring depth not independently verified | Supported (one backend can host multiple studies) |
| RADAR-base | Yes — **Verified 2026-08-25**: `ManagementPortal` is an actively maintained GitHub repository (Apache-2.0), not just a referenced concept | Not independently verified in depth beyond confirming the repo's existence and active status | Consortium/multi-site origin (RADAR-CNS) suggests strong support |
| mindLAMP | Yes | Not independently verified in depth | Not established |
| AWARE Framework | **Not confirmed as existing** — framework may rely on external/custom tooling | N/A | N/A |
| Avicenna Research (Ethica) | Yes, explicitly named "Study Management" | Not independently itemized | Not established |
| MetricWire | Yes — real-time monitoring/analytics dashboard | Adherence/data-flow visibility implied | Not established |
| m-Path | Yes — no-code web study builder | Strong for EMA/EMI design specifically; **API Access is a separate €5,000/year add-on (Verified 2026-08-25), not included by default** | Not established |
| CARP Mobile Sensing | **Revised 2026-08-25**: a `carp-portal` repository exists within the `carp-dk` organization, indicating a dashboard component is part of the ecosystem — but its maturity/completeness is unconfirmed, so "not offered" is no longer accurate | N/A — not independently assessed | N/A |
| LifeData (RealLife Exp) | Yes — real-time engagement and response-rate dashboards, smart reminders, alerts on responses/scores/events | Web builder, roles/permissions, QR/link/code onboarding, researcher-assigned IDs | Yes — institutional master subscriptions with department sub-accounts; multi-site on the Clinical tier |

---

## Table 9 — Meaningful differentiators, not feature lists

| Platform | The one thing it does that others in this module do not |
|---|---|
| **Beiwe** | The only platform with both a free self-hosted path *and* a documented paid managed-hosting alternative (BSC) run by the same lab that builds the software |
| **RADAR-base** | Kafka-based streaming architecture purpose-built for large multi-site, multi-modal (phone + wearable + IoT) consortium-scale studies |
| **mindLAMP** | Explicit dual research-*and*-clinical-care orientation, with cognitive/behavioral assessment tasks built into the platform's core identity |
| **AWARE Framework** | The longest-running, most plugin-extensible open-source sensing framework in the module, reflecting contributions from the widest range of independent academic groups |
| **Avicenna Research (Ethica)** | The most clinically-oriented commercial feature set (TeleVisit, cognitive/behavioral tasks) plus unusually specific export-format support (GEXF network graphs, KML location data) **and, as of 2026-08-25, the only independently audited compliance certification (ISO 27001:2022) confirmed anywhere in this module** |
| **MetricWire** | Documented context/trigger-based survey deployment — surveys fired by sensed context, not only by schedule — plus built-in electronic consent |
| **m-Path** | The only platform in this module with a dedicated peer-reviewed methods paper *and* explicit, published JITAI (context-triggered intervention, not just prompt) support; **as of 2026-08-25, also the only platform with fully public, itemized à-la-carte pricing (base tiers plus priced add-ons for sensing, API access, and wearable integration)** |
| **CARP Mobile Sensing** | The only genuinely library/framework-shaped option — a Flutter package a team builds its own app on top of, not a pre-built app to configure; **as of 2026-08-25, also the only platform in this module with confirmed native Apple Health and Google Health Connect integration** |
| **LifeData (RealLife Exp)** | Sells **audit trails as bespoke service work rather than a shipped feature** — and pairs the module's deepest survey-scheduling engine with essentially **no passive sensing at all**, making it the clearest case in this module of an EMA/ePRO tool sitting inside a digital-phenotyping comparison |

---

## Table 10 — Choosing by research need

| If your primary need is… | Consider | Be cautious of | Why |
|---|---|---|---|
| Full data custody, algorithmic transparency, willing to run AWS | **Beiwe** (self-hosted) | Vendor SaaS platforms | BSD-3, self-hostable, established analysis package (Forest) |
| No in-house infrastructure capacity, still want an open-source lineage | **Beiwe via BSC** | RADAR-base (no confirmed managed-hosting option) | BSC absorbs the infrastructure burden for a quoted fee |
| Large multi-site, multi-country, multi-modal consortium study | **RADAR-base** | Beiwe (single-lab scale by default) | Kafka streaming, IoT gateway, EU consortium origin |
| Bridging research into actual clinical care | **mindLAMP** | Purely research-only platforms | Explicit dual research/clinical design; verify current component status first |
| Sophisticated no-code EMA/EMI/JITAI design | **m-Path** | Sensing-first platforms with thin EMA modules | Published methods paper; explicit JITAI support |
| Context/trigger-based (not just scheduled) survey delivery | **MetricWire** | Purely schedule-based EMA tools | Explicitly documented trigger-based deployment |
| Clinical-trial-style outcome assessment plus sensing, fully managed | **Avicenna Research (Ethica)** | Self-hosted academic platforms if no engineering capacity | Broad active-assessment feature set, fast data availability |
| Full custom mobile app built on a proven sensing engine | **CARP Mobile Sensing** | Any dashboard-configured product, if the team lacks Flutter capacity | MIT-licensed, genuinely cross-platform by design |
| Android-only legacy comparison or historical dataset reuse | **Purple Robot** (comparison context) / **StudentLife dataset** | Treating either as a live platform for new data collection | Purple Robot's live status is Unclear; StudentLife is a completed study, not a tool |
