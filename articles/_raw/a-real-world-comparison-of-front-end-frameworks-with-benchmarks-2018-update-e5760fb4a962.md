---
title: A Real-World Comparison of Front-End Frameworks with Benchmarks (2018 update)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-31T05:59:39.000Z'
originalURL: https://freecodecamp.org/news/a-real-world-comparison-of-front-end-frameworks-with-benchmarks-2018-update-e5760fb4a962
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0aM-p4OCCxRMXroYn0qPVA.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Jacek Schae

  This article is a refresh of A Real-World Comparison of Front-End Frameworks with
  Benchmarks from December 2017.

  In this comparison, we will show how different implementations of almost identical
  RealWorld example apps stack up against...'
---

By Jacek Schae

This article is a refresh of [A Real-World Comparison of Front-End Frameworks with Benchmarks](https://medium.freecodecamp.org/a-real-world-comparison-of-front-end-frameworks-with-benchmarks-e1cb62fd526c) from December 2017.

In this comparison, we will show how different implementations of almost identical [RealWorld example apps](https://github.com/gothinkster/realworld) stack up against each other.

The [RealWorld example app](https://github.com/gothinkster/realworld) gives us:

1. **Real World App** — Something more than a “todo”. Usually “todos” don’t convey enough knowledge and perspective to actually build _real_ applications.
2. **Standardized** — A project that conforms to certain rules. Provides a back-end API, static markup, styles, and spec.
3. **Written or reviewed by an expert** — A consistent, real world project that, ideally, an expert in that technology would have built or reviewed.

#### Criticism from the last version (Dec 2017)

✅️ Angular was not in production. The demo app listed on the RealWorld repo was using a development version, but thanks to [Jonathan Faircloth](https://www.freecodecamp.org/news/a-real-world-comparison-of-front-end-frameworks-with-benchmarks-2018-update-e5760fb4a962/undefined) it is now in production version!

✅ Vue was not listed in the Real World repo, and thus was not included. As you can imagine, in the front-end world, this caused a lot of heat. How come you didn’t add Vue? What the heck is wrong with you? This time around Vue.js is in! Thank you [Emmanuel Vilsbol](https://www.freecodecamp.org/news/a-real-world-comparison-of-front-end-frameworks-with-benchmarks-2018-update-e5760fb4a962/undefined)**.**

#### Which libraries/frameworks are we comparing?

As in the December 2017 article, we included all implementations listed in the RealWorld repo. It doesn’t matter if it has a big following or not. The only qualification is that it appears on the [RealWorld repo](https://github.com/gothinkster/realworld) page.

![Image](https://cdn-media-1.freecodecamp.org/images/fe6a0GVWKWXwg0Q4XKm4JoFTKWvvAJEGFUFW)
_Frontends at [https://github.com/gothinkster/realworld](https://github.com/gothinkster/realworld" rel="noopener" target="_blank" title=") (April 2018)_

### What metrics do we look at?

1. **Performance:** How long does this App take to show content and become usable?
2. **Size:** How big is the App? We will only compare the size of the compiled JavaScript file(s). The CSS is common to all variants, and is downloaded from a CDN (Content Delivery Network). The HTML is common to all variants, too. All technologies compile or transpile to JavaScript, thus we only size this file(s).
3. **Lines of Code:** How many lines of code did the author need to create the RealWorld app based on spec? To be fair some apps have a bit more bells and whistles, but it should not have a significant impact. The only folder we quantify is `src/` in each app.

### Metric #1: **Performance**

Check out the [First meaningful paint](https://developers.google.com/web/tools/lighthouse/audits/first-meaningful-paint) test with [Lighthouse Audit](https://developers.google.com/web/tools/lighthouse/) that ships with Chrome.

The sooner you paint, the better the experience for the person who is using the App. Lighthouse also measures [First interactive](https://developers.google.com/web/tools/lighthouse/audits/first-interactive), but this was almost identical for most apps, and it’s in beta.

![Image](https://cdn-media-1.freecodecamp.org/images/n28etYksl006tP2qpK4DU1jbAPzxNrNVsfjp)
_First meaningful paint (ms) — lower is better_

You probably won’t see a lot of difference when it comes to performance.

### Metric #2: Size

Transfer size is from the Chrome network tab. GZIPed response headers plus the response body, as delivered by the server.

The smaller the file, the faster the download (and there’s less to parse).

This depends on the size of your framework as well as on any extra dependencies you added, and how well your build tool can make a small bundle.

![Image](https://cdn-media-1.freecodecamp.org/images/hKcfeFe6Y00GCEP93hzNHwDgGmxIt-eLeOLu)
_Transfer size (KB) — lower is better_

You can see that Svelte, Dojo 2, and AppRun do a pretty good job. I can’t say enough about Elm— especially when you look at the next chart. I’d like to see how [Hyperapp](https://hyperapp.js.org/) compares…maybe next time, [Jorge Bucaran](https://www.freecodecamp.org/news/a-real-world-comparison-of-front-end-frameworks-with-benchmarks-2018-update-e5760fb4a962/undefined)?

### Metric #3: Lines of Code

Using [cloc](https://github.com/AlDanial/cloc) we count the lines of code in each repo’s src folder. Blank and comment lines are **not** part of this calculation.Why is this meaningful?

> If debugging is the process of removing software bugs, then programming must be the process of putting them in — Edsger Dijkstra

![Image](https://cdn-media-1.freecodecamp.org/images/5o3DrlKWd-5ntxqFg9cTiLL1tKKdlogLzAwl)
_# lines of code — fewer is better_

The fewer lines of code you have, then the probability of finding an error is smaller. You also have a smaller code base to maintain.

### In conclusion

I’d like to say a big thank you to [Eric Simons](https://www.freecodecamp.org/news/a-real-world-comparison-of-front-end-frameworks-with-benchmarks-2018-update-e5760fb4a962/undefined) for creating the [RealWorld Example Apps](https://github.com/gothinkster/realworld) repo, and to numerous contributors who wrote different implementations.

**Update:** Thanks to [Jonathan Faircloth](https://www.freecodecamp.org/news/a-real-world-comparison-of-front-end-frameworks-with-benchmarks-2018-update-e5760fb4a962/undefined) for providing production version of Angular.

> And if you found this article interesting, you should [follow me on Twitter](https://twitter.com/jacekschae) and Medium.

