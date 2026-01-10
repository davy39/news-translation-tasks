---
title: 'You Might Not Know JS: Insights From the JavaScript Bible'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-06T22:18:58.000Z'
originalURL: https://freecodecamp.org/news/you-might-not-know-js-insights-from-the-javascript-bible-2ee9518302aa
coverImage: https://cdn-media-1.freecodecamp.org/images/1*N8GoVaCrqVPJWv4H15RdCw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Jérémy Bardon

  Did you use some JavaScript to make your web app dynamic? That’s the common usage
  for this language, but there is far more waiting for you.

  After reading the popular book series You Don’t Know JS by Kyle Simpson, I realised
  I didn’t ...'
---

By Jérémy Bardon

Did you use some JavaScript to make your web app dynamic? That’s the common usage for this language, but there is far more waiting for you.

After reading the popular book series [You Don’t Know JS](https://github.com/getify/You-Dont-Know-JS) by [Kyle](https://www.freecodecamp.org/news/you-might-not-know-js-insights-from-the-javascript-bible-2ee9518302aa/undefined) Simpson, I realised I didn’t know JS before. The JavaScript community considers this series as one of the references for the language. It’s thick but complete. This series is an invaluable (and free) ally to help you sharpen your skills.

![Image](https://cdn-media-1.freecodecamp.org/images/1*6YTkvM9Y-gcw5F6qyA3ngQ.png)
_You Don’t Know JS (book series)_

In this article, I gathered the most important insights out of it for you. From the simple stuff to the tough (this keyword and promises). I didn’t quote the book but preferred to build my own examples. Consider this as an introduction to the book series.

If you learned JavaScript at school like me, I bet you learned Java first. Be careful, learning JavaScript isn’t about mimicing Java. It doesn’t work like that — you must learn it as new language.

### LESSON #1 — Logical operators

In many languages, expressions which implement logical operators such as **AND** and **OR** return a boolean value. Instead, JavaScript returns one of the two operands as explained in this [ECMAScript specification note](https://tc39.github.io/ecma262/#sec-binary-logical-operators).

![Image](https://cdn-media-1.freecodecamp.org/images/1*ihA6bgwRrlMZWxJ8Ghy2mg.png)

With both operators, it returns the first operand which stops the evaluation. Give it a try by setting `foo` or `bar` to the `false` boolean value. Also, if you don’t include any parenthesis, the **AND** operator has priority over **OR**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*BDscE-3cbvZq3xQnbWI_fA.png)

It first evaluates `foo && foo.bar` as if it’s between parenthesis. You can say **AND** has precedence over **OR**.

Given that the **OR** operator returns the first operand which fulfills it, you can use it to set a default value for empty or not defined variables. It was the preferred way to define [default function parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters) before ES6.

![Image](https://cdn-media-1.freecodecamp.org/images/1*0xc6klIypF2zQkJ0dIM3Xw.png)

Another use case for those logical operators is to avoid `if-else` blocks and ternary expressions:

![Image](https://cdn-media-1.freecodecamp.org/images/1*oISc-T9mbTwvdpiom0XyFg.png)

Here are equivalencies for ternary expressions:

* `a || b` is equivalent to `a ? a : b`
* `a && b` is equivalent to `a ? b : a`

### LESSON #2 — Type conversion

Besides functions such as `valueOf`, JavaScript provides for [type conversion](https://en.wikipedia.org/wiki/Type_conversion). It exists as aother way to convert variables types.

* **Cast** occurs at compilation time and uses the explicit cast operator
* **Coercion** occurs at runtime and often with an implicit syntax

![Image](https://cdn-media-1.freecodecamp.org/images/1*lhxK9yCOl3iB-C8kncEkGg.png)

Implicit coercion is the harder type of conversion to see, so developers often avoid using them. Yet, it’s good to know some common implicit coercions. Here are examples for `String` and `Boolean`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*pOJHWmz4DX0PMqB0M-ZSxQ.png)

Another useful but rarely used operator is `~`, an equivalent to the `-(x+1)` operation. It’s helpful to detect the common [**sentinel value**](https://en.wikipedia.org/wiki/Sentinel_value) `-1`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*MFNIbPhb06Kd507UGSd0vg.png)

### LESSON #3 — Falsy values

Conditions are one of the basic structures in programming and we use them a lot. By the way, the legend says artificial intelligence programs are full of `if`. It’s important to know how it behaves in any programming language.

Values given to a condition are either considered **falsy** or **truthy**. [The ECMAScript specification](https://tc39.github.io/ecma262/#table-10) comes with a curated list of falsy values:

* `'’` empty string
* `undefined`
* `null`
* `false` boolean value
* `0` number value
* `-0` number value
* `NaN` not a number value

Experiment yourself with the following snippet:

![Image](https://cdn-media-1.freecodecamp.org/images/1*P77vOjTLIb-u1UgVnYK7Wg.png)
_Test if a value is truthy or falsy_

Any other value not in the list is truthy. For instance, be careful about `{}` (empty literal object), `[]` (empty array) and `'false'` (false string) which all are `true`.

Combined with logical operators, you can call a function only if a value is truthy without using a `if`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*lwDhNrZH9nOtIG5-raaiFg.png)

### LESSON #4 — Scope and IIFE

The first time you wrote some JavaScript, someone probably told you to use the following notation because _“it works better”_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*STUXPjN-r6umC3VQwC7EmQ.png)

It does the same as declaring a regular function and then calling it immediately.

This notation is an [IIFE](https://en.wikipedia.org/wiki/Immediately-invoked_function_expression), it stands for **Immediately Invoked Function Expression**. And it doesn’t work better but it prevents variable collisions.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Z7r-mW31xLOYz7PeBeVuVg.png)

`foo` variable from a **script tag** is magically attached to the window. Pretty interesting when you know libraries and frameworks define their own variables using the same technique.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ibEEEl6V5oXcq7hyh-Z0GA.png)
_Variable collision on the variable named ‘Vue’_

Actually the **scope** of variables defined with the `var` keyword isn’t bound to all blocks. Those blocks are code parts delimited with curly braces as in `if` and `for` expressions, for instance.

Only `function` and `try-catch` blocks can restrict `var`'s scope. Even `if-else` blocks and `for` loops can’t do it.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jmZGwgpNrrnC3nT2DlKbtg.png)

Using IIFE provides a way to hide variables from the outside and restrict their scope. Thus, no one can alter the business logic by changing the window’s variable values.

![Image](https://cdn-media-1.freecodecamp.org/images/1*SKPQrd8ekt_cDjGEA5yNWw.png)

ES6 comes with the `let` and `const` keyword. Variables using these keywords are bound to blocks defined with curly braces.

### LESSON #5 — Object and maps

Objects help gather variables with the same topic under a unique variable. You end with an object containing many properties. There are two syntaxes to access an object property: dot and array syntax.

![Image](https://cdn-media-1.freecodecamp.org/images/1*PFNO-NyFBTmtIiiHGt3ccg.png)

The array syntax seems to be the best solution to create maps but it’s not. In this setup, keys must be strings. If not it’s coerced into a string. For instance, any object is coerced as `[object Object]` key.

```js
// From here, examples are a bit lengthy.
// I’ll use emebeded code so you can copy/paste and try yourself!

let map = {};
let x = { id: 1 },
    y = { id: 2 };

map[x] = 'foo';
map[y] = 'bar';

console.log(map[x], map[y]); // 'bar', 'bar'
```

From here, examples are a bit lengthy. I’ll use gists so you can copy/paste and try yourself!

In reality, this map got only one value under the `[object Object]` key. First, its value is `'foo'` and then it becomes `'bar'`.

To avoid this issue, use the [Map object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map) introduced in ES6. Yet be careful, the lookup operation to get a value from a key is using a [strict equality](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Equality_comparisons_and_sameness#Strict_equality_using).

```js
var map = new Map();
map.set(x, 'foo');
map.set(y, 'bar');

console.log(map.get(x), map.get(y)); // 'foo', 'bar'

// undefined, undefined
console.log(map.get({ id: 1 }, map.get({ id: 2 });
```

This detail only matters for complex variables such as objects. Because two objects with the same content won’t match with strict equality. You must use the exact variable you put as a key to retrieve your value from the map.

### LESSON #6 — What’s this?

The `this` keyword is used in languages built with classes. Usually, `this` (and its sibling `self`) refer to the current instance of the class being used. Its meaning doesn’t change a lot in [OOP](https://en.wikipedia.org/wiki/Object-oriented_programming). But, JavaScript didn’t have classes prior to ES6 (although it still had the `this` keyword).

The value of `this` in JavaScript is different according to the context. To determine its value, you must first inspect the **call-site** of the function where you’re using it.

```js
function foo () {
   console.log( this.a );
}

// #1: Default binding
var a = 'bar';

// [call-site: global]
foo(); // 'bar' or undefined (strict mode)
```

It seems strange when you compare this behaviour with the OOP standards. This first rule isn’t that important because most JavaScript codes uses [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode). Also, thank’s to ES6, developers will tend to use `let` and `const` instead of the legacy `var`.

This is the first rule which is applied by default to bind a value to `this`. There are 4 rules in total. Here are the remaining 3 rules:

```js
// It’s not easy to understand, copy this code and do some tests!

// #2: Implicit binding
const o2 = { a: 'o2', foo };
const o1 = { a: 'o1', o2 };

o1.o2.foo(); // [call-site: o2] 'o2'

// #3: Explicit binding
const o = { a: 'bar' }; 
foo.call(o); // [call-site: o] 'bar'

const hardFoo = foo.bind(o); // [call-site: o]
hardFoo(); // [call-site: o] 'bar'

// #4: New binding
function foo() {
   this.a = 'bar';
}
let result = new foo(); // [call-site: new]
console.log(result.a); // 'bar'
```

The last **new binding rule** is the first rule JavaScript tries to use. If this rule doesn’t apply, it’ll fall back to the other rules: **explicit binding**, **implicit binding** and eventually **default binding**.

The most important thing to remember:

> this changes with the function call-site, rules for binding get priorities

Besides those rules, there are still some edge-cases. It becomes a bit tricky when some rules are skipped depending on the call-site or `this` value.

```js
// 1- Call-site issue
const o = { a: 'bar', foo };
callback(o.foo); // undefined

function callback(func){
  func(); // [call-site: callback]
}

// 2- Default binding isn't lexical binding
var a = 'foo';
function bar(func){
   var a = 'bar'; // Doesn't override global 'a' value for this
   func();
}
bar(foo); // 'foo'

// 3- this is null or undefined
var a = 'foo';
foo.call(null); // 'foo' because given 'this' is null
```

That’s it about `this` binding. I agree it’s not easy to understand at first glance but after a while it’ll sink in. You must put the effort in to learn how it works and practice a lot.

To be honest, it’s a sum up from the entire [third book of the series](https://github.com/getify/You-Dont-Know-JS/tree/master/this%20%26%20object%20prototypes). Don’t hesitate to begin with this book and read some chapters. [Kyle](https://www.freecodecamp.org/news/you-might-not-know-js-insights-from-the-javascript-bible-2ee9518302aa/undefined) Simpson gives far more examples and very detailed explanations.

### LESSON #7— Promises pattern

Before ES6, the common way to handle asynchronous programming was using callbacks. You call a function which can’t provide a result immediately, so you provide a function it’ll call once it finishes.

Promises are related to callbacks, but they’re going to replace callbacks. The concept of promises isn’t easy to grasp, so take your time to understand the example and try them!

#### From callbacks to promises

First, let’s talk about callbacks. Did you realize that using them introduces an [inversion of control](https://en.wikipedia.org/wiki/Inversion_of_control) (IoC) into the program execution? The function you’re calling gets the control over your script execution.

```js
// Please call 'eatPizza' once you've finished your work
orderPizza(eatPizza);

function orderPizza(callback) {
   // You don't know what's going on here!
   callback(); // <- Hope it's this
}

function eatPizza() {
   console.log('Miam');
}
```

You’ll eat your pizza, once it’s delivered and the order completed. The process behind `orderPizza` isn’t visible to us, but it’s the same for library’s functions. It may call `eatPizza` multiple times, none at all or even wait for a long time.

With promises, you can reverse the callbacks’ IoC. The function won’t ask for a callback but instead, give you a promise. Then, you can subscribe so you’ll get notice after the promise resolves (either with fulfillment or rejection).

```js
let promise = orderPizza(); // <- No callback 

// Subscribes to the promise
promise.then(eatPizza);     // Fulfilled promise
promise.catch(stillHungry); // Rejected promise

function orderPizza() {
  return Promise.resolve(); // <- returns the promise
}
```

Callback-based functions often ask for two callbacks (success and failure) or pass a parameter to the only callback and let you look for errors.

With promises, those two callbacks change into `then` and `catch`. It matches success and failure but promise terms are different. A **fulfilled promise is a success** (with `then`) and a **rejected promise is a failure** (with `catch`).

Depending on the API, or the library you use for promises, the `catch` may not be available. Instead, `then` takes two functions as arguments, and it’s the same pattern as for callback-based functions.

In the example, `orderPizza` returns a fulfilled promise. Usually, this kind of asynchronous function returns a pending promise ([documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)). But, in most cases, you won’t need the promise constructor because `Promise.resolve` and `Promise.reject` are enough.

A promise is nothing more than an object with a state property. The function you’re calling changes this state from **pending** to **fulfilled** or **rejected** once it completes its work.

```js
// Function executed even if there are no then or catch
let promise = Promise.resolve('Pizza');

// Add callbacks later, called depending on the promise status
promise.then(youEatOneSlice);
promise.then(yourFriendEatOneSlice);
promise.then(result => console.log(result)); // 'Pizza'

// Promise is an object (with at least a then function: it's a thenable object)
console.log(promise); // { state: 'fulfilled', value: 'Pizza' }
```

You can join a value to a promise. It’s forwarded to the subscribed callbacks as a parameter (`then` and `catch`). In this example, there are two subscriptions on the fulfillment callback. Once the promise fulfills, the two subscribed functions trigger in any order.

**To sum up: there are still callbacks with promises.**

But promises act like a trusted third party. They’re [immutable](https://en.wikipedia.org/wiki/Immutable_object) after completion and so can’t resolve multiple times. Also, in the next part, you’ll see that it’s possible to react when a promise is still pending for a long time.

Note you can turn a callback-based function into a promise-based function with a few lines of code ([see this gist](https://gist.github.com/jbardon/dedede64f070de31a26e9d88d3ae0562)). For sure there are libraries. Sometimes it’s also included in the language API (TypeScript has a promisify function).

#### Leverage the Promise API

Both callback and promises have to deal with the issue of dependent asynchronous tasks. It occurs when the result of a first async function is necessary to call a second async function. Also, the third async function needs the result from the second function, and so on…

It’s important to look at how to handle this situation properly. That’s what leads to a horrible codebase. Look a the following code, you should be familiar with it:

![Image](https://cdn-media-1.freecodecamp.org/images/1*Bn-bt2dZTNcZySovNCtONw.png)
_An example of callback hell_

You’ve just meet a [callback hell](https://en.wiktionary.org/wiki/callback_hell). To eat a pizza, the chef must cook it, then pack it and the delivery guy deliver it to you. Finally, you can eat the delivered pizza.

Each step is asynchronous and needs the previous step’s result. That’s the point which leads you to write callback hell code. Promises can avoid it because they can either return other promises or values (wrapped in a promise).

![Image](https://cdn-media-1.freecodecamp.org/images/1*DfRiJM9wpGaNF_PBzpGxFg.png)
_Promise chain with syntax shortcus_

This snippet looks complex and simple at the same time. The code is small but it seems like we put in some magic things. Let’s split each step and get rid of ES6 syntax to make it clear:

```js
// Detailled promise chain with plain ES5, try the pratice part!

const cookPromise = cookPizza();

const packPromise = cookPromise.then(function(pizza) {
    return pack(pizza); // Returns a promise stored in packPromise
});
  
const deliverPromise = packPromise.then(function (packedPizza) { // value from pack(pizza)
    return deliver(packedPizza);
});

deliverPromise.then(function (deliveredPizza) {
    return eat(deliveredPizza);
});

/* For you to practice */
// - An example for cookPizza, pack, deliver and eat implementation
//   Each function append something to the previous step string
function pack(pizza) { 
    return Promise.resolve(pizza + ' pack');
}

// - Retrieve the result of eat and display the final string
//   Should be something like: 'pizza pack deliver eat'
eatPromise.eat((result) => console.log(result));
```

Now, you have the short syntax and the most verbose. To better understand this piece of code, you should:

* Implement `cookPizza`, `pack`, `deliver` and `eat` functions
* Check that each function changed the string using the `eatPromise`
* Refactor the code step by step to get to the short syntax

There’s also the regular usage from promises. The [Promises API](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference--/Global_Objects/Promise#Methods) also provides helpers to handle common concurrency interaction conditions such as **gate**, **race** and **latch**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*kmSMWUqTU_QnI9UYDs2YGw.png)

In this example, only the `then` is used but `catch` is also available. For `Promise.all` it’ll trigger instead of `then` if at least one promise is rejected.

As explained before, you can use promises to “_check and act when a promise is still pending for a long time_”. It’s the common use case for `Promise.race`. If you want to get a complete example with a timeout, check out [this part](https://github.com/getify/You-Dont-Know-JS/blob/master/async%20%26%20performance/ch3.md#never-calling-the-callback) of the book.

#### Going further with ES7

In some code, you might find [**deferred objects**](https://developer.mozilla.org/en-US/docs/Mozilla/JavaScript_code_modules/Promise.jsm/Deferred) to handle promises. For instance, AngularJS provides it through the [$q service](https://docs.angularjs.org/api/ng/service/$q).

Using them seems more natural and understandable but they’re not. You better take your time to learn promises.

![Image](https://cdn-media-1.freecodecamp.org/images/1*W5e2awkUrPHB2blVePE7rg.png)

You may need to return a promise and change its state later. Before you choose this solution, make sure there are no others ways. Anyway, the Promise API doesn’t return deferred objects.

**Don’t use a deferred object. If you think you need to, go over promises again**

But you can use the Promise constructor to mimic this behaviour. Check [this gist of mine](https://gist.github.com/jbardon/da9faa37cfc8cf31c2726cca1923262c) to know more but remember — it’s bad!

Last but not least, ES7 introduced a new way to handle promises by leverage [generators syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*). It allows you to make asynchronous functions look like regular synchronous functions.

```js
// ES6 syntax
function load() { 
  return Promise.all([foo(), bar()])
    .then(console.log);
}
load();

// ES7 syntax
async function load() { 
  let a = await foo();
  
  // Gets here once 'foo' is resolved and then call 'bar'
  let b = await bar(); 
  console.log(a, b);
}
load();
```

Flag the `load` which calls the asynchronous functions `foo` and `bar` with the `async` keyword. And put `await` before the asynchronous calls. You’ll be able to use the `load` as before, with a classic `load()`.

This syntax is appealing, isn’t it? No more callback and promise hell with infinite indentation. But wait, you should consider how generators work to avoid performances issues.

In the above example, `bar` is only executed once `foo` promise resolves. Their execution isn’t parallelised. You’ll get the exact same result by writing something like `foo.then(bar)`.

Here is how to fix it:

```js
async function load() {
   let fooPromise = foo();
   let barPromise = bar();
  
   // foo and bar are executed before Promise.all
   let results = await Promise.all([fooPromise, barPromise]);
   console.log(results);
}
load();
```

Make use of the `Promise.all`. Actually, `await` means you want to execute your function step by step. First, from the beginning to the first `await`. Once the promise from the first `await` resolves, it’ll resume the function up to the next `await` keyword. Or to the end of the function if there aren’t more.

In this example, `foo` and `bar` execute during the first step. The `load` function takes a break on `Promise.all`. At this point `foo` and `bar` already began their work.

This was a quick introduction to promises with some notes about the traps you don’t want to fall into. This sums up of the [fifth book of the series](https://github.com/getify/You-Dont-Know-JS/tree/master/async%20%26%20performance) which describes in depth asynchronous patterns and promises.

You can also look at [this article](https://medium.com/@pyrolistical/how-to-get-out-of-promise-hell-8c20e0ab0513) by [Ronald Chen](https://www.freecodecamp.org/news/you-might-not-know-js-insights-from-the-javascript-bible-2ee9518302aa/undefined). He gathers a lot of promise anti-patterns. This article will help you to escape the so-called promise hell.

### Wrapping up

These were the most important lessons I learned by reading [You Don’t Know JS](https://github.com/getify/You-Dont-Know-JS). This book series has way more lessons and details to teach you about how JavaScript works.

Just a heads up: for me, it was sometimes hard to follow when the author quotes the ECMAScript spec and lengthy examples. The books are long for sure, but also very complete. By the way, I almost give up but finally, I keep reading to the end and I can tell you — it was worth it.

This isn’t some kind of advertising for [Kyle](https://www.freecodecamp.org/news/you-might-not-know-js-insights-from-the-javascript-bible-2ee9518302aa/undefined). I just like this series and consider it a reference. Also, it’s free to read and contribute to the series through the [GitHub repository](https://github.com/getify/You-Dont-Know-JS).

**If you found this article useful, please click on the** ? **button a few times to make others find the article and show your support!** ?

**Don’t forget to follow me to get notified of my upcoming articles** ?

### Check out my [Other](https://www.freecodecamp.org/news/author/jbardon/) Articles

#### ➥ JavaScript

* [React for beginners series](https://medium.freecodecamp.org/a-quick-guide-to-learn-react-and-how-its-virtual-dom-works-c869d788cd44)
* [How to Improve Your JavaScript Skills by Writing Your Own Web Development Framework](https://medium.freecodecamp.org/how-to-improve-your-javascript-skills-by-writing-your-own-web-development-framework-eed2226f190)
* [Common Mistakes to Avoid While Working with Vue.js](https://medium.freecodecamp.org/common-mistakes-to-avoid-while-working-with-vue-js-10e0b130925b)

#### ➥ Tips & tricks

* [How to Master IntelliJ to Boost Your Productivity](https://medium.freecodecamp.org/how-to-master-intellij-to-boost-your-productivity-44b9da20c556)
* [Stop Painful JavaScript Debug and Embrace Intellij with Source Map](https://medium.com/dailyjs/stop-painful-javascript-debug-and-embrace-intellij-with-source-map-6fe68eda8555)
* [How To Reduce Enormous JavaScript Bundles Without Effort](https://medium.com/dailyjs/how-to-reduce-enormous-javascript-bundle-without-efforts-59fe37dd4acd)

