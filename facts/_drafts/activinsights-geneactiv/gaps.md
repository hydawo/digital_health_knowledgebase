# Gap hunt: activinsights-geneactiv (2026-10-11)

Scope: Activinsights Ltd (styled "ActivInsights" on its site): GENEActiv raw accelerometer, the
ActivInsights Band, and the company's apps, cloud platform and services. Compared against
`module-01-wearables/profiles/axivity-geneactiv.md` (profile), `module-01-wearables/comparison-matrix.md`
(matrix), `shared/unresolved-questions.md` and `facts/activinsights-geneactiv.yaml` (every field
`unresearched`, so "KB has it" below refers to the profile and matrix). Every quote below returned
`exact 1.0` from `tools/facts/quote_probe.py` on 2026-10-11.

The single biggest gap: the KB describes Activinsights as a USB-only, no-cloud, no-API, no-vendor
device maker, mirroring Axivity. That is true of a basic GENEActiv deployment but no longer of the
company. It runs an Azure-hosted cloud with APIs, a Study Management Hub, background upload apps, and
a GENEActiv 1.3 hardware revision with Bluetooth adherence data. The profile merges two vendors whose
data-path stories now differ.

## A. Contradictions and missing programs

### 1. GENEActiv 1.3 adds Bluetooth near-real-time adherence data (contradicts "no adherence monitoring during wear")
- Fields: `raw_streams`, `export_routes`, `deprecations` (hardware revision)
- Found: the current Instructions for Use (Rev 10, updated Feb 2026) and Product Information Sheet
  (Rev.002, 2025) describe a GENEActiv version 1.3 with a Bluetooth 4.2 module. Once recording, the
  device periodically connects to a background app on a Bluetooth 5 computer or phone, which extracts
  and erases adherence data roughly every five hours. iOS 15+ devices support adherence data only;
  Android 6+, Windows and macOS apps are listed. Raw data still comes off by USB cradle.
- URLs and quotes:
  - https://activinsights.com/wp-content/uploads/2026/02/IFU-GENEActiv-Rev.010.pdf
    - "GENEActiv 1.3 has a Bluetooth module which is qualified Bluetooth 4.2"
    - "Once a device has started recording, it will attempt to initiate a Bluetooth connection periodically to provide adherence data."
    - "The process will typically repeat at roughly five-hour intervals, supporting the provision of near real-time adherence information."
    - "Bluetooth 5 is required for adherence data extraction"
    - "Apple iOS device running iOS version 15 or later (adherence data only supported)"
  - https://activinsights.com/wp-content/uploads/2026/02/Product-Information-Sheet-Rev.002.pdf
    - "Bluetooth functionality is available for real-time adherence data, if required."
  - Independent corroboration of 1.3 shipping: App Store, ActivInsights Companion 0.9.6 (2026-08-19)
    https://apps.apple.com/us/app/activinsights-companion/id1579732913 :
    "Added support for GENEActiv version 1.3 devices. Added support for ActivInsights Study Management Hub."
    App Store, GENEActiv Software (macOS) 4.0.13 (2026-03-06)
    https://apps.apple.com/us/app/geneactiv-software/id1658154045 : "Adds full support for GENEActiv 1.3 devices"
    CRAN GENEAcore NEWS https://cran.r-project.org/web/packages/GENEAcore/news/news.html :
    "New measurement device ‘GENEActiv 1.3’ added to"
- Date: IFU Feb 2026; app releases 2026-03-06 and 2026-08-19. Source types: vendor_docs, app_store, repository.
- KB: **contradicts.** Matrix line 192 gives Axivity/GENEActiv adherence monitoring as "Impossible
  during wear"; profile lines 161 to 162 "No adherence monitoring is possible during the wear period";
  profile line 110 "No app, no phone, no account, no sync". Note also that a competitor guide
  (Fibion, below) still states GENEActiv has no wireless transmission, so secondary sources lag.

### 2. Activinsights runs a cloud platform with APIs, hosted on Azure (contradicts "no cloud, no API, no vendor")
- Fields: `export_routes`, `data_residency`, `hosting` context, `api_platform_fees` (unknown)
- Found: Activinsights offers cloud raw-data management, cloud analysis and a configurable API
  (raw, event, summary, health, quality data) hosted on Azure, with a Fujitsu partnership for
  near-real-time IoT returns. Identifying data is held outside the cloud. Customers can instead keep a
  sovereign local store; the vendor says the customer chooses.
