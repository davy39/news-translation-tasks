---
title: JavaScript String to Boolean – How to Parse a Boolean in JS
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-11-30T22:14:10.000Z'
originalURL: https://freecodecamp.org/news/javascript-string-to-boolean
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/string-to-boolean.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'When you''re manipulating data, receiving values from forms, and dealing
  with data in other ways, these values may take the incorrect datatype.

  Assume you want your value to be a boolean with either true or false, but it is
  stored as a string – "true"...'
---

When you're manipulating data, receiving values from forms, and dealing with data in other ways, these values may take the incorrect datatype.

Assume you want your value to be a boolean with either `true` or `false`, but it is stored as a string – "true" or "false." It becomes challenging to use for your intended purpose, so you must first convert these boolean string values to actual boolean values.

In this article, you will learn how to convert a string to a boolean value using different methods in JavaScript. In case you are in a rush, here is how you can do it:

```js
// Using identity operator
console.log((boolString === "true")); // true / false

// Using Regex
console.log((/true/).test(boolString)); // true
```

If you are not in a rush, let’s understand each of the methods and lots more.

## How to Parse a String to a Boolean with the Identity Operator (`===`)

The strict operator is another name for the identity operator. It will only return `true` if the two values being compared are the same. This implies that their letter case – and everything else – must also be the same. Otherwise, it will return `false`.

In this case, you want to convert a string to a boolean, which means you'll compare it to the string "true". If both values are the same, it will return the boolean value `true`, otherwise, it will return the boolean value `false`.

```js
let boolString = "true"; 
let boolValue = (boolString === "true"); 
console.log(boolValue); // true
```

This is a strict equality operator and will be strict with letter case comparison:

```js
let boolString = "True"; 
let boolValue = (boolString === "true"); 
console.log(boolValue); // false
```

You can fix this using the `toLowerCase()` method, so it first converts the string value to the letter case that fits your comparison and then compares.

```js
let boolString = "True"; 
let boolValue = (boolString.toLowerCase() === "true"); 
console.log(boolValue); // true
```

Another method very similar to the identity operator is the regex method, where you can test if two values match.

## How to Parse a String to a Boolean with Regex

Regex stands for Regular Expressions. It is a vast programming topic and you can use regex as a pattern to match and test string character combinations.

A very simple guide to regex will tell you that the expression is placed between two slashes (`/`). For example, if you want to test for the true string value, you'd do this:

```js
let boolString = "true"; 
let boolValue = (/true/).test(boolString);
console.log(boolValue); // true
```

This also is case sensitive:

```js
let boolString = "True"; 
let boolValue = (/true/).test(boolString);
console.log(boolValue); // false
```

You will have to add the `i` flag at the end of the regular expression to allow for a case-insensitive match.

```js
let boolString = "True"; 
let boolValue = (/true/i).test(boolString);
console.log(boolValue); // true
```

## How to Parse a String to a Boolean with the Double NOT Operator (`*!!*`)

You should also know how to use the single NOT operator, which you can use to invert a result.

When you add the single NOT operator in front of a string, it will either return `true` or `false`. If it’s an empty string, it will return `true` otherwise, `false`:

```js
let stringValue1 = !'true';
let stringValue2 = !'';

console.log(stringValue1); // false
console.log(stringValue2); // true
```

This is not what you want. Rather, you want to convert a string to a boolean, meaning when the string is empty, it should return `false`, and in every other case, it should return `true`.

This is when you can use the double NOT logical operator. You use it to invert the result of the single NOT operator:

```js
let stringValue1 = !!'true';
let stringValue2 = !!'';

console.log(stringValue1); // true
console.log(stringValue2); // false
```

You use this method to convert **any string value** to a boolean. When it is empty, it returns `false`. Otherwise it returns `true`.

One disadvantage of this method is that you cannot convert a string of `"false"` to a boolean value of `false`. It will only return `false` when it is an empty string.

## How to Parse a String to a Boolean with a Boolean Wrapper

The JavaScript Boolean object represents a boolean value. This method works just like the double NOT operator.

```js
// Syntax
Boolean()
```

When you pass a string value into the Boolean object, it will evaluate to `true`, but when you pass an empty string, it will evaluate to `false`.

```js
let stringValue1 = Boolean('true');
let stringValue2 = Boolean('');

console.log(stringValue1); // true
console.log(stringValue2); // false
```

The only limitation with this method is that if you add space between the quote to represent string, it will return `true` — meaning it regards it as a string.

```js
let stringValue = Boolean(' ');

console.log(stringValue); // true
```

**Note:** When you convert a string of `"false"`, you’d expect it to return a boolean value of `false`. But this will return `true` because it only returns `false` when it’s an empty string.

## Wrapping up

In this article, you have learned how to convert a string value to a boolean. The best approach that covers all scenarios is the identity equality operator, while the Boolean object and double logical NOT have better syntax.

Have fun coding!
