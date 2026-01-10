---
title: How to improve the build speed of your Android projects
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-17T15:53:54.000Z'
originalURL: https://freecodecamp.org/news/how-to-improve-the-build-speed-of-your-android-projects-bd49029d8602
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ePDs8qm8U0AHF6chIqHvnA.jpeg
tags:
- name: Android
  slug: android
- name: Java
  slug: java
- name: Kotlin
  slug: kotlin
- name: Productivity
  slug: productivity
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: "By Prateek Phoenix\nRecently, I undertook the task of migrating the Android\
  \ codebase at Kure to AndroidX. It seemed like the perfect opportunity to try and\
  \ fix the build speeds of the project. \nGradle has always had a bad rep for being\
  \ slow and resour..."
---

By Prateek Phoenix

Recently, I undertook the task of migrating the Android codebase at [Kure](http://kureapp.com) to AndroidX. It seemed like the perfect opportunity to try and fix the build speeds of the project. 

Gradle has always had a bad rep for being slow and resource intensive, but I was quite surprised at how minor changes to the project’s build configuration could massively improve the build speeds.

To give you a sneak peek of the time I was able to shed from our clean builds, here’s a before and after metric from the build scan.

![Image](https://cdn-media-1.freecodecamp.org/images/0-6xszNVvl-pP-OilKYuyq7jcTByO52w3E1D)
_pre-optimisation ??_

![Image](https://cdn-media-1.freecodecamp.org/images/KcwLYxol8gNXG3VRm59SAEukx0-nGvnLoQdt)
_post-optimization ⚡️⚡️_

Going down from 5.5 minutes to **17 seconds?? That’s bonkers.**

It’s easy to go overboard with optimizations that you can perform to bring down your build time even further. But I am going to intentionally focus on the minor, painless measures I took to come close to this metric for the sake of keeping this post beginner friendly.

### But first!

Before starting off with the optimization, it’s important to benchmark our project to see how long it currently takes to build. Gradle has a handy scan option that you can use to analyze the performance of your task. Fire up the terminal on Android Studio and execute the following command:

```
./gradlew assembleDebug --scan
```

Once the build completes successfully, it will prompt you to accept the terms of service to upload your build scan results. Type **yes** to proceed. Once it’s done publishing, you will get a link on the terminal to check your build scan. Open the link.

> There are quite a few options on the site, but for the sake of brevity, we’re only gonna take a look at what’s most important.

The summary view shows you a summary of the tasks that were run and how long it took for them to complete. But what we’re interested in here is the **Performance** section. It gives you a more detailed breakdown of the total build time as shown below.

![Image](https://cdn-media-1.freecodecamp.org/images/fQSMqur3f98DHDkLjr77fxG-DSJ3l46R-rwB)

Under the performance section, there’s a **Settings and suggestions** tab that gives you suggestions on how you can improve your build speeds. Let’s check that out.

![Image](https://cdn-media-1.freecodecamp.org/images/BPzUZVTnbe25aKNYE8csrTw37-PcaAF2STIb)

We can find some easy fixes for our build speed in this section. So let’s go ahead and apply these suggestions in our project.

### Step #1: Update your tooling

The Android team is constantly improving and evolving the Android build system. So most of the time you can receive significant improvements just by adopting the latest version of the tooling.

At the time of this refactor, our project was on **version 3.2.1** of the Gradle plugin for Android Studio _(which is a few versions older than the latest release)._

You can visit [**this link**](https://developer.android.com/studio/releases/gradle-plugin) to get the version for the latest release of the Gradle Plugin.

At the time of writing this post, the latest version happens to be **version 3.4.0.**

But it comes with a gotcha that we need to keep in mind for later:

![Image](https://cdn-media-1.freecodecamp.org/images/paGQGAiNaEorLPkxz9cyOLkXMs4XqWSXB8y8)
_[https://developer.android.com/studio/releases/gradle-plugin](https://developer.android.com/studio/releases/gradle-plugin" rel="noopener" target="_blank" title=")_

> When using **Gradle 5.0 and above** we will need to explicitly increase the heap size to ensure our build speed doesn’t worsen. We will come back to this in just a minute.

Open the top level **build.gradle** file which you will find in the root of your project and add the following line in the **dependencies section:**

```
classpath 'com.android.tools.build:gradle:3.4.0'
```

You will also need to update the **distribution URL** in the gradle wrapper properties file located at **_gradle/wrapper/gradle-wrapper.properties._** Update the URL to the following.

_(This link will be available on the [Android Gradle plugin release page](https://developer.android.com/studio/releases/gradle-plugin).)_

```
distributionUrl=https\://services.gradle.org/distributions/gradle-5.1.1-all.zip
```

If you are using Kotlin in your project, you will run into an error if your Kotlin Gradle plugin’s version is less than **1.3.0**. If that’s the case, use the IDE’s prompt to update your Kotlin Gradle plugin to the latest version _(which at the time of writing this post happens to be **version 1.3.31**)._

Alright, let’s run the build again from the terminal to see if we achieved any improvements.

![Image](https://cdn-media-1.freecodecamp.org/images/1VQvb91yf-nxNMXSNH6J6efMBvjoyzzMLnn4)

### Step #2: Update your configurations

So we were able to shed around 2.5 minutes from the build time but it’s still not good enough. Upon investigating the build logs in the terminal, I came across one line which is of interest to us:

![Image](https://cdn-media-1.freecodecamp.org/images/3UtgIeJxNxWUfqwQ-aswTFqEJQpJ8kx-g8zc)

Incremental compilation basically prevents wasteful compilation of the entire set of source files and instead compiles only the files that have changed. Looking at the logs, it’s clear that we’re not taking advantage of this feature. It suggests us to use **_android.enableSeparateAnnotationProcessing=true_** but since we’re using Kotlin in our projects, we should not be using the _‘annotationProcessor’_ configuration anyways.

Luckily, Kotlin **version 1.3.30** added the support for incremental annotation processing.

![Image](https://cdn-media-1.freecodecamp.org/images/ACEJQNcm29SbUFkkGGHdpZymgkA6-Dj911oR)
_[https://kotlinlang.org/docs/reference/kapt.html](https://kotlinlang.org/docs/reference/kapt.html" rel="noopener" target="_blank" title=")_

So let’s

1. Change the **annotationProcessor** configuration to **kapt**
2. Enable the **incremental annotation processing** experimental flag

Open your module level **_build.gradle_** file and add the following line to the top of the file:

```
apply plugin: 'kotlin-kapt'
```

Next, change all annotationProcessor configurations in the dependencies section to use kapt. Here’s an example:

```
//Before
annotationProcessor 'com.google.dagger:dagger-compiler:2.9'

//After
kapt 'com.google.dagger:dagger-compiler:2.9'
```

Now open up your **_gradle.properties_** file located at the root of your project and add the following line:

```
kapt.incremental.apt=true
```

Let’s run the build again. ??????

![Image](https://cdn-media-1.freecodecamp.org/images/-Bm0-tgHPB7Q5i4VGVbhkMlk1u432-qP4VEL)

Alright, looks like we’re getting there.

### Step #3: Gradle Properties

We’re in the last stage now. Remember the gotcha we came across while updating our Gradle plugin version? Turns out the newer versions of Gradle reduce the heap size to 512 MB. This is to make sure lower end machines don’t choke up. I am on a 16 gig machine so I can afford to give around 2–3gigs to the Gradle daemon, but your mileage may vary.

Open the **_gradle.properties_** file located at the root of your project and add the following line. Remember to select the size according to your requirements and machine specification.

```
org.gradle.jvmargs=-Xmx3072m -XX:MaxPermSize=512m -XX:+HeapDumpOnOutOfMemoryError -Dfile.encoding=UTF-8
```

While we’re at it, let’s also enable parallel builds and configure on demand in the properties.

Here’s what my final **_gradle.properties_** file looks like:

```
org.gradle.jvmargs=-Xmx3072m -XX:MaxPermSize=512m -XX:+HeapDumpOnOutOfMemoryError -Dfile.encoding=UTF-8

org.gradle.parallel=true

org.gradle.configureondemand=true

kapt.incremental.apt=true
```

* `org.gradle.parallel` - This flag allows Gradle to build modules within a project in parallel instead of sequentially. This is only beneficial in a multi-module project.
* `org.gradle.configureondemand` - This flag configures only the modules needed by the project, instead of building all of them.

With these, let’s see where we are on our build speed metric:

![Image](https://cdn-media-1.freecodecamp.org/images/n9j1jXgfMdiXBu2MHRS361dbrLARbkrv-jOc)

![Image](https://cdn-media-1.freecodecamp.org/images/tB5MZOlTI7pI7XJzeLHeGjQ295mkEoK1WGvW)

And there we go. ???

### Closing remarks

This is by no means an extensive coverage of all the ways one can optimize the build speed of their project. There are tons of other things which I did not go over in this post like using minSdk 21 when using MultiDex, pre-dexing your libraries, disabling PNG crunching, and so on — to name a few.

But most of these configurations require a deeper understanding of Android’s build system and experience working on large multi-module projects _(which is where the benefits are most apparent)_. The steps I mentioned above are easy to incorporate in a project even by junior devs and have considerable payoffs. I hope this helps you trim down your build speeds!

Alright until next time, peace! ✌?

