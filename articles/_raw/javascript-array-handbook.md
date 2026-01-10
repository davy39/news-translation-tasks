---
title: JavaScript Array Handbook – Learn How JS Array Methods Work With Examples and
  Cheat Sheet
subtitle: ''
author: Nathan Sebhastian
co_authors: []
series: null
date: '2023-08-31T14:22:03.000Z'
originalURL: https://freecodecamp.org/news/javascript-array-handbook
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/JavaScript-Array-for-Beginners-Cover.png
tags:
- name: arrays
  slug: arrays
- name: handbook
  slug: handbook
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'In programming, an array is a data structure that contains a collection
  of elements. Arrays are very useful because you can store, access, and manipulate
  multiple elements in a single array.

  In this handbook, you''ll learn how to work with arrays in J...'
---

In programming, an array is a data structure that contains a collection of elements. Arrays are very useful because you can store, access, and manipulate multiple elements in a single array.

In this handbook, you'll learn how to work with arrays in JavaScript. We'll cover the specific rules you need to follow when creating an array, as well as how to use array methods to manipulate and transform your array as desired.

## Table of Contents

1. [How Arrays Work in JavaScript](#heading-how-arrays-work-in-javascript)
2. [How to Create an Array in JavaScript](#heading-how-to-create-an-array-in-javascript)
3. [How to Access an Array's Elements](#heading-how-to-access-an-arrays-elements)
4. [The Array length Property](#heading-the-array-length-property)
5. [How to Add Elements to an Array](#heading-how-to-add-elements-to-an-array)
6. [How to Remove an Element from an Array](#heading-how-to-remove-an-element-from-an-array)
7. [How To Check If a Variable is an Array](#heading-how-to-check-if-a-variable-is-an-array)
8. [How to Iterate or Loop Over an Array](#heading-how-to-iterate-or-loop-over-an-array)
9. [How to Convert an Array into a String](#heading-how-to-convert-an-array-into-a-string)
10. [How to Compare Two Arrays](#heading-how-to-compare-two-arrays)
11. [How to Copy an Array](#heading-how-to-copy-an-array)
12. [How to Merge Two Arrays as One](#how-to-merge-two-arrays-as-one)
13. [How to Search an Array](#heading-how-to-search-an-array)
14. [How to Sort an Array](#heading-how-to-sort-an-array)
15. [How to Create Multi-dimensional Arrays](#heading-how-to-create-multi-dimensional-arrays)
16. [JavaScript Array Methods Cheat Sheet](#heading-javascript-array-methods-cheat-sheet)
17. [Wrapping Up](#heading-wrapping-up)

## How Arrays Work in JavaScript

In JavaScript, an array is implemented as an object that can have a group of items, elements, or values as an ordered collection. This means you can access an array's element using its position in the collection. You'll see why this is important in the next section.

An array can hold elements of different data types, and the size of the array is not fixed. This means that you can add as many elements to an array as you want.

## How to Create an Array in JavaScript

There are two ways you can create an array in JavaScript:

* Using the square brackets `[]`
* Using the `Array()` constructor

The square brackets `[]` is a literal notation used to create an array. The array elements are defined inside the brackets, with each element separated using a comma `,`.

The following example shows how to create an array named `myArray` that has three elements of different types: a Number, a String, and a Boolean.

```js
let myArray = [29, 'Nathan', true];

```

And here's how to create an array with 3 number elements:

```js
let myNumbers = [5, 10, 15];

```

You can specify as many elements as you want inside the square brackets.

Another way to create an array is to use the `Array()` constructor, which works like the square brackets:

```js
let myArray = Array(29, 'Nathan', true);

// or
let myNumbers = new Array(5, 10, 15);

```

Note that the constructor function can be called with or without the `new` operator. Both create an array object just fine.

In most code examples and codebases, you'll most likely see developers use the square brackets to create an array instead of using the constructor. This is because it's faster to type `[]` instead of `Array()`.

## How to Access an Array's Elements

As I've said before, an array is an ordered collection, so you can access an element from its position (also known as index number) in the array.

To access an array's element, you need to specify the array name followed by square brackets. Inside the square brackets, specify the index of the element you want to access.

For example, here's how you access the first element of `myArray`:

```js
let myArray = [29, 'Nathan', true];

console.log(myArray[0]); // 29
console.log(myArray[1]); // Nathan
console.log(myArray[2]); // true

```

The array index number starts from 0 and increases by 1 for each element added to the array.

If you try to access an index number that hasn't been assigned any value yet, JavaScript will return `undefined` as shown below:

```js
let myArray = [29, 'Nathan', true];

console.log(myArray[3]); // undefined
console.log(myArray[4]); // undefined
console.log(myArray[100]); // undefined

```

You can also replace an element on a certain index number with a new element by using the assignment `=` operator.

The following example shows how to replace the third element (boolean) with a string:

```js
let myArray = [29, 'Nathan', true];

// Replace the third element
myArray[2] = 'Sebhastian';

console.log(myArray); // [ 29, 'Nathan', 'Sebhastian' ]

```

In the example above, you can see that the `true` boolean value is replaced with the string 'Sebhastian'. Next, let's take a look at the `length` property.

## The Array `length` Property

The `length` property shows how many elements an array has. You can access this property using the dot `.` notation as shown below:

```js
let myArray = [29, 'Nathan', true];

console.log(myArray.length); // 3

let animals = ['Dog', 'Cat'];

console.log(animals.length); // 2

```

The `length` property is updated each time you add or remove elements from an array.

## How to Add Elements to an Array

To add one or more elements to an array, you can use the array `push()` and `unshift()` methods.

The `push()` method adds new elements to the end of the array, while the `unshift()` method inserts new elements at the start of the array:

```js
let animals = ['Dog', 'Cat'];

animals.push('Horse', 'Fish');

console.log(animals);
// [ 'Dog', 'Cat', 'Horse', 'Fish' ]

animals.unshift('Bird');

console.log(animals);
// [ 'Bird', 'Dog', 'Cat', 'Horse', 'Fish' ]

```

Here, notice that you can use a comma to separate the elements you want to add to the array.

Next, let's see how you can remove elements from an array.

## How to Remove an Element from an Array

To remove an element from an array, you can use the `shift()` and `pop()` methods, depending on the position of the element you want to remove.

Use the `shift()` method to remove the first element, and use `pop()` to remove the last element in the array:

```js
let animals = ['Dog', 'Cat', 'Horse', 'Fish'];

animals.shift();

console.log(animals);
// [ 'Cat', 'Horse', 'Fish' ]

animals.pop();

console.log(animals);
// [ 'Cat', 'Horse' ]

```

Both `shift()` and `pop()` can only remove one element at a time. If you want to remove an element in the middle of an array, you need to use the `splice()` method.

### How to Use `splice()` to Remove or Add Element(s)

The array `splice()` method is used to remove or add elements at specific positions. You use this method when `push`, `pop`, `shift`, and `unshift` can't get the job done.

To remove elements using the `splice()` method, you need to specify two arguments: the index number to start array manipulation, and the number of elements to delete.

For example, suppose you want to delete two elements at index 1 and 2 in the `animals` array. Here's how you do it:

```js
let animals = ['Dog', 'Cat', 'Horse', 'Fish'];

animals.splice(1, 2);

console.log(animals);
// [ 'Dog', 'Fish' ]

```

The `splice(1, 2)` means start array manipulation at index 1, then delete 2 elements from there.

To add elements using `splice()`, you need to specify the elements to add after the second argument.

For example, here I add a string value 'Bird' and 'Squid' at index 1:

```js
let animals = ['Dog', 'Cat'];

animals.splice(1, 0, 'Bird', 'Squid');

console.log(animals);
// [ 'Dog', 'Bird', 'Squid', 'Cat' ]

```

If you don't want to delete any elements, you can pass `0` as the second argument to the `splice()` method. You then specify the elements you want to add.

The `splice()` method can be confusing the first time you see it, but don't worry! You'll memorize how it works with more practice.

## How to Check if a Variable is an Array

To check if a variable is an array, you can use the `Array.isArray()` method which tests whether the argument given to the method is an array or not.

This method returns `true` when you pass an array to it, and `false` for anything else:

```js
let myArray = [1, 2, 3];
let notAnArray = 'Hello!';

console.log(Array.isArray(myArray)); // true
console.log(Array.isArray(notAnArray)); // false

```

Note that you need to specify the `Array` class when calling the `isArray()` method.

This is because `isArray()` is a static method, so you can only call it directly from the class that defines the method.

## How to Iterate or Loop Over an Array

There are 4 ways you can iterate over an array in JavaScript, depending on the method you use:

1. Using a `for` loop
2. Using a `while` loop
3. Using the `for...in` loop
4. Using the `for...of` loop
5. Using the `forEach()` method

Let's learn how to use these 4 methods with examples.

### 1. How to use a for loop

To iterate over an array using a `for` loop, you need to use the array `length` as the condition expression.

In the following example, a `for` loop will continue to run as long as the variable `i` is less than the array's length:

```js
let animals = ['dog', 'bird', 'cat', 'horse'];

for (let i = 0; i < animals.length; i++) {
  console.log(animals[i]);
}

```

You can manipulate the elements of the array inside the `for` loop's body.

### 2. How to use a while loop

Another way to iterate over an array is to use a `while` loop. You need to use a variable and the array's length to control when the iteration stops, like the `for` loop previously:

```js
let animals = ['dog', 'bird', 'cat', 'horse'];

let i = 0;

while (i < animals.length) {
  console.log(animals[i]);
  i++;
}

```

Inside the while loop, you need to increment the `i` variable by one to avoid an infinite loop.

### 3. How to use a for...in loop

The `for...in` loop is another syntax that you can use to iterate over an array. This loop returns the index position of the array, so you can use it like this:

```js
let animals = ['dog', 'bird', 'cat', 'horse'];

for (i in animals) {
  console.log(animals[i]);
}

```

The `for...in` loop is more concise when compared to a `for` or `while` loop, but it's better to use a `for...of` loop when iterating over an array.

### 4. How to use a for...of loop

The `for...of` loop can be used to iterate over an array. It returns the array's element in each iteration:

```js
let animals = ['dog', 'bird', 'cat', 'horse'];

for (element of animals) {
  console.log(element);
}

```

While the `for...in` loop returns the index position, the `for...of` loop returns the element directly.

### 5. How to use the `forEach()` method

The JavaScript array object itself has a method called `forEach()` that you can use to iterate over an array from position 0 to the last position.

The method accepts a callback function that gets executed in each iteration. For each iteration, the method also passes the array's element and index position. Here's an example of using the method:

```js
let animals = ['dog', 'bird', 'cat', 'horse'];

animals.forEach(function (element, index) {
  console.log(`${index}: ${element}`);
});

```

The output will be:

```txt
0: dog
1: bird
2: cat
3: horse

```

And that's how you iterate over an array using the `forEach()` method. You can use any method you like best.

## How to Convert an Array into a String

To convert an array into a string, you can use the `toString()` or `join()` method.

The `toString()` method converts a given array into a string, with the elements separated by a comma:

```js
const animals = ['cat', 'bird', 'fish'];

console.log(animals.toString()); // "cat,bird,fish"

```

The `join()` method also converts an array into a string, but you can pass a specific string separator as its argument.

The following example shows how to use a slash `/` and an empty string as the string separator:

```js
const animals = ['cat', 'bird', 'fish'];

console.log(animals.join()); // "cat,bird,fish"

console.log(animals.join('/')); // "cat/bird/fish"

console.log(animals.join('')); // "catbirdfish"

```

Behind the scenes, the `toString()` method actually calls the `join()` method to create the string.

## How to Compare Two Arrays

JavaScript arrays are treated as objects. So when you compare two arrays, the comparison will look to the reference — that is, the address to the memory location that stores that array — instead of the actual values.

The comparison of two arrays will return `false` even when they contain the same elements:

```js
let arrayOne = [7, 8, 9];
let arrayTwo = [7, 8, 9];

console.log(arrayOne === arrayTwo); // false

```

This is because `arrayOne` and `arrayTwo` are different objects stored in different memory locations.

The only way an array comparison would return `true` is when both variables refer to the same array object. In the example below, the `arrayTwo` variable is a reference to `arrayOne`:

```js
let arrayOne = [7, 8, 9];
let arrayTwo = arrayOne;

console.log(arrayOne === arrayTwo); // true

```

But this won't work when you need to compare two arrays from different references. One way to compare arrays is by converting the array to a JSON object.

### Compare arrays by converting them to JSON object

Before comparing two different arrays, you need to convert them into JSON objects by calling the `JSON.stringify()` method.

You can then compare the two serialized strings as follows:

```js
let arrayOne = [7, 8, 9];
let arrayTwo = [7, 8, 9];

console.log(JSON.stringify(arrayOne) === JSON.stringify(arrayTwo)); // true

```

But this solution compares the arrays indirectly, and having the same values in different orders will return `false` instead of `true`.

To compare the elements of two arrays programmatically, you need to use another solution.

### How to compare arrays with the `every()` method

Another way you can compare two arrays is by using the combination of the `length` property and the `every()` method.

First, you compare the length of the arrays so the comparison doesn't return `true` when the second array contains more elements than the first array.

After that, you test if the element on the first array is equal to the element on the second array, at the same index position. Use the `&&` operator to join the comparison as shown below:

```js
let arrayOne = [7, 8, 9];
let arrayTwo = [7, 8, 9];

let result =
  arrayOne.length === arrayTwo.length &&
  arrayOne.every(function (element, index) {
    // compare if the element matches in the same index
    return element === arrayTwo[index];
  });

console.log(result); // true

```

This way, you compare if the element at a specific index is really equal or not.

Still, this solution requires both arrays to have equal elements at a certain index in order to return `true`.

If you don't care about the order and only want both arrays to have the same elements, you need to use the `includes()` method instead of the equality `===` operator.

### How to compare arrays with the `includes()` method

In order to compare array elements that are out of order, you can use the combination of the `every()` and `includes()` methods.

The `includes()` method tests whether an array has a specific element you specified as its argument:

```js
let arrayOne = [7, 8, 9];
let arrayTwo = [9, 7, 8];

let result =
  arrayOne.length === arrayTwo.length &&
  arrayOne.every(function (element) {
    return arrayTwo.includes(element);
  });

console.log(result); // true

```

Another alternative to the `includes()` method is to use the `indexOf()` method, which returns the index of the specified element.

When the element isn't found, the `indexOf()` method returns `-1`. This means you need to make `every()` return `true` when `indexOf(element) !== -1` as shown below:

```js
let arrayOne = [7, 8, 9];
let arrayTwo = [9, 7, 8];

let result =
  arrayOne.length === arrayTwo.length &&
  arrayOne.every(function (element) {
    return arrayTwo.indexOf(element) !== -1;
  });

console.log(result); // true

```

As you can see, comparing arrays is not straightforward. You need to use the methods provided by the array object creatively.

But don't worry! Most of the time you don't need to compare array objects when developing a web application. Next, let's learn how you can copy an array.

## How to Copy an Array

One way to copy an array is to use the `slice()` method, which is provided exactly for copying an array.

You only need to call the method and assign the returned array to a new variable like this:

```js
let arrayOne = [7, 8, 9];
let arrayTwo = arrayOne.slice();

console.log(arrayOne); // [ 7, 8, 9 ]
console.log(arrayTwo); // [ 7, 8, 9 ]

```

But keep in mind that the `slice()` method returns a shallow copy, which means that the values of the copy are references to the original array.

A shallow copy won't cause a problem when your array contains primitive values like strings, numbers, or booleans. But it might become an issue when you copy an array of objects. 

To show you what I mean, see the example below:

```js
let arrayOne = [{ name: 'Jack', age: 25 }];
let arrayTwo = arrayOne.slice();

console.log(arrayOne); // [ { name: 'Jack', age: 25 } ]
console.log(arrayTwo); // [ { name: 'Jack', age: 25 } ]

arrayTwo[0].name = 'Nathan';

console.log(arrayOne); // [ { name: 'Nathan', age: 25 } ]
console.log(arrayTwo); // [ { name: 'Nathan', age: 25 } ]

```

Do you notice what's wrong? The code above modifies only the `name` property of `arrayTwo`, but it changes both arrays!

This is because `arrayTwo` is a shallow copy of `arrayOne`. To prevent this behavior, you need to perform a deep copy so that `arrayTwo` values are disconnected from the original array.

### How to create a deep copy of an array

To create a deep copy of an array, you need to copy the array by using the `JSON.parse()` and `JSON.stringify()` methods instead of using the `slice()` method.

The `JSON.stringify()` transforms the array into a JSON string, and `JSON.parse()` converts that string back into an array.

Because the copy is created from a JSON string, there's no connection to the original array anymore:

```js
let arrayOne = [{ name: 'Jack', age: 25 }];
let arrayTwo = JSON.parse(JSON.stringify(arrayOne));

console.log(arrayOne); // [ { name: 'Jack', age: 25 } ]
console.log(arrayTwo); // [ { name: 'Jack', age: 25 } ]

arrayTwo[0].name = 'Nathan';

console.log(arrayOne); // [ { name: 'Jack', age: 25 } ]
console.log(arrayTwo); // [ { name: 'Nathan', age: 25 } ]

```

Here, you can see that changing the property of `arrayTwo` doesn't change the same property in `arrayOne`. Nice work!

## How to Merge Two Arrays into One

JavaScript provides the `concat()` method that you can use to merge two or more arrays into one. The following example shows how to merge the `cats` and `birds` arrays as one array named `animals`:

```js
let cats = ['tiger', 'cat'];
let birds = ['owl', 'eagle'];

let animals = cats.concat(birds);

console.log(animals); // [ 'tiger', 'cat', 'owl', 'eagle' ]
console.log(cats); // [ 'tiger', 'cat' ]
console.log(birds); // [ 'owl', 'eagle' ]

```

At first glance, the syntax of the `concat()` method seems to merge the `birds` array into the `cats` array. But as you can see from the console logs, the `cats` array is actually unchanged.

To make the code more intuitive, you can call the `concat()` method from an empty array instead of from the `cats` array:

```js
let cats = ['tiger', 'cat'];
let birds = ['owl', 'eagle'];

let animals = [].concat(cats, birds);

```

Although this syntax is more intuitive, you will most likely encounter the `cats.concat(birds)` syntax in many JavaScript source code. Which syntax to use? That's for you and your team to decide.

The `concat()` method allows you to merge as many arrays as you need. The following example merges three arrays as one:

```js
let cats = ['tiger', 'cat'];
let birds = ['owl', 'eagle'];
let dogs = ['wolf', 'dog'];

let animals = [].concat(cats, birds, dogs);
console.log(animals); // [ 'tiger', 'cat', 'owl', 'eagle', 'wolf', 'dog' ]

```

You've now learned how to merge arrays using the `concat()` method. Let's look at how you can merge arrays with the spread operator next.

### How to merge arrays with the spread operator

The spread operator `...` can be used to expand elements of the arrays you want to merge. You need to put the expanded elements in one new array as follows:

```js
let cats = ['tiger', 'cat'];
let birds = ['owl', 'eagle'];

let animals = [...cats, ...birds];
console.log(animals); // [ 'tiger', 'cat', 'owl', 'eagle' ]

```

Here, you can see that the elements from `cats` and `birds` arrays are expanded into another array, and that array is assigned as the value of the `animals` variable.

Both the `concat()` method and the spread operator can be used to merge multiple arrays just fine.

## How to Search an Array

There are three ways you can search an array, depending on the result you want to achieve:

1. Find whether an element exists in an array
2. Find the index position of an element in an array
3. Find the value that meets certain criteria in an array

Let's learn all three ways to search an array together. Don't worry, they are simple.

### 1. How to find whether an element exists in an array

If you only want to know if a certain element exists in an array, you can use the `includes()` method. The following example searches for the string value 'e' in an array of strings:

```js
let letters = ['a', 'b', 'c', 'd'];

console.log(letters.include('e')); // false

```

The `includes()` method returns `true` when the element is found, or `false` when it isn't.

### 2. How to find the index position of an element in an array

Other times, you might want to get the index position of the element. You need to use the `indexOf()` method in that case:

```js
let letters = ['a', 'b', 'c', 'd'];

console.log(letters.indexOf('c')); // 2

```

Here, the `indexOf()` method is called on the `letters` array to search for the index of the value 'c'. The method returns `-1` when the element isn't found, but in this case it returns `2` as the letter c is at the 2nd index (remember, JS uses zero-based indexing, meaning the count starts from 0, not 1).

### 3. How to find elements that meet certain criteria in an array

To find elements that meet certain criteria, you need to use the `filter()` method.

The `filter()` method is a built-in method available for JavaScript array objects that can help you in filtering an array. The syntax of the method is as follows:

```js
arrayObject.filter(callback, thisContext);

```

The method has two parameters:

* `callback` (**Required**) – The filtering function that will be executed for each array value
* `thisContext` (**Optional**) – The value of `this` keyword inside the `callback`

The `thisContext` parameter is optional and usually not needed. You only need to define the `callback` function, which will accept three arguments:

* The `currentElement` being processed into the method
* The `index` of the element that starts from `0`
* and the `array` object where you call `filter()`

```js
filterCallback(currentElement, index, array){
  // ...
}

```

The callback function must include a validation pattern that returns either `true` or `false`.

#### Filter method examples

Let's see an example of `filter()` in action. Let's say you have an array called `stockPrices` as follows:

```js
let stockPrices = [3, 7, 2, 15, 4, 9, 21, 14];

```

You want to filter the prices to include only those greater than 5.

Here's how you do it with the `filter()` method:

```js
let stockPrices = [3, 7, 2, 15, 4, 9, 21, 14];

let filteredPrices = stockPrices.filter(function (currentElement) {
  return currentElement > 5;
});

console.log(filteredPrices); // [7, 15, 9, 21, 14]

```

The `filter()` method evaluates the `currentElement` and returns either `true` or `false`.

If your callback function returns `true`, the `currentElement` will be added to the result array:

* During the first iteration, the `currentElement` is `3` so the callback returns `false`
* During the second iteration, the `currentElement` is `7` so the callback returns `true` and the value is pushed into the result array
* The iteration will continue to the last element
* The resulting array is assigned to the `filteredPrices` variable

And that's how the method works. Next, let's see how to use the `filter()` method to filter an array of objects.

#### How to filter an array of objects

The `filter()` method can also be used on an array of objects.

Suppose you have an array of objects containing imaginary stock prices and their symbols as shown below:

```js
let stocks = [
  {
    code: 'GOOGL',
    price: 1700,
  },
  {
    code: 'AAPL',
    price: 130,
  },
  {
    code: 'MSFT',
    price: 219,
  },
  {
    code: 'TSLA',
    price: 880,
  },
  {
    code: 'FB',
    price: 267,
  },
  {
    code: 'AMZN',
    price: 3182,
  },
];

```

Now you need to filter the array to contain only stocks with `price` value less than 1000. Here's how you do it:

```js
let filteredStocks = stocks.filter(function (currentElement) {
  return currentElement.price < 1000;
});

```

The value of `filteredStocks` will be as follows:

```txt
0: {code: "AAPL", price: 130}
1: {code: "MSFT", price: 219}
2: {code: "TSLA", price: 880}
3: {code: "FB", price: 267}

```

Finally, you can also write the callback function using the arrow function syntax like this:

```js
let filteredStocks = stocks.filter(
  currentElement => currentElement.price < 1000
);

```

When you have simple filter criteria, using the arrow function syntax can help you write cleaner code.

## How to Sort an Array

To sort an array, you can use the provided `sort()` method, which sorts an array in ascending order by default:

```js
let numbers = [5, 2, 4, 1];

numbers.sort();

console.log(numbers); // [ 1, 2, 4, 5 ]

```

If you want to sort an array in descending order, you can call the `reverse()` method after the `sort()` method as shown below:

```js
let numbers = [5, 2, 4, 1];

numbers.sort().reverse();

console.log(numbers); // [ 5, 4, 2, 1 ]

```

The `reverse()` method will reverse the array, so the first array element becomes the last, the last becomes the first, and so on.

## How to Create Multi-dimensional Arrays

A multi-dimensional array is an array that contains another array. To create one, you need to write an array inside an array literal (the square bracket)

The following example shows how you can create a two-dimensional array:

```js
let numbers = [[5, 6, 7]];

```

To access the array, you just need to call the variable with two array indices. The first index is for the outer array, and the second index is for the inner array:

```js
let numbers = [[5, 6, 7]];
console.log(numbers[0][0]); // 5
console.log(numbers[0][1]); // 6
console.log(numbers[0][2]); // 7

```

As you can see from the example above, the array `[5, 6, 7]` is stored inside index `0` of the outer `[]` array. You can add more elements inside the array as follows:

```js
let numbers = [[5, 6, 7], [10], [20]];
console.log(numbers[1][0]); // 10
console.log(numbers[2][0]); // 20

```

A multi-dimensional array is not required to have the same array length, as can be seen above. Although you can create even a three or four-dimensional array, it's not recommended to create more than a two-dimensional array because it will be confusing.

Notice how difficult it is to read and access the value `[23]` inside the three-dimensional array below:

```js
let numbers = [[5, 6, 7, [23]]];
console.log(numbers[0][3][0]); // 23

```

Finally, you can still use JavaScript `Array` object methods like `push()`, `shift()`, and `unshift()` to manipulate the multi-dimensional array:

```js
let numbers = [[5, 6, 7, [23]]];
numbers.push([50]);
console.log(numbers); // [[5, 6, 7, [23]], [50]]

numbers.shift();
console.log(numbers); // [[50]]

numbers.unshift('13');
console.log(numbers); // ["13", [50]]

```

A multi-dimensional array has no unique methods compared to a one-dimensional array. Often, it's used to store a group of related data as one array.

The following example shows how to group `name` and `age` values under a multi-dimensional array:

```js
let users = [
  ['Nathan', 28],
  ['Jack', 23],
  ['Alex', 30],
];

```

Unless you have to use an array, it's better to use an array of objects to store a group of related data:

```js
let users = [
  { name: 'Nathan', age: 28 },
  { name: 'Jack', age: 23 },
  { name: 'Alex', age: 30 },
];

```

Ideally, you should use only one-dimensional arrays in your project. Use two-dimensional structure if you really need to, but never go beyond that or you'll have a hard time manipulating the array later.

## JavaScript Array Methods Cheat Sheet

Beginners are usually overwhelmed by the number of methods an array has, so I've prepared a cheat sheet that can help you get a quick lookup at what a method does.

The cheat sheet contains a short description and a quick example of what a method does. You can download it here:

%[https://twitter.com/nsebhastian/status/1696034185398645024]

## Wrapping Up

Congratulations on finishing this JavaScript Array Guide. I hope this tutorial has helped you understand how to create, copy, and manipulate an array in JavaScript.

If you enjoyed this article and want to take your JavaScript skills to the next level, I recommend you check out my new book _Beginning Modern JavaScript_ [here](https://www.amazon.com/dp/B0CQXHMF8G).

[![beginning-js-cover](https://www.freecodecamp.org/news/content/images/2024/01/beginning-js-cover.png)](https://www.amazon.com/dp/B0CQXHMF8G)

The book is designed to be easy to understand and accessible to anyone looking to learn JavaScript. It provides a step-by-step gentle guide that will help you understand how to use JavaScript to create a dynamic application.

Here's my promise: _You will actually feel like you understand what you're doing with JavaScript._

Until next time!

