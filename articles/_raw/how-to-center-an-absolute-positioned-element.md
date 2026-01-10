---
title: How to Center an Absolute Positioned Element Vertically and Horizontally with
  CSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-05-06T19:56:35.000Z'
originalURL: https://freecodecamp.org/news/how-to-center-an-absolute-positioned-element
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/pexels-jack-hawley-57905.jpg
tags:
- name: CSS
  slug: css
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Dillion Megida

  Absolute positioned elements are removed from the flow of a document. And sometimes,
  knowing how to correctly position such elements in the center of the page can be
  confusing.

  I mean, CSS is confusing already. 😅

  In this article, I...'
---

By Dillion Megida

Absolute positioned elements are removed from the flow of a document. And sometimes, knowing how to correctly position such elements in the center of the page can be confusing.

I mean, CSS is confusing already. 😅

In this article, I will show you how to center an absolute element either vertically or horizontally – or both – in a container.

## Code Example

To center an elemenet horizontally:

```css
element {
  position: absolute;
  left: 0;
  right: 0;
  margin: 0 auto;
}
```

To center an element vertically:

```css
element {
  position: absolute;
  top: 0;
  bottom: 0;
  margin: auto 0;
}
```

To center an element both vertically and horizontally:

```css
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  margin: auto;
```

But if you would like to understand how I came to these solutions, read further for more explanation.

## How does the absolute position work?

By default, elements have a `static` position unless specified otherwise as `absolute`, `fixed`, `relative` or `sticky`. You can read [this article on CSS position styles](https://dillionmegida.com/p/static-relative-absolute-fixed-sticky-positions/) to understand the difference.

I will use the following UI to explain how `absolute` elements work:

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-32.png)

Here is the code for the UI:

```html
<div class="container">
  <div class="blue-block"></div>
  <div class="green-block"></div>
  <div class="black-block"></div>
</div>
```

```css
.container {
  margin: 20px;
  display: flex;
  border: 1px solid black;
  padding: 20px;
  width: 400px;
}

.blue-block,
.green-block,
.black-block {
  width: 100px;
  height: 100px;
}

.blue-block {
  background-color: blue;
}

.green-block {
  background-color: green;
}

.black-block {
  background-color: black;
}
```

This container has three blocks: blue, green, and black, respectively. All blocks are currently `static`, so they are ordered the same way in the DOM, just as they are in the code.

What happens when you give the green block an `absolute` position:

```css
.green-block {
  background-color: green;
  position: absolute;
  margin-left: 20px;
  margin-top: 20px;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-31.png)

You can see now that the green block has left the document flow. The container only applies the flex display to the blue and black elements, and the green element wanders around without affecting the others.

So, what if we wanted to position this green block at the center of the container?

## How to position absolute elements in the center

Positioning static elements to the center usually involve auto margins, so a `margin: auto` should suffice, right?

```css
.green-block {
  background-color: green;
  position: absolute;
  margin: auto;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-33.png)

It definitely does not. As an `absolute` element, it loses its flow in the container. Maybe a `left: auto` and `right: auto` then:

```css
.green-block {
  background-color: green;
  position: absolute;
  left: auto;
  right: auto;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-34.png)

Still nothing. At this point, you may be tempted to use hardcoded values:

```css
.blue-block, .black-block {
  display: none;
}

.green-block {
  background-color: green;
  position: absolute;
  left: 190px;
  top: 90px;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-35.png)

This result looks perfect (or almost) but is not the best solution because when you change the size of the container, you have to change the hardcoded values.

Now, let's look at how you can center absolute positioned elements.

The first part is applying a `relative` position to the container:

```css
.container {
  // ...
  position: relative;
}
```

Applying a relative position to the container gives the absolute element a boundary. Absolute elements are bounded by the closest relative positioned parent. But if none of that exists, they will be bounded by the viewport.

Next, we will center the block horizontally. Apply a `left` and `right` property with the value of 0. These properties respectively specify the distance of the left edge (of the block) to the container and the right edge to the container.

```css
.green-block {
  // ...
  left: 0;
  right: 0;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-36.png)

The `left` takes more precendence because the container displays elements from left to right.

The beauty comes in with the next style:

```css
.green-block {
  // ...
  margin: 0 auto;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-37.png)

And you have a horizontally centered absolute element. Think of the `left` and `right` properties specifying an inner container for the block. Within this container, the left and right margins can be `auto` so that they are equal and bring the element to the center.

To center this block vertically, you can already guess that it goes this way:

```css
.green-block {
  // ...
  top: 0;
  bottom: 0;
  margin: auto 0;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-39.png)

The `top` and `bottom` specify the distance between the top and bottom edges of the block, which looks like an inner container. Using `auto` creates equal margins for `margin-top` and `margin-bottom`.

Bringing the two concepts together, you can horizontally and vertically center the block like this:

```css
.green-block {
  background-color: green;
  position: absolute;
  right: 0;
  left: 0;
  top: 0;
  bottom: 0;
  margin: auto;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-38.png)

With this approach, the element stays at the center if you resize the container.

## Wrapping up

Absolute elements behave differently than static elements – they leave the document flow and, by default, do not respect the container they were declared in.

With a `relative` positioned parent element, an `absolute` positioned element has a boundary. And with the `left`, `right`, `top` and `bottom` properties with a value of **0** (specifying the distance of the edges), and an **auto** margin, the absolute element is centered in the parent element.

Note that this is not the only way to position absolute elements in the center. I have seen someone online use a `transform: translate...` to achieve this, too. You can look into that if you like.


