---
title: Learn EmotionJS during your morning coffee — it’s that easy.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-21T16:50:32.000Z'
originalURL: https://freecodecamp.org/news/learn-emotionjs-during-your-morning-coffee-its-that-easy-2bc60213aca7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*V-DbP3ZYLJwyoxRneLdoog.png
tags:
- name: CSS
  slug: css
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By shahar taite

  EmotionJS is a CSS-in-JavaScript library with incredible capabilities. Let’s see
  how the world of CSS evolved to this solution, and then deep dive into what you
  can do with it today.

  The CSS wars (a recap)

  In the last couple of years,...'
---

By shahar taite

EmotionJS is a CSS-in-JavaScript library with incredible capabilities. Let’s see how the world of CSS evolved to this solution, and then deep dive into what you can do with it today.

#### The CSS wars (a recap)

In the last couple of years, we’ve seen a transition to different types of styling methods, all based on CSS. Here is the gist in chronological order:

#### **Plain old CSS**

This is the classic and simple way of applying CSS. We reference a CSS file in our index.html and it is applied to our HTML files by classic rules of CSS.

This approach has problems when applied at scale, as CSS is based on specificity which needs to be handled gently if we want to prevent CSS collisions.

It is also hard to debug when inspecting in the browser. It is hard to understand which combination of CSS properties ended up influencing the style we see on an HTML tag.

#### **CSS preprocessors**

Plain old CSS had some limitations, giving birth to some extensions of CSS such as Less and Sass. These language extensions allow us to write in a language with stronger capabilities. Examples include CSS selector nesting, functions, and more. Our build tool compiles these files into simple CSS files and they are applied in an ordinary manner.

#### **CSS modules**

This approach was introduced once web development started treating web pages as trees of components. CSS-modules is all about styling a component independently, not affecting other parts of the UI and not being affected by them.

After introducing CSS-modules into our project, each component references a CSS file with ordinary or preprocessed CSS. During the build process, our build system (such as webpack) takes each CSS class, prefixes it with the component’s name and suffixes it with a unique identifier so the class is unique.

This approach is great as it’s very easy to achieve CSS isolation. Also, it’s easy to understand which CSS rules were applied to our HTML elements and where they originated. I’ve been a big advocate of this approach — until EmotionJS was released.

#### **CSS-in-JS**

This approach challenges the practice of isolating CSS into CSS files. It allows us to state our CSS rules within our JavaScript code as JS objects.

Some frameworks such as React have built-in support for this method. A few libraries emerged from the need to provide a more isolated and scalable solution. The top libraries are Styled Components and EmotionJS.

Let’s elaborate on these.

### Styled Components versus EmotionJS!

Styled Components arrived first, and EmotionJS was admittedly heavily influenced by it.

Styled Components are simple, small React components. They define a HTML tag and its styles as a function of the component’s props.

This isolates the HTML and CSS semantics from our more functional React components. This in turn provides a more readable and maintainable development experience.

Styled components example:

What we see here is a HTML button with some CSS props.

The `color` and `background` CSS properties are determined as a function of a `primary` prop which is passed (or not) to the component.

Notice how the JSX is very simple and semantic, and the CSS and HTML part is isolated into the styled component.

Now let’s look at EmotionJS.

![Image](https://cdn-media-1.freecodecamp.org/images/1*p236DRigU2r56RfNuPhzuQ.png)

EmotionJS takes the power of styled components and adds some more useful functionality (and also the coolest logo ever).

Let’s demonstrate the things I thought were most impressive with EmotionJS.

One thing I hated up until now was maintaining [CSS media queries](https://www.w3schools.com/css/css_rwd_mediaqueries.asp).

The CSS rules for each breakpoint resided in different areas of the CSS files. It was hard to see and handle the overlapping properties.

In EmotionJS, we can create a constant holding our breakpoint widths with the help of the Facepaint library.

We can then reference this constant, declaring the values of a CSS property for each breakpoint in one place.

Let’s break this example down:

* Line 4-9: we define our breakpoint widths, in one place in our application
* Line 13–23: we define a Button component which is a div tag with some CSS properties. Its `width` and `height` values are defined as an array of values, one for each breakpoint. Notice how we don’t need to specify the `px` units. They are added automatically. Also notice the `background-color` property being dependent on the `primary` prop provided to the Button component. This is similar to the Styled components example.
* Line 26–33: in our React component, we reference our EmotionJS Button and use it as a JSX tag

#### Other features of EmotionJS

EmotionJS has some more ways of achieving some of these capabilities:

* The CSS prop — we can provide our React components with a CSS prop which is a JavaScript object or string defining our CSS properties.

* Media queries can also be targeted with the CSS prop approach

### To conclude: the good, the bad, and the emotional

![Image](https://cdn-media-1.freecodecamp.org/images/0*npYL5O9g1fbrRj6p.jpg)

**Pros:**

* Easy to integrate and replace other CSS solutions.
* Easy to identify and remove dead code compared to other solutions.
* Easier to work with media queries, values are gathered together.
* React components become more semantic as HTML and CSS are isolated.

**Cons:**

* With CSS-modules, it’s easy to understand exactly where the CSS rule is coming from when inspecting in the browser. This is because class names are generated with React component name prefixes. With EmotionJS, this doesn’t happen.
* If we define a CSS property for one media query, we need to define it for the rest as well, as we provide an array of values. In a lot of cases, we just want to address one or two media queries and leave the others as the default value.

### The verdict

EmotionJS is the next step in the right direction, dealing with the pitfalls of CSS. It provides an isolated, maintainable environment keeping our main components logic-centered and semantic.

It literally took me ten minutes to learn and integrate it and it’s a major improvement in this area.

Don’t forget to clap if you liked this, and follow me on Twitter: [https://twitter.com/shahar_taite](https://twitter.com/shahar_taite)

