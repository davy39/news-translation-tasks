---
title: Bash Array – How to Declare an Array of Strings in a Bash Script
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-09-09T14:50:00.000Z'
originalURL: https://freecodecamp.org/news/bash-array-how-to-declare-an-array-of-strings-in-a-bash-script
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/pexels-belle-co-1000445.jpg
tags:
- name: arrays
  slug: arrays
- name: Bash
  slug: bash
- name: command line
  slug: command-line
seo_title: null
seo_desc: "By Veronica Stork\nBash scripts give you a convenient way to automate command\
  \ line tasks. \nWith Bash, you can do many of the same things you would do in other\
  \ scripting or programming languages. You can create and use variables, execute\
  \ loops, use con..."
---

By Veronica Stork

Bash scripts give you a convenient way to automate command line tasks. 

With Bash, you can do many of the same things you would do in other scripting or programming languages. You can create and use variables, execute loops, use conditional logic, and store data in arrays. 

While the functionality may be very familiar, the syntax of Bash can be tricky. In this article, you will learn how to declare arrays and then how to use them in your code.

## How to Declare an Array in Bash

Declaring an array in Bash is easy, but pay attention to the syntax. If you are used to programming in other languages, the code might look familiar, but there are subtle differences that are easy to miss.

To declare your array, follow these steps:

1. Give your array a name
2. Follow that variable name with an equal sign. The equal sign _should not_ have any spaces around it
3. Enclose the array in _parentheses_ (not brackets like in JavaScript)
4. Type your strings using quotes, but with _no commas_ between them

Your array declaration will look something like this: 

```sh
myArray=("cat" "dog" "mouse" "frog")
```

That's it! It's that simple.

## How to Access an Array in Bash

There are a couple different ways to loop through your array. You can either loop through the elements themselves, or loop through the indices.

### How to Loop Through Array Elements

To loop through the array elements, your code will need to look something like this: 

```sh
for str in ${myArray[@]}; do
  echo $str
done
```

To break that down: this is somewhat like using `forEach` in JavaScript. For each string (str) in the array (myArray), print that string. 

The output of this loop looks like this:

```
cat
dog
mouse
frog
```

**Note**: The `@` symbol in the square brackets indicates that you are looping through _all_ of the elements in the array. If you were to leave that out and just write `for str in ${myArray}`, only the first string in the array would be printed. 

### How to Loop Through Array Indices

Alternatively, you can loop through the indices of the array. This is like a `for` loop in JavaScript, and is useful for when you want to be able to access the index of each element. 

To use this method, your code will need to look something like the following:

```sh
for i in ${!myArray[@]}; do
  echo "element $i is ${myArray[$i]}"
done
```

The output will look like this:

```
element 0 is cat
element 1 is dog
element 2 is mouse
element 3 is frog
```

**Note**: The exclamation mark at the beginning of the `myArray` variable indicates that you are accessing the _indices_ of the array and not the elements themselves. This can be confusing if you are used to the exclamation mark indicating negation, so pay careful attention to that. 

**Another note**: Bash does not typically require curly braces for variables, but it does for arrays. So you will notice that when you reference an array, you do so with the syntax `${myArray}`, but when you reference a string or number, you simply use a dollar sign: `$i`.

## Conclusion

Bash scripts are useful for creating automated command line behavior, and arrays are a great tool that you can use to store multiple pieces of data. 

Declaring and using them is not hard, but it is different from other languages, so pay close attention to avoid making mistakes.


