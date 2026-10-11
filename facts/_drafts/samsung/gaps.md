# Samsung: gap hunter findings (baseline run, 2026-10-10)

Compared against `module-01-wearables/profiles/samsung.md` (profile), `module-01-wearables/comparison-matrix.md`
(matrix) and `facts/samsung.yaml` (all fields still `unresearched`, so every finding below is "no" for the
yaml). Every quote was checked with `tools/facts/quote_probe.py` and returned `exact` on 2026-10-10.

Abbreviations: KB = knowledge base. "Date" is the source's own date where it has one, else the read date.

## Contradictions

### 1. fda_clearances: five Samsung watch features are FDA-authorised; the KB itemises none
- **Found:** openFDA's 510(k) endpoint lists these Samsung Electronics Co., Ltd. records relevant to the watch:
  - K201168, "ECG Monitor App", product code QDA, decision 2020-08-04 (SESE).
  - K230292, "Samsung ECG Monitor Application with Irregular Heart Rhythm Notification", QDA, 2023-05-02 (SESE).
  - DEN230041, "Sleep Apnea Feature", QZW, 2024-02-06 (decision code DENG, a De Novo grant).
  - K240909, "Samsung ECG App v 1.3 (ECG)", QDA, 2024-08-02 (SESE).
  - K261011, "Sleep Apnea Feature (v2.0)", QZW, 2026-07-20 (SESE), regulation 868.2378, Class 2.
  - Out of wearable scope but same applicant: K261187 "Hearing Aid Feature", 2026-07-31 (Air-Conduction Hearing Aid Software).
- **URLs:** https://api.fda.gov/device/510k.json?search=k_number:K201168 ; ...:K230292 ; ...:DEN230041 ; ...:K240909 ; ...:K261011 ; ...:K261187 (each `https://api.fda.gov/device/510k.json?search=k_number:<number>`)
- **Quotes (one per URL, all exact):** "ECG Monitor App" / "Samsung ECG Monitor Application with Irregular Heart Rhythm Notification" / "Sleep Apnea Feature" / "Samsung ECG App v 1.3 (ECG)" / "Sleep Apnea Feature (v2.0)" / "Hearing Aid Feature"
- **Date:** decisions as listed; openFDA data last_updated 2026-09-28
- **Source type:** regulator_db (openFDA). accessdata.fda.gov was not tried; the judge may want it for the record.
- **In KB:** contradicts. Matrix line 247 regulatory column says "Not itemised in the profile"; the profile has no FDA content at all (grep for FDA/De Novo/clear returns nothing relevant). Note the Sleep Apnea Feature v2.0 clearance (July 2026) is new within the last 3 months. Sammobile's Stanford item (finding 5) also refers to the De Novo authorisation.

### 2. api_platform_fees: the partner licence reserves the right to charge for the SDK in future
- **Found:** Appendix 1 clause 4(m) of the Samsung Health Partner Service & SDK License Agreement says Samsung reserves the right to charge for the SDK in future. Clause 12.2 lets Samsung end the whole agreement without cause on 30 business days' notice.
- **URL:** https://developer.samsung.com/health/sensor/sdk-license-partner-service-agreement.html
- **Quotes:** "SAMSUNG reserves the right to charge for use of the SDK in the future." / "Samsung may terminate this Agreement (including all Appendices continuing at the time of such notice) upon thirty (30) business days prior written notice to Provider without cause."
- **Date:** read 2026-10-10 (no date on the page)
- **Source type:** vendor_legal
- **In KB:** contradicts (partly). Profile line 157 says "No SDK licence fee is documented. The gate is partner registration for distribution, not payment"; profile line 178 says "No subscription, no API fee"; matrix lines 221 and 389 say "No SDK fee documented" / "No fee documented". True today, but the reservation and the without-cause termination are absent, and they matter for multi-year studies.

