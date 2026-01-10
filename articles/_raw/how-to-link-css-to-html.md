---
title: How to Link CSS to HTML – Stylesheet File Linking
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-06-14T16:22:59.000Z'
originalURL: https://freecodecamp.org/news/how-to-link-css-to-html
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/linkHTMLCSS.png
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'HTML is the markup language that helps you define the structure of a web
  page. CSS is the stylesheet language you use to make the structure presentable and
  nicely laid out.

  To make the stylings you implement with CSS reflect in the HTML, you have to ...'
---

HTML is the markup language that helps you define the structure of a web page. CSS is the stylesheet language you use to make the structure presentable and nicely laid out.

To make the stylings you implement with CSS reflect in the HTML, you have to find a way to link the CSS to the HTML.

You can do the linking by writing inline CSS, internal CSS, or external CSS.

It is a best practice to keep your CSS separate from your HTML, so this article focuses on how you can link that external CSS to your HTML.

## How to Link CSS to HTML

To link your CSS to your HTML, you have to use the link tag with some relevant attributes. 

The link tag is a self-closing tag you should put at the head section of your HTML.

To link CSS to HTML with it, this is how you do it:
```css
<link rel="stylesheet" type="text/css" href="styles.css" />
```

Place the link tag at the head section of your HTML as shown below:

```html
<head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" type="text/css" href="styles.css" /> 
    <title>Link CSS to HTML</title>
</head>
```

## Attributes of the Link Tag

### The `rel` Attribute

`rel` is the relationship between the external file and the current file. For CSS, you use `stylesheet`. For example, `rel="stylesheet"`.

### The `type` Attribute

`type` is the type of the document you are linking to the HTML. For CSS, it is `text/css`. For example `type="text/css"`.

### The `href` Attribute

`href` stands for “hypertext reference”. You use it to specify the location of the CSS file and the file name. It is a clickable link, so you can also hold `CTRL` and click it to view the CSS file.

For example, `href="styles.css"` if the CSS file is located in the same folder as the HTML file. Or `href="folder/styles.css"` if the CSS file is located on another folder.


## Final Thoughts

This article showed you how to properly link an external CSS file to HTML with the `link` tag and the necessary attributes.

We also took a look at what each of the attributes means, so you don’t just use them without knowing how they work.

Keep coding…


