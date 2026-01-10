---
title: JavaScript Concepts to Know Before Learning React
subtitle: ''
author: Musab Habeeb
co_authors: []
series: null
date: '2023-04-20T00:30:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-concepts-to-know-before-learning-react
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/Seven-JavaScript-Concepts-to-master-before-React--2-.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: null
seo_desc: 'A lot of web developers use React as their go-to library for building UI
  components for their websites. React is one of the most popular frameworks for web
  development and it is written entirely in JavaScript.

  Since React was written in JavaScript, i...'
---

A lot of web developers use React as their go-to library for building UI components for their websites. React is one of the most popular frameworks for web development and it is written entirely in JavaScript.

Since React was written in JavaScript, it uses a lot of the JavaScript concepts that were introduced before and in the ES6 version of JavaScript. It is important for anyone who wants to learn React to understand these concepts.

In this article, I will be explaining with detailed examples the seven most important JavaScript concepts that a developer must know before learning React.

Before you start reading this article, check the pre-requisites

## Pre-requisites

To follow along with this article you should have some basic knowledge of:

* JavaScript, and
    
* The browser console (because this is where you will run your code)
    

## How to Use If Statements and Ternary Operators in JavaScript

In JavaScript, you use conditional statements to specify that a block of code should be executed if certain conditions are true.

Conditional statements are useful in the conditional rendering of UI components in React. They allow you to render your UI based on certain conditions.

### If ... Else Statement

The first thing to know regarding conditional statements is how to use the if ... else statement.

You can write code that will add two numbers if the second one is greater than the first, and subtract them if that's not the case. Here's what that would look like using an if ... else statement:

```js
if (a < b) {            
    let output = a + b;        
} else {            
    let output = a - b;        
}
```

In an if ... else statement, you can use an else ... if instead of writing multiple if's.

The else if makes it possible for you to write multiple conditions together. It specifies a new condition to test, if the first condition is false.

```js
if (a < b)  {        
    let output = a + b;    
} else if (a > b) {
    let output = a - b;    
} else {        
    let output = a * b;    
}
```

The code above writes an else if statement to the previous example. The else if tests for the condition a is greater than b, if the previous condition is false.

### Ternary Operator

A ternary operator is a more concise way of writing an if ... else statement.

It takes three operands: a condition followed by a question mark (`?`), then an expression to execute if the condition is truthy followed by a colon (`:`), and finally the expression to execute if the condition is falsy.

If you want to rewrite the above if ... else example using a ternary operator, it should look like this:

```js
(a < b) ? a + b : a - b;
```

The (a &lt; b) is the condition, the ? evaluates the condition, and if it is true it returns a + b, while if it is false it returns a - b.

That's five lines of code from the previous example written in just one line. But, if you want to include else if in your ternary operator code, you would need to write this:

```js
(a < b) ? a + b : (a > b) ? a - b : a * b;
```

In the code above, the ? evaluates the condition (a &lt; b) and if it is true it returns a + b. But, if it is false it evaluates the second condition (a &gt; b) and if that is true it returns a - b else it returns a \* b.

Just, one line too. But, to prevent it from becoming too cumbersome you can split it into multiple lines. This will make your code more readable.

In the example below, you'll see how you can split your code by making the condition and the return statement be on the same line.

```js
(a < b) ? a + b         
: (a > b) ? a - b         
: a * b;
```

## How Destructuring Works in JavaScript

Destructuring in JavaScript is when we unpack values from arrays or properties from objects and assign them to a variable.

It makes it easy to extract data from arrays and objects, and it's applicable in React concepts like useState.

### Array Destructuring

Array destructuring is used to extract data from an array.

In the example below, we destructure the `newArray` array in two ways. One way is to declare an array that contains the variables we want to assign to our array values and assign it to the newArray variable. The other way is to assign the array of variables to the array that contains the values we want to destructure.

```js
let newArray = ["Musab", "I", "Handsome"];    
let [noun, pronoun, adjective] = newArray; 

// The above can also be rewritten as this:  

let [noun, pronoun, adjective] = ["Musab", "I", "Handsome"];    

console.log(noun);    
console.log(pronoun);
```

You can skip one or more values by putting commas in their place.

```js
let newArray = [a, b, c, d, e];

let [firstLetter, , , ,lastLetter] = [a, b, c, d, e];
```

### Object Destructuring

Object destructuring is similar to array destructuring, but in objects we only destructure the keys/properties.

In the example below, the "personObject" was destructured by declaring an object containing the properties of the personObject and assigning it to the personObject.

```js
let personObject = {        
    name: "David",        
    age: 18,        
    height: "6ft 5in",        
    gender: "male",    
}    

let {name, age, height, gender} = personObject   
console.log(name, age, height, gender);
```

Now, you can access the values of each of the keys without calling the object.

You can also assign each of the destructured keys to new variables.

```js
let personObject = {        
    name: "David",        
    age: 18,        
    height: "6ft 5in",        
    gender: "male",    
}    

let {name: personName, age: personAge, height: personHeight, gender: personGender} = personObject;

console.log(personName, personAge, personHeight, personGender);
```

## How to Use Template Literals in JavaScript

