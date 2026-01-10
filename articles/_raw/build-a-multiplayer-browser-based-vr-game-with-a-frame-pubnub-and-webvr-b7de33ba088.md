---
title: Build a Multiplayer Browser-based VR Game with A-Frame, PubNub, and WebVR
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-27T20:50:01.000Z'
originalURL: https://freecodecamp.org/news/build-a-multiplayer-browser-based-vr-game-with-a-frame-pubnub-and-webvr-b7de33ba088
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Iu7_DRv1Pr_9dHfkr22ZVw.png
tags:
- name: coding
  slug: coding
- name: 'tech '
  slug: tech
- name: Virtual Reality
  slug: virtual-reality
- name: vr
  slug: vr
- name: webvr
  slug: webvr
seo_title: null
seo_desc: 'By Namratha Subramanya

  Advancements in technology have made Virtual Reality (VR) more immersive and affordable
  than ever. This immersive environment can be similar to the real world. Or it can
  be fantastical, creating an experience that is not possib...'
---

By Namratha Subramanya

Advancements in technology have made Virtual Reality (VR) more immersive and affordable than ever. This immersive environment can be similar to the real world. Or it can be fantastical, creating an experience that is not possible in ordinary reality.

Better yet, high-quality VR devices are available at low prices these days. With a number of smartphone-compatible VR headsets such as Google Cardboard, Samsung Gear VR, Oculus Rift and HTC Vive, VR is showing to be the next big thing.

In this tutorial, we’ll take advantage of that and build a real-time, multiplayer VR game using A-Frame, PubNub, Glitch, and WebVR.

