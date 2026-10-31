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
| 2 | WHOOP: research, unite, membership, bulk-buy, terms-of-sale, privacy pages | 13 facts fell due 2026-10-24 (device price and FDA re-read by script 2026-10-30) and cite pages that return 403 to scripts | `facts/whoop.yaml` | overdue from 2026-10-24 |
| 3 | Circular: liquidation entry in BODACC (Circular SAS, SIREN 850 542 804) | Read once through a robots-disallowed API; record now rests on societe.com | `facts/circular.yaml` | none |
| 4 | Circular: is the Ring 2 $349 or $299 (promotion or stale copy)? | `device_price` is a conflict | `facts/circular.yaml` | none |
| 5 | Zepp: look up ISO/IEC 27001 certificate IS 743462 in the certifier's directory; check the 2024 vs 2025 renewal year in the Form 20-F on sec.gov | Would raise `iso27001` from Unclear | `facts/zepp-amazfit.yaml` | none |
| 6 | Zepp: read the Zepp App privacy policy (robots-disallowed CDN) and the $69.99 Aura Premium price on aura.zepp.com | Retention, AI-training and residency terms are notes only | `facts/zepp-amazfit.yaml` | none |
| 7 | Avicenna: ISO certificate on UKAS CertCheck (has a CAPTCHA) | Would raise the ISO fact | `facts/avicenna.yaml` | none |
| 8 | Withings: find where the partner terms now live on the developer portal | The 13 Oct 2026 terms rewrite points there | `facts/withings.yaml` | none |
| 9 | Download five free Module 3 papers the publishers block to scripts, then run `/add-paper` on each: 10.1111/jgs.70726 (PACERS), 10.1016/j.gerinurse.2026.104269 (weighted blankets), 10.1002/pan.70309 (EmbracePlus, paediatric anaesthesia), 10.1177/03331024261492220 (EmbracePlus, migraine), 10.1111/acem.70408 (Apple Watch, older ED patients) | Rejected as `unobtainable` only because of bot checks | `module-03-applied-studies/_scan-queue.md` | none |
| 10 | Download 28 free Module 5 sleep papers blocked to scripts (AASM, Oxford Sleep, PMC copies), save under the given names and flip their rows to Verified OA | Seeding pass could not fetch them | `module-05-measurement-science/sleep/_hand-download.md` | none |
| 11 | Download 17 free Module 5 cardiac papers blocked to scripts (Wiley, OUP, PMC copies), check each is CC-licensed, save under the given names and flip their rows to Verified OA | Seeding pass could not fetch them | `module-05-measurement-science/cardiac/_hand-download.md` | none |
| 12 | Download 23 free Module 5 activity papers blocked to scripts (JMIR, Springer/BMC, BMJ, Elsevier, PMC copies), check each is CC-licensed (four have only a repository listing as evidence), save under the given names and flip their rows to Verified OA | Seeding pass could not fetch them | `module-05-measurement-science/activity/_hand-download.md` | none |
| 13 | Download 21 free Module 5 mental health papers blocked to scripts (mostly JMIR, plus PeerJ, Wiley, ACM, OUP, SAGE, Springer, Elsevier, MDPI), check each is CC-licensed, save under the given names and flip their rows to Verified OA | Seeding pass could not fetch them | `module-05-measurement-science/mental-health/_hand-download.md` | none |
| 14 | Download Wyatt 2020 (Apple Watch abnormal pulse, PMC7526465, CC BY-NC) and store it under `module-01-wearables/literature/apple-watch/` | Europe PMC served a bot check | `module-01-wearables/literature-library.md`, Apple Watch Tier C | none |
| 15 | Read the conflict-of-interest statement of Qin 2026 (*Sleep Health*, 10.1016/j.sleh.2026.09.011): are the Oura Pte Ltd affiliations employment (Tier A) or the joint lab (Tier B)? | Publisher served a bot check; tier now B Corroborated | `module-01-wearables/research-library-wearables.md`, Oura Tier B | none |
| 16 | Download PROPHESY (10.1016/j.aucc.2026.101711, physical activity after open heart surgery) and re-screen it for Module 3 | Rejected `unobtainable` only because of a bot check | `module-03-applied-studies/_scan-queue.md` | none |
| 17 | **Due 9 to 10 Nov.** Re-read in a browser the facts no script may fetch: Evidation 31 and Activinsights/GENEActiv 30 (site terms forbid automated collection), LifeData developer_program_status (help centre 403), Verily Study Watch raw_streams (MassDevice 403, due 21 Nov). Update `retrieved` and `recheck_by` in each `facts/<company>.yaml`. (Empatica and Withings support pages now read through the Zendesk API; WHOOP is #2) | These sites block scripts or forbid automated collection | `facts/_reports/2026-10-31-worked-group-a.md`, `-group-b.md`, `-group-d.md`, "Needs a browser" | none |
| 18 | Download Barnard 2026 (Oura, AFLW sleep and diet, PMC13685518) and Paterson 2026 (WHOOP, pre-sleep milk protein, PMC13686207), both CC BY 4.0, into `module-01-wearables/literature/oura/` and `literature/whoop/` | Europe PMC has no rendered PDF yet and PMC served a bot check | `module-01-wearables/research-library-index.json`, 2026-10-26 scan | none |

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
| 6 | Delete the merged scan branches `claude/hopeful-fermat-crstik`, `claude/hopeful-fermat-7k2zdt` and `claude/hopeful-fermat-bt544r` on GitHub (merged into `main` on 2026-10-24 and 2026-10-30; the session's permission check blocks deleting remote branches) | GitHub branches page |

## Done

(Move items here with the date when they are finished.)

- 2026-10-22: Decision 6, licence-restricted sleep PDFs in git history. Hassan: leave them; the removal commit documents the correction.
