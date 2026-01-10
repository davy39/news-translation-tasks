---
title: How to Make Your React Apps Responsive with a Custom Hook
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-03-19T16:28:08.000Z'
originalURL: https://freecodecamp.org/news/make-react-apps-responsive
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/make-your-react-apps-responsive-with-a-custom-hook.png
tags:
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
- name: responsive design
  slug: responsive-design
seo_title: null
seo_desc: 'How do you make your React applications responsive for any sized device?
  Let''s see how to do so by making our own custom React hook.

  At the top of my React site is a Header component. As I decrease the size of the
  page, I want to show fewer links:


  T...'
---

How do you make your React applications responsive for any sized device? Let's see how to do so by making our own custom React hook.

At the top of my React site is a Header component. As I decrease the size of the page, I want to show fewer links:

![resizing window to show header](https://dev-to-uploads.s3.amazonaws.com/i/kxbnn3jmwjarkc8zrpbm.gif)

To do this we could use a media query with CSS, or we could use a custom React hook to give us the current size of the page and hide or show the links in our JSX.

Previously, I was using a hook from the a library called `react-use` to add this functionality. 

Instead of bringing an entire third-party library, however, I decided to create my own hook that would provide the dimensions of the window, both the width and height. I called this hook `useWindowSize`.

## How to create the custom hook

First, we’ll create a new file .js in our utilities (utils) folder, the same name as the hook `useWindowSize` and I’ll import React (to use hooks) while exporting the custom hook.

```js
// utils/useWindowSize.js

import React from "react";

export default function useWindowSize() {}

```

Now since I’m using this within a Gatsby site, which is server rendered, I need to get the size of the window. But we may not have access to it because we’re on the server. 

To check and make sure we’re not on the server, we can see if type of `window` is not equal to the string `undefined`.

In which case we can return to a default width and height for a browser, say, 1200 and 800 within an object:

```js
// utils/useWindowSize.js

import React from "react";

export default function useWindowSize() {
  if (typeof window !== "undefined") {
    return { width: 1200, height: 800 };
  }
}
```

## How to get the width and height from window

And assuming we are on the client and can get the window, we can take the `useEffect` hook to perform a side effect by interacting with `window`. We’ll include an empty dependencies array to make sure the effect function is called only once the component (that this hook is called in) is mounted.

To find out the window width and height, we can add an event listener and listen for the `resize` event. And whenever the browser sizes change, we can update a piece of state (created with `useState`), which we’ll call `windowSize` and the setter to update it will be `setWindowSize`.

```js
// utils/useWindowSize.js

import React from "react";

export default function useWindowSize() {
  if (typeof window !== "undefined") {
    return { width: 1200, height: 800 };
  }

  const [windowSize, setWindowSize] = React.useState();

  React.useEffect(() => {
    window.addEventListener("resize", () => {
      setWindowSize({ width: window.innerWidth, height: window.innerHeight });
    });
  }, []);
}
```

When the window is resized, the callback will be called and the `windowSize` state will be updated with the current window dimensions. To get that, we set the width to `window.innerWidth`, and height to `window.innerHeight`.

## How to add SSR support

However, the code as we have it here will not work. And this is because a key rule of hooks is that they cannot be called conditionally. As a result, we cannot have a conditional above our `useState` or `useEffect` hook, before they are called.

So to fix this, we’ll set the initial value of `useState` conditionally. We’ll create a variable called `isSSR`, which will perform the same check to see if the window is not equal to the string `undefined`.

And we’ll use a ternary to set the width and height by first checking to see if we’re on the server. If we are we’ll use the default value. If not, we’ll use `window.innerWidth` and `window.innerHeight`.

```js
// utils/useWindowSize.js

import React from "react";

export default function useWindowSize() {
  // if (typeof window !== "undefined") {
  // return { width: 1200, height: 800 };
  // }
  const isSSR = typeof window !== "undefined";
  const [windowSize, setWindowSize] = React.useState({
    width: isSSR ? 1200 : window.innerWidth,
    height: isSSR ? 800 : window.innerHeight,
  });

  React.useEffect(() => {
    window.addEventListener("resize", () => {
      setWindowSize({ width: window.innerWidth, height: window.innerHeight });
    });
  }, []);
}
```

Then finally, we need to think about when our components unmount. What do we need to do? We need to remove our resize listener.

### Removing resize event listener

You can do that by returning a function from useEffectand we will remove the listener with `window.removeEventListener`.

```js
// utils/useWindowSize.js

import React from "react";

export default function useWindowSize() {
  // if (typeof window !== "undefined") {
  // return { width: 1200, height: 800 };
  // }
  const isSSR = typeof window !== "undefined";
  const [windowSize, setWindowSize] = React.useState({
    width: isSSR ? 1200 : window.innerWidth,
    height: isSSR ? 800 : window.innerHeight,
  });

  React.useEffect(() => {
    window.addEventListener("resize", () => {
      setWindowSize({ width: window.innerWidth, height: window.innerHeight });
    });

    return () => {
      window.removeEventListener("resize", () => {
        setWindowSize({ width: window.innerWidth, height: window.innerHeight });
      });
    };
  }, []);
}
```

But we need a reference to the same function, not two different ones as we have here. To do that, we’ll create a shared callback function to both of the listeners called `changeWindowSize`.

And finally, at the end of the hook, we will return our `windowSize` state. And that’s it.

```js
// utils/useWindowSize.js

import React from "react";

export default function useWindowSize() {
  const isSSR = typeof window !== "undefined";
  const [windowSize, setWindowSize] = React.useState({
    width: isSSR ? 1200 : window.innerWidth,
    height: isSSR ? 800 : window.innerHeight,
  });

  function changeWindowSize() {
    setWindowSize({ width: window.innerWidth, height: window.innerHeight });
  }

  React.useEffect(() => {
    window.addEventListener("resize", changeWindowSize);

    return () => {
      window.removeEventListener("resize", changeWindowSize);
    };
  }, []);

  return windowSize;
}
```

## How to use the hook

To use the hook, we just need to import it where we need, call it, and use the width wherever we want to hide or show certain elements.

In my case, this is at the 500px mark. There, I want to hide all of the other links and only show the Join Now button, like you see in the example above:

```js
// components/StickyHeader.js

import React from "react";
import useWindowSize from "../utils/useWindowSize";

function StickyHeader() {
  const { width } = useWindowSize();

  return (
    <div>
      {/* visible only when window greater than 500px */}
      {width > 500 && (
        <>
          <div onClick={onTestimonialsClick} role="button">
            <span>Testimonials</span>
          </div>
          <div onClick={onPriceClick} role="button">
            <span>Price</span>
          </div>
          <div>
            <span onClick={onQuestionClick} role="button">
              Question?
            </span>
          </div>
        </>
      )}
      {/* visible at any window size */}
      <div>
        <span className="primary-button" onClick={onPriceClick} role="button">
          Join Now
        </span>
      </div>
    </div>
  );
}
```

This hook will work on any server rendered React app, such as Gatsby and Next.js.

## Become a Professional React Developer

React is hard. You shouldn't have to figure it out yourself.

I've put everything I know about React into a single course, to help you reach your goals in record time:

[**Introducing: The React Bootcamp**](https://www.thereactbootcamp.com)

**It’s the one course I wish I had when I started learning React.**

Click below to try the React Bootcamp for yourself:

[![Click to join the React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Click to get started*

