# Ametris (formerly ActiGraph), CentrePoint, ActiGraph LEAP, Insight Watch

## Quick Facts

| Field | Details |
|---|---|
| Organization | **Ametris**, formerly ActiGraph; rebranded 25 June 2025; **acquired by Signant Health** (definitive agreement announced 16 April 2026; acquisition announced 14 May 2026; ametris.com now reads "A Signant Health Company") |
| Category | Research-grade actigraphy and clinical-trial digital endpoint platform |
| Current status | Active, but **undergoing significant corporate and product transition** |
| Platforms/devices | CentrePoint Insight Watch, ActiGraph LEAP; legacy wGT3X-BT (still sold), GT9X Link (new sales ended 2023-08-23), GT3X+ |
| Open source | No for the platform; ActiGraph publishes the `.gt3x` file format and open-source readers (`pygt3x`, `agcounts`) on GitHub |
| Hosting/deployment | CentrePoint cloud platform (AWS and Azure); ActiLife 7 desktop software, labelled "legacy" by Ametris but still updated (v7.3.2.0, 2026-05-08) |
| Pricing model | Not public; "Pricing is calculated for each unique order" (quote); academic pricing list on request; one dated reseller quote found (Czech Republic, July 2025, see Pricing) |
| Last verified | 2026-10-11 (vendor fact record); earlier passes 2026-08-21 and 2026-10-10 |

## Summary

- ActiGraph is the historical **gold standard for research-grade accelerometry**. For roughly two decades it has been the default device in physical activity, sedentary behaviour, and actigraphy-based sleep research, and its "activity counts" are the unit in which an enormous body of literature is expressed. If a study needs raw accelerometry that reviewers will accept without argument, this is the reference.

- **But the company has changed substantially and recently, and the knowledge base should treat prior assumptions as stale:**

- January 2025, acquired the **Biofourmis Connect** digital trial platform, including the Biovitals Analytics Engine and RhythmAnalytics SaMD products.
- 25 June 2025, **rebranded from ActiGraph to Ametris** (pronounced "uh-ME-tris").
- 16 April 2026, **Signant Health announced a definitive agreement to acquire Ametris**, subject to regulatory approvals and closing conditions; on 14 May 2026 Signant announced the acquisition, to create an end-to-end eCOA and digital outcome measures platform (Signant release and PR Newswire, read 2026-10-10). Corrected 2026-10-10; the earlier text dated the announcement to May only.
- The **GT9X Link is discontinued**: Ametris's own FAQ says sales of new GT9X Link devices ended on 23 August 2023 [20]. The wGT3X-BT is described as a "legacy" device but is still sold, with no end-of-sale date published [27].
- The current device line is the **CentrePoint Insight Watch** and **ActiGraph LEAP**.

- The strategic direction is unambiguous: away from selling devices and software to individual academic investigators, and toward being a **pharmaceutical clinical-trial services provider**. That shift matters for anyone planning an academic study, because the enterprise CentrePoint platform with non-public pricing is now the lead product. The device-plus-ActiLife workflow has not been withdrawn, though. As of 2026-10-11 ActiLife 7 is still updated, all ActiLife licences became perpetual on 2025-07-30, and the wGT3X-BT is still sold, with no end-of-support or end-of-sale date published [27][17][19].

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
- **Legacy:** wGT3X-BT (still sold), GT9X Link (new sales ended 2023-08-23 [20]), GT3X+, the devices behind most of the published literature.
- **LEAP configurations:** offered to academics as Core, Pro and Advanced; Pro has green PPG only and Advanced has multiwave (red and green) PPG [27]. Ametris sells the LEAP for clinical research as prescription use only [28].

- **ActiLife**, the desktop software for device initialisation, download, and analysis (activity counts, cut-points, wear-time validation, sleep scoring algorithms such as Sadeh and Cole-Kripke). Ametris's ActiLife page calls ActiLife 7 "legacy" software, but it is still updated (v7.3.2.0 released 2026-05-08) and is the only version that processes LEAP data; ActiLife 6 still works with GT3X and GT9X devices. No end-of-support date is published (checked 2026-10-11) [27][17][19].

- **Post-acquisition additions** (from Biofourmis Connect): the Biovitals Analytics Engine and RhythmAnalytics, a software-as-a-medical-device product. Ametris states the integrated Connect platform supports proprietary ActiGraph wearables alongside validated third-party sensors including an ECG patch, digital spirometer, and blood pressure cuff, meaningfully broadening the platform beyond accelerometry.

## Sensors and Data Streams

- Every Module 1 profile uses the same table so devices can be compared row by row. Rows are the sensors named in `CLAUDE.md`. "Present" is about the hardware; "Researcher access" is about what a study can actually obtain, which is the module's central question. "Unclear" means nothing current was verified. The convention is recorded in [`../../shared/profile-table-conventions.md`](../../shared/profile-table-conventions.md).

