---
title: 'An introduction to Generative Art: what it is, and how you make it'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-03T15:04:17.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-generative-art-what-it-is-and-how-you-make-it-b0b363b50a70
coverImage: https://cdn-media-1.freecodecamp.org/images/0*JPekOSiNoJpvFeDP.png
tags:
- name: Art
  slug: art
- name: creativity
  slug: creativity
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Ali Spittel

  Generative art can be an intimidating topic — it seems like there is a lot of math
  involved, and art is tricky in itself!

  But, it doesn’t have to be difficult — you can build some really cool things without
  a math or art degree. This p...'
---

By Ali Spittel

Generative art can be an intimidating topic — it seems like there is a lot of math involved, and art is tricky in itself!

But, it doesn’t have to be difficult — you can build some really cool things without a math or art degree. This post will break down what generative art even is and how you can get started building your own generative art.

### First, what is code art?

Code art is any art that is built using code. There are endless examples on CodePen — for example [CSS art](https://dev.to/aspittel/learning-css-through-creating-art-54c0).

### What is generative art?

Often, generative art draws inspiration from modern art, especially pop art that makes heavy use of orderly geometric patterns.

However, it is a very broad and rich category of art created with code with a central characteristic. Generative art incorporates a self-governed or autonomous system in some way.

Randomness is one type of autonomous system. By incorporating chance into a piece of code art, you get a different, completely unique piece of art each time you run your script, load your page, or respond to some user interaction.

There are also more orderly autonomous systems. One example is Mandelbrot’s Fractal, derived from a deceptively simple equation.

We can also integrate both approaches, blending order and chaos!

The artwork becomes a collaboration between the computer and the artist. Some aspects of the artwork are controlled by the coder, but not all of them. The artist controls both the randomness and the order in the art.

In a way, with an autonomous system, the artist gives up control over their art, and the computer is doing it for them. A more nuanced perspective emerges when a new creative process is considered.

The coder-artist engages in a feedback loop where they are constantly tweaking a system to produce more desirable and often more surprising results.

This process embraces experimentation and happy accidents in a way that reshapes the role of the artist. As generative artists, we use the code basics like loops, control flow and specialized functions. We then blend them with often unpredictable forces, to produce completely unique results unlike anything else that exists.

### Examples of Generative Art

[Kate Compton’s Flowers](http://www.galaxykate.com/apps/Prototypes/LTrees/)

[Cellular Automata and the Edge of Chaos](http://math.hws.edu/eck/js/edge-of-chaos/CA.html)

#### Animated generative art in multi-colour by Phil Nash

#### Impressionists Blobs by Murasaki Uma

#### Generated Tree by Miriam Nadler

### What goes into a piece of generative art?

* **Randomness** is crucial for creating generative art. The art should be different each time you run the generation script, so randomness is usually a large part of that.
* **Algorithms** — Implementing an algorithm visually can often generate awesome art, for example, the binary tree above.
* **Geometry** — Most generative art incorporates shapes, and the math from high school geometry class can aid in some really cool effects.

### How can you approach a generative art piece?

There are two main strategies for creating generative art, though most will fall between the two strategies.

The first is to have no results in mind and see what the computer generates as you play around.

The second is that you have a very finalized idea of what you want the art to look like, and the randomness only slightly changes the end result.

### Where should you start?

If you know JavaScript, [p5.js](https://p5js.org/) is an awesome place to start. Its goal is to “make coding accessible for artists, designers, educators, and beginners.” It is a wrapper on the [Canvas API](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API), and it simplifies a lot of the math. It focuses on drawing, but you can also do sound, video, or webcam interaction with it if you are interested in those forms of art!

#### A Quick Introduction to P5

First, load in the [p5 CDN](https://cdnjs.cloudflare.com/ajax/libs/p5.js/0.7.2/p5.js). Then, in your JavaScript file, you will add two functions that will be used in pretty much ever p5 script: `setup` and `draw`. These names are necessary for p5 to call them.

`setup` is called when the program starts. You will probably create a canvas to draw on within it using the `createCanvas` function, and you may set some defaults there. It is only called once!

`draw` is called after setup, and is executed constantly until you call `noLoop`, which will stop it from running again. You can control how many times `draw` runs each second with the `frameRate` function.

With generative art, I usually put `noLoop` in the `setup` function, which makes `draw` only run once instead of continuously.

[Here’s a p5 starter template on CodePen](https://codepen.io/aspittel/pen/EeJJBm).

Since we’ve talked so much about the importance of randomness for generative art, another important function in p5 is `random`. It works similarly to JavaScript's `Math.random` but you can set a range for the numbers so that you don't have to do as much math to get the number to a useful format.

#### p5 Lines

You can create a line in p5.js like this:

```
line(startX, startY, endX, endY)
```

Then, you can randomly generate a bunch of lines and create a simple piece of generative art like this:

Even really simple scripts can generate cool pieces of art!

#### p5 Shapes

You can also create shapes with p5 — like circles, triangles, and squares.

Here’s an example of creating some shapes with p5:

```
// circle ellipse(xCoordinate, yCoordinate, width, height) 
```

```
// square rect(xCoordinate, yCoordinate, width, height) 
```

```
// triangle triangle(xCoordinate1, yCoordinate1, x2, y2, x3, y3)
```

Then, we can create some more shapes to build something more fun!

#### p5 Movement

We can add movement to our drawings by removing the `noLoop` function call in the `setup` function — check this out!

#### Color

You can also play with color with generative art by randomly choosing colors. You can do this mathematically through RGB values, or you can generate a color palette with your favorite color picker (we’ve been using [this](https://www.colorbox.io/) one).

You can set the fill color with the `color` function. It takes a bunch of different formats, like named colors, RGBAs, and hex codes.

You can also change the color of the outline using `stroke`. You can also remove that outline using `noStroke` or make it a different width with `strokeWeight`.

#### Putting it all together

Once we have all of those pieces in place, we can combine the techniques to build some really cool stuff.

### Another Strategy: Tweaking Tutorials

You can also generate really cool generative art by taking someone else’s work and building off of it. For example, here’s the result of a tutorial by [Dan Shiffman](https://www.youtube.com/channel/UCvjgXvBlbQiydffZU7m1_aw):

Here are two tweaks of it to create different effects:

[Here’s](https://codepen.io/collection/nMmoem/) a Codepen Collection with even more!

You can follow tutorials, fork CodePens, or Glitch projects and create something new and unique. Just make sure to give the original artist some credit too.

### Cheatsheet

Here’s a cheat sheet with all of the P5 functionality we used for this tutorial.

![Image](https://cdn-media-1.freecodecamp.org/images/0*hFfffK_1TdH8MOJf.png)

### Read More

* [Generative Artistry](https://generativeartistry.com/)
* [Coding Train](https://www.youtube.com/channel/UCvjgXvBlbQiydffZU7m1_aw)
* [Talk by Tim Holman](https://www.youtube.com/watch?v=4Se0_w0ISYk)

### Keep in Touch

This post was co-written with [James Reichard](https://twitter.com/1800thehive). If you create your own art, make sure to Tweet it at us! ([Ali](https://twitter.com/ASpittel) and [James](https://twitter.com/1800THEHIVE)).

_Originally published at [dev.to](https://dev.to/aspittel/intro-to-generative-art-2hi7)._

