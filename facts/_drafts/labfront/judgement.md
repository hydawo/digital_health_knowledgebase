# Labfront: judgement (baseline fact run)

Judge run, 2026-10-11, from `A.yaml`, `B.yaml` and `gaps.md`. Output: `facts/labfront.yaml`.

Final record: 32 entries (30 fields; `raw_streams` split into Advanced and Basic scopes, `gdpr_statement` split
into a general entry and a scoped "Data Privacy Framework certification" entry). Status: 24 stated, 3 not_public,
2 conflict, 2 unclear, 1 not_applicable. Confidence: 22 Verified, 6 Corroborated, 3 Unclear, 1 none
(`rate_limits`, not_applicable). Every quote re-probed "exact" on 2026-10-11. `validate.py --file
facts/labfront.yaml`: 0 errors, 32/32 researched. `weekly.py --only labfront --no-state`: 26 pages, 0 missing,
0 reworded, 0 dead links. Both ran on the live repo; the scratch-copy fallback was not needed. Nothing was signed
into and no form was submitted. The DPF lookup used the registry's own public search request (read-only).

## Coordinator points

1. **AI training (`ai_training_terms`): conflict kept, confidence Unclear.** Scope checked on the Privacy Policy
   (effective 2022-08-05, updated 2025-12-30). Its "personal information we collect" section names Participants
   and their "Experiment Data", explicitly "including your data collected through a wearable device". Both
   machine-learning sentences ("including by using data to train our machine learning models" under To operate
   the Service; "We also use data to train and improve our machine learning models" under research and
   development) sit under "How We Use Your Personal Information", with no carve-out for Experiment Data. The
   de-identified data clause allows sharing "with third parties for our lawful business purposes". Against that,
   the FAQ says "You own your data, and we do not access it." and the trust page says "Labfront intentionally does
   not have access to your project". These cannot both hold for study data, so this is a real conflict, not a
   scope difference. No opt-out is described. Needs a written answer from Labfront.
2. **Data residency: conflict kept, confidence Corroborated.** FAQ and trust page (current): Virginia. Security
   Statement: "primarily uses an AWS data center in Ohio", last updated 2022-08-25. Both are live and the Security
   Statement is the one Labfront links for IRBs, so it stays a conflict, noted as probably stale. US-only and
   "new EU servers in the future" (undated) are not in dispute.
3. **Polar: superseded mention, not a conflict.** The only Polar mention is a Fitt Insider founder Q&A dated
   2022-11-16 ("consumer wearables like Garmin and Polar"), a general description of the engine. No current
   Labfront page, help article or pricing row mentions Polar. A's separate `raw_streams` conflict entry for Polar
   was dropped; the fact is recorded in a note on the Advanced `raw_streams` entry.
4. **Pricing tiers: confirmed on the live pricing page and pricing FAQ.** Tester free, 5 participants, 30-day
   download window; Basic $500/yr, 20 then $10 each, one integration (Garmin Connect or Dexcom), and the
   comparison table shows "Heart Rate Interval N/A Actigraphy N/A 3-Axis Accelerometer N/A" for Basic; Advanced
   $1,250/yr, 20 then $25 each. Annual billing in advance, automatic renewal. **Refunds settled from the Terms:
   both researchers were half right.** Section 5.3 says fees are non-refundable "Except as set forth in the
   Agreement"; section 9.3 gives 30 days from the Service Commencement Date or any Renewal Commencement Date to
   cancel with a refund; after that, non-refundable, with no prorated refund on cancellation. Renewal cancellation
   needs 30 days' notice.
5. **Developer Access and analytics: confirmed.** Developer Access labelled Beta, Advanced only, from $4,000, S3
   bucket refreshed every 6 hours, no external API or SDK, access granted within 5 working days. Analytics
   reports: HRV linear $4,000, HRV non-linear $6,000, sleep actigraphy $3,000, sleep regularity and timing
   $5,000, each plus $50 per participant (so $3,000 to $6,000 plus $50 per participant). Data Audit from $500.
6. **Retention: stated, not a conflict.** "3 years after study completion" (FAQ, trust page; Security Statement
   "at least 3 years") is a retention practice; the 2022 Terms say terminating all services deletes the
   account's data. They collide only when a customer closes the account within the 3 years, which no page
   reconciles. Recorded in a note with a suggestion to ask Labfront.
