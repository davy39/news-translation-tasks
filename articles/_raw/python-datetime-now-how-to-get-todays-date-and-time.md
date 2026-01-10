---
title: Python Datetime.now() – How to Get Today's Date and Time
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-09-20T20:12:09.000Z'
originalURL: https://freecodecamp.org/news/python-datetime-now-how-to-get-todays-date-and-time
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/kevin-ku-aiyBwbrWWlo-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "You can use the datetime module in Python to retrieve data about date and\
  \ time. \nIn this article, you'll learn how to use the datetime object from the\
  \ datetime module to get the current date and time properties.\nYou'll also learn\
  \ how to get the date ..."
---

You can use the `datetime` module in Python to retrieve data about date and time. 

In this article, you'll learn how to use the `datetime` object from the `datetime` module to get the current date and time properties.

You'll also learn how to get the date and time of different locations around the world using the `datetime.now()` function and the `pytz` module. 

## How to Use the `datetime` Object in Python

In order to make use of the `datetime` object, you have to first import it. Here's how:

```python
from datetime import datetime
```

In the next example, you'll see how to use the `datetime` object. 

```python
from datetime import datetime

current_dateTime = datetime.now()

print(current_dateTime)
# 2022-09-20 10:27:21.240752
```

In the code above, we assigned the `datetime` to a variable called `current_dateTime`. 

When printed to the console, we got the current year, month, day, and time: `2022-09-19 17:44:17.858167`.

Note that we're able to access the information above using the `now()` method: `datetime.now()`.

## How to Use the `datetime.now()` Attributes

In the last section, we retrieved information about the current date and time which included the current year, month, day, and time at that moment. 

But the `datetime.now()` function provides us with extra attributes for extracting individual data. 

For example, to get just the current year, you'd do something like this:

```python
from datetime import datetime

current_dateTime = datetime.now()

print(current_dateTime.year)
# 2022
```

In the example above, we assigned the `datetime.now()` function to a variable called `current_dateTime`. 

Using dot notation, we attached the `year` attribute to the variable declared above: `current_dateTime.year`. When printed to the console, we got 2022. 

The `datetime.now()` function has the following attributes:

* `year`
* `month`
* `day`
* `hour`
* `minute`
* `second`
* `microsecond`

Here's an example of the attributes listed above in use:

```python
from datetime import datetime

current_dateTime = datetime.now()

print(current_dateTime.year) # 2022

print(current_dateTime.month) # 9

print(current_dateTime.day) # 20

print(current_dateTime.hour) # 11

print(current_dateTime.minute) # 27

print(current_dateTime.second) # 46

print(current_dateTime.microsecond) # 582035
```

## How to Get a Particular Timezone in Python Using `datetime.now()` and `pytz`

To get information about different time-zones across the world in Python, you can make use of the `datetime.now()` function and the `pytz` module. 

Here's an example that shows how to get the current date and time in Lagos, Nigeria: 

```python
from datetime import datetime
import pytz

datetime_in_Lagos = datetime.now(pytz.timezone('Africa/Lagos'))

print(datetime_in_Lagos)
# 2022-09-20 12:53:27.225570+01:00
```

In the code above, we first imported the modules:

```python
from datetime import datetime
import pytz

```

Then we passed in the `pytz` object as a parameter to the `datetime.now()` function:

```python
datetime_in_Lagos = datetime.now(pytz.timezone('Africa/Lagos'))
```

The `pytz` object has a `timezone` attribute that takes information/parameter(s) of the specific time-zone you're looking for: `pytz.timezone('Africa/Lagos')`. 

With the `all_timezones` attribute, you can get a list of all the possible time-zones in the `pytz` library that can be passed in as parameters to the `timezone` attribute - just like we did in the last example. That is:

```python
from datetime import datetime
import pytz

all_timezones = pytz.all_timezones

print(all_timezones)
# [List of all timezones...]
```

## Summary

In this article, we talked about getting today's date and time using the `datetime.now()` function in Python. 

We saw some examples that showed how to use the `datetime.now()` function and its attributes.

Lastly, we saw how to get the date and time in specific locations around the world using the `datetime.now()` function and the `pytz` module. 

Happy coding!

