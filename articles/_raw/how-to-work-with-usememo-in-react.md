---
title: How to Work with useMemo in React – with Code Examples
subtitle: ''
author: Joan Ayebola
co_authors: []
series: null
date: '2024-02-07T18:13:41.000Z'
originalURL: https://freecodecamp.org/news/how-to-work-with-usememo-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/Ivory-and-Blue-Lavender-Aesthetic-Photo-Collage-Presentation--6-.png
tags:
- name: hooks
  slug: hooks
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "useMemo is a valuable tool in the React framework, designed to optimize\
  \ performance by memoizing expensive computations. \nWith useMemo, React can store\
  \ the result of a function call and reuse it when the dependencies of that function\
  \ haven't changed,..."
---

`useMemo` is a valuable tool in the React framework, designed to optimize performance by memoizing expensive computations. 

With `useMemo`, React can store the result of a function call and reuse it when the dependencies of that function haven't changed, rather than recalculating the value on every render. 

`useMemo` stands out as a powerful tool for optimizing performance without sacrificing code readability or maintainability. But it's often overlooked or misunderstood by beginners. 

In this comprehensive guide, we'll discuss what `useMemo` is, how it works, and why it's an essential tool for every React developer.

### Table of Contents

1. [What is useMemo?](#heading-what-is-usememo)
2. [How does useMemo Work?](#heading-how-does-usememo-work)
3. [When to Use useMemo?](#heading-when-to-use-usememo)  
– [Data Formatting](#heading-data-formatting)  
– [Filtering Data](#heading-filtering-data)  
– [Sorting Data](#heading-sorting-data)  
– [Memoizing Callback Functions](#memorizing-callback-functions-)  
– [Expensive Calculations](#heading-expensive-calculations)
4. [Benefits of useMemo](#heading-benefits-of-usememo)
5. [Syntax and Usage of the useMemo Hook](#syntax-and-usage-of-the-usememo-hook-)  
– [Avoiding Unnecessary Recalculations](#heading-avoiding-unnecessary-recalculations)  
– [Optimizing Rendering Performance](#heading-optimizing-rendering-performance)  
– [Efficiently Managing Derived Data](#heading-efficiently-managing-derived-data)  
– [Enhancing User Experience](#heading-enhancing-user-experience)
6. [How does useMemo differ from other hooks like useState and useEffect?](#heading-how-does-usememo-differ-from-other-hooks-like-usestate-and-useeffect)  
– [useState](#heading-usestate)  
– [useEffect](#heading-useeffect)  
– [useMemo](#heading-usememo)
7. [How to Memoize Expensive Computations Using useMemo](#how-to-memorize-expensive-computations-using-usememo)  
– [Identify the Expensive Computation](#heading-identify-the-expensive-computation)  
– [Wrap the Computation with useMemo](#heading-wrap-the-computation-with-usememo)  
– [Specify Dependencies](#heading-specify-dependencies)
8. [How to Optimize Complex Calculations within Render Props or Higher-Order Components](#heading-how-to-optimize-complex-calculations-within-render-props-or-higher-order-components)
9. [How to Use useMemo with Custom Hooks](#heading-how-to-use-usememo-with-custom-hooks)
10. [Tips for Using useMemo Effectively](#heading-tips-for-using-usememo-effectively)  
– [Identify expensive computations](#identify-expensive-computations-)  
– [Choose the right dependencies](#choose-the-right-dependencies-)  
– [Avoid unnecessary memorization](#avoid-unnecessary-memorization-)  
– [Measure performance](#measure-performance-)
11. [Conclusion](#heading-conclusion)

## What is useMemo?

`useMemo` is a handy tool in React that helps make your apps faster. Imagine you have a function that does some heavy lifting, like calculating a complex math problem or formatting data. Normally, React recalculates this function every time your component renders, even if the inputs are the same. That can slow things down.

But with `useMemo`, React remembers the result of that function as long as its inputs stay the same. So, if your inputs don't change, React just grabs the stored result instead of recalculating it every time. This saves time and makes your app snappier. 

In simple terms, `useMemo` is like having a smart assistant who remembers the answers to math problems, so you don't have to solve them again and again.

## How Does useMemo Work?

To understand how `useMemo` works, let's consider a scenario where you have a component that renders a list of items, and you need to perform some heavy computation to derive the list. 

Without memoization, this heavy computation would be executed on every render, even if the inputs remain unchanged.

Here's a basic example without `useMemo`:

```jsx
import React from 'react';

const ListComponent = ({ items }) => {
  const processedItems = processItems(items); // Expensive computation

  return (
    <ul>
      {processedItems.map(item => (
        <li key={item.id}>{item.name}</li>
      ))}
    </ul>
  );
};

const processItems = (items) => {
  // Expensive computation
  // Imagine some heavy processing here
  return items.map(item => ({ id: item.id, name: item.name.toUpperCase() }));
};

export default ListComponent;

```

In this example, `processItems` function gets called on every render, even if the `items` prop remains the same. 

To optimize this, we can use `useMemo`:

```jsx
import React, { useMemo } from 'react';

const ListComponent = ({ items }) => {
  const processedItems = useMemo(() => processItems(items), [items]);

  return (
    <ul>
      {processedItems.map(item => (
        <li key={item.id}>{item.name}</li>
      ))}
    </ul>
  );
};

const processItems = (items) => {
  // Expensive computation
  // Imagine some heavy processing here
  return items.map(item => ({ id: item.id, name: item.name.toUpperCase() }));
};

export default ListComponent;

```

By wrapping the `processItems` call inside `useMemo`, React will only recompute the memoized value when the `items` prop changes. This optimization can significantly improve the performance of your application, especially when dealing with large datasets or complex computations.

## When to Use useMemo

You should use `useMemo` in scenarios where you have expensive computations or data transformations within a functional component that are being unnecessarily recalculated on every render. 

Here are some practical examples illustrating basic usage scenarios for `useMemo`:

### Data Formatting:

```jsx
const formattedData = useMemo(() => formatData(rawData), [rawData]);

```

* Use `useMemo` to format raw data into a display-friendly format.
* Recompute `formattedData` only when `rawData` changes, optimizing performance.

### Filtering Data:

```jsx
const filteredData = useMemo(() => filterData(rawData, filterCriteria), [rawData, filterCriteria]);

```

* Use `useMemo` to filter a list of data based on certain criteria.
* Ensure `filteredData` is recalculated only when `rawData` or `filterCriteria` change.

### Sorting Data:

```jsx
const sortedData = useMemo(() => sortData(rawData, sortKey), [rawData, sortKey]);

```

* Use `useMemo` to sort a list of data based on a specific key.
* Re-sort `sortedData` only when `rawData` or `sortKey` change.

### Memoizing Callback Functions:

```jsx
const handleClick = useMemo(() => {
  return () => {
    // Handle click event
  };
}, []);

```

* Use `useMemo` to memoize callback functions to prevent unnecessary function recreations on every render.
* Pass an empty dependency array (`[]`) to ensure the callback function is only created once during the component's lifecycle.

### Expensive Calculations:

```jsx
const result = useMemo(() => {
  // Perform expensive calculation
  return performCalculation(input1, input2);
}, [input1, input2]);

```

* Use `useMemo` to memoize the result of an expensive calculation.
* Recalculate `result` only when `input1` or `input2` change.

In each of these examples, `useMemo` ensures that the expensive computation or transformation is only performed when necessary, reducing unnecessary recalculations and optimizing the performance of your functional components.

## Benefits of useMemo

Utilizing the `useMemo` hook in React applications offers numerous benefits for performance optimization. 

### Avoiding Unnecessary Recalculations:

In React, components re-render whenever their state or props change. If a component performs expensive computations or calculations within its rendering logic, these computations can be re-executed on every render, even if the inputs haven't changed.

By using `useMemo`, you can memoize these computations. React will only recalculate the memoized value when the dependencies (inputs) change. This helps avoid unnecessary recalculations, improving the performance of your components.

### Optimizing Rendering Performance:

React components can become slow to render if they perform heavy computations or transformations during each render cycle. This is particularly problematic in large-scale applications or components that render frequently.

`useMemo` allows you to memoize the results of these computations, ensuring that they are only performed when necessary. This can lead to significant improvements in rendering performance by reducing the computational overhead of your components.

### Efficiently Managing Derived Data:

In many React applications, derived data is computed from the state or props of components. For example, computed properties, filtered lists, or formatted data are often derived from raw data sources.

Memoizing derived data with `useMemo` ensures that these computations are performed efficiently and only when needed. This can prevent unnecessary re-renders and optimize the overall performance of your application.

### Enhancing User Experience:

Performance optimization is crucial for delivering a smooth and responsive user experience. Slow or unresponsive components can lead to a poor user experience and frustrate users.

By leveraging `useMemo` to optimize the performance of your components, you can ensure that your application remains fast and responsive, improving user satisfaction and engagement.

`useMemo` is essential for performance optimization in React applications because it allows you to avoid unnecessary recalculations, optimize rendering performance, efficiently manage derived data, and enhance the overall user experience. 

By memoizing expensive computations with `useMemo`, you can create fast, responsive, and efficient React components that deliver a seamless user experience.

## Syntax and Usage of the useMemo Hook

The `useMemo` hook in React is used to memoize expensive computations. Its syntax is straightforward, and it takes two arguments: a function representing the computation to be memoized, and an array of dependencies. 

Here's the syntax and usage of the `useMemo` hook:

```jsx
import React, { useMemo } from 'react';

const MyComponent = ({ data }) => {
  // Memoize the result of the expensive computation
  const memoizedValue = useMemo(() => {
    // Perform some expensive computation using the data
    return processData(data);
  }, [data]); // Dependency array: recompute if 'data' changes

  return (
    <div>
      {/* Render the memoized value */}
      <p>{memoizedValue}</p>
    </div>
  );
};

export default MyComponent;

```

In this example:

1. We import `useMemo` from the React library.
2. Inside the functional component `MyComponent`, we declare a constant `memoizedValue` using the `useMemo` hook.
3. The first argument of `useMemo` is a function that performs the expensive computation. In this case, we call `processData` function and pass `data` as a parameter.
4. The second argument of `useMemo` is an array of dependencies. React will only recompute the memoized value if any of these dependencies change. Here, we specify `[data]` as the dependency array, indicating that `memoizedValue` should be recalculated whenever the `data` prop changes.
5. Finally, we render the `memoizedValue` inside the component's JSX.

By using `useMemo`, we ensure that the expensive computation inside the function is only executed when necessary, optimizing the performance of our component.

## How Does useMemo Differ from Other Hooks Like useState and useEffect?

`useMemo` differs from other hooks like `useState` and `useEffect` in its purpose and how it affects component behavior:

### useState:

* `useState` is used for managing state within functional components.
* It allows you to create and update state variables, triggering re-renders when their values change.
* State variables managed by `useState` are typically used for storing data that can change over time, such as form inputs, toggles, or counters.

### useEffect:

* `useEffect` is used for handling side effects within functional components.
* It runs after every render and enables you to perform tasks like data fetching, subscriptions, or DOM manipulation.
* `useEffect` allows you to separate side effects from the main component logic, keeping your components clean and organized.

### useMemo:

* `useMemo` is used for memoizing expensive computations within functional components.
* It caches the result of a function and returns the cached result when the inputs to the function remain unchanged.
* Unlike `useState` and `useEffect`, which manage state and side effects respectively, `useMemo` focuses solely on optimizing performance by avoiding unnecessary recalculations.

While `useState` and `useEffect` are used for managing state and handling side effects, respectively, `useMemo` is specifically designed for performance optimization by memoizing computations. Each hook serves a distinct purpose in React development, but they can be used together to build efficient and maintainable components.

## How to Memoize Expensive Computations using useMemo

To memoize expensive computations using `useMemo`, follow these steps:

### Identify the Expensive Computation: 

Determine which computations in your component are expensive and would benefit from memoization. These could include complex calculations, data transformations, or function calls that consume significant resources.

### Wrap the Computation with useMemo: 

Use the `useMemo` hook to memoize the result of the computation. The first argument to `useMemo` is a function that performs the computation, and the second argument is an array of dependencies.

### Specify Dependencies: 

Provide an array of dependencies to `useMemo` to indicate when the memoized value should be recalculated. If any of the dependencies change, `useMemo` will recompute the memoized value.

Here's an example of how to memoize an expensive computation using `useMemo`:

```jsx
import React, { useMemo } from 'react';

const MyComponent = ({ data }) => {
  // Memoize the result of the expensive computation
  const memoizedValue = useMemo(() => {
    // Perform the expensive computation here
    return processData(data);
  }, [data]); // 'data' is a dependency

  return (
    <div>
      {/* Render the memoized value */}
      <p>{memoizedValue}</p>
    </div>
  );
};

export default MyComponent;

```

In this example:

* We use `useMemo` to memoize the result of the `processData` function, which performs the expensive computation.
* The `data` prop is specified as a dependency in the dependency array `[data]`. This means that `memoizedValue` will be recalculated whenever the `data` prop changes.
* The memoized value (`memoizedValue`) is then rendered inside the component's JSX.

By memoizing the expensive computation with `useMemo`, we ensure that it is only recomputed when necessary, optimizing the performance of our component.

## How to Optimize Complex Calculations within Render Props or Higher-order Components

`useMemo` can also be effectively utilized within render props or higher-order components (HOCs) to optimize complex calculations. Consider the following HOC example:

```jsx
import React, { useMemo } from 'react';

const withDataFetching = (WrappedComponent) => {
  return function WithDataFetching({ data }) {
    // Memoize the processedData calculation
    const processedData = useMemo(() => processData(data), [data]);

    return <WrappedComponent processedData={processedData} />;
  };
};

const DisplayData = ({ processedData }) => {
  return (
    <div>
      {processedData.map(item => (
        <div key={item.id}>{item.name}</div>
      ))}
    </div>
  );
};

const processData = (data) => {
  // Expensive computation
  // Imagine some heavy processing here
  return data.map(item => ({ id: item.id, name: item.name.toUpperCase() }));
};

export default withDataFetching(DisplayData);

```

In this example, `processedData` is memoized within the `withDataFetching` HOC using `useMemo`. This optimization ensures that the heavy computation in `processData` is only performed when the `data` prop changes, improving the overall performance of the component.

## How to Use useMemo with Custom Hooks

Another powerful use case for `useMemo` is within custom hooks to memoize values across components. Let's create a custom hook that fetches data from an API and memoizes the result:

```jsx
import { useState, useEffect, useMemo } from 'react';

const useDataFetching = (url) => {
  const [data, setData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch(url);
      const result = await response.json();
      setData(result);
    };

    fetchData();
  }, [url]);

  // Memoize the data value
  const memoizedData = useMemo(() => data, [data]);

  return memoizedData;
};

export default useDataFetching;

```

Now, whenever we use `useDataFetching` hook in a component, the `data` value will be memoized using `useMemo`. This ensures that the fetched data is only recalculated when the URL changes, preventing unnecessary API calls and improving performance across components.

## Tips for Using useMemo Effectively

Here are some tips for using `useMemo` effectively:

1. Identify expensive computations: Identify the parts of your application that involve heavy computations or calculations.
2. Choose the right dependencies: Ensure that you include all the necessary dependencies in the dependency array. Missing dependencies could lead to unexpected behavior.
3. Avoid unnecessary memoization: Avoid memorizing values that don't need to be memoized, as it can add unnecessary complexity to your code.
4. Measure performance: Use performance monitoring tools to measure the impact of `useMemo` on your application's performance and adjust accordingly.

## Conclusion

`useMemo` is a powerful tool for optimizing the performance of your React applications by memoizing the result of expensive computations. 

By using `useMemo` effectively, you can prevent unnecessary re-renders and improve the overall responsiveness of your application. 

So, don't ignore `useMemo` just because it seems intimidating. Embrace it as a valuable tool in your React development journey, and harness its potential to create faster and more efficient web applications.

