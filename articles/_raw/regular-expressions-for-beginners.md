---
title: How to Use Regular Expressions in JavaScript – Tutorial for Beginners
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-08-16T17:51:48.000Z'
originalURL: https://freecodecamp.org/news/regular-expressions-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/regex-image-1.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: Regex
  slug: regex
- name: Regular Expressions
  slug: regular-expressions
seo_title: null
seo_desc: "By Chinwendu Enyinna\nRegular expressions (regex) are a useful programming\
  \ tool. They are key to efficient text processing. Knowing how to solve problems\
  \ using regex is helpful to you as a developer and improves your productivity. \n\
  In this article, yo..."
---

By Chinwendu Enyinna

Regular expressions (regex) are a useful programming tool. They are key to efficient text processing. Knowing how to solve problems using regex is helpful to you as a developer and improves your productivity. 

In this article, you will learn about the fundamentals of regular expressions, regular expression pattern notation, how you can interpret a simple regex pattern, and how to write your own regex pattern. Let’s get to it!

## What Are Regular Expressions?

Regular expressions are patterns that allow you to describe, match, or parse text. With regular expressions, you can do things like find and replace text, verify that input data follows the format required, and and other similar things.

Here's a scenario: you want to verify that the telephone number entered by a user on a form matches a format, say, ###-###-#### (where # represents a number). One way to solve this could be:

```js
function isPattern(userInput) {
  if (typeof userInput !== 'string' || userInput.length !== 12) {
    return false;
  }
  for (let i = 0; i < userInput.length; i++) {
    let c = userInput[i];
    switch (i) {
      case 0:
      case 1:
      case 2:
      case 4:
      case 5:
      case 6:
      case 8:
      case 9:
      case 10:
      case 11:
        if (c < 0 || c > 9) return false;
        break;
      case 3:
      case 7:
        if (c !== '-') return false;
        break;
    }
  }
  return true;
}

```

Alternatively, we can use a regular expression here like this:

```js
function isPattern(userInput) {
  return /^\d{3}-\d{3}-\d{4}$/.test(userInput);
}

```

Notice how we’ve refactored the code using regex. Amazing right?  That is the power of regular expressions.

## How to Create A Regular Expression

In JavaScript, you can create a regular expression in either of two ways:

* Method #1: using a regular expression literal. This consists of a pattern enclosed in forward slashes. You can write this with or without a flag (we will see what flag means shortly). The syntax is as follows:

```js
const regExpLiteral = /pattern/;          // Without flags

const regExpLiteralWithFlags = /pattern/; // With flags

```

The forward slashes `/…/` indicate that we are creating a regular expression pattern, just the same way you use quotes `“ ”` to create a string.

* Method #2: using the RegExp constructor function. The syntax is as follows:

```js
new RegExp(pattern [, flags])

```

Here, the pattern is enclosed in quotes, the same as the flag parameter, which is optional.

So when do you use each of these pattern?

You should use a regex literal when you know the regular expression pattern at the time of writing the code. 

On the other hand, use the Regex constructor if the regex pattern is to be created dynamically. Also, the regex constructor lets you write a pattern using a template literal, but this is not possible with the regex literal syntax.

### What are Regular Expression Flags?

Flags or modifiers are characters that enable advanced search features including case-insensitive and global searching. You can use them individually or collectively. Some commonly used ones are:

* `g` is used for global search which means the search will not return after the first match.
* `i` is used for case-insensitive search meaning that a match can occur regardless of the casing.
* `m` is used for multiline search.
* `u` is used for Unicode search.

Let’s look at some regular expression patterns using both syntaxes.

#### How to use a regular expression literal: 

```js
// Syntax: /pattern/flags

const regExpStr = 'Hello world! hello there';

const regExpLiteral = /Hello/gi;

console.log(regExpStr.match(regExpLiteral));

// Output: ['Hello', 'hello']

```

Note that if we did not flag the pattern with `i`, only `Hello` will be returned. 

The pattern `/Hello/` is an example of a simple pattern. A simple pattern consists of characters that must appear literally in the target text. For a match to occur, the target text must follow the same sequence as the pattern. 

For example, if you re-write the text in the previous example and try to match it:

```js
const regExpLiteral = /Hello/gi;

const regExpStr = 'oHell world, ohell there!';

console.log(regExpStr.match(regExpLiteral));

// Output: null

```

We get _null_ because the characters in the string do not appear as specified in the pattern. So a literal pattern such as `/hello/`, means _h_ followed by _e_ followed by _l_ followed by _l_ followed by _o_, exactly like that.

