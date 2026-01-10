---
title: HTML Center Image – CSS Align Img Center Example
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-02-01T21:16:57.000Z'
originalURL: https://freecodecamp.org/news/html-center-image-css-align-img-center-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/arrows-2889040_1920.jpg
tags:
- name: CSS
  slug: css
- name: css flex
  slug: css-flex
- name: CSS Grid
  slug: css-grid
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "If you're making websites with HTML and CSS, you will be working with images\
  \ a lot. \nDevelopers often struggle with image alignment in CSS, especially when\
  \ trying to figure out how to center an image.\nCentering anything in CSS is not\
  \ really a straigh..."
---

If you're making websites with HTML and CSS, you will be working with images a lot. 

Developers often struggle with image alignment in CSS, especially when trying to figure out how to center an image.

Centering anything in CSS is not really a straightforward thing - especially for beginners. This is why people brag about being able to center a div. :)

Since the `img` element is an inline element, this makes it a little bit harder to center. But don't worry, you can convert the image to a block element and then center it.

In this article, I'm going to show you 4 different ways you can align an image to the center.

## Table of Contents
- [How to Center an Image With the Text Align Property](#heading-how-to-center-an-image-with-the-text-align-property)
- [How to Center an Image with Flexbox](#heading-how-to-center-an-image-with-flexbox)
- [How to Center an Image with CSS Grid](#heading-how-to-center-an-image-with-css-grid)
- [How to Center an Image with the Margin Property](#heading-how-to-center-an-image-with-the-margin-property)

## How to Center an Image With the Text Align Property

You can center an image with the `text-align` property. 

One thing you should know is that the tag for bringing in images – `img` – is an inline element. Centering with the `text-align` property works for block-level elements only.

So how do you center an image with the text-align property? You wrap the image in a block-level element like a `div` and give the `div` a `text-align` of `center`.

```html
<div>
    <img src="fcc22.png" alt="freeCodeCamp" />
</div>
```

```css
div {
      text-align: center;
    }
```
![ss-1](https://www.freecodecamp.org/news/content/images/2022/02/ss-1.png)

## How to Center an Image with Flexbox

The introduction of CSS Flexbox made it easier to center anything.

Flexbox works by putting what you want to center in a container and giving the container a `display` of `flex`. Then it sets `justify-content` to `center` as shown in the code snippet below:

```css
  div {
      display: flex;
      justify-content: center;
    }
```
![ss-1](https://www.freecodecamp.org/news/content/images/2022/02/ss-1.png)

**P.S.:** A `justify-content` property set to `center` centers an image horizontally. To center the image vertically too, you need to set `align-items `to `center`.

## How to Center an Image with CSS Grid

CSS Grid works like Flexbox, with the added advantage that Grid is multidimensional, as opposed to Flexbox which is 2-dimensional.

To center an image with CSS Grid, wrap the image in a container div element and give it a display of `grid`. Then set the `place-items` property to center. 
```css
 div {
      display: grid;
      place-items: center;
    }
```
![ss-1](https://www.freecodecamp.org/news/content/images/2022/02/ss-1.png)

**P.S.:**`place-items` with a value of `center` centers anything horizontally and vertically.

## How to Center an Image with the Margin Property

You can also center an image by setting a left and right margin of auto for it. But just like the `text-align` property, `margin` works for block-level elements only. 

So, what you need to do is convert the image to a block-level element first by giving it a display of block.

```css
img {
      display: block;
      margin: 0 auto;
    }
```

Those 2 properties could be enough. But sometimes, you have to set a width for the image, so the left and right margin of auto would have spaces to take.

```css
 img {
      display: block;
      margin: 0 auto;
      width: 40%;
    }
```

![ss-2](https://www.freecodecamp.org/news/content/images/2022/02/ss-2.png)

**P.S.:** You might not have to go as low as 40% for the width. The image was distorted at a 60+ percentage, that’s why I went as low as 40%.

I hope this article helps you choose which method works best for you in centering an image.

Thank you for reading.


