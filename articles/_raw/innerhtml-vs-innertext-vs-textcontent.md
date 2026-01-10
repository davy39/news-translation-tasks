---
title: innerHTML vs innerText vs textContent – What's the Difference?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-12-11T21:57:38.000Z'
originalURL: https://freecodecamp.org/news/innerhtml-vs-innertext-vs-textcontent
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/Benjamin-Semah---DevAfterHours-1.png
tags:
- name: DOM
  slug: dom
- name: Front-end Development
  slug: front-end-development
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Benjamin Semah

  In HTML, innerHTML, innerText, and textContent are properties of the DOM (Document
  Object Model). They allow you to read and update the content of HTML elements.

  But they have different behaviours in terms of the content they includ...'
---

By Benjamin Semah

In HTML, `innerHTML`, `innerText`, and `textContent` are properties of the DOM (Document Object Model). They allow you to read and update the content of HTML elements.

But they have different behaviours in terms of the content they include and how they handle HTML markup.

By the end of this article, you will know the differences between these three properties and when you should each one. 

## Table of Contents

* [What is the `innerHTML` property?](#heading-what-is-the-innerhtml-property)
* [What is the `innerText` property?](#heading-what-is-the-innertext-property)
* [What is thet `textContent` property?](#heading-what-is-the-textcontent-property)
* [How to read content with `innerHTML`, `innerText`, and `textContent`](#heading-how-to-read-content-with-innerhtml-innertext-and-textcontent)
* [How to update content with `innerHTML`, `innerText`, and `textConent`](#heading-how-to-update-content-with-innerhtml-innertext-and-textcontent)
* [Security concerns when using `innerHTML`](#heading-security-concerns-when-using-innerhtml)
* [Conclusion](#heading-conclusion)

First, I'll explain how these three properties work. And then you will see some example use cases to learn the differences in their behaviour.

## What is the `innerHTML` Property?

When you use the `innerHTML` property, it reads both the HTML markup and the text content of the element. This means when you use it to set the content of elements, you can include HTML tags, and the browser will render them correctly.

But, be cautious if you're inserting content from user input or any untrusted source with `innerHTML`. Attackers can use the HTML `<script>` tag to insert and run malicious code in your app. More on that later in the article.

## What is the `innerText` Property?

This property focuses on the rendered text content. When you use `innerText` to read the content of an element, it returns the text as it appears on screen. It ignores HTML tags. And it also does not include text that is hidden with CSS styles. 

When you need to account for styles, you should consider using `innerText`. Modifying the `innerText` of an element means the browser may need to adjust the layout to accommodate the changes in text size, which can have performance implications.

## What is the `textContent` Property?

The `textContent` property also ignores all HTML tags and returns only the text. Whiles `innerText` reads text as it is rendered on screen, `textContent` reads text as it is in the markup. It also returns all text, whether it's rendered on screen or not.

Also, `textContent` only deals with the raw text and doesn't account for styles. So, in situations where performance is a concern and you don't need to account for styles, `textContent` might be a more efficient choice compared to `innerText`.

## How to Read Content with `innerHTML`, `innerText`, and `textContent`

Now, let's see some practical examples to understand the three properties better.

The following is a simple markup for a navigation bar with four items. The last element with the text "Pricing" is hidden (display set to none). Let's read the content of the `nav` element using all three properties to see the difference.

```html
<nav>
  <a>Home</a>
  <a>About</a>
  <a>Contact</a>
  <a style="display: none">Pricing</a>
</nav>
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-07-at-11.37.48-AM.png)
_A simple nav bar example_

### Getting content with `innerHTML`

```javascript
// Reading content with innerHTML
const navElement = document.querySelector('nav')
console.log(navElement.innerHTML)
```

![innerHTML example that includes both markup and text](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-07-at-11.32.01-AM.png)
_innerHTML example that includes both markup and text_

The `innerHTML` property returns the full content including all the HTML tags inside the `nav` elements and their text content.

### Getting content with `innerText`

```javascript
// Reading content with innerText
const navElement = document.querySelector('nav')
console.log(navElement.innerText)
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-07-at-11.36.52-AM.png)
_innerText example that prints text as it appears on screen_

The `innerText` property returns the content as rendered on the screen. It ignores all the HTML tags. And it also ignores the hidden element (with display set to none).

### Getting content with `textContent`

```javascript
// Reading content with textContent
const navElement = document.querySelector('nav')
console.log(navElement.textContent)
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-07-at-11.47.30-AM.png)
_textContent example that prints text as it is in the markup including hidden text_

The `textContent` property returns the content as it in the HTML markup. Like `innerText`, it also ignores the HTML tags. But it doesn't consider styles, so it returns the "Pricing" text even though it's hidden.

## How to Update Content with `innerHTML`, `innerText`, and `textContent`

You can also use all three properties to update the content of DOM elements. When updating content, the properties behave in a similar way to when you use them to read or get content.

Let's see some examples to understand it better

### Setting content with `innerHTML`

The markup below includes a header element and an empty `<ul>` element. You can use the `innerHTML` property to insert some content to the `<ul>`.

```html
<h2>Programming languages</h2>
<ul class="languages-list"></ul>
```

```javascript
const langListElement = document.querySelector('.languages-list')

// Setting or updating content with innerHTML
langListElement.innerHTML = `
  <li>JavaScript</li>
  <li>Python</li>
  <li>PHP</li>
  <li>Ruby</li>
`
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-08-at-9.50.06-AM.png)
_An example of setting content with the innerHTML property_

The JavaScript code passes a string of an HTML list as the value for `innerHTML`. The `innerHTML` property recognizes the HTML tags and formats the content accordingly.

Unlike `innerHTML`, both `innerText` and `textContent` will ignore the HTML tags and render everything as a string.

### Setting content with `innerText`

Using the same example, let's see how the `innerText` property will update the content of the programming languages list.

```javascript
const langListElement = document.querySelector('.languages-list')

langListElement.innerText = `
  <li>JavaScript</li>
  <li>Python</li>
  <li>PHP</li>
  <li>Ruby</li>
`
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-08-at-11.12.15-AM.png)
_An example of setting content with the innerText property_

Note how `innerText` ignores the HTML tags and prints them on screen as part of the text. But it still recognises formatting like line-breaks and whitespaces.

### Setting content with `textContent`

When setting or updating content, the `textContent` property will ignore HTML markup and it will also ignore things like line breaks and whitespaces too.

```javascript
const langListElement = document.querySelector('.languages-list')

langListElement.textContent = `
  <li>JavaScript</li>
  <li>Python</li>
  <li>PHP</li>
  <li>Ruby</li>
`
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-08-at-11.22.45-AM-1.png)

Because `textContent` ignores formatting like line breaks and whitespaces, all the text is printed on the same line. When you want the raw text and aren't concerned with formatting of the text, `textContent` is a suitable choice.

## Security Concerns When Using `innerHTML`

Because `innerHTML` processes and interprets HTML tags, it is advisable to use it only when inserting content from trusted sources. Or when you have properly sanitised and validated the provided content.

The browser will run any JavaScript code you put in the HTML script tag. And it can open doors to [Cross-Site Scripting (XSS)](https://www.freecodecamp.org/news/cross-site-scripting-what-is-xss/) where attackers can inject and run malicious script in the context of your web page.

See an example:

```html
<div id="commentSection"></div>
```

Assume you are using the `div` above as container for user comments in your app. And you use `innerHTML` to add new comments without any validation or sanitizing the comment.

Here is a very basic example of how a user can inject and run a malicious script:

```javascript
const commentSection = document.getElementById('commentSection')

let userComment = `<img src="malicious-script.jpg" onerror="alert('Malicious Script Executed!')"> This is my comment!`;

commentSection.innerHTML = userComment;
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-08-at-10.35.53-AM.png)
_Malicious script executed via the &lt;script&gt; tag with innerHTML_

The user deliberately gives an incorrect value for the `src` attribute of the image. This will trigger the `onerror` event which runs an alert with the string "Malicious Script Executed!". 

You can imagine how an attacker can take advantage of this to inject harmful JavaScript code, potentially stealing sensitive user information, manipulating the page content, or performing other malicious actions.

## Conclusion

You can use the three properties `innerHTML`, `innerText`, and `textContent` to manipulate the content of DOM elements. But they behave differently. Understanding them will help you decide when it's appropriate to use each one. 

The `innerHTML` property recognizes HTML tags and renders the content according to the tags. `innerText` and `textContent` ignore HTML tags and treat them as part of the text. You also learned in this article how `innerHTML` can lead to security risks and why you should be mindful of this.

Also, `innerText` reads content as it appears on screen, ignores hidden content, and observes formatting of text. But `textContent` reads content as it appears in the markup. This means it reads hidden content too. But it also ignores formatting like whitespaces and line breaks when you are using it set content.

Thanks for reading. And happy coding. For more in-depth tutorials, feel free to [subscribe to my YouTube channel](https://www.youtube.com/@DevAfterHours).




