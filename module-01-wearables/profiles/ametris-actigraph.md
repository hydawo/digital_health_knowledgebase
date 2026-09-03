# Ametris (formerly ActiGraph), CentrePoint, ActiGraph LEAP, Insight Watch

## Quick Facts

| Field | Details |
|---|---|
| Organization | **Ametris**, formerly ActiGraph; rebranded 25 June 2025; **acquired by Signant Health, announced May 2026** |
| Category | Research-grade actigraphy and clinical-trial digital endpoint platform |
| Current status | Active, but **undergoing significant corporate and product transition** |
| Platforms/devices | CentrePoint Insight Watch, ActiGraph LEAP; legacy wGT3X-BT, GT9X Link (end-of-life), GT3X+ |
| Open source | No |
| Hosting/deployment | CentrePoint cloud platform; legacy ActiLife desktop software |
| Pricing model | Not public; quote-based |
| Last verified | 2026-08-21 |

## Summary

- ActiGraph is the historical **gold standard for research-grade accelerometry**. For roughly two decades it has been the default device in physical activity, sedentary behaviour, and actigraphy-based sleep research, and its "activity counts" are the unit in which an enormous body of literature is expressed. If a study needs raw accelerometry that reviewers will accept without argument, this is the reference.

- **But the company has changed substantially and recently, and the knowledge base should treat prior assumptions as stale:**

- January 2025, acquired the **Biofourmis Connect** digital trial platform, including the Biovitals Analytics Engine and RhythmAnalytics SaMD products.
- 25 June 2025, **rebranded from ActiGraph to Ametris** (pronounced "uh-ME-tris").
- May 2026, **Signant Health announced its acquisition of Ametris**, to create an end-to-end eCOA and digital outcome measures platform.
- The **GT9X Link is in end-of-life transition** and no longer available to new customers.
- The current device line is the **CentrePoint Insight Watch** and **ActiGraph LEAP**.

- The strategic direction is unambiguous: away from selling devices and software to individual academic investigators, and toward being a **pharmaceutical clinical-trial services provider**. That shift matters for anyone planning an academic study, because the historical "buy a box of GT3X+ and run ActiLife" workflow is being deprecated, and the replacement is an enterprise platform with non-public pricing.

## Products / Platform Architecture

- **CentrePoint**, described by Ametris as a robust cloud software platform for collecting, processing, and managing real-world digital endpoint data in clinical investigations. Capabilities:
- Deploy wearables across clinical trials and health studies.
- Near real-time access to participant health metrics and adherence data.
- Automated device assignment workflows.
- Passive remote data collection via **cellular gateway or mobile app**, the cellular gateway option removes the smartphone dependency, as with Withings.
- Participant adherence monitoring with customised monthly reports.
- Multi-site coordination across **70+ countries**.
- End-to-end operational support from protocol design through regulatory engagement.

- **Devices:**
- **CentrePoint Insight Watch**, wrist-worn, extended battery life for remote monitoring.
- **ActiGraph LEAP**, accelerometer-based device, continuous movement data, extended battery.
- **Legacy:** wGT3X-BT, GT9X Link (EOL), GT3X+, the devices behind most of the published literature.

- **ActiLife**, the legacy desktop software for device initialisation, download, and analysis (activity counts, cut-points, wear-time validation, sleep scoring algorithms such as Sadeh and Cole-Kripke). Its ongoing status under Ametris/Signant is an open question.

- **Post-acquisition additions** (from Biofourmis Connect): the Biovitals Analytics Engine and RhythmAnalytics, a software-as-a-medical-device product. Ametris states the integrated Connect platform supports proprietary ActiGraph wearables alongside validated third-party sensors including an ECG patch, digital spirometer, and blood pressure cuff, meaningfully broadening the platform beyond accelerometry.

## Sensors and Data Streams

