---
title: What is the Virtual DOM in React?
subtitle: ''
author: Matéu.sh
co_authors: []
series: null
date: '2024-06-05T14:51:11.000Z'
originalURL: https://freecodecamp.org/news/what-is-the-virtual-dom-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2024/06/Virtual-DOM.png
tags:
- name: DOM
  slug: dom
- name: React
  slug: react
- name: virtual dom
  slug: virtual-dom
seo_title: null
seo_desc: As web applications become more complex, managing updates to the user interface
  becomes a challenging task. This is where the Virtual DOM (Document Object Model)
  comes into play – particularly in React, the leading JavaScript library for building
  use...
---

As web applications become more complex, managing updates to the user interface becomes a challenging task. This is where the Virtual DOM (Document Object Model) comes into play – particularly in React, the leading JavaScript library for building user interfaces.

The virtual DOM is a lightweight copy of the real DOM that allows React to manage changes more efficiently by minimizing the direct manipulation required on the real DOM. This process significantly enhances the performance of web apps.

Understanding the virtual DOM is essential for developers who want to get the best out of React. It plays a key role in how React updates the UI, ensuring that changes are applied quickly without unnecessary re-renders.  


In this article, you'll learn:

* What the virtual DOM is and how it works
* How the virtual DOM compares to the real DOM
* Benefits of using the virtual DOM
* How React uses the virtual DOM
* How the virtual DOM compares to the shadow DOM
* Common misconceptions about the virtual DOM

## What Is the Virtual DOM and How Does It Work?

The virtual DOM is an in-memory representation of the real DOM elements. Instead of interacting directly with the real DOM, which can be slow and costly in terms of performance, React creates a virtual representation of the UI components. This virtual representation is a lightweight JavaScript object that mirrors the structure of the real DOM.

Here's a step-by-step process of how the virtual DOM works:

1. **Step 1 – Initial Rendering**: when the app starts, the entire UI is represented as a Virtual DOM. React elements are created and rendered into the virtual structure.
2.  **Step 2 – State and Props Changes**: as the states and props change in the app, React re-renders the affected components in the virtual DOM. These changes do not immediately impact the real DOM.
3. **Step 3 – Comparison Using Diff Algorithm**: React then uses a **diffing algorithm** to compare the current version of the Virtual DOM with the previous version. This process identifies the differences (or "diffs") between the two versions.
4. **Step 4 – Reconciliation Process**: based on the differences identified, React determines the most efficient way to update the real DOM. Only the parts of the real DOM that need to be updated are changed, rather than re-rendering the entire UI. This selective updating is quick and performant.
5. **Step 5 – Update to the Real DOM**: finally, React applies the necessary changes to the real DOM. This might involve adding, removing, or updating elements based on the differences detected in step 3.

For example, let's say we have the following counter functionality in the `App` component:

```jsx
import React, { useState } from 'react';

function App() {
 const [count, setCount] = useState(0);

 return (
   <div>
     <h1>Counter: {count}</h1>
     <button onClick={() => setCount(count + 1)}>Increment</button>
   </div>
 );
}

export default App;
```

The virtual DOM representation will look like this:

```json
{
 "type": "div",
 "props": {},
 "children": [
   {
     "type": "h1",
     "props": {},
     "children": [
       {
         "type": "TEXT_ELEMENT",
         "props": {
           "nodeValue": "Counter: 0"
         }
       }
     ]
   },
   {
     "type": "button",
     "props": {
       "onClick": "setCount(count + 1)"
     },
     "children": [
       {
         "type": "TEXT_ELEMENT",
         "props": {
           "nodeValue": "Increment"
         }
       }
     ]
   }
 ]
}

```

When the `Increase` button is clicked once, only the `h1` element is changed:

```json
{
 "type": "h1",
 "props": {},
 "children": [
   {
     "type": "TEXT_ELEMENT",
     "props": {
       "nodeValue": "Counter: 1"
     }
   }
 ]
}

```

## Comparing the Virtual DOM to the Real DOM

To see the advantages of the virtual DOM, it's important to understand how it differs from the real DOM. The real DOM and the virtual DOM serve similar purposes but operate in distinct ways with significant implications for performance and efficiency.

The real DOM is a built-in standard interface in browsers that represents and interacts with HTML elements, from `Doctype` declaration and the root `html` element to every other element in it.

This real DOM represents the whole HTML document as a tree structure and allows JavaScript to manipulate and change HTML documents. Sometimes when those changes occur, the whole document might re-render.

