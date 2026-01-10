---
title: Function Components vs Class Components in React – With Examples
subtitle: ''
author: Joan Ayebola
co_authors: []
series: null
date: '2024-04-16T22:37:11.000Z'
originalURL: https://freecodecamp.org/news/function-component-vs-class-component-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2024/04/Ivory-and-Blue-Lavender-Aesthetic-Photo-Collage-Presentation--5-.png
tags:
- name: components
  slug: components
- name: React
  slug: react
seo_title: null
seo_desc: 'In React, there are two primary ways to create components: function and
  class components. Each has its own syntax and use cases, although with the introduction
  of React Hooks, the gap between them has narrowed significantly. But the selection
  of appr...'
---

In React, there are two primary ways to create components: function and class components. Each has its own syntax and use cases, although with the introduction of React Hooks, the gap between them has narrowed significantly. But the selection of appropriate component types is still very crucial for building efficient and maintainable React applications.

In this article, we'll explore the foundational differences between function and class components, providing a clear understanding of their strengths and ideal use cases. 

By understanding these concepts, developers can make informed decisions when constructing React components, ultimately enhancing the structure and functionality of their web applications.

## What are React Components?

In React, components are the building blocks of a user interface. They are reusable, self-contained pieces of code that represent a part of the UI. React allows you to break down your UI into smaller components, which makes it easier to manage and maintain your codebase.

You can think of components as custom HTML elements that encapsulate their own logic and UI structure. They can accept inputs called props (short for properties) and return React elements describing what should appear on the screen.

There are two main types of components in React:

**Function Components:** These are simple JavaScript functions that take props as input and return JSX elements. They are often used for presentational or stateless components.

**Class Components:** These are ES6 classes that extend from `React.Component` or `React.PureComponent`. They have a `render()` method where you define the structure of your component's UI using JSX. Class components are used for components that need to manage state or have lifecycle methods.

With the introduction of React Hooks, function components gained the ability to manage state and use lifecycle methods, blurring the distinction between function and class components. However, both types of components are still widely used in React applications.

## Function vs Class Components: A High-Level Overview

### Function Components

**Syntax:** Function components are defined using the `function` keyword or arrow function syntax.

```jsx
import React from 'react';

// Function component using function keyword
function FunctionComponent(props) {
  return (
    <div>
      <h1>Hello, {props.name}!</h1>
      <p>This is a function component.</p>
    </div>
  );
}

// Function component using arrow function syntax
const FunctionComponent = (props) => {
  return (
    <div>
      <h1>Hello, {props.name}!</h1>
      <p>This is a function component.</p>
    </div>
  );
};

export default FunctionComponent;

```

In the code snippet above, both examples define a function component called `FunctionComponent` that takes `props` as input and returns JSX elements. The component simply renders a greeting message along with some text. 

The first example uses the `function` keyword to define the function component, while the second example uses arrow function syntax. Both syntaxes are valid and achieve the same result.

**State Management:** Traditionally, function components were stateless and couldn't hold their own state. However, with the introduction of React Hooks (like `useState`), function components can now manage state using Hooks.

```jsx
import React, { useState } from 'react';

const FunctionComponent = () => {
  // Using useState Hook to manage state
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
};

export default FunctionComponent;

```

In this example, we use the `useState` Hook to initialize a state variable `count` with an initial value of `0`. The `useState` Hook returns an array with two elements: the current state value (`count`) and a function (`setCount`) to update the state. 

When the button is clicked, `setCount` is called with the new value of `count`, triggering a re-render with the updated state value displayed. This demonstrates how function components can now hold and manage their own state using React Hooks, making them more powerful and versatile.

**Lifecycle Methods:** Function components don't have lifecycle methods. However, with React Hooks, you can use the `useEffect` Hook to replicate lifecycle behavior (like `componentDidMount`, `componentDidUpdate`, `componentWillUnmount`, and so on).

Let's discuss some of the most commonly used lifecycle methods:

**componentDidMount:** This method is invoked immediately after a component is mounted (that is, inserted into the DOM tree). It is commonly used to perform initial setup, such as fetching data from an API or setting up event listeners.

**componentDidUpdate:** This method is invoked immediately after updating occurs. It is triggered whenever the component's props or state changes. It is commonly used to perform actions based on the updated state or props, such as making additional API calls.

**componentWillUnmount:** This method is invoked immediately before a component is unmounted and destroyed. It is commonly used to perform cleanup, such as removing event listeners or cancelling any ongoing tasks.

```jsx
import React, { useState, useEffect } from 'react';

const FunctionComponent = () => {
  const [count, setCount] = useState(0);

  // useEffect Hook to replicate componentDidMount and componentDidUpdate
  useEffect(() => {
    // This code block runs after every render
    console.log("Component did mount or update");

    // Clean-up function (replicating componentWillUnmount)
    return () => {
      console.log("Component will unmount");
    };
  });

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
};

export default FunctionComponent;

```

