# Movesense: judgement (baseline run, 2026-10-11)

Inputs: `A.yaml`, `B.yaml`, `gaps.md`. Output: `facts/movesense.yaml`. Every quote in the final record was re-run
against its live page with the `quote_probe.py` matcher on 2026-10-11 and returned `exact`. The judge read the Terms
page, the device library LICENSE.pdf, the FAQ, the Academic Program page and its Google Form, the hardware-variants
and data-storage docs, the API reference, the Flash, HR2, MD and Flash Developer Kit product pages, the specifications
page and the 2021 buy-out news post directly.

## Coordinator's points

1. **Licensing.** Recorded in `academic_vs_commercial`, with every document quoted. FAQ: "All our SDK's, developer
   tools, and sample code are open and free to use." Terms page: a Limited Evaluation Licence Agreement with
   Movesense Ltd, twelve months from signature (section 11), "shall not incorporate or integrate the Licensed
   Technology ... in any products or services", and a note that "A separate Commercial License agreement ... is
   available for commercial use". LICENSE.pdf (SDK License and Evaluation Agreement): Purpose is "evaluation, testing
   and potential development", the same incorporation bar, and commercialization "subject to a separate agreement".
   Mobile library README: Showcase app and sample source are Apache 2.0. sbem-tools: MIT. Status kept `stated`, not
   `conflict`: the documents do not disagree on cost, and the FAQ's "open" is about access, not an open-source
   licence. The tension is spelled out in the value and note. The schema's `licence` field applies only to
   platforms, so it cannot be used for a wearable.
2. **Custom firmware and MDR.** New scoped entry `developer_program_status` / "Medical firmware for Movesense MD",
   five exact quotes (2023 MDR news post, medical_sw docs page, MD product page, 2.3.1 release post).
3. **Organization.** No schema field for ownership, so it sits on `deprecations` as three sources (buy-out post:
   "becoming independent of Suunto following a management buy-out deal" and "The deal effective of Oct 1st 2021";
   Terms: "Movesense Ltd, a limited liability company incorporated in Finland") with a note saying it is context,
   not a deprecation.
4. **Academic Program.** `program_status` Active, Verified (December 2025 news post), with the Q1 2023 list quoted.
   Review cadence is a genuine vendor disagreement (program page "monthly basis", form "weekly basis"), so
   `program_application` is `conflict`. Commercial potential and publicity value are in `program_eligibility`; the
   credit requirement and the publicity-material requirement are in `research_program`.
5. **Memory units.** Notes only, not conflicts. EEPROM: hardware table says 384 kB, data-storage doc says 386 kB; the
   HR2 product page says "3Mbit EEPROM", which is 384 kB, so 386 is a typo. Flash: product page "128 Mb", specs page
   "128MB" and hardware table "128 MB FLASH"; the published logging durations (five days of ECG) fit 128 MB, so "Mb"
   is a typo. Neither changes a study decision.
6. **Accelerometer rates.** Split `sampling_rates` into ECG (`stated`) and IMU (`conflict`). Three vendor figures:
   API reference Info responses list up to 1666 Hz for accelerometer, gyroscope, magnetometer and IMU; Flash
   Developer Kit spec sheet lists 12.5 to 416 Hz; HR2 product page lists 12.5 to 833 Hz. B noted the 416 vs 1666
   split; A recorded 1666 Hz only. This matters, because the KB's headline "1.6 kHz IMU" rests on the API example.
7. **ECG Recorder app.** `retention_terms`, `ai_training_terms` and `data_residency` each have an entry scoped to the
   app, kept separate from the own-integration route where Movesense receives no data.
8. **Labfront.** In `export_routes`, two exact quotes from help.labfront.com (MD, HR2 and Flash compatible;
   participants start each recording manually), type `secondary`.

## Fields where A and B disagreed

