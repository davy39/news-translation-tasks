---
title: JavaScript Basics – How to Work with Strings, Arrays, and Objects in JS
subtitle: ''
author: Houssein Badra
co_authors: []
series: null
date: '2023-03-20T20:12:35.000Z'
originalURL: https://freecodecamp.org/news/javascript-basics-strings-arrays-objects
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/js.png
tags:
- name: beginner
  slug: beginner
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'JavaScript is a popular programming language that 78% of developers use.
  You can build almost anything with JavaScript.

  The problem is that many developers learn JavaScript in a very short period of time,
  without understanding some of the most essent...'
---

JavaScript is a popular programming language that 78% of developers use. You can build almost anything with JavaScript.

The problem is that many developers learn JavaScript in a very short period of time, without understanding some of the most essential features of the language.

In this article, we will cover JavaScript arrays, strings, and objects in depth so you can benefit from some of the most effective static and instance methods that the language offers.

### Here's what we'll cover in this guide:

* Instance and class methods
* How to use strings in JavaScript 
* How to use arrays in JavaScript
* How to use objects in JavaScript

## Instance and Class Methods

JavaScript is heavily object-oriented. It follows a prototype-based model, but it also offers a class syntax to enable typical OOP paradigms. 

In JavaScript, strings and arrays are objects, and every object in JavaScript is a template which has its methods and properties. Every object inherits methods and properties from its prototype. In JavaScript, every object has access to the **Object prototype**.

Static methods are methods that are available on the class level – for example the **Object.freeze()** method. Instance methods are available on the instance level – for example a created instance of an **Array** object has access to the instance methods such as **.join()**, but not the static methods.

## How to Use Strings in JavaScript

Strings are used to hold data that can be represented in text form. To create a string you can use the **String()** constructor or a string literal. Here's an example of both ways:

```javascript
 // Using a constructor

let string1 = String('String Creation');

 // Using a string literal
 
let string2 = 'String Creation';

```

Now let's learn more about instance methods. There are many instance methods, but here I'll discuss seven methods that I consider the most important.

### The .charAt() method

A lot of the time when working with strings, we want to access a character at a certain index of the string. You can do this either with the **charAt()** method or with indexing, the same way we treat an array.

```javascript
 // Let's say we want to access the first character of a given string
 
 let string = 'Hello World';
 
  // using indexing
  
 let first1 = string[0]; // output 'H' and remember that indexing starts at 0
 
  // using the charAt() method
 
 let first2 = string.charAt(0); // output 'H'
```

In JavaScript, the indexing system starts at 0 – for example the first character of a string has index of 0 and so on.

### The .toUpperCase() and .toLowerCase() methods

Now let's say we want to uppercase or lowercase a string. You can do this using the **toUpperCase()** and the **toLowerCase()** instance methods.

```javascript
 let string = 'Hello';
 
  // Let's lowercase a string
 
 let lowerCase = string.toLowerCase(); // output 'hello'
 
  // Let's upperCase a string
  
 let upperCase = string.toUpperCase(); // output 'HELLO'
```

You might use these to see if two strings hold the same word, for example 'Sam' and 'sam'. Actually 'sam' === 'Sam' evaluates to false, while  'sam'.toLowerCase() === 'Sam'.toLowerCase() evaluates to true.

### The .concat()  method

It is often necessary to join text strings together in a program to make a new text string. This is called **concatenation**.

Now for string concatenation we can use the **concat()** method. It looks like the following. An important note is that this method returns a new string without mutating the original one.

```javascript
let string = 'Hello';

 // String concatenation using the concat method
 
let string1 = string.concat(' World'); // output 'Hello World'

```

### The .indexOf() method

Now to find the index of a certain character or a set of characters of a string, we can use the **indexOf()** method. This will return the index of the first index where the passed character or set of characters occurs.

```javascript
let string = 'Hello World';

 // Let's find the index where 'H' occurs for the first time
 
let firstH = string.indexOf('H'); // output 0
 
 // Let's find the first index where 'World' occurs for the first time
 
let firstWorld = string.indexOf('World'); // output 6

 // In case a character or a set of characters   
 // doesn't occur in the string this method returns -1
 
let notThere = string.indexOf('Z'); // output -1
 
```

### The .slice() method

A substring is a subset or part of another string, or it is a contiguous sequence of characters within a string. For example, "Substring" is a substring of "Substring in JavaScript".

