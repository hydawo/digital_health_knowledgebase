# Emerging and Specialist Platforms

Platforms that materially belong in the Module 1 comparison but did not warrant a full profile in
this pass, either because they are narrower in scope, or because public documentation is too thin
to fill the template honestly. Each entry states what was established and what was not.

**Last verified: 2026-08-21; RingConn, Circular and Amazfit / Zepp section added 2026-10-09; Ultrahuman access, Biostrap (now Sensor Bio), Verily status and Zepp research partnerships re-checked 2026-10-10; Biostrap leg-placement claim qualified 2026-10-10. All six vendor entries (Ultrahuman, Sensor Bio, Verily, RingConn, Circular, Zepp) corrected against their vendor fact records 2026-10-22 (vendor fact record).** These entries close the discovery gap recorded in the first pass.

---

## Ultrahuman (Ring PRO and Ring AIR), the second ring with raw data

Corrected 2026-10-22 from the vendor fact record (`../../facts/ultrahuman.yaml`, judged 2026-10-21).

| Field | Detail | Confidence |
|---|---|---|
| Organization | Ultrahuman (India / UAE) |
| Product | **Ring PRO** (the US product) and **Ring AIR** (not sold in the US or Puerto Rico; see Status); **M1 CGM patch**; UltraSignal developer platform | **Verified** (store pages, 2026-10-21) |
| Status | Ring AIR is under a USITC limited exclusion order (337-TA-1398, Oura's patent, issued 21 August 2025; in effect from 21 October 2025 per Ultrahuman via TechRadar). CBP ruled on 6 March 2026 (HQ H354023) that the redesigned Ring PRO is not subject to the order, on condition of an importer certification. No API shutdown is announced | **Verified** (USITC notice, CBP ruling) |
| **Raw data** | **Raw PPG through the PPG Recordings API.** The account holder starts and stops sessions in the app's Developer Mode; files download as gzip-compressed NDJSON from pre-signed links that expire after 1 hour. The API returns only the token holder's own recordings, so a cohort needs per-participant accounts and manually started sessions. UltraSignal also names temperature and accelerometer streams for developer-kit holders, but no public endpoint documents raw temperature or accelerometer data. The daily metrics API returns processed values only | **Verified** (developer docs, `?api=ppg`, 2026-10-21) |
| Developer platform | **UltraSignal**, described as "the world's first wearable-based developer platform" | **Verified** |
| Access | Three developer routes plus an MCP server. **UltraSignal**: a short application; selected developers are loaned a developer kit (the page still offers a Ring AIR kit). **Personal API token**: self-serve in the developer portal (vision.ultrahuman.com/developer); reads the holder's own data, and another user's once that user enters the developer's Partner ID in the app. **Partner OAuth 2.0** (scopes `ring_data`, `cgm_data`, `profile`): registering an app is self-serve in the portal, but Ultrahuman's September 2025 guide still says "approved apps" with credentials from partner onboarding; whether production use needs approval is not documented. **MCP server**: read-only, OAuth 2.1, per user. OAuth token lifetime is stated two ways in the same docs, "valid for a week" and 86400 seconds (1 day); plan for 1 day. Rate limit 200 requests per minute on the PPG and blood-report APIs; each daily-metrics or PPG request spans at most 7 days | Personal token **Verified**; OAuth approval step **Corroborated** (2026-10-21) |
| Derived metrics | Daily metrics API: heart rate, HRV, skin temperature, steps, motion, resting HR, sleep (score, stages, efficiency and more), recovery and recovery index, movement index, VO2 max, SpO2, active minutes; with M1, glucose, metabolic score, variability, average glucose, estimated HbA1c and time in target. Workouts are not exposed | **Verified** (developer docs and Partner API guide) |
| Sampling rates | Raw PPG **typically 50 Hz**; each recording reports its own `sampling_rate_hz`. No rate or epoch is published for temperature, accelerometer, SpO2 or the daily-metric series | PPG **Verified**; others not public |
| Pricing | Ring PRO **USD 479**; Ring AIR USD 349 (global comparison page) or GBP 329 (UK). No subscription for ring data; optional add-ons, for example "Ultrahuman Max" at USD 29.97 for 3 months or USD 99.99 a year on the US store (re-checked 2026-10-30; was "from $9.99/mo"). Heroes pricing on Ring PRO covers scientists and researchers (discount not shown). No published API fee; the API Agreement says Sandbox and Production access are unpaid (Notion page, read by hand). Enterprise "dedicated subscription plans" are unpriced | Prices **Verified**; API fee **Reported** |
| Compliance and regulatory | Not a HIPAA covered entity but "strive[s] to comply"; footer claims ISO 27001, GDPR and HIPAA compliance. ISO 27001 certificate on request, none published; no BAA, DPA or SOC 2 offer published. No 510(k), De Novo or PMA; the only FDA listing is "Ultrahuman Fertile Window" (LHD, no clearance number). AFib Detection is not marketed in the US. Security incident notice dated 27 March 2026 (read-only access to an internal analytics system) | Self-claims **Corroborated**; FDA absence **Verified** |
| Validation | **No independent PSG or ECG validation located** | **Unclear** |

**Why it matters.** Ultrahuman documents a raw PPG route from a ring, at about 50 Hz. Oura's public
API does not offer one. If a study needs finger-PPG data, for custom pulse-wave analysis, or because a
ring is the only form factor a population will tolerate overnight, Ultrahuman is the clearest published
ring route found. The limit is scale, since the PPG Recordings API returns only the token holder's own
Developer Mode sessions. (The UltraSignal page title names Ring PRO while the body names Ring AIR.)

**Research program and academic data access.** No academic program with published terms. Three routes
(fact record, `research_program`, Verified). A "Research Institutions" offering on the partners page
(devices plus an enterprise dashboard) through a "Become a partner" form. **Pulsomics**, Ultrahuman's own
opt-in in-app study (CTRI/2026/08/115584), which invites universities, hospitals and research groups to
collaborate on study design, cohort access and co-authored papers, while raw recordings stay with
Ultrahuman's science team. And the developer routes above. The **API Agreement** (Notion page, read by
hand, Corroborated) says API data remains Ultrahuman's property with limited, revocable usage rights,
limits storage to what legitimate use needs, bars redistribution, and bars using API data "to conduct
research, analysis, or competitive studies against Ultrahuman", including re-deriving its metrics. Read
that clause before any validation or comparison study. Retention for consumers is "as long as
necessary", with de-identified data kept longer for research.

The **M1 CGM patch integration** makes Ultrahuman the only consumer ecosystem here combining ring
biometrics and continuous glucose in a single API. For metabolic research that is a genuinely
distinctive combination. **Reported.**

**Why to be cautious.** No independent validation was located. The raw PPG route covers only the
developer's own recordings, UltraSignal is selection-based with a loaner kit, daily-metric resolution
is unpublished, Ring AIR cannot be imported into the US, and the API Agreement restricts research
against Ultrahuman. Treat as promising and unproven.

Links: https://www.ultrahuman.com/us/ultrasignal/ · https://vision.ultrahuman.com/developer-docs?api=ppg · https://vision.ultrahuman.com/developer · https://www.ultrahuman.com/blog/accessing-the-ultrahuman-partnership-api/ · https://www.ultrahuman.com/us/partners/ · https://www.ultrahuman.com/us/pulsomics/ · support@ultrahuman.com

---

## Biostrap (now Sensor Bio), consumer company that pivoted to research

Corrected 2026-10-22 from the vendor fact record (`../../facts/sensor-bio.yaml`, judged 2026-10-21).

