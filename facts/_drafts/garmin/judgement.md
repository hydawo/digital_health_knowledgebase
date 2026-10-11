# Garmin: judgement (baseline run, 2026-10-10)

Inputs: `A.yaml`, `B.yaml`, `gaps.md`. Output: `facts/garmin.yaml` (42 entries across 30 fields). Every quote in the
final record was re-run through `tools/facts/quote_probe.py` on 2026-10-10 and returned `exact`. Both agreement PDFs
were downloaded and read in full text by the judge, and their PDF metadata and server dates were checked.

## The two developer agreements

Two versions of FRM-0952 Rev. B are live:

| | Garmin International version | Garmin China Shanghai RHQ version |
|---|---|---|
| URL | developerportal.garmin.com/sites/default/files/Garmin%20Connect%20Developer%20Program%20Agreement.pdf | www8.garmin.com/en-US/GARMINCONNECTDEVELOPERPROGRAMAGREEMENT/GARMINCONNECTDEVELOPERPROGRAMAGREEMENT_EN.pdf |
| PDF created / server last-modified | 2023-10-04 / 2025-01-07 | 2026-03-03 / 2026-03-06 |
| Pages | 14 | 19 |
| Governing law | New York | People's Republic of China (Shanghai courts for PRC licensees, New York ICDR arbitration for others) |
| Transfer annex | EU SCCs module one, Garmin Wurzburg as EEA/UK/CH exporter, retention period stated | PIPL standard contract for data leaving the PRC |
| 6.4(a) research exemption from attribution | No | Yes |
| 15.10 AI transparency and consent | No ("artificial intelligence" and "machine learning" absent) | Yes |
| 10.1 no licence fees; future fees on 30 days' notice; over-limit fees | Yes | Yes, identical |
| 8.4 no public statements without approval | Yes | Yes |

No source says which version binds a licensee outside China. A web search found nothing either. The China version
plans for non-PRC licensees in its dispute clause, so it does not limit itself to China by its own text. The
International version reads as the one for everyone else, but that is inference. The record keeps both, each with
a `scope` and a note, for `academic_vs_commercial`, `ai_training_terms` and `dpa`. `retention_terms` and
`gdpr_statement` are scoped to the International version, because the clauses they quote exist only there. The
watch list carries both PDFs.

## Fields where A and B disagreed

| Field | A | B | Decision and reason |
|---|---|---|---|
| research_program | Verified; 2022 release plus Asia grant | Corroborated; 2022 release plus Fitrockr page | **Verified**. Every claim rests on a Garmin newsroom page, all quotes exact. Added the gap hunter's KCL EMBRACE release. Used B's "no formal academic programme" framing, which A's pages also support. |
| program_eligibility | Two scoped entries (SDK enterprise; Asia grant) | One entry, adds business-use-only and an integrator's legal-entity quote | Kept A's two scopes. Folded B's FAQ and Open Wearables quotes into the SDK/programme entry. A's grant quote and B's were different passages; A's is exact on the live page and was kept. |
| program_status | stated, "Active" | stated, "Mixed", grants closed, CDP paused | **B's framing, Corroborated.** The research offering is visibly active (Garmin blog 21 Aug 2026 using the Health API and Companion SDK; SDK request route published), but no grant call is open (Fitrockr "To be announced"). A's "Active" alone hid that no grant is open. |
| developer_program_status | `conflict` (FAQ invites applications vs. support replies) | `stated`, Closed, Corroborated | **stated, Corroborated, "Paused to new applicants".** The FAQ's "please request ... we'll quickly review" is stale boilerplate. The FAQ page itself also carries "Stay tuned for more updates on the program", as does the overview page, and neither page has a request link. That is not two sources disagreeing about the facts, so `conflict` is wrong. It is not Verified, because the pause wording appears only in Garmin support replies reposted by users on Garmin's own forums (two threads) and in press (the5krunner, Terra). Added the5krunner's report that queued requests are frozen too. |
| device_price | CIRQA, Forerunner | vivosmart 5, CIRQA, Forerunner | Kept all three; all exact. vivosmart 5 marked as a 2022 launch price. |
| api_platform_fees | One entry, both routes | Split by Connect Developer Program and SDK | B's split. Added section 10.1 "no license fees" from the agreement (gap 2), which A and B both missed. |
| sampling_rates | Three scoped entries (Garmin Health API Verified; 25 Hz Reported via Fitrockr; Connect IQ) | One combined Corroborated entry with Fitabase and Avicenna | Four scoped entries so Garmin's own statement stays Verified and the integrator figures keep their own labels: Fitabase epochs Reported; 25 Hz Corroborated (Fitrockr and Avicenna agree independently); Connect IQ Verified. |
| rate_limits | not_public | stated (throttled, no figures) | **not_public.** The field asks for limits, and no figures are published. B's throttling and over-limit quotes are kept as context. |
| retention_terms | SCC annex retention plus data-subject rights | Same plus a termination quote | A's version. B's termination quote concerns deleting the API and brand features, not participant data. Scoped to the International agreement, since the China version has no such annex. |
| ai_training_terms | "No AI clause in the agreement" | Adds clause 15.10 from the China-entity version | Both are right about different documents. Two scoped entries (see above). |
| deprecations | unclear | stated, Corroborated (pause as deprecation) | **unclear.** No Garmin API shutdown or migration is announced. A pause of new applications is a status, already in `developer_program_status`. The redesign is reported, not specified. |
| baa | unclear | stated, Reported | **unclear.** Paubox's "Garmin will sign a BAA ... can be reviewed here" links to the Health SDK overview page, which mentions no BAA (the judge checked the link target). With no traceable evidence, Reported overstates it. |
| dpa | One entry (International) | One entry (International) | Agreed. Added a China-version entry for the PIPL annex (gap 9). |
| history_depth | unclear | unclear | Agreed. Added Open Wearables' historical-data page ("Limited to 30 days before the user") as a second page from the same integrator. |
| iso27001 / soc2 | not_public | not_public, with the 10-K tracker | Agreed. Merged source lists. |

