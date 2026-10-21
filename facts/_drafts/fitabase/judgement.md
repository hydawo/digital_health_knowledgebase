# Fitabase: judgement (baseline fact run)

Judge run, 2026-10-21, from `A.yaml`, `B.yaml` (both 2026-10-11) and `gaps.md`. Output: `facts/fitabase.yaml`.
Every cited page was re-read on 2026-10-21, ten days after the drafts, because the Fitbit Web API turns off on
2026-10-30 and the migration pages had moved on.

Final record: 35 entries (30 fields; `raw_streams`, `derived_metrics`, `sampling_rates` and `history_depth` split
into Fitbit / Google Health and Garmin scopes; `gdpr_statement` split into a general entry and a scoped "Data
Privacy Framework certification" entry). Status: 19 stated, 13 not_public, 1 unclear, 2 not_applicable, 0
conflict. Confidence: 30 Verified, 2 Corroborated, 1 Unclear, 2 none (not_applicable). 80 quotes, every one
re-probed "exact" on 2026-10-21. `validate.py --file facts/fitabase.yaml`: 0 errors, 35/35 researched.
`weekly.py --only fitabase --no-state`: 53 pages, 0 missing, 0 reworded, 0 dead links (1 "page changed", the
homepage, which is expected with no stored state). Both ran on the live repo; the scratch-copy fallback was not
needed. Nothing was signed into, no form was submitted, the in-app browser pane was not used. The DPF lookup used
the registry list page's own read-only search request.

## Coordinator points

1. **Garmin SDK route: recorded as a second route, not a conflict.** What each source says:
   - KB "Collecting Enhanced Beat to Beat Interval Data Using Garmin Devices" (undated): Enhanced BBI "is captured
     during sleep directly from the wrist", gen 4+ sensors, and under the heading "Does Fitabase Collect EBBI from
     the Garmin SDK or the Garmin API?" answers with the API method built with Garmin "In early 2025". It does not
     mention an SDK route.
   - Blog "CIRQA: How can Garmin's screenless device work for research?" (2026-07-29): "Fitabase can help you pull
     them using the Garmin SDK" and participants "download the Fitabase Engage app and sync through it instead of
     the Garmin Connect app". It also says HRV and respiration "are measured during sleep" on CIRQA.
   - KB "Setting up Fitabase Engage for the Garmin SDK" (last updated 2026-04-15): troubleshooting only (restart,
     Bluetooth, reinstall needs a new enrollment code). No streams or rates.
   - App Store, Fitabase Engage (developer Small Steps Labs LLC), version history: 1.2 "Connect Garmin device
     directly to the Fitabase Engage app."; 1.3 "Fixes for Garmin SDK"; 1.4 "Fixes and enhancements for Garmin SDK".
     Found by this judge (the gap hunter found no listing).
   Daytime coverage, sampling rate, Enhanced versus legacy BBI and eligibility for the SDK route are all unstated;
   the record says so. `raw_streams [Garmin]` is Corroborated (vendor pages only). `sampling_rates [Garmin]` notes
   that no rate is stated for the SDK route.
2. **Historical Fitbit data: the "example-markdown-article" is rejected; field set to `unclear`.** The page is live
   and listed in the KB's Getting Started menu, titled "Setting Up a New Participant with a Fitbit Device", dated
   February 6, 2026. But its slug and its content both read as CMS sample text: it tells users to pair the Fitbit
   over Bluetooth by clicking "Connect Device" on the Fitabase participant page, to use "Project Settings > Data
   Collection", "Engage > Reminders" and "Fitbit.com > Settings > Personal Info". None of these match the rest of
   the KB, where participants authorize by invitation link or the Google Health app and sync windows are set on the
   participant's details page or at batch level. Not a reliable source. What remains: the example consent form page
   and its PDF (an older UCSD study) describe "Historical data collection" and authorizing download of "historical
   Fitbit data"; the sync-length article counts days "from the moment each participant's account is connected";
   devices hold minute and second data 5 to 7 days. None says whether pre-connection data can be pulled now, so
   `history_depth [Fitbit / Google Health]` is `unclear`, Unclear, with "ask Fitabase".
3. **DPF: found and Verified.** The list page's own search (the POST it makes to
   dpfapi.azurewebsites.net/api/participants) for "Small Steps" and for "Fitabase" returns one Active record,
   OrganizationId 7900, display name "Fitabase"; an "Inactive" search returns nothing. `participants/7900`:
   LegalName "Small Steps Labs LLC", San Diego, Self-Assessment, non-HR data only, JAMS plus FTC. EU-U.S. and
   Swiss-U.S. installed 2018-12-07, UK Extension 2024-06-27, all usage end 2027-10-16. Five lapses, the latest
   **2026-09-07 to 2026-10-16**, which explains B's empty result on 2026-10-11. Cited as `certificate` with `url`
   dataprivacyframework.gov/list and `fetch_url` the JSON, five exact quotes, plus the Privacy Policy self-claim.
   The registry also gives a "Purpose" text naming Microsoft Azure and payment processors as Fitabase's only agents.
   The Privacy Policy shows "last updated on October 1, 2026" and, in its DPF statement, "Updated: October 7, 2026".
   Added the registry to the watch list.