### 3. retention_terms / export_routes: Samsung may collect information about the partner's service, and partners must get user consent for it
- **Found:** The same Appendix 1 clause 4(m) says that, in connection with the licensee's use of the SDK, Samsung may collect and use information about the Service and its use, and the licensee must obtain user consent for that. The agreement also names research as a licensed purpose, bars use or disclosure of user data to third parties for advertising, and forbids public statements about the T&C without approval.
- **URL:** https://developer.samsung.com/health/sensor/sdk-license-partner-service-agreement.html
- **Quotes:** "SAMSUNG may collect and use information about the Service and use of Service" / "Licensee shall obtain all consents from the users of the Service necessary for SAMSUNG to use the foregoing information for the purpose of improving SDK" / "for use in connection with the development of applications and Services, research" / "PROVIDER IS NOT PERMITTED TO USE OR DISCLOSE USER DATA TO THIRD PARTIES FOR PURPOSES OF ADVERTISING" / "Licensee must not issue any press releases or make any other public statements relating to this T&C"
- **Date:** read 2026-10-10
- **Source type:** vendor_legal
- **In KB:** contradicts (partly). Profile line 103 says "no Samsung cloud copy ... because no Samsung server is in the path"; matrix line 247 and 371 treat the Sensor SDK as having no vendor in the path. The clause covers information about the service and its use (scope undefined, possibly telemetry rather than sensor data), but a consent obligation for Samsung's use exists and belongs in the participant consent form. Profile line 153 says publication restrictions "were not found ... but the agreement was not read clause by clause"; the press-statement clause is about the T&C, not research findings, so it does not bar publishing results.

### 4. research_program: Samsung runs direct institutional research collaborations and, since June 2026, a "research platform" offered through a CRO
- **Found (a), Alcedis, 24 June 2026:** Samsung announced a partnership with Alcedis, a digital-first CRO (part of Huma, per TechRepublic), describing "Samsung's research platform" with faster study setup, fine-grained biosensor control and participant- and device-level biosensor data. Alcedis runs study execution; Samsung supplies devices and research infrastructure. No public sign-up, pricing or eligibility found.
- **URL:** https://www.ledinside.com/news/2026/6/2026_06_25_06 (verbatim repost of the Samsung release; news.samsung.com timed out to the fetcher) ; https://www.techrepublic.com/article/news-samsung-alcedis-galaxy-watch-clinical-trials/
- **Quotes:** "Samsung’s research platform allows for faster study setup with fine-grained control of biosensors and access to participant- and device-level insights and biosensor data with respect to the study and established protocols" / "Alcedis will lead study execution and participant engagement, while Samsung will provide its advanced wearable technology and research infrastructure to support evidence generation." / (TechRepublic) "The company is part of Huma, a global healthcare AI firm."
- **Found (b), Open Innovation Initiative:** announced 5 Oct 2023 at SDC23 with MIT Media Lab, Brigham & Women's, Tulane and Samsung Medical Center; still the umbrella in July 2026 for the UCSF Neuroscape TAH-DA study (finding 5).
- **URL:** https://samsungmobilepress.com/articles/samsung-announces-open-innovation-initiative-with-leading-universities-and-academic-hospitals-to-build-digital-health-ecosystem
- **Quote:** "Samsung Electronics Co., Ltd. today announced a new Open Innovation Initiative at the Samsung Developer Conference 2023 (SDC23) in San Francisco."
- **Date:** 2023-10-05; 2026-06-24
- **Source type:** secondary (repost of vendor release); vendor_page (Samsung Mobile Press)
- **In KB:** contradicts (framing). Profile line 102 says "No separate academic programme or academic tier is published" and line 105 "Research Stack appears dormant"; matrix line 389 says "No academic tier". Both still hold for open application, but the KB is silent on Samsung's active, invitation-style research route (institutional collaborations and a Samsung research platform via a CRO), which is the live alternative to the dormant Research Stack.

## Missing from the KB

