# Zepp Health (Amazfit): judgement, 2026-10-22

Cheaper variant: one researcher draft (`A.yaml`), no `B.yaml`, no `gaps.md`. In place of an A-versus-B comparison I audited A source by source, spot-checked its `not_public` and `unclear` calls, and ran my own short gap sweep. Other inputs: the starter `facts/zepp-amazfit.yaml` (all `unresearched`) and `module-01-wearables/profiles/emerging-platforms.md` (Amazfit / Zepp, lines 128 to 138).

Output: `facts/zepp-amazfit.yaml`, 31 entries (17 stated, 8 not_public, 6 unclear, 0 conflict), 60 quotes, 15 watched pages. Every quote in A and every quote I added matched "exact" (same fetch and `match_quote` as `quote_probe.py`). `validate.py --file facts/zepp-amazfit.yaml`: 0 errors, 31/31 researched. `weekly.py --only zepp-amazfit --no-state`: 41 pages, 0 quotes missing, 0 reworded, 0 dead; 1 check by hand (the robots-disallowed app privacy policy on upload-cdn.zepp.com) and 1 unreachable (sec.gov, 403). Re-check dates: 2026-11-21 for research access, pricing and data; 2027-01-20 for compliance. Scratch files: only under the session scratchpad's `zepp-judge/` folder (a probe script and a clone of the public rest-api wiki, used for its edit history).

The robots.txt files on us.amazfit.com and aura.zepp.com were not opened by me directly; the project fetcher reads them only as allow/deny rules. Nothing on any page was acted on as an instruction.

## Coordinator's points

1. **Does the Zepp Open Platform still accept new partners?** Not established, so `program_status` stays `unclear`. What I confirmed on 2026-10-22: dev.huami.com serves "Zepp Open Platform" (HTTP 200); api-open.huami.com answers an API path with HTTP 400 "Missing required parameter 'Authorization'" and auth.huami.com/oauth2/authorize with HTTP 405, so the API is live, not dead. Against that: the wiki was last edited 2020-11-27 (wiki git history), the repo's last commit is 2020-12-29, the API docs' footers say 2017 to 2020, and issue 26 (2022-08-19, still open, no Zepp reply) reports the old platform deprecated after business approval. **Correction to A:** A said "Zepp staff fixed a doc link on the rest-api repo in June 2026." Not so. Issue 28's only reply (2026-06-24) is a bare URL from an account with no stated affiliation and `author_association: NONE`, and the wiki link was not changed. I retyped that source as `secondary` and rewrote the value and note.
2. **Paid API access.** `api_platform_fees` stays `unclear`, **Reported**. The only evidence is issue 25 (opened 2021-12-17, closed 2023-06-07 with no Zepp comment), where the applicant quotes Zepp's reply "You need to pay for our API and purchase our equipment." **Correction to A:** A's `program_application` value said the applicant was "told a Zepp business representative would contact them". That sentence is the applicant quoting the dev.huami.com application docs (item 4), not a reply to them. I reworded the value and added a note. The quote stays, typed `secondary`.
3. **FDA.** Confirmed in openFDA (510(k) data last updated 2026-10-12). Registration listing for Anhui Huami Information Technology, owner/operator 10083608: "Amazfit Balance A2287" under PUH (Analyzer, Body Composition, Exempt; class 2; 21 CFR 870.2770; listed 2023-08-08) and "Zepp Clarity ONE", "Zepp Clarity Omni", "Zepp Clarity Pixie" under QUG (OTC wireless air-conduction hearing aid; class 2; 21 CFR 874.3305; listed 2023-04-04). Both product codes are submission type 4 (exempt). The record uses the accessdata.fda.gov registration page as `url` and the openFDA registration query as `fetch_url` for four exact quotes (both device names, both product descriptions). I restructured A's negative searches the same way: accessdata pages as `url`, openFDA queries as `fetch_url`, with `expect_absent: true`, since openFDA answers "No matches found" with HTTP 404. I added PMA searches (huami, zepp), a 510(k) applicant search for amazfit and a registration search for zepp (all no matches). I narrowed A's value from "No 510(k), De Novo or PMA" to "No 510(k) or PMA", because openFDA has no De Novo endpoint and De Novo was not searched. New: a second "Amazfit Balance A2287" PUH listing held by Shenzhen Zowee Smart Manufacturing (owner/operator 10088482), a contract manufacturer. Recorded in the note.
4. **ISO 27001 renewal year.** Kept `unclear` as instructed; the 2024 versus 2025 discrepancy in the Form 20-F is unresolved, sec.gov was not worked around, and no fetchable source gives a date. **New finding:** the zepp.com website privacy policy's footer, which A cited only as a checked page, states "ISO/IEC 27001:2022 and ISO/IEC 27701:2019 certificate number [IS 743462, PM 743467]". Both its sentences are now quoted (exact) and the certificate numbers are in the value. The page names no certifying body, scope or dates. The "IS"/"PM" prefixes look like BSI's numbering, but that is my inference and is labelled as such. Once the year is settled, or judged immaterial, this can become `stated` at Corroborated. Verified would need a certificate or registry entry.
5. **App privacy policy.** It sits on upload-cdn.zepp.com, which robots.txt disallows. Its terms (regional storage, SCCs, DPO address, AI-feature processing, de-identified R&D data, effective 2026-07-14) stay in notes and values marked as read by hand. They are not quoted. Sources pointing at it carry no quote, and the weekly check lists it under "check by hand".

