# Labfront: gap hunter findings

Run date: 2026-10-11. Company id: labfront. KB files compared: `module-01-wearables/profiles/data-intermediaries.md` (Labfront section, lines 51 to 102), `module-01-wearables/comparison-matrix.md` (lines 184, 193, 207 to 208, 230, 337, 344, 360 to 361), `facts/labfront.yaml` (all fields unresearched).

All quotes below returned "exact" from `tools/facts/quote_probe.py` on 2026-10-11.

## Contradictions first

### 1. retention_terms: "unlimited data history" vs a typical 3-year retention after study completion
- **Found:** The pricing page sells Basic and Advanced with "Unlimited" data access history, but Labfront's data storage and trust pages say research data is typically kept 3 years after study completion, and that researchers can request deletion of all data. "Unlimited history" is a plan feature about how far back the dashboard reaches; it is not a storage guarantee. The KB reads it as the only retention statement.
- **URL:** https://labfront.com/research/data-storage (also https://labfront.com/trust-security)
- **Quote:** "We typically save research data for 3 years after study completion, following the write-up of the results"
- **Second quote:** "We provide the ability to delete all data if requested by the researcher as well"
- **Date:** accessed 2026-10-11 (pages undated)
- **Source type:** vendor_page
- **KB has it:** contradicts (by omission). `data-intermediaries.md` lines 70 to 71 say "Unlimited data history" with no retention limit; no 3-year term anywhere in the KB.

### 2. academic_vs_commercial / raw_streams: Basic plan has no beat-to-beat (BBI) data
- **Found:** The pricing comparison table lists Heart Rate Interval (BBI) as "Each beat" on Tester and Advanced and "N/A" on Basic. Basic also has no actigraphy and no accelerometer streaming; Advanced streams 3-axis accelerometry at 25, 50 or 100 Hz, Tester at 25 Hz. So the free Tester tier gets BBI but the $500 Basic tier does not. The KB says only "standard sampling rates" for Basic, and the comparison matrix line 208 sells "Garmin Enhanced BBI via ... Labfront" without a tier caveat.
- **URL:** https://www.labfront.com/pricing
- **Quote:** "Heart Rate Interval (BBl) Each beat N/A Each beat" (the page spells "BBl" with a lower-case L)
- **Second quote:** "3-Axis Accelerometer (Streaming) 25Hz N/A 25Hz , 50Hz, 100Hz"
- **Date:** accessed 2026-10-11
- **Source type:** vendor_page
- **KB has it:** no / partly contradicts. `data-intermediaries.md` line 70 ("standard sampling rates"); `comparison-matrix.md` line 208 has no tier caveat.

### 3. iso27001 / soc2: the SOC 1/2/3 claim is about AWS, not Labfront
- **Found:** One Labfront page says "Labfront adheres to ICH-GCP, HIPAA, SOC 1/2/3 and GDPR". The security blog makes clear the ISO 27001 and SOC 2 certificates belong to AWS data centres, and offers audit reports and compliance letters on request. I found no SOC 2 report or ISO 27001 certificate in Labfront's own name. Record soc2 and iso27001 as inherited from the hosting provider, not as Labfront attestations.
- **URL:** https://labfront.com/research/data-storage ; https://labfront.com/blog/strengthening-data-security-at-labfront
- **Quote:** "Labfront adheres to ICH-GCP, HIPAA, SOC 1/2/3 and GDPR"
- **Second quote:** "certified with ISO 27001 and SOC 2 standards" (in context: AWS data centres)
- **Third quote:** "We can also provide audit reports and compliance letters upon request"
- **Date:** blog dated 15 July 2025; pages accessed 2026-10-11
- **Source type:** vendor_page
- **KB has it:** no. No Labfront compliance claims anywhere in `data-intermediaries.md` or `comparison-matrix.md`.