In this example, the `useEffect` Hook is used without a dependency array. This means the effect will run after every render, effectively replicating both `componentDidMount` and `componentDidUpdate` behavior. Inside the effect, you can perform any cleanup necessary, such as unsubscribing from subscriptions or removing event listeners, by returning a cleanup function. This cleanup function will be executed when the component unmounts, effectively replicating the `componentWillUnmount` behavior.

By leveraging the `useEffect` Hook, function components can now achieve the same lifecycle behavior as class components, further blurring the distinction between the two component types.

**Readability:** Function components are generally more concise and easier to read, especially for simpler components.

### Class Components

**Syntax:** Class components are ES6 classes that extend from `React.Component` or `React.PureComponent`. They have a `render()` method where you define the structure of your component's UI using JSX.

```jsx
import React, { Component } from 'react';

// Define a class component that extends React.Component or React.PureComponent
class ClassComponent extends Component {
  // Define constructor if necessary
  constructor(props) {
    super(props);
    // Initialize state if needed
    this.state = {
      count: 0
    };
  }

  // Define lifecycle methods if necessary
  componentDidMount() {
    // Code to run after the component is mounted
  }

  // Define instance methods if necessary
  handleClick = () => {
    // Update state or perform other logic
    this.setState({ count: this.state.count + 1 });
  }

  // Define render() method to return JSX
  render() {
    return (
      <div>
        <p>Count: {this.state.count}</p>
        <button onClick={this.handleClick}>Increment</button>
      </div>
    );
  }
}

export default ClassComponent;

```

In this example:

* We imported `React` and `Component` from the 'react' package.
* We defined a class component named `ClassComponent` that extends `Component`.
* Inside the class component, we can define a constructor to initialize state or bind event handlers if necessary.
* We can define lifecycle methods such as `componentDidMount`, `componentDidUpdate`, and so on, to hook into different stages of the component's lifecycle.
* We defined the `render()` method, which returns JSX to describe the structure of the component's UI.
* Any instance methods, event handlers, or other logic can be defined within the class.

**State Management:** Class components can hold and manage local state using the `this.state` property. They can also update state using `this.setState()`.

Let's illustrate this with a simple example:

```jsx
import React, { Component } from 'react';

class ClassComponent extends Component {
  constructor(props) {
    super(props);
    // Initialize state
    this.state = {
      count: 0
    };
  }

  // Define a method to update state
  incrementCount = () => {
    // Use this.setState() to update state
    this.setState({ count: this.state.count + 1 });
  }

  render() {
    return (
      <div>
        <p>Count: {this.state.count}</p>
        <button onClick={this.incrementCount}>Increment</button>
      </div>
    );
  }
}

export default ClassComponent;

```

In this example:

* We initialized the component's state in the constructor using `this.state`.
* The `incrementCount` method was defined within the class to update the `count` state. Inside this method, we called `this.setState()` and passed an object containing the new state or a function that returns the new state. React will merge the new state with the existing state.
* In the `render()` method, we accessed the `count` state using `this.state.count` and displayed it within the JSX.
* When the button is clicked, the `incrementCount` method is called, which updates the `count` state and triggers a re-render of the component.

This demonstrates how class components in React can manage local state and update it using `this.setState()`. 

**Lifecycle Methods:** Class components have access to various lifecycle methods like `componentDidMount`, `componentDidUpdate`, and `componentWillUnmount`, which allow you to hook into different stages of a component's lifecycle.

Here's an example demonstrating the usage of these lifecycle methods in a class component:

```jsx
import React, { Component } from 'react';

class ClassComponent extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: null
    };
  }

  componentDidMount() {
    // Fetch initial data when the component mounts
    this.fetchData();
  }

  componentDidUpdate(prevProps, prevState) {
    // Check if the data has changed
    if (prevState.data !== this.state.data) {
      // Data has changed, perform additional actions
      console.log('Data has been updated:', this.state.data);
    }
  }

  componentWillUnmount() {
    // Cleanup tasks before the component is unmounted
    console.log('Component will unmount');
    // For example, remove event listeners, cancel ongoing tasks, etc.
  }

  fetchData() {
    // Simulate fetching data from an API
    setTimeout(() => {
      this.setState({ data: 'Some data fetched from API' });
    }, 1000);
  }

  render() {
    return (
      <div>
        <p>Data: {this.state.data}</p>
      </div>
    );
  }
}

export default ClassComponent;

```

In this example:

* `componentDidMount` is used to fetch initial data when the component mounts.
* `componentDidUpdate` is used to log a message whenever the data state changes.
* `componentWillUnmount` is used to log a message before the component is unmounted.

