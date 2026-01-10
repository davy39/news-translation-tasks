---
title: How Lazy Loading Works in Web Development
subtitle: ''
author: Sudheer Kumar Reddy Gowrigari
co_authors: []
series: null
date: '2024-01-04T01:08:30.000Z'
originalURL: https://freecodecamp.org/news/how-lazy-loading-works-in-web-development
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/A-simple-banner-image-depicting-the-concept-of-lazy-loading-images.png
tags:
- name: performance
  slug: performance
- name: web performance
  slug: web-performance
seo_title: null
seo_desc: "In the ever-evolving landscape of web development, performance optimization\
  \ remains a top priority. \nAmong the plethora of strategies you can use to enhance\
  \ web performance, lazy loading stands out for its efficiency and impact. \nBut\
  \ what exactly is ..."
---

In the ever-evolving landscape of web development, performance optimization remains a top priority. 

Among the plethora of strategies you can use to enhance web performance, lazy loading stands out for its efficiency and impact. 

But what exactly is lazy loading, and how does it revolutionize the way we handle web resources? That's what we'll cover in this article.

## What is Lazy Loading?

Lazy loading is a web performance optimization strategy that plays a critical role in how resources are loaded on a webpage. 

Traditionally, when you go to access a webpage, the browser attempts to load all resources (images, scripts, stylesheets) immediately. This can lead to longer load times, especially if the page contains many large files. 

Lazy loading addresses this by marking certain resources as non-blocking or non-critical, loading them only when they are needed. This method is especially effective for elements that aren't immediately visible on the initial page load, such as images and videos that appear further down the page.

### Key benefits of lazy loading:

* **Improved Performance**: By loading only the necessary resources, the initial page load is faster, leading to a better user experience.
* **Reduced Bandwidth Usage**: Lazy loading minimizes the amount of data that needs to be transferred initially, saving bandwidth for both the user and the server.
* **Enhanced User Engagement**: Faster load times generally lead to lower bounce rates and higher engagement, as users are less likely to leave a slow-loading site.

Lazy loading can be implemented in various ways, with the most common method being JavaScript-based. But modern web development practices have introduced native HTML ways to implement lazy loading, such as the loading attribute for images.

## The Role of the Image Loading Attribute in Lazy Loading

As we delve deeper into the practicalities of lazy loading, you'll see that the [loading](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#loading) attribute in the [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img) element is a game-changer. 

This attribute, a relatively recent addition to the HTML specification, offers a simple yet powerful way to implement lazy loading natively, without the need for additional JavaScript. By leveraging the loading attribute, you can significantly enhance web performance and user experience, especially in content-heavy websites.

### Browser-Level Lazy Loading

Primarily, browsers like Chrome and Firefox support the loading attribute for <img> and <iframe> elements. Using loading="lazy", the browser defers the loading of images until they are near the viewport. 

This method is efficient and enhances performance by loading images only when they are likely to be viewed by the user. But it's important to note that the lazy value for <iframe> elements is not yet standardized and may undergo changes.

Let's look at some examples to see how this works.

#### Basic lazy loading of a single image

```html
<img src="image-1.jpg" alt="A scenic landscape" loading="lazy">
```

In this example, the `loading="lazy"` attribute in the `<img>` tag tells the browser to defer loading this image until it's about to enter the viewport. This means the image won't load when the page initially loads, but only when the user scrolls near it.

#### Lazy loading with high-priority images

```html
<img src="logo.jpg" alt="Company Logo" loading="eager"> 
<img src="featured.jpg" alt="Featured Product" loading="lazy">
```

Here, the first image (logo) uses `loading="eager"`, which is the default behavior to load the image immediately. It's useful for important images that need to be seen right away. The second image (featured product) uses `loading="lazy"`, ideal for images that are not critical to see immediately.

#### Lazy loading in a gallery