| Field | A | B | Decision and reason |
|---|---|---|---|
| research_program | No scope | Scoped to the program | B's scope, A's fuller value; added the publicity-material quote, which both drafts summarised without quoting. |
| program_application | stated, monthly | stated, monthly | Both missed the form's "weekly". Opened the form; quote exact. Changed to `conflict`. |
| program_status | stated, Verified | stated, Verified | Agreed. The gap hunter wanted Unclear; rejected, because the December 2025 post is a dated vendor statement that a project joined. Added the Q1 2023 quote so the staleness is on record. |
| developer_program_status | Open; licence quotes | Open; business-only kits | Merged: A's licence quotes, B's business-only developer kit quote, plus the FAQ's "open and free". Added the medical-firmware scoped entry. |
| user_cap | stated | not_applicable | **stated.** The Academic Program has real limits (three projects a quarter, sensors sized to scope). |
| academic_vs_commercial | Licence and evaluation terms | Shorter | A's entry extended with LICENSE.pdf, Apache 2.0 and MIT quotes (point 1). |
| device_price (MD) | 349 EUR flat | 349 EUR flat | Both missed the tiers. MD product page: "1-49 349€ 50-99 344€ 100-199 339€", quote exact. |
| device_price (others) | shop page | product-category page | Kept A's shop quotes (all exact) and B's search-cache note. |
| subscription_price | stated, none | not_applicable | **stated.** "No subscription" is a fact about price. Added the gap hunter's 2025 ECG Recorder post saying advanced features will move into a premium subscription. |
| api_platform_fees | FAQ, specs, NRE | FAQ, OEM "no license cost" | Merged; dropped A's specifications quote as redundant. |
| minimum_commitment | 100 labels, 500 SKU | adds 200 pieces | Merged. |
| raw_streams | about-us page, README, MD filter | FAQ "raw, unfiltered", temperature | Merged; replaced A's about-us quote with B's FAQ quote, which says "raw, unfiltered". |
| derived_metrics | rrData JSON example | API front-end sentence | B's quote is plainer; kept A's specs, about-us and app quotes. |
| sampling_rates | 1666 Hz only | 416 and 1666 Hz noted | Split; IMU `conflict` (point 6). |
| history_depth | EEPROM sizes | Flash durations | Merged both; notes on 384/386 and Mb/MB (point 5). |
| export_routes | developers page, .fit | FAQ, Showcase app store | Merged; added Labfront. |
| retention_terms | Two scopes | One entry | A's two scopes. Replaced A's fragment quote ("If you have registered with Movesense") with B's full retention sentence, minus its first clause, since the curly apostrophe made the full sentence fragile. |
| ai_training_terms (app) | stated | unclear | **stated.** The terms are clear about what they say (broad reuse after anonymization, no AI mention); the value says model training is not named. The uncertainty is about interpretation, not about the terms. |
| deprecations | stated, migrations | not_public | **stated.** Logbook JSON change, deprecated /Component/Led, and the MDS crash are documented developer migrations with sources. Added the MDD to MDR SKU succession and the organization context. |
| baa, dpa, hipaa, iso27001, soc2 | not_public, Unclear | not_public, Corroborated | **Corroborated**, the cap for these self-claim fields; the searches were thorough and agree. |
| fda_clearances | not_public, Unclear, 6 openFDA queries | not_public, Verified, roadmap quote | **Verified** (regulator_db sources). Merged queries; added B's "FDA 510k is on the roadmap" quote. |
| data_residency | Two scopes | One combined | A's two scopes; added B's privacy-policy quote to the services scope. |

Recheck dates: compliance fields moved to 2027-01-09 (90 days from 2026-10-11); others kept at 2026-11-09 as both
drafts had them.

## Gap-hunter findings

| # | Finding | Decision |
|---|---|---|
| 1 | Buy-out from Suunto, effective 1 Oct 2021 | **Accepted.** Quotes exact. On `deprecations` as context (no ownership field). |
| 2 | Custom firmware outside MDR | **Accepted.** New scoped `developer_program_status` entry. IEC 62304 and "host medical device" quotes not used; not needed for the fact. |
| 3 | Labfront supports MD, HR2, Flash; manual start; discount | **Accepted.** Compatibility and manual-start quotes in `export_routes`; discount in the note only. |
| 4 | ISO 13485 by Eurofins; MDR and MDD SKUs | **Accepted.** SKU quote on `deprecations`; Eurofins in the `iso27001` note. Certificate and EUDAMED entry not located, so not treated as independent evidence. |
| 5a | Flash logging durations | **Accepted** in `history_depth`. |
| 5b | 128 Mb vs 128 MB | **Accepted as a note**, not a conflict (point 5). |
| 6 | Form live, weekly vs monthly, Suunto credit, Research Bundle 404 | **Accepted.** Weekly quote makes `program_application` a conflict; Suunto wording and 404 in notes. The "up to 20 sensors" poster figure was not probe-confirmed and is **rejected**. |
| 7 | Custom firmware from 200 pieces | **Accepted** in `minimum_commitment`. White-label quote not needed. |
| 8 | No FDA clearance; 510(k) on roadmap | **Accepted.** |
| 9 | Apache 2.0, MIT, placeholder licence | **Accepted** in `academic_vs_commercial`. The datalogger's placeholder is in the note. |
| 10 | Five free tools, EDF+, premium subscription, GSP in default firmware | **Accepted.** Spread across `export_routes` and `subscription_price`. |
| 11 | BLE bottleneck caveat | **Accepted** in substance; the API reference's own BLE warnings are quoted, which say the same thing. |
| 12 | Flash and HR2 prices | **Accepted** (already in both drafts). |
| 13 | IP68, CR2025 battery on the MD FAQ | **Holds up, but no schema field fits.** Not in the record; listed under profile contradictions. |
| 14 | Kubios is a CSV workflow; Fibion resells Flash | **Accepted** as notes (`derived_metrics`, `export_routes`, `research_program`). |
| 15 | Module 3 palliative-care profile not linked | **Out of scope for the record**; listed below for the coordinator. |

