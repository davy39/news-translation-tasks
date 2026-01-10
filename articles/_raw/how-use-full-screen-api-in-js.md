---
title: How to use the Fullscreen API in JavaScript
subtitle: ''
author: Hunor Márton Borbély
co_authors: []
series: null
date: '2024-02-22T14:17:32.000Z'
originalURL: https://freecodecamp.org/news/how-use-full-screen-api-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/Untitled.022.png
tags:
- name: Fullscreen API
  slug: fullscreen-api
- name: canvas
  slug: canvas
- name: JavaScript
  slug: javascript
- name: SVG
  slug: svg
seo_title: null
seo_desc: 'How do you run a game created for the web in fullscreen? In this quick
  tutorial, you''ll see how to display a game or any other HTML element in fullscreen,
  how to exit fullscreen, and how to make a nice fullscreen toggle button in SVG.

  Recently I publ...'
---

How do you run a game created for the web in fullscreen? In this quick tutorial, you'll see how to display a game or any other HTML element in fullscreen, how to exit fullscreen, and how to make a nice fullscreen toggle button in SVG.

Recently I published a long [JavaScript game tutorial](https://www.freecodecamp.org/news/how-to-draw-a-gorilla-with-javascript-on-html-canvas/). While it was a very packed guide, there were still a few things we could not cover in it: how to display the game in fullscreen.

When you watch a video on YouTube, you have the option to also watch it on fullscreen. But did you know that the fullscreen feature isn't only for video elements?

In JavaScript, there’s a [Fullscreen API](https://developer.mozilla.org/en-US/docs/Web/API/Fullscreen_API). And it’s surprisingly simple to use. Here's a quick demo of what we're about to implement. Let's see how it works.

%[https://codepen.io/HunorMarton/pen/QWoRLXM]

You can also [watch this article as a video](https://www.youtube.com/watch?v=jX3mIQdQQ2w&t=15s) on YouTube.

## Table of Contents:

* [How to Enter Fullscreen Mode](#heading-how-to-enter-fullscreen-mode)
* [How to Style the Fullscreen](#heading-how-to-style-the-fullscreen)
* [How to Display Games with the Canvas Element in Fullscreen](#heading-how-to-display-games-with-the-canvas-element-in-fullscreen)
* [How to Exit Fullscreen](#heading-how-to-exit-fullscreen)
* [How to Code a Fullscreen Icon with SVG](#heading-how-to-code-a-fullscreen-icon-with-svg)
* [Learn More](#heading-learn-more)

## How to Enter Fullscreen Mode

Let’s say we have a simple website with some text. And at the bottom, we have a button that will display the text in full screen. We are going to refine the look of this button, but first, let’s get work on the main logic.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-21-at-18.20.51.png)
_A simple website with some text and a Toggle Fullscreen button_

```css
body {
  font-family: Montserrat;
  margin: 50px;
  max-width: 500px;
}
```

In the code above, we attached an event handler to the button in HTML. We can then implement the `toggleFullscreen` function logic in JavaScript.

In this function, all we have to do is call the `requestFullScreen` method on the `document`’s `documentElement` property. And that’s it:

```js
function toggleFullscreen() {
  document.documentElement.requestFullscreen();
}
```

If you click the button, your website will pop into fullscreen.

## How to Style the Fullscreen

Before we cover how to exit full screen and create a nice-looking toggle button, let’s see a few other things.

What you might notice right away is that, with more space, your content might get a bit lost on a full screen. Make sure you have a responsive styling that looks good on every screen size.

You can even style the layout specifically for fullscreen. In CSS you can set a media query that only applies the styling in case the `display-mode` is `fullscreen`. 

For instance, you can change the font-size, or change the `background-color` to have a distinct look on full screen.

```css
@media (display-mode: fullscreen) {
  body {
    background-color: #f9bb86;
    font-size: 1.2em;
  }
}
```

## How to Display Games with the Canvas Element in Fullscreen

In this case, we want to make a game that uses the `canvas` element to be fullscreen – like the [Gorillas](https://www.freecodecamp.org/news/how-to-draw-a-gorilla-with-javascript-on-html-canvas/) game – we also need to resize the `canvas` element to fit the whole screen.

In this case, we can use the `windows`’s `resize` event. The event is triggered both when we simply resize the browser window, and when we enter or exit fullscreen mode. 

With the `resize` event, we can resize the `canvas` element to fit the whole screen, update the scaling, adjust any other properties we need to change on resize and redraw the whole scene.

```js
window.addEventListener("resize", () => {
  // Resize canvas element
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;

  // Update scaling
  // . . .

  // Adjust size dependent properties
  // . . .

  // Redraw canvas
  draw();
});
```

If you check the source code of the [Gorillas game on CodePen](https://codepen.io/HunorMarton/pen/jOJZqvp), you'll find similar steps.

## How to Exit Fullscreen

Now that we know how to enter full screen, how do we exit from it?

By default, if you press the `Escape` key, the browser switches back to the normal view. In Google Chrome, you even get a notification at the top of the screen about this when you enter fullscreen mode.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-21-at-17.47.03-2.png)
_Google Chrome shows a notification on top of the screen once you enter full screen_

What if you want to exit fullscreen mode when you click the HTML button? Let’s change our button’s behavior to toggle fullscreen on or off.

```js
function toggleFullscreen() {
  if (!document.fullscreenElement) {
    document.documentElement.requestFullscreen();
  } else {
    document.exitFullscreen();
  }
}
```

First, we start by checking if we are in fullscreen mode already. We can do this by checking the `document`’s `fullscreenElement` property. If it is undefined, then we enter fullscreen mode the same way we did before. And if we are already in fullscreen mode, then we can exit by calling the document’s `exitFullscreen` method. 

It is really that simple. With a few lines of code, we can implement the logic for a fullscreen toggle button.

## How to Code a Fullscreen Icon with SVG

If you follow [my tutorials](https://www.freecodecamp.org/news/author/hunor/), you know I love creative coding, and [drawing from code](https://www.freecodecamp.org/news/svg-tutorial-learn-to-code-images/). So let’s update the look of our button, to make it look similar to what we have on YouTube.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-21-at-18.06.07.png)
_Fullscreen icon_

Let’s create an SVG image within our button. If you check the source code of YouTube, you will see that they also use an SVG.

Let’s define an SVG element within HTML. We'll set its size to 30 x 30 and define a `path` element:

```html
. . .

<button onclick="toggleFullscreen()">
  <svg width="30" height="30">
    <path
      stroke="black"
      stroke-width="3"
      fill="none"
      d="
        M 10, 2 L 2,2 L 2, 10
        M 20, 2 L 28,2 L 28, 10
        M 28, 20 L 28,28 L 20, 28
        M 10, 28 L 2,28 L 2, 20"
    />
  </svg>
</button>

. . .
```

To style the path, we set its color with the `stroke` property, set its `stroke-width`, and made sure that we didn't end up with a filled shape. SVG paths by default are filled, so we need to set explicitly that we don’t want to `fill` this shape.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-21-at-18.02.10.png)
_Using the move-to and line-to commands within an SVG path_

Then we defined the path with a few move-to and line-to commands. We can set these commands as a string in the `d` attribute of the path element.

We started with a move-to command: `M 10, 2`. The letter `M` signifies that we have a move-to command, and the 10 and 2 are the `x` and `y` coordinates of this command. We moved to the start of one of the four lines.

Then we continued the path with a line-to command that moves to the corner, and then with another line-to command. The line-to command works in a similar way. It starts with the letter `L`, then we set an `x, y` coordinates where the line should go to.

Then we did the same with the other corners. We move to the next line segment with another move-to command and draw a line with two more line-to commands.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Untitled.021.png)
_Drawing a path on a Canvas element with JavaScript has some similarities to defining a path in SVG_

**Note**: If you read my [previous tutorial](https://www.freecodecamp.org/news/how-to-draw-a-gorilla-with-javascript-on-html-canvas/) on how to make the gorillas game, then you might have noticed that we had something similar there. We also drew paths with move to and line to. Except that there we were drawn on a `canvas` element with JavaScript, and now we have the commands as a string within the HTML file.

### How to Toggle the Icon's Appearance

Now the SVG is looking great, but what if we want to have a different look when we are in fullscreen mode? On YouTube, when we enter fullscreen mode, the button switches to a different icon.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-21-at-18.06.33.png)
_The two faces of the fullscreen icon_

You can do this in different ways. The easiest way is probably to define another path, within the same SVG element with a different look. Then make this path transparent by default. We are going to toggle the visibility of these two paths in JavaScript.

```html
. . .

<button onclick="toggleFullscreen()">
  <svg width="30" height="30">
    <path
      id="enter-fullscreen"
      stroke="black"
      stroke-width="3"
      fill="none"
      d="
        M 10, 2 L 2,2 L 2, 10
        M 20, 2 L 28,2 L 28, 10
        M 28, 20 L 28,28 L 20, 28
        M 10, 28 L 2,28 L 2, 20"
    />
    <path
      id="exit-fullscreen"
      stroke="transparent"
      stroke-width="3"
      fill="none"
      d="
        M 10, 2 L 10,10 L 2, 10
        M 20, 2 L 20,10 L 28, 10
        M 28, 20 L 20,20 L 20, 28
        M 10, 28 L 10,20 L 2, 20"
    />
  </svg>
</button>

. . .
```

This second path is very similar to the previous one. Except that we used different coordinates for some of the line-to commands.

Then we set unique IDs for both of these paths, and we update our toggle function in JavaScript. In JavaScript, we get a reference to these paths by ID, and then in the toggle button’s event handler, we can switch the visibility of these elements back and forth.

```js
const enterFullscreen = document.getElementById("enter-fullscreen");
const exitFullscreen = document.getElementById("exit-fullscreen");

function toggleFullscreen() {
  if (!document.fullscreenElement) {
    document.documentElement.requestFullscreen();
    enterFullscreen.setAttribute("stroke", "transparent");
    exitFullscreen.setAttribute("stroke", "black");
  } else {
    document.exitFullscreen();
    enterFullscreen.setAttribute("stroke", "black");
    exitFullscreen.setAttribute("stroke", "transparent");
  }
}
```

Now if you click this button, it toggles the fullscreen mode and changes its own appearance.

## Learn More

If you want to learn more about SVGs, check out [SVG-Tutorial.com](http://SVG-Tutorial.com) where you can find a lot of examples from the basics to more advanced levels. It’s a free site and you can also find the example that we discussed in this article.

To use the button to run a JavaScript game in full screen, check out the whole JavaScript Game Tutorial on how to remake the classic Gorillas game here on [freeCodeCamp](https://www.freecodecamp.org/news/how-to-draw-a-gorilla-with-javascript-on-html-canvas/) or on [YouTube](https://www.youtube.com/watch?v=2q5EufbUEQk&t=2337s). It’s a massive tutorial that covers things from drawing on an HTML Canvas element, to the entire game logic, from event handling, through the animation loop, hit detection, and even AI logic, for the enemy gorilla.

%[https://www.youtube.com/watch?v=2q5EufbUEQk&t=2337s]

You can subscribe to my channel for more JavaScript game development tutorials:

%[https://www.youtube.com/channel/UCxhgW0Q5XLvIoXHAfQXg9oQ]


