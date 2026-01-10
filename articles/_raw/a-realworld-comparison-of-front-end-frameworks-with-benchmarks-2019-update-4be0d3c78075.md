---
title: A Real-World Comparison of Front-End Frameworks with Benchmarks (2019 update)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-08T14:01:11.000Z'
originalURL: https://freecodecamp.org/news/a-realworld-comparison-of-front-end-frameworks-with-benchmarks-2019-update-4be0d3c78075
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9M_Anr2z0eC8AT0adn52Nw.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Jacek Schae

  Also available in:Turkish — thanks to @erdenizZz,Portugues — thanks to @felipefialho

  For the third time, we are comparing Front-End frameworks by using the Real World
  example apps. RealWorld example app gives us:

  RealWorld AppSomething...'
---

By Jacek Schae

Also available in:  
[Turkish](https://medium.com/@erdenizZz/front-end-frameworklerinin-ger%C3%A7ek-bir-kar%C5%9F%C4%B1la%C5%9Ft%C4%B1r%C4%B1lmas%C4%B1-2019-9f417c1c9261) — thanks to [@erdenizZz,](https://medium.com/@erdenizZz)  
[Portugues](https://medium.com/@felipefialho/front-end-frameworks-compara%C3%A7%C3%A3o-realword-com-benchmarks-vers%C3%A3o-2019-ed1024ee3cba) — thanks to [@felipefialho](http://twitter.com/felipefialho)

For the third time, we are comparing Front-End frameworks by using the [Real World example apps](https://github.com/gothinkster/realworld). RealWorld example app gives us:

**RealWorld App**  
Something more than a “todo”. Usually “todos” don’t convey enough knowledge and perspective to actually build *real* applications.

**Standardized**  
A project that conforms to certain rules. Provides a back-end API, static markup, styles, and spec.

**Written or reviewed by an expert**  
A consistent, real-world project that, ideally, an expert in that technology would have built or reviewed.

### Which libraries/frameworks are we comparing?

As of the writing, there are 18 implementations of Conduit at the [RealWorld example app](https://github.com/gothinkster/realworld) repo.

**It doesn’t matter if it has a big following or not. The only qualification is that it appears on the RealWorld repo page.**

![Image](https://cdn-media-1.freecodecamp.org/images/mxmA13gZ63sf7YgfD2ZKaotbT5SDY9mXt9CD align="left")

*Frontends at* [*Real World*](https://github.com/gothinkster/realworld) *repo (Mar 2019)*

### What metrics do we look at?

#### **Performance**

How long does this App take to show content and become usable?

#### **Size**

How big is the App? We will only compare the size of the compiled JavaScript file(s). The CSS is common to all variants and is downloaded from a CDN (Content Delivery Network). The HTML is common to all variants, too. All technologies compile or transpile to JavaScript, thus we only size this file(s).

#### **Lines of Code**

How many lines of code did the author need to create the RealWorld app based on spec? To be fair some apps have a bit more bells and whistles, but it should not have a significant impact. The only folder we quantify is `src/` in each app.

### Metric #1: Performance

We’ll check the Performance score from [Lighthouse Audit](https://developers.google.com/web/tools/lighthouse/) that ships with Chrome. Lighthouse returns a Performance score between 0 and 100. 0 is the lowest possible score.

#### Audit Settings

![Image](https://cdn-media-1.freecodecamp.org/images/itrdsyHI0H0Jb0KJ5UJerNjzWqD9y53yBzzo align="left")

*Lighthouse Audit Settings for all tested apps*

Performance is a combined score from the following metrics

* First Contentful Paint
    
* First Meaningful Paint
    
* Speed Index
    
* First CPU Idle
    
* Time to Interactive
    
* Estimated Input Latency
    

For more details check [Lighthouse Scoring Guide](https://developers.google.com/web/tools/lighthouse/v3/scoring).

#### Performance TL;DR

The sooner you paint and the sooner someone can do something, the better the experience for the person who is using the App.

![Image](https://cdn-media-1.freecodecamp.org/images/atCnTzcBrZlj9WK-GtZdKHSilk8O8LoBN7UD align="left")

*Performance (points 0–100) — higher is better.*

*Note: PureScript was skipped due to a lack of Demo application.*

#### Conclusion

Most of the apps score above 90. You won’t probably feel a lot of difference when it comes to performance.

### Metric #2: Size

Transfer size is from the Chrome network tab. GZIPed response headers plus the response body, as delivered by the server.

This depends on the size of your framework as well as on any extra dependencies you added, and how well your build tool can eliminate the unused code from your bundle.

#### Size TL;DR

The smaller the file, the faster the download, and less to parse.

![Image](https://cdn-media-1.freecodecamp.org/images/DRmH8Fz15DLxXguz9d8NR0eVanX0U9xW9jom align="left")

*Transfer size in KB — fewer is better*

#### Conclusion

There is a lot of sensational things happening in this area. Svelte — The magical disappearing UI framework — really holds true to its punch line. Stencil is the new kid in this benchmark and also performs pretty well. Both are relatively new and are pushing the limits of what is possible in terms of size.

### Metric #3: Lines of Code

Using [cloc](https://github.com/AlDanial/cloc) we count the lines of code in each repo’s src folder. Blank and comment lines are **not** part of this calculation. Why is this meaningful?

> If debugging is the process of removing software bugs, then programming must be the process of putting them in — Edsger Dijkstra

#### Lines of Code TL;DR

This shows how succinct given library/framework/language is. How many lines of code do you need to implement almost the same app (some of them have a bit more belts and whistles) accordingly to the specification.

![Image](https://cdn-media-1.freecodecamp.org/images/Y7vQUAUrMzGi8l3K2VZujbrZYqAIPfKwYXZj align="left")

*\# lines of code — fewer is better*

*Note Imba: Imba was skipped due to* [*cloc*](https://github.com/AlDanial/cloc) *not being able to process* `.imba` files.

*Note Elm: Elm developers write the code a bit more vertically, thus the high count of LoC — at least this is* [*what I have been told*](https://twitter.com/rtfeldman/status/983384187116949505)*.*

*Note Angular+ngrx: LoC calculation done with* `/libs` folder only including `.ts` and `.html` files. If you believe this is wrong, please let me know what is the correct number and how did you calculate it.

*Note Hyperapp: LoC was not correct when the article was published, thanks to* [*Mateusz Kwasniewski*](https://twitter.com/kwasniew) *for pointing out the correct way to calculate LoC.*

#### Conclusion

ClojureScript with re-frame gives you the most bang? for the LoC. Clojure is known for being unusually expressive. If you care about you LoC you should check out ClojureScript, AppRun, and Svelte.

### Summary

Keep in mind that this is not exactly an apples-to-apples comparison. Some implementations use code splitting and some don’t. Some of them are hosted at GitHub, some at Now and some at Netlify. Do you still want to know which one is the best? The best one is the one that fits your needs.

**Q:** Do you like types?  
**A:** Look into Elm, PureScript, and TypeScript — Angular, AppRun, Dojo.

**Q:** Do you want to have a very small footprint?  
**A:** Check out Svelte, Stencil, and AppRun.

**Q:** Do you want to have the smallest code base to maintain?  
**A:** Check out ClojureScript with re-frame, AppRun and Svelte.

**Q:** Want to learn something new?  
**A:** Pick the one you don’t know!

### FAQ

#### **#1 Why were framework X, Y, and Z not included in this comparison?**

Because the implementation is not completed at [RealWorld repo](https://github.com/gothinkster/realworld). Consider contributing! Implement the solution in your favorite library/framework of choice and we will include it next time!

#### #2 Why do you call it the real world?

Because it’s a bit more than a To-Do app. By RealWorld we don’t mean that we’ll compare salaries, maintenance, productivity, learning curves, etc. There are [other surveys](https://insights.stackoverflow.com/survey/2018/) that answer some of these questions. What we mean by RealWorld is an application that connects to a server, authenticates, and allows users to CRUD — just as a real-world app would do.

#### #3 Why didn’t you include my favorite framework?

Please see #1 above, but just in case, here it comes again: because the implementation is not completed at [RealWorld repo](https://github.com/gothinkster/realworld). I don’t do all of the implementations — it’s a community effort. Consider contributing if you want to see your framework in the comparison.

#### #4 Which version of the library/framework did you include?

The one that is available at the time of wiring (Mar 2019). The information comes from [RealWorld repo](https://github.com/gothinkster/realworld). I’m sure you can find this out from the [GitHub repo](https://github.com/gothinkster/realworld).

#### #5 Why did you forget to include a framework that is more popular than the one in the comparison?

Again, see above. The implementation is not complete at [RealWorld repo](https://github.com/gothinkster/realworld); it’s that simple.

Thanks to [Rich Harris](https://twitter.com/Rich_Harris) and [Richard](https://twitter.com/rtfeldman) Feldman for taking a look before publishing.

#### Updates:

When this article has been published the TL;DR LoC had following description:

> The fewer lines of code you have, then the probability of finding an error is smaller. You also have a smaller code base to maintain.  
>   
> If you like this article you should [follow me on Twitter](https://twitter.com/JacekSchae). I only write/tweet about programming and technology.
