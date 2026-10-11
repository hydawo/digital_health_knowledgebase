# Empatica: gap hunter findings (baseline run, 2026-10-10)

Compared against `module-01-wearables/profiles/empatica.md` (profile), `module-01-wearables/comparison-matrix.md`
(matrix) and `facts/empatica.yaml` (every field still `unresearched`, so every finding below is "no" for the
yaml). Every quote was checked with `tools/facts/quote_probe.py` and returned `exact` on 2026-10-10, except
the K242737 PDF quote in finding 4, whose host is in `FALSE_404_HOSTS` (see that entry).

The single biggest source the KB has not used is Empatica's **separate academic help centre**,
https://academic-support.empatica.com/ (62 articles, many updated 2026-09-15 to 2026-09-21). It is
distinct from support.empatica.com, which the KB cites. Findings 1, 2, 3, 5, 6 and 8 come mostly from it.

Abbreviations: KB = knowledge base. "Date" is the source's own date where it has one, else the read date.

## Contradictions

### 1. sampling_rates: per-mode PPG, EDA, temperature and gyroscope rates are published
- **Found:** The "What is a Sensor Mode?" article tabulates every rate for all five modes. EmbracePlus: accelerometer 64 Hz in Pulse Rate Pro, Actigraphy Pro and Gyroscope Max, 32 Hz in Actigraphy Optimized, 100 Hz in Gyroscope 100 (all ±16 g); gyroscope off, off, off, 64 Hz, 100 Hz (±2000 dps); skin temperature 1 Hz in every mode; PPG 64 Hz (IR, green and red, 5 LEDs) in Pulse Rate Pro and 4 Hz (IR, 1 LED) in Actigraphy Pro, off otherwise; EDA 4 Hz in Pulse Rate Pro and Actigraphy Pro, off otherwise. EmbraceMini ambient light 1 Hz. The first mode is named **Pulse Rate Pro**, not "Standard".
- **URL:** https://academic-support.empatica.com/hc/en-us/articles/38901007393053-What-is-a-Sensor-Mode
- **Quotes:** "64 Hz (infrared, green and red, via 5 LEDs)" / "4 Hz (infrared, via 1 LED)" / "Electrodermal Activity (EDA)** 4 Hz 4 Hz OFF OFF OFF" / "Skin Temperature** 1 Hz 1 Hz 1 Hz 1 Hz 1 Hz"
- **Date:** article updated 2026-09-16
- **Source type:** vendor_docs
- **In KB:** contradicts. Profile lines 41, 46, 50 say rate "Unclear"; line 54 says "Per-mode PPG, EDA and temperature rates are still not on Empatica's pages" and names the first mode "Standard"; line 65, line 204 ("Most sampling rates not published") and Open Question line 239 repeat it. Matrix line 108 ("per-mode PPG rate not published", raw EDA "rate not published"), lines 138 and 140 ("Not published"), line 323 ("Per-mode PPG and EDA rates unpublished"). Note EDA 4 Hz and PPG 64 Hz happen to equal the legacy E4 values the KB warned not to assume; they are now documented for EmbracePlus, not assumed.

### 2. academic_vs_commercial: academic plan was Pulse Rate Pro only until 16 Sept 2026, and the mode is locked per account
- **Found (a):** Before the 23 Sept 2026 release, academic buyers got EmbracePlus in one mode only; the four actigraphy and gyroscope modes are new to the academic plan. Studies created before 16 Sept 2026 stay on Pulse Rate Pro.
- **URL:** https://www.empatica.com/blog/embracemini-is-now-available-for-academic-and-basic-research-plan/ ; https://academic-support.empatica.com/hc/en-us/articles/36980797675549-Available-Features
- **Quotes:** "Previously, the Academic & Basic Research Plan offered EmbracePlus in a single configuration, focused on cardiac activity: the mode now designated Pulse Rate Pro." / "Studies created before September 16th, 2026 run the Pulse Rate Pro Sensor Mode by default."
- **Found (b):** The sensor mode is chosen at study creation, applies to the whole account and cannot be changed; a different mode needs a new account. Combined with the academic limit of 1 study per account (profile line 171), a protocol needing two modes needs two academic accounts.
- **URL:** https://academic-support.empatica.com/hc/en-us/articles/38901007393053-What-is-a-Sensor-Mode
- **Quote:** "The Sensor Mode cannot be changed once the account has been created."
- **Date:** blog 2026-09-23; articles updated 2026-09-16
- **Source type:** vendor_page (blog); vendor_docs
- **In KB:** contradicts (partly). Profile line 54 lists five modes as if all were available, and reads the Enterprise actigraphy note as implying some combinations are Enterprise-only (Reported); the academic-only-one-mode history and the per-account lock are absent. Matrix lines 108 and 130 present the actigraphy and gyroscope rates without saying they reached the academic plan only on 16 Sept 2026. The mode lock is absent everywhere.