Now let's say we want to get a substring of a given string. We can use the **slice()** method. Slice is actually one of the most important string methods. You use it to get substrings and also to copy strings. 

Slice takes two optional parameters: the first one is where we want to start slicing and the second one is where we want to finish the slicing operation.

Let's assume that we passed **1** and **10** as parameters for the slice method. The method will then return a substring starting at index **1** and ending at index **9.** 

This means that the substring never includes the character at the ending index. An important note is to never pass an ending index higher than the string length.

```javascript
let string = 'Hello World';
 
 // to check the string length we can use the length instance property
 
let length = string.length; // output 11

 // slicing to get the substring from index 1 -> 9
 
let string1 = string.slice(1 , 10); // output 'ello Worl'

 // not passing any parameters will generate 
 // a copy of the ariginal string with no mutation
 
let copy = string.slice(); // output 'Hello World'
```

### The .split() method

The last string method that we will cover is the **split()** method. This method takes a pattern as an argument and divides the string into multiple substrings. The pattern describes where the splits occurs. This method returns an array of these substrings.

You might find yourself using this method to parse a URL or certain strings.

```javascript
let string = 'Hello World';

 // Divide a string into words
 // This can be done when the passed pattern is a space
 
let words = string.split(' '); // output ['Hello' , 'World']

 // When the passed parameter is an empty string, the output array
 // will carry each of the characters of the given string
 
let chars = string.split(''); 

 // output ["H","e","l","l","o"," ","W","o","r","l","d"]
```

There are many more methods you can learn about, but these are the ones that you will work with the most. You can learn more by reading through the official [MDN web documents](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String).

## How to Use Arrays in JavaScript

Like other programming languages, JavaScript arrays let you store a collection of data under one variable. But unlike C or C++, arrays can be returned from function calls. 

JavaScript arrays are dynamic, so you can add to or delete elements from an array. You can also have elements of multiple data types in a single array. 

Let's talk about how to create arrays in JavaScript. You can easily create an array by assigning a variable to empty brackets [ ] or by using the **Array()** constructor.

```javascript
 // Creating an array from constructor
 
let arr1 = Array();
 
 // Prefered method
 
let arr2 = [];

```

Now let's talk about seven array instance and class methods that I consider to be the most useful. 

### The .indexOf() method

To get the first index of a given array where an element occurs, we can use the **indexOf()** method. It'll look like this. If the argument passed to this method doesn't occur in the array, it will return -1.

```javascript
let array = [1, 2, 3];

 // Let's find the index where 1 occurs for thwe first time
 
let first1 = array.indexOf(1); // output 0

 // Now let's try to find 4 in the array
 
let first4 = array.indexOf(4); // output -1
```

### The .push() and .pop() methods

As I mentioned earlier, JavaScript arrays are dynamic. So we can add elements using the **push()** method and remove the last element using the **pop()** method. An important note is that both of those methods mutate the original array.

```javascript
let array = [1, 2, 3];

 // let's add 4 to the array
 
array.push(4)

console.log(array) // output [1, 2, 3, 4]

 // let's now make the array the same as before
 
let removedElement = array.pop() // output 4

console.log(array) // output [1, 2, 3]
```

Now we'll discuss some more advanced methods – the ones introduced by the ES6 update. 

### The .map() method

First, let's say that you want to create an array using data from another existing array – for example if you have an array of objects representing employees. 

Each employee object has a name property. And you want to create an array where each element is the value of the name property of the employee object at the same index of the array you have.

This is where the **map()** method comes in. It takes a callback function. Map creates a new array and never mutates the old one, and the callback expresses what you want to do with the data from the original array. It will look like this:

```javascript
let arr= [{name : 'joe'} , {name : 'john'}];

 // It is preffered to use an arrow function

let namesArr = arr.map(elem => elem.name); // output ['joe' , 'john']
```

### The .forEach() method

Are you tired of the usual for loops? They are kind of boring, I know. Luckily the **forEach()** method is here to help. 

This method takes a callback as an argument and returns nothing. It iterates over the array and runs a certain task on every element of the array. The callback expresses the task. The code for this will look like this:

```javascript
let arr= [1, 2, 3];

 // let's output each element on the console
 
arr.forEach(elem => console.log(elem));

 // output 
 // 1
 // 2
 // 3
```

### The .filter() method

Now let's say that we have an array of numbers and that we want to create an array of only the numbers that pass a certain condition. 

