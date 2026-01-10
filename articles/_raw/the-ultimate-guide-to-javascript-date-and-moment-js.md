---
title: The Ultimate Guide to JavaScript Date and Moment.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-02T18:01:00.000Z'
originalURL: https://freecodecamp.org/news/the-ultimate-guide-to-javascript-date-and-moment-js
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ee7740569d1a4ca3fce.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'Welcome to our ultimate guide on the JavaScript Date object and Moment.js.
  This tutorial will teach you everything you need to know about working with dates
  and times in your projects.

  How to Create a Date Object

  Get the current date and time

  const n...'
---

Welcome to our ultimate guide on the JavaScript `Date` object and Moment.js. This tutorial will teach you everything you need to know about working with dates and times in your projects.

## How to Create a `Date` Object

### Get the current date and time

```js
const now = new Date();

// Mon Aug 10 2019 12:58:21 GMT-0400 (Eastern Daylight Time)
```

### Get a date and time with individual values

```js
const specifiedDate = new Date(2019, 4, 29, 15, 0, 0, 0);

// Wed May 29 2019 15:00:00 GMT-0400 (Eastern Daylight Time)
```

The syntax is `Date(year, month, day, hour, minute, second, millisecond)`. 

Note that the months are zero-indexed, beginning with January at 0 and ending with December at 11.

### Get a date and time from a timestamp

```js
const unixEpoch = new Date(0);
```

This represents the time at Thursday, January 1st, 1970 (UTC), or the Unix Epoch time. The Unix Epoch is important because it's what JavaScript, Python, PHP, and other languages and systems use internally to calculate the current time.

`new Date(ms)` returns the date of the epoch plus the number of milliseconds you pass in. In a day there's 86,400,000 milliseconds so:

```js
const dayAfterEpoch = new Date(86400000);
```

will return Friday, January 2nd, 1970 (UTC).

### Get a date and time from a string

```js
const stringDate = new Date('May 29, 2019 15:00:00');

// Wed May 29 2019 15:00:00 GMT-0400 (Eastern Daylight Time)
```

Getting the date this way is very flexible. All of the examples below return valid `Date` objects:

```js
new Date('2019-06') // June 1st, 2019 00:00:00
new Date('2019-06-16') // June 16th, 2019
new Date('2019') // January 1st, 2019 00:00:00
new Date('JUNE 16, 2019')
new Date('6/23/2019')
```

You can also use the `Date.parse()` method to return the number of milliseconds since the epoch (January 1st, 1970):

```js
Date.parse('1970-01-02') // 86400000
Date.parse('6/16/2019') // 1560610800000
```

### Setting a time zone

When passing a date string without setting a time zone, JavaScript assumes the date/time are in UTC before converting it to your browser's time zone:

```js
const exactBirthdate = new Date('6/13/2018 06:27:00');

console.log(exactBirthdate) // Wed Jun 13 2018 06:27:00 GMT+0900 (Korean Standard Time)
```

This can lead to errors where the date returned is off by many hours. To avoid this, pass in a time zone along with the string:

```js
const exactBirthdate = new Date('6/13/2018 06:27:00 GMT-1000');

console.log(exactBirthdate) // Thu Jun 14 2018 01:27:00 GMT+0900 (Korean Standard Time)

/*
These formats also work:

new Date('6/13/2018 06:27:00 GMT-10:00');
new Date('6/13/2018 06:27:00 -1000');
new Date('6/13/2018 06:27:00 -10:00');
*/
```

You can also pass some, but not all, time zone codes:

```js
const exactBirthdate = new Date('6/13/2018 06:27:00 PDT');

console.log(exactBirthdate) // Thu Jun 14 2018 01:27:00 GMT+0900 (Korean Standard Time)
```

## `Date` Object Methods

Often you will not need the entire date, but just part of it like the day, week or month. Fortunately there are a number of methods to do just that:

```js
const birthday = new Date('6/13/2018 06:27:39');

birthday.getMonth() // 5 (0 is January)
birthday.getDate() // 13
birthday.getDay() // 3 (0 is Sunday)
birthday.getFullYear() // 2018
birthday.getTime() // 1528838859000 (milliseconds since the Unix Epoch)
birthday.getHours() // 6
birthday.getMinutes() // 27
birthday.getSeconds() // 39
birthday.getTimezoneOffset() // -540 (time zone offset in minutes based on your browser's location)
```

