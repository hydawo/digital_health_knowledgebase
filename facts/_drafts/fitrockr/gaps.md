# Gap hunter: fitrockr

Run: started 2026-10-11, finished 2026-10-21. All quotes below re-probed on 2026-10-21 with
`tools/facts/quote_probe.py` and returned "exact".

**Access note.** fitrockr.com (and api.fitrockr.com) answered every automated request with HTTP 403
from a MalCare WordPress firewall ("Blocked because of Malicious Activities"). This was not bypassed.
Every fitrockr.com quote below was probed against a Wayback Machine capture via `--fetch-url`; the
capture timestamp is given with each one. The live page may have changed since the capture. The
judge should treat these as `vendor_*` sources read through an archive, dated by capture.

KB locations used for comparison:
- Profile section: `module-01-wearables/profiles/data-intermediaries.md` lines 104-116 (Fitrockr table: devices L109, tooling L110, pricing L111, hosting and compliance L112, grants L113)
- `module-01-wearables/profiles/garmin.md` L98 (grants), L91
- `module-01-wearables/comparison-matrix.md` L231, L338, L344-360, L407
- `facts/fitrockr.yaml`: every field `unresearched`

---

## A. Contradictions and narrowings

### A1. ISO 27001 applies to the hosting centre, not to Fitrockr (iso27001)
- **Found:** Fitrockr's own Privacy & Security help page scopes the ISO claim to its cloud hosting centre. The KB quotes the vendor's broader "HIPAA-, CASA- and ISO-certified" line without this scoping. A search for an ISO 27001 certificate naming Fitrockr or Digital Rebels GmbH found none.
- **URL:** https://www.fitrockr.com/research/help-center/privacy-security/ (Wayback capture 20251204202409)
- **Quote:** "Our Cloud hosting center is ISO/IEC 27001 certified"
- **Second URL:** https://www.fitrockr.com/country-of-choice-cloud-hosting/ (capture 20260313045514)
- **Quote:** "By default, the Fitrockr platform is hosted at an ISO-certified hosting center in Germany"
- **Date:** captures 2025-12-04 and 2026-03-13
- **Source type:** vendor_docs, vendor_page
- **KB has it:** contradicts, in part. data-intermediaries.md L112 says the vendor "States 'HIPAA-, CASA- and ISO-certified. GDPR-compliant.' with no certificate linked". That line is accurate as a quote, but the vendor's own documentation scopes ISO to the data centre. The record should say so (Reported, self_claim_cap applies).

### A2. "HIPAA certification" is a self-described certification (hipaa_statement)
- **Found:** a 2023 Fitrockr news post says it "received the certification" for HIPAA. HIPAA has no certifying body, and no certifier is named. The help page elsewhere says only "We comply to HIPAA". No BAA offer was found in any captured page.
- **URL:** https://www.fitrockr.com/fitrockr-received-hipaa-certification/ (capture 20250115192203; post dated Jan 1, 2023)
- **Quote:** "we have worked on HIPAA compliance and have successfully received the certification"
- **Source type:** vendor_page
- **KB has it:** partly. L112 keeps it as a vendor claim but does not say no certifier is named or that no BAA is published.

### A3. Default hosting: Germany or Switzerland, not just Germany (data_residency)
- **Found:** the research help page lists both Germany and Switzerland. The add-on page says Germany by default. The KB lists only Germany.
- **URL:** https://www.fitrockr.com/research/help-center/privacy-security/ (capture 20251204202409)
- **Quote:** "ISO-certified cloud servers located in Germany or Switzerland."
- **Source type:** vendor_docs
- **KB has it:** contradicts, mildly. L112: "Germany cloud included". Record both, labelled as a minor inconsistency in the vendor's pages.

## B. Missing programs and program detail

