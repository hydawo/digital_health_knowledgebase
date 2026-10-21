# Fitabase: gap hunt (baseline fact run)

Gap hunter run, 2026-10-11. Every quote below was checked with `tools/facts/quote_probe.py` on
2026-10-11 and returned "exact". "Date" is the source's own date where it shows one; all pages were
read 2026-10-11. KB = knowledge base. Paths are relative to the repo root.

## Contradictions

### G1. Garmin beat-to-beat route: Fitabase also offers a Garmin SDK route, not only the API route
- Field: raw_streams (also export_routes, sampling_rates)
- Found: Fitabase says raw Garmin beat-to-beat intervals can be pulled through the Garmin SDK, with
  participants syncing through the Fitabase Engage app instead of Garmin Connect. A KB article
  "Setting up Fitabase Engage for the Garmin SDK" (last updated April 15, 2026) exists. The KB
  describes Fitabase's Garmin route as API/OAuth only and sleep-time Enhanced BBI only, and frames
  the SDK route as Labfront's differentiator.
- URL: https://www.fitabase.com/blog/post/garmin-cirqa-screenless-device-for-research/
- Quotes: "Fitabase can help you pull them using the Garmin SDK" ; "You'll have participants
  download the Fitabase Engage app and sync through it instead of the Garmin Connect app"
- Supporting URL: https://www.fitabase.com/resources/knowledge-base/fitabase-engage/setting-up-fitabase-engage-for-the-garmin-sdk/
  (troubleshooting article; no streams or rates listed)
