# Judgement: empatica (2026-10-10)

Inputs: `A.yaml`, `B.yaml`, `gaps.md`. Output: `facts/empatica.yaml`, with 41 facts (37 stated, 4 not_public,
0 conflict). Confidence: 34 Verified, 7 Corroborated. I re-probed all 126 quotes in the final record. 125 came
back `exact` the first time. One quote ("research teams requiring more than 30 devices...") was attributed to
the Available Features article but actually comes from the EmbraceMini blog post. I moved it there and it then
probed `exact 1.0`. `validate.py --file facts/empatica.yaml` gives 41/41 researched and 0 errors.
`weekly.py --only empatica --no-state` checked 43 pages: 0 missing, 0 reworded, 0 dead, 0 check by hand.

## The three conflicts the coordinator named

| Question | What the pages say | Decision |
|---|---|---|
| EmbraceMini magnetometer | The clinical-trials page ("4x sensors: Accelerometer, Gyroscope, Magnetometer, Ambient Light Sensor") and the EmbraceMini product page ("Ambient light sensor, plus 3-axis Accelerometer, Gyroscope and Magnetometer") list one. The research-studies raw-data table, the sensor-mode table in the academic help centre and the Avro stream list never mention a magnetometer. The mode table gives EmbraceMini rates for the accelerometer, gyroscope and ambient light only. | **Not a conflict. The pages answer different questions.** The magnetometer is on the hardware, per two Empatica pages. No magnetometer signal reaches researchers on the academic plan. Recorded in `raw_streams` (EmbraceMini) as "No magnetometer stream is offered to researchers", with the clinical-trials quote and a judge note. Whether Enterprise clients get it is not stated. |
| EmbracePlus battery, 28 days or 14+ days | The academic help centre mode table gives EmbracePlus 2+, 7+, 14+, 5+ and 5+ days (Pulse Rate Pro, Actigraphy Pro, Actigraphy Optimized, Gyroscope Max, Gyroscope 100) and EmbraceMini N/A, 7+, 14+, 3+ and 3+. The research-studies page says "up to 14+ days depending on selected sensor configuration". The clinical-trials page says "Battery life can last up to 28 days", and the Cloud API page says "up to 28 days of battery life". | **The mode table wins for the record. The 28-day figure is noted as unsupported.** The mode table is the only figure tied to a named configuration, and no published mode reaches 28 days. The 28-day claim appears only on Enterprise-facing marketing pages, so it may describe an unpublished Enterprise configuration. That is a guess, and the record says so. Battery has no schema field, so the decision lives in the `sampling_rates` note, since the sensor mode sets both. |
| SDK status | The research-studies page says "We do not provide an SDK for academic research purposes." The remote-patient-monitoring page (live, HTTP 200, listed in the sitemap but not in the main navigation) describes "Empatica's plug-and-play SDK" and says "Use the Empatica Health Monitoring Platform SDK to create a patient app". The Cloud API page offers APIs to sponsors and CROs. | **Not a conflict. Split by scope.** The academic entry says there is no SDK (Verified). A second entry covers Enterprise, sponsors and remote patient monitoring: the Cloud API is Verified on the page, and the SDK is described on a live page, with no sign that it is still sold to new customers, so that entry is Corroborated. The E4 SDK was sunset on 14 Feb 2025 (see `deprecations`). |

## FDA: 12 claimed, 9 in openFDA

- openFDA `applicant:empatica` returns exactly 9 510(k)s: K172935, K181861, K232915, K250515 (POS, seizure);
  K221282 (DQA); K230457 and K242737 (MWI); K252981 (LEL, EmbraceMini); K260374 (GYD, Parkinson's).
- **De Novo:** I searched the FDA De Novo database (`denovo.cfm`, POST search) by requester "empatica" and "global
  kinetics" and by device name "embrace" and "PKG". All four searches returned "No records were found". To confirm
  the search itself worked, I ran requester "apple", which returned DEN230081, DEN180042 and DEN180044. So the gap is not
  De Novo.
- **PKG:** openFDA `device_name:PKG` returns three 510(k)s held by GKC Manufacturing Pty, Ltd. (PKG Health's
  maker), all product code GYD: K140086 (2014-08-22), K161717 (2016-09-20), K211887 (2022-03-11, Gen 2 Plus).
  Empatica acquired PKG Health (blog, quote exact). 9 + 3 = 12 matches the homepage's "12 FDA clearances" (quote
  exact). Empatica doesn't say which records it counts, so the reconciliation is labelled an inference. The three
  records sit in their own scoped entry, which states that the holder of record is GKC, not Empatica.
