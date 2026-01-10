---
title: The React useEffect Hook for Absolute Beginners
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2022-03-01T20:41:00.000Z'
originalURL: https://freecodecamp.org/news/react-useeffect-absolute-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/react-useeffect-absolute-beginners.png
tags:
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
seo_title: null
seo_desc: 'If you have trouble understanding the useEffect hook, you''re not alone.

  Beginners and experienced developers alike find it to be one of the trickiest hooks
  to understand, because it requires understanding a few unfamiliar programming concepts.

  In thi...'
---

If you have trouble understanding the useEffect hook, you're not alone.

Beginners and experienced developers alike find it to be one of the trickiest hooks to understand, because it requires understanding a few unfamiliar programming concepts.

In this quick guide, we're going to cover why this hook exists, how to better understand it, and how to properly use it in your React projects today.

## Why is it called useEffect? 

When the core React Hooks were added to the library in 2018 (useState, useEffect, and so on), many developers were confused by the name of this hook: "useEffect".

What exactly is an "effect"?

The word effect refers to a functional programming term called a **"side effect"**.

But to really understand what a side effect is, we first have to grasp the concept of a **pure function**. 

You may not know this, most React components are intended to be pure functions.

It may be strange to think about React components as functions, but they are.

It helps to see that a regular React function component is declared like a JavaScript function:

```js
function MyReactComponent() {}
```

Most React components are pure functions, meaning they receive an input and produce a predictable output of JSX. 

The input to a JavaScript function is arguments. What is the input to a React component, however? **Props**! 

Here we have a `User` component that has the prop `name` declared on it. Within `User`, the prop value is displayed in a header element. 

```js
export default function App() {
  return <User name="John Doe" />   
}
  
function User(props) {
  return <h1>{props.name}</h1>; // John Doe
}
```

This is pure because, given the same input, it will **always** return the same output.

If we pass `User` a `name` prop with value "John Doe", our output will always be John Doe.

You might be saying, "Who cares? Why do we even have a name for this?"

Pure functions have the great benefit of being **predictable,** **reliable, and easy to test.** 

This is as compared to when we need to perform a side effect in our component.

## What are side effects in React?

Side effects are not predictable because they are actions which are performed with the "outside world." 

We perform a side effect when we need to reach outside of our React components to do something. Performing a side effect, however, will not give us a predictable result.

Think about if we were to request data (like blog posts) from a server that has failed and instead of our post data, gives us a 500 status code response. 

Virtually all applications rely on side effects to work in one way or another, aside from the simplest applications. 

Common side effects include:

* Making a request to an API for data from a backend server 
* To interact with browser APIs (that is, to use `document` or `window` directly)
* Using unpredictable timing functions like `setTimeout` or `setInterval` 

This is why useEffect exists: to provide a way to handle performing these side effects in what are otherwise pure React components. 

For example, if we wanted to change the title meta tag to display the user's name in their browser tab, we _could_ do it within the component itself, but we shouldn't.

```js
function User({ name }) {
  document.title = name; 
  // This is a side effect. Don't do this in the component body!
    
  return <h1>{name}</h1>;   
}
```

If we perform a side effect directly in our component body, it gets in the way of our React component's rendering.

Side effects should be separated from the rendering process. If we need to perform a side effect, it should strictly be done _after_ our component renders.

This is what useEffect gives us.

In short, **useEffect is a tool that lets us interact with the outside world but not affect the rendering or performance of the component that it's in.** 

## How do I use useEffect?

The basic syntax of useEffect is as follows:

```js
// 1. import useEffect
import { useEffect } from 'react';

function MyComponent() {
  // 2. call it above the returned JSX  
  // 3. pass two arguments to it: a function and an array
  useEffect(() => {}, []);
  
  // return ...
}
```

The correct way to perform the side effect in our `User` component is as follows:

1. We import `useEffect` from "react"
2. We call it above the returned JSX in our component
3. We pass it two arguments: a function and an array

```js
import { useEffect } from 'react';

function User({ name }) {
  useEffect(() => {
    document.title = name;
  }, [name]);
    
  return <h1>{name}</h1>;   
}
```

The function passed to useEffect is a callback function. This will be called after the component renders. 

