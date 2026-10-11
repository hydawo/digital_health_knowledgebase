# Judgement: ametris-actigraph (2026-10-11)

Inputs: `A.yaml`, `B.yaml`, `gaps.md`. Output: `facts/ametris-actigraph.yaml`, 46 facts: 35 stated, 6 not_public,
3 unclear, 1 conflict, 1 not_applicable. Confidence: 35 Verified, 5 Corroborated, 3 Reported, 3 Unclear.
I probed all 90 quotes in the final record and every one came back `exact`. `validate.py --file` gives 46/46
researched and 0 errors. `weekly.py --only ametris-actigraph --no-state` checked 40 pages: 0 missing, 0 reworded,
0 dead, 0 check by hand. Watch list: 15 pages.

## The nine points the coordinator named

| # | Question | What the sources say | Decision |
|---|---|---|---|
| 1 | K080545 | openFDA k_number:K080545 returns "ACTITRAINER", applicant Actigraph, LLC, 2008-07-24, Traditional, product code ISD (Exerciser, Measuring, 890.5360). I downloaded the 510(k) summary PDF from accessdata.fda.gov with a browser user agent and read it with pdftotext. It names only the ActiTrainer, with predicate K040554 (the AM7164). The K181077 (Insight Watch) summary uses "ActiTrainer K080545" as its predicate, and the K231532 (LEAP) summary uses K181077. openFDA device_name searches for gt3x, gt9x and wgt3x return no matches. Applicant "actigraph" returns only K080545, K181077 and K231532. Ametris's compliance page says "K080545 - GT9X, wGT3X-BT". | **Split into two entries.** (a) K080545 is the ActiTrainer: Verified, regulator_db. (b) The claim that K080545 covers the GT9X and wGT3X-BT: stated as the vendor's claim, **Reported**, with the compliance-page quote and the openFDA record. Not a `conflict`, because the FDA record doesn't contradict the vendor. It just doesn't show modified devices, and a manufacturer can market a modified device under an existing 510(k) without the database recording it. The note adds Health Canada licence 102376, which lists both devices (from the gap hunter, regulator_db). It also asks Ametris which letter-to-file covers each device. A had put K080545 into a single Verified entry with the vendor's mapping in the value. B had a conflict entry at Unclear. Neither one separated what the FDA confirms from what only the vendor says. I also kept A's K040554 (AM7164) as its own Verified entry. |
| 2 | Data Vault storage | The ActiLife product page says "20GB of free Data Vault storage" in year-one maintenance. The ActiLife 7 upgrade FAQ lists "20GB of Datavault Storage" in the coverage plan. The ActiLife 7 User's Manual (Revision I, effective 2026-01-30, the manual the downloads page offers today) says "ActiLife 7 users receive 4GB of free space." | **Conflict**, scoped `ActiLife Data Vault storage`. A had this as a conflict and B had only the 20GB figure. All three sources are the vendor's own and current. One reading fits both numbers (4GB base, 20GB while covered), but no page says that, so it goes in the note as a possibility and the question goes to the vendor. |
| 3 | LEAP on-device storage | ametris.com/actigraph-leap has two spec blocks: "Data Storage: 30 Days / 1GB" and "Data Storage: 79 Days / 1GB". academic.ametris.com/actigraph-leap gives "1-79 Days / 1 GB" for all three configurations. The LEAP Instructions for Use (Model LEAP E.200.6025, Rev 3, released 2024-12-04) is attached to the Czech procurement record. It gives "Data Storage 79 Days / 1 GB*", and its footnote says this is at the default 32 Hz, accelerometer only. | **79 days, Corroborated.** The controlled document (the IFU) and every academic configuration agree on 79 days. The 30-day block has no footnote or condition, and nothing else supports it. The record cites the IFU (secondary, since it comes from a third-party copy), both vendor pages and the 79-day quote, and the note keeps the 30-day block. Not Verified, because the vendor's own page still contradicts itself. Battery stays at 1 to 32 days in `sampling_rates`, and the note says the IFU gives about 32 days. |
| 4 | SOC 2 Type II, 2023 | The only source is highperformr.ai, which summarizes an Oct 2023 PR Newswire release. Two web searches found no original release, auditor or report. The current compliance page has no SOC 2 text in its rendered page or its raw HTML. | **unclear, Reported** (A's version). B's `not_public` at Verified ignored a dated third-party report. Stating it as current would overstate it, because the claim is three years old, comes from an aggregator, and the current trust page is silent. |
| 5 | ISO/IEC 27001:2022 | The certificate PDF, linked from the compliance page, gives certificate number IA391-260410-001, issued by Ignyte Assurance LLC to "Actigraph L.L.C. dba Ametris", initial certification 16 April 2026, valid to 15 April 2029. | **Verified**, source type certificate (both researchers agreed). Four certificate quotes are probed exact. The note says the PDF is hosted by the vendor and that Ignyte's accreditation (ANAB or IAF) was not checked. |
| 6 | Czech LEAP quote | ProCare B.V. quotation 31576, dated 17-07-25, to Palacký University Olomouc: LEAP device CZK 15.625,00 for 190 units, a 3-year ActiLife 7 Single licence at CZK 136.750,00, a discount of CZK 1.067.025,00, and a total of CZK 2.489.725,00 excluding VAT. | **Added** as its own `device_price` scope ("ActiGraph LEAP, one reseller quote, Czech Republic, July 2025"): stated, **Reported**, source type secondary. Not converted to USD. The note says the roughly 30% discount applies to the whole order, so no per-device net price is stated. The vendor list-price entry stays `not_public`. The `academic_pricing` note points to the quote. |
| 7 | ActiLife perpetual, "legacy" yet updated | FAQ: "All active ActiLife licenses have been automatically converted to a perpetual license on July 30 th , 2025." Product page: "ActiLife 7 is Ametris' legacy data processing software". Downloads page: "v7.3.2.0 Release Date: May 8, 2026". FAQ: ActiLife 6 still works with GT3X and GT9X, and LEAP PPG can be processed only in ActiLife 7. | **All Verified, both facts kept.** The perpetual conversion goes in `api_platform_fees` (ActiLife licences). The "legacy" label and the 2026-05-08 release sit side by side in `deprecations` (ActiLife). I don't read "legacy" as end of support, since nothing gives a date. |
| 8 | Signant acquisition | The Signant release of 14 May 2026 says Signant "today announced its acquisition of Ametris". The definitive agreement was announced on 16 April 2026. Neither release uses the word "completed" or gives a closing date. | Recorded as **announced 2026-05-14**, Verified, with both releases quoted. The note says "completed in May 2026" is an inference, because the release never states a closing. B's draft had called it "completed". |
| 9 | HIPAA | The compliance page's raw HTML has one HIPAA reference: an `<img>` whose alt text is "HIPAA Compliant" (file `ametris_content_regulatory-icons_hippa-1.png`). There is no written statement in the page text or the privacy policy. | **unclear, Unclear** (A's version). B's `not_public` missed the badge. A badge's alt text is a claim, but it isn't page text, so it can't be quoted or probed. The note describes it. |

