---
title: 'Z Index in CSS: What it Is and What it Does'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-11T23:17:00.000Z'
originalURL: https://freecodecamp.org/news/z-index-in-css-what-it-is-and-what-it-does
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c9f740569d1a4ca3342.jpg
tags:
- name: CSS
  slug: css
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'What is a Z Index?

  Z Index (z-index) is a CSS property that defines the order of overlapping HTML elements.
  Elements with a higher index will be placed on top of elements with a lower index.

  Note: Z index only works on positioned elements (position:a...'
---

## **What is a Z Index?**

Z Index (`z-index`) is a CSS property that defines the order of overlapping HTML elements. Elements with a higher index will be placed on top of elements with a lower index.

**Note**: Z index only works on positioned elements (`position:absolute`, `position:relative`, or `position:fixed`).

#### **Possible Values**

```css
/* Default value if not specified */
z-index: auto;

/* Integer values */
z-index: 1;
z-index: 100;
z-index: 9999;
z-index: -1;

/* Global values */
z-index: inherit;
z-index: initial;
z-index: unset;
```

## How to use the Z Index

In this example, you can see three boxes displayed on top of each other in different orders using `z-index`.

*HTML*

```html
<div class="container">
  <div class="box" id="blue"></div>
  <div class="box" id="red"></div>
  <div class="box" id="green"></div>
</div>
```

*CSS*

```css
#blue {
  background-color: blue;
}

#red {
  background-color: red;
}

#green {
  background-color: green;
}
```

Since `z-index` wasn’t defined, it will have a default value of `auto`. This is a result:

![An image of three boxes, with blue in the back, red in the middle, and green in front.](https://cdn.hashnode.com/res/hashnode/image/upload/v1731048763410/8f4d61b3-332f-42f0-be9d-7d14c3dbb818.png align="center")

Try to change the order to Green, Blue, Red in CSS using `z-index`.

```css
#blue {
  background-color: blue;
  z-index: 2;
}

#red {
  background-color: red;
  z-index: 1;
}

#green {
  background-color: green;
  z-index: 3;
}
```

Your result will be:

![An image of three boxes, with red in the back, blue in the middle, and green in front.](https://cdn.hashnode.com/res/hashnode/image/upload/v1731048856409/96a9d38e-f200-4468-9515-e080662c5173.png align="center")

Use Z Index if you need to put a background element below a container. You can easily place the background under every element by giving it a negative Z Index like below:

```css
#background {
  z-index: -1;
}
```
