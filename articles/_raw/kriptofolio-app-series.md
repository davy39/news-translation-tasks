---
title: A roadmap to build a modern Android app
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-12T20:05:00.000Z'
originalURL: https://freecodecamp.org/news/kriptofolio-app-series
coverImage: https://cdn-media-1.freecodecamp.org/images/1*rvYYjocj8-ytP2OBY_Fdpg.png
tags:
- name: Android
  slug: android
- name: Apps
  slug: apps-tag
- name: Cryptocurrency
  slug: cryptocurrency
- name: Kotlin
  slug: kotlin
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Andrius Baruckis

  Kriptofolio app series — Introduction

  Welcome to this series of blog posts where I will be creating a modern Android app.
  I will use the best tools and practices available in the year 2018–2019. I am doing
  this because I want to c...'
---

By Andrius Baruckis

#### Kriptofolio app series — Introduction

Welcome to this series of blog posts where I will be creating a modern Android app. I will use the best tools and practices available in the year 2018–2019. I am doing this because I want to cover all the hottest topics in the Android world and acquire knowledge in them by teaching you.

If you follow this series, you will learn how to develop the app from scratch. Each blog post from this series will cover some specific development topic which I want to talk about. I will try to do my best to create a good quality app and explain the development process. This first blog post from the series is a project’s roadmap of what we are going to do.

### Series content

* Introduction: A roadmap to build a modern Android app in 2018–2019 (you’re here)
    
