---
title: Exploring JavaScript Iteration
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2015-11-23T02:50:20.000Z'
originalURL: https://freecodecamp.org/news/exploring-javascript-for-in-loops-bdfc226d8515
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XJvkwoG4BLFnx6tpfzPZQQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Festus K. Yangani

  Loops allow programs to perform repetitive tasks, such as iterating through an array,
  while adhering to the DRY principle (Don’t Repeat Yourself). They come in handy
  when you want to execute a function a number of times, using di...'
---

By Festus K. Yangani

Loops allow programs to perform repetitive tasks, such as iterating through an array, while adhering to the [DRY principle](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) (Don’t Repeat Yourself)**.** They come in handy when you want to execute a function a number of times, using different sets of inputs each time.

Just like other programming languages, JavaScript supports different kinds of loops. This article will explore **for**, **for/in**, **while** and **do/while** loops.

#### The For Loop

The **for** loop is the most common style of JavaScript loop. Here’s its basic syntax:

```
for (<initialization>; <condition>; <incremental expression>) {   code block // This is executed if condition evaluates to true}
```

* **initialization** - used to declare new variables with the **var** keyword, typically used to initialize a counter variable (var i = 0).
* **condition** - An boolean expression to be evaluated before each loop iteration. If this expression evaluates to true, the inner commands will be executed.
* **incremental expression** - an expression evaluated at the end of each loop iteration. This is usually used to increment, decrement, or otherwise update the counter variable.

Examples:

```
//Counting 1 to 5for (var i = 1; i <= 5; i++) {  console.log(i);}//=&gt; 1//=> 2//=&gt; 3//=> 4//=> 5
```

```
//Iterating through an arrayvar arr = [17, 22, 35, 54, 96];
```

```
for (var i = arr.length; i >=0; i--) {  console.log(arr[i]);}//=&gt; 96//=&gt; 54//=> 35//=> 22//=> 17
```

#### The For/in Loop

The **for/in** loop is used to iterate through properties of an object. A **for/in** statement looks as follows:

```
for (variable in object) {  statements}
```

* **variable** - a different property name is assigned to this on each iteration.
* **object** - the object whose enumerable properties are iterated through.

Example:

```
var myObj = {city: "Austin", state: "Texas", country: "USA"}
```

```
for (var key in myObj) {  console.log(myObj[key]);}//=&gt; Austin//=> Texas//=> USA
```

#### The While Loop

**While** loops are conditional loops where a condition is checked at the start of the iteration, and — if the condition is true — the statements are executed. Here’s the basic syntax of a **while** loop:

```
while (condition) {  statement //code block to be executed as long condition is true.}
```

* **condition** - the expression evaluated before each iteration through the loop. If this condition evaluates to true, the inner commands are executed. If the condition evaluates to false, then the inner statement won’t execute and the program carries on.
* **statement** - the code block to be executed as long as the condition evaluates to true.

Example:

```
var i = 0;while (i < 3) {  console.log(i);  i++;}
```

```
//=>0//=>1//=>2
```

#### The do/while

The **do/while** loop is a variant of the while loop. Unlike in the while loop, **do/while** loop will execute the code block once, before it even checks to see whether the condition is true. Then it will repeat the loop as long as the condition is true.

Syntax:

```
do {      statement //code block to be executed}while (condition);
```

* **statement** - executed at least once, and is re-executed each time the condition evaluates to true.
* **condition** - the expression evaluated after each iteration through the loop. If the condition evaluates to true, the statement is re-executed. If the condition evaluates to false, then execution of statement is stopped.

Example:

```
var cars = ["Tesla", "Prius", "GMC", "Ford"];
```

```
var i = 0;do {      console.log(cars[i]);              i++;}while (i < cars.length)
```

```
//=&gt; Tesla//=> Prius//=> GMC//=> Ford
```

I hope this brief tour of loops has helped you better understand how iteration works in JavaScript. If you have any questions about loops, or just want to chat, you can also reach out to me on [twitter](https://twitter.com/yangani)_._

