# Judgement: apple (2026-10-10)

Inputs: `A.yaml`, `B.yaml`, `gaps.md`. Output: `facts/apple.yaml`, with 72 facts (68 stated, 2 not_public,
1 conflict, 1 not_applicable). Confidence: 61 Verified, 8 Corroborated, 1 Reported, 1 Unclear. I re-probed all
148 quotes in the final record and every one came back `exact 1.0`. `validate.py` gives 0 errors and 0
unresearched. `weekly.py --only apple --no-state` gives 0 missing and 0 reworded. Its 4 "pages changed" are
fingerprint differences against the earlier starter watch state, not quote problems.

Before merging I probed every quote in both drafts. All 81 in A and all 101 in B were exact, so none of the
disagreements below came down to a bad quote. They were about scope, framing or completeness.

## Where A and B disagreed

| Field | A | B | Decision |
|---|---|---|---|
| raw_streams, HealthKit ECG | Stated in one merged entry, with a note that the FAQ and the docs differ | `conflict`, Unclear | **Conflict, kept on purpose.** Both are Apple pages. The FAQ says "No. You cannot access raw ECG data through HealthKit." The HKElectrocardiogram and HKElectrocardiogramQuery docs (I read them through the JSON rendering) describe per-lead voltage measurements at a stated sampling frequency for each ECG saved by Apple Watch. Neither page defines "raw", so the record can't settle it. The note spells out what is undisputed: researchers get the voltage waveform of on-demand ECG-app recordings, and no continuous ECG exists. What's disputed is whether that waveform counts as unprocessed sensor output. A's note argued that the FAQ "appears to mean" the sensor signal, which is an inference and can't be stated as fact. |
| raw_streams, overall structure | One entry mixing SensorKit and HealthKit, including "no raw PPG or accelerometer" via HealthKit (not quoted) | Separate entries for SensorKit, HealthKit ECG, heartbeat series and CMSensorRecorder | B's split, plus a fifth entry for the Core Motion 800 Hz batched sensors from A and the gap hunter. A's unquoted "no raw accelerometer" claim was dropped because CMSensorRecorder contradicts it in spirit: 50 Hz raw accelerometer is available without an entitlement. |
| sampling_rates | 800 Hz/200 Hz Core Motion, "SensorKit heart rate: 1 Hz", FAQ, ECG frequency | 50 Hz CMSensorRecorder, FAQ, ECG frequency | Merged into three scoped entries (Core Motion, HealthKit, Series 12). **A mislabelled `CMHighFrequencyHeartRateData` as SensorKit.** It is a Core Motion class (watchOS 10+, iOS 17+). I corrected the label. |
| history_depth | One merged entry (30-day limit, Watch purge, SensorKit 7 days and 24 h) | Scoped entries for HealthKit (earliestPermittedSampleDate), SensorKit and CMSensorRecorder (3 days) | Scoped entries, combining both sources for HealthKit plus the FAQ iOS 27 quote. |
| ai_training_terms | `unclear`, with one source that had no quote | `stated`, Verified | **Stated, Corroborated.** The quoted terms are real and current: health, motion and fitness use only, research only with permission, and disclosure plus explicit permission for third-party AI. "No term names training" is an absence finding, so I lowered the confidence to Corroborated rather than Verified. |
| soc2 | `not_public` | One `stated` (SOC 3 for Private Cloud Compute) plus one `not_public` | **One `not_public`.** A SOC 3 report is not a SOC 2, and Private Cloud Compute is not a health service. The PCC SOC 3 is in the note, and its page is listed among the pages checked. |
| baa | Cites the developer licence agreement's business-associate clause | Cites the iCloud terms' PHI clause | Both sources kept, Corroborated (capped). |
| fda_clearances | One entry per record (8 entries) | One combined entry, with K212516 and the non-Watch records in a note | A's per-record layout. Added K212516 from B, plus K242058/K250143 (Digital Prism Correction) and K253582 (Medical Imaging Calibration) after I checked openFDA myself: applicant "Apple, Inc." returns 12 records. All use accessdata.fda.gov as `url` and openFDA as `fetch_url`, Verified. |
| program_status | One unscoped entry | Three scoped entries | B's scoped layout, using A's extra quotes (Vision Pro and AirPods Pro, and "standard criteria"). |
| academic_pricing | Single entry | Two entries (fee waiver; no device discount, Corroborated) | Merged into one entry, Verified. Every element is quoted, and the "no device discount" part goes in the note. |
| fee-waiver URL | `developer.apple.com/support/membership-fee-waiver/` | `developer.apple.com/help/account/membership/fee-waivers/` | Both pages carry the quote. I used B's help-centre URL. |
| derived_metrics | data-types page | hkquantitytypeidentifier page plus sleep stages | B's sources, plus two quotes from the HealthKit updates page on new types (medications, menopause). |
| subscription_price | Scoped to nothing, "no subscription needed" in the value | Scoped to Fitness+ | A's framing. "No subscription needed" is the decision-relevant fact. Its basis is an absence finding, which the note explains. |
| device_price SE 3 | Price only | Price plus "no ECG app or hypertension notifications" | The price only. B's extra claim had no quote, so it is in a note. |