These lifecycle methods provide hooks into different stages of a component's lifecycle, allowing you to perform setup, update, and cleanup tasks as needed. 

**Instance Methods:** You can define custom methods directly on the class, which can be helpful for organizing your component's logic.

```jsx
import React, { Component } from 'react';

class ClassComponent extends Component {
  constructor(props) {
    super(props);
    this.state = {
      count: 0
    };
  }

  // Custom method to handle incrementing count
  handleIncrement = () => {
    this.setState({ count: this.state.count + 1 });
  }

  // Custom method to handle decrementing count
  handleDecrement = () => {
    this.setState({ count: this.state.count - 1 });
  }

  render() {
    return (
      <div>
        <p>Count: {this.state.count}</p>
        <button onClick={this.handleIncrement}>Increment</button>
        <button onClick={this.handleDecrement}>Decrement</button>
      </div>
    );
  }
}

export default ClassComponent;

```

In this example:

* We defined two custom instance methods `handleIncrement` and `handleDecrement` within the class component. These methods were defined using arrow function syntax to ensure they have access to the correct `this` context.
* The `handleIncrement` method updates the `count` state by incrementing it by 1 when called.
* The `handleDecrement` method updates the `count` state by decrementing it by 1 when called.
* These custom methods are then used as event handlers for the buttons in the JSX returned by the `render` method.

Defining custom instance methods in class components helps in organizing the component's logic, making it more readable and maintainable. Additionally, these methods can be reused across different parts of the component, enhancing code reusability. 

It is important to note that, with the introduction of React Hooks, many tasks traditionally handled by class components can now be accomplished using function components. 

Hooks such as `useState`, `useEffect`, `useContext`, and others provide a simpler and more concise way to manage state, handle side effects, and share logic across components. This shift towards Hooks empowers developers to write more function and modular code, reducing the reliance on class components. 

While class components still have their place, especially in legacy codebases, the versatility and flexibility of Hooks make function components the preferred choice for building modern React applications.

## Advantages of Function Component

**Simpler Syntax:** Function components have a simpler syntax compared to class components. They are essentially just JavaScript functions that take props as input and return React elements. This simplicity makes them easier to read and understand, especially for beginners.

**Pure Functions:** Function components are essentially pure functions, meaning they only depend on their input (props) to produce output (UI). They don't have internal state or side effects, which makes them easier to reason about and test. This purity also helps improve performance, as React can optimize the rendering process more effectively.

**Reusability:** Function components promote reusability by encapsulating UI logic within small, composable functions. Since they are just JavaScript functions, they can be easily reused in multiple parts of your application, leading to more modular and maintainable code.

**Using Props in Function Components:** Function components make extensive use of props to pass data from parent to child components. This props-based approach promotes a clear and predictable data flow within your application, making it easier to understand how data is passed and used throughout your component hierarchy.

## Advantages of Class Components

**Explicit State Management:** Class components provide a clear and explicit way to manage component state using the `this.state` property. This allows developers to have fine-grained control over state management and updates within the component.

**Lifecycle Methods:** Class components have access to a range of lifecycle methods such as `componentDidMount`, `componentDidUpdate`, and `componentWillUnmount`. These methods allow developers to hook into different stages of the component's lifecycle, enabling tasks like data fetching, event subscriptions, and cleanup operations.

**Instance Methods:** Class components allow you to define custom instance methods directly within the class. These methods encapsulate component logic and can be reused throughout the component. This helps in organizing and structuring the component's codebase.

**Legacy Support:** Class components have been a core part of React since its early days and are still widely used in many codebases. They provide backward compatibility and support for legacy projects that may not have been updated to use function components with Hooks.

**Robustness:** Class components enforce a more strict structure and separation of concerns, which can lead to more robust and maintainable codebases, especially in larger applications with complex UI logic.

**Performance Optimization:** Class components offer optimization opportunities through the use of `PureComponent` or manual implementation of shouldComponentUpdate (a lifecycle method in React). These optimizations can help prevent unnecessary re-renders and improve performance in certain scenarios.

## How to Handle Complex State and Side Effects (Before Hooks)

Before the introduction of React Hooks, class components were the primary way of handling complex state and side effects in React applications. Here's how class components facilitated this:

**State Management:** Class components provided a built-in mechanism for managing component state using the `this.state` property. Developers could initialize state in the constructor and update it using the `this.setState()` method. This allowed for the management of complex state structures and the synchronization of state with the UI.

**Lifecycle Methods:** Class components offered a range of lifecycle methods that allowed developers to hook into different stages of a component's lifecycle. These lifecycle methods, such as `componentDidMount`, `componentDidUpdate`, and `componentWillUnmount`, provided opportunities to perform tasks like data fetching, DOM manipulation, or cleanup operations.

