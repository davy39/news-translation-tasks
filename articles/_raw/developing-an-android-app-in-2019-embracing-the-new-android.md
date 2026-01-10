---
title: 'How to develop an Android App: embracing the ‘new’ Android'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-17T04:19:46.000Z'
originalURL: https://freecodecamp.org/news/developing-an-android-app-in-2019-embracing-the-new-android
coverImage: https://cdn-media-1.freecodecamp.org/images/1*kJIHafbx3Dzn6xWlVWDknA.png
tags:
- name: Android
  slug: android
- name: Kotlin
  slug: kotlin
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Aakarshit Uppal

  or how the Bitotsav ’19 app became a reality

  Background: Pantheon ’17 ⏪

  Almost two years ago, in September 2017, a friend, Ashank Anshuman convinced me
  to work on an app for the technical fest of our institute. We worked for about ...'
---

By Aakarshit Uppal

#### *or how the Bitotsav ’19 app became a reality*

### *Background: Pantheon ’17 ⏪*

Almost two years ago, in September 2017, a friend, Ashank Anshuman convinced me to work on an app for the technical fest of our institute. We worked for about two weeks, day and night, getting it ready for release just in time for the fest. Although we were exhausted, it was an amazing feeling, getting something ‘out there’, in production, that people actually used! It served its purpose perfectly well, helping the organizers easily convey everything to the participants.

