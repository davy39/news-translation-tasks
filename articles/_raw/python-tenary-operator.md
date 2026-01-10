---
title: Python Ternary Operator – Conditional Operators in Python
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-04-26T15:29:37.000Z'
originalURL: https://freecodecamp.org/news/python-tenary-operator
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/chris-ried-ieic5Tq8YMk-unsplash.jpg
tags:
- name: Conditionals
  slug: conditionals
- name: Python
  slug: python
seo_title: null
seo_desc: "You can use conditional operators in Python to execute code based on a\
  \ predefined condition(s). \nIn this article, you'll learn how to use the ternary\
  \ operator in Python. You'll see its syntax along with some practical examples.\
  \ \nWhat Is the Ternary O..."
---

You can use conditional operators in Python to execute code based on a predefined condition(s). 

In this article, you'll learn how to use the ternary operator in Python. You'll see its syntax along with some practical examples. 

## What Is the Ternary Operator Used for in Python?

The ternary operator in Python is simply a shorter way of writing an `if` and `if...else` statements. 

Here's what an `if...else` statement looks like in Python: 

```python
user_score = 90

if user_score > 50:
    print("Next level")
else:
    print("Repeat level")
```

In the code above, we created a variable `user_score` with a value of 90.

We then printed either of two statements based on a predefined condition — `if user_score > 50`. 

So if the `user_score` variable is greater than 50, we print "Next level". If it's less than `user_score`, we print "Repeat level". 

You can shorten the `if...else` statement using the ternary operator syntax. 

## Python Ternary Operator Example

In the last example, we saw how to use an `if...else` statement in Python. 

You can shorten it using the ternary operator. Here's what the syntax looks like:  

```txt
[option1] if [condition] else [option2]
```

In the syntax above, `option1` will be executed if the `condition` is true. If the condition is false then `option2` will be executed. 

In other words, the ternary operator is just a shorthand of the `if` and `if...else` statements. You can use it in just a single line of code.

Here's a more practical example:

```python
user_score = 90

print("Next level") if user_score > 50 else print("Repeat level")
```

In the code above, "Next level" will be printed out because the condition is true. 

## Summary

In this article, we talked about the ternary operator in Python. It's a shorter way of writing `if` and `if...else` statements. 

You can use ternary operators to execute code based on predefined conditions. 

Happy coding! I also write about Python on [my blog](https://ihechikara.com/).

