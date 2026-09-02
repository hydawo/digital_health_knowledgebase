# Meyer et al. 2018 — Sleepsight: 8-week continuous rest-activity monitoring in community schizophrenia, N=15

## Quick Facts

| Field | Details |
|---|---|
| Citation | Meyer N, Kerz M, Folarin A, Joyce DW, Jackson R, Karr C, Dobson R, MacCabe J. "Capturing Rest-Activity Profiles in Schizophrenia Using Wearable and Mobile Technologies: Development, Implementation, Feasibility, and Acceptability of a Remote Monitoring Platform." *JMIR mHealth and uHealth* 2018;6(10):e188. DOI [10.2196/mhealth.8292](https://doi.org/10.2196/mhealth.8292). PMID 30377146 / PMC6234334. |
| Study design | Development-and-feasibility study with pre-specified acceptability thresholds (**wear time or diary response rate ≥70%**), plus end-of-study usability questionnaire and qualitative analysis. Reported against the WHO **mHealth Evidence and Assessment (mERA)** checklist. |
| Sample size (enrolled / analyzed) | **15 recruited, 14 (93%) completed** |
| Population | Adults 18–65 meeting ICD-10 criteria for schizophrenia, recruited through community psychiatric services in South London. **Not selected on clinical status**; mostly low-mild symptom intensity (mean total PANSS 58.4, SD 14.4), but 2 participants had severe negative symptoms and treatment-resistant illness. |
| Duration | **8 weeks** continuous |
| Devices/platforms used | **[Fitbit](../../module-01-wearables/profiles/fitbit-google.md) Charge HR** + **Motorola Moto G (2nd gen)** Android smartphone running **Purple Robot** (Northwestern CBITs). **Provisioned, including a 4G data plan.** |
| Funding/COI | Academic (KCL Institute of Psychiatry, Psychology and Neuroscience; SLaM NHS Trust; Northwestern). Purple Robot is a Northwestern CBITs product and a CBITs-affiliated author is on the paper. |
| Last verified | 2026-08-31 |

## Summary

Small, but it does something no other study here does: it **records why the research-grade wearables
were rejected**, and then demonstrates that the consumer device chosen instead achieved
near-perfect adherence in a population widely assumed to be hard to monitor.

**Initial user-group testing with GENEActiv, ActiGraph GT9X Link and the Empatica E4 concluded they
"would not be acceptable for extended use"** — on appearance and stigma grounds. The user groups
instead favoured the **Fitbit Charge HR** precisely because it looks like a lifestyle device and
lets the wearer see their own sleep and activity. That is a direct, documented tradeoff of **data
fidelity for wearability**, made deliberately, with patients in the room.

The result: **mean wear time 21.8 hours/day, 91% of total study duration, with every participant
meeting the ≥70% threshold.** Sleep diary completion 91%, symptom diary 88%. And the finding that
most directly contradicts received wisdom: **paranoia about the study devices was not a significant
barrier to engagement.**

What *did* predict lower adherence was **negative symptoms** — and strongly.

## Instrumentation and Deployment Model

**Fully provisioned, including connectivity:** study devices, charging cables and adapters, and a
**4G contract with 5 GB/month**, so data could upload continuously regardless of home internet. This
removes the connectivity eligibility filter that excluded 11 patients in
[Jonker et al.](withings-postop-remote-monitoring.md).

**Six stated design principles, and each carries a transferable lesson:**

1. **User-centred design.** People with psychosis were involved throughout development — advising on
   device selection, app design, recruitment strategy, data feedback and incentivisation. A
   *separate* patient group then took part in the feasibility study.
2. **Integration with everyday life.** Research wearables were tested and rejected (above).
3. **Wireless.** Fitbit transferred to the phone and exposed **minute-level activity, sleep and heart
   rate via API calls to the Fitbit server**. The authors are explicit about the cost: **"data are
   preprocessed on the device… which precludes access to raw sensor data."** Charging roughly every 5
   days, ~2 hours; splashproof but not waterproof.
4. **Remote and real-time.** Adherence with the wearable and both diaries was **monitored in
   real time**, and **if adherence lapsed for ≥2 days — e.g. no signal from the wearable — a text
   prompt was sent, followed by a telephone call if necessary.**
5. **Secure.** Usernames obfuscated with an MD5 hash; data encrypted in transit; cached on the phone
   until connectivity was available then cleared after transmission; unique identifiers with no
   personally identifiable digital information stored or transmitted.
6. **Open source.** Platform code published to support replication and external validity.

**A privacy decision made by the user group, not the researchers: GPS location, and call and text
message content, were *not* captured**, because the user group advised this would be perceived as
intrusive. Purple Robot instead sampled the **smartphone accelerometer and light sensor, battery
level, and screen-unlock frequency**. This is the clearest example in the module of participants
constraining the sensor set — and it is worth noting the study still worked.

**Active data:** a once-daily sleep diary (bed time, out of bed, sleep quality) followed by a 2–3
minute self-report symptom diary. Each complete submission triggered **a short motivational message
("good job — see you tomorrow!")**. The app included a help section with device instructions and
contact details.

## Recruitment and Retention

**14 of 15 (93%) completed the 8-week study.** Participants were recruited via clinical teams and
were **not selected on clinical status**. Notably, **not all participants owned a mobile device of
their own, and just over half had a touchscreen device** — so the provisioning decision was
substantive, not a convenience.

## Data Completeness and Technical Issues

**Adherence against the pre-specified ≥70% threshold:**

| Measure | Result | Met threshold |
|---|---|---|
| **Wearable wear time** | **21.8 h/day = 91% of study duration** | **All participants (14/14)** |
| Sleep diary completion | mean **91%** (51/56 questionnaires) | 93% (13/14) |
| Symptom diary completion | mean **88%** (49/56) | 86% (12/14) |

**21.8 hours/day over 8 weeks is the highest provisioned-device wear time in this module** —
comparable to the BYOD consumer figures in [the Fitbit Heart Study](fitbit-heart-study-afib.md)
(23 h/day) and far above RADAR-MDD's provisioned 15.1 h/day over a longer horizon.

**Symptom severity predicted adherence, and negative symptoms dominated:**

| Correlation | ρ | P |
|---|---|---|
| PANSS **negative** × sleep diary completion | **−0.75** | **.001** |
| PANSS **negative** × symptom diary completion | −0.53 | <.05 |
| PANSS **negative** × wearable adherence | −0.49 | <.05 |
| PANSS positive × sleep diary completion | −0.49 | <.05 |
| PANSS positive × symptom diary completion | −0.40 | <.01 |
| **Age × adherence (diaries and wearable)** | **non-significant** | — |

**The two participants who fell at or below the feasibility threshold both scored in the severe
range on negative symptoms (PANSS negative 29 and 36) and had treatment-resistant illness.** One
received **four further weekly top-up training sessions** after reporting difficulty with the diaries
and with using the smartphone for calls and texts.

Note the ordering: **negative symptoms (amotivation, blunted affect) were a stronger barrier than
positive symptoms (paranoia, hallucinations)** — ρ=−0.75 versus −0.49 for sleep diary completion.
This is the opposite of the intuition that drives most concern about monitoring people with
psychosis, and it converges with [Raugh et al.](dp-schizophrenia-tolerability.md), where negative
symptoms and functioning also predicted passive-stream adherence.

**Validity check:** sleep diary and wearable-estimated sleep times showed **good correspondence
(ρ=0.50, P<.001)**.

## Feasibility Findings

The authors' conclusion: **extended use of wearable and mobile technologies is acceptable to people
with schizophrenia living in a community setting**, and **paranoia with study devices was not a
significant barrier to engagement** — a finding they highlight precisely because the field assumed
otherwise.

Design decisions that plausibly produced these numbers, and which should be read as the cost of
them:

- Devices, phone **and mobile data** all provided.
- **Real-time adherence monitoring with escalating outreach** (text at 2 days, then phone call).
- **In-person training, with top-up sessions** where a participant struggled.
- **Motivational feedback** on each diary submission.
- The device chosen was one participants could see their own data on and were happy to be seen
  wearing.

## Relevance to Future Study Design

1. **Let the target population choose the device.** Research-grade wearables were rejected on
   appearance and stigma; the consumer device they picked delivered 91% wear over 8 weeks. Sensor
   specification is worthless if the device is not worn.
2. **Know what you give up.** Choosing a consumer device meant **no raw sensor data** — only
   Fitbit's preprocessed minute-level output via API. That forecloses reanalysis and ties the study
   to a vendor's algorithms. See
   [`../../module-01-wearables/profiles/fitbit-google.md`](../../module-01-wearables/profiles/fitbit-google.md).
3. **Screen and support on negative symptoms, not paranoia.** PANSS negative was the strongest
   adherence predictor (ρ=−0.75). Paranoia was not a barrier. Age was not a barrier.
4. **Build real-time adherence alerts with a defined escalation ladder** — 2 days of silence → text →
   phone call. Cheap, and the same pattern [Huang et al.](beiwe-adolescent-feasibility.md) used
   manually to reach 89% passive completeness.
5. **Provide connectivity, not just hardware**, where the population may lack it. Not all
   participants owned a mobile device.
6. **Accept participant-imposed sensor restrictions.** GPS and message content were dropped on user
   advice and the study still met all its aims — a reminder that maximal sensing is not always
   necessary sensing.
7. **Budget for retraining.** One of 14 participants needed four extra weekly sessions.

## Evidence Confidence

**Verified** for the adherence figures, correlation coefficients, completion rates and device
selection rationale — primary reported results read from the full text.

**Very small (N=15, 14 completing) and mostly mild-to-moderate in symptom severity.** The
correlations, especially ρ=−0.75 on 14 participants, are estimated with wide uncertainty and should
be treated as **indicative rather than precise**. The two below-threshold participants are the
entire basis for the severe-negative-symptom finding.

**Selection:** recruited via clinical teams in one South London service; participants had capacity to
consent and no gross cognitive, sensory or motor impairment precluding device use. The population
that could not use the devices was excluded by design, so this does not speak to feasibility across
all schizophrenia.

**Dated (2018).** The Fitbit Charge HR, the Moto G 2nd generation and the Android background-execution
regime of that era are all superseded. **Wear-time and adherence findings likely transfer; the
technical specifics do not.**

**COI:** Purple Robot is a Northwestern CBITs platform and a CBITs-affiliated author is on the paper.
The findings concern adherence rather than platform comparison, limiting what this could distort.

**Device misattribution corrected.** My discovery pass tagged this study as an Empatica deployment
because the E4 is named in the text. **It is not — the E4 was tested and rejected.** The study used a
Fitbit Charge HR. This profile was renamed from `empatica-sleepsight-schizophrenia` accordingly, and
the record is noted here so the error is not silently repaired.

## Key Links

- Paper (OA, CC BY): https://doi.org/10.2196/mhealth.8292 · https://mhealth.jmir.org/2018/10/e188
- Europe PMC: https://europepmc.org/article/MED/30377146
- **PDF not obtained** — both the PMC and JMIR PDF routes failed this pass. Full text read from the
  Europe PMC XML deposit. Logged as Tier 14 Q110 in `../../shared/unresolved-questions.md`.

## Related profiles

- Device: [Fitbit / Google](../../module-01-wearables/profiles/fitbit-google.md)
- Devices rejected here, profiled elsewhere:
  [Empatica](../../module-01-wearables/profiles/empatica.md),
  [Axivity / GENEActiv](../../module-01-wearables/profiles/axivity-geneactiv.md),
  [ActiGraph](../../module-01-wearables/profiles/ametris-actigraph.md)
- Same population, stream-by-stream adherence:
  [`dp-schizophrenia-tolerability.md`](dp-schizophrenia-tolerability.md)
- Same population, multi-site, much larger:
  [`mindlamp-relapse-3site.md`](mindlamp-relapse-3site.md)

## Sources

1. Meyer N, et al. *JMIR mHealth uHealth* 2018;6(10):e188. DOI 10.2196/mhealth.8292. Full text read
   from the Europe PMC XML deposit (PMC6234334), 2026-08-31. Establishes every figure in this
   profile.
