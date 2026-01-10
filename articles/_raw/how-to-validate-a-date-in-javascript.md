---
title: JS Date Validations – How To Validate a Date in JavaScript (With Examples)
subtitle: ''
author: Nathan Sebhastian
co_authors: []
series: null
date: '2023-08-22T19:08:29.000Z'
originalURL: https://freecodecamp.org/news/how-to-validate-a-date-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/js-date-validations.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'There are times when you need to validate a date input in your JavaScript
  applications.

  This article will show you how to perform the following date validations:


  Check if a string is a valid date

  Validate a string in the DD/MM/YYYY format

  Check if t...'
---

There are times when you need to validate a date input in your JavaScript applications.

This article will show you how to perform the following date validations:

1. Check if a string is a valid date
2. Validate a string in the `DD/MM/YYYY` format
3. Check if the date is in the past or future

Validating a date value helps you prevent users from entering an incorrect date. Let's start with validating the input itself.

## How to Check if a String is a Valid Date with JavaScript

To validate if a string is a valid date input, you need to call the `Date()` constructor and pass the string as its argument.

If the string is a valid date, the constructor returns a `Date` object holding the same value as the string:

```js
let dateInput = "2019/05/15"; // YYYY/MM/DD format

let dateObj = new Date(dateInput);

console.log(dateObj); // 2019-05-15T00:00:00.000Z
```

If you pass an invalid date, the constructor returns an `Invalid Date` object:

```js
let dateInput = "2019/15/15"; // YYYY/MM/DD format

let dateObj = new Date(dateInput);

console.log(dateObj); // Invalid Date
```

Note that the `Date()` constructor requires you to pass a date in the format of `YYYY/MM/DD` or `MM/DD/YYYY`. If you pass a date in `DD/MM/YYYY` format, the contructor also returns an `Invalid Date`.

Now that you have a `Date` object representing the string, you can use the `isNaN()` function to check if the object is valid.

You can create a function to check the validity of the `Date` object as follows:

```js
function isDateValid(dateStr) {
  return !isNaN(new Date(dateStr));
}

// DD/MM/YYYY
console.log(isDateValid("15/05/2019")); // false

// MM/DD/YYYY
console.log(isDateValid("05/15/2019")); // true

// YYYY/MM/DD
console.log(isDateValid("2019/05/15")); // true
```

Here, we reverse the value returned by the `isNaN()` function so that a valid Date returns `true`. You can call the `isDateValid()` function anytime you need to check if a string returns a valid date.

Next, let's see how to handle a date string in `DD/MM/YYYY` format.

## How to Validate a Date and Convert it to DD/MM/YYYY Format

If you want to format the date as a `DD/MM/YYYY` string, you need to use a combination of `getDate()`, `getMonth()`, and `getFullYear()` methods to manually create the date string.

First, you validate the string in the `YYYY/MM/DD` format by passing it to the `Date()` constructor.

Next, you check if the `Date` value is not NaN using an `if` statement:

```js
let dateInput = "2019/05/15"; // YYYY/MM/DD format

let dateObj = new Date(dateInput);

if (!isNaN(dateObj)) {
  // Convert dateObj to DD/MM/YYYY
}
```

When the `Date` isn't a NaN, you can extract the date, month, and year of the object using the `getDate()`, `getMonth()`, and `getFullYear()` methods:

```js
let dateInput = "2019/05/15"; // YYYY/MM/DD format

let dateObj = new Date(dateInput);

if (!isNaN(dateObj)) {
  let day = dateObj.getDate();
  day = day < 10 ? "0" + day : day;
  let month = dateObj.getMonth() + 1;
  month = month < 10 ? "0" + month : month;
  const year = dateObj.getFullYear();

  const resultDate = `${day}/${month}/${year}`;
  console.log(resultDate);  // 15/05/2019
}
```

Here, you can see that the date "2019/05/15" is converted into "15/05/2019". Notice how you need to modify the `day` and `month` variables to add `0` in front of the values if those values are single digits.

The `getMonth()` method returns a number between 0 and 11 that represents the month of the date. You need to increment the returned value by 1 to get the correct date.

## What if I get the Date in DD/MM/YYYY Format?

As I said before, JavaScript doesn't support converting a string in `DD/MM/YYYY` format into a valid `Date` object.

If you have a date string in `DD/MM/YYYY` format, then you need to swap the date and year position before calling the `Date()` constructor. 

You can do so by using the `split()` method to convert the string into an array, then swap the position of date and year at index 0 and 2.

Pass the separator `/` as the argument to the split method as shown below:

```js
let dateInput = "15/05/2019"; // DD/MM/YYYY format

let dateArray = dateInput.split("/");

let newDate = `${dateArray[2]}/${dateArray[1]}/${dateArray[0]}`;

console.log(newDate); // 2019/05/15 (YYYY/MM/DD)
```

The `newDate` variable has the value of `dateInput` but in `YYYY/MM/DD` format. You can pass `newDate` into the `Date()` constructor to see if it's a valid date.

## How to Check if a Date is in the Past or Future

To check if a date is in the past or future, you can use the less than `<` operator to compare the input date with the current date.

When the result is `true`, then the input date is in the past:

```js
// The date you want to check
const inputDate = new Date('2023-08-20'); 

// Get the current date
const currentDate = new Date();

// Compare the input date with the current date
if (inputDate < currentDate) {
  console.log('The input date is in the past.');
} else {
  console.log('The input date is in the future.');
}
```

JavaScript knows how to compare `Date` objects, so you don't need to extract the values and compare them manually.

## Conclusion

Now you've learned how to validate if a string is a valid date, how to convert a date into a `DD/MM/YYYY` format, and how to check if a date is in the past or future.

If you enjoyed this article and want to take your JavaScript skills to the next level, I recommend you check out my new book _Beginning Modern JavaScript_ [here](https://www.amazon.com/dp/B0CQXHMF8G).

[![beginning-js-cover](https://www.freecodecamp.org/news/content/images/2024/01/beginning-js-cover.png)](https://www.amazon.com/dp/B0CQXHMF8G)

The book is designed to be easy to understand and accessible to anyone looking to learn JavaScript. It provides a step-by-step gentle guide that will help you understand how to use JavaScript to create a dynamic application.

Here's my promise: _You will actually feel like you understand what you're doing with JavaScript._

Until next time!