### 4. ai_training_terms: privacy policy permits training ML models on data, and sharing de-identified data
- **Found:** The Kiipo Co. (d/b/a Labfront) privacy policy, updated 30 December 2025, says it uses data to train its machine-learning models and may share anonymous, aggregated or de-identified data with third parties. The policy's scope explicitly includes study participants. Researchers who need to forbid secondary use would need a contract term. This is the kind of term the knowledge base flags for other vendors.
- **URL:** https://help.labfront.com/privacy-policy
- **Quote:** "provide, operate and improve the Service, including by using data to train our machine learning models"
- **Second quote:** "We also use data to train and improve our machine learning models"
- **Third quote:** "We may use this anonymous, aggregated or de-identified data and share it with third parties"
- **Date:** policy effective 5 August 2022, DPF statement "Updated: December 30, 2025"; accessed 2026-10-11
- **Source type:** vendor_legal
- **KB has it:** no.

## Missing programs

### 5. research_program: Labfront Collaborator Program (free, institution-level)
- **Found:** A no-cost program for academic institutions. It offers collaborator-only grants, discounts, analytics guidance, custom webinars, a device loaner scheme ("test wearable devices firsthand") and a dedicated liaison. Applying means filling in a form, and selection is not guaranteed ("If selected").
- **URL:** https://www.labfront.com/collaborator-program
- **Quote:** "Any academic institution is welcome to register and become part of the Labfront Collaborator Program"
- **Second quote:** "Test wearable devices firsthand before making a commitment"
- **Date:** undated page, accessed 2026-10-11
- **Source type:** vendor_page
- **KB has it:** no.

### 6. research_program / program_status: current grants now have fixed deadlines, and one is a Garmin-co-branded CIRQA grant
- **Found:** The KB describes grants as "rolling". The grants page now lists dated calls:
  - 2026 Labfront x Garmin Health Research Grant, built around the Garmin CIRQA Smart Band: five bands, one year of Advanced, a standard analytics package; value $5,500; deadline 2 November 2026; past recipients excluded.
  - 2026 Sleep Science Research Grant: deadline 27 November 2026.
  - 2026 Aging Science Research Grant: deadline 7 December 2026.
  - APS mid-career educator award, each January.
  - "Institutional grants" for Harvard, Cleveland Clinic, Johns Hopkins, Stanford and Mayo, listed as ongoing but with blank details.
  
  Rounds closed in 2026 include a Labfront x Zana multimodal (wearable plus voice biomarker) grant with a 9 June 2026 deadline, plus Diabetes, Behavioral Medicine, and Sport and Exercise Science grants with awardees posted June to September 2026. The pricing FAQ still says grants "run year-round".
- **URL:** https://www.labfront.com/grant ; https://www.labfront.com/blog/multimodal-digital-biomarkers-grant ; https://www.labfront.com/pricing
- **Quote:** "5 x Garmin CIRQA Smart Bands from Garmin 1-year access to a Labfront Advanced account (incl. 20 participants)"
- **Second quote:** "Previous recipients of a Labfront x Garmin Health Research Grant are not eligible to apply for this grant"
- **Third quote:** "Deadline: June 9, 2026" (Zana post, dated 9 March 2026)
- **Fourth quote:** "Labfront grants run year-round" (pricing FAQ)
- **Date:** accessed 2026-10-11
- **Source type:** vendor_page
- **KB has it:** partly. `data-intermediaries.md` lines 74 to 77 mention the programme generically ("rolling basis", SRS Foundation and ACSM examples); no Garmin co-branded grant, CIRQA, Zana or current deadlines. `garmin.md` line 98 says Garmin research grants run with Fitrockr, and misses that Garmin Health also co-brands a Labfront grant.

## Other gaps

### 7. gdpr_statement / data_residency: EU-U.S., UK and Swiss DPF self-certification; US-only hosting in Virginia; EU servers promised
- **Found:** The privacy policy's DPF statement (updated 30 December 2025) says Kiipo Co. complies with the EU-U.S. DPF, the UK Extension and the Swiss-U.S. DPF. Data is stored only in US data centres in Virginia, and EU servers are promised with no date. The company is headquartered in the US and Taiwan. I could not confirm the DPF listing independently: dataprivacyframework.gov is a JavaScript app the probe cannot read.
- **URL:** https://help.labfront.com/privacy-policy ; https://labfront.com/research/data-storage ; https://labfront.com/trust-security
- **Quote:** "Kiipo Co. (d/b/a Labfront) complies with the EU-U.S. Data Privacy Framework (EU-U.S. DPF)"
- **Second quote:** "We currently only support U.S. data centers and the data is stored in Virginia, America"
- **Third quote:** "will be opening up new EU servers"
- **Fourth quote:** "We are headquartered in the United States and Taiwan and have service providers in multiple countries"
- **Date:** accessed 2026-10-11
- **Source type:** vendor_legal / vendor_page
- **KB has it:** no.

