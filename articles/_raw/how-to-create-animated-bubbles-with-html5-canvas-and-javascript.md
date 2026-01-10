---
title: How to Create Animated Bubbles with HTML5 Canvas and JavaScript
subtitle: ''
author: Shruti Kapoor
co_authors: []
series: null
date: '2023-09-05T14:08:02.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-animated-bubbles-with-html5-canvas-and-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/shrutikapoor.dev--11-.jpg
tags:
- name: animation
  slug: animation
- name: HTML5
  slug: html5
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'Hello everyone! Welcome to this tutorial where we''re going to dive into
  the world of creating fun bubbles in code using HTML canvas and JavaScript. The
  best part? We''ll achieve all of this using just a touch of HTML and all JavaScript,
  no CSS.

  What w...'
---

  
Hello everyone! Welcome to this tutorial where we're going to dive into the world of creating fun bubbles in code using HTML canvas and JavaScript. The best part? We'll achieve all of this using just a touch of HTML and all JavaScript, no CSS.

## What we will learn

In this article, you're going to master the following concepts:

* How to create circles using the `arc` method of the canvas context.
* How to utilize the `requestAnimationFrame` function for smooth circle animations.
* How to harness the power of JavaScript classes to create multiple circles without repeating code.
* How to add stroke styles and fill styles to your circles for a 3D bubble effect.

