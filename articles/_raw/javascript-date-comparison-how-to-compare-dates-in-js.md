---
title: JavaScript Date Comparison – How to Compare Dates in JS
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-06-29T19:06:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-date-comparison-how-to-compare-dates-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/cover-template--6-.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'A date is one of the most common datatypes developers use when creating
  real-world applications.

  But often, devs struggle with this datatype and end up using date libraries like
  Moment.js for simple tasks that aren''t worth the large package size that...'
---

A date is one of the most common datatypes developers use when creating real-world applications.

But often, devs struggle with this datatype and end up using date libraries like Moment.js for simple tasks that aren't worth the large package size that comes with installing an entire package.

In this article, we will learn how to perform date comparisons in JavaScript. If you need the code quickly, here it is:

```bash
const compareDates = (d1, d2) => {
  let date1 = new Date(d1).getTime();
  let date2 = new Date(d2).getTime();

  if (date1 < date2) {
    console.log(`${d1} is less than ${d2}`);
  } else if (date1 > date2) {
    console.log(`${d1} is greater than ${d2}`);
  } else {
    console.log(`Both dates are equal`);
  }
};

compareDates("06/21/2022", "07/28/2021");
compareDates("01/01/2001", "01/01/2001");
compareDates("11/01/2021", "02/01/2022");
```

This will return:

```bash
"06/21/2022 is greater than 07/28/2021"
"Both dates are equal"
"11/01/2021 is less than 02/01/2022"
```

When we think of date comparison in JavaScript, we think of using the Date object (`Date()`) and, of course, it works.

The date object allows us to perform comparisons using the `>`, `<`, `=`, or `>=` comparison operators, but not the equality comparison operators like `==`, `!=`, `===`, and `!==` (unless we attach date methods to the date Object).

Let's begin by learning how to perform comparisons using only the date object, and then we'll see how to perform equality comparisons using the date object alongside date methods.

## How to Perform Date Comparison With the Date Object in JavaScript

Suppose we want to compare two dates in JavaScript. We can easily use the Date Object (`Date()`) this way:

```js
let date1 = new Date();
let date2 = new Date();

if (date1 > date2) {
  console.log("Date 1 is greater than Date 2");
} else if (date1 < date2) {
  console.log("Date 1 is less than Date 2");
} else {
  console.log("Both Dates are same");
}
```

The above will return that both dates are the same because we didn’t pass different dates:

```bash
"Both Dates are same"
```

Let’s now pass in different date values:

```js
let date1 = new Date();
let date2 = new Date("6/01/2022");

if (date1 > date2) {
  console.log("Date 1 is greater than Date 2");
} else if (date1 < date2) {
  console.log("Date 1 is less than Date 2");
} else {
  console.log("Both Dates are same");
}
```

This will now return the following:

```bash
"Date 1 is greater than Date 2"
```

Fortunately, the above handles equality as the last option when the first two conditions fail. But suppose we try to handle equality as the condition this way:

```js
let date1 = new Date();
let date2 = new Date();

if (date1 === date2) {
  console.log("Both Dates are same");
} else {
  console.log("Not the same");
}
```

It will return the following, which is wrong:

```bash
"Not the same"
```

## How to Perform Equality Comparison With JavaScript

To handle equality comparison, we use the date object alongside the `getTime()` date method which returns the number of milliseconds. But if we want to compare specific information like day, month, and so on, we can use other date methods like the `getDate()`, `getHours()`, `getDay()`, `getMonth()` and `getYear()`.

```bash
let date1 = new Date();
let date2 = new Date();

if (date1.getTime() === date2.getTime()) {
  console.log("Both  are equal");
} else {
  console.log("Not equal");
}
```

This will return:

```bash
"Both are equal"
```

We can pass in different dates into the date object so as to compare:

```js
let date1 = new Date("12/01/2021");
let date2 = new Date("09/06/2022");

if (date1.getTime() === date2.getTime()) {
  console.log("Both  are equal");
} else {
  console.log("Not equal");
}
```

As expected this will return:

```bash
"Not equal"
```

Note: With the `getTime()` method we can perform all forms of date comparison using all comparison operators, which are `>`, `<`, `<=`, `>=`, `==`, `!=`, `===`, and `!==`.

## How to Perform Specific Date Comparisons

Suppose we want to compare specific date values like the year. Then we can use the `.getYear()` date method this way:

```js
let date1 = new Date("06/21/2022").getYear();
let date2 = new Date("07/28/2021").getYear();

if (date1 < date2) {
  console.log("Date1 is less than Date2 in terms of year");
} else if (date1 > date2) {
  console.log("Date1 is greater than Date2 in terms of year");
} else {
  console.log(`Both years are equal`);
}
```

## Conclusion

In this article, you have learned how to do date comparisons in JavaScript using the date Object without having to install any library.

Happy Coding!

Embark on a journey of learning! [Browse 200+ expert articles on web development](https://joelolawanle.com/contents). Check out [my blog](https://joelolawanle.com/posts) for more captivating content from me.
