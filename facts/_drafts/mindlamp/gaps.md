# mindLAMP: gap hunter findings (baseline run, 2026-10-11)

Compared against `module-02-digital-phenotyping/profiles/mindlamp.md` (profile),
`module-02-digital-phenotyping/comparison-matrix.md` (matrix) and `facts/mindlamp.yaml` (every field still
`unresearched`, so every finding below is "no" for the yaml). Every quote below was checked with
`tools/facts/quote_probe.py` and returned `exact` on 2026-10-11.

Abbreviations: KB = knowledge base. "Date" is the source's own date where it has one, else the read date.
GitHub issues and pull requests were read only. Nothing was opened, commented on or created.

Note for the judge: docs.lamp.digital has been rebuilt (Docusaurus, sitemap of about 200 pages including
`/privacy`, `/projects`, `/publications`, a blog and full sensor and API references). The two official-docs
researchers should cover it; findings 1 to 4 use its privacy page only because they contradict the KB
directly and are tied to repository evidence the docs researchers will not see.

## Contradictions

### 1. hipaa_statement: the mindLAMP docs privacy page does make a HIPAA safeguards claim, and reports a July 2025 penetration test
- **Found:** The KB says no HIPAA claim exists, but it checked only the Division's lab-site privacy page. The platform's own Security & Privacy Policy page at docs.lamp.digital claims safeguards "in line with" the HIPAA Security Rule. It also names the firm that ran a penetration test of the mobile and web apps in July 2025 on a BIDMC test environment, and tells other deployments to commission their own test. This is a vendor self-claim (cap at Corroborated); no certificate, SOC 2 or ISO 27001 evidence was found.
- **URL:** https://docs.lamp.digital/privacy
- **Quotes:** "LAMP offers physical and technical safeguards that are in line with the HIPAA Security Privacy Rule" / "Echelon Risk + Cyber previously performed penetration testing against both the Mobile and Web Application for mindLAMP in a test environment located on BIDMC infrastructure"
- **Date:** read 2026-10-11 (pen test dated July 2025 on the page)
- **Source type:** vendor_legal
- **In KB:** contradicts. Profile line 112 ("makes no HIPAA, SOC 2 or GDPR claim"), line 155, and matrix line 156 ("No HIPAA, SOC 2 or GDPR claim"). The pen test is not in the KB anywhere.