### 3. export_routes: raw data are Avro files on S3, not CSV; CSV is the minute-level biomarker export
- **Found:** High-frequency raw data are delivered only as Avro files (up to about 30 minutes per file, named `[participant_id]_[utc_timestamp_start].avro`, timestamps always UTC) in the S3 bucket. The Care Lab Portal "Download Hub" gives digital biomarkers. A peer-reviewed paper confirms the split: CSV holds minute-aggregated biomarkers, raw signal is Avro only, and Empatica's own Python script just converts Avro to CSV. Up to two active sets of Data Access Keys per portal account; the full Data Access Documentation is only inside the Care Lab Portal.
- **URLs:** https://academic-support.empatica.com/hc/en-us/articles/36981046788765-Raw-Data-in-the-Empatica-Cloud ; https://www.empatica.com/rawdata/ ; https://academic-support.empatica.com/hc/en-us/articles/36981014631837-Generating-and-Revoking-Data-Access-Keys ; https://pmc.ncbi.nlm.nih.gov/articles/PMC11644628/
- **Quotes:** "High-frequency raw data is delivered in Avro format." / "The stream length is up to roughly 30 minutes" / "Data and filename timestamps always use UTC+00:00" / "available to download in Avro format, leaving the processing to you" / "You can have up to two (2) active sets of Data Access Keys at a time." / (paper) "raw signal data are only available in avro file format, with each file storing up to 30 min of signal data organised by universal standard time" / (paper) "Empatica provides a Python script to convert avro files to CSV."
- **Date:** articles updated 2026-07-08; paper 2024 (Sensors, PMC11644628)
- **Source type:** vendor_docs; vendor_page; paper
- **In KB:** contradicts. Profile line 103 says "Raw data download | CSV format, via the Care Portal"; matrix line 47 ("CSV download") and line 108 ("CSV download and S3 access keys") imply raw CSV. Avro appears nowhere in the KB.

### 4. fda_clearances: K242737 is the SpO2 PCCP clearance, not the pulse rate and respiratory rate addition
- **Found:** K242737 (decision 2025-06-06) differs from its predicate K230457 only by an authorized Predetermined Change Control Plan for a subcomponent of the SpO2 algorithm; pulse rate and respiratory rate were already in K230457. Empatica calls it the first PCCP for a pulse oximetry device, letting it update the SpO2 algorithm without a new 510(k).
- **URLs:** https://www.empatica.com/blog/empatica-receives-landmark-fda-pccp-authorization-for-pulse-oximetry/ ; https://www.accessdata.fda.gov/cdrh_docs/pdf24/K242737.pdf ; openFDA record https://api.fda.gov/device/510k.json?search=k_number:K242737
- **Quotes:** (blog, exact) "the U.S. Food & Drug Administration has authorized Empatica’s pulse oximetry (SpO2) algorithm with a Predetermined Change Control Plan (PCCP)" / (openFDA, exact) "Empatica Health Monitoring Platform; EmbracePlus; Empatica Care; Care Portal" / (510(k) summary, read with curl and pdftotext, NOT probe-confirmed because accessdata.fda.gov returns 404 to the probe) "implementation of an authorized Predetermined Change Control Plan (PCCP) specific to a subcomponent of the SpO2 algorithm". The judge should confirm the PDF wording in a browser before marking Verified (regulator_only rule).
- **Date:** decision 2025-06-06; blog 2025-06-10
- **Source type:** regulator_db (openFDA, PDF); vendor_page (blog)
- **In KB:** contradicts. Profile line 137 groups K230457 and K242737 as adding "pulse rate and respiratory rate"; PCCP is not mentioned anywhere. Matrix line 250 lists K242737 without its content.

