---
title: CSS Background Image – How to Add an Image URL to Your Div
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-05T11:22:36.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-an-image-url-to-your-div
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/w-qjCHPZbeXCQ-unsplash.jpg
tags:
- name: CSS
  slug: css
- name: css properties
  slug: css-properties
- name: Design
  slug: design
- name: image
  slug: image
- name: programing
  slug: programing
seo_title: null
seo_desc: "By Amy Haddad\nSay you want to put an image or two on a webpage. One way\
  \ is to use the background-image CSS property. \nThis property applies one or more\
  \ background images to an element, like a <div>, as the documentation explains.\
  \ Use it for aesthetic..."
---

By Amy Haddad

Say you want to put an image or two on a webpage. One way is to use the **`background-image`** CSS property. 

This property applies one or more background images to an element, like a **`<div>`,** as the [documentation](https://developer.mozilla.org/en-US/docs/Web/CSS/background-image) explains. Use it for aesthetic reasons, such as adding a textured background to your webpage.

# Add an Image

It’s easy to add an image using the `background-image` property. Just provide the path to the image in the `url()` value.

The image path can be a URL, as shown in the example below:

```css
div {
   /* Background pattern from Toptal Subtle Patterns */
   background-image: url("https://amymhaddad.s3.amazonaws.com/morocco-blue.png");
   height: 400px;
   width: 100%;
}
```
 

Or it can be a local path. Here’s an example:

```css
body {
   /* Background pattern from Toptal Subtle Patterns */
   height: 400px;
   width: 100%;
   background-image: url("./images/oriental-tiles.png");
}
```

# Add Multiple Images

You can apply multiple images to the `background-image` property.

```css
div {
/* Background pattern from Toptal Subtle Patterns */
   height: 400px;
   width: 100%;
   background-image: 
       url("https://amymhaddad.s3.amazonaws.com/morocco-blue.png"),
       url("https://amymhaddad.s3.amazonaws.com/oriental-tiles.png");
   background-repeat: no-repeat, no-repeat;
   background-position: right, left; 
}
```

That’s a lot of code. Let’s break it down.

Separate each image `url()` value with a comma.

```css
background-image: 
    url("https://amymhaddad.s3.amazonaws.com/morocco-blue.png"),
    url("https://amymhaddad.s3.amazonaws.com/oriental-tiles.png");
```

Now position and enhance your images by applying additional properties.

```css
background-repeat: no-repeat, no-repeat;
background-position: right, left; 
```

There are several [sub-properties](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Backgrounds_and_Borders/Using_multiple_backgrounds) you can add to your background images, such as **`background-repeat`** and **`background-position`**, which we used in the above example. You can even add [gradients](https://developer.mozilla.org/en-US/docs/Web/CSS/gradient) to a background image.

See what it looks like when we put everything together.

%[https://codepen.io/amymhaddad/pen/VwLqWbm]

# Order Matters

The order that you list your images in matters because of the stacking order. That means the first image listed is nearest to the user, according to the [documentation](https://www.w3.org/TR/css-backgrounds-3/#layering). Then, the next one, and the next, and so on. 

Here’s an example.

```css
div {
/* Background pattern from Toptal Subtle Patterns */
   height: 400px;
   width: 100%;
   background-image: 
       url("https://amymhaddad.s3.amazonaws.com/morocco-blue.png"),
       url("https://amymhaddad.s3.amazonaws.com/oriental-tiles.png");
   background-repeat: no-repeat, no-repeat;
}
```

We’ve listed two images in the code above. The first image (morocco-blue.png) will be in front of the second (oriental-tiles.png). Both images are the same size and lack opacity, so we only see the first image.

But if we move the second image (oriental-tiles.png) over to the right by 200 pixels, then you can see part of it (the rest remains hidden).

Here’s what it looks like when we put everything together.

%[https://codepen.io/amymhaddad/pen/oNXrXMo]

## When Should You Use Background Image?

There’s a lot to like about the `background-image` property. But there’s a drawback. 

The image may not be accessible to all users, the [documentation](https://developer.mozilla.org/en-US/docs/Web/CSS/background-image) points out, like those who use screen readers.

That’s because you can’t add textual information to the `background-image` property. As a result, the image will be missed by screen readers.

Use the `background-image` property only when you need to add some decoration to your page. Otherwise, use the HTML **`<img>`** element if an image has meaning or purpose, as the [documentation](https://developer.mozilla.org/en-US/docs/Web/CSS/background-image) notes.

That way, you can add text to an image element, using the **`alt`** attribute, which [describes the image](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img). The provided text will be picked up by screen readers.

```html
<img class="house" 
       src="./images/farnsworth_house.jpeg"
       alt="A glass house designed by Ludwig Mies van der Rohe located in Plano, Illinois.">
```

Think of it this way: `background-image` is a CSS property, and CSS focuses on presentation or style; HTML focuses on semantics or meaning. 

When it comes to images, you’ve got options. If an image is needed for decoration, then the `background-image` property may be a good choice for you.

_I write about learning to program and the best ways to go about it (_[amymhaddad.com](https://amymhaddad.com/)).  

