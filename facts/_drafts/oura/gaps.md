# Oura: gap hunt, 2026-10-10

Gap hunter draft. Sources outside Oura's API docs, membership page and research page: regulator databases (openFDA, FDA 510(k) summaries, EUDAMED), trial registry, papers (Europe PMC full text), Oura's privacy policy and Oura for Organizations sub-pages, partner support, press and partner releases, the SEC S-1.

Quote status key:
- **exact**: `python3 tools/facts/quote_probe.py URL "quote"` returned `exact 1.0` on 2026-10-10.
- **exact (local copy)**: the probe could not fetch the URL (FDA's cdrh_docs returns 404 to the probe's user agent, though the file exists); the PDF was downloaded with curl and the quote matched with the same `match_quote` function from `tools/facts/common.py`. The judge should decide whether this counts.
- **unconfirmed**: sec.gov returns 403 to the probe and to curl. Text came from a WebFetch read of the filing and may be paraphrased. Do not put it in a record until someone reads the filing.

KB file references: P = `module-01-wearables/profiles/oura.md`, M = `module-01-wearables/comparison-matrix.md`, Y = `facts/oura.yaml`.

---

## A. Contradictions and corrections

### A1. The common research route is a named portal, "Oura Teams", used since at least 2022
- **Field:** research_program, export_routes (also program_status)
- **Found:** Papers name the researcher portal "Oura Teams" (also described as "Oura on the Web") and use it to manage participant accounts and export CSVs. Chinoy et al. 2022 (*Nat Sci Sleep*, doi 10.2147/nss.s348795) lists it alongside Polar AccessLink and Fitabase as company portals "set up by the device companies for researchers". Haimovich et al. 2026 (*JMIR Form Res*, doi 10.2196/92359) exported CSVs from it, including one-minute MET data used to estimate wear time. The Lights Out protocol (*JMIR Res Protoc* 2026, doi 10.2196/83980) uses "Oura Teams processing pipelines" for sleep variables. 18 Europe PMC records mention "Oura Teams" (query run 2026-10-10). So the KB's 2026-10-10 framing of the research offering as newly found, and its claim that studies typically use a custom OAuth app or middleware, both miss the route most published studies actually used. Whether "Oura Teams" is the same product as today's "Oura Enterprise Platform" is not stated anywhere found (**Unclear**).
- **URLs and quotes:**
  - https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8957400/fullTextXML: "Device data were exported from online portals set up by the device companies for researchers to manage participant accounts" (exact)
  - https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13626187/fullTextXML: "Data were exported from the Oura Teams platform as comma-separated value files" (exact)
  - https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12822870/fullTextXML: "Processed data will be accessed in the Oura Teams environment" (exact)
  - https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12440682/fullTextXML: "Data were exported from Oura Teams platform (Oura on the Web, Oura Health Oy, 2021)" (exact)
- **Date:** papers published 2022-03-22, 2025-10-01, 2026-01-21, 2026-09-30
- **Source type:** paper
- **KB has it:** contradicts. P line 111 says studies "typically either (a) enrol participants through a custom OAuth app ... or (b) use middleware"; P line 27 says "Oura now sells a first-party research offering", implying it is new. "Oura Teams" appears nowhere in P, M or Y.

### A2. Retention period for member data is stated in the privacy policy
- **Field:** retention_terms (Oura's own retention, not the API Agreement's)
- **Found:** Oura's privacy policy says measurement data are kept only while the account is active. Relevant to the KB's open question on what happens to data when a membership lapses or an account closes.
- **URL:** https://ouraring.com/privacy-policy
- **Quote:** "your measurement data regarding your sleep, readiness, and activity is stored only so long as your Oura account is active" (exact)
- **Date:** read 2026-10-10 (policy page shows no date in the extracted text)
- **Source type:** vendor_legal
- **KB has it:** contradicts. P line 155 lists "retention period" as "Not stated publicly".

