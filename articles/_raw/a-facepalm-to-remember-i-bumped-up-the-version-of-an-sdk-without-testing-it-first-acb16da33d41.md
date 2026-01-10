---
title: 'A Facepalm to Remember: I bumped up the version of an SDK without testing
  it first.'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-16T06:08:31.000Z'
originalURL: https://freecodecamp.org/news/a-facepalm-to-remember-i-bumped-up-the-version-of-an-sdk-without-testing-it-first-acb16da33d41
coverImage: https://cdn-media-1.freecodecamp.org/images/1*-hj6FOiWHQDYIWJgCmbeZQ.jpeg
tags:
- name: Android
  slug: android
- name: android app development
  slug: android-app-development
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: startup
  slug: startup
seo_title: null
seo_desc: 'By Rahul Chowdhury

  It all started when Google made its App Shortcuts API available for developers on
  Android. I was super excited to add this to my hash tagging Android app, Magnify.
  So I started digging through their documentation for steps to imple...'
---

By Rahul Chowdhury

It all started when Google made its App Shortcuts API available for developers on Android. I was super excited to add this to my hash tagging Android app, [Magnify](https://play.google.com/store/apps/details?id=com.upcurve.magnify). So I started digging through [their documentation](https://developer.android.com/guide/topics/ui/shortcuts.html) for steps to implement it.

The first thing I noticed was the required API version for Android `targetSdkVersion` was higher than what I was using. “No big deal,” I thought. And I bumped it up to a newer version.

### The “Mistake”

Bumping up my SDK version wasn’t a mistake. The mistake was that I didn’t test the app extensively on the latest version of Android. I just added the shortcut feature, tested that out thoroughly, then pushed my changes — without realizing that a major API change had been made to this new version of the SDK.

Android Nougat enforces a check on the scope of files shared across apps in the system. If you try to share a file that is saved within the scope of your app with some external app using the traditional `file://` approach, your app will hit a `FileUriExposedException`, causing your app to bring up that ugly crash dialog that no developer — and certainly no user — wants to ever see.

How I fixed this exception is beyond the scope of this article. Instead let me share how this one silly mistake affected my app.

### The “Problem”

Before, when I targeted Android Marshmallow users, my app always managed to sneak out through that hidden door known as “compatibility mode” when running on Nougat. So I was totally chilled out knowing that my app ran fine on the latest version of the OS.

```
android {     defaultConfig {         minSdkVersion 18         targetSdkVersion 23 //Targeting Marshmallow    }}
```

But now things were slightly different for my poor little app. Since it said that it was targeting the latest version of Android, the OS assumed that it had been tested well for all new API updates, and should be punished for any violations. In my case, this was `FileUriExposedException`, as I was sharing photos using the traditional `file://` approach instead of upgrading to a safe and robust solution.

```
android {     defaultConfig {         minSdkVersion 18         targetSdkVersion 25 //Targeting Nougat 7.1    }}
```

The ultimate penalty? “_Unfortunately, Magnify has stopped working._”

### The “Bigger Problem”

Though the crash was a serious problem itself, I had yet to discover an even bigger problem. Since Android Nougat was only available to around 0.6% Android phone users at that time — and to around 2–3% of people using my app — this was a crash that could have been hidden for weeks.

Fortunately, one of my app users had a Google Pixel running Nougat, and it was she who brought to my attention that the app was broken. I patched it up and rolled out another update with the fix to this crash, which thankfully most users were unaware of, as I was notified of the issue within a day or two.

Phew! That was really really close.

### How did I solve it?

Yeah yeah, I said that I won’t be getting deep into solving the problem, but it’s kind of hard for me to watch a fellow developer struggle on the same problem I had, knowing that I could have helped and added some happy moments to their life.

Here’s how I did it:

[**file:// scheme is now not allowed to be attached with Intent on targetSdkVersion 24 (Android Nougat…**](https://inthecheesefactory.com/blog/how-to-share-access-to-file-with-fileprovider-on-android-nougat/en)  
[_Android Nougat is almost be publicly released. And as an Android developer, we need to prepare ourself to adjust…_inthecheesefactory.com](https://inthecheesefactory.com/blog/how-to-share-access-to-file-with-fileprovider-on-android-nougat/en)

### Moral of the story

Never ever — and I repeat never ever — roll out an update to your software without very, very extensive testing when you have bumped up the version of your SDK. Chances are there are some API changes you were unaware of — some of which might break your software for good.

Make sure you ship your updates only after proper testing. A little time spent testing can save a lot of time getting back the trust of your users.

Oh, and:

> There are no mistakes, save one: the failure to learn from a mistake. — Robert Fripp

Because you don’t end a dope article without a kickass quote. ? ✌️

If you enjoyed this story, please do recommend it to other people by hitting the ? button on this page, and follow me for more stories about programming.

