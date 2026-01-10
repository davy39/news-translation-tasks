---
title: How to Design, Code, and Animate SVGs
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-07-12T17:04:01.000Z'
originalURL: https://freecodecamp.org/news/a-guide-to-svg-on-web-c5932dadca03
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ftD823GY_L-c4A-5hY8ozA.png
tags:
- name: animation
  slug: animation
- name: CSS
  slug: css
- name: Design
  slug: design
- name: Web Design
  slug: web-design
- name: women in tech
  slug: women-in-tech
seo_title: null
seo_desc: 'By Surbhi Oberoi

  You can think of Scalable Vector Graphics (SVG’s) as responsive graphics. SVG is
  an XML-based format that allows you to create an image by using defined tags and
  attributes. Your code will render an image that you can edit right in y...'
---

By Surbhi Oberoi

You can think of Scalable Vector Graphics (SVG’s) as responsive graphics. SVG is an XML-based format that allows you to create an image by using defined tags and attributes. Your code will render an image that you can edit right in your code editor.

Here’s a sample SVG. If you look at its code, you’ll notice that it’s made up of tags and attributes, just like an HTML document. The whole thing is contained inside <svg> tag. First, there’s a <rect> tag with black strokes and white fill. And inside that, there’s an ellipse (almost a circle, but notice the ry and rx attributes) which is filled with red color.

We can use SVG on the web in two ways. We can use the SVG files as the src attribute of <img> tags. So, you can have <img src=”japan.svg”> like you would do with PNGs and JPEGs.

But, the more interesting case (in case you have noticed that the tags have an id attribute like HTML) is that we can directly paste the source of the SVG in a <div> inside our HTML. We can then style these divs like individual building blocks — or even groups of building blocks — the way we want. We can apply CSS, animations, or even add interactivity using JavaScript. This is what makes SVGs one of the most versatile and hottest element right now in HTML.

SVGs are infinitely scalable, responsive, have smaller file size, are future-proof for next-generation bazillion-pixel dense screens, and can be styled, animated and interacted with using known web technologies — namely CSS and JavaScript.

Notice that all these things were previously possible only with a Flash embed — which required a flash player and lots of specialized work. And there’s no love going around for Flash these days.

#### Vector vs Raster images

Raster images are made up of pixels to form a complete image. JPEGs, GIFs and PNGs are common raster image types. Almost all of the photos found on the web are raster images.

Raster images consist of a fixed number of pixels, so resizing them without effecting their resolution is not possible. You may have noticed that resizing most images gives them a grainy, and blurry look. That’s because of their fixed pixel count.

Here’s what happens when you zoom in on a raster image:

![Image](https://cdn-media-1.freecodecamp.org/images/0*DZ0Nry0tSMuKYFrL.gif)

Vector images, on the other hand, are flexible and resolution-independent. They are constructed using geometric shapes — lines, rectangles, curves — or a sequence of commands. You can edit their attributes, such as color, fill, and outline.

One common use for vector images is icons and small icon animations. These will appear crisp, even on the highest density displays such as upcoming 4k smartphones.

Here’s what happens when you zoom in on a vector image:

![Image](https://cdn-media-1.freecodecamp.org/images/0*9kjCwkCs_CIlJO9k.gif)

#### SVG tags

**<s**vg>

The <svg> tag embeds an SVG document inside the current document, HTML for instance. The tag has its own x and y coordinates, height and width, and its own unique id.

Here’s what an <svg> tag might look like:

```
<svg width="580" height="400" xmlns="http://www.w3.org/2000/svg">
```

**<**;g>

The <g> tag groups the elements together, and acts like a container for related graphic elements. A <g> element can even contain other <g> elements nested within it.

Here’s an example of a <g> tag:

```
<g> <title>background</title> <rect fill="#fff" id="canvas_background" height="402" width="582" y="-1" x="-1"/> <g display="none" overflow="visible" y="0" x="0" height="100%" width="100%" id="canvasGrid"> <rect fill="url(#gridpattern)" stroke-width="0" y="0" x="0" height="100%" width="100%"/> </g> </g>
```

**<re**ct>

The <rect> element is an SVG basic shape representing a rectangle. The element can have various attributes, like coordinates, height, width, fill color, stroke color, and sharp or rounded corners.

Here’s an example of a <rect> tag:

```
<rect id="svg_1" height="253" width="373" y="59" x="107.5" stroke-width="1.5" stroke="#000" fill="#fff"/>
```

**<u**se>

The <use> element allows you to clone and reuse the graphical SVG elements including other elements like <g> <rect> as well as other <use> elements.

Here’s an example of a <use> tag:

```
<text y="15">black</text> <use x="50" y="10" xlink:href="#Port" /> <text y="35">red</text> <use x="50" y="30" xlink:href="#Port"/> <text y="55">blue</text> <use x="50" y="50" xlink:href="#Port" style="fill:blue"/
```

**<pa**th>

The <path> element defines a path of coordinates for a shape. The code for path tag might seem cryptic, but don’t be intimidated. The following example code can be read like this:  
1. “M150 o” — Move to (150,0)

2.”L75 200" — Draw a line to (75,200) from last position (which was (150,0)

3. “L255 200” — Draw a line to (225,200) from last position (which was (75,200)

4. “Z” — Close the loop (draw to starting point)

You probably don’t need to learn this since the code for path can be generated in any SVG editor, but it’s cool to know.

Here’s an example of a <path> tag:

```
<svg height="210" width="400"> <path d="M150 0 L75 200 L225 200 Z" /> </svg>
```

**<symb**ol>

Finally, the <symbol> element defines symbols that are reusable. These symbols can only be rendered when called by the <use> element.

Here’s an example of a <symbol> tag:

```
<svg> <symbol id="sym01" viewBox="0 0 150 110"> <circle cx="50" cy="50" r="40" stroke-width="8" stroke="red" fill="red"/> <circle cx="90" cy="60" r="40" stroke-width="8" stroke="green" fill="white"/> </symbol> <use xlink:href="#sym01" x="0" y="0" width="100" height="50"/> <use xlink:href="#sym01" x="0" y="50" width="75" height="38"/> <use xlink:href="#sym01" x="0" y="100" width="50" height="25"/> </svg>
```

#### Creating SVGs

There are plenty of SVG editors available, like Adobe Illustrator, and Inkscape, which is free and open source. Since SVG files are plain-text XML, you could also hand-code one in a pinch.

For this example I’ll use a simple online [editor](http://editor.method.ac/) where you can design SVGs without having to install anything.

1. First create a circle

2. Next add more circles and save the source code

**CSS3 animations**

SVGs can be animated by adding an id or a class to the SVG path in the code and then styling it in CSS3 like any other document. Below is an example of how SVGs can be animated.

CSS3 animation offers a variety of animation types that you can chose from. Line animation is another cool attribute of SVG.

For this next example, I wrote the text “Hi, I am Surbhi” using pen in the editor. Then I used CSS3 keyframes again to animate the stroke.

Notice that each path has a unique id. That is because the delay in the animation is important when animating a stroke with more than one word.

#### The <animate> tag animations

<animate> is an animation tag built into the SVG element itself. It defines how the attribute of an element changes from the initial value to the end value in the specified animation duration. This is used to animate properties that cannot be animated by CSS alone.

The common elements of the animate tag are color, motion, and transform.

The animate tag is nested inside the shape tag of the object that has to be animated. It does not work on the path coordinates, but only inside the object tags. Notice the additive attribute. It signifies that the animations do not override one another but instead work together at the same time.

Here’s an example of animating an SVG using the HTML5 animate tag:

#### JavaScript based animations and interactivity

Since SVG is just a document with tags, we can also use JavaScript to interact with individual elements of the SVGs by getting hold of their selectors (id or class).

Apart from vanilla JS, there are various JavaScript libraries available for animating and interacting with SVGs like Vivus.js, Snap.svg, RaphaelJS, and Velocity.js.

In the following example, I have used the Vivus.js library along with jQuery to achieve a line stroke animation.

#### Why not use SVGs for all images?

SVGs are mostly suited for images that can be constructed with few geometrical shapes and formulas. Though, in principle, you can convert anything like your photograph to SVG, the size of the image would be several megabytes, thus defeating the space-saving purpose of using SVGs. You’re better off using SVGs for icons, logos, and small animations.

Here is something I created while I was learning about SVGs, using CSS and SVGs, without any libraries. (Don’t Judge!) [https://github.com/surbhioberoi/surbhi.me](https://github.com/surbhioberoi/surbhi.me)

![Image](https://cdn-media-1.freecodecamp.org/images/0*wWFcDqQBEODlYS8x.gif)

_Originally published at [surbhioberoi.com](http://surbhioberoi.com/a-complete-guide-to-svg/) on July 12, 2016._

