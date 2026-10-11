# m-Path: gap hunter findings (baseline run, 2026-10-11)

Compared against `module-02-digital-phenotyping/profiles/m-path.md` (profile),
`module-02-digital-phenotyping/comparison-matrix.md` (matrix) and `facts/m-path.yaml` (every field still
`unresearched`, so every finding below is "no" for the yaml). Every quote was checked with
`tools/facts/quote_probe.py` on 2026-10-11 and returned `exact`.

Notes on sources. m-Path's legal pages (`/legal/`, `/data-processing/`, `/subcontractors/`,
`/privacy-policy/`, `/terms-and-conditions/`) load their text by script from `https://m-path.io/LegalPage/*.html`,
so those raw files are the probe URLs. The manual is WordPress; its article list with modified dates is at
`https://m-path.io/manual/wp-json/wp/v2/ht-kb` (126 articles, 37 modified since 2026-09-01). Manual pages
are vendor docs and may overlap the documentation researchers; they are included only where the KB lacks
or contradicts them.

Abbreviations: KB = knowledge base.

## Contradictions

### 1. data_residency / hosting_options: data is on Microsoft Azure in Frankfurt, and the privacy policy still names KU Leuven as host
- **Found:** The manual's Storage page (modified 2026-10-09), the FAQ and the sub-processor list all say survey responses are stored on Microsoft Azure in Frankfurt. Encryption at rest is AES-256 (Azure service-managed keys); databases are backed up daily and kept at most one month. Continuous sensing data, audio, video and uploaded pictures do not go to Azure: they go to a researcher-chosen cloud (pCloud or OneDrive) or the customer's own server by SFTP (see finding 5). The participant privacy policy, however, still lists "The KU Leuven" as server host, and KU Leuven is absent from the current sub-processor list. A 2023 version of the Storage page (search snippet only, not probed) said data was on KU Leuven servers in Leuven and Heverlee, so this looks like a migration the privacy policy has not caught up with.
- **URL:** https://m-path.io/manual/knowledge-base/storage/ ; https://m-path.io/faq/ ; https://m-path.io/LegalPage/subcontractors.html ; https://m-path.io/LegalPage/privacy.html
- **Quotes:** "all survey responses are stored on Microsoft Azure servers located in Frankfurt, Germany" / "The data on our servers is encrypted at rest with AES 256-bit encryption" / "Our databases are backed up daily (maximum retainment of one month)" / "data are stored securely on Microsoft Azure servers in Frankfurt, Germany" / "Microsoft Azure servers located in Germany (Frankfurt)"; privacy policy: "The KU Leuven for hosting the information available on the App"
- **Date:** Storage page modified 2026-10-09; read 2026-10-11
- **Source type:** vendor_docs (manual, FAQ), vendor_legal (sub-processors, privacy policy)
- **In KB:** no for location (profile and matrix never say where data is stored); contradicts in spirit the profile line 7 "KU Leuven-affiliated" framing if a reader infers university hosting. Record `data_residency` as `conflict` (Azure Frankfurt in docs and sub-processor list, KU Leuven in the privacy policy). The Azure ISO 27001 / SOC 2 claims on the Storage page are Azure's, not m-Path's; do not use them for `iso27001` or `soc2`.

