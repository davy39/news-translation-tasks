---
title: How I remember CSS Grid properties
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2018-10-25T05:38:32.000Z'
originalURL: https://freecodecamp.org/news/how-i-remember-css-grid-properties-3afee895763
coverImage: https://cdn-media-1.freecodecamp.org/images/0*9_DylWfIulrq5tTl.png
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
seo_title: null
seo_desc: 'The syntax for CSS Grid is foreign and hard to remember. But if you can’t
  remember CSS Grid’s syntax, you won’t be confident when you use CSS Grid.

  To wield CSS Grid effectively, you need to remember its properties and values.

  I want to share how I r...'
---

The syntax for CSS Grid is foreign and hard to remember. But if you can’t remember CSS Grid’s syntax, you won’t be confident when you use CSS Grid.

To wield CSS Grid effectively, you need to remember its properties and values.

I want to share how I remember the most common CSS Grid properties today. This will help you use CSS Grid without googling like a maniac.

### Groups of properties

I remember CSS Grid according to four groups of properties:

1. The explicit grid
2. Gaps
3. Aligning things
4. The implicit grid

### The explicit grid

Let’s say you want to make a grid with 4 columns and 3 rows. You say this 4 columns and 3 rows out loud. It’s explicit.

If you declare the number of rows and columns in your grid, the grid is explicit.

You can use two properties to make an explicit grid:

1. `grid-template-columns`
2. `grid-template-rows`

`grid-template-columns` lets you define the number of columns. `grid-template-rows` lets you define the number of rows.

```
.grid {  display: grid;   grid-template-columns: 1fr 1fr 1fr 1fr;   grid-template-rows: 3em 3em 3em;}
```

This creates a grid with four columns and three rows.

See the Pen [XPyGZp](https://codepen.io/zellwk/pen/XPyGZp/) by Zell Liew ([@zellwk](https://codepen.io/zellwk)) on [CodePen](https://codepen.io/).

How do you know there are four columns and three rows?

`grid-template-columns` create a new column for each length value you add to it. In the `grid-template-columns` declaration above, we have four `1fr` values. This means four columns.

`grid-template-rows` work the same way. The grid above has three `3em` values, which means it has 3 rows.

`grid-template-columns` and `grid-template-rows` can also take in values like `repeat`, `autofill`, `autofit`, `minmax`. We won’t go into these values in this article.

What you need to know now is you can create an explicit grid with two properties:

1. `grid-template-columns`: creates columns
2. `grid-template-rows`: creates rows

### Positioning items in your grid

You can control the position of items in a grid with two properties.

These two properties can only be used on a grid item.

`grid-column` lets you choose which column(s) you want to place your grid item. It is a shorthand for `grid-column-start` and `grid-column-end`.

It works this way: `grid-column-start / grid-columns-end`.

```
/* Using the longhand */.grid-item {  grid-column-start: 1;   grid-column-end: 3;}
```

```
/* Using the shorthand */.grid-item {  grid-column: 1 / 3;}
```

Note: You can also use the `span` keyword to tell CSS Grid how many columns you want your item to take up.

```
/* Using the longhand */.grid-item {  grid-column-start: 1; /* Start at column one */  grid-column-end: span 2; /* Width is two columns */}
```

See the Pen [Explicit Grid properties](https://codepen.io/zellwk/pen/dqQrmm/) by Zell Liew ([@zellwk](https://codepen.io/zellwk)) on [CodePen](https://codepen.io/).

`grid-row` lets you choose which row(s) you want to place your grid item. It is a shorthand for `grid-row-start` and `grid-row-end`.

It works this way: `grid-row-start / grid-row-end`.

```
/* Using the longhand */.grid-item {  grid-row-start: 1;   grid-row-end: span 2;}
```

```
/* Using the shorthand */.grid-item {  grid-row: 1 / span 2;}
```

See the Pen [Positioning items (rows)](https://codepen.io/zellwk/pen/OoaqoG/) by Zell Liew ([@zellwk](https://codepen.io/zellwk)) on [CodePen](https://codepen.io/).

### Positioning items in named areas

You can name parts of your grid if you don’t like counting rows and columns. These named parts are called grid areas. To create a grid area, you use `grid-template-area` on the grid.

Some notes on creating grid areas:

1. You must name every grid area
2. If you don’t want to name an area, use `.`
3. Each group separated by inverted commas (`"row1" "row2"`) signifies a row
4. Each value within inverted commas (`"area1 area2"`) signifies an area

The example below has three grid areas:

1. `header` on the first two and takes up 4 columns
2. `main` on the second row and takes up the middle 2 columns
3. `footer` on the third row and takes up 4 columns

```
.grid {  grid-template-areas: "header header header header"                      ".      main   main   .     "                      "footer footer footer footer";}
```

To place items in a grid area, you use the `grid-area` property on the grid item.

To place items on a grid-area, you use `grid-area`.

```
.grid {  display: grid;   /* ... */}
```

```
main {  grid-area: main}
```

See the Pen [Grid-template-area](https://codepen.io/zellwk/pen/PdxLyg/) by Zell Liew ([@zellwk](https://codepen.io/zellwk)) on [CodePen](https://codepen.io/).

### How to remember these properties

You learned 6 properties so far:

1. `grid-template-columns`
2. `grid-template-rows`
3. `grid-template-areas`
4. `grid-column`
5. `grid-row`
6. `grid-area`

Some tips to remember these 6 properties:

1. The `template` keyword can only be used on the grid  
 a) They’re used to declare grids and named areas  
 b) Properties with the `template` keyword are plural
2. Properties for grid items do not have the `template` keyword  
a) These properties are singular  
b) These properties affect positioning

