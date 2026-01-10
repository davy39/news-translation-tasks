---
title: Python's datetime Module – How to Handle Dates in Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-01T15:59:54.000Z'
originalURL: https://freecodecamp.org/news/python-datetime-module
coverImage: https://cdn-media-2.freecodecamp.org/w1280/6022ad400a2838549dcc1f89.jpg
tags:
- name: modules
  slug: modules
- name: Python
  slug: python
seo_title: null
seo_desc: "By Suchandra Datta\nIn this quick guide to Python's datetime module, you'll\
  \ learn how to parse dates, extract meaningful information from dates, handle timedelta\
  \ objects and much more. \nSo without further ado let's start counting time with\
  \ Python!\nMos..."
---

By Suchandra Datta

In this quick guide to Python's `datetime` module, you'll learn how to parse dates, extract meaningful information from dates, handle `timedelta` objects and much more. 

So without further ado let's start counting time with Python!

Most programming languages provide libraries for easy handling of dates. Python offers the powerful `datetime` module with its many functions and lucid documentation which makes parsing dates easy. 

This article lists out some of the most important functions from this module, how it can be applied for real-world situations, and some tricky things to watch out for when using it. 

## How to Convert Timestamps to `datetime` Objects Using `strptime()`

Dates can give us a lot of information like the month, year, day, weekday and whether it's a holiday or not. `strptime()` converts a timestamp in the form of a string to a `datetime` object which gives us a lot of extra functionalities. This function expects a string and the format of the timestamp. 

```
from datetime import datetime

d = datetime.strptime("21-02-2021 18:46:00", "%d-%m-%Y %H:%M:%S")
```

The string 21-02-2021 18:46:00 is converted to a suitable `datetime` using the format specified. Some of the most useful directives are:

* `%d` for day of month as a zero-padded decimal like 01, 02, 03 
* `%m` for month as a zero-padded decimal number
* `%Y` for year with century as a decimal number
* `%H` for 24 hour clock with a zero-padded hour value
* `%M` for zero-padded minutes, and 
* `%S` for zero-padded seconds.

This collection of format specifiers is enough to get you started. For more options, you can browse through the docs linked [here](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior). 

### How to Get the Current Timestamp Value

Suppose you want to store data to a database with the current timestamp as a key. To obtain the current timestamp, you just need 1 line of code:

```python
#Obtain the current timestamp

from datetime import datetime
print(datetime.now())
```

### How to Know What Day it Is 

Let's say we need to know the day of the week. We can use the `weekday()` function which returns a numeric code for the day of the week, zero through six, where zero represents Monday, one represents Tuesday, and so on. 

The output could be used with a switch statement to convert the numeric code to the required day name or you could use a list like this:

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-169.png)

### How to Generate a List of Dates from a Given Date

Let's say we know how many pizzas people ordered up until today and we are interested in predicting pizza sales for the next week. 

So, given today's date we need all dates for next week for our required analysis. But we don't want to worry about leap years, century years, and so on. Here's one way to do it.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-137.png)

### How to Work with `timedelta` Objects

As the name suggests, `timedelta` objects represent a time duration between two dates. Let's say that we have two dates and we need to know how much time has passed between them.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-138.png)

`timedelta` objects require several arguments like days, seconds, microseconds, milliseconds, minutes, hours and weeks. Default values for all are zero. Let's find out the difference in hours between 2 dates.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-139.png)

What went wrong? `timedelta` does not store anything internally except for days, seconds, and microseconds, so we need to convert them as shown below:

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-141.png)

### How to Get String Representation of Dates from `datetime` or Date Objects using `strftime`

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-170.png)

If we print the `datetime` object itself, the date is printed in ISO format. Using `strftime`, we pass a format string to control the string representation of the date.

## Conclusion

If you've read this far, congrats – you've learned how to parse dates according to a specified format, obtain the current timestamp value, get the weekday, get a list of dates, use timedelta objects, and get the date as a string back from objects. Whew!

This is a compiled collection based on my own numerous internet searches and endless perusal of the official docs. 

Thank you for taking some time out of your busy schedule to read this. Hope you enjoyed reading it just as much as I loved writing it. Have fun parsing dates in Python!

