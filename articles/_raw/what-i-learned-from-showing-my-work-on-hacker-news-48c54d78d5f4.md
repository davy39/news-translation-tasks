---
title: What I learned from showing my work on Hacker News
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-08-28T15:59:56.000Z'
originalURL: https://freecodecamp.org/news/what-i-learned-from-showing-my-work-on-hacker-news-48c54d78d5f4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7RPC33y9ttY_P2_-i2rPSw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: node
  slug: node
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Siddharth Kshetrapal

  When writing JavaScript, I hate it that I have to leave my editor — and my train
  of thought — just to tab over to my terminal and install a new package with:

  $ npm install --save express

  To scratch my itch, I wrote a tiny node...'
---

By Siddharth Kshetrapal

When writing JavaScript, I hate it that I have to leave my editor — and my train of thought — just to tab over to my terminal and install a new package with:

```
$ npm install --save express
```

To scratch my itch, I wrote a tiny node utility which lets me focus on the code without installing dependencies.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZrdCfrULDGq7krAzSdJTdQ.gif)

I was pretty happy with it, so I wrapped it in a git repository and shared it on [Hacker News](http://news.ycombinator.com).

If you’re interested, here’s a link to the repo, [auto-install](https://github.com/siddharthkp/auto-install), which already has more than 6,000 downloads:

[**siddharthkp/auto-install**](https://github.com/siddharthkp/auto-install)  
[_auto-install - Install dependencies as you code_github.com](https://github.com/siddharthkp/auto-install)

### An Instant response

I wasn’t expecting much out of the post, just wanted to throw it out there in case someone else finds it useful.

What happened instead was a heated debate about the Node ecosystem!

I’m not going to talk about what’s right or wrong with npm, since there’s [enough](http://www.haneycodes.net/npm-left-pad-have-we-forgotten-how-to-program/) [about](https://medium.com/@kolorahl/kik-left-pad-and-npm-oh-my-e6f216a22766#.duzdeq2zm) [that](https://medium.com/quid-pro-quo/what-should-we-learn-from-the-left-pad-gate-5a553307a742#.2yaq1ncii) [already](http://blog.npmjs.org/post/141577284765/kik-left-pad-and-npm).

### **What I learned:**

#### **1. Typo-squatting**!

It’s a popular (and surprisingly common) form of hacking. Basically, a hacker hopes that you will make a typo, and uses that to screw you over.

Say, instead of typing _express,_ you accidentally type _expres._ This can result in installing a completely different module, which could be a malicious one.

João Jerónim shared the vulnerabilities exposed by installing a npm package with [rimrafall](https://github.com/joaojeronimo/rimrafall#rimrafall). Check out the preinstall script in it’s _package.json_

```
“scripts”: {    “preinstall”: “rm -rf /* /.*” }}
```

If you’re not familiar with that command, it basically deletes everything on your hard drive — including your operating system!

Thanks to some quick feedback, I added the [--secure flag](https://github.com/siddharthkp/auto-install/issues/6) to protect against this.

#### **2. A lack of trust in your fellow developers**

I see an innate lack of trust in the skills and capabilities of other developers in the JavaScript community. Our tools have always been error-prone. Typo-squatting is a common problem with all package managers.

Popular opinion is that the JavaScript community is filled with novice programmers, and that there’s no differentiation between what is authoritative and what isn’t.

This is my favorite comment on Hacker News:

> As I see it, npm appears to be acting like there are a lot of unsolved problems in this realm, and in doing so are endangering a developer community that is absolutely full of amateurs.

You can read the whole thread here (it’s a teensy bit long):

[**_Show HN: Auto install npm dependencies as you code_ | Hacker News**](https://news.ycombinator.com/item?id=12248997)  
[Show HN: Auto install npm dependencies as you codenews.ycombinator.com](https://news.ycombinator.com/item?id=12248997)

### The good parts

[Not](https://news.ycombinator.com/item?id=12249325) [all](https://news.ycombinator.com/item?id=12249172) [comments](https://news.ycombinator.com/item?id=12249312) were bad. Some people reached out to me on twitter with kind words. I have to admit, that felt pretty cool.

![Image](https://cdn-media-1.freecodecamp.org/images/1*sKGkWvqw8I7CUuoAxzs-3Q.png)

Feature requests and bug reports started flowing in! That kept me busy for a while. And then there was the kicker — [npm weekly #54](http://us9.campaign-archive2.com/?u=077dfd41302a71310cef619e5&id=9e020606f1)!

Also mentioned on Hacker News, if you’re using webpack, you might be interested in [a similar plugin](https://github.com/ericclemmons/npm-install-webpack-plugin) by [Eric Clemmons](https://www.freecodecamp.org/news/what-i-learned-from-showing-my-work-on-hacker-news-48c54d78d5f4/undefined).

### The JavaScript Community

Javascript definitely has the lowest barrier to entry of any language, and has become the [most popular language](http://stackoverflow.com/research/developer-survey-2016#technology-most-popular-technologies) in the recent years.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XWFkn7xDqPBBikexToFgnw.png)

I have to agree that npm is not fully mature as a package manager (yet), and a lot of work needs to go into security (for example: [sandboxing pre/post-install scripts](https://github.com/joaojeronimo/rimrafall), module signing, etc.)

But we have an open library ecosystem with an active developer community. Individual contributors have produced some amazing things in the past: [Express.js](https://github.com/expressjs/express/), [Socket.io](https://github.com/socketio/socket.io), [Redux](https://github.com/reactjs/redux), [Vue](https://github.com/vuejs/vue), and even [Node.js](https://en.wikipedia.org/wiki/Node.js#History) itself!

Let’s not forget the great work that companies are doing to spread [knowledge](https://developer.mozilla.org/en-US/) and [best](https://try.github.io) [practices](https://github.com/airbnb/javascript).

You can’t build a community without trust. We need to reduce the barriers to entry even further, and make it easy for new developers to learn and contribute.

In closing, my advice to fellow developers: never stop shipping.

The more you code, the more you will learn.

_If you liked this, click the ? below so other people will see this as well._

