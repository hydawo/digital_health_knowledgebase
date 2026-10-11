# Withings: gap hunter findings (baseline run, 2026-10-10)

Compared against `module-01-wearables/profiles/withings.md` (profile), `module-01-wearables/comparison-matrix.md`
(matrix) and `facts/withings.yaml` (every field still `unresearched`, so every finding below is "no" for the
yaml). Every quote below returned `exact` from `tools/facts/quote_probe.py` on 2026-10-10 unless the entry
says otherwise.

Abbreviations: KB = knowledge base. "Date" is the source's own date where it has one, else the read date.

## Contradictions

### 1. iso27001 / hipaa_statement / gdpr_statement: independent AFNOR certificates exist, and they say ISO 27001:2022, not 2017
- **Found:** Withings publishes AFNOR Certification certificates. The ISO 27001 certificate (N° 2020/86561.8) is
  to the 2022 version, valid 2026-04-22 to 2029-04-21, and its scope names the Withings Public API, the Withings
  SDK, Withings RPM and the devices, at Issy-les-Moulineaux and Boston. A separate AFNOR certificate covers
  ISO/IEC 27701:2019 (privacy, N° 2023/104367.5, valid 2026-04-24 to 2029-04-23). These are third-party
  certificates, so the self_claim_cap can be lifted for iso27001 (source type `certificate`). The certificates
  say to check the live record on afnor.org; that registry lookup was not done.
- **URLs:** https://media.withings.com/web/med-pro/Certificat-ISO27001.pdf ;
  https://media.withings.com/web/med-pro/certificat-27701.pdf ; linked from https://www.withings.com/uk/en/data-security
- **Quotes:** "NF EN ISO/IEC 27001:2023 (Europe) - ISO/IEC 27001:2022 (International)" / "WITHINGS PUBLIC API" /
  "2026-04-22 Until 2029-04-21" / (27701 cert) "ISO/IEC 27701 : 2019" / (data-security page)
  "ISO 27001:2022, ISO 27701:2019 & HDS"
- **Date:** certificates issued April 2026; read 2026-10-10
- **Source type:** certificate (PDFs); vendor_page (data-security page)
- **In KB:** contradicts. Profile line 159 quotes the developer page's "ISO 27001:2017" and says "No certificate
  registry entry was checked, so none of these is Verified independently"; profile line 262 lists the
  2017-versus-2022 conflict as open; matrix line 249 says "ISO 27001:2017 and HDS stated (C)". The certificates
  resolve the conflict in favour of 2022 and the developer security page is stale. ISO 27701 is absent from the KB.

### 2. data_residency / iso27001: HDS certificate is now v2 and covers a Boston site; health-data backups go to Google Cloud in Dublin
- **Found (a):** the current AFNOR HDS certificate (N° 2020/86563.8, same validity window) is against the HDS v2
  referential, and lists the Boston office for activity 5 (administration and operation of the system holding
  health data). Withings' own data-security page still says HDS "version 1.1 final - May 2018", so the page lags
  the certificate.
- **Found (b):** Withings' HDS guarantee-representations table (March 2026, v1) maps subcontractors: hosting by a
  French provider (BSO, Nanterre), and health-data backups on Google Cloud Storage in the EU (Dublin), encrypted
  with a Withings-held key, with the table flagging access risk under extra-European law for that subcontractor.
  The privacy policy (4 March 2026) says health data is not transferred outside the EEA.
- **URLs:** https://media.withings.com/web/med-pro/certificat-HDS.pdf ;
  https://media.withings.com/web/med-pro/EN_US_Representations_des_Garanties.pdf ;
  https://www.withings.com/uk/en/data-security ;
  https://media.withings.com/web/legal/legal-pdf/privacy-policy/wo-en-withings-privacy-policy-20260304.pdf
