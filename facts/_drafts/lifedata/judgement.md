# LifeData: judgement (baseline fact run)

Judge run, 2026-10-11, started fresh from `A.yaml`, `B.yaml` and `gaps.md` after an earlier run was cut off.
Output: `facts/lifedata.yaml`.

Final record: 37 entries (34 fields; `subscription_price` and `gdpr_statement` each split into a general and a
scoped entry, `app_availability` split by generation). Status: 27 stated, 8 not_public, 1 conflict, 1
not_applicable. Confidence: 26 Verified, 9 Corroborated, 1 Reported, 1 Unclear. Every quote re-probed "exact"
on 2026-10-11 (19 distinct fetch URLs). `validate.py --file facts/lifedata.yaml`: 0 errors, 0 unresearched.
`weekly.py --only lifedata --no-state`: 24 pages, 0 quotes missing, 0 reworded, 0 dead links. Both ran on the
live repo; the scratch-copy fallback was not needed. Help centres were not opened past their bot check, and
nothing was signed into.

## Coordinator points

1. **DPF.** `quote_probe` reads the registry JSON (`dpfapi.azurewebsites.net/api/participants/6382`) and every
   quote tried was exact. The record cites `https://www.dataprivacyframework.gov/list` as `url` with the JSON as
   `fetch_url`, type `certificate`. `gdpr_statement` is split: the general entry (GDPR processor role,
   compliance claim, DPF and Privacy Shield wording) stays Corroborated; a scoped entry, "Data Privacy Framework
   certification", is Verified, with quotes for the EU-U.S. status and dates, the UK Extension status and dates,
   the 2019 lapse and "Self-Assessment". The CEO's name, email and phone are in the JSON and were deliberately
   not quoted.