### B1. Grant packages include platform access, and the 2024 and 2025 rounds offered 3 months (research_program, academic_pricing, user_cap)
- **Found:** the Asia 2026 grant gave 6 months of platform access for up to 50 participants as well as hardware. The Biomarkers 2024 and ANZ 2025 rounds gave 5 Garmin wearables and 3 months of access for up to 50 users. Garmin's own release confirms the platform-access part.
- **URL:** https://www.fitrockr.com/research/research-grants/ (capture 20260713062221)
- **Quote:** "6 months unrestricted access to the Fitrockr Health Solutions Platform for up to 50 participants"
- **Quote (2024/2025 rounds, same page):** "3 months unrestricted access to the Fitrockr Health Solution Platform for up to 50 users"
- **Second URL:** https://www.garmin.com/en-PH/newsroom/press-release/news-2026-mar-fitrockr/ (live, 2026-10-21)
- **Quote:** "Full Platform Access: 6 months of unrestricted access to the Fitrockr Health Solutions Platform."
- **Source type:** vendor_page; secondary (Garmin newsroom; Garmin is a partner, not the subject)
- **KB has it:** no. data-intermediaries.md L113 and garmin.md L98 mention only "five vívoactive 5 units".

### B2. Asia 2026 grant winners are published; there is a longer grant history (program_status, research_program)
- **Found:** the grants page lists ten Asia 2026 awardees, from Hong Kong, Japan, Singapore, Thailand, mainland China, Malaysia, Indonesia and Taiwan. It also lists past rounds with named winners: ANZ 2025 (Western Health, Otago), Biomarkers 2024 (Imperial, UAB, KUNO Regensburg, UPM, Geneva and others), India 2024, and Americas and EMEA 2023 (archived news posts). As of the July 2026 capture, no grant is open.
- **URL:** https://www.fitrockr.com/research/research-grants/ (capture 20260713062221)
- **Quote:** "Kota Maekawa, Kobe City Medical Center General Hospital"
- **Quote:** "New grants will be announced soon."
- **Source type:** vendor_page
- **KB has it:** partly. The KB says Asia 2026 closed and no current grant is listed (L113, verified 2026-10-10). It does not have the winners or the rounds before 2025. The "no current grant" status is consistent, but only as of the July capture, because the live page could not be read on 2026-10-21.

## C. Deprecations and data-access changes

### C1. Sleep data dropped for 13 older Garmin models on Fitrockr-app sync from Sep 2025 (deprecations)
- **Found:** with the move to new Garmin sync technology (by 7 Sep 2025), Garmin no longer provides sleep data for vívosmart 4, vívofit 4, vívomove 3/Style, vívomove Sport, vívoactive 4, Venu Sq, Venu, Lily, Instinct, Instinct Solar, and Forerunner 245, 45 and 55. This applies only when syncing through the Fitrockr app. Projects syncing through Garmin Connect are not affected. Older studies (for example PMC13133593, which used the vívosmart 4, and PMC12536430, which used the vívoactive 4) used affected models.
- **URL:** https://www.fitrockr.com/research/help-center/important-update-upcoming-transition-to-new-garmin-sync-technology/ (capture 20251204202903)
- **Quote:** "As part of this transition, sleep data provision will no longer be supported by Garmin for the following device models"
- **Quote:** "This limitation applies only to projects that use the ‘Fitrockr app’ for syncing"
- **Source type:** vendor_docs
- **KB has it:** no. Nothing in data-intermediaries.md, garmin.md or the matrix. This is probably the single most decision-relevant missing item for anyone reusing older Garmin stock.

### C2. GPS can be switched off per study, including in raw exports (raw_streams, export_routes)
- **Found:** a news post dated May 27, 2026 says administrators can disable GPS for a study, so location never appears in dashboards or raw exports. This matters for ethics and DPIA scope.
- **URL:** https://www.fitrockr.com/disable-gps-data/ (capture 20260616113942)
- **Quote:** "When GPS is disabled for a study, location data is not exposed or visible anywhere in the platform"
- **Source type:** vendor_page
- **KB has it:** no.

### C3. Google Fitbit Air supported from June 2026 (raw_streams / device coverage)
- **Found:** a post dated Jun 4, 2026 claims full compatibility with the Fitbit Air, via the Google Health app, on all subscriptions. (The page misspells it "Fibit".)
- **URL:** https://www.fitrockr.com/google-fitbit-air-compatibility/ (capture 20260616114651)
- **Quote:** "Fitrockr is compatible with the newly released Google Fibit Air wearable."
- **Source type:** vendor_page
- **KB has it:** no. L109 lists Google and Fitbit generically. Whether the data comes via the Google Health API or Health Connect is not stated.

