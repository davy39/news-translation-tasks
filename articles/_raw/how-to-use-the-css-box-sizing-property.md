---
title: How the CSS Box-sizing Property Controls the Size of Elements
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-27T16:44:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-the-css-box-sizing-property
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/Didicodes-j.png
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: Web Design
  slug: web-design
seo_title: null
seo_desc: 'By Edidiong Asikpo

  The CSS box-sizing property is used to adjust or control the size of any element
  that accepts a width or height. It specifies how to calculate the total width and
  height of that element.

  In this article, I will explain how the CSS ...'
---

By Edidiong Asikpo

The CSS box-sizing property is used to adjust or control the size of any element that accepts a `width` or `height`. It specifies how to calculate the total `width` and `height` of that element.

In this article, I will explain how the CSS `box-sizing` property can be used to control the size of elements.

## Prerequisites

* Basic CSS knowledge.
* Code editor.
* Web browser.

## Without the CSS box-sizing property

If you look at the code snippet below, you will notice that there are two `div` elements with the same `width` and `height` – but the first `div` appears to be bigger than the second `div`.

%[https://codepen.io/edyasikpo/pen/mdVoxrg]

That's pretty strange, right? Because why would anyone assign the same width and height to two `div` elements unless they ideally wanted those elements to be the same? 

Keep reading to find out why the two `div` elements are different??‍???‍?. 

By default, the [CSS box model](https://kolosek.hashnode.dev/a-beginners-guide-to-box-model-in-css-ck6rnzojg03fidfs1g2kxl8ci) calculates any element that accepts a width or height in this format:

* width + padding + border = rendered or displayed width of the element's box.
* height + padding + border = rendered or displayed height of the element's box.

This means that whenever you add `padding` or `border` to the element, the size of an element will appear bigger than the size originally assigned to it. This is because the content of that element includes the `width` and `height` properties but does not include the `padding` or `border` property.

Still don't get it yet? Look at the code snippet below to see the actual calculation.

```css
.first-box {
  width: 200px;
  height: 100px;
  border: 8px solid blue;
  padding: 20px;
  background: yellow;
  /* Total width: 200px + (2 * 20px) + (2 * 8px) = 256px
     Total height: 100px + (2 * 20px) + (2 * 8px) = 156px */
}

.second-box {
  width: 200px;
  height: 100px;
  border: 8px solid blue;
  background: yellow;
  /* Total width: 200px + (2 * 8px) = 216px
     Total height: 100px +  (2 * 8px) = 116px */
}

```

As seen in the code snippet, CSS adds the `padding` and `border` to the `width` and `height` already specified. It displays the total value as the size of the element, thereby ignoring the actual size you assigned to the `div`. 

## With the CSS box-sizing Property

With the `box-sizing` property, the default behaviour explained above can be changed.  

Using the same code, let's add the `box-sizing` property and set it to `border-box` and see if we can actually control the size. 

%[https://codepen.io/edyasikpo/pen/zYrbbwP]

You must have noticed that the two `div` elements now have the same size. 

## Syntax

```
box-sizing:content-box;
box-sizing:border-box;

```

## content-box

This is the default behaviour of the box-sizing property. `content-box` doesn't take into account the `width` and `height` specified for an element. 

That is, if you set an element's `width` to **200 pixels**, then set the border to **8 pixels** and the padding to **20 pixels**, the size of the `border` and `padding` will be added to the final rendered width. This makes the element wider than **200 pixels**.

```css
div{
  box-sizing:content-box;
  width: 200px;
  border: 8px solid blue;
  padding: 20px;
  background: yellow;
  /* Total width: 200px + (2 * 20px) + (2 * 8px) = 256px*/
}

```

As seen in the code snippet above, the size of this `div` element has automatically increased to 256px even when it was originally set to 200px.

## border-box

When you set the `box-sizing` property to `border-box`, it tells the browser to account for any `border` and `padding` assigned to the element's width and height. 

That is, if you set an element's `width` to **200 pixels**, that 200 pixels will include any border or padding you add, and the content box will shrink to absorb that extra width.

```css
div{
  box-sizing:border-box;
  width: 200px;
  border: 8px solid blue;
  padding: 20px;
  background: yellow;
  /* Total width: 200px - (2 * 20px) - (2 * 8px) = 144px*/
}

```

As seen in the code snippet above, the size of this `div` element has automatically reduced to 144px even when it was originally set to 200px.

Let's merge both code snippets and see exactly how the box will look with `content-box` and `border-box`.

%[https://codepen.io/edyasikpo/pen/xxZerWW]

## Conclusion

With the CSS box-sizing property, you have the ability to set how the size of elements in your code are calculated. 

According to the [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/box-sizing), it is often useful to set `box-sizing` to `border-box` when you're laying out elements. This makes dealing with the sizes of elements much easier, and generally eliminates a number of pitfalls you can stumble on while laying out your content.  

On the other hand, when you're using `position: relative` or `position: absolute`, using `box-sizing: content-box` allows the positioning values to be relative to the content, and independent of changes to border and padding sizes. Sometimes you might want this.

That's all folks! I hope this was helpful. If so, please share this article and follow me on [Twitter](https://twitter.com/Didicodes).

