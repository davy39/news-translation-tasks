---
title: Python Not Equal – Does Not Equal Operator Tutorial
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-01-07T18:16:14.000Z'
originalURL: https://freecodecamp.org/news/python-not-equal-how-to-use-the-does-not-equal-operator
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/does-not-equal-python-operator.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: Python
  slug: python
seo_title: null
seo_desc: "When you're learning the basics of most programming languages, you are\
  \ bound to come across operators. \nIn this tutorial, we will talk about the not\
  \ equal operator in Python and also see a few examples of how it works. \nOperators\
  \ and Operands in Pyth..."
---

When you're learning the basics of most programming languages, you are bound to come across operators. 

In this tutorial, we will talk about the **not equal** operator in Python and also see a few examples of how it works. 

## Operators and Operands in Python

Before talking about the not equal operator, let's understand what operators and operands are in general.

Operators are symbols that denote a certain type of action or process. They carry out specific operations on certain values or variables. These values or variables are known as the operands of the the operator so the operator performs its operation on them and returns a value.

Here are a few examples of operators and how they interact with operands:

#### Addition operator (`+`)

```py
a = 10
b = 10

print(a + b)

# returns 20 
```

The operator here is the `+` symbol which adds the value of `a` and `b` which are the operands. 

#### Multiplication operator (`*`)

```py
c = 10
d = 10

print(a * b)

# returns 100
```

Similar to the last example, `*` is the operator while `c` and `d` are the operands.

#### Not equal operator (`!=`)

```py
firstNumber = 10
secondNumber = 20

print(firstNumber != secondNumber)

# returns True
```

Again, the operator is the `!=` symbol and the operands are `firstNumber` and `secondNumber`.

There are many other operators in Python which are divided into groups but in this tutorial we will be focusing on the not equal operator (`!=`).

## Not Equal Operator in Python

The not equal operator is a relational or comparison operator that compares two or more values (operands). It returns either true or false depending on the result of the operation. 

If the values compared are equal, then a value of `true` is returned. If the values compared are not equal, then a value of `false` is returned.

`!=` is the symbol we use for the not equal operator.

Let's see a few examples of how it works.

## How to compare numeric values using the `!=` operator in Python

Here, we will define two variables and then compare their values.

```py
a = 600
b = 300

print(a != b)

# True

```

As expected, the above operation returns `true` because the value of `a` is not equal to the value of `b`. If you still find this hard to grasp, then I will represent the code above using plain English to rewrite each line below:

```txt
a is equal to 600
b is equal to 300

print(the value of a does not equal the value of b)

# True, the value of a is not equal to the value of b
```

That should probably simplify it.

Next, we will compare more than two values.

```py
a = 600
b = 300
c = 300

print(a != b & c)

# True
```

If you were expecting a value of `false` then you were probably trying to add some of the values during the comparison. 

To make this simpler to understand, the operator is only going look at the values of each operand and then compare all of them without adding one operand to the other.

Imagine `a`, `b` and `c` as triplets and each baby's face was represented by a number. Now the `!=` operator is saying, "I have made my observations and concluded that the three babies are not identical facially" and that is completely `True`.

When all the operands are the same and the `!=` is used, then the value returned will be false. That is:

```py
a = 600
b = 600
c = 600

print(a != b & c)

# False
```

Here, the triplets all have the same face but `!=` is saying, "All the babies do not have the same face" and that is false because their faces, represented by numbers, are the same – 600.

## How to compare lists in Python using the `!=` operator

In the previous section, we compared the values of numbers. In this section, we will be comparing lists. Lists are used to store more than one item in a single variable. 

```py
a = [2, 3]
b = [2, 3]

print(a != b)

# False
```

Just like we saw in the previous section, the value is `False` because the two lists are the same. It would be `True` if both operands were not the same.

To further grasp the idea of `True` or `False` being returned when using the `!=` operator, you should always have in mind that the value will be `True` if the operands are not the same and `False` if the operands are the same. 

The `!=` operator can also be used to compare Strings, Dictionaries, Tuples and Sets.

## How to use an `if` statement with the `!=` operator in Python

In some cases, you might prefer to carry out a certain command only after evaluating two variables. Consider the example below:

```py
a = 21
b = 10

if ( a != b ):
   print ("True. a is not equal to b")
else:
   print ("False. a is equal to b")
   
   # True. a is not equal to b
```

The `if` statement checks whether the values of the operands are not the same and then prints a message based on the value returned. 

This is a very basic example. As you advance as a Python developer, you'll find yourself crafting more complex (but not necessarily hard) logic to execute various commands.

## Conclusion

This article served as an introduction to using the not equal (`!=`) operator in Python and highlighted a few examples to help you understand its application. 

If you are a beginner interested in learning Python, freeCodeCamp has a [Scientific Computing with Python](https://www.freecodecamp.org/learn/scientific-computing-with-python/) certificate which is a good place to start.

Happy coding!

