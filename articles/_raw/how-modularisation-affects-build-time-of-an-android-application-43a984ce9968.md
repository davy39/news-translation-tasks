---
title: How modularization can speed up your Android app’s built time
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-20T16:48:47.000Z'
originalURL: https://freecodecamp.org/news/how-modularisation-affects-build-time-of-an-android-application-43a984ce9968
coverImage: https://cdn-media-1.freecodecamp.org/images/1*J-1MC3QGbIuwq4tb-yr-iA.png
tags:
- name: Android
  slug: android
- name: android app development
  slug: android-app-development
- name: androiddev
  slug: androiddev
- name: gradle
  slug: gradle
- name: mobile app development
  slug: mobile-app-development
seo_title: null
seo_desc: 'By Nikita Kozlov

  Developers will continue to add new features throughout an application’s lifetime.
  More code means not only longer build times — it means longer incremental build
  time.

  For teams with big projects, waiting for new builds could eventu...'
---

By Nikita Kozlov

Developers will continue to add new features throughout an application’s lifetime. More code means not only longer build times — it means longer _incremental_ build time.

For teams with big projects, waiting for new builds could eventually take up 10-15% of their workday. This not only wastes precious developer time — it also makes test-driven development extremely tedious, which hurts overall code quality.

Splitting an application into modules could be a solution to this problem. I was tempted to just split our codebase by feature, by layer, or in some other quick and obvious way. But first, I decided to create an experiment and collect some data, so I could make a better-informed decision. This article will explore the results I collected and my findings.

Before we dive into my experiment, I’d like to talk about the theory behind all this, and explain how we can decrease incremental build time.

### A bit of theory

When you create an Android application you have to have at least one _application_ module, it is a module that applied the Gradle application plugin in his _build.gradle_ file:

```
apply plugin: 'com.android.application'
```

As a result of building this module you will get an .APK file.

One _application_ module cannot depend on another. It can only depend on a _library._ It is the module that applied the Gradle library plugin:

```
apply plugin: 'com.android.library'
```

As a result of publishing such a module you will get an .AAR file (Android Archive Library). Comparing to .JAR file .AAR has some Android-related things, for example, resources and Manifest.

Building process for any library or application module can be _roughly_ split into five phases, that could be represented with a certain Gradle tasks:

1. **Preparation of dependencies.** During this phase Gradle check that all libraries this module depends on are ready. If this module depends on another one, that module would be built as well.
2. **Merging resources and processing Manifest.** After this phase resources and Manifest are ready to be packaged in the result file.
3. **Compiling.** This phase started with Annotation Processors, in case you use them. Then source code is compiled into byte code. If you are using AspectJ, weaving also happens here.
4. **Postprocessing.** All Gradle tasks with a “transform” prefix are part of this phase. Most important ones are: `transformClassesWithMultidexlist` and `transformClassesWithDex`_._ They produce .DEX files.
5. **Packaging and publishing.** For libraries this stage means creating an .AAR file in the end, for applications — .APK.

As I mentioned, our goal is to minimize incremental build time. It’s difficult to speed up all the phases in one experiment, so I decided to focus on the longest ones. For a project with a single module, those were the compiling and postprocessing phases. The merging resources and processing manifest phase can also sometimes be time-consuming, but if the Java code is untouched, than incremental build is quite fast.

We all know, that Gradle runs task in consequent builds only if input isn’t the same. It also doesn’t rebuild a module if it wasn’t changed. That leads to the following hypothesis:

> “The Incremental build time for a project with multiple modules is faster than for a single-module project, because only modified modules are recompiled.”

All right, lets find out whether this is true!

### Experiment Setup

