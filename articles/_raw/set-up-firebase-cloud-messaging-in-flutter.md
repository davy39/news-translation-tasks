---
title: How to Set Up Firebase Cloud Messaging in Flutter Using Firebase
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2023-07-05T16:38:21.000Z'
originalURL: https://freecodecamp.org/news/set-up-firebase-cloud-messaging-in-flutter
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/A-Complete-Guide-to-FCM-Integration-in-Flutter-Using-Firebase.png
tags:
- name: Android
  slug: android
- name: Firebase
  slug: firebase
- name: Flutter
  slug: flutter
- name: mobile app development
  slug: mobile-app-development
seo_title: null
seo_desc: "In today's highly competitive mobile app landscape, effectively engaging\
  \ your app's users and delivering timely information is key. \nFirebase Cloud Messaging\
  \ (FCM) is a powerful push notification service provided by Firebase. It offers\
  \ a seamless way..."
---

In today's highly competitive mobile app landscape, effectively engaging your app's users and delivering timely information is key. 

Firebase Cloud Messaging (FCM) is a powerful push notification service provided by Firebase. It offers a seamless way to connect with your app's users and keep them engaged. 

In this tutorial, we will delve into the integration of FCM in Flutter. We'll explore its benefits and showcase real-world examples of how it can enhance user engagement and improve app performance. 

## What is Firebase Cloud Messaging?

Firebase Cloud Messaging (FCM) provides a reliable and battery-efficient connection between your server and devices. It allows you to deliver and receive messages and notifications on iOS, Android, and the web at no cost. 

In this tutorial, we will explore the process of setting up and using Firebase Cloud Messaging (FCM) in Flutter using Firebase as the backend service. While the main focus will be on Android implementation, it's worth noting that the process is similar for iOS and Android (with a few configuration differences).

Here is what we'll cover:

1. How to create an app in Firebase
2. How to set up Firebase in Flutter
3. How to implement push notifications using FCM tokens

In this tutorial, you'll learn how to send a simple notification using Firebase to the app running in Flutter. Let's get started.

## How to Create an App in Firebase

I'll create a new project in the Firebase console to get started. I'll walk through the necessary steps, including project setup, how to configure Firebase Cloud Messaging, and how to get the required credentials and configuration files for our Flutter app.

Before creating the app you need to signup for the Firebase [console](https://console.firebase.google.com/) if you don't have an account. After sign up, try to create a project.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-292.png)
_Create a Project in Firebase_

It will take a little time to create a project.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-293.png)
_Creating project in Firebase_

After creating the project, it will redirect you to the project dashboard.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-2.png)
_Project Overview in Firebase Console_

Once you've created the project in Firebase console, it's time to get started with our Flutter app.

## How to Set Up Firebase in Flutter

I have created a simple Flutter project using Visual Studio Code. If you are unfamiliar with building a Flutter project, you can refer to my [previous tutorial](https://www.freecodecamp.org/news/how-to-build-a-simple-login-app-with-flutter/). (If you are already familiar, you can skip this step.)

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-296.png)
_Simple Flutter Application running on Android Device_

Let's integrate Firebase into our Flutter project. To do this, we need a Firebase CLI command line tool. I have already installed the Firebase CLI. If you haven't done this, you can refer to the official [documentation](https://firebase.google.com/docs/cli#setup_update_cli).

Then we need to log in to Firebase using Firebase CLI.

```
firebase login
```

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-305.png)
_Login to Firebase using FirebaseCLI_

This will navigate you to the browser to log in to Firebase. You'll be navigated back once the authentication is successfully completed.

After successful login, we need to install FlutterFire CLI. We can use the FlutterFire CLI to configure our Flutter apps to connect to Firebase. Run the following command to activate the FlutterFire CLI:

```
dart pub global activate flutterfire_cli
```

The FlutterFire CLI is a command-line interface tool that simplifies the integration of Firebase services into Flutter applications. It provides a convenient way to add, configure, and manage Firebase plugins in our Flutter project.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-306.png)
_Installing FlutterFireCLI_

The next step is to add `firebase_core` library to our Flutter project.

The following command will automatically add the `firebase_core` package as a dependency in your project's `pubspec.yaml` file and fetch the latest version of the package from `pub.dev`. After running this command, you can import the `firebase_core` package into the Dart files and use Firebase services in our Flutter app.

```
flutter pub add firebase_core
```

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-307.png)
_Installing Firebase Core package_

The `flutterfire configure` command is used to configure Firebase services in our Flutter project using the FlutterFire CLI. This command helps us set up Firebase authentication, Firestore, Cloud Messaging, and other Firebase services easily and efficiently.