### A3. The API Agreement's counterparty is a US company, not the Finnish one
- **Field:** dpa (contracting entity)
- **Found:** The Oura API and MCP Agreement is made with Ouraring, Inc., a Delaware corporation. The KB lists only Oura Health Oy, Finland. This matters for which entity a DPA, BAA or data-transfer clause would be signed with.
- **URL:** https://cloud.ouraring.com/legal/api-agreement
- **Quote:** "is made and entered by and between OURARING, INC., a Delaware corporation" (exact)
- **Date:** agreement effective 2026-06-08; read 2026-10-10
- **Source type:** vendor_legal
- **KB has it:** contradicts in part. P line 7 gives the organisation as "Oura Health Oy (Ōura), Finland"; P line 305 reasons that Oura being "EU-headquartered" may help EU studies.

### A4. The Y note on AI-training consent is resolved: three clauses, one with a consent route
- **Field:** ai_training_terms
- **Found:** §4(a) lists Prohibited Uses (including AI training) "unless Oura provides prior written consent". §4(d), not mentioned in the KB, separately bars using the API to "develop, train, fine-tune, evaluate, prompt" any AI model, with no consent route, and says LLM use is allowed only through Oura's MCP Server. §6(g) is the capitalised ban already in P. So the repair agent's reading (a consent route exists) and the record's reading (no route) are both right about different clauses. §4(d) also means feeding Oura API data into any LLM-assisted analysis pipeline is barred outside the MCP Server.
- **URL:** https://cloud.ouraring.com/legal/api-agreement
- **Quotes:**
  - "You shall not use, access, process, or exploit Oura Intellectual Property or any User Data for any of the following purposes (each, a “ Prohibited Use ”), unless Oura provides prior written consent" (exact)
  - "you may (unless you are an Aggregator) access and process such Oura Data or User Data solely through the MCP Server" (exact)
  - "You shall not use, and shall not permit any third party to use, the Oura API to develop, train, fine-tune, evaluate, prompt, or otherwise provide input or data to any AI Model or AI Platform" (exact)
- **Date:** effective 2026-06-08; read 2026-10-10
- **Source type:** vendor_legal
- **KB has it:** partly. P line 122 has §4(a)(iii) and §6(g); §4(d) and the MCP-only rule are absent. Y line 184 note flags the unresolved conflict.

---

## B. Research programs and research-relevant partnerships missing from the KB

### B1. Oura Research App: Research Sponsor is controller, Oura is processor, and blinding is supported
- **Field:** dpa, research_program, academic_vs_commercial
- **Found:** The privacy policy has a section on the Oura Research App. The study sponsor is the data controller, Oura acts as processor or service provider, the informed consent form governs where it conflicts with the policy, and studies can blind participants to their scores and insights while the ring keeps collecting. This partly answers the KB's open question on whether research customers sit under different terms than the API Agreement, and blinding is a real design option (reduces reactivity) that the KB does not record.
- **URL:** https://ouraring.com/privacy-policy
- **Quotes:**
  - "the Research Sponsor acts as the controller (or equivalent legal role under applicable data protection laws) of research data collected for the study" (exact)
  - "Oura may act as a processor or service provider to the Research Sponsor in connection with the hosting, storage, or technical administration of the Oura Research App" (exact)
  - "Research studies may involve data blinding or other protocol-based restrictions" (exact)
  - "During a blinded period, you may not be able to access certain personal data, scores, or insights in the Oura Research App, even though your Oura Ring continues to collect sensor data" (exact)
- **Date:** read 2026-10-10
- **Source type:** vendor_legal
- **KB has it:** no. P line 36 describes the app only from its App Store listing; P lines 109 and 300 and M line 387 say whether research customers sign different terms "is not public".

