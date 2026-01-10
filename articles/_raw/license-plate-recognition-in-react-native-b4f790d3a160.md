---
title: License Plate Recognition in React Native
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-02T07:31:23.000Z'
originalURL: https://freecodecamp.org/news/license-plate-recognition-in-react-native-b4f790d3a160
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XU79Bvq2T-jmpoux2giVJQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: React Native
  slug: react-native
seo_title: null
seo_desc: 'By Sam Corcos

  Today, we at CarDash are releasing [react-native-openalpr](https://github.com/cardash/react-native-openalpr),
  an open-source React Native package for automatic license plate recognition using
  OpenALPR (iOS-only as of February 2017).

  Eno...'
---

By Sam Corcos

Today, we at [CarDash](https://www.cardash.com) are releasing `[react-native-openalpr](https://github.com/cardash/react-native-openalpr)`, an open-source React Native package for automatic license plate recognition using [OpenALPR](https://github.com/openalpr/openalpr) (iOS-only as of February 2017).

Enough talk. Here’s a GIF of the [example app](https://github.com/cardash/react-native-openalpr/tree/master/Example) (included in the repo):

![Image](https://cdn-media-1.freecodecamp.org/images/1*u1nTJMFc34aDLTPCIr0-cQ.gif)

### How to use this in your React Native app

To install, follow the instructions in the [documentation](https://github.com/cardash/react-native-openalpr). Once installed, import `Camera` from `react-native-openalpr` and add it to your React Native project.

You can find a full list of options can be found in the [documentation](https://github.com/cardash/react-native-openalpr#options), but the most important option is `onPlateRecognized`, which returns a `plate` and a `confidence` percentage. This function is where you’ll house the logic for what you want to do once you recognize a license plate.

In the example above, when the `confidence` is above 90%, `this.state.plate` is set to the incoming plate, which is then displayed to the user. This is where you might close the camera and dispatch a Redux action if you’re satisfied with result.

### How we built this package

This package is built using [OpenALPR](https://github.com/openalpr/openalpr) and the associated [iOS compilation](https://github.com/twelve17/openalpr-ios). The scaffolding for the camera functionality is based on the popular `[react-native-camera](https://github.com/lwansbrough/react-native-camera)` package.

OpenALPR accepts either a static image or an image stream, and since recognizing images from a stream is way cooler we decided to go with that approach. Unfortunately, none of the existing React Native camera libraries give easy access to an image stream, so we had to build it ourselves.

Since we’re running an image stream through an algorithm (OpenALPR), we need to understand how the algorithm works at a basic level so we can optimize the images that we feed into it.

The algorithm can take any image, but when it receives an image it’s going to run some pre-processing. So if you want to be performant, you need to minimize the number of operations that the algorithm needs to run.

#### Image quality

One thing that the algorithms in OpenCV and OpenALPR do is down-sample (reduce the quality) of your image. Basic edge detection doesn’t require high-resolution. In fact, high-resolution is often an enemy of edge detection, because it introduces noise. Down-sampling acts as a blur and removes unnecessary details.

Knowing that the algorithm is already going down-sample your image, you can optimize your input data by passing in images that are already low-resolution. When you ask for video frames (frame buffers) you can define the resolution that you want to receive. In iOS, you would do this by accessing a preset. `AVSessionPreset` is a parameter that you give the `AVFoundation` framework, which gives you low-level access to the camera.

Most people default to high-resolution images, but since you know that the algorithm is down-sampling anyway, you can let the iPhone camera do all the work with no computation expense rather than processing a memory-intensive image conversion after the fact.

#### Pixels

Another thing the algorithm does is convert the image to grayscale, since edge detection algorithms work on best in a grayscale color plane.

If you want to be clever, you can choose a non-standard pixel format. Ordinarily your images come back as `RGBA`, where R is red, G is green, B is blue, and A is alpha (opacity). You may have also seen `CMYK` (cyan, magenta, yellow and key) if you work with Illustrator or printed materials.

Using `RGBA` as the example, each pixel is represented by 0–4 bytes. In order to get a grayscale image from `RGBA`, you’d need to take the average of the `RGB` components, which corresponds to 3 reads, 3 multiplications, and 2 adds to get grayscale.

Enter `Y'CbCr`, where `Y'` is the brightness and `Cb` and `Cr` are colors.

> Y′ is the [luma](https://en.wikipedia.org/wiki/Luma_(video)) component and CB and CR are the blue-difference and red-difference [chroma](https://en.wikipedia.org/wiki/Chrominance) components. -Wikipedia

In `Y'CbCr`, data is encoded differently. Y prime (`Y'`) is effectively the same as the grayscale information you would get from the `RGB` computation above but doesn’t require a computation step. So if you specify this pixel type, you save some processor time.

This is, as far as we know, the most efficient way to get your data input so that it doesn’t need to be pre-processed.

#### Orientation

Although you can take in optimized images at this point, you still have to handle orientation. Any OCR (optical character recognition) algorithm needs to know which direction is up, since letters lose their meaning when they’re upside down or sideways.

The native way that the iPhone takes in images is in landscape mode with the home button on the right, so in order to get our algorithm to work in portrait mode, you have to recognize the orientation and rotate the image. Fortunately, there’s an efficient way to do this and OpenCV provides an efficient method for rotating images.

#### Coordinate mapping

The last piece is to draw the rectangle around a recognized license plate. When you use the native camera in portrait mode, it puts a letterbox around the camera output. If you try to make the camera full-screen, it’s going to stretch the image to fill the available space. This is called “video gravity.”

In the image below, you can see that the phone on the left is full-screen, which causes the can of WD-40 to appear slightly larger than it does in the camera to the right, which is letterboxed.

![Image](https://cdn-media-1.freecodecamp.org/images/1*71BUUolW8CBdaGyJkGSJBw.jpeg)
_Left camera is experiencing video gravity_

So how do you map the coordinates of the plate from the image space (coordinate system) onto the screen coordinate system, taking into account the aperture ratio, the video aspect ratio, and the video gravity?

The way you do that is to first map the coordinates with `0,0` as the top left and `1,1` as the bottom right. If the orientation is something other than landscape mode with the home button on the right, you need to calculate it slightly differently. Then you map those coordinates onto the screen coordinate system using the magic method given to us by iOS: `pointForCaptureDevicePointOfInterest`

This method takes the normalized coordinate in the image coordinate space and maps it to a coordinate in the screen space. It automatically takes gravity and everything else into consideration for you.

And that’s a wrap.

### Contributors

* Evan Rosenfeld - Evan is the founder of Avocado Hills and technical advisor to CarDash.
* [Your name here] - If you’d like to contribute, send us a pull request— especially if you’re a Java developer interested in building out our Android functionality ?.

_Sam Corcos is the co-founder of [CarDash](https://www.cardash.com), a full-service automotive concierge provider that eliminates the hassle of auto service, care, and maintenance. He is also the author of [Learn Phoenix](http://learnphoenix.io), and lead developer and founder of [Sightline Maps](http://sightlinemaps.com)._

