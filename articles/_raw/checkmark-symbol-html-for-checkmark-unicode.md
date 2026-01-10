---
title: Checkmark Symbol – HTML for Checkmark Unicode
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-04-12T19:17:04.000Z'
originalURL: https://freecodecamp.org/news/checkmark-symbol-html-for-checkmark-unicode
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/checkmark.png
tags:
- name: HTML
  slug: html
- name: unicode
  slug: unicode
seo_title: null
seo_desc: "If you take a look at your keyboard, you'll see that there’s no key for\
  \ typing a checkmark. \nYou could decide to copy the checkmark symbol from the internet\
  \ and paste it directly into your HTML code, but an easier way to do it is to use\
  \ the appropria..."
---

If you take a look at your keyboard, you'll see that there’s no key for typing a checkmark. 

You could decide to copy the checkmark symbol from the internet and paste it directly into your HTML code, but an easier way to do it is to use the appropriate Unicode character or HTML character entity.

If you are wondering what Unicode and HTML character entities are, they are both a piece of text that represents different emojis, symbols, and characters.

In your web projects, you might want to show a checkmark for the purpose of consent or agreement. So, in this article, I will show you how to use the appropriate Unicode and HTML character entity to bring checkmarks into your web projects. I will also show you 4 other variations of the checkmark symbol.

## The Unicode and HTML Characters for Checkmarks
The Unicode character for showing a checkmark is `U+2713`. If you decide to use this Unicode to show a checkmark in HTML and you type it in like that, what you type is shown like this:

```html
 <h1>Languages of the web</h1>
 <h3>U+2713 HTML</h3>
 <h3>U+2713 CSS</h3>
 <h3>U+2713 JavaScript</h3>
 <h3>U+2713 PHP</h3>
```

**So, how do you use the U+2713 Unicode to show the checkmark symbol?**

Remove the `U+` and replace it with an ampersand (`&`), pound sign (#), and `x`. Then type the 2713 in, and then a semi-colon. So, it becomes `&#x2713;`.

```html
 <h1>Languages of the web</h1>
 <h3>&#x2713; HTML</h3>
 <h3>&#x2713; CSS</h3>
 <h3>&#x2713; JavaScript</h3>
 <h3>&#x2713; PHP</h3>
```
![ss2-3](https://www.freecodecamp.org/news/content/images/2022/04/ss2-3.png)

You can also use the HTML character entity for a checkmark to show the checkmark symbol. This is `&#10003;` or `&check;`:

```html
<h1>Languages of the web</h1>
<h3>&check; HTML</h3>
<h3>&#10003; CSS</h3>
<h3>&#10003; JavaScript</h3>
<h3>&check; PHP</h3>
```
![ss2-3](https://www.freecodecamp.org/news/content/images/2022/04/ss2-3.png)

## Other Variations of the Checkmark Symbol
Apart from the traditional `U+2713`, `&#10003;` or `&check;`, there are other variations such as:

### `&#1004;` for a bolder checkmark
```html
<h1>Languages of the web</h1>
<h3>&#10004; HTML</h3>
<h3>&#10004; CSS</h3>
<h3>&#10004; JavaScript</h3>
<h3>&#10004; PHP</h3>
```
![ss3-2](https://www.freecodecamp.org/news/content/images/2022/04/ss3-2.png)

### U+2705 – `&#x2705;` for a white heavy checkmark
```html
<h1>Languages of the web</h1>
<h3>&#x2705; HTML</h3>
<h3>&#x2705; CSS</h3>
<h3>&#x2705; JavaScript</h3>
<h3>&#x2705; PHP</h3>
```
![ss4-1](https://www.freecodecamp.org/news/content/images/2022/04/ss4-1.png)

### U+2611 – `&#x2611;` for a ballot checkmark
```html
<h1>Languages of the web</h1>
<h3>&#x2611; HTML</h3>
<h3>&#x2611; CSS</h3>
<h3>&#x2611; JavaScript</h3>
<h3>&#x2611; PHP</h3>
```
![ss5-1](https://www.freecodecamp.org/news/content/images/2022/04/ss5-1.png)

### U+221A – `&#x221A;` for a square root checkmark 
```html
<h1>Languages of the web</h1>
<h3>&#x221A; HTML</h3>
<h3>&#x221A; CSS</h3>
<h3>&#x221A; JavaScript</h3>
<h3>&#x221A; PHP</h3>
```
![ss6-1](https://www.freecodecamp.org/news/content/images/2022/04/ss6-1.png)

## Conclusion
This article has shown you the Unicode string for a checkmark, how to use it, and other variations of it. 

You also learned about the equivalent HTML character entity for the checkmark symbol, in case you don’t want to show it with the Unicode string.

Now, go insert some checkmarks into your code.


