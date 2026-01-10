---
title: What is rem in CSS? rem Unit Font Size, Padding, Height, and More
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-10-03T22:57:54.000Z'
originalURL: https://freecodecamp.org/news/what-is-rem-in-css-rem-unit-font-size-padding-height-and-more
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/rem-units.png
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Dillion Megida

  The rem measurement unit is a relative unit that you can use for length values in
  CSS. I will explain what this unit is, and how it is different from other units
  in this article.

  In my previous article, I explained the two categorie...'
---

By Dillion Megida

The `rem` measurement unit is a relative unit that you can use for length values in CSS. I will explain what this unit is, and how it is different from other units in this article.

In my previous article, I explained the two categories of units in CSS: [**Absolute** and **Relative** units](https://www.freecodecamp.org/news/absolute-and-relative-css-units/). I recommend checking it out so that you can understand what relative units are and why `rem` falls under this category.

To briefly explain, relative units are used for values that depend on (are relative to) other values.

## What is the rem unit?

`rem` stands for **root em**, which is a measurement unit that refers to the `font-size` of the `root` element of a document. 

It is a relative unit, which means all values that use it change when the root's `font-size` changes. The `root` element in this case refers to the `html` element.

**1rem** means **1 times the root font-size**.

So, if you declare the root's `font-size` to be 16px (which is the default font size) like this:

```css
html {
  font-size: 16px;
}
```

then anywhere you use `1rem` will interpret it as `16px`. `2rem` will interpret it as `32px`. `0.5rem` will interpret it as `8px`, and so on.

## Difference between rem and em

`rem` refers to the `font-size` of the `html` element while `em` refers to the `font-size` of the element it is used on (in some cases, the `font-size` of the parent element).

Let's see some examples for `em`:

```html
<div>
    <p>I am a text</p>
</div>
```

The CSS:

```css
div {
  font-size: 20px;
}

p {
  font-size: 1.5em;
  width: 2em;
}
```

For the `font-size` of the `p` tag, `em` refers to the `font-size` of its parent element, which in this case is the `div`. So `font-size: 1.5em` on the `p` tag will be interpreted as **1.5 times 20px** which is **30px**.

For the `width` of the `p` tag, `em` refers to the `font-size` of the `p` tag itself. So `width: 2em` on the `p` tag will be interpreted as **2 times 30px** which is **60px**.

And for the example showing `rem`:

```html
<div>
    <p>I am a text</p>
</div>
```

Here's the CSS:

```css
html {
  font-size: 18px;
}

div {
  font-size: 20px;
}

p {
  font-size: 1.5rem;
  width: 10rem;
  padding: 0.2rem;
  height: 4rem;
  border: 1rem solid red;
}
```

Here's the result:

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-36.png)

For the `font-size` of the `p` tag, `rem` refers to the `font-size` of the root (`html`) element. So `font-size: 1.5rem` on the `p` tag will be interpreted as **1.5 times 18px** which is **27px**.

For the `width` of the `p` tag, `rem` also refers to the `font-size` of the root element. So `width: 10rem` on the `p` tag will be interpreted as **10 times 18px** which is **180px**.

For the `padding` of the `p` tag, `rem` refers to the `font-size` of the root element. So `padding: 0.2rem` on the `p` tag will be interpreted as **0.2 times 18px** which is **3.6px**.

For the `height` of the `p` tag, `rem` refers to the `font-size` of the root element. So `height: 4rem` on the `p` tag will be interpreted as **4 times 18px** which is **72px**.

And lastly, for the `border-width` of the `p` tag, `rem` still refers to the `font-size` of the root element. So `border: 1rem...` on the `p` tag will be interpreted as **1 times 18px** which is **18px**.

You can use `rem` with other length values in CSS.

## Wrapping Up

Unlike fixed units, relative units make it easier to create responsive designs in most situations. When you change the value that the units depend on, all values with the relative unit scale accordingly.

`rem` is a relative unit that allows you to define a global `font-size`, and every other value with the `rem` unit depends on the global size. If the user of a browser changes their default root font size, the `rem` unit values will also scale accordingly. In the case of fixed values, the user's preference will be ignored.

While `em` refers to the `font-size` of the element itself (or its parent), `rem` refers to the root `font-size`.


