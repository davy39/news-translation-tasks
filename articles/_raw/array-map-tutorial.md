---
title: JavaScript Array.map() Tutorial – How to Iterate Through Elements in an Array
  with map()
subtitle: ''
author: Kingsley Ubah
co_authors: []
series: null
date: '2021-08-19T16:16:57.000Z'
originalURL: https://freecodecamp.org/news/array-map-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/array-map.png
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'When ES6 (EmcaScript 2015) came out, it ushered in a whole new set of methods
  for iterating over an array. And one of the most useful is the map() method.

  Array.prototype.map() is a built-in array method for iterating through the elements
  inside an a...'
---

When ES6 (EmcaScript 2015) came out, it ushered in a whole new set of methods for iterating over an array. And one of the most useful is the `map()` method.

`Array.prototype.map()` is a built-in array method for iterating through the elements inside an array collection in JavaScript. Think of looping as a way to progress from one element to another in a list, while still maintaining the order and position of each element.

This method [takes in a callback function](https://www.freecodecamp.org/news/what-is-a-callback-function-in-javascript/) which gets called for every new element it iterates over.

The callback function takes in three parameters:

* The current value
    
* It's index
    
* The target array
    

If you are a beginner struggling to understand how to use the `map()` method or what exactly it does, then this article is for you.

In this article, I will explain the `map()` method and illustrate how it works with some simple examples.

## How the map() Method Works in JavaScript

Imagine this: there is a queue of people outside a hospital waiting to be vaccinated. This means that they are yet to be vaccinated.

One-by-one, a doctor administers the vaccination to all of them. The doctor does this by iterating through the line. On one end, there is a group of people who are yet to be vaccinated. The doctor took each and every one of them, administered the vaccine to them, and returned them into a **new** line of vaccinated people.

On one end, there is an array (A) you want to operate on. `map()` takes in all elements in that array (A), performs a consistent action on each of those elements, and returns them into a new array (B).

## How to Use the map() method – Avengers Example

To illustrate how `map()` works in JavaScript, let's consider a list of names of some of our favourite Avengers. The problem is that the names in this list are not complete – they are missing an important suffix.

With `map()`, we can take all names in the array and append the "man" suffix to each and every one of them:

```js
let firstNames = ["super", "spider", "ant", "iron"]
let lastName = "man";

let fullNames = firstNames.map(firstName => firstName + lastName);

console.log(fullNames);

// ["superman", "spiderman", "antman", "ironman"]
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/map1-1.png align="left")

*VISUAL CODE*

### What about the women?

Sorry, my bad. I realized my mistake and decided to include a female character at the **first** position in the Array. Each item within an array is identified by a unique value, its **index** (or position in the array). The first item will have an index of `0`, the second an index of `1`, and so on.

Since there is now a female superhero on the list, we will want to make sure we append the right suffix to the appropriate superhero.

Since `map()` also takes in the index of the item we are currently iterating over, we can do this by checking for the index of our hero and making sure we use the "woman" suffix for the first item on our array:

```js
let firstNames = ["wonder", "spider", "ant", "iron"]
let male = "man";
let female = "woman";

let fullNames = firstNames.map(function(firstName, index) {
    return (index == 0) ? firstName + female : firstName + male;
 });

console.log(fullNames);

["wonderwoman", "spiderman", "antman", "ironman"]
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/map--8.png align="left")

### How to Use the Index Argument

In addition to the value being iterated over, map takes in its index position as well. This is very useful if you want to perform different kinds of operations depending on the index position of the item.

In the previous example, we appended a different suffix by checking for the index.

To find out the index position of each of our items within the array, we can do this:

```js
let fullNames = ["wonderwoman", "spiderman", "antman", "ironman"]

fullNames.map(function(firstName, index) {
    console.log(${firstName} is at ${index} position)
});

/*
"wonderwoman is at 0 position"
"spiderman is at 1 position"
"antman is at 2 position"
"ironman is at 3 position"
*/
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/map--1.png align="left")

*RESULT*

### How to Multiply All Items in the Array by 2

Let's work a bit with numbers now. In this example, we simply want to multiply every number in the target array by two and then return their products into a new array:

```js
let numbers = [10, 20, 30, 40]
let multiplier = 2;