## Profile and matrix statements the record contradicts

| File | Line | What it says | What the record says |
|---|---|---|---|
| module-01-wearables/profiles/movesense.md | 1, 7 | "Movesense (Suunto)", "Suunto / Amer Sports, Finland" | Independent of Suunto since the management buy-out effective 1 Oct 2021; Movesense Ltd, Finland |
| profiles/movesense.md | 18, 22, 174-175, 198-199 | Custom firmware and Class IIa status presented together as strengths | Custom firmware is not covered by the MD's MDR registration; certified firmware comes from a separate, access-controlled repository |
| profiles/movesense.md | 46-48, 57, 65, 70, 171, 196 | IMU 13 Hz to 1.6 kHz, Corroborated | `conflict`: 1666 Hz in API examples only; spec sheets give 416 Hz (Flash kit) and 833 Hz (HR2) |
| profiles/movesense.md | 49, 66 | Temperature on "MD and Flash" | API reference says the sensor measures internal temperature; record treats it as all models |
| profiles/movesense.md | 76, 142 | Kubios "integration" | A CSV export and import workflow |
| profiles/movesense.md | 80, 84, 179, 187, 201, 207 | Labfront supports Movesense HR2 | Labfront supports Movesense Medical, HR2 and Flash; participants start recordings manually |
| profiles/movesense.md | 84 | No native researcher tools | Movesense publishes free recording tools (Showcase, Python GSP client, ECG Recorder, Flash datalogger) |
| profiles/movesense.md | 85 | Monthly review; whether the program still selects projects is Unclear | Review cadence conflicts (form says weekly); program is active (December 2025 project) |
| profiles/movesense.md | 11, 98 | Open source: No (SDK proprietary) | Correct for the device library; Showcase app and samples are Apache 2.0, sbem-tools MIT |
| profiles/movesense.md | 115, 184 | ECG products are session-wear | Flash logs up to five days of ECG or over four months of HR intervals |
| profiles/movesense.md | 125, 219 | FDA status Unclear | No FDA clearance in openFDA; Movesense says 510(k) is on the roadmap |
| profiles/movesense.md | 133, 216 | MD price tiers given; developer-kit pricing open | MD also 339 EUR at 100-199; developer kits 399/379/249 EUR |
| profiles/movesense.md | 189-190, 217 | Battery and water rating behind gated PDFs | MD FAQ news post lists IP68 and a CR2025 user-replaceable cell (gap 13; not in the record) |
| profiles/movesense.md | 220 | Flash logging duration open | Answered by Movesense's March 2026 post |
| module-01-wearables/comparison-matrix.md | 109, 129, 150, 333 | IMU to 1.6 kHz | IMU maximum is a vendor conflict |
| comparison-matrix.md | 193, 346 | Labfront: Movesense HR2 | MD, HR2 and Flash |
| comparison-matrix.md | 210 | Battery Unclear (datasheets gated) | Published on the web (gap 13) |
| comparison-matrix.md | 260 | FDA status Unclear | No FDA clearance found |
| comparison-matrix.md | 333 | Custom firmware and Class IIa MDR as joint strengths | Mutually exclusive on the MD |
| comparison-matrix.md | 403 | Monthly review; status Unclear | Weekly vs monthly conflict; program active |

## For the coordinator to check by hand

- Whether 1666 Hz IMU sampling works on every current model and over BLE (vendor question, info@movesense.com).
- Whether a deployed research app counts as "evaluation and potential development" under the twelve-month licence.
- EUDAMED entry and notified-body certificate for MS060222000 (not located).
- The Module 3 profile `module-03-applied-studies/profiles/movesense-palliative-support-trial.md` is not linked from the Module 1 profile.
- Gap 13 (IP68, CR2025 battery) has no schema field; it belongs in the profile.
