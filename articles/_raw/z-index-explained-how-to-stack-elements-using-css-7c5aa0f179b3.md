---
title: 'Z-Index Explained: How to Stack Elements Using CSS'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-18T23:18:51.000Z'
originalURL: https://freecodecamp.org/news/z-index-explained-how-to-stack-elements-using-css-7c5aa0f179b3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*TGyQ2F-PxAhKWA6p6b6rYA.jpeg
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Veronika Ivhed

  I have always struggled with the CSS property z-index. It sounds so easy at first.
  Elements with a higher z-index value are displayed in front of those with a lower
  z-index value. Still, a lot of times I have ended up in situations ...'
---

By Veronika Ivhed

I have always struggled with the CSS property [z-index](https://developer.mozilla.org/en-US/docs/Web/CSS/z-index). It sounds so easy at first. Elements with a higher z-index value are displayed in front of those with a lower z-index value. Still, a lot of times I have ended up in situations where it seems like the z-index value didn’t have any effect at all.

I decided that I’d had enough of trial and error with z-index and that I wanted to get a better understanding. I hope this article can help you so you will never wonder why z-index is not doing what you expect it to do.

### Default stacking order

Let’s first mention the default order the browser stacks elements in, when no z-index is applied:

1. Root element (the <html> element)
2. Non-positioned elements in the order they are defined
3. Positioned elements in the order they are defined

A [non-positioned](https://developer.mozilla.org/en-US/docs/Web/CSS/position) element is an element with the default position value static. A [positioned](https://developer.mozilla.org/en-US/docs/Web/CSS/position) element is an element with any other position value. Examples of other values are: absolute, relative, sticky or fixed.

HTML:

```html
<div class=”pink”>
  <div class=”orange”></div>
</div>
<div class=”blue”></div>
<div class=”green”></div>
```

CSS:

```css
/* This is only the CSS that is relevant for the example. For the complete CSS check the links below the pictures. */

.blue, .pink, .orange {
  position: absolute;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/0ok6C2rWIvGF9pibC1xMz9q0iOmkqNWOx1cT)
_[https://codepen.io/ivhed/pen/QrdEBB](https://codepen.io/ivhed/pen/QrdEBB" rel="noopener" target="_blank" title=")_

We defined the green box last in the document. Still, it appears behind the others because it is non-positioned.

### Stacking with z-index

If we now want to change the stacking order of these elements, we can use the property z-index. An element with a higher z-index will be displayed in front of an element with a lower z-index. One thing to note is that z-index **only works with positioned elements**_._

```css
.blue, .pink, .orange {
  position: absolute;
}

.blue {
  z-index: 2;
}

.orange {
  z-index: 3;
}

.green {
  z-index: 100; // has no effect since the green box is non-         positioned
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/NOdy4A6ZcslzfIFMD-PW5-vqD83i2Qb5vOrQ)
_[https://codepen.io/ivhed/pen/xjqmpV](https://codepen.io/ivhed/pen/xjqmpV" rel="noopener" target="_blank" title=")_

The orange box with a higher z-index is displayed in front of the blue box.

#### Stacking Context

Let’s say that we add another positioned box to the layout which we want to position behind the pink box. We update our code to the following:

HTML:

```html
<div class=”pink”>
  <div class=”orange”></div>
</div>
<div class=”blue”></div>
<div class=”purple”></div>
<div class=”green”></div>
```

CSS:

```css
.blue, .pink, .orange, .purple {
  position: absolute;
}

.purple {
  z-index: 0;
}

.pink {
  z-index: 1;
}

.blue {
  z-index: 2;
}

.orange {
  z-index: 3;
}

.green {
  z-index: 100;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/Uuw9yAx1sVpyVHZ8sCRtVF8H5eBnyCElCH4S)
_[https://codepen.io/ivhed/pen/YLZdjx](https://codepen.io/ivhed/pen/YLZdjx" rel="noopener" target="_blank" title=")_

Our pink box is displayed in front of the purple box as expected, but what happened to the orange box? Why is it all of a sudden behind the blue one even though it has a higher z-index? This is because adding a z-index value to an element forms what is called a [stacking context](https://www.w3.org/TR/CSS21/zindex.html)**.**

The pink box has a z-index value other than auto, which forms a new stacking context. The fact that it forms a stacking context affects how its child elements are being displayed.

It is possible to change the stacking order of the pink box child elements. However, their **z-index only has a meaning within that stacking context**. This means that, we won’t be able to move the orange box in front of the blue box, because they are not within the same stacking context anymore.

If we want the blue box and the orange box to be part of the same stacking context, we can define the blue box as a child element of the pink box. This will make the blue box appear behind the orange one.

```html
<div class=”pink”>
  <div class=”orange”></div>
  <div class=”blue”></div>
</div>
<div class=”purple”></div>
<div class=”green”></div>
```

![Image](https://cdn-media-1.freecodecamp.org/images/T-Z7bkfgeKlqiz8WYbAlU0W9RMM4CtJgxw50)
_[https://codepen.io/ivhed/pen/erGoJE](https://codepen.io/ivhed/pen/erGoJE" rel="noopener" target="_blank" title=")_

Stacking contexts are not only formed when applying z-index to an element. There are [several other properties](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Positioning/Understanding_z_index/The_stacking_context) that cause elements to form stacking contexts. Some examples are: filter, opacity, and transform.

Let’s go back to our previous example. The blue box is again a sibling to the pink box. This time, instead of adding z-index to the pink box, we apply a [filter](https://developer.mozilla.org/en-US/docs/Web/CSS/filter) to it.

HTML:

```html
<div class=”pink”>
  <div class=”orange”></div>
</div>
<div class=”blue”></div>
<div class=”green”></div>
```

CSS:

```css
.blue, .pink, .orange {
  position: absolute;
}

.pink {
  filter: hue-rotate(20deg);
}

.blue {
  z-index: 2;
}

.orange {
  z-index: 3;
}

.green {
  z-index: 100;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/JI1HNPrHCEUbKSZZiKSJLnBlWLyJKPclyEez)
_[https://codepen.io/ivhed/pen/LmWMQb](https://codepen.io/ivhed/pen/LmWMQb" rel="noopener" target="_blank" title=")_

The orange box still has a higher z-index than the blue one, but is still displayed behind it. This is because the filter value caused the pink box to form a new stacking context.

#### Summary

By using z-index on positioned elements, we can change the default stacking order.

When applying certain CSS properties, an element can form a stacking context. Z-index values only have a meaning within the same stacking context.

For more information on z-index, I recommend [this article.](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Positioning/Understanding_z_index) I got a lot of inspiration from it when writing this.

Thanks for reading! :)

