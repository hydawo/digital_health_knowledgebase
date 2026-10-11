# m-Path: judgement (baseline run, 2026-10-11)

Final record: `facts/m-path.yaml`. 35 facts: 27 stated, 5 not_public, 1 conflict, 1 unclear, 1 not_applicable.
Every quote was rechecked with `quote_probe.py` on 2026-10-11 and every one came back `exact`. `validate.py --file`
gives 0 errors with no field left unresearched. `weekly.py --only m-path --no-state` checked 40 pages: 0 quotes
missing, 0 reworded, 0 dead links.

## Where A and B disagreed

| Field | A | B | Decision |
|---|---|---|---|
| data_residency | conflict (Azure Frankfurt vs KU Leuven in privacy statement) | stated, Azure Frankfurt, Verified | **conflict**, confidence Unclear. I read `LegalPage/privacy.html`. It names "The KU Leuven" as host for both the App and the Dashboard, and KU Leuven is not on the current sub-processor list. The storage page (updated October 9, 2026), the FAQ and the sub-processor list all say Azure Frankfurt. B missed the privacy statement. Most likely a migration the privacy statement never caught up with, but nothing on the site says so. |
| history_depth | stated, Verified | unclear | **stated, Corroborated.** The documented parts hold up: data stays after a plan lapses, Thryve has a researcher-set expiry window, and Garmin Lite has a `syncWindowHours` setting. B's actual point, that Thryve backfill isn't documented, went into the value and the note. |
| academic_vs_commercial | Verified; value said clinical use is barred "without consent" | Corroborated | **Corroborated.** A's "without consent" isn't in clause 11.4, which bars clinical or medical services outright, so it was removed. Added the /clinical/ therapy-marketing quote and a note on the tension (point 5). |
| subscription_price | price grid only | flagged that the cards' labels run in reverse | Kept A's grid and added B's note. The pricing page tabs go 300 to 600, but each card lists "600 ... 300 participants per year" next to prices that rise. The manual table (300 = EUR 1,599 / 2,099 / 3,099) settles it. Added the 1,000-slot row from the manual. |
| api_platform_fees | Sensing full "includes Garmin direct and Garmin Lite" | Sensing full "includes Sensing lite and the direct Garmin integrations" | The manual says Sensing lite is included in full. The which-integration page lists Sensing full as the add-on the direct Garmin route needs. The Garmin Lite page calls Garmin Lite its own add-on (Standard or Comfort, no published price), so A's Garmin Lite claim was dropped. Also dropped "yearly" for every add-on: only Oura and the white-label update fee are stated per year. |
| academic_pricing | Verified, slot-recovery rules | Corroborated, SAM.gov and reverse charge | Merged. Verified, because the "Research & Academic Licenses" title and the recovery rules are both stated outright. |
| hosting_price | Verified | Corroborated | Verified. The included-hosting and custom external-server statements are both direct. |
| rate_limits | not_public, Unclear | not_public, Verified | not_public, Corroborated. Several pages checked, but it's an absence. |
| baa / iso27001 / soc2 | not_public, Unclear | not_public, Corroborated | Corroborated, matching the other records. |
| fda_clearances | openFDA URLs as `url` | accessdata URL plus openFDA `fetch_url` | B's format, per the README, with `expect_absent: true` as in the Polar record. Kept A's note on the unrelated K946356 guidewire. |
| deprecations (source type of /legal/) | vendor_page | vendor_legal | vendor_legal. |
| retention_terms | stated with reconciling note | stated | Both stated. See point 4 below. |
| app_availability | download counts, review count in quote | descriptive quotes | Merged. Package ids and App Store ids are in the value. Replaced A's quote with "50K+ Downloads", because A's included the review count and would break whenever it changed. |

All other fields matched in substance. For each one I kept the better-sourced entry and pulled in the other researcher's useful quotes.

## Points the coordinator asked me to settle

