# Shared Terminology

Definitions used consistently across all modules. Where the field uses a term loosely, the
knowledge base commits to one meaning and says so.

---

## Evidence confidence labels

| Label | Meaning |
|---|---|
| **Verified** | Directly supported by a current authoritative primary source read during the research session |
| **Corroborated** | Supported by multiple credible sources but not clearly established in current primary documentation |
| **Reported** | Found in a credible source but not independently confirmed. Vendor marketing claims default to this |
| **Unclear** | Available evidence is incomplete, conflicting, or ambiguous |

**Vendor engineering claims are Reported, not Verified**, no matter how specific the number. A
vendor blog stating "31% improvement in nighttime heart rate tracking" is a claim about a
measurement, not a measurement.

---

## Data granularity

| Term | Meaning in this knowledge base |
|---|---|
| **Raw signal** | Unprocessed sensor output at or near the sensor's native sampling rate — PPG waveform, accelerometer samples in g, ECG voltage samples, EDA in microsiemens. **Not** "raw" in the loose vendor sense of "data we haven't summarized into a score" |
| **Derived / processed metric** | Any output of a vendor algorithm: sleep stages, sleep score, readiness, strain, recovery, stress, Body Battery, HRV summaries, step counts |
| **Intraday / time series** | Within-day values at a fixed epoch (1 s, 1 min, 5 min, 15 min). Between raw and daily summary. Not raw |
| **Daily summary** | One value per day per metric |
| **Epoch** | The aggregation window for a time series. Actigraphy convention is 60 s, 30 s, or 15 s |
| **Activity counts** | The classical actigraphy unit — a device-specific integration of acceleration over an epoch. **Counts are not comparable across manufacturers** unless explicitly harmonized |

**The single most important distinction in Module 1**: a device having a sensor tells you nothing
about whether you can get the signal. Always ask which of the four rows above you are being offered.

---

## Physiological signals and metrics

| Term | Definition | Research caveat |
|---|---|---|
| **PPG** | Photoplethysmography — optical detection of blood volume changes. Green LEDs for HR; red and infrared for SpO2 | Degrades under motion; affected by skin tone, perfusion, tattoos, and fit |
| **ECG** | Electrocardiography — electrical cardiac activity. Consumer wearables provide single-lead, user-initiated, ~30 s recordings | Not continuous. Not diagnostic-equivalent to 12-lead |
| **HR** | Heart rate, beats per minute. On consumer wearables usually a smoothed PPG-derived estimate at an intermittent, non-configurable duty cycle | Ambient sampling rates are typically undocumented and vary with device state |
| **IBI / RR interval** | Inter-beat interval — time between consecutive heartbeats. From ECG these are true RR intervals | The substrate for HRV. Availability is rare: Garmin (BBI), Samsung (IBI), Polar (RR/PPI) |
| **PPI** | Peak-to-peak interval derived from PPG rather than ECG. An approximation of RR | Not interchangeable with RR for HRV analysis; more artefact-prone |
| **HRV** | Heart rate variability. Time-domain (RMSSD, SDNN), frequency-domain, or nonlinear | **Vendor HRV numbers are not comparable across brands.** Different windows (overnight vs 5-min), different metrics, different artefact correction |
| **SpO2** | Peripheral oxygen saturation from red/IR PPG | Consumer SpO2 is generally wellness-labelled, not medical-grade, and degrades at low saturation |
| **EDA / GSR** | Electrodermal activity — skin conductance, an index of sympathetic arousal. **SCL** is the tonic level; **SCR** are phasic responses | Wrist EDA has fewer eccrine glands and more artefact than palmar. Only Empatica offers it as raw research data in Module 1 |
| **Skin temperature** | Peripheral temperature at the wrist or finger | **Not core body temperature.** Strongly influenced by ambient temperature and vasomotor state. Usually reported as a nightly deviation from personal baseline, not an absolute |
| **Energy expenditure (EE)** | Calories burned, estimated from HR and/or acceleration | **No consumer brand achieves acceptable accuracy.** Do not use as a primary endpoint |
| **VO2max** | Estimated maximal oxygen uptake, inferred from HR–pace relationships | An estimate from an estimate; requires running/walking data to compute |

---

## Sleep terminology

