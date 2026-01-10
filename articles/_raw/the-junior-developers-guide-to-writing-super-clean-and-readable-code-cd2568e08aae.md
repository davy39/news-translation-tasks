---
title: The junior developer’s guide to writing super clean and readable code
subtitle: ''
author: Chris Blakely
co_authors: []
series: null
date: '2019-03-28T20:06:23.000Z'
originalURL: https://freecodecamp.org/news/the-junior-developers-guide-to-writing-super-clean-and-readable-code-cd2568e08aae
coverImage: https://cdn-media-1.freecodecamp.org/images/1*BbAtAVDs9srxs33lkY9sbw.jpeg
tags:
- name: clean code
  slug: clean-code
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: null
seo_desc: 'Writing code is one thing, but writing clean, readable code is another
  thing. But what is “clean code?” I’ve created this short clean code for beginners
  guide to help you on your way to mastering and understanding the art of clean code.

  Imagine you a...'
---

Writing code is one thing, but writing clean, readable code is another thing. But what is “clean code?” I’ve created this short _clean code for beginners guide_ to help you on your way to mastering and understanding the art of clean code.

Imagine you are reading an article. There’s an opening paragraph, which gives you a brief overview of what the article is about. There are headings, each with a bunch of paragraphs. The paragraphs are structured with the relevant bits of information grouped together and ordered so that the article “flows” and reads nicely.

Now, image the article didn’t have any headings. There are paragraphs, but they are long and in a confusing order. You can’t skim read the article, and have to really dive into the content to get a feel for what the article is about. This can be quite frustrating!

Your code should read like a good article. Think of your classes/files as headings, and your methods as paragraphs. Sentences are the statements in your code. Here are some of the characteristics of clean code:

1. Clean code is focused — Each function, each class, and module should do one thing and do it well.
2. It should be elegant — Clean code should be _simple_ to read. Reading it should make you smile. It should leave you thinking “I know exactly what this code is doing”
3. Clean code is taken care of. Someone has taken the time to keep it simple and orderly. They have paid appropriate attention to details. They have cared.
4. The tests should pass — Broken code isn’t clean!

On to the big question of the day — how do you actually write clean code as a junior developer? Here’s my top tips to get started.

### Use consistent formatting & indentation

Books would be hard to read if the line spacing was inconsistent, the font sizes were different, and the line breaks were all over the place. The same goes for your code.

To make your code clear and easy to read, make sure the indentation, line breaks, and formatting are consistent. Here’s a good and bad example:

#### The Good

```js
function getStudents(id) { 
     if (id !== null) { 
        go_and_get_the_student(); 
     } else { 
        abort_mission(); 
     } 
}
```

* At a glance, you can tell there is an `if/else` statement within the function
* Braces and consistent indentation make it easy to see where the code blocks start and end
* Braces are consistent — Notice how the opening brace for the `function` and for the `if` are on the same line

#### The Bad

```js
function getStudents(id) {
if (id !== null) {
go_and_get_the_student();} 
    else 
    {
        abort_mission();
    }
    }
```

Woah! So much wrong here.

* The indentation is all over the place — you can’t tell where the function ends, or where the `if/else` block starts (yes there is an if/else block in there!)
* The braces are confusing and are not consistent
* The line spacing is inconsistent

This is a bit of an exaggerated example, but it shows the benefit of using consistent indentation and formatting. I don’t know about you, but the “good” example was much easier on the eyes for me!

The good news is that there are many IDE plugins you can use to automatically format code for you. Hallelujah!

