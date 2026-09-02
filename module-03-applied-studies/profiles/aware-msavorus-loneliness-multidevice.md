# Nguyen et al. 2025 — mSavorUs: AWARE + Oura Ring + Samsung Watch in college students, N=29 over 22 weeks

## Quick Facts

| Field | Details |
|---|---|
| Citation | Nguyen B, Lai J, Qureshi H, Marcotullio C, Labbaf S, Wang Y, Jafarlou S, Dutt N, **Rahmani AM**, Borelli JL. "Feasibility, Acceptability, and Preliminary Outcomes of a Mobile Adaptation of a Relational Savoring Intervention to Prevent Loneliness in College Students: Mixed Methods Pilot Study." *JMIR Formative Research* 2025;9:e70528. DOI [10.2196/70528](https://doi.org/10.2196/70528). PMID 40921010 / PMC12518887. |
| Study design | Randomized controlled **pilot** with a mixed-methods design: Aim 1 thematic analysis of participant feedback on the intervention *and the monitoring tools*; Aim 2 quantitative outcomes (loneliness, connectedness). |
| Sample size (enrolled / analyzed) | **37 enrolled → 8 withdrew → 29 analyzed.** |
| Population | US college students (single university), mean age **19.93 (SD 1.22)**; 13 male / 16 female; **43.3% Latinx, 43.3% Asian American, 17.2% White** — one of the few genuinely non-White-majority cohorts in this module. Excluded: parents, married students, and those returning after a ≥3-year absence. |
| Duration | **22 weeks**, enrolled late Jan – early Feb 2021 (i.e. during COVID-19 restrictions). Three phases: initial monitoring, intervention, continued monitoring. |
| Devices/platforms used | **[AWARE](../../module-02-digital-phenotyping/profiles/aware-framework.md)** (passive smartphone sensing) + **[Oura](../../module-01-wearables/profiles/oura.md) Ring** + **[Samsung](../../module-01-wearables/profiles/samsung.md) Gear Sport smartwatch** + **mSavorUs** (custom intervention app). All wearables **provisioned**. |
| Funding/COI | Academic (UC Irvine). **AWARE deployment and mSavorUs are attributed in-text to co-author Amir Rahmani ("developed by AR")** — a developer-author relationship on both the intervention and the sensing stack. |
| Last verified | 2026-09-01 |

## Summary

This module's **first entry covering either Oura or Samsung**, and its longest multi-device consumer-wearable deployment at 22 weeks — an unusually demanding instrument load (ring + smartwatch + two study apps + the vendors' own apps) carried by a young, ethnically diverse, non-clinical cohort.

Two things make it worth reading despite its small size. First, **EMA adherence is reported by study phase rather than as a single number**, and it declines monotonically: **79% during initial monitoring → 75% during the intervention → 69% overall across all 602 possible observations**. Second, the qualitative arm asked about the *monitoring apparatus* as well as the intervention, and produced a rare explicit statement of a technical-burden dropout: **one participant withdrew because of the burden of managing technical difficulties**.

The intervention itself did not work (no significant reduction in loneliness or increase in connectedness), and the authors attribute this to **delivery timing rather than content** — participants found the content valuable but the just-in-time prompts disruptive. That is a deployment finding, not only a clinical one.

## Instrumentation and Deployment Model

**Fully provisioned wearables on a BYOD phone.** At an in-person baseline, participants were given an **Oura Ring** and a **Samsung Gear Sport smartwatch**, and installed **four apps**: mSavorUs (the intervention), **AWARE** (passive smartphone sensing), and the Oura and Samsung companion apps. Each participant received a study ID pre-assigned across the apps.

Stream allocation as described: the **Oura Ring for sleep** (duration, and averaged sleep-quality measures); the **Samsung watch for daytime physiology and activity**; **AWARE for behavioural context** — GPS-derived time at home, and phone-interaction measures such as time spent texting, calling and browsing.

**Multiple concurrent apps is itself the design decision under test.** Four apps plus two chargers, for 22 weeks, is at the upper end of what this module has seen imposed on a non-clinical cohort — the closest comparators being [RADAR-AD](radar-ad-feasibility-usability.md)'s eight device types and [Johnson-style](../_inventory-and-scope-decisions.md) two-wearable ALS designs.

## Recruitment and Retention

- **37 enrolled, 8 withdrew (21.6%), 29 analyzed.** Only one withdrawal reason is given in the text — technical burden — so **the remaining seven are unattributed**.
- Retention over 22 weeks at 78.4% is respectable for the instrument load, but the study reports no survival analysis and no timing of withdrawals.

## Data Completeness and Technical Issues

**EMA adherence, by phase** (definition: completed EMA observations ÷ scheduled observations):

| Phase | Adherence | Detail |
|---|---|---|
| Initial monitoring | **79%** | mean 166.04 (SD 35.00), range 60–202 of 210 possible |
| Intervention | **75%** | mean 105.57 (SD 35.97), range 14–139 of 140 possible |
| Overall (whole study) | **69%** | mean 417.96 (SD 137.63), range 87–579 of 602 possible |

