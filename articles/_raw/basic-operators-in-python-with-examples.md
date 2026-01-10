---
title: Basic Operators in Python With Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/basic-operators-in-python-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d03740569d1a4ca356e.jpg
tags:
- name: Python
  slug: python
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'Operators are symbols which tells the interpreter to do a specific operation
  such as arithmetic, comparison, logical, and so on.

  The different types of operators in Python are listed below:


  Arithmetic Operators

  Relational Operators

  Bitwise Operators...'
---

Operators are symbols which tells the interpreter to do a specific operation such as arithmetic, comparison, logical, and so on.

The different types of operators in Python are listed below:

1. Arithmetic Operators
2. Relational Operators
3. Bitwise Operators
4. Assignment Operators
5. Logical Operators
6. Membership Operators
7. Identity Operators

## Arithmetic Operators

An arithmetic operator takes two operands as input, performs a calculation and returns the result.

Consider the expression, **“a = 2 + 3”**. Here, `2` and `3` are the _operands_ and `+` is the _arithmetic operator_. The result of the operation is stored in the variable `a`.

| Operator | Description | Usage |
| :---: | :---: | :---: |
| + | Performs Addition on the operands | 12 + 3 = 15 |
| - | Performs Subtraction on the operands | 12 - 3 = 9 |
| * | Performs Multiplication on the operands | 12 * 3 = 36 |
| / | Performs Division on the operands | 12 / 3 = 4 |
| % | Performs a Modulus on the operands | 16 % 3 = 1 |
| ** | Performs an Exponentiation operation | 12 ** 3 = 1728 |
| // | Performs a Floor Division operation | 18 // 5 = 3 |

Note: To get the result in floating type, one of the operands must also be of float type.

## Relational Operators

A relational operator is used to compare two operands to decide a relation between them. It returns a boolean value (true or false) based on the condition.

| Operator | Description | Usage |
| :---: | :---: | :---: |
| > | Returns True if the left operand is greater than the right operand | 12 > 3 returns True |
| < | Returns True if the right operand is greater than the left operand | 12 < 3 returns False |
| == | Returns True if both the operands are equal | 12 == 3 returns False |
| >= | Returns True if the left operand is greater than or equal to the right operand | 12 >= 3 returns True |
| <= | Returns True if the right operand is greater than or equal to the left operand | 12 <= 3 returns False |
| != | 	Returns True if both the operands are not equal | 12 != 3 returns True |


## Bitwise Operators

A bitwise operator performs operations on the operands bit by bit

Consider a = 2 (in binary notation, 10) and b = 3 (in binary notation, 11) for the below usages.

| Operator | Description | Usage |
| :---: | :---: | :---: |
| & | Performs bitwise AND operation on the operands | a & b = 2 (Binary: 10 & 11 = 10) |
| \| | Performs bitwise OR operation on the operands | a \| b = 3 (Binary: 10 \| 11 = 11) |
| ^ | Performs bitwise XOR operation on the operands | a ^ b = 1 (Binary: 10 ^ 11 = 01) |
| ~ | Performs bitwise NOT operation on the operand. Flips every bit in the operand | ~a = -3 (Binary: ~(00000010) = (11111101)) |
| >> | Performs a bitwise right shift. Shifts the bits of left operand, right by the number of bits specified as the right operand | a >> b = 0 (Binary: 00000010 >> 00000011 = 0) |
| << | Performs a bitwise left shift. Shifts the bits of left operand, left by the number of bits specified as the right operand | a << b = 16 (Binary: 00000010 << 00000011 = 00001000) |


## Assignment Operators

An assignment operator is used to assign values to a variable. This is usually combined with other operators (like arithmetic, bitwise) where the operation is performed on the operands and the result is assigned to the left operand.

Consider the following examples,  
**a = 18**. Here `=` is an assignment operator, and the result is stored in variable a.  
**a += 10**. Here `+=` is an assignment operator, and the result is stored in variable a. This is same as a = a + 10.

| Operator | Description |
| :---: | :---: |
| = | a = 5. The value 5 is assigned to the variable a |
| += | a += 5 is equivalent to a = a + 5 |
| -= | a -= 5 is equivalent to a = a - 5 |
| *= | a *= 3 is equivalent to a = a * 3 |
| /= | a /= 3 is equivalent to a = a / 3 |
| %= | a %= 3 is equivalent to a = a % 3 |
| \*\*= |	a \*\*= 3 is equivalent to a = a \*\* 3 |
| //= |	a //= 3 is equivalent to a = a // 3 |
| &= |	a &= 3 is equivalent to a = a & 3 |
| \|= |	a \|= 3 is equivalent to a = a \| 3 |
| ^= | a ^= 3 is equivalent to a = a ^ 3 |
| >>= |	a >>= 3 is equivalent to a = a >> 3 |
| <<= |	a <<= 3 is equivalent to a = a << 3 |

## Logical Operators

A logical operator is used to make a decision based on multiple conditions. The logical operators used in Python are `and`, `or` and `not`.

| Operator | Description | Usage |
| :---: | :---: | :---: |
| and | Returns True if both the operands are True | a and b |
| or | Returns True if any one of the operands are True | a or b |
| not | Returns True if the operand is False | not a |

## Membership Operators

A membership operator is used to identify membership in any sequence (lists, strings, tuples).

`in` and `not in` are membership operators. 

`in` returns True if the specified value is found in the sequence. Returns False otherwise.

`not in` returns True if the specified value is not found in the sequence. Returns False otherwise.

```py
a = [1,2,3,4,5]
  
#Is 3 in the list a?
print 3 in a # prints True 
  
#Is 12 not in list a?
print 12 not in a # prints True
  
str = "Hello World"
  
#Does the string str contain World?
print "World" in str # prints True
  
#Does the string str contain world? (note: case sensitive)
print "world" in str # prints False  

print "code" not in str # prints True
```

## Identity Operators

An identity operator is used to check if two variables share the same memory location.

`is` and `is not` are identity operators.

`is` returns True if the operands refer to the same object. Returns False otherwise.

`is not` returns True if the operands do not refer to the same object. Returns False otherwise.

Please note that two values when equal, need not imply they are identical.

```py
a = 3
b = 3  
c = 4
print a is b # prints True
print a is not b # prints False
print a is not c # prints True

x = 1
y = x
z = y
print z is 1 # prints True
print z is x # prints True

str1 = "FreeCodeCamp"
str2 = "FreeCodeCamp"

print str1 is str2 # prints True
print "Code" is str2 # prints False

a = [10,20,30]
b = [10,20,30]

print a is b # prints False (since lists are mutable in Python)  
```