## D. Data terms

### D1. Each project gets its own server instance, deleted with all data at study end (retention_terms)
- **URL:** https://www.fitrockr.com/research/help-center/privacy-security/ (capture 20251204202409)
- **Quote:** "Each research project receives its own server instance which will be completely deleted including all data at the end of the study."
- **Related:** the Data Vault add-on is the paid route to keep read-only access afterwards. Data Vault page (capture 20260414153944): "Secure, hosted storage of your collected data with read-only access after your main project phase."
- **Related, participant accounts:** privacy policy (last updated Jan 28, 2026; capture 20260511152739): "As soon as your account is deleted, we will delete all your personal data, and keep your activity log anonymously."
- **Source type:** vendor_docs, vendor_page, vendor_legal
- **KB has it:** partly. L111 and matrix L407 have the Data Vault price but not the deletion-at-study-end rule that makes it necessary.

### D2. Data used only for the project purpose; no AI or ML terms found (ai_training_terms)
- **URL:** https://www.fitrockr.com/research/help-center/privacy-security/ (capture 20251204202409)
- **Quote:** "Fitrockr is a sole software service provider without any business or intentions in any data. Data is only used for the project purpose."
- **Related:** Health and Health Research Terms (effective May 27, 2024; capture 20250219072301): "We do not collect data for own research purposes."
- **Source type:** vendor_docs, vendor_legal
- **KB has it:** no. The privacy policy (Jan 2026 capture) contains no AI, machine-learning or model-training language, so the field could be recorded as not_public, with this purpose-limitation quote as context.

## E. API and export routes

### E1. Two APIs, access by email, reference code shared on GitLab (export_routes, api_platform_fees)
- **Found:** the help centre describes a REST DATA-API covering all synced data, and a LIVE-DATA-API that requires the Live add-on. Access details are requested by email, and reference implementations are shared via GitLab. A University of Bern open-source plugin (MPL-2.0, last pushed 2024-07-26) shows the REST API at api.fitrockr.com/v1 (users, dailySummaries, activities endpoints) using an API key and a tenant header.
- **URL:** https://www.fitrockr.com/help-center/fitrockr-api/ (capture 20250909230659)
- **Quote:** "Fitrockr LIVE-DATA-API can only be used if wearable data is live streamed (requires Live Add-on)."
- **Quote:** "Request API access information at support@fitrockr.com"
- **Second URL:** https://raw.githubusercontent.com/humdek-unibe-ch/sh-shp-fitrockr/HEAD/server/component/fitrockrAPI/FitrockrAPIModel.php (live)
- **Quote:** "Get daily summaries for a user."
- **Third URL:** https://github.com/humdek-unibe-ch/sh-shp-fitrockr
- **Quote:** "This is a SelfhelpPlugin that is used for Fitrockr integration"
- **Source type:** vendor_docs; repository
- **KB has it:** partly. L111 has "API access +20%". The two-API split, the live-stream add-on dependency and the gated docs are missing. API docs are not public (api.fitrockr.com returned 403), so rate_limits and history_depth stay not_public.

## F. How researchers actually use it (papers)

### F1. Raw 25 Hz accelerometer exported as CSV, corroborating the KB's 25 Hz figure (sampling_rates, export_routes)
- **URL:** https://pmc.ncbi.nlm.nih.gov/articles/PMC12975902/ (Front Aging 2026, nursing-home dementia, Garmin Venu 3)
- **Quote:** "For each participant, raw acceleration (25 Hz) was exported from the Fitrockr hub/platform in the Comma-Separated Values (CSV) format."
- **Also:** https://pmc.ncbi.nlm.nih.gov/articles/PMC13524361/ (JMIR 2026, one-year study): "Raw data parameters for the smartwatches were synced, paired, and retrieved using a hub through Fitrockr"
- **Source type:** paper
- **KB has it:** yes for the 25 Hz figure (L111, vendor). The papers add independent corroboration. 10.2196/95194 is already in Module 3's scan queue; 10.3389/fragi.2026.1768935 is not in the KB.

