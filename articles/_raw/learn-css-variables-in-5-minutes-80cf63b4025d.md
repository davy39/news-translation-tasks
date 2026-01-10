---
title: Learn CSS Variables in 5 minutes - A tutorial for beginners
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-20T18:32:50.000Z'
originalURL: https://freecodecamp.org/news/learn-css-variables-in-5-minutes-80cf63b4025d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*03NPOHNBLqOn5r22HrvlyQ.png
tags:
- name: coding
  slug: coding
- name: CSS
  slug: css
- name: Design
  slug: design
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'By Per Harald Borgen

  CSS Custom Properties (also known as Variables) is a big win for front-end developers.
  It brings the power of variables to CSS, which results in less repetition, better
  readability and more flexibility.

  Plus, unlike variables fro...'
---

By Per Harald Borgen

CSS Custom Properties (also known as Variables) is a big win for front-end developers. It brings the power of variables to CSS, which results in less repetition, better readability and more flexibility.

Plus, unlike variables from CSS preprocessors, CSS Variables are actually a part of the DOM, which has a lot of benefits. So they’re essentially like SASS and LESS variables on steroids. In this article, I’ll give you a crash course on how this new technology works.

I’ve also created a [free and interactive 8-part course on CSS Variables](https://scrimba.com/g/gcssvariables?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gcssvariables_5_minute_article), so check it out if you want to become an expert on this subject.

[Want to learn CSS Variables? Here’s my free 8-part course!](https://medium.freecodecamp.org/want-to-learn-css-variables-heres-my-free-8-part-course-f2ff452e5140)

### Why learn CSS Variables?

There are many reasons to use variables in CSS. One of the most compelling ones is that it reduces repetition in your stylesheet.

![Image](https://cdn-media-1.freecodecamp.org/images/1*03NPOHNBLqOn5r22HrvlyQ.png)

In the example above it’s much better to create a variable for the `#ffeead` colour than repeating it like we’re doing here:

![Image](https://cdn-media-1.freecodecamp.org/images/1*de4-CIacmaMo9PO6PlTkyQ.png)

Not only will this make your code easier to read, but it gives you more flexibility as well, in case you want to change this colour.

Now this has indeed been possible with SASS and LESS variables for years. However, there are a few big benefits with CSS Variables.

1. They don’t require any transpiling to work, as they’re native to the browser. So you don’t need any setup to get started, as you do with SASS and LESS.
2. They live in the DOM, which opens up a ton of benefits, which I’ll go through in this article and in my upcoming course.

Now let’s get started learning CSS Variables!

### Declaring your first CSS Variable

To declare a variable, you first need to decide which scope the variable should live in. If you want it to be available globally, simply define it on the `:root` pseudo-class. It matches the root element in your document tree (usually the `<html>` tag).

As variables are inherited this will make your variable available throughout your entire application, as all your DOM elements are descendants of the `<html>` tag.

```css
:root {  
  --main-color: #ff6f69;  
}

```

As you can see, you declare a variable just the same way you’d set any CSS property. However, the variable must start with two dashes.

To access a variable, you need to use the `var()` function, and pass in the name of the variable as the parameter.

```css
#title {  
  color: var(--main-color);  
}

```

And that’ll give your title the `#f6f69` colour:

![Image](https://cdn-media-1.freecodecamp.org/images/1*gv5ZAXzaLMT2nQVvmBei5w.png)

### Declaring a local variable

You can also create local variables, which are accessible only to the element it’s declared at and to its children. This makes sense to do if you know that a variable only will be used in a specific part (or parts) of your app.

For example, you might have an alert box which uses a special kind of colour which aren’t being used in other places in the app. In that case, it might make sense to avoid placing it in the global scope:

```css
.alert {  
  --alert-color: #ff6f69;  
}

```

This variable can now be used by its children:

```css
.alert p {  
  color: var(--alert-color);  
  border: 1px solid var(--alert-color);  
}

```

If you tried use the `alert-color` variable somewhere else in your application, for example in the navbar, it simply wouldn’t work. The browser would just ignore that line of CSS.

### Easier responsiveness with variables

A big advantage of CSS Variables is that they have access to the DOM. This isn’t the case with LESS or SASS as their variables are compiled down to regular CSS.

In practice this means that you can, for example, change the variables based upon the width of the screen:

```css
:root {  
  --main-font-size: 16px;  
}

media all and (max-width: 600px) {  
  :root {  
    --main-font-size: 12px;  
  }  
}

```

And with those simple four lines of code you have updated the main font size across your entire app when viewed on small screens. Pretty elegant, huh?

### How to access variables with JavaScript

Another advantage of living in the DOM is that you can access the variables with JavaScript, and even update them, for example, based upon user interactions. This is perfect if you want to give your users the ability to change your website (such as adjusting font size).

Let’s continue on the example from the beginning of this article. Grabbing a CSS Variable in JavaScript takes three lines of code.

```js
var root = document.querySelector(':root');  
var rootStyles = getComputedStyle(root);  
var mainColor = rootStyles.getPropertyValue('--main-color');

console.log(mainColor);   
\--> '#ffeead'

```

To update the CSS Variable simply call the `setProperty` method on the element in which the variables have been declared on and pass in the variable name as the first parameter and the new value as the second.

```js
root.style.setProperty('--main-color', '#88d8b0')

```

This main colour can change the entire look of your app, so it’s perfect for allowing users to set the theme of your site.

![By updating a single variable you can change the colour of the navbar, text and the items.](https://cdn-media-1.freecodecamp.org/images/1*ludyq87oDilcmJR98bcGwA.gif)

  
By updating a single variable you can change the colour of the navbar, text and the items.

### Browser support

Currently, 77 per cent of global website traffic supports CSS Variables, with almost 90 per cent in the US. We’re already using CSS Variables at [Scrimba.com](http://scrimba.com?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gcssvariables_5_minute_article) for a while now, as our audience is pretty tech savvy, and mostly use modern browsers.

![Image](https://cdn-media-1.freecodecamp.org/images/1*oCt-OblOjurKizk-SAITwg.png)

Ok, that was it. I hope you learned something!

If you want to learn it properly, be sure to check out [my free CSS Variables course at Scrimba.](https://scrimba.com/g/gcssvariables?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gcssvariables_5_minute_article)

---

Thanks for reading! My name is Per Borgen, I'm the co-founder of [Scrimba](https://scrimba.com?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gcssvariables_5_minute_article) – the easiest way to learn to code. You should check out our [responsive web design bootcamp](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gcssvariables_5_minute_article) if want to learn to build modern website on a professional level.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/bootcamp-banner.png)
_[Click here to get to the advanced bootcamp.](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gcssvariables_5_minute_article)_

