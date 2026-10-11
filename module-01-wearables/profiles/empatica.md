# Empatica

## Quick Facts

| Field | Details |
|---|---|
| Organization | Empatica Inc. (US/Italy) |
| Category | Research- and clinical-grade wearable with an FDA-cleared health monitoring platform |
| Current status | Active |
| Platforms/devices | **EmbracePlus** and **EmbraceMini** (current); **E4 wristband** (legacy predecessor, still widely cited in the literature; E4 and its software suite sunset 14 February 2025) |
| Open source | No |
| Hosting/deployment | Empatica Cloud; Care Portal web console; AWS S3 data access keys |
| Pricing model | **Published, transparent bundle pricing for academic research**, unusual in this module |
| Last verified | 2026-10-11 (vendor fact record); earlier passes 2026-08-21, 2026-10-09 and 2026-10-10 |

## Summary

- Empatica is the platform to reach for when the research question requires **raw physiological signal from a regulated, purpose-built device** rather than a consumer product with an API bolted on. Two things distinguish it:

1. **EDA (electrodermal activity).** Empatica's wrist EDA, available as raw signal with an FDA-cleared EDA parameter, is the reason the device exists for stress, arousal, emotion, seizure, and autonomic research. **Corrected 2026-10-10:** it is not the only EDA source in this module. Samsung's Health Sensor SDK documents a raw `EDA_CONTINUOUS` tracker at 1 Hz on Galaxy Watch8 and later (Samsung data specifications, **Verified**), and the Verily Study Watch records EDA (see `emerging-platforms.md`, **Corroborated**). Among those, Empatica remains the one with a published self-serve academic plan and an FDA-cleared EDA parameter. Apple, Fitbit, Garmin, Oura, WHOOP, Polar and Withings have no EDA route.
2. **FDA clearance of the platform**, including cleared digital biomarkers. The Empatica Health Monitoring Platform was cleared in November 2022 (K221282: peripheral skin temperature, EDA, SpO2 under no-motion conditions, activity associated with movement during sleep), with later clearances adding pulse rate and respiratory rate (K230457), a Predetermined Change Control Plan for the SpO2 algorithm (K242737) and Parkinson's movement measures (K260374); EmbraceMini has its own clearance (K252981). See Privacy, Security, and Compliance. This is a materially different regulatory posture from every consumer platform here. The research Care Lab App and Care Lab Portal themselves are research use only and not FDA-cleared (corrected 2026-10-11, vendor fact record).

- Empatica also publishes **actual prices for an academic research plan**, which, after working through Garmin's "contact us", Withings' "contracted partners only", Fitabase's "we'll craft a plan", and Ametris' silence, is a significant practical advantage for grant budgeting.

## Products / Platform Architecture

