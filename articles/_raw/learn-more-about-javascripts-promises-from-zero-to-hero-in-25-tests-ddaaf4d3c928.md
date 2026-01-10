---
title: 'Learn more about JavaScript’s promises: from zero to hero in 25 tests'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-11T23:21:47.000Z'
originalURL: https://freecodecamp.org/news/learn-more-about-javascripts-promises-from-zero-to-hero-in-25-tests-ddaaf4d3c928
coverImage: https://cdn-media-1.freecodecamp.org/images/1*JZlPOGIMUKYlwvBnmPomEg.jpeg
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Andrea Koutifaris

  A test is worth a thousand words… or was it a picture…?

  I think the best way to explain JavaScript promises is through examples. What is
  a good, self contained, and short way to write an example? A test!

  For those who have never ...'
---

By Andrea Koutifaris

A test is worth a thousand words… or was it a picture…?

I think the best way to explain JavaScript promises is through examples. What is a good, self contained, and short way to write an example? A test!

For those who have never seen a Jasmine test suit, `it('...', (done) => {..`.}) is a test a`nd d`one is a function that has to be executed when an asynchronous test is completed.

The rules here are:

* **Each test starts by asserting something in English**. You have to deduce why the test code implies that the assertion of the test is true.
* Some tests have expectations. If the test passes, the expectations are true.
* Other tests rely on the callback `done()` to be called. If `done()` is not called, the test fails.

