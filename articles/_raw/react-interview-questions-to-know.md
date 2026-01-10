---
title: 10 React Interview Questions You Should Know in 2022
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2022-02-22T00:21:59.000Z'
originalURL: https://freecodecamp.org/news/react-interview-questions-to-know
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/react-interview-questions-1.png
tags:
- name: interview questions
  slug: interview-questions
- name: JavaScript
  slug: javascript
- name: Job Interview
  slug: job-interview
- name: React
  slug: react
seo_title: null
seo_desc: 'Feel confident about your React knowledge? Put it to the test!

  I have selected all of the major questions you should know as a React developer
  in 2022, whether you are interviewing for a hired position or not.

  These questions cover everything from th...'
---

Feel confident about your React knowledge? Put it to the test!

I have selected all of the major questions you should know as a React developer in 2022, whether you are interviewing for a hired position or not.

These questions cover everything from the core concepts of React to a practical understanding of when you should use certain features.

To get the best results out of this guide, make sure to try to answer each question yourself before looking at the answers.

Let's get started!

## 1. What is React? Why Use It?

React is a JavaScript **library**, not a framework.

We use React because it gives us all the power of JavaScript, but with built-in features that improve the way we build and think about building applications.

* It gives us a way to **easily create user interfaces** with tools like JSX
* It gives us components to easily **share parts of our user interface (UI)**, which static HTML itself cannot do
* It allows us to **create reusable behavior** across any of our components with React hooks
* React **takes care of updating our UI** when our data changes, without the need to update the DOM manually ourselves

**Extra Credit**: There are frameworks in React that give you everything you need to build an app (with little to no third-party libraries), like Next.js and Gatsby. 

React was created for building single-page apps in particular, but you can make everything from static sites to mobile apps with the same React concepts.

## 2. What is JSX?

JSX is a way of building React user interfaces that uses the simple syntax of HTML, but adds the functionality and dynamic nature of JavaScript.

In short, it is **HTML + JavaScript for structuring our React apps**.

Though JSX looks like HTML, under the hood it is actually **JavaScript function calls**.

If you write a `div` in JSX, it's actually the equivalent of calling `React.createElement()`.

We can build our user interfaces by manually calling `React.createElement`, but as we add more elements, it becomes harder and harder to read the structure we have built.

**The browser cannot understand JSX itself,** so we often use a JavaScript compiler called **Babel** to convert what looks like HTML into JavaScript function calls that the browser can understand.

## 3. How do you pass data to React components?

There are 2 main ways of passing data to React components:

1. Props
2. Context API

Props are data passed from a component's immediate parent. Props are declared on the child component, can be named anything, and can accept any valid value.

```js
function Blog() {
  const post = { title: "My Blog Post!" };

  return <BlogPost post={post} />;
}
```

Props are consumed within the child component. Props are always available within the child as **properties on an object**.

```js
function BlogPost(props) {
  return <h1>{props.post.title}</h1>
}
```

Since props are plain object properties, they can be destructured for more immediate access.

```js
function BlogPost({ post }) {
  return <h1>{post.title}</h1>
}
```

Context is data passed from a context provider to any component that consumes the context.

Context allows us to access data anywhere in our app (if the provider is passed around the entire component tree), without using props.

Context data is passed down on the `value` prop using the `Context.Provider` component. It can be consumed using the Context.Consumer component or the `useContext` hook.

```js
import { createContext, useContext } from 'react';

const PostContext = createContext()

function App() {
  const post = { title: "My Blog Post!" };

  return (
    <PostContext.Provider value={post}>
      <Blog />
    </PostContext.Provider>
  );
}

function Blog() {
  return <BlogPost />
}

function BlogPost() {
  const post = useContext(PostContext)

  return <h1>{post.title}</h1>
}
```

## 4. What is the difference between state and props?

States are **values we can read and update** in our React components.

Props are **values that are passed to React components and are read only** (they should not be updated).

You can think of props as being similar to arguments for a function that exist outside of our components, while state are values that change over time, but exist and are declared inside our components.

State and props are similar in that changes to them cause the components in which they exist to re-render.

## 5. What are React Fragments used for?

React fragments are a special feature in React that let you write group children elements or components without creating an actual node in the DOM.

The fragment syntax looks like an empty set of tags `<></>` or are tags labeled `React.Fragment`.

In simpler terms, sometimes we need to put multiple React elements under a single parent, but we don't want to use a generic HTML element like a `div`.

