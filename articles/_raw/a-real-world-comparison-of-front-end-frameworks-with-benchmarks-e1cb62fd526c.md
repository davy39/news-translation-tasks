---
title: A Real-World Comparison of Front-End Frameworks with Benchmarks
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-19T06:15:08.000Z'
originalURL: https://freecodecamp.org/news/a-real-world-comparison-of-front-end-frameworks-with-benchmarks-e1cb62fd526c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*C_VGnwYj_OAnTVT0ae7KQQ.png
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Jacek Schae

  UPDATE: There is a newer version of this article

  A Real-World Comparison of Front-End Frameworks with Benchmarks (2018 update)This
  article is a refresh of A Real-World Comparison of Front-End Frameworks with Benchmarks
  from December 20...'
---

By Jacek Schae

**UPDATE:** There is a newer version of this article

[**A Real-World Comparison of Front-End Frameworks with Benchmarks (2018 update)**](https://medium.freecodecamp.org/a-real-world-comparison-of-front-end-frameworks-with-benchmarks-2018-update-e5760fb4a962)  
[*This article is a refresh of A Real-World Comparison of Front-End Frameworks with Benchmarks from December 2017.\_medium.freecodecamp.org*](https://medium.freecodecamp.org/a-real-world-comparison-of-front-end-frameworks-with-benchmarks-2018-update-e5760fb4a962)

Over the last couple of years we have seen an explosion of front-end frameworks. Each one of them is more than capable of building great web applications. So how do you compare and decide which one to use for your next project?

First of all, to make a meaningful comparison we need a few things:

1. **Real World App** - Something more than a “todo”. Usually “todos” don’t convey knowledge & perspective to actually build *real* applications.
    
2. **Standardized** - A project that conforms to certain rules. Hosted at the same place, provides a back-end API, static markup, styles, and spec.
    
3. **Written by an expert** - A consistent, real world project, that ideally an expert in that technology would have built. This is true, at least most of the time (see below).
    

So how do we get such a project? The good news is that [Eric Simons](https://www.freecodecamp.org/news/a-real-world-comparison-of-front-end-frameworks-with-benchmarks-e1cb62fd526c/undefined) already created a [RealWorld](https://github.com/gothinkster/realworld) project. It’s a clone of the Medium blogging platform. Each implementation of this project uses the same HTML structure, CSS, and API spec, but a different library/framework. When it comes to expert knowledge it’s true most of the time. I wrote an implementation in ClojureScript and [re-frame](https://github.com/Day8/re-frame) and I don’t consider myself an expert. In my defense an expert reviewed my code - thanks [Daniel Compton](https://www.freecodecamp.org/news/a-real-world-comparison-of-front-end-frameworks-with-benchmarks-e1cb62fd526c/undefined).

Now we have a baseline spec, we need a standard set of tests/metrics to compare them.

1. **Performance.** How long does this App take to show content and become usable?
    
2. **Size.** How big is the App? We will only compare the size of the compiled JavaScript. The CSS is common to all variants, and is downloaded from a CDN (Content Delivery Network). The HTML is common to all variants too. All technologies compile or transpile to JavaScript, thus we only size this file.
    
3. **Lines of Code.** How many lines of code did the author need to create RealWorld app based on spec? To be fair some apps have a bit more bells and whistles, but it should not have a significant impact. The only folder we quantify is src/ in each app.
    

At the time of writing (Dec 2017) the RealWorld project is available in the following frameworks:

* [React / Redux](https://github.com/gothinkster/react-redux-realworld-example-app)
    
* [Elm](https://github.com/rtfeldman/elm-spa-example)
    
* [Angular 4+](https://github.com/gothinkster/angular-realworld-example-app)
    
* [Angular 1.5+](https://github.com/gothinkster/angularjs-realworld-example-app)
    
* [React / MobX](https://github.com/gothinkster/react-mobx-realworld-example-app)
    
* [Crizmas MVC](https://github.com/gothinkster/crizmas-mvc-realworld-example-app)
    
* [CLSJ Keechma](https://github.com/gothinkster/clojurescript-keechma-realworld-example-app)
    
* [AppRun](https://github.com/gothinkster/apprun-realworld-example-app)
    
* [CLJS re-frame](https://github.com/jacekschae/conduit) (This is the one I did. It’s not yet listed at RealWorld Project).
    

### Metric #1: Performance

[First meaningful paint](https://developers.google.com/web/tools/lighthouse/audits/first-meaningful-paint) test with [Lighthouse Audit](https://developers.google.com/web/tools/lighthouse/) that ships with Chrome.

The sooner you paint, the better the experience for the person who is using the App. Lighthouse also measures [First interactive](https://developers.google.com/web/tools/lighthouse/audits/first-interactive), but this was almost identical for most apps.

![Image](https://cdn-media-1.freecodecamp.org/images/PjhM-gKQrawvRPhnSaEFNAL37OgDtSap3FPw align="left")

*First meaningful paint (ms) - lower is better*

### Metric #2: Size

Transfer size is from the Chrome network tab. GZIPed response headers plus the response body, as delivered by the server.

Smaller file = faster download and less to parse.

This depends on the size of your framework, any extra dependencies you added, and how well your build tool can make a small bundle.

![Image](https://cdn-media-1.freecodecamp.org/images/XEfqu6RhFdM0M3DKct1wD855Cjsp7MCl8jE4 align="left")

*Transfer size (KB) - lower is better*

### Metric #3: Lines of Code

Using [cloc](https://github.com/AlDanial/cloc) we count lines of code in each repo’s src folder. Blank and comment lines are **not** part of this calculation.Why is this meaningful?

> If debugging is the process of removing software bugs, then programming must be the process of putting them in - Edsger Dijkstra

The fewer lines of code you have the smaller probability of an error and smaller code base to maintain.

![Image](https://cdn-media-1.freecodecamp.org/images/ON1sQcGZEU9VfuY4BjXHbKI6lvHcBpjTaXRb align="left")

*\# Lines of code - fewer is better*

### Conclusion

#### Performance

This is a RealWorld Comparison and not a benchmark in a vacuum. Tests were performed out of Europe (Switzerland). All Apps were hosted on Github. Values may differ for you, which is fine. Tests were performed couple of times for each app, then averaged, and rounded. Results were pretty linear when comparing throughout the day. Most of the libraries/frameworks are in the range of excellent and good. You won’t see a lot of difference when it comes to performance.

#### Size

The bundle size for each App is always the same. We are comparing similar implementations and look at how bundle sizes differ. AppRun is insane! I looked a couple of times because I couldn’t believe it. Elm is doing an amazing job when it comes to bundle size and especially when you look at lines of code.

![Image](https://cdn-media-1.freecodecamp.org/images/olCdKtJHQdBhAnnI3GuQOwIA4Fq-VRBUTqJf align="left")

*AppRun bundle size 18.7KB*

#### **Lines of code**

This has the biggest impact on you as a software developer. The more lines of code, the more you need to type and more to maintain. There are some trade offs here. Especially when it comes to typed vs. dynamic languages. Types give you more safety and come at a cost - more things to type.

#### Typed vs. dynamic

**Typed**: Elm, Angular 4+ and AppRun.

**Dynamic**: React | Redux, Angular 1.5, React | MobX, Crizmas MVC, CLJS Keechma, and CLJS re-frame.

So which is better? It’s not better or worse, it’s different. Like TDD (Test Driven Development), some people love it, some hate it. You can develop great software with or without it - pick the one that fits you better.

#### Where are Vue, Preact, Ember, Svelte, Aurelia and others?

Seems like they are late to the party, but worry not. I’ll do another round when we have them. There are already [open issues](https://github.com/gothinkster/realworld/issues) - consider contributing! Or start from scratch and open a new issue.

#### Final word

This comparison is exactly what it says. Compares different implementations of similar real world web applications in a real world. I know, it’s not perfect. It differs based on server load, network traffic, and many other things that happen in the real world.

Thanks to [Daniel Compton](https://www.freecodecamp.org/news/a-real-world-comparison-of-front-end-frameworks-with-benchmarks-e1cb62fd526c/undefined) for proof-reading.

*If you enjoyed this article, and would like to be notified when I release similar article consider following me on medium and* [*twitter*](https://twitter.com/jacekschae)*.*
