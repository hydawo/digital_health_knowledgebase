# Module 1 — Wearables Comparison Matrix

**Last verified: 2026-08-21.** All cells reflect the state established in the individual profiles;
where a profile records a fact as Unclear, the cell says so rather than guessing.

Multiple tables are used deliberately. Do not attempt to read any single table as a ranking.

---

## Table 1 — Ecosystem orientation and access model

| Ecosystem | Primary orientation | Access model | Vendor cloud in data path? | Approval required? | Self-serve? |
|---|---|---|---|---|---|
| **Apple** | Consumer | Researcher-built iOS app reading HealthKit | **No** — Apple never receives study data | SensorKit only (IRB + Apple review) | HealthKit yes; SensorKit no |
| **Fitbit / Google** | Consumer | Public REST API (migrating to Google Health API) | Yes | Intraday: yes. Google Health scopes: **all Restricted** | Partly |
| **Garmin** | Consumer/athletic | Health API (cloud) **or** Health SDK (mobile, can bypass cloud) | API yes; Standard SDK no | Yes — enterprise program application | No |
| **Oura** | Consumer | Public REST API + webhooks | Yes | **Yes above 10 users** | Up to 10 users |
| **WHOOP** | Consumer | REST API v2 + webhooks | Yes | App approval before launch | Partly |
| **Samsung** | Consumer | Privileged Health SDK (on-device) + Research Stack (self-deployed) | **No** for Privileged SDK path | Yes — Samsung Partner Program | No |
| **Polar** | Athletic/research | **Open BLE SDK (GitHub)** or AccessLink API | **No** for BLE path | **None for BLE SDK** | **Yes** |
| **Withings** | Medical-grade home health | Public Health Data API; Advanced Research API | Yes | **Yes — contracted partners only** for raw | Partly |
| **Empatica** | **Research/medical** | Care Portal export | Yes | Commercial engagement | No |
| **Ametris (ActiGraph)** | **Clinical trials** | CentrePoint platform + API; ActiLife offline | Optional (ActiLife is offline) | Commercial engagement | No |
| **Axivity / GENEActiv** | **Research** | **USB download. No cloud, no API, no account** | **No** | **None** | **Yes** |

---

## Table 2 — Sensors present (device-dependent within each ecosystem)

✓ = present on at least the flagship device. — = absent.

| Ecosystem | PPG | ECG | Accel | Gyro | Temp | SpO2 | GPS | Baro | EDA | BIA |
|---|---|---|---|---|---|---|---|---|---|---|
| Apple Watch | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — |
| Fitbit / Pixel Watch | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | some | ✓ (Sense) | — |
| Garmin | ✓ | some | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — |
| Oura Ring 4 | ✓ | — | ✓ | — | ✓ | ✓ | — | — | — | — |
| WHOOP 5.0 / MG | ✓ | ✓ (MG) | ✓ | — | ✓ | ✓ | — | — | — | — |
| Samsung Galaxy Watch8 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ |
| Polar H10 | — | ✓ | ✓ | — | — | — | — | — | — | — |
| Movesense MD / Flash / HR2 | — | ✓ | ✓ | ✓ | ✓ | — | — | — | — | — |
| Ultrahuman Ring AIR | ✓ | — | ✓ | — | ✓ | ✓ | — | — | — | — |
| Biostrap | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | — | — | — |
| Verily Study Watch | ✓ | ✓ | ✓ | ✓ | — | — | — | — | ✓ | — |
| Polar Verity Sense | ✓ | — | ✓ | ✓ | — | — | — | — | — | — |
| Withings ScanWatch | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | some | — | — |
| **Empatica EmbracePlus** | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | — | **✓** | — |
| Ametris LEAP / wGT3X | some | — | ✓ | some | some | — | — | — | — | — |
| Axivity AX3 / AX6 | — | — | ✓ | ✓ (AX6) | — | — | — | — | — | — |
| GENEActiv Original | — | — | ✓ | — | ✓ (near-body) | — | — | — | — | — |

