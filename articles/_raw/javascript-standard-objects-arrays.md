---
title: 'JavaScript Standard Objects: Arrays'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-26T17:41:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-standard-objects-arrays
coverImage: https://www.freecodecamp.org/news/content/images/2020/02/very-large-array.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'Surely you''ve heard that, in JavaScript, everything is an object. Strings,
  numbers, functions, arrays, and, well, objects are considered objects.

  In this tutorial we''ll take a deep dive into the Array "global" or "standard built-in"
  object, along wit...'
---

Surely you've heard that, in JavaScript, everything is an object. Strings, numbers, functions, arrays, and, well, objects are considered objects.

In this tutorial we'll take a deep dive into the **Array** "global" or "standard built-in" object, along with the methods associated with it.

## What's an array?

In JavaScript, an array is a list-like object that stores comma separated values. These values can be anything – strings, numbers, objects, or even functions.

Arrays start with an opening bracket (`[`) and end with a closing bracket (`]`), use numbers as element indexes.

### How to create an array:

```js
const shoppingList = ['Bread', 'Cheese', 'Apples'];
```

### Access a value in an array with bracket notation

```js
const shoppingList = ['Bread', 'Cheese', 'Apples'];

console.log(shoppingList[1])
// Cheese
```

The array standard object has a number of useful methods, some of which are listed below.

## Array.prototype.isArray()

The `Array.isArray()` method returns `true` if an object is an array, `false` if it is not.

### Syntax

```text
Array.isArray(obj)
```

### **Parameters**

**obj** The object to be checked.

### Examples of .isArray()

```text
// all following calls return true
Array.isArray([]);
Array.isArray([1]);
Array.isArray(new Array());
// Little known fact: Array.prototype itself is an array:
Array.isArray(Array.prototype); 

// all following calls return false
Array.isArray();
Array.isArray({});
Array.isArray(null);
Array.isArray(undefined);
Array.isArray(17);
Array.isArray('Array');
Array.isArray(true);
Array.isArray(false);
Array.isArray({ __proto__: Array.prototype });
```

## **Array.prototype.length**

`length` is a property of arrays in JavaScript that returns or sets the number of elements in a given array.

The `length` property of an array can be returned like so.

```js
let desserts = ["Cake", "Pie", "Brownies"];
console.log(desserts.length); // 3
```

The assignment operator, in conjunction with the `length` property, can be used to set then number of elements in an array like so.

```js
let cars = ["Saab", "BMW", "Volvo"];
cars.length = 2;
console.log(cars.length); // 2
```

## Array.prototype.push

The `push()` method is used to add one or more new elements to the end of an array. It also returns the new length of the array. If no arguments are provided, it will simply return the current length of the array. 

### **Syntax**

```javascript
arr.push([element1[, ...[, elementN]]])
```

### **Parameters**

* **elementN** The elements to add to the end of the array.

### **Return value**

The new length of the array on which the method was called.

## **Example:**

```javascript
let myStarkFamily = ['John', 'Robb', 'Sansa', 'Bran'];
```

Suppose you have an array of the children of House Stark from Game of Thrones. However, one of the members, **Arya**, is missing. Knowing the code above, you could add her by assigning `'Arya'` to the array at the index after the last index like so:

```javascript
myStarkFamily[4] = 'Arya';
```

The problem with this solution is that it can’t handle general cases. If you didn’t know beforehand what the length of the array is, you can’t add new elements this way. This is what `push()` is for. We don’t need to know how long the array is. We just add our element to the end of the array.

```javascript
myStarkFamily.push('Arya');
console.log(myStarkFamily);  // ['John', 'Robb', 'Sansa', 'Bran', 'Arya']

let newLength = myStarkFamily.push('Rickon');  // oops! forgot Rickon
console.log(newLength);  // 6
console.log(myStarkFamily);  // ['John', 'Robb', 'Sansa', 'Bran', 'Arya', 'Rickon']
```

## Array.prototype.reverse

The JavaScript array method `.reverse()` will reverse the order of the elements within the array.

**Syntax**