| Field | Detail | Confidence |
|---|---|---|
| Organization | Biostrap, now trading as **Sensor Bio** (sensorbio.com). Biostrap's home and research pages carry a banner, "Biostrap is now Sensor Bio", and the research page's demo link goes to sensorbio.com/get-started. Biostrap EVO and Kairos users are routed to Sensor Bio continuity pages; a CEO was named in February 2026 and the release refers to V2 and V3 devices (no V3 specification page found). Legal entity names differ across pages (Sensr Biotech, INC.; Sensr Biotech, LLC; Sensor Bio Inc., Austin, TX) | **Verified** (2026-10-21) |
| Products | Current: **Sensor Bio V2** band, three sensors (multi-wavelength PPG, three-axis accelerometer, skin temperature); a general wellness device, "not FDA cleared or approved". Legacy Biostrap kit, listed only on biostrap.com: EVO wrist device, **Activity Pod** (leg-worn), armband and chest-strap HRMs, and a **Thermo Patch** the legacy page calls FDA-cleared. No FDA record ties any clearance to Biostrap, Sensr or Sensor Bio, so the Thermo Patch claim is a legacy kit statement, not a Sensor Bio clearance | V2 **Verified**; Thermo Patch clearance **Unclear** (openFDA, no match, 2026-10-21) |
| **Raw data** | **V2**: raw PPG, IBI and accelerometer export at up to 100 Hz through the RPM dashboard (CSV or JSON, 1 to 7 day windows); the SDK live stream carries raw PPG, IBI, HR, HRV, respiratory rate, SNR and motion during active recording sessions. The REST raw-download endpoint is deprecated and works only for legacy **EVO** devices. **Gyroscope** applies to EVO only; the V2 specification lists none. Whether raw export needs an enterprise-tier account is a **conflict** on Sensor Bio's own pages: the V2 page says raw export is "gated to enterprise-tier accounts", the V2 vs Polar 360 comparison page says it is "the default data product for every partner, not a gated upsell" | V2 export **Verified**; tier gating **Conflict, Unclear** (2026-10-21) |
| **Configurable sampling** | V2 PPG **50 Hz by default, configurable to 25 or 100 Hz per organization**, up to 100 Hz raw export, configurable duty cycle; HR at 1-second resolution during active captures and 1-minute averages otherwise; HRV every 2 minutes overnight. HRV and respiratory rate need at least 50 Hz. A May 2026 Sensor Bio press release claims "15,000 samples per second" without naming a channel; that conflicts with the specification as written. For planning, 100 Hz is the documented ceiling | Specification **Verified**; 15,000 figure **Conflict, Unclear** |
| Study tooling | Customisable participant UX, enrolment workflows, **integrated behavioural health surveys**, educational widgets, automated reporting, compliance notifications; a Research Mode with data-access hierarchies, de-identified user IDs and de-identified downloads. All from the legacy biostrap.com research page; whether these carried over to V2 is not stated | **Verified** that the legacy page says so |
| Integration | Public REST API reference at **developers.sensorbio.com**, but not self-serve: an organisation administrator with the developer feature enabled creates keys, on request to developers@sensorbio.com. Mobile SDK (interface v0.17.0), documentation not public. Per-user OAuth2 availability is unclear (the API reference describes it; Sensor Bio's MCP server README says org API keys are the only supported method). Terra added a Sensor Bio integration in July 2026 and deprecated its Biostrap one | **Verified** (2026-10-21); OAuth2 **Unclear** |
| Validation claims | "14 publications and 22 clinical studies"; partners named include NIHMD (COVID-19), Regeneron (neuromuscular disease), UNLV Athletics; a registered validation trial for ejection fraction and cardiac output (NCT05279066) | **Reported**, vendor-compiled counts |
| Pricing | Not public. V2 "is sold through partnership, not checkout"; units, configuration and platform terms are scoped with a Sensor Bio contact. The $80 in a May 2026 press release is Sensor Bio's own hardware cost per unit, not a price to buyers. No academic pricing found | **Verified** that it is not published (2026-10-21) |
| Compliance claim | HIPAA claims appear only on legacy biostrap.com pages ("Research Platform (HIPAA Compliant)"); sensorbio.com, its privacy policy and terms make no HIPAA statement. No BAA, DPA, ISO 27001 or SOC 2 published. The privacy policy (effective 24 April 2025) still cites the EU-US Privacy Shield, invalidated in 2020 | HIPAA **Reported**; others not public |

**Why it matters.** Biostrap is one of the few platforms combining **raw PPG + configurable sampling
+ integrated surveys + a participant-management dashboard** in one product (the survey and Research Mode
features are documented only on the legacy Biostrap page). That combination, signal access *and* study operations *and* EMA, is otherwise only approached by Samsung's Research
Stack and Labfront. Biostrap explicitly repositioned from consumer to medical/research, unveiling a
next-generation device with raw sensor data at HLTH as part of that shift. **Reported.**

The legacy Biostrap multi-device framework (wrist + leg pod + chest strap + temperature patch; sensorbio.com does not list the pod or patch) is also unusual among
consumer-derived platforms. Leg placement itself is not unique: ActiGraph devices can be worn at the
ankle (see `ametris-actigraph.md`; Ngueleu et al. 2022, *J Neuroeng Rehabil*, PMC9575229, also
reports manufacturer guidance for the thigh), and Open Movement documents attaching the Axivity AX3 at
the thigh with tape or a bandage (see `axivity-geneactiv.md`). What Biostrap adds is vendor-computed
gait, balance and jump metrics from its leg pod, rather than raw accelerometry for the researcher to
process. (Qualified 2026-10-10.)

**Research program and academic data access.** No separate academic program. Sensor Bio markets
"Raw data access, IRB-friendly workflows, and reproducible signal quality for academic and research
studies", as a white-label platform with APIs. Access terms, user caps and pricing are not published;
contact sales (form or booked meeting) is the only entry point. Cloud retention is configured per
deployment with the partner; account deletion removes most data within 30 days and all of it within
90 days (privacy policy). **Verified** for these statements (2026-10-21).

**Why to be cautious.** Pricing is opaque, the published 100 Hz ceiling conflicts with a press claim of
15,000 samples per second, whether raw export is tier-gated is contradicted on Sensor Bio's own pages,
and two API timeseries endpoints were due to be discontinued on 30 September 2026. The company has
rebranded and its legal entity names differ across pages, validation counts are vendor-compiled, and
the most recent registered trial located dates from 2022. Company scale is much smaller than the
majors, which is a continuity risk for multi-year studies.

Links: https://sensorbio.com/ · https://sensorbio.com/product/sensor-bio-v2/ · https://developers.sensorbio.com · https://sensorbio.com/get-started/ · https://biostrap.com/research/ · https://biostrap.com/science/ · https://biostrap.com/validation/ · https://biostrap.com/rpm/

---

## Verily Study Watch, the clinical-research-only wearable

Corrected 2026-10-22 from the vendor fact record (`../../facts/verily.yaml`, judged 2026-10-22).

| Field | Detail | Confidence |
|---|---|---|
| Organization | Verily (Alphabet) |
| Status | **Conflict.** In use across clinical trials since 2017. Press quoting an August 2025 internal memo from Verily's CEO (MD+DI) and a spokesperson (HIT Consultant) reports that Verily fully wound down its devices program, including "Study Devices", and will no longer support its devices; every Study Watch product page is gone (404 on 2026-10-22). Against that, Verily's Security and Trust page still lists "Study Watch & Hub" in its SOC 2 and ISO 27001 scope, and a third party, Quipment Inc., registered as a repack or relabel establishment, added an FDA device listing for Study Watch (K182456) on 2026-05-12. The memo does not name Study Watch, and Verily has published no Study Watch end-of-life notice | **Conflict, Reported** (2026-10-22; was Unclear 2026-10-10) |
| Availability | **Never sold for consumer use**, a clinical research tool only ("not directly available to consumers", "an investigational device") | **Corroborated** |
| **Data streams** | Records **ECG, heart rate, electrodermal activity (EDA), and inertial movement**, plus **PPG at 30 Hz** and **accelerometry at 30 Hz** (Verily-co-authored Project Baseline paper, PMC11699500) and environmental sensors | **Corroborated** |
| **Raw data** | Reported at launch to **store up to a week's worth of raw data** on the device (MassDevice, 2017; Verily's own 2017 launch post is gone). Outside researchers get Study Watch data only as de-identified Project Baseline Health Study (PBHS) data on approved request; whether raw PPG reaches them is not stated (the PBHS paper used derived inter-beat intervals) | **Corroborated** |
| Regulatory | Three FDA 510(k) clearances, product code DXH, all to Verily Life Sciences: **K182456** Study Watch, single-lead ECG (2019-01-17); **K192415** Study Watch with Irregular Pulse Monitor (2020-01-17); **K213357** Study Watch with Irregular Pulse Monitor (Home) (2022-07-19). No registration listing under Verily; no GUDID record. A clearance is not evidence of current supply. MD+DI reports FDA denied a 2021 bid to add a Parkinson's exam tool (no FDA record looked up) | 510(k)s **Verified** (FDA database, 2026-10-22); Parkinson's denial **Reported** |
| Platform | Verily **Pre** (Exchange data catalogue plus **Workbench** trusted research environment); **Viewpoint Evidence** for sponsors, which since March 2026 bundles Samsung Galaxy Watch 8 data | **Verified** |
| Pricing / access | **Workbench Standard is free and self-serve** for anyone with a Google account, labelled **beta**; capped at 5 workspaces and 5 collaborators per workspace; a Data Use Agreement per data collection, including the PBHS Limited collection; compute is billed to the researcher's own cloud account. Workbench Professional is paid, with no published price. Viewpoint is by demo request. No academic pricing or minimum commitment published. No device list price was found | **Verified** (Workbench docs and upgrade page, 2026-10-22) |
| Compliance | Verily claims SOC 2 Type II and ISO/IEC 27001 covering Study Watch & Hub and Workbench, among other products (Coalfire seal on the page; reports may need an NDA). HIPAA audits are claimed for other products, not Study Watch, Workbench or Viewpoint. Verily says it acts as a business associate for research sponsors when HIPAA applies. Two Verily entities are listed Active on the Data Privacy Framework registry | SOC 2, ISO 27001, BAA **Corroborated**; DPF **Verified** |

**Why it matters.** Study Watch records **EDA alongside ECG**. Empatica has EDA without ECG. Corrected
2026-10-10: Samsung Galaxy Watch8 and later also expose both through the Health Sensor SDK (raw EDA at
1 Hz and on-demand raw ECG at 500 Hz; see `samsung.md`). Up to a week of onboard raw storage (2017
press) plus three FDA clearances put it in the regulated-research tier on paper, but with the device
program wound down it cannot be recommended as a procurable research device. Its value now is the
historical Project Baseline data.

### The March 2026 Verily, Samsung collaboration, significant for Module 1

Verily and Samsung Electronics America announced a collaboration bringing **Galaxy Watch 8** data
into Verily's **Pre** platform, with sensor data surfaced in **Viewpoint Evidence**. Verily's own
release says only that it will "fully integrate sensor data" and lists no streams, rates or raw-signal
terms. Verily's chief product officer told MedCity News (March 2026) that researchers get **raw device
signals, such as photoplethysmography and motion from the accelerometers and gyroscopes**. That is a
journalist's paraphrase, so **Reported** (corrected 2026-10-22 from Corroborated).

If Verily confirms it, this is consistent with the Samsung raw-signal capability documented in
`samsung.md`, and it would be a **third access route** to Galaxy Watch raw data alongside the Samsung
Health Sensor SDK (formerly the Privileged Health SDK) and the open-source Research Stack, this one
packaged for pharmaceutical clinical trials rather than academic self-build. Which streams and rates
Viewpoint delivers is a question for Verily.

**Why to be cautious for academic use.** There is no self-serve route to the device or to Viewpoint.
Verily sells Viewpoint to life sciences and government sponsors, paid tiers are unpriced, and Study
Watch was never available for purchase. The exception is Workbench Standard, a free self-serve beta
tier for analysing Exchange data collections such as PBHS Limited under a DUA; whether that collection
includes Study Watch sensor data, and over what dates, is not stated.

Links: https://verily.com/ · https://verily.com/newsroom/verily-and-samsung-collaborate-to-accelerate-clinical-research-with-the-galaxy-watch-and-pre-platform · https://support.workbench.verily.com/docs/guides/admin/licensing_tiers/ · https://verily.com/security-trust · https://clinicaltrials.gov/study/NCT06041373

---

## RingConn, Circular and Amazfit / Zepp, data-access check (2026-10-09)

A desk check of primary sources for whether any of these offers researchers a data route beyond the consumer app, corrected 2026-10-22 against each vendor's fact record (`../../facts/ringconn.yaml`, judged 2026-10-21; `../../facts/circular.yaml` and `../../facts/zepp-amazfit.yaml`, judged 2026-10-22). None publishes a self-serve research API. **Circular** publishes a research partnership offer (devices, raw signal access under agreement and engineering time) and an API and SDK for selected business projects, by contact. **Zepp** documents a legacy cloud OAuth 2.0 partner API (the Huami/Zepp Open Platform) to which institutions can apply; whether it still takes new partners is unclear. Zepp Health also advertises research partnerships on its "Data analytics" page (zepp.com/data-analytics), citing "partnerships with 20 independent research laboratories, hospitals, pharmaceutical companies and universities" at the end of 2020 and 42 million active users in the first half of 2021, but that page states no data-access terms. **RingConn** publishes no research programme; its only institutional route is business@ringconn.com, and an earlier "Educational and Government Partnerships" invitation on that page was removed in its 17 October 2026 rewrite.

