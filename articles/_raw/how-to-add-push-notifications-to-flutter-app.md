---
title: How to Add Push Notifications to a Flutter App using Firebase Cloud Messaging
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-12-09T19:57:23.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-push-notifications-to-flutter-app
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5fd0362ce6787e098393c56a.jpg
tags:
- name: Firebase
  slug: firebase
- name: Flutter
  slug: flutter
- name: messaging
  slug: messaging
- name: push notification
  slug: push-notification
seo_title: null
seo_desc: 'By Krissanawat

  Flutter has quickly become one the most popular frameworks for cross-platform mobile
  application development. It helps developers build native UIs with support for different
  device sizes, pixel densities, and orientations creating a be...'
---

By Krissanawat

Flutter has quickly become one the most popular frameworks for cross-platform mobile application development. It helps developers build native UIs with support for different device sizes, pixel densities, and orientations creating a beautiful pixel-perfect UI/UX. 

In this tutorial, we are going to learn how to add push notifications to a Flutter app using Firebase Cloud Messaging. This tutorial will only deal with configuration for the **Android platform**.

### First, what are push notifications?

Push Notifications are a sort of pop-up messaging medium that alerts app users to what's going on in the app. They are also an important way to amplify user engagement in your app. 

For example, say a user forgets about the app once they have installed it. Then you can use push notifications as a mechanism to regain and retain their interest. Push notifications also help drive traffic to your app. 

Firebase Cloud Messaging is a service offered by Firebase which lets you send these notifications to your users. You can set up various configurations to send different notifications to different audiences based on time and routine. 

Because of all these benefits, we are going to use it to send notifications to our Flutter app.

## Step 1: Create a Flutter Project

First, we are going to create a flutter project. For that, we must have the Flutter SDK installed in our system. You can find simple steps for flutter installation in the official [documentation](https://flutter.dev/docs/get-started/install). 

After you've successfully installed Flutter, you can simply run the following command in your desired directory to set up a complete Flutter project:

```jsx
flutter create pushNotification

```

After you've set up the project, navigate inside the project directory. Execute the following command in the terminal to run the project in either an available emulator or an actual device:

```bash
flutter run

```

After a successful build, you will get the following result in the emulator screen:

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-69.png)

## Step 2: Integrate Firebase Configuration with Flutter

In this step, we are going to integrate Firebase services with our Flutter project. But first, we need to create a Firebase project. The setup guidelines are also provided in the official [firebase documentation](https://firebase.google.com/docs/flutter/setup?platform=android) for Flutter.

To create a Firebase project, we need to log in to [Firebase](https://firebase.google.com/) and navigate to the console. There we can simply click on 'Add a project' to get our project started.

Then a window will appear asking to input the project's name. Here, I've kept the project name as `FlutterPushNotification` as shown in the screenshot below:

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-70.png)

We can continue to the next step when the project has been created. After the project has been set up, we will get a project console as shown in the screenshot below:

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-71.png)

Here, we are going to set up Firebase for the Android platform. So we need to click on the Android icon displayed in the above screenshot. This will lead us to the interface to register Firebase with our Flutter app project.

## Step 3: Register Firebase to Your Android App

As the registration process is platform-specific, we are going to register our app for the Android platform. After clicking on the Android icon, we will be directed to an interface asking for the **Android package name**. 

In order to add the package name of our Flutter project, we need to locate it first. The package name will be available in the **./android/app/build.gradle** file of your Flutter project. You will see something like this:

```jsx
com.example.pushNotification

```

We just need to copy it and paste it to the Android package name input field as shown in the screenshot below:

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-72.png)

After that, we can simply click on the 'Register app' button. This will lead us to the interface where we can get the **google-services.json** file which will link our Flutter app to Firebase Google services. 

We need to download the file and move it to the **./android/app** directory of our Flutter project. The instructions are also shown in the screenshot below:

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-73.png)

## Step 4: Add Firebase Configurations to Native Files in your Flutter Project

