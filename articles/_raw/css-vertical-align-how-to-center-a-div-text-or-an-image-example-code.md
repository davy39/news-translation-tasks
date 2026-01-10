---
title: CSS Vertical Align – How to Center a Div, Text, or an Image [Example Code]
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-08-04T15:02:39.000Z'
originalURL: https://freecodecamp.org/news/css-vertical-align-how-to-center-a-div-text-or-an-image-example-code
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/center.png
tags:
- name: CSS
  slug: css
- name: CSS Grid
  slug: css-grid
- name: flexbox
  slug: flexbox
- name: Web Design
  slug: web-design
seo_title: null
seo_desc: "Even with helpful tools like CSS Grid and Flexbox, centering elements in\
  \ CSS remains notoriously challenging. \nIt's been the subject of many jokes and\
  \ memes, and when you successfully center something, you'll want to brag about it.\n\
  Why is Centering C..."
---

Even with helpful tools like CSS Grid and Flexbox, centering elements in CSS remains notoriously challenging. 

It's been the subject of many jokes and memes, and when you successfully center something, you'll want to brag about it.

## Why is Centering CSS Elements So Hard?

CSS can be tricky to work with. For example, if you're trying to align something horizontally OR vertically, it's not that difficult.

You can just set text-align to center for an inline element, and `margin: 0 auto` would do it for a block-level element.

But issues arise on multiple fronts if you're trying to combine both vertical and horizontal alignments.   

In this tutorial, I will introduce you to three different methods to correctly center a div, text, or image in CSS.

## How to Center an Element with the CSS Position Property 

The CSS position property takes relative, absolute, fixed, and static (the default) as values. When set, you will be able to apply the top, right, bottom, and left properties to the element. 

The combination of relative and absolute values can get a lot of things done, and so you can use it to center anything. 

Take a look at the snippets below to see some examples.

### How to center text with CSS positioning

```html
<div class="container">
    <div class="centered-element">
      <p>I'm a Camper, and I'm vertically centered</p>
    </div>
</div>
``` 

```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
} 

.container {
  position: relative;
  height: 400px;
  border: 2px solid #006100;
}

.centered-element {
  margin: 0;
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
}
```