### B2. Oura Enterprise Platform: Oura keeps aggregated data for its own R&D, and recipients keep what they already extracted
- **Field:** retention_terms, academic_vs_commercial
- **Found:** Under the enterprise platform (which covers researchers as "Data Recipients"), a participant's withdrawal does not touch data the recipient already extracted, which is the opposite of the API Agreement's 72-hour deletion rule. Oura also states it uses aggregated platform data for its own analytics and R&D. Both matter for a consent form.
- **URL:** https://ouraring.com/privacy-policy
- **Quotes:**
  - "withdrawing your consent from the service or changing any other consent settings do not affect the processing of data that the Data Recipient already extracted from Oura Enterprise Platform" (exact)
  - "Oura uses aggregated Oura Enterprise Platform data for analytics, statistics, research and development purposes" (exact)
- **Date:** read 2026-10-10
- **Source type:** vendor_legal
- **KB has it:** no. P line 109 asks whether the API Agreement's retention limits bind research customers; this is the first published evidence that the enterprise route works differently.

### B3. Oura donated rings and memberships to a research dataset (Tidepool, announced November 2025)
- **Field:** academic_pricing, research_program
- **Found:** Oura is contributing Gen3 rings and memberships to Tidepool's diabetes research dataset (IRB-approved study, recruitment planned for early 2026; de-identified data shared with researchers through Tidepool's Big Data Donation Project). A precedent for waived memberships in research, which the KB lists as its "highest-value question". No primary Oura or Tidepool page was found; FemTech Insider and MedTech Dive (403 to the probe) carry it.
- **URL:** https://femtechinsider.com/tidepool-and-oura-collaborate-to-build-diabetes-research-dataset/
- **Quote:** "Oura is contributing Oura Ring Gen 3 devices and memberships to support the research initiative" (exact)
- **Date:** 2025-11-05
- **Source type:** secondary
- **KB has it:** no. P line 162 says waived or bulk membership for study rings is "not established".

### B4. Oura–NUS Joint Lab (opened 22 January 2026)
- **Field:** research_program
- **Found:** Oura's first research entity in Asia-Pacific, with the Centre for Sleep and Cognition at NUS Medicine, using Oura data "within approved research studies". An institutional partnership rather than an open program, but it shows the kind of research partnership Oura runs.
- **URL:** https://www.edb.gov.sg/en/about-edb/media-releases-publications/oura-and-nus-launch-joint-lab-for-personalised-health-research.html (mirror of the NUS release at https://medicine.nus.edu.sg/wp-content/uploads/2026/01/2026-01-19_Opening-of-the-Oura-NUS-Joint-Lab-Press-Release.pdf, which the probe read once with `--show` and then failed to parse on retry)
- **Quotes:**
  - "New Joint Lab marks ŌURA’s first research entity in the APAC region, deepening a six-year partnership with NUS" (exact)
  - "combining continuous, real‑world biometric data from ŌURA within approved research studies" (exact)
- **Date:** 2026-01-22 (dateline of the NUS release as read with `--show`)
- **Source type:** secondary (government agency reprint of a joint press release)
- **KB has it:** no

### B5. Oura is listed as an industry collaborator on registered trials
- **Field:** research_program
- **Found:** ClinicalTrials.gov lists Oura (as "Oura Ring, Inc", "Oura health oy" or "Oura Ring") as collaborator on five academic studies, including Scripps' Wellderly Brain trial (NCT07646054, not yet recruiting, start 2026-07-06) and a UCSD obesity-treatment trial (NCT07736729, start 2026-08-17). Evidence that Oura supports investigator-led studies in kind, outside any published program. What Oura provides in each is not stated in the registry entries read.
- **URLs:** https://clinicaltrials.gov/api/v2/studies/NCT07646054 ; https://clinicaltrials.gov/api/v2/studies/NCT07736729
- **Quotes:** "Oura Ring, Inc" (exact, NCT07646054); "Oura health oy" (exact, NCT07736729)
- **Date:** registry records read 2026-10-10
- **Source type:** secondary (trial registry)
- **KB has it:** no

---

## C. Regulatory

