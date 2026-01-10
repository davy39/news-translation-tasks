---
title: Append a String in Python – STR Appending
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-10-18T19:33:59.000Z'
originalURL: https://freecodecamp.org/news/append-a-string-in-python-str-appending
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/alex-chumak-zGuBURGGmdY-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "In this article, you'll learn the different methods of appending strings\
  \ in Python. \nAnother term commonly used when talking about appending strings is\
  \ concatenation. So you'll often see these terms — append and concatenate — used\
  \ interchangeably. \nE..."
---

In this article, you'll learn the different methods of appending strings in Python. 

Another term commonly used when talking about appending strings is concatenation. So you'll often see these terms — append and concatenate — used interchangeably. 

Either way, to append or concatenate strings means to add or join the value of one string to another string.  

Let's take a look at the different ways you can do this with simple code examples. 

## How to Append a String in Python Using the `+` Operator

You can use the `+` operator to append two or more strings. Here's an example:

```python
first_name = "John"
last_name = "Doe"

print(first_name + last_name)
# JohnDoe
```

In the example above, we created two string variables – `first_name` and `last_name`. They had values of "John" and "Doe", respectively. 

To append these variables, we used the `+` operator: `first_name + last_name`. 

You'll notice in the output that we got the two variables joined together without any spacing: `JohnDoe`. 

You can add a space after the `first_name` value: "John ". Or before the `last_name` value: " Doe". That is: 

```python
first_name = "John "
last_name = "Doe"

print(first_name + last_name)
# John Doe
```

You can also add spacing using quotation marks while appending the strings. Here's how: 

```python
first_name = "John "
last_name = "Doe"

print(first_name + "" + last_name)
# John Doe
```

## How to Append a String in Python Using the `join()` Method

Another way you can append strings in Python is by using the `join()` method.

The `join()` method takes an iterable object — Lists, Tuples, Strings, Sets, Dictionaries —  as its parameter. Here's what the syntax looks like:

```python
string.join(iterable_object)
```

Here's an example showing how use can append strings using the `join()` method: 

```python
first_name = "John"
last_name = "Doe"

print("".join([first_name, last_name]))
# JohnDoe
```

Here, we passed in our two string variables as parameters to the `join()` method. 

You'll also notice that the variables were nested in square brackets `[]`, making it a list of strings: `[first_name, last_name]`. This is because the method only takes one parameter which must be an iterable object. 

One strange thing about the `join()` method is the quotation marks that come before the period/dot. 

You can use these quotation marks to state what appears between the items in your iterable object values. Let me demonstrate with an example. 

```python
first_name = "John"
last_name = "Doe"

print("#".join([first_name, last_name]))
# John#Doe
```

In the example above, I added the `#` symbol to the quotation marks: `"#".join([first_name, last_name])`. This `#` was added between our strings: `John#Doe`. 

In the last section, we had to use different methods to add spacing between our strings. You can achieve that easily by adding a space in the quotation marks that precedes the `join()` method: 

```python
first_name = "John"
last_name = "Doe"

print(" ".join([first_name, last_name]))
# John Doe
```

## How to Append a String in Python Using the String `format()` Method

Here's what the syntax for the string `format()` method looks like: 

```txt
{}.format(value)
```

Basically, the string format method takes the `value` parameter in the syntax above and inserts it into the curly bracket. The resulting value will be a string.

Here's an example:

```python
first_name = "John"
last_name = "Doe"

print("{} {}".format(first_name, last_name))
# John Doe
```

Since we provided two curly brackets in the example and two parameters (`first_name` and `last_name`), the string `format()` method inserts the strings into their respective curly brackets. 

You can add more strings in the quotation marks where you find the curly brackets. This will not alter the string `format()` method's operation — the strings will still be inserted into the curly brackets. That is: 

```python
first_name = "John"
last_name = "Doe"

print("My name is {} {}".format(first_name, last_name))
# My name is John Doe
```

## How to Append a String in Python Using the f-string

This method is pretty easy to understand. The f-string was introduced in Python to make string formatting and interpolation easier. But you can also use it to append strings. 

To use the f-string, you simply write an f followed by quotation marks: `f""`. You can then insert strings and variable names between the quotation marks. All variable names must be nested in curly brackets. 

Here's an example:

```python
first_name = "John"
last_name = "Doe"

print(f"{first_name} {last_name}")
# John Doe
```

## Summary

In this article, we discussed the different methods you can use to append strings in Python. 

To append a string to another means to join them together. 

As discussed in this article, along with code examples, you can append strings in Python using the `+` operator, the `join()` method, the `string()` format method, and the f-string. 

Happy coding!

