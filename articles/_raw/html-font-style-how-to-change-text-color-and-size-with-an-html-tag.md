---
title: HTML Font Style – How to Change Text Color and Size with an HTML Tag
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-08-19T23:23:07.000Z'
originalURL: https://freecodecamp.org/news/html-font-style-how-to-change-text-color-and-size-with-an-html-tag
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/fontstyle.png
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
seo_desc: 'When you code in HTML and add some text, you don’t want to leave it like
  that. You want to make that text look good.

  And to do that, you need to change their appearance through the color and font-size
  properties of CSS.

  In this tutorial, I will show ...'
---

When you code in HTML and add some text, you don’t want to leave it like that. You want to make that text look good.

And to do that, you need to change their appearance through the `color` and `font-size` properties of CSS.

In this tutorial, I will show you two different ways you can make your HTML texts look good.

## Basic `font-size` Syntax

```html
selector {
     font-size: value;
     color: value;
}
```

## How to Change Text Size and Text Color in the HTML Tag

You can change the color and size of your text right inside its tag with the color and font-size properties. This is known as inline CSS. You do it with the style attribute in HTML.

In the HTML code below, we will change the color and size of the freeCodeCamp text.

```html
<h1>freeCodeCamp</h1>
```

```css
body {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100vh;
}
```

It looks like this in the browser:
![unstyled-font](https://www.freecodecamp.org/news/content/images/2021/08/unstyled-font.png)

To change the size of the text, you'll use the style attribute, and then set a value with the `font-size` property like this:

```html
<h1 style="font-size: 4rem">freeCodeCamp</h1>
```

The text now looks like this in the browser: 
![text-size](https://www.freecodecamp.org/news/content/images/2021/08/text-size.png)

If you are wondering what 4rem is, it's a unit of measurement. It's the same as 64 pixels, because 16px makes 1rem unless you change the root `font-size` (`html`) to another value.

To change the color of the text, you can use the style attribute, and then set a value with the color property:

```html
<h1 style="color: #2ecc71">freeCodeCamp</h1>
```

This is what we now have in the browser:
![text-color](https://www.freecodecamp.org/news/content/images/2021/08/text-color.png)

Combining the `font-size` and `color` properties gives us this in the browser:

![inline-text-size-and-color](https://www.freecodecamp.org/news/content/images/2021/08/inline-text-size-and-color.png)

With the code: 

```html
<h1 style="font-size: 4rem; color: #2ecc71">freeCodeCamp</h1>
```

## How to Change Text Size and Text Color in an External CSS File

You can also change the color and size of text in an external stylesheet. Most importantly, you have to link the external CSS in the head section of your HTML.

The basic syntax for doing it looks like this:

```html
<link rel="stylesheet" href="path-to-css-file">
```

Now, to change the text size and color of the freeCodeCamp text, you need to select it in the stylesheet and apply the appropriate properties and values to it.

Remember this is our simple HTML code:

```html
<h1>freeCodeCamp</h1>
```

You can change the color and size of the text by selecting the element (h1) and assigning values to the color and font-size properties:

```css
 h1 {
    color: #2ecc71;
    font-size: 4rem;
}
```

We have the same result in the browser:
![external-text-size-and-color](https://www.freecodecamp.org/news/content/images/2021/08/external-text-size-and-color.png)

## Conclusion

I hope this tutorial gives you the knowledge to be able to change the size and color of your HTML text so you can make them look better.

Thank you for reading, and keep coding.


