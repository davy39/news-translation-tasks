---
title: JavaScript Array Tutorial – Array Methods in JS
subtitle: ''
author: Dario Di Cillo
co_authors: []
series: null
date: '2023-03-27T19:45:43.000Z'
originalURL: https://freecodecamp.org/news/javascript-array-tutorial-array-methods-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/tom-wilson-Em2hPK55o8g-unsplash.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'Arrays are data structures that are extremely useful and versatile. They''re
  present in many programming languages, and they allow you to store multiple values
  in a single variable.

  In this tutorial, we will explore how arrays work in JavaScript, thei...'
---

Arrays are data structures that are extremely useful and versatile. They're present in many programming languages, and they allow you to store multiple values in a single variable.

In this tutorial, we will explore how arrays work in JavaScript, their characteristics, and how to manipulate them using the most common array methods.

## Table of Contents

1. [How to Create an Array in JavaScript](#heading-how-to-create-an-array-in-javascript)
2. [Array Indexing](#heading-array-indexing)
3. [How to Use the `length` Property](#heading-how-to-use-the-length-property)
4. [Multidimensional Arrays](#heading-multidimensional-arrays) 
5. [Sparse Arrays](#heading-sparse-arrays)
6. [How to Compare Arrays in JavaScript](#heading-how-to-compare-arrays-in-javascript)
7. [The Spread Operator vs the Rest Parameter](#heading-the-spread-operator-vs-the-rest-parameter)
8. [Destructuring Assignment](#heading-destructuring-assignment)
9. [How to Add and Remove Elements from an Array](#heading-how-to-add-and-remove-elements-from-an-array)
10. [How to Combine Arrays](#heading-how-to-combine-arrays) 
11. [How to Convert an Array into a String](#heading-how-to-convert-an-array-into-a-string)
12. [How to Compare Arrays](#heading-how-to-compare-arrays)
13. [How to Copy an Array](#heading-how-to-copy-an-array)
14. [How to Search Inside an Array](#heading-how-to-search-inside-an-array)
15. [How to Check if Array Elements Meet a Condition](#heading-how-to-check-if-array-elements-meet-a-condition)
16. [How to Sort an Array](#heading-how-to-sort-an-array)
17. [How to Perform an Operation on Every Array Element](#heading-how-to-perform-an-operation-on-every-array-element)
18. [Conclusion](#heading-conclusion)

# An Introduction to Arrays in JS

In JavaScript, an array is an **object** constituted by a group of items having a specific **order**. Arrays can hold values of **mixed** data types and their **size** is **not fixed**.

## How to Create an Array in JavaScript

You can create an array using a **literal syntax** – specifying its content inside square brackets, with each item separated by a comma.

Let's create an array of strings, called `nobleGases`:

```js
let nobleGases = ['He', 'Ne', 'Ar', 'Kr', 'Xn'];

console.log(nobleGases); // ['He', 'Ne', 'Ar', 'Kr', 'Xn']
```

Alternatively, you can use the `Array()` **constructor**, passing the elements to put inside the array as arguments.

```js
let nobleGases = Array('He', 'Ne', 'Ar', 'Kr', 'Xn');

console.log(nobleGases); // ['He', 'Ne', 'Ar', 'Kr', 'Xn']
```

## Array Indexing

Each element inside an array is identified by its numeric **index** or position – starting from zero (not 1) in JavaScript, as in many programming languages. We can access elements through **bracket notation**, specifying the index inside square brackets. 

```js
let nobleGases = ['He', 'Ne', 'Ar', 'Kr', 'Xn'];
nobleGases[0]; // 'He'
nobleGases[1]; // 'Ne'
nobleGases[2]; // 'Ar'
nobleGases[3]; // 'Kr'
nobleGases[4]; // 'Xn'
nobleGases[5]; // undefined
```

When you try to access a value out of the index range, you get `undefined` as the return value. As you can see, in the example above no value is stored at index 5.

JavaScript arrays are **not fixed in size**. They can grow and shrink according to their content. You can easily verify this by trying to assign `nobleGases[5]` a value:

```js
let nobleGases = ['He', 'Ne', 'Ar', 'Kr', 'Xn'];
nobleGases[5] = 'Rn';
console.log(nobleGases); // ['He', 'Ne', 'Ar', 'Kr', 'Xn', 'Rn']
```

Now, `nobleGases` holds one more value, as you can see in the output.

## How to Use the `length` Property

You can check the number of elements contained inside an array using the `length` property, through **dot notation**:

```js
nobleGases.length; // 6
```

The array length will be the value of the index of the last element inside the array + 1, since the indexing starts at zero.

## Multidimensional Arrays 

JavaScript arrays can hold any allowed values, arrays included. An array inside another array is called a **nested** array. This situation creates the possibility of many array objects nested at different depths. Here's an example of a three-dimensional array:

```js
let elements = [[['H', 'Li', 'Na'], ['Be', 'Mg']], [['B', 'Al'], ['C', 'Si']]];
```

You can access the different elements by repeating the bracket syntax with the indexes corresponding to the elements you are interested in, to go deeper and deeper. Like so:

```js
console.log(elements[0]); // [['H', 'Li', 'Na'], ['Be', 'Mg']]

console.log(elements[0][0]); // ['H', 'Li', 'Na']

console.log(elements[0][0][0]); // 'H'
```

## Sparse Arrays

Sparse arrays are arrays containing **empty** **slots**. For example, if you mistype two consecutive commas when creating an array, you will end up with a sparse array:

```js
let firstGroup = ['H', 'Li', 'Na',, 'K', 'Rb', 'Cs'];
console.log(firstGroup);
// ['H', 'Li', 'Na', empty, 'K', 'Rb', 'Cs']

```

As you can see, between `'Na'` and `'K'` there is an `empty` value. This can be shown in different ways, depending on the coding environment. But it's not the same as having an `undefined` value.

Sparse arrays can also be created by directly changing the `length` property or by assignment to an index greater than the length:

```js
// Increasing the length property
firstGroup.length = 11;
console.log(firstGroup);
// ['H', 'Li', 'Na', empty, 'K', 'Rb', 'Cs', empty × 4]

// Assigning an element to an index greater than the length
firstGroup[15] = 'Fr';
console.log(firstGroup);
// ['H', 'Li', 'Na', empty, 'K', 'Rb', 'Cs', empty × 8, 'Fr']
```

Depending on the operation performed on a sparse array, empty slots [can act as `undefined` or can be skipped](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#array_methods_and_empty_slots). 

## How to Compare Arrays in JavaScript

JavaScript arrays are objects, and if you try to compare two objects, the comparison takes place considering their **references** – and not their actual **values**.

This means that you could try to compare two arrays containing the same elements – and so, that are apparently equal – like this:

```js
let dough1 = ['flour', 'water', 'yeast', 'salt'];
let dough2 = ['flour', 'water', 'yeast', 'salt'];

dough1 === dough2; // false
```

But, according to JavaScript, they are not equal. And even the comparison of two empty arrays, no matter how they're created, would return the same result:

```js
[] === []; // false
Array() === Array(); // false
```

As I mentioned, this happens because **object references are compared**, and not their actual content. And each time you create a new array object, it will have a different reference in memory.

The only way to make this comparison evaluate to `true` is to make the two arrays point to the same reference. For example:

```js
let dough1 = ['flour', 'water', 'yeast', 'salt'];
let dough2 = dough1;

dough1 === dough2; // true
```

In the code above, `let dough2 = dough1` does not mean you are making a copy of `dough1`. It means the `dough2` variable will point exactly to the same reference as `dough1`. They are the same array object.

Having said that, if you want to compare two arrays, you will need to adopt a different strategy. A good approach would be iterating through the array and comparing each element one by one. You can do this with a `for` loop and some conditional statements:

```js
const compareArr = (arr1, arr2) => {
    if (arr1.length !== arr2.length) {
        return false
    } 
    for (let i = 0; i < arr1.length; i++) {
    	if (arr1[i] !== arr2[i]) {
            return false
        }
    }
    return true
};
```

In the code snippet above, you can see a function to check if the two arrays are equal. 

* The first step is verifying if the arrays have the same length. If the length is different, they cannot be equal for sure:

```js
if (arr1.length !== arr2.length) {
        return false
    }
```

* Then, a `for` loop iterates through the array and an `if` statement checks if each element of the first array is different from the element at the corresponding index in the second array:

```js
for (let i = 0; i < arr1.length; i++) {
    	if (arr1[i] !== arr2[i]) {
            return false
        }
    }
```

* If no difference is caught, the arrays are equal and the function returns `true`.

Here's the result of comparing the two arrays from the beginning of this section with our function:

```js
let dough1 = ['flour', 'water', 'yeast', 'salt'];
let dough2 = ['flour', 'water', 'yeast', 'salt'];

compareArr(dough1, dough2); // true
```

Note that we can apply this function only to an array containing **primitive** values_._ If an array contains objects, you should try to figure out the solution that fits your specific problem and deepen the check.

For example, if you know your arrays are nested, like these:

```js
let metal1 = [['Li', 'Na', 'K'], ['Be', 'Mg', 'Ca']];
let metal2 = [['Li', 'Na', 'K'], ['Be', 'Mg', 'Ca']];
```

 One possible solution would be the following:

```js
const compareNested = (arr1, arr2) => {
    if (arr1.length !== arr2.length) {
        return false
    } for (let i = 0; i < arr1.length; i++) {
        for (let j = 0; j < arr1[i].length; j++) {
            if (arr1[i][j] !== arr2[i][j]) {
                return false
            }
        }
    }
    return true
};

compareNested(metal1, metal2); // true
```

With respect to the previous function, we added an additional `for` loop. This is enough to compare elements inside the inner arrays.

If you need to compare two arrays of objects:

```js
let albums1 = [
    {artist: 'Frank Zappa', title: 'Over-Nite Sensation', year: 1973},
    {artist: 'Frank Zappa', title: 'Apostrophe', year: 1974},
    {artist: 'Frank Zappa', title: 'One Size Fits All', year: 1975}
];
let albums2 = [
    {artist: 'Frank Zappa', title: 'Over-Nite Sensation', year: 1973},
    {artist: 'Frank Zappa', title: 'Apostrophe', year: 1974},
    {artist: 'Frank Zappa', title: 'One Size Fits All', year: undefined},
];
```

 You can do something like this:

```js
const compareArrObj = (arr1, arr2) => {
    if (arr1.length !== arr2.length) {
        return false
    }
    for (let i = 0; i < arr1.length; i++) {
        if (Object.keys(arr1[i]).length !== Object.keys(arr2[i]).length) {
            return false
        }
        for (let prop in arr1[i]) {
            if (arr1[i][prop] !== arr2[i][prop]) {
                return false
            }
        }
    }
    return true
};
```

* Again, the first step is verifying if the arrays have the same length. If the length is different, they cannot be equal.
* A `for` loop iterates through the array and an `if` statement checks if each object of the first array has a different length from the object at the corresponding index in the second array:

```js
for (let i = 0; i < arr1.length; i++) {
        if (Object.keys(arr1[i]).length !== Object.keys(arr2[i]).length) {
            return false
        }
//...
}
```

* Then a `for`...`in` loop iterates through the properties of the i-th object of the first array. And an `if` statement checks if the value of each key is different from the value of the corresponding key in the i-th object of the other array:

```js
for (let prop in arr1[i]) {
            if (arr1[i][prop] !== arr2[i][prop]) {
                return false
            }
        }
```

In the end, the result would be:

```js
compareArrObj(albums1, albums2); // false
```

Because the `year` value in the third object of `albums2` is different. If we change it, the result will be `true`:

```js
albums2[2]['year'] = 1975;

compareArrObj(albums1, albums2); // true
```

## The Spread Operator vs the Rest Parameter

The spread operator and the rest parameter have similar syntax (`...`) but they perform fundamentally different operations. 

The **spread** operator enables you to **expand** an array – more generally an iterable object – into its elements. The **rest** parameter allows you to collect an undefined number of arguments into **a single array**.

### How to Use the Spread Operator

Later on in this article, we will see some methods to copy an array or to merge different arrays. But using the spread operator is a valid alternative to do the same things.

In the example below, the `alkali` and `alkEarth` arrays are merged into a single array using the spread syntax. To do this, you need to list the arrays you want to merge between square brackets, prepending three dots to each one.

```js
let alkali = ['Li', 'Na', 'K'];
let alkEarth = ['Be', 'Mg', 'Ca'];

// Merging two arrays with the spread operator
let metals = [...alkali, ...alkEarth];
console.log(metals); // ['Li', 'Na', 'K', 'Be', 'Mg', 'Ca']
```

Also, you can use the same syntax with only one array, to create a copy of an array:

```js
// Copying an array with the spread operator
let metalsCopy = [...metals];
console.log(metalsCopy); // ['Li', 'Na', 'K', 'Be', 'Mg', 'Ca']

```

### How to Use the Rest Parameter

The rest parameter allows you to collect an undefined number of elements into a single array. The rest parameter needs to be the last in a sequence of function parameters. Also, a function can have only one rest parameter.

```js
function f1(first, second, third, ...others) {
	console.log(first);
    console.log(second);
    console.log(third);
    console.log(others);
};

f1('He', 'Ne', 'Ar', 'Kr', 'Xn', 'Rn'); 
// He
// Ne
// Ar
// ['Kr', 'Xn', 'Rn']
```

In the example above, the `f1` function is called with six string arguments. And the arguments after the third one are gathered inside the `others` array by using the rest syntax.

In general, the arguments passed to a function are collected in the `arguments` object, which is an array-like object and does not support the iterative methods we will see in the next section macro-section of this article.

So, the rest parameter provides a way to easily access the arguments passed to a function in array form, instead of using the `arguments` object:

```js
function f2(...args) {
	console.log(args);
    // you can use an iterative method on the args array
};

f2('He', 'Ne', 'Ar', 'Kr', 'Xn', 'Rn');
// ['He', 'Ne', 'Ar', 'Kr', 'Xn', 'Rn']
```

In the example above, we have simply printed the `args` array, but the advantage here is being able to implement an iterative method on it.

## Destructuring Assignment

The destructing syntax provides a simple way to assign values by unpacking them from an array object. Let's see a practical example:

```js
let nobleGases = ['He', 'Ne', 'Ar', 'Kr', 'Xn'];
let [firstRow, secondRow,,FourthRow] = nobleGases;
console.log(firstRow); // 'He'
console.log(secondRow); // 'Ne'
console.log(FourthRow); // 'Kr'
// 'Ar' is skipped because of the additional comma
```

The variables on the left side of the assignment operator are assigned to the value of the corresponding elements of the array on the right. You can skip array elements and go to the next ones by typing more than one comma between each variable name.

# Common Array Methods in JS

In JavaScript, arrays are **objects** and possess **properties** and **methods**.

In this section, we will discuss some of the most common array methods you need to know to work efficiently with arrays in JavaScript.

## How to Add and Remove Elements from an Array

In this section, you will see the most common ways to add and remove elements from an array in JavaScript. All the following methods **mutate** the original array.

### How to Use the `push()` Method

Let's consider the example from the indexing section:

```js
let nobleGases = ['He', 'Ne', 'Ar', 'Kr', 'Xn'];
nobleGases[5] = 'Rn';
console.log(nobleGases); // ['He', 'Ne', 'Ar', 'Kr', 'Xn', 'Rn']
```

We have assigned `Rn` to index `5` of the `nobleGases` array using the bracket notation. At the end of the day, we have simply added `Rn` at the end of that array. 

You can obtain the same result using the `push()` method, and you don't need to know the length of the array for that. You use the dot notation to call `push()`, indicating the element(s) to append inside the parenthesis. Like this:

```js
// Syntax
array.push(element1, /* … ,*/ elementN)
```

The specified element will be added at the **end** of the array, returning the new array length. For example:

```js
let nobleGases = ['He', 'Ne', 'Ar', 'Kr', 'Xn'];
nobleGases.push('Rn'); // 6
// push() returns the length of the modified array
console.log(nobleGases); // ['He', 'Ne', 'Ar', 'Kr', 'Xn', 'Rn']
```

You can append multiple elements with `push()`, indicating their values separated by a comma:

```js
let halogens = ['F', 'Cl'];
console.log(halogens); // ['F', 'Cl']

halogens.push('Br', 'I', 'At'); // 5
// push() returns the length of the modified array
console.log(halogens); // ['F', 'Cl', 'Br', 'I', 'At']
```

### How to Use the `unshift()` Method

Similar to `push()`, the `unshift()` method adds one or more elements to the **beginning** of an array and returns the length of the modified array.

```js
// Syntax
array.unshift(element1, /* … ,*/ elementN)
```

For example:

```js
let halogens = ['F', 'Cl'];
console.log(halogens); // ['F', 'Cl']

halogens.unshift('Br', 'I', 'At'); // 5
// unshift() returns the length of the modified array
console.log(halogens); // ['Br', 'I', 'At', 'F', 'Cl']
```

### How to Use the `pop()` Method

If you need to remove the **last** element of an array, you can use the `pop()` method.

```js
// Syntax
array.pop()
```

 It removes only the last element and returns it.

```js
let nobleGases = ['He', 'Ne', 'Ar', 'Kr', 'Xn', 'Rn'];
console.log(nobleGases); // ['He', 'Ne', 'Ar', 'Kr', 'Xn', 'Rn']

nobleGases.pop(); // 'Rn'
// pop() returns the removed element
console.log(nobleGases); // ['He', 'Ne', 'Ar', 'Kr', 'Xn']
```

### How to Use the `shift()` Method

Similarly, the `shift()` method removes the **first** element from an array and returns it.

```js
// Syntax
array.shift()
```

Here's an example:

```js
let nobleGases = ['He', 'Ne', 'Ar', 'Kr', 'Xn', 'Rn'];
console.log(nobleGases); // ['He', 'Ne', 'Ar', 'Kr', 'Xn', 'Rn']

nobleGases.shift(); // 'He'
// shift() returns the removed element
console.log(nobleGases); // ['Ne', 'Ar', 'Kr', 'Xn', 'Rn']
```

### How to Use the `splice()` Method

If you need to remove one or more elements from a specific position of an array, you can use the `splice()` method.

```js
// Syntax
array.splice(start, count)
```

The first parameter of `splice()` is the **starting index**, while the second is the **number of items to remove** from the array.

```js
let nobleGases = ['He', 'Ne', 'Ar', 'Kr', 'Xn', 'Rn'];
console.log(nobleGases); // ['He', 'Ne', 'Ar', 'Kr', 'Xn', 'Rn']

nobleGases.splice(1, 3); // ['Ne', 'Ar', 'Kr']
// splice() returns an array with removed elements
console.log(nobleGases); // ['He', 'Xn', 'Rn']
```

 So `.splice(1, 3)` means "start at index = `1` and remove `3` elements". The method returns an array containing the elements removed from the original array.

If the second argument is not supplied, the elements are removed until the end.

Using `splice()` you can add elements, too. 

```js
// Syntax
array.splice(start, count, addition1, /* … ,*/ additionN)
```

If you specify additional arguments – after the starting index and the number of elements to remove – those will be inserted in the indicated position. For example:

```js
let nobleGases = ['He', 'Ne', 'Cl', 'Rn'];
console.log(nobleGases); // ['He', 'Ne', 'Cl', 'Rn']

nobleGases.splice(2, 1, 'Ar', 'Kr', 'Xn'); // ['Cl']
// splice() returns an array with removed elements
console.log(nobleGases); // ['He', 'Ne', 'Ar', 'Kr', 'Xn', 'Rn']
```

Here, `.splice(2, 1, 'Ar', 'Kr', 'Xn')` means "start at index = `2`, remove `1` element and add the strings `'Ar'`, `'Kr'`, `'Xn'`". The array returned by the method contains the element `'Cl'`, which was at index = `2` in the original array.

If you don't need to remove any elements from the array, you can simply use zero as the second argument. The elements will be added starting at the specified index, without removing any item:

```js
let nobleGases = ['He', 'Ne', 'Rn'];
console.log(nobleGases); // ['He', 'Ne', 'Rn']

nobleGases.splice(2, 0, 'Ar', 'Kr', 'Xn'); // []
// splice() returns an array with removed elements
console.log(nobleGases); // ['He', 'Ne', 'Ar', 'Kr', 'Xn', 'Rn']
```

## How to Combine Arrays 

### How to Use the `concat()` Method

If you need to combine two or more arrays – that is create a single array containing each element of the arrays you want to merge – you can use the `concat()` method. This method does not change the original arrays and returns a new array.

You need to call `.concat()` on the array that should come first, passing as arguments the arrays you want it to merge with. The order will be reflected in the resulting array.

```js
// Syntax
array1.concat(array2, /* … ,*/ arrayN)
```

Here's an example of combining two and three arrays:

```js
let alkali = ['Li', 'Na', 'K'];
let moreAlkali = ['Rb', 'Cs', 'Fr'];
let alkEarth = ['Be', 'Mg', 'Ca'];

alkali.concat(moreAlkali);
// ['Li', 'Na', 'K', 'Rb', 'Cs', 'Fr']

alkali.concat(moreAlkali, alkEarth);
// ['Li', 'Na', 'K', 'Rb', 'Cs', 'Fr', 'Be', 'Mg', 'Ca']
```

### How to Use the `push()` Method & the Spread Operator

If you don't mind changing the original array you can combine a `.push()` call to the spread syntax (`...`) to add all the elements in one or more arrays to the original array. For example:

```js
let alkali = ['Li', 'Na', 'K'];
let moreAlkali = ['Rb', 'Cs', 'Fr'];
let alkEarth = ['Be', 'Mg', 'Ca'];

alkali.push(...moreAlkali); // 6
console.log(alkali); // ['Li', 'Na', 'K', 'Rb', 'Cs', 'Fr']
```

You cannot use `push()` without the spread syntax in its arguments, unless you want to nest the whole array `moreAlkali` as the last element of `alkali`. In that case, the result would be `['Li', 'Na', 'K', ['Rb', 'Cs', 'Fr']]` – an array composed of 4 elements with the last being an array.

Note that, as we have seen previously, the spread operator alone allows you to merge two or more arrays without causing any mutation. As a continuation of the previous example:

```js
let metals = [...alkali, ...alkEarth];
console.log(metals); // ['Li', 'Na', 'K', 'Rb', 'Cs', 'Fr', 'Be', 'Mg', 'Ca']
console.log(alkali); // ['Li', 'Na', 'K', 'Rb', 'Cs', 'Fr']
```

## How to Convert an Array into a String

If you need to convert an array into a string, you have different options. And now, we are going to see some of them. Note that the following methods do not mutate the original array.

### How to Use the `toString()` & `join()` Methods

These methods enable you to convert arrays into strings.

The `toString()` method is called without a parameter and returns a string representing the content of the array. 

```js
// Syntax
array.toString()
```

The `join()` method takes a separator as the argument, which is used to separate the array elements, in order to form the string.

```js
// Syntax
array.join(separator)
```

Here's an example:

```js
let animals = ['pig', 'dog', 'sheep'];

animals.toString(); // 'pig,dog,sheep'

animals.join(', '); // 'pig, dog, sheep'

animals.join(' '); // 'pig dog sheep'

animals.join(' * '); // 'pig * dog * sheep'
```

These two methods have some limitations. If we consider the array in the following example, we can observe a couple of interesting things:

```js
let arr = [1, 'two', null, undefined, true, {}];

arr.toString(); // '1,two,,,true,[object Object]'

arr.join(); // '1,two,,,true,[object Object]'
```

First, `null` and `undefined` result in the same string output (an empty substring). 

Second, the string representation of an object is `[object Object]`. So if you are trying to convert an array containing objects into a string, you should employ another method. Otherwise, you will not be able to see the object content properly.

### How to Use the `JSON.stringify()` Method

If you want to convert an array containing objects into a string, the `JSON.stringify()` method is what you need. Where the previous methods fail, `JSON.stringify()` enables you to handle objects properly.

```js
// Syntax
JSON.stringify(array)
```

This method takes a JavaScript value as the argument – in this case the `albums` array – and converts it to a JSON string.

```js
let albums = [
    {artist: 'Frank Zappa', title: 'Apostrophe', year: 1974},
    {artist: 'Frank Zappa', title: 'One Size Fits All', year: 1975}
];

JSON.stringify(albums);
//'[{"artist":"Frank Zappa","title":"Apostrophe","year":1974},{"artist":"Frank Zappa","title":"One Size Fits All","year":1975}]'
```

As you can see, the square brackets are retained, so it is often desirable to use this method to create a string from an array.

## How to Compare Arrays

Since arrays are objects, their **comparison is based on references**. Not on the actual values.

Before, we have seen some ways to compare arrays by looping through an array and comparing each element.

Another approach for comparing arrays is converting them into strings with one of the previous methods, and then comparing the string representations of the original arrays.

This is quite fast and easy, but sometimes it can lead to unexpected behavior. For example, when `null` and `undefined` values are compared.

```js
let a = [1, null, 3];
let b = [1, undefined, 3];

a[1] === b[1]; // false

JSON.stringify(a) === JSON.stringify(b); // true

```

You might think that the comparison between the string representation of `a` and `b` would return `false`, since `null` and `undefined` are not equal. But in practice, they are both stringified to null.

In light of this aspect, it would be better to use an iterative technique.

### How to Use the `every()` Method

`every()` is an iterative method that verifies if all the elements in the array pass a condition implemented by a callback function and it returns `true` or `false`.

```js
// Syntax
array.every((element, index, array) => {})
```

Among its many uses, you can build a simple function to compare arrays containing primitive values with `every()`, like this:

```js
const compareEvery = (arr1, arr2) => {
    return arr1.length === arr2.length &&
    arr1.every((elem, index) => elem === arr2[index])
}
```

* First, the lengths are compared. If they are not equal, the arrays are not equal as well.
* Then, `every()` is called on the first array. The callback checks if every element of `arr1` is equal to the element at the corresponding index in `arr2`.

```js
arr1.every((elem, index) => elem === arr2[index])
```

The AND operator ensures that `true` is returned only when both conditions are true.

Here's the function applied to the arrays from before:

```js
let a = [1, null, 3];
let b = [1, undefined, 3];

compareEvery(a,b); // false

```

## How to Copy an Array

All common operations to copy an array in JavaScript generate a **[shallow copy](https://developer.mozilla.org/en-US/docs/Glossary/Shallow_copy)** – instead of a deep copy – of the original array. This means that by mutating the copy, you can change the original array, too. We will see why this happens in a while.

### How to Use the `slice()` Method

The `slice()` method allows you to copy an entire array – or just a portion of it – without mutating it.

```js
// Syntax
array.slice(start, end)
```

As parameters, it takes the **starting index** and the **final index** (not included) to copy. When called without arguments, `slice()` create a duplicate of the whole array. For example:

```js
let dough = ['flour', 'water', 'yeast', 'salt'];

let doughCopy = dough.slice();
console.log(doughCopy); // ['flour', 'water', 'yeast', 'salt']
```

If you try to change `doughCopy` in some way, for example, assigning `doughCopy[1]` a new value, you would see that no change is reflected in the original array:

```js
doughCopy[1] = 'wine';
console.log(doughCopy); // ['flour', 'wine', 'yeast', 'salt']

console.log(dough); // ['flour', 'water', 'yeast', 'salt']
```

This happens because the array is filled with primitive values. However, the story is quite different if you handle an array containing non-primitive values.

Let's consider the following array, with two objects:

```js
let albums = [
    {artist: 'Frank Zappa', title: 'Apostrophe'},
    {artist: 'Frank Zappa', title: 'One Size Fits All'}
];
```

You copy the array using the `slice()` method, like this:

```js
let albumsCopy = albums.slice();
```

Now, `albumsCopy` represents a shallow copy of `albums` and the elements inside each array point to the same objects. In other words, both `albums[0] === albumsCopy[0]` and `albums[1] === albumsCopy[1]` return `true` – remember that this comparison involves object references – because they are the very same objects.

If you change one of them by mutating a property value, the modification involves the other array, too.

```js
albumsCopy[1]['title'] = 'Absolutely Free';
console.log(albumsCopy);
// [
//  {artist: 'Frank Zappa', title: 'Apostrophe'},
//  {artist: 'Frank Zappa', title: 'Absolutely Free'}
// ];

console.log(albums);
// [
//  {artist: 'Frank Zappa', title: 'Apostrophe'},
//  {artist: 'Frank Zappa', title: 'Absolutely Free'}
// ];
```

Note that if you reassign an element to a different object – that is without mutating any of the existent objects – the modification does not involve the other array:

```js
albumsCopy[1] = {artist: 'Captain Beefheart', title: 'Safe as Milk'};

console.log(albumsCopy);
// [
//  {artist: 'Frank Zappa', title: 'Apostrophe'},
//  {artist: 'Captain Beefheart', title: 'Safe as Milk'}
// ];

console.log(albums);
// [
//  {artist: 'Frank Zappa', title: 'Apostrophe'},
//  {artist: 'Frank Zappa', title: 'Absolutely Free'}
// ];
```

### How to Use the `map()` Method

The `map()` method generates a new array containing the result of calling a callback function on every element of an array. 

```js
// Syntax
array.map((element, index, array) => {})
```

The function takes the current element, its index, and the array on which the method is called, as parameters. 

You can use `map()` to copy an array by specifying a function that returns each array element:

```js
let albums = [
    {artist: 'Frank Zappa', title: 'Apostrophe'},
    {artist: 'Frank Zappa', title: 'One Size Fits All'}
];

let mapAlbums = albums.map(element => element);
console.log(mapAlbums);
// [
//  {artist: 'Frank Zappa', title: 'Apostrophe'},
//  {artist: 'Frank Zappa', title: 'One Size Fits All'}
// ];
```

### How to Create a Deep Copy

If you want to create a deep clone of an array, you can convert the array into a string with `JSON.stringify()` and pass its return value to the `JSON.parse()` method.

```js
let albums = [
    {artist: 'Frank Zappa', title: 'Apostrophe'},
    {artist: 'Frank Zappa', title: 'One Size Fits All'}
];

let albumsCopy = JSON.parse(JSON.stringify(albums));
console.log(albumsCopy);
// [
//  {artist: 'Frank Zappa', title: 'Apostrophe'},
//  {artist: 'Frank Zappa', title: 'One Size Fits All'}
// ];
```

In this way, the copy will be completely independent of the original array and you will not risk an unintentional modification.

## How to Search Inside an Array

Depending on what you are looking for, there are several ways to search inside an array. Let's explore some methods to search inside an array by index and by value.

### How to Use the `includes()` Method

If you need to know whether a value is included in an array, you can call the `includes()` method on it, passing the value you are interested in as the argument.

```js
// Syntax
array.includes(value, startingIndex)
```

This method returns `true` if the value is found. Otherwise, `false`.

```js
let dMinor = ['D', 'E', 'F', 'G', 'A', 'B♭', 'C'];

dMinor.includes('E'); // true
dMinor.includes('E', 2); // false
```

It accepts also a second parameter, representing the index where to begin to search – the default is zero.

### How to Use the `indexOf()` Method

If you need to know the index at which a specific value can be found in an array, you should use the `indexOf()` method.

```js
// Syntax
array.indexOf(value, startingIndex)
```

It returns only the **first index** at which the specified value is found, otherwise, it returns -1. The second parameter is the index for where to start searching for the value – the default is zero.

```js
let dMinor = ['D', 'E', 'F', 'G', 'A', 'B♭', 'C'];

dMinor.indexOf('E'); // 1
dMinor.indexOf('E', 2); // -1
```

### How to Use the `find()` & `findLast()` Methods

`find()` and `findLast()` enable you to search for the **first** and the **last** element that satisfies a certain condition in an array, respectively.

```js
// Syntax
array.find((element, index, array) => {})

array.findLast((element, index, array) => {})
```

They both accept a callback function, whose parameters are the current element, its index, and the array the method is called upon.

`find()` and `findLast()` return the first/last element that satisfies the function, or `undefined` when the no value matches the specified condition.

```js
let animals = [
    {no: 1, track: 'Pigs on the Wing (Part One)'},
    {no: 2, track: 'Dogs'},
    {no: 3, track: 'Pigs (Three Different Ones)'},
    {no: 4, track: 'Sheep'},
    {no: 5, track: 'Pigs on the Wing (Part Two)'}
];

animals.find(el => el['track'].includes('Pigs'));
// {no: 1, track: 'Pigs on the Wing (Part One)'}

animals.findLast(el => el['track'].includes('Pigs'));
// {no: 5, track: 'Pigs on the Wing (Part Two)'}

animals.find(el => el['track'].includes('Horses'));
// undefined
```

In the example above, only the first and the last objects containing 'Pigs' are found. The middle object `{no: 3, track: 'Pigs (Three Different Ones)'}` cannot be reached by these two methods.

### How to Use the `findIndex()` & `findLastIndex()` Methods

The `findIndex()` and `findLastIndex()` methods work similarly to the previous ones.

```js
// Syntax
array.findIndex((element, index, array) => {})

array.findLastIndex((element, index, array) => {})
```

But they return the **index** of the first and the last element that satisfies the provided condition, respectively, or `undefined` when the no value matches the specified condition.

```js
let animals = [
    {no: 1, track: 'Pigs on the Wing (Part One)'},
    {no: 2, track: 'Dogs'},
    {no: 3, track: 'Pigs (Three Different Ones)'},
    {no: 4, track: 'Sheep'},
    {no: 5, track: 'Pigs on the Wing (Part Two)'}
];

animals.findIndex(el => el['track'].includes('Pigs')); // 0

animals.findLastIndex(el => el['track'].includes('Pigs')); // 4

animals.findIndex(el => el['track'].includes('Horses')); // -1
```

## How to Check if Array Elements Meet a Condition

### How to Use the `every()` & `some()` Methods

Sometimes you want to verify if the elements inside an array satisfy a specific condition. We have already seen the `every()` method in a previous section. It loops through the array and returns `true` if all the elements meet the specified condition. Otherwise, it returns `false`.

```js
// Syntax
array.every((element, index, array) => {})

array.some((element, index, array) => {})
```

The `some()` method is very similar. It iterates through the array, testing if **some** elements – not all of them – meet the requirements implemented by a callback function.

```js
let nobleGases = ['He', 'Ne', 'Ar', 'Kr', 'Xn'];

nobleGases.every(el => typeof el == 'string'); // true

nobleGases.some(el => el == 'Ar'); // true

nobleGases.some(el => el == 'Rn'); // false
```

The last call returns `false` since none of the array elements is equal to the string `'Rn'`.

### How to Use the `filter()` Method

This method provides you a way to filter the array elements that satisfy a certain criterion.

```js
// Syntax
array.filter((element, index, array) => {})
```

`filter()` takes a callback function, whose parameters are the current element, its index, and the array the method is called upon.

It creates a shallow copy of the original array containing only the values for which the callback returns a truthy value, and it neglects the others.

```js
let animals = [
    {no: 1, track: 'Pigs on the Wing (Part One)'},
    {no: 2, track: 'Dogs'},
    {no: 3, track: 'Pigs (Three Different Ones)'},
    {no: 4, track: 'Sheep'},
    {no: 5, track: 'Pigs on the Wing (Part Two)'}
];

animals.filter(el => el['track'].includes('Pigs'));
// [
// {no: 1, track: 'Pigs on the Wing (Part One)'},
// {no: 3, track: 'Pigs (Three Different Ones)'},
// {no: 5, track: 'Pigs on the Wing (Part Two)'}
// ]
```

Above, only the elements including 'Pigs' are inserted in the filtered array.

## How to Sort an Array

### How to Use the `sort()` Method

If you want to sort an array, you can use `sort()`. This method sorts the array elements **in place**. It changes the array which it's acting on.

```js
// Syntax
array.sort()

array.sort((a, b) => {})
```

The default sorting procedure evaluates Unicode point values and sometimes may lead to unexpected outcomes. For this reason, it is better to pass `sort()` a callback function so that the elements can be sorted according to the return value of the callback.

The following table sums up the sorting criterion at the base of `sort()`.

| (a, b) comparison return value | order |
|-|-|
| > 0 | [b, a] |
| < 0 | [a, b] |
| === 0 |original order |

The elements – represented by a and b parameters – are compared two at a time. If the return value is positive, a is placed after b. If it is negative, b is placed after a. While if the return value is zero the original order is kept.

Here's an example of sorting an array of strings in ascending and descending order:

```js
let nobleGases = ['He', 'Ne', 'Ar', 'Kr', 'Xn', 'Rn'];

// sorting in ascending order
nobleGases.sort((a, b) => {
   return a === b ? 0 : a > b ? 1 : -1; 
}); 
// ['Ar', 'He', 'Kr', 'Ne', 'Rn', 'Xn']

// sorting in descending order
nobleGases.sort((a, b) => {
   return a === b ? 0 : a < b ? 1 : -1; 
});
// ['Xn', 'Rn', 'Ne', 'Kr', 'He', 'Ar']

 
```

The callback function is implemented by a ternary operator, in order to consider the three possible outcomes of the comparison.

## How to Perform an Operation on Every Array Element

### How to Use the `map()` Method

Previously, we used `map()` to duplicate an array. But by using a different callback function you can perform many different operations.

```js
let animals = [
    {no: 1, track: 'Pigs on the Wing (Part One)'},
    {no: 2, track: 'Dogs'},
    {no: 3, track: 'Pigs (Three Different Ones)'},
    {no: 4, track: 'Sheep'},
    {no: 5, track: 'Pigs on the Wing (Part Two)'}
];

let tracks = animals.map(el => el['track']);

console.log(tracks); // ['Pigs on the Wing (Part One)', 'Dogs', 'Pigs (Three Different Ones)', 'Sheep', 'Pigs on the Wing (Part Two)']
```

In the example above, we have used `map()` to create an array populated with the values of the `track` key of each object in the `animals` array.

### How to Use the `forEach()` Method

The `forEach()` method is similar to `map()`. It executes a function on every array element, but it has no return value. For this reason, a `forEach()` call can be used only at the end of a chain.

```js
// Syntax
array.forEach((element, index, array) => {})
```

In the example below, `forEach()` is used to delete the `no` property from each array element:

```js
let animals = [
    {no: 1, track: 'Pigs on the Wing (Part One)'},
    {no: 2, track: 'Dogs'},
    {no: 3, track: 'Pigs (Three Different Ones)'},
    {no: 4, track: 'Sheep'},
    {no: 5, track: 'Pigs on the Wing (Part Two)'}
];

animals.forEach(el => delete el['no']); // it returns undefined

console.log(animals); 
// [
//   {track: 'Pigs on the Wing (Part One)'},
//   {track: 'Dogs'},
//   {track: 'Pigs (Three Different Ones)'},
//   {track: 'Sheep'},
//   {track: 'Pigs on the Wing (Part Two)'}
// ]
```

### How to Use the `reduce()` Method

The `reduce()` method accepts a callback function, which is executed on each array element. The callback takes an accumulator as the first parameter, followed by the current element, its index, and the array which the method is called on.

The return value of each iteration is passed to the next one. So that the array is reduced to a single value. The second parameter of `reduce()` is the starting value of the `accumulator`. If not specified, `accumulator` takes the first array value and the iteration starts at index 1.

```js
// Syntax
array.reduce((accumulator, element, index, array) => {}, initialValue)
```

In the example below, the `reduce()` method is used to count the number of tracks that include 'Pigs' in the title. The method iterates through the array, and when the track property includes 'Pigs', the value of count is incremented and passed to the next iteration.

```js
let animals = [
    {no: 1, track: 'Pigs on the Wing (Part One)'},
    {no: 2, track: 'Dogs'},
    {no: 3, track: 'Pigs (Three Different Ones)'},
    {no: 4, track: 'Sheep'},
    {no: 5, track: 'Pigs on the Wing (Part Two)'}
];

let countPigs = animals.reduce((count, el) => {
	return el['track'].includes('Pigs') ? count + 1 : count
	}, 0);

console.log(countPigs); // 3

```

In this case, it's important to specify the initial value as zero. Otherwise, the initial value will be the whole `{no: 1, track: 'Pigs on the Wing (Part One)'}` object, and this will lead to an unexpected result.

## Conclusion

In JavaScript, arrays are data structures that contain multiple values in a specific order. They can hold values of different data types and they are re-sizable.

In this tutorial, we started with the basics of arrays in JavaScript and then we discussed some of the most common methods that allow you to manipulate arrays.

We have only begun to scratch the surface of this wide topic, but I hope this is a good starting point for you.

Thanks for reading, and happy coding.

