---
title: Here are a few function decorators you can write from scratch
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-03T09:56:39.000Z'
originalURL: https://freecodecamp.org/news/here-are-a-few-function-decorators-you-can-write-from-scratch-488549fe8f86
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Qw0e4LC2Fri7dFkBY0N1cA.jpeg
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Cristian Salcescu

  Discover Functional JavaScript was named one of the best new Functional Programming
  books by BookAuthority!


  A function decorator is a higher-order function that takes one function as an argument
  and returns another function, and...'
---

By Cristian Salcescu

[**Discover Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE) was named one of the [**best new Functional Programming books by BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781)**!**

> A **function decorator** is a higher-order function that takes one function as an argument and returns another function, and the returned function is a variation of the argument function — [Javascript Allongé](https://leanpub.com/javascript-allonge/read#decorators)

Let’s write some common function decorators found in libraries like [underscore.js](http://underscorejs.org/#functions), [lodash.js](https://lodash.com/docs/4.17.5) or [ramda.js](http://ramdajs.com/docs/).

### once()

* [once(fn)](https://jsfiddle.net/cristi_salcescu/zpLeLp0v/): creates a version of the function that executes only once. It’s useful for an initialization function, where we want to make sure it runs only once, no matter how many times it is called from different places.

```
function once(fn){
  let returnValue;
  let canRun = true;
  return function runOnce(){
      if(canRun) {
          returnValue = fn.apply(this, arguments);
          canRun = false;
      }
      return returnValue;
  }
}

var processonce = once(process);
processonce(); //process
processonce(); //
```

`once()` is a function that returns another function. The returned function `runOnce()` is a [closure](https://medium.freecodecamp.org/why-you-should-give-the-closure-function-another-chance-31253e44cfa0). It’s also important to note how the original function was called — by passing in the current value of `this` and all the `arguments` : `fn.apply(this, arguments)` .

> If you want to understand closures better, take a look at [Why you should give the Closure function another chance](https://medium.freecodecamp.org/why-you-should-give-the-closure-function-another-chance-31253e44cfa0).

### after()

* [after(count, fn)](https://jsfiddle.net/cristi_salcescu/4evuoxe6/): creates a version of the function that executes only after a number of calls. It’s useful, for example, when we want to make sure the function runs only after all the asynchronous tasks have finished.

```
function after(count, fn){
   let runCount = 0;
   return function runAfter(){
      runCount = runCount + 1;
      if (runCount >= count) {
         return fn.apply(this, arguments);        
      }
   }
}

function logResult() { console.log("calls have finished"); }

let logResultAfter2Calls = after(2, logResult);
setTimeout(function logFirstCall() { 
      console.log("1st call has finished"); 
      logResultAfter2Calls(); 
}, 3000);

setTimeout(function logSecondCall() { 
      console.log("2nd call has finished"); 
      logResultAfter2Calls(); 
}, 4000);
```

Note how I’m using `after()` to build a new function `logResultAfter2Calls()` that will execute the original code of `logResult()` only after the second call.

### throttle()

* [throttle(fn, wait)](https://jsfiddle.net/cristi_salcescu/5tdv0eq6/): creates a version of the function that, when invoked repeatedly, will call the original function once per every `wait` milliseconds. It’s useful for limiting events that occur faster.

```
function throttle(fn, interval) {
    let lastTime;
    return function throttled() {
        let timeSinceLastExecution = Date.now() - lastTime;
        if(!lastTime || (timeSinceLastExecution >= interval)) {
            fn.apply(this, arguments);
            lastTime = Date.now();
        }
    };
}

let throttledProcess = throttle(process, 1000);
$(window).mousemove(throttledProcess);
```

In this example, moving the mouse will generate a lot of `mousemove` events, but the call of the original function `process()` will just happen once per second.

[**Discover Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE&source=post_page---------------------------) was named one of the [**best new Functional Programming books by BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781&source=post_page---------------------------)**!**

**For more on applying functional programming techniques in React take a look at** [**Functional React**](https://read.amazon.com/kp/embed?asin=B07S1NLFTS&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_Pko5CbA30383Y)**.**

Learn **functional React**, in a project-based way, with [**Functional Architecture with React and Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2)**.**

