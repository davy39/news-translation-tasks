---
title: How to Build and Release a Flutter App in Google Play
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2023-08-30T14:23:42.000Z'
originalURL: https://freecodecamp.org/news/build-and-release-flutter-app-in-google-play
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/Build-and-Release-the-Flutter-App-in-Google-Play.png
tags:
- name: android app development
  slug: android-app-development
- name: Flutter
  slug: flutter
seo_title: null
seo_desc: "In the rapidly evolving world of mobile app development, Flutter has gained\
  \ immense popularity for its ability to create stunning and high-performance apps\
  \ across multiple platforms. \nFlutter's framework allows developers to build beautiful\
  \ user inte..."
---

In the rapidly evolving world of mobile app development, Flutter has gained immense popularity for its ability to create stunning and high-performance apps across multiple platforms. 

Flutter's framework allows developers to build beautiful user interfaces, deliver native performance, and streamline development. 

In this tutorial, I will walk you through building and releasing a Flutter app on the Android platform, from setting up your development environment to distributing your app on the Google Play Store.

## Prerequisites:

1. **Install Flutter and Dart:** Make sure you have Flutter and Dart installed on your machine. Follow the [official Flutter installation guide](https://docs.flutter.dev/get-started/install) for your platform.
2. **Android Studio:** Download and install Android Studio, which comes with useful tools for Android app development.
3. **Google Play Developer Account:** Create an account on the Google Play Console to publish your app on the Play Store.

## How to Develop your app

In this guide, I'll be building and releasing a [simple todo app](https://www.freecodecamp.org/news/learn-state-management-in-flutter/) I built in one of my earlier blogs.

However, you can follow along with this tutorial and release your own app based on what you build. 

As a learner, and if you want to experience the app releasing process, this will be good practice for you.

Run the following command to clone my repo:

```
git clone https://github.com/5minslearn/Flutter-Todo-App
```

Before proceeding with the app-building process, it's crucial to ensure that our app runs smoothly on a simulator or a physical device, without encountering any errors. 

Open the repo in VS Code and press F5 to run the app on your phone / emulator. 

## How to Customize the Default Launcher Icon in Flutter

When a new Flutter app is created, it has a default launcher icon. 

To customize this icon we need to follow the steps below: 

1. You can create your own icon by following this [guideline](https://m3.material.io/styles/icons).
2. In the `[project]/android/app/src/main/res/` directory, place your icon files in folders. The default `mipmap-` folders demonstrate the correct naming convention.
3. In `AndroidManifest.xml, update the application tags` `android:icon` attribute to reference icons from the previous step (for example, `<application android:icon="@mipmap/custom_icon" ...`).

I created an icon named `custom_icon.xml` with multiple resolutions (`mdpi` , `hdpi`, `xhdpi`, `xxhdpi`, `xxxhdpi`):

```
48 × 48 (mdpi)
72 × 72 (hdpi)
96 × 96 (xhdpi)
144 × 144 (xxhdpi)
192 × 192 (xxxhdpi)
```

I also placed each icon in the respective `mipmap-` folder. And finally, I mentioned them in the `AndroidManifest.xml`:

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-169.png)
_Updating custom_icon in AndroidManifest.xml_

```
<manifest xmlns:android="http://schemas.android.com/apk/res/android" package="com.example.todo" >
    <application
        android:label="todo"
        android:name="${applicationName}"
        android:icon="@mipmap/custom_icon">
        .....
        .....
    </application>
</manifest>

```

I am utilizing `ColorControlNormal` in my custom icon file (`custom_icon.xml`):

```
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="48dp"
    android:height="48dp"
    android:viewportWidth="960"
    android:viewportHeight="960"
    android:tint="?attr/colorControlNormal">
  <path
      android:fillColor="@android:color/white"
      android:pathData="M380,....,453.5Q592,463 613,483Z"/>
</vector>

```

**`colorControlNormal`** is a value that refers to a color attribute that is resolved at runtime, allowing the drawable to match the color theme of the app.

As I'm using an older API version, this function isn't accessible within the older API. 

As a solution, I've included the `appcompat` library in my `app/build.gradle` file: 

```
...
dependencies {
    ....
    implementation 'androidx.appcompat:appcompat:1.3.1'
    ....
}
....
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-146.png)
_Implement appcombat library in `build.gradle`_

That's it. Our configurations are done. Let's try to run the app and look at the icon in the device.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-168.png)
_App Icon Changed for Todo App_

The one with the rabbit's face is the one I created. It has been successfully applied to our app. 

Without any delay, let's get into building our Android application.

## What is a Keystore and Why DO You Need it in Flutter?

A keystore in Flutter, specifically for Android, is a secure container used to store cryptographic keys and certificates. 

It's important to maintain the security of your app, especially when dealing with sensitive information such as API keys, authentication tokens, and encryption keys. 

The keystore ensures that these sensitive assets are stored in a way that makes them difficult to extract from the device.

### Security

Storing sensitive information in a Keystore ensures that it is protected from unauthorized access, even if the device is compromised.

### Compliance

Many regulations require apps to protect sensitive data. A keystore helps you meet compliance standards.

### Encryption

If your app uses encryption, the keystore provides a secure location for storing encryption keys.

### Credentials

If your app communicates with APIs or services that require credentials, using a keystore can prevent those credentials from being easily extracted.

## How to Create a Keystore in Flutter

To create a Keystore, you typically use the keytool utility that comes with the Java Development Kit (JDK):

```
keytool -genkey -v -keystore my-release-key.jks -keyalg RSA -keysize 2048 -validity 10000 -alias my-key
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-170.png)
_Sample output for generate a keystore file_

