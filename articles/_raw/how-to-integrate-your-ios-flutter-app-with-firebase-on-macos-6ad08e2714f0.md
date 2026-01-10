---
title: How to integrate your iOS Flutter App with Firebase on MacOS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-28T18:06:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-integrate-your-ios-flutter-app-with-firebase-on-macos-6ad08e2714f0
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e6d740569d1a4ca3d06.jpg
tags:
- name: Firebase
  slug: firebase
- name: Flutter
  slug: flutter
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Shen Huang

  Firebase is a mobile app development platform developed by Firebase, Inc. in 2011,
  and then Acquired by Google in 2014. It provides various features such as Cloud
  Storage, Authentication and an ML kit, which are essential to developing ...'
---

By Shen Huang

Firebase is a mobile app development platform developed by Firebase, Inc. in 2011, and then Acquired by Google in 2014. It provides various features such as Cloud Storage, Authentication and an ML kit, which are essential to developing modern mobile applications. 

Additionally, it provides services such as Performance Monitoring, Crashlytics and Google Analytics to help you improve the quality of your applications.

![Image](https://cdn-media-1.freecodecamp.org/images/rdJbjlOjN0qrQOz1vVGAhz5Ndy3JltvhJWIt)
_App Success Made Simple with Firebase_

In this tutorial I am going to show you how to connect your Flutter iOS application to the Firebase Platform on a Mac Computer, so you can utilize the powerful services provided by the firebase API in your future endeavors…

### 1. Readying a Gmail Account and a Flutter Project

In order to utilize services from Firebase and Google Cloud Platform, you will need a Google Account. If you do not have one, simply following the page instructions [**here**](https://accounts.google.com/signup/v2/webcreateaccount?hl=en-GB&flowName=GlifWebSignIn&flowEntry=SignUp) to register for one.

This tutorial is going to show you how to connect your existing Flutter application to the Firebase platform. If you are interested in how to create your first Flutter application, I have a tutorial on [**How to create your first iOS Flutter app on MacOS**](https://medium.com/front-end-weekly/how-to-create-your-first-ios-flutter-app-on-macos-7dfa9c3e1962). By the end of that tutorial, you should have a **_hello_world_** application ready in the simulator and understand how to alter the application by modifying the **_main.dart_** file.

### 2. Creating a Firebase Project

In order to integrate your Flutter application with the Firebase Platform, first you have to create a Firebase Project. And here are the steps.

1. Go to the [**Firebase Console**](https://console.firebase.google.com/).

2. Click on the big **Add project** button.

![Image](https://cdn-media-1.freecodecamp.org/images/bBzkYgbreUqtXjaF8gHm459WoBGG2iFVJ8zq)

3. Enter your **Project name**.

* I used **_hello-world_** for this example. Firebase automatically appends a unique ID to your project name — for example, the project I created ended up with the name **_hello-world-f2206_**.

4. You can pick a **_Cloud Firestore_** Location.

* I left it as _nam5 (us-central)_ because I live in Los Angeles, but the Cloud Functions are not available on _us-west2_, and the traffic in between will create additional charges. You can find more about service availabilities and server locations [**here**](https://cloud.google.com/about/locations/).

5. Accept the **Terms and Conditions**.

![Image](https://cdn-media-1.freecodecamp.org/images/B5rzqO7YzxBfcTPpL0-SpWj-Opi1dF0FH0h2)

5. Once you are done, scroll to the bottom and click **Create Project**.

![Image](https://cdn-media-1.freecodecamp.org/images/vEG0IraiNoAedcBgHK8T-Iixohwr4-Jvfete)

* See **3.1 Switching to Administrator Account** in the appendix at the end of this article if you encountered an error message asking for an administrator account.

Firebase will take some time to ready your application. Once done, click on the **Continue** button to open up the **Firebase Project Overview Page**.

![Image](https://cdn-media-1.freecodecamp.org/images/juqNs74YCpoCTwiGiwLfNwIhfcwHUsBS7K7D)

#### 4. Configure an iOS Application

1. In your **Firebase Project Overview Page**, launch the setup wizard for **iOS**.

![Image](https://cdn-media-1.freecodecamp.org/images/0oBCTTpEkwEKdWeJx0q8L3eFiUFBbzQj8BPj)

2. Inside the setup wizard, put in the **iOS bundle ID.** The **Register app** button should then light up, click on it.

* A guide on how to find the iOS bundle ID can be found the below in section **4.1 Finding iOS Project root folder & Acquiring Bundle ID** of the appendix.

![Image](https://cdn-media-1.freecodecamp.org/images/AC5HOfe1A3qBExHbEAi3quD3BI7-5FUU9Em5)

3. Download the **_GoogleService-Info.plist_** configuration file and put it into the iOS Project root folder, then click **Next**.

* A guide on how to find the iOS bundle ID can be found below in section **4.1 Finding iOS Project root folder & Acquiring Bundle ID** of the appendix.

![Image](https://cdn-media-1.freecodecamp.org/images/DgXQCKfCZ84AZL5gwAiitFHrpzhw1Jkw4ftA)

4. Follow the instructions to add the **Firebase SDK**, then click **Next**.

![Image](https://cdn-media-1.freecodecamp.org/images/cBV0KNA7yJOUqXZltFjA7NvIJ1gnYIed64dI)

* A detailed guide on how to install **CocoaPods** and **Firebase SDK** can be found below in section **4.2 Installing CocoaPods and Firebase SDK**.

5. Modify the code inside the main **AppDelegate** as instructed by the setup wizard then click **Next**. For this example, I used **Objective-C**, and therefore replaced the contents inside **_AppDelegate.m_** with the following code.

```objectivec
#include "AppDelegate.h"
#include "GeneratedPluginRegistrant.h"

@import UIKit;
@import Firebase;

@implementation AppDelegate

- (BOOL)application:(UIApplication *)application
didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
[FIRApp configure];
return YES;
}

@end
```

![Image](https://cdn-media-1.freecodecamp.org/images/5agXkDqo0aAGpa6N9ZLWgn3oN710M9c5Z2fj)

6. Get back to the root folder and run your app, after a while you should see the setup wizard showing that your app is added to Firebase. Click **Continue to the Console** to finish the setup.

![Image](https://cdn-media-1.freecodecamp.org/images/p5ODqX7TTswka1QMpu4r93k5G9AVHr0Si2kg)

![Image](https://cdn-media-1.freecodecamp.org/images/oBZf6Nqo-nvZTUORtvybrVv8Ia2aldKXnJq6)

Congratulations! You have successful added Firebase to your Flutter application. Despite the fact that having both Firebase and Flutter from Google is supper cool, it is actually a good Software Engineering practice to always have a plan B, as well as plan C, D,E, F, and G. In the future I will write another guide on an example application utilizing Firebase, and more on Flutter.

Have fun coding!!!

### Appendices:

#### 3.1 Switching to Administrator Account

If you ran into the following message, it means that you need to contact the organization of your Gmail account to grant you access to **Google Developers Console**.

![Image](https://cdn-media-1.freecodecamp.org/images/OCEEJckD9203lGfiVrwQavZ26GPzGdKIjscK)
_Request for Administrator Account_

#### 4.1 Finding iOS Project root folder & Acquiring Bundle ID

1. Launch **Xcode** from the **Launchpad**.

2. Select **“Open another project…”** at the bottom of the prompt screen.

![Image](https://cdn-media-1.freecodecamp.org/images/Wlr2j9zKkVEHwNQYdTI9wxWriKAMIvkmp8IQ)

3. Navigate to your Flutter project folder, open the **“ios”** folder and select **“Runner.xcodeproj”**. This should automatically open up the project in Xcode.

![Image](https://cdn-media-1.freecodecamp.org/images/oFjvHMqE4YtJiwfuSP55thHvD0GUjxEwY01x)

4. Select the **Runner** project on the left, you should now see the **Bundle Identifier** under **Identity**.

![Image](https://cdn-media-1.freecodecamp.org/images/kl55NJhmnZH74ihBKE-3fdrXeMmBysovfJ96)

#### **4.2 Installing CocoaPods and Firebase SDK**

In case the instructions inside the setup wizard did not work out, you will have to remove the existing Podfile in order to reinstall them correctly.

![Image](https://cdn-media-1.freecodecamp.org/images/o6kODHbEcH9JMV5gbf7FlBQKOVQnYlGPEuQn)

1. **CocoaPods** is built with **Ruby** and is installable with the default **Ruby** available on **MacOS**. Use the following commands to install it.

```bash
sudo gem install cocoapods
```

![Image](https://cdn-media-1.freecodecamp.org/images/EgRhnJPf9kSRicH5fKajuXeMcPOdKnVerKvw)

2. Initialize the **_Podfile_** with the following command.

```bash
pod init
```

3. Then, add the following code to the initialized **_Podfile_**.

```bash
pod 'Firebase/Core'
```

![Image](https://cdn-media-1.freecodecamp.org/images/zemw1-5IZvI5VkGO7mGO0aSySoY-t5KMQruW)

4. Once done, save the changes made to the **_Podfile_**, and install the **Firebase SDK** with the following command.

```bash
pod install
```

![Image](https://cdn-media-1.freecodecamp.org/images/VuguYbQEDy6r9EcMXQ2vDaeOcvgHBcumNllL)

5. After the installation, you will likely have to configure the **._xcconfig_** files. First you will have to copy the files from the **_Pods/Target Support Files/Pods-Runner_** folder to **_Flutter_** folder.

![Image](https://cdn-media-1.freecodecamp.org/images/3amfUm5sWKDF9bf-ed9tsbknTggn0vVCwxwf)

6. Then you will have to include them into the **_Debug.xcconfig_** and **_Release.xcconfig_** files inside the **_Flutter_** folder.

In **_Debug.xcconfig_**:

```
#include "Pods-Runner.debug.xcconfig"
```

![Image](https://cdn-media-1.freecodecamp.org/images/9zJj8Nyvi1mIWq7y3cfsa2uhBMbw4qOz6zm1)

In **_Release.xcconfig_**:

```
#include "Pods-Runner.profile.xcconfig"
#include "Pods-Runner.release.xcconfig"
```

![Image](https://cdn-media-1.freecodecamp.org/images/BlQuedQwnCZmIQl9PLgBhJL1ugr8VLoqDfPu)

