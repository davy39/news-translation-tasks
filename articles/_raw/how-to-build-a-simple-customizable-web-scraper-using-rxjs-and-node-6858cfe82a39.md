---
title: How to build a simple & customizable web scraper using RxJS and Node
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-27T02:10:34.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-simple-customizable-web-scraper-using-rxjs-and-node-6858cfe82a39
coverImage: https://cdn-media-1.freecodecamp.org/images/0*zqqImyUXrCGM9nA-.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: RxJS
  slug: rxjs
- name: 'tech '
  slug: tech
- name: web scraping
  slug: web-scraping
seo_title: null
seo_desc: 'By Jacob Goh

  Introduction

  After getting to know RxJS (thanks to Angular!), I realized that it’s surprisingly
  a good fit for handling web scraping operations.

  I tried it out in a side project and I would like to share my experience with you.
  Hopefully...'
---

By Jacob Goh

### Introduction

After getting to know RxJS (thanks to Angular!), I realized that it’s surprisingly a good fit for handling web scraping operations.

I tried it out in a side project and I would like to share my experience with you. Hopefully, this will open your eyes to how reactive programming can make your life simpler.

The codes can be found on [https://github.com/jacobgoh101/web-scraping-with-rxjs](https://github.com/jacobgoh101/web-scraping-with-rxjs)

### Requirements

* Node
* RxJS and intermediate understanding of it
* [cheerio](https://www.npmjs.com/package/cheerio): it allows you to use jQuery-like syntax to extract information out of HTML code
* [request-promise-native](https://www.npmjs.com/package/request-promise-native): for sending HTTP request

### Hypothetical Goal

Everybody loves a good comedy movie.

Let’s make it our goal to scrape a list of good comedy movies from IMDB.

There are only 3 requirements that the target data needs to fulfill:

* it is a movie (not TV shows, music videos, etc)
* it is a comedy
* it has a rating of 7 or higher

### Get Started

Let’s set our base URL and define a BehaviorSubject `allUrl$` that uses the base URL as the initial value.

(A BehaviorSubject is a [subject](https://www.youtube.com/watch?v=rdK92pf3abs) with an initial value.)

```
const { BehaviorSubject } =  require('rxjs');const  baseUrl  =  `https://imdb.com`;const  allUrl$  =  new  BehaviorSubject(baseUrl);
```

`allUrl$` is going to be the starting point of all crawling operations. Every URL will be passed into `allUrl$` and be processed on later.

#### Making sure that we scrape each URL only once

With the help of [distinct](https://rxjs-dev.firebaseapp.com/api/operators/distinct) operators and [normalize-url](https://www.npmjs.com/package/normalize-url), we can easily make sure that we never scrape the same URL twice.

```
// ...const { map, distinct, filter } =  require('rxjs/operators');const  normalizeUrl  =  require('normalize-url');
```

```
// ...
```

```
const  uniqueUrl$  =  allUrl$.pipe(    // only crawl IMDB url    filter(url  =>  url.includes(baseUrl)),    // normalize url for comparison    map(url  =>  normalizeUrl(url, { removeQueryParameters: ['ref', 'ref_']     })),    // distinct is a RxJS operator that filters out duplicated values    distinct());
```

#### It’s time to start scraping

We are going to make a request to each unique URL and map the content of each URL into another observable.

To do that, we use [mergeMap](https://www.learnrxjs.io/operators/transformation/mergemap.html) to map the result of the request to another observable.

```
const { BehaviorSubject, from } =  require('rxjs');const { map, distinct, filter, mergeMap } = require('rxjs/operators');const rp = require('request-promise-native');const  cheerio  =  require('cheerio');
```

```
//...const urlAndDOM$ = uniqueUrl$.pipe(  mergeMap(url => {    return from(rp(url)).pipe(      // get the cheerio function $      map(html => cheerio.load(html)),      // add URL to the result. It will be used later for crawling      map($ => ({        $,        url      }))    );  }));
```

`urlAndDOM$` will emit an object consisting of 2 properties, which are `$` and `url`. `$` is a Cheerio function where you can use something like `$('div').text()` to extract information out of raw HTML code.

#### Crawl all the URLs

```
const { resolve } =  require('url');//...
```

```
// get all the next crawlable URLsurlAndDOM$.subscribe(({ url, $ }) => {  $('a').each(function(i, elem) {    const href = $(this).attr('href');    if (!href) return;
```

```
// build the absolute url    const absoluteUrl = resolve(url, href);    allUrl$.next(absoluteUrl);  });});
```

In the code above, we scrape all the links inside the page and send them to `allUrl$` to be crawled later.

#### Scrape and save the movies we want!

```
const  fs  =  require('fs');//...
```

```
const isMovie = $ =>  $(`[property='og:type']`).attr('content') === 'video.movie';const isComedy = $ =>  $(`.title_wrapper .subtext`)    .text()    .includes('Comedy');const isHighlyRated = $ => +$(`[itemprop="ratingValue"]`).text() > 7;
```

```
urlAndDOM$  .pipe(    filter(({ $ }) => isMovie($)),    filter(({ $ }) => isComedy($)),    filter(({ $ }) => isHighlyRated($))  )  .subscribe(({ url, $ }) => {    // append the data we want to a file named "comedy.txt"    fs.appendFile('comedy.txt', `${url}, ${$('title').text()}\n`);  });
```

### Yup, we just created a web scraper

In around 70 lines of code, we have created a web scraper that

* automatically crawled URLs without unnecessary duplicates
* automatically scrapes and saves the info we want in a text file

You may see the code up to this point in [https://github.com/jacobgoh101/web-scraping-with-rxjs/blob/86ff05e893dec5f1b39647350cb0f74efe258c86/index.js](https://github.com/jacobgoh101/web-scraping-with-rxjs/blob/86ff05e893dec5f1b39647350cb0f74efe258c86/index.js)

If you have ever tried writing a web scraper from scratch, you should be able to see now how elegant it is to write one with RxJS.

### But we are not done yet…

In an ideal world, the code above should work forever without any problems.

But in reality, silly errors happen.

### Handling Errors

#### Limit the number of active concurrent connections

If we send too many requests to a server in a short period of time, it’s likely that our IP will be temporarily blocked from making any further requests, especially for an established website like IMDB.

It’s also considered **rude/unethical** to send so many requests at once because it would create a heavier load on the server and in some cases, **crash the server**.

[mergeMap](https://www.learnrxjs.io/operators/transformation/mergemap.html) has built-in functionality to control concurrency. Simply add a number to the 3rd function argument and it will limit the active concurrent connection automatically. Graceful!

```
const maxConcurrentReq = 10;//...const urlAndDOM$ = uniqueUrl$.pipe(  mergeMap(    //...    null,    maxConcurrentReq  ));
```

Code Diff: [https://github.com/jacobgoh101/web-scraping-with-rxjs/commit/6aaed6dae230d2dde1493f1b6d78282ce2e8f316](https://github.com/jacobgoh101/web-scraping-with-rxjs/commit/6aaed6dae230d2dde1493f1b6d78282ce2e8f316)

#### Handle and Retry Failed Request

Requests may fail randomly due to dead links or server-side rate limiting. This is crucial for web scrapers.

We can use [catchError](https://www.learnrxjs.io/operators/error_handling/catch.html), [retry](https://www.learnrxjs.io/operators/error_handling/retry.html) operators to handle this.

```
const { BehaviorSubject, from, of } =  require('rxjs');const {  // ...  retry,  catchError} = require('rxjs/operators');//...
```

```
const maxRetries = 5;// ...
```

```
const urlAndDOM$ = uniqueUrl$.pipe(  mergeMap(    url => {      return from(rp(url)).pipe(        retry(maxRetries),        catchError(error => {          const { uri } = error.options;          console.log(`Error requesting ${uri} after ${maxRetries} retries.`);          // return null on error          return of(null);        }),        // filter out errors        filter(v => v),        // ...      );    },
```

Code Diff: [https://github.com/jacobgoh101/web-scraping-with-rxjs/commit/3098b48ca91a59aa5171bc2aa9c17801e769fcbb](https://github.com/jacobgoh101/web-scraping-with-rxjs/commit/3098b48ca91a59aa5171bc2aa9c17801e769fcbb)

#### Improved Retry Failed Request

Using retry operator, the retry would happen immediately after the request failed. This is not ideal.

It’s better to retry after a certain period of delay.

We can use the `genericRetryStrategy` suggested in [learnrxjs](https://www.learnrxjs.io/operators/error_handling/retrywhen.html) to achieve this.

Code Diff: [https://github.com/jacobgoh101/web-scraping-with-rxjs/commit/e194f4ff128a573241055ffc0d1969d54ca8c270](https://github.com/jacobgoh101/web-scraping-with-rxjs/commit/e194f4ff128a573241055ffc0d1969d54ca8c270)

### Conclusion

To recap, in this post, we discussed:

* how to crawl a web page using Cheerio
* how to avoid duplicated crawl using RxJS operators like filter, distinct
* how to use mergeMap to create an observable of request’s response
* how to limit concurrency in mergeMap
* how to handle error
* how to handle retry

I hope this has been helpful to you and has deepened your understanding of RxJs and web scraping.

_Originally published at [dev.to](https://dev.to/jacobgoh101/simple--customizable-web-scraper-using-rxjs-and-node-1on7)._

