---
title: 'CSP vs RxJS: what you don’t know.'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-04T17:18:15.000Z'
originalURL: https://freecodecamp.org/news/csp-vs-rxjs-what-you-dont-know-1542cd5dd100
coverImage: https://cdn-media-1.freecodecamp.org/images/0*ColTdidsgUyGVesk
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: RxJS
  slug: rxjs
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Kevin Ghadyani

  What happened to CSP?


  _Photo by [Unsplash](https://unsplash.com/@lamppidotco?utm_source=medium&utm_medium=referral"
  rel="noopener" target="_blank" title="">James Pond on <a href="https://unsplash.com?utm_source=medium&utm_medium=re...'
---

By Kevin Ghadyani

#### What happened to CSP?

![Image](https://cdn-media-1.freecodecamp.org/images/0*ColTdidsgUyGVesk)
_Photo by [Unsplash](https://unsplash.com/@lamppidotco?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">James Pond</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

You probably clicked this article thinking “what is CSP?” It’s **communicating sequential processes**. Still baffled?

CSP is a method of communicating between different functions (generators) in your code using a shared channel.

What in the world does that mean? Lemme tell it to ya straight. There’s this concept of a channel. Think of it like a queue. You can put stuff on it and take stuff off it.

So with two functions, you can have one adding stuff on the channel (producer) and another pulling things off and doing some work (consumer).

A typical advanced use case would be multiple producers and one consumer. That way you can control the data you’re getting, but you can have multiple things giving it to you.

Unlike RxJS, these channels are automatic. You don’t get values willy-nilly, you have to ask for them.

### Using CSP

Here’s a small CSP example using the super simple (and dead) library [Channel4](https://www.npmjs.com/package/channel4):

CSP channels run asynchronously. So as soon as this runs, the synchronous “DONE” message gets logged first. Then our channel takers are executed in order.

The most-interesting thing to me is the blocking (but async) nature of CSP. Notice how we created the third `take` before putting “C” on the channel. Unlike the first two `take` functions, the third one doesn’t have anything to take. Once something comes into the channel, it immediately takes it.

Also note, consumers need to be constantly taking things off the channel until that channel closes. That’s why “D” is never logged. You need to define another `take` to grab the next value off the channel.

With observables, you’re given values so you don’t have to worry about manually pulling them off. If you want to buffer those values, RxJS provides quite a few pipeline methods for that very purpose. No need to use CSP.

The entire concept behind observables is that every listeners gets the same data as soon as the observer calls `next`. With CSP, it’s like the IxJS approach where you’re dealing with data in chunks.

### CSP IS DEAD!?

You can find CSP implementations in [Go](https://godoc.org/github.com/thomas11/csp) and [Closure](https://github.com/clojure/core.async). In JavaScript, all but a couple CSP libraries are dead and even then, their audience is small ?.

I found out about CSP from [Vincenzo Chianese’s awesome talk](https://www.youtube.com/watch?v=r7yWWxdP_nc). He recommended this high-end library called [js-csp](https://github.com/ubolonton/js-csp). Sadly, it’s no longer maintained.

Based on what he said in his 2017 talk, it seemed like a big deal. He talked about how transducers were going to to explode in a few months and how js-csp already had support for them.

It looked like CSP could fundamentally change how you developed async applications in JavaScript. But none of that ever happened. Transducers died away; replaced by libraries like RxJS, and the hype around CSP dissolved.

Vincenzo did note how CSP is a whole ‘nother level above promises. He’s right. The power you get having multiple functions interacting asynchronously is incredible.

Promises, by their eager nature, aren’t even in the same ballpark. Little did he know the last few CSP libraries would end up supporting promises under-the-hood ?.

### CSP Alternative: Redux-Saga

If you’ve ever used Redux-Saga, the ideas and concepts around CSP probably sound familiar. That’s because they are. In fact, Redux-Saga is an implementation of CSP in JavaScript; the most popular by far.

There’s even a concept of “channels” in Redux-Sagas:  
[https://github.com/redux-saga/redux-saga/blob/master/docs/advanced/Channels.md](https://github.com/redux-saga/redux-saga/blob/master/docs/advanced/Channels.md)

Channels receive information from external events, buffer actions to the Redux store, and communicate between two sagas. It’s the same way they’re used in CSP with the same `take` and `put` functions.

Pretty cool to see an actual implementation of CSP in JavaScript, but strange very few have noticed it. That shows you how little CSP took off before dying.

### CSP Alternative: Redux-Observable

You might’ve heard of something called Redux-Observable. This is a similar concept to CSP and Redux-Saga, but instead of the imperative style of generators, it takes a functional approach and utilizes RxJS pipelines referred to as “epics”.

In Redux-Observable, everything happens through two subjects: `action$` and `state$`. Those are your channels.

Instead of manually taking and putting, you’re listening for specific actions as a consumer of an action or state channel. Each epic has the ability of also being a producer by sending actions through the pipeline.

If you want to build a queue in Redux-Observable just like CSP, it’s a little more complicated as there’s no operator available for this purpose, but it’s entirely possible.

I created a repl that does just that:

Compared to our earlier CSP example, this is what you can expect to see:

The example only requires RxJS and everything is in a single file for simplicity. As you can see, it’s a lot harder to queue up items in RxJS the same way you might with CSP. It’s entirely possible, but requires a lot more code.

Personally, I’d love to see RxJS add an operator like `bufferWhen` that allows you to divvy out individual items instead of the entire buffer. Then you could accomplish the CSP-style in Redux-Observable a lot easier.

### Conclusion

CSP was a cool concept, but it’s dead in JavaScript. Redux-Saga and Redux-Observable are worthy alternatives.

Even with the ability to integrate with transducer libraries, RxJS still has a clear leg-up. It’s massive community of educators and production applications makes it hard to compete.

That’s why I think CSP died in JavaScript.

### More Reads

If you liked what you read, please checkout my other articles on similar eye-opening topics:

* [Redux-Observable Can Solve Your State Problems](https://medium.com/@Sawtaytoes/redux-observable-can-solve-your-state-problems-15b23a9649d7)
* [Redux-Observable without Redux](https://itnext.io/redux-observable-without-redux-ff4a2b5a4b39)
* [Callbacks: The Definitive Guide](https://itnext.io/the-definitive-guide-to-callbacks-in-javascript-44a39c065292)
* [Promises: The Definitive Guide](https://itnext.io/promises-the-definitive-guide-6a49e0dbf3b7)

