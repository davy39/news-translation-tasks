---
title: 'npm cache: the unsung hero'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-22T21:41:06.000Z'
originalURL: https://freecodecamp.org/news/npm-cache-the-unsung-hero-11e646c09791
coverImage: https://cdn-media-1.freecodecamp.org/images/1*UmRnW6YyI9ygq81OaL8Y-Q.png
tags:
- name: JavaScript
  slug: javascript
- name: npm
  slug: npm
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Siddharth Kshetrapal

  I love npm and believe that this package manager is the single biggest reason for
  JavaScript’s massive success these past few years.

  There was a lot of excitement in the JavaScript community when facebook released
  yarn. And fo...'
---

By Siddharth Kshetrapal

I love npm and believe that this package manager is the single biggest reason for JavaScript’s massive success these past few years.

There was a lot of excitement in the JavaScript community when facebook released yarn. And for good reason. Yarn’s install speeds are amazing. Subsequent installs are even faster because yarn caches installed modules on your machine.

![Image](https://cdn-media-1.freecodecamp.org/images/yAAqrLfduWDgBuRqnlh1xqu7qRiTzMXUjr7f)
_Install speeds @ 12Mbps. Yarn = ?_

But there’s an npm feature that does not get nearly the attention it deserves.

Like Yarn, npm also has a built-in caching mechanism that can make subsequent installs super fast.

Here are some benchmarks:

![Image](https://cdn-media-1.freecodecamp.org/images/oXzMHJNK8dsZwCEAxu2u47WZQwTWOE6MAL08)
_npm + cache is as fast as yarn + cache (if not faster)_

That’s crazy, right? And guess what: this feature has been available to you this whole time, but it’s disabled by default.

### How to enable npm cache

```
npm config set cache-min 9999999
```

That’s it.

Now install your packages as usual:

```
npm install express
```

You can try out these benchmarks for yourself using [this repository](https://github.com/siddharthkp/npm-cache-benchmark):

[**siddharthkp/npm-cache-benchmark**](https://github.com/siddharthkp/npm-cache-benchmark)  
[_npm-cache-benchmark - Benchmark npm cache vs yarn_github.com](https://github.com/siddharthkp/npm-cache-benchmark)

Note that Yarn is not just about speed — it has [other features](https://yarnpkg.com/blog/2016/10/11/introducing-yarn) like consistent installs, which set it apart.

But, if speed is an important consideration for you — as it sure is for me — you should give npm another try, this time with cache.

Thanks to [ashley williams](https://www.freecodecamp.org/news/npm-cache-the-unsung-hero-11e646c09791/undefined) for reviewing this and to [npm,](https://www.freecodecamp.org/news/npm-cache-the-unsung-hero-11e646c09791/undefined) for being awesome.

P.S. You should totally [follow me on twitter](https://twitter.com/siddharthkp).

