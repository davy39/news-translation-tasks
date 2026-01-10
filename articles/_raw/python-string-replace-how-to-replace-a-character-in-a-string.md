---
title: Python string.replace() – How to Replace a Character in a String
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-09-01T21:59:34.000Z'
originalURL: https://freecodecamp.org/news/python-string-replace-how-to-replace-a-character-in-a-string
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/string-replace.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "By Dillion Megida\nPython has numerous string modifying methods, and one\
  \ of them is the replace method. \nIn this article, I'll show you how this method\
  \ can be used to replace a character in a string.\nHow the replace Method Works\
  \ in Python\nThe replace ..."
---

By Dillion Megida

Python has numerous string modifying methods, and one of them is the `replace` method. 

In this article, I'll show you how this method can be used to replace a character in a string.

## How the `replace` Method Works in Python

The `replace` string method returns a new string with some characters from the original string replaced with new ones. The original string is not affected or modified.

The syntax of the `replace` method is:

```python
string.replace(old_char, new_char, count)
```

The `old_char` argument is the set of characters to be replaced.

The `new_char` argument is the set of characters that replaces the `old_char`.

The `count` argument, which is optional, specifies how many occurrences will be replaced. If this is not specified, all occurrences of the `old_char` will be replaced with the `new_char`.

Let's see some examples.

## `string.replace()` Examples

Here's an example that replaces "JavaScript" with "PHP" in a string:

```python
str = "I love JavaScript. I prefer JavaScript to Python because JavaScript looks more beautiful"

new_str = str.replace("JavaScript", "PHP")

print(new_str)
# I love PHP. I prefer PHP to Python because PHP looks more beautiful
```

You can see how the `replace` method replaces the "JavaScript" occurences with "PHP".

In this example, the three occurrences of "JavaScript" are replaced with "PHP". What if you wanted only one occurrence to be replaced? Then you can use the `count` argument like this:

```python
str = "I love JavaScript. I prefer JavaScript to Python because JavaScript looks more beautiful"

new_str = str.replace("JavaScript", "PHP", 1)

print(new_str)
# I love PHP. I prefer JavaScript to Python because JavaScript looks more beautiful
```

By applying a `count` argument of **1**, you can see that only the first "JavaScript" (the first occurrence) is replaced with "PHP". The remaining "JavaScript"s stays untouched.

## When to Use the `replace` Method in Python

A good use case of this method is to replace characters in a user's input to fit some standard.

Let's say, for example, you want users to enter their usernames but you don't want the whitespace character in the username input. You can use the `replace` method to replace the whitespaces in the submitted strings with a hyphen. Here's how to do that:

```python
user_input = "python my favorite"

updated_username = user_input.replace(" ", "-")

print(updated_username)
# python-my-favorite
``` 

From the result of the `replace` method, you can see that the whitespaces have been replaced with hyphens which meets your standard.

## Wrapping Up

The `replace` method replaces an existing substring in a string with a new substring. You specify how many occurrences of the existing substring are to be replaced with the `count` argument of the method.



