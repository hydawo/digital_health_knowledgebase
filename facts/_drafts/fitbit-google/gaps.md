# Gap hunt: fitbit-google (2026-10-10)

Gap hunter pass for Fitbit devices, the legacy Fitbit Web API and the Google Health API. Every quote
below was confirmed `exact` with `tools/facts/quote_probe.py` on 2026-10-10. KB paths are relative to
the repo root. "Profile" means `module-01-wearables/profiles/fitbit-google.md`; "matrix" means
`module-01-wearables/comparison-matrix.md`; "intermediaries" means
`module-01-wearables/profiles/data-intermediaries.md`.

## Contradictions and missing programs first

### 1. Unified-API intermediaries cannot share their Google Health API access (contradicts the KB's main route for new studies)

- **Field:** export_routes (also developer_program_status, academic_vs_commercial)
- **Found:** Thryve says Google Health does not allow an intermediary to run one set of credentials for
  many customers, as Fitbit did. Each customer needs its own Google Cloud project, OAuth client and
  verified app. Validic's transition guide says the same thing: the customer requests its own Google
  Health API developer credentials and passes them to Validic. That page renders in JavaScript, so
  quote_probe could not read it and nothing from it is quoted here. Taken together with Google's "not
  onboarding new projects", a study with no project of its own cannot reach Fitbit data through a
  unified API's cloud route. Fitabase is different: participants re-authorise Fitabase itself (finding
  9), so Fitabase seems to hold its own project. Whether Fitabase can add new customer studies under it
  is not stated.
- **URL:** https://www.thryve.health/blog/fitbit-shutdown-september-2026-migration-options
- **Quote:** "Google Health requires each partner to bring their own OAuth credentials, tied to their own Google Cloud project and their own verified app"
- **Date:** page undated; read 2026-10-10 (its release timeline runs to 15 August 2026)
- **Source type:** secondary
- **KB has it:** **contradicts.** Profile line 26 and intermediaries line 212 give "an intermediary that
  already holds access (Fitabase, or a unified API)" as a route. Intermediaries line 20 and matrix lines
  351 and 376 make the same point. The part about unified APIs looks wrong; the Fitabase part is
  probably fine.

### 2. There is an on-device route that skips Google Health API credentials, verification and CASA (missing)

- **Field:** export_routes
- **Found:** The Google Health app writes data into Apple Health (iOS) and Health Connect (Android). An
  SDK or study app that reads HealthKit or Health Connect can then collect Fitbit and Pixel Watch data
  without a Google Health API project. That gets around Google's onboarding freeze. Google Health
  version 5.05 for iPhone added the write-to-Apple-Health sync in early August 2026. Thryve warns that
  the sync is new and that Google's community forums show open bugs. Records arrive tagged with the
  on-device store as their source, not Google Health.
- **URL 1:** https://www.thryve.health/blog/fitbit-shutdown-september-2026-migration-options
- **Quote 1:** "there is now a route on both platforms that avoids Google Health credentials, OAuth verification, and CASA entirely"
- **Quote 1b:** "Google shipped the Apple Health sync recently, and the public Google Health communities show a number of open bugs"
- **URL 2:** https://www.wareable.com/fitbit/google-health-update-fitbit-data-sync-with-apple-health
- **Quote 2:** "The version 5.05 update enables iPhone users to sync workouts, step counts, sleep metrics, and vitals from their connected Fitbit fitness tracker or Pixel Watch directly into Apple’s HealthKit framework"
- **Date:** Wareable and TechRepublic coverage dated 4 August 2026; Thryve read 2026-10-10
- **Source type:** secondary (no Google help page found for the Apple Health sync)
- **KB has it:** **no.** Profile line 213 names Health Connect as a separate path but does not offer it
  as a way around the freeze, and the KB has no Apple Health route for Fitbit. Profile line 26 lists the
  routes as an intermediary, self-export or All of Us. This matters for phone-based platforms in
  Module 2 that read HealthKit or Health Connect.

### 3. Fitbit-to-Google-Account migration: login cutoff on 19 May 2026, deletions from 15 July 2026, Workspace accounts not allowed (missing)

