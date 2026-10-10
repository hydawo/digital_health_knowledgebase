# Android and iOS background limits for passive sensing

**Last verified: 2026-10-09.** Written to close unresolved question 108. Every Module 2 platform and
every phone-based Module 3 deployment sits on top of these rules, so completeness figures from
studies run before about 2022 carry operating-system assumptions that no longer hold.

## Summary

- Since 2018 both systems moved from "background apps run unless killed" to "background work needs
  an explicit, permission-gated, OS-scheduled route". **Verified.**
- **Android** changed in a fixed sequence: Android 9 stopped sensor events to background apps;
  10 and 11 split out background location; 12 blocked foreground-service starts from the
  background; 13 added the restricted bucket after 8 days unused; 14 made foreground-service types
  mandatory and denied exact alarms by default; 15 capped dataSync services at 6 hours; 16 replaced
  BODY_SENSORS with Health Connect permissions and applied job quotas even alongside a foreground
  service. **Verified.**
- **iOS** changed less. Background tasks, app refresh and silent pushes have never had guaranteed
  timing; Apple says silent pushes are throttled and should not exceed "two or three per hour".
  iOS 13 added BGTaskScheduler, iOS 17 added BGHealthResearchTask for apps in a health research
  study, iOS 26 added BGContinuedProcessingTask. **Verified.**
- In practice: continuous passive sensing on Android needs a typed foreground service, started
  while the app is visible, with the matching permission. On iOS it needs Always location as the
  keep-alive, and a participant who force-quits the app stops collection until they reopen it.
- iOS keeps short on-device histories (7 days of motion activity and steps, 3 days of raw
  accelerometer via CMSensorRecorder), so an app that wakes late can backfill. **Verified.**
- **Not documented anywhere:** Android OEM battery managers (Samsung, Xiaomi, Huawei and others)
  and Apple's scheduling heuristics. These need device testing. **Unclear.**

## Rule table