### 2. dpa: m-Path publishes a data processing agreement and a sub-processor list
- **Found:** The Legal page links a "Data Processing" document: Annex 1, a GDPR Article 28 DPA with m-Path as processor and the researcher or practitioner as controller. It gives general authorisation for sub-processors with a one-month objection right, says services are provided only in the EU or EEA unless the controller is in a third country, allows controller audits at most twice per contract year at the controller's cost (125 EUR per staff hour), and requires deletion of personal data when services end unless the controller asks for a CSV return at least five days before. A separate Subcontractors page lists Azure, Google Play, Apple App Store, Firebase Messaging, opt-in Firebase Analytics (deleted after 2 months) and Sentry (90 days), and Thryve when the smartwatch add-on is bought. The Legal page also carries a stale banner announcing an update on 1 November 2025.
- **URL:** https://m-path.io/LegalPage/dpa.html (shown at https://m-path.io/data-processing/); https://m-path.io/LegalPage/subcontractors.html (shown at https://m-path.io/subcontractors/); https://m-path.io/legal/
- **Quotes:** "the m-Path Services shall be provided exclusively in the EU or EEA" / "The Processor will delete the above personal data immediately as soon as the provision of services to the Controller has ended" / "at an hourly rate of 125 EUR per staff member" / "Thryve (Thryve.health) to gather smart watch data" / "Data is automatically deleted after 2 months" / "Our legal documents will be updated on November 1, 2025"
- **Date:** undated documents; read 2026-10-11
- **Source type:** vendor_legal
- **In KB:** contradicts. Profile line 98 and matrix line 160 say "No SOC 2, ISO 27001, or DPA-template document was located"; profile line 153 lists "a formal DPA template" as unconfirmed. `dpa` can be `stated`. Also bears on `retention_terms` (deletion at end of service) and `data_residency` (EU/EEA clause).

### 3. ai_training_terms / retention_terms: the Terms grant m-Path a broad licence over all user content, including participants'
- **Found:** Terms and Conditions clause 11.7 gives m-Path an irrevocable, worldwide licence to use content users provide "for any purpose". "User" is defined to include participants and clients as well as researchers. Nothing in the Terms, privacy policy or DPA mentions AI or model training either way. The DPA (finding 2) separately says the processor acts only on the controller's instructions, so the two documents pull in different directions; a judge should decide whether this is a conflict or whether the DPA governs research data.
- **URL:** https://m-path.io/LegalPage/terms.html (shown at https://m-path.io/terms-and-conditions/)
- **Quotes:** "grants m-Path a worldwide, irrevocable, non-exclusive, royalty-free license to use the content for any purpose, including to provide and enhance the m-Path Services" / "shall mean the Client, Participant, Practitioner or Researcher using the m-Path Services"
- **Date:** undated; read 2026-10-11
- **Source type:** vendor_legal
- **In KB:** no. Nothing in the profile or matrix on content licences or training. Suggest `ai_training_terms: unclear` (no AI clause; broad licence present), with this quote, and a question to the vendor.

### 4. research_program / user scale: the research page now says 150+ institutions, not 250+ universities
- **Found:** The research landing page counts users as Researchers 1000+, Institutions 150+, Participants 90000+. The enterprise page gives other totals (App users 110000+). The "250+ Universities" figure the KB cites is no longer on the page.
- **URL:** https://m-path.io/landing/research/ ; https://m-path.io/enterprise/
- **Quotes:** "Institutions 150+" / "Researchers 1000+" / "Participants 90000+" / "App users 110000+"
- **Date:** read 2026-10-11
- **Source type:** vendor_page
- **In KB:** contradicts. Profile lines 7, 126, 134 and 171, and `module-02-digital-phenotyping/sources.md` line 141 carry "250+ Universities". Still a vendor claim, Reported.

### 5. app_availability: both apps are on Google Play
- **Found:** "m-Path" (`io.m_Path.kuleuven`, 50K+ downloads, updated 9 Oct 2026) and "m-Path Sense" (`io.m_Path_Sense.kuleuven`, 1K+ downloads, updated 1 Sep 2026), developer m-Path Software. The same developer also lists the white-label "Booster (PROfeel)" app (`io.profeel.kuleuven`). An Android beta channel exists via Play, and iOS betas via TestFlight.
- **URL:** https://play.google.com/store/apps/details?id=io.m_Path.kuleuven&hl=en ; https://play.google.com/store/apps/details?id=io.m_Path_Sense.kuleuven&hl=en ; https://m-path.io/manual/knowledge-base/join-m-path-beta/
- **Quotes:** "50K+ Downloads" / "Updated on Oct 9, 2026" / "Updated on Sep 1, 2026" / "1K+ Downloads" / "The beta app is not stable"
- **Date:** read 2026-10-11
- **Source type:** app_store
- **In KB:** contradicts. Profile line 10 and matrix line 53 say the Google Play listings were not located (Unclear). Note that the Module 3 Niemeijer profile (line 42) says calls and SMS are left out of the Play Store build of m-Path Sense; current docs (finding 7) list call and text data without that caveat, so that gap is still open.

