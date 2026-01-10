---
title: Why your Push Notifications never see the light of day
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-28T18:55:46.000Z'
originalURL: https://freecodecamp.org/news/why-your-push-notifications-never-see-the-light-of-day-3fa297520793
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1KfeXO-IedHQ9cUI83cV3g.jpeg
tags:
- name: android app development
  slug: android-app-development
- name: androiddev
  slug: androiddev
- name: Firebase
  slug: firebase
- name: mobile app development
  slug: mobile-app-development
- name: push notification
  slug: push-notification
seo_title: null
seo_desc: 'By Neil Mathew

  Push Notifications fail on specific Android phones. Here’s why.

  I recently added support for Push Notifications in the Kayako App. I tested and
  shipped it. And I thought I did pretty good job.

  But then one by one, my users start commen...'
---

By Neil Mathew

#### Push Notifications fail on specific Android phones. Here’s why.

I recently added support for [Push Notifications](https://firebase.google.com/docs/cloud-messaging/) in the [Kayako App](https://play.google.com/store/apps/details?id=com.kayako.android.k5). I tested and shipped it. And I thought I did pretty good job.

But then one by one, my users start commenting that the the app doesn’t show any notifications about 95% of the time. At first, I thought it was a mistake because the Push Notifications were working as intended on my emulator and devices. But as I dug deeper, it became clear how serious and valid this problem was. This was but the tip of the iceberg. Close to 50% of our Android app users were affected but only few informed us about it.

### So, what’s the problem?

Push Notifications are **not** working properly on specific Android phones.

I use the word ‘properly’ because users receive push notifications when the app is open but [not when it is closed](https://github.com/firebase/quickstart-android/issues/41), which defeats the purpose of push notifications.

I use the words ‘specific Android phones’ because this issue is noticed only on phones by manufacturers like Xiaomi, Oppo, One Plus, Vivo, Lenovo, Huawei, Samsung, and a few others.

### Why is this happening and how do we fix it?

To understand the problem, let’s first understand the Android UI and the expected behavior of Push Notifications.

On Android, we have three buttons at the bottom as part of the Navigation Bar. The square button, on click, opens the **Recents** screen. The **Recents** screen lists all the ongoing tasks or apps recently opened. We can clear these applications at any time, as shown below.

![Image](https://cdn-media-1.freecodecamp.org/images/VMda4Y0jAqWe3uv5jqChb4HzarB7g2ffPjU0)
_Recents Screen_

Yet on certain [stock ROMs](https://www.xda-developers.com/what-is-custom-rom-android/) (Android operating system customized by device manufacturers), clearing an application kills that application and its background services. This is bad because we need background services to show Push Notifications.

When the server informs the Android device of a new Push Notification, it would normally re-start the application’s background services to show the notification to the user. That’s good because background services will automatically start to show push notifications.

The image below shows the expected behavior which is the case for vanilla ROMs. This is the original Android firmware that is not customized by manufacturers.

![Image](https://cdn-media-1.freecodecamp.org/images/vsgpo013XZS9sWzJO4yXmsRyZ7O8TsP8QinG)
_Expected Push Notification Behavior_

Yet despite this, some Android phones using the Kayako app are **not** receiving Push Notifications when the app is cleared from **Recents** screen. The reason is that phone manufacturers like Oppo, Xiaomi, and One Plus use a stock ROM that disables the re-starting of background services for most apps. This is bad because we’re back to where we started with no way to show Push Notifications.

Thankfully, these stock ROMs have a Settings page to enable the re-starting of background services. Although the auto-starting of background services are disabled by default, users can manually enable this feature by following some instructions. This is good because now background services can be automatically started to show Push Notifications. But, it’s an ugly solution because it involves some manual work that the user has to do.

The intentions of the manufacturers are to conserve battery and improve performance. The app users now have to open their settings app, navigate to the correct page, scroll through a list of apps, and then enable the feature for the Kayako app.

#### But wait, why don’t apps like Gmail and Slack have these problems?

Top-popular apps like Gmail, Slack and Whatsapp are whitelisted by these stock ROMs. That means these apps have auto-launch enabled for them by default.

However our app, along with many many others, have auto-launch disabled by default.

![Image](https://cdn-media-1.freecodecamp.org/images/m-OlwUJt4m7rnaN84273MxOWR5viXIcDORZr)
_One Plus ‘Apps auto-launch’ Settings page_

#### I can’t find the settings to enable auto-launch. Where are they located?

The steps to enable auto-launch for an app are different for different manufacturers. This is because this is not a native Android feature and is very specific to stock ROMs.

It should also be noted that the terminology used by each manufacturer is different. The auto-launch feature can be referred to as app auto-start, start-up manager, auto-start manager, app optimisation, protected apps, or background app management.

To make matters worse, the auto-launch settings page is not easy to find. For One Plus devices (using [Nougat](https://www.android.com/versions/nougat-7-0/) or below), you need to open up Settings, click Apps, then the gear icon located on the toolbar, and then Apps Auto-launch under the Advanced sub-category at the very bottom.

### Alright, what’s the solution?

In the end, the user will have to perform the steps manually. This can not be programmatically enabled for all devices. The best we can do is to make it as easy as possible for app users to do so.

#### Create a support article

[Kelly O’Brien](https://www.freecodecamp.org/news/why-your-push-notifications-never-see-the-light-of-day-3fa297520793/undefined) and I wrote an article which makes an attempt to identify all the device manufacturers with this problem and explain the steps to enable Push Notifications on those devices. You can read about it [here](https://support.kayako.com/article/1461-why-aren-t-push-notifications-working-on-my-android-app).

#### Inform users in-app

As I mentioned before, not everyone takes the time out to complain. I can not expect users to contact the support team or search for the support article online. At the same time, there’s no easy way to automatically identify if Push Notifications aren’t working when the app is closed.

I decided to show a small footer on the Push Notifications Settings page where the article is available to the user at all times.

![Image](https://cdn-media-1.freecodecamp.org/images/t1U0ZBIa3qJG1hvdU1lQT9GO4tJg3N0q5JUY)
_Push Notification Settings Page_

#### Open the concerned settings page in-app

I’ve found many Stack Overflow answers like [this one](https://stackoverflow.com/questions/34149198/how-to-enable-auto-start-for-my-app-in-xiaomi-programmatically) which recommend programmatically opening the concerned settings page by detecting your device manufacturer. While I like the idea, I have not implemented this. I haven’t had the chance to test if the device-specific code actually works which puts me at unease.

If you have other suggestions or ideas, I welcome them.

