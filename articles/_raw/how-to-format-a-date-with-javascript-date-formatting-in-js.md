---
title: How to Format a Date with JavaScript – Date Formatting in JS
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2023-05-31T17:48:04.000Z'
originalURL: https://freecodecamp.org/news/how-to-format-a-date-with-javascript-date-formatting-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/cover-template.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'Dates are a fundamental part of many JavaScript applications, whether it''s
  displaying the current date on a webpage or handling user input for scheduling events.

  But displaying dates in a clear and consistent format is crucial for a positive
  user exp...'
---

Dates are a fundamental part of many JavaScript applications, whether it's displaying the current date on a webpage or handling user input for scheduling events.

But displaying dates in a clear and consistent format is crucial for a positive user experience.

In the past, I have written two articles on Date formatting. The first explained solely [how to use the `toLocaleDateString()` method to format dates](https://www.freecodecamp.org/news/how-to-format-dates-in-javascript/), while the second explained [custom date formatting with the `getFullYear()`, `getMonth()`, and `getDate()` methods](https://www.freecodecamp.org/news/javascript-date-format-how-to-format-a-date-in-js/).

In this article, we'll explore various techniques to format dates in JavaScript, enabling you to present dates in your desired format for your application.

## How to Use the JavaScript Date Object

Before we dive into date formatting, let's get familiar with the JavaScript `Date` object. It provides methods to work with dates and times effectively.

To create a new date instance, you can use the `new Date()` constructor.

For example:

```js
const currentDate = new Date();
console.log(currentDate); // Wed May 31 2023 08:26:18 GMT+0100 (West Africa Standard Time)
```

The above code will output the current date and time in the default format. However, this format is not suitable for all use cases.

This is why we need to format dates so we can extract what we need from this date object.

In JavaScript, there is no direct syntax that provides you with your expected format because date format varies based on location, circumstance, and so on.

## Basic JavaScript Date Formatting Methods

JavaScript provides a few built-in methods to format dates conveniently. Let's take a look at some of these methods:

1. **toDateString()**: This method converts the date portion of a `Date` object into a human-readable string format.
    

For example:

```js
const date = new Date();
console.log(date.toDateString());
```

Output: `Wed May 30 2023`

2. **toISOString()**: This method converts a `Date` object into a string representation following the ISO 8601 format.
    

For example:

```js
const date = new Date();
console.log(date.toISOString());
```

Output: `2023-05-30T00:00:00.000Z`

3. **toLocaleDateString()**: This method returns a string representing the date portion of a `Date` object using the system's local conventions.
    

For example:

```js
const date = new Date();
console.log(date.toLocaleDateString());
```

Output: `5/30/2023`. This Format may vary based on the system's locale. For more explanation on how this method works, [read this article](https://www.freecodecamp.org/news/how-to-format-dates-in-javascript/).

## Custom Date Formatting in JavaScript

While the basic formatting methods can be useful in certain scenarios, you might often need more control over the date format.

JavaScript provides a couple ways to achieve custom date formatting:

1. **String Concatenation**: One approach is to manually concatenate the different components of a date using string manipulation.
    

For example:

```js
const date = new Date();
const formattedDate = `${date.getDate()}-${date.getMonth() + 1}-${date.getFullYear()}`;
console.log(formattedDate);
```

Output: `**30-5-2023**`.

You can manipulate this however you like and come up with more creative ways of representing dates. You can read this article to understand custom date formatting in detail and [this article](https://www.freecodecamp.org/news/javascript-date-format-how-to-format-a-date-in-js/) on [how to format dates with ordinal number suffixes (-st, -nd, -rd, -th) in JavaScript](https://www.freecodecamp.org/news/format-dates-with-ordinal-number-suffixes-javascript/).

2. **Intl.DateTimeFormat**: JavaScript's `Intl` object offers powerful formatting capabilities through the `DateTimeFormat` object. It provides localization support and various options to format dates and times.
    

Here's an example:

```js
const date = new Date();
const formatter = new Intl.DateTimeFormat('en-US', { dateStyle: 'short' });
const formattedDate = formatter.format(date);
console.log(formattedDate);
```

Output: `5/30/23`

Using `Intl.DateTimeFormat`, you can specify the desired locale and various options to format dates precisely as needed. There are more options you can use in the [official documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat).

## How to Handle Time Zones When Working with Dates

When working with dates, it's essential to consider time zones, especially when dealing with global applications or time-sensitive information.

JavaScript provides methods to handle time zones effectively:

1. **Time Zone Offset**: The `getTimezoneOffset()` method of the `Date` object returns the difference in minutes between the local time zone and UTC. You can use this offset to adjust dates for specific time zones.
    
2. **Displaying Time Zones**: To display the time zone information alongside the date, you can use the `toLocaleString()` method with the appropriate options.
    

For example:

```js
const date = new Date();
const formattedDate = date.toLocaleString('en-US', { timeZoneName: 'short' });
console.log(formattedDate);
```

Output: `5/30/2023, 12:00:00 AM PDT`.

## Common Date Formatting Patterns

Certain date formatting patterns are commonly used. Here are a few examples:

1. **Specific Date Format**: To display a date in a specific format, such as `DD/MM/YYYY`, you can use `Intl.DateTimeFormat` with the appropriate options.
    

For example:

```js
const date = new Date();
const formatter = new Intl.DateTimeFormat('en-US', { day: '2-digit', month: '2-digit', year: 'numeric' });
const formattedDate = formatter.format(date);
console.log(formattedDate);
```

Output: `30/05/2023`.

2. **Time Format**: To format the time portion of a date, you can use the `hour`, `minute`, and `second` options.
    

For example:

```js
const date = new Date();
const formatter = new Intl.DateTimeFormat('en-US', { hour: '2-digit', minute: '2-digit', second: '2-digit' });
const formattedTime = formatter.format(date);
console.log(formattedTime);
```

Output: `12:00:00 AM`

## How to Handle Date Input

Apart from formatting dates for display, it's essential to handle user input for dates effectively. Here are a few considerations:

1. **Parsing User Input**: Use the `Date.parse()` method or external libraries like Moment.js or Luxon to parse user-provided dates into valid `Date` objects.
    
2. **Validating User Input**: Implement validation mechanisms to ensure the user's input adheres to the expected date format. Regular expressions or external libraries can help with this.
    

## Wrapping Up

Formatting dates in JavaScript is an essential skill when building web applications. By utilizing the built-in date formatting methods, custom formatting techniques, and external libraries, you can ensure dates are presented clearly and accurately.

Experiment with different approaches and stay mindful of time zones for a seamless user experience with date formatting in JavaScript.

For further study on how to format dates, check these resources:

* [JavaScript Date Format – How to Format a Date in JS](https://www.freecodecamp.org/news/javascript-date-format-how-to-format-a-date-in-js/)
    
* [How to Format Dates in JavaScript with One Line of Code](https://www.freecodecamp.org/news/how-to-format-dates-in-javascript/)
    
* [How to Format Dates with Ordinal Number Suffixes (-st, -nd, -rd, -th) in JavaScript](https://www.freecodecamp.org/news/format-dates-with-ordinal-number-suffixes-javascript/)
    

Embark on a journey of learning! [Browse 200+ expert articles on web development](https://joelolawanle.com/contents). Check out [my blog](https://joelolawanle.com/posts) for more captivating content from me.
