---
title: Learn React Props – The Animated Guide
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2023-12-17T21:38:23.000Z'
originalURL: https://freecodecamp.org/news/react-props-animated-guide
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/react-props-animated.png
tags:
- name: React
  slug: react
seo_title: null
seo_desc: 'Props are a common stumbling block when moving from JavaScript to React.

  In reality, using props in React components is almost identical to using arguments
  in plain JavaScript functions.

  Let''s take a quick look at what props are in React through some...'
---

Props are a common stumbling block when moving from JavaScript to React.

In reality, using props in React components is almost identical to using arguments in plain JavaScript functions.

Let's take a quick look at what props are in React through some helpful animations. These will help you visualize how props function and how you can use them in your React projects.

## How to Pass Data to a JavaScript Function

The following JavaScript function is broken. What will happen if you try to use it?

```js
function sum() {
  return a + b;
} 

sum(); // Reference Error: a is not defined
```

![1](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/quaqsusb34cn96j9etvh.gif)
_When sum function is called, it throws a Reference Error: a is not defined_

If you call this function, you’re going to get a Reference Error which says, "a is not defined".

This makes sense – the `sum` function is using two values, `a` and `b`, but has no idea what they are.

To fix it, we need to add `a` and `b` as parameters and pass two numbers as arguments.

```js
function sum(a, b) {
  return a + b;   
}

sum(2, 2); // 4
```

![2](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/6ad157f12fb7vqs2ndg5.gif)
_Fix the sum function by passing values to both arguments a and b_

That’s how you pass data to a JavaScript function, but what about a React component?

## How to Pass Data to a React Component

A React component looks a lot like a plain JavaScript function. But unlike a JS function, it returns and renders React elements, such as a button.

```js
function Button() {
  return <button>Click me</button>;   
}
```

![3](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/cbqcu6zf3qwpufqpbp8c.gif)
_React component, Button, that renders a button element_

To call a React component and have it display those elements, we use it as if it was a custom HTML element, but written in JavaScript.

```js
function App() {
  return <Button />;   
}

function Button() {
  return <button>Click me</button>;   
}
```

![4](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/xmcqn8e44iiid275os5r.gif)
_Button component is used in another component, App_

But how do we pass data to functions when they are called like this?

Using this HTML-like syntax, we can pass it any data we like as if it was a custom HTML attribute.

For example, if we wanted to add our own custom text to our button, we could add a text attribute and set its value equal to some string.

```js
function App() {
  return <Button text="⭐️" />;   
}

function Button() {
  return <button>Click me</button>;   
}
```

![5](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/8qf1wtif6bfamoz7cb8j.gif)
_"text" prop is added to the Button component, with value ⭐️_

In the world of React, this custom attribute is what is known as a "prop". 

We can add as many props to our components as we like. They can be any JavaScript data type.

```js
function App() {
  return <Button text="⭐️" color="green" />;   
}

function Button() {
  return <button>Click me</button>;   
}
```

![6](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/98vxu9888zplkonokr3q.gif)
_prop named "color" (with the value "green") is added to the Button component_

If we want to use the props we've passed down to our component, you might think that each one is passed as a separate argument.

![7](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/jsymr9ltwjl9kqqcxbpk.gif)
_Passed props are not provided as separate arguments to a component_

But that’s not the case. Unlike a regular JavaScript function, all of these props are collected into one value, which is itself an object.

This single parameter is referred to and named "props”.

![8](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/h2vkphx043s8x0mewa58.gif)
_All props that are passed to a component become properties on a single object within that component's parameters_

It can be named anything, but the convention is to call this parameter "props" because that's what it contains – all of the values that are passed down to this component.

Another reason it makes sense to call these values “props” is because what we've passed down are turned into properties on an object.

Once we’ve passed down the data that we like to our component, they can be used inside that component with curly braces.

```js
function App() {
  return <Button text="⭐️" color="green" />;   
}

function Button(props) {
  return (
    <button style={{ background: props.color }}>
     {props.text}
    </button>
  );
}
```

![9](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/n5smudo77dekbv641msq.gif)
_The "color" and "text" props are used as properties within the Button component_

And a neat pattern to use if your components are small, is to destructure the props object.

By adding a set of curly braces in your parameters, you can use destructure props into individual variables that you can use directly.

```js
function App() {
  return <Button text="⭐️" color="green" />;   
}

function Button({ color, text }) {
  return (
    <button style={{ background: color }}>
     {text}
    </button>
  );
}
```

![10](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/1c19ivyfpnfnpepejkjp.gif)
_Props are destructured as individual variables within the Button component, "color" and "text"_

## 🏆 Become a Professional React Developer

React is hard. You shouldn't have to figure it out yourself.

I've put everything I know about React into a single course, to help you reach your goals in record time:

[**Introducing: The React Bootcamp**](https://www.thereactbootcamp.com)

It features over 100 hands-on challenges, real-world projects, and a complete series of animations to help you finally understand how React works.

**It’s the one course I wish I had when I started learning React.**

Click below to try the React Bootcamp for yourself:

[![Click to join the React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Click to get started*

