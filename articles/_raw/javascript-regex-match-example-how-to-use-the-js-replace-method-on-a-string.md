---
title: JavaScript Regex Match Example – How to Use JS Replace on a String
subtitle: ''
author: Kristofer Koishigawa
co_authors: []
series: null
date: '2021-01-04T10:21:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-regex-match-example-how-to-use-the-js-replace-method-on-a-string
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/6020e04e0a2838549dcc0c26-1.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Regex
  slug: regex
- name: Regular Expressions
  slug: regular-expressions
seo_title: null
seo_desc: 'Regular expressions, abbreviated as regex, or sometimes regexp, are one
  of those concepts that you probably know is really powerful and useful. But they
  can be daunting, especially for beginning programmers.

  It doesn''t have to be this way. JavaScript...'
---

Regular expressions, abbreviated as regex, or sometimes regexp, are one of those concepts that you probably know is really powerful and useful. But they can be daunting, especially for beginning programmers.

It doesn't have to be this way. JavaScript includes several helpful methods that make using regular expressions much more manageable. Of the included methods, the `.match()`, `.matchAll()`, and `.replace()` methods are probably the ones you'll use most often.

In this tutorial, we'll go over the ins and outs of those methods, and look at some reasons why you might use them over the other included JS methods 

## A quick introduction to regular expressions

According to MDN, regular expressions are "patterns used to match character combinations in strings".

These patterns can sometimes include special characters (`*`, `+`), assertions (`\W`, `^`), groups and ranges (`(abc)`, `[123]`), and other things that make regex so powerful but hard to grasp.

At its core, regex is all about finding patterns in strings – everything from testing a string for a single character to verifying that a telephone number is valid can be done with regular expressions.

If you're brand new to regex and would like some practice before reading on, check out our [interactive coding challenges](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/regular-expressions/using-the-test-method).

## How to use the `.match()` method

So if regex is all about finding patterns in strings, you might be asking yourself what makes the `.match()` method so useful?

Unlike the `.test()` method which just returns `true` or `false`, `.match()` will actually return the match against the string you're testing. For example:

```js
const csLewisQuote = 'We are what we believe we are.';
const regex1 = /are/;
const regex2 = /eat/;

csLewisQuote.match(regex1); // ["are", index: 3, input: "We are what we believe we are.", groups: undefined]

csLewisQuote.match(regex2); // null

```

This can be really helpful for some projects, especially if you want to extract and manipulate the data that you're matching without changing the original string.

If all you want to know is if a search pattern is found or not, use the `.test()` method – it's much faster.

There are two main return values you can expect from the `.match()` method:

1. If there's a match, the `.match()` method will return an array with the match. We'll go into more detail about this in a bit.
2. If there isn't a match, the `.match()` method will return `null`.

Some of you might have already noticed this, but if you look at the example above, `.match()` is only matching the first occurrence of the word "are".

A lot of times you'll want to know how often a pattern is matched against the string you're testing, so let's take a look at how to do that with `.match()`.

### Different matching modes

If there's a match, the array that `.match()` returns had two different _modes_, for lack of a better term.

The first mode is when the global flag (`g`) isn't used, like in the example above:

```js
const csLewisQuote = 'We are what we believe we are.';
const regex = /are/;

csLewisQuote.match(regex); // ["are", index: 3, input: "We are what we believe we are.", groups: undefined]

```

In this case, we `.match()` an array with the first match along with the index of the match in the original string, the original string itself, and any matching groups that were used.

But say you want to see how many times the word "are" occurs in a string. To do that, just add the global search flag to your regular expression:

```js
const csLewisQuote = 'We are what we believe we are.';
const regex = /are/g;

csLewisQuote.match(regex); // ["are", "are"]

```

You won't get the other information included with the non-global mode, but you'll get an array with all the matches in the string you're testing.

### Case sensitivity

An important thing to remember is that regex is case sensitive. For example, say you wanted to see how many times the word "we" occurs in your string:

```js
const csLewisQuote = 'We are what we believe we are.';
const regex = /we/g;

csLewisQuote.match(regex); // ["we", "we"]

```

In this case, you're matching a lowercase "w" followed by a lowercase "e", which only occurs twice.

If you'd like all instances of the word "we" whether it's upper or lowercase, you have a couple of options.

First, you could use the `.toLowercase()` method on the string before testing it with the `.match()` method:

```js
const csLewisQuote = 'We are what we believe we are.'.toLowerCase();
const regex = /we/g;

csLewisQuote.match(regex); // ["we", "we", "we"]

```

Or if you want to preserve the original case, you could add the case-insensitive search flag (`i`) to your regular expression:

```js
const csLewisQuote = 'We are what we believe we are.';
const regex = /we/gi;

csLewisQuote.match(regex); // ["We", "we", "we"]

```

## The new `.matchAll()` method

