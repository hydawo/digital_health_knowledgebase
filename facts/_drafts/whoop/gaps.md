# WHOOP gap hunt (baseline fact run, 2026-10-10)

Compared against `module-01-wearables/profiles/whoop.md` (profile), `module-01-wearables/comparison-matrix.md`
(matrix) and `facts/whoop.yaml` (all fields still `unresearched`). Every quote below returned `exact` from
`python3 tools/facts/quote_probe.py`. whoop.com returns HTTP 403 to scripted requests, so whoop.com pages were
probed with `--fetch-url` pointing at a Wayback Machine capture; the capture URL is given for each. Researcher
B's draft (`facts/_drafts/whoop/B.yaml`) already carries findings 2, 6 and 10 in some form; they are kept here
because the knowledge base itself lacks or contradicts them.

## Contradictions

### 1. Raw HR, RR intervals and accelerometry were offered to WHOOP Unite research partners (contradicts "no raw data of any kind")
- **Fields:** raw_streams, export_routes, sampling_rates, api_platform_fees, research_program
- **Found:** A WHOOP-authored "Research FAQs" for WHOOP Unite (hosted by the University of Arizona sensor lab, file dated 2023-05) says WHOOP gives research partners raw data files, with RR intervals per row, and API extraction at extra cost. It also gives 52 Hz HR/accelerometer collection, a participant-blinded mode, and membership transfer between participants.
- **URL:** https://www.sensorlab.arizona.edu/sites/default/files/2023-05/WHOOP%20Unite%20Research%20FAQs_0.pdf
- **Quotes:**
  - "WHOOP provides raw data for analysis via CSV/Excel files."
  - "We do have API capabilities for data extraction at an additional cost."
  - "WHOOP collects HR and accelerometer data at 52 Hz 24/7."
  - "Each row in the raw data file will end with RR-intervals."
  - "all user wellness data is blocked on the mobile app and the participant would only have access to device-related metrics such as remaining battery life"
  - "we can turn off their membership and transfer that status to the next user"
- **Date:** document dated 2023-05; probed 2026-10-10
- **Source type:** secondary (vendor-authored FAQ hosted by a university; not on a WHOOP domain)
- **KB has it:** contradicts. Profile line 20 ("A researcher who wants the underlying physiology cannot get it"), line 125 ("No raw-data escape hatch of any kind"), line 210 ("No raw data of any kind"), line 232; matrix line 99 and 319 ("Derived scores only"). The profile's statements are true of the public API, but a vendor research route to raw files existed. Whether it still exists is open: B.yaml records that whoopunite.com now 301-redirects to whoop.com and reports Unite layoffs. Profile line 96 ("no adherence dashboard") and 135 (screenless means no feedback) also miss the blinded mode.

### 2. Member CSV export includes Journal entries (contradicts "Journal appears not to be exportable")
- **Fields:** export_routes, derived_metrics
- **Found:** WHOOP's own data-export article says the in-app CSV export includes Journal entries, daily scores, RHR, HRV, respiratory rate and sleep architecture; MG members on Life get extra data; whole-history exports can take up to 24 hours.
- **URL:** https://www.whoop.com/us/en/thelocker/access-your-whoop-data-with-new-integrations-data-export-options/ (fetched via https://web.archive.org/web/20260617105808/https://www.whoop.com/us/en/thelocker/access-your-whoop-data-with-new-integrations-data-export-options/)
- **Quotes:**
  - "It also includes your individual Journal entries, allowing you to see how your behaviors correlate with physiological changes."
  - "The file contains your daily scores, resting heart rate, heart rate variability , respiratory rate , and sleep architecture details."
  - "If you request a large date range or your entire account history, the file generation may take up to 24 hours."
  - "WHOOP Life members using WHOOP MG receive additional medical-grade health data."
