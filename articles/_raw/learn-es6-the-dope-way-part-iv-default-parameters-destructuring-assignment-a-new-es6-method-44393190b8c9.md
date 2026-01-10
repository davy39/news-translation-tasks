---
title: 'Learn ES6 The Dope Way Part IV: Default Parameters, Destructuring Assignment,
  and a new method!'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-06-17T22:09:51.000Z'
originalURL: https://freecodecamp.org/news/learn-es6-the-dope-way-part-iv-default-parameters-destructuring-assignment-a-new-es6-method-44393190b8c9
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

  Welcome to Part IV of Learn ES6 The Dope Way, a series created to help you easily
  understand ES6 (ECMAScript 6)!

  Today let’s explore two new ES6 concepts and introduce a new method!


  Default Function Parameters

  Destructuring Assign...'
---

By Mariya Diminsky

Welcome to Part IV of **Learn ES6 The Dope Way**, a series created to help you easily understand ES6 (ECMAScript 6)!

Today let’s explore two new ES6 concepts and introduce a new method!

* Default Function Parameters
* Destructuring Assignment
* A New ES6 Method ❤

#### Default Function Parameters

Benefits:

* Useful for situations when you need default values in a function.
* When _undefined_ is passed in, it will still use the default value instead!

Beware:

* If you set a function as a default value inside of another function, it will throw a ReferenceError
* The location of your input values, when you call a function, will affect whether you reach the parameter with the default value. For example, if you had two parameters and wanted to reach the second parameter, you would only enter one item in the function you are calling. Since the second parameter would be missing the default value would appear there. See examples below for further explanation.

If you’ve ever wanted to create a function that would have default values as a backup…CONGRATULATIONS! This glorious day has finally arrived!

![Image](https://cdn-media-1.freecodecamp.org/images/ZRTmNPBsvuaLTCz8U0fFrX7mzhY7jZxxvMu4)

Default function parameters allow you to initialize default values if either no values are passed, or if _undefined_ is passed. Before, if you had something like this:

```js
function add(x, y) {
  console.log(x+y);
}
add(); // => NaN
```

You would get _NaN_, not a number. But now you can do this:

```js
function add(x=5, y=7) {
  console.log(x+y);
}
add(); // => 12
```

You get 12! This means if you don’t specifically add values to this function when you call it, it will use the default values. So you can also do this:

```js
function add(x=5, y=7) {
  console.log(x+y);
}
add(12, 15); // => 27
add(); // => 12

// AND THIS:
function haveFun(action='burrowing', time=3) {
  console.log(`I will go ${action} with Bunny for ${time} hours.`)
}
haveFun(); // => I will go burrowing with Bunny for 3 hours.
haveFun('swimming', 2); // => I will go swimming with Bunny for 2 hours.
```

The overwriting of default values will occur based on the position in which you enter your input values when you call the function. For example:

```js
function multiply(a, b = 2) {
  return a*b;
}
multiply(3) // => 6 (returns 3 * 2)
multiply(5, 10) // => 50 (returns 5 * 10 since 10 replaces the default value)
```

When passing undefined values, the default value is still chosen:

```js
// TEST IT HERE: http://goo.gl/f6y1xb
function changeFontColor(elementId, color='blue') {
  document.getElementById(elementId).style.color = color;
}
changeFontColor('title') // => sets title to blue
changeFontColor('title', 'pink') // => sets title to pink
changeFontColor('title', undefined) // => sets title to blue
```

If no default value is assigned for a parameter, it will just return undefined, as normal:

```js
function test(word1='HeyHeyHey', word2) {
  return `${word1} there, ${word2}!`
}
test(); // => HeyHeyHey there, undefined!

// IMPORTANT:
// In order to reach the second parameter and overwrite the default function,
// we need to include the first input as well:
test('Hi', 'Bunny') // => Hi there, Bunny!
```

#### Destructuring Assignment

Benefits:

* Extracts data from arrays and objects and assigns them to variables
* Simplifies the amount of keystrokes needed, and improves readability
* Super useful when needing to pass in large amount of data with the same properties (such as user profiles)

Beware:

* Can be a bit complicated to understand in the beginning, but once you understand its benefits, just review the examples provided and research further. You’ll get the hang of it! :)

Let’s take a step back and learn about Destructuring Assignment, and how it’s used in relation to Arrays, Objects, and even in combination with Default Parameters!

First, let’s practice with arrays by creating an array of Bunny’s favorite food. We _could_ access the first and fifth item in the array the traditional way:

```js
var BunnyFavFoods = ['Carrots', 'Carrot Bits', 'Grass', 'Berries', 'Papaya', 'Apples'];
console.log(BunnyFavFoods[0]) // => Carrots
console.log(BunnyFavFoods[4]) // => Papaya
```

Or we could use Destructuring Assignment! We do this by removing the variable name and passing in a bracket that will point to what items we want in the array when we call it:

```js
var [firstItem, fifthItem] = ['Carrots', 'Carrot Bits', 'Grass', 'Berries', 'Papaya', 'Apples'];
console.log(firstItem) // => Carrots
console.log(fifthItem) // => Carrot Bits
```

Whoa whoa whoa! What just happened? Where is our Papaya?

AHA! Got you there!

![Image](https://cdn-media-1.freecodecamp.org/images/VhvNuGj9otpoPJB9N1vIctw0Dt7yjLG8SgQg)

Check this out — _firstItem_ and _fifthItem_ are just words. The real trick here is where they are placed. The location of the word you place in the brackets will correspond to the location of the item you want in the array.

This is why the first word in the brackets — _firstItem —_ corresponds to the first item in the array ‘_Carrots_’’ and the second word—_fifthItem —_ corresponds to the second item in the array, ‘_Carrot Bits_’.

Here’s how to get access to a different location with the same word:

```js
// Every additional comma added will represent the next item in the array.
var [firstItem,,,,fifthItem] = ['Carrots', 'Carrot Bits', 'Grass', 'Berries', 'Papaya', 'Apples'];
console.log(firstItem) // => Carrots
console.log(fifthItem) // => Papaya

// Wohoo! Let’s try some more! Which item in the array will this get?
var [firstItem,,guessThisItem,,fifthItem] = ['Carrots', 'Carrot Bits', 'Grass', 'Berries', 'Papaya', 'Apples'];
console.log(firstItem) // => Carrots
console.log(guessThisItem) // => Grass
console.log(fifthItem) // => Papaya

// Are you noticing a pattern? One comma separates one word from another and 
// every additional comma before a word represents a place in the array.
// Ok, What would happen if we added a comma to the front?
var [,firstItem,,guessThisItem,,fifthItem] = ['Carrots', 'Carrot Bits', 'Grass', 'Berries', 'Papaya', 'Apples'];
console.log(firstItem) // => Carrot Bits
console.log(guessThisItem) // => Berries
console.log(fifthItem) // => Apples

// Everything moves one place over!
// And what if we moved everything back and added a word to the end?
var [firstItem,,guessThisItem,,fifthItem, whichOneAmI] = ['Carrots', 'Carrot Bits', 'Grass', 'Berries', 'Papaya', 'Apples'];
console.log(firstItem) // => Carrots
console.log(guessThisItem) // => Grass
console.log(fifthItem) // => Papaya
console.log(whichOneAmI) // => Apples
```

Play around with this code in your console so you can better understand this new concept, and tell us all in the comments section what you find. :)

Ok, we’ve got arrays down, so now how about Destructuring Assignment with objects? Let’s first check out the typical way we access items in an object:

```js
var iceCream = {
  cost: 3.99,
  title: 'Ice Cream Flavors',
  type: ['chocolate', 'vanilla', 'caramel', 'strawberry', 'watermelon']
}

console.log(iceCream.cost, iceCream.title, iceCream.type[2]); 
//=> 3.99 ‘Ice Cream Flavors’ ‘caramel’
```

Now let’s destructure this object using a similar approach to what we used with arrays . Take away the variable name and in it’s place, put curly braces — as this is an object — just like we did brackets for arrays.

Inside the curly braces, pass in the object properties that we’ll want access to:

```js
var {cost, title, type} = {
  cost: 3.99,
  title: 'Ice Cream Flavors',
  type: ['chocolate', 'vanilla', 'caramel', 'strawberry', 'watermelon']
}

// VOILA!
console.log(cost, title, type[2]) 
//=> 3.99 'Ice Cream Flavors' 'caramel'
```

Here’s a slightly more complicated but useful way of using Destructuring:

Let’s say you have a function that you want to gain access to all the objects with the same properties but different values. This can be especially useful for large data sets, such as user profiles. But in this example we will use Bunny’s favorite things to make the concept clear:

```js
var iceCream = {
  cost: 3.99,
  name: 'Ice Cream Flavors',
  type: ['chocolate', 'vanilla', 'caramel', 'strawberry', 'watermelon']
}

var sushi = {
  cost: 5.99,
  name: 'Sushi Combinations',
  type: ['Eel Roll', 'Philadelphia Roll', 'Spicy Salmon Handroll', 'Rainbow Roll', 'Special Roll']
}

var fruit = {
  cost: 1.99,
  name: 'Fruits', 
  type: ['cherry', 'watermelon', 'strawberry', 'cantaloupe', 'mangosteen']
}

function favThings({cost, name, type}) {
  var randomNum = Math.floor((Math.random() * 4) + 1);
  console.log(`Bunny loves her ${name}! She especially loves ${type[randomNum]} for only $${cost}!`);
}

// Randomly generated for the type parameter.
// First time:
favThings(iceCream) // => Bunny loves her Ice Cream Flavors! She especially loves caramel for only $3.99!
favThings(sushi) // => Bunny loves her Sushi Combinations! She especially loves Philadelphia Roll for only $5.99!
favThings(fruit) // => Bunny loves her Fruits! She especially loves cantaloupe for only $1.99!

// Second time:
favThings(iceCream) // => Bunny loves her Ice Cream Flavors! She especially loves vanilla for only $3.99!
favThings(sushi) // => Bunny loves her Sushi Combinations! She especially loves Spicy Salmon Handroll for only $5.99!
favThings(fruit) // => Bunny loves her Fruits! She especially loves mangosteen for only $1.99!

// Try it in the console yourself and see what you get!
```

