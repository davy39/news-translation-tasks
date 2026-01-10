---
title: Face centering Android library build on top of Google Vision API
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-07-20T11:15:42.000Z'
originalURL: https://freecodecamp.org/news/face-centering-android-library-build-on-top-of-google-vision-api-f88661b97959
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9MTjfLoGfWIRXjlhMaTucw.png
tags:
- name: Android
  slug: android
- name: android app development
  slug: android-app-development
- name: Design
  slug: design
- name: open source
  slug: open-source
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Rohit Arya

  In our Android apps, when we crop photos to display them, we often encounter the
  problem of positioning faces properly.

  This inspired me to create a tool that will locate faces and in an image (if there
  are any) and center the cropped i...'
---

By Rohit Arya

In our Android apps, when we crop photos to display them, we often encounter the problem of positioning faces properly.

This inspired me to create a tool that will locate faces and in an image (if there are any) and center the cropped image around them.

Here’s how I did it.

I started with [Face Detection API](https://developers.google.com/vision/face-detection-concepts) of Google’s mobile vision. This API provides:

* Face detection (not face recognition)
* Face tracking (extends face detection to video sequences)
* A **landmark** — a point of interest within a face (like eyes, nose, etc)
* Classification of a face to determine if the face is smiling, eyes are open or closed, and other features

Since I just wanted the position of the face, I only used the face detection component. To start with that, I created the face detector:

```java
FaceDetector detector = new FaceDetector.Builder(context)
    .setTrackingEnabled(false)
    .build();
```

Now given a bitmap, I created a frame instance from the bitmap to supply to the detector:

```java
Frame frame = new Frame.Builder().setBitmap(bitmap).build();
```

Now, I tried to detect faces synchronously in the frame:

```java
SparseArray<Face> faces = detector.detect(frame);
```

Once I got faces, I chose one face (for now) to crop the image around, keeping that face in the center.

Now to begin cropping the image:

* I created a scaled new bitmap to fit the target view (ImageView).
* I then recalculated the position of the face in the new bitmap.
* Keeping the face in the center, I cropped the original bitmap to get a new bitmap.
* If no face is detected, then I fallback to CENTER CROP.

_You can find the full code in [my GitHub repositories](https://github.com/aryarohit07) below._

Here are some results of it:

![Image](https://cdn-media-1.freecodecamp.org/images/uaukFMMKsp3BvFT7JUNMHn4Cvg-X4VpvIhpK)
_Original image to be cropped._

![Image](https://cdn-media-1.freecodecamp.org/images/-yG3bvIhkNPDtAtgmbgEEsJGXjxg0eKYF6JA)
_Results after cropping_

![Image](https://cdn-media-1.freecodecamp.org/images/Hms3iIRztMyLsd6gDHInDvSbhIIhrD2e2NLH)
_Original image_

![Image](https://cdn-media-1.freecodecamp.org/images/WLQx73hHnBlvLriXqHJPA1agUmEedBcTRIsh)
_Results after cropping_

![Image](https://cdn-media-1.freecodecamp.org/images/np-29WMZZdUWy6XQHjxZhAAa5EaQWtY8YBdP)
_Original Image_

![Image](https://cdn-media-1.freecodecamp.org/images/slny81MI3mfiuITJE--qFn5q2qZqkHNnOqoL)
_Results after cropping_

![Image](https://cdn-media-1.freecodecamp.org/images/Lg6EwpnyTdemmnG97sljtu-o2LyucFQPNB5y)
_Original Image_

![Image](https://cdn-media-1.freecodecamp.org/images/osDqcv3pEObAsIHEaMD8VaTwM0EwfuKzkL6b)
_Results after cropping_

I finally exported this as a library, which you can find below.

For [Glide](https://github.com/bumptech/glide):

[**aryarohit07/GlideFaceDetectionTransformation**](https://github.com/aryarohit07/GlideFaceDetectionTransformation)  
[_GlideFaceDetectionTransformation - An Android image transformation library providing cropping above Face Detection…_](https://github.com/aryarohit07/GlideFaceDetectionTransformation)  
[github.com](https://github.com/aryarohit07/GlideFaceDetectionTransformation)

For [Picasso](https://github.com/square/picasso):

[**aryarohit07/PicassoFaceDetectionTransformation**](https://github.com/aryarohit07/PicassoFaceDetectionTransformation)  
[_PicassoFaceDetectionTransformation - An Android image transformation library providing cropping above Face Detection…_](https://github.com/aryarohit07/PicassoFaceDetectionTransformation)  
[github.com](https://github.com/aryarohit07/PicassoFaceDetectionTransformation)

I am planning to release it for [Fresco](https://github.com/facebook/fresco) too.

Feel free to make use of this tool, and help me improve it over on GitHub.

> _If you enjoyed reading this article, it would mean a lot if you recommend it using the ❤ icon and share with your colleagues and friends. Thanks!_

