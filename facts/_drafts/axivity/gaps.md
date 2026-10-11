# Gap hunter: axivity (2026-10-11)

Company: Axivity Ltd (AX3, AX6, OmGui and the Open Movement tooling).
Compared against: `module-01-wearables/profiles/axivity-geneactiv.md` (cited as "profile"),
`module-01-wearables/comparison-matrix.md` ("matrix") and `facts/axivity.yaml` (every field still
`unresearched`, so nothing below is in the record yet).

Every quote was checked with `tools/facts/quote_probe.py` and returned "exact". Wayback quotes were
probed with `--fetch-url` pointing at the `id_` (raw) capture of the same snapshot.

Ordering: contradictions first, then missing programs and partners, then other gaps.

---

## Contradictions

### C1. AX3 and AX6 record light and temperature; the KB says only GENEActiv does
- **Schema field:** raw_streams (also sampling_rates)
- **Found:** Axivity's own product pages say the AX3 and AX6 carry a light sensor and a temperature sensor. The Open Movement docs say these auxiliary channels (light, device temperature, battery voltage) are always recorded alongside movement, sampled internally at 1 Hz and stored once per data sector. They export through OmGui, cwa-convert, and the MATLAB and Python loaders. The temperature is internal device temperature, used mainly for auto-calibration, and the light sensor reads through the case, so it is a relative indicator rather than calibrated lux.
- **URLs and quotes:**
  - https://axivity.com/product/ax3: "The light sensor can be used to help determine periods of wear as well as provide useful environmental data."
  - https://axivity.com/product/ax3: "The temperature sensor gives a rough sense of outside environment temperature and also if the sensor is being worn or not."
  - https://axivity.com/product/ax6: "The AX6 has additional light and temperature sensors, their output is inserted in to the recorded data stream."
  - https://github.com/openmovementproject/openmovement/blob/master/Docs/ax3/ax3-auxiliary.md: "This data is always recorded, regardless of configuration, whenever the device is logging movement data."
  - same URL: "The sensors are internally sampled at 1 Hz"
- **Date:** checked 2026-10-11 (product pages live; auxiliary doc last edited 2026-07-19 per repo history)
- **Source type:** vendor_page; repository
- **KB has it:** **contradicts.** Profile line 45 (Temperature: present on "GENEActiv Original" only), line 50 (Ambient light: "GENEActiv Original" only), lines 26 and 59 to 61 (AX3 described as accelerometer only), line 159 ("No ... temperature (except GENEActiv's near-body temperature)"), line 175 (light channel credited to GENEActiv only for circadian work). Matrix line 86 gives Axivity AX3 / AX6 "No" in the temperature column.
- **Related (repository):** GitHub issue #11 records that OmGui, cwa-convert and the Axivity help pages used different temperature conversion formulas. The maintainer settled it in 2023: https://github.com/openmovementproject/openmovement/issues/11: "the correct temperature conversion from ADC values is". Worth a caveat if the temperature channel is added.

### C2. "No vendor-derived metrics whatsoever" is not quite true: OmGui ships built-in analysis
- **Schema field:** derived_metrics
- **Found:** Axivity's download page describes the AX3 software as having built-in analysis. The Open Movement research guide says OmGui, through omconvert, provides simple analysis methods. The omconvert README lists SVM/ENMO epochs, cut-point PA classification using published GENEActiv cut-points, and wear-time validation. These are open, published algorithms run locally, not proprietary vendor metrics, but the profile's absolute wording is wrong.
- **URLs and quotes:**
  - https://axivity.com/downloads/ax3: "Software for the AX3 sensors with built-in analysis (Windows)"
  - https://github.com/openmovementproject/openmovement/blob/master/Docs/ax3/ax3-research.md: "Some simple analysis methods are available through the open source OmGui configuration tool"
- **Date:** checked 2026-10-11
- **Source type:** vendor_page; repository
- **KB has it:** **contradicts.** Profile line 18 ("no derived metrics"), line 42 ("No vendor-derived metrics exist"), line 65 ("There are no vendor-derived metrics whatsoever"), line 165 ("There is no 'download a CSV of steps' path"; no step count is offered, but epoch SVM and cut-point CSVs are).

