---
title: How to get push notifications working with Ionic 4 and Firebase
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-25T14:27:04.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-push-notifications-working-with-ionic-4-and-firebase-ad87cc92394e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*EciBTQhuzIrkzA12dfsQJQ.jpeg
tags:
- name: Apps
  slug: apps-tag
- name: Firebase
  slug: firebase
- name: General Programming
  slug: programming
- name: push notification
  slug: push-notification
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Filip Jerga

  A full step-by-step tutorial that will get you on the right track for iOS and Android


  Setting up push notifications can be truly frustrating and time consuming. So I
  went through all of the setups and prepared this tutorial for you.

  P...'
---

By Filip Jerga

#### A full step-by-step tutorial that will get you on the right track for iOS and Android

![Image](https://cdn-media-1.freecodecamp.org/images/1*EciBTQhuzIrkzA12dfsQJQ.jpeg)

Setting up push notifications can be truly frustrating and time consuming. So I went through all of the setups and prepared this tutorial for you.

### Prerequisite

Ionic 4 should already be installed.

### Section navigation

1. [Package installation](https://www.freecodecamp.org/news/how-to-get-push-notifications-working-with-ionic-4-and-firebase-ad87cc92394e/#1-package-installation)
2. [Firebase setup for Android and iOS](https://www.freecodecamp.org/news/how-to-get-push-notifications-working-with-ionic-4-and-firebase-ad87cc92394e/#2-firebase-setup-for-ios-and-android)
3. [Push notification code implementation](https://www.freecodecamp.org/news/how-to-get-push-notifications-working-with-ionic-4-and-firebase-ad87cc92394e/#3-push-notification-code-implementation)
4. [Test push notifications on Android](https://www.freecodecamp.org/news/how-to-get-push-notifications-working-with-ionic-4-and-firebase-ad87cc92394e/#4-test-push-notifications-on-android)
5. [iOS push notification pre-setup](https://www.freecodecamp.org/news/how-to-get-push-notifications-working-with-ionic-4-and-firebase-ad87cc92394e/#5-ios-push-notification-pre-setup)
6. [Test push notifications on iOS](https://www.freecodecamp.org/news/how-to-get-push-notifications-working-with-ionic-4-and-firebase-ad87cc92394e/#6-test-push-notification-on-ios)

### 1. Package installation

Open your Ionic project in the coding editor of your choice, and open your terminal as well. Navigate to your project’s folder.

First, we will install all of the required packages.

**What we need to install:**

* **Cordova plugin for firebase:** `ionic cordova plugin add cordova-plugin-firebase`
* **Firebase native package:** since Ionic 4 is in beta, check your Ionic-native packages in `package.json` and install the same version as other Ionic-native packages. Finally, let’s type: `npm install --save @ionic-native/firebase@5.0.0-beta.14`

![Image](https://cdn-media-1.freecodecamp.org/images/1*4R0G8E3rY6N8xrwRYpWO8A.png)
_I have version of beta.14_

* One last package, **AngularFire 2**. This is a library for Angular and Firebase: `npm install --save angularfire2 firebase`

Packages install, done! Let’s move to the second section.

### 2. Firebase setup for iOS and Android

Before we will start all of the setup, I need to warn you that you cannot test your push notifications on iOS emulator. To test it out you need to have an Apple Developer account, which costs around $99USD per year. I suggest you to go through iOS setup anyway so it will give you a better understanding for future projects.

**Note:** The steps starting here are very important, so please be patient. Read slowly and make sure you get everything right. Looking for issues after all of the setup can be very frustrating, trust me — I am speaking from my own experience.

#### iOS

[Navigate to the Firebase page](https://firebase.google.com) and login to a console. If you don’t have a project created yet, do it now. You should see this screen.

![Image](https://cdn-media-1.freecodecamp.org/images/1*YKEMKgcl7nukC-1QOOqmAw.png)

Click on the iOS button and you’ll see this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*yzwF8xD5qUFfy5yBWmmkZw.png)

Now we need to provide our iOS bundle ID and this has to be the same as in your Ionic project. Let’s say I want to have the bundle name `com.filipjerga.angularcourse`, then I need to do the following:

Open your Ionic projects and navigate to “config.xml” file. Let’s inspect the widget element. The **Id** attribute holds the unique identifier of your application**.** I said before if you specified your bundle name to `com.filipjerga.angularcourse` in Firebase, the **id** in your Ionic project has to be the same! You can also leave the **id** as you have it already in your Ionic project but then you need to change it in Firebase.

![Image](https://cdn-media-1.freecodecamp.org/images/1*nKaEn3rqKjQQSK5DbOTx1Q.png)
_widget element id is what we need to specify in Firebase_

After you get the value of **id,** don’t forget to provide it to your Firebase application as the bundle ID.

![Image](https://cdn-media-1.freecodecamp.org/images/1*80_WthW7_5CQbd5Dcg6BvA.png)
_Bundle ID has to be a same as your widget id_

That should be everything in the first step of registering the application. This step is crucial, so double check the value of **id** on the widget and bundle ID of your Firebase application**.**

Leave the other fields blank and click “Register app”.

Now we need to download “GoogleService-Info.plist”.

![Image](https://cdn-media-1.freecodecamp.org/images/1*OdG0hBlzpiMMvYT7w6gPxg.png)

When it’s downloaded, paste it into a base folder of your projects. You can see a folder structure in [my project here](https://github.com/Jerga99/heartStoneLib).

We can skip all of the further steps, as they are not required for the Ionic project setup. You should have your IOS application ready.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HVdgpvS2Rv2a1dfuNDPgtw.png)
_Skip this step_

#### Android

The following steps for Android are almost the same as for the iOS setup:

* Click ‘add app’ for Android, same as we did in iOS before.
* The Android package name needs to be the same as our widget id, in my case: `com.filipjerga.angularcourse`
* Next, download `google-services.json`**.** Same as before with the iOS file, we need to copy it to the base folder of our applications
* Click “Next” until you are on the last step, which you can skip, and you should end up with both applications created.

Yay! Congrats! But it’s still too early to cheer.

![Image](https://cdn-media-1.freecodecamp.org/images/1*QN0VI93SeNd5aJ1-yDHJSg.png)
_Both iOS and Angular apps created._

### 3. Push notification code implementation

#### Package importing

The time has come to finally warm up our fingers by typing some code. We will start with importing the packages we installed before.

1. Go to `app.module.ts`
2. Your file should look like this:

```ts
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule, RouteReuseStrategy } from '@angular/router';

import { IonicModule, IonicRouteStrategy } from '@ionic/angular';
import { SplashScreen } from '@ionic-native/splash-screen/ngx';
import { StatusBar } from '@ionic-native/status-bar/ngx';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { AngularFireModule } from 'angularfire2';
import { AngularFirestoreModule } from 'angularfire2/firestore';
import { Firebase } from '@ionic-native/firebase/ngx';

const config = {
    apiKey: "AIzaSyD-K6SlFECXKmd8iHwEvggVtavKgyPF2k8",
    authDomain: "angular2-course-9270e.firebaseapp.com",
    databaseURL: "https://angular2-course-9270e.firebaseio.com",
    projectId: "angular2-course-9270e",
    storageBucket: "angular2-course-9270e.appspot.com",
    messagingSenderId: "443316848633"
  };

@NgModule({
  declarations: [AppComponent],
  entryComponents: [],
  imports: [
    BrowserModule,
    IonicModule.forRoot(),
    AppRoutingModule,
    IonicStorageModule.forRoot(),
    AngularFireModule.initializeApp(config),
    AngularFirestoreModule],
  providers: [
    StatusBar,
    SplashScreen,
    Firebase,
    { provide: RouteReuseStrategy, useClass: IonicRouteStrategy }
  ],
  bootstrap: [AppComponent]
})
export class AppModule {}
```

You can see `Firebase` in the providers array, and `AngularFirestoreModule` and `AngularFireModule` in imports.

But where did the `config` object came from ? You can see lot of information there as “apiKey, authDomain” and so on.

To answer this we need go back to our Firebase console and create a **web app**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*js9Izqbu8Bceb2kIZSDzRg.png)
_Select web platform_

You need to click on a web platform icon on the right from the Android icon (see the image above). When the web app is selected you will be presented with your own **config** object.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5a3ry984v5Mer9Ob63axZQ.png)
_My config object for Firebase after selecting web app._

Now it’s time to copy whole **config** object to `app.module.ts` in our Ionic projects. Please **make sure** you change it for your config object! Mine will not work for you.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Gkp_0kiAs4f_t3UL_hUNVw.png)
_Provide config to app.module.ts_

Now we can start working on the implementation of the push notification service.

#### Push notification service

Let’s create a new service. Call it what you like. I will call mine `fcm.service.ts`. FCM stands for Firebase Cloud Messaging.

First, let’s take a look at the service implementation. I will explain it line by line.

```ts
import { Injectable } from '@angular/core';
import { Firebase } from '@ionic-native/firebase/ngx';
import { Platform } from '@ionic/angular';
import { AngularFirestore } from 'angularfire2/firestore';

@Injectable()
export class FcmService {

  constructor(private firebase: Firebase,
              private afs: AngularFirestore,
              private platform: Platform) {}

  async getToken() {
    let token;

    if (this.platform.is('android')) {
      token = await this.firebase.getToken();
    }

    if (this.platform.is('ios')) {
      token = await this.firebase.getToken();
      await this.firebase.grantPermission();
    }

    this.saveToken(token);
  }

  private saveToken(token) {
    if (!token) return;

    const devicesRef = this.afs.collection('devices');

    const data = {
      token,
      userId: 'testUserId'
    };

    return devicesRef.doc(token).set(data);
  }

  onNotifications() {
    return this.firebase.onNotificationOpen();
  }
}
```

If we want to send a push notification to a device, we need to get an unique identifier of the device. In this case it’s called a `token`.

We need to check for a platform specific device, because of an additional step in the iOS setup. iOS requires explicit permissions to receive push notifications.

Now we need to store this token somewhere, but where? We will store tokens in the **Firebase database**. You can see, I am creating **device** collections and I am filling them with `data` that contains the `token` and just a testing `UserId`. Perfect! Now, we have stored our token and we can subscribe to notifications.

Subscribing to notifications is actually very simple. We just need to call `this.firebase.onNotificationOpen()`

Amazing. Service checked!

All of this is nice but kinda useless, since we are not using our service yet. Let’s fix it!

Move to your `app.component.ts` and write the following:

```ts
import { Component } from '@angular/core';

import { Platform } from '@ionic/angular';
import { SplashScreen } from '@ionic-native/splash-screen/ngx';
import { StatusBar } from '@ionic-native/status-bar/ngx';

import { FcmService } from './shared/service/fcm.service';
import { ToastService } from './shared/service/toast.service';
import { ToastController } from '@ionic/angular';

@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html'
})
export class AppComponent {

  constructor(
    private platform: Platform,
    private splashScreen: SplashScreen,
    private statusBar: StatusBar,
    private fcm: FcmService,
    private toastr: ToastService,
    public toastController: ToastController

  ) {
    this.initializeApp();
  }

  private async presentToast(message) {
    const toast = await this.toastController.create({
      message,
      duration: 3000
    });
    toast.present();
  }

  private notificationSetup() {
    this.fcm.getToken();
    this.fcm.onNotifications().subscribe(
      (msg) => {
        if (this.platform.is('ios')) {
          this.presentToast(msg.aps.alert);
        } else {
          this.presentToast(msg.body);
        }
      });
  }

  initializeApp() {
    this.platform.ready().then(() => {
      this.statusBar.styleDefault();
      this.splashScreen.hide();
      this.notificationSetup();
    });
  }
}
```

Especially important here is the function `notificationSetup`.

We are getting an unique token of the device first.

We are also subscribing to incoming notifications from Firebase.

When the message is received, we need to check, again, for specific platforms. On iOS your message text is under `aps.alert` . On Android it’s under `body`.

Then we will just simply display the received message as a `Toast`.

Now the code setup is done. We are getting very close! It’s time to test it out.

### 4. Test push notifications on Android

All of the required setup for Android should be done right now. You can start emulating your app by:

`ionic cordova emulate android`

or

`ionic cordova build android` and open your build manually in Android Studio.

Let’s launch our applications and go to a Home menu, so we will see a push notification there. Make sure your application was launched properly in emulator and you have no errors.

Go back to your browsers to your Firebase Applications. Now it’s time to inspect our Firebase Database. You can find the database option in the left panel under the **Develop** category.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ev05fxLy5yySp_Xa-uA4JQ.png)
_Firebase Database_

After your application was launched in emulators, the code from **app.component.ts** we wrote a few moments ago ran. No wonder our database is populated. In the “saveToken” function we specified the “devices” collection and we saved the token with the user id as a document into this devices collection. That is what we see in our database.

In my case, I have multiple tokens in my database but you should have only one since we’ve run our app the first time. You will create a new document per unique device/emulator you are running your app on.

Now it’s time to copy this token in order to send push notification to a specific device.

![Image](https://cdn-media-1.freecodecamp.org/images/1*tGtpXyvp46jGuGr9SzsBTg.png)
_Firebase database collection, You will see only one document_

**Navigate to the left panel to a grow tab** and click on cloud messaging.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_oO9cu4Gw3IAXbvGuWeWOQ.png)
_Click on Cloud Messaging_

Now we need to fill in the necessary data. Enter the text of your message and provide the token of the device from the database we just copied.

![Image](https://cdn-media-1.freecodecamp.org/images/1*vdXEcVntcKkfqr8ll49r6Q.png)

When you are sending a message, open your emulated device simultaneously and watch what happens.

Send a message, aaaaand Congrats! Now your Android setup is done and you are able to send push notifications! Isn’t that awesome?

![Image](https://cdn-media-1.freecodecamp.org/images/1*HwQKVZAHeF6Tb1QZV46Zzw.png)
_Push notification on Android._

### 5. iOS push notification pre-setup

Buckle up guys, iOs setup is coming. Let’s separate this setup into multiple steps, so we will not have a panic attack. Let’s dig in!

**First,** build your application for iOS: `ionic cordova build ios`

Open your Xcode, and find your built app in `platforms/ios/nameofyourapp.xcodeproj` . Open it.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2J27mF3dE36yro4TDuDbZA.png)
_Open your .xcodeproj_

This should open a tree structure of your application on the left side. Double Click the root file of this structure. This will open an additional menu with more settings for your app.

![Image](https://cdn-media-1.freecodecamp.org/images/1*CwCbrVvqy_lYJhOHahe5qQ.png)
_More settings_

Sign in with your developer account.

![Image](https://cdn-media-1.freecodecamp.org/images/1*AD1U9EEfHRozZHoUn3d5Ng.png)
_Sign in with a developer account_

5. Open the top “Capabilities” tab and enable “Push Notifications”.

![Image](https://cdn-media-1.freecodecamp.org/images/1*4lOdzB6p9BWGiVkYuC1G1w.png)
_Enable Push Notifications_

6. Navigate to your [Apple developer account page](https://developer.apple.com). Under “Certificates” select “All” and click "`+"` to **add** a new certificate.

![Image](https://cdn-media-1.freecodecamp.org/images/1*M_sJ-0Y6UcfCSXvZexoh9g.png)
_Click the plus sign._

Enable the Apple Push Notification service and proceed to the next step.

![Image](https://cdn-media-1.freecodecamp.org/images/1*sUsADfJUdEJcyi2xblFjwg.png)

Now let’s choose your application.

![Image](https://cdn-media-1.freecodecamp.org/images/1*nXick1xCKeQt8Xrv5LSdvw.png)

We need to **request a certificate**. On your Mac, go to “Keychain Access” -> “Certificate Assistant” -> “Request a Certificate From a Certificate Authority”.

![Image](https://cdn-media-1.freecodecamp.org/images/1*rhTf5N0TL1AmKoXcWbhfoQ.png)

Complete all the necessary information — your email and common name — and save it to disk.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ytVFGho1inBYnv2pYYLLbA.png)

In the Apple Console proceed to the next step and **upload** your certificate request.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Qlz9edFubew4V3ozdt2X7A.png)

In the next step your certificate should be created and you can download it. **You will need it later.**

![Image](https://cdn-media-1.freecodecamp.org/images/1*n5YZm8E6QYxNCDb9Ns7tyQ.png)

Now we need to **create a service key** to enable Apple push notifications. Under “Keys” select “All” . Choose your key name. Enable “Apple Push Notifications service (APNs)”.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8lXVFTpEjwrApP2FArRaew.png)

Click “Continue” and confirm your key. **Never share such data with others.** You can now download your key.

![Image](https://cdn-media-1.freecodecamp.org/images/1*S_gRFhnecm29gSTaSWpfiA.png)

Now we need to go back to Firebase.

In Firebase, open your iOS application and navigate to “Cloud Messaging”.

![Image](https://cdn-media-1.freecodecamp.org/images/1*10JoxYxq7LPUNv_magHS9A.png)

We need to **upload** our APN Authentication Key we generated a while ago. Click “Upload”.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jZtNNpy7gTjsv4tjZfsy9A.png)

Provide all the information and upload the key.

First, upload your “.p8” file, downloaded from the Apple console earlier. Enter your Key ID. You can get the App ID prefix from the Apple console in “Identifiers”->“App IDs”->“Your App”->“Prefix”.

![Image](https://cdn-media-1.freecodecamp.org/images/1*TKeh5ZvgKRN6MXZvw7e0qw.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*l7g5BPKU9GvG0c9RJFWTUA.png)
_Upload p8 file and get keyID and ID prefix_

That’s it. Tears of joy are running down my face.

We can test Push Notifications on iOS. Let’s not forget we need to use a real device.

### 6. Test push notification on iOS

First, we need to build our applications so let’s run: `ionic cordova build ios`

In Xcode you can run your application on a device connected by USB with your computer.

![Image](https://cdn-media-1.freecodecamp.org/images/1*f4NOHT2xCJPgd2SXCXl-EA.png)
_Choose your device_

Let’s wait until everything is launched. We can now repeat the steps to send push notifications from [**Section 4**](https://medium.com/p/ad87cc92394e#0d9c)**,** because it is the same as on Android.

Remember that **you need to use a new token** now, that was generated for your iOS device. Go to Databases, get a new token, and send a push notification. Your result should look like this.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZOE5hMQpOWxUIfE9zjDyfg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*zBEkbPOB6EEurPt5j3qzrw.png)

I hope you have been successful with setting up your push notifications. It takes some time and patience to get everything right, but the outcome and benefits are amazing.

If you like my tutorial and you are interested in more, you can check out my course on Udemy: [**Ionic 4 Crash Course with Heartstone API and Angular.**](http://bit.ly/2Ne2PhK)

For a full project see [my Github Repo](https://github.com/Jerga99/heartStoneLib).

Happy Coding!

Filip