## Other places where A and B differed

| Field | A | B | Decision |
|---|---|---|---|
| research_program | Academic channel only | Same | Merged, and the gap hunter's Accelerant program added as its own scoped entry (B1, quotes exact). |
| program_eligibility | Store quotes | Store quotes | Merged, plus the LEAP "prescription use only" FAQ quote (gap C5). |
| program_application | Quote with markdown syntax, from the raw README | Rendered GitHub quote | B's quote, probed exact on the rendered page. |
| program_status | Signant quote | Ametris blog roadmap quote, "completed May 2026" | Union of both, plus the April agreement release; "completed" dropped (point 8). |
| user_cap | stated (ActiLife activation tiers) | not_public | Both, as scoped entries: ActiLife activation caps stated, CentrePoint not_public. |
| academic_vs_commercial | Corroborated | Verified | Verified. Every claim is quoted from the vendor's own pages, and they're facts about its own sales channels, not self-certifications. |
| device_price | not_public, Fibion figure in the note | not_public | not_public for list prices, plus the Czech quote scope (point 6). Fibion's US$600 is kept in a note only. |
| api_platform_fees (ActiLife) | Conflict (Data Vault) | Stated, 20GB | Split into licences (stated, perpetual) and Data Vault (conflict). |
| raw_streams | One entry | CentrePoint API and Devices scopes | B's scopes, plus A's microphone-off quote and the ActiLife 7 LEAP PPG quote (gap A3). |
| derived_metrics | Integration-guide quote, LEAP investigational status | README endpoint quotes | A's base, plus SpO2 listed (gap A2) and the algorithm marketplace (gap B3). |
| sampling_rates | One entry | Four scoped entries | B's scopes. A's 15/30/60-second epoch quote is added to the API scope. |
| history_depth | stated, LEAP "30 or 79 days" | unclear (cloud only) | Two scopes: on-device storage (stated, Corroborated, point 3) and CentrePoint cloud (unclear). |
| rate_limits | Includes the V2 daily limit | V3 only | A's version. |
| retention_terms | 30-day removal, sponsor routing | Typo quote, controller quote | Union of the three quotes. |
| ai_training_terms | not_public, Verified | not_public, Verified | not_public, lowered to **Corroborated**. It rests on absence, and the contracts weren't readable. This follows the Empatica precedent. |
| deprecations | One entry citing Fibion for GT9X | Three scoped entries | B's scopes. Fibion is replaced by Ametris's own GT9X FAQ ("As of August 23, 2023 ... discontinued", gap E1), and the 2026-05-08 release is added (point 7). |
| baa | not_public, Verified | not_public, Verified | Lowered to **Corroborated**. A BAA could exist in non-public contracts. |
| soc2 / hipaa_statement | unclear | not_public | A's version (points 4 and 9). |
| gdpr_statement | DPF quote from the privacy policy | DPF quote from the compliance page | A's privacy-policy quote ("has certified to the U.S. Department of Commerce"), which is the stronger wording. The DPF registry was not checked. |

