---
title: 'React for Beginners: Complete React Cheatsheet for 2021'
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-05-14T20:17:37.000Z'
originalURL: https://freecodecamp.org/news/react-for-beginners-cheatsheet
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/react-for-beginners-2021.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: cheatsheet
  slug: cheatsheet
- name: hooks
  slug: hooks
- name: React
  slug: react
seo_title: null
seo_desc: 'Welcome to the React for Beginners guide. It''s designed to teach you all
  the core React concepts that you need to know to start building React applications
  in 2021.

  I created this resource to give you the most complete and beginner-friendly path
  to l...'
---

Welcome to the React for Beginners guide. It's designed to teach you all the core React concepts that you need to know to start building React applications in 2021.

I created this resource to give you the most complete and beginner-friendly path to learn React from the ground up.

By the end you will have a thorough understanding of tons of essential React concepts, including:

* The Why, What, and How of React
* How to Easily Create React Apps
* JSX and Basic Syntax
* JSX Elements
* Components and Props
* Events in React
* State and State Management
* The Basics of React Hooks

### Want Your Own Copy?‬ 📄

**[Download the cheatsheet in PDF format here](https://reedbarger.com/resources/react-beginners-2021)** (it takes 5 seconds).

Here are some quick wins from grabbing the downloadable version:

* Quick reference guide to review however and whenever
* Tons of copyable code snippets for easy reuse
* Read this massive guide wherever suits you best. On the train, at your desk, standing in line... anywhere.

There's a ton of great stuff to cover, so let's get started.

## React Basics

### What is React, really?

React is officially defined as a "JavaScript library for creating user interfaces," but what does that really mean?

React is a library, made in JavaScript and which we code in JavaScript, to build great applications that run on the web.

### What do I need to know to learn React?

In other words, you do need to have a basic understanding of JavaScript to become a solid React programmer?

The most basic JavaScript concepts you should be familiar with are variables, basic data types, conditionals, array methods, functions, and ES modules.

How do I learn all of these JavaScript skills? [Check out the comprehensive guide](https://reactbootcamp.com/javascript-skills-for-react-2021/) to learn all of the JavaScript you need for React.

### If React was made in JavaScript, why don't we just use JavaScript?

React was written in JavaScript, which was built from the ground up for the express purpose of building web applications and gives us tools to do so.

JavaScript is a 20+ year old language which was created for adding small bits of behavior to the browser through scripts and was not designed for creating complete applications.

In other words, while JavaScript was used to create React, they were created for very different purposes.

### Can I use JavaScript in React applications?

Yes! You can include any valid JavaScript code within your React applications.

You can use any browser or window API, such as geolocation or the fetch API.

Also, since React (when it is compiled) runs in the browser, you can perform common JavaScript actions like DOM querying and manipulation.

## How to Create React Apps

### Three different ways to create a React application

1. Putting React in an HTML file with external scripts 
2. Using an in-browser React environment like CodeSandbox
3. Creating a React app on your computer using a tool like Create React App

### What is the best way to create a React app?

Which is the best approach for you? The best way to create your application depends on what you want to do with it.

If you want to create a complete web application that you want to ultimately push to the web, it is best to create that React application on your computer using a tool like Create React App.

If you are interested in creating React apps on your computer, [check out the complete guide to using Create React App](https://reactbootcamp.com/create-react-app-10-steps/).

The easiest and most beginner-friendly way to create and build React apps for learning and prototyping is to use a tool like CodeSandbox. You can create a new React app in seconds by going to [react.new](https://react.new)!

## JSX Elements

### JSX is a powerful tool for structuring applications

**JSX** is meant to make creating user interfaces with JavaScript applications easier.

It borrows its syntax from the most widely used programming language: HTML. As a result, JSX is a powerful tool to structure our applications.

The code example below is the most basic example of a React element which displays the text "Hello World":

```js
<div>Hello React!</div>
```

Note that to be displayed in the browser, React elements need to be **rendered** (using `ReactDOM.render()`).

### How JSX is different from HTML

We can write valid HTML elements in JSX, but what differs slightly is the way some attributes are written.

Attributes that consist of multiple words are written in the camel-case syntax (like `className`) and have different names than standard HTML (`class`).

```js
<div id="header">
  <h1 className="title">Hello React!</h1>
</div>
```

JSX has this different way of writing attributes because it is actually made using JavaScript functions (more on this later).

### JSX must have a trailing slash if it is made of one tag

Unlike standard HTML, elements like `input`, `img`, or `br` must close with a trailing forward slash for it to be valid JSX.

```js
<input type="email" /> // <input type="email"> is a syntax error
```

### JSX elements with two tags must have a closing tag

Elements that should have two tags, such as `div`, `main` or `button`, must have their closing, second tag in JSX, otherwise it will result in a syntax error.

```js
<button>Click me</button> // <button> or </button> is a syntax error
```

### How JSX elements are styled

Inline styles are written differently as well as compared to plain HTML.

* Inline styles must not be included as a string, but within an object.
* Once again, the style properties that we use must be written in the camel-case style.

```js
<h1 style={{ color: "blue", fontSize: 22, padding: "0.5em 1em" }}>
  Hello React!
</h1>;
```

Style properties that accept pixel values (like width, height, padding, margin, etc), can use integers instead of strings. For example, `fontSize: 22` instead of `fontSize: "22px"`.

### JSX can be conditionally displayed

New React developers may be wondering how it is beneficial that React can use JavaScript code.

One simple example if that to conditionally hide or display JSX content, we can use any valid JavaScript conditional, like an if statement or switch statement.

```js
const isAuthUser = true;

if (isAuthUser) {
  return <div>Hello user!</div>   
} else {
  return <button>Login</button>
}
```

Where are we returning this code? Within a React component, which we will cover in a later section.

### JSX cannot be understood by the browser

As mentioned above, JSX is not HTML, but is composed of JavaScript functions.

In fact, writing `<div>Hello React</div>` in JSX is just a more convenient and understandable way of writing code like the following:

```js
React.createElement("div", null, "Hello React!")
```

Both pieces of code will have the same output of "Hello React".

To write JSX and have the browser understand this different syntax, we must use a **transpiler** to convert JSX to these function calls.

The most common transpiler is called **Babel.**

## React Components

### What are React components?

Instead of just rendering one or another set of JSX elements, we can include them within React **components**.

Components are created using what looks like a normal JavaScript function, but it's different in that it returns JSX elements.

```js
function Greeting() {
  return <div>Hello React!</div>;   
}
```

### Why use React components?

React components allow us to create more complex logic and structures within our React application than we would with JSX elements alone.

Think of React components as our custom React elements that have their own functionality.

As we know, functions allow us to create our own functionality and reuse it where we like across our application.

Components are reusable wherever we like across our app and as many times as we like.

### Components are not normal JavaScript functions

How would we render or display the returned JSX from the component above?

```js
import React from 'react';
import ReactDOM from 'react-dom';

function Greeting() {
  return <div>Hello React!</div>;   
}

ReactDOM.render(<Greeting />, document.getElementById("root));
```

We use the `React` import to parse the JSX and `ReactDOM` to render our component to a **root element** with the id of "root."

### What can React components return?

Components can return valid JSX elements, as well as strings, numbers, booleans, the value `null`, as well as arrays and fragments.

Why would we want to return `null`? It is common to return `null` if we want a component to display nothing.

```js
function Greeting() {
  if (isAuthUser) {
    return "Hello again!";   
  } else {
    return null;
  }
}
```

Another rule is that JSX elements must be wrapped in one parent element. Multiple sibling elements cannot be returned.

If you need to return multiple elements, but don't need to add another element to the DOM (usually for a conditional), you can use a special React component called a fragment.

Fragments can be written as `<></>` or when you import React into your file, with `<React.Fragment></React.Fragment>`.

```js
function Greeting() {
  const isAuthUser = true;  
    
  if (isAuthUser) {
    return (
      <>
        <h1>Hello again!</h1>
        <button>Logout</button>
      </>
    );
  } else {
    return null;
  }
}
```

Note that when attempting to return a number of JSX elements that are spread over multiple lines, we can return it all using a set of parentheses () as you see in the example above.

### Components can return other components

The most important thing components can return is other components.

Below is a basic example of a React application contained with in a component called `App` that returns multiple components:

```js
import React from 'react';
import ReactDOM from 'react-dom';

import Layout from './components/Layout';
import Navbar from './components/Navbar';
import Aside from './components/Aside';
import Main from './components/Main';
import Footer from './components/Footer';

function App() {
  return (
    <Layout>
      <Navbar />
      <Main />
      <Aside />
      <Footer />
    </Layout>
  );
}

ReactDOM.render(<App />, document.getElementById('root'));
```

This is powerful because we are using the customization of components to describe what they are (that is, the Layout) and their function in our application. This tells us how they should be used just by looking at their name.

Additionally, we are using the power of JSX to compose these components. In other words, to use the HTML-like syntax of JSX to structure them in an immediately understandable way (like the Navbar is at the top of the app, the Footer at the bottom, and so on).

### JavaScript can be used in JSX using curly braces

Just as we can use JavaScript variables within our components, we can use them directly within our JSX as well.

There are a few core rules to using dynamic values within JSX, though:

* JSX can accept any primitive values (strings, booleans, numbers), but it will not accept plain objects.
* JSX can also include expressions that resolve to these values.

For example, conditionals can be included within JSX using the ternary operator, since it resolves to a value.

```js
function Greeting() {
  const isAuthUser = true;  
    
  return <div>{isAuthUser ? "Hello!" : null}</div>;
}
```

## Props in React

### Components can be passed values using props

Data passed to components in JavaScript are called **props**.

Props look identical to attributes on plain JSX/HTML elements, but you can access their values within the component itself.

Props are available in parameters of the component to which they are passed. Props are always included as properties of an object.

```js
ReactDOM.render(
  <Greeting username="John!" />,
  document.getElementById("root")
);

function Greeting(props) {
  return <h1>Hello {props.username}</h1>;
}

```

### Props cannot be directly changed

Props must never be directly changed within the child component.

Another way to say this is that props should never be **mutated**, since props are a plain JavaScript object

```js
// We cannot modify the props object:
function Header(props) {
  props.username = "Doug";

  return <h1>Hello {props.username}</h1>;
}
```

Components are considered pure functions. That is, for every input, we should be able to expect the same output. This means we cannot mutate the props object, only read from it.

### Special props: the children prop

The **children** prop is useful if we want to pass elements / components as props to other components

The children prop is especially useful for when you want the same component (such as a Layout component) to wrap all other components.

```js
function Layout(props) {
  return <div className="container">{props.children}</div>;
}

function IndexPage() {
  return (
    <Layout>
      <Header />
      <Hero />
      <Footer />
    </Layout>
  );
}

function AboutPage() {
  return (
    <Layout>
      <About />
      <Footer />
    </Layout>
  );
}
```

The benefit of this pattern is that all styles applied to the Layout component will be shared with its child components.

## Lists and Keys in React

### How to iterate over arrays in JSX using map

How do we displays lists in JSX using array data? We use the **`.map()`** function to convert lists of data (arrays) into lists of elements.

```js
const people = ["John", "Bob", "Fred"];
const peopleList = people.map((person) => <p>{person}</p>);

```

You can use `.map()` for components as well as plain JSX elements.

```js
function App() {
  const people = ["John", "Bob", "Fred"];

  return (
    <ul>
      {people.map((person) => (
        <Person name={person} />
      ))}
    </ul>
  );
}

function Person({ name }) {
  // we access the 'name' prop directly using object destructuring
  return <p>This person's name is: {name}</p>;
}
```

### The importance of keys in lists

Each React element within a list of elements needs a special **key prop**.

Keys are essential for React to be able to keep track of each element that is being iterated over with the `.map()` function.

React uses keys to performantly update individual elements when their data changes (instead of re-rendering the entire list).

Keys need to have unique values to be able to identify each of them according to their key value.

```js
function App() {
  const people = [
    { id: "Ksy7py", name: "John" },
    { id: "6eAdl9", name: "Bob" },
    { id: "6eAdl9", name: "Fred" },
  ];

  return (
    <ul>
      {people.map((person) => (
        <Person key={person.id} name={person.name} />
      ))}
    </ul>
  );
}
```

## State and Managing Data in React

### What is state in React?

**State** is a concept that refers to how data in our application changes over time. 

The significance of state in React is that it is a way to talk about our data separately from the user interface (what the user sees).

We talk about state management, because we need an effective way to keep track of and update data across our components as our user interacts with it.

To change our application from static HTML elements to a dynamic one that the user can interact with, we need state.

### Examples of how to use state in React

We need to manage state often when our user wants to interact with our application. 

When a user types into a form, we keep track of the form state in that component.

When we fetch data from an API to display to the user (such as posts in a blog), we need to save that data in state.

When we want to change data that a component is receiving from props, we use state to change it instead of mutating the props object.

### Introduction to React hooks with useState

The way to "create" state is React within a particular component is with the `useState` hook.

What is a hook? It is very much like a JavaScript function, but can only be used in a React function component at the top of the component.

We use hooks to "hook into" certain features, and `useState` gives us the ability to create and manage state.

`useState` is an example of a core React hook that comes directly from the React library: `React.useState`.

```js
import React from 'react';

function Greeting() {
  const state = React.useState("Hello React");  
    
  return <div>{state[0]}</div> // displays "Hello React"
}
```

How does `useState` work? Like a normal function, we can pass it a starting value (like "Hello React").

What is returned from useState is an array. To get access to the state variable and its value, we can use the first value in that array: `state[0]`.

There is a way to improve how we write this, however. We can use array destructuring to get direct access to this state variable and call it what we like, such as `title`.

```js
import React from 'react';

function Greeting() {
  const [title] = React.useState("Hello React");  
    
  return <div>{title}</div> // displays "Hello React"
}
```

What if we want to allow our user to update the greeting they see? If we include a form, a user can type in a new value. However, we need a way to update the initial value of our title.

```js
import React from "react";

function Greeting() {
  const [title] = React.useState("Hello React");

  return (
    <div>
      <h1>{title}</h1>
      <input placeholder="Update title" />
    </div>
  );
}

```

We can do so with the help of the second element in the array that useState returns. It is a setter function, to which we can pass whatever value we want the new state to be.

In our case, we want to get the value that is typed into the input when a user is in the process of typing. We can get it with the help of React events.

### What are events in React?

Events are ways to get data about a certain action that a user has performed in our app.

The most common props used to handle events are `onClick` (for click events), `onChange` (when a user types into an input), and `onSubmit` (when a form is submitted).

Event data is given to us by connecting a function to each of these props listed (there are many more to choose from than these three).

To get data about the event when our input is changed, we can add `onChange` on input and connect it to a function that will handle the event. This function will be called `handleInputChange`:

```js
import React from "react";

function Greeting() {
  const [title] = React.useState("Hello React");

  function handleInputChange(event) {
    console.log("input changed!", event);
  }

  return (
    <div>
      <h1>{title}</h1>
      <input placeholder="Update title" onChange={handleInputChange} />
    </div>
  );
}
```

Note that in the code above, a new event will be logged to the browser's console whenever the user types into the input

Event data is provided to us as an object with many properties which are dependent upon the type of event.

### How to update state in React with useState

To update state with useState, we can use the second element that useState returns to us in its array.

This element is a function that will allow us to update the value of the state variable (the first element). Whatever we pass to this setter function when we call it will be put in state.

```js
import React from "react";

function Greeting() {
  const [title, setTitle] = React.useState("Hello React");

  function handleInputChange(event) {
    setTitle(event.target.value);
  }

  return (
    <div>
      <h1>{title}</h1>
      <input placeholder="Update title" onChange={handleInputChange} />
    </div>
  );
}
```

Using the code above, whatever the user types into the input (the text comes from `event.target.value`) will be put in state using `setTitle` and displayed within the `h1` element.

What is special about state and why it must be managed with a dedicated hook like useState is because a state update (such as when we call `setTitle`) causes a re-render.

A re-render is when a certain component renders or is displayed again based off the new data. If our components weren't re-rendered when data changed, we would never see the app's appearance change at all!

## **What's Next**

I hope you got a lot of out this guide.

If you want a copy of this cheatsheet to keep for learning purposes, you can [download a complete PDF version of this cheatsheet here](https://reedbarger.com/resources/react-beginners-2021).

Once you have finished with this guide, there are many things you can learn to advance your skills to the next level, including:

* [How to write custom React hooks](https://reactbootcamp.com/how-to-code-react-hooks/)
* [The complete guide to React props](https://reactbootcamp.com/react-props-cheatsheet/)
* [How to fetch data in React from front to back](https://reactbootcamp.com/fetch-data-in-react/)
* [How to build fullstack apps in React with Node](https://reactbootcamp.com/react-app-node-backend/)
* [Learn more about React state](https://reactbootcamp.com/what-to-know-about-react-state/)
* [How to add routing to your React app with React Router](https://reactbootcamp.com/react-router-cheatsheet/)
* [Learn every part of React with the advanced React cheatsheet](https://reactbootcamp.com/react-cheatsheet-2021/)

## Become a Professional React Developer

React is hard. You shouldn't have to figure it out yourself.

I've put everything I know about React into a single course, to help you reach your goals in record time:

[**Introducing: The React Bootcamp**](https://www.thereactbootcamp.com)

**It’s the one course I wish I had when I started learning React.**

Click below to try the React Bootcamp for yourself:

[![Click to join the React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Click to get started*

