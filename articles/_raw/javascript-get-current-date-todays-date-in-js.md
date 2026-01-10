---
title: JavaScript Get Current Date – Today's Date in JS
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-06-17T15:45:01.000Z'
originalURL: https://freecodecamp.org/news/javascript-get-current-date-todays-date-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/cover-template--2-.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'When you''re developing web applications, you might need to include the
  current date on which a particular operation is performed.

  For example, when submitting data via a form, you may want to include the date that
  data was created or when the form wa...'
---

When you're developing web applications, you might need to include the current date on which a particular operation is performed.

For example, when submitting data via a form, you may want to include the date that data was created or when the form was submitted.

In this article, we will learn how to easily get the current date (today's date) with JavaScript from scratch. We'll also learn how to do this with an external library like Moment.js, a popular JavaScript date library.

Just a note – in general, it's not recommended to use an external library for an operation like this. But if you already have a library installed on your project or you're using it for other operations in your application, you can use it.

### Here's an Interactive Scrim about How to Get the Current Date in JavaScript

<iframe src="https://scrimba.com/scrim/coc634945941f26de68c42292?embed=freecodecamp,mini-header,no-sidebar" width="100%" height="420"></iframe>

## How to Get the Current Date in JavaScript

In JavaScript, we can easily get the current date or time by using the `new Date()` object. By default, it uses our browser's time zone and displays the date as a full text string, such as "Fri Jun 17 2022 10:54:59 GMT+0100 (British Summer Time)" that contains the current date, time, and time zone.

```js
const date = new Date();
console.log(date); // Fri Jun 17 2022 11:27:28 GMT+0100 (British Summer Time)
```

Let's see how we can extract only the date from this long string. We'll make it more readable and understandable to users by using some JavaScript methods that operate on a date object.

### How to Use JavaScript Date Methods

The date object supports numerous date methods, but for this article, we only need the current date and will only use three methods:

* `getFullYear()` – we will use this method to get the year as a four digit number (yyyy), for example 2022.
    
* `getMonth()` – This gets the month as a number (0-11), for example 2 for March since it’s a zero based index (meaning it starts from 0).
    
* `getDate()` – gets the day as a number (1-31).
    

Let’s now put all these together based on the format in which we want our date to appear:

```js
const date = new Date();

let day = date.getDate();
let month = date.getMonth() + 1;
let year = date.getFullYear();

// This arrangement can be altered based on how we want the date's format to appear.
let currentDate = `${day}-${month}-${year}`;
console.log(currentDate); // "17-6-2022"
```

**Note:** We added one to the `date.getMonth()`'s value since it’s `0`\-based indexing. Suppose we don't want to make use of dash(-) between our date values, all we have to do is replace the dash with whatever we prefer.

### How to Use the toJSON() Method

We just saw how to get the current date using date methods. Now let's see how to use the `toJSON()` method, which returns our date in the `yyyy-mm-dd` format in addition to the time format, `hh:mm:ss.ms`.

```js
let date = new Date().toJSON();
console.log(date); // 2022-06-17T11:06:50.369Z
```

Since we want only the current date, we can use the `slice()` method this way to get the first 10 characters:

```js
let currentDate = new Date().toJSON().slice(0, 10);
console.log(currentDate); // "2022-06-17"
```

### How to Use toLocaleDateString()

This is another simple method that returns the date object as a string using local conventions. For example, the date format differs between languages, and this method accepts an argument to correct that.

Let's begin by passing an argument:

```js
let date = new Date().toLocaleDateString();
console.log(date); // 6/17/2022
```

Suppose we want the time in Germany:

```js
let date = new Date().toLocaleDateString("de-DE");
console.log(date); // 17.6.2022
```

Note: We can get a list to all locale codes [here](https://saimana.com/list-of-country-locale-code/).

### How to Use Moment.js

Moment.js is one of the most popular date packages available to everyone, and we can use it to get the current date as well.

As long as you have Moment.js installed in your project, all you need to do is get the current date as follows:

```js
var date = moment();

var currentDate = date.format('D/MM/YYYY');
console.log(currentDate); // "17/06/2022"
```

We can also manipulate it based on how we want the date’s format to appear.

## Conclusion

In this article, we learned about various approaches for obtaining the current date using JavaScript alone or with an external JavaScript library.

You can read more about how you can easily format dates [here](https://www.freecodecamp.org/news/how-to-format-dates-in-javascript/).

Embark on a journey of learning! [Browse 200+ expert articles on web development](https://joelolawanle.com/contents). Check out [my blog](https://joelolawanle.com/posts) for more captivating content from me.
