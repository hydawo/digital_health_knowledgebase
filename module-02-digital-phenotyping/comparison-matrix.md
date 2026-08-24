# Module 2 — Digital Phenotyping Comparison Matrix

**Last verified: 2026-08-24.** All cells reflect what is established in the individual profiles. Where
a profile records a fact as Unclear or not independently verified, the cell says so rather than
guessing. This module's research pass was a single session (not the two-pass depth Module 1
received), so **more cells here are "Not independently verified" than in the Module 1 matrix** —
that is a true reflection of thinner primary-source access this session, not an oversight to be
silently smoothed over.

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

---

## Table 2 — iOS / Android support (parity NOT assumed — see individual profiles)

| Platform | iOS | Android | Parity confirmed? |
|---|---|---|---|
| Beiwe | Yes, native app | Yes, native app | **Not independently verified this session** |
| RADAR-base | Yes | Yes | **Not independently verified this session** |
| mindLAMP | Yes | Yes | **Not independently verified this session** |
| AWARE Framework | Port exists, but **Verified (2026-08-24 second pass) at only ~14 of ~33 documented sensor modules — Locations/GPS, Applications, Communication, Installations, Keyboard, Screenshot, Screentext, and Telephony are Android-only** | Primary platform, full ~33-module catalog | **No — quantified and Verified, not just self-described** (see `profiles/aware-framework.md`) |
| Avicenna Research (Ethica) | Yes | Yes | **Not independently verified this session** |
| MetricWire | Yes | Yes | **Not independently verified this session** |
| m-Path | Yes (mobile app) | Yes (mobile app) | **Not independently verified this session** |
| CARP Mobile Sensing | Yes (Flutter cross-platform by design) | Yes (Flutter cross-platform by design) | Design goal stated; **not independently verified stream-by-stream** |
| Purple Robot | **No — Android only** | Yes, most complete Android sensor coverage cited in literature | N/A — no iOS |

**The one platform in this table with a self-documented iOS/Android gap is AWARE, and that gap is now
Verified and quantified** (second pass, 2026-08-24) rather than just self-described — notably,
**location data is Android-only**, ruling AWARE out for any iOS-inclusive study needing GPS. Every
other "not independently verified" cell reflects a genuine research-session limitation, not a claim
of parity — a future pass should verify each platform's developer documentation stream-by-stream
before this table is used to make an iOS-heavy or Android-heavy study design decision.

---

## Table 3 — Open source, self-hosting, and deployment model

| Platform | Open source | Self-hosting | Hosting requirement to run it |
|---|---|---|---|
| Beiwe | Yes (BSD-3) | Yes, on AWS (own account) | AWS + Django/Python expertise, **or** pay for the BSC managed service |
| RADAR-base | Yes (Apache 2.0) | Yes, Kafka-based backend | Institutional DevOps/data-engineering capacity — likely higher floor than Beiwe |
| mindLAMP | Yes | Yes (`LAMP-server`) | Not independently benchmarked |
| AWARE Framework | Yes (**Apache-2.0, confirmed 2026-08-24** on `aware-client` and named plugin repos) | Yes; distributed via GitHub, **not app stores** (permissions exceed store policy). No managed/SaaS hosting option found. | Sideloading/enterprise distribution needed for participants |
| Avicenna Research (Ethica) | No | **No** — vendor SaaS only | None — fully managed |
| MetricWire | No | **No** — vendor SaaS only | None — fully managed |
| m-Path | No | **No** — vendor SaaS only | None — fully managed |
| CARP Mobile Sensing | Yes (MIT) | N/A — it's a library, not a hosted service; **the adopting team builds and hosts their own app** | Flutter/Dart mobile-development capacity |

**Practical read:** the module splits cleanly into three deployment postures — (1) self-hosted
academic open source requiring real infrastructure capacity (Beiwe, RADAR-base, mindLAMP, AWARE),
(2) fully managed commercial SaaS requiring none (Avicenna Research, MetricWire, m-Path), and (3) a
build-your-own-app framework requiring mobile-development capacity rather than backend/DevOps
capacity (CARP). No platform in this module offers a documented, comparably-priced managed-hosting
option the way Labfront did for Garmin in Module 1 — **except Beiwe**, via the Beiwe Service Center.

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

---

## Table 5 — Passive sensing breadth (as documented; NOT independently bench-tested this session)

| Platform | Named passive streams | Wearable integration named |
|---|---|---|
| Beiwe | GPS, accelerometer, gyroscope, call logs, SMS logs, Wi-Fi, Bluetooth, screen/power state, audio samples | Not identified |
| RADAR-base | Accelerometer, location, audio (platform description); broader via device integrations | **Yes — Garmin, Huawei, Empatica, and others named as 2026 partners** |
| mindLAMP | Not independently itemized this session | Not established |
| AWARE Framework | **Itemized and Verified 2026-08-24**: ~33 documented sensor/plugin modules (accelerometer, barometer, battery, Bluetooth, gravity, gyroscope, light, locations, magnetometer, network, proximity, rotation, screen, temperature, WiFi, and more — see profile for full per-platform table) | Historically device-agnostic via plugins; no specific wearable integration itemized |
| Avicenna Research (Ethica) | "Wide range of smartphone sensors and wearables" (vendor framing, not itemized) | Yes, per vendor framing — not itemized |
| MetricWire | Passive sensor + geolocation capture (vendor framing, not itemized) | Not established |
| m-Path | GPS, Bluetooth, pedometer, environmental/noise context (m-Path sense module) | **Yes — "wearable triggers" named explicitly** |
| CARP Mobile Sensing | On-board phone sensors + attached wearables | **Yes — ECG monitor integration named specifically** |

