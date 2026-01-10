---
title: CSS Opacity Property and Image Opacity Explained
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-13T18:08:00.000Z'
originalURL: https://freecodecamp.org/news/css-opacity
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9eb9740569d1a4ca3eb6.jpg
tags:
- name: CSS
  slug: css
seo_title: null
seo_desc: 'The opacity property controls how opaque an element is on a scale of 0.0
  to 1.0. The lower the value, the more transparent the element is.

  You can choose up to what extent you want to make the element transparent. You have
  to add the following CSS pr...'
---

The `opacity` property controls how opaque an element is on a scale of 0.0 to 1.0. The lower the value, the more transparent the element is.

You can choose up to what extent you want to make the element transparent. You have to add the following CSS property to achieve the transparency levels.

**Fully Opaque**

```css
.class-name {
  opacity: 1;
}

/* OR */

.class-name {
  opacity: 1.0;
}
```

**Semitransparent**

```css
.class-name {
  opacity: 0.5;
}
```

**Fully t**ransparent****

```css
.class-name {
  opacity: 0;
}

/* OR */

.class-name {
  opacity: 0.0;
}
```

Alternatively, you can use `rgba` to set the opacity of an element:

```css
.class-name{
  background-color: rgba(0, 0, 0, .5);
}
```

This sets the `background-color` of an element to black with 50% opacity. The last value in an `rgba` value is the _alpha value_. An alpha value of 1 is equal to 100% opacity, and 0.5 (or .5 like above) is equal to 50% opacity.

## **Image Opacity and Transparency**

The `opacity` property allows you to make an image transparent by lowering how opaque it is.

`Opacity` takes a value between 0.0 and 1.0.

1.0 is the default value for any image. It is fully opaque.

Example

```css
img {
    opacity: 0.3;
 }
```

Include `filter: alpha(opacity=x)` for IE8 and earlier. The x takes a value from 0-100.

```css
img {
   opacity: 0.3;
   filter: alpha(opacity=30);
}
```

Here’s an example of an image set to the parameters in the example above.

![image at 30% opacity](https://github.com/lvcoulter/images/blob/master/Opacity30percent.jpg?raw=true)

You can pair `opacity` with `:hover` to create a dynamic mouse-over effect.

Example:

```css
img {
    opacity: 0.3;
    filter: alpha(opacity=30);
}
img:hover {
   opacity: 1.0;
   filter: alpha(opacity=100);
}
```

[A codepen example to show a transparent image turning opaque on hover](https://codepen.io/lvcoulter/full/JrzxXa/)

You can create the opposite effect with less code since the image is 1.0 opacity by default

Example:

```css
img:hover {
   opacity: 0.3;
   filter: alpha(opacity=30);
}
```

Here's a [codepen example to show transparency on mouse-over](https://codepen.io/lvcoulter/full/xXBQoR/).

## More about CSS

### **Cascading Style Sheets (CSS)**

CSS is an acronym for Cascading Style Sheets. It was first invented in 1996, and is now a standard feature of all major web browsers.

CSS allows developers to control how web pages look by “styling” the HTML structure of that page.

CSS specifications are maintained by the [World Wide Web Consortium (W3C)](https://www.w3.org/).

You can build some pretty amazing things in CSS alone, such as this pure-CSS [Minesweeper game](https://codepen.io/bali_balo/pen/BLJONk) (which uses no JavaScript).

