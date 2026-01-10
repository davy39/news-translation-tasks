---
title: Let’s demystify JavaScript’s ‘new’ keyword
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-24T00:33:18.000Z'
originalURL: https://freecodecamp.org/news/demystifying-javascripts-new-keyword-874df126184c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*yF1csYj3s_p4lBZW8L0iCA.jpeg
tags:
- name: code
  slug: code
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Cynthia Lee

  Over the weekend, I completed Will Sentance’s JavaScript: The Hard Parts. It might
  not sound like the most glorious way to spend a weekend, but I actually found it
  pretty fun and relaxing to complete the course. It touched on functiona...'
---

By Cynthia Lee

Over the weekend, I completed Will Sentance’s [JavaScript: The Hard Parts](https://frontendmasters.com/courses/javascript-hard-parts/). It might not sound like the most glorious way to spend a weekend, but I actually found it pretty fun and relaxing to complete the course. It touched on functional programming, higher-order functions, closures, and asynchronous JavaScript.

For me, the highlight of the course was how he expanded on the JavaScript approaches to Object-Oriented Programming (OOP) and demystified the magic behind the **new** operator. I now have a well-rounded understanding of what goes on under the hood when the **new** operator is used.

### Object-Oriented Programming in **JavaScript**

![Image](https://cdn-media-1.freecodecamp.org/images/OjGA-narSWLOzyUTLWqTITXh4qD6KIcE36ag)
_Photo by [Unsplash](https://unsplash.com/@nickkarvounis?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Nick Karvounis</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Object-Oriented Programming (OOP) is a programming paradigm based on the concept of “objects.” Data and functions (attributes and methods) are bundled within an object.

An object in JavaScript is a collection of key-value pairs. These key-value pairs are properties of the object. A property can be an array, a function, an object itself or any primitive data type such as strings or integers.

What techniques do we have in our JavaScript toolbox for object creation?

Let’s assume that we are creating users in a game that we just designed. How would we store user details such as their names, points, and implement methods such as an increment in points? Here are two options for basic object creation.

#### **Option 1 — Object Literal Notation**

```js
let user1 = {
  name: "Taylor",
  points: 5,
  increment: function() {
    user1.points++;
  }
};
```

A JavaScript object literal is a list of name-value pairs wrapped in curly braces. In the example above, the object ‘user1’ is created, and the associated data is stored within it.

#### **Option 2 — Object.create()**

`Object.create(proto, [ propertiesObject ])`

`Object.create` methods accept two arguments:

1. proto: the object which should be the prototype of the newly-created object. It has to be an object or null.
2. propertiesObject: properties of the new object. This argument is optional.

Basically, you pass into `Object.create` an object that you want to inherit from, and it returns a new object that inherits from the object you passed into it.

```js
let user2 = Object.create(null);

user2.name = "Cam";
user2.points = 8;
user2.increment = function() {
  user2.points++;
}
```

The basic object creation options above are repetitive. It requires each one to be manually created.

How do we overcome this?

### Solutions

#### **Solution 1 — Generate objects using a function**

A simple solution is to write a function to create new users.

```js
function createUser(name, points) {
  let newUser = {};
  newUser.name = name;
  newUser.points = points;
  newUser.increment = function() {
    newUser.points++;
  };
  return newUser;
}
```

To create a user, you would now enter the information in parameters of the function.

```js
let user1 = createUser("Bob", 5);
user1.increment();
```

However, the increment function in the example above is just a copy of the original increment function. This is not a good way to write your code, as any potential changes to the function will need to be done manually for each object.

#### **Solution 2 — Use the prototypal nature of JavaScript**

Unlike object-oriented languages such as Python and Java, JavaScript does not have classes. It uses the concept of prototypes and prototype chaining for inheritance.

When you create a new array, you automatically have access to built-in methods such as `Array.join`, `Array.sort`, and `Array.filter`. This is due to the fact that array objects inherit properties from Array.prototype.

![Image](https://cdn-media-1.freecodecamp.org/images/CHrqNxf5I7tIo4-CfbSXqC6fnDd2H273ieWJ)
_Image credit: [JavaScript Prototype Chains, Scope Chains, and Performance ](https://www.toptal.com/javascript/javascript-prototypes-scopes-and-performance-what-you-need-to-know" rel="noopener" target="_blank" title=")by Diego Castorina_

Every JavaScript function has a prototype property, which is empty by default. You can add functions to this prototype property, and in this form, it is known as a method. When an inherited function is executed, the value of this points to the inheriting object.

```js
function createUser(name, points) {
  let newUser = Object.create(userFunction);
  newUser.name = name;
  newUser.points = points;
  return newUser;
}

let userFunction = {
  increment: function() {this.points++};
  login: function() {console.log("Please login.")};
}

let user1 = createUser("Bob", 5);
user1.increment();
```

When the `user1` object was created, a prototype chain bond with userFunction was formed.

When `user1.increment()` is in the call stack, the interpreter will look for user1 in the global memory. Next, it will look for the increment function, but will not find it. The interpreter will look at the next object up the prototype chain and will find the increment function there.

#### **Solution 3 — _new_ and _this_ keywords**

![Image](https://cdn-media-1.freecodecamp.org/images/OQKKYIojqDyXBnOwHdtZfxKL8YMOCii-2GTl)

The **new** operator is used to create an instance of an object which has a constructor function.

When we call the constructor function with new, we automate the following actions:

* A new object is created
* It binds `this` to the object
* The constructor function’s prototype object becomes the __proto__ property of the new object
* It returns the object from the function

This is fantastic, because the automation results in less repetitive code!

```js
function User(name, points) {
 this.name = name; 
 this.points = points;
}
User.prototype.increment = function(){
 this.points++;
}
User.prototype.login = function() {
 console.log(“Please login.”)
}

let user1 = new User(“Dylan”, 6);
user1.increment();
```

By using the prototype pattern, each method and property is added directly on the object’s prototype.

The interpreter will go up the prototypal chain and find the increment function under the prototype property of User, which itself is also an object with the information inside it. Remember — **All functions in JavaScript are also objects**. Now that the interpreter has found what it needs, it can create a new local execution context to run `user1.increment()`.

**Side note: Difference between __proto__ and prototype**

If you are already getting confused about __proto__ and prototype, don’t worry! You are far from the only one to be confused about this.

Prototype is a property of the constructor function that determines what will become the __proto__ property on the constructed object.

So, __proto__ is the reference created, and that reference is known as the prototype chain bond.

#### **Solution 4 — ES6 ‘syntactic sugar’**

![Image](https://cdn-media-1.freecodecamp.org/images/svX1DgD7SmEqaQLIchi26EuKUV4toaacQSJG)

Other languages allow us to write our shared methods within the object “constructor” itself. ECMAScript6 introduced the **class** keyword, which allows us to write classes that resemble normal classes of other classical languages. In reality, it is syntactic sugar over JavaScript’s prototypal behavior.

```js
class User {
  constructor(name, points) {
    this.name = name;
    this.points = points;
  }
  increment () {
    this.points++;
  }
  login () {
    console.log("Please login.")
  }
}

let user1 = new User("John", 12);
user1.increment();
```

In solution 3, the associated methods were precisely implemented using `User.prototype.functionName`. In this solution, the same results are achieved but the syntax looks cleaner.

### **Conclusion**

We have now learned more about the different options we have in JavaScript to create objects. While **class** declarations and the **new** operator are relatively easy to use, it is important to understand what is automated.

To recap, the following actions are automated when the constructor function is called with **new**_:_

* A new object is created
* It binds `this` to the object
* The constructor function’s prototype object becomes the __proto__ property of the new object
* It returns the object from the function

Thanks for reading my article, and clap if you liked it! Check out my other articles like [How I built my Pomodoro Clock app, and the lessons I learned along the way](https://medium.freecodecamp.org/how-i-built-my-pomodoro-clock-app-and-the-lessons-i-learned-along-the-way-51288983f5ee).

