# Movesense: gap hunter findings (baseline run, 2026-10-11)

Compared against `module-01-wearables/profiles/movesense.md` (profile), `module-01-wearables/comparison-matrix.md`
(matrix) and `facts/movesense.yaml` (every field still `unresearched`, so every finding below is "no" for the
yaml). Every quote was checked with `tools/facts/quote_probe.py` on 2026-10-11 and returned `exact`.

Sources the KB has not used: the Movesense news feed (37 pages; 2025 and 2026 posts on firmware, Flash logging
and the ECG Recorder app), the conformity page, the MD terms and conditions, the medical-software docs page, the
Bitbucket repo tree (7 public repos), the Academic Program's Google Form, Labfront's Movesense help page, openFDA.

Abbreviations: KB = knowledge base. "Date" is the source's own date where it has one, else the read date.

## Contradictions

### 1. Organization: Movesense has been independent of Suunto since 1 October 2021
- **Found:** Movesense left Suunto through a management buy-out announced 30 Sept 2021; the buyer is a company owned by Jussi Kaasinen, now CEO. Supply chain and manufacturing links with Suunto continue. Movesense Ltd (Movesense Oy) is the legal manufacturer of the MD (finding 4) and the App Store seller of its apps.
- **URLs:** https://www.movesense.com/news/2021/09/movesense-grows-independent-from-suunto/ ; https://www.suunto.com/en-gb/News/movesense-grows-independent-from-suunto
- **Quote:** "is becoming independent of Suunto following a management buy-out deal" (exact on both pages)
- **Date:** 2021-09-30
- **Source type:** vendor_page; secondary (Suunto newsroom)
- **In KB:** contradicts. Profile line 1 title "Movesense (Suunto)" and line 7 "Movesense (Suunto / Amer Sports, Finland)". Note the Academic Program's live application form still says the program "is initiated by the Movesense team at the Finnish sports watch expert Suunto" (finding 6), which may be where the stale framing comes from.

### 2. regulatory / export_routes: custom firmware is outside the MD's MDR certification
- **Found:** The Class IIa status covers the MD only with Movesense's certified firmware. Firmware a team writes itself is not covered, and the team must certify its own solution. Production medical firmware comes from a separate medical repository, access by email request. The last certified firmware before June 2025 was 2.1.5; 2.3.1 (June 2025) brought later features to medical use. MD firmware is developed under IEC 62304:2006. The MD is intended to be used with a host medical device or application, and the buyer is responsible for use within the intended purpose.
- **URLs:** https://www.movesense.com/news/2023/02/movesense-medicals-mdr-registration-approaches-what-does-it-mean-for-movesense-md-customers/ ; https://movesense.com/docs/medical/medical_sw/ ; https://www.movesense.com/news/2025/06/movesense-sensor-firmware-2-3-1-released-a-major-upgrade-for-medical-use/ ; https://www.movesense.com/product/movesense-medical-mdr/ ; https://www.movesense.com/md-terms-and-conditions/
- **Quotes:** "If you are developing your own sensor firmware, it is not covered with the MDR registration of Movesense MD." / "You must validate the possible clinical benefit and certify the solution separately." / "The Movesense Medical sensor only fulfills the requirements of the medical device standards if it has been paired with the certified Movesense firmware." / "The previous firmware version certified for medical use is 2.1.5, and subsequent updates have been intended for non-medical use only." / "the firmware is available through the Movesense Medical software repository, to which access is granted separately" / "Movesense MD firmware is developed in accordance with IEC 62304: 2006." / "If starting to develop a commercial medical firmware, please send an email to info@movesense.com to receive access to the medical firmware development repository." / "The Movesense MD is intended, by its manufacturer, to be used together with a host medical device or an application"
- **Date:** 2023-02-01; 2025-06-12; docs and product page read 2026-10-11
- **Source type:** vendor_page; vendor_docs; vendor_legal
- **In KB:** contradicts by omission. Profile lines 18, 22, 174-175 and Best-Fit lines 198-199 present custom firmware and Class IIa status side by side as joint strengths; nothing says they are mutually exclusive. Matrix line 333 does the same. A study planning custom on-sensor processing on the MD would lose the medical-device status it may be relying on.

