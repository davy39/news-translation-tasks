---
title: How to Use React Hooks – useEffect, useState, and useContext Code Examples
subtitle: ''
author: Joan Ayebola
co_authors: []
series: null
date: '2023-12-04T18:38:16.000Z'
originalURL: https://freecodecamp.org/news/react-hooks-useeffect-usestate-and-usecontext
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/Orange-and-Yellow-Retro-Flower-Power-Daily-Class-Agenda-Template.png
tags:
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
seo_title: null
seo_desc: "React is a powerful JavaScript library for building user interfaces. And\
  \ it has undergone significant changes over the years. \nOne of the most noteworthy\
  \ additions is the introduction of hooks, which revolutionized the way developers\
  \ manage state and..."
---

React is a powerful JavaScript library for building user interfaces. And it has undergone significant changes over the years. 

One of the most noteworthy additions is the introduction of hooks, which revolutionized the way developers manage state and side effects in functional components. 

In this guide, we'll explore three fundamental hooks for beginners: `useState`, `useEffect`, and `useContext`.

## Introduction to React Hooks

Before hooks, stateful logic in React was primarily managed using class components. 

With the advent of functional components and hooks, developers gained a more concise and expressive way to handle state and lifecycle methods. Hooks allow you to use state and other React features without writing a class.

### What are React Hooks?

React hooks are functions that enable functional components to use state and lifecycle features that were previously only available in class components. They were introduced in React 16.8 to provide a more consistent way to manage stateful logic in functional components.

## How to Use the `useState` Hook

The `useState` hook is perhaps the most basic and essential hook in React. It enables you to add state to your functional components, allowing them to keep track of data that changes over time. Let's dive into how `useState` works with a simple example.

### Basic Usage of `useState`

```jsx
import React, { useState } from 'react';

const Counter = () => {
  // Declare a state variable named 'count' with an initial value of 0
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
};

export default Counter;

```

In this example, we import the `useState` hook from the 'react' library. The `useState` function returns an array with two elements: the current state value (`count`) and a function (`setCount`) to update it. We initialize `count` to 0, and clicking the "Increment" button increases its value.

### How to Use Multiple `useState` Hooks

You can use the `useState` hook multiple times in a single component to manage different pieces of state independently. Let's modify our `Counter` component to include a second piece of state.

```jsx
import React, { useState } from 'react';

const Counter = () => {
  const [count, setCount] = useState(0);
  const [isEven, setIsEven] = useState(false);

  return (
    <div>
      <p>Count: {count}</p>
      <p>{isEven ? 'Even' : 'Odd'}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
      <button onClick={() => setIsEven(!isEven)}>Toggle Even/Odd</button>
    </div>
  );
};

export default Counter;

```

Now, our `Counter` component has two independent pieces of state: `count` and `isEven`. Clicking the "Toggle Even/Odd" button will switch the value of `isEven`.

## How to Use the `useEffect` Hook

The `useEffect` hook is used to perform side effects in your functional components, such as fetching data, subscribing to external events, or manually changing the DOM. It combines the functionality of `componentDidMount`, `componentDidUpdate`, and `componentWillUnmount` in class components.

### Basic Usage of `useEffect`

```jsx
import React, { useState, useEffect } from 'react';

const DataFetcher = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    // Fetch data from an API
    fetch('https://api.example.com/data')
      .then((response) => response.json())
      .then((result) => setData(result))
      .catch((error) => console.error('Error fetching data:', error));
  }, []); // Empty dependency array means this effect runs once after the initial render

  return (
    <div>
      {data ? (
        <ul>
          {data.map((item) => (
            <li key={item.id}>{item.name}</li>
          ))}
        </ul>
      ) : (
        <p>Loading data...</p>
      )}
    </div>
  );
};

export default DataFetcher;

```

In this example, the `useEffect` hook is used to fetch data from an API when the component mounts. The second argument of `useEffect` is an array of dependencies. If the dependencies change between renders, the effect will run again. An empty array means the effect runs once after the initial render.

### Cleaning Up in `useEffect`

