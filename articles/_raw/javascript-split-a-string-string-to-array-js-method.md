---
title: JavaScript split() a String – String to Array JS Method
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2022-01-10T21:24:30.000Z'
originalURL: https://freecodecamp.org/news/javascript-split-a-string-string-to-array-js-method
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/pankaj-patel-1IW4HQuauSU-unsplash.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "If you need to split up a string into an array of substrings, then you\
  \ can use the JavaScript split() method. \nIn this article, I will go over the JavaScript\
  \ split() method and provide code examples. \nBasic Syntax of the split() method\n\
  Here is the sy..."
---

If you need to split up a string into an array of substrings, then you can use the JavaScript `split()` method. 

In this article, I will go over the JavaScript `split()` method and provide code examples. 

## Basic Syntax of the split() method

Here is the syntax for the JavaScript `split()` method.

```js
str.split(optional-separator, optional-limit)
```

The optional separator is a type of pattern that tells the computer where each split should happen. 

The optional limit parameter is a positive number that tells the computer how many substrings should be in the returned array value.

## JavaScript split() method code examples

In this first example, I have the string `"I love freeCodeCamp"`. If I were to use the `split()` method without the separator, then the return value would be an array of the entire string.

```js
const str = 'I love freeCodeCamp';

str.split();
// return value is ["I love freeCodeCamp"]
```

### Examples using the optional separator parameter

If I wanted to change it so the string is split up into individual characters, then I would need to add a separator. The separator would be an empty string.

```js
const str = 'I love freeCodeCamp';

str.split('');
// return value ["I", " ", "l", "o", "v", "e", " ", "f", "r", "e", "e", "C", "o", "d", "e", "C", "a", "m", "p"]
```

Notice how the spaces are considered characters in the return value.

If I wanted to change it so the string is split up into individual words, then the separator would be an empty string with a space.

```js
const str = 'I love freeCodeCamp';

str.split(' ');
// return value ["I", "love", "freeCodeCamp"]
```

### Examples using the optional limit parameter

In this example, I am going to use the limit parameter to return an array of just the first word of the sentence `"I love freeCodeCamp"`.

```js
const str = 'I love freeCodeCamp';

str.split(' ',1);
// return value ["I"]
```

If I change the limit to be zero, then the return value would be an empty array.

```js
const str = 'I love freeCodeCamp';

str.split(' ',0);
//return value []
```

## Should you use the split() method to reverse a string?

The reverse a string exercise is a very popular coding challenge.  One common way to solve it involves using the `split()` method. 

In this example, we have the string "freeCodeCamp".  If we wanted to reverse the word, then we can chain together the `split()`, `reverse()` and `join()` methods to return the new reversed string.

```js
const str = 'freeCodeCamp';

str.split('').reverse().join('');
//return value "pmaCedoCeerf"
```

The `.split('')` portion splits up the string into an array of characters.

The `.reverse()` portion reverses the array of characters in place.

The `.join('')` portion joins the characters together from the array and returns a new string.

This approach seems to work fine for this example. But there are special cases where this would not work.

Let's take a look at the example provided in the [MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split).

If we tried to reverse the string "mañana mañana", then it would lead to unexpected results.

```js
const str = 'mañana mañana'
const reversedStr = str.split('').reverse().join('')

console.log(reversedStr)
// return value would be "anãnam anañam"
```

Notice how the tilde(~) is placed over the letter `"a"` instead of `"n"` in the reversed word. This happens because our string contains what is called a grapheme. 

A grapheme cluster is a series of symbols combined to produce one single character that humans can read on screen. When we try to reverse the string using these types of characters, the computer can misinterpret these characters and produce an incorrect version of the reversed string.

If we just isolate the split method, you can see how the computer is breaking up each individual character.

```js
const str = 'mañana mañana'

console.log(str.split(''))
//["m", "a", "ñ", "a", "n", "a", " ", "m", "a", "n", "̃", "a", "n", "a"]
```

There are [packages](https://github.com/mathiasbynens/esrever) that you can use in your projects to fix this issue and reverse the string correctly if you are using these special characters. 

## Conclusion

The JavaScript `split()` method is used to split up a string into an array of substrings.

Here is syntax for the JavaScript `split()` method.

```js
str.split(optional-separator, optional-limit)
```

The optional separator is a type of pattern that tells the computer where each split should happen. 

The optional limit parameter is a positive number that tells the computer how many substrings should be in the returned array value.

You could use the split method to reverse a string, but there are special cases where this would not work. If your string contains grapheme clusters, then the result might produce an incorrectly reversed word. 

You could also choose to use the spread syntax to split up the string before reversing it.

```js
const str = 'mañana mañana'
console.log([...str].reverse().join(""))
```

I hope you enjoyed this article and best of luck on your JavaScript journey. 

