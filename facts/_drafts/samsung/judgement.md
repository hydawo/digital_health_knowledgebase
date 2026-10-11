# Samsung: judgement (baseline run, 2026-10-10)

Inputs: `A.yaml`, `B.yaml`, `gaps.md`, the old `facts/samsung.yaml` (all `unresearched`), the profile
`module-01-wearables/profiles/samsung.md` and `module-01-wearables/comparison-matrix.md`. Every quote in the final
record was re-run through `tools/facts/quote_probe.py` on 2026-10-10 and returned `exact`.

Final record: 37 facts (several fields split by `scope`). 26 stated, 10 not_public, 1 unclear, 0 conflict.

## Fields where A and B disagreed

| Field | A | B | Decision and why |
|---|---|---|---|
| research_program | stated, Research Stack only | stated, Research Stack only | Agreed on Research Stack; split into two scoped entries and added a second one for the institutional collaborations and the Alcedis "research platform" from the gap hunter (see below). |
| program_eligibility | stated (Research Stack is Apache-2.0, so anyone) | not_public | **B.** The licence of an open-source tool is not eligibility for a program; what a study team needs to know is who gets SDK partner approval or a collaboration, and that is unpublished. The Apache point is kept in the note. |
| program_application | stated | stated | Merged. Added B's Data SDK process quote, the "developer mode is intended only for testing" quote (found on the Sensor process page; the gap hunter's copy on the Data FAQ was **missing**), and Thryve's "approvals do not transfer". |
| program_status | unclear | unclear | Agreed on unclear; scoped to Research Stack and corrected a shared error (see below). Added a scoped stated entry for the Alcedis platform. |
| developer_program_status | stated | stated | Merged; added the Sensor SDK 1.4.1 release date. |
| academic_pricing | stated (Education Offer Program, 15% off) | not_public | **B.** The education offer is a personal retail promotion for verified students and educators, not research or institutional pricing, and its quote ("plus an extra 15% off") is a weekly-changing promo that would churn the monitor. Kept in the note. |
| api_platform_fees | not_public | not_public (and said the partner agreement was behind sign-in) | Changed to **stated**: no fee is published, but the public partner licence reserves Samsung's right to charge in future (gap finding 2). B was wrong that the agreement is behind sign-in; it is a public page. |
| minimum_commitment | stated (two-year initial term) | not_public | **A.** Opened the agreement: two-year initial term, yearly auto-renewal unless 60 days' notice, Samsung may terminate without cause on 30 business days' notice. B had assumed the agreement was not readable. |
| quote_required | stated "No", Reported | not_public | **A**, raised to Corroborated: device prices are on samsung.com and the SDK is a free download (both quotes exact); "no quote" for volume or the Alcedis platform is not established and is noted. |
| device_price | one entry, Watch9 and Ring | three scoped entries incl. Ultra2 | **B's structure**, all three quotes exact. |
| subscription_price | Corroborated, watch page quote | Verified, Samsung Health app page | **B**: the app page states the app is free directly. |
| history_depth | stated, Corroborated | not_public | **A**, extended with the gap hunter's Health Connect 30-day default (Google docs, exact). The Sensor SDK "live only" part is documented; only the Data SDK lookback is an absence, hence Corroborated. |
| export_routes | one combined entry | three scoped entries | B's scoped structure plus a fourth scope for Health Connect and participant self-export (A's quotes). |
| rate_limits | not_applicable | not_public | **B.** There is no cloud API, but the Data SDK is still an API whose query limits are simply undocumented; not_public is the dated, checkable claim. |
| retention_terms | partner agreement + US consumer notice | consumer notices only (said partner agreement behind sign-in) | **A**, plus B's EU "active user" quote and the gap hunter's clause 4(m) (Samsung may collect information about the partner's service; partner must obtain user consent). |
| ai_training_terms | stated incl. partner-agreement ad/data-mining ban | stated, consumer only | Merged both. |
| deprecations | stated incl. 1.3.0 rename | stated | Merged, plus the "end of service in 2028" newsletter quote (gap 6) and the v1.4.0 Android 16 permission change. |
| dpa | unclear | not_public | **B.** No DPA is published; the agreement's data-protection clauses and "supplemental agreement" hook are recorded in the note. The question asked is whether a DPA is offered, and the dated answer is that none is published. |
| data_residency | Corroborated | Verified | **Verified.** data_residency is not in the schema's self-claim cap, and the source is Samsung's own legal notice describing its own processing. The "without limitation" caveat is in the note. |
| fda_clearances | stated, five records | stated, five records | Agreed. Kept accessdata.fda.gov as `url` and the openFDA query as `fetch_url`. |
| user_cap, academic_vs_commercial, baa, hipaa_statement, gdpr_statement, iso27001, soc2, raw_streams, derived_metrics, sampling_rates | agreed | agreed | Merged best-sourced quotes. |

## Research Stack: dormant or mature, and why program_status stays unclear

Decided deliberately: **unmaintained, not mature; status left `unclear` because Samsung says neither.**

- A shared error in A, B and the coordinator's brief: "the announced 2.0 never shipped" is not right. Samsung's
  release notes page `research/release-notes/v20.html` is titled "Version v 2.0 Beta Release Notes" and documents
  the Sensor SDK integration that the September 2024 SDK Suite release promised for the "forthcoming 2.0 version"
  (quote found on the Samsung Mobile Press copy of the release; news.samsung.com times out for the fetcher). The backend's last commit is "Release v2.0-beta", 2024-10-10. What never
  appeared is a non-beta 2.0.
- GitHub API, 2026-10-10: backend-system, app-sdk and web-portal last pushed 2024-10-24; starter-app 2024-08-20;
  none archived; no published releases.
- A beta that has not been touched in nearly two years, and that depends on fast-moving Android, Wear OS and
  Firebase APIs, is not a mature product, so "dormant" is the fair working description. But a stated status needs
  Samsung's own words, and there are none (no retirement, no support statement; the docs are still live and
  promoted on the developer hub). So `unclear`, with the evidence in the note.