Sometimes, side effects need to be cleaned up, especially when dealing with subscriptions or timers to prevent memory leaks. The `useEffect` hook can return a cleanup function that will be executed when the component unmounts.

```jsx
import React, { useState, useEffect } from 'react';

const Timer = () => {
  const [seconds, setSeconds] = useState(0);

  useEffect(() => {
    const intervalId = setInterval(() => {
      setSeconds((prevSeconds) => prevSeconds + 1);
    }, 1000);

    // Cleanup function to clear the interval when the component unmounts
    return () => clearInterval(intervalId);
  }, []); // Empty dependency array for initial setup only

  return <p>Seconds: {seconds}</p>;
};

export default Timer;

```

In this example, the `setInterval` function is used to update the `seconds` state every second. The cleanup function returned by `useEffect` clears the interval when the component is unmounted.

## How to Use the `useContext` Hook

The `useContext` hook is used to consume values from a React context. Context provides a way to pass data through the component tree without having to pass props manually at every level. Let's explore how `useContext` works with a simple example.

### How to Create a Context

First, let's create a context to hold a user's authentication status.

```jsx
import React, { createContext, useContext, useState } from 'react';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  const login = () => {
    setIsAuthenticated(true);
  };

  const logout = () => {
    setIsAuthenticated(false);
  };

  return (
    <AuthContext.Provider value={{ isAuthenticated, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  return useContext(AuthContext);
};

```

In this example, we create an `AuthContext` using `createContext` and provide an `AuthProvider` component. The `AuthProvider` component wraps its children with the context provider and includes functions for logging in and out.

### How to Use `useContext`

Now, let's use the `useContext` hook in a component to access the authentication status.

```jsx
import React from 'react';
import { useAuth } from './AuthContext';

const AuthStatus = () => {
  const { isAuthenticated, login, logout } = useAuth();

  return (
    <div>
      <p>User is {isAuthenticated ? 'logged in' : 'logged out'}</p>
      <button onClick={login}>Login</button>


      <button onClick={logout}>Logout</button>
    </div>
  );
};

export default AuthStatus;

```

Here, the `useAuth` hook is used to access the values provided by the `AuthContext`. The `AuthStatus` component displays the user's login status and provides buttons to log in and out.

## Putting It All Together

Let's create a more complex example that combines `useState`, `useEffect`, and `useContext` in a single component. Suppose we have a component that fetches user data from an API and displays it, taking into account the user's authentication status.

```jsx
import React, { useState, useEffect } from 'react';
import { useAuth } from './AuthContext';

const UserProfile = () => {
  const { isAuthenticated } = useAuth();
  const [userData, setUserData] = useState(null);

  useEffect(() => {
    if (isAuthenticated) {
      // Fetch user data when authenticated
      fetch('https://api.example.com/user')
        .then((response) => response.json())
        .then((result) => setUserData(result))
        .catch((error) => console.error('Error fetching user data:', error));
    }
  }, [isAuthenticated]); // Run the effect when isAuthenticated changes

  return (
    <div>
      {isAuthenticated ? (
        <div>
          <h2>Welcome, {userData ? userData.name : 'User'}!</h2>
          <p>Email: {userData ? userData.email : 'Loading...'}</p>
        </div>
      ) : (
        <p>Please log in to view your profile.</p>
      )}
    </div>
  );
};

export default UserProfile;

```

In this example, the `UserProfile` component uses the `useAuth` hook to check the user's authentication status. If authenticated, it fetches the user data and displays a personalized welcome message. If not authenticated, it prompts the user to log in.

## Conclusion

React hooks, including `useState`, `useEffect`, and `useContext`, have transformed the way developers write components by providing a more intuitive and flexible approach to managing state and side effects. 

As you continue your journey with React, mastering these hooks will empower you to build more efficient and maintainable applications.

Remember, practice is key to becoming proficient with React hooks. Experiment with different scenarios, explore additional hooks like `useReducer` and `useCallback`, and stay up-to-date with the React documentation for any new features or best practices. Happy coding!