**Instance Methods:** Class components allowed developers to define custom instance methods directly within the class. These methods encapsulated component logic and allowed for better organization and structure of the component's codebase. Instance methods could handle complex logic, event handling, or interaction with external APIs.

**Higher Order Components (HOCs) and Render Props:** Before the widespread adoption of Hooks, developers often used Higher Order Components (HOCs) or Render Props to encapsulate and share complex logic between components. HOCs and Render Props patterns facilitated the reuse of logic across multiple components, making it easier to manage complex state and side effects.

Overall, class components provided a structured and class-based approach to handling complex state and side effects in React applications. While Hooks have since emerged as a more lightweight and function alternative, class components continue to be used in many codebases, especially in legacy projects or situations where specific lifecycle methods or patterns are required.

## When to Use Each Component Type

Let's discuss when to use function components and class components in React, as well as when error boundaries might necessitate the use of class components:

### When to Choose Function Components

**Simplicity and Readability:** Use function components for simpler UI elements or components that don't require state or lifecycle methods. They have a simpler syntax and are easier to read and understand, making them ideal for presentational components.

**Reusability and Composition:** Function components promote reusability and composability by allowing you to create small, composable functions that can be easily reused across your application. They are well-suited for building reusable UI components.

**Performance:** Function components with React Hooks offer a more optimized approach to state management and side effects, potentially leading to better performance compared to class components. They avoid the overhead of class instantiation and provide a more lightweight alternative.

### When to Choose Class Components (Error Boundaries)

**Lifecycle Methods:** Use class components when you need access to lifecycle methods such as `componentDidCatch`. Class components provide a way to implement error boundaries, which are components that catch JavaScript errors anywhere in their child component tree and display a fallback UI instead of crashing the whole application.

**Handling Complex State and Side Effects (Before Hooks):** In legacy codebases or situations where specific lifecycle methods or optimizations are required, class components might still be the preferred choice. They offer a more structured approach to handling complex state, side effects, and lifecycle behavior.

**Backward Compatibility:** Class components are still widely used in many existing React codebases and libraries. If you're working on a project that relies heavily on class components or if you need to integrate with libraries that haven't migrated to function components with Hooks, you may need to use class components for compatibility reasons.

In summary, function components with Hooks are generally preferred for most use cases due to their simplicity, reusability, and performance benefits. However, class components are still relevant, especially when specific lifecycle methods or error boundaries are necessary. It's essential to weigh the pros and cons of each component type and choose the one that best fits your project's requirements and constraints.

### React Hooks: Bridging the Gap

React Hooks are a feature introduced in React 16.8 that allow function components to have stateful logic and access React lifecycle features without needing to write a class component. Hooks are functions that let you use React state and lifecycle features from within function components.

### Using Hooks for State Management (useState)

The `useState` Hook is one of the most fundamental React Hooks. It allows function components to manage state without needing to define a class. Here's an example of how to use `useState`:

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

In this example, `useState` is used to declare a state variable `count` and a function `setCount` to update it. The initial value of `count` is set to `0`. Whenever `setCount` is called with a new value, React will re-render the component with the updated state.

### Other Useful Hooks (useEffect, useContext, etc.)

React provides several other Hooks for managing side effects, context, and more. Some commonly used ones include:

**`useEffect`:** This Hook allows you to perform side effects in function components. It replaces lifecycle methods like `componentDidMount`, `componentDidUpdate`, and `componentWillUnmount`. You can use it to fetch data, subscribe to external events, or perform cleanup.

**`useContext`:** This Hook allows you to consume context in function components. It allows you to access values from the nearest `Context.Provider` in the component tree.

**`useReducer`:** This Hook is an alternative to `useState` for managing more complex state logic. It's based on the reducer pattern and is useful for managing state transitions in a predictable way.

**`useCallback` and `useMemo`:** These Hooks are used for performance optimization. `useCallback` memoizes functions, preventing unnecessary re-renders, while `useMemo` memoizes values, preventing expensive calculations on every render.

These are just a few examples of the many Hooks available in React. Each Hook serves a specific purpose and allows function components to have the same capabilities as class components, bridging the gap between the two component types and enabling a more function and composable approach to building React applications.

### Conclusion

In summary, React Hooks have made a big impact on how we build components in React. Function components have become really popular because they're simpler and more flexible than class components. 

With Hooks, we can easily manage state, handle side effects, and control how components behave. This has made React development more straightforward and efficient.

Looking forward, function components with Hooks are likely to become the standard way of building React applications. They're easier to use and offer better performance, making them a favorite among developers. 

While class components still have their place, especially in older projects, the trend is moving towards function components with Hooks. They provide a modern and efficient approach to building user interfaces, making React development more enjoyable for everyone involved.

Connect with me on [LinkedIn](https://ng.linkedin.com/in/joan-ayebola).