Each test is in [this JSFiddle](https://jsfiddle.net/kouty79/e52qkkmu/), so feel free to play with it while reading. Especially if you have some doubts about any of the tests, do change the test code and study what happens.

### The tests

Let’s begin with Promise basics:

```
it('Promise executor is run SYNCHRONOUSLY', () => {  let executorRun = false;  new Promise(function executor() {    executorRun = true;  });  expect(executorRun).toBe(true);});it('you can resolve a promise', (done) => {  new Promise((resolve) => setTimeout(resolve, 1))    .then(done);});it('... or you can reject a promise', (done) =&gt; {  new Promise((resolve, reject) => setTimeout(reject, 1))    .then(undefined, done);});it('An error inside the executor, rejects the promise', (done) => {  new Promise(function executor() {    throw 'Error';  }).catch(done);});
```

It seems that when you call `resolve()` , the first `then(...)` callback is run. If you call `reject()` or an error is thrown, `catch()` or the second callback of `then(...)` is run.

Also, **promise executor is run** **synchronously**. This means that promises are a way to handle asynchronous code, not to execute tasks in asynchronous threads. Use [Web Workers](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers) if you want to execute some JavaScript code outside the main thread.

Let’s see more in detail what those `then(...)` and `catch()` functions are, and what “chaining promises” means:

```
// Chaining promises
```

```
it('you can chain promise because .then(...) returns a promise'  , (done) => {  fetch('https://jsonplaceholder.typicode.com/posts/1')    .then(response => response.json())    .then(json => expect(json.userId).toBe(1))    .then(done);});it('you can use the fail callback of .then(success, fail) to ' +  'handle rejected promises', (done) => {  Promise.reject()    .then(function success() {      throw 'I must not be executed';    }, function fail() {      done();    });});it('... or you can use .catch() to handle rejected promises'  , (done) => {  Promise.reject()    .then(function success() {      throw 'I must not be executed';    })    .catch(done);});it('also .catch() returns a promise, allowing promise chaining'  , (done) => {  Promise.reject()    .catch(() => undefined)    .then(done);});it('you must return a rejected promise if you want to ' +  'execute the next fail callback', (done) => {  function someApiCall() {    return Promise.reject('Error');  }  someApiCall()    .catch((err) => {      console.error(err);      // Without the line below, .catch gets not called      return Promise.reject(err);    })    .catch(done);});it('... or you can throw an error if you want to ' +  'execute the next fail callback', (done) => {  function someApiCall() {    return Promise.reject('Error');  }  someApiCall()    .catch((err) => {      console.error(err);      throw err; // Without this line, .catch gets not called    })    .catch(done);});it('values returned inside .then()/.catch() callbacks ' +  'are provided to the next callback', (done) => {  Promise.resolve(1)    .then(value => value + 1)    .then(value => expect(value).toBe(2));  Promise.reject(1)    .catch(value => value + 1)    .then(value => expect(value).toBe(2));  setTimeout(() => {    done();  }, 1);});
```

OK, but what are `Promise.resolve()` and `Promise.reject()` ? Let’s find out!

```
it('you can use Promise.resolve() to wrap values or promises'  , (done) => {  function iMayReturnAPromise() {    return Math.random() >= 0.5 ? Promise.resolve() : 5;  }
```

```
  Promise.resolve(iMayReturnAPromise()).then(done);});
```

```
it('you can use Promise.resolve() to execute something just after'  , (done) => {  let arr = [];  Promise.resolve().then(() => arr.push(2));  arr.push(1);
```

```
  setTimeout(() => {    expect(arr).toEqual([1, 2]);    done();  }, 1);});
```

```
/** @seehttps://jakearchibald.com/2015/tasks-microtasks-queues-and-schedules **/it('Promise.resolve() is normally executed before setTimeout(.., 0)'  , (done) => {  let arr = [];  setTimeout(() => arr.push('timeOut'), 0);  Promise.resolve().then(() => {    arr.push('resolve');  });
```

```
  setTimeout(() => {    expect(arr).toEqual(['resolve', 'timeOut']);    done();  }, 1);});
```

```
it('you can create rejected promises', (done) => {  Promise.reject('reason').catch(done);});
```

```
it('pay attention to "Uncaught (in promise) ..."', () => {  Promise.reject('The error');  // Outputs in the console Uncaught (in promise) The error});
```

#### Chaining promises vs. creating new ones

Although `new Promise(...)` is a way to create a promise, you should avoid using it. Most of the time, functions/libraries return a promise, so you should chain promises and not create new ones:

```
it("Don't use new Promise(...), prefer chaining", (done) => {  const url = 'https://jsonplaceholder.typicode.com/posts/1';  function badlyDesignedCustomFetch() {    return new Promise((resolve, reject) => {      fetch(url).then((response) => {        if (response.ok) {          resolve(response);        } else {          reject('Fetch failed');        }      });    });  }  function wellDesignedCustomFetch() {    return fetch(url).then((response) =>; {      if (!response.ok) {        return Promise.reject('Fetch failed');      }      return (response);    });  }  Promise.all([    badlyDesignedCustomFetch(),    wellDesignedCustomFetch()  ]).then(done);});
```

But, when should you use `new Promise(...)` ? When you want to move from a callback interface to a Promise one. See below:

```
function imgOnLoad(img) {  return new Promise((resolve, reject) => {    img.onload = resolve;    img.onerror = reject;  });}
```

#### Parallel execution

Promise chaining is nice, but what about executing asynchronous operations in parallel? Below is all you need to know:

```
// Parallel execution of promises
```

```
it('you can use Promise.all([...]) to execute promises in parallel'  , (done) => {  const url = 'https://jsonplaceholder.typicode.com/posts';  const p1 = fetch(`${url}/1`);  const p2 = fetch(`${url}/2`);  Promise.all([p1, p2])    .then(([res1, res2]) => {      return Promise.all([res1.json(), res2.json()])    })    .then(([post1, post2]) => {      expect(post1.id).toBe(1);      expect(post2.id).toBe(2);    })    .then(done);});it('Promise.all([...]) will fail if any of the promises fails'  , (done) =&gt; {  const p1 = Promise.resolve(1);  const p2 = Promise.reject('Error');  Promise.all([p1, p2])    .then(() => {      fail('I will not be executed')    })    .catch(done);});it("if you don't want Promise.all() to fail, wrap the promises " +  "in a promise that will not fail", (done) => {  function iMayFail(val) {    return Math.random() >= 0.5 ?      Promise.resolve(val) :      Promise.reject(val);  }  function promiseOr(p, value) {    return p.then(res => res, () => value);  }  const p1 = iMayFail(10);  const p2 = iMayFail(9);  Promise.all([promiseOr(p1, null), promiseOr(p2, null)])    .then(([val1, val2]) => {      expect(val1 === 10 || val1 === null).toBe(true);      expect(val2 === 9 || val2 === null).toBe(true);    })    .catch(() => {      fail('I will not be executed')    })    .then(done);});it('Promise.race([...]) will resolve as soon as ' +  'one of the promises resolves o rejects', (done) => {  const timeout =    new Promise((resolve, reject) => setTimeout(reject, 100));  const data =    fetch('https://jsonplaceholder.typicode.com/posts/1');  Promise.race([data, timeout])    .then(() => console.log('Fetch OK'))    .catch(() => console.log('Fetch timeout'))    .then(done);});
```

#### Syntax

Promise syntax is a bit complex compared to the typical syntax of synchronous code. It is true that by chaining promises, the code keeps good readability, but it could be better. The new **await/async syntax** makes using promises as easy as writing synchronous code.

```
// New await/async syntax
```

```
it('you can use the new await/async syntax', async () => {  function timeout(ms) {    return new Promise((resolve) => setTimeout(resolve, ms));  }  const start = Date.now();  const delay = 200;  await timeout(delay + 2); // Just some ms tolerance  expect(Date.now() - start).toBeGreaterThanOrEqual(delay);});it('an async function returns a promise', (done) => {  async function iAmAsync() {    return 1;  }  iAmAsync()    .then((val) => expect(val).toBe(1))    .then(done);});it('await just awaits a promise resolution', async (done) => {  await Promise.resolve();  done();});it('await will throw an error if the promise fail', async(done) =&gt; {  try {    await Promise.reject();    fail('I will not be executed');  } catch (err) {    done();  }});
```

#### Synchronous functions

On last consideration: when you design a function, you have to decide whether it is synchronous or not. Don’t return a promise just because “you never know”. Use “normal” synchronous functions when possible.

All the tests are [here](https://jsfiddle.net/kouty79/e52qkkmu/), on JSFiddle.

That’s all! Hope you enjoyed this article.

