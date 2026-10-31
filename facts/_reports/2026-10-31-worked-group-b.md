# Group B worked (Activinsights, Axivity, Ametris, Movesense, Polar), 2026-10-31

Fact keeper pass for the monthly vendor-fact re-check, limited to activinsights-geneactiv, axivity,
ametris-actigraph, movesense and polar. Work list: the 59 facts due by 2026-11-10 that the automatic
extension could not confirm (not_public, unclear, conflict and not_applicable facts, plus every
Activinsights fact, since its site is terms-blocked), and this group's items in
`facts/_reports/2026-10-31.md`. Every quote listed below was re-probed today with
`tools/facts/quote_probe.py` and came back exact. `python3 tools/facts/validate.py`: 35 companies,
1340/1340 facts, 0 errors. `generate.py` not run (the coordinator runs it).

Nothing changed. No value, status or confidence moved. Axivity, Ametris, Movesense and Polar were
all re-read live: 29 facts re-verified, `retrieved` set to 2026-10-31 on every source re-read, and
`recheck_by` moved to 2026-11-30. All 30 Activinsights facts wait for a browser, because
activinsights.com's website terms forbid automated collection.

## Items

### Quotes missing

None for this group.

### Quotes reworded

None for this group.

### Dead links

None for this group.

### Check by hand

All 29 activinsights.com URLs in the report's "Check by hand" section are `terms_blocked`. Nothing
was fetched from activinsights.com, by script or by WebFetch. See "Needs a browser or vendor".

### Work list: re-verified, unchanged

| Company | Field | What I found | What I changed | Confidence |
|---|---|---|---|---|
| axivity | research_program | Home, support, FAQ, contact, Biobank case study and ax3-research.md read. Still no named program. The research guide still lists McRoberts and Vincent van Hees as third-party help | retrieved, recheck_by 2026-11-30 | not_public, Corroborated (unchanged) |
| axivity | program_eligibility, program_application, program_status, user_cap, subscription_price | Store unchanged: AX3 GBP 139 to 149, AX6 GBP 199 to 209, add-to-cart, no account, no subscription | retrieved, recheck_by | not_applicable (unchanged) |
| axivity | academic_pricing | No academic or volume discount on products, product, shipping, FAQ or contact pages | retrieved, recheck_by | not_public, Corroborated (unchanged) |
| axivity | minimum_commitment | No minimum stated. Warranty page still "a period of ONE YEAR" | retrieved, recheck_by | not_public, Corroborated (unchanged) |
| axivity | history_depth [AX3] | All four quotes exact: datasheet "up to 21 days" and "30 days at 12.5 Hz or 14 days at 100 Hz", product page "30 days @ 12.5Hz; 14 days @ 100Hz", Open Movement FAQ table | retrieved, recheck_by | conflict, Unclear (unchanged) |
| axivity | rate_limits | AX3-GUI wiki still describes USB-only transfer | retrieved, recheck_by | not_applicable (unchanged) |
| axivity | ai_training_terms | Privacy policy and terms have no AI, ML or training terms | retrieved, recheck_by | not_applicable (unchanged) |
| axivity | deprecations | No announced end-of-life. Both quotes exact. Firmware page unchanged: AX3 V50 experimental (2020-05-19), V48 newest standard, AX6 V56 (2019-12-09) | retrieved, recheck_by | not_public, Corroborated (unchanged) |
| ametris-actigraph | user_cap [CentrePoint] | No participant, device or study limit on the CentrePoint page, API docs repo or store | retrieved, recheck_by | not_public, Verified (unchanged) |
| ametris-actigraph | device_price [Vendor list prices] | Store still lists accessories only (LEAP wristband 25.00 USD, CPIW dock 45.00 USD); product pages still "Request a Quote" | retrieved, recheck_by | not_public, Verified (unchanged) |
| ametris-actigraph | subscription_price | No consumer product or membership | retrieved, recheck_by | not_applicable, Verified (unchanged) |
| ametris-actigraph | academic_pricing | Academic site still offers "Get Pricing List"; "Pricing is calculated for each unique order" | retrieved, recheck_by | not_public, Verified (unchanged) |
| ametris-actigraph | api_platform_fees [ActiLife Data Vault storage] | All three quotes exact: product page and upgrade FAQ say 20GB, the ActiLife 7 manual says 4GB | retrieved, recheck_by | conflict, Unclear (unchanged) |
| ametris-actigraph | minimum_commitment | No minimum order or term on CPIW, ActiLife, CentrePoint or store pages | retrieved, recheck_by | not_public, Verified (unchanged) |
| ametris-actigraph | history_depth [CentrePoint cloud] | Both quotes exact (raw-request "SHALL NOT" rule, "reprocessed indefinitely"); no retrieval limit published | retrieved, recheck_by | unclear, Unclear (unchanged) |
| ametris-actigraph | ai_training_terms | Privacy policy still only "providing or developing the Ametris platform"; Signant release still names AI and ML as a direction; compliance page silent | retrieved, recheck_by | not_public, Corroborated (unchanged) |
| movesense | program_application [Movesense Academic Program] | All four quotes exact. Program page says monthly, form says weekly. Form still open (no closed notice) and still names Suunto | retrieved, recheck_by | conflict, Verified (unchanged) |
| movesense | sampling_rates [IMU] | All four quotes exact: API example to 1666 Hz, Flash kit to 416 Hz, HR2 to 833 Hz, BLE bandwidth warning | retrieved, recheck_by | conflict, Verified (unchanged) |
| movesense | rate_limits, ai_training_terms [Own app or developer tools] | FAQ quote exact: data "does not go to Movesense servers" | retrieved, recheck_by | not_applicable, Verified (unchanged) |
| polar | user_cap | AccessLink still scales rate limits with registered users ("500 + number of users x 20"); no cap in the docs, API agreement or SDK repo | retrieved, recheck_by | not_public, Corroborated (unchanged) |
| polar | academic_pricing | No academic or volume discount on research-tools, business/science, collaborate-with-us or business pages | retrieved, recheck_by | not_public, Corroborated (unchanged) |
| polar | minimum_commitment [Business and B2B] | Polar 360 and business pages state no minimum | retrieved, recheck_by | not_public, Corroborated (unchanged) |
| polar | export_routes [BLE SDK, stored 24/7 data on watch line] | All four quotes exact. The SDK product doc still lists 24/7 HR, PPi and skin temperature under data export. Issue 887 was closed as completed on 6 Oct 2026, staff reply unchanged | retrieved, recheck_by | conflict, Unclear (unchanged) |
| polar | ai_training_terms [API and SDK licensees] | API agreement still "Latest update: 22 August 2025"; neither it nor the SDK licence mentions AI or ML | retrieved, recheck_by | not_public, Corroborated (unchanged) |

