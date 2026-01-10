---
title: The Best CSS and CSS3 Tutorials
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-25T00:43:00.000Z'
originalURL: https://freecodecamp.org/news/best-css-and-css3-tutorial
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f10740569d1a4ca409f.jpg
tags:
- name: CSS
  slug: css
- name: CSS3
  slug: css3
- name: Tutorial
  slug: tutorial
seo_title: null
seo_desc: 'Cascading Style Sheets (CSS)

  CSS is an acronym for Cascading Style Sheets. It was first invented in 1996, and
  is now a standard feature of all major web browsers.

  CSS allows for developers to control how web pages look by “styling” the HTML structure...'
---

### **Cascading Style Sheets (CSS)**

CSS is an acronym for Cascading Style Sheets. It was first invented in 1996, and is now a standard feature of all major web browsers.

CSS allows for developers to control how web pages look by “styling” the HTML structure of that page.

CSS specifications are maintained by the [World Wide Web Consortium (W3C)](https://www.w3.org/).

You can build some pretty amazing things in CSS alone, such as this pure-CSS [Minesweeper game](https://codepen.io/bali_balo/pen/BLJONk) (which uses no JavaScript).

![Image](https://cdn-media-1.freecodecamp.org/images/1*GFcKk9KxqHAnWa1ECcKDOQ.png)

A good start is the freeCodeCamp curriculum [Introduction to Basic CSS](https://learn.freecodecamp.org/responsive-web-design/basic-css).

Another suggestion for beginners is W3C’s [Starting with HTML + CSS](https://www.w3.org/Style/Examples/011/firstcss) which teaches how to create a style sheet.

The site [CSS Zen Garden](http://www.csszengarden.com/) is a great example how the same html can be styled to look totally unique.

For a demonstration of the power of CSS, check out [Species In Pieces](http://species-in-pieces.com/#).

# Tutorials for starting with CSS and CSS3

The best place to start learning CSS is with freeCodeCamp's [2-hour intro to CSS tutorial](https://www.youtube.com/watch?v=ieTHC78giGQ).

Then, if you're feeling more adventurous, we have an entire [12-hour course that covers HTML, HTML5, and CSS in detail](https://www.youtube.com/watch?v=mU6anWqZJcc).

![Image](https://img.youtube.com/vi/mU6anWqZJcc/maxresdefault.jpg)

## **Flexbox**

Flexbox is a new way to structure content in CSS3. It provides a wonderful way to create responsive websites that work well across different screen sizes and order content.

There are 3 simple steps to use Flexbox:

1. Convert the parent container to a flex container by using `display: flex;`
2. Adjust the layout of different containers by using `flex-direction`
3. Adjust the layout of items within a container by using properties like `justify-content`, `align-items`, and so on

Flexbox allows you to efficiently lay out, align, and adjust the space among different page elements, even if you don't know their exact size. Instead, items and containers are dynamic, and will "flex" to best fill the available space.  


* **main-axis**: The primary axis of a flex container along which flex items are laid out. Keep in mind that this can be horizontal or vertical depending on the `flex-direction` property.
* **main-start | main-end**: Flex items are placed in a container from `main-start` to `main-end`.
* **main size**: A flex item's main dimension, which can be its width or height, acts as the item's main size.
* **cross axis**: The axis that is perpendicular to the main axis. The direction of the cross axis depends on the main axis's direction.
* **cross-start | cross-end**: Flex lines and items are placed in a flex container starting from the `cross-start` to the `cross-end` side.
* **cross size**: The item's cross dimension (width or height) acts as the item's cross size.

## **Grid Layout**

CSS Grid Layout, simply known as Grid, is a layout scheme that is the newest and the most powerful in CSS. It is [supported by all major browsers](https://caniuse.com/#feat=css-grid) and provides a way to position items on the page and move them around.

It can automatically assign items to _areas_, size and resize them, take care of creating columns and rows based on a pattern you define, and it does all the calculations using the newly introduced `fr` unit.

### **Why Grid?**

* You can easily have a 12-column grid with one line of CSS. `grid-template-columns: repeat(12, 1fr)`
* Grid lets you move things in any direction. Unlike Flex, where you can move items either horizontally (`flex-direction: row`) or vertically (`flex-direction: column`) - and not both at the same time - Grid lets you move any _grid item_ to any predefined _grid area_ on the page. The items you move do not have to be adjacent.
* With CSS Grid, you can **change the order of HTML elements using only CSS**. Move something from top to the right, move elements that were in the footer to the sidebar etc. Instead of moving the `<div>`from `<footer>` to `<aside>` in the HTML, you can just change its placement with `grid-area` in the CSS stylesheet.

### **Grid vs. Flex**

* Flex is one-dimensional - either horizontal or vertical, while Grid is two-dimensional, meaning you can move elements in both horizontal and vertical planes
* In Grid, we apply layout styles to the parent container and not the items. Flex, on the other hand, targets the flex item to set properties like `flex-basis`, `flex-grow`, and `flex-shrink`
* Grid and Flex are not mutually exclusive. You can use both on the same project.

### **Checking browser compatibility with `@supports`**

Ideally, when you build a site, you’d design it with Grid and use Flex as a fallback. You can find out if your browser supports grid with the `@support` CSS rule (aka feature query). Here’s an example:

```css
.container {
  display: grid; /* display grid by default */
}

@supports not (display: grid) { /* if grid is not supported by the browser */
  .container {
    display: flex; /* display flex instead of grid */
  }
}
```

### **Getting Started**

To make any element a grid, you need to assign its `display` property to `grid`, like so:

```css
.conatiner {
  display: grid;
}
```

And that’s it. You just made your `.container` a grid. Every element inside the `.container` automatically becomes a grid item.

### **Defining templates**

Rows and columns

```css
grid-template-columns: 1fr 1fr 1fr 1fr;
grid-template-rows: auto 300px;
```

Areas

```css
grid-template-areas: 
  "a a a a"
  "b c d e"
  "b c d e"
  "f f f f";
```

or

```css
grid-template-areas:
  "header header header header"
  "nav main main sidebar";
```

### **Grid Areas**

Here’s some sample code on how to define and assign grid areas:

```css
.site {
  display: grid;
  grid-template-areas: /* applied to grid container */
    "head head" /* you're assigning cells to areas by giving the cells an area name */
    "nav  main" /* how many values kind of depends on how many cells you have in the grid */
    "nav  foot";
}

.site > header {
  grid-area: head;
}

.site > nav {
  grid-area: nav;
}

.site > main {
    grid-area: main;
}

.site > footer {
    grid-area: foot;
}
```

### **The `fr` unit**

Grid introduces a new `fr` unit, which stands for _fraction_. The good thing about using the `fr` unit is that it takes care of calculations for you. Using `fr` avoids margin and padding issues. With `%` and `em` etc. it becomes a math equation when calculating `grid-gap`. If you used `fr` unit, it’ll automatically calculate both column and gutter sizes and adjust the size of the columns accordingly. Plus there will be no bleeding gaps at the end either.

## Examples

#### **Changing the order of elements based on screen size**

Let’s say you want to move the footer to the bottom on small screens and to the right on bigger screens, and there’s a bunch of other HTML elements in between the two.

The simple solution is to change the `grid-template-areas` based on the screen size. You can also **change the number of columns and rows based on the screen size**, too. This is a much cleaner and simpler alternative to Bootstrap’s Grid system (`col-xs-8 col-sm-6 col-md-4 col-lg-3`).

```css
.site {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-areas:
    "title title"
    "main header"
    "main sidebar"
}

@media screen and (min-width: 34em) { /* If the screen is big enough, use a different template for grid areas */
  .site {
    grid-template-columns: 2fr 1fr 1fr;
    grid-template-areas:
      "title title title"
      "main header header"
      "main sidebar footer"
  }
}
```

#### **More Information:**

* [CSS Grid Palyground by Mozilla](https://mozilladevelopers.github.io/playground/): Great starting point if you’re new to CSS Grids. It has visuals to help you understand the terminology easily
* [YouTube: Morten Rand-Hendriksen: CSS Grid Changes Everything (About Web Layouts)](https://www.youtube.com/watch?v=txZq7Laz7_4): This presentation will convince you in less than an hour why CSS Grids are cool and why/how you should use them.
* [Videos: Learn Grid Layout Video Series by Rachel Andrew](https://gridbyexample.com/video/): Rachel Andrew is an expert on the subject. The video titles may look strange and overwhelming, but the content is short and to the point
* [Book: Get Ready for CSS Grid Layout by Rachel Andrew](https://abookapart.com/products/get-ready-for-css-grid-layout)

# **Selectors**

Selectors are CSS rules to target HTML elements to apply styles. Tag names, class names, ids, and attributes are some of the hooks used as selectors.

## **Selector Syntax**

Selectors arranged in a specific sequence build up to a rule to target elements. An example:

```css
/* selects anchor tags */
a { 
    color: orange;
}

/* selects elements with hero class */
.hero {
    text-align: center;
}
```

## **Type of Selectors**

* TypeDescription are Type selectors and Tag names are used to select elements such as `h1` or `a`. 
* Universal Selectors apply to all elements.
*  `div *` matches all elements within div elements. 
* Attribute Selectors are Selectors that target elements based on their attributes [and optionally, their values].
*  `h1[title]` selects `h1` elements with `title` attribute. 
* Class Selectors are Selectors that target elements using their class names. 
* ID Selectors are Selectors that use ID to target elements. `#logo` selects the element with `logo` as ID. 
* Pseudo-class Selectors are Special selectors that target elements based on their state. `a:hover` selector applies style when pointer hovers over links.

## **Selector Combinators**

Combinator: Purpose `white space`Descendant combinator. `.nav li` selects all `li` children within the class `.nav`, including nested `li` elements.`>`Child combinator. `.menu > li` selects all li that are direct children of elements with `.menu` class.`+`Adjacent sibling combinator. `.logo + h1` targets `h1` that is an immediate sibling to `.logo` class.`~`General sibling combinator. `header ~ div` targets `div` elements that are siblings to `header` elements.

This section details all of these electors.

#### **More Information:**

You can learn more about selectors on these resources:

* [Official CSS3 Selectors specification](https://www.w3.org/TR/css3-selectors)
* [Selectors page on Mozilla Developer Network](https://developer.mozilla.org/en-US/docs/Learn/CSS/Introduction_to_CSS/Selectors)
* [CSS Selectors Cheat Sheet on FreeCodeCamp Guides](https://guide.freecodecamp.org/css/tutorials/css-selectors-cheat-sheet)

Selectors in CSS (cascading style sheets) are determined based on _specificity._ With this we are able to be more specific on our style rules and override other rules that may be targeting the same element but are not as specific. 

The way this specificity hierarchy works is based on weight. This means that an element Selector has a weight of 1 (one), a class selector has a weight of 10 (ten) and a id selector has a weight of 100 (one hundred). We are able to combine different selectors together be more specific on the element we want to change.

As an example:

```css
    p {
      color: blue;
    }
    p .red {
       color: red;
    }
```

Our type selector p will select all p elements in our html document, but it only has a weight of one. In contrast, the class selector has a weight of 11, because we are combining a type selector with a class selector (this selector is matching all p elements with a class of red). 

Note: 

* Directly targeted rules will always have precedence over rules which inherit elements from their ancestor. 
* Specificity is only applied when multiple declarations are targeting the same element, and only then this rule is applied.
* Specificity is usually why some of the style rules do not apply to elements when you would expect them to.

## **CSS Display**

The display property specifies the type of box used for an HTML element. It has 20 possible keyword values. The commonly used ones are:

```css
    .none             {display: none}
    .block            {display: block}
    .inline-block     {display: inline-block}
    .inline           {display: inline}
    .flex             {display: flex}
    .inline-flex      {display: inline-flex}
    .inline-table     {display: inline-table}
    .table            {display: table}
    .inherit          {display: inherit}
    .initial          {display: initial}
```

The `display:none` property can often be helpful when making a website responsive. For example, you may want to hide an element on a page as the screen size shrinks in order to compensate for the lack of space. `display: none` will not only hide the element, but all other elements on the page will behave as if that element does not exist. 

This is the biggest difference between this property and the `visibility: hidden` property, which hides the element but keeps all other page elements in the same place as they would appear if the hidden element was visible.

These keyword values are grouped into six categories:

* `<display-inside>`
* `<display-outside>`
* `<display-listitem>`
* `<display-box>`
* `<display-internal>`
* `<display-legacy>`

