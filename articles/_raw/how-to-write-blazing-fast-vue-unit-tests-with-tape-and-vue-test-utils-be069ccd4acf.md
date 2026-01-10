---
title: Write blazing fast Vue unit tests with Tape and Vue Test Utils
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-01T19:59:38.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-blazing-fast-vue-unit-tests-with-tape-and-vue-test-utils-be069ccd4acf
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XgAqbm90jYFUxWA-8Z0zOw.png
tags:
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: Testing
  slug: testing
- name: Vue.js
  slug: vuejs
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Edd Yerburgh

  Tape is the fastest framework for unit testing Vue components.

  In this article, we’ll see how to write Vue unit tests with Tape and Vue Test Utils.

  This tutorial is for users familiar with unit testing. If you’re new to unit testing
  c...'
---

By Edd Yerburgh

Tape is the fastest framework for [unit testing](https://github.com/eddyerburgh/vue-unit-test-perf-comparison) Vue components.

In this article, we’ll see how to write Vue unit tests with Tape and Vue Test Utils.

This tutorial is for users familiar with unit testing. If you’re new to unit testing check out [unit testing Vue components](https://eddyerburgh.me/unit-test-vue-components-beginners) for beginners.

### What is Tape?

Tape is a bare bones unit test framework that outputs the test report in [TAP](https://testanything.org/) (Test Anything Protocol) format.

It’s got a simple API to assert that your JavaScript and Vue components are behaving correctly.

### Why Tape?

A couple weeks ago I ran some performance tests on different testing frameworks. I wanted to find out which framework was the fastest for testing Vue SFCs (Single File Components).

I added Tape for completeness sake, and was shocked to find it was the fastest performing framework.

To run tests in Tape, we need to do some setup. Let’s dive right in.

### Bootstrapping the project

I’ve made a simple starter project to start with. Git clone the project into a directory:

```
git clone https://github.com/eddyerburgh/jest-vue-starter.git
```

`cd` into it and install the dependencies:

```
cd jest-vue-starter && npm install
```

Run the dev server as `npm run dev` to check out the app.

It’s pretty simple. The the main point of this tutorial is to see how to set up Tape and Vue, not to write complex tests.

### Setting up Tape and Vue Test Utils

First thing to do is install Tape and Vue Test Utils:

```
npm install --save-dev tape @vue/test-utils
```

**Vue Test Utils is in beta, so we need to request the version explicitly**

Vue Test Utils needs a browser environment to run. This doesn’t mean we need to run the tests in a browser (thank fully!).

We can use jsdom to set up a browser environment in Node. It adds global variables like `document` and `window` to Node.

jsdom is a bit of a pain to setup. Luckily some enterprising node developer made a wrapper library called `browser-env`.

```
npm install --save-dev browser-env
```

We need to run `browser-env` before the tests. Tape lets us define files to run before the tests, we’ll do that in a sec.

Vue SFCs need to be compiled before they’re tested. We can use `**require-hooks**` to run WebPack on files when they’re required in Node. It’s a simple setup.

First, install `require-extension-hooks` and its variants:

```
npm install --save-dev require-extension-hooks require-extension-hooks-babel require-extension-hooks-vue
```

Let’s make that setup file I spoke about earlier. Create a `test` directory, and add a `setup.js` file. The final path will be `test/setup.js`.

We’re nearly there. Crazy stuff.

Let’s write a smoke test in Tape. Create a new file called `List.spec.js` in the test directory. Full path `test/List.spec.js`. Copy the test below into the file:

What’s going on there? We define a `test`, and get a `t` object in the callback. The `t` object contains assertion methods. It also has a `plan` method . We need to tell Tape how many tests it should expect.

Now we need a script to run the tests. Open the `package.json` and add this script:

```
"unit": "tape ./test/specs/*.spec.js -r ./test/setup.js"
```

This tells tape to run all `.spec` files in `test/specs`. The `-r` tells Tape to `require` or run `test/setup` before running our tests.

Run the `unit` tests:

```
npm run unit
```

Yay, we have a passing test. But hoo boy—that’s some ugly test output ☹️

Remember I mentioned TAP earlier? This is TAP in it’s naked glory. Pretty ugly right? Don’t worry, we can prettify it.

Install `tap-spec`:

```
npm install --save-dev tap-spec
```

We can pipe our TAP output from Tape. Edit the `unit` script to pipe the output to `tap-spec`:

```
"unit": "tape ./test/specs/*.spec.js -r ./test/setup.js | tap-spec"
```

And run the tests again:

```
npm run unit
```

Much better ?

### Writing tests with Tape and Vue Test Utils

Let’s write some tests then. Since we’re using Vue Test Utils, the tests are pretty readable.

In `List.spec.js`, we’re going to write a `test` that passes an `items` array to `List`. We’ll use the `[shallow](https://github.com/vuejs/vue-test-utils/blob/dev/docs/en/api/shallow.md)` method from Vue Test Utils to shallow mount the component. `shallow` returns a `wrapper` containing the mounted component. We can use `[findAll](https://github.com/vuejs/vue-test-utils/blob/dev/docs/en/api/wrapper/findAll.md)` to search the render tree for`<`li> tags, and check how many there are.

Copy the test from below into `test/specs/List.spec.js`.

Watch the tests pass with `npm run unit`. Notice we have a custom error message for out `t.equals` assertion. The default messages aren’t very readable, so it’s better to add our own.

Now add a new file `test/specs/MessageToggle.spec.js`. In here we’ll write a test for, you guessed it, `MessageToggle.vue`.

We’re going to write two tests now. One will check the `<`;p> tag renders a default message. We’l`l use s`hallow again to get a wrapper containing the mounted component, and us`e th`e text method to return the text insid`e t`he <p> tag.

The second test is similar. We’ll assert that the message changes when the `toggle-message` button is pressed. To do that, we can use the `[trigger](https://github.com/vuejs/vue-test-utils/blob/dev/docs/en/api/wrapper/trigger.md)` method.

Copy the code below into `test/specs/MessageToggle.spec.js`:

Run the tests again with `npm run unit`. Woop—green tests ?

### Pros and cons of Tape

Now we’ve added some tests, let’s look at the pros and cons of using Tape.

#### Pros

* **It’s fast**  
 Like really fast ?
* **It’s simple**  
 You can read the source code to
* **It uses TAP**.   
Because TAP is a standard, there are lots of programs that work directly with TAP  
Like the tap-spec module, we just piped some TAP text into it and it prettified it for us
* **Limited assertions**  
 Limited assertions keep your assertions easy to understand

#### Cons

* **Limited assertions**  
 This is a con too  
You can get useful error messages with assertions like `hasBeenCalledWith`, this is difficult to replicate with `t.equal`
* [It breaks](https://github.com/substack/tape/issues/389)  
When you run more than 10000 tests  
You probably won’t hit that. But it might be a deal breaker for a large Vue project
* **It’s basic**  
 You’ll need to use other libraries for mocking, stubbing and faking

The pros and cons are pretty similar. Tape is basic, and that can be a good thing or a bad thing depending on who you ask.

Most importantly though, it’s blazing fast!

Fast unit tests are good unit tests.

### Call to action

The best way to work out a new test framework is to use it.

On the next Vue project you start, try Tape. You can find a list of assertions on the Tape [README](https://github.com/substack/tape/).

Enjoy ?

You can find [the finished repo](https://github.com/eddyerburgh/tape-vue-example) on GitHub.

