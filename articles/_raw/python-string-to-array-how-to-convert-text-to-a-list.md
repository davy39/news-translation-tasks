---
title: Python String to Array – How to Convert Text to a List
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-02-21T18:47:23.000Z'
originalURL: https://freecodecamp.org/news/python-string-to-array-how-to-convert-text-to-a-list
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/steve-johnson-8VO-UxlJ-Lw-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'There will be times where you need to convert one data type to another.

  Fear not, because Python offers a variety of different ways to help you do that.

  In this article, you''ll see a few of the ways in which you can convert a string
  to a list.

  Here i...'
---

There will be times where you need to convert one data type to another.

Fear not, because Python offers a variety of different ways to help you do that.

In this article, you'll see a few of the ways in which you can convert a string to a list.

Here is what we will cover:

1. [An overview of strings and lists](#intro)
    1. [How to check the data type of an object](#type)
2. [Convert a string to a list of individual characters](#characters)
3. [Convert a string to a list of words](#words)
    1. [`split()` method suntax breakdown](#syntax)
    2. [Use `split()` with a separator](#sep)
    3. [Use `split()` with `maxsplit` parameter](#maxsplit)
4. [Convert a string of numbers to a list of numbers](#numbers)

## What are Strings and Lists in Python? <a name="intro"></a>

A **string** is an ordered sequence of characters. It is a series of characters, with one character following the other.

A string is surrounded by either single or double quotation marks:

```python
# all the following are strings

# a string enclosed in single quotes
first_name = 'John'

#a string enclosed in double quotes
last_name = "Doe"
```

If you want to create a string that spans multiple lines, or what is known as a multiline string, use triple quotes to start and end it:

```python
# a multiline string enclosed in triple quotes

phrase = '''I am learning Python
and I really enjoy learning the language!
'''
```

Strings are *immutable*. This means that once they have been created, they cannot change. The individal characters that make up a string cannot be altered.

For example, if you tried to change the first letter of a word from lowercase to uppercase, you would get an error in your code:

```python
#try and change lowercase 'p' to uppercase 'P'
fave_language = "python"
fave_language[0] = "P"

print(fave_language)

#the output will be an error message
#fave_language[0] = "P"
#TypeError: 'str' object does not support item assignment
```

However, you can reassign a different string by updating the variable, like so:

```python
fave_language = "python"
fave_language = "Python"

print(fave_language)

#output
#Python
```

A **list** is an ordered collection of data.

Multiple (typically related) items are stored together under the same variable.

You can create a list by enclosing zero or more items in square brackets, `[]`, each separated by a comma.

A list can contain any of Python's built-in data types.

```python
# a list of numbers
my_numbers_list = [10,20,30,40,50]

print(my_numbers_list)

#output
# [10, 20, 30, 40, 50]
```

Lists are *mutable*.

You can change list items after the list has been created. This means that you can modify existing items, add new items, or delete items at any time during the life of the program.

```python
programming_languages = ["Javascript", "Python", "Java"]

#update the 1st item in the list
programming_languages[0] = "JavaScript"

print(programming_languages)

#output
#['JavaScript', 'Python', 'Java']
```

### How to Determine the Data Type of an Object in Python <a name="type"></a>

To find the data type of an object in Python, use the built-in `type()` function, which has the following syntax:

```python
type(object)

#where object is the object you need to find the data type of
```

The `type()` function will return the type of the object that was passed as an argument to the function.

This is commonly used for debugging purposes.

Let's see how to use `type()` with strings and lists in the example below:

```python
my_name = "John Doe"
my_lucky_numbers = [7,14,33]

print(type(my_name))
print(type(my_lucky_numbers))

#output
#<class 'str'>
#<class 'list'>
```

## How to Convert a String to a List of Individual Characters <a name="characters"></a>         

You can take a word and turn it into a list.

Every single character that makes up that word becomes an individual and separate element inside the list.

For example, let's take the text "Python". 

You can convert it to a list of characters, where each list item would be every character that makes up the string "Python". 

This means that the `P` character would be one list item, the `y` character would be another list item, the `t` character would be another one, and so on.

The most straightforward way is to type cast the string into a list. 

Tyepcasting means to directly convert from one data type to another – in this case from the string data type to the list data type.

You do this by using the built-in `list()` function and passing the given string as the argument to the function.

```python
programming_language = "Python"

programming_language_list = list(programming_language)

print(programming_language_list)

#output
#['P', 'y', 't', 'h', 'o', 'n']
```

Let's take a look at another example:

```python
current_routine = " Learning Python ! "

current_routine_list = list(current_routine)

print(current_routine_list)

#output
#[' ', 'L', 'e', 'a', 'r', 'n', 'i', 'n', 'g', ' ', 'P', 'y', 't', 'h', 'o', 'n', ' ', '!', ' ']
```

The text `" Learning Python ! "` has both leading and trailing whitespace, whitespace between the words "Learning" and "Python", and whitespace between the word "Python" and the exclamation mark.

When the string is converted to a list of characters, every whitespace is treated as an individual character and that's why you see empty spaces, `' '`, as list items.

To remove whitespace only from the beginning and end of the string, use the `strip()` method.

```python
current_routine = " Learning Python ! "

#the leading and trailing whitespace will no longer be separate elements in the list
current_routine_list = list(current_routine.strip())

print(current_routine_list)

#output
#['L', 'e', 'a', 'r', 'n', 'i', 'n', 'g', ' ', 'P', 'y', 't', 'h', 'o', 'n', ' ', '!']
```

To remove *all* and not just the leading and trailing whitespace and make it so no whitespace characters are included in the new list, use the `replace()` method instead:

```python
current_routine = " Learning Python ! "

#replace every instance of whitespace with no space
current_routine_list = list(current_routine.replace(" ", ""))

print(current_routine_list)

#output
#['L', 'e', 'a', 'r', 'n', 'i', 'n', 'g', 'P', 'y', 't', 'h', 'o', 'n', '!']
```

## How to Convert a String to a List of Words <a name="words"></a>

Another way to convert a string to a list is by using the `split()` Python method.

The `split()` method splits a string into a list, where each list item is each word that makes up the string.

Each word will be an individual list item.

### Syntax Breakdown of the `split()` Method in Python <a name="syntax"></a>

The general syntax for the `split()` method is the following:

```python
string.split(separator=None, maxsplit=-1)
```

Let's break it down:

- `string` is the given string you want to turn into a list.
- The `split()` method turns a string into a list. It takes two *optional* parameters.
- `separator` is the first optional parameter, and it determines where the string will split. By default the separator is whitespace and the string will split wherever there is any whitespace.
- `maxsplit` is the second optional parameter. It specifies the maximum number of splits to do. The default value, `-1`, means that it splits across all the entire string and there are no limits to the splitting.

Let's see an example of how that works.

```python
phrase = "I am learning Python !"

print(type(phrase))

#output
#<class 'str'>
```

In the above string, each word that makes up the string is separated by a whitespace.

To turn that string into a list of words, use the `split()` method.

You don't need to specify a separator or a `maxsplit` paramter, as we want to separate all the words wherever there is whitespace between them.

```python
phrase = "I am learning Python !"

phrase_to_list = phrase.split()

print(phrase_to_list)
print(type(phrase_to_list))


#output
#['I', 'am', 'learning', 'Python', '!']
#<class 'list'>
```

The string was split based on where there was any whitespace, and each word that made up the string turned into an individual list item.

### How to Use the `split()` method with a Separator <a name="sep"></a>

You can also convert a string to a list using a separator with the `split()` method. The separator can be any character you specify.

The string will separate based on the separator you provide.

For example, you can use a comma, `,`, as the separator. 

The string will turn into a list whenever there is a comma, starting from the left.

Items that are comma separated will be the individual list items.

Let's take the following string:

```python
phrase = "Hello world,I am learning Python!"
```

There is a comma that separates `Hello world` from `I am learning Python!`.

If we want to use that comma as a separator to create two individual list items, we would do the following:

```python
phrase = "Hello world,I am learning Python!"

phrase_to_list = phrase.split(",")

print(phrase_to_list)

#output
#['Hello world', 'I am learning Python!']
```

Two separate items were created as list items and the separation occured where there was a comma.

Another example could be to separate a domain name, whenever there is a dot, `.`.

```python
domain_name = "www.freecodecamp.org"

domain_name_list = domain_name.split(".")

print(domain_name_list)

#output
#['www', 'freecodecamp', 'org']
```

Every time there is a dot, a new list item will be added to the list.

### How to Use the `split()` method with the `maxsplit` Paramter <a name="maxsplit"></a>

As mentioned earlier, `maxsplit` is an optional parameter of the `split()` method.

It defines how many elements of the list will get split and turned into individual list items. By default, it is set to `-1`, which means all elements that make up the string will be split.

But we can change the value to a specific number.

To split only two words and not every word, we set `maxsplit` to two:

```python
current_routine = "I enjoy learning Python everyday"

current_routine_list = current_routine.split(maxsplit=2)

print(current_routine_list)

#output
#['I', 'enjoy', 'learning Python everyday']
```

`maxsplit` is set to `2`, which means a maximum of only two words will be split by space and will make two individual list items. The third list item will be the rest of the words that make up the initial string.

Using another example from the section above, you can combine a separator with `maxsplit` to make a targeted conversion of a string to a list:

```python
domain_name = "www.freecodecamp.org"

domain_name_list = domain_name.split(".", maxsplit=1)

print(domain_name_list)

#output
#['www', 'freecodecamp.org']
```

In this example, the separator was a dot and only the first element got split.

## How to Convert a String of Integers to a List of Integers <a name="numbers"></a>

Numbers are considered strings when they are enclosed in either single or double quotes.

Say you have your date of birth stored as a string, like such:

```python
birthdate = "19/10/1993"

print(type(birthdate))

#output
#<class 'str'>
```

To remove the slashes and store the numbers associated with the date, month, and year of birth as separate list items, you would do the following:

```python
birthdate = "19/10/1993"

birthdate_list = birthdate.split("/")

print(birthdate_list)
print(type(birthdate_list))

#output
#['19', '10', '1993']
#<class 'list'>
```

In the example, the separator was the slash, `/`, and whenever there was a slash a new list item was created.

If you take a closer look at the output you'll see that the list items are still strings, since they are surrounded by single quotes and there has been no type conversion.

To convert each list item from a string to an integer, use the `map` function.

The `map` function takes two arguments:

- A function. In this case the function will be the `int` function.
- An iterable, which is a sequence or collection of items. In this case the iterable is the list we created.

```python
birthdate = "19/10/1993"

birthdate_list = birthdate.split("/")

str_to_int = (map(int, birthdate_list))

print(str_to_int)

#output
#<map object at 0x10e289960>
```

That is not exactly the output we wanted. When we check the data type, we see that we no longer have a list:

```python
print(type(str_to_int))

#output
#<class 'map'>
```

To correct this, we instead need to go back and add the `list()` function before the conversion:

```python
birthdate = "19/10/1993"

birthdate_list = birthdate.split("/")

str_to_int = list(map(int, birthdate_list))

print(type(str_to_int))
print(str_to_int)

#output
#<class 'list'>
#[19, 10, 1993]
```

## Conclusion

And there you have it! You now know some of the ways to convert a string to a list in Python.

To learn more about the Python programming language, check out freeCodeCamp's [Scientific Computing with Python Certification](https://www.freecodecamp.org/learn/scientific-computing-with-python/).

You'll start from the basics and learn in an interacitve and beginner-friendly way. You'll also build five projects at the end to put into practice and help reinforce what you've learned.

Thanks for reading and happy coding!