Now that you know all about the `.match()` method, it's worth pointing out that the `.matchAll()` method was recently introduced.

Unlike the `.match()` method which returns an array or `null`, `.matchAll()` requires the global search flag (`g`), and returns either an iterator or an empty array:

```js
const csLewisQuote = 'We are what we believe we are.';
const regex1 = /we/gi;
const regex2 = /eat/gi;

[...csLewisQuote.matchAll(regex1)]; 
// [
//   ["We", index: 0, input: "We are what we believe we are.", groups: undefined],
//   ["we", index: 12, input: "We are what we believe we are.", groups: undefined]
//   ["we", index: 23, input: "We are what we believe we are.", groups: undefined]
// ]

[...csLewisQuote.matchAll(regex2)]; // []

```

While it seems like just a more complicated `.match()` method, the main advantage that `.matchAll()` offers is that it works better with capture groups.

Here's a simple example:

```js
const csLewisRepeat = "We We are are";
const repeatRegex = /(\w+)\s\1/g;

csLewisRepeat.match(repeatRegex); // ["We We", "are are"]

```

```js
const csLewisRepeat = "We We are are";
const repeatRegex = /(\w+)\s\1/g;

[...repeatStr.matchAll(repeatRegex)];

// [
//   ["We We", "We", index: 0, input: "We We are are", groups: undefined],
//   ["are are", "are", index: 6, input: "We We are are", groups: undefined],
// ]

```

While that just barely scratches the surface, keep in mind that it's probably better to use `.matchAll()` if you're using the `g` flag and want all the extra information that `.match()` provides for a single match (index, the original string, and so on).

## How to use the `.replace()` method

So now that you know how to match patterns in strings, you'll probably want to do something useful with those matches.

One of the most common things you'll do once you find a matching pattern is replace that pattern with something else. For example, you might want to replace "paid" in "paidCodeCamp" with "free". Regex would be a good way to do that.

Since `.match()` and `.matchAll()` return information about the index for each matching pattern, depending on how you use it, you could use that to do some fancy string manipulation. But there's an easier way – by using the `.replace()` method.

With `.replace()`, all you need to do is pass it a string or regular expression you want to match as the first argument, and a string to replace that matched pattern with as the second argument:

```js
const campString = 'paidCodeCamp';
const fCCString1 = campString.replace('paid', 'free');
const fCCString2 = campString.replace(/paid/, 'free');

console.log(campString); // "paidCodeCamp"
console.log(fCCString1); // "freeCodeCamp"
console.log(fCCString2); // "freeCodeCamp"

```

The best part is that `.replace()` returns a new string, and the original remains the same.

Similar to the `.match()` method, `.replace()` will only replace the first matched pattern it finds unless you use regex with the `g` flag:

```js
const campString = 'paidCodeCamp is awesome. You should check out paidCodeCamp.';
const fCCString1 = campString.replace('paid', 'free');
const fCCString2 = campString.replace(/paid/g, 'free');

console.log(fCCString1); // "freeCodeCamp is awesome. You should check out paidCodeCamp."
console.log(fCCString2); // "freeCodeCamp is awesome. You should check out freeCodeCamp."

```

And similar to before, whether you pass a string or a regular expression as the first argument, it's important to remember that the matching pattern is case sensitive:

```js
const campString = 'PaidCodeCamp is awesome. You should check out PaidCodeCamp.';
const fCCString1 = campString.replace('Paid', 'free');
const fCCString2 = campString.replace(/paid/gi, 'free');

console.log(fCCString1); // "freeCodeCamp is awesome. You should check out PaidCodeCamp."
console.log(fCCString2); // "freeCodeCamp is awesome. You should check out freeCodeCamp."

```

## How to use the `.replaceAll()` method

Just like how `.match()` has a newer `.matchAll()` method, `.replace()` has a newer `.replaceAll()` method.

The only real difference between `.replace()` and `.replaceAll()` is that you need to use the global search flag if you use a regular expression with `.replaceAll()`:

```js
const campString = 'paidCodeCamp is awesome. You should check out paidCodeCamp.';
const fCCString1 = campString.replaceAll('paid', 'free');
const fCCString2 = campString.replaceAll(/paid/g, 'free');

console.log(fCCString1); // "freeCodeCamp is awesome. You should check out freeCodeCamp."
console.log(fCCString2); // "freeCodeCamp is awesome. You should check out freeCodeCamp."

```

The real benefit with `.replaceAll()` is that it's a bit more readable, and replaces all matched patterns when you pass it a string as the first argument.

That's it! Now you know the basics of matching and replacing parts of strings with regex and some built-in JS methods. These were pretty simple examples, but I hope it still showed how powerful even a little bit of regex can be.

Was this helpful? How do you use the `.match()`, `.matchAll()`, `.replace()`, and `.replaceAll()` methods? Let me know over on [Twitter](https://twitter.com/kriskoishigawa).