- **Field:** deprecations (also retention_terms, program_eligibility in a study-operations sense)
- **Found:** Fitbit accounts that were not moved to a Google Account lost app access after 19 May 2026.
  Google started deleting unmigrated accounts' data on 15 July 2026. This affects any study holding a
  pool of provisioned Fitbit-login accounts and any participant who did not migrate. Google Health also
  cannot be linked to a Google Workspace account. Institution-managed Workspace accounts therefore
  cannot serve as provisioned participant accounts, which the Research Pledge's advice on setting up
  participant Google accounts (profile line 72) does not mention. A Google Account is also required to
  activate new Fitbit and Pixel devices.
- **URL:** https://support.google.com/googlehealth/answer/14237024?hl=en
- **Quote 1:** "After May 19, 2026, you can no longer access Fitbit with your Fitbit account."
- **Quote 2:** "You can still download or delete your data any time before we begin processing data deletions on July 15, 2026."
- **Quote 3:** "You can't link your Google Health account to a Google Workspace account."
- **Quote 4:** "A Google Account is now required to sign up for the Google Health app and activate newly-released Fitbit and Pixel devices."
- **Date:** read 2026-10-10
- **Source type:** vendor_docs (Google Health help centre)
- **KB has it:** **no.** Profile line 39 gives 19 May 2026 only as the app rebrand date. The account
  cutoff, the 15 July deletions and the Workspace exclusion are not mentioned anywhere.

### 4. Google Health API launch date: release notes say 24 March 2026, the profile says late May (contradicts)

- **Field:** developer_program_status
- **Found:** The release notes date the launch announcement to 24 March 2026, the same day the research
  policy and pledge took effect. Validic says it has been in Google's beta programme since December 2025.
- **URL:** https://developers.google.com/health/release-notes
- **Quote:** "Google Health API Launch Announcement The Google Health API is the next generation of the Fitbit Web API"
- **Date:** the entry is headed "March 24, 2026"; read 2026-10-10
- **Source type:** vendor_docs
- **KB has it:** **contradicts.** Profile line 38 has "Opened late May 2026 (Corroborated)". May 26 is
  when the ECG and IRN scopes, rate limits and verification content were added, not the launch.

### 5. FDA clearances: five Fitbit-applicant records (missing)

- **Field:** fda_clearances
- **Found:** openFDA 510(k) records with Fitbit as applicant:
  - K200948, Fitbit ECG App, decided 2020-09-11, product code QDA
  - K212372, Fitbit Irregular Rhythm Notifications, 2022-04-08, QDB
  - K242967, Loss of Pulse Detection, 2025-02-25, SDY (a Pixel Watch 3 feature, according to Google's
    blog and the trade press)
  - DEN230050, Body Temperature Software (BTS), De Novo, 2023-12-15, QZA, and K243778, same name,
    2025-02-13. The records do not name the host device, so this needs checking. It may be the Pixel
    phone thermometer rather than a wearable.
  - K133872, Aria Wi-Fi Smart Scale, 2014-06-02, MNW (historical)
  - Nothing for blood pressure or hypertension. A Fitbit Labs hypertension study (Pixel Watch 3, up to
    10,000 US adults, 180 days) was reported in November 2025. It is a feasibility study, not a
    clearance.
- **URL:** https://api.fda.gov/device/510k.json?search=applicant:fitbit&limit=50
- **Quotes:** "Fitbit ECG App"; "Fitbit Irregular Rhythm Notifications"; "Loss of Pulse Detection"; "Body Temperature Software (BTS)"; "K242967"
- **Date:** queried 2026-10-10
- **Source type:** regulator_db
- **Note:** The accessdata.fda.gov pmn.cfm?ID= pages returned 404 to quote_probe, so the openFDA API was
  used instead. CE marks for the ECG app (2020) and IRN (2022) were seen in press coverage only and were
  not probed. FDA warning letters were not searched.
- **KB has it:** **no.** Matrix line 243 (Fitbit compliance row) says the regulatory column is "Not
  itemised in the profile", and the profile has no FDA section.

### 6. Google Health Enterprise lists "Researcher" as a customer type (missing program lead)

- **Field:** research_program (also quote_required)
- **Found:** Fitbit Health Solutions is now "Google Health Enterprise" at healthapp.google, built around
  Google Health Coach and Fitbit Air. The sales contact form's organisation-type list includes
  "Researcher". No research tier, pricing or data-access terms are published. This is a sales route to
  ask about, not evidence of a research program. The old 2015 Fitbit enterprise BAA offer was found only
  in press from 2015 and 2016, and the current enterprise pages do not mention HIPAA or a BAA.
