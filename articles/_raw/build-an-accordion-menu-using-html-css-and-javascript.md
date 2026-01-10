---
title: How to Build an Accordion Menu Using HTML, CSS and JavaScript
subtitle: ''
author: Kingsley Ubah
co_authors: []
series: null
date: '2021-09-29T19:45:33.000Z'
originalURL: https://freecodecamp.org/news/build-an-accordion-menu-using-html-css-and-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/accordion-canva.png
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'You can use HTML, CSS and JavaScript to create stylish and dynamic web
  elements. And one useful element you can build is an accordion menu.

  Accordion menus expand and collapse when a user clicks a button. It''s a great way
  to not have to show all the ...'
---

You can use HTML, CSS and JavaScript to create stylish and dynamic web elements. And one useful element you can build is an accordion menu.

Accordion menus expand and collapse when a user clicks a button. It's a great way to not have to show all the info about a topic up front, and instead give users the option to show only what they need.

In this tutorial, I'll show you how to build a simple accordion menu that looks like this:

![ezgif.com-gif-maker.gif](https://cdn.hashnode.com/res/hashnode/image/upload/v1632910257498/EuFFg0l3d.gif align="left")

## What is an Accordion Menu?

In UI design, an accordion menu is a vertically stacked list of various pieces of information. For each list, there is a labelled header pointing to corresponding content. Each list's content is hidden by default. Clicking on a particular label will expand its content.

One very common use case for accordions is to hold a list of frequently asked questions. Clicking on any question will toggle/show a corresponding answer.

## How to Build an Accordion Menu using HTML, CSS and JS

We'll begin by defining the HTML markup. If you are using an IDE like VS Code and you have emmet installed, create a new `index.html` file and type `!` followed by enter. This should create HTML boilerplate code for your project.

Alternatively, you can copy the following code into your `index.html`, or get the code for this project from [Codepen](https://codepen.io/ubahthebuilder/pen/gORqxNe).

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>

  <script src="app.js" type="text/javascript"></script>
</body>
</html>
```

The folder structure is simple. We will create a folder called accordion. Inside the folder we will create three files: `index.html`, `styles.css`, and `app.js`. We will also link all files into our HTML markup as you can see above.

### HTML Markup for the Accordion

For each list in the menu, we will have two `div`s – one for the label, the other for the content.

```html
<body>
  <div class="accordion-body">
  <div class="accordion">
    <h1>Frequently Asked Questions</h1>
    <hr>
    <div class="container">
      <div class="label">What is HTML</div>
      <div class="content">Hypertext Markup Language (HTML) is a computer language that makes up most web pages and online applications. A hypertext is a text that is used to reference other pieces of text, while a markup language is a series of markings that tells web servers the style and structure of a document. HTML is very simple to learn and use.</div>
    </div>
    <hr>
    <div class="container">
      <div class="label">What is CSS?</div>
      <div class="content">CSS stands for Cascading Style Sheets. It is the language for describing the presentation of Web pages, including colours, layout, and fonts, thus making our web pages presentable to the users. CSS is designed to make style sheets for the web. It is independent of HTML and can be used with any XML-based markup language. CSS is popularly called the design language of the web.
</div>
    </div>
    <hr>
    <div class="container">
      <div class="label">What is JavaScript?</div>
      <div class="content">JavaScript is a scripting or programming language that allows you to implement complex features on web pages — every time a web page does more than just sit there and display static information for you to look at — displaying timely content updates, interactive maps, animated 2D/3D graphics, scrolling video jukeboxes, etc. — you can bet that JavaScript is probably involved. It is the third of the web trio.</div>
    </div>
    <hr>
    <div class="container">
      <div class="label">What is React?</div>
      <div class="content">React is a JavaScript library created for building fast and interactive user interfaces for web and mobile applications. It is an open-source, component-based, front-end library responsible only for the application’s view layer. In Model View Controller (MVC) architecture, the view layer is responsible for how the app looks and feels. React was created by Jordan Walke, a software engineer at Facebook. </div>
    </div>
    <hr>
    <div class="container">
      <div class="label">What is PHP?</div>
      <div class="content">PHP is a server-side and general-purpose scripting language that is especially suited for web development. PHP originally stood for Personal Home Page. However, now, it stands for Hypertext Preprocessor. It’s a recursive acronym because the first word itself is also an acronym.</div>
    </div>
    <hr>
    <div class="container">
      <div class="label">What is Node JS?</div>
      <div class="content">Node.js is an open-source, cross-platform, back-end JavaScript runtime environment that runs on the V8 engine and executes JavaScript code outside a web browser. Node.js lets developers use JavaScript to write command line tools and for server-side scripting—running scripts server-side to produce dynamic web page content before the page is sent to the user's web browser. Consequently, Node.js represents a "JavaScript everywhere" paradigm</div>
    </div>
    <hr>
  </div>
  </div>

  <script src="index.js" type="text/javascript"></script>
</body>
```

Without CSS, our page will look all bare, like this:

![htmlook.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1632478639319/6_WWaZagG.png align="left")

*How the accordion menu looks without CSS*

### How to Style the Accordion with CSS

We want our accordion menu to look good, of course. Time to bring some CSS into play. I've added some comments in the code to explain what each piece is doing:

```c
@import url('https://fonts.googleapis.com/css2?family=Rubik:wght@300&display=swap');

/* Sets the background color of the body to blue. Sets font to Rubik */

body {
  background-color: #0A2344;
  font-family: 'rubik', sans-serif;
}

/* Aligns the heading text to the center. */
 
h1 {
  text-align: center;
}

/* Sets the width for the accordion. Sets the margin to 90px on the top and bottom and auto to the left and right */

.accordion {
  width: 800px;
  margin: 90px auto;
  color: black;
  background-color: white;
  padding: 45px 45px;
}
```

With all of these styles applied, here is how our accordion will look like now:

![withcss1.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1632479039630/X8DyVEIrx.png align="left")

*Styles added to the accordion menu*

Now we need to start doing some work on the inside to set up its functionality. First, we set the position property for each of the containers (holding both the label and content) to relative.

That means we can now position its children relative to it.

```css
.accordion .container {
  position: relative;
  margin: 10px 10px;
}

/* Positions the labels relative to the .container. Adds padding to the top and bottom and increases font size. Also makes its cursor a pointer */

.accordion .label {
  position: relative;
  padding: 10px 0;
  font-size: 30px;
  color: black;
  cursor: pointer;
}
```

You can now notice the difference in the image below:

![withcss2.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1632479377592/ZaOptRvWO5.png align="left")

The next action will be to append a little '+' sign at the end of each list. This will let users know that they can expand the section to learn/see more.

We will achieve this using the `::before` selector. The `::before` and `::after` selector is used to place content before of or after a specified element.

Here, we are inserting '+' before the label. But we will use the offset properties `top` and `right` to place it at the far right corner.

```css

/* Positions the plus sign 5px from the right. Centers it using the transform property. */

.accordion .label::before {
  content: '+';
  color: black;
  position: absolute;
  top: 50%;
  right: -5px;
  font-size: 30px;
  transform: translateY(-50%);
}

/* Hides the content (height: 0), decreases font size, justifies text and adds transition */

.accordion .content {
  position: relative;
  background: white;
  height: 0;
  font-size: 20px;
  text-align: justify;
  width: 780px;
  overflow: hidden;
  transition: 0.5s;
}

/* Adds a horizontal line between the contents */

.accordion hr {
  width: 100;
  margin-left: 0;
  border: 1px solid grey;
}
```

This will make everything better. Also notice that the content for each list is now hidden.

![nowbig.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1632480128515/4Q2E4YR5d.png align="left")

*Accordion menu's content is now hidden*

### Adding JavaScript to our Accordion

At this point, our accordion is pretty much static. To make a container display the content when a user clicks on it, we will need to bring in some JavaScript.

Navigate to your script `app.js` and type in the following code:

```js
const accordion = document.getElementsByClassName('container');

for (i=0; i<accordion.length; i++) {
  accordion[i].addEventListener('click', function () {
    this.classList.toggle('active')
  })
}
```

This script will access all of our lists by `classname` of `container`.

Then we will loop through the list. For each container, we simply want to register an event listener to it. When it gets clicked, we want to toggle the class "active" on that element.

Now we are going to test this effect. Click the first container with the label `What is HTML`, open your DevTools (click on F12), and inspect it inside of the elements tab.

You should find the `active` class registered on it:

![active.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1632480884158/5AuG4fo_q.png align="left")

*active class toggled on first menu item*

Clicking on the element again will remove the `active` class from it.

### How to Finish Up the App

There is one last thing we need to do. We need to create an active class within a stylesheet. We will define how we want our accordion to look once JavaScript toggles the class on a container.

```css

/* Unhides the content part when active. Sets the height */

.accordion .container.active .content {
  height: 150px;
}

/* Changes from plus sign to negative sign once active */

.accordion .container.active .label::before {
  content: '-';
  font-size: 30px;
}
```

This is how our app looks and behaves in the end:

![ezgif.com-gif-maker.gif](https://cdn.hashnode.com/res/hashnode/image/upload/v1632910257498/EuFFg0l3d.gif align="left")

*Final look*

## Wrapping Up

So in this tutorial, we built an accordion menu using HTML, CSS, and JavaScript.

Thanks for following along. I hope you learned something useful from this tutorial.

If you are interested in content like this, [follow my blog](https://ubahthebuilder.tech).

Have a great week.

> **P/S**: If you are learning JavaScript, I created an eBook which teaches 50 topics in JavaScript with hand-drawn digital notes. [Check it out here](https://ubahthebuilder.gumroad.com/l/js-50).
