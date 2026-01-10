---
title: 'Vue Test Utils and Jest: how to write simple unit tests for Vue components'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-08T13:24:32.000Z'
originalURL: https://freecodecamp.org/news/simple-unit-tests-with-vue-test-utils-and-jest-c384d7abc321
coverImage: https://cdn-media-1.freecodecamp.org/images/1*KlrR7EWfaDgtcW5hJGFjHQ.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: vue
  slug: vue
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Edd Yerburgh

  In this tutorial I’m going to show you how to test Vue components.

  We’re going to write unit tests and snapshot tests with Jest and Vue Test Utils.
  All without Webpack.

  This tutorial is for users familiar with unit testing. If you’re ...'
---

By Edd Yerburgh

In this tutorial I’m going to show you how to test Vue components.

We’re going to write unit tests and snapshot tests with Jest and Vue Test Utils. All without Webpack.

This tutorial is for users familiar with unit testing. If you’re new to unit testing check out my article on [unit testing Vue components for beginners](https://eddyerburgh.me/unit-test-vue-components-beginners).

### Setup

I’ve made [a simple starter project](https://github.com/eddyerburgh/vue-unit-test-starter/). Git clone it into a directory:

```
git clone https://github.com/eddyerburgh/vue-unit-test-starter.git
```

cd into it and install the dependencies:

```
cd vue-unit-test-starter && npm install
```

When the dependencies are installed, run the development server:

```
npm run dev
```

Now we can get back to the code.

One thing to talk about is aliases. Aliases are a way to use shorthand notation to import files. Instead of long import statements like the one below:

```
import someModule from '../../../../../src/components/someModule'
```

You can use a shorthand notation, or alias. a common alias is the `@` symbol, which resolves to the `src` directory:

```
import someModule from '@/components/someModule'
```

Note: You can set any alias you want, but the vue-cli projects use `@` to refer to the `src` directory.

In vue-cli projects, [Webpack is used to add the functionality](https://github.com/eddyerburgh/jest-vue-starter/blob/master/build/webpack.base.conf.js#L25). This is great, but we aren’t using Webpack to run our tests. We need another way to resolve aliases.

That’s where babel comes in. There’s a plugin — babel-plugin-module-resolver — that resolves aliases in babel. You can see it in the `.babelrc`. It’s only used in the test environment, because when you run the dev or production build, Webpack does the alias resolving.

Check out this file:

Ok, now you’ve got an overview of the project, it’s time to add Jest.

### Jest

Jest is a test framework. It’s one of [the fastest testing frameworks for Vue single file components](https://github.com/eddyerburgh/vue-unit-test-perf-comparison) (SFCs).

As well as running tests, Jest comes with a load of other features out the box, like mocks, code coverage and snapshot testing.

First thing to do is install Jest:

```
npm install --save-dev jest
```

To test SFCs, you need to compile them into JavaScript before you run the tests. If you try and run an uncompiled SFC, you’ll get a syntax error.

Jest doesn’t compile `.vue` files out the box. You need to tell it to compile them. You do this by adding a `jest` field to the `package.json`.

Add the code below to your `package.json`.

```
"jest": {    "moduleFileExtensions": [      "js",      "json",      "vue"    ],    "transform": {      "^.+\\.js$": "<rootDir>/node_modules/babel-jest",      ".*\\.(vue)$": "<rootDir>/node_modules/vue-jest"    }  }
```

You’ll see a `moduleFileExtensions` field. This tells Jest to run files with a `.vue` extension, as well as `.js` and .`json`.

There’s also a `transform` field. This tells Jest how to compile files before running them. It matches all `.js` files, and compiles with babel-jest. All .vue files are compiled with vue-jest.

These are custom transforms built for Jest. babel-jest, compiles JavaScript. vue-jest takes `.vue` files and compiles them into JavaScript.

You need to install both packages:

```
npm install --save-dev babel-jest vue-jest
```

Ok cool, now you should add a smoke test, to make sure everything’s working.

In `src/components` create a `__tests__` directory. Add a `MessageToggle.spec.js` file. So the full file path will be `src/components/__tests__/MessageToggle.spec.js`.

Copy the code below into the file:

Jest runs all `.js` files in `__tests__` directory automatically. It even adds a test environment variable, so all your test script does is run Jest.

In the `scripts` field of your `package.json` add the `unit` script:

```
"unit": "jest"
```

Now run the script:

```
npm run unit
```

Great, first passing test ?.

Now you’re going to write more complicated tests using Vue Test Utils.

### Vue Test Utils

[Vue Test Utils](https://github.com/vuejs/vue-test-utils/) is in beta at the moment, but you can use it now without a problem. The API is pretty much finalized.

Install it:

```
npm install --save-dev @vue/test-utils
```

Now you’re going to replace the test in `MessageToggle.spec.js` with tests using Vue Test Utils.

Copy the code below into `src/components/__tests__/MessageToggle.spec.js`

Here, we can use the `[mount](https://github.com/vuejs/vue-test-utils/blob/dev/docs/en/api/mount.md)` function to return a wrapper object. the wrapper contains some helper methods, like `text`, that help assert components. You can see a full list in [the docs](https://github.com/vuejs/vue-test-utils/tree/dev/docs/en/api/wrapper).

Ok, let’s add a more complicated test that performs an action on the `Messagetoggle` component. Copy the code below into `MessageToggle.spec.js`:

This time, we’re clicking a button (`#toggle-message`) in `MessageToggle` and checking that the `<`;p> tag text has changed correctly.

Now run the test script:

```
npm run unit
```

Woop, passing tests! ?

Vue Test Utils abstracts away the Vue internals. So all you need to do is learn the Vue Test Utils API.

Now you’re going to write a test for the List component. The List component takes props, luckily Vue Test Utils gives us a way to pass props when mounting the component.

Create a file `/src/components/__tests__/List.spec.js`, and paste in the code below

This time you’ll notice we use the `shallow` function. This is the same as `mount`, except it only renders the component one level deep. Generally, it’s best to use shallow.

Now you’ve written some unit tests, it’s time to look at snapshot testing.

### Snapshot testing

Jest has this great feature called snapshot testing.

Snapshot testing basically takes a copy of your component tree as a string, and then compares against it each time you run your tests. If the rendered component HTML changes, the test fails.

Let’s add a snapshot test to `Messag.spec.js`.

You need to render the component to a string using the vue-server-renderer. The string returned isn’t very pretty, so you should add jest-serializer-vue to prettify your snapshots.

```
npm install --save-dev vue-server-renderer jest-serializer-vue
```

You also need to tell Jest to use the serializer. Add a `snapshotSerializers` field inside the `jest` field in your`package.json`:

```
"snapshotSerializers": [    "<rootDir>/node_modules/jest-serializer-vue"]
```

Now update List.spec.js to include a snapshot test:

This test shallow mounts the component, and renders it to an HTML string with vue-server-renderer.

Now run your tests:

```
npm run unit
```

You’ll see some new output about a snapshot being saved. go have a look in `src/components/__tests__/__snapshots__/List.spec.js.snap`:

```
// Jest Snapshot v1, https://goo.gl/fbAQLP
```

```
exports[`List.vue has same HTML structure 1`] = `<ul>    <li>        list item one    </li>    <li>        list item two    </li></ul>`;
```

Cool, a snapshot. ?

Now if the markup of `List.vue` changes, Jest will warn you the snapshot changed when you run your tests.

### Conclusion

Now you’ve set up unit tests and snapshot tests with Jest and Vue Test Utils.

I skipped over a few concepts. You can look at the [finished repository on GitHub](https://github.com/eddyerburgh/jest-vue-example) if your project didn’t work correctly.

Jest has [loads more features](https://facebook.github.io/jest/) to make testing easier.

Vue Test Utils also has a lot more methods — [check out the docs](https://github.com/vuejs/vue-test-utils/tree/dev/docs/en).

Unit testing Vue components has never been easier, so get out there and write some tests!

If you learned something from this article, share and give a ? to get the word out!

