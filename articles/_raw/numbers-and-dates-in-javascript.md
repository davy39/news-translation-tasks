---
title: How to Work with Numbers and Dates in JavaScript
subtitle: ''
author: Kedar Makode
co_authors: []
series: null
date: '2022-09-16T15:42:30.000Z'
originalURL: https://freecodecamp.org/news/numbers-and-dates-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/Frame-388--1-.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'Numbers, dates, and timers are important parts of JavaScript. And you''ll
  need to know how to work with them when writing your code.

  We often ignore these topics as many articles don''t discuss them. So here, we''ll
  dive deep into the techniques you can...'
---

Numbers, dates, and timers are important parts of JavaScript. And you'll need to know how to work with them when writing your code.

We often ignore these topics as many articles don't discuss them. So here, we'll dive deep into the techniques you can use and learn some interesting things you can use in your next project.

## How to Work with Numbers in JS

A number is a primitive **wrapper object** used to convert the data type to a number. First, we will see how to convert a string to number using the `Number` wrapper object.

```js
let str = "23";
console.log(typeof str); // string

let num = Number(str);
console.log(typeof num); // number
```

The above example shows how you can convert a string to a number.

There is another way you can do this using type coercion. We just have to add the `+` symbol before the string which will convert the string to a number.

```js
let str = "23";
console.log(typeof str); // string

// reassigning str variable
str = +"23";
console.log(typeof str);  // number
```

So from above example we can see that there are two methods to convert a string to number. But we usually prefer the `Number()` method as it is clearer what we are doing and it's also more precise.

### How to Use parseInt() and parseFloat()

We have a function `parseInt()` that can parse only integer parts from the string. But the string should start with an integer. We can only parse the first occurrence of an integer in a string. Let's try to understand with an example.

**We can use parsing in 2 different ways:**

* Number.parseInt()
    
* parseInt()
    

The first method is better because it is more precise.

```js
let padding = "22px";
console.log(Number.parseInt(padding)); // 22

let margin = "16px 12px";
console.log(Number.parseInt(margin)); // 16

let body = "container 12px";
console.log(Number.parseInt(body)); // NaN
```

From the above example, you can see that you can only parse the first occurrence of an integer in a string and the string should start with a number.

You can also parse floating numbers with the same rules with `parseFloat()`.

```js
let padding = "2.5rem";
console.log(Number.parseFloat(padding)); // 2.5

let margin = "1.5rem 2.5rem";
console.log(Number.parseFloat(margin)); // 1.5

let body = "container 1rem";
console.log(Number.parseFloat(body)); // NaN
```

This is how you extract integers or floating numbers from a string. So where can we use it? If you are familiar with HTML and CSS, you can use parseInt() to extract text-size mentioned in HTML/CSS with the help of JavaScript. After extracting that info, you can manipulate the text and change size of an element in terms of padding, margin, and so on.

### How to Use the `Math` Object

Math is an in-built object which has different methods and functions to help you perform mathematical calculations.

Just keep in mind that Math works with the Number type only.

There are many methods and functions in Math. But we will see only a few of them in this tutorial. To explore more you can visit [the docs here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math).

```js
let num = 16;
console.log(Math.sqrt(num)); 
// Gives the square root of a number.

let arr = ['1',4,7,20,32,35,41,'45'];
console.log(Math.max(...arr)); // 45
// ...arr is destructuring the array in place.
// max uses type coercion to convert a string to a number 
// and givse back the maximum number in an array.

console.log(Math.min(...arr)); // 1
// min gives back the min integer in an array
```

There are 4 math methods that can be very confusing for beginners. But here we will simplify them as much as possible to gain a good understanding.

Those 4 method are:

* `trunc()`
    
* `floor()`
    
* `round()`
    
* `ceil()`
    

#### Math.trunc()

This method only removes the decimal part of an integer. It doesn't matter how long the decimal part is.

```js
let height = 23.4;
let width = 23.6;

console.log(Math.trunc(height)); // 23
console.log(Math.trunc(width)); // 23
```

#### Math.floor()

When we use the floor method on a floating number it rounds down to the nearest whole number.