- **Quotes:** "Référentiel de certification HDS v2" / "225 FRANKLIN ST US-US BOSTON MA 02111 (activité 5)" /
  (data-security page) "version 1.1 final - May 2018" / (guarantees table) "Mapping of health data transfers to a
  country outside the European Economic Area" / "Google Cloud" / "the encryption key is kept by Withings" /
  (privacy policy) "Your Personal Data is hosted in France and Health Data is not transferred outside the EEA."
- **Date:** certificate statement of applicability 2025-11-04, certificate 2026-04; guarantees table March 2026;
  privacy policy 2026-03-04
- **Source type:** certificate; vendor_legal
- **In KB:** no for the hosting subcontractors, backup location and HDS v2; profile line 144 and matrix line 249
  give only "EU (France) or US medical cloud". The judge should read the guarantees table's GCS row in full
  (the PDF table layout breaks long quotes, so only short fragments probe exact).

### 3. raw_streams: raw ECG waveform IS available through the API (Heart v2 - Get), plus a raw stethoscope signal from BeamO
- **Found:** the Health Data API exposes ECG signal points and a stethoscope audio signal, outside the
  ScanWatch-only Raw Data API. Withings' "All available health data" page lists "ECG Signal" for ScanWatch, the
  BPM line and BeamO, and "Stethoscope" under BeamO. The developer guide documents decoding the stetho signal
  (A-law G.711, 4 kHz). The API reference's OpenAPI spec (in the page's JS bundle) describes Heart v2 - Get as
  providing "the high frequency data of an ECG recording in micro-volt", with ScanWatch at 300 Hz for 30 s,
  BPM Core 500 Hz for 20 s, Move ECG 300 Hz for 30 s, and Stetho v2 - List/Get endpoints. **Those API reference
  wordings could not be quote-probed:** `quote_probe.py` runs the JS bundle through the HTML stripper, which
  destroys it. They were read directly from https://developer.withings.com/assets/js/main.8ae1c0ad.js and need a
  manual check. The plans page puts "FDA/CE cleared biomarkers" including ECG on Advanced Biomarkers only, so
  whether the waveform endpoint works on Start for Free is unclear.
- **URLs:** https://developer.withings.com/developer-guide/v3/data-api/all-available-health-data ;
  https://developer.withings.com/developer-guide/v3/get-signal/decode-stetho-to-pcm ;
  https://developer.withings.com/api-reference/ (operationId heartv2-get, stethov2-get) ;
  https://static.withings.com/content/api/plans/plans.html
- **Quotes:** "ECG Signal Atrial Fibrillation (PPG) Atrial Fibrillation (ECG)" / "Cardiac Assessment ECG Signal
  AFib Detection Respiratory Stethoscope" / "Signal is A-law G 711 encoded with a sample rate of 4khz and each
  sample of 16 bit" / (plans) "FDA/CE cleared biomarkers ECG, AFib, SpO₂, vascular age, AHI, EDA/NHS ✗ ✗ ✓"
- **Date:** read 2026-10-10
- **Source type:** vendor_docs
- **In KB:** contradicts. Profile line 52 says ECG is "a device feature rather than a raw stream"; profile line 76
  "ECG raw waveform Not mentioned as available"; open question line 255 "Is raw ECG waveform available under
  any agreement?"; matrix line 105 "Not in the Raw Data API"; Summary line 22 and Limitations line 220 frame
  raw data as ScanWatch-only. The stethoscope signal is absent everywhere.

### 4. research_program / derived_metrics (active collection): Withings has an on-device questionnaire API (Patient Insights)
- **Found:** "Patient Insights" questionnaires run on the BPM Pro 2 touchscreen, are managed and retrieved through
  survey and answers endpoints, can be triggered by thresholds, schedules or once, draw on a Withings library,
  and Withings will build custom questionnaires on request. The plans page gates "Symptom tracking &
  questionnaires" to Advanced Biomarkers.
- **URLs:** https://developer.withings.com/developer-guide/v3/integration-guide/surveys/surveys-overview ;
  https://developer.withings.com/developer-guide/v3/integration-guide/surveys/surveys-library ;
  https://static.withings.com/content/api/plans/plans.html
