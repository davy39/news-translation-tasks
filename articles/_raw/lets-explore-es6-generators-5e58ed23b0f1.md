---
title: Let’s explore ES6 Generators
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-06-21T17:22:27.000Z'
originalURL: https://freecodecamp.org/news/lets-explore-es6-generators-5e58ed23b0f1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*OiK88NOSMsbrlpWdDarvlg.gif
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Tiago Lopes Ferreira

  Generators are an implementation of iterables.

  The big deal about generators is that they are functions that can suspend its execution
  while maintaining the context.

  This behaviour is crucial when dealing with executions that ...'
---

By Tiago Lopes Ferreira

Generators are [an implementation of iterables](https://medium.freecodecamp.com/demystifying-es6-iterables-iterators-4bdd0b084082).

The big deal about generators is that **they are functions that can suspend its execution while maintaining the context**.

This behaviour is crucial when dealing with executions that need to be paused, but its context maintained in order to recover it in the future.

**Does async development sounds familiar here?**

### Syntax

The syntax for generators starts with it’s `function*` declaration (please note the _asterisk_) and the `yield` through which a generator can pause it’s execution.

Calling our `generator` function creates new generator that we can use to control the process through `next` function.

Running `next` will execute our `generator`’s code until an `yield` expression is reached.

At this point the value on `yield` is emitted and the `generator`’s execution is suspended.

#### yield

`yield` was born with generators and allow us to emit values. However, we can only do this while we are inside a generator.

If we try to `yield` a value on a callback, for instance, even if declared inside the generator, we will get an error.

#### yield*

`yield*` was built to enable calling a generator within another generator.

Our `b` iterator, produced by `bar` generator, does not work as expected when calling `foo`.

This is because, although the execution of `foo` produces an iterator, we do not iterate over it.

That’s why ES6 brought the operator `yield*`.

This works perfectly with data consumers.

Internally `yield*` goes over every element on the generator and `yield` it.

### Generators as Iterators

![Image](https://cdn-media-1.freecodecamp.org/images/1*p65T1aheR-c6JDSWRcUVhA.gif)

**Generators are simple iterables**, which means that they follow the `iterable` and `iterator` protocols:

* The `iterable` protocol says that an object should return a function iterator whose key is `Symbol.iterator`.

* The `iterator` protocol says that the iterator should be an object pointing to the next element of the iteration. This object should contain a function called `next`.

Because generators are iterables then we can use a data consumer, e.g. `for-of`, to iterate over generators’ values.

#### Return

We can add a `return` statement to our generator, however `return` will behave differently according to the way generators’ data is iterated.

When performing the iteration by hand, using `next`, we get our returned value (i.e. `done`) as the last `value` of our iterator object and our `done` flag as true.

On the side, when using a defined data consumer such as `for-of` or `destructuring`, the returned value is ignored.

#### **yield***

We saw that `yield*` allows us to call a generator inside a generator.

It also allow us to store the value returned by the executed generator.

#### Throw

We can `throw` inside a generator and `next` will propagate our exception.

As soon as an exception is thrown the iterator flow breaks and it’s state is set to `done: true` indefinitely.

### Generators as Data Consumers

Besides generators being data producers, through `yield`, they also have the ability to consume data using `next`.

There’s some interesting points to explore here.

#### Generator Creation (1)

At this stage we are creating our generator `g`.

Our execution stops at point `A`.

#### First next (2)

The first execution of `next` gets our generator to be executed until the first `yield` statement.

On this first execution any value sent through `next` is ignored. This is because there’s no `yield` statement until the first `yield` statement ?

Our execution suspends at `B` waiting for a value to be filled to `yield`.

#### Next next (3)

On the next executions of `next` our generator will run the code until the next `yield`.

In our case, it logs the value that is got through `yield` (i.e. `Got: foo`) and it gets suspended again on `yield`.

### Use Cases

![Image](https://cdn-media-1.freecodecamp.org/images/1*OiK88NOSMsbrlpWdDarvlg.gif)

#### Implement Iterables

Because **generators are an iterable implementation**, when created we get an iterable object, where each `yield` represents the value to emitted on each iteration. This description allow us to use generators to create iterables.

The following example represents a generator as iterable that iterates over even numbers until `max` is reached. Because our generator returns an iterable we can use `for-of` to iterate over the values.

It’s useful to remember that `yield` pauses the generator’s execution, and on each iteration the generator resumes from where it was paused.

#### Asynchronous Code

We can use generators to better work with async code, such as `promises`.

This use case it a good introduction to the new `async/await` on ES8.

Next is an example of fetching a JSON file with `promises` as we know it. We will use [Jake Archibald](https://twitter.com/jaffathecake) example on [developers.google.com](https://developers.google.com/web/fundamentals/getting-started/primers/promises).

Using [co library](https://github.com/tj/co) and a generator our code will look more like synchronous code.

As for the new `async/await` our code will look a lot like our previous version.

### Conclusion

This is schema, made by [Axel Rauschmayer](https://twitter.com/rauschma) on [Exploring ES6](http://exploringjs.com/es6/index.html) show us how generators relate with iterators.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XBMTOSxCUQ6MloksmDYdJw.png)

Generators are an implementation of iterables and follow the `iterable` and `iterator` protocol. Therefore they can be used to build iterables.

The most amazing thing about generators is their ability to suspend their execution. For this ES6 brings a new statement called `yield`.

However, calling a generator inside a generator is not as easy as executing the generator function. For that, ES6 has `yield*`.

> **Generators are the next step to bring asynchronous development close to synchronous.**

### Thanks to ?

* [Axel Rauschmayer](https://twitter.com/rauschma) for his [Exploring ES6 — Generators](http://exploringjs.com/es6/ch_generators.html)
* [Nicolás Bevacqua](https://twitter.com/nzgb) for his [PonyFoo — ES6 Generators in Depth](https://ponyfoo.com/articles/es6-generators-in-depth)
* [Jake Archibald](https://twitter.com/jaffathecake) for his promises example on [developers.google.com](https://developers.google.com/web/fundamentals/getting-started/primers/promises)
* To all [Regular Show](https://www.youtube.com/watch?v=n_OC-RAm7Qs) fans

_Be sure to check out my other articles on ES6_

[**Demystifying ES6 Iterables & Iterators**](https://medium.freecodecamp.com/demystifying-es6-iterables-iterators-4bdd0b084082)  
[_Let’s demystify JavaScript new way to interact with data structures._medium.freecodecamp.com](https://medium.freecodecamp.com/demystifying-es6-iterables-iterators-4bdd0b084082)

