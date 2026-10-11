# Garmin: gap hunter findings (baseline run, 2026-10-10)

Compared against `module-01-wearables/profiles/garmin.md` (profile), `module-01-wearables/comparison-matrix.md`
(matrix) and `facts/garmin.yaml` (all fields still `unresearched`, so every finding below is "no" for the
yaml). Every quote was checked with `tools/facts/quote_probe.py` and returned `exact` on 2026-10-10.

Abbreviations: KB = knowledge base. "Date" is the source's own date where it has one, else the read date.

## Contradictions

### 1. fda_clearances: Garmin ECG App is FDA-cleared, K221774
- **Found:** Garmin International's ECG App, 510(k) K221774, product code QDA, decision 12 Jan 2023 (SESE, Class II, 21 CFR 870.2345). The openFDA 510(k) endpoint returns this as the only Garmin-applicant clearance (`https://api.fda.gov/device/510k.json?search=applicant:"garmin"`). The accessdata.fda.gov page returned 404 to the fetcher, so the quote below is from a mirror of the FDA record; the judge should confirm on accessdata.fda.gov before marking Verified (regulator_only rule).
- **URL:** https://510k.innolitics.com/device/K221774 (mirror); also https://api.fda.gov/device/510k.json?search=k_number:K221774 (quote "Garmin ECG App" exact)
- **Quote:** "K221774 · Garmin International, Inc. · QDA · Jan 12, 2023"
- **Date:** 2023-01-12 decision
- **Source type:** secondary (mirror of regulator_db); openFDA API is regulator_db
- **In KB:** contradicts. Matrix line 244 regulatory column says "Not itemised in the profile"; profile line 49 says only ECG is "region-gated" and "Not documented as available via the Health API" with no clearance named. Profile line 130 says compliance/regulatory "not verified".

### 2. api_platform_fees: the developer agreement says no fees are due, but reserves future fees
- **Found:** Section 10.1 of the Connect Developer Program Agreement says no licence fees or payments are due, which cuts against the "$5,000 administrative fee" the KB carries as Reported. The same section reserves the right to charge for future API use on 30 days' notice, and 10.2 reserves fees for request volume above limits.
- **URL:** https://www8.garmin.com/en-US/GARMINCONNECTDEVELOPERPROGRAMAGREEMENT/GARMINCONNECTDEVELOPERPROGRAMAGREEMENT_EN.pdf
- **Quotes:** "Licensee acknowledges and agrees that no license fees or other payments will be due under this Agreement in exchange for the rights granted under this Agreement." / "reserves the right to charge fees for future use of or access to the API" / "reserves the right to charge fees for request volume that exceeds any limits set forth in the Application Requirements"
- **Date:** read 2026-10-10 (form FRM-0952 Rev. B, no date on the document)
- **Source type:** vendor_legal
- **In KB:** contradicts (partly). Profile line 137 and matrix line 218 carry the $5,000 fee as "Reported and unconfirmed"; the agreement's no-fee clause is not cited anywhere. The future-fee and over-limit-fee reservations are absent. Note this agreement text does not override the FAQ's metric-specific licence fee (profile line 136), which may sit in a separate licence.

### 3. research_program: Garmin itself launched the Asia 2026 grant, and runs direct institutional research deals
- **Found (a):** Garmin's own newsroom says Garmin Health launched the Asia Research Grant 2026 with Fitrockr, published 5 March 2026.
- **URL:** https://www.garmin.com/en-PH/newsroom/press-release/news-2026-mar-fitrockr/
- **Quote:** "Garmin Health officially launched its first research grant specific to Asia on February 2, in collaboration with Fitrockr"
- **Found (b):** Garmin and King's College London announced (17 Sep 2025, Garmin Health Summit) that Garmin is exclusive smartwatch provider for the EMBRACE maternal health research programme, up to 40,000 adults, described as Garmin's largest research-institution collaboration.
- **URL:** https://www.garmin.com/en-US/newsroom/?p=5892
- **Quotes:** "up to 40,000 adult participants" / "This is the largest collaboration to-date between Garmin and a research institution."
- **Date:** 2025-09-17 and 2026-03-05
- **Source type:** vendor_page (newsroom)
- **In KB:** contradicts (framing). Profile line 98 says "Research grants run through partners, not Garmin directly" and cites only fitrockr.com; matrix line 386 says "grants only through partners". Garmin's own release frames it as a Garmin Health launch. The KCL collaboration is absent from the KB; it shows Garmin Health does strike direct institutional research agreements, even though no open academic programme exists (profile line 95 still holds as written).

## Missing from the KB

