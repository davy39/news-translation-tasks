---
title: React State for Absolute Beginners
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2022-03-09T16:48:55.000Z'
originalURL: https://freecodecamp.org/news/react-state
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/react-state-absolute-beginners.png
tags:
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
- name: 'State Management '
  slug: state-management
seo_title: null
seo_desc: "One of the most essential concepts that any modern JavaScript developer\
  \ needs to understand is state. \nIf you don't understand state, you're not going\
  \ to be able to fully use and take advantage of powerful libraries such as React\
  \ to build your applic..."
---

One of the most essential concepts that any modern JavaScript developer needs to understand is **state**. 

If you don't understand state, you're not going to be able to fully use and take advantage of powerful libraries such as React to build your applications. 

Let's see exactly what state is, how it already exists in your JavaScript applications now, and how React allows us to much more easily manage it with built-in hooks like `useState`.

## What is state?

Something that may surprise you is that any website or application you build with plain JavaScript already involves state. It's just not obvious where it lives. 

Here is a basic example:

Let's say that we're building a counter application with JavaScript. We want this application to be able to display the current count as well as increase and decrease the count by one. 

It will consist of just the current count as well as a button to increase the count by one and another to decrease the count by one.

This is what the final version of our app will look like:

![Image](https://www.freecodecamp.org/news/content/images/2022/03/TKZ1PcCJxw9ORF2DSIEdw.gif)
_The final counter app_

Here is the starting markup for our application:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Counter App</title>
    <meta charset="UTF-8" />
  </head>

  <body>
    <div>
      <button>+ 1</button>
      <span>0</span>
      <button>- 1</button>
    </div>
  </body>
</html>
```

Simply put, **state is data that we need to manage over time within our application.** 

State is often changed through user input and that is the case within our application here. 

What is the state in our counter app? It is the count number. 

Our user can increase or decrease the state value by clicking on the appropriate button. What's important is that we want to display those changes to our user. 

## Problems with state in plain JavaScript

While state seems like a simple concept, there are two problems with managing it when you use plain JavaScript alone:

1. It is not obvious what the state is or where it lives.
2. Reading and updating the state is an unnatural and often repetitive process when using native browser APIs like `document`. 

How would we go about updating our count state when our user clicks on either button?

We first need to get a reference to each element. To do this in plain JavaScript, it is common practice to add a unique `id` attribute to each element, select each element in JavaScript with the `document.querySelector` method, and store the reference in a local variable:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Counter App</title>
    <meta charset="UTF-8" />
  </head>

  <body>
    <div>
      <button id="increment">+ 1</button>
      <span id="count">0</span>
      <button id="decrement">- 1</button>
    </div>

    <script>
      const increment = document.querySelector("#increment");
      const count = document.querySelector("#count");
      const decrement = document.querySelector("#decrement");
    </script>
  </body>
</html>
```

Now that we have references to every HTML element, how do we make the increment button work?

We first need to listen for a click event on our increment button. Then, when the button is clicked, we need to get the current count value from the element with the `id` of "count". 

To do so, we dive into the HTML document using the `document` API and get that value with `count.innerText`. The `innerText` value is a string, so we convert it to a number, add 1, and then write that value _back_ to `count.innerText`. 

To make the decrement button work, we do the same steps again. The only difference is that we use the expression `Number(count.innerText - 1)`.

```js
<!DOCTYPE html>
<html>
  <head>
    <title>Counter App</title>
    <meta charset="UTF-8" />
  </head>

  <body>
    <div>
      <button id="increment">+ 1</button>
      <span id="count">0</span>
      <button id="decrement">- 1</button>
    </div>

    <script>
      const increment = document.querySelector("#increment");
      const count = document.querySelector("#count");
      const decrement = document.querySelector("#decrement");

      increment.addEventListener("click", () => {
        count.innerText = Number(count.innerText) + 1;
      });

      decrement.addEventListener("click", () => {
        count.innerText = Number(count.innerText) - 1;
      });
    </script>
  </body>
</html>
```

This isn't too much code, but you can see that there are a number of steps here that are not very intuitive and repetitive:

* Add arbitrary id to HTML elements
* Query for the element using JavaScript
* Store element reference in variable
* Listen for appropriate event on element
* Get current state value using `document` API
* Write new state value back to the page with `.innerText`

These are a lot of low-level instructions that are required for our program to operate, but they don't help us thinking about the underlying state.

As we saw, the state lives in the browser. This means we have to "find" the state first and then **imperatively** (in a way that the computer understands better than we do) update that value.

Fortunately, React gives us a much easier way of updating state and _thinking_ about state.

## How does React help us manage state?

One significant benefit of using React and why it's in your interest to use React in develop your JavaScript applications is that it gives you much easier patterns for updating your state. 

Unlike plain JavaScript, React takes care of the difficult work of updating what the user sees. All we have to do is tell it what state we're managing and what the new value should be. 

Instead of the state living within the browser and having to find it every time we need to read it or update it, we are able to simply put it in a variable and then update that variable's value. After we do that, the update and new value will be displayed to our users. 

**This is the whole concept of managing state in React.** 

Instead of using an HTML document, we can write all of our markup within a React component. 

It is written identically to a regular JavaScript function and it displays the same HTML elements using an identical syntax called JSX.

```js
export default function Counter() {
  return (
    <div>
      <button>+ 1</button>
      <span>0</span>
      <button>- 1</button>
    </div>
  );
}
```

How can we make the same counter application with React? 

In our React app, once we've identified what our state is, we control it using a JavaScript variable.

This variable can be declared in many ways. The most popular way to manage component state is with the **`useState` hook**.

A **hook** in React works very similarly to regular JavaScript functions. That means we can call it up at the top of our component and we pass it the default value as the starting value for our counter app. 

Since the starting value of our count value is zero, we just call our hook and pass it the value `0` and that value is put into our state variable. 

```js
import { useState } from 'react';

export default function Counter() {
  // the count value lives and is managed up here!
  const [count] = useState(0);  
    
  return (
    <div>
      <button>+ 1</button>
      <span>{count}</span> {/* use curly braces to output the count value: 0 */}
      <button>- 1</button>
    </div>
  );
}
```

There's no need to use `count.innerText` anymore. We can just output and read the value of our state by using `count`.

Just like any JavaScript variable, we can name it however we want. It doesn't have to be called `count`. You could call it literally anything else as long as its a valid JavaScript name.

The return value from `useState` is an array. When we destructure it, the first destructured value is the state variable. The second one is the function to update state. 

```js
import { useState } from 'react';

export default function Counter() {
  const [count, setCount] = useState(0);  
    
  return (
    <div>
      <button>+ 1</button>
      <span>{count}</span>
      <button>- 1</button>
    </div>
  );
}
```

How do we make the increment button work?

Here's what we _don't_ need to do:

* We don't need to add an `id` to our HTML elements 
* We don't need to dive into the DOM and figure out which button is which
* We don't need to listen for a click event with `document.addEventListener`

To update state when you click on a button, add the `onClick` prop to each button. This allows you to call a function when the button is pressed by the user. 

For the increment button, we will update state by passing `count + 1` to `setCount`, and for the decrement button, we will pass `count - 1` to `setCount`.

```js
import { useState } from 'react';

export default function Counter() {
  const [count, setCount] = useState(0);  
    
  function incrementCount() {
    setCount(count + 1);
  }
    
  function decrementCount() {
    setCount(count - 1);   
  }
    
  return (
    <div>
      <button onClick={incrementCount}>+ 1</button>
      <span>{count}</span>
      <button onClick={decrementCount}>- 1</button>
    </div>
  );
}
```

This is all the code we need to create a working counter app with React.

When each button is pressed and state is updated, React will do all the work of updating the page so that the user can see the new state.

This is the great benefit of using React versus plain JavaScript: when state is managed using hooks like `useState` and React takes care of efficiently updating what the user sees, we can create simpler, more reliable apps where state is easy to see, read and update.

## Become a Professional React Developer

React is hard. You shouldn't have to figure it out yourself.

I've put everything I know about React into a single course, to help you reach your goals in record time:

[**Introducing: The React Bootcamp**](https://www.thereactbootcamp.com)

**It’s the one course I wish I had when I started learning React.**

Click below to try the React Bootcamp for yourself:

[![Click to join the React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Click to get started*

