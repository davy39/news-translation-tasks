---
title: How to Build a Beginner-Friendly JavaScript Application
subtitle: ''
author: Tapas Adhikary
co_authors: []
series: null
date: '2023-05-09T16:05:03.000Z'
originalURL: https://freecodecamp.org/news/build-a-beginner-friendly-javascript-application
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/freeCodeCamp-Cover.png
tags:
- name: beginner
  slug: beginner
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "JavaScript is a popular programming language for building web, mobile,\
  \ and desktop applications. \nThere are many frameworks and libraries that have\
  \ been built around JavaScript, with more likely being developed even as you are\
  \ reading this article. I..."
---

JavaScript is a popular programming language for building web, mobile, and desktop applications. 

There are many frameworks and libraries that have been built around JavaScript, with more likely being developed even as you are reading this article. If you plan to start learning JavaScript, some of them are worth learning as well.

Like with any programming language, getting a grip on JavaScript has two vital parts: understanding the key concepts and practicing what you've learned. You need to build up familiarity with the main concepts of the language, and at the same time, you need to start hands-on practice coding projects using the concepts you've learned. 

I recently published an article on [How to Learn JavaScript Effectively with Tips and Learning Strategies](https://www.freecodecamp.org/news/how-to-learn-javascript-effectively/). You should check it out if you haven't already.

In this article, we will focus on the hands-on practice part. We will build a beginner-friendly JavaScript application that will teach you the basics of creating HTML structure, working with CSS, and finally adding dynamic behaviour using JavaScript.

All set? Let's get started.

If you like to learn from video content as well, this article is also available as a video tutorial here: 🙂

%[https://www.youtube.com/watch?v=NkO4mVXnrtM]

## What Are We Building Today?

We will be building a project called `Colorify`. It shows a coloured circle on the web page and has some buttons that let you change the colours by clicking on them. 

The image below shows a red circle with three buttons labeled Red, Green, and Yellow. When you click on the Red, the circle colour will turn Red – the same for Green and Yello, respectively.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-32.png)
_The Colorify Project_

We will use the following concepts of web development while creating this application:

* Basic DIV styling with border-radius and centering
* Laying out Buttons
* Usage of Template Literals
* Adding Click Handlers
* DOM manipulation to set values

## How to Create a JavaScript Project Structure

First things first, let's create the project structure. Create a folder called `colorify` and create these empty files inside it.

* **index.html**: The HTML file that will contain the skeleton and markup of the application.
* **index.css**: All the styles and beautification code of the application goes into this CSS file. We will include the CSS file in the HTML file created above.
* **index.js**: The JavaScript code goes into this file. We will create functions to provide dynamic behaviour to the application. Like the CSS file, we will also include this file in the `index.html` file.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/unnamed.png)
_The project structure_

## How to Build the HTML Structure 

Let's create the HTML page structure. We need a circle and three buttons as part of the project requirements. Copy the following code and paste it inside the `index.html` file:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Colorify</title>
  <link rel="stylesheet" href="./index.css">
  <script src="./index.js" defer></script>
</head>
<body>
  <div class="container">
    <h1>Colorify</h1>
    <p class="subheading">
      With colorify we want to start
      learning JavaScript.
    </p>
    <div class="circle" id="circleID"></div>
    <div class="action">
      <button onclick="paint('red')">Red</button>
      <button onclick="paint('green')">Green</button>
      <button onclick="paint('yellow')">Yellow</button>
    </div>
  </div>
</body>
</html>
```

The HTML file has two primary sections:

### the `<head>` section

The `<head>` section includes meta information like the supported character set, what version of Internet Explorer the page should be rendered using the X-UA-Compatible value, and the viewport information. We also provided a title to the web page.

We have included the CSS file using the link tag. We used the `href` attribute to point to the `index.css` file. Last, we added the `index.js` script file using the script tag. 

Note that we used the `defer` attribute to add the script to the HTML. You can tackle the script loading performance with attributes like defer and async. 

If you are new to this, you can check out this article: [JavaScript Performance – How to Improve Page Speed with async and defer](https://www.freecodecamp.org/news/javascript-performance-async-defer/).

```html
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Colorify</title>
  <link rel="stylesheet" href="./index.css">
  <script src="./index.js" defer></script>
