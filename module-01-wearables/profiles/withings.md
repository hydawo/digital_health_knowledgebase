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
| Last verified | 2026-10-11 (vendor fact record); earlier passes 2026-08-21; raw accelerometer rate re-checked 2026-10-09; API plans, Withings+ requirement, security and compliance statements, API reference and FDA 510(k) list re-verified 2026-10-10; cellular uniqueness claim, Strengths sampling rate and Schyvens figure corrected 2026-10-10 |

## Summary

- Withings is the wrong shape to compare directly against Apple/Fitbit/Garmin, and that is precisely why it belongs in this module. It is a **connected-health-device company with a purpose-built decentralised clinical trials business** (Withings Health Solutions), not a fitness-wearable company. Its distinguishing capabilities are:

1. **Medically-oriented, regulated devices**, blood pressure monitors, weighing scales with body composition, ECG-capable hybrid watches, which cover measurement domains no wrist fitness tracker touches.
2. **Cellular connectivity.** Withings offers device variants that transmit over cellular without a paired smartphone. For elderly, low-digital-literacy, or rural cohorts this **eliminates the single largest source of missing data in remote studies**, the participant's phone. Withings is not alone here: Ametris's CentrePoint Data Hub is a "cellular-powered communication gateway" that sends Insight Watch and LEAP data from the participant's home to the CentrePoint Cloud (ametris.com/centrepoint, read 2026-10-10; see `ametris-actigraph.md`). Withings' distinction is that its cellular options are built into consumer-priced measurement devices such as BP monitors and scales rather than a separate hub alongside an enterprise trial platform.
3. **An Advanced Research API** giving contracted partners access to **raw accelerometer and raw PPG** signals, a genuine raw-data path on a consumer device. Its public overview and raw-data guide were removed in late October 2026, so whether it is still offered is **unclear** (2026-10-30).

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
| ECG | ScanWatch and ScanWatch 2 single lead; Move ECG; BPM Core; Body Scan 6-lead | Full single-lead waveform in microvolts through Heart v2 - Get (Health Data API), not the Raw Data API, so raw mode is not needed [13] | ScanWatch 300 Hz, 30 s; Move ECG 300 Hz, 30 s; BPM Core 500 Hz, 20 s [13] | Plan gating not stated. The plans page lists ECG among "FDA/CE cleared biomarkers" on Advanced Biomarkers only, so whether a Start for Free or Enterprise app can call Heart v2 needs Withings (2026-10-10). |
| Accelerometer | ScanWatch, 3-axis | Raw via the Advanced Research API in raw mode | About 24.824 Hz in the documented raw mode, plus or minus 4 g, about 2 mg sensitivity. The overview page's "25 Hz by default (up to 100 Hz)" describes the sensor, and no documented setting reaches 100 Hz. | Raw capture must be activated via API first. Whether a contract can unlock a higher rate needs Withings to confirm (re-checked 2026-10-09). |
| Gyroscope | Unclear | Unclear | Unclear |  |
| Magnetometer | Unclear | Unclear | Unclear |  |
| Temperature | ScanWatch 2 | Unclear | Unclear |  |
| SpO2 | ScanWatch and ScanWatch 2 | Derived SpO2 through the Health Data API; the plans page lists SpO2 among "FDA/CE cleared biomarkers" on Advanced Biomarkers only [8, 14] | Spot-check readings (the cleared indication under K201456) [21] | No raw SpO2 signal is documented beyond raw red and infrared PPG in raw mode. |
| GPS | Unclear | Unclear | Unclear |  |
| Barometer / altimeter | ScanWatch 2 | Unclear | Unclear |  |
| EDA | Body Scan, for nerve assessment | Unclear | Unclear |  |
| Ambient light | Unclear | Unclear | Unclear |  |
| Other | Body Scan weight and segmental composition; BPM oscillometric blood pressure; Sleep and Sleep Rx ballistocardiography with sleep staging, HR, respiratory rate, snoring and apnoea detection; BeamO digital stethoscope | Summaries via the standard API; BeamO stethoscope audio retrievable as a signal [14, 25] | Per measurement; stethoscope A-law G.711, 4 kHz, 16-bit samples [25] | Plan gating for the stethoscope signal is not stated. |

**Verification.** From Withings' Advanced Research API and product documentation as recorded in the Module 1 passes; see the notes below for the raw-mode constraints in full. The ECG, SpO2 and Other rows were updated 2026-10-11 from the vendor fact record (`facts/withings.yaml`).

### Notes from earlier verification passes

### ScanWatch raw-data capability (Advanced Research API / Raw Data API)

| Signal | Detail |
|---|---|
| **3-axis accelerometer** | ±4g range. Samples at **25 Hz by default, up to 100 Hz** per the Advanced Research API overview; see the 2026-10-09 reconciliation note below. |
| **PPG (optical)** | **3-wavelength digital photoplethysmograph, green, red, and infrared** (some configurations single green LED). |
| Effective sampling rate | Both sensors sample at **approximately 24.824 Hz** |
| Device support | **Withings ScanWatch only** |
| ECG raw waveform | Not part of the Raw Data API. **Corrected 2026-10-11:** the full waveform is a separate Health Data API service (Heart v2 - Get); see the ECG row above [13] |

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