### 3. raw_streams / export_routes: Labfront supports Movesense MD and Flash, not only HR2, with a device discount; recording is participant-started
- **Found:** Labfront lists Movesense Medical, HR2 and Flash as compatible, offers a Movesense device discount to its customers, and delivers Movesense data as CSV by data type. Participants must manually start each recording through a task in the Labfront app, which bears on adherence.
- **URL:** https://help.labfront.com/movesense-overview
- **Quotes:** "Labfront is compatible with the following Movesense devices: Movesense Medical Movesense HR2 Movesense Flash" / "Our partnership with Movesense allows us to offer a discount to Labfront customers" / "manually start recording data through a task on the participant app in order to capture their data"
- **Date:** read 2026-10-11
- **Source type:** secondary (integrator docs)
- **In KB:** contradicts. Profile line 80 "Labfront supports Movesense HR2"; matrix line 346 "Garmin, Movesense HR2, Dexcom G7". The discount and the manual-start requirement are absent.

### 4. compliance: MDR certification has independent evidence (ISO 13485:2016 certified by Eurofins; two MD product numbers, MDR and legacy MDD)
- **Found:** The conformity page states Movesense Ltd is ISO 13485:2016 certified, with the QMS audited and certified by Eurofins Electric & Electronics Finland Ltd. It lists two MD product numbers: MS060222000 under MDR 2017/745 and SS050341000 under the old MDD 93/42/EEC, Class IIa per Annex IX rule 9, conformity route Annex II. A researcher buying MD units should check the SKU, since older stock is MDD-certified. The MD terms name MS060222000 as the MDR-certified SKU. The certificate itself and the EUDAMED entry were not located (searched; see bottom), so this remains a vendor statement naming its auditor.
- **URLs:** https://www.movesense.com/conformity ; https://www.movesense.com/md-terms-and-conditions/
- **Quotes:** "The quality management system of Movesense was audited and certified by Eurofins Electric & Electronics Finland Ltd." / "Product number MS060222000: MDR 2017/745 Product number SS050341000: MDD 93/42/EEC"
- **Date:** read 2026-10-11
- **Source type:** vendor_legal
- **In KB:** no. Profile lines 22, 28, 123 and matrix line 260 state Class IIa MDR with no ISO 13485, no named auditor and no SKU distinction.

### 5. sampling_rates / history_depth: Flash logging durations are published; memory unit is inconsistent across vendor pages
- **Found (a):** Movesense publishes Flash logging capacities: up to five days of single-channel ECG, heart-rate intervals for over four months (battery change about monthly), accelerometry four days at 26 Hz, 9-axis IMU at 52 Hz almost 19 hours. A free, open-source Flash Datalogger GUI was released Jan 2026 and improved Mar 2026; it needs Flash firmware 2.3.x or later.
- **URL:** https://www.movesense.com/news/2026/03/improved-ecg-imu-data-logger-for-movesense-flash-now-available/
- **Quotes:** "can store up to five days of single-channel ECG or heart rate intervals for over four months" / "for heart rate interval recording the battery must be replaced approximately once a month" / "Acceleration data can be logged for four days at a sample rate of 26 Hz." / "For 9-axis motion data (acceleration, gyro, magnetometer) at 52 Hz, the capacity is enough for almost 19 hours." / "the tool is free to use and open source"
- **Found (b):** The Flash product page says "128 Mb" (megabits, which would be 16 MB); the specifications page says "128MB". The published durations are consistent with 128 MB, so the product page is probably a typo, but the vendor's own pages disagree.
- **URLs:** https://www.movesense.com/product/movesense-flash/ ; https://www.movesense.com/specifications/
- **Quotes:** "The sensor stores data for post-analysis in its 128 Mb integrated memory." / "128MB internal memory for logging data autonomously"
- **Date:** 2026-03-26; product and spec pages read 2026-10-11
- **Source type:** vendor_page
- **In KB:** no for (a): Open Question line 220 "Maximum continuous logging duration on Flash's 128 MB at given rates" is answered here; Participant Experience line 115 calls the ECG products "session-wear" while the vendor claims five days of ECG logging on Flash. (b) is a source conflict the KB does not record (profile lines 29, 91, 176 say 128 MB).

