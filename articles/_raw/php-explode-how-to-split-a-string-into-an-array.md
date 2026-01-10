---
title: PHP Explode – How to Split a String into an Array
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-10-17T17:19:46.000Z'
originalURL: https://freecodecamp.org/news/php-explode-how-to-split-a-string-into-an-array
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/explode.png
tags:
- name: arrays
  slug: arrays
- name: PHP
  slug: php
seo_title: null
seo_desc: 'The PHP explode() function converts a string to an array. Each of the characters
  in the string is given an index that starts from 0. Like the built-in implode()
  function, the explode function does not modify the data (string).

  Syntax of the explode()...'
---

The PHP `explode()` function converts a string to an array. Each of the characters in the string is given an index that starts from 0. Like the built-in `implode()` function, the explode function does not modify the data (string).

### Syntax of the `explode()` Function

The `explode()` function takes in three parameters:
- the separator
- the string to convert to an array
- and the limit

The full syntax looks like this:
```js
explode(separator, string, limit)
```

Unlike `implode()` which works even if the separator is not provided, the `explode()` function won’t work without the separator. So, just like the string split into an array, the separator is required. You can use the limit parameter to specify the number of arrays expected. It is optional.

## Examples of `implode()`

Let's say that I have the string "Hello World". If the string is passed into an `explode()` function, `Hello` takes an index of 0 in the array, and `World` takes an index of 1. Remember that arrays use zero-based indexing.

```js
$str = "Hello world";
$newStr = explode(" ", $str);

// We are printing an array, so we can use print_r()
print_r($newStr); 
```

![ss1-3](https://www.freecodecamp.org/news/content/images/2022/10/ss1-3.png)

If you specify a limit in the `explode()` function, the index(es) won’t be more than that number. For example, if you specify 2, all the strings would show, but the index won’t be more than 2.

```js
$str = "CSS, HTML, PHP, Java, JavaScript";
$newStr = explode(" ", $str, 2);

// We are printing an array, so we can use print_r()
print_r($newStr); 
```

![ss2-3](https://www.freecodecamp.org/news/content/images/2022/10/ss2-3.png) 

You can see that the first element takes an index of 0 and the rest of the comma-separated elements take 1. The index is not more than the limit of 2 specified.

The `explode()` function looks at spaces in the string to split the string into an array. If you type two different words together, they are treated as one:

```js
$str = "CSS HTMLPHP Java JavaScript";
$newStr = explode( " ", $str);

// We are printing an array, so we can use print_r()
print_r($newStr); 
```
![ss5-2](https://www.freecodecamp.org/news/content/images/2022/10/ss5-2.png)

You can see that HTML and PHP got ptinted together because there was no space between them.

## Conclusion
This article showed you how to use the `explode()` function in PHP. 

Note that unlike `implode()` which works without the separator, the separator is very important in `explode()`. If you don’t specify a separator, `explode()` won’t work as expected.

```js
$str = "CSS, HTML, PHP, Java, JavaScript";
$newStr = explode($str, 2);

// We are printing an array, so we can use print_r()
print_r($newStr); 
```

![ss3-3](https://www.freecodecamp.org/news/content/images/2022/10/ss3-3.png)

And if you leave the separator as an empty string, you get an error:

![ss4-3](https://www.freecodecamp.org/news/content/images/2022/10/ss4-3.png) 
 
Thank you for reading.