### C1. Oura holds no FDA clearance, but Fertile Window is an FDA-listed device and an EU Class I device
- **Field:** fda_clearances
- **Found:**
  - openFDA registration and listing: Oura Health Oy (Oulu, Finland) is registered as a device manufacturer and lists one device, "Fertile Window", product code LHD ("Device, Fertility Diagnostic, Proceptive"), device class "U", listing created 2023-08-08. No K-number attached.
  - openFDA 510(k): no records with Oura as applicant or device name (queries `applicant:oura` and `device_name:oura` both returned "No matches found", 2026-10-10).
  - EUDAMED: four "Fertile Window" UDI-DI records (iOS and Android, versions 1 and 2.x), manufacturer Oura Health Oy, SRN FI-MF-000037866, risk class I, status on the market.
  - Natural Cycles 510(k) K202897 (decision 2021-06-24) cleared automatic temperature input from the Oura ring; later Natural Cycles clearances (K231274, K241006, K250561, K253694) keep Oura as a compatible wearable. The FDA-cleared contraceptive use belongs to Natural Cycles, not Oura.
  - S-1 (unconfirmed, see key): states Oura holds no marketing authorizations, markets Fertile Window in the US under enforcement discretion, and that Fertile Window is a self-certified Class I device under the EU MDR; also names an investigational "Blood Pressure Profile" algorithm for hypertension.
- **URLs and quotes:**
  - https://api.fda.gov/device/registrationlisting.json?search=registration.name:oura&limit=5: "OURA HEALTH OY" (exact); "Fertile Window" (exact); "Device, Fertility Diagnostic, Proceptive" (exact); "2023-08-08" (exact)
  - https://ec.europa.eu/tools/eudamed/api/devices/udiDiData?tradeName=fertile%20window&page=0&pageSize=10&iso2Code=en&languageIso2Code=en: "Oura Health Oy" (exact); "FI-MF-000037866" (exact); "refdata.risk-class.class-i" (exact)
  - https://www.accessdata.fda.gov/cdrh_docs/pdf20/K202897.pdf: "the device allows automatic temperature input from the Oura ring, a wearable temperature monitor" (exact, local copy)
  - https://www.accessdata.fda.gov/cdrh_docs/pdf23/K231274.pdf: "the predicate submission cleared the Oura Ring for automatic temperature input" (exact, local copy)
  - https://www.sec.gov/Archives/edgar/data/0002133022/000119312526381855/d119865ds1.htm: unconfirmed extracts "We currently hold no marketing authorizations for our device functionality"; "We market our Fertile Window medical device function in the United States under an FDA enforcement discretion policy"; "the Fertile Window feature of Oura App is currently registered as a self-certified Class I medical device software"
  - https://organizations.ouraring.com/solutions/partners-resellers: "Natural Cycles, the first FDA-cleared birth control app, integrates daily temperature trends to predict fertility status" (exact)
- **Date:** FDA listing 2023-08-08; K202897 2021-06-24; S-1 filed September 2026; all read 2026-10-10
- **Source type:** regulator_db (openFDA, EUDAMED, FDA 510(k) summaries); vendor_legal (S-1); vendor_page (partner page)
- **KB has it:** no. Y line 246 `fda_clearances: unresearched`; M line 245 regulatory column for Oura says "None documented in the profile"; P has no regulatory section. Not a contradiction (no Oura-held clearance exists), but the matrix should record the listing and the EU Class I status.

### C2. No FDA warning letter, recall or enforcement record found
- **Field:** fda_clearances
- **Found:** openFDA device recall query `recalling_firm:oura` returned "No matches found"; web search for Oura warning letters found none. Recorded under "searched, nothing found" below as well.
- **Source type:** regulator_db
- **KB has it:** n/a

---

## D. Terms, pricing and access changes

### D1. Participant consent does not lift the API's Prohibited Uses
- **Field:** ai_training_terms, retention_terms
- **Found:** §4(c) says the Prohibited Uses apply even if the user consented. A study cannot cure a retention, sharing or AI use under the API route through its own consent form; only Oura's written consent (where the clause allows it) does.
- **URL:** https://cloud.ouraring.com/legal/api-agreement
- **Quote:** "the foregoing Prohibited Uses shall apply regardless of whether a User has purportedly consented to any such use" (exact)
- **Date:** effective 2026-06-08
- **Source type:** vendor_legal
- **KB has it:** no. P lines 119 to 126 cover the Agreement but not this clause.