- **Date:** page shows June 15, 2026 (capture 2026-06-17)
- **Source type:** vendor_page
- **KB has it:** contradicts. Profile line 90 says Journal data "appears not to be exportable ... Treat as unavailable unless confirmed otherwise"; line 107 says participant self-export is "not verified"; line 247 lists Journal export as open; matrix line 180 says "**Journal not exportable**". The API-only statement (line 216) stays correct; the export route is missing.

### 3. Cycles now carry a step count (contradicts "no step time series / not step-based")
- **Fields:** derived_metrics, raw_streams, deprecations (changelog)
- **Found:** API changelog entry dated 2026-09-23 adds `step_count` to the Cycle object under the existing `read:cycles` scope.
- **URL:** https://developer.whoop.com/docs/api-changelog/
- **Quotes:**
  - "Cycles now include the total number of steps taken during the cycle."
  - "null when no step data exists for the cycle"
  - "Covered by the existing read:cycles scope"
- **Date:** 2026-09-23
- **Source type:** vendor_docs
- **KB has it:** contradicts in part. Profile line 75 lists cycle score fields without steps; lines 44 and 215 say no step time series (still true: one total per cycle); line 236 lists "step-based endpoints" as poor fit, which now needs qualifying. Matrix does not mention WHOOP steps.

### 4. Developer tier approvals are stalling for months (bears on the KB's tier plan for cohorts)
- **Fields:** developer_program_status, user_cap, program_application
- **Found:** Multiple developer-forum threads from June to August 2026 report no decision on requests to raise the 10-member Sandbox cap, for 60 days to over 3 months, with no tracking ID.
- **URLs and quotes:**
  - https://www.community.whoop.com/t/production-api-access-submitted-jun-26-no-decision-after-60-days-playerslab-integration-already-built/15628 : "No decision, no denial, and no stated reason in ~60 days" (2026-07-26)
  - https://www.community.whoop.com/t/no-response-on-api-app-approval-to-raise-the-10-user-limit/15246 : "Same here - we have been waiting for a response for over 3 months now" (2026-06-30)
  - https://www.community.whoop.com/t/app-approval-to-raise-the-10-user-limit-3-submissions-since-april-still-no-response-today-ai/15779 : "we’ve had no approval, no rejection, and no timeline beyond the initial auto-reply" (2026-08-06)
- **Source type:** secondary (developer forum, user posts)
- **KB has it:** no. Profile line 99 and matrix lines 43 and 388 describe the tier rules and manual review but give no evidence on turnaround; the profile's cohort-planning advice assumes reviews happen. Treat as Reported.

## Missing programs and research routes

### 5. Digital WHOOP Labs (in-app research platform) and WHOOP Labs
- **Fields:** research_program, program_status
- **Found:** WHOOP runs an in-app remote research feature with stated 2025 scale (200k+ unique participants, 30+ studies). Data are de-identified and restricted to authorised researchers. This is WHOOP's internal research, not a route for outside teams, but it is the source of WHOOP-authored papers.
- **URL:** https://www.whoop.com/us/en/digital-whoop-labs/ (fetched via https://web.archive.org/web/20260727062958/https://www.whoop.com/us/en/digital-whoop-labs/)
- **Quotes:**
  - "Digital WHOOP Labs is an in-app feature that lets you participate in research studies remotely."
  - "Unique participants in 2025"
  - "All research data is de-identified and stored in secure, access-controlled systems, accessible only to authorized researchers."
- **Date:** capture 2026-07-27
- **Source type:** vendor_page
- **KB has it:** no. Profile line 29 mentions an internal clinical research function only.

### 6. Academic collaboration via WHOOP-held member data (Stanford Wu Tsai, npj Digital Medicine 2026)
- **Fields:** research_program, academic_vs_commercial, retention_terms
- **Found:** A Stanford-led paper analysed de-identified WHOOP member data (1.3 million days) under a WHOOP women's-health research consent, with WHOOP co-authors; data stay with WHOOP and are shared only with WHOOP's permission. This shows the practical academic route is collaboration with WHOOP, not the public API.
- **URL:** https://doi.org/10.1038/s41746-026-02799-9 (fetched via https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13482339/fullTextXML)
- **Quotes:**
  - "consented to participate in a women’s health research study"
  - "Data are however available from the authors upon reasonable request and with permission of WHOOP, Inc."
  - "Wu Tsai Human Performance Alliance, Stanford University"