* VS Code: [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)
* Atom: [Atom Beautify](https://atom.io/packages/atom-beautify)
* Sublime Text: [Prettify](https://packagecontrol.io/packages/HTML-CSS-JS%20Prettify)

### Use clear variable and method names

In the beginning, I talked about how it’s important that your code is easy to read. A big aspect of this is the naming you choose (this is one of the [mistakes I made when I was a junior developer](https://www.chrisblakely.dev/7-mistakes-i-made-as-a-junior-developer/)). Let’s look at an example of good naming:

```
function changeStudentLabelText(studentId){                  
     const studentNameLabel = getStudentName(studentId); 
}
function getStudentName(studentId){ 
     const student = api.getStudentById(studentId); 
     return student.name; 
}
```

This code snippet is good for a number of ways:

* The functions are named clearly with well-named arguments. When a developer is reading this, it’s clear in their mind, “If I call the `getStudentName()` method with a `studentId`, I will get a student name back" - they don't have to navigate to the `getStudentName()` method if they don't need to!
* Within the `getStudentName()` method, the variables and method calls are again clearly named - it's easy to see that the method calls an `api`, get's a `student` object, and returns the `name` property. Easy!

Choosing good names when writing clean code for beginners is harder than you think. As your app grows, use these conventions to ensure your code is easy to read:

* Choose a naming style and be consistent. Either `camelCase` or `under_scores` but not both!
* Name your function, methods, and variables by what that thing does, or what that thing is. If your method _get’s_ something, put `get` in the name. If your variable _stores_ a color of a car, call it `carColour`, for example.

**BONUS TIP** — if you can’t name your function or method, then that function is doing too much. Go ahead and break it up into smaller functions! E.g if you end up calling your function `updateCarAndSave()`, create 2 methods `updateCar()` and `saveCar()`.

### Use comments where necessary

There is a saying, “code should be self-documenting”, which basically means, instead of using comments, your code should read well enough reducing the need for comments. This is a valid point, and I guess this makes sense in a perfect world. Yet, the world of coding is far from perfect, so sometimes comments are necessary.

Documentation comments are comments that describe what a particular function or class does. If you’re writing a library, this will be helpful for developers who are using your library. Here’s an example from useJSDoc:

```js
/** * Solves equations of the form a * x = b 
* @example * 
// returns 2 * globalNS.method1(5, 10); 
* @example * 
// returns 3 * globalNS.method(5, 15); 
* @returns {Number} Returns the value of x for the equation. */ globalNS.method1 = function (a, b) { return b / a; };
```

Clarification comments are intended for anyone (including your future self) who may need to maintain, refactor, or extend your code. More often than not, clarification comments could be avoided, in favor of “self-documenting code”. Here’s an example of a clarification comment:

```js
/* This function calls a third party API. Due to some issue with the API vender, the response returns "BAD REQUEST" at times. If it does, we need to retry */ 
function getImageLinks(){ 
     const imageLinks = makeApiCall(); 
     if(imageLinks === null){ 
        retryApiCall(); 
     } else { 
        doSomeOtherStuff(); 
     } 
}
```

Here’s some comments you should try and avoid. They don’t offer much value, can be misleading and simply clutter the code.

Redundant comments that don’t add value:

```js
// this sets the students age 
function setStudentAge();
```

Misleading comments:

```js
//this sets the fullname of the student 
function setLastName();
```

Funny or insulting comments:

```js
// this method is 5000 lines long but it's impossible to refactor so don't try 
function reallyLongFunction();
```

### Remember the DRY principle (Don’t Repeat Yourself)

The DRY principle is stated as:

> “Every piece of knowledge must have a single, unambiguous, authoritative representation within a system.”

At its simplest level, this basically means that you should aim to reduce the amount of duplicated code that exists. (Note that I said “_reduce”_ and not _“eliminate” —_ There are some instances where duplicated code isn’t the end of the world!)

Duplicated code can be a nightmare to maintain and alter. Let’s look at an example:

```js
function addEmployee(){ 
    // create the user object and give the role
    const user = {
        firstName: 'Rory',
        lastName: 'Millar',
        role: 'Admin'
    }
    
    // add the new user to the database - and log out the response or error
    axios.post('/user', user)
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
}

function addManager(){  
    // create the user object and give the role
    const user = {
        firstName: 'James',
        lastName: 'Marley',
        role: 'Admin'
    }
    // add the new user to the database - and log out the response or error
    axios.post('/user', user)
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
}

function addAdmin(){    
    // create the user object and give the role
    const user = {
        firstName: 'Gary',
        lastName: 'Judge',
        role: 'Admin'
    }
    
    // add the new user to the database - and log out the response or error
    axios.post('/user', user)
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
}
```

Imagine you are creating a human resources web app for a client. This app allows admins to add users with roles to a database via an API. There are 3 roles; employee, manager, and admin. Let’s look at some of the functions that might exist:

Cool! The code works and all is well in the world. After a while, our client comes along and says:

> _Hey! We would like the error message that is displayed to contain the sentence “there was an error”. Also, to be extra annoying, we want to change the API endpoint from `/user` to `/users`. Thanks!_

So before we jump in and start coding, let’s step back. Remember at the beginning of this clean code for beginners article, when I said _“Clean code should be focused”._ i.e, do one thing and do it well? This is where our current code has a small issue. The code that makes the API call and handles the error is repeated — which means we have to change the code in 3 places to meet the new requirements. Annoying!

So, what if we refactored this to _be more focused_? Have a look at the following:

```js
function addEmployee(){ 
    // create the user object and give the role
    const user = {
        firstName: 'Rory',
        lastName: 'Millar',
        role: 'Admin'
    }
    
    // add the new user to the database - and log out the response or error
    saveUserToDatabase(user);
}

function addManager(){  
    // create the user object and give the role
    const user = {
        firstName: 'James',
        lastName: 'Marley',
        role: 'Admin'
    }
    // add the new user to the database - and log out the response or error
    saveUserToDatabase(user);
}

function addAdmin(){    
    // create the user object and give the role
    const user = {
        firstName: 'Gary',
        lastName: 'Judge',
        role: 'Admin'
    }
    
    // add the new user to the database - and log out the response or error
    saveUserToDatabase(user);
}

function saveUserToDatabase(user){
    axios.post('/users', user)
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log("there was an error " + error);
  });
}
```

We’ve moved the logic that creates an API call into its own method `saveUserToDatabase(user)` (is that a good name? You decide!) which the other methods _will call_ to save the user. Now, if we need to change the API logic again, we only have to update 1 method. Likewise, if we have to add another method that creates users, the method to save the user to the database via api already exists. Hurray!

### An example of refactoring using what we learned so far

Let’s close our eyes and pretend really hard that we’re making a calculator app. There are functions that are used which allows us to add, subtract, multiply and divide respectively. The result is outputted to the console.

Here’s what we have so far. See if you can spot the issues before moving on:

```js
function addNumbers(number1, number2)
{
    const result = number1 + number2;
        const output = 'The result is ' + result;
        console.log(output);
}

// this function substracts 2 numbers
function substractNumbers(number1, number2){
    
    //store the result in a variable called result
    const result = number1 - number2;
    const output = 'The result is ' + result;
    console.log(output);
}

function doStuffWithNumbers(number1, number2){
    const result = number1 * number2;
    const output = 'The result is ' + result;
    console.log(output);
}

function divideNumbers(x, y){
    const result = number1 / number2;
    const output = 'The result is ' + result;
    console.log(output);
}
```

What are the issues?

* The indentation is inconsistent — it doesn’t matter too much what indentation format we use, just as long as it’s consistent
* The 2nd function has some redundant comments — we can tell what’s going on by reading the function name and the code within the function, so do we really need a comment here?
* The 3rd and 4th functions don’t use good naming — `doStuffWithNumbers()` isn't the best function name as it doesn't state what it does. `(x, y)` aren't descriptive variables either - are `x & y` functions? numbers? bananas?
* The methods _do more than one thing —_ performs the calculation, but also displays the output. We can split the _display_ logic out to a separate method — as per the **DRY principle**

Now we’ll use what we learned in this clean code for beginners guide to refactor everything so that our new code looks like:

```js
function addNumbers(number1, number2){
	const result = number1 + number2;
	displayOutput(result)
}

function substractNumbers(number1, number2){
	const result = number1 - number2;
	displayOutput(result)
}

function multiplyNumbers(number1, number2){
	const result = number1 * number2;
	displayOutput(result)
}

function divideNumbers(number1, number2){
	const result = number1 * number2;
	displayOutput(result)
}

function displayOutput(result){
	const output = 'The result is ' + result;
	console.log(output);
}
```

* We’ve fixed the indentation so that it's consistent
* Adjusted the naming of the functions and variables
* Removed the unneeded comments
* Moved the `displayOutput()` logic into its own method - if the output needs to change, we only need to change it one place

Congrats! You can now talk about how you know clean code principles in your interviews and when [writing your killer resume](https://www.chrisblakely.dev/how-to-write-an-awesome-junior-developer-resume-in-a-few-simple-steps/)!

### Don’t “over clean” your code

I often see developers go over the top when it comes to clean code. Be careful not to try and clean your code too much, as it can have the opposite effect, and actually make your code _harder to read and maintain._ It can also have an impact on productivity, if a developer has to constantly jump between many files/methods in order to make a simple change.

Be mindful of clean code, but do not overthink it at the early stages of your projects. Make sure your code works, and is well tested. During the refactoring stage is when you should really think about how to clean up your code using the DRY principle etc.

In this clean code for beginners guide, we learned how to:

* Use consistent formatting & indentation
* Use clear variable and method names
* Use comments where necessary
* Use the DRY principle (Don’t Repeat Yourself)

If you enjoyed this guide, make sure to check out [_Clean Code: A Handbook of Agile Software Craftsmanship_ by Robert C Martin](https://amzn.to/2U7JO4N). If you are serious about writing clean code and breaking out of the junior developer level, I highly recommend this book.

Thanks for reading!

To get the latest guides and courses for junior developers straight to your inbox, make sure to join the mailing list at [www.chrisblakely.dev](https://www.chrisblakely.dev/#sign-up)!

