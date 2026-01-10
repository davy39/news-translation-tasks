---
title: How to Use Animations in CSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-06T23:42:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-animations-in-css
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9cbb740569d1a4ca33e0.jpg
tags:
- name: animations
  slug: animations
- name: CSS
  slug: css
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'Using CSS Animations

  CSS animations add beauty to the webpages and make transitions from one CSS style
  to the other beautiful.

  To create a CSS animation sequence, we have different sub-properties in the animation
  property in CSS :


  animation-delay

  an...'
---

## **Using CSS Animations**

CSS animations add beauty to the webpages and make transitions from one CSS style to the other beautiful.

To create a CSS animation sequence, we have different sub-properties in the `animation` property in CSS :

* `animation-delay`
* `animation-direction`
* `animation-duration`
* `animation-iteration-count`
* `animation-name`
* `animation-play-state`
* `animation-timing-function`
* `animation-fill-mode`

## Sample CSS animation sequence to move text across the screen

In the HTML part we will have a `div` with class `container` and a `h3` with the text `Hello World`:

```html
<div class="container">
    <h3> Hello World ! </h3>
</div>
```

For the CSS part:

```css
.container {
    /* We will define the width, height and padding of the container */
    /* The text-align to center */
    width: 400px;
    height: 60px;
    padding: 32px;
    text-align: center;

    /* Use the animation `blink` to repeat infinitely for a time period of 2.5s*/
    animation-duration: 2.5s;           
    animation-iteration-count: infinite;
    animation-direction: normal;        
    animation-name: blink;              
    
    /* The same can be written shorthand as     */
    /* --------------------------------------   */
    /* animation: 2.5s infinite normal blink;   */
}
@keyframes blink {
    0%, 100% {              /* Defines the properties at these frames */
        background: #333;
        color: white;
    }

    50% {                   /* Defines the properties at these frames */
        background: #ccc;
        color: black;
        border-radius: 48px;
    }
}
```

![Imgur](https://imgur.com/sczZjwm.gif)

## More information on CSS Animations:

* [A Quick intro to CSS Animations](https://www.freecodecamp.org/news/a-quick-introduction-to-css-animations-a1655375ec90/)


