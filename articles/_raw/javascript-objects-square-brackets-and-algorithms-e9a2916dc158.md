---
title: JavaScript Objects, Square Brackets and Algorithms
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-10T20:58:59.000Z'
originalURL: https://freecodecamp.org/news/javascript-objects-square-brackets-and-algorithms-e9a2916dc158
coverImage: https://cdn-media-1.freecodecamp.org/images/1*UNpp95VAxeCcyKy8z6w_oA.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: Computer Science
  slug: computer-science
- name: JavaScript
  slug: javascript
- name: learning to code
  slug: learning-to-code
- name: software development
  slug: software-development
seo_title: null
seo_desc: 'By Dmitri Grabov

  One of the most powerful aspects of JavaScript is being able to dynamically refer
  to properties of objects. In this article we will look at how this works and what
  advantages this might give us. We will take a quick look at some of t...'
---

By Dmitri Grabov

One of the most powerful aspects of JavaScript is being able to dynamically refer to properties of objects. In this article we will look at how this works and what advantages this might give us. We will take a quick look at some of the data structures used in Computer Science. In addition we will look at something called Big O notation which is used to describe the performance of an algorithm.

### Objects intro

Let’s begin by creating a simple object representing a car. Each object has something called `properties`. A property is a variable that belongs to an object. Our car object will have three properties: `make`, `model` and `color`.

Let’s see what it could look like:

```
const car = {  make: 'Ford',  model: 'Fiesta',  color: 'Red'};
```

We can refer to individual properties of an object using dot notation. For example, if we wanted to find out what the color of our car is, we can use dot notation like this `car.color`.

We could even output it using `console.log`:

```
console.log(car.color); //outputs: Red
```

Another way to refer to a property is using square bracket notation:

```
console.log(car['color']); //outputs: Red
```

In the above example, we use the property name as a string inside square brackets to get the value corresponding to that property name. The useful thing about square bracket notation is that we can also use variables to get properties dynamically.

That is, rather than hardcoding a specific property name, we can specify it as a string in a variable:

```
const propertyName = 'color';const console.log(car[propertyName]); //outputs: Red
```

### Using dynamic lookup with square bracket notation

Let’s look at an example where we can use this. Let’s say we run a restaurant and we want to be able to get the prices of items on our menu. One way doing this is using `if/else` statements.

Let’s write a function which will accept an item name and return a price:

```
function getPrice(itemName){  if(itemName === 'burger') {    return 10;  } else if(itemName === 'fries') {    return 3;  } else if(itemName === 'coleslaw') {    return 4;  } else if(itemName === 'coke') {    return 2;  } else if(itemName === 'beer') {    return 5;  }}
```

While the above approach works, it’s not ideal. We have hardcoded the menu in our code. Now if our menu changes, we will have to rewrite our code and redeploy it. In addition, we could have a long menu and having to write all this code would be cumbersome.

A better approach would be to separate our data and our logic. The data will contain our menu and the logic will look up prices from that menu.

We can represent the `menu` as an object where the property name, also known as a key, corresponds to a value.

In this case the key will be the item name and value will be the item price:

```
const menu = {  burger: 10,  fries: 3,  coleslaw: 4,  coke: 2,  beer: 5};
```

Using square bracket notation we can create a function which will accept two arguments:

* a menu object
* a string with item name

and return the price of that item:

```
const menu = {  burger: 10,  fries: 3,  coleslaw: 4,  coke: 2,  beer: 5};
```

```
function getPrice(itemName, menu){  const itemPrice = menu[itemName];  return itemPrice;}
```

```
const priceOfBurger = getPrice('burger', menu);console.log(priceOfBurger); // outputs: 10
```

The neat thing about this approach is that we have separated our data from our logic. In this example, the data lives in our code, but it could just as easily be coming from a database or API. It is no longer tightly coupled with our lookup logic which converts item name to item price.

### Datastructures and algorithms