If you are writing a table, for example, this would be invalid HTML:

```js
function Table() {
  return (
    <table>
      <tr>
        <Columns />
      </tr>
    </table>
  );
}

function Columns() {
  return (
    <div>
      <td>Column 1</td>
      <td>Column 2</td>
    </div>
  );
}

```

We could avoid this problem by using a fragment instead of a `div` element in our `Columns` component.

```js
function Columns() {
  return (
    <>
      <td>Column 1</td>
      <td>Column 2</td>
    </>
  );
}
```

Another reason for choosing a fragment is that sometimes adding an additional HTML element may change the way our CSS styles are applied.

## 6. Why do we need keys for React lists?

Keys are a unique value that we must pass to the `key` prop when we are using the `.map()` function to loop over an element or a component. 

If we are mapping over an element, it would look like this:

```javascript
posts.map(post => <li key={post.id}>{post.title}</li>)
```

Or like this if we are mapping over a component:

```javascript
posts.map(post => <li key={post.id}>{post.title}</li>)
```

And in both case, we need to add a key that is a unique value, otherwise React will warn us.

Why? Because **keys tell React which element or component is which in a list**. 

Otherwise, if we were to try to change items in this list by inserting more or editing them in some way, React wouldn’t know the order to put them in.

This is because React takes care of all of the business of updating the DOM for us (using a virtual DOM), but **keys are necessary for React to update it properly**.

## 7. What is a ref? How do you use it?

A ref is a **reference to a DOM element** in React.

Refs are created with the help of the `useRef` hook and can be immediately placed in a variable.

This variable is then passed to a given React element (not a component) to get a reference to the underlying DOM element (that is, div, span, and so on).

The element itself and its properties are now available on the **.current property** of the ref.

```js
import { useRef } from 'react'

function MyComponent() {
  const ref = useRef();

  useEffect(() => {
    console.log(ref.current) // reference to div element
  }, [])

  return <div ref={ref} />
}
```

Refs are often referred to as an "escape hatch" to be able to work with a DOM element directly. They allow us to do certain operations that can't be done through React otherwise, such as clearing or focusing an input.

## 8. What is the useEffect hook used for?

The `useEffect` hook is used for performing side effects in our React components.

**Side effects** are operations that are performed with the "outside world" or something that exists outside the context of our React app.

Some examples of side effects include making a GET or POST request to an external API endpoint or working with a browser API like `window.navigator` or `document.getElementById()`.

We cannot perform operations like these directly within the body of our React component. `useEffect` gives us a function within which to perform side effects and a dependencies array which lists any external values that the function relies upon.

If any value within the dependencies array changes, the effect function runs again.

## 9. When do you use React Context vs Redux?

> Redux is probably the most commonly used third-party global state library for React, but you can replace the word "Redux" with any global state library for React.

React context is a way to provide and consume data throughout our application **without using props**.

React context helps us prevent the problem of "**props drilling**", which is when you are passing data with props through components that don't need it.

Instead, with context we can **consume the data exactly in the component that needs it**.

While we only use Context to get or "read" values globally in our application, Redux and other third-party state libraries **allow us to both read and update state**.

Context is not a replacement for a third-party state library like Redux because **it is not built for state updates**. This is because any time the value provided on Context changes, all of its children will re-render, which can hurt performance.

## 10. What are the useCallback & useMemo hooks used for?

The `useCallback` and `useMemo` hooks exist to improve our components' performance.

`useCallback` is to prevent functions that are declared within the body of function components from being recreated on every render.

This can lead to unnecessary performance issues, especially for callback functions that are passed down to child components.

`useMemo`, on the other hand, memoizes an expensive operation that we give it.

**Memoization** is a technical term for functions that are able to "remember" past values they have computed if their arguments have not changed. If so, the function returns the "remembered" value.

In other words, we may have a calculation that takes a significant amount of computing resources and we want it to be performed as sparingly as possible.

If that case, we use the `useMemo` hook, which differs from the `useCallback` hook in that it returns a value, not a function. 

## Become a Professional React Developer

React is hard. You shouldn't have to figure it out yourself.

I've put everything I know about React into a single course, to help you reach your goals in record time:

[**Introducing: The React Bootcamp**](https://www.thereactbootcamp.com)

**It’s the one course I wish I had when I started learning React.**

Click below to try the React Bootcamp for yourself:

[![Click to join the React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Click to get started*

