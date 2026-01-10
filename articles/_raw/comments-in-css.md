---
title: CSS Comment Example – How To Comment Out CSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-26T21:57:00.000Z'
originalURL: https://freecodecamp.org/news/comments-in-css
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d7b740569d1a4ca3800.jpg
tags:
- name: CSS
  slug: css
- name: CSS3
  slug: css3
- name: Design
  slug: design
- name: style
  slug: style
seo_title: null
seo_desc: 'Comments are used in CSS to explain a block of code or to make temporary
  changes during development. The commented code doesn’t execute.

  Both single and multi-line comments in CSS begin with /* and end with */, and you
  can add as many comments to you...'
---

Comments are used in CSS to explain a block of code or to make temporary changes during development. The commented code doesn’t execute.

Both single and multi-line comments in CSS begin with `/*` and end with `*/`, and you can add as many comments to your stylesheet as you like. For example:

```css
/* This is a single line comment*/
.group:after {
  content: "";
  display: table;
  clear: both;
}

/*
  This is
  a multi-line
  comment
*/
```

You can also make your comments more readable by stylizing them:

```css
/*
***
* SECTION FOR H2 STYLE 
***
* A paragraph with information
* that would be useful for someone
* who didn't write the code.
* The asterisks around the paragraph 
* help make it more readable.
***
*/
```

## Organizing CSS with comments

In larger projects, CSS files can quickly grow in size and become difficult to maintain. It can be helpful to organize your CSS into distinct sections with a table of contents to make it easier to find certain rules in the future:

```css
/* 
*  CSS TABLE OF CONTENTS
*   
*  1.0 - Reset
*  2.0 - Fonts
*  3.0 - Globals
*  4.0 - Color Palette
*  5.0 - Header
*  6.0 - Body
*    6.1 - Sliders
*    6.2 - Imagery
*  7.0 - Footer
*/

/*** 1.0 - Reset ***/

/*** 2.0 - Fonts ***/

/*** 3.0 - Globals ***/

/*** 4.0 - Color Palette ***/

/*** 5.0 - Header ***/

/*** 6.0 - Body ***/
h2 {
  font-size: 1.2em;
  font-family: "Ubuntu", serif;
  text-transform: uppercase;
}

/*** 5.1 - Sliders ***/

/*** 5.2 - Imagery ***/

/*** 7.0 - Footer ***/
```

## A little bit more about CSS: **CSS Syntax and Selectors**

When we talk about the syntax of CSS, we’re talking about how things are laid out. There are rules about what goes where, both so you can write CSS consistently and a program (like a browser) can interpret it and apply it to the page correctly.

There are two main ways to write CSS.

### **Inline CSS**

Specifics on CSS Specificity: [CSS Tricks](https://css-tricks.com/specifics-on-css-specificity/)

Inline CSS applies styling to a single element and its children, until another style overriding the first is encountered.

To apply inline CSS, add the “style” attribute to an HTML element that you’d like to modify. Inside quotes, include a semicolon-delimited list of key/value pairs (each in turn separated by a colon) indicating styles to set.

Here’s an example of inline CSS. The words “One” and “Two” will have a background color of yellow and text color of red. The word “Three” has a new style that overrides the first, and will have a background color of green and text color of cyan. In the example, we’re applying styles to `<div>` tags, but you can apply a style to any HTML element.

```html
<div style="color:red; background:yellow">
  One
  <div>
    Two
  </div>
  <div style="color:cyan; background:green">
    Three
  </div>
</div>
```

### **Internal CSS**

While writing an inline style is a quick way to change a single element, there’s a more efficient way to apply the same style to many elements of the page at once.

The internal CSS has its styles specified in the `<style>` tag, and it is embedded in the `<head>` tag.

Here’s an example that has a similar effect as the “inline” example above, except the CSS has been extracted to its own area. The words “One” and “Two” will match the `div` selector and be red text on a yellow background. The words “Three” and “Four” will match the `div` selector too, but they also match the `.nested_div` selector which applies to any HTML element that references that class. This more specific selector overrides the first, and they end up appearing as cyan text on a green background.

```html
<style type="text/css">
  div { color: red; background: yellow; }
  .nested_div { color: cyan; background: green; }
</style>

<div>
  One
  <div>
    Two
  </div>
  <div class="nested_div">
    Three
  </div>
  <div class="nested_div">
    Four
  </div>
</div>
```

The selectors shown above are extremely simple, but they can get quite complex. For example, it’s possible to apply styles only to nested elements; that is, an element that’s a child of another element.

Here’s an example where we’re specifying a style that should only be applied to `div` elements that are a direct child of other `div` elements. The result is that “Two” and “Three” will appear as red text on a yellow background, but “One” and “Four” will remain unaffected (and most likely black text on a white background).

```html
<style type="text/css">
  div > div { color: red; background: yellow; }
</style>

<div>
  One
  <div>
    Two
  </div>
  <div>
    Three
  </div>
</div>
<div>
  Four
</div>
```

### **External CSS**

All the styling has its own document which is linked in the `<head>` tag. The extension of the linked file is `.css`