- **EmbracePlus**, wrist-worn multi-sensor device, the current product.
- **EmbraceMini**, a smaller actigraphy-focused wearable sold alongside EmbracePlus (listed as "New" on Empatica's site), with its own FDA 510(k) K252981 (2025-12-22) for movement and sleep-movement monitoring. Its research-studies table covers 12 of the 17 named biomarkers, with no PPG, EDA or temperature measures. **Verified** (2026-10-10).
- **E4 wristband**, the legacy device. Empatica sunset the E4 and its whole software suite (E4 connect, manager, realtime app, streaming server and SDK) on 14 February 2025 [28]; hardware support ended 1 August 2024 per a University of Twente lab notice [29] (secondary). It appears in a very large volume of published EDA and stress research and remains the reference point in that literature. Studies replicating E4-based work should confirm signal comparability with EmbracePlus rather than assuming equivalence.
- **Empatica Cloud**, data storage and processing.
- **Care Portal**, web console for professionals to manage participants across sites and monitor digital biomarkers.
- **Care app** (Enterprise plan) / **Care Lab app** (Academic & Basic Research plan), the participant/operator-facing applications; note the plan-tier split.
- **Empatica Health Monitoring Platform**, the FDA-cleared regulatory entity encompassing device + algorithms + platform.

## Sensors and Data Streams

- Every Module 1 profile uses the same table so devices can be compared row by row. Rows are the sensors named in `CLAUDE.md`. "Present" is about the hardware; "Researcher access" is about what a study can actually obtain, which is the module's central question. "Unclear" means nothing current was verified. The convention is recorded in [`../../shared/profile-table-conventions.md`](../../shared/profile-table-conventions.md).

| Sensor | Present | Researcher access to underlying signal | Resolution or sampling | Notes |
|---|---|---|---|---|
| PPG | Yes, advanced optical (EmbracePlus only) | Raw blood volume pulse and systolic peaks (IBI) as Avro files [22]; pulse rate and pulse rate variability (RMSSD) biomarkers | 64 Hz via 5 LEDs (infrared, green, red) in Pulse Rate Pro; 4 Hz infrared via 1 LED in Actigraphy Pro; off in the other modes [20] | **Verified 2026-10-11** (vendor fact record). |
| ECG | No | Not applicable | Not applicable |  |
| Accelerometer | Yes | Raw acceleration data | Set by sensor mode, all ±16 g. Pulse Rate Pro 64 Hz, Actigraphy Pro 64 Hz, Actigraphy Optimized 32 Hz, Gyroscope Max 64 Hz, Gyroscope 100 100 Hz [20] | Sensor modes are "hardware configurations", not free rates. **Verified 2026-10-11** (vendor fact record). |
| Gyroscope | Yes, in selected sensor modes | Raw angular velocity ("with the gyroscope enabled in selected sensor modes") | 64 Hz in Gyroscope Max, 100 Hz in Gyroscope 100, ±2000 dps; off in the other three modes [20] | **Verified 2026-10-11** (vendor fact record). |
| Magnetometer | EmbracePlus none listed. EmbraceMini yes, per Empatica's clinical-trials and EmbraceMini pages [10] | No researcher stream on the academic plan; absent from the raw-data table, the sensor-mode table and the Avro stream list | Not applicable | **Verified 2026-10-11** (vendor fact record). Whether Enterprise clients get magnetometer data is not stated. |
| Temperature | Yes, digital skin temperature (EmbracePlus only) | Peripheral skin temperature | 1 Hz in every mode [20] | **Verified 2026-10-11** (vendor fact record). |
| SpO2 | Yes, on EmbracePlus (the device in K221282) | SpO2 is an FDA-cleared parameter under K221282 for "trained healthcare professionals or researchers", **under no-motion conditions only**; the 510(k) states it is "not intended for SpO2 monitoring in conditions of motion or low perfusion". The academic help centre lists SpO2 as an Enterprise biomarker [38], so academic buyers should not expect it (vendor fact record, 2026-10-11). | Range 70 to 100%, resolution 1% (510(k) summary) | **Verified 2026-10-10** (openFDA record and K221282 summary read). Accuracy 2.6% Arms over 70 to 100% in a 13-subject arterial blood gas study, not tested with motion or low perfusion. Corrected from "Unclear" to agree with the compliance section. |
| GPS | No | Not applicable | Not applicable |  |
| Barometer / altimeter | Unclear | Unclear | Unclear |  |
| EDA | Yes, ventral EDA (EmbracePlus only) | Electrical conductance at the skin surface; skin conductance level biomarker | 4 Hz in Pulse Rate Pro and Actigraphy Pro; off in the other modes [20] | The differentiating sensor. **Verified 2026-10-11** (vendor fact record). |
| Ambient light | EmbracePlus none listed. EmbraceMini yes | EmbraceMini ambient light stream and biomarker | 1 Hz (EmbraceMini) [20] | **Verified 2026-10-11** (vendor fact record). |
| Other | Unclear | Unclear | Unclear | Not verified against current documentation. |

**Verification.** **Corrected 2026-10-11 (vendor fact record).** Empatica's academic help centre now publishes every rate for all five sensor modes (Pulse Rate Pro, Actigraphy Pro, Actigraphy Optimized, Gyroscope Max, Gyroscope 100) [20]. The first mode is named Pulse Rate Pro, not "Standard" as the 2026-10-10 pass had it. PPG and EDA run only in Pulse Rate Pro and Actigraphy Pro, and Pulse Rate Pro is EmbracePlus only. EDA 4 Hz and PPG 64 Hz happen to equal the legacy E4 values, but they are now documented for EmbracePlus, not assumed. Three constraints matter for study design.

- Until 16 September 2026 the Academic & Basic Research plan offered EmbracePlus in one mode only, the one now called Pulse Rate Pro [31]. Studies created before that date run Pulse Rate Pro by default [20].
- The sensor mode "cannot be changed once the account has been created" [20]. With one study per academic account, a protocol needing two modes needs two accounts.
- The McRoberts algorithm set is Enterprise-only [32]. Gyroscope 100 computes no activity biomarkers, but its raw output is described as compatible with the McRoberts and Mobilise-D libraries, so academics can run those themselves.

### Notes from earlier verification passes

| Sensor | Detail |
|---|---|
| **Advanced optical PPG** | Clinically validated pulse rate (PR) and pulse rate variability (PRV) |
| **Ventral EDA sensor** | Measures electrical conductance changes at the skin surface, the differentiating sensor |
| **Accelerometer** | Raw acceleration data |
| **Digital temperature sensor** | Peripheral skin temperature |

- *(Superseded 2026-10-11: per-mode rates are now published; see the table above.)* Empatica describes the device as using "optimized sampling rates" to balance data quality against battery efficiency. **Specific per-sensor sampling rates for EmbracePlus were not published on the pages retrieved**, a significant documentation gap given that sampling rate is the whole point of buying a research device. (For reference, the legacy E4 sampled EDA at 4 Hz, PPG/BVP at 64 Hz, ACC at 32 Hz, and temperature at 4 Hz; **do not assume EmbracePlus matches these.**) Obtain the EmbracePlus sampling specification in writing before designing a study.

## Derived Metrics / Analytics

- Empatica supplies validated digital biomarkers computed on its platform. **The count is stated inconsistently across Empatica's own pages**, status: Unclear:
- The research-studies page lists **18 validated biomarkers**: sleep detection, pulse rate, pulse rate variability, respiratory rate, electrodermal activity (SCL), temperature, wearing detection, activity classification, steps, activity counts, actigraphy counts, MET, activity intensity, body position, and accelerometer magnitude standard deviation (among others).
- The store page for the Academic & Basic Research plan states **"over 11 digital biomarkers."**
- Another Empatica page refers to **"over 100 research-grade biomarkers."**

- The most likely reconciliation is that the tiers differ, the Academic & Basic Research plan gives "a standard suite of raw data and digital biomarkers" while the Enterprise plan gives "the complete suite." **Confirm exactly which biomarkers the academic plan includes before purchase**, because the differentiator (EDA-derived measures) may or may not be fully in the standard tier.

- **Re-checked 2026-10-09 (partly resolved).** All three figures above have changed or gone. Read as of today:
  - The research-studies page (now at https://www.empatica.com/platform/research-studies/, the `/en-eu/` path redirects) no longer states a count. It shows a table of **17 named digital biomarkers** with EmbracePlus and EmbraceMini columns: accelerometer magnitude standard deviation, acticounts, actigraphy counts, activity counts, activity classification, activity intensity, ambient light (EmbraceMini only), body position, EDA skin conductance level, METs/calories, pulse rate, pulse rate variability, respiratory rate, sleep detection, steps, skin temperature, and wearing detection. EmbracePlus covers 16 of them; EmbraceMini covers 12 (no PPG, EDA or temperature measures). **Verified.**
  - The Academic plan store page carries the same table and now says "a selection of digital biomarkers"; the "over 11" wording is gone. **Verified.**
  - The "over 100 research-grade biomarkers" line is no longer on the Care page. Empatica's homepage and clinical-trials page now say **"300+ digital measures"**, of which "Six measures carry direct FDA clearance" and the rest are described as research-grade. A November 2023 press release used 128. **Verified** for current wording.
  - Reading: the large figure is the clinical-trial measure library, and the research-studies table is what the self-serve academic product exposes. That reading is **Corroborated**, not stated by Empatica in so many words. Whether an Academic buyer can get any measure outside the 17-row table needs Empatica to confirm.
  - The same pages now list a second device, **EmbraceMini** (actigraphy-focused, FDA 510(k) for sleep, circadian rhythm and physical activity monitoring, 14+ days battery in its optimized mode). It was not profiled in the first pass.

- **Which biomarkers each mode yields (vendor fact record, 2026-10-11).** The academic help centre's biomarker list matches the 17-row table above [21]. Pulse, respiratory and EDA measures need EmbracePlus in Pulse Rate Pro. Gyroscope 100 computes no activity biomarkers. SpO2 is marked Enterprise [38]. Enterprise pages market 300+ measures, 6 of them FDA-cleared [10]. **Verified.**

- Notable in that list for methodological reasons: **actigraphy counts** and **activity counts** are provided, meaning EmbracePlus output can be made comparable to the enormous ActiGraph-based physical activity literature, a genuinely useful bridge.

## Active Data Collection

- Not a survey/EMA platform. Empatica is a sensing platform; self-report must come from elsewhere. The device's utility in seizure research does include participant/caregiver event marking, but a general EMA capability is not documented.

## Researcher and Study Management Features

- The Care Portal provides a real study console, one of only two platforms in this module (with Ametris/CentrePoint) that does:

- Create studies, sites and participant credentials. **Corrected 2026-10-11 (vendor fact record).** An academic account allows 1 study, 1 site, 1 study manager and up to 1,000 participants, and its sensor mode is fixed at creation [15][20]. Enterprise accounts manage multiple studies and sites [10], with a minimum order of 100 devices and no published participant cap [21].
- Manage **multiple sessions across participants from one device**, meaning a single device can be recycled across participants, which materially changes the cost model for sequential-cohort designs.
- **Live tracking of participant wearing time** to minimise data loss, active adherence monitoring, not post-hoc discovery.
- Onboard and offboard participants in a few clicks.
- Multi-site management (Enterprise plan only; the academic plan allows 1 site).

## Data Access and Export

| Route | Detail |
|---|---|
| **Raw data download** | **Avro format only**, from the Empatica AWS S3 bucket, in files of up to about 30 minutes with UTC timestamps [22]. Streams are accelerometer, gyroscope, blood volume pulse, EDA, skin temperature, systolic peaks (IBI), steps and tags, depending on device and mode. Empatica supplies a Python Avro-to-CSV script, and community readers exist [37]. Corrected 2026-10-11 (vendor fact record); the earlier "CSV via the Care Portal" was wrong for raw signal. |
| **Biomarker download** | CSV, from the Care Lab Portal Download Hub and the S3 bucket [25] |
| **Programmatic access** | **Data access keys via Amazon S3**, bulk, scriptable retrieval with Cyberduck, the AWS CLI or AWS SDKs [23]. Up to two active key sets at a time [24]. No other rate limit is published; the full Data Access Documentation sits inside the portal |
| **Upload latency** | The Care Lab App sends data in 30-minute batches [25]. Actigraphy Optimized syncs once a day, so data may be up to 24 hours old [20] |
| **Enterprise Cloud API** | Sold through sales to clinical trial sponsors and CROs, with developer documentation given to clients only; data still in S3 as Avro and CSV [26] |
| **Care Portal visualisation** | Biomarkers viewable in the console |
| **Cloud storage** | Data held in Empatica Cloud with historical, timestamped retrieval |
| **Real-time streaming** | **Not available.** Empatica's FAQ: data are "not viewable in real-time. This means you cannot stream data live". Re-verified 2026-10-10. Real-time seizure alerting exists only in the separate EpiMonitor product (K250515), not in the research plan. |

- The absence of real-time streaming rules Empatica out for closed-loop or just-in-time adaptive intervention (JITAI) designs that need to act on physiology within minutes. For retrospective analysis it is irrelevant.

- The S3 access-key route is a good design: it means bulk export is a first-class capability rather than a per-participant portal click, which is where many platforms fall down at scale.

## APIs, SDKs, and Extensibility

- S3-based bulk data access.
- Care Portal.
- **Corrected 2026-10-11 (vendor fact record).** A **Cloud API** exists for clinical trial sponsors and CROs, sold through sales, with full developer documentation "provided" only to clients [26]. It is not part of the academic plan. **Verified.**
- No device SDK; EmbracePlus is not user-programmable. Empatica's FAQ: "We do not provide an SDK for academic research purposes." (**Verified** 2026-10-10.)
- The legacy E4 offered a real-time BLE streaming SDK. **Resolved 2026-10-11:** the E4 SDK was sunset with the rest of the E4 suite on 14 February 2025 [28], and no research plan offers a replacement. A remote-patient-monitoring page still describes a "plug-and-play" platform SDK for building a patient app that streams EmbracePlus data, outside the research plans, with no public documentation [27]. Nothing shows it is still sold to new customers (**Corroborated**). A custom real-time EmbracePlus build exists for the DATALAND museum, so the hardware can stream, but no plan offers it.

## Deployment and Infrastructure

- Vendor cloud (Empatica Cloud, AWS-based). No self-hosting option. Research team needs only the ability to pull from S3 and store data.

## Participant Experience

- Wrist-worn. Purpose-built for continuous wear including sleep.
- **Battery life depends on the sensor mode (corrected 2026-10-11, vendor fact record).** The academic help centre gives EmbracePlus 2+, 7+, 14+, 5+ and 5+ days for Pulse Rate Pro, Actigraphy Pro, Actigraphy Optimized, Gyroscope Max and Gyroscope 100. EmbraceMini gives 7+, 14+, 3+ and 3+ days for the last four (Pulse Rate Pro is not available on it). On-device memory holds about 1.5 to 14 days of data, by mode [20]. Pulse Rate Pro, the only academic mode before 16 September 2026, runs about 2 days per charge, which matters when reading older EmbracePlus studies.
- Empatica's clinical-trials and Cloud API pages say battery "can last up to 28 days" [10][26]. No published mode reaches 28 days, so treat that figure as unsupported. It may describe an unpublished Enterprise configuration; Empatica has not said.
- An extra charger is sold separately at $42.90.
- Silicone band loops are a separate accessory at $21.90.
- The device is a medical/research device rather than a consumer product, so it offers little participant-facing engagement value, participants wear it because the study asks them to, not because they want to. Expect adherence to depend on study contact rather than device appeal.
- Multi-session device reuse supports staggered enrolment designs.

## Privacy, Security, and Compliance

- **FDA clearances (re-verified 2026-10-10 in openFDA and the 510(k) indications for use).** FDA clearance of a platform is not a blanket endorsement of every output; cite the specific clearance.
  - **K221282** (2022-11-20), Empatica Health Monitoring Platform: for "trained healthcare professionals or researchers" to remotely monitor peripheral skin temperature, electrodermal activity, SpO2 under no-motion conditions, and activity associated with movement during sleep, in ambulatory adults 18 and older in home-healthcare settings.
  - **K230457** (2023-10-30), Health Monitoring Platform with EmbracePlus, Empatica Care and Care Portal, adds pulse rate and respiratory rate (no-motion).
  - **K242737** (2025-06-06), same device as K230457 except for an authorized Predetermined Change Control Plan (PCCP) for a subcomponent of the SpO2 algorithm, per its 510(k) summary [18][34]. It is for "retrospective remote monitoring" and states "the platform does not provide real-time alerts". Corrected 2026-10-11 (vendor fact record); the profile previously credited it with pulse rate and respiratory rate.
  - **K260374** (2026-08-14), Health Monitoring Platform for Parkinson's Disease Monitoring (EmbracePlus, EmbraceMini, PKG Monitor): kinematics of tremor, bradykinesia and dyskinesia, ages 46 to 83.
  - **K252981** (2025-12-22), EmbraceMini: remote monitoring of limb or body movement and activity associated with movement during sleep.
  - Seizure products: Embrace (K172935, K181861) and EpiMonitor (K232915; **K250515**, 2025-06-19, EmbracePlus plus app, generalized tonic-clonic seizure alerts to a caregiver, ages 6 and up, prescription only).
  - **PKG System** (acquired with PKG Health, October 2025), product code GYD: K140086 (2014-08-22), K161717 (2016-09-20) and Gen 2 Plus K211887 (2022-03-11). The holder of record in openFDA is GKC Manufacturing Pty, Ltd., not Empatica [35]. Empatica's homepage claims "12 FDA clearances"; the 9 Empatica 510(k)s plus these 3 make 12, but Empatica does not say which records it counts, so that reconciliation is an inference.
  - The research Care Lab App and Care Lab Portal are research use only and not FDA-cleared.
  - The only FDA enforcement record found is a Class II recall of the consumer Embrace2 (Z-0159-2024, battery may last under 48 hours), outside the research platform. Embrace2 is no longer sold; existing subscriptions continue [39].
  - **Verified** (openFDA, https://api.fda.gov/device/510k.json?search=applicant:empatica, and the 510(k) PDFs, 2026-10-10; vendor fact record 2026-10-11).
- **Security and data governance (read 2026-10-10).** Empatica's legal page lists ISO/IEC 27001:2022 ("performed by independent third-party auditors"), ISO 13485:2016 QMS certification, MDSAP and CE certificates, and a published "Empatica Health Monitoring Platform - Data Processing Agreement". The participant privacy policy says Empatica stores User Data "on HIPAA-compliant cloud infrastructure located in US, Virginia" and retains it during the service "plus a period of 10 years after the termination" of the contract. These are vendor statements (**Corroborated**), except as noted below.
- **ISO/IEC 27001:2022 certificate, opened 2026-10-11 (vendor fact record).** TÜV Rheinland Cert GmbH, registration no. 01 153 2117571, holder Empatica Srl (Milan), valid 2025-10-31 to 2028-10-30, first certified 2023. Scope covers design and manufacture of the wearables and the monitoring software and platforms [33]. **Verified** from the certificate, though not cross-checked on TÜV's Certipedia registry. Separate TÜV Rheinland Italia certificates cover ISO 13485 (39 05 0072201, valid to 2028-05-24) and the EU MDR QMS (notified body 1936).
- **HIPAA and GDPR.** Empatica says the platform is GDPR and HIPAA compliant and that data is stored and transmitted in line with 21 CFR Part 11, HIPAA and GDPR [10][15]. Empatica Srl has appointed a Data Protection Officer [17]. Vendor statements, **Corroborated**.
- **Data residency.** Research participant data sits in an Amazon S3 bucket on AWS in Virginia, US [17][23]. No EU or regional residency option is published (**Corroborated**; Enterprise contracts may differ).
- **DPA.** The terms of service incorporate an Empatica Health Monitoring Platform Data Processing Agreement [30], also listed in the academic vendor pack with a HECVAT and an IT risk assessment [36]. The DPA itself sits behind a JavaScript-rendered Salesforce link and was not read (**Corroborated**).
- **Use of customer data.** The terms let Empatica use customer data to create digital biomarkers and anonymized data sets for its own business purposes, owned by Empatica [30]. No clause names AI or machine-learning training (**Corroborated**, since the DPA was not read).
- **Not public (2026-10-11).** No SOC 2 report or statement; the legal page and vendor-pack contents list ISO 27001 instead (**Verified** absence). No Business Associate Agreement is mentioned on any public page (**Corroborated** absence, because the DPA and the form-gated vendor pack were not read). Ask compliance@empatica.com.

## Pricing

- **Corrected 2026-08-21: Empatica's academic pricing is public, contrary to the first pass.** Read directly from the Empatica store's Academic & Basic Research plan page. **Verified.**

| Item | List | **Academic (25% off)** |
|---|---|---|
| EmbracePlus device (from) | **$1,166.40** | |
| **3-year bundle** (device + charger + 3 yr Empatica Cloud & Care Portal + service and maintenance) | **$2,332.80** | **$1,749.60** |
| **5-year bundle** (as above, 5 yr data access) | **$2,916.00** | **$2,187.00** (25% off plus a further 10% on data access) |
| EmbraceMini device | **$641.52** | |
| EmbraceMini 3-year bundle | **$1,516.32** | **$1,137.24** |
| EmbraceMini 5-year bundle | **$1,953.72** | **$1,465.29** |

- **Re-verified 2026-10-10** (store page, primary). The EmbracePlus figures are unchanged. EmbraceMini rows added (R-217).
- **How the figures fit together.** Each "bundle" list price is the device plus a platform subscription: EmbracePlus $1,166.40 + 3-year subscription $1,166.40 = $2,332.80, and + 5-year subscription $1,749.60 = $2,916.00; EmbraceMini $641.52 + $874.80 = $1,516.32, and + $1,312.20 = $1,953.72. The store page's plan data list 3-year options at $1,166.40 and $874.80 and 5-year options at $1,749.60 and $1,312.20 without naming the device; assigning the lower pair to EmbraceMini is an inference, supported by the sums matching the bundle list prices exactly. The academic price is 25% off the bundle list. Empatica's `llms.txt` lists "5-year Platform Subscription: $1,749.60", which is the 5-year subscription alone at list price; it equals the academic 3-year EmbracePlus bundle price by coincidence, so the two figures do not conflict. Checked 2026-10-10.
- **The academic price is not automatic.** Empatica's academic-discount page says "University students and Academics" are eligible for a discount code, applicants fill in a form, "Only University institutional email addresses will be considered", and the code arrives by email. **Verified** (lp.empatica.com/academic-discount-professional-plan, 2026-10-10).

- Volume discounts apply automatically at **5+ devices**. Taxes and shipping additional.

- **Renewal (added 2026-10-11, vendor fact record).** After the bundled 3 or 5 years, the subscription can be extended one year at a time per device, from $388.80 / €359.64 a year (EmbracePlus) and $291.60 / €269.73 a year (EmbraceMini) [21]. Subscriptions are only sold with devices bought from Empatica, so devices from other sources cannot be added [21]. The store offers an optional 30-day quote with no payment method, and teams needing more than 30 devices are asked to contact Empatica [15][31]. **Verified.**

- *(Superseded 2026-10-09: the store page no longer uses "11+"; see the re-check under Derived Metrics.)* The academic plan includes **"11+ digital biomarkers"** per the store page, note this conflicts with the 18 named on the research-studies page and the "over 100" claimed in platform marketing. Three different public figures. **Unclear** which biomarkers a purchaser actually receives; this is now the most consequential remaining commercial question about Empatica, because it determines whether the academic tier is sufficient for a given protocol.

- **Enterprise plan** pricing is not public and requires contacting Empatica (`llms.txt` says "enterprise pricing is not self-serve") [13]. The Enterprise minimum order is **100 devices** [21]. Cloud API fees are not public. Corrected 2026-10-11 (vendor fact record); the profile previously gave no minimum.

### Research program and academic data access (checked 2026-10-10)

- **Program:** the **Academic & Basic Research plan**, sold self-serve on Empatica's store with no application review, with a 25% academic discount by application (above). The discount code needs a university email. The terms limit Academic Subscriptions to educational institutions and qualified non-profit research organizations, used by their own staff or students for non-commercial teaching and research [30]. The platform as a whole is also sold to for-profit research institutions [17], and Enterprise qualification is decided with sales [21]. **Verified** (vendor fact record, 2026-10-11).
- **What academics get:** the device plus 3 or 5 years of Empatica Cloud data access and Care Lab Portal access, with "Access to all EmbracePlus and EmbraceMini sensor raw data and a selection of digital biomarkers across vital signs, sleep and activity" (store page). Data come by self-serve download and Amazon S3 data access keys; there is no real-time streaming and no SDK for academic research. The academic account is limited to 1 study, 1 site, 1 study manager and 1,000 participants (research-studies page, 2026-10-09), and its sensor mode is fixed when the account is created [20]. **Verified.**
- **How it differs from Enterprise (corrected 2026-10-11, vendor fact record).** The academic plan is aimed at smaller studies without a dedicated account manager, and is non-commercial only [21][30]. Until 16 September 2026 it offered EmbracePlus in one mode only, now called Pulse Rate Pro; four more modes and EmbraceMini were added that month [31]. Enterprise is for large clinical trials, with a 100-device minimum, multiple studies and sites, IRB support, audit trails, the Cloud API and quoted pricing [10][21][26]. Named Enterprise-only items are the McRoberts algorithms [32] and SpO2 [38]. Empatica's clinical-trial pages cite "300+ digital measures" (source 10). Enterprise uses the Care app rather than Care Lab (source 3). **Verified.**
- **Retention (corrected 2026-10-11, vendor fact record).** Participant data is retained during the service plus 10 years after contract end [17]. Access can be extended yearly (see Pricing). After termination the customer can retrieve its data for 60 days, must stop using the platform when the term expires, and continued access beyond the term may carry extra charges [30]. Repair or replacement of a device may delete data stored on it [30]. **Verified.**
- **Status:** active (store page and academic-discount form live on 2026-10-10). EmbraceMini and four extra EmbracePlus sensor modes joined the academic plan in September 2026 [31]. No deprecation is announced for EmbracePlus, EmbraceMini or the platform.

### What this means in practice

- At **~$1,750 per device for three years including cloud and support**, an EmbracePlus is roughly 4× an Oura Ring 5 with membership (~$470/yr) and roughly 5× a Garmin Vivosmart. That is expensive per unit, but the platform explicitly supports **running multiple participants sequentially on one device**, so in a study with, say, 2-week wear periods, a single $1,750 device can serve dozens of participants across three years. On a per-participant basis Empatica can be cheaper than a consumer-device study, provided the design is sequential rather than concurrent.

- For concurrent designs it is unambiguously the second-most expensive option here, after Ametris.

## Research Evidence and Validation

- Empatica describes its PR and PRV measurements as clinically validated and its digital biomarkers as validated; the FDA clearances lend these claims more weight than the marketing language of consumer vendors.
- The **E4 predecessor has a very large peer-reviewed footprint**, particularly in EDA/stress, affective computing, epilepsy/seizure detection, and autonomic research. Empatica's origins are in the seizure-detection domain (the Embrace line), which remains its deepest evidence base.
- **Empatica was not included in either the 2024 *Sensors* or 2025 Schyvens PSG sleep-staging comparisons.** Its sleep-detection validity relative to consumer devices is therefore not established by those benchmarks, though its FDA clearance covering "movement during sleep" biomarkers suggests a regulatory validation package exists.
- **EDA validation caveat that applies to the whole modality, not just Empatica:** wrist EDA is noisier and less well-standardised than palmar/finger EDA, is highly sensitive to motion artefact and ambient temperature, and produces substantial unusable data in free-living conditions. Studies should budget for aggressive artefact rejection and should not assume free-living wrist EDA behaves like laboratory EDA. **Quantified 2026-10-09:** against finger/palmar or laboratory references, E4 wrist EDA agrees poorly. Menghini et al. 2019 (*Psychophysiology* 56(11):e13441, N=40): wrist skin conductance "showed neither correlation nor visual resemblance with finger SC signal". Milstein and Gordon 2020 (*Front Behav Neurosci* 14:148, N=30): "The E4 failed to produce reliable EDA data". Hu et al. 2024 (*Behav Res Methods* 56(7), N=67): ICC 0.09 for skin conductance level and 0.38 for response count vs MindWare, with valid EDA about 41 to 43% of the time. No EmbracePlus validation against a palmar reference was located; Brandebusemeyer et al. 2026 (*Sensors* 26(14):4376) compared it only exploratorily with the E4. **Corroborated** (abstracts; Milstein PDF in `../literature/empatica/`).

## Strengths

- **Raw wrist EDA with an FDA-cleared EDA parameter and a self-serve academic plan**, still the most accessible EDA route in this module for stress, arousal, and seizure research (Samsung Galaxy Watch8 now also exposes raw EDA at 1 Hz through its partner-gated SDK; corrected 2026-10-10).
- **FDA-cleared platform** with cleared digital biomarkers, a regulatory posture no consumer platform matches.
- **Raw data access as a standard, documented feature** (Avro raw signal and CSV biomarkers through S3 keys), not a gated partnership.
- **Published academic pricing**, genuinely rare and enormously helpful for grant writing.
- Real study-management console with **live wear-time monitoring**.
- **Device reuse across participants** dramatically improves cost efficiency in staggered designs.
- Actigraphy counts provide a bridge to the established physical activity literature.
- Purpose-built for research; no consumer-product compromises.
- Deep evidence base in epilepsy, stress, and affective research via the E4 lineage.

## Limitations

- **No real-time streaming**, rules out JITAI and closed-loop designs.
- **One fixed sensor mode per academic account.** The mode cannot be changed after the account is created, and PPG and EDA run only in two of the five modes. (Sampling rates, listed as unpublished before 2026-10-11, are now documented per mode.)
- Biomarker count stated inconsistently across Empatica's own pages; academic-tier contents unclear.
- Cost per simultaneous participant is an order of magnitude above consumer devices.
- Short battery in the cardiac mode. Pulse Rate Pro lasts about 2 days per charge; only the actigraphy modes reach 7 to 14 days.
- The E4's real-time BLE streaming SDK was sunset on 14 February 2025, with no replacement in any research plan.
- Raw signal comes only as Avro files, which needs conversion tooling.
- No survey/EMA capability.
- No self-hosting; vendor cloud only.
- Not included in the major comparative sleep validations.
- Wrist EDA is intrinsically noisy in free-living conditions.
- Little participant-facing value, so adherence depends entirely on study contact.
- E4-to-EmbracePlus signal comparability is not established, complicating replication of the older literature.

## Best-Fit Use Cases

- **Stress, arousal, emotion, and autonomic research** requiring EDA.
- **Epilepsy and seizure detection/monitoring**, the platform's founding domain.
- Studies needing **raw multimodal physiological signal** (EDA + PPG + ACC + temperature) from a single validated device.
- **Regulated or clinical studies** where an FDA-cleared platform materially eases the regulatory pathway.
- **Staggered-enrolment designs** where devices rotate between participants, the cost model rewards this strongly.
- Multi-site clinical studies needing centralised participant management and wear-time monitoring (Enterprise plan; the academic plan allows 1 site).
- Studies that need to bridge to the ActiGraph activity-count literature while also capturing autonomic signals.

## Poor-Fit Use Cases

- Large simultaneous cohorts on a consumer-scale budget.
- Real-time or closed-loop intervention designs.
- Studies where participant engagement with the device is part of the intervention.
- Sleep staging as a primary endpoint (unvalidated in the major comparisons).
- Location or GPS-based research.
- Studies needing integrated surveys/EMA without a separate platform.

## Open Questions

- *(Directed to Empatica: https://www.empatica.com/ , support at https://support.empatica.com/)*

- ~~What are the exact per-sensor sampling rates for EmbracePlus in each sensor mode?~~ Resolved 2026-10-11; all rates are published per mode (see Sensors and Data Streams).
- **Exactly which raw signals and which biomarkers are included in the Academic & Basic Research plan** versus Enterprise? Is EDA-derived biomarker output in the standard tier?
- ~~Reconcile the "18 biomarkers" / "over 11 biomarkers" / "over 100 research-grade biomarkers" discrepancy.~~ Partly resolved 2026-10-09: the academic pages now show one 17-row table and the clinical-trial pages say "300+ digital measures". Still to confirm with Empatica: can an Academic plan buyer access any measure outside that table?
- ~~What is EmbracePlus battery life?~~ Resolved 2026-10-11; 2+ to 14+ days by mode. Still open: does an Enterprise-only mode back the "up to 28 days" claim?
- ~~Is the E4's BLE streaming SDK available in any form?~~ Resolved 2026-10-11; sunset 14 February 2025. Still open: is the remote-patient-monitoring platform SDK still offered, and to whom?
- ~~Is there a REST API?~~ Resolved 2026-10-11; a Cloud API exists for sponsors and CROs, documented to clients only. Its fees and rate limits are not public.
- Do Enterprise clients get EmbraceMini magnetometer data?
- ~~Exact scope of each FDA clearance.~~ Resolved 2026-10-10; see Privacy, Security, and Compliance.
- BAA, and the DPA's content (SOC 2 is confirmed absent from Empatica's published certifications; ISO 27001 certificate, ISO 13485, a DPA, US-Virginia hosting and 10-year retention are documented). Ask compliance@empatica.com.
- Signal comparability between E4 and EmbracePlus for replication studies.
- Volume/multi-device pricing and whether device-only (no cloud) purchase is possible. (Subscription-only purchase for outside devices is not possible.)
- ~~Data retention after the 3- or 5-year access window expires.~~ Resolved 2026-10-11; yearly extensions are sold, data stays retrievable for 60 days after termination, and later access may carry extra charges.
- Have the three PKG 510(k)s been transferred from GKC Manufacturing to Empatica?

## Vendor Fact Record

<!-- facts:begin -->
*Generated from the fact record by `tools/facts/generate.py`. Edit the record, not this block.*

**Research access**

| Fact | Value |
|---|---|
| Formal research or academic program (name, what it offers) | Academic & Basic Research plan of the Empatica Health Monitoring Platform: EmbracePlus or EmbraceMini bundled with 3 or 5 years of Care Lab App, Care Lab Portal and Empatica Cloud data access, sold self-serve. A separate Enterprise plan serves large clinical trials with dedicated services [V, 2026-10-10] |
| Who can join the research program | Academic Subscriptions are limited to educational institutions and qualified non-profit research organizations, used by their own staff or students for non-commercial teaching and research. The 25% academic discount code needs a university institutional email. The platform as a whole is sold to not-for-profit and for-profit research institutions; Enterprise qualification is decided with sales [V, 2026-10-10] |
| How to apply, and any approval or review step | **Academic & Basic Research plan:** No application review. Buy through the online store (recommended for 30 devices or fewer) or through sales; the subscription activates on shipment and the Care Lab Portal account is self-registered. The academic discount code is requested by form; Pay Later orders wait on purchase-order verification [V, 2026-10-10]<br>**Enterprise plan:** Through the sales team, which decides whether a study qualifies; studies needing more devices are steered to a bespoke solution [V, 2026-10-10] |
| Whether the program is active, paused, renamed or closed | Active. EmbraceMini and four extra EmbracePlus sensor modes were added to the Academic & Basic Research plan in September 2026. The earlier E4 research wristband and its software were sunset on 14 February 2025 [V, 2026-10-10] |
| Whether the general developer or API program is open to new applicants | **Academic & Basic Research plan:** No developer program and no SDK for academic research. Data access is by file download from the Care Lab Portal and the S3 bucket [V, 2026-10-10]<br>**Enterprise, clinical trial sponsors and remote patient monitoring:** No open developer program. A Cloud API, with developer documentation given to clients, is sold through sales to clinical trial sponsors and CROs. A remote-patient-monitoring page still describes a plug-and-play SDK for building a patient app, with no public documentation or sign-up [C, 2026-10-10] |
| Participant or user limits before approval or by tier | **Academic & Basic Research plan:** One Care Lab Portal account with 1 study, 1 site, 1 study manager and up to 1000 participants. The sensor mode is fixed per account, so a protocol needing two modes needs two accounts [V, 2026-10-10]<br>**Enterprise plan:** Minimum order of 100 devices; no published participant cap [V, 2026-10-10] |
| How academic access differs from commercial or consumer access | Academic & Basic Research: self-serve, 25% discount, 1 study and 1 site, no dedicated account manager, no SDK, non-commercial use only. Until 16 September 2026 it offered EmbracePlus in one mode only (now Pulse Rate Pro). Enterprise: large clinical trials, 100-device minimum, multiple studies and sites, IRB support, audit trails, Cloud API, quoted pricing, and third-party algorithms such as the McRoberts set [V, 2026-10-10] |

**Pricing**

| Fact | Value |
|---|---|
| Device or hardware list price | **Academic & Basic Research plan:** EmbracePlus USD 1,166.40 and EmbraceMini USD 641.52 per device line on the store, before the academic discount, sold only together with a 3- or 5-year platform subscription [V, 2026-10-10]<br>**EpiMonitor (consumer epilepsy monitoring, not a research plan):** EmbracePlus for EpiMonitor USD 399 / EUR 399 per unit [V, 2026-10-10] |
| Consumer subscription or membership price | **Academic & Basic Research plan:** The first 3 or 5 years of platform subscription come bundled with the device (3-year EmbracePlus subscription USD 1,166.40 list). Extensions per device per additional year from USD 388.80 / EUR 359.64 (EmbracePlus) and USD 291.60 / EUR 269.73 (EmbraceMini) [V, 2026-10-10]<br>**EpiMonitor (consumer epilepsy monitoring, not a research plan):** Monthly plans from USD 17.40 (Basic, 1 caregiver) to USD 52.90 (Plus, 10 caregivers) [V, 2026-10-10] |
| Research or academic pricing or discount | 25% academic discount, by code. Discounted bundles: EmbracePlus 3-year USD 1,749.60 (list 2,332.80), 5-year USD 2,187 (list 2,916, includes a further 10% off data access); EmbraceMini 3-year USD 1,137.24 (list 1,516.32), 5-year USD 1,465.29 (list 1,953.72). Volume discounts from 5 devices [V, 2026-10-10] |
| Fees for API, SDK, platform or data access | **Academic & Basic Research plan:** No separate data-access fee; Empatica Cloud, S3 data access and the Care Lab Portal are part of the per-device subscription bundled with the device [V, 2026-10-10]<br>**Enterprise plan and Cloud API:** Not public [2026-10-10] |
| Minimum order, term or commitment | Academic: each device must be bought with its platform subscription, a 3- or 5-year bundle, extendable one year at a time; subscriptions cannot be bought for devices obtained elsewhere. Enterprise: minimum order of 100 devices [V, 2026-10-10] |
| Whether pricing requires contacting sales | Academic pricing is public and self-serve, with an optional 30-day quote; studies over 30 devices are steered to sales. Enterprise and clinical trial pricing requires contacting Empatica [V, 2026-10-10] |

**Data access and terms**

| Fact | Value |
|---|---|
| Raw signals available to researchers, and by which route | **EmbracePlus:** Accelerometer, gyroscope (gyroscope modes only), blood volume pulse (PPG), EDA, skin temperature, systolic peaks (IBI), steps and user tags, delivered as Avro files in the Empatica S3 bucket. Which streams are recorded depends on the sensor mode (PPG and EDA only in Pulse Rate Pro and Actigraphy Pro) [V, 2026-10-10]<br>**EmbraceMini:** Accelerometer, gyroscope (gyroscope modes only), ambient light, steps and user tags. No PPG, EDA or temperature. No magnetometer stream is offered to researchers [V, 2026-10-10] |
| Derived or processed metrics available to researchers | Academic plan digital biomarkers: accelerometer magnitude SD, acticounts, actigraphy counts, activity classification, activity counts, activity intensity, ambient light (EmbraceMini), body position, EDA skin conductance level, METs, pulse rate, pulse rate variability (RMSSD), respiratory rate, skin temperature, sleep detection, steps and wearing detection. Pulse, respiratory and EDA measures are EmbracePlus only and Pulse Rate Pro only; Gyroscope 100 computes no activity biomarkers. Enterprise markets 300+ measures, 6 FDA-cleared, plus SpO2 [V, 2026-10-10] |
| Documented sampling rates or temporal resolution | Fixed by sensor mode (Pulse Rate Pro / Actigraphy Pro / Actigraphy Optimized / Gyroscope Max / Gyroscope 100): accelerometer 64 / 64 / 32 / 64 / 100 Hz, all +/-16 g; gyroscope off / off / off / 64 / 100 Hz; PPG 64 Hz with 5 LEDs (Pulse Rate Pro) or 4 Hz infrared (Actigraphy Pro), else off; EDA 4 Hz in the first two modes, else off; skin temperature 1 Hz (EmbracePlus); ambient light 1 Hz (EmbraceMini). Pulse Rate Pro is EmbracePlus only. Uploads in 30-minute batches; Actigraphy Optimized syncs once a day [V, 2026-10-10] |
| How far back data can be retrieved | Data stays downloadable for the subscription term (3 or 5 years per device, extendable yearly) and for 60 days after termination; continued access beyond the term may carry extra charges [V, 2026-10-10] |
| Export, API, SDK or file routes | Academic: Care Lab Portal Download Hub for digital biomarkers (CSV), and Data Access Keys (up to two active sets) to the AWS S3 bucket, read with Cyberduck, the AWS CLI or AWS SDKs. Raw signal is Avro only, in files of up to about 30 minutes with UTC timestamps; biomarkers are CSV. No live streaming and no SDK. Enterprise: Cloud API to the sponsor's systems, data still in S3 as Avro and CSV [V, 2026-10-10] |
| API rate limits | Not public [2026-10-10] |
| Terms on retaining, storing or deleting data | Participant data is kept during the services plus 10 years after the contract ends; customers can retrieve data for 60 days after termination and must stop using the platform when the subscription term expires. Device repair or replacement may delete data on the device [V, 2026-10-10] |
| Terms on using data to train AI or ML models | The terms let Empatica use customer data to create digital biomarkers and anonymized data sets for its own business purposes, owned by Empatica. No clause names AI or machine-learning training [C, 2026-10-10] |
| Announced shutdowns, deprecations or migrations, with dates | E4 wristband retired and its software suite (E4 connect, manager, realtime app, streaming server, SDK) sunset on 14 February 2025; E4 hardware support ended 1 August 2024. Embrace2 no longer sold, subscriptions continue. Studies created before 16 September 2026 run the Pulse Rate Pro sensor mode by default. No deprecation announced for EmbracePlus, EmbraceMini or the platform [V, 2026-10-10] |

**Compliance and regulatory**

| Fact | Value |
|---|---|
| Whether a HIPAA Business Associate Agreement is offered | Not public [2026-10-10] |
| Whether a data processing agreement is offered | Yes. An Empatica Health Monitoring Platform Data Processing Agreement is incorporated into the terms of service, listed on the legal page and included in the academic vendor pack (with HECVAT and an IT risk assessment) [C, 2026-10-10] |
| Published HIPAA statement | Empatica says the platform is HIPAA compliant, that data is stored and transmitted in compliance with HIPAA, and that participant data is held on HIPAA-compliant cloud infrastructure [C, 2026-10-10] |
| Published GDPR statement | Empatica says the platform is GDPR compliant and that data is stored and transmitted in compliance with GDPR; Empatica Srl (Milan) has appointed a Data Protection Officer [C, 2026-10-10] |
| ISO/IEC 27001 status and evidence | ISO/IEC 27001:2022 certified by TÜV Rheinland Cert GmbH, registration no. 01 153 2117571, holder Empatica Srl (Milan, with sites per annex), valid 2025-10-31 to 2028-10-30, first certified 2023. Scope covers design and manufacture of the wearables and of the monitoring software and platforms [V, 2026-10-10] |
| SOC 2 status and evidence | Not public [2026-10-10] |
| FDA clearances, from the FDA database | **Empatica Health Monitoring Platform and EmbracePlus:** 510(k) K221282 (2022-11-20, product code DQA: skin temperature, EDA, SpO2 at rest, sleep movement), K230457 (2023-10-30, MWI) and K242737 (2025-06-06, MWI), the last two naming EmbracePlus, Empatica Care and Care Portal. K242737 is the same device as K230457 plus an authorized Predetermined Change Control Plan (PCCP) for a subcomponent of the SpO2 algorithm [V, 2026-10-10]<br>**EmbraceMini:** 510(k) K252981, decision 2025-12-22, product code LEL (movement and sleep-movement monitoring) [V, 2026-10-10]<br>**Parkinson's Disease Monitoring:** 510(k) K260374, decision 2026-08-14, product code GYD, covering EmbracePlus, EmbraceMini, Empatica Care, PKG Monitor and Care Portal [V, 2026-10-10]<br>**Epilepsy (Embrace, EpiMonitor):** Product code POS: Embrace K172935 (2018-01-26) and K181861 (2018-12-20); EpiMonitor K232915 (2024-02-15) and K250515 (2025-06-19) [V, 2026-10-10]<br>**PKG System (acquired with PKG Health, October 2025; 510(k) holder GKC Manufacturing Pty, Ltd.):** Product code GYD: Personal Kinetigraph (PKG) System K140086 (2014-08-22) and K161717 (2016-09-20); PKG System Gen 2 Plus K211887 (2022-03-11). Holder of record is GKC Manufacturing, not Empatica [V, 2026-10-10] |
| Where data is stored, and residency options | Research participant data is stored on AWS in Virginia, US, in an Amazon S3 bucket; no regional or EU residency option is published [C, 2026-10-10] |

<!-- facts:end -->

## Key Links

- Official site: https://www.empatica.com/
- Research studies platform: https://www.empatica.com/en-eu/platform/research-studies/
- Clinical trials platform: https://www.empatica.com/en-eu/platform/clinical-trials/
- Empatica Care: https://www.empatica.com/care/
- **Academic & Basic Research store/pricing:** https://www.empatica.com/store/platform-professional/
- Academic discount application: https://lp.empatica.com/academic-discount-professional-plan
- Legal and certifications: https://www.empatica.com/legal/
- Participant privacy policy: https://www.empatica.com/privacy-participant/
- Plan explanation: https://support.empatica.com/hc/en-us/articles/17721117772317-Understanding-your-Empatica-Health-Monitoring-Platform-Plan
- FDA clearance (platform): https://www.empatica.com/blog/the-empatica-health-monitoring-platform-receives-fda-clearance
- FDA clearance (cardiac digital biomarkers): https://www.empatica.com/blog/empatica-receives-new-fda-clearance-for-cardiac-digital-biomarkers/
- Support: https://support.empatica.com/
- Academic help centre: https://academic-support.empatica.com/
- Cloud API (Enterprise): https://www.empatica.com/cloud-api
- Terms of service (purchase agreement): https://www.empatica.com/purchase-agreement/

## Sources

1. Empatica, Health Monitoring Platform for Research Studies. https://www.empatica.com/en-eu/platform/research-studies/ (accessed 2026-08-21). **Primary.** Establishes the four sensors (optical PPG with clinically validated PR/PRV, ventral EDA, accelerometer, digital temperature), "optimized sampling rates" language, the 18-biomarker list, CSV raw download via Care Portal, cloud storage with historical timestamped retrieval, absence of real-time streaming, and the Care Portal study/site/participant management and live wear-time tracking features.
2. Empatica store, Academic & Basic Research plan. https://www.empatica.com/store/platform-professional/ (accessed 2026-08-21). **Primary.** Establishes the 3-year bundle at $1,749.60 (from $2,332.80), the 5-year bundle at $2,187 (from $2,916), extra charger $42.90, band loops $21.90, package contents, self-serve download, S3 data access keys, and the "over 11 digital biomarkers" figure.
3. Empatica Support, Understanding your Empatica Health Monitoring Platform Plan. https://support.empatica.com/hc/en-us/articles/17721117772317-Understanding-your-Empatica-Health-Monitoring-Platform-Plan (accessed 2026-08-21). Establishes the Care app (Enterprise) vs Care Lab app (Academic & Basic Research) split and the standard-vs-complete biomarker suite distinction.
4. Empatica, "The Empatica Health Monitoring Platform receives FDA clearance." https://www.empatica.com/blog/the-empatica-health-monitoring-platform-receives-fda-clearance (accessed 2026-08-21). Establishes the November 2022 clearance covering EDA, SpO2, skin temperature, and movement-during-sleep digital biomarkers.
5. Empatica, "Empatica Receives New FDA Clearance for Cardiac Digital Biomarkers." https://www.empatica.com/blog/empatica-receives-new-fda-clearance-for-cardiac-digital-biomarkers/ ; PR Newswire, https://www.prnewswire.com/news-releases/empaticas-platform-receives-new-fda-clearance-for-cardiac-digital-biomarkers-301975974.html (accessed 2026-08-21).
6. Empatica Care. https://www.empatica.com/care/ (accessed 2026-08-21). Source of the "over 100 research-grade biomarkers" figure, conflicts with (1) and (2).
8. Empatica, Health Monitoring Platform for Research Studies (current URL). https://www.empatica.com/platform/research-studies/ (accessed 2026-10-09). **Primary.** Supersedes the count in (1): no number stated, a 17-row digital-biomarker table split by EmbracePlus and EmbraceMini, EmbraceMini specification, sensor modes, Academic bundle prices unchanged from (2), 1 study, 1 site and 1,000 participants per Academic account, no SDK for academic research.
9. Empatica store, Academic plan, re-read. https://www.empatica.com/store/platform-professional/ (accessed 2026-10-09). **Primary.** "A selection of digital biomarkers" with the same table; the "over 11" figure in (2) no longer appears.
10. Empatica homepage and clinical-trials page. https://www.empatica.com/ , https://www.empatica.com/platform/clinical-trials/ (accessed 2026-10-09). **Primary, vendor marketing.** "300+ digital measures", six with direct FDA clearance, the rest described as research-grade. Replaces the "over 100" figure attributed to (6), which the Care page no longer shows.
7. Wikipedia, Empatica. https://en.wikipedia.org/wiki/Empatica (accessed 2026-08-21). Background on the E4 lineage and seizure-detection origins; **secondary, low weight**.
11. Empatica store, Academic & Basic Research plan, re-read. https://www.empatica.com/store/platform-professional/ (accessed 2026-10-10). **Primary.** EmbracePlus and EmbraceMini device, subscription and bundle prices; "Access to all EmbracePlus and EmbraceMini sensor raw data".
12. Empatica, Apply for an Academic Discount. https://lp.empatica.com/academic-discount-professional-plan (accessed 2026-10-10). **Primary.** Eligibility and institutional-email application.
13. Empatica, llms.txt. https://www.empatica.com/llms.txt (accessed 2026-10-10). "5-year Platform Subscription: $1,749.60" (subscription only).
14. Empatica, "Empatica Actigraphy" blog post. https://empatica.com/blog/empatica-actigraphy-the-new-standard-to-measure-sleep-and-physical-activity (accessed 2026-10-10). **Primary, vendor.** Actigraphy Pro 64 Hz, Actigraphy Optimized 32 Hz and 14 days battery; Enterprise note.
15. Empatica, Health Monitoring Platform for Research Studies, re-read. https://www.empatica.com/platform/research-studies/ (accessed 2026-10-10). **Primary.** Five sensor modes, gyroscope in selected modes, 100 Hz Gyroscope 100 mode, no real-time streaming, no SDK for academic research.
16. Empatica legal page. https://www.empatica.com/legal/ (accessed 2026-10-10). **Primary, vendor.** ISO/IEC 27001:2022, ISO 13485:2016, MDSAP, CE, Data Processing Agreement.
17. Empatica participant privacy policy. https://www.empatica.com/privacy-participant/ (accessed 2026-10-10). **Primary.** HIPAA-compliant US-Virginia hosting; service period plus 10 years retention.
18. openFDA 510(k) records for Empatica. https://api.fda.gov/device/510k.json?search=applicant:empatica (accessed 2026-10-10), with indications for use read in https://www.accessdata.fda.gov/cdrh_docs/pdf22/K221282.pdf , https://www.accessdata.fda.gov/cdrh_docs/pdf24/K242737.pdf , https://www.accessdata.fda.gov/cdrh_docs/pdf26/K260374.pdf , https://www.accessdata.fda.gov/cdrh_docs/pdf25/K252981.pdf and https://www.accessdata.fda.gov/cdrh_docs/pdf25/K250515.pdf . **Primary.**
19. Samsung Health Sensor SDK, data specifications. https://developer.samsung.com/health/sensor/guide/data-specifications.html (accessed 2026-10-10). **Primary.** `EDA_CONTINUOUS`, raw, 1 Hz, Galaxy Watch8 and later.
20. Empatica academic help centre, "What is a Sensor Mode?" https://academic-support.empatica.com/hc/en-us/articles/38901007393053-What-is-a-Sensor-Mode (accessed 2026-10-10, vendor fact record). **Primary.** Per-mode rates for every sensor, battery and memory by mode, Actigraphy Optimized daily sync, mode fixed per account, Pulse Rate Pro default for studies created before 16 September 2026.
21. Empatica academic help centre, "Available Features." https://academic-support.empatica.com/hc/en-us/articles/36980797675549-Available-Features (accessed 2026-10-10). **Primary.** Academic and Enterprise plans, Enterprise MOQ of 100 devices, renewal prices, subscriptions only with Empatica devices, "Systolic Peaks (IBI)", academic biomarker list.
22. Empatica academic help centre, "Raw Data in the Empatica Cloud." https://academic-support.empatica.com/hc/en-us/articles/36981046788765-Raw-Data-in-the-Empatica-Cloud (accessed 2026-10-10). **Primary.** Avro-only raw data, stream list, UTC timestamps.
23. Empatica academic help centre, "Accessing Data on the S3 Bucket." https://academic-support.empatica.com/hc/en-us/articles/36981086545181-Accessing-Data-on-the-S3-Bucket (accessed 2026-10-10). **Primary.** S3 access tools; AWS storage.
24. Empatica academic help centre, "Generating and Revoking Data Access Keys." https://academic-support.empatica.com/hc/en-us/articles/36981014631837-Generating-and-Revoking-Data-Access-Keys (accessed 2026-10-10). **Primary.** Up to two active key sets.
25. Empatica academic help centre, "How the Empatica Health Monitoring Platform works." https://academic-support.empatica.com/hc/en-us/articles/36980824207261-How-the-Empatica-Health-Monitoring-Platform-works (accessed 2026-10-10). **Primary.** 30-minute upload batches; Data Access Keys for raw and biomarker data.
26. Empatica, Cloud API. https://www.empatica.com/cloud-api (accessed 2026-10-10). **Primary, vendor.** Cloud API for sponsors and CROs, client-only documentation, Avro and CSV in S3, "up to 28 days of battery life".
27. Empatica, Remote Patient Monitoring. https://www.empatica.com/platform/remote-patient-monitoring/ (accessed 2026-10-10). **Primary, vendor.** Platform SDK for patient apps, outside the research plans.
28. Empatica, E4 sunset. https://www.empatica.com/research/e4-sunset/ (accessed 2026-10-10). **Primary.** E4 and its software suite, including the SDK, sunset 14 February 2025.
29. University of Twente BMS Lab, notice on the Empatica E4. https://www.utwente.nl/en/bmslab/about-us-contact/news-and-events/news/2024/8/1702215/important-information-about-the-empatica-e4-wristband (accessed 2026-10-10). **Secondary.** E4 hardware support ended 1 August 2024.
30. Empatica, Terms of Service (purchase agreement), version 1.0, effective 1 September 2022. https://www.empatica.com/purchase-agreement/ (accessed 2026-10-10). **Primary.** Academic eligibility and non-commercial limits, DPA incorporation, 60-day retrieval after termination, charges for access beyond the term, data deletion on repair, use of data for anonymized data sets.
31. Empatica, "EmbraceMini is now available for the Academic and Basic Research plan." https://www.empatica.com/blog/embracemini-is-now-available-for-academic-and-basic-research-plan/ (accessed 2026-10-10). **Primary, vendor.** EmbraceMini and four EmbracePlus modes added; academic plan previously Pulse Rate Pro only; discount covers EmbraceMini; teams over 30 devices to contact Empatica.
32. Empatica, McRoberts partnership. https://www.empatica.com/blog/empatica-and-mcroberts-partnership-achieves-20-endpoints-and-opens-platform-to-external-algorithm-developers/ (accessed 2026-10-10). **Primary, vendor.** McRoberts algorithms for Enterprise users.
33. Empatica ISO/IEC 27001:2022 certificate (TÜV Rheinland). https://www.empatica.com/go/empatica-iso-iec (accessed 2026-10-10). **Certificate.** Registration 01 153 2117571, valid 2025-10-31 to 2028-10-30.
34. Empatica, "Empatica receives landmark FDA PCCP authorization for pulse oximetry." https://www.empatica.com/blog/empatica-receives-landmark-fda-pccp-authorization-for-pulse-oximetry/ (accessed 2026-10-10). **Primary, vendor.** SpO2 algorithm PCCP (K242737).
35. openFDA 510(k) records K140086, K161717 and K211887 (holder GKC Manufacturing Pty, Ltd.), https://api.fda.gov/device/510k.json?search=device_name:PKG ; Empatica, PKG Health acquisition, https://www.empatica.com/blog/empatica-acquires-pkg-health-to-transform-parkinson-s-disease-monitoring/ ; Empatica homepage, "12 FDA clearances", https://www.empatica.com/ (accessed 2026-10-10). **Primary.**
36. Empatica, academic vendor documentation pack. https://lp.empatica.com/vendor-pack (accessed 2026-10-10). Contents list (HECVAT, ISO and CE certificates, DPA, IT risk assessment); pack itself form-gated.
37. Sensors 2024, LOTUS paper. https://pmc.ncbi.nlm.nih.gov/articles/PMC11644628/ (accessed 2026-10-10). **Paper.** Avro-only raw signal, Empatica's Avro-to-CSV script, community readers.
38. Empatica academic help centre, "Monitoring Participant Digital Biomarkers." https://academic-support.empatica.com/hc/en-us/articles/36980846789277-Monitoring-Participant-Digital-Biomarkers (accessed 2026-10-10). **Primary.** SpO2 marked Enterprise.
39. Empatica, Embrace2. https://www.empatica.com/embrace2/ (accessed 2026-10-10). **Primary.** No longer sold; subscriptions continue.
