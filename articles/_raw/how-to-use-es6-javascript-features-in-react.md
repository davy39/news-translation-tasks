---
title: How to Use ES6 Features in React
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2021-10-28T15:23:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-es6-javascript-features-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/g30.png
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: null
seo_desc: "Many JavaScript frameworks use ES6 features. So to help you learn these\
  \ handy features, I'll introduce you to them and then show you how to apply them\
  \ in React.js. \nHere are the ES6 features we'll cover in this guide:\n\nModules\n\
  Destructuring\nSpread Op..."
---

Many JavaScript frameworks use ES6 features. So to help you learn these handy features, I'll introduce you to them and then show you how to apply them in React.js. 

Here are the ES6 features we'll cover in this guide:

* Modules
* Destructuring
* Spread Operator
* Arrow functions
* Template Literals

All the examples we'll see here are quite basic and should be easy for beginners to grasp.

## How to Use ES6 Modules 

Modules help you split various functionalities of your app into separate files/scripts. You can have different scripts for form validation, logging a user in, and so on. 

Here, we will have two scripts: one for adding numbers and the other for subtracting numbers. We will take it step by step.

This is the structure of our folder:

> index.html  
> script.js  
> myModules/  
>  add.js  
>  sub.js

First we'll see how to use modules in vanilla JavaScript. Then we'll see how to apply them in React.

### Step 1 – Create the HTML file and link your script

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>ES6 Modules</title>
</head>
<body>
    <script type="module" src="script.js"></script>
</body>
```

You will notice that the script tag has a `type` which has the value of `module`. That should be the first thing you do if you are going to use the Module feature. 

You may come across resources that use a different method like adding a `.mjs` extension to their files, but to be on the safe side I'd recommend this method. The `script.js` will act as the "parent script" which we will be importing our modules into. 

### Step 2 – Create and export functions into separate files

Here's the function for addition in `add.js`:

```javascript
export function add(a, b){
    return a + b;
}
```

Here's the function for subtraction in `sub.js`:

```javascript
export function sub(a, b){
    return a - b;
}
```

Did you notice the `export` statement? To be able to use these functions in other scripts, you have to export them by adding the `export` statement. 

Here, we used inline export by adding the statement before the function – but you can opt to export this function at the bottom of the document like this: `export default add;`.

### Step 3 – Import the functions into `script.js`

```javascript
import { add } from "./myModules/add.js";
import { sub } from "./myModules/sub.js"

console.log(add(6, 4)); // 10

console.log(sub(6, 4));  // 2
```

To import the `add` function, we first typed the `import` statement followed by the name of the function nested in curly brackets and then the path to the file which the function exists in. 

You can see how we used `add(6, 4);` without reinventing the wheel by creating the function from scratch. Now you can import this function into any script you want.

### Step 4 – How to apply modules in React.js

Now that you have seen how we can use modules in vanilla JavaScript, let's have look at how you can use them in a React app. 

When you create a React application, the `App.js` component usually acts as the main component. We are going to create another component called `User.js` with some content about a user.

Here's the `App.js` component:

```javascript
function App() {
  return (
    <div className="App">
      
    </div>
  )
}

export default App

```

This component has just a `div` without any content.

And here's the `User.js` component: 

```javascript
function User() {
    return (
        <div>
            <h1>My name is Ihechikara.</h1>
            <p>I am a web developer.</p>
            <p>I love writing.</p>
        </div>
    )
}

export default User

```

If you can recall, you can export your functions at the bottom of the script as we just did. Next, we will import this function into the `App.js` component:

```javascript
import User from "./User"

function App() {
  return (
    <div className="App">
      <User/>
    </div>
  )
}

export default App

```

Just two additions to the script: `import User from "./User"` which point to the location of the component, and `<User/>` being the component itself. 

Now you can reuse the logic in the `User.js` component across your app and you can make it more dynamic using props instead of hard coding the user's information – but that is beyond the scope of this tutorial.

## How to Use ES6 Destructuring 

To destructure means to dismantle the structure of something. In JavaScript, this structure could be an array, an object, or even a string where the properties that make up the structure would be used to create a new identical structure (the properties can be altered). 

If what I have said still seems abstract to you, don't worry because you will understand better from the examples.

Prior to ES6, this is how you would extract some data in JavaScript:

```javascript
var scores = [500, 400, 300];

var x = scores[0],
    y = scores[1],
    z = scores[2];

    console.log(x,y,z); // 500 400 300
```

But in ES6, using destructuring, we can do this:

```javascript
let scores = [500, 400, 300];

let [x, y, z] = scores;

