# Withings: judgement, 2026-10-10

Inputs: `A.yaml`, `B.yaml`, `gaps.md`, the starter `facts/withings.yaml` (every field unresearched), the profile `module-01-wearables/profiles/withings.md` and `module-01-wearables/comparison-matrix.md`. Output: `facts/withings.yaml`, 47 entries (41 stated, 4 not_public, 2 conflict), 15 watched pages, 125 sources. Every quote re-confirmed "exact" with `quote_probe.py` or the same check inside `weekly.py`. `validate.py --file facts/withings.yaml`: 0 errors, 0 unresearched. `weekly.py --only withings --no-state`: 47 pages, 0 quotes missing, 0 reworded, 0 unreachable.

## Fields where A and B disagreed

| Field | A | B | Decision and reason |
|---|---|---|---|
| subscription_price | $9.95/month only (Withings+ terms) | $9.95/month or $99.50/year (US BeamO shop) | Read three pages. The US store says $99.50/yr three times, including its own Withings+ purchase terms ("99.5€ (or $99.5 or £89.5)"). The Withings+ FAQ (updated 2025-10-14) and the bundle sections of the Withings+ terms say $99.95/yr. Both are Withings' own pages, so status `conflict`, confidence Unclear, with a note that the live store is probably current. Monthly $9.95 agrees everywhere. |
| sampling_rates (raw) | stated: ~25 Hz (24.824), accelerometer up to 100 Hz per overview | conflict between the two pages | Read both pages. The overview says the sensor "samples at 25Hz by default (up to 100Hz)"; the raw-data page gives "about 24.824 Hz" for both sensors. The defaults agree; 100 Hz is a sensor ceiling with no documented API setting. Kept `stated` with a note, matching the profile's own 2026-10-09 reconciliation. |
| program_status | Verified | Corroborated | Corroborated. No page says the program is active; it is inferred from live documentation. Added the gap hunter's observation that the Advanced Research API Integration Guide now 302-redirects (confirmed with curl). |
| program_application | contact forms (research-request page and partner form), Verified | contact plus contract, Corroborated | Merged. All three quotes exact; Verified because each step is stated on a page. |
| fda_clearances, K230812 | Body Scan and BodyScan 2 | scoped to ScanWatch ECG | A is right. The openFDA registration listing for K230812 names "Withings Scan Monitor 2 (Body Scan, wbs08; BodyScan 2, WBS15)". |
| fda_clearances, K201456 product codes | DPS, DQA (oximeter), DXH via listing | DPS only; no SpO2 510(k) found | Both true. The 510(k) record has DPS only; the device listing under K201456 for ScanWatch and ScanWatch 2 carries DQA (oximeter) and DXH. Recorded both, and that no SpO2-specific 510(k) exists under a Withings applicant, against the plans page's SpO2 "FDA/CE cleared" claim. |
| fda_clearances, BP monitors | Transtek K223374 and K240102 listed for BPM Connect, Connect Pro, Pro 2, Vision | not covered | Added from A; listings confirmed in openFDA. K240102 decision date 2024-04-29 read from openFDA. |
| retention_terms | API terms, privacy policy, lapsed Withings+ keeps history | API terms, privacy policy, 10-year inactivity | Merged into one `stated` entry for partners, plus a separate `conflict` entry for inactive-account deletion (gap 6). |
| ai_training_terms | plans page only | plans page only | Agreed. Added a second scope for Withings' own pseudonymised AI use (gap 14). |
| data_residency | BSO France, GCP US, Corroborated | EU hosting, Verified | Corroborated: every source is a vendor statement. Added the GCS Dublin backup from the HDS guarantees table (gap 2). |
| export_routes, user_cap, rate_limits, deprecations | minor wording differences | | Merged; added A's notice-period source and B's 10-user review quote. |
| device_price | Light and Nova quoted from the ScanWatch 2 page | quoted from each product's own page | Used B's per-product pages (all exact). |

## Gap findings

