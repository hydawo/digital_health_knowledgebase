# Gap hunt: lifedata (LifeData LLC, RealLife Exp / LifeData+)

Run date: 2026-10-11. Gap hunter, baseline fact run. Compared against
`module-02-digital-phenotyping/profiles/lifedata.md` (cited below as "profile"),
`module-02-digital-phenotyping/comparison-matrix.md` ("matrix") and `facts/lifedata.yaml`
(every field still `unresearched`, so every finding below is "no" against the YAML; the KB column
refers to the profile and matrix). Every quote was checked with `tools/facts/quote_probe.py` and
returned `exact`.

## Contradictions and corrections first

### 1. LifeData (LifeData+) Android app now declares sharing data with third parties
- **Field:** app_availability (also bears on retention_terms / dpa)
- **Found:** The Google Play listing for the LifeData+ participant app (`com.lifedata.lifedata`) now says the app may share "Device or other IDs" with third parties, for app functionality and analytics. It was updated on Oct 8, 2026. The profile records this app as sharing nothing with third parties.
- **URL:** https://play.google.com/store/apps/details?id=com.lifedata.lifedata&hl=en_US ; detail at https://play.google.com/store/apps/datasafety?id=com.lifedata.lifedata&hl=en_US
- **Quotes:** "This app may share these data types with third parties Device or other IDs" ; "Device or other IDs App functionality, Analytics" ; "Updated on Oct 8, 2026"
- **Date:** checked 2026-10-11
- **Source type:** app_store
- **KB:** contradicts. Profile line 317 says the LifeData app "shares no data with third parties". Profile line 51 gives the Android update date as 2026-07-18 (now Oct 8, 2026).

### 2. Data Privacy Framework status confirmed on the regulator's list, with details the KB lacks
- **Field:** gdpr_statement (also dpa, data_residency)
- **Found:** The Department of Commerce DPF participant API lists LifeData (Marion, IN) as an active participant in all three frameworks. Status is "Active - Re-certification under Review". EU-U.S. and Swiss-U.S. original certification 2018-05-31 (so continuous from the Privacy Shield era), UK Extension 2023-10-31, next certification due 2027-04-28. Covers HR and non-HR data. Verification method is self-assessment. One recorded lapse, 2019-06-30 to 2019-07-08. Recourse is the EU DPAs, the Swiss FDPIC and the UK ICO, with the FTC as statutory body. LifeData describes itself as a data processor. The privacy policy registered there is dated 2024-06-12 and described as updated on input from the DPF. Company size field: "Fewer than 100".
- **URL:** https://dpfapi.azurewebsites.net/api/participants/6382 (the JSON behind https://www.dataprivacyframework.gov/list, searched for "LifeData")
- **Quotes:** "Active - Re-certification under Review" ; "LifeData operates as a Data Processor" ; "Self-Assessment" ; "2018-05-31T12:00:00+00:00" ; "2023-10-31T12:00:00+00:00" ; "2027-04-28T12:00:00+00:00" ; "Lapse" ; "2019-06-30T12:00:00+00:00" ; "This is the current LifeData Privacy Policy since June 12, 2024 that was updated per input from DPF."
- **Date:** checked 2026-10-11
- **Source type:** regulator_db
- **KB:** no (upgrade). Profile line 157 holds this at Corroborated because the registry "returned errors to automated requests" and asks a human to confirm. Matrix line 162 says "self-certification". The registry now confirms it independently. The "re-certification under review" status, the 2019 lapse and the self-assessment verification method are not in the KB.

### 3. Profile's app-version table is internally stale
- **Field:** app_availability
- **Found:** App Store lookup gives LifeData v1.0.17 released 2026-10-10 (notes: "Performance improvement, bug fixes and UI flow update."), min iOS 18.0; RealLife Exp v2.8.14 of 2026-04-06, min iOS 13.0. The LifeData app's App Store page also lists Mac (Apple silicon) compatibility.
- **URL:** https://apps.apple.com/us/app/lifedata/id6443996884 ; https://itunes.apple.com/lookup?id=6443996884&country=us
- **Quote:** "Requires iOS 18.0 or later." (App Store page)
- **Date:** checked 2026-10-11
- **Source type:** app_store
- **KB:** contradicts within the profile. Quick Facts (line 10) already says v1.0.17 of 2026-10-10, but the platform table (line 50) still says v1.0.16 of 2026-08-27.

## Missing from the KB

