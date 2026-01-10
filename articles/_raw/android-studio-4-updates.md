---
title: Android Studio 4.0 – the Most Exciting Updates Explained
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-19T22:28:00.000Z'
originalURL: https://freecodecamp.org/news/android-studio-4-updates
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/android.png
tags:
- name: Android
  slug: android
- name: android app development
  slug: android-app-development
- name: mobile app development
  slug: mobile-app-development
seo_title: null
seo_desc: "By Roger James\nIn the midst of a pandemic, Google finally released its\
  \ stable version of Android Studio 4.0 on May 28, 2020. \nEvery release brings its\
  \ own interesting updates and bug fixes that help developers code smarter and develop\
  \ apps faster tha..."
---

By Roger James

In the midst of a pandemic, Google finally released its stable version of **Android Studio 4.0 on May 28, 2020.** 

Every release brings its own interesting updates and bug fixes that help developers code smarter and develop apps faster than ever. And Android studio 4.0 is no exception.

In this article we will learn about some of the exciting features that Android studio 4.0 brings to the table that will help developers out a lot. 

You can get a direct link to download Android Studio 4.0 by [clicking here](http://studio) for your Windows, Mac, and Linux machines.

Here are some highlights of the release notes:

![Image](https://lh4.googleusercontent.com/L6l7K-eujulsvFgFa-c-Z8Uw5vf8G2g-P_3lLVWFm5Ijt7KEFZRw6OLenSHrCZxOHoRLQaWVfONUAnxSRoqqQGwZqh4ipYZYrJqoOPaKnnn1GhD8yOzrIr2eJprSl4p_ievJswEa)

Android Studio 4.0 introduces a plethora of interesting features, including

* Build Speed Window
* Layout Multi Preview
* Motion Editor
* Live Layout Inspector
* Smart Editor for R8 Rules 
* Kotlin DSL script files

Let’s take an in-depth look at the fun new features of Android Studio 4.0.

## What are Android Studio 4.0's new features?

Following is a list of new features along with some info about how they work and why they're great.

### 1. Motion Editor

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-101.png)

The Motion Editor upgrades the visual design editor for motion layout and it also generates XML. MotionLayout is a subpart of _ConstraintLayout_ that helps developers manage widget and motion animation in [mobile applications](https://www.freecodecamp.org/news/how-to-secure-mobile-apps/). 

It has a visual design editor that helps you create, edit, and preview your animations without developing the application. It also allows you to play/pause animations for debugging. 

Motion layout takes the place of the previous constraint layout and improves it. It helps Android app developers animate between layout states and manage critical animations easily.

You can now deploy the the _Motion Layout API_ with the advanced _Motion Editor_ to develop or edit an animation while everything is stored in an XML file.  

The only difference is that you don't need to write it out manually because everything is now be managed by the Motion Editor. You can easily preview your animations and make any changes.

### 2. Live Layout Inspector

![Image](https://lh6.googleusercontent.com/CY3Ej_RuhXaxqK9wYYAqDXcoNL_3pJR1nxZUO4_eypEC1ChBZjD4Je_IFKNRal-L4xIQznl8aGW0fefhj0tbkyno6yEm3ooBUynqUaSdTGhwpt08EKFQd3ErFIZPAsz7pdKiy_a-)
_[**Image Source**](https://medium.com/androiddevelopers/layout-inspector-1f8d446d048)_

Android Studio 4.0 now allows developers to have real-time insights into their mobile applications’ UI. This means now you can visualize how your application will be laid out on-screen along with various features.  

It also has a dynamic layout hierarchy that gets updated with each refresh, and has detailed view attributes that help you determine resource values. 

You can deploy the feature by selecting **View> Tool Windows> Layout Inspector** from the main menu. 

If you are deploying an app to a device running on the API level 29 or higher, then you can access some additional features like a dynamic layout. There's a lot of detailed information on the Layout Inspector to check out as well.

Its property value resolution feature allows you to learn the origin of the property in the source code. It also navigates you to its location using the hyperlink. You can leverage the benefit of 3D representation if your application or device is running on **Android API 29** or more.

Developers can now deploy a 3D representation of the on-screen animation and inspect the other attributes. So, when you hire a developer to revamp your app interface or add in new features, you don’t have to worry about the look of the app with modern UX/UI design typography as you can check simultaneously during coding.

### 3. Layout Validation

![Image](https://lh6.googleusercontent.com/mNaXO7Uhmu5DFI2ctSeWhqGeEz1zOgVjp82W6wJ4CaKV0SVPNK7Lb3DfU8UsRTNXYT4-DqHeuFYFj5hhuO-ZchoNm4TpriRLhvGf2dYSS_uXY5oJwQOfsK0DPgPAv_TOpUaf5i9b)
_[**Image Source GIF** ](https://developer.android.com/studio/debug/layout-inspector)_

You can now produce layouts in various devices and configure them at the same time without any interruption. _Layout Validation_ or _Layout Multi_ preview are visual tools.  

Previously, when creating a layout in Android studio, switching between different screen sizes and resolutions in preview mode was challenging. But with these latest updates, it's a lot simpler.

How so? Well, you just need to choose the pixel devices and then you can easily check or preview the changes in the integrated development environment. 

You can also use this tool to identify possible issues in the UI as you're often designing a UI for a particular configuration or visible screen size.

You can access this tool by clicking on the **Layout Validation** tab in the **top right corner** of the **IDE window**.

### 4. Build Analyzer

![Image](https://lh3.googleusercontent.com/QHwWxAxkZUKTSzxmElJXcV6U8TL88Cg-aRYU_9C-H_x0lJUbCaIq-YHHdCYEShM5pIJVb6_2eW9cQpXZeVsDkRqNHn2TJdlAOFiAs6hBzIEpLRd_kVW_2tc9xq99BsidcgC9HU51)
_[**Image Source**](https://developer.android.com/studio/build/apk-analyzer)_

Android Studio 4.0 introduced a Build Analyzer tool that helps developers analyze and handle build-related issues. Application development time has always represented a lot of overhead for Android devs.

This new feature quickly mitigates lost time and productivity by recognising outdated and misconfigured jobs. The build analyzer tool shows your jobs and plugins and suggests ways to reduce regressions. 

This also helps with another problem – before, developers didn't know exactly which part of the build system was taking more time. Not the case now.

So the new grade plug-in 4.0 helps developers analyze and find the issue, such as improperly configured tasks, in the build process. You can easily specify the default settings by including one or more of the lines below in each modules’ build.gradle file.

![Image](https://lh4.googleusercontent.com/IfEkdNyS602D0FbzFoVDUj_vkXeqIyNdAJI4FzbZW6WhxG3ik3MBx0fGRoIAfaWxJE32d6VK_T-WJfuWGf6d_ktladRlmQRBV_I-lYSQJA_iqwi40sxdVpfJTsjMpK1MaBfT9ntl)

Build analyzer also helps you address and understand bottlenecks in your build by calling out the plug-ins and tasks that are most important for overall application build time. It then gives you some steps to mitigate regressions.

### 5. Java 8 Language Library Desugaring for all APIs

![Image](https://lh5.googleusercontent.com/eBFuPz0PDehdRa28ZEMxNTd3Ya2cZH48-bNlO_COUAG6ZPLfY9Wd-uflU4Cp4le12aFmv0cGD1-OuLopJ-48oThRNszytUiOtVsl69lWyFdy9N4gQ6aiKEhdNQ1qJIaR34r-j36u)
_[**Image Source**](https://developer.android.com/studio/write/java8-support?hl=el)_

Another super annoying part of Android app development has been trying to deploy Java 8 features. You may find some code that uses a **Stream** or want to implement a **lambda function** or there may even be a Java 8 API that you require which isn't practical to work around. 

But with the **Android Gradle** plugin, you can compile certain Java 8 features with your older APIs.

And Android Studio 4.0 enables the desugaring engine to provide support to Java languages.

### 6. Build Features

![Image](https://lh6.googleusercontent.com/uLTDonznC4iK9bVZR3aCBh3RYjfKe4t5JeumdJw3gGs_XawiJ02o4Cujzg8LixhSVtmtFToeJ62rgeNfIC57DgewvVcZdE43SreMHunupZbW-kGved-0_9hTVjrkBl9HcQCgm-L9)
_[**Image Source**](https://developer.android.com/studio/releases)_

Developers leveraging Android Studio 4.0 can enable and disable build features, such as view binding, data binding, or auto-generated BuildConfig classes. 

Also, you may not require these plugins and libraries for each and every project, so you can disable the libraries/plugins and surge the scalability for big projects. 

Kotlin is one of the most used technologies among [android programmers in India](https://www.valuecoders.com/hire-developers/hire-android-developers?utm_source=freecodecamp&utm_medium=hire%2Bandroid%2Bdeveloper_rg&utm_campaign=website), and this feature will likely encourage its adoption for faster app development in the future.

### 7. Latest Editor for R8 Rules

R8 was introduced in Android Gradle plug-in 3.4.0 to combine shrinking, desugaring, dexing, and obfuscating all in one step. This resulted in improved build performance. 

Previously, there was no support for a smart editor that offered auto-suggestions while writing R8 rules. But with Android Studio 4.0, a smart editor can write the rules for code shrinking.

When developing rules files for R8, Android Studio now offers various features, including completion, syntax highlighting, and error-checking. 

This editor smoothly works with your project to offer full symbol completion for all models, classes, and fields and also includes refactoring and navigation.

![Image](https://lh6.googleusercontent.com/6GkRn5PchI3-pblXj1xTrVive131J_4A1-CWlNlNLa0nCOhb9ZmmXiJdWmBKgHSdaGK3JfUApKFelO8wbEGdcl_u_4gyOi64VwrZZbFdKdWKJf7U5do2VhDBmD86ukOng6_Yu_oV)
_[**Image Source**](https://miro.medium.com/max/711/1*fzTTnrKnVuVpO0H_eWnWmQ.png)_

### 8. Fragment Wizards

![Image](https://lh3.googleusercontent.com/82lsSjJI0AJhHUjW0UDWg9vEp4b4grDfh4Xfrsei4OrT9eEloifBFvCni_OpH4qhoh77aXpc23STWWpGog4LtpFgdglKJyOGyUzNSpb1PS3PGLebdWYw7tkPnrw-L9qQM56IvI5t)
_[**Image Source**](https://stackoverflow.com/questions/37432212/android-wizard-with-multiple-fragments-back-button-behavior)_

New fragment templates and fragment wizards are now available in the navigation editor.

These templates allow developers to quickly navigate fragment wizard content to creating slideshows using **ViewPager** (which is available in the support library). This tool lets you easily set up slide animation and enhances the app's look and feel. 

These updates have made it easier for developers to implement an animated default screen slide through simple drag & drop templates available in the navigation editor. And there's less coding involved, too. 

Basically, Fragment is a class in Android that allows the integration of a UI that's adaptable to different device screen orientations. It combines different types of segments into a single screen element.

The introduction of templates into Fragment Wizard makes using these different features pretty effortless. And it's definitely a bonus when your mobile app's UI adapts to different screen sizes and orientations.

### 9. Kotlin Android Live Templates

![Image](https://lh3.googleusercontent.com/Fp4myIQSWXL9PR8S706CmBWUwc7w2un7Yp3fPL6LUYQp2pmiFdYYeMgXf4fTn_TOfNHqrQxRk4SnBf-k3-R9xC5VBKvl1EZLe0hw2SpIOGmTXu8skKiNdpSH3V0uMeCPFOFQwPU5)
_[**Image Source** ](https://stackoverflow.com/questions/51473637/how-to-create-a-kotlin-live-template-for-newinstance-fragments-using-android-stu)_

The latest version of Android Studio has built-in support for **Kotlin DSLscript** files. You can easily use the full suite of quick fixes that are supported by the project structure dialogue. Android Studio now has Android-specific live templates for Kotlin code.

For instance, simply type **“toast”** and press the **Tab Key** to swiftly insert boilerplate code for a Toast. 

For a full list of live templates, navigate to **Editor> Live templates** in the settings (or preferences) dialogue.

### 10. CPU Profiler UI Upgrades

![Image](https://lh6.googleusercontent.com/L3ENpbiZj0xq8XtsuSe_3yi91WXYvkxmkO4O7XtADPvDmmTuebvFqKO7Su5-_CT09MiNk8f703tCIDpmwrKUqETbE1TS7C-rLai7g0LZNi1p9NfyT2dCkKTBQrJVzilB5Clkdw8h)
_[**Image Source**](https://developer.android.com/studio/profile/cpu-profiler.html?hl=lt)_

CPU Profilers are one of the best new features in Android Studio – especially when it comes to performance. The CPU profiler is designed to give you information related to trace recording and your app’s thread activity. 

Before, all the profilers’ data used to display under one section:

![Image](https://lh3.googleusercontent.com/7BAmmJFUBcUgNEc4RNpg6iEEdZHg3P9svGM-EqwT8cb1tcBOIpMlI5eL_aksD0aSlRIKKxbt8MbeWuetlFukOJxus9WAlCHXEu2JfxHGwkw604lmlHXUFF1mzQqNhFMmL4r3QC7O)
_[**Image Source**](https://miro.medium.com/max/788/1*4IDJaeUhsraqzeqc9Mynrg.png)_

With Android Studio 4.0, CPU recordings can be set aside from the main profiler timeline and managed in groups to allow easier analysis. Developers can easily drag-and-drop and move groups up and down individual items within a group for further customization. 

In addition, for smooth side-by-side analysis, you can inspect all thread activity in the Thread Activity timeline (including functions, methods, and events) and try the latest navigation shortcuts to move around data.

The System Trace UI was also upgraded so that the events can be uniquely coloured for improved visual distinctions. Threads can also be sorted to surface the busier ones based on priority, and you can focus more on seeing data for only the threads you have selected rather than all combined data. 

For detail description on CPU Profiler [click here](https://developer.android.com/studio/releases#cpu-profiler-upgrades).

### 11. Feature on Feature Dependencies

![Image](https://lh6.googleusercontent.com/BHSx1Ets1xQMFDaqXAop0cfNXOZ9_iQVOlXHGOurDGDTHcuzg_YFHEzAX-FgPmxaZIC2vAVl3q2y0-q4AU5ZUFZwkyRHqS7-QPwK-p_SxI_pTuqRk1kDi13RDS7PzDONG3KhGYeb)
_[**Image Source**](https://android-developers.googleblog.com/2020/05/android-studio-4.html)_

Android Studio 4.0 lets developers designate which dynamic feature module is dependent on another feature module. By deploying this, you can check if the app has sufficient modules to improve the functionality of your applications.

For example, if a user records a video, then the computer module automatically gets downloaded. This is because the video module depends on the camera module.

## Conclusion

These are the features of Android Studio 4.0 that will really help improve the performance of your Android applications. They'll also help Android app developers code more quickly and efficiently.

Currently, creating Android apps is a major investment interest among both entrepreneurs and enterprises. 

Thus, there is huge competition among businesses to choose an [android app development company](https://www.pixelcrayons.com/mobile-app-development/android-development?utm_source=freecodecamp&utm_medium=android%2Bapp%2Bdevelopment_sk&utm_campaign=website) that's up to speed on modern technology verticals and that can create valuable products. 

The launch of Android 4.0 will make things a whole lot easier and more interesting for everyone.

