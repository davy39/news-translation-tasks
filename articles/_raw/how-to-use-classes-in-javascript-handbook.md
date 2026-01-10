---
title: How to Use Classes in JavaScript – A Handbook for Beginners
subtitle: ''
author: Spruce Emmanuel
co_authors: []
series: null
date: '2025-02-18T12:29:27.257Z'
originalURL: https://freecodecamp.org/news/how-to-use-classes-in-javascript-handbook
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1739878241514/a725b4af-8061-49c2-9575-2aa4096acb74.png
tags:
- name: JavaScript
  slug: javascript
- name: Object Oriented Programming
  slug: object-oriented-programming
seo_title: null
seo_desc: Are you curious about classes in JavaScript but feel a little puzzled about
  how they work or why you'd even use them? If that's you, then you're definitely
  in the right place. Lots of developers find classes a bit tricky at first, and honestly,
  I was...
---

Are you curious about classes in JavaScript but feel a little puzzled about how they work or why you'd even use them? If that's you, then you're definitely in the right place. Lots of developers find classes a bit tricky at first, and honestly, I was once there too.

This article is for you if any of these sounds familiar:

* JavaScript is your first programming language.
    
* You are new to, or not entirely comfortable with, Object-Oriented Programming (OOP) principles.
    
* You have primarily used functions for structuring your JavaScript code.
    

If you're nodding along to any of these, then keep reading.

In this article, we'll take a step-by-step approach, showing you how object-oriented programming is implemented in JavaScript with objects and constructor functions, and clearly illustrate why understanding and using classes will make you a more versatile and effective JavaScript developer, even if you’re used to writing everything in functions. We’ll end everything with a simple to-do app example so you can see how to use classes.

## Table of Contents