| Term | Definition | Caveat |
|---|---|---|
| **PSG** | Polysomnography — the reference standard, EEG-based | The only true criterion for sleep staging |
| **Sleep staging** | Classification into wake / light (N1–N2) / deep (N3) / REM | Requires EEG to do properly. Wearables infer it from HR, HRV, and movement. **Deep-sleep sensitivity across tested consumer devices ranges from 32% to 80%** |
| **Sleep–wake detection** | Binary asleep/awake classification | Classical actigraphy does this (Cole-Kripke, Sadeh) and does it reasonably well. It cannot stage |
| **TST** | Total sleep time | |
| **SE** | Sleep efficiency — TST as a proportion of time in bed | |
| **WASO** | Wake after sleep onset | |
| **Sensitivity / specificity** | For sleep staging, sensitivity for a stage = proportion of true epochs of that stage correctly identified | Devices with high overall accuracy can still have very poor deep-sleep or REM sensitivity |
| **Cohen's kappa** | Agreement corrected for chance | The right summary statistic for multi-stage agreement; raw "accuracy" is misleading when stages are imbalanced |

**Actigraphy answers "when were they asleep." PPG wearables attempt "what stage were they in."
These are different questions with different evidence bases.** Do not treat a device's actigraphic
credibility as staging credibility, or vice versa.

---

## Access, API, and platform terms

| Term | Meaning |
|---|---|
| **OAuth 2.0** | The near-universal delegated-authorization pattern. The participant authorizes your application against their vendor account |
| **Scope** | The unit of consent. Participants may grant some and deny others, producing structurally missing data that looks like non-wear |
| **Personal Access Token (PAT)** | A long-lived token for accessing one's own account. Convenient for pilots; **Oura deprecated these in December 2025** |
| **Webhook** | Vendor push notification on new data. Generally preferable to polling |
| **Ping/Pull** | Vendor notifies that data exists; you fetch it |
| **Push** | Vendor delivers the data itself to your endpoint |
| **Backfill** | Retrieval of data predating the participant's authorization |
| **Rate limit** | Request ceiling. **Critically, some are per user (Fitbit: 150/hr/user) and some per application (WHOOP: 10,000/day/client).** Per-client limits impose a hard ceiling on study size |
| **Intraday approval** | Fitbit's case-by-case gate on minute-level data for non-personal applications |
| **Restricted scope** | Google Health API classification requiring privacy and security review for all scopes |
| **BYOD** | Bring your own device — participants use hardware they already own. Cheap and high-retention; introduces device-model confounding and socioeconomic selection bias |
| **Provisioned device** | Study-supplied hardware. Controls the instrument; adds procurement, shipping, fitting, charging support, and recovery logistics |
| **Unified API** | A third-party layer normalizing several vendor APIs behind one schema. Cannot exceed the underlying vendors' data, and hides algorithm heterogeneity |

---

## Study operations

