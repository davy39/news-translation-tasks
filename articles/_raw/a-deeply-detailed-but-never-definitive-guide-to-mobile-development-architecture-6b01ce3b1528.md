---
title: A deeply detailed but never definitive guide to mobile development architecture
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-05T16:34:24.000Z'
originalURL: https://freecodecamp.org/news/a-deeply-detailed-but-never-definitive-guide-to-mobile-development-architecture-6b01ce3b1528
coverImage: https://cdn-media-1.freecodecamp.org/images/1*kHze88HBCkKt8Tw4MESC9Q.png
tags:
- name: JavaScript
  slug: javascript
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Jose Berardo Cunha

  Native, Web, PWA, hybrid, Cross-Compiled… what is “the best” way to develop for
  Android and iOS platforms? What looks reasonable? And how are you supposed to choose
  among the options? In this article, I’ll lay it all out so you ...'
---

By Jose Berardo Cunha

Native, Web, PWA, hybrid, Cross-Compiled… what is “the best” way to develop for Android and iOS platforms? What looks reasonable? And how are you supposed to choose among the options? In this article, I’ll lay it all out so you can make an informed decision.

First things first, let me provide you with a bit of context. I am an IT senior consultant, and the idea of putting together this guide was born from discussions with one of our clients about what could be the best approach for them. Yes, just for them. And we realized that we did not have a well-defined strategy, a solid and reliable foundation, to help us come up with the right answer.

And you know what? I could not find such a guide easily anywhere on the Internet, either. Although there are several articles about this topic, none of those I came across were reasonably complete. Unfortunately the majority overlook a lot of concepts or, even worse, are essentially wrong.

Now, I’d like to take a wider look. And while I’m potentially helping someone make their own decisions, I’m also asking around the community for more thoughts on the subject.

This guide has two parts:

1. Mobile Development Architectural Tiers (this)
2. How to make your decision

It's also available on [YouTube as a series of 10 videos](https://www.youtube.com/watch?v=B_vADCc-3HI&list=PLrUPmiKGH0g6TyS3F_FqOxnxWNXhZBqkR) and as a [free course on Udemy](https://www.udemy.com/mobile-development-architecture). There, you’ll find the same written material as here, the same videos from the YouTube series, as well as quizzes to fix all the topics and a final certification.

So let’s get started.

### Introduction

