---
title: Why Arrow Functions and bind in React’s Render are Problematic
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-22T14:40:09.000Z'
originalURL: https://freecodecamp.org/news/why-arrow-functions-and-bind-in-reacts-render-are-problematic-f1c08b060e36
coverImage: https://cdn-media-1.freecodecamp.org/images/1*mcgExlgxxMzp9ZugfTc9LQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: React Native
  slug: react-native
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Cory House

  (Hint: It makes shouldComponentUpdate and PureComponent cranky)

  In a previous post, I explained how to extract React child components to avoid using
  bind or arrow functions in render. But I didn’t provide a clear demo to show why
  this i...'
---

By Cory House

#### (Hint: It makes shouldComponentUpdate and PureComponent cranky)

In a previous post, I explained how to [extract React child components to avoid using bind or arrow functions in render](https://medium.freecodecamp.org/react-pattern-extract-child-components-to-avoid-binding-e3ad8310725e). But I didn’t provide a clear demo to show why this is useful.

Here’s a quick example.

In this example, I’m using an arrow function in render to bind the relevant user ID to each delete button.

%[https://codesandbox.io/s/54k49onoyl?from-embed]

On line 35, I’m using an arrow function to pass a value to the deleteUser function. That’s a problem.

To see why, check out User.js (click the hamburger icon on the top left to select different files in the example). I’m logging to the console each time render is called. I’ve declared User as a [PureComponent](https://facebook.github.io/react/docs/react-api.html#react.purecomponent). So User should only re-render when props or state change. But **when you click on delete for a user, note that render is called for _all_ User instances**.

Here’s why: The parent component is passing down an arrow function on props. Arrow functions are reallocated on every render (same story with using bind). So although I’ve declared User.js as a PureComponent, the arrow function in User’s parent causes the User component to see a new function being sent in on props for all users. So every user re-renders when **_any_** delete button is clicked. ?

Summary:

> Avoid arrow functions and binds in render. It breaks performance optimizations like shouldComponentUpdate and PureComponent.

### What Should I Do Instead?

For contrast, here’s an example that doesn’t use an arrow function in render.

%[https://codesandbox.io/s/jnowr0ww7v?from-embed]

In this example, index.js has no arrow function in render. Instead, the relevant data is passed down to User.js. In User.js, onDeleteClick calls the onClick function passed in on props with the relevant user.id.

With this change, when you click on delete, notice that render isn’t called for the other Users! ?

### Summary

For optimal performance,

1. Avoid arrow functions and bind in render.
2. How? [Extract child components](https://medium.freecodecamp.org/react-pattern-extract-child-components-to-avoid-binding-e3ad8310725e), or [pass data on the HTML element](https://medium.com/@mgnrsb/another-way-to-avoid-binding-in-render-in-simple-cases-like-this-where-all-you-need-is-to-remember-68af83da0258).

### Looking for More on React? ⚛️

I’ve authored [multiple React and JavaScript courses](http://bit.ly/psauthorpageimmutablepost) on Pluralsight ([free trial](http://bit.ly/pstrialimmutablepost)). My latest, “[Creating Reusable React Components](http://bit.ly/psreactcomponentsimmutablepost)” just published! ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*BkPc3o2d2bz0YEO7z5C2JQ.png)

[Cory House](https://twitter.com/housecor) is the author of [multiple courses on JavaScript, React, clean code, .NET, and more on Pluralsight](http://pluralsight.com/author/cory-house). He is principal consultant at [reactjsconsulting.com](http://www.reactjsconsulting.com), a Software Architect at VinSolutions, a Microsoft MVP, and trains software developers internationally on software practices like front-end development and clean coding. Cory tweets about JavaScript and front-end development on Twitter as [@housecor](http://www.twitter.com/housecor).

