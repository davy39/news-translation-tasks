---
title: HTML Background Image – How to Add Wallpaper Images to Your Website
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-09-23T19:18:19.000Z'
originalURL: https://freecodecamp.org/news/html-background-image-how-to-add-wallpaper-images-to-your-website
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/jonatan-pie-3l3RwQdHRHg-unsplash.jpg
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: image
  slug: image
seo_title: null
seo_desc: "Background images can help beautify websites and make them more attractive\
  \ to users. \nIn this article, you'll learn: \n\nHow to add a background image to\
  \ your website using the CSS background-image property. \nOther CSS background properties\
  \ for images...."
---

Background images can help beautify websites and make them more attractive to users. 

In this article, you'll learn: 

* How to add a background image to your website using the CSS `background-image` property. 
* Other CSS background properties for images.

## How to Add Wallpaper Images to Your Website

When coding a website, using an image as the background image of the website is different from inserting an image in HTML using the `img` element.

To use an image as the background of your website, you'll use CSS. 

Here's an example: 

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" href="style.css">
    <title>Background Image</title>
</head>

<body>
    <h1>Background image</h1>
</body>
</html>
```

```css
h1{
    text-align: center;
}
```

We have two code blocks above — the HTML code displays text that says "Background image" on the webpage while the CSS code centers the text on the page. 

To add a wallpaper image to the website — one that covers the entire page — you have to write some CSS rules for the `body` element. Here's how: 

```css
body{
    background-image: url('bg-image.jpg');
}
```

In the code above, we're using the `background-image` property to add an image to the body of the webpage. The path/location of the image is passed in as a parameter to the `url()` function: `url('bg-image.jpg')`. 

Here's what the webpage looks like now:

![Image](https://www.freecodecamp.org/news/content/images/2022/09/full-bg-image.PNG)

## What if the Background Image Is Smaller Than the Browser Window?

In situations where the image is smaller than the browser, the image is repeated a couple 0f time to cover up the spaces that remain. 

This repetition doesn't look great for every picture. Here's what a smaller version of the image used in the previous section looks like in the browser: 

![Image](https://www.freecodecamp.org/news/content/images/2022/09/repeat.PNG)

The image has been split into four uneven parts. Unless this is the effect you're looking for, you can fix it using the `background-repeat` property. 

Here's how to fix the image repetition problem:

```css
body{
    background-image: url('bg-image-small.jpg');
    background-repeat: no-repeat;
}

```

In the code above, we assigned a `no-repeat` value to the `background-repeat` property.

Here's what the webpage looks like now:

![Image](https://www.freecodecamp.org/news/content/images/2022/09/small-image.PNG)

The image is no longer being repeated across the page but we have a new problem — the image no longer covers the whole page.  

To fix that, we use the `background-size` and `background-attachment` properties:

```css
body{
    background-image: url('bg-image-small.jpg');
    background-repeat: no-repeat;
    background-size: cover;
    background-attachment: fixed;
}
```

Setting the value of the `background-size` property to `cover` makes the image cover the whole element (the `body`/entire page in our case). 

With the `fixed` value of the `background-attachment` property, the image's position is fixed. This way it remains in the same position even when you scroll across the page. 

Here's the image now:

![Image](https://www.freecodecamp.org/news/content/images/2022/09/cover-image.PNG)

The downside of stretching out a small image to cover the entire page is that the image loses quality and becomes blurry as its being stretched. In this case, you should consider that before using a small image as the background image for your website. 

## Summary

In this article, we talked about adding wallpaper images to a website. 

You can add a background image to your website using the CSS `background-image` property.

We also learned how to use other CSS background properties like `background-repeat`, `background-size`, and `background-attachment`. 

Happy coding!

