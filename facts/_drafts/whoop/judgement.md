# WHOOP judgement (baseline fact run, 2026-10-10)

Inputs: `A.yaml`, `B.yaml`, `gaps.md`. Output: `facts/whoop.yaml` (38 entries over 30 fields).
Every quote in the final record was re-run through `tools/facts/quote_probe.py` and came back
`exact`. www.whoop.com, join, shop and support pages answer scripts with HTTP 403, so whoop.com
quotes use an Internet Archive capture as `fetch_url`; the live URL stays as `url`, the capture date
is in a source note, and any fact resting only on a capture or on a 2022 to 2023 WHOOP document is
capped at Reported with `recheck_by: 2026-10-24` for a browser check.

Final counts: 33 stated, 3 not_public, 2 unclear, 0 conflict. Confidence: 13 Verified,
3 Corroborated, 20 Reported, 2 Unclear.

## Where A and B disagreed, and how it was decided

| Field | A | B | Decision |
|---|---|---|---|
| research_program | stated, Reported, rests on the 2022 Unite deck | unclear, browser read of the research page, no quote | **stated, Reported.** Neither draft found a machine-checkable current source. I found one: the research page's contact link goes to WHOOP's Typeform titled "Research Request Intake" (live, quote exact). Combined with the privacy policy's "research partners" line (capture 2026-08-06), the Stanford npj Digital Medicine paper (data only "with permission of WHOOP, Inc.") and Digital WHOOP Labs (capture 2026-07-27), the value is now: no named self-serve program, research runs through WHOOP-approved partnerships. Unite kept as history. |
| program_eligibility | unclear, Unclear | unclear, Reported | **unclear, Unclear.** No source states criteria; B's browser read cannot be quoted. |
| program_application | stated (healthcare@whoop.com, 2023 FAQ) | unclear (Typeform, no quote) | **stated, Reported.** Intake form quoted live; healthcare@whoop.com kept as the 2023 route; added the 2026 *Clin Transl Sci* tutorial on institutional legal review (gap 10). |
| program_status | unclear, three 403 pages | unclear, 301 redirect plus 2023 layoffs article | **unclear, Unclear.** See the Unite decision below. Added the live intake form as the one thing that is current. |
| academic_vs_commercial | not_public, Corroborated | not_public, Reported | **not_public, Reported.** The developer side is Verified, but the research page that might draw a distinction is unreadable to scripts, so Corroborated overstates it. |
| device_price | stated, Reported (trackervs plus developer.whoop.com trial line) | unclear (browser read) | **stated, Reported.** Added a vendor quote from the 2026-10-02 membership capture ("Each membership includes a device, a charger, and a unique set of features"). |
| subscription_price | stated, Reported (trackervs) | unclear (browser read, Tom's Guide One price) | **stated, Reported.** US prices from two secondary sources agree with B's browser read; vendor quote added for Canadian prices from the capture (gap 14). US vendor prices still need a browser check. |
| academic_pricing | unclear | not_public | **not_public, Reported.** Nothing published. A quoted trackervs's "No permanent student ... discounts", which conflicts with B's browser read of a Student Beans footer link; consumer student pricing is not research pricing, so it is left out rather than recorded as a conflict. |
| api_platform_fees | two entries (developer API; Unite extra cost) | one entry, Unite in a note | **Two entries.** Developer API Verified. Research entry Reported, now carrying the 2023 FAQ and the 2026 tutorial's paid group-download web application (gap 10). |
| minimum_commitment | stated, Reported (trackervs 12-month) | unclear (terms of sale browser read) | **stated, Reported.** The trackervs quote is exact; no vendor page contradicts it; added the tutorial's possible minimum device order. Membership term still unconfirmed on a vendor page. |
| quote_required | unclear | two entries, both Verified | **Two entries.** Developer API "No", Verified. Research and partner entry downgraded to Reported: the Partner API quote proves exclusivity, not that pricing needs a quote, so "Yes in practice" is an inference. |
| raw_streams, sampling_rates | agree | agree | Merged; added the exact RR-interval quote and the 30-second epoch quote to the Unite-era entries. |
| history_depth | Corroborated | Verified | **Corroborated.** The quote shows no lower bound on start time; that a newly authorised member's full history comes back is inferred, not stated. Added the export article's "entire account history" line. |
| export_routes | API, BLE, Partner API | adds member CSV export (browser read) and Apple Health sync | **Three entries.** API Verified. Member CSV export Reported from the vendor article via its 2026-06-17 capture (gap 2). Research route Reported (2023 FAQ, 2026 tutorial). Apple Health sync dropped: neither draft had a source for it. |
| dpa | unclear, Unclear | unclear, Reported (SCC line from browser read) | **stated, Reported.** The gap hunter's capture of the August 2026 privacy policy makes the SCC line quotable: SCCs "with our customers upon request". No DPA template found. |
| soc2 | stated, Reported (2022 deck) | not_public | **stated, Reported, recheck 2026-10-24.** The 2022 deck does claim SOC 2 (quote exact), so not_public would hide a vendor claim; the value says plainly that it is the only claim and is dated. |
| iso27001 | not_public, Unclear | not_public, Reported | **not_public, Reported.** |

## The WHOOP Unite research route: current, discontinued or unclear?

**Unclear.** Evidence: `whoopunite.com` returns HTTP 301 to `https://www.whoop.com/` (curl,
2026-10-10); `www.whoop.com/us/en/unite/` is 403 and has no Internet Archive capture since 2025;
Athletech News reported 22 Unite layoffs on 2023-01-13; no closure announcement was found; the only
documents describing raw CSV files, RR intervals, 52 Hz sampling, blinded mode and membership
transfer are the 2022 deck and 2023 FAQ hosted by the University of Arizona. A live "Research
Request Intake" form and a 2026 tutorial reporting a paid group-download web app show WHOOP still
handles research customers somehow, but nothing current says raw files are on offer. So the Unite
raw route is recorded under a scope that says "current availability unclear", Reported, recheck
2026-10-24, and program_status is `unclear`. Discontinued would be an inference from a redirect.

## Gap-hunter findings

| # | Finding | Decision |
|---|---|---|
| 1 | Unite raw CSV, RR intervals, 52 Hz, blinded mode, membership transfer | **Accepted** (all six quotes exact), under Unite-scoped entries, Reported. Blinded mode in an export_routes note. |
| 2 | Member CSV export includes Journal entries | **Accepted.** All four quotes exact on the 2026-06-17 capture. Reported, recheck 2026-10-24 because the live article is 403. |
| 3 | step_count on cycles (changelog 2026-09-23) | **Accepted, Verified.** Live changelog dated 2026-09-23, quotes exact, read:cycles scope. One total per cycle, not a time series. |
| 4 | Tier-upgrade delays on the developer forum | **Accepted, Reported**, as a scoped developer_program_status entry. Quotes exact and dates confirmed through the forum's JSON. Qualified: in thread 15246 WHOOP staff escalated cases on 2026-07-04 to 07-08 and at least two posters then reported approval, one about 17 days after submitting. |
| 5 | Digital WHOOP Labs | **Accepted** as a source in research_program (internal only). "Unique participants in 2025" not used: the figure itself was not quoted. |
| 6 | Stanford npj Digital Medicine 2026 collaboration | **Accepted** in research_program. |
| 7 | Privacy policy "research partners" and LLM partner zero-training | **Accepted.** Research line in research_program; LLM line in the ai_training_terms note (consumer feature, not researcher terms). |
| 8 | Mubadala $75M and Health Research Initiative | **Accepted** as a secondary source in research_program. |
| 9 | Qatar lab and Qatar Foundation partnership | **Partly accepted.** Einpresswire quote exact; mentioned in the research_program note only. The Qatar Foundation capture was not re-probed (archive throttling), so it is not cited. |
| 10 | Paid group-download web app; institutional legal review, possible minimum device order | **Accepted, Reported** (paper), in program_application, api_platform_fees, minimum_commitment and export_routes. It is a general tutorial statement, not WHOOP's own terms. |
| 11 | HIPAA: not a covered entity, BAA unnecessary; privacy policy HIPAA notice; Advanced Labs authorization | **Accepted.** BAA quote kept; HIPAA notice quote added to hipaa_statement; Advanced Labs in a note only (consumer, not research). |
| 12 | GDPR representative, SCCs, US processing | **Accepted.** Quotes exact on the 2026-08-06 capture; used in gdpr_statement, dpa, data_residency. |
| 13 | IHRN sold outside the US, not available in the US | **Accepted, Reported**, as a scoped fda_clearances entry. Staff account confirmed via forum JSON (2025-05-09); capture footnote says IHRN "is not currently available in every region"; openFDA has no IHRN record. |
| 14 | Canadian vendor prices and 14+ day battery | **Accepted.** |
| 15 | All of Us forum request; export granularity | **Granularity accepted** as a member-report source on the self-export entry. **All of Us rejected**: a member's wish, not a fact about WHOOP. |

## Statements in the profile or matrix that the record contradicts

Profile: `module-01-wearables/profiles/whoop.md`. Matrix: `module-01-wearables/comparison-matrix.md`.

| File, line | It says | The record says |
|---|---|---|
| profile 20 | "A researcher who wants the underlying physiology cannot get it." | True of the public API. WHOOP supplied raw CSV files with RR intervals to Unite research partners (2023 FAQ); availability today is unclear (raw_streams, program_status). |
| profile 31 | "No published academic or research program was found." | Still no named program, but a live WHOOP "Research Request Intake" form exists and WHOOP states it works with research partners (research_program, program_application). |
| profile 32 | WHOOP Unite "is WHOOP's enterprise offering" (present tense) | whoopunite.com 301-redirects to whoop.com; Unite's current status is unclear (program_status). |
| profile 44, 62, 215 | No step time series in the API | Still true for time series, but cycles carry a step_count total since 2026-09-23 (derived_metrics). Profile line 75's cycle field list lacks step_count. |
| profile 90, 216, 247 | Journal "appears not to be exportable ... Treat as unavailable" | Not in the API (line 216 stays right), but WHOOP's June 2026 article says the member CSV export includes Journal entries (export_routes, Reported). |
| profile 96, 218 | No study tooling or group dashboard | A 2026 tutorial reports a paid WHOOP web application for viewing and downloading group data; the 2023 FAQ describes a participant-blinded mode (export_routes, Reported). |
| profile 99, 213 | Tier upgrades by manual review, planned into enrolment | Correct, but developers report waits of two to over three months in mid-2026 (developer_program_status, Reported). |
| profile 106, 248 | "Historical depth: not established." | No documented lower bound on API start time; member export can cover the entire account history (history_depth, Corroborated). |
| profile 107 | Participant self-export "not verified in this session" | CSV export by date range, emailed link, documented by WHOOP June 2026 (export_routes, Reported). |
| profile 125, 210, 232 | "No raw-data escape hatch of any kind"; "No raw data of any kind" | True of the API; a Unite research raw-file route existed in 2023, current status unclear. |
| profile 143, 252 | SOC 2, ISO, GDPR DPA, data residency "were not verified" | SOC 2 claimed only in a 2022 deck; ISO 27001 not public; SCCs offered to customers on request; data processed in the US, AWS West per 2023 FAQ (soc2, iso27001, dpa, data_residency, all Reported). |
| profile 236 | "Location, mobility, or step-based endpoints" as poor fit | Per-cycle step totals now exist; step time series still do not. |
| profile 194 to 196 | ECG and BPI only | Also Irregular Heart Rhythm Notifications, marketed on Life but not available in the US (fda_clearances, Reported). Not a contradiction of what is there. |
| matrix 160 | Historical backfill "Not established" | No lower bound on API start time (Corroborated). |
| matrix 180 | "None in the public platform; WHOOP Unite is enterprise, terms not public"; "**Journal not exportable**" | Journal is in the member CSV export; Unite status unclear; a paid group web app is reported. |
| matrix 200 | Battery "Not stated in the profile" | 14+ day battery for 5.0 and MG (vendor membership capture 2026-10-02). |
| matrix 99, 319 | "API v2, derived scores only"; "Derived scores only" | Correct for the API; a raw route existed through Unite (2023), current status unclear. |
| matrix 388 | "No published academic programme (R); WHOOP Unite is enterprise" | Research intake form live; Unite status unclear. |
| matrix 246 | GDPR / DPA "Unclear"; SOC 2 / ISO "Unclear" | GDPR notice, EU representative and SCCs on request (Reported); SOC 2 only a 2022 claim; ISO 27001 not public. |

Consistent with the record and not contradicted: subscription prices (profile 148, matrix 220), API
fee (profile 151), API terms clauses (profile 108 to 120), rate limits, member tiers, FDA status.

## For the coordinator to check by hand (in a browser)

1. www.whoop.com/us/en/membership/ in US dollars: confirm $199, $239 and $359 per year and whether a
   12-month term applies (subscription_price, minimum_commitment).
2. www.whoop.com/us/en/research/: what it offers and to whom (research_program, program_eligibility).
3. The June 2026 data-export article and the privacy policy: still live and unchanged? Both rest on
   Internet Archive captures.
4. Whether any WHOOP Unite or research raw-data offering exists today; only WHOOP can answer this
   (intake form or healthcare@whoop.com).
5. The Typeform's questions were not read; nothing was submitted.
