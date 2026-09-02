# Huang et al. 2025 — Beiwe digital phenotyping in adolescents with bipolar disorder over 18 months, N=48

## Quick Facts

| Field | Details |
|---|---|
| Citation | Huang D, Emedom-Nnamdi P, **Onnela JP**, Van Meter A (co-senior authors). "Design and feasibility of smartphone-based digital phenotyping for long-term mental health monitoring in adolescents." *PLOS Digital Health* 2025;4(7):e0000883. DOI [10.1371/journal.pdig.0000883](https://doi.org/10.1371/journal.pdig.0000883). PMC12212497. |
| Study design | Prospective observational cohort, 18 months, two groups (bipolar disorder vs typically developing). **Preliminary — data collection was still ongoing at publication.** |
| Sample size (enrolled / analyzed) | **48 analyzed** (those who had completed participation) — 26 bipolar disorder, 22 typically developing. **39/48 (81%) completed the full 18 months.** |
| Population | Adolescents aged 14–19. Mean baseline age 15.85 (SD 1.37); 54% female, 42% male, 4.2% other. **54% from a minoritized racial/ethnic background** — 46% non-Hispanic White, 23% Hispanic, 15% non-Hispanic Asian/South Asian, 6.2% non-Hispanic Black, 10% other. **96% iPhone.** Parental education significantly higher in the TD group (mother 16.27 vs 14.35 years, p=0.018; father 15.82 vs 13.64, p=0.018). |
| Duration | 18 months intended; **mean participation 17.1 months (SD 3.7)**. Spanned the initial COVID-19 lockdown period. |
| Devices/platforms used | **[Beiwe](../../module-02-digital-phenotyping/profiles/beiwe.md)** — participants' own phones (BYOD). Passive: accelerometer, GPS, gyroscope and others. Active: thrice-weekly surveys. Plus **monthly clinical interviews** with participant *and* caregiver. |
| Funding/COI | Academic (Harvard Chan Biostatistics; NYU Grossman Child & Adolescent Psychiatry; CSU Long Beach). Onnela, Beiwe's originator, is co-senior author. **Participants were paid** — see below. |
| Last verified | 2026-08-31 |

## Summary

The longest adolescent digital phenotyping deployment on record — the authors state it is the first
to follow adolescent patients and community controls for **more than a year** — and the clearest
demonstration in this module that **passive and active data decay on completely different curves**.

Over 18 months: **passive data completion was 89% and, critically, flat over time** (90% → 95% →
95% → 94% across four blocks). **Active survey completion averaged 47% and collapsed monotonically**
— 65% → 52% → 40% → 30%. Clinical interviews, the most human-intensive channel, held best at 99%
overall but still declined 98% → 82%.

That divergence is the finding. It says that for multi-year monitoring, self-report surveys are not
a viable primary instrument regardless of how short you make them, while passive collection is
essentially durable once established. The authors state this directly: surveys "are not a viable
option for frequent assessment over months or years due to declining adherence over time."

## Instrumentation and Deployment Model

**BYOD, overwhelmingly iOS (96%; only 2 of 48 on Android)** — which limits any OS-comparison read
and, given the Android disadvantage documented in
[Yi et al.](beiwe-chronic-disease-substudy.md) and
[Kiang et al.](beiwe-missing-data-sociodemographic.md), likely makes these completeness figures
*favourable* relative to a mixed-OS cohort.

Three parallel data channels:

1. **Beiwe passive** — accelerometer, GPS, gyroscope and others, continuously.
2. **Beiwe active** — thrice-weekly surveys.
3. **Monthly clinical interviews** with the participant and a caregiver.

**The engagement model, which differs deliberately per channel and is the most instructive design
detail here:**

| Channel | Reminder regime | Completion |
|---|---|---|
| Clinical interviews | **Participants reminded by the study team, and interviews rescheduled when missed** | **99%** |
| Passive data | Study team **monitored metadata (volume)** and contacted participants when no data appeared over multiple days | **89%** |
| Active surveys | **App notification only — no direct reminders from the study team.** Participants were told at month end, with their payment, how many surveys they had missed | **47%** |

The completion ordering follows the intensity of human contact almost exactly. The authors note the
passive-data monitoring loop **could be automated**, which would cut its cost substantially.

**Compensation:** participants were paid, but **passive data earned only up to $1.50 per week**. The
authors flag payment as a limit on clinical generalisability while arguing that in a care setting,
provider feedback on what the data showed would plausibly motivate more than the small sums did.

## Recruitment and Retention

- **39/48 (81%) completed the full 18 months.**
- Mean participation **17.1 months (SD 3.7)** — BD 17.7 (SD 2.9), TD 16.5 (SD 4.5), p=0.085.
- **9 dropped out — 5 bipolar, 4 typically developing (19% vs 18%, p>0.999).** Diagnosis did not
  predict dropout.
- The authors report **no differences between completers and dropouts** on measured characteristics.

81% completion over 18 months in an adolescent clinical cohort is a strong result and considerably
better than the adult comparators in this module over similar horizons.

## Data Completeness and Technical Issues

**Overall completion by channel:**

| Channel | Overall | Bipolar | Typically developing | Test |
|---|---|---|---|---|
| Clinical interviews | **99%** (826/835) | 98% | 99% | χ²=1.84, p=0.175 (ns) |
| **Passive data** | **89%** (22,233/25,029 days) | **87%** | **91%** | χ²=109.09, **p<0.0001** |
| Thrice-weekly surveys | **47%** (4,945/10,448) | **44%** | **52%** | χ²=71.45, **p<0.0001** |

**Completion over time — the central table:**

| Period | Active surveys | Passive data | Clinical interviews |
|---|---|---|---|
| First 20 weeks | **65%** | 90% | 98% (first 4 mo) |
| Second 20 weeks | 52% | 95% | 94% |
| Third 20 weeks | 40% | 95% | 92% |
| Final 19 weeks | **30%** | **94%** | 85% → 82% (last 3 mo) |

**Passive completion did not decay — it rose slightly and then held.** Active survey completion more
than halved. This is the cleanest demonstration of the divergence in the module, because both
streams came from the same app on the same phone in the same participants.

**Group differences converged over time**: TD survey completion started well above BD (70% vs 56%
before week 29) but the gap closed later (41% vs 36%). Same pattern for passive (early 93% vs 90%;
later 95% vs 94%).

**Data quality metrics:**

- Mean survey duration **50.51 s** (median 34.70 s; range 2.78 s to 1.5 hours). **~98% of responses
  fell inside the acceptable 15 s – 5 min window**, with more out-of-range among BD (2.3% vs 0.9%,
  p<0.001).
- BD participants took longer per survey on average (**56 s vs 45 s**), which the authors read as
  possibly reflecting cognitive-function differences.
- **Survey duration declined until week 20 then stabilised**, attributed to familiarity — a useful
  reminder that response *time* is not a stable quality metric early in a study.
- Per-person passive data volumes: **accelerometer 4,101 MB** (SD 2,091, max 8,822), **gyroscope
  4,867 MB** (SD 2,182, max 9,704), **GPS 120 MB** (SD 65, max 261). **No significant BD/TD
  difference in volume**, but volume was highly variable across individuals.

**Causes of variation the authors offer** for passive data quality differences: phone operating
system differences, **available storage space on the participant's phone**, or other unmeasured
factors. Storage space is a failure mode not named in any other profile in this module.

**A maintenance burden named explicitly:** *"when there are app modifications or phone operating
system upgrades, patients may need to reregister their app or take other steps for the app to
continue working properly."* In a clinical deployment this implies a staff member must monitor data
and actively help participants maintain the app — an ongoing operational cost, not a one-off setup.

## Feasibility Findings

The authors conclude digital phenotyping is a **viable approach to long-term monitoring requiring
less time and resources than traditional approaches**, and that passive data is "a practical,
nonburdensome way to monitor mental health in this population long-term."

Their stated design conclusions:

1. **Surveys are not viable for frequent assessment over months or years.** Stated plainly, on their
   own data, and consistent with the literature they cite.
2. **Passive-data monitoring with automated re-engagement prompts is the scalable pattern** — they
   note their manual "contact them if no data for several days" loop could be automated. (This is
   conceptually the same problem Beiwe's later `heartbeat` feature addresses in software; see
   [`beiwe-als-adherence.md`](beiwe-als-adherence.md).)
3. **Reminder intensity drives completion.** The three-channel contrast is effectively a natural
   experiment: team-reminded-and-rescheduled 99%, metadata-monitored 89%, app-notification-only 47%.
4. Clinical translation requires a staff member to monitor data and maintain apps through OS
   upgrades, at an interaction level the authors say is "not clear."

## Relevance to Future Study Design

1. **Do not build a multi-year design on survey completion.** 65% → 30% over 18 months, with short
   surveys (median 35 seconds) and monthly payment feedback, is close to a best case.
2. **Passive collection, once established, is durable.** Flat at ~94% from month 5 to month 18 is the
   strongest longevity evidence in this module and directly contradicts the assumption that all
   remote data decays.
3. **Match reminder intensity to how much you need each channel.** Cheap app notifications bought
   47%; human rescheduling bought 99%.
4. **Monitor passive data volume as an operational alert and automate it.** This study did it
   manually and got 89%.
5. **Ask about phone storage space at screening** alongside OS — the authors name it as a plausible
   driver of individual variation.
6. **Plan for app re-registration at OS upgrades** as recurring operational work over a long study.
7. **Adolescents and a bipolar diagnosis were not adherence barriers** — 81% completion, and
   diagnosis did not predict dropout. The BD/TD completeness gaps were statistically significant but
   small in magnitude (87% vs 91% passive), and they narrowed over time.
8. **Budget storage:** ~9 GB per participant across accelerometer and gyroscope alone over 18 months.

## Evidence Confidence

**Verified** for all retention, completion, timing, duration and data-volume figures — primary
reported results read from the published PDF.

**Limitations the authors state:**

- **Preliminary.** Data collection was ongoing; these are 48 participants, not the final cohort.
- **COVID-19 lockdown overlapped much of the collection**, with effects the authors say are hard to
  sign — more phone time during lockdown, but also high family stress and fewer youth presenting for
  psychiatric care. Importantly, **sensitivity analyses found no difference in data completeness for
  participants enrolled in 2020 or after**, which is real if partial reassurance.
- **Consent-based selection**: not everyone approached consented, and those who did may be more
  engaged with technology.

**Additional caveats this profile adds:**

- **96% iPhone.** Given the Android penalty documented elsewhere in this module, these completeness
  figures should not be transferred to an Android-heavy cohort.
- **Small N (48) with a clinical/control split of 26/22.** The highly significant χ² values on
  completion reflect the very large number of *observations* (25,029 days, 10,448 surveys), not a
  large number of participants — the group differences are precisely estimated but small.
- **Pre-heartbeat** (collection predates the mid-2024 rollout), though this study's manual
  data-monitoring loop was performing a similar function by hand.

**COI:** Onnela, Beiwe's originator, is co-senior author. The paper reports 47% survey completion
without minimising it and concludes that a core Beiwe feature (surveys) is unsuitable for long
studies, which cuts against platform interest.

## Key Links

- Paper (OA, CC BY): https://doi.org/10.1371/journal.pdig.0000883
- Europe PMC: https://europepmc.org/article/PMC/PMC12212497
- Local PDF: `../literature/2025-plosdigitalhealth-beiwe-adolescent-digital-phenotyping-feasibility.pdf`

## Related profiles

- Platform: [Beiwe](../../module-02-digital-phenotyping/profiles/beiwe.md)
- Same platform at scale, same passive > active ordering:
  [`beiwe-chronic-disease-substudy.md`](beiwe-chronic-disease-substudy.md)
- Same platform, no engagement scaffolding at all:
  [`beiwe-als-adherence.md`](beiwe-als-adherence.md)
- Same divergence on other platforms:
  [`radar-mdd-longterm-engagement.md`](radar-mdd-longterm-engagement.md),
  [`mindlamp-relapse-3site.md`](mindlamp-relapse-3site.md)

## Sources

1. Huang D, et al. *PLOS Digital Health* 2025;4(7):e0000883. DOI 10.1371/journal.pdig.0000883. Full
   text and tables read from the published PDF (via Europe PMC, PMC12212497), 2026-08-31.
   Establishes every figure in this profile.
