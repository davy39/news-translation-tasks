---
title: JavaScript Sort() – How to Use the Sort Function in JS
subtitle: ''
author: Grant Riordan
co_authors: []
series: null
date: '2023-05-16T20:29:44.000Z'
originalURL: https://freecodecamp.org/news/how-does-the-javascript-sort-function-work
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/blog_header2.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'In this article I will explain how to use, and maximize the full potential
  of the sort() function.

  What is the sort() Function?

  The sort() function allows you to sort an array object by either the default sorting
  order, or by a custom sorting functio...'
---

In this article I will explain how to use, and maximize the full potential of the `sort()` function.

## What is the `sort()` Function?

The `sort()` function allows you to sort an array object by either the default sorting order, or by a custom sorting function.

By default, it sorts the elements in the array in ascending order based on their string Unicode values. The function takes the inputs, converts them to strings, and then sorts them using Unicode values.

### What is Unicode? 

Unicode is a standard that provides a unique numeric value (code point) for every character used in writing systems around the world. It allows computers to represent and handle various languages, symbols, and characters consistently.

English Latin Alphabet:

```
U+0041 to U+005A: Latin capital letters (A-Z)
U+0061 to U+007A: Latin small letters (a-z)
```

So for example the Latin Alphabet (English) word "Apple" is represented in Unicode as:

**A:** U+0041 <br>
**p:** U+0070 <br>
**p:** U+0070 <br>
**l:** U+006C <br>
**e:** U+0065 <br>

### How Does `sort()` Use these Unicode Characters?

The sort() function sorts the array by applying a sorting algorithm. This could be the bubble sort, quick sort, heap sort, or mergesort algorithms, for example (there are more, too).

The choice of algorithm may depend on factors such as the size of the array, the data types being sorted, and the engine's optimisation strategies.

**Note:** The term "engine" refers to the JavaScript engine, which is a software component that executes JavaScript code. It is responsible for interpreting and running JavaScript programs. 

JavaScript engines are typically implemented as part of web browsers, server-side JavaScript platforms, or standalone JavaScript runtime environments.

Among the sorting algorithms mentioned, the most commonly used algorithm for sorting arrays in JavaScript is typically either quicksort or a variation of quicksort.

If you'd like to read more about the quicksort algorithm, you can check out the [W3Resource Website here](https://www.w3resource.com/javascript-exercises/searching-and-sorting-algorithm/searching-and-sorting-algorithm-exercise-1.php)

## How to Use the JavaScript `sort()` Function

Ok, so now we have an idea of what `sort()` is doing under the hood. Let's look at how to use the function.

To use the function, simply call `{array}.sort()`. This will implement the default sort action described above.

```javascript
const characters = [
  "Nebula",
  "Thanos",
  "Star Lord",
  "Groot",
  "Rocket",
  "Drax",
  "Gamora",
];

const sortedArray = characters.sort();

// Output:
["Drax", "Gamora", "Groot", "Nebula", "Rocket", "Star Lord", "Thanos"];
```

As you can see, the names of the characters have been sorted by ascending order according to their Unicode representation.

If we wanted to have them in descending alphabetical order, we could chain the `reverse()` function, reversing the items once they've been sorted. 

```javascript
const characters = [
  "Nebula",
  "Thanos",
  "Star Lord",
  "Groot",
  "Rocket",
  "Drax",
  "Gamora",
];

const descending = characters.sort().reverse();
console.log(descending);

// Output:
["Thanos", "Star Lord", "Rocket", "Nebula", "Groot", "Gamora", "Drax"];
```

### What about sorting numbers?

Well, let's try it:

```javascript
const numbers = [9, 3, 12, 11, 40, 28, 5];

const sortedNumbers = numbers.sort();
console.log(sortedNumbers);

// Output:
[11, 12, 28, 3, 40, 5, 9];
```

Wait a minute! That's not sorted in the expected order, is it? Why not? 

