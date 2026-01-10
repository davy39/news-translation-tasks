---
title: 3 JavaScript questions to watch out for during coding interviews
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-03T20:25:17.000Z'
originalURL: https://freecodecamp.org/news/3-questions-to-watch-out-for-in-a-javascript-interview-725012834ccb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*pTg8YVc-Hdps3vGURqJGDQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: learning to code
  slug: learning-to-code
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Daniel Borowski

  JavaScript is the official language of all modern web browsers. As such, JavaScript
  questions come up in all sorts of developer interviews.

  This article isn’t about the newest JavaScript libraries, common development practices,
  or ...'
---

By Daniel Borowski

JavaScript is the official language of [all modern web browsers](https://developer.mozilla.org/en-US/docs/Web/JavaScript). As such, JavaScript questions come up in all sorts of developer interviews.

This article isn’t about the newest JavaScript libraries, common development practices, or any of the new [ES6 functions](https://hackernoon.com/es6-features-you-need-to-know-now-b525e2b0755e#.seo0weyr4). Rather, it’s about 3 things that usually come up in interviews when discussing JavaScript. I myself have been asked these questions, and my friends have told me they’ve been asked them, too.

Of course these aren’t the only 3 things you should study before a JavaScript interview — there are a [multitude](http://jstherightway.org/#getting-started) of [ways](https://medium.com/javascript-scene/10-interview-questions-every-javascript-developer-should-know-6fa6bdf5ad95#.7fty5p61c) you [can](http://www.thatjsdude.com/interview/js2.html) better prepare for an upcoming interview — but below are 3 questions an interviewer may ask to judge how well you know and understand the JavaScript language and the [DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction).

So let’s get started! Note that we’re going to use vanilla JavaScript in the examples below, since your interviewer will usually want to see how well you understand JavaScript and the DOM without the help of libraries like jQuery.

### Question #1: Event delegation

When building an application, sometimes you’ll need to attach event listeners to buttons, text, or images on the page in order to perform some action when the user interacts with the element.

If we take a simple todo list as an example, the interviewer may tell you that they want an action to occur when a user clicks one of the list items. And they want you to implement this functionality in JavaScript assuming the following HTML code:

```html
<ul id="todo-app">
  <li class="item">Walk the dog</li>
  <li class="item">Pay bills</li>
  <li class="item">Make dinner</li>
  <li class="item">Code for one hour</li>
</ul>
```

You may want to do something like the following to attach event listeners to the elements:

```js
document.addEventListener('DOMContentLoaded', function() {
  
  let app = document.getElementById('todo-app');
  let items = app.getElementsByClassName('item');
  
  // attach event listener to each item
  for (let item of items) {
    item.addEventListener('click', function() {
      alert('you clicked on item: ' + item.innerHTML);
    });
  }
  
});
```

While this does technically work, the problem is that you’re attaching an event listener to every single item individually. This is fine for 4 elements, but what if someone adds 10,000 items (they may have a lot of things to do) to their todo list? Then your function will create 10,000 separate event listeners and attach each of them to the DOM. This isn’t very [efficient](https://www.kirupa.com/html5/handling_events_for_many_elements.htm).

In an interview it would be best to first ask the interviewer what the maximum number of elements the user can enter is. If it can never be more than 10, for example, then the above code would work fine. But if there’s no limit to the number of items the user can enter, then you’d want to use a more efficient solution.

If your application could end up with hundreds of event listeners, the more efficient solution would be to actually attach **one** event listener to the whole container, and then be able to access each item when it’s actually clicked. This is called [event delegation](https://davidwalsh.name/event-delegate), and it’s much more efficient than attaching separate event handlers.

Here’s the code for event delegation:

```js
document.addEventListener('DOMContentLoaded', function() {
  
  let app = document.getElementById('todo-app');
  
  // attach event listener to whole container
  app.addEventListener('click', function(e) {
    if (e.target && e.target.nodeName === 'LI') {
      let item = e.target;
      alert('you clicked on item: ' + item.innerHTML);
    }
  });
  
});
```

### Question #2: Using a closure within a loop

Closures are sometimes brought up in an interview so that the interviewer can gauge how familiar you are with the language, and whether you know when to implement a closure.

A closure is basically when an [inner function has access](https://medium.com/javascript-scene/master-the-javascript-interview-what-is-a-closure-b2f0d2152b36#.44xk49tyt) to variables outside of its scope. Closures can be used for things like [implementing privacy](https://medium.com/written-in-code/practical-uses-for-closures-c65640ae7304#.70gp35hbn) and creating [function factories](https://medium.com/javascript-scene/javascript-factory-functions-vs-constructor-functions-vs-classes-2f22ceddf33e#.1817w0lmb). A common interview question regarding the use of closures is something like this:

_Write a function that will loop through a list of integers and print the index of each element after a 3 second delay._

A common (incorrect) implementation I’ve seen for this problem looks something like this:

```js
const arr = [10, 12, 15, 21];
for (var i = 0; i < arr.length; i++) {
  setTimeout(function() {
    console.log('The index of this number is: ' + i);
  }, 3000);
}
```

If you run this you’ll see that you actually get the **4** printed out every time instead of the expected **0, 1, 2, 3** after a 3 second delay.

To correctly identify why this is happening it would be useful to have an understanding of why this happens in JavaScript, which is exactly what the interviewer is trying to test.

The reason for this is because the `setTimeout` function creates a function (the closure) that has access to its outer scope, which is the loop that contains the index `i`. After 3 seconds go by, the function is executed and it prints out the value of `i`, which at the end of the loop is at 4 because it cycles through 0, 1, 2, 3, 4 and the loop finally stops at 4.

There are actually [a few ways](http://stackoverflow.com/questions/3572480/please-explain-the-use-of-javascript-closures-in-loops) of [correctly writing](https://coderbyte.com/algorithm/3-common-javascript-closure-questions) the function for this problem. Here are two of them:

```js
const arr = [10, 12, 15, 21];
for (var i = 0; i < arr.length; i++) {
  // pass in the variable i so that each function 
  // has access to the correct index
  setTimeout(function(i_local) {
    return function() {
      console.log('The index of this number is: ' + i_local);
    }
  }(i), 3000);
}
```

```js
const arr = [10, 12, 15, 21];
for (let i = 0; i < arr.length; i++) {
  // using the ES6 let syntax, it creates a new binding
  // every single time the function is called
  // read more here: http://exploringjs.com/es6/ch_variables.html#sec_let-const-loop-heads
  setTimeout(function() {
    console.log('The index of this number is: ' + i);
  }, 3000);
}
```

### Question #3: Debouncing

There are some browser events that can fire many times within a short timespan very quickly, such as resizing a window or scrolling down a page. If you attach an event listener to the window scroll event for example, and the user continuously scrolls down the page very quickly, your event may fire thousands of times within the span of 3 seconds. This can cause some serious performance issues.

If you’re discussing building an application in an interview, and events like scrolling, window resizing, or key pressing come up, make sure to mention debouncing and/or throttling as a way to improve page speed and performance. A real example taken from this [guest post on css-tricks](https://css-tricks.com/debouncing-throttling-explained-examples/):

> In 2011, an issue popped up on the Twitter website: when you were scrolling down your Twitter feed, it became slow and unresponsive. John Resig published [a blog post about the problem](http://ejohn.org/blog/learning-from-twitter) where it was explained how bad of an idea it is to directly attach expensive functions to the `scroll` event.

Debouncing is one way to solve this issue by limiting the time that needs to pass by until a function is called again. A correct implementation of debouncing would therefore _group_ several function calls into one and execute it only once after some time has elapsed. Here’s an implementation in plain JavaScript that makes use of topics such as [scope](https://toddmotto.com/everything-you-wanted-to-know-about-javascript-scope/), closures, [this](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this), and [timing events](http://www.w3schools.com/jsref/met_win_settimeout.asp):

```js
// debounce function that will wrap our event
function debounce(fn, delay) {
  // maintain a timer
  let timer = null;
  // closure function that has access to timer
  return function() {
    // get the scope and parameters of the function 
    // via 'this' and 'arguments'
    let context = this;
    let args = arguments;
    // if event is called, clear the timer and start over
    clearTimeout(timer);
    timer = setTimeout(function() {
      fn.apply(context, args);
    }, delay);
  }
}
```

This function — when wrapped around an event — will execute only after a certain amount of time has elapsed.

You would use this function like so:

```js
// function to be called when user scrolls
function foo() {
  console.log('You are scrolling!');
}

// wrap our function in a debounce to fire once 2 seconds have gone by
let elem = document.getElementById('container');
elem.addEventListener('scroll', debounce(foo, 2000));
```

Throttling is another technique that’s is similar to debouncing, except that instead of waiting for some time to pass by before calling a function, throttling just spreads the function calls across a longer time interval. So if an event occurs 10 times within 100 milliseconds, throttling could spread out each of the function calls to be executed once every 2 seconds instead of all firing within 100 milliseconds.

For more information on debouncing and throttling, the following articles and tutorials may be helpful:

* [Throttling and Debouncing in JavaScript](https://medium.com/@_jh3y/throttling-and-debouncing-in-javascript-b01cad5c8edf#.ly8uqz8v4)
* [The Difference Between Throttling and Debouncing](https://css-tricks.com/the-difference-between-throttling-and-debouncing/)
* [Examples of Throttling and Debouncing](https://css-tricks.com/debouncing-throttling-explained-examples/)
* [Remy Sharp’s blog post on Throttling function calls](https://remysharp.com/2010/07/21/throttling-function-calls)

If you enjoyed reading this article, then you may like reading the JavaScript tutorials and solving some of the JavaScript coding challenges that I host on [Coderbyte](https://www.coderbyte.com). I’d love to hear what you think!