| Term | Meaning |
|---|---|
| **Wear time / non-wear** | Periods the device was actually on the body. Detected by movement, temperature, or capacitive sensing. **Non-wear filtering materially changes results** and must be pre-specified |
| **Adherence monitoring** | Researcher-side visibility into whether participants are wearing and syncing, *during* the study. Impossible with Axivity/GENEActiv; native in Empatica and Ametris; bought from Fitabase for Fitbit/Garmin |
| **Sync dependency** | Whether data reaching the researcher requires participant action. Oura's sleep data requires the participant to open the app; this is a design constraint, not a bug |
| **Silent degradation** | An API returning something plausible but wrong rather than an error — e.g. Fitbit returning summary data instead of intraday when the request exceeds 24 hours |
| **JITAI** | Just-in-time adaptive intervention. Requires real-time or near-real-time data; rules out platforms without live access (e.g. Empatica's research platform) |
| **Hawthorne / reactivity confound** | Behaviour change caused by the measurement device itself. Screenless (WHOOP) and screen-free research devices (ActiGraph, Axivity) minimize this; feedback-rich smartwatches maximize it |

---

## Compliance and governance

| Term | Meaning |
|---|---|
| **HIPAA** | US health privacy law. Relevant only where the entity is a covered entity or business associate |
| **BAA** | Business Associate Agreement. Required before a vendor may handle PHI on a covered entity's behalf. **Never infer a BAA from a "HIPAA-compliant" marketing claim** |
| **GDPR** | EU data protection regulation |
| **DPA** | Data Processing Agreement, GDPR's analogue to a BAA |
| **SOC 2** | Security controls attestation (Type I: design; Type II: operating effectiveness) |
| **De-identification** | Removing identifiers. Distinct from a BAA: a platform may de-identify precisely so it never handles PHI, and therefore never needs a BAA |
| **Data residency** | The jurisdiction where data is stored |
| **Data custody** | Who physically holds the data. Note that Apple, Samsung's Privileged SDK, Polar's BLE SDK, and Axivity/GENEActiv all permit full institutional custody with **no vendor in the data path at all** |
| **SaMD** | Software as a Medical Device |
| **510(k) clearance** | US FDA clearance route. Applies to a specific device and a specific indication — **"FDA-cleared" without an indication statement is close to meaningless** |

---

## Terms used loosely in the field, and how this knowledge base uses them

| Loose usage | Our usage |
|---|---|
| "Raw data" meaning "data before we made a score out of it" | Reserved for near-native-rate sensor output only |
| "Research-grade" as a marketing adjective | Used only where raw data is available **and** either a regulatory clearance or a substantial independent validation literature exists |
| "Validated" meaning "the vendor ran a study" | Split into vendor-authored (**Reported**) and independent peer-reviewed (**Corroborated**) |
| "API access" meaning any programmatic route | Distinguished into cloud REST API, mobile SDK, on-device framework, and file export — these have completely different operational profiles |
| "HIPAA compliant" | Treated as a vendor claim requiring a BAA to be actionable |

---

## Module 2 — Digital phenotyping platform terms

| Term | Definition | Research caveat |
|---|---|---|
| **Digital phenotyping** | The moment-by-moment quantification of human behavior in situ using data from smartphones and other personal digital devices (the term originates with Onnela and Torous, Beiwe's and mindLAMP's respective originating labs) | Distinguish from "digital biomarker," which usually implies a specific validated clinical measure — digital phenotyping is the broader behavioral-quantification framing |
| **Passive sensing** | Data collected from phone sensors/usage without requiring participant action beyond carrying the phone (GPS, accelerometer, call/SMS metadata, screen state, app usage, Bluetooth/Wi-Fi proximity) | iOS background-execution limits materially constrain passive sensing relative to Android for several stream types — **never assume iOS/Android parity for any passive stream** |
| **Active data collection** | Data requiring deliberate participant input: surveys, EMA/ESM prompts, cognitive/behavioral tasks, audio diaries | Distinguished in this module from passive sensing throughout; a platform's strength in one does not imply strength in the other (e.g., AWARE is passive-sensing-first with no confirmed first-party EMA module; m-Path is EMA-first with sensing as an add-on module) |
| **EMA / ESM** | Ecological Momentary Assessment / Experience Sampling Method — repeated, in-the-moment self-report prompts, typically scheduled, randomized, or event/context-triggered | "Context-triggered" (firing a prompt based on sensed context, e.g. location or detected activity) is a materially more sophisticated capability than fixed-schedule delivery, and not every platform in this module documents it (MetricWire explicitly does) |
| **EMI** | Ecological Momentary Intervention — delivering an intervention (not just an assessment prompt) in the moment, based on context | The active-delivery counterpart to EMA; see JITAI below |
| **JITAI** | Just-in-time adaptive intervention — an intervention delivered when sensed context indicates it is needed, adapting over time. Already defined in Module 1's terminology as requiring real-time/near-real-time data access | m-Path is the platform in this module with the most explicitly documented, peer-reviewed JITAI support |
| **Self-hosted vs. managed vs. SaaS** | **Self-hosted**: the research team runs the backend on its own infrastructure (Beiwe, RADAR-base, mindLAMP, AWARE all support this). **Managed**: the platform's own developers run a paid hosted instance on the research team's behalf (Beiwe Service Center is the only clearly documented example in this module). **SaaS**: a commercial vendor's own multi-tenant cloud, with no self-hosting option (Avicenna Research, MetricWire, m-Path) | These are three distinct cost/control tradeoffs, not points on one spectrum — a "self-hosted" platform with no managed option and a "SaaS-only" platform with no self-hosting option fail differently for a team with the wrong capacity profile |
| **Framework / library (vs. product)** | A codebase (e.g., CARP Mobile Sensing's `carp_mobile_sensing` Flutter package) that a research team integrates into its **own** custom-built app, as opposed to a pre-built app the team configures through a dashboard | Requires mobile-development capacity rather than backend/DevOps capacity — a genuinely different adoption cost axis than the self-hosted/managed/SaaS distinction above |
| **Active Participant Month** | Beiwe Service Center's specific billing unit: one participant collecting data for one month. Total study cost scales with (participants × months), plus a separate fixed fee scaled to overall study duration | The only publicly documented pricing *methodology* — as distinct from actual rate figures — found for any managed/SaaS platform in this module |
| **Data transformer / privacy-preserving transformation** | A pipeline-stage capability (documented as a first-class feature of CARP Mobile Sensing) that converts collected data to a standardized format and/or applies anonymization or aggregation before storage | Not confirmed as a first-class, documented feature of any other platform in this module — most likely handled as custom per-study engineering elsewhere |
