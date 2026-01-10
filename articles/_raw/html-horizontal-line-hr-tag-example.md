---
title: HTML Horizontal Line – HR Tag Example
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-01-26T18:36:53.000Z'
originalURL: https://freecodecamp.org/news/html-horizontal-line-hr-tag-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/hr.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "You can use the HTML <hr> tag to separate out different topics on a page.\n\
  We often use this tag when we want to create a thematic break or separate items\
  \ on an HTML page. \nIn this article, you'll learn how to use this tag in your HTML\
  \ code.\nTable of ..."
---

You can use the HTML `<hr>` tag to separate out different topics on a page.

We often use this tag when we want to create a thematic break or separate items on an HTML page. 

In this article, you'll learn how to use this tag in your HTML code.

## Table of Contents
- [Basic Syntax](#heading-basic-syntax)
- [Attributes of `<hr />` Tag](#heading-attributes-of-tag)
- [The Width Attribute](#heading-the-width-attribute)
- [The Color Attribute](#heading-the-color-attribute)
- [The Size Attribute](#heading-the-size-attribute)
- [The Align Attribute](#heading-the-align-attribute)
- [Conclusion](#heading-conclusion)

## Basic Syntax

The `<hr>` tag is an empty element. This means that it only has an opening tag, `<hr>`.

Starting in HTML5, we now need to attach a slash to the tag of an empty element. So, instead of having just `<hr>`, you should make it `<hr />`.

In browsers, the `<hr />` tag is displayed as a horizontal rule or line, like this: 
![ss-1-2](https://www.freecodecamp.org/news/content/images/2022/01/ss-1-2.png)


## Attributes of `<hr />` Tag

The `<hr />` tag accepts attributes such as `width`, `color`, `size`, and `align`. 

Before showing you how the individual attributes look and work, I will be setting everything in the body to center with this CSS code:

```css
body {
      display: flex;
      align-items: center;
      justify-content: center;
      height: 100vh;
    }
```

### The Width Attribute

The `width` attribute is used for specifying a width for the `<hr />` tag. It takes pixels or percentage as a value.

```html
<hr width="50%" />
```
![ss-2-2](https://www.freecodecamp.org/news/content/images/2022/01/ss-2-2.png)

### The Color Attribute

The `color` attribute is used to specify a color for the `<hr />` tag.

```html
    <hr width="50%" color="green" />
```

Here is how it would look if we set a green color for the `<hr />` tag:
![ss-3-3](https://www.freecodecamp.org/news/content/images/2022/01/ss-3-3.png)

### The Size Attribute

You can define a height for the `<hr />` tag with the `size` attribute. The value must be set in pixels.

```html
<hr width="50%" color="green" size="50px" />
```

A height of `50px` looks like the screenshot below:
![ss-4-3](https://www.freecodecamp.org/news/content/images/2022/01/ss-4-3.png)

### The Align Attribute

The `align` attribute is used to set an alignment for the `<hr />` tag. It takes `left`, `center` and `right` values. 

The default is left – meaning if an alignment is not set, the `<hr />` tag automatically aligns to the left.

```html
    <hr width="50%" color="green" size="50px" align="right" />
```

Setting an alignment of `right` for the `<hr />` tag looks like this:
![ss-5-4](https://www.freecodecamp.org/news/content/images/2022/01/ss-5-4.png)

## Conclusion

This article shows you what the `<hr />` tag looks like, what it is used for, and the attributes it accepts.

Since the `<hr />` tag appears as a horizontal rule in browsers, you might be thinking of using it to draw a line. 

But you shouldn’t do this because the horizontal rule appears as is only presentationally, not semantically. Instead, you should draw a line with a `div` or `span` as the case may be.

If you find this article helpful, share it with your friends and family.