| Sensor | Present | Researcher access to underlying signal | Resolution or sampling | Notes |
|---|---|---|---|---|
| PPG | LEAP: multi-wavelength (green 530 nm, red 655 nm, IR 940 nm) | Raw PPG via CentrePoint API Data Access Files: green 25 Hz, green 100 Hz, red/IR 50 Hz, "only available for certain devices, firmware versions, and study configuration, and ... subject to contract restrictions" | 25 to 100 Hz by category | Verified 2026-10-10 (LEAP page; CentrePoint API docs). ActiLife 7 also processes LEAP PPG locally; ActiLife 6 cannot [17]. Pro configuration green only, Advanced multiwave [27]. No PPG listed for Insight Watch or wGT3X-BT. |
| ECG | No | Not applicable | Not applicable |  |
| Accelerometer | Yes | Raw, retained; raw files via CentrePoint API | **Insight Watch and LEAP: 32 to 256 Hz**, primary accelerometer ±8 g (default 32 Hz); **wGT3X-BT: 30 to 100 Hz, ±8 g** | Verified 2026-10-10 (Ametris product pages). Primary range is listed as fixed, not configurable. LEAP IMU accelerometer ±16 g in one spec block, ±2 g/±16 g in another. |
| Gyroscope | LEAP (IMU) | Raw IMU files via CentrePoint API (`imu` category) | ±2000 dps; rate not stated | Verified 2026-10-10. One LEAP spec block footnotes these sensors as available "Q1 2024 or later". |
| Magnetometer | Not listed for current devices | Not applicable | Not applicable | Not on the Insight Watch, LEAP or wGT3X-BT spec pages (2026-10-10). |
| Temperature | LEAP (skin, -20 to 50 °C); Insight Watch (near-body) | Raw temperature files via CentrePoint API | Not stated | Verified 2026-10-10. |
| SpO2 | LEAP: listed as an investigational vital sign (derived from PPG) | Through Ametris Scientific Services only; not covered by the LEAP 510(k) | Not stated | ametris.com/actigraph-leap lists "Oxygen Saturation (SpO2)" and says vital signs beyond activity, sleep and mobility are "for investigational use only" (vendor fact record, 2026-10-11) [9]. No SpO2 for Insight Watch or wGT3X-BT. |
| GPS | No | Not applicable | Not applicable |  |
| Barometer / altimeter | LEAP: 300 to 1100 hPa | Raw barometer files via CentrePoint API | Not stated | Verified 2026-10-10. LEAP also has a microphone (100 Hz to 10 kHz), disabled by default. |
| EDA | No | Not applicable | Not applicable |  |
| Ambient light | wGT3X-BT | Lux values alongside motion data | Not stated | Verified 2026-10-10 (wGT3X-BT page). |
| Other | Unclear | Unclear | Unclear | Not verified against current documentation. |

**Verification.** Re-verified 2026-10-10 against ametris.com/cpiw, /actigraph-leap and /actigraph-wgt3x-bt and the CentrePoint API documentation (**Verified**). Storage and battery: Insight Watch 30 days / 512 MB and 30 days battery at the default 32 Hz; wGT3X-BT 180 days / 4 GB and 25 days battery. **LEAP (updated 2026-10-11, Corroborated).** Storage is 79 days / 1 GB at the default 32 Hz with the accelerometer only, and battery is 1 to 32 days depending on configuration, about 32 days at that default. The LEAP Instructions for Use (Rev 3, released 2024-12-04, read from a copy attached to a public Czech procurement record) and every configuration on academic.ametris.com/actigraph-leap give 79 days [27][23]. One older spec block on ametris.com/actigraph-leap still says 30 days storage and 30 days battery; it carries no condition and nothing else supports it, so it is treated as an outdated figure. Corroborated rather than Verified because the vendor page still contradicts itself. See the notes below for the original wording.

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

- **CentrePoint outputs** (Integration Guide, 2026-10-11) are minute (epoch) summaries at 15, 30 or 60 seconds, daily statistics, sleep periods and event markers covering steps, wear, sleep, energy expenditure and activity-intensity cut points [22].
- **LEAP vital signs** (heart rate, HRV, skin temperature, AF/cardiac rhythm, SpO2, respiratory rate) and gait and balance measures need Ametris Scientific Services and are investigational. The LEAP 510(k) covers activity, sleep and mobility only [9].
- **Partner algorithms** run in the Ametris platform, including Hyfe cough, PKG by Empatica, Mobilise-D digital mobility outcomes and CSEM vital signs [29].

## Active Data Collection

- Not a survey/EMA platform natively. Under Signant Health, whose core business is eCOA (electronic clinical outcome assessment), integrated ePRO alongside device data is the explicit strategic direction of the acquisition. For sponsors, a combined Ametris DHT plus Signant eCOA offering for CNS trials was announced on 2026-03-10, before the acquisition, and AliveCor ECG and Kayentis eCOA integrations were announced in early 2026 (vendor fact record note, `academic_vs_commercial`, 2026-10-11). How deep the integration goes, and whether it reaches academic customers, is not stated.

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
- **CentrePoint API (V3), documented publicly on GitHub (`actigraph/CentrePoint3APIDocumentation`, last pushed 2026-07-08; read 2026-10-10, Verified).** Ametris's marketing says "Data outcomes" can be integrated through the API, which undersells it: the API returns raw data as well as outcomes.
  - **Authentication:** OAuth 2.0 client-credentials grant; tokens expire after 3,600 s. ActiGraph/Ametris must enable API access for the account and issue the client ID and secret.
  - **Raw data:** "Data Access Files", pre-made day files under the `DataAccess` scope, in categories raw-accelerometer, temperature, ppg-green (25 Hz), ppg-green-100-hz, barometer, imu and ppg-red-ir-50-hz. The PPG categories are "only available for certain devices, firmware versions, and study configuration, and ... subject to contract restrictions". Formats: gzipped CSV or AVRO.
  - **Raw activity requests** (`DataRetrieval` scope, formats gt3x, csv or avro) are capped at 10 concurrent requests, GT3X-format ranges are limited to 15 days, and the docs now recommend Data Access Files instead for raw accelerometer data [10]. They must not be used "to retrieve ALL the historic RAW data for all subjects in a given study"; they are meant to be used with the raw-processing-complete webhook as data arrive. The docs warn that "There may be fees associated for historical data access file generation if the study has not been previously setup."
  - **Derived data:** minute (epoch) summaries, daily statistics, sleep periods, study, subject and visit management, and webhooks, including one that pushes daily statistics [22].
  - **Rate limit:** more than 500 requests per minute from one IP address returns HTTP 429. The older V2 (Study Admin) API is still supported with separate credentials and has an unpublished daily request limit [22][30].
  - **History depth (Unclear, 2026-10-11).** No limit on how far back CentrePoint data can be retrieved is published [10].
  - **Access** is enabled per customer by contacting Ametris; there is no self-serve developer program. CROs and technology vendors can get API integration and raw study data through the Accelerant Partnership Program [10][25].