## Gap-hunter findings

| Finding | Decision |
|---|---|
| A1 ISO 27001 certificate | Accepted (point 5). |
| A2 LEAP lists SpO2 and other vital signs as investigational | Accepted into `derived_metrics`. "Oxygen Saturation (SpO2)" and the 510(k)-scope sentence are both exact. |
| A3 ActiLife 7, perpetual licences, LEAP PPG | Accepted (`api_platform_fees`, `raw_streams`, `deprecations`). |
| A4 LEAP IFU, 79 days | Accepted (point 3). |
| B1 Accelerant Partnership Program | Accepted as a scoped `research_program` entry, and mentioned in `developer_program_status`. |
| B2 DECODE consortia | Mentioned only in a note. The only source is a republished release on a secondary site, and the consortia are pharma-only. |
| B3 Algorithm marketplace | Accepted. The Mobilise-D quote is exact, and the partner names are in the value. |
| B4 NHANES 2027-2030 LEAP | Note only, because it is the vendor's claim and not confirmed by CDC or NCHS. |
| B5 Signant CNS, AliveCor and Kayentis integrations | Note in `academic_vs_commercial`. The integration depth is not stated. |
| B6 China partnership | Note in `data_residency`. |
| C1 EU MDR Class I self-certified | Not recorded. The schema has no CE field, and it doesn't belong under `fda_clearances`. Profile follow-up. |
| C2 Health Canada licence 102376 | Used as supporting context in the wGT3X-BT/GT9X FDA note. I probed the MDALL API and the device dates match. |
| C3 MDSAP and ISO 13485, Intertek | Mentioned in the `iso27001` note. The certificate number mismatch the gap hunter flagged (-03 in the filename, -04 in the content) is not resolved. |
| C4 Biofourmis 510(k)s | Not recorded. The holder is Biofourmis Singapore and the transfer isn't shown, so these are not Ametris clearances on the record. Profile follow-up. |
| C5 Prescription use only | Accepted (`program_eligibility`). |
| D1 Czech quote | Accepted (point 6). |
| D2 Fibion LEAP US$600 | Rejected as a fact (an unverified competitor citing a forum post). Kept in a note. |
| E1 GT9X discontinued 2023-08-23 | Accepted, with the vendor source. |
| F1 Official GitHub tooling | Accepted into `export_routes` (GT3X-File-Format and pygt3x quotes exact, the others in a note). |
| F2 Privacy policy | Already covered by A and B. |
| F3 App Store, iOS 18 floor | Note in `export_routes`. Not quoted, since the app is a participant tool, not an export route. |
| F4 RADAR-base issue 153 | Note in `developer_program_status`. Read only. |
| G Corporate context (ArchiMed seller, StatCan) | Not recorded. The source is a paywalled headline or an unprobed search excerpt. |

## Statements in the profile and matrix that the record contradicts

