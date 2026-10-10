# Withings

## Quick Facts

| Field | Details |
|---|---|
| Organization | Withings (France) |
| Category | Connected health devices (scales, BP monitors, sleep mats, hybrid smartwatches) with a dedicated clinical-trials business unit |
| Current status | Active |
| Platforms/devices | ScanWatch / ScanWatch 2 / ScanWatch Light, Body series smart scales, BPM series blood pressure monitors, Sleep / Sleep Rx under-mattress mats, U-Scan; iOS and Android |
| Open source | No |
| Hosting/deployment | Vendor cloud (Withings Health Data API); **cellular-connected device options remove the smartphone dependency** |
| Pricing model | Device purchase. API plans (Verified 2026-10-10): **Start for Free** (self-serve, 10 users, more after Withings review), **Enterprise** and **Advanced Biomarkers** (custom price by active users). **From 12 October 2026, Withings accounts created after that date need a paid Withings+ membership to share data with a Start for Free app**, unless the app is on Enterprise or Advanced Biomarkers. Advanced Research API (raw data) is contract-gated |
| Last verified | 2026-08-21; raw accelerometer rate re-checked 2026-10-09; API plans, Withings+ requirement, security and compliance statements, API reference and FDA 510(k) list re-verified 2026-10-10; cellular uniqueness claim, Strengths sampling rate and Schyvens figure corrected 2026-10-10 |

## Summary

- Withings is the wrong shape to compare directly against Apple/Fitbit/Garmin, and that is precisely why it belongs in this module. It is a **connected-health-device company with a purpose-built decentralised clinical trials business** (Withings Health Solutions), not a fitness-wearable company. Its distinguishing capabilities are:

1. **Medically-oriented, regulated devices**, blood pressure monitors, weighing scales with body composition, ECG-capable hybrid watches, which cover measurement domains no wrist fitness tracker touches.
2. **Cellular connectivity.** Withings offers device variants that transmit over cellular without a paired smartphone. For elderly, low-digital-literacy, or rural cohorts this **eliminates the single largest source of missing data in remote studies**, the participant's phone. Withings is not alone here: Ametris's CentrePoint Data Hub is a "cellular-powered communication gateway" that sends Insight Watch and LEAP data from the participant's home to the CentrePoint Cloud (ametris.com/centrepoint, read 2026-10-10; see `ametris-actigraph.md`). Withings' distinction is that its cellular options are built into consumer-priced measurement devices such as BP monitors and scales rather than a separate hub alongside an enterprise trial platform.
3. **An Advanced Research API** giving contracted partners access to **raw accelerometer and raw PPG** signals, a genuine raw-data path on a consumer device.

- The constraints are narrow scope and gated access: the raw-data programme is **ScanWatch only** and **contracted partners only**, and Withings' own sleep-staging performance was the weakest of six devices in the strongest recent independent validation.

- **Dated change, 12 October 2026 (Verified, Withings API plans page, read 2026-10-10).** Withings now publishes a self-serve **Start for Free** API plan (10 users, more once Withings reviews the app). From **12 October 2026**, Withings accounts created after that date "will need a membership to share health data with a free-plan app, including apps that are already live". The membership is Withings+. Withings states the requirement also covers sharing through Apple Health or Google Health. Accounts created before that date are unaffected. Enterprise and Advanced Biomarkers plans lift the requirement for the use cases in the agreement, and Withings says it "can be removed for specific use cases: Cellular Solutions, SDK and Research partners." **A free-plan study recruiting participants with new Withings accounts after 12 October 2026 must budget for each participant's Withings+ membership or move to a paid plan.**

## Products / Platform Architecture

- **ScanWatch / ScanWatch 2**, hybrid analogue watches with PPG, ECG, SpO2, temperature (ScanWatch 2), and long battery life (~30 days, a major advantage over smartwatches).
- **Body / Body Pro / Body Scan**, smart scales with weight, body composition, and (Body Scan) segmental impedance and a 6-lead ECG.
- **BPM Connect / BPM Pro / BPM Vision**, blood pressure monitors, several with cellular variants.
- **Sleep / Sleep Rx**, under-mattress ballistocardiography mats providing sleep staging, heart rate, respiratory rate, and sleep apnoea detection **without the participant wearing anything**. This is a distinctive and underused research modality.
- **U-Scan**, in-toilet urine analysis device.
- **Withings Health Solutions**, the B2B arm covering remote patient monitoring, research, and clinical trials.

