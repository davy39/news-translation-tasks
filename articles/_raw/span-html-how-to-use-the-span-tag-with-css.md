---
title: Span HTML – How to Use the Span Tag with CSS
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-09-08T01:18:28.000Z'
originalURL: https://freecodecamp.org/news/span-html-how-to-use-the-span-tag-with-css
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/span-tag.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "You can use the HTML span tag as a container to group inline elements together\
  \ so you can style or manipulate them with JavaScript. \nIn this article, I will\
  \ show you how to use the span tag to make a certain part of your content distinct\
  \ from the res..."
---

You can use the HTML `span` tag as a container to group inline elements together so you can style or manipulate them with JavaScript. 

In this article, I will show you how to use the span tag to make a certain part of your content distinct from the rest. Then you should be able to start using it in your coding projects.

## What is the `span` tag used for?

The `span` tag is just like a div, which is used to group similar content so it can all be styled together. 

But `span` is different in that it is an inline element, as opposed to `div`, which is a block element.

Also, keep in mind that `span` itself does not have any effect on its content unless you style it.

There are two major uses of the `span` tag – styling and manipulating a particular text with JavaScript.

### How to style text with the `span` tag

If you want to makes some particular text or any other content different from the rest, you can wrap it in a `span` tag, give it a class attribute, then select it with the attribute value for styling.

In the examples below, I change the `color`, `background-color`, and `font-style` of some text by wrapping it in a `span` tag. 

#### How to change the text color

```html
<p>This a <span class="crimson-text">crimson text</span> within others.</p>
```

```css
.crimson-text {
      color: crimson;
   }
```


I have added some basic CSS to center everything on the page:

```css
body {
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto;
        height: 100vh;
      }
```

![text-color-span](https://www.freecodecamp.org/news/content/images/2021/09/text-color-span.png)

#### How to change background color

```html
<p>
      A <span class="green-background">green background color</span> perfectly
      implies the beauty of nature.
</p>
```

```css
 .green-background {
        background-color: #2ecc71;
      }
```

![background-color-span](https://www.freecodecamp.org/news/content/images/2021/09/background-color-span.png)

#### How to change font style

```html
<p>
   An <span class="font-style">italic</span> font style could be instrumental
   in laying emphasis on a text.
</p>
```

```
.font-style {
     font-style: italic;
   }
```

 ![font-style-span](https://www.freecodecamp.org/news/content/images/2021/09/font-style-span.png)
 
### How to Manipulate JavaScript with the `span` tag 

Just as it is possible to style content by wrapping a `span` tag around it, you can also manipulate your content by wrapping it in a `span` tag. You give it an `id` attribute and then select it by its id with JavaScript so you can manipulate it.

In the example below, I changed some text within other text to uppercase with JavaScript:

```html
<p>
   The text, <span id="uppercase"> freecodecamp</span>, was turned to
   upperase with JavaScript
</p>
```

```js
const uppercase = document.querySelector("#uppercase");

uppercase.style.textTransform = "uppercase";
```

![javascript-span](https://www.freecodecamp.org/news/content/images/2021/09/javascript-span.png)

## Conclusion 

In this tutorial, you have learned how to manipulate a particular piece of text with CSS and JavaScript by wrapping it in a `span` tag and giving it a unique `class` or `id` attribute. 

Please note that in cases like this, you should use classes for styling and ids for manipulation with JavaScript in order to avoid confusion. 

Thank you for reading, and keep coding.


