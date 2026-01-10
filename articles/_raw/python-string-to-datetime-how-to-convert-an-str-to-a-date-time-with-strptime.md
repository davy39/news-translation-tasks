---
title: Python String to Datetime – How to Convert an Str to a Date Time with Strptime
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2023-02-02T15:57:55.000Z'
originalURL: https://freecodecamp.org/news/python-string-to-datetime-how-to-convert-an-str-to-a-date-time-with-strptime
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/pexels-marko-klaric-6408282.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'Python offers a variety of built-in modules that you can include in your
  program.

  A module is a Python file containing the necessary code to execute an individual
  functionality. This file is imported into your application to help you perform a
  specif...'
---

Python offers a variety of built-in modules that you can include in your program.

A module is a Python file containing the necessary code to execute an individual functionality. This file is imported into your application to help you perform a specific task.

One of those modules is the `datetime` module for working with and manipulating times and dates.

The `datetime` module includes the `datetime` class, which in turn provides the `strptime()` class method. The `strptime()` method creates a datetime object from a string representation of a corresponding date and time.

In this article, you will learn how to use the `datetime.strptime()` method to convert strings to datetime objects.

Let's get into it!

## What Is the `datetime.strptime()` Method in Python? A `datetime.strptime()` Syntax Breakdown

The general syntax for the `datetime.strptime()` method looks something similar to the following:

```
datetime.strptime(date_string, format_code)
```

Let's break it down.

Firstly, `datetime` is the class name.

Then, `strptime()` is the method name. The method accepts two *required* string arguments.

* The first required argument is `date_string` – the string representation of the date you want to convert to a datetime object.
* The second required argument is `format_code` – a specific format to help you convert the string to a datetime object.

Here is a brief list of some of the most commonly used code formats you may come across:

- `%d` - the day of the month as a zero-padded decimal number such as `28`.
- `%a` - a day's abbreviated name, such as `Sun`.
- `%A` - a day's full name, such as `Sunday`. 
- `%m` - the month as a zero-padded decimal number, such as `01`.
- `%b` - month's abbreviated name, such as `Jan`.
- `%B` - the month's full name, such as `January`.
- `%y` - the  year  without century, such as `23`.
- `%Y`- the year with century, such as `2023`.
- `%H` - the hours of the day in a 24-hour format, such as `08`.
- `%I` - the hours of the day in a 12-hour format.
- `%M` -  the minutes in an hour, such as `20`.
- `%S` - the seconds in a minute, such as `00`.

To view a table that shows all of the format codes for `datetime.strptime()`, refer to the [Python documentation](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes).

## How to Use the `datetime.strptime()` Method in Python? How to Convert a String to a Datetime Object in Python

Let's say I have the following string that represents a date and time:

```
28/01/23  08:20:00
```

And I want to get the following output:

```
2023-01-28 08:20:00
```

How would I achieve that?

Let's take a look at the code below:

```python
# import the datetime class from the datetime module
from datetime import datetime

date_time_str = "28/01/23  08:20:00"

# check data type of date_time_str
print(type(date_time_str))

# output

# <class 'str'>
```

First, I import the `datetime` module with the `from datetime import datetime` statement.

Then, I store the string I want to convert to a datetime object in a variable named `date_time_str` and check its type using the `type()` function. The output indicates that it is a string.

Now, let's convert the string to a datetime object using the `strptime()` method of the `datetime` class and check the data type:

```python
from datetime import datetime

date_time_str = "28/01/23  08:20:00"

date_time_object = datetime.strptime(date_time_str, "%d/%m/%y %H:%M:%S")

print(date_time_object)

# check date_time_object_type
print(type(date_time_object))

# output

# 2023-01-28 08:20:00
# <class 'datetime.datetime'>
```

The format codes for the string `28/01/23  08:20:00` are `%d/%m/%y %H:%M:%S`.