## Gap-hunter findings

| # | Finding | Decision |
|---|---|---|
| 1 | Five FDA records for watch features | **Accepted** (both researchers had them too). K261187 Hearing Aid Feature **kept out of the value**: product code SCR, air-conduction hearing aid software, nothing ties it to a watch or ring. K132148 S HEALTH (2013) noted only. |
| 2 | Licence reserves right to charge; 30 business days' termination without cause | **Accepted**, both quotes exact. Moved api_platform_fees to stated and added termination to minimum_commitment. |
| 3 | Samsung may collect information about the service; partner must obtain user consent; research is a licensed purpose; no public statements about the T&C | **Accepted** into retention_terms and academic_vs_commercial notes. The press-statement clause is about the T&C, not research results, so it is not recorded as a publication restriction. |
| 4a | Alcedis/Huma "Samsung's research platform", June 2026 | **Accepted** at Corroborated (research_program) and Reported (program_status). LEDinside repost and TechRepublic quotes exact. The original news.samsung.com page responds to curl but times out for the fetcher, so it is named in a note, not cited. Nothing published says how to get in or what it costs. |
| 4b | Open Innovation Initiative (SDC23, 2023) | **Accepted**, Samsung Mobile Press quote exact; also on Samsung's partnerships page. |
| 5 | UCSF Neuroscape, MGH GLP-1, Stanford sleep apnoea studies | **Accepted** as evidence of the invitation route (all quotes exact). These are deployments, not a program anyone can join. Module 3 candidates once results publish. |
| 6 | Android SDK deprecated 31 July 2025, end of service 2028 | **Accepted** (newsletter quote exact). |
| 7 | Data SDK needs its own partner approval; legacy approvals do not transfer | **Accepted**. Samsung's process page quote exact; Thryve quote exact. The "developer mode is intended only for testing" quote is **missing** on the Data FAQ where the gap hunter placed it; the same words are exact on the Sensor process page, cited there instead. |
| 8 | Data SDK version, non-Samsung phones, Galaxy Ring as source, wellness-only | **Accepted**, all exact. |
| 9 | Consumer AI-training consent (July 2026) | **Accepted**; Samsung's own static notice was found (content.samsungknowledge.com), so the vendor text is primary and press is secondary. |
| 10 | Sensor SDK 1.4.0/1.4.1, Android 16 `READ_ADDITIONAL_HEALTH_DATA` | **Accepted**, all exact. The release-note table lists BIA, ECG, EDA, MF-BIA and both PPG trackers under the Samsung permission; heart rate and SpO2 use standard Android HealthPermissions. |
| 11 | EU ECG App IFU carries the medical-device symbol | **Accepted as a note** under fda_clearances (no CE field in the schema). MDR class not established. |
| 12 | Terra privileged partnership; Fitrockr Samsung integration | Terra **accepted as a note** under export_routes (exact). Fitrockr **not used**: page date unconfirmed and the probe did not complete. |
| 13 | Health Connect 30-day default history | **Accepted** into history_depth. |
| 14 | Xealth, Medicare App Library, GalaxyPPG | **Not added**: Xealth unquoted; the other two are not research-access facts. |

## Statements in the profile or matrix that the record contradicts

Profile: `module-01-wearables/profiles/samsung.md`. Matrix: `module-01-wearables/comparison-matrix.md`.

