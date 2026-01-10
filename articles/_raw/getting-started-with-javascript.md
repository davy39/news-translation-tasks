---
title: How to Start Learning JavaScript
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2023-07-13T20:22:41.000Z'
originalURL: https://freecodecamp.org/news/getting-started-with-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/pexels-mikhail-nilov-6968122.jpg
tags:
- name: beginner
  slug: beginner
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'Just in case you haven''t yet been properly introduced, JavaScript is a
  powerful programming language that provides significant value in web development.

  Its benefits include:


  Server-side development through Node.js

  Client-side interactivity where sc...'
---

Just in case you haven't yet been properly introduced, JavaScript is a powerful programming language that provides significant value in web development.

Its benefits include:

* Server-side development through Node.js
* Client-side interactivity where scripts run directly within your users' browsers
* Responsive and interactive user interfaces
* Broad API and third-party service integration that permit multi-tier applications
* Cross-platform mobile app development through frameworks like React Native and Ionic
* Near-universal browser support, and vast ecosystem of libraries, frameworks, and tools

If you're planning to add interactivity into any of your websites, then you'll need to pick up some JavaScript skills. But the basics are actually pretty straightforward. 

In this article I'm going to show you how you can incorporate JavaScript into your HTML code, what simple operations might look like using JavaScript, how to create and execute functions in JavaScript, and how you can take advantage of your browser's console to test JavaScript in a live – but safe – environment.

By the way, there isn't any technical connection between JavaScript and the Java programming language. 

Some time after Brendan Eich created his LiveScript language at Netscape in just 10 days back in 1995, legend has it, he renamed his project JavaScript to leverage the popularity of Java at the time. 

But that was more of a marketing strategy than an indication of any technical relationship.

