---
title: Text Align in CSS – How to Align Text in Center with HTML
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2022-04-26T19:08:29.000Z'
originalURL: https://freecodecamp.org/news/text-align-in-css-how-to-align-text-in-center-with-html
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/nick-karvounis-TkZYCXmrKK4-unsplash.jpg
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
seo_title: null
seo_desc: 'There will be many times where you will need to center some text using
  HTML and CSS. But what is the best way to go about that?

  In this article, I will show you how to use the text-align property in CSS and show
  you how to vertically align text using...'
---

There will be many times where you will need to center some text using HTML and CSS. But what is the best way to go about that?

In this article, I will show you how to use the `text-align` property in CSS and show you how to vertically align text using CSS Flexbox. I will also talk about the `<center>` tag and why you shouldn't use it to center text.

## How to Use the `text-align` Property in CSS 

When you are working with heading or paragraph tags, the default styling in HTML will position the text on the left hand side of the page.

In this example, we have an `<h1>` which is placed on the upper left hand side of the page.

```html
<h1 class="title">Let's learn about centering text</h1>
```

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screen-Shot-2022-04-24-at-11.41.12-AM.png)

If we wanted to horizontally center that text on the page, then we can use the `text-align` property.

```css
.title {
  text-align: center;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screen-Shot-2022-04-24-at-11.42.48-AM.png)

If you wanted to horizontally center all of the text on the page, then you can use the `text-align` property in the body selector. 

In this next example, we have some more text in our HTML. 

```html
<h1>freeCodeCamp is awesome</h1>
<section>
  <h2>I love learning about HTML</h2>
  <p>Here is my first paragraph</p>
</section>

<section>
  <h2>I love learning about CSS</h2>
  <p>Here is my second paragraph</p>
</section>
```

Without any styling, it currently looks like this on the page.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screen-Shot-2022-04-24-at-12.30.14-PM.png)

In our CSS, we can target the `body` selector and use the `text-align` property.

```css
body {
  text-align: center;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screen-Shot-2022-04-24-at-12.29.56-PM.png)

## How to Horizontally and Vertically Center Text

The `text-align` property is used to horizontally center text on the page. But we can also use CSS Flexbox to vertically center the text. 

In this example, we have some text in our HTML:

```html
<h2 class="title">Let's learn how to center text vertically and horizontally</h2>

<div class="flex-container">
  <p>Flexbox is cool!!!</p>
</div>
```

This is what it currently looks like without any styling.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screen-Shot-2022-04-24-at-12.35.30-PM.png)

We can center the `<h2>` using the `text-align` property.

```css
.title {
  text-align: center;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screen-Shot-2022-04-24-at-12.42.49-PM.png)

We can then horizontally and vertically center the paragraph inside the `flex-container` div using Flexbox. 

```css
.flex-container {
  display: flex;

  /*this centers the text horizontally*/
  justify-content: center;

  /*this centers the text vertically*/
  align-items: center;

  height: 200px;
  color: #fff;
  font-size: 1.2rem;
  background: #00008b;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screen-Shot-2022-04-24-at-12.58.57-PM.png)

## Should you use the center tag?

In older versions of HTML, the `<center>` tag was used as a way to center text horizontally on the page.

```html
<center>I am using center tags to center my text
  <p>This paragraph is also centered</p>
</center>
```

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screen-Shot-2022-04-24-at-12.14.09-PM.png)

A lot of new developers will still use this tag because it does display the correct results. However, the `<center>` tag was deprecated in HTML 4 because best practice is to use the CSS `text-align` property instead.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screen-Shot-2022-04-24-at-12.16.58-PM.png)
_This is the deprecation warning from [MDN docs](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/center)_

It is important to remember that HTML is for content while CSS is for styling. It is best practice to separate those two concerns and not use HTML for styling purposes. 

I hope you enjoyed this article on how to center text using HTML and CSS.

