---
title: Python str() Function – How to Convert to a String
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-04-04T12:48:48.000Z'
originalURL: https://freecodecamp.org/news/python-str-function-how-to-convert-to-a-string
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/str-2.png
tags:
- name: Python
  slug: python
- name: Python 3
  slug: python3
seo_title: null
seo_desc: 'Python’s primitive data types include float, integer, Boolean, and string.
  The programming language provides several functions you can use to convert any of
  these data types to the other.

  One of those functions we’ll look at in this article is str()....'
---

Python’s primitive data types include float, integer, Boolean, and string. The programming language provides several functions you can use to convert any of these data types to the other.

One of those functions we’ll look at in this article is `str()`. It’s a built-in function you can use to convert any non-string object to a string.


## What is the `str()` Function?
The `str()` function takes a compulsory non-string object and converts it to a string. This object the `str()` function takes can be a float, integer, or even a Boolean.

Apart from the compulsory data to convert to a string, the `str()` function also takes two other parameters. Here are all the parameters it takes:

* **object**: the data you want to convert to a string. It’s a compulsory parameter. If you don’t provide it, `str()` returns an empty string as the result.
* **encoding**: the encoding of the data to convert. It’s usually `UTF-8`. The default is `UTF-8` itself.
* **errors**: specifies what to do if decoding fails. The values you can use for this parameter include `strict`, `ignore`, `replace`, and others.


## Basic Syntax of the `str()` Function
You have to comma-separate each of the parameters in the `str()` function, and the values of both encoding and errors have to be in strings:

```py
str(object_to_convert, encoding='encoding', errors='errors')
``` 

## How to Use the `str()` Function
First, let’s see how to use all the parameters of the `str()` function:

```py
my_num = 45
converted_my_num = str(my_num, encoding='utf-8', errors='errors')

print(converted_my_num)
```

If you run the code, you’ll get this error:

```py
converted_my_num = str(my_num, encoding='utf-8', errors='errors')
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: decoding to str: need a bytes-like object, int found
```

This error occurs because you’re using the encoding parameter without providing a bytes object. In this case, you don’t need the `encoding` and `errors` at all. You only need the number you want to convert:

```py
my_num = 45
converted_my_num = str(my_num)

print(converted_my_num) # 45
```

If you’re insistent on using the `encoding` and `errors` parameters, then the object to convert must be a bytes object:

```py
my_num = b'45'
converted_my_num = str(my_num, encoding='utf-8', errors='strict')

print(converted_my_num) # 45
```

### How to Convert an Integer and Float to String with the `str()` Function
You can convert an integer or float to a string with str() this way:

```py
my_int = 45
my_float = 34.8

# Convert both to string
converted_my_int = str(my_int)
converted_my_float = str(my_float)

print(converted_my_int) # output: 45
print(converted_my_float) # output: 34.8
```

You can see I got the numbers back. You can also verify that the types of the results are strings with the `type()` function:

```py
my_int = 45
my_float = 34.8

# Convert both to string
converted_my_int = str(my_int)
converted_my_float = str(my_float)

print("Converted integer is", converted_my_int, "and the type of the result is ", type(converted_my_int)) # Converted integer is 45 and the type of the result is <class 'str'>
print("Converted float is", converted_my_float, "and the type of the result is ", type(converted_my_float)) # Converted float is 34.8 and the type of the result is <class 'str'>
```

You can see the type of the converted integer and float is a string.

### How to Convert a Boolean to String with the `str()` Function
You can also convert a Boolean to a string if you want:

```py
my_true_bool = True
my_false_bool = False

converted_my_true_bool = str(my_true_bool)
converted_my_false_bool = str(my_false_bool)

print("Converted Boolean is", converted_my_true_bool, "and the type of the result is ", type(converted_my_true_bool)) # Converted Boolean is True and the type of the result is <class 'str'>

print("Converted Boolean is", converted_my_false_bool, "and the type of the result is ", type(converted_my_false_bool)) # Converted Boolean is False and the type of the result is <class 'str'>
```

## How to use the `encoding` Parameter of the `str()` Function for Encoding and Decoding Objects
The `encoding` parameter is useful for encoding a string to bytes and decoding a bytes to strings.

To encode a string to bytes, for example, you have to use the `encoding()` method this way:

```py
my_str = "Hello world!"
my_bytes = my_str.encode(encoding='UTF-8', errors='strict')

print(my_bytes) # Output: b'Hello, world!'
print(type(my_bytes)) # Output: <class 'bytes'>
```

To decode a bytes to string, you should use the `decode()` method this way:

```py
my_bytes = b'Hello, world!'
my_str = my_bytes.decode(encoding='UTF-8', errors='strict')

print(my_str)  # Output: "Hello, world!"
print(type(my_str))  # Output: <class 'str'>
```


## Conclusion
You’ve seen that the `str()` function is instrumental in converting non-string objects and primitive data types to strings.

You might be wondering if you can use the `str()` function to convert iterable data like lists, tuples, and dictionaries to a string. Well, you don’t get an error if you do that, what you’ll get back is the iterable as it is:

```py
my_list = ['ant', 'soldier', 'termite']
converted_my_list = str(my_list)

print(converted_my_list) # ['ant', 'soldier', 'termite']
```

To convert the list to a string, you have to use the `join()` method:

```py
my_list = ['ant', 'soldier', 'termite']
converted_my_list =' '.join(my_list)

print(converted_my_list) # ant, soldier, termite
print(type(converted_my_list)) # <class 'str'>
```

Same thing is applicable to dictionaries and tuples.

Thank you for reading.