### 5. research_program: named Samsung-funded or Samsung-partnered studies, 2025 to 2026
- **Found:** UCSF Neuroscape TAH-DA study (announced 9 July 2026): one year, Galaxy Watch plus Galaxy Tab A9, target 200 adults per decade aged 40 to 89, part of the Open Innovation Initiative. MGH Diabetes Research Center GLP-1 study (28 May 2026): 100 adults starting GLP-1 treatment, Galaxy Watch8 BIA vs DXA. Stanford Medicine sleep apnoea collaboration (Sammobile, April 2025), building on the De Novo-authorised feature.
- **URLs:** https://samsungmobilepress.com/articles/neuroscape-samsung-cognitive-study-partnership ; https://www.engadget.com/2182683/samsung-study-galaxy-watch-8-glp1-ozempic/ ; https://www.sammobile.com/news/samsung-partners-stanford-university-medicine-improve-sleep-apnea-detection-galaxy-watches/
- **Quotes:** "The study advances Samsung’s Open Innovation Initiative" / "with a goal of enrolling 200 adults from each decade of life between the ages of 40 and 89" / (Engadget) "will divide 100 adults just starting GLP-1 treatment into two groups" / (Sammobile) "The study will be led by professor Robson Capasso as principal investigator and professor Clete Kushida as co-principal investigator."
- **Date:** 2026-07-09; 2026-05-28; 2025-04 (Sammobile page; exact day not confirmed)
- **Source type:** vendor_page (Samsung Mobile Press); secondary
- **In KB:** no. Candidates for Module 3 too, once results publish. The MGH release (news.samsung.com) timed out to the fetcher, so Engadget is cited.

