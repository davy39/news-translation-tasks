---
title: Python find() – How to Search for a Substring in a String
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-07-25T13:56:30.000Z'
originalURL: https://freecodecamp.org/news/python-find-how-to-search-for-a-substring-in-a-string
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/tarn-nguyen-XlEafYGDvV0-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'When you''re working with a Python program, you might need to search for
  and locate a specific string inside another string.

  This is where Python''s built-in string methods come in handy.

  In this article, you will learn how to use Python''s built-in fin...'
---

When you're working with a Python program, you might need to search for and locate a specific string inside another string.

This is where Python's built-in string methods come in handy.

In this article, you will learn how to use Python's built-in `find()` string method to help you search for a substring inside a string.

Here is what we will cover:

1. [Syntax of the `find()` method](#syntax)
    1. [How to use `find()` with no start and end parameters example](#no-params)
    2. [How to use `find()` with start and end parameters  example](#params)
    3. [Substring not found example](#not-found)
    4. [Is the `find()` method case-sensitive?](#case-sensitive)
2. [`find()` vs `in` keyword](#find-vs-in)
3. [`find()` vs `index()`](#find-vs-index)

## The `find()` Method - A Syntax Overview <a name="syntax"></a>

The `find()` string method is built into Python's standard library.

It takes a substring as input and finds its index - that is, the position of the substring inside the string you call the method on. 

The general syntax for the `find()` method looks something like this:

```
string_object.find("substring", start_index_number, end_index_number)
```

Let's break it down:

- `string_object` is the original string you are working with and the string you will call the `find()` method on. This could be any word you want to search through.
- The `find()` method takes three parameters – one required and two optional.
- `"substring"` is the first *required* parameter. This is the substring you are trying to find inside `string_object`. Make sure to include quotation marks.
- `start_index_number` is the second parameter and it's *optional*. It specifies the starting index and the position from which the search will start. The default value is `0`.
- `end_index_number` is the third parameter and it's also *optional*. It specifies the end index and where the search will stop. The default is the length of the string.
- Both the `start_index_number` and the `end_index_number` specify the range over which the search will take place and they narrow the search down to a particular section.

The return value of the `find()` method is an integer value.

If the substring is present in the string, `find()` returns the index, or the character position, of the **first** occurrence of the specified substring from that given string.

If the substring you are searching for is **not** present in the string, then `find()` will return `-1`. It will not throw an exception.

### How to Use `find()` with No Start and End Parameters Example <a name="no-params"></a>

The following examples illustrate how to use the `find()` method using the only required parameter – the substring you want to search.

You can take a single word and search to find the index number of a specific letter:

```python
fave_phrase = "Hello world!"

# find the index of the letter 'w'
search_fave_phrase = fave_phrase.find("w")

print(search_fave_phrase)

#output

# 6
```

I created a variable named `fave_phrase` and stored the string `Hello world!`.

I called the `find()` method on the variable containing the string and searched for the letter 'w' inside `Hello world!`.

I stored the result of the operation in a variable named `search_fave_phrase` and then printed its contents to the console.

The return value was the index of `w` which in this case was the integer `6`.

Keep in mind that indexing in programming and Computer Science in general always starts at `0` and **not** `1`.

### How to Use `find()` with Start and End Parameters  Example <a name="params"></a>

Using the start and end parameters with the `find()` method lets you limit your search.

For example, if you wanted to find the index of the letter 'w' and start the search from position `3` and not earlier, you would do the following:

```python
fave_phrase = "Hello world!"

# find the index of the letter 'w' starting from position 3
search_fave_phrase = fave_phrase.find("w",3)

print(search_fave_phrase)

#output

# 6
```

Since the search starts at position 3, the return value will be the first instance of the string containing 'w' from that position and onwards.

You can also narrow down the search even more and be more specific with your search with the end parameter:

```python
fave_phrase = "Hello world!"

# find the index of the letter 'w' between the positions 3 and 8
search_fave_phrase = fave_phrase.find("w",3,8)

print(search_fave_phrase)

#output

# 6
```

### Substring Not Found Example <a name="not-found"></a>

As mentioned earlier, if the substring you specify with `find()` is not present in the string, then the output will be `-1` and not an exception.

```python
fave_phrase = "Hello world!"

# search for the index of the letter 'a' in "Hello world"
search_fave_phrase = fave_phrase.find("a")

print(search_fave_phrase)

# -1
```
 
### Is the `find()` Method Case-Sensitive? <a name="case-sensitive"></a>

What happens if you search for a letter in a different case?

```python
fave_phrase = "Hello world!"

#search for the index of the letter 'W' capitalized
search_fave_phrase = fave_phrase.find("W")

print(search_fave_phrase)

#output

# -1
```

In an earlier example, I searched for the index of the letter `w` in the phrase "Hello world!" and the `find()` method returned its position.

In this case, searching for the letter `W` capitalized returns `-1` – meaning the letter is not present in the string.

So, when searching for a substring with the `find()` method, remember that the search will be case-sensitive. 

## The `find()` Method vs the `in` Keyword – What's the Difference? <a name="find-vs-in"></a>

Use the `in` keyword to check if the substring is present in the string in the first place.

The general syntax for the `in` keyword is the following:

```
substring in string
```

The `in` keyword returns a Boolean value – a value that is either `True` or `False`.

```python
>>> "w" in "Hello world!"
True
```

The `in` operator returns `True` when the substring is present in the string.

And if the substring is not present, it returns `False`:

```python
>>> "a" in "Hello world!"
False
```

Using the `in` keyword is a helpful first step before using the `find()` method. 

You first check to see if a string contains a substring, and then you can use `find()` to find the position of the substring. That way, you know for sure that the substring is present.

So, use `find()` to find the index position of a substring inside a string and not to look if the substring is present in the string.

## The `find()` Method vs the `index()` Method – What's the Difference? <a name="find-vs-index"></a>

Similar to the `find()` method, the `index()` method is a string method used for finding the index of a substring inside a string. 

So, both methods work in the same way.

The difference between the two methods is that the `index()` method raises an exception when the substring is not present in the string, in contrast to the `find()` method that returns the `-1` value.

```python
fave_phrase = "Hello world!"

# search for the index of the letter 'a' in 'Hello world!'
search_fave_phrase = fave_phrase.index("a")

print(search_fave_phrase)

#output

# Traceback (most recent call last):
#  File "/Users/dionysialemonaki/python_article/demopython.py", line 4, in <module>
#    search_fave_phrase = fave_phrase.index("a")
# ValueError: substring not found
```

The example above shows that `index()` throws a `ValueError` when the substring is not present.

You may want to use `find()` over `index()` when you don't want to deal with catching and handling any exceptions in your programs.

## Conclusion

And there you have it! You now know how to search for a substring in a string using the `find()` method.

I hope you found this tutorial helpful.

To learn more about the Python programming language, check out [freeCodeCamp's Python certification](https://www.freecodecamp.org/learn/scientific-computing-with-python/).

You'll start from the basics and learn in an interactive and beginner-friendly way. You'll also build five projects at the end to put into practice and help reinforce your understanding of the concepts you learned.

Thank you for reading, and happy coding!

Happy coding!


