---
title: React Hooks Fundamentals for Beginners
subtitle: ''
author: Tapas Adhikary
co_authors: []
series: null
date: '2022-03-15T19:20:16.000Z'
originalURL: https://freecodecamp.org/news/react-hooks-fundamentals
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/freeCodeCamp-Cover.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
seo_title: null
seo_desc: "React.js is an open-source JavaScript-based user interface library. It\
  \ is hugely popular for web and mobile app development. \nReact follows the principle\
  \ of component-based architecture. A component in React is an isolated and reusable\
  \ piece of code...."
---

React.js is an open-source JavaScript-based user interface library. It is hugely popular for web and mobile app development. 

React follows the principle of `component-based` architecture. A `component` in React is an isolated and reusable piece of code. The components can be of two types – class components and functional components.

Before React version 16.8, developers could handle state and other React features only using class components. But with version 16.8, React introduced a new pattern called `Hooks`. 

With React Hooks, we can use state, and other React features, in a functional component. It empowers devs to do functional programming in React.

In this article, we will learn the fundamentals of `React Hooks`. The motivation behind writing this piece is to encourage beginners to think that "React Hooks are easy to learn, create, and use". Yes, that's true as long as you understand them fundamentally.

If you like to learn from video content as well, this article is also available as a video tutorial here: 🙂

%[https://www.youtube.com/watch?v=CvNvRaS3u60]

## Before You Learn About Hooks...

Before you think of hooks, think of plain-old (aka vanilla) `JavaScript functions`.

In the JavaScript programming language, functions are reusable code logic to perform repeated tasks. Functions are composable. This means you can invoke a function in another function and use its output.

In the image below, the `someFunction()` function composes (uses) functions `a()` and `b()`. The `b()` function uses the function `c()`.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-13.png)
_Function Composability_

If we write this in code, it will be like this:

```js
function a() {
    // some code
}

function c() {
    // some code
}

function b() {
    // some code
    
    c();
    
    // some code
}

function someFunction() {
    // some code
    
	a();
    b();
    
    // some code
}
```

It is not a secret that functional components in React are just plain old JavaScript functions! So if functions have composability, React components can also have composability. This means we can use (compose) one or more components into another component as shown in the image below:

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-14.png)
_Components Composability_

## Stateful vs. Stateless Components

Components in React can be stateful or stateless.

* A stateful component declares and manages local state in it.
* A stateless component is a pure function that doesn't have a local state and side-effects to manage.

A [pure function](https://blog.greenroots.info/what-are-pure-functions-and-side-effects-in-javascript) is a function without any side-effects. This means that a function always returns the same output for the same input.

If we take out the stateful and side-effects logic from a functional component, we have a stateless component. Also, the stateful and side-effects logic can be reusable elsewhere in the app. So it makes sense to isolate them from a component as much as possible.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-15.png)
_Stateful Component as the component has Stateful Logic_

## React Hooks and Stateful Logic

With React Hooks, we can isolate stateful logic and side-effects from a functional component. Hooks are JavaScript functions that manage the state's behaviour and side effects by isolating them from a component. 

So, we can now isolate all the stateful logic in hooks and use (compose them, as hooks are functions, too) into the components.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-16.png)
_Isolated Stateful Logic into Hooks_

The question is, what is this stateful logic? It can be anything that needs to declare and manage a state variable locally. 

For example, the logic to fetch data and manage the data in a local variable is stateful. We may also want to reuse the fetching logic in multiple components.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-17.png)

## So, What Exactly Are React Hooks?

So, how can we define React Hooks in plain English? Now that we understand functions, composability, components, states, and side-effects, here goes a definition of React Hooks:

> React Hooks are simple JavaScript functions that we can use to isolate the reusable part from a functional component. Hooks can be stateful and can manage side-effects.

React provides a bunch of standard in-built hooks:

* `useState`: To manage states. Returns a stateful value and an updater function to update it.
* `useEffect`: To manage side-effects like API calls, subscriptions, timers, mutations, and more.
* `useContext`: To return the current value for a context.
* `useReducer`: A `useState` alternative to help with complex state management.
* `useCallback`: It returns a memorized version of a callback to help a child component not re-render unnecessarily.
* `useMemo`: It returns a memoized value that helps in performance optimizations.
* `useRef`: It returns a ref object with a `.current` property. The ref object is mutable. It is mainly used to access a child component imperatively.
* `useLayoutEffect`: It fires at the end of all DOM mutations. It's best to use `useEffect` as much as possible over this one as the `useLayoutEffect` fires synchronously.
* `useDebugValue`: Helps to display a label in React DevTools for custom hooks.

You can read about these hooks in more detail [from here](https://reactjs.org/docs/hooks-reference.html). Please notice that each of these hook names start with `use`. Yes, this is a standard practice to identify a hook in the React codebase quickly. 

We can also create custom hooks for our unique use cases like data fetching, logging to disk, timers, and many more.

So next time, if you encounter React Hooks in a codebase or are asked to write one, take it easy. It is just another JavaScript function to deal with state and side-effects outside of functional components. 

If you are looking for a step-by-step guide to design and create a custom hook, you may find [this article helpful](https://blog.greenroots.info/how-to-create-a-countdown-timer-using-react-hooks).

## Before We End...

I hope you found the introduction to React Hooks helpful. After spending many years with React, I have started a [YouTube video series](https://www.youtube.com/watch?v=ODKIxaSMgpU&list=PLIJrr73KDmRyrDnDFy-hHvQ24rRjz6e_J) that aims to cover all the aspects of React end to end. Please [subscribe](https://www.youtube.com/tapasadhikary?sub_confirmation=1) if you find it helpful. 

Let's connect. I share my learnings on JavaScript, Web Development, and Blogging on these platforms as well:

* [Follow me on Twitter](https://twitter.com/tapasadhikary)
* [Side projects on GitHub](https://github.com/atapas)
* [React.JS Community on Showwcase](https://www.showwcase.com/community/react.js)

See you soon with my next article. Until then, please take care of yourself, and stay happy.