The format codes `%d,%m,%y,%H,%M,%S` represent the day of the month, the month as a zero-padded decimal number, the year without century, the hour of the day, the minutes of the day and the seconds of the day, respectively.

Now, let's change the initial string a bit.

Let's change it from `28/01/23` to `28 January 2023` and check the data type of `date_time_str`:

```python
from datetime import datetime

date_time_str = "28 January 2023 08:20:00"

#check data type
print(type(date_time_str))

# output

# <class 'str'>
```

Now, let's convert `date_time_str` to a datetime object – keep in mind that because the string is different, you must also change the format codes:

```python
from datetime import datetime

date_time_str = "28 January 2023 08:20:00"

date_object = datetime.strptime(date_time_str, "%d %B %Y %H:%M:%S")

print(date_object)

#check data type
print(type(date_object))

# output

# 2023-01-28 08:20:00
# <class 'datetime.datetime'>
```

The format codes for the string `28 January 2023 08:20:00` are `%d %B %Y %H:%M:%S`.

Because I changed the month of January from its zero-padded decimal number representation, `01`, to its full name, `January`, I also needed to change its format code – from `%m` to `%B`.

## How to Convert a String to a `datetime.date()` Object in Python

What if you only want to convert the date but not the time from a string?

You may only want to convert only the `28/01/23` part of the `28/01/23  08:20:00` string to an object.

To convert a string to a date object, you will use the `strptime()` method like you saw in the previous section, but you will also use the `datetime.date()` method to extract only the date.

```python
from datetime import datetime

date_time_str = "28 January 2023 08:20:00"

date_object = datetime.strptime(date_time_str, "%d %B %Y %H:%M:%S").date()

print(date_object)

#check data type
print(type(date_object))

# output

# 2023-01-28
# <class 'datetime.date'>
```

## How to Convert a String to a `datetime.time()` Object in Python

And to convert only the time part,`08:20:00` from the `28/01/23  08:20:00` string, you would use the `datetime.time()` method to extract only the time:

```python
from datetime import datetime

date_time_str = "28 January 2023 08:20:00"

date_object = datetime.strptime(date_time_str, "%d %B %Y %H:%M:%S").time()

print(date_object)
print(type(date_object))

# output

# 08:20:00
# <class 'datetime.time'>
```

## Why Does a `ValueError` Get Raised When Using `datetime.strptime()` in Python?

Something to keep in mind is that the string you pass as an argument to the `strptime()` method needs to have a specific format – not any string gets converted into a datetime object.

Specifically, the year, month, and day in the string must match the format code.

For example, the format code for the month in the string `28/01/23` must be `%m`, which represents the month as a zero-padded decimal number.

What happens when I use the format code `%B` instead?

```python
from datetime import datetime

date_time_str = "28/01/23  08:20:00"

date_time_object = datetime.strptime(date_time_str, "%d/%B/%y %H:%M:%S")

print(date_time_object)

# output

# raise ValueError("time data %r does not match format %r" %
# ValueError: time data '28/01/23  08:20:00' does not match format '%d/%B/%y # %H:%M:%S'
```

I get a `ValueError`!

The `%B` format code represents the month's full name, such as `January`, and not `01`.

So, if the string passed to `strptime()` does not match the format specified, a `ValueError` gets raised.

To help with this, you can test and handle the error by using a `try-except` block, like so:

```python
from datetime import datetime

date_time_str = "28/01/23  08:20:00"

try:
  date_time_object = datetime.strptime(date_time_str, "%d/%B/%y %H:%M:%S")
except ValueError as error:
  print('A ValueError is raised because :', error)
  
# output

# A ValueError is raised because : time data '28/01/23  08:20:00' does not # match format '%d/%B/%y %H:%M:%S'
```

## Conclusion

Hopefully, this article helped you understand how to convert a string to a datetime object in Python using the `strptime()` method.

Thank you for reading, and happy coding!


