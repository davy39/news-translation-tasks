---
title: What is Prototypal Inheritance in JavaScript? Explained with Code Examples
subtitle: ''
author: Austin Asoluka
co_authors: []
series: null
date: '2024-05-31T08:10:16.000Z'
originalURL: https://freecodecamp.org/news/javascript-prototypal-inheritance
coverImage: https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-05-29-at-00.19.30.png
tags:
- name: inheritance
  slug: inheritance
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "Prototypal inheritance can feel like a complex concept shrouded in technical\
  \ jargon. But fear not! This guide will break it down using clear, relatable examples\
  \ that go beyond the typical textbook explanations. \nWe'll ditch the confusing\
  \ terms and fo..."
---

Prototypal inheritance can feel like a complex concept shrouded in technical jargon. But fear not! This guide will break it down using clear, relatable examples that go beyond the typical textbook explanations. 

We'll ditch the confusing terms and focus on real-world scenarios that you can easily understand.

By the end of this post, you'll be a prototypal inheritance pro, realizing that it wasn't that hard after all!

## Table of Contents

* [Concept Introduction](#heading-concept-introduction)
* [What are JavaScript Objects?](#heading-what-are-javascript-objects)
* [What is an Object Prototype?](#heading-what-is-an-object-prototype)
* [How to Work with .prototype Object of a Constructor](#heading-how-to-work-with-prototype-of-a-constructor)
* [How to Alter a Constructor's Prototype](#heading-how-to-alter-a-constructors-prototype)
* [The __proto__ Property](#heading-the-proto-property)
* [Summary](#heading-summary)

## Concept Introduction

Imagine that I'm a parent and I have a child and a grandchild. If you were to represent my family tree in a diagram, it should look like this:

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Screenshot-2024-05-09-at-23.12.29.png)
_**Fig 1**: Depicting the inheritance structure with family_

You can see that `grandparent` is at the top of this family tree, while the `parent` is a direct descendant of the `grandparent`, and the `child` is a descendant of `parent`.  
  
If you attempt to walk your way back up, you'll see that `grandchild` is a child of `parent` and its own parent is a `child` of `grandparent`.

## What are JavaScript Objects?

You may have come across this statement at some point: "In JavaScript, almost everything is an Object".

Notice how I spelt `Object`? When I use Object and object throughout this article, they will mean different things.

Object is a constructor used to create objects. That is: one is parent/ancestor and the other is child.

Using the illustration in **Fig 1.0** above, let's attempt to demonstrate how the family tree works in JavaScript.

 `Object` ⁠ is the grandparent.

Constructors like ⁠ `Array`, `String`, `Number`, `Function`, ⁠ and `⁠ Boolean` ⁠ are all descendants of ⁠ `Object`.

They all produce offspring of different types: `array`, `string`, `number`, `function`, and `Boolean`. However, if you trace back to their origin, they are all `Objects`.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Screenshot-2024-05-10-at-00.08.57.png)
_**Fig 2**: Object is at the top of the inheritance tree in JavaScript_

So if you're asked why everything (except `null` and `undefined`) are regarded as objects in JavaScript, it is because they are all descendants of the `Object` constructor.  
  
The constructors listed in the image above are responsible for the different data types you use in JavaScript. That is, they are used behind the scenes to create familiar data types (and you can also use them to create values of different types explicitly).

Let's try out some code snippets.

### How to Create an object

```js
// Using the regular object syntax
const newObj = {}

// Using the object constructor
const newObjWithConstructor = new Object()
```

### How to Create an array

```js
// Using the regular array syntax
const newArr = []

// Using the array constructor
const newArrWithConstructor = new Array()
```

### How to Create a number

```js
// Using the regular syntax
const num = 3

// Using the number constructor
const numWithConstructor = new Number(3)
```

### How to Create a function

```js
// Using regular function syntax
function logArg (arg) {
	console.log(arg)
}

// Using the Function constructor
const logArgWithConstructor = new Function('arg1', 'console.log(arg1)')
```

### How to Create a boolean

```js
// Using the regular boolean syntax
const isValid = true

// Using the Boolean constructor
const isValidWithConstructor = new Boolean(true)
```

You can see that from the example snippets above, it is possible to explicitly create values using the appropriate constructor, or just by using the simple syntax and allow JavaScript to create the value with the appropriate type for us.

**Note**: It is important to state that each method of creating values have their own use case and side effects but we won't be getting into that in this article.

The constructors of these various values have something called a prototype.

## What is an Object Prototype?

In JavaScript, there is something called `prototype`. The closest concept to this is the human DNA.

Just like DNA acts as blueprints that define characteristics that are passed on through generations of the human family tree, `prototypes` in JavaScript are used to define properties and methods that are inherited by objects down the JavaScript Object tree.

Let us combine **Fig 1** and **Fig 2** above, updating it now to accommodate the concept of DNA and prototype.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Screenshot-2024-05-10-at-01.01.47.png)
_Fig 3: Comparing JavaScript inheritance with the concept of inheritance in humans_

In JavaScript, all constructors have a prototype**.** The prototype of a constructor is a dictionary of everything that values created with the constructor should inherit.

Read the line above ☝️ again and proceed when it is clear.

Think of the constructor like a parent and the prototype like the DNA. When the constructor (parent) creates (gives birth to) an offspring (value), the offspring inherits from the DNA (prototype) of it's parent the constructor.

  
Let's consider another diagram:

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Screenshot-2024-05-10-at-01.28.05.png)
_Fig 4: Rough depiction of DNA Inheritance in human_

From **Fig 4**, you can see that a child inherits directly from their parent and their parent inherits traits from the grandparent. In this chain of inheritance, the child actually inherits from both the grandparent and the parent. 

In fact, the child's characteristics traits are strongly influenced by the combination of the DNA of every ancestor before itself.

This is how prototypal inheritance works in JavaScript.

The properties in the prototype of a constructor are inherited by the children created by that constructor. This continues down the chain. You can reason about it like this:

Every descendant in the inheritance chain, inherits everything available in the prototype of its ancestors.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Screenshot-2024-05-10-at-02.07.22.png)
_Fig 5: Prototypal inheritance chain_

From the diagram above, you can see that all other prototypes inherit from the Object prototype. Therefore, any value created with the Array constructor (for instance), will inherit from the Array prototype, and also, the Object prototype.

This is so because Array prototype inherits from Object prototype.

The term Array prototype is written as `Array.prototype` in JavaScript, while Object prototype is `Object.prototype`.

**Note**: It is important to note that the concept of DNA is complex so if stretched, we would quickly discover that there are some nuances and difference between how DNA and prototypes work but at the high level, they are very similar.

Therefore, an understanding of inheritance in human family tree would give us a strong understanding of prototypal inheritance in JavaScript.

If you learn better with videos, [watch this](https://www.youtube.com/watch?v=TzqJPmEkZ0o), before you continue.

## How to Work With `.prototype` of a Constructor

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Screenshot-2024-05-10-at-02.16.07.png)

To view the content of a constructor's prototype, we simply write `theConstructorName.prototype`. Foe example: `Array.prototype`, `Object.prototype`, `String.prototype` and so on.

Ever imagined how it is possible to write `[2, 8, 10].**map**(...)`? This is because, in the prototype of the Array constructor, there's a key called `map`. So even though you did not create the property `map` by yourself, it was inherited by the array value because that value was created by the `Array` constructor internally.

Read the above statement thus: Have you ever wondered why you have your specific blood type? It's because you get your blood type from the genes you inherited from your parents!

So the next time you make use of properties and methods like `.length`, `.map`, `.reduce`, `.valueOf`, `.find`, `.hasOwnProperty` on a value, just remember that they are all inherited from the constructor's prototype or some prototype up the prototype chain (the ancestry).

You can see the constructor prototype as the prototype of the entity used to construct/create/make a value.

You should be aware that the `.prototype` of every constructor is an object. The constructor itself is a function, but it's prototype is an object.

```js
console.log(typeof Array) // function
console.log(typeof Array.prototype) // object
```

**Note**: An exception to this is the prototype of the Function constructor. It is a function object, but it still has properties attached to it and those properties can be accessed like we would do with regular objects (using the `.` notation).

If you recall, we can add new properties to and retrieve values of already existing properties of objects by using the dot `.` notation. For example: `objectName.propertyName`

```js
const user = {
	name: "asoluka_tee",
    stack: ["Python", "JavaScript", "Node.js", "React", "MongoDB"],
    twitter_url: "https://twitter.com/asoluka_tee"
}

// Using the syntax objectName.propertyName, to access the name key we'll write; user.name 
const userName = user.name;
console.log(userName) // asoluka_tee

// To add a new property to the object we'd write;
user.eyeColor = "black"

// If we log the user object to the console now, we should see eyeColor as part of the object properties with the value of 'black'
```

  
Ever heard of DNA mutation? It's the idea of altering ones DNA. In JavaScript, this is possible with prototypes.

Just like DNA mutation is an extremely dangerous thing to try and the outcome could be uncertain or cause undesired side-effects, altering the prototype of a constructor is not a good idea unless you know what you are doing.

## How to Alter a Constructor's Prototype

In JavaScript, it is possible to alter the prototype object of a constructor just the same way you can with a regular JavaScript object (as shown above).  
  
This time, we just need to follow this syntax `constructorName.prototype.newPropertyName = value`. For example, if you want to add a new property named `currentDate` to the prototype object of the Array constructor, you'd write:

```js
//constructorName.prototype.newPropertyName
Array.prototype.currentDate = new Date().toDateString();
```

  
From now on, in your code, because `currentDate` now exists in the prototype of the `Array` constructor `(Array.prototype)`, every array created in our program can access it like this: `[1, 2, 3].currentDate` and the result will be today's date.   
  
If you want every object in your JavaScript program to have access to `currentDate`, you have to add it to the prototype object of the `Object` constructor `(Object.prototype)` instead:

```js
//constructorName.prototype.newPropertyName
Object.prototype.currentDate = new Date().toDateString();

const newArr = [1, 2, 3]
const newObj = {}
const newBool = true

// NB: The date shown is the date of writing this article
console.log(newArr.currentDate) // 'Fri May 10 2024'
console.log(newObj.currentDate) // 'Fri May 10 2024'
console.log(newBool.currentDate) // 'Fri May 10 2024'
```

This is possible because the prototype object of all constructors inherit from the prototype object of the `Object` constructor.  
  
Let's write our version of two popular array methods and use them just like we'd used the original.

1. **Array.prototype.reduce**: We'll call ours `.reduceV2`

```js
// Add our new function to the prototype object of the Array constructor
Array.prototype.reduceV2 = function (reducer, initialValue) {
  let accum = initialValue;
  for (let i = 0; i < this.length; i++) {
    accum = reducer(accum, this[i]);
  }
  return accum;
};

// Create an array of scores
let scores = [10, 20, 30, 40, 50];

// Use our own version of Array.prototype.reduce to sum the values of the array
const result = scores.reduceV2(function reducer(accum, curr) {
  return accum + curr;
}, 0);

// Log the result to the console
console.log(result);
```

The focus here is not to explain the whole syntax, it is to show you that by leveraging the prototype chain, you can create your own methods and use them just like the ones JavaScript provides.

Notice that you can just replace our `.reduceV2` with the original `.reduce` and it will still work (edge cases are not handled here).  
  
2. **Array.prototype.map**: We'll call ours `.mapV2` 

```js
// Add mapV2 method to the prototype object of the Array constructor
Array.prototype.mapV2 = function (func) {
  let newArray = [];
  this.forEach((item, index) => newArray.push(func(item, index)));
  return newArray;
};

// Create an array of scores 
const scores = [1, 2, 3, 4, 5];

// Use our mapV2 method to increment every item of the scores array by 2
const scoresTimesTwo = scores.mapV2(function (curr, index) {
	return curr * 2;
})

// Log the value of scoresTimesTwo to the console.
console.log(scoresTimesTwo)
```

**Note**: It is important to state that this is by no means a perfect implementation of the original versions of the `map` method of JavaScript. It is just an attempt to show you what's possible with a constructor's prototype object.

Before we round up this lesson, there's one more thing I need to mention; It is the `__proto__` property of every object.

## The __proto__ Property

`__proto__` is a setter and getter for [[prototype]] property of an object. This means that it is used to set or get the prototype of an object (for example, the object from which another object inherits from).

Consider this code snippet;

```js
const user = {}
const scores = []

user.prototype // undefined
scores.prototype // undefined
```

In the above snippet, we tried to access the prototype object directly from values. This is not possible in JavaScript. 

This makes sense because only constructors have the `prototype` property attached to them.

Just like DNA mutation is risky, it could be chaotic to mess with the prototype object if you do not absolutely know what you're doing.  
  
Under normal circumstances, a child should not try to alter the DNA of its ancestor or even determine who to inherit traits from 😉

The JavaScript language however provides a way for us to access the prototype object from values that are not constructors using the `__proto__` property.

This is a deprecated method and should not be used for new projects. I am mentioning `__proto__` because you could be employed to work in a codebase that still uses it.

`__proto__` allows a value to access the prototype object of it's constructor directly. So if for any reason you wish to see what is available in the prototype chain of a value's immediate ancestor, the `__proto__` property could be used for that.  
  
You can also use `__proto__` to determine which object a value should inherit from.

For instance, we have an object called `human`, and we want another object called `parent` to inherit from human, this can be done with the `__proto__` property of parent like this;

```js
// Create a human object
const human = {
    walk: function () { console.log('sleeping') },
    talk: function () { console.log('talking') },
	sleep: function () { console.log('sleeping') }
}

// Create a parent object and configure it to inherit from human.
const parent = {
    __proto__: human
}

// Use a method from the ancestor of parent
parent.sleep() // sleeping
```

Notice how we can call the `sleep` method on `parent` because `parent` now inherits from `human`.

There are more modern recommended methods to use when interacting with the prototype object like `Object.getPrototypeOf` and `Object.setPrototypeOf`

```js
const user = {}
const scores = []

// Get the prototype of the user object
console.log(Object.getPrototypeOf(user))

// Change the prototype of the scores array. This is like switching ancestry and should be done with great care.
console.log(Object.setPrototypeOf(scores, {}))

// Check the prototype of scores now
console.log(Object.getPrototypeOf(scores)) // {}
```

These methods should be used with great care. In fact, you should read more about them in the MDN JS docs to get more information on their pros and cons.

If you've read up to this point, you now know the fundamentals of `Array.prototype` and from now on, learning about any other concept built on top of this in JavaScript will be easier to understand.  
  
Let's summarize what you have learned so far.

## Summary

We have different constructors in JavaScript: `Array`, `Boolean`, `Function`, `Number`, `String`, and `Object`.   
  
Object is the parent of all the other constructors.

Each constructor has a `.prototype` object and this object contains properties and methods that could be accessed by values created using the constructor. For example, a value created using the `Array` constructor will have access to all the properties and methods available in the `Array.prototype` object and this inheritance goes all the way up.  
  
That is to say, a value created using the `Array` constructor (whether implicitly or explicitly), will not only have access to properties and methods in the `Array.prototype` object, but also properties and methods in the `Object.prototype` object.  
  
This is because of the concept of prototypal inheritance. `Object` is parent of `Array` and every child produced by `Array` will have access to traits from both `Array` and `Object`.

This is what happens when you try to get a property from a value which is not explicitly declared on the value. See code snippet below:

```js
const user = {}

// trying to retireve .valueOf property from the user object
console.log(user.valueOf)
```

Obviously the `user` object has no `.valueOf` property, so it looks up its prototype chain for any prototype which has that property and if it is found, the value is returned. Otherwise, we get `undefined`.

We also learned that we can alter the prototype of any constructor to add functionality and this should be done with caution.

Finally, we learned about how `__proto__`, `getPrototypeOf`, and `setPrototypeOf` could be used to retrieve and set the prototype of a value.

### How is This Useful? 

Imagine that you want to create a method which creates a new object based on an array and returns it when called on the array.  
  
This one's for you to try out yourself.

```js
// Array.prototype.toObject
const names = ['Austin', 'Tola', 'Joe', 'Victor'];

// Write your implementation of toObject here.

console.log(names.toObject()) // {0: 'Austin', 1: 'Tola', 2: 'Joe', 3: 'Victor'}
```

Hurray!!! I know you feel like a JavaScript ninja already.

If you learn better with videos, do subscribe to my [YouTube](https://www.youtube.com/@asoluka_tee) channel and I'd be releasing lecture videos soon.

Thanks for reading! Happy coding!

