---
title: How to use the Google Cloud Vision API and ClickSend to keep tabs on your pets
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-06T16:17:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-the-google-cloud-vision-api-and-clicksend-to-keep-tabs-on-your-pets-6024b4daac29
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4bblfUcScLKK4bWm3_FE0A.png
tags:
- name: Google
  slug: google
- name: image recognition
  slug: image-recognition
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Namratha Subramanya

  Just like people, dogs are scared by all kinds of things. Most often, it’s a result
  of having a negative experience or not being handled when their natural fears surface.
  In this article, we’ll create a way to make sure your do...'
---

By Namratha Subramanya

Just like people, dogs are scared by all kinds of things. Most often, it’s a result of having a negative experience or not being handled when their natural fears surface. In this article, we’ll create a way to make sure your dog is safe when you are away.

You can attach a camera to your dog’s collar that can capture images, and use Vision API to detect and recognize the images.

Let’s say your dog is scared of cats, and you want to make sure your little furry friend is safe from cats while playing in the backyard in your absence. You could build an application where you could get SMS alerts to your device when cats are recognized by Cloud Vision API.

In this tutorial, you’ll learn how to recognize an image using Google Cloud Vision API and alert the user with an SMS using ClickSend API. PubNub forms the skeleton of the application and interconnects the features.

[**The full project GitHub repo is available here.**](https://github.com/namrathasubramanya/PubNub-VisionAPI-ClickSend)

### Let’s Get Building

Assume your laptop’s webcam is the camera fixed to your dog’s collar. Below is the code that opens your webcam and takes pictures for you. You could set a time interval to capture images frequently. These images go into a canvas element and can be saved on your device. You can find the code for clicking and saving the images below.

### Cloud Vision API

The Google Cloud Vision API enables developers to understand the content of an image through its powerful machine learning models. To get started with implementing the Vision API, you need to create a new project [here](https://console.cloud.google.com/cloud-resource-manager?_ga=2.203919383.-603090119.1528760418). Before you create a new project, you need to set up your billing account. After this, you need to enable Vision API.

For more details, check this quick start [link](https://cloud.google.com/vision/docs/quickstart).

Run the following command in your terminal:

```
pip install --upgrade google-cloud-vision
```

To run the client library, you must first set up authentication by creating a service account [here](https://console.cloud.google.com/apis/credentials) and setting an environment variable.

* From the **Service account** drop-down list, select **the New service account**.
* Enter a name into the **Service account name** field.
* Do not select a value from the **Role** drop-down list. No role is required to access this service.
* Click **Create**. A note appears, warning that this service account has no role.
* Click **Create without role**. A JSON file that contains your key will download to your computer.

Now set the environment variable `GOOGLE_APPLICATION_CREDENTIALS` to the file path of the JSON file that contains your service account key. This can be done as follows:

For Linux/Mac OS:

```
export GOOGLE_APPLICATION_CREDENTIALS="[PATH]"
```

For Windows:

```
set GOOGLE_APPLICATION_CREDENTIALS=[PATH]
```

Now you are all ready to run the code that recognizes your images. Here’s the Python code that takes the snapshots from the directory where you have saved them (mine is Downloads) and responds with labels.

The result of the image recognition is sent to the user using [PubNub Real-time Messaging](https://www.pubnub.com/docs/tutorials/pubnub-publish-subscribe/?utm_source=Syndication&utm_medium=Medium&utm_campaign=SYN-CY18-Q2-Medium-June-28). You just need to subscribe your device to a channel, say, `alert_notify` to which Vision API’s sends the results of the image recognition.

![Image](https://cdn-media-1.freecodecamp.org/images/0*u-0bRBK1pv8V8YsA.jpg)

### Web Notification Alert using PubNub

You’ll now have to initialize your PubNub keys. [Sign up for a PubNub account](https://www.pubnub.com/docs/tutorials/pubnub-publish-subscribe/?utm_source=Syndication&utm_medium=Medium&utm_campaign=SYN-CY18-Q2-Medium-June-28) and create a project in the [Admin Dashboard](https://admin.pubnub.com/#/login/?utm_source=Syndication&utm_medium=Medium&utm_campaign=SYN-CY18-Q2-Medium-June-28).

Now you can publish the alert message inside your Python code which you can send as a web push notification to your device. The device, in turn, subscribes to `alert_notify` channel and receives the alert message from your camera.

You can design the web push notification using the [Notification API](https://developer.mozilla.org/en-US/docs/Web/API/notification) in HTML5.

### ClickSend API

[ClickSend API](https://developers.clicksend.com/) allows developers to integrate SMS, voice, fax, posts, or email into their applications. You could send an SMS to your mobile device along with web push notifications using PubNub. The ClickSend API is well-documented for developers.

You can use ClickSend’s [HTTP API](https://clicksendhttpapiv2.docs.apiary.io/#). Every time Vision API recognizes an image, you get an SMS to your device.

### Congrats!

Now that you have set up Cloud Vision API and ClickSend API to communicate with each other through PubNub’s Publish-Subscribe, you will be able to receive web notifications and SMS alerts sent to your device every time your camera captures an image of a cat. Undoubtedly, this is a great starting point for building applications using different APIs and connecting them through PubNub.

_Originally published at [www.pubnub.com](https://www.pubnub.com/blog/image-recognition-using-vision-api-and/?utm_source=Syndication&utm_medium=Medium&utm_campaign=SYN-CY18-Q2-Medium-June-28)._

