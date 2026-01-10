---
title: JavaScript Modules – A Beginner's Guide
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-12-15T16:47:38.000Z'
originalURL: https://freecodecamp.org/news/javascript-modules-beginners-guide
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/lego.jpg
tags:
- name: JavaScript
  slug: javascript
- name: modules
  slug: modules
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Madison Kanna

  JavaScript modules (also known as ES modules or ECMAScript modules) were created
  to help make JavaScript code more organized and maintainable.

  Understanding how ES modules work will help you become a better JavaScript developer.
  In t...'
---

By Madison Kanna

JavaScript modules (also known as ES modules or ECMAScript modules) were created to help make JavaScript code more organized and maintainable.

Understanding how ES modules work will help you become a better JavaScript developer. In this article, we'll cover:

* [What is a module?](#heading-what-is-a-module)
* [What are ES modules? Why do we use them?](#heading-what-are-es-modules-why-do-we-use-them)
* [How to use ES modules](#heading-how-to-use-es-modules)
* [Other module systems used in JavaScript](#heading-other-module-systems-in-javascript)

Let's get started.

<h1 id="module">What is a module?</h1>

A module in JavaScript is just a file of code. You can think of a module as a reusable and independent unit of code.

Modules are the building blocks of your codebase. As your application gets bigger, you can split your code up into multiple files, aka modules. 

Using modules allows you to break down large programs into more manageable pieces of code. 

<h1 id="es-modules">What are ES modules? Why do we use them?</h1>

**ES modules are the official module system used in JavaScript.** There are other module systems that can be used in JavaScript as well, and we'll talk more about those later. But for now, know that we're learning about ES modules rather than other module systems because they're standard for modules in JavaScript. 

As a JavaScript developer, you'll likely use ES modules in your daily work.

Here are some of the advantages that developers get from using ES modules:

1. **Organization.** By breaking down large programs into smaller pieces of related code, you keep your program organized.
2. **Reusability.** With ES modules, you can write code in one place and reuse that code in other files throughout your codebase. For example, instead of rewriting the same function everywhere, you can write a function inside of one module and then import it into another file and use it there.

Let’s dive into an example using ES modules. We'll learn about how ES modules work so you can use them in your projects going forward. As we work with ES modules, we’ll see each of the above advantages demonstrated. 

<h1 id="how-to-use">How to use ES Modules</h1>

Let’s start out with creating a vanilla JavaScript [Replit](https://replit.com/). You can also find the completed code [here](https://replit.com/@madisonkanna/ES-Modules).  
  
Once on Replit, we can create a new project and choose HTML, CSS, and JavaScript. This will create a starter project that has an `index.html` file, a `script.js` file, and a `style.css` file. This is everything we need to get set up.

Inside of our index.html file, we're going to modify our script tag to include `type="module"`. This will allow us to start using ES modules in our code. Modify your script tag to be:

```javascript
<script type="module" src="script.js"></script>
```

Let’s start out by writing a simple add function. This function will take two numbers, add them together, and then return the result of that addition. We'll also call this function. We'll write this function in our `script.js` file:

```javascript
function add(a, b) {
 return a + b;
};
console.log(add(5, 5)); //outputs 10
```

So far, our `script.js` file is small with little code in it. But imagine that this application gets bigger and we have dozens of functions like this. This `script.js` file could get too big and become harder to maintain.  

Let’s avoid this problem by creating a module. We can do this by clicking 'Add File', within our replit. Remember, a module is just a file of related code. 

We'll call our module `math.js`. We're going to remove this add function from our `script.js` file, and we're going to create a new file, `math.js`. This file will be our module where we'll keep our math-related functions. Let's place our add function inside this file:

```javascript
// math.js

function add(a, b) {
 return a + b;
};
```

We've decided to call this module `math.js`, because we will create more math related functions in this file later on. 

If we were to open this application and see it at a glance, we'd know that our math-related logic is inside this file. We don’t need to waste time coming into this application and searching for our math functions and wondering about where they are – we've organized them neatly into a file.

Next, let’s use the add function inside of our `script.js` file, even though the function itself now lives inside of the `math.js` file. To do this, we need to learn about ES module syntax. Let's go over the `export` and the `import` keywords. 

## The export keyword

When you want to make a module available in other files besides the one it lives in, you can use the `export` keyword. Let’s use the `export` keyword with our add function so we can use it inside of our `script.js` file. 

Let's add `export default` underneath our add function inside of math.js:

```javascript
// math.js

function add(a, b) {
 return a + b;
};

export default add;
```

With the last line, we are making this add function available to use in other places besides the `math.js` module.

Another way of using the `export` keyword is to add it just before we define our function: 

```js
// math.js

export default function add(a, b) {
 return a + b;
};
```

These are two different ways of using the `export` keyword, but both work the same.  
  
You might be wondering what that `default` keyword is that comes after `export`. We'll get to that in a minute. For now, let's actually use our `add` function in another file, now that we've exported it. 

## The import keyword

We can use the import keyword to import our add function into our `script.js` file. Importing this function just means we'll gain access to that function and be able to use it within the file. Once the function is imported, we can use it:

```js
// script.js
import add from './math.js';

console.log(add(2, 5)); //outputs 7
```

Here, with `./math.js`, we're using a relative import. To learn more about relative paths and absolute paths, check out this helpful [StackOverflow](https://stackoverflow.com/questions/21306512/difference-between-relative-path-and-absolute-path-in-javascript) answer.

When we run this code, we can see the result of calling our add function, `7`. Now you can use the add function as many times as you’d like within this file. 

The code for the add function itself is now out of sight, and we can use the add function without necessarily needing to look at the code for the function itself. 

If we commented out the line `import add from './math.js'` for a moment, we'd suddenly get an error: `ReferenceError: add is not defined`. This is because `script.js` does not have access to the add function unless we explicitly import that function into this file. 

We've exported our add function, imported it into our `script.js` file, and then called that function. 

Let’s look into our `math.js` file again. As mentioned earlier, you may have been confused when you saw the word `default` with the `export` keyword. Let's talk more about the `default` keyword. 

## Named exports versus default exports in JavaScript

With ES modules, you can use named exports or default exports.

In our first example, we used a **default export.** With a default export, we exported only a single value (our add function) from our `math.js` module. 

When using a default export, you can rename your import if you'd like to. In our `script.js` file, we can import our add function and call it addition (or any other name) instead:

```js
// script.js
import addition from './math.js';

console.log(addition(2, 5)); //outputs 7
```

On the other hand, **named exports** are used to export _multiple values_ from a module. 

Let's create an example using named exports. Back in our `math.js` file, create two more functions, subtract and multiply, and place them underneath our add function. With a named export, you can just remove the `default` keyword:

```js
// math.js

export default function add(a, b) {
 return a + b;
};

export function subtract(a, b) {
 return a - b;
};

export function multiply(a, b) {
 return a * b;
};
```

In `script.js`, let's remove all the previous code and import our subtract and multiply functions. To import the named exports, surround them in curly brackets:

```js
import { multiply, subtract } from './math.js';

```

Now we can use both of these functions inside of our `script.js` file:

```js
// script.js
import { multiply, subtract } from './math.js';

console.log(multiply(5, 5));

console.log(subtract(10, 4))
```

If you'd like to rename a named export, you can do so with the `as` keyword:

```js
import add, { subtract as substractNumbers } from './math.js';

console.log(substractNumbers(2, 5)); 
```

Above, we've renamed our `subtract` import to `subtractNumbers`.

Let's get back to our add function. What if we'd like to use it again in our `script.js` file, alongside our `multiply` and `subtract` functions? We can do so like this:

```js
import add, { multiply, subtract } from './math.js';

console.log(multiply(5, 5));

console.log(subtract(10, 4))

console.log(add(10, 10));
```

Now we've learned how to use ES modules. We've learned how to use the `export` keyword, the `import` keyword, and we've learned about the differences between named exports and default exports. And we've learned how to rename both our default exports and our named exports.  

<h1 id="other">Other module systems in JavaScript</h1>

When learning about modules, you may have seen or even used a different type of import, possibly one that looks like this:

```javascript
var models = require('./models')
```

This is where learning about modules in JavaScript can get confusing. Let's dive into a brief history of JavaScript modules to clear up the confusion.

The code example above using the `require` statement is CommonJS. CommonJS is another module system that can be used in JavaScript.   
  
When JavaScript was first created, it didn’t have a module system. Because JavaScript had no module system, developers created their own module systems on top of the language. 

Different module systems were created and used over the years, including CommonJS. When working in a codebase at a company or in an open source project, you might spot different module systems being used. 

Ultimately, ES modules were introduced as the standardized module system in JavaScript. 

In this article, we've learned about what modules are and why developers use them. We've learned about how ES modules work and the different kinds of module systems in JavaScript.

If you enjoyed this post, join my [coding club](https://madisonkanna.us14.list-manage.com/subscribe/post?u=323fd92759e9e0b8d4083d008&id=033dfeb98f), where we tackle coding challenges together every Sunday and support each other as we learn new technologies.

If you have feedback or questions on this post, or find me on Twitter [@madisonkanna](https://twitter.com/Madisonkanna).

  


  