1. **Data residency:** recorded as `conflict` (see above). Sources: the storage page, FAQ, sub-processor list, privacy statement and DPA clause 1.7 (EU/EEA unless the controller is in a third country), plus the pCloud/OneDrive/SFTP cloud page. The value says continuous sensing, Garmin-direct and media data bypass m-Path and go to the researcher's own storage. It also notes that Thryve data passes through the manufacturer's servers and Thryve first, per the which-integration page.
2. **Pricing:** confirmed against the manual table: 300 slots EUR 1,599 / 2,099 / 3,099, 1,000 slots EUR 4,441 / 5,829 / 8,607, 3,000 slots EUR 9,043 / 11,380 / 16,593. Add-ons are Standard plan and up, scale above 1,000 slots, one-year minimum, no auto-renew. The reversed card labels are in a note.
3. **Clause 11.7:** confirmed word for word. Clause 1.17 defines "User" to include Participant. A search of the Terms found no AI, artificial-intelligence or training clause. `ai_training_terms` is `unclear`, with the clause 10.3 own-purposes quote and the DPA instructions-only quote.
4. **Deletion:** after reading both, I don't see a conflict. A lapse drops the account to the Free plan, so services continue and DPA 8.1's "services ended" trigger never fires. Recorded as stated with a note. What's left unanswered is whether data on a Free-plan account is ever deleted without a request. Added the 8.1 CSV-return quote.
5. **Clinical use:** clause 11.4 bars use "to provide clinical or medical services", while /clinical/ ("m-Path for Therapy") markets in-session therapy use. Recorded in `academic_vs_commercial` with both quotes. Not made a conflict, because the field is about access tiers, not permitted use.
6. **HIPAA:** claimed on the homepage, FAQ and research page only. No BAA (`baa` not_public). ISO 27001 and SOC 2 are cited only for Azure (`iso27001`, `soc2` not_public).
7. **Apps:** both Play listings and both App Store listings confirmed. m-Path Sense is CARP-based (manual quote in `raw_streams` and `licence`).
8. **Garmin direct vs Thryve:** HR from 1 s (default 30 s), all BBI, 25 Hz accelerometer, 32 Hz gyroscope, steps locked at 60 s. Thryve is "Lower resolution but includes computed measures". Both are in `raw_streams` and `sampling_rates`.
9. **Institution count:** "Institutions 150+" on /landing/research/, in `research_program`. "250+" no longer appears on the page.

## Gap-hunter findings

| # | Finding | Decision |
|---|---|---|
| 1 | Azure Frankfurt vs KU Leuven host | Accepted; drives the `data_residency` conflict. The 2023 storage snippet wasn't probed, so it's mentioned only as context in the note. |
| 2 | DPA and sub-processor list | Accepted (`dpa`, `retention_terms`, `data_residency`). |
| 3 | Clause 11.7 licence; User includes participants | Accepted (`ai_training_terms`). |
| 4 | 150+ institutions, not 250+ universities | Accepted (`research_program`). |
| 5 | Both apps on Google Play | Accepted (`app_availability`). The Niemeijer calls/SMS caveat went into the `raw_streams` note. The beta channel and PROfeel app weren't added (no field for them). |
| 6 | Sensing data to pCloud, OneDrive or SFTP | Accepted (`export_routes`, `hosting_options`, `hosting_price`, `data_residency`). |
| 7 | Sensing Full stream list incl. gyroscope, call/text | Accepted (`raw_streams`), with a note that the sensor table doesn't list them. |
| 8 | Thryve, Oura surcharge, non-integrated devices, Garmin routes | Accepted (`raw_streams`, `api_platform_fees`). |
| 9 | m-Path Keyboard | Accepted (`raw_streams`, `derived_metrics`, `export_routes`). No price found. |
| 10 | mpathr and mpathsenser on CRAN | Accepted (`licence`, `export_routes`). |
| 11 | Bulk export paid-only | Accepted (`export_routes`). |
| 12 | One-year minimum, 3-month extension, slot prices | Accepted (`minimum_commitment`, `subscription_price`). The Prolific-needs-premium detail wasn't added (no field for it). |
| 13 | m-Path Software BV, 2024 spin-off | Accepted as a note in `research_program`. No quote added; the company number wasn't needed. |
| 14 | Research-page HIPAA claim, 2FA | HIPAA quote accepted (`hipaa_statement`). 2FA not recorded (no field). |
| 15 | Samsung deep sleep | Rejected for the record (no schema field). It's a profile Participant Experience item. |

## Profile and matrix statements the record contradicts

Profile: `module-02-digital-phenotyping/profiles/m-path.md`. Matrix: `module-02-digital-phenotyping/comparison-matrix.md`.