Verily Study Watch also carries **EDA**, and Empatica is the only other EDA source here.

**Reminder: sensor presence ≠ data access.** See Table 3.

**Correction (second pass):** the first version listed ECG for the Polar Verity Sense and omitted its
gyroscope and magnetometer; and it attributed the depth gauge and water temperature sensor to Apple
Watch Ultra 3 alone when Series 11 carries both.

---

## Table 3 — Raw signal availability to researchers (the decisive table)

**Substantially revised 2026-08-21 (second pass).** The first version understated how many platforms
expose raw signal, and understated the sampling rates available at low cost.

| Ecosystem | Raw accel | Raw PPG waveform | ECG | IBI / RR / BBI | Raw EDA | Route |
|---|---|---|---|---|---|---|
| Apple | No | No | Discrete ECG voltage samples via `HKElectrocardiogramQuery`; continuous ECG no. *Contradicted by ResearchKit FAQ — Unclear* | No | n/a | HealthKit |
| Fitbit / Google | No | No | ECG readings; raw waveform no | No | n/a | REST API |
| **Garmin** | **Yes** | No | No | **Yes — Enhanced BBI with per-beat confidence, via cloud API *or* SDK *or* Fitabase/Labfront. Nocturnal only** | n/a | **Health API, Health SDK, or a research platform** |
| Oura | No | No | n/a | No | n/a | — |
| WHOOP | No | No | MG only, not via API | No | n/a | — |
| **Samsung** | **Yes, 25 Hz** | **Yes — incl. IR + Red channels** | **Yes, raw, on-demand** | **Yes (IBI)** | n/a | **Privileged Health SDK**; also via Verily Pre |
| **Polar H10** | **Yes, 25/50/100/200 Hz, ±2/4/8 g** | — | **Yes, 130 Hz in µV** | **Yes, RR at 1 Hz** | n/a | **Open BLE SDK, no registration** |
| **Polar Verity Sense** | **Yes, 52 Hz; SDK mode 26–416 Hz, ±2–16 g** | **Yes — SDK mode 28–176 Hz, 22-bit** | No | **Yes (PPI)** — but not in SDK mode | n/a | **Open BLE SDK** |
| **Movesense** | **Yes — IMU 13 Hz–1.6 kHz, 9-axis** | — | **Yes, 125–512 Hz** | **Yes, RR at 1 ms resolution** | n/a | **Open API, custom firmware, no licence cost** |
| **Withings** | **Yes, ScanWatch, ~25 Hz** | **Yes, green/red/IR** | No | No | n/a | **Advanced Research API — contracted only; disables all other watch features; 3–4 day battery** |
| **Ultrahuman** | **Yes** | **Yes — raw PPG from a ring** | — | No | n/a | **UltraSignal, whitelist + loaner dev kit** |
| **Biostrap** | **Yes (+ gyroscope)** | **Yes, waveform kept raw** | — | No | n/a | **RPM dashboard / API / BLE SDK, configurable rates** |
| **Empatica** | **Yes, 64 Hz** | **Yes — BVP, 64 Hz** | No | Systolic peaks | **Yes, 4 Hz** | **Avro/CSV from Care Portal** |
| **Verily Study Watch** | **Yes (inertial)** | — | **Yes** | — | **Yes** | Verily Pre / Viewpoint Evidence, enterprise only |
| **Ametris** | **Yes, configurable** | Unclear | No | No | n/a | ActiLife / CentrePoint |
| **Axivity / GENEActiv** | **Yes, to 100 Hz, ±8 g** | n/a | n/a | n/a | n/a | **USB, raw file, no vendor** |

### Sampling-rate league table, cheapest-first

