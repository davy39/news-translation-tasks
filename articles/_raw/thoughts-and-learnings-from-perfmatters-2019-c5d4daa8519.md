---
title: 'What I learned from attending the #PerfMatters conference'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-05T21:38:11.000Z'
originalURL: https://freecodecamp.org/news/thoughts-and-learnings-from-perfmatters-2019-c5d4daa8519
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5ECCYqZOEG5Tui_YIWybRw.png
tags:
- name: conference
  slug: conference
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Stacey Tay

  Notes from a front-end web performance conference

  This week I had the privilege of attending #PerfMatters, a conference focused on
  front-end web performance. I’ve never been to a conference before, but I was thrilled
  to be attending bec...'
---

By Stacey Tay

#### Notes from _a_ front-end web performance conference

This week I had the privilege of attending [#PerfMatters](https://perfmattersconf.com), a conference focused on front-end web performance. I’ve never been to a conference before, but I was thrilled to be attending because it promised an [amazing lineup of speakers](https://perfmattersconf.com/2019) and [topics](https://perfmattersconf.com/schedule/).

I started [delving into web performance](https://medium.com/carousell-insider/how-we-made-carousells-mobile-web-experience-3x-faster-bbb3be93e006) about over a year ago, and so thought this would be a great chance to deepen my knowledge and meet other people in the community.

This post consists of three parts:

(1) my experience attending the conference,

(2) some of the things I learnt at the conference, and

(3) parting thoughts.

### Thoughts on the conference experience

#### Everyone is so friendly and approachable

I went alone and it was a fairly intimidating experience, since I’m generally a shy person and can take awhile to warm up. But, I made a rule to not sit alone during lunch and to try to talk to at least 2 people each day. I’m glad I did because everyone I met was nice and fun to talk to.

I ended up meeting a lot of people, talking about things ranging from the [PRPL pattern](https://developers.google.com/web/fundamentals/performance/prpl-pattern/), experimenting with [Cloudflare workers](https://blog.cloudflare.com/introducing-cloudflare-workers/) to better serve users in Australia (from servers in the US), functional programming’s increasing prevalence in front-end web development, and how to get started with snowboarding (not performance related, in case you’re wondering).

#### The talks were absolutely amazing

All the speakers had something related to web performance in one form or another to talk about, and it was obvious that they put in a lot of effort into their presentations. [Jenna Zeigen](https://mobile.twitter.com/zeigenvector)’s [talk](https://perfmattersconf.com/talks/#jenna) covered a long list of performance tricks and each of her points had a song lyric to go along with them, which was so entertainingly informative. She told me that it took her about 15 minutes for each song and there’s like over 30 in there ?

> Videos of the talks should be announced on [@perfmattersconf](https://mobile.twitter.com/perfmattersconf) soon, but a number of the slides have already been published with [#perfmattersconf](https://mobile.twitter.com/hashtag/perfmattersconf).

#### The talks cover the many facets of working on web performance

Improving a web page’s performance isn’t just a one-off audit, fixing the problems that makes that page slow, and then moving on. It takes a **concerted effort from all stakeholders**—business, design, engineering, marketing, product—in an organisation to get and stay fast.

The talks weren’t all just about how we could improve [_TTI_](http://Improving%20a%20web%20page%E2%80%99s%20performance%20isn%E2%80%99t%20just%20a%20one-off%20audit,%20fixing%20the%20problems%20that%20makes%20that%20page%20slow,%20and%20moving%20on.%20It%20takes%20a%20concerted%20effort%20from%20all%20stakeholders%E2%80%94business,%20design,%20engineering,%20marketing,%20product%E2%80%94in%20an%20organisation%20to%20get%20and%20stay%20fast.)s or load times, which are important. But, they also covered the other important parts of **making the web accessible and usable for as many people as possible**. From [how people perceive performance](https://mobile.twitter.com/GemmaPetrie/status/1113508695428612097) to [empowering a performance culture](https://perfmatters.alfre.do), and from [**how privilege defines performance**](https://mobile.twitter.com/fox/status/1113675170374475776?s=20) to the [intersection of performance and accessibility](https://noti.st/ericwbailey/Yfyaxa).

![Image](https://cdn-media-1.freecodecamp.org/images/1*5ECCYqZOEG5Tui_YIWybRw.png)
_❤️ Thoughtful swag from the conference ♻️_

### A non-exhaustive list of performance tips and tricks learnt

Some, if not all, of these might be common knowledge, but many were new to me.

#### Performance Culture

* [**Empower developers with tools**](https://perfmattersconf.com/talks/#greg) to enable better performance. Also, [make performance part of the development process](https://perfmatters.alfre.do/#/27).
* **Compare your site with your competitors’** to get executive buy-in on driving performance. Use [WebPagetest’s side-by-side video comparison](https://www.webpagetest.org/video/) of your webpage against a competitor’s loading journey to succinctly drive your point across.
* **Measure the potential annual revenue gains** from increasing site speed with [Google’s Test My Site tool](https://www.thinkwithgoogle.com/feature/testmysite).

#### Performance on the Web

* [**Latency has an outsized impact over bandwidth**](http://www.stuartcheshire.org/rants/latency.html) on network requests.
* [**SVG animations**](https://css-tricks.com/book-release-svg-animations/) **are great for animating loaders** because of their (relatively) smaller sizes.
* [**Squeeze your page into 14KB** if possible, to avoid multiple round trips because of TCP slow-start](https://calendar.perfplanet.com/2018/tcp-slow-start/).
* **Not all CDNs are doing [HTTP/2 prioritisation as expected](https://github.com/andydavies/http2-prioritization-issues).**
* **If you have to use web fonts**, [Zach Leatherman](https://mobile.twitter.com/zachleat) wrote a [great guide on how to load them well](https://www.zachleat.com/web/comprehensive-webfonts/).
* **Perceived performance is influenced** by **_duration_** (actual duration that a process takes, referred to as “performance”), **_responsiveness_**, **_fluency_** (perceived smoothness of a process), and **_tolerance_** (how long does the user expect a process to take). [Slides](https://docs.google.com/presentation/d/1mMgpxtnyqBJsyhY5jOmh1DF0eqOPEijCH23ef9uya3U/edit) from [Gemma Petrie](https://gemmapetrie.com) and [Heather McGaw](https://mobile.twitter.com/HeatherMcGaw)’s talk on _Measuring Perceived Performance to Prioritize Product Work_.

#### Some Neat Tools

* **Chrome’s [code coverage tool](https://developers.google.com/web/updates/2017/04/devtools-release-notes#coverage)** is useful for determining where and when to code-split stuff out. Interact with the page a little to see how the numbers change, and according to [Tim Kaldec](https://timkadlec.com), about 45% unused code is normal and it’ll be diminishing marginal gains to optimise over that.
* **Chrome’s [override network resource](https://developers.google.com/web/updates/2018/01/devtools#overrides)** feature allows developers to return a locally saved file, which is useful for debugging something on the fly.
* [**Google Docs Spreadsheet to do bulk WebPagetest audits**](https://calendar.perfplanet.com/2014/driving-webpagetest-from-a-google-docs-spreadsheet/)**.**
* [**Online JavaScript AST explorer**](https://astexplorer.net) (alright, this one isn’t exactly related to web performance, but I found out about it during the conference and can’t stop playing with it).
* [**Request Map**](http://requestmap.webperf.tools/render/190405_F1_ab827a1745d3fb3eac56185132ebb952) creates a network graph from a web page and is useful for visualising third party requests.

### Parting Thoughts

If there’s one overarching theme I got from the conference, it’s that to be good at web performance, it’s crucial to understand [how](https://www.slideshare.net/KatrinaSylorMiller/happy-browser-happy-user-perfmatters-conference-2019) [the browser](https://jenna.is/slides/at-perfmatters.pdf) [_works_](https://github.com/ksylor/happy-browser-happy-user) (things like how [rendering](https://developers.google.com/web/fundamentals/performance/critical-rendering-path/render-tree-construction) happens and the [critical rendering path](https://developers.google.com/web/fundamentals/performance/critical-rendering-path/)). But, **performance doesn’t just stop at technical gains**.

> Getting buy-in from all stakeholders, not just engineering, is crucial to improving and maintaining performance because web performance goes beyond loading a page as fast as possible.

There’s also **perceived performance** to consider, and then determining whether further improvements in performance creates **additional significant business or user improvements**. It’s important to keep in mind that **performance is just _one_ part of the user experience**.

I didn’t take too many photos during the conference (note to self to definitely take more photos the next time), but I did manage to snap this one.

![Image](https://cdn-media-1.freecodecamp.org/images/1*C7ySQkNv1gOAYOf-UOS9_w.jpeg)
_✨ Slide from Addy Osmani’s [talk](https://perfmattersconf.com/talks/#addy" rel="noopener" target="_blank" title=") on The Cost Of JavaScript ?_

If you’re interested in web performance or just web development in general, this is an amazing conference to [check out](https://mobile.twitter.com/perfmattersconf) and it’s scheduled to happen next year too! There’s also a [scholarship program](https://perfmattersconf.com/diversity/) for those unable to attend without financial assistance. Looking forward to seeing you there next year!

_Thanks to [Hui Yi](https://www.freecodecamp.org/news/thoughts-and-learnings-from-perfmatters-2019-c5d4daa8519/undefined), [Jingwen Chen](https://www.freecodecamp.org/news/thoughts-and-learnings-from-perfmatters-2019-c5d4daa8519/undefined), and [Yao Hui Chua](https://www.freecodecamp.org/news/thoughts-and-learnings-from-perfmatters-2019-c5d4daa8519/undefined) for reading an earlier draft and sharing their feedback._