7. **Compliance self-claims.** HIPAA and GDPR claims are Corroborated (self-claims). `soc2` and `iso27001` are
   `unclear`: the "SOC 1/2/3" line is on one marketing page, and Labfront's July 2025 security blog says the AWS
   data centres are "certified with ISO 27001 and SOC 2 standards"; the Security Statement also attributes
   ISO 27001 to AWS. No Labfront report or certificate. GovRAMP: the spotlight (2024-12-09) says Labfront
   "joined GovRAMP", and I re-downloaded GovRAMP's product list (about 3.2 MB): no "Labfront" or "Kiipo"; recorded
   in the `soc2` note as membership only. No BAA anywhere (`baa` not_public). DPA available on request (Privacy
   Policy), DUA template on request (FAQ), HECVAT on request (FAQ).
8. **DPF: checked and Verified.** The registry's public search (the POST the list page makes) for "Kiipo" and for
   "Labfront" returns one Active record, OrganizationId 9072; no inactive record. `participants/9072` gives
   LegalName "Kiipo Co.", display name Labfront, Sharon MA, EU-U.S., Swiss-U.S. and UK Extension all Active for
   non-HR data, installed 2026-01-05, usage end 2027-01-05, no inactive periods, Self-Assessment, JAMS. Cited as
   `certificate` with `url` dataprivacyframework.gov/list and `fetch_url` the JSON, four exact quotes. Set the
   scoped entry's `recheck_by` to 2027-01-05, the certification end date. The COO's name, email and phone are in
   the JSON and were deliberately not quoted.
9. **Programs: confirmed.** Collaborator Program "offered at no cost", any academic institution, form then
   selection. 2026 calls: Labfront x Garmin Health (CIRQA Smart Band, value $5,500) deadline 2 November; Sleep
   Science 27 November; Aging Science 7 December. The pricing page still says "rolling basis" and "year-round".
10. **Garmin backfill: confirmed**, from the 2022-04-27 blog post: "up to two years old" and "All that's required
    from you is the Garmin Connect login info". Recorded in `history_depth` with an IRB caution.
11. **Movesense models: the movesense records are right.** help.labfront.com/movesense-overview says "Labfront is
    compatible with the following Movesense devices: Movesense Medical Movesense HR2 Movesense Flash". The
    compatible-devices page shows only HR2 in its recommended device cards, which is a shortlist, not a
    compatibility list. `data-intermediaries.md` line 59 (HR2 only) is the one to fix.

## Fields where A and B disagreed

| Field | A | B | Decision |
|---|---|---|---|
| `subscription_price` | stated, plan prices | not_applicable (no consumer subscription; prices under `api_platform_fees`) | Stated with A's prices; the value says there is no consumer subscription. Plan prices are the subscription. |
| `api_platform_fees` | add-ons only | plans plus add-ons | Add-ons only (A), so plan prices are not duplicated. |
| `minimum_commitment` | refundable within 30 days | non-refundable | Both partly right; Terms 5.3 and 9.3 read together (point 4). |
| `raw_streams` | split Advanced / Basic | one entry plus a Polar conflict entry | A's split kept; Polar conflict dropped as superseded (point 3); added Movesense models and the Basic-versus-Tester BBI/accelerometer detail. |
| `dpa` | not_public | stated (DPA on request) | Stated, Corroborated. The Privacy Policy's DPF statement says a DPA can be provided on request; A missed it. |
| `retention_terms` | stated with Terms deletion source | stated without it | A's sources plus a note explaining why it is not a conflict (point 6). |
| `gdpr_statement` | Corroborated, DPF unchecked | Corroborated, DPF unchecked | Split: general entry Corroborated, scoped DPF entry Verified from the registry. |
| `academic_vs_commercial` | Verified | Corroborated | Corroborated: the "no separate commercial tier" part is inference from one price list. |
| `baa` | not_public, Corroborated | not_public, Unclear | Corroborated (A). |
| `deprecations` | Verified | Unclear | Verified (A): four pages checked, nothing announced. |
| `fda_clearances` | not_public with `expect_absent` | not_public without | A's form (`expect_absent: true`), so a 404 confirms rather than reports a dead link. |
| `rate_limits` | not_applicable with source | not_applicable, note only | A's form. |
| `data_residency` | conflict | conflict | Agreed; same decision. |
| `ai_training_terms` | conflict | conflict | Agreed; scope verified (point 1). |

