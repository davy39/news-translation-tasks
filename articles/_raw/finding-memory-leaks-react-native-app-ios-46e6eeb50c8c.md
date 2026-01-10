---
title: Finding memory leaks react-native app (iOS)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-10T07:51:39.000Z'
originalURL: https://freecodecamp.org/news/finding-memory-leaks-react-native-app-ios-46e6eeb50c8c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*krH5Jncq4a9wjIikKiHP2A.png
tags:
- name: iOS
  slug: ios
- name: JavaScript
  slug: javascript
- name: mobile app development
  slug: mobile-app-development
- name: React
  slug: react
- name: React Native
  slug: react-native
seo_title: null
seo_desc: 'By Jignesh Kakadiya

  Problem:Our react-native app was working well on all devices and except iPhone 6
  it was resulting in a crash. After high level profiling we found out that its a
  memory issue. While using some heavy features in the app memory was s...'
---

By Jignesh Kakadiya

**Problem:**  
Our react-native app was working well on all devices and except iPhone 6 it was resulting in a crash. After high level profiling we found out that its a memory issue. While using some heavy features in the app memory was shooting up to 600+ MB. And since iPhone 6 has 1GB of ram, iPhone automatically kills the app.

**Solution:**  
This is what I did to reduce app total memory usage from 600MB to 60MB.

1. While profiling for memory leaks we need to make sure app is built with the release Scheme. Since dev build includes logging/warning, hot reloading features we don’t need them when checking for leaks. [This is how you can change the release build with xcode](https://facebook.github.io/react-native/docs/running-on-device.html#2-configure-release-scheme).
2. **Start tracking for leaks**  
Go to XCode → Product → Profile (⌘ + i)  
It will popup profiling templates. Please select whichever is required.  
Select `Leaks`and click on `choose`.

![Image](https://cdn-media-1.freecodecamp.org/images/cDoGQtXWVyDoua8UUIIqNsjlJaLzyE62nXhD)
_Profilers list_

3. This should open the leaks profiler on your screen. Then you can click on the `red dot` on top left corner which will **restart the app in simulator** and you can start playing with the app.

![Image](https://cdn-media-1.freecodecamp.org/images/fxTsPg0wyIhD6GNGdWCq020cNQhZTWPp13Ha)

4. This is how it looks after performing some swipes in the screen and carousel operations. I realised when I jump into the carousel screen and select an image from carousel of 12 images, memory shoots up for every single image. Result below shows us the memory taken by “in memory” image objects.

![Image](https://cdn-media-1.freecodecamp.org/images/6A-UcrCs6eyxJtaQ0LKLQGSaYGw8hHZgnIeg)

5. **Finding the cause.**  
We were using the [react-native-fast-image](https://github.com/DylanVann/react-native-fast-image) package for caching the images on that screen and since react-native doesn’t have a “better” way to cache fetched images we ended up using `react-native-fast-image`. So I decided to remove this wonderful package from my app, and result was shocking. This is what the result looks like after removing it.

![Image](https://cdn-media-1.freecodecamp.org/images/MaLE0gA8bGNEq95gdnUPP3iOT0kvHWWlQldK)

PS: Just so you know we ended up using [react-native-cached-image](https://github.com/kfiroo/react-native-cached-image), which doesn’t store image in memory.

If you are building something with react-native and need help. Please let me know.