- URLs and quotes:
  - https://activinsights.com/research-study-services/data-infrastructure/
    - "Our raw data management, cloud data analysis and application programming interface (API) platform is hosted on Azure."
    - "We have a specialised partnership with Fujitsu to return personal data from Internet of Things (IoT) sensor products in near real time."
    - "All our data infrastructure is pseudonymised, holding directly identifying personal data outside of the cloud infrastructure in physically separate, study-specific systems."
    - "ActivInsights data services are based in the UK under European GDPR regulations."
  - https://activinsights.com/research-study-services/apps-software/
    - "the GENEActiv software will extract sensor-level, raw data to local, sovereign data stores."
    - "The uploaded data can be queried, downloaded or analysed on-demand by the ActivInsights Band Clinic App or via application programming interface (API)."
  - https://activinsights.com/wp-content/uploads/2026/03/GENEActiv-Product-Comparison-Sheet-Jan-2025.pdf
    - "Sovereign data store or use of ActivInsights’" (GENEActiv data-storage row; continues "cloud store")
  - https://activinsights.com/remote-monitoring-wearables/
    - "We give complete customer control of where data is stored and processed."
- Date: data-infrastructure page modified 2025-04-30; apps page 2026-01-29. Source type: vendor_page.
- KB: **contradicts.** Matrix line 54 "USB download. No cloud, no API, no account"; matrix line 259
  "N/A, no processor exists"; profile lines 12, 18, 93, 118 to 122 ("No third-party data processor
  exists", "No HIPAA BAA required for the device vendor, because the vendor never touches data").
  Still true for a USB-only GENEActiv study; false as a statement about the vendor's offering. A
  study that uses the Hub, Device Manager or Advanced Sleep Toolkit sends .bin files to Activinsights.

### 3. ActivInsights Study Management Hub and Device Manager (missing product)
- Fields: `export_routes`, `research_program` (services), `quote_required`
- Found: a web Study Management Hub for device configuration, participant assignment, real-time
  device and participant status and adherence, multi-site access. Demo by request; no public price.
  The Device Manager automates .bin upload to the Hub.
- URLs and quotes:
  - https://activinsights.com/demo-request-study-management-hub/
    - "The ActivInsights Study Management Hub provides real-time visibility into device and participant status, streamlining every step of decentralised clinical study management."
  - https://activinsights.com/digital-health-technologies/advance_sleeptoolkit/
    - "Upload a .bin file to the ActivInsights Study Management Hub (this is automated with the ActivInsights Device Manager)."
- Date: demo page 2025-06-11; app support added 2026-08-19 (finding 1). Source type: vendor_page, app_store.
- KB: **no** (profile line 88 "None from the vendor" for study management; matrix line 54 study management "None").

### 4. ActivInsights Band: a second, cloud-connected wearable with on-device analytics (missing product)
- Fields: `derived_metrics`, `raw_streams`, `subscription_price`, `export_routes`, `retention_terms`
- Found: wrist band with on-device behaviour classification (about 12 activity classes, steps,
  energy expenditure, sleep), no raw data, up to one year battery, uploads by app (iOS, Android,
  Windows) at least weekly, reports via Clinic App or API. Software access for one year included
  with purchase; unlimited reports on an annual renewable basis. Pricing by quote.
- URLs and quotes:
  - https://activinsights.com/resources/activinsights-band-support/
    - "Access to the ActivInsights Band software for up to one year is included with the purchase of the ActivInsights Band."
    - "Access to unlimited lifestyle reports can be provided on an annual, renewable basis."
    - "The data collected should be uploaded via the app at least once a week."
  - Google Play listing id com.activinsights.banduploader; Microsoft Store 9N4GQTVK9PKF (linked from
    the support page; listings not readable by fetch, not quoted).
- Date: support page 2026-03-09. Source type: vendor_page.
- KB: **no.** Profile line 30 only notes "the site lists a second wearable, the ActivInsights Band". No
  data streams, pricing model or data path recorded. A judge may decide the Band belongs in its own
  section or out of scope; either way the KB should say which.

### 5. FDA listing is product code IKK, Class II (510(k)-exempt), not Class I (conflict with vendor wording)
- Fields: `fda_clearances`
- Found: openFDA registration and listing shows ACTIVINSIGHTS LTD., proprietary name GENEActiv,
  listed 2018-01-04 under product code IKK "System, Isokinetic Testing And Evaluation", 21 CFR
  890.1925, device class 2, submission type 4 (510(k) exempt). No 510(k) clearances exist for the
  applicant. The vendor's GENEActiv page says Class I (that refers to the EU MDD) plus "FDA 510(k)
  exemption status".
- URLs and quotes:
  - https://api.fda.gov/device/registrationlisting.json?search=registration.name:activinsights&limit=5
    - "System, Isokinetic Testing And Evaluation"
  - https://api.fda.gov/device/classification.json?search=product_code:IKK : "890.1925"
  - https://activinsights.com/digital-health-technologies/professional-wearables/geneactiv/
    - "GENEActiv falls under the classification of Class I Non-Sterile Medical Devices, under the Medical Device Directive 93/42/EEC."
  - https://activinsights.com/remote-monitoring-wearables/
    - "The GENEActiv has FDA 510(k) exemption status and is EU CE marked."
- Date: openFDA data current 2026-09-28; registration expiry year 2026. Source type: regulator_db, vendor_page.
- KB: **partly.** Profile line 30 and matrix line 259 record only the MDD Class I to EU MDR move. FDA
  status, product code and US class are absent. EU importer (ActivInsights Actigraphy Limited, Dublin)
  and EU authorised representative (AR Experts B.V.) are named in the IFU, also absent.

### 6. Published ISO/IEC 27001 certificate expired 31 October 2025 (compliance evidence gap)
- Fields: `iso27001`
- Found: the certificate linked from the 2023 press release (British Assessment Bureau, certificate
  239005, BS EN ISO/IEC 27001:2017, initial certification 16 June 2023) shows "Expiry Date: 31 October
  2025". The certificate PDF is an image, so its text could not be quote-probed; read visually at
  https://activinsights.com/wp-content/uploads/2023/08/Activinsights-ISO-27001-Certificate-BAB-Exp.-Oct-2025-1.pdf .
  The site still claims current certification. 31 October 2025 was also the deadline for moving from
  the 2013/2017 edition to ISO/IEC 27001:2022. No renewed certificate was found; UKAS CertCheck is
  behind a bot check and was not used.
- Quotes (claims still live):
  - https://activinsights.com/activinsights-announces-opening-of-new-u-s-office-in-texas-to-power-global-growth/ :
    "ISO27001-certified systems with rigorous data privacy and security standards"
  - https://activinsights.com/digital-health-technologies/activinsights-actigraphy-sleep-toolkit/ :
    "all hosted within our secure, ISO27001-compliant environment."
- Date: press release 2025-06-05. Source type: certificate (expired), vendor_page.
- KB: **no.** Nothing on ISO 27001 in the profile or matrix. Ask Activinsights for the current
  certificate before relying on it.

### 7. Advanced Sleep Toolkit: free hosted analysis up to 10 participants (missing program)
- Fields: `research_program`, `academic_pricing`, `api_platform_fees`, `derived_metrics`
- Found: a vendor-hosted toolkit that scores sleep directly from GENEActiv .bin files (TST, SOL,
  efficiency, WASO, naps), free up to 10 participants; beyond that the price is not stated. Requires
  an account login. Page dated 2026-04-28, so new this year.
- URL: https://activinsights.com/digital-health-technologies/advance_sleeptoolkit/
- Quote: "Our Advanced Sleep Toolkit is free for use with up to 10 participants."
- Date: 2026-04-28. Source type: vendor_page.
- KB: **no** (profile line 65 "There are no vendor-derived metrics whatsoever"; matrix line 54 "None").

### 8. Free Actigraphy Sleep Toolkit and .bin to AWD conversion, positioned as Actiwatch replacement (missing program)
- Fields: `research_program`, `export_routes`, `deprecations` (market context)
- Found: free web toolkit for manual sleep scoring of AWD files from GENEActiv or Philips Actiwatch.
  GENEActiv software converts .bin to raw CSV, epoch CSV, or AWD (since a 2022 announcement).
- URLs and quotes:
  - https://activinsights.com/digital-health-technologies/activinsights-actigraphy-sleep-toolkit/ :
    "As Philips phases out Actiwatch and Actiware from the sleep research and clinical market, our toolkit fills the gap with a reliable alternative."
- Date: page 2026-02-11. Source type: vendor_page.
- KB: **no.** Profile line 92 lists only `.bin` as the GENEActiv export.

### 9. Vendor R Markdown analysis tools are non-commercial licence only (nuance to "open analysis ecosystem")
- Fields: `export_routes`, `academic_vs_commercial`
- Found: Activinsights' R Markdown report tools are gated behind an email form and licensed for
  non-commercial use within "the Activinsights ecosystem". The CRAN packages (GENEAread 2.0.10,
  GENEAclassify 1.5.5, GENEAcore 1.2.0) are GPL. SDKs for integration are "under licence".
- URLs and quotes:
  - https://activinsights.com/resources/geneactiv-support-1-2/
    - "The agreement clearly states it can only be used for the non-commercial analysis of raw data."
    - "The resources are openly available for the research community but are restricted to use within the Activinsights ecosystem with limited rights of redistribution."
  - https://activinsights.com/research-study-services/apps-software/
    - "ActivInsights can provide software development kits (SKDs) under licence to facilitate the integration of our professional measurement tools into your existing systems."
- Date: support page 2026-09-10. Source type: vendor_legal, vendor_page, repository.
- KB: **partly.** Profile line 11 "proprietary device, open analysis ecosystem"; GENEAread and
  GENEAclassify are not named anywhere; the licensing split is not recorded.

## B. Other gaps (KB lacks or is vaguer)

### 10. GENEActiv sampling and recording-duration table (fills an "Unclear")
- Fields: `sampling_rates`, `raw_streams`
- Found: selectable 10 to 100 Hz; fixed ±8 g, 12-bit (3.9 mg); temperature 0 to 60 °C, every 30 s
  minimum, 0.25 °C resolution. IFU table: version 1.2 and 1.3 record 14 days at 100 Hz, 26 at 50 Hz,
  44 at 20 Hz, 56 at 10 Hz; version 1.1 only 7 days at 100 Hz, 30 at 20 Hz. Version 1.3 drops the
  30, 40, 60, 66.7, 75 and 85.7 Hz options. A start delay costs about 5% per week.
- URL: https://activinsights.com/wp-content/uploads/2026/02/Product-Information-Sheet-Rev.002.pdf
- Quotes: "Logging Frequencies Selectable 10-100Hz"; "Maximum Logging Periods 60 days @20hz, 14 days @100hz";
  "Range +/- 8g"; "Resolution 12 bit (3.9mg)"; "Measurement Frequency Every 30s minimum"
- Internal conflict: the Product Information Sheet says 60 days at 20 Hz, the IFU table says 44 days
  (v1.2/1.3), and the FAQ says 30 days: https://activinsights.com/resources/faqs/ :
  "For example, recording at 100Hz lasts for 7 days and 20Hz records for 30 days." (the FAQ matches
  version 1.1). Record as a conflict with the device-version explanation.
- Source type: vendor_docs.
- KB: **no / Unclear.** Matrix line 116 "GENEActiv raw, rate not in the profile"; profile lines 45, 50
  and 107 mark temperature, light and GENEActiv duration as Unclear; unresolved-questions line 262.

### 11. Device lifetime: 50 charging cycles or 2 years (missing; affects reuse cost)
- Fields: `device_price` context, `minimum_commitment`
- URL: https://activinsights.com/wp-content/uploads/2026/02/IFU-GENEActiv-Rev.010.pdf
- Quote: "The device is reusable with a lifetime of 50 charging cycles or 2 years from the date of purchase."
- Source type: vendor_docs. KB: **no.** Relevant to the matrix's cheapest-option framing (line 235).

### 12. Third-party GENEActiv price indication (fills "by quote")
- Fields: `device_price`, `quote_required`
- Found: a 2026 Fibion comparison lists GENEActiv 0.5 GB at £425 to £510. Fibion sells a competing
  device; treat as Reported. (A search summary attributed US$750 to US$995 to GENEActiv; on reading,
  that figure belongs to the Micro Motionlogger, not GENEActiv.) The same page claims GENEActiv has no
  wireless transmission, which finding 1 contradicts for version 1.3.
- URL: https://web.fibion.com/articles/best-accelerometers-circadian-rhythm-research/
- Quote: "Device Price: GENEActiv 0.5 GB: £425–£510"
- Source type: secondary. KB: **no** (matrix lines 235 and 402 "GENEActiv quote"; profile line 126).

### 13. Pricing held for US customers despite tariffs; US office in Austin, Texas (June 2025)
- Fields: `device_price`, `quote_required`
- URL: https://activinsights.com/activinsights-announces-opening-of-new-u-s-office-in-texas-to-power-global-growth/
- Quote: "Despite tariffs and trade pressures, we’ve maintained pricing with no compromise to U.S. customers"
- Date: 2025-06-05. Source type: vendor_page. KB: **no.** US distributors listed on the Partners page
  include First Nation Group (federal supply schedule reseller, quote only) and VivoSense.

### 14. Privacy notices: processing country GB; Band data shared within the Coelition ecosystem; data may be used to promote goods and services
- Fields: `data_residency`, `retention_terms`, `ai_training_terms` (no AI statement found), `gdpr_statement`
- URL: https://activinsights.com/privacy-policies/privacy-policy-for-activinsights-band/
- Quotes:
  - "Processing Countries: GB"
  - "We may use your data to maintain our records; promote our goods & services and support health & medical research."
  - "Your personal data will be processed by other members of the Coelition ecosystem and associates who will process such personal data on behalf of the controller and in accordance with the controller’s instructions."
- Also https://activinsights.com/legal-data-protection/ : "ActivInsights is a registered member of Coelition, as are our data services providers."
- Date: notices dated 2024-11-08 (still list the old Harvard Industrial Estate address). Source type: vendor_legal.
- KB: **no.** No DPA, BAA or HIPAA statement was found on the site.

### 15. Warranty one year; recycling programme with £5 credit per returned device
- Fields: `device_price` context
- URLs and quotes:
  - https://activinsights.com/resources/warranty-and-returns/ : "ActivInsights offers a full 1-year warranty period."
  - https://activinsights.com/digital-health-technologies/recycling-programme/ :
    "When a GENEActiv device is returned, we will reward you with £5 off* a new device purchased as a replacement."
- Source type: vendor_page. KB: **no.**

### 16. Activinsights contributes GENEActiv 1.2+ light calibration to GGIRread (September 2026)
- Fields: `raw_streams` (light channel usability)
- URL: https://github.com/wadpac/GGIRread/releases/tag/1.0.11
- Quote: "Added GENEActiv light calibration needed for device model GENEActiv 1.2 and above."
- Date: 2026-09-18. Source type: repository. Related open GGIR issue #1544 (documentation) and closed
  #1432 ("GENEAsleep" bin files not recognised, Dec 2025). KB: **no.** Implication: light data from
  v1.2+ devices processed with older GGIRread is uncalibrated.

### 17. DiMe Core Digital Measures for paediatric rare disease collaboration (2025 to 2026)
- Fields: `research_program` (partnership, not a researcher access route)
- URL: https://activinsights.com/advancing_digital_endpoints_paediatric/ (2026-02-20). Source type: vendor_page.
- Found: Activinsights worked with DiMe's Core Measures team and Rafa's Moonshot (STXBP1) using
  GENEActiv. Not quoted; context only. KB: **no.**

## Searched, nothing found
- A formal academic or research access program, academic discount, grant or device-loan scheme: none
  on the site (the free Sleep Toolkits are the closest).
- Public GENEActiv or Band list price on activinsights.com or First Nation Group: quote only.
- FDA 510(k) clearances, warning letters or recalls for Activinsights: none (openFDA 510k search empty).
- EUDAMED entry for GENEActiv under MDR: not checked in this pass; no MDR certificate found on the vendor site.
- Renewed ISO 27001 certificate or SOC 2 report: none found. UKAS CertCheck needs a bot check.
- BAA, HIPAA statement, DPA template: none published.
- AI or model-training terms: none in the three privacy notices or website terms.
- Activinsights GitHub account: exists but no public repositories.
- Discontinuation notice for GENEActiv versions 1.1 or 1.2: none; the support page asks owners of
  serial numbers beginning 0 to contact the company.
- Job postings: careers page says no live vacancies.
- Integrators (Fitabase, Labfront, Terra, Thryve): not searched; GENEActiv has no cloud API for them to use, and the Band API is sold directly.
- Recent news after February 2026: none in the post sitemap (last post 2026-02-20).