### D2. Oura reserves the right to charge for the API, with different pricing for business users; apps may not charge users
- **Field:** api_platform_fees
- **Found:** §3(h) lets Oura start charging for the API, MCP Server or platform with notice, including "differentiated pricing for business users". §4(a)(xiii) bars charging users for anything related to the API. "Free" is today's policy, not a term.
- **URL:** https://cloud.ouraring.com/legal/api-agreement
- **Quotes:**
  - "Oura reserves the right to charge you fees for use of the MCP Server, the Oura API, or for access to the Oura Platform in the future at its discretion, including, without limitation, rated pricing and/or differentiated pricing for business users" (exact)
  - "charging Users in any manner for access to or use of the MCP Server or any services or functionality included in or related to the MCP Server, Oura API, or Oura Platform" (exact)
- **Date:** effective 2026-06-08
- **Source type:** vendor_legal
- **KB has it:** no. Y line 124 `api_platform_fees: unresearched`; P line 116 quotes "the Oura API is free to use" without the reservation; M line 387 says "API free".

### D3. Deletion is also triggered by a user cancelling the study app's subscription
- **Field:** retention_terms
- **Found:** Beyond the 72-hour deletion on request already in the KB, §5 also requires deletion when a user terminates or cancels the app's subscription, and bans any retention after a deletion request.
- **URL:** https://cloud.ouraring.com/legal/api-agreement
- **Quotes:**
  - "YOU SHALL NOT RETAIN ANY USER DATA AFTER THE USER HAS REQUESTED DELETION OF USER DATA" (exact)
  - "You must also delete User Data upon such User’s termination or cancellation of applicable Collaborator Application subscriptions" (exact)
- **Date:** effective 2026-06-08
- **Source type:** vendor_legal
- **KB has it:** partly. P line 121 has the 72-hour rule and deletion on termination of the Agreement, not on cancellation of the app subscription.

### D4. The 2021 API Agreement is archived and marked superseded
- **Field:** deprecations
- **Found:** A Previous Terms page keeps the old agreement ("Last update: May 11, 2021"), marked superseded. Useful for any study that started under the old terms and needs to show what applied.
- **URL:** https://cloud.ouraring.com/legal/api-agreement/previous-terms/2021
- **Quote:** not probed as a full sentence; `--show` output began "Oura API Agreement (2021 – superseded) This is a superseded version of the Oura API Agreement." Treat as unconfirmed until probed.
- **Date:** read 2026-10-10
- **Source type:** vendor_legal
- **KB has it:** no

### D5. Partner support portal and "dedicated Partner support" for the API
- **Field:** developer_program_status
- **Found:** Oura runs a separate partner support site (partnersupport.ouraring.com) and the partners page offers custom integration options and dedicated partner support. The partner-site API article also says Gen2 users are unaffected by the membership gate (the member-site article, already in the KB, says "Gen3 and later").
- **URLs and quotes:**
  - https://organizations.ouraring.com/solutions/partners-resellers: "We provide custom integration options and dedicated Partner support for the Oura API" (exact)
  - https://partnersupport.ouraring.com/hc/en-us/articles/20949682312211-Intro-to-the-Oura-API: "Oura Ring Generation 2 users will not experience any changes to the availability of their data through the Oura API" (exact)
- **Date:** read 2026-10-10
- **Source type:** vendor_page, vendor_docs
- **KB has it:** no

---

## E. Compliance claims beyond the research page

