# Ultrahuman: gap hunt (baseline fact run, 2026-10-11)

Scope: Ultrahuman Ring AIR / Ring PRO, UltraSignal, Partner API. Compared against
`module-01-wearables/profiles/emerging-platforms.md` (lines 11 to 45), `module-01-wearables/comparison-matrix.md`
(Ultrahuman rows 56, 80, 111, 144, 173, 236, 334, 378, 404) and `facts/ultrahuman.yaml` (every field `unresearched`).

Every quote below returned `exact` from `tools/facts/quote_probe.py` on 2026-10-11, except the three
API Agreement quotes in G4, which are flagged there.

---

## Contradictions and missing programs first

### G1. Raw PPG is available through a self-serve "PPG Recordings API" (Developer Mode), at about 50 Hz
- **Fields:** raw_streams, sampling_rates, export_routes, developer_program_status
- **Found:** Ultrahuman's developer docs (Ultrahuman Vision) list five APIs: Daily Metrics, Home Metrics, PPG Recordings, Blood Test Reports, Blood Test Report Details. The PPG Recordings API returns raw PPG captured by turning on Developer Mode in the Ultrahuman app (Profile, Settings, Developer Mode), as gzip-compressed NDJSON via pre-signed S3 links that expire after 1 hour. The field reference gives the sampling rate as typically 50 Hz. Limits: date range at most 7 days; it returns only the token holder's own recordings, so at present it is a per-account route, not a cohort route. This is a different route from the loaned-kit UltraSignal application the KB describes. The UltraSignal marketing page still describes only the loaned kit.
- **URL:** https://vision.ultrahuman.com/developer-docs?api=ppg
- **Quotes:**
  - "The PPG Recordings API provides access to raw photoplethysmography (PPG) data recorded through Developer Mode on Ultrahuman Ring"
  - "Sampling frequency (typically 50 Hz)"
  - "This API returns only your own PPG recordings (associated with your partner account email)"
  - "Recording data is stored in NDJSON format (gzip compressed)"
  - "Download URLs are pre-signed and expire after 1 hour"
- **Date:** read 2026-10-11 (page shows "v1.0 Live"; no publication date)
- **Source type:** vendor_docs
- **KB has it:** **contradicts.** Profile line 17 says format and rates are not documented and the stream is not called raw; line 21 says sampling rates are "Not documented"; matrix lines 111, 144 ("Not published"), 334 and 378 ("Biostrap and Ultrahuman claims are unproven"); unresolved question Q67 (shared/unresolved-questions.md line 275) asks exactly for the raw PPG sampling rate. The docs answer the "is it raw" and "what rate" parts. Price and scale remain open.
- **Note for judge:** the example payload in the docs shows a download host `ultrahuman-ppg-data.s3.ap-south-1.amazonaws.com` (AWS Mumbai). That is illustrative example JSON, not a residency statement; I did not quote it.

### G2. A self-serve developer portal with personal API tokens and OAuth apps, not only "approved apps"
- **Fields:** developer_program_status, program_application, export_routes, user_cap
- **Found:** vision.ultrahuman.com/developer lets any Ultrahuman account holder create OAuth applications and generate a Personal API token. The personal token can also read other users' data once each user enters the developer's data sharing code under Profile, Settings, Partner ID in the app. This is a third route alongside UltraSignal and the OAuth Partner API, and it is a practical small-study route: participant enters a code, researcher pulls daily metrics by email. Open Wearables' integration guide confirms the self-serve path (sign in with a personal account, create an OAuth app, get client ID and secret), while still headlining "Requires Partnership API access".
- **URLs:** https://vision.ultrahuman.com/developer ; https://vision.ultrahuman.com/developer-docs ; https://openwearables.io/docs/providers/ultrahuman-api-integration
- **Quotes:**
  - "Create an OAuth application to integrate with Ultrahuman's API." (vision.ultrahuman.com/developer)
  - "This token grants access to your own personal data and can also be used to access other users’ data" (vision.ultrahuman.com/developer)
  - "Create your Personal API token from the developer portal" (developer-docs)
  - "Enter the data sharing code provided by the API developer" (developer-docs)
  - "Date range queries cannot exceed 7 days" (developer-docs, Daily Metrics API)
  - "Login requires a personal Ultrahuman account - the same one you use with the Ultrahuman app." (Open Wearables)
