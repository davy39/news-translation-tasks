---
title: How to Implement a PWA and Barba.js into internet kiosks
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-09T18:12:52.000Z'
originalURL: https://freecodecamp.org/news/how-to-implement-a-pwa-and-barba-js-into-internet-kiosks-854d4895fd04
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7QocFarKH2FtHu64nQA-JA.jpeg
tags:
- name: Android
  slug: android
- name: JavaScript
  slug: javascript
- name: PWA
  slug: pwa
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Nino Mihovilić

  The project we’ll describe here is an interactive internet kiosk that’s used as
  an extension for the LikeUs mobile application. LikeUs is a mobile app that makes
  it easy for users to choose a place to go out, have coffee or listen t...'
---

By Nino Mihovilić

The project we’ll describe here is an interactive internet kiosk that’s used as an extension for the [LikeUs mobile application](https://likeus.hr/). LikeUs is a mobile app that makes it easy for users to choose a place to go out, have coffee or listen to a concert. Because Zagreb’s Tkalčićeva street is a place where quite a lot of young people hang out, we decided it was the right place for our offline promotion of the LikeUs app.

#### Implementing the Kiosk Mode

One of the first challenges we faced was the implementation of the kiosk browser mode on our device. It was an Android Box and we used Chrome as a web browser that will run the app. Kiosk browser mode is a mode in which you run the application in fullscreen and without any browser user interface or, in our case, without any Android user interface.

The intent is to prevent users from running anything other than the browser-based content. As there are hundreds of kiosk mode apps, we decided to use one of the available applications instead of building one from the ground up.

After some research, we decided to use the [Kiosk Browser Lockdown](https://www.android-kiosk.com/) app. It has all of the features we were looking for:

* Locking the device to a single URL
* Hiding toolbar options
* Hiding the notifications screen
* Hiding the Android user interface

The next step was to test the PWA in the Android environment and in the Kiosk Browser app. That’s when we discovered that things wouldn’t go as smooth as we planned!

The first problem we encountered was on the frontend side — the final website seemed like an upscaled version of the initial design, and this was due to some screen limitations and a different rendering environment. As the deadline was approaching, we didn’t have enough time to tweak every single item in CSS to fit the initial design outlines, so we decided to downscale the entire document.

It was a reasonable approach considering all the inputs we had. Having to test everything once more was a big downside, but we had to be sure that everything will work in this context.

The second problem was that external scripts like Google Maps weren’t loading in the Kiosk Browser app with the PWA, so we did a little tweak. We started the Kiosk Browser app, which removed the Android user interface, and then exited the Kiosk Browser app and started the PWA outside of the Kiosk Browser app. This way we managed to remove the Android interface with all external scripts loading as they were supposed to.

![Image](https://cdn-media-1.freecodecamp.org/images/HpUfeFTjyE05czMLe-X7GgCVO0uacIPiAjrE)

#### Developing a Progressive Web App

After going through the project brief and specifications, the first thing that came to our mind was… we should do a PWA (Progressive Web App). A Progressive Web App is an application that provides similar capabilities and functionalities as native mobile apps:

* Service workers allow apps to show content nearly instantly and reliably because they cache every request
* There is an ability to add the app to the home screen like a normal native app
* Push notifications can be implemented for multipurpose usages
* The app is fast and smooth
* It uses HTTPS and is easy to implement.

After evaluating client’s requests, all features of the PWA were meeting our requests.

Our requests were:

* To build an app that could be used on an interactive screen
* The app should use an existing API we built for our LikeUs mobile app
* The device used will be an Android Box
* Internet access would be restricted because the app would be connected to a public network (this would change later)
* The app should have an additional section for banners and a banner management system

We could build a web app with our existing API without having to implement additional functionalities, and we could also build a simple CMS (content management system) for banner management and push notifications for content reloading. As internet access would be restricted and unstable, we could use the PWA feature to cache pages and serve them even when the app is offline.

Be sure to check out this [in-depth tutorial](https://medium.com/@jewbre/service-workers-6a5c13c9a123) and explanation for Service Workers.

#### Tweaking the Banner Management System

The app is divided into two sections. The top section is the banner section, and the bottom part is the main section divided into tabs.

We have two types of banners — Youtube videos and images. Since banners can be changed, we needed to develop a CMS. We developed a simple CMS in which the client can enter Youtube videos and images into a slider.

The problem we encountered here was refreshing the app to reload new banner content. You see, because the app was using Barba.js, it was never refreshing. To make it work, we used a cool feature of our PWA — push notifications. Push notifications are a feature that uses the Notifications API and the Push API to send messages from the server to the client.

How did push notifications help solve our content reloading problem? The solution is pretty simple and straightforward. When the user changes banner content in the CMS, we send a push to the PWA and then the PWA refreshes two times. The PWA needs to be refreshed two times to delete the cache and to reload new content.

#### Dealing with External Obstacles

Internet kiosks are often placed in outdoor environments where internet connection is sometimes unstable and slow. When the internet connection is public and in a pretty crowded street, you face a lot of problems when using real-time communication and external APIs.

A common “hacky” approach is to extend the delay time and hope that everything works well. Even though this is not the preferred way, it can serve as a backup if everything else fails.

Google Maps was one of the external APIs that gave us a lot of headaches. We had to reload and add new pins, but on a slow connection, this was sometimes impossible.

![Image](https://cdn-media-1.freecodecamp.org/images/hyvg705AuzUl8rybWXHDDk9stgbs7vsnTmec)

#### Balancing Between Fixed and Dynamic Content

Optimization is not only applied in the realm of advanced caching techniques and content delivery networks. Smart layout placement and understanding elements that can be “pushed out” of the page reloading flow can reduce the number of requests and speed up the entire navigation flow.

The advertising content in the kiosk was hosted on Youtube — it was a video slider that was repeating through all pages. Below that, we had the main content with inline navigation. When selecting different navigation items, the default browser behaviour was to reload the entire page, including that fixed advertising area. It’s a performance nightmare, especially when having external scripts such as Youtube API.

The question here is — how to reload only one specific part of the page? Well, there will be no browser reloading and the only thing that can be done is changing content in the background without leaving the page.

Because of the implemented analytics, we had to update the URL accordingly. We did this by using the PJAX (Push State Ajax) technology. This technology allows content prefetching and swapping target DOM nodes in the background.

To avoid content flashing, create a simple fade transition that fires when content changes. As it’s time-consuming to manually manage all states of content swapping, we used an external library called Barba.js. This library allows advanced transition management and is compatible with all animation frameworks.

![Image](https://cdn-media-1.freecodecamp.org/images/yzC0x5NH-VvltNXi-nOOXA871NO2gcJnlcQy)

Barba.js has internal state caching that can be used to leverage browser caching and optimize loading time. Barba cache is a global Javascript object where every value is a Promise that has to be resolved.

#### Implementing Analytics and Virtual Pageviews

We wanted to measure user interaction and page views. Because we are using Barba.js, this is basically a one-page app without page reloads, so the trick to measure page views in this type of app is to use Virtual Pageviews. They are page hits sent to Google Analytics, without actually reloading the page.

The first step is to include the [Google Tag manager](https://developers.google.com/tag-manager/quickstart) code, and then to actually send Virtual Pageviews to the data layer. We can do it with the next snippet:

```
dataLayer.push({ 'event': 'VirtualPageview', 'virtualPageURL': currentUrl, 'virtualPageTitle': title });
```

This snippet needs to be called on each new page. On each user interaction that opens a new “page”, we call this snippet that sends the page URL and the page title to Google Analytics. This way we can track pageviews in single page apps that use Barba.js or any other PJAX technology.

![Image](https://cdn-media-1.freecodecamp.org/images/pkJtXRjiySB4CfjP6v8gC1ujMJZFTSGe2qjI)

#### To Conclude

When working in a specific environment, sometimes the “by the book” solution is not your only solution. There is usually an opportunity to innovate and use some common tools and libraries in a not so standard environment with a specific set of challenges.

_Originally published at [www.bornfight.com](https://www.bornfight.com/blog/how-to-implement-pwa-and-barba-js-into-internet-kiosks/)._

