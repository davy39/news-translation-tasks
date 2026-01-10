---
title: HTML Arrow – Symbol Unicode for Single and Double Arrows, Left and Right Arrows
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-06-17T15:35:12.000Z'
originalURL: https://freecodecamp.org/news/html-arrow-symbol-unicode-for-single-and-double-arrows-left-and-right-arrows
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/unicode-for-arrows.png
tags:
- name: HTML
  slug: html
- name: unicode
  slug: unicode
seo_title: null
seo_desc: 'By Dillion Megida

  What are Unicodes?

  Unicodes are universal characters that represent different things. These could be
  symbols, characters, scripts, and many more forms of character combinations.

  Unicodes are adopted by many platforms (mobile and web...'
---

By Dillion Megida

## What are Unicodes?

Unicodes are universal characters that represent different things. These could be symbols, characters, scripts, and many more forms of character combinations.

Unicodes are adopted by many platforms (mobile and web) to make characters available everywhere.

## Why are Unicodes useful?

Unicodes are useful because they provide a standard for character representations across different systems and languages. 

Unicode also represents special characters that are not available in [ASCII](https://en.wikipedia.org/wiki/ASCII) and helps us create consistent character displays on various platforms.

You can also apply styles (colors, sizes) like you would with other characters.

## How to use Unicodes in HTML

You can write most Unicode symbols in two ways: using the hexadecimal reference or using the entity name.

Hexadecimal references are usually hard to read, but entity names are generally descriptive for the Unicode symbol you want to write.

For hexadecimal numbers, you write them in between `&#` (an ampersand and a number sign) and `;` (a semi-colon) like this:

```html
&#[NUMBER];
```

For entity names, you write them in between `&` and `;` like this:

```html
&[ENTITY];
```

This syntax is necessary so that HTML understands that the characters you're writing are not just text but Unicode symbol representations.

## Unicode for Single and Double Left and Right Arrows

Now that we've briefly looked at what Unicode is and how to use it in HTML, let's look at some examples.

There are many symbols with Unicode representations you can use in HTML. For this article, I will share four examples of arrow symbols.

There are different arrow symbols and Unicode values for them. The arrows used here are just examples.

### Left Arrow

For the single left arrow:

The hexadecimal reference is **8592** and the entity name is **larr**. In HTML, it would be written like:

```html
&#8592;
<!-- or -->
&larr;
```

This code will print this on a page:

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-100.png)

For the double left arrow:

The hexadecimal reference is **8647** and the entity name is **llarr** written as:

```html
&#8647;
<!-- or -->
#llarr
```

This will result in:

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-99.png)

### Right arrow
For the single right arrow:

The hexadecimal reference is **8594** and the entity name is **rarr** written like:

```html
&#8594;
<!-- or -->
&rarr;
```

The result:

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-98.png)

For the double right arrow:

The hexadecimal reference is **8649** and the entity name is **rrarr** written as:

```html
&#8649;;
<!-- or -->
#rrarr
```

This will result in:

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-101.png)

You can use Unicode representations to print many other symbols in HTML. You can either use the hexadecimal reference or the entity name of the symbol, as I have shown you in this article.


