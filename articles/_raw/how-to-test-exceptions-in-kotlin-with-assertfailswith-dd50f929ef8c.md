---
title: How to test exceptions in Kotlin with assertFailsWith
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-26T18:40:05.000Z'
originalURL: https://freecodecamp.org/news/how-to-test-exceptions-in-kotlin-with-assertfailswith-dd50f929ef8c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*97MX1nM7-TWatCX9pbU-Kw.png
tags:
- name: Kotlin
  slug: kotlin
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Testing
  slug: testing
seo_title: null
seo_desc: 'By Daniel Newton

  I wanted to write this short post to highlight the assertFailsWith function available
  to Kotlin. This function makes testing exceptions a bit easier. Testing exceptions
  isn’t something fancy or new to JVM languages (from now on I wil...'
---

By Daniel Newton

I wanted to write this short post to highlight the `assertFailsWith` function available to Kotlin. This function makes testing exceptions a bit easier. Testing exceptions isn’t something fancy or new to JVM languages (from now on I will use Java for comparisons). Kotlin comes with the nice extra benefit of providing this functionality as part of its standard library. Comparing this to Java, you are likely to bring [AssertJ](http://joel-costigliola.github.io/assertj/) into the mix to achieve similar results.

The main purpose of this post is to make you aware of the `assertFailsWith` function. I personally did not know it existed for a while and defaulted to depending on AssertJ. Not that I have anything against AssertJ, that is. There are many other features that the library provides. For this specific instance, it might be possible to remove it (assuming you are not using it for anything else).

What is good about `assertFailsWith` and AssertJ in general? It provides better exception testing than the simple constructs that JUnit provides. More precisely, it allows you to specify which part of your test that you expect an exception to be thrown, instead of declaring that an exception will arise somewhere in the code. This could lead to exceptions being incorrectly swallowed by test at an incorrect point and tricking you into thinking it is working as you think it should.

Now I have that brief point out of the way, let's get on with the main content of this post. Below is what `assertFailsWith` looks like inside a test:

In this example, `hereIsAnException` is placed inside the body of `assertFailsWith`, who checks that an `IllegalArgumentException` is thrown. If one is not raised, then the assertion will fail. If one does occur, then the assertion will pass and the exception is caught.

Catching the exception allows the execution of the test code to continue if needed as well as allowing you to make further assertions on the state of the exception.

For example, is it a wrapper around another exception (what is the type of its `cause` property)?

Is the message what you expect (not the most sturdy of checks)?

Only exceptions that are of the same type or subtype as specified by `assertFailsWith` will be caught. Any others will cause the test to fail. Since it catches subtypes, please don’t go around just specifying `Exception` or `RuntimeException`. Try to be precise so your tests are as useful as possible.

As touched on earlier, `assertFailsWith` will only catch an exception that is thrown within the body of the function. Therefore if this was written instead:

The test would fail. `hereIsAnException` has thrown an exception, which has not been caught and leads to the test failing. I believe this is the best part of this sort of function over the previous ways this used to be done (e.g. asserting inside `@Test` that an exception would occur).

I personally have never really used the message part of an assertion. Maybe you do, so, I thought I’d at least let you know.

Before I wrap up the little amount of content in this post, let's have a quick look at AssertJ so that we can draw a comparison between the two. Again, this is only for the case of catching exceptions which is only a small part of what AssertJ provides.

This is slightly more “verbose” than the `assertFailsWith` version. But, that is made up for with the plethora of functions that AssertJ provides that makes any further checking of the returned exception much easier. More precisely, when using `assertFailsWith` I needed to write another assertion to check the message. In AssertJ this is just a function chained onto the end of the previous call.

To conclude, `assertFailsWith` is a nice little function to use in testing to ensure that a piece of code throws a specific type of exception. It is built into the Kotlin standard library which removes the need to bring in an extra dependency to your project. That being said, it is a relatively simple function and does not bring the sort of functionality that a library like AssertJ would. It is likely to suffice until you want to write tests that contain a wide range or assertions as this is the point where it can get messy.

The official docs for `assertFailsWith` can be found here if you are interested [Kotlin Docs – assertFailsWith](https://kotlinlang.org/api/latest/kotlin.test/kotlin.test/assert-fails-with.html).

If you found this post helpful, you can follow me on Twitter at [@LankyDanDev](https://twitter.com/LankyDanDev) to keep up with my new posts.

[View all posts by Dan Newton](https://lankydanblog.com/author/danknewton/)

_Originally published at [lankydanblog.com](https://lankydanblog.com/2019/01/26/testing-exceptions-in-kotlin-with-assertfailswith/) on January 26, 2019._

