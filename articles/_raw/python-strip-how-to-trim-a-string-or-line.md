---
title: Python strip() – How to Trim a String or Line
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-01-12T20:48:03.000Z'
originalURL: https://freecodecamp.org/news/python-strip-how-to-trim-a-string-or-line
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/aleksander-vlad-jiVeo0i1EB4-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "In this article, you'll learn how to trim a string in Python using the\
  \ .strip() method. \nYou'll also see how to use the .lstrip() and .rstrip() methods,\
  \ which are the counterparts to .strip().\nLet's get started!\nHow to trim a string\
  \ in Python\nPython ..."
---

In this article, you'll learn how to trim a string in Python using the `.strip()` method. 

You'll also see how to use the `.lstrip()` and `.rstrip()` methods, which are the counterparts to `.strip()`.

Let's get started!

## How to trim a string in Python

Python has **three** built-in methods for trimming leading and trailing whitespace and characters from strings.

- `.strip()`
- `.lstrip()`
- `.rstrip()`

Each method returns a new trimmed string.

### How to Remove Leading and Trailing Whitespace from Strings in Python

When the `.strip()` method has no argument, it removes any leading and/or trailing whitespace from a string.

So, if you have whitespace at the start and/or end of a word or phrase, `.strip()` alone, by default, will remove it.

The following variable `greeting` has the string "Hello" stored in it. The string has space both to the right and left of it.

```python
greeting = "     Hello!  "

print(greeting,"How are you?")

#output
#     Hello!   How are you?
```

To remove both of them, you use the `.strip()` method, like so:

```python
greeting = "     Hello!  "

stripped_greeting = greeting.strip()

print(stripped_greeting,"How are you?")

#output
#Hello! How are you?
```

You could have also used the `.strip()` method in this way:

```python
greeting = "     Hello!  "

print(greeting.strip(),"How are you?")

#output
#Hello! How are you?
```

### How to Remove Leading and Trailing Characters from Strings in Python

The `.strip()` method takes *optional* characters passed as arguments.

The characters you add as arguments specify what characters you would like to remove from the start and end of the string.

Below is the general syntax for this case:

```python
str.strip(char)
```

The characters you specify are enclosed in quotation marks.

So, for example, say you have the following string:


```python
greeting = "Hello World?"
```

You want to remove "H" and "?", which are at the beginning and at end of the string, respectively.

To remove them, you pass both characters as arguments to `strip()`.

```python
greeting = "Hello World?"

stripped_greeting = greeting.strip("H?")

print(stripped_greeting)

#output
#ello World
```

Notice what happens when you want to remove "W" from "World", which is at the middle and not at the start or end of the string, and you include it as an argument:

```python
greeting = "Hello World?"

stripped_greeting = greeting.strip("HW?")

print(stripped_greeting)
#ello World
```

It will not be removed! Only the characters at the **start** and **end** of said string get deleted.

That being said, look at the next example.

Say you want to remove the first two and the last two characters of the string:

```python
phrase = "Hello world?"

stripped_phrase = phrase.strip("Hed?")

print(stripped_phrase)

#output
#llo worl
```

The first two characters ("He") and the last two ("d?") of the string have been removed.

Another thing to note is that the argument does not remove only the first instance of the character specified.

For example, say you have a string with a few periods at the beginning and a few exclamation marks at the end:

```python
phrase = ".....Python !!!"
```

When you specify as arguments `.` and `!`, all instances of both will get removed:

```python
phrase = ".....Python !!!"

stripped_phrase = phrase.strip(".!")

print(stripped_phrase)

#output
#Python 
```

### How to Remove Only Leading Whitespace and Characters from Strings in Python

To remove *only* leading whitespace and characters, use `.lstrip()`.

This is helpful when you want to remove whitespace and characters only from the start of the string.

An example for this would be removing the `www.` from a domain name.


```python
domain_name = "www.freecodecamp.org www."

stripped_domain = domain_name.lstrip("w.")

print(stripped_domain)

#output
#freecodecamp.org www.
```

In this example I used the `w` and `.` characters both at the start and the end of the string to showcase how `.lstrip()` works.

If I'd used `.strip(w.)` I'd have the following output:

```python
freecodecamp.org 
```

The same goes for removing whitespace.

Let's take an example from a previous section:

```python
greeting = "     Hello!  "

stripped_greeting = greeting.lstrip()

print(stripped_greeting,"How are you?" )

#output
#Hello!   How are you?
```

Only the whitespace from the start of the string has been removed from the output.

### How to Remove only Trailing Whitespace and Characters from Strings in Python

To remove *only* trailing whitespace and characters, use the `.rstrip()` method.

Say you wanted to remove all punctuation only from the end of a string.

You would do the following:

```python
enthusiastic_greeting = "!!! Hello !!!!"

less_enthusiastic_greeting = enthusiastic_greeting.rstrip("!")

print(less_enthusiastic_greeting)

#output
#!!! Hello 
```

Same goes for whitespace.

Taking again the example from earlier, this time the whitespace would be removed only from the end of the output:

```python
greeting = "     Hello!  "

stripped_greeting = greeting.rstrip()

print(stripped_greeting,"How are you?")

#output
#     Hello! How are you?
```

## Conclusion

And there you have it! You now know the basics of how to trim a string in Python.

To sum up:

- Use the `.strip()` method to remove whitespace and characters from the beginning **and** the end of a string.
- Use the `.lstrip()` method to remove whitespace and characters only from the **beginning** of a string.
- Use the `.rstrip()` method to remove whitespace and characters only from the **end** of a string.

If you want to learn more about Python, check out freeCodeCamp's [Python Certification](https://www.freecodecamp.org/learn/scientific-computing-with-python/). You'll start learning in an interacitve and beginner-friendly way. You'll also build five projects at the end to put into practice and help reinforce what you learned.

Thanks for reading and happy coding!






