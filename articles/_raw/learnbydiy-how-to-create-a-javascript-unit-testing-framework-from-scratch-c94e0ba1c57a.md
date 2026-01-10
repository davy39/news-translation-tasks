---
title: '#LearnByDIY - How to create a JavaScript unit testing framework from scratch'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-09T03:01:20.000Z'
originalURL: https://freecodecamp.org/news/learnbydiy-how-to-create-a-javascript-unit-testing-framework-from-scratch-c94e0ba1c57a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*cedi3xCR8cINoPAje7Nrjw.jpeg
tags:
- name: DIY
  slug: diy
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Testing
  slug: testing
seo_title: null
seo_desc: 'By Alcides Queiroz

  I promise, this is gonna be fun. =)

  Probably, automated tests are part of your daily routine (if not, please stop reading
  this article and start from the beginning, by learning from the father of TDD himself).
  You’ve been using tes...'
---

By Alcides Queiroz

I promise, this is gonna be fun. =)

Probably, automated tests are part of your daily routine (if not, please stop reading this article and [start from the beginning](https://www.amazon.com/Test-Driven-Development-By-Example/dp/0321146530), by learning from the father of TDD himself). You’ve been using testing frameworks such as [Node-tap](https://www.node-tap.org/) (or [Tape](https://github.com/substack/tape)), [Jasmine](https://jasmine.github.io/), [Mocha](https://mochajs.org/) or [QUnit](https://qunitjs.com/) for quite a while, just accepting that they do some magic stuff and not asking too many questions about them. Or, if you’re like me, maybe you’re always curious about how things work, including testing frameworks, of course.

This article will guide you through the process of creating a JavaScript testing framework from scratch, with a pretty decent DSL and a nicely detailed output. This is the first article in my **#LearnByDIY** series. The idea is to demystify certain kinds of software that we’re used to, by creating simpler versions of them.

#### Disclaimers

Before starting, some important notes:

* The goal of this article is **not** to create a production-ready tool. Please, **don’t use the framework that we’ll be creating to test production code.** Its purpose is purely educational. =)
* Naturally, our little framework won’t be full-featured. Things such as async tests, parallel executions, a richer set of matchers, a CLI (with options like `--watch`), pluggable reporters and DSLs, etc., won’t be present in our final version. However, I **strongly recommend** that you keep toying with this project and maybe try to **implement some of these missing parts**. Perhaps you can transform it into a serious open source project. I’d love to know that this toy project became an “actual” testing framework.

### ⚔️ Tyrion - A tiny testing framework

Our framework will be tiny, but “brave” for its size. So, there’s no better name than Tyrion (yeap, he’s my favorite GoT character, too).

![Image](https://cdn-media-1.freecodecamp.org/images/1*cedi3xCR8cINoPAje7Nrjw.jpeg)
_Tyrion is small, but brave._

We’ll be using Node.js in this project, with good and old CommonJS modules. The minimum Node version you’ll need is v8.6.0. If you have an older version, please update it.

Oh, I almost forgot… I’m using [Yarn](https://yarnpkg.com/lang/en/docs/install/) throughout this article, for things like `yarn init`, `yarn link` and so on, but you can use “vanilla” NPM in a similar manner (`npm init`, `npm link`, …).

#### Creating the project folder structure

First, let’s create the following folder structure:

```
tyrion/||______ proj/|      ||      |______ src/||______ playground/       |       |______ src/       |______ tests/
```

In other “words”:

```
$ mkdir -p tyrion/proj/src tyrion/playground/src tyrion/playground/tests
```

We need two folders, each one to a separate project.

* The `proj` folder will contain the Tyrion framework package.
* The `playground` folder will contain a disposable Node project for playing with our framework. It will serve as a lab during our development process.

#### Initializing the Node projects

Go to the `playground` folder and run `yarn init -y`. This command generates a basic package.json file. Open it, remove the `"main": "index.js",` line, and add a “scripts” entry like the one in the example below:

```
{  "name": "playground",  "version": "1.0.0",  "scripts": {    "test": "node tests"  },  "license": "MIT"}
```

After creating this file, let’s do the same for the other project, the Tyrion package itself. In the `proj` folder, run `yarn init`. It will prompt you for some information to properly create the package.json file. Enter the following values (in bold):

```
question name (proj): tyrion <enter>question version (1.0.0): <enter>question description: <enter>question entry point (index.js): src/index.js <enter>question repository url: <enter>question author: <enter>question license (MIT): <enter>question private: <enter>
```

Now, we need to install Tyrion as a development dependency in our playground project. If it was a published package, we’d just need to install it directly, through `npm i --dev` or `yarn add --dev`. As we only have Tyrion locally, this is not possible. Luckily, both Yarn and NPM have a feature to help developers during this package “inception” phase, allowing us to simulate a link between two packages (one as a dependency of the other).

To create this dependency link, go to the `proj` folder and run:

```
$ yarn link
```

Then, in the `playground folder`, run:

```
$ yarn link tyrion 
```

That’s all. Now Tyrion is a dependency of the playground project.

#### Creating some modules to be our “guinea pigs”

In the `playground/src` folder, let’s create two modules to be tested by Tyrion:

#### Writing some tests

Now is the time to use our imagination. How should Tyrion’s DSL look? Are you sick of `expect`, `assert` , and so on? Let’s make it different, just for the fun of it. I suggest `guarantee` as our assertion function. Do you like it?

Let’s write a few tests to see it more clearly. Of course, nothing will work, since we didn’t implement anything in our framework.

And a `tests/index.js` file, to import our tests in only one place.

Tyrion will borrow one of Node-tap’s principles:

> **Test files should be “normal” programs that can be run directly.**

> That means that it can’t require a special runner that puts magic functions into a global space. `node test.js` is a perfectly ok way to run a test, and it ought to function exactly the same as when it’s run by the fancy runner with reporting and such. JavaScript tests should be JavaScript programs; not english-language poems with weird punctuation.

> [https://www.node-tap.org/#tutti-i-gusti-sono-gusti](https://www.node-tap.org/#tutti-i-gusti-sono-gusti).

As you might remember, in our playground’s package.json file, we have a `test` script which simply runs `node tests`. So, to execute it, just type `npm test` and hit enter. Yeap, do it. Let’s see it crashing:

![Image](https://cdn-media-1.freecodecamp.org/images/1*9h8lW-Kon3LuqlqQUI-0hA.png)

This error is clear. We don’t have anything in our framework. No module is being exported at all. To fix it, in the `proj` folder, create a `src/index.js` file exporting an empty object, as you can see below:

```
module.exports = {};
```

Now, we’ll run `npm test` again:

![Image](https://cdn-media-1.freecodecamp.org/images/1*ge5-uzTfUm-2bgrB8Gm3SQ.png)

Node is complaining because our `guarantee` function doesn’t exist. This is simple to fix, too:

```
const guarantee = () => {};
```

```
module.exports = { guarantee };
```

Run the test script again:

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZNsFSHaRf8JWCRake1fTNw.png)

Voilà! No errors, but nothing happens, either. =(

#### The guarantee function

Our assertion function should execute flawlessly if the supplied value is [_truthy_](https://developer.mozilla.org/en-US/docs/Glossary/Truthy), but should throw an error if it’s [_falsy_](https://developer.mozilla.org/en-US/docs/Glossary/Falsy).

Let’s implement it:

And to test if it works, let’s append another assertion to the end of our `number-utils.test.js` file:

```
guarantee(123 === 321); // This should fail 
```

Now run it once more:

![Image](https://cdn-media-1.freecodecamp.org/images/1*O8V_b4cKO7zxutYoLVuRdw.png)

A-ha! It works! It’s ugly, but it’s functional.

#### The check function

We need a way to wrap assertions into test units. Basically, all testing frameworks have this feature, like the `it` function in Jasmine or the `test` function in Node-tap.

In Tyrion, our test unit function will be called `check`. Its signature should be `check(testDescription, callback)`. We also want it to give us a friendlier output, describing the passing and failing tests.

This is what it will look like:

Now, we can rewrite our tests to use the new `check` function:

And re-run our test suite:

![Image](https://cdn-media-1.freecodecamp.org/images/1*CMuw0w6MzEfrKsyvR2QykQ.png)

Cool. But… what about some colors?? Wouldn’t it be a lot easier to distinguish between passing and failing tests?

Add the [colors](https://www.npmjs.com/package/colors) module as a dependency:

```
yarn add colors
```

So, import it at the top of the `proj/src/index.js` file:

```
const colors = require('colors');
```

And let’s put some colors in our output:

```
const check = (title, cb) => {  try{    cb();    console.log(`${' OK '.bgGreen.black} ${title.green}`);  } catch(e) {    console.log(`${' FAIL '.bgRed.black} ${title.red}`);    console.log(e.stack.red);  }};
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*D_Qp69Sx7kC5AfX2N9nfzg.png)

That’s better. =)

#### The xcheck function

It would be nice to have an easy way to disable a specific test, like the `xit` function in Jasmine. This can be easily implemented by creating a no-op function which just outputs that a test is disabled (well, it’s not completely no-op, but almost):

```
const xcheck = (title, cb) => {  console.log(`${' DISABLED '.bgWhite.black} ${title.gray}`);};
```

```
module.exports = { guarantee, check, xcheck };
```

So, import the `xcheck` function in the `number-utils.test.js` file and disable one of our tests:

```
const { guarantee, check, xcheck } = require('tyrion');const numberUtils = require('../src/number-utils');
```

```
// method: isPrimexcheck('returns true for prime numbers', () => {  guarantee(numberUtils.isPrime(2));  guarantee(numberUtils.isPrime(3));  guarantee(numberUtils.isPrime(5));  guarantee(numberUtils.isPrime(7));  guarantee(numberUtils.isPrime(23));});
```

And here’s how it behaves:

![Image](https://cdn-media-1.freecodecamp.org/images/1*kSCPsNlejl9OdZC8VUruyw.png)

#### Test summary and exit code

If we wanted to use Tyrion in a CI server, it would need to finish its process with different exit codes for error and success conditions.

Another desirable feature is a test summary. It would be nice to know how many tests passed, failed, or skipped (the disabled ones). For this, we could increment some counters in both `check` and `xcheck` functions.

We will create the `end` function, which prints the test summary and finishes with the appropriate exit code:

And don’t forget to call it in the `playground/tests/index.js` file:

```
const { end } = require('tyrion');
```

```
require('./string-utils.test');require('./number-utils.test');
```

```
end();
```

Or maybe:

```
const tyrion = require('tyrion');
```

```
require('./string-utils.test');require('./number-utils.test');
```

```
tyrion.end();
```

Now, let’s re-run `npm test`:

![Image](https://cdn-media-1.freecodecamp.org/images/1*MK7W8WxuDSD6grErVrSZKA.png)

Great, it works.

#### The group function

Many test frameworks have some way of grouping related tests. In Jasmine, for example, there is the `describe` function. We will implement a `group` function for this purpose:

And update our tests to use this new function:

Here’s the new output:

![Image](https://cdn-media-1.freecodecamp.org/images/1*8y2171rDoHbOhGMIt3myGw.png)

Well, the good news is that it works. The bad news is that it’s getting hard to understand. We need a way to indent this output in order to make it more readable:

Run it again:

![Image](https://cdn-media-1.freecodecamp.org/images/1*X1QQ7GuihVzZkFS6yQ91Jg.png)

That’s way better!

So, how does it work?

* The `repeat` function repeats a string `n` times.
* The `indent` function repeats an indent (of four spaces) `n` times by using the `repeat` function.
* The `indentLines` function indents a string with multiple lines by adding `n` indents to the beginning of each line. We’re using it to indent error stacks.
* The `indentLevel` variable is incremented at the beginning of each group execution and decremented at its end. This way, nested groups can be correctly indented.

#### More matchers

The `guarantee` function is not flexible enough for a lot of scenarios. We need a richer set of matchers in order to make our tests more meaningful.

First, create the `matchers` folder:

```
$ mkdir proj/src/matchers
```

Now, we’ll create each matcher in a separate file:

The `same` matcher uses the strict equality operator (===) to test if two arguments are exactly the same object (for reference types) or equal (for primitive types). It behaves similarly to the `toBe` matcher in Jasmine and `t.equal` in node-tap.

**Note:** Node-tap also has a matcher called `t.same`, but it works differently (it won’t verify if two objects are exactly the same, but if both are deeply equivalent).

The `identical` matcher verifies that two arguments are equivalent. It uses the `==` operator for comparing values.

The `deeplyIdentical` matcher does a deep comparison of two objects. This kind of comparison can be considerably complex, or at least too complex for this article’s purpose. So, let’s install an existing module to handle deep equality and use it in our matcher:

```
$ yarn add deep-equal
```

Then:

This is how an error will look:

![Image](https://cdn-media-1.freecodecamp.org/images/1*P3SI0UMJlXOusnB0A9yrNw.png)

The `falsy` matcher will fail if the supplied value is truthy.

The `truthy` matcher works in a similar manner to our `guarantee` function. It passes when the supplied value is truthy and breaks if it’s falsy.

The `throws` matcher will pass if a function throws an error. It’s possible to specify the wanted error message, but this is not mandatory.

An `index.js` file to re-export all matchers:

And finally let’s glue them all together:

You can use our new matchers this way:

```
const { guarantee, check } = require('tyrion');
```

```
check('playing with our new matchers', () => {  // The original guarantee function still works  guarantee(123 === 123);
```

```
  guarantee.truthy('abc');  guarantee.falsy(null);
```

```
  const a = { whatever: 777 };  const b = a;  guarantee.same(a, b);  guarantee.identical(undefined, null);
```

```
  const c = { whatever: { foo: { bar: 'baz' } } };  const d = Object.assign({}, c);  guarantee.deeplyIdentical(c, d);
```

```
  function boom() { throw new Error('Some error...'); }  guarantee.throws(boom);  guarantee.throws(boom, 'Some error...');});
```

#### The beforeEach function

To implement a `beforeEach` function, we need to use a stack to accumulate all `beforEach` callbacks. This is done for each new scoped level created every time a group is declared:

How does it work?

* Every time a group is declared, we’re pushing a new array to the `beforeEachStack` variable. This array will accumulate all `beforeEach` callbacks declared in that scope.
* After a group execution is completed, we remove the array at the top of our callbacks stack.
* The `beforeEach` function receives a callback and appends it to the array at the top of our callbacks stack.
* At the beginning of each `check` function, we’re calling every `beforeEach` callback in all levels of our stack.

#### The beforeAll function

Our last addition will be the `beforeAll` function. **For simplicity’s sake**, we’re assuming that calls to the `beforeAll` function will always be put before all groups and tests (**or**, when scoped within a group, at its very top).

Otherwise, if we wanted to ensure that the `beforeAll` function works correctly even in the middle or at the end of a group, we should dramatically change our existing logic. Well, we’re not going to do that, since it isn’t a rational usage of this function.

Our version of `beforeAll` will just receive a callback and immediately execute it.

```
const beforeAll = cb => cb();
```

```
module.exports = {   group, check, xcheck, guarantee, beforeAll, end };
```

An example of usage:

```
const { guarantee, check, group, beforeAll } = require('tyrion');
```

```
let a;beforeAll(() => {  a = { something: 'example' };});
```

```
group('playing with the beforeAll function', () => {  let b;  beforeAll(() => {    b = { something: 'example' };  });
```

```
  check('some test', () => {    guarantee.deeplyIdentical(a, b);  });
```

```
  check('another test', () => {    guarantee.identical(11, 11);  });});
```

#### The final version of Tyrion

It has been a long journey, but Tyrion is finally complete. =)

I added a SILENT option which disables logging. It’s being used to make it easier to test Tyrion (yep, testing frameworks need to be tested too).

The complete project is available [here](https://www.github.com/alcidesqueiroz/tyrion).

#### Possible improvements

Tyrion lacks many features, like:

* Support for async tests
* Parallel execution of tests
* `afterEach` and `afterAll` functions
* A `xgroup` function, which disables an entire group
* A function similar to [Jasmine’s fit](https://jasmine.github.io/api/edge/global.html#fit)
* Spies
* Decoupling DSL from reporting logic.
* Pluggable reporters
* A terminal CLI (with a `--watch` option)
* Yet more matchers
* Friendlier error stacks

I encourage you to keep playing with this project. Feel free to use and expand it. Please let me know your thoughts, suggestions, and experiments by leaving a comment below. =)