## Gap-hunter findings

| # | Finding | Decision |
|---|---|---|
| 1 | 3-year retention vs "Unlimited" history | Accepted, in `retention_terms` note. |
| 2 | Basic has no BBI, actigraphy or accelerometer; Tester does | Accepted; quotes in `raw_streams` (Basic) and `subscription_price`. |
| 3 | SOC 1/2/3 and ISO 27001 are AWS's | Accepted; blog quotes added to `soc2` and `iso27001`. |
| 4 | ML training and de-identified sharing in the Privacy Policy | Accepted; third-party sharing quote added. |
| 5 | Collaborator Program | Accepted (also in A and B). The gap hunter's URL `/collaborator-program` was not used; A and B's `/collaborator` probes exact. |
| 6 | Dated 2026 grant calls, Garmin CIRQA grant | Accepted for the open calls. Closed rounds (Zana, June 2026) not recorded, since `program_status` is about what is open now. |
| 7 | DPF, US-only hosting, EU servers | Accepted, and the DPF registry was then checked (point 8). The "headquartered in the United States and Taiwan" sentence was not added; no field needs it. |
| 8 | GovRAMP membership only | Accepted; re-checked the product list myself; recorded in the `soc2` note. |
| 9 | No published BAA | Accepted. |
| 10 | CIRQA Smart Band on the device page | Accepted for the profile list below; not a separate fact (no field for device models). |
| 11 | "Retroactive Garmin Data Access" row on paid plans | Accepted in `history_depth`, with a note that its link to the 2-year extraction service is not stated. |
| 12 | Dexcom per-study approval | Accepted; the Dexcom overview's "about 2 months" quote is in `raw_streams` (Advanced). |
| 13 | Holmqvist et al. 2025 deployment | Rejected for this record: a deployment finding, not a vendor fact. It belongs in Module 3 (already listed as a candidate). |
| 14 | Movesense model inconsistency | Accepted and settled (point 11). |
| "Searched, nothing found": FDA not_applicable | Rejected in favour of not_public with the openFDA queries, which is the README's rule for a negative FDA result. |

## Statements in the KB that the record contradicts or overtakes

Do not edit these here; listed for the coordinator.

- `module-01-wearables/profiles/data-intermediaries.md` line 59: "Movesense HR2" as the only Movesense device. The
  record (help centre) says Medical, HR2 and Flash. The Garmin list also lacks the CIRQA Smart Band, now on the
  compatible-devices page.
- `data-intermediaries.md` line 70: Basic "standard sampling rates". The record: Basic has no beat-to-beat interval,
  actigraphy, accelerometer or Movesense data at all, while the free Tester plan has BBI and 25 Hz accelerometry.
- `data-intermediaries.md` lines 70 to 71: "Unlimited data history" with no retention term. The record: data is
  typically kept 3 years after study completion, deletion on request, and account closure deletes data.
- `data-intermediaries.md` lines 74 to 77: grants "on a rolling basis", SRS Foundation and ACSM examples. The
  record: three dated 2026 calls (2 Nov Garmin CIRQA, 27 Nov Sleep, 7 Dec Aging) and a free Collaborator Program
  the profile does not mention.
- `data-intermediaries.md` Labfront section has no compliance, AI-training, residency or refund content. The
  record adds the ML-training conflict, US-only hosting (Virginia vs Ohio), DPF certification, no BAA, SOC and
  ISO claims that are AWS's, and the 30-day refund window.
- `module-01-wearables/comparison-matrix.md` line 379 (and line 107): "Garmin Enhanced BBI (via Labfront or
  Fitabase)" with no tier caveat. The record: Labfront BBI needs the Advanced plan (or Tester for a pilot), not
  Basic.
- `module-01-wearables/profiles/garmin.md` line 98: "Research grants are run by Garmin Health with Fitrockr." The
  record: Garmin Health also co-brands a current Labfront grant (Labfront x Garmin Health Research Grant, deadline
  2026-11-02).
- `module-01-wearables/profiles/movesense.md` lines 83, 195, 218, 277 and `comparison-matrix.md` lines 198 and
  352 (MD, HR2 and Flash) agree with the record; no change needed there.
