---
title: How Animations Work in React Native
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-17T14:08:45.000Z'
originalURL: https://freecodecamp.org/news/how-react-native-animations-work
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/poster.jpg
tags:
- name: mobile app development
  slug: mobile-app-development
- name: React Native
  slug: react-native
seo_title: null
seo_desc: 'By Mehul Mohan

  React Native is a great framework that lets you create cross platform mobile applications.
  It''s especially helpful if you''re a web developer and want a fast, low cost solution
  to develop native mobile applications that work on both And...'
---

By Mehul Mohan

React Native is a great framework that lets you create cross platform mobile applications. It's especially helpful if you're a web developer and want a fast, low cost solution to develop native mobile applications that work on both Android and iOS. Bonus: you don't have to spend $$$ on separate iOS, Android, and web teams. 

This not only decreases your costs, but also allows you to share a chunk of your codebase among all three (Android, iOS and Web) builds, making it easier to make changes and roll out updates. 

React Native also allows you to work pretty close to the actual OS, which is important for performance critical tasks like animations. 

Animations are an integral part of any application because they make it interactive and more appealing to the end user. But a lot of times, while working with animations, you might feel like you're working with a black box. 

So let's learn how animations work in React Native. You can start learning animations in React Native from scratch from [this free YouTube playlist](https://www.youtube.com/playlist?list=PLYxzS__5yYQmdfEyKDrlG5E0F0u7_iIUo).

# The Animated API

React Native exposes an API called Animated. It consists of a lot of wonderful things like animatable values, spring/timing animations, and events. But we're not here to discuss the API – I'll leave that to the [official docs](https://reactnative.dev/docs/animations#__docusaurus) and my [YouTube playlist](https://www.youtube.com/playlist?list=PLYxzS__5yYQmdfEyKDrlG5E0F0u7_iIUo). They do a much better job covering that for you.

What we want to discuss here is, in fact, how React Native animates stuff on the screen and what goes on under the hood.

# Two Ways to Animate

You should know [how React Native works under the hood](https://www.freecodecamp.org/news/how-react-native-constructs-app-layouts-and-how-fabric-is-about-to-change-it-dd4cb510d055/) from my other article. (Give it a quick read if you haven't already.) Since React Native makes use of React, and JavaScript, there are precisely 2 ways animations on the screen can be carried out. 

First of all, let's get one fact clear. React Native constructs actual native views on the screen, and not the ones rendered through embedded web browsers like Ionic. Because of this, if you want to animate a view in any way, that ultimately has to be done on the native view. 

JavaScript has to communicate with the OS in some way that the view needs to be updated. JavaScript runs in a different thread than the UI thread (main thread), and only this UI thread can update the views. So JS needs to use the bridge React Native provides to serialize and communicate that data to the OS.

## Do work in JS and update the native view

This approach means that you take a view which is already visible on the user's screen, and work on what needs to be done for its next position in the JavaScript thread. The steps roughly look like this:

1. The animation starts
2. JavaScript runs the `requestAnimationFrame` function - a function which **tries** to run at 60 calls/second (60 FPS)
3. JavaScript calculates the next position/opacity/transform/whatever you're animating on the view.
4. JavaScript serializes this value and sends it over the bridge.
5. At the other end of bridge, Java (Android) or Objective C (iOS) deserializes this value and applies the given transformations on the view mentioned.
6. The frame is updated on the screen.

Did you see what happened there? None of the steps actually re-render a React Native component. This means that the Animated API actually "bypasses" React's philosophy of not mutating "state" variables. 

The good news: this is actually helpful in case of animations because it'll be way too slow and bad for performance if we let React re-render a component 60 times a second!

This is all nice and good, but there's a very fundamental problem here. JavaScript is single threaded. So the asynchronous nature of JavaScript doesn't work here because animations are a CPU bound task. Let's take a look at the pros and cons of this approach.

### Pros

1. You can have very sophisticated animations written in JS and visible as native animations.
2. More control over the animation state

### Cons

1. Huge performance penalty if your JavaScript thread is super busy.
2. If the bridge is busy, there is decreased performance when the OS/JS want to communicate with each other.

That con is a big con to be honest. There's a video further down in the article which actually shows you this issue in real time. You'll see how JS screws up big time with animations when the JavaScript thread becomes busy.

### Why do JS animations lag?

The animations done in JS will start lagging when the animation is going on and the user (or app) requests some other action which must be handled by the JS thread. 

For example, imagine there's an animation occurring. This means that JS is busy running the `requestAnimationFrame` function. Assuming that the updates are themselves not too heavy, suppose a user starts tapping a button on screen which increments a counter. 

Now with the `requestAnimationFrame` being called frequently, your React virtual tree is also re-rendering again and again in order to account for the increased counter. 

Both of them are CPU bound tasks running on a single thread, so there will be a performance hit. `requestAnimationFrame` will start dropping frames because of additional work being done by the JS thread. 

All of this means you'll get a very jerky animation.

## Native Driver Animations

Worry not, because React Native actually allows you to run animations on the native driver as well! What do I mean by that, you might ask?

Well, simply put, it means that React Native offloads the animation work from the JS thread to the UI thread (the OS) and lets it handle the animation of the object. This has a couple of benefits:

1. The JS thread (and the React Native bridge) is now free for handling other intensive tasks like repetitive taps from user.
2. Animations are much smoother because there is no serialization/deserialization and bridge communication overhead.

How does React Native accomplish that? The folks at React Native allow you as a developer to provide a property called `useNativeDriver` as a boolean value when you're constructing an animation object. 

When set to true, React Native, before starting the animation, serializes the whole animation state and what needs to be done in the future. It then transfers it once over the bridge to the OS. 

From then on, the Java (Android) or Objective C (iOS) code runs the animations instead of JavaScript calculating the next animation frame and sending that data again and again over the bridge.

This speeds up animations a lot and the animations run more smoothly, especially on low end devices. Let's see a video demonstration of Native Animations vs JS-based animations in React Native:

%[https://www.youtube.com/watch?v=lsRf_PspjSs]

In this case, the steps roughly look like this:

1. The animation starts
2. JS serializes the animation info and sends it over the bridge.
3. At the other end, OS receives that information and runs the animation natively.

That's it! Animations are much lighter for the JS thread now. No more `requestAnimationFrame` running endlessly.

However, this method has its own share of pros and cons. 

### Pros:

1. Faster animations
2. Non blocking JS thread
3. Less bloated bridge

### Cons:

1. Less control over animations (JS cannot see what's happening on the screen once the "automatic" animation starts)
2. Less properties to manipulate - the native driver does not support all the properties to be animated. For example,  `width` or `height` are not natively animatable, but `opacity` and `transform` are.

In a lot of cases, you'll find that you can work around a different set of animations using the `useNativeDriver: true` to create a similar effect which cannot be achieved without setting `useNativeDriver: false`. 

The React Native team is working on adding support for more properties as we speak, but for now, I believe it works just fine at the moment.

## Conclusion

This article showed you how React Native animations actually work under the hood and why they are beautiful. 

What do you think about this article? Tell me by connecting with me on my [Instagram](https://instagram.com/mehulmpt) and [Twitter](https://twitter.com/mehulmpt) accounts! New to React Native? Start learning it on [codedamn](https://codedamn.com) - a platform for developers to learn and connect!

Peace!