console.log(x,y,z); //500 400 300
```

The x, y and z variables will inherit the values in the scores array in the order which they appear, so `x = 500`, `y = 400` and `z = 300`. In a situation where all the values in the array have been inherited, any other value left without a parent value will return as undefined. That is:

```javascript
let scores = [500, 400, 300];

let [x, y, z, w] = scores;

console.log(x,y,z,w); //500 400 300 undefined
```

Here is an example using objects:

```javascript
let scores = {
    pass: 70,
    avg: 50,
    fail: 30
};

let { pass, avg, fail} = scores;

console.log(pass, avg, fail); // 70 50 30
```

The process is the same as destructuring arrays. 

Here is another example, but with strings:

```javascript
let [user, interface] = 'UI';

console.log(user); // U

console.log(interface); // I
```

The string was split into individuals letters and then assigned to the variables in the array.

### How to use destructuring in React.js

There are various scenarios where you might want to use destructuring in React. But a very common one would be with the `useState` hook.

```javascript
import { useState } from 'react';

function TestDestructuring() {
    const [grade, setGrade] = useState('A');
    
    return(
        <>
        
        </>
    )
}

export default TestDestructuring

```

Above, we created a constant variable `grade` along with a function `setGrade` whose purpose is to update the value of the variable. And we set the value of  `grade` to 'A' using destructuring. 

## How to Use the ES6 Spread Operator 

The spread operator `...` lets you copy all or some parts of an array, object, or string into another array, object, or string. For example:

```javascript
const collectionOne = [10, 20, 30];
const collectionTwo = [40, 50, 60];

const allCollections = [...collectionOne, ...collectionTwo];

console.log(allCollections); //10, 20, 30, 40, 50, 60
```

There is really not much to this. Using the `...` symbol, all the values of the first two collections were assigned to the third collection. 

Now that we have all the collections in one array, we will use the spread operator to copy the array and output the highest number. That is:

```
const allCollections = [10, 20, 30, 40, 50, 60];

const maxNumber = Math.max(...allCollections);
console.log(maxNumber) //60
```

### How to combine the spread operator with destructuring

In the last section, we saw the application of destructuring in JavaScript. Now, let's see how we can combine destructuring and the spread operator:

```javascript
let scores = [500, 400, 300];

let [x, ...y] = scores;

console.log(x); // 500

console.log(y); // [400, 300]
```

Here, the `x` variable inherited the first number in the array then the `y` variable spread across the array and copied everything that was left.

## How to Use ES6 Arrow Functions 

Basically, arrow functions allows us write our functions using shorter syntax. Before ES6, this is how you would write a function:

```javascript
var greetings = function() {
  console.log("Hello World!")
}

//OR

function greetings2() {
  console.log("HI!")
}
```

With ES6, a different syntax was introduced:

```javascript
var greetings = () => {
  console.log("Hello World!")
}

var greetings = () => {
  console.log("HI!")
}

```

The `function` keyword was removed while the fat arrow operator `=>` was introduced. 

Note that arrow functions are anonymous.

### How to use arrow functions with parameters

Parameters in arrow functions are passed into the parenthesis that come before the fat arrow operator. Example:

```javascript
var add = (a,b)=>{
  return a + b;
}
console.log(add(2,2)) //4
```

## How to Use ES6 Template Literals

Template literals allow you use back-ticks (``) instead of quotes ("") to define a string. This has various advantages.

Before ES6:

```
var name = "My name is Ihechikara" 

console.log(fullname);
```

With ES6:

```javascript
var name = `My name is Ihechikara` 

console.log(fullname);
```

### Interpolation in template literals

String interpolation lets you include variables and statements in your strings without breaking it up with the `+` operator. That is:

```javascript
var me = 'Ihechikara';

var fullname = `My name is Abba ${me}`;

console.log(fullname);
```

To interpolate a variable into your string, you use `${}` with the name of the variable passed into the curly brackets. Always remember that your string must be nested inside back-ticks and not quotation marks. 

The same applies when you are creating your DOM elements dynamically with JavaScript. You would do something like this:

```javascript
let name = 'Ihechikara';
let myHtmlTemplate = `<h1> This is a paragraph created by ${name}</h1>`;
```

## Conclusion

This article covered some of the most important ES6 features like modules, destructuring, spread operator, arrow functions and template literals. 

You will see these features being used frequently while learning or understanding JavaScript frameworks, so it should help you grasp their application in whatever framework they appear. 

If you have any questions about these features, you can find me on Twitter [@ihechikara2](https://twitter.com/Ihechikara2). Thank you for reading!

