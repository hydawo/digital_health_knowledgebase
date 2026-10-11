# Axivity: judgement, 2026-10-11

Inputs: `A.yaml`, `B.yaml`, `gaps.md`, the starter `facts/axivity.yaml` (every field unresearched), the profile `module-01-wearables/profiles/axivity-geneactiv.md` and `module-01-wearables/comparison-matrix.md`. Output: `facts/axivity.yaml`, 34 entries (16 stated, 1 conflict, 8 not_public, 9 not_applicable), 15 watched pages. Every quote (60 distinct) re-confirmed "exact" with `quote_probe.py`. `validate.py --file facts/axivity.yaml`: 0 errors, 34 of 34 researched. `weekly.py --only axivity --no-state`: 32 pages, 0 quotes missing, 0 reworded, 0 unreachable.

`weekly.py` was run on an isolated copy (only `_schema.yaml` and `axivity.yaml`), because in the live tree it stops on a YAML parse error in `facts/movesense.yaml` line 941. That file belongs to another judge's run and was not touched.

All Open Movement links use `github.com/openmovementproject/...`. B cited the old `digitalinteraction` URLs, which 301-redirect; each was rewritten and re-probed at the new address.

## Fields where A and B disagreed

| Field | A | B | Decision and reason |
|---|---|---|---|
| academic_vs_commercial | not_public, Verified | stated, Corroborated, with the Academic Use Licence quote | stated, Corroborated. A real difference does exist, but it sits in a third-party tool: the Open Movement research guide says biobankAccelerometerAnalysis is under an "Academic Use Licence; not currently compatible with AX6 data", and its LICENSE.md excludes commercial businesses (both exact). Axivity's own offer has no split. |
| baa | not_public, Verified | not_applicable | not_applicable. Axivity sells offline USB loggers; the OmGui docs and FAQ show data goes from the device to the researcher's computer and never to Axivity. A vendor that never receives PHI is not a business associate, so the field does not apply. The note says no BAA is mentioned anywhere and that the question moves to any third-party service used. |
| dpa | not_public, Verified | not_applicable | not_applicable, same reasoning. Axivity is not a processor of study data. Its privacy policy covers only its own customer data. |
| research_program, academic_pricing, minimum_commitment, hipaa_statement, iso27001, soc2 | Verified | Corroborated | Corroborated. These are absence claims drawn from vendor pages, and four of them fall under the self-claim cap anyway. |
| fda_clearances | Verified | Corroborated | Corroborated. The openFDA null results are from the regulator, but a null search cannot rule out a listing under another name. Merged A's and B's searches (510(k), two registration-listing queries, UDI); re-ran the UDI query: "No matches found". Added the gap hunter's FCC quote. |
| deprecations | not_public, Verified | not_public, Unclear | not_public, Corroborated. Neither found an announcement. Merged both lists of quiet changes and added the gap hunter's V50 "experimental" finding (exact on the firmware page; V48 confirmed as the newest standard release). |
| device_price | one entry, both devices | scoped AX3 and AX6 | B's scoping, with A's split quotes (each exact). The 2025 price rise goes in each entry's note, with the Internet Archive capture URLs; all three archived quotes probed exact. |
| quote_required | Corroborated | Verified | Verified. The list prices are quoted directly from the store. |
| sampling_rates | one combined entry | scoped AX3 and AX6 | Scoped, plus a third scope for the auxiliary channels and the clock (gap findings C1 and O4). The AX6 gyroscope range is on the AX6 product page. |
| history_depth | stated, one entry, datasheet "21 days" in a note | stated, AX6 140 days from datasheet | Split by device. AX3 is now `conflict`. In Axivity's own AX3v2 datasheet, the description says "up to 21 days of continuous data" while the spec table says "30 days at 12.5 Hz or 14 days at 100 Hz". The product page agrees with the table, and the Open Movement FAQ says about 65 days at 12.5 Hz. All quotes exact. AX6 stays `stated` with B's datasheet figures plus the product page. |
| retention_terms | Verified, scoped to website data | Corroborated, with a procurement-notice quote | Verified. The privacy-policy quote is the vendor's own; the device-only data path is quoted from the OmGui docs. B's Contracts Finder quote is kept as supporting secondary evidence. |
| data_residency | Verified | Corroborated | Verified. This is architecture stated in the vendor's own technical docs, not a compliance self-claim. |
| developer_program_status, derived_metrics, raw_streams, export_routes | wording differences | | Merged, keeping the best-sourced quotes from each. |

