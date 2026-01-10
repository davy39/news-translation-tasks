---
title: What are Absolute and Relative Units in CSS? Explained with Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-09-30T21:19:17.000Z'
originalURL: https://freecodecamp.org/news/absolute-and-relative-css-units
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/absolute-relative-units-1.png
tags:
- name: CSS
  slug: css
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Dillion Megida

  In CSS, we categorize measurement units as either absolute or relative units. In
  this article, I''ll explain what these categories are with examples of units that
  fall under each of them.

  CSS Measurement Units

  You can use different m...'
---

By Dillion Megida

In CSS, we categorize measurement units as either absolute or relative units. In this article, I'll explain what these categories are with examples of units that fall under each of them.

## CSS Measurement Units

You can use different measurement units in CSS. You use these units with length or size values and they can be associated with properties like `font-size`, `width`, `border-width`, `padding`, and so many more.

When using `font-size`, you specify a value for the size of the font.

You also specify a length for the `width` of an element.

And with padding, you specify a length.

These values have units that help CSS understand what length or size their elements should be on the screen. And as I mentioned in the beginning of the article, we can categorize these values into **Absolute** and **Relative** units.

## What are Absolute Units?

Absolute units specify a fixed length value. It doesn't matter if the screen's width or height changes, the value will remain fixed.

Units that fall under this category include:

`mm` (millimeters)
`cm` (centimeters): 10mm makes 1cm
`in` (inches): 2.54cm makes 1in
`pt` (points): 1/72in makes 1pt
`pc` (picas) – 12pt makes 1pc
`px` (pixel)– 0.75pt makes 1px

For high-resolution media like print documents, it is recommended that you use `cm`, `mm`, or `pt`. For webpages, `px` is the recommended unit.

Here is an example:

```html
<div>Hello</div>
```

And the CSS:

```css
div {
  border: 2px solid black;
  width: 300px;
}
```

On a full screen, here is the result:

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-475.png)

When the screen becomes smaller, the `div` still maintains a `300px` width because it is a fixed value:

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-476.png)

The width of the block is not relative to anything, so regardless of other size changes, the DOM is still going to try to maintain that `300px` width as much as possible.

## What are Relative Units?

Unlike absolute units, relative units are not fixed. Their values are "relative" to another value. This means that when that other value changes, the relative unit value will also change.

Units that fall under this category include:
`%` (percentage): relative to the size of the parent element
`em` (font size): relative to the size of the font
`rem` (root `em`): relative to the font size of the root element
`vw` (viewport width): relative to the width of the viewport
`vh` (viewport height): relative to the height of the viewport

You can see how values with these units are relative to another value. Here's an example:

```html
<div class='container'>
    <div class='card'>
        Hello
    </div>
</div>
```

And the CSS:

```css
.container {
  width: 300px;
  border: 2px solid black;
  padding: 20px;
}

.card {
  width: 60%;
  border: 2px solid green;
  padding: 10px;
}
```

The result:

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-478.png)

From the above, you see that the `.container` div is `300px` (fixed). But the `.card` div is `60%` width, which means `60%` of the width of its parent element. So you have **60% of 300px**, and that results in the `.card` div having a width of `180px`.

If the width of the `.container` div changes, the `.card` div will also change.

Here's another example using `vw`:

```css
.container {
  width: 100vw;
  background-color: blue;
  padding: 10px;
}

.card {
  width: 80vw;
  height: 100vh;
  background-color: red;
}
```

Here is the result:

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-479.png)

Here, you can see that the `.container` div is `100vw` width, which means 100% of the viewport width. The `.card` div is `80vw` width and `90vh` height, which means 80% of the viewport width and 90% of the viewport height.

When you reduce the size of the viewport, these relative values will adjust:

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-481.png)

Here, I have reduced the width and height of the viewport, and so the relative values applied on `.container` and `.card` are adjusted also.

The `em` unit can mean two things: in the context of typography, it means "**relative to the parent element's font size**" and in the context of size properties like widths and heights, it means "**relative to the current element's font size**".

Let's see an example:

```html
<div class='container'>
    <p class='text'>I am a text</p>
</div>
```

And the CSS:

```css
.container {
  font-size: 16px;
}

.text {
  font-size: 2em;
  width: 3em;
  border: 1px solid red;
  padding: 10px;
}
```

Here's the result:

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-482.png)

I'll explain what happened in the result above.

The `.container` div has a `font-size` of `16px`.

The `.text` p has a `font-size` of `2em`. Since this is typography, it means "**the font size is 2 times the parent's font-size**", so it is `32px`.

The p tag also has a `width` of `3em`. Since this property doesn't fall under typography, it means "**the width is 3 times the font-size of the element itself**". The `font-size` is `32px`, so the `width` will be `96px`.

`rem` on the other hand, in both contexts, means "**relative to the root element's font size**".  Here's an example:

```html
<div class='container'>
    <p class='text'>I am a text</p>
</div>
```

And the CSS:

```css
html {
  font-size: 20px;
}

.container {
  width: 5rem;
  border: 1px solid green;
}

.text {
  font-size: 0.5rem;
  width: 2rem;
  padding: 1rem;
  border: 1px solid red;
}
```

Here is the result:

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-484.png)

The root element has a `font-size` of `20px`. Here are the calculations for the relative units in the CSS:

* `.container` div has a `width` of `5rem` which is **5 times 20px** and that is **100px**
* `.text` p has a:
    * `font-size` of `0.5rem` which is **1/2 of 20px** and that is **10px**
    * `width` of `2rem` which is **2 times 20px** and that is **40px**
    * `padding` of `1rem` which is **1 times 20px** and that is **20px**


## Wrapping up

Units are a value of measurement in CSS, which helps CSS determine what length/size values will be applied to size-based properties.

In this article, we've looked at the two categories of units which are **Absolute** and **Relative**.

As a recap, **Absolute** units are used for fixed values. These values do not change regardless of changes in the sizes of the surrounding elements or the viewport. 

**Relative** units, on the other hand, are used for values that are relative to – or depend on – values of other elements (usually the parent, the viewport, or the root element).

Thank you for reading!