On everything else (program_eligibility, program_application, user_cap, developer_program_status,
api_platform_fees, minimum_commitment, quote_required, export_routes, retention_terms for HealthKit, dpa,
hipaa_statement, gdpr_statement, iso27001, data_residency, deprecations for iOS 27), A and B agreed. I merged
them, keeping the better-sourced entry and the union of quotes.

## Gap-hunter findings

| # | Finding | Decision |
|---|---|---|
| 1 | Investigator Support Program | **Accepted.** I confirmed all seven quotes on the ISP page and the FAQ, plus the Clin Transl Sci 2026 corroboration on PMC (exact). The program is active: three cycles a year, devices in kind, no funding, agreement and ethics approval before devices ship, quarterly reports. |
| 2 | Study App Template | **Accepted** as its own research_program entry, plus export_routes and api_platform_fees. |
| 3 | iOS 27 30-day limit and HealthKit Research Entitlement | **Accepted.** I confirmed the entitlement page ("If granted, this entitlement will do two things..."; "requires iOS 27.1 or later") and the FAQ ("Starting in iOS 27, HealthKit gives participants more control... past 30 days"; "does not gate access to HealthKit data types"). It appears in research_program, program_eligibility, program_application, program_status, history_depth and deprecations. The developer forum thread 842499 was not used (JavaScript only). |
| 4 | CMSensorRecorder background accelerometer | **Accepted.** The JSON docs say the system records 50 Hz "even if your app is suspended or terminated", for up to 43,200 s per call, readable for up to three days. The class lists iOS 9.0 and watchOS 2.0 with no deprecation flag. No research entitlement is needed, only the motion usage permission. |
| 5 | Series 12 5-second HR and 5-minute HRV | **Accepted**, scoped to Series 12 as a device-side figure, with a note that the HealthKit cadence is undocumented. |
| 6 | SensorKit public-sharing restriction (Funk et al. 2025, PLOS One) | **Accepted, as Reported.** The data availability sentence is exact on journals.plos.org. It is the paper's report of Apple's terms, and Apple's own page confirms only that additional non-public terms exist. Recorded as a separate SensorKit retention_terms entry. |
| 7 | 12 FDA records and the AFib History MDDT | **Accepted.** I checked openFDA directly and found 12 records, all now in the record. The MDDT quote is exact on fda.gov/media/178230. I recorded it as regulator_db, but it's a qualification, not a clearance. The "May 2024" date was not re-checked. |
| 8 | Blood Oxygen US redesign | **Accepted** in deprecations (Apple newsroom quote exact). The ITC termination is a secondary source and sits only in the note. |
| 9 | SensorKit 24 h hold and 7-day lookback | **Accepted.** Both drafts already had it. |
| 10 | Two-stage SensorKit entitlement | **Accepted** in program_application. |
| 11 | Background Health Research Task entitlement | **Accepted** in research_program and program_eligibility. The "iOS 17.0 vs 17.1" discrepancy the gap hunter mentioned was not checked. The record uses Apple's own "17.1". |
| 12 | Developer Program fee waiver | **Accepted.** |
| 13 | App Review 5.1.3 ethics approval; third-party AI rule | **Accepted** (program_eligibility, ai_training_terms). |
| 14 | 800 Hz/200 Hz Core Motion, workout session required | **Accepted.** The WWDC23 transcript quote is exact. |
| 15 | Movement Disorder API | **Accepted** in derived_metrics. |
| 16 | HealthKit clinical records (FHIR) | **Accepted** in export_routes. |
| 17 | New HealthKit data types | **Accepted in part.** I used the medications and menopause quotes in derived_metrics. Mental well-being and time in daylight are not quoted. |
| 18 | Apple feature validation summaries | **Rejected for this record.** They are validation evidence and fit no schema field. They belong in `literature-library.md`. |
| 19 | Apple Heart and Movement Study ended | **Accepted** in program_status, Corroborated. The source is the Brigham and Women's study site (secondary), backed by Apple's Research app page. |
| 20 | Health+ wound down | **Rejected as a fact.** It is a secondary report of a product that never shipped. It is mentioned in the subscription_price note. |
| 21 | ISO 27001/27018 covers iCloud | **Accepted.** It matches both drafts. Stays Corroborated because the Coalfire certificate was not retrieved. |
| 22 | SensorKit 94% sharing at 2 months | **Rejected for this record.** It is acceptability evidence, not a vendor term. It belongs in the profile or in Module 3. |
| 23 | ResearchKit 3.4.x pre-releases | **Rejected.** There's no quote (the figures come from the GitHub API), and it is activity, not a deprecation. |

## Profile and matrix statements the record contradicts

`module-01-wearables/profiles/apple-watch-healthkit.md`:

