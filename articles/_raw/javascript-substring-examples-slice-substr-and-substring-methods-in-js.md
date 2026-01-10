---
title: JavaScript Substring Examples - Slice, Substr, and Substring Methods in JS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-22T20:38:14.000Z'
originalURL: https://freecodecamp.org/news/javascript-substring-examples-slice-substr-and-substring-methods-in-js
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c0d740569d1a4ca2fa6.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'By Cem Eygi

  In daily programming, we often need to work with strings. Fortunately, there are
  many built-in methods in JavaScript that help us while working with arrays, strings
  and other data types. We can use these methods for various operations lik...'
---

By Cem Eygi

In daily programming, we often need to work with strings. Fortunately, there are many built-in methods in JavaScript that help us while working with arrays, strings and other data types. We can use these methods for various operations like searching, replacing, concatenating strings, and so on.

Getting a substring from a string is one of the most common operations in JavaScript. In this article, you’re going to learn how to get a substring by using 3 different built-in methods. But first, let me explain briefly what a substring is.

### What is a Substring?

A substring is a subset of another string:

```javascript
"I am learning JavaScript and it is cool!"  -->  Original String

"I am learning JavaScript"  -->  Substring

"JavaScript is cool!"  -->  Another Substring
```

Like in the example above, in some cases we need to get one or more substrings from a complete sentence or a paragraph. Now let’s see how to do that in JavaScript in 3 different ways.

**You can also watch the video version of the example usages here:**

%[https://youtu.be/8um4gEiv5mg]

## 1. The substring( ) Method

Let’s start with the substring( ) method. This method basically gets a part of the original string and returns it as a new string. The substring method expects two parameters:

```javascript
string.substring(startIndex, endIndex);
```

* **startIndex**: represents the starting point of the substring
* **endIndex**: represents the ending point of the substring (optional)

Let’s see the usage in an example. Suppose that we have the example string below:

```javascript
const myString = "I am learning JavaScript and it is cool!";
```

Now if we set the startIndex as 0 and the endIndex as 10, then we will get the first 10 characters of the original string:

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Ekran-Resmi-2020-03-21-19.17.10.png)
_**The first character's index is always 0**_

However, if we set only a starting index and no ending index for this example:

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Ekran-Resmi-2020-03-21-19.16.46.png)

Then we get a substring starting from the 6th character until the end of the original string.

**Some additional points:**

* If startIndex = endIndex, the substring method returns an empty string
* If startIndex and endIndex are both greater than the length of the string, it returns an empty string
* If startIndex > endIndex, then the substring method swaps the arguments and returns a substring, assuming as the endIndex > startIndex

## 2. The slice( ) Method

The slice( ) method is similar to the substring( ) method and it also returns a substring of the original string. The slice method also expects the same two parameters:

```javascript
string.slice(startIndex, endIndex);
```

* **startIndex**: represents the starting point of the substring
* **endIndex**: represents the ending point of the substring (optional)

#### **The common points of substring( ) and slice( ) methods:**

* If we don’t set an ending index, then we get a substring starting from the given index number until the end of the original string:

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Ekran-Resmi-2020-03-22-01.03.15.png)

* If we set both the startIndex and the endIndex, then we will get the characters between the given index numbers of the original string:

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Ekran-Resmi-2020-03-22-01.03.43.png)

* If startIndex and endIndex are greater than the length of the string, it returns an empty string

#### **Differences of the slice( ) method:**

* If startIndex > endIndex, the slice( ) method returns an empty string
* If startIndex is a negative number, then the first character begins from the end of the string (reverse):

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Ekran-Resmi-2020-03-22-15.54.09.png)

> **Note:** We can use the slice( ) method also for JavaScript arrays. You can find [here my other article](https://www.freecodecamp.org/news/lets-clear-up-the-confusion-around-the-slice-splice-split-methods-in-javascript-8ba3266c29ae/) about the slice method to see the usage for arrays.

## 3. The substr( ) Method

[According to the Mozilla documents](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/substr), the substr( ) method is considered a legacy function and its use should be avoided. But I will still briefly explain what it does because you might see it in older projects.

The substr( ) method also returns a substring of the original string and expects two parameters as:

```javascript
string.substring(startIndex, length);
```

* **startIndex**: represents the starting point of the substring
* **length**: number of characters to be included (optional)

You can see the difference here: the substr( ) method expects the second parameter as a length instead of an endIndex:

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Ekran-Resmi-2020-03-22-00.40.29-2.png)

In this example, it basically counts 5 characters starting with the given startIndex and returns them as a substring.

However, if we don’t define the second parameter, it returns up to the end of the original string (like the previous two methods do):

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Ekran-Resmi-2020-03-22-00.40.23.png)

> **Note:** All 3 methods return the substring as a new string and they don’t change the original string.

## Wrap up

So these are the 3 different methods to get a substring in JavaScript. There are many other built-in methods in JS which really help us a lot when dealing with various things in programming. If you find this post helpful, please share it on social media.

**If you want to learn more about web development, feel free to** [**follow me on Youtube**](https://www.youtube.com/channel/UC1EgYPCvKCXFn8HlpoJwY3Q)**!**

Thank you for reading!

