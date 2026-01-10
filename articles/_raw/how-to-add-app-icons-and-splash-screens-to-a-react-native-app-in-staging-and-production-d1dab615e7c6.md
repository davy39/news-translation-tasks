---
title: How to add app icons and splash screens to a React Native app in staging and
  production
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-24T20:08:55.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-app-icons-and-splash-screens-to-a-react-native-app-in-staging-and-production-d1dab615e7c6
coverImage: https://cdn-media-1.freecodecamp.org/images/0*JXVkvIcwnggBNCRp.jpg
tags:
- name: Apps
  slug: apps-tag
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Khoa Pham

  React Native was designed to be “learn once, write anywhere,” and it is usually
  used to build cross platform apps for iOS and Android. And for each app that we
  build, there are times we need to reuse the same code, build and tweak it a b...'
---

By Khoa Pham

React Native was designed to be “learn once, write anywhere,” and it is usually used to build cross platform apps for iOS and Android. And for each app that we build, there are times we need to reuse the same code, build and tweak it a bit to make it work for different environments. For example, we might need multiple skins, themes, a free and paid version, or more often different staging and production environments.

And the task that we can’t avoid is adding app icons and splash screens to our apps.

In fact, to add a staging and production environment, and to add app icons, requires us to use Xcode and Android Studio, and we do it the same way we do with native iOS or Android projects.

