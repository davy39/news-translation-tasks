---
title: How to title case a sentence in JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-06T12:11:28.000Z'
originalURL: https://freecodecamp.org/news/title-case-a-sentence-in-javascript-929012c88574
coverImage: https://cdn-media-1.freecodecamp.org/images/1*opgaEHfHpqV67c5Lu3j1Bw.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Dylan Attal

  Remember in grade school when your teachers showed you how to properly write a paper?
  The first thing you start with is a good title, and every good title is properly
  capitalized.

  During this algorithm scripting challenge, we’ll learn ...'
---

By Dylan Attal

Remember in grade school when your teachers showed you how to properly write a paper? The first thing you start with is a good title, and every good title is properly capitalized.

During this algorithm scripting challenge, we’ll learn how to title case a sentence in JavaScript. Ultimately, we’re going to have our algorithm take in a sentence and capitalize the first letter of each word as if it were the title of a paper.

#### Algorithm instructions

> Return the provided string with the first letter of each word capitalized. Make sure the rest of the word is in lower case.

> For the purpose of this exercise, you should also capitalize connecting words like “the” and “of”.

#### Provided Test Cases

* `titleCase("I'm a little tea pot")`should return a string.
* `titleCase("I'm a little tea pot")`should return `I'm A Little Tea Pot`.
* `titleCase("sHoRt AnD sToUt")`should return `Short And Stout`.
* `titleCase("HERE IS MY HANDLE HERE IS MY SPOUT")`should return `Here Is My Handle Here Is My Spout`.

### Solution #1: .map( ) and .slice( )

#### PEDAC

**Understanding the Problem**: We have one input, a string. Our output is also a string. Ultimately, we want to return the input string with the first letter — and only the first letter — of each word capitalized.

**Examples/Test Cases**: Our provided test cases show that we should have a capitalized letter only at the beginning of each word. We need to lower case the rest. The provided test cases also show that we aren’t being thrown any curve balls in terms of weird compound words separated by symbols instead of whitespace. That’s good news for us!

**Data Structure**: We are going to have to transform our input string into an array in order to manipulate each word separately.

A couple of notes on the methods we’ll be using:

Let’s talk about `[.map()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)`:

`.map()` creates a new array with the results of calling a function on every element in the array.

In other words, `.map()` allows us to manipulate each element in an array with a function, then return a new array with the results of our manipulation. The function can target both the currentValue and index of that currentValue, like so:

```
array.map((currentValue, Index) => {  // manipulate the currentValue in some way})
```

We don’t always have to use the Index. There will be times, though, when we need to target elements of an array by their index, so it’s handy to keep in mind.

Now let’s see an example of `.map()` in action. We have an array full of numbers and we want to multiply each number by 2.

```
let arrayOfNumbers = [3, 6, 10, 42, 98]arrayOfNumbers.map(number => number * 2)// returns [6, 12, 20, 84, 196]
```

Now let’s investigate `[.slice()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/slice)`:

`.slice()` extracts a section of a string and returns it as a new string. If you call `.slice()` on a string without passing it any additional information, it will return the whole string.

```
"Bastian".slice()// returns "Bastian"
```

We have the option of passing `.slice()` a beginIndex and endIndex, like so

```
.slice(beginIndex, endIndex)
```

This tells `.slice()` where to start the slicing and where to end the slicing. Keep in mind that strings are zero-indexed! So if we wanted to return from the 2-indexed letter of “Bastian” _until but not including_ the 5-indexed letter of “Bastian”, we could do this:

```
"Bastian".slice(2, 5)// returns "sti"
```

With that in mind, we can chop off the beginning of words and return the rest of them by passing in only a beginIndex, like so:

```
"Bastian".slice(3)// returns "tian"
```

**Algorithm**:

1. Turn all the letters in `str` to lower case letters.
2. Split the lower case `str` into an array, with each word being a separate element in the array.
3. Capitalize the first letter of each element in the array.
4. Join each element of the array into one string, separating each word by a whitespace.
5. Return the title cased string.

**Code**: See below!

I created a lot of unnecessary local variables in the above code to show the effect of each method on the input. Below I’ve removed the local variables, chained all the methods together, and removed the comments.

### Solution #2: regex

**Warning! Regex is not the best solution for beginners. Regular expressions are difficult in their own right, and their complexity is a common gripe for many experienced developers.** But hey, I’m feeling adventurous as I’m writing this, and I love to challenge myself to further understand regex whenever I can. This algorithm scripting challenge actually lends itself well to regex, so let’s take a look at it and see if we can further our understanding of regex!

#### PEDAC

**Understanding the Problem**: We have one input, a string. Our output is also a string. Ultimately, we want to return the input string with the first letter — and only the first letter — of each word capitalized.

**Examples/Test Cases**: Our provided test cases show that we should have a capitalized letter only at the beginning of each word. We need to lower case the rest. The provided test cases also show that we aren’t being thrown any curve balls in terms of weird compound words separated by symbols instead of whitespace. That’s good news for us!

**Data Structure**: We will not transform our string into an array while using regular expressions. JavaScript has a nifty method `[.replace()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace)` that allows us to target pretty much anything we want in a string and replace it with something else. We use regular expressions to target what we want to replace.

There are so many symbols used in regular expressions that I can’t hope to give a broad overview of them here. I can point you towards this [cheatsheet](https://www.rexegg.com/regex-quickstart.html), though, which I use whenever I have to employ regex.

What I can do is tell you that regex with `.replace()` in JavaScript follows a basic pattern. `.replace()` takes two arguments: a pattern (usually a regular expression) and a replacement (could be a string or a function).

```
string.replace(regex, function)
```

In our solution, we’ll be replacing the letter at the beginning of each word. How do we get regex to do this for us? We tell `.replace()` to match any character following a whitespace or matching the first character of the whole string (because the very first word of the string does not have a whitespace before it).

Let’s break down the regex part of our solution. To do that, let’s look at the first argument of the `.replace()` function. This is the regex code that determines what pattern we are looking to match and replace.

```
// full solution:
```

```
function titleCase(str) {  return str.toLowerCase().replace(/(^|\s)\S/g,  (firstLetter) => firstLetter.toUpperCase());}
```

We ultimately want to find all non-whitespace characters, which is represented by `\S`.

Then we want to specify that we want to match those non-whitespace characters at the beginning of a string `^` or `|` after any whitespace character `\s`.

We add the global modifier `g` to search for and replace all such patterns in the entire string.

**Algorithm**:

1. Turn all the letters in `str` to lower case letters.
2. Replace the first letter of each word in the string with the capitalized letter.
3. Return the title cased string.

**Code**: See below!

If you have other solutions and/or suggestions, please share in the comments!

#### This article is a part of the series [freeCodeCamp Algorithm Scripting](https://medium.com/@DylanAttal/freecodecamp-algorithm-scripting-b96227b7f837).

#### This article references [freeCodeCamp Basic Algorithm Scripting: Title Case a Sentence](https://learn.freecodecamp.org/javascript-algorithms-and-data-structures/basic-algorithm-scripting/title-case-a-sentence)

You can follow me on [Medium](https://medium.com/@DylanAttal), [LinkedIn](https://www.linkedin.com/in/dylanattal/), and [GitHub](https://github.com/DylanAttal)!

