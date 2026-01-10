---
title: How to Use GitHub Copilot with Visual Studio Code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-07-05T15:12:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-github-copilot-with-visual-studio-code
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/How-to-Build-a-Weather-Application-using-React--1-.png
tags:
- name: automation
  slug: automation
- name: GitHub
  slug: github
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'By Nishant Kumar

  Hey everyone, welcome! In this article, we will learn how to use the GitHub Copilot
  AI tool with Visual Studio Code.

  What is GitHub Copilot?

  GitHub Copilot is a tool that can help you write easier and faster code. It is powered
  by GP...'
---

By Nishant Kumar

Hey everyone, welcome! In this article, we will learn how to use the GitHub Copilot AI tool with Visual Studio Code.

## What is GitHub Copilot?

GitHub Copilot is a tool that can help you write easier and faster code. It is powered by **GPT-3**. You just have to write the description of the code you need – for example, writing a function to generate a random number, or sorting an array – and Copilot creates it for you.

And it doesn't just create one solution. It generates more than one, and you can choose which one you want.

In this tutorial, we will learn to how to set up the GitHub Copilot AI tool for Visual Studio Code, as well as how to generate code for JavaScript, React, and HTML.

## How to Install GitHub Copilot

To add GitHub Copilot, head over to your [GitHub](https://github.com/) and go to settings.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-02-181658.png)

Choose GitHub Copilot on the left menu and simply allow it, then click the **Save** button.

Now open Visual Studio Code and go to **Extensions**. Search for GitHub Copilot in the search bar.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-02-181954.png)

Install Github Copilot and restart your Visual Studio Code.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-02-182152.png)

And at the bottom, you will see that GitHub Copilot has been activated.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/Untitled-design.png)

But keep in mind that we only have the trial version at the moment. And it's only good for two months – the free trial ends August 22nd. We'll have to buy the full version after the trial finishes.

It will cost you $10 per month, or $100 per year.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-02-182753.png)

Now that we have installed Copilot, let's get to the more fun part where we get to use it.

## How to Use GitHub Copilot to Generate JavaScript Code

Let's start with something simple. Let's create a function to add two numbers.

In a JavaScript file, simply write a comment like "**Generate a function to add two numbers**."

```
//Generate a function to add two numbers
```

Then press enter. It will throw you the suggestions, which you can accept by pressing the **tab button.**

```
//Generate a function to add two numbers
function add(a, b) {
```

Then press enter for the next line, and when the next line of code comes up, press **tab again.**

```
//Generate a function to add two numbers
function add(a, b) {
  return a + b;
}

```

And here is your function to add two numbers.

Now let's call the function **`add()`**. Write the function invocation, and it will accept some random parameters automatically.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot--267--1.png)

We can also subtract, multiply, and divide numbers. 

## How to Use GitHub Copilot to Generate a Function to Display the Colors of the Rainbow in an Array

We will start with a comment "**Generate an array of all the colors from the rainbow**."

```
//Generate an array of all the colors from the rainbow
```

Then just like before, we will press enter.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot--268-.png)

And it will generate the array of all the colors in the rainbow. 

```
//Generate an array of all the colors from the rainbow
var colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'];
```

## How to Create Three Arrays with the Types Number, String, and Boolean and Merge them in an Object

Now let's try to create an array of Numbers, Strings, and Boolean values.

```
//Create an array of numbers
var numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

//Create an array of strings
var strings = ["hello", "world", "how", "are", "you"];

//Create an array of booleans
var booleans = [true, false, true, false, true];
```

Now, let's merge them in an object. We will create an **Object** like this:

```
var objects = [
    {
        number: 1,
        string: "hello",
        boolean: true
    },
    {
        number: 2,
        string: "world",
        boolean: false
    },
    {
        number: 3,
        string: "how",
        boolean: true
    },
]
```

Write a comments that says "**Create an array of objects with the above array items as key value pairs**."

You can press the **Tab** button to accept the solution, or press **CTRL + Enter** to open the Copilot solutions page.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-02-185657.png)

You can accept any solution you want. Simply click **Accept**.

```
//Create an array of numbers
var numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

//Create an array of strings
var strings = ["hello", "world", "how", "are", "you"];

//Create an array of booleans
var booleans = [true, false, true, false, true];

//Create an array of objects with the above array items as key value pairs
var objects = [
  {
    number: 1,
    string: "hello",
    boolean: true,
  },
  {
    number: 2,
    string: "world",
    boolean: false,
  },
  {
    number: 3,
    string: "how",
    boolean: true,
  },
  {
    number: 4,
    string: "are",
    boolean: false,
  },
  {
    number: 5,
    string: "you",
    boolean: true,
  },
];

```

## How to Import Things in React and Express

Now let's try to see how things work in React and Express.

We will simply import a few modules.

Let's first import the **useState Hook** from **React**.

```
//Import useState Hook from react
```

Write the comment, and press Enter. Copilot will generate the code.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot--270-.png)

```
//Import useState Hook from react
import React, { useState } from 'react';
```

Let's try one more for React, which is importing the useEffect and the useState Hooks from React.

```
//Import useState and useEffect hook from react
import React, { useState, useEffect } from 'react';
```

Let's do something in Express. Let's import the **CORS npm Package** in Express, which is made for Node and Express. And it will be here.

```
//Import cors from express
const cors = require('cors');
```

## How to Generate Code for HTML

Let's try some HTML code.

First, let's generate some code to create an unordered list, with Nishant, 25, and Patna. 

```
Create an ul tag with list items Nishant, 25, and Patna
    <ul>
      <li>Nishant</li>
      <li>25</li>
      <li>Patna</li>
    </ul>
```

![Image](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-02-191108.png)

Let's try the same, but with the list style as none.

```
Create an ul tag with the list having a class of lists and the items
    Nishant, 25, and Patna and the list style as none
    <ul class="lists" style="list-style: none">
      <li>Nishant</li>
      <li>25</li>
      <li>Patna</li>
    </ul>
```

And here it is. Amazing right?

## Wrapping Up

In this article you learned what GitHub Copilot is and how to use it.

You can also check out my video on the same topic, which is [Let's Test the GitHub Copilot - GitHub Copilot Tutorial with Visual Studio Code](https://youtu.be/PdXBepPOqqI)

Thank you for reading. Happy Learning.