Well, remember when I said the default sorting method uses Unicode character sorting, after converting to a string? Well, that's why. The numbers are converted to their string equivalent and then sorted based on Unicode values.

As a result, all the '1' numbers come before everything else, so it will sort '11' before '3' and so on.

Let's look at the Unicode values for these:

11 = U+0031 U+0031 </br>
12 = U+0031 U+0032 </br>
28 = U+0032 U+0038 </br>
3 = U+0033 </br>
40 = U+3034 U+0030</br>
5 = U+3035 </br>
9 = U+3039 </br>

So hopefully you can see that if we sort using the Unicode characters, 0031 < 0033. So each time it compares 1 with 3, the numbers starting with 1 will be pushed to the front of the array.

_"Well thats annoying"_ I hear you say. Don't worry, there's a solution: custom compare functions.

## How to Use a Custom Sort Function

As mentioned above, the `sort()` function can also take an argument of a custom comparison function.

```javascript
sort(compareFn?: ((a: never, b: never) => number) | undefined): never[]

Function used to determine the order of the elements. It is expected to return a negative value if the first argument is less than the second argument, zero if they're equal, and a positive value otherwise. If omitted, the elements are sorted in ascending, ASCII character order.

[11,2,22,1].sort((a, b) => a - b)

Sorts an array in place. This method mutates the array and returns a reference to the same array.
```

So what does this all mean?

The comparison function has some expectations. It expects you to return some specific values:

* **-1**: if the value you're comparing on the left is less than the right. 
* **0**: if the value you're comparing on the left is equal to the right. 
* **1**: if the value you're comparing on the left is greater than the right. 

In its simplest form, it means that -1 moves the item to the left (before comparing value), 0 keeps it where it is, and 1 moves the item to the right (after comparing value)

Now let's look at some examples to see how it works.

Taking the example before, if we're struggling to sort an array of numbers, we can fix this using our custom compare function:

``` javascript
const numberSortFn = (a, b) => {
  if (a < b) {
    return -1;
  } else if (a === b) {
    return 0;
  } else {
    return 1;
  }
};

const numbers = [9, 3, 12, 11, 40, 28, 5];
const sortedNumbers = numbers.sort(numberSortFn);
console.log(sortedNumbers);

//Output
[3, 5, 9, 11, 12, 28, 40];
```

As you can see, this now works as we expected, with the numbers being sorted in numerical ascending order. So why is this different? Because now the less than operator compares the left and right sides as numbers, rather than strings.

## Other Uses of the Custom Comparison Function

### Sorting objects based on property

You can use the custom compare function to sort objects using their properties. Below is an example of sorting an array of objects (books) based on their year of publication.

``` javascript
const books = [
  { title: "Book A", year: 2010 },
  { title: "Book B", year: 2005 },
  { title: "Book C", year: 2018 },
];

const booksSortedByYearAsc = books.sort((a, b) => a.year - b.year);
console.log(booksSortedByYearAsc);

// Output:
[
  { title: "Book B", year: 2005 },
  { title: "Book A", year: 2010 },
  { title: "Book C", year: 2018 },
];
```

We tell the comparison function to specifically compare based on the `.year` property when running the comparison.

### Sorting based on the content of the string

Let's go one step further and say we had a bunch of attendees at a seminar, and we want to list them all out for a register. But we want all the Doctors to be listed at the top, as these are the keynote speakers.

We can do this with a custom comparison function:

``` javascript
const names = ["Mike Smith", "Dr. Johnson", "John Doe", "Dr. Williams"];

names.sort((a, b) => {
  if (a.startsWith("Dr.") && !b.startsWith("Dr.")) {
    return -1;
  } else if (!a.startsWith("Dr.") && b.startsWith("Dr.")) {
    return 1;
  } else {
    return a.localeCompare(b); // sort alphabetically
  }
});

console.log(names);

// Output:
["Dr. Johnson", "Dr. Williams", "John Doe", "Mike Smith"];
```

So above, we're stating that if the string begins with "Dr" and the next value doesn't start with "Dr" then it should go before the right value, and then vice versa for the 2nd if statement.