## Points the coordinator asked to settle

1. **Light and temperature (AX3 and AX6).** Accepted. Both product pages and `ax3-auxiliary.md` say light, temperature and battery are always recorded at 1 Hz internally and stored once per sector. Temperature is internal device temperature, "primarily useful to help with sensor auto-calibration". Light is a relative indicator. Issue #11 (read only) records the conversion-formula mix-up and the maintainer's July 2023 correction. All of this is in raw_streams and sampling_rates.
2. **OmGui built-in analysis.** Accepted. The AX3 downloads page says "with built-in analysis", and the research guide says "Some simple analysis methods are available". derived_metrics now lists SVM epochs, MET cut-points, wear-time validation and a simple sleep detector, framed as open algorithms the researcher runs locally rather than vendor metrics.
3. **libOMAPI and axR.** Accepted. The research guide documents the device API. The libomapi repo is live at openmovementproject/libomapi (the old URL redirects). The axR r-universe page is exact. Both appear in developer_program_status and export_routes; axR is labelled third-party and not on CRAN.
4. **Recording duration.** Recorded as a `conflict` on history_depth (AX3), as above.
5. **Prices.** The current GBP 139 / 199 is stated; the GBP 129 / 189 history is in the notes.
6. **Repository move.** Done throughout.
7. **biobankAccelerometerAnalysis.** Recorded under academic_vs_commercial and cross-referenced from derived_metrics.
8. **BAA and DPA.** not_applicable, as above.

## Gap findings

| # | Finding | Decision |
|---|---|---|
| C1 | AX3 and AX6 record light and temperature | Accepted (raw_streams, sampling_rates). Five quotes exact, plus the auxiliary doc's internal-temperature and relative-light sentences. |
| C2 | OmGui has built-in analysis | Accepted (derived_metrics). |
| C3 | Documented device API (libOMAPI), axR | Accepted (developer_program_status, export_routes). |
| C4 | biobankAccelerometerAnalysis: academic only, no AX6 | Accepted (academic_vs_commercial). |
| C5 | Datasheet 21 days vs product page | Accepted as a `conflict` (history_depth, AX3). |
| P1 | McRoberts and van Hees paid services | Accepted as a note on research_program. The research guide names "Dr. Vincent van Hees" rather than "accelting", so the note uses his name. McRoberts' redirect was not re-tested, so "unclear" is kept. |
| P2 | AX-Deploy and the web configurator's limits | Accepted (export_routes), all three quotes exact. |
| R1 | GBP 10 price rise in 2025 | Accepted, as a note on device_price. |
| R2 | Firmware V50 is experimental | Accepted (deprecations). |
| G1 | CE under the EMC Directive, FCC Class B, no FDA records | Accepted (fda_clearances, iso27001 notes). |
| G2 | GDPR statement covers website customers only | Accepted (gdpr_statement scope, retention_terms). |
| O1 | AX3v2 hardware revision | Accepted (deprecations quote). |
| O2 | UK Biobank: 17% incomplete kits on reused devices | Accepted as a note on history_depth (AX3), with no quote and the document cited by name. The PDF was not re-probed. |
| O3 | INTERVAL, 6000 participants; Newcastle AX6 contract | INTERVAL accepted into the research_program note (quote exact). The contract is in the academic_pricing note. |
| O4 | Clock drift of about 2 s per day | Accepted (sampling_rates, auxiliary and clock scope). |
| O5 | Under-36-months choking hazard | Rejected for the record, since no schema field fits. Worth adding to the profile's participant section. |
| O6 | One-year warranty, customs duties | Accepted as notes (minimum_commitment, device_price). |
| O7 | WAX9 discontinued | Accepted as a note on deprecations, labelled as a relayed 2017 reply. |
| O8 | GitHub issue support is light | Rejected for the record (operational, no field). Issues were read only. |

