---
title: 'React Hooks Cheat Sheet: The 7 Hooks You Need To Know'
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-02-08T15:28:32.000Z'
originalURL: https://freecodecamp.org/news/react-hooks-cheatsheet
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/react-hooks-cheatsheet-2021.png
tags:
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
seo_title: null
seo_desc: 'This new tutorial will show you everything you need to know about React
  Hooks from scratch.

  I''ve put this cheatsheet together to help you become knowledgeable and effective
  with React Hooks as quickly as possible.

  Plus, this tutorial is also an inter...'
---

This new tutorial will show you everything you need to know about React Hooks from scratch.

**I've put this cheatsheet together to help you become knowledgeable and effective with React Hooks as quickly as possible.**

Plus, this tutorial is also an interactive video guide that will show you practical examples of how to use each hook in 30 seconds or less.

Each example builds off of the previous one and it includes tons of patterns and best practices that will help you build apps with React Hooks for years to come.

## Want Your Own Copy?‬

**[Click here to download the cheatsheet in PDF format](https://reedbarger.com/resources/react-hooks-2021)** (it takes 5 seconds).

Here are 3 quick wins you get when you grab the downloadable version:

* You'll get tons of copyable code snippets for easy reuse in your own projects.
* It is a great reference guide to strengthen your skills as a React developer and for job interviews.
* You can take, use, print, read, and re-read this guide literally anywhere that you like.

There's a ton of great stuff to cover, so let's get started:

### Table of Contents:

1. [useState Hook](#heading-1-usestate-hook)
2. [useEffect Hook](#heading-2-useeffect-hook)
3. [useRef Hook](#heading-3-useref-hook)
4. [useCallback Hook](#heading-4-usecallback-hook)
5. [useMemo Hook](#heading-5-usememo-hook)
6. [useContext Hook](#heading-6-usecontext-hook)
7. [useReducer Hook](#heading-7-usereducer-hook)

## 1. useState Hook

### useState to Create State Variables

The useState hook allows us to create state variables in a React function component.

> State allows us to access and update certain values in our components over time

When we create a state variable, we must provide it a default value (which can be any data type).

We get that state variable as the first value in an array, which we can destructure and declare with `const`.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/clip-1-usestate-min.gif)

### Update State Variables

useState also gives us a setter function to update the state after it is created.

To update our state variable, we pass the setter function the new value we want our state to be.

> When you declare your setter function, in most cases you will prefix it with the word "set"

![Image](https://www.freecodecamp.org/news/content/images/2021/02/clip-2-usestate-min.gif)

### Can Be Used Once Or Many Times

useState can be used once or multiple times within a single component.

Sometimes you will want to create multiple state variables and other times you may want to use a single variable with an object (see below).

![Image](https://www.freecodecamp.org/news/content/images/2021/02/clip-3-usestate-min.gif)

### Update State based on Previous Value

If the new state depends on the previous state, we can take the previous state variable and apply whatever changes we want to make.

For example, as in the example below, add 1 to the current `years` value to increment it.

To guarantee the update is done reliably, we can use a function within the setter function that gives us the correct previous state.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/clip-4-usestate-min.gif)

### Manage State with an Object

You can use an object with useState, which allows you to manage individual values as key-value pairs.

As the example below shows, when you are updating state with an object, you need to spread in the previous state. 

Why? Because any properties other than the one you are updating will not be included in the new state.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/clip-5-usestate-min.gif)

## 2. useEffect Hook

### useEffect to Perform Side Effects

useEffect lets us perform side effects in function components.

> Side effects are when we need to reach into the outside world. Such as fetching data from an API or working with the DOM.

Side effects are actions that can change our component state in an unpredictable fashion (that have caused 'side effects').

useEffect accepts a callback function (called the 'effect' function), which will by default run every time the component re-renders.

In the example below, we are interacting with the DOM to change style properties of the document body:

![Image](https://www.freecodecamp.org/news/content/images/2021/02/clip-1-useeffect-min.gif)

### Run Again when a Value Changes

useEffect lets us conditionally perform effects with the dependencies array.

The dependencies array is the second argument passed to useEffect. 

If any one of the values in the array changes, the effect function runs again.

If no values are included in the dependencies array, useEffect will only run on component mount and unmount.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/clip-2-useeffect-min.gif)

### Unsubscribe by Returning a Function

useEffect lets us unsubscribe from listeners that we might have created by returning a function at the end.

We want to unsubscribe from certain events, such as an event listener, because when the component unmounts (i.e. the user goes to a different page), React may attempt to update state that no longer exists, causing an error.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/clip-3-useeffect-min.gif)

### Fetch Data from an API

useEffect is the hook to use when you want to make an HTTP request (namely, a GET request when the component mounts).

Note that handling promises with the more concise `async/await` syntax requires creating a separate function.

This is because the effect callback function cannot be async. 

In the example below, we resolve our promise (returned from `fetch`) with a series of `.then()` callbacks to get our data.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/clip-4-useeffect-min.gif)

## 3. useRef Hook

### useRef to Reference React Elements

Refs are a special attribute that are available on all React components. They allow us to create a reference to a given element / component when the component mounts.

useRef allows us to easily use React refs. They are helpful (as in the example below) when we want to directly interact with an element, such as to clear its value or focus it, as with an input.

We call useRef (at the top of a component) and attach the returned value to the element's ref attribute to refer to it.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/clip-1-useref-min.gif)

## 4. useCallback Hook

### useCallback Prevents Callbacks from Being Recreated

useCallback is a hook that is used for improving our component performance.

> Callback functions are the name of functions that are "called back" within a parent component.

The most common usage is to have a parent component with a state variable, but you want to update that state from a child component. 

What do you do? You pass down a callback function to the child from the parent. That allows us to update state in the parent component.

useCallback memoizes our callback functions, so they not recreated on every re-render. Using useCallback correctly can improve the performance of our app.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/clip-1-usecallback-min.gif)

## 5. useMemo Hook

### useMemo Can Improve Expensive Operations

useMemo is very similar to useCallback and helps improve performance. But instead of being for callbacks, it is for storing the results of expensive operations.

> useMemo allows us to memoize, or remember the result of expensive operations when they have already been made for certain inputs.

Memoization means that if a calculation has been done before with a given input, there's no need to do it again, because we already have the stored result of that operation.

useMemo returns a value from the computation, which is then stored in a variable.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/clip-1-usememo-min.gif)

## 6. useContext Hook

### useContext Helps Us Avoid Prop Drilling

In React, we want to avoid the following problem of creating multiple props to pass data down two or more levels from a parent component.

> In some cases, it is fine to pass props through multiple components, but it is redundant to pass props through components which do not need it.

Context is helpful for passing props down multiple levels of child components from a parent component and sharing state across our app component tree.

The useContext hook removes the unusual-looking render props pattern that was required in consuming React Context before. 

Instead, useContext gives us a simple function to access the data we provided on the `value` prop of the Context Provider in any child component.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/clip-1-usecontext-min.gif)

## 7. useReducer Hook

### useReducer is (Another) Powerful State Management Tool

useReducer is a hook for state management, much like useState, and relies upon a kind of function called a reducer.

> Reducers are simple, predictable (pure) functions that take a previous state object and an action object and return a new state object.

useReducer can be used in many of the same ways that useState can, but is more helpful for managing state across multiple components that may involve different operations or "actions".

You will need to reach for useReducer less than useState around your app. But it is very helpful as a powerful means of managing state in smaller applications, rather than having to reach for a third-party state management library like Redux.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/clip-1-usereducer-min.gif)

## Want to keep this guide for future reference?

**[Download a complete PDF version of this cheatsheet here.](https://reedbarger.com/resources/react-hooks-2021)**

Enjoy!

## Become a Professional React Developer

React is hard. You shouldn't have to figure it out yourself.

I've put everything I know about React into a single course, to help you reach your goals in record time:

[**Introducing: The React Bootcamp**](https://www.thereactbootcamp.com)

**It’s the one course I wish I had when I started learning React.**

Click below to try the React Bootcamp for yourself:

[![Click to join the React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Click to get started*

