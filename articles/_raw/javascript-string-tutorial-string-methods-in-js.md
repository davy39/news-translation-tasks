---
title: JavaScript String Tutorial – String Methods in JS
subtitle: ''
author: Dario Di Cillo
co_authors: []
series: null
date: '2023-03-10T19:14:14.000Z'
originalURL: https://freecodecamp.org/news/javascript-string-tutorial-string-methods-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/belen-garrido-n642zkjBAEY-unsplash.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "A string is a sequence of characters intended to represent text. Strings\
  \ can contain any kind of character, like letters, numbers, or special characters.\
  \ \nThey are a very useful data type and you will be probably working with them\
  \ frequently. So it's..."
---

A string is a sequence of characters intended to represent text. Strings can contain any kind of character, like letters, numbers, or special characters. 

They are a very useful data type and you will be probably working with them frequently. So it's important to know how to manipulate them efficiently.

In this article, you will learn about:

* The basics of strings in JavaScript
* Common string methods in JavaScript

Let's start.

## The Basics of Strings in JavaScript

Here's a simple definition of a [string](https://www.freecodecamp.org/news/what-is-a-string-in-javascript/):

> In JavaScript, a string is a data type representing a sequence of characters that may consist of letters, numbers, symbols, words, or sentences.

Strings are used to represent text. So, basically, anything that is a [Unicode character](https://unicode.org/charts/).

Let's proceed and see something practical.

### How to create strings in JavaScript

In JavaScript, you can create strings by wrapping the text inside single quotes (`'`), double quotes (`"`), or backticks (```).

```js
// A string created using single quotes
let string1 = 'I am a very cool string! 😎';

// A string created using double quotes
let string2 = "I am a very cool string! 😎";

// A string created using backticks, also known as template literal
let string3 = `I am a very cool string! 😎`;
```

Strings created in this way, as in the example above, are treated equally. You can easily compare them to prove it:

```js
string1 === string2; // true

string1 === string3; // true

string2 === string3; // true
```

Strings created using backticks are also known as _template literals_ and possess special features which we will discuss in a while.

A string created using single quotes, double quotes, or backticks is generated as a **primitive value**, similar to numbers and boolean values. Primitive data are **immutable**, which means they cannot be changed. Also, they do not have any methods or properties.

For your knowledge, there is another way to create strings in JavaScript, which is via the [`String()` constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/String). The `String()` constructor generates a string as an **object** (when called with `new`). If called as a function (`str2` in the example below), the value is [coerced](https://www.freecodecamp.org/news/coercion-and-type-conversion-in-javascript/) to a primitive string.

```js
let str1 = new String('What am I?');
typeof str1; // 'object'

let str2 = String('What am I?');
typeof str2; // 'string'

let str3 = "What am I?";
typeof str3; // 'string'

str1 === str2; // false
str1 === str3; // false
str2 === str3; // true
```

The `typeof` operator returns a string indicating the data type of the operand. This time, although `str1` and `str2` might seem equal, their comparison returns `false`, since they are completely different values.

Note: From now on I will discuss exclusively primitive strings.

## Basic String Manipulation in JavaScript

### String indexing

You can access each character inside a string through its numeric **index** – starting from zero – using bracket notation:

```js
let str = 'larch';
str[0]; // 'l'
str[1]; // 'a'
str[2]; // 'r'
str[3]; // 'c'
str[4]; // 'h'
```

Also, you can use the `charAt()` method to get a specific character inside the string:

```js
str.charAt(0); // 'l'
```

While you can use bracket notation to change _non-primitive_ data, for example, arrays:

```js
let arr = ['birch', 'larch', 'oak'];
typeof arr; // 'object'
arr[2] = 'scots pine';
console.log(arr); // ['birch', 'larch', 'scots pine']
```

You **cannot mutate** a string, since it is a _primitive_ value:

```js
let str = 'larch';
typeof str; // 'string'
str[0] = 'm'; //This could throw an error if you are in strict mode
console.log(str); // 'larch'
```

The value of our `str` variable is still `'larch'` and you cannot do anything to mutate it. This peculiarity of primitive values does not mean that you can't make the `str` variable point to a different value through reassignment:

```js
let str = 'larch';
str = 'march'; // Reassigning str another value
console.log(str); // 'march'

```

Just a note – some of the following examples will use lines from these songs:

* _Always Look on the Bright Side of Life_, lyrics by Eric Idle
* _The Trek_ by Primus
* _The Trees_ by Rush

### The `length` property

You get the number of characters contained in a string using the `length` property:

```js
let sentence = 'Always look on the bright side of life';
sentence.length; // 38
```

The `length` property returns the number of characters the string is composed of, including white spaces. So the last character of our sentence will have the index 37 (the value returned by length -1, because indexing starts at 0).

### String concatenation

You can concatenate (or join) two or more strings using the concatenation operator, `+`. Check out the following example:

```js
let a = 'When candles are out,';
let b = 'all cats are grey.';
let c = a + ' ' + b;
console.log(c); // 'When candles are out, all cats are grey.'
```

Note that I added an extra string between `a` and `b` to give the final sentence the correct spacing.

You can do a similar thing with the use of the addition assignment operator `+=`:

```js
let a = 'When candles are out,';
let b = 'all cats are grey.';
console.log(a += ' '); // 'When candles are out, '
console.log(a += b); // 'When candles are out, all cats are grey.'
```

By doing that, the `a` variable is assigned to its value plus the value on the right side of the operator (`+=`). Now, `a` holds the entire sentence, while in the previous example the complete sentence was stored in another variable, `c`.

If you try to concatenate a number to a string, that number will be coerced to a string value. For example:

```js
console.log('The ' + 3 + ' Musketeers'); // 'The 3 Musketeers'
```

### String comparison

You can compare strings based on their alphabetical order and length using arithmetic comparison operators. The return value is a boolean. 

In the example below, we are comparing two strings according to their alphabetical order:

```js
'Berry' < 'Copper'; // true
// because 'B' comes before 'C'

'Berry' < 'Bingo'; // true
// because the first characters are the same and 'e' comes before 'i'

'berry' < 'Copper'; // false
// because the comparison is case-sensitive and capital letters come first
```

The comparison is performed letter by letter, starting from the first one. And it is actually based on the Unicode order. That's why _C_ comes before _b_ – uppercase letters are placed before lowercase letters inside the Unicode table.

For the same reason, `'$' < '&'` evaluates `true` – _$_ comes before _&_ in the Unicode table.

After letter-by-letter comparison, if each character equates its counterpart in the other string, and the strings have the same length, they are equal. Otherwise, the longest string is the greater. 

In the example below, `quote` lacks the final exclamation mark, so `quoteMark` is greater:

```js
let quote = 'All generalizations are dangerous, even this one';
let quoteMark = 'All generalizations are dangerous, even this one!';
quote < quoteMark; // true
```

If you need to compare the lengths of two strings, you simply use the length property:

```js
quote.length < quoteMark.length; // true
```

### Template literals

Before, we said that template literals (strings created with backticks, ```) have some special features. One is the ability to display the text on multiple lines, easy peasy.

```js
const chorus = `Don't lose heart, comrades
It's over that hill
Paradise is just over that hill`;

console.log(chorus);
//Don't lose heart, comrades
//It's over that hill
//Paradise is just over that hill
```

The displayed text mirrors the spacing used to write the string. That would not have been the case for other literal strings, which require the use of a newline character, `\n`, in order to have the text arranged in a multi-line fashion. For example:

```js
const verse = "There is unrest in the forest\nTrouble with the trees";

console.log(verse);
//There is unrest in the forest
//Trouble with the trees
```

If you want to include a variable inside a string created with single or double quotes, you should make use of concatenation, as seen before.

```js
const dog1 = 'Bach';
const dog2 = 'Bingo';

console.log('My two dogs are called ' + dog1 + ' and ' + dog2 + '.');
// My two dogs are called Bach and Bingo.
```

But template literals provide a feature called **[string interpolation](https://www.freecodecamp.org/news/javascript-string-format-how-to-use-string-interpolation-in-js/)**, that simplifies the readability and makes the code more fluid. 

Here's the previous example rewritten with template literals:

```js
const dog1 = 'Bach';
const dog2 = 'Bingo';

console.log(`My two dogs are called ${dog1} and ${dog2}.`);
// My two dogs are called Bach and Bingo.
```

In short, you assemble the string by substituting the content of placeholders, `${}`, which is added to the text.

In the example above, each placeholder contains a variable, but placeholders can hold any expression whose value will be converted to a string, building the final string.

## Common String Methods in JavaScript

As we said previously, primitive data does not have methods and properties. Hey, what about the `length` property we used before? And the `charAt()` method? And what about this section?!

Primitive data does not have methods or properties, indeed. But when you call a method on a string, or access a property, JavaScript generates a wrapper object under the hood. In the end, methods and properties perform their job on this wrapper object. After the use, the wrapper object is disposed.

So, it turns out we do have something to discuss in this section. Here are some of the most common string methods in JavaScript with examples.

### The `concat()` method

The effect of the `concat()` method is very similar to using the `+` and `+=` operators. It concatenates one or more strings passed as arguments to the string on which the method is called, returning the concatenated string.

Let's rewrite the example from the [concatenation](#heading-string-concatenation) section:

```js
let a = 'When candles are out,';
let b = 'all cats are grey.';
let c = a.concat(' ', b);
console.log(c); // 'When candles are out, all cats are grey.'
```

### The `toLowerCase()` & `toUpperCase()` methods

Sometimes, you might need to manipulate the letter case of specific strings to compare them properly, store inputs with a certain uniformity, or for other reasons.

As their names may suggest, `toLowerCase()` and `toUpperCase()` convert a string to lowercase and uppercase letters, respectively. These methods don't change the original string.

```js
let sentence = 'Always look on the bright side of life';

console.log(sentence.toLowerCase());
// always look on the bright side of life

console.log(sentence.toUpperCase());
// ALWAYS LOOK ON THE BRIGHT SIDE OF LIFE
```

### The `includes()` method

The `includes()` method checks if a specified string, passed as an argument, is present inside another string. The search is case-sensitive and the return value is a boolean.

Also, you can specify a second argument stating the index at which to start searching for the specified string.

```js
let sentence = 'Always look on the bright side of life';
sentence.includes('look up'); // false 
sentence.includes('look on'); // true
sentence.includes('look on', 8); // false
```

### The `indexOf()` methods

The `indexOf()` method searches for a substring and returns the first occurrence of the substring inside the calling string. It takes an optional parameter, indicating a specific index to start searching. For example:

```js
let sentence = 'Always look on the bright side of life';

sentence.indexOf('l'); // 1
sentence.indexOf('l', 2); // 7
sentence.indexOf('l', 8); // 34
sentence.indexOf('L'); // -1
```

`indexOf()` returns the index of the first occurrence of the substring. If the substring is not found, it returns `-1`. Keep in mind that the search is case-sensitive. That's why `sentence.indexOf('L')` in the example above returns `-1`.

### The `startsWith()` & `endsWith()` methods

The `startsWith()` method checks if a string begins with a specific sequence of characters and returns a boolean value. The search is case-sensitive.

The method takes an optional argument indicating the position in which to start searching for the specified string.

```js
let dish = 'Lemon curry';
dish.startsWith('Lem'); // true
dish.startsWith('lem'); // false
dish.toLowerCase().startsWith('lem'); // true
dish.startsWith('cu'); // false
dish.startsWith('cu', 6); // true
```

Similarly, the `endsWith()` method checks if a string ends with a specific sequence of characters, returning a boolean value. Also in this case the search is case-sensitive.

The optional argument indicates the expected end position of the specified substring (the index of the expected final character + 1).

```js
let dish = 'Lemon curry';
dish.endsWith('ry'); // true
dish.endsWith('on', 5); // true
```

### The `slice()` & `substring()` methods

The `slice()` and `substring()` methods pull a portion of a string, returning it as a new string. They do not change the content of the original string.

The first argument passed to each method is the index of the first character to include in the string to extract. The second argument is the index of the first character to exclude. For example:

```js
let sentence = 'Always look on the bright side of life';

sentence.slice(7); // 'look on the bright side of life'
sentence.substring(7); // 'look on the bright side of life'
sentence.slice(0, 6); // 'Always'
sentence.substring(0, 6); // 'Always'
```

These two methods are almost identical, except for a few differences. One of them is that if the first index passed to `substring()` is greater than the second index, the two arguments are exchanged so that a string is still returned. In the same scenario, the `slice()` method returns an empty string instead:

```js
let sentence = 'Always look on the bright side of life';

sentence.substring(11, 7); // 'look'
sentence.slice(11, 7); // ''
```

### The `split()` method

The `split()` method takes a separator argument and breaks a string up, according to the occurrence of the separator character inside the string. Then, it returns an array of strings.

It also takes an optional argument, indicating the maximum number of items to put inside the array. For example:

```js
let sentence = 'Always look on the bright side of life';

sentence.split(' '); // ['Always', 'look', 'on', 'the', 'bright', 'side', 'of', 'life']
sentence.split(' ', 5); // ['Always', 'look', 'on', 'the', 'bright']
```

### The `match()` method

The `match()` method searches for a specific pattern – passed as a regular expression – inside a string, and returns an array containing the matching results. For example:

```js
const tongueTwister = "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"
const regex1 = /(w|c)o*(ul)?d/g;
const regex2 = /wool/g;
tongueTwister.match(regex1);
// ['wood', 'would', 'wood', 'wood', 'could', 'wood']
tongueTwister.match(regex2);
// null

```

If you only need to know if a pattern is present or not inside a string, you should use `test()`.

### The `test()` method

The `test()` method searches for a specific pattern – passed as a regular expression – inside a string, and returns a boolean. The syntax is reversed respective to `match()`. 

Considering the previous example, using the `test()` method would look like this:

```js
const tongueTwister = "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"
const regex1 = /(w|c)o*(ul)?d/g;
const regex2 = /wool/g;
regex1.test(tongueTwister); // true
regex2.test(tongueTwister); // false

```

## Wrapping up

A string is a sequence of characters that represents text. In JavaScript, strings are primitive data. You can create them by wrapping the text inside single quotes, double quotes, or backticks.

Template literals enable you to write cleaner code thanks to string interpolation, and when you need multi-line strings.

Strings are everywhere, so you will need to know how to manipulate them efficiently. In this tutorial, you have learned about the most common string methods you will use to work with strings. But there are many more for you to discover!

Happy learning :)

