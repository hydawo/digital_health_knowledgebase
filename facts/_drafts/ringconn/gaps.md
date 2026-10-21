# Gap hunter: RingConn (Shenzhen Ninenovo Technology)

Run date: 2026-10-21. Scope: sources outside the official docs the two researchers cover, compared against
`module-01-wearables/profiles/emerging-platforms.md` (RingConn row, line 134), `module-01-wearables/comparison-matrix.md`
(no RingConn entry), `module-01-wearables/sources.md` (lines 307 to 308), `shared/unresolved-questions.md` (Q50, line 333)
and `facts/ringconn.yaml` (every field `unresearched`). All quotes below returned "exact" from `tools/facts/quote_probe.py`.

Note on the 2026-10-17 rewrites. The Wayback Machine holds no capture of
`/blogs/news/smart-ring-health-data-security` in any language (checked en, de, es, fr via the availability API on
2026-10-21; the de, es and ko pages now serve the same rewritten English text). So the pre-rewrite wording of that
article cannot be checked against an archive; the knowledge base itself never cited it. The business article does
have captures (2024-07-16 to 2025-11-25), and finding 2 uses the 2025-11-25 one.

---

## Contradictions and missing programs

### 1. FDA 510(k) K260490 for a Ninenovo SpO2 ring (fda_clearances)
- **Found:** Shenzhen Ninenovo received 510(k) K260490, decision 2026-10-02 (received 2026-02-13), product code DQA
  (oximeter), "Substantially Equivalent". The cleared device is named "Ninenovo Blood Oxygen Ring" with model numbers
  BORMB-01-6 to BORMB-01-14, not "RingConn Gen 3". Which consumer ring, firmware or app build corresponds to the cleared
  device is not stated anywhere I found. Company announced it by PR Newswire on 2026-10-10 and says clinical validation
  work is ongoing.