### C3. "No device API" is wrong: a documented device API (libOMAPI) exists
- **Schema field:** export_routes
- **Found:** The device communication protocol is documented and the C library libOMAPI (separate repo, last pushed 2026-07-21) can be used to build custom configuration and download software. A third-party R wrapper, axR (Circadia Lab, r-universe only, not on CRAN; v0.1.3 published 2026-07-21), wraps it for device discovery, configuration and download from R.
- **URLs and quotes:**
  - https://github.com/openmovementproject/openmovement/blob/master/Docs/ax3/ax3-research.md: "The AX device communication is documented, and a software API exists that can be used to create your own software to communicate with the AX devices"
  - https://circadia-bio.r-universe.dev/axR: "Serial communication and data retrieval for Axivity AX3/AX6 accelerometer devices"
- **Date:** checked 2026-10-11 (libOMAPI pushed 2026-07-21; axR 0.1.3 published 2026-07-21)
- **Source type:** repository
- **KB has it:** **contradicts.** Profile line 98 says "No device API (none needed)". The matrix's "no API" (line 54) means no cloud API, which remains true. axR is not mentioned anywhere.

### C4. biobankAccelerometerAnalysis is academic-use only and does not read AX6 data
- **Schema field:** derived_metrics (also academic_vs_commercial)
- **Found:** The Open Movement research guide notes that the Oxford UK Biobank pipeline carries an Academic Use Licence and is not compatible with AX6 data. The same guide says pampro does not read AX6 data either. The licence file bars commercial use.
- **URLs and quotes:**
  - https://github.com/openmovementproject/openmovement/blob/master/Docs/ax3/ax3-research.md: "Academic Use Licence; not currently compatible with AX6 data"
  - https://github.com/OxWearables/biobankAccelerometerAnalysis/blob/master/LICENSE.md: "THE SOFTWARE IS INTENDED FOR USE BY ACADEMICS CARRYING OUT RESEARCH AND NOT FOR USE BY CONSUMERS OR COMMERCIAL BUSINESSES."
- **Date:** checked 2026-10-11 (repo last pushed 2025-11-10)
- **Source type:** repository
- **KB has it:** **contradicts (partly).** Profile lines 75 to 76, 129 ("the analysis toolchain here is free and open") and 146 to 147 present it as part of a free, open pipeline with no licence caveat and no AX6 caveat. GGIR remains the open option.

### C5. Recording duration: Axivity's own datasheet and product page disagree
- **Schema field:** sampling_rates (recording window)
- **Found:** The AX3v2 datasheet (v1.8, dated 18/04/2023, linked from the AX3 product page) says up to 21 days. The product page says 30 days at 12.5 Hz and the Open Movement FAQ says about 65 days at 12.5 Hz. The datasheet's "21 days" is probably a different configuration, but it is unqualified.
- **URL and quote:** https://axivity.com/files/resources/AX3v2_Datasheet.pdf: "sensor will record for up to 21 days of continuous data"
- **Date:** datasheet dated 2023-04-18; checked 2026-10-11
- **Source type:** vendor_docs
- **KB has it:** **no** (profile line 107 cites only the product page and FAQ figures). Record as a vendor-internal conflict, not a KB error.

---

## Programs, partners and services (missing)

### P1. No research program; third-party analysis services exist instead (McRoberts, accelting)
- **Schema field:** research_program, academic_vs_commercial
- **Found:** Axivity runs no research or academic program (consistent with the KB). The Open Movement research guide names third parties offering paid support. McRoberts offers data collection and processing with Open Movement sensors, and Vincent van Hees (GGIR author, accelting.com) offers consulting. The McRoberts link (`mcroberts.nl/axivity-services`) now 301-redirects to the McRoberts homepage, so whether that service is still offered is **Unclear**. Separately, the KB's Empatica notes say McRoberts algorithms sit in Empatica's Enterprise tier.
- **URL and quote:** https://github.com/openmovementproject/openmovement/blob/master/Docs/ax3/ax3-research.md: "offer analytics using Open Movement sensors"
- **Date:** checked 2026-10-11 (redirect observed 2026-10-11)
- **Source type:** repository; secondary
- **KB has it:** **no.** Profile line 88 says "None from the vendor" and line 162 of the matrix says "There is no vendor to ask". Both are still true of Axivity itself, but the paid-services route is unmentioned.

