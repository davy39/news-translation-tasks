---
title: CSS Properties – Max-width, Min-width, Max-height, and Min-height Explained
  with Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-07-20T17:09:20.000Z'
originalURL: https://freecodecamp.org/news/css-properties-examples
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/pexels-scott-webb-1544944.jpg
tags:
- name: CSS
  slug: css
- name: css properties
  slug: css-properties
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Nelson Michael

  If you''re building a website, making it responsive is one of the most important
  things you''ll do.

  It can be difficult to create websites that look good across a variety of screen
  sizes. You''ll have to handle rendering an element''s w...'
---

By Nelson Michael

If you're building a website, making it responsive is one of the most important things you'll do.

It can be difficult to create websites that look good across a variety of screen sizes. You'll have to handle rendering an element's width or height, and specifying varied width sizes using media queries is not easy. 

While relative units such as "percentage percent" can be useful in some contexts, they can also be disastrous in others.

But don't worry – characteristics like max-width and min-width are here to help. These properties allow us to avoid using media queries to solve some responsive challenges.

By the end of this article, you'll know what max-width, min-width, and max-height are and how to use them.

## The Max-width Property

The max-width property lets you specify an element's maximum width. This means that an element can increase in width until it reaches a specific [absolute or relative unit](https://www.freecodecamp.org/news/css-unit-guide/), at which point it should fix its width to that unit.

Here's what I'm talking about:

Imagine setting the width of an element to **80%** of the viewport's width. If the viewport has a width of **375px**, our element will have a width of **300px**, which isn't too shabby.

(80/100) * 375 = 300px

But what if we had a wider viewport, say **1300px**, in which case our element will be **1040px** wide.

(80/100) * 1300 = 1040px

This is where the max-width property comes in handy. When you're using relative units like a percentage, setting a max-width property on an element causes it to keep increasing in width until it reaches a point we designate.

Here's an example:

%[https://codepen.io/D_kingnelson/pen/mdmeEOV]

Notice how our card's size never exceeded **350px**? That's how max-width works. It allows our card to grow on smaller screens. 

If the width is less than 350px, it takes 80% of whatever the current screen size is. But as soon as the width reaches 350px, it clamps down and doesn’t exceed that set width.

Here’s what the code looks like:

```
//The card can not get larger than 350px.

.card{
  margin:0 auto;
  padding:1.5em;
  width:80%;
  max-width:350px;
  height:50%;
  background: #FFFFFF;
  box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.3);
  border-radius:4px;
  overflow:hidden;
}
```

## The Min-Width Property 

In contrast to the max-width property, the min-width property specifies the minimum width. It indicates the minimal possible width for an element.

In some cases, you may want your element to have flexible width, so you give it a width in a relative unit such as a percentage. But as the screen shrinks, the element's width shrinks as well. 

This is where min-width comes in – you can set a minimum width so that the card knows not to shrink smaller than the specified width.

%[https://codepen.io/D_kingnelson/pen/zYwdzxW]

```
//Here the card element can not get smaller than 250px
.card{
  margin:0 auto;
  padding:1.5em;
  width:80%;
  max-width:350px;
  //here we set the min-width property
  min-width : 250px;
  height:50%;
  background: #FFFFFF;
  box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.3);
  border-radius:4px;
  overflow:hidden;
}
```

## The Max-Height Property

The max-height property operates similarly to the max-width property, but it affects the height instead of the width.

Here's an example :

%[https://codepen.io/D_kingnelson/pen/gOWxRrb]

```
// it fixes the height of an element to a specified unit, effectively stopping it from increasing in height

.card{
  margin:0 auto;
  padding:1.5em;
  width:80%;
  max-width:350px;
  height:70%;
  //here we set the max-height for the card.
  max-height: 400px;
  background: #FFFFFF;
  box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.3);
  border-radius:4px;
  overflow:hidden;
}
```

## The Min-Height Property

In contrast to max-height, the min-height property provides a minimum height for an element.

This occurs when the viewport shrinks and the element's height cannot be reduced beyond a defined height unit.

%[https://codepen.io/D_kingnelson/pen/yLboXVz]

```
.element{
    height:40vh;
    min-height:200px;
}
```

## Conclusion

Responsiveness is an important factor to consider in web development. Keeping track of how things appear across multiple screen sizes may be challenging, but the max-width, min-width and max-height, and min-height properties help tackle these challenges. 

These properties let you adjust the size of elements without needing to use media queries.

