---
title: Python String to Int – Convert a String Example
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-03-17T23:53:39.000Z'
originalURL: https://freecodecamp.org/news/python-string-to-int-convert-a-string-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/integer.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "When creating a program, you may need to get numerical input from users\
  \ and perform various mathematical operations on the value. \nSimilarly, there are\
  \ cases where you might want to perform mathematical operations on string values.\
  \ \nIn both cases, th..."
---

When creating a program, you may need to get numerical input from users and perform various mathematical operations on the value. 

Similarly, there are cases where you might want to perform mathematical operations on string values. 

In both cases, the values returned are strings so we cannot perform mathematical operations with them as this will throw an error our way.

In this article, we'll see how to convert a string to an integer in Python with some examples.

## How to Convert a String to Int in Python

In Python, we can use the built in `int()` function to convert strings to integers. Here is what the syntax looks like: 

```
int(string_value)
```

So we pass the string to be converted as an argument in the `int()` function. That's it!

Here is an example to help you understand:

```python
userAge = "10"

print(userAge + 8)

# TypeError: can only concatenate str (not "int") to str
```

In the example above, we are adding 8 to the `userAge` variable which is a string – but this shows an error because the interpreter assumes we are trying to add (concatenate) two strings. 

Now let's convert the variable to an integer and perform the same operation:

```python
userAge = "10"

convertUserAge = int(userAge)

print(convertUserAge + 8)

# 18
```

We converted the `userAge` variable and stored it in a variable called `convertUserAge` and then performed our operation again to get the expected result. 

In the next example, similar to the last one, we will get a user's input and perform some calculations to display their age.

```python
from datetime import date

currentDate = date.today()
currentYear = currentDate.year

userBirthYear = input("What is your birth year?")

convertUserBirthYear = int(userBirthYear)

userAge = currentYear - convertUserBirthYear

print(userAge)

```

In the code above, we first imported the `date` class from the `datetime` module. With this, we were able to get and store the current year in a variable. 

We then requested the user's birth year: `userBirthYear = input("What is your birth year?")`

After that we converted the user's birth year (which was returned to us as a string) to an integer using the `int()` function. With the integer value, we were able to subtract the user's birth year from the current year to get and print their actual age.

You can copy the code and play around with it.

## Conclusion

In this article, we learned how to convert strings to integers in Python.  We first saw an example where we had to use the `int()` function to convert a string to an integer and perform a simple operation with the value.

In the second example, we got an input from a user, converted it to an integer, and then performed our mathematical operation to print their current age.

Thank you for reading and happy coding!