| Platform | What is documented | Research data access | Confidence |
|---|---|---|---|
| **RingConn** (Ninenovo) | Syncs to Health Connect on Android 9 and later since Google Fit sync ended on 1 October 2025 (RingConn blog, 7 August 2025); HRV is not synced there ("algorithm compatibility issue"). Apple Health sync is confirmed on RingConn's own sync guide, HealthKit types not listed. Company-run studies with Shanghai Jiao Tong University and hospitals, including a 2026 *npj Digital Medicine* paper on bilateral ring PPG (DOI 10.1038/s41746-026-03036-z). FDA 510(k) **K260490**, "Ninenovo Blood Oxygen Ring" (SpO2, product code DQA), cleared 2026-10-02 to Shenzhen Ninenovo; no source links the cleared models to a consumer ring, and the Gen 3 page says "This product is not a medical device". US supply continues under a multi-year, royalty-bearing Oura patent licence announced October 2025 (length not public). US prices Gen 3 $349, Gen 2 $299, Gen 2 Air $199; no subscription required (an optional "RingConn Partner+" in-app purchase has undocumented contents). | No public developer API, SDK or research programme. Institutional proposals go to business@ringconn.com (bulk orders sales@ringconn.com). Public routes (Health Connect, Apple Health, portability requests) carry processed records, not raw PPG. One company-involved 2026 paper (BMC Sports Science, Medicine and Rehabilitation, DOI 10.1186/s13102-026-01960-x) used raw 100 Hz green-channel PPG from a Gen 2 through firmware customised for research export; three authors are company staff. OpenCircuit, a community reverse-engineered BLE client, now runs on Gen 2 and Gen 3 with no RingConn account, under a non-commercial licence; it is still not a supportable research route. | No API: **Verified** absence (fact record). Health Connect and Apple Health sync: **Verified**. Raw PPG via research firmware: **Reported** (single paper, conflict of interest). FDA clearance: **Verified**. |
| **Circular** (Circular Ring 2) | Ring 2 sensors per the science page: PPG (green, red, infrared) 25 Hz, single-lead ECG 510 Hz (40 s recordings), skin temperature 1 Hz at 0.01 °C, accelerometer 25 Hz. **No FDA record for Circular**; its terms state the ring and the app are not medical devices. CES 2025 press (Wareable) called the AFib detection FDA-cleared through a partner's algorithm ("B-Heart"); any such clearance would belong to the partner's software, and nothing confirms which company or 510(k). **Company status**: the original operator, Circular SAS, was converted to judicial liquidation on 14 October 2025 (societe.com, secondary); the current terms name Circular Health Limited (Paris trade register 990 900 326), and the founders told press the headquarters moved to Hong Kong. **Blood pressure and glucose claims contradict each other**: the science page says Circular does not infer blood glucose or blood pressure from optical data, yet the BP page offers cuff-calibrated BP estimates claiming medical-grade accuracy (no study cited) and release notes add glucose-monitoring compatibility; treat both as unvalidated vendor estimates. Price conflict: $349 on the store product page, $299 on the shop page. Ring 3 pre-orders December 2026. | **Research partnerships** for clinical, academic and enterprise partners ("Bring us a protocol"): devices, raw signal access under agreement and engineering time; no terms, cost or format published. **API and SDK** on the Professional track, by contact, "limited to selected projects"; no public documentation. **Free team dashboard** (dashboard.circular.care) with CSV export of any metric, daily and historical; business orders from 25 rings, by quote. **App sync** of intraday values (temperature, SpO2, breathing rate), HRV and sport sessions to Apple Health and Health Connect (processed, not waveforms). Firmware 1.7.2 (12 October 2026) mentions an undocumented "Research mode". Whether agreements signed with the old entity carry over is not published. | Research offer, API by contact, dashboard CSV and health-store sync: **Verified** (circular.xyz, 2026-10-22). Raw signal access: **Corroborated** (no format published). Company status: **Unclear** (secondary sources). FDA: no record, **Verified**. Contact support@circular.xyz. |
| **Amazfit / Zepp Health** | Zepp OS developer framework (docs.zepp.com) for on-watch Mini Programs. The device-app API exposes an `Accelerometer` (x, y, z in cm/s², from API level 3.0, with `FREQ_MODE_LOW`, `FREQ_MODE_NORMAL` and `FREQ_MODE_HIGH` and no Hz values published), a `Gyroscope` with the same pattern, `HeartRate` as bpm values plus a per-minute array for the current day, and `BloodOxygen` as SpO2 results. Apps can be side-loaded or published through the Zepp store's review. developer.zepp.com/os/home now returns quotable text (2026-10-22). **No FDA clearance** for any Amazfit watch feature; FDA listings only (Amazfit Balance under PUH, body composition, and Zepp Clarity hearing aids under QUG, both 510(k)-exempt). Zepp's privacy policy states ISO/IEC 27001:2022 and 27701:2019 certificates (IS 743462, PM 743467), certifying body and renewal year not stated. US prices from about $99.99 (Active 2, Helio Strap); core features need no subscription, Zepp Aura Premium is optional. | **Zepp OS on-watch API**: no raw PPG or ECG waveform API; accelerometer and gyroscope need a custom watch app. **Legacy Huami/Zepp Open Platform**: an OAuth 2.0 cloud Web API (api-open.huami.com) for corporate partners; a PhD researcher must apply in the institution's name, through dev.huami.com, with a 3 to 7 day review (contacts developer@zepp.com, datapartner@huami.com). Its docs (2017 to 2020) list raw ECG at 250 samples per second, per-minute raw motion data and user-tagged sensor files with a PPG CSV example. The API hosts still answer (2026-10-22), but the docs were last edited in 2020, a 2022 applicant reported the old platform deprecated, and a 2021 applicant reported Zepp said API access must be paid for. Third-party aggregators offer normalised summaries: Terra lists "Activity, Daily and Sleep" data types for Zepp, "normalized by the Terra unified API", polled every 5 to 10 minutes because Zepp does not notify Terra of changes (tryterra.co/integrations/zepp, 2026-10-10). Thryve's Zepp page is live at thryve.health/supported-wearable-devices/zepp-amazfit (2026-10-22); the URL cited earlier returned 404 on 2026-10-10. The Zepp app also writes 26 data types to Health Connect (since January 2025) and links to Apple Health. Unofficial reverse-engineered cloud access exists and is not a supportable research route. | On-device sensor API: **Verified** from docs.zepp.com (rates still unpublished). Legacy partner cloud API exists: **Corroborated**. Open to new partners: **Unclear**. Raw streams in the legacy API: **Reported** (docs years old). Fee: **Reported**. Accelerometer rate per mode: **Unclear**. Research partnerships: vendor page, figures from 2020 to 2021. |

**Bottom line.** None of the three offers a self-serve research API in the sense Ultrahuman (PPG Recordings API) or Samsung (Health Sensor SDK) now do. Circular comes closest on paper, with raw signal under a research agreement, an API and SDK for selected projects and a free CSV dashboard, but its terms are unpublished and its operating company changed after a 2025 liquidation. Zepp has a documented but aging partner cloud API whose open status and fee only Zepp can confirm, plus an on-device route to motion sensors that requires building a watch app. RingConn has no route beyond OS health stores, apart from one company-run research firmware build. For most studies the realistic routes remain OS health stores (Health Connect, Apple Health) or an aggregator, at summary-metric resolution.

---

## Not investigated in this pass

Recorded so their absence remains a known gap rather than an implied judgement.

| Technology | Note |
|---|---|
| **Samsung Galaxy Ring (as a distinct research target)** | Smart ring with no separate research data pathway assessed beyond the Samsung profile. Samsung's docs confirm only a processed route through the phone-side Data SDK and no raw route (`../../facts/samsung.yaml`, 2026-10-11). RingConn and Circular were checked on 2026-10-09 and corrected against their fact records on 2026-10-22; see the section above |
| **Whoop 5.0 vs 4.0** | Whether the Schyvens 2025 result on the 4.0 transfers to current hardware is unknown |
| **Activinsights / GENEActiv production status** | Checked 2026-10-09: still sold by quote, product page republished January 2026, no discontinuation notice. Manufacturing status and lead times not public. See `axivity-geneactiv.md` |
| **Open Movement project maintenance** | Checked 2026-10-09: repository active (last push 2026-08-18), OmGui last released 2022-10-31 (v45), AX3 firmware V50, AX6 firmware V56. See `axivity-geneactiv.md` |
| **Muse, Dreem and EEG wearables** | Deliberately deferred as a distinct modality |
| **Dexcom, Abbott and CGM generally** | Deliberately deferred to a connected-medical-devices module. Note that both Labfront and Ultrahuman now integrate CGM with wearables, so this boundary is eroding |

---

## Where these platforms change the Module 1 conclusions

1. **"Only Samsung, Polar, Withings and Empatica expose raw signal" was wrong.** Add **Ultrahuman**
   (raw ring PPG through the PPG Recordings API, typically 50 Hz, own recordings only), **Biostrap / Sensor Bio** (raw PPG, IBI and accelerometer at up to 100 Hz on V2, per the vendor), **Movesense** (512 Hz ECG,
   1.6 kHz IMU), **Verily** (ECG, EDA, PPG and inertial, up to a week of onboard raw per 2017 press; device program wound down in 2025), and **Garmin** (raw accel
   via SDK, BBI via cloud API).
2. **A ring with a documented raw PPG route now exists** (Ultrahuman PPG Recordings API), and Circular offers raw ring signal under a research agreement. Oura's closed-data position is a vendor choice, not a
   constraint of the form factor.
3. **The raw-data tier is no longer synonymous with expensive.** Polar ($104.95 for the H10 or Verity Sense, Polar US store, 2026-10-10) and Movesense sit
   alongside Empatica (~$1,750/3 yr) and Ametris.
4. **Verily, Samsung may give Galaxy Watch raw signal a commercial clinical-trial route**, not
   just a self-build one. Reported only, from a press paraphrase of Verily's chief product officer;
   Verily's own release lists no streams.

## Vendor Fact Record

### Ultrahuman

<!-- facts:begin ultrahuman -->
*Generated from the fact record by `tools/facts/generate.py`. Edit the record, not this block.*

**Research access**