### F2. Manual sync burden on the Fitrockr Hub app (study operations; bears on export_routes)
- **Found:** a pulmonary-rehab study using the vívosmart 4 had patients sync by hand twice a day because the app did not sync automatically. Fitrockr's 2025 review lists "Garmin Background Syncing" as a 2025 feature, so this may describe an older app state.
- **URL:** https://pmc.ncbi.nlm.nih.gov/articles/PMC13133593/ (JMIR 2026)
- **Quote:** "As the mobile app does not synchronize automatically with the smart band, patients were asked to manually synchronize them twice a day"
- **Source type:** paper
- **KB has it:** no.

### F3. Clinic-hosted deployment and FHIR integration via the API (hosting_options, data_residency, export_routes)
- **URL:** https://pmc.ncbi.nlm.nih.gov/articles/PMC12653439/ (J Clin Med 2025, congenital heart disease, Bern)
- **Quote:** "This setup allowed continuous and automated data transfer to a clinic’s internal cloud infrastructure."
- **URL:** https://pmc.ncbi.nlm.nih.gov/articles/PMC12536430/ (Front Digit Health 2025, EHDS/FHIR case study)
- **Quote:** "This study used the Garmin Vívoactive 4 smartwatch to collect PGHD and integrate it into a FHIR server via the Fitrockr hub and API."
- **Source type:** paper
- **KB has it:** no (local hosting is listed as an add-on in L112, but there is no evidence of use).

### F4. Smartphone compatibility as an exclusion criterion (study operations)
- **URL:** https://pmc.ncbi.nlm.nih.gov/articles/PMC13446883/ (2026 protocol, SCORE2 surrogates, Bern)
- **Quote:** "smartphone incompatibility with Fitrockr"
- **Source type:** paper
- **KB has it:** no.

## G. Scale and app presence

### G1. Usage scale stated by the vendor for 2025 (context for program_status)
- **URL:** https://www.fitrockr.com/2025-year-in-review/ (capture 20260515072720)
- **Quote:** "So far, we supported 300+ projects"
- **Quote:** "with 27,000 daily participants actively engaging with the platform"
- **Source type:** vendor_page
- **KB has it:** no.

### G2. Participant app on the App Store, actively updated (app_availability, if applied to intermediaries)
- **Found:** "Fitrockr Sync" by Digital Rebels GmbH, first released 2024-05-31, version 20261006.1 released 2026-10-07 (iTunes lookup API).
- **URL:** https://apps.apple.com/us/app/fitrockr-sync/id6480404044
- **Quote:** "Fitrockr Sync is the participant and patient app for the Fitrockr Health Solutions platform"
- **Source type:** app_store
- **KB has it:** no. The legal entity, Digital Rebels GmbH, is also not named in the KB (L108 says only "Fitrockr (Berlin)").

---

## Searched, nothing found
- ISO 27001 certificate naming Fitrockr or Digital Rebels GmbH (web search): none.
- CASA letter of validation or tier for Fitrockr: none public.
- BAA or DPA template, or a partner or university mentioning one with Fitrockr: none.
- SOC 2 or a trust portal: none.
- FDA or CE/MDR status: none (it is a software data platform; no device claims found).
- AI, ML or model-training language in the privacy policy (Jan 2026 capture) and the participant terms: none.
- Public API reference or rate limits: not public (docs gated by email; api.fitrockr.com 403).
- WHOOP-specific integration announcement: none found beyond the compatible-devices listing.
- A new grant after Asia 2026: none on the July 2026 capture or in Garmin newsrooms. The live page could not be checked.
- Google Play listing for the participant app: not found via search (a 2024 Android "Fitrockr Sync" news post exists on fitrockr.com but could not be read).
- Job postings, developer forum or changelog: nothing research-relevant beyond the help centre and news posts above.
- Live fitrockr.com pages on 2026-10-11 and 2026-10-21: blocked by the site firewall. Not bypassed.
