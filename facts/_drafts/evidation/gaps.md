# Gap hunter findings: evidation

Run date: 2026-10-11. Every quote below returned "exact" from `tools/facts/quote_probe.py` on 2026-10-11.
Profile: `module-02-digital-phenotyping/profiles/evidation.md` (cited as "profile"). Matrix:
`module-02-digital-phenotyping/comparison-matrix.md` (cited as "matrix"). `facts/evidation.yaml` has
every field `unresearched`, so it lacks all of these.

## Contradictions

### 1. Leadership dates: CEO appointed March 2025 and CMO December 2025, not 2026
- **Field:** program_status (context only; no schema field for leadership)
- **Found:** Leslie Oley Wilberforce became CEO on 2025-03-06, succeeding Christine Lemke. Dr. Ghazanfar Khan became Chief Medical Officer on 2025-12-02. The profile says both were "appointed in 2026".
- **URLs and quotes:**
  - https://evidation.com/resources/evidation-appoints-leslie-oley-wilberforce-as-ceo : "March 6, 2025 — Evidation, the leader in direct-to-participant real-world data and health research, today announced the appointment of Leslie Oley Wilberforce as Chief Executive Officer"
  - https://evidation.com/resources/evidation-appoints-dr-ghazanfar-khan-as-chief-medical-officer : "December 2, 2025 — Evidation, the leader in direct-to-participant real-world data and health research, today announced the appointment of Dr. Ghazanfar Khan as Chief Medical Officer"
- **Date:** 2025-03-06 and 2025-12-02
- **Source type:** vendor_page (press releases)
- **KB has it:** contradicts. Profile line 9 ("a new chief executive and chief medical officer appointed in 2026").

### 2. Non-US deployment: Evidation is the participant platform for the UK's Our Future Health
- **Field:** hosting_options / app_availability / data_residency
- **Found:** Our Future Health (UK, target up to five million participants) selected Evidation in November 2023 to supply its participant-facing app and technology infrastructure, accessible by app or browser, with wearable integration planned. The profile treats Evidation as US-only and lists "Studies outside the United States" as a poor fit. That holds for Evidation's own member base, but the company has run a white-label participant platform for a non-US national cohort. Whether Evidation still runs the OFH platform in 2026 was not confirmed; Dr. Khan's release (2025-12-02) says he came from OFH, where he was Executive Director of Digital Health.
- **URLs and quotes:**
  - https://evidation.com/resources/evidation-selected-by-our-future-health-as-participant-platform-for-uks-largest-health-research-program : "Evidation's technology will power the digital experience, including a participant-facing app and technology infrastructure"
  - https://ourfuturehealth.org.uk/news/our-future-health-welcomes-evidation-as-new-technology-provider-to-enhance-volunteer-experience/ : "integrate wearable technology, such as fitness trackers and smart watches"
