# Ultrahuman: judgement, 2026-10-21

Inputs: `A.yaml` and `B.yaml` (both finalised 2026-10-21), `gaps.md` (written 2026-10-11, every quote re-probed today), the starter `facts/ultrahuman.yaml` (all `unresearched`) and `module-01-wearables/profiles/emerging-platforms.md` lines 11 to 45. Output: `facts/ultrahuman.yaml`, 33 entries (24 stated, 7 not_public, 2 unclear, 0 conflict), 89 quotes, 14 watched pages. Every quote matched "exact" with the same fetch and `match_quote` as `quote_probe.py`. `validate.py --file facts/ultrahuman.yaml`: 0 errors, 0 unresearched. `weekly.py --only ultrahuman --no-state`: 35 pages, 0 quotes missing, 0 reworded, 0 dead, 0 check by hand. No scratch copy was needed.

## Coordinator's points

1. **Notion API Agreement.** `quote_probe` gets only "Notion" from the page; both drafts' agreement quotes came back "missing 0.00". I read the full text myself from Notion's `loadPageChunk` page data (a POST, no sign-in) on 2026-10-21. Every agreement quote is now out of the `quote` fields. The page is cited as a quote-less `vendor_legal` source wherever it informs a fact. Its key clauses are in notes, each labelled "read from Notion's page data on 2026-10-21, unverifiable by script". Those clauses are: unpaid as-is Sandbox and Production access, Premium Access, 30 days' notice before fees, storage limited to what is necessary, Ultrahuman owns API data, the bar on research or analysis "against Ultrahuman", reverse engineering, 36-hour breach notice, termination on 30 days' notice, Indian law and Bengaluru courts. Confidence changes: `api_platform_fees` is now Reported, because "unpaid" rests only on Notion (A had Verified, B Corroborated). `retention_terms` and `ai_training_terms` are now Corroborated, because the Ultrahuman-side parts rest on the probe-checkable privacy policy and terms of use while the partner-side parts rest on Notion. `rate_limits`, `deprecations` and `data_residency` keep their confidence, because their main claims rest on checkable sources. The Notion page is left off the watch list, since its fingerprint would only ever be "Notion". **It needs a hand check each recheck cycle.**
2. **Docs chunk.** A stabler route exists. The docs' query-string routes are server-rendered: `?api=daily`, `?api=ppg`, `?api=blood_reports`, `?type=oauth` and `?type=mcp` (the tab ids come from the bundle's own router). A plain fetch of each returns that tab's text. Every docs quote now cites one of these URLs with no `fetch_url`, and the hashed chunk `5898-7e1e79f1b88fcd98.js` is gone from the record. One exception: the S3 `ap-south-1` example URL appears only in the chunk, so it is no longer quoted. It is described in the `data_residency` note as an illustrative sample.
3. **Raw PPG.** Accepted (gap G1). `raw_streams` cites the PPG Recordings API on `?api=ppg`, which calls the data raw and gives the format (gzip NDJSON, pre-signed links that expire after 1 hour), the source (Developer Mode sessions, own recordings only) and a 7-day request window. `sampling_rates` is split by scope: raw PPG is stated as "typically 50 Hz", and daily metrics and other sensors are not_public. This contradicts the profile's "format and rates are not documented".
4. **Self-serve or approval.** Not a conflict once it is scoped. **Personal API token**: stated, Verified, self-serve. The portal says "Generate a token to access your own data" and says the token can reach other users who link via Partner ID, and no approval step is described. **Partner OAuth**: stated, Corroborated. App registration is self-serve in the portal ("Create an OAuth application ..."), and Open Wearables' setup guide does exactly that. Against this, Ultrahuman's September 2025 blog says "approved apps" and "partner onboarding", and Open Wearables' May 2026 blog says "not self-serve". The agreement calls the licensee "the approved Partner" and has Sandbox and Production levels. Decision: creating an app is self-serve, while whether production use or other users' consent needs approval is undocumented. B's conflict is replaced by these two scoped entries.
5. **Ring AIR US ban and prices.** `deprecations` cites the USITC notice (LEO, 21 August 2025) and CBP HQ H354023 (6 March 2026, probed through `rulings.cbp.gov/api/ruling/H354023`), which says Ring PRO is not subject to the order on condition of an importer certification. The 21 October 2025 effective date comes only from TechRadar quoting Ultrahuman ("purchased on or before October 21, 2025"); the CBP text I read does not state it. Kept at Verified for the ban itself, with that sourcing in the note. `device_price` is split into Ring PRO (USD 479, US and global buy pages) and Ring AIR (USD 349 from the pro-vs-air page, GBP 329 UK).
6. **Pulsomics.** The note under `research_program` records what outside institutions can get: study design, cohort access and co-authorship. It also records what they cannot: raw recordings ("limited to the Ultrahuman science team"); published output is aggregated across many users. No collaboration, DSA, IP or cost terms are published. Ethics approval (Medstar Speciality Hospital Ethics Committee) re-probed exact.
7. **Compliance.** `hipaa_statement` (Corroborated) quotes both the privacy policy's "not a Covered Entity ... strive to comply" and the footer's "ISO27001, GDPR, and HIPAA compliant". `iso27001` is Corroborated: certificate on request, none published. `baa`, `dpa` and `soc2` are not_public and Corroborated (self-claim cap). The 27 March 2026 incident notice is quoted in `iso27001` and summarised in the `hipaa_statement` note, with the California AG filing URL.
8. **FDA.** not_public, Verified, following the Oura pattern. The openFDA 510(k) and PMA "no match" queries are cited with `expect_absent: true`, and the Fertile Window listing (LHD, class U, 2024-11-12, owner 10091886, registration 3033531398, no K number) uses an accessdata URL plus an openFDA `fetch_url`. I re-ran six negative searches. On AFib: it is **not marketed in the US**. The PowerPlugs FAQ lists Europe, UK, Turkey and Switzerland and says "We're soon looking to launch in USA, UAE, and India". A's statement that the partners page markets AFib no longer holds; the word does not appear there today. No clearance was found.
9. **Ultrahuman Max.** "Ultrahuman Max. Everything, covered. Starting at $9.99/mo" is quoted exact on `/us/ring-pro/buy/`. Its absence on 2026-10-11 is A's report only, not confirmed by me, and the note says so. The no-subscription-for-data point is quoted from the same page.
10. **Token lifetime.** On `?type=oauth`, "valid for a week" is followed directly by "Expiration: 86400 seconds (1 day)", and the refresh example returns `"expires_in": 86400`. Both are quoted in `export_routes`, and the note advises planning for 1 day.

