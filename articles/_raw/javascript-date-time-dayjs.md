---
title: JavaScript Dates – How to Use the DayJS Library to work with Date and Time
  in JS
subtitle: ''
author: Grant Riordan
co_authors: []
series: null
date: '2023-08-28T22:09:07.000Z'
originalURL: https://freecodecamp.org/news/javascript-date-time-dayjs
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/fcc_template--5-.png
tags:
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'When it comes to handling dates and times in JavaScript, developers often
  find themselves grappling with the complexities of the built-in Date object.

  While vanilla JavaScript provides fundamental functionality, it can be quite cumbersome
  to work wit...'
---

When it comes to handling dates and times in JavaScript, developers often find themselves grappling with the complexities of the built-in `Date` object.

While vanilla JavaScript provides fundamental functionality, it can be quite cumbersome to work with, especially when dealing with parsing, formatting, and manipulating dates.

This is where external libraries like DayJS come into play, offering a plethora of advantages that make working with dates and times a breeze.

In this article I am going to introduce you to DayJS and how this tiny library can hugely improve your code base and productivity.

Here's what we'll cover:

* How to install the DayJS library
* How to work with dates and time within JavaScript
* How you can utilise the DayJS library to make these functions easier, more concise, and more readable
* Comparisons between executing functionality in both vanilla JS and DayJS
* Useful functions available within the DayJS library

## Table of Contents:

1. [Quick Intro to the Date Object in JavaScript](#heading-quick-intro-to-the-date-object-in-javascript)
2. [How to Install the DayJS Library](#heading-how-to-install-the-dayjs-library)
3. [DayJS API and Basic Syntax](#heading-dayjs-api-and-basic-syntax)
4. [Modularity in DayJS](#heading-modularity-in-dayjs)
5. [Mutability in DayJS](#heading-mutability-in-dayjs)
6. [Immutability and Immutable Objects in DayJS](#heading-immutability-and-immutable-objects-in-dayjs)
7. [Parsing Flexibility](#heading-parsing-flexibility)
8. [How to Add to or Subtract from Date and Time](#heading-how-to-add-to-or-subtract-from-date-and-time)
9. [How to Compare Dates in DayJS](#heading-how-to-compare-dates-in-dayjs)
10. [How to Get the Difference Between Two Dates](#heading-how-to-get-the-difference-between-two-dates)
11. [How to Get the Start or End of a Time Period](#heading-how-to-get-the-start-or-end-of-a-time-period)
12. [How to Combine Functions in DayJS](#heading-how-to-combine-functions-in-dayjs)
13. [Conclusion](#heading-conclusion)


## Quick Intro to the Date Object in JavaScript

You can use the `Date` object in JavaScript to work with dates and periods of time. But sometimes working with the `Date` object can be cumbersome, and the date / time can be hard to manipulate. 

Let's look at how to get today's date within JavaScript:

```javascript
var date = new Date();
```

Easy enough right? This will give us an ISO date (this is a universal date format) which ouputs like this:
`2023-07-16T14:51:47.557Z`

So you can see that in `year-month-date`, the `T` marks the point in which the Time part of the Date begins. Then the following numbers are `hours:minutes:seconds.fractional seconds`. The `Z` at the end means there is no timezone specified and should utilise UTC timezone (it's pronounced "Zulu").

You can read more about this format [here](https://www.ionos.co.uk/digitalguide/websites/web-development/iso-8601/).

# The DayJS Library

Now, I'm not saying the other methods of working with dates and time are wrong, but due to their complexity, for me, they just don't seem worth the hassle. 

When dealing with date and time in code, I want an easy to use, out of the box solution that adds readability to my code and offers flexibility.

This is where DayJS comes into play. It's an alternate way to handle dates and time in JavaScript, in the form of a libary. 

This library, unlike others, is extremely small in size. For example there is another common libary used by some developers called `MomentJs`, but its file size is very large. Moment.js itself is **280.9kb**, and this increases to **467.6kb** after including the timezone library (allowing you to set default timezones, and manipulate dates based on specific timezones). 

Large imports and library files are something we really want to avoid when developing for both the web and mobile to help increase loading speeds and bundle sizes. 

DayJs comes in at a impressive **2kb** – that's an extremely small file size, especially considering its capabilities and functionality.

## How to Install the DayJS Library

In order to learn the most from this tutorial, I highly reccommend installing DayJS so you can follow along with the examples and points made. 

DayJS is easily installed via the yarn or npm package managers using the following commands

```cmd
// yarn
yarn add dayjs

//node
npm install dayjs
```

To use DayJS in your `.js` file, simply import it using the regular import syntax:

```javascript
import dayjs from 'dayjs'
```


## DayJS API and Basic Syntax

Working with dates and times in vanilla JavaScript often involves multiple method calls and calculations. This makes the code too verbose and challenging to read. 

The DayJS library addresses this issue by providing a much more intuitive and streamlined API, which greatly simplifies date and time manipulation.

Consider the task of formatting a date into a specific format, such as "YYYY-MM-DD HH:mm:ss", (year-month-date 24Hour:minutes:seconds).

Here's how you could do it using vanilla JavaScript's Date object:

```javascript
const currentDate = new Date();
const formattedDate = `${currentDate.getFullYear()}-${(currentDate.getMonth() + 1).toString().padStart(2, '0')}-${currentDate.getDate().toString().padStart(2, '0')} ${currentDate.getHours().toString().padStart(2, '0')}:${currentDate.getMinutes().toString().padStart(2, '0')}:${currentDate.getSeconds().toString().padStart(2, '0')}`;

console.log(formattedDate); // Output 2023-08-23 17:02:33
```

The above code utilises the `Date` built-in functions to gather various parts of the date object.

- `getFullYear()` – gets the full year 
- `getMonth()` –  gets the month part
- `getDate()` – gets the date part
- `getHours()` – gets the current hour in 24hr format
- `getMinutes()` – gets the minutes part
- `getSeconds()` – gets the seconds part

It then builds a complex interpolated string variable containing all the required parts as we'd expect to see them, that is with leading 0's for single digit months / days / minutes / seconds, (which is what the `padStart()` function is doing). 

As you can see, this is highly unreadable – and we could refactor this to make it more readable. But the concept still stands. 

Let's take the example below. Here we're creating a `formatDate` function that will take in a JS `Date` object, and return a formatted date using the `day/month/year` format:

```javascript
const formatDate = (date) => {
  // Get the individual date components
  var day = date.getDate(); // get the Date part
  var month = date.getMonth() + 1; // Get the Month (Months are zero-based)
  var year = date.getFullYear(); // Get the year
  var hours = date.getHours(); // Get the hour
  var minutes = date.getMinutes(); // Get the minutes
  var seconds = date.getSeconds(); // Get the seconds
```

You may be asking why we had to add 1 to the month. As I tried to explain in the comments, `getMonth()` is zero-based. This means that January equals **0**, so to get the correct month number, we need to add 1 to all the months. This means that now January would become **1**.

So, in the above code we've got the relevant parts of the Date object we need (day, month, year). Now we've got do some formatting to these parts, to make them fit our expected outcome of 2 digits for day and month.

```javascript
  // Pad single digits with leading zeros to make 2 digits, 
  var formattedDay = day < 10 ? "0" + day : day;
  var formattedMonth = month < 10 ? "0" + month : month;

  // Concatenate (join) the formatted date components
  return formattedDay + "/" + formattedMonth + "/" + year;
};

// Usage example
var currentDate = new Date();
var formatted = formatDate(currentDate);
console.log(formatted); // Output: "16/07/2023"
```

So if we were to put it all together, we'd get the following code:

```
const formatDate = (date) => {
  // Get the individual date components
  var day = date.getDate(); // get the Date part
  var month = date.getMonth() + 1; // Get the Month (Months are zero-based)
  var year = date.getFullYear(); // Get the year
  var hours = date.getHours(); // Get the hour
  var minutes = date.getMinutes(); // Get the minutes
  var seconds = date.getSeconds(); // Get the seconds
  
  // Pad single digits with leading zeros to make 2 digits, 
  var formattedDay = day < 10 ? "0" + day : day;
  var formattedMonth = month < 10 ? "0" + month : month;

  // Concatenate (join) the formatted date components
  return formattedDay + "/" + formattedMonth + "/" + year;
}

// Usage
var currentDate = new Date();
var formatted = formatDate(currentDate);
console.log(formatted); // Output: "16/07/2023"
```

Now that's a combination of 19 lines of code, 6 object-based functions, and 1 utility function – and it's also highly inflexible. 

### How can DayJS help make this easier?

Let's see how we could accomplish this in DayJS:

```javascript

const currentDate = dayjs();
const formattedDate = currentDate.format('YYYY-MM-DD HH:mm:ss');
console.log(formattedDate);

```

That's it! In 3 lines of code, we've retrieved the current date and time using the `dayjs()` function, formatted it to the provided dateTime format using a string parameter, and logged out the ouput.

In the above code we're using the `dayjs.format()` utility function. This function allows us to pass our preferred date format, based on a common JS format syntax. 

`YYYY` = numeric year
`MM` = numeric month of the year as 2 digits
`DD` = numeric date as 2 digits
`HH` = 24hour clock for hours
`mm` = 2 digit minutes
`ss` = 2 digit seconds

All seperated with hyphens and colons.

For a list of all possible formats, see the DayJS documentation format options [here](https://day.js.org/docs/en/display/format#list-of-all-available-formats).

I think we can all agree that 3 lines of readable code are far superior to 19 lines of convoluted code. 

# Modularity in DayJS
The DayJS library offers a modular design that allows developers to include only the specific functionalities they need. 

This modularity not only enhances the library's flexibility but also helps in optimising the size of your application bundle. Here's a closer look at how DayJS achieves modularity and its implications for application size.

DayJS is designed as a set of individual plugins that provide various features. These plugins can be included or excluded based on your project's requirements. 

Some of the available plugins cover features like timezone support, duration calculations, custom parsing, and more advanced formatting options. 

This modular structure ensures that you only load the parts of the library that you'll actually use, preventing unnecessary bloat in your application.

Here's a simplified example of how you can leverage modularity in DayJS:

```javascript

// Import only the specific dayjs functionalities you need
import dayjs from 'dayjs';
import timezone from 'dayjs/plugin/timezone';

// Apply the required plugin
dayjs.extend(timezone);

// Now you have a customized dayjs instance with only the necessary functionalities
const customDayjs = dayjs().tz('America/New_York');
```

Above, as you can see in the comments, we are simply importing DayJS, as well as the `theetimezone` module. We then simply create a new `dayjs()` object and set the timezone to New York America. This means that the date and time will be current date/time in New York, rather than the DayJS default UTC.

The modularity of the DayJS library provides developers with the flexibility to tailor their date and time handling to specific project needs. This not only keeps your codebase clean and focused but also optimizes the size of your application bundle. 

By including only the required functionalities, you can enhance the performance of your application, particularly in terms of loading times for users.

This is a complete contrast to vanilla JavaScript's `Date` object which, because it is baked into the JavaScript language, it cannot be overwritten, extended, or have particular elements removed. 

# Mutability in DayJS

Wait, what does mutability mean?

Mutability refers to the ability of an object's state to change after it's created. 

In programming, a **mutable** object can be modified. That is, its properties or values can be altered after its initial creation. This can lead to unexpected changes and side effects, potentially affecting the behavior of the program.  

This is especially true when dealing with dates and times. Vanilla JavaScript's Date object is **mutable**, meaning that altering one instance can inadvertently affect others. 

This is why the `Date` object has `set` methods on the object itself. So when calling these methods, it affects the object itself.

Maybe an example will help:

With the vanilla JS Date Object (mutable):

```javascript
var date = new Date("2023-07-16"); // original date object
console.log(date); //2023-07-16T00:00:00.000Z

date.setDate(date.getDate() + 1); // change the date - add 1 day
console.log(date); // 2023-07-17T00:00:00.000Z the original date has been changed
```

Here we have used the `new Date()` command to initialise a new date object. This object is mutable, and to get an updated value, we have to mutate the orginal object because its *mutable*. We do this using the `setDate()` function. 

When using JavaScript's built in Date functionality you have to be careful how you are utilising and modifying the date objects. You can become entangled in a web of unexpected outcomes if you begin modifying the original date object too much. 

## Immutability and Immutable Objects in DayJS

In contrast, immutability means that an object's state cannot change once it's created, as it doesn't make "changing" actions on the actual object itself. 

When working with immutable objects, you create a new instance with modified values instead of altering the original. This helps ensure that your data remains consistent and predictable throughout your program. 

Immutable data structures are often favored in functional programming and can lead to more robust, easier-to-maintain code.

When you perform operations on a DayJS object, such as adding or subtracting time, the library returns a new instance with the modified value, leaving the original instance unchanged. 

This approach prevents unexpected changes to your data and reduces the risk of introducing errors that can be hard to trace.

Consider the following example using DayJS:

```javascript
var originalDate = dayjs("2023-07-16");
var modifiedDate = originalDate.add(1, "day");

console.log(originalDate.format("YYYY-MM-DD")); // Output: "2023-07-16"
console.log(modifiedDate.format("YYYY-MM-DD")); // Output: "2023-07-17"
```

Using DayJS you can modify the original date object as much as you want using the various available functions, without discarding the original value. This means that it can be used / accessed at any time.

### Benefits of Immutability 

- Predictability: Immutability ensures that once a date or time object is created (set), it won't change unexpectedly throughout your code. This makes it easier to reason about your program's behavior.

- Debugging: Mutable objects can lead to difficult-to-trace bugs when their values change unexpectedly. With immutability, you can be confident that a date or time won't change without your explicit intent.

- Parallel Processing: In multithreaded or parallel programming environments, immutable data structures are inherently thread-safe. This can prevent race conditions and synchronization issues.

**Note:** You can achieve an "immutable" like work around by cloning the original `Date` object like so:

```javascript
const cloneDate = (date) => {
  return new Date(date.getTime());
};

// Usage example
var originalDate = new Date("2023-07-16");
var mutableDate = cloneDate(originalDate);

mutableDate.setDate(mutableDate.getDate() + 1);

console.log(originalDate); // 2023-07-16T00:00:00.000Z
console.log(mutableDate); // 2023-07-17T00:00:00.000Z
```

This code creates a clone function, which takes the original date, and then creates a new date from the original and returns it. This allows you to keep the original date, but make some modifications to a replica of that date, without modifying the original. 

The downside to this is more memory usage, and the complexity overhead. 

## Parsing Flexibility

Parsing date strings can be a real challenge in vanilla JavaScript, particularly when handling non-standard formats. 

DayJS offers an extensive set of parsing options, making it much more versatile when dealing with a wide range of input formats. This feature proves especially valuable when working with data from diverse sources or APIs that might have different date representations.

* User Input: When dealing with user input, such as dates from forms, users might enter dates in various formats. DayJS's parsing capabilities enable you to handle these inputs accurately and consistently.

* Database Interaction: Databases might store dates in different formats or time zones. DayJS's parsing can assist in correctly interpreting these dates for use within your application.

* API Responses: APIs often return date and time data in standardized formats like ISO 8601, but they can also vary. DayJS enables you to parse API responses easily, ensuring correct data representation in your application.


### How this Compares with Vanilla JavaScript:

Vanilla JavaScript's Date object lacks the same level of parsing flexibility. While it can handle some standard formats (ISO8601 / RFC2822) and a few other variations, handling non-standard or diverse formats can be challenging. You often need to manually split the date string and perform calculations to create a valid Date object.

Let's say we had a en-GB date, (day/month/year). By default the `Date` object doesn't cater for this. Meaning we have to parse it ourselves by splitting the string into parts, and passing these to the `new Date()` call. 

```javascript
const dateString = "23/08/2023";
const parts = dateString.split("/");
const dateObject = new Date(parts[2], parts[0] - 1, parts[1]);

console.log(dateObject);
```

If you tried to pass `dateString` directly to the `new Date()` call you would get an error, however in en-US format (month/date/year) it works fine. 

```javascript
const ukDate = new Date("21/01/2023");
console.log(ukDate) // Output: Invalid Date

const usDate = new Date("01/21/2023");
console.log(usDate); // Output: 2023-01-21T00:00:00.000Z
```

Here, you can see that knowledge of how the `Date` object works is necessary. If this were in an actual application, testing would be necessary to ensure we don't get any errors when parsing from multiple sources. 

### DayJS parsing flexibility

DayJS builds on `Date`'s core functionality, and for me adds one of the best parsing options for developers. It allows you to pass any date string to the `dayjs()` function, along with the format of that string. 

**Note:** This does require adding the `customParseFormat` plugin from DayJS – this can be imported very easily.

```javascript:
import dayjs from "dayjs";
import CustomParseFormat from "dayjs/plugin/customParseFormat";

dayjs.extend(CustomParseFormat);
```

This means that when dealing with multiple sources, you can tell DayJS to parse the date string according to how the source is presenting it. 

Normally I'd say store all dates (where you have control over such thing) as UTC ISO8601 date strings, as then you have a solid baseline, and can convert these to the relevant timezone when needed. 

Breaking down the `dayjs()` function, we can see it can receive multiple parameters. These are:

- **string** (string) – this is the string representation of the date you'd like to create.

- **format** (string) – this is the format of the string you're passing in (in the same way we did with the `format()` function).

- **timezone** / **locale** (string) – Locale key to use when parsing.

- **strict** **parsing** (boolean) – Strict parsing requires that the format and the input match exactly including delimiters. 

So what does all this mean? Well, it means we have a lot more control over our parsing / creating of dates. 

Examples:

```javascript
const date1 = dayjs('20/03/2013', 'DD/MM/YYYY').toISOString(); // No Error & Output: '2023-03-20T00:00:00.000Z'

// state the format the dateString will be in from the API
const customFormat = 'YYYY/MM/DD HH:mm:ss'; 

const dateStr = '2023/08/23 14:37:41'; // dateString from the API

// create dayjs object from dateString parsing it using the provided format
const parsedDate = dayjs(dateStr, customFormat);

// format the parsed date , removing the time stamp
console.log(parsedDate.format('YYYY-MM-DD'));  // Outputs: 2023-08-23
```

Hopefully you can see that DayJS makes parsing and working with dates a lot easier. It offers a multitude of different and flexible ways to parse various dates, making working with multiple sources far easier than simply using the built in `Date` object. 

# What Else Can DayJS Do?

## How to Add to or Subtract from Date and Time

Many times I've been asked to calculate a date in the future by adding a number of days to the current date, or subtracting a number of hours from the time.

### How to do this in Vanilla JavaScript:

Using JavaScript's `Date` object we can do this by using the `setDate()` functions. We do this by:

1. Getting the current date
2. Getting the number of days to add (5 days)
3. Using the `setDate()` function on the `Date` object by obtaining the date portion of the Date object, and adding on 5 days, 

So for example, `getDate()` could return 16, so we're resetting the date portion to 16 + 5 = 21. So then the date would be the 21st rather than the 16th. 

Example below:

```javascript
var date = new Date(); //2023-08-16T16:43:33.072Z
var daysToAdd = 5;
date.setDate(date.getDate() + daysToAdd);

console.log(date); // 2023-08-21T16:43:33.072Z

```

or condensed (if lines of code are a concern) to:

```javascript
var date = new Date()
console.log(date.setDate(date.getDate() + 5));
```

Although concise, it loses its readability somewhat. 

### How to do this in DayJS:

DayJS has a naming convention that is more readable for its functions. This means when reading through your code, you can see what it is doing more clearly.

For example taking the same example as above and writing it in DayJS would look something like this:

```javascript
var date = dayjs().add(5, "day").toISOString(); //2023-08-21T16:43:33.000Z
```

Here we are maximising the usage of function chaining amd calling `add()` on the returned dayjs object. We're passing in a number we want to add, as well as a time period to add (in this case `day`). The DayJS library will then take care of adding 5 days to our current date. Then it returns this date in the format of an ISO string. 

This can also be done with subtracting days as follows:

In Vanilla JavaScript:

```javascript
var date = new Date(); //2023-08-16T16:43:33.072Z
var daysToSubtract = 5;
date.setDate(date.getDate() - daysToAdd);

console.log(date); // 2023-08-11T16:43:33.072Z

```

In DayJS:

```javascript
var date = dayjs().subtract(5, "day").toISOString(); //2023-08-11T16:43:33
```

Once again the clarity of the DayJS library allows for the user to read it more like plain English: "Subtract 5 days from this DayJS object and return as an ISO string."

## How to Compare Dates in DayJS

When working with dates, there will often be times where you need to compare date objects – for example checking whether one date is before or after another specific date. 

With the JavaScript `Date` object, you'd usually do this using the `greaterThan` (>) or `lessThan` (<) operators.

But it can often be confusing which way around these operators should be used. This is because to apply the operators to dates, the dates are converted to timestamps under the hood, and then compared chronologically. 

For example:

```javascript
var date1 = new Date("2023-07-16");
var date2 = new Date("2023-07-18");

if (date1 < date2) {
  console.log("Date 1 is before Date 2");
} else {
  console.log("Date 1 is after Date 2");
}

// after
if (date1 > date2) {
  console.log("Date 1 is after Date 2");
} else {
  console.log("Date 1 is before Date 2");
}

// same
if (date1 === date2) {
  console.log("Date 1is exaclty the same as Date 2");
} else {
  console.log("Date 1 not exactly the same as Date 2");
}
```

Although this seems very simple to read and work with, DayJS offers a great API for dealing with date comparison, which can be a little easier to read straight away.

For example:

```javascript
var date1 = dayjs("2023-07-16");
var date2 = dayjs("2023-07-18");
```

Now say we want to check if date1 is before date2 – we can use the `isBefore()` API function. I and many other developers find it far clearer as to what the code is actually doing, rather than having to think about which operator the code is using. 

```javascript
if (date1.isBefore(date2)) {
  console.log("Date 1 is before date 2");
} else {
  console.log("Date 1 is after date 2");
}
```

You can also use acheieve a similar outcome with the `isAfter()` function, checking if date1 is **after** date2.

```javascript
if (date1.isAfter(date2)) {
  console.log("Date 1 is after date 2");
} else {
  console.log("Date 1 is before date 2");
}
```

One API function I find much more reliable is the `isSame` function. As many JavaScript developers will know, when checking the equality of objects, especially developers new to the language, it can be confusing when to use `==` vs `===`. 

DayJS removes this unknown, and gives a clear / readable function to do this for you. 

```
//check if date1 is the same as date2
if (date1.isSame(date2)) {
  console.log("Date 1 is exactly the same as date 2");
} else {
  console.log("Date 1 is not exactly the same as date 2");
}
```

Say we want to check that a date falls in between two ranges. Again, DayJS makes this easier, with the `isBetween()` function. Using the `isBetween()` function gives us several other benefits:

* Easy Date Range Checking: Instead of manually comparing dates and performing arithmetic operations, you can use `isBetween()` to easily check if a date is within a specified range.

* Readability and Maintainability: Using `isBetween()` makes your code more readable and understandable. It clearly conveys the intent of checking whether a date falls within a certain range.

* Support for Inclusive and Exclusive Ranges: The `isBetween()` function in DayJS allows you to specify whether the start and end dates are included or excluded from the range. This gives you flexibility in defining your date intervals.

Example:

```javascript
const targetDate = dayjs('2023-08-15');
const startDate = dayjs('2023-08-01');
const endDate = dayjs('2023-08-31');

const isWithinRange = targetDate.isBetween(startDate, endDate, null, '[]'); 
console.log(isWithinRange) // Output: true
```

As you can see, the functions `isBefore`, `isAfter`, `isSame`, and `isBetween` make it clearer what the code is checking. 

Having such verbose names shows a clear intent of what the function is doing (as opposed to JavaScript's built in methods using operators, or mathmatical conversions). The clear and concise nature of the API functions may be helpful for junior developers, or when simply skimming through code.

This is certainly more apparent with DayJS functions like:

- `isYesterday()`
- `isTomorrow()`
- `isToday()`

## How to Get the Difference Between Two Dates

The `diff` function makes obtaining the difference between two dates so simple. Much easier than with the standard `Date` object!

When would we want to do this, though? Say you were building a user portal and you wished to display the number of days or hours since your last visit. Or a countdown app, that can show us how many days, weeks, hours until a particular date and time. You could do all this using the `diff()` function. 

Let's take a look at the `diff` function:

```javascript
const date1 = dayjs("2019-01-25");
const date2 = dayjs("2018-06-05");

const differenceInMilliseconds = date1.diff(date2); 
console.log(differenceInMilliseconds); // Output: // 20214000000 
```

But milliseconds isn't always useful for UI elements, where we may want to display days, weeks, or months. 

Fortunately for us, DayJS allows us to specify the denonmiation of time we'd like to return the difference as.

Going back to our example of user UI, we could have a toggle which could switch between multiple denominations of time. This would show the user multiple timeframes since their last login, or how many days or hours they've spent completing a game etc. 

Available denominations:
- days
- weeks
- quarters
- months
- years
- hours
- seconds
- milliseconds

```javascript
const date1 = dayjs("2023-01-25");
const date2 = dayjs("2022-06-05")
date1.diff(date2, "month"); // 7 (months)

const date1 = dayjs("2023-08-25");
date1.diff("2023-08-27", "day"); // 2
```

By default, `diff()` will truncate the result to zero decimal places, returning an integer. If you want a floating point number, pass true as the third argument, which will give you a more accurate difference.

```javascript
const date1 = dayjs("2023-01-25");
date1.diff("2022-06-05", "month", true); // 7.645161290322581
```

Ok, but why is this so much better than using the `Date` object in JavaScript? Well let's look at how we'd do this with `Date`.

```javascript
function calculateDateDifferenceInDays(date1, date2) {
  // Convert both dates to milliseconds
  const date1Millis = date1.getTime();
  const date2Millis = date2.getTime();

  // Calculate the difference in milliseconds
  const differenceMillis = Math.abs(date2Millis - date1Millis);

  // Convert milliseconds to days (1 day = 24 hours = 24 * 60 * 60 * 1000 ms)
  const differenceDays = differenceMillis / (24 * 60 * 60 * 1000);

  return differenceDays;
}

// Example usage
const startDate = new Date('2023-08-15');
const endDate = new Date('2023-08-25');

const daysDifference = calculateDateDifferenceInDays(startDate, endDate);
console.log(`The difference between the dates is ${daysDifference} days.`);

```

Off the bat, we've had to hard code the function to only return `days`. To allow for the same variations as we get in the `dayjs` library we would have to write our own extension function, which would handle each combination of conversion needed.

For example, getting the difference in months could be calculated slightly differently:

```javascript
function calculateMonthDifference(startDate, endDate) {
  const startYear = startDate.getFullYear();
  const startMonth = startDate.getMonth();

  const endYear = endDate.getFullYear();
  const endMonth = endDate.getMonth();

  const yearDifference = endYear - startYear;
  const monthDifference = endMonth - startMonth;

  return yearDifference * 12 + monthDifference;
}
```

But again, it's just more and more complex code to do something that a tiny library could do in a maximum of 3 lines of code. It's just not as flexible and easy to use as DayJS is. 

## How to Get the Start or End of a Time Period

`startOf` and `endOf` are two more great functions within the DayJS library. They allow you to easily return the start and end of a date period. 

For example you could get the start / end of the day, week, month, or year. This could be handy when needing to calculate how many days are left in a month. Some months have more days than others, but we don't want to have to calculate / keep track of this somewhere in our code. 

Let's look at how you can use it:

```javascript
const startOfDay = dayjs().startOf("day"); // 00:00:00 of today

// or given date
const startOfGivenDate = dayjs("2023-08-12T15:00:00").startOf("day");

const startOfWeek = dayjs().startOf("week"); // 00:00:00 first day of the week (locale aware)
const startOfYear = dayjs().startOf("year"); // 1st Jan 2023 00:00:00

const endOfDay = dayjs().endOf("day"); // 23:59:59 of today
const endOfWeek = dayjs().endOf("week"); // 23:59:59 of last day of week (locale aware)
const endOfYear = dayjs().endOf("year"); // 31 Dec 2023 23:59:59
```

If we wanted to accomplish the same thing with vanilla JavaScript, we would have to do something like this:

```javascript
const beginningOfDay = (inputTime?: string) => {

  // Convert inputTime to a Date object if provided
  let date inputTime ? new Date(inputTime) : new Date();

  // Set the time to 00:00:00
  date.setHours(0, 0, 0, 0);

  return date;
};

const givenTime = "2023-08-12T15:00:00"; // 3pm on 12th August 2023
const startOfGiven = beginningOfGivenDay(givenTime);
```

As you can see, DayJS makes handling beginning and end of time periods far easier than using pure JavaScript. JavaScript tends to require more code, because you would need to write your own implementation of each of these methods.


## How to Combine Functions in DayJS

As already discussed, DayJS allows for chaining of functions, making it a  highly powerful tool. 

Take a scenario where we have a user portal and we want to know if the time between today and the end of the month is greater than 7 days to determine what UI element to display (for example "expiring soon" or "keep going").

You can do this in fewer than 5 lines of code with DayJS like so:

```javascript
const current = dayjs();
const differenceInDays = current.endOf('month').diff(current,'day');

if(differenceInDays <= 7){
 console.log("Expires Soon"); 
}
```

**What is it doing?**

1. Getting the current date and time
2. Using function chaining and immutability to:
    a. get the end of the current month
    b. get the difference between the current end of month and current date and time.
3. Checking if the `differenceInDays` is less than or equal to 7
4. If so, displaying an `expires soon` message.

"Oh come on we could do this in JavaScript still" I hear you saying. Well, yes – like all the other examples, you could do it in JS. But again, it would take more effort and code which needs to be maintained. Here's what it would look like:

```javascript
function daysUntilEndOfMonth() {
  const currentDate = new Date();
  const currentYear = currentDate.getFullYear();
  const currentMonth = currentDate.getMonth();
  
  // Get the first day of the next month
  const firstDayOfNextMonth = new Date(currentYear, currentMonth + 1, 1);
  
  // Subtract one day to get the last day of the current month
  const lastDayOfCurrentMonth = new Date(firstDayOfNextMonth.getTime() - 1);
  
  // Calculate the difference in days (using timestamp)
  const timeDifference = lastDayOfCurrentMonth - currentDate;
  console.log(timeDifference) // Output: 689366264 (milliseconds)
  
  // Convert the timestamp to actual days
  const daysDifference = Math.ceil(timeDifference / (24 * 60 * 60 * 1000));
  
  return daysDifference;
}

// Example usage
const daysUntilEnd = daysUntilEndOfMonth();
console.log(`Number of days until the end of the month: ${daysUntilEnd} days`); //Output: Number of days until the end of the month: 8 days

```

A bit simpler with DayJS, isn't it?


## Conclusion

In essence, the end goal of this article was to highlight a helpful library that makes working with dates and times far easier. The code is much more concise and easier to read than the standard built in Date object within JavaScript. 

I'm not saying that any of usages of `Date` object in this tutorial are wrong or bad. I'm just pointing out that you don't always need to write cumbersome, over-complicated code when there is a free libary available. Especially when it's extrememly small (negligible) in size. It'll also have miniscule impact on your code's bundling or running, and it offers you so much in terms of benefits. 

Go check it out and add it to your next or existing project. Give it a try, and let me know what you think via [twitter](http://twitter.com/gweaths).

You can find out more about DayJS and take advantage of all its capabilities [here](https://dayjs.org) on their website. 



