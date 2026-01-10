---
title: How to Include an Empty String in RegEx
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-03-31T11:50:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-include-empty-string-in-regex
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/start-graph--7-.png
tags:
- name: Regex
  slug: regex
seo_title: null
seo_desc: "Regular expressions (RegEx or RegExp for short) are a sequence of characters\
  \ that define a search pattern. \nYou can use them to search, replace, and validate\
  \ the strings of a text in a wide variety of applications, such as text editors,\
  \ developer too..."
---

Regular expressions (RegEx or RegExp for short) are a sequence of characters that define a search pattern. 

You can use them to search, replace, and validate the strings of a text in a wide variety of applications, such as text editors, developer tools, and command line tools.

RegEx is also widely used in programming languages because many of the languages have built-in support for it.

Since you can match the strings of a text with RegEx, it means you can also match empty strings. 

In this article, I’ll show you three ways to match an empty string in RegEx.

## What We'll Cover
- [How to Match Empty String in RegEx with the Caret and Dollar Sign Metacharacters](#heading-how-to-match-empty-string-in-regex-with-the-caret-and-dollar-sign-metacharacters)
- [How to Match Empty String in RegEx with a Lookahead](#heading-how-to-match-empty-string-in-regex-with-a-lookahead)
- [How to Match Empty String in RegEx with a Negative Lookahead](#heading-how-to-match-empty-string-in-regex-with-a-negative-lookahead)
- [Conclusion](#heading-conclusion)


## How to Match Empty String in RegEx with the Caret and Dollar Sign Metacharacters
The caret (`^`) and dollar sign (`$`) metacharacters match the start of a string and its end, respectively.
![Screenshot-2023-03-31-at-08.22.21](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-31-at-08.22.21.png)

So, if you don’t put anything between both `^` and `$`, it matches an empty string:

```console
^$
```


## How to Match Empty String in RegEx with a Lookahead
In RegEx, a lookahead is a zero-width assertion that allows you to match a string only if it is followed by another specific string without including that specific string in the match result. 

There are both positive and negative lookaheads in RegEx. `?=` indicates a positive lookahead and `?!` indicates a negative lookahead. You can use them to create more complex regular expressions.

Let’s look at how to match an empty string with a positive lookahead:

```console
^(?=\s*$)
```

In the pattern above:
* the `^` character matches the beginning of the string
* the `(?=\s*$)` is a positive lookahead that matches a position in the string where the following is true:
* `\s*` matches zero or more whitespace characters
* `$` matches the end of the string

Since the lookahead only matches the position and not any characters, the regular expression will match only an empty string.


## How to Match Empty String in RegEx with a Negative Lookahead
As I mentioned earlier, `?!` specifies a negative lookahead. You can use the negative lookahead below to match an empty string:

```console
^(?!.*\S)
```

In the RegEx above:
* the `^` character matches the beginning of the string
* the `(?!.*\S)` is a negative lookahead that matches a position in the string where the following is not true:
* `.*` matches zero or more characters
* `\S` matches any non-whitespace character

Since the negative lookahead only matches the position and not any characters, the regular expression will match an empty string.


## Conclusion
In many RegEx testing engines, you won’t get a match for an empty string if you test an empty string with start and end metacharacters, negative lookahead, and positive lookahead.
![Screenshot-2023-03-31-at-09.19.48](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-31-at-09.19.48.png)

But in JavaScript, for example, you’ll get a match:
```js
// Start and end metacharacters
const regEx1 = /^$/g;

// Positive lookahead
const regEx2 = /^(?=\s*$)/g;

// Negative lookahead
const regEx3 = /^(?!.*\S)/g;

const text = '';

console.log(regEx1.exec(text)); // [ '', index: 0, input: '', groups: undefined ]
console.log(regEx2.exec(text)); // [ '', index: 0, input: '', groups: undefined ]
console.log(regEx3.exec(text)); // [ '', index: 0, input: '', groups: undefined ]

console.log('\n');

console.log(regEx1.test(text)); // true
console.log(regEx2.test(text)); // true
console.log(regEx3.test(text)); // true
```

Happy coding!


