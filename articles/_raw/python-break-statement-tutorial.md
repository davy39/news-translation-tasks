---
title: Python Break Statement – How to Break Out of a For Loop in Python
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2024-04-10T16:51:21.985Z'
originalURL: https://freecodecamp.org/news/python-break-statement-tutorial
coverImage: https://cdn.hashnode.com/res/hashnode/image/stock/unsplash/ieic5Tq8YMk/upload/1e00a0a8acc5c22dea9a4910bffecbb1.jpeg
tags:
- name: Python
  slug: python
- name: Loops
  slug: loops
seo_title: null
seo_desc: 'You can use loops in Python to execute code logic repeatedly until a specified
  condition is met.

  Python provides some built-in control statements that let you change the behavior
  of a loop. Some of these control statements include continue, break, pa...'
---

You can use loops in Python to execute code logic repeatedly until a specified condition is met.

Python provides some built-in control statements that let you change the behavior of a loop. Some of these control statements include `continue`, `break`, `pass`, and `else`.

In this article, you'll learn how to terminate the current loop or a switch statement using the `break` statement.

## How to Use the `break` Statement in a Python `for` Loop

Consider the Python list below:

```python
usernames = ["Jade", "John", "Jane", "Doe"]
```

You can use a `for` loop to iterate through and print the elements of the `usernames` list:

```python
usernames = ["Jade", "John", "Jane", "Doe"]

for i in usernames:
    print(i)
# Jade
# John
# Jane
# Doe
```

But what if you want to stop the loop when a particular username is found? You can do this using the `break` statement.

Here's an example:

```python
usernames = ["Jade", "John", "Jane", "Doe"]

for i in usernames:
    print(i)
    if i == "John":
        break
# Jade
# John
```

In the code above, we created an `if` statement that checks whether the current value of `i` is "John": `if i == "John"`.

In the body of the `if` statement, we used the `break` statement. So the loop will stop when it finds an element in the list with the value of "John".

So instead of printing the whole list ("Jade", "John", "Jane", "Doe"), "Jade" and "John" were printed because the loop stopped immediately after it found "John".

## How to Use the `break` Statement in a Python `while` Loop

You can terminate a `while` loop using the `break` statement:

```python
usernames = ["Jade", "John", "Jane", "Doe"]

i = 0
while i < len(usernames):
    print(usernames[i])
    if usernames[i] == "John":
        break
    i += 1
```

Just like we did in the `for` loop example, we created a `usernames` list with four elements: `["Jade", "John", "Jane", "Doe"]`.

Using an `if` statement in the `while` loop, we checked when the current loop was at the index with a value "John". When that happens, the loop is terminated.

Once again, "Jade" and "John" were printed because the loop stops when "John" is found.

## Conclusion

In this article, you learned to use the `break` statement in Python. You can use it to terminate the current loop when a condition is met.

From the above examples, you learned how to use the `break` statement to terminate `for` and `while` loops in Python.

Happy coding!