- **URL (regulator):** https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K260490 (probed via
  https://api.fda.gov/device/510k.json?search=k_number:K260490)
- **Quote:** "Ninenovo Blood Oxygen Ring"
- **URL (press release repost):** https://technode.global/?p=994924
- **Quote:** "RingConn continues to conduct clinical research related to blood oxygen monitoring, building a solid data foundation for clinical validation of the product."
- **Date:** decision 2026-10-02; announced 2026-10-10. **Source type:** regulator_db; secondary (press release repost).
- **Japan angle:** a Japanese trade article quotes RingConn Japan that the clearance does not change the product's
  status in Japan, where it is not a medical device. URL https://www.smartwatchlife.jp/83508/ , quote
  "今回のFDAのクリアランスによって、日本での位置づけが変わるわけではありません。" (secondary).
- **KB has it:** no. `emerging-platforms.md` line 134 and Q50 say nothing about FDA status; `facts/ringconn.yaml`
  `fda_clearances` is unresearched. Researcher draft A already cites K260490, so this is a KB gap rather than a draft gap.

### 2. Institutional partnership offer existed before the 2026-10-17 rewrite and is now gone (research_program, program_status)
- **Found:** the Wayback capture of the business article from 2025-11-25 had an "Educational and Government
  Partnerships" section inviting schools, government agencies and institutions to integrate the ring into their
  programs, explicitly including "data analytics", routed to business@ringconn.com. The live page (Updated October 17,
  2026) no longer contains that sentence (probe: missing). The same capture carried a site banner "RingConn is HSA/FSA
  eligible."
- **URL:** https://web.archive.org/web/20251125062457/https://ringconn.com/blogs/news/feedback-and-business-collaboration-with-ringconn
- **Quote:** "We seek partnerships with schools, government agencies, and institutions to integrate smart ring technology into their programs, enhancing health monitoring, data analytics, and personal tracking."
- **Date:** captured 2025-11-25; removed by 2026-10-17. **Source type:** vendor_page (archived).
- **KB has it:** no. `emerging-platforms.md` line 130 says RingConn publishes no research programme "as checked
  2026-10-09", and Q50 (`shared/unresolved-questions.md` line 333) names support@ringconn.com as the contact. Neither
  mentions that an institutional partnership route, with business@ringconn.com as its address, was published until
  October 2026. The KB conclusion (no formal programme) still holds; the contact address in Q50 is the weaker one and
  the narrowing should be recorded as a change.

### 3. Company-assisted raw PPG export at 100 Hz exists for research, via customised firmware and app (raw_streams, sampling_rates, academic_vs_commercial)
- **Found:** a 2026 method-comparison study (64 shooting athletes, RingConn Gen 2 vs Polar H10; preprint on Research
  Square, version of record in BMC Sports Science, Medicine and Rehabilitation, 2026-08-18, DOI 10.1186/s13102-026-01960-x)
  used raw green-channel finger PPG at 100 Hz to derive inter-beat intervals. The firmware and app build were customised
  for research export, three authors are Ninenovo/RingConn LLC staff, and the companies supplied equipment and technical
  support. This is the clearest evidence of how researchers actually got raw RingConn data: through the company, not a
  public route. It also shows the ring has green, red and infrared PPG channels.
- **URL:** https://doi.org/10.21203/rs.3.rs-9564367/v1 (probed against the preprint PDF
  https://assets-eu.researchsquare.com/files/rs-9564367/v1_covered_1d7f615a-644b-4b19-8b6f-9f1d301ef27f.pdf )
- **Quotes:** "The firmware and app build used for research data export were customized" ;
  "100 Hz, and ring sizes 6–14 were available" ; "only the green channel was used in the" ;
  "organizations provided equipment and technical support."
- **Date:** preprint 2026-06-11; journal 2026-08-18. **Source type:** paper.
- **KB has it:** contradicts in part. `emerging-platforms.md` line 134 says researchers get "summary metrics, not raw
  PPG". True for the consumer route, but the KB does not record that raw 100 Hz PPG has been released to research teams
  under a company collaboration. Worth adding as a company-mediated route, Reported, with the COI noted.

### 4. Apple Health sync is confirmed on a RingConn page (export_routes)
- **Found:** RingConn's own guide states the ring syncs with Apple Health and gives the HealthKit permission step. It
  does not list the HealthKit data types.
- **URL:** https://ringconn.com/blogs/guides/how-sync-health-and-sleep-tracker-data
- **Quotes:** "RingConn’s official materials say the ring can store up to seven days of data offline and can sync with Apple Health, Google Fit, and other platforms." ;
  "Grant Apple Health permission to read and/or receive the supported health categories you want to sync."
- **Date:** read 2026-10-21 (page undated). **Source type:** vendor_page.
- **KB has it:** contradicts. `emerging-platforms.md` line 134 rates Apple Health sync **Unclear**, "not confirmed on a
  RingConn page". It is now confirmed on one; the per-type list is still not public. Note the guide still names Google
  Fit, which RingConn stopped syncing on 2025-10-01.

## Other findings the KB lacks

### 5. Oura patent licence keeps RingConn on sale in the US (deprecations / availability)
- **Found:** in October 2025 Oura and RingConn settled the ITC dispute; RingConn pays royalties under a multi-year
  licence and avoided the import exclusion that hit Ultrahuman. Relevant to any US study planning multi-year RingConn
  supply. Licence length is confidential.
- **URL:** https://ouraring.com/blog/oura-itc-case/
- **Quote:** "ŌURA has granted RingConn a multi-year license to continue offering RingConn smart rings and their companion app, with RingConn making royalty payments to ŌURA."
- **Date:** 2025-10-21 (Oura blog "Updated October 21, 2025"); Wareable report 2025-10-22. **Source type:** secondary (competitor's own blog).
- **KB has it:** no for RingConn (`emerging-platforms.md` line 134 is silent). `facts/ultrahuman.yaml` line 701 cites
  a TechRadar piece that mentions RingConn only in passing.

### 6. The npj Digital Medicine paper: DOI and publication date (research evidence)
- **Found:** "Large-scale bilateral cardiovascular monitoring via wearable rings", npj Digital Medicine,
  DOI 10.1038/s41746-026-03036-z, published online 2026-07-21 per Crossref (the press release KB cites is dated
  2026-08-12).
- **URL:** https://doi.org/10.1038/s41746-026-03036-z (probed via https://api.crossref.org/works/10.1038/s41746-026-03036-z)
- **Quote:** "Large-scale bilateral cardiovascular monitoring via wearable rings"
- **Date:** 2026-07-21. **Source type:** paper (metadata).
- **KB has it:** partly. `sources.md` line 308 (S-EMG-10) and profile line 134 cite only the company press release;
  no DOI.

### 7. Independent academic deployment: 14-day RingConn Gen 2 plus CGM in older adults with T2D (research evidence, Module 3 candidate)
- **Found:** a Shanghai multicentre trial secondary analysis (preprint 2026-09-11) gave participants RingConn Gen 2
  alongside a CGM for 14 days and used the ring's app-derived sleep staging. No competing interests declared, but one
  author (Cheng Chen, SJTU) is also on the company-linked papers. How ring data left the app is not described.
- **URL:** https://doi.org/10.21203/rs.3.rs-10863852/v1 (probed against
  https://assets-eu.researchsquare.com/files/rs-10863852/v1/64747d9d-8367-4833-b555-5a1ff6d7a020.pdf )
- **Quote:** "Participants underwent 14-day of concurrent monitoring using a RingConn Gen2 (smart ring) and GS1 continuous glucose monitoring (CGM)."
- **Date:** 2026-09-11. **Source type:** paper (preprint).
- **KB has it:** no. Possible Module 3 `_scan-queue.md` candidate (not added; gap hunter writes only this file).

### 8. Community BLE client now works with no RingConn account or app, including on Gen 3 (export_routes, data_residency)
- **Found:** the OpenCircuit project says ring authentication is fully reverse-engineered, so it connects to Gen 2 and
  Gen 3 rings with no RingConn account, writing to Apple Health. Licence is PolyForm Noncommercial 1.0.0, which bars
  commercial use. It also asserts the official app stores data in RingConn's cloud on AWS in the UK (third-party claim,
  not a vendor statement).
- **URL:** https://github.com/perezjuanj/OpenCircuit/wiki
- **Quotes:** "so OpenCircuit connects and streams on its own, with no RingConn account or app ever needed" ;
  "License: LICENSE (PolyForm Noncommercial 1.0.0)" ; "The RingConn app sends your data to RingConn's cloud (AWS, UK)"
- **Date:** read 2026-10-21. **Source type:** repository.
- **KB has it:** partly. Profile line 134 mentions OpenCircuit as "not a supportable research route" but not the
  account-free operation, Gen 3 support, or the non-commercial licence. The AWS-UK claim should not be used for
  `data_residency` without a vendor source.

---

## Searched, nothing found
- Formal research, academic, grant or "for organizations" program (web search, sitemap via draft A, Wayback of business article): none, beyond the removed partnership paragraph.
- Public developer API, SDK, developer forum or changelog: none.
- Aggregators: RingConn not found on Terra (tryterra.co/integrations), Sahha SDK docs or Spike integrations page by text search; Thryve and ROOK integration URLs returned 404. These pages may render lists by script, so absence is Reported only.
- Gadgetbridge support for RingConn: not found.
- FDA clearance for sleep apnea or blood pressure features: none found; only K260490 (SpO2). No FDA warning letters found.
- Other openFDA registrations under "Ninenovo": none returned.
- Independent peer-reviewed validation of sleep or HR outside company-linked authors: none found in Europe PMC (10 hits for "RingConn"); the 2024 PSG accuracy study is an IEEE BioCAS conference paper (DOI 10.1109/biocas61083.2024.10798254) with a company author.
- I-SMART pregnancy trial (NCT05709327) surfaced in search but uses Oura, not RingConn.
- ISO 27001, SOC 2, trust portal, BAA or DPA evidence from third parties: none found.
- Job postings and conference talks: not searched in depth; nothing surfaced in general searches.
