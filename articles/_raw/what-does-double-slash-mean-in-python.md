---
title: What Does // Mean in Python? Operators in Python
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-07-21T15:30:37.000Z'
originalURL: https://freecodecamp.org/news/what-does-double-slash-mean-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/doubleSlash.png
tags:
- name: Math
  slug: math
- name: Python
  slug: python
seo_title: null
seo_desc: 'In Python, you use the double slash // operator to perform floor division.
  This // operator divides the first number by the second number and rounds the result
  down to the nearest integer (or whole number).

  In this article, I will show you how to use...'
---

In Python, you use the double slash `//` operator to perform floor division. This `//` operator divides the first number by the second number and rounds the result down to the nearest integer (or whole number).

In this article, I will show you how to use the `//` operator and compare it to regular division so you can see how it works.

It doesn’t end there, though – you will also learn about a Python math method that is synonymous with the double slash `//` operator.

## What We'll Cover
- [The Basic Syntax of the `//` Operator](#heading-the-basic-syntax-of-the-operator)
- [Examples of Floor Division](#heading-examples-of-floor-division)
- [The Double Slash `//` Operator Works Like `math.floor()`](#heading-the-double-slash-operator-works-like-mathfloor)
- [How the Double Slash `//` Operator Works Behind the Scenes](#heading-how-the-double-slash-operator-works-behind-the-scenes)
- [Conclusion](#heading-conclusion)

## The Basic Syntax of the `//` Operator

To use the double slash `//` operator, you do things almost like in regular division. The only difference is that instead of a single slash `/`, you use double slash `//`:
```py
firstNum // secondNum
```

## Examples of Floor Division

In the example below, the floor division of 12 by 5 resulted in 2:
```py
num1 = 12
num2 = 5
num3 = num1 // num2

print("floor division of", num1, "by", num2, "=", num3)
# Output: floor division of 12 by 5 = 2
```
Whereas, the regular division of 12 by 5 would be equal to 2.4. That is, 2 remainder 4:
```py’num1 = 12
num2 = 5
num3 = num1 / num2

print("normal division of", num1, "by", num2, "=", num3)
# Output: normal division of 12 by 5 = 2.4
```

This shows you that the `//` operator rounds down the result of the division of two numbers to the nearest whole number. 

Even if the decimal point is 9, the `//` operator would still round the result down to the nearest whole number.

```py
num1 = 29 
num2 = 10 
num3 = num1 / num2
num4 = num1 // num2

print("normal division of", num1, "by", num2, "=", num3)
print("but floor division of", num1, "by", num2, "=", num4)

"""
Output:
normal division of 29 by 10 = 2.9
but floor division of 29 by 10 = 2
"""
```
And if you perform floor division with a negative number, the result would still be rounded down.

To prepare your mind for the result, rounding down a negative number means going away from 0. So, -12 divided by 5 results in -3. Don’t get confused – even though at first glance it seems like the nubmer is getting "bigger", it's actually getting smaller (further from zero/a larger negative number).
```py
num1 = -12
num2 = 5
num3 = num1 // num2

print("floor division of", num1, "by", num2, "=", num3)

# floor division of -12 by 5 = -3
```

## The Double Slash `//` Operator Works Like `math.floor()`
In Python, `math.floor()` rounds down a number to the nearest integer, just like the double slash `//` operator does.

So, `math.floor()` is an alternative to the `//` operator because they do the same thing behind the scenes.

Here's an example:
```py
import math

num1 = 12
num2 = 5
num3 = num1 // num2
num4 = math.floor(num1 / num2)

print("floor division of", num1, "by", num2, "=", num3)
print("math.floor of", num1, "divided by", num2, "=", num4)

"""
Output:
floor division of 12 by 5 = 2
math.floor of 12 divided by 5 = 2
"""
```
You can see that `math.floor()` does the same thing as the `//` operator.

## How the Double Slash `//` Operator Works Behind the Scenes

When you use the `//` operator to divide two numbers, the method that gets called behind the scenes is the `__floordiv__()`.

You can also use this `__floordiv__()` method directly in place of the `//` operator:
```py
num1 = 12
num2 = 5
num3 = num1 // num2
num4 = num1.__floordiv__(num2)

print("floor division of", num1, "by", num2, "=", num3)
print("using the floordiv method gets us the same value of", num4)

"""
Output:
floor division of 12 by 5 = 2
using the floordiv method gets us the same value of 2
"""
```

## Conclusion

In this article, you’ve learned how you can use the double slash `//` operator and how it works behind the scenes.

In addition, you learned about two alternatives of the `//` operator – `math.floor()` and the `__floordiv__()` method.

Don’t be confused about which to use. The three ways you can perform floor division work the same way. But I would advise you to use the double slash `//` operator because you get to type less with it.

Thank you for reading.