This article comes from [my Complete LPI Web Development Essentials Study Guide course](https://www.udemy.com/course/complete-lpi-web-development-essentials-exam-study-guide/?referralCode=C92570BCBB38302A9257). If you'd like, you can follow the video version here:

%[https://youtu.be/TrARdpmfD7c]

## How to Incorporate JavaScript into Your HTML Code

You can include JavaScript code in your HTML web pages in a couple ways. First, you can do it by referencing an external `.js` file as an attribute of a `<script>` tag – the way you see here:

```
<script src="script.js"></script>
```

Or you can drop your code between `<script>` tags in the head section of your HTML like this:

```
<head>
  <title>JavaScript App Example</title>
  <script>
    function greet() {
      var name = prompt("What's your name?");
      alert("Hello, " + name + "!");
    }
  </script>
</head>
```

Both work fine. Since the adoption of HTML5, however, you no longer need to add `text/javascript` as an attribute of the `<script>` tag. At this point, JavaScript is the _default_ scripting language for HTML.

## How to Execute Some Simple JavaScript

Here's a simple hello-world kind of script that'll work to get us up and running: 

```
<!DOCTYPE html>
<html>
<head>
  <title>JavaScript App Example</title>
  <script>
    // JavaScript code
    function greet() {
      var name = prompt("What's your name?");
      alert("Hello, " + name + "!");
    }
  </script>
</head>
<body>
  <h1>JavaScript App Example</h1>
  <button onclick="greet()">Say Hello</button>
</body>
</html>
```

Let's work through that code one section at a time. 

You can see that the JavaScript is all in between those two `<script>` tags and contains its own comment line. 

```
  <script>
    // JavaScript code
    function greet() {
      var name = prompt("What's your name?");
      alert("Hello, " + name + "!");
    }
  </script>
```

I really don't know why it has to be this way, but the comment escape codes for one language never seem to work for another. In the JavaScript world, you'll need two forward slashes: `//`.

The first line of real code introduces a new function that's named `greet`. 

```
    function greet() {
      var name = prompt("What's your name?");
      alert("Hello, " + name + "!");
    }
```

The parentheses are necessary and, I assure you, you'll make good use of them later. The function's code must all lie between two curly braces the way you see here.

This function has just two lines. The first uses `var` to declare a variable that'll be called `name`. `name` will take the value entered by users when they're prompted with the "What's your name?" question. 

NOTE: while declaring a variable as `var` still has its use cases, for most modern JavaScript development, [using `let` and `const` is considered a best practice](https://www.freecodecamp.org/news/differences-between-var-let-const-javascript/) due to their improved scoping rules and stricter variable assignment behavior. I went with `var` here for simplicity

Once a value has been entered, `alert` will generate a pop-up window with the text `Hello` , a comma and space, the current value of the `name` variable, and an exclamation mark. The `+` character serves to concatenate all these values into a sentence.

But hang on: you can't see any name entry field on this page, can you? And how exactly is the function executed?

Excellent questions. That'll happen down in the HTML section. This is basically a `<button>` tag that has a text label of `Say Hello`. But it's the tag's attribute that really interests us.

`onclick` calls our `greet` function. In other words, `onclick` tells the browser to execute the `greet` function whenever the button is clicked.

```
<body>
  <h1>JavaScript App Example</h1>
  <button onclick="greet()">Say Hello</button>
</body>
</html>

```

Paste the code into an `.html` file and load it in a browser. When you click the button a new dialog box opens with a data entry field looking for your name. When you type your name and then click `OK`, you'll see nicely concatenated sentence, all perfectly arranged.

## How to Work with JavaScript in a Browser Console

But before moving on, I should remind you that JavaScript was built for browsers. So we can expect some useful integrations. Well, perhaps the most useful of them all is the console. 

You can open the console by right-clicking on any empty spot on a browser page and selecting `Inspect`. This should work no matter what browser you're using. Hitting `F12` is another way to get to the same place. 

In my Brave browser, the console appears on the right side:

![Image](https://www.freecodecamp.org/news/content/images/2023/06/console1.png)
_Opening the console_

This is known as the developer's console, because there are all kinds of helpful debugging and code analysis features packed in. 

In the `Elements` tab, you'll see a representation of the page code. You can expand the `<head>` and the `<script>` sections so you can see what you're working with. Moving over to the `Console` tab, you find a live JavaScript environment.

In this example, I pasted three JavaScript operations into the console which we can actually test. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/webdev-s4-01-f011630.png)

Here's that world-changing code in a cut-and-paste format:

```
console.log(2 + 2);
console.log("Hello" + " " + "World");
var fruits = ["Apple", "Banana", "Orange"];
console.log(fruits.length);
```

Try it yourself.

Now, you should be aware that `console.log()` is a built-in JavaScript function that allows you to output messages or values to the console. It is commonly used for debugging and displaying information during the development process. So, as a rule, you'll only want to use the `console.log` function here.

This would be a great opportunity to introduce you to some JavaScript syntax. The function accepts one or more arguments within parentheses and prints them to the console. 

The first execution is the sum of 2 + 2. 

```
console.log(2+2);
```

From here we can see that you can use any of the arithmetic operators (like plus, minus, the asterisk for multiplication, the forward slash for division, the right angle for greater than, the left angle for less then, and the equal sign) as-is within your JavaScript code. 

The only other thing about this that might catch your attention is the semicolon that follows. In JavaScript, semicolons are statement terminators that help you avoid ambiguity and, sometimes, unexpected behavior. Use 'em early, use 'em often.

The second line contains another example of concatenation. 

```
console.log("Hello" + " " + "World");
```

This one will print the word "Hello" followed by a space, and then the word "World".

Before running the next command, we'll declare a variable called `fruits`, which will contain an array of three words: "Apple", "Banana", and "Orange". 

```
var fruits = ["Apple", "Banana", "Orange"];
console.log(fruits.length);
```

The code that follows will take the variable `fruits` and output its length.

When I hit `Enter` , all three commands will execute in one go. There are three lines of output: "4", "Hello World", and "3" – which is exactly what we would have expected. 

That was nice and everything, but it hardly makes use of your browser's full resources. So now try running a command that'll generate an error. You could, say, add a couple of illegal characters to an operation like these asterisks:

```
console.log("Hello" + " " + "World")**;
```

Here's what happens:

```
VM30:1 Uncaught SyntaxError: Unexpected token ';'
```

You should see an uncaught syntax error. The `VM30:1` test even shows us which line of our code contained the problem - `1` in this case. If this were real code, we'd be a step closer to solving a bug.

## Wrapping Up

You're now properly introduced to the basics of JavaScript and, in particular, how to integrate JavaScript with your HTML and how to use your browser's console environment. Now go see what you can build!

_This article comes from [my Complete LPI Web Development Essentials Study Guide course](https://www.udemy.com/course/complete-lpi-web-development-essentials-exam-study-guide/?referralCode=C92570BCBB38302A9257)._ _And there's much more technology goodness available at [bootstrap-it.com](https://bootstrap-it.com/)_

