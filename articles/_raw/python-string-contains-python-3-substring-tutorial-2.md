---
title: Python String Contains – Python 3 Substring Tutorial
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-11-17T16:47:04.000Z'
originalURL: https://freecodecamp.org/news/python-string-contains-python-3-substring-tutorial-2
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/pexels-kevin-ku-577585.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'In this article, you will learn how to check if a string contains a substring
  in Python.

  Checking if a string contains a substring comes in handy when you have received
  user input and want your program to behave a certain way – or even when you want
  ...'
---

In this article, you will learn how to check if a string contains a substring in Python.

Checking if a string contains a substring comes in handy when you have received user input and want your program to behave a certain way – or even when you want to replace one word with another. 

Python offers many ways to confirm whether a substring is present in a string, and in this quick guide, you will see a few of them in action.

Here is what we will cover:

1. [How to check if a string contains a substring using the `in` operator](#in-operator)
    1. [How to perform a case insensitive search when using the `in` operator](#case-insensitive)
2. [How to check if a string contains a substring using the `.index()` method](#index-method)
3. [How to check if a string contains a substring using the `.find()` method](#find-method)

## How to Check if a String Contains a Substring Using the `in` Operator in Python <a name="in-operator"></a>

Using the `in` operator is one of the clearest, most readable, and most Pythonic ways to confirm whether a substring is present in a string.

Therefore, the `in` operator is the preferred way of checking that a string contains a substring.

The general syntax for using the `in` operator is the following:

```
substring in string
```

The `in` operator returns a Boolean value. A Boolean value is either `True` or `False`. 

The `in` operator returns `True` if the substring is present in the string and `False` if the substring is not present.

```python
>>> learn_coding = "You can learn to code for free!"
>>> "free" in learn_coding
True
```

In the example above, I entered Python's interactive console, also known as the Python interpreter or Python shell.

You can enter it after installing Python locally, opening your terminal, and typing `Python` or `Python3` depending on your system.

I store the phrase `You can learn to code for free!` in a variable called `learn_coding`.

Then, I check to see if the substring `free` is present in the phrase `You can learn to code for free!` using the `in` operator. 

Since the substring is present, `in` returns `True`.

It is important to note that the `in` operator only checks if the substring is present and exists in the string. It doesn't check the position of the substring, nor does it give any information on how many times the substring appears in the string.

As a side note, you can also choose to check if a substring is **not** present in a string by using the `not in` operator:

```python
>>> learn_coding = "You can learn to code for free!"
>>> "free" not in learn_coding
False
```

This time, I use the `not in` operator to check whether the substring `free` is **not** present in the string `You can learn to code for free!`. Since `free` is present, the `not in` operator returns `False`.

Now, let's go back to the `in` operator. 

You can use the `in` operator to control the behavior of your program by setting conditions.

Let's take the following example:

```python
user_input = input("Do you need to pay to learn to code?: ")

if "yes" in user_input:
  print("Wrong! You can learn to code for free!!")
```

In the example above, I am asking a user for input and storing their answer in a variable named `user_input`.

Then, I use a conditional statement paired with the `in` operator to make a decision (if you need a refresher on conditional statements in Python, read [this article](https://www.freecodecamp.org/news/python-else-if-statement-example/)).

If their answer contains the substring `yes`, then `in` returns the phrase `Wrong! You can learn to code for free` because the code in the `if` statement executes:

```
Do you need to pay to learn to code?: yes, I think you do
Wrong! You can learn to code for free!!
```

In the example above, the string the user entered, `yes, I think you do`, contains the substring `yes` and the code in the `if` block runs.

What happens when the user enters `Yes, I think you do` with a capital `Y` instead of a lowercase one?

```
Do you need to pay to learn to code?: Yes, I think you do
```

As you see, nothing happens! The program has no output because Python strings are case-sensitive.

You could write an `else` statement to solve this. However, you could instead account for case sensitivity when checking to see if a substring is present in a string.

Let's see how to do that in the following section.

### How to Perform a Case Insensitive Search When Using the `in` Operator in Python <a name="case-insensitive"></a>

In the section above, you saw that when searching if a substring is present in a string, the search is case-sensitive.

So, how can you make the search case insensitive?

You can convert the whole user input into lowercase by using the `.lower()` method:

```python
user_input = input("Do you need to pay to learn to code?: ").lower()

if "yes" in user_input:
  print("Wrong! You can learn to code for free!!")
```

Now, when the user enters `Yes` with a capital `Y`, the code in the `if` statement runs, even if you were searching for the substring `yes` with a lowercase `y`. This is because you converted the user input text to all lowercase letters.

## How to Check if a String Contains a Substring Using the `.index()` Method in Python <a name="index-method"></a>

You can use the `.index()` Python method to find the starting index number of the first character of the first occurrence of a substring inside a string:

```python
learn_coding = "You can learn to code for free! Yes, for free!"
substring = "free"

print(learn_coding.index(substring))

# output

# 26
```

In the example above, I stored the string `You can learn to code for free! Yes, for free!` in a variable named `learn_coding`.

I also stored the substring `free` in the variable `substring`.

Then, I called the `.index()` method on the string and passed the substring as the argument to find where the first `free` substring occurrence appears. (The string stored in `learn_coding` contains two instances of the substring `free`).

Finally, I printed the result.

If the substring is **not** present in the string, then a `ValueError: substring not found` error gets raised:

```python
learn_coding = "You can learn to code for free! Yes, for free!"
substring = "paid"

print(learn_coding.index(substring))

# output

# Traceback (most recent call last):
#  File "main.py", line 4, in <module>
#    print(learn_coding.index(substring))
# ValueError: substring not found
```

The `.index()` method comes in handy when you want to know the location of the substring you are searching for and where the substring occurs and starts in the string.

The `in` operator lets you know whether the substring exists in the string, whereas the `.index()` method also tells you *where* it exists.

That said, `.index()` is not ideal when Python can't find the substring in the string because it raises a `ValueError` error.

If you want to avoid that error from being raised when searching for a string, and you don't want to use the `in` operator, you can use the Python `find()` method instead.

## How to Check if a String Contains a Substring Using the `.find()` Method in Python <a name="find-method"></a>

The `.find()` method works similarly to the `.index()`  method - it checks to see if a string contains a substring, and if the substring is present, it returns its starting index.

```python
learn_coding = "You can learn to code for free! Yes, for free!"
substring = "free"

print(learn_coding.find(substring))

# output

# 26
```

The difference between the `.find()` method and the `.index()` method is that with `.find()`, you don't have to worry when it comes it handling exceptions, in comparison to `.index()`.

As you saw in the section above, when the string doesn't contain the substring, `index()` raises an error.

On the other hand, when you are using the `.find()` method and the string doesn't contain the substring you are searching for, `.find()` returns `-1` without raising an exception:

```python
learn_coding = "You can learn to code for free! Yes, for free!"
substring = "paid"

print(learn_coding.find(substring))

# output

# -1
```

## Conclusion

Hopefully, this article helped you understand how to check if a string contains a substring in Python.

To learn more about the Python programming language, check out [freeCodeCamp's Python certification](https://www.freecodecamp.org/learn/scientific-computing-with-python/).

You'll start from the basics and learn in an interactive and beginner-friendly way. You'll also build five projects at the end to put into practice and help reinforce what you've learned.

Thank you for reading, and happy coding!