## What I changed from A, and why

| Field | A | Final | Reason |
|---|---|---|---|
| watch | 15 incl. docs.zepp.com/docs/intro/ | 15, intro swapped for the Accelerometer reference | The intro page carries no fact. The Accelerometer page is cited three times and was on the starter watch list. |
| research_program | stated, Corroborated, 3 quotes | Same, plus App Store quote for "STF Sleep Research" | Gap finding: a Zepp Inc. iOS app built for Stanford sleep studies (last updated 2021-03-05), showing study-specific apps as one collaboration route. Note also records that the zepp.com footer "Academics" link only goes to the technology page's academic section. |
| program_application | Value said applicant was "told" a representative would call | Reworded | That sentence is the applicant quoting Zepp's docs (point 2). |
| program_status | unclear; claimed a Zepp staff doc fix in June 2026 | unclear; claim removed; issue 28 retyped `secondary`; probes and dates added | Point 1. |
| developer_program_status | Note: "had a release hmauth/0.0.6" | Note: a commit titled "release \|> hmauth/0.0.6", no release object, only tag v0.0.5 | GitHub API shows a commit, not a release. Also says this does not show the partner program is open. |
| subscription_price | $9.99 monthly quote only | Added "Yearly, 14 Day Free Trial $29.99" (exact) | The value names the yearly range, so one end of it should be quoted. I also checked that the listing shows yearly plans of $29.99, $34.99, $39.99 and $49.99. |
| api_platform_fees | unclear, Reported | Same; note adds issue dates and no Zepp follow-up | Point 2. |
| ai_training_terms | not_public, confidence Unclear | unclear, with a value | The governing app policy is unreadable by the tool, so "searched and not published" is not a clean claim. The fetchable pages (website policy, wiki) have no "train" or "machine learning" text, which I checked. |
| baa, dpa, hipaa_statement, soc2 | not_public, Verified | not_public, Corroborated | These fields fall under the self-claim cap. Other judged records (for example RingConn) hold them at Corroborated. Spot check: no "HIPAA", "SOC 2", "Business Associate" or "processing agreement" text on the website privacy policy, data-analytics, technology, privacy-support or security-center pages. |
| iso27001 | unclear; 20-F and src.zepp.com only, no quote | unclear; two privacy-policy quotes with certificate numbers added | Point 4. |
| fda_clearances | Verified; negatives as bare openFDA URLs | Verified; accessdata url + openFDA fetch_url throughout, `expect_absent` on negatives, 2 more quotes, PMA searches, contract-manufacturer listing, De Novo wording narrowed | Point 3. |

Checked and left as A had them: every other quote (all exact); device prices (the store's products.json runs from $9.99 accessories to $649.99 T-Rex Dual Solar, consistent with A's note); the legacy docs' "Last updated" footers (ECG 2018-03-08, sensor 2017-10-19, main API 2020-01-19); the PPG CSV example in the sensor-tagging doc; the website privacy policy's statement that it does not cover app or device data; user_cap, academic_pricing, minimum_commitment and rate_limits as not_public. No field needed `conflict`.

## Own gap sweep

| Finding | Decision |
|---|---|
| zepp.com privacy policy states ISO/IEC 27001:2022 and 27701:2019 certificate numbers | Accepted into iso27001 (point 4). |
| "STF Sleep Research" iOS app by Zepp Inc. for Stanford sleep research | Accepted into research_program. |
| Shenzhen Zowee contract-manufacturer FDA listing of Amazfit Balance A2287 | Accepted as a note in fda_clearances. |
| Web search for a current (2026) Zepp research or partner data API | Nothing found. Results were aggregators (Terra, Thryve, Spike, Sahha) and the 2020 to 2021 data-analytics page. |
| zepp.com footer "Academics" link | Points to technology-2#technology_academic, already cited. Noted only. |
| Certification body's public directory for IS 743462 | Not checked: it is a script-driven search form. Left for the coordinator. |

