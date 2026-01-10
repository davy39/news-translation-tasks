---
title: The new security features in Android Pie and why I’m excited about them
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-27T17:29:15.000Z'
originalURL: https://freecodecamp.org/news/the-new-security-features-in-android-pie-and-why-im-excited-about-them-4a2f45be61fe
coverImage: https://cdn-media-1.freecodecamp.org/images/1*UL2cOeH9M7dVfIe1k5qlrw.jpeg
tags:
- name: Android
  slug: android
- name: mobile app development
  slug: mobile-app-development
- name: Security
  slug: security
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Onur Tuna

  I gave a talk at the Google Developer Group Devfest 18 in Ankara about Android as
  I do every year. Quite likely this was the last talk I will give on Android. I talked
  about one of the big improvements in the latest version of Android. T...'
---

By Onur Tuna

I gave a talk at the Google Developer Group Devfest 18 in Ankara about Android as I do every year. Quite likely this was the last talk I will give on Android. I talked about one of the big improvements in the latest version of Android. To me, this has been the most exciting Android improvement so far. There are lots of new security and feature updates in Android Pie, and I want to introduce them here briefly.

> You can get my presentation [here](https://drive.google.com/file/d/1OzDPj-8urX5tRpBUJiSVM2MOUUao45-K/view?usp=sharing).

#### Restriction on the usage of mic or camera in the background

Apps won’t be able to use your mic or camera in the background with Android Pie. This is one of the most important security features coming with the new Android.

![Image](https://cdn-media-1.freecodecamp.org/images/XZOMpqVe7lZvCv-5Wsm06tNACR1hgPE5bDwu)

Apps will only be able to use your mic or camera if they are actively being used on screen. If you have any paranoia about some apps listening to you, you can be sure that no apps can listen to you secretly with Android Pie.

While this move prevents apps from listening to your conversations, Google will still be able to listen to you. ‘OK Google.’ ?

BTW no app will be able to use any other sensors besides the mic and camera.

#### New lockdown mode

![Image](https://cdn-media-1.freecodecamp.org/images/yUjuzkTOaouvv5YQ8CoA7ag7-bZeucj4qGGP)

When the fingerprint authentication was first introduced, it helped everyone. Do you know how many times an average human authenticates their mobile phone in a day? Yeah. Too many.

Here comes the trouble: there are many stories about how police or people with bad intentions could force you to unlock your phone with your fingerprint to search it. Anyone could force you to unlock your phone with your face id to gain access to your digital life (nowadays it’s your actual life).

You can disable fingerprint and face authentication in Android Pie by enabling the lockdown mode. Only your PIN, pattern, or password will work when it’s enabled. However, this feature will not be needed in your casual life. It’s just good to have for higher-risk situations.

#### **HTTPS is the default for apps**

Today most people are aware that websites which have a green locked key are secure enough to enter. You can search for that key in your browser. However, you can not know if the app you use makes calls to HTTPS services.

Any regular app sends data over the Internet. Any bad person may read this data you send unless it is encrypted. HTTPS guarantees that the transaction is encrypted. Android will force developers to send data over HTTPS to make sure that the data sent from your phone will be encrypted.

#### **Restoring your device will require a passcode**

![Image](https://cdn-media-1.freecodecamp.org/images/Aw96iyrmcpvoSVchcozPV159UoIdANOD7H-1)

With Android Pie, you will restore your device using your PIN or pattern or password. Fingerprint or face id has been enough to restore the device so far. However, this simplicity came with some vulnerability. A second auth layer has been introduced to restore your device more securely. Be aware that if you forget the PIN, you will not be able to restore your device.

#### **The alert tone when your call is being recorded**

There are many apps which can record calls. It has been a big vulnerability so far. There are two cases: any app can record your call, or someone you’re talking to can record the call.

Now if you record a call, an alert tone will be sent periodically to you and to the person you’re talking to. Android Pie ends this paranoia permanently.

I’ve tried to introduce significant new improvements in Android Pie with this post. While there are many more enhancements, these were the ones I found most important. Android Pie will be the most secure Android version ever.

