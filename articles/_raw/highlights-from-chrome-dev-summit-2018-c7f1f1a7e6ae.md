---
title: Highlights from Chrome Dev Summit 2018
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-12T16:53:21.000Z'
originalURL: https://freecodecamp.org/news/highlights-from-chrome-dev-summit-2018-c7f1f1a7e6ae
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6QoOuhbOMjuUbJtzDXg-Dw.png
tags:
- name: Google Chrome
  slug: chrome
- name: Google
  slug: google
- name: performance
  slug: performance
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Chiamaka Ikeanyi

  Have you heard of Google Chrome Dev Summit? If you haven’t heard of it and the awesome
  cool things Chrome engineers have been working on lately, this article is for you.

  I’m a front-end engineer working on an application that serv...'
---

By Chiamaka Ikeanyi

Have you heard of Google Chrome Dev Summit? If you haven’t heard of it and the awesome cool things Chrome engineers have been working on lately, this article is for you.

I’m a front-end engineer working on an application that serves millions of users. I also use Chrome Dev Tools every day to debug and monitor performance. So I found it imperative to learn about the tools and technologies that will help me optimize my applications and contribute to building a better web. Debugging and optimizations become easier when you are aware of the tools to take advantage of, and metrics to look out for.

Chrome Dev Summit offered me the opportunity to hear about updates on these tools and technologies, and showed me avenues to contribute toward making these tools better. I learned a lot from Chrome engineers during the summit, and I would like you to benefit from that knowledge so we can build an awesome web experience together.

Chrome Dev Summit is an opportunity for Google Chrome engineers and leading web developers to celebrate the web platform, provide updates on their latest work, and get feedback from the community.

This year, developers from across the globe converged at Yerba Buena Center for the Arts in San Francisco, California for a two-day (12th and 13th November) exploration of modern web experiences. It was celebrated in style as Chrome engineers mark the 10-year anniversary of shipping Google Chrome, the most used web browser.

The event focused on what it means to build a fast, high-quality web experience using modern web technologies and best practices, as well as looking at new and exciting capabilities coming to the web platform. The major highlights are summarized below.

### Performance Budgets

