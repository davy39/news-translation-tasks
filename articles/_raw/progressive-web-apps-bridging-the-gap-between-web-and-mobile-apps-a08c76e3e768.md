---
title: 'Progressive Web Apps: Bridging the gap between web and mobile apps'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-26T11:16:26.000Z'
originalURL: https://freecodecamp.org/news/progressive-web-apps-bridging-the-gap-between-web-and-mobile-apps-a08c76e3e768
coverImage: https://cdn-media-1.freecodecamp.org/images/1*G8GpxgnXeOoagIk5huIbUw.png
tags:
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Ajay NS

  Unless you’ve been living under a rock, you’ve probably heard of PWAs or Progressive
  Web Apps. It’s a hot topic right now because its support is increasing in multiple
  platforms, and major companies are deciding to work on PWA versions of ...'
---

By Ajay NS

Unless you’ve been living under a rock, you’ve probably heard of PWAs or Progressive Web Apps. It’s a hot topic right now because its support is increasing in multiple platforms, and major companies are deciding to work on PWA versions of their web apps including Twitter, Lyft, Starbucks, NASA, and more.

Recently it gained more attention, when Apple announced Service Worker and Web Manifest support for Safari. Microsoft brought PWAs to the Windows store, and Chrome has experimental PWA support for all the platforms.

Okay that should be enough to convince you that they’re worth going through.