## Missing programs and program changes

### 6. program_status / program_application: Academic Program form is still live, but signals are mixed
- **Found:** The Google Form linked as "APPLY HERE" still loads and accepts applications (no "no longer accepting responses" notice on 2026-10-11). It says applications are reviewed weekly, while the program page says monthly. It still credits Suunto as co-initiator (stale since 2021). The program page's "Benefits for Scientific Research" page links a "Research Bundle" whose product URL now returns 404. Latest cohort listed remains Q1 2023. Earlier wording (program poster, per a search summary, not probe-confirmed) mentioned up to 20 sensors per project and Kaasa's Data Collector app; the live page no longer gives a number.
- **URLs:** https://forms.gle/3TbrtfVbdAXFdM2S7 (resolves to https://docs.google.com/forms/d/e/1FAIpQLSe4R4gB78sni_M-LH1VJOWL-1j_h4mEo55T7MY0gp1KcLXFXA/viewform) ; https://www.movesense.com/movesense-academic-program/ ; https://www.movesense.com/benefits-of-movesense-sensor-for-scientific-research/ ; https://www.movesense.com/product/movesense-research-bundle-hr2/ (404)
- **Quotes:** (form) "Movesense team reviews the applications on weekly basis and invites up to three projects per quarter to the program." / (form) "The program is initiated by the Movesense team at the Finnish sports watch expert Suunto" / (benefits page) "have a look at our Research Bundle of sensors and chest straps"
- **Date:** read 2026-10-11
- **Source type:** vendor_page
- **In KB:** partly. Profile line 85 and matrix line 403 have the program and the Q1 2023 staleness (Unclear). The live form, the weekly/monthly conflict and the dead Research Bundle link are absent. Status should stay Unclear; only vendor contact (info@movesense.com) can settle it.

### 7. academic_vs_commercial / minimum_commitment: research-to-commercial path, custom firmware in production from 200 units
- **Found:** Movesense pitches a path from research to product: custom branding and custom firmware flashed on the production line from 200 pieces; white-label OEM supply. This is the "separate agreement" the SDK licence points to (profile line 99).
- **URLs:** https://www.movesense.com/benefits-of-movesense-sensor-for-scientific-research/ ; https://www.movesense.com/news/2024/06/faq-regarding-movesense-md-medical-sensor/
- **Quotes:** "starting from as low minimum quantities as 200 pieces" / "We can ship white-labeled OEM products in mass quantities."
- **Date:** read 2026-10-11; FAQ 2024-06-17
- **Source type:** vendor_page
- **In KB:** no.

## Regulatory

### 8. fda_clearances: no FDA clearance; Movesense says 510(k) is "on the roadmap"
- **Found:** openFDA 510(k) returns no match for applicant "movesense" or device name "movesense"; the only Suunto record is K971644 (Suunto USA, 1997, unrelated). The registration and listing database returns no Movesense establishment. Movesense's own MD FAQ says FDA 510(k) is planned. The ECG Recorder app (Class IIa in the EU as part of the MD) is nonetheless listed on the US App Store.
- **URLs:** https://api.fda.gov/device/510k.json?search=applicant:movesense ; https://api.fda.gov/device/registrationlisting.json?search=registration.name:movesense ; https://www.movesense.com/news/2024/06/faq-regarding-movesense-md-medical-sensor/ ; https://apps.apple.com/us/app/movesense-ecg-recorder/id6443902831
- **Quote:** "FDA 510k is on the roadmap and coming up in the future."
- **Date:** FAQ 2024-06-17; openFDA queried 2026-10-11
- **Source type:** regulator_db; vendor_page; app_store
- **In KB:** no. Profile lines 125 and 219 and matrix line 260 leave FDA status "Unclear". It can be set to: no clearance found in the FDA database (regulator_db), planned per vendor.

## Data access, software and licensing

