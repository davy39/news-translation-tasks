---
title: React Unit Testing with Mocha and Enzyme
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-05-31T09:15:48.000Z'
originalURL: https://freecodecamp.org/news/react-unit-testing-with-mocha-and-enzyme-77d18b6875cb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Tk8MKzapWo7uPf0m5VF7Gg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Michael Shilman

  A step-by-step tutorial for UI testing in Meteor.

  This is a short tutorial to help you test your React UI components. It presents
  a simple UI testing pattern I contributed to the Meteor Guide (?) and Todos sample
  app (?).

  You shoul...'
---

By Michael Shilman

#### A step-by-step tutorial for UI testing in Meteor.

This is a short tutorial to help you test your React UI components. It presents a simple UI testing pattern I contributed to the Meteor [Guide](http://guide.meteor.com/) ([?)](https://github.com/meteor/guide/pull/466) and T[odos](https://github.com/meteor/todos/tree/react) sample app (?[).](https://github.com/meteor/todos/pull/141)

You should read this if you:

1. Are using [React](https://facebook.github.io/react/) to develop your apps
2. Want an easy way to automatically test your UI
3. Are using [Meteor](https://www.meteor.com/) … **or not** — most of this will work in any React setup!

Here are the tests we’ll be writing on the left, and the UI components we’ll be testing on the right:

![Image](https://cdn-media-1.freecodecamp.org/images/1*fxu5arW8UWdhVxeZi_zMmw.png)

As we step through several tests in detail, you’ll learn the building blocks of React UI testing and best practices for how to structure a test suite. You can apply these patterns to your own apps to catch bugs, write code faster, document code behavior, and make sure things don’t break as you add new features to your app.

The tutorial assumes a basic familiarity with React and [ES6](https://github.com/lukehoban/es6features), but does not require much Meteor knowledge. All the source code is available in Meteor’s [Todos](https://github.com/meteor/todos/tree/react) sample app so you can run it on your own machine and play around with the code.

### UI Unit Testing

There are many ways to test your software, but UI unit tests are small isolated tests of individual UI components, rather than full tests of the system. They are (relatively) easy to set up and fast to execute.

Here’s a screen grab of the current suite of Todos unit tests, including both Client (UI) and Server tests. The entire suite runs in just over a second on my laptop:

![Image](https://cdn-media-1.freecodecamp.org/images/1*5FSjCZurIXQkazef3LVN_A.gif)

Because the tests run so quickly, you can run them every time you [check in code](https://en.wikipedia.org/wiki/Continuous_integration) or even every time you [edit a file](https://wallabyjs.com/).

> _Having a full test suite gives you piece of mind that your code is always working as you expect it to._

### Technologies

Before we jump in, a few words about the various open-source technologies in play:

![Image](https://cdn-media-1.freecodecamp.org/images/1*1e_oWbWMM_LK4d5HpUiqXw.png)

[Meteor](https://www.meteor.com/) is a full-stack Javascript platform for modern web and mobile applications. It runs Node.JS on the backend and any of several UI frameworks on the front-end including React. Testing got a huge boost in the recent [1.3 release](http://info.meteor.com/blog/announcing-meteor-1.3), so we’re taking that for a spin today!

[React](https://facebook.github.io/react/) is Facebook’s Javascript library for user interfaces. It’s a popular way to develop modern web interfaces, and with [React Native](https://facebook.github.io/react-native/) is also making headway in native mobile and desktop apps.

[Mocha](https://mochajs.org/) is the most popular Javascript unit test runner. Just like we won’t cover everything about testing, we won’t cover everything about unit testing in Mocha. But there should be enough here to give you a solid start.

[Enzyme](https://github.com/airbnb/enzyme) is AirBnB’s library for unit testing React components. It’s great because it makes it easy to simulate the context of a React component without actually having to spin up a browser, and you can still perform CSS selection and simulate user events.

Except for Enzyme, which is React-specific, all of these libraries operate independently from one another. Together they make a pretty great way to build realtime apps.

> **_?:_** _O_k. Can we just start testing?

If you have the Todos app set up on your machine, or don’t care about actually running the tests, you can skip to the next section. Otherwise let’s get your machine set up. ?

### Machine Setup

If you want to run the tests on your local machine, here’s the quick setup for Linux/Mac. For a much more more detailed walkthrough, the Meteor site provides a [full tutorial for the Todos app](https://www.meteor.com/tutorials/react/creating-an-app):

NOTE: there’s currently [an issue](https://github.com/meteor/todos/issues/144) where it gives the following warning on the command line when running the tests:

```
Unable to resolve some modules:"react/addons" in /path/to/react-compat.js"react/lib/ReactContext" in /path/to/react-compat.js"react/lib/ExecutionEnvironment" in /path/to/react-compat.js
```

It is safe to ignore this and you should be able to see the results of the test run in the browser at [http://localhost:3000.](http://localhost:3000.)

The test results are coming from any files with the suffix **.tests.js** in the source tree, and when we edit any files or add new files with that naming scheme, the test suite will automatically re-execute and update the browser window.

NOTE: confusingly, there is also a **tests/** directory in the top level of the source tree. This contains end-to-end tests, and you should ignore this for this tutorial. For more information [see the guide](http://guide.meteor.com/testing.html).

### Component Rendering

The simplest UI test is whether a component renders properly according to the data passed into it. For example, if you render a todo item, you’d expect to see the item’s name shown in the label, and it’s checked state to be reflected properly on the page.

![Image](https://cdn-media-1.freecodecamp.org/images/1*asDZOHrIZND0FXK7rhsI7Q.png)

Here’s how that looks in Enzyme and Mocha:

There are a few things going on here.

**Structure.** In Mocha, _describe_ starts a test suite, and _it_ starts a single test case. For our first test, we’re using the simplest possible structure. Note that the contents of _describe_ and _it_ are just functions, so we can do things like exit early to force the tests to only run on the client side.

Within each test, we follow a **_setup → exercise → verify → teardown_** pattern which comes under different names, but is the [common best practice](http://www.agile-code.com/blog/the-anatomy-of-a-unit-test/) in unit testing:

**Setup.** First we create the data to render, which in this case is a Javascript object. Easy peasy.

**Exercise.** Next use the _shallow_ function to render the data into a component. This rendering is what we’re actually testing, so that’s why it’s part of the _exercise_ phase rather than _setup_. Calling _shallow_ returns an Enzyme _wrapper_ object that contains the rendered component instance, as well as a bunch of utility functions to simulate user events like mouse clicks and query the UI state.

**Verify.** Next, we use _hasClass_, _find,_ and _prop_ to query the UI state to verify that the component has rendered properly. All _TodoItem_ instances should have the _list-item_ class, and checked items should have the _checked_ class. Finally we make sure that the default value of the input is “Embrace the Ecosystem” as we’d expect.

**Teardown.** In many tests there’s also some cleanup to do, but in this case there’s nothing to clean up since all the variables are temporary.

To add this test to the Todos app, simply copy the snippet into a file **imports/ui/components/TodoItem-render.tests.js** underneath the _todos_ directory (any file with the **.tests.js** suffix actually, but we put it in the same directory as the component by convention). This test will be redundant with the tests already in **TodoItem.tests.js**, but now you know how to add your own.

### Rendering with State

Let’s do another example that’s slightly more complex. The list header actually has two states: a normal state and an editing state, and it displays two different UI’s depending on internal component state.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Dgy5ayc59KGlIKvjwlVs9g.png)

And here’s how the test looks:

**Structure.** Notice that we’ve split the code up into two _describe_ blocks to give it a little more structure. This will help when we start adding more tests, since in addition to rendering differently, the component’s interaction changes depending on the state. We’ll talk about this more below.

**Setup/Exercise.** Business as usual, except that we’ve used Enzyme’s _mount_ function to render rather than _shallow_, which we used above. We use _mount_ to simulate the full component context. The difference is that _shallow_ only renders the component passed, but _mount_ requires that we are running in a browser context (browser or headless browser) and also renders child components.

**Test.** We’ve used Enzyme’s _setState_ utility to manipulate the component state. This is like simulating a mouse click, except for rather than simulating the user directly, we are simulating a change from another part of the application.

**Verify/Teardown.** Nothing special: querying the DOM and no cleanup required for this simple test.

### User Interaction

Rendering is only half of the equation, and things get more interesting when we want to test user interaction. First, let’s model when a user clicks the checkbox on a todo item:

![Image](https://cdn-media-1.freecodecamp.org/images/1*6tSODdVWqKJex8HhcbtBdA.gif)

And here’s how that test looks:

**Structure.** This code follows the same _setup → exercise → verify → teardown_ structure as above, but in this case we actually get to do something meaningful in each step.

**Setup.** This one is interesting because when you click on the checkbox, the component actually calls a [Meteor Method](http://guide.meteor.com/methods.html), which asks the server to update the database. However, when we’re running a unit test there is no server, and even if there was we wouldn’t want to modify any data. So we stub out the method using the [Sinon](http://sinonjs.org/) library (commonly used with Mocha). It replaces the _setCheckedStatus_ method’s _call_ function with a dummy that looks like the original, but simply records the user’s behavior and doesn’t actually do anything with it.

NOTE: You may be scratching your head because up until now, the _shallow/mount_ rendering has been part of the _exercise_ phase, but this time around it’s in _setup_. It’s a subtle point, but since the focus of this test is the user interaction action so rendering is just part of the setup.

**Exercise.** Next, we use the _simulate_ function to make the click. Pretty straightforward. We can also simulate keyboard events, form submissions and so forth, but we don’t need that for this test.

**Verify.** Now we we can see how the stub comes into play. We assert that the _setCheckedStatus_ method was called with the arguments we expect. This not only tests the behavior but provides nice documentation about how the interaction works.

**Teardown.** Setting up the stub actually modifies the _setCheckedStatus_ method globally, so at the end of the test we should clean it up. restore replaces the stub with the original function.

All of our other interaction tests follow the same basic structure and you can see them in the [Todos repo](https://github.com/meteor/todos/tree/react).

### Test Suite Structure

Using these basic patterns above for testing _rendering_ and _interaction_, you should be able to test any React component in the Todos example and easily adapt the pattern to your own apps. But if you start adding tests willy-nilly, without some way of structuring your code, things will quickly get out of control. So I’ll wrap up the tutorial by describing a higher-level test structure.

I mentioned above how using Mocha’s _describe_ can both delineate a logical structure and also save code, and we’ll use that to our advantage as we add more tests. Let’s see how that works.

Recall our _ListHeader_ example above where we distinguished between the the default and editing states. The test had the following structure:

Now let’s refactor the code using Mocha’s _beforeEach_ construct which gets executed before each of the tests inside the _describe_ suite:

At first glance, this change appears to be a net loss: the code got longer and a complicated. However, the more tests we add, the more reuse we get and the more this structure starts to make sense. Here is the test structure in the Todos app, and this is only a partial test of the header’s functionality:

Before you go all code cowboy with this, you should note that because _beforeEach_ executes for every test in every nested block, it’s very easy to write inefficient tests this way. For example, in the code above a new React router stub is created five times, once for every single _it_ test, although it’s really only needed for one of the tests. In this case, I was fine with that. However, it’s tempting to throw all your test setup into _beforeEach_, but you should generally only put what you need there.

### Conclusion and Next Steps

In this tutorial, we’ve gone through the basics of UI Component testing, with well-documented examples of how to test rendering and interaction. These are the basic building blocks for testing your UI, and using them you should be able to unit test most aspects of any React UI you develop.

Here are some next steps to learn more:

1. **Your homework**. Check out the [Todos app](https://github.com/meteor/todos), and add a unit test for a different behavior. For example, the app distinguishes between public and private Todos, but the current tests don’t cover that. Add a test for that! _Extra credit: submit a pull request!_
2. **More React UI Testing.** Fellow Meteor geek [Arunoda](https://www.freecodecamp.org/news/react-unit-testing-with-mocha-and-enzyme-77d18b6875cb/undefined)’s [UI Testing in React](https://voice.kadira.io/ui-testing-in-react-74fd90a5d58b#.tek2zwsvq) covers a lot of the same ground, but from a different angle. And if you’re so inclined, [Ken Wheeler](https://www.freecodecamp.org/news/react-unit-testing-with-mocha-and-enzyme-77d18b6875cb/undefined) explains a similar setup for [Unit Testing React Native](https://blog.formidable.com/unit-testing-react-native-with-mocha-and-enzyme-51518f13ba73).
3. **Testing in General.** UI unit testing is just a piece of the puzzle. [Eric Elliott](https://www.freecodecamp.org/news/react-unit-testing-with-mocha-and-enzyme-77d18b6875cb/) gives five questions to answer in each unit test. The Meteor Guide’s [testing section](http://guide.meteor.com/testing.html) is a great overview of other kinds of tests in Meteor, and of testing in general.

Comment below with questions or suggestions. And follow me here or [on Twitter](https://twitter.com/mshilman) for _more great articles coming down the pipe._

**And finally, if this was useful, please tap the ? button below. Thanks!**

_Many thanks to [Tom Coleman](https://www.freecodecamp.org/news/react-unit-testing-with-mocha-and-enzyme-77d18b6875cb/undefined) for Meteor/PR guidance; [Sean Moon](https://www.freecodecamp.org/news/react-unit-testing-with-mocha-and-enzyme-77d18b6875cb/undefined) for introducing me to testing; [Keywon](https://www.freecodecamp.org/news/react-unit-testing-with-mocha-and-enzyme-77d18b6875cb/undefined), [Ross Geesman](https://www.freecodecamp.org/news/react-unit-testing-with-mocha-and-enzyme-77d18b6875cb/undefined), [Josh Owens](https://www.freecodecamp.org/news/react-unit-testing-with-mocha-and-enzyme-77d18b6875cb/undefined), [Sam Hatoum](https://www.freecodecamp.org/news/react-unit-testing-with-mocha-and-enzyme-77d18b6875cb/undefined) for excellent feedback on the draft._