#### How to use a regex constructor:

```js
// Syntax: RegExp(pattern [, flags])

const regExpConstructor = new RegExp('xyz', 'g'); // With flag -g

const str = 'xyz xyz';

console.log(str.match(regExpConstructor));

// Output: ['xyz', 'xyz']

```

Here, the pattern `xyz` is passed in as a string same as the flag. Also both occurrences of `xyz` got matched because we passed in the -g flag. Without it, only the first match will be returned. 

We can also pass in dynamically created patterns as template literals using the constructor function. For example:

```js
const pattern = prompt('Enter a pattern');
// Suppose the user enters 'xyz'

const regExpConst = new RegExp(`${pattern}`, 'gi');

const str = 'xyz XYZ';

console.log(str.match(regExpConst)); // Output: ['xyz', 'XYZ']

```

## How to Use Regular Expression Special Characters

A **special** **character** in a regular expression is a character with a reserved meaning. Using special characters, you can do more than just find a direct match. 

For example, if you want to match a character in a string that may or may not appear once or multiple times, you can do this with special characters. These characters fit into different subgroups that perform similar functions.

Let's take a look at each subgroup and the characters that go with them.

### Anchors and Boundaries:

**Anchors** are metacharacters that match the start and end of a line of text they are examining. You use them to assert where a boundary should be. 

The two characters used are `^` and `$`.

* `^` matches the start of a line and anchors a literal at the beginning of that line. For example:

```js
const regexPattern1 = /^cat/;

console.log(regexPattern1.test('cat and mouse')); // Output: true

console.log(regexPattern1.test('The cat and mouse')); // Output: false because the line does not start with cat

// Without the ^ in the pattern, the output will return true
// because we did not assert a boundary.

const regexPattern2 = /cat/;

console.log(regexPattern2.test('The cat and mouse')); // Output: true

```

* `$` matches the end of a line and anchors a literal at the end of that line. For example:

```js
const regexPattern = /cat$/;

console.log(regexPattern.test('The mouse and the cat')); // Output: true

console.log(regexPattern.test('The cat and mouse')); // Output: false

```

Note that anchors characters `^` and `$` **match just the position of the characters in the pattern** and not the actual characters themselves.

**Word Boundaries** are metacharacters that match the start and end position of a word – a sequence of alphanumeric characters. You can think of them as a word-based version of `^` and `$`.  You use the metacharacters `b` and `B` to assert a word boundary. 

* `\b` matches the start or end of a word. The word is matched according to the position of the metacharacter. Here's an example:

```js
// Syntax 1: /\b.../ where .... represents a word.

// Search for a word that begins with the pattern ward
const regexPattern1 = /\bward/gi;

const text1 = 'backward Wardrobe Ward';

console.log(text1.match(regexPattern1)); // Output: ['Ward', 'Ward']

// Syntax 2: /...\b/

// Search for a word that ends with the pattern ward
const regexPattern2 = /ward\b/gi;

const text2 = 'backward Wardrobe Ward';

console.log(text2.match(regexPattern2)); // Output: ['ward', 'Ward']

// Syntax 3: /\b....\b/

// Search for a stand-alone word that begins and end with the pattern ward
const regexPattern3 = /\bward\b/gi;

const text3 = 'backward Wardrobe Ward';

console.log(text3.match(regexPattern3)); // Output: ['Ward']

```

* `\B` is opposite of `\b` . It matches every position `\b` doesn't.

### Shortcodes for Other Metacharacters:

In addition to the metacharacters we have looked at, here are some of the most commonly used ones:

* `\d` – matches any decimal digit and is shorthand for [0-9].
* `\w` – matches any alphanumeric character which could be a letter, a digit, or an underscore. `\w` is shorthand for [A-Za-z0-9_].
* `\s` – matches any white space character.
* `\D` – matches any non-digit and is the same as [^0-9.]
* `\W` – matches any non-word (that is non-alphanumeric) character and is shorthand for  [^A-Za-z0-9_].
* `\S` – matches a non-white space character.
* `.` – matches any character.

### What is a Character Class?

A character class is used to match any one of several characters in a particular position. To denote a character class, you use square brackets `[]` and then list the characters you want to match inside the brackets. 

Let's look at an example:

```js
// Find and match a word with two alternative spellings

const regexPattern = /ambi[ea]nce/;

console.log(regexPattern.test('ambiance')); // Output: true

console.log(regexPattern.test('ambiance')); // Output: true

// The regex pattern interprets as:  find a followed by m, then b,
// then i, then either e or a, then n, then c, and then e.

```

