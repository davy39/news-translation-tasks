---
title: JavaScript Array Length – How to Find the Length of an Array in JS
subtitle: ''
author: Tantoluwa Heritage Alabi NB
co_authors: []
series: null
date: '2024-02-01T15:56:36.000Z'
originalURL: https://freecodecamp.org/news/javascript-array-length-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/pexels-venelin-dimitrov-3476312.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'JavaScript arrays are fundamental data structures that allow you to store
  and manipulate collections of elements efficiently.

  While working with arrays, you''ll often need to know their length. The length of
  an array tells us how many elements are pre...'
---

JavaScript arrays are fundamental data structures that allow you to store and manipulate collections of elements efficiently.

While working with arrays, you'll often need to know their length. The length of an array tells us how many elements are present in the array. You can use this to check if an array is empty and, if not, iterate through the elements in it.

## How to Find the Length of an Array

### Using the `<.length>` property

Javascript has a `<.length>` property that returns the size of an array as a number(integer).

Here's an example of how to use it:

```python
let numbers = [12,13,14,25]
let numberSize = numbers.length
console.log(numberSize)
# Output
# 4
```

In the above code, a variable with the name `numbers` stores an array of numbers, while the variable `numberSize` stores the number of elements present in the array by using the method `.length`. The number size is then printed using console.log – hence the output 4.

Let's now check to see what the data type of the `length` property is:

```python
let numbers = [12,13,14,25]
let numberSize = numbers.length
console.log(typeof numberSize)
# Output
# number
```

In the above code we see that the output is `number`.

Here's an example of how to access an array element with the `length` property in a for loop:

```python
let numbers = [12,13,14,25]
for (i = 0; i < numbers.length; i++){
   console.log(numbers[i]);
}
# Output
# 12
# 13
# 14
# 25
```

### Without Using the `.length()` method

In this method, we will iterate through the elements and count each of the elements present in the array.

Here's how it works:

```python
function arrayLength(arr) {
   let count = 0;
   for (const element of arr) {
     count++;
   }

   return count; 
}
let numbers = [12,13,14,25]
console.log("Length of array:", arrayLength(numbers));
# Output
# Length of array: 4
```

In the above code, there's a function named `arrayLength` that accepts the array as input. We created a variable called `count` that is assigned 0. The `count` variable will store the count of the number of elements in the array.

To count the elements in the array, we used a [for-of loop](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of) to check each element in the array.

The code iterates over each element in the array until undefined is encountered. That is, we iterate over each element in the array until we reach the end of the array where there are no more elements to check. Finally we return `count` as the output.

We pass in the variable `<numbers>` as the input to the function in order to obtain the length of the array as the returned value.

## Conclusion

The most common and straightforward method is to use the length property of the array. But you can also use a longer method by looping through the array. These methods allow you to work with arrays of different sizes and types.

If you have any questions, you can reach out to me on [Twitter](https://twitter.com/HeritageAlabi1) 💙.