The implied continued-monitoring-phase figure is lower still, and the **range widens dramatically** — from 60–202 in phase 1 to 14–139 during the intervention. A participant completing 14 of 140 intervention-phase prompts is contributing essentially nothing while still counting as retained. This is the same retention-versus-completeness divergence [Matcham et al.](radar-mdd-recruitment-retention.md) document at much larger scale.

**Named technical failures:**

- **"On at least 2 occasions, data from AWARE were not being received"**, requiring the research team to keep in close communication with participants to troubleshoot. No count of affected participants or lost days is given.
- Participants **had trouble submitting surveys and intervention responses through mSavorUs**, requiring the computer-science team to intervene directly.
- **One withdrawal was caused by the cumulative burden of managing these difficulties.**

**Wearable wear time and Oura/Samsung data completeness are not reported.** This is the profile's biggest gap: a 22-week two-wearable deployment that does not publish wear-time or device-yield figures cannot be used as evidence about either device's adherence characteristics. Do not cite this study for Oura or Samsung wear compliance.

## Feasibility Findings

**Aim 1 (qualitative).** Participants found the mSavorUs *content* rewarding and helpful, but the **timing of just-in-time delivery was often experienced as disruptive**. Managing the monitoring apparatus generated its own friction.

**Aim 2 (quantitative).** **No significant reduction in loneliness and no significant increase in perceived connectedness.** The authors' interpretation is that the delivery format, not the intervention content, limited effectiveness, and that future iterations should reconsider timing and delivery strategy.

The deployment-relevant reading: **a just-in-time adaptive intervention triggered off passive sensing was, in this cohort, undermined by the trigger rather than the payload.** Any study planning JITAI delivery on top of a phenotyping stack should treat prompt timing as an intervention component requiring its own piloting.

## Relevance to Future Study Design

1. **Report EMA adherence by study phase.** The 79%→75%→69% decline would be invisible in a single headline number, and the phase in which adherence is lowest is the phase during which the intervention is delivered — exactly where data loss is most costly.
2. **Ranges matter more than means in small pilots.** A 14–139 range on a 140-prompt phase means the mean is describing very few people.
3. **App count is a burden variable.** Four study-related apps plus two chargers produced documented troubleshooting load and at least one withdrawal.
4. **Do not assume silent passive collection.** AWARE stopped delivering data at least twice and only staff–participant contact recovered it. This is the same class of dependency [Beukenhorst et al.](beiwe-als-adherence.md) describe for Beiwe: passive collection needs active monitoring.
5. **Publish wear time.** A 22-week Oura + Samsung deployment is scarce and valuable; without wear-time reporting most of that value is lost.

## Evidence Confidence

**Verified** — the 37/8/29 enrolment flow, the demographic composition, the 22-week duration, all three phase-level adherence figures with their means, SDs and ranges, the device and app inventory, the two named AWARE/mSavorUs technical failures, the single technical-burden withdrawal, and the null result on loneliness and connectedness. Read from the full text (Europe PMC PMC12518887), 2026-09-01.

**Unclear** — Oura and Samsung wear time and data yield (not reported); reasons for 7 of 8 withdrawals (not reported); the number of participants or days affected by the AWARE outages; and whether the continued-monitoring phase adherence figure was computed and simply not stated.

**Small-sample caution.** N=29 analyzed, single site, one university, enrolled during COVID-19 restrictions in early 2021, when both loneliness levels and daily mobility were atypical. Treat all quantitative figures as pilot-scale.

**COI:** co-author Amir Rahmani is credited in-text as the developer of both mSavorUs and the AWARE deployment. The paper's headline quantitative result is null and its qualitative arm surfaces technical failures, which runs against interest; the feasibility framing does not.

## Key Links

- Paper (OA, CC BY): https://doi.org/10.2196/70528
- Europe PMC: https://europepmc.org/article/PMC/PMC12518887
- Local PDF: `../literature/2025-nguyen-jmirformres-msavorus-loneliness-multidevice-pilot.pdf`

## Related profiles

- Platform: [AWARE](../../module-02-digital-phenotyping/profiles/aware-framework.md)
- Devices: [Oura](../../module-01-wearables/profiles/oura.md), [Samsung](../../module-01-wearables/profiles/samsung.md)
- Multi-device instrument load: [`radar-ad-feasibility-usability.md`](radar-ad-feasibility-usability.md)
- Retention vs completeness divergence: [`radar-mdd-recruitment-retention.md`](radar-mdd-recruitment-retention.md)
- Passive collection requiring active monitoring: [`beiwe-als-adherence.md`](beiwe-als-adherence.md)

## Sources

1. Nguyen B, et al. *JMIR Form Res* 2025;9:e70528. DOI 10.2196/70528. Full text read from Europe PMC (PMC12518887), 2026-09-01. Establishes every figure in this profile.
