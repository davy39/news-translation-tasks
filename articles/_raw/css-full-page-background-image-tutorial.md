---
title: CSS Background Image Size Tutorial – How to Code a Full Page Background Image
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-02T20:58:10.000Z'
originalURL: https://freecodecamp.org/news/css-full-page-background-image-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/CSS-BG-Img-Tutorial.jpg
tags:
- name: coding
  slug: coding
- name: CSS
  slug: css
- name: responsive design
  slug: responsive-design
seo_title: null
seo_desc: 'By Joe Liang

  This tutorial will show you a simple way to code a full page background image using
  CSS. And you''ll also learn how to make that image responsive to your users'' screen
  size.

  Making a background image fully stretch out to cover the entire ...'
---

By Joe Liang

This tutorial will show you a simple way to code a full page background image using CSS. And you'll also learn how to make that image responsive to your users' screen size.

Making a background image fully stretch out to cover the entire browser viewport is a common task in web design. Fortunately, this task can be taken care of with a few lines of CSS.

##Cover Viewport with Image

First, we will want to make sure our page actually covers the entire viewport:

```css
html {
   min-height: 100%;
}

Inside `html`, we will use the `background-image` property to set the image:

```css
background-image: url(image.jpg); /*replace image.jpg with path to your image*/

##Magic of 'Background-Size' Property

The magic happens with the `background-size` property:

```css
background-size: cover;

`cover` tells the browser to make sure the image always covers the entire container, in this case `html`. The browser will cover the container even if it has to stretch the image or cut a little bit off the edges.

Because the browser may stretch the image, you should use a background image that has high enough resolution. Otherwise the image may appear pixelated.

If you care about having all of the image appear in the background, then you will want to make sure the image is relatively close in aspect ratio compared to the screen size.

## How to Fine Tune an Image Position and Avoid Tiling

The browser can also choose to display your background image as tiles depending on its size. To prevent this from happening, use `no-repeat`:

```css
background-repeat: no-repeat;

To keep things pretty, we will keep our image always centered:   

```css
background-position: center center;

This will center the image both horizontally and vertically at all times.

We have now produced a fully responsive image that will always cover the entire background:

```css
html {
   min-height: 100%;
   background-image: url(image.jpg);
   background-size: cover;
   background-repeat: no-repeat;
   background-position: center center;
}


## How to Fix an Image in Place When Scrolling

Now, just in case you want to add text on top of the background image and that text overflows the current viewport, you may wish to make sure your image stay in the background when the user scrolls down to see the rest of the text:

```css
background-attachment: fixed;

You can include all of the background properties described above using short notation:

```css
background: url(image.jpg) center center cover no-repeat fixed;

##Optional: How to Add a Media Query for Mobile

To add some icing on the cake, you may wish to add a media query for smaller screens:

```css
@media only screen and (max-width: 767px) {
  html {
     background-image: url(smaller-image.jpg);
  }
}


You can use Photoshop or some other image editing software to downsize your original image to improve page load speed on mobile internet connections.

So now that you know the magic of creating a responsive, full page image background, it is time to go create some beautiful websites!

##Want to See More Web Development Tips and Knowledge?

* [Subscribe](https://1000mileworld.com/#post) to my weekly newsletter
* Visit my blog at  [1000 Mile World](https://1000mileworld.com/)
* [Follow me](https://twitter.com/1000mileworld) on Twitter