- **URL 1:** https://healthapp.google/enterprise-contact
- **Quote 1:** "Health Plan Clinical Care Partner Wellness Partner Health System Employer Broker/Consultant Researcher"
- **URL 2:** https://healthapp.google/enterprise-solutions/
- **Quote 2:** "Google Health Enterprise helps organizations improve population health"
- **Date:** read 2026-10-10
- **Source type:** vendor_page
- **KB has it:** **no.** Profile line 188 says Google and Fitbit "provide no first-party research
  console". The enterprise offer is not mentioned.

### 7. Fitbit Health Equity Research Initiative (2021, historical program, missing)

- **Field:** research_program, program_status
- **Found:** Fitbit and Fitabase ran a 2021 initiative offering Fitbit products and services, announced
  as up to $500,000 in value. Six researchers received awards in October 2021. No later round was found,
  so treat the program as historical or closed (Unclear).
- **URL:** https://fitabase.com/blog/post/announcing-the-awardees-of-the-fitbit-health-equity-research-initiative/
- **Quote:** "This past April, Fitbit and Fitabase announced the launch of the Fitbit Health Equity Research Initiative."
- **Date:** post dated 13 October 2021
- **Source type:** secondary (partner blog)
- **KB has it:** no

## Other findings

### 8. Google pushed the turn-off to 30 October because of CASA delays (KB has the date, not the reason)

- **Field:** deprecations
- **Found:** Google originally gave 30 September 2026 as the decommission date and later separated it
  into "support ends 30 Sep" and "turned off 30 Oct". Trade press reports that Google said the extra
  month was for developers held up by the CASA assessment. That points to CASA being a real queue.
- **URL:** https://gadgetsandwearables.com/2026/09/28/fitbit-api-migration-deadline-october-30/
- **Quote:** "The company says the extra time is intended to help developers dealing with delays around the required Cloud Application Security Assessment"
- **Date:** article 2026-09-28, update dated 30/9/2026
- **Source type:** secondary
- **KB has it:** partly. Profile line 28 records the date change but not the reason.

### 9. Fitabase's migration: participants re-authorise by 31 October, brown-outs, new export columns

- **Field:** export_routes, deprecations
- **Found:** Fitabase asks studies to have participants re-authorised by 31 October 2026, one day after
  Google's 30 October turn-off. It warns of syncing delays during Google Health "brown-outs" and says
  exports gain UTC, time-zone and source columns, which will break scripts that expect fixed columns.
- **URL:** https://www.fitabase.com/blog/post/webinar-fitbit-api-transition-for-researchers/
- **Quote 1:** "Having every participant reconnected by October 31, 2026 so data sync isn't delayed at the Fitbit API shutoff"
- **Quote 2:** "Syncing delays during Google Health brown-outs as the transition is made to the new API"
- **Quote 3:** "New UTC and time-zone columns, plus a source column showing whether data came from the Fitbit or Google Health API"
- **Date:** post dated 10 September 2026
- **Source type:** secondary (integrator)
- **KB has it:** partly. Profile line 208 has the reauthorisation caveat from Fitabase's earlier post.
  The brown-outs, the export schema change and the 31 October date (which conflicts with Google's 30
  October) are missing.

### 10. Google's own newsletter says intraday data is available for all relevant data types

- **Field:** sampling_rates
- **Found:** The August 2026 developer newsletter says the Google Health API offers intraday data for
  every relevant data type and adds gRPC alongside REST. This is a vendor claim, not a documented
  sampling contract, but it weakens the profile's "leaning negative" reading of intraday access.
- **URL:** https://developers.google.com/health/newsletters
- **Quote 1:** "availability of intraday data for all relevant data types"
- **Quote 2:** "adding gRPC alongside REST"
- **Date:** August 2026 issue; page last updated 2026-09-29
- **Source type:** vendor_docs
- **KB has it:** partly, and the tone conflicts. Profile lines 87 to 100 call intraday "Unclear,
  leaning negative" (with the 2026-10-10 update at line 89 partly superseding that). Open question at
  line 293. gRPC is not mentioned.

### 11. Pixel Watch step counts returned by the web API were wrong for 95 days in 2026