| Signal | Best available | Rate | Cost of entry |
|---|---|---|---|
| **ECG** | **Movesense** | **up to 512 Hz** | Developer kit, no licence fee |
| ECG | Polar H10 | 130 Hz | **~$95, open SDK, no approval** |
| **IMU / accelerometer** | **Movesense** | **up to 1.6 kHz, 9-axis** | Developer kit |
| Accelerometer | Polar Verity Sense (SDK mode) | up to 416 Hz | ~$95 |
| Accelerometer | Axivity AX3 | 100 Hz, ±8 g | Device only, no software cost |
| Accelerometer | Empatica / Ametris | 64 Hz / configurable | $1,750+ / five figures |
| Accelerometer | Samsung | 25 Hz | Partner approval |
| **Raw PPG** | **Polar Verity Sense (SDK mode)** | **28–176 Hz, 22-bit** | **~$95** |
| Raw PPG | Empatica (BVP) | 64 Hz | ~$1,750 / 3 yr |
| Raw PPG | Samsung (incl. IR + Red) | undocumented | Partner approval |
| Raw PPG | Withings ScanWatch | ~24.8 Hz | Contract |
| **EDA** | **Empatica** | **4 Hz** | ~$1,750 / 3 yr |
| EDA | Verily Study Watch | undocumented | Enterprise only |

**The headline: the highest sampling rates in this module are available from the cheapest and most
open vendors.** Polar and Movesense beat every major consumer platform and every clinical-trial
vendor on raw signal specification, at a fraction of the cost and with no approval process. What you
give up is form factor, wear duration, derived metrics, and study infrastructure — not signal.

## Table 4 — API characteristics

| Ecosystem | Auth | Rate limit | Push/webhooks | Historical backfill | Latency driver |
|---|---|---|---|---|---|
| Apple | On-device permission | n/a | HealthKit background delivery | **Full device history at enrollment** | iOS background execution limits |
| Fitbit (legacy) | Fitbit OAuth 2.0 | **150 req/hr per consented user** | Subscription API | Date-ranged; intraday HR **max 24h per request, silently degrades to summary** | Participant app sync |
| Google Health API | Google OAuth 2.0 | Not published — **Unclear** | `projects.subscribers` | Unclear | Unclear |
| Garmin | Garmin consent | Not published — **Unclear** | **Ping/Pull or Push** | Supported on first connect; depth Unclear | Device→Garmin Connect sync |
| Oura | **OAuth 2.0 only** (PATs deprecated Dec 2025) | 5,000 req / 5 min; per-token **and** per-application tiers | **Yes, ~30s after app sync** | Bulk on first connect, 1–3 month chunks, `next_token` | **Sleep only syncs when user opens the app** |
| WHOOP | OAuth 2.0 | **100 req/min, 10,000 req/day per client** | Yes (v2; v1 removed) | Date-ranged | Device→cloud sync |
| Samsung | On-device SDK | n/a | n/a | n/a | Researcher's own pipeline |
| Polar (BLE) | None | **None** | n/a | Device onboard memory | Bluetooth range |
| Withings | OAuth 2.0 | Unclear | Unclear | Unclear | Cellular or app sync |
| Empatica | Portal login | n/a | **No real-time access** | Full study history in cloud | Batch upload |
| Ametris | Unclear | Unclear | Unclear | Full | Cellular gateway or app |
| Axivity / GENEActiv | n/a | n/a | n/a | n/a | **Device return** |

---

## Table 5 — Study operations and management

