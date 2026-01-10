---
title: How to Format Dates with Ordinal Number Suffixes (-st, -nd, -rd, -th) in JavaScript
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2023-01-03T21:57:47.000Z'
originalURL: https://freecodecamp.org/news/format-dates-with-ordinal-number-suffixes-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/cover-template--4-.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'Many online resources teach you how to format dates. But it''s hard to
  find any that explain how to format dates with an ordinal number suffix (like 1st)
  in JavaScript – without using a library.

  In this short article, you will learn how to format date...'
---

Many online resources teach you how to format dates. But it's hard to find any that explain how to format dates with an ordinal number suffix (like 1**st**) in JavaScript – without using a library.

In this short article, you will learn how to format dates in JavaScript with ordinal numbers. Ordinal numbers all use a suffix. The suffixes are “-st” (like for 1st), “-nd” (like for 2nd), “-rd” (like for 3rd), or “-th” (like for 4th). They are used for dates and when you need to order something. Instead of 15, you would have 15th, for example.

For dates, it is also a user-friendly way to represent a date on the web page, and you may be asked to format your date with ordinal numbers, such as May 15th, 2022, instead of May 15, 2022.

## How to Format Dates in JavaScript

There are many ways to format your dates in JavaScript. But for this, you need the day, month, and year assigned to different variables so you can bring them together in your desired arrangement:

```js
const dateObj = new Date();
const day = dateObj.getDate();
const month = dateObj.toLocaleString("default", { month: "long" });
const year = dateObj.getFullYear();

const date = `${month} ${day}, ${year}`;
console.log(date); // "December 23, 2022"
```

**Note:** You can learn more about how to format dates in [this article](https://www.freecodecamp.org/news/javascript-date-format-how-to-format-a-date-in-js/) and this [one-line method](https://www.freecodecamp.org/news/how-to-format-dates-in-javascript/).

## How to Format Dates with Ordinal Number Suffixes (-st, -nd, -rd, and -th) in JavaScript

Now you have your date, but you want the day formatted as an ordinal number – meaning 23 should be 23rd, for example.

You can create a function that checks for each number and returns the appropriate suffix.

```js
const nthNumber = (number) => {
  if (number > 3 && number < 21) return "th";
  switch (number % 10) {
    case 1:
      return "st";
    case 2:
      return "nd";
    case 3:
      return "rd";
    default:
      return "th";
  }
};
```

This method checks for each number group and returns the appropriate suffix. For example, from 4 to 20, it'll have the ordinal number suffix of “th”. Then the switch case statements properly check other groups of numbers and return the appropriate ordinal number suffix.

You can now update your date arrangement to add the `nthNumber()` function and pass in the day number:

```js
const date = `${month} ${day}${nthNumber(day)}, ${year}`;
console.log(date); // "December 23rd, 2022"
```

This is what the entire code looks like:

```js
const dateObj = new Date();
const day = dateObj.getDate();
const month = dateObj.toLocaleString("default", { month: "long" });
const year = dateObj.getFullYear();

const nthNumber = (number) => {
  if (number > 3 && number < 21) return "th";
  switch (number % 10) {
    case 1:
      return "st";
    case 2:
      return "nd";
    case 3:
      return "rd";
    default:
      return "th";
  }
};

const date = `${month} ${day}${nthNumber(day)}, ${year}`;
console.log(date); // "December 23rd, 2022"
```

## Wrapping Up

You can write the function in many ways, but all you are doing is checking the number to attach the appropriate ordinal number suffix. Here is another way of writing the method:

```js
const nthNumber = (number) => {
  return number > 0
    ? ["th", "st", "nd", "rd"][
        (number > 3 && number < 21) || number % 10 > 3 ? 0 : number % 10
      ]
    : "";
};
```

Feel free to tweak the function to produce your desired output, and have fun coding!