let products = numbers.map(number => number * multiplier);

console.log(products);

// [20, 40, 60, 80]
```

### How to Round to the Nearest Integer

What if we have an array of decimals but we want each of those decimal numbers to be rounded to the nearest integer?

```c
let numbers = [3.7, 4.9, 6.2]
let rounded = numbers.map(function(number) {
    return Math.round(number);
})

console.log(rounded);

// [4, 5, 6]
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/map--2.png align="left")

### How to Change Strings to Numbers

We have a list of numbers which are of the string type. However, we want to convert each one to the number type:

```js
let strings = ["10","20","30"]

let numbers = strings.map(function(string) {
    return Number(string);
})

console.log(numbers);

// [10, 20, 30]
```

### How to Get the Avengers' Real Names

In this example, we are working with objects. We have five avengers in the array, and each one has both a real name and a hero name. However, we only want to retrieve their real names into the new array.

```js
let avengers = [
    {name: "steve rogers", heroName: "captain america"},
    {name: "tony stark", heroName: "iron man"},
    {name: "bruce banner", heroName: "the hulk"},
    {name: "peter parker", heroName: "spiderman"},
    {name: "tchalla", heroName: "black panther"}
]

let realNames = avengers.map(avenger => avenger.name);

console.log(realNames);

// ["steve rogers", "tony stark", "bruce banner", "peter parker", "tchalla"]
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/map--5-1.png align="left")

### How to Get the Avengers' Hero Names

To get only their hero names, we do almost the exact same thing, only in this case we access the `heroName` property:

```js
let avengers = [
    {name: "steve rogers", heroName: "captain america"},
    {name: "tony stark", heroName: "iron man"},
    {name: "bruce banner", heroName: "the hulk"},
    {name: "peter parker", heroName: "spiderman"},
    {name: "tchalla", heroName: "black panther"}
]

let heroNames = avengers.map(avenger => avenger.heroName);

console.log(heroNames);

// ["captain america", "iron man", "the hulk", "spiderman", "black panther"]
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/map--10.png align="left")

### How to Separate Out a Function

Instead of defining a function directly inside of `map()`, we can define the function outside and then call it inside our `map()` function:

```js
let avengers = [
    {name: "steve rogers", heroName: "captain america"},
    {name: "tony stark", heroName: "iron man"},
    {name: "bruce banner", heroName: "the hulk"},
    {name: "peter parker", heroName: "spiderman"},
    {name: "tchalla", heroName: "black panther"}
]

let getName = avenger =>avenger.name;

let realNames = avengers.map(getName);

console.log(realNames);

// ["steve rogers", "tony stark", "bruce banner", "peter parker", "tchalla"]
```

### How the Array Argument Works

Earlier I stated that on every iteration, the `map()` method takes in the value being iterated over and also its index position. There is another argument to add to those two, the `Array` argument.

The `arr` argument represents the target array being looped over, along with its entire content. With this argument, you can essentially look into the full array to find something.

In this example, we will access the `arr` parameter to look in and check if the current item is the last item in the list. If it is not, we access the next item and subtract it from the current item. If it is the last, we just return it.

```js
const oldArray = [33, 20, 10, 5];
const newArray = oldArray.map((currentVal, index, arr) => {
    let nextItem = index + 1 < arr.length ? arr[index + 1] : 0
    return currentVal - nextItem;
	});


console.log(newArray);

// [13, 10, 5, 5]
```

## Wrapping Up

The `map()` method was introduced in ES6. With this method, we can access and perform a consistent action on every single item inside an array collection.

It takes in a callback function which it calls for every new element it iterates over.

In this tutorial, I have introduced the map() method, illustrated how it works with an analogy and given some practical examples of its usage in JavaScript code.

I hope you got something useful from this piece. If you like programming-related tutorials like this, you should [check out my blog](https://ubahthebuilder.tech). I regularly publish articles on software development there.

Thank you for reading and see you soon.

**P/S**: If you are learning JavaScript, I created an eBook which teaches 50 topics in JavaScript with hand-drawn digital notes. [Check it out here](https://ubahthebuilder.gumroad.com/l/js-50).
