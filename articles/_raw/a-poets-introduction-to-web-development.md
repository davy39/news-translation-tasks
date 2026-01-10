---
title: A poet's introduction to web development
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-15T16:00:00.000Z'
originalURL: https://freecodecamp.org/news/a-poets-introduction-to-web-development
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca172740569d1a4ca4ea0.jpg
tags:
- name: beginners guide
  slug: beginners-guide
- name: learning to code
  slug: learning-to-code
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Usheninte Dangana

  I honestly feel that coding is the best thing, after baked bread. The freedom it
  offers - financial and otherwise - is a high motivator, and gives the welcoming
  feeling that makes most people choose to learn to code.

  Let''s get to...'
---

By Usheninte Dangana

I honestly feel that coding is the best thing, after baked bread. The freedom it offers - financial and otherwise - is a high motivator, and gives the welcoming feeling that makes most people choose to learn to code.

Let's get to it.

---

### What is web development?

For most people, this involves static web development, with **HTML**, **CSS**, and **JavaScript**. This generally means, web development without the overhead of UI  Libraries or Frameworks like React, Angular or Vue.

So, what makes up a website. Generally, the table below explains this in a straightforward way:

Element | Use
---|---
HTML | Structure
CSS | Styling
JS | Interactivity

HTML stands for **HyperText Markup Language** and this is responsible for the structural side of websites. Think of it as a skeleton of sorts.

CSS stands for **Cascading StyleSheets**, and does the large portion of the styling and design work that goes into websites. CSS adds an extra element of aesthetic to web development, and gives that essential element of seasoning to the dish that is a website. Think of it as a sort of skin.

JS stands for **JavaScript**, and this adds the layer of interactivity essential to everything on the web. Think of it as the nerves of a website. JavaScript makes things bounce, twirl, and do other fun stuff. This is a great understatement - however, you get the picture. ?

Here is a basic webpage that has all the elements above. However, this is far from production grade.

```html
<!-- HTML -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Poets Web Intro</title>

  <!-- CSS -->
  <style>
    h1 {
      color: #3cb271;
    }
  </style>
  <!-- End of CSS -->

</head>
<body>

  <h1>Hi there :)</h1>

  <p></p>
  
  <!-- JavaScript -->
  <script>
    var text = document.querySelector("p");

    text.innerHTML = "Hello Readers!";
  </script>
  <!-- End of JavaScript -->

</body>
</html>
<!-- End of HTML -->
```

Here, the styling is inline and attached to the head section of the HTML document. The `<head></head>` section of a HTML document contains the most important information regarding a website.

The following section `<body></body>` holds information, that will be displayed within the browser window. In this case a simple `<h1>` tag (or **header 1** element) that shows users a large welcome message.

Here is a [live demo](https://codepen.io/usheninte/full/KjxJVb) of the code above.

The inline CSS does not do much here. It only changes the color of the `h1` element to a shade of green:

![Image](https://www.freecodecamp.org/news/content/images/2019/07/3cb271---green.png)
_#3cb271 - GREEN_



If you look back at the code, there is an empty paragraph tag. This is the opening and closing `<p></p>` tag, that has nothing in-between. Yet still, the text "**Hello Readers!**" can be screen in the demo browser window. This is a small display of the power that JavaScript has.

The paragraph tag was first targeted with `document.querySelector("p")`, which picked the element on the HTML document, with the tag `<p>`. It was then saved into a variable with `var text`, with the **second word** here being the **variable name**. 

The second line within the `<script></script>` tag, where the JavaScript resides in this HTML document, does something beautiful. It targets the newly created variable `text` using the HTML DOM property of **innerHTML**, with the following line:

```js
text.innerHTML = "Hello Readers!";
```

This then fills the **text** variable with the text "**Hello Readers!**", and then by so doing, the `<p></p>` with the same text content.

```js
var text = document.querySelector("p");

text.innerHTML = "Hello Readers!";
```

---

### The DOM - Document Object Model

![Image](https://www.freecodecamp.org/news/content/images/2019/07/html-dom.png)
_Source: ([https://www.w3schools.com/whatis/whatis_htmldom.asp](https://www.w3schools.com/whatis/whatis_htmldom.asp))_

What we did in the example above, was find an HTML element in the DOM, and update its content using Vanilla JS. Pure JavaScript (or _Vanilla JS_) is a term, used to refer to natural JavaScript syntax and functionalities without any Framework or Library interference.

The **HTML DOM** works in two ways - both as an **Object Model** for HTML and an **API** for JavaScript. It is generally responsible for interactivity within websites. 

![Image](https://www.freecodecamp.org/news/content/images/2019/07/html-dom-2.png)
_Source: ([https://www.w3schools.com/whatis/whatis_htmldom.asp](https://www.w3schools.com/whatis/whatis_htmldom.asp))_

The manipulation of the DOM is a significant part of web development, as it helps developers create more dynamic and visually appealing websites.

---

I do hope you've had a good time reading through this. This a very introductory level overview of web development. You can follow the **freeCodeCamp** [Responsive Web Design curriculum](https://learn.freecodecamp.org/), to have a firmer grasp on web development concepts. 

> Remember to do some projects too! ?

