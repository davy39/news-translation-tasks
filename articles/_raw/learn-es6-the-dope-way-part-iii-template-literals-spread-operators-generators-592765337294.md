---
title: 'Learn ES6 The Dope Way Part III: Template Literals, Spread Operators, and
  Generators!'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-06-14T08:50:52.000Z'
originalURL: https://freecodecamp.org/news/learn-es6-the-dope-way-part-iii-template-literals-spread-operators-generators-592765337294
coverImage: https://cdn-media-1.freecodecamp.org/images/1*RuxaPPPrL6K09eF4pFhISw.jpeg
tags:
- name: education
  slug: education
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: Tutorial
  slug: tutorial
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Mariya Diminsky

  Welcome to Part III of Learn ES6 The Dope Way, a series created to help you easily
  understand ES6 (ECMAScript 6)!

  Let’s adventure further into ES6 and cover three super valuable concepts:


  Template Literals

  Spread Operators

  Generat...'
---

By Mariya Diminsky

Welcome to Part III of **Learn ES6 The Dope Way**, a series created to help you easily understand ES6 (ECMAScript 6)!

Let’s adventure further into ES6 and cover three super valuable concepts:

* Template Literals
* Spread Operators
* Generators

#### Template Literals

Benefits:

* Easy expression interpolation and method calls! See examples below.
* Including complex information in the format you want is simple!
* You don’t need to worry about multiple quotation marks, multi-lines, spaces, or using “+” sign either! Only two back ticks recognize all the information inside of them! Woohoo!

Beware:

* Commonly called “Template Strings”, as this was their name in prior editions of ES2015 / ES6 specification.
* Variables and parameters need to be wrapper in dollar sign and curly braces, ie. _placeholder_ ${EXAMPLE}.
* The plus sign,“+”, inside of a Template Literal literally acts as a math operation, not a concatenation if also inside ${}. See examples below for further explanation.

#### Migrating to Template Literal Syntax

After reviewing the benefits and items to be aware of, take note of these examples and study the subtle differences with using Template Literals:

```js
// #1
// Before:
function sayHi(petSquirrelName) { console.log('Greetings ' + petSquirrelName + '!'); }
sayHi('Brigadier Sir Nutkins II'); // => Greetings Brigadier Sir Nutkins II!

// After:
function sayHi(petSquirrelName) { console.log(`Greetings ${petSquirrelName}!`); }
sayHi('Brigadier Sir Nutkins II'); // => Greetings Brigadier Sir Nutkins II!

// #2
// Before:
console.log('first text string \n' + 'second text string'); 
// => first text string 
// => second text string

// After:
console.log(`first text string 
second text string`); 
// => first text string 
// => second text string

// #3
// Before:
var num1 = 5;
var num2 = 10;
console.log('She is ' + (num1 + num2) +  ' years old and\nnot ' + (2 * num1 + num2) + '.');
// => She is 15 years old and
// => not 20.

// After:
var num1 = 5;
var num2 = 10;
console.log(`She is ${num1 + num2} years old and\nnot ${2 * num1 + num2}.`);
// => She is 15 years old and
// => not 20.

// #4 
// Before:
var num1 = 12;
var num2 = 8;
console.log('The number of JS MVC frameworks is ' + (2 * (num1 + num2)) + ' and not ' + (10 * (num1 + num2)) + '.');
//=> The number of JS frameworks is 40 and not 200.

// After:
var num1 = 12;
var num2 = 8;
console.log(`The number of JS MVC frameworks is ${2 * (num1 + num2)} and not ${10 * (num1 + num2)}.`);
//=> The number of JS frameworks is 40 and not 200.

// #5
// The ${} works fine with any kind of expression, including method calls:
// Before:
var registeredOffender = {name: 'Bunny BurgerKins'};
console.log((registeredOffender.name.toUpperCase()) + ' you have been arrested for the possession of illegal carrot bits!');
// => BUNNY BURGERKINS you have been arrested for the possession of illegal carrot bits!

// After:
var registeredOffender = {name: 'Bunny BurgerKins'};
console.log(`${registeredOffender.name.toUpperCase()} you have been arrested for the possession of illegal carrot bits!`);
// => BUNNY BURGERKINS you have been arrested for the possession of illegal carrot bits!
```

Let’s checkout an even more complex way of using Template Literals! Look at how easy it is to include all this information without worrying about all the “+” signs, spaces, math logic, and quotation placement! It can be _so_ convenient! Also please note, you will need to include another dollar sign, outside of the placeholder, if printing out prices:

```js
function bunnyBailMoneyReceipt(bunnyName, bailoutCash) {
  var bunnyTip = 100;
  
  console.log(
    `
    Greetings ${bunnyName.toUpperCase()}, you have been bailed out!
    
      Total: $${bailoutCash}
      Tip: $${bunnyTip}
      ------------
      Grand Total: $${bailoutCash + bunnyTip}
    
    We hope you a pleasant carrot nip-free day!  
    
  `
  );

}

bunnyBailMoneyReceipt('Bunny Burgerkins', 200);

// Enter the above code into your console to get this result:
/* 
  Greetings BUNNY BURGERKINS, you have been bailed out!
    
      Total: $200
      Tip: $100
      ------------
      Grand Total: $300
    
    We hope you a pleasant carrot nip-free day! 
*/
```

Wow, so much simpler!! It’s so exciting…Ahh!!

![Image](https://cdn-media-1.freecodecamp.org/images/PLbJ5KyPdRVJmbS-4MXy5XC5eZ5EcHtDw6f4)

#### Spread Operators

If you have multiple arguments in an array that you want to insert into a function call, or multiple arrays and/or array elements that you want to insert into another array seamlessly, use Spread Operators!

Benefits:

* Easily concats arrays inside of other arrays.
* Place the arrays wherever you want inside of that array.
* Easily add arguments into function call.
* Just 3 dots ‘…’ before the array name.
* Similar to _function.apply_ but can be used with the _new_ keyword, while _function.apply_ cannot.

Let’s take a look at a situation where we would want to add several arrays into another main array without using the Spread Operator:

```js
var squirrelNames = ['Lady Nutkins', 'Squirrely McSquirrel', 'Sergeant Squirrelbottom'];
var bunnyNames = ['Lady FluffButt', 'Brigadier Giant'];
var animalNames = ['Lady Butt', squirrelNames, 'Juicy Biscuiteer', bunnyNames];

animalNames;
// => ['Lady Butt', ['Lady Nutkins', 'Squirrely McSquirrel', 'Sergeant Squirrelbottom'], 'Juicy Biscuiteer', ['Lady FluffButt', 'Brigadier Giant']]

// To flatten this array we need another step:
var flattened = [].concat.apply([], animalNames);
flattened;
// => ['Lady Butt', 'Lady Nutkins', 'Squirrely McSquirrel', 'Sergeant Squirrelbottom', 'Juicy Biscuiteer', 'Lady FluffButt', 'Brigadier Giant']

```

With the Spread Operator, your arrays are automatically inserted and concatenated wherever you’d like. No need for any extra steps:

```js
var squirrelNames = ['Lady Nutkins', 'Squirrely McSquirrel', 'Sergeant Squirrelbottom'];
var bunnyNames = ['Lady FluffButt', 'Brigadier Giant'];
var animalNames = ['Lady Butt', ...squirrelNames, 'Juicy Biscuiteer', ...bunnyNames];

animalNames;
// => ['Lady Butt', 'Lady Nutkins', 'Squirrely McSquirrel', 'Sergeant Squirrelbottom', 'Juicy Biscuiteer', 'Lady FluffButt', 'Brigadier Giant']

```

Another useful example:

```js
var values = [25, 50, 75, 100]

// This:
console.log(Math.max(25, 50, 75, 100)); // => 100

// Is the same as this:
console.log(Math.max(...values)); // => 100

/* 
  NOTE: Math.max() typically does not work for arrays unless you write it like:
        Math.max.apply(null, values), but with Spread Operators you can just insert it
        and voila! No need for the .apply() part! Wohoo! :)
*/
```

#### Potentially more useful than .apply()

What if you have multiple arguments to place inside of a function? You could use the good ol’ _Function.prototype.apply_:

```js
function myFunction(x, y, z) {
  console.log(x + y + z)
};
var args = [0, 1, 2];
myFunction.apply(null, args);
// => 3
```

Or use the Spread Operator:

```js
function myFunction(x, y, z) {
  console.log(x + y + z);
}
var args = [0, 1, 2];
myFunction(...args);
// => 3
```

In ES5 it is not possible to compose the _new_ keyword with the _apply_ method. Since the introduction of the Spread Operator syntax, you can now!

```js
var dateFields = readDateFields(database);
var d = new Date(…dateFields);
```

#### Generators

Benefits:

* Allows you to pause functions to be resumed later.
* Easier to create asynchronous functions.
* Used commonly with _setTimeout()_ or _setInterval()_ to time asynchronous events.

Be aware:

* You know you are looking at a generator if you see * and the word _yield_.
* You need to call the function each time so the next function within is called, otherwise it won’t run, unless it’s within a _setInterval()_.
* Result naturally comes out in object form, add ._value_ to get value only.
* Object comes with _done_ property that is set to false until all _yield_ expressions are printed.
* Generators end either when all functions/values have been called or if a _return_ statement is present.

Example:

```js
function* callMe() {
  yield '1';
  yield '…and a 2';
  yield '…and a 3';
  return;
  yield 'this won’t print';
}

var anAction = callMe();

console.log(anAction.next());
//=> { value: ‘1’, done: false }

console.log(anAction.next());
//=> { value: ‘…and a 2’, done: false }

console.log(anAction.next());
//=> { value: ‘…and a 3’, done: false }

console.log(anAction.next());
//=> { value: ‘undefined’, done: true }

console.log(anAction.next());
//=> { value: ‘undefined’, done: true }

// NOTE: To get only the value use anAction.next().value otherwise the entire object will be printed.

```

Generators are super useful when it comes to asynchronous functions calls. Let’s say you have 3 different functions that you’ve stored in an array and you want to call each one after another after a certain amount of time:

```js
// Bunny needs to go grocery shopping for her friend’s birthday party.
var groceries = '';

// Let’s create three functions that need to be called for Bunny.
var buyCarrots = function () {
  groceries += 'carrots';
}

var buyGrass = function () {
  groceries += ', grass';
}

var buyApples = function () {
  groceries += ', and apples';
}

// Bunny is in a hurry so you have to buy the groceries within certain amount of time!
// This is an example of when you would use a timer with a Generator.
// First store the functions within an array:
var buyGroceries = [buyCarrots, buyGrass, buyApples];

// Then loop through the array within a Generator:
// There are some issues doing this with the forEach, recreate this using a for loop.
function* loopThrough(arr) {
  for(var i=0; i<arr.length; i++) {
    yield arr[i]();
  }
}

// add the array of three functions to the loopThrough function.
var functions = loopThrough(buyGroceries);

// Lastly, set the time you want paused before the next function call 
// using the setInterval method(calls a function/expression after a specific set time).
var timedGroceryHunt = setInterval(function() {
  var functionCall = functions.next();
  if(!functionCall.done) {
    console.log(`Bunny bought ${groceries}!`);
  }else {
    clearInterval(timedGroceryHunt);
    console.log(`Thank you! Bunny bought all the ${groceries} in time thanks to your help!`);
  }
}, 1000);

// Enter this code into your console to test it out!
// after 1 second: => Bunny bought carrots!
// after 1 second: => Bunny bought carrots, grass!
// after 1 second: => Bunny bought carrots, grass, and apples!
// after 1 second: => Thank you! Bunny bought all the carrots, grass, and apples in time thanks to your help!

```

This can similarly be accomplished via a _promise_ (an operation that hasn’t completed yet, but is expected in the future) as well. Developers sometimes use promises and Generators together in their code, so it’s good to be aware of both.

Congrats! You’ve made it through **Learn ES6 The Dope Way** Part III and now you’ve acquired three super valuable concepts! You can now safely brush up and make efficient use of Template Literals, Spread Operators, and Generators within your code. Woohoo! Go you!

Although, you might want to wait since there are still browser issues with ES6 and it’s important to use compilers like _Babel_ or a module bundler like _Webpack_ before publishing your code. All of these will be discussed in future editions of **Learn ES6 The Dope Way! Thanks for reading** **❤**

Keep your wisdom updated by liking and following as more **Learn ES6 The Dope Way** is coming soon to Medium!

**[Part I: const, let & var](https://www.freecodecamp.org/news/learn-es6-the-dope-way-i-const-let-var-ae828580472b/)**

**[Part II: (Arrow) => functions and ‘this’ keyword](https://www.freecodecamp.org/news/learn-es6-the-dope-way-part-ii-arrow-functions-and-the-this-keyword-381ac7a32881/)**

**[Part III: Template Literals, Spread Operators & Generators!](https://www.freecodecamp.org/news/learn-es6-the-dope-way-part-iii-template-literals-spread-operators-generators-592765337294/)**

**[Part IV: Default Parameters, Destructuring Assignment, and a new ES6 method!](https://www.freecodecamp.org/news/learn-es6-the-dope-way-part-iv-default-parameters-destructuring-assignment-a-new-es6-method-44393190b8c9/)**

**[Part V: Classes, Transpiling ES6 Code & More Resources!](https://www.freecodecamp.org/news/learn-es6-the-dope-way-part-v-classes-browser-compatibility-transpiling-es6-code-47f62267661/)**

You can also find me on github ❤ [https://github.com/Mashadim](https://github.com/Mashadim)