- **Date:** published 2026-05-25
- **Source type:** paper
- **KB has it:** partly. The paper is in `module-01-wearables/literature-library.md` line 107 as validation evidence, but the profile's research-access section (lines 30 to 34) says no research route exists and does not mention this one.

### 7. WHOOP privacy policy: de-identified data used with "research partners"
- **Fields:** research_program, retention_terms, ai_training_terms
- **Found:** Privacy policy (Last Updated August 3, 2026) says WHOOP uses de-identified wellness data for research with research partners, and that its LLM partner has a zero-retention, zero-training policy for WHOOP metrics.
- **URL:** https://www.whoop.com/privacy/full-privacy-policy/ (fetched via https://web.archive.org/web/20260806173749/https://www.whoop.com/privacy/full-privacy-policy/)
- **Quotes:**
  - "We also use de-identified wellness data for research purposes to help us and our research partners answer important questions about human performance"
  - "Last Updated: August 3, 2026"
- **Date:** 2026-08-03
- **Source type:** vendor_legal
- **KB has it:** no.

### 8. Mubadala partnership and the WHOOP–Mubadala Health Research Initiative (UAE)
- **Fields:** research_program, program_status
- **Found:** Announced 2026-05-07 with a $75 million Mubadala investment; WHOOP will launch a research initiative running longitudinal studies with UAE institutions, plus Advanced Labs in the UAE.
- **URL:** https://www.mubadala.com/en/news/mubadala-partners-with-whoop-to-strengthen-preventative-health-and-research-capabilities-in-the-uae
- **Quotes:**
  - "anchored by Mubadala’s $75 million investment in WHOOP"
  - "The WHOOP–Mubadala Health Research Initiative will support structured collaboration with leading UAE institutions to conduct longitudinal studies in cardiovascular health, sleep science, recovery, and behavioral performance."
- **Date:** 2026-05-07
- **Source type:** secondary (partner press release)
- **KB has it:** no.

### 9. Qatar: WHOOP Labs Doha and Qatar Foundation research partnership
- **Fields:** research_program
- **Found:** Invest Qatar partnership (2025-10-28) to set up WHOOP's first international performance lab in Doha, with local research partnerships; Qatar Foundation partnership (2026-05-16) to explore joint research in sports science, wellness and precision health.
- **URLs and quotes:**
  - https://www.einpresswire.com/article/861893774/invest-qatar-partners-with-whoop-to-establish-first-international-performance-lab-in-qatar : "The facility will also enable partnerships with local institutions for sport performance research" (2025-10-28, secondary)
  - https://www.whoop.com/us/en/press-center/qatar-foundation-and-whoop-partner-to-support-careers-skills-and-research-in-health-and-fitness-tech/ (fetched via https://web.archive.org/web/20260617190449/https://www.whoop.com/us/en/press-center/qatar-foundation-and-whoop-partner-to-support-careers-skills-and-research-in-health-and-fitness-tech/) : "QF and WHOOP will work together to explore collaborative research opportunities in areas such as sports science, wellness, and precision health" (2026-05-16, vendor_page)
- **KB has it:** no. Both are regional, institution-level partnerships, not open programs; relevant mainly to researchers in Qatar.

### 10. Vendor-reported group download portal for a fee, and institutional legal review before API access
- **Fields:** export_routes, program_application, minimum_commitment, api_platform_fees
- **Found:** A 2026 experience-based tutorial in *Clinical and Translational Science* says WHOOP sells a web application for group data download, and requires institutional legal review, possibly tied to a minimum device order, before API access.
- **URL:** https://doi.org/10.1111/cts.70693 (fetched via https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13438180/fullTextXML)
- **Quotes:**
  - "Oura and WHOOP provide web applications (with an additional fee) to view and download health data for groups of individuals."
  - "Many manufacturers, including Garmin and WHOOP, require an institutional legal review (which may be conditioned upon a minimum device order) before granting API access, along with a review process for API applications."