- **Quotes:** "Patient Insights are targeted questionnaires displayed on the device’s touchscreen" / "Withings
  offers the option to develop custom questionnaires tailored to your specific requirements" / "Symptom tracking
  & questionnaires ✗ ✗ ✓"
- **Date:** read 2026-10-10
- **Source type:** vendor_docs; vendor_page
- **In KB:** contradicts. Profile line 103 "Active Data Collection: None native"; Limitations line 227 "No
  survey/EMA capability"; Poor-fit line 247. Matrix line 183 only notes "Advanced Biomarkers plan lists
  questionnaires". No schema field fits exactly; nearest is derived_metrics or research_program.

### 5. export_routes: Withings does offer a mobile SDK (contract), and more contract-only routes than the KB lists
- **Found:** Withings' agent-onboarding reference lists, besides the contract-free Public API, contract-only
  routes: Cellular Dropship and Bulkship, SDK (Dropship and Bulkship), Withings RPM and OnSite Mode. The SDK
  embeds device setup in the partner's own iOS or Android app. The sitemap also shows a Features API (switch
  device features on or off), Program Member ID (scale user attribution on Body Pro 2) and Health Nudges.
- **URL:** https://developer.withings.com/llms.md ; https://developer.withings.com/sitemap.xml
- **Quote:** "Embed Withings SDK (iOS / Android) into your mobile app"
- **Date:** read 2026-10-10
- **Source type:** vendor_docs
- **In KB:** contradicts (partly). Profile line 139 says "No device SDK; devices are not programmable". The SDK is
  a setup and sync SDK, not device programming, so the second half may stand; the first half is wrong. The plans
  page's own "SDK" exemption (profile line 26) already hints at it.

### 6. retention_terms: inactive-account deletion, 3 years in the French terms versus 10 years in the privacy policy
- **Found:** the French General Terms (last updated 5 January 2026) say Withings deletes inactive accounts, defined
  as no login and no device sync for more than three years. The global English privacy policy (4 March 2026)
  defines inactive as 10 years, with a 90-day email warning. For a longitudinal study using participants' own
  accounts, the deletion rule matters. The English US terms page served on 2026-10-10 is an older version
  (Part 1 last updated 26 January 2023) and has no inactive-account clause.
- **URLs:** https://www.withings.com/fr/fr/legal/api-terms-of-use ;
  https://media.withings.com/web/legal/legal-pdf/privacy-policy/wo-en-withings-privacy-policy-20260304.pdf
- **Quotes:** "Un Compte Inactif est tout compte qui ne s'est pas connecté depuis plus de trois (3) ans" /
  "Dernière mise à jour : 5 janvier 2026" / "Your Withings App account will be considered inactive if for 10 years"
- **Date:** 2026-01-05 and 2026-03-04
- **Source type:** vendor_legal
- **In KB:** no (KB says retention is not published, profile lines 121 and 133, matrix line 391). Record as
  conflict.

## Missing from the KB

### 7. fda_clearances: 2023 Class II recall of ScanWatch ECG, plus a 2018 BPM recall
- **Found:** FDA recall Z-1280-2023 (event 91523, initiated 2022-12-19) for Scan Monitor/ScanWatch: a software bug
  skipped the physician activation and review of ECG that the clearance requires. Also Z-2829-2018 for the Nokia
  BPM+ (Withings-era) failing systolic requirements. No warning letter was found.
- **URL:** https://api.fda.gov/device/recall.json?search=recalling_firm:withings&limit=50
- **Quotes:** "A software bug eliminated the initial ECG activation and review of the ECG under a physician." / "Z-1280-2023"
- **Date:** 2022-12-19 (recall initiated)
- **Source type:** regulator_db
- **In KB:** no. Profile line 160 lists 510(k)s only.