- **Date:** read 2026-10-11
- **Source type:** vendor_docs (Ultrahuman Vision); secondary (Open Wearables)
- **KB has it:** **contradicts / no.** Profile line 19 and matrix lines 56, 173 describe only "two routes" and OAuth for "approved apps", with partner-onboarding-issued credentials. No user cap is stated anywhere, so user_cap stays not public.

### G3. Pulsomics: an in-app research program, ethics-approved and CTRI-registered, that also invites academic partners
- **Fields:** research_program, program_eligibility, program_application, program_status, academic_vs_commercial, ai_training_terms
- **Found:** Pulsomics is an opt-in research program in the Ultrahuman app for Ring AIR and Ring PRO users aged 18+. Live studies: Sleep Sufficiency, VO2 Max, Glucose Metabolism; coming soon: Cardiovascular Load, Sleep Journal. The ring records "short windows of raw pulse overnight" paired with questionnaire and uploaded lab data, explicitly to train a "foundational model of the human pulse". Registered with CTRI (CTRI/2026/08/115584); ethics approval from Medstar Speciality Hospital Ethics Committee. Critically for this KB, the page invites institutions: "Universities, hospitals and research groups can work with us on study design, cohort access and co-authored publications", with a "Partner with Ultrahuman" link. Press (Athletech, September 2026) dates the launch to earlier in 2026.
- **URL:** https://www.ultrahuman.com/pulsomics/ ; https://athletechnews.com/ultrahuman-70-million-funding-qualcomm/
- **Quotes:**
  - "Universities, hospitals and research groups can work with us on study design, cohort access and co-authored publications."
  - "Registered with the Clinical Trials Registry – India: CTRI/2026/08/115584."
  - "It holds ethics committee approval from Medstar Speciality Hospital Ethics Committee"
  - "The ring records short windows of raw pulse overnight."
  - "Data is de-identified before use, never sold, never shared with advertisers, employers or insurers."
  - "includes participation from Qualcomm Ventures, Labcorp, Alpha Wave, Blume, Nexus and Alteria" (Athletech, for the funding context)
- **Date:** page read 2026-10-11; CTRI number implies August 2026 registration
- **Source type:** vendor_page; secondary
- **KB has it:** **contradicts.** Profile line 31 says "No academic program is published"; matrix line 404 says "No academic programme". The partner offer has no published terms, price or eligibility; the KB should say a research-partnership route now exists, terms not public.

### G4. The API Agreement for Developers and Partners exists and sets fee, retention, benchmarking and termination terms
- **Fields:** api_platform_fees, retention_terms, ai_training_terms, rate_limits, minimum_commitment, deprecations
- **Found:** Linked as "API Terms" from the Ultrahuman Vision developer pages and from the ultrahuman.com footer. Contracting party: Ultrahuman Healthcare Private Limited (India). Key terms: Sandbox and Production access are free and "as-is", with a paid "Premium Access" for priority support; fees may be introduced on 30 days' notice; partners must not store data beyond what is necessary for legitimate use; all data transmitted via the API "remains the property of the Company"; no redistribution; **no use of the API or its data "to conduct research, analysis, or competitive studies against Ultrahuman or its products"** (a benchmarking clause that could catch validation studies); either party may terminate on 30 days' notice; usage is subject to unpublished "reasonable limits". The agreement says nothing about AI or ML training by partners.
- **URL:** https://ultrahumanapp.notion.site/API-Agreement-for-Developers-and-Partners-120755317a9180999ce3edcfc1047f58
- **Quotes:** **NOT probe-confirmed.** The page is a JavaScript-rendered Notion page; `quote_probe.py` gets 7 characters ("Notion"). I read the text verbatim from Notion's public `loadPageChunk` JSON for the same page id. The following strings are copied from that JSON, not reconstructed, but the judge should re-check them in a browser before they go in a record:
  - "Both Sandbox and Production Access are provided on an unpaid, as-is basis."
  - "Partners may not use the API or its data to conduct research, analysis, or competitive studies against Ultrahuman or its products."
  - "Partners shall not collect, store, or distribute any data retrieved via the API beyond what is necessary for the legitimate use of the API."
- **Date:** read 2026-10-11; no effective date on the page
- **Source type:** vendor_legal
- **KB has it:** **no.** Profile line 33 says "No retention, AI-training or data-sharing terms were read"; matrix line 404 "Not read, Unclear"; matrix line 236 lists API fees "Not disclosed".