| Stream or mechanism | Android rule (version) | iOS rule | Practical effect on a research app |
|---|---|---|---|
| Accelerometer and gyroscope in background | Android 9: background apps get no continuous, on-change or one-shot sensor events, so a foreground service is required. Android 12: motion-sensor rate cap for apps targeting 12 (the 200 Hz figure without HIGH_SAMPLING_RATE_SENSORS is **Reported**) | No continuous background sampling unless the app stays awake, usually through location. CMSensorRecorder (iOS 9+) records 50 Hz while the app is suspended or terminated, kept 3 days. Motion permission required | Android needs a persistent notification and a foreground service. iOS can backfill raw accelerometer data if the app wakes within 3 days |
| Foreground-service start and type | Android 8: background service limits. Android 12 (target 31+): no start from background except listed cases (high-priority FCM, exact alarm, boot, activity-recognition or geofence transition, battery optimisation disabled by the user). Android 14: type mandatory; "location" needs location permission, "health" needs ACTIVITY_RECOGNITION, BODY_SENSORS or health permissions; location, health or microphone services started from background throw SecurityException without the background permission. Android 15: dataSync and mediaProcessing limited to 6 h per 24 h; BOOT_COMPLETED cannot start dataSync, camera or microphone services | Not applicable. Nearest equivalent is a background mode (location, audio, Bluetooth LE) | Upload loops built on dataSync die after 6 h on Android 15+. Use a location or health service type, or WorkManager. Restart after reboot must use an allowed type |
| Location in background | Android 8: background updates "only a few times each hour". Android 10: ACCESS_BACKGROUND_LOCATION. Android 11: "Allow all the time" moved to a settings page. Android 12: users can grant approximate only. Background location exempts the app from the restricted bucket | Always authorization plus the Location updates background mode. Significant-change updates relaunch a terminated app, roughly every 500 m and at most once every 5 min. CLBackgroundActivitySession (iOS 17+) must be created in the foreground. iOS 14+ allows approximate-only grants | GPS is the most fragile stream to enrol: a two-step grant on both systems, and approximate location degrades mobility features. On iOS, location is also the keep-alive for every other stream |
| Activity recognition, steps, motion history | Android 10: ACTIVITY_RECOGNITION runtime permission. Transition events are an allowed foreground-service start trigger | CMMotionActivityManager and CMPedometer keep 7 days of history | iOS can backfill step and activity labels up to 7 days after a gap. Android needs live collection or Health Connect |
| Exact alarms (EMA scheduling) | Android 12: SCHEDULE_EXACT_ALARM. Android 14: denied by default on new installs (target 33+). USE_EXACT_ALARM is only for calendar and alarm-clock apps | Local notifications with calendar or time triggers, delivered by the OS. Cap of 64 pending requests (**Corroborated**, older Apple guides). Time Sensitive level (iOS 15+) breaks through Focus and Notification Summary, but the user can turn it off | Android EMA apps must ask for "Alarms & reminders" or accept inexact timing. On iOS, Focus and Summary can hide prompts unless they are Time Sensitive |
| Notifications and push wake-ups | Android 13: POST_NOTIFICATIONS runtime permission. High-priority FCM can be deprioritised if no visible notification follows | Silent pushes are low priority, not guaranteed, throttled (two or three per hour), and discarded after a force-quit. Each wake gets 30 s | Server keep-alives such as Beiwe's heartbeat work better as visible notifications than silent ones |
| Jobs and standby buckets | Android 9: App Standby buckets. Restricted bucket after 8 days unused on Android 13 (45 days on 12): jobs once a day in a 10-minute batch, 1 alarm a day. Android 16: job runtime quota applies even alongside a foreground service | BGAppRefreshTask and BGProcessingTask (iOS 13+) run when the system decides. setMinimumBackgroundFetchInterval deprecated in iOS 13. BGHealthResearchTask (iOS 17+) gives processing time to health research apps; whether it needs an entitlement is **Unclear** | Low-interaction passive studies drift into the restricted bucket on Android. iOS uploads land at OS-chosen times, often overnight while charging |
| Health data (wearables) | Health Connect built into Android 14+. 30 days of history before first grant unless READ_HEALTH_DATA_HISTORY is granted; background reads need READ_HEALTH_DATA_IN_BACKGROUND. Android 16: BODY_SENSORS replaced by android.permissions.health.*, and a privacy-policy activity is required or the permission is revoked | HealthKit. Background-delivery details not re-checked in this pass | Android studies can pull wearable history after enrolment, 30 days by default |
| Calls, SMS, app usage | Android 9: call-log permission group. Google Play SMS and Call Log policy from January 2019 (**Corroborated**; the change that cut RADAR-MDD's text and call data mid-study). App usage needs PACKAGE_USAGE_STATS special access | No public API for SMS, app usage or keyboard. Calls only through CXCallObserver while the app runs: events with no history and no numbers | Android-only by design, and policy-gated on Play-distributed builds |
| Permission decay | Android 11: permissions of unused apps reset automatically. Android 12: hibernation after "a few months" | Periodic reminder prompts for background location (**Corroborated**) | Long studies lose grants silently on Android. Plan re-consent checks |

## Sources

All accessed 2026-10-09.

**Android developer documentation**

1. Android 9 behaviour changes. https://developer.android.com/about/versions/pie/android-9.0-changes-all
2. Android 12 behaviour changes. https://developer.android.com/about/versions/12/behavior-changes-12
3. Android 15 behaviour changes. https://developer.android.com/about/versions/15/behavior-changes-15
4. Android 16 behaviour changes, all apps. https://developer.android.com/about/versions/16/behavior-changes-all
5. Android 16 behaviour changes, apps targeting 16. https://developer.android.com/about/versions/16/behavior-changes-16
6. Foreground service types. https://developer.android.com/develop/background-work/services/fgs/service-types
7. Restrictions on starting a foreground service from the background. https://developer.android.com/develop/background-work/services/fgs/restrictions-bg-start
8. Exact alarms denied by default (Android 14). https://developer.android.com/about/versions/14/changes/schedule-exact-alarms
9. App Standby buckets. https://developer.android.com/topic/performance/appstandby
10. Background location limits (Android 8). https://developer.android.com/about/versions/oreo/background-location-limits
11. Background location permission. https://developer.android.com/develop/sensors-and-location/location/permissions/background
12. Health Connect, reading data. https://developer.android.com/health-and-fitness/guides/health-connect/develop/read-data

**Apple developer documentation** (read through the JSON endpoints under
`developer.apple.com/tutorials/data/documentation/`, because the normal pages need JavaScript)

13. CMSensorRecorder and recordAccelerometer(forDuration:)
14. CMMotionActivityManager queryActivityStarting; CMPedometer queryPedometerData
15. BGTaskScheduler; BGContinuedProcessingTask; BGHealthResearchTask
16. Choosing background strategies for your app
17. startMonitoringSignificantLocationChanges; Handling location updates in the background
18. Pushing background updates to your app
19. UNNotificationInterruptionLevel.timeSensitive; setMinimumBackgroundFetchInterval (deprecated)
