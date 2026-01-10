---
title: Python Bytes to String – How to Convert a Str to Bytes and Back Again
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2024-04-16T20:07:39.959Z'
originalURL: https://freecodecamp.org/news/python-bytes-to-string-code-examples
coverImage: https://cdn.hashnode.com/res/hashnode/image/stock/unsplash/zGuBURGGmdY/upload/6d5b13a8926b01576cba45ee0d72bfc8.jpeg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'You can use bytes in Python to represent data in binary form. In this article,
  you''ll learn how to convert bytes to a string, and vice versa.

  Before we look at the conversions, let''s talk about how bytes work in Python. You
  can skip to the next secti...'
---

You can use bytes in Python to represent data in binary form. In this article, you'll learn how to convert bytes to a string, and vice versa.

Before we look at the conversions, let's talk about how bytes work in Python. You can skip to the next section if you already understand this, or you're just interested in the conversions.

## How Bytes Work in Python

You can create byte literals by prefixing the `b` notation. This tells the Python interpreter that a set of characters should be treated as bytes. Here's an example:

```python
byte_data = b'Hello'
```

In the code above, we prefixed `b` right before the string value: `b'Hello'`. If you print the characters in the string, you'll get a binary value for each. That is:

```python
byte_data = b'Hello'
print(byte_data[0]) # 72
```

So instead of "H", 72 was returned. If you go on to print the value of each index in the sequence, you should get their binary values:

```python
byte_data = b'Hello'
print(byte_data[0]) # 72 => H
print(byte_data[1]) # 101 => e
print(byte_data[2]) # 108 => l
print(byte_data[3]) # 108 => l
print(byte_data[4]) # 111 => 0
```

Now let's talk about how to convert a string to bytes, and how to convert bytes to a string.

# How to Convert a Str to Bytes in Python

You can use the `encode()` method to convert a string to bytes in Python. The method simply encodes a string using a specific encoding like UTF-8, ASCII, and so on.

Here's an example:

```python
string_data = "Hello"
print(string_data[0]) # H
```

In the code above, we created a string called `string_data` with a value of "Hello". We also printed the first character of the string, which is "H".

Now let's convert the string to bytes using the `encode()` method:

```python
string_data = "Hello"
byte_data = string_data.encode('utf-8')
print(byte_data[0]) # 72
```

We converted the `string_data` variable to bytes using the `encode()` method which took "utf-8" as a parameter. We stored this conversion in the `byte_data` variable: `byte_data = string_data.encode('utf-8')`.

Lastly, we printed the first character of the `byte_data` variable and got a binary value: `print(byte_data[0]) # 72`.

# How to Convert Bytes to a Str to in Python

You can use the `decode()` method to convert bytes to a string in Python. It works just like the `encode()` variable: attach the variable to be converted using dot notation and specify the encoding type as the method's parameter.

Here's an example:

```python
byte_data = b'Hello'
string_data = byte_data.decode('utf-8')
print(string_data[0]) # H
```

In the code above, we created a bytes object called `byte_data`.

Using the `decode()` method, we converted it to a string and stored it in a `string_data` variable: `string_data = byte_data.decode('utf-8')`.

When you print the characters of the `string_data` variable, you should get string characters instead of binary values: `print(string_data[0]) # H`

# Conclusion

In this article, you learned how to use bytes in Python. You also learned two conversion methods:

* How to convert a string to bytes using the `encode()` method.
    
* How to convert bytes to a string using the `decode()` method.
    

Happy coding!
