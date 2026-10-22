# Judgement: verily, 2026-10-22

Single-researcher run, so this is an audit of A.yaml instead of an A-versus-B comparison. There was
no B.yaml and no gaps.md. I opened the source for every quoted fact and re-probed every quote with
`quote_probe.py`. I also spot-checked each `unclear` and `not_public` call and ran my own short gap
sweep. Nothing was signed into, no form was submitted, and no bot check was bypassed. The DPF lookup
used the registry list page's own public read-only search request.

Final record: 33 facts. 25 stated, 3 not_public, 3 unclear, 1 conflict, 1 not_applicable. 15 watch
pages. `validate.py --file facts/verily.yaml`: 0 errors, 0 unresearched. `weekly.py --only verily
--no-state`: 32 pages, 0 quotes missing, 0 reworded, 0 dead, 0 check by hand.

## Audit of A: what held, what I changed and why

All 53 quotes in A probed "exact" on their live pages (or fetch_url) on 2026-10-22. Both
`expect_absent` sources (verily.com/solutions/verily-study-watch) still return 404.

| Field | A | Final | Why |
|---|---|---|---|
| `research_program` | note: "No Study Watch page survives in the verily.com sitemap" | Note reworded: no Study Watch *product* page survives | The sitemap still lists Study Watch stories, including /stories/verily-study-watch-afib-clearance, /stories/verily-study-watch-receives-fda-510-k-clearance-for-ecg and /stories/study-watch-another-step-closer-to-powering-precision-health. A itself cites two of them. |
| `program_status` [Study Watch] | conflict, Reported. Quipment described as "a clinical-trial equipment firm" and in the note as "initial importer" | Still conflict, Reported. Added two MD+DI quotes from the CEO's memo ("fully wind down the program", "Study Devices launched with numerous study partners"). Quipment is now described only as openFDA shows it: establishment type "Repack or Relabel Medical Device", with the initial-importer flag Y. Added that quote. Build-ID note added. | openFDA lists Quipment's establishment type as repack or relabel. The "initial importer" wording comes from a flag, not from the type. Nothing I read says Quipment is a clinical-trial equipment firm, so I dropped that phrase. The memo is the closest thing to a Verily statement. It names "Study Devices" but not Study Watch, so the conflict stands, and Reported is still right. The trust page still lists "Study Watch & Hub" in both its SOC 2 and ISO 27001 lists (confirmed in the JSON). |
| `device_price` | stated, Verified | stated, **Corroborated**; value reworded | The quotes say "not directly available to consumers" and "investigational device". "Never sold" and "no list price was ever published" are inferences from absence, so the confidence can't be Verified. |
| `raw_streams` [Study Watch] | PPG, accel, ECG, environmental; Corroborated | Added EDA, heart rate and "up to a week" of onboard raw storage, from MassDevice (2017) | Gap sweep. The 2017 Verily launch post is gone: verily.com/blog/introducing-verily-study-watch redirects to a 404 under /perspectives/. MassDevice is the surviving source for EDA and onboard storage. Engadget also confirms EDA, but I didn't add it. |
| `raw_streams` [Viewpoint + Galaxy Watch] | unclear, Unclear | **stated, Reported** | Gap sweep. MedCity News (March 2026) paraphrases Verily's chief product officer: researchers get "raw device signals, such as photoplethysmography and motion data from the Galaxy watches' accelerometers and gyroscopes". This is a journalist's paraphrase. Verily's own release lists no streams. So: Reported, not Corroborated. |
| `deprecations` | HIT Consultant, GUDID, release notes | Added the MD+DI memo quote | Gives the CEO's memo wording, not just a spokesperson soundbite. Confidence stays Corroborated. GUDID dates re-checked: retinal cameras 2026-04-27; Onduo 2025-12-15 and 2025-12-17. |
| `retention_terms` | value: "Workbench ToS lets Verily delete trial accounts..." | value: "Workbench release notes say..." | The quote comes from the release notes page, not a ToS. |
| `ai_training_terms` | unclear | unclear (kept). Note records the searches. | Searched the privacy policy and terms JSON for "artificial intelligence", "machine learning" and "train". The only hit was a training-materials confidentiality clause in the SignalPath terms. No model-training clause, so `unclear` holds. |
| `dpa` | unclear | unclear (kept). Note records the searches. | No "processing agreement" or "Data Processing" text in the privacy policy or terms. |
| `gdpr_statement` | one entry, Corroborated; DPF not checked | General entry kept at Corroborated. **New scoped entry "Data Privacy Framework certification", Verified, type `certificate`.** | See the DPF section below. |
| `fda_clearances` | Verified; decision dates in the value without date quotes; "the only current registration listing for K182456 is by Quipment" | Added exact quotes for each decision date and for the K192415 device name. Value now says openFDA returns no listing for K192415 or K213357, or under Verily. Note on the Parkinson's exam-tool denial (MD+DI). | Every date in a value should have a quote. All three 510(k)s were re-confirmed in openFDA: applicant Verily Life Sciences, LLC; product code DXH; Traditional; Substantially Equivalent; decided 2019-01-17, 2020-01-17 and 2022-07-19. The registrationlisting searches for K192415, K213357, `registration.name:VERILY` and `owner_operator.firm_name:verily` all return NOT_FOUND. |
| `iso27001` | Corroborated | Corroborated; value notes the Coalfire seal on the page | The seal image is named CoalfireCert-ISO27001. No certificate is published, so the self-claim cap still applies. |
| Build-ID notes | none | Added a note to every fact whose source fetch_url carries `/_next/data/1y9FmmHH1nlmtBVxwLMlY/`: program_status [Study Watch], retention_terms, ai_training_terms, baa, dpa, hipaa_statement, gdpr_statement (general), iso27001, soc2, data_residency | See below. |
| Watch list | 14 | 15: added the DPF registry (fetch_url participants/10091) | The trust role now has an independent source. |