### 6. raw_streams / hosting_options: continuous sensing data never reaches m-Path; it goes to pCloud, OneDrive or the customer's SFTP server
- **Found:** Sensing Full data, audio, video and uploaded pictures go straight to a researcher-linked pCloud or OneDrive account, or to the researcher's own SFTP server; OneDrive supports direct phone-to-folder upload that bypasses m-Path servers. Storing questionnaire answers on the customer's own servers is possible for an extra development cost. This is the most concrete description found of what the "External servers" add-on covers.
- **URL:** https://m-path.io/manual/knowledge-base/adding-a-cloud-storage-location-for-client-file-uploads/ ; https://m-path.io/manual/knowledge-base/storage/
- **Quotes:** "It is possible to connect two cloud storage providers: pCloud and OneDrive" / "upload this data to your own servers via SFTP" / "Doing so requires an additional development cost"
- **Date:** cloud page modified 2026-10-05, Storage 2026-10-09; read 2026-10-11
- **Source type:** vendor_docs
- **In KB:** contradicts (partly). Profile lines 12, 83, 131, 145 and 157 and matrix line 75 say the External servers scope "is not stated" and list no hosting route other than vendor SaaS. Answers part of profile open question line 157.

## Missing (KB lacks)

### 7. raw_streams: the vendor's own Sensing Full stream list fills most of the profile's Unclear rows
- **Found:** Sensing Full lists app usage and screen activity, accelerometer, gyroscope and light sensor, battery level, Bluetooth and Wi-Fi (cryptographically anonymised), GPS, pedometer and physical activity, and call and text data (cryptographically anonymised). Sensing Lite (regular app, questionnaire-time only) records location (lat, long, altitude, accuracy, speed), noise level, step count and others; it needs a Standard or Comfort subscription. The vendor notes some phones from "Chinese imported brands" block some requests.
- **URL:** https://m-path.io/manual/knowledge-base/full-sensing-vs-sensing-lite-which-do-you-need/ ; https://m-path.io/manual/knowledge-base/mobile-sensing-lite-version/
- **Quotes:** "App Usage and Screen Activity data" / "Accelerometer, Gyroscope and Light sensor data" / "Call and text data (cryptographically anonimized)" / "This has to be purchased additionally to the Standard or Comfort subscription"
- **Date:** comparison page modified 2026-02-17, Lite page 2026-10-05; read 2026-10-11
- **Source type:** vendor_docs
- **In KB:** contradicts the "Unclear" state. Profile table lines 35 to 53 mark accelerometer, gyroscope, ambient light, screen state, app usage, battery, Wi-Fi, calls and SMS Unclear; matrix line 117 lists only GPS, Bluetooth, pedometer and noise. iOS versus Android parity per stream is still not stated.

### 8. raw_streams / api_platform_fees: wearables run through Thryve; Oura costs €3,000 a year extra; research devices are not integrated; Garmin has two raw-data integrations
- **Found:** The standard Smartwatch integration is built on Thryve (Garmin, Fitbit, Apple, Polar named) and returns lower-resolution and computed measures; access lasts for a researcher-set expiry window after connection. Oura is an extra €3,000 per year. Empatica, movisens and ActiGraph are not integrated. Two Garmin-only add-ons skip Thryve: Direct Garmin (via m-Path Sense, configurable sampling, heart rate up to 1 s, raw beat-to-beat intervals, triggers) and Garmin Lite (sync at questionnaire time; needs Standard or Comfort). Data flows to the researcher's cloud. m-Path's about page lists a "Chief Wearable Officer", which fits this push.
- **URL:** https://m-path.io/manual/knowledge-base/wearables/ ; https://m-path.io/manual/knowledge-base/which-wearable-integration-is-right-for-my-project/ ; https://m-path.io/manual/knowledge-base/wearables-garmin-direct-integration/ ; https://m-path.io/manual/knowledge-base/wearables-garmin-lite/
- **Quotes:** "Through the Thryve platform , m-Path supports most commercial wearables, including Garmin, Fitbit, Apple and Polar" / "Oura can be added for €3,000 per year" / "Research devices such as Empatica, movisens and ActiGraph are not integrated" / "heart rate at up to 1-second intervals and raw beat-to-beat intervals (BBI) for HRV computation" / "Raw data collection with customizable sampling rates" / "you need to have a Standard of Comfort subscription for this"
- **Date:** wearables page modified 2026-10-06; Garmin pages 2026-05-18 and 2026-06-02; read 2026-10-11
- **Source type:** vendor_docs
- **In KB:** no. Profile line 111 and matrix line 117 list the €3,000 add-on with Fitbit, Garmin, Apple Watch; no Thryve, Oura surcharge, Garmin direct routes or exclusions. Answers profile open question line 155. Cross-link the Thryve profile (Module 1 or the fact file `facts/thryve.yaml`).

