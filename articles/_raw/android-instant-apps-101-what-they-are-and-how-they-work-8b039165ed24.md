---
title: 'Android Instant Apps 101: what they are and how they work'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-28T21:56:05.000Z'
originalURL: https://freecodecamp.org/news/android-instant-apps-101-what-they-are-and-how-they-work-8b039165ed24
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tuoH_I8zkHA2f1PuqtIcfQ.jpeg
tags:
- name: Android
  slug: android
- name: Instant Apps
  slug: instant-apps
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Tomislav Smrečki

  Android Instant Apps are a cool new way to consume native apps without prior installation.
  Only parts of the app are downloaded and launched, giving the users a native look
  and feel in a couple of seconds.

  How do they work?

  First ...'
---

By Tomislav Smrečki

Android Instant Apps are a cool new way to consume native apps without prior installation. Only parts of the app are downloaded and launched, giving the users a native look and feel in a couple of seconds.

#### How do they work?

First of all, don’t confuse them with Progressive Web Apps where a launcher icon opens a web app via the Chrome browser. An Instant app will actually be installed on your phone, but without the need to search for it on the Play Store.

Web URLs will trigger the Google Play Store on your phone and fetch only the part of the app that is associated with the requested URL. The rest of the app is not downloaded. This way users can quickly enjoy the native experience of your Android application.

#### What’s the background?

Well, you need to divide your Android project into a couple of modules. One of them is a base module with the essential code which is used in all other modules (API connection, database, shared preferences etc.). The other, feature modules, contain specific functionalities and activities which can be accessed via associated URLs.