### 8. fda_clearances: BPM Pro 2 announced as FDA-cleared (Dec 2024) but has no Withings-applicant 510(k) in openFDA
- **Found:** Withings Health Solutions' press release (18 Dec 2024) says BPM Pro 2 is FDA-cleared. openFDA 510(k)
  searches by applicant "withings" and device name "withings" return eight records, none of them BPM Pro 2 (the KB
  list is complete for those queries; device name searches "BPM Pro" and "WPM07" return nothing). The clearance is
  probably held by an OEM under another name. The judge should not add it without the K number from the FDA
  database. Also: openFDA lists K121971 "WITHINGS, SMART BODY SCALE" (2012) under applicant Zhongshan Transtek,
  which the KB's applicant-only search missed.
- **URLs:** https://insider.fitt.co/press-release/withings-bpm-pro-2-is-now-fda-cleared-and-named-ces-2025-innovation-awards-honoree-for-digital-health/ ;
  https://api.fda.gov/device/510k.json?search=device_name:withings
- **Quote:** "is now FDA-cleared"
- **Date:** 2024-12-18
- **Source type:** secondary (reprinted vendor press release); regulator_db for the openFDA absence
- **In KB:** no. Profile line 160 and matrix line 249 omit both BPM Pro 2 and K121971.

### 9. subscription_price: Withings+ price, now needed per participant on the free API plan
- **Found:** Withings+ costs €9.95 / $9.95 / £8.95 a month or €99.95 / $99.95 / £89.95 a year (FAQ updated
  14 Oct 2025). This is the per-participant cost for a Start for Free study recruiting new accounts after
  12 October 2026.
- **URL:** https://support.withings.com/hc/articles/8986672043153
- **Quote:** "a monthly rate of €9.95 / $9.95 / £8.95 per month or a yearly rate of €99.95 / $99.95 / £89.95 per year"
- **Date:** 2025-10-14
- **Source type:** vendor_page (support)
- **In KB:** no. Profile line 166 says the membership price "was not read"; matrix line 226 "price not read".

### 10. deprecations: Withings' published change-notice policy, and the Advanced Research API integration guide has gone
- **Found (a):** major breaking changes get one month's notice, up to three months for business-critical ones;
  emergency changes up to two weeks with no notice. Changes are tracked on a developer updates portal and
  mailing list, and the app's registered contact email is subscribed automatically.
- **URL:** https://developer.withings.com/developer-guide/v3/maintain-your-integration/understand-our-timeline-for-notice ;
  https://developer.withings.com/developer-guide/v3/maintain-your-integration/track-changes-on-our-services
- **Quotes:** "One month - Up to three months for a Business Critical change" / "previous version of the services
  may become deprecated or forbidden"
- **Found (b):** the "Advanced Research API Integration Guide"
  (`/developer-guide/v3/integration-guide/advanced-research-api/advanced-research-api-overview`) now returns a
  302 redirect to the Partner Hub home page and is absent from the sitemap, though search engines still index
  it. The Research APIs overview and Raw Data pages still return 200. No quote possible (the page is gone);
  evidence is the redirect, observed 2026-10-10. It may mean the guide moved behind login or the programme is
  being reworked; worth watching.
- **Date:** read 2026-10-10
- **Source type:** vendor_docs
- **In KB:** no for both.

### 11. rate_limits / retention_terms: polling guidance and token lifetimes
- **Found:** Withings tells integrators not to poll more than once every 10 minutes per user. Refresh tokens last
  a year, and an old one dies 8 hours after rotation. A study that misses a year of refreshes loses access
  without the participant re-consenting.
- **URL:** https://developer.withings.com/llms.md
- **Quotes:** "Do not poll more than once every 10 minutes per user" / "(after rotation, the previous token
  becomes invalid after 8 hours)"
- **Date:** read 2026-10-10
- **Source type:** vendor_docs
- **In KB:** no. Profile line 133 and matrix line 164 carry the plan rate limits only.

### 12. user_cap: the 10-user cap is a starting cap, lifted by an application form
- **Found:** Withings' API plans form says every free-plan app starts at 10 users and asks for a privacy policy
  link and client ID to scale.
