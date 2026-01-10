---
title: Spend your Sunday (or any day) with the canvas element and JavaScript.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-02T00:50:57.000Z'
originalURL: https://freecodecamp.org/news/sunday-with-canvas-element-and-javascript-38ae80e0fbeb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1d6oMjjsNM4QrprjTxb87w.png
tags:
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Ashish Nandan Singh

  Recently during the JavaScript30 days challenge, I had the chance to get my hands
  dirty with the HTML inbuilt canvas property. What convinced me to write about the
  entire experience was the relative comfort level and learning c...'
---

By Ashish Nandan Singh

Recently during the JavaScript30 days challenge, I had the chance to get my hands dirty with the HTML inbuilt canvas property. What convinced me to write about the entire experience was the relative comfort level and learning curve.

In its simplest form, HTML canvas element enables a web developer to draw graphics on a web page, through javaScript, and this very aspect makes this HTML element far more interesting.

The **<canva**s> element is just a container — you would always use JavaScript to actually draw the graphics. One may argue that we can always have the points added or maybe an SVG for that matter, but again — what fun would that be? :D

Coming back to the **<canva**s> element: a canvas is a rectangular area on an HTML page. By default, a canvas has no border and no content.

The markup looks like this:

> <canvas id=”canvas” width=”200" height=”100"></canvas>

#### The beginning

Alright so much for the introduction. Let’s focus on building something fun using some plain old JavaScript, (not so old — ES6!). First, we’ll take a look at the starter files.

Let’s break it down. We have a stylesheet named **style.css.** Then we go about defining a **canvas** element with 800 width and 800 height. Lastly, we have a **script** tag named **app.js** where all the magic happens. On that note, lets start doing stuff with our very own app.js.

* We start with selecting the canvas element in the first line and store the value in a const variable named **canvas** for simplicity.
* Then we capture the context of the same canvas in 2D aspect and set it to the **variable.**
* Set the width and height of the canvas to be the inner width of window and height respectively.

Now that we finally have our canvas in place, we move on to defining the most basic attributes of the canvas.

* **ctx.strokeStyle** sets or returns the color, gradient, or pattern used for strokes. Yes, you read it right: the default color looks #BADASS.
* **ctx.lineWidth s**ets or returns the current line width. We set it to 1, and we will come to this later on.
* **ctx.lineJoin s**ets or returns the type of corner created when two lines meet. We set it to round so that when two lines meet, we have a neat connection point.
* **ctx.lineCap** sets or returns the style of the end caps for a line. We set it to round so that when we don’t meet any other line, we still end up getting that same neat pipe figure depending on the width of stroke defined earlier.

Now that we have all these pieces in place, let’s see how we can go about actually drawing on the canvas.

First, we need to add some event listeners for the mouse movement on canvas, and then trigger a function that would actually draw something on the canvas. Let’s take a look at the additions we may have in the app.js file.

Let’s break this down:

* We start by defining a variable called **isDrwaing** which would help us figure out if the user is actually trying to draw on the canvas or not. We’ll come back to this later on.
* For now, let’s have a function called **draw** which will be triggered and later on will be responsible for the whole action.
* Lastly, we add a bunch for event listeners for various events just to make sure we capture the right events and only execute the **draw** function when it’s needed.

By declaring the **isDrawing** variable and setting its property to **false,** we set the **initial state** of the canvas as soon as the canvas element is loaded as not drawing. Then in every subsequent event listener, we use an **inline function** and change the value of the **isDrawing** function every time according to the type of event fired.

At the start of the draw function, if the value of **isDrawing** is set to false, the function gets called off after encountering the return statement. If **isDrawing** is set to true, the draw function gets executed.

#### Draw Function

Let’s expand on that draw function:

* We start by defining two variables globally, **lastX, lastY,** and set the initial value to be 0.
* If you go to the console of your browser now, you’ll see that you have an enormous log of all the mouse movements you have been making. This **MouseEvent** object has some very important and useful properties:

