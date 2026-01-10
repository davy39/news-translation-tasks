---
title: How I style my websites with my favorite CSS resets
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2019-03-25T18:05:27.000Z'
originalURL: https://freecodecamp.org/news/how-i-style-my-websites-with-my-favorite-css-resets-7ace41dbc43d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*cHZLhJhJgiRK48Dzhem5-w.jpeg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'Many frontend developers begin styling their websites with Normalize. Some
  developers have personal preferences that they add on to Normalize.css. I have my
  preferences, too.

  In this article, I want to share these preferences with you, my personal CS...'
---

Many frontend developers begin styling their websites with Normalize. Some developers have personal preferences that they add on to Normalize.css. I have my preferences, too.

In this article, I want to share these preferences with you, my personal CSS reset (that I use in addition to Normalize.css).

I categorize the resets into 8 categories:

1. Box sizing

2. Removing margins and paddings

3. Lists

4. Forms and buttons

5. Images and embeds

6. Tables

7. The hidden attribute

8. Noscript

# Box Sizing

The `box-sizing` property changes how the CSS Box model works. It changes how `width`, `height`, `padding`, `border`, and `margin` properties are calculated.

The default setting for `box-sizing` is `content-box`. I prefer changing this to `border-box` because it’s easier for me to style `padding` and `width`.

For more info on Box Sizing, you might be interested in “[Understanding Box sizing](https://zellwk.com/blog/understanding-css-box-sizing/)”.

```css
html {
  box-sizing: border-box;
}
*,
*::before,
*::after {
  box-sizing: inherit;
}
```

# Removing margins and paddings

Browsers set different margins and paddings for different elements. These default settings throw me off when I’m not aware. When I code, I prefer to set all margins and paddings myself.

```css
/* Reset margins and paddings on most elements */
body,
h1,
h2,
h3,
h4,
h5,
h6,
ul,
ol,
li,
p,
pre,
blockquote,
figure,
hr {
  margin: 0;
  padding: 0;
}
```

# Lists

I use unordered lists in many situations, and I don’t need a `disc` style in most of them. Here, I set `list-style` to none. When I need the `disc`style, I set it back manually on the specific `<ul>`.

```css
/* Removes discs from ul */
ul {
  list-style: none;
}
```

# Forms and buttons

Browsers don’t inherit typography for forms and buttons. They set `font` to `400 11px system-ui`. I find this mind-boggling and weird. I always have to make them inherit from ancestor elements manually.

```css
input,
textarea,
select,
button {
  color: inherit; 
  font: inherit; 
  letter-spacing: inherit; 
}
```

Different browsers have styled the borders for forms elements and buttons differently. I dislike these default styles, and would prefer to set them to `1px solid gray`.

```css
button {
  border-radius: 0; 
  padding: 0.75em 1em;
  background-color: transparent;
}
```

I made a few more adjustments to buttons:

1. Set button padding to `0.75em` and `1em` because they seem like sensible defaults from my experience.
2. Removed the default `border-radius` that’s applied to buttons.
3. Forced background color to be transparentbutton {   border-radius: 0;    padding: 0.75em 1em;   background-color: transparent; }

Finally, I set `pointer-events: none` to elements within a button. This is mainly used for JavaScript interaction.

(When users click on something in a button, `event.target` is the thing they clicked on, not the button. This style makes it easier to work with `click` events if there are HTML elements inside a button).

```css
css button * {   pointer-events: none; }
```

Media elements include images, videos, objects, iframes, and embed. I tend to let these elements conform to the width of their containers.

I also set these elements to `display: block` because `inline-block`creates unwanted whitespace at the bottom of the element.

```css
embed,
iframe,
img,
object,
video {
  display: block;
  max-width: 100%;
}
```

# Tables

I rarely use tables, but they may be useful sometimes. Here’s the default styles I’ll begin with:

```css
table {
  table-layout: fixed;
  width: 100%;
}
```

When an element has a `hidden` attribute, they should be hidden from view. Normalize.css does this for us already.

```css
[hidden] {
  display: none;
}
```

The problem with this style is its low specificity.

I often add `hidden` to other elements I style with a class. A class’s specificity is high than an attribute, and the `display: none` property doesn’t work.

This is why I opt to bump up `[hidden]`'s specificity with `!important`.

```css
[hidden] {
  display: none !important;
}
```

# Noscript

If a component requires JavaScript to work, I’ll add a `<noscript>` tag to let users know (if they’ve disabled JavaScript).

This creates default styles for the `<noscript>` tag.

```css
/* noscript styles */
noscript {
  display: block;
  margin-bottom: 1em;
  margin-top: 1em;
}
```



# Wrapping up

Everyone begins their projects differently. Please feel free to use any of these styles I mentioned. Here’s a [Github repo](https://github.com/zellwk/css-reset) of my personal CSS Resets.

Do you have any recommendations that would help improve this CSS Reset file? If you do, feel free to reach out and let me know!

Thanks for reading. Did this article help you out? If it did, I hope you consider [sharing it](https://twitter.com/share?text=My%20CSS%20reset%20by%20@zellwk%20%F0%9F%91%87%20&url=https://zellwk.com/blog/css-reset/). You might help someone else out. Thanks so much!

---

This article was originally posted at [my blog](https://zellwk.com/blog/css-reset). Sign up for my [newsletter](https://zellwk.com/) if you want more articles to help you become a better frontend developer.

