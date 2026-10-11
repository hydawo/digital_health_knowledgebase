# MetricWire: gap hunt (baseline fact run)

Gap hunter run, 2026-10-11. Company id: `metricwire`. Profile: `module-02-digital-phenotyping/profiles/metricwire.md`.
All quotes below returned `exact` from `python3 tools/facts/quote_probe.py URL "quote"` on 2026-10-11.

Short version: MetricWire publishes a public OpenAPI specification for a "MetricWire Consumer API" on SwaggerHub. It covers participants, survey and diary submissions, 31 phone sensor types, Fitbit and Polar wearable data, cognitive tasks and API triggers. The knowledge base says no official API documentation exists. It also says wearable integration is "Not established", but the app listings and the API show HealthKit, Fitbit and Polar. Penn State runs an enterprise licence, open to external researchers, that the knowledge base does not mention.

---

## A. Contradictions

### A1. An official, public API specification exists (SwaggerHub, "MetricWire Consumer API")

- **Schema fields:** `export_routes`, `developer_program_status`, `raw_streams`
- **Found:** The MetricWire organisation on SwaggerHub publishes "MetricWire Consumer API". The default version is 3.0.0, created 2023-06-29 and modified 2025-05-21. Version 4.0.0 was created 2025-05-13 and is a subset of 3.0.0 (seven endpoints dropped, none added). Earlier versions are 1.0.0 (created 2019-05-20) and 2.0.0 (2021-01-05). The registry marks every version `X-Private: false`, so the spec is publicly readable. Host: `consumer-api.metricwire.com`. Authentication uses OAuth2 client credentials (client key and secret exchanged for a bearer token). The endpoints cover workspaces, studies, surveys, intakes, survey, diary and analysis submissions (with a "PII option"), media, participants, device snapshot activity, study and survey activity, cognitive-task submissions, sensor data, Fitbit, Polar, digital interventions, and create/update/delete of "API triggers". Version dates come from the registry listing `https://api.swaggerhub.com/apis/MetricWire/ConsumerAPI`. They are registry metadata, not a quote.
- **URL:** https://app.swaggerhub.com/apis-docs/MetricWire/ConsumerAPI/3.0.0 (the page renders with JavaScript, so it was checked through the registry JSON with `--fetch-url https://api.swaggerhub.com/apis/MetricWire/ConsumerAPI/3.0.0`)
- **Quotes:**
  - "Using this API, authenticated users will be able to query their data and receive the responses back in the form of JSON"
  - "The API uses the OAuth2 Client Credentials flow to provide authorized access to the API"
  - "Get the all api triggers in study"
  - "Get Device Snapshot Activity for User Paginated"
  - "Get Cognitive Task Submissions from a task"
