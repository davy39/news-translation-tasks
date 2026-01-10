---
title: How to Parse a String in Python – Parsing Strings Explained
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-05-04T21:04:02.000Z'
originalURL: https://freecodecamp.org/news/how-to-parse-a-string-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/split-and-split-methods-in-python.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "Parsing a string can mean different things in Python. You can parse a string\
  \ by splitting or extracting the substrings. \nYou can also parse a string by converting\
  \ it to an integer or float variable. Although this should be categorized as a type\
  \ conve..."
---

Parsing a string can mean different things in Python. You can parse a string by splitting or extracting the substrings. 

You can also parse a string by converting it to an integer or float variable. Although this should be categorized as a type conversion operation, you'll come across resources that refer to it as string parsing. 

In this article, you'll learn how to parse a string using the `split()` and `strip()` methods. You'll also learn how to convert a string to an integer using the `int()` function.

## How To Parse a String in Python Using the `split()` Method

You can use the `split()` method in Python to "split" substrings of a string into a list. 

Here's what the parameter looks like: 

```txt
string.split(separator, maxsplit)
```

The `split()` method has two optional parameters:

* `separator` specifies where to start splitting from (you'll understand this better with the examples in the next section). 
* `maxsplit` specifies the maximum number of splits. 

### `split()` Method Example #1 - How To Use the Separator Parameter

```python
favorite_languages = "JavaScript, Python, and Java"

lang_split = favorite_languages.split(",")

print(lang_split)
# ['JavaScript', ' Python', ' and Java']

```

In the example above, we created a string called `favorite_languages` which had three substrings: "JavaScript, Python, and Java". 

Using the `split()` method, we specified that each substring should be split after each comma in the string: `favorite_languages.split(",")`. 

The result was a list of each substring: ['JavaScript', ' Python', ' and Java']. 

This example shows how to use the first parameter of the `split()` method. The next example will help you understand the second parameter. 

### `split()` Method Example #2 - How To Use the Maxsplit Parameter

```python
favorite_languages = "JavaScript, Python, and Java"

lang_split = favorite_languages.split(",", 1)

print(lang_split)
# ['JavaScript', ' Python, and Java']
```

In the code above, we made use of the `maxsplit` parameter which specifies the number of splits to be performed. 

So `favorite_languages.split(",", 1)` means that only one substring should be split, while the rest would remain as they were in the original string. 

In the output of the code, only JavaScript was split, while Python and Java retained their initial positions in the string. That is: `['JavaScript', ' Python, and Java']`. 

## How To Parse a String in Python Using the `strip()` Method

You can use the `strip()` method to remove white spaces or specified characters in a string.

Here's what the syntax looks like:

```python
string.strip([chars])
```

The `chars` parameter specifies the set of characters to be removed. This parameter is optional, so leaving the parenthesis empty will only remove white spaces. 

Let's see some examples.

### `strip()` Method Example #1

```python
username = "       Doe      "

user = username.strip()

print(user) 
# Doe
```

In the example above, we had a string with leading and trailing whitespace characters: "       Doe      ". 

Using the strip method without any parameter, we got rid of the whitespaces: `username.strip()`. 

In the next example, we'll pass in parameters to the `strip()` method. 

### `strip()` Method Example #2

In this section, we'll use a string that has different characters in it that aren't whitespaces: 

```python
username = "=+---Doe---+="
```

The goal here is to get rid of the unwanted characters (=+-) found in the `username` variable.

If you use the `strip()` method without any parameters, it won't get rid of those characters. Without parameters, the `strip()` method only removes whitespaces. 

To remove the characters in the string, you have to use them as a parameter to tell the `strip()` method that they should be removed. That is: 

```python
username = "=+---Doe---+="

user = username.strip("=+-")

print(user) 
# Doe
```

In the code above, we passed in the characters to be removed from the string as a parameter to the `strip()` method: `username.strip("=+-")`. 

Note that you have to nest those characters in quotation marks ("=+-").

## How To Convert a String to an Integer Using the `int()` Function

Data type conversion helps you perform certain operations that involve incompatible data types. 

For instance, the example below shows what happens when you try to add an integer and a string: 

```python
age = "300"

print(age + 300) 
# TypeError: can only concatenate str (not "int") to str
```

In the code above, we created a string value with a value of "300". When we tried adding it to an integer value of 300, we got an error.

The error is thrown because the compiler assumes we're trying to add two strings. [String concatenation in Pytho](https://www.freecodecamp.org/news/python-concatenate-strings-how-to-combine-and-append-strings-in-python/)n cannot be performed using a string and an integer. 

To solve this problem, you can convert the string to an integer before using it in a mathematical operation. 

Here's how you can do that using the `int()` function:

```python
age = "300"

age_to_int = int(age)

print(age_to_int + 300) 
# 600
```

In the code above, we used the `int()` function to convert the `age` string to an integer: `int(age)`. 

Now, you're to use the variable as an integer. 

A common use case for converting from a string to an integer is seen when getting input from a user. You can see an example like that in [this article](https://www.freecodecamp.org/news/python-convert-string-to-int-how-to-cast-a-string-in-python/#:~:text=A%20practical%20example%20of%20converting%20a%20string%20to%20an%20int).

## Summary

In this article, we talked about parsing strings in Python. 

We saw examples that showed how to parse a string using the `split()` and `strip()` methods. 

We also saw how to convert a string to an integer using the `int()` function. 

Happy coding! I also write about Python on [my blog](https://ihechikara.com/). 

