---
title: Trim a String in Python – How to Strip Trailing Whitespace
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2023-03-03T17:28:17.000Z'
originalURL: https://freecodecamp.org/news/how-to-strip-trailing-whitespace-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/pexels-christina-morillo-1181359.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'Python has three built-in methods for trimming leading and trailing whitespace
  and characters from strings: strip(), lstrip(), and rstrip().

  In this article, I will explain how to remove trailing whitespace in Python using
  the rstrip() method.

  Let''s ...'
---

Python has three built-in methods for trimming leading and trailing whitespace and characters from strings: `strip()`, `lstrip()`, and `rstrip()`.

In this article, I will explain how to remove trailing whitespace in Python using the `rstrip()` method.

Let's get into it!

## How To Trim Whitespace From A String in Python
To trim a string and remove any whitespace, whether leading or trailing, use the `strip()` method.

When the `strip()` method has no argument, it removes both leading and trailing whitespace from a string.

So, if you have whitespace at the start or end of a word or phrase, `strip()` alone, by default, will remove it.

Let's take the following example:

```python
fave_phrase = " Hello World "
```

I stored the phrase `" Hello World "` in a variable named `fave_phrase`.

The phrase has leading whitespace — a space before the first character, `H`. 

The phrase also has trailing whitespace — a space after the last character, `d`.

I then print the contents of `fave_phrase` to the console:

```python
print(fave_phrase)

# output

 Hello World 
```

To remove both leading *and* trailing whitespace from the phrase, call the `strip()` method on `fave_phrase` and store the result in the variable with the name` trimmed_fave_phrase` like so:

```python
fave_phrase = " Hello World "

trimmed_fave_phrase = fave_phrase.strip()

print(trimmed_fave_phrase)

# output

Hello World
```

Now any whitespace at the beginning and end of the string has gone!

### How to Remove Only Any Trailing Whitespace in Python
But what if you want to remove only trailing whitespace (that is, any whitespace at the end of the string)?

Python has the `rstrip()` method you can use to do just that:

```python
fave_phrase = " Hello World "

trimmed_fave_phrase = fave_phrase.rstrip()

print(trimmed_fave_phrase)

# output

 Hello World
```

In the example above, the leading space at the beginning of the string remains preserved, and the trailing space gets removed.

So, with `rstrip()`, the whitespace gets removed only from the end of the string.

## Conclusion
And there you have it! You now know how to strip any trailing whitespace from a string in Python.

To learn more about Python, check out [freeCodeCamp's Python for beginners course](https://www.freecodecamp.org/news/python-programming-course/).

Thanks for reading, and happy coding!


