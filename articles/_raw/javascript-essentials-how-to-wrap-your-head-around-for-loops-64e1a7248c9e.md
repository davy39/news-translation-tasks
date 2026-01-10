---
title: 'JavaScript Essentials: how to wrap your head around for loops'
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2017-12-13T17:04:02.000Z'
originalURL: https://freecodecamp.org/news/javascript-essentials-how-to-wrap-your-head-around-for-loops-64e1a7248c9e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*TqBCXYI6enDiSuoVEOeVoA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'Let’s say you want to run a function, bounceBall, four times. How would
  you do it? Like this?

  function bounceBall() {   // bounce the ball here }

  bounceBall() bounceBall() bounceBall() bounceBall()

  This approach is great if you need to bounceBall onl...'
---

Let’s say you want to run a function, `bounceBall`, four times. How would you do it? Like this?

```
function bounceBall() {   // bounce the ball here } 
```

```
bounceBall() bounceBall() bounceBall() bounceBall()
```

This approach is great if you need to `bounceBall` only for a few times. What happens if you need to `bounceBall` for a hundred times?

The better way is through a `for` loop.

### The ‘for’ loop

The `for` loop runs a block of code as many times as you want to. Here’s a for loop that runs `bounceBall` ten times:

```
for (let i = 0; i < 10; i++) {   bounceBall() }
```

It’s broken down into four parts — the `initialExpression`, the `condition`, the `incrementalExpression` , and the `statement`:

```
for (initialExpression; condition; incrementExpression) {   statement }
```

Before you loop, you need to have a **statement**. This statement is the block of code you’d like to run multiple times. You can write any number of lines of code here. You can even use functions.

Here’s what the `for` loop looks like with `bounceBall` as its statement:

```
for (initialExpression; condition; incrementExpression) {     bounceBall() }
```

Next, you need an **initial expression** to begin a loop. This is where you declare a variable. For most loops, this variable is called `i`. It’s also set to 0.

Here’s how it’ll look like when you put the `initialExpression` into the `for` loop:

```
for (let i = 0; condition; incrementExpression) {   bounceBall() }
```

After the statement runs, the variable, `i` is increased or decreased. You increase or decrease the value of `i` in the **increment expression**.

To increase the value of `i` by one, you reassign `i` such that it becomes `i + 1` with `i = i + 1`. The shorthand for this reassignment is `i++`, which is what you’ll find in most `for` loops.

To decrease the value of `i` by one, you reassign `i` such that it becomes `i - 1` with `i = i - 1`. The shorthand for this reassignment is `i--`, which is another variation of what you’ll find in most `for` loops.

In the `bounceBall` example above, we increased the variable `i` by one each time the code runs:

```
for (let i = 0; condition; i++) {   bounceBall() }
```

But should you increase or decrease `i`?

The answer lies in the **condition**. This condition statement evaluates either to `true` or `false`. If the statement evaluates to `true`, the statement runs.

When the statement has ran, JavaScript runs the increment expression and checks if the condition evaluates to `true` again. It repeats this process until the condition evaluates to `false`.

Once the condition evaluates to `false`, JavaScript skips the loop and moves on with the rest of your code.

So, if you do not want the loop to run, you can set a condition that evaluates to false immediately:

```
// This loop will not run since the condition evaluates to false for (let i = 0; i < 0; i++) {   bounceBall()   const timesBounced = i + 1   console.log('The ball has bounced ' + timesBounced + ' times') } 
```

```
// You will only see this console.log('next line of code')
```

![Image](https://cdn-media-1.freecodecamp.org/images/SXFTUbdOUIUpS6r2614f1jst5qkyyZzIYh3h)

If you want the loop to **run twice**, you change the condition such that it evaluates to false when the increment expression has run twice.

```
// This loop will run twice for (let i = 0; i < 2; i++) {   bounceBall()   const timesBounced = i + 1   console.log('The ball has bounced ' + timesBounced + ' times')") } 
```

```
console.log('next line of code')
```

![Image](https://cdn-media-1.freecodecamp.org/images/5ssuIegeT3CruvHrbE9cDiw2Hgzhz4h7SQbA)

If you want the loop to **run ten times**, you change the condition such that it evaluates to false when the increment expression has run ten times.

```
// This loop will run ten times for (let i = 0; i < 10; i++) {   bounceBall()   const timesBounced = i + 1   console.log('The ball has bounced ' + timesBounced + ' times')") } 
```

```
console.log('next line of code')
```

![Image](https://cdn-media-1.freecodecamp.org/images/b15Gl3ujfERmjQFZ5cc9GHXo9OB2lBsmj7l4)

### Infinite loops

Infinite loops occur when the **condition** for your `for` loops always return `true`. Your browser will hang if you run an infinite loop.

To recover from an infinite loop, you need to quit your browser forcefully. On a Mac, this means you right click on your browser icon and select “force quit.” On a Window’s machine, you open the Windows Task manager with `ctrl` + `alt` + `del`, select your browser, and click “End task.”

### Looping through arrays

In practice, you almost never write a loop that runs ten times like in the `bounceBall` example above. You’d always loop through an array or a object.

When you loop (or iterate) through an array, you go through each item in the array once. To do so, you can use the length or the array as a condition:

```
const fruitBasket = ['banana', 'pear', 'guava'] 
```

```
// fruitBasket.length is 3 for (let i = 0; i < fruitBasket.length; i++) {   console.log("There's a " + fruitBasket[i] + " in the basket") } 
```

```
// => There's a banana in the basket // => There's a pear in the basket // => There's a guava in the basket
```

The alternate way to write this `for` loop is to use a negative increment expression. This version runs slightly faster than the `for` loop above, but loops the array from the end instead.

```
for (let i = fruitBasket.length - 1; i >= 0; i--) {  console.log("There's a " + fruitBasket[i] + " in the basket") } 
```

```
// => There's a guava in the basket // => There's a pear in the basket // => There's a banana in the basket
```

### Looping through arrays with “for of”

Yet another (much better) way to loop through an array is to use a `for...of` loop. This is a new loop syntax that comes with ES6. It looks like this:

```
const fruitBasket = ['banana', 'pear', 'guava'] 
```

```
for (let fruit of fruitBasket) {   console.log(fruit) } 
```

```
// => There's a banana in the basket // => There's a pear in the basket // => There's a guava in the basket
```

The `for...of` loop is preferable to the standard `for` loop because it always loops through the array once. There’s no need to write `array.length`, which makes your code much easier to read and maintain.

You can use `for...of` with any iterable object. These are objects that contain the `Symbol.iterator` property. Arrays are one such object. If you `console.log` an empty array, you’ll see that it has the `Symbol.iterator` as one of its keys (within the Array `__proto__` key):

![Image](https://cdn-media-1.freecodecamp.org/images/MKAx1db1lQjOZE9FAG2A06V4H6nGBN41rLRA)

### Logic in loops

You can use `if/else` or any other logic within a for loop.

For example, let’s say you have a list of numbers, and you want to create a second list of numbers that are smaller that 20.

To complete this objective, you first loop through the numbers.

```
const numbers = [25, 22, 12, 56, 8, 18, 34]
```

```
for (let num of numbers) {   // do something here }
```

Here, you want to check if each `num` is smaller than 20.

```
const numbers = [25, 22, 12, 56, 8, 18, 34]
```

```
for (let num of numbers) {   if (num < 20) {     // do something   } }
```

If `num` is smaller than 20, you want to add it to another array. To do so, you use the `push` method.

```
const numbers = [25, 22, 12, 56, 8, 18, 34]let smallerThan20 = [] 
```

```
for (let num of numbers) {   if (num < 20) {     smallerThan20.push(num)   } } 
```

```
// smallerThan20 === [12, 8 , 18]
```

### Wrapping up

A `for` loop is used when you want to execute the same task (or a set of tasks) multiple times.

You would rarely loop through code for exactly ten times. Normally, you’ll want to loop through an array instead.

To loop through an array exactly once, you can use the `for...of` loop, which is much easier to write and understand compared to the traditional `for` loop.

Remember, you can write any amount of logic you want in loops. You can use functions, `if/else` statements, or even use loops in loops.

If you loved this article, you’ll love learn **Learn JavaScript** — a course that helps you learn to **build real components from scratch** with Javascript. [Click here to find out more about Learn JavaScript](https://learnjavascript.today/) if you’re interested.

(Oh, by the way, if you liked this article, I’d appreciate it if you could [share it](http://twitter.com/share?text=Understanding%20Javascript%20for%20Loops%3A%20you%20can%20write%20any%20amount%20of%20logic%20you%20want%20in%20loops.%20You%20can%20use%20functions%2C%20%60if%2Felse%60%20statements%20or%20even%20use%20loops%20in%20loops%20?%20&url=https://zellwk.com/blog/js-for-loops/&hashtags=). ?)

_Originally published at [zellwk.com](https://zellwk.com/blog/js-for-loops/)._