- **K242737:** I downloaded the 510(k) summary with a browser user agent and read it with pdftotext. It says the
  device is substantially equivalent to K230457 "other than the implementation of an authorized Predetermined
  Change Control Plan (PCCP) specific to a subcomponent of the SpO2 algorithm". accessdata.fda.gov returns 404
  to the probe, so this wording lives in the note, not as a quote. The quoted sources are the openFDA record and
  Empatica's PCCP blog post, both `exact`.
- Records use the accessdata.fda.gov record page as `url` and the openFDA k_number query as `fetch_url`,
  Verified, with full "applicant date SESE country device" quotes copied from the openFDA text. B had used
  single-word quotes ("Embrace", "EpiMonitor"), which would match any of several records, so I replaced them.

## Where A and B disagreed

| Field | A | B | Decision |
|---|---|---|---|
| developer_program_status | One entry, Verified, no mention of the RPM SDK | One entry, Corroborated, RPM SDK included | Two scoped entries (see above). |
| program_application | One unscoped entry | Academic and Enterprise entries | B's scoped layout. A's discount-form quote went into the academic entry, and A's "larger number of devices" quote went into the Enterprise entry. |
| program_status | Store page and the E4 sunset | September 2026 EmbraceMini and sensor-mode expansion | Merged. Both are true and both are quoted. |
| program_eligibility | Purchase agreement clause (i), the university-email rule, Enterprise via sales | Non-profit definition, platform sold to for-profit institutions too | Merged all five quotes. |
| user_cap | One entry | Academic and Enterprise entries | B's scoped layout, plus the gap hunter's sensor-mode lock ("cannot be changed once the account has been created") in the academic entry. |
| device_price / subscription_price | Research and EpiMonitor mixed in one entry | Scoped | Scoped. EpiMonitor device price ($399) added from A as its own scope. |
| api_platform_fees | One stated entry ("Enterprise not published") | Academic stated plus Enterprise not_public | B. |
| raw_streams | One entry for both devices | Separate EmbracePlus and EmbraceMini entries | B, plus Avro delivery (gap 3) and "Systolic Peaks (IBI)" (gap 5). |
| derived_metrics | Partial research-page table | Full academic help-centre list, 300+ Enterprise figure, SpO2 Enterprise-only | B. |
| history_depth | Access beyond the term may cost extra | 60 days of retrieval after termination | Both. They are separate clauses of the same agreement and don't contradict each other. |
| retention_terms | 10 years, cease use at term end | 10 years, 60 days, repair may delete data | Union of all four quotes. |
| ai_training_terms | Verified | Verified | Lowered to **Corroborated**. "No AI clause" is an absence finding, and the DPA could not be read. |
| deprecations | Verified, from Empatica's /research/e4-sunset/ page | Corroborated, saying Empatica's sunset page was 404 and relying on a University of Twente notice | **Verified.** /research/e4-sunset/ answered on 2026-10-10 and both of A's quotes are `exact`. B had tried /connect, which now serves the same page. Twente is kept only for the 1 Aug 2024 hardware-support date, marked secondary. |
| rate_limits | not_public, Unclear | not_public, Verified | **Verified.** The absence is itself certain, because the documentation that would hold limits is client-only or inside the portal. |
| baa | not_public, Unclear | not_public, Verified | **Corroborated.** The DPA is unreadable and the vendor pack is form-gated, so a BAA could exist in either. |
| soc2 | not_public, Unclear | not_public, Verified | **Verified.** The legal page lists its certifications without SOC 2, and so does the vendor-pack contents list. |
| gdpr_statement DPO quote | /privacy, "postal address" | /privacy-participant, "email address" | B's. The participant policy is the one that governs research data. |
| fda_clearances | One combined entry | Five scoped entries | Scoped, with fuller quotes, the PCCP content and the PKG entry. |