### G5. US import ban on Ring AIR (ITC 337-TA-1398), and Ring PRO's conditional clearance by CBP
- **Fields:** deprecations, program_status (availability), device_price
- **Found:** The ITC found Ring AIR infringed Oura patents; the limited exclusion order issued 21 August 2025 took effect after presidential review on 21 October 2025. Ring AIR can no longer be imported into the US; retailers may sell remaining stock; Ultrahuman says it still supports existing owners. On 6 March 2026 CBP ruled (HQ H354023) that the redesigned **Ring PRO** is not subject to the order, conditional on an importer certification CBP must approve, with Oura as an interested party. The US store's `/us/ring/buy/` now sells Ring PRO only. For US studies this means Ring AIR (the device named throughout the KB and on the UltraSignal page) is not purchasable new, and the developer-kit device may differ.
- **URLs:** https://rulings.cbp.gov/docs/hq/2026/h354023 (text via fetch-url https://rulings.cbp.gov/api/ruling/H354023) ; https://www.techradar.com/health-fitness/ultrahuman-smart-rings-have-just-been-banned-in-the-us-but-theres-better-news-for-ringconn-fans
- **Quotes:**
  - "We find that Ultrahuman has met its burden to show that the Ring Pro" (CBP ruling, probed with `--fetch-url https://rulings.cbp.gov/api/ruling/H354023`)
  - "retailers won’t be able to import or stock the Ultrahuman Ring Air beyond what is kept in their existing inventory" (TechRadar)
- **Date:** LEO 2025-08-21; effective 2025-10-21; CBP ruling 2026-03-06
- **Source type:** regulator_db (CBP ruling); secondary (TechRadar)
- **KB has it:** **no.** Profile line 29 only notes that the UltraSignal page title names Ring PRO. Nothing on the ban or the redesign.

### G6. Device price published and no subscription: Ring PRO $479 (US)
- **Fields:** device_price, subscription_price
- **Found:** US store shows Ring PRO total $479 with charging case, and states no recurring fee for data. Premium PowerPlugs (AFib Detection, Cardio Adaptability) are paid add-ons. M2 Live CGM (Abbott Lingo, no prescription) is $99 per month for 2 sensors on subscription.
- **URLs:** https://www.ultrahuman.com/us/ring-pro/buy/ ; https://www.ultrahuman.com/us/pricing/ ; https://www.ultrahuman.com/us/powerplugs/
- **Quotes:**
  - "Total $ 479" (ring-pro/buy)
  - "Rest assured, there are no recurring subscription fees for accessing your data." (ring-pro/buy)
- **Date:** read 2026-10-11
- **Source type:** vendor_page
- **KB has it:** **contradicts.** Profile line 22 "Pricing: Not disclosed"; matrix line 236 "Ultrahuman ... Not disclosed" for device, subscription and API fees.

