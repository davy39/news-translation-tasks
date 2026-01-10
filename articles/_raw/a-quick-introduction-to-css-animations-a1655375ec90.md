---
title: A quick introduction to CSS animations
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2018-05-03T15:47:53.000Z'
originalURL: https://freecodecamp.org/news/a-quick-introduction-to-css-animations-a1655375ec90
coverImage: https://cdn-media-1.freecodecamp.org/images/1*feAfQ6VwBLSlXlYVmUxqLQ.png
tags:
- name: CSS
  slug: css
- name: education
  slug: education
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "Interested in learning CSS? Get my CSS Handbook \n\nIntroduction\nAn animation\
  \ is applied to an element using the animation property.\n.container { animation:\
  \ spin 10s linear infinite;}\nspin is the name of the animation, which we need to\
  \ define separatel..."
---

> Interested in learning CSS? Get my [CSS Handbook](https://flaviocopes.com/page/css-handbook/) 

#### Introduction

An animation is applied to an element using the `animation` property.

```
.container { animation: spin 10s linear infinite;}
```

`spin` is the name of the animation, which we need to define separately. We also tell CSS to make the animation last 10 seconds, perform it in a linear way (no acceleration or any difference in its speed), and to repeat it infinitely.

You must **define how your animation works** using **keyframes**. Here’s an example of an animation that rotates an item:

```
@keyframes spin { 0% {  transform: rotateZ(0); } 100% {  transform: rotateZ(360deg); }}
```

Inside the `@keyframes` definition you can have as many intermediate waypoints as you want.

In this case, we instruct CSS to make the transform property to rotate the Z axis from 0 to 360 grades, completing the full loop.

You can use any CSS transform here.

Notice how this does not dictate anything about the temporal interval the animation should take. This is defined when you use it via `animation`.

#### A CSS Animations Example

I want to draw four circles, all with a starting point in common, all 90 degrees distant from each other.

```
<div class="container">  <div class="circle one"></div>  <div class="circle two"></div>  <div class="circle three"></div>  <div class="circle four"></div></div>
```

```
body {  display: grid;  place-items: center;  height: 100vh;}
```

```
.circle { border-radius: 50%; left: calc(50% - 6.25em); top: calc(50% - 12.5em); transform-origin: 50% 12.5em; width: 12.5em; height: 12.5em; position: absolute; box-shadow: 0 1em 2em rgba(0, 0, 0, .5);}
```

```
.one,.three { background: rgba(142, 92, 205, .75);}
```

```
.two,.four { background: rgba(236, 252, 100, .75);}
```

```
.one { transform: rotateZ(0);}
```

```
.two { transform: rotateZ(90deg);}
```

```
.three { transform: rotateZ(180deg);}
```

```
.four { transform: rotateZ(-90deg);}
```

You can see them in this Glitch:

Let’s make this structure (all the circles together) rotate. To do this, we apply an animation on the container, and we define that animation as a 360 degrees rotation:

```
@keyframes spin { 0% {  transform: rotateZ(0); } 100% {  transform: rotateZ(360deg); }}
```

```
.container { animation: spin 10s linear infinite;}
```

See it here:

You can add more keyframes to have funnier animations:

```
@keyframes spin { 0% {  transform: rotateZ(0); } 25% {  transform: rotateZ(30deg); } 50% {  transform: rotateZ(270deg); } 75% {  transform: rotateZ(180deg); } 100% {  transform: rotateZ(360deg); }}
```

See the example:

### The CSS animation properties

CSS animations offers a lot of different parameters you can tweak:

* **animation-name —** the name of the animation which references an animation created using keyframes
* **animation-duration —** how long the animation should last, in seconds
* **animation-timing-function —** the timing function used by the animation (common values: linear, ease). Default: ease
* **animation-delay —** optional number of seconds to wait before starting the animation
* **animation-iteration-count —** how many times the animation should be performed. Expects a number, or infinite. Default: 1
* **animation-direction —** the direction of the animation. Can be normal, reverse, alternate or alternate-reverse. In the last 2, it alternates going forward and then backwards
* **animation-fill-mode —** defines how to style the element when the animation ends, after it finishes its iteration count number. None or backwards go back to the first keyframe styles. Forwards and both use the style that’s set in the last keyframe
* **animation-play-state —** if set to paused, it pauses the animation. Default is running.

The `animation` property is a shorthand for all these properties, in this order:

```
.container {  animation: name             duration             timing-function             delay             iteration-count             direction             fill-mode             play-state;}
```

This is the example we used above:

```
.container { animation: spin 10s linear infinite;}
```

### JavaScript events for CSS Animations

Using JavaScript, you can listen for the following events:

* `animationstart`
* `animationend`
* `animationiteration`

Be careful with `animationstart`, because if the animation starts on page load, your JavaScript code is always executed after the CSS has been processed. Then the animation will already be started and you cannot intercept the event.

```
const container = document.querySelector('.container')container.addEventListener('animationstart', (e) => { //do something}, false)container.addEventListener('animationend', (e) => { //do something}, false)container.addEventListener('animationiteration', (e) => { //do something}, false)
```

> Interested in learning CSS? Get my [CSS Handbook](https://flaviocopes.com/page/css-handbook/) 

