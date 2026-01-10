---
title: How to use the position property in CSS to align elements
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-18T14:54:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-the-position-property-in-css-to-align-elements-d8f49c403a26
coverImage: https://cdn-media-1.freecodecamp.org/images/1*fXBo56b0tanSCNHo4O2eWw.jpeg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Cem Eygi

  Positioning elements with CSS in web development isn’t as easy as it seems. Things
  can get quickly complicated as your project gets bigger and without having a good
  understanding of how CSS deals with aligning HTML elements, you won''t be ...'
---

By Cem Eygi

Positioning elements with CSS in web development isn’t as easy as it seems. Things can get quickly complicated as your project gets bigger and without having a good understanding of how CSS deals with aligning HTML elements, you won't be able to fix your alignment issues.

There are different ways/methods for positioning elements with pure CSS. Using CSS **float, display** and **position** properties are the most common methods. 

In this article, I will be explaining one of the most confusing ways for aligning elements with pure CSS: the **position property.** I also have another tutorial for [CSS Display Property here](https://www.youtube.com/watch?v=hgoFi0fCv3w).

If you prefer, you can watch the video version of CSS Positioning Tutorial:

%[https://youtu.be/NYEEN4rs4T8]

Let's begin...

### CSS Position & Helper Properties

So there are 5 main values of the **Position** Property**:**

`position: static | relative | absolute | fixed | sticky`

and additional properties for setting the coordinates of an element (I call them **“helper properties”**):

`top | right | bottom | left` AND the `z-index`

> _**Important Note**_**:** Helper properties don’t work without a declared position, or with **position: static.**__

#### What is this z-index?

We have height and width (x, y) as 2 dimensions. Z is the 3rd dimension. An element in the webpage comes in front of other elements as its `z-index` value increases. 

> **Z-index** doesn’t work with `position: static` or without a declared position.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Dc7075K8xmYZQAqn6BaJPg.png)
_Elements are ordered from back to front, as their <strong class="markup--strong markup--figure-strong" style="font-weight: 700;">z-index** increase_

You can watch the video on my channel to see how to use the **z-index** in more details:

%[https://www.youtube.com/watch?v=vo1JBj-OAa8]

Now let’s move on with the **position** property **values**...

### 1. Static

`position: static` is the **default value**. Whether we declare it or not, elements are positioned in a normal order on the webpage. Let’s give an example:

First, we define our HTML structure:

```html
<body>
  <div class="box-orange"></div>
  <div class="box-blue"></div>
</body>
```

Then, we create 2 boxes and define their widths, heights & positions:

```css
.box-orange {          // without any position declaration
  background: orange;
  height: 100px;
  width: 100px;       
}

.box-blue {
  background: lightskyblue;
  height: 100px;
  width: 100px; 
  position: static;   // Declared as static
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*atA27-7dzI4wKkg_HfAtLw.png)
_same result with &amp; without<strong class="markup--strong markup--figure-strong" style="font-weight: 700;"> position: static**_

As we can see in the picture, defining **position: static** or not doesn't make any difference. The boxes are positioned according to the **normal document flow**.

### 2. Relative

`position: relative`: **An element’s new position relative to its normal position.**

Starting with `position: relative` and for all **non-static** position values, we are able to change an element’s **default** position by using the **helper propertie**s that I've mentioned above.

Let’s move the orange box next to the blue one.

```css
.box-orange {
  position: relative;  // We are now ready to move the element
  background: orange;
  width: 100px;
  height: 100px;
  top: 100px;         // 100px from top relative to its old position
  left: 100px;        // 100px from left
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*noqTpZ-EBTftlKdFi48Iiw.png)
_<strong class="markup--strong markup--figure-strong" style="font-weight: 700;">Orange box is moved 100px to bottom &amp; right, relative to its normal position**_

> _NOTE: Using **position: relative**_ for an element, doesn’t affect other elements’ positions.

### 3. Absolute

In `position: relative`, the element is positioned **relative to itself.** However, an **absolute**ly positioned element is **relative to its parent**.

An element with `position: absolute` is removed from the normal document flow. It is positioned automatically to the starting point (**top-left corner)** of its parent element. If it doesn’t have any parent elements, then the initial **document <html>** will be its parent.

Since `position: absolute` removes the element from the document flow, other elements **are affected** and behave as the element is removed completely from the webpage.

Let’s add a **container** as parent element:

```html
<body>
  <div class="container">
    <div class="box-orange"></div>
    <div class="box-blue"></div>
  </div>
</body>
```

```css
.box-orange {
  position: absolute;
  background: orange;
  width: 100px;
  height: 100px;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*C15mDxOdtFLkXLcFaVRYBQ.png)
_<strong class="markup--strong markup--figure-strong" style="font-weight: 700;">position: absolute** takes the element to the <strong class="markup--strong markup--figure-strong" style="font-weight: 700;">beginning** of its parent_

Now it looks like the blue box has disappeared, but it hasn’t. The blue box behaves like the orange box is removed, so it shifts up to the orange box’s place.

Let’s move the orange box 5 pixels:

```css
.box-orange {
  position: absolute;
  background: orange;
  width: 100px;
  height: 100px;
  left: 5px;
  top: 5px;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*ss6uEQz9Bbdrdst8kNiHqQ.png)
_<strong class="markup--strong markup--figure-strong" style="font-weight: 700;">Now we can see the blue box**_

The coordinates of an **absolute** positioned element are **relative to its parent** if the parent also has a **non-static position.** Otherwise, helper properties position the element relative to the **initial <html>.**

```css
.container {
  position: relative;
  background: lightgray;
}

.box-orange {
  position: absolute;
  background: orange;
  width: 100px;
  height: 100px;
  right: 5px;    // 5px relative to the most-right of parent
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*AEX5fn8t0MJZCo4Lx52Uaw.png)

### 4. Fixed

Like `position: absolute`, fixed positioned elements are also removed from the normal document flow. The differences are:

* They are **only relative to the <html> document,** not any other parents.
* They are **not affected by scrolling**.

```css
.container {
  position: relative;
  background: lightgray;
}

.box-orange {
  position: fixed;
  background: orange;
  width: 100px;
  height: 100px;
  right: 5px;    // 5px relative to the most-right of parent
}
```

Here in the example, I change the orange box’s position to **fixed**, and this time it is relative 5px to the right of the **<html>**, not its **parent (container)**:

%[https://codepen.io/cem_eygi/pen/EebjaB]

As we can see, scrolling the page doesn’t affect the **fixed** positioned box. It is not relative to its parent (container) anymore.

### 5. Sticky

`position: sticky` can be explained as a mix of `position: relative` and `position: fixed`.

It behaves until a declared point like `position: relative`, after that it changes its behavior to `position: fixed` . The best way to explain **position: sticky** is by an example:

%[https://codepen.io/cem_eygi/pen/RYjrWz]

**IMPORTANT:** Position Sticky is not supported in Internet Explorer and earlier versions of other browsers. **You can check the browser support at [caniuse.com](https://caniuse.com).**

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Ekran-Resmi-2019-10-04-23.09.24.png)
_Browser Support for Position:sticky_

---

The best way to understand the CSS Position Property is by practice. Keep coding until you have a better understanding. If something is not clear, I will answer your questions below in the comments section.

**If you want to learn more about web development, feel free to** [**follow me on Youtube**](https://www.youtube.com/channel/UC1EgYPCvKCXFn8HlpoJwY3Q)**!**

Thank you for reading!

