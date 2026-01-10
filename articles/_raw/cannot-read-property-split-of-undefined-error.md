---
title: Cannot Read Property 'split' of Undefined
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-02T02:16:00.000Z'
originalURL: https://freecodecamp.org/news/cannot-read-property-split-of-undefined-error
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9aa5740569d1a4ca26db.jpg
tags:
- name: error
  slug: error
- name: JavaScript
  slug: javascript
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'If you''ve ever used JavaScript''s split method, there''s a good chance
  that you''ve encountered the following error: TypeError: Cannot read property ''split''
  of undefined.

  There are a few reasons why you would receive this error. Most likely it''s just
  a ...'
---

If you've ever used JavaScript's `split` method, there's a good chance that you've encountered the following error: `TypeError: Cannot read property 'split' of undefined`.

There are a few reasons why you would receive this error. Most likely it's just a basic misunderstanding of how `split` works and how to iterate through arrays.

For example, if you try to submit the following code for the [Find the Longest Word in a String challenge](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-algorithm-scripting/find-the-longest-word-in-a-string):

```js
function findLongestWord(str) { 
  for(let i = 0; i < str.length; i++) {
    const array = str.split(" ");
    array[i].split("");
  }
}

findLongestWord("The quick brown fox jumped over the lazy dog");
```

it will throw the `TypeError: Cannot read property 'split' of undefined` error.

### The `split` method

When `split` is called on a string, it splits the string into substrings based on the separator passed in as an argument. If an empty string is passed as an argument, `split` treats each character as a substring. It then returns an array containing the substrings:

```js
const testStr1 = "Test test 1 2";
const testStr2 = "cupcake pancake";
const testStr3 = "First,Second,Third";

testStr1.split(" "); // [ 'Test', 'test', '1', '2' ]
testStr2.split(""); // [ 'c', 'u', 'p', 'c', 'a', 'k', 'e', ' ', 'p', 'a', 'n', 'c', 'a', 'k', 'e' ]
testStr3.split(","); // [ 'First', 'Second', 'Third' ]

```

Check out [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split) for more details about `split`.

### The problem explained with examples

Knowing what the `split` method returns and how many substrings you can expect is the key to solving [this challenge](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-algorithm-scripting/find-the-longest-word-in-a-string).

Let's take another look at the code above and see why it's not working as expected:

```js
function findLongestWord(str) { 
  for(let i = 0; i < str.length; i++) {
    const array = str.split(" ");
    array[i].split("");
  }
}

findLongestWord("The quick brown fox jumped over the lazy dog");

```

Splitting `str` into an array like this (`const array = str.split(" ");`) works as expected and returns `[ 'The',   'quick',   'brown',   'fox',   'jumped',   'over',   'the',   'lazy',   'dog' ]`.

But take a closer look at the `for` loop. Rather than using the length of `array` as a condition to iterate `i`, `str.length` is used instead. 

`str` is "The quick brown fox jumped over the lazy dog", and if you log `str.length` to the console, you'll get 44.

The last statement in the body of the `for` loop is what's causing the error: `array[i].split("");`. The length of `array` is 9, so `i` would quickly go way over the maximum length of `array`:

```js
function findLongestWord(str) { 
  for(let i = 0; i < str.length; i++) {
    const array = str.split(" ");
    console.log(array[i]);
    // array[0]: "The"
    // array[1]: "quick"
    // array[2]: "brown"
    // ...
    // array[9]: "dog"
    // array[10]: undefined
    // array[11]: undefined
  }
}

findLongestWord("The quick brown fox jumped over the lazy dog");

```

Calling `array[i].split("");` to split each string into substrings of characters is a valid approach, but it will throw `TypeError: Cannot read property 'split' of undefined` when it's passed `undefined`.

### How to solve Find the Longest Word in a String with `split`

Let's quickly go over some pseudo code for how to solve this problem:

1. Split `str` into an array of individual words
2. Create a variable to track the greatest word length
3. Iterate through the array of words and compare the length of each word to the variable mentioned above
4. If the length of the current word is greater than the one stored in the variable, replace that value with the current word length
5. Once the length of every word is compared with the maximum word length variable, return that number from the function

First, split `str` into an array of individual words:

```js
function findLongestWordLength(str) {
  const array = str.split(" ");
}
```

Create a variable to keep track of the longest word length and set it to zero:

```js
function findLongestWordLength(str) {
  const array = str.split(" ");
  let maxWordLength = 0;
}
```

Now that the value of `array` is `['The', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog']`, you can use `array.length` in your `for` loop:

```js
function findLongestWordLength(str) {
  const array = str.split(" ");
  let maxWordLength = 0;
  
  for (let i = 0; i < array.length; i++) {
    
  }
}
```

Iterate through the array of words and check the length of each word. Remember that strings also have a `length` method you can call to easily get the length of a string:

```js
function findLongestWordLength(str) {
  const array = str.split(" ");
  let maxLength = 0;
  
  for (let i = 0; i < array.length; i++) {
    array[i].length;
  }
}
```

Use an `if` statement check if the length of the current word (`array[i].length`) is greater than `maxLength`. If so, replace the value of `maxLength` with `array[i].length`:

```js
function findLongestWordLength(str) {
  const array = str.split(" ");
  let maxLength = 0;
  
  for (let i = 0; i < array.length; i++) {
    if (array[i].length > maxLength) {
      maxLength = array[i].length;
    }
  }
}
```

Finally, return `maxLength` at the end of the function, after the `for` loop:

```js
function findLongestWordLength(str) {
  const array = str.split(" ");
  let maxLength = 0;
  
  for (let i = 0; i < array.length; i++) {
    if (array[i].length > maxLength) {
      maxLength = array[i].length;
    }
  }
    
  return maxLength;
}
```