- **Date:** spec v3.0.0 modified 2025-05-21; read 2026-10-11
- **Source type:** vendor_docs
- **Knowledge base:** **contradicts.** `module-02-digital-phenotyping/profiles/metricwire.md` line 77 says "**No official, MetricWire-published API documentation was located**". Line 122 says the API "is not publicly documented for general researcher self-service". Line 134 lists "a documented public API" as a poor fit. Line 144 is an open question asking whether an official documented channel exists. `shared/unresolved-questions.md` line 294 (#90) says "MetricWire's API still Unclear". This finding answers #90. Still unknown: whether API credentials come with every licence or only some tiers (several operation IDs end in "Enterprise", for example `GetSensorSubmissionsFromStudyEnterprise`).

### A2. The zeolite client is built on that official API, not reverse-engineered

- **Schema fields:** `export_routes`
- **Found:** The README of the UW-Madison `zeolite` client points to MetricWire's SwaggerHub documentation. It says workspace IDs appear in a "Workspace API Reference" section of the researcher workspace. So the API is a feature exposed in the product, not a private or partner channel. The client's development was DARPA-sponsored. The last commits are dated 2024-09-19.
- **URL:** https://github.com/uwmadison-chm/zeolite
- **Quotes:**
  - "API documentation is available on Swaggerhub"
  - "ID values for your project should be listed in a workspace's \"Workspace API Reference\" section"
  - "Metricwire, Inc does not endorse, sponsor, or maintain this project"
- **Date:** README current at 2026-10-11; last commit 2024-09-19
- **Source type:** repository
- **Knowledge base:** **contradicts** the profile's reading of this repo. Line 77 says it shows an API "that at least one outside research-computing group has reverse-engineered or been given credentialed access to", and calls it "private/partner-only". Line 161 (source 4) says "no official public API documentation was located". The README itself links the official documentation.

### A3. Wearable and health-platform integration is documented (HealthKit, Fitbit, Polar, Health Connect)

- **Schema fields:** `raw_streams`, `derived_metrics`, `export_routes`
- **Found:** The App Store listing says Catalyst integrates with Apple HealthKit. The Google Play listing names Fitbit and Polar. The participant privacy policy names Health Connect. The API has a Fitbit endpoint with 19 data types, including intraday heart rate, HRV, breathing rate and SpO2, plus ECG and temperature. It has 13 Polar endpoints, including continuous heart rate, sleep hypnogram, Nightly Recharge HRV and breathing rate.
- **URLs and quotes:**
  - https://apps.apple.com/us/app/catalyst-by-metricwire/id1585123028 : "Catalyst integrates with Apple HealthKit to collect movement data such as sleep, step count, exercise, and distance if enabled by the Study Team"
  - https://play.google.com/store/apps/details?id=com.metricwire.digitalhealth&hl=en_US : "Researchers may ask questions about activity and fitness or collect data through wearable sensors like Fitbit or Polar"
  - https://metricwire.com/participant-privacy-policy/ : "The use of information received from Health Connect will adhere to the Health Connect Permissions Policy, including the Limited Use requirements."
  - https://app.swaggerhub.com/apis-docs/MetricWire/ConsumerAPI/3.0.0 (checked via the registry JSON): "Get all fitbit data on a user"; "fitbitHeartRateIntraday, fitbitHeartRateVariabilityIntraday, fitbitBreathingRateIntraday, fitbitBloodOxygenIntraday"; "Get Polar Continuous Heart Rate for Participant"; "Get Polar Nightly Recharge HRV Data for Participant"
- **Date:** read 2026-10-11 (app listings current; spec modified 2025-05-21)
- **Source type:** app_store, vendor_legal, vendor_docs
- **Knowledge base:** **contradicts.** `module-02-digital-phenotyping/comparison-matrix.md` line 116, wearable column for MetricWire: "Not established". The profile has no wearable, HealthKit or Health Connect section. Module 1 Polar and Fitbit profiles may want a back-link (not checked in depth).

### A4. The phone sensor catalogue is enumerated in the API, with separate iOS stream types

- **Schema fields:** `raw_streams`, `derived_metrics`
- **Found:** The sensor-data endpoint's `sensorType` parameter lists 31 values: accelerometer, gyroscope, magnetometer, passivelocation, linearacceleration, pedometer, ambient, gravity, activitytypes, deviceinformation, activity, steps, noise, light, mobility, battery, bluetooth, screenevent, messages, calls, apps, appusage, appusageevents, mobilityplaces, mobilitystops, mobilitymoves, usageeventsios, usageios, callsios, messagesios, lightios. The `*ios` variants suggest iOS streams are stored separately from Android ones. The "mobilityplaces/stops/moves" types look like derived mobility features. The default page size is 100000 records. This is an API enumeration, not a per-OS availability statement, so the profile's iOS/Android columns still cannot be filled from it.
- **URL:** https://app.swaggerhub.com/apis-docs/MetricWire/ConsumerAPI/3.0.0 (checked via the registry JSON)
- **Quotes:**
  - "accelerometer, gyroscope, magnetometer, passivelocation, linearacceleration, pedometer, ambient, gravity, activitytypes, deviceinformation, activity, steps, noise, light, mobility, battery, bluetooth, screenevent, messages, calls, apps, appusage, appusageevents"
  - "mobilityplaces, mobilitystops, mobilitymoves, usageeventsios, usageios, callsios, messagesios, lightios"
  - "If no number is provided, default is 100000"
- **Date:** spec modified 2025-05-21; read 2026-10-11
- **Source type:** vendor_docs
- **Knowledge base:** **contradicts / no.** Profile lines 33 to 51 mark every stream except GPS "Unclear", and line 61 says derived metrics were "Not verified in any pass to date". Matrix line 116: "'Passive Sensors' named without a list". A search snippet (not quotable; the Atlassian page now 404s) also said sensors arrived in version 4.0 and are sold as an add-on. Treat that as unconfirmed.

---

## B. Missing programmes

### B1. Penn State Survey Research Center enterprise licence (TRACE), open to external investigators

- **Schema fields:** `research_program`, `program_eligibility`, `academic_pricing`, `academic_vs_commercial`
- **Found:** Since March 2024, Penn State's SRC has held an enterprise-level MetricWire licence. It offers three tiers: an independent licence at reduced cost, projects run on the SRC licence with SRC programming and data management, and no-cost access for Penn State pilot or thesis projects. The first two tiers are open to external partners. No prices are published.
- **URLs and quotes:**
  - https://survey.psu.edu/trace/metricwire : "The SRC holds an enterprise-level license of Metricwire and can provide access to investigators at significantly reduced costs."; "Investigators, both affiliated with Penn State and external partners, can choose between three distinct levels of platform access"; "can gain access to the enterprise-level license at no cost."
  - https://www.psu.edu/news/social-science-research-institute/story/survey-research-center-adds-metricwire-trace-portfolio : "Penn State's Survey Research Center (SRC) recently acquired an enterprise-level MetricWire license" (published 2024-03-14)
- **Date:** 2024-03-14 (announcement); TRACE page read 2026-10-11
- **Source type:** secondary (institutional partner)
- **Knowledge base:** **no.** Nothing in the repo mentions Penn State or TRACE for MetricWire. It is relevant to profile line 101 and matrix line 135 (academic programme column). It is a concrete route to the "Academic Site Licence" model, run by a reseller institution.

---

## C. Other findings the knowledge base lacks

### C1. Data retention: research team deletes at study end; MetricWire keeps no extra copies

- **Schema field:** `retention_terms`
- **URL:** https://metricwire.com/participant-privacy-policy/ (sitemap lastmod 2023-11-03)
- **Quotes:**
  - "When the study is over, the Research Team will delete your data from the MetricWire servers. MetricWire does not retain any additional copies of your data on our servers or in the MetricWire Mobile Application."
  - "there may be situations where we are obligated to retain one archival copy of your information to allow us to comply with laws or respond to legal processes"
- **Date:** policy page modified 2023-11-03; read 2026-10-11
- **Source type:** vendor_legal
- **Knowledge base:** **no.** Profile line 145 lists "Data retention" as open. No retention period or automatic deletion is stated: deletion depends on the research team.

### C2. DPAs with service providers; HIPAA-compliant US servers (participant policy)

- **Schema fields:** `dpa`, `hipaa_statement`, `data_residency`
- **URL:** https://metricwire.com/participant-privacy-policy/
- **Quotes:**
  - "We enter into Data Protection Agreements and regularly audit our relationships with all of our service providers"
  - "your data are immediately synced to HIPAA-Compliant servers located in the United States and removed from your mobile device"
- **Date:** 2023-11-03 (page lastmod); read 2026-10-11
- **Source type:** vendor_legal
- **Knowledge base:** **partly.** US storage is already in the profile (line 95, from the security summary). The DPA statement covers MetricWire's own subprocessors, not a DPA offered to customers. The `dpa` field should say so. No BAA wording was found on any metricwire.com page (see section D).

### C3. Google Play data-safety: app interactions shared for advertising or marketing

- **Schema fields:** `retention_terms` (data-use terms); also relevant to participant-experience notes
- **URL:** https://play.google.com/store/apps/datasafety?id=com.metricwire.digitalhealth&hl=en_US
- **Quote:** "App interactions App functionality, Analytics, Advertising or marketing, Personalization"
- **Found:** This line appears under "Data shared". The same panel lists optional collection of precise location, installed apps, and health and fitness info. Data is encrypted in transit, and deletion can be requested. The iOS privacy label lists location, photos or videos, audio data and sensitive info as "Data Not Linked to You".
- **Date:** read 2026-10-11
- **Source type:** app_store
- **Knowledge base:** **no.** Worth a line for IRB reviewers, since it is a developer self-declaration that sits oddly against the research-only positioning.

### C4. Background ambient-noise measurement added (iOS 5.16.0, re-listed in 6.9.0)

- **Schema fields:** `raw_streams`, `deprecations` (change log)
- **URL:** https://apps.apple.com/us/app/catalyst-by-metricwire/id1585123028
- **Quote:** "Ambient noise measurement can now continue in the background for studies that include it. Only sound levels are measured; no audio is recorded."
- **Found:** In the version history, this note is attached to 5.16.0 (2025-10-06) and also shown as the current "What's New" for 6.9.0. A 6.0.0 major release shipped 2026-02-18 with only "Bug fixes" notes.
- **Date:** read 2026-10-11
- **Source type:** app_store
- **Knowledge base:** **no.** Profile line 49, "Audio / microphone", is "Unclear". This shows sound level only, no audio recording, on iOS.

### C5. Cognitive tasks and digital interventions are product features

- **Schema field:** `derived_metrics` (active-task side); mainly a profile gap
- **URL:** https://metricwire.com/
- **Quotes:** "Run cognitive experiments and evaluate digital interventions under real world conditions."; "Enable questions, notifications and passive data capture based on contextual elements such as location, previous responses, passive data, dates and times or randomized options."
- **Date:** read 2026-10-11 (page footer copyright 2023)
- **Source type:** vendor_page
- **Knowledge base:** **no** for cognitive tasks and digital interventions. Trigger-based delivery is already in the profile (line 65). The API's cognitive-task and digital-intervention endpoints (A1) back this up.

### C6. m2c2kit integration guide repository archived

- **Schema field:** `deprecations` (third-party integration)
- **URL:** https://github.com/m2c2-project/m2c2kit-integration-guides/blob/main/docs/metricwire.md
- **Quotes:** "This repository was archived by the owner on Aug 12, 2026. It is now read-only."; "it is possible for them to be embedded via Qualtrics, REDCAP, and Metricwire (as well as anything else with a WebView)"
- **Date:** archived 2026-08-12; read 2026-10-11
- **Source type:** repository
- **Knowledge base:** **no.** Profile line 77 and source 3 (line 160) cite the guide as live. The guide still reads, but it is no longer maintained.

### C7. Public knowledge base (Atlassian) is gone, not just one page

- **Schema field:** `export_routes` (documentation route)
- **Found:** On 2026-10-11 the REST endpoint for the whole space (`https://metricwire.atlassian.net/wiki/rest/api/space/mwknowledgebase`) and the pages "Smartphone Sensor Data" (229638145), "Workspaces" (42369032) and "Understanding Responses" (2359312) all returned HTTP 404. No replacement help centre was found: help., support., docs. and kb. subdomains do not resolve. No quote is possible because the pages are gone.
- **Source type:** vendor_docs (absence)
- **Knowledge base:** **partly.** Profile line 91 and source 8 (line 165) record one dead page. The whole knowledge base is unavailable, so the help-centre route to sensor, export and background details is closed until the vendor restores it.

### C8. Published-use breadth is much larger than the PubMed title/abstract count

- **Schema field:** none directly (Research Evidence section; relevant to the "most published EMA platform" claim)
- **Found:** Europe PMC full-text search for `"metricwire"` returned 351 records (130 from 2025 to 2026). ClinicalTrials.gov search for `metricwire` returned 12 studies. Counts are from the APIs on 2026-10-11 and are not quotes: `https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%22metricwire%22&format=json` and `https://clinicaltrials.gov/api/v2/studies?query.term=metricwire&countTotal=true`. Hits are mentions, not confirmed deployments.
- **Source type:** paper (bibliographic database)
- **Knowledge base:** **no.** Profile line 107 reports only the three PubMed title/abstract records. It does not contradict them, but it understates breadth of use.

### C9. Terms of use: Ontario law, non-refundable fees

- **Schema field:** `minimum_commitment` (weakly)
- **URL:** https://metricwire.com/terms-of-use/ (sitemap lastmod 2025-09-15)
- **Quotes:** "This Agreement is governed by the laws of the Province of Ontario, Canada"; "Any fees paid by you are non-refundable"
- **Date:** 2025-09-15 (page lastmod); read 2026-10-11
- **Source type:** vendor_legal
- **Knowledge base:** **no.** Minor. There is no AI-training, aggregation-for-benchmarking or retention clause in the terms. The general privacy policy (not the participant one) allows disclosing aggregate, non-identifying usage data to third parties.

---

## D. Searched, nothing found

- **FDA:** openFDA 510(k), registration and listing, and MAUDE event searches for "metricwire" all returned NOT_FOUND. No clearances, as expected for a research data-collection platform (`fda_clearances` can be `not_applicable` or `not_public` with this evidence).
- **ISO 27001 / SOC 2 evidence:** no certificate, certification body, registry entry or trust-centre page was found. Only the vendor's own Data Privacy & Security Summary makes the claim.
- **BAA:** no BAA wording on metricwire.com (home, terms, both privacy policies, security summary, site licence, responsible disclosure), and no partner page mentioning a MetricWire BAA.
- **AI or ML training terms:** none in the terms of use or either privacy policy.
- **News, funding, acquisition, job postings (2025 to 2026):** nothing found. The site's page sitemap shows no new pages since 2025-09-15 (terms of use). `/sas2024/` is a contact form only.
- **Pricing figures:** none in directories, grant budgets or partner pages. Penn State gives no figures either.
- **Other university licences:** only Penn State found. Brown CAAS lists MetricWire as a tool its programmer uses, but no licence offer.
- **Integrator pages (Fitabase, Labfront, Terra, Thryve):** no MetricWire integration found. Wearable data comes through MetricWire's own Fitbit and Polar connectors.
- **Status page:** status.metricwire.com exists (UptimeRobot), with no incident history captured.
- **apis.io directory:** says MetricWire publishes no public API specification. That is contradicted by A1 and should not be cited.
