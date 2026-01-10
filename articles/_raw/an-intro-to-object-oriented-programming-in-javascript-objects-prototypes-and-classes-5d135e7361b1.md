---
title: 'An intro to object-oriented programming in JavaScript: objects, prototypes,
  and classes'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-28T16:31:35.000Z'
originalURL: https://freecodecamp.org/news/an-intro-to-object-oriented-programming-in-javascript-objects-prototypes-and-classes-5d135e7361b1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*zGuG4nFo8O4e0WMoNWVbMA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: object oriented
  slug: object-oriented
- name: General Programming
  slug: programming
- name: prototype
  slug: prototype
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Andrea Koutifaris

  In many programming languages, classes are a well-defined concept. In JavaScript
  that is not the case. Or at least that wasn’t the case. If you search for O.O.P.
  and JavaScript you will run into many articles with a lot of differ...'
---

By Andrea Koutifaris

In many programming languages, classes are a well-defined concept. In JavaScript that is not the case. Or at least that wasn’t the case. If you search for O.O.P. and JavaScript you will run into many articles with a lot of different recipes on how you can emulate a `class` in JavaScript.

Is there a simple, K.I.S.S. way to define a class in JavaScript? And if so, why so many different recipes to define a class?

Before answering to those questions, let’s understand better what a JavaScript `Object` is.

### **Objects in JavaScript**

Let’s begin with a very simple example:

```js
const a = {};
a.foo = 'bar';
```

In the above code snippet an object is created and enhanced with a property `foo`. The possibility of adding things to an existing object is what makes JavaScript different from classic languages like Java.

More in detail, the fact that an object can be enhanced makes it possible to create an instance of an “implicit” class without the need to actually create the class. Let’s clarify this concept with an example:

```js
function distance(p1, p2) {
  return Math.sqrt(
    (p1.x - p2.x) ** 2 + 
    (p1.y - p2.y) ** 2
  );
}

distance({x:1,y:1},{x:2,y:2});
```

In the example above, I didn’t need a Point class to create a point, I just extended an instance of `Object` adding `x` and `y` properties. The function distance doesn’t care if the arguments are an instance of the class `Point` or not. Until you call `distance` function with two objects that have an `x` and `y` property of type `Number`, it will work just fine. This concept is sometimes called _duck typing_.

Up to now, I’ve only used a data object: an object containing only data and no functions. But in JavaScript it is possible to add functions to an object:

```js
const point1 = {
  x: 1,
  y: 1,
  toString() {
    return `(${this.x},${this.y})`;
  }
};

const point2 = {
  x: 2,
  y: 2,
  toString() {
    return `(${this.x},${this.y})`;
  }
};
```

This time, the objects representing a 2D point have a `toString()` method. In the example above, the `toString` code has been duplicated, and this is not good.

There are many ways to avoid that duplication, and, in fact, in different articles about objects and classes in JS you will find different solutions. Have you ever heard of the “Revealing module pattern”? It contains the words “pattern” and “revealing”, sounds cool, and “module” is a must. So it must be the right way to create objects… except that it isn’t. Revealing module pattern can be the right choice in some cases, but it is definitely not the default way of creating objects with behaviors.

We are now ready to introduce classes.

### **Classes in JavaScript**

What is a class? From a dictionary: a class is “a set or category of things having some property or attribute in common and differentiated from others by kind, type, or quality.”

In programming languages we often say “An object is an instance of a class”. This means that, using a class, I can create many objects and they all share methods and properties.

Since objects can be enhanced, as we’ve seen earlier, there are may ways to create objects sharing methods and properties. But we want the simplest one.

Fortunately ECMAScript 6 provides the keyword `class`, making it very easy to create a class:

```js
class Point {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }

  toString() {
    return `(${this.x},${this.y})`;
  }
}
```

So, in my opinion, that is the best way of declaring classes in JavaScript. Classes are often related to inheritance:

```js
class Point extends HasXY {
  constructor(x, y) {
    super(x, y);
  }

  toString() {
    return `(${this.x},${this.y})`;
  }
}
```

As you can see in the example above, to extend another class it is enough to use the keyword `extends` .

You can create an object from a class using the `new` operator:

```js
const p = new Point(1,1);
console.log(p instanceof Point); // prints true
```

A good object oriented way of defining classes should provide:

* a simple syntax to declare a class
* a simple way to access to the current instance, a.k.a. `this`
* a simple syntax to extend a class
* a simple way to access the super class instance, a.k.a. `super`
* possibly, a simple way of telling if an object is an instance of a particular class. `obj instanceof AClass` should return `true` if that object is an instance of that class.

The new `class` syntax provides all the points above.

Before the introduction of the `class` keyword, what was the way to define a class in JavaScript?

In addition, what really is a class in JavaScript? Why do we often speak about _prototypes_?

### **Classes in JavaScript 5**

From [Mozilla MDN page about classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes):

> JavaScript classes, introduced in ECMAScript 2015, are primarily syntactical sugar over JavaScript’s existing **prototype-based inheritance**. The class syntax does not introduce a new object-oriented inheritance model to JavaScript.

The key concept here is **prototype-based inheritance**. Since there is a lot of misunderstanding on what that kind of inheritance is, I will proceed step by step, moving from `class` keyword to `function` keyword.

```js
class Shape {}
console.log(typeof Shape);
// prints function
```

It seems that `class` and `function` are related. Is `class` just an alias for `function` ? No, it isn’t.

```js
Shape(2);
// Uncaught TypeError: Class constructor Shape cannot be invoked without 'new'
```

