---
title: How to create objects in JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-28T07:58:05.000Z'
originalURL: https://freecodecamp.org/news/a-complete-guide-to-creating-objects-in-javascript-b0e2450655e8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*S6zT7E9uySUcbD69OPQR8A.jpeg
tags:
- name: education
  slug: education
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Kaashan Hussain

  We all deal with objects in one way or another while writing code in a programming
  language. In JavaScript, objects provide a way for us to store, manipulate, and
  send data over the network.

  There are many ways in which objects in ...'
---

By Kaashan Hussain

We all deal with objects in one way or another while writing code in a programming language. In JavaScript, objects provide a way for us to store, manipulate, and send data over the network.

There are many ways in which objects in JavaScript differ from objects in other mainstream programming languages, like Java. I will try to cover that in a another topic. Here, let us only focus on the various ways in which JavaScript allows us to create objects.

In JavaScript, think of objects as a collection of ‘key:value’ pairs. This brings to us the first and most popular way we create objects in JavaScript.

Let’s get this started.

#### 1. Creating objects using object literal syntax

This is really simple. All you have to do is throw your key value pairs separated by ‘:’ inside a set of curly braces({ }) and your object is ready to be served (or consumed), like below:

```js
const person = {
  firstName: 'testFirstName',
  lastName: 'testLastName'
};
```

This is the simplest and most popular way to create objects in JavaScript.

#### 2. Creating objects using the ‘new’ keyword

This method of object creation resembles the way objects are created in class-based languages, like Java. By the way, starting with ES6, classes are native to JavaScript as well and we will look at creating objects by defining classes towards the end of this article. So, to create an object using the ‘new’ keyword, you need to have a constructor function.

Here are 2 ways you can use the ‘new’ keyword pattern —

**a) Using the ‘new’ keyword with’ in-built Object constructor function**

To create an object, use the new keyword with `Object()` constructor, like this:

```js
const person = new Object();
```

Now, to add properties to this object, we have to do something like this:

```js
person.firstName = 'testFirstName';
person.lastName = 'testLastName';
```

You might have figured that this method is a bit longer to type. Also, this practice is not recommended as there is a scope resolution that happens behind the scenes to find if the constructor function is built-in or user-defined.

**b) Using ‘new’ with user defined constructor function**

The other problem with the approach of using the ‘Object’ constructor function result from the fact that every time we create an object, we have to manually add the properties to the created object.

What if we had to create hundreds of person objects? You can imagine the pain now. So, to get rid of manually adding properties to the objects, we create custom (or user-defined) functions. We first create a constructor function and then use the ‘new’ keyword to get objects:

```js
function Person(fname, lname) {
  this.firstName = fname;
  this.lastName = lname;
}
```

Now, anytime you want a ‘Person’ object, just do this:

```js
const personOne = new Person('testFirstNameOne', 'testLastNameOne');
const personTwo = new Person('testFirstNameTwo', 'testLastNameTwo');
```

#### 3. Using Object.create() to create new objects

This pattern comes in very handy when we are asked to create objects from other existing objects and not directly using the ‘new’ keyword syntax. Let’s see how to use this pattern. As stated on [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/create):

> The `**Object.create()**` method creates a new object, using an existing object as the prototype of the newly created object.

To understand the `**Object.create**` method, just remember that it takes two parameters. The first parameter is a mandatory object that serves as the prototype of the new object to be created. The second parameter is an optional object which contains the properties to be added to the new object.

We will not deep dive into prototypes and inheritance chains now to keep our focus on the topic. But as a quick point, you can think of prototypes as objects from which other objects can borrow properties/methods they need.

Imagine you have an organization represented by `orgObject`

```
const orgObject = { company: 'ABC Corp' };
```

And you want to create employees for this organization. Clearly, you want all the employee objects.

```js
const employee = Object.create(orgObject, { name: { value: 'EmployeeOne' } });

console.log(employee); // { company: "ABC Corp" }
console.log(employee.name); // "EmployeeOne"
```

#### 4. Using Object.assign() to create new objects

What if we want to create an object that needs to have properties from more than one object? `Object.assign()` comes to our help.

As stated on [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign):

> The `Object**.**assign**()**` method is used to copy the values of all enumerable own properties from one or more source objects to a target object. It will return the target object.

`Object**_._**assign` method can take any number of objects as parameters. The first parameter is the object that it will create and return. The rest of the objects passed to it will be used to copy the properties into the new object. Let’s understand it by extending the previous example we saw.

Assume you have two objects as below:

```js
const orgObject = { company: 'ABC Corp' }
const carObject = { carName: 'Ford' }
```

Now, you want an employee object of ‘ABC Corp’ who drives a ‘Ford’ car. You can do that with the help of `Object.assign` as below:

`const employee = Object.assign({}, orgObject, carObject);`

Now, you get an `employee` object that has `company` and `carName` as its property.

```js
console.log(employee); // { carName: "Ford", company: "ABC Corp" }
```

#### 5. Using ES6 classes to create objects

You will notice that this method is similar to using ‘new’ with user defined constructor function. The constructor functions are now replaced by classes as they are supported through ES6 specifications. Let’s see the code now.

```js
class Person {
  constructor(fname, lname) {
    this.firstName = fname;
    this.lastName = lname;
  }
}

const person = new Person('testFirstName', 'testLastName');

console.log(person.firstName); // testFirstName
console.log(person.lastName); // testLastName


```

These are all the ways I know to create objects in JavaScript. I hope you enjoyed this post and now understand how to create objects.

_Thanks for your time for reading this article. If you liked this post and it was helpful to you, please click the clap ? button to show your support. Keep learning more!_

