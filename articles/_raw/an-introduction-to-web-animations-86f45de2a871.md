---
title: An Introduction to Web Animations
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-31T19:43:41.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-web-animations-86f45de2a871
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Ez-Q3W-m0iDOFJyExQJMdw.jpeg
tags:
- name: animation
  slug: animation
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By CodeDraken

  In this introduction to web animations article, we will cover basic CSS animations
  using pseudo-classes, transitions, and transformations.

  If you’re unsure why you should use CSS animations then take a look at these articles.

  Some basic...'
---

By CodeDraken

In this introduction to web animations article, we will cover basic CSS animations using **pseudo-classes**, **transitions**, and **transformations**.

If you’re unsure why you should use CSS animations then take a look at [these](https://developers.google.com/web/fundamentals/design-and-ux/animations/css-vs-javascript) [articles](https://medium.com/bridge-collection/improve-the-payment-experience-with-animations-3d1b0a9b810e).

Some basic ( and very ugly (for now) ) example code for this article will be on CodePen:

### Triggered

Before we jump into some animations, let’s think about how they’re going to be activated. Most of our animations won’t run immediately when a page loads. More commonly _they’ll be triggered_ by a class change (via JavaScript) or using Pseudo Classes.

#### Pseudo Foo

Here are a few [pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes) that are most commonly used for animations.

[**:hover**](https://developer.mozilla.org/en-US/docs/Web/CSS/:hover)  
The hover pseudo-class is triggered when you _hover over the target_ with the mouse. In this example, we set the `<`;p> to change its color to blue when hovered. It will revert back to its original color after the mouse moves off of it.

```
<style> #hover-example:hover {  color: blue;  cursor: pointer; }</style>
```

```
<p id=”hover-example”>Hover example</p>
```

[**:focus**](https://developer.mozilla.org/en-US/docs/Web/CSS/:focus)

> “The :focus CSS pseudo-class represents an element (such as a form input) that has received focus.” — MDN

(um… isn’t that like using a word to define itself??)

Focus is mainly used for inputs and buttons when they’re selected/activated — that is, _when you click on an input or tab into it_. In this example, clicking or tabbing into the input will cause it to change the width and its background color. Clicking out of it will cause it to revert back to its original size (and color).

```
<style> input:focus {  background-color: #f4f4f4;  width: 50vw; }</style>
```

```
<input type=”text”>
```

[**:active**](https://developer.mozilla.org/en-US/docs/Web/CSS/:active)  
Active seems similar to focus, but it’s usually only _triggered for a split second_. The first use case that comes to mind are anchors (links). In this example, we make anything with the class `activate` change while it’s being clicked (that is, while it’s active).

```
<style> .activate:active {  background-color: orange; }</style>
```

```
<p class=”activate”>Click me!</p><div class=”activate”>Activate me!</div><button class=”activate”>Hold me!</button>
```

### [Transformers](https://developer.mozilla.org/en-US/docs/Web/CSS/transform)

> “The transform CSS property lets you rotate, scale, skew or translate a given element. “ — MDN

Transform is where you take your CSS animations to the next level. There are 21 or so functions you can use with transform, but we will not cover all of them in this article.

#### Translate ( x, y )

To translate means you’re moving something. In the example below, we move whatever has the `translate` class `10rem` over on the X-axis and `5rem` over on the Y-axis. (If you’re not familiar with rem, you can use pixels, too.)

This is the shorthand function that combines X and Y, but you can use `translateX` or `translateY` instead if you prefer.

```
<style> .translate {  transform: translate(10rem, 5rem) }</style>
```

#### Scale ( x, y )

Similar to `translate`, scale also has a `scaleX`, `scaleY`, and a `scale` shorthand function. Use scale to _change the size of something_. In the example below, elements with the `scale` class are reduced to half their size.

```
<style> .scale {  transform: scale(0.5); }</style>
```

#### [Transform-origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin) ( x, y, z )

Transform-origin is an important property when dealing with animations, especially rotations. It’s a bit odd and difficult to explain with just words, and I strongly suggest looking at the MDN docs for this one if you’re not already familiar with changing origins (like in Photoshop). The documentation words it best:

> “The transformation origin is the point around which a transformation is applied” — MDN

Imagine a wheel:

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ez-Q3W-m0iDOFJyExQJMdw.jpeg)
_ferris wheel from Unsplash_

When the wheel spins it rotates around that center point. But now imagine that center point was moved to, say, the top left corner. Now the wheel rotates around that new point thus providing a very different experience. That center point is similar to the origin. See the [CodePen](https://codepen.io/CodeDraken/pen/OwOLrW) for an interactive example.

#### Rotate (angle)

Rotate does exactly what it says it does. You can specify any angle, negative, positive, any number and it will spin it around that much. There are a few different values you can use (deg, rad, grad) — [see more value types on MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/angle).

### Making things smooth

Using [transitions](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Transitions/Using_CSS_transitions) we can smooth things out and control the flow of our animations.

Transitions are like tweens or a _speed control_ for our animation. It can take 4 arguments, and I’ll cover each in detail.

#### [transition-property](https://developer.mozilla.org/en-US/docs/Web/CSS/transition-property)

Transition property is _what you’re animating_. This could be color, size, a transform, and so on. You could also say `all` to transition everything, but you should avoid doing this and be more specific.

There’s a [huge list of properties](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_animated_properties) you can animate on MDN. You should avoid animating anything not on the list.

`transition-property: all;`

#### [transition-duration](https://developer.mozilla.org/en-US/docs/Web/CSS/transition-duration)

This is _how long the animation will take to finish_. Use seconds or milliseconds.

`transition-duration: 2s;`

#### [transition-timing-function](https://developer.mozilla.org/en-US/docs/Web/CSS/transition-timing-function)

This is where it gets more complex. The transition timing function is an _acceleration curve that describes how the animation flows_. Take a look at [these](http://cubic-bezier.com/#.17,.67,.83,.67) [sites](https://easings.net/) to see what this curve looks like and how it affects the animation.

You can have it ease in then ease out, slowly start then finish fast, or a more complex flow with some slow parts and fast parts. There are many ways to have your animation flow.

Luckily, there are some predefined values we can use:

```
easeease-inease-outease-in-outlinearstep-startstep-end
```

You’ll have to play with them a bit to find the one for your animation.

Sometimes we’ll have to make our own using `cubic-bezier` (or [use a library](https://daneden.github.io/animate.css/)). For that, I suggest you find an online tool (see above links) or use your browser’s developer tools to make one.

`transition-timing-function: cubic-bezier(.29, 1.01, 1, -0.68);`

#### [transition-delay](https://developer.mozilla.org/en-US/docs/Web/CSS/transition-delay)

This is perhaps the simplest value. Transition-delay is the time it will _wait before starting the effect_. Use seconds or milliseconds.

`transition-delay: 500ms;`

#### [Transition](https://developer.mozilla.org/en-US/docs/Web/CSS/transition) (property, duration, timing, delay)

You’ve guessed it, this is the _shorthand_ to combine all of the above functions.

Here is what it looks like with one transition:

`transition: background 1s ease-in-out 0.5s;`

For multiple, you need to add them to the same transition separated by commas.

```
transition: background 1s ease-in-out 0.5s,width 2s ease-in,height 1.5s;
```

### In conclusion

This is all you need to start making interactive websites. Go practice what you’ve learned, and once you have mastered the topics covered here, you can move on to more advanced animations.

In the next article (or two) I’ll talk about keyframes, 3D transforms, performance, JavaScript animations, and more.

Thanks for reading! If you have any questions, comments, or criticism, then please leave a comment below and I’ll respond ASAP.