- Three API tiers:

| Tier | Content | Access |
|---|---|---|
| **Public Health Data API** | Measures, sleep, heart, activity, workouts, processed data | OAuth app registration. Plans (2026-10-10): Start for Free (10 users, more after review, "Standard" rate limits, EU-hosted; Withings+ required for users with accounts created after 12 October 2026), Enterprise (custom, 1,500+ requests/minute, US-hosted HIPAA, HDS, DPA and BAA) and Advanced Biomarkers (custom; FDA/CE-cleared biomarkers, "AI model training contract", anonymisation, clinical study support add-on) |
| **Raw Data API** | Raw accelerometer and raw PPG; the API reference calls it "part of the Advanced research API", "around 25Hz", ScanWatch only | **Contracted partners only**; which plan carries it is not stated on the plans page |
| **Advanced Research API** | The research-oriented packaging of raw access | Gated; contact Withings |

## Sensors and Data Streams

- Every Module 1 profile uses the same table so devices can be compared row by row. Rows are the sensors named in `CLAUDE.md`. "Present" is about the hardware; "Researcher access" is about what a study can actually obtain, which is the module's central question. "Unclear" means nothing current was verified. The convention is recorded in [`../../shared/profile-table-conventions.md`](../../shared/profile-table-conventions.md).

| Sensor | Present | Researcher access to underlying signal | Resolution or sampling | Notes |
|---|---|---|---|---|
| PPG | ScanWatch, 3-wavelength green, red and infrared (some configurations single green) | Raw via the Advanced Research API when raw mode is activated | About 24.824 Hz effective | Raw mode disables every other watch feature and drains the battery four to seven times faster, so it suits bounded windows, not weeks. |
| ECG | ScanWatch 2 single lead; Body Scan 6-lead; some BPM models | Not mentioned as available through the Raw Data API; a device feature rather than a raw stream | Per reading |  |
| Accelerometer | ScanWatch, 3-axis | Raw via the Advanced Research API in raw mode | About 24.824 Hz in the documented raw mode, plus or minus 4 g, about 2 mg sensitivity. The overview page's "25 Hz by default (up to 100 Hz)" describes the sensor, and no documented setting reaches 100 Hz. | Raw capture must be activated via API first. Whether a contract can unlock a higher rate needs Withings to confirm (re-checked 2026-10-09). |
| Gyroscope | Unclear | Unclear | Unclear |  |
| Magnetometer | Unclear | Unclear | Unclear |  |
| Temperature | ScanWatch 2 | Unclear | Unclear |  |
| SpO2 | ScanWatch 2 | Unclear | Unclear |  |
| GPS | Unclear | Unclear | Unclear |  |
| Barometer / altimeter | ScanWatch 2 | Unclear | Unclear |  |
| EDA | Body Scan, for nerve assessment | Unclear | Unclear |  |
| Ambient light | Unclear | Unclear | Unclear |  |
| Other | Body Scan weight and segmental composition; BPM oscillometric blood pressure; Sleep and Sleep Rx ballistocardiography with sleep staging, HR, respiratory rate, snoring and apnoea detection | Summaries via the standard API | Per measurement |  |

**Verification.** From Withings' Advanced Research API and product documentation as recorded in the Module 1 passes; see the notes below for the raw-mode constraints in full.

### Notes from earlier verification passes

### ScanWatch raw-data capability (Advanced Research API / Raw Data API)

| Signal | Detail |
|---|---|
| **3-axis accelerometer** | ±4g range. Samples at **25 Hz by default, up to 100 Hz** per the Advanced Research API overview; see the 2026-10-09 reconciliation note below. |
| **PPG (optical)** | **3-wavelength digital photoplethysmograph, green, red, and infrared** (some configurations single green LED). |
| Effective sampling rate | Both sensors sample at **approximately 24.824 Hz** |
| Device support | **Withings ScanWatch only** |
| ECG raw waveform | **Not mentioned as available** through the Raw Data API, ECG appears to be a device feature, not a raw API stream |