- **Date:** 2023-11-16 (the Evidation page's structured metadata says 2024-10-15; the dateline says 2023-11-16)
- **Source type:** vendor_page; secondary (partner's own newsroom)
- **KB has it:** contradicts (partly). Profile line 154 ("United States centred membership; international availability is Unclear") and line 168 ("Studies outside the United States" under Poor-Fit). No mention of Our Future Health anywhere in the KB.

## Missing programs and access routes

### 3. Everyone Registry data is shared, coded, with "research partners"; US-wide eligibility
- **Field:** research_program / program_eligibility / academic_vs_commercial
- **Found:** Evidation's member-facing page for the Evidation Everyone Research Registry (2025-12-18) says shared data is coded before going to research partners and that members can take part from anywhere in the US. This partly answers the profile's open question on whether the registry reaches outside researchers: data go to "research partners", but who qualifies and on what terms is not stated.
- **URL:** https://evidation.com/blog/shape-the-future-of-health-research
- **Quotes:** "The data you share is coded before it’s shared with research partners" ; "You can participate from anywhere in the U.S., whenever it works best for you"
- **Date:** 2025-12-18
- **Source type:** vendor_page
- **KB has it:** no. Profile line 97 says the ISPOR abstract "does not say whether outside researchers can access it"; line 176 keeps it open.

### 4. WAVE study: BARDA-funded, 18,157 enrolled, coded data sharing with approved external partners planned but undecided
- **Field:** research_program / academic_vs_commercial / raw_streams
- **Found:** NCT06207929, sponsored by Evidation Health with the Biomedical Advanced Research and Development Authority as collaborator. Decentralised, 2024-01-21 to 2024-08-07, 18,157 actual enrolment, paired wearable data, symptoms and PCR results. IPD sharing is "UNDECIDED", and the statement describes a planned route for approved external research partners. This is a second potential non-sponsor data route, alongside ALiR.
- **URL:** https://clinicaltrials.gov/study/NCT06207929 (probed through https://clinicaltrials.gov/api/v2/studies/NCT06207929, since the study page renders client-side)
- **Quotes:** "We have provisions in our study protocol and consent to share Coded Study Data with approved external research partners. The sharing process is not yet finalized." ; "Biomedical Advanced Research and Development Authority"
- **Date:** record last updated 2024-09-05
- **Source type:** regulator_db (ClinicalTrials.gov registry)
- **KB has it:** no. The WAVE study and BARDA funding appear nowhere in the KB.

### 5. 1upHealth partnership: the EHR linkage route is 1up Patient Connect (FHIR)
- **Field:** export_routes / raw_streams
- **Found:** Since October 2024 Evidation has integrated 1upHealth's FHIR-based Patient Connect so members can authorise their health-record data for Evidation research. This is the mechanism behind the profile's "EHR linkage" and the Everyone Registry's 75 percent EHR opt-in.
- **URL:** https://evidation.com/resources/evidation-partners-with-1uphealth-to-integrate-diverse-sources-of-permissioned-real-world-health-data-for-research
- **Quote:** "Evidation will integrate 1up Patient Connect into its enterprise offering to allow individuals to permission their health record data for Evidation research"
- **Date:** 2024-10-17
- **Source type:** vendor_page (press release)
- **KB has it:** no. The profile mentions EHR linkage (lines 27, 97) but not how it is done.

### 6. Cohort data sold as data access plus on-demand analyses; GLP-1 cohort of 165,000 since July 2024
- **Field:** api_platform_fees / quote_required / export_routes
- **Found:** The July 2026 GLP-1 release directs organisations to partner@evidation.com for "available data, on-demand analyses, and population-level insights" from a cardiometabolic and weight management cohort of more than 165,000 people. This shows a second commercial model beyond commissioned studies: licensing existing cohort data and buying analyses.
- **URL:** https://evidation.com/resources/growth-potential-and-uneven-adoption-in-the-glp-1-market
- **Quote:** "can contact partner@evidation.com to discuss available data, on-demand analyses, and population-level insights"
- **Date:** 2026-07-02 (dateline; page metadata says 2026-07-13)
- **Source type:** vendor_page (press release)
- **KB has it:** no. Profile line 128 says pricing goes through "the vendor's form" and does not mention the partner address or the data-plus-analyses offer.

## Data terms (member privacy notice, not fetched by the KB)

### 7. Member Privacy Notice updated 2026-07-13 allows machine learning and AI use of personal information
- **Field:** ai_training_terms
- **Found:** The separate Member Privacy Notice (the one the profile says was not fetched) is dated 2026-07-13. It lists machine learning and other AI methods within "service delivery" for certain services.
- **URL:** https://evidation.com/members-privacy
- **Quotes:** "Evidation Member Privacy Notice Last Updated : July 13, 2026" ; "for certain Services, this includes using personal information in machine learning and other artificial intelligence methods"
- **Date:** 2026-07-13
- **Source type:** vendor_legal
- **KB has it:** no. Profile line 122: "A separate privacy notice governs the consumer app. It was not fetched".

### 8. Retention for research participants is set per study consent, not in the notice
- **Field:** retention_terms
- **Found:** The member notice defers retention periods for Health Program (research) participants to each study's informed consent. Sponsors and researchers need the consent document to know retention terms.
- **URL:** https://evidation.com/members-privacy
- **Quote:** "applicable retention periods for data processed in connection with your participation may be described in the terms of the specific informed consent"
- **Date:** 2026-07-13
- **Source type:** vendor_legal
- **KB has it:** no.

### 9. Member data hosted primarily in US data centres
- **Field:** data_residency
- **URL:** https://evidation.com/members-privacy
- **Quote:** "Currently, we primarily use data centers in the United States"
- **Date:** 2026-07-13
- **Source type:** vendor_legal
- **KB has it:** yes in the matrix (line 163, "US data centres"), but the profile cites only the corporate notice. This adds the member-notice source.

## Compliance evidence

### 10. Published security.txt with a PGP key and a vulnerability contact
- **Field:** soc2 / iso27001 (context only; not certification evidence)
- **Found:** evidation.com publishes a security.txt (expires 2027-08-21) naming vuln@evidation.com and an OpenPGP fingerprint. The member notice names a different address (security@evidation.com). No SOC 2 report, ISO 27001 certificate, trust portal or BAA was found anywhere; hackerone.com/evidation returns 404.
- **URL:** https://evidation.com/.well-known/security.txt
- **Quote:** "Contact: mailto:vuln@evidation.com"
- **Date:** checked 2026-10-11
- **Source type:** vendor_docs
- **KB has it:** no. Profile line 123 records only that /security and /trust return 404.

## Searched, nothing found
- FDA openFDA 510(k), classification and registration/listing: no Evidation entries (2026-10-11). fda_clearances can be `not_applicable` or `not_public` with this check as evidence.
- SOC 2, ISO 27001 certificate registries, trust portal, HIPAA BAA: nothing found beyond the security.txt; UpGuard's external scan (secondary, not an audit) is the only third-party security item.
- Public API, developer portal, GitHub: none (agrees with profile).
- Academic or grant program on vendor pages: none, apart from the Everyone Registry and WAVE routes above.
- Funding: latest round found is the 2021 Series E; no 2025 or 2026 funding, layoff or shutdown news.
- Fitbit-to-Google account migration (deadline 2026) effect on Evidation connections: no Evidation-specific notice found. help.evidation.com returns HTTP 403 to automated fetches, so help-centre articles (including the EHR FAQ) could not be checked.
- American Heart Association "Research Goes Red" partnership: reported by Fierce Biotech (403 to the probe); Evidation's CEO release confirms only that it has partnered with the AHA and the Michael J. Fox Foundation. Not quoted here.
- Pharmaphorum interview with the CEO: headline seen in search results only; not read.
- Integrator pages (Fitabase, Labfront, Terra, Thryve): not relevant, since Evidation takes wearable data in rather than being a source integrators connect to.
