# Oura: judgement, 2026-10-10

Inputs: `A.yaml`, `B.yaml`, `gaps.md`, and the pilot `facts/oura.yaml` (treated as a third input, not as ground truth). Output: `facts/oura.yaml`, 41 entries (32 stated, 7 not_public, 1 conflict, 1 unclear), 14 watched pages. All 98 quotes matched "exact" on their live pages (same fetch and `match_quote` as `quote_probe.py`). `validate.py --file facts/oura.yaml`: 0 errors, 0 unresearched. `weekly.py --only oura --no-state`: 0 quotes missing, 0 reworded. Two accessdata.fda.gov search pages show as unreachable (404 to automated requests, expected).

## Fields where the inputs disagreed

| Field | A | B | Pilot | Decision and reason |
|---|---|---|---|---|
| ai_training_terms | No training; no feeding API data to any AI (s.6(g), s.4(d)) | Prohibited "without Oura's prior written consent" (s.4(a)) | No route; note flags a repair agent's contrary reading | Read the whole Agreement. Both readings are right about different clauses. s.4(a)(iii) has a consent route ("unless Oura provides prior written consent"). s.4(d) ("shall not ... use ... the Oura API to develop, train, fine-tune, evaluate, prompt, or otherwise provide input or data to any AI Model") and s.6(g) ("YOU SHALL NOT USE OR ALLOW THE USE OF USER DATA TO TRAIN ...", material breach) have none. s.4(c): Prohibited Uses apply "regardless of whether a User has purportedly consented". s.6 is the Intellectual Property section. Net: training on API data is not obtainable under this Agreement alone; whether a separate Research Agreement overrides is not public. All five clauses quoted in the record. |
| rate_limits | 5,000 / 5 min, Verified | 5,000 / 5 min, Verified | Two layers, numbers not published | Read OpenAPI 1.41. Its FAQ says "The Oura API is limited to 5000 requests per 5-minute period"; its newer Rate Limits section names the two layers and gives no number. Both are in the current document, so the figure is published. Kept 5,000/5 min, Verified, with a note that the per-layer split is unstated. The pilot was wrong. |
| retention_terms | stated; Agreement only | stated; Agreement plus docs FAQ "Store the historical data in your own database", noted as tension | stated; Agreement only | Status `conflict` for the API scope, with both sources. The Agreement is the contract and the FAQ is guidance, said in the note. Added the s.5(f) subscription-cancellation deletion rule and s.4(c) (gap D1, D3). Kept B's consumer scope (privacy policy) and added an Enterprise Platform scope (gap B2). |
| program_eligibility | stated (target segment list) | stated (same, plus Research Sponsor selects participants) | not_public | stated. The page does list segments; the value also says no criteria are published. B's terms-and-conditions quote confirmed exact. |
| program_application | not_public | stated (contact form; Order; Research Agreement) | stated (contact form) | stated, Verified. B's business-terms quote about a Research Agreement confirmed exact. |
| program_status | Corroborated | Verified | Verified | Verified: the page and app listing are live. B's note that a consumer science page says "14 active collaborations" gave no URL; not verified, dropped. |
| academic_vs_commercial | stated, Corroborated | stated, Verified | unclear | stated, Corroborated (premium metrics undefined). Combined B's "free for personal and commercial" quote with A's reservation of business pricing. |
| device_price | Per-finish product pages | Store page "From" prices | unresearched | Store page (one watched URL), three scopes. Finish prices in the value read from the same page. |
| minimum_commitment | not_public (org) | consumer stated + org not_public | unresearched | Both scopes. A's 30-day/no-auto-renew note now carries the exact quote from the partner article. |
| raw_streams [API] | Corroborated | Verified | unresearched | Corroborated. The docs never say "no raw signals"; the absence is read from the data-flow text and the route list. |
| derived_metrics | One entry | API and Enterprise scopes | unresearched | B's two scopes, with A's fuller route list for the API. |
| export_routes | Includes MCP Server, Oura on the Web shutdown | Includes Health Connect/Apple Health, Gen3 membership gate, Terra and Fitrockr secondary sources | stated | Merged. Dropped B's Terra and Fitrockr secondary sources (not needed once Oura's own partner article states the gate). |
| baa | Whitepaper only | Business terms plus whitepaper | unresearched | Both, plus the privacy policy's "acting as a Business Associate" (gap E2). Corroborated (self-claim cap). |
| dpa | unclear | not_public | unresearched | not_public, Corroborated. No DPA is published; the processor role and the independent-controller clause are recorded as context, plus the Ouraring, Inc. counterparty (gap A3). |
| iso27001, academic_pricing, history_depth | Confidence Verified or Corroborated | Unclear | mixed | Kept not_public with Verified or Corroborated: a dated "not published on these pages" claim is not uncertain. iso27001 kept at Corroborated. |
| fda_clearances | stated, Corroborated | stated, Corroborated | unresearched | not_public, Verified, per the README rule for negative FDA results. The openFDA 510(k) dataset includes De Novo (DEN) records, so `applicant:oura` covers De Novo (checked: DEN records exist in the dataset, 489). Searches listed in the note. The Fertile Window registration (3015599655, LHD, class U, 2023-08-08) is cited with an exact quote from openFDA. |
| hipaa_statement | trust-center vs security URL | security | trust-center | Used ouraring.com/security, where both researchers read the text; trust-center dropped from the watch list. |

