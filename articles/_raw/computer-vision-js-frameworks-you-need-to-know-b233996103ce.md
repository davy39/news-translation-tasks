---
title: Computer Vision .js frameworks you need to know
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-18T16:05:59.000Z'
originalURL: https://freecodecamp.org/news/computer-vision-js-frameworks-you-need-to-know-b233996103ce
coverImage: https://cdn-media-1.freecodecamp.org/images/0*uXRPu25xSI_86KUw
tags:
- name: Computer Vision
  slug: computer-vision
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: Machine Learning
  slug: machine-learning
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Shen Huang

  Computer vision has been a hot topic in recent years, enabling countless great applications.
  With the effort from some dedicated developers in the world, creating an application
  utilizing computer vision is no longer rocket science. In ...'
---

By Shen Huang

Computer vision has been a hot topic in recent years, enabling countless great applications. With the effort from some dedicated developers in the world, creating an application utilizing computer vision is no longer rocket science. In fact, you can build many of the application in a few lines of JavaScript code. In this article, I will introduce you to some of them.

### 1. TensorFlow.js

Being one of the largest machine learning frameworks, TensorFlow also allows the creation of Node.js and front-end JavaScript applications with [**Tensorflow.js**](https://www.tensorflow.org/js). Below is one of their demos matching poses with a collection of images. TensorFlow also has a [**playground**](https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=circle&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=0&networkShape=4,2&seed=0.27185&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false) allowing us to visualize better artificial neural networks, which can be great for educational purposes.

![Image](https://cdn-media-1.freecodecamp.org/images/fzXRDjBio2OIxVNIHI2Njxb9sg6x9rVQRAph)
_A Move Mirror Demo from [Tensorflow.js](https://experiments.withgoogle.com/move-mirror" rel="noopener" target="_blank" title=")_

### 2. Amazon Rekognition

[**Amazon Rekognition**](https://aws.amazon.com/rekognition/?sc_channel=PS&sc_campaign=acquisition_US&sc_publisher=google&sc_medium=ACQ-P%7CPS-GO%7CBrand%7CDesktop%7CSU%7CMachine%20Learning%7CRekognition%7CUS%7CEN%7CText&sc_content=aws_recognition_software_e&sc_detail=amazon%20rekognition&sc_category=Machine%20Learning&sc_segment=293645376368&sc_matchtype=e&sc_country=US&s_kwcid=AL!4422!3!293645376368!e!!g!!amazon%20rekognition&ef_id=EAIaIQobChMIwLzV1obx4AIVEK6WCh3MZAPREAAYASAAEgJlv_D_BwE:G:s) is a powerful cloud-based tool. But they also provide SDKs for JavaScript in browsers which can be found [**here**](https://aws.amazon.com/sdk-for-browser/). Below is an image illustrating how detailed their face detection can be.

![Image](https://cdn-media-1.freecodecamp.org/images/0pIcn86SNFaM5cbA5CXboENRyfMtX0ayQ3rb)
_Facial Feature Detection with [Amazon Rekognition API](https://docs.aws.amazon.com/rekognition/latest/dg/faces-detect-images.html" rel="noopener" target="_blank" title=")_

### 3. OpenCV.js

Being one of the oldest computer vision frameworks out there, [**OpenCV**](https://opencv.org/) has served developers in computer vision for a very long time. They also have a [**JavaScript version**](https://docs.opencv.org/3.4/d5/d10/tutorial_js_root.html) allowing developers to implement those features onto a website.

![Image](https://cdn-media-1.freecodecamp.org/images/axCPVu-3ItA12kmt4OLraf0WgqxzZ-BmmUfr)
_Example Face Detection with OpenCV, Image from [DZone](https://dzone.com/articles/face-detection-using-html5" rel="noopener" target="_blank" title=")_

### 4. tracking.js

If you are only looking to build a quick face detection app, such as a web version of the snapchat filters, you should take a look at [**tracking.js**](https://trackingjs.com/). This framework allows integration of face recognition with JavaScript with a fairly simple setup. I have also wrote a [**guide**](https://medium.freecodecamp.org/how-to-drop-leprechaun-hats-into-your-website-with-computer-vision-b0d115a0f1ad) on this framework dropping a leprechaun hat onto faces for St. Patrick’s Day.

![Image](https://cdn-media-1.freecodecamp.org/images/ntEODKKA39CkXs9Q8Fcb8uMBEaVC0OZZZpot)
_tracking.js face detection [example](https://trackingjs.com/examples/face_hello_world.html" rel="noopener" target="_blank" title=")_

### 5. WebGazer.js

Whether you are trying to perform user experience studies or creating new interactive systems for your game or websites, [**WebGazer.js**](https://webgazer.cs.brown.edu/) can be a great place to start. This powerful framework allows our apps to know where the person is looking at with camera inputs.

![Image](https://cdn-media-1.freecodecamp.org/images/ofDdoti6XYIdLDUNfnDA4X54j8AHvNXeOpJY)
_WebGazer.js gaze tracking [example](https://webgazer.cs.brown.edu/#examples" rel="noopener" target="_blank" title=")_

### 6. three.ar.js

Another framework from Google, [**three.ar.js**](https://github.com/google-ar/three.ar.js?files=1) extends the functionalities of [**ARCore**](https://developers.google.com/ar/) onto front-end JavaScript. It enables us to integrate surface and object detection into browsers, which is the perfect tool for an AR game.

![Image](https://cdn-media-1.freecodecamp.org/images/2jPTttH19OZg9eeSQ7YXiFsQ-Xq8E2bqmk96)
_[three.ar.js](https://github.com/google-ar/three.ar.js?files=1" rel="noopener" target="_blank" title=") demo_

### In the End…

I am passionate about learning new technology and sharing it with the community. If there is anything you wish to read in particular, please let me know. Below are my previous articles related to this subject. Stay tuned and have fun engineering!

* [**How Computer Vision is Revolutionizing eCommerce**](https://medium.com/swlh/how-computer-vision-is-revolutionizing-ecommerce-d05e0ca11765)
* [**How to drop LEPRECHAUN-HATS into your website with COMPUTER VISION**](https://medium.freecodecamp.org/how-to-drop-leprechaun-hats-into-your-website-with-computer-vision-b0d115a0f1ad)