### 4. Real prices paid: three U.S. Department of Veterans Affairs contracts
- **Field:** subscription_price, academic_pricing, minimum_commitment, quote_required
- **Found:** USAspending lists three firm-fixed-price VA contracts to LIFEDATA LLC (UEI CVHBNZ7KQWB3), all for VA San Diego Healthcare System through Network Contract Office 22, NAICS 518210:
  - 36C26224C0205, "LIFEDATA SURVEY SUBSCRIPTION": period 2024-05-01 to 2027-04-30, potential end 2029-04-30, sole source under FAR 6.302-1. API fields: total obligation 18000.0, base and all options 25360.0. Transactions endpoint: base 3680.0 (2024-05-01), option year 1 3680.0 (2025-04-06), modification increase 3480.0 (2025-06-23), option year 2 7160.0 (2026-03-19).
  - 36C26224C0221, "LIFEDATA ACADEMIC RESEARCH SERVICES": 2024-05-30 to 2025-05-29, total obligation 3480.0.
  - 36C26223P0320, "LIFE DATA RESEARCH": 2023-06-01 to 2024-12-05 (potential end 2027-05-31), total obligation 13920.0.
- **URLs:** https://api.usaspending.gov/api/v2/awards/CONT_AWD_36C26224C0205_3600_-NONE-_-NONE-/ ; https://api.usaspending.gov/api/v2/awards/CONT_AWD_36C26224C0221_3600_-NONE-_-NONE-/ ; https://api.usaspending.gov/api/v2/awards/CONT_AWD_36C26223P0320_3600_-NONE-_-NONE-/ ; transactions via POST https://api.usaspending.gov/api/v2/transactions/
- **Quotes (all exact on the award URLs):** "LIFEDATA SURVEY SUBSCRIPTION" ; "ONLY ONE SOURCE-OTHER (FAR 6.302-1 OTHER)" ; "664-SAN DIEGO HEALTHCARE SYS(00664)" ; "FIRM FIXED PRICE" ; "CVHBNZ7KQWB3" ; "LIFEDATA ACADEMIC RESEARCH SERVICES" ; "LIFE DATA RESEARCH" ; "2029-04-30"
- **Caveat:** quote_probe strips numeric JSON values, so the dollar amounts could not be probed. They are copied from the API's `total_obligation`, `base_and_all_options` and transaction `federal_action_obligation` fields, not reconstructed. The number of researchers and participants each contract covers is not stated, so these are price points for one VA site, not list prices. Reading the base and option-year amounts as an annual subscription of roughly that size is inference.
- **Date:** checked 2026-10-11
- **Source type:** secondary (federal spending record; not a certificate)
- **KB:** no. Profile lines 173 to 186 and matrix line 138 say no figures exist anywhere.

### 5. LifeData+ console asks study owners whether they will handle PHI, and puts GDPR on the researcher
- **Field:** hipaa_statement, baa, gdpr_statement
- **Found:** The public JavaScript of the LifeData+ researcher console (`app.lifedatacorp.com`) contains onboarding fields "Protected Health Information (PHI)" and "GDPR". The PHI tooltip asks study owners to say whether they will collect, store or transmit PHI. The GDPR tooltip says researchers decide whether GDPR applies and meet its requirements. This shows a product-level PHI switch exists. It does not show that a BAA is signed.
- **URL:** https://app.lifedatacorp.com/assets/index-HDLErs9z.js (bundle filename is build-specific and will change)
- **Quotes:** "Protected Health Information (PHI) is individually identifiable health information protected under HIPAA." ; "Select Yes if you plan to use LifeData to collect, store, or transmit PHI" ; "Researchers are responsible for determining whether GDPR applies to their study and for meeting applicable requirements"
- **Date:** checked 2026-10-11
- **Source type:** vendor_docs (product UI text, not documentation)
- **KB:** no. Profile line 167 treats HIPAA as marketing-only with no product or legal backing.

### 6. Features page now words HIPAA as "support" for compliant workflows
- **Field:** hipaa_statement
- **Found:** Under the "HIPAA & GDPR Compliance" heading, the LifeData+ features page (sitemap lastmod 2026-06-27) now says the platform supports HIPAA- and GDPR-compliant workflows through configurable privacy and consent options. That is weaker than "is HIPAA compliant" wording on older pages.
- **URL:** https://www.lifedatacorp.com/features/
- **Quote:** "Support HIPAA- and GDPR- compliant research workflows with configurable privacy and consent options"
- **Date:** checked 2026-10-11
- **Source type:** vendor_page
- **KB:** no. Profile lines 167 and 306 record only the heading and the older "is HIPAA and GDPR compliant" wording.

