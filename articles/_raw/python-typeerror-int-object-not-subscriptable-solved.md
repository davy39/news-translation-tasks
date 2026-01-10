---
title: 'TypeError: ''int'' object is not subscriptable [Solved Python Error]'
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-10-31T17:37:23.000Z'
originalURL: https://freecodecamp.org/news/python-typeerror-int-object-not-subscriptable-solved
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/in_not_subable.png
tags:
- name: error
  slug: error
- name: error handling
  slug: error-handling
- name: Python
  slug: python
seo_title: null
seo_desc: "The Python error \"TypeError: 'int' object is not subscriptable\" occurs\
  \ when you try to treat an integer like a subscriptable object. \nIn Python, a subscriptable\
  \ object is one you can “subscript” or iterate over. \nWhy the \"TypeError: 'int'\
  \ object is n..."
---

The Python error "TypeError: 'int' object is not subscriptable" occurs when you try to treat an integer like a subscriptable object. 

In Python, a subscriptable object is one you can “subscript” or iterate over. 

## Why the "TypeError: 'int' object is not subscriptable Error" Occurs
You can iterate over a string, list, tuple, or even dictionary. But it is not possible to iterate over an integer or set of numbers. 

So, if you get this error, it means you’re trying to iterate over an integer or you’re treating an integer as an array.

In the example below, I wrote the date of birth (`dob` variable) in the ddmmyy format. I tried to get the month of birth but it didn’t work. It threw the error “TypeError: 'int' object is not subscriptable”:

```py
dob = 21031999
mob = dob[2:4]

print(mob)

# Output: Traceback (most recent call last):
#   File "int_not_subable..py", line 2, in <module>
#     mob = dob[2:4]
# TypeError: 'int' object is not subscriptable
```

## How to Fix the "TypeError: 'int' object is not subscriptable" Error

To fix this error, you need to convert the integer to an iterable data type, for example, a string. 

And if you’re getting the error because you converted something to an integer, then you need to change it back to what it was. For example, a string, tuple, list, and so on.

In the code that threw the error above, I was able to get it to work by converting the `dob` variable to a string:

```py
dob = "21031999"
mob = dob[2:4]

print(mob)

# Output: 03
```

If you’re getting the error after converting something to an integer, it means you need to convert it back to string or leave it as it is. 

In the example below, I wrote a Python program that prints the date of birth in the ddmmyy format. But it returns an error:

```py
name = input("What is your name? ")
dob = int(input("What is your date of birth in the ddmmyy order? "))
dd = dob[0:2]
mm = dob[2:4]
yy = dob[4:]
print(f"Hi, {name}, \nYour date of birth is {dd} \nMonth of birth is {mm} \nAnd year of birth is {yy}.")

#Output: What is your name? John Doe
# What is your date of birth in the ddmmyy order? 01011970
# Traceback (most recent call last):
#   File "int_not_subable.py", line 12, in <module>
#     dd = dob[0:2]
# TypeError: 'int' object is not subscriptable
```

Looking through the code, I remembered that input returns a string, so I don’t need to convert the result of the user’s date of birth input to an integer. That fixes the error:

```py
name = input("What is your name? ")
dob = input("What is your date of birth in the ddmmyy order? ")
dd = dob[0:2]
mm = dob[2:4]
yy = dob[4:]
print(f"Hi, {name}, \nYour date of birth is {dd} \nMonth of birth is {mm} \nAnd year of birth is {yy}.")

#Output: What is your name? John Doe
# What is your date of birth in the ddmmyy order? 01011970
# Hi, John Doe,
# Your date of birth is 01
# Month of birth is 01
# And year of birth is 1970.
```

## Conclusion
In this article, you learned what causes the "TypeError: 'int' object is not subscriptable" error in Python and how to fix it.

If you are getting this error, it means you’re treating an integer as iterable data. Integers are not iterable, so you need to use a different data type or convert the integer to an iterable data type. 

And if the error occurs because you’ve converted something to an integer, then you need to change it back to that iterable data type.

Thank you for reading.


