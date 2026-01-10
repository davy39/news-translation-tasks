---
title: JavaScript replaceAll() – Replace All Instances of a String in JS
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-07-28T16:15:26.000Z'
originalURL: https://freecodecamp.org/news/javascript-replaceall-replace-all-instances-of-a-string-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/pexels-christina-morillo-1181675.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'When working with a JavaScript program, you might need to replace a character
  or word with another one.

  Specifically, you may need to replace not just one but all occurrences of that character
  or word with something else.

  There are a few ways you can...'
---

When working with a JavaScript program, you might need to replace a character or word with another one.

Specifically, you may need to replace not just one but all occurrences of that character or word with something else.

There are a few ways you can achieve this with JavaScript. 

One of the ways is using the built-in `replaceAll()` method, which you will learn to use in this article.

Here is what we will cover:

1. [What is `replaceAll()` in JavaScript?](#intro)
    1. [`replaceAll()` syntax](#syntax)
2. [`replaceAll()` with a string as the first parameter](#string-param)
3. [`replaceAll()` with a regular expression as the first parameter](#regEx)
4. [`replaceAll()` VS `replace()`](#differences)

## What Is `replaceAll()` in JavaScript? <a name="intro"></a>

The `replaceAll()` method is part of JavaScript's standard library. When you use it, you replace all instances of a string.

There are different ways you can replace all instances of a string. That said, using `replaceAll()` is the most straightforward and fastest way to do so.

Something to note is that this functionality was introduced with ES2021. 

Although the `replaceAll()` method is compatible with all the major browsers, it is not the best solution when developing for older versions of browsers, as these older versions may not be able to understand and support it.

### The `replaceAll()` Method - A Syntax Breakdown <a name="syntax"></a>

The general syntax for the `replaceAll()` method looks like this:

```
string.replaceAll(pattern, replacement)
```

Let's break it down:

- `string` is the original string you are working with and the string you will call the `replaceAll()` method on.
- The `replaceAll()` method takes 2 parameters:
-  `pattern` is the first parameter, which can be a substring or a regular expression - this refers to the item you want to change and replace with something else.
    - If `pattern` is a **regular expression**, you need to include the `g` flag (where `g` stands for `g`lobal) or `replaceAll()` will throw an exception - specifically, the error will be a `TypeError`.
- `replacement` is the second parameter, which can be another string or a function to replace `pattern`. 

Something to note here is that the `replaceAll()` method doesn't change the original string. Instead, it returns a new copy. 

All instances of the specified `pattern` will be replaced by `replacement`.

## How to Use `replaceAll()` with a String as the First Parameter Example <a name="string-param"></a>

Earlier, you saw the `replaceAll()` method accepts two parameters - `pattern` as the first parameter and `replacement` as the second.

You also saw that `pattern` could be a string or a regular expression.

Now, let's see how `replaceAll()` works when it takes a **string** as the first parameter.

So, say you have the following example:

```js
const my_string = "I like dogs because dogs are adorable!";

let pattern = "dogs";
let replacement = "cats";

let my_new_string = my_string.replaceAll(pattern,replacement);
```

I store the text `I like dogs because dogs are adorable!` in a variable named `my_string`. 

This is the original string I am working with and I want to modify some of its contents.

Specifically, I want to change the substring `dogs`, which appears *twice* in the original string - this will be my `pattern`. 

I store this substring I want to replace with something else in a variable called `pattern`.

I then store the string `cats` in a variable called `replacement` - this is the string that will replace `dogs`.

I then call the `replaceAll()` method on the original string, pass the two substrings as parameters, and store that result in a variable named `my_new_string`.

```js
console.log(my_new_string);

// I like cats because cats are adorable!
```

The `replaceAll()` method will replace *all* instances of the substring `dogs` in the string `I like dogs because dogs are adorable!` with `cats`.

The original string will remain unchanged.

Something to note here is that the substitution when using a string as the first parameter is case sensitive. This means that only the string with the same case that matches the `pattern` is replaced.

```js
const my_string = "I like Dogs because dogs are adorable!";

let pattern = "dogs";
let replacement = "cats";

let my_new_string = my_string.replaceAll(pattern,replacement);

console.log(my_new_string);
```

In the example above, there are two instances of `dogs`, but the first one has a capital `D`.

As you can see by the output, the substitution was case-sensitive:

```
I like Dogs because cats are adorable!
```

## How to Use `replaceAll()` with a Regular Expression as the First Parameter Example <a name="regEx"></a>

As you saw earlier, you can pass a regular expression (also known as regex) as the first parameter.

A regular expression is a sequence of characters that create a search pattern.

The general syntax to do this looks similar to the following:

```
string.replaceAll(/pattern/g, replacement)
```

Let's take the example from the previous section, and instead of a string, use a regular expression as the first parameter:

```js
const my_string = "I like dogs because dogs are adorable!";

let pattern = /dogs/g;
let replacement = "cats";

let my_new_string = my_string.replaceAll(pattern,replacement);

console.log(my_new_string);

//output

// I like cats because cats are adorable!
```

When using a regular expression as the first parameter, make sure to use the `g` flag.

If you don't, you will end up getting an error in your code:

```js
const my_string = "I like dogs because dogs are adorable!";

let pattern = /dogs/;
let replacement = "cats";

let my_new_string = my_string.replaceAll(pattern,replacement);

console.log(my_new_string);

// output

// test.js:6 Uncaught TypeError: String.prototype.replaceAll called with a // non-global RegExp argument
//    at String.replaceAll (<anonymous>)
//   at test.js:6:31
```

Let's tweak the original string a little bit.

```js
const my_string = "I like Dogs because dogs are adorable!";

let pattern = /dogs/g;
let replacement = "cats";

let my_new_string = my_string.replaceAll(pattern,replacement);

console.log(my_new_string);
```

I've now got two instances of `dogs`, but one of them is with a capitalized `D`.

I end up with the following output:

```
I like Dogs because cats are adorable!
```

From that output, you can tell that it is a case-sensitive replacement.

To make it case-insensitive, make sure to add the `i` flag after the `g` flag like so:

```js
const my_string = "I like Dogs because dogs are adorable!";

let pattern = /dogs/gi;
let replacement = "cats";

let my_new_string = my_string.replaceAll(pattern,replacement);

console.log(my_new_string);

// output

// I like cats because cats are adorable!
```

The regular expression `/dogs/gi` will match all instances that contain that substring and make the replacement case insensitive.

## The `replaceAll()` vs the `replace()` Method - What's The Difference? <a name="differences"></a>

The difference between the `replaceAll()` and the `replace()` methods is that `replaceAll()` performs a global substitution straight out of the box.

The `replaceAll()` method will substitute *all* instances of the string or regular expression pattern you specify, whereas the `replace()` method will replace only the *first* occurrence.

This is how `replace()` works with a string as a first parameter:

```js
const my_string = "I like dogs because dogs are adorable!";

let pattern = "dogs";
let replacement = "cats";

let my_new_string = my_string.replace(pattern,replacement);

console.log(my_new_string);

// output
// I like cats because dogs are adorable!
```

And this is how `replace()` works with a regular expression as the first parameter:

```js
const my_string = "I like dogs because dogs are adorable!";

let pattern = /dogs/;
let replacement = "cats";

let my_new_string = my_string.replace(pattern,replacement);

console.log(my_new_string);

// output
// I like cats because dogs are adorable!
```

The only way to perform global substitution with the `replace()` method is to use a regular expression with the `g` flag:

```js
const my_string = "I like dogs because dogs are adorable!";

let pattern = /dogs/g;
let replacement = "cats";

let my_new_string = my_string.replace(pattern,replacement);

console.log(my_new_string);

// output

// I like cats because cats are adorable!
```

## Conclusion

And there you have it! You now know how the `replaceAll()` method works and some ways you can use it.

To learn more about JavaScript, head to freeCodeCamp's [JavaScript Algorithms and Data Structures Certification](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/).

It's a free, well-thought-out, and structured curriculum where you will learn interactively. In the end, you will also build 5 projects to claim your certification and solidify your knowledge.

Thanks for reading!


