---
title: React Lifecycle Methods and Hooks – a Beginner's Guide
subtitle: ''
author: Casmir Onyekani
co_authors: []
series: null
date: '2023-10-02T17:22:49.000Z'
originalURL: https://freecodecamp.org/news/react-lifecycle-methods-and-hooks-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/lifecycle.jpg
tags:
- name: hooks
  slug: hooks
- name: lifecycle methods
  slug: lifecycle-methods
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
seo_title: null
seo_desc: 'React is all about building user interfaces. And to do that effectively,
  React provides ways for components to manage their lifecycles.

  This means that components can perform specific tasks at different stages of their
  existence, from the moment they...'
---

[React](https://www.freecodecamp.org/news/react-beginner-handbook/#howmuchjavascriptyouneedtoknowtousereact) is all about building user interfaces. And to do that effectively, React provides ways for components to manage their lifecycles.

This means that components can perform specific tasks at different stages of their existence, from the moment they are created to the point they are removed from the user interface.

Lifecycle methods have been a fundamental part of React for many years. But with the introduction of hooks, React's approach to managing state and side effects in functional components has become more intuitive and flexible.

Just a quick note: although hooks generally replace class components, there are no plans to remove classes from React.

### Why This Guide?

In this tutorial, you will learn about class component lifecycle methods such as `componentDidMount`, `componentDidUpdate`, `componentWillUnmount`, and `shouldComponentUpdate`.

You'll also explore React hooks like `useState`, `useEffect`, and `useContext`, and understand why they were introduced. This will make your React journey smoother and more enjoyable.

Whether you're just getting started with React or looking to deepen your understanding, this guide will equip you with the knowledge you need to build responsive and interactive web applications using React's powerful tools.

Let's dive in and uncover the magic of React lifecycle methods and hooks.

## How the Component Lifecycle Works

In React, components go through a lifecycle composed of distinct stages. Each of these stages offers specific methods that you can customize to run code at various moments during a component's existence.

These methods help you perform tasks such as initializing data, managing updates, and tidying up resources as needed.

### Class Component Lifecycle Methods

Let's start by looking at the class component lifecycle methods. These were the primary way to manage component lifecycle before the introduction of hooks.

#### How to use `componentDidMount`:

This is called after a component has been inserted into the DOM. It's a great place to perform initial setup tasks, like fetching data from an API or setting up event listeners.

Code example:

```jsx

import React, { Component } from 'react';

class MyComponent extends React.Component {
  constructor() {
    super();
    this.state = {
      data: null,
    };
  }

  componentDidMount() {
    // This is where you can perform initial setup.
    
    // In this example, we simulate fetching data from an API after the     		component has mounted.
    // We use a setTimeout to mimic an asynchronous operation.
    setTimeout(() => {
      const fetchedData = 'This data was fetched after mounting.';
      this.setState({ data: fetchedData });
    }, 2000); // Simulate a 2-second delay
  }

  render() {
    return (
      <div>
        <h1>componentDidMount Example</h1>
        {this.state.data ? (
          <p>Data: {this.state.data}</p>
        ) : (
          <p>Loading data...</p>
        )}
      </div>
    );
  }
}

export default MyComponent;
```

In this example, we created a class component called `MyComponent`. In the constructor, the component's state is initialized with data set to null, and we use it to store the fetched data.

In the `componentDidMount` method, we simulate fetching data from an API using `setTimeout` to mimic an asynchronous operation. After 2 seconds (2000 milliseconds), the component's state updates with the fetched data.

In the render method, content is conditionally rendered based on the data state. If data is null, a `Loading data...` message is displayed. Otherwise, the fetched data is displayed.

When you use this component in your application, you'll notice that the Loading data... message is shown initially, and after 2 seconds, the fetched data is displayed. This demonstrates how `componentDidMount` is useful for performing tasks after a component has been added to the DOM.

#### How to use `componentDidUpdate`B:

This is called after a component has re-rendered due to changes in its state or props. It's a great place to handle side effects or perform additional actions based on those changes.

Code Example:

```jsx
import React, { Component } from 'react';

class Counter extends React.Component {
  constructor() {
    super();
    this.state = {
      count: 0,
    };
  }

  // This method will be called when the "Increment" button is clicked
  handleIncrement = () => {
    this.setState({ count: this.state.count + 1 });
  };

  // componentDidUpdate is called after the component updates
  componentDidUpdate(prevProps, prevState) {
    // You can access the previous props and state here
    console.log('Component updated');
    console.log('Previous state:', prevState);
    console.log('Current state:', this.state);
  }

  render() {
    return (
      <div>
        <h1>Counter</h1>
        <p>Count: {this.state.count}</p>
        <button onClick={this.handleIncrement}>Increment</button>
      </div>
    );
  }
}

export default Counter;
```

In this code example, we create a `Counter` class component with a constructor that initializes the `count` state to 0. The `handleIncrement` method updates the count state when the *Increment* button is clicked.

Inside the `componentDidUpdate` lifecycle method, we log a message (Component updated) to the console. We also log both the previous state (prevState) and the current state (this.state). This demonstrates how you can access both the previous and current values during an update. The render method displays the current count and a button to increment it.

Now, when you use this `Counter` component in your application, open the browser's console. Every time you click the *Increment* button, you'll see messages in the console indicating that the component has updated, along with the previous and current state values.

You can use `componentDidUpdate` for various purposes, such as making network requests when props or state change, updating the DOM based on state changes, or interacting with third-party libraries after an update. It provides a way to perform actions that should occur specifically after a component has re-rendered.

#### How to use `componentWillUnmount`

This is called just before a component is removed from the DOM. It's a crucial place to perform cleanup tasks, such as clearing timers, unsubscribing from events, or releasing resources to prevent \[memory leaks\](https://en.wikipedia.org/wiki/Memory\_leak#:~:text=In computer science%2C a memory,longer needed is not released.).

Let's illustrate a simple React component that sets up a timer when it mounts, using `componentDidMount` method, and clears that timer when it unmounts using the `componentWillUnmount` method.

Code example:

```jsx
import React, { Component } from 'react';

class TimerComponent extends React.Component {
  constructor() {
    super();
    this.state = {
      seconds: 0,
    };
    this.timer = null; // Initialize the timer
  }

  // When the component mounts, start the timer
  componentDidMount() {
    this.timer = setInterval(() => {
      this.setState({ seconds: this.state.seconds + 1 });
    }, 1000); // Update every 1 second (1000 milliseconds)
  }

  // When the component unmounts, clear the timer to prevent memory leaks
  componentWillUnmount() {
    clearInterval(this.timer);
  }

  render() {
    return (
      <div>
        <h1>Timer Component</h1>
        <p>Elapsed Time: {this.state.seconds} seconds</p>
      </div>
    );
  }
}

export default TimerComponent;
```

In this example, we created the `TimerComponent` class. Inside the constructor, the component's state is initialized with a seconds property, which we'll use to keep track of the elapsed time. The timer variable is also set to null.

In the `componentDidMount` lifecycle method, the timer is started by using `setInterval`. This timer increments the seconds state property every second.

In the `componentWillUnmount` lifecycle method, the timer is cleared using `clearInterval` to ensure that it doesn't continue running after the component has been removed from the DOM.

In the render method, the elapsed time is displayed based on the seconds state property.

When you use this `TimerComponent` in your application and render it, you'll notice that the timer starts when the component is mounted and stops when the component is unmounted. This is thanks to the cleanup performed in the `componentWillUnmount` method. This prevents resource leaks and ensures that  
the timer is properly managed throughout the component's lifecycle.

#### How to use `shouldComponentUpdate`

We use this lifecycle method to control whether a component should re-render when its state or props change. It is particularly useful for optimizing performance by preventing unnecessary renders.

Let's create a simple React class component and use the `shouldComponentUpdate` method to decide whether the component should re-render based on changes in its state.

Code Example:

```jsx
import React, { Component } from 'react';

class Counter extends React.Component {
  constructor() {
    super();
    this.state = {
      count: 0,
    };
  }

  shouldComponentUpdate(nextProps, nextState) {
    // Allow the component to re-render only if the count is even
    if (nextState.count % 2 === 0) {
      return true; // Re-render
    }
    return false; // Don't re-render
  }

  incrementCount = () => {
    this.setState((prevState) => ({ count: prevState.count + 1 }));
  };

  render() {
    return (
      <div>
        <h1>Counter Example</h1>
        <p>Count: {this.state.count}</p>
        <button onClick={this.incrementCount}>Increment</button>
      </div>
    );
  }
}

export default Counter;
```

In this example, we created the `Counter` class component that maintains a count state, which starts at 0. In the `shouldComponentUpdate` method, we check whether the next state's count is even. If it is, we allow the component to re-render. Otherwise, we prevent the re-render.

The `incrementCount` method is called when the *Increment* button is clicked. It updates the count state by incrementing it.

In the render method, the current count and a button to increment it is displayed.

If you click the *Increment* button and the count becomes an odd number, the component won't re-render. This behavior demonstrates how `shouldComponentUpdate` can be used to optimize rendering in situations where not all state changes should trigger a re-render.

## Introducing React Hooks

React introduced hooks in version 16.8. They granted functional components access to state and various React features without writing class components.

As a result, class components have become largely unnecessary. Hooks simplify component logic and make it more reusable.

### Why use Hooks?

Hooks were introduced to address several issues and make React code easier to understand and maintain:

* Complexity – class components can become complex when managing state and side effects.
    
* Reusability – logic in class components isn't easily shareable between components.
    
* Learning Curve – class components introduce a steeper learning curve for newcomers to React.
    

### Commonly used React Hooks

#### The `useState` hook

`useState` lets you add state to functional components. It returns an array with the current state value and a function to update it.

Code Example:

```jsx
import React, { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}
```

In this example, we used the `useState` hook to manage a counter's state. When the Increment button is clicked, `setCount` updates the count state, causing the component to re-render with the updated value.

#### The `useEffect` hook

`useEffect` is used for side effects in functional components, similar to `componentDidMount` and `componentDidUpdate`. It runs after rendering and can be controlled by specifying dependencies.

Code Example:

```jsx
import React, { useState, useEffect } from 'react';

function Example() {
  const [data, setData] = useState(null);

  useEffect(() => {
    // Fetch data from an API
    fetch('https://api.example.com/data')
      .then(response => response.json())
      .then(data => setData(data));
  }, []); // Empty dependency array, runs only once

  return <div>{data ? data.message : 'Loading...'}</div>;
}
```

In this example, `useEffect` is used to fetch data from an API when the component mounts. The empty dependency array `[]` ensures that the effect runs only once.  
When the data is fetched, `setData` updates the data state, causing a re-render with the fetched information.

#### The `useContext` hook

`useContext` allows functional components to access context values. It's a way to pass data down the component tree without explicitly passing props.

Code Example:

```jsx

import React, { useContext } from 'react';

// Create a context
const MyContext = React.createContext();

function MyComponent() {
  const value = useContext(MyContext);

  return <div>Context Value: {value}</div>;
}
```

In this example, we create a context called `MyContext`. The `useContext` hook allows `MyComponent` to access the value stored in this context. It's a powerful tool for managing global state in your application.

### Benefits of custom hooks

Custom hooks are functions that use hooks internally and can be reused across multiple components. They help encapsulate and share complex logic.

Here's an example of a custom hook called `useLocalStorage` that simplifies storing and retrieving data in the browser's local storage:

```jsx
import { useState } from 'react';

function useLocalStorage(key, initialValue) {
  // Retrieve the stored value from local storage
  const storedValue = localStorage.getItem(key);

  // Initialize the state with the stored value or the initial value
  const [value, setValue] = useState(storedValue || initialValue);

  // Update the local storage whenever the state changes
  const setStoredValue = (newValue) => {
    setValue(newValue);
    localStorage.setItem(key, newValue);
  };

  return [value, setStoredValue];
}

export default useLocalStorage;
```

In this custom hook, we import `useState` from React because we'll use it to manage the state. The `useLocalStorage` function takes two parameters:

* **key**: A string representing the key under which the data will be stored in local storage.
    
* `**initialValue**`: The initial value for the state.
    

Inside the hook, we first attempted to retrieve the stored value from local storage using `localStorage.getItem(key)`. Then we initialized the state variable value using `useState`, using the `storedValue` if it exists or the `initialValue` if not.

Next, we defined a function `setStoredValue` that updates both the state and the local storage when called. It sets the new value in local storage using `localStorage.setItem(key, newValue)`.

Finally, we returned an array `[value, setStoredValue]` as the hook's return value, allowing components to access the stored value and update it as needed.

Here's an example of how you can use the `useLocalStorage` hook in a component:

```jsx
import React from 'react';
import useLocalStorage from './useLocalStorage'; // Import the custom hook

function App() {
  // Use the custom hook to manage a "username" stored in local storage
  const [username, setUsername] = useLocalStorage('username', 'Guest');

  const handleInputChange = (e) => {
    setUsername(e.target.value);
  };

  return (
    <div>
      <h1>Hello, {username}!</h1>
      <input
        type="text"
        placeholder="Enter your username"
        value={username}
        onChange={handleInputChange}
      />
    </div>
  );
}

export default App;
```

In this example, we import the `useLocalStorage` custom hook and use it to manage a username value in local storage. The component initializes the username state using the hook and updates it when the input field changes.

The value is stored and retrieved from local storage, allowing it to persist across page reloads.

Custom hooks are a powerful way to encapsulate and reuse complex logic in React applications, making your code more modular and maintainable.

## Conclusion

React provides developers with powerful tools to manage the lifecycles of their components. These lifecycles allow components to perform specific tasks at different stages of their existence, from creation to removal.

In this guide, we've explored React's class component lifecycle methods. These methods have been a fundamental part of React for many years and continue to be relevant in certain scenarios.

You've also been introduced to React Hooks. These have become the preferred way to manage state and side effects in React applications. They offer a more intuitive and flexible approach to building components.

While hooks have gained popularity and generally replace the need for class components, it's important to note that there are no plans to remove class components from React. Existing codebases and third-party libraries may still use class components, so understanding both class component lifecycles and hooks is  
valuable for React developers.

In summary, React's lifecycle methods and hooks are crucial for building dynamic and efficient applications, and they offer developers a range of options to manage component behavior and state. As you continue to explore and work with React,  
you'll find that having a solid understanding of both lifecycles and hooks will make you a more versatile and capable React developer.

If you found this guide helpful and enjoyable, please give it a like. For more insightful tutorials, follow me on [X](https://twitter.com/casweb_dev) for updates 🙏.

Enjoy your coding!