Template literals are enclosed in backticks just like strings are enclosed in quotes. They allow you to store multiline strings and also interpolate strings with embedded expressions.

The example below shows a basic template literal.

```js
let basic = `I write codes`
```

You can write a template literal that stores multiline strings like this:

```js
let multiLine = `I write codes                     
		I debug codes`;
```

You can use the dollar sign and curly braces to embed expressions in template literals. In the example below, the function myName is embedded in the display variable with a template literal.

```js
function myName(Musab, Habeeb) {        
    alert("Musab Habeeb");    
}    

let display = `This displays my name ${myName()}`
```

## How to Use Objects in JavaScript

An object allows you to store collections of data. The data are stored in a pair of curly braces in a key-value pair format.

In the example below, we create an object named "myObject" and we give it three keys with their corresponding values.

```js
let myObject = {        
    name: Musab,        
    number: 12,        
    developer: [true, "David", 1]    
}
```

You can access the values that belong to each key in an object in two ways:

* by using dot notation (this is the most commonly used) or
    
* by using bracket notation
    

In the example below we access the name property using bracket notation and the number property using dot notation.

```js
let myObject = {        
    name: "Musab",        
    number: 12,        
    developer: [true, "David", 1]    
}

console.log(myObject["name"]);
console.log(myObject.number);
```

Object keys must be in string form. If they aren't, they will be inaccesible using dot notation.

In the example below, by accessing the property 3 you will get a syntax error.

```js
let numbers = {
    one: David,
    two: George,
    3: Peter
}

console.log(numbers.two);
console.log(numbers.3);
```

You must always put a comma at the end of every value in an object except the last value in the object.

## How to Use Arrays and Array Methods in JavaScript

Arrays are special types of objects that store data in an ordered form. Array methods are built-in functions that can be called on an array to do something on or with the array.

There are a lot of array methods, but the ones you will be using the most in React are the map, filter, and reduce methods.

### Map method

This method iterates through the elements of an array and calls a function on each element of the array. This returns a new array that contains the result of each function call.

```js
let fruits = ["pawpaw", "orange", "banana"];   

let mappedFruits = fruits.map(item => item + "s");    

console.log(mappedFruits); // ["pawpaws", "oranges", "bananas"]
```

### Filter method

This method returns all items of an array that match a specific condition.

```js
let fruits = ["pawpaw", "orange", "banana", "grape"];
    
let filteredFruits = fruits.filter(fruit => fruit.length > 5);

console.log(filteredFruits);  // ["pawpaw", "orange", "banana"]
```

### Reduce Method

The reduce method iterates over all the elements of an array and takes an action on each iteration. The result of that action is carried on to the next iteration to be used in the next action until the final iteration. Then, the final result will be returned.

It takes two arguments, which are:

* a function and,
    
* an optional argument that denotes the value the function will start from.
    

```js
let evenNumbers = [2, 4, 6, 8, 10]; 
    
evenNumbers.reduce((sum, current) => sum += current, 0);
```

## How to Use Functions and Arrow Functions in JavaScript

### Functions

A function is a block of code that performs a particular task. A function takes an argument, performs a task using the argument, and returns a result.

Functions are used to create functional components in React.

To declare a function you will use the keyword "function" and the function's name like this:

```js
function plusFour(a)  {        
    return a + 4;    
}
```

The function in the code above is named "plusFour" which takes an argument "a", adds four to "a" and returns the result.

To execute a function you will call the function by writing the function's name with brackets

```js
// We will call the plusFour function in the earlier example    
    
plusFour();
```

### Arrow functions

Arrow functions are an alternative way of writing functions. They are more compact and also, they contain deliberate limitations. You can rewrite the plusFour function above as an arrow function like this:

```js
let plusFour = (a) => {        
    return a + 4;    
}
```

Since the return statement is just one line, we can make the arrow function one line:

```js
let plusFour = (a) => a + 4;
```

Arrow functions cannot be used as methods, generators, or constructors while a regular function can.

## ES Modules

Before 2015, JavaScript variables, arrays, objects, and functions created in a file could only be accessed in that file.

But, with the introduction of ES6 in 2015 came modules. Modules allow you to carry out objects, arrays, functions, and so on in one file and use them in another file.

This helps you to maintain the size of your file while your application continues to grow larger.

Modules are what make React work as a single page application framework. All other files are in the form of components and are imported when and where they are needed.

There are two keywords we use when we work with modules:

* export keyword
    
* import keyword
    

The export keyword allows you to make the content of the module available to all other JavaScript files, while the import keyword allows you to bring in available content from one JavaScript file into another JavaScript file.

In the example below, the cook function is exported from its file.

```js
// file name: cook.js

function cook(ingredients, water, heat) {        
    let food = ingredients + water + heat;        
    return food;     
}    

export default cook;
```

Then, in the example below, the cook function is imported into the kitchen.js file and called.

```js
// file name: kitchen.js

import cook from './cook';    
cook();
```

## Conclusion

These seven JavaScript concepts are the most important ones to know if you're trying to learn React.

By learning these concepts it will be easier for you to learn React because you will start seeing their applications in your React code.

You should read more in-depth about these concepts and also try to formulate code examples involving them so you can better understand them.

Keep on learning, and keep on improving.
