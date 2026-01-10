---
title: How to use a RegExp to confirm the ending of a String in JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-05T21:51:45.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-a-regexp-to-confirm-the-ending-of-a-string-in-javascript-4b42f3749af1
coverImage: https://cdn-media-1.freecodecamp.org/images/0*YLruZvgbUfHmlITM
tags:
- name: algorithms
  slug: algorithms
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Regex
  slug: regex
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Catherine Vassant (aka Codingk8)

  Using the Regexp ?️ constructor


  _Photo by [Unsplash](https://unsplash.com/@jluebke?utm_source=medium&utm_medium=referral"
  rel="noopener" target="_blank" title="">Justin Luebke on <a href="https://unsplash.com?utm_...'
---

By Catherine Vassant (aka Codingk8)

Using the Regexp ?️ constructor

![Image](https://cdn-media-1.freecodecamp.org/images/0*YLruZvgbUfHmlITM)
_Photo by [Unsplash](https://unsplash.com/@jluebke?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Justin Luebke</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

_This article is based on [freeCodeCamp](https://www.freecodecamp.org/)’s Basic Algorithm Scripting “[Confirm the ending](https://learn.freecodecamp.org/javascript-algorithms-and-data-structures/basic-algorithm-scripting/confirm-the-ending)”._

This challenge involves checking whether a String ends with a specific sequence of letters or not.

In this article, I’ll explain how to solve this challenge using a RegExp.

The interesting aspect of this solution is using the RegExp constructor to create the specific RegExp you need to check Strings passed as arguments.

#### Algorithm Challenge

> Check if a string (first argument, `str`) ends with the given target string (second argument, `target`).

> This challenge can be solved with the `.endsWith()`method, which was introduced in ES2015. But for the purpose of this challenge, we would like you to use one of the JavaScript substring methods instead.

#### Provided test cases

> `confirmEnding("Bastian", "n")`should return true.

> `confirmEnding("Congratulation", "on")`should return true.

> `confirmEnding("Connor", "n")`should return false.

> `confirmEnding("Walking on water and developing software from a specification are easy if both are frozen", "specification")`should return false.

> `confirmEnding("He has to give me a new name", "name")`should return true.

> `confirmEnding("Open sesame", "same")`should return true.

> `confirmEnding("Open sesame", "pen")`should return false.

> `confirmEnding("Open sesame", "game")`should return false.

> `confirmEnding("If you want to save our world, you must hurry. We dont know how much longer we can withstand the nothing", "mountain")`should return false.

> `confirmEnding("Abstraction", "action")`should return true.

> Do not use the built-in method `.endsWith()`to solve the challenge.

### 1. The first idea that does not work at all

If, like me, you’re a RexExp lover, your first attempt might be to try solve the challenge with the **code below**, and it **won’t work**.

The reason is, with this syntax, the test() function will look for the specific “target” String and not “target” as a variable passed as an argument.

If we go back to our test cases, the ones that should return “false”, do pass, but none of the ones that should return “true” pass, which is quite predictable.

![Image](https://cdn-media-1.freecodecamp.org/images/0*eIBStwAQ1PDwZkrJ)
_Photo by [Unsplash](https://unsplash.com/@fotolancaster?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Pablo Lancaster Jones</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

### 2. Solve the challenge by creating the specific RegExp you need with the RegExp constructor

In order to use a RegExp that is going to “understand” that the “target” argument is a variable and not the String “target”, you have to **create a taylor-made RegExp using the RegExp constructor**.

And, before we move forward, let’s go back for a minute and look at what we want to test: the “target” argument should be the ending of the “str” argument. This means **our RegExp should end with the “$” character**.

#### **Now, we can solve this challenge in three steps**

**Step 1** - Create a variable adding the “$” at the end of the “target” argument, using the concat() method in this case.

**Step 2** - Use the RegExp constructor and the “new” operator to create the right RexExp with the above variable.

**Step 3** - Return the result of the test() function.

And this passes all the case tests beautifully ?

#### **This can be refactored in two lines like this**

**Note**: since none of the test cases imply to test the capitalization of the letters, there’s no need to use the “i” flag.

#### Useful links

[String.prototype.concat()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/concat) in MDN

[RegExp.prototype.test()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/test) in MDN

[RegExp constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp) in MDN

[Regular Expressions](https://learn.freecodecamp.org/javascript-algorithms-and-data-structures/regular-expressions) in [freeCodeCamp](https://www.freecodecamp.org/)

#### Other solutions to this challenge

The **challenge “[Get a Hint](https://guide.freecodecamp.org/certifications/javascript-algorithms-and-data-structures/basic-algorithm-scripting/confirm-the-ending/)”** suggests a solution using the **slice() method**.

You can find two other ways of solving this challenge, one with the **substr() method** and the other with the **endsWith() method, explained by [Sonya Moisset](https://www.freecodecamp.org/news/how-to-use-a-regexp-to-confirm-the-ending-of-a-string-in-javascript-4b42f3749af1/undefined) in [this article](https://medium.freecodecamp.org/two-ways-to-confirm-the-ending-of-a-string-in-javascript-62b4677034ac)**.

This ad-hoc RegExp solution can **also help you solve the freeCodeCamp Intermediate Algorithm Scripting “[Search and Replace](https://learn.freecodecamp.org/javascript-algorithms-and-data-structures/intermediate-algorithm-scripting/search-and-replace)” challenge**.

**Thank you for reading!** ✨

If you enjoyed this article, **please “hands-clap” as many times as you like** and share it **to help other people find it.** That may make their day.

If you have a **reaction/question/suggestion**, be sure to leave a **comment below**. I’ll be glad to read from you!

You can also get in touch and/or follow [**me on Twitter**](https://twitter.com/codingk8)**.**

