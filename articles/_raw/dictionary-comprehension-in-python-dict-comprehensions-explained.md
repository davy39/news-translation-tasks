---
title: Dictionary Comprehension in Python – Dict Comprehensions Explained
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-09-16T18:47:35.000Z'
originalURL: https://freecodecamp.org/news/dictionary-comprehension-in-python-dict-comprehensions-explained
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/element5-digital-OyCl7Y4y0Bk-unsplash.jpg
tags:
- name: dictionary
  slug: dictionary
- name: Python
  slug: python
seo_title: null
seo_desc: "You can use Dictionaries in Python to store data in key and value pairs.\
  \ \nAnd you can use dictionary comprehension to create a new dictionary from an\
  \ already existing one. \nWhen creating a new dictionary using dictionary comprehension,\
  \ you can perfor..."
---

You can use [Dictionaries](https://www.freecodecamp.org/news/python-add-to-dictionary-adding-an-item-to-a-dict/) in Python to store data in key and value pairs. 

And you can use dictionary comprehension to create a new dictionary from an already existing one. 

When creating a new dictionary using dictionary comprehension, you can perform various operations using expressions to determine the data (key and/or value) that will be stored in the new dictionary. 

In this article, you'll learn how to create dictionaries in Python using dictionary comprehension. You'll also see various expressions that you can use to modify the data to be stored in the new dictionary. 

Let's get started!

## How to Use Dictionary Comprehension in Python

Before we take a look at some examples, here's what the syntax for dictionary comprehension looks like:

```txt
new_dictionary = {key: value for (key,value) in iterable}
```

In the syntax above, `key` and `value` represent the key and value in the initial dictionary. Whatever operation you carry out on them determines the keys/values in the new dictionary — you'll understand this better soon with some examples. 

The `key` and `value` in parenthesis – `(key, value)` – are still the same as the ones we mentioned above. In this case, they are used in a `for` loop. 

So whatever operation you perform on `key` and `value` will be used by the loop to apply that operation on every item the operation is associated with in the initial dictionary.

`iterable`, in the syntax, denotes an iterable object. In our case, it denotes the initial dictionary.

Let's look at some examples to help you understand the explanations above.

```python
items_in_cm = {'pen': 40, 'book': 50, 'keyboard': 60}
```

In the code above, we created a dictionary with three items. The keys are the names of the items while the values are the length of these items in centimeters. 

Using a dictionary comprehension, we'll create a new dictionary with the length of each item in meters. 

Here's how it works:

```python
items_in_cm = {'pen': 40, 'book': 50, 'keyboard': 60}

items_in_meters = {key: value/100 for (key, value) in items_in_cm.items()}

print(items_in_meters)
# {'pen': 0.4, 'book': 0.5, 'keyboard': 0.6}
```

What to look out for is in the second line above: `items_in_meters = {key: value/100 for (key, value) in items_in_cm.items()}`

Let's break it down.

The first part has this: `key: value/100`. This implies that every `value` in the dictionary is to be divided by 100. 

But the dictionary comprehension is yet to understand where to apply the command above. 

This leads us to the second part: `for (key, value) in items_in_cm.items()`. This part the code has a `for` loop that takes two parameters — `key` and `value`. 

So this will run through every key and value in the `items_in_cm` dictionary and divide each value by 100. 

We are able to access the items in that dictionary using the `items()` method which returns every key and value pair in a dictionary. 

Printing the new dictionary (`items_in_meters`), we have this: `{'pen': 0.4, 'book': 0.5, 'keyboard': 0.6}`. Every value in the new dictionary has been divided by 100. 

You'll notice that we only altered the data in the dictionary's values. You can also modify the keys. Here's an example: 

```python
items_in_cm = {'pen': 40, 'book': 50, 'keyboard': 60}

items_in_meters = {key + ' in meters': value/100 for (key, value) in items_in_cm.items()}

print(items_in_meters)
# {'pen in meters': 0.4, 'book in meters': 0.5, 'keyboard in meters': 0.6}

```

In the example above, we added a string to every key in the dictionary comprehension: `key + ' in meters'`. 

## How to Use Conditional Statements in Dictionary Comprehension in Python

In this section and the next, you'll learn about other expressions that you can use to modify the items stored in dictionaries created using dictionary comprehension. 

We'll start with conditional statements.

```python
developers = {'Jane': 'Python', 'Jade': 'JavaScript', 'John': 'Python', 'Doe': 'JavaScript'}

python_developers = {key: value for (key, value) in developers.items() if value == 'Python'}

print(python_developers)
# {'Jane': 'Python', 'John': 'Python'}

```

In the example above, we created a dictionary called `developers` which stores a list of developers with their favorite languages: `{'Jane': 'Python', 'Jade': 'JavaScript', 'John': 'Python', 'Doe': 'JavaScript'}`.

In the dictionary comprehension, we added an expression at the end: `if value == 'Python'`. This will scan through and return all the items whose `value` has a value of 'Python'. 

When printed out, we have this in the console: `{'Jane': 'Python', 'John': 'Python'}`. 

We can also use an `if/else` statement in dictionary comprehensions. Here's an example:

```python
random_items = {'monitor': 100, 'pen': 40, 'keyboard': 60, 'pencil': 30}

items_length_check = {key: ('above 50' if value > 50 else 'below 50') for (key, value) in random_items.items()}

print(items_length_check)
# {'monitor': 'above 50', 'pen': 'below 50', 'keyboard': 'above 50', 'pencil': 'below 50'}
```

Using an `if/else` statement above, we modified the values in the new dictionary. The `value` for each item will be "above 50" if the value in the initial dictionary is above 50 and "below 50" if less than 50.

The code in the dictionary comprehension is starting to look bulky. We'll clean it up in the next section using a function. 

## How to Use a Function in Dictionary Comprehension in Python

When using dictionary comprehension, you can use functions to replace/extract logic that should go into the curly brackets of the dictionary comprehension. This help keep the code neat and readable. 

```python
random_items = {'monitor': 100, 'pen': 40, 'keyboard': 60, 'pencil': 30}

def check_length(value):
    if value >50:
        return 'above 50'
    else:
        return 'below 50'

items_length_check = {key: check_length(value) for (key, value) in random_items.items()}


print(items_length_check)
# {'monitor': 'above 50', 'pen': 'below 50', 'keyboard': 'above 50', 'pencil': 'below 50'}

```

The example above is similar to the one in the last section. 

We made one major change — extracting the logic in the dictionary comprehension and putting it in a function. That is:

```python
def check_length(value):
    if value >50:
        return 'above 50'
    else:
        return 'below 50'
```

We then put the function name in the dictionary comprehension: `items_length_check = {key: check_length(value) for (key, value) in random_items.items()}`.

When the code in the dictionary comprehension runs, the function is fired. 

## Summary

In this article, we talked about dictionary comprehension in Python. You can use it to create new dictionaries from existing ones.

We saw the syntax and how to use dictionary comprehension.

We also saw examples that showed how to use conditional statements and functions when working with dictionary comprehension. 

Happy coding!

