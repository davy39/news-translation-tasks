---
title: How to Create a Slideshow with HTML, CSS, and JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-03T21:14:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-slideshow
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e44740569d1a4ca3c37.jpg
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "A web slideshow is a sequence of images or text that consists of showing\
  \ one element of the sequence in a certain time interval.\nFor this tutorial you\
  \ can create a slideshow by following these simple steps:\nWrite some markup\n \
  \ <!DOCTYPE html>\n  <html..."
---

A web slideshow is a sequence of images or text that consists of showing one element of the sequence in a certain time interval.

For this tutorial you can create a slideshow by following these simple steps:

### **Write some markup**

```html
  <!DOCTYPE html>
  <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>Slideshow</title>
      <link rel="stylesheet" href="style.css">
    </head>
    <body>
      <div id="slideshow-example" data-component="slideshow">
        <div role="list">
          <div class="slide">
            <img src="" alt="">
          </div>
          <div class="slide">
            <img src="" alt="">
          </div>
          <div class="slide">
            <img src="" alt="">
          </div>
        </div>
      </div>
    <script src="slideshow.js"></script>
    </body>
  </html>
```

## Write styles to hide slides and show only one slide.

To hide the slides you have to give them a default style. It'll dictate that you only show one slide if it is active or if you want to show it.

```css
  [data-component="slideshow"] .slide {
    display: none;
  }

  [data-component="slideshow"] .slide.active {
    display: block;
  }
```

## Change the slides in a time interval.

The first step to changing which slides show is to select the slide wrapper(s) and then its slides.

When you select the slides you have to go over each slide and add or remove an active class depending on the slide that you want to show. Then just repeat the process for a certain time interval.

Keep it in mind that when you remove an active class from a slide, you are hiding it because of the styles defined in the previous step. But when you add an active class to the slide, you are overwritring the style `display:none to display:block` , so the slide will show to the users.

```js
  var slideshows = document.querySelectorAll('[data-component="slideshow"]');
  
  // Apply to all slideshows that you define with the markup wrote
  slideshows.forEach(initSlideShow);

  function initSlideShow(slideshow) {

    var slides = document.querySelectorAll(`#${slideshow.id} [role="list"] .slide`); // Get an array of slides

    var index = 0, time = 5000;
    slides[index].classList.add('active');  
    
    setInterval( () => {
      slides[index].classList.remove('active');
      
      //Go over each slide incrementing the index
      index++;
      
      // If you go over all slides, restart the index to show the first slide and start again
      if (index === slides.length) index = 0; 
      
      slides[index].classList.add('active');

    }, time);
  }
```

#### **[Codepen example following this tutorial](https://codepen.io/AndresUris/pen/rGXpvE)**