| Ecosystem | Researcher portal | Participant roster | Adherence / wear-time monitoring | Multi-site | Surveys / EMA | Device reuse workflow |
|---|---|---|---|---|---|---|
| Apple | No | No | No | No | Build with ResearchKit | n/a (BYOD) |
| Fitbit / Google | No (**Fitabase**) | Via Fitabase | Via Fitabase (sync + battery status) | Via Fitabase | Fitabase Engage, Summer 2026 | Via Fitabase |
| Garmin | No (**Fitabase**) | Via Fitabase | Via Fitabase | Via Fitabase | No | Via Fitabase |
| Oura | No | No | No | No | Tags only | Requires re-sizing |
| WHOOP | No (Unite is enterprise) | No | No | No | Journal (API availability Unclear) | Membership-bound |
| Samsung | **Research Stack portal** | Yes | Unclear | Unclear | **Yes (Research Stack)** | Unclear |
| Polar | No (Team Pro is team-sport) | No | No | No | No | Yes, trivially |
| Withings | Partnership model | Via partner/RPM | Via partner | Yes | Via DCT partner | Yes |
| **Empatica** | **Care Portal** | **Yes, unlimited credentials** | **Yes, live wear-time** | **Yes** | Tags only | **Yes — first-class feature** |
| **Ametris** | **CentrePoint / Connect** | **Yes** | **Yes, near-real-time + monthly reports** | **Yes, 70+ countries** | Via Connect / Signant eCOA | Yes |
| Axivity / GENEActiv | **No** | No | **Impossible during wear** | No | No | Yes |

---

## Table 6 — Participant experience and operational burden

| Ecosystem | Form factor | Battery | Charging conflict with sleep? | Phone required? | BYOD viable? |
|---|---|---|---|---|---|
| Apple | Watch | ~1–2 days | **Yes — significant** | Yes (iPhone) | **Yes, excellent** |
| Fitbit | Band/watch | ~5–10 days | Minor | Yes | Yes |
| Garmin | Watch | **7–14+ days** | **No** | Yes (API); yes for SDK | Yes |
| Oura | **Ring** | ~4–7 days | Minor | **Yes — sleep sync depends on it** | Partly (sizing) |
| WHOOP | Screenless strap | ~4–5 days, **on-wrist battery swap** | **No — no wear interruption** | Yes | Partly (membership) |
| Samsung | Watch / ring | ~1.5–3 days (less when streaming raw) | Yes | Yes (Android) | Android only |
| Polar H10 | Chest strap | Session-wear | n/a | No (onboard memory) | No |
| Withings | Hybrid watch / scale / BP / **sleep mat** | ~30 days (3–4 in raw mode) | No | **No — cellular options** | Partly |
| Empatica | Wristband | **7 days raw, 14 extended** | No | Yes | No |
| Ametris | Research puck/watch | ~25–30 days | No | **No — cellular gateway** | No |
| Axivity / GENEActiv | Sealed puck | Full recording window, **no charging** | **No** | **No** | No |

---

## Table 7 — Cost structure

| Ecosystem | Device cost | Recurring per-participant | API/platform fee | Pricing public? |
|---|---|---|---|---|
| Apple | Consumer retail | **None** | Free ($99/yr dev account) | Device yes; total cost is engineering |
| Fitbit / Google | ~$80–180 | Premium for some metrics | API free; **Fitabase non-public** | Partly |
| Garmin | ~$150–1,000+ | **None** | API free; **SDK: licence fee or device MOQ**, non-public | Devices only |
| Oura | **Ring 5 $399–$499** | **$69.99/yr membership (mandatory)** | API free | Mostly |
| WHOOP | Included in membership | **$199 / $239 / $359 per yr** (One / Peak / **Life = MG**) | No published fee | **Yes** |
| Samsung | Consumer retail | **None** | **No published fee**; Research Stack free/open | Devices only |
| **Polar** | **~$90 (H10 / Verity Sense)** | **None** | **Free, open SDK** | **Yes** |
| **Movesense** | Not public | **None** | **No licence cost** | Partly |
| **Labfront** (Garmin/Movesense platform) | — | **Free / $500 / $1,250 per yr + $10–25 per extra participant** | Included | **Yes — the only research platform that publishes prices** |
| Withings | ~$100–350 | Varies | **Research API contracted, non-public** | Devices only |
| Empatica | **From $1,166.40; 3-yr academic bundle $1,749.60** | Included in bundle | Included | **Yes, for academic** |
| Ametris | ~$325–1,016 reported | Non-public | ActiLife ~$1,695, CentrePoint ~$3,500/yr *(third-party, dated)* | **No** |
| Axivity / GENEActiv | Low–mid hundreds | **None** | **None — open toolchain** | **No (quote), but no recurring cost** |

