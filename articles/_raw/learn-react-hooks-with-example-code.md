---
title: Learn React Hooks – Common Hooks Explained with Code Examples
subtitle: ''
author: Prankur Pandey
co_authors: []
series: null
date: '2024-09-25T16:04:35.573Z'
originalURL: https://freecodecamp.org/news/learn-react-hooks-with-example-code
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1727212733982/7c9b8ae3-e8ac-4e20-b154-7edc60a6985a.avif
tags:
- name: React
  slug: reactjs
- name: ReactHooks
  slug: reacthooks
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'Web development is a popular field in the tech industry. It involves building
  web software using HTML, CSS, and JavaScript – sometimes with the help of various
  frameworks and libraries.

  Using libraries and frameworks allows developers to focus more o...'
---

Web development is a popular field in the tech industry. It involves building web software using HTML, CSS, and JavaScript – sometimes with the help of various frameworks and libraries.

Using libraries and frameworks allows developers to focus more on the development while the tools take care of certain functionality in the background. And React.js is a popular JavaScript library for building front-end applications.

In this article, you’ll learn about the backbone of React which is **Hooks,** and how they can make your life easier as a developer.

## What We’ll Cover:

* [Prerequisites:](#heading-prerequisites)
    
* [Getting Started](#heading-getting-started)
    
* [What are Hooks?](#heading-what-are-hooks)
    
* [Types of React Hooks](#heading-types-of-react-hooks)
    
    * [State Management Hooks](#heading-state-management-hooks)
        
    * [Effect Hooks](#heading-effect-hooks)
        
    * [Ref Hook](#heading-ref-hook)
        
    * [Performance Hooks](#heading-performance-hooks)
        
    * [Context Hook](#heading-context-hook)
        
    * [Transition Hook](#heading-transition-hook)
        
    * [Some Random Hooks](#heading-some-random-hooks)
        
* [Conclusion](#heading-conclusion)
    

## Prerequisites:

* You should know the basics of JavaScript.
    
* You should also know the basics of React, like setting up an app, updating it, and using state.
    

## Getting Started

So you've decided to build a React app—congratulations! 🎉 But as you dive into the world of React hooks, you might find yourself feeling overwhelmed. With a plethora of hooks available, figuring out which ones to use and when can be a bit daunting.

Well, don’t worry – in this guide, I’ll break down every major hook so you can see how they fit together. We’ll also discuss which ones you'll use more frequently versus more rarely.

By the end of this article, you'll have a comprehensive map of React hooks and their practical applications.

## **What are Hooks?**

In JavaScript, we use variables to store data and later perform operations on that data.

Hooks in React work similarly, but they are designed to manage state in **functional components**. Instead of manually declaring a single variable, hooks like `useState` give us a way to declare stateful values along with a setter function to update that state.

Here’s a simple example:

```javascript
import React, { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);  // Initialize state and state updater

  return (
    <div>
      <p>You clicked {count} times</p>
      <button onClick={() => setCount(count + 1)}>Click me</button>
    </div>
  );
}
```

In this code, I use the `useState` hook to declare a piece of state called `count` and set its initial value to 0. The `setCount` function allows us to update this state. Every time the button is clicked, we use `setCount` to increase `count` by 1. When the state updates, React re-renders the component to reflect the change.

Unlike declaring `let count = 0`, using `useState` lets React remember the state across renders and ensures that the UI updates correctly.

## Types of React Hooks

To make things easier, you can think of React hooks as falling into eight major categories:

* **State Management Hooks** – For handling state.
    
* **Effect Hooks** – For side effects.
    
* **Ref Hooks** – For referencing JavaScript values or DOM elements.
    
* **Performance Hooks** – For optimizing performance.
    
* **Context Hooks** – For accessing React context.
    
* **Transition Hooks** – For smoother user experiences.
    
* **Some Random Hooks** – Special-purpose hooks.
    
* **New Hooks (React 19)** – Cutting-edge tools introduced in the latest React version.
    

In React, you can also build custom hooks for different use cases. Every hook starts with the `use` keyword – even custom hooks start with this structure. This keyword is reserved for Hooks in React.

Let’s explore these hooks in detail.

### **State Management Hooks**

#### **1.** `useState`

The `useState` hook is the bread and butter of React. It’s the most commonly used hook, and it’s key for managing state in functional components. With `useState`, you can capture user inputs, show or hide components, and manage numbers, like in an ecommerce app with a shopping cart.

`useState` is versatile and straightforward: you initialize it with a value, and it returns a state variable and an updater function.

```jsx
import React, { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);  // Initialize state and state updater

  return (
    <div>
      <p>You clicked {count} times</p>
      <button onClick={() => setCount(count + 1)}>Click me</button>
    </div>
  );
}
```

**Code explanation**: `useState` initializes the state (count) and provides a function (`setCount`) to update that state.

#### **2\.** `useReducer`

When `useState` isn’t enough, `useReducer` comes into play. This hook is perfect for managing complex state logic.

It uses a reducer function to simplify state updates and is especially useful when multiple state variables are interdependent or when actions need to be dispatched.

Think of it as an upgrade for managing more complicated state scenarios. Here’s an example:

```jsx
import React, { useReducer } from 'react';

const initialState = { count: 0 };

function reducer(state, action) {
  switch (action.type) {
    case 'increment':
      return { count: state.count + 1 };
    case 'decrement':
      return { count: state.count - 1 };
    default:
      return state;
  }
}

function Counter() {
  const [state, dispatch] = useReducer(reducer, initialState);

  return (
    <div>
      <p>Count: {state.count}</p>
      <button onClick={() => dispatch({ type: 'increment' })}>+</button>
      <button onClick={() => dispatch({ type: 'decrement' })}>-</button>
    </div>
  );
}
```

**Code explanation**: `useReducer` is useful for managing complex state updates, like handling multiple related actions.

**3\.** `useSyncExternalStore`  
`useSyncExternalStore` is a hook for integrating non-React state stores into your React components.

While not commonly used, it’s crucial if you’re building your own state management library from scratch.

```jsx
import React, { useSyncExternalStore } from 'react';

const externalStore = {
  subscribe: (callback) => {
    const interval = setInterval(callback, 1000);
    return () => clearInterval(interval);
  },
  getSnapshot: () => new Date().toLocaleTimeString(),
};

function Clock() {
  const time = useSyncExternalStore(externalStore.subscribe, externalStore.getSnapshot);
  return <div>{time}</div>;
}
```

**Code explanation**: `useSyncExternalStore` lets you connect your React component to non-React data sources, like global stores.

### **Effect Hooks**

**1.** `useEffect`  
The `useEffect` hook performs side effects on your components. Whether you’re interacting with the DOM or fetching data, `useEffect` is your go-to. It runs after each render by default, but you can customize its behavior using a dependency array.

But you should consider using more specialized tools or libraries like React Query for event-based or render-based side effects.

```jsx
import React, { useState, useEffect } from 'react';

function DataFetcher() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch('https://api.example.com/data')
      .then((response) => response.json())
      .then((data) => setData(data));
  }, []);  // Empty dependency array means it runs once on mount

  return <div>{data ? JSON.stringify(data) : 'Loading...'}</div>;
}
```

**Code explanation**: The `useEffect` hook fetches data when the component mounts. The effect will only run one time when the array is empty.

**2\.** `useLayoutEffect`  
`useLayoutEffect` works similarly to `useEffect` but runs synchronously right after the DOM has been updated. It’s used for operations that need to happen before the browser paints the UI, like measuring elements.

Use it sparingly, as it runs less frequently than `useEffect`. Here’s an example:

```jsx
import React, { useLayoutEffect, useRef } from 'react';

function Measure() {
  const divRef = useRef();

  useLayoutEffect(() => {
    console.log(divRef.current.getBoundingClientRect());
  }, []);

  return <div ref={divRef}>Measure me!</div>;
}
```

**Code explanation**: `useLayoutEffect` measures DOM elements before the browser repaints.

**3\.** `useInsertionEffect`  
Exclusively for CSS-in-JS library developers, `useInsertionEffect` runs before `useEffect` and `useLayoutEffect` to ensure that CSS styles are inserted properly. It’s niche, but crucial for maintaining style integrity in complex applications.

```jsx
import React, { useInsertionEffect, useState } from 'react';

function StyledComponent() {
  const [text, setText] = useState('Hover over me!');

  useInsertionEffect(() => {
    const style = document.createElement('style');
    style.textContent = `
      .hovered {
        color: red;
        font-size: 24px;
        transition: color 0.3s ease;
      }
    `;
    document.head.appendChild(style);

    return () => {
      document.head.removeChild(style);
    };
  }, []);

  return (
    <div
      className="hovered"
      onMouseEnter={() => setText('You hovered over me!')}
      onMouseLeave={() => setText('Hover over me!')}
    >
      {text}
    </div>
  );
}
```

**Code explanation**: The `useInsertionEffect` hook is used to inject styles into the DOM at runtime, making the component’s styling dynamic and scoped only to that component.

### **Ref Hook**

1\. `useRef`  
`useRef` allows you to persist values across renders without causing re-renders. It's perfect for storing mutable values or referencing DOM elements. Whether you’re handling intervals, storing a DOM node, or keeping track of the previous state, `useRef` has you covered.

```jsx
import React, { useRef } from 'react';

function FocusInput() {
  const inputRef = useRef(null);

  const handleFocus = () => {
    inputRef.current.focus();
  };

  return (
    <div>
      <input ref={inputRef} type="text" />
      <button onClick={handleFocus}>Focus Input</button>
    </div>
  );
}
```

**Code explanation:** This React code uses `useRef` to create a reference to an input element. When the button is clicked, the `handleFocus` function triggers the input field to gain focus using `inputRef.current.focus()`.

### **Performance Hooks**

**1\.** `useMemo`  
For optimizing performance, `useMemo` is your friend. It caches the results of expensive computations and only recalculates when dependencies change. This can significantly improve performance, especially in scenarios involving heavy calculations.

```jsx
import React, { useState, useMemo } from 'react';

function ExpensiveCalculation() {
  const [count, setCount] = useState(0);

  const expensiveComputation = useMemo(() => {
    return count * 100;
  }, [count]);

  return (
    <div>
      <p>Expensive Computation: {expensiveComputation}</p>
      <button onClick={() => setCount(count + 1)}>Increase Count</button>
    </div>
  );
}
```

**Code explanation:**This React code uses `useMemo` to optimize an expensive calculation (`count * 100`). The calculation only re-runs when `count` changes. The button increments `count`, triggering a UI update with the new result.

**2\.** `useCallback`  
`useCallback` is similar to `useMemo`, but it focuses on memoizing callback functions. This is useful for preventing unnecessary re-renders of child components by keeping functions stable across renders.

```jsx
import React, { useState, useCallback } from 'react';

function Child({ onClick }) {
  return <button onClick={onClick}>Click me</button>;
}

function Parent() {
  const [count, setCount] = useState(0);

  const handleClick = useCallback(() => {
    console.log('Clicked');
  }, []);

  return (
    <div>
      <Child onClick={handleClick} />
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increase Count</button>
    </div>
  );
}
```

**Code explanation:** This React code uses `useCallback` to memoize the `handleClick` function, preventing re-creation on every render. The `Child` component uses this function for its button. The parent updates `count` independently.

### **Context Hook**

1\. `useContext`  
The `useContext` hook simplifies accessing context values. It reads the value from the nearest context provider and works seamlessly across nested components. This makes it easier to manage global states or themes.

```jsx
import React, { useContext, createContext } from 'react';

const ThemeContext = createContext('light');

function ThemedButton() {
  const theme = useContext(ThemeContext);
  return <button>{theme}</button>;
}

function App() {
  return (
    <ThemeContext.Provider value="dark">
      <ThemedButton />
    </ThemeContext.Provider>
  );
}
```

**Code explanation**: This React code uses `createContext` to create a `ThemeContext`. `useContext` accesses the context value, displaying it in the button. The `App` component provides "dark" as the theme to `ThemedButton`.

### **Transition Hook**

1\. `useTransition`  
`useTransition` lets you mark specific state updates as low-priority, enhancing the user experience by keeping the app more responsive during intensive computations or transitions. This improves the user experience by making the app more responsive.

```jsx
import React, { useState, useTransition } from 'react';

function TransitionComponent() {
  const [count, setCount] = useState(0);
  const [isPending, startTransition] = useTransition();

  const handleClick = () => {
    startTransition(() => {
      setCount((prevCount) => prevCount + 1);
    });
  };

  return (
    <div>
      <button onClick={handleClick}>Increase Count</button>
      {isPending ? <p>Loading...</p> : <p>Count: {count}</p>}
    </div>
  );
}
```

**Code explanation:** This code uses `useTransition` to increment `count` without blocking the UI. While the state updates, `isPending` shows "Loading...". Clicking the button triggers a smooth, non-blocking state transition.

### **Some Random Hooks**

**1.** `useDeferredValue`  
Similar to `useTransition`, `useDeferredValue` helps in deferring state updates to keep the app responsive. It schedules updates to happen at an optimal time, enhancing the user experience without manual intervention.

```jsx
import React, { useState, useDeferredValue } from 'react';

function DeferredComponent() {
  const [value, setValue] = useState('');
  const deferredValue = useDeferredValue(value);

  return (
    <div>
      <input value={value} onChange={(e) => setValue(e.target.value)} />
      <p>Deferred Value: {deferredValue}</p>
    </div>
  );
}
```

**Code explanation**: `useDeferredValue` delays the update of `deferredValue` to ensure that the UI remains responsive.

**2\.** `useDebugValue`  
`useDebugValue` is a hook primarily for debugging. It lets you label custom hooks in React DevTools, making it easier to track and debug your hooks.

```jsx

import React, { useDebugValue, useState } from 'react';

function useCustomHook(value) {
  useDebugValue(value ? "Has Value" : "No Value"); return value; }
function DebugComponent() { const [value, setValue] = useState(''); const customValue = useCustomHook(value);

return (
 <input value={value} onChange={(e) => setValue(e.target.value)} />
Value: {customValue}
); }
```

**Code explanation:** This code uses `useDebugValue` to show "Has Value" or "No Value" in React DevTools based on `value`. `useCustomHook` is used in `DebugComponent` to track the input state and display it dynamically.

**3\.** `useId`  
`useId` generates unique IDs for elements, ensuring that form inputs and labels are properly linked without conflicts. It’s particularly useful when dealing with dynamically repeated elements.

```javascript

import React, { useId } from 'react';

function FormComponent() {
  const id = useId();

  return (
    <div>
      <label htmlFor={id}>Name: </label>
      <input id={id} type="text" />
    </div>
  );
}
```

**Code explanation**: `useId` ensures that form elements have unique IDs, avoiding potential conflicts.

## Conclusion

React hooks can seem overwhelming at first, but with this guide, you’re well-equipped to handle them. Mastering these hooks improves your React skills and makes your development process smoother and more efficient.

For a deeper dive and hands-on practice, check out my comprehensive React Bootcamp, where you’ll find interactive challenges, videos, and cheat sheets to reinforce your knowledge.