### What is a Negated Character Class?

If you add a caret symbol inside a character class like this `[^...]`, it will match any character that is not listed inside the square brackets. For example:

```js
const regexPattern = /[^bc]at/;

console.log(regexPattern.test('bat')); // Output: false

console.log(regexPattern.test('cat')); // Output: false

console.log(regexPattern.test('mat')); // Output: true

```

### What is a Range?

A hyphen `-` indicates range when used inside a character class. Suppose you want to match a set of numbers, say [0123456789], or a set of characters, say[abcdefg]. You can write it as a range like this, [0-9] and [a-g], respectively.

### What is Alternation?

Alternation is yet another way you can specify a set of options. Here, you use the pipe character `|` to match any of several subexpressions. Either of the subexpressions is called an **alternative**. 

The pipe symbol means ‘or’, so it matches a series of options. It allows you combine subexpressions as alternatives. 

For example, `(x|y|z)a` will match `xa` or `ya`, or `za`.  In order to limit the reach of the alternation, you can use parentheses to group the alternatives together. 

Without the parentheses, `x|y|za`  would mean `x` or `y` or `za`. For example:

```js
const regexPattern = /(Bob|George)\sClan/;

console.log(regexPattern.test('Bob Clan')); // Output: true

console.log(regexPattern.test('George Clan')); // Output: true

```

### What are Quantifiers and Greediness?

Quantifiers denote how many times a character, a character class, or group should appear in the target text for a match to occur. Here are some peculiar ones:

* `+` will match any character it is appended to if the character appears at least once. For example:

```js
const regexPattern = /hel+o/;

console.log(regexPattern.test('helo'));          // Output:true

console.log(regexPattern.test('hellllllllllo')); // Output: true

console.log(regexPattern.test('heo'));           // Output: false

```

* `*` is similar to the + character but with a slight difference. When you append * to a character, it means you want to match any number of that character including none. Here’s an example:

```js
const regexPattern = /hel*o/;

console.log(regexPattern.test('helo'));    // Output: true

console.log(regexPattern.test('hellllo')); // Output: true

console.log(regexPattern.test('heo'));     // Output: true

// Here the * matches 0 or any number of 'l'

```

* `?` implies "optional". When you append it to a character, it means the character may or may not appear. For example:

```js
const regexPattern = /colou?r/;

console.log(regexPattern.test('color'));  // Output: true

console.log(regexPattern.test('colour')); // Output: true

// The ? after the character u makes u optional

```

* `{N}`, when appended to a character or character class, specifies how many of the character we want. For example `/\d{3}/` means match three consecutive digits.
* `{N,M}` is called the interval quantifier and is used to specify a range for the minimum and maximum possible match. For example `/\d{3, 6}/` means match a minimum of 3 and a maximum of 6 consecutive digits.
* `{N, }` denotes an open-ended range. For example `/\d{3, }/` means match any 3 or more consecutive digits.

### What is Greediness in Regex?

All quantifiers by default are **greedy**. This means that they will try to match all possible characters. 

To remove this default state and make them non-greedy, you append a `?` to the operator like this `+?`, `*?`, `{N}?`, `{N,M}?`.....and so on.

### What are Grouping and Backreferencing?

We previously looked at how we can limit the scope of alternation using the parentheses. 

What if you want to use a quantifier like `+` or `*` on more than one character at a time – say a character class or group? You can group them together as a whole using the parentheses before appending the quantifier, just like in this example:

```js
const regExp = /abc+(xyz+)+/i;

console.log(regExp.test('abcxyzzzzXYZ')); // Output: true

```

Here's what the pattern means: The first + matches the c of abc, the second + matches the z of xyz, and the third + matches the subexpression xyz, which will match if the sequence repeats.

**Backreferencing** allows you to match a new pattern that is the same as a previously matched pattern in a regular expression. You also use parentheses for backreferencing because it can remember a previously matched subexpression it encloses (that is, the captured group).

However, it is possible to have more than one captured group in a regular expression. So, to backreference any of the captured group, you use a number to identify the parentheses. 

Suppose you have 3 captured groups in a regex and you want to backreference any of them. You use `\1`, `\2`, or `\3`, to refer to the first, second, or third parentheses. To number the parentheses, you start counting the open parentheses from the left.

Let's look at some examples:

**`(x)`** matches x and remembers the match.