- Every Module 1 profile uses the same table so devices can be compared row by row. Rows are the sensors named in `CLAUDE.md`. "Present" is about the hardware; "Researcher access" is about what a study can actually obtain, which is the module's central question. "Unclear" means nothing current was verified. The convention is recorded in [`../../shared/profile-table-conventions.md`](../../shared/profile-table-conventions.md).

| Sensor | Present | Researcher access to underlying signal | Resolution or sampling | Notes |
|---|---|---|---|---|
| PPG | Some models | Unclear | Unclear | Legacy GT9X had an optional module; Insight Watch status not established. |
| ECG | No | Not applicable | Not applicable |  |
| Accelerometer | Yes | Raw, retained | Configurable, historically 30 to 100 Hz | The core capability. Current-device rates not established; confirm for Insight Watch and LEAP. |
| Gyroscope | Some legacy models | Unclear | Unclear | GT9X Link had an IMU; current status not established. |
| Magnetometer | Some legacy models | Unclear | Unclear | As gyroscope. |
| Temperature | Unclear | Unclear | Unclear | Not established for current devices. |
| SpO2 | No | Not applicable | Not applicable |  |
| GPS | No | Not applicable | Not applicable |  |
| Barometer / altimeter | No | Not applicable | Not applicable |  |
| EDA | No | Not applicable | Not applicable |  |
| Ambient light | Some legacy models | Unclear | Unclear |  |
| Other | Unclear | Unclear | Unclear | Not verified against current documentation. |

**Verification.** Drawn from the pages retrieved in the Module 1 passes; sampling rates for current devices were not established. See the notes below for the original wording.

### Notes from earlier verification passes

| Sensor | Detail |
|---|---|
| **Triaxial accelerometer** | The core capability. Research-grade, high sampling rate, raw data retained. |
| Gyroscope / magnetometer | Present on some legacy models (GT9X Link had an IMU); current-device status not established. |
| Heart rate (PPG) | Present on some models (legacy GT9X with optional module; Insight Watch status not established). |
| Ambient light | Present on some legacy models. |
| Temperature | Not established for current devices. |

- **Sampling rates for current devices were not established** from the pages retrieved. Historically ActiGraph devices sampled at configurable rates from 30 Hz to 100 Hz, which is the range the literature assumes. **Confirm for Insight Watch and LEAP before designing a study**, this is the single most important technical specification for a device chosen specifically for raw accelerometry.

## Derived Metrics / Analytics

- The defining value proposition, in Ametris' own words, is **"future-proof raw sensor data that can be reprocessed indefinitely as new methods emerge."** This is the key methodological argument for research-grade actigraphy over consumer wearables: the raw signal is preserved, so when the field's algorithms improve, the study's data can be re-analysed. Every consumer platform in this module delivers only the vendor's current algorithm output, which cannot be revisited.

- Established derived outputs in the ActiGraph tradition: **activity counts** (the historical unit), ENMO and MAD (raw-acceleration metrics used by modern open-source pipelines), wear-time validation, sedentary/light/moderate/vigorous intensity classification via published cut-points, step counts, and actigraphy-based sleep/wake scoring.

- An important ecosystem point: because the raw data is available, ActiGraph output is analysable with **open-source, reproducible pipelines** independent of the vendor, notably GGIR (R) and related packages. This makes the analysis chain publishable and auditable in a way that no consumer platform's black-box scores can be.

## Active Data Collection

- Not a survey/EMA platform natively. Under Signant Health, whose core business is eCOA (electronic clinical outcome assessment), integrated ePRO alongside device data is the explicit strategic direction of the acquisition. **Current availability is not established.**

## Researcher and Study Management Features

- CentrePoint is a genuine, mature clinical-trial study platform, the most operationally complete in this module alongside Empatica's Care Portal:

- Secure web portal with **near real-time participant wear compliance**, outcomes, site performance details, and overall study progress.
- Automated device assignment workflows.
- Customised monthly adherence reports.
- Multi-site, multi-country coordination (70+ countries).
- Operational support spanning protocol design through regulatory engagement.