- **Date:** 2026
- **Source type:** paper
- **KB has it:** contradicts in part. Profile line 96 and matrix line 180 say no study tooling or group dashboard; line 151 and matrix line 220 say the API is free, which stays true for the public API. The paper is not in the KB (no DOI match).

## Compliance and regulatory

### 11. HIPAA and BAA: WHOOP says it is not a covered entity and a BAA is unnecessary
- **Fields:** baa, hipaa_statement
- **Found:** The Unite research FAQ answers "Is WHOOP required to sign a BAA?" by saying WHOOP is not a covered entity and that the arrangement can be structured to avoid one. The 2026 privacy policy defers to the covered entity's Notice of Privacy Practices when WHOOP processes data on a covered entity's behalf. Separately, Advanced Labs requires a HIPAA authorization so Quest Diagnostics and SteadyMD can share PHI with WHOOP.
- **Quotes:**
  - https://www.sensorlab.arizona.edu/sites/default/files/2023-05/WHOOP%20Unite%20Research%20FAQs_0.pdf : "or the PI can obtain consent to disclosure, making a BAA unnecessary" (2023-05, secondary)
  - https://www.whoop.com/privacy/full-privacy-policy/ (via https://web.archive.org/web/20260806173749/https://www.whoop.com/privacy/full-privacy-policy/) : "our processing of your personal information in that context will be governed by the Notice of Privacy Practices of the relevant covered entity" (2026-08-03, vendor_legal)
- **KB has it:** partly. Profile line 142 covers the API terms' HIPAA clause and says a BAA-type arrangement is "contemplated but none is published". The vendor's research-facing position (BAA unnecessary) is not recorded.
  - https://www.whoop.com/us/en/termsofuse/ (via https://web.archive.org/web/20260604120953/https://www.whoop.com/us/en/termsofuse/) : "you will be required to sign an authorization in accordance with the Health Insurance Portability and Accountability Act of 1996 (HIPAA) permitting Quest Diagnostics and SteadyMD to share your protected health information with WHOOP" ; "Last Updated: April 13, 2026" (vendor_legal; consumer Advanced Labs only, not research)

### 12. GDPR, EU representative, transfer mechanism and data residency
- **Fields:** gdpr_statement, dpa, data_residency
- **Found:** Privacy policy names an EU representative (Whoop Limited, Dublin) and a UK representative, says data are processed in the US, and offers Standard Contractual Clauses to customers on request. The 2023 Unite FAQ says data are stored in AWS West (US), and that WHOOP signs data protection agreements with vendors.
- **Quotes:**
  - https://www.whoop.com/privacy/full-privacy-policy/ (via archive capture above) : "Our EU Representative is: Whoop Limited" ; "Whoop will enter into the Standard Contractual Clauses with our vendors who process personal data, and with our customers upon request." ; "To provide the Services, we will process your Personal Data in the United States, where WHOOP is based." (2026-08-03, vendor_legal)
  - https://www.sensorlab.arizona.edu/sites/default/files/2023-05/WHOOP%20Unite%20Research%20FAQs_0.pdf : "Data is stored in the United States in Amazon Web Services (AWS) West." ; "WHOOP enters into Data Protection Agreements with third-party vendors (when necessary and appropriate)" ; "WHOOP is US Privacy Shield self-certified." (2023-05, secondary; the Privacy Shield line is stale, as the 2026 policy itself says Privacy Shield was invalidated)
- **KB has it:** no. Profile line 143 says GDPR DPA and data residency "were not verified"; line 252 lists them as open.

