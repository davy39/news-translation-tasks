---
title: Changing H2 Element Color
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-02T02:14:00.000Z'
originalURL: https://freecodecamp.org/news/changing-h2-element-color
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9aa8740569d1a4ca26ea.jpg
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'In coding there are often many different solutions to a given problem.
  This is especially true when it comes to styling an HTML element.

  One of the easiest things to change is the color of text. But sometimes it seems
  like nothing you try is working:...'
---

In coding there are often many different solutions to a given problem. This is especially true when it comes to styling an HTML element.

One of the easiest things to change is the color of text. But sometimes it seems like nothing you try is working:

```html
<style>
  h2 .red-text {
    color: red;
  }
</style>

<h2 class="red-text" color=red;>CatPhotoApp</h2>
```

So how can you change the color of the H2 element to red?

### Option #1: Inline CSS

One way would be to use inline CSS to style the element directly.

Like with the other methods, formatting is important. Take a look again at the code above:

```html
<h2 class="red-text" color=red;>CatPhotoApp</h2>
```

To use inline styling, make sure to use the `style` attribute, and to wrap the properties and values in double quotes ("):

```html
<h2 class="red-text" style="color: red;">CatPhotoApp</h2>
```

### Option #2: Use CSS selectors

Rather than using inline styling, you could separate your HTML, or the structure and content of the page, from the styling, or CSS.

First, get rid of the inline CSS:

```html
<style>
  h2 .red-text {
    color: red;
  }
</style>

<h2 class="red-text">CatPhotoApp</h2>
```

But you need to be careful about the CSS selector you use. Take a look at the `<style>` element:

```css
h2 .red-text {
  color: red;
}
```

When there's a space, the selector `h2 .red-text` is telling the browser to target the element with the class `red-text` that's child of `h2`. However, the H2 element doesn't have a child – you're trying to style the H2 element itself.

To fix this, remove the space:

```css
h2.red-text {
  color: red;
}
```

Or just target the `red-text` class directly:

```css
.red-text {
  color: red;
}
```

