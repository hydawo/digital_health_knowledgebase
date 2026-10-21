# Thryve gap hunt (baseline fact run)

Gap hunter, 2026-10-11. Every quote below returned `exact` from `python3 tools/facts/quote_probe.py URL "quote"` on 2026-10-11.

KB files compared: `module-01-wearables/profiles/data-intermediaries.md` (profile), `module-01-wearables/comparison-matrix.md`, `facts/thryve.yaml` (all 30 fields `unresearched`, so every finding is new to the record; the "KB has it" column refers to the prose files).

Legal entity for registry lookups: Thryve is mHealth Pioneers GmbH, Berlin. Quote: "Local registry of Charlottenburg HRB 183287 B" (https://www.thryve.health/legal/imprint, vendor_legal, read 2026-10-11).

---

## A. Contradictions and missing programs

### A1. Terve Research: a Huawei-funded, Thryve-operated European research platform (missing program)
- **Fields:** research_program, program_eligibility, program_status, academic_pricing
- **Found:** Announced 31 August 2026 at ESC Congress. Thryve runs it on its white-label research platform; Huawei funds it and says it has no operational role. Two study models: closed studies (researcher recruits, provides devices) and open studies (Huawei watch users across Europe browse and enrol in the app). Participation needs a compatible Huawei device. The Terve site offers researchers ethics-committee and joint-controllership templates, and says selected studies may get sponsored devices and implementation support.
- **Quotes:**
  - "Terve Research is independently managed and operated by Thryve, who also collaborates with researchers to set up and run studies in full compliance with European data protection laws." https://www.thryve.health/news/thryve-huawei-terve-research-partnership (vendor_page, dated 31 August 2026)
  - "The role of Huawei is limited to the contribution of funding, with no involvement in the actual operations." (same URL)
  - "Research teams can also open studies to users of compatible Huawei wearables across Europe." (same URL)
  - "Terve Research is a dedicated digital research platform for European academic and medical institutions." https://www.mynewsdesk.com/dk/huawei-dk/pressreleases/huawei-launches-european-health-platform-terve-research-and-unveils-huawei-watch-d3-3463233 (secondary: Huawei Danmark press release, 31 August 2026)
  - "Selected studies may receive sponsored devices and support for implementation and runtime once Terve launches." https://terveresearch.com (vendor_page, read 2026-10-11)
  - "Participation will require a compatible Huawei device at launch." (same URL)
  - "Huawei has no direct control over the operation of the app or platform, the acceptance or decline of research projects, or overall access to user data." (same URL)
- **KB has it:** no. `data-intermediaries.md:140` describes Thryve only as "EU-based health data API; publishes analysis of the Fitbit API deprecation" (Reported). No mention of Terve anywhere in the repo.
- **Note:** this is also relevant to any future Huawei coverage; Huawei has no profile in Module 1.

### A2. Terve launch status conflicts between sources (program_status)
- **Fields:** program_status
- **Found:** The Huawei release says two studies (social jetlag, led from University Hospital Zurich; activity and cardiovascular risk, led by the ESC programme chair) launch in September 2026. On 2026-10-11 the Terve site still says it is pre-launch and collecting early-access emails, and no Terve app appears in the Apple App Store (iTunes Search API, DE, GB and FI storefronts, 2026-10-11).
- **Quotes:**
  - "two clinical studies launching in September" (Huawei release URL above, 31 August 2026)
  - "We're launching soon." https://terveresearch.com (vendor_page, read 2026-10-11)
- **KB has it:** no. Record as `conflict` or `unclear` on program_status, recheck in 30 days.

### A3. Thryve "Research Partners" application route (missing program)
- **Fields:** research_program, program_application
- **Found:** A "Become a Partner" page with a three-step route: apply, set up the study with Thryve support, run and publish. No eligibility criteria, pricing or review step is published.
- **Quote:** "Tell us about your research first. Get access to Thryve's research infrastructure, documentation, and compliance materials." https://www.thryve.health/research-partners (vendor_page, read 2026-10-11)
- **KB has it:** no (`data-intermediaries.md:140`, `:166`).

### A4. Scale Up plan is restricted to young startups (KB lists it unrestricted)
- **Fields:** program_eligibility, academic_vs_commercial, api_platform_fees
- **Found:** The pricing page limits Scale Up (from €1,000 per month) to startups founded less than 10 years ago, so a university or established research institute would appear to be limited to Start Up (500 users) or bespoke Enterprise. Additional users on Scale Up are €999 per 10,000.
- **Quotes:**
  - "Special plan for startups with growth-stage needs (less than 10 years of founding)." https://www.thryve.health/pricing (vendor_page, read 2026-10-11)
  - "Scale your user base with additional €999 per 10,000 users." (same URL)
- **KB has it:** no. `data-intermediaries.md:166` lists "Scale Up from €1,000 per month for up to 5,000 users" with no eligibility restriction and no overage price; `comparison-matrix.md:407` likewise.

### A5. CASA assessment cost: Thryve's figure differs from the KB's (soft contradiction)
- **Fields:** api_platform_fees, deprecations
- **Found:** Thryve's Fitbit shutdown guide (last updated 29 September 2026) prices CASA at about €1,000 and up, with annual renewal. The KB carries Google's own range of $500 to $4,500 (Verified). Different source and currency, not necessarily wrong, but the judge should keep Google's figure as primary and treat Thryve's as an integrator estimate.
- **Quote:** "typically starts around €1,000 and upwards" https://www.thryve.health/blog/fitbit-shutdown-september-2026-migration-options (secondary/vendor blog, updated 29 September 2026)
- **KB has it:** contradicts (soft), `module-01-wearables/profiles/fitbit-google.md:65`.

---

## B. Compliance

### B1. BAA and DPA standard on every plan
- **Fields:** baa, dpa
- **Found:** Thryve's certifications page says BAAs and DPAs come with every plan, not only Enterprise. Distinguishes Thryve from Terra (BAA only on Enterprise, per KB). Vendor claim; no signed agreement seen, so cap at Reported.
- **Quote:** "Business Associate Agreements and Data Processing Agreements are standard on every plan" https://www.thryve.health/certifications-compliance (vendor_page, read 2026-10-11)
- **KB has it:** partly. `data-intermediaries.md:166` notes only a "Data processing / Business association agreement" row in the plan table, not that it covers every plan.

### B2. ISO 27001 and ISO 9001 claimed, recertified 2025; no independent certificate found
- **Fields:** iso27001
- **Found:** Thryve claims ISO 9001 and 27001 and says it passed recertification in 2025. No certificate number, certification body or registry entry was found for mHealth Pioneers GmbH (web search for the legal name plus ISO terms; nothing returned). A 2020 South African "thryve" ISO 27001 news item (fanews.co.za) is a different company and should not be used.
- **Quote:** "Successfully passed ISO 9001 & ISO 27001 recertification" https://www.thryve.health/updates/2025-year-in-review-thryve (vendor_page, undated, covers 2025)
- **KB has it:** no. The KB cites only the "100% GDPR and HIPAA compliant" FAQ line (`data-intermediaries.md:166`). Self-claim cap applies: Reported at most until a certificate is seen.

### B3. Hosting: German servers with ISO 27017/27018 cloud certification; Terve on T Cloud Public
- **Fields:** data_residency
- **Quotes:**
  - "All data processed and stored by Thryve is hosted in Germany." https://www.thryve.health/pricing (vendor_page, read 2026-10-11)
  - "Data is encrypted and hosted on ISO 27017/27018-certified German servers." https://www.thryve.health/multimodal-clinical-trial-platform (vendor_page, read 2026-10-11)
  - "Hosted on T Cloud Public, Germany" https://terveresearch.com (vendor_page, read 2026-10-11)
- **KB has it:** no.

### B4. Tokenization at ingestion
- **Fields:** gdpr_statement, hipaa_statement
- **Quote:** "Raw health data is tokenized at ingestion" https://www.thryve.health/certifications-compliance (vendor_page, read 2026-10-11)
- **KB has it:** no.

### B5. Not a medical device; no FDA records
- **Fields:** fda_clearances
- **Found:** Thryve says it is not a medical device, while marketing its research product as supporting customers' CE, MDR and FDA documentation. openFDA 510(k) and registration-listing queries for "mHealth Pioneers" and "Thryve" returned no matches (2026-10-11). Suggests `not_applicable` for fda_clearances.
- **Quotes:**
  - "Thryve itself is a data infrastructure platform, not a medical device." https://www.thryve.health/health-ai-chatbots (vendor_page, read 2026-10-11)
  - "Designed to support CE, MDR, and FDA documentation processes for evidence generation." https://www.thryve.health/multimodal-clinical-trial-platform (vendor_page, read 2026-10-11)
- **KB has it:** no.

---

## C. Data access, terms and deprecations

### C1. Historical backfill defaults to 14 days
- **Fields:** history_depth
- **Quotes:**
  - "By default, we allow for the retrieval of 14 days of historic data." https://docs.thryve.health/thryve-product-overview/control (vendor_docs, read 2026-10-11)
  - "Up to 14 days of Fetching historical data" https://www.thryve.health/pricing (Scale Up column; Enterprise "Flexible")
- **KB has it:** no. Matters for studies that want pre-enrolment baselines.

### C2. Fitbit shutdown handling: connections cut within 24 hours, history kept
- **Fields:** deprecations, retention_terms
- **Found:** After Google turns the Fitbit Web API off on 30 October 2026, Thryve disconnects all Fitbit connections within 24 hours; already-ingested Fitbit data stays under the same user ID. New Google Health connections need the customer's own credentials, and unverified configurations are capped at 100 users.
- **Quotes** (all https://www.thryve.health/blog/fitbit-shutdown-september-2026-migration-options, updated 29 September 2026):
  - "Within 24 hours, we will proactively disconnect all Fitbit connections on the Thryve side."
  - "Your historical Fitbit data stays."
  - "Google Health does not permit shared infrastructure."
  - "Until both are complete, you are capped at 100 users on an unverified configuration."
- **KB has it:** partly. Own-credentials requirement and 100-user cap are in `fitbit-google.md:27` and `:59`; the 24-hour disconnect and retention of history are not. Note the post itself is internally inconsistent (header says 30 October; body still says "what happens on 30 September" and "Google has not communicated an extension").

### C3. Legacy Samsung Health module deprecated; users must reconnect
- **Fields:** deprecations
- **Found:** SDK 5.2 replaces `module_shealth` with `module_samsung_health` on Samsung's official Health Data SDK. Existing connections cannot migrate. Release post is undated; SDK 5.1.0 was early 2026 and docs now reference SDK 5.3.0, so 5.2 is mid-2026.
- **Quotes** (https://www.thryve.health/updates/sdk-5-2-update, vendor_page):
  - "Samsung does not support migration of existing user connections."
  - "users upgrading to the new module must reconnect their Samsung Health accounts"
- **KB has it:** no.

### C4. Shared OAuth client: all scopes requested, shared rate limits
- **Fields:** rate_limits, export_routes
- **Found:** By default participants authorize Thryve's shared app, which requests every data scope; bringing your own OAuth client gives scope control and separate rate limits. Relevant to ethics review (data minimisation) and to the Garmin pause (the shared client is how new customers reach Garmin without their own Garmin approval; whether Thryve's Garmin client still accepts new customers was not confirmed anywhere).
- **Quotes** (https://docs.thryve.health/thryve-data-sources/overview/shared-and-custom-oauth-clients, vendor_docs):
  - "When using the shared OAuth clients provided by Thryve, users will be asked to grant access to all data scopes."
  - "API rate limits are tied to the customer’s own developer account, not shared with others"
- **KB has it:** no.

### C5. Garmin Companion SDK module: real-time beat-to-beat intervals over Bluetooth
- **Fields:** raw_streams, sampling_rates
- **Found:** SDK 5.3.0 adds a Garmin Companion module streaming heart rate, BBI (inter-beat intervals), SpO2, respiration, stress, Body Battery and more to the app and Thryve's warehouse. Requires Garmin Connect on the phone. KB's Garmin profile says the Companion SDK is "Available to Garmin Health enterprise partners"; whether a Thryve customer needs its own Garmin licence is not stated (Unclear). This could be a route to Garmin beat-to-beat data during the developer-program pause.
- **Quotes** (https://docs.thryve.health/thryve-data-sources/garmin-health-companion, vendor_docs):
  - "Thryve SDK 5.3.0 provides real-time bluetooth device data integration through the"
  - "requires the Garmin Connect app to be installed on the phone"
- **KB has it:** no (`garmin.md:38` covers Garmin's own Companion SDK, not Thryve's wrapper).

### C6. Fitbit epoch data via Thryve is sparse without intraday partnership
- **Fields:** sampling_rates
- **Quote:** "Almost all epoch data from Fitbit is only provided when users actively record activities or during sleep periods." https://docs.thryve.health/thryve-data-sources/fitbit (vendor_docs)
- **KB has it:** no. Largely moot after 30 October 2026, but applies to any retained legacy data.

### C7. Foundation analytics included at no extra charge
- **Fields:** derived_metrics, api_platform_fees
- **Quote:** "Thryve’s foundational analytics are now available to all clients at no additional charge" https://www.thryve.health/updates/foundation-analytics-now-included (vendor_page, undated)
- **KB has it:** no. Pricing page still shows "Analytics Capabilities: Upon Request", so advanced analytics remain quoted.

---

## D. Research use and deployments

### D1. Pulsatio white-label research app, iOS build not updated since March 2023
- **Fields:** export_routes, program_status
- **Found:** Thryve markets Pulsatio (iOS and Android) as its participant app for enrolment, surveys and wearable connection. The iOS listing (seller mHealth Pioneers GmbH, first released August 2021) shows the latest version as 3.9.8 from 24 March 2023. The public app may be superseded by white-label builds, but the gap is worth noting.
- **Quotes:**
  - "Through the Pulsatio app (iOS and Android), participants can easily enroll, complete surveys, and connect wearables" https://www.thryve.health/multimodal-clinical-trial-platform (vendor_page, read 2026-10-11)
  - "Version 3.9.8 24.03.2023" https://apps.apple.com/de/app/pulsatio/id1575886891 (app_store, read 2026-10-11)
- **KB has it:** no.

### D2. REMIT (German Ministry of Health), mHealth Pioneers named as partner
- **Fields:** research_program (evidence of use)
- **Found:** Independent government listing names mHealth Pioneers GmbH among REMIT partners (post/long-COVID remote monitoring, led by University Hospital Jena, runtime 1 November 2024 to 1 January 2029). Corroborates Thryve's own press release.
- **Quotes** (https://www.bundesgesundheitsministerium.de/ministerium/ressortforschung/handlungsfelder/forschungsschwerpunkte/long-/post-covid/modul-2/remit.html, regulator/government page):
  - "FIMO Health GmbH mHealth Pioneers GmbH"
  - "Projektlaufzeit 01.11.2024 - 01.01.2029"
- **KB has it:** no. Possible Module 3 candidate once results are published.

### D3. Corona-Datenspende (RKI, 2020 to 2022), built by Thryve; aggregated data open on Zenodo
- **Fields:** research_program (evidence of use)
- **Found:** Thryve built the RKI's wearable data-donation app (launched April 2020). RKI published district-level aggregates of resting pulse, steps and sleep for the full April 2020 to December 2022 period on Zenodo. A Thryve co-founder co-authored Amft et al., IEEE Pervasive Computing 2020 (doi:10.1109/MPRV.2020.3021321, PubMed 35936518).
- **Quotes:**
  - "The data donation tool built for the German center for disease control Robert Koch-Institute, analyzes data of more than 500.000 citizens for COVID-19 symptoms." https://www.thryve.health/news/how-thryve-built-a-data-donation-tool-to-fight-covid-19-for-the-german-government (vendor_page)
  - "Sie decken den vollständigen Erhebungszeitraum der CDA vom April 2020 bis Dezember 2022 ab." https://zenodo.org/records/8229284 (secondary: RKI dataset, published 10 August 2023)
- **KB has it:** no. The largest known Thryve deployment; a Module 3 candidate if a feasibility or retention paper is found (a 2024/2025 long-COVID paper on CDA wearable data exists at PMC11920215 but robots.txt blocked the probe, so it is not quoted here).

---

## Searched, nothing found
- Formal academic discount or academic price list: none public (pricing page, research pages, Terve site).
- SOC 2: no claim or report found on Thryve's site or by web search.
- ISO certificate registry entry for mHealth Pioneers GmbH: none found by web search (IAF CertSearch not queried, needs an interactive search).
- FDA: openFDA 510(k) and registration listing, "mHealth Pioneers" and "Thryve", no matches.
- CE/MDR or EUDAMED entry for Thryve as a device: none; Thryve says it is not a device.
- AI training terms: nothing in public pages; no public general terms and conditions page reachable from the site navigation (privacy, cookie and imprint only).
- Public GitHub repo or SDK changelog: none found; SDK release notes are on thryve.health/updates only.
- Garmin developer-pause impact on Thryve's shared Garmin client: no Thryve statement found.
- 2026 funding: none; latest is a €4 million Series A dated 2 September 2024 (Capricorn Partners release; a Techleap listing dates it 2025).
- Partner/integrator pages (Fitabase, Labfront, Terra) mentioning Thryve: none relevant. m-Path resells Thryve as a wearable add-on, already in `module-02-digital-phenotyping/profiles/m-path.md:28`.
- Peer-reviewed papers describing data access via Thryve: only the 2020 Amft et al. commentary in PubMed.