| File | Line | Says | Record says |
|---|---|---|---|
| profile | 7 | "KU Leuven-affiliated research team ... 250+ universities per vendor claim" | Operated by m-Path Software BV, a 2024 KU Leuven spin-off. The research page now claims 150+ institutions (`research_program`). |
| profile | 10 | Google Play listings "were not located ... (Unclear)" | Both apps are on Google Play: io.m_Path.kuleuven and io.m_Path_Sense.kuleuven (`app_availability`). |
| profile | 12, 83, 131, 145, 157 | External servers scope "not stated"/"unconfirmed"; vendor SaaS the only route | Answer data can be stored on the customer's servers for a development cost. Sensing, Garmin-direct and media data always go to the researcher's pCloud, OneDrive or SFTP (`hosting_options`, `hosting_price`). |
| profile | 13, 106 to 109 | Prices given as 300 to 600 participants, up to EUR 5,338 | Plans run 300 to 3,000 slots, up to EUR 16,593 (Comfort, 3,000) (`subscription_price`, `user_cap`). |
| profile | 34 to 53 | Accelerometer, gyroscope, light, screen, app usage, battery, connectivity, Wi-Fi, calls, SMS and keyboard all Unclear | Documented in the manual. Several are Android-only (screen, app usage, light, memory); calls and texts are anonymised; there is a keyboard (`raw_streams`). |
| profile | 55 | "manual's sensor sub-pages were not reached"; sampling configurability Unclear | Sampling is researcher-set per periodic sensor; location every minute (Android) or every 10 m (iOS) (`sampling_rates`). |
| profile | 75 (per gap hunter) | Export "not verified" | Single-participant export on all plans, bulk CSV on paid plans, wearable JSON, cloud/SFTP upload, R packages (`export_routes`). |
| profile | 98 | "No SOC 2, ISO 27001, or DPA-template document was located"; separate `Privacy_Policy_m-Path_Sense.html` | A DPA (Annex 1 of the Terms) is published (`dpa`). There is a single privacy statement for app and dashboard, and it names KU Leuven as host, which conflicts with Azure Frankfurt (`data_residency`). ISO 27001 and SOC 2 are cited for Azure only. |
| profile | 111, 130 | Add-on billing period not stated; Smartwatch add-on with Fitbit, Garmin, Apple Watch | Add-ons attach to the one-year subscription, are available from Standard up, and scale above 1,000 slots. Smartwatch runs through Thryve; Oura costs EUR 3,000 a year more; Empatica, movisens and ActiGraph aren't integrated; direct Garmin needs Sensing full (`api_platform_fees`, `raw_streams`). |
| profile | 126, 134, 171 | "250+ universities" | "Institutions 150+" (`research_program`). |
| profile | 153 | "a formal DPA template remain[s] unconfirmed" | DPA published (`dpa`). |
| profile | 155 | Which wearables, and how they relate to the Smartwatch add-on? | Answered: Thryve (Garmin, Fitbit, Apple Health, Polar), Oura extra, direct Garmin via Sensing full, and Garmin Lite (`raw_streams`, `api_platform_fees`). |
| matrix | 53 | Google Play listing not located (Unclear) | Both apps on Google Play (`app_availability`). |
| matrix | 75 | External servers "scope not stated"; no other hosted option | As in profile lines 12 and 83 above. |
| matrix | 117 | Streams limited to GPS, Bluetooth, pedometer/activity, noise (Reported); smartwatch add-on names Fitbit, Garmin, Apple Watch | Full stream list (`raw_streams`). Thryve route, Oura surcharge, direct Garmin at 1 s HR / 25 Hz accelerometer. |
| matrix | 136 | EUR 1,599 to 5,338 (300 to 600 participants); add-on billing period not stated | Plans go to 3,000 slots and EUR 16,593. Add-ons attach to the yearly subscription and are available from Standard up. |
| matrix | 160 | "Separate privacy policy for m-Path Sense"; "No SOC 2, ISO or DPA template located" | DPA published; single privacy statement; residency conflict. |
| sources.md | 141 | S-MP-03 "250+ Universities" claim | Page now says "Institutions 150+". |

## For the coordinator to check by hand

- **Data residency:** worth asking m-Path directly which host is current and whether the privacy statement is due for an update. Its line "Our legal documents will be updated on November 1, 2025" is still up nearly a year later.
- **Clause 11.7 and clinical use:** two written questions for the vendor. Does 11.7 apply to participant responses held under the DPA? How does the therapy product fit with clause 11.4?
- **Free-plan data:** ask whether data on a Free-plan account is ever deleted without a request.
- **Garmin Lite:** no published price.
- **Pricing labels:** the reversed participant labels on the pricing cards could confuse the weekly check if m-Path fixes the order. The quoted card string "€ 1599 € 2052 € 2505 € 2958 Prices are excl. VAT per year" only carries prices, so it should survive a label fix.