| File, line | Says | Record says |
|---|---|---|
| Profile 20, Quick Facts "Pricing model" | "no documented SDK fee" | True today, but the licence reserves Samsung's right to charge for the SDK in future (api_platform_fees). |
| Profile 148 and 176, Pricing and Strengths | "No SDK licence fee is documented. The gate is partner registration for distribution, not payment"; "No subscription, no API fee" | Same reservation; also Samsung may terminate the agreement without cause on 30 business days' notice (minimum_commitment). |
| Profile 151, Pricing | "Not established: whether the Samsung Partner Program imposes any commercial terms on academic applicants" | The public agreement applies to everyone: two-year term, yearly renewal, termination without cause, future-fee reservation. |
| Profile 103 and 143, Research program / Privacy | "no Samsung cloud copy, no rate limit and no Samsung retention term, because no Samsung server is in the path"; "the study's data does not flow into Samsung's consumer cloud" | Sensor data does not, but the licence lets Samsung collect information about the service and its use, and the partner must get users' consent for that (retention_terms). Belongs in consent forms. |
| Profile 145, Privacy | Publication restrictions "not found ... the agreement was not read clause by clause" | The agreement bars public statements about the T&C without approval; that does not bar publishing results. |
| Profile 102, Research program | "No separate academic programme or academic tier is published" | Still true for open application, but the profile omits Samsung's invitation route: the Open Innovation Initiative, named studies (Stanford, Tulane/Huma, UCSF, MGH) and the June 2026 Alcedis research platform (research_program). |
| Profile 25, 90, 105 | "Research Stack 2.0 Beta (September 2024)"; "Research Stack appears dormant" | Dormant is consistent; the 2.0 Beta release commit is dated 2024-10-10 rather than September. Minor. |
| Profile 82 and 194; Open Questions 220 | Galaxy Ring "raw-data access story is not established"; "integrated through the Data SDK" | Ring processed data via the Data SDK is now Verified (Data SDK overview and FAQ name Galaxy Ring as a source); no raw route exists in either SDK. |
| Profile 112, Data Access table | Data SDK row "Processed metrics, multi-source" with no gate | The Data SDK needs its own partner approval to distribute, and legacy approvals do not carry over (program_application). Steps are aggregate-only. |
| Profile 146 and 157, Participant Experience | Permissions described only generally | Apps targeting Android 16 need Samsung's READ_ADDITIONAL_HEALTH_DATA permission for ECG, EDA, PPG and BIA trackers (raw_streams). |
| Profile, whole file | No FDA content; no mention of the deprecated Samsung Health SDK for Android | Five FDA authorisations (fda_clearances); Android SDK deprecated 31 July 2025, end of service 2028 (deprecations). |
| Profile, whole file | No AI-training content | Samsung Health consumer data can be used for AI training with opt-in consent since July 2026 (ai_training_terms); relevant to Data SDK and Health Connect routes. |
| Profile 25 (SDK "v1.4.1") | Version without date | v1.4.1 dated 20 August 2025; no release since. |
| Matrix 201 | Samsung phone requirement "Galaxy owners only" | The Data SDK runs on non-Samsung Android phones too (Samsung Health 6.30.2+); the watch component still needs a Galaxy Watch. |
| Matrix 221 and 389 | "No SDK fee documented" / "No fee documented" | Future-fee reservation, as above. |
| Matrix 247 | Regulatory column "Not itemised in the profile"; "no Samsung server in the Sensor SDK path" | Five FDA records; Samsung may collect service-use information under the licence. |
| Matrix 371 | Samsung Sensor SDK listed as free of retention or ML-training limits ("no vendor in the path") | Still no ML-training limit in the licence, but Samsung's information-collection clause and the consumer AI-training consent (Data SDK route) should be footnoted. |
| Matrix 389 | "No academic tier"; "Research Stack dormant since 24 Oct 2024" | Add the invitation/CRO route; dormant status consistent. |

## For the coordinator to check by hand

1. news.samsung.com Alcedis release (URL in the research_program note): confirm the date (24 June 2026) and wording
   in a browser; if it loads for the fetcher later, swap it in for LEDinside and raise to Verified.
2. The content.samsungknowledge.com fetch_urls carry version numbers (pp_us 18.0.1, pp_eugdpr 18.0.0,
   shd_gen_ai_us 1.0.0). They will 404 when Samsung republishes; re-find them from the network log at
   samsunghealth.com/privacy.
3. The EU ECG App IFU PDF (gap 11) for MDR class and notified body, and EUDAMED, if CE status is wanted.
4. Developer-forum reports of paused or refused academic partner intake (404 to the fetcher).