> [**Pantheon '17 - Apps on Google Play**](https://play.google.com/store/apps/details?id=in.pantheon17)  
> [\_In its endeavor to provide a national platform for the youth to showcase their technical skills; displaying…\_play.google.com](https://play.google.com/store/apps/details?id=in.pantheon17)

It was rated 4.9 with around 120 reviews, which Google’s bots removed for some reason, but that’s a story for another time. We received some requests to share the source of the app, but we declined, due to many reasons — but mostly because we weren’t that satisfied with the code, especially the parts rushed through near the end. We simply didn’t have enough time and experience to write code good enough for people to learn from and/or use.

### Here We Go Again! ?

Fast forward to November 2018: Ankit Agrawal (he’s that ‘fest guy’) asks me to join the team for Bitotsav, our annual socio-cultural fest, to which I agree, as I was looking for some excuse to revisit Android. This time I convinced Ashank (took a lot of convincing!) to work on the app.

We didn’t do much in December, but I did start reading on things like Architecture Components, AndroidX, Jetpack etc. I had also been getting familiar with Kotlin over the past few months, with a couple courses being instrumental: A two-part course by the one and only [Hadi Hariri](https://twitter.com/hhariri) and another more recent one by Svetlana Isakova and Andrey Breslav (which he introduced in KotlinConf 2018). Kotlin was thus the obvious choice for the app.

> [**Introduction to Kotlin Programming**](http://shop.oreilly.com/product/0636920052982.do)  
> [\_Kotlin 1.0 was released in February 2016, and since that time it's been embraced by developers around the world…\_shop.oreilly.com](http://shop.oreilly.com/product/0636920052982.do)

> [**Kotlin for Java Developers | Coursera**](https://www.coursera.org/learn/kotlin-for-java-developers)  
> [\_Kotlin for Java Developers from JetBrains. The Kotlin programming language is a modern language that gives you more…\_www.coursera.org](https://www.coursera.org/learn/kotlin-for-java-developers)

### **Decisions ?**

The first half of January also went by with not much code being written, as I was preoccupied and couldn’t reach the college till 16th Jan. We did, however, make some major decisions:

* **Use** [**Kotlin**](https://developer.android.com/kotlin) **exclusively**
    
* **Use** [**Feature-based packaging**](https://hackernoon.com/package-by-features-not-layers-2d076df1964d)
    
* **Use** [**Jetpack**](https://developer.android.com/jetpack) [**Architecture Components**](https://developer.android.com/topic/libraries/architecture/) **with** [**AndroidX**](https://developer.android.com/jetpack/androidx/releases)
    
* **Use** [**API 21 as Min API**](https://developer.android.com/about/dashboards/) *(22 might’ve been a better choice)*
    
* **Use** [**Android Studio Canary**](https://developer.android.com/studio/preview)
    
* Use [Git Flow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) & [SemVer](https://semver.org/)
    
* Write code good enough to make it public after the fest ?
    

![Image](https://cdn-media-1.freecodecamp.org/images/G3zLWh-8mSzeAdIsNmP5YL6ahsna4m2mqm8o align="left")

*Jetpack with AndroidX*

So basically, a hard reset from all the experience of developing an app in 2017 to the bleeding edge in 2019. It was really exciting, but also a big challenge.

### Code Code Code! ?

We decided that Ashank would take care of the Backend of the app (DB & Networking, Notifications with FCM, Background Processing) and I’d take care of the Frontend and Integration, just like we did for Pantheon ’17. Many resources came in handy while getting started and as we worked, but the best by far were these awesome codelabs offered by Google:

* [Room with a View - Kotlin](https://codelabs.developers.google.com/codelabs/android-room-with-a-view-kotlin) (ViewModel, LiveData & Room with Coroutines)
    
* [Using Kotlin Coroutines in your Android App](https://codelabs.developers.google.com/codelabs/kotlin-coroutines)
    
* [Data Binding Codelab](https://codelabs.developers.google.com/codelabs/android-databinding)
    
* [Navigation Codelab](https://codelabs.developers.google.com/codelabs/android-navigation): (Navigation Architecture Component)
    
* [Background Work with WorkManager](https://codelabs.developers.google.com/codelabs/android-workmanager/#0)
    

> [**Google Codelabs**](https://codelabs.developers.google.com/?cat=Android)  
> [\_Google Developers Codelabs provide a guided, tutorial, hands-on coding experience. Most codelabs will step you through…\_codelabs.developers.google.com](https://codelabs.developers.google.com/?cat=Android)

Also, the [Sunflower](https://github.com/googlesamples/android-sunflower) & [Google IO 18](https://github.com/google/iosched) apps by Google were ideal codebases for the purpose of reference. [Android Dev Summit app](https://github.com/google/iosched/tree/adssched) would also have been a good source for reference, had I known about it before!

> [**googlesamples/android-sunflower**](https://github.com/googlesamples/android-sunflower)  
> [\_A gardening app illustrating Android development best practices with Android Jetpack. - googlesamples/android-sunflower\_github.com](https://github.com/googlesamples/android-sunflower)

With these in our arsenal, we began coding. I decided to use the new [**Navigation architecture component**](https://developer.android.com/topic/libraries/architecture/navigation) **to implement a** [**single-Activity app architecture**](https://www.youtube.com/watch?v=2k8x8V77CrU). Ashank started with Room and FCM. I had also been thinking about using [**Koin**](https://insert-koin.io/) **for IoC**, but wasn’t so sure.

Incidentally, Joe Birch launched a Koin course right around that time on [caster.io](https://caster.io) (Features small, to the point courses by professionals, each free for a week on launch!), and decided to go with it. No regrets there! Seriously, the android support is amazing and the [documentation](https://beta.insert-koin.io/docs/2.0/documentation/reference/index.html#_koin_for_android_developers) is fabulous ❤️

> [**Koin**](https://caster.io/courses/koin)  
> [\_In this course, we'll be learning about a dependency injection framework known as Koin by building a fully functional…\_caster.io](https://caster.io/courses/koin)

With Navigation and Koin setup, I began with the UI, deciding was to **use material design components** exclusively for UI for which the [**guidelines**](https://material.io/design/components/) **and** [**docs**](https://material.io/develop/android/components/bottom-app-bar/) came in handy. Also, I *had* to **use** [**Data Binding**](https://developer.android.com/topic/libraries/data-binding) because I love it! Meanwhile Ashank implemented [WorkManager](https://developer.android.com/topic/libraries/architecture/workmanager), which we decided to **use instead of Firebase Job Dispatcher**, going full Jetpack!

The first thing I developed was the Schedule UI, which helped me get comfortable with Architecture Components. With that done, I moved on to the Registration-flow UI, probably the most complex part of the app, which featured advanced usage of LiveData and Navigation for implementing three steps with live-validated forms (Worth a blog post of its own, coming soon?!). This made me a lot more confident in these components, and it was a smooth ride from there on. We completed the planned features, discovered some gotchas, fixed some bugs.

### Launch ?

With major features implemented, we did some UI brush-ups, completed some final TODOs, and were ready for launch! As a finishing touch, I added something I had been planning for all along:

A different color theme on every configuration change! This was done to compliment the theme of the fest: “*Colours of Asia”*

The app was live on the Play Store on Feb 11, 2019! ??

> [**Bitotsav '19 - Apps on Google Play**](https://play.google.com/store/apps/details?id=in.bitotsav)  
> [\_Bitotsav '19 the 29th edition of Birla Institute of Technology, Mesra's annual socio-cultural fest is all set to take…\_play.google.com](https://play.google.com/store/apps/details?id=in.bitotsav)

![Image](https://cdn-media-1.freecodecamp.org/images/r2U-QsAbLp7bc-Z69tXP9dNi1OyqTxZzKt24 align="left")

*Bitotsav ’19 App*

#### Fixes & Updates

We faced (the only!) two bugs within hours, which we fixed right away. The first one was related to DAO methods being marked `suspend`, but I’m still not a 100% sure why exactly it was happening ?. The second one was caused by obfuscation causing a serialization failure, and was easily fixed with a K\_eep a\_nnotation.

Then I started working on the next update, in which I added the leaderboard in the feed and the night events for the fest in the schedule, along with some other changes. A third update followed adding some more minor features.

**The fest went well, and the app was used by over 1000 participants!**

We did face a minor issue due to an incorrect DB entry in the servers by our friend Sushant Gupta, who later proceeded to write a rather dramatic blog post on the same.

> [**DDoS Attack on Bitotsav '19 Website**](https://cs.sonudoo.com/2019/02/ddos-attack-on-bitotsav-19-website.html)  
> [\_This is not a technical write up. This is a story that I want to share which might be a lesson for several Web & App…\_cs.sonudoo.com](https://cs.sonudoo.com/2019/02/ddos-attack-on-bitotsav-19-website.html)

After the fest, we released a final update, storing the event details, feed etc. as JSONs as part of the app and redacting the contact numbers of the organizers for privacy reasons.

#### Going Public!

It was time to open source the code! This time around, we had taken care to write understandable code, and it was ready for the world. I prepared a slick README, and to remove the contact numbers from the history of the repository, we used the amazing [BFG Repo Cleaner](https://rtyley.github.io/bfg-repo-cleaner) tool.

The code for the Bitotsav ’19 app is now public, for anyone to review, refer to, learn from or use! Check it out and don’t forget to leave a ? ?

> [**aksh1618/Bitotsav-19**](https://github.com/aksh1618/Bitotsav-19)  
> [\_Official app for Bitotsav '19. Contribute to aksh1618/Bitotsav-19 development by creating an account on GitHub.\_github.com](https://github.com/aksh1618/Bitotsav-19)

### Challenges ?

We did face some challenges during the development:

* **Time Limitations:** The main challenge we faced was of having a very limited time to learn very new concepts and use them to create an app to be used by hundreds. This time constraint led to a lot of continuous hours being put in, leading to stress and fatigue, but we were able to power through and deliver!
    
* **WorkManager with Coroutines:** On the technical side of things, we faced some minor challenges with WorkManager and Coroutines, but were able to overcome them. Hoping for a better support for coroutines throughout the Android SDK as development continues ?.
    
* **API 21:** We chose min API 21 to avoid having to adapt everything to work on older versions, as most android devices are on API 21 and above anyway. But surprisingly, [some things](https://stackoverflow.com/a/29756195/6346531) refused to work on API 21, especially view backgrounds. It was really frustrating, making me wish we had set min API as 22, even more so when we found out that the app had been installed only on two API 21 devices: the ones we had tested on ?.
    
* **Lack of Devices:** Another challenge we faced was not having enough devices to test on. During Pantheon ’17, we had a hostel with ~200 people, and thus testing was easy. This time around most people were gone for internships, so we were left with relying on having confidence in the code!
    
* **No code reviewers:** A lot of what we used was new to us, and we did our best to ensure we were doing everything right. But having a reviewer would have been very helpful. Even now, if you feel like you could do a quick review of the app’s code, we’d be very thankful!
    
* **The Apocalypse:** We did also face that ‘ *DDoS* ’ issue, read Sushant’s blog post linked above, you won’t regret it!
    

### Takeaways ✅

* **Kotlin + Jetpack = ❤️ :** The main takeaway was that Android Development has come a long way and with Kotlin and Jetpack, it’s definitely a lot more fun and purely joyful! Seriously, there were multiple *orgasmic* moments during the coding process!
    
* **Nothing is Impossible:** Kinda cliché but true: if you have the will to work hard, you can do anything, no matter how difficult. Sure, there will be stressful phases, but keep powering through. Just believe in yourself!
    

### Regrets ?

* **No Instant App / App Bundles**: We just straight up missed this one. Didn’t even think about it. Ah well, maybe next time.
    
* **No tests**: I know, this is a big one! Having proper tests in place could have helped us a lot, but due to the time constraints, we decided not to write tests until a ‘later’ time, which hasn’t yet come ?.
    

### TL;DR. ?

Starting with an app with 2019?

#### Use Kotlin & Coroutines

* [Learn](http://shop.oreilly.com/product/0636920052982.do) Kotlin and [use it](https://codelabs.developers.google.com/codelabs/taking-advantage-of-kotlin) exclusively!
    
* [Learn to use](https://codelabs.developers.google.com/codelabs/kotlin-coroutines) coroutines with Android.
    

#### Use Jetpack Components with AndroidX

* [Learn to use](https://codelabs.developers.google.com/codelabs/android-navigation) Navigation Component for Single-Activity Architecture.
    
* [Learn to use](https://codelabs.developers.google.com/codelabs/android-room-with-a-view-kotlin) Lifecycle Components for UI & Room for persistence.
    
* Do yourself a favor and [use](https://codelabs.developers.google.com/codelabs/android-databinding) Data Binding!
    
* [Learn to use](https://codelabs.developers.google.com/codelabs/android-workmanager/#0) WorkManager for background processing.
    

#### Use Material Components

* [Material Components Guidelines](https://material.io/design/components/)
    
* [Material Components Android Docs](https://material.io/develop/android/components/bottom-app-bar/)
    

#### Write Tests!

Well we couldn’t but you definitely should! Do NOT skip tests.

#### Refer to Source Code

.. of apps that do these things: [Sunflower App](https://github.com/googlesamples/android-sunflower), [IO App](https://github.com/google/iosched), [Dev Summit App](https://github.com/google/iosched/tree/adssched) or, of course, the [Bitotsav ‘19 App](https://github.com/aksh1618/Bitotsav-19)! (also, leave a star ?)

#### Stay up to date

Subscribe to blogs and newsletters to stay up to date! Here are some to start with: [Android Weekly,](https://androidweekly.net/) [ProAndroidDev](https://proandroiddev.com), [AndroidPub,](https://android.jlelse.eu) [Kotlin Weekly](http://www.kotlinweekly.net/). Overwhelmed? Check out this awesome talk by [Huyen Tue Dao](https://www.freecodecamp.org/news/developing-an-android-app-in-2019-embracing-the-new-android/undefined):

> [**Be Like Water: Keeping up with Android**](https://academy.realm.io/posts/360-andev-2017-keynote-huyen-tue-keeping-up-with-android)  
> [\_If you enjoy talks from 360 AnDev, please support the conference via Patreon! The one constant of working in mobile is…\_academy.realm.io](https://academy.realm.io/posts/360-andev-2017-keynote-huyen-tue-keeping-up-with-android)

Well, there we go. This is a great time for Android Development, so go get started with your new app, and don’t forget to have fun while doing it!

If you learned something, leave a comment. Constructive criticism welcome ?

Catch me on [Twitter](https://twitter.com/aksh1618) ? , [LinkedIn](https://www.linkedin.com/in/aakarshit-uppal/?lipi=urn%3Ali%3Apage%3Ad_flagship3_feed%3BdcfpLfCgSPiW0Cox1OEGIQ%3D%3D&licu=urn%3Ali%3Acontrol%3Ad_flagship3_feed-identity_welcome_message) ? or [GitHub ?](https://github.com/aksh1618)?

Until next time ??
