---
title: parseInt() in JavaScript – JS String to Int Example
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-02-11T00:44:09.000Z'
originalURL: https://freecodecamp.org/news/parseint-in-javascript-js-string-to-int-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/parseint.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "In this tutorial, we will talk about the parseInt function in JavaScript.\
  \ This function parses (break down) a string and returns an integer or NaN (Not\
  \ a Number). \nHow the parseInt function works\nThe main purpose of using the parseInt\
  \ function is to ..."
---

In this tutorial, we will talk about the `parseInt` function in JavaScript. This function parses (break down) a string and returns an integer or `NaN` (Not a Number). 

## How the `parseInt` function works

The main purpose of using the `parseInt` function is to extract a number from a string. This turns the returned value to an actual number. 

Here is the syntax:

```txt
parseInt(string)
```

Consider the example below:

```javascript
const myNumber = '3';
console.log(2 + myNumber);
// returns 23
```

In the example above, 3 is a string and not an actual number. When we add 2 to the string, we are given 23 because we are just adding 2 to a string that is just in the form of a number.

With the `parseInt` function, we can can extract 3 from the string and turn it to an actual number. Here is an example:

```javascript
const myNumber = '3';
console.log(2 + parseInt(myNumber));
// returns 5

```

Now the function has removed 3 from the string and converted it to an actual number.

From '3' to 3.

Recall that we said that the `parseInt` function can either return an integer or `NaN`. So when would we get a `NaN` value? 

This happens when we have some text before a number in a string. Something like "age is 50" will return a `NaN` value because the `parseInt` function only looks at the first value starting the string. If the value is not a number, `NaN` is returned. Here:

```javascript
const age = 'age is 50';
console.log(parseInt(age));
// returns NaN
```

Let's rearrange the string and see what happens.

```javascript
const age = '50 is the age';
console.log(parseInt(age));
// returns 50
```

Now the first value in the string is a number and that number is returned to us.

Note that the `parseInt` function ignores float values. If the age above was 50.05 then it would still return 50 and ignore .05. 

In the same manner, if we had a string like this: "50 100 150 200" then we'd only get 50 returned to us. This is because the `parseInt` function only attempts to extract the first value of a string. 

And if the string had its values written together like this: '50istheage', 50 would still be returned.

## The `radix` parameter

The `parseInt` function accepts a second parameter known as `radix`. This parameter specifies what number system to use. If the radix is omitted then 10 is taken as the default. 

Here is the syntax:

```txt
parseInt(string, radix)
```

This is usually an integer between 2 and 36. If the value of the radix is less than 2 or greater than 36 then `NaN` is returned. 

If we were to specify a radix of 12 then it implies that the number in the string should be parsed from the duodecimal value of the number to its decimal value.

Here is a quick example:

```javascript
console.log(parseInt("50", 12));

// returns 60
```

We get 12 returned because the duodecimal value of 50 in base 10 (decimal) is 60. 

## Conclusion

In this tutorial, we learned how to use the `parseInt` function to extract numbers from strings. 

We also saw how we could use the `radix` parameter to specify what number system to be used when converting our returned integer.

Thank you for reading!