So, it seems that the people who introduced `class` keyword wanted to tell us that a class is a function that must be called using the `new` operator.

```js
var Shape = function Shape() {} // Or just function Shape(){}
var aShape = new Shape();
console.log(aShape instanceof Shape);
// prints true
```

The example above shows that we can use `function` to declare a class. We cannot, however, force the user to call the function using the `new` operator. It is possible to throw an exception if the `new` operator wasn’t used to call the function.

Anyway I suggest you don’t put that check in every function that acts as a class. Instead use this convention: any function whose name begins with a capital letter is a class and must be called using the `new` operator.

Let’s move on, and find out what a _prototype_ is:

```js
class Shape {
  getName() {
    return 'Shape';
  }
}
console.log(Shape.prototype.getName);
// prints function getName() ...
```

Each time you declare a method inside a class, you actually add that method to the prototype of the corresponding function. The equivalent in JS 5 is:

```js
function Shape() {}
Shape.prototype.getName = function getName() {
  return 'Shape';
};
console.log(new Shape().getName()); // prints Shape
```

Sometimes the class-functions are called _constructors_ because they act like constructors in a regular class.

You may wonder what happens if you declare a static method:

```js
class Point {
  static distance(p1, p2) {
    // ...
  }
}

console.log(Point.distance); // prints function distance
console.log(Point.prototype.distance); // prints undefined
```

Since static methods are in a 1 to 1 relation with classes, the static function is added to the constructor-function, not to the prototype.

Let’s recap all these concepts in a simple example:

```js
function Point(x, y) {
  this.x = x;
  this.y = y;
}

Point.prototype.toString = function toString() {
  return '(' + this.x + ',' + this.y + ')';
};
Point.distance = function distance() {
  // ...
}

console.log(new Point(1,2).toString()); // prints (1,2)
console.log(new Point(1,2) instanceof Point); // prints true
```

Up to now, we have found a simple way to:

* declare a function that acts as a class
* access the class instance using the `this` keyword
* create objects that are actually an instance of that class (`new Point(1,2) instanceof Point` returns `true` )

But what about inheritance? What about accessing the super class?

```js
class Hello {
  constructor(greeting) {
    this._greeting = greeting;
  }

  greeting() {
    return this._greeting;
  }
}

class World extends Hello {
  constructor() {
    super('hello');
  }

  worldGreeting() {
    return super.greeting() + ' world';
  }
}

console.log(new World().greeting()); // Prints hello
console.log(new World().worldGreeting()); // Prints hello world
```

Above is a simple example of inheritance using ECMAScript 6, below the same example using the the so called **prototype inheritance**:

```js
function Hello(greeting) {
  this._greeting = greeting;
}

Hello.prototype.greeting = function () {
  return this._greeting;
};

function World() {
  Hello.call(this, 'hello');
}

// Copies the super prototype
World.prototype = Object.create(Hello.prototype);
// Makes constructor property reference the sub class
World.prototype.constructor = World;

World.prototype.worldGreeting = function () {
  const hello = Hello.prototype.greeting.call(this);
  return hello + ' world';
};

console.log(new World().greeting()); // Prints hello
console.log(new World().worldGreeting()); // Prints hello world
```

This way of declaring classes is also suggested in the Mozilla MDN example [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/create#Examples).

Using the `class` syntax, we deduced that creating classes involves altering the prototype of a function. But why is that so? To answer this question we must understand what the `new` operator actually does.

### New operator in JavaScript

The `new` operator is explained quite well in the Mozilla MDN page [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new). But I can provide you with a relatively simple example that emulates what the `new` operator does:

```js
function customNew(constructor, ...args) {
  const obj = Object.create(constructor.prototype);
  const result = constructor.call(obj, ...args);

  return result instanceof Object ? result : obj;
}

function Point() {}
console.log(customNew(Point) instanceof Point); // prints true
```

Note that the real `new` algorithm is more complex. The purpose of the example above is just to explain what happens when you use the `new` operator.

When you write `new Point(1,2)`what happens is:

* The `Point` prototype is used to create an object.
* The function constructor is called and the just created object is passed as the context (a.k.a. `this`) along with the other arguments.
* If the constructor returns an Object, then this object is the result of the new, otherwise the object created from the prototype is the result.

So, what does **prototype inheritance** mean? It means that you can create objects that inherit all the properties defined in the prototype of the function that was called with the `new` operator.

If you think of it, in a classical language the same process happens: when you create an instance of a class, that instance can use the `this` keyword to access to all the functions and properties (public) defined in the class (and the ancestors). As opposite to properties, all the instances of a class will likely share the same references to the class methods, because there is no need to duplicate the method’s binary code.

### Functional programming

Sometimes people say that JavaScript is not well suited for Object Oriented programming, and you should use functional programming instead.

While I don’t agree that JS is not suited for O.O.P, I do think that functional programming is a very good way of programming. In JavaScript functions are [first class citizens](https://developer.mozilla.org/en-US/docs/Glossary/First-class_Function) (e.g. you can pass a function to another function) and it provides features like `bind` , `call` or `apply` which are base constructs used in functional programming.

In addition RX programming could be seen as an evolution (or a specialization) of functional programming. Have a look to [RxJs here](https://rxjs-dev.firebaseapp.com/).

### Conclusion

Use, when possible, ECMAScript 6 `class` syntax:

```js
class Point {
  toString() {
    //...
  }
}
```

or use function prototypes to define classes in ECMAScript 5:

```js
function Point() {}
Point.prototype.toString = function toString() {
  // ...
}
```

Hope you enjoyed the reading!

