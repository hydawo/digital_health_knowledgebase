# Judgement: sensor-bio (2026-10-21)

Inputs: A.yaml and gaps.md (2026-10-11), B.yaml (2026-10-21), the coordinator's nine points, and the
live pages re-read on 2026-10-21. A's and the gap hunter's quotes were re-probed today. Final record:
`facts/sensor-bio.yaml`, 32 facts (16 stated, 14 not_public, 2 conflict), 15 watched pages. Every
quote (61) returned "exact" from `quote_probe.py` on 2026-10-21. `validate.py --file
facts/sensor-bio.yaml`: 0 errors, 0 unresearched, 0 overdue. `weekly.py --only sensor-bio
--no-state`: 26 pages, 0 quotes missing, 0 reworded, 0 dead links, 0 check by hand.

## Things that changed after the drafts were written

1. **API reference rewritten between 2026-10-11 and 2026-10-21.** `developers.sensorbio.com/swagger.json`
   no longer carries a version number (A recorded v1.4.0), no longer mentions getsensr.io anywhere, and
   no longer has a full OAuth2 section. Three of A's quotes are gone: "Developer access must be enabled
   on your account. Contact developers@sensorbio.com" (now "Contact developers@sensorbio.com if your
   account does not yet have this feature."), "The old getsensr.io hostnames will continue to work
   until 30 September 2026," and "A short-lived Bearer token representing a single end user's
   delegated". Replaced where a current sentence says the same thing; the hostname sentence has no
   replacement and is described in the `deprecations` note only. No Wayback snapshot of the swagger
   file exists (CDX returned none).
2. **Terra launched a Sensor Bio integration (July 2026) and deprecated its Biostrap one.** Not in
   either draft or the gap hunt (the gap hunt only had the older Biostrap integration page). Added to
   `export_routes` and `deprecations`, quoted from Terra's July changelog. This matches
   `facts/terra.yaml`, which already says "Biostrap deprecated".
3. **The two timeseries endpoints** are still documented with "will be discontinued on 30 September
   2026", three weeks after that date. Not tested (needs a key).

## Coordinator points

1. **Sampling (conflict kept).** The exact press wording is "captures raw physiological signals at
   15,000 samples per second". It names no channel, sensor, ADC or aggregate. An aggregate across the
   exported channels cannot produce it (3 PPG wavelengths plus 3 accelerometer axes at the 100 Hz
   ceiling is 600 per second), so the text gives no basis for reading it as a different measure.
   Recorded as `conflict`, Unclear, with 100 Hz as the documented researcher-facing ceiling in the
   note.
