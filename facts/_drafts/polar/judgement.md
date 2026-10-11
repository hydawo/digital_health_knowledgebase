# Polar: judgement, 2026-10-11

Inputs: `A.yaml`, `B.yaml`, `gaps.md`, the starter `facts/polar.yaml` (every field unresearched), the profile `module-01-wearables/profiles/polar.md` and `module-01-wearables/comparison-matrix.md`. Output: `facts/polar.yaml`, 47 entries (37 stated, 9 not_public, 1 conflict), 15 watched pages. `validate.py --file facts/polar.yaml`: 0 errors, 0 unresearched. `weekly.py --only polar --no-state`: 45 pages, 0 quotes missing, 0 reworded, 0 unreachable. GitHub issues #835, #886 and #887 were read with `gh` (read only); nothing was opened, commented on or created.

## Coordinator's points

1. **BLE SDK licence.** Read the whole `Polar_SDK_License.txt`. It is a proprietary "Software Development Kit Limited License Agreement" with Polar Electro Oy, not an open-source licence. It is free while you comply (section 6). You may use, copy and modify it with the notice kept, for private or commercial software. The grant is worldwide, non-exclusive and non-transferable, and limited to "enabling Data transfer between POLAR product and Developer Software" (3.1). Polar keeps all ownership (4.1). There is no duty to update or support (5). The SDK and devices are not for medical use (3.2). Liability is capped at 50 euros (8). Clause 10.2 reads, as written, "terminated by Polar by either Party by providing a ninety (90) days prior written notice". Polar may also terminate immediately for a breach not cured within 7 days, or on insolvency (10.3). On termination you must delete all copies of the SDK and of Polar's Confidential Information (10.4). That clause does not name participant Data, unlike the API agreement. The schema's `licence` field applies only to platforms, so the licence is recorded under `api_platform_fees` [BLE SDK] (nature, grant, ownership, fee) and `retention_terms` [BLE SDK licence] (termination and deletion). Every quote is exact.
2. **AccessLink Elixir Biosensing vs "no raw ECG".** A wrote "No raw sensor waveforms" and B wrote "AccessLink gives no raw optical or ECG signal". Both are wrong on ECG. The AccessLink schema for `GET /v3/users/biosensing/ecg` includes a `samples` array (`recording_time_delta_ms`, `amplitude_mv`) plus quality levels, average HR, HRV, RR and pulse transit time. The resource is in beta (changelog 19.12.2023). SpO2 test results and body and skin temperature come through the same resource. The #887 staff reply says ECG/Elixir is not available over the Vantage V3 BLE SDK. That reply does not conflict with the API docs, because it covers a different route. Recorded as `stated`: the cloud API is the only route to watch ECG. The ECG sample rate is not documented.
3. **Watch-line SDK docs vs #887.** These genuinely disagree on stored 24/7 data. `PolarVantageV3andGritX2Pro.md` lists "Data export" of 24/7 HR samples, 24/7 PPi samples and skin temperature data. Polar staff (#887, and again in #886, 2026-10-05) say the Vantage V3 does not save these for SDK loading, and that they come only by online streaming. Recorded as `conflict` under `export_routes` [watch line], confidence Unclear, with both sides quoted. Offline recording is a different matter. The watch doc does not claim it, the SDK's `polar_device_capabilities.json` marks `recordingSupported: false` for the watches, and #887 says it is not supported, so there is no conflict for the watches. #887's broader sentence ("supported only by Polar H10") does conflict with the Verity Sense and Polar 360 docs. Those docs are kept as governing, and the sentence is a note on `raw_streams` [Verity Sense]. It may refer to the H10's separate internal recording, since the capabilities file also marks `recordingSupported` false for Sense and 360. Polar should clarify.
4. **Polar Research Center proposal route.** Accepted as `research_program` and `program_application`, Verified. The page asks for a research co-operation application with a research plan of up to 10 pages that includes a budget and a "proposal for Polar support (technology, money, other)". Review criteria include "value for the company", and Polar replies within two weeks. An accepted study gets a signed research agreement, and the partner handles ethics approval. All quotes are exact.
5. **Verity Sense price.** The live US store says $104.95 (exact), and A, B and the profile agree. The "~$95 (2026-08-21, not re-read)" figure is stale. It appears in comparison-matrix.md lines 131, 138 and 228, and in wearable-data-atlas.html lines 630, 634 and 750.
6. **Fitness Program EUR 9.99.** This is not from a 2025 release only. A quoted the live product page, `polar.com/us-en/fitness-program`, and the same text is on `/en/fitness-program`: "Try for free, then 9,99 €/month", exact on 2026-10-11. B's April 2025 launch release gives the same price. Recorded with both sources, Verified. Polar publishes no USD price; B's note mentions a press-reported $8.99, which was not used.
7. **ISO.** Polar publishes ISO 9001:2015 for Polar Electro Oy (Kiwa, issued 2025-06-25, valid until 2028-08-31; quote exact) and ISO 14001:2015 for Polar Electro Malaysia (SGS, valid 2024-01-08 to 2027-01-07; read on the PDF). No ISO 27001 was found. `iso27001` is `not_public`, Corroborated, with both certificates as the evidence of what Polar does certify. A web-search summary claimed the Finnish 9001 had lapsed in 2025; that summary had found the older PDF. The current certificate runs to 2028.