```javascript
  let array = [1, 2, 3, 4, 5];
  array.reverse();
```

## **Description**

`.reverse()` reverses the index of the elements of an array.

## **Examples**

**Use `.reverse()` to reverse the elements of an array**

```javascript
  let array = [1, 2, 3, 4, 5];
  console.log(array);
  // Console will output 1, 2, 3, 4, 5

  array.reverse();

  console.log(array);
  /* Console will output 5, 4, 3, 2, 1 and
  the variable array now contains the set [5, 4, 3, 2, 1] */
```

## Array.prototype.indexOf

The `indexOf()` method returns the first index at which a given element can be found in the array. If the element is not present, it returns -1.

The `indexOf()` takes an element you want to search for as a parameter, iterates through the elements in an array, and returns the first index where the element can be found. If the element is not in the array, `indexOf` returns -1.

**Syntax**

```javascript
  arr.indexOf(searchElement[, fromIndex])
```

**Parameters**

* **searchElement**: The element you're searching for.
* **fromIndex** (Optional): The index at which you want to start the search at. If the `fromIndex` is greater than or equal to the array’s length, the array is not searched and the method returns -1. If the fromIndex is a negative number, it considered an offset from the end of the array (the array is still searched forwards from there). The default value is 0, which means the entire array is searched.
* The array index you want to start searching form. The default value is 0, meaning the search starts from the first index of the array. If `fromIndex` is greater than or equal to the array's length, then the method doesn't search the array and returns -1.

### Examples

```javascript
var array = [1, 2, 4, 1, 7]

array.indexOf(1); // 0
array.indexOf(7); // 4
array.indexOf(6); // -1
array.indexOf('1'); // -1
array.indexOf('hello'); // -1
array.indexOf(1, 2); // 3
array.indexOf(1, -3); // 3
```

## Array.prototype.findIndex

The `findIndex()` method goes through an array and tests every element against the testing function that's passed as a parameter. It returns the index of the first element of the array that returns true against the testing functions. If no elements return true, `findIndex()` returns -1.

Note that `findIndex()` does not mutate the array it's called on.

**Syntax**

```text
arr.findIndex(callback(element, index, array), [thisArg])
```

##### **Parameters**

`callback`: Function to execute on each value in the array, which takes three arguments: 

* `element`: The current element being processed in the array.
* `index`: The index of the current element being processed in the array.
* `array`: The array findIndex() was called upon.

`thisArg` (Optional): An object to use as `this` when executing the callback function.

### Examples

This example will find the corresponding item in the array and return the index from it.

```javascript
let items = [
    {name: 'books', quantity: 2},
    {name: 'movies', quantity: 1},
    {name: 'games', quantity: 5}
];

function findMovies(item) { 
    return item.name === 'movies';
}

console.log(items.findIndex(findMovies));

// Index of 2nd element in the Array is returned,
// so this will result in '1'
```

The following example shows the output of each optional parameter to the callback function. This will return `-1` because none of the items will return true from the callback function.

```javascript
function showInfo(element, index, array) {
  console.log('element = ' + element + ', index = ' + index + ', array = ' + array);
  return false;
}

console.log('return = ' + [4, 6, 8, 12].findIndex(showInfo));

// Output
//  element = 4, index = 0, array = 4,6,8,12
//  element = 6, index = 1, array = 4,6,8,12
//  element = 8, index = 2, array = 4,6,8,12
//  element = 12, index = 3, array = 4,6,8,12
//  return = -1
```

## Array.prototype.find

The `find()` method goes through an array and tests every element against the testing function that's passed as a parameter. It returns the value of the first element of the array that returns true against the testing functions. If no elements return true, `find()` returns `undefined`.

Note that `find()` does not mutate the array it's called on.

### Syntax

```text
arr.find(callback(element, index, array), [thisArg])
```

##### **Parameters**

`callback`: Function to execute on each value in the array. It takes three arguments:

* `element`: The current element being processed in the array.
* `index`: The index of the current element being processed in the array.
* `array`: The array find was called upon.