* [Functions, Functions Everywhere I Turn](#heading-functions-functions-everywhere-i-turn)
    
* [Hold on a second. Are we saying functions are bad now?](#heading-hold-on-a-second-are-we-saying-functions-are-bad-now)
    
* [Wait, what? JavaScript has no real classes?](#heading-wait-what-javascript-has-no-real-classes)
    
* [Let's talk about objects in JavaScript.](#heading-lets-talk-about-objects-in-javascript)
    
* [Constructor Functions: Object Blueprints—Let's Get Practical](#heading-constructor-functions-object-blueprintslets-get-practical)
    
* [Constructor Functions: Great for Blueprints, but... Memory Waste?](#heading-constructor-functions-great-for-blueprints-but-memory-waste)
    
* [Prototypes to the Rescue (Again): Sharing Methods Efficiently](#heading-prototypes-to-the-rescue-again-sharing-methods-efficiently)
    
* [Constructor Functions + Prototypes: A Powerful Combo](#heading-constructor-functions-prototypes-a-powerful-combo)
    
* [Inheritance with Constructor Functions: Passing Down the Family Traits (the Constructor Way)](#heading-inheritance-with-constructor-functions-passing-down-the-family-traits-the-constructor-way)
    
* [Enter ES6 Classes: Syntactic Sugar for Prototypes](#heading-enter-es6-classes-syntactic-sugar-for-prototypes)
    
* [ES6 Classes: Class Syntax – Prototypes in Disguise](#heading-es6-classes-class-syntax-prototypes-in-disguise)
    
* [What’s Next? More Class Features and Real-World Examples](#heading-whats-next-more-class-features-and-real-world-examples)
    
* [Conclusion](#heading-conclusion)
    

## Functions, Functions Everywhere I Turn

If you started with JavaScript, chances are that you've become really comfortable with functions. They're like the building blocks of everything for you, right? Think about it: if I asked you to write a program to greet someone by name, you'd probably whip up something like this in a flash:

```javascript
function greetUser(userName) {
  alert("Hello, " + userName + "!");
}

greetUser("Alice"); // Like magic! It greets Alice.
```

Okay, let's level up a bit. Imagine that I asked you to write a program that figures out someone's birth year just by knowing their age. If they're 25, you'd want it to tell them '2000' (assuming the current year is 2025).

What would your first thought be? Probably something like, 'Function time!' Am I right? You'd think, 'I'll write a function; it'll take the age, and boom, it'll spit out the birth year.' See?

Function-first thinking. Totally natural in JavaScript. And here's how you might code it:

```javascript
function getBirthYear(age) {
  const currentYear = 2025; //  For this example, let's say it's 2025
  const birthYear = currentYear - age;
  return birthYear;
}
console.log(getBirthYear(25)); // Yep, it logs 2000!
```

%[https://codepen.io/Spruce_khalifa/pen/gbOYvvo] 

Now, let's make it a bit more complex. What if we want to be a little smarter and make sure the age is actually a valid age? You know, not some crazy string or a negative number. Sticking with our function-loving brains, what's the natural next step? Another function, of course. We'd probably create a `validateAge` function:

```javascript
function validateAge(age) {
  if (typeof age !== "number" || age <= 0 || age > 120) {
    return "Invalid age";
  } else {
    return age; //  Age is good to go!
  }
}

console.log(validateAge(25)); //  Output: 25 (valid!)
console.log(validateAge("twenty")); //  Output: Invalid age (not a number)
console.log(validateAge(-5)); //  Output: Invalid age (negative)
```

%[https://codepen.io/Spruce_khalifa/pen/xbxKYjZ] 

See how we're just piling up functions? `getBirthYear` does one thing, `validateAge` does another. They're separate little boxes of code.

Let's push this a little further. What if we also wanted to figure out someone's zodiac sign based on their birth year? Yep, you guessed it—the brain says, 'More functions.' Let's just write another `getZodiacSign` function:

```javascript
function getZodiacSign(birthYear) {
    const signs = [
        "Monkey", 
        "Rooster", 
        "Dog", 
        "Pig", 
        "Rat",    
        "Ox",
        "Tiger", 
        "Rabbit", 
        "Dragon", 
        "Snake", 
        "Horse", 
        "Sheep"
    ];
    return signs[birthYear % 12]; // Simple modulo trick!
}
```

%[https://codepen.io/Spruce_khalifa/pen/RNwbQxg] 

Are you noticing the pattern here? For every new thing we want to do we're just adding more *and* more separate functions. Things are starting to feel a *bit...* scattered, right? And we're not even done adding features.

Okay, now let's say we want to store even more information about a person—their name, country, profession, besides just age. How would we manage all this with our function-centric approach? Well, we might try to create a big 'Person' function that takes all this info:

```javascript
function Person(name, age, country, profession) {
  const personName = name;
  const personAge = age;
  const personCountry = country;
  const personProfession = profession;

  const validatedAge = validateAge(personAge);
  const birthYear = getBirthYear(validatedAge);
  const zodiacSign = getZodiacSign(birthYear);

  alert(
    `${personName}, you're ${personAge} years old, born in ${birthYear}, zodiac sign: ${zodiacSign}!`
  );
}
```

What if we then want to use the person's name in our other functions, like `getZodiacSign` or `getBirthYear`? We'd have to go back and manually add `name` as an argument to each of those functions. Imagine having to update every function whenever you add a new piece of person information.

```js
//  Suddenly, we need 'name' everywhere!

function getZodiacSign(birthYear, name) {
  alert("Zodiac sign for " + name + " is...");
  //... rest of zodiac logic...
}

function getBirthYear(age, name) {
  alert("Birth year for " + name + " is...");
  // ... rest of birth year logic...
}
```

In this tiny example, it's sort of manageable. But picture a huge project with tons of functions spread across files and folders, how you’d try to keep everything in sync and update functions whenever your `person` data changes. That sounds like a recipe for headaches, bugs, and a lot of frustration. It can become incredibly inefficient and, honestly, pretty error-prone.

## Hold on a second. Are we saying functions are bad now?

Functions are amazing. Think of this function-focused approach as the 'classic JavaScript way' of doing things. If you started with JavaScript, this probably feels totally natural and comfortable—and that's great. Even super popular modern libraries like React are built using functions for components. Functions are incredibly powerful and flexible.

But, even in React, if you change some core data (like a 'prop' in React terms) in a main component, you might have to go digging through lots of other components to make sure everything still works smoothly. Functions are fantastic, but sometimes, for certain kinds of problems, there might be another way to organize our code. A way that, for some folks, feels more intuitive, especially if they come from other programming backgrounds.

Imagine asking a programmer whose first language was Java or C++ to build our `birth year` program. Their brain might light up, but they'd probably think something a bit different. Maybe something like this:

'We need a `Person(class)`. A `Person` has an `age(proterty)` and we need a way to `calculateBirthYear(action)` for a `Person`.'

Notice anything different? Functions aren't the first thing that jumps to their mind. It's more about `objects` and `things` having `properties` and `actions`. Mind-blowing, huh? Many programmers who started with languages like Java or C++ naturally think in this object-oriented (or OOP) style. And hey, maybe that's why you're reading this—maybe you're curious about exploring this object-thinking approach too, especially in JavaScript. Don't worry, I’m not asking you to suddenly switch to Java 😉.

So, about these classes in JavaScript. Get ready for a little JavaScript twist. Here's the thing: JavaScript technically doesn't have classes in the way languages like Java or C++ do. I know, it can be a bit of a head-scratcher. Instead of classical classes as found in languages like Java or C++, JavaScript is built on something called prototypes\*.\* It uses these flexible prototypes and objects to mimic how classes work in other languages. So, if you want to use classes in JavaScript effectively, the real key is to understand objects and prototypes first. That's where the magic is in JavaScript OOP.

## Wait, what? JavaScript has no real classes?

Does that mean we are stuck with just functions forever? Nope. Even though JavaScript does things its own way with prototypes (instead of classic classes), it still fully supports 'Object-Oriented Programming' (OOP).

Let's break down OOP in plain English. Two big ideas in OOP are **Encapsulation** and **Inheritance**. Sounds fancy, right? But they're actually pretty simple concepts.

Encapsulation? Imagine a capsule, like for medicine. You're just bundling things that belong together. In OOP, encapsulation means grouping data (like age, name) and the actions you can do with that data (like calculate birth year, greet) inside a single 'object'. JavaScript objects are perfect for this.

And inheritance? Think of it like inheriting traits from your family. In JavaScript OOP, objects can 'inherit' properties and behaviors from other objects. JavaScript calls this prototypal inheritance, and the object you inherit from is called the prototype (we'll dive deeper into prototype soon).

See? No function jail here. JavaScript is totally ready for OOP. To see this in action, let's rewrite our birth year program, but this time using this OOP style in JavaScript.

Check this out. Here's how we could rewrite our birth year program using an OOP style in JavaScript, using just a good old JavaScript object:

```javascript
const Person = {
  //  --- Properties (Data) ---
  name: "Spruce",
  age: 25,
  country: "Nigeria",
  profession: "Engineer",

  //  --- Methods (Actions related to Person data) ---
  isValidAge: function () {
    return typeof this.age === "number" && this.age > 0;
  },

  getBirthYear: function () {
    if (!this.isValidAge()) {
      return "Invalid age!";
    }
    return new Date().getFullYear() - this.age;
  },

  getZodiacSign: function () {
    if (!this.isValidAge()) {
      return "Oops, can't get zodiac for an invalid age!";
    }

    const birthYear = this.getBirthYear();
    const zodiacSigns = [
      "Capricorn",
      "Aquarius",
      "Pisces",
      "Aries",
      "Taurus",
      "Gemini",
      "Cancer",
      "Leo",
      "Virgo",
      "Libra",
      "Scorpio",
      "Sagittarius",
    ];
    return zodiacSigns[birthYear % 12];
  },

  greet: function () {
    return (
      `Hello, I'm ${this.name}. I'm ${
        this.age
      } years old, born in ${this.getBirthYear()}, ` +
      `working as a ${this.profession} from ${
        this.country
      }.  My zodiac sign is ${this.getZodiacSign()}.`
    );
  },
};

//  --- Let's use our Person object! ---
console.log(Person.greet());
```

```javascript
//  Output (might vary slightly depending on year):

// "Hello, I'm Spruce. I'm 25 years old, born in 2000, working as a Engineer from Nigeria.  My zodiac sign is Pig."
```

%[https://codepen.io/Spruce_khalifa/pen/mydbXKq] 

See how neat that is? Everything about a `Person`, their details (name, age, and so on) and what you can do with a person (validate age, get birth year, greet) is all bundled together, and nicely organized inside this single `Person` object. That's encapsulation in action. Pretty cool, right?

Now, want to know the `Person` name? Super easy:

```javascript
console.log(Person.name); // Output: "Spruce"
```

Birth year? Piece of cake:

```javascript
console.log(Person.getBirthYear()); // Output (if current year is 2025): 2000
```

And here's the real magic of encapsulation: if we change something inside the `Person` object (like, say, we decide to change the age), all the methods (actions) inside automatically adapt. We don't have to go hunting around in separate functions to update things. Let me show you:

```javascript
//  Age is 25 initially...
console.log("Birth year when age is 25:", Person.getBirthYear()); // Output (if current year is 2025): 2000

//  Let's update the age directly in the Person object...
Person.age = 30;

//  Now, getBirthYear automatically uses the *new* age!
console.log("Birth year when age is 30:", Person.getBirthYear()); // Output (if current year is 2025): 1995
```

So, JavaScript uses objects—and, as we'll see, prototypes—to bring OOP to life, even if it doesn't have classic classes. Hopefully, you're starting to see the appeal of organizing code this way. Before we jump into classes, it makes a ton of sense to get a really solid understanding of objects and prototypes in JavaScript, right? That's what we'll dive into next.

## Let's talk about objects in JavaScript.

If you're already familiar with how objects work, that's fantastic. It'll make understanding everything we cover in this article even smoother. To make sure we're all on the same page, let's start with a super basic object:

```javascript
const Person = {};
```

So, is `Person` an empty object? At first glance, it certainly looks empty. If you thought "yes," you're not alone. It's a common initial thought. But in JavaScript, objects are a little more interesting than just what we explicitly put into them. Let's explore how objects really work under the hood.

### Okay, so how do objects work in JavaScript?

Let's break it down. At its core, an object is a collection of properties. Think of properties as named containers for values. Each property has a name (also called a 'key').

```javascript
const Person = {
  firstName: "John",
  lastName: "Doe",
};
```

`firstName` and `lastName` are the property names (keys), and `"John"` and `"Doe"` are their respective values. A property in an object is always a key-value pair. The value part can be many things.

The value associated with a property can be a primitive data type. In JavaScript, primitives are things like strings, numbers, booleans (`true` or `false`), `null`, `undefined`, and symbols. Let's see some examples:

```javascript
const exampleObject = {
  name: "Example", // String
  age: 30, // Number
  isStudent: false, // Boolean
  favoriteColor: null, // null
};
```

But the cool thing is, property values can also be more complex data types or even other objects, functions, and arrays. Let's look at that:

```js
const anotherObject = {
  address: {
    // Value is another object
    street: "123 Main St",
    city: "Anytown",
  },
  hobbies: ["reading", "hiking"], // Value is an array
  greet: function () {
    // Value is a function (a method!)
    console.log("Hello!");
  },
};
```

When a function is a property of an object, we call it a method. It's essentially a function that belongs to the object and usually operates on the object's data.

```javascript
const calculator = {
  value: 0,
  add: function(number) {
    this.value += number; // 'this' refers to the calculator object
  },
  getValue: function() {
    return this.value;
  }
};

calculator.add(5);
console.log(calculator.getValue()); // Output: 5
```

Now, here’s where things get really interesting. Objects in JavaScript don't just have the properties we explicitly define. They can also reference properties from other objects. This is a core concept called prototypal inheritance (sometimes just called prototypal delegation).

Remember our seemingly empty `Person = {}` object? We said it looked empty, right? Well, it's time for a bit of JavaScript magic. Even though we didn't put any properties in it ourselves, it's not completely empty. Every object in JavaScript, by default, has a hidden link (often referred to internally as its \[\[Prototype\]\] property) to another object called its prototype.

For objects created using the simple `{}` syntax (like our `person` object), their default prototype is the built-in `Object.prototype`. Think of `Object.prototype` as a kind of parent object that provides some basic, built-in functionality to all objects.

This is why you can do things like this, even with our "empty" `Person` object:

```javascript
console.log(Person.toString()); // Output: [object Object]
```

Wait a minute. We never defined a `toString()` method in our `Person` object. So where is it coming from? It's coming from its prototype, `Object.prototype`. `toString()` is a method that's built into `Object.prototype`, and because `Person's` prototype is `Object.prototype`, `Person` can access and use the `toString()` method.

So, a good way to think about it is: "The prototype of an object is another object from which it can look up and use properties and methods if it doesn't have them itself."

Why is understanding prototypes so important? Because it unlocks the power of code reuse and creating specialized objects based on more general ones. This is where things get really powerful, especially as your JavaScript projects grow.

Imagine that we want to create a more specific type of `Person`—say, a `Developer`. A `Developer` is still a `Person`, but they might have some additional properties or behaviors specific to developers. Basically, we want a `Developer` object to be a `Person`, but also have its own unique stuff.

This is where we can explicitly set up prototypes. Instead of relying on the default `Object.prototype`, we can tell JavaScript: "Hey, I want the prototype of my `Developer` object to be the `Person` object we already defined." We can do this using `Object.create()`:

```js
const Person = {
  firstName: "John",
  lastName: "Doe",
  sayHello: function () {
    console.log(`Hello, my name is ${this.firstName} ${this.lastName}`);
  },
};

const developer = Object.create(Person); // developer's prototype is now 'Person'
developer.firstName = "Spruce"; // Add a *specific* firstName for developer
developer.programmingLanguage = "JavaScript"; // Developer's own property

developer.sayHello(); // Output: Hello, my name is Spruce Person (still accesses sayHello from 'person' prototype!)
console.log(developer.programmingLanguage); // Output: JavaScript (developer's own property)
console.log(developer.lastName); // Output: Doe (inherited from 'Person' prototype!)
```

Let's break down what's happening when we access properties on `Developer`:"

```javascript
console.log(developer.firstName); // Output: Spruce (developer's *own* property)
console.log(developer.programmingLanguage); // Output: JavaScript (developer's *own* property)
console.log(developer.lastName); // Output: Doe (found on the *prototype* 'Person')
console.log(developer.sayHello()); // Output: Hello, my name is Spruce Person (method from *prototype*)
console.log(developer.job); // Output: undefined (not on 'Developer' OR 'Person' prototype)
```

When you try to access a property like `Developer.lastName`, JavaScript does the following:

1. First, it checks: Does `Developer` have a property named `lastName` directly on itself? In our example, `Developer` only has `firstName` and `programmingLanguage` as its own properties. `lastName` is not there.
    
2. If it doesn't find it on the object itself, JavaScript then looks at the object's prototype (which we set to `Person using` `Object.create()`).
    
3. It checks: 'Does the `Person` object (the prototype) have a property named `lastName`?' Yes, `Person` does have `lastName: "Doe"`. So, JavaScript uses this value.
    
4. If the property isn’t found on the prototype either, JavaScript would then look at the `Person`'s prototype (which is `Object.prototype` by default), and so on, up the prototype chain. If it goes all the way up the chain and still doesn't find the property, it finally returns `undefined` (like when we tried to access `developer.job`).
    

Own properties are simply the properties that are defined directly on the object itself when you create it (like `firstName` and `programmingLanguage` on `Developer`). Prototype properties are accessed through the prototype chain.

You can even create longer prototype chains. For example, let's say we want to create a `JavaScriptDeveloper` object, which is a type of `Developer`. We can make `Developer` the prototype of `JavaScriptDeveloper`:

```javascript
const JavaScriptDeveloper = Object.create(Developer); // javaScriptDeveloper's prototype is 'Developer'

JavaScriptDeveloper.framework = "React"; // JavaScriptDeveloper's own property

console.log(JavaScriptDeveloper.firstName); // Output: Spruce (from 'Developer' prototype)

console.log(JavaScriptDeveloper.lastName); // Output: Doe (from 'Person' prototype)

console.log(JavaScriptDeveloper.programmingLanguage); // Output: JavaScript (from 'Developer' prototype)

console.log(JavaScriptDeveloper.framework); // Output: React (JavaScriptDeveloper's own property)

console.log(JavaScriptDeveloper.job); // Output: undefined (not found anywhere in the chain)
```

(Optional Exploration: If you're curious, trace the lookup for `javaScriptDeveloper.lastName`. It goes: `JavaScriptDeveloper` -&gt; `Developer` -&gt; `Person` -&gt; `Object.prototype`).

Okay, prototypes are powerful. We can create objects that share properties and behaviors and specialize them for different needs. But imagine if we wanted to create hundreds of `Person` objects, hundreds of `Developer` objects, and hundreds of `JavaScriptDeveloper` objects.

Using `Object.create()` every time would still be quite repetitive, especially if we want to ensure that every `Person` starts with the same basic properties (like `firstName` and `lastName`).

We need a better way to create multiple objects that follow the same pattern, like a blueprint that we can re-use over and over again to create objects. This is what classes are for, they are just blueprints that we can use to create multiple objects, and JavaScript uses Constructor functions to create classes (the blueprints).

In the next section, we’ll dive into how javascript uses Constructor functions to implement classes.

## Constructor Functions: Object Blueprints—Let's Get Practical

Okay, prototypes are pretty cool for code reuse and making specialized objects. We saw how `Object.create()` lets us create objects that inherit from others. But imagine that we wanted to make tons of `Person` objects, like, hundreds of them for a website. Typing out `Object.create(person)` for every single one would get super repetitive, especially if we always want every `Person` to start with the same basic properties, like a `firstName` and `lastName`.

We need a more efficient way to make lots of objects that follow the same pattern. What we really need is something like a blueprint—something we can use over and over again to stamp out new objects, all looking and working in a similar way. And guess what? That’s exactly what constructor functions are for.

Think of constructor functions as JavaScript's way of creating blueprints for objects. They're like object factories. And in JavaScript, we use constructor functions, which are specialized functions used in a particular way, to create these blueprints. Yep, functions again. But we use them in a special way.

### So what is a constructor function, exactly?

Well, like I said, it's a function that creates objects. Take a look at this example:

```js
function PersonConstructor(name, age) {
  this.name = name;
  this.age = age;
  this.greet = function () {
    console.log(`Hello, I'm ${this.name}`);
  };
}
```

That looks like a regular function. You're absolutely right. It looks just like any other function you've probably written in JavaScript. In fact, let's prove it. If we just log `PersonConstructor` itself, we’ll see:

```js
console.log(PersonConstructor);
```

```js
// output
function PersonConstructor(name, age) {
  this.name = name;
  this.age = age;
  this.greet = function () {
    console.log(`Hello, I'm ${this.name}`);
  };
}
```

See? Just a regular function. So, what makes it a constructor function?

### The Magic Ingredient: The `new` Keyword

What turns an ordinary function into a constructor\*\*—\*\*something that builds objects—is the `new` keyword. It's like saying to JavaScript, "Hey, treat this function as a blueprint, and use it to create a new object for me."

Let's see it in action:

```js
const person1 = new PersonConstructor("Alice", 25);

console.log(person1);
```

```js
// output

// PersonConstructor { name: 'Alice', age: 25, greet: [Function] }
```

In the output now, instead of just seeing the function code, we're seeing a `PersonConstructor` object. The `new` keyword didn't just call the function, it actually created a brand new object based on the `PersonConstructor` blueprint.

Now, we can use this blueprint, `PersonConstructor`, to create as many `Person` objects as we want, all with the same basic structure:

```js
const person1 = new PersonConstructor("Alice", 25);
const person2 = new PersonConstructor("Bob", 30);
const person3 = new PersonConstructor("Charlie", 28);

console.log(person1);
console.log(person2);
console.log(person3);
```

```js
// output
PersonConstructor { name: 'Alice', age: 25, greet: [Function] }
PersonConstructor { name: 'Bob', age: 30, greet: [Function] }
PersonConstructor { name: 'Charlie', age: 28, greet: [Function] }
```

Cool, right? We have three distinct `Person` objects, all created from the same `PersonConstructor` blueprint.

### Hold Up... What's This `this` Keyword I Keep Seeing?

You've probably noticed the word `this` popping up a lot in these code examples, like in `this.name`, `this.age`, and `this.greet()`. And you might be thinking, "What in the JavaScript world is `this`?"

Don't worry, `this` can be a bit confusing at first, but it's actually pretty simple once you get the hang of it. Let's break it down with a simple analogy.

Imagine you're describing yourself. You might say, "My name is \[Your Name\]." In this sentence, "my" refers to you, the person speaking.

In JavaScript objects, `this` is like "my" or "me." It's a way for an object to refer to itself.

Let's see this with a regular object example first:

```js
const PersonObject = {
  name: "Spruce",
  greet: function () {
    console.log("Hello, my name is " + PersonObject.name); //  Using PersonObject.name directly
  },
};

PersonObject.greet(); // Output: Hello, my name is Spruce
```

In this `PersonObject`, inside the `greet` function, we used `PersonObject.name` to access the `name` property. This works perfectly fine. We're directly telling JavaScript to get the `name` property from the `PersonObject`. We could use `this` here too, but let's see why `this` becomes super helpful, especially in constructor functions.

Now, consider this slightly different version using `this`:

```js
const PersonObjectThis = {
  name: "Spruce",
  greet: function () {
    console.log("Hello, my name is " + this.name); // Using 'this.name'
  },
};

PersonObjectThis.greet(); // Output: Hello, my name is Spruce
```

See? It still works the same way. When `greet` is called on `PersonObjectThis`, inside the `greet` function, it automatically refers to `PersonObjectThis`. So `this.name` is just a more dynamic way of saying "the `name` property of this current object."

### Why use `this` instead of directly naming the object?

Because `this` is dynamic and context-aware. It always points to the object that is currently calling the method. This becomes essential in constructor functions because constructor functions are designed to create many different objects.

### Back to constructor functions: What does `this` mean there?

Let's revisit our `PersonConstructor`:

```js
function PersonConstructor(name, age) {
  this.name = name;
  this.age = age;
  this.greet = function () {
    console.log(`Hello, I'm ${this.name}`);
  };
}

const person1 = new PersonConstructor("Alice", 25);
const person2 = new PersonConstructor("Bob", 30);
```

When we do `const person1 = new PersonConstructor("Alice", 25);` inside the `PersonConstructor` function:

* `this` becomes `person1`. It's as if JavaScript is doing:
    
    * [`person1.name`](http://person1.name) `= "Alice";`
        
    * `person1.age = 25;`
        
    * `person1.greet = function() { ... };`
        

And when we do `const person2 = new PersonConstructor("Bob", 30);` inside `PersonConstructor` again:

* `this` becomes `person2`. Like JavaScript doing:
    
    * [`person2.name`](http://person2.name) `= "Bob";`
        
    * `person2.age = 30;`
        
    * `person2.greet = function() { ... };`
        

So, `this` in a constructor function is like a placeholder that gets filled in with the specific object being created when you use `new`. It's what lets us create many different objects from the same blueprint.

## Constructor Functions: Great for Blueprints, but... Memory Waste?

Okay, so now that you know how to create object blueprints using constructor functions, and you understand what `this` does, we can make lots of `Person` objects.

But there's a little problem lurking in our `PersonConstructor`:

```js
function PersonConstructor(name, age) {
  this.name = name;
  this.age = age;
  this.greet = function () {
    // 😬 Look at this greet function!
    console.log(`Hello, I'm ${this.name}`);
  };
}

const person1 = new PersonConstructor("Alice", 25);
const person2 = new PersonConstructor("Bob", 30);

console.log(person1, person2);
```

```js
// output

PersonConstructor {name: "Alice", age: 25, greet: function}

PersonConstructor {name: "Bob", age: 30, greet: function}
```

Notice the `greet` function inside the `PersonConstructor`? Every time we create a new `Person` object using `new PersonConstructor()`, we're actually copying the entire `greet` function to each and every object.

Imagine that we create one thousand `Person` objects. We'd have a thousand identical `greet` functions in memory. For a simple `greet()` function, the memory impact might seem small. However, if you had more complex methods with lots of code, or if you were creating thousands or even millions of objects, duplicating these functions for every single object can become a significant waste of memory.

It also impacts performance as JavaScript has to manage all these duplicated functions. That's a lot of duplicated code, and it's not very memory-efficient, especially if the `greet` function (or other methods) were more complex.

## Prototypes to the Rescue (Again): Sharing Methods Efficiently

Remember prototypes? We learned that objects can inherit properties and methods from their prototypes. Well, constructor functions have a built-in way to use prototypes to solve this memory-waste problem.

Instead of defining the `greet` function inside the constructor and thus copying it to every instance, we can add it to the `prototype` of the `PersonConstructor` function.

Like this:

```js
function PersonConstructor(name, age) {
  this.name = name;
  this.age = age;
}

//  --- Add the greet method to the PROTOTYPE of PersonConstructor! ---
PersonConstructor.prototype.greet = function () {
  console.log(`Hello, I'm ${this.name}`);
};
```

Now, the `greet` method is defined only once on `PersonConstructor.prototype`. But all objects created with `PersonConstructor` can still use it. They inherit it from the prototype.

Let's test it:

```js
const person1 = new PersonConstructor("Alice", 25);
const person2 = new PersonConstructor("Bob", 30);

person1.greet(); // Output: Hello, I'm Alice  - Still works!
person2.greet(); // Output: Hello, I'm Bob    - Still works!

console.log(person1.greet === person2.greet); // Output: false - They are NOT the same function object in memory

console.log(person1.__proto__.greet === person2.__proto__.greet); // Output: true - But they share the same prototype method!
```

`person1.greet()` and `person2.greet()` still work perfectly. But now, the `greet` function is not copied for each object. It's shared through the prototype. This is much more efficient, especially when we're dealing with lots of objects and methods.

## Constructor Functions + Prototypes: A Powerful Combo

We've now seen how constructor functions act as blueprints for creating objects, and how using the prototype of a constructor function lets us efficiently share methods among all objects created from that blueprint.

This is a key pattern in JavaScript for creating reusable object structures.

### Okay, we've covered object creation and efficient methods... But what about inheritance with constructor functions?

What if we want to create a `DeveloperPerson` blueprint that inherits from our `PersonConstructor` blueprint? So that `DeveloperPerson` objects automatically has `name`, `age`, and `greet`, but can also have its own special developer-related properties and methods?

That's where things get a bit more involved with constructor functions, and we'll need to use a special trick called `call()` to make inheritance work. Let's dive into that next.

## Inheritance with Constructor Functions: Passing Down the Family Traits (the Constructor Way)

Alright, we're making good progress. We've got constructor functions to create object blueprints, and prototypes to share methods efficiently. But one of the big reasons people use OOP is for inheritance – the idea of creating specialized objects that build upon more general ones.

Think back to our `Person` and `Developer` example. A `Developer` is a `Person`, right? They have a name, an age, maybe they greet people, but they also have developer-specific properties, like a favorite programming language and the ability to code.

How can we create a `DeveloperPersonConstructor` blueprint that inherits all the basic `PersonConstructor` stuff, and then adds its own developer-specific features? With constructor functions, you can use something called `call()`.

### `call()`: The Secret Inheritance Handshake

`call()` is a function method that lets you do something a bit unusual: you can borrow a function from one object and run it in the context of another object. Sounds confusing? Let's simplify.

To illustrate `call()`, let's consider our `PersonConstructor`. We want to create a `DeveloperPersonConstructor` that also sets up `name` and `age` in the same way `PersonConstructor` does, before adding developer-specific properties.

This is where `call()` comes in. We can use `call()` to essentially say: "Hey `PersonConstructor`, run your code, but run it as if you were inside `DeveloperPersonConstructor`, and set up `name` and `age` for this `DeveloperPerson` object we're currently creating."

Let's see this in code to make it clearer:

```js
function PersonConstructor(name, age) {
  this.name = name;
  this.age = age;
}

PersonConstructor.prototype.greet = function () {
  console.log(`Hello, I'm ${this.name}`);
};

function DeveloperPersonConstructor(name, age, programmingLanguage) {
  //  --- "Borrow" the PersonConstructor to set up name and age! ---
  PersonConstructor.call(this, name, age); //  <--  The magic of 'call()'

  // --- Now, add developer-specific properties ---
  this.programmingLanguage = programmingLanguage;
  this.code = function () {
    console.log(`${this.name} is coding in ${this.programmingLanguage}`);
  };
}
```

See that line: [`PersonConstructor.call`](http://PersonConstructor.call)`(this, name, age);` ? That's the key to inheritance here. Let's break it down:

* [`PersonConstructor.call`](http://PersonConstructor.call)`(...)`: We're calling the `PersonConstructor` function, but not in the usual way. We're using `.call()`.
    
* `this`: The first argument to `call()` is crucial. It specifies what `this` should be inside the `PersonConstructor` function when it runs. Here, we're passing `this` from `DeveloperPersonConstructor`. Why? Because we want `PersonConstructor` to set up `name` and `age` on the `DeveloperPerson` object that's currently being created.
    
* `name, age`: These are the arguments we're passing to the `PersonConstructor` function itself. So, when `PersonConstructor` runs (thanks to `.call()`), it will receive `name` and `age` and do what it normally does: set `this.name = name` and `this.age = age`. But because `this` is actually the `DeveloperPerson` object, it sets these properties on the `DeveloperPerson` object.
    

### Putting it all Together: Creating a `DeveloperPerson`

Now, let's create a `DeveloperPerson` object and see what happens:

```js
const devPerson1 = new DeveloperPersonConstructor("Eve", 30, "JavaScript");

console.log(devPerson1.name); // Output: Eve (Inherited from PersonConstructor!)
console.log(devPerson1.age); // Output: 30 (Inherited from PersonConstructor!)
devPerson1.greet(); // Output: (Oops! Error!)
console.log(devPerson1.programmingLanguage); // Output: JavaScript (Developer-specific)
devPerson1.code(); // Output: Eve is coding in JavaScript (Developer-specific)
```

Notice that `devPerson1.name` and `devPerson1.age` are there. `DeveloperPersonConstructor` borrowed the part of `PersonConstructor` that sets up those basic properties. And we also have `devPerson1.programmingLanguage` and `devPerson1.code()` which are specific to developers.

### Uh Oh! Where's `greet()`?

But wait, `devPerson1.greet()` is throwing an error. Why? Because even though we borrowed the constructor logic from `PersonConstructor`, we haven't yet set up the prototype chain for inheritance of prototype methods like `greet()`.

Right now, `devPerson1`'s prototype is just the default object prototype (`Object.prototype`). It's not inheriting from `PersonConstructor.prototype`. We need to fix that.

### Setting the Prototype Chain for Constructor Inheritance

To make `DeveloperPersonConstructor` objects also inherit prototype methods from `PersonConstructor`, we need to manually adjust the prototype chain. We can do this using `Object.create()` again.

We want the prototype of `DeveloperPersonConstructor` to be an object that inherits from `PersonConstructor.prototype`.

Here's the code:

```js
function PersonConstructor(name, age) {
  this.name = name;
  this.age = age;
}

PersonConstructor.prototype.greet = function () {
  console.log(`Hello, I'm ${this.name}`);
};

function DeveloperPersonConstructor(name, age, programmingLanguage) {
  PersonConstructor.call(this, name, age);
  this.programmingLanguage = programmingLanguage;
  this.code = function () {
    console.log(`${this.name} is coding in ${this.programmingLanguage}`);
  };
}

// ---  Set up the Prototype Chain for Inheritance! ---
DeveloperPersonConstructor.prototype = Object.create(
  PersonConstructor.prototype
);
```

That line `DeveloperPersonConstructor.prototype = Object.create(PersonConstructor.prototype);` is doing the magic. It's saying, "Hey JavaScript, set the prototype of `DeveloperPersonConstructor` to be a new object that inherits from `PersonConstructor.prototype`."

Now, let's try `devPerson1.greet()` again:

```js
const devPerson1 = new DeveloperPersonConstructor("Eve", 30, "JavaScript");

devPerson1.greet(); // Output: Hello, I'm Eve  - 🎉 It works now!
```

`devPerson1.greet()` now works. `devPerson1` is inheriting the `greet()` method from `PersonConstructor.prototype` through the prototype chain we just set up.

### Let's Trace the Prototype Chain

Let's really understand what's happening when we do `devPerson1.greet()`:

1. JavaScript checks: Does `devPerson1` itself have a `greet` property? No.
    
2. JavaScript looks at `devPerson1`'s prototype: `DeveloperPersonConstructor.prototype`. Does it have a `greet`property? No, we only added developer-specific methods or properties to `DeveloperPersonConstructor` directly, not to its prototype in our example. (We could add developer-specific prototype methods later).
    
3. JavaScript goes up the prototype chain to `DeveloperPersonConstructor.prototype`'s prototype: `PersonConstructor.prototype`. Does it have a `greet` property? Yes. We defined `PersonConstructor.prototype.greet = function() { ... };`
    
4. JavaScript finds `greet()` on `PersonConstructor.prototype`, and executes it in the context of `devPerson1` (so `this.name` inside `greet()` refers to `devPerson1.name`).
    

Prototype chain in action. `devPerson1` -&gt; `DeveloperPersonConstructor.prototype` -&gt; `PersonConstructor.prototype`\-&gt; `Object.prototype`.

### Going Even Further: JavaScript Developer Person

We can even create longer inheritance chains. Let's say we want to create a `JavaScriptDeveloperPersonConstructor` that's a special type of `DeveloperPersonConstructor`, maybe with a specific JavaScript framework preference.

We can do the same pattern:

```js
function JavaScriptDeveloperPersonConstructor(name, age, framework) {
  //  "Borrow" from DeveloperPersonConstructor first!
  DeveloperPersonConstructor.call(this, name, age, "JavaScript"); // Hardcoded "JavaScript"
  this.framework = framework;
  this.codeJavaScript = function () {
    // Specific to JavaScript developers
    console.log(`${this.name} is coding in JavaScript with ${this.framework}`);
  };
}

// Set up prototype chain: JavaScriptDeveloperPerson -> DeveloperPerson -> Person
JavaScriptDeveloperPersonConstructor.prototype = Object.create(
  DeveloperPersonConstructor.prototype
);
```

Now we have a three-level inheritance chain.

### Constructor Functions: Powerful, but a Bit... Verbose?

Constructor functions and prototypes are really powerful. They are the fundamental way JavaScript achieves OOP-like behavior. However, as you can see, setting up inheritance with `call()` and `Object.create()` can get a bit wordy and tricky to read, especially as inheritance chains get longer.

And guess what? The JavaScript folks noticed this too. In 2015, a new, cleaner syntax for creating object blueprints was introduced in JavaScript.

## Enter ES6 Classes: Syntactic Sugar for Prototypes

You see, in 2015, JavaScript developers recognized that using prototypes and constructor functions directly to achieve class-like patterns could become verbose and less straightforward to manage as applications grew. Therefore, they introduced the `class` syntax in ECMAScript 2015 (ES6).

Classes in JavaScript provide a much cleaner and more familiar way to create object blueprints and set up inheritance. But here’s the super important thing to remember: JavaScript classes are still built on top of prototypes. They don't fundamentally change how JavaScript OOP works. They are just syntactic sugar – a nicer, easier way to write code that's still using prototypes behind the scenes.

In the next section, we'll see how to rewrite our `Person`, `DeveloperPerson`, and `JavaScriptDeveloperPerson` examples using the new `class` syntax, and you'll see how much cleaner and more class-like (pun intended) it feels, while using the power of JavaScript prototypes.

## ES6 Classes: Class Syntax – Prototypes in Disguise

Okay, we've wrestled with constructor functions and `call()` and `Object.create()` to get inheritance working with prototypes. It's powerful, but let's be honest, it can feel a little verbose and indirect, especially if you're used to class-based languages.

That's where ES6 classes come to the rescue. They offer a much more streamlined and class-like syntax for creating object blueprints in JavaScript.

Let's rewrite our `PersonConstructor` example using the `class` syntax. Get ready for a breath of fresh air.

### `PersonClass` - Constructor Function Reimagined as a Class

Here's how we can define our `Person` blueprint as a class:

```js
class PersonClass {
  //  Using the 'class' keyword!
  constructor(name, age) {
    //  'constructor' method - like our old constructor function
    this.name = name; //  Still using 'this' in the constructor
    this.age = age;
  }

  greet() {
    console.log(`Hello, I'm ${this.name}`);
  }
}
```

Doesn't that look much cleaner and more organized? Let's break down the class syntax:

* `class PersonClass { ... }`: We start with the `class` keyword, followed by the class name (`PersonClass` in this case). Class names are conventionally capitalized.
    
* `constructor(name, age) { ... }`: Inside the class, we have a special method called `constructor`. This is like our old `PersonConstructor` function. It's where we put the code to initialize the properties of a new `PersonClass` object when it's created with `new`. We still use `this` inside the `constructor` to refer to the new object being created.
    
* `greet() { ... }`: This is how we define methods in a class. We simply write the method name (`greet`), followed by parentheses for parameters (none in this case), and then the method body in curly braces. Notice that we don't use the `function` keyword here. It's just `greet() { ... }`.
    

### Creating Objects from a Class - Still Using `new`

To create objects from our `PersonClass` blueprint, we still use the `new` keyword, just like we did with constructor functions:

```js
const classPerson1 = new PersonClass("Charlie", 28);
const classPerson2 = new PersonClass("Diana", 32);

console.log(classPerson1.name); // Output: Charlie
classPerson1.greet(); // Output: Hello, I'm Charlie
```

Yep, it works exactly the same way as our constructor function example, but the class syntax is just much more readable and less cluttered.

### `DeveloperPersonClass` - Inheritance Made Easy with `extends`

Now, let's tackle inheritance using classes. Remember how we had to use `call()` and `Object.create()` to get `DeveloperPersonConstructor` to inherit from `PersonConstructor`? With classes, inheritance becomes super straightforward using the `extends` keyword.

Here's how we can rewrite `DeveloperPersonConstructor` as a `DeveloperPersonClass` that inherits from `PersonClass`:

```js
class DeveloperPersonClass extends PersonClass {
  //  'extends' for inheritance!
  constructor(name, age, programmingLanguage) {
    super(name, age); //  'super()' calls the parent class constructor!
    this.programmingLanguage = programmingLanguage;
  }

  code() {
    // Developer-specific method
    console.log(`${this.name} is coding in ${this.programmingLanguage}`);
  }
}
```

Look at that. Inheritance in classes is declared using the `extends` keyword: `class DeveloperPersonClass extends PersonClass {...}`. This line alone says, "Hey JavaScript, `DeveloperPersonClass` should inherit from `PersonClass`."

Inside the `DeveloperPersonClass` constructor, we have this line: `super(name, age);`. `super()` is crucial for class inheritance. It's how we call the constructor of the parent class (`PersonClass` in this case). When we call `super(name, age)`, it's essentially doing the same thing as `PersonConstructor.call(this, name, age)` in our constructor function example—it's running the `PersonClass` constructor to set up the inherited properties (`name` and `age`) on the `DeveloperPersonClass` object.

After calling `super()`, we can then add any developer-specific properties or methods to our `DeveloperPersonClass`, like `this.programmingLanguage = programmingLanguage;` and the `code()` method.

### Using `DeveloperPersonClass` - Inheritance in Action, Cleaner Syntax

Let's create a `DeveloperPersonClass` object and see inheritance in action with this cleaner syntax:

```js
const classDevPerson1 = new DeveloperPersonClass("Eve", 35, "JavaScript");

console.log(classDevPerson1.name); // Output: Eve (Inherited from PersonClass!)
console.log(classDevPerson1.age); // Output: 35 (Inherited from PersonClass!)
classDevPerson1.greet(); // Output: Hello, I'm Eve (Inherited from PersonClass!)
console.log(classDevPerson1.programmingLanguage); // Output: JavaScript (Developer-specific)
classDevPerson1.code(); // Output: Eve is coding in JavaScript (Developer-specific)
```

It works exactly as expected. `classDevPerson1` inherits `name`, `age`, and `greet()` from `PersonClass` and also has its own `programmingLanguage` and `code()` methods. But the class syntax makes the inheritance relationship much more obvious and easier to work with.

### Classes: Syntactic Sugar, Prototype Power Underneath

Let's be crystal clear again: JavaScript classes are syntactic sugar over prototypes. They are a more user-friendly way to write code that is still based on prototypes and constructor functions behind the scenes.

When you define a class, JavaScript is actually doing these things for you under the hood:

* It's creating a constructor function (like our `PersonConstructor`).
    
* It's setting up the `.prototype` property of that constructor function.
    
* When you use `extends`, it's using `Object.create()` and `call() to` set up the prototype chain for inheritance.
    

Classes don't change the fundamental prototype-based nature of JavaScript OOP. They just give us a more familiar and less verbose syntax to work with it.

### So, Are Classes Just "Fake" Classes?

Some people argue that JavaScript classes are “fake” because they’re merely syntactic sugar. But honestly, that’s not the point at all. Syntactic sugar is awesome—it makes our code easier to read, write, and maintain. For those coming from a class-based language background, classes make object-oriented programming in JavaScript much more approachable and understandable.

The key takeaway is that while classes give you a neat, familiar syntax, you still need to understand the underlying mechanism: prototypes. Classes are just a friendly layer on top of JavaScript’s prototype system.

## What’s Next? More Class Features and Real-World Examples

Alright, now that you’re comfortable with the idea of classes, it’s time to see them in action. Understanding the theory is only half the battle—we need some practical examples.

And to solidify your understanding, let’s walk through building a classic example: a basic to-do list app. While a to-do app is still relatively simple in concept, it introduces enough front-end interaction to see how classes can organize front-end JavaScript code for interactive elements in a manageable way for learning.

Imagine you want to build a really basic to-do app. What do you need to manage?

* To-dos: Each to-do item has a description and a status (done or not).
    
* Actions: You’ll want to add new to-dos, mark them as complete, delete them, and list them.
    

This naturally leads us to think of a “ToDo” item as an object, and if you’re creating many to-do items, a `ToDo` class is a perfect blueprint.

### Setting Up Your Files

Before writing any code, create two files in the same folder:

* `index.html`: This is the webpage structure.
    
* `script.js`: This is where your JavaScript code with classes will live.
    

You can use any text editor (like VS Code, Sublime Text, or even Notepad) to create these files.

### Creating the ToDo Class

Let’s start by building our `ToDo` class. Copy and paste the following code into your `script.js` file:

```javascript
class ToDo {

constructor(description) {

this.description = description; // Every to-do needs a description

this.completed = false; // By default, it's not completed

}

markComplete() {

this.completed = true;

console.log("${this.description}" marked as complete!);

}

// More methods (e.g., for editing the to-do) can be added later.

}
```

Notice how clean that is. The `constructor` sets up the description and completed status for each new to-do item. The `markComplete()` method updates the status and logs a confirmation message.

### Building the ToDoList Class

Next, we’ll build a `ToDoList` class to manage our collection of to-dos. Add the following code to your `script.js` file, below the `ToDo` class:

```javascript
class ToDoList {

constructor() {

this.todos = []; // Start with an empty array of to-dos

}

addTodo(description) {

const newTodo = new ToDo(description); // Create a new ToDo object

this.todos.push(newTodo); // Add it to our list

this.renderTodoList(); // Update the webpage display

}

listTodos() {

return this.todos; // Return the array of todos (for further processing or rendering)

}

markTodoComplete(index) {

if (index >= 0 && index < this.todos.length) {

this.todos[index].markComplete();

this.renderTodoList(); // Update the display after marking complete

}

}

renderTodoList() {

const todoListElement = document.getElementById('todoList');

todoListElement.innerHTML = ''; // Clear the current list in HTML

this.todos.forEach((todo, index) => {

const listItem = document.createElement('li');

listItem.textContent = todo.description;

if (todo.completed) {

listItem.classList.add('completed'); // Add CSS class for styling completed items

}

// Create a "Complete" button for each to-do

const completeButton = document.createElement('button');

completeButton.textContent = 'Complete';

completeButton.onclick = () => this.markTodoComplete(index);

listItem.appendChild(completeButton);

todoListElement.appendChild(listItem);

});

}

}
```

In this class:

* The `constructor` initializes an empty array to hold our to-do items.
    
* `addTodo(description)` creates a new `ToDo` object and adds it to the array, then calls `renderTodoList()` to update the display.
    
* `listTodos()` returns the list of to-dos.
    
* `markTodoComplete(index)` marks a specific to-do as complete and refreshes the display.
    
* `renderTodoList()` finds the HTML element with the ID `todoList`, clears its content, and then creates list items for each to-do, including a “Complete” button.
    

### Creating the HTML Structure

Next, open your `index.html` file and paste in the following HTML code:

```javascript
<!DOCTYPE html>

<html>

<head>

  <title>My Simple To-Do App</title>

  <style>

    /* Simple CSS to style completed items */

    .completed {

      text-decoration: line-through;

      color: gray;

    }

  </style>

</head>

<body>

  <h1>My To-Do List</h1>

  <input type="text" id="todoInput" placeholder="Enter new to-do...">

<button id="addButton">Add To-Do</button>

  <ul id="todoList"></ul>

  <script src="script.js"></script>

</body>

</html>
```

This HTML file sets up:

* A heading for your to-do list.
    
* An input box (with `id="todoInput"`) for entering new to-dos.
    
* An “Add To-Do” button (with `id="addButton"`).
    
* An empty unordered list (with `id="todoList"`) where your to-dos will appear.
    
* A link to the `script.js` file that contains your JavaScript code.
    

### Making It All Work Together

Finally, let’s hook up our HTML elements with our JavaScript. At the bottom of your `script.js` file, add this code:

```js
const myTodoList = new ToDoList(); // Create an instance of ToDoList

// Get references to the HTML elements

const addButton = document.getElementById("addButton");

const todoInput = document.getElementById("todoInput");

// Listen for clicks on the "Add To-Do" button

addButton.addEventListener("click", () => {
  const todoText = todoInput.value.trim(); // Get the text from the input box

  if (todoText) {
    // Only add if the input is not empty

    myTodoList.addTodo(todoText); // Add the new to-do

    todoInput.value = ""; // Clear the input box
  }
});

// Render the to-do list initially (it will be empty to start)

myTodoList.renderTodoList();
```

This code does the following:

* Creates an instance of the `ToDoList` class.
    
* Finds the HTML elements for the input and button.
    
* This code adds an event listener to the HTML button element that has the ID "addButton". This listener is set to react to "click" events on this button. When the "Add To-Do" button is clicked, the code inside the event listener function will execute. This code takes the text that the user has typed into the HTML input field with the ID "todoInput" and adds it as a new to-do item to our list.
    
* Initially renders the to-do list on the webpage.
    

%[https://codepen.io/Spruce_khalifa/pen/vEYBdQe] 

### Your Challenge: Go Proto-Style

Now that you’ve seen how classes can make building this to-do app more structured, here’s a challenge: Try building the same to-do app without using the `class` keyword. Use object literals and prototypes instead. Think about:

* How would you create a `ToDo` “blueprint” using a constructor function and prototypes?
    
* How would you add the `markComplete()` method to the `ToDo` prototype?
    
* How would you structure a `ToDoList` “blueprint” similarly?
    

By building the same app using both approaches, you’ll really understand that classes are just a nicer, more familiar way of writing prototype-based code.

## Conclusion

Congratulations! You’ve built a basic, interactive to-do app using JavaScript classes and HTML. You now see how classes help you organize code and encapsulate related functionality. While classes are just syntactic sugar over prototypes, they make it much easier to write, read, and maintain your code—especially as your applications grow.

Your next step? Experiment with the prototype approach and compare it with the class-based approach. The more you code, the more natural these concepts will become. Happy coding, and keep building cool stuff.

If you have any questions, feel free to find me on Twitter at [@sprucekhalifa](https://x.com/sprucekhalifa), and don’t forget to follow me for more tips and updates. Happy coding!