So this article is a summary of the concepts and approaches that Progressive Web Apps follow. I’ve written this from my experience building them, and I outlined this article after going through the [Google Progressive Web Apps Training](https://developers.google.com/web/ilt/pwa/).

The training does a good job of explaining how everything works together, and also takes you straight into the code. Udacity’s [Mobile Web Specialist course](https://goo.gl/nvzoPG) also could be of help here.

### Why PWA?

![Image](https://cdn-media-1.freecodecamp.org/images/dC96dvAcZ241P7xcT3R0P1vt-4GXq-JWBJdu)
_Time spent by average users on Web vs Apps_

The web is Operating System independent, is widely reachable, and is the biggest platform on the internet. Yet we see that users spend a lot more time on native apps than on the web.

Why is this so?

The main reason is the smooth experience and engagement native apps provide. How about we bring these features to Web Apps? That would mean the combination of the ease of access and reach of the Web (3x as compared to native apps), along with the immersive experience of native apps.

According to Alex Russell, who coined the term, PWAs are:

> Just websites that took all the right vitamins

These vitamins are just features of native apps that we add on to Web Apps to get the best of both worlds. Apps that you can access directly from the Web, yet work smoothly and faster, are installable, and may even have notifications.

![Image](https://cdn-media-1.freecodecamp.org/images/aEKAnAk-nfEiXs-SRPOL05qVmDEh9U8LacSF)
_Comparing web, native and progressive web apps, from Google’s PWA training_

### What makes PWAs what they are

The key features according to [Google](https://developers.google.com/web/progressive-web-apps/):

1. **Reliable:** Offline-first, meaning it should provide interfaces even in poor or no internet connection. But this also doesn’t mean that the app should just be able to work when offline, but rather provides undisrupted service in all network conditions.
2. **Fast:** Instant-loading, and smooth experiences even on loading content.
3. **Engaging:** Should provide an immersive experience, equivalent to that of a native app. Can have Push notifications, Web Payments, or Credential management and so on. Being installable is also a key feature here.

But these are just concepts — how do we think about implementation from a technical point of view? Samsung Internet’s [Peter O’Shaughnessy](https://medium.com/@poshaughnessy?source=post_header_lockup) has a good approach for this:

![Image](https://cdn-media-1.freecodecamp.org/images/ZcYyAHiWU1fGXX5oPhYOk-fRFNa6frEkS8Jr)
_PWA Standards_

So let’s get into these one by one:

### Service Worker

It’s a JavaScript file that runs separately from the main browser thread in the background, intercepting network requests, caching resources, and providing a base for multiple APIs including push notifications, background sync, and caching.

![Image](https://cdn-media-1.freecodecamp.org/images/mDv4XvnYgfsotIUSEOP7-iIwAsQwBWrQgs76)
_Flow diagram for Service Workers intercepting network requests_

The ability of service workers to run separately in the background helps give a lot of functionality to the app even when closed, providing a more native app-like and engaging experience.

It also helps in making the app offline-first as it acts a proxy between the server and application.

An introduction to service workers can be found [here](https://developers.google.com/web/fundamentals/primers/service-workers/), and Google has a few helpers open sourced in their [Service Worker Toolbox](https://github.com/GoogleChromeLabs/sw-toolbox).

### HTTPS

Hypertext Transfer Protocol Secure is an adaptation for secure HTTP communications using SSL or TLS encryption. But let’s not get into that — rather, we’ll go into the reason why it’s important.

Other than the fact that PWAs are expected to be highly secure, service workers that they use can intercept network requests and modify responses. This can be exploited easily to cause serious attacks. There are many services which help you get your site an SSL certificate like [LetsEncrypt](https://letsencrypt.org/) and [SSLforfree](https://www.sslforfree.com/).

### Web App Manifest

Basically, a JSON file that gives information about how the app should look in the home screen, on the web, and so on. It can be used to add a theme color, icons for the home screen, and a splash screen to name a few.

![Image](https://cdn-media-1.freecodecamp.org/images/A5vD1Vw7DTXejsWsc124V8uWz8CqgHNfPEqs)

A simple manifest would look like this:

```
{  "name": "HackerWeb",  "short_name": "HackerWeb",  "start_url": ".",  "display": "standalone",  "background_color": "#fff",  "description": "A simply readable Hacker News app.",  "icons": [{    "src": "images/touch/homescreen48.png",    "sizes": "48x48",    "type": "image/png"  }, {    "src": "images/touch/homescreen72.png",    "sizes": "72x72",    "type": "image/png"  }, {    "src": "images/touch/homescreen96.png",    "sizes": "96x96",    "type": "image/png"  }, {    "src": "images/touch/homescreen192.png",    "sizes": "192x192",    "type": "image/png"  }],  "related_applications": [{    "platform": "play",    "url": "https://play.google.com/store/apps/details?id=cheeaun.hackerweb"  }]}
```

It makes the app look more native-friendly with all the icons, themes, and splash screens. It’s installable with just a JSON file.

Read more about them in Mozilla’s [Web Docs](https://developer.mozilla.org/en-US/docs/Web/Manifest) and generate one [here](https://tomitm.github.io/appmanifest/).

For favicons of different sizes, you can generate them from a single high quality image by using [Favicon-Generator](https://www.favicon-generator.org/) and the theme. Background colors can be picked from the app’s palette.

### Push Notifications and Background Sync

The server delivers push messages to the service workers, which intercept and update the local state or display a notification to the user. Since they run independently as a background process, this is possible even with the app closed. [Push API](https://developer.mozilla.org/en-US/docs/Web/API/Push_API) could help you implement this functionality.

![Image](https://cdn-media-1.freecodecamp.org/images/ncx23EVESHpPFgbcxpXKQqGAJXrb1RqQntSb)

[Background Sync API](https://www.chromestatus.com/feature/6170807885627392) pushes periodic updates to the server so that the app can update when it’s online. Basically it makes sure all the messages are sent when there’s a good connection.

### Additional Concepts

Below are few approaches and standards to follow while working on building Progressive Web Apps.

#### Lighthouse and PWA Checklist

![Image](https://cdn-media-1.freecodecamp.org/images/fzop4QpaTHgwxutmtCZx7ko-JPk-KAb5goj2)
_Lighthouse audit taken for AliExpress PWA_

[Lighthouse](https://developers.google.com/web/tools/lighthouse/) is an automated tool for checking the quality of web pages by taking audits in performance, best practices, accessibility, SEO, and progressive web app standards. This is a good way to check if your app meets the standards and to see how good of a PWA it is.

You can figure out what your web app lacks and how it can be improved by using the suggestions from Lighthouse audits and also this [PWA Checklist](https://developers.google.com/web/progressive-web-apps/checklist) by Google which lays down all the general guidelines to follow, and how to fix issues. And the best part is, right now, Lighthouse comes built into Chrome DevTools!

#### Storage

According to Addy Osmani (on the Google Chrome team), the best practice for storage to be followed in PWAs is:

> Use the [**Cache API**](https://davidwalsh.name/cache) for **URL addressable resources** (part of [Service Worker](https://developers.google.com/web/fundamentals/primers/service-worker/)). For all other data, use **IndexedDB** (with a [Promises](http://www.html5rocks.com/en/tutorials/es6/promises/) wrapper).

Both of these are asynchronous APIs which work with web/service workers. This makes them suitable for use with PWAs, unlike other methods such as localStorage.

For a quick idea of what IndexedDB is, you can refer to [this](https://developers.google.com/web/ilt/pwa/working-with-indexeddb) resource.

Put simply, it’s a large scale noSQL storage system which can store about anything from the browser. It also works as a high-performance API.

#### Caching

The Cache API which can be used in the Service Worker allows you store responses keyed by request. This allows content to be directly loaded from Cache in the event of a poor network and it can also be further configured to load only the necessary data while relying on the cache for everything else.

![Image](https://cdn-media-1.freecodecamp.org/images/RVLZ0I1tzR95WCKrzfjZdM1eQpSJ4XJkn27M)
_Example for app shell in Flipkart Lite PWA_

One of the popular patterns for approaches for offline-first and native-app-like experience is caching the application shell. This includes all the basic HTML, CSS, and JavaScript that make up the navigation/toolbars or whatever is common throughout the layout. So the app shell loads instantly and shows a loading screen as content is fetched, giving a streamlined experience.

#### Fetch and Promises

For fetching resources, the latest and recommended way is to use the Fetch API with Promises.

```
// A basic fetch example with promisesfetch(‘examples/example.json’).then(function(response) {   // Do stuff with the response}).catch(function(error) {   console.log(‘Looks like there was a problem: \n’, error);});
```

XMLHttpRequest (XHR) requests are unnecessarily verbose and so are callbacks, which fragments code and causes confusion when long callback chains are used.

Promises are a better way of handling asynchronous code.

Service Workers, Cache API, and Network requests extensively use these for performing a variety of tasks and are required at base level, hence it’s very important have a proper idea about these.

#### Responsive Design

This not only means using responsive units of width. Content blocks should be manipulated for the needs of the layout. The app needs to look perfectly made for mobile, and overall it should look like a well-designed native app.

![Image](https://cdn-media-1.freecodecamp.org/images/bluXA0ACI9qf0KuVi8fqjs77avSYwsEZ89ZZ)
_Steps for Manipulating content_

Modern CSS layout systems such as [CSS Grid](https://css-tricks.com/snippets/css/complete-guide-grid/) (Learn with this [free course](https://cssgrid.io/) by Wes Bos) or [Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/) can be of great help for managing different layouts and arrangements of different screen sizes.

#### Image Optimization

![Image](https://cdn-media-1.freecodecamp.org/images/rxc-8mnQTfIeBdLHQ2oS3Iw0ZgZg1iU173Mi)
_Data distribution in web apps_

One of the key features of PWAs is that they should be blazing fast, and you can see that images aren’t helping. They need to be replaced with SVGs or removed wherever possible. Web optimized formats should only be used with the lowest size possible.

But it’s also important that these images be fluid and still go well with different screen sizes, as another import feature of PWAs is their native app-like experience.

### Stories and Examples

![Image](https://cdn-media-1.freecodecamp.org/images/CLx2fiuhFfqkS4pK3FeOS9IR7chAlZqgaC3E)
_A few real-world examples of PWAs_

### Conclusion

With every service launching an app, people often find it inconvenient to actually go to the store and download it. They hate spending that much time, mobile data, and space on the device. This often leads them to the web, which requires way less effort. But then, we see high bounce rates, because the web experience is not as smooth and optimal as the native app.

The solution for both of these problems is Progressive Web Apps, which combine the best of the two worlds, giving the optimal user experience.

As mentioned, with the support for PWAs increasing greatly in all platforms, now would be the best time to get started.

[BookMyShow’s Progressive Web App drives an 80% increase in conversions](https://developers.google.com/web/showcase/2017/bookmyshow)

[Building Flipkart Lite: A Progressive Web App](https://medium.com/progressive-web-apps/building-flipkart-lite-a-progressive-web-app-2c211e641883)

[Great examples of progressive web apps in one room](https://www.progressivewebapproom.com/index.html)

### Further Reading

[**6 myths of Progressive Web Apps**](https://medium.com/samsung-internet-dev/6-myths-of-progressive-web-apps-81e28ca9d2b1)  
[_Terms like “Progressive Web Apps” (PWAs) are useful to help spread concepts, but they come with a risk of misuse and…_medium.com](https://medium.com/samsung-internet-dev/6-myths-of-progressive-web-apps-81e28ca9d2b1)[**A Tinder Progressive Web App Performance Case Study**](https://medium.com/@addyosmani/a-tinder-progressive-web-app-performance-case-study-78919d98ece0)  
[_Tinder recently swiped right on the web. Their new responsive Progressive Web App — Tinder Online — is available to…_medium.com](https://medium.com/@addyosmani/a-tinder-progressive-web-app-performance-case-study-78919d98ece0)

Converting React apps to PWAs:

[**React Progressive Web Apps — Part 1**](https://medium.com/progressive-web-apps/react-progressive-web-apps-part-1-1cf381421672)  
[_Progressive Web Apps(PWA) are gaining a lot of popularity these day, and with one of the updates this year (2017), the…_medium.com](https://medium.com/progressive-web-apps/react-progressive-web-apps-part-1-1cf381421672)

Converting Angular apps to PWAs:

[**A new Angular Service Worker — creating automatic progressive web apps. Part 1: theory**](https://medium.com/progressive-web-apps/a-new-angular-service-worker-creating-automatic-progressive-web-apps-part-1-theory-37d7d7647cc7)  
[_Announcement: There is “Part 2: practice” of this article is available._medium.com](https://medium.com/progressive-web-apps/a-new-angular-service-worker-creating-automatic-progressive-web-apps-part-1-theory-37d7d7647cc7)

_Hope you enjoyed this article and found it to be a good read! You can check out all my projects on [Github](http://github.com/ajayns/) and don’t hesitate to reach out to me on [Twitte](https://twitter.com/ajayns08)r!_

