---
title: How to Check if a String Contains a Substring in JavaScript
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-10-07T18:00:38.000Z'
originalURL: https://freecodecamp.org/news/how-to-check-if-a-string-contains-a-substring-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/pexels-tranmautritam-251225.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'When you''re working with a JavaScript program, you might need to check
  whether a string contains a substring. A substring is a string inside another string.

  Specifically, you might need to check whether a word contains a specific character
  or a speci...'
---

When you're working with a JavaScript program, you might need to check whether a string contains a substring. A substring is a string inside another string.

Specifically, you might need to check whether a word contains a specific character or a specific set of characters.

Thankfully, there are a few quick ways to achieve this with JavaScript.

In this article, you will learn two different ways you can check if a string contains a substring using JavaScript methods.

Specifically, you will learn:
-  How to use the built-in `includes()` JavaScript method.
-  How to use the built-in `indexOf()` JavaScript method.

Here is what we will cover in more detail:

1. [Syntax breakdown of the `includes()` method in JavaScript](#includes-syntax)
    1. [How to check if a string contains a specific substring using the `includes()` method](#includes-example)
2. [Syntax breakdown of the `indexOf()` method in JavaScript](#index-syntax)
    1. [How to check if a string contains a specific substring using the `indexOf()` method](#index-example)
 3. [How to make a case-insensitive check with the `includes()` and `indexOf()` methods](#insensitive)

## What Is The `includes()` Method in JavaScript? `includes()` Method Syntax Breakdown <a name="includes-syntax"></a>

The JavaScript `includes()` method was introduced with ES6, and it is the most common and modern way of checking if a string contains a specific character or a series of characters.

The general syntax for the `includes()` method looks something similar to this:

```
string.includes(substring, index);
```

Let's break it down:

- `string` is the word you want to search through.
- `includes()` is the method you call on the word you want to search through, which in this case is `string`.
- The `includes()` method accepts two arguments - one is required, and one is optional.
- The first argument the `includes()` method accepts is `substring`, and it is *required*. `substring` is the character or the series of characters you are checking to see if they exist within `string`.
- The second argument the `includes()` method accepts is `index`, and it is *optional*. `index` refers to the position from which the search for `substring` will start - the default value is `0` because indexing in programming languages begins at `0`.

The return value is a Boolean value. A Boolean value can either be `true` or `false` depending on whether the substring is present or not within the string.

Something to keep in mind is that the `includes()` method is **case-sensitive**.

### How To Check if A String Contains A Specific Substring in JavaScript Using The `includes()` Method <a name="includes-example"></a>

Let's see an example of how the `includes()` method works.

First, I created a variable that holds the string `Hello, World` - this is the string I want to search through:

```js
let string= "Hello, World";
```

Next, I created a variable with the substring `Hello` - this is the substring I want to search for in the original string:

```js
let string= "Hello, World";
let substring = "Hello";
```

Next, I will check if `substring` is present within `string` using the `includes()` method and print the result to the console:

```js
let string= "Hello, World";
let substring = "Hello";

console.log(string.includes(substring));

// output
// true
```

The return value was `true`, meaning `Hello` is present in the variable `string`.

As mentioned in the section above, the `includes()` method is case-sensitive.

See what happens when I change the value of `substring` from `Hello` to `hello`:

```js
let string= "Hello, World";
let substring = "hello";

console.log(string.includes(substring));

// output
// false
```

The return value, in this case, is `false`, as there is no substring `hello` with a lowercase `h`. So, keep this in mind when working with the `includes()` method - it differentiates between capital and lowercase letters. 

Now, let's see how to use the `includes()` method with the second argument, `index`.

As a reminder, the second argument specifies the position from which you want to start the search for the substring.

Let's take the same `string` variable from the previous examples:

```js
let string= "Hello, World";
```

I will change the value of the `substring` variable to `H`:

```js
let string= "Hello, World";
let substring = "H";
```

And I will specify the search of the substring to start from position `0`:

```js
let string= "Hello, World";
let substring = "H";

console.log(string.includes(substring,0));

// output
// true
```

The return value is `true` because the substring `H` is at index position `0` within the string `Hello, World`.

Remember, the first letter in a string has a position of `0`, the second a position of `1`, and so on.

## What Is The `indexOf()` Method in JavaScript? `indexOf()` Method Syntax Breakdown <a name="index-syntax"></a>

Similar to the `includes()` method, the JavaScript `indexOf()` method checks if a string includes a substring.

The general syntax for the `indexOf()` method looks something similar to this:

```
string.indexOf(substring, index);
```

Let's break it down:

- `string` is the word you want to search through.
- `index0f()` is the method you call on the word you want to search through, in this case, `string`.
- The `includes()` method takes two arguments - one is required, and one is optional.
- The first argument to the `indexOf()` method is `substring`, and it is *required*. `substring` is the character or the series of characters you are searching for.
- The second argument to the `indexOf()` method is `index`, and it is *optional*. `index` refers to the position from which the search for `substring` will start. The default value is `0` because indexing in programming languages begins at `0`.

The difference between the two methods is their return value. 

The `includes()` method returns a Boolean value (a value that is either `true` or `false`), whereas the `indexOf()` method returns a number.

The number will be the starting index position where the substring you are looking for is found within the string. The return value will be `-1` if the substring is not found in the string.

And just like the `includes()` method, the `indexOf()` method is **case-sensitive**.


### How To Check if A String Contains A Specific Substring in JavaScript Using The `indexOf()` Method <a name="index-example"></a>

Let's use the same example from earlier to see how the `indexOf()` method works.

```js
let string= "Hello, World";
let substring = "H";
```

There is the variable `string` with the original string, and the variable `substring` with the substring you are searching for.

```js
let string= "Hello, World";
let substring = "H";

console.log(string.indexOf(substring));

// output
// 0
```

The output is `0`, which is the starting position of the substring you are searching for.

In this case, the value you were searching for was a single character.

Let's change the value of `substring` from `H` to `Hello`:


```js
let string= "Hello, World";
let substring = "Hello";

console.log(string.indexOf(substring));

// output
// 0
```

The return value is again `0` since `index0f()` returns the *starting* position of the substring you are looking for. Since the first character of the substring is located at the `0` position, `indexOf()` returns `0`.

Now, let's change the value of `substring` from `Hello` to `hello` with a lowercase `h`:

```js
let string= "Hello, World";
let substring = "hello";

console.log(string.indexOf(substring));

// output
// -1
```

The return value is `-1`. As mentioned earlier, `index0f()` is case-sensitive, so it cannot find a substring `hello` with lowercase `h`. And when `indexOf()` cannot find the given substring, it returns `-1`.

Finally, you can specify the index value you want to start your search from by passing the second argument that `indexOf()` accepts.

```js
let string= "Hello, World";
let substring = "hello";

console.log(string.indexOf(substring,1));

// output
// -1
```

Say you want to start your search from position `1`. The return value is `-1` since the starting position of the substring you are searching for is `0`. An exact match is not found at position `1` so `indexOf()` returns `-1`.

## How To Make A Case-Insensitive Check With the `includes()` and `indexOf()` Methods <a name="insensitive"></a>

So far, you have seen that the `includes()` and `indexOf()` methods are case-insensitive.

But what happens when you want to perform a case-insensitive check?

To do a case-insensitive check and see if a substring is present within a string, you will need to convert both the original string and the substring to lowercase using the `toLowerCase()` JavaScript method before calling one of the two methods.

Here is how you would do that using the `includes()` method:

```js
let string= "Hello, World";
let substring = "hello";

console.log(string.toLowerCase().includes(substring.toLowerCase()));

// output
// true
```

By default, the return value would have been `false` because the original string contains an uppercase `H`, whereas the substring contains a lowercase `h`. After converting both strings to lowercase, you don't have to worry about the capitalization of the original string and the substring you are searching for.

And here is how you would do the same thing using the `indexOf()` method:

```js
let string= "Hello, World";
let substring = "hello";

console.log(string.toLowerCase().indexOf(substring.toLowerCase()));

// output
// 0
```

By default, the return value would have been `-1` because the original
string and the substring you are searching for have different cases.

After using the `toLowerCase()` method, the `indexOf()` method returns the staring position of the substring.

## Conclusion

And there you have it! You now know how to check if a string contains a substring in JavaScript.

To learn more about JavaScript, head to freeCodeCamp's [JavaScript Algorithms and Data Structures Certification](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/).

It's a free, well-thought-out, and structured curriculum where you will learn interactively. In the end, you will also build 5 projects to claim your certification and solidify your knowledge.

Thanks for reading!