### P2. AX-Deploy, a mass-deployment tool, and limits of the web configurator
- **Schema field:** export_routes (study operations)
- **Found:** Open Movement provides AX-Deploy for mass deployments, which configures each device with a unique session ID from a barcode. It does not support AX6 gyroscope configuration. The web configurator, AX Config, configures one device at a time and cannot download data.
- **URL and quotes:** https://github.com/openmovementproject/openmovement/blob/master/Docs/ax3/ax3-research.md:
  - "software is specifically for mass deployments, where each device may have a unique configuration"
  - "This is not be compatible with AX6 device gyroscopes"
  - "one-at-a-time configuration (but not download)"
- **Date:** checked 2026-10-11
- **Source type:** repository
- **KB has it:** **no / contradicts (minor).** AX-Deploy is not mentioned. Profile line 78 says to "Plan on OmGui 45 ... or the web configurator", without saying the web tool cannot download. Line 102 calls a laptop plus OmGui "the entire infrastructure".

---

## Changes in the last 12 months

### R1. List prices rose by £10 on both devices, between Jan 2025 and Dec 2025
- **Schema field:** device_price
- **Found:** Wayback captures show the AX3 puck at £129 ex VAT (2025-01-04) and the AX6 puck at £189 ex VAT (2024-09-13). By 2025-12-10 the AX6 puck was £199, and by 2026-01-25 the AX3 was £139, the current prices. The banded variants rose by the same £10. Third-party guides (Fibion) still quote the old £129/£189 figures. Note also that the shipping page says "Prices include VAT where applicable", while the product pages say "(exc VAT)".
- **URLs and quotes:**
  - https://web.archive.org/web/20250104090451/https://axivity.com/product/ax3: "AX3 Puck £129.00 (exc VAT)"
  - https://web.archive.org/web/20240913171031/https://axivity.com/product/ax6: "AX6 Puck £189.00 (exc VAT)"
  - https://web.archive.org/web/20251210225700/https://axivity.com/product/ax6: "AX6 Puck £199.00 (exc VAT)"
  - https://axivity.com/product/ax3: "AX3 Puck £139.00 (exc VAT)"
  - https://axivity.com/shipping: "Prices include VAT where applicable."
- **Date:** snapshots 2024-09-13, 2025-01-04, 2025-12-10; live page 2026-10-11
- **Source type:** vendor_page (archived)
- **KB has it:** **no** (current price is in profile line 126; no price history, and the Fibion figures would read as a conflict without it).

### R2. AX3 firmware V50 is labelled experimental; V48 is the last standard release
- **Schema field:** deprecations (firmware status)
- **Found:** The firmware notes, re-edited 2026-06-04 to add dates, describe V50 as an experimental alternative interface build. V48 (11-05-2020, wide 32-bit device IDs) is the newest non-experimental build, and the page says users should not need to update firmware themselves.
- **URL and quote:** https://github.com/openmovementproject/openmovement/blob/master/Downloads/AX3/AX3-Firmware.md: "Experimental alternative generic (and WinUSB) interface support."
- **Date:** doc edited 2026-06-04; checked 2026-10-11
- **Source type:** repository
- **KB has it:** **partly.** Profile line 78 names V50 as "the newest AX3 firmware" and calls it a "WinUSB/generic variant" without saying it is experimental.

---

## Regulatory and compliance

### G1. CE marking is under the EMC Directive, not as a medical device; FCC Part 15 Class B tested
- **Schema field:** fda_clearances (also regulatory status generally)
- **Found:** The AX3v2 datasheet's certification section cites the EMC Directive 2014/30/EU, EN 61000-6-1/-6-3, FCC Part 15 Class B, IP68 (IEC 60529), WEEE and UN 38.3 battery transport. It does not mention medical device classification (MDR, MDD, UKCA medical). openFDA 510(k) and registration-listing searches for "axivity" returned no matches. The AX3 is therefore a CE-marked electronic product, not a regulated medical device. Contrast with GENEActiv, which the KB records as moving to EU MDR.
- **URL and quotes:** https://axivity.com/files/resources/AX3v2_Datasheet.pdf:
  - "The product is compliant with the Directive 2014/30/EU; the relevant Declaration of Conformity is available from Axivity."
  - "tested to comply with FCC CFR 47 part 15.107 and 15.109 (Class B Device)"
