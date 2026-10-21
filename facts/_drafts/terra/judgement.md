# Judgement: terra (2026-10-21)

Inputs: A.yaml, B.yaml, gaps.md (all 2026-10-11), the coordinator's eleven points, and the live pages
re-read on 2026-10-21. Final record: `facts/terra.yaml`, 33 facts (27 stated, 3 not_public,
2 not_applicable, 1 conflict), 15 watched pages. Every quote returned "exact" from
`quote_probe.py`. `validate.py --file facts/terra.yaml`: 0 errors, 0 unresearched.
`weekly.py --only terra --no-state`: 0 quotes missing, 0 reworded, 0 dead links.

## Things that changed after the drafts were written

1. **Garmin credentials (coordinator point 4 does not hold).** The live Garmin integration page now
   reads "You supply your own Garmin app credentials . Apply at developerportal.garmin.com". The
   Wayback snapshot of 2026-10-14 still reads "Terra manages the Garmin API credentials, so there is
   nothing to register" (the gap hunter's quote). So the page changed between 2026-10-14 and
   2026-10-21. Recorded under `developer_program_status` (scope Garmin through Terra) with both
   quotes, and a note that a new customer may have no Garmin route while Garmin's own programme
   takes no applications. Whether existing customers keep Terra-managed credentials is not stated.
2. **Integration Partner Terms rewritten 2026-10-12.** Draft A's quote ("Terra may use de-identified
   and/or aggregated data for internal analytics, research, AI/ML development, and product
   improvement...") is no longer on the page. The page is now "Integration Onboarding Terms" and
   clause 8.3 says Terra may use De-Identified Data "for any lawful purpose". Recorded the new clause;
   A's quote dropped.
3. **Google Health API onboarding.** Per the coordinator, Google's About page no longer says "not
   onboarding new projects" and `facts/fitbit-google.yaml` now says apparently open again. The Terra
   record does not state that Google is closed.

## Fields where A and B disagreed

| Field | A | B | Decision |
|---|---|---|---|
| research_program | stated (accelerator is nearest route) | not_public | stated, Corroborated. The accelerator FAQ explicitly admits research projects, which is a documented fact; the absence of an academic programme is noted as a search result. |
| program_eligibility, program_application, program_status | stated (accelerator) | not_applicable | stated with scope "Startup Accelerator". It is the only route a research team can use, and the page addresses research projects directly. B's "not aimed at academic groups" is contradicted by the FAQ. Added the card requirement from the gap hunt. |
| academic_vs_commercial | stated (no tier; accelerator credit requirement) | not_public | stated, Verified. Combined: clause 1.2(v) (coordinator point 10, quoted exactly), the development-account evaluation-only clause (point 5), the accelerator credit condition, and B's non-profit forum reply. |
| academic_pricing | stated (no discount; accelerator) | not_public | not_public, Corroborated. "No academic discount" is an absence, so not_public fits the schema better; the accelerator is cross-referenced in the note. |
| api_platform_fees | Quick Start, events, overage, streaming | same plus add-on list | Merged. Kept Graph API and streaming credits; dropped B's Health Scores/Lab Reports "$499 each" line because it had no quote. |
| minimum_commitment | 60-day annual notice, 30-day guarantee | upfront annual, liable for period, spike protection | Merged A's notice clause and B's upfront clause. Spike protection dropped (no quote). |
| sampling_rates | device-set, Huawei, streaming | adds 5 to 10 minute polling, Android SDK 8-hour schedule | Kept polling (quote confirmed on the non-.md page). Dropped the SDK schedule (not re-probed; low value). |
| rate_limits | conflict, Unclear | conflict, Verified | conflict, Unclear. Both sources read: the reference gives 1,825 days per request and 6,000 requested days per user per hour; the environments page still says no REST rate limits. Confidence cannot be Verified when the vendor contradicts itself. Also noted the reference calls the window "rolling" in its table and fixed UTC hours in its FAQ. |
| retention_terms | stated | stated, with exception list | Merged; added the Enterprise "Enable data storage" line from the gap hunt. Kept B's note that the "functioning connection" exception blurs the six-month cap. |
| ai_training_terms | stated, Corroborated, partner AI/ML clause | unclear | stated, Verified. A's partner quote is gone (see above). Point 1 is supported by the text: the End User Privacy Policy (last updated 2026-09-24) now includes research and publication; the Wayback snapshots confirm the wording was absent on 2025-10-16 and present on 2026-02-24. The value says plainly that no clause names AI training. The npj paper is in the note as context. |
| deprecations | Google Fit, Peloton/Technogym, JS SDK, base URL | adds fitbit_v2 rename, Biostrap | Merged; added the Fitbit-to-Google migration doc (Fitbit connection runs on the legacy Web API). |
| export_routes | destinations, SDKs | adds FIT/FHIR, Avengers app | Merged; Avengers app kept in the note only, since its source is a forum reply and no App Store listing exists. |
| iso27001 | not_public, Verified | not_public, Corroborated | Corroborated. The Vanta trust centre could not be read, so the search is incomplete. |
| data_residency | Verified, UK + NL | Corroborated, UK, subprocessors | Verified, merged: DPA (UK and Netherlands), privacy policy, subprocessor hosting (US, UK, EU), Enterprise dedicated instance. |
| fda_clearances | three openFDA queries | two | Used B's encoded URLs plus A's PMA query; not_public, Verified. retrieved left at 2026-10-11, as those queries were not re-run. |

## Coordinator points