`thisArg` (Optional): An object to use as `this` when executing the callback function.

### Examples

This example will find the corresponding item in the array and return the object from it.

```javascript
let items = [
    {name: 'books', quantity: 2},
    {name: 'movies', quantity: 1},
    {name: 'games', quantity: 5}
];

function findMovies(item) { 
    return item.name === 'movies';
}

console.log(items.find(findMovies));

// Output
//  { name: 'movies', quantity: 1 }
```

The following example shows the output of each optional parameter to the callback function. This will return `undefined` because none of the items will return true from the callback function.

```javascript
function showInfo(element, index, array) {
  console.log('element = ' + element + ', index = ' + index + ', array = ' + array);
  return false;
}

console.log('return = ' + [4, 6, 8, 12].find(showInfo));

// Output
//  element = 4, index = 0, array = 4,6,8,12
//  element = 6, index = 1, array = 4,6,8,12
//  element = 8, index = 2, array = 4,6,8,12
//  element = 12, index = 3, array = 4,6,8,12
//  return = undefined
```

## Array.prototype.join

The JavaScript array method `.join()` will combine all elements of an array into a single string.

**Syntax**

```javascript
  const array = ["Lorem", "Ipsum", "Dolor", "Sit"];
  const str = array.join([separator]);
```

### Parameters

**separator** Optional. Specifies the string to use to separate each element of the original array. If the separator is not a string, it will be converted to a string. If separator parameter is not provided, array elements are separated with a comma by default. If separator is an empty string `""`, all array elements are joined without a separator character between them.

### Description

`.join()` joins all elements of an array into a single string. If any of the array elements are `undefined` or `null`, that element is converted to the empty string `""`.

### Examples

**Using `.join()` four different ways**

```javascript
const array = ["Lorem", "Ipsum", "Dolor" ,"Sit"];

const join1 = array.join();           /* assigns "Lorem,Ipsum,Dolor,Sit" to join1 variable
                                     (because no separator was provided .join()
                                     defaulted to using a comma) */
const join2 = array.join(", ");       // assigns "Lorem, Ipsum, Dolor, Sit" to join2 variable
const join3 = array.join(" + ");      // assigns "Lorem + Ipsum + Dolor + Sit" to join3 variable
const join4 = array.join("");         // assigns "LoremIpsumDolorSit" to join4 variable
```

## **Array.prototype.concat**

The `.concat()` method returns a new array consisting of the elements of the array on which you call it, followed by the elements of the arguments in the order they are passed.

You can pass multiple arguments to the `.concat()` method. The arguments can be arrays, or data types like booleans, strings, and numbers.

### **Syntax**

```javascript
const newArray = array.concat(value1, value2, value3...);
```

### **Examples**

#### **Concatenating two arrays**

```javascript
const cold = ['Blue', 'Green', 'Purple'];
const warm = ['Red', 'Orange', 'Yellow'];

const result = cold.concat(warm);

console.log(result);
// results in ['Blue', 'Green', 'Purple', 'Red', 'Orange', 'Yellow'];
```

#### **Concatenating value to an array**

```javascript
const odd = [1, 3, 5, 7, 9];
const even = [0, 2, 4, 6, 8];

const oddAndEvenAndTen = odd.concat(even, 10);

console.log(oddAndEvenAndTen);
// results in [1, 3, 5, 7, 9, 0, 2, 4, 6, 8, 10];
```

## Array.prototype.slice

The JavaScript array method `.slice()` will return a new array object which will be a segment (a slice) of the original array. The original array is not modified.

**Syntax**

```javascript
  array.slice()
  arr.slice(startIndex)
  arr.slice(startIndex, endIndex) 
```

### Parameters

* **startIndex** The zero-based index where the slice should begin. If the value is omitted, it will start at 0.
* **endIndex** The slice will end **before** this zero-based index. A negative index is used to offset from the end of the array. If the value is omitted, the segment will slice to the end of the array.

### Examples