You can follow along with me, or use [the final codepen](https://codepen.io/shrutikapoor08/pen/wvQXMVO) if you want to take a look at the source code.

If you prefer to learn in a video format, follow along this video:



%[https://www.youtube.com/watch?v=IjPgXP3gDyI&ab_channel=ShrutiKapoor]

## Getting Started

First things first, we need an HTML5 Canvas element. Canvas is a powerful element for creating shapes, images and graphics. This is what we'll use for creating the bubbles.

Let’s set it up:

```html
<canvas id="canvas"></canvas>

```

In order to do anything meaningful with canvas, we need to have access to it’s `context`. [Context](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D) provides an interface to render objects on the canvas and draw shapes.

Here's how to get access to canvas and it's context.

```js
const canvas = document.getElementById('canvas');
const context = canvas.getContext('2d');

```

We'll also set up our canvas to use the entire window height and width:

```js
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

```

Next, we'll give it canvas a nice soothing light blue background by adding some css. This is the only CSS we're going to use. You can also do this with JavaScript if you wish.

```css
#canvas {
  background: #00b4ff;
}

```

## How to Create Bubbles with Canvas

Let’s get to the fun part. We're going to create bubbles by clicking on the canvas. To achieve this, we'll start by creating a click event handler:

```js
canvas.addEventListener('click', handleDrawCircle);

```

Since we need to know where we clicked on our canvas, we are going to keep track of it in our `handleDrawCircle` function and use the event’s coordinates:

```js

//We are adding x and y here because we will need it later.
let x, y
const handleDrawCircle = (event) => {
  x = event.pageX;
  y = event.pageY;

  // Draw a bubble!
  drawCircle(x, y);
};

```

### How to Draw Circles Using the `arc` Method

To create circles, we're going to utilize the [`arc` method available on canvas’s context.](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/arc) The `arc` method accepts `x` and `y` (the center of the circle), a radius, and a start angle and end angle which for us will be `0` and `2* Math.PI` respectively because we're creating a full circle.

That is:

```js
const drawCircle = (x, y) => {
  context.beginPath();
  context.arc(x, y, 50, 0, 2 * Math.PI);

  context.strokeStyle = 'white';
  context.stroke();
};

```

![Drawing circles](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/1zrbq3gcpff40nbvzbt8.png)
_circles created using the arc method_

### How to Move Circles Using the `requestAnimationFrame` Method

Now that we have circles, let's make them move because...

![A scene from the "I like to move it" song from the movie -Madagascar](https://media.giphy.com/media/ptS6CV6Ty7Dt26k6wq/giphy.gif)

Remember that when we created a circle, we used the `arc` method which accepted `x` and `y` coordinates — the center of the circle. If we move the `x` and `y` coordinate of our circle really fast, it will give an impression that the circles are moving. Let’s try that!

```js
//Define a speed by which to increment to the x and y coordinates

const dx = Math.random() * 3;
const dy = Math.random() * 7;

//Incremenet the center of the circle with this speed
x = x + dx;
y = y - dy;

```

We can move this inside a function:

```js
let x, y;

const move = () => {
  const dx = Math.random() * 3;
  const dy = Math.random() * 7;

  x = x + dx;
  y = y - dy;
};

```

To give our circle a seamless movement, we're going to create an `animate` function and use the browser's `requestAnimationFrame` method to create a moving circle:

```js
const animate = () => {
  context.clearRect(0, 0, canvas.width, canvas.height);

  move();
	drawCircle(x,y);

  requestAnimationFrame(animate);
};

//Don't forget to call animate at the bottom 
animate();

```

![Circle animating](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/z01uy7e82sqia06svu5t.gif)
_moving circles created with requestAnimationFrame method_

### How to Create Particles Using a Particle Class

Now that we have created one circle, it’s time to create multiple circles! But before we do that, let's prepare our code.

In order to avoid repeating our code, we are going to use classes and introduce a `Particle` class. Particles are the building blocks of our dynamic artwork and animation. Each bubble is a particle with its own position, size, movement, and color attributes. Let's define a **`Particle`** class to encapsulate these properties:

```js
class Particle {
  constructor(x = 0, y = 0) {}

  draw() {
    // Drawing the particle as a colored circle
    // ...
  }

  move() {
    // Implementing particle movement
    // ...
  }
}

```

Let’s move some of the constants we had set up to the `Particle` class:

```js
class Particle {
  constructor(x = 0, y = 0) {
    this.x = x;
    this.y = y;
    this.radius = Math.random() * 50;
    this.dx = Math.random() * 3;
    this.dy = Math.random() * 7;
  }

  draw() {
    // Drawing the particle as a colored circle
    // ...
  }

  move() {
    // Implementing particle movement
    // ...
  }
}

```

The **`draw`** method will be responsible for rendering the particle on the canvas. We have already implemented this functionality in `drawCircle`, so let’s move it in our class and update the variables to be class variables:

```js
class Particle {
  constructor(x = 0, y = 0) {
    this.x = x;
    this.y = y;
    this.radius = Math.random() * 50;
    this.dx = Math.random() * 3;
    this.dy = Math.random() * 7;
    this.color = 'white';
  }

  draw() {
    context.beginPath();
    context.arc(this.x, this.y, this.radius, 0, 2 * Math.PI);
    context.strokeStyle = this.color;
    context.stroke();

    context.fillStyle = this.color;
    context.fill();
  }

  move() {}
}

```

Similarly, let’s move the `move` function within the class:

```js
move() {
	this.x = this.x + this.dx;
	this.y = this.y - this.dy;
}

```

Next, we need to make sure that we are calling the `Particle` class in our event handler:

```js
const handleDrawCircle = (event) => {
  const x = event.pageX;
  const y = event.pageY;

  const particle = new Particle(x, y);
};

canvas.addEventListener('click', handleDrawCircle);

```

Since we need to access this particle in our animate function in order to call the `move` method on it, we'll store this particle in an array called `particleArray`. This array will also be helpful when creating lots of particles. 

Here’s the updated code to reflect this:

```js
const particleArray = [];

const handleDrawCircle = (event) => {
  const x = event.pageX;
  const y = event.pageY;

  const particle = new Particle(x, y);
  particleArray.push(particle);
};

canvas.addEventListener('click', handleDrawCircle);

```

Remember to update the `animate` function too:

```javascript
const animate = () => {
	context.clearRect(0, 0, canvas.width, canvas.height);

	particleArray.forEach((particle) => {
		particle?.move();
		particle?.draw();
	});

	requestAnimationFrame(animate);
};
```

At this point, you will see these particles on your screen:

![Multiple circles moving](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/92rs6a5i1xn4v2gzdv8o.gif)

Awesome! Now, to the fun part! Let's creates lots of circles and style them to make them look like bubbles.

To create lots of bubbles, we are going to create particles using a `for` loop and add them to the `particleArray` we had created.

```js
const handleDrawCircle = (event) => {
  const x = event.pageX;
  const y = event.pageY;

  for (let i = 0; i < 50; i++) {
    const particle = new Particle(x, y);
    particleArray.push(particle);
  }
};

canvas.addEventListener('click', handleDrawCircle);

```

In the animate function, we'll continuously update the canvas by clearing it and redrawing the particles in their new positions. This will give an illusion of the circle moving:

```js
const animate = () => {
  context.clearRect(0, 0, canvas.width, canvas.height);

  particleArray.forEach((particle) => {
    particle?.move();
    particle?.draw();
  });

  requestAnimationFrame(animate);
};

animate();

```

![Multiple circles animating](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ya5u8w8qetqkcy2nbowe.gif)

Now that we have bubbles moving, it’s time to add color to them to make them look like actual bubbles!

We will do this by adding a gradient fill to the bubbles. This can be done using the `context.createRadialGradient` method:

```js
const gradient = context.createRadialGradient(
  this.x,
  this.y,
  1,
  this.x + 0.5,
  this.y + 0.5,
  this.radius
);

gradient.addColorStop(0.3, 'rgba(255, 255, 255, 0.3)');
gradient.addColorStop(0.95, '#e7feff');

context.fillStyle = gradient;

```

![Bubbles](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/l80yde62l9mw3ceh1f1i.gif)

[Here’s the final codepen](https://codepen.io/shrutikapoor08/pen/wvQXMVO) if you want to take a look at the source code.

## Wrap Up

Congratulations! You've just created something super fun using only HTML Canvas and JavaScript. You've learned how to use the `arc` method, how to leverage the `requestAnimationFrame` method, how to harness the power of JavaScript classes, and how to style your bubbles using gradients for the 3D bubble effect.

Feel free to experiment with colors, speeds, and sizes to make your animations truly unique.

I hope you had as much fun following this tutorial as I did creating it. Now, it's your turn to experiment. I would love to see if you tried this out and what you created. Share with me your code link and I would love to check it out.

---

And now a #DevJoke:

Question - Who won the debate for the best name for loop variable?

Answer - i won.

---

If you enjoyed this article, share it with someone who will benefit from it. 

If you are interested in articles like this and front-end articles on JavaScript, React, GraphQL or Accessibility and career advice from a Staff Engineer, [sign up for my newsletter](https://tinyletter.com/shrutikapoor) and get these directly in your inbox.

