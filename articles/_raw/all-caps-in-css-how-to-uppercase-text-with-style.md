---
title: All Caps in CSS - How to Uppercase Text with Style
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-05-24T21:02:28.000Z'
originalURL: https://freecodecamp.org/news/all-caps-in-css-how-to-uppercase-text-with-style
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/how-to-uppercase-text-in-CSS.png
tags:
- name: CSS
  slug: css
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "By Dillion Megida\nWhen you're designing a website or working on a project,\
  \ you might want to use uppercase text for various reasons. Maybe you want to use\
  \ an abbreviation or acronym, emphasize certain text, or use it for headings. \n\
  There are multiple..."
---

By Dillion Megida

When you're designing a website or working on a project, you might want to use uppercase text for various reasons. Maybe you want to use an abbreviation or acronym, emphasize certain text, or use it for headings. 

There are multiple ways to uppercase text in HTML. The first way is to hardcode the uppercase text in HTML:

```html
<p>UPPERCASE TEXT</p>
```

The second way is to use the [`toUpperCase()` JavaScript String method](https://dillionmegida.com/p/10-useful-string-methods-in-javascirpt/#touppercase-and-tolowercase) and render it on the DOM:

```js
const upper = string.toUpperCase()

// then render
```

The third way, which we will look at in this article, is using the `text-transform` CSS property.

## How to Use text-transform in CSS

You can use the `text-transform` CSS property to capitalize text in different forms. This property can modify text to be in **uppercase**, **lowercase**, or **capitalized** (so that each word begins with a capital letter and the remaining characters in the word retain their original form).

To transform text to uppercase in CSS, use the following style declaration:


```css
element-selector {
  text-transform: uppercase;
}
```

This styles the text in the selected element to uppercase.

This declaration does not change the content of the DOM. For example, take a look at this HTML code:


```html
<p class='paragraph'>
  Some text
</p>
```

And this style:

```css
.paragraph {
  text-transform: uppercase;
}
```

On the UI, the text is styled like this:

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-137.png)

But in the DOM, the text remains the same like this:

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-139.png)

When you copy the text on the browser, the original text  "Some text" is copied in some browsers, but in others, the styled version is copied.

## Should you Use text-transform in CSS or the Other Methods?

If you're using uppercase for styling purposes, I recommend using CSS. The reason is there can be inconsistencies in how different browsers and browser tools handle uppercased text.

One inconsistency is the copy-pasting differences I mentioned earlier.

Another inconsistency is that some screen readers interpret the uppercase text as abbreviations. So a text like "SOME TEXT" will be read as "S.O.M.E T.E.X.T", which can affect how a reader understands a message.

Although, it is worth noting that some screen readers also interpret text uppercased with CSS as abbreviations.

However, it is recommended to keep styles as styles. If you want to have uppercase text just for style purposes, use CSS, and have the original text in HTML. But if you're using uppercase for abbreviations or a specific reason to have uppercased text, you can hardcode that in HTML.

You can refer to [this tweet on uppercasing without CSS](https://twitter.com/Mandy_Kerr/status/1285866670284668930) to see discussions around it.