## Fields where A and B disagreed

| Field | A | B | Decision and reason |
|---|---|---|---|
| research_program | Corroborated (marketing copy) | Verified | Verified for what the pages say; the undocumented partnership terms are spelled out in the note. |
| program_status | Corroborated | Verified | Verified: pages live and CTRI number quoted. Unknown kit intake is in the note. |
| developer_program_status | stated, Verified (both routes open) | conflict, Unclear | Two scoped stated entries (see point 4). |
| user_cap, minimum_commitment | not_public, Unclear | not_public, Verified | not_public, Verified: a dated "not published on these pages" is not uncertain. |
| baa, dpa, soc2 | not_public, Unclear | not_public, Verified | not_public, Corroborated (self-claim cap fields). |
| quote_required | Corroborated | Reported | Corroborated. Several vendor pages route organisational buying through forms with no prices. The note says the conclusion is inferred. |
| api_platform_fees | Verified | Corroborated | Reported (point 1). |
| retention_terms, ai_training_terms | Verified / Corroborated | Verified | Corroborated (point 1). |
| deprecations | Verified, USITC | Corroborated, TechRadar | Verified, with USITC, CBP and TechRadar combined; TechRadar is the source only for the effective date. |
| device_price | One entry | Ring PRO and Ring AIR scopes | B's scopes, A's "Ultrahuman Ring AIR $349" quote. |
| sampling_rates | One entry | PPG and daily-metrics scopes | B's scopes. |
| subscription_price | Includes Max and PowerPlugs | No Max | A's content, with the Max quote probed today. |
| export_routes | Personal token, OAuth, MCP, a week | Adds app sync, aggregators | Merged. Added the Terra quote (gap G13) and the token contradiction (point 10). |
| data_residency | S3 region in note, Indian law quoted | S3 region quoted from chunk | Both quote-less now (point 2 and point 1); privacy-policy quotes carry the fact. |
| watch list | /global/ URLs, Notion, chunk | /us/ URLs, Notion page, chunk | /us/ variants where both exist (same text), docs tab routes instead of chunk, 14 pages. |

## Gap hunter findings