---

## Table 6 — Pricing and service model

| Platform | Software cost | Hosting/service cost | Pricing public? |
|---|---|---|---|
| Beiwe (self-hosted) | Free | Own AWS bill | Infra cost not public; no licence fee |
| Beiwe (via BSC) | Free (same code) | **Quote-based**, methodology published: fixed fee by study duration (T) + variable fee by Active Participant Months (N × per-participant months) | Methodology yes; rate figures **no** |
| RADAR-base | Free | Own infra; no managed-hosting option identified | N/A |
| mindLAMP | Free | Not established | N/A |
| AWARE Framework | Free | Own infra; community-funded via Open Collective | N/A |
| Avicenna Research (Ethica) | N/A (SaaS) | **Non-public**; free trial reported by third-party directories | **No** |
| MetricWire | N/A (SaaS) | **Non-public**; trial offered | **No** |
| m-Path | N/A (SaaS) | **Non-public** — not established this session | **No** |
| CARP Mobile Sensing | Free (MIT) | Adopting team's own dev + infra cost | N/A |

**Five of eight active platforms have entirely non-public commercial pricing** (Avicenna Research,
MetricWire, m-Path, and — for the managed path specifically — Beiwe's BSC rate figures, plus
RADAR-base's unconfirmed managed-hosting-or-not question). Only Beiwe publishes its **pricing
methodology** (not rates); no platform in this module publishes actual rate figures the way Labfront
did in Module 1.

---

## Table 7 — Privacy, security, and compliance posture

| Platform | Documented encryption/security design | HIPAA/GDPR/SOC2 documentation located this session |
|---|---|---|
| Beiwe | **Yes — specific**: on-device, in-transit (RSA-AES hybrid), at-rest encryption; SHA-256/PBKDF2 identifier hashing with device-specific salts | **Not located** — flagged as open question |
| RADAR-base | Self-hosting emphasized for "in-hospital" privacy control (design framing, not a certification) | **Not located** |
| mindLAMP | Not established | **Not located**; clinical-use orientation makes this a first-order open question |
| AWARE Framework | Not established | **Not located** |
| Avicenna Research (Ethica) | Not established | **Not located** despite clinical-trial positioning |
| MetricWire | Not established | **Not located** despite stated CRO customer base |
| m-Path | Not established | **Not located** |
| CARP Mobile Sensing | **Yes — named framework feature**: privacy-preserving data-transformation pipeline | **Not located**; DTU/EU base makes GDPR a likely (not verified) design consideration |

**Every "Not located" in this table is a vendor/maintainer question, not an inference of
non-compliance.** See `../shared/unresolved-questions.md`.

---

## Table 8 — Study operations and management

| Platform | Researcher dashboard | Study-management depth | Multi-study/multi-site |
|---|---|---|---|
| Beiwe | Yes (part of `beiwe-backend`) | Study/participant/survey configuration confirmed; adherence monitoring depth not independently verified | Supported (one backend can host multiple studies) |
| RADAR-base | Yes ("Management Portal," referenced) | Not independently verified in depth | Consortium/multi-site origin (RADAR-CNS) suggests strong support |
| mindLAMP | Yes | Not independently verified in depth | Not established |
| AWARE Framework | **Not confirmed as existing** — framework may rely on external/custom tooling | N/A | N/A |
| Avicenna Research (Ethica) | Yes, explicitly named "Study Management" | Not independently itemized | Not established |
| MetricWire | Yes — real-time monitoring/analytics dashboard | Adherence/data-flow visibility implied | Not established |
| m-Path | Yes — no-code web study builder | Strong for EMA/EMI design specifically | Not established |
| CARP Mobile Sensing | **Not offered** — adopting team builds this | N/A | N/A |

---

## Table 9 — Meaningful differentiators, not feature lists

| Platform | The one thing it does that others in this module do not |
|---|---|
| **Beiwe** | The only platform with both a free self-hosted path *and* a documented paid managed-hosting alternative (BSC) run by the same lab that builds the software |
| **RADAR-base** | Kafka-based streaming architecture purpose-built for large multi-site, multi-modal (phone + wearable + IoT) consortium-scale studies |
| **mindLAMP** | Explicit dual research-*and*-clinical-care orientation, with cognitive/behavioral assessment tasks built into the platform's core identity |
| **AWARE Framework** | The longest-running, most plugin-extensible open-source sensing framework in the module, reflecting contributions from the widest range of independent academic groups |
| **Avicenna Research (Ethica)** | The most clinically-oriented commercial feature set (TeleVisit, cognitive/behavioral tasks) plus unusually specific export-format support (GEXF network graphs, KML location data) |
| **MetricWire** | Documented context/trigger-based survey deployment — surveys fired by sensed context, not only by schedule — plus built-in electronic consent |
| **m-Path** | The only platform in this module with a dedicated peer-reviewed methods paper *and* explicit, published JITAI (context-triggered intervention, not just prompt) support |
| **CARP Mobile Sensing** | The only genuinely library/framework-shaped option — a Flutter package a team builds its own app on top of, not a pre-built app to configure |

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