So what just happened?

When we passed in our objects(iceCream, sushi, fruit), the favThings function parsed it and allowed us to access these properties because we used same property names in each object.

#### Combining Destructuring Assignment with Default Parameters

Study the example below:

```js
function profilePage({favColor: favColor} = {favColor: 'vintage pink'}, [name, age] = ['Bunny', 24]) {
  console.log(`My name is ${name}. I am ${age} years old and my favorite color is ${favColor}!`)
}

profilePage(); 
// => My name is Bunny. I am 24 years old and my favorite color is vintage pink!
profilePage({favColor: 'blue'}, ['Ed', 30]) 
// => My name is Ed. I am 30 years old and my favorite color is blue!
```

Or if you had an object and array ready for Destructuring:

```js
var aboutEdward = {
  info: ['Edward', 30],
  favColor: 'blue',
  favSushiRoll: 'Squidy squid squid'
}

function profilePage({favColor} = {favColor: 'vintage pink'}, [name, age] = ['Bunny', 24]) {
  console.log(`My name is ${name}. I am ${age} years old and my favorite color is ${favColor}!`)
}
profilePage(); 
// => My name is Bunny. I am 24 years old and my favorite color is vintage pink!
profilePage(aboutEdward, aboutEdward.info); 
// => My name is Edward. I am 30 years old and my favorite color is blue!
```

#### A New ES6 Method ❤

Benefits:

* Repeat strings without using your own algorithm

Beware:

* Negative numbers and infinity will cause a _RangeError_
* Decimal Numbers will be rounded down to an integer

Ever seen that algorithm, the one that you usually get when you first start learning algorithms and it asks you to repeat a word/string several times?

CONGRATULATIONS!

Your string-repeating-algorithm days are over!

![Image](https://cdn-media-1.freecodecamp.org/images/Gmhzyylidg2RgnlYdMijrfnnyy7Z1zV6rrHV)

Introducing the new _repeat.()_ method brought to you by ES6!

Here’s how it works:

```js
// The general syntax: str.repeat(count);

// Examples:
'Bunny'.repeat(3); // => BunnyBunnyBunny
'Bunny'.repeat(2.5)// => BunnyBunny
'Bunny'.repeat(10/2) // => BunnyBunnyBunnyBunnyBunny
'Bunny'.repeat(-3) // => RangeError: Invalid count value
'Bunny'.repeat(1/0) // => RangeError: Invalid count value
```

Though if you’re reading this and you’re learning algorithms or haven’t started learning them yet, I would highly advise to actually create a function for repeating a string and not using this method since that would defeat the purpose of learning and solving challenges. Once you got it down, go ahead and use this method to your heart’s content. YIPEE!

Congrats! You’ve made it through **Learn ES6 The Dope Way** Part IV and now you’ve acquired two super important ES6 concepts: Default Function Parameters and Destructuring Assignment, as well as learned a fun new method for repeating a string! Yay! Go you!

Remember that if you want to use ES6, there are still browser compatibility issues, so use compilers like _Babel_ or a module bundler like _Webpack_ before publishing your code. All of these will be discussed in future editions of **Learn ES6 The Dope Way! Thanks for reading** **❤**

Keep your wisdom updated by liking and following as more **Learn ES6 The Dope Way** is coming soon to Medium!

**[Part I: const, let & var](https://www.freecodecamp.org/news/learn-es6-the-dope-way-i-const-let-var-ae828580472b/)**

**[Part II: (Arrow) => functions and ‘this’ keyword](https://www.freecodecamp.org/news/learn-es6-the-dope-way-part-ii-arrow-functions-and-the-this-keyword-381ac7a32881/)**

**[Part III: Template Literals, Spread Operators & Generators!](https://www.freecodecamp.org/news/learn-es6-the-dope-way-part-iii-template-literals-spread-operators-generators-592765337294/)**

**[Part IV: Default Parameters, Destructuring Assignment, and a new ES6 method!](https://www.freecodecamp.org/news/learn-es6-the-dope-way-part-iv-default-parameters-destructuring-assignment-a-new-es6-method-44393190b8c9/)**

**[Part V: Classes, Transpiling ES6 Code & More Resources!](https://www.freecodecamp.org/news/learn-es6-the-dope-way-part-v-classes-browser-compatibility-transpiling-es6-code-47f62267661/)**

You can also find me on github ❤ [https://github.com/Mashadim](https://github.com/Mashadim)

