---
title: JavaScript String to Date – Date Parsing in JS
subtitle: ''
author: Eamonn Cottrell
co_authors: []
series: null
date: '2022-06-29T15:46:32.000Z'
originalURL: https://freecodecamp.org/news/javascript-string-to-date-date-parsing-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/Javascript-String-to-Date-01-1.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'Dates are a pretty fundamental concept. We use them all the time. And computers
  use them all the time. But parsing dates using JavaScript can be a little...well,
  interesting.

  In this article, we''ll:


  Discuss date formatting

  Turn a wee ol'' string into...'
---

Dates are a pretty fundamental concept. We use them all the time. And computers use them all the time. But parsing dates using JavaScript can be a little...well, interesting.

In this article, we'll:

1. Discuss date formatting
2. Turn a wee ol' string into a proper date object using JavaScript.
3. Parse a date object into a number
4. Show an alternative way to use arguments instead of strings to create a date object.

Dates are tricky, but they're also incredibly helpful to use. And once you spend a little time going over the basics, your confidence will grow.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/date.gif)

## What is the Date Format in JavaScript?

ISO 8601, of course! This is the name of the international standard for communicating date and time data. We need to be using this format when dealing with dates in JavaScript

Here's what this format looks like. You're familiar with it already – it just combines a date and time into one big piece of info that JavaScript can get cozy with.

```javascript
// YYYY-MM-DDTHH:mm:ss.sssZ
// A date string in ISO 8601 Date Format
```

## How to Use the `new Date()` Constructor in JavaScript

`new Date()` is the constructor to create a new date in JavaScript. Shocker! 😂 

![Image](https://www.freecodecamp.org/news/content/images/2022/06/shocker.gif)

If you don't pass anything into the new date constructor, it will give you a date object of whatever the **current date and time** is.

```javascript
new Date()

// Thu Jun 23 2022 20:35:51 GMT-0400 (Eastern Daylight Time)
```

Note that a date object can, and often should, contain a time down to the millisecond in addition to the month, day, and year. 

### How to Create a New Date With a String

You may pass a date string into `new Date()` to create a date object.

You don't have to specify a time when creating a date object.

`new Date('2022-06-13')` is perfectly valid. However, when you console log this new date, you'll see that a time will be automatically assigned even though we didn't declare one. 

```javascript
let aDate = new Date('2022-06-13')

// Sun Jun 12 2022 20:00:00 GMT-0400 (Eastern Daylight Time)
```

This can create schisms in the matrix, and it is best to include a full date. For instance, since the local system time is used to interpret the date, depending upon where in the world your computer is, you could get different results from the same non-specific date.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/glitch.gif)

So, when passing a string into `new Date()`, use a full date with hours:minutes.milliseconds.

A capital **T** separates the day component from the time component as shown below:

```javascript
new Date('2022-05-14T07:06:05.123')

// Sat May 14 2022 07:06:05 GMT-0400 (Eastern Daylight Time)
```

### How to Create a New Date With a Number

You can also pass a number into a `new Date()` constructor. More on what the numbers represent below – but `new Date(1656033105000)`, for instance, will return a legitimate date: 

```javascript
console.log(Date(1656033105000))

// Thu Jun 2022 21:12:06 GMT-0400 (Eastern Daylight Time)
```

### How to Create a New Date With Arguments

More on this below too...You many pass up to seven arguments into `new Date()` as well, creating a simpler way to represent a date and time to the Date constructor. 

```javascript
new Date(2022,03,14,07,33,245)

// Thu Apr 14 2022 07:37:05 GMT-0400 (Eastern Daylight Time)
```

## What is Date.parse()?

So, an interesting thing happens if you were to use the parse method on a date object. It spits out a huge number. 

`Date.parse()` tells us the number of milliseconds that have elapsed since January 1, 1970. This is helpful when comparing multiple dates. It's easier to compare and measure differences in dates when they are converted to numbers rather than strings.

```javascript
let anotherDate = new Date(2012,07,12,12,00,234)

Date.parse(anotherDate)

// 1344787434000
```

## Which is Better – Dates Made With Arguments or Strings?

When dating, learn to argue well for long term success. When using dates in JavaScript, use arguments over strings for long term success.

`new Date(2022, 00, 12, 8, 01, 33, 456)`

This can be a bit easier than creating a date using a string. The arguments are simply entered in descending order starting with the year, and ending with the milliseconds.

Only tricky part here: the month is zero indexed. So, January is 00. 

```javascript
new Date(2022,00,12,8,01,33,456)

// Wed Jan 12 2022 08:01:33 GMT-0500 (Eastern Standard Time)
```

## How to Go Deeper With Javascript Dates

This only scratches the surface of the Date object. Check out [MDN for a deep dive](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date). As with all things, there is a treasure trove of information there.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/deep.gif)

You've got the basics now, though. Go put it into practice. You now know how to create a date object in JavaScript with `new Date()`. You can grab the current date and time by not passing anything into the constructor, or you can pass in a string, a number or arguments.

## Thanks for Reading

Thanks for reading! I write about design and development here: [https://blog.eamonncottrell.com/](https://blog.eamonncottrell.com/)

And you can find me on [Twitter](https://twitter.com/EamonnCottrell) and [LinkedIn](https://www.linkedin.com/in/eamonncottrell/).

Have a great one!

![Image](https://www.freecodecamp.org/news/content/images/2022/06/thank-you.gif)