### Work list: Activinsights, sources outside activinsights.com only

The non-blocked sources were re-read and probed exact, and their `retrieved` date set to
2026-10-31. Fibion's two GBP 425 to 510 quotes are still there. The First Nation Group reseller page
is still quote-only. The App Store quotes ("Only for Mac Free", "Adds full support for GENEActiv
1.3 devices"), the GGIRread 1.0.11 release note, the CRAN GENEAread description, and both Play Store
quotes ("Data can’t be deleted", "Rebrand with support for both GENEActiv and ActivInsights Band
devices") are unchanged. That covers device_price [GENEActiv], subscription_price [GENEActiv],
raw_streams [GENEActiv], export_routes [GENEActiv], retention_terms and deprecations. Each of these
facts also rests on activinsights.com pages, so `recheck_by` stays at 2026-11-10 for all 30.

## Prose fixed

None. No fact changed, so no profile prose is contradicted.

## Shared-file edits needed

None.

## Needs a browser or vendor

- **Activinsights, all 30 work-list facts (due 2026-11-10).** These are research_program,
  program_eligibility, program_application, both user_cap scopes, both academic_vs_commercial
  scopes, both device_price scopes, both subscription_price scopes, academic_pricing, both
  api_platform_fees scopes, minimum_commitment, quote_required, raw_streams, derived_metrics,
  sampling_rates and history_depth (GENEActiv and Band each), export_routes (both scopes),
  rate_limits, retention_terms, ai_training_terms and deprecations. Every one cites activinsights.com,
  whose terms forbid "systematic or automated data collection". Open the 29 URLs listed under
  "Check by hand" in `facts/_reports/2026-10-31.md` in a browser, confirm each quote, then set
  `retrieved` and `recheck_by` (2026-11-30, or 30 days from the read). Worth checking while there:
  the GENEActiv history_depth conflict (IFU Rev.010 per-version table, 44 days at 20 Hz, against 60
  days on the product sheet), whether an ActivInsights Band price or sampling rate is now published,
  and whether a renewed ISO 27001 certificate has been posted (the last one expired 2025-10-31).
  This is already item 17 on `shared/manual-sweep.md`. The other fix is written consent from
  Activinsights for automated checks.
- **Vendor questions, unchanged from earlier passes:** Ametris, 4GB versus 20GB Data Vault
  allowance. Movesense, the monthly versus weekly review cadence, and whether 1666 Hz IMU sampling
  works on every model and over BLE. Polar, whether the Vantage V3 and Grit X2 line store 24/7 HR
  and PPi for SDK read-back (the SDK doc and the issue 887 staff reply still disagree). Axivity,
  whether an academic or volume price exists (info@axivity.com).
