---
title: How to Create a Reusable Fade-in Animation Component in React With GSAP
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-27T22:16:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-reusable-fade-in-animation-component-in-react-with-gsap
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9983740569d1a4ca2029.jpg
tags:
- name: animation
  slug: animation
- name: React
  slug: react
- name: Web Design
  slug: web-design
seo_title: null
seo_desc: 'By Dillion Megida

  If you haven''t heard about or used GSAP, you''re missing out. GSAP is an animation
  library for components and elements. Their homepage shows a lot of awesome animations
  you can make with the tool.

  GSAP has a lot of configurations, an...'
---

By Dillion Megida

If you haven't heard about or used GSAP, you're missing out. GSAP is an animation library for components and elements. [Their homepage](https://greensock.com/gsap/) shows a lot of awesome animations you can make with the tool.

GSAP has a lot of configurations, and there's no one right way to achieve one type of animation. So we'll be looking at one way (opinionated) of creating a 'Fade In' animation when a component loads.

This article won't be going into detail about how to use GSAP. Their documentation is the go-to resource if you want an in-depth guide to learn the tool.

## What we're going to animate

Here's a little description of what we're going to animate:

It's something simple. When a component is loaded (wherever), it fades in. We'll also add direction so that the component fades in from area to the normal position.

We'll also make the animation component reusable so that we can apply it to different elements.

## Let's get started!

### GSAP installation

First, you must have a react project set up. [create-react-app](https://www.npmjs.com/package/create-react-app) is there for you if you need to quickly set one up for this project.

To install GSAP, enter the following command in your terminal (with the current directory being your react project directory):

```shell
npm install --save gsap
```

### Create a Usable Animation Component

#### Setting up the component

Let's call our componet, `FadeIn`:

```js
import React, {useRef, useEffect} from 'react'

const FadeInAnimation = ({children, wrapperElement = 'div', direction = null, ...props}) => {
  const Component = wrapperElement;
  const compRef = useRef(null)
  useEffect(() => {
    // animations
  }, [compRef])
  return (
    <Component ref={compRef} {...props}>
      {children}
    </Component>
  )
}

export default FadeInAnimation
```

Our animation isn't ready yet, but let's understand what we're starting with.

- `wrapperElement`: used to specify what the component would be. It has a default of `div`. This is better than creating an extra DOM node to wrap the component we want to animate.
- [`useRef`](https://reactjs.org/docs/hooks-reference.html#useref): `gsap` we need this to know what to trigger animations for. With this, we can refer to our component in the DOM.
- `useEffect`: without this, `gsap` will trigger animations with a null reference (`useRef(null)`). We have to ensure the component is mounted already, hence this hook.
- `children`: this will be what's found between `<FadeInAnimation>` and `</FadeInAnimation>`. Could be text, or even a group of elements.
- `...props`: to extend reusability, this is necessary so that the components can apply other props like `className` and `style`.
- `direction`: for cases where we want to add direction to the fade-in effect. The default value is null.

Now let's head over to GSAP.

#### Setting up the animation

```js
import React, { useRef, useEffect } from "react";
import { gsap } from "gsap";

const FadeInAnimation = ({
  children,
  wrapperElement = "div",
  direction = null,
  delay = 0,
  ...props
}) => {
  const Component = wrapperElement;
  let compRef = useRef(null);
  const distance = 200;
  let fadeDirection;
  switch (direction) {
    case "left":
      fadeDirection = { x: -distance };
      break;
    case "right":
      fadeDirection = { x: distance };
      break;
    case "up":
      fadeDirection = { y: distance };
      break;
    case "down":
      fadeDirection = { y: -distance };
      break;
    default:
      fadeDirection = { x: 0 };
  }
  useEffect(() => {
    gsap.from(compRef.current, 1, {
      ...fadeDirection,
      opacity: 0,
      delay
    });
  }, [compRef, fadeDirection, delay]);
  return (
    <Component ref={compRef} {...props}>
      {children}
    </Component>
  );
};

export default FadeInAnimation;
```

Let's go over what happened here:

- We initialized a variable `distance` to be 200. This is useful for cases where a direction is applied. You can also add this to the input props so that the component using it can decide.
- We have our `switch` case. This is to determine the direction of the fade-in, with the default case for cases where the direction is not specified.
- Then [`gsap`](https://greensock.com/docs/v3/GSAP). This is exposed from GSAP to animate our component. There's `.to`, `.from`, `.fromTo` and more you can find in the docs.
- `gsap.from` in our case refers to the initial state of the component before the final one (set in the component's stylesheet). We target the current element of the ref, apply a duration of 1 second, and apply the animation options.
- `...fadeDirection`: we spread the object so it appears there as `{x: 200}` or as specified. `x` is for horizontal and `y` is for vertical.
- Then, an initial opacity of 0 and a delay as specified by the component.

And that's it. Let's make a component that uses this awesome animation.

### How to use our resuable fade in component

Head over to the component you want to animate and do something similar to the following:

```js
import React from "react";
import FadeInAnimation from "./FadeInAnimation";

export default function App() {
  return (
    <div>
      <FadeInAnimation wrapperElement="h1" direction="down">
        Hello CodeSandbox
      </FadeInAnimation>
      <FadeInAnimation wrapperElement="h2" direction="right" delay={2}>
        Start editing to see some magic happen!
      </FadeInAnimation>
      <FadeInAnimation
        style={{
          width: 200,
          color: "white",
          height: 200,
          backgroundColor: "purple"
        }}
        direction='up'
      >
        <p>Hello</p>
      </FadeInAnimation>
    </div>
  );
}
```

As seen above, our `FadeInAnimation` component can accept a `style` prop. Remember we did `...props`.

Here's the result in [CodeSandBox](https://codesandbox.io/s/react-gsap-fadein-effect-z8xqd?file=/src/App.js)

## Wrap up

That's a wrap. This is a simple (opinionated) usage of GSAP for fade-in effects. 

Of course, you can configure it further, like making a fade-in bounce effect, fade-in rotate, and other fun things. But I hope this article has given you a brief and concise introduction to how awesome GSAP is and how to get started doing amazing things on the web.

Side note: this is similar to the setup I'm using in a new animation package I'm launching soon. I'll share it in this article when it's published : )