Fields where A and B agreed and the better-sourced entry was kept: user_cap, academic_pricing, minimum_commitment,
quote_required, raw_streams, derived_metrics, export_routes, hipaa_statement, gdpr_statement, fda_clearances,
data_residency, subscription_price (A's `?p=5556` URL and B's long URL both exact; kept `?p=5556`).

## Gap-hunter findings

| # | Finding | Decision |
|---|---|---|
| 1 | FDA K221774 | **Accepted.** Already in both drafts. Confirmed via openFDA (applicant Garmin International, Inc.; 2023-01-12), cited with the accessdata page as `url`. openFDA `applicant:garmin` returns only K221774. The innolitics mirror was not used. |
| 2 | Agreement 10.1 says no licence fees | **Accepted.** Quote exact in both agreement versions. It contradicts the $5,000 admin fee: that figure is on no Garmin page, its source (techdepot.blog) returned 403, and aifitnessapi.com says only "some third-party reports mention a setup fee". Recorded as unsupported in the note. 10.1 does not rule out metric licence fees, which Garmin's FAQ and Health API page set outside the agreement. |
| 3a | Garmin Health launched the Asia 2026 grant itself | **Accepted.** Quote exact on Garmin's newsroom. |
| 3b | KCL EMBRACE, up to 40,000 participants, Garmin's largest research-institution deal | **Accepted.** Both quotes exact on garmin.com/en-US/newsroom/?p=5892 (17 Sep 2025). |
| 4 | Agreement AI Transparency Statement | **Accepted with a correction.** The clause exists only in the China-entity version. The gap hunter did not notice the two versions. |
| 5 | Research exemption from attribution | **Accepted**, scoped to the China-entity version, under academic_vs_commercial. |
| 6 | Redesign reason; queue frozen | **Accepted** into developer_program_status (the5krunner quote exact). The Strava lawsuit link is kept only as press context in the deprecations note. |
| 7 | ECG App EU MDR Class IIa | **Accepted as a note** on fda_clearances. Quote exact on Garmin Deutschland's mynewsdesk page. No EUDAMED check, and the field is FDA only. |
| 8 | Connect+ $6.99/$69.99 | **Accepted.** Already in both drafts; quotes exact. |
| 9 | China entity and PIPL annex | **Accepted.** dpa entry scoped to the China version, plus the version analysis above. |
| 10 | 8.4 bar on public statements | **Accepted as a note** on academic_vs_commercial. Present in both versions. No schema field fits. |
| 11 | Garth deprecated | **Accepted as a note** on export_routes. Quote exact on garth.readthedocs.io. The March 2026 date is not quote-verified and was left out. |
| 12 | 10-K NIST CSF, no ISO/SOC 2 | **Accepted** as context for iso27001/soc2 not_public. Quote exact on the tracker mirror; sec.gov not fetched. |