## Profile and matrix statements the record contradicts

| File | Line | Says | Record says |
|---|---|---|---|
| profiles/axivity-geneactiv.md | 18 | "no derived metrics, no algorithms" | OmGui ships built-in open analysis: SVM, cut-points, wear time, sleep (derived_metrics) |
| profiles/axivity-geneactiv.md | 42 | "No vendor-derived metrics exist" | Same as above |
| profiles/axivity-geneactiv.md | 65 | "There are no vendor-derived metrics whatsoever. Counts, cut-points, sleep scoring, non-wear detection ... produced entirely by the analyst's own pipeline" | OmGui provides cut-points, wear-time validation and sleep detection, run locally by the researcher |
| profiles/axivity-geneactiv.md | 165 | "There is no 'download a CSV of steps' path" | True for steps, but OmGui exports epoch SVM and cut-point results |
| profiles/axivity-geneactiv.md | 26, 59 to 60 | AX3 "accelerometer-only"; streams listed as accelerometer (plus gyroscope on AX6) | Both also always record light, internal temperature and battery (raw_streams) |
| profiles/axivity-geneactiv.md | 45 | Temperature: "GENEActiv Original" only | AX3 and AX6 record internal device temperature (mainly for calibration) |
| profiles/axivity-geneactiv.md | 50 | Ambient light: "GENEActiv Original" only | AX3 and AX6 record a relative light level |
| profiles/axivity-geneactiv.md | 159 to 160 | "No ... temperature (except GENEActiv's near-body temperature)" | AX3 and AX6 have an internal temperature channel |
| profiles/axivity-geneactiv.md | 175 | Circadian light work credited to GENEActiv's light channel | AX3 and AX6 also have a relative light channel |
| profiles/axivity-geneactiv.md | 98 | "No device API (none needed)" | Documented device API (libOMAPI) plus the third-party axR wrapper |
| profiles/axivity-geneactiv.md | 75 to 76, 129, 146 to 147 | biobankAccelerometerAnalysis presented as part of a free, open toolchain | Academic Use Licence that excludes commercial users; cannot read AX6 data |
| profiles/axivity-geneactiv.md | 78 | V50 is "the newest AX3 firmware"; "Plan on ... the web configurator" | V50 is labelled experimental (V48 is the newest standard release); the web configurator cannot download data |
| profiles/axivity-geneactiv.md | 107 | Product-page and FAQ durations given as agreed, Verified | Axivity's own datasheet also says "up to 21 days"; AX3 duration is a vendor-internal conflict |
| profiles/axivity-geneactiv.md | 127 | "None exists and none is needed" for the research program; no data-use terms | Still true of Axivity. Third parties (McRoberts, van Hees) offer paid analysis, and one recommended tool carries a licence restriction |
| comparison-matrix.md | 86 | Axivity AX3 / AX6 Temp column: "No" | AX3 and AX6 record internal device temperature |
| comparison-matrix.md | 54 | "No cloud, no API" | No cloud API is still correct, but a local device API exists |
| comparison-matrix.md | 214 | AX3 "14 days at 100 Hz, 30 days at 12.5 Hz (vendor)" | Correct for the product page, but the vendor datasheet also says "up to 21 days" (conflict) |

## For the coordinator to check by hand

- `facts/movesense.yaml` line 941 has a YAML error that stops `weekly.py` and `generate.py` for every company until it is fixed (presumably another judge is mid-write).
- The UK Biobank PDF figures (O2) come from the gap hunter and were not re-probed.
- The McRoberts service link: whether McRoberts still offers Axivity services.