### 5. raw_streams: IBI is delivered as a raw stream ("Systolic Peaks (IBI)")
- **Found:** The academic plan's raw high-frequency data list includes systolic peaks, labelled as IBI; Pulse Rate Pro also yields IBI, PRV (RMSSD) and respiratory rate.
- **URL:** https://academic-support.empatica.com/hc/en-us/articles/36980797675549-Available-Features
- **Quote:** "Systolic Peaks (IBI)"
- **Date:** updated 2026-09-16
- **Source type:** vendor_docs
- **In KB:** contradicts. Matrix line 108, IBI column: "Unclear (pulse rate variability biomarker provided)". Profile line 41 does not name IBI or systolic peaks.

### 6. developer API: a Cloud API exists, for sponsors and CROs
- **Found:** Empatica sells a Cloud API that lets sponsors and CROs manage EmbracePlus participants from their own CTMS (import participant IDs, change status, end collection, read wear detection), with full developer documentation given to clients. Data still land in S3 as Avro and CSV. It was used for PROJECT REMOTE (finding 10). No sign it is offered on the academic plan.
- **URL:** https://www.empatica.com/cloud-api
- **Quote:** "All Cloud API clients will be provided with full developer documentation."
- **Date:** read 2026-10-10; launched by Oct 2024 (BARDA post calls it "our latest platform capability")
- **Source type:** vendor_page
- **In KB:** contradicts. Profile line 117: "A general-purpose REST API for study/participant management was not established"; Open Question line 244 asks the same. Best schema field: export_routes or academic_vs_commercial.

## Missing programs, regulatory events and terms

### 7. deprecations: E4 and its whole software suite were shut down on 14 Feb 2025
- **Found:** The E4 is retired and no longer sold; E4 connect, E4 manager, E4 realtime app, E4 streaming server and E4 SDK no longer collect or store data. A user institution reports hardware repairs ended 1 Aug 2024.
- **URLs:** https://www.empatica.com/connect/login.php ; https://www.utwente.nl/en/bmslab/about-us-contact/news-and-events/news/2024/8/1702215/important-information-about-the-empatica-e4-wristband
- **Quotes:** "As of February 14th, 2025, the E4 and its software suite have officially been sunset" / "(E4 connect, E4 manager, E4 realtime app, E4 streaming server, and E4 SDK) can no longer collect and store data" / (Twente) "Hardware support ended on August 1st, 2024"
- **Date:** 2025-02-14 (sunset); Twente notice 2024-08-13
- **Source type:** vendor_page; secondary
- **In KB:** no. Profile lines 10 and 29 call the E4 "legacy" with no end date; line 119 says EmbracePlus "does not appear to" have the E4's streaming SDK and asks for confirmation, and Open Question line 243 asks whether the E4 streaming SDK survives "in any form". The sunset answers that: it does not.

### 8. subscription_price / minimum_commitment / quote_required: renewal price, euro prices, Enterprise MOQ
- **Found:** Each device is bought as a package with its subscription; subscriptions can be extended one year at a time per device, from $388.80 (EmbracePlus) or $291.60 (EmbraceMini) a year. Euro prices are published (EmbracePlus package from €2,157.84). Subscriptions are sold only with devices bought from Empatica. Enterprise has a minimum order of 100 devices; academic teams needing more than 30 devices are asked to contact Empatica. The 25% academic discount covers EmbraceMini.
- **URLs:** https://academic-support.empatica.com/hc/en-us/articles/36980797675549-Available-Features ; https://www.empatica.com/blog/embracemini-is-now-available-for-academic-and-basic-research-plan/
- **Quotes:** "it can be extended by one year at a time, for each device" / "Starting from $388.80 or €359.64" / "Packages starting from $2,332.80 or €2,157.84" / "A subscription cannot be purchased on its own for a device obtained from any other source." / "MOQ: 100 devices" / "research teams requiring more than 30 devices are encouraged to contact Empatica directly" / "The 25% academic discount applies to EmbraceMini bundles on the same terms as EmbracePlus."
- **Date:** article updated 2026-09-16; blog 2026-09-23
- **Source type:** vendor_docs; vendor_page
- **In KB:** no. Profile line 166 says Enterprise is quote-only with no MOQ; lines 173 and 249 leave access after the 3- or 5-year window "Unclear" (renewal is now documented, though what happens to data if not renewed is still not); Open Question line 248 asks whether device-only purchase is possible (the converse, subscription-only, is now answered: no). Matrix lines 227 and 392 lack renewal and MOQ.

