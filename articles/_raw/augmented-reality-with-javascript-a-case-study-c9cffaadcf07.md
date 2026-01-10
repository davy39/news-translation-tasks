---
title: How to use Augmented Reality with JavaScript — a case study
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-21T13:28:42.000Z'
originalURL: https://freecodecamp.org/news/augmented-reality-with-javascript-a-case-study-c9cffaadcf07
coverImage: https://cdn-media-1.freecodecamp.org/images/1*evN61t_cenPxPZgDZOB2Mw.png
tags:
- name: AR
  slug: ar
- name: Augmented Reality
  slug: augmented-reality
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: Virtual Reality
  slug: virtual-reality
seo_title: null
seo_desc: 'By Apurav Chauhan

  In this experiment, I talk about how Augmented Reality with JS can be used to make
  learning more fun and interactive. The case study will discuss the design process,
  implementation and feedback from children in the age group 2 to 10...'
---

By Apurav Chauhan

In this experiment, I talk about how Augmented Reality with JS can be used to make learning more fun and interactive. The case study will discuss the design process, implementation and feedback from children in the age group 2 to 10 years.

![Image](https://cdn-media-1.freecodecamp.org/images/1*evN61t_cenPxPZgDZOB2Mw.png)
_Education and Interactive Alphabets learning using Augmented Reality and Javascript_

Augmented Reality (AR) has always attracted me, and in this experiment, I try to create a practical AR application. The use-case we will cover is primary education and we will see how we can make the learning fun and interactive. We will make an app to learn alphabets in three languages primarily: Punjabi, Hindi, and English.

_The Javascript Augmented Reality app currently doesn’t have plane detection. For simplicity’s sake we are only superimposing our objects over the viewport with 3d motion tracking._

#### END GOAL

Below is a demo of our Javascript AR experiment. You can download and play with the app [here](https://play.google.com/store/apps/details?id=com.webilm.games.arlearning&hl=en).

The full code has been open-sourced for learning purposes and is available [here](https://github.com/apuravchauhan/augmented-reality-javascript).

![Image](https://cdn-media-1.freecodecamp.org/images/1*nfxElKKhaa0zlcdODDdtPg.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*O6FCNchAd2dNaJwK32GL-A.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*UKBmHOO3uW7NIKuoHYDNXA.jpeg)
_Alphabets in augmented reality and javascript to make education more fun and engaging_

### The Design Process

To make the learning fun and effortless, I am relying on the following points:

1. Active participation of the child
2. Child’s physical activity instead of sitting in one place
3. A bit of effort in finding the alphabets.
4. Intuitive UX/UI.

The core theme of the app will be quite similar to the famous Pokemon Go Augmented reality app. Only two main components will be involved: the **Camera Viewport** and **Alphabets**.

#### Alphabet UX for AR Game

_Iteration 1_

![Image](https://cdn-media-1.freecodecamp.org/images/1*_711pNZKifCSaa9bXWbc5g.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*YdiDXaHGXYKPMD1gdGbZaw.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*EmkTDWxyVZYcqA9vn2Ixtg.png)
_2d Alphabets in English, Hindi and Punjabi for our JS Augmented Reality Game_

In our first iteration we have 2d alphabets which we will try to merge in our camera viewport. The idea of the Augmented Reality(AR) app is to have children find these alphabet letters in a room or space around them. The prototype after merging the space with 2d alphabets will look something like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*gu70VjYLyFLzzmMvhafZyA.gif)
_AR Motion sensor with 2d object_

As you can see above, the immersive experience is missing with a 2d model because the human eye sees things in 3d.

_Iteration 2_

Lets try to create a 3d model and see if we can improve the experience of our Javascript-based Augmented Reality game:

![Image](https://cdn-media-1.freecodecamp.org/images/1*lHUszUcxZfFJj0f81Ebixg.gif)

![Image](https://cdn-media-1.freecodecamp.org/images/1*cyXqdHs11SmHwICi-P461g.gif)

![Image](https://cdn-media-1.freecodecamp.org/images/1*GK2PuNQlEEJU8FY9edCR8A.gif)
_3D Alphabets in English, Hindi and Punjabi for our AR project_

And below is the comparison of the experience of a motion sensor with 2d vs 3d alphabet models. As you can see, 3D naturally gives you a much more immersive experience when it comes to Augmented reality.

![Image](https://cdn-media-1.freecodecamp.org/images/1*gu70VjYLyFLzzmMvhafZyA.gif)

![Image](https://cdn-media-1.freecodecamp.org/images/1*IPTMBO-kP6EcqhL0tDD_8A.gif)
_2d vs 3d AR motion experience_

### The AR Implementation process

To implement the above AR concept, I’ll be using the following tools and technologies:

1. [Ionic Framework](https://ionicframework.com): For building the hybrid app
2. [Aframe](https://aframe.io/): For bringing the Virtual reality (VR) and Augmented Reality (AR) experience to our app
3. [MagicaVoxel](https://ephtracy.github.io/): For creating our 3D models

The basic app building process is very simple. You can follow my earlier post to learn how to go about building and deploying an app using the Ionic framework [here](https://codeburst.io/part-1-simple-ionic-tutorial-from-scratch-from-0-to-live-app-9a79db510a90).

Once you have followed the above tutorial to create a simple app, it’s time to integrate Aframe to bring our 3D alphabets with motion sensors into our app.

Just load the below Aframe core and Aframe loader libraries in ionic’s project index.html file:

```
<script src="https://aframe.io/releases/0.8.2/aframe.min.js"></script>
```

```
<script src="https://rawgit.com/donmccurdy/aframe-extras/v2.1.1/dist/aframe-extras.loaders.min.js"></script>
```

With this we are ready to do some AR/VR magic in our Javascript code base.

Now in your home component’s home.html, let’s include our 3D models exported from magicavoxel:

And this should make a 3D scene ready for interaction with all motion sensors ready:

![Image](https://cdn-media-1.freecodecamp.org/images/1*fref3HwlAuN0AJ9VHRaWhQ.gif)
_Final 3D Virtual Reality scene ready with 3D alphabets_

#### Adding Augmented Reality Effect

The final part of this experiment is to add the Augmented Reality (AR) feeling in our Javascript-based hybrid app. As already explained, Augmented Reality is when you superimpose 3D models or other objects on top of your camera viewport. So the only thing missing is the camera viewport behind our scene.

To do this, we use the camera preview plugin as explained [here](https://ionicframework.com/docs/native/camera-preview/). And here is the full gist after integration with the camera preview plugin:

We also need to ensure that our backgrounds are transparent so that the camera preview is visible in mobile. This is very **IMPORTANT** otherwise you might feel that the plugin is not working. Here is the home.scss file with transparency css enabled:

**And this is what it would finally look like:**

#### User reaction to our Augmented reality JS game

The final step to measure the success of your concept is real user validation — in our case, kids :) And below is their live feedback recorded.

It was pretty clear that each one of them enjoyed the game and we got full points on fun part. However, initially I had to tell them to move the phone in space to find the letters. Points lost in terms of intuitiveness :(

![Image](https://cdn-media-1.freecodecamp.org/images/1*Fe97s79RI5BFONl9X5T27w.png)
_Points scored out of 10_

#### User feedback for Augmented Reality JS game

### Final Thoughts

Well it was an exciting project and I could see a lot of potential for Augmented Reality in learning and education. Children really like it and it surely adds the missing fun factor to education, especially in our monotonous Education system.

Feel free to comment and share your feedback.

### Downloads

The code for this app is available in [github](https://github.com/apuravchauhan/augmented-reality-javascript). Feel free to play and push new features in it. I’ll be happy to push updates over production.

You can download the app for android [here](https://play.google.com/store/apps/details?id=com.webilm.games.arlearning&hl=en).

