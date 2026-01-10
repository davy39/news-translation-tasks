---
title: The real difference between catch vs onRejected
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-24T22:08:33.000Z'
originalURL: https://freecodecamp.org/news/the-real-difference-between-catch-vs-onrejected-15cab8978e92
coverImage: https://cdn-media-1.freecodecamp.org/images/1*JLtSGRqnw1wIR-o3LPziwA.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: promises
  slug: promises
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Max Belsky

  Most popular articles describe the difference between catch and onRejected in a
  code snippet like this:

  const getPromise = () => new Promise((resolve, reject) => {  Math.round(Math.random())
  ?     resolve(''resolve #1'') :     reject(''rej...'
---

By Max Belsky

Most popular articles describe the difference between catch and onRejected in a code snippet like this:

```
const getPromise = () => new Promise((resolve, reject) => {  Math.round(Math.random()) ?     resolve('resolve #1') :     reject('reject #1')})
```

```
getPromise().then(result => {  throw new Error('reject #2')}, error => {  // Handles only 'reject #1'})
```

```
getPromise().then(result => {  throw new Error('reject #2')})  .catch(error => {    // Handles both 'reject #1',     // and 'reject #2'  }))
```

onRejected never handles rejected promises from the same `.then(onFulfilled)` callback and `.catch` takes both. However besides the behavior difference, there is one more nuance. It’s about how these ways will be translated to [microtasks](https://jakearchibald.com/2015/tasks-microtasks-queues-and-schedules/) and how they will be queued.  
Let’s see an example of the difference.

#### Promise.race

There is a task — write `Promise.race` polyfill. We use a common pattern in both functions to handle `resolved` promises and different tools to handle `rejected` promises.

```
const promiseRaceOnRejected = (promises = []) => {  return new Promise((resolve, reject) => {    promises.forEach(promise => {      promise.then(        result => resolve(result),        error => reject(error)      )    })  })}
```

```
const promiseRaceCatch = (promises = []) => {  return new Promise((resolve, reject) => {    promises.forEach(promise => {      promise.then(result => resolve(result))        .catch(error => reject(error))    })  })}
```

Try some tests to be sure that both solutions work well:

```
// A helper function to create a delayed promiseconst getPromise = (resolveMs, rejectMs) => {  return new Promise((resolve, reject) => {    if ('number' === typeof rejectMs) {      setTimeout(() => reject(rejectMs), rejectMs)    }
```

```
    if ('number' === typeof resolveMs) {      setTimeout(() => resolve(resolveMs), resolveMs)    }  })}
```

```
const testRaces = async () => {  const r1 = await promiseRaceOnRejected([    getPromise(0),     getPromise(5)  ])  // 0
```

```
const r2 = await promiseRaceCatch([    getPromise(0),     getPromise(5)  ])  // 0
```

```
const r3 = await promiseRaceOnRejected([    getPromise(5),     getPromise(null, 2)  ])    .catch(e => e)  // 2
```

```
const r4 = await promiseRaceCatch([    getPromise(5),     getPromise(null, 2)  ])    .catch(e => e)  // 2}
```

```
testRaces()
```

As you can see, both polyfills work as expected. Arguments order and `rejected` promises handler variation don’t matter. Until we try it with the next set of tests:

```
const r5 = await promiseRaceOnRejected([    Promise.resolve('Resolve'),     Promise.reject('Reject')  ])  // Resolve
```

```
const r6 = await promiseRaceCatch([    Promise.resolve('Resolve'),     Promise.reject('Reject')  ])  // Resolve
```

```
const r7 = await promiseRaceOnRejected([    Promise.reject('Reject'),     Promise.resolve('Resolve')  ])    .catch(e => e)  // Reject
```

```
const r8 = await promiseRaceCatch([    Promise.reject('Reject'),     Promise.resolve('Resolve')  ])    .catch(e => e)  // ???
```

The fifth, sixth and seventh races return expected values. What about the eighth? Instead of `Reject` it returns `Resolve` and it is not a bug.

#### Microtasks queue

Depending on the job’s result, a pending promise changes its state to `resolved` or `rejected`. JS environment puts that promise in a microtasks queue. Like it described in ECMA 2015 [specification](http://www.ecma-international.org/ecma-262/6.0/#sec-jobs-and-job-queues), this queue works by the [FIFO](https://en.wikipedia.org/wiki/FIFO_(computing_and_electronics)) principle — first in, first out. Base on this, let’s review the eighth race’s case.

![Image](https://cdn-media-1.freecodecamp.org/images/uFX52cgzB6WwzZeyDMGbhZwt40hV6C8k-uWa)
_Queue’s first tick_

At the start of the race, we already have two queued promises, and the rejected is first. `.then` without a second argument cannot handle a rejected promise, so it puts the promise back into the queue. And instead of handling this promise with `.catch`, the JS environment switches to `p2` because it has higher priorities in the queue.

![Image](https://cdn-media-1.freecodecamp.org/images/-ZAASKNuYIOZwBQBwd7XpBdvYecTiE2n0ZWF)
_Queue’s second tick_

On next tick `.then` handles `p2` and the race ends with `Resolve` result.

Next time when you’re choosing between the catch and onRejected handlers, remember not only which rejected promises they catch, but about the queuing difference too!

