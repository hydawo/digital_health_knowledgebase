# Judgement: fitrockr (2026-10-21)

Inputs: A.yaml (Wayback captures, 2025-09 to 2026-10-07), B.yaml (live site read on 2026-10-21), gaps.md.
Output: facts/fitrockr.yaml. 30 of 30 fields researched, 0 validation errors.

## Access situation

On 2026-10-21 www.fitrockr.com was blocked to scripts again (MalCare firewall, HTTP 403). It failed on my
first quote_probe, and the coordinator saw the same thing on /pricing/ and /help-center/. I did not retry
live fitrockr.com pages and did not try to get around the block. As a result:

- **No fitrockr.com quote could be re-read live by the judge.**
- **Quotes re-confirmed "exact" against Wayback captures** (each source carries a `fetch_url`): grants
  page (2026-07-13), old pricing page /research/pricing/ (2026-07-13), old help-centre articles
  (privacy-security 2026-04-29, data-export 2026-07-13, data-dictionary 2026-07-13, HRV via Garmin
  Connect 2026-06-17, long-term storage 2026-04-22, pricing-plans-payment 2026-04-22, Garmin sync
  transition 2026-04-29, smartphone sync 2026-04-29, device runs full 2026-07-13), the **new**
  /help-center/data-dictionary/ (2026-09-07, the only capture of a restructured page), API article
  (2025-09-09), terms effective 2025-11-09 and privacy policy of 2026-01-28 (both captured 2026-05-11),
  Data Vault (2026-04-14), country-of-choice hosting (2026-06-17), HIPAA news post (2026-04-22),
  unlimited-users news post (2026-05-15), GPS switch-off post (2026-06-16), Fitbit Air post (2026-06-16),
  export enhancements (2026-10-07).
- **Quotes resting only on researcher B's live reading of 2026-10-21** (no `fetch_url`, each noted "Read
  by researcher B on 2026-10-21; site blocks scripts, not re-confirmed by the judge"). No capture exists
  of the new /pricing/, /features/, or the 2026-09-19 terms and privacy policy (CDX checked). These pages
  are: /pricing/ (new prices, Data Vault EUR 250, +25% sensor add-on, 2-year import EUR 500, "Germany
  cloud hosting included", quote-request line), /help-center/pricing-plans-payment/ ("based on user
  numbers"), /features/ (HIPAA certified, CASA, ISO, sampling rates), /health-solutions/terms-of-use/
  2026-09-19 (retrieval period, AI clause, DPA, no auto-renewal, integrations), and
  /health-solutions/privacy-policy/ 2026-09-19 (BAA, AI, HIPAA scope, Chapter V).
- **Confirmed live by the judge on non-Fitrockr hosts:** Garmin's 2026-03-05 release, App Store (Fitrockr
  Sync; old app id1553631734 returns 404), Google Play (Fitrockr Sync, updated Oct 7, 2026), openFDA
  (NOT_FOUND on all four queries) and PMC12975902.

Every fact that rests on a fitrockr.com page (capture or B's reading) is **Reported** with recheck_by
**2026-11-04**. Exceptions: the three grant fields backed by Garmin's live release (research_program,
program_eligibility, program_application) are Corroborated with recheck 2026-11-20, and fda_clearances
is Verified with recheck 2027-01-19. The weekly check will put every live fitrockr.com source under
"unreachable", then "check by hand", while the firewall is up. Those pages need a person with a browser.
They are the B-only pages listed above, plus the watch list's fitrockr.com pages.

Rule applied on A vs B: where B's live value differs from A's capture, B's value is recorded as the
current one, labelled as B's reading, and A's capture value goes into the note as dated history
(coordinator instruction). Where both agree, the capture quote is the primary source because it can
be re-checked.

## Fields where A and B disagreed