![ss1b](https://www.freecodecamp.org/news/content/images/2021/08/ss1b.png)

### How to center an image with CSS positioning

```html
<div class="container">
    <div class="centered-element">
      <img src="freecodecamp.png" alt="centered" />
    </div>
</div>
```

```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.container {
  position: relative;
  height: 400px;
  border: 2px solid #006100;
}

.centered-element {
  margin: 0;
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
}
```

![ss2b](https://www.freecodecamp.org/news/content/images/2021/08/ss2b.png)

The above code has made the text and image centered vertically. To take care of both vertical and horizontal centering, we need to make a little tweak in the CSS. We'll set the top property to 50%, and we'll add a transform on both the X and Y axes.

```
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.container {
  position: relative;
  height: 400px;
  border: 2px solid #006100;
}

.centered-element {
  margin: 0;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

```

The text now looks like this:
![ss4b](https://www.freecodecamp.org/news/content/images/2021/08/ss4b.png)

And the image like this: 
![ss3b](https://www.freecodecamp.org/news/content/images/2021/08/ss3b.png)

Note that I applied the transform property because the child (with the class of centered-element) was slightly off-center. `translateY()` pushes it to the center vertically and translate on both the X and Y-axis (`translate()`) pushes it to the center vertically and horizontally. 

## How to Center an Element with Flexbox in CSS

CSS Flexbox handles layouts in one dimension (row or column). With Flexbox, it is pretty easy to center a div, text, or image in just three lines of code. 

Check the snippets below for examples. 

### How to center text with Flexbox

```html
<div class="container">
    <div class="centered-element">
      <p>I'm a Camper, and I'm vertically centered</p>
    </div>
</div>
```

```css
.container {
    display: flex;
    align-items: center;
    height: 600px;
    border: 2px solid #006100; 
}
```
![ss5b-1](https://www.freecodecamp.org/news/content/images/2021/08/ss5b-1.png)

### How to center an image with Flexbox

```html
<div class="container">
    <div class="centered-element">
      <img src="freecodecamp.png" alt="centered" />
    </div>
</div>
```

```css
.container {
    display: flex;
    align-items: center;
    height: 600px;
    border: 2px solid #006100; 
}
```
![ss6b](https://www.freecodecamp.org/news/content/images/2021/08/ss6b.png)

We took care of the vertical alignment in just two lines of code. To make the image and text horizontally centered, add in justify-content: center.

```html
<div class="container">
    <div class="centered-element">
      <p>I'm a Camper, I'm now vertically and horizontally centered</p>
    </div>
</div>
```

```html
<div class="container">
    <div class="centered-element">
      <img src="freecodecamp.png" alt="centered" />
    </div>
</div>
```

```css
.container {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 600px;
    border: 2px solid #006100;
}
```

The text now looks like this:
![ss7bb](https://www.freecodecamp.org/news/content/images/2021/08/ss7bb.png)

And the image like this: ![ss11bb](https://www.freecodecamp.org/news/content/images/2021/08/ss11bb.png)

## How to Center an Element with CSS Grid 

With Flexbox, it is pretty easy to center anything, right? But with CSS Grid, it is really easy to center anything, because two lines of code are enough to do it for you. 

### How to center text with CSS Grid 

```html
<div class="container">
    <div class="centered-element">
      <p>I'm a Camper, and I'm vertically centered</p>
    </div>
</div>
```

```css
.container {
    display: grid;
    align-items: center;
    height: 600px;
    border: 2px solid #006100;
}
```

![ss8bb](https://www.freecodecamp.org/news/content/images/2021/08/ss8bb.png)

### How to center an Image with CSS Grid

```html
<div class="container">
    <div class="centered-element">
      <img src="freecodecamp.png" alt="centered" />
    </div>
</div>
```

```css
.container {
    display: grid;
    align-items: center;
    height: 600px;
    border: 2px solid #006100;
}
```

The above examples takes care of vertical centering for you. To get the text and image centered horizontally too, replace the align items with `place items` – a combination of both `align-items` and `justify-content`:

```css
.container {
    display: grid;
    place-items: center;
    height: 600px;
    border: 2px solid #006100;
}

```

The text now looks like this:

![ss7bb-1](https://www.freecodecamp.org/news/content/images/2021/08/ss7bb-1.png)

And the image like this:
![ss11bb-1](https://www.freecodecamp.org/news/content/images/2021/08/ss11bb-1.png)

## How to Center a Standalone Div, Text, or Image in CSS

The three methods above let you center a div, text, or image in a container. You can also center a standalone div, text, or image. 

Let's see how to do that now.
 
### How to center a standalone div in CSS

```html
<div class="container"></div>
```

```css
div.container {
    height: 300px;
    width: 300px;
    border: 2px solid #006100;
    margin: 0 auto;
  }
```

![ss12bb](https://www.freecodecamp.org/news/content/images/2021/08/ss12bb.png)

### How to center standalone text in CSS 

```html
<p>I'm a Camper, and I'm centered</p>
```
 
```css
     p {
         text-align: center;
     }
```

![ss13bb](https://www.freecodecamp.org/news/content/images/2021/08/ss13bb.png)

### How to center a standalone image in CSS

```html
<img src="freecodecamp.png" alt="centered" />
```

```css
img {
      display: block;
      margin: 0 auto;
 }
 /* Applies a display of block, a margin 0f 0 at the top and bootom, 
 and auto on the left and right */
```

![ss14bb](https://www.freecodecamp.org/news/content/images/2021/08/ss14bb.png)

## Conclusion

I hope this tutorial gives you enough knowledge about vertical alignment and how to center elements in CSS so it's less of a hassle for you in your next project. 

Thank you for reading, and keep coding.