When it comes to mobile platforms, [it's arguable that there are just two big players](http://gs.statcounter.com/os-market-share/mobile/worldwide): Android and iOS. Other technologies like Tizen, Blackberry, or Windows Phone are either dead or have been around for a while and have no prospects of reaching any significative market share.

A quick look at this massive duopoly might make you think that developers do not have many options when creating mobile apps. This idea can't be further from the truth, though. You can quickly spot a fistful of programming languages being used out there: C/C++, Java, Kotlin, Objective-C, Swift, JavaScript, TypeScript, C#, Dart, Ruby, and I'm pretty sure I’ve missed a few more.

The same is true of mobile development frameworks. Unless you are not a developer, or have somehow been unaware of new technologies for the last 10 years, you’ve probably heard about Cordova/PhoneGap, React Native, Xamarin, Ionic, Nativescript, or Flutter, just to name a few cross-platform solutions for mobile apps.

So let’s look at all these pieces of the architecture and break things down a bit.

#### TL;DR

There's no clear winner. All approaches have pros and cons, and might be either the best fit or the worst fit for your next project. In this guide, I'm classifying many different solutions into various tiers according to the distance their architectures are from the native platform.

### Native Apps

To start, let's go straight to the metal. Our first architectural tier is Native Apps.

![Image](https://cdn-media-1.freecodecamp.org/images/1*y6li0mJWKGdZ95utOH7meA.png)
_Native Apps Tier — Where you develop for each specific platform (it might be even more specific when considering NDK)_

This is the tier where you must be aware of the idiosyncrasies of each platform. It’s not my intention to dig into them, I just want to mention a few things in a bit of context.

#### iOS

Starting on the iOS side, just because it's simpler, there's only Apple ruling the world. Originally, developers needed to learn Objective-C, a proprietary object-oriented variation of C with some inspiration from SmallTalk ([and an insanely long-named API](https://mackuba.eu/2010/10/31/the-longest-names-in-cocoa/)).

In 2014, Apple announced Swift, a multi-paradigm language, which was a lot easier than its predecessor. It's still possible to deal with Objective-C legacy code, but Swift has reached high maturity levels. So, if you're planning to learn how to natively develop for iOS, Swift is definitely where you should start.

#### Android

On the Android side, there are a number of different manufacturers. The [vast majority of them rely upon ARM processors](https://www.androidpit.com/fastest-smartphone-processors). But generally speaking, Android apps lay on virtual machine instances ([instances of ART](https://developer.android.com/guide/platform/index.html#art)) to help deal with potential underlying specificities ([not without many amazing tricks](https://source.android.com/devices/tech/dalvik/#features)).

That's why, originally, the language of choice was Java. It’s not only been the most popular language in the World for almost two decades ([with a few position swaps with C](https://www.tiobe.com/tiobe-index/)), but it’s also notable for its Java Virtual Machine (JVM). This empowered developers to compile their code down to an intermediate bytecode that could be read and run by the JVM.

With the Android Native Development Kit (NDK), it's also possible to develop critical parts of the app directly in native code, writing in C/C++. In this case, you have to be aware of underlying platform quirks.

Kotlin is a language unveiled by JetBrains in 2011. When it first came out, despite its flexibility and conciseness, it wasn't more than yet another JVM language with more successful competitors like Scala, Clojure, or Groovy. However, after its first major release in 2016, it rapidly started to stand out from the crowd, especially after Google announced that it would be officially supported on the Android platform at [Google I/O 2017](https://www.youtube.com/watch?v=EtQ8Le8-zyo).

Kotlin is becoming Google's first class language (currently Kotlin and Java — in this order — are used throughout Android's official documentation). A total Java replacement is expected even more so now that the US Federal Appeals Court has ruled on the [endless lawsuit](http://money.cnn.com/2018/03/27/news/companies/google-oracle-case/index.html) filed by Oracle accusing Google of violating Java copyrights.

### Native components

Developing in this tier, you can also leverage all native APIs and, in particular, the native components. This saves your app from having to reinvent the wheel.

I've published a video demo of how to create a simple project on Xcode (iOS) and Android Studio. If you want to check it out:

#### Native Apps advantages

* Best performance and top user engagement
* Bleeding edge native features
* Notably good IDEs Android Studio / Xcode
* Modern high-level languages Kotlin / Swift
* Very low-level approach with NDK

#### Native Apps disadvantages

* Two codebases to maintain
* Require installation (except Android Instant Apps)
* Hard to analyze SEO
* Very expensive to get users to download the app

### Web Apps

On the other side of the spectrum, we have Web Apps. Web Apps are essentially apps run by the browser. You don't write code targeting the platform, but rather any browser running on top of it.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HIDGvnpanv4vQ3vLrc7IhA.png)
_Web Apps Tier — clearly on top of a browser bar targeting a beast sitting in between Android and iOS._

In this tier you’ll find an insane number of contenders jumping at each other's throats. But they all use an arsenal consisting of the same weapons: HTML, CSS, and Javascript.

Web frameworks and libraries, even when leveraging CSS pre-compilers like [LESS](http://lesscss.org/) or [SASS](https://sass-lang.com/), even Javascript pre-compiled languages like [TypeScript](http://www.typescriptlang.org/), [CoffeeScript](https://coffeescript.org/) or [Flow](https://flow.org/en/), even symbiosis like [JSX](https://reactjs.org/docs/introducing-jsx.html) or [Elm](http://elm-lang.org/), leaving alone tools like [Babel](https://babeljs.io/) used to transpile everything to Javascript with different configurable levels of conformance with ECMAScript yearly specifications (ES6 / ES7 / ES8, or if you prefer ES2015 / ES2016 / ES2017 / ES2018).

At the end of the day, they all are HTML, CSS, and JavaScript rendered and run by the browser. There's no direct access to native APIs like camera, vibration, battery status, or file system, but some of them can be achieved via Web API's:

![Image](https://cdn-media-1.freecodecamp.org/images/1*JZu_xrK3KAbCL_qaIS4jHw.png)
_[Can I rely on the Web Platform features to build my app?](https://whatwebcando.today" rel="noopener" target="_blank" title=")_

The big issue with Web APIs is their maturity level. Many of them are not supported by some browsers. There are differences in implementations, especially across mobile browsers.

#### Web App advantages

* Shared code between platforms and desktop browsers
* Do not require previous installations, just navigate and use
* Tons of frameworks and libraries to go with them
* Best for SEO

#### Web App disadvantages

* Lower performance
* Hard to get a native user experience
* Require an internet connection
* Not available on official app stores
* API not as mature and reliable as native API

### Frameworks and Web components

[Angular](https://angular.io/), [React](https://reactjs.org/), and [Vue](https://vuejs.org/) are probably the most popular web frameworks as of 2018. To be precise, however, React is considered just a library due to its flexible and less opinionated nature. Angular, on the other hand, is a strongly opinionated framework. Vue lives at some point in between them.

![Image](https://cdn-media-1.freecodecamp.org/images/1*hWUMcJv-8wWJni6PDOAAaQ.png)
_Angular vs React vs Vue_

Angular, originally called [AngularJS](https://angularjs.org/), was presented to the world in 2010 by Google. It quickly started to shine, due to its inversion of paradigms in comparison with other libraries from that time (like [jQuery](https://jquery.com/), the most popular back then). Instead of directly talking to HTML elements to manipulate the UI state, with AngularJS, templates were magically updated whenever the JavaScript model was updated.

As AngularJS became more and more popular, it also grew in purpose. It turned into a complete and opinionated framework that was one of the first that took SPAs (Single Page Apps) seriously. This growth (in both aspects) was responsible for some API bloats and performance issues.

React was created by Facebook to solve their own needs on the presentation layer. It introduced many aspects that suddenly became very popular, like virtual DOM, one-way data flow (originally named [Flux](https://facebook.github.io/flux/docs/in-depth-overview.html#content), especially popular through an implementation library called [Redux](https://redux.js.org/)), and a mixture of HTML and JavaScript called [JSX](https://reactjs.org/docs/introducing-jsx.html).

Only in 2016, after long debates and unexpected big changes, Google launched version two of its popular web framework. They called it Angular, instead of AngularJS. But, as many people already called the first version “Angular” (without the "JS" suffix), people started calling the new version Angular 2. That turned into a naming problem, as Google also announced that it would release new major versions every 6 months.

In my opinion, that was a mammoth mistake. I've seen this before (with Struts vs Struts 2/WebWork, for example). They have a massively popular product that appears to have reached its plateau, and it has started to be more criticized than praised. If Google decides to rebuild it from the ground up, they should never, by any means, just change its major version. How will people trust that they will not repeat it every new major version release? Version two is supposed to present breaking changes, but it doesn't mean it can be totally revamped.

Angular is a spectacular web framework, and I really feel passionate about it. However, it's a completely new beast. It does not have much to do with AngularJS. Even Vue, which is another amazing framework (probably one of the most pleasant to work with, by the way) looks more similar to AngularJS from a bird's-eye view. I believe this caused a significant movement away from Angular and contributed substantially to React's popularity.

Vue is the only one of the three most popular web frameworks that is not backed by a big company. It was actually started by a former Google developer. Due to its formidable simplicity and tiny footprint, it got attention from a massive and enthusiastic community.

Although there are more complete solutions, they all work on top of the concept of [web components](https://www.webcomponents.org/). There's an open specification about them currently in progress in W3C, and some interesting implementations like [Polymer](https://www.polymer-project.org/), [Stencil](https://stenciljs.com/) and [X-Tag](https://x-tag.github.io/).

In the third video of the series, I don't spend too much time discussing frameworks but discuss web component libraries:

### Mobile Apps vs Web Apps

I’m not sure if you’ve noticed, but the order of tiers I'm presenting here follows what I think is the easiest path to learn all approaches. I started from the Native Tier, the most genuinely mobile development. Then I decided to fly directly to the other extreme to present the Web Tier, which is the tier that has been available since the first smartphones.

Only now, after elaborating on a comparison between the two edges of my diagram, will I start talking about many of the cross-platform approaches to build mobile apps.

There's a long debate between Mobile Apps vs Web Apps. Everything I say about Mobile Apps is not exclusive to the Native Tier. It is also applicable to all cross-platform tiers I present later on.

#### The user behavior dilemma

![Image](https://cdn-media-1.freecodecamp.org/images/1*OYBXoiGa1wc3jYpxnJwUog.png)
_Users spend more time on Mobile Apps (87%) than on Mobile Websites (13%)_

According to a [Comscore survey in 2017](https://www.comscore.com/layout/set/popup/Request/Presentations/2017/The-2017-US-Mobile-App-Report?logo=0&c=12), a user's fidelity to a mobile app is way more relevant than it is to mobile websites. According to an [aligned article on Forbes](https://www.forbes.com/sites/quora/2017/12/19/why-many-online-shopping-sites-are-becoming-mobile-shopping-apps/#1e86018f62c2), this is usually because of convenience (for example, home screen buttons, widgets, top notifications), speed (for example, smoother interfaces, almost instant start ups), and stored settings (for example, offline content).

![Image](https://cdn-media-1.freecodecamp.org/images/1*Jh90US1AS-UQWB4xIwAYWw.png)
_Mobile Websites reach more people (8.9M monthly unique visitors against 3.3M of Mobile Apps)_

On the other hand, in the same Comscore data, we learn that customers can be reached more easily from mobile websites, as they are not as much tied to their few apps of preference. If you compare the most popular websites versus the most downloaded apps, it's estimated that an average of 8.9 million unique web visitors per month access the top 1000 websites. That's almost three times more than the average unique users of the top 1000 most downloaded apps.

![Image](https://cdn-media-1.freecodecamp.org/images/1*hcjh-XXWh_j9x3iIy1BxvQ.png)
_Distribution (Web App) x Engagement (Mobile App)_

That's all about distribution vs engagement. Your web app has a higher chance of being accessed, as users are more likely to try new things when navigating through their mobile browsers. But Mobile Apps have been proven to be more engaging, and catch the users attention for much longer periods.

Now that you understand the dilemma, let's have a look at Progressive Web Apps. This is an approach so tied to the Web Apps tier that I classify it as just an addendum to Web Apps. But it's a big disruptor and a serious candidate for the most prominent new and cool thing in web and mobile development.

### Progressive Web Apps

Progressive Web Apps (PWAs) are a set of tools used to give Web App users the same experience they are accustomed to when they run Mobile Apps. This means that Web Apps can leverage the potentially higher levels of distribution with more decent levels of engagement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*raQWH9nuC6o8dY73a7dp3A.png)
_Progressive Web Apps addendum to Web Apps tier_

Google defined three main qualifications for PWAs: they must be [Reliable, Fast, and Engaging](https://developers.google.com/web/progressive-web-apps/#reliable).

Features called [Service Workers](https://developers.google.com/web/ilt/pwa/introduction-to-service-worker) and the [App Shell](https://developers.google.com/web/fundamentals/architecture/app-shell) are the foundation of Progressive Web Apps. They were created to promote apps’ reliability as they are now designed to work regardless of the device’s connection status. That includes offline mode, as well as poor connections. They also provide significant perceived performance boost, as apps launch using locally cached data, which eliminates delays for synchronous content downloads.

You could consider reliability an indirect vector of engagement. Users are not affected while commuting by train, for example. They can stay engaged.

The same applies to speed. According to Google:

> 53% of users will abandon a site if it takes longer than 3 seconds to load!

However, being exclusively reliable and fast on load doesn't necessarily guarantee high engagement. PWAs leverage mobile-related features that used to be exclusive to mobile apps, like an “Add to Home Screen” option and Push Notifications.

When it comes to to the “Add to Home Screen” feature, you might notice that Apple has had a similar feature since the very first iPhone. [Some people even argue that Progressive Web Apps are Google's fancy new name for an original Apple idea](https://youtu.be/EFGltzFSK-c?start=651).

And you really can’t completely disagree. Some ideas are actually cycling. They come, go away, and then come back with a new name and some enhancements (for instance, Service Workers), so they can finally stick around.

On the other hand, it’s hard to completely agree. Steve Jobs’ speech about Web 2.0 + AJAX and the memorable announcement of the iPhone back in WWDC 2007 are not convincing enough to call him as the father, or even the prophet, of PWAs.

To be fair, the Add to Home Screen capability on iPhone has been nothing more than a subtle, almost hidden, feature to generate desktop icons that just start up Web Apps in fullscreen mode. It has all the burden of HTTP request-response cycles and no clear path around caches.

PWAs start from the right point. They explore how previous installations of Web Apps aren’t necessary without losing the client-side bootstrap of Mobile Apps. This means that everything a user needs for their first interaction following startup might be locally cached (read: App Shell) and kept available as soon as they hit “Add to Home Screen.”

Moving onto another well-known characteristic of PWAs, let’s talk about the super engaging (or re-engaging) feature of the Mobile Apps world: Push Notifications. They are alert-style messages that appear on the top notification bar / area, as well as on lock screens. They have the power of pulling users back to your app once they receive the notification.

To reinforce the appeal of PWAs, Google has been pulling all modern Web APIs under the PWA umbrella. So expect to see things like Payment Requests, Credential Management, WebVR, Sensors, WebAssembly, and WebRTC in the context of Progressive Web Apps. But these feature are not necessarily tied to PWAs, and some were even born before the term PWA was coined.

#### PWA and Apple

Apple, on the other hand, announced their first solid milestones towards PWAs only in March 2018. [Although there are still some limitations, the progress is appreciable](https://medium.com/@firt/progressive-web-apps-on-ios-are-here-d00430dee3a7). Some of the limitations might be related to the fact that Safari has fallen behind its competitors. Others could be attributed to Apple's philosophy of tight control.

Still, [Apple has a more profitable App Store than Google](https://www.techrepublic.com/article/google-play-hits-record-19b-downloads-but-apples-app-store-still-makes-more-money/). Apple's asserts that more criteria on app publications brings more overall reliability, and PWAs are bound to hurt the App Store's revenue. This suggests that some limitations that seem to be intentionally imposed (like 50Mb of PWA maximum cache size) will cost more to be revoked.

#### Unfortunately PWAs are not perfect

Web solutions and, on different levels, all cross-platform solutions struggle to attain the excellence and comprehensiveness of Native Apps. Every new feature, and every detail particular to Android or iOS makes that native feel harder and harder to access as you distance your app from the native tier.

Overall, PWAs fix some issues in the Web Apps tier. But there are other issues that can’t be fixed by a solution working on top of a browser.

#### What PWAs fix

* More “native” experience
* Faster load times
* Do not require an internet connection
* Force web developers to be aware of situations where there’s no connection as well as a bad connection
* Incorporate features from Mobile Apps like Push Notifications, Geolocation, or Speech Recognition

#### What they don’t

* Inherent slowness
* Not available on app stores (just yet)
* Still not fully supported by all browsers
* Still lack mobile features like NFC, Ambient Light, Geofencing
* Also lack support for peculiarities of Android or iOS like PiP, smart app banners, launch screen widgets, and 3D touch

In the video below, I do a brief overview of PWAs.

### Hybrid Apps

At this level, we begin to dive into the Mobile App world. We’ll start from the most distant tier: Hybrid Apps.

The term Hybrid is also commonly applied to all cross-platform solutions. Here, however, I’m restricting it to Apps that work inside mobile components, called WebViews.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Hk7QdcVm2K8NpPd0FXrZBQ.png)
_The Hybrid Apps tier. Below the browser's line but on top of WebViews_

In the demos in the second video, my purpose for adding WebView as the Hello World example was to make clear that there's a native component for each platform that is able to perform like an actual browser.

#### Cordova/PhoneGap

Solutions like [Cordova](https://cordova.apache.org/)/[PhoneGap](https://phonegap.com/) close the gap (sorry for the uninspired pun) between Web and Mobile Apps. They provide tools to package developer's HTML, JavaScript, and CSS code (as well as any extra assets like images or videos) and transform them into Mobile Apps (yes, real Android or iOS apps). These apps have their WebView exclusively to interpret and run the original web code, starting with the “index.html” file in the app’s main folder (normally called “www”). They also bridge the JavaScript code to native APIs through plugins which are partially implemented in JavaScript and partially in a native language.

So, let's make things clearer. Hybrid Apps are able to access native APIs (instead of Web APIs), but they are enclosed by the WebView. A button with Cordova must be an HTML button rendered by a WebView instead of a mobile native button.

This is the magical tier that allows companies to port their Web Apps to Mobile Apps to be shipped by app stores. So any web framework is allowed here.

#### Ionic

Frameworks like [Ionic](https://www.ionicframework.com/) wrap Cordova into their own solutions. With Ionic, you don't need to use Cordova’s command line interface (CLI), because all of its commands are wrapped by the Ionic CLI.

Recently, the Ionic team decided to take the reins of the entire stack of Hybrid Apps. So they launched a proposed replacement for Cordova called [Capacitor](https://capacitor.ionicframework.com/). Capacitor has support for Cordova plugins, and can also be used by a non-Ionic project.

You can watch me going through a Cordova Hello World sample in the fifth video of the series:

#### Hybrid Apps advantages

* They are essentially web apps that are shippable to official app stores
* Can be used along with any JavaScript framework / library
* The code is still highly shareable across platforms
* Access to native features (for instance, camera, accelerometer, contact list)

#### Hybrid Apps disadvantages

* Struggle with performance issues and memory consumption, as web views are responsible for rendering everything on screen
* Have to mimic all native UI components on top of a single web view
* Harder to be accepted and published on App Store
* Usually take longer to have native features available for these environments

### Web Native

Web Native is a relatively new and often misunderstood tier. That's where Web Apps meet native components. Although Appcelerator (Axway) Titanium has been around a long time, there are some relatively new competitors that justify making this a completely separate category of mobile apps.

![Image](https://cdn-media-1.freecodecamp.org/images/1*MLfTZk4rl_3nFNW-OoXO4A.png)
_Web Native Apps don't need WebView as they talk directly to other native components_

As you can see above, there's no web view to render and run your application. So, how is your JavaScript executed? Is it compiled? Well, if you consider transpilation (compilation from one language to another — for example TypeScript to JavaScript), bundling, minification, mangling, and obfuscation all together as a compilation, yes JavaScript is compiled.

But the problem is, this doesn't make your JavaScript something directly understood by Android or iOS operational systems. And, in theory, there's no native component that only serves as a JavaScript engine without the bloat of the HTML layout engine.

The strategy is to ship JavaScript engines (normally [V8](https://developers.google.com/v8/) for Android and [JavaScriptCore](https://developer.apple.com/documentation/javascriptcore) for iOS) along with your code. Although they have small footprints and are very fast, they are something external that must be provided by your app.

On the other hand, this approach tends to have better UI performance, as all the components are the same (or are based on the same thing for React Native, for example) as the ones used by Native Apps.

#### Web Native Apps advantages

* Reach both platforms with one single codebase
* Roughly the same performance as native apps, as they also deal with native UI components
* Tweaks are necessary, but the code is still shareable with web development

#### Web Native Apps disadvantages

* Even with one single codebase, the developer must be aware of native components
* Steeper learning curve than Hybrid / Web Apps for web developers, especially when it comes to layout

#### React Native

In part 6 of the series, I do a quick Hello World in React Native. This shows, on Android Studio's Layout Inspector, what components were rendered in the emulator. I compare with the previous examples, ensuring that there's no WebView whatsoever.

#### Nativescript

Another amazing framework that I've been particularly interested in over the last two years ([I have a course on Udemy about it](https://www.udemy.com/angular-native) — in Portuguese), is [Nativescript](https://www.nativescript.org/). It’s similar to React Native but is not tied to the React world ([there's an unofficial integration, Nativescript-Preact, though](https://github.com/staydecent/nativescript-preact)).

With Nativescript, you can develop using vanilla JavaScript, TypeScript, Angular and, more recently, Vue. Of course you can use other frameworks, but those are the ones officially supported. It’s fairly well documented too, by the way.

Nativescript has tools like [Nativescript Sidekick](https://www.nativescript.org/nativescript-sidekick) and [Nativescript Playground](https://play.nativescript.org/), as well as project structures based on [templates](https://market.nativescript.org/?tab=templates) that can be provided by the community. This should help you in project creation, giving you the ability to start, deploy, test, and run on simulators on the cloud and iPhone devices even when you are not developing using a Mac.

In the seventh part of the series, I do a Hello World using Sidekick along with another project started from the CLI and a [WhatsApp clone template](https://github.com/Especializa/nativescript-whatsapp-template) I created for learning purposes.

It's important to have a look at the Layout Inspector when your app is running on an Android emulator. With Nativescript, it shows the native components (again, no WebView), and direct instances of common Android classes like TextView. This is different than React Native, which has its own classes to wrap the native components.

That's probably why Nativescript claims that there’s no delay between when a new feature is available on iOS and Android and when you can use it in a Nativescript project. For example, [they posted on their blog](https://www.nativescript.org/blog/preview-of-augmented-reality-in-nativescript) an AR project on the same day iOS 11 was officially released with the new ARKit API.

#### Weex

Another framework worth mentioning in this category is [Weex](https://weex.apache.org/). It's a project developed by Alibaba, and is currently incubated at Apache Sofware Foundation (ASF). It uses common HTML tags like `<d`iv> and CSS commands i`nside &`lt;style> tags to call native components instead. From their documentation:

> Although components in Weex look like HTML tags, you are not able to use all of them. Instead, you can only use the built-in components and your custom components.

### Cross Compiled

At this level, it’s time to jump off the Web bandwagon. This is the closest tier to native development, but has the advantage of using one single codebase to target Android and iOS.

![Image](https://cdn-media-1.freecodecamp.org/images/1*dNq3N6jsMK3lKII2xD4bWw.png)
_Development tiers now complete with Cross Compiled Apps_

#### RubyMotion and Xamarin

There are solutions like [RubyMotion](http://www.rubymotion.com/). This is a way to write mobile apps using Ruby and compile directly to the targeted platform (as it was created using any "native" language).

Another option is [Xamarin](https://www.xamarin.com/), where you write in C#, compile to an intermediate bytecode, and deploy your app along with an instance of the [Mono](https://www.mono-project.com/) common language runtime. This approach has the same drawback as Web Native (where V8 and JavaScriptCore are delivered by your app), but can also rely upon JIT compilations to optimize the app at runtime.

#### Flutter

Last but not least, I'd like to bring up [Flutter](https://flutter.io/). It’s Google's newest cool initiative for mobile development. It fits in the Cross Compiled tier because you write apps using the [Dart language](https://www.dartlang.org/) and compile them down to the native platform.

Flutter has innovated in some aspects. Probably the most outstanding one is the fact that it provides its own set of components.

**What? Own set of components?**

Yes, Flutter provides a number of different components so you can completely skip the ones from the platform. It has generic components as well as [Material Design](https://flutter.io/widgets/material/) components for Android, and [Cupertino](https://flutter.io/widgets/cupertino/) components for iOS.

Rather than .Net virtual machine (as Xamarin) or JavaScript engines (as Web Native frameworks), with Flutter your app will deliver the components you decide to use.

**Are they native components?**

Yes, they are. Your app is native, too. Everything is compiled to the native architecture. However, bear in mind they are not the pre-existing native components.

**What's the point of that?**

Well, in my opinion, this solution is clever and audacious. I've been waiting to talk about advantages and disadvantages, but as it's just one particular technology, let me address them now.

One of the biggest challenges for Web Native and Cross Compiled solutions (remember, above Native but below the WebView in our tiers) is how to deal with native components. For example, an important problem is how to lay them out. That's because they were not created to be used by those external resources. Also, they were not created with a counterpart in the other platform in mind. The Android NavBar doesn't work like iOS UINavBar, for example.

With Flutter, components are created with cross-platform always in mind. So let's have a look at the pros and cons of the Cross Compiled Apps tier:

#### Cross Compiled Apps advantages

* Reach both platforms with one single language
* Roughly the same performance as native apps, as they also deal with native UI components

#### Cross Compiled Apps disadvantages

* Slightly delayed support for the latest platform updates
* Code not shareable with web development
* Even with one single codebase, the developer must be aware of native components

PS: With Flutter, you’ll provide your own set of widgets along with your app's code

### Mobile Apps runtime architecture

![Image](https://cdn-media-1.freecodecamp.org/images/1*BI2on3Tup2LSs5MjToEcWw.png)
_Four different Mobile Apps runtime architectures._

As you can see, Cross Compiled solutions can be spread across three of the four different quadrants. In the top-left, you find Native and Cross Compiled (for example RubyMotion), where your app (in green) is compiled to native binaries. It talks directly to OEM Widgets (Original Equipment Manufacturer widgets — what we've been calling native components) as well as the native API.

The top-right quadrant is exclusive to Hybrid Apps. Your app is necessarily HTML/CSS/JavaScript executed by the native WebView (as we did in the fifth video of the series). Cordova/PhoneGap or Capacitor can provide a bridge to allow your JavaScript code to talk to native APIs.

The bottom-left quadrant is where all Web Native solutions, as well as Xamarin, fit in. Your app is not compiled to native code (but rather to a binary stream in Xamarin) and it wraps an interpreter to act as a bridge to everything in the platform.

Finally, at the bottom-right, I could have said Cross Compiled, but it seems very particular to Flutter. It’s different than other Cross Compiled strategies that seem more traditional. In this case, there's no bridge, but there's also no contact to OEM Widgets (at least no need for that).

Notice that Web Apps (even including PWAs) are not in the graph, because they don't touch the native environment at all.

In Part 8 of the series, I discuss Cross Compiled Apps and focus on Flutter with a Hello World project.

### Wrapping up

To sum up, I hope it's clear to you that there's no big winner here. It's not easy to spot the idiosyncrasies and points in common for a general classification. My intention was not to present the market share of each strategy or try to find the most productive, pleasant, or reliable way to build mobile apps.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Yx4X3FwFbhYi51M0TCWtEw.png)
_All Mobile Development Tiers with their main characteristics._

My intention was to present an overview of the players, and the approaches they take, so you can choose what best suits your needs.

#### A few tips to help you find your way

Please allow me being a bit more opinionated at this point and bring up some questions and answers that hopefully pave your way.

Before we go ahead, guess what? Exactly! I put together another video covering what I'm about to say:

#### **1. Does my app need intensive CPU processes?**

If the answer is **yes**: Native Apps.  
Remember: the lower you get, the more performant your app tends to be.

Apps that need intensive computation power, for instance Machine Learning (even just running pre-trained models), are good candidates for the Native tier (or, at least, Cross Compiled).

If you are thinking about games, you might have heard about the Unreal and Unity game engines. They are the way to go for many gaming companies, and I feel like they kind of fit in the Cross Compiled layer. I decided to leave them off this list just because I'm starting to be concerned about the length of this post. :)

#### **2. Is my team BIG enough to maintain two codebases?**

If the answer is **no**: Everything but Native Apps.  
Remember: the higher you get, the more abstract and platform-independent you are.

That's the biggest thing that pulls people back when considering Native Apps. Generally speaking, two codebases make things costly and hard to evolve. In theory, you don't want to have an app with significantly more features on Android than iOS, or vice-versa.

If both items 1 and 2 are relevant to your app, your must nominate which one is crucial. Or, again, consider a middle ground with the Cross Compiled approach.

#### **3. What does my team do best?**

If the answer is **C#**: Xamarin.  
If the answer is **Java**: Native (Android).  
If the answer is **Web/Javascript**: From Web to Web Native.

It seems obvious but, believe me, I've seen cases where people take it for granted. Except when Apple came up with Objective-C, thus throwing away Steve Job's bet on a PWA-like approach for apps on iPhone, all solutions are built with developers' previous abilities in mind.

#### **4. Where do my users come from?**

If the answer is **Unknown** (or any other than app stores): Progressive Web Apps.  
Remember: Having to install apps from App Stores is causes extra friction.

We discussed the Web distribution power over mobile apps in general (every tier below the browser).

#### Mix of approaches

Web technologies allow you to have a mixed codebase, and target not only mobile platforms but also desktops. I know solutions like [Electron](https://electronjs.org/) make it easy to deploy your app to Windows, Mac, or Linux computers. But I’m talking about making a Web App (or even better a PWA) share code with a Mobile App.

OK, you might think Cordova does it pretty decently. Well, I agree. Hybrid Apps are Web apps run by a WebView, but I'm still trying to convince you to think out of the box. What if you want a Web App, with HTML templates, that shares code with a Web Native App?

Depending on what architectural pattern you use to structure your app, things can be facilitated by reusing the business logic and a lot of boilerplate code, like routing and state management. You just need to define two sets of templates, one for web, another for mobile.

There are some project seeds to help you to start. For example, with [Angular-Native-Seed](https://github.com/TeamMaestro/angular-native-seed) you start an Angular project that’s ready to deploy on mobile devices. It can be as simple as creating a template file with different extensions:

```
Extension                      | Platform------------------------------ | --------------------------.{html/scss}                   | Recommended for Web.tns.{html/scss}               | Only for mobile.tns.ios.{html/scss}           | Only for iOS.tns.android.{html/scss}       | Only for Android.tns.ios.phone.{html/scss}     | Only for iOS Phone .tns.android.phone.{html/scss} | Only for Android Phone
```

Just decorate your Angular component with a `templateUrl` and the right template file will be picked up according to which platform is running.

In the snippet above, `my-component.android.html` would be automatically picked up when running on Android.

Sometimes things are not dead simple. There's a chance that you might have a completely separate component just for one particular platform. But having this managed by your app in a single codebase shouldn't be a big deal.

Have a look [here](http://jkaufman.io/react-web-native-codesharing/) and see how to achieve something similar with React (Web) and React Native.

That leads to another question. When should you go Hybrid and when should you go Web Native?

My 10 cents on that is this: if performance and native user experience are what you aim for, simply go Web Native. On the other hand, if keeping the layout consistent across all targets is the big deal, and managing two or more sets of templates and stylesheets sounds overwhelming, just go Hybrid.

As you can see, when it comes to mobile development, any of those approaches might work for you. As long as the vendors or maintainers support their products, there’s a good reason to try each one mentioned in this study.

I hope this has been helpful and that you have enjoyed this journey through many different mobile development solutions and strategies.

### What's next?

You might have noticed that I didn't add the last video of the series. Ok, there we go:

This one is all about helping you decide **what is the best mobile technology to learn in 2018.** If you’re asking what’s the best technology to pick up for your next project, then I’d say **it depends.** I don’t just want to say **"Whatever. Just pick and choose. Wish you all the best"**. I'd like to provide you with a path for a more efficient learning process, so you can master more than one technology quickly. So check out that last video.

There's a convergence happening across mobile platforms and languages are getting more and more similar. Watch this last video, even if you don't code. I present many features from Kotlin, Swift, and TypeScript. In the end, I just want you to realize that they are not that different. Trust me. Have a look at the video and let me know in the comments section. I really look forward to hearing your thoughts on that.

Thank you for reading!

