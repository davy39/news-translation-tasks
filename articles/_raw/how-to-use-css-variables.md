---
title: How To Use CSS Variables – Explained with Code Examples
subtitle: ''
author: Matéu.sh
co_authors: []
series: null
date: '2024-04-02T19:53:03.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-css-variables
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/CSS-Variables.png
tags:
- name: CSS
  slug: css
- name: React
  slug: react
- name: variables
  slug: variables
seo_title: null
seo_desc: 'If you are building websites or web apps, you should already know that
  code repetition is considered a bad practice.

  That''s why you should learn how to use CSS variables to reduce the amount of CSS
  code you write and take your styling to a new level....'
---

If you are building websites or web apps, you should already know that code repetition is considered a bad practice.

That's why you should learn how to use CSS variables to reduce the amount of CSS code you write and take your styling to a new level.

The most successful web apps have spectacular designs. Unfortunately, to reach the desired effects, web developers need to prepare large amounts of styles. This forces us to repeat values, such as colors, in many different elements. 

Fortunately, modern stylesheets support CSS variables, which lets you reduce repetition in your codebase. You don't need external tools such CSS modules, Less or SASS to take advantage of it. 

In this comprehensive guide, I'm going to show you how to effectively use CSS variables, covering basic examples in plain HTML and CSS to more advanced frameworks like React and Next.js.

## Prerequisites

This guide is dedicated to beginners so you don't need any special knowledge to benefit from it. 

I included a few examples in React and Next.js and they are dedicated to beginner React developers. Only those examples will require basic React knowledge to understand them. Feel free to skip them if you don't work with React.

## What are CSS Variables?

CSS variables (officially called CSS custom properties) allow developers to manage and reuse values in CSS stylesheets. Web developers can define reusable variables that can use be used across many CSS files, making code easier to update. CSS variables make it super easy to implement features such as dark mode.

Modern websites require large amounts of styles and this results in repeated CSS values in many different stylesheets. The ecosystem was working hard to address this issue by inventing tools such as SASS, Less and CSS modules but all of those tools have a flaw – they need to be compiled to CSS files in the end.

Fortunately, thanks to CSS variables, we can simplify our stylesheets without sophisticated tools and build processes.

## How To Create CSS Variables

Defining a CSS variable is quite simple. You can define a CSS variable using the `--` prefix followed by a name of your choice, then assigning it a value using the `var()` function. 

Here's how you do it:

```css
:root {
  /* Backgrounds */
  --primary-background: #faf8ef;
  /* Colors */
  --primary-text-color: #776e65;
}
```

As you can see, I defined CSS variables inside the `:root` pseudo-class to make them globally available. 

Each variable started with `--`, followed by a name: `--primary-background` or `--primary-text-color`. Lastly, I assigned values to those variables.

Using this, I'll be able to change website colors just by modifying the values of those variables.

## How To Use CSS Variables

Now let me show you how to use CSS variables to define global background and text color for your website:

```css
body {
  margin: 0;
  background: var(--primary-background);
  color: var(--primary-text-color);
}
```

To use a variable, you need to refer to them by using the `var()` function and passing the variable name as an argument.

That's it! Now your website is using CSS variables to render styles.

**Note**: `var()` helper is a built-in CSS function so you don't need any libraries to use it.

## How To Use CSS Variables in React?

Many web developers build their web apps in React so I will show you how you can get values and update CSS variables in React. Many modern web apps support dark mode and this feature can become one of a React developer's nightmares. 

Next, I'll show you an easy method to add a dark mode in React apps just by using CSS variables. 

### How To Set the Value of CSS Variable in React?

Changing the value of CSS variables in React might be tricky since React doesn't offer any tools to directly interact with the DOM tree. That's why we'll use plain JavaScript to read and set CSS variables. 

Here's how you can set a CSS Variable in React:

```jsx
import { useEffect } from 'react';

export default function Example() {
  useEffect(() => {
    document.documentElement.style.setProperty('--primary-background', `black`);
    document.documentElement.style.setProperty('--primary-text-color', `white`);
  }, [])

  return <div style={{color: "var(--primary-text-color"}}>Hello World</div>
};

```

As you can see, I took advantage of the global `document` variable to get into the DOM tree and modify style properties. I used `setProperty` method that requires two arguments:

* CSS custom property (CSS variable) name.
* The value of the variable.

**Note**: It doesn't matter if you work in React or plain JavaScript, you can always call `document.documentElement.style.setProperty` to modify CSS variable values. It's a JavaScript built-in function.

### How To Get the Value of CSS Variables in React?

Sometimes you might need to read the value of a CSS variable and store it in React. In this case, I would suggest utilizing `useState` and `useEffect` hooks. 

Here's how I would approach this issue:

```jsx
import { useEffect, setState } from 'react';

export default function Example() {
  const [color, setColor] = useState('black');

  useEffect(() => {
    const cssColor = document.documentElement.style.getPropertyValue('--primary-text-color');
    setColor(cssColor);
  }, [])

  return <div style={{color: color}}>Hello World</div>
};

```

As you can see, I retrieved the value of a `--primary-text-color` variable to the `cssColor` constant. In the next line, I updated component's state by using `setColor` helper created by `useState` hook. Using the method, my CSS variable can be used easily in React Components.

That's it. Now you can use this variable in your React app.

## Conclusion

CSS variables can be used in different kinds of websites and no JavaScript is needed to take advantage of them. Everybody can benefit of them – no matter their level of experience in web development. Understanding CSS variables can greatly improve your styling experience and make you more efficient.

I hope you liked this article. It would mean the world to me if you share it on your social media.

If you have any questions or just want to hear updates from me, you can find me on [Twitter](https://twitter.com/msokola).

## Learn React

If you are still learning React or you want to learn more tricks like this one, you should join my course on Next.js. Next.js is the most popular React framework that powers the most of React app these days. I will teach you how to use it by building an awesome 2048 game with animations. No fluff. Tactics only.

🚀 **Join m**y [Next.js Crash **Course**](https://www.mateu.sh/learn-nextjs).

This course includes:

* 🎥 5.5 hours on-demand video
* 📱 Access on mobile and TV
* 🗓️ Full lifetime access
* 🎓 Certificate of completion

[![Click to join the Next.js Crash Course](https://assets.mateu.sh/assets/fcc-css-variables)](https://mateu.sh/learn-nextjs)  
_Click to get started_