```javascript
  const array = ['books', 'games', 'cup', 'sandwich', 'bag', 'phone', 'cactus']
  
  const everything = array.slice()
  // everything = ['books', 'games', 'cup', 'sandwich', 'bag', 'phone', 'cactus']
  
  const kitchen = array.slice(2, 4)
  // kitchen = ['cup', 'sandwich']
  
  const random = array.slice(4)
  // random = ['bag', 'phone', 'cactus']
  
  const noPlants = array.slice(0, -1)
  // noPlats = ['books', 'games', 'cup', 'sandwich', 'bag', 'phone']
  
  // array will still equal ['books', 'games', 'cup', 'sandwich', 'bag', 'phone', 'cactus']
```

#### 

## **Array.prototype.splice**

The splice method is similar to [Array.prototype.slice](https://guide.freecodecamp.org/javascript/standard-objects/array/array-prototype-slice), but unlike `slice()` it mutates the array it is called on. It also differs in that it can be used to add values to an array as well as remove them.

### **Parameters**

`splice()` can take one or more parameters detailed below.

#### **splice(start)**

If only one parameter is included, then `splice(start)` will remove all array elements from `start` to the end of the array.

```js
let exampleArray = ['first', 'second', 'third', 'fourth'];
exampleArray.splice(2);
// exampleArray is now ['first', 'second'];
```

If `start` is negative, it will count backwards from the end of the array.

```js
let exampleArray = ['first', 'second', 'third', 'fourth'];
exampleArray.splice(-1);
// exampleArray is now ['first', 'second', 'third'];
```

#### **splice(start, deleteCount)**

If a second parameter is included, then `splice(start, deleteCount)` will remove `deleteCount` elements from the array, beginning with `start`.

```js
let exampleArray = ['first', 'second', 'third', 'fourth'];
exampleArray.splice(1, 2);
// exampleArray is now ['first', 'fourth'];
```

#### **splice(start, deleteCount, newElement1, newElement2, …)**

If more than two parameters are included, the additional parameters will be new elements that are added to the array. The location of these added elements will be begin at `start`.

Elements can be added without removing any elements by passing `0` as the second parameter.

```js
let exampleArray = ['first', 'second', 'third', 'fourth'];
exampleArray.splice(1, 0, 'new 1', 'new 2');
// exampleArray is now ['first', 'new 1', 'new 2', 'second', 'third', 'fourth']
```

Elements can also be replaced.

```js
let exampleArray = ['first', 'second', 'third', 'fourth'];
exampleArray.splice(1, 2, 'new second', 'new third');
// exampleArray is now ['first', 'new second', 'new third', 'fourth']
```

### **Return value**

In addition to changing the array that it is called on, `splice()` also returns an array containing the removed values. This is a way of cutting an array into two different arrays.

```js
let exampleArray = ['first', 'second', 'third', 'fourth'];
let newArray = exampleArray.splice(1, 2);
// exampleArray is now ['first', 'fourth']
// newArray is ['second', 'third']
```

## **Array.prototype.filter**

The filter method takes an array as an input. It takes each element in the array and it applies a conditional statement against it. If this conditional returns true, the element gets “pushed” to the output array.

Once each element in the input array is “filtered” as such, it outputs a new array containing each element that returned true.

In this example below, there is an array that has multiple objects within it. Normally, to iterate through this array, you might use a for loop.

In this case, we want to get all the students whose grades are greater than or equal to 90.

```javascript
const students = [
  { name: 'Quincy', grade: 96 },
  { name: 'Jason', grade: 84 },
  { name: 'Alexis', grade: 100 },
  { name: 'Sam', grade: 65 },
  { name: 'Katie', grade: 90 }
];
//Define an array to push student objects to.
let studentsGrades = []
for (var i = 0; i < students.length; i++) {
  //Check if grade is greater than 90
  if (students[i].grade >= 90) {
    //Add a student to the studentsGrades array.
    studentsGrades.push(students[i])
  }
}

console.log(studentsGrades); // [ { name: 'Quincy', grade: 96 }, { name: 'Alexis', grade: 100 }, { name: 'Katie', grade: 90 } ]
```

This for loop works, but it is pretty lengthy. It can also become tedious to write for loops over and over again for many arrays that you need to iterate through.

This is a great use case for filter!

Here is the same example using filter:

```javascript
const students = [
  { name: 'Quincy', grade: 96 },
  { name: 'Jason', grade: 84 },
  { name: 'Alexis', grade: 100 },
  { name: 'Sam', grade: 65 },
  { name: 'Katie', grade: 90 }
];

const studentGrades = students.filter(function (student) {
  //This tests if student.grade is greater than or equal to 90. It returns the "student" object if this conditional is met.
  return student.grade >= 90;
});

console.log(studentGrades); // [ { name: 'Quincy', grade: 96 }, { name: 'Alexis', grade: 100 }, { name: 'Katie', grade: 90 } ]
```

The filter method is much faster to write and cleaner to read while still accomplishing the same thing. Using ES6 syntax we can even replicate the 6-line for-loop with filter:

```javascript
const students = [
  { name: 'Quincy', grade: 96 },
  { name: 'Jason', grade: 84 },
  { name: 'Alexis', grade: 100 },
  { name: 'Sam', grade: 65 },
  { name: 'Katie', grade: 90 }
];

const studentGrades = students.filter(student => student.grade >= 90);
console.log(studentGrades); // [ { name: 'Quincy', grade: 96 }, { name: 'Alexis', grade: 100 }, { name: 'Katie', grade: 90 } ]
```

Filter is very useful and a great choice over for loops to filter arrays against conditional statements.

## **Array.prototype.forEach**

The `.forEach()` array method is used to iterate through each item in an array. The method is called on the array object and is passed a function that is called on each item in the array.

```javascript
let arr = [1, 2, 3, 4, 5];

arr.forEach(number => console.log(number * 2));

// 2
// 4
// 6
// 8
// 10
```

The callback function can also take a second parameter of an index in case you need to reference the index of the current item in the array.

```javascript
let arr = [1, 2, 3, 4, 5];

arr.forEach((number, i) => console.log(`${number} is at index ${i}`));

// '1 is at index 0'
// '2 is at index 1'
// '3 is at index 2'
// '4 is at index 3'
// '5 is at index 4'
```

## **Array.prototype.reduce**

The `reduce()` method reduces an array of values down to just one value. It's been called the Swiss Army knife, or multi-tool, of array transformation methods. Others, such as `map()` and `filter()`, provide more specific transformations, whereas `reduce()` can be used to transform arrays into any output you desire.

### **Syntax**

```js
arr.reduce(callback[, initialValue])
```

The `callback` argument is a function that will be called once for every item in the array. This function takes four arguments, but often only the first two are used.

* _accumulator_ - the returned value of the previous iteration
* _currentValue_ - the current item in the array
* _index_ - the index of the current item
* _array_ - the original array on which reduce was called
* The `initialValue` argument is optional. If provided, it will be used as the initial accumulator value in the first call to the callback function (see Example 2 below).

### **Example 1**

Transform an array of integers into the sum of all integers in the array.

```js
const numbers = [1,2,3]; 
const sum = numbers.reduce(function(total, current){
    return total + current;
});
console.log(sum); 
```

This will output `6` to the console.

### **Example 2**

Transform an array of strings into a single object that shows how many times each string appears in the array. Notice this call to reduce passes an empty object `{}` as the `initialValue` parameter. This will be used as the initial value of the accumulator (the first argument) passed to the callback function.

```js
const pets = ['dog', 'chicken', 'cat', 'dog', 'chicken', 'chicken', 'rabbit'];

const petCounts = pets.reduce(function(obj, pet){
    if (!obj[pet]) {
        obj[pet] = 1;
    } else {
        obj[pet]++;
    }
    return obj;
}, {});

console.log(petCounts); 
```

Output:

```js
 { 
    dog: 2, 
    chicken: 3, 
    cat: 1, 
    rabbit: 1 
 }
```

## **Array.prototype.sort**

This method sorts the elements of an array in place and returns the array.

The `sort()` method follows the **ASCII order**!

```js
let myArray = ['#', '!'];
let sortedArray = myArray.sort();   // ['!', '#'] because in the ASCII table "!" is before "#"

myArray = ['a', 'c', 'b'];
console.log(myArray.sort()); // ['a', 'b', 'c']
console.log(myArray) // ['a', 'b', 'c']

myArray = ['b', 'a', 'aa'];
console.log(myArray.sort());   // ['a', 'aa', 'b']

myArray = [1, 2, 13, 23];
console.log(myArray.sort());   // [1, 13, 2, 23] numbers are treated like strings!
```

### Advanced usage

The `sort()` method can also accept a parameter: `array.sort(compareFunction)`

### **For example**

```js
function compare(a, b){
  if (a < b){return -1;}
  if (a > b){return 1;}
  if (a === b){return 0;}
}

let myArray = [1, 2, 23, 13];
console.log(myArray.sort()); // [ 1, 13, 2, 23 ]
console.log(myArray.sort(compare));   // [ 1, 2, 13, 23 ]

myArray = [3, 4, 1, 2];
sortedArray = myArray.sort(function(a, b){.....});   // it depends from the compareFunction
```

## Array.prototype.some()

The JavaScript array method `.some()` will take a callback function to test each element in the array; once the callback returns `true` then `.some()` will return true immediately.

**Syntax**

```javascript
  var arr = [1, 2, 3, 4];
  arr.some(callback[, thisArg]);
```

## **Callback Function**

**Syntax**

```javascript
  var isEven = function isEven(currentElement, index, array) {
      if(currentElement % 2 === 0) {
          return true;
      } else {
          return false;
      }
  }
```

See wiki on [Arithmetic Operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Arithmetic_Operators) to see the remainder operator `%`

**Has 3 arguments**

currentElement

* this is a variable that represents the element that is being passed to the callback.

index

* this is the index value of the current element starting at 0

array

* the array that `.some()` was call on.

The callback function should implement a test case.

### thisArg

Is an optional parameter and more info can be found at the [MDN

### Description

`.some()` will run the callback function for each element in the array. Once the callback returns true, `.some()` will return `true`. If the callback returns a [falsy value](https://developer.mozilla.org/en-US/docs/Glossary/Falsy) for _every_ element in the array then `.some()` returns false.

`.some()` will not change/mutate the array that called it.

### Examples

**Passing a function to `.some()`**

```javascript
const isEven = function isEven(currentElement, index, array) {
  if(currentElement % 2 === 0) {
      return true;
  } else {
      return false;
  }
}

const arr1 = [1, 2, 3, 4, 5, 6];
arr1.some(isEven);  // returns true
const arr2 = [1, 3, 5, 7];
arr2.some(isEven);  // returns false
```

**Anonymous function**

```javascript
const arr3 = ['Free', 'Code', 'Camp', 'The Amazing'];
arr3.some(function(curr, index, arr) {
  if (curr === 'The Amazing') {
      return true;
  } 
}); // returns true

const arr4 = [1, 2, 14, 5, 17, 9];
arr4.some(function(curr, index, arr) {
  return curr > 20;
  });  // returns false

// ES6 arrows functions
arr4.some((curr) => curr >= 14)  // returns true
```

## Array.prototype.every

The `every()` method tests every whether every element in the array passes the provided test.

**Syntax**

```javascript
  arr.every(callback[, thisArg])
```

### Parameters

1. The **callback** takes up to three arguments:

* **currentValue** (required) – The current element in the array.
* **index** (optional) – The index or the current element in the array.
* **array** (optional) – The array the `every` method was called on.

2.  **thisArg** is optional. It's the value used as `this` in the callback.

## **Description**

The `every` method calls the `callback` function one time for each array element, in ascending index order, until the `callback` function returns false. If an element that causes `callback` to return false is found, the every method immediately returns `false`. Otherwise, the every method returns `true`.

The callback function is not called for missing elements of the array.

In addition to array objects, the every method can be used by any object that has a length property and that has numerically indexed property names. `every` does not mutate the array on which it is called.

## **Examples**

```javascript
  function isBigEnough(element, index, array) {
    return element >= 10;
  }
  [12, 5, 8, 130, 44].every(isBigEnough);   // false
  [12, 54, 18, 130, 44].every(isBigEnough); // true

  // Define the callback function.
  function CheckIfEven(value, index, ar) {
      document.write(value + " ");

      if (value % 2 == 0)
          return true;
      else
          return false;
  }

  // Create an array.
  var numbers = [2, 4, 5, 6, 8];

  // Check whether the callback function returns true for all of the
  // array values.
  if (numbers.every(CheckIfEven))
      document.write("All are even.");
  else
      document.write("Some are not even.");

  // Output:
  // 2 4 5 Some are not even.
```

## **Array.prototype.map**

The `.map()` method loops through the given array and executes the provided function on each element. It returns a new array which contains the results of the function call on each element.

### **Examples**

**ES5**

```js
var arr = [1, 2, 3, 4];
var newArray = arr.map(function(element) { return element * 2});
console.log(newArray); // [2, 4, 6, 8]
```

**ES6**

```js
const arr = [1, 2, 3, 4];
const newArray = arr.map(element => element * 2);
console.log(newArray);
//[2, 4, 6, 8]
```

## **Array.prototype.includes**

The `includes()` method determines whether an array includes a value. It returns true or false.

It takes two arguments:

1. `searchValue` - The element to search for in the array.
2. `fromIndex` - The position in the array to start searching for the proivded `searchValue`. If a negative value is supplied it starts from the array’s length minus the negative value.

### **Example**

```js
const a = [1, 2, 3];
a.includes(2); // true 
a.includes(4); // false
```

## **Array.prototype.toLocaleString**

The `toLocaleString()` method returns a string representing the elements of an array. All the elements are converted to Strings using their toLocaleString methods. The result of calling this function is intended to be locale-specific.

##### **Syntax:**

```text
arr.toLocaleString();
```

##### **Parameters**

* `locales` (Optional) - argument holding either a string or an array of language tags [BCP 47 language tag](http://tools.ietf.org/html/rfc5646).
* `options` (Optional) - object with configuration properties

##### **Return value**

A string representing the elements of the array separated by a locale-specific String (such as a comma “,”)

### Examples

```javascript
const number = 12345;
const date = new Date();
const myArray = [number, date, 'foo'];
const myString = myArray.toLocaleString(); 

console.log(myString); 
// OUTPUT '12345,10/25/2017, 4:20:02 PM,foo'
```

Different outputs could be displayed based on the language and region identifier (the locale).

```javascript
const number = 54321;
const date = new Date();
const myArray = [number, date, 'foo'];
const myJPString = myArray.toLocaleString('ja-JP');

console.log(myJPString);
// OUTPUT '54321,10/26/2017, 5:20:02 PM,foo'
```

And with that, you should know everything necessary to create and manipulate arrays in JavaScript. Now go forth and array stuff up!

## More info about arrays:

* [What in the world is a JavaScript array?](https://www.freecodecamp.org/news/what-in-the-world-is-a-javascript-array/)
* [JavaScript array functions explained with examples](https://www.freecodecamp.org/news/javascript-map-reduce-and-filter-explained-with-examples/)
* [Ultimate guide to Reduce](https://www.freecodecamp.org/news/the-ultimate-guide-to-javascript-array-methods-reduce/)
* [Ultimate guide to Map](https://www.freecodecamp.org/news/the-ultimate-guide-to-javascript-array-methods-map/)
* [JavaScript array length explained](https://www.freecodecamp.org/news/javascript-array-length/)

## More info about callback functions

One thing you've undoubtedly noticed is that many of the array methods use callback functions. Check out these articles for more information about them:

* [What is a callback function in JavaScript?](https://www.freecodecamp.org/news/what-is-a-callback-function-in-javascript/)
* [How to avoid callback hell](https://www.freecodecamp.org/news/how-to-deal-with-nested-callbacks-and-avoid-callback-hell-1bc8dc4a2012/)

