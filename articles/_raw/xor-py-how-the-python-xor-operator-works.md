---
title: xor.py – How the Python XOR Operator Works
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-05-08T16:35:55.000Z'
originalURL: https://freecodecamp.org/news/xor-py-how-the-python-xor-operator-works
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/xor-in-python.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "You can use bitwise operators in Python to perform different operations\
  \ on the individual bits of an integer. \nThere are different bitwise operators\
  \ like the bitwise AND (&), bitwise OR (|), bitwise XOR (^), and so on. \nIn this\
  \ article, we'll focus o..."
---

You can use bitwise operators in Python to perform different operations on the individual bits of an integer. 

There are different bitwise operators like the bitwise AND (`&`), bitwise OR (`|`), bitwise XOR (`^`), and so on. 

In this article, we'll focus on the bitwise XOR (`^`) operator. You'll learn about its mode of operation along with some practical examples. 

## How the Python XOR Operator Works

The XOR operator first converts the integers involved in the operation to their binary format. The operator then evaluates the corresponding bits of the binary values.

When two bits are evaluated, the value returned will be dependent on the bits. If both bits are 0, 0 is returned. If both bits are 1, 0 is returned. If either of the bits is 1 while the other is 0 then 1 will be returned. 

So the XOR operator will only return 1 when two bits have different values. That is: 

0 ^ 0 = 0.   
1 ^ 1 = 0.  
1 ^ 0 = 1.  
0 ^ 1 = 1.

After evaluating all the corresponding bits, the resulting binary value will be returned in base 10. 

Don't worry if the explanations above seem confusing – the examples in the next section should simplify how the XOR operator works.

## Python XOR Operator Example

In this section, you'll see code examples that show how the bitwise XOR operator works. 

```python
x = 12
y = 10

print(x ^ y)
# 6
```

In the code above, we created two variables `x` and `y` with 12 and 10 as their respective values. 

Using the XOR operator — `x ^ y` — we got 6 returned. 

Let's break the code down to see how we got a value of 6 from the operation.

### Step #1 - Conversion to Binary Values

We started with two values (12 and 10):

```python
x = 12
y = 10
```

These values have to be converted to their binary format by the XOR operator before the operations starts. 

The binary value of 12 is 1100 while the binary value of 10 is 1010. 

### Step #2 - Evaluating Corresponding Bits

Now that the values have been converted to their binary formats, the next thing that the XOR operator does is to compare corresponding bits. 

So the first bit in 1100 will be compared to the first bit in 1010. The second bit in both binary values will be compared next. This comparison will continue until there are no bits left to compare. 

Recall that we discussed how the XOR operator returns a value from each comparison: 

0 ^ 0 = 0.   
1 ^ 1 = 0.  
1 ^ 0 = 1.  
0 ^ 1 = 1.

Using the logic above, lets compare the bits in both operands — 1100 and 1010. We'll denote them as operand A and B, respectively.

Operand A's first bit value = 1. Operand B's first bit value = 1.   
1 ^ 1 = 0. 

Operand A's second bit value = 1. Operand B's second bit value = 0.   
1 ^ 0 = 1. 

Operand A's third bit value = 0. Operand B's third bit value = 1.   
0 ^ 1 = 1. 

Operand A's fourth bit value = 0. Operand B's fourth bit value = 0.   
0 ^ 0 = 0. 

When we collect the resulting values from each comparison, we have 0110 which is the same as 6 in base 10. 

The bit comparisons above explain how the code in the last section returned a value of 6. That is:

```python
x = 12
y = 10

print(x ^ y)
# 6
```

## Summary

In this article, we talked about bitwise operators in Python. They are used to perform operations involving the individual bits of integers. 

We talked about the bitwise XOR (`^`) operator which converts integers to their binary format, and the compares their corresponding bit values. 

We saw an example that showed how the XOR operator works under the hood. 

Happy coding! You can learn more about Python on [my blog](https://ihechikara.com/).

