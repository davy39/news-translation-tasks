---
title: How to Create a New Stacking Context with the Isolation Property in CSS
subtitle: ''
author: Natalie Pina
co_authors: []
series: null
date: '2022-03-11T20:03:45.000Z'
originalURL: https://freecodecamp.org/news/the-css-isolation-property
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/stacked.jpg
tags:
- name: CSS
  slug: css
seo_title: null
seo_desc: "What is the CSS Isolation Property?\nIn CSS, you can use the isolation\
  \ property to create a new stacking context. Here's what that looks like:\n.container-for-new-stacking-context\
  \ {\n  isolation: isolate;\n}\n\nThe default value for isolation is auto, whic..."
---

## What is the CSS Isolation Property?

In CSS, you can use the `isolation` property to create a new stacking context. Here's what that looks like:

```css
.container-for-new-stacking-context {
  isolation: isolate;
}
```

The default value for `isolation` is `auto`, which is a bit more nuanced as a stacking context _can_ be created – but it depends on the properties of the element and if they require it. 

You can also set the value to `inherit`,  `initial`, `revert`, or `unset`. 

Using `isolation: isolate;` is a definitive way to create a new stacking context. 

## What is the Stacking Context?

![Image](https://www.freecodecamp.org/news/content/images/2022/01/doll-g9145bb1e2_1280.jpg)

In CSS, the stacking context quite literally allows for HTML elements to be stacked with their starting position based upon a base element that provides context.

Elements are placed along an imaginary matrix with a x-axis and y-axis. There is also a z-axis, in which element can be placed in front of or behind each other. The `z-index` property is commonly used to place elements along the z-axis. 

Keep in mind that when the root HTML element is rendered, it comes along with a root/global stacking context.

There are many ways to create stacking contexts within the global stacking context. One common way is to use `position: relative` with `z-index`. 

Using `position: sticky` or `fixed` works, but will take elements outside of the flow layout and require additional properties for desired placement. 

You can also use `transform`, `clip-path`, or `filter` to facilitate stacking. To see all the ways the stacking context can be formed, read more on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Positioning/Understanding_z_index/The_stacking_context).

Stacking contexts can contain subsequent inner stacking contexts, and continue on to nest further. That may be a bit too _Inception_-like to conceptualize, so let's get down to why this is useful.

## The Z-Index Black Hole

![Image](https://www.freecodecamp.org/news/content/images/2022/01/wormhole-g9c2a60580_1280.png)

Using `z-index` can be hard to maintain. You have to be really cautious about where you are using it and what values you are supplying to it. 

Design systems can help to solve issues related to this. Creating a set of reusable values and documenting in what cases they should be used can be really helpful. For example, setting aside your highest variable values for modals and other items that will always take over the entire page. 

But most of the time we're really just trying to have our style appear the way we want it to. Which can mean prescribing arbitrary `z-index` values and continuing to bump up those values until they work. 

I've encountered the infamous `z-index: 999999;` many times. Tracking down these random values and creating new order can become arduous. This can lead to issues that are hard to debug. 

The higher numbers you begin to use, the deeper and deeper you can go into the black hole and the harder it is to get back out of it later on.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/zindex.svg)

### Keep It Simple with Isolation Instead

Setting the isolation property to isolate is a simple one-liner that can create a new stacking context without reaching for `z-index` to place elements in front of each other.

You can use isolation on statically-position elements and it will not affect children elements. It's a great way to create an isolated base for containing children elements within. The isolation property is also widely [supported](https://caniuse.com/?search=isolation). 

![Image](https://www.freecodecamp.org/news/content/images/2022/01/isolation-3.svg)

Just as a reminder, here's the syntax for that:

```css
.container-for-new-stacking-context {
  isolation: isolate;
}
```

## To Sum Up:

Setting  `isolation: isolate;` will create a new stacking context for children elements when applied to a top-level element. 

If you found this article helpful, feel free to reach out on Twitter [@ui_natalie](https://twitter.com/ui_natalie). Happy stacking! 

### Resources

* [MDN Web Docs - Isolation](https://developer.mozilla.org/en-US/docs/Web/CSS/isolation)
* [MDN Web Docs - The Stacking Context](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Positioning/Understanding_z_index/The_stacking_context)
* [What The Heck, z-index??](https://www.joshwcomeau.com/css/stacking-contexts/)


