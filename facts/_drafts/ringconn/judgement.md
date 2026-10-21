# RingConn: judgement, 2026-10-21

Inputs: `A.yaml` and `B.yaml` (both read 2026-10-21; B first researched 2026-10-11), `gaps.md` (2026-10-21), the starter `facts/ringconn.yaml` (all `unresearched`) and `module-01-wearables/profiles/emerging-platforms.md` (RingConn section, lines 128 to 134). Output: `facts/ringconn.yaml`, 34 entries (19 stated, 10 not_public, 4 not_applicable, 1 unclear, 0 conflict), 81 quotes, 14 watched pages. Every quote matched "exact" with the same fetch and `match_quote` as `quote_probe.py`. `validate.py --file facts/ringconn.yaml`: 0 errors, 34/34 researched. `weekly.py --only ringconn --no-state`: 29 pages, 0 quotes missing, 0 reworded, 0 dead, 0 check by hand; one "page changed" (the Health Connect migration article, against the starter fingerprint). No scratch copy was needed. Re-check dates: 2026-11-20 for research access, pricing and data; 2027-01-19 for compliance. The in-app browser was not used. The Terms of Service page is disallowed by robots.txt and was not fetched; the record says it is unread wherever it would matter (developer_program_status, retention_terms, baa, data_residency).

## Coordinator's points

