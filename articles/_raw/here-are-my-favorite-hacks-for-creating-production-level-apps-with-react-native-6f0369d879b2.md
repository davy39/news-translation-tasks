---
title: Here are my favorite hacks for creating production level apps with React Native
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-18T21:57:29.000Z'
originalURL: https://freecodecamp.org/news/here-are-my-favorite-hacks-for-creating-production-level-apps-with-react-native-6f0369d879b2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*VCJ_bcWjUGSK19znF1KMwg.jpeg
tags:
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: React Native
  slug: react-native
- name: technology
  slug: technology
- name: tips
  slug: tips
seo_title: null
seo_desc: 'By Mehul Mohan

  Trust me when I say this, React Native is hard. And it’s not the usual hard of what
  we think hard is. It is hard in terms of working with in general. In this blog post,
  I’ll go over some tips and tricks and eventually the best practice...'
---

By Mehul Mohan

Trust me when I say this, React Native is hard. And it’s not the usual hard of what we think hard is. It is hard in terms of working with in general. In this blog post, I’ll go over some tips and tricks and eventually the best practices I’ve deployed for one of my apps coded in React Native: [codedamn Android](http://play.google.com/store/apps/details?id=com.codedamn) (or [codedamn iOS](https://itunes.apple.com/us/app/codedamn/id1426709377)).

Hi! My name is Mehul. I’m a student, [youtuber](https://youtube.com/c/codedamn), [fullstack developer](https://stackoverflow.com/users/2513722/mehulmpt), app developer and can deploy servers as well. Recently, I decided to launch a developer focused platform (you guessed it right, codedamn). To get it off the ground real quick on mobile devices, I went with React Native. Partly because I’m not a huge fan of Swift and Xcode for now. But little did I know that I’d be interacting more with native code than I thought. Anyway, let’s begin with the information I want to mention.

_Note: At the time of writing this article, React Native was at v0.57-rc4. Check if some of the things are already available/fixed in recent React Native version!_

### #0: Know what you’re doing

Realize that the React Native world is a lonely world right now. You might get yourself into a problem which no one has faced till now (or you’re not able to google it properly). Always keep VCS up with your native project and regularly commit your changes (all the cool kids call it CI). It helps you to revert back to the last working copy pretty quickly without losing a lot of code.

It is equally important to know what you’re doing. You might end up breaking your project completely if you’re unaware. If you did not use a VCS, well then you are in trouble.

### #1: Upgrade your JSC

JSC (JavaScriptCore) is a webkit based JavaScript engine used by React Native on Android platforms to evaluate your JavaScript code. Don’t tell me you thought that React Native converts JavaScript into native code. It doesn’t! ;-)

Whatever JS you write is still executed as JavaScript only by JSC on Android. The problem is React Native ships with a very old version of JSC. This means you have to use babel transformations extensively. Sometimes there are bugs so nasty you’ll pull your hair every time you sit to code, because of an older version of JSC.

I learned it the hard way after wasting a day of debugging. There was an unknown random fatal error in between app execution. After studying the logs for quite some time, I came to a conclusion that the app was crashing somewhere where [Symbol.iterator] is used in the transpiled JS code by babel.

Now, Symbols is an ES6 thing. Babel did not transpile this further, and JSC was so old it wasn’t able to hold up simple things like these and crashed. I wasted almost a day behind figuring out that JSC upgrade was a better solution than other patchy hacks.

Upgrading your JSC is pretty straightforward. Follow this [github repo](https://github.com/react-community/jsc-android-buildscripts) and you should be up and running in no time.

### #2: Setup Redux correctly

Redux can be a pain to setup correctly. And by setting it up correctly, I mean integrating it deeply with your app. Whether it is your own reducers or whether it is React navigation. Setting up react navigation with Redux is a great decision for the long-term even though the React navigation page gives a warning about this:

![Image](https://cdn-media-1.freecodecamp.org/images/ItiPqHDhW9zo-NBMXZkcy0CW2UvMXmrAyw18)

Heck no. We’re talking about enterprise and production level apps here. Go ahead and store your navigation state in Redux and gain very fine control over your state.

But remember, with great power comes great responsibility. With such fine control over your navigation, make sure you set it up correctly. Or else your app will randomly crash. It’s going to be a pain to set it up initially, but trust me its worth the time.

Read about Redux and its integration with [react navigation here](https://reactnavigation.org/docs/en/redux-integration.html).

### #3: Use available automation tools like fastlane

Fastlane is a great command line utility for automating a lot of common tasks you’ll encounter. It is more like time optimization rather than code optimization. I think it deserves a spot here because it saves a lot of time once setup correctly.

Checkout fastlane here: [https://fastlane.tools/](https://fastlane.tools/)

### #4: Do error handling correctly

Don’t expect your users to ping you with exactly how the app crashes. With more complex apps, it is difficult to find specific steps which lead to the app crash. I use sentry.io for error handling on my apps, and I personally like it a lot. It can hook up in your build steps and even upload the sourcemap to their servers so you can see the actual code, not random garbage in your crash traces.

Sentry is available at [https://sentry.io/](https://sentry.io/)

### #5: Do debugging the right way!

Are you still using that fancy chrome inspect console to debug your React Native apps? And how about Redux? Another tab? What if you want to clear the async storage of your app? Force stop the app and clear data? Seems too tedious especially when you’re actively developing the application. Instead, use a standalone dedicated debugger for react native. Best part? It’s free!

Here’s your React Native debugger: [https://github.com/jhen0409/react-native-debugger](https://github.com/jhen0409/react-native-debugger)

### 5 quick tips:

* Keep your file structure organized. It is very important to scale your application.
* Avoid using expo for your apps. PLEASE NO. Even if you use it you’ll realize you HAVE to eject at some point, and then good luck figuring out all the mess. It’s not impossible, it will eat a lot of your time later on. Remember, expo is good but we’re talking about long-term business/startup related apps and not a cat age app (for which expo would be good).
* MAKE SURE to create a package-lock.json file (if using npm). You’ll regret it a big time later when you accidentally remove your node_modules folder and realize no package on npm cares about semantic versioning.
* Do not use very heavy UI libraries with React Native. It slows down performance even in production. I do not recommend [NativeBase](https://nativebase.io/) as of now, even though it seems very fancy in terms of UI. It’s expensive on performance. There are much better options available like [react native paper](https://github.com/callstack/react-native-paper).  
Thanks to [Andre Biel](https://www.freecodecamp.org/news/here-are-my-favorite-hacks-for-creating-production-level-apps-with-react-native-6f0369d879b2/undefined) for the comment, please make sure to review this doc page thoroughly if you’re tired of slow RN apps and/or profiling them. It is a goldmine: [https://facebook.github.io/react-native/docs/performance.html](https://facebook.github.io/react-native/docs/performance.html)
* Take advantage of React Native’s replacing JS bundle on the fly without re-submitting the app to app stores using technologies like [CodePush](https://microsoft.github.io/code-push/).
* Get comfortable with at least the basics of native code on both platforms. Especially the build files on Android and pod files on iOS. Those are some files you’ll spend most of your spending-time-on-native time on.

I will continue to write blog posts on React Native as a series of posts, maybe, let’s see!

### Questions?

Ask away in the comments below! I’ll be happy to help.

**_Quick shameless plug:_** _If you’re getting started with React Native, here’s my 95% off course on how to get started with it: [React Native — The First Steps](http://bit.ly/rn-basics-medium)_