```html
<img src="gallery-image-1.jpg" alt="Gallery Image 1" loading="lazy"> 
<img src="gallery-image-2.jpg" alt="Gallery Image 2" loading="lazy">
<img src="gallery-image-3.jpg" alt="Gallery Image 3" loading="lazy">
```

For image galleries, using `loading="lazy"` for each image ensures that images load as the user scrolls through the gallery, improving page load time and reducing bandwidth usage.

**Combining Lazy Loading with Art Direction**

Art direction in web design refers to the practice of adapting the presentation of content to suit different contexts, devices, or demographics. It often involves using different images or visual styles to convey a specific message or feeling that resonates with various audience segments or fits different screen sizes.

For instance, a website might display a detailed, large image on a desktop but a simpler, smaller image on a mobile device – both delivering the same message but optimized for their respective viewing contexts. 

Here’s how you can implement this alongside lazy loading:

```html
<picture>
  <source media="(min-width: 800px)" srcset="large.jpg" loading="lazy">
  <source media="(min-width: 400px)" srcset="medium.jpg" loading="lazy">
  <img src="small.jpg" alt="Responsive Image" loading="lazy">
</picture>
```

In this code, the `<picture>` element contains multiple `<source>` elements, each with a different `srcset` attribute for different screen sizes, and a default `<img>` element. The `loading="lazy"` attribute is added to each source to enable lazy loading.

### Intersection Observer for Polyfilling

The Intersection Observer API is a modern web API that provides a way to asynchronously observe changes in the intersection of a target element with an ancestor element or the viewport. Essentially, it allows you to execute code when an element enters or leaves the viewport, which is perfect for lazy loading images.

Polyfilling is a technique in web development where modern functionality is replicated in older browsers that do not support that functionality natively. A polyfill is a piece of code (usually JavaScript) that provides the technology that developers expect the browser to provide natively.

When it comes to lazy loading, if a browser does not support the `loading` attribute, we can use the Intersection Observer as a polyfill to achieve lazy loading behavior.

This JavaScript-based method involves observing `<img>` elements to determine their visibility within the viewport. When an image becomes visible, its `src` and `srcset` attributes are updated to load the actual image. 

This method requires additional markup, including a class attribute for selection, a `src` attribute for a placeholder image, and `data-src` and `data-srcset` attributes for the actual image URLs

#### First, the HTML setup:

```html
<img class="lazy" src="placeholder.jpg" data-src="actual-image.jpg" alt="Description">
```

* `class="lazy"`: A class identifier for JavaScript selection.
* `src`: A placeholder image URL.
* `data-src`: The actual image URL to be loaded.

#### Then, the JavaScript:

```javascript
document.addEventListener("DOMContentLoaded", function() {
  var lazyImages = [].slice.call(document.querySelectorAll("img.lazy"));

  if ("IntersectionObserver" in window) {
    let lazyImageObserver = new IntersectionObserver(function(entries, observer) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          let lazyImage = entry.target;
          lazyImage.src = lazyImage.dataset.src;
          lazyImage.classList.remove("lazy");
          lazyImageObserver.unobserve(lazyImage);
        }
      });
    });

    lazyImages.forEach(function(lazyImage) {
      lazyImageObserver.observe(lazyImage);
    });
  } else {
    // Fallback for browsers without Intersection Observer support
  }
});

```

This section of code demonstrates how you can use the Intersection Observer API to implement lazy loading. It checks if the Intersection Observer is supported in the browser and, if so, uses it to load images only when they enter the viewport.

## Wrapping Up

Using lazy loading, particularly through the **loading** attribute in HTML, can significantly help you improve web performance. By selectively deferring the loading of images and iframes until they are needed, this technique not only enhances the speed and efficiency of web pages but also contributes to a more seamless and responsive user experience. 

Whether you apply lazy loading to individual images, galleries, or complex responsive layouts, the versatility of the loading attribute allows you to cater to various web development scenarios, ensuring that resources are utilized effectively and efficiently. 

As web technologies continue to evolve, adopting such performance-centric strategies will become increasingly vital in delivering content that meets the expectations of modern web users.

