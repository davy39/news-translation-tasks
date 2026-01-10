---
title: How Do I Make RegEx Optional? Specify Optional Pattern in Regular Expressions
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-03-09T11:34:42.000Z'
originalURL: https://freecodecamp.org/news/how-do-i-make-regex-optional-specify-optional-pattern-in-regular-expressions
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/start-graph--5-.png
tags:
- name: Regex
  slug: regex
seo_title: null
seo_desc: 'Regular expressions are greedy by default, meaning they try to match as
  many strings as possible. One of the ways to write accurate regular expressions
  is to make them as lazy as possible.

  The metacharacter that helps achieve laziness is the question...'
---

Regular expressions are greedy by default, meaning they try to match as many strings as possible. One of the ways to write accurate regular expressions is to make them as lazy as possible.

The metacharacter that helps achieve laziness is the question mark `?`. It helps you make any RegEx pattern optional.

In this article, we’ll take a look at the question mark metacharacter and how you can make any RegEx pattern optional with it.


## What is the Question Mark `?` Metacharacter?
The question mark `?` metacharacter is a quantifier that specifies 0 or 1. The other common quantifiers are asterisk (`*`) and plus (`+`). Asterisk means 0 or many and plus means 1 or many.

Unlike many other metacharacters, you don’t need to escape the question mark `?` metacharacter to make it work. The only time you need to escape it is when you want to match the question mark symbol itself.
![Screenshot-2023-03-09-at-08.54.31](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-09-at-08.54.31.png)


## How to Use the Zero or One `?` Quantifier in RegEx
The question mark quantifier can be useful when you are expecting two different but acceptable inputs from a user.

For instance, if you expect the user to type in “color” or “behavior”, but you’re not sure whether they speak British or American English, you can make the "u" optional:
![Screenshot-2023-03-09-at-09.08.31](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-09-at-09.08.31.png)

By putting the question mark symbol in front of the letter “u”, it means the "u" is optional. So, "color" and "colour" get matched, "behavior" and "behaviour" also get matched. 

You can also use the question mark quantifier to reduce greediness in your regular expressions. 

For example, let’s try to match everything inside the paragraph tags below:
```html
<p>freeCodeCamp is the best place to learnn coding for free</p> <p>freeCodeCamp is ubiquitous</p>

<p>You can learn any tech skill with freeCodeCamp</p>
```

This pattern, ` /<p>.*<\/p>/g` would match everything inside the tags. Everything would be two matches due to the carriage return separating the last `p` tag from the rest:
![Screenshot-2023-03-09-at-09.18.06](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-09-at-09.18.06.png)

You can separate all the tags into separate matches with the zero or one quantifier (`?`):
![Screenshot-2023-03-09-at-09.19.44](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-09-at-09.19.44.png)

And if you want just the first paragraph tag to be the match, you can turn off the `global` flag:
![Screenshot-2023-03-09-at-09.20.41](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-09-at-09.20.41.png) 

The question zero or one (`?`) quantifier would also work fine in any language that supports RegEx. Here’s an example in JavaScript:
```js
let str1 = 'Color is American';
let str2 = 'Colour is British';

let re1 = /colou?r/i;

console.log(re1.exec(str1)); // [ 'Color', index: 0, input: 'Color is American', groups: undefined ]
console.log(re1.exec(str2)); // [ 'Colour', index: 0, input: 'Colour is British', groups: undefined ]
```

## Conclusion
The zero or one quantifier helps stop regular expressions from being greedy by making a string optional on its own or within others. You should use it whn necessary in order to write less greedy and more accurate regular expressions.

Happy coding!



