---
title: strftime() Python – Datetime Format Tutorial
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-07-15T16:55:14.000Z'
originalURL: https://freecodecamp.org/news/strftime-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/python-datetime-format-tutorial.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'By Dillion Megida

  In Python, you can format date objects and present them in readable form using the
  strftime function. In this article, I''ll show you how.

  What is strftime() in Python?

  strftime() is a Python date method you can use to convert dates ...'
---

By Dillion Megida

In Python, you can format date objects and present them in readable form using the `strftime` function. In this article, I'll show you how.

## What is `strftime()` in Python?

`strftime()` is a Python date method you can use to convert dates to strings. It doesn't just convert to strings, but also allows you to format your dates in a readable way.

If you're familiar with JavaScript, think of this method as the `format` function of the `date-fns` library which has different characters for formatting dates.

## How to Use `strftime()` in Python

The syntax of the `strftime` method is:

```python
date.strftime(format)
```

The `format` argument can be a combination of different characters for the final output of the string. Let's see some of them:

```python
from datetime import datetime

current_date = datetime.now()
print(current_date)
# 2022-07-14 23:37:38.578835

string_date = current_date.strftime("%Y")
print(string_date)
# 2022
```

`datetime.now` returns the current date. Using the `strftime` method and the "%Y" character, the date is converted to a string showing the year.

Here's another example:

```python
from datetime import datetime

date = datetime.fromisoformat("2022-07-15 00:15:14.643725")

string_date = current_date.strftime("%Y-%b")
print(string_date)
# 2022-Jul
```

Using the `fromisoformat` of the `datetime` object, you can pass a full date string, so that you can get a date object for that string.

`%Y` is for the full year (2022) and `%b` is for the short version of the month (Jul).

`strftime` retained the hyphen "-" but replaced the other characters with the correct date representation.

Here's one more example to format times in dates:

```python
from datetime import datetime

date = datetime.now()

string_time = date.strftime("%X")
print(string_time)
# 00:54:20
```

The `%X` character formats a date string by showing the time representation in `hours:minutes:seconds`.

## Wrap up

In this tutorial, we've seen how to format date strings using different characters passed as an argument to the `strftime` date method. 

We used:

* `%Y` for a full year
* `%b` for an abbreviated month name
* `%X` for time representation

There are many other characters for full month names, abbreviated year names, and times. Check out the [Python strftime cheatsheet](https://strftime.org/) to learn about more characters you can use to represent dates.