- The regulatory-engagement support is distinctive: for a study whose endpoints must satisfy a regulator, having a vendor that has taken digital endpoints through that process before is worth a great deal.

## Data Access and Export

- **Raw sensor data** retained and reprocessable indefinitely.
- **CentrePoint API**, enables data outcomes to be integrated directly into a third-party system.
- **Web portal** access to compliance and outcome data.
- Legacy path: device → ActiLife → local files (`.gt3x` raw, plus derived `.agd`/CSV).

- API specifics, authentication, rate limits, whether raw waveform data (as opposed to processed outcomes) is retrievable via API, and export formats, are **not established** from public documentation and are a priority vendor question.

## APIs, SDKs, and Extensibility

- CentrePoint API (details not public).
- Third-party sensor support in the Connect platform (ECG patch, spirometer, BP cuff).
- The `.gt3x` raw file format has been reverse-engineered/documented by the research community, and open-source readers exist in R and Python, an important hedge against vendor lock-in.
- No device SDK.

## Deployment and Infrastructure

- Vendor cloud (CentrePoint). No self-hosting. The legacy ActiLife model was fully local, device initialised and downloaded on the researcher's own machine, with no cloud at all, which some IRBs and institutions strongly preferred. **The move to a cloud platform is a governance change, not just a convenience change**, and studies with data-locality constraints should check whether a purely local workflow remains available.

## Participant Experience

- Devices are worn at the wrist, hip, or ankle depending on protocol, **wear location flexibility is a research-grade feature** that consumer wrist wearables do not offer. Hip-worn placement remains the convention for much of the physical activity literature; wrist for sleep/24h protocols.
- **Extended battery life** suitable for remote monitoring, a design priority for both Insight Watch and LEAP. Historically ActiGraph devices ran for weeks on a charge, which is why they dominate 7-day and 14-day free-living protocols.
- **Cellular gateway option removes the smartphone requirement**, as with Withings, this unlocks populations that cannot reliably operate a phone app.
- Devices have no participant-facing display or feedback in the traditional research configuration, which is deliberate: **it prevents the measurement from changing the behaviour being measured.** For observational physical activity research this is a methodological requirement, not a limitation.
- Correspondingly, there is no participant engagement value; adherence depends on study contact and on the monitoring/reporting that CentrePoint provides.

## Privacy, Security, and Compliance

- Not verified in this session. Given the clinical-trial positioning, the 70+ country footprint, the SaMD products acquired from Biofourmis, and the Signant Health acquisition, a substantial compliance apparatus almost certainly exists (21 CFR Part 11, HIPAA, GDPR, ISO). **None of it is confirmed here**, obtain documentation directly.

## Pricing

- **Not published.** All figures below are **Reported** and come from a **competitor's** published pricing guides (Fibion, which sells alternative research accelerometry). Treat them as indicative order-of-magnitude only, and note the obvious source bias:

| Item | Reported price |
|---|---|
| GT3X+ | $325, $1,016 (varies by region/distributor/agreement) |
| GT9X Link | ~$500 (**no longer available to new customers**, EOL) |
| wGT3X-BT | $325, $1,016 |
| ActiLife software | ~$1,695 |
| CentrePoint software | ~$3,500/year |
| CentrePoint Hub | ~$600 purchase, or ~$300/year rental |

- Current-device (Insight Watch, LEAP) and CentrePoint platform pricing under Ametris/Signant is **entirely non-public**. The strategic shift toward pharmaceutical clients suggests pricing is now oriented to sponsor budgets rather than academic grants, which should be tested early in study planning rather than assumed.

## Research Evidence and Validation