### 9. raw_streams: m-Path Keyboard logs keystrokes on iOS and Android
- **Found:** A custom keyboard records every keystroke or every nth, keyboard events and suggestion use, with data sent from the phone to the researcher and not via m-Path servers. Participants can delete the last 10 minutes. Marketed on the mobile sensing page as sentiment and typing-behaviour analysis without storing raw text.
- **URL:** https://m-path.io/manual/knowledge-base/m-path-keyboard/
- **Quotes:** "Recording every keystroke or configurable intervals" / "sent directly to the researcher, bypassing MPath servers entirely"
- **Date:** modified 2025-12-16; read 2026-10-11
- **Source type:** vendor_docs
- **In KB:** contradicts. Profile line 50 and matrix keep Keyboard as Unclear. Price and add-on status not stated.

### 10. export_routes / licence: two open-source R packages on CRAN
- **Found:** `mpathr` (m-Path Software, GPL-3, v1.0.4, published 2026-02-05) imports dashboard exports and computes response rates; `mpathsenser` (Koen Niemeijer, KU Leuven, GPL-3, v1.2.4, published 2025-11-13) reads m-Path Sense JSON into SQLite. The vendor's GitHub org `m-path-io` has two public repos (mpathr, a preprocessing guide). The mobile sensing page markets this as the "m-Path SenseR package".
- **URL:** https://cran.r-project.org/web/packages/mpathr/index.html ; https://cran.r-project.org/web/packages/mpathsenser/index.html ; https://github.com/m-path-io ; https://m-path.io/mobile-sensing/
- **Quotes:** "Easily Handling Data from the ‘m-Path’ Platform" / "2026-02-05" / "Process and Analyse Data from m-Path Sense" / "2025-11-13" / "Process and analyze your passive sensing data in R with our m-Path SenseR package"
- **Date:** as stated; read 2026-10-11
- **Source type:** repository
- **In KB:** partly. `mpathsenser` appears in the Module 3 Niemeijer profile line 116 and as unresolved question 113 (no decision recorded); `mpathr` appears nowhere. Profile "Derived Metrics" (line 63) and "Data Access and Export" (line 75) say not verified.

### 11. export_routes / user_cap: bulk export is paid-only; the Free tier gets single-participant export
- **Found:** Single-participant export from the Visualize tab on all plans; the advanced multi-participant CSV export (semicolon-delimited) needs a paid subscription.
- **URL:** https://m-path.io/manual/knowledge-base/export-data/
- **Quotes:** "Advanced export requires a paid subscription"
- **Date:** modified 2026-10-05; read 2026-10-11
- **Source type:** vendor_docs
- **In KB:** no. Profile line 75 says export was not verified (the pricing table says "Basic" and "Advanced" export without defining them).

