---
title: Lessons I learned while building in React Native
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-13T18:17:18.000Z'
originalURL: https://freecodecamp.org/news/lessons-i-learned-while-building-in-react-native-917cb7bb5993
coverImage: https://cdn-media-1.freecodecamp.org/images/1*gLt2OppZEywjKDYKkfsBQw.jpeg
tags:
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: React Native
  slug: react-native
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Amanda Bullington

  When I received an offer for a software engineering role to build an app in React
  Native, I wasn’t sure what to expect.

  On one hand, it sounded exciting to be able to build a mobile application for iOS
  and Android using a single ...'
---

By Amanda Bullington

When I received an offer for a software engineering role to build an app in React Native, I wasn’t sure what to expect.

On one hand, it sounded exciting to be able to build a mobile application for iOS and Android using a single codebase. On the other, hearing that companies like Airbnb had [tested the platform and ultimately decided against it](https://medium.com/airbnb-engineering/react-native-at-airbnb-the-technology-dafd0b43838) left me feeling like there would be a fair number of challenges ahead.

Now I’m a few months in, and here are some of the lessons I learned along the way.

#### **Choosing the right libraries**

One of the first things I learned about React Native is that the choice of third-party libraries is often limited. As a JavaScript web developer, I had a wide choice of libraries that I could customize to various projects.

React Native libraries are more complex to build. They require a knowledge of native code for iOS and Android to work across platforms. Because of this, there aren’t as many people who develop libraries for React Native.

![Image](https://cdn-media-1.freecodecamp.org/images/4j9MuYQpj3Qzl6q9BkQnkh8FGCCEF1qyeTLh)
_There really aren’t this many choices in React Native_

After some futile searching on GitHub, I ended up choosing most of my app libraries from the [React Native Community repo](https://github.com/react-native-community). These are generally the best maintained and almost guaranteed to work with the latest version of React. The [Native Directory](https://native.directory/) was another helpful place to quickly search what’s available in React Native.

Even within the RN community repo, not all libraries worked out of the box. Sometimes I needed to fork the repo and make a few tweaks of my own. Other times, I needed to downgrade to a version that fixed the particular bug that showed up in my app. Version control is all the more important when there are few libraries and few maintainers.

#### **Getting comfortable with Flexbox**

With more than 10,000 types of devices for Android alone, it can be tricky to build an app that works for all screen sizes. I needed my app to look good on devices as small as the iPhone SE and as large as the Pixel 2XL.

At first, I tried styling my app by using React Native’s built-in Dimensions class to find the width and height of each screen. Ultimately, this was too complicated to maintain as the app grew. Instead, Flexbox is the key to being able to tackle styling across screen sizes gracefully. A quick run through of the [Flexbox Froggy](https://flexboxfroggy.com/) tool is a good way to get up to speed.

Flexbox didn’t solve all my styling problems. I still encountered quirky screen sizes that needed their own styling solutions like the [SafeAreaView](https://facebook.github.io/react-native/docs/safeareaview) for the iPhone X series. I also needed to use conditional statements for different iOS and Android styling on many screens. But overall, it’s a great tool for designing apps in React Native.

#### **Turning it off and back on again**

Once I installed a new third-party library and ran `react-native link`, I often ran into the “undefined is not an object” error. React Native is known for its non-descriptive error messages. It took me a while to figure out what this meant. At first, I thought there was something wrong with the library. Or that it didn’t work with the version of React Native I had installed.

Then, deep in a GitHub issue thread for one particular library, I found [this comment](https://github.com/react-native-community/react-native-image-picker/issues/269#issuecomment-326609908) that finally shed light on why none of my libraries were working smoothly.

Like many developers, I had gotten into the habit of simply reloading my project while running `react-native run-android` or `react-native run-ios`. Hot-reloading is great for saving time while making tiny styling tweaks to the app and checking out screens. However, it does not help integrate new libraries into the app. My new libraries wouldn’t work until I closed all my simulators/emulators, disconnected my devices, and re-ran `npm start` to restart the Metro bundler.

In other words, I needed to turn everything off and back on again to smoothly integrate third-party libraries without misleading error messages.

#### **Working without a debugger**

![Image](https://cdn-media-1.freecodecamp.org/images/Hu2yf4yDMQizsYlGJGLbGTjMoNrOxFLKNj75)
_Photo by [Pexels](https://www.pexels.com/@mikebirdy?utm_content=attributionCopyText&amp;utm_medium=referral&amp;utm_source=pexels" rel="noopener" target="_blank" title="">Mikes Photos</a> from <a href="https://www.pexels.com/photo/ladybug-plastic-toy-198101/?utm_content=attributionCopyText&amp;utm_medium=referral&amp;utm_source=pexels" rel="noopener" target="_blank" title=")_

As a web developer, I was practiced at searching for bugs in the Google Chrome debugger. In React Native, it only took a few weeks before I lost my ability to debug in Chrome.

One of the constraints of my app was that I needed to use Realm as my primary database. However, Realm has a [frequently reported issue](https://github.com/realm/realm-js/issues/2128) where it cannibalizes the Chrome debugger, making it impossible to use. I needed to find a different solution.

React Native has a [built-in debugger](https://facebook.github.io/react-native/docs/debugging) where you can log console.logs to the terminal with `react-native log-android` or `react-native log-ios`. While this works well on Android, I ran into [issues](https://github.com/facebook/react-native/issues/9441) using this debugger for iOS. I began to adopt an Android-first approach to development, where I would build and test everything on Android to easily access console.logs, then make tweaks to the iOS version as needed. I also invested in writing better error messages within my app, which benefited both my users and me.

I also experimented with using XCode and Android Studio to debug, but I ultimately found my Android-first approach to be the easiest solution with the least amount of screen switching.

#### **Running production builds early**

Experienced React Native developers have told me that they rarely run into any issues in production mode that they didn’t already see and solve for in development. That wasn’t my experience. When I ran my production builds on physical devices, I was able to catch a few errors that I hadn’t spotted before.

![Image](https://cdn-media-1.freecodecamp.org/images/w4OEUSr1hMms6sjVU1eUO7CRFthO3B93JJoG)
_Ready, set, production_

One example was navigation. Setting up navigation in a mobile app was tricky for me to wrap my head around at first, and I needed to make a few changes to the way I set up my react-navigation library to deliver data to the user at the right time. Using a physical device let me simulate all the ways a user might run through my app (i.e. when they would move to a new screen vs. pressing the back button) and set up navigation accordingly.

Another issue that I found in production involved dangerous [Android permissions](https://facebook.github.io/react-native/docs/permissionsandroid). Newer Android phones require more explicit permission requests, and once I tested on a physical device, I realized that my app’s photo gallery needed these permissions to load correctly.

#### **Conclusion**

React Native is well-documented and relatively quick to learn, especially if you already know React. It’s immensely satisfying to build a mobile application that works across both iOS and Android with a single codebase.

The challenges I ran into above were some of the trickier parts — but overall, there weren’t any huge hurdles to developing an app in React Native. Mostly, I needed to wrap my head around the quirks of mobile development and get comfortable with some of the awkward error messages. Now that I’m past these initial learning curves and settled on an Android-first approach, development is much faster.

Would I develop in React Native again? Absolutely.