2. **Two generations.** `deprecations` kept as `conflict` (A's call): the home page says "Released in 2026", both
   store listings say 2025, and the iTunes lookup gives releaseDate 2025-05-28. Confidence Unclear, as the
   project's scale uses that label for conflicting evidence. The terms' "reasonable advance notice" clause added
   as the fourth source. No shutdown date anywhere. `app_availability` split by scope, with version, minimum iOS
   and download counts confirmed (iTunes lookup: LifeData 1.0.17 of 2026-10-10, iOS 18.0; RealLife Exp 2.8.14 of
   2026-04-06, iOS 13.0; Play: 100+ and 10K+ downloads).
3. **VA prices.** A USAspending API response can be cited with an exact quote for its text fields (award title,
   "ONLY ONE SOURCE-OTHER (FAR 6.302-1 OTHER)", "NOT COMPETED UNDER SAP") but not for amounts, which are numeric
   JSON values that `quote_probe` drops. So: `subscription_price` stays not_public (no published price), plus a
   scoped entry "VA San Diego Healthcare System contracts (USAspending), 2023 to 2029", status stated,
   confidence Reported, quoting the titles, with every dollar figure in the note and the API URLs as
   `fetch_url`. I re-fetched the award and transaction endpoints myself. Two corrections to the brief:
   - 36C26223P0320 ($13,920) is not "2023 to 2024" only. It is four $3,480 actions: 2023-05-25, then options
     on 2024-05-24, 2025-06-01 and 2026-05-04, with a potential end of 2027-05-31. It is a purchase order under
     simplified acquisition (FAR 6.302-5(a)(2)(i)), not a 6.302-1 sole source.
   - 36C26224C0205 also has a $0 modification on 2026-06-09. Base 3,680, option year 1 3,680, funding increase
     3,480 (2025-06-23), option year 2 7,160 (2026-03-19); obligated 18,000, base and all options 25,360.
4. **Play data safety.** Confirmed exact on the details page: "This app may share these data types with third
   parties Device or other IDs" and "Updated on Oct 8, 2026". Recorded as a source and note in `retention_terms`
   (the nearest data-use field, as in the MetricWire record) and noted in the LifeData+ `app_availability` entry.
5. **HIPAA.** `hipaa_statement` stated, Corroborated, with the healthcare-research page ("is HIPAA compliant"),
   the features page's new "Support HIPAA- and GDPR- compliant research workflows", the ePRO page and the
   clinical-research page ("HIPPA"). Both legal documents are listed as checked sources without quotes; searched
   on 2026-10-11, no "HIPAA" in either. `baa` not_public, Verified.
6. **Privacy Shield vs DPF.** Terms "Effective date: December 12, 2014" and privacy policy "Updated: December
   12, 2024" both confirmed on the pages. The Privacy Shield sentence is quoted in the general `gdpr_statement`
   entry and called stale in its note.
7. **Active data only.** `raw_streams` stated, Corroborated (an absence cannot be quoted, and the help centre is
   gated). Added the JAMA Netw Open 2025 paper (PMC12481226) showing a team collected continuous location
   through Google Maps alongside RealLife Exp. GPS once per response is in `raw_streams` and `sampling_rates`.
8. **Retention.** 180 days, 30 days, 12 months, phone-side deletion and US storage all in `retention_terms`
   (Verified, vendor legal). Azure as example host in `hosting_options` and `data_residency`.

## Fields where A and B disagreed

| Field | A | B | Decision and reason |
|---|---|---|---|
| research_program | not_applicable | stated, Verified | stated, Verified, matching the other platform records (Avicenna, m-Path, MetricWire, CARP, mindLAMP all use stated). The value says plainly there is no separate program. |
| program_eligibility | Corroborated | Verified | Verified: the vendor's own page about its own offer. Merged quotes. |
| developer_program_status | not_public, Verified | not_public, Verified | Both agreed; lowered to Corroborated because the help centres could not be read. |
| api_platform_fees | Corroborated | Verified | Verified: three exact vendor-page quotes describe the subscription's scope. The no-API point moved to the note. |
| minimum_commitment | Corroborated | Verified | Corroborated: that six months is the minimum is inferred, and the half-year wording is on one plan card only. Took B's non-refundable quote. |
| raw_streams | Corroborated | Verified | Corroborated: rests on an absence. |
| history_depth | Corroborated | Verified | Verified: the vendor's legal terms are the authority on its own retention. B's 12-month inactivity quote added. |
| ai_training_terms | stated, Verified | not_public | stated, Corroborated. A's quotes are exact and the closest the terms come; B is right that nothing names AI. Corroborated because applying the 2014 clause to model training is interpretation. |
| deprecations | conflict | stated | conflict (see point 2). |
| licence | Corroborated | Verified | Corroborated: closed source is inferred from the terms plus no repositories. |
| dpa | stated, Corroborated | unclear | stated, Corroborated. The terms say they "serve as a contract" between processor and controllers, which is a stated arrangement even if no separate DPA exists. |
| data_residency | Verified | Corroborated | Verified: not a self-claim-capped field; the vendor's policy is the primary source for where it stores data (MetricWire precedent). |
| gdpr_statement | one entry | one entry | Split by scope (point 1). |
| watch list | 13 pages | 13 pages | Merged to 15: pricing, VA award, both legal pages, features, research solutions, home (changelog), healthcare and clinical pages (trust), DPF registry (trust), four store listings, openFDA. Dropped the ePRO and psychological-science pages (quotes still cited where used). |

Only one field ended as `conflict`.

## Gap-hunter findings

| # | Finding | Decision |
|---|---|---|
| 1 | LifeData+ Play listing shares Device or other IDs | Accepted, exact. retention_terms, app_availability. |
| 2 | DPF registry confirmation | Accepted, exact. gdpr_statement (scoped, Verified). |
| 3 | Profile's version table stale | Accepted (iTunes lookup confirms 1.0.17 of 2026-10-10). app_availability; listed below as a profile contradiction. |
| 4 | VA contracts | Accepted with corrections (point 3). subscription_price scoped entry, Reported. |
| 5 | Console PHI and GDPR onboarding fields | Accepted in notes only (baa, hipaa_statement). Both quotes exact on `index-HDLErs9z.js`, but the bundle name is build-specific, so it is not a cited source and would break the weekly check. |
| 6 | Features page "Support HIPAA- and GDPR- compliant" wording | Accepted, exact. hipaa_statement. |
| 7 | App Store privacy labels list audio, health, sensitive info | Accepted in the raw_streams note ("Audio Data" exact). Kept as unclear evidence, not a new stream. |
| 8 | Google Maps Timeline alongside RealLife Exp | Accepted; PMC12481226 quote exact, cited in raw_streams. |
| 9 | Co-founder COI in a Merck-funded RCT | Rejected for the record: no schema field fits. Flag for Module 3 and the profile's evidence section. |
| 10 | NUS study clarified export fields with vendor | Accepted in the export_routes note (not probed as a source). |
| 11 | Wearables run side by side | Accepted in the raw_streams note only. |
| 12 | LifeData+ export as session-type data requests; Azure telemetry | Accepted in the export_routes and developer_program_status notes; build-specific URLs not cited. |
| 13 | Legal pages unchanged since 2024 | Accepted; dates confirmed on the pages themselves rather than the sitemap. |

## Profile and matrix statements the record contradicts

`module-02-digital-phenotyping/profiles/lifedata.md`:

- Line 50: LifeData iOS "v1.0.16 (2026-08-27)". Record: v1.0.17 of 2026-10-10 (line 10 of the same profile already has it).
- Line 51: LifeData Android "updated 2026-07-18". Record: updated Oct 8, 2026.
- Line 317: the LifeData app "shares no data with third parties". Record: Play now declares it may share Device or other IDs with third parties.
- Line 147: RealLife Exp "3.6 on Google Play". The listing read on 2026-10-11 shows 3.5 (127 reviews); not a recorded fact, minor.
- Line 157: DPF held at Corroborated, "a human should confirm the listing". Record: Verified on the registry, status "Active - Re-certification under Review", self-assessed, first certified 2018-05-31, lapse 2019-06-30 to 2019-07-08, next due 2027-04-28.
- Lines 155 to 163: the legal-documents section lists the DPF but not that the 2014 Terms of Use still cite Privacy Shield. Record: both, with dates.
- Line 167: quotes only the older "is HIPAA compliant" wording for the features page. Record: the features page now says "Support HIPAA- and GDPR- compliant research workflows". A PHI setting exists in the LifeData+ console (gap hunter).
- Lines 175, 186 and 325: no price figures exist anywhere and all figures need vendor contact. Record: three VA San Diego awards on USAspending with amounts (Reported, scoped to those awards).
- Line 14: "Last verified 2026-09-02". Record retrieved 2026-10-11.

`module-02-digital-phenotyping/comparison-matrix.md`:

- Line 138 (pricing): "Non-public" with no figures. Record: list price non-public, but VA contract amounts exist (Reported).
- Line 162 (compliance): "Data Privacy Framework self-certification". Record: registry-confirmed (Verified), currently "Re-certification under Review"; GDPR compliance itself still a self-claim.

## For the coordinator to check by hand

- The DPF status reads "Re-certification under Review"; worth a re-look after the next weekly run to see whether it returns to plain Active or lapses.
- The VA dollar figures are copied from numeric API fields and cannot be monitored by the weekly check; only the award titles are watched.
- The help centres (help.lifedatacorp.com, support.lifedatacorp.com) remain unread behind a bot check; any API, BAA or export-schema answer is likely there or with the vendor.
- Gap finding 9 (co-founder equity disclosure in a Merck-funded RCT, PMC12771224) has no home in the record; it belongs in the profile's evidence section and the Module 3 queue.
