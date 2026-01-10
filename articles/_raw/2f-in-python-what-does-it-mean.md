---
title: '%.2f in Python – What does it Mean?'
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-06-22T18:30:58.000Z'
originalURL: https://freecodecamp.org/news/2f-in-python-what-does-it-mean
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/susan-holt-simpson-GQ327RPuxhI-unsplash.jpg
tags:
- name: Math
  slug: math
- name: Python
  slug: python
seo_title: null
seo_desc: "In Python, there are various methods for formatting data types. \nThe %f\
  \ formatter is specifically used for formatting float values (numbers with decimals).\
  \ \nWe can use the %f formatter to specify the number of decimal numbers to be returned\
  \ when a fl..."
---

In Python, there are various methods for formatting data types. 

The `%f` formatter is specifically used for formatting float values (numbers with decimals). 

We can use the `%f` formatter to specify the number of decimal numbers to be returned when a floating point number is rounded up. 

## How to Use the `%f` Formatter in Python

In this section, you'll see some examples on how to use the `%f` formatter and the various parameters it can be used with to return varying results.

Here's the first example:

```python
floatNumber = 1.9876

print("%f" % floatNumber)
# 1.987600
```

Using `%f` in the example above added two zeros to the number. But there's nothing too special about that. We'll see what else we can do to modify the resulting value soon.

Note that the `%f` formatter must be nested inside quotation marks, and should be separated from the floating number which it is formatting by a modulo operator (%): `"%f" % floatNumber`.

Let's take a look at another example. 

```python
floatNumber = 1.9876

print("%.1f" % floatNumber)
# 2.0
```

In the code above, we added .1 between % and f in the `%f` operator. This means that we want the number to be rounded up to one decimal place.

Note that you'll get a similar result to the one in the first example if you omit the period/dot symbol (**.**) that comes before the digit we passed in-between % and f.

The resulting value in our example is 2.0 which was returned when 1.9876 was rounded up to one decimal place.

Let's use `%.2f` and see what happens.

```python
floatNumber = 1.9876

print("%.2f" % floatNumber)
# 1.99
```

As expected, the floating point number (1.9876) was rounded up to two decimal places – 1.99. So `%.2f` means to round up to two decimal places.

You can play around with the code to see what happens as you change the number in the formatter. 

## How to Use the `%d` Formatter in Python

Another formatting method we can use with floating point numbers in Python is the `%d` formatter. This returns the whole number in a floating point number. 

Here's an example:

```python
floatNumber = 1.9876

print("%d" % floatNumber)
# 1
```

In the example above, we created a floating point number: `floatNumber = 1.9876`. 

When the `floatNumber` variable was formatted using `%d`, only 1 was returned. 

The `%d` formatter ignores the decimal numbers and returns only the whole number. 

## Summary

In this article, we talked about the `%f` formatter in Python. You use it to format floating point numbers. 

Depending on the parameters provided, the `%f` formatter rounds up a float value to the nearest decimal place provided.

We also talked about the `%d` formatter which returns only a whole number from a floating point number. 

Happy coding!