### 4. ai_training_terms: agreement requires an AI Transparency Statement
- **Found:** Section 15.10 requires the licensee's privacy policy to carry a conspicuous AI Transparency Statement if Garmin end-user data is used to train or be processed by AI systems; 15.7 lets Garmin request evidence of compliance with "the artificial intelligence transparency requirements". No outright ban on AI training was found (searched "machine learning", "artificial intelligence").
- **URL:** https://www8.garmin.com/en-US/GARMINCONNECTDEVELOPERPROGRAMAGREEMENT/GARMINCONNECTDEVELOPERPROGRAMAGREEMENT_EN.pdf
- **Quote:** "if End User Data will be used for training with, or processing by, artificial intelligence systems"
- **Date:** read 2026-10-10
- **Source type:** vendor_legal
- **In KB:** no. Profile has no AI/ML terms; the matrix carries this for WHOOP only (line 246).

### 5. retention_terms / export_routes: research use is exempt from Garmin attribution rules
- **Found:** Section 6.4 requires Garmin attribution whenever Garmin device data is displayed or distributed to third parties, per the API Brand Guidelines (which cover "exported data, derived data"). Section 6.4(a) exempts Health API data used only in defense, research or remote patient monitoring markets, unless shown with licensee or third-party branding.
- **URL:** https://www8.garmin.com/en-US/GARMINCONNECTDEVELOPERPROGRAMAGREEMENT/GARMINCONNECTDEVELOPERPROGRAMAGREEMENT_EN.pdf ; https://developer.garmin.com/brand-guidelines/overview/
- **Quotes:** "used only within the defense, research, or remote patient monitoring markets" / "requirements for Garmin attribution on title-level displays, secondary screens, exported data, derived data, and social media"
- **Date:** read 2026-10-10
- **Source type:** vendor_legal; vendor_docs
- **In KB:** no. Best schema fit is unclear (no attribution field); closest are retention_terms or export_routes. Worth a note in the profile's Data Access section.