- Date: 2026-07-29 (blog post)
- Source type: vendor_page
- KB has it: **contradicts.** module-01-wearables/comparison-matrix.md:102 and :374 ("Fitabase's
  API route captures it during sleep"; daytime BBI listed as not via Fitabase);
  module-01-wearables/profiles/garmin.md:59 and :102 ("Fitabase (Garmin API route, Enhanced BBI
  during sleep"); shared/unresolved-questions.md:97 (Q74 answered as API vs SDK split). The KB's
  description of the API route may still be right; what is missing is that Fitabase now has an SDK
  route too. Whether that SDK route is daytime, its rate, and which customers can use it are not stated.

### G2. Study count: customers page says 2500+ studies and 900+ institutions; KB cites 1,100
- Field: research_program (track record context; not a schema field of its own)
- Found: The customers page headline gives 900+ institutions and 2500+ studies. The homepage
  still says "over 1,100 research studies" (re-checked 2026-10-11). Vendor pages disagree with each
  other; the KB cites only the homepage figure.
- URL: https://www.fitabase.com/how-it-works/customers/
- Quote: "900+ Institutions, 2500+ Studies"
- Date: undated page, read 2026-10-11
- Source type: vendor_page
- KB has it: **contradicts / incomplete.** module-01-wearables/profiles/data-intermediaries.md:38
  and :96; module-01-wearables/profiles/fitbit-google.md:18 cite "over 1,100" only.

### G3. Engage is launched, not only "coming"
- Field: program_status (product status; also research_program)
- Found: Fitabase "re-launched" Engage on 21 April 2026 at the Society of Behavioral Medicine
  conference, described as a flow designer with branching logic, triggers, variables and
  randomization, plus an AI assistant that turns plain-language study descriptions into flows. A KB
  section with three Engage app setup articles is live. The Engage Wrist App page still says
  "Preview · Summer 2026" and names the starting Garmin models.
- URLs: https://www.fitabase.com/blog/post/relaunch-of-fitabase-engage/ ;
  https://www.fitabase.com/engage/wrist/
- Quotes: "design participant interactions using branching logic, conditional triggers, variables,
  and randomization" ; "helps translate plain-language study descriptions into structured
  interaction flows" ; "Starting models include the Garmin Vivoactive 5, Vivoactive 6, Venu 3, and Venu 4"
- Date: 2026-04-21 (blog); wrist page undated
- Source type: vendor_page
- KB has it: **partly contradicts.** data-intermediaries.md:37 ("Coming") and :94 ("Engage suite,
  Summer 2026") present Engage as future; the April relaunch, the AI flow assistant and the Garmin
  model list are absent.

## Missing programs and access routes

### G4. Google demo (de-identified) accounts route for Fitbit studies
- Field: program_application (also academic_vs_commercial)
- Found: Google provides de-identified "demo" Google accounts for research, applied for through a
  research application with IRB approval or waiver, about 5 to 7 business days to approve; accounts
  expire after six months and are extended by Fitbit support in six-month increments. Fitabase has
  a KB article on using them.
- URL: https://www.fitabase.com/blog/post/google-rolls-out-deidentified-accounts-for-fitbit-research/
- Quotes: "Demo accounts are de-identified Google profiles designed for research" ; "Demo accounts
  expire after six months"
- Date: 2025-03-12 (blog). Current availability under the Google Health API not restated; the
  migration FAQ does cover reauthorizing demo accounts, implying they continue.
- Source type: vendor_page (secondhand on a Google program)
- KB has it: **no.** No mention of demo or de-identified Google accounts in data-intermediaries.md
  or fitbit-google.md.

### G5. Custom projects are capacity-limited
- Field: minimum_commitment / quote_required
- Found: Pricing page lists "Custom Solutions" with a yearly cap on custom projects.
- URL: https://www.fitabase.com/how-it-works/pricing/
- Quote: "We accept a limited number of custom projects each year"
- Date: undated, read 2026-10-11
- Source type: vendor_page
- KB has it: **no.** data-intermediaries.md:39 lists the add-ons but not this.

## Deprecations and migration (last 12 months)

### G6. Fitabase migration specifics: reauthorization window runs to 30 November 2026, with backfill
- Field: deprecations
- Found: Fitabase key-dates page: reauthorization opens mid-to-late October 2026 (date TBD); end of
  October is the target; the reconnect banner and Fitabase links keep working through 30 November
  2026. Late reauthorization backfills the gap provided the participant kept syncing to the Google
  Health app. Reauthorization cannot be done programmatically.
- URLs: https://www.fitabase.com/resources/knowledge-base/google-health-api-migration/key-dates/ ;
  https://www.fitabase.com/resources/knowledge-base/google-health-api-migration/if-participants-dont-reauthorize/ ;
  https://www.fitabase.com/resources/knowledge-base/google-health-api-migration/migration-faq/
- Quotes: "The reconnect banner stays in the Google Health app, giving participants who missed the
  deadline a way back" ; "Fitabase automatically goes back and fills in the data from the time they
  were disconnected" ; "Each account has to go through Google's sign-in and permission screens"
- Date: pages last updated September 2026 (overview and export pages say September 23, 2026)
- Source type: vendor_docs
- KB has it: **partly.** fitbit-google.md:49 and :216 have the 31 October target, brown-outs and new
  export columns; the 30 November grace, backfill behaviour and no-programmatic-reauth are missing.

### G7. Migration drops "classic sleep" dataset and step-goal writing; Fitabase API unchanged
- Field: deprecations (also derived_metrics)
- Found: Classic sleep will no longer be a separate dataset; writing step goals to the app is not
  available in the Google Health API yet (studies with dynamic step goals affected). The Fitabase
  API itself is not changing.
- URL: https://www.fitabase.com/resources/knowledge-base/google-health-api-migration/migration-faq/
- Quotes: "There will no longer be classic sleep data split out as its own dataset" ; "isn't
  available in the Google Health API yet" ; "If you pull data through the Fitabase API, your
  integration keeps working as-is"
- Date: September 2026, read 2026-10-11
- Source type: vendor_docs
- KB has it: **no.**

### G8. Export source column
- Field: export_routes
- Found: Exports add UTC, time-zone and a source column naming the API each row came from.
- URL: https://www.fitabase.com/resources/knowledge-base/google-health-api-migration/export-changes/
- Quote: "A new source column shows which API each row came from"
- Date: last updated September 23, 2026
- Source type: vendor_docs
- KB has it: **yes.** fitbit-google.md:216 and :366.

## New capabilities (last 12 months)

### G9. Webhooks
- Field: export_routes
- Found: Fitabase webhooks POST to a customer HTTPS endpoint when a participant's connection status
  changes. Plan and price not stated.
- URL: https://www.fitabase.com/blog/post/webhooks/
- Quotes: "Fitabase will automatically send a POST request to an HTTPS endpoint you specify" ;
  "whenever a participant's connection status changes"
- Date: 2026-03-11
- Source type: vendor_page
- KB has it: **no.** data-intermediaries.md:36 lists only the Aggregate Data API.

### G10. Garmin Index blood pressure monitor data
- Field: raw_streams
- Found: Fitabase pulls readings from the Garmin Index BPM (systolic, diastolic, pulse, source:
  device or manual entry), in individual and batch CSV exports.
- URL: https://www.fitabase.com/blog/post/garmin-index-blood-pressure-monitor/
- Quote: "Our platform can now pull readings from the Garmin Index Blood Pressure Monitor"
- Date: 2026-01-20
- Source type: vendor_page
- KB has it: **no** for Fitabase (Labfront's Index BPM support is listed at data-intermediaries.md:59).

### G11. Fitbit Air and Garmin CIRQA support; second-device interference caveat
- Field: raw_streams
- Found: Fitabase blog posts cover both screenless trackers. For Fitbit Air, a second Fitbit device
  paired to the same Google Health account interferes with collection.
- URL: https://www.fitabase.com/blog/post/fitbit-air-screenless-tracker-for-research/
- Quote: "A second Fitbit device paired to the participant's Google Health account would interfere
  with data collection"
- Date: 2026-07-30 (Air), 2026-07-29 (CIRQA)
- Source type: vendor_page
- KB has it: **no** for Fitabase specifically.

## Data resolution and history

### G12. Second-level heart rate, not just minute-level
- Field: sampling_rates
- Found: Fitbit heart rate via Fitabase at variable 3 to 15 second sampling; sleep stages at 30 s;
  HRV at 5-minute readings; timestamped ECG logs, skin and core temperature, wear time.
- URL: https://www.fitabase.com/resources/knowledge-base/learn-about-fitbit-data/data-resolutions/
- Quote: "variable sampling with readings every 3-15 seconds"
- Date: undated, read 2026-10-11
- Source type: vendor_docs
- KB has it: **incomplete.** data-intermediaries.md:33 says "Daily, hourly, minute-level" only.

### G13. Historical Garmin data requires participant opt-in
- Field: history_depth
- Found: Historical capture works by setting sync dates in the past, but Garmin Connect's
  historical-data toggle is off by default; no maximum lookback stated.
- URL: https://www.fitabase.com/resources/knowledge-base/getting-started/capturing-historical-garmin-data/
- Quote: "turned off by default on Garmin Connect"
- Date: undated, read 2026-10-11
- Source type: vendor_docs
- KB has it: **no.**

## Compliance and hosting

### G14. Hosting on Microsoft Azure; backups encrypted; disaster-recovery snapshots
- Field: data_residency (also retention_terms)
- Found: Fitabase code and databases on Microsoft Azure; ISO 27001 cited only for Microsoft's data
  centres (dated "ISO/IEC 27001:2005", old text), not for Fitabase. Snapshot archives kept for
  disaster recovery; no retention or deletion period stated. Region not stated.
- URLs: https://www.fitabase.com/resources/knowledge-base/working-with-the-irb/data-security-privacy/ ;
  https://www.fitabase.com/resources/knowledge-base/working-with-the-irb/answers-to-common-questions-irb-data-security/
- Quotes: "Fitabase code and databases physically reside on the Microsoft Azure platform" ; "Small
  Steps Labs LLC maintains snapshot archives of database for disaster recovery purposes" ; "Our
  data is housed in secure Azure (Microsoft) servers"
- Date: undated, read 2026-10-11
- Source type: vendor_docs
- KB has it: **no.** data-intermediaries.md:40 checked FAQ, privacy and terms only; these IRB KB
  pages were not cited. They also contain no HIPAA, BAA, PHI or SOC 2 wording (consistent with
  KB Q16 still open).

### G15. No GPS collected, by design
- Field: raw_streams
- Found: Fitabase does not support GPS data because it is potentially identifiable.
- URL: https://www.fitabase.com/resources/knowledge-base/working-with-the-irb/answers-to-common-questions-irb-data-security/
- Quote: "we currently do not support any GPS data as that is potentially identifiable as well"
- Date: undated, read 2026-10-11
- Source type: vendor_docs
- KB has it: **no.**

## Company context

### G16. Small team, growing R&D; no open positions
- Field: none directly (operational context for program_status)
- Found: December 2025 post says R&D spending increased and the dev team grew by one; careers page
  shows "No Current Positions Open" (2026-10-11). A third-party profile (RocketReach) estimates
  about 5 employees; not quoted, unreliable.
- URL: https://www.fitabase.com/blog/post/reflections-on-14-years-in-business-and-an-exciting-2026/
- Quote: "growing the dev team with a new member"
- Date: 2025-12-18
- Source type: vendor_page
- KB has it: **no** (low priority).

## Searched, nothing found
- HIPAA BAA, SOC 2, ISO 27001 (Fitabase itself), trust portal: web search, FAQ, IRB KB pages,
  data-security page. Nothing beyond Azure hosting. Third-party evidence: one ClinicalTrials.gov
  consent form describes de-identified flow through Fitabase; no BAA mentioned.
- Pricing figures: pricing page, web search for per-participant or licence fees in papers and
  budgets, third-party aggregator (getpulsesignal.com, no figures). medRxiv cost-analysis PDF
  (10.1101/2023.12.20.23300342) returned 403; not checked.
- New-study capacity under Fitabase's own Google Health API project: migration overview, FAQ,
  key dates and export pages do not address it. Still Unclear.
- FDA clearances: not applicable (data platform, not a device); no regulatory events found.
- App store listing for the Fitabase Engage app: not found by search.
- Data retention period, AI training terms, API rate limits: not found on KB, FAQ or security pages.
- Garmin partnership status: only 2018 press (Garmin, MobiHealthNews, Wareable); no 2026 update.
- Health Equity Research Initiative with Google/Fitbit: last post January 2023; no 2024 to 2026
  round found (treated as inactive, not confirmed).
- Integrations beyond Fitbit and Garmin (Dexcom 2019, BodyTrace 2017 blog posts): current pages
  and device-comparison page list only Fitbit and Garmin devices; current status of those older
  integrations not stated.
- Job postings: none.