---

## Table 8 — Privacy, security, and compliance posture

| Ecosystem | HIPAA BAA | GDPR/DPA | SOC 2 / ISO | Regulatory clearance | Self-hosting / data custody |
|---|---|---|---|---|---|
| Apple | **N/A — Apple is not in the data path** | Researcher's obligation | n/a | ECG, AFib, sleep apnea, hypertension features cleared | **Full — researcher holds all data** |
| Fitbit / Google | **Unclear** | Unclear | Unclear | ECG/AFib features cleared | No |
| Garmin | Standard SDK described as **HIPAA-compliant** (vendor claim) | Unclear | Unclear | Some ECG features | **Yes via Standard SDK** |
| Oura | **Unclear** | Unclear (EU company) | Unclear | Limited | No |
| WHOOP | **Explicitly disclaimed** for the APIs | Unclear | Unclear | MG ECG / BP claimed | No; **terms prohibit permanent copies** |
| Samsung | Unclear | Unclear | Unclear | Some features cleared | **Yes — Research Stack self-deployed** |
| Polar | Unclear (Flow) | Unclear (EU company) | Unclear | H10 is a reference-grade sensor | **Yes — BLE path has no processor** |
| Withings | Unclear | Unclear (EU company) | Unclear | Medical-grade devices, multiple clearances | No |
| **Empatica** | Unclear | Unclear | Unclear | **FDA-cleared platform + cleared digital biomarkers; CE** | No |
| **Ametris** | Unclear | Unclear | Unclear | **FDA-cleared medical-grade; SaMD products** | Partial (ActiLife offline) |
| **Axivity / GENEActiv** | **N/A — no processor exists** | **Trivial — no processor** | n/a | None (research instruments) | **Full** |

**Every "Unclear" in this table is a vendor question, not an inference.** See
`../shared/unresolved-questions.md`.

---

## Table 9 — Evidence and validation summary

**Corrected 2026-08-21.** The first version misreported Schyvens et al. 2025 by quoting per-stage
accuracy as if it were the headline agreement statistic. Full extraction: `validation-evidence.md`.

### Sleep staging vs PSG — the two studies, side by side

| Device | Robbins 2024 (N=35, healthy, **Oura-funded**) | Schyvens 2025 (N=62, **independent**) |
|---|---|---|
| | four-stage κ | overall κ |
| **Oura Gen3** | **0.65** | not tested |
| **Apple Watch S8** | 0.60 | **0.53** |
| **Fitbit Sense / Sense 2** | 0.55 | 0.42 |
| Fitbit Charge 5 | not tested | 0.41 |
| **Whoop 4.0** | not tested | **0.37** |
| **Withings ScanWatch** | not tested | **0.22** |
| **Garmin Vivosmart 4** | not tested | **0.21** |

### The findings that matter more than the ranking

| Finding | Detail |
|---|---|
| **Deep sleep and REM are unreliable on every device** | Robbins ICCs — deep sleep: Oura **0.32**, Fitbit 0.36, Apple **0.13**; REM: Oura **0.27**, Fitbit **0.13**, Apple 0.37. All poor. **Stage-minute outcomes are largely device noise** |
| **TST and SE are the defensible endpoints** | ICC 0.74–0.85 across devices |
| **Every device underestimates WASO** | −12 to −48 min. Fragmentation endpoints are systematically flattered |
| **High sensitivity, poor specificity, universally** | Sleep detection 92–96%; wake detection **27–52%** |
| **Data loss is a real design risk** | Schyvens: Garmin failed **18/43** nights, Apple **15/35**, in a supervised lab. Withings and Oura lost **zero** |
| **Robbins 2024 has a declared conflict** | Funded by Oura; lead author on Oura's Medical Advisory Board and paid consultant. Never cite κ=0.65 without it |
| **Oura and WHOOP have never met** | A bridged estimate through Apple Watch suggests Oura is meaningfully ahead — labelled inference, not evidence. See `validation-evidence.md` §3 |
| **No consumer brand is acceptable for energy expenditure** | Unchanged across six years of reviews |
| **Current hardware is untested** | Oura Ring 5, WHOOP 5.0/MG, Apple Series 11, Fitbit Air all postdate every study above |

