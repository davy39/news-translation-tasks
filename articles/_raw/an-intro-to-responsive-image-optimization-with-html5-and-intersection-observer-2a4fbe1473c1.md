---
title: An intro to responsive image optimization with HTML5 and Intersection Observer
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-29T23:43:17.000Z'
originalURL: https://freecodecamp.org/news/an-intro-to-responsive-image-optimization-with-html5-and-intersection-observer-2a4fbe1473c1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*VjKU4KyUs4A7oaRA-3j0Dg.jpeg
tags:
- name: HTML5
  slug: html5
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Riccardo Canella

  Images often account for most of the downloaded bytes on a web page and often occupy
  a significant amount of visual space. As a result, optimizing images can frequently
  yield some of the largest byte savings and performance improv...'
---

By Riccardo Canella

Images often account for most of the downloaded bytes on a web page and often occupy a significant amount of visual space. As a result, optimizing images can frequently yield some of the largest byte savings and performance improvements for your website. The fewer bytes the browser has to download, the less time the user will have to wait for the render of useful content on the screen.

Image optimization is both a science and an art. It is a science because there are many well developed techniques and algorithms that can significantly reduce the size of an image. It is an art because there is no one definitive answer.

But how we can optimize our images from mobile form in addition to using image magic or any other web optimization tool?

### The img element

The HTML5 <img> element has been designed to give the developer the ability to optimize the images according to the screen resolution. This is done through two attributes, `srcset` and `sizes`. With a very simple syntax, you can instruct the browser to decide which one of the different image sizes are needed:

```html
<img srcset="the-death-star-320w.jpg,
             the-death-star-480w.jpg 1.5x,
             the-death-star-640w.jpg 2x"
             src="the-death-star-640w.jpg" 
alt="The Death Star">
```

The browser, in this case, will choose the image best suited to its resolution. But, the assumption is that the image should be displayed in full screen (100vw). That’s usually not an awful assumption to make.

The `sizes` attribute is used to avoid this problem and, therefore, to help the browser choose the most optimized image for that case. You can use sizes to match your CSS layout exactly and tell the browser exactly how big that image is going to be on every screen size, matching how your breakpoints work in your design.

That can get a little complicated, and honestly it might be a little dangerous. You’re putting CSS stuff in markup and you know how that goes. It can be automated or injected server-side. Even in this case the syntax is really very simple:

```html
<img srcset="the-death-star-320w.jpg,
             the-death-star-480w.jpg 1.5x,
             the-death-star-640w.jpg 2x"
             src="the-death-star-640w.jpg" 
sizes="(min-width: 800px) 50vw, 100vw"
alt="The Death Star">
```

### The picture element

There are different formats for optimizing images for the web, such as `webp`and `jpg2000`. But not all browsers are able to support them — Internet Explorer, for example. This should not preclude us from using the most optimized format for most modern browsers.

The picture element is a great way to provide alternative sources for image files, so the browser can choose depending on device capabilities. The syntax is very similar to the <video> element and allows you to use the attributes that I first showed you for the <img> element.

```html
<picture>
  <source type="image/webp" srcset="the-death-star.webp">
  <source media=”(min-width: 320px)” srcset=”the-death-star-mn.jpg”>
  <source media=”(min-width: 465px)” srcset=”the-death-star-sm.jpg”>
  <source media=”(min-width: 650px)” 
          srcset=”the-death-star-md.jpg, 
                 the-death-star-lg.jpg 1.5x”
          sizes="(min-width: 800px) 50vw, 100vw"
  >
  <img src=”the-death-star.jpg” alt=”Flowers” style=”width:auto;”>
</picture>
```

**But can I use the <picture> element everywhere?**

Unfortunately, no. Browsers like Internet Explorer 11 do not support this element.