### Gaps

When you create a grid, you can create spaces between columns and rows. These spaces are called gaps.

There are three properties to remember:

1. `grid-column-gap`
2. `grid-row-gap`
3. `grid-gap`

`grid-column-gap` determines the space between columns.

`grid-row-gap` determines the space between rows.

`grid-gap` is a shorthand for `grid-column-gap` and `grid-row-gap`.

For this shorthand:

1. the `column` value comes first: `column-gap / row-gap`
2. If you use a single number, both values will be that number.

```
/* Different values */.grid {  grid-column-gap: 1em;  grid-row-gap: 2em;}
```

```
.grid {  grid-gap: 1em / 2em; }/* Same values */.grid {  grid-column-gap: 1em;  grid-row-gap: 1em;}
```

```
.grid {  grid-gap: 1em;}
```

See the Pen [Explicit Grid with gap](https://codepen.io/zellwk/pen/bxQZZG/) by Zell Liew ([@zellwk](https://codepen.io/zellwk)) on [CodePen](https://codepen.io/).

### Aligning things

This is where many people get confused.

There are six properties to align things:

1. `justify-content`
2. `align-content`
3. `justify-items`
4. `align-items`
5. `justify-self`
6. `align-self`

You can see two groups of patterns here:

* The first group is `justify` vs `align`
* The second group is `content`, `items`, and `self`

These two groups of properties tell you what you’re dealing with. If you understand the property keyword, you’ll know how to use them.

### Justify vs align

Each CSS Grid has two axes:

1. The main-axis
2. The cross-axis

When you `justify` something, you’re changing the alignment according to the _main-axis_. When you `align` something, you’re changing the alignment according to the _cross-axis_.

Here’s an easy way to identify the main and cross axis:

1. Identify the direction of the language
2. Main-axis is the way you read the language
3. Cross-axis is the way you read after you read the end of the first line.

Let’s take English as an example. How do you read English?

1. Left to right
2. Top to bottom

So the main and cross axis is:

1. Main: left to right
2. Cross: top to bottom

Note: the main and cross axes change if you change the language direction with `writing-mode`.

### Content, items, and self

`justify-content` and `align-content` lets you align the grid itself to the available space outside of the grid. You will only need these properties if your grid is smaller than its defined area (which is rare).

```
.grid {  justify-content: /* some value */;   align-content: /* some value */; }
```

You can pick from seven values:

1. **start**: flush grid to the start of the axis
2. **end**: flushed grid to the end of the axis
3. **center**: align grid to the center of the axis
4. **stretch**: grid fills the axis (this is the default value)
5. **space-between**: spreads whitespace between grid items. No whitespace at the ends
6. **space-around**: spreads whitespace around each grid item
7. **space-evenly**: spreads whitespace evenly around all grid items including the ends

![Image](https://cdn-media-1.freecodecamp.org/images/Bji3J37rICTz6Njcts4IL6ejCB-Z4Usg6DkH)

The pictures above are taken from CSS Tricks’s [A complete Guide to Grid](https://css-tricks.com/snippets/css/complete-guide-grid/). It explains what each value does in detail. You can read it for more information.

Our focus here is remembering the properties and how to use them. Let’s get back on track with the next set of properties.

`justify-items` and `align-items` lets you align grid-items to any available whitespace in their respective cells. Most of the time, when you’re trying to align things, you’re looking for either `justify-items` or `align-items`.

```
.grid {  justify-items: /* some value */;   align-items: /* some value */; }
```

You can pick from the same four values:

1. **start**: flush item to the start of the axis
2. **end**: flush item to the end of the axis
3. **center**: align item to the center of the axis
4. **stretch**: fills the axis (this is the default value)

![Image](https://cdn-media-1.freecodecamp.org/images/QsF6-6HHFmOHMEv4utrE0MZd-xelyg5ueVb6)

`justify-self` and `align-self` does the same thing as `justify-items` and `align-items`. The difference is it lets you change the alignment for only one grid-item.

```
.grid-item {  justify-self: /* some value */;  align-self: /* some value */;}
```

### Implicit Grid

Let’s say you created a CSS Grid, but you don’t have enough rows. In this example below, I only created an explicit grid for three items (3 columns, 1 row).

```
.grid {  display: grid;   grid-template-columns: 1fr 1fr 1fr;  grid-template-row: 3em;}
```

But I have six items!

```
<!-- This is HTML -->
```

```
<div class="grid">  <div class="grid-item"></div>  <div class="grid-item"></div>  <div class="grid-item"></div>  <div class="grid-item"></div>  <div class="grid-item"></div>  <div class="grid-item"></div></div>
```

When you don’t have enough space in your explicit grid, CSS Grid will help you create additional grids automatically. By default, it’ll create more rows.

If you want to switch the grid direction, you’ll set `grid-auto-flow` to `row`.

This automatically created parts are called the implicit grid.

You can adjust the automatically created column(s) or row(s) with these two properties:

1. `grid-auto-columns`
2. `grid-auto-rows`

```
.grid {  display: grid;   grid-template-columns: 1fr 1fr 1fr;  grid-template-rows: 3em;   grid-auto-rows: 6em;}
```

See the Pen [Implicit grid](https://codepen.io/zellwk/pen/yxQrJb/) by Zell Liew ([@zellwk](https://codepen.io/zellwk)) on [CodePen](https://codepen.io/).

### How to remember the implicit grid

`auto` is the keyword you want to watch out for.

1. `template` creates the explicit grid
2. `auto` creates the implicit grid

I use the implicit grid a lot. I’ll share how I use CSS Grid in another article.

### Wrapping up

That’s almost every CSS Grid property you need to know for 80% of your grids! Here’s a summary of the properties you learned:

* Creating a grid  
a. Explicit:   
 1) `grid-template-columns`   
 2) `grid-template-rows`   
 3) `grid-template-areas`   
b. Implicit:  
 1) `grid-auto-columns`   
 2) `grid-auto-rows`
* Gaps   
 1) `grid-column-gap`  
 2) `grid-row-gap`   
 3) `grid-gap`
* Positioning items in a grid  
1) `grid-column`  
2) `grid-row`
* Aligning things  
1) `justify-content`   
2) `align-content`   
3) `justify-items`   
4) `align-items`   
5) `justify-self`   
6) `align-self`

I hope this helps you remember CSS Grid! All the best!

Thanks for reading. Did this article help you in any way? If you did, [I hope you consider sharing it](http://twitter.com/share?text=How%20I%20remember%20CSS%20Grid%20properties%20by%20@zellwk%20?%20&url=https://zellwk.com/blog/remember-css-grid-properties/&hashtags=). You might help someone out. Thank you!

This article was originally posted at [zellwk.com](https://zellwk.com/blog/remember-css-grid-properties/).  
Sign up for my [newsletter](https://zellwk.com/) if you want more articles to help you become a better frontend developer.

