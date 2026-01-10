---
title: CSS Text Align – Centered, Justified, Right Aligned Text Style Example
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-01-28T17:30:39.000Z'
originalURL: https://freecodecamp.org/news/css-text-align-centered-justified-right-aligned-text-style-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/cssTextAlign.png
tags:
- name: CSS
  slug: css
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "We use the CSS text-align property to align content inside a block-level\
  \ element. \nExamples of block-level elements are paragraphs (<p>...</p>), divs\
  \ (<div>...</div>), sections (<section>...</section>), articles (<article>...</article>),\
  \ and so on.\nT..."
---

We use the CSS `text-align` property to align content inside a block-level element. 

Examples of block-level elements are paragraphs (`<p>...</p>`), divs (`<div>...</div>`), sections (`<section>...</section>`), articles (`<article>...</article>`), and so on.

This alignment affects the horizontal axis only. So the `text-align` property is different from the `vertical-align` property which we use to set the vertical alignment of an element.

## Table of Contents
- [Basic Syntax](#heading-basic-syntax)
- [Values of the `text-align` Property](#heading-values-of-the-text-align-property)
- [The `left` Value](#heading-the-left-value)
- [The `center` Value](#heading-the-center-value)
- [The `right` Value](#heading-the-right-value)
- [The `justify` Value](#heading-the-justify-value)
- [The `inherit` Value](#heading-the-inherit-value)
- [Conclusion](#heading-conclusion)

## Basic Syntax 

Here's the basic syntax for the `text-align` property:

```css
block-level-element {
      text-align: value;
    }
```

Now we'll look at the different values it can take to help you position things on the page.

## Values of the `text-align` Property

The `text-align` property accepts `left`, `center`, `right`, `justify`, and `inherit` as values.

We will take a look at these values one by one.

Before I dive into the values and what they look like in the browser, take a look at the below CSS. I set these styles for improved visibility, so you can see things better:

```css
   body {
      display: flex;
      align-items: center;
      justify-content: center;
      height: 100vh;
    }

    div {
      background-color: #adadad;
      width: 40rem;
      height: 4rem;
      padding: 3rem 0.5rem;
    }
```

### The `left` Value

The `left` value of the `text-align` property is the default. So, every content inside a block-level element is aligned to the left by default.

```css
 div {
      text-align: left;
    }
```
![ss-1-3](https://www.freecodecamp.org/news/content/images/2022/01/ss-1-3.png)

If you want the content inside a block-level element to align to the left, you don't need to assign it a `text-align` value of `left`. If you do, you're just duplicating what's already the default.

### The `center` Value

With the center value, spaces are created on the left and right, so, everything gets pushed to the center. 

If you want to align the content inside a block-level element to the center, the `center` value is your best bet. 

```css
  div {
      text-align: center;
    }
```
![ss-2-3](https://www.freecodecamp.org/news/content/images/2022/01/ss-2-3.png)

### The `right` Value

Assigning a value of `right` to the `text-align` property pushes the content inside a block-level element to the right.

```css
  div {
      text-align: right;
    }
```
![ss-3-4](https://www.freecodecamp.org/news/content/images/2022/01/ss-3-4.png)

### The `justify` Value

The `justify` value of the `text-align` property lines up the content on the left and right edges of the block-level element (the box). If the last line isn't a full line, then it leaves it alone. It's easier to see how this works in the image below: 

```css
 div {
      text-align: justify;
    }
```
![ss-4-4](https://www.freecodecamp.org/news/content/images/2022/01/ss-4-4.png)

### The `inherit` Value

The `inherit` value of the `text-align` property behaves as the name implies. An element with its text-align value set to `inherit` inherits the `text-align` value of its direct parent.

```css
 div {
      text-align: inherit;
    }
```
![ss-5-5](https://www.freecodecamp.org/news/content/images/2022/01/ss-5-5.png)

In this case, our `div` inherits the text-align value of the body – which is `left` by default.

If the `text-align` value of the `body` is set to `right`, and that of the `div` is left to inherit, the text inside the `div` aligns to the right.

```css
 body {
      text-align: right;
    }

    div {
      text-align: inherit;
    }
```
![ss-6-1](https://www.freecodecamp.org/news/content/images/2022/01/ss-6-1.png)

## Conclusion

In this article, you learned about the CSS `text-align` property and its values. 

The examples we looked at here to see how the values behave contained text only – so you might be wondering if the values work on images too. Well, yes they do.

Below is an image inside a div with text-align set to center:

```html
 <div>
      <img
        src="coming-soon.jpg"
        alt="coming_soon"
        width="74px"
        height="54px"
      />
</div>
```
```css
 div {
      text-align: center;
    }
```
![ss-7-2](https://www.freecodecamp.org/news/content/images/2022/01/ss-7-2.png)

Thank you for reading.