### 8. Compliance evidence: GovRAMP (formerly StateRAMP) membership only, not on GovRAMP's participant list
- **Found:** Labfront's trust page shows a StateRAMP badge, and its July 2025 blog calls this a "membership". GovRAMP's own spotlight (9 December 2024) says only that Labfront "joined" GovRAMP and gives no status level (Core, Ready, Provisional, Authorized). The spotlight's URL slug says "certification". I downloaded GovRAMP's Program Participants list page (about 3.2 MB, 427 table rows, includes e.g. Butterfly Network). It contains neither "Labfront" nor "Kiipo". Treat as membership, not authorization. Labfront also says it has completed a HECVAT, available from support.
- **URL:** https://govramp.org/member-spotlights/labfront-elevating-health-research-security-with-stateramp-certification ; https://govramp.org/product-list/ ; https://labfront.com/trust-security ; https://labfront.com/research/data-storage
- **Quote:** "Labfront joined GovRAMP to affirm our commitment to the highest standards of cybersecurity"
- **Second quote:** "Cybersecurity framework ensuring US cloud service security and compliance" (trust page StateRAMP badge)
- **Third quote:** "Yes, we have completed the HECVAT form that many higher institutions use"
- **Date:** spotlight 2024-12-09; registry checked 2026-10-11
- **Source type:** certificate (registry, by absence) / secondary / vendor_page
- **KB has it:** no.

### 9. baa / hipaa_statement: HIPAA claims, no published BAA
- **Found:** Labfront claims HIPAA compliance (data-storage, trust pages). Its stated model is to limit PHI by assigning participant codes, without storing participant personal details. I found no published BAA template and no third party mentioning one. The pricing page FAQ does not cover a BAA. Record baa as not_public. Note a tension: the PMC paper below created Garmin accounts "with deidentified information", consistent with that model.
- **URL:** https://labfront.com/research/data-storage
- **Quote:** "Labfront adheres to ICH-GCP, HIPAA, SOC 1/2/3 and GDPR"
- **Date:** accessed 2026-10-11
- **Source type:** vendor_page
- **KB has it:** no.

