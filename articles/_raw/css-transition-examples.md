---
title: CSS Transition Examples – How to Use Hover Animation, Change Opacity, and More
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-10-13T17:18:52.000Z'
originalURL: https://freecodecamp.org/news/css-transition-examples
coverImage: https://www.freecodecamp.org/news/content/images/2020/10/Untitled--2--1.png
tags:
- name: animation
  slug: animation
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Said Hayani

  If you are working with web technologies like CSS, HTML, and JavaScript, it''s important
  to have some basic knowledge about CSS animations and transitions.

  In this article we are going to learn how to make some basic transition animatio...'
---

By Said Hayani

If you are working with web technologies like CSS, HTML, and JavaScript, it's important to have some basic knowledge about CSS animations and transitions.

In this article we are going to learn how to make some basic transition animations using CSS.

%[https://codesandbox.io/s/background-transition-hcosp?file=/index.html:0-1294]

## How to animate an element with basic transition on hover

In this example, we will make the opacity of an element change when a user hovers or mouses over the element.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>Static Template</title>
  </head>
  <style>
    .elem {
      background: blueviolet;
      width: 300px;
      height: 150px;
    }
    .elem:hover {
      opacity: 0.5;
    }
  </style>
  <body>
    <div class="elem"></div>
  </body>
</html>
```

![Image](https://www.freecodecamp.org/news/content/images/2020/10/hover.gif)

This is a simple transition that can be triggered when we hover over the element. We can add more than one transition that will run at the same time.

Let's add a scale transform property to add scale transition to the element.

```css
 .elem:hover {
      transform: scale(1.1);
    }
```

![Image](https://www.freecodecamp.org/news/content/images/2020/10/scale.gif)

But the transition doesn't seem to be smooth, because we didn't define the duration of the transition or use any timing function.  

If we add the `transition` property, it will make the element move more smoothly.

```css
 .elem {
      background: blueviolet;
      width: 300px;
      height: 150px;
      margin: 20px auto;
      transition: 500ms linear; 
    }
```

![Image](https://www.freecodecamp.org/news/content/images/2020/10/transition.gif)

Let's break down how the transition property works:

```css
  transition: 500ms linear;
```

* `500ms`: the duration of the transition in milliseconds
* `linear`: the timing-function

```css
div {
    transition: <property> <duration> <timing-function> <delay>;
}
```

We can add more options like below (examples from the [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Transitions/Using_CSS_transitions)):

```css
#delay {
  transition-property: font-size;
  transition-duration: 4s;
  transition-delay: 2s;
}
```

So what's this code doing?

* transition-property: the property you want to animate. It can be any CSS element like `background`, `height`, `translateY`, `translateX`, and so on. 
* transition-duration: the duration of the transition
* transition-delay: the delay before the transition starts

You can learn more about the different uses of `transition` in CSS [here](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Transitions/Using_CSS_transitions).

## How to make transitions more interactive using the animation property and keyframes

We can do more with CSS transitions to make this animation more creative and interactive.

### How to move an element with Keyframes

Let's look at an example where the element moves from point A to point B. We will be using translateX and translateY.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>Static Template</title>
  </head>
  <style>
    .elem {
      background: orange;
      width: 300px;
      height: 150px;
      animation: moveToRight 2s ease-in-out;
      animation-delay: 1000ms;
    }

    @keyframes moveToRight {
      0% {
        transform: translateX(0px);
      }
      100% {
        transform: translateX(300px);
      }
    }
  </style>
  <body>
    <div class="elem"></div>
  </body>
</html>
```

And this is what we get:

![Image](https://www.freecodecamp.org/news/content/images/2020/10/translatex.gif)

This time we used new properties like animation and keyframes. We used the `animation` property to define the animation name and duration, and keyframes let us describe how the element should move.

```css
  animation: moveToRight 2s ease-in-out;
```

Here I named the animation `moveToRight` – but you can use any name you like. The duration is `2s` , and `ease-in-out` is a timing function. 

There are other timing functions you can use like `ease-in`, `linear`, `ease-out` which basically make the animation smoother. You can learn more about the [timing functions here](https://developer.mozilla.org/en-US/docs/Web/CSS/animation-timing-function). 

`@keyframes` takes the name of the animation. In this case it's `moveToRight`.

```css
 @keyframes moveToRight {
      0% {
        transform: translateX(0px);
      }
      100% {
        transform: translateX(300px);
      }
    }
```

`keyframes` will execute the animation in multiples steps. The example above uses a percentage to represent the range or the order of the transitions. We could also use the `from` and `to` methods. like below"

```css
 @keyframes moveToRight {
     from {
        transform: translateX(0px);
      }
     to {
        transform: translateX(300px);
      }
    }
```

`from` represents the starting point or the first step of the animation.

`to` is the end point or the last step of the animation to be executed.

You may want to use a percentage in some cases. For example, say you want to add more than two transitions that will be executed in a sequence, like the following:

```css
 @keyframes moveToRight {
     0% {
        transform: translateX(0px);
      }
     50% {
        transform: translateX(150px);
      }
       100% {
        transform: translateX(300px);
      }
    }
```

We can be more creative and animate many properties at the same time like in the following example:

![Image](https://www.freecodecamp.org/news/content/images/2020/10/multiple-transitions.gif)

You can play around with properties and animation techniques in the sandbox here:

%[https://codesandbox.io/s/css-transition-examples-how-to-use-a-hover-animation-change-opacity-and-mor-forked-lcblf?fontsize=14&hidenavigation=1&theme=dark]

They are plenty more things we can do with keyframes. First, let's add more transitions to our animation. 

### How to animate more properties and include them in the transition

This time we will animate the background, and we will make the element move in a square pattern. We'll make the animation run forever using the `infinite` property as a timing function.

%[https://codesandbox.io/s/background-transition-hcosp?file=/index.html]

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>Static Template</title>
  </head>
  <style>
    .elem {
      background: orange;
      width: 250px;
      height: 250px;
      border-radius: 10px;
      animation: moveToLeft 5s linear infinite;
      animation-delay: 1000ms;
    }

    @keyframes moveToLeft {
      0% {
        transform: translateX(0px);
        background: linear-gradient(
          to right,
          #ff8177 0%,
          #ff867a 0%,
          #ff8c7f 21%,
          #f99185 52%,
          #cf556c 78%,
          #b12a5b 100%
        );
      }
      25% {
        transform: translateX(400px);
        background: linear-gradient(120deg, #84fab0 0%, #8fd3f4 100%);
      }
      50% {
        transform: translateY(200px) translateX(400px);
        background: linear-gradient(to top, #30cfd0 0%, #330867 100%);
      }

      75% {
        transform: translateX(0px) translateY(200px);
        background: linear-gradient(120deg, #f6d365 0%, #fda085 100%);
      }
      100% {
        transform: translateY(0px);
      }
    }
  </style>
  <body>
    <div class="elem"></div>
  </body>
</html>

```

Let's break it down. First we add `infinite` to make the animation run forever.

```css
animation: moveToLeft 5s linear infinite;
```

And then we split the animation into four steps. At each step, we'll run a different transition and all the animation will run in a sequence.

* First step: set the element horizontally to `translateX(0px)`, and change the background to the gradient. 

```css
 0% {
        transform: translateX(0px);
        background: linear-gradient(
          to right,
          #ff8177 0%,
          #ff867a 0%,
          #ff8c7f 21%,
          #f99185 52%,
          #cf556c 78%,
          #b12a5b 100%
        );
      }
```

* The second animation will move the element from the left to the right and change the background color.

```css
 25% {
        transform: translateX(400px);
        background: linear-gradient(120deg, #84fab0 0%, #8fd3f4 100%);
      }
```

* The third animation will move the element down using `translateY` and change the background color again.
* In the fourth step, the element will move back to the left and change the background color.
* In the fifth animation the element should go back to its original place.

## Wrapping up

In this article, we covered various things you can do with CSS transitions. You can use CSS transitions in many ways in your applications to create a better user experience.

After learning the basic of CSS animations you may want to go beyond and make more complex things that require user interaction. For this you can use JavaScript or any third party animation libraries out there.

> Hi, my name is Said Hayani I created [subscribi.io](https://subscribi.io/) to help creators, bloggers and influencers to grow their audience through newsletter.