## Gap hunter findings

| Finding | Decision | Why |
|---|---|---|
| A1 "Oura Teams" research portal in papers 2022 to 2026 | Accepted as a separate `research_program` scope, confidence Reported | Three paper quotes confirmed exact. Papers are secondary to the vendor, and Oura never uses the name; relation to the Enterprise Platform is unknown. One paper equates it with "Oura on the Web". teams.ouraring.com does not resolve. The Haimovich PMC13626187 quote was used; the protocol paper PMC12822870 was not needed. |
| A2 Privacy policy retention while account active | Accepted (consumer scope of retention_terms) | Quote exact. |
| A3 Agreement counterparty Ouraring, Inc. | Accepted (dpa source and note) | Quote exact. |
| A4 Three AI clauses | Accepted | Confirmed by reading the full Agreement (see above). |
| B1 Research App: sponsor controller, Oura processor, blinding | Accepted (research_program, dpa) | Quotes exact. |
| B2 Enterprise Platform: withdrawal does not touch extracted data; Oura uses aggregated data | Accepted (retention_terms, Enterprise scope) | Quotes exact. |
| B3 Tidepool donated rings and memberships | Accepted as a secondary source in academic_pricing's note | Quote exact; secondary only, so it informs the note, not the status. |
| B4 Oura-NUS Joint Lab | Accepted in research_program note only | Partnership, not a program; no quote added. |
| B5 Oura as trial collaborator | Accepted in research_program note only | Registry names only; what Oura provides is not stated. |
| C1 FDA: no clearance; Fertile Window listing; EUDAMED Class I; Natural Cycles | Accepted, except EUDAMED not re-checked (noted as gap hunter's) and S-1 extracts rejected | openFDA re-run by me. S-1 text unconfirmed (sec.gov 403). K202897/K231274 local-copy quotes not used; the note states the Natural Cycles point without a quote. |
| C2 No recall or warning letter | Accepted in fda_clearances note | openFDA recall search re-run, no matches. |
| D1 s.4(c) consent does not override | Accepted | Quote exact. |
| D2 Right to charge later; no charging users | Accepted (api_platform_fees, academic_vs_commercial) | Quotes exact. |
| D3 Deletion on subscription cancellation | Accepted (retention_terms) | Quote exact. |
| D4 2021 Agreement superseded | Accepted (deprecations) | Probed a sentence from the page: exact. |
| D5 Partner support; Gen2 unaffected | Accepted in notes | Gen2 line read on the partner API article. |
| E1 Government page NIST 800-171/IL5; healthcare "Enterprise API" | Accepted: Enterprise API quote in export_routes; NIST/IL5 in soc2 note | Enterprise API quote exact. NIST/IL5 is a vendor claim with no field of its own. |
| E2 BAA: S-1 vs privacy policy | Privacy policy accepted; S-1 rejected | S-1 unreadable (403). |
| F1 IPO filed and postponed | Rejected | No schema field; context only. |

## Statements in the profile or matrix that the record contradicts

| File | Line | What it says | What the record says |
|---|---|---|---|
| module-01-wearables/profiles/oura.md | 22 | "two-layer rate limits (numbers no longer published)" | OpenAPI 1.41 FAQ publishes 5,000 requests per 5 minutes |
| module-01-wearables/profiles/oura.md | 117 | Current docs "no longer publish numeric limits"; 5,000/5 min "came from a secondary source" | Same: the figure is in Oura's current OpenAPI document |
| module-01-wearables/profiles/oura.md | 257, 270 | Numeric limits "not published" | As above |
| module-01-wearables/comparison-matrix.md | 159 | "numbers not published"; 5,000 figure "from a secondary source only" | As above |
| module-01-wearables/profiles/oura.md | 122 | AI terms are s.4(a)(iii) (consent route) and s.6(g) only | Also s.4(d): no use of the API to "evaluate, prompt" any AI model, LLM use only via the MCP Server, no consent route; and s.4(c): user consent does not lift Prohibited Uses |
| module-01-wearables/comparison-matrix.md | 387 | "no AI/ML training (one clause has no consent exception)" | Two clauses (s.4(d), s.6(g)) have no consent exception, and s.4(d) also bars prompting or evaluation |
| module-01-wearables/profiles/oura.md | 121 | Deletion on request and on termination of the Agreement | Also on the user's cancellation of the app's subscription (s.5(f)) |
| module-01-wearables/profiles/oura.md | 109, 300; comparison-matrix.md 387 | Whether research customers sign different terms "is not public" | The privacy policy shows the Enterprise Platform does not apply 72-hour deletion to extracted data, and the Research App makes the sponsor controller with Oura as processor; a Research Agreement is named in the business terms |
| module-01-wearables/profiles/oura.md | 111 | Studies "typically" use a custom OAuth app or middleware | Many published studies used an Oura researcher portal named "Oura Teams" (Reported) |
| module-01-wearables/profiles/oura.md | 27 | Oura "now sells" a research offering, implying it is new | Papers show a researcher portal in use since at least 2022 |
| module-01-wearables/profiles/oura.md | 116; comparison-matrix.md 219 | API "free to use" / "API free" | Free today, but the Agreement reserves the right to charge, including differentiated pricing for business users |
| module-01-wearables/profiles/oura.md | 155, 274, 305; comparison-matrix.md 245 | BAA availability not stated / "no BAA published" | Business terms require a BAA before uploading PHI; whitepaper describes a BAA enclave (Corroborated) |
| module-01-wearables/profiles/oura.md | 155, 274 | Data residency not stated | Whitepaper: enterprise deployment options can support geo-specific residency (no regions named) |
| module-01-wearables/profiles/oura.md | 155 | Retention period not stated | Privacy policy: measurement data kept only while the account is active |
| module-01-wearables/profiles/oura.md | 159, 307; comparison-matrix.md 219 | Ring 5 price Corroborated from launch press, "not found on an Oura page" | ouraring.com/store lists Ring 5 from $399 (Verified); Ring 4 still sold from $349 |
| module-01-wearables/profiles/oura.md | 154, 318 | Trust centre quotes cited at ouraring.com/trust-center | Same text is on ouraring.com/security; not a contradiction, but the record now cites /security |
| module-01-wearables/comparison-matrix.md | 245 | Regulatory: "None documented in the profile" | No clearance (Verified), but an FDA registration listing for Fertile Window (LHD) exists |
| module-01-wearables/profiles/oura.md | 7, 305 | Organization Oura Health Oy, Finland; EU headquarters may help EU studies | The API Agreement's counterparty is Ouraring, Inc., a Delaware corporation |
| module-01-wearables/profiles/oura.md | 320 | Developer portal: https://cloud.ouraring.com/ | That page now serves only "Oura on the web" (discontinued 5 Oct 2026); new apps are created in the newer developer portal |
| module-01-wearables/profiles/oura.md | 162 | Waived or bulk membership for study rings "not established" | Still not published, but a secondary source reports Oura donated rings and memberships to the Tidepool dataset (2025) |

## For the coordinator to check by hand

- The s.4(d) reading: it bars using the API to "prompt" any AI model, which on its face covers an LLM-assisted analysis of API data. Worth a legal read before the profile states it strongly.
- Whether "Oura Teams" is the current Enterprise Platform, and whether the 5 October 2026 shutdown of Oura on the Web touched it. One paper equates the two names.
- EUDAMED Fertile Window Class I entry (gap hunter only, not re-run).
- DPF certification on dataprivacyframework.gov (JavaScript list).
- The two accessdata.fda.gov search URLs will report as unreachable weekly and move to "check by hand" after two weeks; that is expected for that host.
