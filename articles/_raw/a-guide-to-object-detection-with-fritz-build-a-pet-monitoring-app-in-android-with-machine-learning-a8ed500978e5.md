---
title: 'A guide to Object Detection with Fritz: Build a pet monitoring app in Android
  with machine learning'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-30T18:03:22.000Z'
originalURL: https://freecodecamp.org/news/a-guide-to-object-detection-with-fritz-build-a-pet-monitoring-app-in-android-with-machine-learning-a8ed500978e5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*m7zfN9KePEAdXApefron6Q.png
tags:
- name: Android
  slug: android
- name: app development
  slug: app-development
- name: Machine Learning
  slug: machine-learning
- name: mobile app development
  slug: mobile-app-development
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Eric Hsiao

  Whether it is detecting plant damage for farmers, tracking vehicles on the road,
  or monitoring your pets — the applications for object detection are endless. With
  the rise of mobile frameworks like TensorFlow Lite and Core ML, more and ...'
---

By Eric Hsiao

Whether it is [detecting plant damage for farmers](https://heartbeat.fritz.ai/community-spotlight-nuru-a-mobile-app-by-plantvillage-to-detect-crop-disease-in-africa-28d142bf63d5), tracking vehicles on the road, or monitoring your pets — the applications for [**object detection**](https://fritz.ai/features/object-detection.html) are endless. With the rise of mobile frameworks like **TensorFlow Lite** and **Core ML,** more and more mobile apps leverage the power of machine learning to create features that leave us in awe.

#### _So what exactly is object detection?_

In plain English, object detection _identifies and locates specific items in an image or live video with a bounding box._

![Image](https://cdn-media-1.freecodecamp.org/images/1*134aK_z6iXpT_Yz6WoqwaQ.png)
_The middle one is a poodle dressed up as Toothless for Halloween_

But creating features powered by machine learning isn’t easy. Many engineering teams cannot justify the time and resources. You need the right in-house expertise to collect data, train a model, and iterate on the performance and accuracy. Understandably, with pressure from product teams to deliver value quickly for end-users, potential features are tossed aside in a backlog abyss.

In this post, I’ll show you how any Android developer can use real-time object detection to create an app that detects and recognizes pets — all in less than 30 minutes. To do this, I’ll use the [Fritz SDK](https://fritz.ai) (full disclosure, I work at Fritz) which makes it easier to leverage machine learning capabilities without any prior experience.

### Getting started

To start using the Fritz SDK, we’ll go through adding the necessary dependencies in a sample app that we’ve created.

#### 1. First, create a Fritz account

[Sign up here](https://fritz.ai?utm_source=medium&utm_campaign=freecodecamp) and follow the [get started directions](https://docs.fritz.ai/get-started.html?utm_source=medium&utm_campaign=freecodecamp).

#### **2.** Clone the sample camera app

Set up a skeleton app that includes a video feed and camera code. In this tutorial, we won’t go depth into the [Camera 2 API](https://developer.android.com/reference/android/hardware/camera2/package-summary), but if you have any questions, please leave a comment.

```
git clone https://github.com/fritzlabs/camera-sample-app
```

#### **3.** Register the Android app in the webapp

You need to register your app with Fritz in order to use ML-features. When you’re adding the app to Fritz, use the same applicationId (ai.fritz.camera) as the **app/build.gradle.**

![Image](https://cdn-media-1.freecodecamp.org/images/1*T9Vf0XvJgy8w1-RcyBT3oQ.png)
_In your app/build.gradle, notice the applicationId field_

![Image](https://cdn-media-1.freecodecamp.org/images/1*8LB6zgaIzCXbeiAX4eitZQ.png)
_The package ID must match the applicationId shown above for your application. In this case, the package id is **ai.fritz.camera**_

Make sure you note the API Key for Step 5. If you need to access it again, you can go to Project Settings > Your App (Pet Monitor)> Show API Key (in the options menu).

#### **4.** Add FritzCore + dependencies in **app/build.gradle**

Make sure to add the Fritz repository. This will allow you to download the necessary dependencies:

In the dependencies section, add these 2 libraries:

```
dependencies {    implementation "ai.fritz:core:2.0.0"    implementation "ai.fritz:vision-object:2.0.0"}
```

#### 5. Configure the SDK

Call **Fritz.configure** in the **Application** or **MainActivity onCreate** lifecycle method with the API key you got in Step 3.

With that, you’re ready to use object detection in your app.

### Detecting dogs & cats on live video

Now let’s get to the fun stuff. We’ll jump into the MainActivity and use the object detection predictor on each frame passed in on the video stream.

#### 1. Get an instance of FritzVisionObjectPredictor

The predictor takes in a **FritzVisionImage** and returns a list of **FritzVisionObjects** detected.

#### **2.** Convert each frame to a **FritzVisionImage** object

Use either **fromBitmap** or **fromMediaImage** static methods to create an object from a **Bitmap** or **media.Image** object. For the sample app, use **fromMediaImage**, which also takes in the rotation applied on the image from the camera.

The rotation depends on the device rotation and the camera orientation sensor. The **cameraId** identifies the active camera being used on the device (front, back, etc.), and you can get the rotation angle with the following helper method.

```
int rotation = FritzVisionOrientation.getImageRotationFromCamera(this, cameraId);
```

Finally, create a **FritzVisionImage** object with the **Image** and rotation value.

#### **3. Run prediction**

Pass the image into the predictor to detect different objects in the image.

#### **4. Filter the result and display bounding boxes**

Each **FritzVisionObject** comes with a label, a confidence score, and a bounding box that shows where it’s located on the original image. In this case, we only care about pets (specifically cats and dogs), so we can filter out the other items.

Finally, display the bounding boxes around your pets. **FritzVisionObject** has a convenient method called **drawOnCanvas** which makes it easy to display the detected objects.

Here’s the complete code after the render callback:

**Notice the scale factor on the boxes.** This is because the **media.Image** object we used to create the FritzVisionImage object is the same size as the preview viewport. In the camera sample app, it’s 1280 x 960. The bounding boxes will have coordinates associated with the preview size. Since we want to show this on the full screen, we need to scale the result to the phone’s viewport.

Here’s the final result:

For the finished code, take a look at the [GitHub repo](https://github.com/fritzlabs/pet-monitor-android).

### Why this is useful

With the machine learning feature behind this basic app, there are ton of different features you can create (both practical and goofy):

* Alert the owners with a text message if the dog walker hasn’t returned.
* Record a message telling your dog to “Sit down!” when they’re running around the room with no one around. I bet you could capture funny photos of your dog in this moment, too.
* Show the user a message when a cat / dog is detected (take a look at the completed code for an example)
* Sound an alarm when the camera detects cats (I’m allergic).

Of course, not many people have a spare Android tablet / phone that they can use as an expensive pet monitoring camera, but this is just a simple example among many different possibilities for how you might create an app with [object detection](https://docs.fritz.ai/features/object-detection/about.html?utm_source=medium&utm_campaign=freecodecamp) using [Fritz](https://fritz.ai?utm_source=medium&utm_campaign=freecodecamp). I can’t wait to see what all the creative developers of the world build using object detection.

Got an idea? Leave a comment!

I’m a lead developer at [Fritz](https://fritz.ai?utm_source=medium&utm_campaign=freecodecamp) specializing in mobile machine learning. If you’re looking to create features powered by AI/ML, we offer prebuilt APIs ([image segmentation](https://docs.fritz.ai/features/image-segmentation/about.html?utm_source=medium&utm_campaign=freecodecamp), [image labeling](https://docs.fritz.ai/features/image-labeling/about.html?utm_source=medium&utm_campaign=freecodecamp), [style transfer](https://docs.fritz.ai/features/style-transfer/about.html?utm_source=medium&utm_campaign=freecodecamp)) and [custom model](https://docs.fritz.ai/custom-models/overview.html?utm_source=medium&utm_campaign=freecodecamp) support.

