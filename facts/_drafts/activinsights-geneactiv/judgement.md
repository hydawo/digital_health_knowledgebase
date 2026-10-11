# Activinsights (GENEActiv): judgement, 2026-10-11

Inputs: `A.yaml`, `B.yaml`, `gaps.md`, the starter `facts/activinsights-geneactiv.yaml` (every field unresearched), the profile `module-01-wearables/profiles/axivity-geneactiv.md` and `module-01-wearables/comparison-matrix.md`. Output: `facts/activinsights-geneactiv.yaml`, 42 entries (28 stated, 11 not_public, 1 conflict, 1 unclear, 1 not_applicable), 11 watched pages, 40 distinct cited URLs (29 on activinsights.com). Every quote re-confirmed "exact" with the `quote_probe.py` matcher on 2026-10-11. `validate.py --file`: 0 errors, 0 unresearched. `weekly.py --only activinsights-geneactiv --no-state`: 40 pages, 0 quotes missing, 0 reworded, 0 unreachable.

**Scoping.** Facts are split per product wherever GENEActiv and the ActivInsights Band or cloud platform differ: user_cap, device_price, subscription_price, api_platform_fees, raw_streams, derived_metrics, sampling_rates, history_depth, export_routes, fda_clearances, data_residency. The GENEActiv scope describes the USB-cradle route, and notes where uploading .bin files to the Study Management Hub or Advanced Sleep Toolkit puts data in the vendor cloud.

## Fields where A and B disagreed

| Field | A | B | Decision and reason |
|---|---|---|---|
| research_program | stated, no named program, services, Verified | not_public, Unclear | Stated. The services page says it serves academic research; what is missing is a named program, which goes in the value and note. Added the Advanced Sleep Toolkit (gap 7). |
| program_eligibility, program_application | stated (who devices are sold to; quote form and demo request) | not_applicable | A. Both are stated on vendor pages and tell a study team how to get in. All quotes exact. |
| program_status | stated Active, Verified | not_applicable | A's status, but Corroborated: "active" is inferred from 2026 releases and the US office, not stated. Swapped in the App Store 1.3/Hub release note as a source. |
| developer_program_status | Verified | Corroborated | Verified; the SDK-under-licence statement is direct. Noted the "open SDKs" (product page) vs "under licence" (apps page) wording. |
| user_cap | stated, Advanced Sleep Toolkit, 10 participants | not_applicable | Both, as two scopes. |
| academic_vs_commercial | non-commercial R Markdown licence | adds FAQ positioning | Merged; added the "restricted to the Activinsights ecosystem" quote (gap 9). Added a second scoped entry for terms-of-sale clause 24 (see below). |
| device_price | not_public, Fibion figure in note only | stated, Reported, Fibion quotes | Stated, **Reported**, scoped GENEActiv, per the coordinator's cap. Both Fibion quotes exact, but they disagree on what the range covers (0.5 GB only vs 0.5 vs 1.0 GB) and current devices have 2.0 GB, so the figure may be stale. Dropped the forum-sourced USD 260 to a note. Band price separate, not_public. |
| subscription_price (Band) | stated, one year included | not_public | A. Quote exact; added the annual-renewal quote. |
| api_platform_fees | two scopes (toolkits free; API/SDK/Hub not public) | one not_public | A's structure. |
| raw_streams (Band) | stated, behavioural only, Verified | unclear (API page lists raw data) | Stated, **Corroborated**. The privacy notice and comparison sheet describe behavioural events only; the API page's "Raw data" is a platform-wide list that fits GENEActiv uploads. B's doubt kept in the note. |
| sampling_rates (Band) | stated "no rate published" | not_public | not_public; a value that says "not published" is not a stated fact. |
| sampling_rates / history_depth (GENEActiv durations) | durations in a sampling_rates note; history_depth stated at 60 days | history_depth conflict (product sheet vs FAQ) | **Conflict** in history_depth, three ways. I read the IFU Rev.010 per-version table myself: v1.1 gives 7 days at 100 Hz and 30 at 20 Hz (matching the FAQ exactly), and v1.2/1.3 give 14 at 100 Hz, 44 at 20 Hz and 56 at 10 Hz. The product sheet and the IFU's own spec table say 60 days at 20 Hz, which the IFU's table contradicts. Note says: plan on 44 days at 20 Hz until the vendor confirms. Neither researcher had found the 44-day row. The IFU also has an editorial comment left in its "Duration of use 14 to 60 days" line, and the comparison sheet says 1 Gb, about 3 weeks. |
| rate_limits | Verified | Unclear | not_public, Verified (precedent: 50 of 61 not_public entries in other records are Verified). The roughly five-hour adherence sync goes in export_routes, with a pointer here, because it is a device schedule, not an API limit (point 5). |
| ai_training_terms | unclear | not_public | not_public. No AI term exists in any notice or terms; the research-use clause is a source and the note explains the ambiguity. |
| baa, dpa, hipaa_statement, soc2 | not_public Verified | not_public Unclear | not_public, Verified, as above. DPA note gets the Coelition processor wording (gap 14), both quotes exact. |
| iso27001 | unclear (found the expired certificate) | stated, Corroborated (did not find it) | **unclear, Unclear.** See point 1 below. |
| fda_clearances | stated, Verified, openFDA URL as url | stated, Verified, accessdata URL with fetch_url | Same facts. Used B's citation form (accessdata as url, openFDA as fetch_url, per README). Added the Band as a separate not_public scope. |
| data_residency | Verified | Corroborated | Corroborated, since every source is the vendor's own statement (follows the Withings judge). Split into a cloud scope and a GENEActiv USB scope. |
| deprecations | Verified | Corroborated | Verified; each event is directly stated. Added the GENEActiv 1.3 revision with the macOS App Store release note. |