### E1. Government page claims NIST 800-171 and IL5; healthcare pages offer de-identification and an "Enterprise API"
- **Field:** soc2 / iso27001 (nearest fields; the schema has none for NIST or DoD impact levels), hipaa_statement, export_routes
- **Found:** The government and defense page says the platform is designed to meet DoD compliance including NIST 800-171 and IL5. The healthcare-provider page offers configurable de-identification, role-based permissions, and an "Enterprise API" distinct from the public API. Vendor claims only; no DoD authorization record was looked up.
- **URLs and quotes:**
  - https://organizations.ouraring.com/solutions/government-defense: "Designed to meet stringent DoD compliance, adhering to GDPR, HIPAA, and NIST 800-171 and IL5 standards" (exact)
  - https://organizations.ouraring.com/solutions/healthcare-providers: "Protects user privacy with configurable options for de-identification and role-based permissions" (exact); "Enterprise API to send data to external systems for further analysis or data enrichment" (exact)
- **Date:** read 2026-10-10
- **Source type:** vendor_page
- **KB has it:** no. P line 102 quotes the research page's "Integrate data into existing systems with Oura API" but not the Enterprise API or de-identification options.

### E2. Business-associate status: the S-1 and the privacy policy point different ways
- **Field:** baa
- **Found:** The S-1 (unconfirmed) says Oura operates as a HIPAA business associate in some cases. The privacy policy says Oura is not a business associate when a member directs a covered entity to send records to Oura. These are not in conflict (different flows), but together they suggest BAAs exist for some enterprise or healthcare work. No signed BAA or partner mention was found.
- **URLs and quotes:**
  - https://ouraring.com/privacy-policy: "Oura is not a Business Associate of that entity for purposes of this sharing" (exact)
  - https://www.sec.gov/Archives/edgar/data/0002133022/000119312526381855/d119865ds1.htm: unconfirmed extract "we operate as a “business associate” (as defined by HIPAA)"
- **Date:** read 2026-10-10
- **Source type:** vendor_legal
- **KB has it:** no. Y line 209 `baa: unresearched`; P line 155 "BAA availability" not stated.

---

## F. Company context

### F1. IPO filed and then postponed
- **Field:** none in the schema (context for program_status and pricing stability)
- **Found:** Public S-1 filed September 2026 (ticker OURA, Nasdaq); the offering was postponed on 2026-09-29 with no new date. The S-1 (unconfirmed) gives 5.0 million paid members at 2026-06-30 and says Oura trains its proprietary models on its member data, and describes the DoD as an enterprise customer.
- **URL:** https://tech.eu/2026/09/29/oura-delays-15bbn-us-ipo/
- **Quote:** "Finland-founded smart ring maker Oura is delaying its US IPO due to market uncertainty, it said today" (exact)
- **Date:** 2026-09-29
- **Source type:** secondary
- **KB has it:** no

---

## Searched, nothing found

- **FDA warning letters or close-outs for Oura:** web search and openFDA recall query (`recalling_firm:oura`), none.
- **Oura-held 510(k) or De Novo:** openFDA 510(k) by applicant and by device name, none. The hypertension feature is reported as investigational only (S-1 unconfirmed; MedTech Dive returns 403 to the probe).
- **HITRUST certificate in an independent registry or an Oura HITRUST press release:** web search found nothing; the trust centre statement remains a self-claim. The HITRUST assurance lookup was not queried directly.
- **ISO 27001 certificate:** nothing found.
- **Data residency or hosting provider:** privacy policy and S-1 (unconfirmed) mention only third-party data centers; no region named.
- **EU Data Act request process at Oura:** no Oura page found.
- **New research grant, fellowship or open academic-access program in the last 12 months:** none found beyond A1 and B1 to B5.
- **API developer intake paused, waitlist or approval delays (forums, Reddit):** nothing found for Oura (a WHOOP forum thread turned up instead).
- **Official Oura MCP Server announcement or docs outside the Agreement:** nothing found.
- **Oura support in Fitabase or Labfront:** neither site mentions Oura. Thryve's supported-wearables URL is dead (404). Terra lists an Oura integration (already implied by M line 339).
- **Oura Research app on Google Play:** three guessed package IDs returned 404 and a Play search found no listing; the app may be iOS-only (**Unclear**, not established).
- **Membership or ring price changes in the last 12 months:** nothing beyond what P already records.