- **Web portal** access to compliance and outcome data.
- Device path: device → ActiLife → local files (`.gt3x` raw, plus derived `.agd`/CSV); ActiLife exports scored daily, hourly and summary data as one consolidated CSV [27].
- **ActiLife Data Vault storage (conflict, recorded 2026-10-11).** The ActiLife product page and the ActiLife 7 upgrade FAQ say a licence's first-year maintenance or a coverage plan includes 20 GB of Data Vault storage; the ActiLife 7 User's Manual (Revision I, effective 2026-01-30) says ActiLife 7 users get 4 GB free [27][17][18]. One possible reading is 4 GB base and 20 GB while covered, but no page says so. Ask Ametris.
- The CentrePoint Connect iOS participant app requires iOS 18 or later (vendor fact record note, 2026-10-11).

## APIs, SDKs, and Extensibility

- CentrePoint API: public documentation on GitHub (see Data Access and Export).
- Third-party sensor support in the Connect platform (ECG patch, spirometer, BP cuff).
- ActiGraph publishes the `.gt3x` file format itself (`actigraph/GT3X-File-Format`) and its own open-source tools on GitHub, including `pygt3x` (Python GT3X/AGDC reader), `agcounts` (ActiLife counts in Python), `actiapi` (CentrePoint API client) and `vertdetach` (DETACH non-wear algorithm) [21]. Community readers in R and Python also exist. Together these are an important hedge against vendor lock-in.
- RADAR-base has an open roadmap issue (RADAR-REST-Connector issue 153, opened 2024-12-16) for a LEAP connector via the CentrePoint API; no shipped third-party connector was found (2026-10-11).
- No device SDK.

## Deployment and Infrastructure

- Vendor cloud (CentrePoint), hosted on Amazon Web Services and Microsoft Azure; regions and residency options are not published [24]. Ametris announced a China deployment partnership (Lingyan Innovation, 2025-11-20) without saying where Chinese participant data are hosted. No self-hosting.
- **A local workflow is still available (2026-10-11).** ActiLife 7 initialises devices and processes downloaded device files on the researcher's own machine, including LEAP accelerometer and PPG data; Data Vault cloud storage is optional [27][17]. Some IRBs and institutions strongly prefer this. **The move to a cloud platform is a governance change, not just a convenience change**, and the ActiLife page's "legacy" label, with no end-of-support date, is the thing to watch.

## Participant Experience

- Devices are worn at the wrist, hip, or ankle depending on protocol, **wear location flexibility is a research-grade feature** that consumer wrist wearables do not offer. Hip-worn placement remains the convention for much of the physical activity literature; wrist for sleep/24h protocols.
- **Extended battery life** suitable for remote monitoring, a design priority for both Insight Watch and LEAP. Historically ActiGraph devices ran for weeks on a charge, which is why they dominate 7-day and 14-day free-living protocols.
- **Cellular gateway option removes the smartphone requirement**, as with Withings, this unlocks populations that cannot reliably operate a phone app.
- Devices have no participant-facing display or feedback in the traditional research configuration, which is deliberate: **it prevents the measurement from changing the behaviour being measured.** For observational physical activity research this is a methodological requirement, not a limitation.
- Correspondingly, there is no participant engagement value; adherence depends on study contact and on the monitoring/reporting that CentrePoint provides.

## Privacy, Security, and Compliance

- **Ametris Compliance Center (read 2026-10-10).**
  - QMS conforms to **ISO 13485:2016**, with participation in **MDSAP** since 2018 and annual surveillance audits by an independent auditing organisation; certificates are linked on the page. **Verified** that the page says so.
  - **GDPR:** Ametris "will support customers in meeting their GDPR requirements with data processing agreement[s]" including standard contractual clauses, and states compliance with the EU-U.S. Data Privacy Framework, its UK Extension and the Swiss-U.S. DPF.
  - **Security:** **ISO/IEC 27001:2022** certificate IA391-260410-001, issued by Ignyte Assurance LLC to Actigraph L.L.C. dba Ametris; initial certification 2026-04-16, valid to 2029-04-15; scope is the ISMS for the digital health platform ecosystem (**Verified** 2026-10-11 from the certificate PDF linked on the compliance page) [16]. The PDF is hosted on Ametris's site, not a registry, and the certification body's accreditation was not checked. Hosting uses "qualified cloud vendors: Microsoft Azure and Amazon Web Services".
  - **Validation:** describes design validation and a procedure for validating computerised systems; the page does not say "21 CFR Part 11" in words.
  - **HIPAA (Unclear, 2026-10-11).** No written HIPAA statement on the compliance page or in the privacy policy. The compliance page shows a logo image whose alt text is "HIPAA Compliant"; that badge is the only HIPAA claim found [11][24].
  - **SOC 2 (Unclear, Reported).** A company-data aggregator reports an October 2023 announcement that ActiLife and CentrePoint achieved SOC 2 Type II attestation; the original release, auditor and report period were not found, and the current compliance page does not mention SOC 2 [26]. Whether a current attestation exists is unknown; ask Ametris for the latest report.
  - **BAA (not public, 2026-10-11).** No BAA offer on public pages; customer contracts are not public, so one could exist there [11][24].
  - **Data roles and retention.** Per the privacy policy (last updated 2025-02-20, before the Signant acquisition), the study organization is the data controller and Ametris the processor. Personal data is kept in identifiable form only as long as it serves a processing purpose; customer removal requests are answered within 30 days, and participants must send access or deletion requests to the sponsor. No fixed retention period for study data is published [24].
  - **AI training (not public, Corroborated).** Nothing in the privacy policy, compliance page or API docs names AI or model training on customer data. The Signant acquisition release names AI and machine learning across eCOA and sensor data as a direction [24][31].
  - **Not found:** any statement on whether the Signant acquisition changed data-processing terms.