| Fact | Value |
|---|---|
| Formal research or academic program (name, what it offers) | No dedicated academic data program with published terms. Three routes: (1) research partnerships, a "Research Institutions" offering on the partners page (devices plus an enterprise dashboard) reached through a "Become a partner" form; (2) Pulsomics, Ultrahuman's own opt-in in-app research program, registered with CTRI, which invites universities, hospitals and research groups to collaborate on study design, cohort access and co-authored papers while keeping the raw recordings with the Ultrahuman science team; (3) UltraSignal, an application-based developer platform with a loaned developer kit for PPG, temperature and accelerometer streams. [V, 2026-10-21] |
| Who can join the research program | UltraSignal: open application; priority goes to applicants building an app on Ring AIR data. Pulsomics collaboration: universities, hospitals and research groups, no further criteria. Pulsomics participants: anyone 18 or over actively using a Ring AIR or Ring PRO. Partnerships: no eligibility criteria published. [V, 2026-10-21] |
| How to apply, and any approval or review step | UltraSignal: a brief application (Typeform linked from the page); applications are reviewed and selected applicants are loaned a developer kit. Personal API tokens and OAuth app registration: created by the account holder in the developer portal (see developer_program_status). Ultrahuman's September 2025 Partner API guide lists the OAuth client ID and secret as coming from "partner onboarding". Research partnerships and Pulsomics collaboration: a "Become a partner" / "Partner with us" contact route, with no criteria, review step or timeline published. Pulsomics participants opt in inside the app. [V, 2026-10-21] |
| Whether the program is active, paused, renamed or closed | All three routes are live as of 2026-10-21. Pulsomics is new in 2026 (CTRI/2026/08/115584; three studies open, two marked coming soon). The UltraSignal page is up, its title names Ring PRO, and its body still offers a Ring AIR developer kit, although Ring AIR is no longer sold in the US. [V, 2026-10-21] |
| Whether the general developer or API program is open to new applicants | **Personal API token:** Open and self-serve. Any Ultrahuman account holder can generate a Personal API token in the developer portal (vision.ultrahuman.com/developer, sign-in required). The token reads the holder's own data, and another user's data once that user links their account by entering the developer's data sharing code (Partner ID) in the app. No approval step is described for this route. [V, 2026-10-21]<br>**Partner OAuth API:** Open, with an unclear approval step. The developer portal lets a signed-in account holder create an OAuth application, and Open Wearables' setup guide walks through doing so without any review. Ultrahuman's own Partner API guide (19 September 2025) still says "approved apps" with credentials from "partner onboarding", and an Open Wearables blog post (May 2026) says credentials are not self-serve. Reading the exact wording together: registering an app is self-serve today; whether an app needs Ultrahuman's approval before users outside the developer's own account can authorise it, or before production use, is not documented. [C, 2026-10-21] |
| Participant or user limits before approval or by tier | Not public [2026-10-21] |
| How academic access differs from commercial or consumer access | Unclear |

**Pricing**

| Fact | Value |
|---|---|
| Device or hardware list price | **Ring PRO:** USD 479 including the PRO charging case, on the US and global storefronts. Prices are set per regional store. [V, 2026-10-21]<br>**Ring AIR:** USD 349 on the global PRO-versus-AIR comparison page; GBP 329 list on the UK store. Not sold in the US or Puerto Rico (see deprecations). [V, 2026-10-21] |
| Consumer subscription or membership price | None for ring data. Optional paid add-ons are priced per store, for example the Cardio Adaptability PowerPlug (USD 2.9/month) and, on the US store, the "Ultrahuman Max" bundle at USD 29.97 for 3 months or USD 99.99 a year (all premium PowerPlugs, Jade Pro, UltrahumanX and member pricing). CGM plans are also separate. [V, 2026-10-30] |
| Research or academic pricing or discount | Heroes special pricing on Ring PRO covers scientists and researchers (plus healthcare workers, athletes, veterans and military, and education); proof of eligibility may be required. The discount is not shown. No institutional, bulk or study-volume research pricing is published. [V, 2026-10-21] |
| Fees for API, SDK, platform or data access | No published fee for API access. The API Agreement says Sandbox and Production access are unpaid and as-is, offers a paid Premium Access support tier (price not published), and requires 30 days' notice before fees are introduced. The developer docs mention enterprise "dedicated subscription plans" (price not published). [R, 2026-10-21] |
| Minimum order, term or commitment | Not public [2026-10-21] |
| Whether pricing requires contacting sales | Consumer ring and add-on prices are published per store. Research partnership, enterprise dashboard and UltraWork bulk pricing is not published; those routes go through "Become a partner" and "Request access" forms. [C, 2026-10-21] |

**Data access and terms**

| Fact | Value |
|---|---|
| Raw signals available to researchers, and by which route | Raw PPG, through the PPG Recordings API: sessions the account holder starts and stops in the app's Developer Mode, downloaded as gzip-compressed NDJSON from pre-signed links. The API returns only the token holder's own recordings, so it does not reach a participant cohort without per-participant accounts and manual sessions. UltraSignal also names temperature and accelerometer streams for developer-kit holders, but no public endpoint documents raw temperature or accelerometer data. The daily metrics API returns processed values only. [V, 2026-10-21] |
| Derived or processed metrics available to researchers | Daily metrics API: heart rate, skin temperature, HRV, steps, motion, night and sleep resting HR, sleep (score, total, efficiency, time in bed, REM/deep/light, temperature deviation, HR drop, restorative sleep, movements, morning alertness, full cycles, tosses and turns, average body temperature), recovery and recovery index, movement index, VO2 max, SpO2, active minutes; with CGM: glucose, metabolic score, glucose variability, average glucose, estimated HbA1c, time in target. Separate endpoints cover Home environment metrics and Blood Vision reports. Workouts are not exposed. [V, 2026-10-21] |
| Documented sampling rates or temporal resolution | **Raw PPG recordings:** Typically 50 Hz, returned per recording as sampling_rate_hz. [V, 2026-10-21]<br>**Daily metrics and other sensors:** Not public [2026-10-21] |
| How far back data can be retrieved | Unclear |
| Export, API, SDK or file routes | (1) REST API at partner.ultrahuman.com (daily metrics, Home metrics, PPG recordings, blood test reports and details) with a Personal API token; another user's data needs their email and their entering the developer's code under Partner ID in the app. (2) Partner OAuth 2.0 API (scopes ring_data, cgm_data, profile). (3) Raw PPG files as pre-signed download URLs that expire after 1 hour. (4) A read-only MCP server (OAuth 2.1, per user). (5) App sync to Apple Health, Google Fit and other apps. Aggregators Terra and Open Wearables integrate Ultrahuman. No in-app CSV export was found. OAuth access-token lifetime is stated inconsistently: "valid for a week" and, in the next lines, 86400 seconds (1 day). [V, 2026-10-21] |
| API rate limits | 200 requests per minute, documented as the 429 error for the PPG Recordings and blood report APIs; the MCP server uses a cost-weighted per-user budget returning HTTP 429 with Retry-After. No numeric limit is published for the daily metrics or OAuth endpoints. Per-request windows: 7 days for daily metrics and PPG, 365 days for blood reports. [V, 2026-10-21] |
| Terms on retaining, storing or deleting data | Ultrahuman keeps personal data only as long as necessary or legally required, but may keep de-identified data longer for research and statistics. For API partners, the API Agreement limits storage to what is necessary for legitimate use, says all API data remains Ultrahuman's property with only limited, revocable usage rights for the partner, bars redistribution, and requires breach notice within 36 hours. Raw PPG download links expire after 1 hour. [C, 2026-10-21] |
| Terms on using data to train AI or ML models | Ultrahuman's side: the privacy policy lists developing machine learning algorithms "with your consent", the terms of use allow user information to be used for "analysis, research, training", and Pulsomics pools opted-in raw pulse data to build models. Partner side: the API Agreement has no clause on training AI or ML models, but bars using API data for research or analysis against Ultrahuman and reverse-engineering its algorithms or metrics. [C, 2026-10-21] |
| Announced shutdowns, deprecations or migrations, with dates | No API shutdown or migration is announced. Hardware: Ring AIR is no longer sold in the US or Puerto Rico. The USITC issued a limited exclusion order in 337-TA-1398 (Oura's '178 patent) on 21 August 2025, which took effect after Presidential review on 21 October 2025; Ring AIR cannot be imported, and retailers may sell existing stock. On 6 March 2026 CBP ruled (HQ H354023) that the redesigned Ring PRO is not subject to the order, so Ring PRO is the US product. The API Agreement promises at least 30 days' notice of significant API changes. [V, 2026-10-21] |

**Compliance and regulatory**

| Fact | Value |
|---|---|
| Whether a HIPAA Business Associate Agreement is offered | Not public [2026-10-21] |
| Whether a data processing agreement is offered | Not public [2026-10-21] |
| Published HIPAA statement | Privacy policy: Ultrahuman is not a HIPAA covered entity, but "strive[s] to comply" with HIPAA for US customers' health data. The site footer separately claims "ISO27001, GDPR, and HIPAA compliant." No attestation or audit is published. [C, 2026-10-21] |
| Published GDPR statement | Claims compliance with UK and EU GDPR and names an outsourced EEA/UK Data Protection Officer (Ametros Group Ltd). Privacy policy last updated 13 September 2026. [C, 2026-10-21] |
| ISO/IEC 27001 status and evidence | Claims ISO 27001 certification, with the certificate available on request. No certificate, number, scope or certification body is published, and no registry entry was found. [C, 2026-10-21] |
| SOC 2 status and evidence | Not public [2026-10-21] |
| FDA clearances, from the FDA database | Not public [2026-10-21] |
| Where data is stored, and residency options | Stored with AWS, Snowflake and MongoDB Atlas in the United States, and may be processed in any country where Ultrahuman or its affiliates operate. No residency choice is offered. Ultrahuman Healthcare Private Limited is an Indian company, and the API Agreement is governed by Indian law with Bengaluru courts. [C, 2026-10-21] |

<!-- facts:end -->

### Sensor Bio

<!-- facts:begin sensor-bio -->
*Generated from the fact record by `tools/facts/generate.py`. Edit the record, not this block.*

**Research access**

| Fact | Value |
|---|---|
| Formal research or academic program (name, what it offers) | No named academic program. Research is one of the marketed segments of the Sensor Bio B2B platform (raw data access, IRB-friendly workflows). The legacy Biostrap research page, still live under a "Biostrap is now Sensor Bio" banner, describes a Research Mode in the RPM dashboard with data access hierarchies, de-identified user IDs and de-identified downloads. [V, 2026-10-21] |
| Who can join the research program | Aimed at IRB-approved studies, institutional deployments and population-level programs. No eligibility criteria are published. [V, 2026-10-21] |
| How to apply, and any approval or review step | Contact sales: a form or a booked meeting on the Get Started page. A Sensor Bio contact scopes units, configuration and platform terms. No application form, review step or timeline is published. [V, 2026-10-21] |
| Whether the program is active, paused, renamed or closed | Active under the Sensor Bio name. Biostrap (founded 2016) renamed itself Sensor Bio; Biostrap EVO and Kairos users are routed to Sensor Bio through continuity pages. Bruce Smith was named CEO in February 2026, and the CEO release refers to V2 and V3 devices. [V, 2026-10-21] |
| Whether the general developer or API program is open to new applicants | A public REST API reference (Sensor Bio Developers API) is online, but it is not self-serve: API keys are created in the web dashboard by an organisation administrator whose account has the developer feature enabled, on request to developers@sensorbio.com. Mobile SDK keys are issued the same way and the Mobile SDK documentation is not public. OAuth2 per-user access is unclear: the API reference describes an OAuth2 Bearer token with in-browser user consent, while Sensor Bio's own MCP server README (repository last pushed 2026-02-19) says the auth server does not support the authorization_code grant for external OAuth2 apps. [V, 2026-10-21] |
| Participant or user limits before approval or by tier | Not public [2026-10-21] |
| How academic access differs from commercial or consumer access | Not public [2026-10-21] |

