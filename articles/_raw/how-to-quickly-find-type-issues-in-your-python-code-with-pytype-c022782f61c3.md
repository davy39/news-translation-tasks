---
title: How to quickly find type-issues in your Python code with Pytype
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-13T15:50:52.000Z'
originalURL: https://freecodecamp.org/news/how-to-quickly-find-type-issues-in-your-python-code-with-pytype-c022782f61c3
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/python-1.jpeg
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Ehud Tamir

  TL;DR — If you’re working on a large Python project or just like to keep your code-base
  tidy and neat, Pytype is the tool for you.

  Python is a great programming language for prototyping and scripting. The concise
  syntax, flexible type s...'
---

By Ehud Tamir

**TL;DR —** If you’re working on a large Python project or just like to keep your code-base tidy and neat, [Pytype](https://github.com/google/pytype) is the tool for you.

Python is a great programming language for prototyping and scripting. The concise syntax, flexible type system, and interpreted nature allows us to quickly try an idea, tweak it, and try again.

When Python projects **grow**, the flexibility that was once an enabler for speed becomes a burden on development velocity. As additional developers join the project, and more code is written, the lack of type information makes it harder to read and understand the code. Without a type-checking system, mistakes are easy to make and hard to catch.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/python.jpeg)
_CC BY 2.5, [https://commons.wikimedia.org/w/index.php?curid=648709](https://commons.wikimedia.org/w/index.php?curid=648709)_

[**Pytype**](https://github.com/google/pytype) to the rescue! Pytype is an open-source tool for type checking and type inference in Python. And it works out-of-the-box — just install and run!

Pytype will…

1. Statically infer type information and check your code for type errors.
2. Validate PEP 484 type annotations in your code for consistency.
3. Merge back inferred type information into your code, **if you want**.

If you’re sold, go ahead and visit [Pytype](https://github.com/google/pytype) for installation and usage instructions. Below I present some cool usage examples!

### Example #1: Type inference and checking

This is the most common scenario. You wrote some code and want to sanity-check that you didn’t make any mistakes. Consider this function:

```py
import re

def GetUsername(email_address):
  match = re.match(r'([^@]+)@example\.com', email_address)
  return match.group(1)
```

Pretty straightforward. It extracts the part of an email address before the @ using a regular expression, and returns it. Did you notice the bug?

Let’s see what happens when we use `pytype` to check it:

```py
% pytype get_username.py
Analyzing 1 sources with 0 dependencies
File "/.../get_username.py", 
line 5, in GetUsername: No attribute 'group' on None [attribute-error]
  In Optional[Match[str]]
```

Pytype tells us that `group` is not a valid function call on `match`. Oh! `re.match()` returns `None` when no match is found. Indeed, in these cases `match.group(1)` will throw an exception.

Let’s fix the bug, by having the function return None for an invalid email address:

```py
import re
def GetUsername(email_address):
  match = re.match(r'([^@]+)@example\.com', email_address)
  
if match is None:
    return None
  return match.group(1)  # <-- Here, match can't be None
```

Now, when we re-run `pytype`, the error is gone. Pytype infers that if the code after the **if** gets executed, match is guaranteed not to be `None`.

### Example #2: Validation of type annotations

In Python 3, you can type-annotate ([PEP 484](https://www.python.org/dev/peps/pep-0484)) your code to help type-checking tools **and other developers** understand your intention. Pytype is able to alert when your type annotations have mistakes:

```py
import re
from typing import Match

def GetEmailMatch(email) -> Match:
  return re.match(r'([^@]+)@example\.com', email)
```

Let’s use `pytype` to check this code snippet:

```py
% pytype example.py
Analyzing 1 sources with 0 dependencies
File "/.../example.py", line 5, in GetEmailMatch: 
bad option in return type [bad-return-type]
  Expected: Match
  Actually returned: None
```

Pytype is telling us that `GetEmailMatch` might return `None`, but we annotated its return type as `Match`. To fix this, we can use the `Optional` type annotation from the typing module:

```py
import re
from typing import Match, Optional

def GetEmailMatch(email) -> Optional[Match]:
  return re.match(r'([^@]+)@example\.com', email)
```

`Optional` means that the return value can be a `Match` object or `None`.

### Example #3: Merging back inferred type information

To help you adopt type annotations, Pytype can add them into the code for you. Let’s look at this code snippet:

```py
import re
  
def GetEmailMatch(email):
  return re.match(r'([^@]+)@example\.com', email)

def GetUsername(email_address):
  match = GetEmailMatch(email_address)
  if match is None:
    return None
  return match.group(1)
```

To add type annotations to this code, we first run `pytype` on the file. `pytype` saves the inferred type information into a `.pyi` file. Then, we can run `merge-pyi` to merge the type annotations back into the code:

```
% pytype email.py
% merge-pyi -i email.py pytype_output/email.pyi
```

And voilà!

```py
import re
from typing import Match
from typing import Optional

def GetEmailMatch(email) -> Optional[Match[str]]:
  return re.match(r'([^@]+)@example\.com', email)

def GetUsername(email_address) -> Optional[str]:
  match = GetEmailMatch(email_address)
  if match is None:
    return None
  return match.group(1)
```

The type annotations, including `import` statements, are now in the source file.

For more usage examples and installation instructions, please visit [Pytype on GitHub](https://github.com/google/pytype).

Thanks for reading!