- **The deepest validation base of any device in this module.** ActiGraph accelerometry underpins decades of physical activity epidemiology, including national surveillance studies (NHANES has used ActiGraph devices), and the activity-count and cut-point literature is extensive.
- ActiGraph is routinely used as the **criterion or reference measure** when validating consumer wearables, for example in mechanical shaker-table comparisons of raw accelerometry across ActiGraph, Apple Watch, Garmin, and Fitbit. Being the comparator is the strongest available statement of standing.
- Actigraphy-based sleep/wake scoring (Sadeh, Cole-Kripke, and successors) is an accepted method in sleep research, with well-characterised limitations, actigraphy systematically overestimates sleep and underestimates wake in disturbed sleepers, and cannot stage sleep.
- **Caveat worth stating plainly:** the strength of the evidence attaches to *raw accelerometry and its established processing pipelines*, not automatically to the newer Insight Watch, LEAP, or the Biovitals/RhythmAnalytics products. Validation of the current device line against the legacy devices that generated the literature is **not established here** and should be requested.

## Strengths

- **Gold-standard research-grade accelerometry** with the deepest validation base and the strongest reviewer acceptance.
- **Raw data preserved and reprocessable indefinitely**, the study's data survives methodological progress.
- **Open-source, reproducible analysis pipelines** (GGIR and others) work on the raw output, making the whole analysis chain auditable.
- **Wear-location flexibility** (wrist, hip, ankle), matches protocol to literature.
- Long battery life suited to multi-week free-living protocols.
- **No participant-facing feedback**, eliminating measurement reactivity.
- Mature multi-site, multi-country clinical-trial platform with adherence monitoring, automated device assignment, and regulatory-engagement support.
- Cellular gateway removes smartphone dependency.
- Expanded multi-sensor platform post-Biofourmis (ECG patch, spirometer, BP cuff).

## Limitations

- **Corporate instability**: rebrand (2025) plus acquisition (2026) means product roadmaps, pricing, support arrangements, and even product names are in flux. Long studies face real continuity risk.
- **Pricing entirely non-public**, and the strategic direction is toward pharma budgets rather than academic ones.
- **Legacy devices going end-of-life** (GT9X Link), breaking continuity with prior study protocols and requiring re-validation for longitudinal cohorts.
- **Cloud-only current platform**, the fully local ActiLife workflow that many institutions preferred may not survive.
- No physiological sensing depth comparable to Empatica (no EDA) or consumer devices (limited/no HR, SpO2, temperature on the core accelerometry devices).
- No participant engagement value.
- Current-device sampling rates, API details, and compliance credentials all unverified.
- Validation of current devices against the legacy devices that generated the literature not established.
- Substantially higher cost per participant than consumer wearables.

## Best-Fit Use Cases

- **Physical activity and sedentary behaviour epidemiology** where comparability with the existing literature is essential.
- **Regulatory-grade digital endpoints** in pharmaceutical clinical trials.
- Studies where **raw accelerometry must be preserved for future reprocessing**.
- Actigraphy-based sleep/wake and rest-activity rhythm research (circadian, chronotype, fragmentation).
- Protocols requiring **non-wrist wear locations**.
- Observational designs where participant feedback would bias the outcome.
- Multi-site international trials needing centralised device logistics and adherence monitoring.
- Populations where a smartphone cannot be relied upon (cellular gateway).

## Poor-Fit Use Cases

- Studies needing rich multimodal physiology (HR, HRV, EDA, SpO2, temperature) from one device.
- Small academic studies on consumer-scale budgets.
- Studies needing participant-facing feedback or engagement.
- Sleep staging endpoints (actigraphy cannot stage sleep).
- Studies requiring a purely local, no-cloud data workflow, unless a legacy path is confirmed available.
- Rapid, low-overhead deployments.

## Open Questions

