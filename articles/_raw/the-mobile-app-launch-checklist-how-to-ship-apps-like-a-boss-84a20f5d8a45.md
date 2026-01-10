---
title: The Mobile App Launch Checklist — How to Ship Apps Like a Boss
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-08T23:23:49.000Z'
originalURL: https://freecodecamp.org/news/the-mobile-app-launch-checklist-how-to-ship-apps-like-a-boss-84a20f5d8a45
coverImage: https://cdn-media-1.freecodecamp.org/images/1*19x5Ze6FU-bYSCsvUdzF2Q.png
tags:
- name: Android
  slug: android
- name: iOS
  slug: ios
- name: mobile app development
  slug: mobile-app-development
- name: Productivity
  slug: productivity
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Michal Bialas

  In this article, I would like to present a short guide on how to release mobile
  apps. I’ll emphasise the internal releases. I’m also not limiting myself to Android,
  as I believe this may apply to iOS as well.

  I split this article int...'
---

By Michal Bialas

In this article, I would like to present a short guide on how to release mobile apps. I’ll emphasise the internal releases. I’m also not limiting myself to Android, as I believe this may apply to iOS as well.

I split this article into some points just to increase readability. If you’d like to get to know more, please stay with me! I hope you will like it.

### **1 . Make sure all your tests pass** ✅

