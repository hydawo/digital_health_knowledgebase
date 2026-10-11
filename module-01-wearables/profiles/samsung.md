# Samsung (Galaxy Watch / Galaxy Ring / Samsung Health SDK Suite)

## Quick Facts

| Field | Details |
|---|---|
| Organization | Samsung Electronics |
| Category | Consumer wearable ecosystem with an unusually research-oriented SDK suite |
| Current status | Active |
| Platforms/devices | Galaxy Watch4 and later (Wear OS powered by Samsung), Galaxy Ring, Android phones (the Data SDK also runs on non-Samsung Android phones with Samsung Health 6.30.2 or later [15]); **Android only** |
| Open source | Partly, **Samsung Health Research Stack is open source** (GitHub: S-HealthStack), but **no repository has been pushed to since 24 October 2024** (Verified 2026-10-10); the SDKs themselves are not open source |
| Hosting/deployment | On-device SDK access; Research Stack backend is self-hosted by the researcher |
| Pricing model | Device purchase (Galaxy Watch9 from $379.99 US [22]); no SDK fee is published, but the partner licence reserves Samsung's right to charge for the SDK in future [11]; access gated by partner-programme approval |
| Last verified | 2026-10-11 (vendor fact record); earlier passes 2026-08-21, 2026-10-09 and 2026-10-10 |

## Summary

- Samsung is the **most under-appreciated platform in this module for researchers who need raw signals from a consumer device.** The **Samsung Health Sensor SDK** (formerly the Samsung Privileged Health SDK; part of the Samsung Health SDK Suite, announced September 2024) exposes **raw sensor data from the BioActive sensor**: accelerometer (25 Hz), PPG green, IR and red (25 Hz continuous, 100 Hz on demand), ECG (500 Hz on demand), **EDA (1 Hz, Galaxy Watch8 and later)**, and heart rate with inter-beat intervals, directly to registered partner applications running on the watch (Samsung data specifications, Verified 2026-10-10). No other mainstream consumer smartwatch vendor offers this to any developer who completes partner registration. Apple exposes raw PPG and ECG only through SensorKit under a per-study research entitlement; Fitbit, Garmin's cloud API, Oura and WHOOP expose neither raw PPG nor raw accelerometry.

- Samsung paired this with **Samsung Health Research Stack**, an open-source end-to-end research platform (app SDK + backend + web portal) that the research team self-hosts. **As of 2026-10-10 none of the S-HealthStack repositories has been pushed to since 24 October 2024** (GitHub API; none archived), so treat Research Stack as unmaintained unless Samsung confirms otherwise. The Sensor SDK itself is current (v1.4.1, 20 August 2025; no release since [17]).

- The costs are equally clear: **Android only** (no iOS), the access model is on-device rather than a cloud cohort API, partner-programme approval is required, and the validation literature is far thinner than Fitbit's or Apple's.

## Products / Platform Architecture

- The Samsung Health SDK Suite has four components:

| Component | What it does | Research relevance |
|---|---|---|
| **Samsung Health Sensor SDK** (formerly Privileged Health SDK, renamed in v1.3.0, 22 September 2024), v1.4.1 (20 August 2025) | Raw and processed sensor data from the BioActive sensor, on-watch | The core reason to consider Samsung |
| **Data SDK**, v1.1.0 | Phone-side reads of the Samsung Health store, including Galaxy Watch and Galaxy Ring data; runs on non-Samsung Android phones with Samsung Health 6.30.2 or later [15] | Aggregation layer, added from October 2024; replaces the Samsung Health SDK for Android, deprecated 31 July 2025 and reaching end of service in 2028 [16] |
| **Accessory SDK** | Connectivity to accessories | Peripheral |
| **Samsung Health Research Stack** | Open-source app SDK + backend service + web portal for study design and data analysis | Full study platform, self-hosted; **no code pushed since October 2024** |

- Data flow for the Sensor SDK is **on-device**: a Wear OS app you build runs on the watch, subscribes to sensor trackers, and receives data locally. Notably, the SDK **operates independently and does not share data with Samsung Health**, meaning the research app's data path is separate from Samsung's consumer cloud. From a data-custody perspective this resembles the Apple/HealthKit model (researcher controls the pipeline) but with far better sensor access.

- There is **no Samsung cloud REST API** for pulling a cohort's data the way Fitbit, Garmin, Oura, and WHOOP offer. On Android, Samsung Health data can also flow into **Health Connect**, the OS-level aggregation layer, which is a separate integration path exposing processed data types only. Samsung Health syncs activity, heart rate and sleep to Health Connect, and by default a Health Connect app reads only 30 days before its first permission grant unless it requests the history permission [21].

## Sensors and Data Streams

- Every Module 1 profile uses the same table so devices can be compared row by row. Rows are the sensors named in `CLAUDE.md`. "Present" is about the hardware; "Researcher access" is about what a study can actually obtain, which is the module's central question. "Unclear" means nothing current was verified. The convention is recorded in [`../../shared/profile-table-conventions.md`](../../shared/profile-table-conventions.md).