```js
let height = 23.4;
let width = 23.6;

console.log(Math.floor(height)); // 23
console.log(Math.floor(width)); // 23
```

#### Math.round()

Math.round() rounds off to nearest integer of a floating point number. If the floating point (the number after the decimal) is below 5, it rounds down. If the floating point is above 5, it rounds up. You can see how that works here:

```js
let height = 23.4;
let width = 23.6;

console.log(Math.round(height)); // 23
console.log(Math.round(width)); // 24
```

#### Math.ceil()

Math.ceil() rounds up to next integer of the floating point. It is totally opposite to Math.floor().

```js
let height = 23.4;
let width = 23.6;

console.log(Math.ceil(height)); // 24
console.log(Math.ceil(width)); // 24
```

When we perform operations on floating points in JavaScript we often run into the problem of decimal precision. Let's check out the below example:

```js
let operation = 0.1 / 0.3;
console.log(operation); // 0.33333333333333337
```

We got a lot of recurring decimals here. We can have control over these recurring decimal and specify how many decimals we want using the `toFixed()` method.

```js
let operation = 0.1 / 0.3;
console.log(operation); // 0.33333333333333337
console.log(operation.toFixed(1)); // 0.3
console.log(operation.toFixed(2)); // 0.33
```

## How to Work with Dates in JS

A date is an object in JavaScript. We can calculate a date with the help of the constructor `new Date()`. Now a date object contains a number which is in milliseconds (we count the milliseconds from 1st Jan 1970).

```js
let now = new Date();
console.log(now); // current date

console.log(new Date() / 1000); // milliseconds from 1st Jan 1970
```

There are mainly four ways to create a date:

```js
// 1
let now = new Date();
console.log(now);

// 2
now = new Date("Aug 31 2022 11:45:45");
console.log(now);

// 3
now = new Date("Nov 14 2022");
console.log(now);

// 4
let birth = "01-05-1998";
console.log(new Date(birth)); // 05 Jan 1998
```

* You'll want to use the first method when you're working with the current date and want to dynamically change dates and time in your application.
    
* You can use the second method when you want to work with dates provided by the user or stored past dates.
    
* The third method is a simple alternative to the second method and is a bit simpler.
    
* If you want to convert a string into date/time format, you can go with the fourth method.
    

You can use any of these methods. Because if we want to extract any information regarding that date you have pre-defined method to use which you cannot use with strings.

When we create a new Date(), there are 7 numbers which are year, month, day, hour, minute, second, and millisecond in that order.

There are many methods that we can use to get different information.

* `getFullYear()`
    
* `getMonth()`
    
* `getDate()`
    
* `getDay()`
    
* `getHours()`
    
* `getMinutes()`
    
* `getSeconds()`
    
* `getTime()`
    

```js
let now = new Date();

console.log(now.getFullYear()); // gives full year.
console.log(now.getMonth()); // gives number of month starting from 0.
console.log(now.getDate()); // gives date.
console.log(now.getDay()); //  gives day with Monday as 0 and so on.
console.log(now.getHours()); // gives hours in 24 hour format.
console.log(now.getMinutes()); //  gives minutes
console.log(now.getSeconds()); // gives seconds
console.log(now.getTime()); // gives time passed from 1 Jan 1970 till now in milliseconds
```

### How to Perform Operations on Dates

We can perform different operations on dates. If there are two dates and we want to find the difference between those dates we can perform subtraction. But when we get the result we get it in the form of a timestamp which we have to convert into days.

```js
let present = new Date('Aug 31 2020');
let past = new Date('Aug 31 1990');
let days  = present - past;
console.log(days); //  time stamp
console.log(Math.abs(new Date(days)/(1000*60*60*24))); // No of days
```

If you want more precise calculation for dates you can use [**moment.js**](https://momentjs.com/) – but it may not be necessary for simple projects and apps.

## Wrapping Up

I hope you now understand how numbers and dates work in JavaScript. Thank you for reading!

You can follow me on:

* [LinkedIn](https://www.linkedin.com/in/kedar-makode-9833321ab/)
    
* [Twitter](https://twitter.com/Kedar__98)
    
* [Instagram](https://www.instagram.com/kedar_98/)
