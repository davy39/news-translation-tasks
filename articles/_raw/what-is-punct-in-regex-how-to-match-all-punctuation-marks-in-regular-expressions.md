---
title: What is Punct in RegEx? How to Match All Punctuation Marks in Regular Expressions
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-04-28T11:28:37.000Z'
originalURL: https://freecodecamp.org/news/what-is-punct-in-regex-how-to-match-all-punctuation-marks-in-regular-expressions
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/matchPunctuationRegEx.png
tags:
- name: Regex
  slug: regex
seo_title: null
seo_desc: "In regular expressions, \"punct\" means punctuation marks. It is all non-word\
  \ and non-space characters. \"Punct\" is a predefined character class in regular\
  \ expressions, and you can use it in any regex flavor that supports it. \nThe Punct\
  \ character class ..."
---

In regular expressions, "punct" means punctuation marks. It is all non-word and non-space characters. "Punct" is a predefined character class in regular expressions, and you can use it in any regex flavor that supports it. 

The `Punct` character class is denoted by `\p{Punct}` or simply `\p{P}`. It matches any punctuation mark in a string. This includes characters such as periods, commas, exclamation marks, and quotation marks. 

Since there’s a way you can match all punctuation marks, that’s what we are going to look at in this article.


## How to Match all Punctuation Marks in RegEx Engines
Few regex engines out there have regex flavors that support `\p{P}`. So, for those that support it, `\p{P}` would match all punctuation marks in them.
![Screenshot-2023-04-28-at-08.07.14](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-28-at-08.07.14.png)

For regex engines that don’t support `\p{P}`, you can match all punctuation marks by negating word characters and space characters with the pattern `[^\w\s]+`:
![Screenshot-2023-04-28-at-08.10.24](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-28-at-08.10.24.png)


## How to Match all Punctuation Marks in JavaScript RegEx
If you want to use the pattern `\p{P}` to match all punctuation marks in JavaScript, you have to assign it the Unicode flag like this `/\p{P}/u`. Otherwise, it won’t work. Let’s see that in action:

```js
const text = `That said, Kolade, you don't have to forget to take home things you buy at the store again. Do you understand?

I just said that to show you that the pattern really matches punctuation marks. I don't forget things at the store. Here are other punctuation marks:! " # $ % & ' ( ) * + , - . / : ; | < = > { } ? @ [ \ ] ^ _ `;

const regex1 = /\p{P}/gu;
const regex2 = /[^\w\s]+/g;

console.log(regex1.test(text)); //true
console.log(regex2.test(text)); //true

console.log(regex1.exec(text));
console.log(regex2.exec(text));
```

Since `exec()` would only return one match and `test()` would only return a Boolean, you can loop through the matches with `exec()` and `while` loop to see all of them:

```js
const text = `That said, Kolade, you don't have to forget to take home things you buy at the store again. Do you understand?

I just said that to show you that the pattern really matches punctuation marks. I don't forget things at the store. Here are other punctuation marks:! " # $ % & ' ( ) * + , - . / : ; | < = > { } ? @ [ \ ] ^ _ `;

const regex1 = /\p{P}/gu;
const regex2 = /[^\w\s]+/g;

let match;

while ((match = regex1.exec(text)) !== null) {
  console.log('A match: ', match[0], 'at index: ', match.index);
}
```
![Screenshot-2023-04-28-at-08.28.30](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-28-at-08.28.30.png)


## Conclusion
That’s how you can match all punctuation marks in regex engines and JavaScript. Don’t forget that if you’re using `\p{P}` to match punctuation marks, you have to use it with the Unicode flag like this `/\p{P}/u`. You can also apply the same to other programming languages.

If you want to learn more about regular expressions, you can use [this video](https://www.youtube.com/watch?v=ZfQFUJhPqMM) made by Beau Carnes of freeCodeCamp.

Keep coding!