| Sensor | Present | Researcher access to underlying signal | Resolution or sampling | Notes |
|---|---|---|---|---|
| PPG | Yes | Raw PPG green, infrared and red via the Health Sensor SDK (`PPG_CONTINUOUS`, `PPG_ON_DEMAND`) | **25 Hz continuous; 100 Hz on demand** | Rates from Samsung's data specifications, Verified 2026-10-10. No rate parameter is documented, so the rates appear fixed. |
| ECG | Yes | Raw ECG, on-demand tracker (`ECG_ON_DEMAND`) | **500 Hz**, on demand | Only one on-demand tracker type at a time; Samsung advises about 30 seconds per on-demand measurement and foreground use. |
| Accelerometer | Yes | Raw via the Health Sensor SDK (`ACCELEROMETER_CONTINUOUS`) | 25 Hz |  |
| Gyroscope | Yes | Standard Wear OS sensor APIs, not the Health Sensor SDK | Unclear |  |
| Magnetometer | Unclear | Unclear | Unclear |  |
| Temperature | Yes | Skin and ambient temperature via the SDK, continuous or on demand; not body temperature | Continuous | Galaxy Watch5 series and later (Verified 2026-10-10). |
| SpO2 | Yes | On demand via the Health Sensor SDK (`SPO2_ON_DEMAND`, Health Sensor Service v1.3.0 or higher) | On demand | Verified 2026-10-10 (data specifications). |
| GPS | LTE and GPS models | Standard Wear OS APIs | Unclear |  |
| Barometer / altimeter | Yes | Standard Wear OS APIs | Unclear |  |
| EDA | Yes, Galaxy Watch8 series and later | **Raw**, via the Health Sensor SDK (`EDA_CONTINUOUS`) | **1 Hz** continuous | "EDA measurement is available with Galaxy Watch8 series and later models" (data specifications, Verified 2026-10-10). |
| Ambient light | Yes | Standard Wear OS APIs | Unclear |  |
| Other | Heart rate with inter-beat intervals; BIA and MF-BIA body composition (on demand; MF-BIA Watch8 and later); SpO2 on demand; sweat loss | Via the SDK | HR with IBI at 1 Hz | Supported tracker types vary by watch model and software version. Neither SDK offers a raw route from Galaxy Ring [15]. |

**Verification.** PPG, ECG, accelerometer, EDA and HR rows re-verified 2026-10-10 against Samsung's Health Sensor SDK data specifications and overview pages (**Verified**). Other rows from the Module 1 passes; see the notes below.

### Notes from earlier verification passes

- Samsung Privileged Health SDK trackers (2026-08-21 reading; the SDK is now named Samsung Health Sensor SDK):

- **Continuous trackers:**
| Tracker | Detail |
|---|---|
| Accelerometer | **25 Hz** |
| Heart rate | Including **IBI (inter-beat intervals)** for HRV computation |
| PPG | Raw photoplethysmogram; a notable update added **continuous access to PPG Infrared (IR) and Red LED data for the first time** (previously green only) |
| Skin temperature | Continuous |

- **On-demand trackers:**
| Tracker | Detail |
|---|---|
| ECG | Raw electrocardiogram |
| BIA | Bioelectrical impedance analysis (body composition) |

- **Constraint:** only one on-demand tracker type can be used at a time. Supported tracker types also **vary by watch model and software version**, so a heterogeneous device fleet will have heterogeneous capability, verify per model before purchasing.

- Other sensors present on Galaxy Watch hardware (SpO2, barometer, GPS on LTE/GPS models, gyroscope, ambient light) are exposed through standard Wear OS/Android sensor APIs rather than the Health Sensor SDK; researchers should not assume the Health Sensor SDK is the only route.

- **Galaxy Ring** is Samsung's ring-form competitor to Oura. Its processed data reaches studies through the Data SDK, which names Galaxy Ring as a source; neither SDK offers a raw route from the ring (**Verified** 2026-10-10 [15]).

## Derived Metrics / Analytics

- Through the Data SDK (phone app reading Samsung Health) the listed read types are activity summary, exercise, floors, heart rate, sleep, sleep apnea, irregular heart rhythm notification, energy score, blood oxygen, skin and body temperature, blood pressure, blood glucose, body composition, nutrition, water, steps, goals and user profile [15]. Stress is not among them. Steps are aggregate only, and Samsung says Data SDK data is for fitness and wellness only. These are consumer-processed metrics comparable to competitors'.
- HRV is not exposed as a metric by either SDK; it has to be computed from the Sensor SDK's inter-beat intervals [1].

- The research value, though, is that Samsung lets you **bypass** the derived layer entirely and compute your own metrics from raw PPG/ECG/ACC, which means metric definitions are under the researcher's control and are not silently changed by a firmware update. That is a genuine methodological advantage for longitudinal work.

## Active Data Collection

- **Samsung Health Research Stack** provides the survey/task layer: it includes an app SDK for building study apps, a backend service managing collected data, and a web portal for research design and data analysis. This is the only vendor-published, open-source, end-to-end research platform among the major consumer wearable manufacturers.