### G7. Vendor-published accuracy studies and papers now exist (all Ultrahuman-authored)
- **Fields:** (evidence, outside the schema; bears on the profile's Validation row)
- **Found:** ultrahuman.com/science/studies lists accuracy studies by metric with reference and cohort, e.g. sleep stages 62% four-stage agreement against an FDA-cleared EEG home sleep test (23 paired nights), SpO2 97.4% against a clinical pulse oximeter (10 participants), AFib 98.8% against 12-lead ECG (236 in the published study). Publications: Frontiers in Digital Health 2026 (Cardio Age, 442 adults) and two medRxiv preprints (VO2max; Blood Age, 20,858 adults); every author listed is affiliated with Ultrahuman Healthcare Pvt Ltd. An Ultrahuman blog (2026-09-25) reports an independent Journal of Circadian Rhythms study by Matthew Driller's group using Ring AIR after EEG validation; I could not locate the paper itself. PubMed "ultrahuman" returns only the Frontiers paper and a 2024 Sci Rep M1 CGM paper as relevant hits.
- **URLs:** https://www.ultrahuman.com/science/studies/ ; https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2026.1842633/full ; https://www.ultrahuman.com/blog/new-study-reveals-that-your-wearable-knows-how-you-slept-better-than-you-do/
- **Quotes:**
  - "Sleep stages , 62% four-stage agreement , measured against an FDA-cleared home sleep test (EEG) , 23 paired nights"
  - "Blood oxygen , 97.4% blood oxygen agreement , measured against a clinical pulse oximeter , 10 participants"
  - "Ultrahuman Healthcare Pvt Ltd., Bangalore, India" (Frontiers author affiliation)
  - "The study, published in the Journal of Circadian Rhythms , was led by Matthew Driller and colleagues, an independent research group" (Ultrahuman blog)
- **Date:** read 2026-10-11
- **Source type:** vendor_page; paper
- **KB has it:** **partly contradicts.** Profile line 23 and matrix line 334 say "No independent PSG or ECG validation located". Still true for independent PSG validation, but the KB should note vendor-run studies now exist, with small cohorts for several metrics.

### G8. Ultrahuman claims "ISO27001, GDPR, and HIPAA compliant"; its privacy policy says it is not a HIPAA covered entity
- **Fields:** iso27001, hipaa_statement, gdpr_statement, data_residency, retention_terms
- **Found:** Site-wide footer claims ISO 27001, GDPR and HIPAA compliance. No certificate, trust portal or registry entry found. The privacy policy (last updated 13 September 2026) says Ultrahuman is not a HIPAA covered entity and "strive[s] to comply"; names AWS, Snowflake and MongoDB Atlas in the US for storage; keeps de-identified data longer for research; and lists ML development "with your consent" as a purpose. Self-claims, so capped at Corroborated without a certificate.
- **URLs:** https://www.ultrahuman.com/us/for-work/ (footer, any page) ; https://www.ultrahuman.com/us/privacyPolicy/
- **Quotes:**
  - "ISO27001, GDPR, and HIPAA compliant."
  - "We do not provide medical care or advise and are thus not a Covered Entity under HIPAA"
  - "for the purposes of storage such as including AWS, Snowflake and MongoDB Atlas in the United States"
  - "We may keep de-identified data for research and statistical purposes for a longer period."
  - "Developing machine learning algorithms and tools to improve targeting of Products and Services, and other products and services we offer you, with your consent."
- **Date:** read 2026-10-11
- **Source type:** vendor_page; vendor_legal
- **KB has it:** **no.** Ultrahuman has no row in the compliance table (matrix line 247 onward); profile says nothing on compliance.

### G9. Security incident, 27 March 2026 (filed with the California Attorney General)
- **Fields:** (compliance evidence; bears on hipaa_statement / iso27001 credibility)
- **Found:** Unauthorised read-only access to an internal analytics system on 27 March 2026; affected data included contact and account details, order history and "some fitness related data". Users were notified about June 2026. Press (TechCrunch via secondary outlets) attributes entry to credentials stolen from an employee's malware-infected laptop; not confirmed here from a primary source.
- **URL:** https://oag.ca.gov/system/files/security-notice.pdf
- **Quotes:**
  - "On 27 March 2026, we had a security incident"
  - "the affected dataset contained your contact and account details, your order and transaction history, and some fitness related data associated with your product usage and purchases"
- **Date:** incident 2026-03-27; notice about June 2026
- **Source type:** regulator_db (state AG breach filing, company-authored letter)
- **KB has it:** **no.**

### G10. FDA: one establishment listing, no clearance; AFib relies on FibriCheck and is not offered in the US
- **Fields:** fda_clearances
- **Found:** openFDA has no 510(k) under applicant or device name "ultrahuman". The registration and listing database shows "UltraFactory - Ultrahuman Manufacturing Facility" (registration 3033531398, Bengaluru address) listing "Ultrahuman Fertile Window", product code LHD, class U, created 2024-11-12, no premarket number. Same pattern the KB records for Oura's Fertile Window. The AFib Detection PowerPlug is not available in the US per Ultrahuman's own FAQ; press says it is powered by FibriCheck's clearance (not verified here).
- **URLs:** https://api.fda.gov/device/registrationlisting.json?search=registration.name:ultrahuman&limit=5 ; https://www.ultrahuman.com/us/powerplugs/
- **Quotes:**
  - "Ultrahuman Fertile Window" (openFDA registration listing)
  - "We're soon looking to launch in USA, UAE, and India." (PowerPlugs FAQ, on AFib Detection)
- **Date:** read 2026-10-11
- **Source type:** regulator_db; vendor_page
- **KB has it:** **no** (fda_clearances unresearched; profile silent).

### G11. Partner API token lifetime: the docs contradict themselves (a week vs 1 day)
- **Fields:** export_routes, rate_limits
- **Found:** The OAuth docs say access tokens are "valid for a week" and, a line later, "Expiration: 86400 seconds (1 day)". The KB states about a week. Scopes `profile`, `ring_data`, `cgm_data` as in KB. No rate limit is published for the Partner API.
- **URL:** https://vision.ultrahuman.com/developer-docs?type=oauth
- **Quotes:**
  - "They are issued after a successful token exchange and are valid for a week, post week they need to be refreshed"
  - "Expiration: 86400 seconds (1 day)"
- **Date:** read 2026-10-11
- **Source type:** vendor_docs
- **KB has it:** **contradicts (partly).** Profile line 19 and matrix line 173 say tokens "last about a week"; record as conflict.

### G12. Official MCP server, with a published (cost-weighted) rate-limit behaviour
- **Fields:** export_routes, rate_limits
- **Found:** Remote MCP server at api.ultrahuman.com/mcp, OAuth 2.1 with PKCE, read-only, per-user (returns only the signed-in user's data). Rate limiting is cost-weighted per user with HTTP 429 and Retry-After; no numeric budget. Not a research route (single user), but relevant to the KB's Oura MCP comparison.
- **URL:** https://vision.ultrahuman.com/developer-docs?type=mcp
- **Quotes:**
  - "Rate limiting: cost-weighted per user; over budget returns HTTP 429 with Retry-After"
  - "Server URL: https://api.ultrahuman.com/mcp"
- **Date:** read 2026-10-11
- **Source type:** vendor_docs
- **KB has it:** **no.**

## Other findings (KB lacks, lower priority)

### G13. Aggregator routes: Terra and Open Wearables support Ultrahuman
- **Fields:** export_routes
- **Found:** Terra lists an Ultrahuman integration (body, daily, sleep; glucose included). Open Wearables (open source) integrates via the Partnership API, hourly polling, 30-day default sync, and states workouts are not available from the Partnership API. No Ultrahuman integration found for Fitabase, Labfront or Thryve.
- **URLs:** https://tryterra.co/integrations/ultrahuman ; https://openwearables.io/docs/providers/ultrahuman-api-integration
- **Quotes:**
  - "Terra API integrates with any Ultrahuman device currently supported by Ultrahuman" (Terra)
  - "Workouts / Activities No (not available via Partnership API)" (Open Wearables)
- **Date:** read 2026-10-11
- **Source type:** secondary
- **KB has it:** **no** for Ultrahuman specifically (the aggregator profiles were not checked line by line for an Ultrahuman mention).

### G14. M2 Live: OTC CGM (Abbott Lingo) replaces the prescription route in the US
- **Fields:** device_price, derived_metrics (cgm_data scope)
- **Found:** Launched in the US June 2026, using Abbott's over-the-counter Lingo sensor; M1 Live used FreeStyle Libre and needed a consultation in the US (press). Bears on the KB's "M1 CGM patch" wording (profile line 16, line 37), which names M1 only.
- **URL:** https://femtechinsider.com/ultrahuman-launches-m2-live-glucose-monitoring-platform-with-abbotts-lingo-cgm/
- **Quote:** "integrating glucose data from Abbott's over-the-counter Lingo continuous glucose monitor into its metabolic health platform"
- **Date:** 2026-06-18
- **Source type:** secondary
- **KB has it:** **no.**

### G15. UltraWork (corporate wellness, bulk orders)
- **Fields:** academic_vs_commercial, quote_required
- **Found:** "For Work" page offers bulk orders on request; no price. Not a research program, but the only published organisational purchasing route.
- **URL:** https://www.ultrahuman.com/us/for-work/
- **Quote:** "Bulk orders Request access"
- **Date:** read 2026-10-11
- **Source type:** vendor_page
- **KB has it:** **no.**

---

## Searched, nothing found
- ISO 27001 or SOC 2 certificate, certification-body registry entry, or a trust portal for Ultrahuman (web search; nothing beyond the footer claim).
- BAA or DPA offered to partners or researchers (privacy policy, API Agreement, developer pages, partner pages): none mentioned.
- FDA 510(k) or De Novo under "ultrahuman" (openFDA 510(k) by applicant and device name): none. FDA warning letters: none found in search.
- Independent PSG validation of Ring AIR or Ring PRO (PubMed "ultrahuman", web search): none located; the Driller Journal of Circadian Rhythms paper is reported by Ultrahuman but not located.
- Ultrahuman integrations with Fitabase, Labfront, Thryve: none found.
- Published UltraSignal pricing, kit counts or user caps: none (Q67 remains open on price and scale).
- A published Partner API rate limit: none (only "reasonable limits" in the API Agreement, and MCP's cost-weighted 429 behaviour).
- GitHub: only community projects (MCP servers, dashboards, an Oura vs Ultrahuman comparison repo); no official Ultrahuman SDK repo found.
- Not covered in depth: app-store listings, job postings, conference talks, EUDAMED / CE status of AFib Detection, the India Delhi High Court case (Ultrahuman v Oura), USPTO PTAB review of the '178 patent.
