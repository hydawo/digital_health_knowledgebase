# Polar: gap hunter findings (baseline run, 2026-10-11)

Compared against `module-01-wearables/profiles/polar.md` (profile), `module-01-wearables/comparison-matrix.md`
(matrix) and `facts/polar.yaml` (every field still `unresearched`, so every finding below is "no" for the
yaml). Every quote was checked with `tools/facts/quote_probe.py` on 2026-10-11 and returned `exact`. For
GitHub files the probe used the github.com URL with `--fetch-url` pointing at raw.githubusercontent.com.

Abbreviations: KB = knowledge base. "Date" is the source's own date where it has one, else the read date.

## Contradictions

### 1. Licence (export_routes, academic_vs_commercial): the BLE SDK is not open source; it ships under Polar's proprietary limited licence
- **Found:** The repo's licence file is a "Software Development Kit Limited License Agreement" with Polar Electro Oy, not an open-source licence (GitHub reports the licence as NOASSERTION). It lets you use, copy and modify the SDK and is free of charge, but Polar keeps ownership. The grant is limited to "enabling Data transfer between POLAR product and Developer Software". Polar can end it on 90 days' notice, or on 7 days for an uncured breach, after which all copies must be deleted. It also disclaims medical use. In issue #835 (June 2026) Polar approved a research project's GPLv3-with-linking-exception licence, which shows the SDK's terms are separate from, and not compatible by default with, open-source licences.
- **URL:** https://github.com/polarofficial/polar-ble-sdk/blob/master/Polar_SDK_License.txt ; https://github.com/polarofficial/polar-ble-sdk/issues/835
- **Quotes:** "SOFTWARE DEVELOPMENT KIT LIMITED LICENSE AGREEMENT" / "You may use, copy and modify the SDK as long as you include the original copyright and license notice in any copy of the software/source and you comply with the license terms." / "Polar and its licensors shall continue to own all right, title and interest, including copyright and all other intellectual property rights in and to the Licensed Materials" / "This Agreement shall remain in force until terminated by Polar by either Party by providing a ninety (90) days prior written notice to the other Party." / "You shall cease the use of Licensed Materials and Confidential Information and any of its rights under Section 3, and destroy and delete all copies of the Licensed Materials and Confidential Information." / "Licensed Materials and Polar's devices are not intended to be used in life critical, life supporting or medical purpose." / (issue #835, Polar staff) "the license looks good, you can proceed with that"
- **Date:** read 2026-10-11 (licence file undated); issue #835 closed 2026-06-18
- **Source type:** repository (vendor_legal text hosted in the vendor's repo)
- **In KB:** contradicts. Profile line 11 "**SDK is open source** (Polar BLE SDK, GitHub)", line 18 "The **Polar BLE SDK is open source on GitHub**", line 29 "An open-source Android/iOS SDK", line 154 "**Polar BLE SDK**, open source", line 182 "**SDK: free and open source.**", line 198 "**Free, open-source SDK**"; matrix lines 50, 127, 228, 328 say "open SDK" or "Open BLE SDK". The profile's "no API deprecation risk on the raw-data path" (lines 162, 201) also needs softening: the SDK licence can be terminated on notice. "Source-available, free, under Polar's limited licence" is the accurate wording.

### 2. research_program / program_application: Polar runs a documented research-collaboration application process
- **Found:** The "Collaborate with us" page sets out a proposal process: a research co-operation application sent by email, a list of required documents (research plan of up to 10 pages, budget, and a "proposal for Polar support (technology, money, other)"), review criteria that include "value for the company", and a two-week response. So Polar does describe an application and review step and can provide money or technology, even though there is no open academic tier or published discount.
- **URL:** https://www.polar.com/en/science/collaborate-with-us
- **Quotes:** "Please send your research co-operation application to the email address below." / "budget and proposal for Polar support (technology, money, other)" / "value for the company" / "Proposals are evaluated and response given to applicant within two weeks."
- **Date:** read 2026-10-11
- **Source type:** vendor_page
- **In KB:** contradicts (partly). Profile line 136 says the science page offers a "Collaborate with us" contact and "No grant, discount or application process is described"; matrix line 398 says "No formal programme; 'Collaborate with us' contact". The application process, support types and review criteria are absent. Note: Polar's own business page names partner institutions (Canadian Sport Institute Calgary, University of Oulu, University of Jyväskylä, SFISM Magglingen, Santasport, University of Helsinki), as profile line 136 says.

### 3. raw_streams / fda_clearances: AccessLink returns wrist ECG waveforms, SpO2 test results and temperature (Elixir biosensing)
- **Found:** AccessLink v3 has an "Elixir Biosensing" resource (beta since 19 Dec 2023, body temperature added 5 Mar 2024) with body temperature, sleep skin temperature, skin contact, **wrist ECG test results** and **SpO2 test results**. The ECG test result schema includes ECG samples (`amplitude_mv` with `recording_time_delta_ms`), quality measurements, average HR, HRV, RR interval and pulse-transit-time fields. SpO2 results carry `blood_oxygen_percent`, class, deviation from baseline and altitude. Polar's support page says the wrist ECG (Vantage V3, Grit X2, Grit X2 Pro, Vantage M3) is not for medical use, and Polar staff confirmed in SDK issue #887 that the ECG is not available over the BLE SDK. So the only researcher route to a Polar watch's ECG is the cloud API.
- **URL:** https://www.polar.com/accesslink-api/ ; https://support.polar.com/en/wrist-ecg ; https://github.com/polarofficial/polar-ble-sdk/issues/887
- **Quotes:** "Elixir™ Biosensing data consists of body temperature data, sleep skin temperature data, skin contacts data, wrist ECG test report data and SpO2 test report data." / "Elixir™ biosensing data released in beta status" / (support) "The ECG test is not intended for medical or diagnostic use." / (support) "average heart rate, heart rate variability, beat-to-beat interval and pulse arrival times (PAT)" / (#887) "ECG / Elixir is not available through the Vantage V3 BLE SDK."
- **Date:** AccessLink changelog 19.12.2023 and 05.03.2024; read 2026-10-11; issue #887 answered 2026-10-05
- **Source type:** vendor_docs; vendor_page; repository
- **In KB:** contradicts. Profile line 44 lists ECG for the H10 only; line 49 says SpO2 "Unclear"; line 48 says temperature "Unclear"; line 147 lists AccessLink contents without any biosensing, ECG or SpO2 data. Matrix lines 75 to 77 do not list the Vantage V3 / Grit X2 line. Not a regulatory clearance: openFDA shows no Polar Electro 510(k) (see "searched, nothing found").

### 4. sampling_rates / raw_streams: the watch line's SDK data are documented, and are narrower than "Unclear" implies
- **Found (a):** `PolarVantageV3andGritX2Pro.md` lists online streaming of HR, accelerometer (50 Hz, plus or minus 8 g), PPG, PPI, gyro, magnetometer, pressure and skin temperature, and data export of sleep, steps, Nightly Recharge, 24/7 HR, 24/7 PPi, skin temperature, calories and SpO2 test results. Ignite 3 and Pacer / Pacer Pro stream only HR, PPI and 50 Hz accelerometry. SDK release 7.1.0 (21 Apr 2026) added SpO2 test-result loading.
- **Found (b):** SDK mode is not supported on watches, streaming only works from the exercise-wait view after a manual pairing and "Share" step on the watch, and starting a training session stops PPI streaming.
- **Found (c), conflict inside Polar's own sources:** in issue #887 (5 Oct 2026) Polar staff said the Vantage V3 does not save 24/7 HR, PPi or skin temperature for SDK loading (online streaming only), which contradicts the product page's "Data export" list. The same answer said the offline recording API "is currently supported only by Polar H10", which conflicts with `PolarVeritySense.md` and `Polar360.md` (both document offline recording). Treat the reply as Reported and the per-device docs as governing, pending clarification.
- **URL:** https://github.com/polarofficial/polar-ble-sdk/blob/master/documentation/products/PolarVantageV3andGritX2Pro.md ; https://github.com/polarofficial/polar-ble-sdk/blob/master/documentation/UsingSDKWithWatches.md ; https://github.com/polarofficial/polar-ble-sdk/releases/tag/7.1.0 ; https://github.com/polarofficial/polar-ble-sdk/issues/887
- **Quotes:** "Accelerometer data with sample rate of 50 Hz and range of 8 G." / "24/7 PPi samples" / "SPO2 test results" / "SDK Mode is currently not supported in Polar watches." / "Starting a training with PPI streaming ongoing will stop the PPI streaming automatically, as this cannot work during training." / "Adds SDK support for loading SPO2 test result data" / (#887) "Vantage V3 does not save offline/24/7 HR, PPi, or skin-temperature data." / (#887) "PolarOfflineRecordingApi is currently supported only by Polar H10. It is not supported by Vantage V3."
- **Date:** read 2026-10-11; release 7.1.0 2026-04-21; issue answered 2026-10-05
- **Source type:** repository
- **In KB:** contradicts (partly). Profile line 108 "Per-device rates were not retrieved for these models. **Unclear.**"; line 48 temperature "Unclear"; lines 50 and 51 GPS and barometer "Unclear" (pressure is now documented for the Vantage V3 / Grit X2 line). Profile line 150 says Verity Sense and H10 record without a phone, which the per-device docs support; the #887 statement is the outlier.

### 5. derived_metrics / sampling_rates: 24/7 PPi on Polar 360 and Loop is session-based, not continuous
- **Found:** Polar staff (issue #886, 5 Oct 2026) said 24/7 PPi on Polar 360 and Loop is stored as automatically triggered measurement sessions, not a continuous recording; the schedule, session length and day/night differences are undocumented; each interval carries an error estimate plus skin-contact, movement and online/offline flags. Polar recommends a pilot to measure coverage.
- **URL:** https://github.com/polarofficial/polar-ble-sdk/issues/886
- **Quotes:** "PPi is stored as separate, automatically triggered measurement sessions rather than a continuous 24/7 recording." / "The exact acquisition schedule is not documented."
- **Date:** 2026-10-05
- **Source type:** repository
- **In KB:** contradicts (framing). Profile line 112 and matrix line 108 say "PP interval and 24/7 PPI samples" and call the 360 "the only Polar device in this profile with a documented multi-day raw-PPG offline path"; nothing says 24/7 PPI is intermittent with an undocumented duty cycle, which matters for any HRV endpoint.

### 6. api_platform_fees / retention_terms / deprecations: the Polar API agreement (22 Aug 2025) reserves fees, requires deletion on termination, and lets Polar cut access for any reason
- **Found:** The AccessLink licence is now the "Polar Application Programming Interface (API) Limited License Agreement" (latest update 22 August 2025), covering AccessLink and the Team Pro API. Key terms: free "at the moment" but fees reserved; 30 days' notice to terminate; Polar may suspend or terminate any access "for any or no reason, with immediate effect"; on termination the licensee must delete all copies of the Data; the app's primary purpose must be "extending and improving the Member's experience"; Polar must be credited as the data source on any display of data or derived data; EU DMA gatekeepers are excluded; the licensee is an independent data controller for AccessLink. The old PDF URL (`/sites/default/files/static/ACL_Ltd_License_Agreement.pdf`) now returns 404. No AI/ML-training clause and no research carve-out.
- **URL:** https://www.polar.com/en/legal/polar-api-agreement
- **Quotes:** "Latest update: 22 August 2025" / "Polar reserves the right to charge fees from time to time at its discretion" / "This Agreement shall remain in force until terminated by either Party by providing a thirty (30) days prior written notice to the other Party." / "to suspend or terminate Your, Your Corporate Customer’s or any Member’s access to Polar Ecosystem for any or no reason, with immediate effect" / "You shall cease the use of Licensed Materials, access to Polar Ecosystem and Data and Your rights under Section 2 shall cease, and You shall destroy and delete all copies of the Licensed Materials and Data." / "the primary purpose of your application and service shall be extending and improving the Member’s experience" / "shall credit Polar Ecosystem as the source of Data when displaying any Data, or any data derived from Data in Your application or service" / "Gatekeepers shall not be eligible to enter into this Agreement." / "When using AccessLink, You (or the relevant Corporate Customer as the case may be) shall also be data controller"
- **Date:** 2025-08-22
- **Source type:** vendor_legal
- **In KB:** contradicts (partly). Profile line 185 "no documented API fee" and matrix line 228 "AccessLink no fee" omit the fee reservation; matrix line 398 says the agreement is "not summarised in the profile"; the deletion-on-termination duty is absent, and matrix line 379 lists Polar BLE among routes with no retention limits (true for the SDK's data, but the API route has this clause). Controller role matches profile line 178.

## Missing from the KB

### 7. deprecations: transactional AccessLink endpoints deprecated (Aug 2025 and Jan 2026)
- **Found:** Changelog 18.08.2025 deprecates the transactional Exercises and Daily activity endpoints in favour of new non-transactional ones; 13.01.2026 deprecates the transactional Physical info endpoint and adds a PHYSICAL_INFORMATION webhook. The deprecated transactional endpoints use a 28-day window; the non-transactional exercises list uses 30 days. No removal date is given. Other operational terms: webhooks auto-deactivate after 7 days of failed delivery, and a 403 is returned if the user has not accepted all mandatory consents (both 28.06.2023).
- **URL:** https://www.polar.com/accesslink-api/
- **Quotes:** "Transactional endpoint for Exercises is deprecated" / "Only data that has been uploaded in the last 28 days will be available. This resource is deprecated. Please use non-transactional Exercises instead." / "Webhooks are automatically deactivated if they fail to deliver data for 7 days" / "Status code 403 Forbidden is returned if user has not given consent to all mandatory data types"
- **Date:** changelog 2025-08-18, 2026-01-13, 2023-06-28
- **Source type:** vendor_docs
- **In KB:** no. Profile lines 138 and 147 cite the 13.01.2026 changelog date but not the deprecations or the webhook auto-deactivation rule.

### 8. data_residency / ai_training_terms: Flow data is stored in Ireland and Sweden; de-identified data is used for Polar R&D
- **Found:** Privacy notice (updated 14 January 2026): service data is stored on EU/EEA servers in Ireland and Sweden, with email or user ID occasionally sent outside the EU for notifications or error reporting. Polar may use data, cleared of identifiers "to the maximum amount possible", in its own R&D; users can opt out of R&D use of telemetry logs. No AI or machine-learning wording (searched "artificial intelligence", "machine learning", " AI ").
- **URL:** https://www.polar.com/en/legal/privacy-notice
- **Quotes:** "The actual service data (your account details and the data coming from your Polar devices) is stored on servers located in the EU/EEA area; Ireland and Sweden" / "We may use some of the data in research and development work to improve our services, but for such purposes data is cleared from identifiers to the maximum amount possible." / "This Privacy Notice was updated on January 14, 2026."
- **Date:** 2026-01-14
- **Source type:** vendor_legal
- **In KB:** no. Profile line 178 says "Certifications and data residency were not checked"; matrix line 255 residency "Not checked".

### 9. subscription_price: Polar now sells an optional Fitness Program subscription
- **Found:** Polar Flow's Fitness Program (launched April 2025 per press coverage) is free to try, then EUR 9.99 a month, and needs a Polar watch. Core features remain free. Polar Loop (launched 3 Sep 2025, EUR 179.90 / GBP 149.50 / USD 199.90) is marketed as subscription-free and is SDK-accessible through `Polar360.md`.
- **URL:** https://www.polar.com/en/fitness-program ; https://polar.com/en/media-room/polar-launches-polar-loop-first-screen-free-subscription-free-wearable
- **Quotes:** "Try for free, then 9,99 €/month" / "Retail price: EUR 179.90 / GBP 149.50 / USD 199.90" / "SEPTEMBER 3, 2025"
- **Date:** read 2026-10-11; Loop release 2025-09-03
- **Source type:** vendor_page
- **In KB:** no. Profile line 184 "**No subscription** for core functionality" is still true but omits the paid tier; matrix line 228 subscription "**None**". Loop price is not in the profile (matrix lines 132 and 140 say "Price not in profile" for Polar 360).

### 10. iso27001 / soc2: Polar holds ISO 9001 (Kiwa, valid to 2028-08-31), not an information-security certificate
- **Found:** Polar publishes an ISO 9001:2015 certificate for Polar Electro Oy from Kiwa, issued 2025-06-25, valid until 2028-08-31, covering design, marketing and sales of heart rate monitors and service and software production. No ISO 27001 or SOC 2 evidence was found (see below).
- **URL:** https://polar.com/img/documents/iso/ISO_9001_Certification_PEOY_en.pdf
- **Quote:** "The certificate is valid until 2028-08-31."
- **Date:** issued 2025-06-25
- **Source type:** certificate
- **In KB:** no. Profile line 178 "Certifications ... were not checked"; matrix line 255 "Not checked". Useful as evidence of absence for iso27001/soc2, not as a security certification.

### 11. research_program: Polar Research Library 2025 update (vendor usage counts)
- **Found:** Polar's newsroom says the Research Library added 1,958 studies published in 2025 (up 25% on 2024), and the H10 appeared in nearly 800 of them, often as the reference device. The business page claims 17,500 published studies and "6000 API partners". Vendor claims; method not stated beyond indexing in PubMed Central, ScienceDirect, Scopus and SpringerLink.
- **URL:** https://www.polar.com/en/media-room/polar-research-library-update-adds-record-number-scientific-studies-in-2025 ; https://www.polar.com/en/business
- **Quotes:** "adds 1,958 studies published in 2025 alone, a record-breaking number and a 25% increase compared with 2024" / "The Polar H10 alone appeared in nearly 800 studies, increasing 55% year over year, and was often used as a reference device." / "6000 API partners"
- **Date:** release undated on page (covers 2025 publications); read 2026-10-11
- **Source type:** vendor_page
- **In KB:** no (stale). Profile lines 20, 191 and 192 carry only the 2022 to 2023 "600 studies" and "1,000 papers per year" figures.

### 12. research_program: Seppo Säynäjäkangas Science Foundation (2026 call open)
- **Found:** Polar's founder's foundation funds research by students; 2026 applications run 1 Sep to 31 Oct 2026. Eligibility is narrow: Finnish citizens studying at a university in northern Finland. Not an access route for most researchers, but it is a Polar-linked grant.
- **URL:** https://www.polar.com/en/foundation
- **Quotes:** "You are a Finnish citizen" / "You are currently a student in a recognized university in northern Finland"
- **Date:** read 2026-10-11
- **Source type:** vendor_page
- **In KB:** no.

### 13. developer_program_status / academic_vs_commercial: Polar 360 is sold B2B as a white-label platform with SDK and API
- **Found:** The Polar for Business Polar 360 page pitches a screenless band that organisations can build their own apps on via the SDK, or connect via the API; contact is through a B2B form, with no public pricing.
- **URL:** https://www.polar.com/en/business/polar-360
- **Quote:** "Build your own app from scratch, or integrate Polar 360's powerful data into existing ecosystems seamlessly with Polar SDK; or plug ‘n’ play with Polar API."
- **Date:** read 2026-10-11
- **Source type:** vendor_page
- **In KB:** partly. Profile line 171 says "Polar 360 is a screenless band aimed at organisational/health-programme deployments"; route and B2B contact are not described, and no price is recorded.

### 14. deprecations: BLE SDK platform churn in 2026 (breaking major versions, iOS 15 floor, CocoaPods)
- **Found:** Major releases 7.0.0 (Android moved from RxJava to Kotlin Flow, 15 Apr 2026) and 8.0.0 (iOS moved from RxSwift to Combine and Swift Concurrency, 27 May 2026) require app changes. 8.4.0 (1 Oct 2026) notes Xcode 27 dropped pre-iOS 15 support, so 9.0.0 will follow, and urges a move from CocoaPods to Swift Package Manager.
- **URL:** https://github.com/polarofficial/polar-ble-sdk/releases/tag/8.4.0
- **Quote:** "Apple has removed support for pre-iOS 15 versions"
- **Date:** 2026-10-01
- **Source type:** repository
- **In KB:** no. Profile line 138 cites release 8.4.0 only as evidence the SDK is active; lines 162 and 201 say there is "no API deprecation risk" on the raw path. Study apps on the SDK still carry maintenance cost from breaking SDK majors.

### 15. export_routes: H10 internal-recording download is cut off if the sensor leaves the strap
- **Found:** Known issue: the H10 drops BLE 45 seconds after removal from the strap, which cancels reading a long internal recording; workaround is to keep it on a worn strap. Also, ECG/ACC streaming must be stopped by the phone app or the H10 stays on until the battery runs out.
- **URL:** https://github.com/polarofficial/polar-ble-sdk/blob/master/documentation/KnownIssues.md
- **Quote:** "H10 disconnects the BLE connection after 45 seconds timeout when H10 is removed from strap."
- **Date:** read 2026-10-11
- **Source type:** repository
- **In KB:** no. Profile lines 76 and 150 describe H10 internal memory without this operational caveat.

### 16. KB-internal inconsistency: Verity Sense price
- **Found:** Polar US store lists Verity Sense at $104.95, as the profile says.
- **URL:** https://www.polar.com/us-en/products/accessories/polar-verity-sense
- **Quote:** "Polar Verity Sense Optical Heart Rate Sensor $104.95"
- **Date:** read 2026-10-11
- **Source type:** vendor_page
- **In KB:** contradicts within the KB. Profile lines 183 and 186 give $104.95 (2026-10-10); matrix lines 131, 138 and 228 still carry "~$95 (2026-08-21, not re-read)".

### 17. Third-party route (context): RADAR-base integrates Polar Vantage V3 and H10
- **Found:** Already recorded in the Module 2 RADAR-base profile (line 27: Polar Vantage V3 and H10 through the Android pRMT app). Not mentioned in the Polar profile's third-party tools list.
- **In KB:** partly. `module-02-digital-phenotyping/profiles/radar-base.md` line 27 has it; Polar profile line 132 names only Fibion and wearipedia. No new quote taken; source is that profile's source 18.

## Searched, nothing found

- **FDA:** openFDA 510(k) search for applicant "polar electro" and registration/listing for "polar electro" returned no matches; applicant "polar" returned only unrelated firms (Avanti Polar Lipids, Polar Wrap, Polar Latex). No warning letters found. Wrist ECG is labelled not for medical use (finding 3).
- **ISO 27001, SOC 2, trust portal:** no certificate, registry entry or trust page found; Polar's certificate library holds ISO 9001 and ISO 14001 (manufacturing subsidiaries) only.
- **HIPAA / BAA / DPA for researchers:** none in the API agreement or the privacy notice (privacy notice processor role is for Team Pro and GoFit only, as the KB says).
- **AI/ML training terms:** no clause in the API agreement, SDK licence or privacy notice.
- **Academic pricing or discount:** none published; the collaboration process (finding 2) is the only research route.
- **AccessLink changes after 13.01.2026:** none in the changelog; no API shutdown date announced.
- **Company events 2026:** no layoffs, acquisition or developer-programme pause found. Secondary press (the5krunner, 30 Sep 2026) says the announced Flow app rebuild has not shipped; not pursued further.
- **Aggregator integrations (Terra, Thryve, Labfront, Fitabase):** web search returned nothing confirming Polar support; not verified on each vendor's own pages.
- **CE / MDR:** no Polar medical-device CE or EUDAMED entry looked for beyond the wrist-ECG disclaimer; nothing indicating medical-device status.