**Pricing**

| Fact | Value |
|---|---|
| Device or hardware list price | Not public [2026-10-21] |
| Consumer subscription or membership price | Not public [2026-10-21] |
| Research or academic pricing or discount | Not public [2026-10-21] |
| Fees for API, SDK, platform or data access | Not public [2026-10-21] |
| Minimum order, term or commitment | Not public [2026-10-21] |
| Whether pricing requires contacting sales | Yes. V2 is sold only through partnership; units, configuration and platform terms are scoped with a Sensor Bio contact. No list prices. [V, 2026-10-21] |

**Data access and terms**

| Fact | Value |
|---|---|
| Raw signals available to researchers, and by which route | **Sensor Bio V2:** Three sensors: multi-wavelength PPG (green, red, infrared), a three-axis accelerometer and skin temperature. No gyroscope is listed. Raw PPG, inter-beat intervals and accelerometer export at up to 100 Hz through the RPM dashboard; the SDK live stream carries raw PPG, IBI, HR, HRV, respiratory rate, SNR and motion during active recording sessions. The REST API raw-download endpoint does not support V2 ("planned for a future release"). [V, 2026-10-21]<br>**Sensor Bio V2, who can get raw export:** Sensor Bio's pages disagree on whether raw export is tier-gated. The V2 specification page says raw export is "gated to enterprise-tier accounts". The Sensor Bio V2 vs Polar 360 comparison page says raw waveform export is "the default data product for every partner, not a gated upsell", and, in the same SDK paragraph where the specification page has its enterprise-tier sentence, says "No separate license. No gated tier." (conflict) [U, 2026-10-21]<br>**Biostrap EVO (legacy):** Raw PPG, accelerometer and gyroscope through the RPM dashboard and through the deprecated asynchronous REST raw-download endpoint (zipped archive, emailed link valid 5 hours, at most 10 users and 1 week per request), which still works only for EVO devices. [V, 2026-10-21] |
| Derived or processed metrics available to researchers | **Sensor Bio V2:** Heart rate, HRV (rMSSD, HRV-CV, LF/HF; SDNN and SD1/SD2 on spot checks), respiratory rate, skin temperature deviation, steps, calories, activity score, recovery score, sleep stages (REM, deep, light, awake) and sleep, circadian score and sleep debt, workouts, stress index and ANS balance. Available through the SDK, the REST API and the RPM dashboard. HRV and respiratory rate need at least 50 Hz PPG sampling. SpO2 on V2 is announced but not live. [V, 2026-10-21] |
| Documented sampling rates or temporal resolution | **Sensor Bio V2:** The V2 specification: PPG sampling 50 Hz by default, configurable to 25 or 100 Hz per organization, with up to 100 Hz raw export and a configurable duty cycle; HR at 1-second resolution during active captures and 1-minute averages otherwise; HRV sampled every 2 minutes overnight. Sensor Bio's May 2026 AHA press release says the platform "captures raw physiological signals at 15,000 samples per second". The press wording names no channel, sensor or aggregate, so it cannot be read as a different measure from the text; the two vendor statements conflict as written. (conflict) [U, 2026-10-21] |
| How far back data can be retrieved | **Sensor Bio V2:** Cloud history is retained per deployment as configured with the partner; API queries cannot go back before the user's account creation. Per-request windows: raw export 1 to 7 days and computed metrics 1 to 30 days in the dashboard; at most 6 hours per API timeseries call. The band buffers about 14 days at default sampling, overwriting the oldest data. [V, 2026-10-21] |
| Export, API, SDK or file routes | RPM web dashboard export (CSV or JSON, up to 2 GB per file; raw 1 to 7 day windows, computed 1 to 30 day windows); REST API with an Organization API Key (server-to-server) or a per-user OAuth2 token (availability unclear); a mobile SDK (interface v0.17.0) with BLE live stream; participant self-download of account data. Terra added a Sensor Bio integration in July 2026 and marked its Biostrap integration deprecated. [V, 2026-10-21] |
| API rate limits | Not public [2026-10-21] |
| Terms on retaining, storing or deleting data | For partners, retention is configured per deployment. For account holders, deletion removes most data within 30 days and all data, including backups, within up to 90 days. No published research-data retention terms. [V, 2026-10-21] |
| Terms on using data to train AI or ML models | Not public [2026-10-21] |
| Announced shutdowns, deprecations or migrations, with dates | API: the continuous-mode biometrics timeseries and normalized activity timeseries endpoints were to be discontinued on 30 September 2026; the raw-download endpoint is deprecated and works only for legacy EVO devices (V1/V2 support "planned for a future release"); several other EVO-only endpoints are deprecated. The old api.getsensr.io and auth.getsensr.io hostnames were to stop working after 30 September 2026 (read 2026-10-11; that text has since been removed). Brand: Biostrap renamed Sensor Bio, with EVO and Kairos continuity pages; Terra marked its Biostrap integration deprecated in July 2026. [V, 2026-10-21] |

**Compliance and regulatory**

| Fact | Value |
|---|---|
| Whether a HIPAA Business Associate Agreement is offered | Not public [2026-10-21] |
| Whether a data processing agreement is offered | Not public [2026-10-21] |
| Published HIPAA statement | **Legacy Biostrap pages (biostrap.com):** HIPAA-compliant research and RPM platform, claimed only on the legacy biostrap.com pages. The current sensorbio.com site, privacy policy and terms make no HIPAA statement. [R, 2026-10-21] |
| Published GDPR statement | The privacy policy (effective 24 April 2025) asks GDPR-covered users for explicit consent to process health data, lists legal bases and names a Data Protection Officer at support@sensorbio.com. For EU-US transfers it still relies on consent and the EU-US and Swiss-US Privacy Shield, a framework the EU Court of Justice invalidated in July 2020. [C, 2026-10-21] |
| ISO/IEC 27001 status and evidence | Not public [2026-10-21] |
| SOC 2 status and evidence | Not public [2026-10-21] |
| FDA clearances, from the FDA database | Not public [2026-10-21] |
| Where data is stored, and residency options | Sensor Bio cloud platform hosted on AWS; data is transferred to the United States and other countries. No region or residency option is published. [V, 2026-10-21] |

<!-- facts:end -->

### Verily

<!-- facts:begin verily -->
*Generated from the fact record by `tools/facts/generate.py`. Edit the record, not this block.*

**Research access**

| Fact | Value |
|---|---|
| Formal research or academic program (name, what it offers) | Verily no longer markets a Study Watch research program. What it offers researchers now is Verily Pre (Exchange data catalogue plus Workbench trusted research environment), with a free self-serve Standard tier for individual researchers, and, for study sponsors, Viewpoint Evidence, which since March 2026 bundles Samsung Galaxy Watch 8 sensor data with Verily's registry cohorts. [V, 2026-10-22] |
| Who can join the research program | **Verily Pre Workbench and Viewpoint Evidence:** Workbench individual accounts are open to anyone with a Google identity; organisation users join through an enterprise contract. Viewpoint Evidence targets life sciences and government sponsors. [V, 2026-10-22] |
| How to apply, and any approval or review step | Workbench Standard is self-serve sign-up, then a Data Use Agreement per data collection (including the Project Baseline Health Study Limited collection). Professional tier and Viewpoint go through Verily contact forms. Fuller Project Baseline (Study Watch) data for reproducibility is by request, subject to PBHS governance approval. [V, 2026-10-22] |
| Whether the program is active, paused, renamed or closed | **Verily Pre Workbench Standard tier:** Workbench Standard Researcher tier is live but labelled beta. [V, 2026-10-22]<br>**Verily Study Watch:** Study Watch appears discontinued but Verily has not said so on its own public pages. Press quoting an August 2025 internal memo and a spokesperson reports that Verily fully wound down its devices program, including "Study Devices", stopped manufacturing medical devices and will no longer support them, and every Study Watch product page is gone. Yet the Security and Trust page still lists "Study Watch & Hub" in its SOC 2 and ISO 27001 scope, and a third party, Quipment Inc. (Kennesaw, GA), registered as a repack or relabel establishment, added an FDA device listing for Study Watch (K182456) on 2026-05-12. (conflict) [R, 2026-10-22] |
| Whether the general developer or API program is open to new applicants | There is no public Study Watch API or SDK. The general researcher route, Workbench, is open to self-serve sign-up and documents a CLI (wb) and Terraform provider. [V, 2026-10-22] |
| Participant or user limits before approval or by tier | **Verily Pre Workbench:** Standard (free) tier is capped at 5 workspaces and 5 collaborators per workspace; Professional (paid) is unlimited. No participant caps published for Viewpoint. [V, 2026-10-22] |
| How academic access differs from commercial or consumer access | Access differs by tier (individual Standard or Professional vs contracted Enterprise), not by academic vs commercial status. No academic-specific terms are published. [V, 2026-10-22] |

**Pricing**

| Fact | Value |
|---|---|
| Device or hardware list price | Study Watch was an investigational device for research participants and not available to consumers; no list price was found. Galaxy Watch pricing in the Samsung bundle is not published by Verily. [C, 2026-10-22] |
| Consumer subscription or membership price | n/a |
| Research or academic pricing or discount | Not public [2026-10-22] |
| Fees for API, SDK, platform or data access | **Verily Pre Workbench:** Workbench Standard is free; Professional is paid with no published price; cloud compute is billed to the researcher's own account on both tiers. [V, 2026-10-22] |
| Minimum order, term or commitment | Not public [2026-10-22] |
| Whether pricing requires contacting sales | Yes for everything paid. Professional upgrade is through a contact form; Viewpoint and Pre are "Request a demo". [V, 2026-10-22] |

**Data access and terms**

