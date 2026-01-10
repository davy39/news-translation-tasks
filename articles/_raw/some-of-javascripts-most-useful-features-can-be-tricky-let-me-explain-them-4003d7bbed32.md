---
title: JavaScript Symbols, Iterators, Generators, Async/Await, and Async Iterators
  — All Explained Simply
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-11T23:16:55.000Z'
originalURL: https://freecodecamp.org/news/some-of-javascripts-most-useful-features-can-be-tricky-let-me-explain-them-4003d7bbed32
coverImage: https://cdn-media-1.freecodecamp.org/images/1*UovxjrPZdmpuy_P4w-5I5A.jpeg
tags:
- name: Apps
  slug: apps-tag
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By rajaraodv

  Some JavaScript (ECMAScript) features are easier to understand than others. Generators
  look weird — like pointers in C/C++. Symbols manage to look like both primitives
  and objects at the same time.

  These features are all inter-related an...'
---

By rajaraodv

Some JavaScript (ECMAScript) features are easier to understand than others. `Generators` look weird — like pointers in C/C++. `Symbols` manage to look like both primitives and objects at the same time.

**These features are all inter-related and build on each other. So you can’t understand one thing without understanding the other.**

So in this article, I’ll cover `symbols`,`global symbols`,`iterators`, `iterables`, `generators` , `async/await` and `async iterators`. **I’ll explain “_why_” they are there in the first place and also show how they work with some useful examples.**

> This is relatively advanced subject, but it’s not rocket science. This article should give you a very good grasp of all these concepts.

**OK, let’s get started.?**

