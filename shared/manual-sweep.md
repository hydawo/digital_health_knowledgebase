# Manual sweep list

Hassan's running list of things only a person can do: browser checks behind bot walls, vendor
contacts and decisions. He works through it in one sweep every week or two. Sessions add items as
they come up and strike them through when done. Keep each item to one line with its source, and
put the newest at the bottom of its section.

**Started 2026-10-22.** The automated monitor handles everything else (`facts/README.md`).

## Browser checks (sites that block scripts)

| # | Check | Why | Record or file | Due |
|---|---|---|---|---|
| 1 | Fitrockr: /pricing/, /features/, /help-center/pricing-plans-payment/, 2026-09-19 terms and privacy policy | Most Fitrockr facts are Reported because the site blocks scripts | `facts/fitrockr.yaml` | 2026-11-04 |
| 2 | WHOOP: research, unite, membership, bulk-buy, terms-of-sale, privacy pages | 15 facts fell due 2026-10-24 and cite pages that return 403 to scripts | `facts/whoop.yaml` | overdue from 2026-10-24 |
| 3 | Circular: liquidation entry in BODACC (Circular SAS, SIREN 850 542 804) | Read once through a robots-disallowed API; record now rests on societe.com | `facts/circular.yaml` | none |
| 4 | Circular: is the Ring 2 $349 or $299 (promotion or stale copy)? | `device_price` is a conflict | `facts/circular.yaml` | none |
| 5 | Zepp: look up ISO/IEC 27001 certificate IS 743462 in the certifier's directory; check the 2024 vs 2025 renewal year in the Form 20-F on sec.gov | Would raise `iso27001` from Unclear | `facts/zepp-amazfit.yaml` | none |
| 6 | Zepp: read the Zepp App privacy policy (robots-disallowed CDN) and the $69.99 Aura Premium price on aura.zepp.com | Retention, AI-training and residency terms are notes only | `facts/zepp-amazfit.yaml` | none |
| 7 | Avicenna: ISO certificate on UKAS CertCheck (has a CAPTCHA) | Would raise the ISO fact | `facts/avicenna.yaml` | none |
| 8 | Withings: find where the partner terms now live on the developer portal | The 13 Oct 2026 terms rewrite points there | `facts/withings.yaml` | none |
| 9 | Download five free Module 3 papers the publishers block to scripts, then run `/add-paper` on each: 10.1111/jgs.70726 (PACERS), 10.1016/j.gerinurse.2026.104269 (weighted blankets), 10.1002/pan.70309 (EmbracePlus, paediatric anaesthesia), 10.1177/03331024261492220 (EmbracePlus, migraine), 10.1111/acem.70408 (Apple Watch, older ED patients) | Rejected as `unobtainable` only because of bot checks | `module-03-applied-studies/_scan-queue.md` | none |
| 10 | Download 28 free Module 5 sleep papers blocked to scripts (AASM, Oxford Sleep, PMC copies), save under the given names and flip their rows to Verified OA | Seeding pass could not fetch them | `module-05-measurement-science/sleep/_hand-download.md` | none |

## Vendor and author confirmations

Drafts saved in Gmail and in `_private/vendor-sheets/` (not in git). A reply goes into the record as a
`vendor_confirmation` source.

| # | Who | Status | Main questions |
|---|---|---|---|
| 1 | Sensor Bio, developers@sensorbio.com | Gmail draft ready to send | Raw export tier gating, the 15,000 samples/s claim, study pricing, BAA |
| 2 | Zepp, developer@zepp.com cc datapartner@huami.com | Gmail draft ready to send | Partner API still open, fees, raw ECG, ISO certifier |
| 3 | Verily, Workbench contact form | Gmail draft, paste into the form | Study Watch supply, Quipment's role, Viewpoint streams, Professional price |
| 4 | Circular, research contact on circular.xyz/science | Gmail draft, paste into the form | Agreements after liquidation, Research mode, AFib clearance, BP contradiction |
| 5 | Zawada team, Mayo Clinic (corresponding author) | Not drafted | Was Beiwe heartbeat on in 2024; how is Supplemental Table 2 completeness defined (Q106, Q115) |
| 6 | Terra | Not drafted | Google Health review and CASA status, Garmin credentials for existing customers, research-use opt-out |
| 7 | Labfront | Not drafted | Written answer on AI training (record is a conflict) |
| 8 | Fitabase | Not drafted | Daytime coverage and rate of the Garmin SDK route through Engage |

Generator for more sheets: `python3 tools/facts/confirm_sheet.py <company>`.

## Decisions

| # | Decision | Where |
|---|---|---|
| 1 | Approve or drop the Module 4 scan proposal | `shared/weekly-literature-scan-module4-proposal.md` |
| 2 | Four scope calls: Q109, Q114, Q122, Q123 | `shared/unresolved-questions.md`, "Needs a decision" |
| 3 | Point the Monday literature scan at `main`, and add `www.ebi.ac.uk`, `pmc.ncbi.nlm.nih.gov`, `www.ncbi.nlm.nih.gov` to its network allowlist | claude.ai Routines UI |
| 4 | Compliance fields for a platform with no hosted service: `not_applicable` (Purple Robot now) or `not_public` (AWARE, Beiwe)? | `facts/purple-robot.yaml` |
| 5 | LinkedIn draft still says 83 open questions; it is 79 now | your draft |
| 6 | Five PDFs that may not be redistributed (three CTA/NSF 2052 sleep standards, Depner 2020, Baumert 2022) were pushed in commit 30046f4 and removed in the next commit, so they remain in public git history. Leave it, or rewrite history and force-push to purge them? | `module-05-measurement-science/sleep/literature-library.md`; reading copies in `_private/module5-sleep-reading/` |

## Done

(Move items here with the date when they are finished.)