The drafts agreed on research_program, academic_vs_commercial, academic_pricing, minimum_commitment,
quote_required, sampling_rates, export_routes, dpa, hipaa_statement, iso27001 and data_residency. I merged
those, keeping the union of quotes and adding gap material where noted.

## Gap-hunter findings

| # | Finding | Decision |
|---|---|---|
| 1 | Per-mode PPG, EDA, temperature and gyroscope rates; the first mode is "Pulse Rate Pro" | **Accepted** (`sampling_rates`). I read the full article myself. |
| 2 | Academic plan offered one mode until 16 Sept 2026; mode locked per account | **Accepted** (`academic_vs_commercial`, `user_cap`, `deprecations`). |
| 3 | Raw data is Avro only, CSV holds the biomarkers; two key sets; LOTUS paper | **Accepted** (`export_routes`, `raw_streams`). The /rawdata/ page quote was not needed. |
| 4 | K242737 is the SpO2 PCCP clearance | **Accepted.** I confirmed the PDF wording myself (see FDA above). |
| 5 | IBI delivered as "Systolic Peaks (IBI)" | **Accepted** (`raw_streams`). |
| 6 | Cloud API for sponsors and CROs | **Accepted** (`developer_program_status`, `export_routes`, `academic_vs_commercial`). |
| 7 | E4 suite sunset 14 Feb 2025 | **Accepted** (`deprecations`, `program_status`). |
| 8 | Renewal prices, euro prices, 100-device MOQ, more than 30 devices to sales, discount covers EmbraceMini | **Accepted** (`subscription_price`, `minimum_commitment`, `user_cap`, `quote_required`, `academic_pricing`). |
| 9 | Battery, memory, data volume, latency per mode | **Accepted in part.** Battery, the 30-minute batches and the 24-hour lag in Actigraphy Optimized are in `sampling_rates`. Memory-full data loss, the 1.5-hour charge and the Bluetooth 5.0 phone requirement have no schema field and are listed below for the profile. |
| 10 | BU MODES deal, BARDA PROJECT REMOTE, PKG acquisition | **Accepted as context only.** BU and BARDA appear in the `research_program` note (both quotes `exact`). They are deployments, not a program. The PKG acquisition is quoted in the PKG FDA entry. |
| 11 | McRoberts algorithms are Enterprise-only; Gyroscope 100 output is McRoberts/Mobilise-D compatible | **Accepted** (`academic_vs_commercial`). |
| 12 | TÜV Rheinland ISO 27001 certificate; ISO 13485 and MDR certificates | **Accepted.** ISO 27001 is `certificate`-sourced and Verified, which lifts the self-claim cap. The ISO 13485 certificate number and validity were probed `exact` on the cdn.sanity.io PDF and the MDR notified body on the CE certificate; both are in the iso27001 note, since there is no field for them. Certipedia was not checked. |
| 13 | Embrace2 Class II recall Z-0159-2024, ongoing | **Accepted as a note** on the platform FDA entry. I confirmed it in openFDA enforcement: Class II, Ongoing, initiated 2023-07-13, 1,360 units. |
| 14 | Community Avro tooling | **Accepted** (paper quote in `export_routes`, tools named in its note). |
| 15 | Real-time streaming in the custom DATALAND build | **Accepted as a note** in `export_routes`. It does not change the academic "no streaming" fact. |
| 16 | Vendor survey of 84 clients on adherence | **Rejected for this record.** No schema field, and it's a self-selected vendor survey. Worth a Module 3 mention as Reported. |
| 17 | "160+ countries, 100,000+ devices" | **Rejected.** Marketing figure, no field. |

## Profile and matrix statements the record contradicts

Profile: `module-01-wearables/profiles/empatica.md`. Matrix: `module-01-wearables/comparison-matrix.md`.

