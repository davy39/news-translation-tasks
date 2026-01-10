---
title: Smart Quotes – Single Quote and Double Quotation Mark for Copy + Paste
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-05-10T14:31:24.000Z'
originalURL: https://freecodecamp.org/news/smart-quotes-single-quote-and-double-quotation-mark-for-copy-paste
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/smartQuotes-1.png
tags:
- name: HTML
  slug: html
- name: technical writing
  slug: technical-writing
- name: writing
  slug: writing
seo_title: null
seo_desc: "Smart quotes are commonly used punctuation marks in HTML and in writing.\
  \ Knowing how to use them correctly can make a significant difference in the clarity\
  \ and professionalism of your writing. \nSo in this article, you will get access\
  \ to the commonly ..."
---

Smart quotes are commonly used punctuation marks in HTML and in writing. Knowing how to use them correctly can make a significant difference in the clarity and professionalism of your writing. 

So in this article, you will get access to the commonly used quotation marks out there that you can copy and paste them into your articles, papers, and HTML.

It doesn’t end there. You will get access to the Unicode characters, HTML entities, and CSS entities of all the smart quotes. Make sure you check the end of this article so you can learn how to use the HTML and CSS entities and Unicode characters of the smart quotes.

Before showing you a table containing all the smart quotes, let's see how to use them in HTML and CSS first.


## What We'll Cover
- [How to Use Smart Quotes (Quotation Marks) in HTML and CSS](#heading-how-to-use-smart-quotes-quotation-marks-in-html-and-css)
- [Table of Smart Quotes, their Unicode Characters, HTML, and CSS Codes](#heading-table-of-smart-quotes-their-unicode-characters-html-and-css-codes)
- [Conclusion](#heading-conclusion)

## How to Use Smart Quotes (Quotation Marks) in HTML and CSS
To use smart quotes in HTML and CSS, you need their Unicode characters. For instance, the Unicode for quotation marks is `U+0022`. So, to use it in HTML, strip out the `U+` part, prepend the other letters or numbers with `&#x`, and end them with semicolon (`;`) like this:

```bash
&#x0022;
```

That translates to this: &#x0022;

In CSS, you need to strip out the `U+` part again and replace them with a backslash (`\`). So this is how you'd use a quotation mark in CSS:

```bash
\0022
```

But there's a caveat to using Unicode characters in CSS. To make them visible on a web page, you need to create a pseudo-element and make the Unicode character the content:

```css
element::after {
  content: '\0022';
}
```

## Table of Smart Quotes, their Unicode Characters, HTML, and CSS Codes
The table below contains the quotation marks available for use in HTML and other writings:

| Quotation Mark Name | Symbol | Unicode | HTML Code | CSS Code | 
| ----------- | ----------- | ----------- | ----------- | ----------- |
| Quotation Mark   | `"` | `U+0022` | `&#x0022` | `\0022`  | 
| Single High Reversed Quotation Mark | `‛` | `U+201B` | `&#x201B` | `\201B` |
| Double High Reversed Quotation Mark | `‟` | `U+201F` | `&#x201F` | `\201F` |
| Full Width Quotation Mark | `＂` | `U+FF02` | `&#xFF02` | `\FF02` |
| Right Single Quotation Mark | `’` | `U+2019` | `&#x2019` | `\2019` |
| Left Single Quotation Mark | `‘` | `U+2018` | `&#x2018` | `\2018` |
| Single Low Quotation Mark | `‚` | `U+201A` | `&#x201A` | `\201A` |
| Double Prime Quotation Mark | `〞`   | `U+301E` | `&#x301E` | `\301E` |
|Reversed Double Prime Quotation Mark | `〝` | `U+301D` | `&#x301D` | \301D|
| Low Double Prime Quotation Mark | `〟` | `U+301F` | `&#x301F` | `\301F` |
| Right Double Quotation Mark | `”` | `U+201D` | `&#x201D` |`\201D`|
| Left Double Quotation Mark |`“` | `U+201C` | `&#x201C` | `\201C` |
|Double Low Quotation Mark | `„` | `U+201E` | `&#x201E` | `\201E` |
| Double Low Reversed Quotation Mark | `⹂` | `U+2E42` | `&#x2E42` | `\2E42` |
| Heavy Right Pointing Angle Quotation Mark Ornament | `❯` | `U+276F` | `&#x276F` | `\276F` |
| Heavy Left Pointing Angle Quotation Mark Ornament | `❮` | `U+276E` | `&#x27CE` | `\27CE` |
|Single Right Pointing Angle Quotation Mark  | `›` | `U+203A` | `&#x203A` | `\203A` |
| Single Left Pointing Angle Quotation Mark | `‹` | `U+2039` | `&#x2039` | `\2039` |
| Heavy Low Single Comma Quotation Mark Ornament | `❟` | `U+275F` | `&#x275F` | `\275F` |
| Heavy Single Comma Quotation Mark Ornament | `❜` | `U+275C` | `&#x275C` | `\275C` |
| Heavy Single Turned Comma Quotation Mark Ornament | `❛` | `U+275B` | `&#x275B` | `\275B` |
| Heavy Double Turned Comma Quotation Mark Ornament | `❝` | `U+275D` | `&#x275D` | `\275D` |
| Heavy Double Comma Quotation Mark Ornament | `❞` | `U+275E` | `&#x275E` | `\275E` | 
| Right Pointing Double Angle Quotation Mark | `»` | `U+00BB` | `&#x00BB` | `\00BB` |
|Left Pointing Double Angle Quotation Mark | `«` | `U+00AB` | `&#x00AB` | `\00AB` |
| Full Width Apostrophe | `＇` | `U+FF07` | `&#xFF07` | `\FF07` |

Note: if you have a Mac, you may not be able to see the "Double low revesed quotation mark" and the "Heavy low single comma quotation mark". Here's what they're supposed to look like:

![Image](https://www.freecodecamp.org/news/content/images/2023/05/Screenshot-2023-05-10-at-7.20.26-AM.png)

![Image](https://www.freecodecamp.org/news/content/images/2023/05/Screenshot-2023-05-10-at-7.20.35-AM.png)

## Conclusion

I hope this article helps you learn about the smart quotes out there, and how to use them in your HTML and CSS files, and other writings.

Try to share the article with your friends and family so they can have access to the smart quotes.

Thank you.