## Profile and matrix statements the record contradicts

| File | Line | What it says | What the record says |
|---|---|---|---|
| module-01-wearables/profiles/garmin.md | 137 | $5,000 administrative fee, "Reported, and specifically flagged as unconfirmed" | Agreement 10.1 says no licence fees or other payments are due, and the FAQ says no licensing or maintenance fees. The figure has no Garmin source and its cited source is unreachable. Downgrade to unsupported, or drop it. |
| module-01-wearables/comparison-matrix.md | 218 | "a $5,000 admin fee is Reported and unconfirmed" | Same as above. |
| module-01-wearables/profiles/garmin.md | 13, 18, 139, 152 | "no consumer subscription" | True for core metrics, but optional Garmin Connect+ ($6.99/month, $69.99/year) exists since March 2025 and paywalls some AI insights. |
| module-01-wearables/comparison-matrix.md | 218 | Recurring per participant "**None**" | Same as above; worth a qualifier. |
| module-01-wearables/comparison-matrix.md | 218 | Device cost "Wide retail range (no figure in profile)" | Launch prices now recorded: vivosmart 5 $149.99, CIRQA $199.99, Forerunner 70/170 $249.99 to $349.99. |
| module-01-wearables/profiles/garmin.md | 98 | "Research grants run through partners, not Garmin directly" | Garmin's own release says Garmin Health launched the Asia 2026 grant with Fitrockr. Garmin also signs direct institutional deals (KCL EMBRACE, Sept 2025). |
| module-01-wearables/comparison-matrix.md | 386 | "grants only through partners" | Same as above. |
| module-01-wearables/profiles/garmin.md | 49, 69; matrix 244 | ECG "region-gated" with no clearance named; regulatory "Not itemised in the profile" | ECG App FDA 510(k) K221774 (2023-01-12, Verified). Garmin also states EU MDR Class IIa. Index BPM's K221486 belongs to Ya Horng, not Garmin. |
| module-01-wearables/profiles/garmin.md | 130 | Privacy and compliance "Not established", GDPR DPA "not verified" | The International agreement sets Garmin as independent controller (no processor DPA), incorporates EU SCCs module one, and states a retention period. ISO 27001 and SOC 2 are not public. A BAA is unclear (one unsupported secondary claim). |
| module-01-wearables/comparison-matrix.md | 244 | GDPR / DPA "Unclear"; SOC 2 / ISO "Unclear" | GDPR/DPA: as above (Corroborated). SOC 2 / ISO: not public (no certificate; 10-K cites NIST CSF alignment only). |
| module-01-wearables/comparison-matrix.md | 386 | Retention and AI-training terms "Not published" | Retention: SCC annex period (International agreement). AI: brand guidelines require attribution; China-entity agreement 15.10 requires an AI transparency statement and explicit consent. |
| module-01-wearables/profiles/garmin.md | 207 | Key link "Developer Program Agreement (PDF)" is the www8 URL | That URL serves the Garmin China Shanghai RHQ version. The Garmin International version is on developerportal.garmin.com. Label both. |
| module-01-wearables/profiles/garmin.md | 22, 114 | Pause described for new requests only | Requests already in the queue are also frozen, and Garmin's stated reason is a programme redesign (the5krunner, 14 Sep 2026). Additive, not a contradiction. |

## For the coordinator to check by hand

- Which agreement version a US or EU licensee actually signs. Only Garmin can answer
  (connect-support@developer.garmin.com).
- The Garmin research page and the Connect privacy policy are script-rendered. Their hand-read content (Research
  Participation Program; US/UK/Australia storage and mainland-China storage) is in notes only.
- accessdata.fda.gov returns 404 to automated requests. The record uses openFDA as `fetch_url`, per the README.
- The fitrockr.com research-grants page was slow to respond during re-probing. The "CURRENT GRANTS" quote was
  confirmed exact earlier in the run, but the page's other quote (in B) was not re-confirmed and was dropped.
