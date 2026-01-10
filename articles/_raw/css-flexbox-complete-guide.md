---
title: CSS Flexbox Explained – Complete Guide to Flexible Containers and Flex Items
subtitle: ''
author: Oluwatobi Sofela
co_authors: []
series: null
date: '2022-10-28T14:28:24.000Z'
originalURL: https://freecodecamp.org/news/css-flexbox-complete-guide
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/css-flexbox-complete-guide-codesweetly-pexels-chris-f-6664375.jpg
tags:
- name: CSS
  slug: css
- name: flexbox
  slug: flexbox
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'CSS Flexbox gives you the tools to create basic and advanced website layouts
  in flexible and responsive ways.

  This tutorial discusses everything you need to know to use Flexbox like a pro.

  Table of Contents


  What Is Flexbox?

  Flex Container vs. Flex I...'
---

CSS Flexbox gives you the tools to create basic and advanced website layouts in flexible and responsive ways.

This tutorial discusses everything you need to know to use Flexbox like a pro.

## Table of Contents

1. [What Is Flexbox?](#heading-what-is-flexbox)
2. [Flex Container vs. Flex Item: What's the Difference?](#heading-flex-container-vs-flex-item-whats-the-difference)
3. [What Is a `flex` Value in CSS?](#heading-what-is-a-flex-value-in-css)
4. [What Is an `inline-flex` Value in CSS?](#heading-what-is-an-inline-flex-value-in-css)
5. [Properties for Specifying Flexbox's Layout](#heading-properties-for-specifying-flexboxs-layout)
6. [What Are the Flexible Containers Properties?](#heading-what-are-the-flexible-containers-properties)
7. [What Is Flexbox's `flex-direction` Property?](#heading-what-is-flexboxs-flex-direction-property)
8. [What Is Flexbox's `flex-wrap` Property?](#heading-what-is-flexboxs-flex-wrap-property)
9. [What Is Flexbox's `flex-flow` Property?](#heading-what-is-flexboxs-flex-flow-property)
10. [What Is Flexbox's `justify-content` Property?](#heading-what-is-flexboxs-justify-content-property)
11. [What Is Flexbox's `align-items` Property?](#heading-what-is-flexboxs-align-items-property)
12. [What Is Flexbox's `align-content` Property?](#heading-what-is-flexboxs-align-content-property)
13. [What Are the Flexible Items Properties?](#what-are-the-flexible-items-properties)
14. [What Is Flexbox's `align-self` Property?](#heading-what-is-flexboxs-align-self-property)
15. [What Is Flexbox's `order` Property?](#heading-what-is-flexboxs-order-property)
16. [What Is Flexbox's `flex-grow` Property?](#heading-what-is-flexboxs-flex-grow-property)
17. [What Is Flexbox's `flex-shrink` Property?](#heading-what-is-flexboxs-flex-shrink-property)
18. [What Is Flexbox's `flex-basis` Property?](#heading-what-is-flexboxs-flex-basis-property)
19. [What Is Flexbox's `flex` Property?](#heading-what-is-flexboxs-flex-property)
20. [How to Center Elements Horizontally with Flexbox](#heading-how-to-center-elements-horizontally-with-flexbox)
21. [How to Center Elements Vertically with Flexbox](#heading-how-to-center-elements-vertically-with-flexbox)
22. [How to Center Elements Horizontally and Vertically with Flexbox](#heading-how-to-center-elements-horizontally-and-vertically-with-flexbox)
23. [Overview](#heading-overview)

So, without any further ado, let's understand what Flexbox is.

## What Is Flexbox?

**Flexbox** makes browsers display selected HTML elements as flexible [box models](https://codesweetly.com/css-box-model).

Flexbox allows easy resizing and repositioning of a flexible container and its items one-dimensionally.

**Note:**

* "One-dimensionally" means Flexbox allows laying out box models in a row or column at a time. In other words, Flexbox cannot lay out box models in a row and column at the same time.
* Flexbox is sometimes called a flexible box layout module.
* Use the [grid layout module](https://codesweetly.com/css-grid-explained) if you need to resize and reposition elements two-dimensionally.

## Flex Container vs. Flex Item: What's the Difference?

A **flex container** is an [HTML element](https://codesweetly.com/web-tech-terms-h#html-element) whose [`display`](https://codesweetly.com/css-display-property) property's value is `flex` or `inline-flex`.

**Flex items** are the direct children of a flex container.

![Illustration of a flex container and a flex item](https://www.freecodecamp.org/news/content/images/2022/10/css-flex-container-flex-item-illustration-codesweetly.png)
_A flex container (the large yellow area in the image) is an HTML element whose display property's value is flex or inline-flex. Flex items (the smaller boxes within the yellow container) are the direct children of a flex container._

## What Is a `flex` Value in CSS?

`flex` tells browsers to display the selected HTML element as a block-level flexible box model.

In other words, setting an element's `display` property's value to `flex` turns the box model into a [block-level](https://developer.mozilla.org/en-US/docs/Web/HTML/Block-level_elements) flexbox.

**Here's an example:**

```css
section {
  display: flex;
  background-color: orange;
  margin: 10px;
  padding: 7px;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-gctvuc?file=style.css)

The snippet above used the `flex` value to convert the HTML document's `<section>` elements from regular `<section>` nodes to block-level flexible box models.

**Note:**

* Converting an HTML node to a flexible box model makes the element's direct children become flexible items.
* The `display: flex` directive only affects a box model and its direct children. It does not affect grandchildren nodes.

Let's now discuss `inline-flex`.

## What Is an `inline-flex` Value in CSS?

`inline-flex` tells browsers to display the selected HTML element as an inline-level flexible box model.

In other words, setting an element's `display` property's value to `inline-flex` turns the box model into an [inline-level](https://developer.mozilla.org/en-US/docs/Web/HTML/Inline_elements) flexbox.

**Here's an example:**

```css
section {
  display: inline-flex;
  background-color: orange;
  margin: 10px;
  padding: 7px;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-ksagv8?file=style.css)

The snippet above used the `inline-flex` value to convert the HTML document's `<section>` elements from regular `<section>` nodes to inline-level flexible box models.

**Note:**

* Converting an HTML node to a flexible box model makes the element's direct children become flexible items.
* The `display: inline-flex` directive only affects a box model and its direct children. It does not affect grandchildren nodes.

## Properties for Specifying Flexbox's Layout

On converting a regular HTML element to a `flex` (or `inline-flex`) box model, Flexbox provides two categories of properties for positioning the flexible box and its direct children:

* Flexible containers properties
* Flexible items properties

## What Are the Flexible Containers Properties?

A flexible container's properties specify how browsers should layout items within the flexible box model.

**Note:** We define a flexible container's property on the flex container, not its items.

The six (6) types of flex container properties are:

* `flex-direction`
* `flex-wrap`
* `flex-flow`
* `justify-content`
* `align-items`
* `align-content`

Let's discuss the six types now.

## What Is Flexbox's `flex-direction` Property?

**flex-direction** tells browsers the specific direction (row or column) they should lay out a flexible container's direct children.

In other words, `flex-direction` defines a flexbox's [main axis](https://codesweetly.com/css-flex-direction-property#main-axis-vs-cross-axis-whats-the-difference).

![Illustration of a flexbox's main and cross-axis](https://www.freecodecamp.org/news/content/images/2022/10/css-flexbox-main-axis-cross-axis-illustration-codesweetly.png)
_A Flexbox's main axis is the layout orientation defined by a flex-direction property. Its cross axis is the perpendicular orientation to the main axis._

**Here's an example:**

```css
section {
  display: flex;
  flex-direction: column;
  background-color: orange;
  margin: 10px;
  padding: 7px;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-jtpqir?file=style.css)

The snippet above organized the flexible `<section>` containers' items in the column direction of your browser's default language.

**Tip:** Use `flex-direction: column-reverse` (or `flex-direction: row-reverse`) to reverse the browser's layout direction.

## What Is Flexbox's `flex-wrap` Property?

**flex-wrap** specifies whether browsers should wrap overflown flexible items onto multiple lines.

The `flex-wrap` property accepts the following values:

* `nowrap`
* `wrap`
* `wrap-reverse`

Let's discuss the three values.

### What is `flex-wrap: nowrap` in CSS flexbox?

`nowrap` is `flex-wrap`'s default value. It forces all items within a flexible container into a single line (that is, row-wise or column-wise direction).

In other words, `nowrap` tells browsers _not_ to wrap a flexible container's items.

**Note:** Suppose the total width (or height) of all the items in a flexible container is greater than the flexbox's width (or height). In such a case, `nowrap` will cause the elements to overflow out of the container.

**Here's an example:**

```css
section {
  width: 130px;
  display: flex;
  flex-wrap: nowrap;
  background-color: orange;
  margin: 10px;
  padding: 7px;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-yn6yw8?file=style.css)

The snippet above used `nowrap` to force browsers to lay out the flexible containers' items in a single line.

### What is `flex-wrap: wrap` in CSS flexbox?

`wrap` moves all overflow items within a flexible container to the next line.

In other words, `wrap` tells browsers to wrap a flexible container's overflow items.

**Here's an example:**

```css
section {
  width: 130px;
  display: flex;
  flex-wrap: wrap;
  background-color: orange;
  margin: 10px;
  padding: 7px;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-78ez1m?file=style.css)

We used `wrap` to wrap the flexible containers' overflow items to the next line.

### What is `flex-wrap: wrap-reverse` in CSS flexbox?

`wrap-reverse` moves all overflow items within a flexible container to the next line in reverse order.

**Note:** `wrap-reverse` does the same thing as `wrap`—but in reverse order.

**Here's an example:**

```css
section {
  width: 130px;
  display: flex;
  flex-wrap: wrap-reverse;
  background-color: orange;
  margin: 10px;
  padding: 7px;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-eyqxtf?file=style.css)

We used `wrap-reverse` to wrap the flexible containers' overflow items to the next line in reverse order.

## What Is Flexbox's `flex-flow` Property?

**flex-flow** is a shorthand for the `flex-direction` and `flex-wrap` properties.

In other words, instead of writing:

```css
section {
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
}
```

You can alternatively use the `flex-flow` property to shorten your code like so:

```css
section {
  display: flex;
  flex-flow: column wrap;
}
```

## What Is Flexbox's `justify-content` Property?

**justify-content** specifies how browsers should position a flexible container's items along the flexbox's [main axis](https://codesweetly.com/css-flex-direction-property#main-axis-vs-cross-axis-whats-the-difference).

The `justify-content` property accepts the following values:

* `flex-start`
* `center`
* `flex-end`
* `space-between`
* `space-around`
* `space-evenly`

Let's discuss these six values.

### What is `justify-content: flex-start` in CSS Flexbox?

`flex-start` is `justify-content`'s default value. It aligns a flexible container's items with the main-start edge of the flexbox's main axis.

![Illustration of justify-content's flex-start value](https://www.freecodecamp.org/news/content/images/2022/10/css-justify-content-flex-start-illustration-codesweetly.png)
_flex-start aligns a flexible container's items with the main-start side of the flexbox's main axis._

**Here's an example:**

```css
section {
  display: flex;
  justify-content: flex-start;
  background-color: orange;
  margin: 10px;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-ma7svj?file=style.css)

The snippet above used the `flex-start` value to align the flexible container's items to the flexbox's main-start edge.

### What is `justify-content: center` in CSS Flexbox?

`center` aligns a flexible container's items to the center of the flexbox's main axis.

![Illustration of justify-content's center value](https://www.freecodecamp.org/news/content/images/2022/10/css-justify-content-center-illustration-codesweetly.png)
_center aligns a flexible container's items to the center of the flexbox's main axis._

**Here's an example:**

```css
section {
  display: flex;
  justify-content: center;
  background-color: orange;
  margin: 10px;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-jfzcwc?file=style.css)

We used the `center` value to align the flexible container's items to the center of the flexbox.

### What is `justify-content: flex-end` in CSS Flexbox?

`flex-end` aligns a flexible container's items with the main-end side of the flexbox's main axis.

![Illustration of justify-content's flex-end value](https://www.freecodecamp.org/news/content/images/2022/10/css-justify-content-flex-end-illustration-codesweetly.png)
_flex-end aligns a flexible container's items with the main-end side of the flexbox's main axis._

**Here's an example:**

```css
section {
  display: flex;
  justify-content: flex-end;
  background-color: orange;
  margin: 10px;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-iyhlbr?file=style.css)

We used the `flex-end` value to align the flexible container's items to the flexbox's main-end side.

### What is `justify-content: space-between` in CSS Flexbox?

`space-between` does the following:

* It aligns a flexible container's first item with the main-start edge of the flexbox's main axis.
* It aligns the container's last item with the main-end edge of the flexbox's main axis.
* It creates even spacing between each pair of items between the first and last item.

![Illustration of justify-content's space-between value](https://www.freecodecamp.org/news/content/images/2022/10/css-justify-content-space-between-illustration-codesweetly.png)
_space-between creates even spacing between each pair of items between the first and last item._

**Here's an example:**

```css
section {
  display: flex;
  justify-content: space-between;
  background-color: orange;
  margin: 10px;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-dylovp?file=style.css)

The snippet above used the `space-between` value to create even spacing between each pair of items between the first and last flex item.

### What is `justify-content: space-around` in CSS Flexbox?

`space-around` assigns equal spacing to each side of a flexible container's items.

Therefore, the space before the first item and after the last element is half the width of the space between each pair of elements.

![Illustration of justify-content's space-around value](https://www.freecodecamp.org/news/content/images/2022/10/css-justify-content-space-around-illustration-codesweetly.png)
_space-around assigns equal spacing to each side of a flexible container's items._

**Here's an example:**

```css
section {
  display: flex;
  justify-content: space-around;
  background-color: orange;
  margin: 10px;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-t6wpcj?file=style.css)

The snippet above used the `space-around` value to assign equal spacing to each side of the flexible container's items.

### What is `justify-content: space-evenly` in CSS Flexbox?

`space-evenly` assigns even spacing to both ends of a flexible container and between its items.

![Illustration of justify-content's space-evenly value](https://www.freecodecamp.org/news/content/images/2022/10/css-justify-content-space-evenly-illustration-codesweetly.png)
_space-evenly assigns even spacing to both ends of a flexible container and between its items._

**Here's an example:**

```css
section {
  display: flex;
  justify-content: space-evenly;
  background-color: orange;
  margin: 10px;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-p67eh8?file=style.css)

We used the `space-evenly` value to assign even spacing to both ends of the flexbox and between its items.

Let's now discuss the fifth type of flexible container property.

## What Is Flexbox's `align-items` Property?

**align-items** specifies how browsers should position a flexible container's items along the [cross-axis](https://codesweetly.com/css-flex-direction-property#main-axis-vs-cross-axis-whats-the-difference) of the flexbox.

The `align-items` property accepts the following values:

* `stretch`
* `flex-start`
* `center`
* `flex-end`
* `baseline`

Let's discuss the five values.

### What is `align-items: stretch` in CSS Flexbox?

`stretch` is `align-items`' default value. It stretches a flexible container's items to fill the flexbox's cross-axis.

![Illustration of align-items' stretch value](https://www.freecodecamp.org/news/content/images/2022/10/css-align-items-stretch-illustration-codesweetly.png)
_stretch stretches a flexible container's items to fill the flexbox's cross-axis._

**Here's an example:**

```css
section {
  display: flex;
  align-items: stretch;
  background-color: orange;
  margin: 10px;
  height: 300px;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-ezugee?file=style.css)

The snippet above used the `stretch` value to stretch the flexible items to fill the `<section>`'s cross-axis.

### What is `align-items: flex-start` in CSS Flexbox?

`flex-start` aligns a flexible container's items with the cross-start edge of the flexbox's cross-axis.

![Illustration of align-items' flex-start value](https://www.freecodecamp.org/news/content/images/2022/10/css-align-items-flex-start-illustration-codesweetly.png)
_flex-start aligns a flexible container's items with the cross-start edge of the flexbox's cross-axis._

**Here's an example:**

```css
section {
  display: flex;
  align-items: flex-start;
  background-color: orange;
  margin: 10px;
  height: 300px;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-cjzhj2?file=style.css)

We used the `flex-start` value to align the flexible items to the cross-start edge of the `<section>`'s cross-axis.

### What is `align-items: center` in CSS Flexbox?

`center` aligns a flexible container's items to the center of the flexbox's cross-axis.

![Illustration of align-items' center value](https://www.freecodecamp.org/news/content/images/2022/10/css-align-items-center-illustration-codesweetly.png)
_center aligns a flexible container's items to the center of the flexbox's cross-axis._

**Here's an example:**

```css
section {
  display: flex;
  align-items: center;
  background-color: orange;
  margin: 10px;
  height: 300px;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-ywexqr?file=style.css)

The snippet above used the `center` value to align the flexible items to the center of the `<section>`'s cross-axis.

### What is `align-items: flex-end` in CSS Flexbox?

`flex-end` aligns a flexible container's items with the cross-end edge of the flexbox's cross-axis.

![Illustration of align-items' flex-end value](https://www.freecodecamp.org/news/content/images/2022/10/css-align-items-flex-end-illustration-codesweetly.png)
_flex-end aligns a flexible container's items with the cross-end edge of the flexbox's cross-axis._

**Here's an example:**

```css
section {
  display: flex;
  align-items: flex-end;
  background-color: orange;
  margin: 10px;
  height: 300px;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-bwdeyz?file=style.css)

We used the `flex-end` value to align the flexible items to the cross-end edge of the `<section>`'s cross-axis.

### What is `align-items: baseline` in CSS Flexbox?

`baseline` aligns a flexible container's items with the [baseline](https://stackoverflow.com/a/34611670/11841906) of the flexbox's cross-axis.

![Illustration of align-items' baseline value](https://www.freecodecamp.org/news/content/images/2022/10/css-align-items-baseline-illustration-codesweetly.png)
_baseline aligns a flexible container's items with the baseline of the flexbox's cross-axis._

**Here's an example:**

```css
section {
  display: flex;
  align-items: baseline;
  background-color: orange;
  margin: 10px;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-xxvj57?file=style.css)

The snippet above used the `baseline` value to align the flexible items to the `<section>`'s baseline.

Now, let's talk about the sixth CSS flexible container property type.

## What Is Flexbox's `align-content` Property?

**align-content** specifies how browsers should position a flexible container's lines along the flexbox's [cross-axis](https://codesweetly.com/css-flex-direction-property#main-axis-vs-cross-axis-whats-the-difference).

**Note:** The `align-content` property does not affect a flexbox with only one line—for instance, a flexible container with `flex-wrap: nowrap`. In other words, `align-content` works only on flexboxes with multiple lines.

The `align-content` property accepts the following values:

* `stretch`
* `flex-start`
* `center`
* `flex-end`
* `space-between`
* `space-around`
* `space-evenly`

Let's discuss the seven values.

### What is `align-content: stretch` in CSS Flexbox?

`stretch` is `align-content`'s default value. It stretches the flexible container's lines to fill the flexbox's cross-axis.

![Illustration of align-content's stretch value](https://www.freecodecamp.org/news/content/images/2022/10/css-align-content-stretch-illustration-codesweetly.png)
_stretch stretches the flexible container's lines to fill the flexbox's cross-axis._

**Here's an example:**

```css
section {
  display: flex;
  flex-wrap: wrap;
  align-content: stretch;
  background-color: orange;
  margin: 10px;
  width: 90px;
  height: 500px;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-dway6n?file=style.css)

The snippet above used the `stretch` value to stretch the flexbox's lines to fill the `<section>`'s cross-axis.

### What is `align-content: flex-start` in CSS Flexbox?

`flex-start` aligns a flexible container's lines with the cross-start edge of the flexbox's cross-axis.

![Illustration of align-content's flex-start value](https://www.freecodecamp.org/news/content/images/2022/10/css-content-flex-start-illustration-codesweetly.png)
_flex-start aligns a flexible container's lines with the cross-start edge of the flexbox's cross-axis._

**Here's an example:**

```css
section {
  display: flex;
  flex-wrap: wrap;
  align-content: flex-start;
  background-color: orange;
  margin: 10px;
  width: 90px;
  height: 500px;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-c9pzbc?file=style.css)

The snippet above used the `flex-start` value to align the flexbox's lines to the cross-start edge of the `<section>`'s cross-axis.

### What is `align-content: center` in CSS Flexbox?

`center` aligns a flexible container's lines to the center of the flexbox's cross-axis.

![Illustration of align-content's center value](https://www.freecodecamp.org/news/content/images/2022/10/css-align-content-center-illustration-codesweetly.png)
_center aligns a flexible container's lines to the center of the flexbox's cross-axis._

**Here's an example:**

```css
section {
  display: flex;
  flex-wrap: wrap;
  align-content: center;
  background-color: orange;
  margin: 10px;
  width: 90px;
  height: 500px;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-j3poyu?file=style.css)

We used the `center` value to align the flexbox's lines to the center of the `<section>`'s cross-axis.

### What is `align-content: flex-end` in CSS Flexbox?

`flex-end` aligns a flexible container's lines with the cross-end edge of the flexbox's cross-axis.

![Illustration of align-content's flex-end value](https://www.freecodecamp.org/news/content/images/2022/10/css-align-content-flex-end-illustration-codesweetly.png)
_flex-end aligns a flexible container's lines with the cross-end edge of the flexbox's cross-axis._

**Here's an example:**

```css
section {
  display: flex;
  flex-wrap: wrap;
  align-content: flex-end;
  background-color: orange;
  margin: 10px;
  width: 90px;
  height: 500px;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-cmaz6z?file=style.css)

We used the `flex-end` value to align the flexbox's lines to the cross-end edge of the `<section>`'s cross-axis.

### What is `align-content: space-between` in CSS Flexbox?

`space-between` does the following:

* It aligns the flexbox's first line with the main-start edge of the flexible container's main axis.
* It aligns the flexbox's last line with the main-end side of the flexible container's main axis.
* It creates equal spacing between each pair of lines between the first and last line.

![Illustration of align-content's space-between value](https://www.freecodecamp.org/news/content/images/2022/10/css-align-content-space-between-illustration-codesweetly.png)
_space-between creates equal spacing between each pair of lines between the first and last line_

**Here's an example:**

```css
section {
  display: flex;
  flex-wrap: wrap;
  align-content: space-between;
  background-color: orange;
  margin: 10px;
  width: 90px;
  height: 500px;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-kltdwx?file=style.css)

The snippet above used the `space-between` value to create equal spacing between each pair of lines between the first and last line.

### What is `align-content: space-around` in CSS Flexbox?

`space-around` assigns equal spacing to each side of a flexible container's lines.

Therefore, the space before the first line and after the last one is half the width of the space between each pair of lines.

![Illustration of align-content's space-around value](https://www.freecodecamp.org/news/content/images/2022/10/css-align-content-space-around-illustration-codesweetly.png)
_space-around assigns equal spacing to each side of a flexible container's lines._

**Here's an example:**

```css
section {
  display: flex;
  flex-wrap: wrap;
  align-content: space-around;
  background-color: orange;
  margin: 10px;
  width: 90px;
  height: 500px;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-kx9gdy?file=style.css)

The snippet above used the `space-around` value to assign equal spacing to each side of the flexible container's lines.

### What is `align-content: space-evenly` in CSS Flexbox?

`space-evenly` assigns even spacing to both ends of a flexible container and between its lines.

![Illustration of align-content's space-evenly value](https://www.freecodecamp.org/news/content/images/2022/10/css-align-content-space-evenly-illustration-codesweetly.png)
_space-evenly assigns even spacing to both ends of a flexible container and between its lines._

**Here's an example:**

```css
section {
  display: flex;
  flex-wrap: wrap;
  align-content: space-evenly;
  background-color: orange;
  margin: 10px;
  width: 90px;
  height: 500px;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-eevqoj?file=style.css)

We used the `space-evenly` value to assign even spacing to both ends of the flexbox and between its lines.

So, now that we know the types of CSS flexible container properties, we can discuss the flex item properties.

## What Are the Flexible Item's Properties?

A flexible item's properties specify how browsers should layout a specified item within the flexible box model.

**Note:** We define a flexible item's property on the flex item, not its container.

The six (6) types of flex item properties are:

* `align-self`
* `order`
* `flex-grow`
* `flex-shrink`
* `flex-basis`
* `flex`

Let's discuss the six types now.

## What Is Flexbox's `align-self` Property?

**align-self** specifies how browsers should position selected flexible items along the flexbox's [cross-axis](https://codesweetly.com/css-flex-direction-property#main-axis-vs-cross-axis-whats-the-difference).

**Note:**

* `align-self` affects only the selected flexible item—not all the flexbox's items.
* `align-self` overrides the `align-items` property.

The `align-self` property accepts the following values:

* `stretch`
* `flex-start`
* `center`
* `flex-end`
* `baseline`

Let's discuss the five values.

### What is `align-self: stretch` in CSS Flexbox?

`stretch` stretches the selected flexible items to fill the flexbox's cross-axis.

![Illustration of align-self's stretch value](https://www.freecodecamp.org/news/content/images/2022/10/css-align-self-stretch-illustration-codesweetly.png)
_stretch stretches the selected flexible item(s) to fill the flexbox's cross-axis._

**Here's an example:**

```css
.flex-item2 {
  align-self: stretch;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-o5qr62?file=style.css)

We used the `stretch` value to stretch `flex-item2` to fill its container's cross-axis.

### What is `align-self: flex-start` in CSS Flexbox?

`flex-start` aligns the selected flexible items with the cross-start edge of the flexbox's cross-axis.

![Illustration of align-self's flex-start value](https://www.freecodecamp.org/news/content/images/2022/10/css-align-self-flex-start-illustration-codesweetly.png)
_flex-start aligns the selected flexible item(s) with the cross-start edge of the flexbox's cross-axis._

**Here's an example:**

```css
.flex-item2 {
  align-self: flex-start;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-6uianm?file=style.css)

The snippet above used the `flex-start` value to align `flex-item2` to the cross-start edge of its container's cross-axis.

### What is `align-self: center` in CSS Flexbox?

`center` aligns the selected flexible items to the center of the flexbox's cross-axis.

![Illustration of align-self's center value](https://www.freecodecamp.org/news/content/images/2022/10/css-align-self-center-illustration-codesweetly.png)
_center aligns the selected flexible item(s) to the center of the flexbox's cross-axis._

**Here's an example:**

```css
.flex-item2 {
  align-self: center;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-tazf2p?file=style.css)

The snippet above used the `center` value to align `flex-item2` to the center of its container's cross-axis.

### What is `align-self: flex-end` in CSS Flexbox?

`flex-end` aligns the selected flexible items with the cross-end edge of the flexbox's cross-axis.

![Illustration of align-self's flex-end value](https://www.freecodecamp.org/news/content/images/2022/10/css-align-self-flex-end-illustration-codesweetly.png)
_flex-end aligns the selected flexible item(s) with the cross-end edge of the flexbox's cross-axis._

**Here's an example:**

```css
.flex-item2 {
  align-self: flex-end;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-7bec4q?file=style.css)

The snippet above used the `flex-end` value to align `flex-item2` to the cross-end edge of its container's cross-axis.

### What is `align-self: baseline` in CSS Flexbox?

`baseline` aligns the selected flexible items with the [baseline](https://stackoverflow.com/a/34611670/11841906) of the flexbox's cross-axis.

**Here's an example:**

```css
.flex-item2 {
  font-size: 3rem;
  align-self: baseline;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-wmawek?file=style.css)

We used the `baseline` value to align `flex-item2` to its container's baseline.

Let's now discuss the second type of flexible item property.

## What Is Flexbox's `order` Property?

**order** changes a flexible item's default order (arrangement).

In other words, `order` allows you to reposition a flexbox's item without altering your HTML code's layout.

**Here's an example:**

```html
<ul style="display: flex; flex-direction: column">
  <li style="order: 6">1</li>
  <li style="order: 4">2</li>
  <li style="order: 1">3</li>
  <li style="order: 7">4</li>
  <li style="order: 2">5</li>
  <li style="order: 5">6</li>
  <li style="order: 3">7</li>
</ul>
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-hmz9my?file=index.html)

The HTML snippet above used the `order` property to change the unordered list's arrangement.

So, instead of the following order:

* 1
* 2
* 3
* 4
* 5
* 6
* 7

The browser will display this:

* 3
* 5
* 7
* 2
* 6
* 1
* 4

Use the `order` property with caution, as it prevents screen readers from accessing the correct reading order of an HTML document. Only use it if it is super important to use CSS to change the HTML code's layout.

But in most cases, it is best to rearrange the HTML code directly rather than using CSS.

**Note:** The `style="value"` syntax, in the HTML snippet above, is the [inline CSS](https://codesweetly.com/inline-vs-internal-vs-external-css#what-is-an-inline-css) technique for styling HTML elements.

## What Is Flexbox's `flex-grow` Property?

**flex-grow** tells browsers how much of the flexbox's left-over space they should add to the selected flexible item's size.

**Note:** A left-over space refers to the space remaining after browsers have deducted the sum of all flexible items' sizes from the flexbox's size.

**Here's an example:**

```css
.flex-item3 {
  flex-grow: 0.5;
}
```

```html
<section>
  <div class="flex-item1">1</div>
  <div class="flex-item2">2</div>
  <div class="flex-item3">3</div>
  <div class="flex-item4">4</div>
</section>
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-grtdo1?file=style.css)

We used the `flex-grow` property to make browsers add half of `<section>`'s left-over space to `flex-item3`'s size.

**Note:** `flex-grow`'s default value is `0`.

## What Is Flexbox's `flex-shrink` Property?

**flex-shrink** tells browsers how much the specified flexible item should shrink when the sum of all items' sizes exceeds the flexbox's size.

In other words, suppose the flexbox's size is insufficient to fit the flexible items. In that case, browsers will shrink the items to fit the container.

Therefore, `flex-shrink` allows you to specify the shrinking factor of a flexible item.

**Here's an example:**

```css
.flex-item3 {
  flex-shrink: 0;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-h2numw?file=style.css)

We used the `flex-shrink` property to prevent browsers from shrinking `flex-item3`.

**Note:**

* Browsers will not shrink flexible items with a `flex-shrink` value of `0`.
* `flex-shrink`'s default value is `1`.

## What Is Flexbox's `flex-basis` Property?

**flex-basis** sets the initial length of a flexible item.

**Here's an example:**

```css
.flex-item3 {
  flex-basis: 100px;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-kwcche?file=style.css)

We used the `flex-basis` property to set `flex-item3`'s initial length to `100px`.

**Note the following:**

* `auto` is `flex-basis`' default value.
* A `flex-basis`' value (other than `auto`) has higher specificity than `width` (or `height`). Therefore, suppose you define both for a flexible item. In that case, browsers will use `flex-basis`.
* The `flex-basis` property sets the [content box](https://codesweetly.com/css-box-model#what-is-a-content-box)'s initial width. But you can use the [box-sizing](https://developer.mozilla.org/en-US/docs/Web/CSS/box-sizing) property to make it set the [border box](https://codesweetly.com/css-box-model#what-is-a-border-box)'s width instead.

## What Is Flexbox's `flex` Property?

**flex** is a shorthand for the `flex-grow`, `flex-shrink`, and `flex-basis` properties.

In other words, instead of writing:

```css
.flex-item3 {
  flex-grow: 0.5;
  flex-shrink: 0;
  flex-basis: 100px;
}
```

You can alternatively use the `flex` property to shorten your code like so:

```css
.flex-item3 {
  flex: 0.5 0 100px;
}
```

**Note the following:**

* `flex: auto` is equivalent to `flex: 1 1 auto`.
* `flex: none` is equivalent to `flex: 0 0 auto`.
* `flex: initial` sets the `flex` property to its default value. It is equivalent to `flex: 0 1 auto`.
* `flex: inherit` inherits its parent element's `flex` property's values.

So, now that we know the flexbox properties developers use to layout flexible boxes and their direct children, we can discuss how to center elements with flexbox.

## How to Center Elements Horizontally with Flexbox

You can center any element horizontally within its container by:

* Setting its container's `display` property to `flex`
* Setting the flexible container's `justify-content` property to `center`

**Here's an example:**

```css
section {
  display: flex;
  justify-content: center;
  background-color: orange;
  width: 100%;
  height: 400px;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-trl46e?file=style.css)

## How to Center Elements Vertically with Flexbox

You can center any element vertically within its container by:

* Setting its container's `display` property to `flex`
* Setting the flexible container's `align-items` property to `center`

**Here's an example:**

```css
section {
  display: flex;
  align-items: center;
  background-color: orange;
  width: 100%;
  height: 400px;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-tm1don?file=style.css)

## How to Center Elements Horizontally and Vertically with Flexbox

You can center any HTML element horizontally and vertically within its container by:

* Setting its container's `display` property to `flex`
* Setting the flexible container's `justify-content` and `align-items` properties to `center`

**Here's an example:**

```css
section {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: orange;
  width: 100%;
  height: 400px;
}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-ryzwmq?file=style.css)

## Overview

In this article, we discussed all the Flexbox tools you need to create basic and advanced website layouts in flexible and responsive ways.

### Thanks for reading!

If you like the images I used in this tutorial, you can get them all in [this booklet](https://store.codesweetly.com/l/css-flexbox-explained-visually).

### And here's a useful ReactJS resource:

I wrote a book about React!

* It's beginner friendly ✔
* It has live code snippets ✔
* It contains scalable projects ✔
* It has plenty of easy-to-grasp examples ✔

The [React Explained Clearly](https://www.amazon.com/dp/B09KYGDQYW) book is all you need to understand ReactJS.

[![React Explained Clearly Book Now Available at Amazon](https://www.freecodecamp.org/news/content/images/2022/01/Twitter-React_Explained_Clearly-CodeSweetly-Oluwatobi_Sofela.jpg)](https://www.amazon.com/dp/B09KYGDQYW)