### 7. LifeData+ app store privacy labels declare audio, fitness and sensitive-info data
- **Field:** raw_streams
- **Found:** The iOS privacy label for the LifeData+ app lists "Audio Data", "Health Fitness" and "Sensitive Info" (not linked to identity). The RealLife Exp label lists Health & Fitness, precise location and photos or videos but no audio. Google Play for LifeData+ lists Health info and Fitness info as optional, for analytics. The console's question types (from the same public bundle) are AmountOfTime, DateTime, FreeText, ImageView, MultipleChoice, NumberEntry, PersonalIdentifier, PhotoEntry, RangeSlider, RatingScale, VideoResponse and WebPage. There is no audio type, and video responses are capped at 120 seconds. Most likely the audio label covers the sound in video responses and the health labels cover survey answers, not a sensor or HealthKit stream. That is inference.
- **URLs:** https://apps.apple.com/us/app/lifedata/id6443996884 ; https://play.google.com/store/apps/datasafety?id=com.lifedata.lifedata&hl=en_US ; https://app.lifedatacorp.com/assets/index-HDLErs9z.js
- **Quotes:** "Audio Data" ; "Health Fitness" ; "Sensitive Info" (App Store) ; "Health info · Optional Analytics" (Play) ; "Maximum video length is 120 seconds" (bundle)
- **Date:** checked 2026-10-11
- **Source type:** app_store; vendor_docs
- **KB:** no (unclear against profile line 82, which marks audio/microphone "No"). Video response questions and the PersonalIdentifier question type are not in the profile either.

### 8. Researchers add Google Maps Timeline to get continuous location
- **Field:** raw_streams
- **Found:** Two University of Pennsylvania tobacco-retail studies (JMIR Res Protoc 2026, PMC13353911; JAMA Netw Open 2025, PMC12481226) ran EMA in RealLife Exp and collected geolocation separately through Google Maps, with participants uploading their Timeline files. This is outside evidence for the profile's finding that LifeData captures location only with a response.
- **URLs:** https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13353911/fullTextXML ; https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12481226/fullTextXML
- **Quotes:** "EMA data were collected via LifeData" ; "geolocation data were collected through Google Maps" ; "refusal to install Google Maps or LifeData apps on their mobile phone" ; "geolocation tracking data were collected through Google Maps (Google), while participants completed a series of ecological momentary assessment questions each day through the RealLife Exp application (LifeData, LLC)"
- **Date:** papers 2025 and 2026; checked 2026-10-11
- **Source type:** paper
- **KB:** no (consistent with profile line 65; the outside evidence is new).

### 9. Co-founder conflict of interest in a Merck-funded RCT that used LifeData
- **Field:** none directly (evidence and validation context; bears on academic_vs_commercial)
- **Found:** A double-blind suvorexant RCT (JAMA Netw Open 2026, doi 10.1001/jamanetworkopen.2025.50186, PMC12771224, funded by a Merck investigator-initiated grant) delivered its insomnia EMA four times a day through RealLife Exp. A LifeData co-founder is an author and disclosed equity. This is a regulated-drug RCT using the platform, relevant to the Clinical tier, and a vendor-affiliated paper in the evidence base.
- **URL:** https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12771224/fullTextXML
- **Quotes:** "Dr Steenbergh reported being a cofounder and equity holder of LifeData LLC" ; "via a commercial EMA software app (LifeData RealLife Exp)"
- **Date:** 2026 paper; checked 2026-10-11
- **Source type:** paper
- **KB:** no. Profile lines 188 to 208 list no vendor-affiliated papers. Module 3 candidate (pointer only).

### 10. Field teams confirm export fields with the vendor because docs are gated
- **Field:** export_routes, program_application
- **Found:** A National University of Singapore feasibility study (JMIR Form Res 2026, PMC13392534, n=130 older adults, 14 days, RealLife Exp) pretested the data export and resolved questions about exported fields with the vendor before enrolment. Participants joined with a one-time passcode and created no account. This is outside evidence for the profile's gated-documentation finding, plus a non-US deployment (data exported to institutional storage).
- **URL:** https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13392534/fullTextXML
- **Quotes:** "Any uncertainties regarding app functions or exported data fields were clarified with the app provider before participant enrollment" ; "No account registration or user profile creation was required"
- **Date:** 2026 paper; checked 2026-10-11
- **Source type:** paper
- **KB:** no. Supports profile lines 139 to 140. Module 3 candidate (pointer only).