1. **FDA.** Confirmed in openFDA today (dataset last updated 2026-10-12). K260490, "Ninenovo Blood Oxygen Ring (BORMB-01-6 ... BORMB-01-14)", applicant Shenzhen Ninenovo Technology Limited, DQA (oximeter, 870.2700, class 2), received 2026-02-13, decision SESE 2026-10-02, Traditional. It is recorded as stated and Verified, with the accessdata page as `url` and the openFDA query as `fetch_url`. The value says plainly that no source links the BORMB-01 models to a consumer RingConn model, and that the Gen 3 page still says "This product is not a medical device." One finding: B's `applicant:ninenovo` search returns K260490 for me today, so B's "No matches" was wrong or stale. All other negative searches (applicant ringconn and onovo, device_name ringconn, three registration-listing searches) still return no match and are listed in the note. The Gen 2 and Gen 2 Air static pages carry no medical-device disclaimer, so only Gen 3's disclaimer is quoted.
2. **Raw PPG.** Split into two scoped entries. *Consumer and public routes*: not_public, Verified. *Company research collaboration*: stated, **Reported**. It rests on one company-involved paper, and RingConn publishes nothing about it. Four quotes are exact against the Research Square preprint PDF (customised firmware and app build for research data export, 100 Hz, green channel only, companies provided equipment and technical support). The version of record (BMC, DOI 10.1186/s13102-026-01960-x, 2026-08-18) is confirmed through Crossref, but biomedcentral.com and link.springer.com serve a bot challenge to scripts, so they were not read and the challenge was not bypassed. The note says this is not a general offering.
3. **2026-10-17 rewrites.** *Business article*: the Wayback 2025-11-25 partnership sentence is exact on the archive and "missing" on the live page. The live page is stamped "Updated October 17, 2026." The dated history sits in notes under `research_program` and in the value and note of `program_status` (now stated, Corroborated, because the removal is shown by absence plus an archive). *Data-security article*: the current wording quoted is the UK disclaimer ("does not support a blanket statement ... United Kingdom") and "Is all RingConn data stored in the U.K.? ..." (B's quote, used in the drafts; I kept A's sentence). I searched the live text for "AWS", "Amazon", "download all" and "research" and found none of them; the only "United Kingdom" hits are the region menu and that disclaimer. The removed claims (UK storage, AWS, "download all your data", no hidden backups, research opt-in) are recorded as history in the notes of data_residency, export_routes, retention_terms and ai_training_terms. They rest on the researchers' 2026-10-11 reading only, because the gap hunter found no Wayback capture of this article. *Privacy commitments page*: the unnamed "EU cybersecurity certification" claim is still live and is quoted in gdpr_statement and iso27001.
4. **Sampling.** `unclear`. App Features has no "2.5", "every" or "min" in today's static rendering. The 100 Hz figure applies only to the research firmware and is mentioned in the note, not used as the consumer rate.
5. **Offline storage.** Both drafts were right, for different pages. Split by scope. Gen 3: 10 days (Gen 3 spec block, Gen 3 manual). Gen 2 and Gen 2 Air: each product spec says "Offline Storage 5–7 days", while both compare tables say 7 days. I recorded the value as 5 to 7 days, with the 7-day table figure noted. I checked the column order on both tables: /pages/product-compare is Gen 3, Gen 2, Gen 2 Air, and the Gen 3 page table is Gen 3, Gen 2 Air, Gen 2.
6. **Health Connect, Apple Health, Google Fit.** derived_metrics carries the Health Connect list (including height and weight), HRV not synced ("algorithm compatibility issue", plus the guide's "does not export HRV"), Apple Health confirmed by RingConn's own guide (types not listed) and BP results excluded from all third-party platforms. Google Fit's end (2025-10-01 23:00 UTC) is under deprecations. The Apple Health guide still names Google Fit; that is noted.
7. **Prices.** Gen 3 $349, Gen 2 $299, Gen 2 Air $199 (B's three scoped entries), no subscription, student 10% via ID.me (the page says "Gen 2 Order", recorded as such), bulk on request. **New finding:** the US App Store lists in-app purchases "RingConn Partner+(Monthly) $5.99" and "(Annual) $69.99", both exact. Neither draft had them, and no RingConn page found says what they unlock. Recorded in subscription_price as optional and undocumented.
8. **Data residency.** China users stay in China; everyone else is stored outside China, possibly in another jurisdiction, with SCCs. For all users, Sentry crash data and customer-service data are processed in mainland China (both quoted; "Data shared with customer service systems will be stored on cloud servers located in Mainland China." is new). The App Store seller is Onovo Technology (Hong Kong) Limited (quoted) and the policy's controller is Shenzhen Ninenovo; the note says the contracting entity for a study is not stated.
9. **Blood Pressure Trends beta.** retention_terms quotes the retention-table row (PPG raw signals, accelerometer, skin temperature; anonymised within 90 days after the beta) and the "physical deletion ... not possible" sentence. ai_training_terms quotes the own-models-only clause.
10. **Oura licence.** Under deprecations, with the Oura blog quote (dated October 21, 2025, typed secondary) and RingConn's own US-continuity quote.

## Fields where A and B disagreed

| Field | A | B | Decision and reason |
|---|---|---|---|
| research_program | not_public, Corroborated | not_public, Verified | not_public, Verified. A dated "not published" is not uncertain. Added the Wayback quote. |
| program_eligibility | not_public | not_applicable | not_applicable: no program exists. A's quote moved into the note. |
| program_status | not_public | not_applicable | stated, Corroborated: the removal of the partnership invitation is the status change worth recording (point 3). |
| developer_program_status | not_public, Corroborated | stated, Reported (nextpit) | not_public, Verified, with both drafts' sources. "No developer program" is a not-published finding, not a statement someone made. |
| academic_vs_commercial | Corroborated | Verified | Verified, with a pointer to the collaboration route. |
| device_price | One entry with variants | Three scoped entries | B's scopes, A's variant prices in notes (from products.json, not quoted). |
| academic_pricing | not_public | stated (student, bulk) | stated, Verified. The student and bulk offers are published facts; the absence of research pricing is in the value. |
| raw_streams | not_public, Corroborated | not_public, Verified | Two scoped entries (point 2). |
| sampling_rates | not_public | unclear | unclear (point 4). |
| history_depth | stated, 10/7/7 | unclear, 5 to 7 | Two scoped stated entries (point 5). |
| baa, dpa, hipaa_statement, iso27001, soc2 | Corroborated | Verified | Corroborated, following the self-claim cap fields' practice in other records. |
| gdpr_statement | store-policy SCC/IDTA quote | summary-page quotes | Merged. Added the summary page's own SCC sentence, and noted that /pages/privacy-policy is the store notice. |
| fda_clearances | stated, K260490 | not_public | A, after my own openFDA check (point 1). |
| deprecations | Google Fit only | Adds Oura licence | B. |
| derived_metrics, export_routes | Various | Various | Merged. Added the Apple Health guide and OpenCircuit. B's Sahha quote left out (it is script-rendered and only says the name is listed), mentioned in the note. |
| watch list | 14 pages incl. sitemap, manual, Play Store | 14 incl. openFDA search, security-disclosure | 14: business article, compare, three product pages, student page, app policy, privacy summary, data-security article, migration article, data-sync guide, FDA K260490 (with fetch_url), App Store, Oura ITC post. |

No field was left as `conflict`.

## Gap hunter findings

| Finding | Decision | Why |
|---|---|---|
| 1 K260490 | Accepted | openFDA confirmed today; TechNode quote exact. Japan comment kept as a note only (secondary). |
| 2 Removed partnership paragraph | Accepted | Wayback quote exact; live probe missing. |
| 3 Raw PPG at 100 Hz via customised firmware | Accepted, Reported, scoped | Preprint quotes exact; VoR bot-challenged (point 2). Sample size not recorded (gaps.md says 64; the preprint text mentions 89 recruited, and I did not settle the analysed N). |
| 4 Apple Health confirmed on RingConn guide | Accepted | Both quotes exact; used in derived_metrics and export_routes. |
| 5 Oura licence | Accepted | Quote exact. |
| 6 npj DOI 10.1038/s41746-026-03036-z | Accepted as a note | No schema field; DOI mentioned in research_program note. |
| 7 T2D CGM preprint | Rejected for the record | No field needs it; Module 3 scan-queue candidate for the coordinator. |
| 8 OpenCircuit account-free, Gen 3, non-commercial licence | Accepted in export_routes | Account-free quote exact; licence in note. Its "AWS, UK" claim is not used for data_residency. |

## Profile and matrix statements the record contradicts

The comparison matrix has no RingConn row.

| File | Line | Says | Record says |
|---|---|---|---|
| module-01-wearables/profiles/emerging-platforms.md | 134 | Apple Health sync is "**Unclear**, not confirmed on a RingConn page" | Confirmed on RingConn's own guide (`/blogs/guides/how-sync-health-and-sleep-tracker-data`) and in the app privacy policy; HealthKit types not listed. |
| module-01-wearables/profiles/emerging-platforms.md | 134 | Researchers get "summary metrics, not raw PPG" | True for public routes. One company collaboration released raw 100 Hz finger PPG via customised firmware (Reported, COI). |
| module-01-wearables/profiles/emerging-platforms.md | 134 | Silent on FDA | 510(k) K260490 cleared 2026-10-02 for the "Ninenovo Blood Oxygen Ring" (SpO2); not linked to a consumer model. |
| module-01-wearables/profiles/emerging-platforms.md | 134 | Silent on US availability risk | Oura multi-year royalty-bearing patent licence (October 2025). |
| module-01-wearables/profiles/emerging-platforms.md | 134 | OpenCircuit "is not a supportable research route" | Still true, but it now runs with no RingConn account on Gen 2 and Gen 3, under a non-commercial licence. |
| module-01-wearables/profiles/emerging-platforms.md | 130 | RingConn publishes no research programme | Still true; a published partnership invitation existed until the 2026-10-17 rewrite and should be recorded as a change. |
| shared/unresolved-questions.md | 333 | Q50 contact for RingConn is support@ringconn.com | RingConn's own route for institutional proposals is business@ringconn.com (sales@ringconn.com for bulk). |
| module-01-wearables/sources.md | 308 | S-EMG-10 cites the npj paper only through a press release | DOI 10.1038/s41746-026-03036-z, published 2026-07-21 (gap finding 6). |

## For the coordinator to check by hand

- **Partner+.** What the $5.99 a month or $69.99 a year in-app purchase unlocks, and whether any export or data feature is paywalled.
- **Terms of Service** (`/pages/terms-of-service`, blocked by robots.txt): read it in a browser for retention, research use and contracting-entity terms.
- **BMC version of record**: confirm the firmware, 100 Hz and COI wording matches the preprint.
- **Research Square PDF URL**: it is used as a `fetch_url` and may not be permanent.
- **Removed data-security claims**: there is no archive of the pre-rewrite text, so the history rests on the researchers' 2026-10-11 reading.