### 9. Battery, memory, data volume and latency per sensor mode (study operations; no schema field, closest sampling_rates)
- **Found:** EmbracePlus battery 2+ days (Pulse Rate Pro), 7+ (Actigraphy Pro), 14+ (Actigraphy Optimized), 5+ (both gyroscope modes); offline memory about 1.5, 7, 14, 5 and 3 days; phone upload about 6, 1.5, 1, 1.5 and 2.5 GB a month. Full charge about 1.5 hours. Data upload in 30-minute batches, but Actigraphy Optimized syncs once a day, so portal data can be up to 24 hours old. When memory fills, further data are lost. The Care Lab App needs a Bluetooth 5.0 phone. Separately, the Cloud API page claims "up to 28 days of battery life", which no mode table supports.
- **URLs:** https://academic-support.empatica.com/hc/en-us/articles/38901007393053-What-is-a-Sensor-Mode ; https://academic-support.empatica.com/hc/en-us/articles/36980824207261-How-the-Empatica-Health-Monitoring-Platform-works ; https://academic-support.empatica.com/hc/en-us/articles/36981190603421-EmbracePlus-Memory-is-Full-M-Icon ; https://academic-support.empatica.com/hc/en-us/articles/36980864789021-Charging-EmbracePlus-and-Checking-the-Battery ; https://academic-support.empatica.com/hc/en-us/articles/36981129315101--Phone-is-Not-Supported-Message-on-the-Care-Lab-App ; https://www.empatica.com/cloud-api
- **Quotes:** "Battery duration (days) EmbracePlus 2+ 7+ 14+ 5+ 5+" / "Data usage** (per month) EmbracePlus ~6 GB" / "with Actigraphy Optimized, the most recent data may be up to 24 hours old" / "The Care Lab App transmits the data to the Empatica Cloud in 30-minute batches" / "any data that would have been recorded while the memory is full is lost" / "A full charge takes about 1 hour and 30 minutes" / "requires a companion device equipped with Bluetooth 5.0" / (Cloud API page) "a modular FDA-cleared medical wearable with up to 28 days of battery life"
- **Date:** articles updated 2026-07-08 to 2026-09-16
- **Source type:** vendor_docs; vendor_page
- **In KB:** contradicts (study operations). Profile lines 128, 207 and Open Question 242 say battery and charging cadence are not documented; matrix line 206 says "other modes not documented" and "phone requirement not stated"; matrix line 165 gives latency only as "Batch upload". Note the 2-day battery in Pulse Rate Pro, the only academic mode until 16 Sept 2026, which matters for anyone reading older Empatica studies.

### 10. research_program: institutional deals and large deployments outside the store plan
- **Found (a):** Boston University's MODES study announced an agreement with Empatica (1 June 2026) to use EmbraceMini for technical validation of mobility algorithms in knee osteoarthritis.
- **URL:** https://sites.bu.edu/modes/2026/06/01/new-partnership-with-empatica/
- **Quote:** "we will include Embrace Mini as one of the devices in MODES study for technical validation of algorithms for mobility assessment in people with knee osteoarthritis"
- **Found (b):** Empatica is technology partner to Allucent on BARDA-funded PROJECT REMOTE (Project NextGen), a decentralized Phase IV COVID-19 vaccine study of 4,000 participants using EmbracePlus via the Cloud API.
- **URL:** https://www.empatica.com/blog/empatica-selected-as-a-technology-partner-for-government-funded-decentralized-research-program/
- **Quote:** "Allucent will be utilizing the Empatica EmbracePlus wearable and Empatica Health Monitoring Platform to collect continuous, real-time physiological data from 4,000 participants"
- **Found (c):** Empatica acquired PKG Health (1 Oct 2025); PKG's movement-disorder measures now run on EmbraceMini (FDA K260374 already in KB).
- **URL:** https://www.empatica.com/blog/empatica-acquires-pkg-health-to-transform-parkinson-s-disease-monitoring/
- **Quote:** "announced the successful acquisition of PKG Health"
- **Date:** 2026-06-01; 2024-10-15; 2025-10-01
- **Source type:** secondary (BU); vendor_page
- **In KB:** no. Profile's research-program section (lines 168 to 174) covers only the self-serve store plan. The PKG acquisition explains K260374 (profile line 138) but is not mentioned.