## The coordinator's points

1. **ISO 27001.** I opened the certificate PDF and read it by eye. It says British Assessment Bureau certificate 239005, Activinsights Ltd, BS EN ISO/IEC 27001:2017, UKAS 8289, initial certification and latest issue 16 June 2023, expiry 31 October 2025. The PDF has no text layer, so `quote_probe` cannot match anything on it. I put no quote on the certificate source and recorded what it says in the `note`, labelled as read by eye. The status is `unclear` with confidence `Unclear`. The only independent evidence lapsed almost a year ago, the site still claims certification on the company page, the sleep toolkit page and a 2025 press release (quoted as evidence of the claim, not of its truth), and a renewed certificate could exist unpublished. A search of the WordPress media library for "27001" and "certificate" found no other certificate. The server's Last-Modified header on the old PDF is 2026-08-05, but its content still shows the 2025 expiry. UKAS CertCheck was not used. The weekly monitor can only watch this PDF's link and fingerprint. A replaced certificate under the same URL would show as "page changed".
2. **FDA.** Verified from openFDA: listed, not cleared, under IKK (21 CFR 890.1925, class 2, submission type 4 = 510(k) exempt), registration 3014083954, owner/operator 10056642, listed 2018-01-04. 510(k) searches return nothing. The IFU's 882.1400 and 882.5050 Class II claim and the web page's Class I (an EU MDD class) are quoted as vendor statements and explained in the note. One inference is labelled as such: under 882.5050, openFDA's LEL "Device, Sleep Assessment" code needs a 510(k), so the IKK listing does not cover a sleep-assessment claim.
3. **Recording duration.** Settled as a conflict, with the version explanation above.
4. **Band and cloud vs GENEActiv USB.** Scoped per product as listed above. The Study Management Hub, Device Manager, Azure APIs and the Advanced Sleep Toolkit (free to 10 participants) are all in.
5. **Bluetooth adherence about every five hours.** In export_routes (GENEActiv), quote exact, with the Bluetooth 5 requirement and iOS limited to adherence data. Also in raw_streams.
6. **Terms of sale clause 24.** Included under `academic_vs_commercial`, scope "Terms of sale, all customers", Verified. The PDF is two-column, and the extracted text breaks the clause at "operation or", so the exact quote ends there. The full clause, from the layout text, ends "use of the Product." The schema has no field for publication terms, so the coordinator may want to add one.
7. **Website terms vs robots.txt.** `https://activinsights.com/website-terms-of-service/` says (exact on the page): "You must not conduct any systematic or automated data collection activities (including without limitation scraping, data mining, data extraction and data harvesting) on or in relation to our website without our express written consent." `robots.txt` is the Yoast default, `User-agent: * Disallow:`, so it allows everything. The weekly monitor honours robots.txt, so it will fetch this site every Monday: 29 distinct activinsights.com URLs (cited sources plus watched pages), not just the 11 watched pages. That is low-volume and paced, but it is automated collection that the terms forbid without written consent. Options for the coordinator: (a) ask Activinsights for written consent; (b) exclude activinsights.com from the automated fetch and move its facts to a manual re-check on their `recheck_by` dates; (c) accept the risk. I kept the watch list at 11 pages either way. The terms page is cited only as a no-quote source under ai_training_terms.
8. **Fibion price.** Reported, as above.

## Gap findings

| # | Finding | Decision |
|---|---|---|
| 1 | GENEActiv 1.3 Bluetooth adherence | Accepted (raw_streams, export_routes, deprecations). IFU and App Store quotes exact. |
| 2 | Azure cloud platform with APIs | Accepted (export_routes, data_residency). |
| 3 | Study Management Hub and Device Manager | Accepted (program_application, export_routes, api_platform_fees). |
| 4 | ActivInsights Band | Accepted, as separate scopes throughout. |
| 5 | FDA IKK listing | Accepted (fda_clearances). |
| 6 | Expired ISO certificate | Accepted (iso27001, point 1). |
| 7 | Advanced Sleep Toolkit, free to 10 | Accepted (research_program, user_cap, api_platform_fees). |
| 8 | Actigraphy Sleep Toolkit, AWD conversion, Actiwatch replacement | Accepted (subscription_price, api_platform_fees, export_routes, deprecations note). |
| 9 | Non-commercial R Markdown licence | Accepted (academic_vs_commercial). |
| 10 | Duration table | Accepted, and extended. The gap hunter's 44 and 56 days for v1.2/1.3 are right. It is the basis of the conflict. |
| 11 | Device lifetime 50 cycles or 2 years | Accepted into device_price (GENEActiv), quote exact. |
| 12 | Fibion price | Accepted as Reported. |
| 13 | US pricing held despite tariffs | Note only (device_price). It is a 2025 marketing line with no figure. |
| 14 | Privacy notices, GB, Coelition processing | Accepted (data_residency, dpa, retention_terms). |
| 15 | Warranty and recycling credit | Note only (device_price, academic_pricing). |
| 16 | GGIRread light calibration for v1.2+ | Accepted into raw_streams, release note quote exact. |
| 17 | DiMe paediatric collaboration | Rejected: not a decision fact for access, price, terms or compliance. |