Spot-checks that held without change: `academic_pricing`, `minimum_commitment` and `rate_limits`
(not_public). Each checked page loads and shows no such terms. `history_depth` (unclear) also held.
So did `subscription_price` (not_applicable) and `user_cap`, `api_platform_fees` and
`quote_required` (the upgrade-contact page table matches).

## The three points the coordinator asked about

1. **Study Watch status.** Confirmed as conflict at Reported, as described above. The HIT
   Consultant quote (2025-08-29) is exact, but the article doesn't name Study Watch. The trust page
   still lists "Study Watch & Hub". The openFDA registration listing for K182456 is under QUIPMENT
   INC., Kennesaw GA, registration 3012302888. The product was created 2026-05-12, with proprietary
   name "Study Watch" and product code DXH. It's the only listing for any Study Watch 510(k). FDA
   facts use the accessdata.fda.gov page as `url` and openFDA as `fetch_url`, as required.
2. **The three 510(k)s.** K182456, K192415 and K213357 were all confirmed. Details are in the
   table above.
3. **Next.js build-ID URLs.** I found no stable alternative. The static HTML at
   verily.com/privacy-policy, /security-trust and /terms carries the text only inside the
   `__NEXT_DATA__` script, which `common.html_to_text` strips. Probing the plain URLs gave "missing"
   for every policy and trust quote, except the soc2 NDA sentence, which is in static HTML. The page
   links no PDF, no CMS API host and no printable copy. A Strapi-style `documentId` is present, but
   no public endpoint is exposed. The only external links are a Vercel blob store for images, a
   OneTrust request webform and support.verily.com. So I kept the `_next/data` fetch_urls and added
   a note on every affected fact. The watch entries keep their fetch_urls too. When Verily
   redeploys, every Verily policy and trust quote will show "missing" in the same week. The fix is
   to read the new `buildId` from the page source and replace it in all 16 fetch_urls (3 watch, 13
   sources).

## DPF participation

The registry search for "Verily" returns two Active records. Both are in Dallas, TX, with
self-assessment.

