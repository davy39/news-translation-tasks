---
title: Why Progressive Web Apps Are The Future Of Web Development
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-05T18:20:16.000Z'
originalURL: https://freecodecamp.org/news/why-progressive-web-apps-are-the-future-of-web-development-13db7dd5f640
coverImage: https://cdn-media-1.freecodecamp.org/images/1*oc4pOoEeR_QMrCA6LkF5Kw.jpeg
tags:
- name: Apps
  slug: apps-tag
- name: development
  slug: development
- name: PWA
  slug: pwa
- name: web
  slug: web
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Tushar Agrawal


  “The key is to embrace disruption and change early. Don’t react to it decades later.
  You can’t fight innovation.” — Ryan Kavanaugh


  Lately, there’s been a lot of buzz around PWAs with many claiming it to be future
  of web developmen...'
---

By Tushar Agrawal

> “The key is to embrace disruption and change early. Don’t react to it decades later. You can’t fight innovation.” — Ryan Kavanaugh

Lately, there’s been a lot of buzz around PWAs with many claiming it to be future of web development, especially in terms of mobile devices. At its core, a Progressive Web App (PWA) is simply a web application that uses modern web techniques to deliver a native app-like experience to users. These are web applications with progressive enhancement to implement features like caching, background sync, and push notifications.

Even though [PWAs](https://developers.google.com/web/progressive-web-apps/) have been around for more than two years now, the response is quite underwhelming. Few big players have adopted this philosophy but most haven’t actually embraced it very much. Chrome and Mozilla are perhaps the best browsers to test out your PWAs as Apple is yet to get into this stuff.

### PWA — Is it really good ?

On one hand, we have native apps that are undoubtedly fast and efficient in most of the cases. On the other hand, there are websites that are kinda slow and with the connectivity issues, it only gets worse.

Accelerated Mobile Pages Project ([AMP](https://www.ampproject.org/)) spearheaded by Twitter and Google was launched in 2016 to solve those slow connection issues only. PWAs work flawlessly in all the possible scenarios. With a good connection, there is never a problem. The problem is when we have no connection and we are greeted with the error page.

![Image](https://cdn-media-1.freecodecamp.org/images/1*0DOKUYA7bHE9COGpJw5q0Q.png)

But this can become most annoying if we have a slow connection. The page seems to be loading and all we see is a blank screen. We just wait, wait and wait but the page never seems to load. This is where PWA comes to our rescue. The best part about PWAs — you get the best user experience possible in slow connectivity as well as no connectivity (yep , you read it right..).

### Why it makes sense to use PWA

According to a study, an average user spends 80% of his total time on apps on only three of his apps (For me its Chrome, Quora and Medium).

The other apps just sit idle for most of this time consuming a precious portion of the memory. Moreover, it costs around ten times to develop an app rather than creating a website for the same. The cost can get much higher if you plan to develop and maintain separate code bases for different platforms like Android, iOS and the web.

### Native App features that PWAs can use

* Push notifications
* Full Screen
* Offline working
* Splash screen is supported giving it a more app like feel

PWAs can make use of many more such features. The above points are only to give you a hint of what PWAs are capable of. However, there are some traditional features that only native apps enjoy as of now.

### Native App features that PWAs can’t use as of now

* No or highly restrictive access to different hardware sensors
* Alarms
* Phonebook Access
* Modfiying System Settings

PWAs are evolving quite fast and we can hope to see these features come to action pretty soon.

### Two Major Components of a PWA

**App Manifest**  
It’s a JSON file that defines an app icon, how to launch the app (standalone, full-screen, in the browser etc), and any such related information. It’s located in the root of your app. A link to this file is required on each page that has to be rendered.

It is added in the head section of the HTML page:  
`<link rel=”manifest" href="/manifest.jso`n">

**Service Worker**  
Service worker is where most of the magic of happens. Its nothing but JavaScript code that acts as programmable proxies solely responsible for intercepting and responding to network requests. Since it acts as a proxy and can be easily programmable, the application must be served over HTTPS to keep the data secure.

Its worth noting that the service worker caches the actual response, including all HTTP headers, rather than just the response data. This means that your application can simply make network requests and process the response without any specific code to handle the cache.

### How do I get started?

The best thing about getting started is that it’s quite easier than it seems. In fact, it’s very much possible to take an existing site and convert into a PWA. I highly suggest you watch this if you intend to develop a PWA.

#### Thanks for reading! If you liked it, please support by clapping and sharing the post.

