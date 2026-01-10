---
title: Python Add to Dictionary – Adding an Item to a Dict
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-03-15T00:33:07.000Z'
originalURL: https://freecodecamp.org/news/python-add-to-dictionary-adding-an-item-to-a-dict
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/dictionaary.jpg
tags:
- name: dictionary
  slug: dictionary
- name: Python
  slug: python
seo_title: null
seo_desc: "Data structures help us organize and store collections of data. Python\
  \ has built-in data structures like Lists, Sets, Tuples and Dictionaries. \nEach\
  \ of these structures have their own syntax and methods for interacting with the\
  \ data stored. \nIn this ..."
---

Data structures help us organize and store collections of data. Python has built-in data structures like Lists, Sets, Tuples and Dictionaries. 

Each of these structures have their own syntax and methods for interacting with the data stored. 

In this article, we'll talk about Dictionaries, their features, and how to add items to them. 

## How to Create a Dictionary in Python

Dictionaries are made up of key and value pairs nested in curly brackets. Here's an example of a Dictionary:

```python
devBio = {
  "name": "Ihechikara",
  "age": 120,
  "language": "JavaScript"
}
print(devBio)
# {'name': 'Ihechikara', 'age': 120, 'language': 'JavaScript'}
```

In the code above, we created a dictionary called `devBio` with information about a developer – the developer's age is quite overwhelming.

Each key in the dictionary – `name`, `age` and `language` – has a corresponding value. A comma separates each key and value pair from another. Omitting the comma throws an error your way.

Before we dive into how we can add items to our dictionaries, let's have a look at some of the features of a dictionary. This will help you easily distinguish them from other data structures in Python. 

## Features of a Dictionary

Here are some of the features of a dictionary in Python:

### Duplicate Keys Are Not Allowed

If we create a dictionary that has two or multiple identical keys in it, the last key out of them will override the rest. Here's an example: 

```python
devBio = {
  "name": "Ihechikara",
  "name": "Vincent",
  "name": "Chikara",
  "age": 120,
  "language": "JavaScript"
}
print(devBio)
# {'name': 'Chikara', 'age': 120, 'language': 'JavaScript'}
```

We created three keys with an identical key name of `name`. When we printed our dictionary to the console, the last key having a value of "Chikara" overwrote the rest.

Let's see the next feature.

### Items in a Dictionary Are Changeable

After assigning an item to a dictionary, you can change its value to something different. 

```python
devBio = {
  "name": "Ihechikara",
  "age": 120,
  "language": "JavaScript"
}

devBio["age"] = 1

print(devBio)

# {'name': 'Chikara', 'age': 120, 'language': 'JavaScript'}
```

In the example above, we reassigned a new value to `age`. This will override the initial value we assigned when the dictionary was created. 

We can also use the `update()` method to change the value of items in our dictionary. We can achieve the same result in the last example by using the `update()` method – that is: `devBio.update({"age": 1})`. 

### Items in a Dictionary Are Ordered

By being ordered, this means that the items in a dictionary maintain the order in which they were created or added. That order cannot change. 

Prior to Python 3.7, dictionaries in Python were unordered.

In the next section, we will see how we can add items to a dictionary.

## How to Add an Item to a Dictionary

The syntax for adding items to a dictionary is the same as the syntax we used when updating an item. The only difference here is that the index key will include the name of the new key to be created and its corresponding value.

Here's what the syntax looks like: `devBio[**newKey**] = **newValue**`**.**

We can also use the `update()` method to add new items to a dictionary. Here's what that would look like: `devBio.**update**({"**newKey**": **newValue**})`. 

Let's see some examples.

```python
devBio = {
  "name": "Ihechikara",
  "age": 120,
  "language": "JavaScript"
}

devBio["role"] = "Developer"

print(devBio)

# {'name': 'Ihechikara', 'age': 120, 'language': 'JavaScript', 'role': 'Developer'}
```

Above, using the index key `devBio["role"]`, we created a new key with the value of `Developer`.

In the next example, we will use the `update()` method. 

```python
devBio = {
  "name": "Ihechikara",
  "age": 120,
  "language": "JavaScript"
}

devBio.update({"role": "Developer"})

print(devBio)

# {'name': 'Ihechikara', 'age': 120, 'language': 'JavaScript', 'role': 'Developer'}
```

Above, we achieved the same result as in the last example by passing in the new key and its value into the `update()` method – that is: `devBio.update({"role": "Developer"})`.

## Conclusion

In this article, we learned what dictionaries are in Python, how to create them, and some of their features. We then saw two ways through which we can add items to our dictionaries. 

Happy coding!