### Non-sleep evidence positions

| Ecosystem | Strongest evidence asset |
|---|---|
| Apple | **Apple Heart Study** — AFib notification at scale |
| Fitbit / Google | ***All of Us*** — 59,000+ participants, minute-level, EHR/genomics-linked |
| Garmin | Enhanced BBI vs ECG: mean error **0.506 ms**, SD 8.55 ms, r=0.975 — but **N=1, one night, manufacturer-published** |
| Oura | Robbins 2024 (with conflict) + temperature/illness-onset literature |
| WHOOP | Schyvens 2025 — best deep-sleep *accuracy* (69.6%), fourth-best overall agreement |
| Samsung | High step-count validity in cross-brand reviews; **absent from every PSG comparison** |
| **Polar** | **Used as the criterion device** in others' validations — revealed preference of the field |
| Withings | Medical-grade validation for **BP and weight**, not for sleep |
| **Empatica** | **FDA-cleared platform and cleared digital biomarkers** |
| **Movesense** | **Class IIa MDR 2017/745** on the MD variant; **no independent validation located** |
| Verily | Multiple FDA 510(k) clearances incl. on-demand ECG and irregular pulse |
| **Ametris** | **Is the actigraphy reference standard** |
| **Axivity / GENEActiv** | **UK Biobank 100,000+**, open reproducible toolchain |

## Table 10 — Meaningful differentiators, not feature lists

| Ecosystem | The one thing it does that others do not |
|---|---|
| **Apple** | SensorKit behavioural/phone-usage signals + deep retrospective history at enrollment, with no vendor in the data path |
| **Fitbit / Google** | Cheapest devices, largest literature, and an existing 59,000-participant open dataset requiring no procurement at all |
| **Garmin** | Raw accelerometry **and** beat-to-beat intervals at consumer cost, with 2-week battery and no subscription |
| **Oura** | Best measured sleep-staging agreement in a form factor people actually keep on overnight |
| **WHOOP** | Uninterrupted 24/7 wear (on-wrist battery swap) with no screen to change behaviour |
| **Samsung** | Raw PPG (IR + Red), raw ECG, and IBI from a mainstream smartwatch — **plus** an open-source research backend and portal |
| **Polar** | Raw ECG from a $90 device via an open GitHub SDK, with no cloud, no approval, and no fee |
| **Withings** | Cellular-connected medical-grade home devices that remove the participant's phone from the data path; plus a zero-burden under-mattress sleep mat |
| **Empatica** | **Raw EDA** — available nowhere else here — with FDA clearance and real study management |
| **Ametris** | The actigraphy reference standard, with regulated-trial operations in 70+ countries |
| **Axivity / GENEActiv** | Fully open hardware/firmware/analysis, no vendor in existence for governance purposes, and direct comparability with UK Biobank |
| **Movesense** | The only sensor here you can **reprogram** — custom firmware, no licence cost — at 512 Hz ECG and 1.6 kHz IMU, with EU Class IIa certification on the MD variant |
| **Ultrahuman** | The only **ring** exposing raw PPG, and the only ecosystem pairing ring biometrics with CGM in one API |
| **Biostrap** | Raw PPG **plus** configurable sampling **plus** integrated surveys **plus** a participant dashboard, with leg-worn gait/balance/jump metrics no one else offers |
| **Verily Study Watch** | ECG **and** EDA **and** inertial in one FDA-cleared device with weeks of onboard raw storage — never sold to consumers |
| **Labfront** | The only research platform in Module 1 that **publishes its pricing**, with a free 5-participant tier and EMA included at every level |


---

## Table 11 — Study-operations platforms (the layer most vendors don't provide)

