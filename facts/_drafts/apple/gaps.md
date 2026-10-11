# Gap hunt: apple (2026-10-10)

Scope: Apple Watch, HealthKit, SensorKit, ResearchKit and CareKit, the Apple Research app. Compared
against `module-01-wearables/profiles/apple-watch-healthkit.md` (profile), `module-01-wearables/comparison-matrix.md`
(matrix) and `facts/apple.yaml` (all fields `unresearched`, so "KB has it" below refers to the profile
and matrix). Every quote below returned `exact 1.0` from `tools/facts/quote_probe.py` on 2026-10-10.

## A. Contradictions and missing programs

### 1. Investigator Support Program: Apple gives free devices to researchers (missing program, contradicts)
- Fields: `research_program`, `program_eligibility`, `program_application`, `academic_pricing`, `academic_vs_commercial`
- Found: Apple runs an Investigator Support Program that awards Apple devices (most often Apple Watch; Apple Vision Pro and AirPods Pro also) and app development resources. Three review cycles a year (due 5 Jan, 5 Apr, 5 Sep), decision typically 6 to 8 weeks after the due date. No funding. Institution signs an Investigator Support Program Agreement and shows ethics approval before devices ship. Quarterly status reports and notice of planned publications required. Apply to research_proposals@apple.com.
- URL: https://www.researchandcare.org/investigator-support-program/
- Quotes:
  - "The program provides researchers with the opportunities to receive Apple devices to use in their research studies, as well as access to app development resources to enhance their projects."
  - "Apple reviews applications in three cycles per year with due dates on January 5, April 5, and September 5."
  - "The review committee typically makes a determination 6-8 weeks after the due date in each cycle."
  - "The Investigator Support Program does not provide study sponsorship or funding."
  - "your institution will need to complete a standard Investigator Support Program Agreement and provide proof of study ethics board approval before devices can be awarded"
  - "investigators will provide quarterly status reports on the research and share details of any planned publications"
  - "Complete the Investigator Support Program application form and submit it to research_proposals@apple.com"
- Second source, devices: https://www.researchandcare.org/faq/ : "The Investigator Support Program most commonly focuses on Apple Watch devices. Apple Vision Pro and AirPods Pro can now be requested through this program where available." and "While there is no specific limit, Apple has a limited number of devices available for the program."
- Independent corroboration: https://pmc.ncbi.nlm.nih.gov/articles/PMC13438180/ (Clin Transl Sci 2026, DOI 10.1111/cts.70693): "Apple has multiple partnerships with the research community, including an Investigator Support Program that provides free devices."
- Date: page current 2026-10-10 (copyright 2026). Source type: vendor_page (paper: paper).
- KB: **contradicts.** Profile line 137 says "SensorKit is Apple's only research-specific data programme open to outside academics"; matrix line 384 says "Apple's only research-specific programme" and "User caps: None from Apple"; matrix line 216 and profile line 165 give no research pricing route. The program is listed only as a watch URL in `facts/apple.yaml` and as a "Search summary" row S-APL-05 in `module-01-wearables/sources.md` line 21; the profile never mentions it.

### 2. Study App Template: Apple's no-code study app for researchers (missing program, contradicts)
- Fields: `research_program`, `export_routes`, `academic_pricing`
- Found: Apple offers, free to approved applicants through the Investigator Support Program application, a "Study App Template" with consent, surveys, ResearchKit active tasks, HealthKit and SensorKit collection, encrypted export to the researcher's servers, notifications and localisation.
- URL: https://www.researchandcare.org/resources/study-app-template/
- Quotes:
  - "Available at no cost for approved applicants so you can focus on what truly matters: the science."
  - "When data is exported to your servers, it's secured with built in encryption."
  - From https://www.researchandcare.org/investigator-support-program/ : "Using Study App Template, minimal to no coding experience is required to build a study data collection app."
- Date: current 2026-10-10. Source type: vendor_page.
- KB: **contradicts.** Profile line 99 says study tooling is "None provided by Apple to third parties. ... Every one of these must be built or bought"; lines 23, 194 and 215 present custom app engineering as the only route for teams without developers. `sources.md` line 19 notes "Study App Template" in passing; the profile and matrix do not.

