---
title: PHP Implode – Convert Array to String with Join
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-10-06T16:14:10.000Z'
originalURL: https://freecodecamp.org/news/php-implode-convert-array-to-string-with-join
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/implode.png
tags:
- name: arrays
  slug: arrays
- name: PHP
  slug: php
seo_title: null
seo_desc: "In PHP, the implode() function is a built-in function that takes an array\
  \ and converts it to a string. implode() doesn’t modify the original array. \nIt\
  \ doesn’t matter whether the array is an indexed or associative array. Once you\
  \ pass in the array to..."
---

In PHP, the `implode()` function is a built-in function that takes an array and converts it to a string. `implode()` doesn’t modify the original array. 

It doesn’t matter whether the array is an indexed or associative array. Once you pass in the array to `implode()`, it joins all the values to a string.

## PHP `implode()` Syntax
`implode()` takes in two values as parameters – the separator and the array you want to convert to a string. 

The separator could be any character or an empty string. It is valid as long as you specify it in quotes. If you don’t pass in the separator, `implode()` still works. The array on the other hand could be an associative array or an indexed array.

NB: `implode()` doesn’t work with nested arrays.

The full syntax of an `implode()` looks like this:

```js
implode(" ", $array);
```

In the syntax above, an empty space (" ") is the separator, and `$array` is the array.

## Examples of Implode with an Indexed Array
In PHP, an indexed array is what it sounds like – each value in the array has an index automatically assigned to it. You can also assign the indexes if you want.

Below is an example of how `implode()` works with an indexed array:

```js
<?php
$langs = array("PHP", "JavaScript", "Python", "C++", "Ruby"); 

$newLangs = implode($langs);
// Since we are printing a string, we can use echo to display the output in the browser
echo $newLangs;
?>
```

![ss1-2](https://www.freecodecamp.org/news/content/images/2022/10/ss1-2.png) 

Note that I did not pass in a separator and `implode()` still works fine.
In the example below, I passed in an empty space, comma, and hyphen as separators:

```js
<?php
$langs = array("PHP", "JavaScript", "Python", "C++", "Ruby"); 

$newLangsSpace = implode(" ", $langs);
$newLangsComma = implode(", ", $langs);
$newLangsHyphen = implode("-", $langs);

// Since we are printing a string, we can use echo to display the output in the browser
echo $newLangsSpace."<br>"."<br>";
echo $newLangsComma."<br>"."<br>";
echo $newLangsHyphen ."<br>";
?>
```

![ss2-2](https://www.freecodecamp.org/news/content/images/2022/10/ss2-2.png) 

You can see it’s better to specify a separator so you can see the values well.

## Examples of Implode with an Associative Array
You define a named index with an associative array. Let’s see how `implode()` works with associative arrays.

```js
<?php
$person = [
    'first_name' => "Kolade",
    'last_name' => "Chris",
    'likes' => "football and Pro-wrestling",
    'email' => "kolade@gmail.com",
];
//That's not my email. Don't bother sending me a message.

$newPerson = implode(" ", $person);
echo $newPerson."<br>";
?>
```

![ss3-2](https://www.freecodecamp.org/news/content/images/2022/10/ss3-2.png) 

You can see the indexes were not printed. To print the indexes too, you need to attach the array to the `array_keys()` method while printing the array:

```js
<?php
$person = [
    'first_name' => "Kolade",
    'last_name' => "Chris",
    'likes' => "football and Pro-wrestling",
    'email' => "kolade@gmail.com",
];
// That’s not my email. Don't bother sending me a message.

$newPersonValues = implode(", ", $person)."<br>";
$newPersonKeys = implode(", ", array_keys($person));

echo $newPersonKeys."<br>"; 
echo $newPersonValues;
?>
```

![ss4-2](https://www.freecodecamp.org/news/content/images/2022/10/ss4-2.png) 

To prove that the original array is never modified, I’ll print the array alongside the imploded variables:

```js
<?php
$person = [
    'first_name' => "Kolade",
    'last_name' => "Chris",
    'likes' => "football and Pro-wrestling",
    'email' => "kolade@gmail.com",
];
// That's not my email. Don't bother sending me a message.

$newPersonValues = implode(", ", $person)."<br>";
$newPersonKeys = implode(", ", array_keys($person));

echo $newPersonKeys."<br>"; 
echo $newPersonValues."<br>";

print_r($person);
?>
```

You can use the PHP View Chrome extension to format your printed array so it can look better:

![phpViewer](https://www.freecodecamp.org/news/content/images/2022/10/phpViewer.png) 

## Final Thoughts
In this article, you learned about the `implode()` function in PHP and how it works. We looked at how the `implode()` function works with both indexed and associative arrays, too, with examples.

Don’t forget that `implode()` doesn’t work with nested arrays (multidimensional arrays). In fact, I can prove it:

```js
<?php
$persons = array (
  array("Kolade", 22, 03),
  array("Yemi", 15, 12),
  array("Cook", 07, 01),
  array("Oliver", 19, 01)
);

$newPersons = implode($persons);
print_r($newPersons);
?>
```

![ss6-2](https://www.freecodecamp.org/news/content/images/2022/10/ss6-2.png) 

It doesn’t work that way because `implode()` only works with flat arrays (`[ ]`) instead of multidimensional arrays (`[ [ ] ]`). Implode looks at the first array, and once it sees that the first array has many arrays in it, it throws an error.

Thank you for reading.


