# Judgement: circular (2026-10-22)

This was the cheaper variant. Inputs were `A.yaml` and nothing else: there was no `B.yaml` and no `gaps.md`. In place of
an A-versus-B comparison, I audited A against its sources, spot-checked its `not_public` and `unclear` calls, and ran a
short gap sweep of my own. Output: `facts/circular.yaml`, 30 facts (20 stated, 7 not_public, 2 unclear, 1 conflict).
Confidence: 21 Verified, 4 Corroborated, 2 Reported, 3 Unclear. Watch list: 14 pages.

I probed every quote in A first. All 52 came back `exact 1.0`, so no change below was about a bad quote. In the final
record I re-probed all 67 quotes and every one is `exact 1.0`. `validate.py --file facts/circular.yaml` gives 0 errors and
0 unresearched. `weekly.py --only circular --no-state` gives 0 missing and 0 reworded.

## Audit of A: what I changed and why

| Field | A had | Change | Why |
|---|---|---|---|
| program_status | Value called Circular Health Limited "a Hong Kong company registered in Paris". The note cited BODACC record A202502091404, published 2025-10-30, "read through the BODACC open-data API". | Value now says the terms name Circular Health Limited, registered in the Paris trade register under 990 900 326, and that the founders told press the headquarters moved to Hong Kong. Added the Gadgets & Wearables quote for the Hong Kong move. **Dropped the BODACC record number and publication date** from the note. | The terms of use and sale give only a Paris registered office (1 Rue Marguerin). "Hong Kong" appears nowhere on Circular's pages, only in press relaying the founders. I checked bodacc.fr's robots.txt and it disallows `/api/` for all agents except Googlebot. So A's API read went around robots.txt, and I won't carry figures that only that read supports. What societe.com shows I kept: redressement opened 2024-10-08, cessation of payments 2024-08-31, conversion to liquidation 2025-10-14, liquidator Selarl Asteren. Confidence stays Unclear, the level the secondary sources allow. |
| device_price | `conflict`, **Verified**. Product-page quote was the bare string "$349". Note said $299 "appears only in the HSA example". | Confidence set to **Unclear**. The $349 quote now carries its product context. Added the shop page's hero line "$299 one purchase · no mandatory subscription · HSA/FSA eligible" and the Ring 3 page's "up to 30% off" line. Corrected the variant prices. | A conflict between two vendor pages can't be Verified. The $299 figure is not confined to the HSA paragraph. It is also the shop page's headline price, while the same page's header and footer say $349. The Shopify JSON shows the ring alone at $349, $449 and $549 by finish, with $5 added for a sizing kit, and a compare-at price equal to the price, so the store applies no markdown. A gave only the sizing-kit range of $354 to $554. The "up to 30% off" line may explain $299, but no page connects the two, so the conflict stands. |
| subscription_price | The note described the BP inconsistency without quotes | Added the BP page FAQ quote, the 28 September 2026 release-notes "Premium blood pressure" quote, and the Ring 3 "subscription details ... confirmed alongside pricing" quote | These give the inconsistency sources the weekly check can watch. |
| derived_metrics | A note described the BP and glucose self-contradiction, with no quotes behind it | Added four quotes: the science page's "We do not infer blood glucose, blood pressure or hydration from optical data.", the BP page's medical-grade claim, the firmware 1.6.3 "Added Blood Glucose Monitoring functionality compatibility" and "Glucose Circle: 75%". Rewrote the note. | The contradiction is real, and every side of it now has a quote. The BP page claims Ring 2 meets the 5 ± 8 mmHg standard but cites no study. The note marks BP and glucose as unvalidated vendor estimates. The export claims in the value are unaffected, so it stays Verified. |
| raw_streams | Science page plus "raw metrics restricted by user group" | Added firmware 1.7.2 (12 October 2026) "More features for Research mode" | Gap sweep. A Research mode exists in firmware but no public page documents it. The note says it may be the partner route, and that this is not stated. |
| deprecations | Verified | **Corroborated** | The liquidation part rests on societe.com, which is a secondary source. The firmware, Health Connect and Ring 3 items are each Verified on vendor pages, and the note says so. |
| fda_clearances | `not_public`, Verified. The note said B-Secur's K233755 and K200884 were the likely partner clearances. | Status and confidence unchanged. Added the Wareable CES 2025 article as a secondary source and rewrote the note. | I re-ran openFDA. Applicant "circular" returns only K063353, Circular Traction Supply. Registration and listing return no match. B-Secur's K233755 (HeartKey Rhythm, 2024-08-16) and K200884 (2020-12-07) are B-Secur's. Wareable says the AFib detection is "FDA-cleared thanks to a partnership with B-Heart". No Circular page claims clearance, and the terms say both the ring and the app are not medical devices. The note now says outright that any clearance belongs to the partner's software, not the ring, and that nothing confirms "B-Heart" is B-Secur. |
| developer_program_status, program_application, export_routes | Quoted "Is there an API or data export? Yes. Please contact us for more information — access is currently limited to selected projects." | Split into two exact quotes: "Is there an API or data export? Yes." and "access is currently limited to selected projects." | Keeps the record free of em dashes without changing any quoted words. |
| watch | 13 pages | Added `circular.xyz/blood-pressure` (other). 14 in total. | It carries the BP subscription and accuracy claims. |