### 9. licence / export_routes: mobile samples and Showcase app are Apache 2.0; newer tools MIT or open source
- **Found:** Not all Movesense software is under the proprietary SDK agreement. The mobile library repo states the Showcase app and sample source are Apache 2.0 (the MDS core library itself is a binary from a third-party maker). The 2026 `sbem-tools` repo (Movesense's binary log format) is MIT. The Flash datalogger is described as open source, but its README licence section is an unfilled placeholder. There are 7 public Bitbucket repos; `movesense-mobile-lib` updated 2026-06-01, `python-datalogger-tool` 2026-10-08, `sbem-tools` 2026-09-14. Official Flutter plugin (`mdsflutter`); React Native and Xamarin plugins are third-party.
- **URLs:** https://bitbucket.org/movesense/movesense-mobile-lib/raw/master/README.md ; https://bitbucket.org/movesense/sbem-tools/raw/master/README.md ; https://bitbucket.org/movesense/python-datalogger-tool/raw/master/README.md
- **Quotes:** "ShowcaseApp and sample source code is published under Apache 2.0 license." / "The bug has been reported to the maker of MDS" / "This project is licensed under the MIT License." / "[Add your license information here]"
- **Date:** read 2026-10-11
- **Source type:** repository
- **In KB:** contradicts (partly). Profile line 11 "Open source | No" and matrix line 55 "No" are correct for the device library, but no profile or matrix line separates the Apache 2.0 mobile samples and MIT tools from the proprietary device SDK.

### 10. export_routes: five free vendor recording tools, including EDF+ export from the ECG Recorder app
- **Found:** Movesense lists five free recording tools: Showcase app (iOS/Android, CSV and JSON), Python GATT SensorData client (Windows/macOS/Linux), ECG Recorder (MD only; CSV, PDF, EDF+), Python Flash datalogger, and an Android datalogger sample. GATT SensorData Protocol has been in default firmware since 2.3.0, so raw ECG and IMU can be collected on a laptop without custom firmware. ECG Recorder is certified Class IIa as part of the MD; Movesense said advanced features will move to a premium subscription. Firmware 2.3.0 added 16-bit mV ECG storage and an optional "wipe datamem on DFU".
- **URLs:** https://www.movesense.com/news/2025/11/recording-data-with-movesense-sensors-five-free-tools-to-get-you-started/ ; https://www.movesense.com/news/2025/07/movesense-ecg-recorder-update-2-1-adds-new-ecg-reports-to-the-app/ ; https://bitbucket.org/movesense/movesense-device-lib/raw/master/CHANGES.md
- **Quotes:** "The Movesense ECG Recorder app is certified as a class IIa medical device as part of the Movesense MD sensor." / "some of the application’s advanced features will be packaged into a premium subscription version" / "Feature: Wipe datamem on DFU"
- **Date:** 2025-11-20; 2025-07-10; CHANGES.md read 2026-10-11
- **Source type:** vendor_page; repository
- **In KB:** no. Profile Data Access lines 90-93 list only BLE streaming and onboard logging; Active Data Collection and Researcher Features (lines 80, 84) say "None" with no mention of the vendor's own recording apps.

### 11. sampling_rates: vendor FAQ warns BLE is the bottleneck at high rates
- **Found:** The device-lib FAQ says high sampling rates can lose data over BLE and advises lowering the rate or buffering. Relevant to the KB's 1.6 kHz IMU and 512 Hz ECG headline figures, which are sensor capabilities, not streaming guarantees.
- **URL:** https://bitbucket.org/movesense/movesense-device-lib/raw/master/FAQ.md
- **Quote:** "Bluetooth transmission between the sensor and mobile device is often the bottleneck"
- **Date:** read 2026-10-11
- **Source type:** repository
- **In KB:** no. Profile lines 70 and 171 and matrix lines 109, 125, 129 present the ceilings without this caveat.

## Pricing

### 12. device_price: Flash and HR2 list prices are public
- **Found:** Flash €249 (1-49), €244 (50-99), €239 (100-199), VAT 0%. HR2 €99 (1-49), €94, €89. Accessories sold separately.
- **URLs:** https://www.movesense.com/product/movesense-flash/ ; https://www.movesense.com/product/movesense-sensor-hr2/
- **Quotes:** "1-49 249€" / "1-49 99€"
- **Date:** read 2026-10-11
- **Source type:** vendor_page
- **In KB:** no. Profile line 133 gives MD only ("other models also listed in the web shop"); matrix line 229 MD only.

## Participant experience

### 13. Battery and water rating are on the web, not gated
- **Found:** The MD FAQ lists IP68 water and shock proofing and a user-replaceable Maxell CR2025 coin cell, and says the MD is suitable for hyperbaric chambers. The device FAQ adds that battery-level readings are only reliable near discharge.
- **URL:** https://www.movesense.com/news/2024/06/faq-regarding-movesense-md-medical-sensor/
- **Quotes:** "Water (IP68) and shock proof construction" / "User replaceable battery (Maxell CR2025 coin cell)"
- **Date:** 2024-06-17
- **Source type:** vendor_page
- **In KB:** no. Profile lines 189-190 say battery and water rating are behind gated PDFs; Open Question line 217 and matrix line 210 ("Unclear (datasheets gated)").

## Ecosystem and evidence

### 14. Kubios "integration" is a CSV workflow; Fibion resells Flash
- **Found:** Movesense's Kubios post describes recording in the Showcase app, saving CSV and opening it in Kubios HRV. That is file import, not an integration. Separately, Fibion (Finnish research-device vendor) sells a Movesense-Flash-based "Fibion Flash" HRV research kit, a third route to the hardware.
- **URLs:** https://www.movesense.com/news/2022/08/kubios-and-movesense-combine-advanced-ecg-and-hrv-analysis-tools/ ; https://web.fibion.com/articles/movesense-hrv-research-fibion-flash/
- **Quotes:** "Save the recorded data files as csv with the app Open the csv files in Kubios HRV" / "The Movesense Flash sensor is increasingly used in research for ECG and HRV data collection due to its small size, affordability, and technical specifications."
- **Date:** 2022-08-08; Fibion read 2026-10-11
- **Source type:** vendor_page; secondary
- **In KB:** partly. Profile line 76 calls Kubios an "integration" (Reported); can be Corroborated as a CSV workflow. Fibion is absent.

### 15. Module 3 already has a Movesense deployment the profile does not link
- **Found:** `module-03-applied-studies/profiles/movesense-palliative-support-trial.md` (Helmer 2025, BMC Palliat Care, PMC12126900) used the Movesense Medical chest sensor; chest-wall valid-data share 55.2% of monitored time. Also relevant: NeuralCloud pilot (Feb 2026, non-binding) for AI Holter reporting with MD data; no FDA or US detail.
- **URLs:** https://pmc.ncbi.nlm.nih.gov/articles/PMC12126900/ ; https://www.movesense.com/news/2026/02/movesense-and-neuralcloud-to-pilot-ai-powered-ecg-and-holter-reporting/
- **Quote:** none needed for the cross-link (Module 3 profile holds the full-text figures).
- **Date:** 2025-05-31; 2026-02-17
- **Source type:** paper; vendor_page
- **In KB:** no in the Module 1 profile (Research Evidence lines 138-167 have no Module 3 link, contrary to CLAUDE.md's cross-reference rule).

## Searched, nothing found
- FDA 510(k), De Novo and registration/listing (openFDA) for Movesense; nothing beyond the unrelated 1997 Suunto record.
- EUDAMED and the notified body's certificate number for the MD: not located by search; Eurofins is named only by Movesense.
- HIPAA, BAA, SOC 2, ISO 27001, GDPR statements for any Movesense software: none found (no cloud in the default path; the ECG Recorder app's privacy terms were not read).
- Bitbucket issue trackers: the Bitbucket issues API is deprecated (CHANGE-3071), so issues could not be listed; no GitHub org exists.
- 2024-2026 Academic Program cohorts: none on the program page, news feed pages 1-2, or search.
- Price or availability of developer kits and the HR+ model; the Research Bundle page is 404.
- Data terms, AI-training terms, rate limits, deprecations: none apply in the BLE path; no shutdown or deprecation announcements found in 2025-2026 news.
- PubMed `movesense[tiab]`: 18 hits, same count as the KB's 2026-10-09 search; the 2026 Front Digit Health arrhythmia paper (PMID 42591110) is the only newer item and was not read.
- BioStock MedTech Summit 2026 article (403; company-funded coverage, not read).
