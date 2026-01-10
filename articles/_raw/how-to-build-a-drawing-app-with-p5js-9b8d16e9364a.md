---
title: How to build a drawing app with p5js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-15T15:53:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-drawing-app-with-p5js-9b8d16e9364a
coverImage: https://cdn-media-1.freecodecamp.org/images/0*YgE7CTX63DNOO6P6.png
tags:
- name: coding
  slug: coding
- name: creativity
  slug: creativity
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Florin Pop

  The theme for week #5 of the Weekly Coding Challenge is:

  Creating a Drawing Application

  This is the first application that we are building in the #weeklyCodingChallenge
  program. So far we have built smaller projects, so this is pretty e...'
---

By Florin Pop

The **theme** for week #5 of the [Weekly Coding Challenge](https://www.florin-pop.com/blog/2019/03/weekly-coding-challenge/) is:

### Creating a Drawing Application

This is the first application that we are building in the #weeklyCodingChallenge program. So far we have built smaller projects, so this is pretty exciting if you ask me! ?

In this article we’ll use p5js, a drawing library, to build a [Drawing Application](https://codepen.io/FlorinPop17/full/VNYyZQ):

Check out the CodePen here:

%[https://codepen.io/FlorinPop17/pen/VNYyZQ]

If you want to learn more about p5js and what it does, you can visit their [official website](http://p5js.org/). Basically, I am using it because it works very well on top of the browser’s [canvas](https://www.w3schools.com/html/html5_canvas.asp) element by providing a clear API.

### The HTML

As you can notice in the example above, on the left side of the screen we have a `.sidebar`. We'll put inside it our 'tools' - a `color` picker, a `weight` selector and the `clear` button (trashcan icon):

```html
<div class="sidebar">
    <ul>
        <li>
            <label for="color">Color:</label>
            <input type="color" id="color" />
        </li>
        <li>
            <label for="weight">Stroke:</label>
            <input type="number" id="weight" min="2" max="200" value="3" />
        </li>
        <li>
            <button id="clear"><i class="fa fa-trash"></i></button>
        </li>
    </ul>
</div>
```

### The CSS

Using CSS we’ll move the `.sidebar` and everything that’s inside it in the left side. We will style it a little bit to make it look nicer (nothing fancy, basic CSS):

```css
.sidebar {
    background-color: #333;
    box-shadow: 0px 0px 10px rgba(30, 30, 30, 0.7);
    color: #fff;
    position: absolute;
    left: 0;
    top: 0;
    height: 100vh;
    padding: 5px;
    z-index: 1000;
}

.sidebar ul {
    display: flex;
    justify-content: center;
    align-items: flex-start;
    flex-direction: column;
    list-style-type: none;
    padding: 0;
    margin: 0;
    height: 100%;
}

.sidebar ul li {
    padding: 5px 0;
}

.sidebar input,
.sidebar button {
    text-align: center;
    width: 45px;
}

.sidebar li:last-of-type {
    margin-top: auto;
}

.sidebar button {
    background-color: transparent;
    border: none;
    color: #fff;
    font-size: 20px;
}

.sidebar label {
    display: block;
    font-size: 12px;
    margin-bottom: 3px;
}
```

Now for the **important** part…

### The JS / P5JS

As you might have noticed, we haven’t added a `canvas` element into our HTML since p5js will create it for us.

There are two important functions which we’ll use from the [p5js](http://p5js.org/) library:

* [setup](http://p5js.org/reference/#/p5/setup) — is called once when the program starts. It’s used to define initial environment properties such as screen size and background color.
* [draw](http://p5js.org/reference/#/p5/draw) —is called directly after `setup()`. The `draw()` function continuously executes the lines of code contained inside its block.

```js
function setup() {
    // create a canvas which is full width and height
    createCanvas(window.innerWidth, window.innerHeight);

    // Add a white background to the canvas
    background(255);
}

function draw() {}
```

Before moving forward, let’s stop for a moment and see what we want to achieve.

So, basically, we want to add a `mousepressed` eventListener to the `canvas` that will start 'drawing' a shape inside it as long as the `mouseIsPressed`.

We’ll create an array of points which we’re going to use to create a `path` (or a shape) using the [beginShape](http://p5js.org/reference/#/p5/beginShape) and [endShape](http://p5js.org/reference/#/p5/endShape) methods to draw this shape inside the canvas. The shape is going to be constructed by connecting a series of vertices (see [vertex](http://p5js.org/reference/#/p5/vertex) for more information).

As we want this shape to be _re-drawn_ every time, we’ll put this code inside the `draw` method:

```js
const path = [];

function draw() {
    // disabled filling geometry - p5js function
    noFill();

    if (mouseIsPressed) {
        // Store the location of the mouse
        const point = {
            x: mouseX,
            y: mouseY
        };
        path.push(point);
    }

    beginShape();
    path.forEach(point => {
        // create a vertex at the specified location
        vertex(point.x, point.y);
    });
    endShape();
}
```

As you can see, p5js has a [mouseIsPressed](http://p5js.org/reference/#/p5/mouseIsPressed) flag that we can use to detect when the mouse buttons are pressed.

Everything might look good so far, but there is a **big** issue. Once the mouse button is released and we try to draw another shape, the last point from the previous shape will be connected to the first point of the new shape. This is definitely not what we want, so we need to change our approach a little bit.

Instead of having one array of points (the path array), we’ll create a `pathsarray` and we are going to store all the `paths` inside it. Basically, we’ll have a double array with points. Also, for this, we will need to keep track of the `currentPath` while the mouse is still pressed. We’ll reset this array once the mouse button is pressed again. Confusing? ? Let’s see the code and I bet that it will become clearer:

```js
const paths = [];
let currentPath = [];

function draw() {
    noFill();

    if (mouseIsPressed) {
        const point = {
            x: mouseX,
            y: mouseY
        };
        // Adding the point to the `currentPath` array
        currentPath.push(point);
    }

    // Looping over all the paths and drawing all the points inside them
    paths.forEach(path => {
        beginShape();
        path.forEach(point => {
            stroke(point.color);
            strokeWeight(point.weight);
            vertex(point.x, point.y);
        });
        endShape();
    });
}

// When the mouse is pressed, this even will fire
function mousePressed() {
    // Clean up the currentPath
    currentPath = [];

    // Push the path inside the `paths` array
    paths.push(currentPath);
}
```

I also added some comments in the code above, make sure you check them out.

The [mousePressed](http://p5js.org/reference/#/p5/mousePressed) _function is called once after every time a mouse button is pressed_ — p5js stuff! ?

Great! Now we can draw individual shapes in our canvas! ?

The last thing to do is to _hook_ up those buttons that we created in the HTML and use the values that are inside them to style the shape:

```js
const colorInput = document.getElementById('color');
const weight = document.getElementById('weight');
const clear = document.getElementById('clear');

function draw() {
    noFill();

    if (mouseIsPressed) {
        const point = {
            x: mouseX,
            y: mouseY,
            // storing the color and weights provided by the inputs for each point
            color: colorInput.value,
            weight: weight.value
        };
        currentPath.push(point);
    }

    paths.forEach(path => {
        beginShape();
        path.forEach(point => {
            // using the color and the weight to style the stroke
            stroke(point.color);
            strokeWeight(point.weight);
            vertex(point.x, point.y);
        });
        endShape();
    });
}

clear.addEventListener('click', () => {
    // Remove all the paths
    paths.splice(0);

    // Clear the background
    background(255);
});
```

And with this, we have finished our little application! Yay! ?

### The entire JS code

```js
const colorInput = document.getElementById('color');
const weight = document.getElementById('weight');
const clear = document.getElementById('clear');
const paths = [];
let currentPath = [];

function setup() {
    createCanvas(window.innerWidth, window.innerHeight);
    background(255);
}

function draw() {
    noFill();

    if (mouseIsPressed) {
        const point = {
            x: mouseX,
            y: mouseY,
            color: colorInput.value,
            weight: weight.value
        };
        currentPath.push(point);
    }

    paths.forEach(path => {
        beginShape();
        path.forEach(point => {
            stroke(point.color);
            strokeWeight(point.weight);
            vertex(point.x, point.y);
        });
        endShape();
    });
}

function mousePressed() {
    currentPath = [];
    paths.push(currentPath);
}

clear.addEventListener('click', () => {
    paths.splice(0);
    background(255);
});
```

Also, make sure that you import the `p5js` file in your html too before importing this `js` file.

### Conclusion

I hope that you liked this drawing app that we’ve built. There are a bunch of functionalities that could be added to this app and I challenge you to let your creative mind to come up with new ideas! ?

What if you could save the drawing as an image (`.png` or `.jpg`)? ? (you can do this with the p5js library).

As of now, we are only checking the `mouse` events. Maybe you could make it work on mobile, too, by figuring out the `touch` events? The sky is the limit with the amount of functionalities that could be added to this app!

I’d love to see what you are going to build! Tweet me [@florinpop1705](https://twitter.com/florinpop1705) with your creation!

You might also like one of the other challenges from the Weekly Coding Challenge program. Check them out [here](https://www.florin-pop.com/blog/2019/03/weekly-coding-challenge/).

See ya next time! Happy Coding! ?

_Originally published at [www.florin-pop.com](https://www.florin-pop.com/blog/2019/04/drawing-app-built-with-p5js/)._

