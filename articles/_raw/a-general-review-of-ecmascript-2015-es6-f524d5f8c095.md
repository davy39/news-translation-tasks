---
title: A general review of ECMAScript 2015 (ES6)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-24T18:54:53.000Z'
originalURL: https://freecodecamp.org/news/a-general-review-of-ecmascript-2015-es6-f524d5f8c095
coverImage: https://cdn-media-1.freecodecamp.org/images/1*NSN1a2xVtV1exzcD8fpzhA.jpeg
tags:
- name: coding
  slug: coding
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Cem Eygi

  ES6 is the newer standardization/version of Javascript, which was released in 2015.
  It is important to learn ES6, because it has many new features that help developers
  write and understand JavaScript more easily. Modern Frameworks like An...'
---

By Cem Eygi

ES6 is the **newer standardization/version of** **Javascript**, which was released in 2015. It is important to learn ES6, because it has many new features that help developers write and understand JavaScript more easily. Modern Frameworks like Angular and React are being developed with ES6. Its syntax is also different than classic JavaScript.

So what’s new in ES6? Let’s have a look.

### 1. let & const keywords

ES6 brings two new keywords for variable declarations: `let` and `const`.

We used to have only the `var` keyword in JavaScript to declare variables:

```js
var name = 'Cem';
```

In ES6, we use the `let` keyword instead.

#### Why ‘let’ instead of ‘var’ ?

Because the usage of `var` causes **scope** problems. For example, let’s define a string with `var` globally and locally:

```js
var word = 'I am global';

if(true) {  
  var word = 'I am local'; 
}

console.log(word); // What do you expect here as result?
```

The _console.log_ should print the **global** string: `'I am global'`. Because the second declaration `var word = 'I am local'` is a **local** string and _console.log_ is outside of the _if block_:

