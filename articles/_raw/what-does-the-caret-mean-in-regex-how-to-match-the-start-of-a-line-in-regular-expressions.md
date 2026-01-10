---
title: What Does the Caret Mean in RegEx? Caret Metacharacter in Regular Expressions
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-04-20T16:47:22.000Z'
originalURL: https://freecodecamp.org/news/what-does-the-caret-mean-in-regex-how-to-match-the-start-of-a-line-in-regular-expressions
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/caretMeta.png
tags:
- name: Regex
  slug: regex
seo_title: null
seo_desc: "A caret (^) is one of the many symbols for creating patterns in regular\
  \ expressions. \nA caret matches the start of a line or a particular string. But\
  \ that’s not all there is to the caret (^) symbol.\nThe caret symbol (^) is often\
  \ referred to as an \"an..."
---

A caret (`^`) is one of the many symbols for creating patterns in regular expressions. 

A caret matches the start of a line or a particular string. But that’s not all there is to the caret (`^`) symbol.

The caret symbol (`^`) is often referred to as an "anchor" because it anchors the pattern to the beginning of a line or string.  So, you can call it "start of line anchor". 

The other anchor is the dollar sign (`$`), which anchors the pattern to the end of the line, which means it is "end of line anchor".


## What We'll Cover
- [What Does the Caret Symbol Do in RegEx](#heading-what-does-the-caret-symbol-do-in-regex)
- [How to Match the Start of a Line with Caret](#heading-how-to-match-the-start-of-a-line-with-caret)
- [How to Negate a Character Set with Caret](#heading-how-to-negate-a-character-set-with-caret)
- [How to Match the Caret as a Character in a String](#heading-how-to-match-the-caret-as-a-character-in-a-string)
- [How to Use the Caret Metacharacter in JavaScript](#heading-how-to-use-the-caret-metacharacter-in-javascript)
- [Conclusion](#heading-conclusion)


## What Does the Caret Symbol Do in RegEx?
There are two main things the caret symbol does – it matches the start of a line or the start of a string, and it negates a character set when you put it inside the square brackets.

In addition, you might want to match the caret symbol itself since it's used for other things outside of regular expressions. In that case, you have to escape it.


## How to Match the Start of a Line with Caret
To match the start of a line with the caret symbol, prepend your pattern with it.

In the example below, I have the pattern `/^hello\s*world/igm` which would only match a `hello world` text that is at the start of a line. Any other `hello world` in between or at the end of a line won’t be a match:
![Screenshot-2023-04-20-at-14.21.33](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-20-at-14.21.33.png)

Also, the pattern `/^c/igm` would only match the words that start with the letter `c` only if they are at the start of the line:
![Screenshot-2023-04-20-at-14.22.33](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-20-at-14.22.33.png)


## How to Negate a Character Set with Caret
Another thing you can do with the caret is to negate a character set. For example, if you want to negate vowels, you can put them in a character set and prepend caret to them:
![Screenshot-2023-04-20-at-14.29.46](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-20-at-14.29.46.png)

You can see that all the vowels were not matched.


## How to Match the Caret as a Character in a String
You can use caret for other things like exponentiation in Mathematics and bitwise XOR operator in C++. 

If you want to match it, you have to escape it with a backslash `\` since its recognized as a metacharacter by RegEx engines:
![Screenshot-2023-04-20-at-14.39.07](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-20-at-14.39.07.png)


## How to Use the Caret Metacharacter in JavaScript
The caret metacharacter works fine in JavaScript. The code snippet below shows I test it with some strings:

```js
const text1 = `There's hello world in every programming language
Hello world is what starts many programming language courses.
Many programmers don't know any other hello apart from hello world.`;

const text2 = `caret is anchors your pattern to the start of a line
To match the caret itself, you have to escape it.`;

const text3 = '4 raised to power 2 in mathematics is 4 ^ 2';

const re1 = /^hello\s*world/gim;
const re2 = /^c/gim;
const re3 = /\^/;

console.log(re1.test(text1)); //true
console.log(re2.test(text2)); //true
console.log(re3.test(text3)); //true
```


## Conclusion
This article showed you how you can use the "start of line anchor" (caret `^` metacharacter) to anchor a pattern to the start of a line or string in both RegEx engines and JavaScript.

To learn about the end of line anchor (`$`), you can read [this article](https://www.freecodecamp.org/news/what-does-mean-in-regex/).

Happy coding!


