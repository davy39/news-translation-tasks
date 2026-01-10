---
title: JavaScript Split – How to Split a String into an Array in JS
subtitle: ''
author: Tapas Adhikary
co_authors: []
series: null
date: '2021-06-16T21:19:08.000Z'
originalURL: https://freecodecamp.org/news/javascript-split-how-to-split-a-string-into-an-array-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/freeCodeCamp-Cover-1.png
tags:
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "In general, a string represents a sequence of characters in a programming\
  \ language. \nLet's look at an example of a string created using a sequence of characters,\
  \ \"Yes, You Can DO It!\". In JavaScript, we can create a string in a couple of\
  \ ways:\n\nUsing..."
---

In general, a `string` represents a sequence of characters in a programming language. 

Let's look at an example of a string created using a sequence of characters, "Yes, You Can DO It!". In JavaScript, we can create a string in a couple of ways:

* Using the string literal as a primitive

```js
const msg = "Yes, You Can DO It!";
```

* Using the `String()` constructor as an object

```js
const msg = new String("Yes, You Can DO It!");
```

One interesting fact about strings in JavaScript is that we can access the characters in a string using its index. The index of the first character is 0, and it increments by 1. So, we can access each of the characters of a string like this:

```js
let str = "Yes, You Can Do It!";

console.log(str[0]); // Y
console.log(str[1]); // e
console.log(str[2]); // s
console.log(str[3]); // ,

console.log(str[10]); // a
```

The image below represents the same thing:

![Image](https://www.freecodecamp.org/news/content/images/2021/06/split.png)
_Accessing String Characters by the Index_

Apart from its ability to access string characters by their indices, JavaScript also provides plenty of utility methods to access characters, take out a part of a string, and manipulate it. 

In this article will learn about a handy string method called `split()`. I hope you enjoy reading it.

# The split() Method in JavaScript

The `split()` method splits (divides) a string into two or more substrings depending on a `splitter` (or divider). The splitter can be a single character, another string, or a regular expression. 

After splitting the string into multiple substrings, the `split()` method puts them in an array and returns it. It doesn't make any modifications to the original string.

Let's understand how this works with an example. Here is a string created using string literals:

```js
let message = 'I am a Happy Go lucky Guy';

```

We can call the `split()` method on the `message` string. Let's split the string based on the space (`'  '`) character. Here the space character acts as a splitter or divider.

```js
// Split using a space character
let arr = message.split(' ');

// The array
console.log(arr); // ["I", "am", "a", "Happy", "Go", "lucky", "Guy"]


// Access each of the elements of the array.
console.log(arr[0]); // "I"
console.log(arr[1]); // "am"
console.log(arr[2]); // "a"
console.log(arr[3]); // "Happy"
console.log(arr[4]); // "Go",
console.log(arr[5]); // "lucky"
console.log(arr[6]); // "Guy"


```

The main purpose of the `split()` method is to get the chunks you're interested in from a string to use them in any further use cases.

## How to Split a String by Each Character

You can split a string by each character using an empty string('') as the splitter. In the example below, we split the same message using an empty string. The result of the split will be an array containing all the characters in the message string.

```js
console.log(message.split('')); // ["I", " ", "a", "m", " ", "a", " ", "H", "a", "p", "p", "y", " ", "G", "o", " ", "l", "u", "c", "k", "y", " ", "G", "u", "y"]
```

> 💡 Please note that splitting an empty string('') using an empty string as the splitter returns an empty array. You may get this as a question in your upcoming job interviews!

```js
''.split(''); // returns []
```

## How to Split a String into One Array

You can invoke the `split()` method on a string without a splitter/divider. This just means the `split()` method doesn't have any arguments passed to it. 

When you invoke the `split()` method on a string without a splitter, it returns an array containing the entire string.

```js
let message = 'I am a Happy Go lucky Guy';
console.log(message.split()); // returns ["I am a Happy Go lucky Guy"]
```

> 💡 Note again, calling the `split()` method on an empty string('') without a splitter will return an array with an empty string. It doesn't return an empty array.

Here are two examples so you can see the difference:

```js
// Returns an empty array
''.split(''); // returns []

// Returns an array with an empty string
''.split() // returns [""]
```

## How to Split a String Using a Non-matching Character

Usually, we use a splitter that is part of the string we are trying to split. There could be cases where you may have passed a splitter that is not part of the string or doesn't match any part of it. In that case, the `split()` method returns an array with the entire string as an element.

In the example below, the message string doesn't have a comma (,) character. Let's try to split the string using the splitter comma (,).

```js
let message = 'I am a Happy Go lucky Guy';
console.log(message.split(',')); // ["I am a Happy Go lucky Guy"]
```

> 💡 You should be aware of this as it might help you debug an issue due to a trivial error like passing the wrong splitter in the `split()` method.

# How to Split with a Limit

If you thought that the `split()` method only takes the splitter as an optional parameter, let me tell you that there is one more. You can also pass the `limit` as an optional parameter to the `split()` method.

```js
string.split(splitter, limit);
```

As the name indicates, the `limit` parameter limits the number of splits. It means the resulting array will only have the number of elements specified by the limit parameter.

In the example below, we split a string using a space (' ') as a splitter. We also pass the number `4` as the limit. `The split()` method returns an array with only four elements, ignoring the rest.

```js
let message = 'I am a Happy Go lucky Guy';
console.log(message.split(' ', 4)); // ["I", "am", "a", "Happy"] 
```

# How to Split Using Regex

We can also pass a regular expression (regex) as the splitter/divider to the `split()` method. Let's consider this string to split:

```js
let message = 'The sky is blue. Grass is green! Do you know the color of the Cloud?';
```

Let's split this string at the period (.), exclamation point (!), and the question mark (?). We can write a regex that identifies when these characters occur. Then we pass the regex to the `split()` method and invoke it on the above string.

```js
let sentences = message.split(/[.,!,?]/);
console.log(sentences);
```

The output looks like this:

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-102.png)
_Split using a Regular Expression_