### 10. raw_streams / export_routes: Garmin CIRQA Smart Band now supported; KB device list is stale
- **Found:** The compatible-devices page lists the Garmin CIRQA Smart Band (Garmin's screen-free band, announced July 2026) alongside vívosmart 5, vívoactive 5, Index BPM, Index S2 and Movesense HR2. It also says all Garmin devices, including older models, work through the Garmin Connect route. The Garmin grant page notes that CIRQA bands are consumer wellness devices, not medical devices.
- **URL:** https://www.labfront.com/compatible-devices
- **Quote:** "Garmin CIRQA Smart Band"
- **Date:** accessed 2026-10-11
- **Source type:** vendor_page
- **KB has it:** no. `data-intermediaries.md` line 59 lists four Garmin devices without CIRQA.

### 11. history_depth: "Retroactive Garmin Data Access" on paid plans only
- **Found:** The pricing table has a row "Retroactive Garmin Data Access", marked N/A on Tester and included on Basic and Advanced. The help centre does not say how far back retroactive access reaches. It is presumably data recorded on the participant's Garmin Connect account before enrolment, but that is an inference.
- **URL:** https://www.labfront.com/pricing
- **Quote:** "Retroactive Garmin Data Access"
- **Date:** accessed 2026-10-11
- **Source type:** vendor_page
- **KB has it:** no.

### 12. program_application (Dexcom): per-project Dexcom approval gates go-live
- **Found:** Adding Dexcom requires Dexcom to approve each project, and the project cannot go live until it does. No timeline is given. Fitrockr documents the same per-study Dexcom approval, which suggests it is Dexcom's policy rather than Labfront's.
- **URL:** https://help.labfront.com/add-dexcom-to-labfront
- **Quote:** "While awaiting Dexcom's approval, your project will not be able to go live"
- **Date:** undated, accessed 2026-10-11
- **Source type:** vendor_docs
- **KB has it:** no. `data-intermediaries.md` line 59 lists Dexcom G7 with no approval caveat.

### 13. export_routes (operations): published deployment needed two apps synced daily, plus a Garmin Connect account
- **Found:** Holmqvist et al. 2025 (JMIR Human Factors, PMC12015335): 44 older adults, Garmin Vivosmart 4 plus Labfront, 4 weeks. A Garmin Connect account was created per participant, and participants synced both the Labfront and Garmin apps daily. Adherence was high (about 20 h per day wear, 93% EMA response per the preprint). This is evidence of how researchers actually ran the data path. The help centre confirms that data types and rates depend on the source (Garmin Connect, Labfront Companion or both).
- **URL:** https://pmc.ncbi.nlm.nih.gov/articles/PMC12015335/
- **Quote:** "Sync Labfront and Garmin apps once a day"
- **Second quote:** "A Garmin account was created for each participant using the Garmin Connect mobile app on their smartphone with deidentified information"
- **Date:** published 2025-04-08
- **Source type:** paper
- **KB has it:** partly. Listed as a candidate in `module-03-applied-studies/_across-the-board-scan-2026-09.md` line 119 and `_device-side-scan-2026-09.md` line 91; no profile, and not in `data-intermediaries.md`.

### 14. KB internal inconsistency (Movesense models)
- **Found:** Labfront's compatible-devices page names only Movesense HR2. `movesense.md` lines 83 and 195 say Labfront supports Movesense MD, HR2 and Flash (citing the Labfront help page), while `data-intermediaries.md` line 59 says HR2 only. One of them needs reconciling against help.labfront.com/movesense-overview.
- **URL:** https://www.labfront.com/compatible-devices
- **Quote:** "Garmin CIRQA Smart Band" (same device list; HR2 is the only Movesense model on it)
- **Date:** accessed 2026-10-11
- **Source type:** vendor_page
- **KB has it:** contradicts internally (`movesense.md` lines 83, 195 vs `data-intermediaries.md` line 59).

## Searched, nothing found
- FDA clearances: Labfront is software for research data collection; no 510(k) or De Novo under Labfront or Kiipo expected or found. fda_clearances should be not_applicable for Labfront itself; the Garmin Index BPM's status belongs to Garmin.
- SOC 2 or ISO 27001 report or certificate in Labfront's or Kiipo's own name: none found (see finding 3).
- Published BAA or DPA template: none found; no partner or university page mentions a signed Labfront BAA.
- dataprivacyframework.gov listing for Kiipo: could not be read (JavaScript app), so the DPF claim rests on the vendor's statement.
- Developer Access (Beta) documentation: `labfront.com/developer-access` returns 404; no public API docs, rate limits or GitHub repo found. Only the pricing line "Starting from $4000" (Advanced only), which the KB already has.
- JITAI product page: `/research/jitai` 404; JITAI appears only as a navigation item.
- Pricing changes in the last 12 months: none beyond what the KB recorded 2026-10-10. Capterra's "$495 per year" listing is a stale third-party figure.
- Shutdowns, deprecations, Garmin API pause effect on Labfront: nothing published. Labfront's route is the Health SDK partnership, which the pause on new Connect Developer Program applicants does not obviously touch.
- Funding or ownership changes: nothing after the 2022 pre-seed and 500 Global Taiwan accelerator round.
- App stores: Labfront Companion on iOS and Android (help page says iOS 14.1+, Android 8.0+ with Google Play); no store-level issues found.
- Integrator pages (Terra, Thryve, Fitabase) mentioning Labfront: none relevant.