| # | Finding | Decision |
|---|---|---|
| 1 | AFNOR ISO 27001:2022 certificate, ISO 27701 certificate | Accepted. iso27001 is Verified on the certificate (source type `certificate`). AFNOR's online register was not checked. |
| 2 | HDS v2 certificate with Boston site; GCS Dublin backups | Accepted. HDS v2 and Boston quoted exact on the HDS certificate; backup row added to data_residency. |
| 3 | Raw ECG waveform via Heart v2 (ScanWatch and Move ECG 300 Hz, BPM Core 500 Hz); BeamO stethoscope signal | Accepted. The gap hunter could not probe the JS bundle; all four OpenAPI wordings are exact on `developer.withings.com/openapi.yaml`. Plan gating unclear and noted. |
| 4 | Patient Insights on-device questionnaires (BPM Pro 2) | Accepted, recorded under derived_metrics with its own scope (no better field). |
| 5 | Contract SDK and other contract routes | Accepted into export_routes. |
| 6 | Inactive-account deletion, 3 years (French terms, 2026-01-05) vs 10 years (privacy policy) | Accepted as `conflict`. Both quotes exact. The US terms page has no such clause. |
| 7 | Recall Z-1280-2023 and Z-2829-2018 | Accepted. Quotes exact through openFDA (`recall.json?search=cfres_id:198114`), cited against the accessdata recall page id 198114 (the gap hunter gave no record id). openFDA status is "Open, Classified". The gap hunter's "Class II" is not in openFDA's recall or enforcement data, so it was left out of the value. |
| 8 | BPM Pro 2 FDA clearance not under a Withings applicant | Resolved by A's finding: listed under Transtek's K240102. The press release was not used. K121971 added in a note. |
| 9 | Withings+ $99.95/yr (FAQ) | Accepted as one side of the subscription_price conflict. |
| 10a | Change-notice policy | Accepted into deprecations. |
| 10b | Advanced Research API Integration Guide redirects | Accepted as a note on program_status (302 confirmed). No quote possible. |
| 11 | Polling guidance; refresh-token lifetime | Accepted (rate_limits, export_routes). |
| 12 | 10-user cap form | Accepted. |
| 13 | In-app Research Center; Health Solutions partnering; 29 publications in 2025 | Research Center accepted as its own research_program scope. The publication count was not added (not a decision fact). |
| 14 | Withings' own AI use of pseudonymised data | Accepted as a second ai_training_terms scope. |
| 15 | API agreement reserves right to charge | Accepted into api_platform_fees. |

## Profile and matrix statements the record contradicts

| File | Line | Says | Record says |
|---|---|---|---|
| profiles/withings.md | 52 | ECG researcher access "Not mentioned as available through the Raw Data API; a device feature rather than a raw stream" | ECG waveform in microvolts via Heart v2 - Get, ScanWatch 300 Hz, BPM Core 500 Hz (raw_streams, sampling_rates) |
| profiles/withings.md | 76 | "ECG raw waveform: Not mentioned as available" | Same as above |
| profiles/withings.md | 255 | Open question "Is raw ECG waveform available under any agreement?" | Answered: documented in the API reference; plan gating unclear |
| profiles/withings.md | 57 | SpO2 researcher access "Unclear" | SpO2 is a Health Data API biomarker, gated to Advanced Biomarkers per the plans page |
| profiles/withings.md | 103 | Active data collection "None native" | Patient Insights questionnaires on BPM Pro 2 (Advanced Biomarkers) |
| profiles/withings.md | 227, 247 | "No survey/EMA capability"; poor fit for integrated surveys | Same; on-device questionnaires exist on one device |
| profiles/withings.md | 139 | "No device SDK" | Contract SDK for iOS and Android (setup and sync, not device programming) |
| profiles/withings.md | 121, 133, 258 | No retention term published | Inactive-account deletion is published (3 or 10 years, in conflict); API terms say copies may remain |
| profiles/withings.md | 159, 229 | Compliance vendor-stated only; ISO 27001:2017; "No certificate registry entry was checked, so none of these is Verified independently" | AFNOR ISO/IEC 27001:2022 certificate valid 2026-04-22 to 2029-04-21; ISO 27701 and HDS v2 certificates |
| profiles/withings.md | 262 | 2017 vs 2022 ISO conflict open | Resolved in favour of 2022 by the certificate |
| profiles/withings.md | 160 | FDA list of 8 Withings-applicant 510(k)s only | Adds Transtek K223374 and K240102 (BPM Connect, Connect Pro, Pro 2, Vision), the K201456 DQA listing, and recall Z-1280-2023 |
| profiles/withings.md | 166 | "Withings+ membership price was not read" | $9.95/month; annual $99.50 or $99.95 (conflict) |
| profiles/withings.md | 144 | EU (France) or US medical cloud | Also GCS backups in Dublin; HDS v2 Boston site |
| comparison-matrix.md | 105 | ECG "Not in the Raw Data API" | Correct as worded, but ECG waveform is available via Heart v2 |
| comparison-matrix.md | 183 | Surveys "Via DCT partner; Advanced Biomarkers plan lists questionnaires" | On-device Patient Insights on BPM Pro 2 |
| comparison-matrix.md | 226 | Withings+ "price not read" | $9.95/month; annual in conflict |
| comparison-matrix.md | 249 | "ISO 27001:2017 and HDS stated (C)"; FDA list of 8 | ISO 27001:2022 Verified by certificate; Transtek BP clearances and the 2023 recall |
| comparison-matrix.md | 391 | "retention not published" | Inactive-account deletion published, in conflict |

## For the coordinator to check by hand

- The K201456 SpO2 scope: the 510(k) record carries DPS only, while the device listing adds DQA. Read the accessdata page and its summary PDF in a browser to confirm whether SpO2 is in the cleared indications.
- The recall class for Z-1280-2023 on the accessdata recall page (id 198114).
- AFNOR's online certificate register for 2020/86561.8.
- Which inactive-account rule (3 or 10 years) applies to US accounts.
- Whether Heart v2 ECG signal is callable on Start for Free or Enterprise, or only on Advanced Biomarkers.
