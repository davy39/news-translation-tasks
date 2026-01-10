---
title: Python .split() – Splitting a String in Python
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2022-05-29T20:27:27.000Z'
originalURL: https://freecodecamp.org/news/python-split-string
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/mariana-jm-UvdzLNj1Vmk-unsplash_jpg.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'Do you want to turn a string into an array of strings using Python? One
  way to do this is with Python''s built-in .split() method.

  Here''s an example of how to do this in the Python command line:

  >>> string1 = "test your might"

  >>> string1.split(" ");

  ...'
---

Do you want to turn a string into an array of strings using Python? One way to do this is with Python's built-in `.split()` method.

Here's an example of how to do this in the Python command line:

```
>>> string1 = "test your might"
>>> string1.split(" ");
# Output: ['test', 'your', 'might']
```

You can open up the Python REPL from your command line. Python is built into Linux, Mac, and Windows. I've written a guide to how you can [open the latest version of Python from your Mac terminal](https://www.freecodecamp.org/news/python-version-on-mac-update/).

Note that the "," argument in the example above is actually optional. Check this out:

```py
>>> string1 = "test your might"
>>> string1.split();
# Output: ['test', 'your', 'might']

>>> string2 = "test,your,might"
>>> s.split();
# Output: ['test', 'your', 'might']
```

The Python `.split()` method is smart enough to infer what the separator should be. In `string1` I used a space. In `string2` I used a comma. In both cases it worked.

## How to use Python .split() with a specific separator

In practice, you will want to pass a `separator` as an argument. Let me show you how to do that:

```
>>> s = "test your might"
>>> s.split(" ");
# Output: ['test', 'your', 'might']

>>> s2 = "test,your,might"
>>> s.split(",");
# Output: ['test', 'your', 'might']
```

The output is the same, but it's cleaner. Here's a more complicated string, where specifying the separator makes bigger difference:

```
>>> string3 = "excellent, test your might, fight, mortal kombat"
>>> string3.split(",");
# Output: ['excellent', ' test your might', ' fight', ' mortal kombat']

>>> string3.split(" ");
# Output: ['excellent,', 'test', 'your', 'might,', 'fight,', 'mortal', 'kombat']
```

As you can see, it's a safer bet to specify a separator.

Also note that leading and trailing spaces may be included in some of the strings in your resulting array. Just something to look out for. 😉

## How do you split a string into multiple strings in Python?

You can split a string into as many parts as you need. This all depends on what character you want to split the string on.

But if you want to ensure that a string does not get split into more than a certain number of parts, you will want to use pass the `maxsplit` argument in your function call.

## How do you split a string into 3 parts in Python?

If you want to put an upper bound on the number of parts your string will be split into, you can specify this using the `maxsplit` argument, like this:

```python
string3 = "excellent, test your might, fight, mortal kombat"

print(string.split(" ", 3))

# Output: ['excellent,', 'test', 'your', 'might, fight, mortal kombat']
# maxsplit=3 means that string will be split into at most three parts
```

As you can see, the `split` function simply stops splitting the string after the 3rd space, so that a total of 4 strings are in the resulting array.

I hope you find this is helpful. Thanks for reading, and happy coding. If you want to learn more, check out [freeCodeCamp's core curriculum](https://www.freecodecamp.org/learn).

