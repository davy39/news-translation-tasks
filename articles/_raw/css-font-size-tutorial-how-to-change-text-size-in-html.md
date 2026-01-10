---
title: CSS Font Size Tutorial – How to Change Text Size in HTML
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-28T13:50:54.000Z'
originalURL: https://freecodecamp.org/news/css-font-size-tutorial-how-to-change-text-size-in-html
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/font.jpg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: HTML
  slug: html
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "By Amy Haddad\nUse the CSS font-size property to determine the size of\
  \ your text.\n.container {\n    font-size: 33px;\n}\n\nThis property takes several\
  \ types of values:\n\nKeywords (absolute-size and relative-size keywords),\nLength\
  \ (such as pixels (px) and e..."
---

By Amy Haddad

Use the CSS **`font-size`** property to determine the size of your text.

```css
.container {
    font-size: 33px;
}
```

This property takes several types of values:

* Keywords (absolute-size and relative-size keywords),
* Length (such as pixels (px) and em units), and
* Percentages.

```css
.container {
    font-size: xx-large;
}
```

The question is: which type of value should you choose and why? 

That’s the question this article tackles. It’ll show you how to use the `font-size` property and the differences between its many values. So the next time you need to change the font size of your text, you’ll know which value to reach for.

## Keyword Values

There are two types of keyword values you can use with font size: `absolute-size` and `relative-size` keywords. Let’s start with absolute.

### Absolute-Size Keywords

The code below uses the absolute-size keyword **`small`** to size the HTML text.

```css
.childElement {
    font-size: small;
}
```

There are more absolute-size keyword options to choose from:

* xx-small
* x-small
* small
* medium
* large
* x-large
* xx-large
* xxx-large

The value of an absolute-size keyword is determined by the browser’s [default font size](https://developer.mozilla.org/en-US/docs/Web/CSS/font-size). Typically, that size is medium.

## Relative-Size Keywords

Relative-size keywords are another keyword option to consider. You have two to choose from: **`smaller`** and **`larger`**.

```css 
.parentElement {
    font-size: smaller;
}
```

The font size of an element with a relative-size keyword is _relative_—larger or smaller—to its parent’s font size. 

Put another way, the font size of the parent element affects the font size of the child element, as you can see below.

%[https://codepen.io/amymhaddad/pen/eYZLNGN]

In this example, the relative-size keyword **`smaller`** is applied to the child element, and the absolute-size value **`large`** is applied to the parent element.

# Length Values

`font-size` accepts several different length values. We’ll explore three of them: pixels (px) and em and rem units. Despite your selection, the length value you use must be positive.

```css
.parentElement {
    font-size: 60px;
}
```

### Pixels

Pixels are an [absolute length unit](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Values_and_units). That means, they're _not_ affected by other elements, like the parent element, or the window size.

As a result, pixels are precise: you define the exact number of pixels you need on an element and that’s typically what you get. However, there may be slight differences between browsers.

%[https://codepen.io/amymhaddad/pen/KKzRbMb]

Notice that the child elements use `pixels` and have the same font size in the code sample above. 

## EMs

While you can think of pixels as fixed, think of em values as variable. 

That’s because em values are a [relative length unit](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Values_and_units). The font size of an element that uses an em value is _relative_ to the font size of its parent.   

However, say you haven’t set a font size for the parent element. Nor have you set one elsewhere higher up in the DOM. In this case, the em value is calculated using [the browser’s default](https://developer.mozilla.org/en-US/docs/Web/CSS/font-size) (often 16px).

Let’s make this idea concrete. 

Say the parent element is set to 30px and the child element is set to 2em. Then, the child element’s rendered font size is 60px (2 x 30px = 60px). You can see this scenario in the code below.

%[https://codepen.io/amymhaddad/pen/zYqJrOJ]

em values can be problematic due to their compounding effect, which is demonstrated in the following example.

%[https://codepen.io/amymhaddad/pen/LYNBjOp]

When you have multiple elements that use em values nested within each other, the font size values compound: they get larger and larger. This is the compounding effect in action.

## REMs

Enter rem values, which were created to deal with the compounding problem of ems. 

Recall that em values are relative to the parent element. In contrast, rem values are relative to the font size of the root (html) element.  

This means you can apply a rem value to an element, and it won’t be affected by the parent’s font size. This evades the compounding effect we experienced above.

This example uses the `font-size` property with a rem value.

%[https://codepen.io/amymhaddad/pen/JjXByvd]

Here's a key point from the above example: the font size of the parent element does _not_ affect the font size of the child elements.

# Percentages

Percentages offer yet one more way to set the font size _relative_ to the parent element’s font size. 

The element with the percentage refers to its parent element to determine its font size. The percentage value must be positive. 

Here’s an example.

%[https://codepen.io/amymhaddad/pen/mdPjMjw]

As you can see, when it comes to font size you’ve got plenty of options to fit your needs.

_I write about learning to program, and the best ways to go about it on [amymhaddad.com](http://amymhaddad.com/)._ I also _tweet about programming, learning, and productivity: [@amymhaddad](https://twitter.com/amymhaddad)._