### 13. Irregular Heart Rhythm Notifications: sold outside the US, not available in the US
- **Fields:** fda_clearances
- **Found:** WHOOP Life (MG) lists Irregular Heart Rhythm Notifications; WHOOP community staff said in May 2025 that IHRN is not available in the US for regulatory reasons. openFDA still shows only K243236 for WHOOP (rechecked 2026-10-10), so IHRN has no US clearance.
- **Quotes:**
  - https://community.whoop.com/t/is-ihrn-available-in-the-us/477 : "No, Irregular Heart Rhythm Notifications (IHRN) are not currently available in the United States due to regulatory restrictions." (2025-05-09, secondary, WHOOP staff reply)
  - https://www.whoop.com/us/en/membership/ (via https://web.archive.org/web/20261002041123/https://www.whoop.com/us/en/membership/) : "Heart Screener with ECG readings Irregular Heart Rhythm Notifications" (capture 2026-10-02, vendor_page)
- **KB has it:** no. Profile lines 194 to 196 cover ECG and BPI only.

## Pricing and device facts

### 14. Official membership prices (Canadian capture) and 14+ day battery
- **Fields:** subscription_price, device_price
- **Found:** The archived membership page (served in CAD to the archive crawler) lists WHOOP One from CA$259/year, Peak CA$349/year, Life CA$529/year, and 14+ day battery for 5.0 and MG. US-dollar prices were not obtainable (whoop.com 403).
- **URL:** https://www.whoop.com/us/en/membership/ (via https://web.archive.org/web/20261002041123/https://www.whoop.com/us/en/membership/)
- **Quotes:** "Starting at CA$259/year." ; "Available at CA$349/yr" ; "Available at CA$529/yr" ; "Everything on WHOOP One, plus WHOOP 5.0 with 14+ day battery"
- **Date:** capture 2026-10-02
- **Source type:** vendor_page
- **KB has it:** partly. Profile line 148 and matrix line 220 give US prices from secondary sources (Reported); the CAD figures are the only vendor-page prices found. Matrix line 200 says battery is "Not stated in the profile".

## Lower-value context

### 15. Researcher demand for WHOOP in All of Us; member complaints on data granularity
- **Fields:** academic_vs_commercial, raw_streams
- **Found:** A member asked WHOOP (April 2026) to engage with the All of Us research community; another thread (May 2026) says neither API nor export gives intraday HR or sleep-stage epochs.
- **Quotes:**
  - https://www.community.whoop.com/t/research-data-sharing/14542 : "It would be a significant gesture of the value of Whoop if they would engage with the ALL OF US research community." (2026-04-15)
  - https://www.community.whoop.com/t/please-open-up-access-to-my-data-through-any-channel/14709 : "Both the API and the export only return per-stage totals." ; "The export doesn’t have it either." (2026-05-04, referring to intraday HR)
- **Source type:** secondary (forum)
- **KB has it:** no for All of Us (WHOOP is not an All of Us source); the granularity point matches the profile and adds the export side.

## Searched, nothing found
- New FDA clearances or letters: openFDA 510(k) (`applicant:whoop`) returns only K243236; registration listing shows QDA only. No new warning letter after the 17 June 2026 close-out found.
- SOC 2 report, ISO 27001 certificate, public trust portal: none found by web search. Only a WHOOP job ad listing SOC 2 and ISO 27001 familiarity as a plus.
- EU-US Data Privacy Framework listing for WHOOP: not found by search (dataprivacyframework.gov not checked directly). The privacy policy relies on SCCs.
- Fitabase and Labfront: no WHOOP integration found. Terra lists a WHOOP integration that runs on the developer's own WHOOP app credentials and approval, so it does not bypass the tier caps.
- GitHub: no official WHOOP SDK or API repo (WhoopInc org holds only old infrastructure tools).
- API changelog: no deprecations or shutdown dates after the v1 webhook removal (2025-11-01); newest entry is the 2026-09-23 step count.
- Published academic or research pricing, or a named academic program open to outside teams: none found. B.yaml separately records a research contact Typeform on whoop.com.
- WHOOP 5.0/MG independent validation: not re-searched (profile line 187 covers it as of 2026-10-09).
- Scuderia Ferrari partnership (2026): includes a joint research paper with the team's medical staff; not relevant to research data access, not quoted.