In this function, we can perform our side effects or multiple side effects if we want. 

The second argument is an array, called the dependencies array. This array should include all of the values that our side effect relies upon. 

In our example above, since we are changing the title based off of a value in the outer scope, `name`, we need to include that within the dependencies array.

What this array will do is it will check and see if a value (in this case name) has changed between renders. If so, it will execute our use effect function again. 

This makes sense because if the name changes, we want to display that changed name and therefore run our side effect again. 

## How to fix common mistakes with useEffect

There are some subtle details to be aware of avoid mistakes with useEffect. 

If you do not provide the dependencies array at all and only provide a function to useEffect, **it will run after every render**. 

This can lead to problems when you're attempting to update state within your useEffect hook.

If you forget to provide your dependencies correctly and you are setting a piece of local state when the state is updated, the default behavior of React is to re-render the component. And therefore, since useEffect runs after every single render without the dependencies array, we will have an infinite loop.

```js
function MyComponent() {
  const [data, setData] = useState([])  
    
  useEffect(() => {
    fetchData().then(myData => setData(myData))
    // Error! useEffect runs after every render without the dependencies array, causing infinite loop
  }); 
}
```

After the first render, useEffect will be run, state will be updated, which will cause a re-render, which will cause useEffect to run again, starting the process over again ad infinitum. 

This is called an **infinite loop** and this effectively breaks our application. 

If you are updating state within your useEffect, make sure to provide an empty dependencies array. If you do provide an empty array, which I recommend you do by default for any time that you use useEffect, this will cause the effect function to only run once after the component has rendered the first time. 

A common example for this is to fetch data. For a component, you may just want to fetch data once, put it in state, and then display it in your JSX.

```js
function MyComponent() {
  const [data, setData] = useState([])  
    
  useEffect(() => {
    fetchData().then(myData => setData(myData))
    // Correct! Runs once after render with empty array
  }, []); 
   
  return <ul>{data.map(item => <li key={item}>{item}</li>)}</ul>
}
```

## What is the cleanup function in useEffect?

The final part of performing side effects properly in React is the **effect cleanup function**.

Sometimes our side effects need to be shut off. For example, if you have a countdown timer using the `setInterval` function, that interval will not stop unless we use the `clearInterval` function. 

Another example is to use subscriptions with WebSockets. Subscriptions need to be "turned off" when we are no longer using them, and this is what the cleanup function is for. 

If we are setting state using `setInterval` and that side effect is not cleaned up, when our component unmounts and we're no longer using it, the state is destroyed with the component – but the `setInterval` function will keep running.

```js
function Timer() {
  const [time, setTime] = useState(0);
    
  useEffect(() => {
    setInterval(() => setTime(1), 1000); 
    // counts up 1 every second
    // we need to stop using setInterval when component unmounts
  }, []);
}
```

The problem with this if the component is destroying, is that `setInterval` will try to update a variable a piece of state `time` that no longer exists. This is an error called a memory leak.

To use the cleanup function, we need to return a function from within the useEffect function. 

Within this function we can perform our cleanup, in this case to use `clearInterval` and stop `setInterval`. 

```js
function Timer() {
  const [time, setTime] = useState(0);
    
  useEffect(() => {
    let interval = setInterval(() => setTime(1), 1000); 

    return () => {
      // setInterval cleared when component unmounts
      clearInterval(interval);
    }
  }, []);
}
```

The cleanup function will be called when the component is unmounted.

A common example of a component being unmounted is going to a new page or a new route in our application where the component is no longer rendered. 

When a component is unmounted, our cleanup function runs, our interval is cleared, and we no longer get an error of attempting to update a state variable that doesn't exist. 

Finally, the side effect cleanup is not required in every case. It is only required in a few cases, such as when you need to stop a repeated side effect when your component unmounts.

## Become a Professional React Developer

React is hard. You shouldn't have to figure it out yourself.

I've put everything I know about React into a single course, to help you reach your goals in record time:

[**Introducing: The React Bootcamp**](https://www.thereactbootcamp.com)

**It’s the one course I wish I had when I started learning React.**

Click below to try the React Bootcamp for yourself:

[![Click to join the React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Click to get started*