Let’s say you have a web app with a list of products and a single page of the product. For example, you can link [https://example.domain/products](https://example.domain/products) to launch the ProductsListActivity and [https://example.domain/products/12](https://example.domain/products/12) to launch the ProductActivity.

To make them accessible as instant app activities, they need to be packed into individual feature modules and they need to have associated App Links defined in their module manifests. We will call them Product and Product list modules.

Now, when a user tries to open [https://example.domain/products/12](https://example.domain/products/12,)[,](https://example.domain/products/12,) both Product and Base modules will start to download and the ProductActivity will be launched.

#### What are app links and how are they defined?

You’ve probably heard of deep links. They are defined in the app manifest, and they will be registered to the OS. When a user tries to open such a link, the OS will ask the user to choose between opening the link in a web browser or in your app. However, this is not enough for Instant apps, you need to go one step further — [App Links](https://developer.android.com/training/app-links/). You need to include the **autoVerify=”true”** property.

```
<activity android:name=".ProductActivity"> <intent-filter android:autoVerify="true" android:order="100"> 
```

```
<action android:name="android.intent.action.VIEW" /> <category android:name="android.intent.category.DEFAULT" /> <category android:name="android.intent.category.BROWSABLE" /> 
```

```
<data android:scheme="http"      android:host="example.domain"       android:pathPrefix="/products" /> <data android:scheme="https"/> 
```

```
</intent-filter> </activity>
```

Your app will [verify](https://developer.android.com/training/app-links/verify-site-associations) if the links you specified are really associated with your domain. For this, you need to include the **assetlinks.json** file into the following folder of your domain root:

[**https://example.domain/.well-known/assetlinks.json.**](https://example.domain/.well-known/assetlinks.json.)

Also, notice the **android:order=”100″** property. This is actually a priority in this case. If you have a product list and a product single that correspond to the same path **(/products and /products/10)**, the product single activity will be launched if there’s an id after the **/products** path. If not, then the product list activity is launched.

It is very important to define this. If there are two activities that correspond to the same path, the Play Store won’t know which part of the app should be fetched.

#### Associate your app with your domain

The **assetlinks.json** will need to contain your SHA256 keystore hashes. The relation field is set to the default value below, and the target object needs to be filled with app specific data and your SHA256 hash of the keystore.

```
[{   "relation": ["delegate_permission/common.handle_all_urls"],  "target": {   "namespace": "android_app",   "package_name": "com.example.app",   "sha256_cert_fingerprints":["00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00"]   } }]
```

When **autoVerify=true** does its magic, all associated App Links will directly launch your app. If you don’t have the app installed, the instant app will be downloaded instead.

Here’s an example of a demo app we did recently. When clicked on the associated link, a screen like this opens and offers to use the instant app instead. Note how quickly the app is opened, and on Oreo it’s even faster.

#### How to Define Android Instant Modules?

For an instant app, your project will consist of at least three different modules. You need to use Android Studio 3.0 for this. If you’re creating your app from scratch, there’s an option to enable the Instant app support for your project.

All of the following modules will be initialised automatically. If you’re modifying an older app, you’ll need to break the old app module into a single base module and a couple of feature modules. Also, you’ll need to create an App and an Instant app module, which you will use to build both regular and instant app APKs.

**App Module**

First, you have to create an app module which defines the dependencies for all other modules (base + feature modules). In the build.gradle file of this module, you will need to define the following:

```
apply plugin: 'com.android.application' ...
```

```
dependencies {   implementation project(':product')   implementation project(':productlist')   implementation project(':base') }
```

**Base Module**

In this module, you will define the following dependency statements. Also, make sure that the **‘com.android.feature’** plugin is applied here.

```
apply plugin: 'com.android.feature' android {  baseFeature true   ... } 
```

```
dependencies {   api 'com.android.support:appcompat-v7:26.0.1'   api 'com.android.support.constraint:constraint-layout:1.0.2'  implementation 'com.google.firebase:firebase-appindexing:11.0.4'  application project(':app')   feature project(':product')   feature project(':productlist') }
```

Note that here, the compile statements become API statements for the regular dependencies we used before. The application project and feature projects are defined separately.

**Feature Module**

This module will have the following setting, also with the **com.android.feature** plugin applied.

```
apply plugin: 'com.android.feature' ... dependencies {   implementation project(':base')   ... }
```

You need to state which module is your base module and include it with the implementation project statement. Next, you can include the dependencies which are required only for this specific module. For example, if you’re using an animation library which is not used in any of the other modules.

**Instant App Module**

Finally, now there’s a **com.android.instantapp** plugin to be included in the **build.gradle** file for the instantapp module.

```
apply plugin: 'com.android.instantapp' dependencies {   implementation project(':product')   implementation project(':productlist')   implementation project(':base') }
```

In this module, we will define which modules will be built as instant apps. The result of the instantapp module build is a zip file with the instant app APKs which you can upload separately to Google Play Store in the Android Instant Apps release manager. These APKs are handled similarly as the regular ones, they have their own rollout history and versioning.

That’s it! It’s fairly simple to start developing Android Instant Apps. But, there’s always a but!

#### What were the Android Instant Apps’ challenges?

First of all, the Instant Apps are not enabled by default for now. If you want to try it, you need to check your phone settings under Google account and enable the Instant Apps setting.

Next, we found that it’s extremely important to specify app links data in the following format:

```
<intent-filter android:autoVerify="true"> ... <data android:scheme="http"   android:host="example.domain"   android:pathPrefix="/products" /> <data android:scheme="https"/> </intent-filter>
```

Both http and https schemes need to be defined as shown in this code snippet. Any other way would cause a link verification failure and the app wouldn’t be linked properly.

Also, there is a recommendation to include the following code snippet into one of the activities in your app manifest. This annotates which activity should be launched in case the Instant app is launched from the Settings or a system launcher.

```
<meta-data  android:name="default-url" android:value="https://example.domain" />
```

The official documentation states that the Google Search would offer Instant app annotation by default (small thunder icon), but we had problems with it. For our demo app, this was not the case. Google Search results didn’t annotate our demo links as Instant apps and the links led to the web page. Only if we tried to open the associated link from another app, like Gmail, the whole instant app process was triggered and the instant app was launched. Have you encountered any similar problems?

#### Conclusion

When first announced two years ago, I was very enthusiastic about Android Instant Apps. They respond to the problem of users having to search for the apps on the Store and wait till they’re downloaded to start using them. Web apps are much more accessible in that regard and the ease of discovery is much better.

Instant apps come really close to filling this gap between web and native mobile apps. They already act very well and I think that they will become more popular with time. The main problems we encountered was a rather small community and the lack of proper documentation, but the situation on that matter is also getting better.

We would love to hear from you if you’ve tried using them or had any challenges implementing them!

_Originally published at [www.bornfight.com](https://www.bornfight.com/blog/android-instant-apps-101/)._

