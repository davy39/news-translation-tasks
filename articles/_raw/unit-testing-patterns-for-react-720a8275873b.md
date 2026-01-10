---
title: Check out these beginner-friendly unit testing patterns for React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-04T20:56:00.000Z'
originalURL: https://freecodecamp.org/news/unit-testing-patterns-for-react-720a8275873b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*JIQ0Vp6gRaNr40h4wDw7GA.jpeg
tags:
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Redux
  slug: redux
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Benedek Gagyi

  There are many frameworks and even more ways to test a React component. But in my
  experience, there are a few patterns that are particularly useful to know, regardless
  of the testing framework you prefer (especially if you are just g...'
---

By Benedek Gagyi

There are many frameworks and even more ways to test a React component. But in my experience, there are a few patterns that are particularly useful to know, regardless of the testing framework you prefer (especially if you are just getting to know React). So here are 5 **framework-agnostic** unit testing patterns for React.

[Alex Moldovan](https://www.freecodecamp.org/news/unit-testing-patterns-for-react-720a8275873b/undefined) published a [great article](https://medium.com/@alexnm/evolving-patterns-in-react-116140e5fe8f) a few days ago about the current patterns in React. The thing I liked about it the most is the way he approached the problem. You see, since React is so unopinionated, a universal style guide would not suit the community (we saw the exact opposite when [John Papa](https://www.freecodecamp.org/news/unit-testing-patterns-for-react-720a8275873b/undefined) published his style guide for AngularJS).

Alex solves this by offering patterns that are useful for beginners and more experienced developers alike without stating one “true” way of doing things.

So as a continuation of his work, here are a few patterns I find useful when writing unit tests for React components.

**First things first: what should I test?**

Every time I teach the basics of unit testing, the same question gets asked: “What should I write my tests against? What are the cases my tests should check?” Giving a one-sentence answer that fits all the possible situations is quite hard, but in case of React it’s slightly easier.

Most of the components you are going to work with will be stateless, so they can be viewed simply as pure functions: they get a few arguments as props and return a rendered component. So the answer in this case for the question above is: “Check if the different combinations of inputs result in correct outputs.” If you ask me, that’s a lot easier to wrap your head around and to execute!

Just be careful: if you see _this.state_ in a component, it means that it’s stateful. So on top of the things mentioned earlier, you’ll need to write tests against the state mutations, too.

**#1: PropTypes**

In most testing frameworks, a warning is thrown when a prop is not provided or has an incorrect type. For some reason, many people ignore these and let them pile up, rendering the PropTypes useless from the testing point of view.

An argument in favor of doing this is that these errors will appear in the browser console as errors at runtime, so there’s no reason to provide all the needed props in the tests.

In my experience, while the above statement is true, proceeding this way has one major drawback: some errors and bugs can only be found at runtime and not by running the tests. And that’s one of the reasons we write unit tests: so we don’t have to check everything manually at runtime.

If you are using a type system like TypeScript or Flow, this may not apply to you, since in that case an error will be thrown at compile time. This is a big advantage and should be considered when deciding upon using such tools. Thanks to [Liran Tal](https://www.freecodecamp.org/news/unit-testing-patterns-for-react-720a8275873b/undefined), who pointed this out!

Omitting to set a prop in a unit test is not a bug in our application, so why should we bother fulfilling the PropTypes contract correctly? The answer is simple: because it helps to keep the tests healthy. Adding a prop in a component will result in a PropType warning in the tests, thus warning us that our tests don’t cover every case. The same goes for changing the type of a PropType: if a warning is thrown in our tests, it means that they need updating.

The only drawback of this method is that the props in the test need to be kept up to date. Next, I’ll discuss the way I prefer to do it.

**#2: Reusable props**

When testing a React component, most of your test cases will need a certain set of props to hydrate the component with. The most straightforward way to do this is to create a constant for each test case containing a version of the props needed.

The problem with this solution is that there are rarely any cases when all the props provided are relevant to that given test case. Most of the time they are just there to secure the correct behavior of the component (and to fulfill the PropTypes).

Copying and pasting these extra props is cumbersome, error prone, and results in a bloated code that’s hard to read.

The pattern I prefer to use to avoid this is based on having a global props constant, and extending it where necessary using the spread operator.

This pattern has three main benefits:

* no copy-pasting is needed, the code is more concise, and there’s no bloat
* the PropTypes are always fulfilled correctly
* the readability of the tests increases, since the props being used by the given test case are highlighted. It’s enough just to look at the definition of the props to see which case is being tested there. This is why I like to redefine a property if it’s used in that test case, even if it has the same or similar value in the global props object.

A variation of this pattern also uses a global props object. But instead of always creating a new object for each test case, it keeps mutating the global object to fit the current needs. I find this solution too fragile for my taste. But my biggest issue with it is that it causes tests to depend on each other, resulting in severe performance problems, since these tests can’t be run in parallel.

**#3: Shallow rendering**

A challenge of unit testing in general is writing code that tests the given unit, but not its dependencies. Just like in any decent ecosystem, we have a ton of options when we want to mock or stub the dependencies of a React component.

One of these libraries uses such a simple, yet elegant solution that I think should be part of all of your React unit tests. This library is called [Enzyme](https://github.com/airbnb/enzyme). It’s made by the nice people over at [AirbnbEng](https://www.freecodecamp.org/news/unit-testing-patterns-for-react-720a8275873b/undefined), and the feature I’m talking about is shallow rendering.

Shallow rendering is basically a way to render a React component without rendering its subcomponents, thus making the test independent from these subcomponents.

Let me give you an example. Let’s say we have a component called _TextAndButton_ that has a child component called _Button_:

When _TextAndButton_ is rendered in a browser, its subcomponent is rendered also. So in the end it will look something like this:

But when you do a shallow rendering, the subcomponents remain just as they were written:

This way if _Button_ has any dependencies, it’s not dragged in for this rendering. Even better: the parent component doesn’t need to know anything about its children.

Besides the clear performance benefits, I like this approach because it simplifies the mental model and makes it clear what should be tested where.

In the case of our example, the test for _TextAndButton_ should only check if the correct action was passed to _Button._ But we don’t care about anything it actually does, like displaying the correct text or actually calling the provided function when needed.

In addition to that, your tests will be more robust, since changing a child component won’t break the tests written for the parent.

While I can imagine a few instances where shallow rendering is not the best idea, in general I think it can and should be used for all of your component tests.

**#4: Redux Reducers and Action Creators**

The philosophy of React is heavily influenced by functional programming, and the same is true for Redux. So don’t get scared by all the fancy names like “reducer” and “action creator”: these are just regular, pure functions with specific purposes.

The popularity of Redux is in part due to its simplicity. That’s why it amazes me every time I see projects using overcomplicated reducer and action creator testing patterns.

In my experience, unit testing the reducers and the action creators as functions is perfectly sufficient. Check if they return the correct value for the given input (for example, a reducer should return the correct state object for the given input state and action), and that’s it. Doing anything more, like simulating actions or actually dispatching them on a mock store is overkill — that way, you end up testing Redux itself (besides your unit).

Don’t take this from me: the [official Redux testing docs](https://github.com/reactjs/redux/blob/master/docs/recipes/WritingTests.md) use the same simplistic, function-based approach.

On the other hand there’s nothing wrong with simulating actions if your goal is to create integration tests to find out if everything is wired up correctly. But it’s important to not mix unit and integration tests, so use this pattern accordingly.

**#5: Don’t test the DOM**

In my experience, writing fragile unit tests is almost as bad as writing none. If a unit test breaks when it should not (when the actual behavior of the unit didn’t change), it eats up time until the developer either fixes the fragility (costing extra time and effort) or even worse just comments it out.

There are many ways one can write fragile tests for React components, but there’s one I saw multiple times that’s really easy to avoid: writing tests against the DOM.

To give you a simple example, asserting against the DOM would be checking the number of children the given component has. The way I see it, this is not a useful test, since it won’t fail when we actually break the component (for example by switching a password field to a regular text input). But it will break when we make minor, non-breaking adjustments (like wrapping a text in a _span_ tag).

Another way to test the DOM is to query certain elements inside your component by their “heritage,” by going through “child-of-sibling-of-child-of” chains. How a given component is built up internally should not be tested because it changes too often and, more importantly, because it holds no additional value.

Opt instead for focused, CSS-like queries that target only the element you are interested in. Again, a query like _div span img_ is not a good idea. Go instead for class-based queries that don’t rely on the HTML structure.

**Final thoughts**

Testing React components, especially with the latest tools, is a breeze. Don’t get discouraged by the initial hardships and the few hours spent googling at the beginning. You’ll win back those hours tenfold if you keep writing good quality tests.

And don’t forget: you are not only helping your future self, but also your users, who’ll be thankful to receive the cool new features faster and bug free.