- **Field:** derived_metrics (data quality)
- **Found:** Google's status dashboard lists a 2026 Web API incident, starting 20 March 2026 and lasting
  95 days, in which steps calculated by Pixel Watches could come back wrong from the web APIs. Studies
  with Pixel Watch step data from roughly late March to late June 2026 should check it. The dashboard
  also lists a 20-day 2024 incident of "data discrepancies or syncing issues between 3P apps and
  Fitbit".
- **URL:** https://status.healthapp.google.com/products/nQL9J5JmKTULiJ42QUqc/history
- **Quote 1:** "Some users querying web APIs for steps calculated by Pixel Watches may see incorrect values."
- **Quote 2:** "20 Mar 2026 95 days, 4 hours"
- **Date:** read 2026-10-10
- **Source type:** vendor_docs (status dashboard)
- **KB has it:** no. The status dashboard (added 22 June 2026 per the release notes) is not linked
  either.

### 12. No published history lookback limit for the Google Health API

- **Field:** history_depth
- **Found:** Thryve says Google has not published a limit on how far back the Google Health API returns
  data, so backfill after a re-consent gap is limited and uncertain.
- **URL:** https://www.thryve.health/blog/fitbit-shutdown-september-2026-migration-options
- **Quote:** "Google has not yet published a definitive historical lookback limit for the Google Health API"
- **Date:** read 2026-10-10
- **Source type:** secondary
- **KB has it:** yes, consistent. Profile line 294 and matrix line 157 record backfill depth as open or
  Unclear. This adds a third-party confirmation that it is unpublished.

### 13. CASA renews every year, costs about EUR 1,000 or more in one integrator's experience, and has an accelerator for ISO 27001 or SOC 2 holders

- **Field:** api_platform_fees
- **Found:** CASA renews every year. Thryve puts the typical start at around EUR 1,000 and says
  applicants holding ISO/IEC 27001 or SOC 2 may qualify for a reduced-scope "CASA Accelerator". The KB
  has Google's $500 to $4,500 figure but not the accelerator, which a university IT security office
  with ISO 27001 might qualify for.
- **URL:** https://www.thryve.health/blog/fitbit-shutdown-september-2026-migration-options
- **Quote 1:** "It runs through one of Google's authorised assessors, renews annually, and typically starts around €1,000 and upwards"
- **Quote 2:** "If you hold ISO/IEC 27001 or SOC 2, you may qualify for the CASA Accelerator reduced scope and faster turnaround."
- **Date:** read 2026-10-10
- **Source type:** secondary
- **KB has it:** partly. Profile lines 57 to 60 have the fee range and annual reassessment (Corroborated).
  The accelerator is missing.

### 14. Google Health API v4beta channel (1 October 2026) and 7-day webhook retry

- **Field:** deprecations / export_routes
- **Found:** A v4beta preview channel was added on 1 October 2026, and features tagged v4beta may change
  before they reach v4. Failed webhook notifications are retried for up to 7 days, which sets the window
  a subscriber can be down without losing notifications.
- **URL:** https://developers.google.com/health/release-notes
- **Quote 1:** "Added v4beta channel to serve as a public preview for broad partner testing and market validation prior to promotion to the stable v4 channel."
- **Quote 2:** "Automatically retries failed webhook notifications for up to 7 days if communication with the subscriber is lost."
- **Date:** entries dated 1 October 2026 and 26 May 2026
- **Source type:** vendor_docs
- **KB has it:** no. Profile line 166 has only v4 resources.

### 15. Google Fit sunset is now on Google's own pages (KB has it as Corroborated)

- **Field:** deprecations
- **Found:** Google's own pages say the Fit APIs will be "deprecated in 2026", are supported until the
  end of 2026, and have taken no new sign-ups since 1 May 2024.
- **URL 1:** https://developers.google.com/fit
- **Quote 1:** "The Google Fit APIs, including the Google Fit REST API, will be deprecated in 2026"
- **Quote 1b:** "As of May 1, 2024, developers cannot sign up to use these APIs"
- **URL 2:** https://developer.android.com/health-and-fitness/health-connect/migration/fit
- **Quote 2:** "The Google Fit APIs will be supported until the end of 2026."
- **Date:** read 2026-10-10
- **Source type:** vendor_docs
- **KB has it:** yes. Profile line 44 has it as Corroborated; it can now be Verified. The no-sign-ups
  date is missing.