- **Sampling-rate reconciliation (re-read 2026-10-09, Corroborated).** Both Withings pages were re-read and still carry their original wording. The Advanced Research API overview says the accelerometer "samples at 25Hz by default (up to 100Hz)". The Raw Data page says data are "sampled at approximately 25 Hz" and that "Both sensors sampling rate are about 24.824 Hz". The two are compatible once read as different things: 24.824 Hz is the precise effective rate of the documented raw mode, which the overview rounds to 25 Hz, and "up to 100 Hz" is a hardware ceiling that neither page exposes as a setting. Plan a study at about 24.8 Hz. Only Withings can say whether a contracted partner can get 100 Hz.
- **Critical operational constraints on raw mode**, documented by Withings:
- Raw capture must be **explicitly activated via API** before data can be retrieved.
- Activating raw data puts the device into a **specific mode that disables all features except raw data capture.** The watch stops being a watch.
- Battery drains **four to seven times faster**, reducing ScanWatch battery life to roughly **3 to 4 days** under continuous raw collection (from ~30 days normally).

- These constraints define the realistic protocol: raw mode is for **bounded measurement windows**, not for continuous multi-week capture. A design might alternate, normal mode for longitudinal summaries, raw mode for scheduled intensive assessment periods.

### Standard device sensors

| Device | Sensors |
|---|---|
| ScanWatch 2 | PPG, ECG (single-lead), SpO2, temperature, accelerometer, altimeter |
| Body Scan | Weight, segmental body composition, 6-lead ECG, electrodermal activity for nerve assessment |
| BPM series | Oscillometric blood pressure, some with ECG |
| Sleep / Sleep Rx | Ballistocardiography (pneumatic sensor), sleep staging, HR, respiratory rate, snoring, apnoea detection |

## Derived Metrics / Analytics

- Public Health Data API domains: measures (weight, body composition, blood pressure, temperature, SpO2), sleep (stages, duration, sleep score, apnoea indicators), heart (heart rate, ECG readings, HRV), and activity (steps, distance, calories, workouts).

- The **blood pressure and weight/body composition streams are the genuinely differentiated ones**, no wrist fitness tracker in this module provides validated blood pressure or segmental body composition. For cardiometabolic, hypertension, obesity, and heart-failure research these are the endpoints that matter, and Withings is the natural choice.

## Active Data Collection

- None native. Withings is a measurement-device company; surveys and ePRO must come from a separate system. In decentralised clinical trials Withings devices are commonly integrated *into* a DCT platform (e.g. the Medable partnership) which supplies the ePRO layer.

## Researcher and Study Management Features

- Provided through **Withings Health Solutions** rather than a self-serve portal:
- Device logistics and provisioning at scale.
- Cellular device management (no participant setup).
- Integration into RPM platforms, DCT platforms, and CROs.
- Withings states it works with pharmaceutical groups and CROs on real-world data collection in decentralised trials, and will "help find the best way to retrieve and adapt data" via cellular connectivity, mobile app, an RPM platform, API, or other routes.

- This is a **services-and-integration model**, not a self-service research console. It suits funded clinical trials better than investigator-initiated academic studies with small budgets.

### Research program and academic data access (added 2026-10-10)