Now in order to enable Firebase services in our Android app, we need to add the [google-services plugin](https://developers.google.com/android/guides/google-services-plugin) to our Gradle files.

First in our **root-level (project-level)** Gradle file (**android/build.gradle**), we need to add rules to include the Google Services Gradle plugin. We need to check if the following configurations are available or not:

```jsx
buildscript {
  repositories {
    // Check that you have the following line (if not, add it):
    google()  // Google's Maven repository
  }
  dependencies {
    ...
    // Add this line
    classpath 'com.google.gms:google-services:4.3.4'
  }
}

allprojects {
  ...
  repositories {
    // Check that you have the following line (if not, add it):
    google()  // Google's Maven repository
    ...
  }
}

```

If not, we need to add the configurations as shown in the code snippet above.

Now in our module (app-level) Gradle file (**android/app/build.gradle**), we need to apply the **Google Services Gradle** plugin. 

For that, we need to add the piece of code highlighted in the following code snippet to the **./android/app/build.gradle** file of our project:

```jsx
// Add the following line:
**apply plugin: 'com.google.gms.google-services'**  // Google Services plugin

android {
  // ...
}

```

Now, we need to run the following command so that some automatic configurations can be made:

```jsx
flutter packages get

```

With that we have successfully integrated Firebase configurations with our Flutter project.

## Step 5: Integrate Firebase Messaging with Flutter

First, we need to add the firebase-messaging dependency to the **./android/app/build.gardle** file. In the file, we need to add the following dependencies:

```dart
dependencies {
    implementation "org.jetbrains.kotlin:kotlin-stdlib-jdk7:$kotlin_version"
    implementation 'com.google.firebase:firebase-messaging:20.1.0'
}

```

Next, we need to add an `action` and a `category` as an `intent-filter` within the `activity` tag in the **./android/app/src/main/AndroidManifest.xm**l file:

```xml
<intent-filter>
    <action android:name="FLUTTER_NOTIFICATION_CLICK" />
    <category android:name="android.intent.category.DEFAULT" />
</intent-filter>

```

Now, we need to create a Java file called **Application.java** in the path **/android/app/src/main/java/<app-organization-path>**.

Then, we need to add the code from the following code snippet inside it:

```java
package io.flutter.plugins.pushNotification;

import io.flutter.app.FlutterApplication;
import io.flutter.plugin.common.PluginRegistry;
import io.flutter.plugin.common.PluginRegistry.PluginRegistrantCallback;
import io.flutter.plugins.GeneratedPluginRegistrant;
import io.flutter.plugins.firebasemessaging.FirebaseMessagingPlugin;
import io.flutter.plugins.firebasemessaging.FlutterFirebaseMessagingService;

public class Application extends FlutterApplication implements PluginRegistrantCallback {
    @Override
    public void onCreate() {
        super.onCreate();
        FlutterFirebaseMessagingService.setPluginRegistrant(this);
    }

    @Override
    public void registerWith(PluginRegistry registry) {
        FirebaseMessagingPlugin.registerWith(registry.registrarFor("io.flutter.plugins.firebasemessaging.FirebaseMessagingPlugin"));
    }
}

```

Now, we need to assign this `Application` activity to the `application` tag of the **AndroidManifest.xml** file as shown in the code snippet below:

```xml
<application
        android:name=".Application"

```

This completes our setup of the Firebase messaging plugin in the native Android code. Now, we'll move on to the Flutter project.

## Step 6: Install the Firebase Messaging Package

Here, we are going to use the `[firebase_messaging`] package, which [you can find here](https://pub.dev/packages/firebase_messaging/). For that, we need to add the plugin to the dependency option of the pubspec.yaml file. 

We need to add the following line of code to the dependencies option:

```yaml
firebase_messaging: ^7.0.3

```

## Step 7: Implement a Simple UI Screen

Now, inside the `MyHomePage` stateful widget class of the **main.dart** file, we need to initialize the `FirebaseMessaging` instance and some constants as shown in the code snippet below:

```dart
String messageTitle = "Empty";
String notificationAlert = "alert";

FirebaseMessaging _firebaseMessaging = FirebaseMessaging();

```

The `messageTitle` variable will receive the notification message title and `notificationAlert` will be assigned the action that's been completed once the notification comes up.

Now, we need to apply these variables to the build function inside the `Scaffold` widget body as shown in the code snippet below:

```dart
Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text(
              notificationAlert,
            ),
            Text(
              messageTitle,
              style: Theme.of(context).textTheme.headline4,
            ),
          ],
        ),
      ),
    );
  }

```

Next, we need to run the Flutter application by executing the following command in the project terminal:

```bash
flutter run

```

We will get the result you see in the image below:

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-74.png)