### 16. Legacy Fitbit Web API closed to new app registrations

- **Field:** developer_program_status
- **Found:** An integrator states that no new legacy Fitbit Web API credentials can be obtained.
- **URL:** https://openwearables.io/blog/fitbit-web-api-shutdown-2026-migration-guide
- **Quote:** "New developer registrations are closed. If you do not already have Fitbit API credentials, you cannot get them."
- **Date:** read 2026-10-10
- **Source type:** secondary
- **KB has it:** no, but it makes no practical difference with the API turning off on 30 October.

### 17. Legacy device policy: updates for at least two years after last sale, then pairing ends

- **Field:** deprecations (devices)
- **Found:** Fitbit devices get software updates for at least two years after Google last sells them,
  after which updates, support and the ability to pair with the app end. This matters for studies that
  reuse older stock (for example Charge 4 or Versa 2). Trade press also reports that Google has ended new
  Versa and Sense generations, with Versa 4 and Sense 2 still on sale; that was not probed.
- **URL:** https://support.google.com/product-documentation/answer/15187883?hl=en
- **Quote 1:** "Our devices typically receive software updates for at least two years after the device is last sold on Fitbit.com or the Google Store"
- **Quote 2:** "Eventually we must discontinue software updates, support and ability for our devices to pair with the Fitbit app."
- **Date:** read 2026-10-10
- **Source type:** vendor_legal
- **KB has it:** no

### 18. Google's consumer privacy page: users can opt in to share data for Google R&D and health research

- **Field:** ai_training_terms (Google's own use of the data, not developer terms)
- **Found:** Google Health users can consent to their de-identified data being used for Google's
  research and development of new products or for health research. Neither the Google Health API
  Developer Terms nor the Developer and User Data Policy (last updated 2026-03-24) contains any
  AI-training, machine-learning or benchmarking clause; searches for "train", "machine learning",
  "artificial intelligence" and "benchmark" found nothing. The developer policy does require honouring
  deletion requests.
- **URL 1:** https://healthapp.google/privacy
- **Quote 1:** "With your consent, you can also share data to be used for the research and development of new products and services or to support health research."
- **URL 2:** https://developers.google.com/health/policies/health-api-developer-user-data-policy
- **Quote 2:** "Honor user requests to delete their data."
- **Date:** read 2026-10-10
- **Source type:** vendor_page; vendor_legal
- **KB has it:** no. Matrix line 385 says "AI-training terms not covered in the profile". The Developer
  and User Data Policy is not cited anywhere in the profile.

## Searched, nothing found

- A published date for reopening Google Health API onboarding, or a waitlist or form (Google pages,
  newsletter, release notes, developer forums in web search).
- A Google or Fitbit academic or research-specific access tier, data grant or programme active in 2026,
  beyond the Health Research Policy, Pledge and Attestation already in the KB.
- A current Fitbit or Google Health BAA offer. Only 2015 and 2016 press on the old Fitbit enterprise
  BAA turned up, and the current enterprise pages do not mention HIPAA.
- FDA 510(k) or De Novo records with Google LLC as applicant (openFDA returned none). No blood pressure
  clearance. FDA warning letters were not searched.
- An All of Us notice on whether participants must re-link Fitbit for the Google Health API. The KB
  says the All of Us dataset has no exposure to the shutoff (intermediaries line 192). That holds for
  data already collected, but ongoing Fitbit sync into All of Us probably depends on the new API.
  Unverified.
- Peer-reviewed papers or preprints describing data collection through the Google Health API: none
  found.
- An official Google GitHub organisation for Google Health API samples (the release notes mention REST
  libraries on GitHub, but no repo was located). The Google Fit samples repo is archived.
- AI-training and benchmarking clauses in the Google Health API developer terms and data policy: none
  (see 18).
- Data residency for the Google Health API: nothing found outside Google's docs.
- ISO 27001 or SOC 2 evidence specific to Fitbit or Google Health: not searched in certificate
  registries. Google Cloud's general certifications were not treated as covering Fitbit.
- Not searched: job postings, conference talks, Labfront and Terra pages (Labfront does not support
  Fitbit per the KB), and app-store listings (the Google Health Studies Play listing returned 404 to
  quote_probe).
