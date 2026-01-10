---
title: Python Substring – How to Slice a String
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-07-27T15:24:00.000Z'
originalURL: https://freecodecamp.org/news/python-substring-how-to-slice-a-string
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/pexels-hitesh-choudhary-7775640.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'By Davis David

  In Python, a string is a sequence of characters that may contain special characters
  or alphanumeric characters.

  An example of a string is "we meet on Friday at 08:00 am". And you can access specific
  sub-parts of the string commonly kno...'
---

By Davis David

In Python, a string is a sequence of characters that may contain special characters or alphanumeric characters.

An example of a string is _"we meet on Friday at 08:00 am_". And you can access specific sub-parts of the string commonly known as substrings.

We can define a substring as a sequence of characters within a string. From the previous example, Python substrings can be "Friday", "at", and "meet", for example.

## How to Generate a Substring in Python

Python provides different ways and methods to generate a substring, to check if a substring is present, to get the index of a substring, and more.

You can extract a substring from a string by slicing with indices that get your substring as follows:

`string[start:stop:step]`

* **start** - The starting index of the substring.
* **stop** - The final index of a substring.
* **step** - A number specifying the step of the slicing. The default value is 1.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image--2-.png)

Indices can be positive or negative numbers. The positive indices start from the beginning and go to the end of the string, and the negative indices start from the end and go to the beginning of a string.

In this article, you will learn how to perform various operations related to substrings in Python.

## How to Get the First n Characters of a String in Python

This example will show you how to slice the first 5 characters from the string.

```python
string = "hello world"
print(string[:5])

```

Here you define the stop index which is 5. The start index is by default 0.

The output is `‘hello’`.

## How to Get the Middle Characters of a String via Python Substrings

This example will show you how to slice characters from index 3 to index 5 from the string.

```python
string = "hello world"
print(string[3:5])

```

The output is `'lo’`.

## How to Get the Last Character of a String in Python

To get the last character use the -1 index (negative index). Check out the following example:

```python
string = "freecodecamp"
print(string[-1])

```

The output will be `‘p’`.

## How to Get the Last n Characters of a String in Python

In this example, you will slice the last 4 characters from the string. Here you use the negative index to start slicing from the end of the string.

```python
string = "freecodecamp"
print(string[-4:])

```

The output will be `‘camp’`.

## How to Slice the String with Steps via Python Substrings

You can slice the string with steps after indicating a start-index and stop-index. By default, the step is 1 but in the following example, the step size is 2.

```python
string = "welcome to freecodecamp"
print(string[::2])

```

The output will be `‘wloet fecdcm’`.

## How to Check if a Substring is Present Within a String in Python

Sometimes you want to check if a substring is present in a string. The following example will validate if the substring ‘code’ is in the string:

```python
substring = "code"
string = "welcome to freecodecamp"
print(substring in string)

```

If present, it will return True, otherwise False.  
  
Here, the output will be `True`.

## Another Way to Check if the Python Substring is Present in the String

You can use the `find()` method to check if a substring is present in the string.

Let’s check the following example:

```python
substring = "zz"
string = "hello world"
print(string.find(substring))

```

If it's available it returns the left-most index of the substring, otherwise it returns -1 (which means it's not available).

Here the output is `-1`, which means **“zz”** is not present in “hello world”.

## How to Get the Character of a Given Index in a String in Python

You can choose to slice a specific character according to its index number.

```python
string ="hello world"
print(string[4])

```

The output will be `‘O’`.

## How to Create a List of Substrings from a String in Python

You can use the **`split()`** method to create a list of substrings. Let’s check out the following example:

```python
string = "welcome to freecodecamp platform"
print(string.split())

```

The output will be `['welcome', 'to', 'freecodecamp', 'platform']`

## How to Reverse a String in Python with Negative Steps

To reverse the string, the step must be a negative value, for example -1.

```python
string = "welcome to freecodecamp"
print(string[::-1])

```

The output is `‘pmacedoceerf ot emoclew’`.

## How to Count How Many Times a Substring is Present in a String in Python

You can use the `count()` method to know how many times a particular substring is in a string.

```python
string = "we will have a quick coding lesson this afternoon"
print(string.count('noon'))

```

The output is 1.

## Final Thoughts on Python Substrings

Congratulations 👏👏, you have made it to the end of this article! I hope you have learned something new about Python substrings.

If you learned something new or enjoyed reading this article, please share it so that others can see it. Until then, see you in the next post!

You can also find me on Twitter [@Davis_McDavid](https://twitter.com/Davis_McDavid?ref=hackernoon.com).

And you can read more articles like this [here](https://hackernoon.com/u/davisdavid?ref=hackernoon.com)