### 12. minimum_commitment / academic_pricing: one-year minimum, 3-month minimum extension, published slot prices beyond 600
- **Found:** No subscription under one year; extensions from 3 months, pro rata. 1,000 slots on Essential is €4,441 a year; extra blocks of 100 mid-term cost €535 (Essential) or €700 (Standard). Prolific recruitment needs a premium subscription.
- **URL:** https://m-path.io/manual/knowledge-base/subscription-length/ ; https://m-path.io/manual/knowledge-base/buying-participant-slots/ ; https://m-path.io/manual/knowledge-base/setting-up-a-study-with-m-path-and-prolific/
- **Quotes:** "It is not possible to buy a subscription for less than one year" / "The smallest possible extension is 3 months" / "1000 participant slots per year cost 4441 Euro" / "Adding 100 new participant slots costs 535 Euro for the essential subscription, 700 Euro for the standard subscription" / "Using Prolific in combination with m-Path is only possible with a Premium Subscription"
- **Date:** modified 2026-10-06 and 2026-03-30; read 2026-10-11
- **Source type:** vendor_docs
- **In KB:** partly. Profile line 112 has one-year access and "extra participant slots can be bought at any time", but no minimum extension, mid-term slot price or 1,000-slot price.

### 13. research_program (organisation): m-Path Software BV, a 2024 KU Leuven spin-off
- **Found:** The about page says m-Path was founded in 2019 and spun off from KU Leuven's Faculty of Psychology in 2024; the operating company is m-Path Software BV (company number 1010.164.730, Leuven). The `mpathsenser` package and the app package names still carry KU Leuven.
- **URL:** https://m-path.io/about/
- **Quotes:** "Founded in 2019, m-Path emerged as one of the pioneering spin-offs from KU Leuven's Faculty of Psychology in 2024" / "Company Number (ondernemingsnummer) 1010.164.730"
- **Date:** read 2026-10-11
- **Source type:** vendor_page
- **In KB:** partly. Matrix line 34 says "KU Leuven spin-off" and profile line 98 has it from a search summary; profile line 7 says "KU Leuven-affiliated research team". Spin-off year and legal entity are missing.

### 14. hipaa_statement / gdpr_statement: more vendor-stated wording, still no BAA
- **Found:** The research page and FAQ restate GDPR and HIPAA compliance and add 2FA support. No BAA, HIPAA policy or US-specific term appears in the Terms, privacy policy, DPA or sub-processor list.
- **URL:** https://m-path.io/landing/research/ ; https://m-path.io/faq/
- **Quotes:** "Our platform complies with GDPR and HIPAA regulations" / "We support two-factor authentication (2FA)"
- **Date:** read 2026-10-11
- **Source type:** vendor_page
- **In KB:** yes for the claim (profile line 98, matrix line 160); no for 2FA. `baa` should be `not_public` with these pages listed as checked.

### 15. Participant experience: Samsung deep sleep stops notifications
- **Found:** On some phones, notably Samsung Galaxy, an unused m-Path is put into deep sleep and stops receiving notifications; the vendor recommends a weekly empty questionnaire in long or burst designs.
- **URL:** https://m-path.io/manual/knowledge-base/deep-sleep/
- **Quotes:** "Apps in deep sleep cannot receive notifications anymore"
- **Date:** modified 2026-06-24; read 2026-10-11
- **Source type:** vendor_docs
- **In KB:** no (profile line 87, Participant Experience, "Not verified"). No schema field; profile note only.

## Searched, nothing found
- FDA, CE or MDR status: no clearance, CE mark or "not a medical device" statement found (web search; no EUDAMED hit). `fda_clearances` likely `not_applicable` or `not_public`.
- ISO 27001 or SOC 2 for m-Path itself: none; only Azure's certificates are cited.
- BAA: none in legal docs or by web search.
- API documentation: none public; the pricing page still only says "Get access to the m-Path API".
- Thryve partner or integration page naming m-Path: none found.
- Newsroom or press releases: the blog (blog.m-path.io) is methods content only, 16 posts in 2026, no product or policy news.
- Deprecations or shutdowns: none found. The Legal page's "update on November 1, 2025" banner is still up; no changelog of what changed.
- Job postings: only "Future Chief Front End Officer" on the about page.
- 2025 to 2026 papers on how researchers got m-Path Sense data: none beyond Niemeijer 2023 (already in Module 3).
- The old `m-path.io/Privacy_Policy_m-Path_Sense.html` (profile line 98) was not re-checked; the current Legal page has a single privacy policy for app and dashboard.
