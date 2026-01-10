---
title: Time-saving CSS techniques to create responsive images
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-12T19:18:06.000Z'
originalURL: https://freecodecamp.org/news/time-saving-css-techniques-to-create-responsive-images-ebb1e84f90d5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*aVzJTznRRfP1lM7AXe9yLw.jpeg
tags:
- name: coding
  slug: coding
- name: CSS
  slug: css
- name: General Programming
  slug: programming
- name: responsive design
  slug: responsive-design
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Adrien Zaganelli

  As a web developer, there is a high probability that you have encountered the two
  enemies of this article: images and deadlines. Sometimes, for some reasons, your
  images won’t fit the layout and you don’t want to wrap your head ar...'
---

By Adrien Zaganelli

As a web developer, there is a high probability that you have encountered the two enemies of this article: **images** and **deadlines**. Sometimes, for some reasons, your images won’t fit the layout and you don’t want to wrap your head around this for hours.

This situation has happened to me many times and I have learned from my mistakes. No more black magic hacks — here are my five favorites techniques to handle image resizing.

### the “OMG I NEED THIS ASAP” way

It’s 5:00 pm on Friday, you have to finish this page, but the images won’t fit the layout. It’s time to use your magic trick!

```css
.myImg {
  background-image: url("my-image.png");
  background-size: cover;
}
```

Sounds familiar? We’ve all done it once, doesn’t it feel like cheating to you?

Using `background` properties is very useful, they just work. Yet, remember that you should use them only for non-content images or as a replacement of text and in [some particular cases](https://stackoverflow.com/a/1469139).

### The way from the future

What if I told you this kind of magic exists also for `<img>` elements? Say “hi” to the object-fit property — which also works for videos, by the way!

```css
.myImg {
  object-fit: cover;
  width: 320px;
  height: 180px;
}
```

That’s all folks! See how when we retrieve the friendly value `cover`, we can also use `contain`.

#### **Okay what’s the trap?**

Unfortunately `object-fit` will not work on IE and older versions of Safari, but there is a [polyfill](https://github.com/bfred-it/object-fit-images/).

![Image](https://cdn-media-1.freecodecamp.org/images/1*d0wZwFpXGiAYH9_NrJCroA.png)
_source: [https://css-tricks.com/almanac/properties/o/object-fit/#article-header-id-4](https://css-tricks.com/almanac/properties/o/object-fit/#article-header-id-4" rel="noopener" target="_blank" title=")_

%[https://codepen.io/adri_zag/pen/VBQJYg]

### The “Netflix” way

You may think “nice trick man, one more way that doesn’t work in old browsers like IE ?”. Don’t worry, this one works everywhere and it is my favorite! You’ll need to wrap your image with a relative padded parent.

We will keep the image ratio with a percentage on the `padding` property. Your image will be a full size absolute child.

The code looks like this:

```css
.wrapper {
  position: relative;
  padding-top: 56.25%; /* 16:9 Aspect Ratio */
}
img {
  position: absolute;
  left: 0;
  top: 0;
  width: 100%;
  height: auto;
}
```

“Hey man, it looks complicated.”

Once you get the concept, the technique is simple and [widely used](https://www.w3schools.com/howto/howto_css_aspect_ratio.asp). Netflix uses it!

![Image](https://cdn-media-1.freecodecamp.org/images/1*rTrhAIVolZR2oQh2ou1jXg.png)
_Take a look at the class names !_

A little demo:

%[https://codepen.io/adri_zag/pen/BPrejO]

### The Simple way

You may already know this one:

```css
img {
  height: auto;
  width: 100%;
/* even more control with max-width */
  max-width: 720px;
}
```

If your layout isn’t too complicated, it works in most cases.

%[https://codepen.io/adri_zag/pen/LBQvwy]

### The Performance way (Advanced)

By performance, I mean load times. A big hero image can ruin it and make your page feel slow, especially on mobile.

Did you know that in [modern browsers](https://caniuse.com/#feat=srcset) you can change an image source depending on your page width? That’s what `srcset` is made for!

You can combine them with the HTML 5 `[<picture>](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images)` tag, which gracefully degrades with an `<img>`.

```css
<picture>
  <source media="(max-width: 799px)" srcset="elva-480w.jpg">
  <source media="(min-width: 800px)" srcset="elva-800w.jpg">
  <img src="elva-800w.jpg">
</picture>
```

%[https://codepen.io/adri_zag/pen/pZLBpx]

### To Recap

1. Use `background-image` if your image is not part of the page’s content.
2. Use `object-fit` if you don’t care about IE.
3. The padded container technique, used by Netflix, works everywhere.
4. In most cases, just add `height: auto;` in your CSS.
5. If you need fast load times, use `srcset` to load smaller images on mobile.

