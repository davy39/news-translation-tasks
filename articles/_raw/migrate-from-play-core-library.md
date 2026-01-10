---
title: How to Migrate from Play Core Library
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2024-06-26T17:53:46.000Z'
originalURL: https://freecodecamp.org/news/migrate-from-play-core-library
coverImage: https://www.freecodecamp.org/news/content/images/2024/06/ben-hershey-fnRKVPx5_xY-unsplash.jpg
tags:
- name: Android
  slug: android
- name: android app development
  slug: android-app-development
seo_title: null
seo_desc: 'You may have recently received an email from Google Play Store stating
  the following:


  Update your Play Core Maven dependency to an Android 14 compatible version! Your
  current Play Core library is incompatible with targetSdkVersion 34 (Android 14),
  w...'
---

You may have recently received an email from Google Play Store stating the following:

> _Update your Play Core Maven dependency to an Android 14 compatible version! Your current Play Core library is incompatible with targetSdkVersion 34 (Android 14), which introduces a backwards-incompatible change to broadcast receivers to improve user security. As a reminder, from August 31, Google Play requires all new app releases to target Android 14. Update to the latest Play Core library version dependency to avoid app crashes:_ [_https://developer.android.com/guide/playcore#playcore-migration_](https://developer.android.com/guide/playcore#playcore-migration)  
>   
> _You may not be able to release future versions of your app with this SDK version to production or open testing._

Looks frightening, doesn’t it?

Don’t be so worried. It is actually easier than it looks.

## What the Change is Actually About

Basically, Google stopped releasing new versions of the play core library back in early 2022.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/1.jpg)
_The last version of play core library released_

And from April 2022, they have broken down the original play core library into four separate libraries:

* Play Assets Delivery Library
* Play Feature Delivery Library
* Play In-App Reviews Library
* Play In-App Updates Library

Each library has its own functionality and responsibility.

Since the older core play library only supports up to a certain API level, you need to migrate your application to use the newer libraries that have support for the most recent API levels.

In essence, you need to figure out which functionality of the original core play library you are using and then download the correct part. For example, if you had logic to notify users when a newer version of your application was available, you need to take the Play In-App-Updates library.

We will be presenting two uses cases here:

* Native Android application
* Flutter application

## Use Case – Native Android App

If you have a native Android application, whether it is written in Kotlin or Java, you need to do the following:

1. Open your application level build.gradle file
2. Most probably you will see under the dependencies block, this line:

```groovy
implementation 'com.google.android.play:core-ktx:1.8.1'

```

3.  You will need to remove it and replace it according to what you used in the previous core library

4.  If you need to take the Play In-App-Updates library, then you need to add these to the dependencies block:

```groovy
implementation 'com.google.android.play:app-update:2.1.0'
//Add the dependency below if you are using Kotlin in your application
implementation 'com.google.android.play:app-update-ktx:2.1.0'
```

5.  Rebuild your application and see that everything works as it should.

✋ You might also need to change import statements from **import com.google.android.play.core.tasks.*;** to **import com.google.android.gms.tasks.*;**.

## Use Case – Flutter Application

Since Flutter is a framework that caters to both Android and iOS, this scenario is a bit different from the one above. If you receive the warning to upgrade the core play library in your Flutter application, you need to have a look at the libraries you are using in your pubspec.yaml file:

```yaml
dependencies:
  flutter:
    sdk: flutter
  ...
  in_app_update: ^3.0.0
```

As you can see above, the application depends on the **in_app_update** library, which has to do with notifying users when a newer version of the application is available. When we head over to in_app_update’s pub.dev [changelog page](https://pub.dev/packages/in_app_update/changelog), we can see that:

![Image](https://www.freecodecamp.org/news/content/images/2024/06/1-1.jpg)
_version 4.1.0 added the required support_

So we need to update our pubspec.yaml file to use that version (at the very least).

```yaml
dependencies:
  flutter:
    sdk: flutter
  ...
  in_app_update: ^4.1.0
```

Run Pub get and you should be good to go.

