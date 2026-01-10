---
title: SVG Toggle Button Tutorial – How to Handle Dark Mode with CSS and JavaScript
subtitle: ''
author: Hunor Márton Borbély
co_authors: []
series: null
date: '2024-03-08T13:46:26.000Z'
originalURL: https://freecodecamp.org/news/how-to-handle-dark-mode-with-css-and-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/thumbnail.png
tags:
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
- name: SVG
  slug: svg
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'How can you detect dark mode in CSS and JavaScript? How can you manually
  override it with a toggle button? And how can you create a sun and moon icon with
  SVG?

  In this tutorial, you will learn how to detect dark mode in CSS and JavaScript,
  and you wi...'
---

How can you detect dark mode in CSS and JavaScript? How can you manually override it with a toggle button? And how can you create a sun and moon icon with SVG?

In this tutorial, you will learn how to detect dark mode in CSS and JavaScript, and you will create a toggle button with SVG to override the default behavior. You will use plain HTML, CSS, and JavaScript, so you don't need any preliminary requirements before starting.

You can also [watch this article as a video](https://youtu.be/GUSUA72t7p0) on YouTube.

## Table of Contents

* [How to Handle Dark Mode with CSS](#heading-how-to-handle-dark-mode-with-css)
* [How to Code a Sun Icon with SVG](#heading-how-to-code-a-sun-icon-with-svg)
* [How to Detect Dark Mode in JavaScript](#heading-how-to-detect-dark-mode-in-javascript)
* [How to Code a Moon Icon with SVG](#heading-how-to-code-a-moon-icon-with-svg)
* [How to Toggle Dark Mode with JavaScript](#heading-how-to-toggle-dark-mode-with-javascript)
* [Next Steps](#next-step)

## How to Handle Dark Mode with CSS

Let's say you have a simple website with some text. By default, you set the text color to be black and the background color to be white. Implementing dark mode for this site with CSS is very simple:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Dark Mode</title>
    <link rel="stylesheet" href="index.css" />
    <script src="index.js" defer></script>
  </head>

  <body>
    <p>
      How to detect dark mode in CSS and in JavaScript? How can we override it
      manually with a toggle button? In this quick tutorial, we look into
      detecting dark mode in CSS and JavaScript, and then we create a toggle
      button with SVG to override the default behavior.
    </p>
  </body>
</html>

```

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Screenshot-2024-03-07-at-11.33.28.png)
_A simple website with some text in dark mode_

All you need to do is add a media query and set a condition. With this condition, you set the following CSS statements to be only valid if the preferred color scheme is dark. 

Inside this media query, you can define the colors for dark mode. In this case, you flip the colors and set the text color to white and the background color to black:

```css
body {
  font-family: Montserrat;
  margin: 50px;
  max-width: 500px;
}

@media (prefers-color-scheme: dark) {
  body {
    background-color: black;
    color: white;
  }
}

```

This will take the setting from your OS or browser setting. By default, it comes from the Operating System, but the browser can decide to override it. In Google Chrome, you can find this setting under 'Appearance'. By default, it follows the device setting.

What's great about the CSS solution is that if you change this setting while visiting the website, the styling will update automatically.

This way, you can set a custom style for the body element and any other elements as well. 

It doesn't work in one case, though. You cannot style what's inside an HTML Canvas element with CSS. If you built up a [game entirely from JavaScript](https://www.freecodecamp.org/news/gorillas-game-in-javascript/) using the Canvas API or Three.js, you must also set the colors for dark mode in JavaScript.

In the next steps, we will cover this and look into how to create an SVG toggle button to switch between light and dark modes.

## How to Code a Sun Icon with SVG

Before you learn how to handle dark mode in JavaScript, let's take a quick detour and see how to code a dark mode toggle button with SVG. Detecting dark mode is one thing, but you should allow the user to manually toggle between light and dark modes.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Slides-1.022.png)
_Sun Icon_

Check out my previous tutorial if you need a quick introduction to [coding SVG icons](https://www.freecodecamp.org/news/svg-tutorial-learn-to-code-images/). It contains many great examples from beginner to advanced levels. And if you are new to SVGs, don't worry. These are very simple examples.

So, let's start with the `svg` element. This will serve as a container for all the image elements. Set its size to 30 times 30:

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Slides-1.004.png)
_The `svg` element_

Then, add a circle. For a `circle` element, you have to set the center coordinates of the circle and its radius. The center coordinates are both 15, and the radius is 6. Then, set a color with the `fill` property:

```html
<svg width="30" height="30">
  <circle cx="15" cy="15" r="6" fill="currentColor" />
</svg>
```

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Slides-1.006.png)
_We add a `circle` as the core of the sun_

To set the color, you can use the `currentColor` property that takes over the current `color` setting from CSS. This will come in handy later when you toggle dark and light modes. The icon will switch colors automatically.

Then, add the sun rays. You need to use the `line` element for this, where you have to set the starting and end coordinates. You can also set the stroke color with the `stroke` property, the `stroke-width` to add thickness, and the `stroke-linecap` property to make the ends of the lines rounded:

```html
<svg width="30" height="30">
  <circle cx="15" cy="15" r="6" fill="currentColor" />

  <line
    id="ray"
    stroke="currentColor"
    stroke-width="2"
    stroke-linecap="round"
    x1="15"
    y1="1"
    x2="15"
    y2="4"
  ></line>
</svg>
```

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Slides-1.010.png)
_We add a `line` element as a sunray_

Now, once you have one ray, you can reuse the same ray to draw the others. 

You can give this ray an `id` and reuse it with the `use` element. For the reused elements, you can set a rotation. Set the rotation angle and the center of rotation. You want to rotate the rays around the center of the sun, so set it to `15,15`. Then, increment the rotation by 45 degrees for each ray:

```html
<svg width="30" height="30">
  <circle cx="15" cy="15" r="6" fill="currentColor" />

  <line
    id="ray"
    stroke="currentColor"
    stroke-width="2"
    stroke-linecap="round"
    x1="15"
    y1="1"
    x2="15"
    y2="4"
  ></line>

  <use href="#ray" transform="rotate(45 15 15)" />
  <use href="#ray" transform="rotate(90 15 15)" />
  <use href="#ray" transform="rotate(135 15 15)" />
  <use href="#ray" transform="rotate(180 15 15)" />
  <use href="#ray" transform="rotate(225 15 15)" />
  <use href="#ray" transform="rotate(270 15 15)" />
  <use href="#ray" transform="rotate(315 15 15)" />
</svg>
```

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Slides-1.016.png)
_The finished sun icon_

## How to Detect Dark Mode in JavaScript

Before we get to the moon icon, let's see how to detect dark mode in JavaScript. This can be useful when building a game, like we did a couple weeks ago in the [Gorillas JavaScript game tutorial](https://www.freecodecamp.org/news/gorillas-game-in-javascript/). 

In that game, we were drawing on an HTML Canvas element with JavaScript. We set all the colors with JavaScript. If we want to support dark mode, we can set the colors based on a `darkMode` variable. But how do we detect if we are in dark mode? How do we set the value of this variable?

The following code is an example snippet from the game tutorial above. Here we set the fill color before we draw a rectangle on the canvas. To learn more about drawing on a `canvas` element, check out [this tutorial](https://www.freecodecamp.org/news/gorillas-game-in-javascript/).

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Slides-1.018.png)
_When drawing on a `canvas` element we set the colors from JavaScript. But how we detect dark mode?_

Detecting dark mode in JavaScript is also very simple. Interestingly enough, this solution also depends on the CSS query selectors you used before.

You can create a `matchMedia` object with the same condition we used in CSS. This method can check if the document matches a media query. Pass on `prefers-color-scheme: dark` as an argument:

```javascript
const darkModeMediaQuery = window.matchMedia("(prefers-color-scheme: dark)");

let darkMode = darkModeMediaQuery.matches;

. . .

function drawBuildings() {
  state.buildings.forEach((building) => {
    ctx.fillStyle = darkMode ? "#254D7E" : "#947285";
    ctx.fillRect(building.x, 0, building.width, building.height);
  });
}
```

Then, can check the `matches` property of this object. If it is true, then you are in dark mode. You can save this into a variable, and later, you can use this variable to decide what colors you should use when painting on the canvas element.

This variable, however, doesn't get refreshed automatically when you switch between light mode and dark mode. You need to add an event listener that detects if the settings change. 

Here, we define a function that checks the `matches` property of the incoming object to decide if you just switched to bright or dark mode:

```javascript
const darkModeMediaQuery = window.matchMedia("(prefers-color-scheme: dark)");

let darkMode = darkModeMediaQuery.matches;

darkModeMediaQuery.addEventListener("change", (e) => {
  if (e.matches) {
    darkMode = true;
  } else {
    darkMode = false;
  }
});

. . .

function drawBuildings() {
  state.buildings.forEach((building) => {
    ctx.fillStyle = darkMode ? "#254D7E" : "#947285";
    ctx.fillRect(building.x, 0, building.width, building.height);
  });
}
```

Now, if you set the colors based on this `darkMode` variable, you should see that the game's appearance changes once you switch between light and dark mode in the OS settings. Check out this [demo](https://codepen.io/HunorMarton/pen/jOJZqvp) to see it in action.

## How to Code a Moon Icon with SVG

Before we discuss overriding the default OS setting with a toggle button, let's examine the other half of our toggle icon: Let's draw a moon.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Slides-1.023.png)
_The Sun and Moon icons_

Start with an `svg` element of the same size and define a path inside it. You can define a `path` element by setting its `d` attribute. In this attribute, you build a path from a series of commands:

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Slides-1.026.png)
_We define a `path` with a series of commands_

You start with the move-to command to go to the initial position. This command consists of the letter `M` and the starting coordinate: 

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Slides-1.027.png)
_Using the move-to command within a path_

Then, use an arc command to draw the outer arc of the moon. This command might look a bit scary because it has several properties. Let's see what we have:

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Slides-1.028.png)
_The arc command and it's several properties_

A command always continues the previous command, so this arc will draw the arc from the coordinates of the move-to command. Commands also end with the coordinates of the endpoint. 

Here, you set where the arc ends. The rest of the properties are about how to draw an arc from the starting point to the endpoint:

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Slides-1.029.png)
_The last two properties of the arc command show the endpoint of the arc_

The first two properties are the horizontal and vertical radius of our arc. In our case, we want to have the arc of a circle, so we set the same value for both. With the third argument, you can set a rotation. When both radiuses are the same, this property makes no difference. You can leave it at zero:

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Slides-1.030.png)
_Horiyontal and vertical radius of the arc_

Then, we have the large arc flag property. With this, you can decide whether to go the long or short way to our end coordinate. You can see that you can reach the endpoint in multiple ways, even with the same radiuses. 

There are two arcs – in the case of the first one, you go the long way and in the case of the second one, you will go the short way. This is a flag, so the value here can be 0 or 1:

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Slides-1.032.png)
_The large arc flag decides if we should reach the endpoint the short way or the long way_

Finally, there is the sweep flag. This basically sets whether you should draw the arc clockwise or counterclockwise. The two options mirror each other. In the first case, you set this to zero – in the second, you set it to one:

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Slides-1.035.png)
_The sweep flag decides if we should go clockwise or counterclockwise_

Now that you have one arc, you set up the other one. Here, you set the endpoint to the beginning. To the same coordinates as you used for the move-to command.

Then you can use the same radiuses, but you have to change the large arc flag and the sweep flag to end up with a moon:

```html
<svg width="30" height="30">
  <path
    fill="currentColor"
    d="
      M 23, 5
      A 12 12 0 1 0 23, 25
      A 12 12 0 0 1 23, 5"
  />
</svg>
```

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Slides-1.039.png)
_The finished moon icon_

How can you use these two icons in a button to toggle light mode and dark mode in JavaScript?

## How to Toggle Dark Mode with JavaScript

If you want to override the system or browser settings for dark mode with a manual switch, you can't rely on the CSS media query anymore. This works for rendering the UI based on the settings, but you can't override it from JavaScript.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Slides-1.041.png)
_You can't override a CSS media query_

Instead, you can define a `dark-mode` class and toggle it from JavaScript. 

In CSS, define a class that will change the same settings the media query did before. Then, in JavaScript, you can use the same logic you had before to get the default setting and then add or remove this class. 

You can set this class on our initial page load and toggle it if you click a button:

```css
body {
  font-family: Montserrat;
  margin: 50px;
  max-width: 500px;
}

.dark-mode {
  background-color: black;
  color: white;
}
```

Now, how do you toggle this with a button? In your HTML file, add a button element with an event handler. Then, move both SVGs inside this button element and assign IDs for them. You will toggle the visibility of these icons from JavaScript:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Dark Mode</title>
    <link rel="stylesheet" href="index.css" />
    <script src="index.js" defer></script>
  </head>

  <body>
    <p>
      How to detect dark mode in CSS and in JavaScript? How can we override it
      manually with a toggle button? In this quick tutorial, we look into
      detecting dark mode in CSS and JavaScript, and then we create a toggle
      button with SVG to override the default behavior.
    </p>

    <button onclick="toggleDarkMode()">
      <svg width="30" height="30" id="light-icon">
        <circle cx="15" cy="15" r="6" fill="currentColor" />

        <line
          id="ray"
          stroke="currentColor"
          stroke-width="2"
          stroke-linecap="round"
          x1="15"
          y1="1"
          x2="15"
          y2="4"
        ></line>

        <use href="#ray" transform="rotate(45 15 15)" />
        <use href="#ray" transform="rotate(90 15 15)" />
        <use href="#ray" transform="rotate(135 15 15)" />
        <use href="#ray" transform="rotate(180 15 15)" />
        <use href="#ray" transform="rotate(225 15 15)" />
        <use href="#ray" transform="rotate(270 15 15)" />
        <use href="#ray" transform="rotate(315 15 15)" />
      </svg>
      <svg width="30" height="30" id="dark-icon">
        <path
          fill="currentColor"
          d="
          M 23, 5
          A 12 12 0 1 0 23, 25
          A 12 12 0 0 1 23, 5"
        />
      </svg>
    </button>
  </body>
</html>

```

You can also unset the default appearance of the button element in CSS, except the cursor property. You should have that as pointer:

```css
. . .

button {
  all: unset;
  cursor: pointer;
}

. . .
```

Now, let's implement the event handler in JavaScript. First you need to access the SVG icons by ID:

```js
const lightIcon = document.getElementById("light-icon");
const darkIcon = document.getElementById("dark-icon");

. . .
```

Then, add the `dark-mode` class to the `body` element in case you are in dark mode and hide one of the SVG icons based on the `darkMode` variable. You detect dark mode as you did before:

```js
. . .

// Check if dark mode is preferred
const darkModeMediaQuery = window.matchMedia("(prefers-color-scheme: dark)");
let darkMode = darkModeMediaQuery.matches;

// Set dark-mode class on body if darkMode is true and pick icon
if (darkMode) {
  document.body.classList.add("dark-mode");
  darkIcon.setAttribute("display", "none");
} else {
  lightIcon.setAttribute("display", "none");
}

. . .
```

And finally,  can implement the function that flips the `darkMode` property. This function toggles the `dark-mode` class on the body element, and toggles the SVG icons:

```js
. . .

// Toggle dark mode on button click
function toggleDarkMode() {
  // Toggle darkMode variable
  darkMode = !darkMode;

  // Toggle dark-mode class on body
  document.body.classList.toggle("dark-mode");

  // Toggle light and dark icons
  if (darkMode) {
    lightIcon.setAttribute("display", "block");
    darkIcon.setAttribute("display", "none");
  } else {
    lightIcon.setAttribute("display", "none");
    darkIcon.setAttribute("display", "block");
  }
}
```

Now, this works: by default, you still have the setting from the OS or browser. But once you click this button, it will override this manually.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Screenshot-2024-03-07-at-12.31.42.png)
_Final look in light mode_

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Screenshot-2024-03-07-at-12.31.27.png)
_Final look in dark mode_

## Next Steps

With all this in place, you have a functionality that takes the dark mode setting from the browser or the OS by default, and you can override it with a nice-looking toggle button. In the [YouTube version of this tutorial](https://youtu.be/GUSUA72t7p0), you can also learn how to use `localStorage` to save this setting for the next session.

If you want to learn more about SVGs, check out [SVG-tutorial.com](https://svg-tutorial.com/), where you can learn more about SVGs from beginner to advanced levels with many great examples.

If you want to use this behavior in a game, check out the [Gorillas JavaScript game tutorial](https://www.freecodecamp.org/news/gorillas-game-in-javascript/), where we build the entire game from scratch. It's a massive two-hour tutorial that covers drawing on a Canvas element with JavaScript and the whole game logic with plain JavaScript.

%[https://youtu.be/2q5EufbUEQk?si=MIWVN_3MlFlKRC_G]

Subscribe to my channel for more JavaScript game development tutorials:

%[https://www.youtube.com/channel/UCxhgW0Q5XLvIoXHAfQXg9oQ]

  


  

