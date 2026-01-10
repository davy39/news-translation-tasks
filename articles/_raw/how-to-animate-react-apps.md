---
title: How to Animate Your React Apps with Lottie
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-03-10T17:07:22.000Z'
originalURL: https://freecodecamp.org/news/how-to-animate-react-apps
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/how-to-animate-react-apps.png
tags:
- name: animation
  slug: animation
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: null
seo_desc: "Animations can make for a more engaging user experience in our React apps.\
  \ \nTo make good looking animations, however, can be a great deal of work and can\
  \ require a lot of code.\nI am going to show you how to use a very powerful library\
  \ with React to m..."
---

Animations can make for a more engaging user experience in our React apps. 

To make good looking animations, however, can be a great deal of work and can require a lot of code.

I am going to show you how to use a very powerful library with React to make stunning, pixel-perfect animations that enhance your apps, without a lot of work.

## Introducing the Lottie Library for React

The library I’m talking about is called Lottie. Lottie provides a totally different way of creating impressive animations by using animations that are produced in the popular program Adobe After Effects, which are imported and exported as JSON files.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/a8unjslg43xwnrjtvokh.gif)

And best of all, to find and use these animations, you don’t need to have the program Adobe After Effects.

## How to Use LottieFiles

All you need to do is to use a completely free resource called [LottieFiles](https://lottiefiles.com). It's a site that hosts tons of free and paid Lottie animations.

Let’s say we want an animated React logo in our application (note that you can use any animation that they make available).

I’ll personally choose the following React animation from LottieFiles in which [the React logo is spinning](https://lottiefiles.com/6610-react-logo-spinning). From there, we can preview it and change things like the background color. 

When we’re ready to use it, we can download the animation’s JSON file by selecting Lottie JSON:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/4ulaytnlgqbk6eesw3un.png)

Regardless of how you’ve created your React project, you can put it in whatever folder you like. You can put it in the static folder in the root of your project or you can put it in an animations folder in the src folder. 

It is up to you, as we will be importing the JSON data from whatever the file path may be. 

I chose to put my JSON file (called react-logo.json) in my static folder:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/6z09zv7kdv5ofkqvf8x3.png)

## How to Install Lottie-Web

Once that’s done, we’ll install Lottie by bringing in the package `lottie-web`.

```bash
npm i lottie-web
```

Note that there is an alternative Lottie package available called `react-lottie`, but it uses `lottie-web` under the hood which can be easily used directly as you’ll see in just a moment.

Once `lottie-web` is installed, we can place our animation within any JSX element by giving an indication that we want it to live in a certain selector. 

The best way to do this is by using the id attribute, since it should only be used once across our app's elements.

In our case, we could give it the id value of `react-logo`:

```jsx
// src/App.js
import React from "react";

export default function App() {
  return (
    <div>
      <h1>Hello World</h1>
      <div id="react-logo" />
    </div>
  );
}
```

To use Lottie, we can import it from `lottie-web` and we’ll import the JSON from wherever we placed it:

```jsx
// src/App.js
import React from "react";
import lottie from "lottie-web";
import reactLogo from "../static/react-logo.json";

export default function App() {
  return (
    <div>
      <h1>Hello World</h1>
      <div id="react-logo" />
    </div>
  );
}
```

## How to Use Lottie with the useEffect Hook

Using Lottie itself is simple. We need to get a reference to the JSX/DOM element that we want to put the animation in and give it the JSON data.

To interact with the DOM itself, we’ll need to make sure the component has mounted, so we’ll use `useEffect` to perform a side effect and pass in an empty dependencies array.

In `useEffect`, we can now call `lottie.loadAnimation` to run our animation, by passing it an object. On this object, the first thing we’ll need to provide is the container, the DOM node that we want this animation to be run in.

We’ll can use any method we want to reference the DOM node; I’ll personally use `document.getElementById('react-logo')`.

```jsx
// src/App.js
import React from "react";
import lottie from "lottie-web";
import reactLogo from "../static/react-logo.json";

export default function App() {
  React.useEffect(() => {
    lottie.loadAnimation({
      container: document.querySelector("#react-logo"),
    });
  }, []);

  return (
    <div>
      <h1>Hello World</h1>
      <div id="react-logo" />
    </div>
  );
}


```

And with that container, we just need to supply the JSON data itself on a property called `animationData`.

```jsx
// src/App.js
import React from "react";
import lottie from "lottie-web";
import reactLogo from "../static/react-logo.json";

export default function App() {
  React.useEffect(() => {
    lottie.loadAnimation({
      container: document.querySelector("#react-logo"),
    });
  }, []);

  return (
    <div>
      <h1>Hello World</h1>
      <div id="react-logo" />
    </div>
  );
}


```

After that you should see the animation run automatically:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/yfn5x0sklji6legt1egf.gif)

If you have the same code I have, and have your animation running in an empty div, it will look huge. 

You can fix that by providing some styles and adding a fixed width and height for the container div:

```jsx
<div id="react-logo" style={{ width: 200, height: 200 }} />
```

## Lottie.loadAnimation properties

Along with container and animationData, there are some other important properties that we can pass to `loadAnimation` to change the animation’s appearance and function.

```jsx
lottie.loadAnimation({
  container: document.querySelector("#react-logo"),
  animationData: reactLogo,
  renderer: "svg", // "canvas", "html"
  loop: true, // boolean
  autoplay: true, // boolean
});


```

Above, I’ve included all of the default settings for `loadAnimation`. The default way the animation is rendered is as SVG, with the `renderer` property. This has the most features, but the HTML option can be more performant and supports 3D layers.

The animation loops or repeats infinitely by default because `loop` is set to true. You can turn this behavior off by setting it to false.

The animation’s `autoplay` setting is by default true, meaning the animation will play automatically when it is loaded. If you wanted to conditionally run the animation, you could set it to true or false by using a state variable (say if you wanted to play the animation only when it was visible).

## How to Add Lottie Light

Finally, the last thing I’ll mention about Lottie is that `lottie-web` is a rather large dependency. 

If you would like to use all of its features but are concerned about bringing too much code into your final bundle, you can import the light version of Lottie as follows:

```jsx
import lottie from "lottie-web/build/player/lottie_light";
```

## Final Code

Hopefully this post helped you get up and running with Lottie as a neat feature to add to your React projects when you’re looking for something special in your web apps.

Check out the [CodeSandbox link](https://codesandbox.io/s/damp-dust-i7k1u?file=/src/App.js:174-292) if you’d like to play around with the final code yourself.

## Become a Professional React Developer

React is hard. You shouldn't have to figure it out yourself.

I've put everything I know about React into a single course, to help you reach your goals in record time:

[**Introducing: The React Bootcamp**](https://www.thereactbootcamp.com)

**It’s the one course I wish I had when I started learning React.**

Click below to try the React Bootcamp for yourself:

[![Click to join the React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Click to get started*

