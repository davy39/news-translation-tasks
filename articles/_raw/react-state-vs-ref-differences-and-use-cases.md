---
title: React State vs Refs – Differences and Use Cases
subtitle: ''
author: Timothy Olanrewaju
co_authors: []
series: null
date: '2024-04-11T13:07:51.000Z'
originalURL: https://freecodecamp.org/news/react-state-vs-ref-differences-and-use-cases
coverImage: https://www.freecodecamp.org/news/content/images/2024/04/STATE-VS-REF.png
tags:
- name: React
  slug: react
- name: 'State Management '
  slug: state-management
seo_title: null
seo_desc: 'In this article, we''ll delve into a thorough comparison of React state
  and refs, exploring their suitability for specific scenarios.

  When faced with the need to store data in your React application, the first question
  that comes to mind is: "Will the...'
---

In this article, we'll delve into a thorough comparison of React `state` and `refs`, exploring their suitability for specific scenarios.

When faced with the need to store data in your React application, the first question that comes to mind is: "Will the data change at some point during the component's lifecycle?" If it won't, a regular `const` variable is well-suited. 

However, if the data will change, then that is where the `useState` and `useRef` hooks comes in.

## Understanding the useState and useRef Hooks

### useState Hook

The `useState` hook is designed to manage a component's state, which represents data that can change over time and is important for the component to render. You can add state to your component by importing the `useState` hook from React.

```react
import { useState } from 'react';
```

The `useState` hook is usually initialized with an initial value and returns an array of a declared state variable and its associated setter function. It looks something like this:

```react
import { useState } from "react";

function App() {
  const [count, setCount] = useState(0); //declared useState hook
  
  return (
    <>
      <h1>State example</h1>
      <div>
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
      </div>
    </>
  );
}
export default App;
```

In the above code,

1. The `useState` is initialized with a value of zero and returns a `count` variable and `setCount` setter function.
2.  The `count` variable is set dynamically by the `setCount` setter function that increments the `count` by 1. 
3. For each click of the button, the `App` component is re-rendered and the updated value is displayed within the button text.

Having a good understanding of React state is important as it is one of the most used concept. You can have a more in-depth read on states here: [State Management in React](https://www.freecodecamp.org/news/react-state-management/).

### useRef Hook

The `useRef` hook  is used to create refs in React components. A ref is an object with a `current` property that holds a value. It basically references a DOM element or an instance of a component. We can read and update the value by accessing the current property.

```react
const ref = useRef(initialValue)

ref.current = initialValue
```

Here, is a full code snippet of ref in action:

```react
import { useRef } from "react";

function App() {
  let ref = useRef(0); 
  
  function handleIncrease() {
    ref.current++;
    alert(`You have clicked it ${ref.current} times`);
  }
  return (
    <>
      <h1>Ref example</h1>
      <div>
        <button onClick={handleIncrease}>Click Me</button>
      </div>
    </>
  );
}

export default App;
```

Let's break it down:

1. We imported `useRef` from React.
2. In our `App` component, we declared a `ref` object with the initial value set to zero.
3. `handleIncrease` is our handler function that increments the `ref.current` value by 1 and then alerts the user of the current value.
4. In our `App` component's JSX, we have a button with an `onClick` prop and the `handleIncrease` handler function passed to it.

Having understood how the two hooks work, we'll go ahead to compare and explore when they would be suitable to use.

## React State vs Ref

### Render Trigger

In React, states always trigger a re-render due to a mechanism known as `reconciliation` – which updates the user interface based on changes made to the state or props. 

Under the hood, React compares the new state to the previous and computes the minimal changes needed to update the user interface that reflects the new state. This process ensures consistency with the changed state or props.

On the flip side, refs do not trigger a re-render when changes are made to it. Refs are not directly linked to the component's rendering cycle. 

Therefore, if you want a consistent user interface that reacts to data changes, it is advisable to use states. Refs are better used for managing mutable values without affecting the user interface.

### Mutability

React state cannot be directly changed once it has been set because the setter function updates of the state variable. By using this approach, React maintains the predictability and stability of the data flow. This also helps in making debugging easier.

Conversely, refs are mutable as you can modify the `ref current` value outside of the rendering process. Values can be changed at any point unlike states – refs do not have an updater function. 

### Read/Write Operations

The `useState` hook setter function allows you to update the state value. For instance:

```react
const [state, setState] = useState(false)
function handleOpposite(){
	setState(!state)
 }
```

In this code, we can see that:

1. The initial value is set to a boolean value of `false`.
2. The `handleOpposite` function is negating the boolean value of the `state`  and the `setState` houses the updated value of `true` .

In this simple operation,

1. An implicit **read** operation has been done as the initial value had to be accessed before the negation.
2.  A **write** operation occurred when the negation (!) was used on the initial value, which changed the value to the opposite.

An explicit **read** operation of state happens when you simply access the state variable directly within a component's JSX. For instance:

```
<button onClick={() => setCount((count) => count + 1)}>
  count is {count}
 </button>
```

The `{count}` is the currently accessed value of the state and would be displayed on the UI accordingly.

On the other hand, accessing or modifying a `ref`'s current value during rendering can interfere with React's reconciliation process, potentially causing inconsistencies between the virtual DOM and the actual DOM. 

In order to ensure predictable behavior and optimal performance in components, it's best to adhere to React's guidelines and avoid either accessing or modifying refs during rendering.

### Persisting Across Renders

Data persistence across renders in React means that data remains consistent and available between different render cycles of a component. When data is persisted, it remains unchanged and accessible after re-rendering. State and Ref both persist data across renders.

Persistence is crucial for maintaining the integrity of the application's state and ensures that components operate as expected. 

### Asynchronous Updates

Updates in React state are asynchronous which means that when there is a request for an update, there is a possibility that the updates will not be executed immediately. React might leave some state changes for later while updating other components in one go!

Ref updates are done synchronously where tasks are performed in a sequential manner. Each task waits for the previous one to finish before starting, ensuring that they are executed in a predictable and deterministic manner.

## Conclusion

In this article, we looked extensively at the hooks — `useState` and `useRef` — that handle dynamic data (data that will change) in React applications. 

We compared both hooks and at this point, you should be know their similarities, differences, when and where they are best suited.

Connect with me on [LinkedIn](https://www.linkedin.com/in/timothy-olanrewaju750/) for front-end related discussions and posts. See you on the next one!