| Fact | Value |
|---|---|
| Raw signals available to researchers, and by which route | **Verily Study Watch (historical data):** Study Watch recorded PPG and accelerometry at 30 Hz, ECG, heart rate and electrodermal activity, plus environmental sensors, and was reported at launch to hold up to a week of raw data on the device. Researchers outside Verily get its data only as de-identified Project Baseline data on approved request. [C, 2026-10-22]<br>**Viewpoint Evidence with Samsung Galaxy Watch:** Verily's chief product officer told MedCity News the Galaxy Watch bundle gives researchers raw device signals, such as PPG and accelerometer and gyroscope motion data. Verily's own press release says only that it will "fully integrate sensor data" and lists no streams, rates or raw-signal terms. [R, 2026-10-22] |
| Derived or processed metrics available to researchers | **Verily Study Watch:** Study Watch produced proprietary derived metrics including PPG inter-beat intervals with a per-beat quality flag, and an ambulatory-status classifier (10-second windows and total daily ambulatory time). [C, 2026-10-22] |
| Documented sampling rates or temporal resolution | **Verily Study Watch:** PPG 30 Hz and accelerometer 30 Hz (Study Watch, per a Verily-co-authored PBHS paper). No rates published for the Galaxy Watch integration. [C, 2026-10-22] |
| How far back data can be retrieved | Unclear |
| Export, API, SDK or file routes | No device-level export route. Data reach researchers through Verily Pre (Exchange data collections analysed inside Workbench under a DUA), through PBHS data requests, or as a Viewpoint sponsor. Workbench Standard users cannot bring their own data. [V, 2026-10-22] |
| API rate limits | Not public [2026-10-22] |
| Terms on retaining, storing or deleting data | The general privacy policy keeps personal information as long as necessary for the collection purpose (it excludes HIPAA-covered and research-study data handled for sponsors). Workbench release notes say Verily may delete trial accounts' data when the licence expires. [V, 2026-10-22] |
| Terms on using data to train AI or ML models | Unclear |
| Announced shutdowns, deprecations or migrations, with dates | Verily fully wound down its medical device program and stopped manufacturing and supporting devices (internal memo of August 2025, reported by press). Its other devices are marked "Not in Commercial Distribution" in GUDID (retinal cameras ended 2026-04-27; Onduo December 2025). Study Watch has no GUDID record and its product pages are gone. Platform renames since then include Data Discovery becoming Data Exchange (30 Sep 2025) and Workbench moving into Verily Pre (11 Nov 2025). [C, 2026-10-22] |

**Compliance and regulatory**

| Fact | Value |
|---|---|
| Whether a HIPAA Business Associate Agreement is offered | Verily says it acts as a business associate when subject to HIPAA for research sponsors; no standalone BAA offer page. [C, 2026-10-22] |
| Whether a data processing agreement is offered | Unclear |
| Published HIPAA statement | Verily claims independent HIPAA Security and Privacy Rule audits for Lightpath, Retinal Service, Site CTMS and Onduo. Study Watch, Workbench and Viewpoint are not in that list. [C, 2026-10-22] |
| Published GDPR statement | Privacy policy (Verily Health Inc., effective 2026-04-14) covers EU, UK and Swiss data, states participation in the EU-U.S. Data Privacy Framework and its UK and Swiss extensions, and uses standard contractual clauses for transfers. [C, 2026-10-22]<br>**Data Privacy Framework certification:** Two Verily entities, both in Dallas, TX, are listed Active on the Commerce Department's Data Privacy Framework registry under the EU-U.S. DPF, the Swiss-U.S. DPF and the UK Extension (HR and non-HR data for EU and UK, non-HR for Swiss). Verily Health Inc. (OrganizationId 10091, the entity named in the current privacy policy): certified 2026-04-20, next certification due 2027-04-20, no inactive periods. Verily Life Sciences, LLC (OrganizationId 7768): EU-U.S. and Swiss-U.S. since 2018-02-02, UK Extension since 2025-01-13, next certification due 2027-03-12, with lapses 2024-02-12 to 2025-01-13 and 2025-02-18 to 2025-03-17. Verification method for both: self-assessment. [V, 2026-10-22] |
| ISO/IEC 27001 status and evidence | Verily claims ISO/IEC 27001 certification covering Lightpath, Onduo, Research Sponsor (Project Baseline), Site CTMS, Retinal Service, Study Watch & Hub, and Workbench. Certificate not published (the page shows a Coalfire certification seal); reports may need an NDA. [C, 2026-10-22] |
| SOC 2 status and evidence | Verily claims a SOC 2 Type II audit for the same product list (including Study Watch & Hub and Workbench). Report available only on request, possibly under NDA. [C, 2026-10-22] |
| FDA clearances, from the FDA database | Three 510(k) clearances, product code DXH, all to Verily Life Sciences, LLC: K182456 Study Watch (single-lead ECG), decided 2019-01-17; K192415 Study Watch with Irregular Pulse Monitor, 2020-01-17; K213357 Study Watch with Irregular Pulse Monitor (Home), 2022-07-19. No GUDID record exists for Study Watch. The only registration listing openFDA returns for any of the three is K182456 by Quipment Inc., a repack or relabel establishment (created 2026-05-12); none is listed under Verily. [V, 2026-10-22] |
| Where data is stored, and residency options | General privacy policy says data may be stored outside the user's country, including in the United States. Workbench lets data owners apply region policies on GCP- and AWS-backed collections. [V, 2026-10-22] |

<!-- facts:end -->

### RingConn

<!-- facts:begin ringconn -->
*Generated from the fact record by `tools/facts/generate.py`. Edit the record, not this block.*

**Research access**

| Fact | Value |
|---|---|
| Formal research or academic program (name, what it offers) | Not public [2026-10-21] |
| Who can join the research program | n/a |
| How to apply, and any approval or review step | No application process. Institutional or business proposals go by email to business@ringconn.com; dealer and bulk-purchase enquiries go to sales@ringconn.com. RingConn says contacting it does not guarantee a partnership and that an enquiry does not establish that an unlisted capability (such as data access) can be supplied. [V, 2026-10-21] |
| Whether the program is active, paused, renamed or closed | No program has been launched, paused or closed. A published invitation for educational, government and institutional partnerships (including data analytics) was on the business article until at least 2025-11-25 and is absent from the version rewritten on 2026-10-17. The live page now offers only a business enquiry address and promises no partnership eligibility. [C, 2026-10-21] |
| Whether the general developer or API program is open to new applicants | Not public [2026-10-21] |
| Participant or user limits before approval or by tier | n/a |
| How academic access differs from commercial or consumer access | Not public [2026-10-21] |

**Pricing**

| Fact | Value |
|---|---|
| Device or hardware list price | **RingConn Gen 3 (US store):** $349 [V, 2026-10-21]<br>**RingConn Gen 2 (US store):** $299 [V, 2026-10-21]<br>**RingConn Gen 2 Air (US store):** $199 [V, 2026-10-21] |
| Consumer subscription or membership price | No subscription is required for any current ring (Gen 3, Gen 2, Gen 2 Air). The US App Store lists optional in-app purchases, "RingConn Partner+" at $5.99 monthly or $69.99 annually; no RingConn page found says what they unlock. [V, 2026-10-21] |
| Research or academic pricing or discount | No research or institutional pricing is published. Consumer student discount of 10% on a Gen 2 order, verified through ID.me. Customised offers or discounts for bulk purchases on request. [V, 2026-10-21] |
| Fees for API, SDK, platform or data access | n/a |
| Minimum order, term or commitment | Not public [2026-10-21] |
| Whether pricing requires contacting sales | Single-unit retail prices are public. Bulk and dealer pricing is not published; it is a customised offer through sales@ringconn.com. [V, 2026-10-21] |

**Data access and terms**

| Fact | Value |
|---|---|
| Raw signals available to researchers, and by which route | **Consumer and public routes:** Not public [2026-10-21]<br>**Company research collaboration:** One documented case, not a general offering: a 2026 method-comparison study in shooting athletes (preprint 2026-06-11; version of record in BMC Sports Science, Medicine and Rehabilitation, 2026-08-18, DOI 10.1186/s13102-026-01960-x) used raw finger PPG from a RingConn Gen 2 at 100 Hz (green channel only; the ring has green, red and infrared sensors) to derive inter-beat intervals. The firmware and app build were customised for research data export. Three authors are Shenzhen Ninenovo and/or RingConn LLC staff, and the companies supplied the equipment and technical support. [R, 2026-10-21] |
| Derived or processed metrics available to researchers | Via Health Connect (Android): resting energy, steps, exercise calories; time in bed, awake duration, sleep stages; resting and average heart rate; height; weight; oxygen saturation. HRV is not synced to Health Connect ("algorithm compatibility issue"). Apple Health sync is confirmed on RingConn pages but the HealthKit types are not listed. Blood Pressure Trends (Beta) results are never shared with any third-party health platform. In-app only: sleep, stress and recovery scores, respiratory rate, skin temperature trends and other proprietary metrics. [V, 2026-10-21] |
| Documented sampling rates or temporal resolution | Unclear |
| How far back data can be retrieved | **RingConn Gen 3:** On the ring: up to 10 days of unsynced data. In the account: synced history stays with the RingConn account, with no published cap; no API exists to retrieve it. [V, 2026-10-21]<br>**RingConn Gen 2 and Gen 2 Air:** On the ring: 5 to 7 days of unsynced data per each product page's specifications; the compare tables give the upper figure, 7 days. In the account: as for Gen 3. [V, 2026-10-21] |
| Export, API, SDK or file routes | Participant-side only. Apple Health (iOS) and Android Health Connect (Android 9 or later), both user-authorised per data type; Google Fit sync ended 2025-10-01. Portability on request (structured, machine-readable) through account settings, the in-app feedback feature or data_protect@ringconn.com. An in-app CSV export was reported in a December 2023 app update. No API, SDK, web dashboard, bulk researcher export or direct Strava sync. [C, 2026-10-21] |
| API rate limits | n/a |
| Terms on retaining, storing or deleting data | Personal data kept only as long as necessary for the policy purposes or as required by law; data in backups that cannot be deleted at once is isolated until deletion is possible; anonymised data may be used indefinitely. Blood Pressure Trends (Beta): raw PPG, accelerometer and skin temperature data cannot be physically deleted per user during the beta (processing stops and the data is isolated on request), and are irreversibly anonymised within 90 days after the beta ends. [V, 2026-10-21] |
| Terms on using data to train AI or ML models | **App privacy policy (all users); the training restriction is specific to Blood Pressure Trends (Beta):** Only the Blood Pressure Trends (Beta) section addresses training: that data (questionnaires, tags, entered BP values and ring PPG, accelerometer and temperature signals) is used for algorithm optimisation and only for RingConn's own models, not for other health products or any third party's training. The general policy allows use of data to improve products, indefinite use of anonymised data, and sharing of aggregated non-personal data, with no explicit AI-training clause. [V, 2026-10-21] |
| Announced shutdowns, deprecations or migrations, with dates | Google Fit sync ended 2025-10-01 23:00 UTC, replaced by Android Health Connect (HRV not yet synced there). Separately, after Oura's 2025 US ITC patent case, Oura granted RingConn a multi-year, royalty-bearing licence (announced October 2025) so US sales and the companion app continue; RingConn says US devices, app access, updates, warranty and support continue uninterrupted. [V, 2026-10-21] |

**Compliance and regulatory**

