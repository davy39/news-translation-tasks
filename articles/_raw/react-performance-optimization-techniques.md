---
title: React Optimization Techniques to Help You Write More Performant Code
subtitle: ''
author: Temitope Oyedele
co_authors: []
series: null
date: '2024-02-16T00:57:28.000Z'
originalURL: https://freecodecamp.org/news/react-performance-optimization-techniques
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/pexels-howard-adams-575835--1-.jpg
tags:
- name: optimization
  slug: optimization
- name: performance
  slug: performance
- name: React
  slug: react
seo_title: null
seo_desc: "Performance optimization is a critical aspect of developing web applications.\
  \ Users expect applications to load quickly and respond to their interactions smoothly.\
  \ \nIn the React ecosystem, performance optimization techniques can significantly\
  \ enhance..."
---

Performance optimization is a critical aspect of developing web applications. Users expect applications to load quickly and respond to their interactions smoothly. 

In the React ecosystem, performance optimization techniques can significantly enhance the user experience by reducing load times and improving responsiveness.

In this article, we will discuss eight effective techniques for optimizing the performance of your React application.

## Table of Contents

1. [Why Performance Optimization is Important](#heading-why-performance-optimization-is-important)
2. [List visualization](#heading-list-visualization)
3. [Lazy Loading Images](#heading-lazy-loading-images)
4. [Memoization](#heading-memoization)
5. [Throttling and Debouncing Events](#heading-throttling-and-debouncing-events)
6. [Code Splitting](#heading-code-splitting)
7. [React Fragments](#heading-react-fragments)
8. [Web Workers](#heading-web-workers)
9. [UseTransition Hook](#heading-usetransition-hook)
10. [Conclusion](#heading-conclusion)

## Why Performance Optimization is Important

Optimizing the performance of your React application is crucial for several reasons:

* **Better User Experience:** A slow-loading or laggy application can lead to a poor user experience, negatively impacting your business. Users expect fast and responsive interactions, and performance optimization helps deliver that.
* **Improved SEO:** Search engines like Google consider page load times and overall performance when ranking websites. A well-optimized application will rank higher in search results, making it more visible to potential users.
* **Reduced Bounce Rates:** If your application takes too long to load or respond, users will likely leave and never return. By optimizing performance, you can reduce bounce rates and increase engagement.
* **Cost Savings** A performant application requires fewer resources (like servers and memory) to handle the same workload. This means lower hosting costs and reduced infrastructure needs.
* **Competitive Advantage:** A fast and efficient application sets you apart from competitors whose applications may be slower or less optimized. According to research by [Portent](https://www.portent.com/blog/analytics/research-site-speed-hurting-everyones-revenue.htm), a website that loads within one second has a conversion rate five times higher than a site that takes ten seconds to load. Therefore, ensuring your React applications perform well is crucial for retaining users and maintaining a competitive edge.

## 8 React Performance Optimization Techniques

Below are eight React performance optimization techniques you can use to speed up your applications.

### List visualization

List visualization, or windowing, involves rendering only the items currently visible on the screen. 

When dealing with a large number of items in a list, rendering all the items at once can lead to slow performance and consume a significant amount of memory. List virtualization tackles this issue by rendering only a subset of the list items currently visible within the view, which conserves resources as the users scroll through the list.

The virtualization technique dynamically replaces rendered items with new ones, keeping the visible portion of the list updated and responsive. It efficiently allows you to render large lists or tabular data by only rendering the visible portion, recycling components as needed, and optimizing scroll performance.

There are different approaches to implementing list visualization in React, and one is using a popular library called [React Virtualized](https://www.npmjs.com/package/react-virtualized). 

To install `react-virtualized`, you can use the following command:

```bash
npm install react-virtualized --save
```

After installing `react-virtualized`, you can import the required components and styles. Below is an example of how to use the `List` component to create a virtualized list:

```javascript
import React from 'react';
import { List } from 'react-virtualized';
import 'react-virtualized/styles.css'; // Import styles

// Your list data
const list = Array(5000).fill().map((_, index) => ({
  id: index,
  name: `Item ${index}`
}));

// Function to render each row
function rowRenderer({ index, key, style }) {
  return (
    <div key={key} style={style}>
      {list[index].name}
    </div>
  );
}

// Main component
function MyVirtualizedList() {
  return (
    <List
      width={300}
      height={300}
      rowCount={list.length}
      rowHeight={20}
      rowRenderer={rowRenderer}
    />
  );
}

export default MyVirtualizedList;

```

In this example, `List` is the main component provided by `react-virtualized`. The `rowRenderer` function defines how each row should be rendered. The `width`, `height`, `rowCount`, `rowHeight`, and `rowRenderer` props are essential for configuring the list's behavior and appearance. 

React applications can handle massive amounts of data by leveraging list virtualization without sacrificing performance or user experience.

### Lazy Loading Images

Similar to the list virtualization technique, lazy loading images prevents the creation of unnecessary DOM nodes, thereby boosting performance. Lazy loading allows you to defer or delay the loading of images until they are needed or visible to the user instead of loading all the images on page load.

The concept behind lazy loading is to initiate the load of a placeholder or a small low-resolution version of the image, typically a small-sized thumbnail or a blurred placeholder. As the user scrolls or interacts with the page, the actual image is loaded dynamically, replacing the placeholder when the user enters the viewport or when it becomes visible.

Lazy loading in React can be achieved using various libraries and techniques. One of the popular libraries is the [react-lazyload](https://www.npmjs.com/package/react-lazyload).  

To install `react-lazyload`, you can use the following command:

```bash
npm install --save react-lazyload
```

Below is an example of a simple React component that uses `react-lazyload` to implement lazy loading for images:

```javascript
import React from 'react';
import LazyLoad from 'react-lazyload';

const MyLazyLoadedImage = ({ src, alt }) => {
  return (
    <LazyLoad height={200} offset={100}>
      {/* The height and offset props control when the image should start loading */}
      <img src={src} alt={alt} />
    </LazyLoad>
  );
};

export default MyLazyLoadedImage;

```

In this example, `MyLazyLoadedImage` uses the `LazyLoad` component from `react-lazyload`. The `height` prop specifies the height of the placeholder, and the `offset` prop determines how far below the viewport the placeholder should start loading.

Another approach is to use the [intersection observer API](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API), which is a web API that allows you to detect when an element enters or exists the viewport efficiently. Here's how we can use the Intersection Observer API along with the `useEffect` hook in React:

```javascript
import React, { useEffect, useRef } from 'react';

const IntersectionLazyLoad = ({ src, alt }) => {
  const imageRef = useRef();

  useEffect(() => {
    const options = {
      root: null, // Use the viewport as the root
      rootMargin: '0px', // No margin around the root
      threshold: 0.5, // 50% of the image should be visible
    };

    const observer = new IntersectionObserver(handleIntersection, options);

    if (imageRef.current) {
      observer.observe(imageRef.current);
    }

    return () => {
      // Cleanup the observer when the component is unmounted
      observer.disconnect();
    };
  }, []);

  const handleIntersection = (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        // Load the image when it becomes visible
        imageRef.current.src = src;
        imageRef.current.alt = alt;
      }
    });
  };

  return <img ref={imageRef} style={{ height: '200px' }} alt="Placeholder" />;
};

export default IntersectionLazyLoad;

```

In this example, `IntersectionLazyLoad` uses the Intersection Observer API to determine when the image becomes visible in the viewport. 

By utilizing this API along with React `useEffect` hook, you can implement your custom lazy loading solution for images in React.

### Memoization

Memoization in React is a technique used to optimize the performance of functional components by caching the results of expensive computations or function calls. It's particularly useful when dealing with computationally intensive or frequently called functions with the same input values, as it helps avoid redundant calculations and improves the overall efficiency of the application.

In React, there are three techniques for memoization: `React.memo()`, `useMemo(),` and `useCallback().` Let's delve into the details for each:

#### How to use `React.memo()`

This higher-order component wraps purely functional components to prevent re-rendering if the received props remain unchanged.

By using `React.memo()`, the rendering result is cached based on props. If the props haven't changed since the last render, React reuses the previously rendered result instead of redoing the rendering process. This saves time and resources.

 Below is an example on how to use the `React.memo` with a functional component:

```javascript
import React from 'react';

const Post = ({ signedIn, post }) => {
  console.log('Rendering Post');
  return (
    <div>
      <h2>{post.title}</h2>
      <p>{post.content}</p>
      {signedIn && <button>Edit Post</button>}
    </div>
  );
};

export default React.memo(Post);

```

In the code above, `Post` (functional component) depends on the `signedIn` and `post` props. By wrapping it with `React.memo()`, React will only re-render the `Post` component if either `signedIn` or `post` changes.

You can now use the memoized component like any other component in your application:

```javascript
import React, { useState } from 'react';
import Post from './Post';

const App = () => {
  const [signedIn, setSignedIn] = useState(false);
  const post = { title: 'Hello World', content: 'Welcome to my blog!' };

  return (
    <div>
      <Post signedIn={signedIn} post={post} />
      <button onClick={() => setSignedIn(!signedIn)}>
        Toggle Signed In
      </button>
    </div>
  );
};

export default App;

```

When you click the `Toggle Signed In` button, it will toggle the `signedIn` state. Since `Post` is wrapped with `React.memo()`, it will only re-render when the `signedIn` prop changes, thus saving rendering time and resources

#### How to use `useMemo()`

The `useMemo()` hook optimizes performance by memoizing the result of a function call or an expensive computation. It caches the result and recalculates it only when the input values change. Below is an example on how to use the `useMemo` hook in functional component:

```javascript
import React, { useMemo } from 'react';

function App() {
  const [count, setCount] = React.useState(0);
  const [otherState, setOtherState] = React.useState('');

  const expensiveComputation = (num) => {
    let i =  0;
    while (i <  1000000000) i++;
    return num * num;
  };

  const memoizedValue = useMemo(() => expensiveComputation(count), [count]);

  return (
    <div>
      <p>Count: {count}</p>
      <p>Square: {memoizedValue}</p>
      <button onClick={() => setCount(count +  1)}>Increase Count</button>
      <input type="text" onChange={(e) => setOtherState(e.target.value)} />
    </div>
  );
}

export default App;

```

In the code above, the `expensiveComputation` function simulates a resource-intensive operation, like squaring a number. 

The `useMemo` hook is utilized to cache the result of this computation. The memoized value, stored in `memoizedValue`, is only recalculated when the `count` state changes, as `count` is specified as a dependency in the `useMemo` dependency array. Consequently, clicking the `Increase Count` button increments the `count` state, triggering a recalculation of the memoized value. 

Conversely, changing the `otherState` via the input field does not prompt a recalculation, as `otherState` is not included in the `useMemo` dependency array.

#### How to use `useCallback()`

The `useCallback()` hook in React is used to memoize a function instead of memoizing the function result. It is particularly useful when passing events as props to child components to prevent unnecessary re-renders. 

`useCallback()` memoizes the function, ensuring it remains the same across re-renders as long as the dependencies haven't changed. 

This is especially beneficial when passing functions as props to child components, preventing unnecessary re-renders. It is often used with `React.memo()` to ensure child components do not re-render when unnecessary. Below is an exmple of how to use the `useCallback()` hook:

```javascript
import React, { useState, useCallback } from 'react';

const ParentComponent = () => {
  const [count, setCount] = useState(0);

  // Define a function that increments the count state
  const incrementCount = () => {
    setCount(count + 1);
  };

  // Memoize the incrementCount function using useCallback
  const memoizedIncrement = useCallback(incrementCount, [count]);

  return (
    <div>
      <p>Count: {count}</p>
      <ChildComponent onIncrement={memoizedIncrement} />
    </div>
  );
};

const ChildComponent = React.memo(({ onIncrement }) => {
  console.log('Child component rendered');
  return (
    <div>
      <button onClick={onIncrement}>Increment Count</button>
    </div>
  );
});

export default ParentComponent;

```

In the code above, the `ParentComponent` is responsible for managing a state variable named `count` and introduces a function called `incrementCount`, which handles the incrementation of the count. Utilizing the `useCallback` hook, the `incrementCount` function is memoized, guaranteeing its stability across renders unless any of its dependencies, in this case, `count`, undergo changes.

On the other hand, the `ChildComponent` is a component nested within the parent. It receives the memoized `onIncrement` function from the parent as a prop. 

To optimize performance and prevent unnecessary re-renders when the props remain constant, the `ChildComponent` is wrapped with `React.memo()`. This ensures that the child component will only re-render when its props, specifically the memoized function, experience changes, contributing to a more efficient rendering process.

It's important to note that `useCallback` should be used sparingly and only for performance-critical parts of your application. Overusing `useCallback` can actually lead to worse performance due to the overhead of memoization itself. Always measure the performance impact before and after using `useCallback` to ensure it's having the desired effect.

### Throttling and Debouncing Events

Throttling in React is a technique used to limit the number of times a function or an event handler is invoked. It ensures that the function is called at a specified interval, preventing it from being executed too frequently. 

Throttling allows you to control the rate at which the function is called by setting up a minimum time interval between each function invocation. If the function is called multiple times within that interval, only the first invocation is executed, and subsequent invocations are ignored until the interval elapses

Now, let's illustrate throttling with a code example. First, without throttling:

```javascript
// Without throttling, this function will be called every time the event is triggered
function handleResize() {
  console.log('Window resized');
}

window.addEventListener('resize', handleResize);

```

With throttling, we can limit how often the `handleResize` function is called:

```javascript
// Throttling function
function throttle(func, delay) {
  let lastCall =  0;
  return function(...args) {
    const now = new Date().getTime();
    if (now - lastCall < delay) {
      return;
    }
    lastCall = now;
    func(...args);
  };
}

// Throttled event handler
const throttledHandleResize = throttle(handleResize,  200);

window.addEventListener('resize', throttledHandleResize)

```

In this example, the `throttle` function wraps `handleResize` and ensures it's not called more often than every 200 milliseconds. If the `resize` event fires more frequently than that, the `handleResize` function will only be executed once every 200 milliseconds, reducing the potential for performance issues caused by rapid, repeated function calls

Debouncing, on the other hand, is also used to limit the number of times a function or an event handler is invoked. It ensures that the function is called only after a certain period of inactivity. Debouncing allows you to postpone the function call until the user has finished typing or a specific time has elapsed since the last event.

For example, imagine you have a search input field and want to trigger a search API request only when the user has finished typing for a certain duration, like `300ms`. 

With debouncing, the search function will only be invoked after the user stops typing for `300ms`. If the user continues typing within that interval, the function call will be delayed until the pause occurs. Without debouncing, the function will be called for every keystroke, potentially leading to excessive function calls and unnecessary computation. let's demonstrate with a code example:

```javascript
import React, { useState, useEffect } from 'react';

const SearchComponent = () => {
  const [searchTerm, setSearchTerm] = useState('');

  // Function to simulate a search API request
  const searchAPI = (query) => {
    console.log(`Searching for: ${query}`);
    // In a real application, you would make an API request here
  };

  // Debounce function to delay the searchAPI call
  const debounce = (func, delay) => {
    let timeoutId;
    return function (...args) {
      clearTimeout(timeoutId);
      timeoutId = setTimeout(() => {
        func(...args);
      }, delay);
    };
  };

  // Debounced search function
  const debouncedSearch = debounce(searchAPI, 300);

  // useEffect to watch for changes in searchTerm and trigger debouncedSearch
  useEffect(() => {
    debouncedSearch(searchTerm);
  }, [searchTerm, debouncedSearch]);

  // Event handler for the search input
  const handleSearchChange = (event) => {
    setSearchTerm(event.target.value);
  };

  return (
    <div>
      <label htmlFor="search">Search:</label>
      <input
        type="text"
        id="search"
        value={searchTerm}
        onChange={handleSearchChange}
        placeholder="Type to search..."
      />
    </div>
  );
};

export default SearchComponent;

```

With this setup, the `searchAPI` function will only be invoked after the user stops typing for 300ms, preventing excessive API requests and improving the overall performance of the search functionality.

### Code Splitting

Code splitting in React is a technique used to split a large JavaScript bundle into smaller, manageable chunks. It helps improve performance by loading only the necessary code for a specific part of an application rather than loading the entire bundle upfront. 

When you develop a new React application, all your JavaScript code is typically bundled together into a single file. This file contains all the components, libraries, and other code required for your application to function. But as your application grows, the bundle size can become quite large, resulting in slow initial load times for your users.

Code splitting allows you to divide a single bundle into multiple chunks, which can be loaded selectively based on the current needs of your application. Instead of downloading the entire bundle upfront, only the necessary code is fetched and executed when a user visits a particular page or triggers a specific action.

Below is a basic example of code splitting:

```javascript
// AsyncComponent.js
import React, { lazy, Suspense } from 'react';

const DynamicComponent = lazy(() => import('./DynamicComponent'));

const AsyncComponent = () => (
  <Suspense fallback={<div>Loading...</div>}>
    <DynamicComponent />
  </Suspense>
);

export default AsyncComponent;


// DynamicComponent.js
import React from 'react';

const DynamicComponent = () => (
  <div>
    <p>This is a dynamically loaded component!</p>
  </div>
);

export default DynamicComponent;

```

In this example, `AsyncComponent` is a component that uses `lazy` and `Suspense` to perform code splitting. The `DynamicComponent` is dynamically imported using the import() syntax. 

When `AsyncComponent` is rendered, React will load `DynamicComponent` only when it is needed, reducing the initial bundle size and improving the application's performance. The fallback prop in Suspense specifies what to render while waiting for the dynamic import to resolve, providing a better user experience during the loading process.

### React Fragments

React Fragments are a feature introduced in [React 16.2](https://legacy.reactjs.org/blog/2017/11/28/react-v16.2.0-fragment-support.html) that allows you to group multiple elements together without adding an additional DOM node. This is particularly useful when you need to return multiple elements from a component's render method, but you don't want to introduce unnecessary DOM elements that could affect the layout or styles of your application.

Imagine you are arranging books on a bookshelf. Each book represents a React component, and the bookshelf represents the DOM. 

Normally, if you have multiple books, you might want to group them together under a category label (analogous to a DOM element like a `<div>`). But sometimes you just want to place the books side by side without a label because the label itself doesn't hold any value and only takes up physical space. 

React Fragments are like the option to arrange the books without a label, saving space and making the arrangement cleaner.

Here's an example of how to utilize React fragments:

```javascript
import React from 'react';

function BookShelf() {
  return (
    <>
      <Book title="React for Beginners" />
      <Book title="Mastering Redux" />
      <Book title="JavaScript Essentials" />
    </>
  );
}

function Book({ title }) {
  return <li>{title}</li>;
}

export default BookShelf;

```

In this example, the `BookShelf` component returns a list of `Book` components without wrapping them in a `<div>` or other unnecessary DOM element. Instead, it uses the `<>` shorthand syntax for React Fragments. 

This results in a cleaner DOM structure, which can improve the performance of your React application by reducing the number of elements that the browser has to process and render. Using fragments can also reduce unnecessary markup and contribute to a cleaner and more efficient render tree.

### Web Workers

JavaScript operates as a single-threaded application designed to handle synchronous tasks. 

When a web page is being rendered, JavaScript executes multiple tasks, including manipulating DOM elements, managing UI interactions, handling API response data, and enabling CSS animations, all within a single thread. Despite its efficiency in managing these tasks, executing them in a single thread can sometimes lead to performance bottlenecks.

Web Workers serve as a solution to alleviate the burden on the main thread. They allow the execution of scripts in the background on a separate thread, distinct from the main JavaScript thread. 

This separation enables the handling of computationally intensive tasks, execution of long-running operations, or management of tasks that might otherwise block the main thread. By doing so, Web Workers contribute to maintaining user interface responsiveness and overall application performance.

To use web worker in React, create a new JavaScript file that will contain the code for the worker thread:

```javascript
// worker.js
self.onmessage = function(event) {
  var input = event.data;
  var result = performHeavyComputation(input);
  postMessage(result);
};

function performHeavyComputation(input) {
  // Insert your heavy computation logic here
  return input *   2; // Just a placeholder operation
}

```

In your React component, instantiate the Web Worker and establish a communication channel with it:

```javascript
import React, { useEffect, useRef } from 'react';

function MyComponent() {
  const workerRef = useRef();

  useEffect(() => {
    // Initialize the worker
    workerRef.current = new Worker('path-to-your-worker-file.js');

    // Handle incoming messages from the worker
    workerRef.current.onmessage = (event) => {
      console.log('Message received from worker:', event.data);
    };

    // Cleanup the worker when the component unmounts
    return () => {
      workerRef.current.terminate();
    };
  }, []);

  // Function to send a message to the worker
  const sendMessageToWorker = (message) => {
    workerRef.current.postMessage(message);
  };

  // Rest of your component
  return (
    // ...
  );
}


```

In this example, a Web Worker is initialized in the `useEffect` hook and stored in a ref for future use. Messages from the worker are handled with an `onmessage` event listener, and the worker is terminated when the component is unmounted to clean up resources. The `sendMessageToWorker` function demonstrates how to communicate with the worker using `postMessage`

### UseTransition Hook

The `useTransition` hook in React plays a pivotal role in improving the performance of applications by allowing the marking of state updates as non-blocking transitions. This capability enables React to defer rendering for these updates, preventing UI blocking and enhancing overall responsiveness. 

When utilizing `useTransition,` state updates within the `startTransition` function are treated as low-priority transitions, susceptible to interruption by higher-priority state updates. So if a high-priority update occurs during a transition, React may prioritize finishing the high-priority update, interrupting the ongoing transition.

This non-blocking transition mechanism is valuable in preventing UI blocking during intensive operations such as data fetching or large-scale updates. By deferring the rendering of components associated with transition updates, React ensures that the user interface remains responsive even in scenarios where the UI might otherwise become unresponsive.

This example demonstrates the use of `useTransition` in a React component:

```javascript=
import React, { useState, useTransition } from 'react';

function MyComponent() {
  const [state, setState] = useState(initialState);
  const [isPending, startTransition] = useTransition();

  function handleClick() {
    startTransition(() => {
      setState(newState); // This state update is marked as a transition
    });
  }

  return (
    <>
      {/* Your component JSX */}
      <button onClick={handleClick}>Update State</button>
      {isPending && <div>Loading...</div>}
    </>
  );
}

```

This example showcases how React avoids blocking the UI during transitions triggered by user actions, allowing for interruption if higher-priority state updates are detected. 

Note that `useTransition` is part of the Concurrent Mode API, introduced in React 18 and later versions. As a powerful tool for altering the default behavior of state updates, make sure you use it with care, considering the specific implications of deferring rendering within the context of your application.

## Conclusion

Optimizing the performance of a React application involves a combination of strategies, from the fundamental understanding of React's diffing algorithm to leveraging built-in features and third-party tools. 

By applying these techniques judiciously, you can create applications that are not only visually appealing but also performant, leading to a better overall user experience.