This is in contrast to the virtual DOM, which uses a **diff algorithm** to compare the current and previous versions of updates to the DOM. It only re-renders the parts of the UI that have changed, instead of the whole thing.

## Benefits of Using the Virtual DOM in Web Development

### Simplified Development

The Virtual DOM lets you write code in a more declarative style. This means that instead of writing detailed instructions on how to update the UI, you can simply describe what the UI should look like, and React takes care of the rest. This is made possible by React's declarative syntax and its component-based architecture.

### Improved Performance

One of the major advantages of using the virtual DOM is the significant performance improvement it offers. Direct manipulation of the real DOM is slow and can lead to performance issues, especially in complex applications.

### Enhanced User Experience

The Virtual DOM contributes to a better UX by ensuring that UI updates are smooth, responsive, and without full-page refreshes. Users are less likely to experience lag or jank, resulting in a more seamless interaction with the app.

### Cross-platform Development

The principles of the Virtual DOM are not limited to web development only. React Native – a version of React for building cross-platform mobile apps – uses a similar approach. This increases productivity and reduces development time because you can reuse code across web and mobile platforms

## Common Misconceptions About the Virtual DOM

There are a few misconceptions about the virtual DOM. Let's look at five of these misconceptions and the realities of each of them.

### The Virtual DOM Is a Browser Feature

**Reality**: the virtual DOM is an abstraction implemented by React, not a browser feature. Browsers have the real DOM, which is the standard way to represent and interact with HTML documents. The virtual DOM exists solely in memory within React and is used to optimize updates to the real DOM.

### The Virtual DOM Replaces the Real DOM

**Reality**: The virtual DOM acts as an intermediary between React and the browser, not a replacement for the real DOM. The real DOM is still what the browser uses to render the UI, but the updates to it are managed through the Virtual DOM.

### React is the Only Library and Framework that Uses the Virtual DOM

**Reality**: React only popularized the concept of the virtual DOM, it is not the only library or framework that uses it. Other frameworks like VueJS and SolidJS also use the virtual DOM to update the UI.

### The Virtual DOM Solves All Performance Problems

**Reality**: The virtual DOM can significantly improve performance, but it is not a magical solution to all problems. Poor coding practices, unnecessary renders, and large component trees can still lead to performance issues.

### The Virtual DOM and Shadow DOM Are the Same

**Reality**: The virtual DOM and shadow DOM are not the same thing. The virtual DOM is a lightweight copy of the Real DOM with which React optimize UI updates. On the other hand, shadow DOM is a browser technology used to encapsulate the styles and structure of web components.

## Real DOM vs Virtual DOM vs Shadow DOM

Now that we've established that the virtual DOM, shadow DOM, and real DOM are not the same, let's look at the differences between the three of them.

|  **Aspect** | **Real DOM**  | **Virtual DOM**   | **Shadow DOM**  
|---|---|---|---|---|
| **Definition**  | Standard browser API for representing and interacting with HTML documents  |  In-memory representation of the Real DOM | A browser technology that encapsulates and scopes DOM and style of web components  
|**Flexibility**| Directly manipulated via JavaScript or DOM APIs | Abstracted and optimized by the framework | Limited to component boundaries
|  **Implementation** |  Provided by the browser | Implemented by frameworks like React and Vue  | Part of the Web Components standard, provided by the browser 
|  **Performance** | Direct manipulation can be slow and cause performance issues  | Already optimized for efficient updates  | Provides encapsulation, reducing style conflicts 
|**Usage**|For rendering and interacting with web documents|For efficient UI updates by frameworks| For creating isolated, reusable web components
|**Updates**| Immediate updates to the UI | Updates are batched and optimized | Updates are scoped to the component, not affecting the global DOM
| **Repaints** | Frequent updates can cause costly repaints | Minimizes repaints by batching updates | Scoped to the component, reducing global repaints
|**Use Cases**| General web development and document manipulation | Efficient UI updates in frameworks like React and Vue | Encapsulation of styles and structure in web components


## Conclusion

As you've read in this article, the Virtual DOM is a key React feature that enhances performance and efficient UI updates. With this, React can batch updates, minimize reflows and repaints, and apply changes efficiently. This makes UI updates fast and smooth, providing a better user experience in the process.

Understanding the Virtual DOM and how it works can help you build performant React applications.

## Learn React and Next JS

Want to discover more cool React features like the virtual DOM? Enroll in my React 18 course on Udemy! I'll guide you through the React world by creating a cool 2048 game with animations from scratch.

[![Next.js crash course on Udemy](https://assets.mateu.sh/assets/fcc-universal)](https://assets.mateu.sh/r/fcc-universal)  


