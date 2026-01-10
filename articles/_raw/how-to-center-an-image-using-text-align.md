---
title: 'How to Center an Image Using Text Align: Center'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-30T21:11:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-center-an-image-using-text-align
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e5e740569d1a4ca3cbb.jpg
tags:
- name: CSS
  slug: css
seo_title: null
seo_desc: 'An <img> element is an inline element (display value of inline-block).
  It can be easily centered by adding the text-align: center; CSS property to the
  parent element that contains it.

  To center an image using text-align: center; you must place the <i...'
---

An `<img>` element is an inline element (display value of `inline-block`). It can be easily centered by adding the `text-align: center;` CSS property to the parent element that contains it.

To center an image using `text-align: center;` you must place the `<img>` inside of a block-level element such as a `div`. Since the `text-align` property only applies to block-level elements, you place `text-align: center;` on the wrapping block-level element to achieve a horizontally centered `<img>`.

### **Example**

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Center an Image using text align center</title>
    <style>
      .img-container {
        text-align: center;
      }
    </style>
  </head>
  <body>
    <div class="img-container"> <!-- Block parent element -->
      <img src="user.png" alt="John Doe">
    </div>
  </body>
</html>
```

**Note:** The parent element must be a block element. If it is not a block element, you should add `display: block;` CSS property along with the `text-align` property.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Center an Image using text align center</title>
    <style>
      .img-container {
        text-align: center;
        display: block;
      }
    </style>
  </head>
  <body>
    <span class="img-container"> <!-- Inline parent element -->
      <img src="user.png" alt="">
    </span>
  </body>
</html>
```

**Demo:** [Codepen](https://codepen.io/aravindio/pen/PJMXbp)

## Object Fit

Once your image is centered, you might want to resize it. The `object-fit` property specifies how an element responds to the width / height of it’s parent box.

This property can be used for image, video, or any other media. It can also be used with the `object-position` property to get more control on how the media is displayed.

Basically we use the `object-fit` property to define how it stretch or squish an inline media.

### Syntax

```css
.element {
    object-fit: fill || contain || cover || none || scale-down;
}
```

### Values

* `fill`: **This is the default value**. Resize the content to match its parent box regardless of the aspect-ratio.
* `contain`: Resize the content to fill its parent box using the correct aspect-ratio.
* `cover`: similar as `contain` but often cropping the content.
* `none`: display the image in its original size.
* `scale-down`: compare the difference between `none` and `contain` to find the smallest concrete object size.

### Browser Compatibility

The `object-fit` is supported by most of the modern browsers, for the most updated info about compatibility you can check this out [http://caniuse.com/#search=object-fit](http://caniuse.com/#search=object-fit).

## **Documentation**

* [**text-align**](https://developer.mozilla.org/en-US/docs/Web/CSS/text-align) - MDN
* [**object-fit** - MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/object-fit)
* [**<img>**](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img) - MDN

