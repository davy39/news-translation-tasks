---
title: JavaScript Arrays - How to Create an Array in JavaScript
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2022-05-16T18:17:35.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-an-array-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/jexo-73REk-BB7-Y-unsplash.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "An array is a type of data structure where you can store an ordered list\
  \ of elements. \nIn this article, I will show you 3 ways you can create an array\
  \ using JavaScript.  I will also show you how to create an array from a string using\
  \ the split() meth..."
---

An array is a type of data structure where you can store an ordered list of elements. 

In this article, I will show you 3 ways you can create an array using JavaScript.  I will also show you how to create an array from a string using the `split()` method.

## How to create an array in JavaScript using the assignment operator

The most common way to create an array in JavaScript would be to assign that array to a variable like this:

```js
const books = ["The Great Gatsby", "War and Peace", "Hamlet", "Moby Dick"];
```

If we `console.log` the array, then it will show us all 4 elements listed in the array. 

```js
const books = ["The Great Gatsby", "War and Peace", "Hamlet", "Moby Dick"];

console.log(books);
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-01-at-11.11.38-PM.png)

## How to create an array in JavaScript using the new operator and Array constructor

Another way to create an array is to use the `new` keyword with the `Array` constructor. 

Here is the basic syntax:

```js
new Array();
```

If a number parameter is passed into the parenthesis, that will set the length for the new array.

In this example, we are creating an array with a length of 3 empty slots.

```js
new Array(3)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-14-at-11.07.33-PM.png)

If we use the length property on the new array, then it will return the number 3.

```js
new Array(3).length
```

But if we try to access any elements of the array, it will come back undefined because all of those slots are currently empty.

```js
new Array(3)[0]
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-14-at-11.10.02-PM.png)

We can modify our example to take in multiple parameters and create an array of food items.

```js
let myFavoriteFoods = new Array("pizza", "ice cream", "salad");

console.log(myFavoriteFoods); // ["pizza","ice cream","salad"]
console.log(myFavoriteFoods.length); // 3
console.log(myFavoriteFoods[1]); // "ice cream"
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-14-at-11.13.48-PM.png)

## How to create an array in JavaScript using Array.of()

Another way to create an array is to use the `Array.of()` method. This method takes in any number of arguments and creates a new array instance. 

Here is the basic syntax:

```js
Array.of(); 
```

We can modify our earlier food example to use the `Array.of()` method like this.

```js
let myFavoriteFoods = Array.of("pizza", "ice cream", "salad");

console.log(myFavoriteFoods); // ["pizza","ice cream","salad"]
console.log(myFavoriteFoods.length); // 3
console.log(myFavoriteFoods[1]); // "ice cream"
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-14-at-11.47.54-PM.png)

This method is really similar to using the Array constructor. The key difference is that if you pass in a single number using  `Array.of()` it will return an array with that number in it. But the Array constructor creates x number of empty slots for that number.

In this example it would return an array with the number 4 in it.

```js
let myArr = Array.of(4);

console.log(myArr);
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-15-at-12.00.27-AM.png)

But if I changed this example to use the Array constructor, then it would return an array of 4 empty slots. 

```js
let myArr = new Array(4);

console.log(myArr);
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-15-at-12.02.03-AM.png)

## How to create an array from a string using the split() method

Here is the syntax for the JavaScript `split()` method.

```js
str.split(optional-separator, optional-limit)
```

The optional separator is a type of pattern that tells the computer where each split should happen.

The optional limit parameter is a positive number that tells the computer how many substrings should be in the returned array value.

In this example, I have the string `"I love freeCodeCamp"`. If I were to use the `split()` method without the separator, then the return value would be an array of the entire string.

```js
const str = 'I love freeCodeCamp';

console.log(str.split());
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-15-at-12.09.10-AM.png)

If I wanted to change it so the string is split up into individual characters, then I would need to add a separator. The separator would be an empty string.

```js
const str = "I love freeCodeCamp";

console.log(str.split(""));
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-15-at-12.10.58-AM.png)

Notice how the spaces are considered characters in the return value.

If I wanted to change it so the string is split up into individual words, then the separator would be an empty string with a space.

```js
const str = "I love freeCodeCamp";

console.log(str.split(" "));
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-15-at-12.11.32-AM.png)

## Conclusion

In this article I showed you three ways to create an array using the assignment operator, Array constructor, and `Array.of()` method. 

The most common way to create an array in JavaScript would be to assign that array to a variable like this:

```js
const books = ["The Great Gatsby", "War and Peace", "Hamlet", "Moby Dick"];
```

Another way to create an array is to use the `new` keyword with the `Array` constructor.

```js
new Array();
```

If a number parameter is passed into the parenthesis, that will set the length for the new array with that number of empty slots.

For example, this code will create an array with a length of 3 empty slots.

```js
new Array(3)
```

We can also pass in multiple parameters like this:

```js
let myFavoriteFoods = new Array("pizza", "ice cream", "salad");

console.log(myFavoriteFoods); // ["pizza","ice cream","salad"]
```

Another way to create an array is to use the `Array.of()` method. This method takes in any number of arguments and creates a new array instance.

```js
Array.of(); 
```

You can also take a string and create an array using the `split()` method

```js
str.split(optional-separator, optional-limit)
```

I hope you enjoyed this article on JavaScript arrays. 