- **URL:** https://www.withings.com/pages/withings-api-plans-form
- **Quote:** "Every app on the Free API plan starts capped at 10 users so you can build, test, and validate."
- **Date:** read 2026-10-10
- **Source type:** vendor_page
- **In KB:** yes in substance (profile line 120 "more after a Withings review"); adds the application route.
  Search snippets elsewhere quote older caps (5,000 users and 120 requests/minute; 1,000 active users) that are
  not on the current pages; the KB already flags the 120 req/min figure as Reported (line 133).

### 13. research_program: Withings runs its own in-app research programmes, and Health Solutions offers study-design partnership
- **Found:** the privacy policy lists consent for "our research programs", withdrawn by unchecking "Research
  Center" in the app, and separate processing for anonymisation for research and research in the public interest.
  Withings Health Solutions' research page offers to act as a study-design "thought partner". Withings' own
  research review counts 29 PubMed publications featuring its technology in 2025.
- **URLs:** https://media.withings.com/web/legal/legal-pdf/privacy-policy/wo-en-withings-privacy-policy-20260304.pdf ;
  https://www.withings.com/en-eu/pages/research-clinical-trials ;
  https://www.withings.com/us/en/blog/research/research-year-in-review-2025
- **Quotes:** "Uncheck \"Research Center\" in your notification center" / "Interested in partnering with Withings
  Health Solutions?" / "thought partner" / "29 scientific publications"
- **Date:** 2026-03-04; read 2026-10-10
- **Source type:** vendor_legal; vendor_page
- **In KB:** no for the in-app Research Center and the 2025 publication count; the Health Solutions partnering
  offer is partly in profile lines 107 to 113. The en-eu research page is fetchable, unlike the US path the
  profile reports as 403 (line 122).

### 14. ai_training_terms: consumer-side AI processing uses pseudonymised health data under consent
- **Found:** the privacy policy lists "The use of artificial intelligence algorithms to provide you with a
  personalized experience" over pseudonymised profile and health data, and product improvement "including
  algorithm performance improvement" on pseudonymised data under legitimate interest. This is Withings' own use,
  separate from the partner "AI model training contract" on Advanced Biomarkers.
- **URL:** https://media.withings.com/web/legal/legal-pdf/privacy-policy/wo-en-withings-privacy-policy-20260304.pdf
- **Quote:** "These data are pseudonymized so that they do not allow you to identify yourself directly."
- **Date:** 2026-03-04
- **Source type:** vendor_legal
- **In KB:** no. Matrix line 391 covers the partner contract only.

### 15. api_platform_fees: the developer agreement reserves the right to charge
- **Found:** the Withings Developer Software Agreement (API terms, last updated 12 September 2018, still served)
  reserves the right to charge for the API and change fees at its discretion.
- **URL:** https://www.withings.com/us/en/legal/api-terms-of-use
- **Quotes:** "Your use of the Software may be or may become subject to charges." / "Last updated: 12 September 2018"
- **Date:** 2018-09-12
- **Source type:** vendor_legal
- **In KB:** no. Relevant context for the Withings+ change, which is a fee in practice.

## Searched, nothing found
- New 2026 FDA 510(k) clearances for Withings (openFDA by applicant and device name; Body Scan 2 clearance was
  announced as a goal at CES 2026, no record found).
- FDA warning letters to Withings.
- A formal Withings academic grant or discount programme; no academic price anywhere.
- Published papers that used the Advanced Research API or raw ScanWatch accelerometer or PPG.
- SOC 2 report or statement; ISO 13485 certificate (not on the data-security page).
- Fitabase and Labfront Withings integrations (not found); Terra and Thryve integrate Withings via the web API.
- 2026 Withings Health Solutions clinical-trial partnerships (2026 releases in search results, not opened, were care-delivery deals:
  MedStar concierge, 9amHealth, CMS ACCESS Model, not research).
- History depth or backfill limits for the Public API.
