---
title: Learn JavaScript in ONE hour with this free and interactive course
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-19T14:30:48.000Z'
originalURL: https://freecodecamp.org/news/want-to-learn-javascript-heres-a-free-24-part-course-to-get-you-started-e7777baf86fb
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9cae64740569d1a4caa61c.jpg
tags:
- name: learning to code
  slug: learning-to-code
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: startup
  slug: startup
seo_title: null
seo_desc: 'By Per Harald Borgen


  _A breakdown of the course. You can click here to jump directly to the course._

  JavaScript is the most popular programming language on the web. You can use it to
  create websites, servers, games and even native apps. So no wonder...'
---

By Per Harald Borgen

![Image](https://cdn-media-1.freecodecamp.org/images/1*qwstevkkpIh4WQeO0503aw.png)
_A breakdown of the course. [You can click here to jump directly to the course.](https://scrimba.com/g/gintrotojavascript?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gintrotojavascript_launch_article)_

JavaScript is the most popular programming language on the web. You can use it to create websites, servers, games and even native apps. So no wonder it’s such a valuable skill in today’s job market.

So I reached out to [Dylan C. Israel](https://medium.com/u/7f21f9c02e5b) — a [programming YouTuber](http://www.youtube.com/CodingTutorials360) and freeCodeCamp grad — and asked him to create a [free JavaScript course on Scrimba](https://scrimba.com/g/gintrotojavascript?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gintrotojavascript_launch_article).

The course contains 15 lectures and 7 interactive challenges and is suitable for beginners. It will give you a quick intro to the most important JavaScript concepts.

Here’s how the course is laid out.

### Part #1: Introduction

![Image](https://cdn-media-1.freecodecamp.org/images/1*Gpj7-WF-Esr45IoY8TPjyg.png)

As always, the course begins with a screencast about the subject in general and an overview of the course structure. Dylan will also tell you a little bit about himself so that you’ll get to know him before you dive into the coding.

### Part #2: Variables

The first concept you’ll need to learn is _variables,_ which are for storing values. In modern JavaScript there are two keywords for doing that: `let` and `const`.

Let’s store the name _Dylan_ in a `let` which we’ll call `name`.

```js
let name = 'Dylan';  
console.log(name);

// --> 'Dylan'

```

As you can see, we can then refer to that variable later on in order to fetch out the value, for example, to log it out to the console, using the `console.log()` method.

### Part #3: Strings

In the second lesson, you’ll learn about your first data type: _strings_. A string simply stores a sequence of characters wrapped in quotes. So whenever you wrap something inside single or double quotes, it’s turned into a string in JavaScript, like this:

```js
let name = "Dylan";

```

### Part #4: Strings challenge

It’s time for the first challenge of the course! In this one, you’re going to try and combine two variables into one.

```js
let firstName = "Dylan";  
let lastName = "Israel";

console.log(fullName);

// --> ReferenceError: fullName is not defined

```

If this is your very first introduction to JavaScript you’ll need to use your freshly acquired knowledge of both _variables_ and _strings_ in order to solve this problem. You also might have to do a little code of experimentation. Luckily, this is possible in the Scrimba platform.

### Part #5: Numbers

Next up is the second data type you’ll need to learn: _numbers_. Other languages often have multiple data types for numbers, like _floats_ for decimal numbers and _integers_ for the whole numbers_._ However, in JavaScript, they’re both _numbers_.

We can use the `typeof` to check the data type:

```js
let example1 = 7;  
let example2 = 7.77;

console.log(typeof example1);  
console.log(typeof example2);

// --> "number"  
// --> "number"

```

In this lecture you’ll also learn how to convert values between strings and number using `parseInt()` and `parseFloat()` methods.

### Part #6: Numbers challenge

In the numbers challenge, you’ll be exposed to a few different strings and numbers combined with the methods you’ve learned so far. Your job is to guess which values these expressions end up as.

```js
let example1 = parseInt("33 World 22");  
let example2 = parseFloat('44 Dylan 33');  
let example3 = 55.3333.toFixed(0);  
let example4 = 200.0.toFixed(2);

```

It might be a bit tricky, so don’t be discouraged if you do mistakes!

### Part #7: Booleans

Booleans are simple, they’re either _true_ or _false._ Here’s how you create a boolean value:

```js
let example = true;

```

The fact that `example` now is set to _true_ can come in handy when you’re programming, as you sometimes want to take actions based upon conditions like this one.

You’ll also learn about _truthy_ or _falsy_ values in this lecture, which are other data types, like strings or numbers, but which has a _truthy_ or _falsy_ side to them.

### Part #8: Booleans challenge

In the booleans challenge, Dylan follows the same pattern as the numbers one, where you are to guess a bunch of values. Your job is to guess whether or not these variables are _truthy_ or _falsy:_

```js
let example1 = false;  
let example2 = true;  
let example3 = null;  
let example4 = undefined;  
let example5 = '';  
let example6 = NaN;  
let example7 = -5;  
let example8 = 0;

```

### Part #9: Arrays

The data types you’ve learned up until now, are so-called _primitive_ values. Now it’s about time to learn about the array, which is a _non-primitive_ value.

An array is simply a list of values, like this:

```js
let example = ['programming', 'design', 'art'];

```

You’ll learn how to create arrays, how to add and remove items and even how to loop through the entire array using the `forEach()` method.

### Part #10: Arrays challenge

In the arrays challenge you’ll be introduced to the concept of padding by _reference_ or _value_, which is important in order to understand JavaScript properly. We’ll also revisit this concept later on, as repetition will help the knowledge stick.

```js
let example1 = ['Dylan', 5, true];  
let example2 = example1;

example2.push(11);

console.log(example1);  
console.log(example2);

```

The results that are logged above might surprise you if you’re not aware of the _passing by reference_ concept.

### Part #11: Objects

From arrays, we’ll continue to its close relatives called _objects._ Objects are like arrays in the sense that they can store multiple values. However, instead of consisting of a list of values, an object consists of so-called key-value pairs. We create an object using curly brackets:

```js
let example = {  
  firstName: 'Dylan';  
  lastName: 'Israel'  
};

```

In this lecture, you’ll learn how to populate objects and fetch their values.

### Part #12: Objects challenge

In this challenge, we’ll revisit the concept of passing by _reference_ or _value_. You’ll also learn about the `Object.assign()` method, which allows you to create copies of objects.

```js
let example1 = {  
  firstName: 'Dylan'  
};  
let example2 = example1;  
example2.lastName = 'Israel';

console.log(example1);  
console.log(example2);

```

### Part #13: Arithmetic operators

A programming language would be almost useless if it didn’t know how to do arithmetic operations. Doing it in JavaScript is pretty straight-forward:

```js
let example = 5 + 5;

console.log(example)

// --> 10

```

In this lecture, you’ll also experience how JavaScript handles expressions where multiple operations are combined.

### Part #14: Relational operators

When programming we often have to compare values, to see if they’re equal to each other, or if one of them is larger than the other, so in this lecture, you’ll learn how to do that.

```js
let example1 = 10;  
let example2 = 15;

console.log(example1 > example2)

// --> false

```

And real-world example of this would be when you want to check if a user has got enough credit to purchase an item. If the credit is above the price, then they’re allowed to buy, otherwise, they’re not.

### Part #15: Relational operators challenge

In this challenge you’ll be able to test how well you understand relational operators, through guessing the boolean value of these variables:

```js
let example1 = 5 === 5;  
let example2 = 5 == '5';  
let example3 = 6 != '6';  
let example4 = 7 !== '7';

```

### Part #16: Increment & decrement

Making values grow or shrink is very often done in programming, for example when you’re counting. It can be done in a few different ways, though, so it deserves its own lecture.

```js
let example = 1;  
example = example + 1;

console.log(example);

// --> 2

```

### Part #17: Increment & decrement challenge

This challenge will look at the difference between doing `example++` and `++example`.

This might require you to experiment a bit in order to understand it, or even googling, which also is a critical skill for any developer.

### Part #18: If, else if, else

Conditional statements like `if`, `if else` and `else` are critical when programming. It’s what allows you to have logic in your application. So in this lecture, you’ll learn how to work with all three of them.

```js
let example = 5;

if (example === 5) {  
  console.log('Runs');  
} else if ( true ) {  
  console.log('else if');  
} else {  
  console.log('else');  
}

```

You’ll also learn about how to combine these conditionals with relational operators to make complex logic.

### Part #19: If, else if, else challenge

In this challenge, you’ll try to guess what the following expressions evaluate to. This builds upon both what you’ve learned in the relational operators' lecture and in the previous one.

```js
console.log(10 === 10 && 5 < 4);  
console.log(10 === 10 || 5 < 4);  
console.log((5 >= 5 || 4 > 4) && 3 + 2 === 5);

```

Again, don’t lose the courage if you don’t manage to guess correctly. This stuff is tricky for a beginner!

### Part #20: Switch

In this lecture, you’ll learn about so-called `switch` statements, which are really handy if you have many conditions to check between. Here’s an example of that:

```js
let studentAnswer = 'D';

switch(studentAnswer) {  
  case 'A':  
    console.log('A is wrong.');  
    break;  
  case 'B' :  
    console.log('B is wrong.');  
    break;  
  case 'C':  
    console.log('C is correct.');  
    break;  
  default:  
    console.log('Not a real answer.');  
}

```

### Part #21: For loop

For loops allow you to execute a block of code a number of times. The amount is dictated by you by setting three conditionals. Here’s an example of a simple `for` loop:

```js
for (let i = 0; i < 5; i++) {  
  console.log(i);  
}

// -->  
// 0  
// 1  
// 2  
// 3  
// 4 

```

In this lecture, you’ll see how you can calculate the total sum of an array of numbers using a `for` loop.

### Part #22: While & do while

If you want to execute a piece of code multiple times but don’t know _how_ many times, then a `while` loop might be exactly what you need. It allows you to execute a block of code as long as a certain condition is met.

```js
let count = 0;

while (count < 20) {  
  count++;  
}

console.log(count);

```

You’ll also learn about the `do/while` statement.

### Part #23: Functions

Finally, you’ll need to learn about functions, as it’s critical for any application. You’ll learn the syntax of functions, how they’re called and how you can add parameters to them.

```js
function add() {  
  console.log('add');  
}

add();

// --> 'add'

```

And when you’ve finished this lecture you’re done with the syllabus for this course, as you know have an understanding of the core concepts in JavaScript.

### Part #24: What’s next?

![Image](https://cdn-media-1.freecodecamp.org/images/1*H3vOeCjQV7IlHFqbjLmm_A.png)

Dylan ends the course by telling you a little bit about what you can do next in order to further improve your JavaScript skills! Remember, this course was just the beginning.

Once you’ve reached this far, I’d strongly encourage you to continue, as you’re on track to gain highly valuable skill in today's society.

Not only can JavaScript help you improve your career, but you’ll also be able to build products on your own!

So be sure to [take this free course today](https://scrimba.com/g/gintrotojavascript?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gintrotojavascript_launch_article). You’ll be able to build projects in JavaScript on your own before you know it!

---

Thanks for reading! My name is Per Borgen, I'm the co-founder of [Scrimba](https://scrimba.com) – the easiest way to learn to code. You should check out our [responsive web design bootcamp](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gintrotojavascript_launch_article) if want to learn to build modern website on a professional level.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/bootcamp-banner.png)
_[Click here to get to the advanced bootcamp.](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gintrotojavascript_launch_article)_