Let’s call our app `MyApp` and bootstrap it with `react-native init MyApp` . There will of course, be tons of [libraries](https://github.com/thekevinbrown/react-native-schemes-manager) to help us with managing different environments.

In this post, we will do just like we did with native apps, so that we know the basic steps.

### Build configuration, target, build types, production flavor, and build variant

There are some terminologies we needed to remember. In iOS, debug and releases are called [build configurations](https://developer.apple.com/library/archive/featuredarticles/XcodeConcepts/Concept-Build_Settings.html), and staging and production are called [targets](https://developer.apple.com/library/archive/featuredarticles/XcodeConcepts/Concept-Targets.html).

> A build configuration specifies a set of build settings used to build a target’s product in a particular way. For example, it is common to have separate build configurations for debug and release builds of a product.

> A target specifies a product to build and contains the instructions for building the product from a set of files in a project or work-space. A target defines a single product; it organizes the inputs into the build system — the source files and instructions for processing those source files — required to build that product. Projects can contain one or more targets, each of which produces one product

In Android, debug and releases are called build types, and staging and production are called product flavors. Together they form [build variants](https://developer.android.com/studio/build/build-variants).

> For example, a “demo” _product flavor_ can specify different features and device requirements, such as custom source code, resources, and minimum API levels, while the “debug” _build type_ applies different build and packaging settings, such as debug options and signing keys. The resulting build variant is the “demoDebug” version of your app, and it includes a combination of the configurations and resources included in the “demo” product flavor, “debug” build type, and `main/` source set.

### Staging and production targets in iOS

Open `MyApp.xcodeproj` inside `ios` using Xcode. Here is what we get after bootstrapping:

![Image](https://cdn-media-1.freecodecamp.org/images/aT6TxJtPwQZYaQFQdx5RRnMfT18AHhveEHoW)

React Native creates iOS and tvOS apps, and two test targets. In Xcode, a project can contain many targets, and each target means a unique product with its own build settings — Info.plist and app icons.

#### Duplicate target

If we don’t need the tvOS app, we can delete the `MyApp-tvOS` and `MyApp-tvOSTests` . Let’s use `MyApp` target as our production environment, and `right click -> Duplic`ate to make another target. Let’s call `it MyApp Stag`ing.

![Image](https://cdn-media-1.freecodecamp.org/images/5hHjVB8EwYB5quzM26IUy9DufaCXNiRjp2N3)

Each target must have unique bundle id. Change the bundle id of `MyApp` to `com.onmyway133.MyApp` and `MyApp Staging` to `com.onmyway133.MyApp.Staging`.

![Image](https://cdn-media-1.freecodecamp.org/images/g02pyEjScSy4RYD2BlxlqndP-czHtvanJ7K7)

#### Info.plist

When we duplicate `MyApp target` , Xcode also duplicates `Info.plist` into `MyApp copy-Info.plist` for the staging target. Change it to a more meaningful name `Info-Staging.plist` and drag it to the `MyApp` group in Xcode to stay organised. After dragging, `MyApp Staging` target can’t find the plist, so click `Choose Info.plist File` and point to the `Info-Staging.plist`.

![Image](https://cdn-media-1.freecodecamp.org/images/sKyaTbgpYQfP7hRLus8TNqKb9tbsEwfqjHRU)

#### Scheme

Xcode also duplicates the scheme when we duplicate the target, so we get `MyApp copy`:

![Image](https://cdn-media-1.freecodecamp.org/images/ipNpPhA6cf4n6riHzYOv6L3rARKgZX78F4eb)

Click `Manage Schemes` in the scheme drop-down to open Scheme manager:

![Image](https://cdn-media-1.freecodecamp.org/images/EwS7sAXkEYSz1dNAEDSAx5nXTtxgpdOrqW4W)

I usually delete the generated `MyApp copy` scheme, then I create a new scheme again for the `MyApp Staging` target. You need to make sure that the scheme is marked as Shared so that it is tracked into git.

![Image](https://cdn-media-1.freecodecamp.org/images/pubibFLRmRXA70peau6B-lCOTsezlSw7ph5E)

For some reason, the staging scheme does not have all the things set up like the production scheme. You can run into issues like `‘React/RCTBundleURLProvider.h’ file not found` or `[RN: ‘React/RCTBridgeModule.h’ file not found](https://github.com/onmyway133/notes/issues/380)` . It is because `React` target is not linked yet.

To solve it, we must disable `Parallelise Build` and add `React` target and move it above `MyApp Staging`.

![Image](https://cdn-media-1.freecodecamp.org/images/VhJq58o3EFkfP2OohZEOi2Mc6d2oDwcOdOE6)

#### Staging and production product flavors in Android

Open the `android` folder in Android Studio. By default there are only debug and release build types:

![Image](https://cdn-media-1.freecodecamp.org/images/LXNMq2Tdm4QFsoWCpw-SEgUkQsk9PsUOs0Od)

They are configured in the `app` module `build.gradle`:

```
buildTypes {    release {        minifyEnabled enableProguardInReleaseBuilds        proguardFiles getDefaultProguardFile("proguard-android.txt"), "proguard-rules.pro"    }}
```

First, let’s change application id to `com.onmyway133.MyApp` to match iOS. It is not required but I think it’s good to stay organised. Then create two product flavors for staging and production. For staging, let’s add `.Staging` to the application id.

From Android Studio 3, “all flavors must now belong to a named flavor dimension” — normally we just need default dimensions. Here is how it looks in `build.gradle` for our `app` module:

```
android {    compileSdkVersion rootProject.ext.compileSdkVersion    buildToolsVersion rootProject.ext.buildToolsVersion    flavorDimensions "default"
```

```
defaultConfig {        applicationId "com.onmyway133.MyApp"        minSdkVersion rootProject.ext.minSdkVersion        targetSdkVersion rootProject.ext.targetSdkVersion        versionCode 1        versionName "1.0"        ndk {            abiFilters "armeabi-v7a", "x86"        }    }    splits {        abi {            reset()            enable enableSeparateBuildPerCPUArchitecture            universalApk false  // If true, also generate a universal APK            include "armeabi-v7a", "x86"        }    }    buildTypes {        release {            minifyEnabled enableProguardInReleaseBuilds            proguardFiles getDefaultProguardFile("proguard-android.txt"), "proguard-rules.pro"        }    }
```

```
productFlavors {        staging {            applicationIdSuffix ".Staging"        }
```

```
        production {
```

```
        }    }}
```

Click `Sync Now` to let gradle do the syncing job. After that, we can see that we have four build variants:

![Image](https://cdn-media-1.freecodecamp.org/images/-nEATkMoAQykQ76AMDFzoYMzxU8DRidBmLm1)

#### How to run staging and production

To run the Android app, we can specify a variant like `react-native run-android — variant=productionDebug`, but I prefer to go to Android Studio, select the variant, and run.

To run iOS app, we can specify the scheme like `react-native run-ios — simulator=’iPhone X’ — scheme=”MyApp Staging”` . As of `react-native 0.57.0` this does not work. But it does not matter as I usually go to Xcode, select the scheme, and run.

#### Add app icon for iOS

According to the [Human Interface Guideline](https://developer.apple.com/design/human-interface-guidelines/ios/icons-and-images/app-icon/), we need app icons of different sizes for different iOS versions, device resolutions, and situations (notification, settings, Spring Board). I’ve crafted a tool called [IconGenerator](https://github.com/onmyway133/IconGenerator), which was previously mentioned in [Best Open Source Tools For Developers](https://dev.to/sarthology/best-open-source-tools-for-developers--300f). Drag the icon that you want — I prefer those with 1024x1024 pixels for high resolution app icons — to the Icon Generator MacOS app.

![Image](https://cdn-media-1.freecodecamp.org/images/8ptxiQkjwO8gYHh2l5hOQ7jalJ1vMjmLUgu2)

Click `Generate` and we get `AppIcon.appiconset` . This contains app icons of the required sizes that are ready to be used in Asset Catalog. Drag this to Asset Catalog in Xcode. That is for production.

For staging, it’s good practice to add a “Staging” banner so that testers know which is staging, and which is production. We can easily do this in Sketch.

![Image](https://cdn-media-1.freecodecamp.org/images/IZniQguM52R2egi9K3Q2RiSwDZJh1MGoIwQS)

Remember to set a background, so we don’t get a transparent background. For an app icon with transparent background, iOS shows the background as black which looks horrible.

After exporting the image, drag the staging icon to the IconGenerator the same way we did earlier. But this time, rename the generated `appiconset` to `AppIcon-Staging.appiconset`. Then drag this to Asset Catalog in Xcode.

For the staging target to use staging app icons, open `MyApp Staging target` and choose `AppIcon-Staging` as `App Icon Source`.

![Image](https://cdn-media-1.freecodecamp.org/images/gTgyPbp9meNYC3hGR14NOXkODGUCAXZuVwsg)

#### Add app icon for Android

![Image](https://cdn-media-1.freecodecamp.org/images/XsdkrkclUz4Anzqe2rkViump5lmveYWNo02c)

I like to switch to Project view, as it is easier to change app icons. Click `res -> New -> Image` Asset to open Asset Studio. We can use the same app icons that we used in iOS:

![Image](https://cdn-media-1.freecodecamp.org/images/40-HvrVL2bCPt8sYJEh0yIvwTQO-Us1MEpX7)

Android 8.0 (API level 26) introduced [Adaptive Icons](https://developer.android.com/guide/practices/ui_guidelines/icon_design_adaptive) so we need to tweak the Resize slider to make sure our app icons look as nice as possible.

> Android 8.0 (API level 26) introduces adaptive launcher icons, which can display a variety of shapes across different device models. For example, an adaptive launcher icon can display a circular shape on one OEM device, and display a squircle on another device. Each device OEM provides a mask, which the system then uses to render all adaptive icons with the same shape. Adaptive launcher icons are also used in shortcuts, the Settings app, sharing dialogs, and the overview screen. — [Android developers](https://developer.android.com/guide/practices/ui_guidelines/icon_design_adaptive)

We are doing for production first, which means the `main` Res Directory. This step will replace the existing placeholder app icons generated by Android Studio when we bootstrapped React Native projects.

![Image](https://cdn-media-1.freecodecamp.org/images/Ejg8cMXAsfFGELEFjuDrHpW8xiJjNjOKZCPI)

Now that we have production app icons, let’s make staging app icons. Android manages code and assets via convention. Click on `src -> New -> Dir`ectory and cre`ate a s`taging folder. Inside staging, create a folder c`all`ed res . Anything we pla`ce in s`taging will replace the on`es i`n main — this is c`alled sourc`e sets.

![Image](https://cdn-media-1.freecodecamp.org/images/kwh1pi0dNor35pcf8sIVw1jSE8fhoNmFp9qu)

You can read more here: [Build with source sets](https://developer.android.com/studio/build/build-variants).

> You can use source set directories to contain the code and resources you want packaged only with certain configurations. For example, if you are building the “demoDebug” build variant, which is the crossproduct of a “demo” product flavor and “debug” build type, Gradle looks at these directories, and gives them the following priority:

> `src/demoDebug/` _(build variant source set)_

> `src/debug/` _(build type source set)_

> `src/demo/` _(product flavor source set)_

> `src/main/` _(main source set)_

Right click on `staging/res -> New -> Image` Asset to make app icons for staging. We also use the same staging app icons like in iOS, but this time we c`hoose s`taging as Res Directory. This way Android Studio knows how to generate diff`erent ic_la`uncher and put them `into s`taging.

![Image](https://cdn-media-1.freecodecamp.org/images/ZDniqZf7J2-O9kGlNs4TCaK76wKrq5FWlLf4)

#### Add launch screen for iOS

The splash screen is called a [Launch Screen](http://Launch Screen) in iOS, and it is important.

> A launch screen appears instantly when your app starts up. The launch screen is quickly replaced with the first screen of your app, giving the impression that your app is fast and responsive

In the old days, we needed to use static launch images with different sizes for each device and orientation.

![Image](https://cdn-media-1.freecodecamp.org/images/vpvYxIfUWBNeC5qLkHAZu8LnIxPnUD5oi8UE)

#### Launch Screen storyboard

For now the recommended way is to use `Launch Screen storyboard` . The iOS project from React Native comes with `LaunchScreen.xib` but `xib` is a thing of the past. Let’s delete it and create a file called `Launch Screen.storyboard` .

Right click on `MyApp` folder -> New and chose Launch Screen, add it to both targets as usually we show the same splash screen for both staging and production.

![Image](https://cdn-media-1.freecodecamp.org/images/GeAUVDHsi4usmEM1WAOIYfNKCTfMdVnk6K9u)

![Image](https://cdn-media-1.freecodecamp.org/images/fET7YnCtOakmd6bxa9EINtjvBvWDLAfIZwnd)

#### Image Set

Open asset catalog, right click and select `New Image Set` . We can name it anything. This will be used in the `Launch Screen.storyboard`.

![Image](https://cdn-media-1.freecodecamp.org/images/FOAnVwAIPlu9Sw0xTw2DKDN-D9zFRhUrgJfo)

Open Launch Screen.storyboard and add an `UIImageView` . If you are using Xcode 10, click the Library button in the upper right corner and choose `Show Objects Library`.

![Image](https://cdn-media-1.freecodecamp.org/images/ElDQfbXBrCnkgUv1bdTbFeSjp1FD531aCLKQ)

Set image for Image View, and make sure `Content Mode` is set to `Aspect Filled`, as this ensures that the image always covers the full screen (although it may be cropped). Then connect ImageView using constraints to the `View`, not the `Safe Area`. You do this by `Control+drag` from the Image View (splash) to the `View`.

![Image](https://cdn-media-1.freecodecamp.org/images/djyPzopJFIhBCgNmR8NTzajn6yhiwWq1QCZF)

#### Constrains without margin

Click into each constraint and uncheck `Relative to Margin`. This makes our ImageView pin to the very edges of the view and with no margin at all.

![Image](https://cdn-media-1.freecodecamp.org/images/Ca4SGVE43ZoYt2vO9xzEhCEM5OwUtYmG9IhL)

Now go to both targets and select `Launch Screen.storyboard` as `Launch Screen File`:

![Image](https://cdn-media-1.freecodecamp.org/images/tWdkNOVF8YocN9aSArVkKyTeqoLT8LkVquci)

On iOS, the launch screen is often cached, so you probably won’t see the changes. One way to avoid that is to delete the app and run it again.

#### Add a launcher theme for Android

There are [several](https://android.jlelse.eu/the-complete-android-splash-screen-guide-c7db82bce565) [ways](https://android.jlelse.eu/right-way-to-create-splash-screen-on-android-e7f1709ba154) to add splash screen for Android, from using launcher themes, Splash Activity, and a timer. For me, a reasonable splash screen for Android should be a very minimal image.

As there are many Android devices with different ratios and resolutions, if you want to show a full screen splash image, it will probably not scale correctly for each device. This is just about UX.

For the splash screen, let’s use the launcher theme with `splash_background.xml` .

#### Learn about Device Metric

There is no single splash image that suits all Android devices. A more logical approach is to create multiple splash images for all common resolutions in portrait and landscape. Or we can design a minimal splash image that works. You can find more info here: [Device Metric](https://material.io/tools/devices/).

![Image](https://cdn-media-1.freecodecamp.org/images/7sCUEag7s1Bd6XQT5xUzl06wK0Fe8LMINn1f)

![Image](https://cdn-media-1.freecodecamp.org/images/W1QM52Nl-syNrLkP8DvrOtC3hc2pGVye2ZCK)

Here is how to add splash screen in 4 easy steps:

#### Add splash image

We usually need a common splash screen for both staging and production. Drag an image into `main/res/drawble` . Android Studio seems to have a problem with recognising some jpg images for the splash screen, so it’s best to choose png images.

#### Add splash_background.xml

`Right click on drawable -> New -> Drawable resourc`e file . Name it whatever you want — I c`hoose splash_backgrou`nd.xml . Choose the root eleme`nt as laye`r-list:

![Image](https://cdn-media-1.freecodecamp.org/images/ZpgiZzFrcfGgJ9z1PPdmrkrSU5CqIhEEeq1E)

![Image](https://cdn-media-1.freecodecamp.org/images/lCEe4-zJ4J3-xPuKXnG9TRbFqL1F0NpI8lxO)

A [Layer List](http://Layer List) means “a Drawable that manages an array of other Drawables. These are drawn in array order, so the element with the largest index is drawn on top”. Here is how `splash_background.xml` looks like:

```
<?xml version="1.0" encoding="utf-8"?><!-- The android:opacity=”opaque” line — this is critical in preventing a flash of black as your theme transitions. --><layer-list xmlns:android="http://schemas.android.com/apk/res/android"    android:opacity="opaque">    <!-- The background color, preferably the same as your normal theme -->    <item android:drawable="@android:color/white"/>    <!-- Your splash image -->    <item>        <bitmap            android:src="@drawable/iron_man"            android:gravity="center"/>    </item></layer-list>
```

Note that we point to our splash image we added earlier with `android:src=”@drawable/iron_man”`.

#### Declare style

Open `styles.xml` and add `SplashTheme`:

```
<style name="SplashTheme" parent="Theme.AppCompat.NoActionBar">    <item name="android:windowBackground">@drawable/splash_background</item></style>
```

#### `Use SplashTheme`

Go to `Manifest.xml` and change the theme of the the launcher activity, which has `category android:name="android.intent.category.LAUNCHER"` . Change it to `android:theme="@style/SplashTheme"` . For React Native, the launcher activity is usually `MainActivity` . Here is how `Manifest.xml looks`:

```
<manifest xmlns:android="http://schemas.android.com/apk/res/android"    package="com.myapp">    <uses-permission android:name="android.permission.INTERNET" />    <uses-permission android:name="android.permission.SYSTEM_ALERT_WINDOW"/>    <application      android:name=".MainApplication"      android:label="@string/app_name"      android:icon="@mipmap/ic_launcher"      android:allowBackup="false"      android:theme="@style/AppTheme">      <activity        android:name=".MainActivity"        android:label="@string/app_name"        android:configChanges="keyboard|keyboardHidden|orientation|screenSize"        android:theme="@style/SplashTheme"        android:windowSoftInputMode="adjustResize">        <intent-filter>            <action android:name="android.intent.action.MAIN" />            <category android:name="android.intent.category.LAUNCHER" />        </intent-filter>      </activity>      <activity android:name="com.facebook.react.devsupport.DevSettingsActivity" />    </application></manifest>
```

Run the app now and you should see the splash screen showing when the app starts.

### Managing environment configurations

The differences between staging and production are just about app names, application ids, and app icons. We probably use different API keys, and backend URL for staging and production.

Right now the most popular library to handle these scenarios is [react-native-config](https://github.com/luggit/react-native-config), which is said to “bring some 12 factor love to your mobile apps”. It requires lots of steps to get started, and I hope there is a less verbose solution.

#### Where to go from here

In this post, we touched Xcode and Android Studio more than Visual Studio Code, but this was inevitable. I hope this post was useful to you. Here are some more links to read more about this topic:

* [Add App Icons and Launch Screens to React Native Apps (iOS & Android)](https://medium.com/@scottianstewart/react-native-add-app-icons-and-launch-screens-onto-ios-and-android-apps-3bfbc20b7d4c)
* [How to Add a Splash Screen to a React Native App (iOS and Android)](https://medium.com/handlebar-labs/how-to-add-a-splash-screen-to-a-react-native-app-ios-and-android-30a3cec835ae)
* [Managing Configuration in React Native](https://medium.com/differential/managing-configuration-in-react-native-cd2dfb5e6f7b)
* [Adding multiple target pipelines for React Native Apps (and Fastlane CircleCI deployment) pt. 1](https://medium.com/@jacks205/adding-multiple-target-pipelines-for-react-native-apps-and-fastlane-circleci-deployment-pt-1-ae9590ae52f2)
* [The (Complete) Android Splash Screen Guide](https://android.jlelse.eu/the-complete-android-splash-screen-guide-c7db82bce565)

If you like this post, consider visiting [my other articles](https://github.com/onmyway133/blog/issues/165) and [apps](https://onmyway133.github.io/) ?