![Image](https://cdn-media-1.freecodecamp.org/images/1*OUcCcMG5ljNwh1aJPqsHSA.png)
_MouseEvent object_

We are only interested in the offsetX and offsetY property of this object.

* With the very **ctx.beginPath,** we begin a path, or reset a current path. Both of which we want we do for every event triggered.
* **ctx.moveTo** moves the path to the specified point in the canvas, without creating a line. In our case this would be the lastX and lastY defined outside the function at global scope.
* **ctx.lineTo** adds a new point and creates a line to that point from the last specified point in the canvas.
* **ctx.stroke()** actually draws the path you have defined — the real hard worker, guys!

Inside the **ctx.lineTo,** we have leveraged the event property **offsetX** and **offsetY** to get the latest point of X and Y in the canvas only to draw a line with **ctx.lineTo.**

We have pretty much everything in place. Every mouse event on the webpage draws a line on the canvas — but with some trouble and not much swag. So lets add some swag.

#### Swag!

For now, all the lines are drawn from the 0 and 0 point in canvas. We set this as the initial set of points to start drawing from when we load the canvas or even when we execute the draw function.

Let’s fix this to have a better real time experience. If you think about it, the answer is very simple: every time the draw function is executed, we want the initial point to always be the **offsetX** and **offsetY** property of the **MouseEvent object**.

By using ES6 array destructuring, we can reset the values of lastX and lastY to be the offsetX and offsetY property of the MouseEvent object. We can do this at the very end of the draw function. Lets take a look at the app.js file after adding some swag in it.

* As soon as the **mousemove** event occurs, we fire the draw function. Then we go ahead and set the value of lastX and lastY in the draw function using ES6 destructuring.
* In the case of a **mousedown** event, first we change the inline function to block, as you can see, and then we again set the lastX and lastY values to be the event’s offset property. This is to make sure we have the line visible to us on the canvas while we are moving from one point to another point in canvas.

Let’s make it colorful and add some dynamics in the stroke.

HOLY MOLY!!

That is lot to handle, but let’s break it down.

* I defined a new variable called **hue** and set its property to 0.
* If you don’t already know about hue and why is it awesome, head over to Google and give it a try, or just [click here](http://mothereffinghsl.com/).

In its simplest form, hsl lets us use the same rainbow of colors ranging between 0 and 360. Each number has a lightness and alpha value. Defining hsl looks something like this: hsl(173, 99%, 50%). Here number 173 represents a color — 99% is the lightness and 50% is the alpha value.

Again, by using some awesome ES6 backticks, we can leverage the hsl and influence it by doing something like this:

`ctx.strokeStyle = `hsl(${hue}, 100%, 50%)``

as we did on the line 7 in the above gist.

Next we increase the value of the **hue** variable which changes the color of the stroke with every **mousemove** event. Once the hue value has been incremented until 360, we reset the value of hue to be 0 on line 14 of the above gist. But even if we don’t do this, we will still have the same result. Even so, let’s just do the right thing. :D lol

`if(hue>360){`  
 `hue =`0   
 }

Next, let’s add some dynamics to the width of the stroke being drawn every time, like this:

`if(ctx.lineWidth>=75 || ctx.lineWidth<=1){`  
 `direction = !direct`ion;  
}

`if(direction){`  
 `ctx.lineWidth++`  
`} else {`  
 `ctx.lineWidth = 0`  
`}`

All we did here is first check if the current **lineWidth** is bigger than 75 or less than 1. If it is, then we reverse the value of the variable **direction** which is set to true as default.

Next we check if the value of the variable **direction** is true. If it is, then increment the value of lineWidth by 1, else reset the **lineWidth** to be 0.

That was not very much JavaScript. You should have your pretty canvas ready by now if you have been following along properly.

Let’s take a quick look at what the final file structure looks like. Since we only changed the app.js file, I’ll show you only that, as index.html remains almost unchanged since the beginning.

This is just the tip of the iceberg when thinking about the total power of the canvas element combined with JavaScript. I would encourage you to do a little more research and make the canvas look even better. Maybe add a couple of button’s to clear the screen, or maybe select a specific color to draw on canvas. So many options!

All I am saying is there are million ways to make this better. I’ll definitely update the story if I have anything worth updating.

Lastly, I’d like to leave you with a video of how the canvas would look like at the very end.

Hope you enjoyed reading all this! Any comments or suggestions to improve or discuss this further would really be appreciated. You can connect with me on [twitter](https://twitter.com/ashishnandansin) and [linkedIn](https://www.linkedin.com/in/ashish-nandan-singh-490987130/) as well.

