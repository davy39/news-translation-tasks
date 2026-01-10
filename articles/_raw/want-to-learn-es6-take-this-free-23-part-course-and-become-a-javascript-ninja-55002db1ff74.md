---
title: Learn ES6+ in this free and interactive 23-part course
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-26T21:10:00.000Z'
originalURL: https://freecodecamp.org/news/want-to-learn-es6-take-this-free-23-part-course-and-become-a-javascript-ninja-55002db1ff74
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0-gCRnSTrgH7kWyg91ofGA.png
tags:
- name: coding
  slug: coding
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Per Harald Borgen


  _Click here to get to the course._

  JavaScript is undoubtedly one of the most popular programming languages in the world.
  It’s used almost everywhere: from large-scale web applications to complex servers
  to mobile and IoT devices...'
---

By Per Harald Borgen

![Image](https://cdn-media-1.freecodecamp.org/images/1*TsmDHkE8rZ7DQMVnqQqtYw.png)
_[Click here to get to the course.](https://scrimba.com/g/gintrotoes6?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gintrotoes6_launch_article)_

JavaScript is undoubtedly one of the most popular programming languages in the world. It’s used almost everywhere: from large-scale web applications to complex servers to mobile and IoT devices.

So we’ve partnered with [Dylan C. Israel](https://medium.com/u/7f21f9c02e5b) — a programming YouTuber and freeCodeCamp grad — and asked him to create [Introduction to ES6 course on Scrimba.](https://scrimba.com/g/gintrotoes6?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gintrotoes6_launch_article)

The course contains 17 lessons and 4 interactive challenges. It’s for JavaScript developers who want to learn the modern features of JavaScript introduced in ES6, ES7, and ES8.

Let’s have a look at the course structure:

### Part #1: Introduction

![Image](https://cdn-media-1.freecodecamp.org/images/1*TsmDHkE8rZ7DQMVnqQqtYw.png)

In the introductory video, Dylan gives an overview of what his course will look like and what main topics he’ll be touching on. He also gives you an intro about himself, so that you are familiar with him before jumping into the coding stuff.

### Part #2: Template Literals

The first feature of ES6 that the course covers is template literals. Template literals are a cleaner and more beautiful way to play with strings. They get rid of the need for a lot of `+` signs to concat strings.

```js
let str1 = 'My name is:'  
let name = 'Dylan';

let str2 = `${str1} ${name}`

// --> 'My name is: Dylan'

```

Template literals start with a backtick, and we use the `$` sign and curly brackets to introduce a variable in-between.

### Part #3: Destructuring Objects

In part 3, you’ll learn how to de-structure an object and extract the properties you are interested in.

```js
let information = { firstName: 'Dylan', lastName: 'Israel'};

let { firstName, lastName } = information;

```

In the code above, we’re extracting the properties `firstName` and `lastName` from the object and we assign them to variables by using Object Destructuring.

### Part #4: Destructuring Arrays

In this part, you’ll learn how to get the pointer of the item we are interested in from the array by using array destruction.

```js
let [ firstName ] = ['Dylan', 'Israel'];

```

Here, `firstName` is pointing towards the first item in the array on the right-hand side. We can also create more pointers on the left-hand side of the elements in our array.

### Part #5: Object Literal

In part 5 of our course, we will learn another cool feature of ES6, which is the Object Literal. Object Literals allow you to omit the key in the object if the name of the key and value are the same.

```js
let firstName = 'Dylan';  
let information = { firstName };

```

So, in the example above, we wanted to add the property of `firstName` in our `information` object. The `firstName` variable is another variable with the same name. We omit the key and just pass the name of the variable, and it will create the property and assign value itself.

### Part #6: Object Literal (Challenge)

Now it’s time for the first challenge of the course! The goal here is to console log the new city, the new address, and the country with it.

```js
function addressMaker(address) {  
   const newAddress = {  
      city: address.city,  
      state: address.state,  
      country: 'United States'  
   };  
   ...  
}

```

You are encouraged to use the topics we have learned so far to solve this problem. This includes Template Literals, Object Destruction, and Object Literals.

### Part #7: For…Of Loop

In part 7, you will learn about a new way of looping through elements. ES6 introduced a For…Of loop statement, which creates a loop that iterates over iterable objects like String, Array, NodeList objects, and more.

```js
let str = 'hello';

for (let char of str) {  console.log(char);}// "h"// "e"// "l"// "l"// "o"

```

In the code example above, the For…Of loop loops over a string and logs the characters out.

### Part #8: For…Of Loop challenge

In this challenge, you are asked to guess what happens when you use `let` over `const` inside a `for…of` loop, and to try to manipulate the values inside the loop.

```js
let incomes = [62000, 67000, 75000];

for (const income of incomes) {

}  
console.log(incomes);

```

### Part #9: Spread Operator

In part 9 of the course, you will learn about one of the coolest features included in ES6: the Spread Operator.

```js
let arr1 = [1, 2, 3];
let arr2 = [4, 5, 6];
let arr3 = [...arr1, ...arr2];

// arr3 = [1, 2, 3, 4, 5, 6];

```

The code above demonstrates one of the many cool implementations of using the spread operator. Here we are combining two arrays by putting them in a new array with three dots (…) in front of the name of the array.

### Part #10: Rest Operator

In this lesson, you’ll be learning a few use cases for the Rest operator. The Rest operator helps us handle function parameters in a better way by allowing us to represent the variable number of the function parameters as an array.

```js
function findLength(...args) {  console.log(args.length);}

findLength();  // 0
findLength(1); // 1
findLength(2, 3, 4); // 3

```

Here, we are calling the same function with a different number of parameters, and the Rest operator is handling that perfectly for us.

### Part #11: Arrow Functions

This lesson teaches us one of the coolest and most talked about features introduced in ES6: Arrow Functions. Arrow Functions have changed the way we write functions.

```js
const square = num => num * num;


square(2); // 4

```

By using the arrow function, the look of a _squaring_ function has completely been changed. In just a single line of code, we are able to return the square of a number. Arrow Functions have a lot of other awesome implementations, which are explained in the lesson.

### Part #12: Default Parameters

Default parameters allow us to initialise functions with the default value. In this lesson, you will learn how helpful this feature can be in real life coding tasks, as it helps you avoid errors and bugs. A simple example of default parameters would be:

```js
function sum (a, b = 1) {    
  return a + b;
}

sum(5); // 6

```

Here we are setting the default value of `b` so that when we do not pass any value of b, it will use the default value for calculating the result.

### Part #13: includes()

Using the `includes` method, we can find out if any string contains a particular character or a substring. In this lesson, you will learn in detail about the practical use-cases of this function.

```js
let str = 'Hello World';

console.log(str.includes('hello')); // true

```

Here, we find out if our string contains the substring of `hello`. As you can see, the includes method returns either true or false depending on whether or not the condition is matching.

### Part #14: Let and Cost

Perhaps the most important feature of ES6 is the two new keywords for declaring variables: `let` and `const`.

```js
let str = 'Hello World';

const num = 12345;

```

Using `let`, we can create variables which can be changed later in the program. Variables declared with `const` can never be changed. We will learn about them in this lesson.

### Part #15: Import and Export

We all know how important it is to have modular code, especially if you are working on large-scale applications. With `import` and `export` statements in JavaScript, it has become extremely easy and clean to declare and use modules.

In part 15 of this course, you will learn how to use export and import statements to create modules.

```js
// exports function 
export function double(num) {   
 return num * num;  
}

```

In the code above, we are exporting a function by the name of `double.` We’re then importing the function in a separate file:

```js
// imports function  
import { double } from '..filepath/filename

```

### Part #16: padStart() and padEnd()

ES2017 introduced two new methods to manipulate strings, which you will learn in detail in this part. `padStart` and `padEnd` will simply add padding at the start and end of the string.

```js
let str = 'Hello';  
str.padStart(3); // '   Hello'

str.padEnd(3); // 'Hello   '

```

### Part #17: padStart() and padEnd() challenge

In this part, you’ll tackle the third challenge of this course. It’s a small quiz in which Dylan first asks you to guess, and then explains what happens when the following code runs

```js
let example = 'YouTube.com/CodingTutorials360';

// console.log(example.padStart(100));  
// console.log(example.padEnd(1));

```

### Part #18: Classes

Classes were introduced in ES6, and they have completely stepped up the game for using Object Oriented Patterns in JavaScript. Although it is simply syntactical sugar over JavaScript’s existing prototypical inheritance, it has made it easier to write in a more object-oriented way.

So in this lesson, you will learn in detail how you can use classes and take the benefit of OOP features like, for example, inheritance. Below is a simple example of using classes.

```js
class Car {
   constructor(wheels, doors) {
      this.wheels = wheels;
      this.doors = doors;
   }
   describeMe() {
     console.log(`Doors: ${this.doors} and Wheels: ${this.wheels}`);
   }}


const car1 = new Car(4, 2);  
car1.describeMe(); // Doors: 2 and Wheels: 4

```

Here, we create a simple Car class in which we have a constructor assigning the wheels and doors. We also have a method which logs the number of doors and wheels of the car.

Then, we create a new instance and pass the values of wheels and doors. Finally, we call the `describeMe` method on it.

### Part #19: Trailing Commas

In lesson 19, you will be learning how to use trailing commas. They make it easier to add new elements, properties, or attributes to your code, as you can do so without having to worry about adding a comma to the previous element.

```js
let arr = [  1,   2,   3, ];arr.length; // 3

```

This was just a simple example of using trailing commas. You will learn more about them in our lesson during our course.

### Part #20: Async & Await

Async & Await is my favourite features of ES6. With Async & Await, we can write asynchronous code which looks like synchronous code. This is clean, easy to read, and easy to understand. So in this lesson, you’ll learn a few practical examples of how to use it.

```js
let response = await fetch('https://example.com/books');
console.log('response');

```

In the example above, we have used the await keyword before the fetch statement, so it will wait until the result of this API has been fetched before moving forward to the next line.

### Part #21: Async & Await (Challenge)

This is the last challenge of this course, and it is of course about Async & Await. You will be asked to first try converting the following promise-based code into using Async & Await:

```js
function resolveAfter3Seconds() {  
   return new Promise(resolve => {  
      setTimeout(() => {  
        resolve('resolved');  
      }, 3000);  
   });  
}

```

Don’t worry if you can’t solve it completely. Dylan will explain in detail how to do it. By the end of the lesson, you will be confident enough to start using it immediately.

### Part #22: Sets

In the final lecture of the course, you will be learning about a very important data structure, Set. This is an object which lets you store unique values. So whenever you want to have a collection which contains only unique values, you can use Sets.

```js
const set1 = new Set([1, 2, 3, 4, 5]);

```

### Part #23: What’s next?

![Click the image to get to the course](https://cdn-media-1.freecodecamp.org/images/1*R6H7A7OZqNdCyeN6EXIEPA.png)

To wrap up the course, Dylan gives some tips on how to take this learning on further and improve the code you write today.

And that’s it! If you get this far you can give yourself a pat on the back! You’ve completed the course and are one step closer to becoming a JavaScript ninja.

Thanks for reading! My name is Per, I’m the co-founder of [Scrimba](https://scrimba.com), and I love helping people learn new skills. Follow me on [Twitter](https://twitter.com/perborgen) if you’d like to be notified about new articles and resources.

---

Thanks for reading! My name is Per Borgen, I'm the co-founder of [Scrimba](https://scrimba.com) – the easiest way to learn to code. You should check out our [responsive web design bootcamp](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gintrotoes6_launch_article) if want to learn to build modern website on a professional level.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/bootcamp-banner.png)
_[Click here to get to the advanced bootcamp.](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gintrotoes6_launch_article)_


