---
title: How to write more powerful unit tests by using value assertions
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-05T11:26:29.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-powerful-unit-tests-using-value-assertions-3de5146c0088
coverImage: https://cdn-media-1.freecodecamp.org/images/1*kmxDhQcCfG3cuel6qBz2Iw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Edd Yerburgh

  Unit tests are awesome. Writing unit tests reduces bugs by 40–80%.

  But you need to do them right. Poorly written unit tests can suffocate a codebase,
  and cause more problems than they solve.

  One way to improve your unit tests is to us...'
---

By Edd Yerburgh

Unit tests are awesome. Writing unit tests [reduces bugs by 40–80%](https://www.computer.org/csdl/mags/so/2007/03/s3024.pdf).

But you need to do them right. Poorly written unit tests can suffocate a codebase, and cause more problems than they solve.

One way to improve your unit tests is to use **value assertions**.

In this article we’ll look at what value assertions are, and how to use them to improve your tests.

### Understanding assertions

Assertions are functions that check to make sure the code behaved as we expected.

Different languages have different conventions. In JavaScript, it’s common to follow the `expect` pattern. This is where you `expect` a condition to match a value.

We combine the `expect` function with another function called a **matcher**.

In the example below, we `expect` the result of `sum(1,1)` to equal `2`. The `toBe` matcher checks that the expect value equals `2`.

```
expect(sum(1,1)).toBe(2)
```

If the result of `sum(1,1)` equals `2`, the function won’t do anything and the test will pass. If `sum(1,1)` doesn’t equal `2`, the function throws an **assertion error** and the test fails.

### Debugging assertion errors

In test frameworks, assertion errors are formatted to make the message easier to read. Assertion errors let you figure out quickly what went wrong in the test.

You can see a failing [Jest](https://facebook.github.io/jest/) assertion error below:

![Image](https://cdn-media-1.freecodecamp.org/images/-2e06m0DKQjtjvDUzRoGmkv60nm0HE8YiHFU)
_A Jest assertion error_

For some reason, `sum(1,1)` returned `3`.

If we check the code, we’ll find someone accidentally added `b` twice:

```
function sum(a,b) {  return a + b + b}
```

We can fix the error quickly and get the `sum` function working again. The assertion error helped us figure out what went wrong and where.

### What’s a value assertion?

A value assertion is **an assertion that compares two values**.

We just wrote a value assertion:

```
expect(sum(1,1)).toBe(2)
```

And it generated the assertion error:

```
Expected value to be (using ===): 2 Received: 3
```

### What other assertions are there?

Another common assertion is a **boolean assertion**.

A boolean assertion is **an assertion that compares two booleans.**

```
expect(add(1,1) === 2).toBe(true)
```

This generates a boolean assertion error:

```
Expected value to be (using ===): true Received: false
```

### Debugging a value assertion

Value assertions throw descriptive assertion errors.

When a test fails with a value assertion, you can see why the test is failing. This gives us a clue to what is happening in the code:

```
warning: expected 'somevalue' to equal 'some value'
```

You know what to look for in the code when you see an error like this. Oh, it looks like someone deleted a space by accident.

Value assertions improve the debuggability (yes that’s a word) of unit tests. From reading the assertion error, you can see what went wrong in the test.

Let’s look at an assertion error from a boolean assertion:

![Image](https://cdn-media-1.freecodecamp.org/images/fyKQxgYRoihV-B-hRLYOIVVzYhAromkgOkAn)
_A Jest boolean assertion error_

What’s gone wrong?

It takes longer to debug a test with a boolean assertion, because you don’t know what value was returned by the tested code.

This makes boolean assertion errors pretty useless in unit tests.

### Writing value assertions

So we want to write value assertions.

Most JavaScript testing libraries provide functions to write value assertions.

Jest contains tons of [useful matchers](https://facebook.github.io/jest/docs/en/expect.html) to create value assertions:

```
.toBeGreaterThan(number).toContain(item).toHaveBeenCalled().toHaveProperty(keyPath, value)
```

### Call to action

Now you understand the power of value assertions, your tests will improve.

Get out there and write some debuggable unit tests!

If you enjoyed this article, please give me some claps so more people see it. Thanks!