## Make Working with Dates Easier with Moment.js

Getting dates and times right is no small task. Every country seems to have a different way of formatting dates, and accounting for different time zones and daylight savings/summer time takes, well, a whole lot of time. That's where Moment.js shines – it makes parsing, formatting, and displaying dates a breeze.

To start using Moment.js, install it through a package manager like `npm`, or add it to your site through a CDN. See the [Moment.js documentation](https://momentjs.com/docs/) for more details.

### Get the current date and time with Moment.js

```js
const now = moment();
```

This returns an object with the date and time based on your browser's location, along with other locale information. It's similar to native JavaScript's `new Date()`.

### Get a date and time from a timestamp with Moment.js

Similar to `new Date(ms)`, you can pass the number of milliseconds since the epoch to `moment()`:

```js
const dayAfterEpoch = moment(86400000);
```

If you want to get a date using a Unix timestamp in seconds, you can use the `unix()` method:

```js
const dayAfterEpoch = moment.unix(86400);
```

### Get a date and time from a string with Moment.js

Parsing a date from a string with Moment.js is easy, and the library accepts strings in the ISO 8601 or RFC 2822 Date Time format, along with any string accepted by the JavaScript `Date` object.

ISO 8601 strings are recommended since it is a widely accepted format. Here are some examples:

```js
moment('2019-04-21');
moment('2019-04-21T05:30');
moment('2019-04-21 05:30');

moment('20190421');
moment('20190421T0530');
```

### Setting a time zone with Moment.js

Up until now, we have been using Moment.js in _local mode_, meaning that any input is assumed to be a local date or time. This is similar to how the native JavaScript `Date` object works:

```js
const exactBirthMoment = moment('2018-06-13 06:27:00');

console.log(exactBirthMoment) // Wed Jun 13 2018 06:27:00 GMT+0900 (Korean Standard Time)
```

However, to set a time zone, you must first get the Moment object in _UTC mode:_

```js
const exactBirthMoment = moment.utc('2018-06-13 06:27:00');

console.log(exactBirthMoment) // Wed Jun 13 2018 15:27:00 GMT+0900 (Korean Standard Time)
```

Then you can adjust for the difference in time zones with the `utcOffset()` method:

```js
const exactBirthMoment = moment.utc('2018-06-13 06:27:00').utcOffset('+10:00');

console.log(exactBirthMoment) // Wed Jun 13 2018 06:27:00 GMT+0900 (Korean Standard Time)
```

You can also set the UTC offset as a number or a string:

```js
moment.utc().utcOffset(10) // Number of hours offset
moment.utc().utcOffset(600) // Number of minutes offset
moment.utc().utcOffset('+10:00') // Number of hours offset as a string
```

To use named time zones (`America/Los_Angeles`) or time zone codes (`PDT`) with Moment objects, check out the [Moment Timezone](https://momentjs.com/timezone/) library.

### Format the date and time with Moment.js

One of the major strengths that Moment.js has over native JavaScript `Date` objects is how easy it is to format the output date and time. Just chain the  `format()` method to a Moment date object and pass it a format string as a parameter:

```js
moment().format('MM-DD-YY'); // "08-13-19"
moment().format('MM-DD-YYYY'); // "08-13-2019"
moment().format('MM/DD/YYYY'); // "08/13/2019"
moment().format('MMM Do, YYYY') // "Aug 13th, 2019"
moment().format('ddd MMMM Do, YYYY HH:mm:ss') // "Tues August 13th, 2019 19:29:20"
moment().format('dddd, MMMM Do, YYYY -- hh:mm:ss A') // "Tuesday, August 13th, 2019 -- 07:31:02 PM"
```

Here's a table with some common formatting tokens:

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{font-family:Lato, sans-serif;font-size:2.2rem;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}
.tg th{font-family:Lato, sans-serif;font-size:2.2rem;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}
.tg .tg-v1p6{font-size:2.2rem;font-family:Lato !important;;text-align:right;vertical-align:top}
.tg .tg-nh17{font-size:2.2rem;font-family:Lato !important;;text-align:left;vertical-align:top}
.tg .tg-htb4{font-weight:bold;font-size:2.2rem;font-family:Lato !important;;background-color:#efefef;text-align:center;vertical-align:top}
</style>
<table class="tg">
  <tr>
    <th class="tg-htb4">Input</th>
    <th class="tg-htb4">Output</th>
    <th class="tg-htb4">Description</th>
  </tr>
  <tr>
    <td class="tg-v1p6">YYYY</td>
    <td class="tg-nh17">2019</td>
    <td class="tg-nh17">4 digit year</td>
  </tr>
  <tr>
    <td class="tg-v1p6">YY</td>
    <td class="tg-nh17">19</td>
    <td class="tg-nh17">2 digit year</td>
  </tr>
  <tr>
    <td class="tg-v1p6">MMMM</td>
    <td class="tg-nh17">August</td>
    <td class="tg-nh17">Full month name</td>
  </tr>
  <tr>
    <td class="tg-v1p6">MMM</td>
    <td class="tg-nh17">Aug</td>
    <td class="tg-nh17">Abbreviated month name</td>
  </tr>
  <tr>
    <td class="tg-v1p6">MM</td>
    <td class="tg-nh17">08</td>
    <td class="tg-nh17">2 digit month</td>
  </tr>
  <tr>
    <td class="tg-v1p6">M</td>
    <td class="tg-nh17">8</td>
    <td class="tg-nh17">1 digit month</td>
  </tr>
  <tr>
    <td class="tg-v1p6">DDD</td>
    <td class="tg-nh17">225</td>
    <td class="tg-nh17">Day of the year</td>
  </tr>
  <tr>
    <td class="tg-v1p6">DD</td>
    <td class="tg-nh17">13</td>
    <td class="tg-nh17">Day of the month</td>
  </tr>
  <tr>
    <td class="tg-v1p6">Do</td>
    <td class="tg-nh17">13th</td>
    <td class="tg-nh17">Day of the month with ordinal</td>
  </tr>
  <tr>
    <td class="tg-v1p6">dddd</td>
    <td class="tg-nh17">Wednesday</td>
    <td class="tg-nh17">Full day name</td>
  </tr>
  <tr>
    <td class="tg-v1p6">ddd</td>
    <td class="tg-nh17">Wed</td>
    <td class="tg-nh17">Abbreviated day name</td>
  </tr>
  <tr>
    <td class="tg-v1p6">HH</td>
    <td class="tg-nh17">17</td>
    <td class="tg-nh17">Hours in 24 hour time</td>
  </tr>
  <tr>
    <td class="tg-v1p6">hh</td>
    <td class="tg-nh17">05</td>
    <td class="tg-nh17">Hours in 12 hour time</td>
  </tr>
  <tr>
    <td class="tg-v1p6">mm</td>
    <td class="tg-nh17">32</td>
    <td class="tg-nh17">Minutes</td>
  </tr>
  <tr>
    <td class="tg-v1p6">ss</td>
    <td class="tg-nh17">19</td>
    <td class="tg-nh17">Seconds</td>
  </tr>
  <tr>
    <td class="tg-v1p6">a</td>
    <td class="tg-nh17">am / pm</td>
    <td class="tg-nh17">Ante or post meridiem</td>
  </tr>
  <tr>
    <td class="tg-v1p6">A</td>
    <td class="tg-nh17">AM / PM</td>
    <td class="tg-nh17">Capitalized ante or post meridiem</td>
  </tr>
  <tr>
    <td class="tg-v1p6">ZZ</td>
    <td class="tg-nh17">+0900</td>
    <td class="tg-nh17">Timezone offset from UTC</td>
  </tr>
  <tr>
    <td class="tg-v1p6">X</td>
    <td class="tg-nh17">1410715640.579</td>
    <td class="tg-nh17">Unix timestamp in seconds</td>
  </tr>
  <tr>
    <td class="tg-v1p6">XX</td>
    <td class="tg-nh17">1410715640579</td>
    <td class="tg-nh17">Unix timestamp in milliseconds</td>
  </tr>
</table>

See the [Moment.js docs](https://momentjs.com/docs/) for more formatting tokens.

Working with JavaScript `Date` objects and Moment.js doesn't have to be time consuming. Now you should know more than enough to get started with both.