* [Part 1: An introduction to the SOLID principles](https://www.freecodecamp.org/news/kriptofolio-app-series-part-1)
    
* [Part 2: How to start building your Android app: creating Mockups, UI, and XML layouts](https://www.freecodecamp.org/news/kriptofolio-app-series-part-2)
    
* [Part 3: All about that Architecture: exploring different architecture patterns and how to use them in your app](https://www.freecodecamp.org/news/kriptofolio-app-series-part-3)
    
* [Part 4: How to implement Dependency Injection in your app with Dagger 2](https://www.freecodecamp.org/news/kriptofolio-app-series-part-4)
    
* [Part 5: Handle RESTful Web Services using Retrofit, OkHttp, Gson, Glide and Coroutines](https://www.freecodecamp.org/news/kriptofolio-app-series-part-5)
    

### The app: “Kriptofolio” (previously “My Crypto Coins”) idea

At first it was hard to think of a plan to showcase all Android development trends, but finally, I found one which I liked. It is related to my huge interest area — blockchain and cryptocurrencies. I decided to create an app which would contain your cryptocurrencies portfolio and let you know how much they are worth converted to fiat money.

The important thing for the user is that this app is going to ensure 100% trust. It will not require any login/registration process. It won’t collect users’ data by sending it to the server. I guess nobody would feel comfortable sharing information online about owned money.

Users’ provided data about cryptocurrency investments will be only stored inside a local database that is kept inside an Android device. However, to know the portfolio’s value converted to the fiat money, the app is going to use the Internet to get the latest conversion rates.

So as you see for training purposes, this app idea is great. It is technically challenging you to try different approaches to work with data. This is one of the most important skills to know to build modern apps. The topic of money for people is so sensitive. To ensure even more trust, I will be developing this app openly by creating this blog posts series and making the project code available so everyone can see that there is nothing to hide.

### What are we going to use?

First, to create this app, we need to know about various cryptocurrency prices at the current moment. This data will be provided from the Internet as it is continually changing.

#### Data API:

[CoinMarketCap](https://coinmarketcap.com/) — one of the most popular websites for getting an overview of the cryptocurrency market. This website offers a free [API](https://coinmarketcap.com/api) that anyone can use and it fits perfectly for us as a data service provider.

Next, I made a list of my most significant trending things in the Android world that fit this project and should be used in it.

#### Programming language:

[Kotlin](https://kotlinlang.org/) — an official language on Android. It is expressive, concise, and powerful. Best of all, it’s interoperable with existing Android languages and runtime.

This new language introduction was one of the hottest topics in 2017 for Android. Our app needs to be written in it. I also talk about Kotlin and its features in my past blog post “[Let’s learn Kotlin by building Android calculator app](https://medium.com/mindorks/learn-kotlin-android-calculator-app-b86b275cc27c)”.

#### Integrated development environment (IDE):

[Android Studio](https://developer.android.com/studio) — the official IDE for Android. It provides the fastest tools for building apps on every type of Android device. There are no better alternatives for developing native apps. It’s our main choice for an IDE without any question.

#### Project build management system:

[Gradle](https://gradle.org/) — is an advanced general purpose build management system based on Groovy and Kotlin. It supports the automatic download and configuration of dependencies or other libraries. It is the recommended build system by Google. It is well integrated inside Android Studio so we will be using it.

#### Architecture:

[Android Architecture Components](https://developer.android.com/topic/libraries/architecture) — a collection of libraries that help you design robust, testable, and maintainable apps.

[Model–View–ViewModel (MVVM)](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93viewmodel) — an architectural pattern. The concept is to separate data presentation logic from business logic by moving it into a particular class for a clear distinction. The Android team is pushing this pattern as the default choice. Also, it’s an alternative to [MVC](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller) and popular [MVP](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93presenter) patterns.

I’ll be talking separately in this series about this pattern choice, other architecture options and how to organize our code well in general. It is essential if we want to build an easily maintainable solid project.

[Coroutines](https://kotlinlang.org/docs/reference/coroutines-overview.html) — a concurrency design pattern that you can use on Android to simplify code that executes asynchronously.

#### Data persistence:

[SQLite Database](https://developer.android.com/training/data-storage/sqlite) — it is an open source SQL database that stores data persistently to a text file on a device. Android comes in with built-in SQLite database implementation. SQLite supports all the relational database features.

[Shared Preferences](https://developer.android.com/reference/android/content/SharedPreferences) — an API from Android SDK to store and retrieve application preferences. SharedPreferences are merely sets of data values stored persistently. It allows you to save and retrieve data in the form of key value pairs.

#### Libraries:

[*Android Jetpack*](https://developer.android.com/jetpack) *components:*

[AppCompat](https://developer.android.com/topic/libraries/support-library/packages#v7-appcompat) — it is a set of support libraries which can be used to make the apps that were developed with newer versions work with older versions.

[Android KTX](https://developer.android.com/kotlin/ktx) — a set of Kotlin extensions for Android app development. The goal of Android KTX is to make Android development with Kotlin more concise, pleasant, and idiomatic by leveraging the features of the language such as extension functions/properties, lambdas, named parameters, and parameter defaults.

[Data Binding](https://developer.android.com/topic/libraries/data-binding) — is a support library that allows you to bind UI components in your layouts to data sources in your app using a declarative format rather than programmatically.

[Lifecycles](https://developer.android.com/topic/libraries/architecture/lifecycle) — for managing your activity and fragment lifecycles.

[LiveData](https://developer.android.com/topic/libraries/architecture/livedata) — is an observable data holder class which was designed to help solve common Android Lifecycle challenges and to make apps more maintainable and testable.

[Room](https://developer.android.com/topic/libraries/architecture/room) — it provides an abstraction layer over SQLite to allow easy database access while harnessing the full power of SQLite.

[ViewModel](https://developer.android.com/topic/libraries/architecture/viewmodel) — designed to store and manage UI-related data in a lifecycle conscious way. The ViewModel class allows data to survive configuration changes such as screen rotations.

*Other:*

[ConstraintLayout](https://developer.android.com/reference/android/support/constraint/ConstraintLayout) — for building flexible and efficient layouts. The Layout Editor uses constraints to determine the position of a UI element within the layout. A constraint represents a connection or alignment to another view, the parent layout, or an invisible guideline.

[CardView](https://developer.android.com/reference/android/support/v7/widget/CardView) — element which represents the information in a card manner with a drop shadow (elevation) and corner radius which looks consistent across the platform.

[RecyclerView](https://developer.android.com/reference/android/support/v7/widget/RecyclerView) — a flexible and efficient version of ListView. It is a container for rendering large data set of views that can be recycled and scrolled very efficiently.

*Third-party:*

[Dagger 2](https://google.github.io/dagger) — this is an entirely static, compile-time dependency injection framework for both Java and Android.

[Retrofit 2](https://square.github.io/retrofit) — an open source type-safe HTTP client for Android and Java. With Retrofit, we can compose the HTTP connection easily through a simple, expressive interface just like an API document.

[OkHttp](http://square.github.io/okhttp) — an open source modern, fast and efficient HTTP client which supports HTTP/2 and SPDY.

[Gson](https://github.com/google/gson) — an open source Java library to serialize and deserialize Java objects to and from JSON.

[Glide](https://bumptech.github.io/glide) — a fast and efficient image loading library for Android focused on smooth scrolling. Glide offers an easy to use API, a performant and extensible resource decoding pipeline and automatic resource pooling.

### Configuring a new project

We will create this project from scratch. So I’ll launch Android Studio, create a new Project, name it “My Crypto Coins” and select “Basic Activity”. At this point, there is nothing special to discuss. Our goal is to make a fresh, clean start and avoid any complexity in our minds by adding additional features (e.g., instant app support). We can add anything later if we want during the development process.

For a start let’s include Kotlin language support and target [API 23: Android 6.0 (Marshmallow)](https://en.wikipedia.org/wiki/Android_Marshmallow).

Why am I not targeting a lower or higher API? Let’s face it. It’s nice to cut the support for some older devices and not worry about any compatibility issues during development. Also, I am a proud owner of an old [Nexus 7 (2013) tablet](https://en.wikipedia.org/wiki/Nexus_7_\(2013\)), which is running Android 6.0.1. I hope to test my app live on it. ? So for this individual project that impacted my minimum SDK choice.

Also as you’ve noticed, I am going to ask IDE to add automatically generated basic activity with fragment support and a floating action button. I feel all that could be useful for our project.

![Image](https://cdn-media-1.freecodecamp.org/images/TVPZwad45enjSKAkTnJPRK4ld-BV1toGKXs- align="left")

***In Android Studio from v3.0 Kotlin plugin is already built-in, just select checkbox to add support.***

![Image](https://cdn-media-1.freecodecamp.org/images/vp5Rm1gsBRER1UbDrkcMv5LjQihJsI6cqXFT align="left")

***Select minimum targeted SDK based on business needs.***

![Image](https://cdn-media-1.freecodecamp.org/images/xNcIHSD6HRUnVbKI5u42o520HMfDLu9NeM9o align="left")

***Choose basic activity which will generate useful code for a start.***

![Image](https://cdn-media-1.freecodecamp.org/images/Bl0EpPhu8JPnNuDkYveUdbwqGWJurodIuhX8 align="left")

***Select the checkbox to have content placed into the fragment.***

[GitHub](https://github.com/) — one of the most popular web-based hosting service for version control. This is an open source project, and of course, I will be using it.

All the blog posts from this series will have its commits made as separate branches and the master branch for the latest source code version. Here is a link for you to the repository.

#### [View Source code on GitHub](https://github.com/baruckis/Kriptofolio)

That’s it for the start. If you have any questions, suggestions, remarks to make, please feel free to do that in comments. And now let’s learn together! Part 2 is up next… ?

---

***Ačiū! Thanks for reading! I originally published this post for my blog*** [***www.baruckis.com***](https://www.baruckis.com/android/kriptofolio-app-series/) ***on February 12, 2018.***
