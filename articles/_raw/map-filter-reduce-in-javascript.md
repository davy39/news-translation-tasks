---
title: How to Use map(), filter(), and reduce() in JavaScript
subtitle: ''
author: Bhavesh Rawat
co_authors: []
series: null
date: '2022-10-03T22:06:51.000Z'
originalURL: https://freecodecamp.org/news/map-filter-reduce-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/fCC-blog-2.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'If you want to learn React, it''s important to get a fair understanding
  of some core JavaScript concepts first.

  So if that''s what you''re doing, first of all – great job! You have made a wise
  decision by not starting directly with React.

  Second, React ...'
---

If you want to learn React, it's important to get a fair understanding of some core JavaScript concepts first.

So if that's what you're doing, first of all – great job! You have made a wise decision by not starting directly with React.

Second, React builds on key concepts like the map(), filter(), and reduce() JavaScript methods (after all – React is a JavaScript library). So this makes these methods a must-learn.

Map, filter, and reduce are three of the most useful and powerful high-order array methods. In this tutorial, you'll see how each of these high-order array methods work. You'll also learn where you'll want to use them and how to use them, with the help of analogies and examples. It’ll be fun!

## How to Use the `map()` Method

Suppose you have an array `arrOne` where you’ve stored some numbers, and you’d like to perform some calculations on each of them. But you also **don’t want to mess with the original array**.

This is where `map()` comes into the picture. The `map` method will help you do this:

```javascript
let arrOne = [32, 45, 63, 36, 24, 11]
```

map() takes a maximum of three arguments, which are value/element, index, and array.

```javascript
arrOne.map(value/element, index, array)
```

Let’s say you want to multiply each element by 5 while not changing the original array.

Here's the code to do that:

```js
let arrOne = [32, 45, 63, 36, 24, 11]
const multFive = (num) => {
return num * 5; //'num' here, is the value of the array.
}
let arrTwo = arrOne.map(multFive)
console.log(arrTwo)
```

And here's the output:

```js
[ 160, 225, 315, 180, 120, 55 ]
```

So what's going on here? Well, I have an `arrOne` array with 6 elements in it. Next, I initialized an arrow function `multFive` with ‘num’ as an argument. This returns the product of `num` and 5, where the ‘num’ variable is fed the data by the map() method.

If you’re new to arrow functions but are familiar with regular functions, an arrow function is the same as this:

```js
function(num) 
	{  
    	return num * 5;
    }
```

Then, I initialized another variable `arrTwo` that will store the new array that the map() method will create.

On the right-hand side, I called the map() method on the ‘arrOne’ array. So, the map() method will pick each value of that array starting from the index\[0\] and perform the desired calculation on each value. Then it'll form a new array with the calculated values.

**Important**: Notice how I’m stressing not changing the original array. That is because this property is what makes the map() method different from the ‘forEach()’ method. The map() method makes a new array whereas the ‘forEach()’ method mutates/changes the original array with the calculated array.

## How to Use the `filter()` Method

The name kind of gives it away, doesn't it? You use this method to filter the array based on conditions you provide. The filter() method also creates a new array.

**Let’s take an example**: Suppose you have an array `arrName` and that array stores a bunch of numbers. Now, you would like to see what numbers can be divided by 3 and make a separate array from them.

Here's the code to do that:

```js
let arrNum = [15, 39, 20, 32, 30, 45, 22]
function divByFive(num) {
  return num % 3 == 0
}
let arrNewNum = arrNum.filter(divByFive)
console.log(arrNewNum)
```

And here's the output:

```js
[ 15, 39, 30, 45 ]
```

Let's break down this code. Here, I have an array `arrNum` with 7 elements in it. Next, I initialized a function `divByFive` with ‘num’ as an argument. It returns true or false for each time a new num is passed for the comparison, where the ‘num’ variable is fed the data by the filter() method.

Then, I initialized another variable `arrNewNum` that will store the new array that the filter() method will create.

On the right-hand side, I called the filter() method on the `arrNum` array. So, the filter() method will pick each value of that array starting from the index\[0\] and perform the operation on each value. Then it'll form a new array with the calculated values.

## How to Use the reduce() Method

Let’s say you are asked to find the sum of all elements of an array. Now, you could use a for loop or the forEach() method, but reduce is built for this kind of task.

The `reduce()` method reduces an array to a single value by performing the desired operation on the elements collectively.

Let’s take the above example and use reduce on it:

```js
let arrNum = [15, 39, 20, 32, 30, 45, 22]
function sumOfEle(num, ind) {
  return num + ind;
}
let arrNum2 = arrNum.reduce(sumOfEle)
console.log(arrNum2)
```

Here's the output:

`203`

Everything is the same as the map() and filter() methods – but what’s important to understand is how the reduce method works under the hood.

There’s not a definite [syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce#syntax) of the reduce() method. Let’s see the simplest one and that will give you the gist of all the ways you can use reduce().

Here's some example syntax for `reduce()`:

```js
//Taking the above array for an example
let arrNum = [15, 39, 20, 32, 30, 45, 22]arr.reduce((a1, a2) => { 
 return a1 + a2
})
```

Take a look at this syntax. Here, reduce is taking two arguments, `a1` and `a2`, where `a1` acts as an accumulator while the `a2` has the index value.

Now, on the first run the accumulator is equal to zero and `a2` holds the first element of the array. What reduce does is that it throws the value in the accumulator that a2 holds and increments it to the next one. After that, the reduce() method performs the operation on both operands. In this case it is addition.

So, basically `a1` is the accumulator which is currently zero and `a2` holds 15. After the first run, the accumulator has 15 in it and `a2` is holding the next value which is 39.

So, `0 + 15 = 15`

Now, on second run, reduce throws `a2`’s value, 39 in the accumulator and then performs the operation on both operands.

So, `15 + 39 = 54`

Now, on the third run, the accumulator has a sum of 15 and 39 which is 54. `a2` now holds 20 which the reduce method throws at the accumulator which sums up to `54 + 20 = 74`.

This process keeps on going until the end of the array.

## Signing Off

Well, that’s it, everyone! Hope you have a good idea of how these high-order array methods work now. Consider sharing if you had a good time reading it and find it helpful.

Check out my latest story [here](https://medium.com/geekculture/5-reasons-why-you-should-invest-in-a-vpn-90e95e9524fe), and for my Git eBook, check [here](https://bhaveshrawat.gumroad.com/l/lets-git-it-beginners-guide-to-git-bash-commands).