- **Date:** datasheet v1.8, 2023-04-18; FDA API checked 2026-10-11
- **Source type:** vendor_docs; regulator_db (null result)
- **KB has it:** **no.** Matrix line 259 has a regulatory note for GENEActiv only. Profile lines 116 to 122 discuss data governance but not device regulatory status.

### G2. Axivity's published GDPR statement covers website customers only
- **Schema field:** gdpr_statement (also retention_terms, dpa)
- **Found:** The privacy policy (latest revision 26 July 2021) covers personal data collected through the website and orders, cites UK GDPR and keeps that data 6 years. It says nothing about participant data, because Axivity never receives any. This supports the KB's "no processor" position, so a DPA or BAA is not applicable for study data.
- **URL and quotes:** https://axivity.com/privacy:
  - "Under the UK General Data Protection Regulation (UK GDPR)"
  - "We retain Personal Data for period of 6 years."
- **Date:** policy revised 2021-07-26; checked 2026-10-11
- **Source type:** vendor_legal
- **KB has it:** **no** (profile lines 116 to 122 reason from the architecture, not from a vendor statement). Consistent, not contradictory.

---

## Other gaps

### O1. AX3v2 hardware revision
- **Schema field:** raw_streams (device generations)
- **Found:** The current AX3 datasheet is for the "AX3v2". Its enclosure is improved and the USB connector has moved, but it is otherwise functionally identical.
- **URL and quote:** https://axivity.com/files/resources/AX3v2_Datasheet.pdf: "The AX3v2 is functionally identical to the AX3"
- **Date:** 2023-04-18
- **Source type:** vendor_docs
- **KB has it:** **no.**

### O2. UK Biobank seasonal repeat study: 17% incomplete kits from battery wear on reused devices
- **Schema field:** history_depth / study operations (device reuse risk)
- **Found:** UK Biobank's Physical Activity Monitor document v2.0 (August 2025) adds a seasonal repeat study. More than 5000 people were invited in Nov 2017 to Apr 2018, and 3000+ accepted for four cycles. In season 1, 17% of dispatched kits came back incomplete, against under 1% later. UK Biobank attributes this to battery performance in devices reused from the main study. The document also names the AX3 as a commercial version of Newcastle's Open Movement design.
- **URL and quotes:** https://biobank.ndph.ox.ac.uk/ukb/ukb/docs/PhysicalActivityMonitor.pdf:
  - "Over 5000 invitations to an accelerometry seasonal repeat study were sent"
  - "This disparity is due to suboptimal battery performance among kits that were re-used from the main study in season 1, which was rectified in later seasons."
  - "a commercial version of the Open Movement AX3 open source sensor designed by Open Lab, Newcastle University"
- **Date:** document v2.0, August 2025
- **Source type:** secondary (study documentation)
- **KB has it:** **no.** Profile lines 88 and 114 cover postal deployment and device loss but not battery degradation on reused units. This is relevant to the open question at profile line 196.

### O3. Other documented large deployments: INTERVAL (6000 participants) and IDEA-FAST / Mobilise-D AX6 procurement
- **Schema field:** research_program (evidence of use)
- **Found:** Axivity's case study says the INTERVAL blood-donation trial used the AX3 band with 6000 participants. A UK Contracts Finder notice shows Newcastle University awarding Axivity a £200,000 contract (19 Oct 2021, negotiated without competition) for AX6 devices for the EU IDEA-FAST and Mobilise-D projects. The notice also confirms the supplier is an SME.
- **URLs and quotes:**
  - https://axivity.com/case-studies/interval: "INTERVAL is using the AX3 band to assess the impact of blood donation interval on the physical activity levels of 6000 participants"
  - https://www.contractsfinder.service.gov.uk/Notice/202ae1a7-9e51-4348-ab6d-2c5df211ce83: "These devices are required for the EU IDEA-FAST and Mobilise-D projects."
  - same URL: "Total value of contract £200,000"
- **Date:** case study undated; contract awarded 2021-10-19
- **Source type:** vendor_page; secondary (government procurement record)
- **KB has it:** **no** (only UK Biobank is profiled; no Module 3 profile on any Axivity deployment).