## Fields where A and B disagreed

| Field | A | B | Decision and reason |
|---|---|---|---|
| raw_streams (AccessLink) | "No raw sensor waveforms"; ECG and SpO2 as spot-test results | "No raw optical or ECG signal"; RR samples with H-series straps | Neither is right on ECG. The schema has ECG samples in mV (point 2). Merged: B's RR-strap quote plus the ECG schema quotes. |
| raw_streams (BLE SDK) | per device (H10, Verity Sense, Loop/360) | one combined entry | Kept A's per-device split and added a watch-line entry from the gap hunter (4a/4b), with the #887 ECG statement. |
| program_eligibility | Verified | Corroborated | Corroborated. "No published rule" is an inference from absence. |
| program_application | research route only | research route plus AccessLink self-registration | The research route only. API self-service belongs in developer_program_status. Merged the quotes from both and added the "send your application" and address quotes. |
| user_cap, academic_pricing, minimum_commitment, baa, hipaa, iso27001, soc2 (not_public) | Verified | Corroborated | Corroborated. A negative found by search is not Verified. fda_clearances stays Verified because its sources are regulator queries. |
| device_price (watches) | Vantage V3 only | Pacer, Ignite 3, Vantage V3, Grit X2 Pro | B's fuller entry; all four quotes exact. |
| subscription_price | live page, Verified | 2025 release only, Corroborated | Both sources, Verified (point 6). |
| quote_required | one entry | two scoped entries | B's split. |
| rate_limits | AccessLink only | adds Team Pro API (1 request per second) | Added B's Team Pro entry. Dropped B's "burst bucket of up to 100" from the value, because no quote supports it. |
| retention_terms | API and Flow | adds Team Pro 180 days | Merged, and added a separate BLE SDK licence entry (point 1). |
| ai_training_terms | single `unclear` entry | two scopes: licensees `not_public`, Polar's own use `stated` | Used B's split. Added the gap hunter's de-identification quote from the privacy notice and A's data-notice quote. |
| deprecations | AccessLink only | AccessLink plus SDK 8.4.0 (Xcode 27, CocoaPods) | Two scopes. Added gap 14's 7.0.0 and 8.0.0 breaking majors. The 7.0.0 quote was replaced with an exact sentence; the first one rendered with link spacing and matched only 99%. |
| dpa | `not_public` | `stated` (Team Pro processor) | `stated`, Corroborated. The privacy notice does state the processor arrangement for Team Pro. Added A's point that AccessLink is controller-to-controller, with the API-agreement quote. |
| gdpr_statement | controller roles, Data Act | GDPR compliance claim, DPF and SCCs | Merged all four quotes. Corroborated (self-claim cap). DPF registry not checked. |
| data_residency | Corroborated | Verified | Corroborated. The sources are vendor statements only. Merged in the privacy-notice quote (gap 8) and the AWS EU row. |
| fda_clearances | api.fda.gov URLs as `url` | accessdata URLs with openFDA `fetch_url`, `expect_absent` | B's form, which the README asks for. |
| developer_program_status | adds DMA gatekeeper exclusion | adds Team Pro portal | Merged, and added the Polar 360 B2B quote (gap 13). |

## Gap findings

