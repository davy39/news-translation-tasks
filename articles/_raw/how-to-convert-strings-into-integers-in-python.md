---
title: How to Convert Strings into Integers in Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-16T16:58:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-convert-strings-into-integers-in-python
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9dd6740569d1a4ca39e8.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'Similar to the built-in str() method, Python also offers the handy int()
  method that takes a string object as an argument and returns an integer.

  Example Usage:

  # Here age is a string object

  age = "18"

  print(age)


  # Converting a string to an integer

  ...'
---

Similar to the built-in `str()` method, Python also offers the handy `int()` method that takes a string object as an argument and returns an integer.

#### **Example Usage:**

```py
# Here age is a string object
age = "18"
print(age)

# Converting a string to an integer
int_age = int(age)
print(int_age)
```

**Output:**

```py
18
18
```

Although the output is visually similar, keep in mind that the first line is a string object while the following line is an integer object. This is further illustrated in the next example:

```py
age = "18"
print(age + 2)
```

**Output:**

```py
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: cannot concatenate 'str' and 'int' objects
```

The error should make it clear to you that you need to convert the `age` object to an integer before adding something to it.

```py
age = "18"
age_int = int(age)
print(age_int + 2)
```

**Output:**

```py
20
```

But keep these special cases in mind:

* A floating point (an integer with fractional part) as an argument will return the float rounded down to the nearest whole integer. For example : `print(int(7.9))` will print `7`. On the other hand, `print(int("7.9"))` will result in an error since a float as a string object cannot be converted to an integer.

```py
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '7.9'
```

* Words given as an argument will return the same error. For example, `print(int("one"))` will return:

```py
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'one'
```