- Version history: Health Stack Alpha (2022) → Health Stack 1.0 (2023) → **Samsung Health Research Stack 2.0 Beta**, rebranded to emphasise research. The September 2024 SDK Suite release promised a forthcoming 2.0 integrating the Sensor and Data SDKs; what appeared is the v2.0 Beta (release notes; last backend commit "Release v2.0-beta", 10 October 2024), and no non-beta 2.0 has followed [25]. Code is at the S-HealthStack GitHub organisation. As of 2026-10-10 none of the S-HealthStack repositories has been updated since 24 October 2024 (backend-system, app-sdk and web-portal last pushed 24 October 2024; starter-app 20 August 2024; none archived; GitHub API), so the Research Stack should be treated as unmaintained unless Samsung confirms otherwise. **Verified** (repository activity).

## Researcher and Study Management Features

- Provided by the Research Stack's web portal, study design, participant data management, and analysis support, rather than by a Samsung-operated SaaS. Because the researcher hosts the backend, they also own the study console. This is functionally similar to the Module 2 self-hosted platform model (Beiwe, RADAR-base) rather than the consumer-wearable SaaS model.

### Research program and academic data access (added 2026-10-10)

- **No separate academic programme or academic tier is published.** Academic and commercial teams go through the same Samsung Partner Program request and the same partner agreement, which names research among its licensed purposes but sets no separate academic terms [11]. Eligibility, approval criteria, turnaround and any user cap are not stated on Samsung's pages (**Verified** that they are unpublished, 2026-10-10). The licence covers all countries except sanctioned or embargoed ones.
- **Invitation route, not an open programme.** Samsung also runs direct collaborations with chosen institutions, with no published application route [18]. These include the Open Innovation Initiative (announced at SDC23, October 2023) and named studies with Stanford (sleep apnoea), Tulane and Huma (HEARTBEAT), UCSF Neuroscape (cognition, announced July 2026) and MGH (GLP-1 and body composition, May 2026) [18][20]. **Corroborated**, since several of these rest on press coverage.
- **Samsung research platform via Alcedis (announced 24 June 2026).** Samsung announced a partnership with Alcedis, a CRO that is part of Huma, in which Samsung provides its research platform (study setup, biosensor control, participant- and device-level biosensor data) and Alcedis runs study execution and participant engagement [19][20]. No sign-up, eligibility or pricing is published, and Samsung has not said whether the platform is Research Stack, the Sensor SDK or something new. No later status found (2026-10-10). Treat it as a sponsor route.
- **What a team can get:** the SDK v1.4.1 is a public download, and developer mode allows testing "only for testing or debugging your app. It is not intended for app users." To distribute a study app, the team submits a partner request; once approved, the app's package name and SHA-256 signature are registered, and unregistered apps get a policy error. Data are raw and processed on-watch signals (see the table), streamed to the team's own app, with no Samsung cloud copy of the sensor data, because no Samsung server is in the path. Rate limits are not published; with no cloud API, web-style limits do not arise, and the documented constraint is one on-demand tracker at a time. The partner agreement sets no retention period but limits the provider to processing User Data only as needed for its service, and it lets Samsung collect and use information about the partner's service and its use to improve the SDK; the partner must obtain users' consent for that [11]. The scope of that information is not defined, so the consent form should cover it. History depth is whatever the study app records from enrolment onward.
- **Research Stack**, Samsung's open-source study platform, is still on GitHub but has not been updated since 24 October 2024.
- **Is it active?** The partner programme is open. Sensor SDK v1.4.1 (20 August 2025, no release since) and Data SDK v1.1.0 are public downloads usable in developer mode; read-only Data SDK development no longer needs a partner request [15][17]. Whether partner requests are being approved, and how fast, is not published. Research Stack status is **unclear** as of 2026-10-10. Samsung has announced no retirement and states no support level, but the latest release is a v2.0 Beta and no repository has been pushed since October 2024 [12][25].

## Data Access and Export

| Route | Mechanism | Notes |
|---|---|---|
| Health Sensor SDK | On-watch app subscribes to trackers | Raw signals; partner registration required to distribute |
| Data SDK | Android phone app reads the Samsung Health store (Galaxy Watch, Galaxy Ring and other sources) | Processed metrics only, steps aggregate only; no cloud or web API, no iOS; no lookback limit documented (Corroborated). Needs its own partner approval to distribute, and approvals under the deprecated Samsung Health SDK for Android do not carry over [15][24] |
| Health Connect | Android OS aggregation layer | Processed types only (activity, heart rate, sleep synced from Samsung Health); separate integration; 30-day default history before first grant unless the history permission is requested [21] |
| Research Stack | Self-hosted backend | Researcher controls storage, export, and retention; code unmaintained since October 2024 |
| Participant self-export | Samsung Health app export | Available; format/completeness not verified |

- **No cloud cohort-pull API.** Everything routes through code you deploy to the device.

## APIs, SDKs, and Extensibility

- Samsung Health Sensor SDK, formerly Privileged Health SDK (Wear OS, Kotlin/Java), v1.4.1.
- Samsung Health Data SDK v1.1.0 (phone side). It replaces the Samsung Health SDK for Android, deprecated 31 July 2025, which stays operational at least two years and reaches end of service in 2028 (no exact date) [16].
- Samsung Health Research Stack (open source).
- Health Connect (Android platform-level).
- Wear OS / Android standard sensor APIs.