A map in Computer Science terms is a data structure which is a collection of key/value pairs where each key maps to a corresponding value. We can use it to look a value which corresponds to a specific key. This is what we are doing in the previous example. We have a key which is an item name and we can look up the corresponding price of that item using our menu object. We are using an object to implement a map data structure.

Let’s look at an example of why we may want to use a map. Let’s say we run a book shop and have a list of books. Each book has a unique indentifier called International Standard Book Number (ISBN), which is a 13 digit number. We store our books in an array and want to be able to look them up using the ISBN.

One way of doing so is by looping over the array, checking the ISBN value of each book and if it matches returning it:

```
const books = [{  isbn: '978-0099540946',  author: 'Mikhail Bulgakov',  title: 'Master and Margarita'}, {  isbn: '978-0596517748',  author: 'Douglas Crockford',  title: 'JavaScript: The Good Parts'}, {  isbn: '978-1593275846',  author: 'Marijn Haverbeke',  title: 'Eloquent JavaScript'}];
```

```
function getBookByIsbn(isbn, books){  for(let i = 0; i < books.length; i++){    if(books[i].isbn === isbn) {      return books[i];    }  }}
```

```
const myBook = getBookByIsbn('978-1593275846', books);
```

That works fine in this example since we only have three books (it’s a small book shop). However, if we were Amazon, iterating over millions of books could be very slow and computationally expensive.

[Big O notation](https://rob-bell.net/2009/06/a-beginners-guide-to-big-o-notation/) is used in Computer Science to describe the performance of an algorithm. For example if _n_ is the number of books in our collection, the cost of using iteration to look up a book in the worst case scenario (the book we look for is last in the list) will be _O(n)_. That means if the number of books in our collection doubles, the cost of finding a book using iteration will double as well.

Let’s take a look at how we can make our algorithm more efficient by using a different data structure.

As discussed, a map can be used to look up the value which corresponds to a key. We can structure our data as map instead of an array by using an object.

The key will be the ISBN and the value will be the corresponding book object:

```
const books = {  '978-0099540946':{    isbn: '978-0099540946',    author: 'Mikhail Bulgakov',    title: 'Master and Margarita'  },  '978-0596517748': {    isbn: '978-0596517748',    author: 'Douglas Crockford',    title: 'JavaScript: The Good Parts'  },  '978-1593275846': {    isbn: '978-1593275846',    author: 'Marijn Haverbeke',    title: 'Eloquent JavaScript'  }};
```

```
function getBookByIsbn(isbn, books){  return books[isbn];}
```

```
const myBook = getBookByIsbn('978-1593275846', books);
```

Instead of using iteration, we can now use a simple map lookup by ISBN to get our value. We no longer need to check the ISBN value for each object. We get the value directly from the map using the key.

In terms of performance, a map lookup will provide a huge improvement over iteration. This is because the map lookup has constant cost in terms of computation. This can be written using Big O notation as _O(1)_. It does not matter if we have three or three million books, we can get the book we want just as fast by doing a map lookup using the ISBN key.

### Recap

* We have seen we can access the values of object properties using dot notation and square bracket notation
* We learned how we can dynamically look up values of property by using variables with square bracket notation
* We have also learned that a map datastructure maps keys to values. We can use keys to directly look up values in a map which we implement using an object.
* We had a first glance at how algorithm performance is described using _Big O_ notation. In addition, we saw how we can improve the performance of a search by converting an array of objects into a map and using direct lookup rather than iteration.

Want to test your new found skills? Try the [Crash Override](https://www.codewars.com/kata/crash-override/javascript) exercise on Codewars.

Want to learn how to write web applications using JavaScript? I run [Constructor Labs](http://constructorlabs.com/), a 12 week [JavaScript coding bootcamp](http://constructorlabs.com/course) in London. The technologies taught include **HMTL**, **CSS**, **JavaScript**, **React**, **Redux**, **Node** and **Postgres**. Everything you need to create an entire web app from scratch and get your first job in the industry. Fees are £3,000 and next cohort starts on 29th May. [Applications are open now](http://constructorlabs.com/admission).