| Fact | Value |
|---|---|
| Whether a HIPAA Business Associate Agreement is offered | Not public [2026-10-21] |
| Whether a data processing agreement is offered | Not public [2026-10-21] |
| Published HIPAA statement | Not public [2026-10-21] |
| Published GDPR statement | RingConn states it complies with GDPR and CCPA; health and other special-category data is processed only with explicit consent; cross-border transfers use EU Standard Contractual Clauses (and, per the store policy, the UK IDTA). DPO contact data_protect@ringconn.com. [C, 2026-10-21] |
| ISO/IEC 27001 status and evidence | Not public [2026-10-21] |
| SOC 2 status and evidence | Not public [2026-10-21] |
| FDA clearances, from the FDA database | 510(k) K260490, "Ninenovo Blood Oxygen Ring" (models BORMB-01-6 to BORMB-01-14), applicant Shenzhen Ninenovo Technology Limited (RingConn's maker), product code DQA (oximeter, 21 CFR 870.2700, class II), received 2026-02-13, decision Substantially Equivalent 2026-10-02. No source links the cleared BORMB-01 models to a consumer RingConn model, and the Gen 3 product page still says "This product is not a medical device." No clearance for sleep apnea or blood pressure features was found. [V, 2026-10-21] |
| Where data is stored, and residency options | Mainland China users: stored on servers in the PRC. Users outside mainland China: stored on servers outside the PRC, possibly in a different jurisdiction from where the data was collected ("RingConn Cloud infrastructure deployed for global operations"), with SCCs for transfers. For all users, app crash and error monitoring (self-hosted Sentry, no health data) and customer-service system data are processed in mainland China. No region choice is offered. RingConn no longer claims universal UK storage. [V, 2026-10-21] |

<!-- facts:end -->

### Circular

<!-- facts:begin circular -->
*Generated from the fact record by `tools/facts/generate.py`. Edit the record, not this block.*

**Research access**

| Fact | Value |
|---|---|
| Formal research or academic program (name, what it offers) | No named program. The science page invites research partners to "bring us a protocol"; Circular supplies devices, raw signal access under agreement and engineering time for studies run against a reference standard. [V, 2026-10-22] |
| Who can join the research program | Clinical, academic and enterprise partners; no further criteria published beyond studies that use a reference standard. [V, 2026-10-22] |
| How to apply, and any approval or review step | Contact the research team through the science page (typical reply within five working days); no application form, review criteria or timeline published. API access for business customers is by contact and limited to selected projects. [V, 2026-10-22] |
| Whether the program is active, paused, renamed or closed | Unclear |
| Whether the general developer or API program is open to new applicants | No public developer program or API documentation. An API and SDK are offered to business customers on the Professional track, by contact, and access is limited to selected projects. [V, 2026-10-22] |
| Participant or user limits before approval or by tier | Not public [2026-10-22] |
| How academic access differs from commercial or consumer access | No separate academic track. Research partnerships are offered on the same terms to clinical, academic and enterprise partners; business buyers choose between a no-code team dashboard track and a Professional API/SDK track. [R, 2026-10-22] |

**Pricing**

| Fact | Value |
|---|---|
| Device or hardware list price | Circular Ring 2 lists at $349 (US, Obsidian Black) on the store product page, but the shop page's hero and HSA/FSA copy both call it a $299 ring. Circular Ring 3 price not yet announced (pre-orders December 2026). (conflict) [U, 2026-10-22] |
| Consumer subscription or membership price | No subscription required. Optional premium "Circles" are unlocked month by month with in-app coins, 12,000 to 16,000 coins a month, at about 4,000 coins per euro (roughly 3 to 4 euros a month); coins can also be earned by wearing the ring. [V, 2026-10-22] |
| Research or academic pricing or discount | Not public [2026-10-22] |
| Fees for API, SDK, platform or data access | Team dashboard (multi-account web dashboard with CSV export) is free; API and SDK fees are not published and go through a quote. [V, 2026-10-22] |
| Minimum order, term or commitment | Business orders start at 25 rings. [V, 2026-10-22] |
| Whether pricing requires contacting sales | Yes for business and research use. Both business tracks are priced by quote (volume discount on every ring); consumer rings are list-priced. [V, 2026-10-22] |

**Data access and terms**

| Fact | Value |
|---|---|
| Raw signals available to researchers, and by which route | Raw signal (PPG green/red/IR, single-lead ECG, skin temperature, 3-axis accelerometer) only through a research partnership, under agreement. No public route to raw signal; the app's Apple Health and Health Connect sync carries processed intraday values, not waveforms. [C, 2026-10-22] |
| Derived or processed metrics available to researchers | Through the team dashboard, CSV export of any metric with daily and historical detail per wearer. Through the phone, intraday values (temperature, SpO2, breathing rate and others), HRV and sport sessions sync to Apple Health and Health Connect. ECG and blood pressure reports export as PDF. [V, 2026-10-22] |
| Documented sampling rates or temporal resolution | **Circular Ring 2:** Ring 2 sensor rates per the science page; PPG (green, red, infrared) 25 Hz, single-lead ECG 510 Hz (40 s recordings), skin temperature 1 Hz at 0.01 °C resolution, 3-axis accelerometer 25 Hz. Resolution of exported metrics is not documented. [V, 2026-10-22] |
| How far back data can be retrieved | The team dashboard shows each wearer's full record, from last night back to the start; no API history limit is published. [R, 2026-10-22] |
| Export, API, SDK or file routes | (1) Team dashboard at dashboard.circular.care with CSV export, free for business customers; (2) API and SDK for selected projects by contact; (3) app sync to Apple Health and Health Connect (Google Fit retired February 2025); (4) PDF reports for ECG and blood pressure; (5) in-app export or deletion of a user's data; (6) raw signal under a research agreement. [V, 2026-10-22] |
| API rate limits | Not public [2026-10-22] |
| Terms on retaining, storing or deleting data | Personal data kept as long as needed for the stated purposes or as required by law, then deleted or kept only in anonymised form; the terms of use add that data held for contractual and regulatory obligations is deleted no later than ten years on, unless litigation arises. No API-side retention terms published. [V, 2026-10-22] |
| Terms on using data to train AI or ML models | With the user's explicit consent, Circular uses users' data to improve its machine learning models. No terms on research partners or API customers training models on Circular data are published. [V, 2026-10-22] |
| Announced shutdowns, deprecations or migrations, with dates | Circular Ring 1 Pro and Slim deprecated in ring firmware 1.1.142 (listed in early 2025); Google Fit replaced by Health Connect (app 25.0.0, 14 February 2025). Circular SAS converted to liquidation 14 October 2025, with operations moved to Circular Health Limited. Circular Ring 3 Pro and Slim announced, pre-orders December 2026. [C, 2026-10-22] |

**Compliance and regulatory**

| Fact | Value |
|---|---|
| Whether a HIPAA Business Associate Agreement is offered | Not public [2026-10-22] |
| Whether a data processing agreement is offered | Not public [2026-10-22] |
| Published HIPAA statement | The privacy policy says ring data is health information that may be subject to HIPAA; there is no claim of HIPAA compliance and no BAA. [C, 2026-10-22] |
| Published GDPR statement | Circular states it is the GDPR data controller; the policy lists EU data subject rights (access, erasure, portability and others) and says data may be transferred to the US and UK with safeguards. [C, 2026-10-22] |
| ISO/IEC 27001 status and evidence | Unclear |
| SOC 2 status and evidence | Not public [2026-10-22] |
| FDA clearances, from the FDA database | Not public [2026-10-22] |
| Where data is stored, and residency options | Data stored with Amazon Web Services in the Paris region (France); may be transferred to the US and UK. The terms add that personal data of visitors from the US is retained in the US. No residency choice offered. [V, 2026-10-22] |

<!-- facts:end -->

### Zepp Health (Amazfit)

<!-- facts:begin zepp-amazfit -->
*Generated from the fact record by `tools/facts/generate.py`. Edit the record, not this block.*

**Research access**

| Fact | Value |
|---|---|
| Formal research or academic program (name, what it offers) | No named, open research or academic access program. Zepp describes bespoke research collaborations (Stanford sleep study, UCSD Center for Wearable Sensors membership, NTNU on PAI, Peking University First Hospital AF study, Chinese universities) and a "data analytics services" offer aimed at researchers, providers, insurers and employers, with partnerships at 20 research labs, hospitals, pharma companies and universities as of end 2020. The only documented data route for third parties is the legacy Huami/Zepp Open Platform "data cooperation" OAuth Web API (see developer_program_status). [C, 2026-10-22] |
| Who can join the research program | No eligibility rules for a research program are published. For the legacy Open Platform data API: corporate applicants only, not individuals; a PhD researcher must apply in the name of the institution. [C, 2026-10-22] |
| How to apply, and any approval or review step | Research and developer enquiries go to developer@zepp.com (contact page). Legacy data API: register and apply on the Zepp Open Platform (dev.huami.com), 3 to 7 day review, then submit the cooperation details (country, platform, business, user numbers, needs); escalation to datapartner@huami.com. A December 2021 applicant quotes the Open Platform's own application docs (item 4) as saying a Zepp business representative will make contact and sign an agreement, and reports that Zepp then replied that the API must be paid for and equipment bought. [C, 2026-10-22] |
| Whether the program is active, paused, renamed or closed | Unclear |
| Whether the general developer or API program is open to new applicants | Two programs. (1) Zepp OS developer program, open: free SDK, Zeus CLI, simulator and Zepp Console for watch Mini Programs and watch faces, published through a store review. (2) Legacy Huami/Zepp Open Platform OAuth 2.0 Web API (api-open.huami.com) for cloud data, by application and review for corporate partners; subscriptions (webhooks) for invited partners only; docs last updated 2020; open-to-new-applicants status unclear. [C, 2026-10-22] |
| Participant or user limits before approval or by tier | Not public [2026-10-22] |
| How academic access differs from commercial or consumer access | No separate academic track. The legacy data API treats academics as institutional (corporate) applicants; individuals cannot apply. Commercial data-analytics customers (insurers, employers, wellness programs) are served by contract. [C, 2026-10-22] |

**Pricing**

| Fact | Value |
|---|---|
| Device or hardware list price | US store list prices on 2026-10-22, examples: Active 2 (Round) from $99.99; Helio Strap (screenless band) $99.99; Balance 3 $369.99 to $449.99. Range in the store runs from about $50 (earbuds) to $649.99 (T-Rex Dual Solar). [V, 2026-10-22] |
| Consumer subscription or membership price | Core features need no subscription. Optional Zepp Aura Premium (AI sleep and wellness coaching) and fitness membership are sold in the app; the US App Store lists in-app plans including a $9.99 monthly plan and yearly plans from $29.99 to $49.99, without naming which product each belongs to. [C, 2026-10-22] |
| Research or academic pricing or discount | Not public [2026-10-22] |
| Fees for API, SDK, platform or data access | Unclear |
| Minimum order, term or commitment | Not public [2026-10-22] |
| Whether pricing requires contacting sales | Devices are sold at public list prices. Data partnership and data-analytics terms are by agreement after contact with Zepp (no public price list). [C, 2026-10-22] |

**Data access and terms**

| Fact | Value |
|---|---|
| Raw signals available to researchers, and by which route | **Zepp OS on-watch apps:** A custom Zepp OS Mini Program can read accelerometer (x, y, z in cm/s^2), gyroscope (deg/s), barometer, compass and GPS on the watch, each behind a permission; heart rate is exposed as computed BPM values, and no raw PPG or ECG waveform API is documented. [V, 2026-10-22]<br>**Legacy Open Platform Web API:** The legacy Web API documents raw ECG (250 samples per second, from ECG-capable devices), per-minute raw motion data, and user-tagged sensor files (example shows a PPG CSV). Whether these endpoints still serve current devices is not stated. [R, 2026-10-22] |
| Derived or processed metrics available to researchers | On watch (Zepp OS): heart rate, resting HR, daily HR summary, AFib records, SpO2, stress, sleep (score, stages, times), steps, calories, distance, PAI, stand, fat burning, body temperature, workouts. Legacy Web API scopes: profile, activity (steps, distance, calories), sleep, heart rate, motion, sport summary and detail, PAI. Integrators (Terra, Thryve) expose activity, daily and sleep data. [V, 2026-10-22] |
| Documented sampling rates or temporal resolution | Zepp OS: heart-rate history is per minute (up to 1,440 values for the current day); accelerometer and gyroscope offer low, normal and high trigger-frequency modes with no Hz figures published. Legacy Web API: ECG at 250 samples per second; motion per minute; activity daily or hourly (hourly marked as becoming obsolete). [C, 2026-10-22] |
| How far back data can be retrieved | Unclear |
| Export, API, SDK or file routes | (1) Zepp OS Mini Program reading sensors on the watch, with a phone-side companion service that can send data to a server by HTTP fetch; (2) legacy Open Platform OAuth 2.0 Web API (partners); (3) third-party aggregators (Terra, which holds its own Zepp API credentials and polls every 5 to 10 minutes; Thryve); (4) one-way write from the Zepp app to Android Health Connect (26 data types since January 2025), plus Apple Health, Google Fit and Strava linking; (5) participant self-export of personal data from the app (Profile, Settings, Exercising user rights). [C, 2026-10-22] |
| API rate limits | Not public [2026-10-22] |
| Terms on retaining, storing or deleting data | Users can clear data, delete the account with all data, revoke consent, and request deletion through the app or the privacy-support page. No retention terms for third-party data partners are published. [C, 2026-10-22] |
| Terms on using data to train AI or ML models | Unclear |
| Announced shutdowns, deprecations or migrations, with dates | Unclear |

**Compliance and regulatory**

| Fact | Value |
|---|---|
| Whether a HIPAA Business Associate Agreement is offered | Not public [2026-10-22] |
| Whether a data processing agreement is offered | Not public [2026-10-22] |
| Published HIPAA statement | Not public [2026-10-22] |
| Published GDPR statement | Zepp says its privacy protection is designed following GDPR and CCPA, and a company blog calls Amazfit fully GDPR compliant. EEA transfers use standard contractual clauses per the app privacy policy (check by hand). [C, 2026-10-22] |
| ISO/IEC 27001 status and evidence | Unclear |
| SOC 2 status and evidence | Not public [2026-10-22] |
| FDA clearances, from the FDA database | No 510(k) or PMA found under Huami, Zepp or Amazfit in openFDA. FDA establishment registration (Anhui Huami Information Technology, owner/operator 10083608) lists the Amazfit Balance A2287 under product code PUH (body composition analyzer, class II, 510(k) exempt, listed 2023-08-08) and Zepp Clarity ONE, Omni and Pixie hearing aids under QUG (OTC air-conduction hearing aid with wireless technology, class II, exempt, listed 2023-04-04). Neither listing is a clearance. No clearance was found for any Amazfit watch feature (ECG, AFib, SpO2, blood pressure). [V, 2026-10-22] |
| Where data is stored, and residency options | Cloud data is held on AWS according to the company. Region detail (US and Canadian users in US data centres, EEA users in Germany, mainland China users in China; 20-F says AWS for North America and most of Europe, Tencent Cloud elsewhere) comes from documents the project fetcher cannot read; check by hand. Some devices (T-Rex 3) can keep GPS data on the watch only. [C, 2026-10-22] |

<!-- facts:end -->

## Sources

See `../sources.md` entries S-EMG-01 through S-EMG-08, and S-EMG-09 through S-EMG-13 (added 2026-10-09).

Added 2026-10-10 (rows for `../sources.md` proposed to the coordinator):
- Ultrahuman, UltraSignal page. https://www.ultrahuman.com/ultrasignal/ (accessed 2026-10-10). **Primary.** PPG, temperature and accelerometer "data stream"; application and loaned developer kit.
- Ultrahuman blog, "Accessing the Ultrahuman Partnership API", 19 September 2025. https://www.ultrahuman.com/blog/accessing-the-ultrahuman-partnership-api/ (accessed 2026-10-10). **Primary.** OAuth 2.0 for approved apps, scopes and data list.
- Biostrap, home and research pages. https://biostrap.com/ ; https://biostrap.com/research/ (accessed 2026-10-10). **Primary.** "Biostrap is now Sensor Bio" banner; raw PPG and IBI; raw and/or processed PPG, gyroscope and accelerometer; HIPAA claim.
- Sensor Bio home page. https://sensorbio.com/ (accessed 2026-10-10). **Primary, vendor.** "Full access to raw PPG and derived physiological signals, timestamped and exportable".
- Zepp Health, Data analytics page. https://www.zepp.com/data-analytics (accessed 2026-10-10). **Primary, vendor.** Research partnerships (end-2020 figure).
- Terra, Zepp integration page. https://tryterra.co/integrations/zepp (accessed 2026-10-10). **Secondary (aggregator).** Activity, Daily and Sleep data types.
- Verily, study-watch URLs https://verily.com/solutions/study-watch and https://verily.com/perspectives/verily-study-watch (HTTP 404 on 2026-10-10).

Added 2026-10-22, from the vendor fact records (each record holds the exact quotes and retrieval dates):
- Ultrahuman (`../../facts/ultrahuman.yaml`). Developer docs https://vision.ultrahuman.com/developer-docs?api=ppg and ?type=oauth, ?type=mcp; developer portal https://vision.ultrahuman.com/developer; https://www.ultrahuman.com/us/ring-pro/buy/ ; https://www.ultrahuman.com/gb/ring/buy/ ; https://www.ultrahuman.com/us/pulsomics/ ; https://www.ultrahuman.com/us/heroes/ ; API Agreement https://ultrahumanapp.notion.site/API-Agreement-for-Developers-and-Partners-120755317a9180999ce3edcfc1047f58 (read by hand); USITC notice https://www.usitc.gov/system/files/secretary/fed_reg_notices/337/337_1398_notice08212025sgl.pdf ; CBP ruling https://rulings.cbp.gov/docs/hq/2026/h354023 ; incident notice https://www.ultrahuman.com/legal/notice-march-2026 .
- Sensor Bio (`../../facts/sensor-bio.yaml`). https://sensorbio.com/product/sensor-bio-v2/ ; https://sensorbio.com/comparison/sensor-bio-v2-vs-polar-360/ ; https://developers.sensorbio.com ; https://sensorbio.com/privacy-policy/ ; https://sensorbio.com/press/sensor-bio-joins-innovators-network-at-american-heart-association-center-for-hea/ ; https://docs.tryterra.co/changelog/2026/july-update-2026 ; openFDA and FDA 510(k) searches for Biostrap, Sensr and Sensor Bio (no match).
- Verily (`../../facts/verily.yaml`). https://www.mddionline.com/business/verily-permanently-ceases-medical-device-manufacturing ; https://hitconsultant.net/2025/08/29/alphabets-verily-shuts-down-medical-device-division-shifts-focus-to-ai/ ; https://verily.com/security-trust ; FDA 510(k) K182456, K192415, K213357 (https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K182456 and equivalents) and registration listing https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfRL/rl.cfm?start_search=1&knumber=K182456 ; https://www.massdevice.com/verily-launches-biosensor-equipped-study-watch-clinical-study-patient-monitoring/ ; https://pmc.ncbi.nlm.nih.gov/articles/PMC11699500/ ; https://medcitynews.com/2026/03/verily-samsung-wearable-smartwatch-healthcare-pharma-research/ ; https://verily.com/newsroom/verily-launches-free-version-of-its-pre-exchange-and-workbench-solutions-powering-precision-health-ai-and-discovery ; https://support.workbench.verily.com/docs/guides/admin/licensing_tiers/ ; https://verily.com/solutions/pre-platform/workbench/upgrade-contact ; https://www.dataprivacyframework.gov/list .
- RingConn (`../../facts/ringconn.yaml`). https://ringconn.com/blogs/news/feedback-and-business-collaboration-with-ringconn ; https://ringconn.com/blogs/guides/how-sync-health-and-sleep-tracker-data ; https://ringconn.com/blogs/news/ringconn-will-migrate-from-google-fit-to-health-connect ; FDA 510(k) https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K260490 ; https://ouraring.com/blog/oura-itc-case/ ; research-firmware preprint https://doi.org/10.21203/rs.3.rs-9564367/v1 ; https://github.com/perezjuanj/OpenCircuit/wiki .
- Circular (`../../facts/circular.yaml`). https://www.circular.xyz/science ; https://www.circular.xyz/professionals ; https://www.circular.xyz/release-notes ; https://www.circular.xyz/blood-pressure ; https://www.circular.xyz/terms-of-use ; https://shop.circular.xyz/products/circular-ring-2 ; https://www.circular.xyz/shop ; https://www.societe.com/societe/circular-850542804.html (secondary) ; https://gadgetsandwearables.com/2026/02/14/circular-ring-liquidation/ (secondary) ; https://www.wareable.com/ces/circular-ring-2-ces (secondary) ; openFDA 510(k) and registration searches for Circular (no match).
- Zepp Health (`../../facts/zepp-amazfit.yaml`). https://github.com/zepp-health/rest-api/wiki ; https://zepp-health.github.io/rest-api/api-ecg-doc.html ; https://dev.huami.com/ ; https://github.com/zepp-health/rest-api/issues/25 and /issues/26 (secondary) ; https://www.zepp.com/contact-us ; https://docs.zepp.com/docs/distribute/ ; https://developer.zepp.com/os/home ; https://www.thryve.health/supported-wearable-devices/zepp-amazfit (secondary) ; https://www.zepp.com/privacy-policy ; FDA registration listing https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfRL/rl.cfm?start_search=1&ownerOperatorNumber=10083608 ; https://us.amazfit.com/products/active-2-round .