If neither values for comparison have "Dr" in them, then the function will utilise the `localCompare` function. This essentially reverts back to the default Unicode comparison as discussed earlier in this article.

### Strings of Numbers and Letters

Suppose you want to sort an array that contains both numbers and letters. You want the numbers to appear before the letters, and within each group, you want the elements to be sorted numerically and alphabetically, respectively. Here's how you can achieve that:

```javascript
const items = ["b", "3", "a", "2", "c", "1"];

items.sort((a, b) => {
  const aIsNumber = !isNaN(a); // isNaN = is Not a Number
  const bIsNumber = !isNaN(b);

  if (aIsNumber && !bIsNumber) {
    return -1; // numbers should be sorted before letters
  } else if (!aIsNumber && bIsNumber) {
    return 1; // letters should be sorted after numbers
  } else if (aIsNumber && bIsNumber) {
    return a - b; // sort numbers numerically
  } else {
    return a.localeCompare(b); // sort letters alphabetically
  }
});

console.log(items);

// Output
["1", "2", "3", "a", "b", "c"];
```

First we check if each value is a number by expecting false to be returned from `isNaN`, as `isNaN()` returns if the value is not a number. So by checking if false is returned, we know it **is** in fact a number.

We can then use some smart logic to determine the order of things.

- **a is a number, and b is NOT a number** = we know that the number should come first so we can return -1 
- **a is NOT a number, and b is a number** = we know that the letter should be moved to the right, so 1 is returned.
- **both values are numbers** = we can simply subtract b from a, thus returning a negative, 0, or positive number. This indicates what do with the values in relation to order. 

If none of these are true, we simply order by Unicode values again, as we know that the two values are both strings by process of elimination.

### Sorting in descending order

Earlier we used the `sort().reverse()` function to order the list of characters. We can also use the `sort(compareFn)` function like so:

```javascript
const characters = [
  "Nebula",
  "Thanos",
  "Star Lord",
  "Groot",
  "Rocket",
  "Drax",
  "Gamora",
];

const sortedArray = characters.sort((a, b) => b.localeCompare(a));
console.log(sortedArray);

// Output:
["Thanos", "Star Lord", "Rocket", "Nebula", "Groot", "Gamora", "Drax"];
```

Wait, don't we normally compare `a` to `b`? Yes, if we want ascending order – but in this case because we want descending, we compare `b` to `a`.

### What are the performance hits?

This is something you need to be mindful of when sorting arrays, but it really can depend, for example:

- which JS engine is running the code
- size of the array
- complexity of the custom function

**Time Differences:**

Let's look at an array made of 100 words sorted in ascending order, using both the default `sort()` vs `sort(compareFn)` implementations.

```

sort() => 1.812ms;
sort(compareFn) => 0.14ms
```

However, if we were to sort the same array in descending order, we get the following times:

```

sort().reverse() =>  1.764ms
sort(compareFn) => 7.77ms
```

You can see that the `sort().reverse()` chaining is much faster. This may be because we are performing a simple sorting algorithm which has been optimized by ECMAScript, and then running a basic reversal function to return in descending order. 

In comparison, running a custom function adds a layer of complexity to the process and additional computation.

6ms difference may seem very small (and don't get me wrong it is still extremely fast). But this could grow as the size of the array grows.

As a broad rule, I'd reccomend using the default / built-in `sort()` method when you can, as this has been optimised, leaving custom functions to more complex requirements.

## Conclusion

In this article we've explored:

- What the `sort()` function is
- A below the surface look at how it works
- Common uses of the `sort()` function
- Some more elaborate usages of the `sort()` function to get a better understanding of the many tasks you can carry out with it
- Some considerations when sorting arrays

I hope you have found this article helpful in giving you a better understanding of the JavaScript `sort()` function and how powerful it can be.

Feel free to give me a follow on Twitter at [gWeaths](https://twitter.com/gweaths) should you wish to know when I've posted other articles.