- **Two research routes exist, both gated:**
  - **Advanced Research API.** Withings describes it as "Designed for research groups, universities, and advanced health studies", giving "direct access to raw sensor data": accelerometer "25Hz by default (up to 100Hz)" and PPG with three LEDs or one, **ScanWatch only**, by contacting Withings (developer page re-read 2026-10-10, **Verified**). Contract terms and price are not published.
  - **Advanced Biomarkers plan** ("Clinical studies & AI research"). Custom-priced; adds FDA/CE-cleared biomarkers (ECG, AFib, SpO2, vascular age, AHI, "EDA/NHS"), risk scores, symptom tracking and questionnaires, an "AI model training contract", anonymisation, and a "Clinical study support team" add-on (plans page, **Verified** that these are offered; the cleared-biomarker wording is Withings' own).
- **What a low-budget academic study can get without a contract:** the Start for Free plan's derived data (activity, sleep, body, heart) for up to 10 users, more after a Withings review, at "Standard" rate limits, EU-hosted. **From 12 October 2026**, participants whose Withings accounts are created after that date need a paid Withings+ membership to share data with a free-plan app, and Withings says this also applies to sharing via Apple Health or Google Health. Withings says the requirement can be removed for "Research partners", but the terms for that are not published.
- **How it differs from commercial access:** the plans are the same for academic and commercial customers; there is no published academic price. Raw signals and the AI-training right come only by contract. No history-depth or retention term is published for any plan.
- **Is it active?** Yes (pages current, 2026-10-10). Withings' research and clinical-trials page returned 403 to scripted requests and was not re-read.

## Data Access and Export

| Route | Content | Gate |
|---|---|---|
| Public Health Data API | Processed measures, sleep, heart, activity | App registration; Start for Free plan self-serve up to 10 users; Withings+ needed for participants with accounts created after 12 October 2026 unless on Enterprise or Advanced Biomarkers |
| Raw Data API / Advanced Research API | Raw ACC + PPG from ScanWatch | **Contracted partners only** |
| Cellular device direct-to-cloud | All standard measures | Device purchase; no participant phone needed |
| Participant self-export | Withings account data export | GDPR-backed |

- **Rate limits (2026-10-10):** Enterprise and Advanced Biomarkers "1,500+ requests/minute"; Start for Free is labelled only "Standard" (**Verified**, plans page). A search snippet of an earlier version of the page gave 120 requests/minute for the free tier (**Reported**, not on the current page). Throttled calls return body status 601 "Too many request" (**Verified**, API reference). Historical depth, backfill and retention are **not documented**; sync uses the `lastupdate` parameter.

## APIs, SDKs, and Extensibility

- REST + OAuth 2.0 via the Withings Partner Hub (`developer.withings.com`). The full API reference at `developer.withings.com/api-reference/` is public, with no login (re-checked 2026-10-10; the 2026-08-21 pass recorded it as login-gated).
- Notification/webhook mechanism for new measurements (referenced by Withings' integration guide; not verified in detail here).
- No device SDK; devices are not programmable.
- Documented integrations with DCT and RPM platforms.

## Deployment and Infrastructure

- Vendor cloud. No self-hosting, but a **choice of cloud**: Withings describes an EU Medical Cloud based in France and a US Medical Cloud (security and compliance page, read 2026-10-10). The plans page puts the free plan on EU hosting and offers US hosting on Enterprise and Advanced Biomarkers. **Corroborated** (vendor statements).

## Participant Experience

- This is where Withings is strongest and most differentiated:

- **Cellular devices require no smartphone, no app, no pairing, and no participant technical action.** A participant steps on a scale or uses a BP cuff and the reading reaches the study. For geriatric, low-literacy, low-income, or rural cohorts this transforms feasibility.
- **ScanWatch battery life of ~30 days** in normal mode, effectively no charging burden. (Raw mode destroys this; see above.)
- **The Sleep mat requires no wearing at all**, placed under the mattress, it collects nightly sleep data with zero adherence burden. For populations who will not tolerate a wearable (dementia, paediatric, sensory sensitivity), this is a genuinely distinct capability.
- Hybrid analogue watch styling is more socially acceptable than sport watches in some populations.
- iOS and Android.

## Privacy, Security, and Compliance

- Withings devices in the medical lines carry regulatory clearances. The US FDA 510(k) list is now checked (see below); clearance status in other markets and the exact feature scope of each clearance were not verified and vary by jurisdiction.
- **Compliance statements (re-checked 2026-10-10; Corroborated, vendor statements without linked certificates):** Withings' developer security page says its EU Medical Cloud, based in France, "is GDPR compliant, HDS, HIPAA and ISO 27001:2017 certified", and its US Medical Cloud "is a US based, ISO 27001:2017 certified and HIPAA compliant", adding "Withings complies with HIPAA rules and regulations". The plans page offers "DPA, BAA and security questionnaire" on Enterprise and Advanced Biomarkers only, not on Start for Free. No SOC 2 statement was found. No certificate registry entry was checked, so none of these is Verified independently. (The 2026-08-21 text said HIPAA, ISO and DPA terms were not found.)
- **FDA 510(k) clearances (Verified, openFDA, 2026-10-10):** Withings Blood Pressure Monitor K110872 (2011) and K133125 (2014); Withings Thermo K160544 (2016); Scan Monitor K201456 (2021-10-05) and Scan Monitor 2.0 K230812 (2023-08-23); Withings Sleep Rx K231667 (2024-09-06); Withings ECG App K240795 (2025-06-15); Withings BeamO K252474 (2025-11-10). CE-mark scope per device was not checked.
- **Do not infer regulatory clearance of a device from the existence of a clinical trials business.**

## Pricing

- **Devices:** consumer retail pricing for scales, BP monitors, ScanWatch, and Sleep mats, generally moderate. Cellular variants and Health Solutions pricing differ.
- **Public API:** Start for Free plan has no fee, but from 12 October 2026 participants with Withings accounts created after that date need their own **Withings+** membership to share data with a free-plan app; Withings says this cannot be avoided by routing through Apple Health or Google Health. Enterprise and Advanced Biomarkers are custom-priced by active users (and biomarkers); on those plans Withings says users "do not subscribe individually and there is no per-member charge". Withings+ membership price was not read (withings.com returned 403 to scripted requests).
- **Advanced Research API / Raw Data API:** contract-gated; **pricing not public.**
- **Withings Health Solutions:** quote-based B2B.
- No consumer subscription is required for core measurements in the Withings app itself; the API data-sharing requirement above is the exception for new accounts on the free plan.

## Research Evidence and Validation

- *(Rewritten 2026-08-21 after reading Schyvens et al. 2025 in full, the ScanWatch result flagged as missing in the first pass is now recovered.)*

### Schyvens et al., *SLEEP Advances* 2025, ScanWatch results

- N=62, single-night PSG, six devices, independently funded (VLAIO), no author conflicts. Full tables in `../validation-evidence.md`.

| Metric | Withings ScanWatch | Rank of 6 |
|---|---|---|
| **Cohen's kappa** | **0.22, "fair"** | **5th of 6** (only Garmin worse) |
| Sleep/wake sensitivity | 94.32% | 3rd |
| Sleep/wake specificity | **31.09%** | 5th |
| Wake accuracy | **31.09%** | 5th |
| Light sleep accuracy | **53.04%** | **6th, worst** |
| "Deep" accuracy (N3+REM combined) | 66.74% † | 2nd |
| **TST bias** | **+39.87 min (p<0.001)** | 6th, worst overestimate |
| **SE bias** | **+10.19% (p<0.001)** | 6th, worst |
| **WASO bias** | **−47.94 min (p<0.001)** | 6th, worst underestimate |
| SOL bias | +6.59 min (ns) | |
| **Data loss** | **0 / 41, best in the study** | **1st** |

- † **The ScanWatch does not do four-stage classification.** It combines REM and N3 into a single "deep sleep" category, i.e. three-state output. Its 66.74% figure is therefore not comparable to the four-state devices, and it **overestimated that combined category by +73.20 minutes (p<0.001)**.

- Misclassification detail: 53.89% of PSG wake epochs were called light sleep; 41.13% of PSG light sleep was called deep; 27.69% of true deep sleep was called light. **Verified.**

- **Honest assessment.** ScanWatch sleep staging is poor, second-worst overall agreement of the six devices, worst light-sleep accuracy, and the largest biases on TST, SE and WASO in the study. It overestimates sleep by 40 minutes a night and misses 48 minutes of wake. **Do not use Withings wrist-derived sleep architecture as a research endpoint.**

- The one genuinely excellent result is **reliability**: ScanWatch was the only device with **zero data loss** across 41 attempts, in a study where Garmin failed 18/43 nights and Apple 15/35. For a free-living study, a device that always produces data is worth a great deal, but produce-data and produce-*correct*-data are different properties, and here they diverge sharply.

### Where Withings' evidence is actually strong

- The medical-grade framing is defensible for the **non-wearable** devices, not the watch. BPM blood pressure monitors and Body scales are the clinically validated products with regulatory clearances; the ScanWatch's FDA-cleared feature is **single-lead ECG for AFib detection**, not sleep staging. Withings publishes a device-validation studies page and a study index spanning hypertension, diabetes, surgical recovery, sleep and HIV research. **Reported**, individual studies not reviewed.

- **The correct read on Withings: buy it for blood pressure, weight, body composition and ECG. Do not buy it for sleep.**

## Strengths

- **Cellular, phone-free data collection**, removes the dominant failure mode in remote studies and unlocks populations most consumer platforms cannot reach (Ametris offers a cellular hub for its research devices; see Summary).
- **Raw accelerometer (about 24.8 Hz in the documented raw mode; the overview's "up to 100 Hz" is not a documented setting, see the sampling-rate reconciliation above) and 3-wavelength raw PPG** available on a consumer device via the Advanced Research API.
- **Measurement domains nobody else covers**: blood pressure, body composition, and contactless under-mattress sleep.
- ~30-day ScanWatch battery in normal mode, essentially no charging burden.
- Zero-burden sleep measurement via the Sleep mat.
- Purpose-built clinical trials / DCT business with device logistics and CRO integration.
- EU vendor, favourable posture for GDPR-governed research.
- Discreet hybrid-watch form factor.

## Limitations

- **Raw data is ScanWatch-only and contracted-partners-only**, not accessible to an ordinary academic study without a commercial agreement.
- **Raw mode disables all other device functions and cuts battery life to 3 to 4 days**, restricting it to short intensive windows.
- **Worst sleep-staging performance of six devices** in the strongest independent validation.
- Wrist heart rate accuracy is in the lower tier.
- No self-serve research console; access to the research capability runs through a sales conversation.
- Pricing for research access is non-public: the plan structure is published, but Enterprise, Advanced Biomarkers and raw-data prices are custom.
- **From 12 October 2026 the free API plan needs a paid Withings+ membership for each participant with a new Withings account.**
- No survey/EMA capability.
- Not a general activity-tracking platform, step/activity outputs are secondary to the measurement devices.
- Compliance is vendor-stated only (no certificates checked); BAA and DPA only on paid plans.

## Best-Fit Use Cases

- **Decentralised clinical trials** needing validated blood pressure, weight, and body composition endpoints collected remotely.
- **Cardiometabolic, hypertension, obesity, and heart-failure research.**
- Studies in **elderly, rural, low-digital-literacy, or low-income cohorts** where smartphone dependence would cause unacceptable attrition, the cellular devices are close to unique here.
- Sleep research in populations who will not wear a device (Sleep mat).
- Short intensive raw-signal assessment windows on a consumer device, where a commercial partnership is feasible.
- Long-duration studies where charging burden must be near zero.

## Poor-Fit Use Cases

- Sleep staging as an endpoint.
- Wrist heart rate accuracy as a primary concern.
- Physical activity or exercise physiology research.
- Small academic studies needing raw data without a commercial contract.
- Studies needing continuous multi-week raw signal capture.
- Studies requiring integrated surveys/EMA without a separate platform.

## Open Questions

- *(Directed to Withings: https://www.withings.com/us/en/health-solutions/research-clinical-trials and the Partner Hub at https://developer.withings.com/)*

- **What are the terms and cost of an Advanced Research API contract, and will Withings contract with an individual academic investigator or only with institutions/sponsors?**
- Will the raw-data programme extend beyond ScanWatch to ScanWatch 2 or other devices?
- Is raw ECG waveform available under any agreement?
- Can a contracted partner configure the ScanWatch accelerometer above the documented ~24.824 Hz raw-mode rate, up to the 100 Hz the overview page cites? Both pages re-read 2026-10-09 and neither documents a rate setting.
- Precise raw-data file structure, retrieval mechanics, volume, and any retention window on Withings' side.
- Historical depth, backfill and retention for the Public Health Data API (rate limits partly published 2026-10-10).
- Does a research partner on a free plan qualify for the Withings+ exemption, and on what terms?
- Which plan includes the Raw Data API, and at what price?
- **Per-device regulatory clearance and validation-protocol compliance** (especially BP monitors against ESH/AAMI/ISO 81060-2, and ECG/SpO2 clearances by market).
- Partly answered 2026-10-10: HIPAA, HDS, ISO 27001:2017 and GDPR are vendor-stated; DPA and BAA are offered on Enterprise and Advanced Biomarkers; EU or US cloud. Still open: SOC 2, ISO 13485, certificate evidence, and the conflict between ISO 27001:2017 on the developer page and the 2022 version that search snippets attribute to Withings' consumer security page.
- Cellular device coverage by country and carrier, and cost of the cellular data component.
- Sleep mat validation evidence for staging and apnoea detection.

## Key Links

- Official site: https://www.withings.com/
- Health Solutions, research & clinical trials: https://www.withings.com/us/en/health-solutions/research-clinical-trials
- Research page: https://www.withings.com/en-us/pages/research
- Partner Hub (developer portal): https://developer.withings.com/
- API reference (public, no login): https://developer.withings.com/api-reference/
- **API plans:** https://developer.withings.com/developer-guide/v3/withings-solutions/withings-api-plans/ (content at https://static.withings.com/content/api/plans/plans.html)
- Security and compliance: https://developer.withings.com/developer-guide/v3/withings-solutions/security-and-compliance/
- **Advanced Research API:** https://developer.withings.com/developer-guide/v3/withings-solutions/research-apis/
- **Raw data documentation:** https://developer.withings.com/developer-guide/v3/integration-guide/public-health-data-api/data-api/raw-data/
- For health professionals: https://www.withings.com/us/en/for-professionals

## Sources

1. Withings, Advanced Research API. https://developer.withings.com/developer-guide/v3/withings-solutions/research-apis/ (accessed 2026-08-21). **Primary.** Establishes ScanWatch-only support, 3-axis accelerometer at 25 Hz default up to 100 Hz, PPG with three LEDs (green/red/IR) or one (green), the targeting at research groups and universities, and that access is gated by contacting Withings. Re-read 2026-10-09: wording unchanged, still "samples at 25Hz by default (up to 100Hz)" and still ScanWatch-only.
2. Withings, Raw data documentation. https://developer.withings.com/developer-guide/v3/integration-guide/public-health-data-api/data-api/raw-data/ (accessed 2026-08-21). **Primary.** Establishes the ±4g accelerometer range, the ~24.824 Hz effective sampling rate for both sensors, "contracted partners only" access, the requirement to activate raw capture via API, the disabling of all other device features in raw mode, and the 4 to 7× battery drain reducing life to 3 to 4 days. Also establishes that ECG is not listed among Raw Data API types. Re-read 2026-10-09: wording unchanged, and the page also says "approximately 25 Hz" and "~2 mg" sensitivity.
3. Withings Health Solutions, research and clinical trials. https://www.withings.com/us/en/health-solutions/research-clinical-trials (accessed 2026-08-21). Establishes the pharma/CRO decentralised-trials positioning and the multiple retrieval routes offered (cellular, mobile app, RPM platform, API).
4. Withings Partner Hub. https://developer.withings.com/ (accessed 2026-08-21).
5. Schyvens A.-M. et al., "A performance validation of six commercial wrist-worn wearable sleep-tracking devices for sleep stage scoring compared to polysomnography." *SLEEP Advances* 2025;6(2):zpaf021. https://academic.oup.com/sleepadvances/article/6/2/zpaf021/8090472 (full text also at https://pmc.ncbi.nlm.nih.gov/articles/PMC12038347/, re-read 2026-10-10). Withings ScanWatch overall Cohen's kappa 0.22, 5th of six (only Garmin Vivosmart 4 lower at 0.21); "deep" accuracy 66.74%, but for a combined N3+REM category not comparable with the four-state devices. Corrected 2026-10-10 from a stale search-summary percentage.
6. Fuller D. et al. *JMIR mHealth uHealth* 2020;8(9):e18694. https://mhealth.jmir.org/2020/9/e18694/, Apple Watch stronger agreement than Garmin, Fitbit, and Withings for heart rate.
7. Medable, Withings Health Solutions partnership announcement (secondary). https://www.businesswire.com/news/home/20220721005032/en/ (accessed 2026-08-21). Evidence of DCT platform integration.
8. Withings API plans. https://developer.withings.com/developer-guide/v3/withings-solutions/withings-api-plans/ (content served from https://static.withings.com/content/api/plans/plans.html), accessed 2026-10-10. **Primary.** Start for Free, Enterprise and Advanced Biomarkers plans; 10-user cap; 1,500+ req/min on paid plans; DPA, BAA and US hosting on paid plans; Withings+ required from 12 October 2026 for new accounts on the free plan, including via Apple Health or Google Health; exemption for "Cellular Solutions, SDK and Research partners".
9. Withings, Security and compliance. https://developer.withings.com/developer-guide/v3/withings-solutions/security-and-compliance/ (accessed 2026-10-10). **Primary (vendor statement).** EU Medical Cloud in France: GDPR, HDS, HIPAA, ISO 27001:2017; US Medical Cloud: ISO 27001:2017, HIPAA.
10. Withings API reference. https://developer.withings.com/api-reference/ (accessed 2026-10-10; public, OpenAPI spec embedded in the page bundle). **Primary.** Raw Data "part of the Advanced research API", PPG and accelerometer "around 25Hz", ScanWatch only; activation takes `rawdata_type` and `enddate`; status 601 "Too many request".
11. openFDA 510(k) database, applicant Withings. https://api.fda.gov/device/510k.json?search=applicant:withings (accessed 2026-10-10). **Primary (independent record).** K110872, K133125, K160544, K201456, K230812, K231667, K240795, K252474.
12. Withings, Advanced Research API (re-read 2026-10-10). https://developer.withings.com/developer-guide/v3/withings-solutions/research-apis/ . Wording unchanged from source 1.
