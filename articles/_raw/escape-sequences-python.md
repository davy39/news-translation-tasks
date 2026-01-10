---
title: Escape Sequences in Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-03T22:21:00.000Z'
originalURL: https://freecodecamp.org/news/escape-sequences-python
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e3b740569d1a4ca3c0a.jpg
tags:
- name: Python
  slug: python
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'Escape sequences allow you to include special characters in strings. To
  do this, simply add a backslash (\) before the character you want to escape.

  For example, imagine you initialized a string with single quotes:

  s = ''Hey, whats up?''

  print(s)


  Outp...'
---

Escape sequences allow you to include special characters in strings. To do this, simply add a backslash (`\`) before the character you want to escape.

For example, imagine you initialized a string with single quotes:

```py
s = 'Hey, whats up?'
print(s)
```

**Output:**

```sh
Hey, whats up?
```

But if you include an apostrophe without escaping it, then you will get an error:

```py
s = 'Hey, what's up?'
print(s)
```

**Output:**

```sh
  File "main.py", line 1
    s = 'Hey, what's up?'
                   ^
SyntaxError: invalid syntax
```

To fix this, just escape the apostrophe:

```py
s = 'Hey, what\'s up?'
print(s)
```

To add newlines to your string, use `\n`:

```
print("Multiline strings\ncan be created\nusing escape sequences.")
```

**Output:**

```
Multiline strings
can be created
using escape sequences.
```

An important thing to remember is that, if you want to include a backslash character in a string, you will need to escape that. For example, if you want to print a directory path in Windows, you'll need to escape each backslash in the string:

```py
print("C:\\Users\\Pat\\Desktop")
```

**Output:**

```
C:\Users\Pat\Desktop
```

## Raw strings

A _raw_ string can be used by prefixing the string with `r` or `R`, which allows for backslashes to be included without the need to escape them. For example:

```py
print(r"Backslashes \ don't need to be escaped in raw strings.")

```

**Output:**

```
Backslashes \ don't need to be escaped in raw strings.
```

But keep in mind that unescaped backslashes at the end of a raw string will cause and error:

```
print(r"There's an unescaped backslash at the end of this string\")
```

**Output:**

```
  File "main.py", line 1
    print(r"There's an unescaped backslash at the end of this string\")
                                                                      ^
SyntaxError: EOL while scanning string literal
```

# Common escape sequences

| Escape Sequence | Meaning |
| ---- | ---- |
| \\ | Backslash (`\`) |
| \' | Single quote (`'`) |
| \" | Double quote (`"`) |
| \n | ASCII Linefeed (adds newline) |
| \b | ASCII Backspace |

A full list of escape sequences can be found [here](https://docs.python.org/3/reference/lexical_analysis.html#strings) in the Python docs.