You can use the `limit` parameter to limit the output to only the first three elements, like this:

```js
sentences = message.split(/[.,!,?]/, 3);
console.log(sentences);
```

The output looks like this:

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-103.png)
_Split using a Regular Expression and Limit value_

> 💡 If you want to capture the characters used in the regular expressions in the output array, you need to tweak the regex a bit. Use parenthesis to capture the matching characters. The updated regex will be `/([.,!,?])/`.

# How to Replace Characters in a String using Split() Method

You can solve many interesting problems using the `split()` method combined with other string and array methods. Let's see one here. It could be a common use case to replace all the occurrences of a character in the string with another character. 

For example, you may want to create the `id` of an HTML element from a name value. The name value may contain a space (' '), but in HTML, the id value must not contain any spaces. We can do this in the following way:

```js
let name = 'Tapas Adhikary';
let subs = name.split(' ');
console.log(subs); // ["Tapas", "Adhikary"]

let joined = subs.join('-');
console.log(joined); // Tapas-Adhikary
```

Consider the name has the first name (Tapas) and last name (Adhikary) separated by a space. Here we first split the name using the space splitter. It returns an array containing the first and last names as elements, that is`['Tapas', 'Adhikary']`.

Then we use the array method called `join()` to join the elements of the array using the `-` character. The `join()` method returns a string by joining the element using a character passed as a parameter. Hence we get the final output as `Tapas-Adhikary`.

# ES6: How to Split with Array Destructuring

ECMAScript2015 (ES6) introduced a more innovative way to extract an element from an array and assign it to a variable. This smart syntax is known as `Array Destructuring`. We can use this with the `split()` method to assign the output to a variable easily with less code.

```js
let name = 'Tapas Adhikary';
let [firstName, lastName] = name.split(' ');
console.log(firstName, lastName);
```

Here we split the name using the space character as the splitter. Then we assign the returned values from the array to a couple of variables (the `firstName` and `lastName`) using the Array Destructuring syntax.

# Before We End...

👋 Do you want to code and learn along with me? You can find the same content here in this YouTube Video. Just open up your favorite code editor and get started.

%[https://www.youtube.com/watch?v=xbHFdstSpvc]

I hope you've found this article insightful, and that it helps you understand JavaScript String's `split()` method more clearly. Please practice the examples multiple times to get a good grip on them. You can find all the [code examples in my GitHub repository](https://github.com/atapas/js-handbook-examples/blob/master/string/split/index.js).

Let's connect. You will find me active on [Twitter (@tapasadhikary)](https://twitter.com/tapasadhikary). Please feel free to give a follow.

You may also like these articles:

* [The JavaScript Array Handbook – JS Array Methods Explained with Examples](https://www.freecodecamp.org/news/the-javascript-array-handbook/)
* [10 DevTools tricks to help you with CSS and UX design](https://blog.greenroots.info/10-devtools-tricks-to-help-you-with-css-and-ux-design-ckpp7mtnu04u6whs143e7huwx)
* [A practical guide to object destructuring in JavaScript](https://blog.greenroots.info/a-practical-guide-to-object-destructuring-in-javascript-cknx6tb2l06yvg1s1425rh54f)
* [10 trivial yet powerful HTML facts you must know](https://blog.greenroots.info/10-trivial-yet-powerful-html-facts-you-must-know-ckmx0d7q30346c1s125iydcsa)
* [10 VS Code emmet tips to make you more productive](https://blog.greenroots.info/10-vs-code-emmet-tips-to-make-you-more-productive-ckknjvxal028f1qs18w20e94t)

