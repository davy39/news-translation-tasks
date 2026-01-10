---
title: Flexbox vs Grid - How to Build the Most Common HTML Layouts
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-14T17:43:43.000Z'
originalURL: https://freecodecamp.org/news/flexbox-vs-grid-how-to-build-the-most-common-html-layouts
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/halacious-weRQAu9TA-A-unsplash-1.jpg
tags:
- name: CSS
  slug: css
- name: CSS Grid
  slug: css-grid
- name: flexbox
  slug: flexbox
- name: HTML
  slug: html
seo_title: null
seo_desc: "By Ondrej Polesny\nThere are so many great CSS resources all over the internet.\
  \ But what if you just want a simple layout and you want it NOW? \nIn this article,\
  \ I describe the 5 most common web page layouts and how to build them using both\
  \ Flexbox and..."
---

By Ondrej Polesny

There are so many great CSS resources all over the internet. But what if you just want a simple layout and you want it NOW? 

In this article, I describe the 5 most common web page layouts and how to build them using both Flexbox and Grid.

### How this will work

There is a link below every layout for the full HTML and CSS code on CodePen. 

Note that I'm using SASS for composing style definitions, so if you want to do the same on your local, install SASS using:

```js
npm i sass -g
```

## Basic card template

![Image](https://www.freecodecamp.org/news/content/images/2020/08/card.png)

I used the above card as the base of the web page layout. It's composed of three elements in a vertical direction, so normal `div` blocks would work well. However, I will later need to make the middle element - the text paragraph - stretch.

Here both Flexbox and Grid do the job seamlessly. I prefer Flexbox as it's more straightforward to me.

**Winner: Flexbox**

[CodePen Flexbox](https://codepen.io/ondrabus/pen/rNeOEQJ), [CodePen Grid](https://codepen.io/ondrabus/pen/mdPeZvd)

Now let's start creating our different layouts.

## #1 Vertically and horizontally centered card

![Image](https://www.freecodecamp.org/news/content/images/2020/08/card--1-.png)

With Flexbox, we need one element that centers horizontally, and another (the child element) that centers vertically. 

The order of items is defined by `flex-direction`. How the element positions itself in the available space is set by `align-self` on the element or `align-items` on its parent.

With Grid, we need three columns and three rows. Then we position the card in the middle cell. 

The horizontal centering is easy. We define three columns and their sizes using `grid-template-columns: auto 33% auto` as the card should be as wide as 1/3 of the visible area. 

The problem is, we don't know the vertical dimensions. We want the top and bottom rows to take up the remaining space which is not possible with grid. The card is centered, but its height depends on the height of the window. 

However, we can solve this with an additional wrapping element around the card and center it using `margin`.

**Winner: Flexbox**

[CodePen Flexbox](https://codepen.io/ondrabus/pen/vYGYobr), [CodePen Grid](https://codepen.io/ondrabus/pen/yLOYdLO)

## #2 Two cards vertically and horizontally centered 

![Image](https://www.freecodecamp.org/news/content/images/2020/08/two-cards.png)

Often we need to center more than just one element. These two cards should also maintain the same height if one or the other contains longer text.

With Flexbox, we need to wrap both cards in another element and use it to center both cards at once. 

We can't use `align-items` here as that applies to the Y-axis in this case. We need to define how the remaining space on the X-axis should be distributed with `justify-content: center`. That ensures both cards are horizontally centered.

If we omit the variable height problem of Grid, we can achieve the same result even without any additional wrapping elements. This time we define grid with five columns with `grid-template-columns: auto 33% 50px 33% auto`. The rest stays the same as in the previous example.

**Winner: Flexbox**

[CodePen Flexbox](https://codepen.io/ondrabus/pen/mdPybJa), [CodePen Grid](https://codepen.io/ondrabus/pen/RwaWXOp)

## #3 Multiple cards with same width and height

![Image](https://www.freecodecamp.org/news/content/images/2020/08/cards.png)

This is another typical use case for blogs, e-commerce sites, or generally any site that displays some kind of listing. We want the cards to have the same width and height. Height needs to be inferred from the greatest element in the list.

This can be done in Flexbox using `flex-wrap: wrap`. Elements will wrap to the next line if their width exceeds the remaining space of each line. However, the same height is only preserved in the scope of a single line, unless you define it explicitly.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/3-flexbox-1.png)

Grid shows its true power here. This layout can be created using `grid-auto-rows: 1fr` which enforces the same height on all rows.

**Winner: Grid**

[CodePen Flexbox](https://codepen.io/ondrabus/pen/LYNpawv), [CodePen Grid](https://codepen.io/ondrabus/pen/QWNjPLg)

## #4 Alternating text and images vertically and horizontally centered

![Image](https://www.freecodecamp.org/news/content/images/2020/08/alternating-text.png)

In this example, we have text with CTA buttons accompanied by an image on the other side. Both components should be vertically centered, as their size can vary.

This is a piece of cake for Flexbox. Every row is an `article` element split into two wrapping containers, `.img` and `.content`. They are required for even size distribution (`flex-basis: 50%`). 

Vertical centering of the inner content is defined by `align-items: center`. 

The alternation is achieved by reversing the direction of Flexbox by `flex-direction: row-reverse` on every odd article.

Grid handles this use-case nicely too. We don't need to define one giant grid, but rather one for each `article`. 

It defines equally wide columns that are vertically centered using `align-items: center`. 

The alternation is defined on the cell-level by switched values for `grid-column`.

**Winner: tie**

[CodePen Flexbox](https://codepen.io/ondrabus/pen/BaKoEyQ), [CodePen Grid](https://codepen.io/ondrabus/pen/WNwrOOv)

## #5 Horizontal header with menu

![Image](https://www.freecodecamp.org/news/content/images/2020/08/menu.png)

To achieve this design using Flexbox, both sides of the header need to be represented by a single element.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/5-flexbox.png)

The logo and company name form one `anchor` on the left, and the menu is a single `nav` element on the right. Flexbox positions them with `justify-content: space-between`.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/5-grid.png)

With Grid, we need two columns - one for the logo and the other for the menu. The menu is another grid that distributes the size of columns evenly using `grid-template-columns: repeat(4, minmax(0, 1fr))`. 

The problem here is that if we want to add another item to the menu, we also need to adjust the CSS.

**Winner: Flexbox**

[CodePen Flexbox](https://codepen.io/ondrabus/pen/wvGMqXq), [CodePen Grid](https://codepen.io/ondrabus/pen/oNxbeKx)

## And the winner is...

The final score is 5:2 in favor of Flexbox, but this does not mean that it becomes the ultimate CSS winner. There are situations when you need to use one or the other, sometimes even both together, to achieve what you need.

If you need flexible and conditional positioning, use Flexbox. If you want to create listings or similar structures that require equally sized elements or have a table form, use Grid. 

As a front-end developer, you won't get away with not knowing both.

[Reference guide Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/), [Reference guide Grid](https://css-tricks.com/snippets/css/complete-guide-grid/)

P.S. If I missed a layout you use on a daily basis, let me know on [Twitter](https://twitter.com/ondrabus) and I'll prepare a sequel :-)

