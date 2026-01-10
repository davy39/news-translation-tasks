---
title: An overview of JavaScript iterators
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-11T07:01:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-iterators-17ab32c3cae7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*wEv6UnPpMocWKCoH2x1HSA.jpeg
tags:
- name: education
  slug: education
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Joanna Gaudyn

  The difference between for, for…in and for…of loops


  _[source](https://unsplash.com/photos/kJAl5OPoRgQ" rel="noopener" target="blank"
  title=")

  Iteration might be one of the most commonly used operations in programming. It is
  taking a...'
---

By Joanna Gaudyn

#### The difference between for, for…in and for…of loops

![Image](https://cdn-media-1.freecodecamp.org/images/tS2k4SixOdqRW2ZATfBIIOTtNTaqjv2hU3ba)
_[source](https://unsplash.com/photos/kJAl5OPoRgQ" rel="noopener" target="_blank" title=")_

Iteration might be one of the most commonly used operations in programming. It is taking a set of items and performing a given operation on each and every one of them in a sequence. Loops allow for a quick and easy way to do something repeatedly.

In JavaScript, different looping mechanisms let you define the beginning and end of a loop in different ways. There’s no easy answer to which of the mechanisms is the best, as different situations call for different approaches, meaning that your needs can be more easily served by one type of loop over the others.

Here’s what you can use to [loop in JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration):

* do…while statement
* while statement
* labeled statement
* break statement
* continue statement
* for statement
* for…in statement
* for…of statement

Let’s have a closer look at the last 3. They tend to be quite confusing when you start working with JavaScript, as the names don’t really make it easier to memorize the mechanics behind them. I hope a couple of examples will make things fall in place if you still are a little shaky on the concepts.

![Image](https://cdn-media-1.freecodecamp.org/images/PjMWkwqImDEcv4L38v-POyEuuE8LndiFaRKz)
_[source](https://www.pexels.com/photo/red-surface-1412212/" rel="noopener" target="_blank" title=")_

#### The ‘for’ loop

The `for` loop is the most common type of looping and you might have stumbled upon it in other programming languages as well, so let’s just have a quick refresher.

Here is the basic syntax:

```js
for ([initialExpression]; [exit condition]; [incrementExpression]) {
  do something;
}
```

Let’s take an example:

```js
const numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

for (let i = 0; i < numbers.length; i++) {
  console.log(numbers[i]);
}
```

Prints**:**

> 0  
>  1  
>  2  
>  3  
>  4  
>  5  
>  6  
>  7  
>  8  
>  9

So what really happens here? A `for` loop repeats until a specified condition evaluates to false. In our case, we are starting a counter (variable `i`) at 0, print a number from our `numbers` array which lives at the `i` index of the array, and finally increment the counter. We also declare that our loop is supposed to break when the counter is no longer smaller than the size of the array (`numbers.length`).

The biggest drawbacks of a `for` loop is having to keep track of a counter and exit condition. The syntax is also not very straightforward, and to understand what’s happening you really just need to memorize what each part of the code stands for. Even though a `for` loop can be a practical solution to loop through an array, there’s often neater ways to do it.

![Image](https://cdn-media-1.freecodecamp.org/images/nR8ENaf2lEQW1NzZH9sxELuxxwm3C1oFrNDf)
_[source](https://unsplash.com/photos/wKTF65TcReY" rel="noopener" target="_blank" title=")_

#### The for…in loop

The `for ... in` loop eliminates the two major weaknesses of the `for` loop. There’s no need to think of a counter or an exit condition.

```js
const numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

for (const index in numbers) {
  console.log(numbers[index]);
}
```

Prints:

> 0  
>  1  
>  2  
>  3  
>  4  
>  5  
>  6  
>  7  
>  8  
>  9

The main disadvantage of this solution is that we still need to use an index to access the elements of the array.

Another thing that can be problematic is that `for ... in` loops loop over all enumerable properties. What does it mean in practice? If you need to add an additional method to your object (in our case: array), this method will also appear in your loop.

Have a look at this example:

```js
Array.prototype.decimalfy = function() {
  for (let i = 0; i < this.length; i++) {
    this[i] = this[i].toFixed(4);
  }
};

const numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

for (const index in numbers) {
  console.log(numbers[index]);
}
```

Prints:

> 0  
>  1  
>  2  
>  3  
>  4  
>  5  
>  6  
>  7  
>  8  
>  9  
>  function() {  
>  for (let i = 0; i < this.length; i++) {  
>  this[i] = this[i].toFixed(2);  
>  }  
>  }

I guess you’ll agree that it’s not exactly what we were after. When looping over arrays, try to stay away from the `for ... in` loops to avoid unexpected surprises.

![Image](https://cdn-media-1.freecodecamp.org/images/SGFyxaY3XVEM7kIYdpwHLHVREdS1C4cjKm3b)
_[source](https://pixabay.com/en/tiger-and-turtle-duisburg-looping-1940551/" rel="noopener" target="_blank" title=")_

#### The for … of loop

The for…of loop is the newest addition to the family of `for` loops in JavaScript.

It combines the strengths of the `for` loop and the `for ... in` loop, allowing you to loop over any type of data type that is iterable (= follows the [iterable protocol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols)), such as string, array, set or map. Note that object ( `{}`) is not iterable by default.

The syntax of a `for ... of` loop is almost the same as of a `for ... in` loop:

```js
const numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

for (const number of numbers) {
  console.log(number);
}
```

Prints:

> 0  
>  1  
>  2  
>  3  
>  4  
>  5  
>  6  
>  7  
>  8  
>  9

One big advantage is that we no longer need an index and can access elements or our array directly. It makes the `for ... of` loop the most compact of the whole family of for loops.

In addition, the `for ... of` loop mechanism allows for a loop break, depending on your condition. Have a look at this example:

```js
const numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

for (const number of numbers) {
  if (number % 2 !== 0) {
    continue;
  }
  console.log(number);
}
```

Prints:

> 0  
>  2  
>  4  
>  6  
>  8

Furthermore, adding new methods to objects doesn’t affect the `for ... of` loop:

```js
Array.prototype.decimalfy = function() {
  for (i = 0; i < this.length; i++) {
    this[i] = this[i].toFixed(4);
  }
};
const numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
for (const number of numbers) {
  console.log(number);
}
```

Prints:

> 0  
>  1  
>  2  
>  3  
>  4  
>  5  
>  6  
>  7  
>  8  
>  9

This makes the `for ... of` loop the most potent of all!

#### Side note: the forEach loop

What might also be worth mentioning is a `forEach` loop. Note, however, that `forEach()` is an array method and therefore cannot be used on other JavaScript objects. This method can be useful if your case meets two conditions: you want to loop over an array and you don’t need to stop the loop before the end of that array:

```js
const numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

numbers.forEach(function(number) {
  console.log(number);
});
```

Prints:

> 0  
>  1  
>  2  
>  3  
>  4  
>  5  
>  6  
>  7  
>  8  
>  9

I hope these examples helped you wrap your head around all the different mechanics of iteration in JavaScript.

Are you just starting your journey with programming? Here’s some articles that might interest you as well:

* [Is a coding bootcamp something for you?](https://medium.freecodecamp.org/is-a-coding-bootcamp-something-for-you-974c3b5bd3b2)
* [Is career change really possible?](https://medium.com/datadriveninvestor/is-career-change-really-possible-c29c9a0d791c)
* [Why Ruby is a great language to start programming with](https://medium.com/@aska.gaudyn/why-ruby-is-a-great-language-to-start-programming-with-2f17e0c2907a)