| Line | Says | Record says |
|---|---|---|
| 13, 165 | "no research programme fee"; pricing is device purchase plus Developer Program fee | Mostly consistent, but it misses the Investigator Support Program's free devices and the fee waiver for nonprofits, educational institutions and government (academic_pricing). |
| 22, 187 | "no vendor retention policy" / "no data-processing agreement with Apple for the study copy" | True for HealthKit. **Not for SensorKit**: there are additional non-public use and handling terms, and Funk et al. 2025 report that they bar public data sharing (retention_terms, SensorKit). |
| 48, 69 | Accelerometer "Not via HealthKit. In-app on watchOS via Core Motion while the app runs"; `CMSensorRecorder` called "historical" | CMSensorRecorder is current (not deprecated) and records 50 Hz accelerometer while the app is suspended or terminated, for up to 12 h per call, kept for 3 days. There is also 800 Hz in workouts (raw_streams, sampling_rates). |
| 49 | Gyroscope "Core Motion in-app only" | The 200 Hz device motion during workouts is a batched route. "In-app only" undersells it. |
| 52, 72, 223 | US SpO2 "disrupted", listed as an open question | Since August 2025 the US redesign computes Blood Oxygen on the paired iPhone (deprecations). |
| 89, 226 | Background HR "roughly every few minutes at rest"; cadence unpublished | Apple says Series 12 takes background HR every 5 s and HRV as often as every 5 min, device-side (sampling_rates, Series 12). Whether HealthKit receives that cadence is undocumented. |
| 99, 194, 215 | "None provided by Apple to third parties" for study tooling; "no study-management tooling"; poor fit for teams without engineers | Apple offers the Study App Template free to approved ISP applicants, needing "minimal to no coding" (research_program, export_routes). |
| 118 | Background execution limits, with no mitigation mentioned | The Background Health Research Task entitlement exists for exactly this (research_program). |
| 137 | "SensorKit is Apple's only research-specific data programme open to outside academics" | The Investigator Support Program, the HealthKit Research Entitlement and the Background Health Research Task entitlement are also research-specific programs open to outside teams (research_program). |
| 138 | HealthKit gives "full on-device history the participant authorises" | From iOS 27 participants can limit an app to the past 30 days unless it holds the HealthKit Research Entitlement (history_depth, deprecations). |
| 141 | Lists SensorKit and ResearchKit activity only | Missing the ISP, the HealthKit Research Entitlement (new, iOS 27.1) and the end of Heart and Movement Study data collection (program_status). |
| 177 (and matrix 242) | Only K250507 itemised | 12 FDA records plus the AFib History MDDT qualification (fda_clearances). |
| 196, 214 | "Core Motion gives in-app motion data but not a retrospective raw archive"; raw continuous accelerometry needs SensorKit approval | CMSensorRecorder is a retrospective 50 Hz archive (3 days) with no entitlement. It isn't continuous beyond the 12 h per call, but calls can be repeated. |
| 47, 68, 222 | ECG voltage access "resolved 2026-10-09 in favour of access", marked Verified | Access to the voltages is Verified, but Apple's research FAQ says "You cannot access raw ECG data through HealthKit". The record keeps this as a conflict about whether the waveform is "raw". The profile should name the FAQ statement rather than present the question as closed. |

`module-01-wearables/comparison-matrix.md`:

| Line | Says | Record says |
|---|---|---|
| 95 | Accelerometer "SensorKit only ... Core Motion in-app; not via HealthKit" | CMSensorRecorder gives background 50 Hz with no entitlement, and there is 800 Hz in workouts. |
| 155 | History "Full on-device history the participant authorises" | Participants can cap it at 30 days from iOS 27, unless the app holds the Research Entitlement. |
| 216 | Research pricing "**None**" | ISP devices in kind and the Developer Program fee waiver. |
| 242 | FDA "other features not itemised" | 12 records plus the MDDT. |
| 289 (and `README.md` 182) | "Apple Series 11" as current hardware | Series 12, Ultra 4 and SE 3 are on sale (device_price). |
| 315 | "full on-device history at enrolment" | The 30-day option from iOS 27. |
| 384 | "SensorKit (Apple's only research-specific programme)"; "No Apple cloud copy or Apple retention term"; research pricing via the Developer Program fee only | ISP, the HealthKit Research Entitlement and BGHealthResearchTask also exist. SensorKit carries non-public use and handling terms. Fee waiver and free ISP devices. |

Matrix line 371 lists "Apple HealthKit" as safe for retention, deposit or ML training. That is consistent for
HealthKit, but the line should not be read as covering SensorKit.

## For the coordinator to check by hand

- **The HealthKit ECG conflict.** It needs an answer from Apple to resolve. One sentence to Apple (via the
  researchandcare.org FAQ contact or sensorkitrequest@apple.com) asking whether HKElectrocardiogram voltages
  are filtered would settle it.
- **The MDDT qualification date (May 2024)** and whether the DPCF and MICF records belong to Vision Pro. I didn't
  check either.
- **Whether iPhone-computed Blood Oxygen samples** reach HealthKit the same way as before. Not checked.
- **The BGHealthResearchTask minimum iOS version.** Apple's resource page says 17.1. A third-party summary said
  the class page lists 17.0. Not checked.
- **The Series 12 HR/HRV cadence** is a marketing claim. Whether it reaches HealthKit, and whether HRV is still
  SDNN, is undocumented.
