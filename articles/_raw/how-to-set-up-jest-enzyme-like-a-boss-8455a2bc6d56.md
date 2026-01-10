---
title: How to set up Jest & Enzyme like a boss
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-12T18:00:01.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-jest-enzyme-like-a-boss-8455a2bc6d56
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tozYeK-3Cjp7xjBAJE0FeQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: unit testing
  slug: unit-testing
seo_title: null
seo_desc: 'By Adeel Imran


  _Photo by [Unsplash](https://unsplash.com/@quinoal?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit">Quino
  Al / <a href="https://unsplash.com/?utm_source=ghost&utm_medium=referral&utmcampaign=api-credit)

  When I started out...'
---

By Adeel Imran

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-249.png)
_Photo by [Unsplash](https://unsplash.com/@quinoal?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Quino Al</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

When I started out writing tests for my React application, it took me some tries before I figured out how to set up my testing environment using `Jest` & `Enzyme`. This tutorial assumes that you already have a React application set up with `webpack` & `babel`. We’ll continue from there.

This is part of a series of articles I have written. I talk about how to set up a React application for production the right and easy way.

* **Part 1** [How to combine Webpack 4 and Babel 7 to create a fantastic React app](https://medium.freecodecamp.org/how-to-combine-webpack-4-and-babel-7-to-create-a-fantastic-react-app-845797e036ff) (Talks about setting up webpack with babel, along with .scss support)
* **Part 2** [These tools will help you write clean code](https://medium.freecodecamp.org/these-tools-will-help-you-write-clean-code-da4b5401f68e) (Talks about automating your code, so all code you write is good code)
* This is **Part 3** in which I will talk about setting up Jest with Enzyme.

Before we begin, if at any time you feel stuck please feel free to check the [**code repository**](https://github.com/adeelibr/react-starter-kit). PR’s are most welcome if you feel things can be improved.

### Prerequisite

You need to have Node installed in order to use npm (node package manager).

First things first, create a folder called `app` then open up your terminal and go into that `app` folder and type:

```
npm init -y
```

This will create a `package.json` file for you. In your `package.json` file add the following:

```json
{
  "name": "react-boiler-plate",
  "version": "1.0.0",
  "description": "A react boiler plate",
  "main": "src/index.js",
  "author": "Adeel Imran",
  "license": "MIT",
  "scripts": {
    "test": "jest",
    "test:watch": "jest --watch",
    "test:coverage": "jest --coverage --colors",
  },
  "devDependencies": {
    "@babel/core": "^7.0.0",
    "@babel/polyfill": "^7.0.0-beta.51",
    "@babel/preset-env": "^7.0.0-beta.51",
    "@babel/preset-react": "^7.0.0-beta.51",
    "babel-core": "^7.0.0-bridge.0",
    "babel-jest": "^23.4.2",
    "enzyme": "^3.3.0",
    "enzyme-adapter-react-16": "^1.1.1",
    "jest": "^23.4.2"
  }
}
```

Second create a folder called `src` in your `app` folder. `src/app/` folder is where all of your React code along with its test will reside. But before that let’s understand why we did what we did in our `package.json` file.

I’ll talk about the `scripts` in a bit (promise). But before that let’s learn why we need the following dependencies. I want you to know what goes inside your `package.json` So let’s start.

`@babel/core` Since generally we use webpack to compile our react code. Babel is a major dependency that helps tell webpack how to compile the code. This is a peer dependency for using Jest as well.

`@babel/polyfil` Jest requires a thing called `regenerator-runtime`, @babel/polyfill comes built-in with it and some other cool features.

`@babel/preset-env` & `@babel/preset-react` Is for features like ES6 and React, so while writing unit tests `Jest` knows about **ES6** syntax and **JSX.**

`babel-core` This is mostly a dependency for `Jest`, as we need `babel-core` for Jest to work.

`babel-jest` Will help Babel understand the code we write in `Jest`

`enzyme` This is an assertion library that makes it easier to assert, manipulate, and traverse your React Components’ output.

`enzyme-adapter-react-16` An adapter/middle-ware to help Jest connect with `enzyme`

`jest` Jest is the test library on which we will run our tests.

You can have a look at a very simple bare bone example by the cool folks at **jest.** It uses babel to run a simple test [**here**](https://github.com/facebook/jest/tree/master/examples/babel-7)**.**

Also if you want to [setup webpack for React](https://medium.freecodecamp.org/how-to-combine-webpack-4-and-babel-7-to-create-a-fantastic-react-app-845797e036ff), this is a detailed walkthrough on how I did it. Or you can simply go through the entire code base which uses the basic bare bones structure of what you will need when setting up your React application along with jest/enzyme ([**starter-kit here**](https://github.com/adeelibr/react-starter-kit)).

Next let’s create a file called `jest.config.js` in our main `app` folder and add the following code to it. I’ll talk about what this does in a bit.

```javascript
// For a detailed explanation regarding each configuration property, visit:
// https://jestjs.io/docs/en/configuration.html

module.exports = {
  // Automatically clear mock calls and instances between every test
  clearMocks: true,

  // An array of glob patterns indicating a set of files for which coverage information should be collected
  collectCoverageFrom: ['src/**/*.{js,jsx,mjs}'],

  // The directory where Jest should output its coverage files
  coverageDirectory: 'coverage',

  // An array of file extensions your modules use
  moduleFileExtensions: ['js', 'json', 'jsx'],

  // The paths to modules that run some code to configure or set up the testing environment before each test
  setupFiles: ['<rootDir>/enzyme.config.js'],

  // The test environment that will be used for testing
  testEnvironment: 'jsdom',

  // The glob patterns Jest uses to detect test files
  testMatch: ['**/__tests__/**/*.js?(x)', '**/?(*.)+(spec|test).js?(x)'],

  // An array of regexp pattern strings that are matched against all test paths, matched tests are skipped
  testPathIgnorePatterns: ['\\\\node_modules\\\\'],

  // This option sets the URL for the jsdom environment. It is reflected in properties such as location.href
  testURL: 'http://localhost',

  // An array of regexp pattern strings that are matched against all source file paths, matched files will skip transformation
  transformIgnorePatterns: ['<rootDir>/node_modules/'],
  
  // Indicates whether each individual test should be reported during the run
  verbose: false,
};
```

Second create a file called `enzyme.config.js` in your main `app` folder and add the following code to it.

```javascript
/** Used in jest.config.js */
import { configure } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';

configure({ adapter: new Adapter() });
```

Let’s first talk about `jest.config.js`

`clearMocks` will clear all mocks, so that the mock in `nth` test doesn’t mutate or affect the test at `n+1` position.

`collectCoverageFrom` tells jest to collect the code coverage from all the .js files in the `src/` folder. Coverage tells you what percentage of the code is being covered by your test cases.

`coverageDirectory` tells the Jest that the coverage directory should be named `coverage` in the main `app/` folder.

`moduleFileExtensions` takes in an array of extensions that tells Jest which files it can test. We tell it to test all .js|.jsx|.json files.

`setupFiles` this is really important, as it tells Jest the path from where it can get configurations for enzyme (more on this later)

`testEnvironment` specifies what environment Jest will run its test on, since we are testing a web application. I have set the environment to `jsdom`

`testMatch` tells Jest which files it will test. I pass in 2 configurations here, one being test all files in any folder named `__tests__` or test all files that end with `spec.js|.jsx` or `test.js|.jsx`

`testPathIgnorePatterns` I don’t want Jest to run tests inside my `node_modules` folder. So I have ignored those files here.

`testURL` This option sets the URL for the jsdom environment. It is reflected in properties such as location.href

`transformIgnorePatterns` An array of regexp pattern strings that are matched against all source file paths, matched files will skip transformation. Here I give it only one for `node_modules`

`verbose` If true gives you a very detail log when you run tests. I don’t want to see that, and only focus on the gist of my tests. So I have set its value to `false`

Let’s talk about `enzyme.config.js`

I pass the path of `enzyme.config.js` in my `setupFiles` in Jest configurations. When it goes to this file, Jest takes in enzyme configurations. So that means all the tests will be run on Jest. But the assertions and everything else will be done by enzyme.

With this in place, our configurations are done. Let’s talk about scripts:

```
"scripts": {    
    "test": "jest",
    "test:watch": "jest --watch",    
    "test:coverage": "jest --coverage --colors",  
},
```

`npm run test` this will run Jest and execute all the tests

`npm run test:watch` will run all the tests and keep on watch mode, so that when we make any changes to our test cases, it will execute those test cases again.

`npm run test:coverage` will generate a coverage report based on all the tests it executes, and give you a detailed coverage report in the `app/coverage` folder.

Before we run a test, we need to create one. So let’s start. In your `app/src/` folder create a file called **WelcomeMessage.js**.

```
import React, { Fragment } from 'react';

const styles = {
  heading: {
    color: '#fff',
    textAlign: 'center',
    marginBottom: 15,
  },
  logo: {
    width: 250,
    heading: 250,
    objectFit: 'cover',
  },
};

const WelcomeMessage = ({ imgPath }) => {
  return (
    <Fragment>
      <h1 style={styles.heading}>
        Welcome To
      </h1>
      <img src={imgPath} alt="app logo" style={styles.logo} />
    </Fragment>
  );
};

export default WelcomeMessage;
```

In the same folder create a file called [**WelcomeMessage.test.js**](https://gist.github.com/adeelibr/ac60da132758c7ebbcb30e28672975fe)

```
import React from 'react';
import { shallow } from ‘enzyme’;

// Components
import WelcomeMessage from './WelcomeMessage';

function setup() {
  const props = {
    imgPath: 'some/image/path/to/a/mock/image',
  };
  const wrapper = shallow(<WelcomeMessage />);
  return { wrapper, props };
}

describe('WelcomeMessage Test Suite', () => {
  it('Should have an image', () => {
    const { wrapper } = setup();
    expect(wrapper.find('img').exists()).toBe(true);
  });
});
```

One thing to note here is you won’t be able to actually run the `WelcomMessage.js` file since you don’t have `webpack` set up with `babel`. If you are looking for a way to set that up, check out my tutorial on [How to combine Webpack 4 and Babel 7 to create a fantastic React app](https://medium.freecodecamp.org/how-to-combine-webpack-4-and-babel-7-to-create-a-fantastic-react-app-845797e036ff). Also if you just want the source code to this tutorial, here is the [**code repository**](https://github.com/adeelibr/react-starter-kit). It already has Jest & Enzyme set up. Feel free to make a fork and start playing with the code base.

Coming back to the code we just wrote, in your terminal type `npm run test`. It will execute a script and find all files that end with `*.test.js` and execute them. After it has executed you will see a message like this:

```
Test Suites: 1 passed, 1 total
Tests:       1 passed, 1 total
```

Now I know this isn’t much of a practical unit test, but I wanted this tutorial to focus on purely setting up Jest & Enzyme.

Again here is the source code to this [**tutorial**](https://github.com/adeelibr/react-starter-kit).