- **FDA 510(k)s (openFDA, 2026-10-11).** **Verified** from the FDA database [12][15]
  - K231532, ActiGraph LEAP activity monitor, cleared 2023-06-23 (Special 510(k)), product code LEL, predicate K181077.
  - K181077, ActiGraph CentrePoint Insight Watch, cleared 2018-05-24 (Special 510(k)), product code LEL, predicate K080545.
  - K080545, ActiTrainer, cleared 2008-07-24 (Traditional 510(k)), product code ISD, predicate K040554.
  - K040554, ActiGraph AM7164 models, applicant Manufacturing Technology, Inc., cleared 2004-07-16; Ametris lists it as inactive.
- **wGT3X-BT and GT9X Link (Reported, per Ametris).** Ametris's compliance page lists K080545 as the clearance for the GT9X and wGT3X-BT. The FDA record for K080545 names only the 2008 ActiTrainer, and the FDA database has no 510(k) under either device name [11][15]. A modified device can be marketed under an existing 510(k) without a new database entry, so the mapping may be legitimate, but it cannot be confirmed from the regulator. Health Canada licence 102376 (Class II) lists both devices from 2019-02-11 (MDALL, per the vendor fact record note).

## Pricing

- **Not published.** Ametris's device pages say: "Pricing is calculated for each unique order. For a price quote or more information, please contact our team directly." (LEAP and Insight Watch pages, **Verified** 2026-10-10.) The academic store lists only accessories (for example LEAP wristband US$25.00, Insight Watch charging dock US$45.00) [13].

- **One dated real-order price (Reported, 2026-10-11).** Reseller ProCare B.V. quoted Palacký University Olomouc on 2025-07-17 for 190 LEAP devices at CZK 15,625 each (watchband CZK 875, charger CZK 1,500 each) and a 3-year ActiLife 7 Single licence at CZK 136,750. A CZK 1,067,025 discount (about 30%) applied to the CZK 3,556,750 subtotal, for a total of CZK 2,489,725 excluding VAT [23]. This is one academic order through a European reseller, not a list price; the discount applies to the whole order, so no per-device net price is stated. Figures are not converted because no dated exchange rate is recorded.
- **ActiLife licensing.** Sold by quote in activation tiers, from Single (1 full, 5 lite activations) to Large Enterprise (15 full, 20 lite) [27]. All active licences were converted to perpetual licences on 2025-07-30; new licences include one year of maintenance and service, and paid coverage plans (support, file repair, updates, Data Vault storage) are offered for existing licences [17]. The Czech quote above priced a 3-year licence 13 days before that conversion.
- **CentrePoint fees.** Licence and API fees are not published. The API docs say generating historical data access files may carry fees if the study was not set up for them [10]. No participant, device or study limits are published for CentrePoint, and no minimum commitment is published for any product.

The figures below are older and **Reported**, from a **competitor's** published pricing guides (Fibion, which sells alternative research accelerometry), except the US$349 ActiLife figure, which is from a 2022 systematic review. Treat them as indicative order-of-magnitude only, and note the obvious source bias. A Fibion figure of about US$600 for the LEAP repeats an unverified forum post and is not used here.

| Item | Reported price |
|---|---|
| GT3X+ | $325, $1,016 (varies by region/distributor/agreement) |
| GT9X Link | ~$500 (new sales ended 2023-08-23 per Ametris [20]) |
| wGT3X-BT | $325, $1,016 |
| ActiLife software | **Conflicting secondary figures: US$349 or ~$1,695** (see note below the table) |
| CentrePoint software | ~$3,500/year |
| CentrePoint Hub | ~$600 purchase, or ~$300/year rental |

- **ActiLife price conflict (recorded 2026-10-10, Unclear).** Two secondary sources disagree and neither is a vendor price. Ngueleu et al. 2022 (*J Neuroeng Rehabil*, PMC9575229, full text read 2026-10-10) gives device prices "between US$325 (+ US$349 for the Actilife software) and US$1016" with no date or region for the quote. The ~$1,695 figure is from the Fibion pricing guides read on 2026-08-21, which per search-engine excerpts attribute it to a ResearchGate forum post and describe it as a price from "some years ago"; a direct re-read on 2026-10-10 was blocked by a Cloudflare bot check and was not bypassed. The two figures may reflect different years, licence types or regions; this is not established. Ametris's ActiLife page (read 2026-10-10) shows no price, only "Request a Quote". Budget from a quote, not from either figure. (Independent review finding R-146.)

### Research program and academic data access (checked 2026-10-10)

- **An academic channel exists.** academic.ametris.com ("Academic Research and Population Health") offers a "Get Pricing List" form, a "Grant Toolkit", a dataset library and a contact route to an "academic and public health research team". Its Academic Store (store.ametris.com) sells accessories online (wristbands, chargers, docks, USB hubs, priced in USD) but device prices are not shown, and "Online purchasing through our store is currently available only to academic institutions with existing client accounts". International customers are sent to resellers. **Verified** (2026-10-10). No academic discount, grant program or free-device scheme is described; a one-off research grant was announced in August 2022, and no current grant call was found (2026-10-11). No application or review step is published.
- **Accelerant Partnership Program (2026-10-11).** A three-tier partner program for CROs and technology vendors that resell or deliver Ametris technology to trial sponsors; the middle tier (Accelerant API) includes API integration and access to raw study data. It is not aimed at academic investigators [25].
- **What academics can get:** the same devices and the same data as sponsors. Raw accelerometry (and, where licensed, PPG, temperature, barometer and IMU files) comes through CentrePoint's API or portal, or through ActiLife from `.gt3x` files on the legacy workflow. The API docs warn that historical raw-file generation may carry fees and that some PPG categories are "subject to contract restrictions". **Verified.**
- **How it differs from commercial access:** no separate academic data tier is documented; the difference is the sales channel (academic store and pricing list) rather than the data. **Unclear** whether academic prices differ.
- **Status:** active; now part of Signant Health.

