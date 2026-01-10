---
title: Functional Programming In JavaScript — With Practical Examples (Part 1)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-11-14T18:28:03.000Z'
originalURL: https://freecodecamp.org/news/functional-programming-in-js-with-practical-examples-part-1-87c2b0dbc276
coverImage: https://cdn-media-1.freecodecamp.org/images/1*U1TQD4tsM3JLZ-MfBH-vJA.jpeg
tags:
- name: Angular
  slug: angularjs
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
seo_title: null
seo_desc: 'By rajaraodv

  Functional Programming(FP) can change the way you program for the better. But it’s
  hard to learn and many posts and tutorials don’t go into details like Monads, Applicative
  and so on and don’t seem to use practical examples to help us us...'
---

By rajaraodv

Functional Programming(FP) can change the way you program for the better. But it’s hard to learn and many posts and tutorials don’t go into details like Monads, Applicative and so on and don’t seem to use practical examples to help us use powerful FP techniques on a daily basis. That’s why I thought of writing a post to make it easier to use FP techniques.

> Please Note: The emphasis in this blog is on **WHY** xyz feature is required than just **WHAT** xyz feature is.

**In Part 1, you’ll learn Functional Programming basics, Currying, Pure Functions, “Fantasy-land” specs, “Functors”, “Monads”, “Maybe Monads” and “Either Monads” via couple of examples.**

### Functional Programming

Functional Programming is a style of writing programs by simply composing a set of functions.

Essentially, FP asks us to wrap virtually everything in functions, write lots of small reusable functions and simply call them one after the other to get the result like: (**func1.func2.func3**) or in a compose fashion, like: **func1(func2(func3()))**.

But in order to actually write programs in this style, functions need to follow some rules and overcome some challenges like the ones mentioned below:

#### The FP Challenges:

If everything can be done by composing a set of functions..

1. How can we handle if-else condition? (**Hint: “Either” Monad**)
2. How can we handle Null Exceptions (**Hint: “Maybe” Monad**)?
3. How to ensure functions are truly “reusable” and can be reused anywhere, (**Hint:** **Pure functions,** **referential transparency**)?
4. How to ensure the data we pass to it is unchanged so that we can reuse the data elsewhere(**Hint:** **Pure functions, immutability**)?
5. If a function is taking multiple values but chaining can only pass a single value, how can we still make it part of a chain (**Hint:** “**currying” and “higher-order functions”**)?
6. and more..<add your question here>.

#### The FP Solution:

In order to deal with all these challenges, fully Functional Programming languages like Haskell provides various tools and concepts from mathematics like “Monads”, “Functors” and so on out-of-the-box.

While JavaScript doesn’t provide many of the tools out-of-the-box, thankfully it has enough FP features that allows people to write libraries.

### Fantasy-Land Specs And FP Libraries

Libraries that want to provide features like Functors, Monads and so on, need to implement functions/classes that follow some specs in order to provide functionalities like they are in languages like Haskell.

