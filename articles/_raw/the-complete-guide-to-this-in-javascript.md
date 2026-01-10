---
title: The Complete Guide to this in JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-18T07:45:00.000Z'
originalURL: https://freecodecamp.org/news/the-complete-guide-to-this-in-javascript
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9dc9740569d1a4ca39a1.jpg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: programming languages
  slug: programming-languages
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "In JavaScript, every function has a this reference automatically created\
  \ when you declare it. \nJavaScript's this is quite similar to a this reference\
  \ in other class-based languages such as Java or C# (JavaScript is a prototype-based\
  \ language and no “..."
---

In JavaScript, every function has a `this` reference automatically created when you declare it. 

JavaScript's `this` is quite similar to a `this` reference in other class-based languages such as Java or C# (JavaScript is a prototype-based language and no “class” concept): _It points to the which object is calling to the function_ (this object sometimes called as _context_). In JavaScript, however, _the `this` reference inside functions can be bound to different objects depending on where the function is being called_. 

Here are 5 basic rules for `this` binding in JavaScript:

### **Rule 1**

When a function is called in the global scope, the `this` reference is by default bound to the **global object** (`window` in the browser, or `global` in Node.js). For example:

```javascript
function foo() {
  this.a = 2;
}

foo();
console.log(a); // 2
```

Note: If you declare the `foo()` function above in strict mode, then you call this function in global scope, `this` will be `undefined` and assignment `this.a = 2` will throw `Uncaught TypeError` exception.

### **Rule 2**

Let’s examine example below:

```javascript
function foo() {
  this.a = 2;
}

const obj = {
  foo: foo
};

obj.foo();
console.log(obj.a); // 2
```

Clearly, in the above snippet, the `foo()` function is being called with _context_ is `obj` object and `this` reference now is bound to `obj`. So when a function is called with a context object, the `this` reference will be bound to this object.

### **Rule 3**

`.call`, `.apply` and `.bind` can all be used at the call site to explicitly bind `this`. Using `.bind(this)` is something you may see in quite a lot of React components.

```javascript
const foo = function() {
  console.log(this.bar)
}

foo.call({ bar: 1 }) // 1
```

Here’s a quick example of how each one is used to bind `this`:

* `.call()`: `fn.call(thisObj, fnParam1, fnParam2)`
* `.apply()`: `fn.apply(thisObj, [fnParam1, fnParam2])`
* `.bind()`: `const newFn = fn.bind(thisObj, fnParam1, fnParam2)`

### **Rule 4**

```javascript
function Point2D(x, y) {
  this.x = x;
  this.y = y;
}

const p1 = new Point2D(1, 2);
console.log(p1.x); // 1
console.log(p1.y); // 2
```

The thing you must notice that is the `Point2D` function called with `new` keyword, and `this` reference is bound to `p1` object. So when a function is called with `new` keyword, it will create a new object and `this` reference will be bound to this object.

Note: As you call a function with `new` keyword, we also call it as _constructor function_.

### **Rule 5**

JavaScript determines the value of `this` at runtime, based on the current context. So `this` can sometimes point to something other than what you expect.

Consider this example of a Cat class with a method called `makeSound()`, following the pattern in Rule 4 (above) with a constructor function and the `new` keyword.

```javascript
const Cat = function(name, sound) {
  this.name = name;
  this.sound = sound;
  this.makeSound = function() {
    console.log( this.name + ' says: ' + this.sound );
  };
}

const kitty = new Cat('Fat Daddy', 'Mrrooowww');
kitty.makeSound(); // Fat Daddy says: Mrrooowww
```

Now let’s try to give the cat a way to `annoy()` people by repeating his sound 100 times, once every half second.

```javascript
const Cat = function(name, sound) {
  this.name = name;
  this.sound = sound;
  this.makeSound = function() {
    console.log( this.name + ' says: ' + this.sound );
  };
  this.annoy = function() {
    let count = 0, max = 100;
    const t = setInterval(function() {
      this.makeSound(); // <-- this line fails with `this.makeSound is not a function` 
      count++;
      if (count === max) {
        clearTimeout(t);
      }
    }, 500);
  };
}

const kitty = new Cat('Fat Daddy', 'Mrrooowww');
kitty.annoy();
```

That doesn’t work because inside the `setInterval` callback we’ve created a new context with global scope, so `this` no longer points to our kitty instance. In a web browser, `this` will instead point to the Window object, which doesn’t have a `makeSound()` method.

A couple of ways to make it work:

1. Before creating the new context, assign `this` to a local variable named `me`, or `self`, or whatever you want to call it, and use that variable inside the callback.

```javascript
const Cat = function(name, sound) {
  this.name = name;
  this.sound = sound;
  this.makeSound = function() {
    console.log( this.name + ' says: ' + this.sound );
  };
  this.annoy = function() {
    let count = 0, max = 100;
    const self = this;
    const t = setInterval(function() {
      self.makeSound();
      count++;
      if (count === max) {
        clearTimeout(t);
      }
    }, 500);
  };
}

const kitty = new Cat('Fat Daddy', 'Mrrooowww');
kitty.annoy();
```

1. With ES6 you can avoid assigning `this` to a local variable by using an arrow function, which binds `this` to the context of the surrounding code where it’s defined.

```javascript
const Cat = function(name, sound) {
  this.name = name;
  this.sound = sound;
  this.makeSound = function() {
    console.log( this.name + ' says: ' + this.sound );
  };
  this.annoy = function() {
    let count = 0, max = 100;
    const t = setInterval(() => {
      this.makeSound();
      count++;
      if (count === max) {
        clearTimeout(t);
      }
    }, 500);
  };
}

const kitty = new Cat('Fat Daddy', 'Mrrooowww');
kitty.annoy();
```