![Image](https://cdn-media-1.freecodecamp.org/images/m8SaIngTlbZkpYa4eqzV1F8hdi26pco4kVfE)

Project uses Gradle plugins v2.2.2. Minimal Android SDK is 15, that covers most of the devices according to [API level dashboard](https://developer.android.com/about/dashboards/index.html). All modules have a dependency on _Butterknife_, to make project a bit more “alive”, since all projects has external dependencies.

In all variants application module is called _“app”_, while library modules are called _“app2”_, _“app3”_ and so on.

Each variant has in total around 100 packages 15,000 classes 90,000 methods. Assembled that is two DEX files, almost three. Generated code is dummy, to keep all the methods in the .APK file, minifying and shrinking were disabled.

All measurements was done with Gradle build-in profiler. To use it you just need to add “--profile” in the end of the command, like this:

```
./gradlew assembleDebug --profile
```

As a result you will get a .HTML file with measurements.

For each setup I repeated each measurement 4 to 15 times, to make sure that my results were reproducible.

#### Java Code Generator

Writing all 15,000 classes by hand is time consuming, so I wrote a simple code generator in Python. It is available in [Gist](https://gist.github.com/NikitaKozlov/ff9d8e65d9d880a2f35e1cac58a84990). Below you can find a schema of the code it generates.

![Image](https://cdn-media-1.freecodecamp.org/images/OMOMY0Ji9nNhHYvfyKBdTcPmeC8fVujWWVYv)

As you can see, every next generated method called the previous one, and every first method of the next class called the last method of the previous class. That makes code more coupled, and increased compilation time.

#### Pure Java modules

I didn’t make a special experiments for pure Java modules. But I played with them a bit, and I can say that usually they are faster then Android ones. That happens because during build less tasks are executed, for example, there is no resources to merge.

If you’re interested in results for pure Java modules, please write a comment. Or you can clone the project from [GitHub](https://github.com/NikitaKozlov/GradleBuildExperiment) and modify it according to your needs. But don’t forget that actual results depend on hardware. To be able to compare your results, please repeat some experiments in your environment as well.

#### Small losses here and there

It’s no surprise that doing something in parallel does slow down the build. Even having a second project open in Android Studio can make build 5–10% slower. Listening to music, watching YouTube, or browsing the internet increases the build time a lot! I personally saw a speeding up of a build process by up to 30% after just closing everything except Android Studio.

All experiments were done with only necessary browser tabs and a single Android Studio project open.

### Let’s do the experiment

#### Initial State

As a starting point I took a project with a single module that contains all 15 000 classes. For this setup incremental build time is _1m 10s_.

#### 3 Modules

First step is splitting one module into three: one application module and two library ones. Application module depends on libraries, but library modules are independent from one another. Each module has about 5 000 classes and 30 000 methods.

If changes are made only in application module, then build time is about 35 seconds. Almost 30 seconds win compare to initial state. But when one of library module is changed, even if application module is untouched, incremental build time grows to _1m 50s_. 40 seconds longer!

Let’s take a look into profile report and see what took so long:

![Image](https://cdn-media-1.freecodecamp.org/images/haPhcC7iI9R6lMmNaSTWm-sEQ3LzTZg8hI41)

![Image](https://cdn-media-1.freecodecamp.org/images/4RI8AzAfrQCPVsDjVRt009zHjGdaUPo30Rbk)
_Profile report of an incremental build with changes in library module (“:app2”). Since application module (“:app”) depends on the library one, it is also recompiled._

In the screenshots above, you can see that most of the time was spent on building the library module. You might also notice that for library modules, both debug and release tasks were executed. Gradle wasted time executing two sets of tasks instead of one! This is why it took an extra 40 seconds longer than the single-module project.

We can avoid this and make this build even faster than our initial _1m 10s_ by splitting our code into modules.

But that’s not the only problem. Let’s look into _how_ our application module depends on library modules:

```
dependencies {    compile project(path: ':app2')    compile project(path: ':app3')}
```

There’s an important problem in the code above: if a library is added like this, then the application always depends on the _release_ variant, independent of it’s own build type. It also doesn’t matter which variant is chosen in Android Studio. Here’s what the [Gradle Plugin User Guide](http://tools.android.com/tech-docs/new-build-system/user-guide#TOC-Library-Publication) says about all this:

> By default a library only publishes its _release_ variant. This variant will be used by all projects referencing the library, no matter which variant they build themselves. This is a temporary limitation due to Gradle limitations that we are working towards removing.

Luckily, it’s possible to change the variant our application depends on.

First, add the following code to libraries’ _build.gradle_ file. It will allow library to publish _debug_ variant as well:

```
android {    defaultConfig {        defaultPublishConfig 'release'        publishNonDefault true    }}
```

Second, application module should depend on library ones like this:

```
dependencies {    debugCompile project(path: ':app2', configuration: "debug")    releaseCompile project(path: ':app2', configuration: "release")    debugCompile project(path: ':app3', configuration: "debug")    releaseCompile project(path: ':app3', configuration: "release")}
```

Now the debug variant of our application depends on the debug variant of the libraries, and its release depends on their release. So lets make some changes to the module _app2_ and rebuild it. After these changes, we can check our profile report again:

![Image](https://cdn-media-1.freecodecamp.org/images/khyDy7gT4Hd8SiCz7rfoDlarUfRyGRCINpXs)

![Image](https://cdn-media-1.freecodecamp.org/images/D-udP9Ns1gkbTFHdcLh0AE7MDlkYoNb3jJ66)

The most significant difference is the absence of _:app2:packageReleaseJarArtifact,_ which saves us about 15 seconds. In addition, the time is reshuffled a bit between rest of the tasks, and we end up with _1m 32s_. That is 18 seconds faster then before, but still 22 seconds slower then our initial configuration. For changes only in the application module, build time stays almost the same — _36 seconds_ vs _35 seconds_ in our previous configuration.

Unfortunately I didn’t found a proper explanation for why it builds both flavors. I hope that once this Gradle limitation is resolved, then this problem will just go away as well. The same issue is discussed in [AOSP Issue Tracker](https://code.google.com/p/android/issues/detail?id=52962).

I’m also planning to spend some time experimenting with Gradle tasks to find a workaround for this problem. One possible way is to exclude all release tasks for debug builds.

#### 5 Modules

Obviously, build time depends on the amount of code. If you reduce amount of code by half then the build should also be roughly two times faster. If instead of 3 modules project is split in 5, then build time should be approximately 40% faster.

It is almost true.

![Image](https://cdn-media-1.freecodecamp.org/images/JsR7H3b6U9J49HLLY6rV5BCsNnuCQIT0O4rx)

If changes are made only in application module then incremental build time is approximately 24_s._ For changes in a library module incremental build takes _50s_. Compare to initial _1m 10s_ that is already a win. But I have a few more tricks at my disposal.

#### Reduce Size of The Application Module

Independently of what module is changed, application module will be recompiled every time. So reducing it’s size makes total sense. Ideally, it should just assemble whole application from a separate modules and might also provide a splash screen, because splash screen often depends on lots of features.

That is how idea about _3+1_ and _5+1_ configurations was born. In both cases project has a small application module that depends on 3 and 5 library modules accordingly. All library modules are independent from one another and has equal sizes. Let’s see what that gives us:

![Image](https://cdn-media-1.freecodecamp.org/images/e5AZF2lz4WsblcBuK1WA94CRadMgF7lPrjr-)

We can observe further drop in incremental build time. Even with changes in library module _5+1_ configuration is build almost twice as fast as an initial single-module project. This is a decent progress.

#### Why does project actually depends on Butterknife?

This is a point where I have to make a confession. There was one very strong reason to add a dependency on _Butterknife_.

In the initial configuration incremental compilation takes _45s_ out of _1m 10s_, but if _Butterknife_ is removed then project is compiled in _15s_ only! Three times faster! Whole incremental build without Butterknife is _40s_.

Is it a problem in the library?

As it appeared — no. Without _Butterknife_ project compiles so fast because of actual Java incremental compilation, which is disabled for projects that use Annotation processors. You can find related issues in [Gradle Jira](https://issues.gradle.org/browse/GRADLE-3259), in [AOSP Issue Tracker](https://code.google.com/p/android/issues/detail?id=200043), it is also tracked in Gradle [design docs](https://github.com/gradle/gradle/blob/master/design-docs/incremental-java-compilation.md). If you will take a closer look into the issue from ASOP Issue Tracker, one of the comment says:

> _“Annotation processors is not yet supported with incremental java compilation. It will depend on changes in Gradle._

> _We disabled it for project that apply com.neenbedankt.android-apt, so it's no longer a significant issue.”_

That is why build just becomes slower without a notification.

Personally I won’t remove Annotation processors from the whole project. I find libraries like _Dagger_ and _Butterknife_ useful. But having a couple of modules without them could be a good idea, that would make their builds so much faster!

#### One More Trick — Rump Up API Level

Compilation is not the only thing that slows down build process. Producing .DEX files could also be time consuming. Especially if an application is above DEX Limit. Using multidex configuration increases build time, build system need to decided which classes go to which .DEX file. With introduction of Android Runtime the way how Android OS works with application that has multiple DEX files has changed. This is what [Android Studio documentation](https://developer.android.com/studio/build/multidex.html#mdex-on-l) says about it:

> _“Android 5.0 (API level 21) and higher uses a runtime called ART which natively supports loading multiple DEX files from APK files. ART performs pre-compilation at app install time which scans for `classesN.dex` files and compiles them into a single `.oat` file for execution by the Android device.”_

That leads to decrease in build time. The reason is that each module produces its own DEX files, that are included into APK without modification. If you take a look into the tasks that run during build, you will notice that `transformClassesWithMultidexlist` is no longer executed. Also compilation itself became faster. You can find more information and instructions how to make a flavor that uses API 21 [here](https://developer.android.com/studio/build/multidex.html#dev-build).

#### Fastest Build Configuration Achieved.

Using API 21 for debug is an easy gain for every project. I tried it for _5+1_ configuration and results were amazing:

![Image](https://cdn-media-1.freecodecamp.org/images/odoCUKJg-NQm9vl4yJKfZfh7jLCsxqEPqRAS)

Even for changes in library module incremental build time was only _17 seconds_! But take into account that all modules are independent from one another. Once dependency between modules is introduced, build time increases from _17s_ to _42s_ (last row in the table above)!

#### Developing Library Module in a Test Driven Way

One of the main reasons why test-driven development (TDD) is difficult for single-module project is build time. TDD encourage to run test often. Running tests multiple times in a minute is a normal practice. But when build takes a minute or two, working in Test Driven way couldn’t be very productive.

With introduction of modules that problem is automagically resolved. Building a single module in the last configuration took only _9s_! It make possible to run tests as often as needed.

### Conclusion

![Image](https://cdn-media-1.freecodecamp.org/images/8hhEYND4vfQGxgZ-NOcL8YVohRxBHLHqjm3G)

First and most important, the hypothesis was correct, modularizing project can significantly speed up build process, but not for all configurations.

Second, if splitting is done in a wrong way, then build time will be drastically increased, because Gradle build both, release and debug version of library modules.

Third, working in test-driven way is much easier for a project with multiple modules, because building a small library module is way faster then the whole project.

Forth, doing many things in parallel slows down the build. So having more powerful hardware is a good idea.

Below you can find results of all experiments described in this article:

![Image](https://cdn-media-1.freecodecamp.org/images/hxYQoAIaUGfb-dIVjjBmZVtiDyiPmpGyOOkw)

Please vote for mentioned issues. Resolving any of those would be a huge step towards faster builds. Below you can find all links:

* [https://code.google.com/p/android/issues/detail?id=52962](https://code.google.com/p/android/issues/detail?id=52962)
* [_https://issues.gradle.org/browse/GRADLE-3259_](https://issues.gradle.org/browse/GRADLE-3259)
* [https://code.google.com/p/android/issues/detail?id=200043](https://code.google.com/p/android/issues/detail?id=200043)

All code is published on [GitHub](https://github.com/NikitaKozlov/GradleBuildExperiment).

[**Nikita Kozlov (@Nikita_E_Kozlov) | Twitter**](https://twitter.com/Nikita_E_Kozlov)  
[_The latest Tweets from Nikita Kozlov (@Nikita_E_Kozlov): “https://t.co/wmGSJ7snW1"_twitter.com](https://twitter.com/Nikita_E_Kozlov)

_Thank you for you time reading this article. If you like it, don’t forget to click the_ ? _below._

