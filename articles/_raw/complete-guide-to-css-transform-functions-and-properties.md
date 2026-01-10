---
title: CSS Transform Handbook – Complete Guide to CSS Transform Functions and Properties
subtitle: ''
author: Oluwatobi Sofela
co_authors: []
series: null
date: '2023-06-19T21:13:33.000Z'
originalURL: https://freecodecamp.org/news/complete-guide-to-css-transform-functions-and-properties
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1738338625918/27521e84-35de-4453-a153-1d419e1d0e2b.png
tags:
- name: code
  slug: code
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'CSS transform allows you to translate, rotate, skew, scale, or add perspective
  effects to HTML elements.

  This tutorial discusses everything you need to know to transform HTML elements like
  a pro.

  Table of Contents


  What is the CSS transform Property?...'
---

**CSS transform** allows you to translate, rotate, skew, scale, or add perspective effects to HTML elements.

This tutorial discusses everything you need to know to transform HTML elements like a pro.

## Table of Contents

1. [What is the CSS `transform` Property?](#heading-what-is-the-css-transform-property)
    
2. [What is the CSS `rotate()` Function?](#heading-what-is-the-css-rotate-function)
    
3. [What is the CSS `rotateX()` Function?](#heading-what-is-the-css-rotatex-function)
    
4. [What is the CSS `rotateY()` Function?](#heading-what-is-the-css-rotatey-function)
    
5. [What is the CSS `rotateZ()` Function?](#heading-what-is-the-css-rotatez-function)
    
6. [What is the CSS `rotate3d()` Function?](#heading-what-is-the-css-rotate3d-function)
    
7. [CSS Rotate Functions vs. `rotate` Property: What's the Difference?](#heading-css-rotate-functions-vs-rotate-property-whats-the-difference)
    
8. [What is the CSS `scale()` Function?](#heading-what-is-the-css-scale-function)
    
9. [CSS `scale()` Function vs. `scale` Property: What's the Difference?](#heading-css-scale-function-vs-scale-property-whats-the-difference)
    
10. [What is the CSS `scaleZ()` Function?](#heading-what-is-the-css-scalez-function)
    
11. [What is the CSS `scale3d()` Function?](#heading-what-is-the-css-scale3d-function)
    
12. [What is the CSS `skew()` Function?](#heading-what-is-the-css-skew-function)
    
13. [What is the CSS `translate()` Function?](#heading-what-is-the-css-translate-function)
    
14. [What is the CSS `translateZ()` Function?](#heading-what-is-the-css-translatez-function)
    
15. [What is the CSS `translate3d()` Function?](#heading-what-is-the-css-translate3d-function)
    
16. [CSS Translate Functions vs. `translate` Property: What's the Difference?](#heading-css-translate-functions-vs-translate-property-whats-the-difference)
    
17. [What is the CSS `perspective()` Function?](#heading-what-is-the-css-perspective-function)
    
18. [CSS `perspective()` Function vs. `perspective` Property: What's the Difference?](#heading-css-perspective-function-vs-perspective-property-whats-the-difference)
    
19. [What is the CSS `matrix()` Function?](#heading-what-is-the-css-matrix-function)
    
20. [Why Does the CSS Transform Functions' Order Matter?](#heading-why-does-the-css-transform-functions-order-matter)
    
21. [Tools for Converting Transform Functions to `matrix()`](#heading-tools-for-converting-transform-functions-to-matrix)
    
22. [Important Stuff to Know about Transforming Elements in CSS](#heading-important-stuff-to-know-about-transforming-elements-in-css)
    
23. [Wrapping Up](#heading-wrapping-up)
    

So, without further ado, let's discuss the CSS `transform` property.

## What Is the CSS `transform` Property?

The CSS `transform` property specifies the transformational effect you wish to apply to an HTML element.

**Here's the syntax:**

```css
html-element {
  transform: value;
}
```

The CSS `transform` property accepts the following values:

* `inherit`: Transforms the element with its parent element's `transform` value.
    
* `initial`: Transforms the HTML element with its default `transform` value.
    
* `matrix()`: Transforms the element two-dimensionally with a matrix of six values.
    
* `matrix3d()`: Transforms the HTML element three-dimensionally with a 4x4 matrix of sixteen values.
    
* `none`: Applies *no* transformation to the HTML element.
    
* `perspective()`: Transforms a 3D transformed element with a perspective view.
    
* `rotate()`: Transforms the element by rotating it two-dimensionally.
    
* `rotate3d()`: Transforms the element by rotating it three-dimensionally.
    
* `rotateX()`: Transforms the element by rotating it three-dimensionally along the X-axis.
    
* `rotateY()`: Transforms the element by rotating it three-dimensionally along the Y-axis.
    
* `rotateZ()`: Transforms the HTML element by rotating it three-dimensionally along the Z-axis.
    
* `scale()`: Transforms the element by scaling it two-dimensionally.
    
* `scale3d()`: Transforms the element by scaling it three-dimensionally.
    
* `scaleX()`: Transforms the element by scaling it along the X-axis.
    
* `scaleY()`: Transforms the element by scaling it along the Y-axis.
    
* `scaleZ()`: Transforms the HTML element by scaling it three-dimensionally along the Z-axis.
    
* `skew()`: Transforms the element by skewing it two-dimensionally along the X- and Y-axis.
    
* `skewX()`: Transforms the element by skewing it two-dimensionally along the X-axis.
    
* `skewY()`: Transforms the element by skewing it two-dimensionally along the Y-axis.
    
* `translate()`: Transforms the HTML element by translating (moving) it two-dimensionally.
    
* `translate3d()`: Transforms the element by translating it three-dimensionally.
    
* `translateX()`: Transforms the element by translating it along the X-axis.
    
* `translateY()`: Transforms the element by translating it along the Y-axis.
    
* `translateZ()`: Transforms the element by translating it three-dimensionally along the Z-axis.
    

**Note:** The `transform` property accepts one or more [CSS transform functions](https://codesweetly.com/web-tech-terms-c#css-transform-functions). For instance, here's a valid `transform` declaration:

```css
div {
  transform: perspective(370px) scaleZ(5) rotate(17deg);
}
```

In the snippet above, we assigned three transform functions to the `transform` property. Let's talk more about some of `transform`'s values.

## What is the CSS `rotate()` Function?

`rotate()` transforms an element by rotating it two-dimensionally around a fixed point.

**Note:**

* "Transform origin" is the fixed point around which an element rotates.
    
* You can define your element's fixed point using the CSS [`transform-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin) property. But the default is `center`.
    

### Syntax of the CSS `rotate()` function

`rotate()` accepts a single [argument](https://codesweetly.com/javascript-arguments-vs-parameters). Here is the syntax:

```css
element {
  transform: rotate(angle);
}
```

**Note the following:**

* The `rotate(angle)` function is equivalent to `rotate3d(0, 0, 1, angle)` or `rotateZ(angle)`.
    
* The `angle` argument specifies the element's angle of rotation.
    
* `angle` can be in [degrees](https://en.wikipedia.org/wiki/Degree_%28angle%29), [gradians](https://en.wikipedia.org/wiki/Gradian), [radians](https://en.wikipedia.org/wiki/Radian), or [turns](https://en.wikipedia.org/wiki/Turn_\(angle\)).
    
* An `angle` argument consists of a number followed by the unit you wish to use—for instance, `45deg`.
    
* Your browser's writing direction determines the element's direction of rotation.
    
* A positive angle will rotate the element clockwise in a left-to-right writing direction. But a negative angle will do a counterclockwise rotation.
    
* A positive angle will rotate the element counterclockwise in a right-to-left writing context. But a negative angle will do a clockwise rotation.
    

### Examples of the CSS `rotate()` function

Below are some examples of how the CSS `rotate()` function works.

#### How to do a zero-degree rotation in CSS:

```css
img {
  transform: rotate(0deg);
  width: 80%;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-zcgvaa?file=style.css)

The snippet above used the `rotate()` function to specify a zero-degree (0⁰) rotation for the image element.

#### How to do a 45-degree rotation in CSS:

```css
img {
  transform: rotate(45deg);
  width: 80%;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-86xhmx?file=style.css)

The snippet above used the `rotate()` function to specify a forty-five-degree (45⁰) rotation for the image element.

#### How to do a negative seventy-degree rotation in CSS:

```css
img {
  transform: rotate(-70deg);
  width: 80%;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-3gb1my?file=style.css)

The snippet above used the `rotate()` function to specify a negative seventy-degree (70⁰) rotation for the image element.

## What is the CSS `rotateX()` Function?

`rotateX()` transforms an element by rotating it three-dimensionally around the X-axis.

![Illustration of the 3D Cartesian coordinate system](https://www.freecodecamp.org/news/content/images/2023/06/cartesian-coordinate-system-three-dimensional-diagram-codesweetly.png align="left")

*A three-dimensional Cartesian coordinate system showing the X-, Y-, and Z-axis*

### Syntax of the CSS `rotateX()` function

`rotateX()` accepts a single argument. Here is the syntax:

```css
element {
  transform: rotateX(angle);
}
```

**Note the following:**

* The `rotateX(angle)` function is equivalent to `rotate3d(1, 0, 0, angle)`.
    
* The `angle` argument specifies the element's angle of rotation.
    
* `angle` can be in degree, gradian, radian, or turn.
    
* An `angle` argument consists of a number followed by the unit you wish to use—for instance, `45deg`.
    

### Examples of the CSS `rotateX()` function

Below are some examples of how the CSS `rotateX()` function works.

#### How to do a zero-degree rotation around the X-axis:

```css
img {
  transform: rotateX(0deg);
  width: 80%;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-ej9ent?file=style.css)

The snippet above used the `rotateX()` function to specify a zero-degree (0⁰) rotation for the image around the X-axis.

#### How to do a 70-degree rotation around the X-axis:

```css
img {
  transform: rotateX(70deg);
  width: 80%;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-fvhyjx?file=style.css)

The snippet above used the `rotateX()` function to specify a seventy-degree (70⁰) rotation for the image around the X-axis.

## What is the CSS `rotateY()` Function?

`rotateY()` transforms an element by rotating it three-dimensionally around the Y-axis.

### Syntax of the CSS `rotateY()` function

`rotateY()` accepts a single argument. Here is the syntax:

```css
element {
  transform: rotateY(angle);
}
```

**Note the following:**

* The `rotateY(angle)` function is equivalent to `rotate3d(0, 1, 0, angle)`.
    
* The `angle` argument specifies the element's angle of rotation.
    
* `angle` can be in degrees, gradians, radians, or turns.
    
* An `angle` argument consists of a number followed by the unit you wish to use—for instance, `45deg`.
    

### Examples of the CSS `rotateY()` function

Below are some examples of how the CSS `rotateY()` function works.

#### How to do a zero-degree rotation around the Y-axis:

```css
img {
  transform: rotateY(0deg);
  width: 80%;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-frg3ks?file=style.css)

The snippet above used the `rotateY()` function to specify a zero-degree (0⁰) rotation for the image around the Y-axis.

#### How to do a 70-degree rotation around the Y-axis:

```css
img {
  transform: rotateY(70deg);
  width: 80%;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-yvydga?file=style.css)

The snippet above used the `rotateY()` function to specify a seventy-degree (70⁰) rotation for the image around the Y-axis.

## What is the CSS `rotateZ()` Function?

`rotateZ()` transforms an element by rotating it three-dimensionally around the Z-axis.

### Syntax of the CSS `rotateZ()` function

`rotateZ()` accepts a single argument. Here is the syntax:

```css
element {
  transform: rotateZ(angle);
}
```

**Note the following:**

* The `rotateZ(angle)` function is equivalent to `rotate3d(0, 0, 1, angle)` or `rotate(angle)`.
    
* The `angle` argument specifies the element's angle of rotation.
    
* `angle` can be in degrees, gradians, radians, or turns.
    
* An `angle` argument consists of a number followed by the unit you wish to use—for instance, `45deg`.
    

### Examples of the CSS `rotateZ()` function

Below are some examples of how the CSS `rotateZ()` function works.

#### How to do a zero-degree rotation around the Z-axis:

```css
img {
  transform: rotateZ(0deg);
  width: 80%;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-ozqupq?file=style.css)

The snippet above used the `rotateZ()` function to specify a zero-degree (0⁰) rotation for the image around the Z-axis.

#### How to do a 70-degree rotation around the Z-axis:

```css
img {
  transform: rotateZ(70deg);
  width: 80%;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-g6qrwc?file=style.css)

The snippet above used the `rotateZ()` function to specify a seventy-degree (70⁰) rotation for the image around the Z-axis.

## What is the CSS `rotate3d()` Function?

`rotate3d()` transforms an element by rotating it three-dimensionally around the x-, y-, and z-axis.

### Syntax of the CSS `rotate3d()` function

`rotate3d()` accepts four arguments. Here is the syntax:

```css
element {
  transform: rotate3d(x, y, z, angle);
}
```

**Note the following:**

* The `x`, `y`, and `z` arguments are numbers specifying the x-, y-, and z-coordinates.
    
* The coordinates are the axis around which the element will rotate.
    
* The `angle` argument specifies the element's angle of rotation.
    
* `angle` can be in degrees, gradians, radians, or turns.
    
* An `angle` argument consists of a number followed by the unit you wish to use—for instance, `45deg`.
    

### Examples of the CSS `rotate3d()` function

Below are some examples of how the CSS `rotate3d()` function works.

#### How to do a 70-degree rotation around the Z-axis:

```css
img {
  transform: rotate3d(0, 0, 1, 70deg);
  width: 80%;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-i6f9pr?file=style.css)

The snippet above used the `rotate3d()` function to specify a seventy-degree (70⁰) rotation for the image around the Z-axis.

#### How to do a 70-degree rotation around the X-, Y-, and Z-axis:

```css
img {
  transform: rotate3d(1, 1, 1, 70deg);
  width: 80%;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-ctws81?file=style.css)

The snippet above used the `rotate3d()` function to specify a seventy-degree (70⁰) rotation for the image around the x-, y-, and z-axis.

## CSS Rotate Functions vs. `rotate` Property: What's the Difference?

CSS rotate functions and CSS `rotate` property provides two similar ways to specify rotation transformations.

The main differences between the two rotation techniques are as follows:

* The CSS `rotate` property allows rotating an element without using the CSS `transform` property.
    
* The CSS `rotate` property's syntax is shorter than its function alternative.
    
* The CSS `rotate` property saves you from remembering the specific order to position the [transform functions](https://codesweetly.com/web-tech-terms-c#css-transform-functions).
    
* Browsers calculate the transform functions' matrix in the order you assigned them to the CSS `transform` property—from left to right.
    
* Browsers calculate the transform properties' matrix in the following [transformation matrix order](https://www.w3.org/TR/css-transforms-2/#ctm):
    
    1. `translate`
        
    2. `rotate`
        
    3. `scale`
        

Below are some examples.

### How to use CSS `rotate` property vs. function to do a 45-degree rotation

```css
img {
  rotate: 45deg; /* Equivalent to a transform: rotate(45deg) property */
  width: 80%;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-rdw9a5?file=style.css)

The snippet above used the `rotate` property to specify a forty-five-degree (45⁰) rotation for the image element.

### How to use CSS `rotate` property vs. function to do a 70-degree rotation around the X-axis

```css
img {
  rotate: x 70deg; /* Equal to a transform: rotateX(70deg) property */
  width: 80%;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-pal1am?file=style.css)

The snippet above used the `rotate` property to specify a seventy-degree (70⁰) rotation for the image around the X-axis.

### How to use CSS `rotate` property vs. function to do a 70-degree rotation around the Y-axis

```css
img {
  rotate: y 70deg; /* Equal to a transform: rotateY(70deg) property */
  width: 80%;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-ldnmfd?file=style.css)

The snippet above used the `rotate` property to specify a seventy-degree (70⁰) rotation for the image around the Y-axis.

### How to use CSS `rotate` property vs. function to do a 70-degree rotation around the Z-axis

```css
img {
  rotate: z 70deg; /* Equal to a transform: rotateZ(70deg) property */
  width: 80%;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-stf9ty?file=style.css)

The snippet above used the `rotate` property to specify a seventy-degree (70⁰) rotation for the image around the Z-axis.

### How to use CSS `rotate` property vs. function to do a 70-degree rotation around the X-, Y-, and Z-axis

```css
img {
  rotate: 1 1 1 70deg; /* Equal to a transform: rotate3d(1, 1, 1, 70deg) property */
  width: 80%;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-qfflxq?file=style.css)

The snippet above used the `rotate` property to specify a seventy-degree (70⁰) rotation for the image around the x-, y-, and z-axis.

**Note:** A `none` value tells browsers *not* to rotate the selected element.

## What is the CSS `scale()` Function?

`scale()` transforms an element by resizing (scaling) it two-dimensionally from a fixed point.

**Note:**

* "Transform origin" is the fixed point from which the computer scales an element.
    
* You can define your element's fixed point using the CSS `transform-origin` property. But the default is `center`.
    

### Syntax of the CSS `scale()` function

`scale()` accepts two arguments. Here is the syntax:

```css
element {
  transform: scale(x, y);
}
```

**Note the following:**

* The `x` argument can be a number or percentage. It specifies the element's scaling factor along the x-axis.
    
* The `y` argument can also be a number or percentage. It defines the element's scaling factor along the y-axis.
    
* Y-axis' default value is `x`. Therefore, if you do not provide a `y` argument, the browser automatically uses `x`'s value.
    
* Suppose `x` and `y` are equal. In that case, browsers will scale your element uniformly and preserve its aspect ratio.
    

![Illustration of the 2D Cartesian coordinate system](https://www.freecodecamp.org/news/content/images/2023/06/cartesian-coordinate-system-two-dimensional-diagram-codesweetly.png align="left")

*A two-dimensional Cartesian coordinate system showing the X- and Y-axis*

### Examples of the CSS `scale()` function

Below are some examples of how the CSS `scale()` function works.

#### How to scale an element uniformly along the X- and Y-axis in CSS:

```css
img {
  transform: scale(0.3);
  transform-origin: left;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-k3d6nm?file=style.css)

The snippet above used the `scale()` function to specify a `0.3` scaling factor for the image element along the X- and Y-axis.

**Note:**

* `scale(0.3)` is equivalent to `scale(0.3, 0.3)`.
    
* The percentage equivalence of `scale(0.3)` is `scale(30%)`.
    

#### How to scale an element non-uniformly along the X- and Y-axis in CSS:

```css
img {
  transform: scale(0.3, 65%);
  transform-origin: top left;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-fxjhwb?file=style.css)

The snippet above used the `scale()` function to specify a `0.3` scaling factor for the image along the X-axis and `65%` along the Y-axis.

#### How to scale an element along only the X-axis:

```css
img {
  transform: scale(0.3, 1);
  transform-origin: top left;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-7mwvto?file=style.css)

The snippet above used the `scale()` function to specify a `0.3` scaling factor for the image along only the X-axis.

**Note:**

* A scale factor of `1` or `100%` tells browsers *not* to apply any scaling effect on the selected element.
    
* `scale(0.3, 1)` is equivalent to `scaleX(0.3)`.
    

#### How to scale an element along only the Y-axis:

```css
img {
  transform: scale(100%, 0.2);
  transform-origin: top left;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-i5yrt4?file=style.css)

The snippet above used the `scale()` function to specify a `0.2` scaling factor for the image along only the Y-axis.

**Note:**

* A `100%` or `1` scale factor tells browsers *not* to apply any scaling effect on the selected element.
    
* `scale(100%, 0.2)` is equivalent to `scaleY(0.2)`.
    

## CSS `scale()` Function vs. `scale` Property: What's the Difference?

The CSS `scale()` function and the CSS `scale` property provide two similar ways to specify a scale transformation.

The main differences between the two scaling techniques are as follows:

* The CSS `scale` property allows scaling an element without using the CSS `transform` property.
    
* The CSS `scale` property's syntax is shorter than its function alternative.
    
* The CSS `scale` property saves you from remembering the specific order to position the transform functions.
    
* Browsers calculate the transform functions' matrix in the order you assigned them to the CSS `transform` property—from left to right.
    
* Browsers calculate the transform properties' matrix in the following order:
    
    1. `translate`
        
    2. `rotate`
        
    3. `scale`
        

**Here's an example:**

Use the CSS `scale` property to scale an element nonuniformly along the X- and Y-axis.

```css
img {
  scale: 0.3 65%; /* Equal to a transform: scale(0.3, 65%) property */
  transform-origin: top left;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-exkib5?file=style.css)

The snippet above used the `scale` property to specify a `0.3` scaling factor for the image along the X-axis and `65%` along the Y-axis.

**Note:** A `none` value tells browsers *not* to scale the selected element.

## What is the CSS `scaleZ()` Function?

`scaleZ()` transforms an element by resizing (scaling) it three-dimensionally from a fixed point along the z-axis.

**Note:**

* "Transform origin" is the fixed point from which the computer scales an element.
    
* You can define your element's fixed point using the CSS `transform-origin` property. But the default is `center`.
    

### Syntax of the CSS `scaleZ()` function

`scaleZ()` accepts a single argument. Here is the syntax:

```css
element {
  transform: scaleZ(number);
}
```

**Note:**

* The `scaleZ(number)` function is equivalent to `scale3d(1, 1, number)`.
    
* The `number` argument specifies the element's scaling factor along the z-axis.
    

### Examples of the CSS `scaleZ()` function

We often use `scaleZ()` with other CSS functions such as `perspective()`, `translateZ()`, and `rotateX()`. Below are some examples.

#### How to use `scaleZ()` with CSS `perspective()` and `rotateX()` functions:

```css
img {
  transform: perspective(370px) scaleZ(5) rotateX(17deg);
  width: 80%;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-kqmccz?file=style.css)

Here's what we did in the snippet above:

1. We used the `perspective()` function to define a `370px` distance between the user and the [z=0 plane](https://codesweetly.com/css-perspective-function#what-is-the-z0-plane).
    
2. The `scaleZ()` function specifies a scale factor of `5` for the image along the z-axis.
    
3. We used the `rotateX()` function to rotate the image seventeen-degree (17⁰) around the x-axis.
    

**Note:**

* List `perspective()` first whenever you chain it with other [CSS transform functions](https://codesweetly.com/web-tech-terms-c#css-transform-functions). Otherwise, browsers might transform the selected element incorrectly.
    
* List the `scaleZ()` function before `rotateX()`. Otherwise, the browser will *not* scale the element.
    

#### How to use `scaleZ()` with CSS `perspective()` and `translateZ()` functions:

```css
img {
  width: 40%;
}

.second-image {
  transform: perspective(370px) scaleZ(5) translateZ(30px);
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-uyw767?file=style.css)

Here's what we did in the snippet above:

1. We used the `perspective()` function to define a `370px` distance between the user and the z=0 plane.
    
2. The `scaleZ()` function specifies a scale factor of `5` for the image along the z-axis.
    
3. We used the `translateZ()` function to reposition the `second-image` thirty pixels (`30px`) away from its original position along the z-axis.
    

## What is the CSS `scale3d()` Function?

`scale3d()` transforms an element by resizing (scaling) it three-dimensionally from a fixed point along the x-, y-, and z-axis.

**Note:**

* "Transform origin" is the fixed point from which the computer scales an element.
    
* You can define your element's fixed point using the CSS `transform-origin` property. But the default is `center`.
    

### Syntax of the CSS `scale3d()` function

`scale3d()` accepts three arguments. Here is the syntax:

```css
element {
  transform: scale3d(x, y, z);
}
```

The `x`, `y`, and `z` arguments are numbers specifying the x-, y-, and z-coordinates. The coordinates are the axis along which browsers will scale the element.

### Examples of the CSS `scale3d()` function

Below are some examples of how the CSS `scale3d()` function works.

#### How to use `scale3d()` with CSS `perspective()` and `rotateX()` functions:

```css
img {
  transform: perspective(370px) scale3d(1, 1, 5) rotateX(17deg);
  width: 80%;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-inndft?file=style.css)

Here's what we did in the snippet above:

1. We used the `perspective()` function to define a `370px` distance between the user and the z=0 plane.
    
2. The `scale3d()` function specifies a scale factor of `1`, `1`, and `5` for the image along the x-, y-, and z-axis.
    
3. We used the `rotateX()` function to rotate the image seventeen-degrees (17⁰) around the x-axis.
    

**Note:**

* A scale factor of `1` will apply *no* scaling effect on the element.
    
* List `perspective()` first whenever you chain it with other CSS transform functions. Otherwise, browsers might transform the selected element incorrectly.
    
* List the `scale3d()` function before `rotateX()`. Otherwise, the browser will *not* scale the element.
    

#### How to scale elements three-dimensionally:

```css
img {
  width: 40%;
}

.second-image {
  transform: scale3d(5, 3, 0.05);
  transform-origin: top left;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-hq8kbr?file=style.css)

We used the `scale3d()` function to specify a scale factor of `5`, `3`, and `0.05` for the image along the x-, y-, and z-axis.

## What is the CSS `skew()` Function?

`skew()` transforms an element by slanting (skewing) it two-dimensionally around a fixed point.

**Note:**

* "Transform origin" is the fixed point from which the computer skews an element.
    
* You can define your element's fixed point using the CSS `transform-origin` property. But the default is `center`.
    

### Syntax of the CSS `skew()` function

`skew()` accepts two arguments. Here is the syntax:

```css
element {
  transform: skew(aX, aY);
}
```

**Note the following:**

* The `aX` argument specifies the element's skewing angle along the x-axis.
    
* The `aY` argument specifies the element's skewing angle along the y-axis.
    
* `aX` and `aY` can be in degrees, gradians, radians, or turns.
    
* An `angle` argument consists of a number followed by the unit you wish to use—for instance, `45deg`.
    
* `aY` is an optional argument.
    

### Examples of the CSS `skew()` function

Below are some examples of how the CSS `skew()` function works.

#### How to skew an element along only the X-axis:

```css
img {
  transform: skew(30deg);
  transform-origin: top;
  width: 80%;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-gx5dy4?file=style.css)

The snippet above used the `skew()` function to apply a thirty-degree (30⁰) slant on the image along only the x-axis.

**Note:** `skew(30deg)` is equivalent to `skewX(30deg)`.

#### How to skew an element along only the Y-axis:

```css
img {
  transform: skew(0, 40deg);
  transform-origin: top left;
  width: 80%;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-nbkjfj?file=style.css)

The snippet above used the `skew()` function to apply a forty-degree (40⁰) slant on the image along only the y-axis.

**Note:**

* A zero (`0`) skew degree tells browsers *not* to apply any skewing effect on the selected element.
    
* `skew(0, 40deg)` is equivalent to `skewY(40deg)`.
    

#### How to skew an element along the X- and Y-axis:

```css
img {
  transform: skew(30deg, 40deg);
  transform-origin: top left;
  width: 80%;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-ofrk9v?file=style.css)

The snippet above used the `skew()` function to apply a thirty-degree (30⁰) slant on the image along the x-axis. And forty-degree (40⁰) along the y-axis.

## What is the CSS `translate()` Function?

`translate()` transforms an element by repositioning (translating) it two-dimensionally.

### Syntax of the CSS `translate()` function

`translate()` accepts two arguments. Here is the syntax:

```css
element {
  transform: translate(x, y);
}
```

**Note the following:**

* The `x` argument can be a length or percentage value. It specifies the distance you wish to move the element from its original x-axis position.
    
* The `y` argument can be a length or percentage value. It defines the distance you wish to move the element from its original y-axis position.
    
* `y` is an optional argument.
    

### Examples of the CSS `translate()` function

Below are some examples of how the CSS `translate()` function works.

#### How to translate an element along only the X-axis:

```css
img {
  transform: translate(150px);
  width: 80%;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-kuaqzz?file=style.css)

The snippet above used the `translate()` function to reposition the image `150px` away from its original position along the x-axis.

You can also write it like this, specifying the `X`:

```css
img {
  transform: translateX(150px);
  width: 80%
```

**Note:** `translate(150px)` is equivalent to `translateX(150px)`.

#### How to translate an element along only the Y-axis:

```css
img {
  transform: translate(0, 55%);
  width: 80%;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-2bchbd?file=style.css)

The snippet above used the `translate()` function to reposition the image `55%` away from its original position along the y-axis.

**Note:**

* A zero (`0`) translate distance tells browsers *not* to apply any translating effect on the selected element.
    
* `translate(0, 55%)` is equivalent to `translateY(55%)`.
    

#### How to translate an element along the X- and Y-axis:

```css
img {
  transform: translate(60%, 300px);
  width: 80%;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-uwpvu4?file=style.css)

The snippet above used the `translate()` function to reposition the image `60%` away from its original position along the x-axis and `300px` from its y-axis.

## What is the CSS `translateZ()` Function?

`translateZ()` transforms an element by repositioning (translating) it three-dimensionally along the z-axis.

![Illustration of the 3D Cartesian coordinate system](https://www.freecodecamp.org/news/content/images/2023/06/cartesian-coordinate-system-three-dimensional-diagram-codesweetly-1.png align="left")

*A three-dimensional Cartesian coordinate system showing the X-, Y-, and Z-axis*

### Syntax of the CSS `translateZ()` function

`translateZ()` accepts a single argument. Here is the syntax:

```css
element {
  transform: translateZ(length);
}
```

The `length` argument specifies the distance you wish to move the element from its original z-axis position.

![Illustration of the CSS translateZ's length argument](https://www.freecodecamp.org/news/content/images/2023/06/cartesian-coordinate-system-three-dimensional-length-diagram-codesweetly.png align="left")

*A three-dimensional Cartesian coordinate system with a red arrow defining the green plane's translateZ length*

### Examples of the CSS `translateZ()` function

We often use `translateZ()` with the `perspective()` function. Below are some examples.

#### How to use `translateZ()` with the CSS `perspective()` function:

```css
img {
  width: 40%;
}

.second-image {
  transform: perspective(33px) translateZ(10px);
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-hvf8bb?file=style.css)

Here's what we did in the snippet above:

1. We used the `perspective()` function to define a `33px` distance between the user and the [z=0 plane](https://codesweetly.com/css-perspective-function#what-is-the-z0-plane).
    
2. We used the `translateZ()` function to reposition the `second-image` ten pixels (`10px`) away from its original position along the z-axis.
    

**Note:**

* Suppose the `second-image`'s z-axis position is larger than or equal to the `perspective()` function's [argument](https://codesweetly.com/javascript-arguments-vs-parameters). In that case, the image will disappear as though it is behind the user. In other words, the selected item disappears when the user is in the same position as the element (or when the element is behind the user).
    
* The larger the user's distance to the element's z-axis position, the less intensive the perspective effect will be, and vice-versa.
    

#### How to use `translateZ()` with a `70px` perspective:

```css
img {
  width: 40%;
}

.second-image {
  transform: perspective(70px) translateZ(10px);
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-vqd7mm?file=style.css)

Here's what we did in the snippet above:

1. We used the `perspective()` function to define a `70px` distance between the user and the z=0 plane.
    
2. We used the `translateZ()` function to reposition the `second-image` ten pixels (`10px`) away from its original position along the z-axis.
    

## What is the CSS `translate3d()` Function?

`translate3d()` transforms an element by repositioning (translating) it three-dimensionally along the x-, y-, and z-axis.

### Syntax of the CSS `translate3d()` function

`translate3d()` accepts three arguments. Here is the syntax:

```css
element {
  transform: translate3d(x, y, z);
}
```

**Note the following:**

* The `x` argument can be a length or percentage value. It specifies the distance you wish to move the element from its original x-axis position.
    
* The `y` argument can be a length or percentage value. It defines the distance you wish to move the element from its original y-axis position.
    
* `z` can only be a length—not a percentage. It defines the distance you wish to move the element from its original z-axis position.
    

### Examples of the CSS `translate3d()` function

Below are some examples of how the CSS `translate3d()` function works.

#### How to translate an element along only the X-axis

```css
img {
  transform: translate3d(150px, 0, 0);
  width: 80%;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-qrxxmx?file=style.css)

The snippet above used the `translate3d()` function to reposition the image `150px` away from its original position along the x-axis.

**Note:** `translate3d(150px, 0, 0)` is equivalent to `translateX(150px)`.

#### How to translate elements three-dimensionally:

```css
img {
  width: 40%;
}

.second-image {
  transform: perspective(300px) translate3d(15%, 45%, 200px);
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-rksery?file=style.css)

The snippet above used the `translate3d()` function to reposition the image `15%` away from its original position along the x-axis, `45%` from its y-axis, and `200px` from its z-axis.

## CSS Translate Functions vs. `translate` Property: What's the Difference?

The CSS translate functions and the CSS `translate` property provide two similar ways to specify a translation transformation.

The main differences between the two translation techniques are as follows:

* The CSS `translate` property allows translating an element without using the CSS `transform` property.
    
* The CSS `translate` property's syntax is shorter than its function alternative.
    
* The CSS `translate` property saves you from remembering the specific order to position the transform functions.
    
* Browsers calculate the transform functions' matrix in the order you assigned them to the CSS `transform` property—from left to right.
    
* Browsers calculate the transform properties' matrix in the following order:
    
    1. `translate`
        
    2. `rotate`
        
    3. `scale`
        

Below are some examples.

### How to use CSS `translate` property vs. function to translate an element along the X- and Y-axis

```css
img {
  translate: 60% 300px; /* Equal to a transform: translate(60%, 300px) property */
  width: 80%;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-mhrmbj?file=style.css)

The snippet above used the `translate` property to reposition the image `60%` away from its original position along the x-axis. And `300px` from its y-axis.

**Note:** Suppose you wish to translate an element along the z-axis. In that case, set a `perspective` property on the "parent element" of the element you want to translate. Otherwise, the element will not move along its z-axis.

### How to use CSS `translate` property vs. function to translate an element along the Z-axis

```css
img {
  width: 40%;
}

div {
  perspective: 35px;
}

.second-image {
  translate: 0px 0px 17px; /* Equal to a transform: translateZ(17px) property */
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-gjr5sl?file=style.css)

Here's what we did in the snippet above:

1. We used the `perspective` property to define a `35px` distance between the user and the z=0 plane.
    
2. We used the `translate` property to reposition the `second-image` seventeen pixels (`17px`) away from its original position along the z-axis.
    

### How to use CSS `translate` property vs. function to translate an element three-dimensionally

```css
img {
  width: 40%;
}

div {
  perspective: 300px;
}

.second-image {
  translate: 50% 25% 200px; /* Equal to a transform: translate3d(50%, 25%, 200px) property */
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-pgqrgc?file=style.css)

The snippet above used the `translate` property to reposition the image `50%` away from its original position along the x-axis, `25%` from its y-axis, and `200px` from its z-axis.

**Note:** A `none` value tells browsers *not* to translate the selected element.

## What is the CSS `perspective()` Function?

`perspective()` transforms an element by adding some perspective effects to it.

### Syntax of the CSS `perspective()` function

`perspective()` accepts only one argument. Here is the syntax:

```css
element {
  transform: perspective(length);
}
```

The `length` argument specifies the user's distance to the [z=0 plane](https://codesweetly.com/css-perspective-function#what-is-the-z0-plane).

![Illustration of the CSS perspective() method](https://www.freecodecamp.org/news/content/images/2023/06/cartesian-coordinate-system-perspective-method-illustration-codesweetly.png align="left")

*A three dimensional Cartesian coordinate system with a red arrow defining the distance between the user and the z=0 plane*

### Examples of the CSS `perspective()` function

We often use `perspective()` with other CSS functions such as `translateZ()`, `rotateX()`, and `rotateY()`. Below are some examples.

#### How to use `perspective()` with the CSS `translateZ()` function:

```css
img {
  width: 40%;
}

.second-image {
  transform: perspective(33px) translateZ(10px);
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-hvf8bb?file=style.css)

Here's what we did in the snippet above:

1. We used the `perspective()` function to define a `33px` distance between the user and the z=0 plane.
    
2. We used the `translateZ()` function to reposition the `second-image` ten pixels (`10px`) away from its original position along the z-axis.
    

**Note the following:**

* Suppose the `second-image`'s z-axis position is larger than or equal to the `perspective()` function's argument. In that case, the image will disappear as though it is behind the user. In other words, the selected item disappears when the user is in the same position as the element (or when the element is behind the user).
    
* The larger the user's distance to the element's z-axis position, the less intensive the perspective effect will be, and vice-versa.
    

#### How to use `perspective()` with the CSS `rotateY()` function:

```css
img {
  width: 40%;
}

.second-image {
  transform: perspective(33px) rotateY(-10deg);
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-tptutx?file=style.css)

Here's what we did in the snippet above:

1. We used the `perspective()` function to define a `33px` distance between the user and the z=0 plane.
    
2. We used the `rotateY()` function to rotate the `second-image` negative ten-degree (-10⁰) around the y-axis.
    

#### How to use `perspective()` with the CSS `rotateX()` function:

```css
img {
  width: 40%;
}

.second-image {
  transform: perspective(33px) rotateX(17deg);
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-8ddydv?file=style.css)

Here's what we did in the snippet above:

1. We used the `perspective()` function to define a `33px` distance between the user and the z=0 plane.
    
2. We used the `rotateX()` function to rotate the `second-image` seventeen-degree (17⁰) around the x-axis.
    

## CSS `perspective()` Function vs. `perspective` Property: What's the Difference?

The CSS `perspective()` function and the `perspective` property provide two similar ways to add perspective effects to HTML elements.

The main differences between the two perspective techniques are as follows:

* We apply the `perspective()` function "directly on the element" we want to add some perspective effects to.
    
* We apply the `perspective` property "on the parent element" of the element we want to add some perspective effects to.
    
* The `perspective()` function works as a `transform` property's value.
    
* The CSS `perspective` property allows you to create perspective effects without using the CSS `transform` property.
    

**Here's an example:**

Use CSS `perspective` property to add perspective effect to a child element:

```css
img {
  width: 40%;
}

div {
  perspective: 33px;
}

.second-image {
  rotate: x 17deg;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-psssbh?file=style.css)

Here's what we did in the snippet above:

1. We used the `perspective` property to define a `33px` distance between the user and the z=0 plane.
    
2. We used the `rotate` property to rotate the `second-image` seventeen-degree (17⁰) around the x-axis.
    

**Note:**

* The CSS `perspective` property saves you from remembering the specific order to position the transform functions.
    
* A `none` value tells browsers *not* to add any perspective effect to the selected element's children.
    

## What is the CSS `matrix()` Function?

The CSS `matrix()` function is a shorthand for the following 2D transform functions:

* `scaleX()`
    
* `skewY()`
    
* `skewX()`
    
* `scaleY()`
    
* `translateX()`
    
* `translateY()`
    

In other words, instead of writing:

```css
img {
  transform-origin: 0 0;
  transform: translateX(100px) translateY(250px) scaleX(2) scaleY(0.9)
    skewX(10deg) skewY(35deg);
  width: 80%;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-jquhyy?file=style.css)

You can alternatively use the `matrix()` function to shorten your code like so:

```css
img {
  transform-origin: 0 0;
  transform: matrix(2.24693, 0.630187, 0.352654, 0.9, 100, 250);
  width: 80%;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-zzlwhn?file=style.css)

### The CSS `matrix()` function's syntax

The `matrix()` function accepts six values. Here's the syntax:

```css
matrix(scaleX(), skewY(), skewX(), scaleY(), translateX(), translateY())
```

You can represent the CSS matrix's values as [homogeneous coordinates](https://en.wikipedia.org/wiki/Homogeneous_coordinates) on [ℝℙ<sup>2</sup>](https://en.wikipedia.org/wiki/Real_projective_space) like so:

```txt
| scX skX tX | ← x-axis
| skY scY tY | ← y-axis
|  0   0   1 | ← constants
```

**Note the following:**

* `scX` and `skX` are numbers describing an element's scale and skew linear transformation on the x-axis.
    
* `tX` is a number representing an element's translation on the x-axis.
    
* `skY` and `scY` are numbers describing an element's skew and scale linear transformation on the y-axis.
    
* `tY` is a number representing an element's translation on the y-axis.
    
* `0`, `0`, `1` are constants.
    
* We do not pass the constants as [arguments](https://codesweetly.com/javascript-arguments-vs-parameters) to the `matrix()` function because the computer implies them automatically.
    

### Examples of the CSS `matrix()` function

Below are some examples of the CSS `matrix()` function.

#### How to convert `scaleX()` to `matrix()` function:

Consider the following `transform` property:

```css
img {
  transform-origin: 0 0;
  transform: scaleX(2);
  width: 80%;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-9r2euo?file=style.css)

Here is the `matrix()` equivalent of the above `scaleX()` function:

```css
img {
  transform-origin: 0 0;
  transform: matrix(2, 0, 0, 1, 0, 0); /* scX, skY, skX, scY, tX, tY */
  width: 80%;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-bypfbf?file=style.css)

Let's also represent the matrix's values as homogeneous coordinates on ℝℙ<sup>2</sup>:

```txt
| 2 0 0 | ← x-axis
| 0 1 0 | ← y-axis
| 0 0 1 | ← constants
```

Below is another example.

#### How to convert `translateY()` to `matrix()` function:

```css
img {
  transform-origin: 0 0;
  transform: translateY(250px);
  width: 80%;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-w25f3w?file=style.css)

Here is the `matrix()` equivalent of the above `translateY()` function:

```css
img {
  transform-origin: 0 0;
  transform: matrix(1, 0, 0, 1, 0, 250); /* scX, skY, skX, scY, tX, tY */
  width: 80%;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-1coxrt?file=style.css)

Let's also represent the matrix's values as homogeneous coordinates on ℝℙ<sup>2</sup>:

```txt
| 1 0 0   | ← x-axis
| 0 1 250 | ← y-axis
| 0 0 1   | ← constants
```

Below is a third example.

#### How to convert `translateX()` and `scale()` to `matrix()` function:

```css
img {
  transform-origin: 0 0;
  transform: translateX(100px) scale(2);
  width: 80%;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-wje2fa?file=style.css)

Here is the syntax for converting the above `transform` property's value to `matrix()`:

```txt
matrix = (translateX's homogeneous coordinates) x (scale's homogeneous coordinates)
```

Let's begin the conversion by defining `translateX(100px)`'s homogeneous coordinates:

```txt
| 1 0 100 | ← x-axis
| 0 1 0   | ← y-axis
| 0 0 1   | ← constants
```

Let's also define `scale(2)`'s homogeneous coordinates:

```txt
| 2 0 0 | ← x-axis
| 0 2 0 | ← y-axis
| 0 0 1 | ← constants
```

It's now time to multiply the two homogeneous coordinates by using the following syntax:

```txt
| a d g |   | j m p |   | aj + dk + gl   am + dn + go   ap +dq  + gr |
| b e h | x | k n q | = | bj + ek + hl   bm + en + ho   bp + eq + hr |
| c f i |   | l o r |   | cj + fk + il   cm + fn + io   cp + fq + ir |
```

Let's implement the above syntax like so:

```txt
| 1 0 100 |   | 2 0 0 |   | 2 + 0 + 0   0 + 0 + 0   0 + 0 + 100 |
| 0 1  0  | x | 0 2 0 | = | 0 + 0 + 0   0 + 2 + 0   0 + 0 +  0  |
| 0 0  1  |   | 0 0 1 |   | 0 + 0 + 0   0 + 0 + 0   0 + 0 +  1  |
```

The next step is to resolve the addition. So, let's do that now.

```txt
| 1 0 100 |   | 2 0 0 |   | 2 0 100 |
| 0 1  0  | x | 0 2 0 | = | 0 2  0  |
| 0 0  1  |   | 0 0 1 |   | 0 0  1  |
```

The addition's result above gives us the homogeneous coordinates of the `transform: translateX(100px) scale(2)` property.

In other words, the product of `(translateX's homogeneous coordinates)` and `(scale's homogeneous coordinates)` equal:

```txt
| 2 0 100 | ← x-axis
| 0 2  0  | ← y-axis
| 0 0  1  | ← constants
```

Therefore, the matrix equivalence of `transform: translateX(100px) scale(2)` is `transform: matrix(2, 0, 0, 2, 100, 0)`.

```css
img {
  transform-origin: 0 0;
  transform: matrix(2, 0, 0, 2, 100, 0);
  width: 80%;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-njrg4k?file=style.css)

Please note that `transform: translateX(100px) scale(2)` and `transform: scale(2) translateX(100px)` return different matrixes. Let's see an example of the second arrangement below.

#### How to convert `scale()` and `translateX()` to `matrix()` function:

Consider the following `transform` property:

```css
img {
  transform-origin: 0 0;
  transform: scale(2) translateX(100px);
  width: 80%;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-39trog?file=style.css)

Here is the syntax for converting the above `transform` property's value to `matrix()`:

```txt
matrix = (scale's homogeneous coordinates) x (translateX's homogeneous coordinates)
```

Let's begin the conversion by defining `scale(2)`'s homogeneous coordinates:

```txt
| 2 0 0 | ← x-axis
| 0 2 0 | ← y-axis
| 0 0 1 | ← constants
```

Let's also define `translateX(100px)`'s homogeneous coordinates:

```txt
| 1 0 100 | ← x-axis
| 0 1  0  | ← y-axis
| 0 0  1  | ← constants
```

It's now time to multiply the two homogeneous coordinates by using the following syntax:

```txt
| a d g |   | j m p |   | aj + dk + gl   am + dn + go   ap +dq  + gr |
| b e h | x | k n q | = | bj + ek + hl   bm + en + ho   bp + eq + hr |
| c f i |   | l o r |   | cj + fk + il   cm + fn + io   cp + fq + ir |
```

Let's implement the above syntax like so:

```txt
| 2 0 0 |   | 1 0 100 |   | 2 + 0 + 0   0 + 0 + 0   200 + 0 + 0 |
| 0 2 0 | x | 0 1  0  | = | 0 + 0 + 0   0 + 2 + 0    0 + 0 + 0  |
| 0 0 1 |   | 0 0  1  |   | 0 + 0 + 0   0 + 0 + 0    0 + 0 + 1  |
```

The next step is to resolve the addition. So, let's do that now.

```txt
| 2 0 0 |   | 1 0 100 |   | 2 0 200 |
| 0 2 0 | x | 0 1  0  | = | 0 2  0  |
| 0 0 1 |   | 0 0  1  |   | 0 0  1  |
```

The addition's result above gives us the homogeneous coordinates of the `transform: scale(2) translateX(100px)` property.

In other words, the product of `(scale's homogeneous coordinates)` and `(translateX's homogeneous coordinates)` equal:

```txt
| 2 0 200 | ← x-axis
| 0 2  0  | ← y-axis
| 0 0  1  | ← constants
```

Therefore, the matrix equivalence of `transform: scale(2) translateX(100px)` is `transform: matrix(2, 0, 0, 2, 200, 0)`.

```css
img {
  transform-origin: 0 0;
  transform: matrix(2, 0, 0, 2, 200, 0);
  width: 80%;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-3m4vgk?file=style.css)

Notice that `transform: scale(2) translateX(100px)` equals `transform: matrix(2, 0, 0, 2, 200, 0)`. And `transform: translateX(100px) scale(2)` is equivalent to `transform: matrix(2, 0, 0, 2, 100, 0)`.

In other words, the order in which you write the transform functions matters. Let's discuss more on this below.

## Why Does the CSS Transform Functions' Order Matter?

The order in which you write [CSS transform functions](https://codesweetly.com/web-tech-terms-c#css-transform-functions) matters because of the way browsers calculate the matrix's values.

For instance, consider the following snippet:

```css
div {
  position: absolute;
  width: 100px;
  height: 100px;
  transform-origin: 0 0;
}

.red {
  border: 3px solid red;
  background-color: rgba(255, 0, 0, 0.5);
}

.green {
  border: 3px solid green;
  background-color: rgba(0, 128, 0, 0.5);
  transform: translateX(100px) scale(2);
}

.blue {
  border: 3px solid blue;
  background-color: rgba(0, 0, 255, 0.5);
  transform: scale(2) translateX(100px);
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-rvkagy?file=style.css)

The only difference between the green and the blue `div`s is the order in which we wrote their transform functions.

However, the computer translated the two containers using different values (`100px` for the green `div` and `200px` for the blue one).

So, why did the transform functions' order affect the `div`s' translation values? Here's the reason:

* Browsers multiply each transform function's homogeneous coordinates in order—from left to right.
    

In other words, the computer used the following syntax to compute the green `div`'s matrix:

* [Green `div`'s matrix](#how-to-convert-translatex-and-scale-to-matrix-function) = (translateX's homogeneous coordinates) x (scale's homogeneous coordinates)
    

And it used the following syntax to calculate the blue `div`'s matrix:

* [Blue `div`'s matrix](#how-to-convert-scale-and-translatex-to-matrix-function) = (scale's homogeneous coordinates) x (translateX's homogeneous coordinates)
    

Therefore, the position of the transform functions determined the matrix's [arguments](https://codesweetly.com/javascript-arguments-vs-parameters) because browsers began the calculation in order from the leftmost function to the right.

Knowing how to convert transform functions to `matrix()` is beneficial. And having some conversion tools can come in handy. So, let's discuss some helpful tools you can use.

## Tools for Converting Transform Functions to `matrix()`

The two tools you can use to do a quick conversion of transform functions to `matrix()` are:

* JavaScript's `window.getComputedStyle()` method
    
* Eric Meyer and Aaron Gustafson's matrix resolution tool
    

### How to use `window.getComputedStyle()` to convert transform functions to `matrix()`

Suppose you want to convert the following transform functions to matrix:

```css
img {
  transform-origin: 0 0;
  transform: scale(2) translateX(100px);
  width: 80%;
}
```

You will add an `id` attribute to the image element:

```html
<img
  src="https://cdn.pixabay.com/photo/2022/09/26/23/26/african-american-7481724_960_720.jpg"
  alt=""
  id="image"
/>
```

Then, in JavaScript, you will:

1. Use the `id` attribute to get the image element.
    
2. Use the [`window.getComputedStyle()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/getComputedStyle) method to get the image's `transform` property's value.
    

**Here's the code:**

```js
// Get the image element by its id name:
const image = document.getElementById("image");

// Get the image element's transform property's value:
const matrix = window.getComputedStyle(image).getPropertyValue("transform");

// Log the matrix variable's value to the console:
console.log(matrix);
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-39trog?devToolsHeight=33&file=index.js)

Browsers, by default, convert a CSS `transform` property's value to its matrix equivalent. So, the snippet above returned the image's computed value.

Let's now discuss the second conversion tool.

### How to use the matrix resolutions tool to convert transform functions to `matrix()`

Suppose you want to convert the following transform functions to a `matrix()`:

```css
img {
  transform-origin: 0 0;
  transform: scale(2) translateX(100px);
  width: 80%;
}
```

You will do the following:

1. Go to The Matrix Resolutions website: [https://meyerweb.com/eric/tools/matrix/](https://meyerweb.com/eric/tools/matrix/).
    
2. Paste your transform functions (`scale(2) translateX(100px)`) into the first text field.
    
3. Click "The Red Pill" button to generate the transform functions' matrix equivalence.
    

![The matrix resolutions tool's screenshot](https://www.freecodecamp.org/news/content/images/2023/06/how-to-use-the-matrix-resolutions-tool-codesweetly.jpg align="left")

*Click the red pill button to convert CSS transform functions to a matrix() function*

**Tip:** Use [matrix3d()](https://codesweetly.com/css-matrix3d-function) to create a 3D transformation matrix.

## Important Stuff to Know about Transforming Elements in CSS

Here are three essential facts to remember when you transform elements in CSS.

### 1\. Transform creates a stacking context

Suppose you set the `transform` property to any value other than `none`. In that case, the browser will create a [stacking context](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Positioning/Understanding_z_index/The_stacking_context). And the transformed element will serve as a [containing block](https://developer.mozilla.org/en-US/docs/Web/CSS/Containing_block) to any [absolute](https://codesweetly.com/css-position-property#what-is-position-absolute-in-css) or [fixed](https://codesweetly.com/css-position-property#what-is-position-fixed-in-css) positioned elements it contains.

### 2\. Scaling and zooming animations cause accessibility issues

Whenever you include scaling or zooming animations in your app, provide users an option to turn off animations. This option is necessary because scaling and zooming animations cause [accessibility issues](https://developer.mozilla.org/en-US/docs/Web/CSS/transform#accessibility_concerns).

### 3\. Not all elements are transformable

You cannot transform the following [box models](https://codesweetly.com/css-box-model):

* [Non-replaced](https://codesweetly.com/css-transform-property#non-replaced-vs-replaced-elements-whats-the-difference) inline elements
    
* [table-column](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/col) boxes
    
* [table-column-group](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/colgroup)
    

## Wrapping Up

In this article, we discussed all the CSS transform tools you need to translate, rotate, skew, scale, or add perspective effects to HTML elements.

I hope you've found this article helpful.

### Thanks for reading!

If you like this tutorial, you will enjoy my [CSS Flexbox book](https://amzn.to/3N3XUws). It is a handy quick reference guide that uses images and live examples to explain Flexbox.

[![Get CodeSweetly's CSS Flexbox book at Amazon](https://www.freecodecamp.org/news/content/images/2023/06/css-flexbox-book-get-banner-codesweetly.png align="left")](https://amzn.to/3N3XUws)