### 6. deprecations: Samsung Health SDK for Android deprecated 31 July 2025, end of service in 2028
- **Found:** The legacy phone-side Samsung Health SDK for Android was deprecated on 31 July 2025 and reaches end of service in 2028; Samsung directs partners to the Data SDK.
- **URLs:** https://developer.samsung.com/sdp/news/en/2025/10/30/dev-insight-oct-2025-move-to-samsung-health-data-sdk-as-samsung-health-sdk-for-android-deprecates-and-other-latest-news ; https://developer.samsung.com/health/android
- **Quotes:** "Samsung Health SDK for Android was deprecated on July 31, 2025." / "will reach the end of its service in 2028" / (Android page, Samsung's spelling) "has been depricated as of 31 July, 2025"
- **Date:** 2025-10-30 newsletter
- **Source type:** vendor_docs
- **In KB:** no. Profile describes the Data SDK (lines 31, 112, 122) but never the legacy SDK or its shutdown. Matters for any study or intermediary still on the old SDK.

### 7. program_application / developer_program_status: the Data SDK needs its own partner approval; legacy approvals do not carry over
- **Found:** Samsung's Data SDK process page: developer mode is testing-only, a partner request must be submitted before distribution, and writing to Samsung Health needs an access code. Thryve (integrator) states legacy approvals do not transfer and all apps must reapply; it also reports intraday steps are gone in the new SDK and that Thryve dropped the old SDK on 16 April 2026.
- **URLs:** https://developer.samsung.com/health/data/process.html ; https://developer.samsung.com/health/data/faq.html ; https://docs.thryve.health/thryve-data-sources/samsung-health
- **Quotes:** "Please submit partner request before your app distribution." / "The developer mode is intended only for testing or debugging your app." / "To write health data to Samsung Health from an app, the access code is required." / (FAQ) "register your app by submitting a partner request and providing the correct package name and SHA-256 signature" / (Thryve) "Approvals granted for the legacy SDK do not transfer to the Data SDK." / "all apps - including those that were previously approved - must go through a new partner approval process" / "Intraday step data is not available anymore."
- **Date:** read 2026-10-10
- **Source type:** vendor_docs; secondary (integrator)
- **In KB:** no. Profile line 112 describes the Data SDK route as "Processed metrics, multi-source" with no gate; the partner process (lines 127 to 131) is documented only for the Sensor SDK.

### 8. export_routes / derived_metrics: Data SDK specifics (version, phones, data types, Galaxy Ring source, wellness-only)
- **Found:** Data SDK v1.1.0 needs Samsung Health 6.30.2 or later, runs on non-Samsung Android phones too, reads IHRN, sleep apnoea and skin temperature (read-only), and lets apps identify Galaxy Ring as a data source. Samsung states the data is for fitness and wellness only.
- **URLs:** https://developer.samsung.com/health/data/overview.html ; https://developer.samsung.com/health/data/faq.html
- **Quotes:** "Samsung Health Data SDK requires Samsung Health version 6.30.2 or later." / "It is available on all Samsung smartphones and also non-Samsung Android smartphones." / "Irregular heart rhythm notification" / "Data measured using Samsung Health Data SDK is intended for fitness and wellness purposes only and is not for the diagnosis or treatment of any medical condition." / (FAQ) "can be a Galaxy Watch, Galaxy Ring, Galaxy Fit"
- **Date:** read 2026-10-10
- **Source type:** vendor_docs
- **In KB:** partly. Profile line 82 and 194 say Galaxy Ring access "not established"; the FAQ establishes Ring as a processed-data source via the Data SDK (raw Ring access still unestablished). Matrix line 201 says "Galaxy owners only"; the phone side need not be Samsung.

### 9. ai_training_terms: Samsung Health consumer app AI-training consent (July 2026)
- **Found:** In July 2026 Samsung Health began showing some users a consent screen for using health data (including medication, records and cycle data) for AI training, possibly with human review. After backlash Samsung said withdrawing consent deletes only the separate AI-development dataset, not records or sync. Regions not published. Applies to the consumer Samsung Health cloud (the Data SDK and Health Connect routes source from it), not the Sensor SDK path.
- **URL:** https://www.techrepublic.com/de/article/news-samsung-health-ai-opt-out/ (English text)
- **Quotes:** "asks users to let Samsung use information from Samsung Health to improve health-analysis algorithms and AI features. It also says the process may include human review." / "Only data collected separately for AI development will be removed, Samsung said." / "Samsung has not published a complete list of affected regions."
- **Date:** 2026-07-16
- **Source type:** secondary (Samsung's own notice is in-app; no web copy found)
- **In KB:** no. Matrix line 371 lists the Samsung Sensor SDK as free of AI-training limits, which stays true; nothing covers participants' consumer-cloud data.

### 10. raw_streams / deprecations: Sensor SDK release history, and a new Android 16 permission for raw trackers
- **Found:** v1.4.1 (20 Aug 2025) is a stability patch; v1.4.0 (31 Jul 2025) added EDA_CONTINUOUS and MF_BIA_ON_DEMAND and, for apps targeting Android 16, moved ECG, EDA, PPG and BIA trackers behind a Samsung `READ_ADDITIONAL_HEALTH_DATA` permission. No release in the 13+ months since.
- **URL:** https://developer.samsung.com/health/sensor/release-note.html
- **Quotes:** "1.4.1 - August 20, 2025 This patch version improves operational stability." / "Required permissions to use each HealthTrackerType have been changed for targeting Android 16" / "com.samsung.android.hardware.sensormanager.permission.READ_ADDITIONAL_HEALTH_DATA"
- **Date:** 2025-07-31 and 2025-08-20
- **Source type:** vendor_docs
- **In KB:** partly. Profile cites v1.4.1 (lines 30, 121) without a date; the Android 16 permission (participant permission burden, profile line 146) is absent.

### 11. fda_clearances / CE: EU instructions for use label the ECG app (with IHRN) a medical device
- **Found:** Samsung's EU IFU for the ECG App (v1.2, 2024-12) carries the medical-device symbol, names an EU authorised representative and describes an OTC software-only mobile medical application including IHRN. MDR class and notified body not stated in the text searched; EUDAMED not checked.
- **URL:** https://images.samsung.com/is/content/samsung/assets/nl/apps/samsung-health-monitor/IFU_ECG_EU_v1.2_2024-12_v4.1.pdf
- **Quotes:** "Indicates that this is a medical device." / "Indicate information of authorised representative for EU." / "is an over-the-counter (OTC) software-only, mobile medical application operating on a compatible Samsung Galaxy Watch and Phone"
- **Date:** 2024-12 (document version)
- **Source type:** vendor_legal (labelling)
- **In KB:** no.

### 12. export_routes: integrators now carrying Samsung (Terra privileged route, Fitrockr)
- **Found:** Terra's Android docs claim a privileged Samsung partnership giving direct Samsung Health SDK access without Health Connect, still requiring the customer's own Samsung application. Fitrockr announced Samsung Galaxy Watch and Ring integration (page date not confirmed; search snippet said 26 Jan 2026).
- **URLs:** https://docs.tryterra.co/unified-api/mobile-only-sources/android-kotlin ; https://www.fitrockr.com/?p=23869
- **Quotes:** (Terra) "Terra has a privileged partnership with Samsung that gives you direct access to the Samsung Health SDK" / (Fitrockr) "enabling seamless access to health and activity data from devices such as the Samsung Galaxy Watch and Samsung Ring within the Fitrockr platform"
- **Date:** read 2026-10-10
- **Source type:** secondary (integrator)
- **In KB:** no for Samsung specifically. data-intermediaries.md line 109 lists Samsung among Fitrockr's claimed devices only as a "700+ wearables" claim. Terra's claim is the vendor's own account of its Samsung relationship.

### 13. history_depth: Health Connect route reads only 30 days before first permission by default
- **Found:** Google's Health Connect docs: apps read at most 30 days before the first permission grant unless they request PERMISSION_READ_HEALTH_DATA_HISTORY. Applies to Samsung data reached via Health Connect (profile line 113). Data SDK history depth: not stated on the overview or FAQ.
- **URL:** https://developer.android.com/health-and-fitness/health-connect/read-data
- **Quote:** "By default, all applications can read data from Health Connect for up to 30 days prior to when any permission was first granted."
- **Date:** read 2026-10-10
- **Source type:** vendor_docs (Google, platform)
- **In KB:** no for the Samsung profile.

### 14. Lower priority, for context
- **Xealth acquisition:** Samsung closed its acquisition of Xealth (EHR-embedded digital-health prescribing platform) in October 2025. No quote could be confirmed: Business Wire 404'd, MobiHealthNews and news.samsung.com blocked or timed out. Not quoted; mention only.
- **Medicare App Library:** Samsung Electronics America, 8 Sep 2026: "Samsung Health was recently accepted in the Medicare App Library" (exact; https://samsungmobilepress.com/articles/samsung-health-connected-care-innovation-recognition-medicare-app-library-kill-the-clipboard). Clinical-records consumer feature, not a research route. KB: no.
- **Academic use of the Sensor SDK:** GalaxyPPG dataset (Park et al. 2025, KAIST) chose Galaxy Watch 5 because it "officially supports PPG data export" (exact; https://ic.kaist.ac.kr/publications/papers/park2025galaxyppg.pdf) and released its toolkit. KB: no (profile line 170 cites only CLAID).

## Searched, nothing found
- Research Stack: no deprecation, archive or end-of-support notice anywhere; GitHub API re-checked 2026-10-10, still last push 24 Oct 2024, none archived, zero open issues. v2.0 Beta release notes undated, no support statement.
- Samsung Health ISO 27001 / 27701 / SOC 2: certificates found only for other Samsung services (signage, G-CRM). Nothing for Samsung Health or the SDKs.
- HIPAA / BAA / DPA from partners or integrators for Samsung: none found.
- Sensor SDK partner-approval criteria, turnaround, country limits: Samsung developer forum threads (2022 to 2023, academic refusals and paused intake) exist in search results but returned 404 to the fetcher, so nothing is quoted. No current statement found.
- Data SDK partner request countries, history depth, rate limits: not stated on the overview, process or FAQ pages.
- Labfront and Fitabase Samsung support: nothing found.
- MDR class / notified body for the ECG app: not in the IFU text searched; EUDAMED not checked.
- Samsung warning letters: none found (openFDA 510(k) search only; warning-letter database not searched).