### 11. academic_vs_commercial: third-party algorithms (McRoberts, Mobilise-D) are Enterprise-only, but academic raw data are built to be compatible
- **Found:** Empatica hosts all 71 McRoberts endpoints (total "200+") and says it is open to external algorithm developers; the McRoberts algorithms are for Enterprise users. The academic Gyroscope 100 mode computes no activity biomarkers but outputs data "compatible with the McRoberts and Mobilise-D libraries" for researchers to run themselves.
- **URLs:** https://www.empatica.com/blog/empatica-and-mcroberts-partnership-achieves-20-endpoints-and-opens-platform-to-external-algorithm-developers/ ; https://academic-support.empatica.com/hc/en-us/articles/38901007393053-What-is-a-Sensor-Mode
- **Quote:** "The McRoberts algorithms are available to all Enterprise plan users of the Empatica Health Monitoring Platform."
- **Date:** 2024-05-13; article 2026-09-16
- **Source type:** vendor_page; vendor_docs
- **In KB:** no. Profile line 172 says which measures are Enterprise-only "is not published"; this names one concrete Enterprise-only set.

### 12. iso27001 / CE status: the certificates themselves, issued by TÜV Rheinland
- **Found:** ISO/IEC 27001:2022 certificate, reg. no. 01 153 2117571, TÜV Rheinland Cert GmbH, valid 2025-10-31 to 2028-10-30, first certified 2023. ISO 13485 (UNI CEI EN ISO 13485:2021) certificate 39 05 0072201, TÜV Rheinland Italia, valid 2025-05-08 to 2028-05-24. EU MDR QMS certificate ITH 1986726 1 from TÜV Rheinland Italia (notified body 1936), issued 2024-11-29, last revised 2026-03-11, expiry 2029-11-28, Class IIa, covering seizure detection, remote monitoring "and for the retrospective review" of physiological parameters, and (added 2026-03-11) kinematic motion analysis software; EUDAMED SRN IT-MF-000012905. Empatica announced platform MDR certification on 12 Dec 2024 and Parkinson's monitoring MDR on 30 Jan 2026; EmbraceMini is "CE-marked under EU MDR 2017/745" (EmbraceMini blog).
- **URLs:** https://www.empatica.com/go/empatica-iso-iec ; https://cdn.sanity.io/files/ggwhkgro/production/66365d60b7cbed6ee18b03bf83dda5407945fddd.pdf ; https://www.empatica.com/go/empatica-ce-certificate ; https://www.empatica.com/blog/empatica-receives-european-mdr-certification-for-health-monitoring-platform/ ; https://www.empatica.com/blog/empatica-secures-ce-mdr-certification-for-parkinson-s-monitoring-with-embracemini-and-pkg-measures/
- **Quotes:** "The certificate is valid from 2025-10-31 until 2028-10-30." / "TÜV Rheinland Cert GmbH" / "This Certificate is valid from 2025/05/08 to 2028/05/24." / "Notified under No. 1936 to the EC Commission" / "The device is intended for the remote monitoring of physiological parameters and for the retrospective review of the collected physiological parameters." / "has received CE Mark Certification under the European Union’s Medical Device Regulation (MDR) for the Empatica Health Monitoring Platform" / "has received CE Certification under the EU Medical Device Regulation (EU MDR 2017/745) for Parkinson’s monitoring via the Empatica Health Monitoring Platform"
- **Date:** as above
- **Source type:** certificate (PDFs, hosted by Empatica, issued by TÜV Rheinland); vendor_page
- **In KB:** no (upgrade). Profile line 142 and matrix line 250 carry ISO 27001, ISO 13485 and CE as Corroborated with "certificates not opened". These are certificate-type sources, which lift the self_claim_cap for iso27001. The judge may want to cross-check the numbers on TÜV's Certipedia registry, which was not searched.

### 13. fda_clearances (adjacent): Embrace2 Class II recall, still open
- **Found:** Recall Z-0159-2024, Class II, firm-initiated 2023-07-13, 1,360 Embrace2 units, battery may last under the stated 48 hours; status "Ongoing" in openFDA. Embrace2 is a consumer seizure device, not part of the research platform; included so the judge knows the only enforcement record found.
- **URL:** https://api.fda.gov/device/enforcement.json?search=recalling_firm:empatica
- **Quote:** "May have a battery life lasting less than the full 48 hours, requiring the device to be charged more frequently."
- **Date:** initiated 2023-07-13
- **Source type:** regulator_db
- **In KB:** no.

