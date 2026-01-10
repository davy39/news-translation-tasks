---
title: strftime – Python DateTime Timestamp String
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-04-19T01:15:23.000Z'
originalURL: https://freecodecamp.org/news/strftime-python-datetime-timestamp-string
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/brooke-lark-BRBjShcA8D4-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'The datetime object lets us work with dates and times in Python. But the
  value returned when we use this object is of the datatime data type rather than
  a string.

  Here is an example that prints the current year, month, day and time to the console:

  fr...'
---

The `datetime` object lets us work with dates and times in Python. But the value returned when we use this object is of the `datatime` data type rather than a `string`.

Here is an example that prints the current year, month, day and time to the console:

```python
from datetime import datetime

current_day = datetime.now() 

print(current_day)
# 2022-04-18 21:50:24.524022

print(type(current_day))
# <class 'datetime.datetime'>
```

In the code above, we imported the `datetime` object first. `datetime.now()` gives us the all the information about the current day which we stored in a variable called `current_day`. 

When we printed `current_day`, we got this: `2022-04-18 21:50:24.524022`. This shows us year, month, day, and time. And when we printed the type to the console, we got `datetime`.

In this article, we'll talk about the `strftime()` method provided by the `datetime` object. This method let us convert date and time objects in Python to their `string` format.

## What Does `Strptime` Do in Python?

The `strftime()` method takes in an argument (a format code) that specifies what we want to return. 

Here's an example:

```python
from datetime import datetime

current_day = datetime.now()

year = current_day.strftime("%Y")

print("current year:", year)
# current year: 2022

print(type(year))
# <class 'str'>
```

The code above is similar to the last example except that we created a new variable called `year`. In this variable, we attached the `strftime()` method to the current year: `current_day.strftime("%Y")`. 

You'll notice that we passed in an argument to the method – "%Y" – which denotes year. This is called a format code. In the next example, we'll see other format codes.

After using the `strftime()` method, the data type can now be seen as a `string`.

Here is another example:

```python
from datetime import datetime

current_day = datetime.now()

year = current_day.strftime("%Y")
print("current year:", year)
# current year: 2022

month = current_day.strftime("%B")
print("current month:", month)
# current month: April

day = current_day.strftime("%A")
print("current day:", day)
# current day: Monday

time = current_day.strftime("%-I %p")
print("current time:", time)
# current time: 9 PM
```

In the example above, we passed in different format codes in the `strftime()` method to return `string` values for the `month`, `day`, and `time` variables.

These aren't the only format codes that exist. Click [here](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes) to see more format codes you can play around with to see what they do.

## Conclusion

In this article, we talked about the `strftime()` method which helps us convert date and time objects to `strings`.

We saw various format codes that can be passed in as arguments to return different date and time object values.

Happy coding!