- **Patient Insights on the BPM Pro 2 only (Verified, 2026-10-10).** Targeted questionnaires shown on the blood pressure monitor's touchscreen, drawn from a Withings library or custom-built by Withings, and retrieved through survey and answer endpoints [15]. The plans page puts symptom tracking and questionnaires on Advanced Biomarkers only [8].
- No phone or watch survey/EMA layer. Otherwise surveys and ePRO must come from a separate system. In decentralised clinical trials Withings devices are commonly integrated *into* a DCT platform (e.g. the Medable partnership) which supplies the ePRO layer.

## Researcher and Study Management Features

- Provided through **Withings Health Solutions** rather than a self-serve portal:
- Device logistics and provisioning at scale.
- Cellular device management (no participant setup).
- Integration into RPM platforms, DCT platforms, and CROs.
- Withings states it works with pharmaceutical groups and CROs on real-world data collection in decentralised trials, and will "help find the best way to retrieve and adapt data" via cellular connectivity, mobile app, an RPM platform, API, or other routes.

- This is a **services-and-integration model**, not a self-service research console. It suits funded clinical trials better than investigator-initiated academic studies with small budgets.

### Research program and academic data access (added 2026-10-10)

- **Two research routes exist, both gated:**
  - **Advanced Research API.** Withings describes it as "Designed for research groups, universities, and advanced health studies", giving "direct access to raw sensor data": accelerometer "25Hz by default (up to 100Hz)" and PPG with three LEDs or one, **ScanWatch only**, by contacting Withings (developer page re-read 2026-10-10, **Verified**; the page was removed in late October 2026 and is now quoted from a Wayback capture of 2026-10-13). Contract terms and price are not published.
  - **Advanced Biomarkers plan** ("Clinical studies & AI research"). Custom-priced; adds FDA/CE-cleared biomarkers (ECG, AFib, SpO2, vascular age, AHI, "EDA/NHS"), risk scores, symptom tracking and questionnaires, an "AI model training contract", anonymisation, and a "Clinical study support team" add-on (plans page, **Verified** that these are offered; the cleared-biomarker wording is Withings' own).
- **How to apply (Verified, 2026-10-30).** Contact Withings and sign a contract. The Advanced Research API link and the raw-data page contact were on pages removed in late October 2026; the Health Solutions study request form is still live. No review criteria or turnaround time is published [26].
- **Withings' own in-app research (Verified, 2026-10-10).** Withings runs research programs inside the Withings app, joined by consent and left by unchecking "Research Center". This is Withings' research use of consumer data, not a route for outside study teams [19].
- **What a low-budget academic study can get without a contract:** the Start for Free plan's derived data (activity, sleep, body, heart) for up to 10 users, more after a Withings review, at "Standard" rate limits, EU-hosted. **From 12 October 2026**, participants whose Withings accounts are created after that date need a paid Withings+ membership to share data with a free-plan app, and Withings says this also applies to sharing via Apple Health or Google Health. Withings says the requirement can be removed for "Research partners", but the terms for that are not published.
- **How it differs from commercial access:** the plans are the same for academic and commercial customers; there is no published academic price. Raw signals and the AI-training right come only by contract. No maximum history depth is published for any plan (not public, 2026-10-10). For retention, see Data Access and Export.
- **Is it active?** **Unclear** (2026-10-30). Both public pages, the Advanced Research API overview and the raw-data integration guide, were removed between 2026-10-13 and 2026-10-26 and now redirect to the developer portal home, with no notice. The live API reference still lists the Rawdata v2 services as "part of the Advanced research API", ScanWatch only, and the plans page still says "Trusted by 100+ research labs". Whether the program continues, moved behind the Partner Hub login or closed needs Withings. Which ScanWatch generations (2, Light, Nova) are covered is not stated [1, 26].

## Data Access and Export

| Route | Content | Gate |
|---|---|---|
| Public Health Data API | Processed measures, sleep, heart, activity | App registration; Start for Free plan self-serve up to 10 users; Withings+ needed for participants with accounts created after 12 October 2026 unless on Enterprise or Advanced Biomarkers |
| Raw Data API / Advanced Research API | Raw ACC + PPG from ScanWatch | **Contracted partners only** |
| Cellular device direct-to-cloud | All standard measures | Device purchase; no participant phone needed |
| Participant self-export | Withings account data export as a CSV file [27] | GDPR-backed |
| Contract routes | SDK for iOS and Android (device setup and sync inside the partner's app), Cellular Dropship and Bulkship, Withings RPM, OnSite Mode [16] | Contract |

- **Rate limits (2026-10-10):** Enterprise and Advanced Biomarkers "1,500+ requests/minute"; Start for Free is labelled only "Standard" (**Verified**, plans page). A search snippet of an earlier version of the page gave 120 requests/minute for the free tier (**Reported**, not on the current page). Throttled calls return body status 601 "Too many request" (**Verified**, API reference). Withings asks integrators not to poll a user more than once every 10 minutes [16].
- **History depth (not public, 2026-10-10).** No maximum look-back is published. Endpoints take start and end dates or `lastupdate`, with per-call windows (intraday activity 24 hours per call, one sleep endpoint 7 days per call) [13].
- **Tokens.** Refresh tokens last one year. A study that does not refresh a participant's token within a year loses access until the participant re-authorises [16].
- **Retention (Verified, 2026-10-21).** The 2018 API terms set no retention period for partners and said copies may remain after material is removed. Withings rewrote its General Terms of Use on 13 October 2026; the 2018 agreement is no longer on its terms page, which now says partner terms are on the developer portal (not located 2026-10-21). The new terms also say a participant's sharing with third-party services covers only data generated after sharing is enabled. Withings keeps personal data only as long as necessary. If a participant's Withings+ lapses, sharing pauses but historical data is not deleted [8, 18, 19].
- **Inactive-account deletion (conflict, Unclear, 2026-10-21).** Withings closes inactive accounts, but the threshold differs. The French General Terms (13 October 2026) delete accounts with more than 3 years without login, device connection or email click; the US General Terms (same date) say Withings may deactivate an account after 5 years without login; the privacy policy (2026-03-04) says 10 years, with a 90-day email warning. Matters for longitudinal studies on participants' own accounts [18, 19].

## APIs, SDKs, and Extensibility

- REST + OAuth 2.0 via the Withings Partner Hub (`developer.withings.com`). The full API reference at `developer.withings.com/api-reference/` is public, with no login (re-checked 2026-10-10; the 2026-08-21 pass recorded it as login-gated).
- Notification/webhook mechanism for new measurements (referenced by Withings' integration guide; not verified in detail here).
- **SDK for iOS and Android, contract only (Verified, 2026-10-10).** It embeds device setup and sync in the partner's own app; it does not make devices programmable [16].
- **Change notice.** Withings gives one month's notice of major API changes, up to three months for business-critical ones. Some sleep fields (`durationtosleep`, `durationtowakeup`) are marked deprecated [13, 28].
- Documented integrations with DCT and RPM platforms.

## Deployment and Infrastructure

- Vendor cloud. No self-hosting, but a **choice of cloud**: Withings describes an EU Medical Cloud based in France and a US Medical Cloud (security and compliance page, read 2026-10-10). The plans page puts the free plan on EU hosting and offers US hosting and French HDS hosting on Enterprise and Advanced Biomarkers. Consumer and European B2B data sit in BSO data centres in France; US B2B data on Google Cloud in the US. Health-data backups go to Google Cloud Storage in Dublin, encrypted with a key Withings holds, and Withings' HDS guarantees table (March 2026) flags possible access to that backup from the United States under non-European law [8, 20, 29]. **Corroborated** (vendor statements).

## Participant Experience

- This is where Withings is strongest and most differentiated:

- **Cellular devices require no smartphone, no app, no pairing, and no participant technical action.** A participant steps on a scale or uses a BP cuff and the reading reaches the study. For geriatric, low-literacy, low-income, or rural cohorts this transforms feasibility.
- **ScanWatch battery life of ~30 days** in normal mode, effectively no charging burden. (Raw mode destroys this; see above.)
- **The Sleep mat requires no wearing at all**, placed under the mattress, it collects nightly sleep data with zero adherence burden. For populations who will not tolerate a wearable (dementia, paediatric, sensory sensitivity), this is a genuinely distinct capability.
- Hybrid analogue watch styling is more socially acceptable than sport watches in some populations.
- iOS and Android.

## Privacy, Security, and Compliance

- Withings devices in the medical lines carry regulatory clearances. The US FDA 510(k) list is now checked (see below); clearance status in other markets and the exact feature scope of each clearance were not verified and vary by jurisdiction.
- **Compliance statements (re-checked 2026-10-10; Corroborated, vendor statements without linked certificates):** Withings' developer security page says its EU Medical Cloud, based in France, "is GDPR compliant, HDS, HIPAA and ISO 27001:2017 certified", and its US Medical Cloud "is a US based, ISO 27001:2017 certified and HIPAA compliant", adding "Withings complies with HIPAA rules and regulations". The plans page offers "DPA, BAA and security questionnaire" on Enterprise and Advanced Biomarkers only, not on Start for Free. No SOC 2 report or attestation is mentioned (not public, 2026-10-10). HIPAA and GDPR remain vendor statements. (The 2026-08-21 text said HIPAA, ISO and DPA terms were not found.)
- **Certificates (Verified on the certificate, 2026-10-10).** AFNOR Certification ISO/IEC 27001:2022, certificate 2020/86561.8, valid 2026-04-22 to 2029-04-21, scope including the Withings Public API, SDK and devices, sites Issy-les-Moulineaux and Boston. Also ISO/IEC 27701:2019 (2023/104367.5) and HDS v2 (2020/86563.8). The developer page's "ISO 27001:2017" and the data-security page's HDS "version 1.1" are older than these certificates. The PDFs are hosted by Withings; AFNOR's online register was not checked [22, 20].
- **AI use.** Partner AI model training rights come only with an AI model training contract on Advanced Biomarkers [8]. Withings itself uses pseudonymised profile and health data for AI-driven personalisation and product and algorithm improvement, per its privacy policy [19].
- **FDA 510(k) clearances (Verified, openFDA, 2026-10-10):** Withings Blood Pressure Monitor K110872 (2011) and K133125 (2014); Withings Thermo K160544 (2016); Scan Monitor K201456 (2021-10-05); Scan Monitor 2.0 K230812 (2023-08-23), which the FDA listing ties to Body Scan and BodyScan 2, not the watch; Withings Sleep Rx K231667 (2024-09-06); Withings ECG App K240795 (2025-06-15); Withings BeamO K252474 (2025-11-10). CE-mark scope per device was not checked [11, 21].
- **K201456 covers ScanWatch and ScanWatch 2 (HWA09, HWA10).** Its cleared indications are single-channel ECG with AFib detection and spot-check SpO2 in adults, so the watch's SpO2 is cleared under this 510(k) itself; no separate SpO2 510(k) exists. Product code DPS, subsequent codes DQA (oximeter) and DXH [21].
- **Blood pressure monitors under Transtek 510(k)s.** The FDA device listing places BPM Connect and BPM Connect Pro under Guangdong Transtek's K223374 (2023-06-30), and BPM Pro 2 and BPM Vision under K240102 (2024-04-29). The 510(k) records name Transtek, not Withings [23].
- **Recall Z-1280-2023 (Class II, Open, Classified).** Scan Monitor/ScanWatch HWA09 under K201456, initiated 2022-12-19; a software bug skipped the required physician activation and review of ECG. An earlier recall, Z-2829-2018 (Nokia BPM+, K133125), is Completed. No warning letter was found [24].
- **Do not infer regulatory clearance of a device from the existence of a clinical trials business.**

## Pricing

- **Devices (US store, Verified 2026-10-10):** ScanWatch 2 USD 369.95 (38 mm and 42 mm), ScanWatch Light USD 249.95, ScanWatch Nova USD 599.95 [30]. Professional and cellular devices in the Health Solutions catalogue carry no public price.
- **Public API:** Start for Free plan has no fee, but from 12 October 2026 participants with Withings accounts created after that date need their own **Withings+** membership to share data with a free-plan app; Withings says this cannot be avoided by routing through Apple Health or Google Health. Enterprise and Advanced Biomarkers are custom-priced by active users (and biomarkers); on those plans Withings says users "do not subscribe individually and there is no per-member charge". **Withings+ (US):** USD 9.95 per month, agreed by every source. The annual price is in conflict (Unclear, 2026-10-10). The live US store and its Withings+ purchase terms say USD 99.50 per year; the Withings+ FAQ (updated 2025-10-14) and the bundle-offer terms say USD 99.95. The store is probably current, but that is not confirmed [17].
- **Fee reservation and commitments.** The 2018 developer agreement reserved Withings' right to charge for the API and change its fees; since the 13 October 2026 terms rewrite it is no longer on Withings' terms page, and the partner terms that replace it were not located [18]. No minimum term, order or user count is published for Enterprise, Advanced Biomarkers or the research API (not public, 2026-10-10). No academic or research discount is published for devices, Withings+ or API plans (not public, 2026-10-10) [8].
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

- The medical-grade framing is defensible for the **non-wearable** devices, not the watch. BPM blood pressure monitors and Body scales are the clinically validated products with regulatory clearances; the ScanWatch's FDA-cleared features are **single-lead ECG for AFib detection and spot-check SpO2 in adults** (K201456), not sleep staging. Withings publishes a device-validation studies page and a study index spanning hypertension, diabetes, surgical recovery, sleep and HIV research. **Reported**, individual studies not reviewed.

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
- No survey/EMA capability on the phone or watch; on-device questionnaires exist only on the BPM Pro 2 (Patient Insights, Advanced Biomarkers plan).
- Not a general activity-tracking platform, step/activity outputs are secondary to the measurement devices.
- HIPAA and GDPR are vendor statements and no SOC 2 is published; ISO 27001:2022, ISO 27701 and HDS rest on certificates hosted by Withings. BAA and DPA only on paid plans.
- Inactive participant accounts are closed after 3, 5 or 10 years depending on which Withings document applies (conflict, 2026-10-21).

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
- Studies requiring integrated surveys/EMA without a separate platform (only the BPM Pro 2 shows questionnaires).

## Open Questions

- *(Directed to Withings: https://www.withings.com/us/en/health-solutions/research-clinical-trials and the Partner Hub at https://developer.withings.com/)*

- **Is the Advanced Research API still offered after its public pages were removed in late October 2026, and what are the terms and cost of a contract? Will Withings contract with an individual academic investigator or only with institutions/sponsors?**
- Will the raw-data programme extend beyond ScanWatch to ScanWatch 2 or other devices?
- Answered 2026-10-11: the ECG waveform is documented in the API reference (Heart v2 - Get). Still open: is Heart v2 callable on Start for Free or Enterprise, or only on Advanced Biomarkers? Same question for the BeamO stethoscope signal.
- Can a contracted partner configure the ScanWatch accelerometer above the documented ~24.824 Hz raw-mode rate, up to the 100 Hz the overview page cites? Both pages re-read 2026-10-09 and neither documents a rate setting.
- Precise raw-data file structure, retrieval mechanics, volume, and any retention window on Withings' side.
- Historical depth and backfill for the Public Health Data API (not published as of 2026-10-10). Where the partner terms now live, and what they say on fees and retention, is open since the 13 October 2026 rewrite; which inactive-account rule applies (US 5, France 3, privacy policy 10 years) is open.
- Which Withings+ annual price is current in the US, USD 99.50 (store) or USD 99.95 (FAQ)?
- Does a research partner on a free plan qualify for the Withings+ exemption, and on what terms?
- Which plan includes the Raw Data API, and at what price?
- **Per-device regulatory clearance and validation-protocol compliance** (especially BP monitors against ESH/AAMI/ISO 81060-2, and ECG/SpO2 clearances outside the US; US 510(k)s are listed under Privacy, Security, and Compliance).
- Partly answered 2026-10-10: HIPAA and GDPR are vendor-stated; DPA and BAA are offered on Enterprise and Advanced Biomarkers; EU or US cloud. The ISO 27001 2017 versus 2022 conflict is resolved in favour of 2022 by the AFNOR certificate (valid to 2029-04-21). Still open: SOC 2, ISO 13485, and a check of AFNOR's online register.
- Cellular device coverage by country and carrier, and cost of the cellular data component.
- Sleep mat validation evidence for staging and apnoea detection.

## Vendor Fact Record

<!-- facts:begin -->
*Generated from the fact record by `tools/facts/generate.py`. Edit the record, not this block.*

**Research access**

| Fact | Value |
|---|---|
| Formal research or academic program (name, what it offers) | Two research routes. (1) Advanced Research API: raw ScanWatch accelerometer and PPG for research institutions, under contract; its public overview page was removed in late October 2026 and its current status is unclear (see program_status). (2) The Advanced Biomarkers API plan, marketed for clinical studies and AI research (cleared biomarkers, custom device provisioning, anonymization, AI training rights). Withings Health Solutions also offers study partnerships and a study request form. [V, 2026-10-30]<br>**Withings' own in-app research programs (consumer):** Withings runs its own research programs inside the Withings app, joined by consent and left by unchecking "Research Center" in the app's notification center. [V, 2026-10-10] |
| Who can join the research program | Aimed at research groups, universities and advanced health studies. Raw data access is limited to contracted partners. No further eligibility criteria are published. Both pages stating this were removed in late October 2026 (Wayback captures cited). [V, 2026-10-30] |
| How to apply, and any approval or review step | Contact Withings and sign a contract. The Advanced Research API contact link and the raw-data page contact were on pages removed in late October 2026; the Health Solutions study request form is still live. No review criteria or turnaround time is published. [V, 2026-10-30] |
| Whether the program is active, paused, renamed or closed | Unclear |
| Whether the general developer or API program is open to new applicants | Open and self-serve. The Public API needs no contract and apps are created in the developer dashboard. From 2026-10-12, Withings accounts created after that date need a Withings+ membership to share data with Start for Free apps, unless the app is on Enterprise or Advanced Biomarkers. [V, 2026-10-10] |
| Participant or user limits before approval or by tier | **Start for Free plan:** 10 active users, raised to a use-case level once Withings reviews the app (an app review form of about 10 questions). An active user is one whose account is connected with a valid authorization. [V, 2026-10-10]<br>**Enterprise and Advanced Biomarkers plans:** Unlimited active users. [V, 2026-10-10] |
| How academic access differs from commercial or consumer access | No separate academic tier or academic price. Plans are organised by scale and biomarkers. Research use runs through the contracted Advanced Research API or the Advanced Biomarkers plan, and research partners are one of the use cases for which the end-user Withings+ requirement can be removed. [C, 2026-10-10] |

**Pricing**

| Fact | Value |
|---|---|
| Device or hardware list price | **ScanWatch 2 (US store):** USD 369.95 (38 mm and 42 mm) [V, 2026-10-10]<br>**ScanWatch Light (US store):** USD 249.95 [V, 2026-10-10]<br>**ScanWatch Nova (US store):** USD 599.95 [V, 2026-10-10] |
| Consumer subscription or membership price | **Withings+ (US):** USD 9.95 per month (all sources agree). The annual price differs: the live US store and its Withings+ purchase terms say USD 99.50 per year; the Withings+ FAQ (updated 2025-10-14) and the Withings+ terms for bundle offers say USD 99.95 per year. (conflict) [U, 2026-10-10] |
| Research or academic pricing or discount | Not public [2026-10-30] |
| Fees for API, SDK, platform or data access | Start for Free is free. Enterprise is custom-priced on active users; Advanced Biomarkers is custom-priced on active users and biomarkers. Figures are not published. On the paid plans the app pays no per-member Withings+ charge. The 2018 developer agreement reserved the right to charge for the API; since the terms rewrite of 13 October 2026 it is no longer on Withings' terms page, and the partner terms it points to were not located. [V, 2026-10-10] |
| Minimum order, term or commitment | Not public [2026-10-30] |
| Whether pricing requires contacting sales | Yes for Enterprise, Advanced Biomarkers and raw-data research access (custom pricing, "Talk to our team"). No for Start for Free. [V, 2026-10-10] |

**Data access and terms**

| Fact | Value |
|---|---|
| Raw signals available to researchers, and by which route | **Advanced Research API (ScanWatch, contracted partners):** Raw 3-axis accelerometer and PPG (three wavelengths, green, red and infrared, or green only depending on device) via the Rawdata v2 Activate, Deactivate and Get services. Raw mode disables every other watch feature and cuts ScanWatch battery life to 3 to 4 days on continuous capture. [V, 2026-10-30]<br>**ECG waveform (Heart v2, Health Data API):** Full single-lead ECG waveform in microvolts through Heart v2 - Get: ScanWatch and Move ECG 30-second recordings, BPM Core 20-second recordings. Not part of the Raw Data API, so it does not need raw mode. [V, 2026-10-10]<br>**Stethoscope signal (BeamO):** Digital stethoscope audio from BeamO, retrievable as a signal (A-law G.711, 4 kHz, 16-bit samples). [V, 2026-10-10] |
| Derived or processed metrics available to researchers | Activity, sleep, body composition, heart rate, HRV, SpO2, temperature, blood pressure and more via the Health Data API. Core biomarkers (activity, sleep, body, heart) on every plan; FDA/CE cleared biomarkers (ECG, AFib, SpO2, vascular age, AHI) and risk scores only on Advanced Biomarkers. [V, 2026-10-21]<br>**Patient Insights questionnaires (BPM Pro 2):** On-device questionnaires on the BPM Pro 2 touchscreen, managed and retrieved through survey and answer endpoints, from a Withings library or custom-built by Withings. The plans page puts symptom tracking and questionnaires on Advanced Biomarkers only. [V, 2026-10-10] |
| Documented sampling rates or temporal resolution | **ScanWatch raw accelerometer and PPG:** About 25 Hz; the raw-data page gives 24.824 Hz for both sensors. The research overview says the accelerometer samples at 25 Hz by default, up to 100 Hz, but no documented API setting selects a higher rate. [V, 2026-10-30]<br>**ECG waveform (Heart v2):** ScanWatch 300 Hz (30 s); Move ECG 300 Hz (30 s); BPM Core 500 Hz (20 s). [V, 2026-10-10] |
| How far back data can be retrieved | Not public [2026-10-10] |
| Export, API, SDK or file routes | Public Health Data API (OAuth 2.0 REST plus webhooks, no contract); contract-only routes: SDK for iOS and Android (device setup inside the partner's app), Cellular Dropship and Bulkship, Withings RPM and OnSite Mode; Advanced Research API for raw data; participant CSV export from the Withings account. Apple Health and Google Health sharing are covered by the Withings+ requirement from 2026-10-12. Refresh tokens last one year. [V, 2026-10-21] |
| API rate limits | Enterprise and Advanced Biomarkers: 1,500+ requests per minute. Start for Free: "Standard", no number published. Withings asks integrators not to poll a user more than once every 10 minutes; excess calls return status 601. [V, 2026-10-10] |
| Terms on retaining, storing or deleting data | **API partners and Withings' own retention:** The 2018 API terms set no retention period for partners and said copies may remain after material is removed; since 13 October 2026 Withings' terms page says partner terms are on the developer portal, where they were not located on 2026-10-21. Withings keeps personal data only as long as necessary. If a participant's Withings+ lapses, sharing pauses but historical data is not deleted. [V, 2026-10-21]<br>**Inactive participant accounts:** Withings closes inactive accounts, but the threshold differs: the French General Terms (updated 13 October 2026) delete accounts with no login, no device connection and no email click for more than 3 years; the US General Terms (same date) say Withings may deactivate an account after 5 years without a login; the privacy policy (version of 2026-03-04) says 10 years, with a 90-day email warning. (conflict) [U, 2026-10-21] |
| Terms on using data to train AI or ML models | **Partner data (API plans):** AI model training rights come only with an AI model training contract on the Advanced Biomarkers plan; the comparison table marks them absent on Start for Free and Enterprise. The 2018 API terms do not mention AI. [V, 2026-10-10]<br>**Withings' own use of consumer data:** Withings uses pseudonymised profile and health data for AI-driven personalisation and for product and algorithm improvement, per its privacy policy. [V, 2026-10-10] |
| Announced shutdowns, deprecations or migrations, with dates | From 2026-10-12, Withings accounts created after that date need an active Withings+ membership to share data with Start for Free apps, including through Apple Health and Google Health; existing accounts are unaffected and Enterprise or Advanced Biomarkers can lift it. Withings gives one month's notice of major API changes, up to three months for business-critical ones. Minor: some sleep fields (durationtosleep, durationtowakeup) are marked deprecated. [V, 2026-10-10] |

**Compliance and regulatory**

| Fact | Value |
|---|---|
| Whether a HIPAA Business Associate Agreement is offered | Offered on Enterprise and Advanced Biomarkers, not on Start for Free, per the plan comparison table. [C, 2026-10-10] |
| Whether a data processing agreement is offered | Offered on Enterprise and Advanced Biomarkers (DPA and security review); not on Start for Free. [C, 2026-10-10] |
| Published HIPAA statement | Withings states it complies with HIPAA and that its US Medical Cloud is HIPAA compliant; US-hosted HIPAA environment only on Enterprise and Advanced Biomarkers. A HIPAA Compliance Guide is published. [C, 2026-10-10] |
| Published GDPR statement | Withings states its EU-hosted cloud in France is GDPR compliant, on all API plans. [C, 2026-10-10] |
| ISO/IEC 27001 status and evidence | Certified by AFNOR Certification to ISO/IEC 27001:2022 (certificate 2020/86561.8), valid 2026-04-22 to 2029-04-21. Scope includes the Withings Public API, SDK and devices; sites Issy-les-Moulineaux and Boston. Also ISO/IEC 27701:2019 (2023/104367.5) and HDS v2 (2020/86563.8) certificates. [V, 2026-10-10] |
| SOC 2 status and evidence | Not public [2026-10-10] |
| FDA clearances, from the FDA database | **ScanWatch, ScanWatch 2 (ECG and SpO2):** 510(k) K201456 "Scan Monitor" (Withings SA, cleared 2021-10-05, product code DPS, subsequent codes DQA (oximeter) and DXH). The cleared indications cover single-channel ECG with AFib detection and spot-check SpO2 in adults. The FDA registration and listing database lists ScanWatch (HWA09) and ScanWatch 2 (HWA10) under K201456. No separate SpO2 or pulse-oximetry 510(k) under a Withings applicant was found. [V, 2026-10-10]<br>**ScanWatch recall (2023):** Recall Z-1280-2023 (event 91523, initiated 2022-12-19) of Scan Monitor/ScanWatch HWA09 under K201456: a software bug skipped the required physician activation and review of ECG. Class II; status Open, Classified. [V, 2026-10-10]<br>**Withings ECG App:** 510(k) K240795 "Withings ECG App", cleared 2025-06-15, product code QDA (OTC ECG software). [V, 2026-10-10]<br>**Body Scan, BodyScan 2:** 510(k) K230812 "Withings Scan Monitor 2.0", cleared 2023-08-23, product code DPS; FDA listing names Body Scan (WBS08) and BodyScan 2 (WBS15). [V, 2026-10-10]<br>**Sleep Rx:** 510(k) K231667 "Withings Sleep Rx", cleared 2024-09-06, product code MNR. [V, 2026-10-10]<br>**BeamO, BeamO Pro:** 510(k) K252474 "Withings BeamO (SCT02)", cleared 2025-11-10, product code DPS (listing adds SDV and DQD). [V, 2026-10-10]<br>**Blood pressure monitors under Transtek 510(k)s (BPM Connect, BPM Connect Pro, BPM Pro 2, BPM Vision):** Cleared under Guangdong Transtek 510(k)s that Withings lists its devices under: K223374 (2023-06-30) for BPM Connect and BPM Connect Pro; K240102 (2024-04-29) for BPM Pro 2 and BPM Vision. [V, 2026-10-24]<br>**Older Withings-applicant devices:** K160544 Withings Thermo (2016-06-17, FLL); K110872 (2011-05-20) and K133125 (2014-03-24) Withings blood pressure monitors (DXN). [V, 2026-10-10] |
| Where data is stored, and residency options | Consumer and European B2B data hosted in France (BSO data centres); US B2B data on Google Cloud in the US. Start for Free apps get the EU-hosted cloud; US hosting and French HDS hosting need Enterprise or Advanced Biomarkers. Health-data backups go to Google Cloud Storage in Dublin, encrypted with a key Withings holds. [C, 2026-10-10] |

<!-- facts:end -->

## Key Links

- Official site: https://www.withings.com/
- Health Solutions, research & clinical trials: https://www.withings.com/us/en/health-solutions/research-clinical-trials
- Research page: https://www.withings.com/en-us/pages/research
- Partner Hub (developer portal): https://developer.withings.com/
- API reference (public, no login): https://developer.withings.com/api-reference/
- **API plans:** https://developer.withings.com/developer-guide/v3/withings-solutions/withings-api-plans/ (content at https://static.withings.com/content/api/plans/plans.html)
- Security and compliance: https://developer.withings.com/developer-guide/v3/withings-solutions/security-and-compliance/
- **Advanced Research API** (removed from the live site in late October 2026; Wayback capture): https://web.archive.org/web/20261013090128/https://developer.withings.com/developer-guide/v3/withings-solutions/research-apis/
- **Raw data documentation** (removed from the live site in late October 2026; Wayback capture): https://web.archive.org/web/20260521180015/https://developer.withings.com/developer-guide/v3/integration-guide/public-health-data-api/data-api/raw-data/
- For health professionals: https://www.withings.com/us/en/for-professionals

## Sources

1. Withings, Advanced Research API. https://developer.withings.com/developer-guide/v3/withings-solutions/research-apis/ (accessed 2026-08-21). **Primary.** Establishes ScanWatch-only support, 3-axis accelerometer at 25 Hz default up to 100 Hz, PPG with three LEDs (green/red/IR) or one (green), the targeting at research groups and universities, and that access is gated by contacting Withings. Re-read 2026-10-09: wording unchanged, still "samples at 25Hz by default (up to 100Hz)" and still ScanWatch-only. Removed from the live site between 2026-10-13 and 2026-10-26 (302 to the portal home); quoted since 2026-10-30 from the Wayback capture of 2026-10-13.
2. Withings, Raw data documentation. https://developer.withings.com/developer-guide/v3/integration-guide/public-health-data-api/data-api/raw-data/ (accessed 2026-08-21). **Primary.** Establishes the ±4g accelerometer range, the ~24.824 Hz effective sampling rate for both sensors, "contracted partners only" access, the requirement to activate raw capture via API, the disabling of all other device features in raw mode, and the 4 to 7× battery drain reducing life to 3 to 4 days. Also establishes that ECG is not listed among Raw Data API types. Re-read 2026-10-09: wording unchanged, and the page also says "approximately 25 Hz" and "~2 mg" sensitivity. Removed from the live site by 2026-10-26 (302 to the portal home); quoted since 2026-10-30 from the Wayback capture of 2026-05-21.
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
13. Withings OpenAPI specification. https://developer.withings.com/openapi.yaml (accessed 2026-10-10). **Primary.** Heart v2 - Get ECG signal in microvolts; ECG sampling ScanWatch 300 Hz, BPM Core 500 Hz; Raw Data "around 25Hz"; per-call windows (24 hours intraday, 7 days for one sleep endpoint); deprecated sleep fields.
14. Withings, All available health data. https://developer.withings.com/developer-guide/v3/data-api/all-available-health-data (accessed 2026-10-10). **Primary.** Biomarkers by device and plan, including ECG signal and stethoscope.
15. Withings, Patient Insights (surveys) overview and library. https://developer.withings.com/developer-guide/v3/integration-guide/surveys/surveys-overview and https://developer.withings.com/developer-guide/v3/integration-guide/surveys/surveys-library (accessed 2026-10-10). **Primary.** On-device questionnaires on the BPM Pro 2; custom questionnaires built by Withings.
16. Withings developer summary for LLMs. https://developer.withings.com/llms.md (accessed 2026-10-10). **Primary.** No contract for the Public API; contract SDK for iOS and Android; polling no more than once every 10 minutes per user; token rotation.
17. Withings+ prices. US store https://www.withings.com/us/en/beam-o/shop ; Withings+ FAQ https://support.withings.com/hc/articles/8986672043153 ; Withings Terms and Conditions https://support.withings.com/hc/en-us/articles/11132728427921-Withings-Terms-and-Conditions (all accessed 2026-10-10). **Primary.** USD 9.95 per month; annual USD 99.50 (store) versus USD 99.95 (FAQ).
18. Withings terms. US terms https://www.withings.com/us/en/legal/api-terms-of-use ; French General Terms https://www.withings.com/fr/fr/legal/api-terms-of-use (accessed 2026-10-10, rechecked 2026-10-21). **Primary.** On 2026-10-10 the US page carried the 2018 Developer Software Agreement (copies may remain after removal; right to charge for the API). Both pages now carry General Terms of Use dated 13 October 2026: section 6.4 on sharing (Withings+ needed, with exceptions; only data after sharing starts; partner terms on the developer portal), US 5-year and French 3-year inactive-account rules.
19. Withings privacy policy. https://www.withings.com/us/en/legal/privacy-policy and PDF version of 2026-03-04 https://media.withings.com/web/legal/legal-pdf/privacy-policy/wo-en-withings-privacy-policy-20260304.pdf (accessed 2026-10-10). **Primary.** Retention "only for as long as necessary"; 10-year inactivity rule; in-app Research Center; pseudonymised data for AI personalisation and algorithm improvement.
20. Withings, Data security. https://www.withings.com/us/en/data-security (accessed 2026-10-10). **Primary (vendor statement).** BSO data centres in France for B2C and European B2B; GCP in the US for US B2B; ISO 27001:2022, ISO 27701:2019 and HDS.
21. FDA 510(k) K201456, Scan Monitor. https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K201456 ; 510(k) summary https://www.accessdata.fda.gov/cdrh_docs/pdf20/K201456.pdf ; device listing https://api.fda.gov/device/registrationlisting.json?search=k_number:K201456 (accessed 2026-10-10, summary and record page read by hand). **Primary (regulator).** Cleared 2021-10-05; ECG with AFib detection and SpO2 indications; codes DPS, DQA, DXH; ScanWatch HWA09 and ScanWatch 2 HWA10.
22. AFNOR Certification certificates hosted by Withings. ISO/IEC 27001:2022 https://media.withings.com/web/med-pro/Certificat-ISO27001.pdf ; ISO/IEC 27701:2019 https://media.withings.com/web/med-pro/certificat-27701.pdf ; HDS v2 https://media.withings.com/web/med-pro/certificat-HDS.pdf (accessed 2026-10-10). **Primary (certificate).**
23. openFDA device listings for Transtek 510(k)s. https://api.fda.gov/device/registrationlisting.json?search=k_number:K223374 and https://api.fda.gov/device/registrationlisting.json?search=k_number:K240102 ; 510(k) records https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K223374 and https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K240102 (accessed 2026-10-10). **Primary (regulator).** BPM Connect, Connect Pro, Pro 2 and Vision listed under Transtek clearances.
24. FDA recall Z-1280-2023, Scan Monitor/ScanWatch. https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfRES/res.cfm?id=198114 (accessed 2026-10-10; openFDA recall and enforcement records, page read by hand). **Primary (regulator).** Class II; Open, Classified; ECG physician activation and review skipped by a software bug.
25. Withings, Decode stethoscope signal to PCM. https://developer.withings.com/developer-guide/v3/get-signal/decode-stetho-to-pcm (accessed 2026-10-10). **Primary.** A-law G.711, 4 kHz, 16-bit samples.
26. Withings research request form https://www.withings.com/en-us/pages/research-request and research and clinical trials page https://www.withings.com/en-us/pages/research-clinical-trials (accessed 2026-10-10). **Primary.** Study request route; retrieval via cellular, app, RPM platform or API.
27. Withings support, How can I export my data. https://support.withings.com/hc/en-us/articles/360001391287-Privacy-How-can-I-export-my-data (accessed 2026-10-10). **Primary.** Participant CSV export.
28. Withings, Understand our timeline for notice. https://developer.withings.com/developer-guide/v3/maintain-your-integration/understand-our-timeline-for-notice (accessed 2026-10-10). **Primary.** One month's notice, up to three months for business-critical changes.
29. Withings HDS guarantees table (March 2026). https://media.withings.com/web/med-pro/EN_US_Representations_des_Garanties.pdf (accessed 2026-10-10). **Primary (vendor statement).** Google Cloud Storage backups in Dublin, key held by Withings.
30. Withings US store product pages. https://www.withings.com/us/en/scanwatch-2 , https://www.withings.com/us/en/scanwatch-light , https://www.withings.com/us/en/scanwatch-nova (accessed 2026-10-10). **Primary.** US list prices.
