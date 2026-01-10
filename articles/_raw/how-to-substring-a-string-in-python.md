---
title: How to Substring a String in Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-03T21:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-substring-a-string-in-python
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e45740569d1a4ca3c3e.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'Python offers many ways to substring a string. This is often called "slicing".

  Here is the syntax:

  string[start:end:step]


  Where,

  start: The starting index of the substring. The character at this index is included
  in the substring. If start is not in...'
---

Python offers many ways to substring a string. This is often called "slicing".

Here is the syntax:

```python
string[start:end:step]
```

Where,

`start`: The starting index of the substring. The character at this index is included in the substring. If `start` is not included, it is assumed to equal to 0.

`end`: The terminating index of the substring. The character at this index is _not_ included in the substring. If `end` is not included, or if the specified value exceeds the string length, it is assumed to be equal to the length of the string by default.

`step`: Every "step" character after the current character to be included. The default value is 1. If `step` is not included, it is assumed to be equal to 1.

### Here's an Interactive Scrim of How to Substring a String in Python

<iframe src="https://scrimba.com/scrim/cPmJkytm?embed=freecodecamp,mini-header,no-sidebar" width="100%" height="420"></iframe>

## Basic Usage

`string[start:end]`: Get all characters from `start` to `end` - 1

`string[:end]`: Get all characters from the beginning of the string to `end` - 1

`string[start:]`: Get all characters from `start` to the end of the string

`string[start:end:step]`: Get all characters from `start` to `end` - 1, not including every `step` character

## Examples

**1. **Get the first 5 characters of a string****

```python
string = "freeCodeCamp"
print(string[0:5])
```

Output:

```shell
> freeC
```

Note: `print(string[:5])` returns the same result as `print(string[0:5])`

**2. **Get a substring** 4 characters long,** starting **from the 3rd character of the string**

```python
string = "freeCodeCamp"
print(string[2:6])
```

Output:

```shell
> eeCo
```

**3. **Get the last character of the string****

```python
string = "freeCodeCamp"
print(string[-1])
```

Output:

```shell
> p
```

Notice that the `start` or `end` index can be a negative number. A negative index means that you start counting from the end of the string instead of the beginning (from the right to left).

Index -1 represents the last character of the string, -2 represents the second to last character and so on.

**4. **Get the last 5 characters of a string****

```python
string = "freeCodeCamp"
print(string[-5:])
```

Output:

```shell
> eCamp
```

**5. **Get a substring which contains all characters except the last 4 characters and the 1st character****

```python
string = "freeCodeCamp"
print(string[1:-4])
```

Output:

```shell
> reeCode
```

**6. **Get every other character from a string****

```python
string = "freeCodeCamp"
print(string[::2])
```

Output:

```shell
> feCdCm
```