4. **Study counts: noted only.** Homepage "over 1,100 research studies" and customers page "900+ Institutions,
   2500+ Studies", both quoted in `research_program` with a note that they disagree and neither gives a method.
5. **Security PDFs.** Re-checked 2026-10-21: /media/2028/ (business environment analysis), /media/2029/ (security
   awareness training standard), /media/2030/ (cybersecurity policy) and the FAQ's /media/1723/ all 404;
   /media/1780/ (the security page's own link) is 200. Recorded in the `soc2` note. The dead URLs are not cited as
   sources, so the weekly check will not flag them; A's watch list entry for /media/1780/ was dropped in favour of the
   HTML security page, which carries the same text.
6. **ISO 27001.** Fitabase claims none of its own. The security page and PDF repeat Microsoft's old "Windows Azure"
   text that the data centres comply with "ISO/IEC 27001:2005", the host's certification against a superseded
   edition. `iso27001` not_public, with that note.
7. **Engage.** Relaunched 2026-04-21 (blog, quoted). On 2026-10-21 the homepage, /engage/, /engage/mobile/ and
   /engage/wrist/ all still say "Preview · Summer 2026", though summer has passed; the iPhone app is live (1.6.8,
   Oct 9). Recorded in `program_status`; general availability is not stated. No Google Play listing found.
8. **Other points, all accepted and quoted.** Google de-identified demo accounts (Google research application with
   IRB approval or waiver, 5 to 7 business days, six-month expiry extended in six-month increments, Fitabase supplies
   the client ID) in `program_application` and `user_cap`. Webhooks (2026-03-11) in `export_routes`. Garmin Index
   blood pressure (2026-01-20) in `raw_streams [Garmin]`. No GPS by design, two quotes, in `raw_streams [Fitbit]`.
   The annual cap on custom projects in `quote_required`.

**Google onboarding (coordinator update).** Google's pages no longer say "not onboarding new projects"; the
2026-10-21 About page says all scopes are Restricted and need a privacy and security review, then "Like what you
see? Get started now". A's `developer_program_status` quote from Google was dropped, and the record describes
Fitabase's route on its own terms, pointing to facts/fitbit-google.yaml for Google's access status.

## What changed on the migration pages since 2026-10-11

- Reauthorization: was "Mid-to-late October 2026 (exact date TBD)", now "October 15, 2026 Reauthorization opens in
  the Fitabase platform"; the Google Health app's Partner apps screen already offers it. Target date now 30
  October (the 2026-09-10 webinar post still says 31 October).
- Grace period wording changed from "reconnect banner" to "reconnect option stays on the Partner apps screen";
  both drafts' quote for it is now missing and was replaced.
- Migration overview now says "retiring the Fitbit Web API on October 30, 2026" (was "at the end of October 2026");
  quote replaced.
- New: Dataset Availability page (updated 2026-10-14): 29 of 40 exports available from the Google Health API, 8
  "Transition delayed" (Activity Logs, Sedentary Time, Intraday Calories, Intraday METs, ECG Logs, Weight Logs, Food
  Logs, Wear Time via HR), 3 "Fitbit API only" (Daily Sleep, Sleep Logs (Minute), Sleep Log Info; use Sleep Stages
  exports), 5 new Google-only datasets "Coming Soon". Google Health ECG import is paused.
- New: blog 2026-10-19, all active Fitbit projects ending before 2027-01-01 extended to that date at no charge,
  because some datasets will not be delivered before reauthorization; it lists Intraday Calories, Intraday METs,
  ECG and SpO2 as outstanding, while the dataset table shows Daily and Minute SpO2 as Available (noted, not
  resolved).
- Unchanged: classic sleep folded into the main sleep export, step-goal writing not yet available ("next
  quarter"), no programmatic reauthorization, Fitabase API unchanged, UTC, time zone and source columns.

## Fields where A and B disagreed

| Field | A | B | Decision |
|---|---|---|---|
| research_program | Stated, no Health Equity mention | Adds 2021 Health Equity initiative | B's addition kept (quote exact); gap G2 counts added |
| program_eligibility, program_application, developer_program_status, export_routes, api_platform_fees, derived_metrics, sampling_rates, raw_streams, data_residency | Corroborated | Verified | Verified: each is the vendor's own documentation of its own product or terms, not a self-claim field. `raw_streams [Garmin]` stays Corroborated because of the SDK route's blog-only evidence |
| not_public fields (user_cap, academic_vs_commercial, academic_pricing, minimum_commitment, rate_limits, ai_training_terms, baa, dpa, hipaa_statement, iso27001, soc2) | Unclear | Verified | Verified, matching the other records: the absence was searched and is dated |
| subscription_price | not_public ("Custom Pricing for Every Study") | not_applicable (no consumer offering) | not_applicable: the field is consumer subscription price; study pricing is in api_platform_fees and quote_required |
| developer_program_status | Fitabase API add-on plus Google "not onboarding" quote | Fitabase API add-on plus authentication quote | B's framing; Google quote dropped (removed from Google's pages); FAQ "Fitabase API unchanged" quote added |
| history_depth [Fitbit] | conflict (template article vs consent form) | stated (5-7 day device memory only; "no public statement") | `unclear`, template article rejected (point 2) |
| history_depth | Split by scope | Single entry | Split by scope (Garmin stated, Fitbit unclear) |
| retention_terms | Privacy and Terms only | Adds IRB 90-day text and 30-day inactive-account clause | Both merged; 90-day rule flagged as example IRB text only |
| deprecations | 2026-10-11 dates | 2026-10-11 dates plus backfill and March blog note | Rebuilt from the 2026-10-21 pages (see above) |
| gdpr_statement | Stated, DPF self-claim, registry not confirmed | Stated, DPF self-claim, registry search empty | Split: general entry not_public (GDPR not named anywhere); DPF entry Verified from the registry (point 3) |
| fda_clearances | 5 openFDA queries | 3 openFDA queries | Union of 6, all re-run 2026-10-21, all NOT_FOUND |
| derived_metrics | Split by scope; no Body Battery | Single entry; adds Body Battery, respiration, sleep scores | Split by scope; B's Garmin additions kept |

No conflicts remain in the final record.

## Gap-hunter findings

| Gap | Decision |
|---|---|
| G1 Garmin SDK route | Accepted, with the App Store evidence added (point 1) |
| G2 Study counts | Accepted as a note in research_program (point 4) |
| G3 Engage relaunched | Accepted in program_status (point 7) |
| G4 Google demo accounts | Accepted in program_application and user_cap |
| G5 Custom-project cap | Accepted in quote_required |
| G6 Reauthorization window, backfill | Accepted, dates updated to the 2026-10-14 pages |
| G7 Classic sleep, step goals, API unchanged | Accepted in deprecations and developer_program_status |
| G8 Export source column | Accepted in export_routes |
| G9 Webhooks | Accepted in export_routes |
| G10 Garmin Index BPM | Accepted in raw_streams [Garmin] |
| G11 Fitbit Air, CIRQA, second-device caveat | Accepted as a note in raw_streams [Fitbit]; CIRQA quoted for the SDK route |
| G12 Second-level heart rate | Accepted (both drafts already had it) |
| G13 Historical Garmin opt-in | Accepted (history_depth [Garmin]) |
| G14 Azure, snapshots, ISO 2005 | Accepted (data_residency note, iso27001 note) |
| G15 No GPS by design | Accepted, second quote in raw_streams [Fitbit] |
| G16 Small team, no openings | Rejected: no schema field, and the headcount figure is an unquoted third-party estimate |
| "App store listing not found" | Overturned: Fitabase Engage is on the US App Store (id6496601338) |

## Statements in the profile, matrix and related files that the record contradicts or leaves incomplete

Not edited; for the coordinator.

| File | Line | What it says | What the record says |
|---|---|---|---|
| module-01-wearables/profiles/data-intermediaries.md | 33 | Granularity "Daily, hourly, minute-level" | Second-level heart rate (3 to 15 s), 30 s sleep stages (`sampling_rates`) |
| same | 35 | API: "Aggregate Data API" only | Also the Fitabase API add-on (Daily Activity, Profiles, Sync, Batch Export), daily scheduled exports, webhooks (`export_routes`) |
| same | 37 | Engage under "Coming", "Preview · Summer 2026" | Relaunched 2026-04-21; iPhone app live (1.6.8, Oct 9); pages still say Summer 2026 preview (`program_status`) |
| same | 38, 96 | Track record "over 1,100 research studies" / "1,100+ studies" | Customers page also says "900+ Institutions, 2500+ Studies"; vendor figures disagree (`research_program`) |
| same | 40 | Compliance checked FAQ, privacy, terms only; nothing published | Same conclusion for HIPAA/BAA/SOC 2, but Fitabase is Active on the DPF registry (EU-U.S., Swiss-U.S., UK, Verified) and hosts on Azure in the US (`gdpr_statement`, `data_residency`) |
| same | 94 | EMA/surveys "Engage suite, Summer 2026" | As line 37 |
| same | 212 | "A new direct Google Health API project is not possible while Google is not onboarding new projects (2026-10-10)" | Google's onboarding line was removed by 2026-10-19 (coordinator; see fitbit-google.yaml). Fitabase's own route is unchanged |
| module-01-wearables/comparison-matrix.md | 107 | "Fitabase's API route captures it during sleep" | True for the API route, but Fitabase also offers a Garmin SDK route via the Engage app; its daytime coverage is not stated (`raw_streams [Garmin]`) |
| same | 188, 355 | Fitabase Engage "Preview · Summer 2026" / "Engage apps in preview, Summer 2026" | As data-intermediaries.md line 37 |
| same | 358 | Sampling resolution "Enhanced BBI via Garmin OAuth, during sleep" | Incomplete: SDK route also exists (rate unstated) |
| same | 380 | Daytime HRV poor fit: "Garmin Enhanced BBI via the Health API or Fitabase (captured during sleep)" | Fitabase's SDK route is not shown to be sleep-only; daytime coverage unstated |
| module-01-wearables/profiles/garmin.md | 59, 102 | "Fitabase's API route captures it during sleep"; "Fitabase (Garmin API route, Enhanced BBI during sleep...)" | Incomplete: SDK route via Engage app exists |
| module-01-wearables/profiles/fitbit-google.md | 49 | "Fitabase asks for participants to be reconnected by 31 October" | Key-dates page (2026-10-14) now gives 30 October as the target, reauthorization opened 15 October, grace through 30 November (`deprecations`) |
| same | 216, 366 | Migration consequences: reauthorization and new export columns only | Also 8 exports delayed, 3 classic sleep exports Fitbit-API-only, ECG import paused, projects extended to 2027-01-01 at no charge |
| same | 225 | Fitabase "expects minimal change to existing datasets" | Dataset table shows 11 of 40 exports not yet on the Google Health API (2026-10-14) |
| same | 18 | "used in over 1,100 research studies" | As data-intermediaries.md line 38 |
| shared/unresolved-questions.md | 103 (Q74) | Answered as API route (sleep) vs Labfront SDK route (all day) | Fitabase now has an SDK route too; the comparison needs reopening |
| same | 274 (Q8) | "Engage in preview" | Engage relaunched; app live; price still unpublished |

## For the coordinator to check by hand

- **Q74 and the daytime-HRV rows.** Ask Fitabase what its Garmin SDK route collects (daytime BBI? Enhanced or legacy?
  rate?), and who can use it. This is the main open question the record raises.
- **Historical Fitbit data.** Ask Fitabase whether pre-connection Fitbit or Google Health data can be pulled, and
  whether the "example-markdown-article" page is meant to be published.
- **SpO2.** The 2026-10-19 blog lists SpO2 as outstanding while the dataset table (2026-10-14) shows it Available.
- **Re-check right after 2026-10-30.** `program_status` and `deprecations` have recheck_by 2026-11-02; the dataset
  table and key dates are likely to change again.
- **Engage status.** "Preview · Summer 2026" labels are stale on every Engage page; general availability is
  unconfirmed.
- The DPF entry has had five lapses, the latest ending 2026-10-16, five days before this check; worth a glance at the
  next quarterly re-check.