| File, line | Says | Record says |
|---|---|---|
| Profile 21, 137 | K230457 **and K242737** "add pulse rate and respiratory rate" | K242737 differs from K230457 only by an SpO2-algorithm PCCP. Pulse rate and respiratory rate came with K230457. |
| Profile 41, 46, 50; 54; 65; 204; 239 | PPG, temperature and EDA rates "Unclear" / "not published"; first mode called "Standard" | PPG 64 Hz (5 LEDs) or 4 Hz, EDA 4 Hz, skin temperature 1 Hz, gyroscope 64 or 100 Hz, all published per mode. The first mode is "Pulse Rate Pro". |
| Profile 43 | "Rates for Standard and Gyroscope Max modes not published" | Accelerometer 64 Hz in both. |
| Profile 45, 51 | Magnetometer and ambient light "Unclear" | EmbracePlus: none listed. EmbraceMini: magnetometer hardware listed, with no researcher stream; ambient light 1 Hz. |
| Profile 54, 172 | Five modes presented as if all were available; "which measures are Enterprise-only is not published" | The academic plan had only Pulse Rate Pro until 16 Sept 2026. The mode is fixed per account. McRoberts algorithms are named as Enterprise-only. |
| Profile 93; matrix 184 | "unlimited participant credentials" | The academic account allows up to 1,000 participants (the matrix carries both statements). |
| Profile 103; matrix 47, 108 | Raw data download in "CSV format, via the Care Portal" | Raw signal is Avro only, via S3. CSV is the biomarker export from the Download Hub. |
| Profile 117, 244 | "A general-purpose REST API ... not established" | A Cloud API exists for sponsors and CROs, with client-only documentation. |
| Profile 119, 208, 243 | The E4 streaming SDK "does not appear to" carry over, "should be confirmed" | The E4 SDK and the whole E4 suite were sunset on 14 Feb 2025. A remote-patient-monitoring page describes a separate platform SDK outside the research plans. |
| Profile 10, 29 | E4 "legacy" with no end date | Sunset on 14 Feb 2025. Hardware support ended 1 Aug 2024 (secondary). |
| Profile 128, 207, 242; matrix 206 | Battery and charging cadence not documented; "other modes not documented"; phone requirement not stated | EmbracePlus 2+/7+/14+/5+/5+ days by mode. Full charge about 1.5 h. Bluetooth 5.0 phone required (gap 9, help centre). Enterprise pages separately claim up to 28 days, which is unsupported. |
| Profile 142; matrix 250 | ISO 27001 etc. "Corroborated", "certificates not opened" | TÜV Rheinland certificate 01 153 2117571, valid 2025-10-31 to 2028-10-30, Verified. |
| Profile 166; matrix 227 | Enterprise quote-only, no minimum; no renewal price | Enterprise MOQ is 100 devices. Renewal is from $388.80/yr (EmbracePlus) and $291.60/yr (EmbraceMini). Subscriptions can't be bought for devices from other sources. |
| Profile 173, 249; matrix 392 | Access after the 3- or 5-year window "Unclear" | Yearly extensions are sold. Data stays retrievable for 60 days after termination, and continued access may carry extra charges. |
| Matrix 108 (IBI column) | "Unclear (pulse rate variability biomarker provided)" | IBI is a raw stream ("Systolic Peaks (IBI)"). |
| Matrix 108, 138, 140, 323 | PPG and EDA rates "not published" | Published (see sampling_rates). |
| Matrix 165 | Latency "Batch upload" | 30-minute batches, or once a day in Actigraphy Optimized (data up to 24 hours old). |
| Matrix 250 | FDA list omits PKG context and the K242737 content | See the FDA entries. |

## For the coordinator to check by hand

1. The "12 = 9 + 3 PKG" reconciliation is an inference. Only Empatica can confirm it, and only openFDA's holder
   field shows the PKG 510(k)s are still under GKC Manufacturing.
2. The K242737 PCCP wording was read from the PDF via curl and is not probe-checkable. A browser look at
   https://www.accessdata.fda.gov/cdrh_docs/pdf24/K242737.pdf would confirm it.
3. ISO certificate 01 153 2117571 has not been checked on TÜV's Certipedia registry.
4. The 28-day battery claim: worth asking Empatica whether an Enterprise-only mode exists.
5. The DPA (Salesforce, JavaScript) and the form-gated vendor pack were not read. A BAA or AI-use clause could
   sit in either.