| | **Labfront** | **Fitabase** | **Empatica Care Portal** | **Ametris CentrePoint** | **Samsung Research Stack** |
|---|---|---|---|---|---|
| Devices | Garmin, Movesense, Dexcom | **Fitbit**, Garmin | EmbracePlus only | ActiGraph LEAP, Insight Watch | Galaxy Watch / Ring |
| **Pricing public?** | **Yes** | No | **Yes (academic)** | No | Free / open source |
| Cost | Free (5p) / $500 (20p) / $1,250 (20p, all integrations) + $10–25 per extra | Custom quote | $1,749.60 per device / 3 yr academic | Five figures reported | $0 |
| **EMA / surveys** | **Yes, all tiers** | Engage, Summer 2026 | Tags only | Via Connect / Signant | **Yes** |
| Adherence monitoring | Yes | Yes (sync + battery) | **Yes, live wear-time** | **Yes, near-real-time + reports** | Unclear |
| Multi-site | Yes | Yes | **Yes** | **Yes, 70+ countries** | Unclear |
| Raises sampling resolution | **Yes — Garmin SDK partnership** | Enhanced BBI via OAuth | Configurable on device | Configurable | Full SDK control |
| Self-hosting | No | No | No | ActiLife offline | **Yes** |
| Free tier to pilot | **Yes** | No | No | No | **Yes** |

**Practical read:** if your study is Fitbit-based, Fitabase is effectively the only option and you
must request a quote. If it is Garmin-based, Labfront is cheaper, transparent, includes EMA, and can
raise sampling resolution — and you can pilot it free with five participants before spending
anything.

---

## Table 12 — Choosing by research question

| If your primary endpoint is… | Use | Avoid | Why |
|---|---|---|---|
| **Physical activity / sedentary behaviour** | Axivity, GENEActiv, Ametris | Any device where EE is the metric | Raw accelerometry, open pipelines, cohort comparability |
| **Sleep timing / duration (not stages)** | Oura, Withings ScanWatch, actigraphy | — | TST and SE have good ICC; both had zero data loss in PSG studies |
| **Sleep architecture (stages)** | Reconsider the design; PSG or ambulatory EEG | **All consumer wearables** | Deep/REM ICC is 0.13–0.36 on the best devices |
| **Sleep fragmentation / WASO** | Reconsider; PSG | **All consumer wearables** | Every device underestimates WASO by 12–48 min |
| **HRV — nocturnal** | **Garmin Enhanced BBI** (via Labfront/Fitabase), Polar H10, Movesense | PPG devices reporting only a summary HRV number | Beat-level data with confidence flags, or true ECG RR |
| **HRV — daytime / during stressors** | Polar H10, Movesense, Garmin Health SDK | Garmin Enhanced BBI | Enhanced BBI is **nocturnal only** |
| **Cardiac rhythm / AFib** | Apple Watch, Withings ScanWatch, Verily, Movesense MD | — | FDA/CE-cleared ECG features with real evidence |
| **Electrodermal / arousal / stress** | **Empatica**, Verily Study Watch | Everything else | Only sources of raw EDA |
| **Energy expenditure** | Indirect calorimetry, doubly labelled water | **Every consumer wearable** | No brand within acceptable limits, six years running |
| **Custom algorithm development** | Movesense, Polar, Samsung, Biostrap, Ultrahuman | Oura, WHOOP | Requires raw signal |
| **Large-N with no budget** | ***All of Us*** or **UK Biobank** secondary analysis | — | Data already collected, no procurement, no API |
| **Regulated trial endpoint** | Ametris, Empatica, Verily | Consumer platforms | Cleared devices, locked algorithms, Part 11 operations |
| **Behaviour-change intervention** | Any consumer device; unified APIs fine | — | The device is a tool, not an instrument; brand confounding is tolerable |
| **Minimal reactivity / observational purity** | WHOOP, **Fitbit Air**, ActiGraph, Axivity | Feedback-rich smartwatches | Screenless devices do not induce behaviour change |
