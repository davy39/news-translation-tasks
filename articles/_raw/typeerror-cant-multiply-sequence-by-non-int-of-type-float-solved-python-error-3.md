---
title: 'TypeError: can''t multiply sequence by non-int of type float [Solved Python
  Error]'
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-12-21T21:13:46.000Z'
originalURL: https://freecodecamp.org/news/typeerror-cant-multiply-sequence-by-non-int-of-type-float-solved-python-error-3
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/pexels-polina-zimmerman-3747132.jpg
tags:
- name: error
  slug: error
- name: error handling
  slug: error-handling
- name: Python
  slug: python
seo_title: null
seo_desc: "Most times when you encounter errors while coding, you can discover the\
  \ reason why the error is occurring and how you can fix it in the error message.\
  \ \nThe Python error, \"TypeError: can't multiply sequence by non-int of type float\"\
  \ is no exception to..."
---

Most times when you encounter errors while coding, you can discover the reason why the error is occurring and how you can fix it in the error message. 

The Python error, "TypeError: can't multiply sequence by non-int of type float" is no exception to that.

I have prepared this article to show you why this error occurs and how you can fix it. Read on.

## Why the "TypeError: can't multiply sequence by non-int of type float" Error Occurs

To understand why you get the error "TypeError: can't multiply sequence by non-int of type float", let's look at the keywords in the error: **Typeerror**, **multiply**, **sequence**, and **type float**.

- **Typeerror** is an exception thrown when you put together inappropriate data types in an operation
-  **multiply** in the error means you're trying to perform a multiplication
- **sequence** is an ordered set in Python. It could be strings, lists, or tuples.
- **type float** means there's a decimal number in the operation you're trying to perform, for example, 2.4 or 5.40

So, if you're getting this error, it means you're multiplying any of those sequences (usually a string and a tuple) with a floating point number (decimal number).

Indeed, you can multiply a sequence with a number and Python will do the work properly:

```py
site_name = 'freeCodeCamp '

print(site_name * 2)
# freeCodeCamp freeCodeCamp 

print(site_name * 3)
# freeCodeCamp freeCodeCamp freeCodeCamp
```

```py
stringfied_num = '10 '

print(stringfied_num * 3)
# 10 10 10
```

Same thing also works for tuples:

```py
myTuple = (4, 3, 4)
print(myTuple * 2)

# (4, 3, 4, 4, 3, 4)
```

But if you try to do the multiplication with a decimal point number, you get the error "TypeError: can't multiply sequence by non-int of type float":

```py
site_name = 'freeCodeCamp '

print(site_name * 2.5)
# Traceback (most recent call last):  
#   File "seq.py", line 3, in <module>
#     print(site_name * 2.5)
# TypeError: can't multiply sequence by non-int of type 'float'
```

```py
myTuple = (4, 3, 4)
print(myTuple * 2.2)

# Traceback (most recent call last):   
#   File "seq.py", line 11, in <module>
#     print(myTuple * 2.2)
# TypeError: can't multiply sequence by non-int of type 'float'
```

## How to Fix the "TypeError: can't multiply sequence by non-int of type 'float'" Error

To fix the error "TypeError: can't multiply sequence by non-int of type 'float'", make sure you're not multiplying the string or tuple with a decimal point number. 

So instead of multiplying the string or tuple with a floating point number, use an integer. For instance `"freeCodeCamp" * 5` instead of `"freeCodeCamp" * 5.6`:

```py
site_name = 'freeCodeCamp '
print(site_name * 5)

# freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp
```

If you're dealing with a number in strings, for example, "10", you can convert the string to an integer with the `int()` method and to float with the `float()` method:

```py
stringfied_num = '10 '

print(int(stringfied_num) * 3)
# 30
```
```py
stringfied_num = '10 '

print(float(stringfied_num) * 3)
# 30
```

If you're dealing with a user input, you can also find a way to convert the floating-point number to an integer. In fact, you should handle the possibility of the user entering a decimal point number instead of a straight integer:

```py
# declare a string variable
site_name = 'freeCodeCamp '

# Get the user input and convert it to a decimal number
user_input = float(input("Enter a number: "))

# Round the number entered by the user to the nearest whole number
rounded_input = round(user_input)

# Multiply the site_name variable by the user input
result = rounded_input * site_name

# Print the result to the console
print(result)

# I entered 3.6 and the result was: freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp
```

## Conclusion
You cannot multiply a sequence by a floating point number. What you get if you do that is the error, TypeError: can't multiply sequence by non-int of type 'float'. That's why this article was dedicated to letting you know how to fix the error.

The takeaway from this article is that if you're using any string as a number, you should make sure they are converted with the `float()` method – especially if they are used in a calculation.