## Profile, README and unresolved-questions statements the record contradicts

The comparison matrix has no Amazfit / Zepp row.

| File | Line | Says | Record says |
|---|---|---|---|
| module-01-wearables/profiles/emerging-platforms.md | 130 | "None publishes a research API." | Zepp documents a cloud OAuth 2.0 Web API (the legacy Huami/Zepp Open Platform) for approved corporate partners, and says a PhD researcher must apply in the institution's name. Whether it takes new partners is unclear, but it is published. |
| module-01-wearables/profiles/emerging-platforms.md | 130 | Data-analytics page "states no ... application route" | True of that page. But zepp.com/contact-us lists "For Researchers & Developers developer@zepp.com", and the wiki gives an application route (dev.huami.com, 3 to 7 day review, datapartner@huami.com). |
| module-01-wearables/profiles/emerging-platforms.md | 136 | "No cloud research API or research programme found" (confidence: "No research cloud API: Reported") | No named research program (agreed), but a cloud data API exists for partners (developer_program_status, program_eligibility, Corroborated). |
| module-01-wearables/profiles/emerging-platforms.md | 136 | "No raw PPG in the documented API" | True for the Zepp OS on-watch API. The legacy Web API documents raw ECG at 250 samples per second, per-minute raw motion data, and user-tagged sensor files with a PPG CSV example (raw_streams, Legacy Open Platform scope, Reported because the docs date from 2017 to 2020). |
| module-01-wearables/profiles/emerging-platforms.md | 136 | Accelerometer and gyroscope "can be read only by building and side-loading a watch app" | A custom app is needed, but Zepp OS apps can also be published through the Zepp store's review (docs.zepp.com/docs/distribute/), so side-loading is not the only route. |
| module-01-wearables/profiles/emerging-platforms.md | 136 | "the developer.zepp.com landing page is a JavaScript shell with no retrievable text" | developer.zepp.com/os/home returns quotable text today ("Tools and resources to help you build Zepp App faster and easier, across every Zepp OS device."). |
| module-01-wearables/profiles/emerging-platforms.md | 136 | "The Thryve Zepp integration page cited earlier now returns 404" | A Thryve Zepp page is live at thryve.health/supported-wearable-devices/zepp-amazfit (quote exact 2026-10-22). The old URL may still be dead; the integration itself is still advertised. |
| module-01-wearables/profiles/emerging-platforms.md | 138 | "Only the vendors can confirm whether an unpublished partner or research arrangement exists" | A partner arrangement is published (the legacy data-cooperation process), with a 2021 report that it is paid. What only Zepp can confirm is whether it is still open. |
| module-01-wearables/profiles/emerging-platforms.md | 130 to 138 | Silent on FDA, ISO 27001, prices and subscriptions | Not contradictions, but the record now holds the FDA listings (PUH, QUG; no clearances), ISO/IEC 27001:2022 certificate number, device prices, and the optional Zepp Aura Premium subscription. |
| module-01-wearables/README.md | 242 to 243 | RingConn, Circular and Amazfit / Zepp: "none publishes a research API" | Same as line 130 above, for Zepp. |
| shared/unresolved-questions.md | 339 | Q51: "No cloud research API or programme found (Reported)" | Legacy partner Web API is documented; open status and fees are the real open questions (developer@zepp.com, datapartner@huami.com). |

## For the coordinator to check by hand

- **Open Platform status.** Whether Zepp still reviews data-cooperation applications, and the fee. Only Zepp can answer: developer@zepp.com or datapartner@huami.com. dev.huami.com's application docs are script-rendered and were not logged into.
- **ISO 27001 renewal year.** Read the two 20-F passages again (sec.gov, in a browser) and, if possible, look up certificate IS 743462 in the certifying body's public directory. A directory entry would also allow Verified.
- **App privacy policy** (upload-cdn.zepp.com/tposts/8192, robots-disallowed): confirm the regional-storage, SCC, AI-feature and de-identified R&D wording in data_residency, gdpr_statement, retention_terms and ai_training_terms.
- **aura.zepp.com $69.99 annual Zepp Aura Premium** price, which is script-rendered and unquoted.
- **The note in research_program** about the 20-F's "data analytics capabilities" wording, also read by hand only.
