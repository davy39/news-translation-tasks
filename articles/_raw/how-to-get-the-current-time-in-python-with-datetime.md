---
title: How to Get the Current Time in Python with Datetime
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-03-21T13:52:01.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-the-current-time-in-python-with-datetime
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/datetime.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'In your Python applications, you might want to work with time to add functionalities
  like timestamps, check the time of a user’s activity, and more.

  One of the modules that helps you work with date and time in Python is datetime.

  With the datetime mo...'
---

In your Python applications, you might want to work with time to add functionalities like timestamps, check the time of a user’s activity, and more.

One of the modules that helps you work with date and time in Python is `datetime`.

With the `datetime` module, you can get the current date and time, or the current date and time in a particular time zone.

In this article, I will show you how to get the current time in Python with the `datetime` module. I will also show you how to get the current time in any timezone of the world.

## Table of Contents
- [How to Get the Current Time with the `datetime` Module](#heading-how-to-get-the-current-time-with-the-datetime-module)
- [Attributes of the `datetime.now()` Function](#heading-attributes-of-the-datetimenow-function)
- [How to Get the Current Time of a Timezone with `datetime`](#heading-how-to-get-the-current-time-of-a-timezone-with-datetime)
- [Conclusion](#heading-conclusion)

## How to Get the Current Time with the `datetime` Module

The first thing you have to do is to import the `datetime` module like this:

```py
from datetime import datetime
```

The next thing you can do to quickly get the current date and time is to use the `datetime.now()` function from the `datetime` module:

```py
from datetime import datetime
currentDateAndTime = datetime.now()

print("The current date and time is", currentDateAndTime)
# Output: The current date and time is 2022-03-19 10:05:39.482383
```

To get the current time in particular, you can use the `strftime()` method and pass into it the string `”%H:%M:%S”` representing hours, minutes, and seconds. 

This would give you the current time in a 24Hour format:
```py
from datetime import datetime
currentDateAndTime = datetime.now()

print("The current date and time is", currentDateAndTime)
# Output: The current date and time is 2022-03-19 10:05:39.482383

currentTime = currentDateAndTime.strftime("%H:%M:%S")
print("The current time is", currentTime)
# The current time is 10:06:55
```

## Attributes of the `datetime.now()` Function

The `datetime.now` function has several attributes with which you can get the year, month, week, day, hour, minute, and second of the current date.

The snippet of code below prints all the values of the attributes to the terminal:
```py
from datetime import datetime
currentDateAndTime = datetime.now()

print("The current year is ", currentDateAndTime.year) # Output: The current year is  2022
print("The current month is ", currentDateAndTime.month) # Output: The current month is  3 
print("The current day is ", currentDateAndTime.day) # Output: The current day is  19
print("The current hour is ", currentDateAndTime.hour) # Output: The current hour is  10 
print("The current minute is ", currentDateAndTime.minute) # Output: The current minute is  49
print("The current second is ", currentDateAndTime.second) # Output: The current second is  18

``` 
## How to Get the Current Time of a Timezone with `datetime`

You can get the current time in a particular timezone by using the `datetime` module with another module called `pytz`.

You can install the `pytz` module from pip like this:
`pip install pytz`

The first thing you have to do is import both the `datetime` and `pytz` modules:
```py
from datetime import datetime
import pytz
```

You can then check for all available timezones with the snippet below:
```py
from datetime import datetime
import pytz

zones = pytz.all_timezones

print(zones) 
# Output: all timezones of the world. Massive!
```

In the snippet of code below, I was able to get the time in New York:
```py
from datetime import datetime
import pytz

newYorkTz = pytz.timezone("America/New_York") 
timeInNewYork = datetime.now(newYorkTz)
currentTimeInNewYork = timeInNewYork.strftime("%H:%M:%S")

print("The current time in New York is:", currentTimeInNewYork)
# Output: The current time in New York is: 05:36:59
```
How was I able to get the current time in New York?
- I brought in the `pytz` module’s `pytztimezone()` method, passed into it the exact timezone of New York as a string, and assigned it to a variable named `newYorkTz` (for New York timezone) 
- To get the current time in New York, I used the `datetime.now()` function from the `datetime` module and passed into it the variable I created to store the timezone in New York
- To finally get the current time in New York in a 24 Hour format, I used the `strftime()` method on the `timeInNewYork` variable and stored it in a variable named `currentTimeInNewYork`, so I can print it to the terminal

## Conclusion

As shown in this article, the `datetime` module is very handy in working with time and dates, and subsequently getting the current time in your locale. 

When combined with the `pytz` module that you can install from pip, you can also use it to get the current time in any timezone of the world.

Thank you for reading. If you find this article helpful, you can share it with your friends and family.




