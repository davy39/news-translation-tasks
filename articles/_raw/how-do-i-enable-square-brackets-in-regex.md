---
title: How do I Enable Square Brackets in RegEx?
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-04-27T12:31:45.000Z'
originalURL: https://freecodecamp.org/news/how-do-i-enable-square-brackets-in-regex
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/regexSquareBrackets.png
tags:
- name: Regex
  slug: regex
seo_title: null
seo_desc: 'In this article, you’ll learn about what square brackets do in regular
  expressions, how to use them for specifying ranges, and how to match them as a character.

  What Does Square Bracket Do in RegEx?

  In regular expressions, square brackets ([ ]) are c...'
---

In this article, you’ll learn about what square brackets do in regular expressions, how to use them for specifying ranges, and how to match them as a character.


## What Does Square Bracket Do in RegEx?
In regular expressions, square brackets (`[ ]`) are characters that have a special meaning of their own. Since they have a special meaning, you can call them "metacharacter".  Square brackets help you to define a character set, which is a set of characters you want to match.

For example, `[aeiou]` would match all vowels

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-27-at-11.44.03.png)
_Vowel Matches with Square Brackets in RegEx_

In addition to that, some characters may have special meanings inside square brackets.

For instance, if you put a caret (`^`) before any other character inside square brackets, it means you’re negating the characters that follow the caret. That is, **you’re telling the regex engine or your programming language not to match those characters**.

In the screenshot below, I matched all non-vowels and spaces by negating all vowels inside a square bracket.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-27-at-11.44.47.png)
_Negating all Non-Vowels and Spaces with Square Brackets in RegEx_

In another instance, if you put in hyphen (`-`) between two characters inside square brackets, it means **range**.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-27-at-11.47.35.png)
_Specifying Range with Square Brackets in RegEx_

But there are some situations where you want to match the square brackets as a character of their own. Let’s look at how to do that next – the purpose of this article.


## How to Enable Square Brackets in RegEx
If you find yourself in a situation where you want to match square brackets, for example, like you have to do when matching special characters for passwords, **you need to escape them**.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-27-at-11.50.20.png)
_Matching Square Brackets in RegEx_

## How to Use Square Brackets and Enable them in JavaScript
JavaScript works fine with square brackets as metacharacters and a character of their own.

```js
const text =
  'This is the opening square bracket [ and this is the closing square bracket ] Both [ and ] are everyday part of regex';

const regex = /\[|\]/g;

console.log(regex.test(text)); //true
```

You can take it further and loop through the matches by using the `exec()` method and `while` loop:

```js
const text =
  'This is the opening square bracket [ and this is the closing square bracket ] Both [ and ] are everyday part of regex';

const regex = /\[|\]/g;

let match;
while ((match = regex.exec(text)) !== null) {
  console.log('A match:', match[0], 'at Index:', match.index);
}
```
![Screenshot-2023-04-27-at-12.14.23](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-27-at-12.14.23.png)


## Conclusion
This article showed you how to use square brackets as metacharacters and a character of their own in Regex engines and JavaScript.

It's important to keep in mind that some programming languages or regex engines may have slightly different syntax or rules for using square brackets and other metacharacters in regex. So, if you’re using square brackets with other regex engines and programming languages apart from JavaScript, make sure you understand how they work with the square brackets.

Keep coding!