An increasing number of features in web applications today are also being accessed using low-end devices on high latency networks. Because of this, JavaScript becomes [expensive](https://medium.com/@addyosmani/the-cost-of-javascript-in-2018-7d8950fbb5d4) thereby requiring [performance budgeting](https://addyosmani.com/blog/performance-budgets/).

![Image](https://cdn-media-1.freecodecamp.org/images/6SHRW7kkfPoPjCqDLD2Jjy3C-exGXkSjt76n)
_A Performance Budget is a framework that allows you to determine what changes represent progress and what changes represent regression, taking into account a set of shared metrics and budgets for each made actionable_

However, we need to have metrics in place to measure before we can improve on them, as it is impossible to measure what we do not track. When we care about exceptional user experience irrespective of device or network conditions, [building a PWA](https://developers.google.com/web/progressive-web-apps/) with performance in mind becomes a priority.

To build a high-quality web experience, Google developed tools like Lighthouse, PageSpeed Insights, and Chrome User Experience Report(CrUX) to help developers monitor and enhance the web platform. A new lighthouse UI was announced at the event with PWA Refactor, a reduction in lighthouse runtime, and new score bucketing.

![Image](https://cdn-media-1.freecodecamp.org/images/5bUg2is4JueISZ1rZOyjz8p3DXl2WtfYfom1)
_The new Lighthouse score bucketing_

We can also [integrate Lighthouse](https://github.com/ebidel/lighthouse-ci) to our development workflow so it runs on every commit. This helps us to keep an eye on performance.

![Image](https://cdn-media-1.freecodecamp.org/images/eLG9CubQr2dDiVYrSjRcGIa1HDjYg-geIqd-)
_Running Lighthouse in CI_

Tools to help monitor the cost of packages:

* [Webpack Bundle Analyzer](https://www.npmjs.com/package/webpack-bundle-analyzer) which creates a treemap visualization of the contents of your bundles. It helps determine modules that make up most of its size.
* [Bundlephobia](https://bundlephobia.com/) helps to discover the cost of adding an npm package to your bundle.
* [Bundlesize](https://www.npmjs.com/package/bundlesize) helps keep your bundle size in check. You can integrate it in such a way that PRs can’t be merged once the bundle size is greater than the target maximum size.

![Image](https://cdn-media-1.freecodecamp.org/images/WBTc5rwOOoi7FlOIChBRQVNhfL2DGhg9Hw-U)
_Bundle size checks in CI process_

### PageSpeed Insights Powered by Lighthouse

Because of the varying results analysis gotten from PageSpeed Insights and Lighthouse when measuring the performance of websites, the Chrome team introduced PageSpeed API v5. It is essentially Lighthouse API v1 to power PageSpeed Insights. This means that the differing results will be history. PageSpeed Insights also incorporates field data provided by the [CrUX](https://developers.google.com/web/tools/chrome-user-experience-report/).

```
await fetch(`https://www.googleapis.com/pagespeedonline/v5/runPagespeed?&url=${url}`)
```

![Image](https://cdn-media-1.freecodecamp.org/images/f33Kx7eVWw0tMDTIXVoDXbuUUzhpcYLRLhCv)
_By [Paul Irish](undefined" rel="noopener" target="_blank" title=") and Elizabeth Sweeny at Chrome Dev Summit_

### First Input Delay

We are conversant with measuring Speed Index(SI), First Contentful Paint(FCP), Time to Interactive(TTI), First CPU Idle(FCPI) and other metrics which you may have seen using [Lighthouse](https://developers.google.com/web/tools/lighthouse) or [WebPageTest](https://www.webpagetest.org). To help measure a user’s first impression of your site’s interactivity and responsiveness, a new metric was introduced called First Input Delay.

![Image](https://cdn-media-1.freecodecamp.org/images/9yJDWbSpxsXxr3CQntqCXbyPTMafsfYH1lGl)
_By [Paul Irish](undefined" rel="noopener" target="_blank" title=") at Chrome Dev Summit_

First Input Delay (FID) measures the time from when a user first interacts with your site (i.e. when they click a link, tap on a button, or use a custom, JavaScript-powered control) to the time the main thread is free from the long task it is performing, making it possible for the browser to respond to the user’s interaction.

Is that not the same as TTI you may ask? Well, no it is not. Time to interactive (TTI) measures how long it takes your app to load and become capable of quickly responding to user interactions. On the other hand, First Input Delay (FID) is a metric that measures the delay that users experience when they interact with the page while it’s not yet interactive.

![Image](https://cdn-media-1.freecodecamp.org/images/8RwMGUnZmRP25fv5Zdit8gihaZO2KsRtZmIQ)
_The browser receives the input when the main thread is busy, so it has to wait until it’s not busy to respond to the input. The time it must wait is the FID value for this user on this page._

[FID](https://github.com/GoogleChromeLabs/first-input-delay) is a field metric meaning that it can be seen when actual users are really interacting with the web app, while TTI is a lab metric. Field metrics capture a wide spectrum of real-world network conditions and devices used by Chrome users. This can be well measured using Real User Monitoring (RUM) tools like the [Chrome UX Report](https://developers.google.com/web/tools/chrome-user-experience-report/).

Server-side rendered JavaScript apps and sites with third-party iframes need to be particular about tracking this metric. They are susceptible to high FID values especially on low-end devices that take longer to parse and execute JavaScript.

![Image](https://cdn-media-1.freecodecamp.org/images/l-Kpu7dcufzgptE5uyJzRAGOPeOR1-OyieZ3)
_Where to gather these metrics_

### WebP Image Format

Images don’t just become performant on the fly — there are appropriate measures to be put in place to achieve that. You must consider using the right format, compression techniques, and image lazy-loading. With the introduction of [WebP](https://developers.google.com/speed/webp/), a new image format that results in an average of 30% savings, the cost of serving images — which is the largest component of most sites — is reduced.

WebP provides superior lossy and lossless compression for images on the web with support for transparency, making the web faster. Due to the fact that WebP is not yet supported across all browsers, it is advisable to use the `**<pictu**`re> element to provide fallbacks. The image format would then be used on supported browsers while web browsers that don’t yet support WebP will use the image in the format they support.

![Image](https://cdn-media-1.freecodecamp.org/images/aBAOa1f4ODx6im4sRF8r5gZif0zrdohww8E6)
_WebP support stat on [caniuse.com](https://caniuse.com/" rel="noopener" target="_blank" title=")_

![Image](https://cdn-media-1.freecodecamp.org/images/7obCuyaIAxHyCH2U4cM9kciX-9JbWnXF8TAg)
_WebP support stat by Katie Hempenius at Chrome Dev Summit_

```
<picture>  <source type="image/webp" srcset="imagename.webp">  <source type="image/jpeg" srcset="imagename.jpeg">  <img src="imagename.jpeg" alt="image description"></picture>
```

To compress images to and from the WebP format, `[**cwebp**](https://developers.google.com/speed/webp/docs/cwebp)` and `[**dwebp**](https://developers.google.com/speed/webp/docs/dwebp)` command-line tools can be used respectively. Go and try out this image format on [squoosh](https://squoosh.app/) (upload your image and view the compression rate).

### Native Lazy Loading

To improve user experience on the web, native lazy-loading will be coming to Chrome. When added to image tags and cross-origin iframes, this defers the loading of the resource until the page is scrolled down near them. It is supported across all chrome platforms — Mac, Windows, Linux, Chrome OS, Android

To lazy-load resources, use the `lazyload` attribute with “on or off” value. If no value is specified, the browser decides which resource to lazy load.

```
<img src="imagename.png" lazyload="on">
```

### Zero Friction Navigation on the Web

Navigating on the web has not been seamless compared to the experience with native apps. It is a painful experience, especially when navigating the web using low-end devices on slow networks, leaving users staring at a white screen waiting for content to be displayed on the screen. To come to the rescue of these web users, Chrome engineers announced **Web Packaging and Portals.**

![Image](https://cdn-media-1.freecodecamp.org/images/83-0VN2Zyz4DxfaIhndbzbdUmP8yTor8tM4A)
_Available on mobile devices only. The icon identifies the sites that have implemented AMP_

Built on the Accelerated Mobile Pages (AMP) model and achieved through [signed exchanges](https://developers.google.com/web/updates/2018/11/signed-exchanges), [Web Packaging](https://github.com/WICG/webpackage) introduces the ability to sign a web page with a special encryption key that proves the page’s original domain. It then creates a package that can be served from anywhere, which will be used by the browser to represent the domain enabling privacy-preserving instant navigations.

[Portals](https://github.com/KenjiBaheux/portals) work like an iframe but can be navigated into allowing users to transition to the portal’s content. It abstracts navigation between pages, making the user feel like they are on a single-page application.

```
<portal src="https://mywebsite.com"></portal>
```

When the created view is clicked on, add some animations and trigger the activate event:

```
portal.activate();
```

The two proposals combined together enable zero-friction page transitions across the web. This is still early in the development stage, and is therefore subject to change.

### Web.dev

A web platform built to help developers learn how to build for the web and ensure the website is meeting good practice goals. [Web.dev](https://web.dev/) focuses on why developers need to care about a given concept, and gives tips to help developers build a better web keeping it fast, discoverable, accessible, safe and resilient.

![Image](https://cdn-media-1.freecodecamp.org/images/tA9MC830sETVhFxsuvj5xe9fNQTCznIueVwy)

### VisBug

Built with accessibility in mind, [VisBug](https://chrome.google.com/webstore/detail/visbug/cdockenadnadldjbbgcallicgledbeoc) is a tool that can come in handy for engineers. With this extension, you can explore and tweak your site right in the browser to view the building blocks and how it looks if designed differently.

![Image](https://cdn-media-1.freecodecamp.org/images/jwnTD3kNW9BmZCkLGqVN7TQc75PhgYkUBfPQ)
_Using VisBug on my site_

### Squoosh

Squoosh is a 15kB JavaScript-driven progressive web application for image compression written in C. It is compiled using [**emscripten**](https://github.com/kripken/emscripten) to web assembly with best-in-class codecs right in the browser.

![Image](https://cdn-media-1.freecodecamp.org/images/Yvs8MDF29mIMbnT64FMxccL9n7whzeR5W-Ce)
_An original image size of **163kB**: Notice the compression rate of WebP compared to MozJPEG_

Having performance in mind, the team made use of appropriate technologies following coding and performance best practices to yield a performant application:

* Preact (a 3kB library) to orchestrate the DOM
* WebPack for bundling and code splitting
* Web workers for lazy loading and concurrency
* Dynamic module imports
* Web components (a lower level primitive used by Polymer) for custom element polyfill on Edge

As [Jake Archibald](https://www.freecodecamp.org/news/highlights-from-chrome-dev-summit-2018-c7f1f1a7e6ae/undefined) would say, [go squoosh](https://squoosh.app/) some images.

### Key Points

* Performance decisions should be made based on data. Respect the user, their data and preferences.
* As developers, we need to test using low-end devices on slow network connections. When we develop for the web using fast devices on fast network connections, we can’t really feel what our users feel and think we met our performance goals.
* Performance is not an engineering priority. The success of performance initiatives depends on cross-functional buy-ins. There should be an organizational alignment across all teams that affect the website (marketing, design, engineering etc.).
* Understand how service workers affect the performance of your site. They can affect it positively or negatively depending on the implementation.
* Users value a consistent user journey. So, try to reduce friction on your web applications.
* Measure apps using the RAIL model — Response, Animation, Idle, and Load.
* Use HEART (Happiness, Engagement, Adoption, Retention, Task Success) framework to determine the quality of your web app UI.
* Some of these announced features covered here and more are behind Chrome flags — chrome://flags/

### Conclusion

This is just the tip of the iceberg — you wouldn’t want to miss the details. The future is on the web and performance is at the root of it all. All recorded sessions throughout the event are available on the [Google Chrome Developers Channel](https://www.youtube.com/playlist?list=PLNYkxOF6rcIDjlCx1PcphPpmf43aKOAdF). The code is available on [GitHub](https://github.com/GoogleChromeLabs).

Let’s build a better web ?