![Image](https://cdn-media-1.freecodecamp.org/images/cVxBMtGJhUv9UZBuGq4uZc2KSv3cskx-saW5)
_**Surprisingly, the local variable has printed.**_

Unexpectedly, the local variable which we have defined with `var` has ignored the _if block_ and gets printed to the console. To prevent this problem, ES6 brings us a new keyword: **let.**

Let’s try again with `let`:

```js
let word = 'I am global';

if(true) {
  let word = 'I am local'; 
}

console.log(word); // This time what do you expect?
```

![Image](https://cdn-media-1.freecodecamp.org/images/Dwd8aTI-M0eMOKLLrOB5en7-1SGdc9M2Jx0j)
_**The result of using ‘let’**_

This time the **global** string has printed as we expected, `let` solved the scope-problem.

#### Another issue of the ‘var’ statement

We can both re-assign variables with `var` and `let`. But, `let` doesn’t allow us to **redeclare** the same variables:

```js
var number = 1;
var number = 2;

console.log(number); // No errors here, 2 gets printed
```

Let’s try again with **let**:

```js
let number = 1;
let number = 2;

console.log(number); // let doesn't allow redeclaration
```

![Image](https://cdn-media-1.freecodecamp.org/images/VTuifL3QukwZgVbmITOH4rhI1LMpy5ojjfgD)
_**Re-declaration of let throws an error:**_

You can still use **var** in ES6, but it is not recommended.

#### The const keyword

Let’s continue with the `const` keyword. `const` means _constant_.

> “Constant: something that does not change.”

When we declare a constant variable, we cannot change it later. For example, **birth date** is a constant.

```js
const birthYear = 1990;

birthYear = 2000; // You cannot re-assign a constant variable
```

If you try to change or redeclare a _const_ variable, it will give an error:

![Image](https://cdn-media-1.freecodecamp.org/images/xVbUNLdmjjbQJkrniCDmf-eyAl4JVuJgB4XV)
_**Re-assignment of a const variable throws an error**_

Using `const` improves your code quality. Use it only when you’re sure that your variable is not going to change later.

### 2. Template Literals

Template literals are one of the new **syntaxes of ES6,** for creating strings and printing dynamic variables.

* To create a string, use back tics **( `` )** instead of single or double quotes:

```js
let oldWay = 'A word';  // JS Way

let newWay = `A word`;  // ES6 Way
```

* Use the interpolation syntax: **${ expression }** to simplify string concatenation and to create dynamic variables

Let’s define some variables and use the old and new methods to print them:

```js
let name = 'Cem';
let age = 28;
let profession = 'Software Developer';
```

The previous JavaScript way:

```js
console.log("Hello, my name is " + name + ", I'm " + age + " years old and I'm a " + profession);
```

![Image](https://cdn-media-1.freecodecamp.org/images/DmqlgNPaa7B74Bnqumk3t3CseyQPxmahquIy)
_**Output with + signs**_

The ES6 way:

```js
console.log(`Hello, my name is ${name}, I'm ${age} years old and I'm a ${profession}.`);
```

![Image](https://cdn-media-1.freecodecamp.org/images/Uzd--CtKLfVlzdQujxl8VbQCuMcVZfs-pHTP)
_**Output with template literals**_

We can do much more with template literals, and you can check [here](https://css-tricks.com/template-literals/) for more details.

### 3. Arrow Functions

Arrow Functions use a fat arrow `=>` rather than the `function` keyword, when defining a function:

JavaScript Function:

```js
var sum = function addition (firstNum, secondNum) {
    return firstNum + secondNum;
}
```

ES6 Function:

```js
let sum = (firstNum, secondNum) => { return firstNum + secondNum };
```

We can also omit the `return` keyword, unless our function returns a **code block.**

Since this article is about an overview of ES6, I’m not going much deeper of arrow functions. You can get more information about arrow functions [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions).

### 4. The Spread and Rest Operators

Have you ever seen three dots `...` in programming? This is called the **spread syntax**.

#### Spread Operator — Usage for Arrays

We have an array of numbers: `let numberArray = [1, 19, 21, 85, 42]`

We can use the spread operator:

* to get the values (numbers) out of the array:

```js
console.log(...numberArray);
```

![Image](https://cdn-media-1.freecodecamp.org/images/Z1e3qPXYxxSSKjLlMS6Q2Lv3yTPHzKK2YAsD)
_**Numbers are now out of the array**_

**Using the spread operator doesn’t affect the array itself.**

* to concat the array with another array:

```js
let charArray = ['a','b','c'];

charArray.push(...numberArray);

console.log(charArray);
```

![Image](https://cdn-media-1.freecodecamp.org/images/bGTjyMyTgSrg82mgjGSEKGTmhWN3pNa0kq5g)
_**values in numberArray added to charArray**_

Otherwise, the **numberArray** would be added as the fourth element, directly inside the **charArray**:

![Image](https://cdn-media-1.freecodecamp.org/images/P2vv2Sq1-oWKuRDrupnWS9N4XZgdHZZGXBgt)
_**Array in an array, without the spread operator**_

#### Rest Operator — Usage for Functions

The other usage of three dots `...` are for function parameters.

A **parameter** given after three dots turns into an **array** which will contain the rest of the parameters called the **rest operator.**

```js
function count (...counter) { // parameter becomes an array
  console.log(counter.length);
}

count(); // 0
count(10); // 1
count(1, 10, 24, 99, 3); // 5
```

Since the `...counter` is now an array, we can get the length of it. All the parameters that are given to the `count()` function are now values of the **counter** array:

![Image](https://cdn-media-1.freecodecamp.org/images/dCKC-Kbux4M-bU7BPbMqDx4MapabhlxwTGic)
_**Number of Parameters = Length of Array**_

### 5. Import & Export

Another new feature of ES6 is that it lets us **import & export** our classes, functions, and even variables to other parts (files) of our code. This approach helps us programmers a lot when we want to break the code into smaller pieces. It increases the readability and maintenance of the project code in the future.

Let’s see how it works:

Firstly, we create an ES6 function and **export** it with the `export` keyword.

```js
export let myFunction = () => { console.log('I am exported!'); }
```

After that, to import `myFunction` to another file, we need to define its **folder path, name of the file**, and the `import` keyword.

```js
import { myFunction } from './yourFolderPath/fileName';
```

Finally, call the function in the imported file and use it.

```js
myFunction();
```

This is how we can break our code into smaller pieces, with the help of export & import. We can also import other modules and services like **HttpService, Router, Axios,** and **Bootstrap** to use them in our code too, after installing them in our **node_modules**.

I’ve explained some new features of ES6 in this article. There are many other features and more details that you should check out. If you find this article helpful, please share it so more people can read it.

Thank you for reading and for your support! :)

