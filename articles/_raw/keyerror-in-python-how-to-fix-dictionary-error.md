---
title: KeyError in Python – How to Fix Dictionary Error
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-07-07T19:33:31.000Z'
originalURL: https://freecodecamp.org/news/keyerror-in-python-how-to-fix-dictionary-error
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/brett-jordan-XWar9MbNGUY-unsplash.jpg
tags:
- name: error handling
  slug: error-handling
- name: Python
  slug: python
seo_title: null
seo_desc: "When working with dictionaries in Python, a KeyError gets raised when you\
  \ try to access an item that doesn't exist in a Python dictionary.\nHere's a Python\
  \ dictionary called student:\nstudent = {\n  \"name\": \"John\",\n  \"course\":\
  \ \"Python\",\n}\n\nIn the dictio..."
---

When working with dictionaries in Python, a KeyError gets raised when you try to access an item that doesn't exist in a Python dictionary.

Here's a Python dictionary called `student`:

```python
student = {
  "name": "John",
  "course": "Python",
}
```

In the dictionary above, you can access the name "John" by referencing its key – `name`. Here's how:

```python
print(student["name"])
# John
```

But when you try to access a key that doesn't exist, you get a KeyError raised. That is:

```python
student = {
  "name": "John",
  "course": "Python",
}

print(student["age"])
# ...KeyError: 'age'
```

This is simple to fix when you're the one writing/testing the code – you can either check for spelling errors or use a key you know exists in the dictionary.

But in programs where you require user input to retrieve a particular item from a dictionary, the user may not know all the items that exist in the dictionary. 

In this article, you'll see how to fix the KeyError in Python dictionaries. 

We'll talk about methods you can use to check if an item exists in a dictionary before executing a program, and what to do when the item cannot be found.

## How to Fix the Dictionary KeyError in Python

The two methods we'll talk about for fixing the KeyError exception in Python are:

* The `in` keyword.
* The `try except` block.

Let's get started.

### How to Fix the KeyError in Python Using the `in` Keyword

We can use the `in` keyword to check if an item exists in a dictionary. 

Using an `if...else` statement, we return the item if it exists or return a message to the user to notify them that the item could not be found. 

Here's an example:

```python
student = {
  "name": "John",
  "course": "Python",
  "age": 20
}

getStudentInfo = input("What info about the student do you want? ")

if getStudentInfo in student:
    print(f"The value for your request is {student[getStudentInfo]}")
else:
	print(f"There is no parameter with the '{getStudentInfo}' key. Try inputing name, course, or age.")
```

Let's try to understand the code above by breaking it down. 

We first created a dictionary called `student` which had three items/keys – `name`, `course`, and `age`:

```python
student = {
  "name": "John",
  "course": "Python",
  "age": 20
}

```

Next, we created an `input()` function called `getStudentInfo`: `getStudentInfo = input("What info about the student do you want? ")`.  We'll use the value from the `input()` function as a key to get items from the dictionary.

We then created an `if...else` statement to check if the value from the `input()` function matches any key in the dictionary:

```python
if getStudentInfo in student:
    print(f"The value for your request is {student[getStudentInfo]}")
else:
	print(f"There is no parameter with the '{getStudentInfo}' key. Try inputing name, course, or age.")
```

From the `if...else` statement above, if the value from the `input()` function exists as an item in the dictionary, `print(f"The value for your request is {student[getStudentInfo]}")` will run. `student[getStudentInfo]` denotes the `student` dictionary with the value gotten from the `input()` function acting as a key. 

If the value from the `input()` function doesn't exist, then `print(f"There is no parameter with the '{getStudentInfo}' key. Try inputing name, course, or age.")` will run telling the user that their input is wrong, with suggestions of the possible keys they can use. 

Go on and run the code – input both correct and incorrect keys. This will help validate the explanations above.

### How to Fix the KeyError in Python Using a `try except` Keyword

In a `try except` block, the `try` block checks for errors while the `except` block handles any error found. 

Let's see an example. 

```python
student = {
  "name": "John",
  "course": "Python",
  "age": 20
}

getStudentInfo = input("What info about the student do you want? ")

try:
    print(f"The value for your request is {student[getStudentInfo]}")
except KeyError:
    print(f"There is no parameter with the '{getStudentInfo}' key. Try inputing name, course, or age.")
```

Just like we did in the last section, we created the dictionary and an `input()` function. 

We also created different messages for whatever result we get from the `input()` function. 

If there are no errors, only the code in the `try` block will be executed – this will return the value of the key from the user's input.

If an error is found, the program will fall back to the `except` block which tells the user the key doesn't exist while suggesting possible keys to use. 

## Summary

In this article, we talked about the KeyError in Python. This error is raised when we try to access an item that doesn't exist in a dictionary in Python. 

We saw two methods we can use to fix the problem. 

We first saw how we can use the `in` keyword to check if an item exists before executing the code. 

Lastly, we used the `try except` block to create two code blocks – the `try` block runs successfully if the item exists while the `except` runs if the item doesn't exist. 

Happy coding!