- **Access process for the Health Sensor SDK** (re-verified 2026-10-10 on Samsung's process and FAQ pages):
1. Download the SDK from Samsung's developer portal (v1.4.1 is a public download; no approval is needed to obtain it).
2. Enable developer mode for testing and debugging (testing only, not for deployment).
3. **Submit a partnership request to the Samsung Partner Program** to distribute publicly, supplying the app's package name and SHA-256 signature.
4. Apps that are unregistered or whose signature does not match receive `SDK_POLICY_ERROR`.
5. Since v1.4.0 (31 July 2025), apps targeting Android 16 need Samsung's `READ_ADDITIONAL_HEALTH_DATA` permission for the ECG, EDA, PPG, BIA and MF-BIA trackers; heart rate and SpO2 use standard Android health permissions [17].

- **Access process for the Data SDK.** The same partner request is needed before distribution, after which the package name and SHA-256 signature are registered. Writing to Samsung Health also needs an access code issued after approval. Review criteria and turnaround are not published [15].

- This signature-binding is worth flagging operationally: **the approved app build is cryptographically pinned.** Changing signing keys, or distributing a rebuilt variant, requires going back through registration.

## Deployment and Infrastructure

- Sensor access: on-device, no infrastructure needed for capture, but capture is only half the problem; the study must move data off the watch.
- Research Stack backend: self-hosted (containerised deployment via the S-HealthStack repositories). This means the research team needs cloud/DevOps capability, comparable to running a Module 2 platform, and, since the code has not been updated since October 2024, the team also carries its maintenance.
- Data residency and compliance are consequently under the researcher's control, an advantage for EU/GDPR studies and for institutions that will not permit vendor cloud storage.

## Participant Experience

- **Android only, and specifically Galaxy.** Requires a Galaxy Watch4 or later; the SDK does not support phones or emulators. This is a hard exclusion of iPhone users and of non-Samsung watch users for the watch component. The phone-side Data SDK does run on non-Samsung Android phones with Samsung Health 6.30.2 or later [15].
- **Watch4 versus Watch5 (resolved 2026-10-09, Verified).** These are two different statements, not a conflict. The SDK FAQ (now titled Samsung Health Sensor SDK) says the SDK "supports only Galaxy Watch4 and later models running Wear OS powered by Samsung". The Research Stack overview says "The Galaxy Watch 5 has been extensively tested for compatibility with this tech stack" and that "Other devices may work but have not been officially tested." So Watch4 is the SDK's minimum, and Watch5 is the only model Samsung has tested end to end with Research Stack. A study that runs Research Stack on Watch4 hardware should pilot it first. Tracker availability still varies by model and watch software version, per the FAQ.
- Battery life on Galaxy Watch is roughly 1 to 2 days in normal use; **continuous raw sensor capture will reduce this substantially** (raw PPG/ACC subscription is power-hungry; Samsung publishes no battery measurement for it). Any study using the Health Sensor SDK must pilot battery life under its actual sampling configuration, and should expect charging burden closer to Apple Watch than Garmin.
- Requires the participant to install the study app and grant permissions. For apps targeting Android 16, the ECG, EDA, PPG and BIA trackers add a prompt for Samsung's `READ_ADDITIONAL_HEALTH_DATA` permission [17].
- Galaxy Watch is a mainstream, well-accepted consumer device with good comfort and wear compliance.

## Privacy, Security, and Compliance

- The Health Sensor SDK's separation from Samsung Health means the study's sensor data does not flow into Samsung's consumer cloud, the research pipeline is the researcher's own. The partner licence still lets Samsung collect and use information about the partner's service and its use, and requires the partner to obtain users' consent for that; the scope is undefined and may be telemetry [11].
- **Data SDK and Health Connect routes read the consumer Samsung Health store**, so Samsung's consumer terms apply to that data. Samsung keeps Samsung Health data while the user is active, or as long as needed for the service [21]. Since July 2026, with separate opt-in consent, Samsung uses Samsung Health data for AI training and modelling, including human review; withdrawing consent deletes only the AI-development data [21]. The regions where that consent is shown are not published. The EU/UK notice names Samsung Electronics as controller and says data is transferred to countries including the EEA and the Republic of Korea, with no residency choice; the US notice names no location [21].
- The partner agreement bars providers from using or disclosing User Data to third parties for advertising, marketing, selling or data mining [11].
- Because the Research Stack is self-hosted, **HIPAA/GDPR analysis attaches to the researcher's infrastructure**, not to Samsung. As with Apple, there is no vendor DPA to negotiate for the study copy of the data.
- Samsung Partner Program terms: the published "Samsung Health Partner Service & SDK License Agreement" was searched on 2026-10-10 and contains no HIPAA, business-associate or data-processing-agreement language; it defines User Data and data-security breaches. **Verified** (text searched). It says User Data terms "may be outlined in a supplemental agreement", but no supplement or DPA template was found. Restrictions on publication were not found in that search, but the agreement was not read clause by clause.
- Samsung's US Samsung Health Privacy Notice (effective 29 July 2026) does not mention HIPAA, and Samsung's "HIPAA-ready" Knox marketing is about device security. No ISO 27001 or SOC 2 report covering Samsung Health or the SDKs is published (2026-10-10) [21].
- **FDA.** Galaxy Watch features in Samsung Health Monitor, not the SDKs, hold five FDA authorisations. They are ECG Monitor App K201168 (2020-08-04); ECG Monitor Application with Irregular Heart Rhythm Notification K230292 (2023-05-02); Samsung ECG App v1.3 K240909 (2024-08-02); Sleep Apnea Feature De Novo DEN230041 (2024-02-06); Sleep Apnea Feature v2.0 K261011 (2026-07-20) [23]. Samsung says data from both SDKs is for fitness and wellness only [15].

## Pricing

- No SDK or partner fee is published and both SDKs are free downloads, but the partner licence (Appendix 1 clause 4(m)) reserves Samsung's right to charge for use of the SDK in future [11]. The gate today is partner registration for distribution, not payment.
- **Agreement term.** No minimum order or spend. The Samsung Health Partner Service and SDK Licence Agreement runs for two years, then renews yearly unless either party gives 60 days' notice, and Samsung may end it without cause on 30 business days' written notice; no equivalent right for the provider was found [11]. For multi-year studies, the fee reservation and this termination right are the two terms to plan around.
- Device prices are public on samsung.com US (2026-10-10, before trade-in, possibly promotional). Galaxy Watch9 from $379.99, Galaxy Watch Ultra2 from $699.99, Galaxy Ring from $299.99 [22]. The Sensor SDK supports Galaxy Watch4 and later, so older models also work.
- Costs: Galaxy Watch hardware (mid-range consumer pricing, generally below Apple Watch), plus the engineering and hosting cost of the Wear OS app and Research Stack backend.
- No consumer subscription is required for the data. Samsung Health is free; optional iFit premium workout content is paid [22].
- No research, institutional or volume pricing is published (2026-10-10). Samsung's US Education Offer Program is a personal retail discount for verified students and educators, not research pricing. No quote is needed for devices or SDKs; the Alcedis research platform has no published price.
- Academic applicants sign the same public partner agreement as everyone else, with the term, termination and future-fee terms above [11].

## Research Evidence and Validation

- The systematic review of steps/energy expenditure/heart rate found **Apple and Samsung had the highest validity for step count**, and that Samsung measured steps accurately in laboratory settings.
- Energy expenditure: unacceptable across all brands including Samsung (MAPE >30%).
- **Sleep staging (corrected 2026-10-09):** Samsung is absent from Robbins 2024 and Schyvens 2025, but not from all PSG comparisons. Lee T et al. 2023 (*JMIR mHealth uHealth* 11:e50983, N=75, two Korean sleep centres; most authors employed by Asleep, a competing sleep-app maker) found Galaxy Watch 5 four-stage κ 0.42 (macro F1 0.58), level with Fitbit Sense 2 and ahead of Pixel Watch (0.40), Oura Ring 3 (0.35) and Apple Watch 8 (0.30). Byun et al. 2023 (*Chronobiol Int* 40(5):596, independent) found Galaxy Watch 2 underestimated total sleep time by 24.9 min in 127 OSA patients. **Corroborated.**
- **Sleep apnea and SpO2:** Alavi et al. 2026 (*J Clin Sleep Med* 22(1):150, Stanford, N=152, 147 with both PSG nights; **Samsung-funded per Crossref publisher funder metadata and the Europe PMC grant list**, read 2026-10-10; full-text disclosure not read): AUROC 0.94 for AHI ≥15. Browne et al. 2024 (*J Clin Sleep Med* 20(9):1479, Samsung research grant): Galaxy Watch 4 overnight SpO2 RMSE 2.54% vs PSG oximetry. Walzel et al. 2023 (*Sensors* 23(22):9164, independent): Galaxy Watch 5 met the ISO ≤4% Arms limit vs Masimo during induced hypoxemia. HR/HRV: Sarhaddi et al. 2022 (*PLoS One* 17(12):e0268361, independent, Gear Sport). **Corroborated.**
- **Antioxidant Index and Vascular Load: no independent or vendor peer-reviewed validation located** (PubMed searched 2026-10-09). **Unclear.**
- The much more important point for research: because raw ECG/PPG/ACC are accessible, **a study does not have to rely on Samsung's derived metrics at all.** Validation of Samsung's consumer algorithms becomes largely irrelevant if the researcher computes their own outputs from the raw signal using published, validated methods. This inverts the usual validation problem.
- Third-party research tooling exists, e.g. the CLAID framework (ETH Zurich) publishes a Galaxy Watch collector, indicating the platform is in genuine academic use.

## Strengths

- **Raw PPG (green, IR, red; 25 Hz continuous, 100 Hz on demand), raw ECG (500 Hz), raw accelerometer at 25 Hz, raw EDA at 1 Hz (Watch8 and later) and IBI on consumer hardware**, unmatched among mainstream consumer wearables.
- Researcher can define and compute their own metrics, insulating a longitudinal study from vendor algorithm drift.
- **Open-source, self-hosted, end-to-end research platform** (Research Stack) published by the manufacturer.
- Full data custody on the Sensor SDK route; no vendor cloud in the study's data path; data residency under researcher control.
- No subscription and no SDK fee today (the licence reserves the right to charge later).
- Good step-count validity.
- Galaxy Ring available for ring-form designs within the same ecosystem.

## Limitations

- **Android/Galaxy only.** Cannot support iPhone users, which is disqualifying for many representative-sample designs and for most US general-population studies.
- **No cloud cohort API**, all access requires deploying and maintaining a Wear OS app.
- High technical burden: Wear OS development plus self-hosted backend. Comparable to running a Module 2 platform.
- Battery cost of continuous raw capture is significant and must be piloted.
- Tracker availability varies by watch model and software version.
- Only one on-demand tracker (ECG or BIA) at a time.
- Partner registration required before distribution, with cryptographic app-signature pinning that complicates build management.
- Research Stack is unmaintained since October 2024 (no repository updates).
- Sleep staging has two multi-device PSG comparisons: Lee 2023 (Galaxy Watch 5, by a competing app maker) and Byun 2023 (Galaxy Watch 2, independent, 127 OSA patients; the abstract reports total sleep time and time in each sleep stage, with no epoch-by-epoch agreement reported in the abstract). Antioxidant Index and Vascular Load have no published validation (checked 2026-10-09).
- Thin comparative validation literature relative to Fitbit and Apple.
- No raw data from Galaxy Ring; only processed metrics through the Data SDK.
- Samsung may end the partner agreement without cause on 30 business days' notice, and reserves the right to start charging for the SDK.
- Data SDK and Health Connect routes read the consumer Samsung Health store, which since July 2026 can feed Samsung's AI training where the participant has opted in.

## Best-Fit Use Cases

- Studies that need **raw physiological signals** but cannot afford or justify research-grade hardware (Empatica, ActiGraph/Ametris) for every participant.
- Cardiovascular and autonomic research needing raw ECG and IBI from a device participants will actually wear all day.
- Signal-processing and algorithm-development research, building and validating new digital biomarkers on consumer hardware.
- Studies requiring full data custody and self-hosted infrastructure for institutional or regulatory reasons.
- Android-only cohorts, or studies already provisioning Android devices.
- Longitudinal studies that must protect metric definitions from vendor algorithm changes.

## Poor-Fit Use Cases

- Any study requiring iOS participants on the same device platform.
- Teams without Android/Wear OS development capacity and backend/DevOps capability.
- Studies wanting a quick, low-effort cohort data pull.
- Studies depending on Samsung's derived sleep-stage outputs as validated endpoints.
- BYOD designs in populations where Galaxy Watch penetration is low.

## Open Questions

- *(Directed to Samsung: https://developer.samsung.com/health, Samsung Partner Program request.)*

- What are the eligibility criteria and timeline of the Samsung Partner Program for **academic** applicants? Are universities routinely approved? Terms partly answered 2026-10-11: one public agreement for all applicants (see Pricing); eligibility and turnaround still not published.
- How does a study get onto the Samsung research platform offered through Alcedis, and at what cost?
- Do the Partner Program terms restrict publication, data sharing, or open deposition of raw-signal data?
- ~~What are the actual maximum sampling rates and configurability for each tracker? What is the raw PPG sampling rate?~~ Resolved 2026-10-10 (Verified): accelerometer 25 Hz, PPG 25 Hz continuous and 100 Hz on demand, ECG 500 Hz, EDA 1 Hz, HR with IBI 1 Hz; no rate parameter is documented, so the rates appear fixed.
- Measured battery life under continuous raw PPG + ACC subscription, per model.
- Which trackers are available on which specific Galaxy Watch generations and software versions?
- ~~Does the Galaxy Ring expose raw data, and through which SDK?~~ Resolved 2026-10-10 (Verified): no raw route in either SDK; processed Ring data comes through the Data SDK.
- Production-readiness of Samsung Health Research Stack 2.0. Maintenance status partly answered 2026-10-10: no repository pushed since 24 October 2024; whether Samsung still supports it needs Samsung.
- On-device buffering and offline behaviour: how much raw data can the watch hold if the phone is absent?
- Samsung's HIPAA/GDPR posture for any component that does touch Samsung infrastructure. Partly answered 2026-10-10: no BAA, DPA, HIPAA statement, ISO 27001 or SOC 2 is published; the EU/UK notice makes Samsung the controller for the consumer service.
- What "information about the Service and use of Service" Samsung collects under the partner licence.

## Vendor Fact Record

<!-- facts:begin -->
<!-- facts:end -->

## Key Links

- Samsung Health developer hub: https://developer.samsung.com/health
- Samsung Health Sensor SDK overview: https://developer.samsung.com/health/sensor/overview.html
- Health Sensor SDK FAQ: https://developer.samsung.com/health/sensor/faq.html (the old `/health/privileged/` address now shows the Sensor SDK page)
- Health Sensor SDK data specifications: https://developer.samsung.com/health/sensor/guide/data-specifications.html
- Health Sensor SDK process (download, partner request): https://developer.samsung.com/health/sensor/process.html
- Sensor SDK API reference: https://developer.samsung.com/health/sensor/api-reference/overview-summary.html
- Samsung Health Research Stack: https://developer.samsung.com/health/s-healthstack
- Research Stack GitHub organisation: https://github.com/S-HealthStack
- Research Stack backend: https://github.com/S-HealthStack/backend-system
- Research Stack release notes: https://developer.samsung.com/health/research/release-notes/v11.html
- SDK Suite announcement: https://news.samsung.com/global/samsungs-new-health-software-development-kit-suite-powers-advancements-in-healthcare-innovation
- Health Connect (Android): https://developer.android.com/health-and-fitness/health-connect

## Sources

1. Samsung Privileged Health SDK FAQ (now the Samsung Health Sensor SDK FAQ, https://developer.samsung.com/health/sensor/faq.html; the old address below redirects in content to the Sensor SDK, checked 2026-10-10). https://developer.samsung.com/health/privileged/faq.html (accessed 2026-08-21). **Primary.** Establishes continuous trackers (accelerometer 25 Hz, heart rate with IBI, PPG, skin temperature), on-demand trackers (ECG, BIA, one at a time), Galaxy Watch4+ Wear OS exclusivity, no phone/emulator support, the partner-request process with package name and SHA-256 signature, `SDK_POLICY_ERROR` behaviour, model/version-dependent tracker availability, and that the SDK does not share data with Samsung Health.
2. Samsung Health Sensor SDK overview. https://developer.samsung.com/health/sensor/overview.html (accessed 2026-08-21).
3. Samsung Mobile Press, Health SDK Suite announcement, September 2024. https://www.samsungmobilepress.com/articles/samsungs-new-health-software-development-kit-suite-powers-advancements-in-healthcare-innovation (accessed 2026-08-21). Establishes the four-component suite, raw BioActive sensor access, first-time continuous PPG IR and Red LED access, the Data SDK from October, and Research Stack 2.0 integration plans.
4. Samsung Newsroom, Samsung Health Research Stack. https://news.samsung.com/global/samsung-electronics-unveils-samsung-health-research-stack (accessed 2026-08-21). Establishes the open-source app SDK + backend + web portal architecture and the Alpha → 1.0 → 2.0 Beta timeline.
5. Samsung Health Research Stack GitHub. https://github.com/S-HealthStack (accessed 2026-08-21).
8. Samsung Health Research Stack overview. https://developer.samsung.com/health/research/overview.html (accessed 2026-10-09). **Primary.** Establishes that the Galaxy Watch 5 is the officially tested device for Research Stack and that other devices "may work but have not been officially tested"; release notes list v2.0 as the latest version. Read together with (1), re-read the same day, which still states Galaxy Watch4 and later as the SDK minimum and now titles the product Samsung Health Sensor SDK.
6. Fuller D. et al. *JMIR mHealth uHealth* 2020;8(9):e18694. https://mhealth.jmir.org/2020/9/e18694/, Samsung among highest step-count validity; energy expenditure unacceptable across brands.
7. CLAID framework Galaxy Watch collector (ETH Zurich). https://claid.ethz.ch/framework_components/Packages/data_collection/GalaxyWatchCollector/ (accessed 2026-08-21). Evidence of academic tooling.
9. Samsung Health Sensor SDK data specifications. https://developer.samsung.com/health/sensor/guide/data-specifications.html (accessed 2026-10-10). **Primary.** ACCELEROMETER_CONTINUOUS 25 Hz raw; EDA_CONTINUOUS 1 Hz raw, Galaxy Watch8 and later; HEART_RATE_CONTINUOUS with IBI 1 Hz; PPG_CONTINUOUS green, IR, red 25 Hz raw; ECG_ON_DEMAND 500 Hz; PPG_ON_DEMAND 100 Hz; MF_BIA_ON_DEMAND Watch8 and later; on-demand trackers one at a time, about 30 s.
10. Samsung Health Sensor SDK overview, process and FAQ pages. https://developer.samsung.com/health/sensor/overview.html ; https://developer.samsung.com/health/sensor/process.html ; https://developer.samsung.com/health/sensor/faq.html (accessed 2026-10-10). **Primary.** Product name; Galaxy Watch4 and later; EDA listed among data types; v1.4.1 download; developer mode for testing only; partner request with package name and SHA-256 before distribution; policy error if unregistered.
11. Samsung Health Partner Service & SDK License Agreement. https://developer.samsung.com/health/sensor/sdk-license-partner-service-agreement.html (accessed 2026-10-10). **Primary.** No HIPAA, BAA or DPA language found by text search. Two-year initial term, yearly renewal, termination by Samsung without cause on 30 business days' notice; reservation of the right to charge for the SDK and Samsung's collection of information about the service (Appendix 1 clause 4(m)); ban on advertising, marketing, selling or data mining use of User Data; research among licensed purposes.
12. GitHub API, S-HealthStack organisation repositories. https://api.github.com/orgs/S-HealthStack/repos (accessed 2026-10-10). Last pushes: backend-system, app-sdk, web-portal 24 October 2024; starter-app 20 August 2024; none archived.
13. Alavi et al. 2026, "Smartwatch-based detection of moderate-to-severe and high-risk obstructive sleep apnea", *J Clin Sleep Med* 22(1). Crossref record https://api.crossref.org/works/10.1007/s44470-026-00159-8 and Europe PMC record (PMID 42661136), read 2026-10-10. Funder Samsung (publisher-asserted); 152 enrolled, 147 completed both PSG nights; AUROC 0.94.
14. Byun et al. 2023, "Performance of the Fitbit Charge 2 and Galaxy Watch 2 compared with polysomnography in assessing patients with obstructive sleep apnoea", *Chronobiol Int* 40:596-602. https://doi.org/10.1080/07420528.2023.2191720 (Europe PMC abstract read 2026-10-10). 127 OSA patients; TST and time in each sleep stage; funded by the National Research Foundation of Korea.
15. Samsung Health Data SDK overview, process, FAQ and data-types pages. https://developer.samsung.com/health/data/overview.html ; https://developer.samsung.com/health/data/process.html ; https://developer.samsung.com/health/data/faq.html ; https://developer.samsung.com/health/data/guide/features/data-types.html ; migration guide https://developer.samsung.com/health/data/migration-guide/overview.html (accessed 2026-10-10). **Primary.** v1.1.0; read data types; steps aggregate only; Galaxy Watch and Galaxy Ring as sources; non-Samsung Android phones with Samsung Health 6.30.2 or later; partner request before distribution; access code for writing; developer mode without a partner request; fitness and wellness use only.
16. Samsung Health SDK for Android overview, https://developer.samsung.com/health/android/overview.html , and Samsung Developer newsletter, October 2025, https://developer.samsung.com/sdp/news/en/2025/10/30/dev-insight-oct-2025-move-to-samsung-health-data-sdk-as-samsung-health-sdk-for-android-deprecates-and-other-latest-news (accessed 2026-10-10). **Primary.** Deprecated 31 July 2025; operational at least two years; end of service in 2028.
17. Samsung Health Sensor SDK release notes. https://developer.samsung.com/health/sensor/release-note.html (accessed 2026-10-10). **Primary.** v1.3.0 rename (22 September 2024); v1.4.0 Android 16 permission change (31 July 2025); v1.4.1 (20 August 2025).
18. Samsung Health partnerships page, https://developer.samsung.com/health/partnerships ; Samsung Mobile Press, Open Innovation Initiative (SDC23), https://samsungmobilepress.com/articles/samsung-announces-open-innovation-initiative-with-leading-universities-and-academic-hospitals-to-build-digital-health-ecosystem ; Samsung Mobile Press, UCSF Neuroscape study, https://samsungmobilepress.com/articles/neuroscape-samsung-cognitive-study-partnership (accessed 2026-10-10). **Primary.** Institutional collaborations; no application route.
19. Samsung Newsroom, Samsung partners with Alcedis, 24 June 2026. https://news.samsung.com/global/samsung-partners-with-alcedis-to-advance-clinical-research-using-wearable-based-endpoints (accessed 2026-10-10). **Primary.** Samsung research platform (study setup, biosensor control, participant- and device-level data); Alcedis leads study execution.
20. Press coverage of the institutional studies (accessed 2026-10-10). TechRepublic on Alcedis and Huma, https://www.techrepublic.com/article/news-samsung-alcedis-galaxy-watch-clinical-trials/ ; Engadget on the MGH GLP-1 study, https://www.engadget.com/2182683/samsung-study-galaxy-watch-8-glp1-ozempic/ ; SamMobile on the Stanford sleep apnoea study, https://www.sammobile.com/news/samsung-partners-stanford-university-medicine-improve-sleep-apnea-detection-galaxy-watches/ . Secondary.
21. Samsung Health consumer terms and Health Connect (accessed 2026-10-10). US Privacy Notice, https://samsunghealth.com/privacy ; EU/UK Privacy Notice, https://samsunghealth.com/privacy?cc=GB&lc=en ; AI training consent notice (July 2026), https://samsunghealth.com/shd/gen-ai ; 9to5Google on consent withdrawal, https://9to5google.com/2026/07/15/samsung-health-ai-training-data-consent/ ; Samsung Health developer overview (Health Connect sync), https://developer.samsung.com/health/overview.html ; Android Health Connect read-data guide (30-day default), https://developer.android.com/health-and-fitness/health-connect/read-data . **Primary** except 9to5Google.
22. Samsung US store and app pages (accessed 2026-10-10). https://www.samsung.com/us/watches/galaxy-watch9/ ; https://www.samsung.com/us/watches/galaxy-watch-ultra2/ ; https://www.samsung.com/us/rings/galaxy-ring/ ; https://www.samsung.com/us/apps/samsung-health/ . **Primary.** Prices before trade-in; Samsung Health free, iFit content paid.
23. FDA device databases (accessed 2026-10-10). K201168 https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K201168 ; K230292 https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K230292 ; K240909 https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K240909 ; DEN230041 https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/denovo.cfm?id=DEN230041 ; K261011 https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K261011 . **Primary.**
24. Thryve, Samsung Health data source documentation. https://docs.thryve.health/thryve-data-sources/samsung-health (accessed 2026-10-10). Secondary. Legacy SDK approvals do not transfer to the Data SDK.
25. Samsung Health Research Stack v2.0 Beta release notes. https://developer.samsung.com/health/research/release-notes/v20.html (accessed 2026-10-10). **Primary.** Latest release is v2.0 Beta; no non-beta 2.0.
