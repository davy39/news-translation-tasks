---
title: 'Unity vs SceneKit: which tool you should use to build your ARKit app'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-25T18:18:58.000Z'
originalURL: https://freecodecamp.org/news/unity-vs-scenekit-which-tool-you-should-use-to-build-your-arkit-app-3e93122058b1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*yEpBSt5NBKYBhYGdqPv1hw.png
tags:
- name: Game Development
  slug: game-development
- name: iOS
  slug: ios
- name: General Programming
  slug: programming
- name: Swift
  slug: swift
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Neil Mathew

  Everything I wish I knew before building my first ARKit app.


  When starting ARKit development, the first question almost everybody has is what
  tools should I be using to build my AR app? The two most commonly used tools seem
  to be Unit...'
---

By Neil Mathew

#### Everything I wish I knew before building my first ARKit app.

![Image](https://cdn-media-1.freecodecamp.org/images/CcAQzXvdxuV7jc7CqvVMEAVbq5aVlJJHb32Q)

When starting ARKit development, the first question almost everybody has is what tools should I be using to build my AR app? The two most commonly used tools seem to be **Unity** and **SceneKit —** but which is better? Which one is more powerful, flexible, and easier to learn? Which one has the most support?

I’ve had to work through most of these questions myself, as have most developers who have launched AR apps so far. So I thought it would be useful to dive into the main differences between the two platforms to help you make an easier decision about how to invest your time.

If you’re getting started with AR development, **here’s a few things I wish I knew about Unity and SceneKit before I built my first AR app.** So here goes.

### **First, a quick overview:**

[**Unity**](http://unity3d.com) is mature a 3D game engine, which has gotten closely linked to VR and AR because of its strong focus on 3D content. The primary language of development is C#. ARKit development in Unity is done with the Unity ARKit plugin that wraps the ARKit SDK in C# scripts for easy access to all ARKit functions.

[**SceneKit**](https://developer.apple.com/scenekit/) is Apple’s take on a 3D game engine for native iOS development and comes directly integrated with Xcode. The primary languages are Swift and Objective C.

### **Is one of them objectively better?**

When comparing two products, the most frustrating answer on the internet seems to be, “it depends.” So let me start by saying, in most cases, you’ll find that **Unity** is the better solution for AR development. There are some cases, however, where SceneKit wins, and I’ll try my best to explain the pros and cons of each tool so you can make an informed decision.

Let’s first look at two probable scenarios for AR app developers right now:

1. You’re building an App (Consumer, Enterprise etc.)
2. You’re building a Game or an “Experience”

#### **You’re Building an App**

If you’re looking to integrate ARKit into an existing iOS app, look no further. Use SceneKit. SceneKit lets you easily integrate an AR view into your app without changing anything else in your UX.

If you’re an expert iOS developer with experience with XCode, Swift, Cocapods, and so on, you should still probably use SceneKit. You’ll avoid the learning curve of a new platform and you’ll be able to pick up the ARKit SDK pretty quickly.

If you’re building a new consumer or enterprise iOS app and you love how Apple’s UI elements (like buttons, gestures and notifications) look, SceneKit is, again, the better choice. Being an Apple product, SceneKit integrates beautifully with XCode and lets you integrate your 3D scene view with all their built-in 2D UI elements in a pretty seamless manner.

The general rule here is that if 3D content isn’t the central focus of your app, and you care about iOS UX templates, go with SceneKit.

![Image](https://cdn-media-1.freecodecamp.org/images/zicyuUU8h3hK8264a0YRzyod7tFIL6b1yRPZ)
_SceneKit makes it very easy to add Native iOS 2D UI templates to your app_

The **caveat** is that if you care about quick cross-platform development across iOS and Android, or if you have a lot of 3D content like animated models, special effects, and physics planned for your app, you should consider **Unity.** It’s more mature as a cross-platform 3D development toolkit due to its roots as a game engine.

#### You’re Building a Game

If you’re building a game or an immersive experience, especially one with lots of visual 3D content like character animations, game maps, special effects and physics simulations, **Unity is definitely the better choice.**

Unity is filled with tons of built-in methods that allow you to do anything you can possibly think of. If it’s not built-in, it’s probably available on the Unity Asset store. Due to these factors, Unity saves you a lot of time compared to SceneKit, where you might spend a lot of time building and debugging basic functionality rather than building your game.

Further, Unity lets you quickly cross compile to a number of different platforms, so you can port your ARKit game to Android with only few changes to the actual AR tracking libraries. (This is changing soon too — Unity is building a cross-platform XR SDK that abstracts the low level AR libraries for an even faster port). Speed of development is often a pretty major factor for developers, and having to rewrite your app for different platforms can be a pretty big cost.

### **Decision Making Criteria**

If you don’t quite fit into the two scenarios above, or if you’re not sure whether you’re building a game, an app, a gamified app or an appified game, here’s a general comparison based on some common criteria AR developers care about.

#### 1. Performance

In general, an app or game built with SceneKit will have a smaller file size and might be more performant in some cases. When using Unity, you’re bringing along a full blown physics engine into your app. So if you’re not using heavy 3D computation, you might be better off with SceneKit.

However, keep in mind that all the camera code and other AR modules of the Unity plugin are written in Objective C, so they’re very similar in terms of efficiency. It’s mainly the heavy 3D scenes and any inefficiencies in your project design that’ll slow it down. There’s a [good thread on the topic here.](https://www.reddit.com/r/ARKitCreators/comments/6p1a37/swift_vs_unity/)

**The verdict: Unity and SceneKit are pretty equal here.**

#### 2. 3D Format Compatibility

I have personally had a painful time importing 3D models and animations into SceneKit. In general, when sourcing 3D content for your game or app, keep in mind that SceneKit will limit you to using either Collada (.dae) or Wavefront (.obj) files. Further, I’ve occasionally seen that some .obj files don’t render correctly in Scenekit.

Unity is a lot better at handling any kind of 3D format. With Unity, you can not only import .fbx files (3D models that include animations), but you can also directly load scenes from 3D design tools like Blender.

**The verdict: +1 for Unity here.**

#### 3. Ease of Debugging

Unity is a very visual IDE, with awesome visual debugging tools that let you see and interact with all the 3D content in your scene, during runtime. While you do need to run your app directly on an iOS device to properly test and debug ARKit issues, you can use tools like [Unity ARKit Remote](https://blogs.unity3d.com/2017/08/03/introducing-the-unity-arkit-remote/) to prototype the 3D interactions in your app directly in the Unity editor.

SceneKit, on the other hand, only provides console debugging within XCode. While some developers prefer this, it might get in the way of quickly testing 3D interactions in your app or game.

**The verdict: +1 for Unity here.**

![Image](https://cdn-media-1.freecodecamp.org/images/sBxLgTDS8VEOd75fXOaO6XryNCgSBnFUzkT4)
_Unity’s awesome visual scene debugger_

#### **4. Availability of Docs / Tutorials / Samples**

Unity has incredibly vast resources of documentation, tutorials, and sample code for almost anything you can build. Because of their large community of developers, there’s also a lot of tutorials built by developers.

Of course, the iOS developer community is also quite large. While ARKit itself may be new, the sheer size of the community has resulted in a good amount of samples, blog posts, video tutorials, and online courses to make your transition into an AR developer easy.

In terms of 3D content issues like 3D geometry and math, Unity wins because the large community of Unity game developers has ensured that most questions you have will have an answer somewhere on the internet.

If you’re looking to get started, here are my favorite introductory **video tutorials** for Unity and SceneKit.

**Unity**: [Build a walking zombie animation](https://www.youtube.com/watch?v=S7kKQZuOdlk).  
**Scenekit**: C[reate and view simple 3D objects](https://www.youtube.com/watch?v=f3xFpRWZEz8).

**The verdict: +0.5 for Unity here**

#### 5. Speed of development

Many developers report that the learning curve of Unity is shorter than Scenekit. This is probably because you can learn 3D content development in a much easier way on Unity, before jumping into AR development.

From a technical perspective, an AR game is really just a 3D game with a camera backdrop. Splitting your learning process this way makes things a lot more intuitive.

The other big factor here is cross-platform development. While you can’t directly build a Unity ARKit project to Android, you can at least reuse the 3D content and interactions you’ve built on any platform. You only need to plug in a new Camera Manager per device. Unity is making this even easier now by abstracting the hardware specific features like ARKit and ARCore with their new XR SDK.

**The verdict: +1 for Unity here**

### Conclusion

In general, if you’re building a game, Unity is almost always the better solution.

If you’re building an app, you need to consider if you value iOS native development and Apple’s user interface elements over cross-platform development. If your app has minimal 3D interactions, SceneKit will be the better option. Otherwise, stick with Unity.

Another piece of advice I can give you is to not spend too much time on this decision. Just get started with one. You’ll waste a lot less time trying one tool and switching if you feel like it’s not working well enough. As an iOS AR developer, both XCode and Unity will eventually be useful skillsets to acquire.

To sum it up, here’s a good quote from the [ARKitCreators subreddit](https://www.reddit.com/r/ARKitCreators/comments/6p1a37/swift_vs_unity/).

> “A decent rule of thumb would be to use Swift if your app is relatively simple, or if AR and 3D interactions are not at the core of what you are trying to build. And use Unity for the opposite.“

### Who am I?

I’m the CEO and Co-founder of [Placenote](https://placenote.com), an SDK that gives mobile AR apps the ability to permanently lock AR content to any physical location in the real world. So if you were, for example, building an app like indoor navigation, an AR graffiti app or even a multiplayer game, you should check out Placenote SDK.

Placenote SDK has sample code available for both Unity and SceneKit developers so feel free to use our sample apps to help make your platform decision!

[**You can install the SDK here**](https://placenote.com/install)

### References

I compiled this article with the help of these multiple awesome Quora and Reddit threads.

1. [What are the pros and cons of creating augmented reality apps in Swift vs Unity?](https://www.quora.com/What-are-the-pros-and-cons-of-creating-augmented-reality-apps-in-Swift-vs-Unity)
2. [Swift vs Unity](https://www.reddit.com/r/ARKitCreators/comments/6p1a37/swift_vs_unity/)
3. [I want to make AR apps, should I learn ARKit first or Unity?](https://www.quora.com/I-want-to-make-AR-apps-should-I-learn-ARKit-first-or-Unity)
4. [Is it easier to use iOS SceneKit or the Unity game engine to develop for an iOS 11 ARKit project?](https://www.quora.com/Is-it-easier-to-use-iOS-SceneKit-or-the-Unity-game-engine-to-develop-for-an-iOS-11-ARKit-project)

