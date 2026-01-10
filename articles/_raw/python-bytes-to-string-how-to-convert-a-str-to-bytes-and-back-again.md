---
title: Exponent in Python – Power Function and Exponents Using a Loop
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-02-14T17:54:02.000Z'
originalURL: https://freecodecamp.org/news/python-bytes-to-string-how-to-convert-a-str-to-bytes-and-back-again
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/21.-exponents.png
tags:
- name: Math
  slug: math
- name: Python
  slug: python
seo_title: null
seo_desc: 'By Dillion Megida

  The exponent of a number refers to the power to which that number should be raised.
  In this article, I''ll show you how to find exponents using two ways: the power
  function and a loop.

  Exponents are usually written like this: Baseexp...'
---

By Dillion Megida

The exponent of a number refers to the power to which that number should be raised. In this article, I'll show you how to find exponents using two ways: the power function and a loop.

Exponents are usually written like this: **Base<sup>exponent</sup>**

Take an example like **10<sup>3</sup>**. This means, "10, raised to the power of 3". The result of this is evaluated as `10 * 10 * 10` (10 multiplied by itself 3 times), which is `1000`.

There are different ways you can evaluate the exponent of a number (the number is referred to as the base). One way is using the `**` operator. With this operator, you have the number, followed by the operator, and then the exponent like this `10 ** 3` which is 10<sup>3</sup>

But in this post, I'll show you two other ways, which are the `pow` function and using a loop.

## Exponents with the `pow` function

`pow` is an in-built function in Python for evaluating a number raised to an exponent. The syntax for this function is:

```python
pow(base, exponent, modulo)
```

This function accepts three arguments:
* `base`: the number which will be raised
* `exponent`: the power to which the number will be raised
* `modulo`: an optional number that evaluates the remainder when the raised number is divided by it

The last argument is optional, but according to the [python documentation on pow](https://docs.python.org/2/library/functions.html#pow), this argument computes more efficiently than `pow(base, exponent) % number`.

Let's see some examples:

```python
result1 = pow(100, 3)
print(result1) # 1000000

result2 = pow(5, 4)
print(result2) # 625

result3 = pow(3, 2, 5)
print(result3) # 4
```

In the last example, we have `pow(3, 2, 5)`. What happens here is that 3 is first raised to the power of 2, which is 9. Then 9 is divided by 5, and the remainder, which is returned, is `4`.

Note that there's also a `Math.pow` function in Python. The difference between this and pow(), is that `pow()` will only return a float number when the number is a float. It will return an integer if the number is whole. But `math.pow()` always returns a float number.

## Exponents with a loop

You can use any kind of loop to achieve this, but for this post, I'll use a `while` loop.

The syntax for a `while` loop is:

```python
while condition:
  # code to execute
```

For exponents, I can put this loop in a function like this:

```python
def loopExp(number, exp):
  result = number
  counter = 1
  
  while counter < exp:
    result *= number
    counter += 1
   
  return result
```

Here, we defined a `loopExp` function that takes two inputs: `number` and `exp` which stands for exponent.

In the function, we initialize the `result` and `counter` variables with the value of `number` and `1` respectively. Then we have the `while` loop which runs as long as the `counter` variable is less than the `exp` input.

In each loop, we update the `result` variable by multiplying the previous value of the `result` with the `number` input. We also increment the `counter` variable by 1. Then we return the `result` variable.

Let's see this function in use:

```python
result1 = loopExp(100, 3)
print(result1) # 1000000

result2 = loopExp(5, 4)
print(result2) # 625

result3 = loopExp(3, 2)
print(result3) # 9
```

As you can see in the results, we have the exponents calculated using the loop in the `loopExp` function.

## Wrapping up

In this article, I've shown you how to evaluate exponents in different ways. I used examples to show you the `**` operator, the `pow` and `Math.pow` functions, and also using a loop.

Kindly share this if you find it helpful :) 


