---
title: What Does B in RegEx Mean? Word Boundary and Non-word Boundary Metacharacters
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-03-08T14:10:22.000Z'
originalURL: https://freecodecamp.org/news/what-does-b-in-regex-mean-word-boundary-and-non-word-boundary-metacharacters
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/start-graph--4-.png
tags:
- name: Regex
  slug: regex
seo_title: null
seo_desc: 'In regular expressions, “B” is a metacharacter for specifying word boundary.
  It could be in two forms – the capital letter “B” and the small letter “b”.

  Since B (and b) is a metacharacter, you need to escape it to make it work (\b and
  \B). Otherwise,...'
---

In regular expressions, “B” is a metacharacter for specifying word boundary. It could be in two forms – the capital letter “B” and the small letter “b”.

Since `B` (and `b`) is a metacharacter, you need to escape it to make it work (`\b` and `\B`). Otherwise, `b` or `B` would be interpreted as an alphabet letter.

In this article, I’ll guide you through those two variations of the “B” character in RegEx. We'll look at what they do and their usage in both RegEx engines and programming.

## What We'll Cover
- [What Does the “S” Metacharacter Do?](#heading-what-does-the-s-metacharacter-do)
- [How to Use the “B” Metacharacter in RegEx](#heading-how-to-use-the-b-metacharacter-in-regex)
  - [How to Use the Word Boundary (`\b`) Metacharacter](#heading-how-to-use-the-word-boundary-b-metacharacter)
  - [How to Use the Non-word Boundary (`\B`) Metacharacter](#heading-how-to-use-the-non-word-boundary-b-metacharacter)
- [Wrapping Up](#heading-wrapping-up)


## What Does the “S” Metacharacter Do?
The small letter “b” metacharacter stands for a word boundary, and the capital letter “B” stands for a non-word boundary. That's how the pattern for most metacharacters works. 

For instance, the small letter “s” is the metacharacter for a space (spacebar, tab, carriage return, new line), and the capital letter “S” is the non-space metacharacter.

You can [read more about the `s` metacharacter here](https://www.freecodecamp.org/news/what-does-s-in-regex-mean-space-and-negated-space-metacharacters/).

The small letter `\b` word boundary indicates that a pattern is bounded by a non-word character. Non-word characters are all characters apart from numbers, letters, and underscore (`_`). They are denoted by another metacharacter (`\W`).

On the other hand, the capital letter `\B`  is a non-word boundary that indicates that a pattern is bounded by a word character. Word characters are letters, numbers, and underscore (`_`). They are denoted by another metacharacter (`\w`).


## How to Use the “B” Metacharacter in RegEx
The `\b` metacharacter specifies word boundary and `\B` specifies non-word boundary. Both reference positions, not the actual characters, but they match different things as they are opposites.


### How to Use the Word Boundary (`\b`) Metacharacter
Here’s how the word boundary (`\b`) metacharacter works:

For example, in the sentence “One should take care of oneself before takin care of others one by one”, putting `\b` before the word “one” as the defined pattern would match every of the word “one” preceded by a non-word character (anything apart from letters, numbers and underscore `_`):
![Screenshot-2023-03-08-at-11.00.42](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-08-at-11.00.42.png)

If I put `\b` on the other side of the word “one” again, then it would match just the word “one” but not “oneself”:
![Screenshot-2023-03-08-at-11.04.17](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-08-at-11.04.17.png) 

And that’s what the word boundary metacharacter does – it lets you match the exact part of a string you want.

**Note**: I was able to match the word “One” because I turned on the case-insensitive flag.

You also don’t have to use the word boundary metacharacter with one word:
![Screenshot-2023-03-08-at-11.07.57](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-08-at-11.07.57.png) 


### How to Use the Non-word Boundary (`\B`) Metacharacter
For the non-word boundary metacharacter (`\B`), remember it matches anything bounded by a word character.

Here is how I used it to match “for” inside the word “before”:
![Screenshot-2023-03-08-at-11.15.04](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-08-at-11.15.04.png)

And this is how I used it to grab “king” from the word “taking”:
![Screenshot-2023-03-08-at-11.15.54](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-08-at-11.15.54.png)

Now, if you want to match the word “the” inside of “others”, you just need to surround the word “the” with `\B` in your pattern.

The `\b` and `\B` metacharacters would also work fine in a language like JavaScript:
```js
let str =
  'One should take care of oneself before taking care of others one by one';

let regex1 = /\Bking/;
let regex2 = /\bone/;

console.log(regex1.exec(str));
console.log(regex2.exec(str));
```

This is the result in the console:
![Screenshot-2023-03-08-at-11.22.05](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-08-at-11.22.05.png)


## Wrapping Up
The word boundary and non-word boundary metacharacters help you grab the exact word you need in a string or even in a particular word which comes in handy when implementing several validations for user input.

Happy coding!


