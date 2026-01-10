---
title: 'TypeError: can''t multiply sequence by non-int of type ''float'' [SOLVED]'
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-05-24T23:30:53.000Z'
originalURL: https://freecodecamp.org/news/typeerror-cant-multiply-sequence-by-non-int-of-type-float-solved
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/jake-walker-MPKQiDpMyqU-unsplash.jpg
tags:
- name: error
  slug: error
- name: error handling
  slug: error-handling
- name: Python
  slug: python
seo_title: null
seo_desc: "When coding, you're likely to encounter errors. Error messages, in most\
  \ cases, help you understand what the error is about. And understanding an error\
  \ message is one of the steps in solving an error. \nIn this article, we'll talk\
  \ about an error in Pyt..."
---

When coding, you're likely to encounter errors. Error messages, in most cases, help you understand what the error is about. And understanding an error message is one of the steps in solving an error. 

In this article, we'll talk about an error in Python – the "TypeError: can't multiply sequence by non-int of type 'float'" error. 

We'll get to understand what type of error this is, why it happens, and how to fix it with different solutions and code examples. 

## Why Does the Error "TypeError: can’t multiply sequence by non-int of type ‘float’" Occur?

Well, to understand this error, let's take a look at the error message and see what we can grab from it. The first word says **TypeError**.

So what is a TypeError? A TypeError in Python occurs when the data types involved in an operation are incompatible for said operation. So it happens when an unexpected value is seen in an operation. You'll understand this better with some code examples.

The rest of the error message lays emphasis on the word "float". Let's find out why. 

```python
print("John " * 2)
# John John  
```

In the code above, we multiplied a string by an integer (2). This resulted in the string being duplicated. 

Similarly, we'll multiply a tuple with an integer as shown below:

```python
names = ("John ", "Jane ")

print(names * 2)
# ('John ', 'Jane ', 'John ', 'Jane ')
```

We have the values in the tuple duplicated after a multiplication operation. The tuple was multiplied by 2. This is possible because we are multiplying by an integer.

Here's what happens when we try the same thing using a floating point number:

```python
print("John " * 2.0)
# TypeError: can't multiply sequence by non-int of type 'float'  
```

```python
names = ("John ", "Jane ")

print(names * 2.0)
# TypeError: can't multiply sequence by non-int of type 'float'
```

The "TypeError: can't multiply sequence by non-int of type 'float'" error is thrown at us. This is happening because we cannot multiply a string and a floating point number or a tuple and a floating point number. 

Generally, this error occurs when we perform an operation with a data type that should not be multiplied with a floating point number.

In the next section, we'll look at some of the ways of solving this error.

## How to Solve the TypeError: can’t multiply sequence by non-int of type ‘float’ Error

This section will be divided into sub-sections because there are various ways of solving this error. Each sub-section will have a code example(s).

### Solution 1 – Convert Float to Integer

To solve the "TypeError: can't multiply sequence by non-int of type 'float'" error, we can convert the float to an integer. 

Here's an example:

```python
names = ("John ", "Jane ")

print(names * int(2.0))
# ('John ', 'Jane ', 'John ', 'Jane ')
```

Now we're getting the expected result – the tuple has been duplicated. 

We passed in the floating point number into an `int()` function in order to convert it from a float to an integer. This gets rid of the error.

### Solution 2 - Convert String to Integer or Float

This solution is important when the string is of a numerical value. We may be trying to get user input and then perform a multiplication operation on it.

```python
userId = "10"

print(float(userId) * 2.0)
# 20.0

```

In order to perform the operation without getting an error, we converted the string to a float data type using the `float()` function.  

We can equally convert it to an integer using the `int()` function to get the same result. That is:

```python
userId = "10"

print(int(userId) * 2.0)
# 20.0

```

### Solution 3 – Convert User Input to Integer or Float

This solution applies to situations where we perform an operation after getting an input from a user. 

Have a look at the example below:

```python
userId = input("Enter user ID: ")
print(userId * 2.0)
# TypeError: can't multiply sequence by non-int of type 'float'
```

This throws an error after entering a number as the user ID.

To fix this, we'll convert the result of the user's input before performing the operation.

Here's how we can do that:

```python
userId = int(input("Enter user ID: "))
print(userId * 2.0)


```

Now the program should run perfectly when a user types in a number because it will be converted to an integer: `int(input("Enter user ID: "))`. 

We can do the same thing using the `float()` function which converts the user input to a floating point number.

Here's an example:

```python
userId = float(input("Enter user ID: "))
print(userId * 2.0)

```

## Conclusion

In this article, we talked about the "TypeError: can't multiply sequence by non-int of type 'float'" error in Python. 

We started by understanding what the error message means by defining a TypeError. 

We then saw some examples showing why the float data type causes this error. 

To fix the error, we looked at three different solutions with examples relating to the different situations where this error was likely to occur.

Happy coding!

