---
title: How to Animate Your React Apps with 1 Line of Code
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2022-09-15T19:56:57.000Z'
originalURL: https://freecodecamp.org/news/animate-react-apps
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/mugshotbot.com_customize_color-red-image-9129875b-mode-dark-pattern-topography-theme-two_up-url-https___freecodecamp.org.png
tags:
- name: animation
  slug: animation
- name: React
  slug: react
seo_title: null
seo_desc: "Animations have the powerful ability to turn a boring, static application\
  \ into a more dynamic, memorable experience for your users. \nIn general, animations\
  \ can be quite difficult to set up, especially if you intend to animate multiple\
  \ components in y..."
---

Animations have the powerful ability to turn a boring, static application into a more dynamic, memorable experience for your users. 

In general, animations can be quite difficult to set up, especially if you intend to animate multiple components in your app. 

In this tutorial, we will see how to implement virtually every common animation in your React apps with one line of code using the library **AutoAnimate**.

## Why You Should Use AutoAnimate

If you're building a React application, there are many powerful animation libraries you can choose, such as Framer Motion.

The downside of most of these libraries (as well as plain CSS) is that they require quite a bit of code to make your animations work. You traditionally have to specify:

1. The CSS properties you want to animate
2. The duration over which you want the animation to be performed
3. An easing function that determines how the animation progresses through the duration of each cycle

AutoAnimate removes to need to specify **any** of these things.

The power of AutoAnimate is that it allows you to animate your entire app using a using a single function called `autoAnimate`.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/Screen-Shot-2022-09-15-at-11.37.45-AM.png)
_The AutoAnimate animation library_

## How AutoAnimate Works

`autoAnimate` takes one argument: a reference to the parent element which you would like to animate. 

The way the library works is that the parent element will be "auto animated" along with any of its immediate children.

Animations take place whenever one of three events occurs to this parent element:

If a child element is **added**, **removed**, or **moved** around.

We're going to look at how you can use AutoAnimate with three examples: an expandable component, list component and a grid component.

## How to Use AutoAnimate

There are two steps to start using auto animate:

1. Install it in your project using either yarn or NPM 

```bash
npm install @formkit/auto-animate
```

1. Import the auto animate function from the library itself

```js
import autoAnimate from '@formkit/auto-animate'
```

This tutorial covers how to use AutoAnimate in React applications, but you can use it in virtually any JavaScript project (including Svelte, Vue and Vanilla JS).

To animate any parent element you just need to pass a reference of the element to the function.

```js
import { useEffect, useRef } from 'react'

function Component() {
  const parentRef = useRef(null)

  useEffect(() => {
    if (parentRef.current) {
      autoAnimate(parentRef.current);   
    }
  }, [parent])

  return (
    <div ref={parentRef}>
    // ...
  )
}
```

We can see how this works on simple expandable components such as an FAQ (Frequently Asked Questions) component. 

Let's say we want our users to be able to click on a div and expand it to show some more text. 

First, we create a div with some text to display in its initial state (`Show More` ) as well as some text to reveal when clicked.

To animate the text opening, we use the `useRef` hook to reference the parent element and then pass that reference to the auto animate function. 

%[https://codesandbox.io/embed/epic-lamport-5y9uwk?fontsize=14&hidenavigation=1&theme=dark]

And instantly, we have a much more engaging, smoothly animated component.

## How to Animate Lists with AutoAnimate

Another great use case for auto animate is with a list component. 

Let's say we are building a todo application and we would like to animate new items that are added to the list.

```js
import { useState } from "react"
import autoAnimate from "@formkit/auto-animate"

export default function App() {
  const [items, setItems] = useState(["Buy Gas", "Do Laundry"])

  function addItem() {
    const item = "Go To Store"
    setItems([...items, item])
  }

  return (
    <>
      <ul ref={parent}>
        {items.map((item) => (
          <li key={item}>{item}</li>
        ))}
      </ul>
      <button onClick={addItem}>Add Todo</button>
    </>
  )
}
```

In this example, we have a list of to do items, and whenever we click a button it adds a new item to our list. 

If we want to animate it, we can repeat the same steps as before but we add a reference to the parent element (in this case, an unordered list).

%[https://codesandbox.io/embed/unruffled-night-ugucy0?fontsize=14&hidenavigation=1&theme=dark]

Whenever we click the button to add a new item to our list, now each to do is inserted into the list in a smooth manner, animating both its position and opacity.

## How to Customize Animations

AutoAnimate is intended to be an all-in-one solution for animations that does not require configuration, but it does permit us to customize values such as the duration and when the animation plays.

For greater control over our animations, we can use the `useAutoAnimate` which can be imported in this way:

```js
import { useAutoAnimate } from "@formkit/auto-animate/react";
```

Just like any React hook, it is called at the top of any React component in which we want to use it.

The benefit of this hook is that we no longer need to use the `useRef` hook. Instead, the hook returns it as well as a function that allows us to control whether we want to animate the parent element or not.

```js
import { useAutoAnimate } from "@formkit/auto-animate/react";

export default function App() {
  const [parent, enable] = useAutoAnimate({ duration: 500 });
  const [isEnabled, setIsEnabled] = useState(true);

  function toggleEnabled() {
    enable(!isEnabled);
    setIsEnabled(!isEnabled);
  }
 
   // ...
 }
```

Let's say we're using a form to add a new item to this grid and we want to smoothly push all the others out of the way.

AutoAnimate once again makes this very easy, but in this case, we will use the `useAutoAnimate` hook to perform the animation after half a second. To do so, we can use the duration property.

```jsx
  const [parent, enable] = useAutoAnimate({ duration: 500 });

```

As you see, it handles both the animation in of the new card being added as well as the animation of pushing all the other cards aside.

%[https://codesandbox.io/embed/boring-haze-k7tdjr?fontsize=14&hidenavigation=1&theme=dark]

And that's it! Now you can use this helpful library to easily animate your React apps.

## Become a Professional React Developer

React is hard. You shouldn't have to figure it out yourself.

I've put everything I know about React into a single course, to help you reach your goals in record time:

[**Introducing: The React Bootcamp**](https://www.thereactbootcamp.com)

**It’s the one course I wish I had when I started learning React.**

Click below to try the React Bootcamp for yourself:

[![Click to join the React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Click to get started*

