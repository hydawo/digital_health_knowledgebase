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
| Pricing | Ring PRO **USD 479**; Ring AIR USD 349 (global comparison page) or GBP 329 (UK). No subscription for ring data; optional add-ons, for example "Ultrahuman Max" from USD 9.99/month on the US store. Heroes pricing on Ring PRO covers scientists and researchers (discount not shown). No published API fee; the API Agreement says Sandbox and Production access are unpaid (Notion page, read by hand). Enterprise "dedicated subscription plans" are unpriced | Prices **Verified**; API fee **Reported** |
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
<!-- facts:end -->

### Sensor Bio

<!-- facts:begin sensor-bio -->
<!-- facts:end -->

### Verily

<!-- facts:begin verily -->
<!-- facts:end -->

### RingConn

<!-- facts:begin ringconn -->
<!-- facts:end -->

### Circular

<!-- facts:begin circular -->
<!-- facts:end -->

### Zepp Health (Amazfit)

<!-- facts:begin zepp-amazfit -->
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