The [full GitHub code repository can be found here](https://github.com/namrathasubramanya/VR-Bowling-game).

### WebVR

[WebVR](https://webvr.info/) is an open specification that makes it possible to experience VR in your browser. It is a JavaScript browser API that acts as an interface for the VR hardware. WebVR is cross-platform and can be used to develop, view and share VR content on any browser that supports VR. With WebVR, you can open up a browser and get into VR just by clicking a link. Working with WebVR directly requires knowledge of JavaScript and WebGL.

### A-Frame

[A-Frame](https://aframe.io/) is a virtual reality framework that is built upon the WebVR API. It uses the WebVR API to gain access to VR headset sensor data (position, orientation) to transform the camera and to render content directly to VR headsets. A-Frame is an open community project that uses the WebVR API along with HTML, CSS, JavaScript, and Three.js. A-Frame aims for highly immersive and interactive VR content with native-like performance. At the same time, A-Frame wants everyone to be able to get involved with VR content creation. A-Frame supports all major headsets with their controllers.

### Glitch

[Glitch](https://glitch.com/~aframe) provides an online code editor with instant deployment and hosting of websites. The editor supports both front-end and back-end code as well as multiple files and directories. Glitch lets you remix (i.e., copy) existing projects and make them our own and instantly host and deploy changes for everyone to see. Firefox Nightly allows you to debug the VR content using debug console.

### Gaming Environment

#### A-Frame Physics System

`aframe-physics-system` is middleware that initializes the physics engine and exposes A-Frame components for us to apply to entities. When we use its `static-body` or `dynamic-body` components, `aframe-physics-system` creates a `Cannon.Body` instance and attaches it to our A-Frame entities, so on every frame, it adjusts the entity’s position, rotation, etc. to match the body.

#### Ball

`<a-sphe`re> primitive creates a spherical shape. You can define its radius color and position. Becau`se of aframe-physics-`system, the ball can be converted into a dynamic-body with a certain mass.

#### Bowling Lane

`<a-b`ox> creates shapes such as boxes, cubes, or walls. You can create a rectangle box and make a bowling lane out of it by placing pins and ball on top of it.

#### Pins

`<a-cylind`er> primitive is used to create tubes and curved surfaces. These cylinders can be used as bowling pins in the game. Be sure to define the radius, height, position, and mass of the cylinder.

#### Tracks

The ball cannot roll in the same direction every time you throw it. You can define any number of tracks for the ball to roll, and this track can, in turn, define the direction. This game has 5 tracks, and the movement of the ball on these tracks is controlled by 5 triangles or, let’s say, pointers on the bowling lane.

#### Surroundings

A scene is represented by the `<a-sce`ne> element. The scene is the global root object, and all entities are contained within the scene. The objects’ friction, restitution, and iterations are set to values of 0.001, 0.3 and 30 respectively.

A-Frame has an asset management system that allows us to place our assets in one place and to preload and cache assets for better performance. We place such assets within `<a-asse`ts>.

The scale component defines a shrinking, stretching, or skewing transformation of an entity. You can use the scale component to transform a box into a wall behind the bowling lane.

On similar lines, a box can be converted into a button attached to the wall by using the scale component. `<a-te`xt> can add text into your virtual environment.

`<a-b`ox> can also be used to build borders next to the bowling lane.

### The Game

#### Rolling the Ball

As discussed earlier, the ball can roll over 5 imaginary tracks on the bowling lane. This can be achieved using `<a-animati`on>. Animations can be attached in A-Frame th`rough <a-a`nimation> element by making it as a child of the entity to animate.

Now you can bind these animations of the ball with the 5 pointers so that the animation begins every time one of the triangles is clicked. This can be achieved by writing a component. We can register the component in JavaScript and use it declaratively from the DOM. Components are configurable, reusable, and shareable.

#### Falling of Pins

When a dynamic-body of mass 17.5 rolls towards 10 dynamic bodies of mass 1.25, some of them tend to fall. After every knockdown, one can count the number of pins that are down. We can check the position of the pins at the end of the animation. If any of the pin’s rotation has its x-value not equal to 0 or -0 then it means that the pin isn’t standing upright. By counting the number of pins that are lying down, you can calculate the score of the player.

The above line captures the x-value of the rotation attribute of a pin. This way you can fetch x-value of rotation attribute of all the pins and save it into an array. Now you can loop through the array and check every value and increment the `strike` counter.

#### New Game

The player can start a new game at any point of time by clicking on the New Game button on the wall. It automatically refreshes the game.

#### Moving Camera

You can move the camera at any point during the game. Here, I have chosen to move the camera every time the player rolls the ball for a better view of the falling pins.

![Image](https://cdn-media-1.freecodecamp.org/images/1*kZFpH7Qepl0i1OtR7jwmrg.png)

### PubNub

With less than 1/4th of a second latency, PubNub can smoothly publish and subscribe messages between multiple VR devices. Let’s convert this single-player game into a 2-player game.

You’ll now have to initialize your PubNub keys. [Sign up for a PubNub account](https://admin.pubnub.com/#/register/?utm_source=Syndication&utm_medium=Medium&utm_campaign=SYN-CY18-Q3-Medium-Aug-17) and create a project in the [Admin Dashboard](https://admin.pubnub.com/#/register?utm_source=Syndication&utm_medium=Medium&utm_campaign=SYN-CY18-Q3-Medium-Aug-17).

#### Deciding the Turns

Every player gets two turns. The player switch turns after every two shots. So after every two shots, PubNub can notify the other user that they can take control. In this game, every time the player gets his/her turn the 5 triangle pointers surface on the bowling lane. And when it’s not their turn, the 5 triangle pointers are hidden.

Hide the pointers when it’s not your turn. Here, instead of hiding, I am setting the position to 0.

Make the pointer surface back to the bowling lane when it is your turn. By doing this, you’ll be taking control of the tracks again.

#### Replicating the State of Pins After Knockdown

After every knockdown, you can capture the position of pins that are down and send it to the other user using PubNub. By doing so, you can replicate one player’s screen on other players’ screens. In the code below, you can see that the position and rotation values of pin 1 are passed to other players using PubNub. On similar lines, you can send rotation and position values of all the pins through PubNub.

#### Switching Between Static and Dynamic Bodies

Earlier we used `aframe-physics-system` to convert the A-Frame objects into dynamic bodies. When the player isn’t rolling the ball and is just replicating the screen of another player, the ball should not be a dynamic body in order to avoid falling of extra pins.

When it is the current player’s turn, dynamics is set to true, and the `dynamic-body` properties are added.

When it’s not the player’s turn, dynamics is set to false, and the `dynamic-body` properties are removed.

#### Player 2

Once you are done with publishing data through PubNub from Player 1’s screen, you can read the data by subscribing to PubNub’s channel.

When PubNub receives data related to the position of fallen pins’ position and rotation, you can set the attribute of pins on player 2’s screen to the same values as Player 1 and hence make the two screens identical.

### Conclusion

Congratulations! Every time you roll the ball on Player 1’s screen, you can see Player 2’s screen replicating all the movements. Now you can revert this by publishing Player 2’s data back to Player 1 and convert your game into a fully functional 2-player game. It can be converted into a multiplayer game as well. Happy VR gaming!

**The [full GitHub code repository can be found here](https://github.com/namrathasubramanya/VR-Bowling-game).**

_Originally published at [www.pubnub.com](https://www.pubnub.com/blog/build-multiplayer-browser-based-vr-game-aframe-webvr/?utm_source=Syndication&utm_medium=Medium&utm_campaign=SYN-CY18-Q3-Medium-Aug-17)._

