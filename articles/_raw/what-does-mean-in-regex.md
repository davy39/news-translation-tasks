---
title: What Does $ Mean in RegEx? Dollar Metacharacter in Regular Expressions
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-04-19T11:20:42.000Z'
originalURL: https://freecodecamp.org/news/what-does-mean-in-regex
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/start-graph--10-.png
tags:
- name: Regex
  slug: regex
seo_title: null
seo_desc: 'The $ symbol is one of the most commonly used symbols in RegEx. It is used
  to match the end of a string. In other words, you can call it "end of line anchor",
  since it anchors a pattern to the end of the line.

  In this article, I’ll show you exactly w...'
---

The `$` symbol is one of the most commonly used symbols in RegEx. It is used to match the end of a string. In other words, you can call it "end of line anchor", since it anchors a pattern to the end of the line.

In this article, I’ll show you exactly what the dollar sign (`$`) does in RegEx and how to use it.


## What We'll Cover
- [What is the `$` Symbol in RegEx?](#heading-what-is-the-symbol-in-regex)
- [How to Match the Dollar Sign `$` in RegEx](#heading-how-to-match-the-dollar-sign-in-regex)
- [How to Use the Dollar Sign `$` in a JavaScript Regex](#heading-how-to-use-the-dollar-sign-in-a-javascript-regex)
- [Conclusion](#heading-conclusion)


## What is the `$` Symbol in RegEx?
The `$` is one of the RegEx characters known as metacharacters. It matches the end of a string and would only return a match when the text or string it is attached to is at the end of a line.

This is useful in cases where you want to ensure that a string ends with a certain pattern or character. You can use the `$` metacharacter with other metacharacters to create complex patterns that match specific strings or patterns within strings.

In the example below, you can see that the pattern is `freecodecamp$` with the `i`, `g`, and `m` flags. `i` means case insensitive, `g` means global, and `m` means multiline.
![Screenshot-2023-04-19-at-10.46.29](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-19-at-10.46.29.png)

You can also see that only the word `freeCoceCamp` at the end of a line is returned as matches. That’s the power of the `$` metacharacter.


## How to Match the Dollar Sign `$` in RegEx
Since the dollar sign `$` is a metacharacter, how would you match it in a string? You have to escape it with a backslash! That’s how you match all metacharacters in RegEx.
![Screenshot-2023-04-19-at-10.46.37](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-19-at-10.46.37.png)

## How to Use the Dollar Sign `$` in a JavaScript Regex
The dollar sign `$` metacharacter works fine in JavaScript. In the code snippet below, I test the dollar sign as a metacharacter and as a string:

```js
const text1 =
  "At freeCodeCamp, we don't ask you to pay to learn coding, because freeCodeCamp is a charity";

const text2 =
  'You can also hang out with friends on a forum developed by freeCodeCamp';

const text3 = 'The sign of the naira is ₦ and dollar sign is $.';

const regex1 = /freecodecamp$/gim;
const regex2 = /\$/g;

// test the dollar sign as a metacharacter
console.log(regex1.test(text1)); //false
console.log(regex2.test(text2)); //true

// test the dollar sign as a string
console.log(regex2.test(text3)); //true
```

You can see that when I tested the string ` At freeCodeCamp, we don't ask you to pay to learn coding, because freeCodeCamp is a charity ` with the regex `/freecodecamp$/gim;`, it returned `false` because there’s no `freeCodeCamp` at the end of a line. But when I tested ` You can also hang out with friends on a forum developed by freeCodeCamp'` with the same regex, it returned `true` because there’s a `freeCodeCamp` at the end of a line.

Also, you can see that the string `'The sign of the naira is ₦ and dollar sign is $.'` returned `true` when I tested it with the regex `/\$/g`.

You can also use the `exec()` method instead of `test()` to see the exact matches of your regex:

```js
const text1 =
  "At freeCodeCamp, we don't ask you to pay to learn coding, because freeCodeCamp is a charity";

const text2 =
  'You can also hang out with friends on a forum developed by freeCodeCamp';

const text3 = 'The sign of the naira is ₦ and dollar sign is $.';

const regex1 = /freecodecamp$/gim;
const regex2 = /\$/g;

// test the dollar sign as a metacharacter
console.log(regex1.exec(text1));
console.log(regex1.exec(text2));

// test the dollar sign as a string
console.log(regex2.exec(text3));
```

Output:
```js
null
[
  'freeCodeCamp',
  index: 59,
  input: 'You can also hang out with friends on a forum developed by freeCodeCamp',
  groups: undefined
]
[
  '$',
  index: 46,
  input: 'The sign of the naira is ₦ and dollar sign is $.',
  groups: undefined
]
```

The first console log returned `null` because there was no match. The second returned the match, and the third returned the match too.


## Conclusion
You’ve seen how the dollar (`$`) metacharacter matches the end of a line in RegEx and in JavaScript.

You can combine the dollar metacharacter with several other metacharacters to create a complex pattern. For instance, since caret (`^`) matches the start of a line, you can combine it with the dollar metacharacter to match a particular word only.

Happy coding!


