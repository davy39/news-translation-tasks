---
title: Here are examples of everything new in ECMAScript 2016, 2017, and 2018
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-03T06:04:39.000Z'
originalURL: https://freecodecamp.org/news/here-are-examples-of-everything-new-in-ecmascript-2016-2017-and-2018-d52fa3b5a70e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Z-9unq6Am3vekNOa5fD1xg.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By rajaraodv

  It’s hard to keep track of what’s new in JavaScript (ECMAScript). And it’s even
  harder to find useful code examples.

  So in this article, I’ll cover all 18 features that are listed in the TC39’s finished
  proposals that were added in ES201...'
---

By rajaraodv

It’s hard to keep track of what’s new in JavaScript (ECMAScript). And it’s even harder to find useful code examples.

So in this article, I’ll cover all 18 features that are listed in the [TC39’s finished proposals](https://github.com/tc39/proposals/blob/master/finished-proposals.md) that were added in ES2016, ES2017, and ES2018 (final draft) and show them with useful examples.

> This is a pretty long post but should be an easy read. Think of this as “**Netflix binge reading.”** By the end of this, I promise that you’ll have a ton of knowledge about all these features.

#### **OK, let’s go over these one by one.**

![Image](https://cdn-media-1.freecodecamp.org/images/44fYmBIMt2XrYNJgDfEFr5IX0SLCEdnNj2EP)

### `1. Array.prototype.includes`

`includes` is a simple instance method on the Array and helps to easily find if an item is in the Array (including `NaN` unlike `indexOf`).

![Image](https://cdn-media-1.freecodecamp.org/images/0FvN0UrpiwG3vS7AwCxhgFdkmUtRBzsty8Fg)
_ECMAScript 2016 or ES7 — Array.prototype.includes()_

> Trivia: the JavaScript spec people wanted to name it `contains` , but this was apparently already used by Mootools so they used `includes` .

#### `2.` Exponentiation `infix operator`

Math operations like addition and subtraction have infix operators like `+` and `-` , respectively. Similar to them, the `**` infix operator is commonly used for exponent operation. In ECMAScript 2016, the `**` was introduced instead of `Math.pow` .

![Image](https://cdn-media-1.freecodecamp.org/images/gtlnVadz1PTBCP3Quu9KLabgpNI-nC3Bw8-r)
_ECMAScript 2016 or ES7 — ** Exponent infix operator_

![Image](https://cdn-media-1.freecodecamp.org/images/HmFguQSmejxvd4hxOcVsTnWT8XhUoWclGsOj)

### 1. Object.values()

`Object.values()` is a new function that’s similar to `Object.keys()` but returns all the values of the Object’s own properties excluding any value(s) in the prototypical chain.

![Image](https://cdn-media-1.freecodecamp.org/images/8R384SuwAciT2kI9YsAKBh-vxFrSvErxCjWa)
_ECMAScript 2017 (ES8)— Object.values()_

### 2. Object.entries()

`Object.entries()` is related to `Object.keys` , but instead of returning just keys, it returns both keys and values in the array fashion. This makes it very simple to do things like using objects in loops or converting objects into Maps.

**Example 1:**

![Image](https://cdn-media-1.freecodecamp.org/images/1b3wqDqdI1DW2qx9U2aBNjVHkdsK2PHsOfJB)
_ECMAScript 2017 (ES8) — Using Object.entries() in loops_

**Example 2:**

![Image](https://cdn-media-1.freecodecamp.org/images/96Jw9lz3xZ7QUsymo0x73YGz9gfTaNnlUhUd)
_ECMAScript 2017 (ES8) — Using Object.entries() to convert Object to Map_

### 3. String padding

Two instance methods were added to String — `String.prototype.padStart` and `String.prototype.padEnd` — that allow appending/prepending either an empty string or some other string to the start or the end of the original string.

```js
'someString'.padStart(numberOfCharcters [,stringForPadding]); 

'5'.padStart(10) // '         5'
'5'.padStart(10, '=*') //'=*=*=*=*=5'

'5'.padEnd(10) // '5         '
'5'.padEnd(10, '=*') //'5=*=*=*=*='
```

> This comes in handy when we want to align things in scenarios like pretty print display or terminal print.

#### 3.1 padStart example:

In the below example, we have a list of numbers of varying lengths. We want to prepend “0” so that all the items have the same length of 10 digits for display purposes. We can use `padStart(10, '0')` to easily achieve this.

![Image](https://cdn-media-1.freecodecamp.org/images/pDLfNm4KHFG18gimi3kg37nufmeRaqlloadT)
_ECMAScript 2017 — padStart example_

#### 3.2 padEnd example:

`padEnd` really comes in handy when we are printing multiple items of varying lengths and want to right-align them properly.

The example below is a good realistic example of how `padEnd` , `padStart` , and `Object.entries` all come together to produce a beautiful output.

![Image](https://cdn-media-1.freecodecamp.org/images/HvUh0bvyojcU7KfimZiTWoPlHybupuK-Lpaf)
_ECMAScript 2017 — padEnd, padStart and Object.Entries example_

```js
const cars = {
  '?BMW': '10',
  '?Tesla': '5',
  '?Lamborghini': '0'
}

Object.entries(cars).map(([name, count]) => {
  //padEnd appends ' -' until the name becomes 20 characters
  //padStart prepends '0' until the count becomes 3 characters.
  console.log(`${name.padEnd(20, ' -')} Count: ${count.padStart(3, '0')}`)
});

//Prints..
// ?BMW - - - - - - -  Count: 010
// ?Tesla - - - - - -  Count: 005
// ?Lamborghini - - -  Count: 000
```

#### 3.3 ⚠️ padStart and padEnd on Emojis and other double-byte chars

Emojis and other double-byte chars are represented using multiple bytes of unicode. So padStart and padEnd might not work as expected!⚠️

For example: Let’s say we are trying to pad the string `heart` to reach `10` characters with the ❤️ emoji. The result will look like below:

```js
//Notice that instead of 5 hearts, there are only 2 hearts and 1 heart that looks odd!
'heart'.padStart(10, "❤️"); // prints.. '❤️❤️❤heart'
```

This is because ❤️ is 2 code points long (`'\u2764\uFE0F'` )! The word `heart` itself is 5 characters, so we only have a total of 5 chars left to pad. So what happens is that JS pads two hearts using `'\u2764\uFE0F'` and that produces ❤️❤️. For the last one it simply uses the first byte of the heart `\u2764` which produces ❤

So we end up with: `❤️❤️❤heart`

> PS: You may use [this link](https://encoder.internetwache.org/#tab_uni) to check out unicode char conversions.

### 4. `Object.getOwnPropertyDescriptors`

This method returns all the details (including getter `get`and setter `set` methods) for all the properties of a given object. The main motivation to add this is to allow shallow copying / cloning an object into another object that also copies getter and setter functions as opposed to `Object.assign` **.**

**Object.assign shallow copies all the details except getter and setter functions of the original source object.**

The example below shows the difference between `Object.assign` and `Object.getOwnPropertyDescriptors` along with `Object.defineProperties` to copy an original object `Car` into a new object `ElectricCar` . You’ll see that by using `Object.getOwnPropertyDescriptors` ,`discount` getter and setter functions are also copied into the target object.

BEFORE…

![Image](https://cdn-media-1.freecodecamp.org/images/7ZlAkKKdplx53IOn-jYMIPLdZSq90XhAP5jR)
_Before — Using Object.assign_

AFTER…

![Image](https://cdn-media-1.freecodecamp.org/images/23g3sL3-pFGkRri0wOT3g3N2Qzn-oDcKjxVB)
_ECMAScript 2017 (ES8) — Object.getOwnPropertyDescriptors_

```js
var Car = {
 name: 'BMW',
 price: 1000000,
 set discount(x) {
  this.d = x;
 },
 get discount() {
  return this.d;
 },
};

//Print details of Car object's 'discount' property
console.log(Object.getOwnPropertyDescriptor(Car, 'discount'));
//prints..
// { 
//   get: [Function: get],
//   set: [Function: set],
//   enumerable: true,
//   configurable: true
// }

//Copy Car's properties to ElectricCar using Object.assign
const ElectricCar = Object.assign({}, Car);

//Print details of ElectricCar object's 'discount' property
console.log(Object.getOwnPropertyDescriptor(ElectricCar, 'discount'));
//prints..
// { 
//   value: undefined,
//   writable: true,
//   enumerable: true,
//   configurable: true 
// }
//⚠️Notice that getters and setters are missing in ElectricCar object for 'discount' property !??

//Copy Car's properties to ElectricCar2 using Object.defineProperties 
//and extract Car's properties using Object.getOwnPropertyDescriptors
const ElectricCar2 = Object.defineProperties({}, Object.getOwnPropertyDescriptors(Car));

//Print details of ElectricCar2 object's 'discount' property
console.log(Object.getOwnPropertyDescriptor(ElectricCar2, 'discount'));
//prints..
// { get: [Function: get],  ??????
//   set: [Function: set],  ??????
//   enumerable: true,
//   configurable: true 
// }
// Notice that getters and setters are present in the ElectricCar2 object for 'discount' property!
```

### 5. `Add trailing commas in the function parameters`

This is a minor update that allows us to have trailing commas after the last function parameter. Why? To help with tools like git blame to ensure only new developers get blamed.

The below example shows the problem and the solution.

![Image](https://cdn-media-1.freecodecamp.org/images/KyY6NFFjMTOeAITlQNt-kKtE9q9E33vZrBbk)
_ECMAScript 2017 (ES 8) — Trailing comma in function parameter_

> Note: You can also call functions with trailing commas!

### 6. Async/Await

This, by far, is the most important and most useful feature if you ask me. Async functions allows us to not deal with callback hell and make the entire code look simple.

The `async` keyword tells the JavaScript compiler to treat the function differently. The compiler pauses whenever it reaches the `await` keyword within that function. It assumes that the expression after `await` returns a promise and waits until the promise is resolved or rejected before moving further.

In the example below, the `getAmount` function is calling two asynchronous functions `getUser` and `getBankBalance` . We can do this in promise, but using `async await` is more elegant and simple.

![Image](https://cdn-media-1.freecodecamp.org/images/JYCOVItTbISYtWjgbt2lDVdyk8KOOjYVk2sc)
_ECMAScript 2017 (ES 8) — Async Await basic example_

#### **6.1** Async functions themselves return a Promise.

If you are waiting for the result from an async function, you need to use Promise’s `then` syntax to capture its result.

In the following example, we want to log the result using `console.log` but not within the doubleAndAdd. So we want to wait and use `then` syntax to pass the result to `console.log` .

![Image](https://cdn-media-1.freecodecamp.org/images/xnz7tfy5QVKp9VXjcVjqUoMXDwHZuGFX8rd1)
_ECMAScript 2017 (ES 8) — Async Await themselves returns Promise_

#### **6.2 Calling async/await in parallel**

In the previous example we are calling await twice, but each time we are waiting for one second (total 2 seconds). Instead we can parallelize it since `a` and `b` are not dependent on each other using `Promise.all`.

![Image](https://cdn-media-1.freecodecamp.org/images/kWJN5r5sz0F5o2XIpO1qmspgT1BujE0YTTtk)
_ECMAScript 2017 (ES 8) — Using Promise.all to parallelize async/await_

#### 6.3 Error handling async/await functions

There are various ways to handle errors when using async await.

#### **Option 1 — Use try catch within the function**

![Image](https://cdn-media-1.freecodecamp.org/images/PfUYa9Vo5hTFbCHaE5XnaiPjuV4VmUNVWtVh)
_ECMAScript 2017 — **Use try catch within the async/await function**_

```js
//Option 1 - Use try catch within the function
async function doubleAndAdd(a, b) {
 try {
  a = await doubleAfter1Sec(a);
  b = await doubleAfter1Sec(b);
 } catch (e) {
  return NaN; //return something
 }
return a + b;
}

//?Usage:
doubleAndAdd('one', 2).then(console.log); // NaN
doubleAndAdd(1, 2).then(console.log); // 6

function doubleAfter1Sec(param) {
 return new Promise((resolve, reject) => {
  setTimeout(function() {
   let val = param * 2;
   isNaN(val) ? reject(NaN) : resolve(val);
  }, 1000);
 });
}
```

#### **Option 2— Catch every await expression**

Since every `await` expression returns a Promise, you can catch errors on each line as shown below.

![Image](https://cdn-media-1.freecodecamp.org/images/wGCb4bAga1z9mkI1FwKRhYFugCL00pUTeavM)
_ECMAScript 2017 — **Use try catch every await expression**_

```js
//Option 2 - *Catch* errors on  every await line
//as each await expression is a Promise in itself
async function doubleAndAdd(a, b) {
 a = await doubleAfter1Sec(a).catch(e => console.log('"a" is NaN')); // ?
 b = await doubleAfter1Sec(b).catch(e => console.log('"b" is NaN')); // ?
 if (!a || !b) {
  return NaN;
 }
 return a + b;
}

//?Usage:
doubleAndAdd('one', 2).then(console.log); // NaN  and logs:  "a" is NaN
doubleAndAdd(1, 2).then(console.log); // 6

function doubleAfter1Sec(param) {
 return new Promise((resolve, reject) => {
  setTimeout(function() {
   let val = param * 2;
   isNaN(val) ? reject(NaN) : resolve(val);
  }, 1000);
 });
}
```

#### **Option 3 — Catch the entire async-await function**

![Image](https://cdn-media-1.freecodecamp.org/images/bYcQiaVTX1wRzOGg0Vh13TYg5WW8qSVu0DS6)
_ECMAScript 2017 — **Catch the entire async/await function at the end**_

```js
//Option 3 - Dont do anything but handle outside the function
//since async / await returns a promise, we can catch the whole function's error
async function doubleAndAdd(a, b) {
 a = await doubleAfter1Sec(a);
 b = await doubleAfter1Sec(b);
 return a + b;
}

//?Usage:
doubleAndAdd('one', 2)
.then(console.log)
.catch(console.log); // ???<------- use "catch"

function doubleAfter1Sec(param) {
 return new Promise((resolve, reject) => {
  setTimeout(function() {
   let val = param * 2;
   isNaN(val) ? reject(NaN) : resolve(val);
  }, 1000);
 });
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/G9wavF5qssi1AP4C2lF9WgiQ7Hm766eWGt6J)

> ECMAScript is currently in final draft and will be out in June or July 2018. All the features covered below are in Stage-4 and will be part of ECMAScript 2018.

#### 1. [Shared memory and atomics](https://github.com/tc39/ecmascript_sharedmem)

This is a huge, pretty advanced feature and is a core enhancement to JS engines.

**The main idea is to bring some sort of multi-threading feature to JavaScript so that JS developers can write high-performance, concurrent programs in the future by allowing to manage memory by themselves instead of letting JS engine manage memory.**

This is done by a new type of a global object called [SharedArrayBuffer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SharedArrayBuffer) that essentially stores data in a **_shared_** **memory space**. So this data can be shared between the main JS thread and web-worker threads.

Until now, if we want to share data between the main JS thread and web-workers, we had to copy the data and send it to the other thread using `postMessage` . Not anymore!

You simply use SharedArrayBuffer and the data is instantly accessible by both the main thread and multiple web-worker threads.

But sharing memory between threads can cause race conditions. To help avoid race conditions, the “[_Atomics_](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Atomics)” global object is introduced. _Atomics_ provides various methods to lock the shared memory when a thread is using its data. It also provides methods to update such data in that shared memory safely.

> The recommendation is to use this feature via some library, but right now there are no libraries built on top of this feature.

If you are interested, I recommend reading:

1. [_From Workers to Shared Memor_](http://lucasfcosta.com/2017/04/30/JavaScript-From-Workers-to-Shared-Memory.html)_y — [lucasfcosta](http://lucasfcosta.com/)_
2. [_A cartoon intro to SharedArrayBuffers_](https://hacks.mozilla.org/category/code-cartoons/a-cartoon-intro-to-sharedarraybuffers/) _— [Lin Clark](https://www.freecodecamp.org/news/here-are-examples-of-everything-new-in-ecmascript-2016-2017-and-2018-d52fa3b5a70e/undefined)_
3. [_Shared memory and atomics_](http://2ality.com/2017/01/shared-array-buffer.html) _— [Dr. Axel Rauschmayer](http://rauschma.de/)_

#### 2. Tagged Template literal restriction removed

First, we need to clarify what a “Tagged Template literal” is so we can understand this feature better.

In ES2015+, there is a feature called a tagged template literal that allows developers to customize how strings are interpolated. For example, in the standard way strings are interpolated like below…

![Image](https://cdn-media-1.freecodecamp.org/images/qijvAdivaNWMbUMxVg4rer3K1BWYl7bbCcO5)

In the tagged literal, you can write a function to receive the hardcoded parts of the string literal, for example `[ ‘Hello ‘, ‘!’ ]` , and the replacement variables, for example,`[ 'Raja']` , as parameters into a custom function (for example `greet` ), and return whatever you want from that custom function.

The below example shows that our custom “Tag” function `greet` appends time of the day like “Good Morning!” “Good afternoon,” and so on depending on the time of the day to the string literal and returns a custom string.

![Image](https://cdn-media-1.freecodecamp.org/images/aRMqlDhbYudFqPvnNhfrPYkyKXgTkaEn87t0)
_Tag function example that shows custom string interpolation_

```js
//A "Tag" function returns a custom string literal.
//In this example, greet calls timeGreet() to append Good //Morning/Afternoon/Evening depending on the time of the day.

function greet(hardCodedPartsArray, ...replacementPartsArray) {
 console.log(hardCodedPartsArray); //[ 'Hello ', '!' ]
 console.log(replacementPartsArray); //[ 'Raja' ]
    
let str = '';
 hardCodedPartsArray.forEach((string, i) => {
  if (i < replacementPartsArray.length) {
   str += `${string} ${replacementPartsArray[i] || ''}`;
  } else {
   str += `${string} ${timeGreet()}`; //<-- append Good morning/afternoon/evening here
  }
 });
 return str;
}

//?Usage:
const firstName = 'Raja';
const greetings = greet`Hello ${firstName}!`; //??<-- Tagged literal

console.log(greetings); //'Hello  Raja! Good Morning!' ?

function timeGreet() {
 const hr = new Date().getHours();
 return hr < 12
  ? 'Good Morning!'
  : hr < 18 ? 'Good Afternoon!' : 'Good Evening!';
}
```

Now that we discussed what “Tagged” functions are, many people want to use this feature in different domains, like in Terminal for commands and HTTP requests for composing URIs, and so on.

#### ⚠️The problem with Tagged String literal

The problem is that ES2015 and ES2016 specs doesn’t allow using escape characters like “\u” (unicode), “\x”(hexadecimal) unless they look exactly like `\u00A9` or \u{2F804} or \xA9.

So if you have a Tagged function that internally uses some other domain’s rules (like Terminal’s rules), that may need to use **\ubla123abla** that doesn’t look like \u0049 or \u{@F804}, then you would get a syntax error.

In ES2018, the rules are relaxed to allow such seemingly invalid escape characters as long as the Tagged function returns the values in an object with a “cooked” property (where invalid characters are “undefined”), and then a “raw” property (with whatever you want).

```js
function myTagFunc(str) { 
 return { "cooked": "undefined", "raw": str.raw[0] }
} 

var str = myTagFunc `hi \ubla123abla`; //call myTagFunc

str // { cooked: "undefined", raw: "hi \\unicode" }
```

### 3. “dotall” flag for Regular expression

Currently in RegEx, although the dot(“.”) is supposed to match a single character, it doesn’t match new line characters like `\n \r \f etc`.

For example:

```js
//Before
/first.second/.test('first\nsecond'); //false
```

This enhancement makes it possible for the dot operator to match any single character. In order to ensure this doesn’t break anything, we need to use `\s` flag when we create the RegEx for this to work.

```js
//ECMAScript 2018
/first.second/s.test('first\nsecond'); //true   Notice: /s ??  
```

Here is the overall API from the [proposal](https://github.com/tc39/proposal-regexp-dotall-flag) doc:

![Image](https://cdn-media-1.freecodecamp.org/images/leiiozJApb5rPA97rUqBOvzvEtVguXtPcOrk)
_ECMAScript 2018 — Regex dotAll feature allows matching even \n via “.” via /s flag_

### 4. RegExp Named Group Captures ?

This enhancement brings a useful RegExp feature from other languages like Python, Java and so on called “Named Groups.” This features allows developers writing RegExp to provide names (identifiers) in the format`(?<name>...)` for different parts of the group in the RegExp. They can then use that name to grab whichever group they need with ease.

#### 4.1 Basic Named group example

In the below example, we are using `(?<year>) (?<month>) and (?<day>)` names to group different parts of the date RegEx. The resulting object will now contain a `groups` property with properties `year`, `month` , and `day` with corresponding values.

![Image](https://cdn-media-1.freecodecamp.org/images/TkGEzq1zFYdE-YP8YJadJ7VacNhF9gsyf7FB)
_ECMAScript 2018 — Regex named groups example_

#### **4.2 Using Named groups inside regex itself**

We can use the `\k<group name>` format to back reference the group within the regex itself. The following example shows how it works.

![Image](https://cdn-media-1.freecodecamp.org/images/hc1rRx9L0IPX0BG0CGtqUWIRf2KRAHC-5P7R)
_ECMAScript 2018 — Regex named groups back referencing via \k&lt;group name&gt;_

#### **4.3 Using named groups in String.prototype.replace**

The named group feature is now baked into String’s `replace` instance method. So we can easily swap words in the string.

For example, change “firstName, lastName” to “lastName, firstName”.

![Image](https://cdn-media-1.freecodecamp.org/images/bQvxKQY6VfUNRGjeAsCXm0EJEDCbgPe0ti0S)
_ECMAScript 2018 — Using RegEx’s named groups feature in replace function_

### 5. Rest properties for Objects

Rest operator `...` (three dots) allows us to extract Object properties that are not already extracted.

#### **5.1 You can use rest to help extract only properties you want**

![Image](https://cdn-media-1.freecodecamp.org/images/WBZ31BCucgiEXjxal3IkEEdHFbkk3PwpbzGF)
_ECMAScript 2018 — Object destructuring via rest_

#### **5.2 Even better, you can remove unwanted items! ??**

![Image](https://cdn-media-1.freecodecamp.org/images/jMNJhSOaReoiWi9Z6LZdQYmxT0aVHedQiRKO)
_ECMAScript 2018 — Object destructuring via rest_

### **6. Spread properties for Objects**

**Spread properties also look just like rest properties with three dots `...` but the difference is that you use spread to create (restructure) new objects.**

> **Tip: the spread operator is used in the right side of the equals sign. The rest are used in the left-side of the equals sign.**

![Image](https://cdn-media-1.freecodecamp.org/images/Kw63nZhNAIkprEucTKQou35zzTDcvoXenX4D)
_ECMAScript 2018 — Object restructuring via spread_

### **7. RegExp Lookbehind Assertions**

This is an enhancement to the RegEx that allows us to ensure some string exists immediately *_before*_ some other string.

You can now use a group `(?<=…)` _(question mark, less than, equals)_ to look behind for positive assertion.

Further, you can use `(?<!…)` _(question mark, less than, exclamation)_, to look behind for a negative assertion. Essentially this will match as long as the -ve assertion passes.

**Positive Assertion:** Let’s say we want to ensure that the `#` sign exists before the word `winning` (that is: `#winning`) and want the regex to return just the string “winning”. Here is how you’d write it.

![Image](https://cdn-media-1.freecodecamp.org/images/sz6nM4Fzby9XVG96i8eUCvzoE705bGAEeHb7)
_ECMAScript 2018 — `(?&lt;=…) for positive assertion`_

**Negative Assertion:** Let’s say we want to extract numbers from lines that have € signs and not $ signs before those numbers.

![Image](https://cdn-media-1.freecodecamp.org/images/KA-ZXAVf2GOH65G1ndEwkkl7fEFyTaxWDPlL)
_ECMAScript 2018 — (?&lt;!…) for negative assertions_

### **8. [RegExp Unicode Property Escapes](https://github.com/tc39/proposal-regexp-unicode-property-escapes)**

It was not easy to write RegEx to match various unicode characters. Things like `\w` , `\W` , `\d` etc only match English characters and numbers. But what about numbers in other languages like Hindi, Greek, and so on?

That’s where Unicode Property Escapes come in. **It turns out Unicode adds metadata properties for each symbol (character) and uses it to group or characterize various symbols.**

For example, Unicode database groups all Hindi characters(हिन्दी) under a property called `Script` with value `Devanagari` and another property called `Script_Extensions` with the same value `Devanagari`. So we can search for `Script=Devanagari` and get all Hindi characters.

_[Devanagari](https://en.wikipedia.org/wiki/Devanagari_(Unicode_block)) can be used for various Indian languages like Marathi, Hindi, Sanskrit, and so on._

Starting in ECMAScript 2018, we can use `\p` to escape characters along with `{Script=Devanagari}` to match all those Indian characters. **That is, we can use:** `**\p{Script=Devanagari}**` **in the RegEx to match all Devanagari characters.**

![Image](https://cdn-media-1.freecodecamp.org/images/zCjtuGGGmBvzUO9b2cCdqraXfEavM4KrQBhN)
_ECMAScript 2018 — showing \p_

```js
//The following matches multiple hindi character
/^\p{Script=Devanagari}+$/u.test('हिन्दी'); //true  
//PS:there are 3 hindi characters h
```

Similarly, Unicode database groups all Greek characters under `Script_Extensions` (and `Script` ) property with the value `Greek` . So we can search for all Greek characters using `Script_Extensions=Greek` or `Script=Greek` .

**That is, we can use:** `**\p{Script=Greek}**` **in the RegEx to match all Greek characters.**

![Image](https://cdn-media-1.freecodecamp.org/images/hXu3bf5S3R68S0NgqCY6qpBP69HdAShaJdgx)
_ECMAScript 2018 — showing \p_

```js
//The following matches a single Greek character
/\p{Script_Extensions=Greek}/u.test('π'); // true
```

Further, the Unicode database stores various types of Emojis under the boolean properties `Emoji`, `Emoji_Component`, `Emoji_Presentation`, `Emoji_Modifier`, and `Emoji_Modifier_Base` with property values as `true`. So we can search for all Emojis by simply selecting `Emoji` to be true.

**That is, we can use:** `**\p{Emoji}**` **,**`**\Emoji_Modifier**` **and so on to match various kinds of Emojis.**

The following example will make it all clear.

![Image](https://cdn-media-1.freecodecamp.org/images/hp2GXlB3IanbeH9m1fEOzXglZJiofBKUxdY6)
_ECMAScript 2018 — showing how \p can be used for various emojis_

```js
//The following matches an Emoji character
/\p{Emoji}/u.test('❤️'); //true

//The following fails because yellow emojis don't need/have Emoji_Modifier!
/\p{Emoji}\p{Emoji_Modifier}/u.test('✌️'); //false

//The following matches an emoji character\p{Emoji} followed by \p{Emoji_Modifier}
/\p{Emoji}\p{Emoji_Modifier}/u.test('✌?'); //true

//Explaination:
//By default the victory emoji is yellow color.
//If we use a brown, black or other variations of the same emoji, they are considered
//as variations of the original Emoji and are represented using two unicode characters.
//One for the original emoji, followed by another unicode character for the color.
//
//So in the below example, although we only see a single brown victory emoji,
//it actually uses two unicode characters, one for the emoji and another
// for the brown color.
//
//In Unicode database, these colors have Emoji_Modifier property.
//So we need to use both \p{Emoji} and \p{Emoji_Modifier} to properly and
//completely match the brown emoji.
/\p{Emoji}\p{Emoji_Modifier}/u.test('✌?'); //true
```

**Lastly, we can use capital "P”(**`\P` **) escape character instead of small p (**`\p` )**, to negate the matches.**

References:

1. [_ECMAScript 2018 Proposal_](https://mathiasbynens.be/notes/es-unicode-property-escapes)
2. [_https://mathiasbynens.be/notes/es-unicode-property-escapes_](https://mathiasbynens.be/notes/es-unicode-property-escapes)

### **8. Promise.prototype.finally()**

`finally()` is a new instance method that was added to Promise. The main idea is to allow running a callback after either `resolve` or `reject` to help clean things up. The `**finally**` **callback is called without any value and is always executed no matter what.**

Let’s look at various cases.

![Image](https://cdn-media-1.freecodecamp.org/images/yQ99TgkxFshSnmlQqdfFMM73kQcxAcKH2VHl)
_ECMAScript 2018 — finally() in resolve case_

![Image](https://cdn-media-1.freecodecamp.org/images/KlH72OCk03Fj3AXXtaB-gXVnxDFKEtWz7nUp)
_ECMAScript 2018 — finally() in reject case_

![Image](https://cdn-media-1.freecodecamp.org/images/WFFh7DJihhy4C2bGH86n2g5bZ9vyoNu1h7WU)
_ECMASCript 2018 — finally() in Error thrown from Promise case_

![Image](https://cdn-media-1.freecodecamp.org/images/Y34QmvZuh3kYeob2HC3W4fFXB2fFkpRLvfND)
_**ECMAScript 2018 — Error thrown from within **catch** case**_

### **9. Asynchronous Iteration**

This is an *extremely* useful feature. Basically it allows us to create loops of async code with ease!

This feature adds a new **“for-await-of”** loop that allows us to call async functions that return promises (or Arrays with a bunch of promises) in a loop. The cool thing is that the loop waits for each Promise to resolve before doing to the next loop.

![Image](https://cdn-media-1.freecodecamp.org/images/XAZiwAIhT8JdwhA5y7GMP8Dm4oJ1tyqsI5Qo)
_ECMAScript 2018 — Async Iterator via for-await-of_

That’s pretty much it!

If this was useful, please click the clap ? button down below a few times to show your support! ⬇⬇⬇ ??

### My Other Posts

**[_https://medium.com/@rajaraodv/latest_](https://medium.com/@rajaraodv/latest)**

#### **Related ECMAScript 2015+ posts**

1. **[_Check out these useful ECMAScript 2015 (ES6) tips and tricks_](https://medium.freecodecamp.org/check-out-these-useful-ecmascript-2015-es6-tips-and-tricks-6db105590377)**
2. **[_5 JavaScript “Bad” Parts That Are Fixed In ES6_](https://medium.com/@rajaraodv/5-javascript-bad-parts-that-are-fixed-in-es6-c7c45d44fd81#.7e2s6cghy)**
3. **[_Is “Class” In ES6 The New “Bad” Part?_](https://medium.com/@rajaraodv/is-class-in-es6-the-new-bad-part-6c4e6fe1ee65#.4hqgpj2uv)**

