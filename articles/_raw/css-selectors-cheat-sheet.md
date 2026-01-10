---
title: CSS Selectors Cheat Sheet
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-07T00:36:00.000Z'
originalURL: https://freecodecamp.org/news/css-selectors-cheat-sheet
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ed4740569d1a4ca3f63.jpg
tags:
- name: CSS
  slug: css
seo_title: null
seo_desc: "In CSS, selectors are patterns used to select DOM elements.\nHere is an\
  \ example of using selectors. In the following code, a and h1 are selectors:\na\
  \ {\n  color: black;\n}\n\nh1 {\n  font-size 24px;\n}\n\nCheat sheet of common selectors\n\
  head selects the elemen..."
---

In CSS, selectors are patterns used to select DOM elements.

Here is an example of using selectors. In the following code, `a` and `h1` are selectors:

```css
a {
  color: black;
}

h1 {
  font-size 24px;
}
```

## **Cheat sheet of common selectors**

`head` selects the element with the `head` tag

`.red` selects all elements with the ‘red’ class

`#nav` selects the elements with the ‘nav’ Id

`div.row` selects all elements with the `div` tag and the ‘row’ class

`[aria-hidden="true"]` selects all elements with the `aria-hidden` attribute with a value of “true”

* Wildcard selector. Selects all DOM elements. See below for using it with other selectors

## We can combine selectors in interesting ways

### Some examples:

`li a` DOM descendant combinator. All `a` tags that are a child of `li` tags

`div.row *` selects all elements that are descendant (or child) of the elements with `div` tag and ‘row’ class

`li > a` Difference combinator. Select direct descendants, instead of all descendants like the descendant selectors

`li + a` The adjacent combinator. It selects the element that is immediately preceded by the former element. In this case, only the first `a` after each `li`.

`li, a` Selects all `a` elements and all `li` elements.

`li ~ a` The sibling combinator. Selects `a` element following a `li` element.

## Pseudo-selectors or pseudo structural classes 

These are also useful for selecting structural elements from the DOM. 

### Here are some of them:

`:first-child` Target the first element immediately inside (or child of) another element

`:last-child` Target the last element immediately inside (or child of) another element

`:nth-child()` Target the nth element immediately inside (or child of) another element. Admits integers, `even`, `odd`, or formulas

`a:not(.name)` Selects all `a` elements that are not of the `.name` class

`::after` Allows inserting content onto a page from CSS, instead of HTML. While the end result is not actually in the DOM, it appears on the page as if it is. This content loads after HTML elements.

`::before` Allows inserting content onto a page from CSS, instead of HTML. While the end result is not actually in the DOM, it appears on the page as if it is. This content loads before HTML elements.

We can use pseudo-classes to define a special state of an element of the DOM. But they don’t point to an element by themselves . 

### Some examples:

`:hover` selects an element that is being hovered by a mouse pointer

`:focus` selects an element receiving focus from the keyboard or programattially

`:active` selects an element being clicked by a mouse pointer

`:link` selects all links that have not been clicked yet

`:visited` selects a link that has already been clicked

## More info on the nth-child selector

The `nth-child` selector is a css psuedo-class taking a pattern by which to match one or more elements relative to their position among siblings.

### Syntax

```css
  a:nth-child(pattern) {
    /* Css goes here */
  }
```

### **Pattern**

The patterns accepted by `nth-child` can come in the form of keywords or an equation of the form An+B.

#### **Keywords**

##### **Odd**

Odd returns all odd elements of a given type.

```css
  a:nth-childe(odd) {
    /* CSS goes here */
  }
```

##### **Even**

Even returns all even elements of a given type.

```css
  a:nth-childe(even) {
    /* CSS goes here */
  }
```

#### **An+B**

Returns all elements matching the equation An+B for every positive integer value of n (in addition to 0).

For example, the following will match every 3rd anchor element:

```css
  a:nth-childe(3n) {
    /* CSS goes here */
  }
```

## **Games**

[CSS Diner](http://flukeout.github.io/) is a web game that teaches almost everything there is to know about combining selectors.

## **Additional references**

There are many more CSS selectors! Learn about them at [CodeTuts](http://code.tutsplus.com/tutorials/the-30-css-selectors-you-must-memorize--net-16048), [CSS-tricks.com](https://css-tricks.com/almanac/selectors/), or at [Mozilla Developer Network](https://developer.mozilla.org/en/docs/Web/Guide/CSS/Getting_started/Selectors).

