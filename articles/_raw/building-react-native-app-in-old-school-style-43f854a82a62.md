---
title: How to build a React Native App in the old-school style
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-30T12:42:38.000Z'
originalURL: https://freecodecamp.org/news/building-react-native-app-in-old-school-style-43f854a82a62
coverImage: https://cdn-media-1.freecodecamp.org/images/1*voZnfNFpIwpswufxZ6OKqg.png
tags:
- name: internet
  slug: internet
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: React Native
  slug: react-native
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Panth Solanki

  As we all know, it’s high time to learn React Native. There are two ways to develop
  it as a doc. This section focuses on creating apps in Expo, directly on your Android
  device without any internet connection on your device.

  I know it...'
---

By Panth Solanki

As we all know, it’s high time to learn React Native. There are two ways to develop it as a doc. This section focuses on creating apps in Expo, directly on your Android device without any internet connection on your device.

I know it’s very easy by using Expo Client app on your device with the internet, but what if you have an internet issue? You don’t want to use your limited MBs for development. So what if your mobile’s WiFi connectivity has a stability issue, or you just want to develop app old-school style…or any other reason?

Let’s get started, this process includes just three small steps. Remember, it’s just for development on OS Windows and targets OS Android.

#### **Pre-Setup Requirements**

You need to install an adb driver on your PC from [**here**](http://adbdriver.com/downloads/). The procedure is also [**here**](http://adbdriver.com/documentation/how-to-install-adb-driver-on-windows-8-10-x64.html).

Once you complete the process, connect your mobile to your PC. Open _Command Prompt_ and run the command **adb devices_._** If it returns some device name under _list of devices,_ then your setup is completed. But if no name is shown, then you need to install adb drivers properly.

Note: Your mobile should have USB debugging ON in the developer options.

Install the Expo Client App from the play store [**here**](https://play.google.com/store/apps/details?id=host.exp.exponent&hl=en_IN)**.**

#### Setup React Native Project

Follow the steps as described in the docs [**here**](https://facebook.github.io/react-native/docs/getting-started.html)**.**

I’m just copying the steps here. Assuming that you have _Node 10+_ installed, run the following commands:

_npm install -g expo-cli_

_expo init AwesomeProject_

_cd AwesomeProject_

_npm start_

The above commands will open browser with [**_http://localhost:19002_**](http://localhost:19002) (if it doesn’t open automatically, open it manually).

Once you open the localhost, it will show a message like **Tunnel Ready** as below:

![Image](https://cdn-media-1.freecodecamp.org/images/zYHDe2I9we1PUpcQ3LnBoAzpC3ThfLaSXrX9)
_Tunnel Ready means it’s time to create magic :)_

#### Post-Setup Steps

Now it’s time to connect your device and open another command prompt to run the following commands:

**adb devices** // to find the device name of your connected devices

**adb -s <device name> reverse tcp:8081 tc**p:8081 // this will not print anything

Go to [**http://localhost:19002**](http://localhost:19002) in the browser and click **Run on Android device/emulator.**

![Image](https://cdn-media-1.freecodecamp.org/images/VD-QK3SNqyRSVLFLsb11kdTL9NSvhpo09yck)
_Click on Run on Android device/emulator to see magic on your device_

Now you will see the bundles loading on your device. After loading all bundles, your app will be live on your device and your browser will be as follows:

![Image](https://cdn-media-1.freecodecamp.org/images/zamalXDcwXipHylOzpd9S274xeVzgqp7F6cy)
_The sidebar will show your device_

You can debug your app by clicking on the top-right button.

![Image](https://cdn-media-1.freecodecamp.org/images/NScWO4d1NZ0LB1y1HY3NxW4IWqcfPpJAEHlV)
_Click on the top-right button and you can see what data is passed to your device._

I will be happy if this information is useful to you in any way. If you have any questions, do comment — I will be more than happy to help.

Thanks for reading.