For now, the notification title is empty, and the alert is also as defined. We need to assign a proper value to them once we receive the notification message.

So we need to configure the code to receive the notification and use the notification message to display it on the screen.

For that, we need to add the code from the following code snippet in the `initiState` function:

```dart
@override
  void initState() {
    // TODO: implement initState
    super.initState();

    _firebaseMessaging.configure(
      onMessage: (message) async{
        setState(() {
          messageTitle = message["notification"]["title"];
          notificationAlert = "New Notification Alert";
        });

      },
      onResume: (message) async{
        setState(() {
          messageTitle = message["data"]["title"];
          notificationAlert = "Application opened from Notification";
        });

      },
    );
  }

```

Here, we have used the `configure` method provided by `_firebaseMessaging` instance which in turn provides the `onMessage` and `onResume` callbacks. These callbacks provide the notification `message` as a parameter. The `message` response will hold the notification object as a map object.

The `onMessage` function triggers when the notification is received while we are running the app. The `onResume` function triggers when we receive the notification alert in the device notification bar and opens the app through the push notification itself. In this case, the app can be running in the background or not running at all.

Now we are all equipped with the Flutter app. We just need to configure a message in Firebase Cloud Messaging and send it to the device.

## Step 8: Create a Message from the Firebase Cloud Messaging Console

First, we need to go back to the Cloud Messaging console in the Firebase site as shown in the image below:

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-75.png)

Here, we can see the 'Send your first message' option in the window, as we have not configured any messages before. We need to click on it which will lead us to the following window:

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-76.png)

Here, we can enter the title, text, image, and name of the notification. The title we set here will be provided as the title in the `message` object on the callbacks we set before in the Flutter project.

After setting the required fields, we can click on 'Next' which will lead us to the following window:

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-77.png)

Here, we need to provide our target app and click on 'Next'.

For Scheduling we can keep the default option:

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-78.png)

Next, the Conversion window will appear which we can keep as default as well, and then click on the 'Next' button.

Lastly, a window where we need to enter the custom data will appear in which we can set the `title` and `click_action`. This click action event is triggered whenever we click on the notification that appears in the notification bar of the device. 

After clicking on the notification message from the notification bar, the app will open and the `onResume` callback will trigger, setting `title` as assigned in the custom data in the screenshot below:

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-79.png)

Now, we are ready to send the first notification message to the device. First, let's try it with the device running in the emulator.

As we click on the 'Review' button and send the message, we will get the following result in the Cloud Messaging console as well as the emulator:

![Image](https://www.freecodecamp.org/news/content/images/2020/12/pushGIF1.gif)

Here, we can see that the title and the notification alert on the emulator screen are updated as soon as we send a message from the console. We can be sure that the `onMessage` callback was triggered in the app after receiving the notification message.

Now let's try with the app running in the background. As we send the message from the console, we will get the result as shown in the demo below:

![Image](https://www.freecodecamp.org/news/content/images/2020/12/pushGIF2.gif)

Here, as soon as we send the message, we receive a push notification in the notification bar of the device. Then, as we drag down the notification bar, we can see the notification message title and text. And, by clicking on the notification message, we can launch the application and display the custom data on the screen. This ensures that our `onResume` callback was triggered.

And we're done! We have successfully added a push notification feature in our Flutter application using Firebase Cloud Messaging.

## Conclusion

Push notifications are essential in any app. They can be used to alert users to what's going on in the app, and can help drive users' interest back to the app. 

Additionally, Firebase Cloud Messaging makes sending notification alerts much simpler and easier. 

In this tutorial, we started by configuring the Firebase app and then moved on to the setup and implementation of the Firebase messaging configuration in the Flutter app. Lastly, we were able to send notification alerts to the app using Firebase Cloud Messaging. 

The tutorial was meant to be simple and easy to understand. Hope that it helps you add push notification to your Flutter apps. Want to see some examples of how you can implement all this? Check out these powerful [Flutter templates](http://instaflutter.com).

