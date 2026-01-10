---
title: Learn these core JavaScript concepts in just a few minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-27T16:50:06.000Z'
originalURL: https://freecodecamp.org/news/learn-these-core-javascript-concepts-in-just-a-few-minutes-f7a16f42c1b0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*H-25KB7EbSHjv70HXrdl6w.png
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Dler Ari

  Sometimes, you just want to learn something quickly. And reading through comprehensive
  articles that describe specific JavaScript concepts may cause cognitive overload.
  The purpose of this article is to describe a few common concepts as s...'
---

By Dler Ari

Sometimes, you just want to learn something quickly. And reading through comprehensive articles that describe specific JavaScript concepts may cause cognitive overload. The purpose of this article is to describe a few common concepts as simply as possible with:

* A short description
* Why it is relevant
* A practical code example (ES5/ES6 with arrow functions).

It’s always a good idea to have general knowledge when working with the JS ecosystem. You’ll be aware of how things work and interact, and easily learn and improve things quicker.

These JS concepts are picked based on popularity and relevancy I’ve seen among the community. If you want to learn a concept that is not a part of this article, leave a comment and I will add it in the near future.

> If you want to become a better web developer, start your own business, teach others, or simply improve your development skills, I’ll be posting weekly tips and tricks on the latest web development languages.

