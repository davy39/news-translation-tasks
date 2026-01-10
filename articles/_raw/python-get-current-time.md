---
title: Python Get Current Time
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-07-13T22:48:46.000Z'
originalURL: https://freecodecamp.org/news/python-get-current-time
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/getCurrentTime.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'In your websites and applications, you might want to add functionalities
  like timestamps or checking the time of a user’s activity.

  Every programming language has modules or methods for working with time, and Python
  is not an exception.

  With the date...'
---

In your websites and applications, you might want to add functionalities like timestamps or checking the time of a user’s activity.

Every programming language has modules or methods for working with time, and Python is not an exception.

With the `datetime` and `time` modules of Python, you can get the current date and time, or the date and time in a particular time zone.

In this article, I will show you how to get the current time in Python with the `datetime` and `time` modules. 

## How to Get the Current Time with the Datetime Module

The first thing you can do to quickly get the current date and time is to use the `datetime.now()` function from the datetime module:

```py
from datetime import datetime
current_date_and_time = datetime.now()

print("The current date and time is", current_date_and_time)

# The current date and time is 2022-07-12 10:22:00.776664
```

This shows you not just the time but also the date.

To extract the time, you can use the `strftime()` function and pass in `("%H:%M:%S")`

- %H gets the hour
- %M gets the minute
- %S gets the seconds

 ```py
from datetime import datetime
time_now = datetime.now()
current_time = time_now.strftime("%H:%M:%S")

print("The current date and time is", current_time)

# The current date and time is 10:27:45
```

You can also re-write the code like this:
```py
from datetime import datetime
time_now = datetime.now().strftime("%H:%M:%S")

print("The current date and time is", time_now)

# The current date and time is 10:30:37
```

## How to Get the Current Time with the Time Module

Apart from the `datetime()` module, the `time` module is another built-in way to get the current time in Python.

As usual, you have to import the time module first, and then you can use the `ctime()` method to get the current date and time.

```py
import time

current_time = time.ctime()
print(current_time)

# Tue Jul 12 10:37:46 2022
```

To extract the current time, you also have to use the `strftime()` function:

```py
import time

current_time = time.strftime("%H:%M:%S")
print("The current time is", current_time)

# The current time is 10:42:32
```


## Final Thoughts

This article showed you two ways you can get the current time with Python.

If you’re wondering which to use between the `time` and `datetime` modules, it depends on what you want:

- `time` is more precise than `datetime`
- if you don’t want ambiguity with daylight savings time (DST), use `time`
- `datetime` has more built-in objects you can work with but has limited support for time zones.

If you want to work with time zones, you should consider using the `pytz` module.

To learn how you can get the time in a particular zone, I wrote about [the `pytz` module here](https://www.freecodecamp.org/news/how-to-get-the-current-time-in-python-with-datetime/#howtogetthecurrenttimeofatimezonewithdatetime).

Keep coding :)



