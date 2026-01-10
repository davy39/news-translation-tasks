---
title: 'Typeerror: int object is not callable – How to Fix in Python'
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-07-18T14:10:48.000Z'
originalURL: https://freecodecamp.org/news/typeerror-int-object-is-not-callable-how-to-fix-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/typeerror.png
tags:
- name: error
  slug: error
- name: Math
  slug: math
- name: Python
  slug: python
seo_title: null
seo_desc: "In Python, a “Typeerror” occurs when you use different data types in an\
  \ operation. \nFor example, if you attempt to divide an integer (number) by a string,\
  \ it leads to a typeerror because an integer data type is not the same as a string.\
  \ \nOne of those..."
---

In Python, a “Typeerror” occurs when you use different data types in an operation. 

For example, if you attempt to divide an integer (number) by a string, it leads to a `typeerror` because an integer data type is not the same as a string. 

One of those type errors is the “int object is not callable” error.

The “int object is not callable” error occurs when you declare a variable and name it with a built-in function name such as `int()`, `sum()`, `max()`, and others.

The error also occurs when you don’t specify an arithmetic operator while performing a mathematical operation.

In this article, I will show you how the error occurs and what you can do to fix it.

## How to Fix ` Typeerror: int object is not callable` in Built-in Function Names
If you use a built-in function name as a variable and call it as a function, you’ll get the “int object is not callable” error.

For instance, the code below attempts to calculate the total ages of some kids with the built-in `sum()` function of Python. The code resulted in an error because the same `sum` has already been used as a variable name:
```py
kid_ages = [2, 7, 5, 6, 3]

sum = 0
sum = sum(kid_ages)
print(sum)
```
Another example below shows how I tried to get the oldest within those kids with the `max()` function, but I had declared a `max` variable already:
```py
kid_ages = [2, 7, 5, 6, 3]

max = 0
max = max(kid_ages)
print(max)
```

Both code examples led to this error in the terminal:
![error](https://www.freecodecamp.org/news/content/images/2022/07/error.png)

To fix the issue, you need to change the name of the variable you named as a built-in function so the code can run successfully:
```py
kid_ages = [2, 7, 5, 6, 3]

sum_of_ages = 0
sum = sum(kid_ages)
print(sum)

# Output: 23
```
```py
kid_ages = [2, 7, 5, 6, 3]

max_of_ages = 0
max = max(kid_ages)
print(max)

# Output: 7
```

If you get rid of the custom variables, your code will still run as expected:
```py
kid_ages = [2, 7, 5, 6, 3]

sum = sum(kid_ages)
print(sum)

# Output: 23
```

```py
kid_ages = [2, 7, 5, 6, 3]

max = max(kid_ages)
print(max)

# Output: 7
```

## How to Fix `Typeerror: int object is not callable` in Mathematical Calculations

In Mathematics, if you do something like 4(2+3), you’ll get the right answer which is 20. But in Python, this would lead to the `Typeerror: int object is not callable` error.
![ss2-2](https://www.freecodecamp.org/news/content/images/2022/07/ss2-2.png)

To fix this error, you need to let Python know you want to multiply the number outside the parentheses with the sum of the numbers inside the parentheses. 

To do this, you do this by specifying a multiplication sign (*) before the opening parenthesis:
```py
print(4*(2+3))

#Output: 20
```

Python allows you to specify any arithmetic sign before the opening parenthesis. 

So, you can perform other calculations there too:
```py
print(4+(2+3))

# Output: 9
```
```py
print(4-(2+3))

# Output: -1
```

```py
print(4/(2+3))

# Output: 0.8
```

## Final Thoughts

The `Typeerror: int object is not callable` is a beginner error in Python you can avoid in a straightforward way.

As shown in this article, you can avoid the error by not using a built-in function name as a variable identifier and specifying arithmetic signs where necessary.

Thank you for reading.