| # | Finding | Decision |
|---|---|---|
| 1 | SDK under a proprietary limited licence, not open source; #835 | Accepted (point 1). #835 is recorded as a note on academic_vs_commercial. |
| 2 | Collaboration application process | Accepted (point 4). |
| 3 | AccessLink Elixir: wrist ECG waveform, SpO2, temperature | Accepted (point 2). The support-page "not for medical or diagnostic use" quote is exact. |
| 4a | Watch-line SDK streams; 7.1.0 SpO2 loading | Accepted into raw_streams and sampling_rates. The 7.1.0 release is not cited separately; the product doc lists "SPO2 test results". |
| 4b | SDK mode not supported on watches; exercise-wait view | Accepted (UsingSDKWithWatches.md quote exact). The PPI-stops-on-training quote is not used. |
| 4c | #887 vs per-device docs | Accepted as the watch-line `conflict` and a note on Verity Sense (point 3). |
| 5 | 24/7 PPi on 360/Loop is session-based (#886) | Accepted as its own sampling_rates scope, Corroborated (staff reply, not docs). |
| 6 | API agreement: fees reserved, deletion on termination, immediate suspension | Accepted into api_platform_fees, retention_terms and minimum_commitment. The crediting and primary-purpose clauses are not recorded as separate facts. |
| 7 | AccessLink deprecations; webhook auto-deactivation; 403 on missing consents | Accepted. Webhook quote exact; recorded in an export_routes note. |
| 8 | Residency Ireland/Sweden; de-identified R&D use | Accepted. |
| 9 | Fitness Program; Loop launch price | Fitness Program accepted. The Loop EUR/GBP price from the launch release is not added, because the live US store price is recorded. |
| 10 | ISO 9001 only | Accepted (point 7), with the ISO 14001 Malaysia certificate added. |
| 11 | Research Library 2025 counts | Rejected. Vendor usage counts are not a decision fact for these fields; the profile owner may still want to refresh lines 20 and 191. |
| 12 | Seppo Saynajakangas Science Foundation | Recorded as a note on research_program only. It is open only to Finnish students in northern Finland. |
| 13 | Polar 360 B2B white-label | Accepted into developer_program_status. |
| 14 | SDK breaking majors, iOS 15 floor, CocoaPods | Accepted (deprecations [BLE SDK]). |
| 15 | H10 drops BLE 45 s after leaving the strap | Accepted (export_routes, quote exact). |
| 16 | Verity Sense price inconsistency | Accepted (point 5). |
| 17 | RADAR-base integrates Vantage V3 and H10 | Not a vendor fact. Left for the profile. |

## Profile and matrix statements the record contradicts

| File | Line | Says | Record says |
|---|---|---|---|
| profiles/polar.md | 11 | "SDK is open source" | Proprietary SDK Limited License Agreement: free and modifiable, but Polar-owned, limited grant, terminable on 90 days' notice |
| profiles/polar.md | 18, 29, 154, 182, 198, 257, 268 | "open source" / "open-source SDK" | Same: source-available under Polar's limited licence |
| profiles/polar.md | 162, 201 | "no API deprecation risk on the raw-data path" | The SDK licence can be ended on 90 days' notice, with deletion of all SDK copies; breaking SDK majors in 2026 (7.0.0, 8.0.0; 9.0.0 drops pre-iOS 15) |
| profiles/polar.md | 136 | "No grant, discount or application process is described" (in the science-page sentence) | Documented proposal process: plan, budget, request for Polar support (technology, money, other), review on value to Polar, reply in two weeks, research agreement |
| profiles/polar.md | 44 | ECG listed for the H10 only | Watch-line wrist ECG spot tests, with waveform samples in mV, via AccessLink Elixir (beta); not via the BLE SDK |
| profiles/polar.md | 147 | AccessLink contents with no biosensing, ECG or SpO2 | Elixir biosensing: body and skin temperature, wrist ECG and SpO2 test results |
| profiles/polar.md | 48, 49, 51 | Temperature, SpO2 and barometer "Unclear" | Watch line streams skin temperature and pressure over the SDK; SpO2 test results via SDK export and AccessLink |
| profiles/polar.md | 108 | Watch-line per-device rates "not retrieved ... Unclear" | Accelerometer 50 Hz, 8 g documented; other settings to be queried from the device; stored 24/7 data in conflict |
| profiles/polar.md | 112 (and matrix 108) | "24/7 PPI samples" with no qualifier | Session-based, automatically triggered, schedule undocumented (Polar staff, #886) |
| profiles/polar.md | 170 | Watches mean "losing raw ECG" | True for the SDK; ECG spot-test waveforms are available through AccessLink |
| profiles/polar.md | 178 | "Certifications and data residency were not checked" | ISO 9001 (to 2028-08-31) and ISO 14001 (Malaysia) only, no ISO 27001 or SOC 2; data stored in Ireland and Sweden on AWS EU |
| profiles/polar.md | 184 | "No subscription for core functionality" | Still true, but an optional Fitness Program costs EUR 9.99 a month |
| profiles/polar.md | 185 | "no documented API fee" | Free at present, but the API agreement reserves the right to charge fees |
| comparison-matrix.md | 50, 106, 107, 108, 127, 228, 328, 398 | "Open BLE SDK" / "open SDK" / "Free, open SDK" | Polar's limited licence, not open source |
| comparison-matrix.md | 131, 138, 228 | Verity Sense "~$95 (2026-08-21, not re-read)" | $104.95 (US store, 2026-10-11) |
| comparison-matrix.md | 228 | Subscription "None"; "AccessLink no fee" | Optional Fitness Program EUR 9.99/month; API fees reserved |
| comparison-matrix.md | 255 | Polar certifications/residency "Not checked" | ISO 9001/14001 only; EU (Ireland, Sweden) |
| comparison-matrix.md | 398 | "No formal programme; 'Collaborate with us' contact"; API agreement "not summarised" | Documented proposal route; API agreement terms recorded (30-day notice, immediate suspension, deletion on termination, fees reserved) |
| module-01-wearables/wearable-data-atlas.html | 630, 634, 750 | Verity Sense "~$95" | $104.95 |

## For the coordinator to check by hand

- Whether Polar will clarify #887 against its own watch-line doc (24/7 HR and PPi read-back) and against the Verity Sense and Polar 360 offline-recording docs. Any further reply in that issue should be read; nothing was posted.
- The ECG sample rate in AccessLink Elixir data is undocumented. A real API response would settle it.
- DPF participation (gdpr_statement) was not checked on the Commerce Department registry.
