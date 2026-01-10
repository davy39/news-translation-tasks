---
title: Common React Mistakes to Avoid
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2024-08-06T22:19:05.000Z'
originalURL: https://freecodecamp.org/news/react-common-mistakes
coverImage: https://www.freecodecamp.org/news/content/images/2024/08/react-mistakes.png
tags:
- name: React
  slug: react
seo_title: null
seo_desc: 'By Scott Gary

  React is a highly popular and powerful JavaScript library for user interface development.
  Its component-based architecture, combined with its declarative nature, is one of
  the primary reasons it works well for both small and large-scale...'
---

By Scott Gary

React is a highly popular and powerful JavaScript library for user interface development. Its component-based architecture, combined with its declarative nature, is one of the primary reasons it works well for both small and large-scale applications. 

But like with any technology, there are pitfalls that you can fall into when you're writing React code if you're not careful. 

In this article, we will discuss these common mistakes and I'll provide you with best practices to avoid them. This will help you keep your React projects efficient, maintainable, and scalable.

## 1. Mistakes in Key Props Usage

One of the most common mistakes when using React involves the key prop. There are several scenarios where key props are used, with lists being the most common. 

The key prop is crucial because it helps React track which items have changed, been added, or removed. If they are not correctly set, React's diffing algorithm can become inefficient, leading to performance issues and bugs.

**Best Practice:** Always pass a stable and unique key for the items in a list. If possible, use unique IDs from your data instead of array indices as keys.

```
const ItemList = ({ items }) => (
  <ul>
    {items.map(item => (
      <li key={item.id}>{item.name}</li>
    ))}
  </ul>
);

```

In the above code snippet, each item in the list has a key with `item.id`. This ensures that every list item is uniquely identifiable, helping React render more efficiently and reduce unnecessary renders.  
  