_Boost your [JavaScript skills with these helpful JS methods](https://medium.freecodecamp.org/7-javascript-methods-that-will-boost-your-skills-in-less-than-8-minutes-4cc4c3dca03f)_.

#### The JS concepts we’ll be looking at:

1. Scope
2. IIFE
3. MVC
4. Async/await
5. Closure
6. Callback

### 1. Scope

**Scope is simply a box with boundaries.** There are two types of boundaries in JS: local and global, also referred to as inner and outer.

Local means that you have access to everything within the boundaries (inside the box), while global is everything outside the boundaries (outside the box).

These terms are used a lot when we talk about classes, functions, and methods. It provides the ability to determine what is a accessible (visible) to the current context.

#### **Why is this relevant?**

* Separates logic
* Narrows down the focus
* Improves readability

#### **Example**

Let’s assume you create a function and want to access a variable defined in global scope.

#### **ES5**

![Image](https://cdn-media-1.freecodecamp.org/images/FH-wWl6GjJqSkNku4tZBKaAGkFjDdwZhbICJ)
_JavaScript local/global scope_

#### ES6

![Image](https://cdn-media-1.freecodecamp.org/images/ismFUwaw2zTkQCszmFA7xTTzR7HLWZKYnBSk)
_JavaScript local/global scope (arrow functions)_

As shown in the example above, the function `showName()` has access to everything that is defined within its boundaries (locally), and also outside (globally). Remember, the global scope cannot access variables defined in local scope because it is enclosed from the outer world, except if you return it.

### 2. IIFE

**IIFE (Immediately Invoked Function Expression), as the name states means that the function is “Immediately Invoked” when it is created.** Before ES6++ presented classes/methods to support the object-oriented-programming paradigm (OOP), the common way was to mimic IIFE as a class name, and invoke functions as methods wrapped in a `return` type.

**Why is this relevant?**

* Immediately executes code
* Avoids global scope from getting polluted
* Supports asynchronous structure
* Improves readability (some may argue the opposite)

#### Example

Technology has changed quite a lot over the last few years. Now, for example, you have the ability to change the color of just about anything — like your car. Let’s see a code example.

#### **ES5**

![Image](https://cdn-media-1.freecodecamp.org/images/skU76x-Bf186aOzCFNC5ztWMrORzDeWragCa)
_JavaScript IIFE (Immediately Invoked Function Expression)_

#### **ES6**

![Image](https://cdn-media-1.freecodecamp.org/images/1mYlt8zccdCyawVfU2Wjyz9bIKkIY3b3L3sC)
_JavaScript IIFE (arrow functions)_

In the example above, we have wrapped two functions within the `return`type (`changeColorToRed()` & `changeColorToBlack()`). This allows us to access multiple functions, and invoke the method we want.

In short, we first invoke the `car` (function expression) in order to access what’s inside. Then we can use `.` notation to invoke the function that is defined within the `return` type. This approach is similar to the structure of having classes/methods where we first call the class name before we can call the method name. This way you can write clean, maintainable, and reusable code.

### 3. MVC

Model-view-controller is a design-framework (*not a programming language) that allows us to separate behavior into a practical real-world structure. Almost 85% of web-based applications today have this underlying pattern in one way or the other. There are other types of design frameworks out there, but this one is by far the most fundamental and easy-to-understand pattern.

#### Why is this relevant?

* Long-term scalability and maintainability
* Easy to improve, update, and debug (based on personal experience)
* Easy to setup
* Provides structure and overview

#### Example

Let’s look at a short example of the MVC design-framework.

#### ES5

![Image](https://cdn-media-1.freecodecamp.org/images/IYMt5aQAhY2zLTisweqQjuo6OIHcsjDmZyBf)
_Model-view-controller design-pattern_

#### ES6

![Image](https://cdn-media-1.freecodecamp.org/images/m-NV7R88VET9ZkFZrG5IP7kljkBocaP8Avz4)
_Model-view-controller design-pattern (arrow functions)_

As shown in the example above, we would usually divide the `view`, `model`, and `controller` in separate folders/files in terms of best practices, but just to illustrate the concept, we’ve put it all in one file. The objectives of the design-framework are to simplify the development process and support a sustainable collaborative environment.

### 4. Async/await

**Stop and wait until something is resolved.** It provides a way to maintain asynchronous processing in a more synchronous fashion. For instance, you need to check if a user’s password is correct (compare to what exists in the server) before allowing the user to enter the system. Or maybe you’ve performed a REST API request and you want the data to fully load before pushing it to the view.

#### Why is this relevant?

* Synchronous capabilities
* Controls the behavior
* Reduces “callback hell”

#### Example

Let’s assume you want to get all users from a [rest API](https://jsonplaceholder.typicode.com/) and show the results in JSON format.

#### ES5

![Image](https://cdn-media-1.freecodecamp.org/images/8UAkzKiRlj-iOuRldGvPHvgOKwzvCg0eH2qJ)
_Async and Await promises_

#### ES6

![Image](https://cdn-media-1.freecodecamp.org/images/nN3ogGjjsQWjI-Cg4P-33hxyVI0hT8zP1r1p)
_Async and Await promises (arrow functions)_

In order to use `await`, we must wrap it inside an `async` function to notify JS that we are working with promises. As shown in the example, we (a)wait for two things: `response` and `users`. Before we can convert the `response` to JSON format, we need to make sure we have the `response` fetched, otherwise we can end up converting a `response` that is not there yet, which will most likely prompt an error.

### 5. Closure

**A closure is simply a function inside another function.** It is used when you want to extend behavior such as pass variables, methods, or arrays from an outer function to inner function. We can also access the context defined in outer function from inner function, but not the other way around (remember the scope principles we talked about above).

#### **Why is this relevant?**

* Extends behavior
* Useful when working with events

#### **Example**

Let’s assume you work as a development engineer for Volvo, and they need a function that simply prints the name of the car.

#### ES5

![Image](https://cdn-media-1.freecodecamp.org/images/0IezBqbOGhYtOc69mqYc1s62a6iVlrjROYQh)
_JavaScript closure_

#### ES6

![Image](https://cdn-media-1.freecodecamp.org/images/u5gESTsVRAEEzcpzYBvYZs17HCrwjyYTkaZd)
_JavaScript closure (arrow functions)_

The function `showName()` is a Closure, because it extends the behavior of the function `showInfo()`, and also has access to the variable `carType`.

### 6. Callback

**A callback is a function that executes after another function has executed. It is also referred to as a call-after.** In the JavaScript world, a function that waits for another function to execute or return a value (array or object) is referred to as a callback. A callback is a way to make asynchronous operations more synchronous (sequential order).

#### **Why is this relevant?**

* Waits for an event to execute
* Provides synchronous capabilities
* Practical way to chain functionalities (If A is completed, then execute B, and so forth)
* Provides code structure and control
* Be aware, you may have heard about _callback hell._ It basically means that you have a recursive structure of callbacks (callbacks within callbacks within callbacks and so forth). [This is not practical](http://blog.mclain.ca/assets/images/callbackhell.png).

#### **Example**

Let’s say Elon Musk at SpaceX needs a functionality that will fire up Falcon Heavy’s 27 Merlin engines (the most powerful rocket in the world by a factor of two) when a button is pressed.

#### ES5

![Image](https://cdn-media-1.freecodecamp.org/images/by0SLg-QlbxG7OQ5CuiXGLxuZ9WXnfkLIsrB)
_JavaScript Callback_

#### ES6

![Image](https://cdn-media-1.freecodecamp.org/images/rPoRbhRgRbETZ5bKxo5tBJfVHehh784r5t99)
_JavaScript Callback (arrow functions)_

Notice that it waits for an event to occur (a button click) before performing an action (fire up the engines). In brief, we pass `fireUpEngines()` function as an argument (callback) to `pressButton()` function. When the user presses the button, it fires up the engines.

So there you have it! Some of the most popular JS concepts explained simply with examples. I hope these concepts have helped you understand JS a bit more and how it works.

You can find me on Medium where I publish on a weekly basis. Or you can follow me on [Twitter](http://twitter.com/dleroari), where I post relevant web development tips and tricks along with personal stories.

_P.S. If you enjoyed this article and want more like these, please clap ❤ and share with friends, it’s good karma_