```js
const regExp = /(abc)bar\1/i;

// abc is backreferenced and is anchored at the same position as \1
console.log(regExp.test('abcbarAbc')); // Output: true

console.log(regExp.test('abcbar')); // Output: false

```

**`(?:x)`** matches x but does not recall the match. Also, \n (where n is a number) does not remember a previously captured group, and will match as a literal. Using an example:

```js
const regExp = /(?:abc)bar\1/i;

console.log(regExp.test('abcbarabc')); // Output: false

console.log(regExp.test('abcbar\1')); // Output: true

```

### The Escape Rule

A metacharacter has to be escaped with a backslash if you want it to appear as a literal in your regular expression. By escaping a metacharacter in regex, the metacharacter loses its special meaning.

## Regular Expression Methods

### The `test()` method 

We have used this method a number of times in this article. The `test()` method compares the target text with the regex pattern and returns a boolean value accordingly. If there is a match, it returns true, otherwise it returns false.

```js
const regExp = /abc/i;

console.log(regExp.test('abcdef')); // Output: true

console.log(regExp.test('bcadef')); // Output: false

```

### The `exec()` method 

The `exec()` method compares the target text with the regex pattern. If there's a match, it returns an array with the match – otherwise it returns null. For example:

```js
const regExp = /abc/i;

console.log(regExp.exec('abcdef'));
// Output: ['abc', index: 0, input: 'abcdef', groups: undefined]

console.log(regExp.exec('bcadef'));
// Output: null

```

Also, there are string methods that accept regular expressions as a parameter like `[match()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/match)`, `[replace()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace)`, `[replaceAll()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replaceAll)`, `[matchAll()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/matchAll)`, `[search()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/search)`, and `[split()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split)`. 

## Regex Examples

Here are some examples to reinforce some of the concepts we've learned in this article.

First example: How to use a regex pattern to match an email address:

```js
const regexPattern = /^[(\w\d\W)+]+@[\w+]+\.[\w+]+$/i;

console.log(regexPattern.test('abcdef123@gmailcom'));
// Output: false, missing dot

console.log(regexPattern.test('abcdef123gmail.'));
// Output: false, missing end literal 'com'

console.log(regexPattern.test('abcdef123@gmail.com'));
// Output: true, the input matches the pattern correctly

```

Let's interpret the pattern. Here's what's happening:

* **`/`** represents the start of the regular expression pattern.
* **`^`** checks for the start of a line with the characters in the character class.
* `**[(\w\d\W)+ ]+**` matches any word, digit and non-word character in the character class at least once. Notice how the parentheses were used to group the characters before adding the quantifier. This is same as this `[\w+\d+\W+]+` .
* `**@**` matches the literal @ in the email format.
* `**[\w+]+**` matches any word character in this character class at least once.
* `**\.**` escapes the dot so it appears as a literal character.
* `**[\w+]+$**` matches any word character in this class. Also this character class is anchored at the end of the line.
* `**/**` - ends the pattern

Alright, next example: how to match a URL with format http://example.com or https://www.example.com:

```js
const pattern = /^[https?]+:\/\/((w{3}\.)?[\w+]+)\.[\w+]+$/i;

console.log(pattern.test('https://www.example.com'));
// Output: true

console.log(pattern.test('http://example.com'));
// Output: true

console.log(pattern.test('https://example'));
// Output: false

```

Let's also interpret this pattern. Here's what's happening:

* `/...../` represents the start and end of the regex pattern
* `^` asserts for the start of the line
* `[https?]+` matches the characters listed at least once, however `?` makes 's'  optional.
* `:` matches a literal semi-colon.
* `\/\/` escapes the two forward slashes.
* `(w{3}\.)` matches the character w 3 times and the dot that follows immediately. However, this group is optional.
* `[\w+]+` matches character in this class at least once.
* `\.` escapes the dot
* `[\w+]+$` matches any word character in this class. Also this character class is anchored at the end of the line.

## Conclusion

In this article, we looked at the fundamentals of regular expressions. We also explained some regular expression patterns, and practiced with a few examples.

There's more to regular expressions beyond this article. To help you learn more about regular expressions, here are some resources you can read through:

* [Regular Expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions)
* [Learn Regex crash course](https://www.freecodecamp.org/news/regular-expressions-crash-course/)
* [Regular Expression Tutorial](https://www.regular-expressions.info/tutorial.html)
* [Regular Expression Cheatsheet](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions/Cheatsheet)

And that's all for this tutorial. Happy coding :)