### 2. licence: the vendor says "no licensing restrictions"; the repositories carry no licence; an outside team's public licensing question has gone unanswered since July
- **Found:** The docs privacy page describes the platform as free, open source and without licensing restrictions. The repositories say otherwise: LAMP-server, LAMP-core-ios, LAMP-core-android and also LAMP-activities (not named in the KB) have no licence file, and LAMP-dashboard was relicensed to AGPL-3.0-only on 2026-08-25. An outside team evaluating mindLAMP for a research deployment asked in LAMP-platform issue #943 (opened 2026-07-22) whether the unlicensed repositories fall under BSD terms, because they would need to modify them. The issue had zero comments on 2026-10-11. This is the public form of the KB's own open question at profile line 153. Other unlicensed repos found by the GitHub API: LAMP-platform, LAMP-worker, LAMP-data-reports, LAMP-raphe, LAMP-oauth-server.
- **URL:** https://docs.lamp.digital/privacy ; https://github.com/BIDMCDigitalPsychiatry/LAMP-platform/issues/943 ; https://github.com/BIDMCDigitalPsychiatry/LAMP-dashboard/releases/tag/2026.08.05.2
- **Quotes:** "currently developed by Beth Israel Deaconess Medical Center but does not have any licensing restrictions for intellectual property" / "We were not able to find a LICENSE file in the following repositories" / "Relicensed from BSD 3-Clause to AGPL-3.0-only."
- **Date:** issue 2026-07-22; relicence 2026-08-25; read 2026-10-11
- **Source type:** vendor_legal; repository
- **In KB:** contradicts (vendor statement vs the KB's licence finding, which the repos support). Profile lines 11, 93, 134, 153; matrix line 30. Record `licence` as `conflict`. LAMP-activities' missing licence is new.

### 3. retention_terms: the published 90-day deletion promise is called inaccurate by the maintainers' own pending rewrite
- **Found:** The live privacy page promises a 90-day soft-delete window followed by permanent deletion. An open pull request by the lead engineer (LAMP-platform #939, opened 2026-03-16, not merged) rewrites the page to fix what it calls inaccurate data deletion claims: deleted records are soft-deleted and kept in the database until a site administrator removes them by hand, and event data (survey responses, sensor readings) cannot be deleted through the API at all. Until #939 merges, the public promise and the described behaviour disagree.
- **URL:** https://docs.lamp.digital/privacy ; https://github.com/BIDMCDigitalPsychiatry/LAMP-platform/pull/939 ; draft text at https://raw.githubusercontent.com/BIDMCDigitalPsychiatry/LAMP-platform/docs/update-security-privacy-policy/docs/07-privacy.mdx
- **Quotes:** "There is a soft-deletion period of 90 days during which the data is unavailable but may be restored by request" / "Fix inaccurate data deletion claims" / "Deleted data is **not permanently erased** from the database." / "does not currently support deletion through the API"
- **Date:** PR opened 2026-03-16, still open; read 2026-10-11
- **Source type:** vendor_legal; repository
- **In KB:** no (the KB has nothing on deletion or retention). Record as `conflict`. Matters for consent forms and GDPR erasure requests.

### 4. hipaa_statement / soc2 (closest fields; audit logging): "every request is logged" is claimed, but API audit logging is an open, unmerged work item
- **Found:** The privacy page says every create, read, update or delete request is added to an audit log, and the Core page lists audit logs as a service feature. The lead engineer's issue #910 (opened 2025-06-09, still open) says audit logging still needs to be implemented, and the contractor's pull request LAMP-server #264 ("Add Basic Audit Logging") was still open on 2026-10-11. So the audit trail may exist only at the infrastructure level, or only on some deployments; the code record does not show request-level audit logging in the released server.
- **URL:** https://docs.lamp.digital/privacy ; https://github.com/BIDMCDigitalPsychiatry/LAMP-platform/issues/910 ; https://github.com/BIDMCDigitalPsychiatry/LAMP-server/pull/264
- **Quotes:** "will cause the incremental addition of the request to an audit log" / "We need to implement comprehensive audit logging to track all API activity and data changes" / "Add Basic Audit Logging"
- **Date:** issue 2025-06-09; read 2026-10-11
- **Source type:** vendor_legal; repository
- **In KB:** contradicts (in part). Profile lines 97 and 112 and matrix lines 156 and 178 carry the Core's audit-log claim without this caveat. No schema field fits exactly; the judge may want a profile note.

### 5. derived_metrics: Cortex is not legacy; it is the named analytics layer, and a new framework (RAPHE) appeared in September 2026
- **Found:** The KB calls LAMP-cortex legacy and LAMP-toolkit its successor. LAMP-cortex is still maintained (pushed 2026-05-18, BSD-3-Clause per the GitHub API), docs.lamp.digital has a full `developer/cortex` section, the Core page names Cortex, and BIDMC's own AWS blog post of 2026-09-29 calls Cortex the analytics layer. A new public repository, LAMP-raphe (created 2026-09-29, no licence file), describes a reliability-aware phenotyping framework that runs Cortex, Forest or RAPIDS as interchangeable feature engines.
- **URL:** https://aws.amazon.com/blogs/industries/from-cloud-to-clinic-how-aws-powers-digital-psychiatry-at-scale/ ; https://github.com/BIDMCDigitalPsychiatry/LAMP-raphe
- **Quotes:** "Reliability-Aware Personalized Health Phenotyping Engine" / "Cortex can operate as one feature-extraction engine within RAPHE"
- **Date:** blog 2026-09-29; repo created 2026-09-29; read 2026-10-11
- **Source type:** secondary (co-authored by BIDMC staff on an AWS blog); repository
- **In KB:** contradicts. Profile lines 27, 39 ("LAMP-cortex (legacy)"); profile line 77 says derived metrics were never verified. RAPHE is absent.

### 6. Deployment scale: four different figures from the same team within weeks
- **Found:** The Core page says 50+ active sites. BIDMC's AWS blog (2026-09-29) says 65 sites, 42 projects, 17 countries, and that each site runs its own instance and keeps its own data. The docs project gallery says 36 projects in 16 countries (9 active). The Core page also says "50+ Published Studies" alongside "over 120 peer-reviewed publications".
- **URL:** https://www.digitalpsych.org/mindlamp-core ; https://aws.amazon.com/blogs/industries/from-cloud-to-clinic-how-aws-powers-digital-psychiatry-at-scale/ ; https://docs.lamp.digital/projects
- **Quotes:** "The platform is compatible with grant funding and currently supports 50+ active sites worldwide." / "mindLAMP is deployed at 65 sites, across 42 projects, and in 17 countries around the world." / "Each site stands up their own instance and retains their own data" / "36 Projects" / "16 Countries"
- **Date:** read 2026-10-11
- **Source type:** vendor_page; secondary
- **In KB:** contradicts (in part). Profile line 97 and matrix line 178 give only "50+ active sites". Not a schema field; a profile note that adoption figures vary by source.

### 7. raw_streams: text-message features are iOS SensorKit only, Health Connect is the Android wearable route, and the privacy page lists Health Connect types the app no longer requests
- **Found:** (a) BIDMC's AWS blog says call and text logs sync from the phone. The docs telephony reference says text features depend on SensorKit's messages-usage data, which is iOS-only and needs Apple's SensorKit research approval; the Android manifest on `master` requests neither READ_SMS nor READ_CALL_LOG (only READ_PHONE_STATE), so Android "calls" are call-state events, not a call log. The LAMP-swift client has SensorKit loaders (keyboard metrics, phone usage, messages usage, ambient light, visits, wrist detection). (b) Android wearable data comes through Health Connect (2026.05.17 release added the Health Connect disclosure), and a Wear OS companion app exists (target SDK moved to Android 15 in 2025.10.24). (c) The same 2026.05.17 release removed the Body Fat, Oxygen Saturation and Basal Metabolic Rate permissions, but the live privacy page still lists them among Health Connect types read.
- **URL:** https://aws.amazon.com/blogs/industries/from-cloud-to-clinic-how-aws-powers-digital-psychiatry-at-scale/ ; https://docs.lamp.digital/sensors-data/reference/telephony ; https://github.com/BIDMCDigitalPsychiatry/LAMP-core-android/releases/tag/2026.05.17 ; https://github.com/BIDMCDigitalPsychiatry/LAMP-core-android/releases/tag/2025.10.24 ; https://docs.lamp.digital/privacy ; manifest at https://raw.githubusercontent.com/BIDMCDigitalPsychiatry/LAMP-core-android/master/app/src/main/AndroidManifest.xml (no quote: it is an absence)
- **Quotes:** "GPS, accelerometer, screen time, and call and text logs sync from the patient’s phone into encrypted AWS storage" / "Text message features ( text_number , text_degree ) depend on the messages_usage raw feature from iOS SensorKit" / "Removes BodyFat,Oxygen Saturation and BasalMetabolicRate permission from app" / "Update WearOS target SDK to Android 15" / "Basal Metabolic Rate Distance Body Fat"
- **Date:** releases 2025-10-24 and 2026-05-17; read 2026-10-11
- **Source type:** secondary; vendor_docs; repository; vendor_legal
- **In KB:** no / contradicts in part. Profile lines 62 to 63 (calls Android "Yes", SMS "Unclear"), line 55 and matrix line 113 ("paired wearable (devices not itemized)"). Health Connect, Wear OS and SensorKit are absent from the profile.

## Missing programs and program changes

### 8. research_program / program_status: the LAMP Consortium was retired from the docs in favour of the Core interest form, and the community forum was archived for lack of use
- **Found:** Pull request LAMP-platform #930 (merged October 2025) removed the consortium and publications/users pages and added the new interest form that feeds the mindLAMP Core. Earlier, PR #891 (2025-03) removed forum links because the LAMP Forum "was archived due to lack of use". This explains the KB's dead `mindlamp.discourse.group` host and the 404 on the old publications URL (a new `/publications` page exists). The Core is now the only intake route; there is no separate consortium membership.
- **URL:** https://github.com/BIDMCDigitalPsychiatry/LAMP-platform/pull/930 ; https://github.com/BIDMCDigitalPsychiatry/LAMP-platform/pull/891
- **Quotes:** "Removing consortium,  publications/users, and adding new interest form" / "Recently the LAMP Forum was archived due to lack of use"
- **Date:** #930 opened 2025-09-15, closed 2025-10-22; #891 opened 2025-03-06
- **Source type:** repository
- **In KB:** no. Profile line 179 records only a DNS failure; line 166 a dead publications link. The consortium is not in the profile.

### 9. deprecations / export_routes: authentication upgrade retires password access for LAMP-py, forces staff 2FA or OAuth, and adds API keys
- **Found:** Announced 2026-07-17. Phase 1 (dashboard server picker) went live 2026-07-29. Phase 2 moves from Basic auth to server-side sessions, makes 2FA or OAuth mandatory for all staff, and replaces username/password in LAMP-py with API keys; scripts that log in with a password "will stop working after the release". The server code (sessions, OAuth, 2FA, API keys, mobile tokens) merged to LAMP-server `master` on 2026-09-30 but had not been released on 2026-10-11; mobile upgrade builds were in dev testing (issue #944). Self-hosted teams are unaffected until they upgrade, and upgrading is offered "through our Core services process".
- **URL:** https://docs.lamp.digital/blog/authentication-upgrade ; https://github.com/BIDMCDigitalPsychiatry/LAMP-server/pull/284 ; https://github.com/BIDMCDigitalPsychiatry/LAMP-platform/issues/944
- **Quotes:** "LAMP-py will require an API key instead of a username and password." / "these will stop working after the release" / "to discuss options through our Core services process" / "Two factor authentication" / "Prove that updating the mobile apps from the"
- **Date:** blog 2026-07-17; server merge 2026-09-30; release date not announced
- **Source type:** vendor_docs; repository
- **In KB:** no.

### 10. hosting_options: the released server is from July 2023; production runs it; self-hosters are frozen on it unless they go through the Core
- **Found:** The newest LAMP-server release is 2023.7.27. The August 2026 dashboard release notes say it runs against that production server, and the dev test environment in issue #944 is the same Basic-auth 2023.7.27 server. The dashboard notes also show that production ran from a feature branch from May 2026 and that the 2026.08.05 release shipped about sixteen months of unreleased work. "Actively maintained" in the KB is true of commits, not of server releases.
- **URL:** https://github.com/BIDMCDigitalPsychiatry/LAMP-server/releases ; https://github.com/BIDMCDigitalPsychiatry/LAMP-dashboard/releases/tag/2026.08.05 ; https://docs.lamp.digital/blog/dashboard-update-auth-phase-1
- **Quotes:** "2023.7.27" / "no server upgrade, no database migration, and no mobile app release is required or included" / "Production has been served from the" / "Self-hosted teams: all client updates (dashboard, mobile apps, SDKs) remain compatible with currently released server versions"
- **Date:** server release 2023-07-27; dashboard release 2026-08-05
- **Source type:** repository; vendor_docs
- **In KB:** no. Profile line 98 says "actively maintained" with no release date.

### 11. hosting_options / academic_vs_commercial: named outside deployments on their own servers, including a US Army program
- **Found:** The dashboard's new server gateway has branded cards for separately hosted deployments: Mount Sinai PREDiCTOR (`api.mindlamp.mshai.org`), McLean ITP (`api.mindlamp.itpmclean.org`) and SAFEGUARD, whose participant app is "Level Up", a life-skills program for US Army soldiers run with USUHS (`mindlamp.armylevelup.app`). Level Up has its own terms and privacy policy pages, which in October 2026 were updated to disclose Firebase and Sentry (LAMP-platform #948). This shows the dedicated-instance model in use and that some deployments add third-party analytics.
- **URL:** https://github.com/BIDMCDigitalPsychiatry/LAMP-dashboard/releases/tag/2026.08.05 ; https://github.com/BIDMCDigitalPsychiatry/LAMP-dashboard/releases/tag/2026.08.05.2 ; https://docs.lamp.digital/projects/safeguard
- **Quotes:** "PREDiCTOR card now uses the Mount Sinai PREDiCTOR study motif logo." / "New McLean ITP card on the server gateway" / "LevelUp card is labelled" / "Level Up is the app for SAFEGUARD, a life skills training program for U.S. Army soldiers."
- **Date:** 2026-08-05 and 2026-08-25
- **Source type:** repository; vendor_docs
- **In KB:** no.

### 12. Active data collection (no schema field): survey branching is configurable but does nothing at runtime
- **Found:** The dashboard release notes list, as a known issue present in all prior releases, that survey branching settings can be configured but are inert when participants take the survey. The same release line shows participant messaging and modules hidden behind feature flags.
- **URL:** https://github.com/BIDMCDigitalPsychiatry/LAMP-dashboard/releases/tag/2026.08.05.3 ; https://github.com/BIDMCDigitalPsychiatry/LAMP-dashboard/releases/tag/2026.08.05
- **Quotes:** "Survey branching settings remain configurable but inert at runtime" / "Messages icon hidden for participants"
- **Date:** 2026-09-21
- **Source type:** repository
- **In KB:** no. Matrix line 96 says branching depth "not benchmarked"; profile line 81 likewise.

### 13. app_availability: newer iOS builds exist only on TestFlight; the App Store build is still 2023
- **Found:** The App Store listing (iTunes lookup, 2026-10-11) is still v2023.5.2 of 2023-05-26. Issue #944 shows iOS builds distributed by TestFlight at version 2025.4.2 (509) for dev testing of the auth upgrade, which partly answers the KB's open question at profile line 157: newer iOS builds exist but are not public. Mobile builds are produced by an outside contractor (Zco); the server auth refactor came from a `zagaran/auth-refactor` branch (Zagaran also develops Beiwe). Google Play shows 1K+ downloads.
- **URL:** https://github.com/BIDMCDigitalPsychiatry/LAMP-platform/issues/944 ; https://github.com/BIDMCDigitalPsychiatry/LAMP-server/pull/284 ; https://play.google.com/store/apps/details?id=digital.lamp.mindlamp&hl=en_US ; https://itunes.apple.com/lookup?id=1495947054 (JSON, no quote)
- **Quotes:** "2025.4.2 (509)" / "Zco: build baseline builds = current production app code, pointed at dev." / "zagaran/auth-refactor" / "1K+ Downloads"
- **Date:** issue comment 2026-08-28; read 2026-10-11
- **Source type:** repository; app_store
- **In KB:** no (in part). Profile lines 10 and 157 and matrix line 49 record the stale App Store build; the TestFlight build and contractors are new.

### 14. Funding and sustainability: Amazon Research Award, and an NIH data-standards grant now staffing the engineering team
- **Found:** BIDMC's AWS blog says the AI navigator work is supported in part by an Amazon Research Award. The current Software Engineer I posting for mindLAMP says the team works with NIH funding on smartphone and wearable data standards. NIH RePORTER (API, read 2026-10-11) shows that grant as 1RF1MH144469-01, "DIGITS: DIGital health Interoperability Technology Standards", PI John Torous, BIDMC, 2026-08-01 to 2030-07-31, FY2026 award $2,961,081; its abstract plans a consortium governance model funded by consortium fees and eventual stewardship by the APA. The abstract does not name mindLAMP. The posting also lists wearable integrations (Apple Health, Health Connect, cloud wearable services) and "audit-worthy logging" as next-year work.
- **URL:** https://aws.amazon.com/blogs/industries/from-cloud-to-clinic-how-aws-powers-digital-psychiatry-at-scale/ ; https://digitalpsych.org/jobs/software-engineer-i ; NIH RePORTER appl_id 11360541 (https://reporter.nih.gov/project-details/11360541, JavaScript page, not probeable; figures from the RePORTER API)
- **Quotes:** "This work is supported in part by an Amazon Research Award" / "Work with the engineering team with NIH funding to develop new data standards in smartphone and wearable data" / "helping design and build integrations for consumer health APIs (Apple Health, Health Connect, and cloud wearable services)"
- **Date:** blog 2026-09-29; posting read 2026-10-11; grant start 2026-08-01
- **Source type:** secondary (blog, RePORTER); vendor_page (job posting)
- **In KB:** no.

### 15. data_residency: BIDMC-hosted mindLAMP runs on AWS ECS Fargate with DocumentDB
- **Found:** BIDMC's AWS blog gives the hosted stack: ECS Fargate, DocumentDB as the primary data store, AWS Private CA for service-to-service TLS, Terraform and GitHub Actions OIDC. It does not state an AWS region. The draft privacy rewrite (PR #939) also says BIDMC-hosted deployments run on ECS.
- **URL:** https://aws.amazon.com/blogs/industries/from-cloud-to-clinic-how-aws-powers-digital-psychiatry-at-scale/
- **Quotes:** "Amazon DocumentDB : The primary data store for mindLAMP data"
- **Date:** 2026-09-29
- **Source type:** secondary
- **In KB:** no. The KB has the three Core deployment models (profile line 97) but not the stack. Region stays unknown.

## Searched, nothing found

- FDA: openFDA 510(k) search for device name "mindlamp" and applicant "Beth Israel Deaconess", and registration/listing for "mindlamp": no matches. EUDAMED and CE/MDR not searched beyond web search; no CE claim seen anywhere.
- SOC 2, ISO 27001, BAA, DPA: no certificate, trust portal or partner mention found. GDPR appears only as a topic in the AWS blog, not as a statement of compliance.
- Pricing: no fee schedule, academic rate or industry rate on research.bidmc.org/mindlamp/services, digitalpsych.org, the docs, job postings or the AWS blog.
- Integrators: no Fitabase, Labfront, Terra or Thryve connector for mindLAMP found.
- Press/newsroom: no BIDMC press release on mindLAMP in the last 12 months found; the AWS blog is the main external write-up.
- Recent papers on how researchers got the data: nothing new beyond the 2023 missingness analysis (1,178 participants), which the KB already has in `module-03-applied-studies/_across-the-board-scan-2026-09.md`.
- University of Colorado telehealth collaboration page mentions a planned mindLAMP integration with BIDMC, described as still being finalized; not quoted or verified.
- GitHub org (33 repos via API): no new archive or deprecation notices beyond LAMP-app, LAMP-portal and SAMHSA-PAWS; LAMP-r (R client) last pushed 2021-05-07, possibly dormant.
