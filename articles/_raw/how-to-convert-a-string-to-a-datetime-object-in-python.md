---
title: How to Convert a String to a DateTime Object in Python
subtitle: ''
author: Ibrahim Ogunbiyi
co_authors: []
series: null
date: '2022-07-19T20:40:28.000Z'
originalURL: https://freecodecamp.org/news/how-to-convert-a-string-to-a-datetime-object-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/pexels-christina-morillo-1181359--3-.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'When you get dates from raw data, they''re typically in the form of string
  objects. But in this form, you can''t access the date''s properties like the year,
  month, and so on.

  The solution to this problem is to parse (or convert) the string object into ...'
---

When you get dates from raw data, they're typically in the form of string objects. But in this form, you can't access the date's properties like the year, month, and so on.

The solution to this problem is to parse (or convert) the string object into a datetime object so Python can recognized it as a date. And then you can extract any underlying attributes you want to get from it.

This tutorial will teach you how to convert a string to a datetime object in Python. Without further ado, let's get started.

# DateTime Format Codes

Before we learn how to convert strings to dates, you should understand the formatting codes of datetime objects in Python.

These prerequisites will be useful whenever you need to convert a string to a date. We will look at some of the most common formatting codes you'll work with anytime you want to convert string to date.

Here are some of the most common:

* %Y — This is used to represent the Year and it ranges from 0001 to 9999
    
* %m — This is used to represent the month of a year and it ranges from 01 to 12.
    
* %d — This is used to represent the days of the month and ranges from 01 to 31.
    
* %H — This is used to represent the hours of the day in a 24-hour format and ranges from 00 to 23.
    
* %I — This is used to represent the hours of the day in a 12 hour format and ranges from 01 to 12.
    
* %M — This is used to represents minutes in an hour and ranges from 00 to 59.
    
* %S — This is used to represents the seconds in a minute and ranges from 00 to 59 as well.
    

We'll stop here for date format codes, but there are many more in the Python documentation. You can click [here](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes) to see more.

# How to Convert a String to a DateTime Object

Note that the first thing to consider whenever converting a string to date is to make sure that the string is in the right format.

In order to convert a string to a date, it must satisfy the following conditions.

* Firstly, each element in the string must be separated from the others either by a space, letter, or symbol such as / & , % # - and so on.
    
* The element in the string to be parsed as the year, month, or day must be of the same length as the format code. The element in the string must not exceed the range of the format code. For example the %Y code requires 4 numbers to be passed as the year and its range is 0001 – 9999 (so 09, for example, wouldn't work – you need 2009).
    

Let's look at some examples of string-to-date conversions. First, we'll convert the string "2019/08/09" to the date.

We need to import the datetime library in Python to be able to achieve this. We can do that by typing the following:

```python
from datetime import datetime

date_string = "2018/08/09"

format = %Y/%m/%d #specifify the format of the date_string.

date = datetime.strptime(date_string, format)
print(date)
```

Let's go over the above code again to make sure we understand what's going on.

The format variable declares the format of the date string to be passed to the parser (the function that will help us convert the date). We must be aware of the format ahead of time, that is before we pass it to the parser.

In this case, the string is in the format "2019/08/09".

The first element in the string represents a year, for which the format code is `%Y`. Then we have a forward slash followed the month, for which the format code is `%m`. Then we have another forward slash, and finally the day, for which the format code is `%d`.

As a result, we must include the forward slash symbol in the format variable in the same way that it appears in the string. If everything is done correctly, the format should be `"%Y/% m/%d."`

The method `datetime.strptime` is the parser that will help us convert the `date_string` we passed into it as a date. It requires two parameters: the date string and the format.

When we print it after that, it will look like this.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-199.png align="left")

*Image by Author*

We can decide to retrieve any attributes we want from it. For example if we wish to get the year only, we can do that by typing `date.year` and it will print out just the year.

Now that we understand that, let’s go over one more example that is more complex than the above.

### Example – how to convert a string to a date

We will convert this string object to a date: `"2018-11-15T02:18:49Z"`.

Now from the looks of it, we can see that this date string has year, month, day, hours, minutes and seconds. So all we need to do is create the proper format and the symbols in it.

```python
from datetime import datetime

date_string = "2018-11-15T02:18:49Z"

format = "%Y-%m-%dT%H:%M:%SZ

date = datetime.strptime(date_string, format)
print(date)
```

We can see that there is nothing too complex about it. Just follow the format for each part of the date and also pass in any respective symbols or letters you find in the date string.

Do not get distracted by the symbols or letters in the string. If you do everything correctly and print it you should have something like this:

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-200.png align="left")

Make sure you don't confuse the format code `%m` with `%M`. The small `%m` is used for months while the big `%M` is used for minutes.

# Conclusion and Learning More

Now we've gotten to the end of this tutorial. You learned how to convert a string into a date format.

Once you learn the format codes, you'll be good to go. Just make sure you adhere to the principles governing which kind of string can be converted.

For instance you have to remember that the string must be separated with something which can either be a space, letter, or symbol. Also, the string range must not be greater or smaller than the range of the format code.

Thank you for reading.