### 14. export_routes: researchers rely on community tools to read the Avro files
- **Found:** The LOTUS paper says raw EmbracePlus data are hard to use without purpose-built software and surveys GitHub toolkits: LOTUS (MATLAB, github.com/jack-fogarty/LOTUS), empaticaR (R), wearables/wearalyze (R, built for E4), and EmbracePlus-Visualiser (Python). Empatica's own help centre adds Python and MATLAB Avro guides.
- **URL:** https://pmc.ncbi.nlm.nih.gov/articles/PMC11644628/
- **Quote:** "Empatica provides a Python script to convert avro files to CSV."
- **Date:** 2024
- **Source type:** paper
- **In KB:** no. Matrix line 323 and profile line 111 present S3 export as a strength without the processing burden.

### 15. Real-time streaming exists in a custom build, not in research plans
- **Found:** For the DATALAND museum (opened June 2026), Empatica built a custom EmbracePlus with software for real-time streaming. The BARDA post also describes "continuous, real-time physiological data" via the Cloud API. Neither changes the academic plan's documented lack of live streaming (profile line 107), but they show streaming is technically possible on the hardware, which bears on Open Question line 243.
- **URL:** https://www.empatica.com/blog/empatica-announces-partnership-with-dataland-the-world-s-first-omni-sensory-museum/
- **Quote:** "EmbracePlus was customized exclusively for DATALAND with software and algorithms that enable real-time data streaming"
- **Date:** 2026-05-22
- **Source type:** vendor_page
- **In KB:** no.

### 16. Vendor-reported adherence across client deployments (no schema field)
- **Found:** Empatica surveyed 84 institutional clients at the end of 2025; 90% of studies reported average wear compliance of 80% or more and 92% had completion of 75% or more. Vendor survey, self-selected, not peer reviewed; useful only as a Reported figure for Module 3 context.
- **URL:** https://www.empatica.com/blog/rethinking-wearable-compliance-in-trials-evidence-from-real-world-deployments/
- **Quotes:** "We surveyed 84 of our clients" / "90% of studies reported average participant wearing compliance of 80% or higher"
- **Date:** 2026-03-18
- **Source type:** vendor_page
- **In KB:** no. Profile line 130 says adherence depends on study contact; no figures.

### 17. Scale claim on the Cloud API page
- **Found:** "160+ countries" and "over 100,000 devices deployed". Marketing figure, low weight.
- **URL:** https://www.empatica.com/cloud-api
- **Quote:** "with Empatica’s products available in 160+ countries with over 100,000 devices deployed"
- **Date:** read 2026-10-10
- **Source type:** vendor_page
- **In KB:** no.

## Searched, nothing found

- **FDA warning letters and Form 483s:** web search found none; the FDA warning-letter database was not queried directly. openFDA enforcement and recall endpoints hold only the Embrace2 recall (finding 13). openFDA 510(k) list matches the KB's nine K numbers; no new clearance after K260374.
- **SOC 2 and BAA:** no SOC 2 report, trust portal or BAA mention found on Empatica pages, the Cloud API page ("HIPAA, GDPR and ISO" only) or partner pages. KB already records these as not found.
- **AI-training terms:** the participant privacy policy has no clause on training models; it describes "De-identified User Biomarker data" and the service-plus-10-years retention the KB already has. The DPA and Enterprise terms were not read.
- **Integrator connectors for EmbracePlus** (Labfront, Fitabase, Terra, Thryve, RADAR-base, mindLAMP, Avicenna): none found. RADAR-base's Empatica plugin was E4-only and is moot after the sunset.
- **GitHub:** the `empatica` org has five repos; `empatica.github.io` (the old E4 docs) now redirects to the E4 sunset page. No public EmbracePlus SDK or API client.
- **App stores:** iOS "Empatica Care Lab" (id6443699123) and "Empatica Care" both updated 2026-09-24, iOS 17.0 minimum (iTunes Search API). No quote taken; listed for completeness.
- **Funding, layoffs, shutdown:** nothing in the last 12 months; the PKG acquisition and the Sept 2026 inaugural Empatica Summit at MIT Media Lab suggest the company is active.
- **Developer forums, job postings, conference talks:** not searched in depth; no forum exists for the academic plan (support is a ticket form).
- **Academic grant or discount programs beyond the 25% discount:** none found.
