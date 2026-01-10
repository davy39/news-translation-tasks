---
title: Want your tests to be more effective? Write your specifications like this.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-29T16:13:06.000Z'
originalURL: https://freecodecamp.org/news/want-your-tests-to-be-more-effective-write-your-specifications-like-this-5d701a961e35
coverImage: https://cdn-media-1.freecodecamp.org/images/1*eDyt0mtmMAYoUOF0SaA0eA.jpeg
tags:
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Edd Yerburgh

  Writing test specifications is tricky. If you get it right, your tests are easy
  to understand and debug. But get it wrong, and your tests will be confuse people
  more than they’ll help them.

  In this article, I’ll show you how to write ...'
---

By Edd Yerburgh

Writing test specifications is tricky. If you get it right, your tests are easy to understand and debug. But get it wrong, and your tests will be confuse people more than they’ll help them.

In this article, I’ll show you how to write expressive test specifications.

### What are test specifications?

Test specifications (specs) are the string used to identify tests when they’re run by a test runner.

Below you can see an example of the output from a failed test. You can see where the specification and assertion error is used to describe how a test failed.

![Image](https://cdn-media-1.freecodecamp.org/images/PAT9zMtLMXDy-Pphm43EbKfAVIIYX6d7uJLL)
_Console output from a failed test using the specification and assertion error_

### Why are test specifications important?

When a test fails, the way you identify it is with the test specification.

If the specification is well-written, you’ll know straight away why the test failed by using the test specification and the [test assertion](https://medium.freecodecamp.org/how-to-write-powerful-unit-tests-using-value-assertions-3de5146c0088).

```
calls showModal when button is clickedError: Expected spy to have been called but it was not. 
```

We can guess that the test failed because showModal wasn’t called when the button was clicked. This debugability is what you should aim for in tests.

Lets look at some rules to help write spectacular test specifications.

### The Goldilocks rule

You should follow the Goldilocks rule for test specifications—not too general and not too specific.

For example, `does what I expect` is too general. You won’t know why the test failed or what the test was checking.

At the same time, you need to avoid being too specific. Instead of using`adds cache-control none header and vary Lang header`, use a less narrow specification, like `adds correct headers` .

A failing test has two parts. The test specification, and the error message.

```
adds correct headers Error: Expected something to equal none
```

Your test name should tell us what is happening. But it doesn't need to give us every detail. The [assertion error](https://medium.freecodecamp.org/how-to-write-powerful-unit-tests-using-value-assertions-3de5146c0088) should include a value that compliments the test specification.

### Keep them short

Specifications should be short.

My rule of thumb is that they shouldn’t be longer than 150 characters.

If your tests are more than 150 characters, there’s a chance that your units are too complex. Either rewrite the spec to be shorter, or break out the functionality of your units into smaller chunks.

### Write in the present tense

Your test specs should be in the present tense.

For example, `calls toggleModal when button is clicked` , not `will call toggleModal when button is clicked` .

Specifications are statements of how your unit behaves: `returns sum of input` .

Writing in the present tense makes your specifications shorter and easier to read.

### Focus on output and input

Tests should trigger an input and expect an output.

Your specifications should follow this pattern—**output when input**. For example `calls toggleModal when button is clicked` , or `returns true when called with string` .

Keeping to this standard ensures your tests focus on output and input.

### Be concise

You don’t have much space in test specs, so stay away from unnecessary words.

For example, don’t add filler words like should, or will.

`should call showmodal when clicked` ❌

`will call show modal when clicked` ❌

`calls show modal when clicked` ✅

### Don’t use nested describe blocks

A lot of Javascript testing libraries include a feature called `describe` blocks.

`describe` blocks define sections in your tests.

A describe block like the one below:

```
describe('sum', () => {  test('returns sum of input', () => {    expect(sum(1,2)).toBe(3)  })})
```

It creates the following console output:

![Image](https://cdn-media-1.freecodecamp.org/images/NO0xZZRWjaU9ERatYHwHtWvfVGi89wVmNKR9)
_The output using a sum describe block_

You should use describe blocks to define a test suite in a file.

Some developers nest describe blocks inside each other to organize their tests. Never do this.

Instead of writing tests like this:

```
describe('API', () => {  describe('/books', () => {    describe('/id', () => {      describe('not found', () => {        test('returns 404', () => {          expect(4).toBe(4)        })      })    })  })})
```

Write tests like this:

```
describe('API', () => {  test('returns 404 when /books/id is not found', () => {    expect(4).toBe(4)  })})
```

**Never nest describe blocks**. Maintaining twenty or thirty tests in files with nested describe blocks is really confusing. You waste time deciding what block a new test should go in, and it’s easy to accidentally delete a closing curly brace.

Nested describe blocks add unnecessary cognitive load.

### Write different specs for different types of tests

There are two types of test specifications you’ll write — **high-level specs**, and **developer-level specs**.

End to end tests need high-level specs. The actions that end to end tests perform are high-level, and the specification should match that.

High-level specifications are the kind of specs your manager might give you — `the modal opens when the user clicks a button`. You could show your manager the specs, and he’d understand what the test is for.

On the other hand, unit tests need developer-level specifications.

Unit tests check how functions in our code work. They’re low level, so the specifications should reflect that.

Developer-level specs only make sense to other developers, such as`button should trigger action with displayModal true when clicked`. They can mention concepts that don’t make sense to non-devs. They can use terms like `Boolean`, and `throws error`.

Think of unit tests as documentation for future developers, think of end to end tests as documentation for future project managers. And make sure your specifications reflect that.

### Call to action

Now that you know how to write high quality test specifications, go out and write some tests! If you don’t know how to write tests, the [getting started guide from Jest](https://facebook.github.io/jest/docs/en/getting-started.html) is a great place to start.

