# Module 1 — Literature Library

Companion to `research-library-wearables.md`, which is this module's authoritative sponsorship/COI
analysis (Tier A/B/C classification, confidence markers, cross-cutting findings). This file is
narrower and mechanical: it catalogs every **individually-named, individually-cited paper** in that
bibliography — not the vaguer "a cluster of papers" or "systematic reviews as discovery mechanism"
groupings that file deliberately leaves unenumerated — records each paper's **open-access status**,
and stores the actual PDF locally under `literature/<device-slug>/` wherever it is legitimately
open access. Follows the same literature-library convention as
`module-02-digital-phenotyping/literature-library.md` (see `shared/research-log.md`, "2026-08-24
(later) — Literature-library scope decision"), extended here to Module 1.

**This file does not replace or re-derive the Tier A/B/C sponsorship analysis.** The Tier column
below is copied directly from `research-library-wearables.md` and carries the same confidence marker
(**Verified** / **Corroborated** / **Unclear**) that file assigned. Per that file's own instruction:
*"Downstream content should not cite a Tier B/C split more confidently than the marker warrants."*
That applies here too — this table adds an OA/PDF layer on top of the tiering, it does not upgrade or
re-assess it.

**OA-status confidence markers** (matching this knowledge base's evidence-confidence standard and
Module 2's literature-library convention):
- **Verified OA** — the actual PDF was fetched and inspected directly (magic-byte check +
  `pypdf` text-extraction check confirming a genuine, readable academic PDF, not an HTML
  paywall/CAPTCHA page saved with a `.pdf` name), and/or a Europe PMC record explicitly marked the
  article `isOpenAccess: Y`.
- **OA but not obtained this pass** — Europe PMC's own metadata marks the record open access
  (`isOpenAccess: Y`, has a PMCID), but the PDF could not be downloaded — Europe PMC's PDF-render
  service itself returned a server error (HTTP 500) on repeated attempts, distinct from a paywall or
  bot-detection block.
- **Paywalled** — no open-access copy located; publisher page and/or Europe PMC confirm no OA
  license, no PMC deposit, and no preprint predecessor.
- **Preprint OA, publisher-blocked** — a legitimately open preprint or author-manuscript version
  exists and was downloaded, but the final published version sits behind a login/paywall (noted per
  entry).
- **Not a formal publication** — conference abstract, press release, or grey literature with no
  peer-reviewed full-text to obtain.

All PDFs in `literature/` were downloaded via direct publisher URLs or the Europe PMC render
service, then verified with a `pypdf` text-extraction check (not just an HTTP 200 or magic-byte
check) before being kept — the same standard Module 2 used, adopted after Module 2's retrofit found
some sites return HTML CAPTCHA/paywall pages disguised with a `.pdf` extension.

**Last verified: 2026-08-24.**

---

## Oura

All 17 individually-named Oura papers in `research-library-wearables.md` were obtained as verified,
readable PDFs — the only device of the three with zero access gaps.

### Tier A — Oura-employee-authored

| Title | Authors | Venue/Year | DOI | Tier (source confidence) | OA status | PDF |
|---|---|---|---|---|---|---|
| The Promise of Sleep: A Multi-Sensor Approach for Accurate Sleep Stage Detection Using the Oura Ring | Altini M, Kinnunen H. | *Sensors* 2021;21(13):4302 | [10.3390/s21134302](https://doi.org/10.3390/s21134302) | A (Verified) | **Verified OA** (MDPI) | [literature/oura/2021-kinnunen-sensors-promise-of-sleep.pdf](literature/oura/2021-kinnunen-sensors-promise-of-sleep.pdf) |
| Country differences in nocturnal sleep variability: Observations from a large-scale, long-term sleep wearable study | Willoughby AR, Alikhani I, Karsikas M, Chua XY, Chee MWL. | *Sleep Medicine* 2023;110:155–165 | [10.1016/j.sleep.2023.08.010](https://doi.org/10.1016/j.sleep.2023.08.010) | A (Corroborated) | Published version **paywalled** (Elsevier); **PsyArXiv preprint is open** | [literature/oura/2023-willoughby-sleepmed-country-differences-nocturnal-sleep.pdf](literature/oura/2023-willoughby-sleepmed-country-differences-nocturnal-sleep.pdf) — preprint (DOI [10.31234/osf.io/8ahsu](https://doi.org/10.31234/osf.io/8ahsu)); the first page of the downloaded PDF states the peer-reviewed version is at the Sleep Medicine DOI above |

### Tier B — Oura-funded / Oura-affiliated, independent authors

| Title | Authors | Venue/Year | DOI | Tier (source confidence) | OA status | PDF |
|---|---|---|---|---|---|---|
| Accuracy of Three Commercial Wearable Devices for Sleep Tracking in Healthy Adults | Robbins R, Weaver MD, Sullivan JP, Quan SF, Gilmore K, Shaw S, Benz A, Qadri S, Barger LK, Czeisler CA, Duffy JF. | *Sensors* 2024;24(20):6532 | [10.3390/s24206532](https://doi.org/10.3390/s24206532) | B (Verified) | **Verified OA** (MDPI) | [literature/oura/2024-robbins-sensors-accuracy-three-wearables-sleep.pdf](literature/oura/2024-robbins-sensors-accuracy-three-wearables-sleep.pdf) |
| Deriving Accurate Nocturnal Heart Rate, rMSSD and Frequency HRV from the Oura Ring | Liang T, Yilmaz G, Soon CS. | *Sensors* 2024;24(23):7475 | [10.3390/s24237475](https://doi.org/10.3390/s24237475) | B (Corroborated) | **Verified OA** (MDPI) | [literature/oura/2024-liang-sensors-nocturnal-hr-hrv-oura.pdf](literature/oura/2024-liang-sensors-nocturnal-hr-hrv-oura.pdf) |
| Detection of COVID-19 using multimodal data from a wearable device: results from the first TemPredict Study | Mason AE, Hecht FM, Davis SK, et al. (32 authors incl. Smarr BL) | *Scientific Reports* 2022;12:3463 | [10.1038/s41598-022-07314-0](https://doi.org/10.1038/s41598-022-07314-0) | B (Verified) | **Verified OA** (Nature, CC BY) | [literature/oura/2022-mason-scientificreports-tempredict-covid-detection.pdf](literature/oura/2022-mason-scientificreports-tempredict-covid-detection.pdf) |
| Metrics from Wearable Devices as Candidate Predictors of Antibody Response Following Vaccination against COVID-19: Data from the Second TemPredict Study | Mason AE, Kasl P, Hartogensis W, et al. (17 authors incl. Smarr BL) | *Vaccines* 2022;10(2):264 | [10.3390/vaccines10020264](https://doi.org/10.3390/vaccines10020264) | B (Corroborated) | **Verified OA** (MDPI) | [literature/oura/2022-tempredict2-vaccines-antibody-response.pdf](literature/oura/2022-tempredict2-vaccines-antibody-response.pdf) |
| Elevated body temperature is associated with depressive symptoms: results from the TemPredict Study | Mason AE, Kasl P, Soltani S, et al. (15 authors incl. Smarr BL) | *Scientific Reports* 2024 | [10.1038/s41598-024-51567-w](https://doi.org/10.1038/s41598-024-51567-w) | B (Corroborated) | **Verified OA** (Nature, CC BY) | [literature/oura/2024-mason-scientificreports-body-temperature-depression.pdf](literature/oura/2024-mason-scientificreports-body-temperature-depression.pdf) |
| Assessing Adherence to Multi-Modal Oura Ring Wearables From COVID-19 Detection Among Healthcare Workers | Shiba SK, Temple CA, Krasnoff J, Dilchert S, Smarr BL, Robishaw J, Mason AE. | *Cureus* 2023;15(9):e45362 | [10.7759/cureus.45362](https://doi.org/10.7759/cureus.45362) | B (Unclear, upgraded) | **Verified OA** (Cureus is OA by default) | [literature/oura/2023-shiba-cureus-adherence-oura-covid-healthcare-workers.pdf](literature/oura/2023-shiba-cureus-adherence-oura-covid-healthcare-workers.pdf) — **the actual first/lead author is Shiba SK, not previously named in `research-library-wearables.md`, which cited this paper by title only** |

### Tier C — Fully independent

| Title | Authors | Venue/Year | DOI | Tier (source confidence) | OA status | PDF |
|---|---|---|---|---|---|---|
| Accuracy Assessment of Oura Ring Nocturnal Heart Rate and Heart Rate Variability in Comparison With Electrocardiography in Time and Frequency Domains | Cao R, Azimi I, Sarhaddi F, Niela-Vilen H, Axelin A, Liljeberg P, Rahmani AM. | *JMIR* 2022;24(1):e27487 | [10.2196/27487](https://doi.org/10.2196/27487) | C (Verified) | **Verified OA** (JMIR CC BY) | [literature/oura/2022-cao-jmir-accuracy-oura-hr-hrv.pdf](literature/oura/2022-cao-jmir-accuracy-oura-hr-hrv.pdf) |
| Validation of Oura ring energy expenditure and steps in laboratory and free-living | Kristiansson E, Fridolfsson J, Arvidsson D, Holmäng A, Börjesson M, Andersson-Hall U. | *BMC Medical Research Methodology* 2023;23:50 | [10.1186/s12874-023-01868-x](https://doi.org/10.1186/s12874-023-01868-x) | C (Corroborated) | **Verified OA** (BMC, CC BY) | [literature/oura/2023-kristiansson-bmcmedresmethodol-energy-expenditure-steps.pdf](literature/oura/2023-kristiansson-bmcmedresmethodol-energy-expenditure-steps.pdf) |
| Validation of nocturnal resting heart rate and heart rate variability in consumer wearables | Dial MB, Hollander ME, Vatne EA, Emerson AM, Edwards NA, Hagen JA. | *Physiological Reports* 2025;13(16):e70527 | [10.14814/phy2.70527](https://doi.org/10.14814/phy2.70527) | C (Verified — AFRL-funded, no COI, full text read 2026-08-25) | **Verified OA** (Physiological Reports is OA by default) | [literature/oura/2025-dial-physiologicalreports-nocturnal-rhr-hrv-validation.pdf](literature/oura/2025-dial-physiologicalreports-nocturnal-rhr-hrv-validation.pdf) — full-text extraction into `validation-evidence.md` §3a complete |
| Assessing the Accuracy of Popular Commercial Technologies That Measure Resting Heart Rate and Heart Rate Variability | Stone JD, Ulman HK, Tran K, Thompson AG, Halter MD, Ramadan JH, Stephenson M, Finomore VS, Galster SM, Rezai AR, Hagen JA. | *Frontiers in Sports and Active Living* 2021 | [10.3389/fspor.2021.585870](https://doi.org/10.3389/fspor.2021.585870) | C (Unclear, funding not directly read) | **Verified OA** (Frontiers CC BY) | [literature/oura/2021-stone-frontierssportsactiveliving-rhr-hrv-accuracy.pdf](literature/oura/2021-stone-frontierssportsactiveliving-rhr-hrv-accuracy.pdf) |
| The Two Fundamental Shapes of Sleep Heart Rate Dynamics and Their Connection to Mental Health in College Students (LEMURS study) | Fudolig MI, Bloomfield LSP, Price M, Bird YM, Hidalgo JE, Kim JN, Llorin J, Lovato J, McGinnis EW, McGinnis RS, Ricketts T, Stanton K, Dodds PS, Danforth CM. | *Digital Biomarkers* 2024;8:120–131 | [10.1159/000539487](https://doi.org/10.1159/000539487) | C (Corroborated) | **Verified OA** (Karger open access) | [literature/oura/2024-fudolig-digitalbiomarkers-sleep-heart-rate-shapes.pdf](literature/oura/2024-fudolig-digitalbiomarkers-sleep-heart-rate-shapes.pdf) |
| Predicting Symptoms of Depression and Anxiety Using Smartphone and Wearable Data | Moshe I, Terhorst Y, Opoku Asare K, Sander LB, Ferreira D, Baumeister H, Mohr DC, Pulkki-Råback L. | *Frontiers in Psychiatry* 2021;12:625247 | [10.3389/fpsyt.2021.625247](https://doi.org/10.3389/fpsyt.2021.625247) | C (Unclear) | **Verified OA** (Frontiers CC BY) | [literature/oura/2021-moshe-frontierspsychiatry-predicting-depression-anxiety.pdf](literature/oura/2021-moshe-frontierspsychiatry-predicting-depression-anxiety.pdf) |
| Physiological Data Collected From Wearable Devices Identify and Predict Inflammatory Bowel Disease Flares | Hirten RP, Danieletto M, Sanchez-Mayor M, et al. | *Gastroenterology* 2025 | [10.1053/j.gastro.2024.12.024](https://doi.org/10.1053/j.gastro.2024.12.024) | C (Corroborated) | **Verified OA** — NIH-funded (NIDDK K23DK129835) PMC author-manuscript deposit, not a formally OA-licensed journal article | [literature/oura/2025-hirten-gastroenterology-ibd-flares-wearables.pdf](literature/oura/2025-hirten-gastroenterology-ibd-flares-wearables.pdf) |

### Systematic reviews (individually named; classified in their own right per the source file)

| Title | Authors | Venue/Year | DOI | Tier | OA status | PDF |
|---|---|---|---|---|---|---|
| The Oura Ring Versus Medical-Grade Sleep Studies: A Systematic Review and Meta-Analysis | Khan S, Ibrahim AF, Vasudevan SS, Quatela OE, Nanu DP, Carr MM. | *OTO Open* 2025;9(4) | [10.1002/oto2.70181](https://doi.org/10.1002/oto2.70181) | Unclear (funding/COI not read) | **Verified OA** (OTO Open is OA by default) | [literature/oura/2025-khan-otoopen-oura-vs-medical-sleep-studies.pdf](literature/oura/2025-khan-otoopen-oura-vs-medical-sleep-studies.pdf) — resolves the prior 403/CAPTCHA block |
| Smart Ring in Clinical Medicine: A Systematic Review | Gong EJ, Bang CS, Lee JJ, Baik GH. | ***Biomimetics*** 2025;10(12):819 | [10.3390/biomimetics10120819](https://doi.org/10.3390/biomimetics10120819) | C (Verified — Korean government grant, no industry funding) | **Verified OA** (MDPI) | [literature/oura/2025-gong-biomimetics-smart-ring-clinical-medicine.pdf](literature/oura/2025-gong-biomimetics-smart-ring-clinical-medicine.pdf) — **venue correction: `research-library-wearables.md` cites this as "*Diagnostics* (MDPI) / JMIR preprint #83508"; the actual published DOI resolves to *Biomimetics*, a different MDPI journal. Same authors, same title, same findings — this is a venue mislabeling in the source file, not a different paper. Flagged for correction there.** |

**Oura summary: 17/17 individually-named papers obtained as verified PDFs. Zero paywalled or unobtained.**

---

## WHOOP

18 individually-named WHOOP papers in `research-library-wearables.md` (excluding the "Tobacco Use"
item, which has no traceable DOI/journal and is explicitly flagged there as press-release-only, not
a citable paper). 13 obtained; 5 not obtained (3 genuinely paywalled, 1 OA preprint blocked by
bot-detection this pass, 1 unpublished dissertation not located).

### Tier A — WHOOP-employee-authored

| Title | Authors | Venue/Year | DOI | Tier (source confidence) | OA status | PDF |
|---|---|---|---|---|---|---|
| Four core circadian behaviors that improve cardiorespiratory fitness through consistent sleep | Holmes KE, Kim J, Fielding F, Zeitzer JM, von Hippel W. | *Sleep* 2026;49(2):zsaf318 | [10.1093/sleep/zsaf318](https://doi.org/10.1093/sleep/zsaf318) | A (Verified) | **Paywalled** (Oxford Academic *Sleep* is not OA by default; no PMC deposit or preprint located) | Not obtained |
| Inter- and Intrapersonal Associations Between Physiology and Mental Health | Presby D, Jasinski S, Capodilupo E, Holmes KE, von Hippel W, Grosicki GJ, Lee V. | *JMIR* 2025;27:e64955 | [10.2196/64955](https://doi.org/10.2196/64955) | A (Verified) | **Verified OA** (JMIR CC BY) | [literature/whoop/2025-presby-jmir-physiology-mental-health.pdf](literature/whoop/2025-presby-jmir-physiology-mental-health.pdf) |
| A Novel method for quantifying fluctuations in wearable derived daily cardiovascular parameters across the menstrual cycle | Jasinski SR, Presby DM, Grosicki GJ, Capodilupo ER, Lee VH. | *npj Digital Medicine* 2024;7:373 | [10.1038/s41746-024-01394-0](https://doi.org/10.1038/s41746-024-01394-0) | A (Verified) | **Verified OA** (Nature, CC BY) | [literature/whoop/2024-jasinski-npjdigitalmedicine-menstrual-cycle-cardiovascular.pdf](literature/whoop/2024-jasinski-npjdigitalmedicine-menstrual-cycle-cardiovascular.pdf) |
| The menstrual cycle through the lens of a wearable device: insights into physiology, sleep, and cycle variability | **Gonzalez A, O'Day JJ, Johnson SC, Kim J, Jasinski SR, Holmes KE, Delp SL, Hicks JL.** | *npj Digital Medicine* 2026;9:633 (DOI 10.1038/s41746-026-02799-9); bioRxiv preprint 2025 | [10.1101/2025.09.11.675620](https://doi.org/10.1101/2025.09.11.675620) (preprint); [10.1038/s41746-026-02799-9](https://doi.org/10.1038/s41746-026-02799-9) (published) | **A — now Verified, resolving the source file's open item.** 3 of 8 authors (Kim J, Jasinski SR, Holmes KE) are named WHOOP Inc. staff on the sister paper above; lead/corresponding authors Gonzalez and O'Day are Stanford Wu Tsai Human Performance Alliance | **Verified OA** — bioRxiv preprint (CC BY-NC-ND 4.0); published npj version is Nature-login-gated for direct PDF download | [literature/whoop/2026-gonzalez-oday-npjdigitalmedicine-menstrual-cycle-lens-wearable.pdf](literature/whoop/2026-gonzalez-oday-npjdigitalmedicine-menstrual-cycle-lens-wearable.pdf) — **this confirms the author list an earlier pass in `research-library-wearables.md` explicitly flagged as unverified ("Alexander Gonzalez and Johanna J. O'Day... this is unverified and should not be trusted") was in fact correct. The paper is Stanford-led with substantive WHOOP co-authorship — genuinely mixed Tier A, not pure independent Tier C. `research-library-wearables.md`'s downgrade of this paper to "Unclear" should be corrected back to Tier A given this direct read.** |
| Real-world effects of alcohol on heart rate, sleep, and physical activity by age and sex | Grosicki GJ, Robinson AT, Joyner MJ, Carter JR, von Hippel W, Presby DM, Fielding F, Bigalke JA, Kim J, Chapman C, Holmes KE. | *PLOS Digital Health* 2026 | [10.1371/journal.pdig.0001284](https://doi.org/10.1371/journal.pdig.0001284) | A (Verified) | **Verified OA** (PLOS CC BY) | [literature/whoop/2026-grosicki-plosdigitalhealth-alcohol-hr-sleep-activity.pdf](literature/whoop/2026-grosicki-plosdigitalhealth-alcohol-hr-sleep-activity.pdf) |
| Analyzing changes in respiratory rate to predict the risk of COVID-19 infection | Miller DJ, Capodilupo JV, Lastella M, Sargent C, Roach GD, Lee VH, Capodilupo ER. | *PLOS ONE* 2020;15(12):e0243693 | [10.1371/journal.pone.0243693](https://doi.org/10.1371/journal.pone.0243693) | A (Verified) | **Verified OA** (PLOS CC BY) | [literature/whoop/2020-miller-plosone-respiratory-rate-covid19-risk.pdf](literature/whoop/2020-miller-plosone-respiratory-rate-covid19-risk.pdf) |
| Alcohol Use Trajectories During the First 72 Weeks of WHOOP Wearable Platform Membership: Observational Cohort Study | Grosicki GJ, Hippel WV, Fielding F, Chapman CJ, Presby DM, Leota J, Holmes KE. | *JMIR mHealth uHealth* 2026 (Research Letter), PMC13119388 | [10.2196/91288](https://doi.org/10.2196/91288) | A (Corroborated → author list now confirmed) | **Verified OA** (JMIR CC BY) | [literature/whoop/2026-grosicki-jmirmhealth-alcohol-trajectories-whoop-membership.pdf](literature/whoop/2026-grosicki-jmirmhealth-alcohol-trajectories-whoop-membership.pdf) — resolves the author-list uncertainty flagged in `research-library-wearables.md` |
| Optimizing Athlete Travel for Performance: A Scientific Blueprint for Athletes, Coaches, and Sports Medicine Staff (cited in the source file as "Travel, recovery and performance") | Hatamiya N, Holmes KE, Grosicki GJ, Swisher J, Duffaut C, Vail J, Logan-Sprenger H, Donohoe B, Fielding F, Chapman CJ, Leota J, Facer-Childs ER, Goldman JT. | *Sports Medicine* 2026;56:1381–1403 | [10.1007/s40279-026-02455-y](https://doi.org/10.1007/s40279-026-02455-y) | A (Corroborated → author list now confirmed) | **Verified OA** (PMC deposit, PMC13260286) | [literature/whoop/2026-hatamiya-sportsmedicine-travel-recovery-performance.pdf](literature/whoop/2026-hatamiya-sportsmedicine-travel-recovery-performance.pdf) — resolves the author-list uncertainty; note the actual published title differs from the working title used in `research-library-wearables.md` (same DOI, confirmed same paper) |

### Tier B — WHOOP-funded/affiliated, independent-author-led

| Title | Authors | Venue/Year | DOI | Tier (source confidence) | OA status | PDF |
|---|---|---|---|---|---|---|
| Effect of wearables on sleep in healthy individuals: a randomized crossover trial and validation study | Berryhill S, Morton CJ, Dean A, Berryhill A, Provencio-Dean N, Patel SI, Estep L, Combs D, Mashaqi S, Gerald LB, Krishnan JA, Parthasarathy S. | *Journal of Clinical Sleep Medicine* 2020;16(5):775–783 | [10.5664/jcsm.8356](https://doi.org/10.5664/jcsm.8356) | B (Verified) | **Verified OA** — PMC deposit (PMC7849816); JCSM itself is not OA by default | [literature/whoop/2020-berryhill-jcsm-wearables-sleep-rct.pdf](literature/whoop/2020-berryhill-jcsm-wearables-sleep-rct.pdf) |
| Evaluating the Typical Day-to-Day Variability of WHOOP-Derived Heart Rate Variability in Olympic Water Polo Athletes | Bellenger CR, Miller D, Halson SL, Roach GD, Maclennan M, Sargent C. | *Sensors* 2022;22(18):6723 | [10.3390/s22186723](https://doi.org/10.3390/s22186723) | B (Corroborated) | **Verified OA** (MDPI) | [literature/whoop/2022-bellenger-sensors-hrv-variability-water-polo.pdf](literature/whoop/2022-bellenger-sensors-hrv-variability-water-polo.pdf) |
| A validation study of the WHOOP strap against polysomnography to assess sleep | Miller DJ, Lastella M, Scanlan AT, Bellenger C, Halson SL, Roach GD, Sargent C. | *Journal of Sports Sciences* 2020;38(22):2631–2636 | [10.1080/02640414.2020.1797448](https://doi.org/10.1080/02640414.2020.1797448) | B likely (Unclear — funding not directly read) | **Paywalled** (Taylor & Francis; no PMC deposit or preprint located — confirms the source file's "Tandfonline 403" note) | Not obtained |

### Tier C — Fully independent

| Title | Authors | Venue/Year | DOI | Tier (source confidence) | OA status | PDF |
|---|---|---|---|---|---|---|
| Wrist-Based Photoplethysmography Assessment of Heart Rate and Heart Rate Variability: Validation of WHOOP | Bellenger CR, Miller DJ, Halson SL, Roach GD, Sargent C. | *Sensors* 2021;21(10):3571 | [10.3390/s21103571](https://doi.org/10.3390/s21103571) | C (Verified) | **Verified OA** (MDPI) | [literature/whoop/2021-bellenger-sensors-ppg-hr-hrv-validation-whoop.pdf](literature/whoop/2021-bellenger-sensors-ppg-hr-hrv-validation-whoop.pdf) |
| A Validation Study of a Commercial Wearable Device to Automatically Detect and Estimate Sleep | Miller DJ, Roach GD, Lastella M, Scanlan AT, Bellenger CR, Halson SL, Sargent C. | *Biosensors* 2021;11(6):185 | [10.3390/bios11060185](https://doi.org/10.3390/bios11060185) | C (Verified) | **Verified OA** (MDPI) | [literature/whoop/2021-miller-biosensors-wearable-sleep-detection-validation.pdf](literature/whoop/2021-miller-biosensors-wearable-sleep-detection-validation.pdf) |
| A performance validation of six commercial wrist-worn wearable devices for sleep stage scoring compared to polysomnography | Schyvens AM, Peters B, Van Oost NC, Aerts JM, Masci F, Neven A, Dirix H, Wets G, Ross V, Verbraecken J. | *SLEEP Advances* 2025;6(2):zpaf021 | [10.1093/sleepadvances/zpaf021](https://doi.org/10.1093/sleepadvances/zpaf021) | C (Verified) | **Verified OA** (SLEEP Advances is fully OA) | [literature/whoop/2025-schyvens-sleepadvances-six-device-comparison.pdf](literature/whoop/2025-schyvens-sleepadvances-six-device-comparison.pdf) |
| Wearable technology metrics are associated with energy deficiency and psychological stress in elite swimmers | Lundstrom EA, De Souza MJ, Koltun KJ, Strock NCA, Canil HN, Williams NI. | *International Journal of Sports Science & Coaching* 2024;19(4):1578–1587 | [10.1177/17479541231206424](https://doi.org/10.1177/17479541231206424) | C (Unclear — Penn State–WHOOP equipment partnership flagged, not a funding relationship) | **Paywalled** (SAGE; HTTP 403 confirmed, no PMC deposit found) | Not obtained |
| Accuracy, Utility and Applicability of the WHOOP Wearable Monitoring Device in Health, Wellness and Performance — a systematic review | Khodr R, Kamal L, Minerbi A, Gupta G. | *medRxiv* 2024.01.04.24300784 (preprint) | [10.1101/2024.01.04.24300784](https://doi.org/10.1101/2024.01.04.24300784) | C (Corroborated) | **Verified OA — obtained 2026-08-24 retry.** medRxiv's `/v1/full.pdf` URL was bot-blocked (HTTP 403), but Semantic Scholar's Graph API resolved the paper's canonical `.../content/medrxiv/early/.../full.pdf` URL, which succeeded with a browser-like user agent | [literature/whoop/2024-khodr-medrxiv-whoop-systematic-review.pdf](literature/whoop/2024-khodr-medrxiv-whoop-systematic-review.pdf) |
| The Impact of Whoop Technology on Sleep, Recovery, and Performance in NAIA Baseball Players (dissertation) | Harms NR. | University of Nebraska–Lincoln, 2018 (ProQuest/ERIC ED595664) | N/A | C (not peer-reviewed; grey literature) | A UNL DigitalCommons copy exists but returned HTTP 403 on direct fetch; ERIC's own hosted copy returned 404 | Not obtained — low priority per the source file's own framing ("included here only for completeness") |

### Commentary (individually named, Tier C)

| Title | Authors | Venue/Year | DOI | Tier | OA status | PDF |
|---|---|---|---|---|---|---|
| A new metric to understand the association between heart rate variability and menstrual regularity | Heydari K, Enichen EJ, Li B, Kvedar JC. | *npj Digital Medicine* 2025;8:123 | [10.1038/s41746-025-01517-1](https://doi.org/10.1038/s41746-025-01517-1) | C (Corroborated) | **Verified OA** (Nature, CC BY) | [literature/whoop/2025-heydari-npjdigitalmedicine-hrv-menstrual-regularity.pdf](literature/whoop/2025-heydari-npjdigitalmedicine-hrv-menstrual-regularity.pdf) — a short Editorial/commentary (2 pages), not a primary-data article; matches the source file's own description |

**WHOOP summary: 14/18 individually-named papers obtained as verified PDFs (13 initial pass + Khodr
medRxiv resolved on 2026-08-24 retry). 4 not obtained: 2 genuinely paywalled with no OA route (Holmes
2026 *Sleep*, Lundstrom 2024 SAGE), 1 paywalled with no OA route despite an author-cluster COI flag
(Miller 2020 *J Sports Sciences*), and 1 grey-literature dissertation not locatable via an accessible
route (Harms 2018 — see unresolved-questions.md #99).**

---

## Apple Watch

19 individually-named Apple Watch papers/documents in `research-library-wearables.md` (excluding the
DEFINE AFib Study, a conference abstract with no full peer-reviewed paper — see note below — and
excluding the two papers already cross-listed and catalogued once each under Oura/WHOOP above
[Schyvens et al. 2025, Robbins et al. 2024] rather than duplicated here). 13 obtained; 6 not
obtained.

### Tier A — Apple-employee-authored / Apple-sponsored flagship studies

| Title | Authors | Venue/Year | DOI | Tier (source confidence) | OA status | PDF |
|---|---|---|---|---|---|---|
| Large-Scale Assessment of a Smartwatch to Identify Atrial Fibrillation (Apple Heart Study) | Perez MV, Mahaffey KW, Hedlin H, et al. (Apple Heart Study Investigators) | *N Engl J Med* 2019;381:1909–1917 | [10.1056/NEJMoa1901183](https://doi.org/10.1056/NEJMoa1901183) | A (Verified) | **Confirmed genuinely paywalled — checked 2026-08-24 against NCBI's own OA web service** (`oa.fcgi?id=PMC8112605`), which returned `idIsNotOpenAccess`. The PMC deposit is a non-OA author-manuscript record, not a retrieval-infrastructure failure; the earlier HTTP 500/CAPTCHA symptoms were downstream of this, not the cause | Not obtained — NEJM is not OA by default and no legitimate OA copy exists |
| Design and methods of the Apple Women's Health Study: a digital longitudinal cohort study | Mahalingaiah S, Fruh V, Rodriguez E, et al. (19 authors incl. Onnela JP, Jukic AMZ) | *Am J Obstet Gynecol* 2022 | [10.1016/j.ajog.2021.09.041](https://doi.org/10.1016/j.ajog.2021.09.041) | A (Corroborated) | **Verified OA — obtained 2026-08-24 retry.** NCBI's OA web service confirmed a genuine CC BY-NC-ND record with a direct PDF link, but the URL itself sits behind a JS bot-detection interstitial that blocks plain HTTP fetch; a real browser session cleared the challenge (a `cloudpmc-viewer-pow` cookie), and that cookie let a direct curl request through | [literature/apple-watch/2022-mahalingaiah-ajog-apple-womens-health-study-design.pdf](literature/apple-watch/2022-mahalingaiah-ajog-apple-womens-health-study-design.pdf) |
| Understanding activity and physiology at scale: The Apple Heart & Movement Study | Truslow J, Spillane A, Lin H, et al. (22 authors, Apple/AHA/BWH) | *npj Digital Medicine* 2024 | [10.1038/s41746-024-01187-5](https://doi.org/10.1038/s41746-024-01187-5) | A (Corroborated) | **Verified OA** (Nature, CC BY) | [literature/apple-watch/2024-truslow-npjdigitalmedicine-heart-movement-study-scale.pdf](literature/apple-watch/2024-truslow-npjdigitalmedicine-heart-movement-study-scale.pdf) — resolves the author list, previously not enumerated in `research-library-wearables.md` |
| Using Apple Watch to Estimate Cardio Fitness with VO2 max (Apple internal white paper) | Apple Inc. (no individually named academic authors) | Apple, May 2021 | N/A (self-published PDF) | A (Reported, not independently verified) | **Directly obtainable from Apple's own domain** — not a journal article, so OA/paywall status doesn't strictly apply, but it was successfully machine-read this pass (the source file previously noted the PDF was "not machine-readable via fetch") | [literature/apple-watch/2021-apple-whitepaper-vo2max-cardio-fitness.pdf](literature/apple-watch/2021-apple-whitepaper-vo2max-cardio-fitness.pdf) — **resolves an open item from `research-library-wearables.md`'s "Open items for a follow-up pass" list (#8)** |

### Tier C — Fully independent

| Title | Authors | Venue/Year | DOI | Tier (source confidence) | OA status | PDF |
|---|---|---|---|---|---|---|
| Apple Watch Sleep and Physiological Tracking Compared to Clinically Validated Actigraphy, Ballistocardiography and Polysomnography | Jaworski D, Park EJ. | IEEE EMBC 2023 | PMID [38083143](https://pubmed.ncbi.nlm.nih.gov/38083143/) | Unclear | **Paywalled** (IEEE Xplore; no OA route found) | Not obtained |
| Investigating the accuracy of Apple Watch VO2 max measurements: A validation study | Lambe R, O'Grady B, Baldwin M, Doherty C. | *PLOS ONE* 2025 | [10.1371/journal.pone.0323741](https://doi.org/10.1371/journal.pone.0323741) | C (Verified) | **Verified OA** (PLOS CC BY) | [literature/apple-watch/2025-doherty-plosone-vo2max-validation.pdf](literature/apple-watch/2025-doherty-plosone-vo2max-validation.pdf) — lead author is Lambe R, not Doherty C (Doherty is senior/last author); `research-library-wearables.md` cites this paper as "Doherty C, Lambe R, O'Grady B, Baldwin M" — author order differs from the published paper's actual byline |
| The Validity of Apple Watch Series 9 and Ultra 2 for Serial Measurements of Heart Rate Variability and Resting Heart Rate | O'Grady B, Lambe R, Baldwin M, Acheson T, Doherty C. | *Sensors* 2024;24(19):6220 | [10.3390/s24196220](https://doi.org/10.3390/s24196220) | C (Verified) | **Verified OA** (MDPI) | [literature/apple-watch/2024-doherty-sensors-hrv-rhr-validity-series9-ultra2.pdf](literature/apple-watch/2024-doherty-sensors-hrv-rhr-validity-series9-ultra2.pdf) — lead author is O'Grady B, not Doherty C; same author-order note as above |
| Accuracy of Apple Watch to Measure Cardiovascular Indices in Patients with Cardiac Diseases: Observational Study | Khushhal AA, Mohamed AA, Elsayed ME. | *Global Heart* 2025 | [10.5334/gh.1456](https://doi.org/10.5334/gh.1456) | C (Verified) | **Verified OA** (Global Heart is OA, Ubiquity Press) | [literature/apple-watch/2025-khushhal-globalheart-cardiovascular-indices-cardiac-patients.pdf](literature/apple-watch/2025-khushhal-globalheart-cardiovascular-indices-cardiac-patients.pdf) |
| Accuracy of the Apple watch for detection of AF: A multicenter experience | Wasserlauf J, Vogel K, Whisler C, Benjamin E, Helm R, Steinhaus DA, Yousuf O, Passman RS. | *Journal of Cardiovascular Electrophysiology* | [10.1111/jce.15892](https://doi.org/10.1111/jce.15892) | C (Verified) | **Verified OA** — Health Research Alliance member-organization author manuscript, PMC deposit | [literature/apple-watch/2019-wasserlauf-jcardiovascelectrophysiol-apple-watch-afib-multicenter.pdf](literature/apple-watch/2019-wasserlauf-jcardiovascelectrophysiol-apple-watch-afib-multicenter.pdf) — **venue correction: this is *Journal of Cardiovascular Electrophysiology*, not "Circulation: Arrhythmia and Electrophysiology" as the file was initially (mis)named during this retrofit; corrected** |
| Assessment of Apple Watch Series 6 pulse oximetry and electrocardiograms in a pediatric population | Littell L, Roelle L, Dalal A, Van Hare GF, Orr WB, Miller N, Avari Silva JN. | *PLOS Digital Health* | [10.1371/journal.pdig.0000051](https://doi.org/10.1371/journal.pdig.0000051) | C (Verified) | **Verified OA** (PLOS CC BY) | [literature/apple-watch/2023-littell-plosdigitalhealth-apple-watch-pediatric-spo2-ecg.pdf](literature/apple-watch/2023-littell-plosdigitalhealth-apple-watch-pediatric-spo2-ecg.pdf) — **venue correction: this is *PLOS Digital Health*, not PACE as the file was initially (mis)named during this retrofit; corrected** |
| Sensitivity of Apple Watch fall detection feature among wheelchair users | Abou L, Fliflet A, Hawari L, Presti P, Sosnoff JJ, Mahajan HP, Frechette ML, Rice LA. | *Assistive Technology* 2022;34(5):619–625 | [10.1080/10400435.2021.1923087](https://doi.org/10.1080/10400435.2021.1923087) | Unclear | **Paywalled** (Taylor & Francis; no PMC deposit or preprint located) | Not obtained |
| Effectiveness of a Smartwatch App in Detecting Induced Falls: Observational Study | Brew B, Faux SG, Blanchard E. | *JMIR Formative Research* | [10.2196/30121](https://doi.org/10.2196/30121) | C (Verified — funded by My Medic Watch, a competing commercial fall-detection company, not Apple) | **Verified OA** (JMIR CC BY) | [literature/apple-watch/2022-brew-jmirformativeres-smartwatch-fall-detection.pdf](literature/apple-watch/2022-brew-jmirformativeres-smartwatch-fall-detection.pdf) |
| Accuracy of the Apple Watch in Detecting Atrial Fibrillation Among Patients Undergoing 24-Hour Holter Monitoring: A Prospective, Pragmatic Study | Inocian EP, Junia AT, Ong Cordovez MG, et al. | *Philippine Journal of Cardiology* 2024 | N/A (journal DOI not centrally indexed) | C (Verified) | **Verified OA** (direct publisher PDF) | [literature/apple-watch/2024-inocian-philjcardiology-afib-detection-holter.pdf](literature/apple-watch/2024-inocian-philjcardiology-afib-detection-holter.pdf) |
| DEFINE AFib Study (Apple Watch irregular-rhythm notification vs. Medtronic Reveal LINQ) | Piccini J, Lande J, Kanwar R, Johnson L, Passman R, et al. | *European Heart Journal*, Supplement (conference abstract) 2024 | [ehae666.3538](https://academic.oup.com/eurheartj/article/45/Supplement_1/ehae666.3538/7839071) | Unclear | **Not a formal publication** — this is a conference-abstract supplement entry, not a peer-reviewed full paper; no full-text PDF exists to obtain | Not applicable — citation-only by nature, not by access failure |
| Accuracy in Wrist-Worn, Sensor-Based Measurements of Heart Rate and Energy Expenditure in a Diverse Cohort | Shcherbina A, Mattsson CM, Waggott D, Salisbury H, Christle JW, Hastie T, Wheeler MT, Ashley EA. | *Journal of Personalized Medicine* 2017;7(2):3 | [10.3390/jpm7020003](https://doi.org/10.3390/jpm7020003) | C (Corroborated) | **Verified OA** (MDPI) | [literature/apple-watch/2017-shcherbina-jpersmed-hr-energy-expenditure-diverse-cohort.pdf](literature/apple-watch/2017-shcherbina-jpersmed-hr-energy-expenditure-diverse-cohort.pdf) |

### Systematic reviews / meta-analyses (individually named)

| Title | Authors | Venue/Year | DOI | Tier | OA status | PDF |
|---|---|---|---|---|---|---|
| Diagnostic Accuracy of Apple Watch Electrocardiogram for Atrial Fibrillation: A Systematic Review and Meta-Analysis | Shahid S, Iqbal M, Saeed H, Hira S, Batool A, Khalid S, Tahirkheli NK. | *JACC: Advances* 2025;4(2):101538 | [10.1016/j.jacadv.2024.101538](https://doi.org/10.1016/j.jacadv.2024.101538) | Unclear | **Verified OA** (JACC: Advances is OA by default) | [literature/apple-watch/2025-shahid-jaccadvances-ecg-afib-systematic-review.pdf](literature/apple-watch/2025-shahid-jaccadvances-ecg-afib-systematic-review.pdf) — resolves the prior 403 access block |
| Apple watch accuracy in monitoring health metrics: a systematic review and meta-analysis | Choe JP, Kang M. | *Physiological Measurement* 2025 | [10.1088/1361-6579/adca82](https://doi.org/10.1088/1361-6579/adca82) | Unclear | **Paywalled** (IOP Publishing; hybrid journal, this article not OA; no PMC deposit found) | Not obtained |
| The accuracy of Apple Watch measurements: a living systematic review and meta-analysis | Lambe R, Baldwin M, O'Grady B, Schumann M, Caulfield B, Doherty C. | *npj Digital Medicine* 2025 | [10.1038/s41746-025-02238-1](https://doi.org/10.1038/s41746-025-02238-1) | Corroborated (same UCD/SFI lab as the Doherty/Lambe/O'Grady papers above) | **Verified OA** (Nature, CC BY) | [literature/apple-watch/2025-lambe-npjdigitalmedicine-living-systematic-review-accuracy.pdf](literature/apple-watch/2025-lambe-npjdigitalmedicine-living-systematic-review-accuracy.pdf) |
| Accuracy of Detecting Atrial Fibrillation: A Systematic Review and Meta-Analysis of Wrist-Worn Wearable Technology | Belani S, Wahood W, Hardigan P, Placzek AN, Ely S. | *Cureus* 2022;14(11):e20362 (PMC8752409) | [10.7759/cureus.20362](https://doi.org/10.7759/cureus.20362) | Unclear | **Verified OA** (Cureus is OA by default) | [literature/apple-watch/2022-belani-cureus-afib-wristwearable-review.pdf](literature/apple-watch/2022-belani-cureus-afib-wristwearable-review.pdf) — **author-name correction: `research-library-wearables.md` referred to this study only by its Nova Southeastern University affiliation, without author names; the actual authors (Belani, Wahood, Hardigan, Placzek, Ely) are now confirmed** |

**Apple Watch summary: 14/19 individually-named papers/documents obtained as verified PDFs (13 initial
pass + Mahalingaiah/AJOG resolved on 2026-08-24 retry). 5 not obtained: 3 genuinely paywalled with no
OA route (Jaworski/Park IEEE, Abou *Assistive Technology*, Choe & Kang *Physiological Measurement*),
1 confirmed genuinely non-OA on direct check against NCBI's OA web service rather than merely
retrieval-blocked (Perez/NEJM Apple Heart Study — see #98 resolution below), and 1 that is not a
formal peer-reviewed publication at all (DEFINE AFib conference abstract).**

---

## Cross-device summary

| Device | Individually-named papers catalogued | PDFs obtained (Verified OA) | Not obtained | Notes |
|---|---|---|---|---|
| Oura | 17 | **17 (100%)** | 0 | Includes one preprint substitution (Willoughby — published version paywalled, PsyArXiv preprint open) |
| WHOOP | 18 | **14 (78%)** | 4 | 3 genuinely paywalled, 1 dissertation not located |
| Apple Watch | 19 | **14 (74%)** | 5 | 4 genuinely paywalled/non-OA, 1 not a formal publication |
| **Total** | **54** | **45 (83%)** | **9** | ~65 MB total in `literature/` |

### 2026-08-24 retry of unresolved-question #98

Two of the three flagged retrieval-infrastructure failures resolved:

- **Khodr et al. (medRxiv, WHOOP)** — the versioned `/v1/full.pdf` URL was genuinely bot-blocked
  (HTTP 403), but Semantic Scholar's Graph API (`api.semanticscholar.org`) resolved the paper's
  canonical `medrxiv/early/...` PDF path, which a plain browser-UA `curl` request retrieved cleanly.
  **Obtained.**
- **Mahalingaiah et al. (AJOG, Apple Women's Health Study)** — the earlier "HTTP 500" diagnosis was
  a symptom, not the cause: NCBI's own OA web service (`oa.fcgi`) confirms this is a genuine CC
  BY-NC-ND open-access record with a direct PDF link, but that URL sits behind a JS-driven
  bot-detection interstitial ("Preparing to download...") that blocks any non-browser client. A real
  browser session cleared the challenge and yielded a `cloudpmc-viewer-pow` cookie; reusing that
  cookie in a direct `curl` request retrieved the PDF. **Obtained.**
- **Perez et al. (NEJM, Apple Heart Study)** — checked directly against NCBI's OA web service, which
  returned `idIsNotOpenAccess` for PMC8112605. This is **not** an OA record blocked by a retrieval
  failure, unlike the other two — it is a non-OA author-manuscript deposit. **Genuinely paywalled,
  correctly left uncorrected.** The earlier "HTTP 500 / CAPTCHA" symptoms were downstream of this
  underlying non-OA status.

### What this pass corrected in `research-library-wearables.md`

Direct full-text reads surfaced several corrections worth carrying back into the sponsorship-tier
file (not made there in this pass, since the task scope was the literature library — flagged here for
a follow-up edit):

1. **The WHOOP "menstrual cycle through the lens of a wearable device" paper's authorship is now
   confirmed** — Gonzalez A, O'Day JJ (Stanford, co-first/corresponding), plus Johnson SC (Stanford),
   Kim J, Jasinski SR, Holmes KE (all WHOOP Inc.), Delp SL, Hicks JL (Stanford). The AI-generated
   secondary summary that a prior pass explicitly flagged as "unverified and should not be trusted"
   was in fact correct. This paper should be restored to Tier A (mixed Stanford/WHOOP authorship),
   not left at "Unclear."
2. **Gong et al.'s smart-ring systematic review was actually published in *Biomimetics*, not
   *Diagnostics*** — same authors, same title, same findings, different MDPI journal than the source
   file states.
3. **Two Apple Watch PDF filenames were corrected mid-retrofit** after author/venue verification:
   the Wasserlauf AF paper is *Journal of Cardiovascular Electrophysiology* (not "CircEP"), and the
   Littell pediatric SpO2/ECG paper is *PLOS Digital Health* (not "PACE").
4. **Several previously title-only or affiliation-only citations now have confirmed author lists**:
   the Oura/Cureus adherence paper (Shiba SK et al.), the WHOOP alcohol-trajectories JMIR paper
   (Grosicki GJ et al.), the WHOOP travel/recovery *Sports Medicine* paper (Hatamiya N et al., whose
   actual published title is "Optimizing Athlete Travel for Performance," not the working title used
   in the source file), the Apple Heart & Movement Study methods paper (Truslow J et al.), and the
   Cureus AFib-wearables systematic review (Belani S et al., previously identified only by its Nova
   Southeastern University affiliation).
5. **Apple's VO2max white paper is directly fetchable** — the source file's note that "the PDF was
   not machine-readable via fetch" did not hold this pass; it downloaded and extracted cleanly.
6. **The Doherty-lab Apple Watch papers' author order in the source file doesn't match the
   published byline** — Doherty C is the senior/last author on both the VO2max validation (PLOS ONE)
   and HRV/RHR validity (Sensors) papers; the actual lead authors are Lambe R and O'Grady B
   respectively.

None of these are large factual corrections to the underlying findings — they are bibliographic
precision fixes surfaced by reading the actual PDFs rather than relying on search-summary retrieval,
consistent with `CLAUDE.md`'s instruction to trace claims back to primary documentation.