| Finding | Decision | Why |
|---|---|---|
| G1 PPG Recordings API, 50 Hz | Accepted | Quotes exact on `?api=ppg`. |
| G2 Self-serve portal, personal tokens | Accepted, scoped | Quotes exact; see point 4. |
| G3 Pulsomics | Accepted | Quotes exact on `/us/pulsomics/`; Athletech funding quote not needed. |
| G4 API Agreement terms | Accepted as notes only | Text confirmed by my own read of Notion page data; not script-checkable (point 1). |
| G5 ITC ban, CBP ruling | Accepted | CBP quote exact via the API route; TechRadar quote exact. |
| G6 Price and no subscription | Accepted | "Rest assured ..." exact; used the line-item "$ 479" quote rather than "Total $ 479". |
| G7 Vendor accuracy studies | Rejected for the record | No schema field. Relevant to the profile's validation row (below). |
| G8 Footer compliance claim | Accepted | Exact on `/us/partners/`. |
| G9 Security incident | Accepted | Vendor notice quote exact; AG PDF quote exact; malware-laptop attribution not used (press only). |
| G10 FDA listing; AFib not in US | Accepted | openFDA re-run; FAQ quote exact. FibriCheck link left as unverified press. |
| G11 Token lifetime | Accepted | Both quotes exact on `?type=oauth`. |
| G12 MCP server | Accepted | Quotes exact on `?type=mcp`. |
| G13 Terra, Open Wearables | Accepted (export_routes, derived_metrics) | Quotes exact. |
| G14 M2 Live with Abbott Lingo | Rejected | Secondary only, and no field needs it; CGM plans are mentioned only as a separate add-on. |
| G15 UltraWork bulk orders | Accepted (quote_required) | Quote exact. |

## Profile and matrix statements the record contradicts

| File | Line | Says | Record says |
|---|---|---|---|
| module-01-wearables/profiles/emerging-platforms.md | 16 | Product is Ring AIR and M1 CGM patch | Ring AIR is not sold in the US; Ring PRO (USD 479) is the US product (deprecations, device_price). |
| emerging-platforms.md | 17 | "data stream", not "raw"; format and rates not documented | PPG Recordings API is documented as raw PPG, gzip NDJSON, typically 50 Hz (raw_streams, sampling_rates). |
| emerging-platforms.md | 19 | "Two routes"; OAuth for "approved apps", credentials at partner onboarding; tokens "about a week" | Three developer routes (UltraSignal, self-serve personal token, OAuth app registration in the portal) plus MCP; docs give both a week and 86400 seconds (export_routes, developer_program_status). |
| emerging-platforms.md | 21 | Sampling rates not documented | Raw PPG typically 50 Hz; daily-metric resolution still unpublished. |
| emerging-platforms.md | 22 | Pricing not disclosed | Ring PRO USD 479; Ring AIR USD 349 / GBP 329; no subscription for data; API access unpaid per the agreement (device_price, subscription_price, api_platform_fees). |
| emerging-platforms.md | 23, 41 | No validation located | Still true for independent PSG validation, but vendor-run accuracy studies exist (gap G7, outside the record). |
| emerging-platforms.md | 31 to 35 | No academic program; no retention, AI-training or data-sharing terms read | Pulsomics collaboration route exists (terms not public); API Agreement sets storage, ownership, redistribution and research-against-Ultrahuman terms (research_program, retention_terms, ai_training_terms). |
| emerging-platforms.md | 42 | Sampling rates undocumented, pricing unknown | As above. |
| module-01-wearables/comparison-matrix.md | 61 | UltraSignal or Partner API (OAuth for approved apps) | Adds self-serve personal token route. |
| comparison-matrix.md | 116 | PPG "raw format and rates undocumented" | Documented: raw, NDJSON, ~50 Hz, own recordings only. |
| comparison-matrix.md | 149 | Raw PPG resolution "Not published"; access "not disclosed" | ~50 Hz; access via Developer Mode and the PPG Recordings API. |
| comparison-matrix.md | 178 | Tokens last about a week; rate limit not published | Docs contradict themselves (a week vs 1 day); 200 requests/minute on PPG and blood report APIs. |
| comparison-matrix.md | 241 | Ultrahuman pricing "Not disclosed" | Device and subscription prices published; API access unpaid (agreement). |
| comparison-matrix.md | 340 | Raw format and rates undocumented | As above. |
| comparison-matrix.md | 385 | "Biostrap and Ultrahuman claims are unproven" | Ultrahuman's raw PPG is now documented (scale still limited to own recordings). |
| comparison-matrix.md | 411 | "No academic programme"; terms "Not read, Unclear"; "Not disclosed" | Pulsomics collaboration route; API Agreement terms read (Notion); prices published. |
| shared/unresolved-questions.md | 283 (Q67) | Raw PPG sampling rate open | Rate answered (typically 50 Hz); UltraSignal pricing and scale still open. |
| shared/unresolved-questions.md | 370 (Q49) | "whitelist-only Partner API" | Personal tokens and OAuth app registration are self-serve in the portal. |

Not edited: the profile, matrix and unresolved questions are left for the coordinator.
