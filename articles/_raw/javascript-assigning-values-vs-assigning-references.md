---
title: JavaScript Primitive Values vs Reference Values – Explained with Examples
subtitle: ''
author: German Cocca
co_authors: []
series: null
date: '2023-04-18T16:31:17.000Z'
originalURL: https://freecodecamp.org/news/javascript-assigning-values-vs-assigning-references
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/pexels-pedro-figueras-681447.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'Hi everyone! In JavaScript, variables can hold two types of data: primitive
  values and reference values. Understanding the difference between these two types
  of data is crucial for writing efficient and bug-free code.

  In this short article, we will e...'
---

Hi everyone! In JavaScript, variables can hold two types of data: primitive values and reference values. Understanding the difference between these two types of data is crucial for writing efficient and bug-free code.

In this short article, we will explore the difference between values and references in JavaScript.

# Table of Contents

* [What are primitive values?](#heading-what-are-primitive-values)
    
* [What are reference values?](#heading-what-are-reference-values)
    
* [How to pass values and references as function arguments](#heading-how-to-pass-values-and-references-as-function-arguments)
    
* [How to create copies of objects, arrays and functions](#heading-how-to-create-copies-of-objects-arrays-and-functions)
    
    * [Shallow vs deep copies](shallow-vs-deep-copies)
        
* [Wrapping up](#heading-wrapping-up)
    

# What are Primitive Values?

Primitive values are data that are stored directly in a variable. These include numbers, booleans, strings, null, and undefined.

When we assign a primitive value to a variable, a copy of that value is created and stored in memory. Any changes made to the variable do not affect the original value.

For example:

```javascript
let x = 5;
let y = x;
y = 10;
console.log(x); // Output: 5
console.log(y); // Output: 10
```

In the example above, the variable `y` is assigned a copy of the value of `x`. When we change the value of `y`, it does not affect the value of `x`. This is because `x` and `y` are separate variables with separate memory locations.

# What are Reference Values?

Reference values, on the other hand, are objects that are stored in memory and accessed through a reference. These include arrays, objects, and functions.

When we assign a reference value to a variable, a reference to the original value is created and stored in memory. Any changes made to the variable affect the original value.

For example:

```javascript
let array1 = [1, 2, 3];
let array2 = array1;
array2.push(4);
console.log(array1); // Output: [1, 2, 3, 4]
console.log(array2); // Output: [1, 2, 3, 4]
```

In the example above, the variable `array2` is assigned a reference to the original array `array1`. When we push a value to `array2`, it also affects `array1` because both variables reference the same memory location.

# How to Pass Values and References as Function Arguments

When we pass a primitive value as an argument to a function, a copy of that value is created and passed to the function. Any changes made to the variable inside the function do not affect the original value.

For example:

```javascript
function addOne(x) {
    x++;
    return x;
}

let number = 5;
console.log(addOne(number)); // Output: 6
console.log(number); // Output: 5
```

In the example above, the function `addOne` receives a copy of the value of `number`. When we increment the value of `x` inside the function, it does not affect the value of `number`.

When we pass a reference value as an argument to a function, a reference to the original value is passed. Any changes made to the variable inside the function affect the original value.

For example:

```javascript
function addToArray(array) {
    array.push(4);
    return array;
}

let myArray = [1, 2, 3];
console.log(addToArray(myArray)); // Output: [1, 2, 3, 4]
console.log(myArray); // Output: [1, 2, 3, 4]
```

In the example above, the function `addToArray` receives a reference to the original array `myArray`. When we push a value to `array` inside the function, it also affects `myArray` because both variables reference the same memory location.

# How to Create Copies of Objects, Arrays, and Functions

Creating a copy of an object, array, or function can be useful when you want to modify the data without affecting the original. There are several ways to create a copy of an object in JavaScript.

One way to create a shallow copy of an object is to use the object spread syntax, which was introduced in ECMAScript 2018. The syntax is simple and looks like this:

```javascript
const originalObj = { name: "John", age: 30 };
const copyObj = { ...originalObj };
```

In this example, `copyObj` is a new object with the same properties as `originalObj`. However, modifying `copyObj` will not affect `originalObj`.

For arrays, the `slice()` method can be used to create a shallow copy of an array. Here's an example:

```javascript
const originalArr = [1, 2, 3, 4];
const copyArr = originalArr.slice();
```

In this example, `copyArr` is a new array with the same values as `originalArr`.

When it comes to creating a copy of a function, things get a bit more complicated. One approach is to create a new function that simply calls the original function with the same arguments. Here's an example:

```javascript
function originalFunc(arg1, arg2) {
    // function body here
}
const copyFunc = function(...args) {
    return originalFunc.apply(this, args);
};
```

In this example, `copyFunc` is a new function that calls `originalFunc` with the same arguments. But keep in mind that this only creates a shallow copy of the function. Any functions or objects used within `originalFunc` will still reference the original values.

As you can see, creating copies of objects, arrays, and functions can be a useful technique in JavaScript programming. Using the appropriate method for the data type you're working with will help ensure that your code behaves as expected and is more maintainable in the long run.

## Shallow vs Deep Copies

In JavaScript, there are two ways to copy objects and arrays: shallow copy and deep copy. Understanding the difference between these two types of copies is important, as it can affect the behavior of your code.

A shallow copy creates a new object or array, but it only copies the references to the properties of the original object or array.

In other words, the new object or array has the same values for its properties as the original, but the properties themselves still reference the same values in memory. This means that any changes made to the properties of the new object or array will also affect the original object or array, and vice versa.

Here's an example of a shallow copy of an array:

```javascript
const originalArr = [1, 2, 3, [4, 5]];
const shallowCopyArr = [...originalArr];

shallowCopyArr[0] = 10;
shallowCopyArr[3][0] = 40;

console.log(originalArr); // [1, 2, 3, [40, 5]]
console.log(shallowCopyArr); // [10, 2, 3, [40, 5]]
```

In this example, the spread operator is used to create a shallow copy of `originalArr`. Then, the first element of `shallowCopyArr` is changed to `10`, which does not affect `originalArr`. But when the first element of the nested array in `shallowCopyArr` is changed to `40`, it also changes in `originalArr`, because both arrays share a reference to the same nested array.

A deep copy, on the other hand, creates a new object or array. It also copies the values of the properties of the original object or array, rather than just the references. This means that any changes made to the new object or array will not affect the original object or array, and vice versa.

Here's an example of a deep copy of an array:

```javascript
const originalArr = [1, 2, 3, [4, 5]];
const deepCopyArr = JSON.parse(JSON.stringify(originalArr));

deepCopyArr[0] = 10;
deepCopyArr[3][0] = 40;

console.log(originalArr); // [1, 2, 3, [4, 5]]
console.log(deepCopyArr); // [10, 2, 3, [40, 5]]
```

In this example, `JSON.stringify()` is used to convert `originalArr` to a string, and then `JSON.parse()` is used to convert the string back into an array. This creates a new array with the same values as `originalArr`, but the new array is completely independent from the original array.

In conclusion, the main difference between a shallow copy and deep copy in JavaScript is whether the new object or array only copies the references to the properties of the original object or array, or whether it also copies the values of the properties.

When copying complex data types like objects and arrays, it's important to use the appropriate type of copy depending on your use case.

# Wrapping Up

In summary, understanding the difference between values and references in JavaScript is essential for writing efficient and bug-free code. By being aware of how data is stored and manipulated, you can avoid unexpected behavior and improve the performance of your applications.

Remember that primitive types are passed by value, while objects and arrays are passed by reference. Keep this in mind when working with functions and assigning variables.

Finally, it's worth noting that ECMAScript 6 introduced a new keyword called `let` which behaves more like traditional programming languages in regards to variable assignment. `let` allows you to declare a block-scoped variable, meaning that it is only accessible within the block of code it is declared in. This can help prevent confusion with referencing and values as the scope of the variable is limited.

In conclusion, while values and references may seem like a small detail in the grand scheme of JavaScript programming, they can have a significant impact on your code's behavior and efficiency. By understanding the differences and using the appropriate techniques for your particular situation, you can write cleaner, more effective, and less error-prone code.

As always, I hope you enjoyed the article and learned something new.

If you want, you can also follow me on [LinkedIn](https://www.linkedin.com/in/germancocca/) or [Twitter](https://twitter.com/CoccaGerman). See you in the next one!

![Image](https://www.freecodecamp.org/news/content/images/2023/04/monsters-inc-sully.gif align="left")