### 11. Wearables run side by side, never integrated
- **Field:** raw_streams, export_routes
- **Found:** A pediatric depression study (JMIR 2025, PMC12175877) gave each participant a Fitbit synced through its own app while EMA ran in LifeData. A sleep-prediction study (Sensors 2025, PMC12252337) used RealLife Exp only for diary reminders alongside an Oura ring and Empatica E4s. Both are parallel-app designs with no LifeData integration.
- **URLs:** https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12175877/fullTextXML ; https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12252337/fullTextXML
- **Quotes:** "Each participant was given a FitBit, and the device was linked to the participant’s smartphone (for data syncing)" ; "We use the RealLife Exp mobile application to send two notifications in the morning and two notifications in the evening"
- **Date:** 2025 papers; checked 2026-10-11
- **Source type:** paper
- **KB:** no (consistent with profile line 223's "no wearable integration"; the deployment pattern is new). Module 3 candidates.

### 12. LifeData+ export is a queued data request per session type; Azure telemetry in the console
- **Field:** export_routes, data_residency
- **Found:** The LifeData+ console builds exports as data requests per session type, and names four session types: Startup, Check-in, Notification and Closeout. The profile knows only notification and check-in sessions. The console also ships Microsoft Azure Application Insights telemetry, which agrees with the Azure hosting in the privacy policy. It is still a UI-backend route, not a documented researcher API.
- **URLs:** https://app.lifedatacorp.com/assets/study-data-access-BhxiFjsS.js ; https://app.lifedatacorp.com/assets/vendor-telemetry-7cLEnaaS.js (build-specific filenames)
- **Quotes:** "Startup Session Data Request" ; "Notification Session Data Request" ; "Closeout Session Data Request" ; "ApplicationInsights"
- **Date:** checked 2026-10-11
- **Source type:** vendor_docs (product code, not documentation)
- **KB:** no. Profile lines 100 to 101 and 121 to 127 describe only notification and check-in sessions and CSV download.

### 13. Legal pages have not changed since 2024
- **Field:** retention_terms, ai_training_terms
- **Found:** The vendor's page sitemap gives lastmod 2024-12-12 for both the privacy policy and the terms of use. The DPF registry gives the policy's effective date as 2024-06-12 (finding 2). So the retention terms in the profile are current, and no AI or benchmarking clause has been added since.
- **URL:** https://www.lifedatacorp.com/page-sitemap.xml
- **Quote:** none probed (sitemap XML dates; the policy date quote is under finding 2)
- **Date:** checked 2026-10-11
- **Source type:** vendor_page
- **KB:** no (profile does not date the legal documents).

## Searched, nothing found

- **FDA:** openFDA 510(k), registration and listing, UDI and enforcement searches for "lifedata": no matches. No warning letters, CE or MDR status found.
- **Research or academic program:** none beyond the graduate-student discount already in the profile. No grant program, partnership program or "for organizations" page. The VA contracts (finding 4) are procurement, not a program.
- **Press, newsroom, funding:** no press releases, wire stories or funding news for LifeData LLC or LifeData+ (Inside Indiana Business hit was Lifeline Data Centers, unrelated).
- **Trust portal or certificates:** trust.lifedatacorp.com, status.lifedatacorp.com, docs.lifedatacorp.com do not resolve. No SOC 2, ISO 27001 or Part 11 evidence anywhere.
- **Help centres:** support.lifedatacorp.com and help.lifedatacorp.com (the LifeData+ help link) both return 403, and the Zendesk API returns "Couldn't authenticate you". Still gated.
- **API:** api.lifedatacorp.com still 404 at `/`.
- **GitHub and integrators:** no repositories. No LifeData integration found on Fitabase, Labfront, Terra or Thryve. One clinical-trial protocol (NCT04636177) runs LifeData alongside REDCap with no integration described.
- **Job postings:** none current (Indeed profile unclaimed, no listings).
- **Third-party HIPAA claims:** a ClinicalTrials.gov protocol (NCT03279952, Prot_SAP_000.pdf) reportedly says LifeData is HIPAA compliant and IRB-approved at several institutions. The PDF is a scan with no text layer, so the quote could not be verified, and it is left out.
- **GovTribe vendor page:** 403. USAspending was used instead.
- **SDSU EDC slides (2025):** the PDF URL served HTML to automated requests and could not be read.
- **Europe PMC "LifeData+":** no paper names the LifeData+ generation. Every 2025 to 2026 deployment found names RealLife Exp or "LifeData", which supports profile line 57 (no published LifeData+ deployments).