- *(Directed to Ametris / Signant Health: https://ametris.com/ , https://signanthealth.com/)*

- **What is the actual pricing** for CentrePoint plus Insight Watch or LEAP at academic-study scale? Is there academic pricing at all?
- **What are the sampling rates and configurable ranges** for Insight Watch and ActiGraph LEAP?
- Are these current devices validated against the legacy wGT3X-BT/GT3X+ that generated the literature? Are activity counts comparable?
- **Is ActiLife still supported, and is a fully local (no-cloud) workflow still available?**
- CentrePoint API: authentication, rate limits, export formats, and **whether raw waveform data is retrievable via API** or only processed outcomes.
- What is the roadmap for the ActiGraph device line under Signant Health ownership? What are the end-of-life commitments for currently sold devices?
- Which additional sensors (gyro, magnetometer, HR, light, temperature) are on the current devices?
- 21 CFR Part 11, HIPAA/BAA, GDPR DPA, ISO certifications, data residency, and audit-logging capabilities.
- Battery life, storage capacity, and maximum unattended deployment duration for current devices.
- Does the platform now offer integrated ePRO (given Signant's eCOA business)?
- Data retention and what happens to study data at contract end.

## Key Links

- Ametris (formerly ActiGraph): https://ametris.com/
- CentrePoint: https://ametris.com/centrepoint
- Rebrand announcement: https://blog.ametris.com/news/actigraph-rebrands-as-ametris
- "Embracing Our Next Chapter": https://blog.ametris.com/embracing-our-next-chapter-actigraph-is-now-ametris
- Signant Health acquisition: https://signanthealth.com/company/news/signant-health-acquires-ametris
- Acquisition press release: https://www.prnewswire.com/news-releases/signant-health-acquires-ametris-to-create-an-end-to-end-ecoa-and-digital-outcome-measures-platform-302771426.html
- Signant Health: https://signanthealth.com/
- (Legacy domain `theactigraph.com` now 301-redirects to `ametris.com`)

## Sources

1. Ametris, CentrePoint. https://ametris.com/centrepoint (accessed 2026-08-21). **Primary.** Establishes CentrePoint's description as a cloud platform for real-world digital endpoint data in clinical investigations, the two current devices (CentrePoint Insight Watch, ActiGraph LEAP), "future-proof raw sensor data that can be reprocessed indefinitely," the CentrePoint API for third-party integration, the portal's near-real-time wear compliance and site performance views, automated device assignment, cellular gateway or mobile app collection, customised monthly adherence reports, 70+ country coverage, and the "Ametris, a Signant Health Company" branding.
2. Ametris blog, "ActiGraph Rebrands as Ametris." https://blog.ametris.com/news/actigraph-rebrands-as-ametris (accessed 2026-08-21). Establishes the 25 June 2025 rebrand date and rationale.
3. Signant Health, "Signant Health Acquires Ametris." https://signanthealth.com/company/news/signant-health-acquires-ametris (accessed 2026-08-21); PR Newswire, https://www.prnewswire.com/news-releases/signant-health-acquires-ametris-to-create-an-end-to-end-ecoa-and-digital-outcome-measures-platform-302771426.html. Establishes the May 2026 acquisition and the eCOA + digital outcome measures strategic rationale.
4. Clinical Leader, ActiGraph rebrand coverage. https://www.clinicalleader.com/doc/actigraph-rebrands-as-ametris-to-reflect-expanded-clinical-evidence-generation-capabilities-0001 (accessed 2026-08-21). Establishes the January 2025 Biofourmis Connect acquisition, the Biovitals Analytics Engine and RhythmAnalytics SaMD products, and third-party sensor support (ECG patch, digital spirometer, blood pressure cuff).
5. Fibion pricing guides (**secondary, competitor-published, treat with caution**): https://web.fibion.com/articles/actigraph-pricing-information-guide/ ; https://web.fibion.com/articles/guide-to-actigraph-gt9x-pricing/ ; https://web.fibion.com/articles/actigraph-wgt3x-bt-pricing-accessories-guide/ (accessed 2026-08-21). Source of all reported price figures and of the GT9X end-of-life statement.
6. "Comparison of raw accelerometry data from ActiGraph, Apple Watch, Garmin, and Fitbit using a mechanical shaker table." https://pmc.ncbi.nlm.nih.gov/articles/PMC10980217/ (preprint: https://www.medrxiv.org/content/10.1101/2023.05.25.23290556.full.pdf). Evidence of ActiGraph's use as a reference measure.