## **How to Generate APK or AAB in Flutter**

APK (Android Package) and AAB (Android App Bundle) are distribution formats used to package and distribute Android applications. 

It is recommended to build an app as AAB over APK due to the following benefits:

* Smaller downloads and faster installations due to optimized APKs
* Improved efficiency in resource usage and reduced storage consumption
* Dynamic feature delivery support for delivering features on-demand
* Enhanced optimization for specific device configurations

```
flutter build appbundle
or
flutter build apk
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-171.png)
_Sample output to build abb_

We cannot directly install an Android App Bundle (AAB) file on a mobile device.

An AAB is not an executable package like an APK (Android Package) file that can be directly installed on a device. 

Instead, the AAB is a publishing format designed for optimized delivery on the Google Play Store.

When you publish your app on the Google Play Store using an AAB, the Play Store uses it to generate APKs that are tailored to each user's device configuration. 

This dynamic generation allows the Play Store to deliver only the necessary resources and code for a specific device, reducing the app's size and improving performance during installation.

## How to Release a Flutter App on Google Play Store

To release our app on the Google Play Store, we'll require a Google Play developer account. We can create an account by visiting this [link](https://play.google.com/console). 

Please be aware that there is a registration fee of at least $25 associated with the process.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-150.png)
_Google play dashboard to create a new App_

Click on the Create app button in the `All apps` section. Enter the app details in the "Create app" form.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-149.png)
_Creating an app in Google play for release_

After creating the app, we have to go through multiple tasks to release the application. 

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-151.png)
_Steps to testing the app in Goole Play Console_

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-152.png)
_Steps to setting up the app in Goole Play Console_

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-153.png)
_Steps to release the app in Goole Play Console_

However, all these steps will be self-explanatory. 

At each step, you'll be prompted for information about your application, advertisements, privacy policy, and more. 

It's important to note that you can proceed to publish only after completing these steps. 

Make sure to mention everything clearly. Especially the questions about data collection. Because, at any time if Google found that your prescribed information is wrong, your app will not be published or will be taken out, if it's published. 

After completing these steps, we have to send the app for review. Our app will be published once the review is completed from Google Play team. 

It's important to note that there's a higher chance of the app getting rejected if it has security or advertising-related issues. 

Therefore, make sure to thoroughly review your app to ensure that it doesn't have any potential problems in data collection. This will contribute to a smoother and more successful app release experience.

## Conclusion

Throughout this tutorial, we've covered the process of changing the app icon and building a Flutter app for Android. 

While this example provides a foundational understanding of Flutter app development, it's important to note that real-world app complexities may require additional custom configurations in Android. 

For further insights, I encourage you to explore the official [documentation](https://docs.flutter.dev/deployment/android), which offers comprehensive guidance on more advanced aspects.

I hope this tutorial has provided you with valuable insights in your Flutter journey.

Thank you for investing your time, and best of luck in your app development endeavors! 

If you wish to learn more about Flutter, subscribe to my article by visiting my [site](https://5minslearn.gogosoon.com/?ref=fcc_flutter_publish_app) which has a consolidated list of all my blogs.

Cheers! 