1. Research use: recorded under retention_terms and ai_training_terms as above. Exact quotes and Wayback dating confirmed.
2. Rate limits: conflict (see table).
3. Google Health: Terra's docs say "Terra manages the credentials, so there is no Google app for you to register" for the `GOOGLE_HEALTH` connection (Fitbit-to-Google migration help article). This is the Google Health API connection, not the old Fitbit Web API. Terra does not say whether its own Google project has passed restricted-scope review and CASA, or whether a user cap applies. Recorded under developer_program_status (scope Google Health and Fitbit through Terra), Verified as to what Terra says.
4. Garmin: contradicted by the live page; see above.
5. Pricing: confirmed and recorded (api_platform_fees, user_cap, academic_vs_commercial, baa).
6. Accelerator: confirmed (up to $100,000, research eligible if Terra credited).
7. Compliance: capped at Corroborated; Vanta not read; no ISO 27001.
8. Subprocessors: Anthropic and OpenAI, anonymised end-user data, opt-out; in ai_training_terms and data_residency.
9. Smart Fill: confirmed in the August changelog; the blog calls the same feature "health context". In derived_metrics.
10. Clause 1.2(v): quoted exactly: "(v) publicly disseminate information from any source regarding the performance of the Services or Output". In academic_vs_commercial.
11. Residency: confirmed.

## Gap findings

| # | Finding | Decision |
|---|---|---|
| 1 | End-user data used for Terra's own research; policy change dated by Wayback | Accepted (ai_training_terms, retention_terms). All quotes exact. |
| 2 | Terra Research and the npj paper | Accepted as context in notes (research_program, ai_training_terms). Paper quotes not added as sources, since the paper documents Terra's practice, not a term. |
| 3 | Accelerator is the only research route | Accepted. Acceptance rate: page says 0.8%, not the 1.8% search summary. |
| 4 | Fitbit and Google Health credentials | Accepted and resolved with the Google Health docs (point 3). |
| 5 | Terra holds Garmin credentials | Rejected as current fact: the page changed after the gap hunt. Kept as the Wayback history in the Garmin fact. |
| 6 | Bring-your-own credentials for WHOOP, Strava, Dexcom, Samsung | Accepted for WHOOP, Strava, Dexcom (Dexcom from the docs); Huawei added from docs listing. Samsung and the Oura quote were not re-probed and are not in the record. |
| 7 | Retention two days, six months max, storage on Enterprise | Accepted. |
| 8 | DPA, subprocessors, residency | Accepted. |
| 9 | BAA Enterprise only, self-claims, Vanta | Accepted. The gap hunter said "cap at Reported"; the schema cap is Corroborated, used here. |
| 10 | Avengers iOS app | Note only (forum source, no store listing). |
| 11 | Health context imputation | Accepted (derived_metrics). |
| 12 | Provider rate limits shared across users | Accepted (rate_limits). The coverage-endpoint month cap quote was not used; it concerns a different endpoint. |
| 13 | Development accounts evaluation-only; raw data belongs to end user | Accepted (academic_vs_commercial). |
| 14 | Dedicated regional instance | Accepted (data_residency). |

## Statements in the profile, matrix and README that the record contradicts

| File | Line | Says | Record says |
|---|---|---|---|
| module-01-wearables/profiles/data-intermediaries.md | 162 | Intermediaries "add a third-party data processor to the compliance surface" (Terra framed only as a processor) | Terra also uses end-user data for its own statistical, scientific or market research and publication, keeps de-identified derivatives without a time limit, and has published a paper on that pool (ai_training_terms) |
| module-01-wearables/profiles/data-intermediaries.md | 20 | For Fitbit, unified APIs (Thryve, Validic) need each customer's own Google Cloud project, verified app and CASA; Google "not onboarding new projects" | Correct as written for Thryve and Validic, but Terra's docs say Terra manages the Google Health credentials and the customer registers no Google app. The "not onboarding" clause is stale per the coordinator |
| module-01-wearables/profiles/data-intermediaries.md | 212 | "Unified APIs need the customer's own Google Cloud project, verified app and CASA (Corroborated)" | Not true of Terra by its own docs (developer_program_status, Google Health scope) |
| module-01-wearables/README.md | 125 | "Unified APIs need the study's own Google Cloud project, verified app and CASA." | Same contradiction for Terra |
| module-01-wearables/comparison-matrix.md | 365 | "Unified APIs need the study's own Google Cloud project and CASA (C)" | Same contradiction for Terra |
| module-01-wearables/comparison-matrix.md | 50 | "Unified APIs need the customer's own project (C)" | Same contradiction for Terra |
| module-01-wearables/profiles/data-intermediaries.md | 166 | Terra pricing and BAA | Consistent. Missing: development accounts are evaluation-only, 50-user cap in test and staging, and the accelerator as the only research-eligible offer |
| module-01-wearables/profiles/data-intermediaries.md | 207 | Labfront and Fitrockr as the Garmin route while Garmin is closed | Not contradicted. Do not add Terra here: its Garmin page now requires the customer's own Garmin credentials |

The "not onboarding new projects" statements at README.md 72, 122, 182 and comparison-matrix.md 34,
50, 106, 168, 390 belong to the Fitbit/Google record, not Terra, and are listed only because the
coordinator says that record changed.

## Check by hand

- Ask Terra: (a) does its shared Google Health project have restricted-scope approval and CASA, and is
  there a user cap; (b) do existing customers keep Terra-managed Garmin credentials, and can a new
  customer connect Garmin users at all; (c) can a customer or participant opt out of Terra's own
  research use; (d) does clause 1.2(v) cover a methods paper reporting data completeness or latency.
- The Vanta trust centre (SOC 2 report, GDPR assessment) needs a person in a browser.