### 6. deprecations / developer_program_status: Garmin's stated reason for the pause, and the queue is frozen too
- **Found:** the5krunner (14 Sep 2026) reports Garmin correspondence that it is redesigning the API programme and cannot process requests already in the queue. Also places the pause after the July 2025 API Brand Guidelines and Strava's Sept to Oct 2025 lawsuit (Strava dismissed it after 21 days).
- **URL:** https://the5krunner.com/2026/09/14/garmin-developer-api-access-paused/ ; https://www.bikeradar.com/news/strava-drops-lawsuit-against-garmin-21-days-after-filing-it
- **Quotes:** "significant redesign and modernisation of the API program and related processes" / "It also said it could not process new requests already in the queue and could not say when processing would resume." / (BikeRadar, quoting Strava's CPO) "new developer guidelines for all of its API partners"
- **Date:** 2026-09-14; lawsuit Sept to Oct 2025
- **Source type:** secondary
- **In KB:** partly. Profile line 22 has the pause (Corroborated) but not that already-submitted applications are also frozen, nor Garmin's stated redesign reason. The5krunner adds a third independent account of Garmin correspondence, which strengthens Corroborated.

### 7. fda_clearances (CE/MDR): ECG App is an EU MDR Class IIa medical device
- **Found:** Garmin's German press release (Jan 2025) says the ECG App is a Class IIa medical device under EU MDR 2017/745, launched in the EU and Australia; UK and Switzerland followed in April 2025 per Garmin's Swiss release.
- **URL:** https://garmin-deutschland-gmbh.mynewsdesk.com/pressreleases/garmin-bringt-die-ekg-app-fuer-kundinnen-und-kunden-in-australien-und-der-europaeischen-union-auf-den-markt-3363727
- **Quote:** "Die EKG-App ist ein Medizinprodukt der Klasse IIa gemäß EU-Verordnung über Medizinprodukte (MDR) (EU) 2017/745"
- **Date:** 2025-01 (release); read 2026-10-10
- **Source type:** vendor_page (no EUDAMED record checked)
- **In KB:** no.

### 8. subscription_price: Garmin Connect+ ($6.99/month, $69.99/year) exists since March 2025
- **Found:** Garmin launched a paid Connect+ tier (AI "Active Intelligence", performance dashboard, coaching, LiveTrack extras), with existing features kept free.
- **URL:** https://www.garmin.com/en-US/newsroom/?p=5556
- **Quotes:** "then choose between a monthly ($6.99/month) or annual ($69.99/year) plan" / "All existing features and data in Garmin Connect will remain free."
- **Date:** 2025-03-27
- **Source type:** vendor_page (newsroom)
- **In KB:** no. Profile lines 13, 139 and matrix line 218 say "no consumer subscription for core metrics" / "None". That remains true for core metrics but the KB never mentions Connect+ exists; a study should know that some AI insights are paywalled and may differ across participants.

### 9. data_residency / dpa: the EN agreement names a Chinese Garmin entity and carries a PIPL cross-border appendix
- **Found:** The English-language agreement at the KB's watched URL names Garmin China Shanghai RHQ Co., Ltd. as the contracting party and appends a Chinese-law cross-border personal-information transfer contract. Whether US or EU licensees sign a different version is unclear; this may be a China-region version served at the en-US path.
- **URL:** https://www8.garmin.com/en-US/GARMINCONNECTDEVELOPERPROGRAMAGREEMENT/GARMINCONNECTDEVELOPERPROGRAMAGREEMENT_EN.pdf
- **Quotes:** "is a binding agreement between Garmin China Shanghai RHQ Co., Ltd. and its affiliates" / "Information on Cross-border Transfer of Personal Information"
- **Date:** read 2026-10-10
- **Source type:** vendor_legal
- **In KB:** no. Flag for the judge: the watched terms URL may not be the US agreement; worth a vendor question.

### 10. retention_terms (publication): agreement bars public statements about Garmin without approval
- **Found:** Section 8.4 forbids licensee press releases or public statements about Garmin or the agreement's subject matter without Garmin's written approval. Unclear how this applies to academic publication; relevant for a university that signs directly.
- **URL:** https://www8.garmin.com/en-US/GARMINCONNECTDEVELOPERPROGRAMAGREEMENT/GARMINCONNECTDEVELOPERPROGRAMAGREEMENT_EN.pdf
- **Quote:** "Licensee will not issue any press releases or make any other public statements regarding Garmin, this Agreement, or the subject matter hereof"
- **Date:** read 2026-10-10
- **Source type:** vendor_legal
- **In KB:** no. No exact schema field; nearest is retention_terms (data terms).

### 11. export_routes / deprecations: unofficial Garmin Connect libraries broke in March 2026
- **Found:** Garth, the Python library many researchers and tools (python-garminconnect) used to pull participant data from Garmin Connect without the developer programme, is deprecated after Garmin changed its auth flow. python-garminconnect moved to a new login path. This closes or destabilises the informal workaround while the official programme is paused.
- **URL:** https://garth.readthedocs.io/en/latest/
- **Quote:** "Garmin changed their auth flow, breaking the mobile auth approach that Garth depends on."
- **Date:** read 2026-10-10 (change reported March 2026 in python-garminconnect issues; date not quote-verified)
- **Source type:** repository
- **In KB:** no. Profile line 105 covers official participant self-export only.

### 12. iso27001 / soc2: Garmin's 10-K cites NIST CSF alignment, no ISO 27001 or SOC 2
- **Found:** Garmin's FY2025 10-K (Item 1C, filed 18 Feb 2026) describes a programme "aligned" with NIST CSF and a NIST-aligned third-party risk programme. No ISO 27001 certificate or SOC 2 report found from Garmin or a registry; third-party rating sites (Nudge Security, Rankiteo) list badges without evidence and should not be used. sec.gov returned 403 to the fetcher, so the quote is from a 10-K tracker mirror.
- **URL:** https://www.board-cybersecurity.com/annual-reports/tracker/20260218-garmin-cybersecurity-10k (mirror of https://www.sec.gov/Archives/edgar/data/1121788/000119312526056028/grmn-20251227.htm)
- **Quote:** "generally aligned with the tenets and methodologies of industry standards and best practices such as the National Institute of Standards and Technology (NIST) Cybersecurity Framework"
- **Date:** 2026-02-18
- **Source type:** secondary (mirror of a regulatory filing)
- **In KB:** no. Profile line 130 and matrix line 244 say SOC 2 / ISO "Unclear". Supports `not_public` for iso27001 and soc2, with this as context.

## Searched, nothing found
- FDA warning letters or close-outs for Garmin: none found; openFDA 510(k) lists only K221774 for applicant "garmin".
- Garmin BAA offered by Garmin or mentioned by a partner (Fitabase, Labfront, Terra): none found.
- Garmin trust portal, ISO 27001 certificate registry entry, SOC 2 report: none found.
- Garmin Connect privacy policy (garmin.com/privacy/connect): JavaScript-rendered, fetcher returned no text; data residency not established from it.
- Health API deprecation or shutdown notices: none; Health API still live for existing partners.
- Garmin academic tier, university programme, or reopening date for the Connect Developer Program: none.
- Index Sleep Monitor (2025) support in Labfront or Fitabase: not confirmed by either vendor.
- Health API rate limits and latency: not published anywhere found (secondary guides do not cite Garmin).
- EUDAMED entry for the ECG App: not checked (only Garmin's own MDR statement).
- Asia Research Grant 2026 recipients and any later Garmin grant: none found.