### O4. Clock drift of about ±2 s per day
- **Schema field:** sampling_rates
- **Found:** The internal clock is set from the configuring computer to the nearest second, then drifts. This matters for multi-device sync and long recordings. The FAQ suggests shake markers as a mitigation.
- **URL and quote:** https://github.com/openmovementproject/openmovement/blob/master/Docs/ax3/ax3-faq.md: "potentially of the order of around ±2 seconds per day"
- **Date:** FAQ last edited 2026-08-18
- **Source type:** repository
- **KB has it:** **no.**

### O5. Paediatric safety restriction
- **Schema field:** academic_vs_commercial (study suitability)
- **Found:** The safety notes say to keep the device away from children under 36 months because of the choking hazard, and not to use it directly on infants without a tool-removable enclosure.
- **URL and quote:** https://github.com/openmovementproject/openmovement/blob/master/Docs/ax3/ax3-research.md: "Do not allow the device to be accessible to infants under 36 months as it can pose a choking hazard."
- **Date:** checked 2026-10-11
- **Source type:** repository
- **KB has it:** **no.**

### O6. Warranty and shipping terms
- **Schema field:** minimum_commitment (purchase terms)
- **Found:** The hardware warranty is one year and excludes software. International buyers pay customs duties, and dispatch is aimed at within seven days if in stock. No minimum order is stated anywhere on the shop.
- **URLs and quotes:**
  - https://axivity.com/warrantyterms: "for a period of ONE YEAR from that date"
  - https://axivity.com/shipping: "For international orders, any taxes or duties assessed by customs will be the responsibility of the recipient."
- **Date:** warranty terms "as of 1 January 2013"; checked 2026-10-11
- **Source type:** vendor_legal
- **KB has it:** **no.**

### O7. WAX9 Bluetooth IMU: discontinued, but downloads are still listed
- **Schema field:** deprecations
- **Found:** Axivity's downloads page still lists the WAX3 and WAX9 streaming Bluetooth sensors, but the shop sells only the AX3, AX6 and accessories. In 2017 a user relayed Axivity's reply that the WAX9 was no longer manufactured. That relayed reply is Reported only.
- **URLs and quotes:**
  - https://axivity.com/downloads/wax9: "The WAX9 is a streaming inertial measurement unit (IMU)."
  - https://github.com/openmovementproject/openmovement/issues/25: "we are no longer manufacturing the WAX9 sensor"
- **Date:** issue comment 2017-12-12; checked 2026-10-11
- **Source type:** vendor_page; repository (issue)
- **KB has it:** **no.** Low priority, but it explains why a reader finding WAX9 docs cannot buy one.

### O8. GitHub issues: support is light and device-detection problems recur
- **Schema field:** export_routes (operational)
- **Found:** The main repo has 8 open issues. The most recent, closed 2025-08-19, is an AX6 not detected by OmGui; the maintainer replied with a link to the troubleshooting guide, which was updated 2026-06-16. Issues #50 to #52, opened in 2023 (OmGui download failure, AX6 firmware source and gerber gaps), are still open.
- **URL and quote:** https://github.com/openmovementproject/openmovement/issues/55: "AX6 sensor not being detected"
- **Date:** 2025-08-19
- **Source type:** repository
- **KB has it:** **no** (profile line 78 covers maintenance cadence, not support responsiveness or the open AX6 hardware-file gaps). Issues were read only.

---

## Searched, nothing found
- FDA: openFDA 510(k) and registration/listing APIs for "axivity" and "open movement" returned no matches.
- No ISO 13485, ISO 27001, SOC 2, UKCA or MHRA registration evidence. The only certification found is the EMC/FCC/IP68 set in G1.
- No research, academic, grant or partnership program, and no academic discount, on axivity.com, the support FAQ or the Open Movement docs.
- No press releases or newsroom. The site has no news section beyond three case studies (UK Biobank, INTERVAL, ClimbAX).
- No acquisition, ownership change or Companies House filing surfaced in web search.
- No named distributors or resellers in the US or EU; Fibion articles are third-party guides, not sellers.
- No job postings or conference talks found.
- No integrator pages for Axivity at Fitabase, Labfront, Terra or Thryve (expected, since the devices have no cloud).
- No new OmGui release since v45 and no new AX6 firmware.
- The software licence file changed only its copyright year (2026-03-05, now "Newcastle University (UK) and Open Movement project contributors"). The BSD terms are unchanged.
- Our Future Health: no evidence it uses Axivity devices.
