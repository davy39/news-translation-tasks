---
title: How to build modern applications with WEBPACK
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-09T19:01:17.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-modern-applications-with-webpack-c81ccf6dd54f
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca69a740569d1a4ca716e.jpg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
- name: webpack
  slug: webpack
seo_title: null
seo_desc: 'By Samuel Omole

  How far can we get with Webpack’s default configuration?

  I had the privilege of speaking at GDG Devfest last month with a talk that was centered
  around using webpack in our modern day applications. You can check out the slides
  here.

  D...'
---

By Samuel Omole

How far can we get with Webpack’s default configuration?

I had the privilege of speaking at GDG Devfest last month with a talk that was centered around using webpack in our modern day applications. You can check out the slides [here](https://docs.google.com/presentation/d/1LcQYBh0VyM0iE_LuJS11wjJQeT45cApde9SdJQg9mVw/edit?usp=sharing).

Daily, I get to work as an Engineer and/or consultant with amazing and fast-paced teams, and webpack seems like the recurring factor throughout these teams (we use ReactJs for most of our applications). Initially, my talk was supposed to focus on using webpack with frontend frameworks/libraries like ReactJS, Vue, Angular etc.

Before submitting my proposal, I decided to run a mini survey to know what people thought about webpack. To my surprise, a lot of people labeled webpack as “Only used with frameworks” which was far from the truth. Still others said that “setting up webpack was daunting”. This led me to focus more on using webpack with Vanilla JS and seeing how far we could go with webpack’s default configuration.

But first:

### WHAT IS WEBPACK?

![Image](https://cdn-media-1.freecodecamp.org/images/M4slVGkwKmV0e8F2ODUCR-twvwi6foMoM0cD)

> _I personally define webpack as a tool that takes many Javascript modules and merges them into one Javascript module that can be sent off to the browser._

I know, it’s an oversimplification of what webpack does, but people seem to understand it. To explain more, webpack is a bundler that looks for Javascript modules with dependencies (basically, Javascript files that need code from other Javascript files), squashes them together, and then produces a Javascript file or files that have no dependencies. That way they can easily be shipped to the browser.

### History of Webpack

To understand the problems that webpack tries to solve, we need to know a little bit about the history of webpack itself. To keep this section very short, I’ve just outlined two important tools and one concept:

* [Google Web Toolkit](http://www.gwtproject.org/): This is a framework from Google that converts Java to Javascript (I know, right?). It has one feature that seems to be my personal favorite feature in webpack which is “code splitting”. (I will explain code splitting in a subsequent article.)
* [Modules_Webmake](https://github.com/medikoo/modules-webmake): This is the library that webpack originates from. It’s essentially a tool that allows us to organize our Javascript files for the browser the same way we do for NodeJS (awesome).
* IIFE: means immediately invoked function expression. This is basically a Javascript function that is called or invoked the same time as it was created.

#### Immediately Invoked Function Expression

I broke this into its own section because I had to explain further. This is an example of an IIFE:

![Image](https://cdn-media-1.freecodecamp.org/images/xwE0cAzV6-TF1c8Fc3Iqpdky6-LVVxKe7zyl)

If we were to place this function in our script tag, this would run immediately. The script tag is loaded by the browser. It’s kind of equivalent to attaching a function to `window.onload` but with an added advantage.

Because of the way closures work in Javascript, all the variables that were declared in the IIFE are scoped within that function. This means I wouldn’t have issues like namespace clashes in my codebase but at the same time, I still have access to the functions exposed by the IIFE.

### Why Webpack?

So, what are the problems we face today that webpack helps us solve?

First, we have the issue of script tags. I have worked on a codebase where each HTML page has at the very least 30 script tags arranged in a very precise order. I know some might say that isn’t really an issue, but the browser will have to make one request per file which can hurt your “time to load”. Also the script tags can get hard to manage, where rearranging just one could break the application (I tried that ?).

Second, we still have the issue of namespacing where the global namespace can get cluttered. I know we are very creative people especially when it comes to naming variables, but then when you work on a larger team there are times where the variable names just clash with each other. Or even your future self might think of the same name again (yeah it happens).

I know some organizations that make it habit for their developers to always keep their variables within the scope of their function, but we can’t always rely on that (or on `_this_`_)._ In the end, it just makes separation of concern difficult.

Third, remember I mentioned that webpack originated from modules_webmake. Because webpack allows us to organize our files the same way we do in NodeJS (using CommonJS), we have the added benefit of writing modular code which scales really well (just ask people that use frontend frameworks).

### CommonJS

![Image](https://cdn-media-1.freecodecamp.org/images/KjF9FAXBSSZNuiHgzhmjAReSYI1zlggAOPqO)

I won’t explain too much about CJS as this isn’t the point of the article. But you can say it’s a JS module system used in [NodeJS](https://nodejs.org/en/).

Webpack allows us to use this module and even the “better” ES module system in the browser without any issue (Webpack handles it in a smart way). This helps us write really modular and maintainable code where a JS file can handle a single functionality (Single Responsibility Principle).

### ES Modules (ESM)

![Image](https://cdn-media-1.freecodecamp.org/images/e48UD39h8gVqn49uUSrf1BkZ9dx6VkT86BAT)

This is another module system that, believe it or not, is already implemented by current browsers. But unfortunately, it has it’s limitations there. Webpack also allows us to use this module with no issue (as webpack still converts it in the end), but I found that using ESM makes most codebases I have worked on more readable. I would have loved to dive deeper into this but that isn’t the aim of this article. For a better explanation I would recommend this amazing [article](https://medium.com/webpack/the-state-of-javascript-modules-4636d1774358).

### How does Webpack work?

I know I said earlier that Webpack is magic but I lied. To put it as simply as possible:

* Webpack takes a path to a single entry point, which is a JS file, and looks for import statements (it could either be ESM or CJS).
* It then traverses the imported file, also looking for more import statements, while it creates a dependency graph in the process.

To explain better, take a look at the image:

![Image](https://cdn-media-1.freecodecamp.org/images/1RXjLCpnyfAVTfB1JRwvK6jNyZlBI1NgiK3e)
_J.K._

I have two files there, `index.js` and `helpers.js` These two files perform different functions, but I am importing and using the function in helpers.js in my index.js file. By default, Webpack’s entry point is `./src/index.js` and from there it tries to build the dependency graph as shown below:

![Image](https://cdn-media-1.freecodecamp.org/images/slsswDXppG0L7O5s5tEtG5oRnQGa8rx6-Tzx)

### How to get started

To get a better understanding of how webpack works, we are going to build a simple TODO app. It will have just the basic add and delete functionality and we are going to bundle it using Webpack’s default configuration (so no webpack config file). This is what the app will look like:

![Image](https://cdn-media-1.freecodecamp.org/images/XHRBMREv6mSxjWYIYhmKsBIEASYIJvxUfdd-)
_J.K._

The first step is to create a new project directory and create two folders, a folder named `dist` and another named `src` . By default, Webpack’s entry point is the path `./src/index.js` and it outputs the bundled JS into `./dist/main.js` — that’s why we are creating the two folders.

In the `dist` folder you can create the `index.html` file. This is not necessary for webpack as the file can be placed anywhere within the project directory and you can just make reference to the `main.js` file. In the end, your project structure should look like this:

![Image](https://cdn-media-1.freecodecamp.org/images/qz9bu3IEW6cV2awAF8GZ3qkwQ7VBch1hfRfa)

In the `src` folder we will create the `index.html` file where we will start the implementation of our TO-DO app’s functionalities. But first, let’s populate the `index.html` file. Since creating a TO-DO app isn’t part of this tutorial I will just show the code below:

```html
<html>
  <head>
    <title>Todo App</title>
  </head>
  <body>
    <div class="container">
      <p>
        <label for="new-task">Add Item</label>
        <input id="new-task" type="text">
        <button id="addTask">Add</button>
      </p>
      
      <h3>Todo</h3>
      <ul id="tasks">
      </ul>
    </div>
    <script src="main.js"></script>
  </body>
</html>
```

Let us now make it functional. We are going to break the two functions (Add and Delete) into their own files and then import them into `index.js` . We will create two files in our `src` folder named `addTask.js` and `deleteTask.js` . Your project structure should now look like this:

![Image](https://cdn-media-1.freecodecamp.org/images/bYBUgOjdT0BdNHZXrV1e2vB2odF9KHI4ROpd)

We can now start adding the necessary logic, so let’s implement the `deleteTask.js` first because it has no dependencies. Paste this in your `deleteTask.js` file:

```javascript
const deleteTask = function(e) {
  console.log("Delete Task...", e);
  //Remove the parent list item from the ul
  var listItem = e.target.parentNode;
  var ul = listItem.parentNode;
  ul.removeChild(listItem);
};


export default deleteTask;
```

All that is going on in that file is we are creating the `deleteTask` function and then exporting it as a default export.

We can now implement the `addTask` function. In the `addTask.js` file add the following code:

```javascript
import deleteTask from "./deleteTask";


const createNewTaskElement = function(taskString) {

  const listItem = document.createElement("li");
  const label = document.createElement("label");
  const deleteButton = document.createElement("button");
deleteButton.innerText = "Delete";
  deleteButton.className = "delete";
  deleteButton.addEventListener("click", deleteTask);

	label.innerText = taskString;
	listItem.appendChild(label);
  	listItem.appendChild(deleteButton);
	return listItem;
};


const addTask = function(e) {
  const taskList = document.getElementById("tasks");
  const task = document.getElementById("new-task");
  if (task.value !== "") {
    const newTaskItem = createNewTaskElement(task.value);
    taskList.appendChild(newTaskItem);
    task.value = "";
  }
};


export default addTask;
```

In this one, we first of all import the `deleteTask.js` file. By default, if no extension is specified in the import, webpack automatically assumes that it’s a `.js` file. Then we have the function that creates the list item containing the task that was entered in the form. The only thing to note is that we are attaching the delete function to the click handler of the delete button. Then we create the actual addTask function and export it.

We will then need to import our `addTask` function into `index.js` . Paste the code below into your `index.js` file:

```javascript
import addTask from './addTask';

const addTaskButton = document.getElementById("addTask");

addTaskButton.addEventListener("click", addTask);
```

This is pretty straightforward: we are importing the `addTask` function and attaching it to the click handler for the `addTaskButton` . If you followed the steps above you should be good to go.

Finally, to get our `main.js` file we need to run Webpack through our codebase. For this step, make sure you have [NodeJS](https://nodejs.org/en/) installed on your system, then we will install webpack globally using this command:

```
npm install -g webpack OR sudo npm install -g webpack
```

Once it’s done installing run the following command:

```
webpack
```

It will bundle up our file successfully but we should see a warning in the terminal like this:

![Image](https://cdn-media-1.freecodecamp.org/images/zDIK8WvPOHW1207f33J-wEZ-hY7IHDIlif1W)

Webpack is just warning us that we didn’t specify a [mode](https://webpack.js.org/concepts/#mode). We could leave it as is and run the code, everything should work fine. But if you don’t like the warning then you can run Webpack like this:

```
webpack --mode=development
```

And you’re good to go.

### Wrapping up

If you got lost along the way you can always use the GitHub [repo](https://github.com/samie820/todo) for reference (It has some CSS styling in it, though).

I hope this article was able to show you what Webpack has to offer (just the basics, with no configuration whatsoever). In subsequent articles, I will try to show how to set up various custom configurations for features like [code splitting](https://webpack.js.org/guides/code-splitting/), [lazy loading](https://webpack.js.org/guides/lazy-loading/) and configuring Webpack to work with multi-page applications.

In order to keep this article as basic as possible, I avoided the use of a `package.json` file in the article. The use of a `package.json` file and installing webpack locally is the most scalable way of using webpack and I will go into it in my next article on using Webpack.

To help navigate the coming articles, it will really help if you can drop a comment of what you would like to see explained or implemented regarding Webpack. ??

_I will like to especially thank [Sean T. Larkin](https://www.freecodecamp.org/news/how-to-build-modern-applications-with-webpack-c81ccf6dd54f/undefined), [Israel Obiagba](https://www.freecodecamp.org/news/how-to-build-modern-applications-with-webpack-c81ccf6dd54f/undefined) and [Hassan Sani](https://www.freecodecamp.org/news/how-to-build-modern-applications-with-webpack-c81ccf6dd54f/undefined) for their feedback in making the article better than initially planned. You all rock!_

