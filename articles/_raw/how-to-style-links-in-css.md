---
title: How to Style Links in CSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-02T22:53:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-style-links-in-css
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9cd9740569d1a4ca3485.jpg
tags:
- name: CSS
  slug: css
- name: style
  slug: style
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: "Styling Links\nLinks can be styled with any CSS property, such as color,\
  \ font-family, font-size, and padding. Here is an easy example:\na {\n    color:\
  \ hotpink;\n}\n\nIn addition, links can be styled differently depending on what\
  \ state they are in.\nLinks a..."
---

## **Styling Links**

Links can be styled with any CSS property, such as `color`, `font-family`, `font-size`, and `padding`. Here is an easy example:

```css
a {
    color: hotpink;
}
```

In addition, links can be styled differently depending on what state they are in.

Links also have 4 states, and many programmers style each state differently. The four states are:

* `a:link`: an unvisited, unclicked link
* `a:visited`: a visited, clicked link
* `a:hover`: a link when the user’s mouse is over it
* `a:active`: a link when it is clicked

The `<a href="">` property is responsible for creating URLs and can be modified using a number of CSS styling properties, although it has a few by default:

1. Underline
2. Blue color

You can change these by adding changing the `color` and `text-decoration` properties.

```css
   color: black;
   text-decoration: none;
```

You can also style the link based on interaction using these properties, also known as link states:

* a:link - a normal, unvisited link
* a:visited - a link the user has visited
* a:hover - a link when the user mouses over it
* a:active - a link the moment it is clicked

Here is some sample CSS using the 4 states:

```css
a:link { color: red; }
a:visited { color: blue; }
a:hover { color: green; }
a:active { color: blue; }
```

**Note** that there are some _ordering rules_ for when you are setting the style for link states.

* `a:hover` MUST come after `a:link` and `a:visited`

`a:active` MUST come after `a:hover`

a:link - a normal, unvisited link a:visited - a link the user has visited a:hover - a link when the user mouses over it a:active - a link the moment it is clicked

```css
/* unvisited link */
a:link {
    color: red;
}

/* visited link */
a:visited {
    color: green;
}

/* mouse over link */
a:hover {
    color: hotpink;
}

/* selected link */
a:active {
    color: blue;
} 
```

## More on styling in CSS:

* [How to style an HTML tag directly in CSS](https://www.freecodecamp.org/news/inline-css-guide-how-to-style-an-html-tag-directly/) 
* [How to style lists with CSS](https://www.freecodecamp.org/news/how-to-style-lists-with-css/)
* [How to style buttons with CSS](https://www.freecodecamp.org/news/a-quick-guide-to-styling-buttons-using-css-f64d4f96337f/)


