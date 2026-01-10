---
title: How to Square a Number in Python – Squaring Function
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-05-31T15:03:14.000Z'
originalURL: https://freecodecamp.org/news/how-to-square-a-number-in-python-squaring-function
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/square-number-python.png
tags:
- name: Math
  slug: math
- name: Python
  slug: python
seo_title: null
seo_desc: "By Dillion Megida\nTo square a number, you multiply that number by itself.\
  \ And there are multiple ways to do this in Python. \nYou can directly multiple\
  \ a number by itself (number * number) but in this article, I'll show you three\
  \ ways you can do this ..."
---

By Dillion Megida

To square a number, you multiply that number by itself. And there are multiple ways to do this in Python. 

You can directly multiple a number by itself (**number * number**) but in this article, I'll show you three ways you can do this without hardcoding both numbers.

The three ways are:
* \*\*, the power operator
* the in-built `pow()` function
* the `math.pow()` function from the `math` module

## How to Use the Power Operator (**) in Python

`**` is called the power operator. You use it to raise a number to a specified power. Here is the syntax:

```Python
number ** exponent
```

The expression above is evaluated as **number * number...** (for as many times as the value of the exponent). You can also read the expression as **5<sup>2</sup>**.

Using this operator, you can find the square of a number using **2** as the exponent. For example, to find the square of 5, you can do this:

```Python
square = 5 ** 2

print(square)
# 25
```

The power operator evaluates the expression as **5 * 5**, which results in 25.

## How to Use the `pow()` Function in Python

Python has an inbuilt `pow()` function, which evaluates a number to the power of another number. Here's the syntax:

```Python
pow(base, exponent)
// interpreted as ^3
```

The code above is interpreted as base<sup>exponent</sup>.

The function accepts two arguments: the number to be raised (known as the **base**) and the power the number should be raised to (the **exponent**).
    
To find the square of a number using this function, the number will be the base, and the exponent will be **2**, which means number<sup>2</sup>.
    
To find the square of **5**, for example, you can use this function like this:
    
```Python
square = pow(5, 2)
    
print(square)
# 25
```
    
The `pow()` function also receives a third argument: the **modulo**. The sign for modulo is **%**. This argument evaluates the remainder when a value is divided by another.
    
For example, **5 % 2** gives **1** because 5 divided by 2 is 2, remainder 1.
    
Applying the modulo the `pow()` function looks like this:
    
```python
mod = pow(5, 2, 3)

print(mod)
## 1
## 5 * 5 is 25
## 25 % 3 is 1
```
    
According to the [python documentation on pow](https://docs.python.org/2/library/functions.html#pow), this approach computes more efficiently than `pow(5,2) % 3`
    
## How to USe the math.pow() Function in Python
    
`math.pow()` comes from Python's `math` module. This function is similar to the in-built `pow()` function in usage and syntax, except that it has two differences:

* it only accepts two arguments: the **base** and the **exponent**
* it always returns a float number even when the raised number is a whole number.

So, `math.pow(5, 2)` returns **25.0**.

`pow()` will only return a float number when the number is a float. It will return an integer if the number is whole. But `math.pow()` always returns a float number.

Now you know how to square numbers in Python! Thank you for reading.


