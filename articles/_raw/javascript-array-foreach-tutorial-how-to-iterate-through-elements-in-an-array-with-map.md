---
title: JavaScript Array.forEach() Tutorial – How to Iterate Through Elements in an
  Array
subtitle: ''
author: Kingsley Ubah
co_authors: []
series: null
date: '2021-08-24T17:16:41.000Z'
originalURL: https://freecodecamp.org/news/javascript-array-foreach-tutorial-how-to-iterate-through-elements-in-an-array-with-map
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/forEachtwo.png
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'In JavaScript, you''ll often need to iterate through an array collection
  and execute a callback method for each iteration. And there''s a helpful method
  JS devs typically use to do this: the forEach() method.

  The forEach() method calls a specified call...'
---

In JavaScript, you'll often need to iterate through an array collection and execute a callback method for each iteration. And there's a helpful method JS devs typically use to do this: the `forEach()` method.

The `forEach()` method calls a specified callback function once for every element it iterates over inside an array. Just like other array iterators such as `map` and `filter`, the callback function can take in three parameters:

* The current element: This is the item in the array which is currently being iterated over.
    
* Its index: This is the index position of that item within the array
    
* The target array: This is the array which is being iterated over
    

The `forEach` method does not return a new array like other iterators such as `filter`, `map` and `sort`. Instead, the method returns `undefined` itself. So it's not chainable like those other methods are.

Another thing about `forEach` is that you cannot terminate the loop (with the break statement) or make it skip one iteration (with the continue statement). In other words, you can’t control it.

The only way to terminate a `forEach` loop is by throwing an exception inside the callback function. Don’t worry, we will see all of this in practise soon.

## How to Use the `forEach()` Method in JavaScript

Imagine that a group of students lined up for a routine roll call. The class coordinator moves through the line and calls out the name of each student while marking whether they're present or absent.

It is important to note that the coordinator doesn't change the students' order in the line. He also keeps them in the same line after he is finished with the roll call. All he does is perform an action (his inspection) on each of them.

In the following examples, keeping this scenario in mind, we'll see how you can use the `forEach` method in JavaScript to solve real world problems.

## `forEach()` Method Examples in JavaScript

### How to Remove the First Odd Number in an Array with `forEach()`

In this example, we have an array which has one odd number at the first spot and several even numbers following it. But we only want the numbers in this array to be even. So we are going to remove the odd number from the array using the `forEach()` loop:

```js
let numbers = [3, 6, 8, 10, 12]
let odd = 3;

numbers.forEach(function(number) {
    if (number === odd) {
        numbers.shift() // 3 will be deleted from array
    }
})

console.log(numbers);

[6, 8, 10, 12] // All even!
```

### How to Access the Index Property with `forEach()`

In this example, we are going to execute a `rollCall` function for each student looped over inside of the array. The `rollcall` function simply logs a string pertaining to each of the students to the console.

```js
names = ["anna", "beth", "chris", "daniel", "ethan"]

function rollCall(name, index) {
    console.log(`Is the number ${index + 1} student - ${name} present? Yes!`)
    ;}

names.forEach((name, index) => rollCall(name, index));


/*
"Is the number 1 student - anna present? Yes!"
"Is the number 2 student - beth present? Yes!"
"Is the number 3 student - chris present? Yes!"
"Is the number 4 student - daniel present? Yes!"
"Is the number 5 student - ethan present? Yes!"
*/
```

In this example, the only information we had about each student was their name. However, we also want to know what pronouns each student uses. In other words, we want a pronoun property defined for each student.

So we define each student as an object with two properties, name and pronoun:

```js
names = [
    {name:"anna",pronoun: "she"},
    {name: "beth",pronoun: "they"},
    {name: "chris",pronoun: "he"},
    {name: "daniel",pronoun: "he"},
    {name: "ethan",pronoun: "he"}
]

function rollCall(student, index) {
    console.log(`The number ${index + 1} student is ${student.name}. Is ${student.pronoun} present? Yes!`);
}

names.forEach((name, index) => rollCall(name, index));

/*
"The number 1 student is anna. Is she present? Yes!"
"The number 2 student is beth. Is they present? Yes!"
"The number 3 student is chris. Is he present? Yes!"
"The number 4 student is daniel. Is he present? Yes!"
"The number 5 student is ethan. Is he present? Yes!"
*/
```

