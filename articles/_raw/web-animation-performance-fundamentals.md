---
title: Web Animation Performance Fundamentals – How to Make Your Pages Look Smooth
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-02-28T18:49:59.000Z'
originalURL: https://freecodecamp.org/news/web-animation-performance-fundamentals
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/Antics_2-D_Animation_infobox_screenshot-1.png
tags:
- name: animation
  slug: animation
- name: CSS
  slug: css
- name: web performance
  slug: web-performance
seo_title: null
seo_desc: "By Reza Lavarian\nWhat if I told you that web pages were interactive animations\
  \ played back by your web browser?\nWe watch various motions every time we're on\
  \ a web page. \nAnd it's not only JavaScript or CSS animations that I'm talking\
  \ about. Scrolling..."
---

By Reza Lavarian

What if I told you that web pages were interactive animations played back by your web browser?

We watch various motions every time we're on a web page. 

And it's not only JavaScript or CSS animations that I'm talking about. Scrolling, pinch zooming, text selection, and even hovering over a button are technically animations and work similarly.

In fact, they are sequential images displayed rapidly to give us a perception of motion or simply reflect a change.

Every time JavaScript code changes the page, an area in the previous image is invalidated, and the browser draws a new one.

These changes could be as simple as adding or removing a `<div>` element or changing the styles of a button. 

We refer to these images as **frames**.

[Based on W3C frame timing guidelines](https://www.w3.org/TR/frame-timing/#h-introduction), the web browser has to be able to display sixty frames per second (60 fps).

Of course, a frame stays on the screen if there's no change.

How about I show you some examples?

When you scroll through a page, the browser displays off-screen areas of the document as you scroll down (or up).

The image below shows the sequential frames produced and displayed during a few seconds of scrolling.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/animation-scroll-2.png)
_Generated frames during a few seconds of scrolling_

And as you can see, each frame was displayed for 16.7ms (60 fps). 

I used [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/) to create the above recording. You can reproduce it if you want. While in the DevTools, go to the **Performance** panel, and click on the record button. Then, scroll the page for a few seconds, and stop the recording.

You'll see an overview like the one above.

Even when you select a piece of text, new frames are displayed as you select more letters and lines.

In the recording below, I'm moving the mouse over the timeframe to replay the text selection:

![Image](https://www.freecodecamp.org/news/content/images/2022/02/text-select.gif)

Why do I need to know this? you may ask.

When a page doesn't respond swiftly to user interactions or has jerky movements, something must be off.

And it's usually owing to the browser's **main thread** being so busy that it can't deliver frames on time (more on this below).

In this guide, I'll explain how browsers turn code into pixels and how we can work with them to deliver a delightful user experience.

I'll focus on Google Chrome for this writing. However, the high-level concepts are the same across all browsers.

There are many theories to cover here, and I hope don't you mind that.

Michael Jordan said, "Keep the fundamentals down, and the level of everything you do will rise."

Trust me, knowing these theories won't be without a reward! 

You'll have a new perspective on how web pages change. And we'll get into lots of actions in the end.

## Refresh Rate or Frame Rate?

The average display device refreshes the screen sixty times per second (60Hz).

To the human eyes, any frequency above 12Hz is perceived as motion. [This article by Paul Bakaus](https://paulbakaus.com/tutorials/performance/the-illusion-of-motion/) does a great job of explaining it.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Animhorse.gif)
_**[CC BY-SA 2.5 ](https://en.wikipedia.org/wiki/Frame_rate#/media/File:Animhorse.gif">Animated Horse</a>** (12 drawings per second) by <a href="https://en.wikipedia.org/wiki/User:Janke">**Janke**</a>, Licensed under **<a href="https://creativecommons.org/licenses/by-sa/2.5/)**_

There are screens with higher refresh rates like 120Hz or 144Hz, but 60Hz is the standard for most display devices.

The refresh rate is different from the **frame rate**, though.

Refresh rate is the number of times a display device refreshes an image in one second. The frame rate is an arbitrary number of frames (in a filming system), captured or drawn in a second.

For instance, the standard rate for recording films is [24 fps](https://www.masterclass.com/articles/how-frame-rates-affect-film-and-video#3-standard-frame-rates-for-film-and-tv), even though it's not the maximum refresh rate of a modern TV. 

In that case, display devices use an algorithm to repeat specific frames to make the frame rate compatible with their refresh rate. This means you can watch 24 fps film on a 144Hz TV at the original 24 fps.

Why does frame rate even matter for web pages, you may ask?

A user who plays games at 120 fps would notice a slow page scroll on the same computer.

They won't enjoy web animations at any rate under 60 fps, either.

Have you ever come across those websites with plenty of ads and GIFs? I usually leave such pages quickly because I know finding another website would save me some time!

## There's a Deadline to Produce Each Frame

It takes time for the browser to draw a new frame.

Displaying sixty frames per second means each frame must be screen-ready in 16.7ms (1 sec ÷ 60).

Otherwise, the frame would be **delayed** or **dropped**. This issue is often referred to as **jank** on a web page.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/plane-1.gif)
_An animation with frame drops and delays_

So our top priority is clear now: we need to make our pages [jank free](http://jankfree.org/) 👆.

But first, we need to know how everything works.

## How a Frame is Produced

The web browser generates a new frame because something changed on the page. And it should reflect that change.

A web page changes when:

**The user interacts with the page**. They scroll, pinch zoom, click, select a piece of text, and so on.

**A piece of JavaScript code changes the page**. For instance, it adds a `<div>` element or changes a CSS style.

Each change starts a sequence of tasks, which results in a single frame. 

This sequence of tasks is known as **pixel pipeline**, **rendering waterfall**, or **rendering pipeline**.

And this is what it looks like from a high-level perspective:

* **JavaScript Evaluate** – the browser: oh, something changed! I need to generate a new frame.
* **Style Calculate** – the browser: now I must apply class `some-class` to to that `<div>` element).
* **Layout (reflow)** – the browser: I see some elements have new styles now. I need to calculate how much space they take on the screen and where they should be positioned based on these styles. Also, I need to calculate the geometry of every other element affected by this change!
* **Paint** – the browser: Now, I should group elements (that have an output) in multiple layers and convert each layer into a bitmap representation in the memory or the video RAM.
* **Compositing** – the browser: Now, I should combine these bitmaps in the defined order to form the final frame.

The same steps are also taken when the web page is rendered for the first time.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/pipeline-1.png)
_The pixel pipeline_

Each pipeline activity triggers its following activity. For instance, the layout triggers paint, and it continues until the last step.

We need to be mindful of every activity in the pipeline as each can contribute to low performance.

Let's get to know them a bit better.

### Evaluate JavaScript – when JavaScript code runs

You usually change the page from your JavaScript code.

Many of us remove an element like so:

```javascript
let myBox = document.querySelector('.my-box')

if (myBox) {
 myBox.remove()
}
```

Or hide it this way:

```javascript
let myBox = document.querySelector('.my-box')

if (myBox) {
  myBox.style.display = 'none'
}
```

Or add a CSS selector to its class list:

```javascript
let myBox = document.querySelector('.my-box')

if (myBox) {
  myBox.classList.add('my-special-box')
}
```

These changes invalidate a portion of the document and make the browser produce a new frame.

### Style – which CSS styles go with which element

Next, the web browser associates the new styles with the respective elements based on the matching selectors.

For instance, if you add the class `my-special-box` to an element's class list:

```javascript
let myBox = document.querySelector('.my-box')

if (myBox) {
  myBox.classList.add('my-special-box')
}
```

This step is where the respective styles are computed and applied to your element.

Also, as you probably know, [HTML elements and styles are converted into DOM and CSSOM trees, respectively](https://developers.google.com/web/fundamentals/performance/critical-rendering-path/constructing-the-object-model).

The browser uses these data structures internally. But it exposes them to JavaScript via the [browser APIs](https://www.decodingweb.dev/books/decoding-web-development/front-end-skills-to-get-you-started#web-apis) too. That's how we manipulated the document in the previous examples – we used the DOM API.

The web browser **combines** DOM and CSSOM to make a tree of all the visible elements within the `<body>` tag with their computed CSS styles.

This tree is called the **render tree, rendering tree,** or **frame tree**.

CSS Pseudo-elements, which have `content`, will be in the render tree, too.

The goal is now to turn the render tree into an image.

### Layout – to recalculate the geometry of elements after a change

An HTML element's geometry can affect siblings and children.

When your code adds (or removes) an element or changes its style, the browser recalculates the _new_ dimension and position of that element.

It also calculates the dimension and position of every sibling/child it may affect.

For instance, if you increase a paragraph's `margin-top` with JavaScript, it'll push down every following element on the document.

Or if a container's `width` gets smaller, its children might have to shrink in size too.

That said, a simple change to an element's geometry might force the browser to recalculate the geometry of hundreds of other elements affected (directly or indirectly) by the change.

The browser uses the render tree to recalculate the geometry of every visible element within the viewport.

This process is also known as **reflow**.

## Paint – When Code is Converted into Pixels

At this point, the web browser has all the data structures it needs. The styles are computed, and the layout is ready.

Depending on the rendering engine (Blink, Gecko, and so on), more abstractions and auxiliary data structures are created internally. But since browser internals tend to change pretty frequently, we'll keep our discussion as high level as possible. 

The next step is to turn code into pixels. This process is called painting. 

At this step, the browser's renderer creates a [display list](https://en.wikipedia.org/wiki/Display_list) of drawing commands for every element in the render tree.

These commands look like basic drawing commands: **draw a rectangle**, **draw a circle** or **draw a piece of text at these coordinates**.

Google Chrome uses [Skia](https://skia.org/) to do the drawing work. Skia is a 2D graphics library that provides standard APIs across various platforms. 

Chrome records these commands in a Skia `[SkPicture](https://api.skia.org/classSkPicture.html)` object. SkPicture has a `playback` method, which sends the drawing commands one by one to the specified canvas.

Eventually, the output of display lists would be a set of **bitmaps**.

To make sure we're all on the same page, let's quickly define what a bitmap is.

You might know that a pixel (picture element) is the smallest element of a digital image. Every image is a grid of pixels (a*b), and each pixel has a specific color. These pixels together form the image.

Now, what is a bitmap? 

Bitmap (in a graphic context) is a method of storing each pixel's color information as a set of bits.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Twitter-post---59.png)
_**[CC0 1.0](https://en.wikipedia.org/wiki/Raster_graphics#/media/File:Rgb-raster-image.svg">The smiley face</a>** (remixed), Licensed under **<a href="https://creativecommons.org/publicdomain/zero/1.0/deed.en)**_

In the above image, three pixels are highlighted with their color information (a mix of red, green, and blue). 

These values together form the bitmap of the image.

On the other hand, a bitmap is how computers store images in the memory or a storage device.

Turning web page content into bitmaps is known as **paint** or **rasterization**.

Nothing is painted yet, though. This step is more of a paint setup (or pre-paint) than the actual paintwork.

### Elements are painted on multiple layers

The actual paintwork is done at the discretion of the compositor later on. But the renderer provides enough hints to the compositor on how the elements should be painted on multiple layers.

Some elements are grouped as one layer and rasterized together (they share the same bitmap). However, some elements are painted on a dedicated layer.

For instance, in the animation below, the elements are painted onto four layers:

%[https://youtu.be/sSgtcdklEgQ]

You can see these layers in the Layers panel. 

To enable the Layers panel, while in Chrome DevTools, hold ⌘+**⇧**+P (or Ctrl+**⇧** Shift+P) to activate the Command Palette. Then, type "Show Layers" and run it.

These layers (also known as composite layers) make compositing possible.

These composite layers are then combined in the defined order and form the final image (more on this below).

Composite layers are similar to layers in raster graphics editors such as Photoshop. By managing shapes as layers, the designer can transform a shape without affecting other shapes.

If you wanted to change something on a flattened image, you might have to redesign the whole thing. 

Like Photoshop, painting elements onto separate layers enables the web browser to significantly reduce paintwork. 

So if an element on a layer is invalidated (it's changed), only the invalidated areas (tiles) of the respective layer need to be repainted.

The renderer considers various factors to make the layering decisions. For instance, if an element's CSS `opacity` will change at runtime, it'll be rasterized onto a dedicated layer.

You can also promote an element to be painted on a dedicated layer with `will-change` or `translateZ(0)` CSS properties.

You should always promote a layer for a reason, though.

Having many layers will incur costs on memory and processing time. This can become problematic on devices with limited capacity.

### Compositing: when the final frame is generated

The compositor receives a display list from the renderer with auxiliary data structures. 

Its job (among other things) is to arrange drawing the elements as multiple layers. 

Depending on what's on the page (and its styles), the painting can be done by software (software rasterization) or directly on the GPU (hardware rasterization).

Here's how it works on Google Chrome (for other browsers, you should check out their designs docs):

In the case of software rasterization, the graphics commands are executed by a set of raster worker threads, and then the generated bitmaps are shared with the GPU as textures.

However, if hardware rasterization kicks in, Skia generates the bitmaps directly on the GPU by issuing low-level commands to the operating system's graphics API.

Once the layers are ready, the compositor can apply compositor-level transformations (like `transform` and `opacity`) on each layer.

And finally, it combines (composites) the layers into one. If hardware acceleration is on, compositing will be done on the GPU too – by issuing low-level commands to the operating system's graphics API.

Remember this part because it plays a big role in optimising the animation performance.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-16-at-18.01.03-1.png)
_Layers after being composited_

Anytime I think about composite layers, it reminds me of the old cel animation production, where each frame was drawn on a transparent celluloid sheet. 

![Image](https://www.freecodecamp.org/news/content/images/2022/02/cel-animation-frame.jpeg)
_[CC BY-NC 2.0](https://www.flickr.com/photos/gogdog/5281815537">**My GunBuster Animation Cel**</a>, Licensed **<a href="https://creativecommons.org/licenses/by-nc/2.0/)**_

The background was a static drawing, and the animator shifted it to the left by an inch (with a roller) and placed the next cel frame on it.

This technique significantly reduced the drawing work and helped animation studios distribute the design work across multiple teams. 

You can watch this video of Disney's [animation production of Snow White](https://www.youtube.com/watch?v=aQkJM13PMKw) if you're curious about this old production method.

The compositing in the browsers has a similar purpose: **minimizing the paintwork when something changes.**

This is the last step of the pipeline – where a new frame is born.

## How to Optimize the Pipeline Activities

One question still remains, though. How can I avoid jerky page movements and stop annoying my users?

Here are a few things you should do.

### Know the most expensive changes

Not all changes involve every activity of the pixel pipeline. Some changes require less work and might skip a step or two.

Any change to an element's geometry (when you change the height, width, left, top, bottom, right, padding, margin, and so on) involves the whole pipeline.

This type of change is the most expensive change you can make to a web page.

Sometimes it's necessary, but sometimes it's totally avoidable (I'll tell you how).

![Image](https://www.freecodecamp.org/news/content/images/2022/02/pipeline-full-1.png)
_All steps of the pixel pipeline_

### Optimize paintwork

If you change a div's `background-color` property, the browser won't have to recalculate its geometry – because you only changed the color.

That means the web browser **skips the layout step** this time and jumps to painting.

The painting is still an expensive task. However, you can optimize it by reducing paint complexity – choosing simpler styles over complicated ones.

For instance, text shadows or gradients are more expensive than a simple background color.

Always ask yourself if you can choose a cheaper set of styles. Sometimes they make no difference in terms of aesthetics.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/pipeline-paint.png)
_Pixel pipeline without the layout step_

### **Use composited-only transformations**

Some changes won't require layout and paint because the compositor can apply them on its own.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/pipeline-composite.png)
_The pixel pipeline without Layout and Paint_

Below is the list of changes the browser can do cheaply at compositing time:

* **Re-positioning** with transform: `translate(mpx, npx)`
* **Rotating** with `transform:rotate(xdeg)`
* **Scaling** with `transform: scale(x)`
* **Opacity** with `opacity(x)`

These CSS properties seem like all you need when making a change to a page (well, most of it)!

Even better, if hardware acceleration is kept on, the compositor can use the GPU's computing power to apply these transformations. GPUs are created for this type of workload.

So, depending on the change we make to the DOM, the process will be one of these three scenarios.

* JavaScript → Style → Layout → Paint → Composite
* JavaScript → Style → Paint → Composite
* JavaScript → Style →  Composite

**"Performance is the art of avoiding work."**

And of course, the last scenario is the cheapest route to choose.

### Try to reduce the main thread's workload

A web browser is basically a [computer program](https://www.decodingweb.dev/books/processing-fundamentals/how-a-computer-program-works), and as a computer program, it'll have one or more processes in the memory while running.

Most browsers have a multi-process architecture, where activities are distributed across multiple threads of different processes (like the Renderer process and the GPU process, the Browser process, and so on).

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Google-chrome-processes.png)
_The Renderer and GPU process in Google Chrome_

In the case of Chrome, JavaScript, Style, Layout, paint setup happen in the main thread of the Renderer process (each tab has a dedicated Renderer).

This is almost everything!

The HTML content your browser fetches initially via an [HTTP request](https://www.decodingweb.dev/books/decoding-web-development/http) is parsed on a dedicated thread, but rendering and whatever content you add is parsed on the main thread.

That said, the focus should be on taking some load off the shoulders of the main thread. And in return, it helps us have a consistent frame rate.

The [CSS Triggers](https://csstriggers.com/) website can help you understand how changing a CSS property triggers layout, paint, and compositing.

You can also use this cheat sheet I created:

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Twitter-post---55.png)
_CSS properties and their initial step in the pixel pipeline_

### Make sure your JavaScript callbacks catch the train!

Ok, now we know how to help the browser take fewer steps (when possible!), but there's another thing to consider.

Whether it's an animation or a one-off change, we need to make sure our changes are synced with the frame rate at which the browser is displaying the content.

What does it even mean? You may ask.

Imagine a moving train with many wagons. 

This train is moving fast, and you have 16.7ms to draw a picture and throw it into each wagon (while it's moving).

If you fail to load a wagon in 16.7ms, it'll briefly stop until you throw the picture.

<iframe src="https://giphy.com/embed/TlK63EDww4g4tXUd0gE" width="480" height="320" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/train-subway-station-TlK63EDww4g4tXUd0gE">via GIPHY</a></p>

That moving train can be any movement on the web page. It could be an animation, transition, a page scroll, text selection, or any other motion.

If the train has to stop for you, it will deliver the frames with a delay. Users will notice it, and they won't like it!

Anytime you want to change the page, you need to somehow slide your work in a 16.7ms slot without slowing it down.

Sometimes it's tricky to do it, though.

Many developers still use `setInterval()` to make a timed loop. For instance, to repeat an action or create an animation.

There's a problem with  `setInterval()`, though. It doesn't have enough precision to run your code at the exact frequency you define. 

If you set the interval to repeat your code every 16.7ms, your code could run at any point during each 16.7ms slot.

So if we have 16.7ms to make a change, generate the frame, and load it onto its dedicated wagon, we need to make sure our code executes right at the beginning of each 16.7ms slot. 

Otherwise, it would require more than 16.7ms to complete, and it won't be ready for the current slot.

What if there was a way to run the callback right at the beginning of each 16.7ms time slot?

`RequestAnimationFrame()` has been designed just for that.

It makes sure your callbacks are executed right at the beginning of the next frame.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/requestanimationframe.png)
_requestAnimationFrame() v.s. setInterval()_

This way, your code has a higher chance of finishing within the 10ms time to leave enough time for the web browser to do its internal stuff in the total duration of 16.7ms.

So instead of:

```javascript
setInterval(
	() => {
    	// make some change
    },
    16.7
)
```

You can do:

```javascript
const animateSomething = function () {
	// make some change
    
    // Next call
    requestAnimationFrame(animateSomething)
}

// First manual call to start the animation
requestAnimationFrame(animateSomething)
```

Another benefit of using `requestAnimationFrame` is that the browser can run your animation more efficiently.

For instance, if the user switches to another tab, the browser will pause the animation. This reduces the processing time and battery life.

## How to Optimize an Animation – See it in Action

As promised, it's time to do some experiments.

For this experiment, I've created an animation in two different ways. 

The animation is about an airplane flying over the horizon at sunset.

In the first approach, I've used all the layout-triggering properties (left & top) without worrying about any performance trade-offs.

I've also used `setInterval` with 16.7ms frequency for my timed loop.

In the second approach, I refactored the code and used compositor-only styles. I also promoted my moving element (the airplane) with the `will-change` property to make sure it'll have its own layer. 

I also replaced `setInterval` with `requestAnimationFrame` for better timing.

To simulate the airplane's movement, I've used the `Math.sine()` with some adjustments. The traveling path is also drawn with an SVG-based sine graph.

Here's the [CodePen link](https://codepen.io/lavary/pen/YzEpLbE) to the first approach:

%[https://codepen.io/lavary/pen/YzEpLbE]

And [the second approach](https://codepen.io/lavary/pen/eYvOojp) with layer promotion (`will-change: transform`) compositor-only styles (`transform: translate()`) , and `requestAnimationFrame`:

%[https://codepen.io/lavary/pen/eYvOojp]

### Let's compare the two approaches

One of the metrics you can use is the frame rate. It helps you monitor the consistency of the frames during a motion.

Take a look at the below recording:

![Image](https://www.freecodecamp.org/news/content/images/2022/02/animation-paint.png)

You can see the FPS meter in the image above (top left of the screenshot). Even though the screenshot shows 90 fps, the yellow/red bars indicate some frames were missed or delayed.

The Event Log (bottom right) shows all the steps were involved during the recording: **Recalculate Style > Layout > Paint > Composite layers.**

To enable the FPS meter, while in Chrome DevTools, hold ⌘+**⇧**+P (or Ctrl+**⇧** Shift+P) to activate the Command Palette. Then, type `FPS meter` and choose Show frames per second (FPS) meter.

And here's a quick guide on reading it:

![Image](https://www.freecodecamp.org/news/content/images/2022/02/FPS-meter.png)
_FPS meter_

Now, let's measure the second approach:

![Image](https://www.freecodecamp.org/news/content/images/2022/02/animation-composite.png)

In the second recording, the average FPS is 118.8 with no missed or dropped frames.

The event log also confirms no layout and paintwork were necessary, and the compositor did the whole thing (Recalculate Style → Composite Layer).

You can also use Chrome's **Paint Flashing** tool to see what parts of the page are being repainted. This is useful to detect unwanted paintwork during user interactions.

In the airplane example, the area being repainted (the moving airplane) is displayed as green-bordered rectangles. 

%[https://youtu.be/1rd2aemUGCE]

Enabling paint flashing for the second approach won't show anything as there's no paintwork during the animation.

The question is can a user notice this improvement? 

Let's see.

Here are both animations in slow motion (10x slowed down) to see if there's any change:

%[https://youtu.be/X05WCbC-ITY]

I'll leave it to your judgment.

## Too long; didn't read?

To have smooth motions on your page, all you need to do is to make sure:

* Fames are delivered on time
* Frames are delivered on time **consistently**

And here's a checklist to achieve it:

* Make sure your JavaScript changes happen at the beginning of each frame by using `requestAnimationFrame`. 
* When changing the dimension of an element, use `transform:scale()`  over `height` & `width`.
* To move the elements around, always use `transform: translate()` over coordinates (`top`, `right`, `bottom`, and `left`).
* Reduce paint complexity by using simple CSS styles over expensive ones. For instance, if possible, use solid colors over gradients or shadows.
* Normalize using the transitions on mobile versions. Even though the computing capacity of mobile phones is limited, mobile-version UX often contains more transitions/effects owing to their small screen.
* Use your browser's developer tools to diagnose animation performance. Use tools such as Paint Flashing and FPS meter to fine-tune your animations.
* Use DevTool's Performance panel to see how your code runs on lower-end devices.

You can apply these micro-optimizations when doing any type of change. Whether you're making JavaScript or CSS animation, or you're just making a one-off change with JavaScript.

This was the opening line of this guide:

> What if I told you web pages were interactive animations played back by your web browser.

But, what if I tell you now this was just the tip of the iceberg?!

Don't worry, you can already do a lot to make your web pages look pleasant to the eyes.

If you want to take your performance knowledge to the next level, I maintain a [dedicated page to collect web performance resources from various creators](https://www.decodingweb.dev/courses/web-performance). Check it out!

If you have any questions or comments or there's something I missed (or I've gotten wrong), please feel free to fire away at **@lavary_** on Twitter_._

Thanks for reading!

### Attributions:

* Post image: **[Antics 2-D Animation of White Rabbit](https://commons.wikimedia.org/wiki/File:Antics_2-D_Animation_infobox_screenshot.png)** (image was cropped) by **Antics Workshop** under **[CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)** 

