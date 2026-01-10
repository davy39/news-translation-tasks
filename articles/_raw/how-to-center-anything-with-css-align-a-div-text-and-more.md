---
title: How to Center Anything with CSS - Align a Div, Text, and More
subtitle: ''
author: Kristofer Koishigawa
co_authors: []
series: null
date: '2020-05-15T04:24:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-center-anything-with-css-align-a-div-text-and-more
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/5f9c9b00740569d1a4ca291b.jpg
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: responsive design
  slug: responsive-design
seo_title: null
seo_desc: "Centering things is one of the most difficult aspects of CSS. \nThe methods\
  \ themselves usually aren't difficult to understand. Instead, it's more due to the\
  \ fact that there are so many ways to center things. \nThe method you use can vary\
  \ depending on t..."
---

Centering things is one of the most difficult aspects of CSS. 

The methods themselves usually aren't difficult to understand. Instead, it's more due to the fact that there are so many ways to center things. 

The method you use can vary depending on the HTML element you're trying to center, or whether you're centering it horizontally or vertically.

In this tutorial, we'll go over how to center different elements horizontally, vertically, and both vertically and horizontally.

### Here's an Interactive Scrim Showing How to Center Anything with CSS

<iframe src="https://scrimba.com/scrim/co4db41c6a8d6458e2d84500b?embed=freecodecamp,mini-header" width="100%" height="420"></iframe>

## How to Center Horizontally

Centering elements horizontally is generally easier than centering them vertically. Here are some common elements you may want to center horizontally and different ways to do it.

### How to Center Text with the CSS Text-Align Center Property

To center text or links horizontally, just use the `text-align` property with the value `center`:

```html
<div class="container">
  <p>Hello, (centered) World!</p>
</div>

```

```css
.container {
  font-family: arial;
  font-size: 24px;
  margin: 25px;
  width: 350px;
  height: 200px;
  outline: dashed 1px black;
}

p {
  /* Center horizontally*/
  text-align: center;
}

```

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-15.png)

### How to Center a Div with CSS Margin Auto

Use the shorthand `margin` property with the value `0 auto` to center block-level elements like a `div` horizontally:

```html
<div class="container">
  <div class="child"></div>
</div>
```

```css
.container {
  font-family: arial;
  font-size: 24px;
  margin: 25px;
  width: 350px;
  height: 200px;
  outline: dashed 1px black;
}

.child {
  width: 50px;
  height: 50px;
  background-color: red;
  /* Center horizontally*/
  margin: 0 auto;
}

```

