---
title: Python String Methods Explained with Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-30T23:12:00.000Z'
originalURL: https://freecodecamp.org/news/the-string-strip-method-in-python-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d41740569d1a4ca36bc.jpg
tags:
- name: Python
  slug: python
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'String Find Method

  There are two options for finding a substring within a string in Python, find()
  and rfind().

  Each will return the position that the substring is found at. The difference between
  the two is that find() returns the lowest position, a...'
---

## **String Find Method**

There are two options for finding a substring within a string in Python, `find()` and `rfind()`.

Each will return the position that the substring is found at. The difference between the two is that `find()` returns the lowest position, and `rfind()` returns the highest position.

Optional start and end arguments can be provided to limit the search for the substring to within portions of the string.

Example:

```shell
>>> string = "Don't you call me a mindless philosopher, you overweight glob of grease!"
>>> string.find('you')
6
>>> string.rfind('you')
42
```

If the substring is not found, -1 is returned.

```shell
>>> string = "Don't you call me a mindless philosopher, you overweight glob of grease!"
>>> string.find('you', 43)  # find 'you' in string anywhere from position 43 to the end of the string
-1
```

More Information:

String methods [documentation](https://docs.python.org/3/library/stdtypes.html#string-methods).

## **String Join Method**

The `str.join(iterable)` method is used to join all elements in an `iterable` with a specified string `str`. If the iterable contains any non-string values, it raises a TypeError exception.

`iterable`: All iterables of string. Could a list of strings, tuple of string or even a plain string.

#### **Examples**

Join a ist of strings with `":"`

```python
print ":".join(["freeCodeCamp", "is", "fun"])
```

Output

```shell
freeCodeCamp:is:fun
```

Join a tuple of strings with `" and "`

```python
print " and ".join(["A", "B", "C"])
```

Output

```shell
A and B and C
```

Insert a `" "` after every character in a string

```python
print " ".join("freeCodeCamp")
```

Output:

```shell
f r e e C o d e C a m p
```

Joining with empty string.

```python
list1 = ['p','r','o','g','r','a','m']  
print("".join(list1))
```

Output:

```shell
program
```

Joining with sets.

```python
test =  {'2', '1', '3'}
s = ', '
print(s.join(test))
```

Output:

```shell
2, 3, 1
```

#### **More Information:**

[Python Documentation on String Join](https://docs.python.org/2/library/stdtypes.html#str.join)

## **String Replace Method**

The `str.replace(old, new, max)` method is used to replace the substring `old` with the string `new` for a total of `max` times. This method returns a new copy of the string with the replacement. The original string `str` is unchanged.

#### **Examples**

1. Replace all occurrences of `"is"` with `"WAS"`

```python
string = "This is nice. This is good."
newString = string.replace("is","WAS")
print(newString)
```

Output

```python
ThWAS WAS nice. ThWAS WAS good.
```

1. Replace the first 2 occurrences of `"is"` with `"WAS"`

```python
string = "This is nice. This is good."
newString = string.replace("is","WAS", 2)
print(newString)
```

Output

```python
ThWAS WAS nice. This is good.
```

#### **More Information:**

Read more about string replacement in the [Python docs](https://docs.python.org/2/library/string.html#string.replace)

## **String Strip Method**

There are three options for stripping characters from a string in Python, `lstrip()`, `rstrip()` and `strip()`.

Each will return a copy of the string with characters removed, at from the beginning, the end or both beginning and end. If no arguments are given the default is to strip whitespace characters.

Example:

```py
>>> string = '   Hello, World!    '
>>> strip_beginning = string.lstrip()
>>> strip_beginning
'Hello, World!    '
>>> strip_end = string.rstrip()
>>> strip_end
'   Hello, World!'
>>> strip_both = string.strip()
>>> strip_both
'Hello, World!'
```

An optional argument can be provided as a string containing all characters you wish to strip.

```py
>>> url = 'www.example.com/'
>>> url.strip('w./')
'example.com'
```

However, do notice that only the first `.` got stripped from the string. This is because the `strip` function only strips the argument characters that lie at the left or rightmost. Since w comes before the first `.` they get stripped together, whereas ‘com’ is present in the right end before the `.` after stripping `/`.

## String Split Method

The `split()` function is commonly used for string splitting in Python.

#### **The `split()` method**

Template: `string.split(separator, maxsplit)`

`separator`: The delimiter string. You split the string based on this character. For eg. it could be ” ”, ”:”, ”;” etc

`maxsplit`: The number of times to split the string based on the `separator`. If not specified or -1, the string is split based on all occurrences of the `separator`

This method returns a list of substrings delimited by the `separator`

#### **Examples**

Split string on space: ” ”

```python
string = "freeCodeCamp is fun."
print(string.split(" "))
```

Output:

```python
['freeCodeCamp', 'is', 'fun.']
```

Split string on comma: ”,”

```python
string = "freeCodeCamp,is fun, and informative"
print(string.split(","))
```

Output:

```python
['freeCodeCamp', 'is fun', ' and informative']
```

No `separator` specified

```python
string = "freeCodeCamp is fun and informative"
print(string.split())
```

Output:

```python
['freeCodeCamp', 'is', 'fun', 'and', 'informative']
```

Note: If no `separator` is specified, then the string is stripped of **all** whitespace

```python
string = "freeCodeCamp        is     fun and    informative"
print(string.split())
```

Output:

```python
['freeCodeCamp', 'is', 'fun', 'and', 'informative']
```

Split string using `maxsplit`. Here we split the string on ” ” twice:

```python
string = "freeCodeCamp is fun and informative"
print(string.split(" ", 2))
```

Output:

```python
['freeCodeCamp', 'is', 'fun and informative']
```

#### **More Information**

Check out the [Python docs on string splitting](https://docs.python.org/2/library/stdtypes.html#str.split)

