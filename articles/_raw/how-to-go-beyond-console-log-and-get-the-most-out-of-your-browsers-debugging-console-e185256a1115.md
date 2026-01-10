---
title: How to go beyond console.log and get the most out of your browser’s debugging
  console
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-17T14:42:52.000Z'
originalURL: https://freecodecamp.org/news/how-to-go-beyond-console-log-and-get-the-most-out-of-your-browsers-debugging-console-e185256a1115
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Lvtq6fDOejQmexdK5t2Npw.png
tags:
- name: console
  slug: console
- name: debugging
  slug: debugging
- name: JavaScript
  slug: javascript
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Gilad Dayagi

  The console object is a very useful feature of browsers that has been around for
  many years. It provides access to the browser’s debugging console.Most web developers
  know how to print messages to the console using console.log. But I’...'
---

By Gilad Dayagi

The `console` object is a very useful feature of browsers that has been around for many years. It provides access to the browser’s debugging console.  
Most web developers know how to print messages to the console using `console.log`. But I’ve found that many don’t know about other features of the `console`, even though they can be very useful for every web developer.

In this post, I’ll go over some of these lesser known features and capabilities. I hope that you will find them useful and interesting, and will incorporate them into your day to day workflow and code.

I added a screenshot of the result of each example. If you want to try things for yourself, just open the DevTools and copy-paste the examples.

### Using multiple arguments

It is quite common to log several values together. These may be a message along with a related value or the content of several related variables.

Here are two ways I’ve seen developers achieve this:

#### 1. String concatenation

```
const a = 123;const b = 'abc';const c = {aa: 234, bb: 345};console.log('Foo bar ' + a + ' ' + b + ' ' + c);
```

![Image](https://cdn-media-1.freecodecamp.org/images/WFSwkoS7zJAs08juQqlWTIZ2O2I8NVELVZ1Y)
_Result of string concatenation_

#### 2. Using multiple calls

```
const a = 123;const b = 'abc';const c = {aa: 234, bb: 345};console.log('Foo bar');console.log(a);console.log(b);console.log(c);
```

![Image](https://cdn-media-1.freecodecamp.org/images/d2KZzOM5YcPtJSnoSwxdg4rS9XrUEkAKs6lr)
_Result of multiple calls_

These methods may work (sort of), but:

* They are not flexible
* They are not very readable
* They are cumbersome to write
* They need special means to work properly with object variables

There are several better alternatives for outputting many variables. The most useful one for quick data dump is sending multiple arguments to `console.log`, like so:

```
const a = 123;const b = 'abc';const c = {aa: 234, bb: 345};console.log('Foo bar', a, b, c);
```

![Image](https://cdn-media-1.freecodecamp.org/images/5oOGL4AISGJppBuuhXTHdQst6tNS6rK0a5oO)
_Result of multiple arguments_

This is very handy for debugging, but the output is not very controllable. For output that is intended to be read (like for a library), I would use a different method, which we’ll get to later on.

### Using different log levels

Besides the familiar `console.log`, there are other logging methods that correspond to different log levels:

```
console.debug('Debug message');console.info('Info message');console.log('Good old log message');console.warn('A warning message');console.error('This is an error');
```

![Image](https://cdn-media-1.freecodecamp.org/images/7LZRb5ZUSjcnw5ObZc96va9fzNjsJpudvrhS)
_Log levels as seen in Google Chrome_

Each log level may have a different default style, which makes spotting errors and warnings at a glance easier.

You can usually also filter which log levels you want to be visible in the DevTools console. This may help reduce clutter.

![Image](https://cdn-media-1.freecodecamp.org/images/4FS42J3jrB8sTwERLqDj-KS-5-8bq8GkXw0T)
_Filtering log levels in Google Chrome_

The appearance of the different levels and the filtering granularity changes from browser to browser.

### Grouping console lines

Some times it is useful to group log messages together. It may allow for more organised and readable output.

This is actually very simple to achieve:

```
console.group();console.log('First message');console.log('Second message');console.groupEnd();
```

![Image](https://cdn-media-1.freecodecamp.org/images/GYLLEc1rejWitvOzcAAIUyrzWGxYkIe7C4OI)
_Grouped log messages_

Note that log groups can also be nested and labeled:

```
console.group('Group aaa');console.log('First message');console.group('Group bbb');console.log('level 2 message a');console.log('Level 2 message b');console.groupEnd();console.log('Second message');console.groupEnd();
```

![Image](https://cdn-media-1.freecodecamp.org/images/ddmYWHrx7W0lAeHRE0mLPx7wKk-adr2lxT00)
_Nested and labeled groups_

In case you want the group to appear collapsed, use `console.groupCollapsed()`

### Measuring performance

Measuring the time between points in the code can serve as a quick way to check the performance of some operations.

Here is a trivial way to do this:

```
const start = Date.now();// do some stuffconsole.log('Took ' + (Date.now() - start) + ' millis');
```

This works, but there’s a more elegant way to achieve something similar:

```
console.time('Label 1');// do some stuffconsole.timeEnd('Label 1');
```

![Image](https://cdn-media-1.freecodecamp.org/images/OBuRCdSdW7cLv9BSmKHsTGcpwizTlUehKbEj)
_Measuring time with the console_

The code is shorter, the measurement is more accurate, and you can keep track of up to 10,000 different timers in parallel on a page.

### String substitution

Previously we learned that you can pass multiple arguments to `console.log` to output multiple values simultaneously. Another way to achieve something similar is to use string substitution. This method requires familiarity with the available placeholders, but offers greater control over the output.

```
const a = 123;const b = 'abc';const c = {aa: 234, bb: 345};console.log('number %d string %s object %o', a, b, c);
```

![Image](https://cdn-media-1.freecodecamp.org/images/m5jIme1eJX9jT0wCHsBxA6mSUyG70r5Af4aQ)
_Logging with string substitution_

Take a look at the documentation (link in the end) for a list of available placeholders.

### Styling

It can be nice to style different log messages differently to increase readability.

We already mentioned that browsers give different default styling to some log levels, but this can also be customized according to your specific needs. Styling is done using a subset of CSS rules, passed in a string as the second parameter, and applied using the marker `%c`.

Note that you can have different styles for different parts of the log message.

For example:

```
console.log("Normal %cStyled %clorem %cipsum", "color: blue; font-weight: bold", "color: red", "background-image: linear-gradient(red, blue); color: white; padding: 5px;");
```

![Image](https://cdn-media-1.freecodecamp.org/images/al9DXYCJEKx4DtYd1gHx4K8CjKrn0xRCEznU)
_Styled log messages_

### Summary

In this post we have seen some of the features of `console` that I think are less well-known and more useful. This is by no means an exhaustive list of everything the `console` can do, as it has many more tricks up its sleeve.

If this got you interested and you want to find out what other things you can do with the `console`, I recommend reading the [relevant documentation on MDN](https://developer.mozilla.org/en-US/docs/Web/API/console) and trying things out in DevTools.

_If you found this useful please share this article on social media._  
_You can also follow me on twitter (@giladaya). Thanks for reading!_

