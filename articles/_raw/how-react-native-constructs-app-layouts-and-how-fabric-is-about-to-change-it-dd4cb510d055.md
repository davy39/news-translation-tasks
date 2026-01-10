---
title: How React Native constructs app layouts (and how Fabric is about to change
  it)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-17T17:38:30.000Z'
originalURL: https://freecodecamp.org/news/how-react-native-constructs-app-layouts-and-how-fabric-is-about-to-change-it-dd4cb510d055
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ujoyIWzko6WTIW8HhpIBwA.jpeg
tags:
- name: mobile app development
  slug: mobile-app-development
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Mehul Mohan

  The React Native team has been working on something which is fundamentally going
  to change how the internals of React Native communication work with the host Operating
  System. It is nicely codenamed “project fabric” (until there’s an o...'
---

By Mehul Mohan

The React Native team has been working on something which is fundamentally going to change how the internals of React Native communication work with the host Operating System. It is nicely codenamed “project fabric” (until there’s an official name released).

Let us discuss what it actually is and what changes it brings to you as a developer.

### How React Native works right now

If we take a look, React Native right now uses 3 threads:

![Image](https://cdn-media-1.freecodecamp.org/images/1*fKuJS2I7kvpcyII3x0Mxww.jpeg)

1. UI Thread — This is the main application thread on which your Android/iOS app is running. It has access to UI and your UI can be changed only by this thread.
2. Shadow Thread — This thread is the background thread used by React Native to calculate your layout created using React library.
3. JavaScript Thread — This thread is the place where your JavaScript code (your React code, essentially) lives and executes.

#### The inner workings…

Let’s start from the beginning. Suppose you want to draw a red box in the center of your screen. So what happens is that your JS thread contains code to create a layout, i.e. that red box on the screen. Here’s a typical code snippet which might achieve that for React Native (RN):

```jsx
<View style={{ flex: 1, justifyContent: "center", alignItems: "center" }}>
<View style={{width: 100, height: 100, backgroundColor: "red"}}></View>
</View>
```

The host operating system has its own layout implementation and does not follow the kind of flexbox code you just wrote. Therefore, RN first of all has to convert your flexbox coded layout into a layout system which your host operating system can understand.

Hold on! Before doing that, we need to offload this layout calculation part to another thread so we can keep executing our JavaScript thread. Hence, RN uses the Shadow Thread which essentially constructs a tree of your layout you coded in your JS thread. In this thread, RN uses a layout engine called [Yoga](https://github.com/facebook/yoga) which converts the flexbox-based layout into a layout system which your native host can understand.

React Native uses something called a React Native bridge to communicate this information from the JS thread to the Shadow thread. In a nutshell, this simply serializes the data in JSON format and transfers it as a string over the bridge.

At this point, we’re in the Shadow thread. The JS thread is executing and there’s nothing drawn on the screen.

Now, once we have the rendered markup from yoga, this information is again transferred to UI thread via the React Native bridge. Again, this does some serialization on the Shadow thread and deserialization on the main thread. Here, the main thread then renders the UI.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jsICCO6sFLBZt1Bd0VNPfQ.jpeg)

### Problems with this approach

If you see, all the communication among threads happens over a bridge which works, but is full of limitations. These include:

* it’s slow to transfer large chunks of data (say an image file converted into base64 string), and
* there’s unnecessary data copying if the same task can be implemented just by pointing to the data in memory (again, say an image)

Next, all communication is asynchronous, which in most cases is good. However, there is no way currently to update the UI thread from the JS thread synchronously. This creates a problem when you’re using, say, FlatList with a huge list of data. (You can think of FlatList as a weaker implementation of RecyclerView.)

Finally, due to this asynchronous nature of communication between the JS thread and UI thread, native modules which strictly require synchronous data access cannot be used to a complete extent. For example, RecyclerView’s Adapter on android requires synchronous access to the data it is rendering for not having flickers on screen. This is not possible right now due to the multi-threaded architecture setup by React Native.

### Introducing Fabric

Take a step back and think about your browser. If you take a deeper look, the input fields, the buttons, etc. are actually Operating System-specific. Therefore, it is your browser which asks your OS (Windows, Mac, Linux, or pretty much anything else) to draw, for example, an input field somewhere on a webpage. Holy moly! See the beautiful mapping from browsers to React Native.

* UI Thread → UI Thread
* Browser rendering engine → React Native rendering engine (Yoga/Shadow thread)
* JavaScript thread → JavaScript thread

We know that modern browsers are very mature and handle all these tasks efficiently. So why not React Native? What is the missing piece of the puzzle which brutally restricts React Native but not browsers?

#### Exposing Native API calls directly to JavaScript

![Image](https://cdn-media-1.freecodecamp.org/images/1*AYVSGcao8TZW-POMIZRTeg.jpeg)

Have you ever just written commands like `document.getElementById` and commands like `setTimeout` and `setInterval` in your console and seen the output? Oh! Their implementation is actually `[native code]` ! What does that mean?

You see, when you execute these functions, they do not call any JavaScript code. Instead, these functions are linked directly to native C++ code which is called. So the browser does not let JS communicate with the host Operating System using bridging, but instead, directly exposes JS to the OS using native code! In a nutshell, this is what React Native Fabric would do: eliminate the bridge and let the UI be controlled directly from the JS thread using native code.

### Takeaways

1. RN Fabric allows the UI thread (where UI is drawn) to be in sync with the JS thread (where the UI is programmed)
2. Fabric is still under development, and the React Native team did hasn’t mentioned a public release date as of now. But I’m pretty sure that we’ll see something awesome this year.
3. Frameworks for app development like these (RN, NativeScript, Flutter) are getting better day by day!

_Image sources: [https://www.slideshare.net/axemclion/react-native-fabric-review20180725](https://www.slideshare.net/axemclion/react-native-fabric-review20180725)_

### TL;DR

%[https://youtu.be/zsnSqdXqs64]

### Liked this article?

If you liked this article, feel free to give me some claps and connect with me on [twitter](https://twitter.com/mehulmpt). You know the best part? Claps and twitter both are free! If you have any questions, feel free to drop them in the comments!

**_Quick shameless plug:_** _If you’re getting started with React Native, here’s my 95% off course on how to get started with it: [React Native — The First Steps](http://bit.ly/rn-basics-medium)_