![Image](https://cdn-media-1.freecodecamp.org/images/HBiVhsE9-rPJxFPNFdN5-5ZnnZSQmzN89X7H)

### Symbols

In ES2015, a new (6th) datatype called `symbol` was created.

#### WHY?

The three main reasons were:

#### Reason #1 — Add new core-features with backward compatibility

JavaScript developers and the ECMAScript committee ([TC39](http://ecma-international.org/memento/TC39.htm)) needed a way to add new object properties without breaking existing methods like `for in` loops or JavaScript methods like`Object.keys`.

For example, if I have an object, `var myObject = {firstName:'raja', lastName:'rao'}` and if I run`Object.keys(myObject)` it would return`[firstName, lastName]` .

Now if we add another property, say `newProperty` to `myObject` , and if you run `Object.keys(myObject)` it **should** **still** return old values (that is, somehow make it ignore the newly added `newproperty`), and show just`[firstName, lastName]` — and not `[firstName, lastName, newProperty]` . How to do that?

We couldn’t really do this earlier, so a new data type called `Symbols` was created.

If you add `newProperty` as a symbol, then `Object.keys(myObject)` would ignore this (as it doesn’t know about it), and still return `[firstName, lastName]` !

#### Reason #2 — Avoid name collisions

They also wanted to keep these properties unique. This way they can keep adding new properties (and you can add object properties) to global without worrying about name-collisions.

For example, say that you have an object where you are adding a custom `toUpperCase` to global `Array.prototype` .

Now, imagine you loaded another library (or ES2019 came out) and it had a different version of `Array.prototype.toUpperCase.` Then your function might break because of name collision.

![Image](https://cdn-media-1.freecodecamp.org/images/J6B2ibbhbGxk4KQq4j4CYL6zVTWXyXL6-B4o)

So how do you resolve this name collision that you may not know about? That’s where `Symbols` come in. They internally create unique values that allow you to create add properties without worrying about name collision.

#### Reason #3 —Enable hooks to core methods via “Well-known” Symbols

Suppose you want some core function, say`String.prototype.search` to call your custom function. That is, `‘somestring’.search(myObject);` should call `myObject’s` search function and pass `‘somestring’` as a parameter! How do we do that?

This is where ES2015 came up with a bunch of global symbols called “well-known” symbols. And as long as **your** object has one of of those symbols as a property, you can redirect core functions to call your function!

We can’t talk much about this right now, so I’ll go into all details a bit later in this article. But first, let’s learn about how Symbols actually work.

#### Creating Symbols

You can create a symbol by calling a global function/object called `Symbol` . That function returns a value of datatype `symbol`.

![Image](https://cdn-media-1.freecodecamp.org/images/clCoLqejtYU7HEECtCfze7I8Al5voKei--8-)

**Note:** Symbols might appear like Objects because they have methods, but they are not — they are primitives. You can think of them as “special” objects that have some similarities to regular objects, but that don’t behave like regular objects.

For example: Symbols have methods just like Objects, but unlike objects they are immutable and unique.

#### Symbols can’t be created by “new” keyword

Because symbols are not objects and the `new` keyword is supposed to return an Object, we can’t use `new` to return a `symbols` datatype.

```
var mySymbol = new Symbol(); //throws error
```

#### Symbols have “description”

Symbols can have a description — it’s just for logging purposes.

```
//mySymbol variable now holds a "symbol" unique value//its description is "some text"const mySymbol = Symbol('some text');
```

#### Symbols are unique

```
const mySymbol1 = Symbol('some text');const mySymbol2 = Symbol('some text');mySymbol1 == mySymbol2 // false
```

#### Symbols behave like a singleton if we use “Symbol.for” method

Instead of creating a `symbol` via `Symbol()` , you can create it via `Symbol.for(<ke`y>). This takes a “key” (string) to create a Symbol. And if a symbol with `th`at key already exists, it simply returns the old symbol! So it behaves like a singleton if we us`e the Symb`ol.for method.

```
var mySymbol1 = Symbol.for('some key'); //creates a new symbolvar mySymbol2 = Symbol.for('some key'); // **returns the same symbolmySymbol1 == mySymbol2 //true 
```

The real reason to use the `.for` is to create a Symbol in one place and access the same Symbol from some other place.

**Caution:** `Symbol.for` will make the symbol non-unique in the sense that you’ll end up overriding the values if the **keys** are the same! So try to avoid this if possible!

#### Symbol’s “description” versus “key”

Just to make things clearer, if you don’t use `Symbol.for` , then Symbols are unique. However, if you use it, then if your `key` is not unique, then the symbols returned will also be not unique.

![Image](https://cdn-media-1.freecodecamp.org/images/8zbLMllXK82Hk5TjWO0xZgSm8gWlTIp6QAKu)

#### Symbols can be an object property key

This is a very unique thing about Symbols — and also most confusing. Although they appear like an object, they are primitives. And we can attach a symbol to an Object as a property key just like a String.

In fact, this is one of the main ways of using Symbols — as object properties!

![Image](https://cdn-media-1.freecodecamp.org/images/R-dqw1eSSUtKqHL4rqpLOlPDtjTtpclIHSty)

**Note:** Object properties that are symbols are known as “keyed properties”.

#### Brackets operator vs. dot operator

You cannot use a dot operator because dot operators only work on string properties, so you should use a brackets operator.

![Image](https://cdn-media-1.freecodecamp.org/images/hfq5DSd88rGXqlUpyqsJn258KvQu3CD-LniM)

### 3 main reasons to use Symbols — a review

Let’s revisit the three main reasons now that we know how Symbols work.

#### **Reason #1 — Symbols are invisible to loops and other methods**

The for-in loop in the example below loops over an object `obj` but it doesn’t know (or ignores)`prop3` and `prop4` because they are symbols.

![Image](https://cdn-media-1.freecodecamp.org/images/FO2t8FHLz9eRviM4xBs8wLk4SOxR1u7ne31x)

Below is another example where `Object.keys` and `Object.getOwnPropertyNames` are ignoring property names that are Symbols.

![Image](https://cdn-media-1.freecodecamp.org/images/OpEPnJHKdDXt3332AS27me9YBMr3Tx6Efyj-)

#### **Reason #2 — Symbols are unique**

Suppose you want a feature called `Array.prototype.includes` on the global `Array` object. It will collide with the default `includes` method that JavaScript (ES2018) comes with out-of-the-box. How do you add it without colliding?

First, create a variable with proper name `includes` and assign a symbol to it. Then add this variable (now a symbol), to the global `Array` using bracket notation. Assign any function you want.

Finally call that function using bracket notation. But note that you must pass the actual symbol within the brackets like: `arr[includes]()` and not as a string.

![Image](https://cdn-media-1.freecodecamp.org/images/lJo8y-zLg8TZtPXBfyVEmtJSJ3yb6gR7GFoO)

#### Reason #3. Well-known Symbols (that is, “global” symbols)

By default, JavaScript auto-creates a bunch of symbol variables and assigns them to the global `Symbol` object ( yeah, the same `Symbol()`we use to create symbols).

In ECMAScript 2015, These symbols are then added to core methods such as `String.prototype.search` and `String.prototype.replace` of core objects such as arrays and strings.

Some examples of these symbols are: `Symbol.match`, `Symbol.replace`, `Symbol.search`, `Symbol.iterator` and `Symbol.split`.

Since these global symbols are global and exposed, we can make core methods call **our** custom functions instead of internal ones.

#### An Example: `_Symbol.search_`

For example, String object's `String.prototype.search` public method searches for a regExp or a string and returns the index if found.

![Image](https://cdn-media-1.freecodecamp.org/images/69xn6K7tJAA6eJeKkEi8n-bRebGfM7fphoRf)

In ES2015, it first checks if `Symbol.search` method is implemented in the query regExp (RegExp object). If so, then it calls that function and delegates the work to that. And core-objects like RegExp implements the `Symbol.search` symbol that actually does the work.

#### Inner workings of Symbol.search (DEFAULT BEHAVIOR)

1. Parse `‘rajarao’.search(‘rao’);`
2. Convert “rajarao” into String Object `new String(“rajarao”)`
3. Convert “rao” into RegExp object `new Regexp(“rao”)`
4. Call `search` method of “rajarao” String object.
5. `search` method internally calls `Symbol.search` method on “rao” object (delegates the search back to the “rao” object) and pass the “rajarao”. Something like this: `"rao"[Symbol.search]("rajarao")`
6. `"rao"[Symbol.search]("rajarao")` returns index result as `4`to `search` function and finally, `search` returns `4` back to our code.

The below pseudo-code snippet shows how the code internally works:

![Image](https://cdn-media-1.freecodecamp.org/images/eRX3vzKog8jhzxjyMoOMxEyq4-OxrmrxPcYq)

But the beauty is that, you no longer have to have pass RegExp. You can pass any custom object that implements `Symbol.search` and return whatever you want and this will continue to work.

Let’s take a look.

#### Customizing the String.search method to call our function

The below example shows how we can make `String.prototype.search` call our `Product` class’s search function — thanks to `Symbol.search` global `Symbol`.

![Image](https://cdn-media-1.freecodecamp.org/images/kcc8eq6pH5DRkxRTMDTIkCPJpnr4zgrWVESY)

#### Inner workings of Symbol.search (CUSTOM BEHAVIOR)

1. Parse `‘barsoap’.search(soapObj);`
2. Convert “barsoap” into String Object `new String(“barsoap”)`
3. Since `soapObj` is already an object, don’t do any conversion
4. Call `search` method of “barsoap” String object.
5. `search` method internally calls `Symbol.search` method on “`soapObj`” object (that is, it delegates the search back to the “`soapObj`” object) and pass the “barsoap”. Something like this: `soapObj[Symbol.search]("barsoap")`
6. `soapObj[Symbol.search]("barsoap")` returns the index result as `FOUND` to `search` function and finally, `search` returns `FOUND` back to our code.

Hopefully you have a good grasp of Symbols now.

OK, let’s move on to Iterators.

![Image](https://cdn-media-1.freecodecamp.org/images/kEHK8PEgmOHaS6VUgG23msLpi8X8sMxPQsbV)

### Iterators and Iterables

#### WHY?

In almost all our apps, we are constantly dealing with lists of data and we need to display that data in the browser or mobile app. Typically we write our own methods to store and extract that data.

But the thing is, we already have standard methods like the `for-of` loop and spread operator (`…`) to extract collections of data from standard objects like arrays, strings, and maps. Why can’t we use these standard methods for our Object as well?

In the example below, we can’t use a for-of loop or spread operator to extract data from our `Users` class. We have to use a custom `get` method.

![Image](https://cdn-media-1.freecodecamp.org/images/0ZUUfwRblzYmzhfuh9ziyANRNRgzNefSRVQA)

But, wouldn’t it be nice to be able to use these existing methods in our own objects? In order to achieve this, we need to have rules that all developers can follow and make their objects work with existing methods.

If they follow these rules to extract data from their objects, then such objects are called “iterables”.

The rules are:

1. The main object/class should store some data.
2. The main object/class must have the global “well-known” symbol `symbol.iterator` as its property that implements a specific method as per rules #3 to #6.
3. This `symbol.iterator` method must return another object — an “iterator” object.
4. This “iterator” object must have a method called the `next` method.
5. The `next` method should have access to the data stored in rule #1.
6. And if we call `iteratorObj.next()`, it should return some stored data from rule #1 either as `{value:<stored data>, **done:**` false} format if it wants to return more values, `or as {**done**:` true} if it doesn’t want to return any more data.

If all those 6 rules are followed, then the main object is called as an “**iterable**” from rule #1. The object it returned is called an “**iterator**”.

Let’s take a look at how we can make our `Users` object and iterable:

![Image](https://cdn-media-1.freecodecamp.org/images/NCcsb6xvxscZ24U7swkutqwjjFfi4YYHECd-)
_Please click to zoom_

**Important note**: If we pass an `iterable` (`allUsers`) `for-of` loop or spread operator, internally they call `<iterable>[Symbol.itera`tor]() to get the iterator `(like allUsersIt`erator ) and then use the iterator to extract data.

So in a way, all those rules are there to have a standard way to return an `iterator` object.

![Image](https://cdn-media-1.freecodecamp.org/images/mPZxgsP8mMLNhJIqiXGF5yFPJ5fdmeJk9dyG)

### Generator functions

#### **WHY?**

There are two main reasons:

1. provide higher-level abstraction to iterables
2. Provide newer control-flow to help with things like “callback-hell”.

Let’s check them out in detail.

#### REASON #1 — A wrapper for iterables

Instead of making our class/object an `iterable` by following all those rules, we can simply create something called as a “Generator” method to simplify things.

Below are some of the main points about Generators:

1. Generator methods have a new `*<myGenerat`or> syntax inside a class, and Generator functions have the s`yntax function * myGenerat`or(){}.
2. Calling generators `myGenerator()`returns a `generator` object that also implements the `iterator` protocol (rules), so we can use this as an `iterator` return value out-of-the-box.
3. Generators use a special `yield` statement to return data.
4. `yield` statements keep track of previous calls and simply continue from where it left off.
5. If you use `yield` inside a loop, it’ll only execute once each time we call the `next()` method on the iterator.

#### **Example 1:**

The below code shows you how you can use a generator method (`*getIterator()`) instead of using the `Symbol.iterator` method and implementing the `next` method that follows all the rules.

![Image](https://cdn-media-1.freecodecamp.org/images/pZfUjKv5veWYeQQ1zskNUzsL-mEJZ1cGrnko)
_Using generators inside a Class_

#### **Example 2:**

You can simplify it even further. Make a function a generator (with * syntax), and use `yield` to return values one at a time like shown below.

![Image](https://cdn-media-1.freecodecamp.org/images/nYHrw83GR5EF0jPwR3p-0bbkwmBXJuQJB8ER)
_Using Generators directly as functions_

**Important Note**: Although in the examples above, I’m using the word “iterator” to represent `allUsers` , it’s really a `generator` object .

The generator object has methods like `throw` and `return` in addition to the `next` method! But for practical purposes, we can use the returned object as just “iterator”.

#### REASON #2 — Provide better and newer control-flows

Help provide new control-flows that helps us write programs in new ways and solve things like “callback hell”.

Notice unlike a normal function, the generator function can `yield` (store the function’s `state` and `return` value) and also be ready to take additional input values at the point where it yielded.

In the picture below, every time it sees `yield`, it can return the value. You can use `generator.next(“some new value”)` and pass the new value at the point where it yielded.

![Image](https://cdn-media-1.freecodecamp.org/images/y3hrnT63qXkWewIj4rWbfocef-Mu8TeY02gi)
_Normal function vs Generator function_

The below example shows in more concrete terms how the control-flow works:

![Image](https://cdn-media-1.freecodecamp.org/images/JlyaniqPAd5mszB37kq3YbGhELKpdbsTm11c)
_Generator control flow_

### Generator syntax and usage

Generator functions can be used in the following ways:

![Image](https://cdn-media-1.freecodecamp.org/images/xNnkTFsqv23fBgya2lKmTyUb-COXeU4SCVIj)

#### **We can have more code after “yield” (unlike the “return” statement)**

Just like the `return` keyword, the `yield` keyword also returns the value — but it allows us to have code after yielding!

![Image](https://cdn-media-1.freecodecamp.org/images/w9dKtBLs7v3t5sLre8jpFmQ3TCgEWLTN99uj)

#### You can have multiple yields

![Image](https://cdn-media-1.freecodecamp.org/images/RtoVwrmiWrKVGZOnXX5MEqedj2IqllxMmeZW)
_you can have multiple yield statements_

#### Sending values back-and-forth to generators via the “next” method

The iterators `next` method can also pass values back into the generator as shown below.

In fact, this feature enables generators to eliminate “callback hell”. You’ll learn more about this in a bit.

This feature is also used heavily in libraries like [redux-saga](https://redux-saga.js.org/).

In the example below, we call the iterator with an empty `next()` call to get the question. And then, we pass `23` as the value when we call the `next(23)` the 2nd time.

![Image](https://cdn-media-1.freecodecamp.org/images/aSFH1y8bOkNPhzJgN4KFZH3g5QGTxwGIifIs)
_Passing value back to the generator from outside via “next”_

#### Generators help eliminate “callback hell”

You know that we get into [callback hell](http://callbackhell.com/) if we have multiple asynchronous calls.

The example below shows how libraries such as “[co](https://github.com/tj/co)” use the generator feature that allows us to pass a value via the `next` method to help us write async code synchronously.

Notice how the `co` function passes the result from the promise back to the generator via `next(result)` in Step #5 and Step #10.

![Image](https://cdn-media-1.freecodecamp.org/images/DJH7bZWmgDAmQMiecWmHXsPjKN9aiIzC0BGB)
_Step-by-Step explanation of libs like “co” that use “next(&lt;someval&gt;)”_

OK, let’s move on to async/await.

![Image](https://cdn-media-1.freecodecamp.org/images/q2ozY1fqYuvuRBnzmJZSxRDH4e1FTUhF254H)

### ASYNC/AWAIT

#### **WHY?**

As you saw earlier, Generators can help eliminate “callback hell”, but you need some 3rd party library like `co` to make that happen. But “callback hell” is such a big problem, the ECMAScript committee decided to create a wrapper just for that aspect of Generator and came out with the new keywords `async/await`.

The differences between Generators and Async/Await are:

1. async/await uses `await` instead of `yield`.
2. `await` only works with Promises.
3. Instead of `function*`, it uses the `async function` keyword.

So `async/await` is essentially a subset of Generators and has a new syntactic sugar.

The `async` keyword tells the JavaScript compiler to treat the function differently. The compiler pauses whenever it reaches the `await` keyword within that function. It assumes that the expression after `await` returns a promise and waits until the promise is resolved or rejected before moving further.

In the example below, the `getAmount` function is calling two asynchronous functions `getUser` and `getBankBalance` . We can do this in a promise, but using `async await` is more elegant and simple.

![Image](https://cdn-media-1.freecodecamp.org/images/3vUZj-y4RZb-LV2gDU2jNeL7n02zjUH9zbos)

![Image](https://cdn-media-1.freecodecamp.org/images/m9Ky899WlWX2Soj6vEleyTNOHt0LGVSEcZF7)

### ASYNC ITERATORS

#### **WHY?**

It’s a pretty common scenario where we need to call async functions in a loop. So in ES2018 (completed proposal), the TC39 committee came up with a new Symbol `Symbol.asyncIterator` and also a new construct `for-await-of` to help us easily loop over async functions .

The main difference between regular Iterator objects and Async Iterators is as follows:

#### **Iterator object**

1. Iterator object' s `next()` method returns value like `{value: ‘some val’, done: false}`
2. Usage : `iterator.next() //{value: ‘some val’, done: false}`

#### **Async Iterator object**

1. Async Iterator object’s next() method **returns a Promise** that later resolves into something like `{value: ‘some val’, done: false}`
2. Usage: `iterator.next().then(({ value, done })=> {//{value: ‘some val’, done: fals`e}}

The below example shows how `for-await-of` works and how you can use it.

![Image](https://cdn-media-1.freecodecamp.org/images/vgX-wE-V4P3j1f6v6qQv4FERtQXZYAR7-9PC)
_for-await-of (ES2018)_

### SUMMARY

**Symbols** — provide a globally unique data type. You use them mainly as object properties to add new behaviors so you don’t break standard methods like `Object.keys` and `for-in` loops.

**Well-known symbols** — are auto-generated symbols by JavaScript and can be used to implement core methods in our custom objects

**Iterables** — are any objects that store a collection of data and follow specific rules so that we can use standard `for-of` loop and `...` spread operators to extract data from within them.

**Iterators** — are returned by Iterables and have the `next` method — it’s what actually extracts the data from an `iterable`.

**Generators** —provide higher level abstraction to Iterables. They also provide new control-flows that can solve things like callback-hell and provide building blocks for things like `Async/Await`.

**Async/Await** — provides higher level abstraction to Generators in order to specifically solving callback-hell issue.

**Async Iterators** — a brand-new 2018 feature to help with looping over an array of async functions to get the result of each async function just like in a normal loop.

That’s pretty much it!

### Further reading

#### ECMAScript 2015+

1. [Here are examples of everything new in ECMAScript 2016, 2017 and 2018](https://medium.freecodecamp.org/here-are-examples-of-everything-new-in-ecmascript-2016-2017-and-2018-d52fa3b5a70e)
2. [Check out these useful ECMAScript 2015 (ES6) tips and tricks](https://medium.freecodecamp.org/check-out-these-useful-ecmascript-2015-es6-tips-and-tricks-6db105590377)
3. [5 JavaScript “Bad” Parts That Are Fixed In ES6](https://medium.com/@rajaraodv/5-javascript-bad-parts-that-are-fixed-in-es6-c7c45d44fd81#.7e2s6cghy)
4. [Is “Class” In ES6 The New “Bad” Part?](https://medium.com/@rajaraodv/is-class-in-es6-the-new-bad-part-6c4e6fe1ee65#.4hqgpj2uv)

My other posts can be found [here](https://medium.com/@rajaraodv/latest).

### If this was useful, please click the clap ? button down below a few times to show your support! ⬇⬇⬇

