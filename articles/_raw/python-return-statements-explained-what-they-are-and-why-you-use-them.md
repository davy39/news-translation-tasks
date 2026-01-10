---
title: 'Python Return Statements Explained: What They Are and Why You Use Them'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-04T21:22:00.000Z'
originalURL: https://freecodecamp.org/news/python-return-statements-explained-what-they-are-and-why-you-use-them
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e34740569d1a4ca3be2.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'All functions return a value when called.

  If a return statement is followed by an expression list, that expression list is
  evaluated and the value is returned:

  >>> def greater_than_1(n):

  ...     return n > 1

  ...

  >>> print(greater_than_1(1))

  False

  >>>...'
---

All functions return a value when called.

If a return statement is followed by an expression list, that expression list is evaluated and the value is returned:

```text
>>> def greater_than_1(n):
...     return n > 1
...
>>> print(greater_than_1(1))
False
>>> print(greater_than_1(2))
True
```

If no expression list is specified, `None` is returned:

```text
>>> def no_expression_list():
...     return    # No return expression list.
...
>>> print(no_expression_list())
None
```

If a return statement is reached during the execution of a function, the current function call is left at that point:

```text
>>> def return_middle():
...     a = 1
...     return a
...     a = 2     # This assignment is never reached.
...
>>> print(return_middle())
1
```

If there is no return statement the function returns None when it reaches the end:

```text
>>> def no_return():
...     pass     # No return statement.
...
>>> print(no_return())
None
 
```

A single function can have multiple `return` statements. Execution of the function ends when one of these `return` statements is reached:

```text
 >>> def multiple_returns(n):
 ...    if(n):
 ...        return "First Return Statement"
 ...    else:
 ...        return "Second Return Statement"
 ...
 >>> print(multiple_returns(True))
 First Return Statement
 >>> print(multiple_returns(False))
 Second Return Statement
 
```

A single function can return various types:

```text
 >>> def various_return_types(n):
 ...     if(n==1):
 ...         return "Hello World."   # Return a string
 ...     elif(n==2):
 ...         return 42               # Return a value
 ...     else:
 ...         return True             # Return a boolean
 ... 
 >>> print(various_return_types(1))
 Hello World.
 >>> print(various_return_types(2))
 42
 >>> print(various_return_types(3))
 True
```

It is even possible to have a single function return multiple values with only a single return:

```text
 >>> def return_two_values():
 ...     a = 40
 ...     b = 2
 ...     return a,b
 ...
 >>> print("First value = %d,  Second value = %d" %(return_two_values()))
 First value = 40,  Second value = 2
```

See the [Python Docs](https://docs.python.org/3/reference/simple_stmts.html#the-return-statement) for more info.