Profile is `module-01-wearables/profiles/ametris-actigraph.md` (P). Matrix is `module-01-wearables/comparison-matrix.md` (M).

| File:line | What it says | What the record says |
|---|---|---|
| P:146, M:258 | FDA: K231532 and K181077 only | Also K080545 (ActiTrainer, 2008, ISD), which Ametris maps to the GT9X and wGT3X-BT (vendor claim, Reported), and K040554 (AM7164, inactive). K181077's predicate is K080545. |
| P:143, M:258, U:255 | ISO/IEC 27001:2022 "listed without a certificate (C)" | Certificate IA391-260410-001 from Ignyte Assurance, 2026-04-16 to 2029-04-15, Verified. |
| P:145, P:199, M:258, U:255 | No HIPAA statement and no SOC 2 statement found | HIPAA: the compliance page shows a "HIPAA Compliant" badge image with no written statement (unclear). SOC 2: an aggregator reports a 2023 SOC 2 Type II attestation, with no current evidence (unclear, Reported). |
| P:117 | ActiLife includes 20 GB of Data Vault storage | Conflict: 20GB (product page, FAQ) versus 4GB (ActiLife 7 manual, Rev I, 2026-01-30). |
| P:46, P:230 | ActiLife's ongoing status is an open question | ActiLife 7 is current (v7.3.2.0, 2026-05-08). All licences have been perpetual since 2025-07-30. Labelled "legacy" with no end-of-support date. |
| P:128, P:196, P:220 | A fully local, no-cloud workflow may not survive | ActiLife 7 still processes device files locally, including LEAP accelerometer and PPG data. Data Vault cloud storage is optional. |
| P:56, M:115 | Raw LEAP PPG is reachable through the CentrePoint API only | ActiLife 7 also processes LEAP PPG locally. LEAP PPG cannot be processed in ActiLife 6. |
| P:62, M:84 | LEAP SpO2: "No" | The LEAP page lists Oxygen Saturation (SpO2) among its investigational vital signs (Scientific Services required, not covered by the 510(k)). |
| P:69, P:228, M:213, U:401 | LEAP storage and battery: conflict, Unclear (30 or 79 days) | 79 days / 1 GB at the 32 Hz accelerometer-only default (IFU Rev 3 plus the academic page, Corroborated); battery 1 to 32 days, about 32 at the default. |
| P:150-161, M:234, U:254 | No price is published for the LEAP or ActiLife 7. All figures are competitor-sourced | One real dated price: CZK 15,625 per LEAP and CZK 136,750 for a 3-year ActiLife 7 Single licence (reseller quote, Czech Republic, 2025-07-17, Reported, before a roughly 30% order discount). |
| P:25, P:155, P:260 | GT9X end of life, sourced only to Fibion with no date | Ametris's own FAQ: new GT9X Link sales ended on 2023-08-23. |
| P:123 | The `.gt3x` format was "reverse-engineered/documented by the research community" | ActiGraph publishes the format itself (`actigraph/GT3X-File-Format`) and its own readers (`pygt3x`, `agcounts`). |
| P:93, M:191 | Integrated Signant ePRO: "Current availability is not established" | A combined Ametris DHT plus Signant eCOA offering for CNS trials was announced on 2026-03-10 (integration depth not stated). This is a note in the record, not a quoted fact. |
| P:7, P:24 | Wording matches ("acquisition announced 14 May 2026") | No contradiction. Text elsewhere that says "completed" would overstate it. |

## For the coordinator to check by hand

1. **K080545 mapping.** Only Ametris can say which letter-to-file or 510(k) covers the GT9X and wGT3X-BT. If the profile states FDA status for those devices, it should say "per Ametris".
2. **Ignyte Assurance accreditation** for ISO 27001 was not checked. If it isn't accredited by ANAB or another IAF member, consider lowering the confidence to Corroborated.
3. **Data Vault 4GB vs 20GB** needs a vendor answer.
4. **SOC 2.** Look for the Oct 2023 PR Newswire original, and ask Ametris for a current report.
5. **The Czech PDF** is a scanned, OCR'd document. The quotes probe exact against the text the tool extracts, but any change in OCR on that host would break them.
6. The profile's absence of CE/MDR (Class I self-certified LEAP) and of Health Canada licence 102376 is a profile gap, since the schema has no field for either.