| Field | A | B | Decision |
|---|---|---|---|
| research_program | Reported, captures | Verified, live | Same substance. Corroborated, because Garmin's live release confirms the 5 vivoactive 5 watches and the 6 months of access. The round history rests on the capture. |
| program_status | "No current grant" (July capture) | "To be announced" (live) | Agree. Kept the capture quotes, added Garmin's "Deadline: March 31, 2026." Reported. |
| developer_program_status | No public program, add-on | Same, plus a "Wearable API" product from EUR 150 a month for 20 users | Kept the shared substance. B gave no quote for the Wearable API product, so it is only in the note, marked unconfirmed. |
| user_cap | Stated (unlimited users, device-based) | Stated, with a note that the help centre still says user-based | **Conflict.** The pricing page ("Users: Unlimited", device licences) and the help article ("Our pricing is based on user numbers and length of access.") were both live per B, and both appear in captures (pricing 2026-07-13, help article 2026-04-22). |
| academic_vs_commercial | stated | not_public | stated (Reported). A single price list plus "contact us ... limited research funds" is a positive statement that there is no separate tier and a custom-quote route exists. |
| api_platform_fees | Data Vault EUR 150, sensors "Volume Based", live EUR 500 + 20% (2026-07-13 capture) | Data Vault EUR 250, sensors +25%, live +20%, per-stream table removed (live) | B's live values recorded as current (Reported, B's reading). The capture values are in the note. Unchanged plan prices are quoted from both. |
| quote_required | "Get in touch" plus old terms 4.2 | New "fixed pricing contracts or pay-as-you-go" line plus help centre | Merged. Same answer ("partly"). |
| raw_streams | Pricing-table quotes | Data dictionary, pricing +25% | Merged. Used the 2026-09-07 capture of the new data dictionary for 25 Hz. |
| sampling_rates | Per-stream Basic vs Pro table | Fixed 25/32 Hz, configurable epochs, table removed | B's current picture, backed by the 2026-09-07 capture. The old table is in the note as history. |
| history_depth | unclear | stated (2 years via Garmin Connect, EUR 500; device overwrite) | **stated.** B's help-centre quotes match the 2026-04-29 and 2026-07-13 captures of the old article URLs exactly, so A's "unclear" came from not finding those articles. The EUR 500 price is B-only. |
| export_routes | Captures | Live | Same substance. Capture quotes kept. |
| rate_limits | not_public, Unclear | not_public, Verified | not_public, Reported. B's "documented API or usage limits" terms wording is in the note only. |
| retention_terms | 2025-11-09 terms: "irreversibly deletes all data at the end of Service"; Data Vault EUR 150 | 2026-09-19 terms: delete or return after a retrieval period; Data Vault EUR 250 | B's new terms recorded as current. The old wording is in the note. Per-project server deletion confirmed in the capture. |
| ai_training_terms | not_public (no AI language in the old terms or policy) | stated (2026-09-19 terms and policy) | **stated**, B's reading, Reported. A's finding kept in the note as history. |
| deprecations | Garmin sync change, old iOS app gone | Garmin sync change, integrations clause | Merged both. Old app 404 and current app confirmed live by the judge. |
| baa | not_public (old pages) | stated (2026-09-19 policy) | **stated**, Reported (B's reading). I confirmed the 2026-01-28 policy capture has no "Business Associate" text, so the offer is new. |
| dpa | Stated, old terms 5.2 | Stated, new terms | Both quotes kept. Reported. |
| hipaa_statement, gdpr_statement, iso27001 | Reported, captures | Corroborated, live | Reported, because the live quotes cannot be re-checked. The cap would be Corroborated anyway. |
| soc2 | not_public, Unclear | not_public, Verified | not_public, Reported. |
| fda_clearances | not_public, Verified | not_public, Verified | Agree. Kept A's expect_absent queries plus B's registration.name query. All re-run, NOT_FOUND. |
| data_residency | Germany, or Germany or Switzerland | Same, plus country of choice | Agree. Kept the capture quotes and added the military on-premise quote. B's privacy-policy "EEA, US or elsewhere" is in the note only, since B recorded no quote for it. |

Disagreements: 15 fields (user_cap, academic_vs_commercial, api_platform_fees, sampling_rates,
history_depth, retention_terms, ai_training_terms, baa, rate_limits and soc2 confidence,
developer_program_status scope, plus confidence-only differences on research_program and the
compliance self-claims). Conflicts recorded: 1 (user_cap).

## Coordinator's points

1. **Pricing:** recorded as B reported it, labelled, with July values as history. The help centre's
   "based on user numbers" against the pricing page's unlimited users and device licences is recorded
   as a conflict in user_cap. The Wearable API product (EUR 150 a month, 20 users) has no quote from B,
   so it is in notes only.
2. **Raw data:** the Fitrockr app route versus Garmin Connect "supports less data", BBI every beat,
   25/32 Hz fixed, 2-year backfill for Garmin Connect-linked users only, and the September 2025 loss of
   sleep data on 13 models are all in raw_streams, sampling_rates, history_depth and deprecations.
3. **Retention:** per-project server deleted at study end (capture), 2026-09-19 delete-or-return after
   a retrieval period (B), BSON dump (capture). The help article lists no fee for the dump, but the
   quoted sentence does not say it is free, so the record does not claim "free".
4. **Compliance:** BAA new in the 2026-09-19 policy. "HIPAA certified" names no certifier. ISO 27001
   applies to the hosting centre. DPA where required. CASA is claimed. No SOC 2, no FDA record. Hosting
   is Germany (Switzerland on one page) with add-ons. All Reported; none above Corroborated.
5. **AI clause:** recorded with the anonymised/aggregated carve-out spelled out in value and note.
6. **Grants:** corroborated by Garmin's 2026-03-05 release (watches, 6 months, eligibility, deadline).
7. **Old iOS app** id1553631734 returns 404 (expect_absent). The current app is Fitrockr Sync on iOS
   and Google Play.
8. **Addresses:** Friedrichstr. 155 (privacy policy of 2026-01-28) and Friedrichstraße 114A (terms of
   2025-11-09), both seen in captures. Noted in gdpr_statement only.

## Gap-hunter findings

| Finding | Decision |
|---|---|
| A1 ISO scoped to the hosting centre | Accepted (iso27001). |
| A2 "HIPAA certification" self-described | Accepted (hipaa_statement). The gap hunter's "no BAA offer found" is superseded by the 2026-09-19 policy (B). |
| A3 Germany or Switzerland | Accepted (data_residency, note). |
| B1 grant packages, 3 vs 6 months | Accepted (research_program). |
| B2 winners and round history | Accepted in summary (research_program, program_status). Winner names are not recorded. |
| C1 sleep data dropped for 13 models | Accepted (deprecations). |
| C2 GPS switch-off per study | Accepted (raw_streams source, capture confirmed). |
| C3 Fitbit Air | Accepted as a note in raw_streams. The data route is not stated. |
| D1 per-project server deletion | Accepted (retention_terms). |
| D2 project-purpose only, no AI terms | Superseded by the 2026-09-19 AI clause. The purpose quote is kept as context. |
| E1 two APIs, gated docs, Bern plugin | Accepted (developer_program_status, export_routes). The GitHub plugin is in a note, not a quoted source. |
| F1 25 Hz CSV export in a paper | Accepted (raw_streams, shortened quote, see below). F1's second paper was not used. |
| F2 manual sync burden | Not a schema field. Rejected for the record; belongs in Module 3. |
| F3 clinic-hosted and FHIR use | Not added. It supports hosting options, which is a platform-only field. |
| F4 smartphone incompatibility exclusion | Not a schema field. Rejected. |
| G1 300+ projects, 27,000 daily participants | Not a schema field. Rejected. |
| G2 Fitrockr Sync app | Accepted (deprecations). |

Quote fix: the gap hunter's PMC12975902 sentence returned "missing" because the page's "25 Hz" uses a
special space. I shortened it to the part after "(25 Hz)", which probes exact. The opening words are in
the source note.

## Profile and matrix statements the record contradicts

| File | Line | Says | Record says |
|---|---|---|---|
| module-01-wearables/profiles/data-intermediaries.md | 111 | Data Vault "€150 per month" | EUR 250 per month (B's live reading 2026-10-21); EUR 150 was the 2026-07-13 price |
| data-intermediaries.md | 111 | Pro "higher sampling rates"; implies a per-stream table | The per-stream table has been removed (B). Accelerometer and gyroscope are fixed at 25/32 Hz. |
| data-intermediaries.md | 111, 237 | Source URL fitrockr.com/research/pricing, "Verified" 2026-10-10 | Pricing has moved to /pricing/. The site blocks scripts, so the record is Reported. |
| data-intermediaries.md | 111 | "Add-ons include ... API access +20%" with no live-streaming price | Live streaming was EUR 500 + 20% in July and is now +20% (B, unquoted) |
| data-intermediaries.md | 112 | "Germany cloud included"; "HIPAA-, CASA- and ISO-certified" | Germany or Switzerland on one page. ISO applies to the hosting centre only. HIPAA "certification" has no certifier. A BAA is now offered (2026-09-19 policy). |
| data-intermediaries.md | 113 | Asia 2026 grant "(five vívoactive 5 units)" only | The award also includes 6 months of platform access for up to 50 participants |
| data-intermediaries.md | 116 | Licensing per device, "inference" | The pricing page says this, but the help centre still says pricing is based on user numbers (conflict) |
| module-01-wearables/comparison-matrix.md | 236 | "Raw accelerometer and gyroscope +25%" | Agrees with B's live reading. In the July capture it was "Volume Based", so the line is right now but was not verifiable on 2026-10-10 from the old URL. No change needed. |
| comparison-matrix.md | 414 | "Fitrockr Data Vault €150/month" | EUR 250 per month (B) |
| module-01-wearables/profiles/garmin.md | 98 | Asia 2026 grant "offered five vívoactive 5 units" | Also 6 months of platform access for up to 50 participants. Not wrong, but incomplete. |
| garmin.md | 229 | Eligibility "postgraduates, PhD candidates and senior scholars in 11 Asian markets" | Garmin's live release: "Academic researchers, post-docs, and graduate students in Asia". This is probably different wording of the same call, so check the source the profile used. |

Missing from the profile entirely: the September 2025 loss of sleep data for 13 Garmin models on
Fitrockr-app sync, per-project deletion at study end, the AI clause, the BAA offer and the Garmin
Connect versus Fitrockr-app data difference.

## Check by hand

- Open in a browser: /pricing/, /features/, /help-center/pricing-plans-payment/, and the 2026-09-19
  /health-solutions/terms-of-use/ and /health-solutions/privacy-policy/. Confirm B's quotes, the
  2026-09-19 dates, the live-streaming price and the Wearable API product (EUR 150 a month, 20 users).
  Then the B-only facts can go from Reported to Verified or Corroborated, with normal recheck dates.
- Whether the help centre's "based on user numbers" line is still live (user_cap conflict).
- Garmin profile line 229 wording against Garmin's release.