```
flutterfire configure
```

The first step is to choose the project,

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-308.png)
_Connect Flutter App with Firebase app_

The next is to choose the platform. I am using it for Android here, so I choose Android.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-309.png)
_Choosing platform_

After the successful configuration, the Firebase App Id will be displayed.

Finally, we need to add some code changes to our `main.dart` file.

Import the following packages:

```
import 'package:firebase_core/firebase_core.dart';
import 'firebase_options.dart';
```

Add the following configuration to initialize the Firebase config inside the main function of the `main.dart` file.

```
await Firebase.initializeApp(
  options: DefaultFirebaseOptions.currentPlatform,
);
```

Alright, we have successfully completed the Firebase configuration in our Flutter app! Let's take a moment to celebrate this milestone. Configuring Firebase services is a crucial step in building powerful and feature-rich applications.

## How to Implement Push Notification using FCM Tokens

We'll implement the process of registering devices for push notifications and retrieving the unique FCM tokens assigned to each device. This step is crucial for sending targeted notifications to specific devices.

We'll dive into the implementation of sending push notifications to devices using Firebase Cloud Messaging. We'll explore how to structure and send notification messages from the Firebase console and demonstrate how to handle these messages within our Flutter app.

```
flutter pub add firebase_messaging
```

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-310.png)
_Installing firebse messaging Package_

Next, we need to trigger the `setAutoInitEnabled` function to enable automatic initialization of Firebase Cloud Messaging (FCM) in our Flutter app. This means that FCM will automatically initialize and retrieve a device token when the app starts. 

Add the following function call in the `main` method:

```
import 'package:firebase_messaging/firebase_messaging.dart';
...
...
await FirebaseMessaging.instance.setAutoInitEnabled(true);
```

Let's run our Flutter app and verify if we receive the notification.

Navigate to the Firebase [messaging console](https://console.firebase.google.com/project/_/messaging/?_gl=1*gqfrc0*_ga*NDUwNTM5NDI0LjE2ODgwNTc3NjQ.*_ga_CW55HF8NVT*MTY4ODA5ODkyMC4yLjEuMTY4ODEwMjY2NS4wLjAuMA..). As it is our first message, we need to select "Create your first campaign". Select "Firebase Notification messages" and click "Create".

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-311.png)
_Sample test messaging template_

Now we need to enter the notification title, text, and name for the message.

Then we can get the FCM token manually for testing purposes using the code below. To retrieve the current registration token for an app instance, call `getToken()` in the `main()` method. This method will ask the user for notification permissions if notification permission has not been granted. Otherwise, it returns a token or rejects if there's any error.

```
final fcmToken = await FirebaseMessaging.instance.getToken();
log("FCMToken $fcmToken");
```

Copy the FCM token printed on the console and paste it into the "Add an FCM registration token" input box.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-1.png)
_Sent test message using FCM Token_

Click on the Test button. The targeted client device (with the app in the background) should receive the notification.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image.png)
_Received push notification in android device_

Hurray! We got the notification on our Android device. If we click on the notification it will open the app by default.

When we tap a notification, the default behavior on both Android and iOS is to open the application. If the application is terminated, it will be started. If it is in the background, it will be brought to the foreground.

Here, we can see the basic configuration to initialize Firebase messaging.

`main.dart`

```

import 'package:flutter/material.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_messaging/firebase_messaging.dart';
import 'firebase_options.dart';

void main() async {
  runApp(const MyApp());
  await Firebase.initializeApp(
    options: DefaultFirebaseOptions.currentPlatform,
  );
  final fcmToken = await FirebaseMessaging.instance.getToken();
  await FirebaseMessaging.instance.setAutoInitEnabled(true);
  log("FCMToken $fcmToken");
}
```

## Conclusion

In this tutorial we have covered the essential steps for implementing push notifications in Flutter using Firebase Cloud Messaging (FCM). 

By following the outlined steps, you can set up Firebase, integrate it into your Flutter project, and implement push notification functionality. 

With the ability to send and receive notifications seamlessly, you can enhance the user experience and engage with your app's users effectively. Stay tuned for more advanced topics and features in future tutorials.

If you wish to learn more about Flutter, subscribe to my [email newsletter](https://5minslearn.gogosoon.com/?ref=fcc_flutter_firebase) ([https://5minslearn.gogosoon.com/](https://5minslearn.gogosoon.com/?ref=fcc_flutter_firebase)) and follow me on social media. 


