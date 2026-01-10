---
title: How to Use timedelta Objects in Python to Work with Dates
subtitle: ''
author: Bala Priya C
co_authors: []
series: null
date: '2021-06-29T18:25:52.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-timedelta-objects-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/TIMEDELTA-OBJECTS-IN-PYTHON.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "Why do we need the timedelta object?\nWhen you're working with dates and\
  \ times in Python, you'll often use the datetime module. \nIn this post, we'll see\
  \ how we can use the timedelta object in the datetime module. It denotes a span\
  \ of time and can help..."
---

### Why do we need the timedelta object?

When you're working with dates and times in Python, you'll often use the `datetime` module. 

In this post, we'll see how we can use the `timedelta` object in the `datetime` module. It denotes a span of time and can help when we need to perform simple arithmetic operations on datetime objects.

In particular, we shall learn how to do the following with code examples:

1. Create a basic `timedelta` object
2. Print the current date and time
3. Calculate a date in the future
4. Calculate a date in the past
5. Calculate the time elapsed since a particular event or the time remaining for a particular event to occur

### Necessary Imports

Before we get started with these tasks, let's first import the necessary modules as shown in the code snippet below:

```python
# Import Necessary Modules
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
```

## How to Create a Basic timedelta Object in Python

Let's now create a basic `timedelta` object, like this:

```python
time_delt1 = timedelta(days= 270, hours = 9, minutes = 18)
print(time_delt1)

# Sample Output
270 days, 9:18:00
```

We've successfully created a `timedelta` object. Now, we need to create a reference time so that we can apply the `timedelta` object that we have created to perform meaningful arithmetic. Let's do that in the next step.

## How to Print the Current Date and Time in Python

In order to apply the span we created using the `timedelta` object, we'll use the current date and time as a reference. 

We can get the current date and time by calling the `now()` method on the `datetime` object, as shown in the code snippet below:

```python
# to create reference, use current date and time
time_now = datetime.now()
print(time_now)

# Sample Output
2021-06-22 17:49:18.574503
```

## How to Calculate a Date in the Future in Python

Now let's calculate what date it will be after a span of `time_delt1` that we created in the first step above. 

To calculate a future point in time, we only have to add the span defined by the `timedelta` object to the current time.

```python
# check what date it'll be after time_delt1
future_date1 = time_now + time_delt1
print(future_date1)

# Sample Output
2022-03-20 03:07:18.574503
```

Now, let's look at another example where we want to know what date it'll be after a specific number of days, say 189 days.

```python
# What day will it be after 189 days
future_date2 = time_now + timedelta(days=189)
print(future_date2)

# Sample Output
2021-12-28 17:49:18.574503
```

## How to Calculate a Date in the Past in Python

As you might have guessed by now, to find out what day it was 189 days ago, we only have to replace '+' with a '- ' in the above example. You can see this in the code snippet below:

```python
# What day would it have been 189 days ago
past_date1 = time_now - timedelta(days=189)
print(past_date1)

# Sample Output
2020-12-15 17:49:18.574503
```

## How to Calculate Time Elapsed or Time Remaining in Python

Let's now calculate the time left before this year's Teachers' Day. We can do this as follows. 

To calculate with reference to today, we can call the `today()` method on the date object to retrieve today's date:

`Syntax: today = date.today() #Returns today's date`

```python
# create reference objects for today, and teachers' day
teachers_day = date(time_now.year, 9, 5)
today = date.today()
```

We can then find out how far in the future Teachers' Day is using the following code snippet:

```python
# calculate number of days to teachers' day.
time_to_td = teachers_day - today
print(f"Teachers' day is {time_to_td.days} days away")

# Sample Output
Teachers' day is 74 days away
```

It is also possible that this year's Teachers' day will have passed by the time you read this post 😀. If Teachers' Day for this year has already passed, do the following:

* Update the date of interest to next year's Teachers' day date.
* Calculate how many days are left before Teachers' day next year.

This is illustrated in the following code snippet:

```python
# check if teachers' day has passed
if teachers_day < today:
  print(f"This year's Teachers' Day was {(today-teachers_day).days} days ago")
  time_to_td = teachers_day - today
  print(f"Next year's Teachers' day is {time_to_td.days} days away")
```

## A Quick Recap

To summarize, we've seen how we can use `timedelta` objects to perform simple arithmetic on dates and calculate a past and future date. 

We can also calculate the time elapsed since a particular event or the time remaining before a particular event. 

Hope you found this post helpful. Thank you for reading!

For a more detailed reference, please check the official documentation [here](https://docs.python.org/3/library/datetime.html).