## Profile and matrix statements the record contradicts

| File | Line | Says | Record says |
|---|---|---|---|
| profiles/axivity-geneactiv.md | 12 | Hosting "None ... No cloud, no account" | True for USB-only GENEActiv; Activinsights runs an Azure cloud with APIs, a Study Management Hub and the Band |
| profiles/axivity-geneactiv.md | 45, 50 | Temperature and light researcher access "Unclear" | Raw light and temperature in the .bin file; temperature at least every 30 s; light needs GGIRread 1.0.11+ calibration for v1.2+ |
| profiles/axivity-geneactiv.md | 65 | "no vendor-derived metrics whatsoever" | Vendor offers 150+ measures as a service, epoch summaries and Sleep Toolkit scoring; Band computes metrics on the device |
| profiles/axivity-geneactiv.md | 88 | Study management "None from the vendor" | Study Management Hub with real-time device and participant status and adherence (demo by request) |
| profiles/axivity-geneactiv.md | 92 | GENEActiv export is `.bin` only | Also raw CSV, epoch CSV, epoch AWD; Bluetooth adherence on v1.3; optional cloud upload |
| profiles/axivity-geneactiv.md | 93 | "No API, no cloud ... no retention policy" | Cloud APIs exist; privacy notices set a 10-year review retention period |
| profiles/axivity-geneactiv.md | 98 | "No device API" | SDKs under licence (GENEActiv SDK named in the IFU) |
| profiles/axivity-geneactiv.md | 107, 193 | No official GENEActiv duration table (Unclear) | IFU Rev.010 has one; vendor documents conflict (60 vs 44 days at 20 Hz; FAQ matches v1.1) |
| profiles/axivity-geneactiv.md | 110 to 111 | "No app, no phone, no account, no sync" | True for v1.1/1.2 USB use; v1.3 syncs adherence data by Bluetooth roughly every five hours |
| profiles/axivity-geneactiv.md | 118 to 122 | "No third-party data processor exists", no BAA needed, GDPR trivial | True only if no data go to Activinsights; Hub, Device Manager and Advanced Sleep Toolkit uploads make it a processor; no BAA, HIPAA statement or DPA is published |
| profiles/axivity-geneactiv.md | 127 | No account, API, user cap, retention rule or data-use terms | Advanced Sleep Toolkit cap of 10 participants; R Markdown tools non-commercial only; terms of sale clause 24 restricts publishing material about the product's operation or use without consent |
| profiles/axivity-geneactiv.md | 161 to 162 | "No adherence monitoring is possible during the wear period" | Possible on GENEActiv 1.3 |
| profiles/axivity-geneactiv.md | 30, 195 | FDA status absent; MDD Class I only | FDA listed under IKK, class 2, 510(k) exempt; IFU says EU MDR Class IIa and FDA Class II under 882.1400/882.5050 |
| profiles/axivity-geneactiv.md | (none) | ISO 27001 not mentioned | Only published certificate expired 2025-10-31; status unclear |
| comparison-matrix.md | 54 | "USB download. No cloud, no API, no account"; study management "None" | As above for profile lines 12, 88, 93 |
| comparison-matrix.md | 116 | "GENEActiv raw, rate not in the profile" | 10 to 100 Hz, +/- 8 g, 12 bit |
| comparison-matrix.md | 192 | Adherence "Impossible during wear" | Possible on GENEActiv 1.3 |
| comparison-matrix.md | 214 | GENEActiv "up to 2 months" | 14 days at 100 Hz; 44 (or 60, in conflict) at 20 Hz |
| comparison-matrix.md | 235, 402 | GENEActiv "quote"; no platform fee | Still quote only (a competitor reports GBP 425 to 510); cloud services and SDK priced on request |
| comparison-matrix.md | 259 | "N/A, no processor exists"; GDPR "Trivial" | Processor exists when cloud services are used |

## For the coordinator to check by hand

- A current ISO 27001 certificate: ask Activinsights, or check UKAS CertCheck in a browser.
- Which GENEActiv recording duration at 20 Hz is right (44 or 60 days): ask the vendor.
- Whether clause 24 is enforced against academic methods papers.
- The website terms vs the weekly monitor (point 7).
- Whether the profile should split GENEActiv out of the Axivity profile, since the two vendors' data paths now differ.