- Current-device (Insight Watch, LEAP) and CentrePoint platform pricing under Ametris/Signant has **no published list price**; the only dated figure found is the July 2025 Czech reseller quote above. The strategic shift toward pharmaceutical clients suggests pricing is now oriented to sponsor budgets rather than academic grants, which should be tested early in study planning rather than assumed.

## Research Evidence and Validation

- **The deepest validation base of any device in this module.** ActiGraph accelerometry underpins decades of physical activity epidemiology, including national surveillance studies (NHANES has used ActiGraph devices), and the activity-count and cut-point literature is extensive. Ametris says NHANES selected the LEAP for its 2027-2030 cohort (Ametris blog, 2025-02-26, https://blog.ametris.com/blog/actigraph-wearables-support-nhanes-2027); not confirmed on a CDC page as of 2026-10-11.
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
- **Device pricing non-public** (quote or pricing list on request), and the strategic direction is toward pharma budgets rather than academic ones.
- **Legacy devices going end-of-life** (GT9X Link sales ended 2023-08-23; wGT3X-BT labelled legacy), breaking continuity with prior study protocols and requiring re-validation for longitudinal cohorts.
- **Cloud-first current platform.** CentrePoint has no self-hosting; the local ActiLife 7 workflow still exists but is labelled "legacy", with no end-of-support date published.
- No physiological sensing depth comparable to Empatica (no EDA). The LEAP has PPG and skin temperature, but its HR, HRV, SpO2 and other vital signs are investigational, need Scientific Services, and sit outside its 510(k); the Insight Watch and wGT3X-BT have no PPG.
- No participant engagement value.
- No written HIPAA statement (a "HIPAA Compliant" badge only), no BAA offer, no current SOC 2 evidence and no explicit Part 11 statement are published (checked 2026-10-11).
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
- Studies requiring a purely local, no-cloud data workflow over a long horizon, since that path (ActiLife 7) is labelled legacy and its support term is not published.
- Rapid, low-overhead deployments.

## Open Questions

- *(Directed to Ametris / Signant Health: https://ametris.com/ , https://signanthealth.com/)*

- **What is the actual pricing** for CentrePoint plus Insight Watch or LEAP at academic-study scale? Is there academic pricing at all?
- ~~What are the sampling rates and configurable ranges for Insight Watch and ActiGraph LEAP?~~ Resolved 2026-10-10: 32 to 256 Hz, primary accelerometer ±8 g (fixed). LEAP storage taken as 79 days / 1 GB at the default (IFU Rev 3, 2026-10-11, Corroborated); Ametris should still remove or explain the 30-day spec block.
- Are these current devices validated against the legacy wGT3X-BT/GT3X+ that generated the literature? Are activity counts comparable?
- ~~Is ActiLife still supported, and is a fully local (no-cloud) workflow still available?~~ Resolved 2026-10-11: ActiLife 7 is current (v7.3.2.0, 2026-05-08), licences are perpetual since 2025-07-30, and local processing remains available. Still open: what the "legacy" label means for support, and whether the Data Vault allowance is 4 GB or 20 GB.
- Which 510(k) or letter-to-file covers the GT9X and wGT3X-BT (Ametris lists K080545, which the FDA record names as the ActiTrainer)?
- What do the historical data access file fees cost, and is there any limit on CentrePoint history depth?
- ~~CentrePoint API: authentication, rate limits, export formats, raw vs outcomes.~~ Resolved 2026-10-10 from the public API docs: OAuth client credentials, 500 requests per minute per IP, CSV or AVRO, raw and derived both available. Still open: the fees for historical raw-file generation and the contract terms behind PPG access.
- What is the roadmap for the ActiGraph device line under Signant Health ownership? Signant says the combined company will keep Ametris' roadmap [31]. What are the end-of-life commitments for currently sold devices, including the wGT3X-BT?
- ~~Which additional sensors (gyro, magnetometer, HR, light, temperature) are on the current devices?~~ Largely resolved 2026-10-10 and 2026-10-11 (see the Sensors table).
- 21 CFR Part 11 attestation, a written HIPAA statement and BAA, a current SOC 2 Type II report, data residency regions, audit logging, and whether the Signant acquisition changed data-processing terms. (DPA with SCCs, DPF, ISO 13485/MDSAP were documented 2026-10-10; the ISO 27001:2022 certificate was read 2026-10-11.)
- ~~Battery life, storage capacity, and maximum unattended deployment duration for current devices.~~ Largely resolved 2026-10-10 and 2026-10-11 (see the Verification paragraph under Sensors and Data Streams).
- Does integrated ePRO reach academic customers? A combined Ametris DHT plus Signant eCOA offering for CNS trials was announced for sponsors on 2026-03-10; depth not stated.
- What happens to study data at contract end? The privacy policy publishes no fixed retention period.

## Vendor Fact Record

<!-- facts:begin -->
*Generated from the fact record by `tools/facts/generate.py`. Edit the record, not this block.*

**Research access**

| Fact | Value |
|---|---|
| Formal research or academic program (name, what it offers) | **Academic channel:** No formal named research program with an application. Ametris runs an academic and public health research channel (academic.ametris.com): an academic team to contact, an academic online store, a pricing list on request, a grant toolkit and an open-source dataset library. [V, 2026-10-11]<br>**Accelerant Partnership Program (CROs and technology partners):** A three-tier partner program for CROs and technology vendors that resell or deliver Ametris technology to trial sponsors. The middle tier (Accelerant API) includes API integration and access to raw study data. Not aimed at academic investigators. [V, 2026-10-11] |
| Who can join the research program | Online purchasing in the academic store is limited to academic institutions with existing client accounts (accredited universities, research institutions, healthcare organizations, government research centers). International buyers go through authorized resellers. The LEAP is sold for clinical research as a prescription device. [V, 2026-10-11] |
| How to apply, and any approval or review step | No application or review step is published. Researchers contact the academic team, request a quote or the pricing list, or schedule a meeting. CentrePoint API access is enabled per customer on request. [V, 2026-10-11] |
| Whether the program is active, paused, renamed or closed | Academic channel and store live under the Ametris name as of 2026-10-11. Signant Health announced a definitive agreement to acquire Ametris on 2026-04-16 and announced the acquisition on 2026-05-14. Signant says the combined company will keep Ametris' roadmap. [V, 2026-10-11] |
| Whether the general developer or API program is open to new applicants | No self-serve developer program. The CentrePoint V3 API (OAuth 2.0) is documented publicly on GitHub, but access is enabled per customer by contacting the company, and it reaches only CentrePoint study data the client can already see. The V2 (Study Admin) API is still supported with separate credentials. CROs and technology vendors can get API and raw-data access through the Accelerant partner program. [V, 2026-10-11] |
| Participant or user limits before approval or by tier | **ActiLife licences:** ActiLife licences are tiered by activations, from Single (1 full, 5 lite) to Large Enterprise (15 full, 20 lite). [V, 2026-10-11]<br>**CentrePoint:** Not public [2026-10-11] |
| How academic access differs from commercial or consumer access | Academic and population-health customers have a separate site, academic store and academic team, and can choose cloud CentrePoint or desktop ActiLife; LEAP is offered to academics in Core, Pro and Advanced configurations. Industry trials are served through ametris.com with operational and scientific support. Both are priced by quote; how academic prices or terms differ is not published. [V, 2026-10-11] |

**Pricing**

| Fact | Value |
|---|---|
| Device or hardware list price | **Vendor list prices:** Not public [2026-10-11]<br>**ActiGraph LEAP, one reseller quote, Czech Republic, July 2025:** CZK 15,625 per LEAP device for 190 units (watchband CZK 875, charger CZK 1,500 each), quoted 2025-07-17 by reseller ProCare B.V. to Palacký University Olomouc. The same quote has a 3-year ActiLife 7 Single licence at CZK 136,750 and a CZK 1,067,025 discount on the CZK 3,556,750 subtotal (total CZK 2,489,725 excl. VAT). One academic order through a European reseller; not a list price. [R, 2026-10-11] |
| Consumer subscription or membership price | n/a |
| Research or academic pricing or discount | Not public [2026-10-11] |
| Fees for API, SDK, platform or data access | **CentrePoint API:** CentrePoint licence and API fees are not published. The API documentation says generating historical data access files may carry fees if the study was not set up for them. [V, 2026-10-11]<br>**ActiLife licences:** ActiLife is sold in activation tiers by quote. All active licences were converted to perpetual licences on 2025-07-30. New licences include one year of maintenance and service; paid coverage plans (support, file repair, updates, Data Vault storage) are offered for existing licences. [V, 2026-10-11]<br>**ActiLife Data Vault storage:** The ActiLife product page and the ActiLife 7 upgrade FAQ say licences or coverage plans include 20GB of Data Vault storage; the ActiLife 7 User's Manual (Revision I, effective 2026-01-30) says ActiLife 7 users get 4GB free. (conflict) [U, 2026-10-11] |
| Minimum order, term or commitment | Not public [2026-10-11] |
| Whether pricing requires contacting sales | Yes. Devices, CentrePoint and ActiLife are priced per order by quote; international buyers go through authorized resellers. [V, 2026-10-11] |

**Data access and terms**

| Fact | Value |
|---|---|
| Raw signals available to researchers, and by which route | **CentrePoint API:** Data Access Files by category: raw accelerometer for all devices, plus temperature, green PPG at 25 Hz or 100 Hz, red/IR PPG at 50 Hz, barometer and IMU only for certain devices, firmware, study configurations and contracts. Delivered as day files in CSV or AVRO. [V, 2026-10-11]<br>**Devices and ActiLife:** LEAP sensors: accelerometer, gyroscope, PPG (green, red, IR), skin temperature, barometer and a microphone that is off by default. wGT3X-BT: raw acceleration collected at 30 to 100 Hz and transferred to researchers. Raw device files can be processed locally in ActiLife; ActiLife 7 also processes LEAP PPG, which ActiLife 6 cannot. [V, 2026-10-11] |
| Derived or processed metrics available to researchers | CentrePoint: minute (epoch) summaries, daily statistics, sleep periods and event markers covering steps, wear, sleep, energy expenditure and activity-intensity cut points. ActiLife scores data with published algorithms. LEAP vital signs (HR, HRV, skin temperature, AF/cardiac rhythm, SpO2, respiratory rate) and gait and balance measures need Scientific Services and are investigational; the LEAP 510(k) covers activity, sleep and mobility only. Partner algorithms (Hyfe cough, PKG by Empatica, Mobilise-D, CSEM vital signs) run in the Ametris platform. [V, 2026-10-11] |
| Documented sampling rates or temporal resolution | **ActiGraph LEAP:** Accelerometer 32 to 256 Hz (32 Hz default); battery 1 to 32 days depending on configuration. [V, 2026-10-11]<br>**CentrePoint Insight Watch:** 32 to 256 Hz raw acceleration [V, 2026-10-11]<br>**ActiGraph wGT3X-BT:** 30 to 100 Hz raw acceleration [V, 2026-10-11]<br>**CentrePoint API files and summaries:** Green PPG at 25 Hz or 100 Hz; red/IR PPG at 50 Hz; epoch summaries at 15, 30 or 60 seconds. [V, 2026-10-11] |
| How far back data can be retrieved | **On-device storage:** LEAP 79 days / 1 GB at the default 32 Hz with the accelerometer only; CentrePoint Insight Watch 30 days / 512 MB; wGT3X-BT 180 days / 4 GB. [C, 2026-10-11]<br>**CentrePoint cloud:** Unclear |
| Export, API, SDK or file routes | CentrePoint: web portal; V3 REST API (OAuth 2.0) with daily Data Access Files in gzipped CSV or AVRO, raw requests in GT3X, CSV or AVRO, summaries and webhooks that push daily statistics; the V2 API is still supported. ActiLife: local desktop processing of downloaded device files with consolidated CSV export, plus Data Vault cloud storage. ActiGraph publishes the .gt3x file format and open-source readers on GitHub. [V, 2026-10-11] |
| API rate limits | CentrePoint V3 API: more than 500 requests a minute from one IP returns HTTP 429. Raw data requests: at most 10 active at once, GT3X ranges limited to 15 days. V2 API: an unpublished daily request limit. [V, 2026-10-11] |
| Terms on retaining, storing or deleting data | Ametris acts as data processor for the study organization (controller). Personal data is kept in identifiable form only as long as it serves a processing purpose; customer removal requests are answered within 30 days, and participants must send access or deletion requests to the sponsor. No fixed retention period for study data is published. [V, 2026-10-11] |
| Terms on using data to train AI or ML models | Not public [2026-10-11] |
| Announced shutdowns, deprecations or migrations, with dates | **ActiLife:** The ActiLife page calls ActiLife 7 "legacy" software, yet it is still updated (v7.3.2.0 released 2026-05-08) and is the only version that handles LEAP data; ActiLife 6 still works with GT3X and GT9X devices. No end-of-support date is published. [V, 2026-10-11]<br>**ActiGraph wGT3X-BT and GT9X Link:** Sales of new GT9X Link devices ended on 2023-08-23. The wGT3X-BT is described as a legacy device but is still sold; no end-of-sale date is published. [V, 2026-10-11]<br>**CentrePoint API:** The raw activity data request endpoint is superseded by Data Access Files for raw accelerometer data; the V2 (Study Admin) API is still supported alongside V3. No shutdown dates published. [V, 2026-10-11] |

**Compliance and regulatory**

| Fact | Value |
|---|---|
| Whether a HIPAA Business Associate Agreement is offered | Not public [2026-10-11] |
| Whether a data processing agreement is offered | Yes. Ametris offers data processing agreements with standard contractual clauses to support customers' GDPR obligations. [C, 2026-10-11] |
| Published HIPAA statement | Unclear |
| Published GDPR statement | Ametris states it complies with GDPR and has self-certified to the EU-U.S. Data Privacy Framework, its UK extension and the Swiss-U.S. DPF. [C, 2026-10-11] |
| ISO/IEC 27001 status and evidence | ISO/IEC 27001:2022 certificate IA391-260410-001 issued by Ignyte Assurance LLC to Actigraph L.L.C. dba Ametris; initial certification 2026-04-16, valid to 2029-04-15. Scope is the ISMS for the digital health platform ecosystem. [V, 2026-10-11] |
| SOC 2 status and evidence | Unclear |
| FDA clearances, from the FDA database | **ActiGraph LEAP:** 510(k) K231532, ActiGraph LEAP activity monitor, applicant Actigraph, LLC, cleared 2023-06-23 (Special 510(k)), product code LEL, 21 CFR 882.5050. Predicate K181077. [V, 2026-10-11]<br>**CentrePoint Insight Watch:** 510(k) K181077, ActiGraph CentrePoint Insight Watch, cleared 2018-05-24 (Special 510(k)), product code LEL. Predicate K080545 (ActiTrainer). [V, 2026-10-11]<br>**K080545 (ActiTrainer):** 510(k) K080545, ACTITRAINER, applicant Actigraph, LLC, cleared 2008-07-24 (Traditional 510(k)), product code ISD (exerciser, measuring, 21 CFR 890.5360). Predicate K040554 (ActiGraph AM7164). [V, 2026-10-11]<br>**ActiGraph wGT3X-BT and GT9X Link (vendor's mapping to K080545):** Ametris lists K080545 as the clearance for the GT9X and wGT3X-BT. That mapping is the vendor's claim only. The FDA database has no 510(k) under either device name, and the K080545 record is the 2008 ActiTrainer. [R, 2026-10-11]<br>**ActiGraph AM7164 (legacy):** 510(k) K040554, ActiGraph models AM7164-2.2 and AM71256, applicant Manufacturing Technology, Inc., cleared 2004-07-16, product code GWQ. Ametris lists it as inactive. [V, 2026-10-11] |
| Where data is stored, and residency options | CentrePoint is hosted on Amazon Web Services and Microsoft Azure. Regions and residency options are not published. [V, 2026-10-11] |

<!-- facts:end -->

## Key Links

- Ametris (formerly ActiGraph): https://ametris.com/
- CentrePoint: https://ametris.com/centrepoint
- Rebrand announcement: https://blog.ametris.com/news/actigraph-rebrands-as-ametris
- "Embracing Our Next Chapter": https://blog.ametris.com/embracing-our-next-chapter-actigraph-is-now-ametris
- Signant Health acquisition: https://signanthealth.com/company/news/signant-health-acquires-ametris
- Signant definitive-agreement release (16 April 2026): https://signanthealth.com/company/news/signant-health-enters-definitive-agreement-to-acquire-ametris
- CentrePoint API documentation: https://github.com/actigraph/CentrePoint3APIDocumentation
- Compliance Center: https://ametris.com/compliance
- Academic research site: https://academic.ametris.com/ ; academic store: https://store.ametris.com/
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
7. Signant Health, "Signant Health Enters Definitive Agreement to Acquire Ametris", 16 April 2026. https://signanthealth.com/company/news/signant-health-enters-definitive-agreement-to-acquire-ametris (accessed 2026-10-10). **Primary.**
8. PR Newswire, "Signant Health Acquires Ametris to Create an End-to-End eCOA and Digital Outcome Measures Platform", 14 May 2026. https://tools.prnewswire.com/en-us/live/20813/release/20260514EN58707 (accessed 2026-10-10). **Primary (company release).** Announces the acquisition; no explicit closing sentence. Ametris's own page (https://ametris.com/signant-health-company, accessed 2026-10-10) reads "A Signant Health Company".
9. Ametris product pages: https://ametris.com/cpiw , https://ametris.com/actigraph-leap , https://ametris.com/actigraph-wgt3x-bt , https://ametris.com/actilife (accessed 2026-10-10). **Primary.** Sample rates, ranges, storage, battery, sensors, the per-order pricing statement, ActiLife maintenance and Data Vault.
10. ActiGraph CentrePoint V3 API documentation. https://github.com/actigraph/CentrePoint3APIDocumentation (README, sections/authorization.md, sections/data_access_files.md, sections/raw_data_request.md; repository last pushed 2026-07-08; accessed 2026-10-10). **Primary.**
11. Ametris Compliance Center. https://ametris.com/compliance (accessed 2026-10-10). **Primary, vendor statement.**
12. openFDA 510(k) K231532 and K181077. https://api.fda.gov/device/510k.json?search=k_number:K231532 ; https://api.fda.gov/device/510k.json?search=k_number:K181077 (accessed 2026-10-10). **Primary.**
13. Ametris academic research site and academic store. https://academic.ametris.com/ ; https://store.ametris.com/ (accessed 2026-10-10). **Primary.** Academic channel, pricing-list form, grant toolkit, accessory prices, existing-account restriction.
14. Ngueleu A.-M. et al. "Criterion validity of ActiGraph monitoring devices for step counting and distance measurement in adults and older adults: a systematic review." *J Neuroeng Rehabil* 2022;19:112. https://pmc.ncbi.nlm.nih.gov/articles/PMC9575229/ (DOI 10.1186/s12984-022-01085-5; full text read via NCBI E-utilities 2026-10-10). **Secondary.** Source of the US$349 ActiLife figure and of manufacturer wear-site guidance (wrist, ankle, thigh, hip).
15. FDA 510(k) database, K080545 (ActiTrainer) and K040554 (ActiGraph AM7164). https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K080545 ; https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K040554 (accessed 2026-10-11). **Primary, regulator.** Predicates for K181077 and K231532 read from the FDA 510(k) summary PDFs.
16. Ametris ISO/IEC 27001:2022 certificate, Ignyte Assurance. https://ametris.com/hubfs/Quality%20Assurance/Ametris%20-%20Ignyte%2027001%20Certificate.pdf (accessed 2026-10-11). **Primary, certificate (vendor-hosted).**
17. Ametris blog, ActiLife 7 upgrade FAQ. https://blog.theactigraph.com/blog/faq-actilife7-upgrade (accessed 2026-10-11). **Primary.** Perpetual licence conversion on 2025-07-30, coverage plans, 20 GB Data Vault, LEAP PPG only in ActiLife 7, ActiLife 6 still works with GT3X and GT9X.
18. ActiLife 7 User's Manual, Revision I (effective 2026-01-30). https://ametris.com/hubfs/User%20Manuals/ActiLife%207%20Users%20Manual.pdf (accessed 2026-10-11). **Primary.** 4 GB free Data Vault space.
19. Ametris downloads page. https://ametris.com/downloads (accessed 2026-10-11). **Primary.** ActiLife v7.3.2.0 released 2026-05-08.
20. Ametris blog, GT9X Link FAQ. https://blog.ametris.com/blog/gt9x-link-faq-old (accessed 2026-10-11). **Primary.** New GT9X Link sales ended 2023-08-23.
21. ActiGraph GitHub repositories. https://github.com/actigraph/GT3X-File-Format ; https://github.com/actigraph/pygt3x (accessed 2026-10-11). **Primary.** Published `.gt3x` format and official readers.
22. ActiGraph CentrePoint Integration Guide. https://github.com/actigraph/CentrePointIntegrationGuide (accessed 2026-10-11). **Primary.** Analytics outputs, epoch lengths, daily-statistics webhook, continued V2 API support.
23. ProCare B.V. quotation 31576 to Palacký University Olomouc, 2025-07-17, with LEAP Instructions for Use (Rev 3), attached to a Czech contract-registry record. https://smlouvy.gov.cz/smlouva/soubor/42219929/ProCare_BV_FPC_UPOL__Scientific_accelerometers_II._priloha_Redigo.pdf (accessed 2026-10-11). **Secondary (public procurement record, scanned and OCR'd).**
24. Ametris privacy policy (last updated 2025-02-20). https://ametris.com/privacy-policy (accessed 2026-10-11). **Primary, legal.** Controller and processor roles, retention, participant request routing, AWS and Azure hosting, Data Privacy Framework.
25. Ametris Accelerant Partnership Program. https://ametris.com/partnerships (accessed 2026-10-11). **Primary.**
26. Highperformr company profile, ActiGraph. https://www.highperformr.ai/company/actigraph (accessed 2026-10-11). **Secondary, aggregator.** Only source for the 2023 SOC 2 Type II announcement.
27. Ametris academic product pages. https://academic.ametris.com/actigraph-leap ; https://academic.ametris.com/actilife ; https://academic.ametris.com/cpiw ; https://academic.ametris.com/actigraph-wgt3x-bt ; https://academic.ametris.com/grant-toolkit (accessed 2026-10-11). **Primary.** LEAP configurations and storage, ActiLife activation tiers and "legacy" label, wGT3X-BT legacy status, per-order pricing.
28. Ametris blog, LEAP FAQ. https://blog.ametris.com/blog/leap-faq (accessed 2026-10-11). **Primary.** LEAP is prescription use only for clinical research.
29. Ametris algorithm marketplace. https://ametris.com/algorithm-marketplace (accessed 2026-10-11). **Primary.**
30. ActiGraph Study Admin (V2) API documentation. https://github.com/actigraph/StudyAdminAPIDocumentation (accessed 2026-10-11). **Primary.** Unpublished daily request limit.
31. Ametris news, "Signant Health acquires Ametris to create an end-to-end eCOA and wearables platform." https://blog.ametris.com/news/signant-health-acquires-ametris-to-create-an-end-to-end-ecoa-and-wearables-platform (accessed 2026-10-11). **Primary (company release).** Roadmap kept; AI and machine learning named as a direction.
