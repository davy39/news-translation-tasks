---
title: Caching in React – How to Use the useMemo and useCallback Hooks
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-15T18:39:25.000Z'
originalURL: https://freecodecamp.org/news/caching-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/caching-react.jpg
tags:
- name: caching
  slug: caching
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
seo_title: null
seo_desc: "By Scott Gary\nAs you become more proficient at coding in React, performance\
  \ will become a major focal point in your development process. \nAs with any tool\
  \ or programming methodology, caching plays a huge role when it comes to optimizing\
  \ React applica..."
---

By Scott Gary

As you become more proficient at coding in React, performance will become a major focal point in your development process. 

As with any tool or programming methodology, caching plays a huge role when it comes to optimizing React applications.

Caching in React typically goes by the term _memoization_. It's used to improve performance by reducing the amount of times a component renders due to state or prop mutations.

React provides two APIs for caching: useMemo and useCallback. useCallback is a hook that memoizes a function, while useMemo is a hook that memoizes a value. These two hooks are often used in conjunction with the Context API to further improve efficiency.

Here’s a basic list of topics we’ll be covering in this article:

1. React caching default behavior.
2. The useMemo hook.
3. The useCallback hook.

In order to follow along, you'll need a decent understanding of React and stateful components.

## Default Caching Behavior in React

By default, [React](https://www.ohmycrawl.com/react/) uses a technique called “shallow comparison” to determine whether a component should be re-rendered. This basically means that if the props or state of a component haven’t changed, React will assume that the output of the component hasn’t changed either and won’t re-render it.

While this default caching behavior is very effective by itself, it isn’t always enough to optimize complex components that require advanced state management. 

In order to achieve more control over your component’s caching and rendering behavior, React offers the **useMemo** and **useCallback** hooks.

## Caching in React with the useMemo Hook

useMemo is useful when you need to do an expensive computation to retrieve a value, and you want to ensure that the computation is only performed when necessary. By memoizing the value using useMemo, you can ensure that the value is only computed when its dependencies change.

In a React component, you may have multiple properties that make up your state. If a piece of state changes that has nothing to do with our expensive value, why recompute it if it hasn’t changed?

Here’s an example code block reflecting a basic useMemo implementation:

```
react
import React, { useState, useMemo } from 'react';
function Example() {
const [txt, setTxt] = useState(“Some text”);
const [a, setA] = useState(0);
const [b, setB] = useState(0);
const sum = useMemo(() => {
console.log('Computing sum...');
return a + b;
}, [a, b]);
return (
<div>
<p>Text: {txt}</p>
<p>a: {a}</p>
<p>b: {b}</p>
<p>sum: {sum}</p>
<button onClick={() => setTxt(“New Text!”)}>Set Text</button>
<button onClick={() => setA(a + 1)}>Increment a</button>
<button onClick={() => setB(b + 1)}>Increment b</button>
</div>
);
}
```

In our Example component above, assume the **sum()** function performs an expensive computation. If the **txt** state is updated, React is going to re-render our component, but because we memoized the returned value of sum, this function will not run again at this time.

The only time the **sum()** function will run is if either the **a** or **b** state has been mutated (changed). This is an excellent improvement upon the default behavior, which will rerun this method upon each re-render.

## Caching in React with the useCallback Hook

useCallback is useful when you need to pass a function as a prop to a child component, and you want to ensure that the function reference does not change unnecessarily. By memoizing the function using useCallback, you can ensure that the function reference remains the same as long as its dependencies do not change.

Without getting too heavy into JavaScript function references, let’s just take a look at how they can affect the rendering of your React app. When a function reference changes, any child components that receive the function as a prop will re-render, even if the function logic itself has not changed.

This is because, as we already mentioned, React does a shallow comparison of prop values to determine whether a component should re-render, and a new function reference will always be considered a different value than the previous one.

In other words, the simple act of redeclaring a function (even the same exact function), causes the reference to change, and will cause the child component that receives the function as a prop to unnecessarily re-render.

Here’s an example code block reflecting a basic useCallback implementation:

```
react
import React, { useState, useCallback } from 'react';
function ChildComponent({ onClick }) {
console.log('ChildComponent is rendered');
return (
<button onClick={onClick}>Click me</button>
);
}
function Example() {
const [count, setCount] = useState(0);
const [txt, setTxt] = useState(“Some text…”);
const incrementCount = useCallback(() => {
setCount(prevCount => prevCount + 1);
}, [setCount]);
return (
<div>
<p>Text: {txt}</p>
<p>Count: {count}</p>
<button onClick={setTxt}>Set Text</button>
<button onClick={setCount}>Increment</button>
<ChildComponent onClick={incrementCount} />
</div>
);
}
```

As you can see in the above example, we pass the **incrementCount** method instead of the **setCount** method to the child component. This is because **incrementCount** is memoized, and when we run our **setTxt** method, it won’t cause the child component to unnecessarily re-render.

The only way our child component will re-render in this example is if the **setCount** method runs, because we passed it as a dependency parameter to our **useCallback** memoization.

## Conclusion

Caching is an important technique for optimizing React applications. By reducing unnecessary re-renders, caching can help to improve the performance and efficiency of your application.

React provides a default caching behavior by using a virtual DOM to compare changes in state and props, and only updating components after a shallow comparison reflects changes. This is a great optimization technique that’s sufficient in many scenarios, but sometimes more fine-grained control is desired.

The useMemo and useCallback hooks were created to achieve this fine-grained control. 

useMemo is used to memoize the _results_ of a function call, and is useful when the function is expensive to compute and the result does not change often. 

useCallback is used to memoize the actual reference of a function rather than the returned value, and is used when the function is passed as a prop to child components that might cause unnecessary re-renders.

Want to learn more? To learn more check out the [OhMyCrawl Blog](https://www.ohmycrawl.com/blog/) for more programming tips for SEO.

  

