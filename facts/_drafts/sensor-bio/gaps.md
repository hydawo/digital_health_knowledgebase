# Gap hunt: sensor-bio (Sensor Bio, formerly Biostrap)

Run date: 2026-10-11. All quotes below returned "exact" from `tools/facts/quote_probe.py` on 2026-10-11.
KB files compared: `module-01-wearables/profiles/emerging-platforms.md` (Biostrap section, lines 49-85),
`module-01-wearables/comparison-matrix.md`, `facts/sensor-bio.yaml` (all fields unresearched),
`shared/unresolved-questions.md` line 281 (Q68).

The main finding: Sensor Bio now publishes a full V2 product specification page
(https://sensorbio.com/product/sensor-bio-v2/, in the sitemap but not in the record's watch list)
that answers several things the KB calls "undocumented" or "not published". It is a vendor page, so
capability claims stay vendor statements, but the KB's "no Hz figures published" is now wrong.

---

## Contradictions

### 1. sampling_rates: Hz figures are now published (KB says none)
- **Found:** V2 samples PPG at 50 Hz by default, configurable to 25 or 100 Hz per organization; raw export up to 100 Hz; duty cycle configurable.
- **URL:** https://sensorbio.com/product/sensor-bio-v2/
- **Quote:** "50 Hz by default, configurable to 25 or 100 Hz per organization"
- **Date:** page undated (accessed 2026-10-11)
- **Source type:** vendor_docs (product specification page)
- **KB has it:** contradicts. `emerging-platforms.md` line 82 "Sampling rates undocumented (configurable per the research page, but no Hz figures)"; `comparison-matrix.md` lines 112 ("no Hz figures published") and 335 ("no Hz figures"); `shared/unresolved-questions.md` line 281 (Q68 still open on Hz figures).
- **Related conflict, same vendor:** the AHA press release on Sensor Bio's own site says the platform "captures raw physiological signals at 15,000 samples per second". This conflicts with the spec page's 100 Hz maximum; the figure is unexplained (possibly an ADC or aggregate rate). Quote confirmed exact at https://sensorbio.com/press/sensor-bio-joins-innovators-network-at-american-heart-association-center-for-hea/ (May 6, 2026, secondary/press on vendor site). Record as a conflict, not a fact.

### 2. fda_clearances: current device is explicitly not FDA cleared; no Biostrap/Sensr/Sensor Bio 510(k) found
- **Found:** The V2 spec page states the product is a general wellness device, not FDA cleared. openFDA 510(k) and registration/listing searches on applicant names "biostrap", "sensr", "sensor bio" and "sensorbio" return no matches. The App Store listing repeats the not-a-medical-device disclaimer.
- **URL:** https://sensorbio.com/product/sensor-bio-v2/ ; https://api.fda.gov/device/510k.json?search=applicant:%22biostrap%22 ; https://apps.apple.com/app/id6745620963
- **Quotes:** "Sensor Bio V2 is a general wellness device. It is not FDA cleared or approved, and it is not intended for diagnostic use." / App Store: "Sensor Bio wearables are not medical devices and are meant only for general fitness/wellness purposes."
- **Date:** accessed 2026-10-11 (openFDA query returned NOT_FOUND; no quote possible for a negative result)
- **Source type:** vendor_docs; regulator_db (negative search); app_store
- **KB has it:** partly contradicts. `emerging-platforms.md` line 54 lists the "**Thermo Patch** (FDA-cleared continuous temperature, ±0.1 °C)" as **Corroborated**. The only source is Biostrap's research page ("Continuous body temperature FDA Cleared CE Mark High Accuracy (±0.1° C)", confirmed exact at https://biostrap.com/research/). No FDA record ties a clearance to Biostrap; the patch is likely a third-party device whose maker holds any clearance. The KB should not let the patch's claim read as a Sensor Bio clearance, and should state that the core wrist device is not cleared.

### 3. raw_streams: current V2 has no gyroscope (KB lists raw gyroscope)
- **Found:** V2 lists three sensors: PPG, accelerometer, skin temperature. No gyroscope.
- **URL:** https://sensorbio.com/product/sensor-bio-v2/
- **Quote:** "Three sensors: multi-wavelength PPG, three-axis accelerometer, skin temperature"
- **Date:** accessed 2026-10-11
- **Source type:** vendor_docs
- **KB has it:** contradicts for the current device. `emerging-platforms.md` line 55 and `comparison-matrix.md` line 112 cite the older Biostrap research page's "PPG, gyroscope, and accelerometer". That may be true of legacy Biostrap hardware; the profile should say which device.

### 4. academic_vs_commercial / api_platform_fees: raw waveform export gated to enterprise tier (vendor pages disagree with each other)
- **Found:** The V2 spec page says raw export is enterprise-tier only; Sensor Bio's own Polar comparison page says raw export is the default for every partner with no gated tier.
- **URLs:** https://sensorbio.com/product/sensor-bio-v2/ ; https://sensorbio.com/comparison/sensor-bio-v2-vs-polar-360/
- **Quotes:** "Raw data export is available to partners, gated to enterprise-tier accounts" / "Raw waveform export is the default data product for every partner, not a gated upsell." and "No separate license. No gated tier."
- **Date:** accessed 2026-10-11
- **Source type:** vendor_docs; vendor_page
- **KB has it:** no. KB (line 55, line 76-79) presents raw PPG access as generally available to researchers. This is a conflict to record and a question for the vendor (which tier academic studies land in).

## Missing programs and organisational changes

### 5. program_status / deprecations: leadership change and legacy-device continuity pages
- **Found:** Bruce Smith (Hydrow founder) named CEO, Feb 19, 2026. Sensor Bio runs "continuity" pages for Biostrap, Biostrap Evo and Biostrap Kairos users, routing them to Sensor Bio support. The CEO release mentions V2 and V3 devices.
- **URLs:** https://sensorbio.com/press/hydrow-founder-bruce-smith-named-ceo-of-sensor-bio-to-scale-global-preventive-he/ ; https://sensorbio.com/biostrap-kairos/ ; https://sensorbio.com/biostrap-evo/ ; https://sensorbio.com/biostrap-is-now-sensor-bio/
- **Quotes:** "Sensor Bio today announced the appointment of Bruce Smith, founder and former CEO of Hydrow, as Chief Executive Officer." / "We're experiencing incredible demand for our V2 and V3 devices."
- **Date:** 2026-02-19 (press release); continuity pages sitemap lastmod 2026-05-13 and 2026-06-04
- **Source type:** vendor_page (press release on vendor site)
- **KB has it:** no. KB records the rebrand only. The KB's device list (wrist biosensor, Activity Pod, Thermo Patch) does not name V2 (model S2001) or V3; whether Kairos/Evo are still sold or only supported is not stated anywhere found.

### 6. research_program: American Heart Association Innovators' Network membership
- **Found:** Sensor Bio joined the AHA Center for Health Technology & Innovation Innovators' Network (May 6, 2026). Not a research access program for outside researchers, but a partnership relevant to outcome-study building.
- **URL:** https://sensorbio.com/press/sensor-bio-joins-innovators-network-at-american-heart-association-center-for-hea/
- **Quote:** "has joined the American Heart Association Center for Health Technology & Innovation's (the Center) Innovators' Network"
- **Date:** 2026-05-06
- **Source type:** vendor_page (press release)
- **KB has it:** no.

### 7. export_routes: third-party integrator routes (Terra, Labfront) and legacy org-token REST API
- **Found:** Terra lists a Biostrap web API integration; Labfront announced (Jan 2024) integrating Biostrap Kairos data and a PPG service called Biostrap Waveshape; the legacy Biostrap partnerships page describes a REST API with an organization token for group data. Whether these routes survive the Sensor Bio transition is unknown.
- **URLs:** https://tryterra.co/integrations/biostrap ; https://www.labfront.com/blog/labfront-x-biostrap-enhanced-ppg-data-access ; https://biostrap.com/partnerships/
- **Quotes:** "With Terra's Biostrap web API integration, you can use the Terra web API to retrieve various essential health metrics & body measurements from your users' biostraps" / "integrating Biostrap Kairos data into the Labfront platform" / "We will issue you a special organization token allowing you will be able to retrieve a group of users’ data."
- **Date:** Labfront blog Jan 2024 (per search snippet; date not on the probed text); others undated, accessed 2026-10-11
- **Source type:** secondary (integrator pages); vendor_page (partnerships)
- **KB has it:** no. Neither the Biostrap section nor the comparison matrix mentions Terra or Labfront routes. Worth checking `facts/_drafts/terra/` (it mentions Biostrap) and the Labfront profile for consistency.

## Data access details the KB lacks

### 8. export_routes / history_depth: export windows, formats, file size, SDK version
- **Found:** Raw export window 1 to 7 days; computed metrics 1 to 30 days; CSV or JSON up to 2 GB per file; SDK has 8 data categories including a real-time live stream; SDK interface version cited.
- **URL:** https://sensorbio.com/product/sensor-bio-v2/
- **Quotes:** "Raw sensor metrics export across a 1 to 7 day window" / "Computed metrics export across a 1 to 30 day window" / "CSV or JSON, up to 2 GB per file" / "Compiled from the SensorBio SDK interface, v0.17.0." / "During an active recording session the band streams HR, HRV, respiratory rate, beat-to-beat intervals, raw PPG, signal-to-noise ratio, and motion."
- **Date:** accessed 2026-10-11
- **Source type:** vendor_docs
- **KB has it:** no. KB says "API or Bluetooth SDKs" (Reported) only.

### 9. retention_terms / history_depth / data_residency
- **Found:** Retention configured per deployment; cloud hosted on AWS; on-device buffer about 14 days, oldest data overwritten.
- **URL:** https://sensorbio.com/product/sensor-bio-v2/
- **Quotes:** "Configured per deployment to retain the history the partner actually needs" / "Sensor Bio cloud platform, hosted on AWS" / "Approximately 14 days of data at default duty-cycled sampling, overwriting oldest data when full"
- **Date:** accessed 2026-10-11
- **Source type:** vendor_docs
- **KB has it:** no. KB line 78 says retention is not published. AWS region not stated.

### 10. quote_required / device_price: sold through partnership; a per-unit hardware cost figure exists
- **Found:** V2 is not sold at checkout. The AHA release states an $80 per-unit hardware cost (a cost-of-goods framing aimed at investors, not a list price).
- **URLs:** https://sensorbio.com/product/sensor-bio-v2/ ; https://sensorbio.com/press/sensor-bio-joins-innovators-network-at-american-heart-association-center-for-hea/
- **Quotes:** "V2 is sold through partnership, not checkout." / "With a hardware cost of $80 per unit and a 76% gross margin at launch"
- **Date:** 2026-05-06 (release); spec page accessed 2026-10-11
- **Source type:** vendor_docs; vendor_page
- **KB has it:** partly. KB line 60 says pricing not public, demo only (consistent). The $80 figure is absent; it is not a researcher price and should not be recorded as device_price without that caveat.

## Compliance and terms

### 11. dpa / gdpr_statement / ai_training_terms: consumer privacy policy and terms still carry the Sensr legacy text
- **Found:** Privacy policy and terms are effective April 24, 2025. Terms name the contracting party as Sensr Biotech, INC.; the App Store seller is Sensr Biotech, LLC; the site footer says Sensor Bio Inc. The privacy policy still points to an EU-US Privacy Shield dispute provider (Privacy Shield was invalidated in 2020), allows sharing aggregated or de-identified data, including to advertisers, and asks explicit GDPR consent for health data. No HIPAA, BAA, AI-training or model-training language was found in either document.
- **URLs:** https://sensorbio.com/privacy-policy/ ; https://sensorbio.com/terms-and-conditions/ ; https://apps.apple.com/app/id6745620963
- **Quotes:** "Effective: April 24, 2025" / "We may share non-personal information that is aggregated or de-identified so that it cannot reasonably be used to identify an individual." / "advertisers and other third parties for general marketing and promotional purposes" / "https://www.jamsadr.com/eu-us-privacy-shield" / "we ask for your explicit consent to process the data" / "These Terms and Conditions of Use (the "Terms") are a legal agreement between Sensr Biotech, INC." / "Sensr Biotech, LLC"
- **Date:** effective 2025-04-24; accessed 2026-10-11
- **Source type:** vendor_legal; app_store
- **KB has it:** no. KB has only the HIPAA marketing claim (line 61). The entity mismatch (Sensr Biotech INC vs LLC vs Sensor Bio Inc.) matters for who signs a DPA or BAA.

### 12. fda_clearances (other regimes): CE, UKCA and FCC for V2
- **Found:** V2 claims CE and UKCA certification; FCC ID 2BTF2-S2001 (listed on the same page, not checked against the FCC database in this run).
- **URL:** https://sensorbio.com/product/sensor-bio-v2/
- **Quote:** "CE and UKCA certified"
- **Date:** accessed 2026-10-11
- **Source type:** vendor_docs
- **KB has it:** no. Note CE here reads as radio/product conformity for a wellness device, not MDR.

## Evidence

### 13. Validation: 2025 independent-ish Kairos HRV validation (Flatt et al., Sensors)
- **Found:** Kairos Spot Check HRV vs ECG, young adults, supine n=32 and seated n=30, with skin pigmentation analysis. Senior author had 2018 consulting payments from Biostrap; one device supplied by Biostrap.
- **URL:** https://pmc.ncbi.nlm.nih.gov/articles/PMC12115943 (Sensors 2025;25(10):3165, doi:10.3390/s25103165)
- **Quotes:** "Simultaneous 3 min Kairos and ECG samples were obtained in the supine (n = 32) and seated (n = 30) position." / "The senior investigator (A.A.F.) received payment from Biostrap for two educational consulting projects that occurred in 2018."
- **Date:** 2025-05-17
- **Source type:** paper
- **KB has it:** no. KB line 83 says "the most recent registered trial located dates from 2022", and no file in the KB mentions Kairos or Flatt. Also relevant to Module 1's literature library.

### 14. Vendor-claimed validation count changed
- **Found:** AHA release cites 29 peer-reviewed studies, versus the "14 publications and 22 clinical studies" in the KB.
- **URL:** https://sensorbio.com/press/sensor-bio-joins-innovators-network-at-american-heart-association-center-for-hea/
- **Quote:** "The platform has been validated across 29 peer-reviewed studies"
- **Date:** 2026-05-06
- **Source type:** vendor_page
- **KB has it:** contradicts (vendor-compiled counts differ). `emerging-platforms.md` line 59. Both remain vendor-compiled.

---

## Searched, nothing found
- openFDA 510(k) and registration/listing for applicants Biostrap, Sensr, Sensor Bio, SensorBio: no matches (2026-10-11).
- FDA warning letters, recalls: none surfaced in web search.
- Trust portal, SOC 2, ISO 27001 certificate, published BAA or DPA: none found on sensorbio.com (sitemap reviewed in full) or in search.
- A formal academic or research access program, grants or academic pricing: none; only the "Research" marketing block and demo form.
- Developer docs, public API reference, GitHub repo or public SDK package: none found; the V2 page summarises an SDK v0.17.0 but no public docs.
- Google Play listing for the Sensor Bio app: not found in search (iOS listing exists, seller Sensr Biotech, LLC).
- Fitabase, Thryve integrations for Biostrap or Sensor Bio: not found. Spike API and Sahha list Biostrap connectors (not quote-probed; lower value).
- A reported WHOOP acquisition of Biostrap (single low-authority directory) is not supported by any primary source and conflicts with the Sensor Bio continuity pages; not recorded.
- Job postings and conference talks: nothing researcher-relevant found.
- Not probed: the Ken Nelson advisory board (2026-07-09) and Dr Michael Poku clinical advisor (2026-06-08) press pages; FCC ID database entry; sensorbio.com/science/ and /manuals/v2/ (worth adding to the watch list along with /product/sensor-bio-v2/ and /privacy-policy/).
