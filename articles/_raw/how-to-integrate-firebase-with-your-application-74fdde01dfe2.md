---
title: How to Integrate Firebase With Your Application
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2019-01-29T22:22:18.000Z'
originalURL: https://freecodecamp.org/news/how-to-integrate-firebase-with-your-application-74fdde01dfe2
coverImage: https://cdn-media-1.freecodecamp.org/images/0*aClI4EGtanpC5mqJ
tags:
- name: coding
  slug: coding
- name: Firebase
  slug: firebase
- name: Java
  slug: java
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: You’ve probably heard about Firebase, but may not know much about how it
  works and how it fits in with your application. Well, you’ve come to the right place.
  We’ll go over what Firebase is and how to integrate it with your Android project
  straight f...
---

You’ve probably heard about Firebase, but may not know much about how it works and how it fits in with your application. Well, you’ve come to the right place. We’ll go over what Firebase is and how to integrate it with your Android project straight from Android Studio. **_Buckle up_**.

#### Fire-what?

Essentially, Firebase fits into the group of [MBaaS](https://en.wikipedia.org/wiki/Mobile_backend_as_a_service), which means, **_Mobile Backend as a Service_**. If you are a frontend developer, you will need various services that may require backend capabilities. Think file storage, database, push notifications, analytics, advertisements and more. You can use Firebase to help you in connecting your application with those services. To read more about it, go [here](https://firebase.google.com/).

![Image](https://cdn-media-1.freecodecamp.org/images/1*-ZiPpoNKT33nBDCw2STgFg.jpeg)

### Follow These Steps

1. After opening your project in Android Studio, click on the **_Tools_** tab and select **_Firebase_**
2. A new window pops up from the right, the **_Assistant_** tab, with all the services Firebase offers.

![Image](https://cdn-media-1.freecodecamp.org/images/1*NA34OHFxCyy1zjCYIbeUzg.jpeg)
_Firebase Assistant_

3. Select the service you wish to add to your application by clicking on it. We’ll select **_Cloud Messaging_** as an example.

4. Click on the link that shows up, specifically, **_Set up Firebase Cloud Messaging._**

5. The Assistant window will transform into a new menu:

![Image](https://cdn-media-1.freecodecamp.org/images/1*ckAHDd9hqpy8TuM30IQhHQ.jpeg)
_Follow the steps above_

Follow the steps outlined in the Assistant, making sure to pay attention to any code that needs adding (and where it needs to be added).

The first step will always require you to connect your application with Firebase. In order to do so, you have to create a project for your application in the [**_Firebase Console_**](https://console.firebase.google.com).

And the second will guide you to add the specific service you are after. So for our example, FCM stands for **F**irebase **C**loud **M**essaging.

The following things we need to do are:

* Create a new class which extends FirebaseMessagingService
* Override two methods: **_onNewToken_** and **_onMessageReceived_**

* Declare the service in your manifest:

6. The last step you will encounter is called **_Next Steps_**. Here you will be prompted to go to the Firebase Console. This is in order for you to interact with the service you just added.

![Image](https://cdn-media-1.freecodecamp.org/images/1*yb2p7q78i8bGy5TOOQAm1A.jpeg)

You now posses the ability to grant any application you make a powerful backend component that can be up and running in minutes. This will drastically shorten your development time and enable you to focus on what is important for you.

Comments? Questions? Feel free to reach out.

_If you liked this article, clap away so that others can enjoy it as well! ?_