![Image](https://cdn-media-1.freecodecamp.org/images/oMvWjS8YhmpWSXhmyrwVOeb7PcG2gT9gTiag)

If you write end-to-end unit and integration tests, you should always take care to check their output. If they fail, make them work.

### **2. Perform a clean full build of your app** ✅

![Image](https://cdn-media-1.freecodecamp.org/images/WTgYEm7Lso7UbJX8l6z2-7ruJAUQDv4d-bCb)

If you obfuscate code on Android and use [**ProGuard**](https://stuff.mit.edu/afs/sipb/project/android/sdk/android-sdk-linux/tools/proguard/docs/index.html#manual/introduction.html), make sure it does not remove code which may lead the app to crash. You can read about code shrinking [here](https://developer.android.com/studio/build/shrink-code).

The full build can be performed on your local machine as well as using **Continuous Integration**.

If you or your company own a server, you can set-up your **CI** flow using [**Jenkins**](https://jenkins.io/) (which is free open source automation server). If not, you can easily use one of many CI services available on the market. I can recommend, for example, [**Bitrise**](https://app.bitrise.io/users/sign_up?referrer=6ee27e581bdc8285)**, [CircleCI](https://circleci.com/), [Travis](https://travis-ci.org/)** and [**Bitbucket Pipelines**](https://bitbucket.org/product/features/pipelines).

Travis is already integrated with Github, so I if you have a paid plan, it could be your choice. If you use Bitbucket, it is the same for Bitbucket Pipelines.  
[**Bitrise**](https://app.bitrise.io/users/sign_up?referrer=6ee27e581bdc8285) has many great integrations with services like Slack, Fabric, [XCode Archive](https://www.bitrise.io/integrations/steps/xcode-archive), [CocoaPods](https://cocoapods.org/), [Gradle Runner](https://www.bitrise.io/integrations/steps/gradle-runner), [Jira](https://pl.atlassian.com/software/jira) and many more. I wrote a short article about **CircleCI** some time ago, so if you are interested, you can check it out on [**my blog**](http://mmbs.github.io/tools/ci/2016/07/31/circleci-for-android-projects/).

### **3. Perform static code analysis** ✅

![Image](https://cdn-media-1.freecodecamp.org/images/rQ9hAVdxxBuUeNotoGJK2KIjetGv3ULNPz-R)

Make sure you use tools like:

* Lint (_for Java and Kotlin which is available by default in Android Studio ver. 3.1 and above_), [ktlint](https://github.com/shyiko/ktlint), pmd, checkstyle, findbugs, [detekt](https://github.com/arturbosch/detekt), [gradle-static-analysis-plugin](https://github.com/novoda/gradle-static-analysis-plugin) **for Android**
* [OCLint](http://oclint.org/), [tailor](https://github.com/sleekbyte/tailor), [SwiftLint](https://github.com/realm/SwiftLint), [Clang Static Analyzer](http://clang-analyzer.llvm.org/), [Infer](https://fbinfer.com/), [SwiftFormat](https://github.com/nicklockwood/SwiftFormat), [Swimat](https://github.com/Jintin/Swimat), [Faux Pas](http://fauxpasapp.com/) **for iOS**

Of course, use only the tools you find helpful to increase the quality of the project you are currently working on.

### **4. Prepare debug and production builds for internal needs** ✅

![Image](https://cdn-media-1.freecodecamp.org/images/aXzbdMWWClSnIPiaS0fQuZsiVBUnYikB2ksi)

Make sure you prepare a debug and production version of your app and release it internally for testing. You should also use crash reporting tools like [**Instabug’s crash reports**](https://instabug.com/crash-reporting) or [**Fabric**](https://get.fabric.io/) **(Crashlytics)**.

It is vital to check how your app works with a debug / staging API and then with production. For Android, it also important to obfuscate code and check if it is shrunk properly.

When releasing the version for your team, you can use [**TestFlight**](https://developer.apple.com/testflight/) for iOS and [**Google Play Test channel**](https://developer.android.com/distribute/best-practices/launch/test-tracks) for Android. You can also consider free tools like **Fabric** (which will be [shutdown in mid 2019](https://fabric.io/blog/the-future-of-fabric)) or [**Hockey App**](https://hockeyapp.net/#s) which is currently transitioning to [**App Center**](https://appcenter.ms/).

### **5. Automate** ✅

![Image](https://cdn-media-1.freecodecamp.org/images/hD6g7L5PJDEvC8sG7hJkltvIiIGE9RNbjTVy)

Preparing builds can be also automated. You’ve probably heard of [**fastlane**](https://fastlane.tools/). It is a free tool for automating screenshots, beta deployment, App Store / Google Play deployment and code signing. It is supported by all the CI and distribution services which I mentioned earlier.

![Image](https://cdn-media-1.freecodecamp.org/images/gpYGx-FA1FhJ-Lk6jRtECZOYN4iEQTUJlKtt)

The configuration for [Android](https://docs.fastlane.tools/getting-started/android/setup/) and for [iOS](https://docs.fastlane.tools/getting-started/ios/setup/) is quite straightforward but is possible only if you have macOS. Unfortunately there is [no non-macOS platform support](https://github.com/fastlane/fastlane/issues/11687) at this moment. This is painful for Android developers who code on Linux and Windows. But there is a solution! ???

![Image](https://cdn-media-1.freecodecamp.org/images/82tqd9S1PXAXrNFhQT8b9uNlCZSiU7B4trNT)

[**Gradle Play Publisher**](https://github.com/Triple-T/gradle-play-publisher) is a Gradle plugin that automates uploading an App Bundle or APK and other app details to the Google Play Store. And it is a great alternative to Fastlane. I used it quite some time ago, it works really well and I can recommend it. [The documentation](https://github.com/Triple-T/gradle-play-publisher/blob/master/README.md) is comprehensive and it allows you to smooth out configuration of the tool.

### **6. Know and listen to your users** ✅

![Image](https://cdn-media-1.freecodecamp.org/images/eZ1SkkFnARgSIoHKlcnlIQSNsCKYu4bc8dBR)

So you checked your code, set up tools for an automation, prepared a fully operational and tested build and released it to your team for testing. But how many times have you felt like no one cares or does not have time to give you feedback? I know from experience that it is really hard to engage the team to check and play with your newly released app.

The answer for this is [**Instabug**](https://instabug.com/). I did a lot of research about tools which help to gather feedback, bugs, reports etc almost 3 years ago, and since then I have stuck to Instabug.

![Image](https://cdn-media-1.freecodecamp.org/images/l8tko24ko7ifXOJkv7nbYitOPvSOrAuCVoNW)

It is really easy to integrate with any of your apps (it supports Android, iOS, React Native, Xamarin, Unity, Cordova) — it is just a few lines of code.

How you can use this tool:

* Your users can just shake the phone and [write feedback with already taken screenshots](https://instabug.com/bug-reporting). They can even draw or record a movie, what is missing or how to reproduce a bug. It is super helpful.
* Instead of contacting developers via contact forms, end-users can [ask about features or give feedback using In-App Chat](https://instabug.com/in-app-chat). This helps a lot in connecting with the users all the time.  
Also, developers can easily reply back to users who reported bug reports or crashes to get more context from them or thank them or even tell them that the bug/crash was fixed, and they can update an app to the latest version.
* Use [In-App Feature Requests](https://instabug.com/feature-requests) and support your backlog by user-driven prioritising. Thanks to this feature the team and the product owner will know which feature to release first.

### **7. Monitor the engagement** ✅

![Image](https://cdn-media-1.freecodecamp.org/images/g9HjIh0lKL55vSryvS5rFTpHats3OEIDJcbC)

The app is in production, but you have this feeling that people do not use your app. What to do then?

You can integrate tools like **Google Analytics**, **Fabric**, [**Amazon Pinpoint**](https://aws.amazon.com/pinpoint/), [**Mixpanel**](https://mixpanel.com/) or [**Segment.io**](http://segment.io) to check:

* active users,
* session intervals,
* time in the app,
* screen flow,
* retention,
* conversion,
* life time value.

Checking these KPIs is also vital when releasing new app features to production. Do not underestimate them. ?

I believe this is it. I hope you enjoyed the checklist. If you have any insight or other tools which may help with application release, please let me know in the comments. You can also check out my other articles:

* [Lucky 7 new tools and plugins for Android developers & designers](https://proandroiddev.com/lucky-7-new-tools-and-plugins-for-android-developers-designers-1545e5c59f27)
* [25 new Android libraries and projects to check at the beginning of 2018](https://proandroiddev.com/25-new-android-libraries-and-projects-to-check-at-the-beginning-of-2018-ba3b422bbbb4)
* [Terminal on steroids](https://medium.com/@mmbialas/terminal-on-steroids-bbf88f3dcbdb)

If you like my article, please don’t forget to click ??? to recommend it to others ???.

Also, to be notified about my new articles and stories, follow me on [Medium](https://medium.com/@mmbialas) and [Twitter](https://twitter.com/mmbialas). You can find me on [LinkedIn](https://www.linkedin.com/in/mmbialas) as well. Cheers!

