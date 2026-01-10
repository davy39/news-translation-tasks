---
title: The Best JavaScript Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-21T17:38:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-example
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f25740569d1a4ca4102.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'JavaScript is the most widely used scripting language on earth. Here are
  some examples of key syntax patterns in JavaScript.

  Argument Example

  The arguments object is an array-like object (in that the structure of the object
  is similar to that of an a...'
---

JavaScript is the most widely used scripting language on earth. Here are some examples of key syntax patterns in JavaScript.

## Argument Example

The arguments object is an **array-like object** _(in that the structure of the object is similar to that of an array; however it should not be considered an array as it has all the functionality of an object)_ that stores all of the arguments that you passed to a function and is proprietary to that function in particular. 

If you were to pass 3 arguments to a function, say `storeNames()`, those 3 arguments would be stored inside an object called **arguments** and it would look like this when we pass the arguments `storeNames("Mulder", "Scully", "Alex Krycek")` to our function:

* First, we declare a function and make it return the arguments object.
* Then, when we execute that function with **n arguments**, 3 in this case, it will return the object to us and it will **look like** an array. We can convert it to an array, but more on that later…

```javascript
function storeNames() { return arguments; }
```

```javascript
// If we execute the following line in the console:
storeNames("Mulder", "Scully", "Alex Kryceck");
// The output will be { '0': 'Mulder', '1': 'Scully', '2': 'Alex Kryceck' }
```

## **Treat it as an array**

You can invoke arguments by using `arguments[n]` (where _n_ is the index of the argument in the array-like object). But if you want to use it as an array for iteration purposes or applying array methods to it, you need to _convert it to an array_ by declaring a variable and using the Array.prototype.slice.call method (because _arguments_ is not an array):

```javascript
var args = Array.prototype.slice.call(arguments);

// or the es6 way:
var args = Array.from(arguments)
```

Since **slice()** has two (the parameter **end** is optional) parameters. You can grab a certain portion of the arguments by specifying the beginning and the ending of your portion (using the _slice.call()_ method renders these two parameters optional, not just _end_). Check out the following code:

```javascript
function getGrades() {
    var args = Array.prototype.slice.call(arguments, 1, 3);
    return args;
}

// Let's output this!
console.log(getGrades(90, 100, 75, 40, 89, 95));

// OUTPUT SHOULD BE: //
// [100, 75] <- Why? Because it started from index 1 and stopped at index 3
// so, index 3 (40) wasn't taken into consideration.
//
// If we remove the '3' parameter, leaving just (arguments, 1) we'd get
// every argument from index 1: [100, 75, 40, 89, 95].
```

### **Optimization issues with Array.slice()**

There is a little problem: it’s not recommended to use slice in the arguments object (optimization reasons)…

**Important**: You should not slice on arguments because it prevents optimizations in JavaScript engines (V8 for example). Instead, try constructing a new array by iterating through the arguments object.

So, what other method is available to convert _arguments_ to an array? I recommend the for-loop (not the for-in loop). You can do it like this:

```javascript
var args = []; // Empty array, at first.
for (var i = 0; i < arguments.length; i++) {
    args.push(arguments[i])
} // Now 'args' is an array that holds your arguments.
```

For more information on the optimization issues: [Optimization Killers: Managing Arguments](https://github.com/petkaantonov/bluebird/wiki/Optimization-killers#3-managing-arguments)

### **ES6 rest parameter as a way to circumvent the arguments object**

In ES2015/ES6 it is possible to use the rest parameter (`...`) instead of the arguments object in most places. Say we have the following function (non-ES6):

```text
function getIntoAnArgument() {
    var args = arguments.slice();
    args.forEach(function(arg) {
        console.log(arg);
    });
}
```

That function can be replaced in ES6 by:

```text
function getIntoAnArgument(...args) {
    args.forEach(arg => console.log(arg));
}
```

Note that we also used an arrow function to shorten the forEach callback!

The arguments object is not available inside the body of an arrow function.

The rest parameter must always come as the last argument in your function definition.  
`function getIntoAnArgument(arg1, arg2, arg3, ...restOfArgs /*no more arguments allowed here*/) { //function body }`

## Arithmetic Operation Example

JavaScript provides the user with five arithmetic operators: `+`, `-`, `*`, `/` and `%`. The operators are for addition, subtraction, multiplication, division and remainder, respectively.

## **Addition**

**Syntax**

`a + b`

**Usage**

```text
2 + 3          // returns 5
true + 2       // interprets true as 1 and returns 3
false + 5      // interprets false as 0 and returns 5
true + "bar"   // concatenates the boolean value and returns "truebar"
5 + "foo"      // concatenates the string and the number and returns "5foo"
"foo" + "bar"  // concatenates the strings and returns "foobar"
```

_Hint:_ There is a handy [increment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Arithmetic_Operators#Increment_() operator that is a great shortcut when you’re adding numbers by 1.

## **Subtraction**

**Syntax**

`a - b`

**Usage**

```text
2 - 3      // returns -1
3 - 2      // returns 1
false - 5  // interprets false as 0 and returns -5
true + 3   // interprets true as 1 and returns 4
5 + "foo"  // returns NaN (Not a Number)
```

_Hint:_ There is a handy [decrement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Arithmetic_Operators#Decrement_(--) operator that is a great shortcut when you’re subtracting numbers by 1.

## **Multiplication**

**Syntax**

`a * b`

**Usage**

```text
2 * 3                // returns 6
3 * -2               // returns -6
false * 5            // interprets false as 0 and returns 0
true * 3             // interprets true as 1 and returns 3
5 * "foo"            // returns NaN (Not a Number)
Infinity * 0         // returns NaN
Infinity * Infinity  // returns Infinity
```

_Hint:_ When making calculations it is possible to use parentheses to prioritize which numbers should be multiplied together.

## **Division**

**Syntax**

`a / b`

**Usage**

```text
3 / 2                // returns 1.5
3.0 / 2/0            // returns 1.5
3 / 0                // returns Infinity
3.0 / 0.0            // returns Infinity
-3 / 0               // returns -Infinity
false / 5            // interprets false as 0 and returns 0
true / 2             // interprets true a 1 and returns 0.5
5 + "foo"            // returns NaN (Not a Number)
Infinity / Infinity  // returns NaN
```

## **Remainder**

**Syntax**

`a % b`

**Usage**

```text
3 % 2          // returns 1
true % 5       // interprets true as 1 and returns 1
false % 4      // interprets false as 0 and returns 0
3 % "bar"      // returns NaN
```

## **Increment**

**Syntax**

`a++ or ++a`

**Usage** 

```js
// Postfix 
x = 3; // declare a variable 
y = x++; // y = 4, x = 3 

// Prefix 
var a = 2; 
b = ++a; // a = 3, b = 3
```

## **Decrement**

**Syntax**

`a-- or --a`

**Usage** 

```js
// Postfix 
x = 3; // declare a variable 
y = x—; // y = 3, x = 3 

// Prefix 
var a = 2; 
b = —a; // a = 1, b = 1
```

_Important:_ As you can see, you **cannot** perform any sort of operations on `Infinity`.

### Arrow Function Example

Arrow functions are a new ES6 syntax for writing JavaScript function expressions. The shorter syntax saves time, as well as simplifying the function scope.

## **What are arrow functions?**

An arrow function expression is a more concise syntax for writing function expressions using a “fat arrow” token (`=>`).

### **The basic syntax**

Below is a basic example of an arrow function:

```javascript
// ES5 syntax
var multiply = function(x, y) {
  return x * y;
};

// ES6 arrow function
var multiply = (x, y) => { return x * y; };

// Or even simpler
var multiply = (x, y) => x * y;    
```

You no longer need the `function` and `return` keywords, or even the curly brackets.

### **A simplified `this`**

Before arrow functions, new functions defined their own `this` value. To use `this` inside a traditional function expression, we have to write a workaround like so:

```javascript
// ES5 syntax
function Person() {
  // we assign `this` to `self` so we can use it later
  var self = this;
  self.age = 0;

  setInterval(function growUp() {
    // `self` refers to the expected object
    self.age++;
  }, 1000);
}
```

An arrow function doesn’t define its own `this` value, it inherits `this` from the enclosing function:

```javascript
// ES6 syntax
function Person(){
  this.age = 0;

  setInterval(() => {
    // `this` now refers to the Person object, brilliant!
    this.age++;
  }, 1000);
}

var p = new Person();
```

## Assignment Operators

## Assignment Operator Example

Assignment operators, as the name suggests, assign (or re-assign) values to a variable. While there are quite a few variations on the assignment operators, they all build off of the basic assignment operator.

Syntax = **y;DescriptionNecessityxVariableRequired=Assignment operatorRequiredyValue to assign to variableRequired**

## **Examples**

```text
let initialVar = 5;   // Variable initialization requires the use of an assignment operator

let newVar = 5;
newVar = 6;   // Variable values can be modified using an assignment operator
```

## **Variations**

The other assignment operators are a shorthand for performing some operation using the variable (indicated by x above) and value (indicated by y above) and then assigning the result to the variable itself.

For example, below is the syntax for the addition assignment operator:

```text
x += y;
```

This is the same as applying the addition operator and reassigning the sum to the original variable (that is, x), which can be expressed by the following code:

```text
x = x + y;
```

To illustrate this using actual values, here is another example of using the addition assignment operator:

```text
let myVar = 5;   // value of myVar: 5
myVar += 7;   // value of myVar: 12 = 5 + 7
```

### Complete list of JavaScript’s assignment operators

Operator | Syntax | Long version  
------------------------------- | --------- | -------------  
Assignment | x = y | x = y  
Addition assignment | x += y | x = x + y  
Subtraction assignment | x -= y | x = x - y  
Multiplication assignment | x *= y | x = x * y  
Division assignment | x /= y | x = x / y  
Remainder assignment | x %= y | x = x % y  
Exponentiation assignment | x \*\*= y | x = x \*\* y  
Left shift assignment | x <<= y | x = x << y  
Right shift assignment | x >>= y | x = x >> y  
Unsigned right shift assignment | x >>>= y | x = x >>> y  
Bitwise AND assignment | x &= y | x = x & y  
Bitwise XOR assignment | x ^= y | x = x ^ y  
Bitwise OR assignment | x \|= y | x = x \| y

## **Boolean Example**

Booleans are a primitive datatype commonly used in computer programming languages. By definition, a boolean has two possible values: `true` or `false`.

In JavaScript, there is often implicit type coercion to boolean. If for example you have an if statement which checks a certain expression, that expression will be coerced to a boolean:

```javascript
var a = 'a string';
if (a) {
  console.log(a); // logs 'a string'
}
```

There are only a few values that will be coerced to false:

* false (not really coerced, as it already is false)
* null
* undefined
* NaN
* 0
* ” (empty string)

All other values will be coerced to true. When a value is coerced to a boolean, we also call that either ‘falsy’ or ‘truthy’.

One way that type coercion is used is with the use of the or (`||`) and and (`&&`) operators:

```javascript
var a = 'word';
var b = false;
var c = true;
var d = 0
var e = 1
var f = 2
var g = null

console.log(a || b); // 'word'
console.log(c || a); // true
console.log(b || a); // 'word'
console.log(e || f); // 1
console.log(f || e); // 2
console.log(d || g); // null
console.log(g || d); // 0
console.log(a && c); // true
console.log(c && a); // 'word'
```

As you can see, the _or_ operator checks the first operand. If this is true or truthy, it returns it immediately (which is why we get ‘word’ in the first case & true in the second case). If it is not true or truthy, it returns the second operand (which is why we get ‘word’ in the third case).

With the and operator it works in a similar way, but for ‘and’ to be true, both operands need to be truthy. So it will always return the second operand if both are true/truthy, otherwise it will return false. That is why in the fourth case we get true and in the last case we get ‘word’.

## **The Boolean Object**

There is also a native JavaScript `Boolean` object that wraps around a value and converts the first parameter to a boolean value. If a value is omitted or falsy –0, -0, `null`, `false`, `NaN`, `undefined`, or an empty string (`""`) – the object's value is false. Pass all other values, including the string `"false"`, and the object's value is set to true.

Note that primitive Boolean values (`true` and `false`) are different than those of the Boolean object.

### More Details

Remember that any object, the value of which is not `undefined` or `null`, evaluates to true if used in a conditional statement. For example, even though this `Boolean` object is explicitly set to false, it evaluates to true and the code is executed:

```javascript
var greeting = new Boolean(false);
if (greeting) {
  console.log("Hello world");
}

// Hello world
```

This doesn't apply to boolean primitives:

```javascript
var greeting = false;
if (greeting) {
  console.log("Hello world"); // code will not run
}
```

To convert a non-boolean value to a boolean, use `Boolean` as a function rather than as an object: 

```javascript
var x = Boolean(expression);     // preferred use as a function
var x = new Boolean(expression); // don't do it this way
```

## Callback Functions

This section gives a brief introduction to the concept and usage of callback functions in JavaScript.

### Functions are Objects

The first thing we need to know is that in JavaScript, functions are first-class objects. As such, we can work with them in the same way we work with other objects, like assigning them to variables and passing them as arguments into other functions. This is important, because it’s the latter technique that allows us to extend functionality in our applications.

## **Callback Function** Example

A **callback function** is a function that is passed _as an argument_ to another function, to be “called back” at a later time. 

A function that accepts other functions as arguments is called a **higher-order function**, which contains the logic for _when_ the callback function gets executed. It’s the combination of these two that allow us to extend our functionality.

To illustrate callbacks, let’s start with a simple example:

```javascript
function createQuote(quote, callback){ 
  var myQuote = "Like I always say, " + quote;
  callback(myQuote); // 2
}

function logQuote(quote){
  console.log(quote);
}

createQuote("eat your vegetables!", logQuote); // 1

// Result in console: 
// Like I always say, eat your vegetables!
```

In the above example, `createQuote` is the higher-order function, which accepts two arguments, the second one being the callback. The `logQuote` function is being used to pass in as our callback function. When we execute the `createQuote` function _(1)_, notice that we are _not appending_ parentheses to `logQuote` when we pass it in as an argument. This is because we do not want to execute our callback function right away, we simply want to pass the function definition along to the higher-order function so that it can be executed later.

Also, we need to ensure that if the callback function we pass in expects arguments,  we supply those arguments when executing the callback _(2)_. In the above example, that would be the `callback(myQuote);`statement, since we know that `logQuote` expects a quote to be passed in.

Additionally, we can pass in anonymous functions as callbacks. The below call to `createQuote` would have the same result as the above example:

```javascript
createQuote("eat your vegetables!", function(quote){ 
  console.log(quote); 
});
```

Incidentally, you don’t _have_ to use the word “callback” as the name of your argument. JavaScript just needs to know that it’s the correct argument name. Based on the above example, the below function will behave in exactly the same manner.

```javascript
function createQuote(quote, functionToCall) { 
  var myQuote = "Like I always say, " + quote;
  functionToCall(myQuote);
}
```

## **Why use Callbacks?**

Most of the time we are creating programs and applications that operate in a **synchronous** manner. In other words, some of our operations are started only after the preceding ones have completed. 

Often when we request data from other sources, such as an external API, we don’t always know _when_ our data will be served back. In these instances we want to wait for the response, but we don’t always want our entire application grinding to a halt while our data is being fetched. These situations are where callback functions come in handy.

Let’s take a look at an example that simulates a request to a server:

```javascript
function serverRequest(query, callback){
  setTimeout(function(){
    var response = query + "full!";
    callback(response);
  },5000);
}

function getResults(results){
  console.log("Response from the server: " + results);
}

serverRequest("The glass is half ", getResults);

// Result in console after 5 second delay:
// Response from the server: The glass is half full!
```

In the above example, we make a mock request to a server. After 5 seconds elapse, the response is modified and then our callback function `getResults` gets executed. To see this in action, you can copy/paste the above code into your browser’s developer tool and execute it.

Also, if you are already familiar with `setTimeout`, then you’ve been using callback functions all along. The anonymous function argument passed into the above example’s `setTimeout` function call is also a callback! So the example’s original callback is actually executed by another callback. Be careful not to nest too many callbacks if you can help it, as this can lead to something called “callback hell”! As the name implies, it isn’t a joy to deal with.

## **JavaScript Class Example**

JavaScript does not have the concept of classes inherently.

But we could simulate the functionalities of a class by taking advantage of the prototypal nature of JavaScript.

This section assumes that you have a basic understanding of [prototypes](https://guide.freecodecamp.org/javascript/prototypes).

For the sake of clarity, let us assume that we want to create a class which can do the following

```javascript
var p = new Person('James','Bond'); // create a new instance of Person class
	p.log() // Output: 'I am James Bond' // Accessing a function in the class
	// Using setters and getters 
	p.profession = 'spy'
	p.profession // output: James bond is a spy
```

### **Using class keyword**

Like in any other programming language, you can now use the `class` keyword to create a class.

This is not supported in older browsers and was introduced in ECMAScript 2015.

`class` is just a syntactic sugar over JavaScript’s existing prototype-based inheritance model.

In general, programmers use the following ways to create a class in JavaScript.

### **Using methods added to prototypes:**

Here, all the methods are added to prototype

```javascript
function Person(firstName, lastName) {
    this._firstName = firstName;
    this._lastName = lastName;
}

Person.prototype.log = function() {
    console.log('I am', this._firstName, this._lastName);
}

// This line adds getters and setters for the profession object. Note that in general you could just write your own get and set functions like the 'log' method above.
// Since in this example we are trying the mimic the class above, we try to use the getters and setters property provided by JavaScript
Object.defineProperty(Person.prototype, 'profession', {
    set: function(val) {
        this._profession = val;
    },
    get: function() {
        console.log(this._firstName, this._lastName, 'is a', this._profession);
    }
})
```

You could also write prototype methods over function `Person` as below:

```javascript
Person.prototype = {
    log: function() {
        console.log('I am ', this._firstName, this._lastName);
    }
    set profession(val) {
        this._profession = val;
    }

    get profession() {
        console.log(this._firstName, this._lastName, 'is a', this._profession);
    }

}
```

### **Using methods added internally**

Here the methods are added internally instead of prototype:

```javascript
function Person(firstName, lastName) {
    this._firstName = firstName;
    this._lastName = lastName;

    this.log = function() {
        console.log('I am ', this._firstName, this._lastName);
    }

    Object.defineProperty(this, 'profession', {
        set: function(val) {
            this._profession = val;
        },
        get: function() {
            console.log(this._firstName, this._lastName, 'is a', this._profession);
        }
    })
}
```

### **Hiding details in classes with symbols**

Most often, some properties and methods have to be hidden to prevent access from outside the function. 

With classes, to obtain this functionality, one way to do this is by using symbols. Symbol is a new built-in type of JavaScript, which can be invoked to give a new symbol value. Every Symbol is unique and can be used as a key on object. 

So one use case of symbols is that you can add something to an object you might not own, and you might not want to collide with any other keys of object. Therefore, creating a new one and adding it as a property to that object using symbol is the safest. Also, when symbol value is added to an object, no one else will know how to get it.

```javascript
class Person {
    constructor(firstName, lastName) {
        this._firstName = firstName;
        this._lastName = lastName;
    }

    log() {
        console.log('I am', this._firstName, this._lastName);
    }

    // setters
    set profession(val) {
        this._profession = val;
    }
    // getters
    get profession() {
        console.log(this._firstName, this._lastName, 'is a', this._profession);
    }
// With the above code, even though we can access the properties outside the function to change their content what if we don't want that.
// Symbols come to rescue.
let s_firstname  = new Symbol();

class Person {
    constructor(firstName, lastName) {
        this[s_firstName] = firstName;
        this._lastName = lastName;
    }

    log() {
        console.log('I am', this._firstName, this._lastName);
    }

    // setters
    set profession(val) {
        this._profession = val;
    }
    // getters
    get profession() {
        console.log(this[s_firstName], this._lastName, 'is a', this._profession);
    }
```

### JavaScript Closure Example

A closure is the combination of a function and the lexical environment (scope) within which that function was declared. Closures are a fundamental and powerful property of Javascript. This section discusses the ‘how’ and ‘why’ about Closures:

### **Example**

```js
//we have an outer function named walk and an inner function named fly

function walk (){
  
  var dist = '1780 feet';
  
  function fly(){
    console.log('At '+dist);
  }
  
  return fly;
}

var flyFunc = walk(); //calling walk returns the fly function which is being assigned to flyFunc
//you would expect that once the walk function above is run
//you would think that JavaScript has gotten rid of the 'dist' var

flyFunc(); //Logs out 'At 1780 feet'
//but you still can use the function as above 
//this is the power of closures
```

### **Another Example**

```js
function by(propName) {
    return function(a, b) {
        return a[propName] - b[propName];
    }
}

const person1 = {name: 'joe', height: 72};
const person2 = {name: 'rob', height: 70};
const person3 = {name: 'nicholas', height: 66};

const arr_ = [person1, person2, person3];

const arr_sorted = arr_.sort(by('height')); // [ { name: 'nicholas', height: 66 }, { name: 'rob', height: 70 },{ name: 'joe', height: 72 } ]
```

The closure ‘remembers’ the environment in which it was created. This environment consists of any local variables that were in-scope at the time the closure was created.

```js
function outside(num) {
  var rememberedVar = num; // In this example, rememberedVar is the lexical environment that the closure 'remembers'
  return function inside() { // This is the function which the closure 'remembers'
    console.log(rememberedVar)
  }
}

var remember1 = outside(7); // remember1 is now a closure which contains rememberedVar = 7 in its lexical environment, and //the function 'inside'
var remember2 = outside(9); // remember2 is now a closure which contains rememberedVar = 9 in its lexical environment, and //the function 'inside'

remember1(); // This now executes the function 'inside' which console.logs(rememberedVar) => 7
remember2(); // This now executes the function 'inside' which console.logs(rememberedVar) => 9 
```

Closures are useful because they let you ‘remember’ data and then let you operate on that data through returned functions. This allows Javascript to emulate private methods that are found in other programming languages. Private methods are useful for restricting access to code as well as managing your global namespace.

### **Private variables and methods**

Closures can also be used to encapsulate private data/methods. Take a look at this example:

```javascript
const bankAccount = (initialBalance) => {
  const balance = initialBalance;

  return {
    getBalance: function() {
      return balance;
    },
    deposit: function(amount) {
      balance += amount;
      return balance;
    },
  };
};

const account = bankAccount(100);

account.getBalance(); // 100
account.deposit(10); // 110
```

In this example, we won’t be able to access `balance` from anywhere outside of the `bankAccount` function, which means we’ve just created a private variable. 

Where’s the closure? Well, think about what `bankAccount()` is returning. It actually returns an Object with a bunch of functions inside it, and yet when we call `account.getBalance()`, the function is able to “remember” its initial reference to `balance`. 

That is the power of the closure, where a function “remembers” its lexical scope (compile time scope), even when the function is executed outside that lexical scope.

### Emulating block-scoped variables

Javascript did not have a concept of block-scoped variables. Meaning that when defining a variable inside a for-loop, for example, this variable was visible from outside the for-loop as well. So how can closures help us solve this problem? Let’s take a look.

```javascript
    var funcs = [];
    
    for(var i = 0; i < 3; i++){
        funcs[i] = function(){
            console.log('My value is ' + i);  //creating three different functions with different param values.
        }
    }
    
    for(var j = 0; j < 3; j++){
        funcs[j]();             // My value is 3
                                // My value is 3
                                // My value is 3
    }
```

Since the variable i does not have block-scope, it’s value within all three functions was updated with the loop counter and created malicious values. Closures can help us solve this issue by creating a snapshot of the environment the function was in when it was created, preserving its state.

```javascript
    var funcs = [];
    
    var createFunction = function(val){
	    return function() {console.log("My value: " + val);};
    }

    for (var i = 0; i < 3; i++) {
        funcs[i] = createFunction(i);
    }
    for (var j = 0; j < 3; j++) {
        funcs[j]();                 // My value is 0
                                    // My value is 1
                                    // My value is 2
    }
```

The later versions of Javascript (ES6+) have a new keyword called let which can be used to give the variable a blockscope. There are also many functions (forEach) and entire libraries (lodash.js) that are dedicated to solving such problems as the ones explained above. They can certainly boost your productivity, however it remains extremely important to have knowledge of all these issues when attempting to create something big.

Closures have many special applications that are useful when creating large Javascript programs.

1. Emulating private variables or encapsulation
2. Making Asynchronous server side calls
3. Creating a block-scoped variable.

### Emulating private variables

Unlike many other languages, Javascript does not have a mechanism which allows you to create encapsulated instance variables within an object. Having public instance variables can cause a lot of problems when building medium to large programs. However with closures, this problem can be mitigated.

Much like in the previous example, you can build functions which return object literals with methods that have access to the object’s local variables without exposing them. Thus, making them effectively private.

Closures can also help you manage your global namespace to avoid collisions with globally shared data. Usually, all global variables are shared between all scripts in your project, which will definitely give you a lot of trouble when building medium to large programs. 

That is why library and module authors use closures to hide an entire module’s methods and data. This is called the module pattern, it uses an immediately invoked function expression which exports only certain functionality to the outside world, significantly reducing the amount of global references.

Here’s a short sample of a module skeleton.

```javascript
var myModule = (function() = {
    let privateVariable = 'I am a private variable';
    
    let method1 = function(){ console.log('I am method 1'); };
    let method2 = function(){ console.log('I am method 2, ', privateVariable); };
    
    return {
        method1: method1,
        method2: method2
    }
}());

myModule.method1(); // I am method 1
myModule.method2(); // I am method 2, I am a private variable
```

Closures are useful for capturing new instances of private variables contained in the ‘remembered’ environment, and those variables can only be accessed through the returned function or methods.

### JavaScript Comment Example

Programmers use comments to add hints, notes, suggestions, or warnings to their source code; they have no effect on the actual output of the code. Comments can be very helpful in explaining the intent of what your code is or should be doing.

It is always best practice when starting out to comment more often than not, as it can help those reading your code to understand what exactly your code is intending to do.

JavaScript has two ways of assigning comments in its code.

The first way is the `//` comment; all text following `//` on the same line into a comment. For example:

```javascript
function hello() {
  // This is a one line JavaScript comment
  console.log("Hello world!");
}
hello();
```

The second way is the `/* */` comment, which can be used for both single-line and multi-line comments. For example:

```javascript
function hello() {
  /* This is a one line JavaScript comment */
  console.log("Hello world!");
}
hello();
```

```javascript
function hello() {
  /* This comment spans multiple lines. Notice
     that we don't need to end the comment until we're done. */
  console.log("Hello world!");
}
hello();
```

You can also prevent execution of Javascript code just commeting the code lines like this:

```javascript
function hello() {
  /*console.log("Hello world!");*/
}
hello();
```

#### **More Information:**

[How To Write Comments in JavaScript](https://www.digitalocean.com/community/tutorials/how-to-write-comments-in-javascript)

### **Many IDEs come with a keyboard shortcut to comment out lines.**

1. Highlight text to be commented
2. Mac: Push Command(Apple Key) & "/"
3. Windows: Push Control & "/"
4. You can also uncomment code by doing the same steps

A shortcut to comment out a section of Javascript in many code editors is to highlight the lines of code you want to comment out, then press `Cmd/Ctrl + /`.

Comments are also very helpful for code testing as you can prevent a certain code-line/block from running:

```javascript
function hello() {
  // The statement below is not going to get executed
  // console.log('hi')
  }
hello();
```

```text
function hello() {
  // The statements below are not going to get executed
  /*
  console.log('hi');
  console.log('code-test');
  */
}
hello();
```

## JavaScript Comparison Operator Example

JavaScript has both **strict** and **type–converting** comparisons.

* The strict comparison (`===`) only evaluates to true if both operands are the same type.
* The abstract comparison (`==`) attempts to convert both operands to the same type before comparing them.
* With relational abstract comparisons (`<=`), both operands are converted to primitives, then to the same type before comparison.
* Strings are compared using Unicode values based on standard ordering.

## **Features of comparisons:**

* Two strings are considered strictly equal when they have the characters in the same sequence and the same length.
* Two numbers are considered strictly equal when they are the both of the type number and are numerically equal. This means that both `0` and `-0` are strictly equal since they both evaluate to `0`. Note that `NaN` is a special value and is not equal to anything, including `NaN`.
* Two Boolean operands are considered strictly equal if both are `true` or `false`.
* Two objects are never considered equal in both strict or abstract comparisons.
* Expressions that compare objects are only considered true if the operands both reference the same exact object instance.
* Null and undefined are both considered strictly equal to themselves (`null === null`) and abstractly equal to each other (`null == undefined`)

## **Equality operators**

### **Equality (==)**

The equality operator first converts operands that are not of the same type, then strictly compares them to one another.

#### **Syntax**

```text
 x == y
```

#### **Examples**

```text
 1   ==  1        // true
"1"  ==  1        // true
 1   == '1'       // true
 0   == false     // true
 0   == null      // false

 0   == undefined   // false
 null  == undefined // true
```

### **Inequality (!=)**

The inequality operator evaluates to true if both operands are not equal. If the operands are not the same type, it will try to convert them to the same type before making the comparison.

#### **Syntax**

```text
x != y
```

#### **Examples**

```text
1 !=   2     // true
1 !=  "1"    // false
1 !=  '1'    // false
1 !=  true   // false
0 !=  false  // false
```

### **Identity / strict equality (===)**

The identity or strict equality operator returns true if both operands are strictly equal in terms of value and type. Unlike the equality operator (`==`), it will not attempt to convert the operands to the same type.

#### **Syntax**

```text
x === y
```

#### **Examples**

```text
3 === 3   // true
3 === '3' // false
```

### **Non-identity / strict inequality (!==)**

The non-identity or strict inequality operator returns true if both operands are not strictly equal in terms of value or type.

#### **Syntax**

```text
x !== y
```

#### **Examples**

```text
3 !== '3' // true
4 !== 3   // true
```

## **Relational operators**

### **Greater than operator (>)**

The greater than operator returns true if the operand on the left is greater than the one on the right.

#### **Syntax**

```text
x > y
```

#### **Examples**

```text
4 > 3 // true
```

### **Greater than or equal operator (>=)**

The greater than or equal operator returns true if the operand on the left is greater than or equal to the one on the right.

#### **Syntax**

```text
x >= y
```

#### **Examples**

```text
4 >= 3 // true
3 >= 3 // true
```

### **Less than operator (<)**

The less than operator returns true if the operand on the left is less than the one on the right.

#### **Syntax**

```text
x < y
```

#### **Examples**

```text
3 < 4 // true
```

### **Less than or equal operator (<=)**

The less than or equal operator returns true if the operand on the left is less than or equal to the one on the right.

#### **Syntax**

```text
x <= y
```

#### **Examples**

```text
3 <= 4 // true
```

## **JavaScript Form Validation Example**

Form validation used to occur at the server, after the client had entered all the necessary data and then pressed the Submit button. If the data entered by a client was incorrect or was simply missing, the server would have to send all the data back to the client and request that the form be resubmitted with correct information. This was really a lengthy process which used to put a lot of burden on the server.

JavaScript provides a way to validate form’s data on the client’s computer before sending it to the web server. Form validation generally performs two functions:

### **Basic Validation**

First of all, the form must be checked to make sure all the mandatory fields are filled in. It just requires a loop through each field in the form to check for data.

### **Data Format Validation**

Secondly, the data that is entered must be checked for correct form and value. Your code must include appropriate logic to test the correctness of the data.

#### **Example:**

```html
<html>
   
   <head>
      <title>Form Validation</title>
      
      <script type="text/javascript">
         <!--
            // Form validation code will come here.
         //-->
      </script>
      
   </head>
   
   <body>
      <form action="/cgi-bin/test.cgi" name="myForm" onsubmit="return(validate());">
         <table cellspacing="2" cellpadding="2" border="1">
            
            <tr>
               <td align="right">Name</td>
               <td><input type="text" name="Name" /></td>
            </tr>
            
            <tr>
               <td align="right">EMail</td>
               <td><input type="text" name="EMail" /></td>
            </tr>
            
            <tr>
               <td align="right">Zip Code</td>
               <td><input type="text" name="Zip" /></td>
            </tr>
            
            <tr>
               <td align="right">Country</td>
               <td>
                  <select name="Country">
                     <option value="-1" selected>[choose yours]</option>
                     <option value="1">USA</option>
                     <option value="2">UK</option>
                     <option value="3">INDIA</option>
                  </select>
               </td>
            </tr>
            
            <tr>
               <td align="right"></td>
               <td><input type="submit" value="Submit" /></td>
            </tr>
            
         </table>
      </form>
      
   </body>
</html>
```

#### **Output**

Have a look [here](https://liveweave.com/LP9eOP).

### **Basic Form Validation**

First let us see how to do a basic form validation. In the above form, we are calling validate() to validate data when the onsubmit event is occurring. The following code shows the implementation of this `validate()`function.

```html
<script type="text/javascript">
   // Form validation code will come here.
   function validate()
      {
      
         if( document.myForm.Name.value == "" )
         {
            alert( "Please provide your name!" );
            document.myForm.Name.focus() ;
            return false;
         }
         
         if( document.myForm.EMail.value == "" )
         {
            alert( "Please provide your Email!" );
            document.myForm.EMail.focus() ;
            return false;
         }
         
         if( document.myForm.Zip.value == "" ||
         isNaN( document.myForm.Zip.value ) ||
         document.myForm.Zip.value.length != 5 )
         {
            alert( "Please provide a zip in the format #####." );
            document.myForm.Zip.focus() ;
            return false;
         }
         
         if( document.myForm.Country.value == "-1" )
         {
            alert( "Please provide your country!" );
            return false;
         }
         return( true );
      }
</script>
```

#### **Output**

Have a look [here](https://liveweave.com/pCPTnP).

### **Data Format Validation**

Now we will see how we can validate our entered form data before submitting it to the web server.

The following example shows how to validate an entered email address. An email address must contain at least an ‘@’ sign and a dot (.). Also, the ‘@’ must not be the first character of the email address, and the last dot must at least be one character after the ‘@’ sign.

#### **Example:**

```html
<script type="text/javascript">
    function validateEmail()
      {
         var emailID = document.myForm.EMail.value;
         atpos = emailID.indexOf("@");
         dotpos = emailID.lastIndexOf(".");
         
         if (atpos < 1 || ( dotpos - atpos < 2 )) 
         {
            alert("Please enter correct email ID")
            document.myForm.EMail.focus() ;
            return false;
         }
         return( true );
      }
</script>
```

#### **Output**

Have a look [here](https://liveweave.com/nznVs6).

### **HTML5 Form Constraints**

Some of the commonly used HTML5 constraints for `<input>` are the `type` attribute (e.g. `type="password"`), `maxlength`, `required` and `disabled`. A less commonly used constraint is the `pattern` attribute that takes a JavaScript regular expression.

## JavaScript If statement example

The `if` statement executes a statement if a specified condition is `true`. If the condition is `false`, another statement can be executed using the `else` statement.

**Note:** The `else` statement is optional.

```javascript
if (condition)
    /* do something */
else
    /* do something else */
```

Multiple `if...else` statements can be chained to create an `else if` clause. This specifies a new condition to test and can be repeated to test multiple conditions, checking until a true statement is presented to execute.

```javascript
if (condition1)
    /* do something */
else if (condition2)
    /* do something else */
else if (condition3)
    /* do something else */
else
    /* final statement */
```

**Note:** If you want to execute more than one statement in the `if`, `else` or `else if` part, curly braces are required around the statements:

```javascript
if (condition) {
    /* do */
    /* something */
    /* with multiple statements */
} else {
    /* do something */
    /* else */
}
```

[MDN link](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else) | [MSDN link](https://msdn.microsoft.com/en-us/library/85yyde5c.aspx)

## **Examples**

**Using** `if...else`:

```javascript
    // If x=5 z=7 and q=42. If x is not 5 then z=19.
    if (x == 5) {
      z = 7;
      q = 42
    else
      z = 19;
```

**Using** `else if`:

```javascript
if (x < 10)
    return "Small number";
else if (x < 50)
    return "Medium number";
else if (x < 100)
    return "Large number";
else {
    flag = 1;
    return "Invalid number";
}
```

## JavaScript Prototype Example

JavaScript is a prototype-based language, therefore understanding the prototype object is one of the most important concepts which JavaScript practitioners need to know. 

This section will give you a short overview of the Prototype object through various examples. Before reading this part, you will need to have a basic understanding of the [`this` reference in JavaScript](https://www.freecodecamp.org/news/the-complete-guide-to-this-in-javascript/).

### **Prototype object**

For the sake of clarity, let’s examine the following example:

```javascript
function Point2D(x, y) {
  this.x = x;
  this.y = y;
}
```

As `Point2D` function is declared, a default property named `prototype` will be created for it (note that, in JavaScript, a function is also an object). 

The `prototype` property is an object which contains a `constructor`property and its value is `Point2D` function: `Point2D.prototype.constructor = Point2D`. And when you call `Point2D` with `new` keyword, _newly created objects will inherit all properties from_ `Point2D.prototype`. 

To check that, you can add a method named `move` into `Point2D.prototype` as follows:

```javascript
Point2D.prototype.move = function(dx, dy) {
  this.x += dx;
  this.y += dy;
}

var p1 = new Point2D(1, 2);
p1.move(3, 4);
console.log(p1.x); // 4
console.log(p1.y); // 6
```

The `Point2D.prototype` is called **prototype object** or **prototype** of `p1` object and for any other object created with `new Point2D(...)` syntax. You can add more properties to `Point2D.prototype` object as you like. The common pattern is to declare methods to `Point2D.prototype` and other properties will be declared in the constructor function.

Built-in objects in JavaScript are constructed in a similar manner. For example:

* Prototype of objects created with `new Object()` or `{}` syntax is `Object.prototype`.
* Prototype of arrays created with `new Array()` or `[]` syntax is `Array.prototype`.
* And so on with other built-in objects such as `Date` and `RegExp`.

`Object.prototype` is inherited by all objects and it has no prototype (its prototype is `null`).

### **Prototype chain**

The prototype chain mechanism is simple: When you access a property `p` on object `obj`, the JavaScript engine will search this property inside `obj` object. If the engine fails to search, it continues searching in the prototype of `obj` object and so on until reaching `Object.prototype`. If after the search has finished, and nothing has been found, the result will be `undefined`. For example:

```javascript
var obj1 = {
  a: 1,
  b: 2
};

var obj2 = Object.create(obj1);
obj2.a = 2;

console.log(obj2.a); // 2
console.log(obj2.b); // 2
console.log(obj2.c); // undefined
```

In above snippet, the statement `var obj2 = Object.create(obj1)` will create `obj2` object with prototype `obj1` object. In other words, `obj1` becomes the prototype of `obj2` instead of `Object.prototype` by default. As you can see, `b` is not a property of `obj2`; you can still access it via the prototype chain. For the `c` property, however, you get an `undefined` value because it can’t be found in `obj1` and `Object.prototype`.

### **Classes**

In ES2016, we now get to use the `Class` keyword as well as the methods mentioned above to manipulate `prototype`. The JavaScript `Class` appeals to developers from OOP backgrounds, but it’s essentially doing the same thing as above.

```javascript
class Rectangle {
  constructor(height, width) {
    this.height = height
    this.width = width
  }

  get area() {
    return this.calcArea()
  }

  calcArea() {
    return this.height * this.width
  }
}

const square = new Rectangle(10, 10)

console.log(square.area) // 100
```

This is basically the same as:

```javascript
function Rectangle(height, width) {
  this.height = height
  this.width = width
}

Rectangle.prototype.calcArea = function calcArea() {
  return this.height * this.width
}
```

The `getter` and `setter` methods in classes bind an Object property to a function that will be called when that property is looked up. It’s just syntactic sugar to help make it easier to _look up_ or _set_ properties.

## JavaScript Scope Example

If you’ve been programming in JavaScript for a while, you’ve undoubtedly run into a concept known as `scope`. What is `scope`? Why should you take the time to learn it?

In programmer speak, `scope` is the **current context of execution**. Confused? Let’s take a look at the following piece of code:

```text
var foo = 'Hi, I am foo!';

var baz = function () {
  var bar = 'Hi, I am bar too!';
    console.log(foo);
}

baz(); // Hi, I am foo!
console.log(bar); // ReferenceError...
```

This is a simple example, but it does a good job of illustrating what is known as _Lexical scope_. JavaScript, and almost every other programming language, has a _Lexical scope_. There is another kind of scope known as _Dynamic scope_, but we won’t be discussing that.

Now, the term _Lexical scope_ sounds fancy, but as you will see it’s really simple in principle. In a Lexical Scope, there are two kinds of scopes: the _global scope_ and a _local scope_.

Before you type the first line of code in your program, a _global scope_ is created for you. This contains all the variables that you declare in your program **outside any functions**.

In the example above, the variable `foo` is in the global scope of the program, while the variable `bar` is declared inside a function and is therefore **in the local scope of that function**.

Let's break down the example line by line. While you might be confused at this point, I promise you will have a much better understanding by the time you finish reading this.

On line 1 we are declaring the variable `foo`. Nothing too fancy here. Let's call this a left-hand size (LHS) reference to `foo`, because we are assigning a value to `foo` and it’s on the left-hand side of the `equal` sign.

On line 3, we are declaring a function and assigning it to variable `baz`. This is another LHS reference to `baz`. We are assigning a value to it (remember, functions are values too!). This function is then called on line 8. This is a RHS, or a right-hand side reference to `baz`. We are retrieving `baz`’s value, which in this case is a function and then invoking it. 

Another RHS reference to `baz` would be if we assigned its value to another variable, for example `foo = baz`. This would be a LHS reference to `foo` and a RHS reference to `baz`.

The LHS and RHS references might sound confusing, but they are important for discussing scope. Think of it this way: a LHS reference is assigning a value to the variable, while a RHS reference is retrieving the value of the variable. They’re just a shorter and more convenient way of saying ‘retrieving the value’ and ‘assigning a value’.

Let’s now break down what’s happening inside the function itself.

When the compiler compiles the code inside a function, it enters the function’s **local scope**.

On line 4, the variable `bar` is declared. This is a LHS reference to `bar`. On the next line, we have a RHS reference to `foo` inside the `console.log()`. Remember, we are retrieving `foo`’s value and then passing it as an argument to the method `console.log()`.

When we have a RHS reference to `foo`, the compiler looks for the declaration of the variable `foo`. The compiler doesn’t find it in the function itself, or the **function’s local scope**, so it **goes up one level: to the global scope**.

At this point you’re probably thinking that scope has something to do with variables. That is correct. A scope can be thought of as a container for variables. All variables that are created within a local scope are only accessible in that local scope. However, all local scopes can access the global scope. (I know you’re probably even more confused right now, but just bear with me for a few more paragraphs).

So the compiler goes up to the global scope to find a LHS reference to the variable `foo`. It finds one on line 1, so it retrieves the value from the LHS reference, which is a string: `'Hi, I am foo!'`. This string is sent to the `console.log()` method, and outputted to the console.

The compiler has finished executing the code inside the function, so we come back out to line 9. On line 9, we have a RHS reference for the variable `bar`.

Now, `bar` was declared in the local scope of `baz`, but there is a RHS reference for `bar` in the global scope. Since there is no LHS reference for `bar` in the global scope, the compiler can’t find a value for `bar` and throws a ReferenceError.

But, you might ask, if the function can look outside itself for variables, or a local scope can peek into the global scope to find LHS references, why can’t the global scope peek into a local scope? Well that’s how lexical scope works!

```text
... // global scope
var baz = function() {
  ... // baz's scope
}
... /// global scope
```

This is the same code from above which illustrates the scope. This forms a sort of hierarchy that goes up to the global scope:

`baz -> global`.

So, if there is a RHS reference for a variable inside `baz`’s scope, it can be fulfilled by a LHS reference for that variable in the global scope. But the opposite is **not true**.

What if we had another function inside `baz`?

```text
... // global scope
var baz = function() {
  ... // baz's scope

  var bar = function() {
     ... // bar's scope.
  }

}
... /// global scope
```

In this case, the hierarchy or the **scope chain** would look like this:

`bar -> baz -> global`

Any RHS references inside `bar`’s local scope can be fulfilled by LHS references in the global scope or `baz`’s scope, but a RHS reference in `baz`’s scope cannot be fulfilled by a LHS reference in `bar`’s scope.

**You can only traverse down a scope chain, not up.**

There are other two important things you should know about JavaScript scopes.

1. Scopes are declared by functions, not by blocks.
2. Functions can be forward-referenced, variables can’t.

Observe (each comment describes scope at the line that it’s written on):

```text
    // outer() is in scope here because functions can be forward-referenced
    
    function outer() {
    
        // only inner() is in scope here
        // because only functions are forward-referenced
    
        var a = 1;
        
        //now 'a' and inner() are in scope
        
        function inner() {
            var b = 2
            
            if (a == 1) {
                var c = 3;
            }
            
            // 'c' is still in scope because JavaScript doesn't care
            // about the end of the 'if' block, only function inner()
        }
        
        // now b and c are out of scope
        // a and inner() are still in scope
        
    }
    
    // here, only outer() is in scope
```

## JavaScript For Loop Example

### **Syntax**

```javascript
for ([initialization]); [condition]; [final-expression]) {
   // statement
}
```

The javascript `for` statement consists of three expressions and a statement:

* initialization - Run before the first execution on the loop. This expression is commonly used to create counters. Variables created here are scoped to the loop. Once the loop has finished its execution, they are destroyed.
* condition - Expression that is checked prior to the execution of every iteration. If omitted, this expression evaluates to true. If it evaluates to true, the loop’s statement is executed. If it evaluates to false, the loop stops.
* final-expression - Expression that is run after every iteration. Usually used to increment a counter. But it can be used to decrement a counter too.
* statement - Code to be repeated in the loop

any of these three expressions or the statement can be omitted. For loops are commonly used to count a certain number of iterations to repeat a statement. Use a `break` statement to exit the loop before the condition expression evaluates to false.

## **Common Pitfalls**

**Exceeding the bounds of an array**

When indexing over an array many times, it is easy to exceed the bounds of the array (ex. try to reference the 4th element of a 3 element array).

```javascript
    // This will cause an error.
    // The bounds of the array will be exceeded.
    var arr = [ 1, 2, 3 ];
    for (var i = 0; i <= arr.length; i++) {
       console.log(arr[i]);
    }

    output:
    1
    2
    3
    undefined
```

There are two ways to fix this code. Set the condition to either `i < arr.length` or `i <= arr.length - 1`

### **Examples**

Iterate through integers from 0-8

```javascript
for (var i = 0; i < 9; i++) {
   console.log(i);
}

output:
0
1
2
3
4
5
6
7
8
```

Break out of a loop before condition expression is false

```javascript
for (var elephant = 1; elephant < 10; elephant+=2) {
    if (elephant === 7) {
        break;
    }
    console.info('elephant is ' + elephant);
}

output:
elephant is 1
elephant is 3
elephant is 5
```

## JavaScript Break Statement Example

The **break** statement terminates the current loop, `switch` or `label` statement and transfers program control to the statement following the terminated statement.

```text
break;
```

If the **break** statement is used in a labeled statement, the syntax is as follows:

```text
break labelName;
```

## **Examples**

The following function has a **break** statement that terminates the `while` loop when **i** is 3, and then returns the value **3 * x**.

```text
function testBreak(x) {
  var i = 0;

  while (i < 6) {
    if (i == 3) {
      break;
    }
    i += 1;
  }

  return i * x;
}
```

In the following example, the counter is set up to count from 1 to 99; however, the **break** statement terminates the loop after 14 counts.

```text
for (var i = 1; i < 100; i++) {
  if (i == 15) {
    break;
  }
}
```

## JavaScript Do While loop example

The `do...while` loop is closely related to the [`while`](http://forum.freecodecamp.com/t/javascript-while-loop/14668) loop. In the do while loop, the condition is checked at the end of the loop.

Here is the **syntax** for `do...while` loop:

## **Syntax:**

```text
 do {

   *Statement(s);*

} while (*condition*);
```

**statement(s):** A statement that is executed **at least once** before the condition or Boolean expression is evaluated and is re-executed each time the condition evaluates to true.

**condition:** Here, a condition is a [Boolean expression](https://www.freecodecamp.org/news/boolean-definition/). If the Boolean expression evaluates to true, the statement is executed again. When the Boolean expression evaluates to false, the loops ends.

## **Example:**

```text
var i = 0;
do {
  i = i + 1;
  console.log(i);
} while (i < 5);

Output:
1
2
3
4
5
```

## JavaScript For In Loop Example

The `for...in` statement iterates over the enumerable properties of an object, in arbitrary order. For each distinct property, statements can be executed.

```text
for (variable in object) {
...
}
```

Required/OptionalParameterDescriptionRequiredVariable: A different property name is assigned to the variable on each iteration. OptionalObject: an object whose enumerable properties are iterated.

## **Examples**

```text
// Initialize object.
a = { "a": "Athens", "b": "Belgrade", "c": "Cairo" }

// Iterate over the properties.
var s = ""
for (var key in a) {
    s += key + ": " + a[key];
    s += "<br />";
    }
document.write (s);

// Output:
// a: Athens
// b: Belgrade
// c: Cairo

// Initialize the array.
var arr = new Array("zero", "one", "two");

// Add a few expando properties to the array.
arr["orange"] = "fruit";
arr["carrot"] = "vegetable";

// Iterate over the properties and elements.
var s = "";
for (var key in arr) {
    s += key + ": " + arr[key];
    s += "<br />";
}

document.write (s);

// Output:
//   0: zero
//   1: one
//   2: two
//   orange: fruit
//   carrot: vegetable

// Efficient way of getting an object's keys using an expression within the for-in loop's conditions
var myObj = {a: 1, b: 2, c:3}, myKeys = [], i=0;
for (myKeys[i++] in myObj);

document.write(myKeys);

//Output:
//   a
//   b
//   c
```

## JavaScript For Of Loop Example

The `for...of` statement creates a loop iterating over iterable objects (including Array, Map, Set, Arguments object and so on), invoking a custom iteration hook with statements to be executed for the value of each distinct property.

```javascript
    for (variable of object) {
        statement
    }
```

Description variable: On each iteration a value of a different property is assigned to the variable.object Object whose enumerable properties are iterated.

## **Examples**

### **Array**

```javascript
    let arr = [ "fred", "tom", "bob" ];

    for (let i of arr) {
        console.log(i);
    }

    // Output:
    // fred
    // tom
    // bob
```

### **Map**

```javascript
    var m = new Map();
    m.set(1, "black");
    m.set(2, "red");

    for (var n of m) {
        console.log(n);
    }

    // Output:
    // 1,black
    // 2,red
```

### **Set**

```javascript
    var s = new Set();
    s.add(1);
    s.add("red");

    for (var n of s) {
        console.log(n);
    }

    // Output:
    // 1
    // red
```

### **Arguments object**

```javascript
    // your browser must support for..of loop
    // and let-scoped variables in for loops

    function displayArgumentsObject() {
        for (let n of arguments) {
            console.log(n);
        }
    }


    displayArgumentsObject(1, 'red');

    // Output:
    // 1
    // red
```

## JavaScript While Loop Example

The while loop starts by evaluating the condition. If the condition is true, the statement(s) is/are executed. If the condition is false, the statement(s) is/are not executed. After that, while loop ends.

Here is the **syntax** for the while loop:

## **Syntax:**

```text
while (condition)

{

  statement(s);

}
```

_statement(s):_ A statement that is executed as long as the condition evaluates to true.

_condition:_ Here, the condition is a Boolean expression which is evaluated before each pass through the loop. If this condition evaluates to true, statement(s) is/are executed. When the condition evaluates to false, execution continues with the statement after the while loop.

## **Example:**

```text
    var i = 1;
    while (i < 10) 
    {
      console.log(i);
       i++; // i=i+1 same thing
    }

    Output:
    1 
    2 
    3 
    4
    5
    6
    7
    8
    9
```

  