- **Verily Health Inc.**, OrganizationId 10091. EU-U.S., Swiss-U.S. and UK Extension certified
  2026-04-20, next due 2027-04-20, no inactive periods. This is the entity named in the current
  privacy policy (effective and last updated April 14, 2026, "Thank you for your interest in Verily
  Health Inc.").
- **Verily Life Sciences, LLC**, OrganizationId 7768. EU-U.S. and Swiss-U.S. since 2018-02-02, UK
  Extension since 2025-01-13, next due 2027-03-12. Lapses: 2024-02-12 to 2025-01-13 (EU and Swiss),
  and 2025-02-18 to 2025-03-17 (all three).

Following the labfront and fitabase pattern, I added these as a scoped `gdpr_statement` entry at
**Verified**, with type `certificate`, 10 exact quotes and `url`
https://www.dataprivacyframework.gov/list. The general GDPR entry stays Corroborated, because a DPF
listing covers the transfer mechanism only. I left the registry's contact names and emails out of
the record.

## Gap sweep: accepted and rejected

| Finding | Decision |
|---|---|
| MD+DI 2025-08-28 article quoting the CEO's 2025-08-25 memo ("fully wind down the program", "Study Devices") | Accepted into `program_status` [Study Watch] and `deprecations`. |
| MedCity News, March 2026: Verily CPO on raw PPG, accelerometer and gyroscope via the Galaxy Watch bundle | Accepted, `raw_streams` [Viewpoint], Reported. |
| MassDevice 2017: ECG, HR, EDA, inertial; battery up to 1 week; "up to a week's worth of raw data" | Accepted into `raw_streams` [Study Watch]. |
| Engadget 2017: EDA | Holds up, but I didn't add it. MassDevice already covers EDA. |
| Fierce Biotech 2017 | Rejected. 403 to the script, so it's unverifiable here. |
| DPF registry, two entities | Accepted (see above). |
| FDA denial of the Parkinson's exam-tool request (MD+DI) | Recorded as a note on `fda_clearances` only. No FDA record of it was looked up, so it isn't a fact. |
| Reports that Alphabet planned to sell Verily, and the 2025 headquarters move to Dallas (search results) | Rejected. No schema field fits, and I didn't open primary sources. |
| verily.com/perspectives/... Samsung URL in the old record | It 301-redirects to /newsroom/...; A's newsroom URL is correct. |

## Contradictions with the profile and the comparison matrix

I didn't edit either file.

**module-01-wearables/profiles/emerging-platforms.md**

| Line | Profile says | Record says |
|---|---|---|
| 94 | Status Unclear: no product page, no 2026 announcement; was "Active, not discontinued" | Conflict, Reported. Verily wound down its devices program in August 2025 (memo naming "Study Devices"; HIT Consultant, MD+DI). The trust page still lists Study Watch & Hub. A third-party repack/relabel firm listed K182456 with FDA on 2026-05-12. |
| 96 | Data streams: ECG, HR, EDA, inertial (Corroborated) | Consistent. The record adds PPG at 30 Hz and accelerometry at 30 Hz (PBHS paper) and environmental sensors. |
| 97 | "Researchers can 'analyse the raw data points that power digital biomarkers'" (as a Study Watch fact) | That sentence is MedCity News (2026) describing the **Galaxy Watch** bundle, not Study Watch. The quote is misattributed. For Study Watch, outside researchers get de-identified PBHS data on approved request only. |
| 97 | "the device stores weeks of raw data at a time" | MassDevice (2017): "up to a week's worth of raw data". The original Verily post is gone. |
| 98 | 510(k)s incl. on-demand ECG and irregular pulse; Parkinson's exam bid rejected (Corroborated) | Consistent, and now Verified for the 510(k)s: K182456 (2019-01-17), K192415 (2020-01-17), K213357 (2022-07-19). |
| 100 | Pricing/access: not public; enterprise and pharma engagement (Unclear) | Workbench Standard is free and self-serve (Google account, then a DUA per collection, including the PBHS Limited collection). Professional is paid and unpriced. Viewpoint is by demo request. Academic pricing and minimum commitment are not_public. |
| 102-106 | Multi-week onboard raw storage plus FDA clearances place it in the regulated-research tier alongside Empatica and Ametris | The storage is "up to a week". The device program has been wound down, so it can't be recommended as a procurable research device. |
| 113 | Galaxy Watch raw signals, PPG, accel and gyro: **Corroborated** (Verily press release; MedCity News) | The Verily release does not mention raw signals. Only MedCity's paraphrase of Verily's CPO does, so the record has Reported. |
| 120 | "There is no self-serve route." | Workbench Standard is a self-serve free tier (beta), with Project Baseline Limited data under a DUA. There is still no self-serve route to the device or to Viewpoint. |
| 124 | Link verily.com/perspectives/verily-and-samsung-... | It 301-redirects to verily.com/newsroom/verily-and-samsung-.... |
| 161 | "Verily (ECG + EDA + inertial, weeks of onboard raw)" | Up to a week of onboard raw (MassDevice). The device program has been wound down. |
| 167 | Galaxy Watch raw signal now has a commercial clinical-trial route | It rests on a Reported secondary paraphrase. Verily's own materials list no streams. |

**module-01-wearables/comparison-matrix.md**

| Line | Matrix says | Record says |
|---|---|---|
| 63 | Approval: "Enterprise and pharma engagement"; new study without vendor contact: "No; Study Watch status Unclear" | Status is conflict, Reported (device program wound down in 2025). A Workbench Standard account to analyse PBHS Limited data needs no vendor contact. |
| 87 | PPG "Unclear (records heart rate, C)" | PPG present, 30 Hz (Verily-co-authored PBHS paper, Corroborated). |
| 110 | Samsung route "also via Verily Pre / Viewpoint Evidence (C)" | Reported, not Corroborated (MedCity paraphrase only). |
| 119 | Raw PPG waveform "Unclear" | The watch captured PPG at 30 Hz. Whether raw PPG reaches outside researchers is still unstated, since the paper used derived IBIs. So partly consistent; the cell could add "captured at 30 Hz". |
| 318 | 510(k)s (C) | Verified from FDA, three K numbers. |
| 342 | "weeks of onboard raw storage (C)"; "current status Unclear" | Up to a week. Status is conflict, Reported (device program wound down). |
| 413 | Verily: "Enterprise engagement only"; "Not procurable by an academic group"; cost "Not public" | Device: consistent. Platform: Workbench Standard is free and self-serve for individual researchers. |
| 253-table (compliance) | No Verily row | The record has a BAA self-claim (business associate for sponsors), DPF Verified (two entities), and ISO 27001 and SOC 2 self-claims covering Study Watch & Hub. |

## For the coordinator to check by hand

- Whether Verily will still supply Study Watch to new studies, and what Quipment's 2026-05-12
  listing means. Verily is the only party that can answer this.
- Which Galaxy Watch streams and rates Viewpoint delivers, and whether they are raw.
- Whether the PBHS Limited collection on Exchange includes Study Watch sensor data, and its date
  range.
- When Verily redeploys, update the build ID in all 16 `_next/data` fetch_urls.
- MD+DI answered 403 once and then 200 on retry. If the weekly job marks it unreachable, it's a
  transient bot block, not a dead page.