2. **Raw access (conflict, scoped).** The V2 page states the gate twice ("gated to enterprise-tier
   accounts"; "available to partners on enterprise-tier accounts"). The Polar comparison page says raw
   waveform export is "the default data product for every partner, not a gated upsell", and its SDK
   paragraph ends "No separate license. No gated tier." where the V2 page's identical paragraph ends
   with the enterprise-tier sentence. The "No gated tier" sentence alone could refer to SDK data, but
   the "default data product" sentence is about raw waveform export directly, so this is a genuine
   conflict. Recorded as a second `raw_streams` entry (scope "Sensor Bio V2, who can get raw export").
3. **Gyroscope (scoped per device).** V2 entry: three sensors, no gyroscope. EVO entry: gyroscope via
   the RPM dashboard and the EVO-only raw-download endpoint, whose description lists "accelerometer,
   gyroscope, or PPG waveform". The Science page sentence names no device; it is cited under EVO with a
   note explaining why.
4. **API.** Raw-download endpoint deprecated and EVO-only (quoted). Timeseries discontinuation quoted.
   Hostname retirement: in the value as "read 2026-10-11, text since removed", not quoted. Both old
   hostnames still answer with 404 at the root, as do the new ones, so retirement is not confirmable
   from outside. Developer access by email to developers@sensorbio.com (quoted). OAuth2: the reference
   still describes an OAuth2 Bearer token with in-browser consent; the MCP server README (last push
   2026-02-19) says Org API Key is the only supported method for third parties. Its authorization_code
   sentence probes as "reworded" (0.989) because of markdown backticks, so the adjacent sentence is
   quoted. Recorded inside `developer_program_status` as unclear, with confidence Verified for the rest
   of that fact.
5. **Pricing.** All pricing fields `not_public`; `quote_required` stated. The $80 is quoted in
   `device_price` with a note that it is Sensor Bio's own hardware cost beside its gross margin, not a
   price.
6. **FDA.** `not_public`, Verified, with the eight openFDA searches re-run today (all "No matches
   found"). V2's general-wellness statement quoted. The note says the Thermo Patch "FDA Cleared" label
   comes only from the legacy biostrap.com research page and is not a Sensor Bio clearance.
7. **Privacy policy.** Effective date, consent and Privacy Shield reliance all quoted in
   `gdpr_statement`. The three entity names (Sensr Biotech, INC. in terms and policy; Sensr Biotech,
   LLC on the App Store; Sensor Bio Inc. in the footer and the policy's contact block) are in the `dpa`
   note.
8. **HIPAA.** `stated`, scope legacy biostrap.com, confidence Reported (B had Corroborated).
9. **Recheck dates.** 2026-11-20 for research access, pricing and data access; 2027-01-19 for
   compliance.

## Fields where A and B disagreed

| Field | A | B | Decision |
|---|---|---|---|
| developer_program_status | stated, public API reference at developers.sensorbio.com, access on request | stated, Corroborated, "no public API documentation" | A. B missed developers.sensorbio.com, which is live. Rewritten for the changed reference (see above). |
| program_eligibility | not_public | stated, "Built for IRB-approved studies..." | stated (B), with a note that the sentence describes the target market and is not an admission rule. |
| sampling_rates | stated, 50/25/100 Hz | conflict with the 15,000 press figure | conflict (B), per coordinator point 1. |
| raw_streams | two entries (V2, EVO), gyroscope scoped to EVO | one entry, gyroscope flagged in a note | A's split kept and a third entry added for the tier conflict from the gap hunt. |
| export_routes | dashboard, REST API, SDK | dashboard, "cloud API", SDK, Terra/Spike, Privacy Center download | Merged. Kept B's participant download quote; replaced B's Terra quote with Terra's July 2026 changelog. Dropped B's Science-page EMR/EHR quote (marketing, no route described). |
| rate_limits | not_public, from the API reference | not_public, "no public API documentation" | A's reasoning (the reference exists and documents no request-rate limits). |
| deprecations | API endpoint and hostname dates | brand retirement only, "no dated shutdown" | Merged; B's "no dated shutdown" is wrong given the API reference. |
| ai_training_terms | not_public | not_public, with the "sell Aggregate Information" quote | not_public; the aggregate-disclosure point is kept in the note. |
| baa, dpa | Unclear | Corroborated | Corroborated. The searches are thorough and agree; Unclear understated them. |
| iso27001, soc2 | Verified | Corroborated | Corroborated, consistent with baa and dpa for absences of a self-claim. |
| hipaa_statement | Reported | Corroborated | Reported, per coordinator point 8. |
| data_residency | Verified | Corroborated | Verified. AWS hosting is a fact about the vendor's own infrastructure, not a compliance self-claim. |
| program_status | rebrand | rebrand, CEO, App Store version 26.39.2 | Merged with CEO and V3 mention from the gap hunt. Dropped the App Store version and date: the listing now shows a newer release ("1d ago"). |
| subscription_price | not_public, legacy add-ons | not_public, app free with activation code | Merged. The activation-code detail was not re-confirmed on the listing today and is left out. |

## Gap-hunter findings

| # | Finding | Decision |
|---|---|---|
| 1 | Hz figures published; 15,000 conflict | Accepted (`sampling_rates` conflict). |
| 2 | V2 not FDA cleared; no FDA records; Thermo Patch claim legacy only | Accepted (`fda_clearances`). App Store disclaimer not added (the V2 page is stronger). |
| 3 | V2 has no gyroscope | Accepted (`raw_streams` V2 and EVO scopes). |
| 4 | Raw export tier: spec vs Polar page | Accepted as a `raw_streams` conflict entry. |
| 5 | CEO change, continuity pages, V3 | Accepted (`program_status`). |
| 6 | AHA Innovators' Network | Accepted as a note in `research_program` only; it is not an access route. |
| 7 | Terra, Labfront, legacy org-token API | Terra accepted and updated to the July 2026 changelog. Labfront (re-probed exact, dated Jan 18, 2024) and the partnerships page (re-probed exact) are in the `export_routes` note as unconfirmed for V2. |
| 8 | Export windows, formats, SDK version, live stream | Accepted (`export_routes`, `raw_streams`). |
| 9 | Retention per deployment, AWS, 14-day buffer | Accepted (`retention_terms`, `data_residency`, `history_depth`). |
| 10 | Sold through partnership; $80 hardware cost | Accepted, with the cost labelled as not a price. |
| 11 | Legacy legal text, entity names, Privacy Shield, aggregate sharing | Accepted (`gdpr_statement`, `dpa` note, `ai_training_terms` note). |
| 12 | CE, UKCA, FCC ID | Accepted as a note in `fda_clearances`; no schema field for them. |
| 13 | Flatt et al. 2025 Kairos HRV validation | Not a record field. Listed below as a profile contradiction for the coordinator. |
| 14 | "29 peer-reviewed studies" vs "14 publications and 22 clinical studies" | Not a record field. Listed below. |

## Profile and matrix statements the record contradicts

| File | Line | What it says | What the record says |
|---|---|---|---|
| module-01-wearables/profiles/emerging-platforms.md | 54 | Thermo Patch "(FDA-cleared continuous temperature, ±0.1 °C)", Corroborated | The only source is the legacy biostrap.com research page. No FDA record for Biostrap, Sensr or Sensor Bio. V2 is "not FDA cleared or approved". The profile should say the patch claim is a legacy Biostrap kit statement and not a Sensor Bio clearance, and that V2 is a general wellness device. |
| same | 55 | Raw PPG, gyroscope and accelerometer via the RPM dashboard | Gyroscope applies to legacy EVO only; V2 has PPG, accelerometer and skin temperature. Raw export is "gated to enterprise-tier accounts" per the V2 page, contradicted by Sensor Bio's Polar comparison page. |
| same | 56 | Configurable sampling, no figures | 50 Hz default, 25 or 100 Hz per organization, up to 100 Hz raw export (conflict with a 15,000 samples per second press claim). |
| same | 58 | Integration "API or Bluetooth SDKs", Reported | Public REST API reference at developers.sensorbio.com (keys on request); SDK interface v0.17.0; raw REST download is EVO-only; Terra has a Sensor Bio integration since July 2026. |
| same | 59, 81-82 | "14 publications and 22 clinical studies"; most recent registered trial from 2022 | The May 2026 press release says "validated across 29 peer-reviewed studies" (gap hunter, vendor-compiled). Flatt et al. 2025 (Sensors 25(10):3165, PMC12115943) is a Kairos HRV validation with a disclosed 2018 Biostrap consulting link. |
| same | 61 | HIPAA claims, "Corroborated at most" | Claims are only on legacy biostrap.com pages; record has Reported. |
| same | 78 | Access terms, user caps, retention and pricing not published | Retention is configured per deployment; account deletion 30/90 days. User caps and pricing remain unpublished. |
| same | 81 | "Sampling rates undocumented ... no Hz figures" | See line 56. |
| module-01-wearables/comparison-matrix.md | 62 | "API or Bluetooth SDKs (R)" | As profile line 58. |
| same | 86 | Thermo Patch (C) | As profile line 54. |
| same | 117 | "with gyroscope"; "no Hz figures published" | Gyroscope is EVO only; Hz figures published for V2. |
| same | 341 | "no Hz figures or prices" | Hz figures published; prices still not public. |
| same | 412 | Retention and AI-training terms "Not published" | Retention is configured per deployment, with deletion in 30/90 days; AI-training terms are still not published. |
| shared/unresolved-questions.md | 289 (Q68) | Open on Hz figures and pricing | Hz figures answered for V2 (with the 15,000 conflict); pricing still open. |
| same | 369 (Q48) | Resolved as "PPG, gyroscope and accelerometer" | Gyroscope is EVO only. |

## For the coordinator to check by hand

- Ask developers@sensorbio.com: is per-user OAuth2 live; what does 15,000 samples per second
  measure; does an academic study need an enterprise-tier account for raw export; is raw REST export
  for V2 still planned.
- Whether the two timeseries endpoints and the getsensr.io hostnames actually stopped working after
  30 September 2026 (needs an API key).
- Which legal entity signs contracts (Sensr Biotech, INC. vs Sensr Biotech, LLC vs Sensor Bio Inc.).
- The developer reference changes fast (rewritten within ten days). Expect `developers.sensorbio.com`
  to trigger in the weekly check.