![Image](https://www.freecodecamp.org/news/content/images/2020/11/box-centered-horizontally.jpg)

### How to Center a Div Horizontally with Flexbox

Flexbox is the most modern way to center things on the page, and makes designing responsive layouts much easier than it used to be. However, it's not fully supported in some legacy browsers like Internet Explorer.

To center an element horizontally with Flexbox, just apply `display: flex` and `justify-content: center` to the parent element:

```html
<div class="container">
  <div class="child"></div>
</div>

```

```css
.container {
  font-family: arial;
  font-size: 24px;
  margin: 25px;
  width: 350px;
  height: 200px;
  outline: dashed 1px black;
  /* Center child horizontally*/
  display: flex;
  justify-content: center;
}

.child {
  width: 50px;
  height: 50px;
  background-color: red;
}

```

![Image](https://www.freecodecamp.org/news/content/images/2020/11/box-centered-horizontally-1.jpg)

## How to Center Vertically

Centering elements vertically without modern methods like Flexbox can be a real chore. Here we'll go over some of the older methods to center things vertically first, then show you how to do it with Flexbox.

### How to Center a Div Vertically with CSS Absolute Positioning and Negative Margins

For a long time this was the go-to way to center things vertically. For this method you must know the height of the element you want to center.

First, set the `position` property of the parent element to `relative`. 

Then for the child element, set the `position` property to `absolute` and `top` to `50%`:

```html
<div class="container">
  <div class="child"></div>
</div>

```

```css
.container {
  font-family: arial;
  font-size: 24px;
  margin: 25px;
  width: 350px;
  height: 200px;
  outline: dashed 1px black;
  /* Setup */
  position: relative;
}

.child {
  width: 50px;
  height: 50px;
  background-color: red;
  /* Center vertically */
  position: absolute;
  top: 50%;
}

```

![Image](https://www.freecodecamp.org/news/content/images/2020/11/box-centered-vertically-1.jpg)

But that really just vertically centers the top edge of the child element.

To truly center the child element, set the `margin-top` property to `-(half the child element's height)`:

```css
.container {
  font-family: arial;
  font-size: 24px;
  margin: 25px;
  width: 350px;
  height: 200px;
  outline: dashed 1px black;
  /* Setup */
  position: relative;
}

.child {
  width: 50px;
  height: 50px;
  background-color: red;
  /* Center vertically */
  position: absolute;
  top: 50%;
  margin-top: -25px; /* Half this element's height */
}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/11/box-centered-vertically-final.jpg)

### How to Center a Div Vertically with Transform and Translate

If you don't know the height of the element you want to center (or even if you do), this method is a nifty trick.

This method is very similar to the negative margins method above. Set the `position` property of the parent element to `relative`. 

For the child element, set the `position` property to `absolute` and set `top` to `50%`. Now instead of using a negative margin to truly center the child element, just use `transform: translate(0, -50%)`:

```html
<div class="container">
  <div class="child"></div>
</div>

```

```css
.container {
  font-family: arial;
  font-size: 24px;
  margin: 25px;
  width: 350px;
  height: 200px;
  outline: dashed 1px black;
  /* Setup */
  position: relative;
}

.child {
  width: 50px;
  height: 50px;
  background-color: red;
  /* Center vertically */
  position: absolute;
  top: 50%;
  transform: translate(0, -50%);
}

```

![Image](https://www.freecodecamp.org/news/content/images/2020/11/box-centered-vertically-final-1.jpg)

Note that `translate(0, -50%)` is shorthand for `translateX(0)` and `translateY(-50%)`. You could also write `transform: translateY(-50%)` to center the child element vertically.

### How to Center a Div Vertically with Flexbox

Like centering things horizontally, Flexbox makes it super easy to center things vertically.

To center an element vertically, apply `display: flex` and `align-items: center` to the parent element:

```html
<div class="container">
  <div class="child"></div>
</div>
```

```css
.container {
  font-family: arial;
  font-size: 24px;
  margin: 25px;
  width: 350px;
  height: 200px;
  outline: dashed 1px black;
  /* Center vertically */
  display: flex;
  align-items: center;
}

.child {
  width: 50px;
  height: 50px;
  background-color: red;
}

```

![Image](https://www.freecodecamp.org/news/content/images/2020/11/box-centered-vertically-final-2.jpg)

## How to Center Both Vertically and Horizontally

### How to Center a Div Vertically and Horizontally with CSS Absolute Positioning and Negative Margins

This is very similar to the method above to center an element vertically. Like last time, you must know the width and height of the element you want to center.

Set the `position` property of the parent element to `relative`.

Then set the child's `position` property to `absolute`, `top` to `50%`, and `left` to `50%`. This just centers the top left corner of the child element vertically and horizontally.

To truly center the child element, apply a negative top margin set to half the child element's height, and a negative left margin set to half the child element's width:

```html
<div class="container">
  <div class="child"></div>
</div>

```

```css
.container {
  font-family: arial;
  font-size: 24px;
  margin: 25px;
  width: 350px;
  height: 200px;
  outline: dashed 1px black;
  /* Setup */
  position: relative;
}

.child {
  width: 50px;
  height: 50px;
  background-color: red;
  /* Center vertically and horizontally */
  position: absolute;
  top: 50%;
  left: 50%;
  margin: -25px 0 0 -25px; /* Apply negative top and left margins to truly center the element */
}

```

![Image](https://www.freecodecamp.org/news/content/images/2020/11/box-centered-vertically-and-horizontally.jpg)

### How to Center a Div Vertically and Horizontally with Transform and Translate

Use this method to center an element vertically and horizontally if you don't know its exact dimensions and can't use Flexbox.

First, set the `position` property of the parent element to `relative`. 

Next, set the child element's `position` property to `absolute`, `top` to `50%`, and `left` to `50%`. 

Finally, use `transform: translate(-50%, -50%)` to truly center the child element:

```html
<div class="container">
  <div class="child"></div>
</div>

```

```css
.container {
  font-family: arial;
  font-size: 24px;
  margin: 25px;
  width: 350px;
  height: 200px;
  outline: dashed 1px black;
  /* Setup */
  position: relative;
}

.child {
  width: 50px;
  height: 50px;
  background-color: red;
  /* Center vertically and horizontally */
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

```

![Image](https://www.freecodecamp.org/news/content/images/2020/11/box-centered-vertically-and-horizontally-1.jpg)

### How to Center a Div Vertically and Horizontally with Flexbox

Flexbox is the easiest way to center an element both vertically and horizontally.

This is really just a combination of the two previous Flexbox methods. To center the child element(s) horizontally and vertically, apply `justify-content: center` and `align-items: center` to the parent element:

```html
<div class="container">
  <div class="child"></div>
</div>

```

```css
.container {
  font-family: arial;
  font-size: 24px;
  margin: 25px;
  width: 350px;
  height: 200px;
  outline: dashed 1px black;
  /* Center vertically and horizontally */
  display: flex;
  justify-content: center;
  align-items: center;
}

.child {
  width: 50px;
  height: 50px;
  background-color: red;
}

```

![Image](https://www.freecodecamp.org/news/content/images/2020/11/box-centered-vertically-and-horizontally-2.jpg)

That's everything you need to know to center with the best of 'em. Now go forth and center all the things.