In this case we can use the **filter()** method which also takes a callback as an argument. The callback returns a Boolean – true if the element passes the test, otherwise false. Only elements that pass will be in the generated array and the callback expresses the test. Here's how it works:

```javascript
let arr = [1, 2, 3, 4, 5];

 // Let's create an array of numbers bigger than 3
 
let filteredArray = arr.filter(elem => elem > 3); // output [4, 5]
```

### The .some() method

Now let's say we have an array, and we want to check if there is at least one number that passes a certain test. Here comes the **some()** method. 

This method takes a callback as an argument and returns a Boolean which is true if at least one element of the array passes the test, and otherwise is false. The callback expresses the test and it will look as follows:

```javascript
let arr = [1, 2, 3, 4, 5];

 // Let's check if at least one element is bigger than 4
 
let bool = arr.some(elem => elem > 4); // output true
```

### The .sort() method

Sorting is the process of arranging data into a meaningful order so that you can analyze it more effectively.

When talking about arrays we have to mention sorting. In JavaScript the **sort()** method sorts arrays in place and returns the reference to the same array. This method mutates the array and the default sorting order is ascending.

You can implement your own sorting logic by passing a callback which expresses a comparison between two elements and returns a number. If the returned number is positive then the first of the two compared elements will occur first in the sorted array.

```javascript
let arr = [1, 2, 4, 3];

 // sorting in ascending order
 
arr.sort();

console.log(arr); // [1, 2, 3, 4]

 // using custom sort to sort in descending order
 
arr.sort((elem1 , elem2) => elem2 - elem1);

console.log(arr); // output [4, 3, 2, 1]
```

There are plenty of interesting string methods that I didn't mention and they are worth investing time in learning. If you want to do so, you can visit the [MDN official documents](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array).

## How to Use Objects in JavaScript

If you want to be a good JavaScript developer, you should really have a decent understanding of objects and the way they work. 

Almost every object you create in JavaScript inherits methods from the global **`Object`** prototype which is available globally for every object in JavaScript. An exception is null prototype objects which we're not going to talk about. All the methods I am going to talk about are mostly static.

First let's talk about how to create objects using a set of curly braces **{ }** or the **object** constructor. Here's what that looks like:

```javascript
 // Creating an object from an constructor
 
let obj1 = Object();

 // Creating an object using curly braces
 
let obj2 = {};
```

### The .assign() method

Now let's say we want to copy an object. Here comes the **assign()** static method to help us do this. I will show you how this works and a better way to do it. I'll also discuss some common mistakes many devs make when trying to copy objects.

```javascript
let obj = {age : 18};

 // Copying using the assign method
 
let new1 = {};

Object.assign(new1 , obj);

console.log(new1); // output {age : 18}

 // We can do the same with the spread operator
 
let new2 = {...obj}; // output {age : 18}
```

A common mistake is to assign a variable to an object directly. The problem with this is that objects are assigned by reference and not by value. So any changes will mutate the original object.

```javascript
let obj = {age : 18};

let obj1 = obj;

obj1.age = 17;

console.log(obj); // output {age : 17}
```

### The .freeze() and .isFrozen() methods

Let's now say that we want to make an object immutable. For this we can use the **freeze()** static method which makes it impossible to add properties, modify, or delete any of the frozen object's prototypes, methods, and properties. 

To see if an object if frozen, we can use the **isfrozen()** static method.

```javascript
let obj = {age : 18};

Object.freeze(obj);

 // Let's try to mutate this object
 
obj.age = 17; // Throws an error in strict mode

let isFrozen = Object.isFreezed(obj); // output true
```

### The .keys() and .values() methods

Now to get a list of a certain object properties we can call the **keys()** static method. To get a list of the values corresponding to its properties, we can call the **values()** static method. An important note is that the list is an array.

```javascript
let obj = {name : 'John Doe' ,age : 45};

let keys = Object.keys(obj); // output ['name', 'age']

let values = Object.values(obj); // output ['John Doe', 45]
```

You can check the [MDN web documents](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object) to dive deeper into the topic.

## Conclusion

In this tutorial, we talked about arrays, strings, and objects, along with the methods they offer. Hopefully you learned something new today.

In case you're interested in more great content like this, follow me on [LinkedIn](https://www.linkedin.com/in/houssein-badra-943879214) where I share a lot of great content.