</head>
```

### The `<body>` section

The <body> section defines what will be visible to the users through the browser's rendering process. In the code below, we have first created a container div (a simple div tag with a class called `container`) that wraps all the HTML elements we plan to show on the web page.

First is a heading that renders our application name. Next, a paragraph shows some text about the application. Then we have a div with an id called `circleID`. We will use this div to draw a circle. Last, we have three buttons wrapped inside another div.

Also notice that each of the buttons has a click handler associated with it using the `onClick`.

```html
<div class="container">
    <h1>Colorify</h1>
    <p class="subheading">
      With colorify we want to start
      learning JavaScript.
    </p>
    <div class="circle" id="circleID"></div>
    <div class="action">
      <button onclick="paint('red')">Red</button>
      <button onclick="paint('green')">Green</button>
      <button onclick="paint('yellow')">Yellow</button>
    </div>
</div>
```

Let's run the application at this stage and see the output.

Note that there are multiple ways to run the application. The simplest method is to navigate to the project folder and open the `index.html` file on a web browser. But this approach may only work for some scripts. 

The recommended approach is to run the project as part of a `web server`. You can use the `Live Server` extension in the `Visual Studio Code` editor for this.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-35.png)
_The App - First Stage_

Hang on! Where is the circle? We do not see the circle because we have just created a container for it but not provided the style elements to make it look like a circle. 

Also, we can do a far better job aligning the HTML elements on the web page. Let's fix these issues using CSS.

## How to Use CSS to Style the Code

Open the `index.css` file and add the following content to it:

```css
.container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.circle {
  border: 1px solid #000000;
  width: 200px;
  height: 200px;
  border-radius: 50%;
}

.action {
  margin: 10px;
}

button {
  cursor: pointer;
}
```

We have provided a flex layout to the outer container div specifying to centre the elements inside it in a column. We have provided an equal height and width to the circle div to make is appear like a square. Now we curve all side of the border with the the border-radius property to make it look like a circle.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-37.png)
_The App - Second Stage_

Now the app looks much better! 

Let's click on the buttons. Oh! We see that an error gets logged into the console panel. The reason is, we have added the click handlers to the buttons but haven't defined the `paint()` function to execute when user clicks on these buttons.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-38.png)
_The App - Third Stage showing the error_

It's time to define the `paint()` function and get things working.

## How to Add Dynamic Behaviour using JavaScript

Now open the `index.js` file and copy paste the following code snippet to it:

```js
function paint(color) {
  const circle = document.getElementById('circleID');
  circle.style = `background-color:${color}`;
}
```

We have now defined a `paint()` function that we have passed to the `onClick` handlers of the buttons. You may have noticed (in the index.html file), we have passed the respective colours to the `paint()` function when user clicks on a button. 

Let's dive into the `paint()` method and understand things.

* First we access the div element that represents the circle. We can identify the element using the id attribute value provided to it, that is `circleID`. We use the DOM method called `document.getElementById` to get it.
* Once we have the element, we can add a style to it. We are adding a background colour style based on the colour name passed to the function. Note that we are using the template literal expressions here over a regular string concatenation. [This article](https://blog.greenroots.info/what-exactly-is-javascript-tagged-template-literal) will help you to get a grip on template literals if you are new to them.

That's it. Now every time a user clicks on a button, the respective colour gets added as a background colour to the circle. It works like the following example:

![Image](https://www.freecodecamp.org/news/content/images/2023/05/Screen-Recording-2023-05-09-at-3.24.23-PM.gif)
_The App - Final Stage_

## Task for You: Complete the QUIZ

Alright, so you have learned how to create a color changer project using HTML, CSS, and plain JavaScript. Let's take it to one level further. Here is a task for you to complete.

* Add another button called `Random` beside the existing buttons.
* When user click on the `Random` button, you must add a random background colour to the circle.
* You should reuse the existing `random()` function we have seen in the `index.js` file.

If you complete this task and want me to review your code, feel free to create a Tweet/LinkedIn post using the link to your code by tagging me. I'll make sure to review and comment.

## Before We End...

That's all for now. I hope you found this article informative and insightful. All the source code used in this article can be found on [this GitHub repository](https://github.com/atapas/youtube/tree/main/javascript/projects/colorify).

Let's connect.

* [SUBSCRIBE](https://www.youtube.com/tapasadhikary?sub_confirmation=1) to my YouTube channel if you want to learn JavaScript, ReactJS, Node.js, Git, and all about Web Development in a practical way.
* [Follow on Twitter](https://twitter.com/tapasadhikary) or [LinkedIn](https://www.linkedin.com/in/tapasadhikary/) if you don't want to miss the daily dose of Web Development and Programming Tips.
* Check out my Open Source work on [GitHub](https://github.com/atapas).
* Follow on [Showwcase](https://www.showwcase.com/atapas398) for community-based learning.

See you soon with my next article. Until then, please take care of yourself, and stay happy.