![Image](https://cdn-media-1.freecodecamp.org/images/8Mln3ivuAOqt9Dc67yvdlpXjl9yQOj8lBEo8)
_Image [source](https://caniuse.com/#search=picture" rel="noopener" target="_blank" title=")._

**But there is a solution**. [A very small JS library](https://github.com/scottjehl/picturefill) allows you to use this element, even on unsupported browsers.

### Lazy loading the images

One of the most widespread and useful bits of advice I’ve come across is to avoid having the browser download all the images when loading the page. Only download the essential images, and make a lazy loading of the other resources. There are a lot of techniques for lazy loading. These depend on how the page is scrolled, or the next section that the user could visit.

If you’ve written lazy loading code before, you may have accomplished your task by using event handlers such as `scroll` or `resize`. This approach is the most compatible across browsers. However, modern browsers offer a more performant and efficient way to do the work of checking element visibility. This is performed via the Intersection Observer API.

Intersection Observer is easier to use and read than code relying on various event handlers. Developers only need to register an observer to watch elements, rather than writing tedious element visibility detection code. All that’s left to do for the developer is to decide what to do when an element is visible.

```html
<img class="lazy" 
     src="placeholder-image.jpg" 
     data-src="image-to-lazy-load-1x.jpg" 
     data-srcset="image-to-lazy-load-2x.jpg 2x, 
     image-to-lazy-load-1x.jpg 1x" alt="I'm an image!"
>
```

The three relevant pieces of this markup are: the `class` attribute, and the `data-src` and `data-srcset` attributes. The last two are placeholder attributes containing the URL for the image we'll load, once the element is in the viewport.

```js
document.addEventListener("DOMContentLoaded", () => {
 var lazyImages =[].slice.call(
  document.querySelectorAll("img.lazy")
 )
 if ("IntersectionObserver" in window) {
    let lazyImageObserver = 
      new IntersectionObserver((entries, observer) => {
        entries.forEach(function(entry) {
          if (entry.isIntersecting) {
            let lazyImage = entry.target;
            lazyImage.src = lazyImage.dataset.src;
            lazyImage.srcset = lazyImage.dataset.srcset;
            lazyImage.classList.remove("lazy");
            lazyImageObserver.unobserve(lazyImage);
          }
        });
      });

    lazyImages.forEach(function(lazyImage) {
      lazyImageObserver.observe(lazyImage);
    });
  } else {
    // Possibly fall back to a more compatible method here
  }
});
```

The code is very simple and easy to debug ([this is a codepen to see this code in action](https://codepen.io/malchata/pen/YeMyrQ)), but there is a big problem. The Intersection Observer API is not well supported.

![Image](https://cdn-media-1.freecodecamp.org/images/QLM7MhXfeIzVdyRrq3oY4qOtNj-FAuo-k4Nn)
_Image [source](https://caniuse.com/#search=IntersectionObserver" rel="noopener" target="_blank" title=")._

You will need to either use a [polyfill](https://github.com/w3c/IntersectionObserver/tree/master/polyfill), or implement a lazy loading based on the `resize` and `scroll` events.

### Progressive image loading

**This is a little tip:** when you export your images (JPEG, GIF , PNG) you can check the progressive option (for example on Photoshop or Sketch). Images already render progressively in a web browser. But a progressive image starts off low-resolution, and progressively enhances itself over time.

This technique is now used by almost everyone, because it allows you to immediately show a preview of the image to the user and then slowly upload the various details (for example Instagram). This method allows you to prevent users with a slow connection from leaving your site because it displays a white screen.

### Final Pill

Turning to the web, I came across a [wonderful article](https://jmperezperez.com/medium-image-progressive-loading-placeholder/) by [José M. Pérez](https://www.freecodecamp.org/news/an-intro-to-responsive-image-optimization-with-html5-and-intersection-observer-2a4fbe1473c1/undefined) on how Medium optimizes and implements progressive image loading.

If you liked the article please clap and follow me :)   
Thx and stay tuned ?  
Follow my last news and tips on [Facebook](https://www.facebook.com/CanellaRiccardo/)