### 3. iOS 27: participants can cap HealthKit read access at 30 days; new HealthKit Research Entitlement (contradicts history depth)
- Fields: `history_depth`, `program_application`, `deprecations`
- Found: from iOS 27 the HealthKit permission sheet lets a participant limit an app to the past 30 days and adds periodic access reminders. A new HealthKit Research Entitlement (iOS 27.1+, per bundle ID, IRB or IEC approval, app exclusively for one research study) removes the 30-day option from new permission requests and reduces reminders. It does not gate data types. Granting it needs an app update and redistribution.
- URL: https://www.researchandcare.org/resources/healthkit-research-entitlement/
- Quotes:
  - "If granted, this entitlement will do two things: 1) New HealthKit permission requests will not include the option to limit historical data to 30 days and 2) the entitlement will reduce the number of reminders study participants receive."
  - "HealthKitResearch requires iOS 27.1 or later."
  - "Your app must be designed for one unique study."
  - "an app update and redistribution will be required once the entitlement is granted"
  - From https://www.researchandcare.org/faq/ : "Starting in iOS 27, HealthKit gives participants more control over data sharing, including limiting an app's read access to the past 30 days and periodic reminders to review or revoke access." and "No this entitlement does not gate access to HealthKit data types."
- Date: current 2026-10-10. Source type: vendor_page. (A developer forum thread, https://developer.apple.com/forums/thread/842499, discusses the same change; JavaScript-rendered, not quote-checked.)
- KB: **contradicts.** Profile line 138 ("full on-device history the participant authorises"), matrix line 155 ("Full on-device history the participant authorises"), matrix line 315 ("full on-device history at enrolment") and matrix line 384 ("full authorised history") are all wrong for iOS 27 participants unless the study holds the new entitlement.

### 4. CMSensorRecorder records 50 Hz accelerometer in the background for up to 12 h, kept 3 days (contradicts)
- Fields: `raw_streams`, `sampling_rates`, `history_depth`
- Found: Apple's current Core Motion documentation (not deprecated; iOS 9+, watchOS 2+) says `recordAccelerometer(forDuration:)` captures 50 Hz accelerometer data even while the app is suspended or terminated, for up to 43,200 s per call, readable for up to three days.
- URL: https://developer.apple.com/documentation/coremotion/cmsensorrecorder/recordaccelerometer(forduration:).md
- Quotes:
  - "When you call this method, the system begins capturing accelerometer data at a sample rate of 50 Hz. The system records the data for the specified amount of time, even if your app is suspended or terminated. The collected data remains accessible to your app for up to three days."
  - "You may specify a time interval of up to 43,200 seconds (12 hours)."
- Date: current docs, 2026-10-10. Source type: vendor_docs.
- KB: **contradicts.** Profile lines 48 and 69 say accelerometer is available "while the app runs" and call `CMSensorRecorder` "historical"; line 196 says Core Motion gives "not a retrospective raw archive comparable to ActiGraph/Ametris"; matrix line 95 says "Core Motion in-app". A no-entitlement, background, 50 Hz raw accelerometer route exists outside SensorKit.

### 5. Apple Watch Series 12: background HR every 5 s and HRV as often as every 5 min (contradicts sampling description; hardware missing)
- Fields: `sampling_rates`, `derived_metrics`, `device_price`
- Found: Series 12, Ultra 4 and SE 3 are the current line (launched September 2026). Apple says Series 12 takes background HR every five seconds (60x Series 11) and HRV as often as every five minutes; adds a readiness score and Health Age. Battery up to 24 h. Whether the new HR and HRV cadence reaches HealthKit, and whether HRV is still SDNN, is not stated on the page.
- URL: https://www.apple.com/apple-watch-series-12/
- Quotes:
  - "Apple Watch Series 12 measures HRV as often as every five minutes and takes background heart rate readings every five seconds"
  - "60x more frequent background heart rate readings than Series 11"
  - "Get up to 24 hours of normal use."
- Date: 2026-10-10. Source type: vendor_page.
- KB: **contradicts / no.** Profile line 89 says background HR is sampled "roughly every few minutes at rest" and line 88 that HRV is opportunistic; matrix line 289 and `README.md` line 182 name "Apple Series 11" as current hardware. No mention of Series 12, Ultra 4 or SE 3 anywhere in module 1.

### 6. SensorKit data cannot be shared publicly under Apple's terms (contradicts "no Apple retention term")
- Fields: `retention_terms`
- Found: the Intern Health Study's SensorKit paper states in its data availability section that Apple's restrictions block public sharing of SensorKit data. Apple's own SensorKit page says the entitlement carries "additional" terms for use and handling (terms not public).
- URL: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0329707 (Funk et al. 2025, PLOS One, DOI 10.1371/journal.pone.0329707)
- Quotes:
  - "SensorKit data cannot be shared publicly because of Apple's data sharing restrictions."
  - From https://www.researchandcare.org/resources/accessing-sensorkit-data/ : "Accessing SensorKit data requires additional entitlement agreement to certain terms and conditions for use and handling."
- Date: paper 2025; page current 2026-10-10. Source type: paper; vendor_page.
- KB: **contradicts.** Profile line 22 ("no vendor retention policy"), line 138 and matrix line 384 ("No Apple cloud copy or Apple retention term") treat SensorKit like HealthKit. Matrix line 371 lists Apple among safe choices for data deposit; true for HealthKit, not shown to be true for SensorKit. The paper is in `sources.md` line 226 (S-VAL-06) but the restriction is not recorded.

### 7. Apple FDA clearances: 12 Apple, Inc. records, profile itemises one; AFib History is an FDA-qualified MDDT (missing)
- Fields: `fda_clearances`
- Found (openFDA 510(k) API, applicant "Apple Inc", 2026-10-10): DEN180044 ECG App and DEN180042 Irregular Rhythm Notification (2018-09-11); K201525 ECG App (2020-10-08); K212516 IRNF App (2021-10-22); K213971 Atrial Fibrillation History Feature (2022-06-03); K231173 IRNF (2023-07-21); DEN230081 Hearing Aid Feature (2024-09-12); K240929 Sleep Apnea Notification Feature (2024-09-13); K242058 and K250143 Digital Prism Correction Feature (2024-10-21, 2025-06-23); K250507 Hypertension Notification Feature (2025-09-11); K253582 Medical Imaging Calibration Feature (2026-04-01).
- URL: https://api.fda.gov/device/510k.json?search=applicant:%22Apple+Inc%22&limit=50
- Quotes: "Sleep Apnea Notification Feature (SANF)"; "Hearing Aid Feature (HAF)"; "Atrial Fibrillation History Feature"
- MDDT: FDA qualified the AFib History Feature as a Medical Device Development Tool (the first digital health technology so qualified, May 2024) for use as a secondary endpoint in cardiac ablation device trials.
  - URL: https://www.fda.gov/media/178230/download
  - Quote: "The Apple AFib History Feature can be used as a biomarker test to help evaluate estimates of AFib burden as a secondary effectiveness endpoint within clinical studies intended to evaluate the safety and effectiveness of cardiac ablation devices"
- Date: queried 2026-10-10. Source type: regulator_db.
- KB: **no.** Matrix line 242 says "other features not itemised in the profile"; profile line 177 covers only K250507. No mention of the MDDT qualification anywhere in the KB. The FDA accessdata pages returned 404 to the probe; openFDA and the FDA media PDF worked.

## B. Changes and items the KB lacks

### 8. Blood oxygen: US redesign (computed on iPhone) cleared; ITC case closed April 2026 (resolves an open question)
- Fields: `deprecations`, `raw_streams`
- Found: since 14 Aug 2025, US Series 9, Series 10 and Ultra 2 units without Blood Oxygen get a redesigned feature whose calculation runs on the paired iPhone. On 17 Apr 2026 the ITC declined review and terminated the proceeding, finding the redesign does not infringe. Separately, a November 2025 jury award to Masimo (reported $634M) is under appeal (secondary, not quote-checked).
- URLs and quotes:
  - https://www.apple.com/newsroom/2025/08/an-update-on-blood-oxygen-for-apple-watch-in-the-us/ : "Following this update, sensor data from the Blood Oxygen app on Apple Watch will be measured and calculated on the paired iPhone, and results can be viewed in the Respiratory section of the Health app." (vendor_page, 2025-08-14)
  - https://9to5mac.com/2026/04/17/apple-wins-latest-round-in-masimo-fight-as-itc-closes-apple-watch-import-ban-case/ : "This combined proceeding is hereby terminated in its entirety with the conclusion that the accused redesigned products do not infringe the Asserted Patents" (secondary quoting the ITC order, 2026-04-17)
- KB: **no.** Profile line 223 still lists US SpO2 availability as an open question; lines 52 and 72 say "US availability disrupted". Whether iPhone-computed SpO2 samples still land in HealthKit identically was not checked.

### 9. SensorKit: 24-hour holding period and 7-day lookback (missing access constraint)
- Fields: `history_depth`, `rate_limits`
- Found: newly recorded SensorKit data are withheld for 24 hours; an app can read only 7 days of prior data for an active sensor, and only data recorded after it called `startRecording()`.
- URLs and quotes:
  - https://developer.apple.com/documentation/sensorkit/srfetchrequest.md : "SensorKit places a 24-hour holding period on newly recorded data before an app can access it."
  - https://developer.apple.com/documentation/sensorkit/srsensorreader.md : "An app has access to 7 days of prior recorded data for an active sensor."
- Date: current docs 2026-10-10. Source type: vendor_docs.
- KB: **no.** Not in profile or matrix. A study app that fails to fetch for more than 7 days loses data permanently; that matters for upload design.

### 10. SensorKit entitlement is issued in two stages (development, then distribution after IRB)
- Fields: `program_application`
- URL: https://www.researchandcare.org/resources/accessing-sensorkit-data/
- Quote: "You’ll first be granted a development entitlement to use when developing your app. Once you have IRB (or comparable ethics board) approval of your study and are ready to launch, you’ll be provided the entitlement to distribute your app to study participants."
- Date: current 2026-10-10. Source type: vendor_page.
- KB: **partly.** Profile lines 125 to 129 list the steps but not the two-stage entitlement. Note the same page's own SensorKit data-type list is still the short 2021-era list, which the profile already flags (line 122).

### 11. Background Health Research Task entitlement (BGHealthResearchTask)
- Fields: `research_program`, `program_eligibility`, `export_routes`
- Found: an entitlement letting research apps process and upload HealthKit, SensorKit or Bluetooth device data in the background. Per bundle ID; app must be exclusively for health research, have IRB or IEC approval, intend to publish, and show that observer queries and `BGProcessingTask` are insufficient. Requested through the Investigator Support Program application (FAQ).
- URL: https://www.researchandcare.org/resources/background-health-research-task-entitlement/
- Quotes:
  - "process data from HealthKit, SensorKit, and/or a Bluetooth device while the developer’s app is in the background"
  - "BGHealthResearchTask requires iOS 17.1 or later."
  - "You must intend to publish or otherwise make findings from the research study publicly available"
  - From https://www.researchandcare.org/faq/ : "Note that access to Background Health Research Task is provided through an entitlement. You can request entitlement through the Investigator Support Program application ."
- Date: current 2026-10-10. Source type: vendor_page. (Third-party summary says Apple's class page lists iOS 17.0; not checked.)
- KB: **no.** Profile line 118 and matrix line 155 cite background execution limits as a constraint without this mitigation.

### 12. Apple Developer Program fee waiver for nonprofits, accredited educational institutions and government
- Fields: `api_platform_fees`, `academic_pricing`
- Found: eligible organisations (legal entity, not individuals, no paid apps or in-app purchases) can have the 99 USD annual fee waived.
- URL: https://developer.apple.com/support/membership-fee-waiver/
- Quote: "If you’re a nonprofit organization, accredited educational institution, or government entity and meet certain requirements, you can request an Apple Developer Program fee waiver."
- Date: current 2026-10-10. Source type: vendor_docs.
- KB: **no.** Profile line 166 and matrix lines 216 and 384 list the Developer Program fee as a cost with no figure and no waiver.

### 13. App Review Guideline 5.1.3: consent content and ethics board approval are mandatory for research apps; third-party AI sharing needs explicit permission
- Fields: `program_eligibility`, `ai_training_terms`, `retention_terms`
- URL: https://developer.apple.com/app-store/review/guidelines/
- Quotes:
  - "Apps conducting health-related human subject research must secure approval from an independent ethics review board. Proof of such approval must be provided upon request."
  - "may not store personal health information in iCloud"
  - "for advertising, marketing, or other use-based data mining purposes other than improving health management, or for the purpose of health research, and then only with permission"
  - "You must clearly disclose where personal data will be shared with third parties, including with third-party AI, and obtain explicit permission before doing so."
- Also https://developer.apple.com/documentation/healthkit/protecting-user-privacy.md : "If the user consents, you may share their HealthKit data with a third party for medical research."
- Date: current 2026-10-10. Source type: vendor_legal.
- KB: **partly.** Profile line 159 says App Store review enforces health-data policies (no advertising, no selling) but not the ethics-board requirement, the iCloud storage ban, or the third-party AI rule. `ai_training_terms` has no KB content for Apple.

### 14. Core Motion high-rate batched sensors: 800 Hz accelerometer, 200 Hz device motion, during a HealthKit workout
- Fields: `raw_streams`, `sampling_rates`
- URLs and quotes:
  - https://developer.apple.com/documentation/updates/healthkit.md : "New Core Motion APIs provide 800 Hz accelerometer data and 200 Hz device motion data."
  - https://developer.apple.com/videos/play/wwdc2023/10179/ : "That's 800 Hz accelerometer and 200 Hz device motion, compared to 100 Hz with the existing CMMotionManager." and "Because this a workout-centric API, you need to have an active HealthKit workout session to get data."
- Date: June 2023 (WWDC23), docs current 2026-10-10. Source type: vendor_docs.
- KB: **no.** Profile line 48 gives only "Core Motion rates" without figures.

### 15. Movement Disorder API (tremor and dyskinesia), entitlement-gated
- Fields: `derived_metrics`, `program_application`
- URL: https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager.md
- Quotes: "Use `CMMovementDisorderManager` to measure a resting Parkinsonian tremor in the 3-7 Hz range and choreiform dyskinetic symptoms."; "requires an entitlement from Apple"; "Only collect data from patients clinically diagnosed with a movement disorder."
- Date: current docs. Source type: vendor_docs.
- KB: **no.** Not mentioned anywhere in modules 1 to 3.

### 16. HealthKit clinical records (FHIR)
- Fields: `export_routes`, `raw_streams`
- URL: https://developer.apple.com/documentation/healthkit/accessing-health-records.md
- Quote: "Use HealthKit’s clinical record support to read Fast Healthcare Interoperability Resources (FHIR) from the HealthKit store."
- Source type: vendor_docs. KB: **no** (profile has no FHIR or Health Records mention).

### 17. New HealthKit data types 2023 to 2026 (medications, menopause, mental well-being, time in daylight, workout zones)
- Fields: `derived_metrics`
- URL: https://developer.apple.com/documentation/updates/healthkit.md
- Quotes: "Query medications that a person has added to the Health app" (June 2025); "Record and query menopausal state information using point-in-time samples." (June 2026); "Read and write mental well-being samples" (June 2024); "Measure time spent outdoors and average light intensity with new data types." (June 2023)
- Source type: vendor_docs. KB: **no.** Profile line 84 lists older derived metrics only.

### 18. Apple's own feature validation summaries (sleep stages, sleep apnea, blood oxygen and more)
- Fields: `derived_metrics` (validation evidence)
- URL: https://www.researchandcare.org/feature-validation/
- Quotes: "Sleep Stages Validation Summary"; "Sleep Apnea Notifications Validation Summary"; "Blood Oxygen Validation Summary"
- Source type: vendor_page. KB: **partly.** `literature-library.md` lines 162 to 163 hold only the VO2max and hypertension white papers; the sleep stages, sleep apnea, SpO2, heart rate and calorimetry, six-minute walk, mobility and hearing summaries are not catalogued.

### 19. Apple Heart and Movement Study data collection ended; participants moved to the Apple Health Study, which does not need a Watch
- Fields: `program_status`
- URL: https://appleheartandmovementstudy.bwh.harvard.edu/?p=2152
- Quotes: "As data collection for the Apple Heart and Movement Study ends, we invite you to join the holistic Apple Health Study."; "does not require participants to have an Apple Watch"
- Source type: secondary (study site run by Brigham and Women's). KB: **partly.** Profile line 101 says the study "is no longer listed"; the end of collection and the no-Watch eligibility are not recorded.

### 20. Health+ subscription coach wound down (no subscription tier coming)
- Fields: `subscription_price`
- URL: https://www.pymnts.com/apple/2026/apple-scales-back-ai-health-coach-plans/
- Quotes: "Bloomberg reported on Feb. 5 that Apple has wound down the initiative, code-named Mulberry, citing people familiar with the matter."; "Apple referred to the effort internally as Health+."
- Source type: secondary (Reported). KB: **no**, consistent with profile line 13 ("no subscription required").

### 21. ISO/IEC 27001 and 27018 certifications cover iCloud (relevant only where participants sync Health data via iCloud)
- Fields: `iso27001`
- URL: https://support.apple.com/guide/certifications/apc34d2c0468b/web
- Quote: "Evidence of Apple’s ISO/IEC 27001 and 27018 certifications are publicly available. To view Apple’s certifications, go to the Certificate Directory on Coalfire’s website"
- Source type: vendor_page (certificate itself in Coalfire's directory not retrieved; search form). KB: **no.** Profile line 157 mentions iCloud encryption only. Apple is not in the study data path, so this is context, not a study control.

### 22. SensorKit acceptability evidence: 94% still sharing at 2 months (Intern Health Study, via MyDataHelps)
- Fields: `academic_vs_commercial` (how researchers actually got the data)
- URL: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0329707
- Quote: "At 2 months, 94.0% (653/695) of participants were still providing SensorKit data."
- Source type: paper. KB: **partly** (`sources.md` line 226 lists the paper; profile line 131 says participants "may decline" without figures). The paper also shows the SensorKit opt-in order is fixed by Apple and cannot be randomised.

### 23. ResearchKit 3.4.x pre-releases in 2026
- Fields: `deprecations` (activity)
- Found (GitHub API, 2026-10-10): 3.4.0 (2026-07-15) and 3.4.2 (2026-09-23) are tagged pre-release; latest stable is still 3.2.0-stable (2025-09-19). CareKit 4.1.0 released 2026-04-03.
- URL: https://github.com/ResearchKit/ResearchKit/releases/tag/3.4.2
- Source type: repository. Quote: not taken (GitHub page text is navigation chrome; figures from the API).
- KB: **yes, consistent** (profile line 141 gives 3.2.0 as latest), pre-releases unrecorded.

## C. Searched, nothing found or not usable
- SensorKit entitlement approval rates or typical turnaround: nothing published (open question at profile line 225 stays open).
- SensorKit PPG and ECG capture rate or schedule: no new documentation.
- Apple BAA or DPA for HealthKit or SensorKit: none exists or is offered; nothing found.
- SOC 2 report for Apple health services: none found.
- CE or MDR status for hypertension notifications: no CE or EUDAMED record found; only press saying EU availability at launch.
- Fitabase, Labfront: no Apple Watch or HealthKit integration found. Terra, Thryve, Sahha: not re-checked here (their own profiles cover them).
- FDA warning letters or recalls naming Apple, Inc. health features: none found in the search.
- Apple Watch Series 12 price, and whether Series 12 per-5-second HR and 5-minute HRV write to HealthKit: price page is JavaScript-rendered; HealthKit cadence not documented.
- FDA accessdata 510(k) pages (K240929, K250507) and the 510(k) PDF path: 404 to the probe; used openFDA instead.
- Apple developer forum thread 810406 (SensorKit hold reset behaviour) and 842499 (iOS 27 30-day option): JavaScript-rendered, not quote-checked.