We're logging the roll call message of each student to the console, then we perform a check to see what pronoun the student uses, and finally we dynamically pass the accurate pronoun as part of the string.

### How to Copy an Array into a New Array with `forEach()` in JavaScript

After three years of studying, it is now time for each of the students to graduate. In our JavaScript, we define two arrays: `stillStudent` and `nowGraduated`. As you probably guessed, `stillStudent` holds the students right before their graduation.

Then the `forEach` loop takes in each of the students and calls the `graduateStudent` function on it.

In this function we construct an object with two properties: the name of the student as well as the position at which they graduated. Then we pass the new object to the `nowGraduated` array. At that point, the student has become a graduate.

This example also demonstrates how you can use the `forEach()` method to copy an array into a new array.

```js
let stillStudent = ["anna", "beth", "chris", "daniel", "ethan"]
let nowGraduated = []

function graduateStudent(student, index) {
    let object = { name: student, position: index + 1}
    nowGraduated[index] = object
}

stillStudent.forEach((name, index) => graduateStudent(name, index));

console.log(nowGraduated);

/*
[
    { name: "anna", position: 1}, 
    { name: "beth", position: 2}, 
    { name: "chris", position: 3}, 
    { name: "daniel", position: 4}, 
    { name: "ethan", position: 5}]
]
*/
```

### How to Check for the Next Item in an Array with the `array` Parameter

At some point, the teacher will need to check if the list has a particular item next on the list. In such a case, the teacher will need to have a broad view of the whole list. That way, he can tell if there is a next student to call for.

In our JavaScript, we can replicate this because the callback function can also access the `array` (the third) parameter. This parameter represents the target array, which is `name`.

We check if there is a next item (student) on the array. If there is, we pass the string `positive` to the `nextItem` variable. If there is none, we pass the string `negative` to the variable. Then for every iteration, we check if **that** student is indeed the last.

```js
names = ["anna", "beth", "chris", "daniel", "ethan"]

function rollCall(name, index, array) {
    let nextItem = index + 1 < array.length ? "postive" : "negative"
    console.log(`Is the number ${index + 1} student - ${name} present? Yes!. Is there a next student? ${nextItem}!`);
}

names.forEach((name, index, array) => rollCall(name, index, array))

/*
"Is the number 1 student - anna present? Yes!. Is there a next student? postive!"
"Is the number 2 student - beth present? Yes!. Is there a next student? postive!"
"Is the number 3 student - chris present? Yes!. Is there a next student? postive!"
"Is the number 4 student - daniel present? Yes!. Is there a next student? postive!"
"Is the number 5 student - ethan present? Yes!. Is there a next student? negative!"
*/
```

## You can't exit a `forEach` Loop, So Use `every()` Instead

Remember when I mentioned that, by nature, you can't break out of (aka exit) a `forEach` loop? Once it's started, it will run until it reaches the last item in the array. So if you insert a `break` statement, it will return a `SyntaxError`:

```js
let numbers = [2, 4, 5, 8, 12]
let odd = 5;

numbers.forEach(function(number) {
    if (number === odd) {
        break; // oops, this isn't gonna work!
    }
})
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/illegal.png align="left")

Normally you would want to break out of a loop if you end up achieving what you intend to before reaching the last item. In our example above, we already found the odd number (5), so there was then no need to keep iterating over the remaining items (8 and 12).

If you want to break out of the loop on some condition, then you will have to use any of the following methods:

* `for` loop
    
* [`for…of` or `for…in` loop](https://futurestud.io/tutorials/node-js-for-of-vs-for-in-loops)
    
* `Array.some()`
    
* `Array.every()`
    
* `Array.find()`
    

Here is how you can break out of a loop with `Array.every()`:

```js
let numbers = [2, 4, 5, 8, 12]
let odd = 5;

numbers.every(number => {
  if (number == odd) {
    return false;
  }

  console.log(number);
  
  return true;
});

// 2 4
```

## Wrapping Up

In this tutorial, I have introduced the `forEach` method, illustrated how it works with a simple analogy, and I've also given you some practical examples of its usage in JavaScript code.

Hopefully you got something useful from this piece.

**If you want to learn more about Web Development, feel free to visit my** [Blog](https://ubahthebuilder.tech)**.**

Thank you for reading and see you soon.

> **P/S**: If you are learning JavaScript, I created an eBook which teaches 50 topics in JavaScript with hand-drawn digital notes. [Check it out here](https://ubahthebuilder.gumroad.com/l/js-50).