[Fantasyland specs](https://github.com/fantasyland/fantasy-land) is one of the prominent specs that explains how each JS functions/classes should behave.

![Image](https://cdn-media-1.freecodecamp.org/images/1*fwhU3xa-92GSWXCfUg2PKg.png)

The above picture shows all the specs and their dependencies. Specs are essentially laws and similar to “interfaces” in Java. From JS perspective, you can think of specs as “classes” or constructor functions that implement some methods like (**map**, **of**, **chain** and so on) according to the specification.

For example:

A JS class is a “Functor” if it implements a “map” method. And that map method must work as per spec (ps:This is simplified version and there are more rules).

Similarly, a JS class is an “Apply Functor” if it implements “map” and “ap” functions as per spec.

Similarly, a JS class is a “Monad” (aka Monad Functor), if implements requirements of “Functor”, “Apply”, “Applicative”, “Chain” and “Monad” itself (because of the dependency chain).

> Note: The dependency may look like inheritance but not necessarily. For example: Monad implements both “Applicative” and “Chain” specs (in addition to others).

#### Fantasy-Land Spec compliant Libraries

There are several libraries that implement FL spec. For example: [**monet.js,**](https://cwmyers.github.io/monet.js/) [barely-functional](https://github.com/cullophid/barely-functional), [folktalejs](http://folktalejs.org/), [ramda-fantasy](https://github.com/ramda/ramda-fantasy) (based on Ramda), [immutable-ext](https://github.com/DrBoolean/immutable-ext) (based on ImmutableJS), [Fluture](https://github.com/Avaq/Fluture) and more.

### What Libraries Should I Use?

Libraries like [**lodash-fp**](https://github.com/lodash/lodash/wiki/FP-Guide)**, [ramdajs](http://ramdajs.com/)**, only enable you to start writing in FP style. But they don’t provide functions to use key mathematical concepts like Monads, Functors, Foldables to actually solve real-world problems.

So, in addition to them you’ll have to use one of the libraries that follow fantasy-land spec. Some such libraries are: [monet.js,](https://cwmyers.github.io/monet.js/) **barely-functional, [folktalejs](http://folktalejs.org/), [ramda-fantasy](https://github.com/ramda/ramda-fantasy) (based on Ramda), [immutable-ext](https://github.com/DrBoolean/immutable-ext) (based on ImmutableJS), [Fluture](https://github.com/Avaq/Fluture) and more.**

> Note: I’m using [**ramdajs**](http://ramdajs.com/) and [**ramda-fantasy**](https://github.com/ramda/ramda-fantasy)

OK, now that we know the basics, Let’s see some practical examples and learn various FP features and techniques through those examples.

### Example 1 — Dealing With Null Checks

**_Topics covered: Functors, Monads, Maybe Monad, Currying._**

**Use-case:** We want to show different index webpage depending on the user’s “**primary”** **language** (inside user’s prefs, see below). And we need to write **getUrlForUser** that returns appropriate URL from the list of URLs(**indexURLs**) for the user’s (**joeUser**) **primary** **language**(“**spanish”**).

![Image](https://cdn-media-1.freecodecamp.org/images/1*6jUKhJlc2LK1aGAYilmtNw.png)

**The problem is:** the primary language could be null. The user itself could be null (not logged in). The primary language might not be available in our list of indexURLs. So we’ll have to take care of lots of “nulls” or “undefined”.

#### Solution (Imperative Vs FP):

> PS: Don’t worry if the FP version looks hard to understand, I’ll cover them step-by-step later in this post.

OK, Let’s first understand several FP concepts and techniques used in this solution.

#### Functors

Any class(or construction function) or a datatype that stores a value and implements “map” method is called a “Functor”.

For example: An Array is a “Functor”. Because an Array can store values and has “map” method that allows us to map a function to the values it’s storing.

```
const add1 = (a) => a+1;
```

```
let myArray = new Array(1, 2, 3, 4); //store values
```

```
myArray.map(add1) // -> [2,3,4,5] //applies functions
```

Let’s write our own Functor “MyFunctor”. It’s simply a JS class (constructor function) that stores some value and implements a “map” method. This “map” method applies the function to the stored value and then creates a new Myfunctor from the result and returns that new MyFunctor.

> PS: Functors also need to implement other specs (see [Fantasyland specs](https://github.com/fantasyland/fantasy-land)) in addition to “map” but I’m not going to cover them here.

#### Monads

Monads are also Functors, i.e. they have “**map**” method but implements more methods than just “map”. If you look at the spec dependency graph again, you’ll see that also need to implement various other features in different specs like: “[Apply](https://github.com/fantasyland/fantasy-land#apply)” (**ap** method), “[Applicative](https://github.com/fantasyland/fantasy-land#applicative)” (**ap** and **of** method), and “[Chain](https://github.com/fantasyland/fantasy-land#chain)” (**chain** method).

![Image](https://cdn-media-1.freecodecamp.org/images/1*fwhU3xa-92GSWXCfUg2PKg.png)

**_Simplified Explanation:_** _In JS, Monads are classes or constructor functions that store some data and implements “map”, “ap”, “of” and “chain” methods that do something with the stored data as per spec._

Below is a sample implementation so you get an idea of the internals of the Monad.

Now, the generic Monads are not typically used but more specific and more useful Monads like “Maybe Monad” or “Either Monad” are often used in FP programming. So, let’s take a look at “Maybe Monad”.

**“Maybe” Monad**

A “Maybe” Monad is a class that implements Monad spec. But the special thing about Monad is that it takes care of “null” or “undefined” values.

**Specifically, if the data stored is a null or undefined, then it’s “map” function doesn’t run the given function at all and there by avoiding any null or undefined issues**. It is used in situations where we are dealing with Null values.

> Below code shows ramda-fantasy’s implementation of Maybe Monad. It creates an instance of one of the two different sub-classes, **Just** or **Nothing,** depending on the value (i.e. useful value V/s null/undefined respectively).

> While both **Just** and **Nothing** has similar methods (map, orElse etc), Just’s actually does something but Nothing’s doesn’t do anything.

> **Give special attention to “map” and “orElse” methods below**

Let’s see how to use Maybe monad to deal with “null” checks.

Follow these steps:

1. If there any object that might be null or have null properties, create a Monad object out of it.
2. Use some libraries like ramdajs, that are “Maybe-aware” to access value from w/in the Monad and work on it.
3. Provide a default value if the actual value happens to be null (i.e handle Null errors upfront).

### Currying — (Helps Dealing With Global Data And Multi-Param Functions)

Topics covered: **Pure functions** and **Composition**

If we want to chain a series of functions together like: func1.func2.func3 or (func1(func2(func3())), all these functions can only receive just one input parameter each. For example, if func2 takes two parameters func2(param1, param2), then we can’t chain it!

But the practically speaking, many functions take multiple parameters. So how to use them in composition? Solution: “Currying”.

Currying converts a function that takes multiple parameter into a function that takes a single parameter at a time. It wont run the function until all parameters are passed.

#### In addition, Currying can also be used in situations when we are accessing global values. i.e. make it “pure”.

Let’s look at our solution again:

### Example 2— Handling Error Throwing Functions And Exiting Immediately After An Error

**Topics Covered: “Either Monad”**

Maybe Monad is great if we have “default” values to replace Null errors. But what about functions that actually need to throw errors? And how to know which function threw the error when we chain multiple error-throwing functions (i.e. we want fast-failure)?

For example: If we have **func1.func2.func3…** and if **func2** threw an error, we should skip **func3** and other future functions and properly show error from **func2** so we can handle it.

### **Either Monad**

Either Monads are great for dealing with multiple functions when they all can potentially throw error and want to quit immediately after an error so that we can pin-point where the error occurred.

**Use case:** For example in the below imperative snippet, we are calculating “**tax**” and “**discount**” for **items** and ultimately displaying **showTotalPrice**.

Note that the “**tax**” function will throw error if the price is non-numeric. Similarly, “**discount**” function will throw error if price is non-numeric and it will also throw error if the item’s price is less than 10.

> So **showTotalPrice** has multiple error checks.

Let’s see how **showTotalPrice** can be improved by using Either Monad and rewrite everything in FP style.

Either Monad provides two constructors: “Either.Left” and “Either.Right”. Think of them as subclasses of Either. **Both “Left” and “Right” are Monads!** **The idea is to store errors/exceptions in Left and useful values in Right**.

i.e. create an instance of Either.Left or Either.Right depending on the value. **Once we do that we can run map, chain and so on on those values to compose them.**

> While both **Left** and **Right** provide “map”, “chain” and so on, **Left** constructor doesn’t do anything as it stored Errors. Where as the **Right** constructor implements all the functions as it contains actual result.

**OK, Let’s see how to change our imperative example to FP**

**Step 1:** Wrap return values with Left and Right

> Note: “Wrap” means create an instance of some Class. These functions internally call “new” so we don’t have to.

**Step 2:** Wrap the initial value in **Right** because it’s a valid value and so we can compose it.

```
const getItemPrice = (item) =&gt; Right(item.price);
```

**Step 3:** Create two functions, one to handle eventual error and another to handle result. And warp them in **Either.either** (this is from [ramda-fantasy.js api](https://github.com/ramda/ramda-fantasy/blob/master/src/Either.js#L33)).

> **Either.either** takes 3 params. success handler, an error handler and an "Either" Monad. Either is curried. So we can just pass the handlers for now and pass the Either (3rd param) later.

> Once Either.either receives all 3 params, it passes the 3rd param "Either" to the success handler or error handler depending of if the Either is "Right" or "Left" respectively.

```
const displayTotal = (total) => { console.log(‘Total Price: ‘ + total) };
```

```
const logError = (error) => { console.log(‘Error: ‘ + error.message); };
```

```
const eitherLogOrShow = Either.either(logError, displayTotal);
```

**Step 4:** Use “**chain**” method to compose multiple error throwing functions. Pass their result to Either.either (eitherLogOrShow) which will take care of passing the result to success handler or failure handler.

```
const showTotalPrice = (item) => eitherLogOrShow(getItemPrice(item).chain(apply25PercDisc).chain(addCaliTax));
```

Putting it all together:

Thank you for reading! If you liked the post please ? and share it on Twitter!??

**LATEST:** [_Functional Programming In JS — With Practical Examples (Part 2)_](https://medium.com/@rajaraodv/functional-programming-in-js-with-practical-examples-part-2-429d2e8ccc9e#.r2mglxozr)

### My Other Posts

#### Functional Programming

1. [_JavaScript Is Turing Complete — Explained_](https://medium.com/@rajaraodv/javascript-is-turing-complete-explained-41a34287d263#.6t0b2w66p)
2. [_Functional Programming In JS — With Practical Examples (Part 1)_](https://medium.com/@rajaraodv/functional-programming-in-js-with-practical-examples-part-1-87c2b0dbc276#.fbgrmoa7g)
3. [_Functional Programming In JS — With Practical Examples (Part 2)_](https://medium.com/@rajaraodv/functional-programming-in-js-with-practical-examples-part-2-429d2e8ccc9e#.r2mglxozr)

#### ES6

1. [_5 JavaScript “Bad” Parts That Are Fixed In ES6_](https://medium.com/@rajaraodv/5-javascript-bad-parts-that-are-fixed-in-es6-c7c45d44fd81#.7e2s6cghy)
2. [_Is “Class” In ES6 The New “Bad” Part?_](https://medium.com/@rajaraodv/is-class-in-es6-the-new-bad-part-6c4e6fe1ee65#.4hqgpj2uv)

#### WebPack

1. [_Webpack — The Confusing Parts_](https://medium.com/@rajaraodv/webpack-the-confusing-parts-58712f8fcad9#.6ot6deo2b)
2. [_Webpack & Hot Module Replacement [HMR]_](https://medium.com/@rajaraodv/webpack-hot-module-replacement-hmr-e756a726a07#.y667mx4lg) _(under-the-hood)_
3. [_Webpack’s HMR And React-Hot-Loader — The Missing Manual_](https://medium.com/@rajaraodv/webpacks-hmr-react-hot-loader-the-missing-manual-232336dc0d96#.fbb1e7ehl)

#### Draft.js

1. [_Why Draft.js And Why You Should Contribute_](https://medium.com/@rajaraodv/why-draft-js-and-why-you-should-contribute-460c4a69e6c8#.jp1tsvsqc)
2. [_How Draft.js Represents Rich Text Data_](https://medium.com/@rajaraodv/how-draft-js-represents-rich-text-data-eeabb5f25cf2#.hh0ue85lo)

#### React And Redux :

1. [_Step by Step Guide To Building React Redux Apps_](https://medium.com/@rajaraodv/step-by-step-guide-to-building-react-redux-apps-using-mocks-48ca0f47f9a#.s7zsgq3u1)
2. [_A Guide For Building A React Redux CRUD App_](https://medium.com/@rajaraodv/a-guide-for-building-a-react-redux-crud-app-7fe0b8943d0f#.g99gruhdz) _(3-page app)_
3. [_Using Middlewares In React Redux Apps_](https://medium.com/@rajaraodv/using-middlewares-in-react-redux-apps-f7c9652610c6#.oentrjqpj)
4. [_Adding A Robust Form Validation To React Redux Apps_](https://medium.com/@rajaraodv/adding-a-robust-form-validation-to-react-redux-apps-616ca240c124#.jq013tkr1)
5. [_Securing React Redux Apps With JWT Tokens_](https://medium.com/@rajaraodv/securing-react-redux-apps-with-jwt-tokens-fcfe81356ea0#.xci6o9s6w)
6. [_Handling Transactional Emails In React Redux Apps_](https://medium.com/@rajaraodv/handling-transactional-emails-in-react-redux-apps-8b1134748f76#.a24nenmnt)
7. [_The Anatomy Of A React Redux App_](https://medium.com/@rajaraodv/the-anatomy-of-a-react-redux-app-759282368c5a#.7wwjs8eqo)

#### Salesforce

1. [_Developing React Redux Apps In Salesforce’s Visualforce_](https://medium.com/@rajaraodv/developing-react-redux-apps-in-salesforce-s-visualforce-3ad7be560d1c#.f6bao6mtu)