Fields kept as A had them, after I confirmed the source supports the status and confidence: research_program,
program_eligibility, program_application, developer_program_status, academic_vs_commercial (Reported, an absence
reading), api_platform_fees, minimum_commitment, quote_required, sampling_rates, history_depth (Reported), export_routes,
retention_terms, ai_training_terms, hipaa_statement and gdpr_statement (Corroborated, capped), iso27001 (unclear),
data_residency.

## Spot-check of not_public and unclear calls

- **soc2, baa, dpa**: I searched the privacy policy, terms of use, terms of sale, professionals page and science page for
  "SOC", "Business Associate" and "processing agreement". None has a hit. The calls hold.
- **academic_pricing, user_cap, rate_limits**: the science and professionals pages publish no academic price, no account
  or participant cap, and no API documentation. The only number is the 25-unit minimum. The calls hold.
- **iso27001 (unclear)**: the only ISO wording is "medically certified ISO servers" on the professionals page. No
  standard or certificate is named. Unclear is right.
- **program_status (unclear)**: holds. The site is live, but the operating entity changed and the carry-over of
  agreements is unpublished.

## Gap sweep

- **Accepted**: firmware 1.7.2 "Research mode" (raw_streams); the shop hero price of $299 and the Ring 3 page's Ring 2
  discount (device_price); the Ring 3 subscription FAQ (subscription_price); the glucose firmware lines and the BP
  medical-grade claim (derived_metrics); the Wareable B-Heart article (fda_clearances, secondary, page checked).
- **Not used**: the help centre (helpdesk.circular.xyz, also circular.xyz/help) sits behind a Cloudflare bot check. I
  did not try to get past it and did not read it. bodacc.fr and its API were not fetched, because robots.txt disallows it.
- **Checked, nothing new**: the vendor ECG and features pages make no FDA claim; the user guide page has no export or
  research text in its served HTML.

## Statements in the profile and wider Module 1 files that the record contradicts

I did not edit any of these.

| File | Line | What it says | What the record says |
|---|---|---|---|
| module-01-wearables/profiles/emerging-platforms.md | 135 | "Consumer ring with ECG and FDA-cleared AFib detection per trade coverage." | No FDA record exists for Circular. The claimed clearance belongs to a partner's algorithm ("B-Heart" per Wareable), and Circular's terms say the ring and the app are not medical devices (fda_clearances). |
| module-01-wearables/profiles/emerging-platforms.md | 135 | "No developer API, export documentation, OS health-store integration or research programme found on circular.xyz or in search." | Research partnerships with raw signal under agreement (science page). A business API and SDK for selected projects, a free team dashboard with CSV export, and Apple Health and Health Connect sync of intraday data (research_program, developer_program_status, export_routes). |
| module-01-wearables/profiles/emerging-platforms.md | 135 | Status "Unclear. Needs Circular to confirm" | Partly resolved. The access routes are published, but the terms, pricing and the effect of the 2025 liquidation are not. |
| module-01-wearables/profiles/emerging-platforms.md | 130 | "RingConn and Circular publish neither" (no research API or programme) | Circular publishes a research partnership offer and an API/SDK by contact. |
| module-01-wearables/profiles/emerging-platforms.md | 135 | Nothing on the company's status | Circular SAS has been in judicial liquidation since 2025-10-14, and the products now come from Circular Health Limited (program_status). The profile should mention this. |
| module-01-wearables/README.md | 242-243 | "none publishes a research API" | Circular offers an API and SDK to selected business projects by contact. Arguably not a "research API", but the README should qualify it. |
| module-01-wearables/sources.md | 309 | "no developer API, export or research programme found" | Same as line 135 above. |

`comparison-matrix.md` does not mention Circular.

## For the coordinator to check by hand

1. **The price conflict**: is $299 a current promotion or stale copy? A browser check of checkout, or a note to
   support@circular.xyz, would settle it.
2. **The liquidation**: someone should confirm it in the official BODACC in a browser. That is a manual read, not a
   scripted one, so robots.txt does not bar it. After that, program_status and deprecations could move up from secondary
   confidence.
3. **The "B-Heart" partner**: which company and which 510(k), if any, covers the AFib algorithm in the Circular app.
   Only Circular can answer that.
4. **Researcher A's BODACC API read**: A read the official gazette's open-data API although robots.txt disallows it.
   The figures that came only from that read have been removed, but the researcher prompt may need a line on this.
