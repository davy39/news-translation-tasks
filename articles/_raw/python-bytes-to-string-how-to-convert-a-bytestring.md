---
title: Python Bytes to String – How to Convert a Bytestring
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-04-10T22:52:41.000Z'
originalURL: https://freecodecamp.org/news/python-bytes-to-string-how-to-convert-a-bytestring
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/Shittu-Olumide-Python-Bytes-to-String---How-to-Convert-a-Bytestring.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'By Shittu Olumide

  In this article, you will learn how to convert a bytestring. I know the word bytestring
  might sound technical and difficult to understand. But trust me – we will break
  the process down and understand everything about bytestrings bef...'
---

By Shittu Olumide

In this article, you will learn how to convert a bytestring. I know the word bytestring might sound technical and difficult to understand. But trust me – we will break the process down and understand everything about bytestrings before writing the Python code that converts bytes to a string.

So let's start by defining a bytestring.

## What is a bytestring?

A bytestring is a sequence of bytes, which is a fundamental data type in computing. They are typically represented using a sequence of characters, with each character representing one byte of data. 

Bytes are often used to represent information that is not character-based, such as images, audio, video, or other types of binary data. 

In Python, a bytestring is represented as a sequence of bytes, which can be encoded using various character encodings such as UTF-8, ASCII, or Latin-1. It can be created using the `bytes()` or `bytearray()` functions, and can be converted to and from strings using the `encode()` and `decode()` methods.

Note that in Python 3.x, bytestrings and strings are distinct data types, and cannot be used interchangeably without encoding or decoding.

This is because Python 3.x uses Unicode encoding for strings by default, whereas previous versions of Python used ASCII encoding. So when working with bytestrings in Python 3.x, it's important to be aware of the encoding used and to properly encode and decode data as needed.

## How to Convert Bytes to a String in Python 

Now that we have the basic understanding of what bytestring is, let's take a look at how we can convert bytes to a string using Python methods, constructors, and modules.

### Using the `decode()` method

`decode()` is a method that you can use to convert bytes into a string. It is commonly used when working with text data that is encoded in a specific character encoding, such as UTF-8 or ASCII. It simply works by taking an encoded byte string as input and returning a decoded string.

Syntax:

```py
decoded_string = byte_string.decode(encoding)

```

Where `byte_string` is the input byte string that we want to decode and `encoding` is the character encoding used by the byte string.

Here is some example code that demonstrates how to use the `decode()` method to convert a byte string to a string:

```py
# Define a byte string
byte_string = b"hello world"

# Convert the byte string to a string using the decode() method
decoded_string = byte_string.decode("utf-8")

# Print the decoded string
print(decoded_string)

```

In this example, we define a byte string `b"hello world"` and convert it to a string using the `decode()` method with the UTF-8 character encoding. The resulting decoded string is `"hello world"`, which is then printed to the console.

Note that the `decode()` method can also take additional parameters, such as `errors` and `final`, to control how decoding errors are handled and whether the decoder should expect more input.

### Using the `str()` constructor 

You can use the `str()` constructor in Python to convert a byte string (bytes object) to a string object. This is useful when we are working with data that has been encoded in a byte string format, such as when reading data from a file or receiving data over a network socket.

The `str()` constructor takes a single argument, which is the byte string that we want to convert to a string. If the byte string is not valid ASCII or UTF-8, we will need to specify the encoding format using the `encoding` parameter.

Example:

```py
# Define a byte string
byte_string = b"Hello, world!"

# Convert the byte string to a string using the str() constructor
string = str(byte_string, encoding='utf-8')

# Print the string
print(string)

```

Output:

```bash
Hello, world!

```

In this example, we define a byte string `b"Hello, world!"` and use the `str()` constructor to convert it to a string object. We specify the encoding format as `utf-8` using the `encoding` parameter. Finally, we print the resulting string to the console.

### Using the bytes() constructor 

We can also use the `bytes()` constructor, a built-in Python function used to create a new `bytes` object. It takes an iterable of integers as input and returns a new `bytes` object that contains the corresponding bytes. This is useful when we are working with binary data, or when converting between different types of data that use bytes as their underlying representation.

Example:

```py
# Define a string
string = "Hello, world!"

# Convert the string to a bytes object
bytes_object = bytes(string, 'utf-8')

# Print the bytes object
print(bytes_object)

# Convert the bytes object back to a string
decoded_string = bytes_object.decode('utf-8')

# Print the decoded string
print(decoded_string)

```

Output:

```bash
b'Hello, world!'
Hello, world!

```

In this example, we start by defining a string variable `string`. We then use the `bytes()` constructor to convert the string to a bytes object, passing in the string and the encoding (`utf-8`) as arguments. We print the resulting bytes object to the console.

Next, we use the `decode()` method to convert the bytes object back to a string, passing in the same encoding (`utf-8`) as before. We print the decoded string to the console as well.

### Using the `codecs` module

The `codecs` module in Python provides a way to convert data between different encodings, such as between byte strings and Unicode strings. It contains a number of classes and functions that you can use to perform various encoding and decoding operations.

For us to be able to convert Python bytes to a string, we can use the `decode()` method provided by the `codecs` module. This method takes two arguments: the first is the byte string that we want to decode, and the second is the encoding that we want to use. 

Example:

```py
import codecs

# byte string to be converted
b_string = b'\xc3\xa9\xc3\xa0\xc3\xb4'

# decoding the byte string to unicode string
u_string = codecs.decode(b_string, 'utf-8')

print(u_string)

```

Output:

```bash
éàô

```

In this example, we have a byte string `b_string` which contains some non-ASCII characters. We use the `codecs.decode()` method to convert this byte string to a Unicode string. 

The first argument to this method is the byte string to be decoded, and the second argument is the encoding used in the byte string (in this case, it is `utf-8`). The resulting Unicode string is stored in `u_string`.

To convert a Unicode string to a byte string using the `codecs` module, we use the `encode()` method. Here is an example:

```py
import codecs

# unicode string to be converted
u_string = 'This is a test.'

# encoding the unicode string to byte string
b_string = codecs.encode(u_string, 'utf-8')

print(b_string)

```

Ouput:

```bash
b'This is a test.'

```

In this example, we have a Unicode string `u_string`. We use the `codecs.encode()` method to convert this Unicode string to a byte string. The first argument to this method is the Unicode string to be encoded, and the second argument is the encoding to use for the byte string (in this case, it is `utf-8`). The resulting byte string is stored in `b_string`.

## Conclusion

Understanding bytestrings and string conversion is important because it is a fundamental aspect of working with text data in any programming language. 

In Python, this is particularly relevant due to the increasing popularity of data science and natural language processing applications, which often involve working with large amounts of text data.

For further learning, check out these helpful resources:

1. [The difference between bytes and str in Python](https://stackoverflow.com/questions/6224052/what-is-the-difference-between-a-string-and-a-byte-string)
2. [What every developer should know about encoding](https://www.freecodecamp.org/news/everything-you-need-to-know-about-encoding/)
3. [Python documentation on the codecs module](https://docs.python.org/3/library/codecs.html)
4. [Python documentation on bytes methods](https://docs.python.org/3/library/stdtypes.html#bytes-methods)
5. [Python documentation on string methods](https://docs.python.org/3/library/stdtypes.html#string-methods)

Let's connect on [Twitter](https://www.twitter.com/Shittu_Olumide_) and on [LinkedIn](https://www.linkedin.com/in/olumide-shittu). You can also subscribe to my [YouTube](https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A) channel.

Happy Coding!