For more tips on optimizing performance, check out this article on [caching in React](https://www.freecodecamp.org/news/caching-in-react/).

## 2. Ignoring the Virtual DOM

Some developers mistakenly believe that the role of the Virtual DOM means they need to update the DOM themselves. This goes against how React works and can result in unpredictability and bugs.

### What is the Virtual DOM? 

For those new to React, the Virtual DOM is an in-memory representation of the real DOM. It allows React to update the UI efficiently by minimizing direct manipulations of the actual DOM. React compares the new Virtual DOM with the previous one and updates only the necessary parts of the real DOM. 

Developers might assume they need to synchronize the Virtual DOM with the real DOM due to experiences with other libraries or frameworks.

**Best Practice:** Always let React handle the DOM. If you must interact directly with the DOM, use refs.

```
const ItemList = ({ items }) => (
  <ul>
    {items.map(item => (
      <li key={item.id}>{item.name}</li>
    ))}
  </ul>
);

```

**Explanation:**

Using a unique identifier from the data, such as `item.id`, ensures that each key is unique and stable. This allows React to efficiently determine which items have changed, been added, or removed. It helps React's reconciliation algorithm to update the UI efficiently and prevents bugs related to item reordering or deletion.

## 3. Overusing State

State management is crucial in React, but excessive state usage can make a component complex and difficult to maintain. Any change in state triggers a re-render, which can be expensive if not handled properly.

**Best Practice:** Minimize the use of state and lift state only when necessary. For global state, use contexts or state management libraries like Redux.

```
import React, { useState } from 'react';

const MyComponent = () => {
  const [count, setCount] = useState(0);
  const [name, setName] = useState(''); // Additional state

  const handleIncrement = () => setCount(count + 1);
  const handleNameChange = (e) => setName(e.target.value);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={handleIncrement}>Increment</button>
      <input
        type="text"
        value={name}
        onChange={handleNameChange}
        placeholder="Enter name"
      />
    </div>
  );
};

```

In the above example, the `useState` hook is used to maintain a simple count state. When the button is pressed, it displays and increments the count, demonstrating a very basic use of state.

## 4. Forgetting to Clean Up Effects

When using the useEffect hook, it is essential to clean up side effects to prevent memory leaks and other unintended behaviors. Side effects might include setting up subscriptions, timers, or event listeners that need to be cleared when the component unmounts or when the effect dependencies change.

**Best Practice:** Always return a cleanup function from your effect when setting up side effects that need to be cleared.  
  
Example without Cleanup:

```
const Timer = () => {
  const [time, setTime] = React.useState(0);

  React.useEffect(() => {
    const intervalId = setInterval(() => {
      setTime(prevTime => prevTime + 1);
    }, 1000);
    // No cleanup function provided here
  }, []);

  return <div>Time: {time}s</div>;
};

```

In the example above, a timer is set up with `setInterval`, but no cleanup function is provided to clear the interval when the component unmounts. This can lead to memory leaks.

**Correct**: Cleanup with `useEffect`:

```
const Timer = () => {
  const [time, setTime] = React.useState(0);

  React.useEffect(() => {
    const intervalId = setInterval(() => {
      setTime(prevTime => prevTime + 1);
    }, 1000);

    // Cleanup function to clear the interval
    return () => clearInterval(intervalId);
  }, []);

  return <div>Time: {time}s</div>;
};

```

In this corrected example, a cleanup function is provided to clear the interval when the component unmounts, preventing potential memory leaks.

## 5. Ignoring Performance

A React application can encounter serious performance issues, such as excessive re-renders and heavy calculations during render.

**Best Practice:** Memoize components and values using `React.memo`, `useMemo`, and `useCallback` for improved performance.

```
const MemoizedComponent = React.memo(({ data }) => {
  return <div>{data}</div>;
});

```

This example uses `React.memo` to memoize a functional component, preventing it from re-rendering unnecessarily when the `data` prop hasn't changed.

## 6. Overusing the Context API

The Context API is very handy for passing data through your component tree without prop drilling. But it's often overused, leading to performance issues.

**Best Practice:** Avoid using context for frequently changing values. Mainly use it for static values or rare updates.

```
const ThemeContext = React.createContext('light');

const ThemedComponent = () => {
  const theme = useContext(ThemeContext);
  return <div className={theme}>Themed Component</div>;
};

```

In the above example, `ThemeContext` is initialized with the default value `'light'`. The `ThemedComponent` uses the `useContext` hook to get the actual value of the theme.

## 7. Not Handling Errors Properly

One important feature of React is error boundaries. They catch and handle errors in the component tree. Without them, unhandled errors may eventually crash the entire application.

**Best Practice:** Implement error boundaries using `componentDidCatch` or `ErrorBoundary` components.

```
const UserProfile = ({ userId }) => {
  const [user, setUser] = React.useState(null);
  const [error, setError] = React.useState(null);

  React.useEffect(() => {
    fetch(`/api/users/${userId}`)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => setUser(data))
      .catch(err => setError(err.message));
  }, [userId]);

  if (error) {
    return <div>Error: {error}</div>;
  }

  if (!user) {
    return <div>Loading...</div>;
  }

  return <div>{user.name}</div>;
};

```

By adding error handling, we catch any issues with the API request and display an appropriate error message. 

This approach improves the robustness of the component, providing users with feedback in case of an error and ensuring the application remains functional even when unexpected issues occur.

## 8. Failing to Keep Components Pure

React components should always be pure functions of their props. Impure components depend on external states and side effects, making the system unpredictable.

**Best Practice:** Ensure that your components are pure and that their output depends entirely on their props.

```
const MyComponent = ({ name }) => {
  return <div>{name}</div>;
};

```

This functional component is pure because it only depends on the `name` prop to render its output.

## 9. Not Using React Developer Tools

React Developer Tools is a simple yet essential extension for debugging and optimizing the performance of a React application. Development can become more complicated if you don't use this helpful toolkit.

**Best Practice:** Install and use React Developer Tools regularly to inspect component hierarchies, state, and props.

## 10. Ignoring SEO Best Practices

SEO is an important aspect of any web application, and this holds true for React applications as well. Many developers overlook SEO, leading to poor search engine rankings and reduced visibility.

Here are some of the most common React SEO mistakes:

%[https://www.youtube.com/watch?v=tIQv8oIn3g4]

Wondering how to implement the React SEO Best Practices? Good news, I made a follow up video:

%[https://www.youtube.com/watch?v=xAFzD1ckPXs&themeRefresh=1]

**Best Practices:** If video is not your thing, here are the key points to remember:

* Always [render your content server-side](https://www.freecodecamp.org/news/server-side-rendering-javascript/): Google has publicly stated to avoid Client-Side Rendering (CSR).
* Ensure unique URLs for different pages: Since React is a Single Page Application (SPA), always render different URLs for different pages. For example, if you have 5 landing pages, make sure you render 5 unique URLs.
* Ensure unique metadata for each page: As a bonus tip, use [React Helmet](https://www.freecodecamp.org/news/react-helmet-examples/) to ensure every single page has unique metadata.
* Internally link your website: Surprisingly, many developers completely ignore this. Make sure to add internal links to improve navigation and SEO.

## Conclusion

In conclusion, avoiding these common React mistakes can greatly improve the performance and maintainability of your applications. 

If you're interested in learning more about my work or need help with React or Next.js development, check out [hirenext.dev](https://www.hirenext.dev/). Alternatively you can keep up with my blog [OhMyCrawl](https://www.ohmycrawl.com/).   
  
  

