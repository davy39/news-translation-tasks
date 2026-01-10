---
title: Object Oriented Programming in JavaScript – Explained with Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-13T17:46:51.000Z'
originalURL: https://freecodecamp.org/news/how-javascript-implements-oop
coverImage: https://www.freecodecamp.org/news/content/images/2020/02/OOP-IN-JS-1.png
tags:
- name: JavaScript
  slug: javascript
- name: Object Oriented Programming
  slug: object-oriented-programming
seo_title: null
seo_desc: "By Dillion Megida\nJavaScript is not a class-based object-oriented language.\
  \ But it still has ways of using object oriented programming (OOP). \nIn this tutorial,\
  \ I'll explain OOP and show you how to use it.\nAccording to Wikipedia, class-based\
  \ programm..."
---

By Dillion Megida

JavaScript is not a class-based object-oriented language. But it still has ways of using object oriented programming (OOP). 

In this tutorial, I'll explain OOP and show you how to use it.

According to [Wikipedia](https://en.m.wikipedia.org/wiki/Class-based_programming), class-based programming is

> a style of Object-oriented programming (OOP) in which inheritance occurs via defining classes of objects, instead of inheritance occurring via the objects alone

The most popular model of OOP is class-based.

But as I mentioned, JavaScript isn't a classed-based langauge – it's is a prototype-based langauge.

According to Mozilla's documentaion:

> A prototype-based language has the notion of a prototypical object, an object used as a template from which to get the initial properties for a new object.

Take a look at this code:

```javascript
let names = {
    fname: "Dillion",
    lname: "Megida"
}
console.log(names.fname);
console.log(names.hasOwnProperty("mname"));
// Expected Output
// Dillion
// false
```

The object variable `names` has only two properties -  `fname` and `lname` . No methods at all. 

So where does `hasOwnProperty` come from?

Well, it comes from the `Object` prototype.

Try logging the contents of the variable to the console:

```js
console.log(names);
```

When you expand the results in the console, you'll get this:

![Image](https://www.freecodecamp.org/news/content/images/2020/02/1-1.png)
_console.log(names)_

Notice the last property - `__proto__`? Try expanding it:

![Image](https://www.freecodecamp.org/news/content/images/2020/02/2-1.png)
_The __proto__ property of names_

You'll see a set of properties under the  `Object` constructor. All these properties are coming from the global `Object` prototype. If you look closely, you'll also notice our hidden `hasOwnProperty` .

In other words, all objects have access to the `Object`'s prototype. They do not possess these properties, but are granted access to the properties in the prototype.

## The `__proto__` property

This points to the object which is used as a prototype.

This is the property on every object that gives it access to the `Object prototype` property.

Every object has this property by default, which refers to the `Object Protoype` except when configured otherwise (that is, when the object's `__proto__` is pointed to another prototype).

### Modifying the `__proto__` property

This property can be modified by explicitly stating that it should refer to another prototype. The following methods are used to achieve this:

### `Object.create()`

```javascript
function DogObject(name, age) {
    let dog = Object.create(constructorObject);
    dog.name = name;
    dog.age = age;
    return dog;
}
let constructorObject = {
    speak: function(){
        return "I am a dog"
    }
}
let bingo = DogObject("Bingo", 54);
console.log(bingo);
```

In the console, this is what you'd have:

![Image](https://www.freecodecamp.org/news/content/images/2020/02/3-1.png)
_console.log(bingo)_

Notice the `__proto__` property and the `speak` method?

`Object.create` uses the argument passed to it to become the prototype.

### `new` keyword

```javascript
function DogObject(name, age) {
    this.name = name;
    this.age = age;
}
DogObject.prototype.speak = function() {
    return "I am a dog";
}
let john = new DogObject("John", 45);
```

`john`'s `__proto__` property is directed to `DogObject`'s prototype. But remember, `DogObject`'s prototype is an object (**key and value pair**), hence it also has a `__proto__` property which refers to the global `Object` protoype.

This technique is referred to as **PROTOTYPE CHAINING**.

**Note that:** the `new` keyword approach does the same thing as `Object.create()` but only makes it easier as it does some things automatically for you.

### And so...

Every object in Javascript has access to the `Object`'s prototype by default. If configured to use another prototype, say `prototype2`, then `prototype2` would also have access to the Object's prototype by default, and so on.

### Object + Function Combination

You are probably confused by the fact that `DogObject` is a function (`function DogObject(){}`) and it has properties accessed with a **dot notation**. This is referred to as a **function object combination**.

When functions are declared, by default they are given a lot of properties attached to it. Remember that functions are also objects in JavaScript data types.


## Now, Class

JavaScript introduced the `class` keyword in ECMAScript 2015. It makes JavaScript seem like an OOP language. But it is just syntatic sugar over the existing prototyping technique. It continues its prototyping in the background but makes the outer body look like OOP. We'll now look at how that's possible.

The following example is a general usage of a `class` in JavaScript:

```javascript
class Animals {
    constructor(name, specie) {
        this.name = name;
        this.specie = specie;
    }
    sing() {
        return `${this.name} can sing`;
    }
    dance() {
        return `${this.name} can dance`;
    }
}
let bingo = new Animals("Bingo", "Hairy");
console.log(bingo);
```

This is the result in the console:

![Image](https://www.freecodecamp.org/news/content/images/2020/02/5-1.png)
_console.log(bingo)_

The `__proto__` references the `Animals` prototype (which in turn references the `Object` prototype).

From this, we can see that the constructor defines the major features while everything outside the constructor (`sing()` and `dance()`) are the bonus features (**prototypes**).

In the background, using the `new` keyword approach, the above translates to:

```javascript
function Animals(name, specie) {
    this.name = name;
    this.specie = specie;
}
Animals.prototype.sing = function(){
    return `${this.name} can sing`;
}
Animals.prototype.dance = function() {
    return `${this.name} can dance`;
}
let Bingo = new Animals("Bingo", "Hairy");
```

## Subclassing

This is a feature in OOP where a class inherits features from a parent class but possesses extra features which the parent doesn't. 

The idea here is, for example, say you want to create a *cats* class. Instead of creating the class from scratch - stating the *name*, *age* and *species* property afresh, you'd inherit those properties from the parent *animals* class. 

This *cats* class can then have extra properties like *color of whiskers*.

Let's see how subclasses are done with `class`.

Here, we need a parent which the subclass inherits from. Examine the following code:

```js
class Animals {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    sing() {
        return `${this.name} can sing`;
    }
    dance() {
        return `${this.name} can dance`;
    }
} 
class Cats extends Animals {
    constructor(name, age, whiskerColor) {
        super(name, age);
        this.whiskerColor = whiskerColor;
    }
    whiskers() {
        return `I have ${this.whiskerColor} whiskers`;
    }
}
let clara = new Cats("Clara", 33, "indigo");
```

With the above, we get the following outputs:

```js
console.log(clara.sing());
console.log(clara.whiskers());
// Expected Output
// "Clara can sing"
// "I have indigo whiskers"
```

When you log the contents of clara out in the console, we have:

![Image](https://www.freecodecamp.org/news/content/images/2020/02/6-1.png)
_console.log(clara)_

You'll notice that `clara` has a `__proto__` property which references the constructor `Cats` and gets access to the `whiskers()` method. This `__proto__` property also has a `__proto__` property which references the constructor `Animals` thereby getting access to `sing()` and `dance()`. `name` and `age` are properties that exist on every object created from this.

Using the `Object.create` method approach, the above translates to:

```js
function Animals(name, age) {
    let newAnimal = Object.create(animalConstructor);
    newAnimal.name = name;
    newAnimal.age = age;
    return newAnimal;
}
let animalConstructor = {
    sing: function() {
        return `${this.name} can sing`;
    },
    dance: function() {
        return `${this.name} can dance`;
    }
}
function Cats(name, age, whiskerColor) {
    let newCat = Animals(name, age);
    Object.setPrototypeOf(newCat, catConstructor);
    newCat.whiskerColor = whiskerColor;
    return newCat;
}
let catConstructor = {
    whiskers() {
        return `I have ${this.whiskerColor} whiskers`;
    }
}
Object.setPrototypeOf(catConstructor, animalConstructor);
const clara = Cats("Clara", 33, "purple");
clara.sing();
clara.whiskers();
// Expected Output
// "Clara can sing"
// "I have purple whiskers"
```

`Object.setPrototypeOf` is a method which takes in two arguments - the object (first argument) and the desired prototype (second argument).

From the above, the `Animals` function returns an object with the `animalConstructor` as prototype. The `Cats` function returns an object with `catConstructor` as it's prototype. `catConstructor` on the other hand, is given a prototype of `animalConstructor`.

Therefore, ordinary animals only have access to the `animalConstructor` but cats have access to the `catConstructor` and the `animalConstructor`.

## Wrapping Up

JavaScript leverages its prototype nature to welcome OOP developers to its ecosystem. It also provides easy ways to creating prototypes and organize related data.

True OOP languages do not perform prototyping in the background - just take note of that.

A big thanks to [Will Sentance](https://frontendmasters.com/teachers/will-sentance/)'s course on Frontend Masters - [JavaScript: The Hard Parts of Object Oriented JavaScript](https://frontendmasters.com/courses/object-oriented-js/). I learned everything you see in this article (plus a little extra research) from his course. You should check it out.

You can hit me up on Twitter at [iamdillion](https://twitter.com/iamdillion) for any questions or contributions.

Thanks for reading : )

### Useful Resources

- [Object-oriented JavaScript for beginners](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object-oriented_JS)
- [Introduction to Object Oriented Programming in JavaScript](https://www.geeksforgeeks.org/introduction-object-oriented-programming-javascript/)


