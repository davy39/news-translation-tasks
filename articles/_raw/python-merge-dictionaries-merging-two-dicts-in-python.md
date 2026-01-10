---
title: Python Merge Dictionaries – Merging Two Dicts in Python
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-05-11T21:51:40.000Z'
originalURL: https://freecodecamp.org/news/python-merge-dictionaries-merging-two-dicts-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/hannah-busing-Zyx1bK9mqmA-unsplash.jpg
tags:
- name: dictionary
  slug: dictionary
- name: Python
  slug: python
seo_title: null
seo_desc: "Dictionaries are one of the built-in data structures in Python. You can\
  \ use them to store data in key-value pairs. \nYou can read about the different\
  \ methods you can use to access, modify, add, and remove elements in a dictionary\
  \ here. \nIn this articl..."
---

Dictionaries are one of the built-in data structures in Python. You can use them to store data in key-value pairs. 

You can read about the different methods you can use to access, modify, add, and remove elements in a dictionary [here](https://www.freecodecamp.org/news/python-dictionary-methods-dictionaries-in-python/). 

In this article, you'll learn how to merge two dictionaries using the following:

* The `update()` method.
* The double asterisk/star operator (`**`). 
* The `chain()` method.
* The `ChainMap()` method.
* The merge operator (`|`).
* The update operator (`|=`).

## How to Merge Two Dictionaries in Python

In this section, we'll discuss the different methods you can use to merge dictionaries in Python, along with code examples.

All the examples you'll see in this article will involve the merging of two dictionaries, but you can merge as many as you want.

### How to Merge Two Dictionaries in Python Using the `update()` Method

The `update()` method is a built-in method that you can use to add data to dictionaries. 

Consider the dictionary below:

```python
devBio = {
  "name": "Ihechikara",
  "age": 500,
  "language": "Python"
}

devBio.update({"role": "Technical Writer"})

print(devBio)
# {'name': 'Ihechikara', 'age': 500, 'language': 'Python', 'role': 'Technical Writer'}
```

In the code above, we created a dictionary called `devBio` with three key and value pairs: `{'name': 'Ihechikara', 'age': 50, 'language': 'Python'}`. 

Using the `update()` method, we added another key and value pair: `devBio.update({"role": "Technical Writer"})`. 

In the same manner, we can merge two dictionaries by passing another dictionary as a parameter to the `update()` method. Here's an example:

```python
devBio = {
  "name": "Ihechikara",
  "age": 500,
  "language": "Python"
}

tools = {
  "dev environment": "JupyterLab",
  "os": "Windows",
  "visualization": "Matplotlib"
}

devBio.update(tools)

print(devBio)
# {'name': 'Ihechikara', 'age': 500, 'language': 'Python', 'dev environment': 'JupyterLab', 'os': 'Windows', 'visualization': 'Matplotlib'}
```

In the code above, we created two dictionaries — `devBio` and `tools`. 

Using the `update()` method, we merged the key and value pairs of the `tools` dictionary to the `devBio` dictionary: `devBio.update(tools)`. 

The merged dictionaries looked like this: 

```python
{
    'name': 'Ihechikara', 
    'age': 500, 
    'language': 'Python', 
    'dev environment': 'JupyterLab', 
    'os': 'Windows', 
    'visualization': 'Matplotlib'
}
```

### How to Merge Two Dictionaries in Python Using the Double Asterisk Operator (`**`)

You can use the double asterisk (also called double star) operator (`**`) to "unpack" and merge the key and value pairs of two or more dictionaries into a variable. 

Here's a code example: 

```python
devBio = {
  "name": "Ihechikara",
  "age": 500,
  "language": "Python"
}

tools = {
  "dev environment": "JupyterLab",
  "os": "Windows",
  "visualization": "Matplotlib"
}

merged_bio = { **devBio, **tools}

print(merged_bio)
# {'name': 'Ihechikara', 'age': 500, 'language': 'Python', 'dev environment': 'JupyterLab', 'os': 'Windows', 'visualization': 'Matplotlib'}
```

In the code above, we unpacked the `devBio` and `tools` dictionaries using the double asterisk operator: `{ **devBio, **tools}`. 

We then stored them in a variable called `merged_bio`. 

### How to Merge Two Dictionaries in Python Using the `chain()` Method

The `chain()` method takes multiple iterable objects as its parameter. It merges and returns the objects as one iterable object. 

You have to import the `chain()` method from the `itertools` module before using it: 

```python
from itertools import chain

devBio = {
  "name": "Ihechikara",
  "age": 500,
  "language": "Python"
}

tools = {
  "dev environment": "JupyterLab",
  "os": "Windows",
  "visualization": "Matplotlib"
}

merged_bio = dict(chain(devBio.items(), tools.items()))

print(merged_bio)
# {'name': 'Ihechikara', 'age': 500, 'language': 'Python', 'dev environment': 'JupyterLab', 'os': 'Windows', 'visualization': 'Matplotlib'}

```

In the code above, we passed the dictionaries to be merged as parameters to the `chain()` method: `chain(devBio.items(), tools.items())`. 

We used the `items()` method to access the key and value pairs of each dictionary. 

Lastly, we nested the `chain()` method and its parameters in the `dict()` method: `dict(chain(devBio.items(), tools.items()))`.

The `dict()` method can be used to create a dictionary so we used it to convert the iterable objects returned (the key and value pairs) into a dictionary, and stored them in the `merged_bio` variable.

### How to Merge Two Dictionaries in Python Using the `ChainMap()` Method

The `ChainMap()` method works the same way as the `chain()` method as regards to merging dictionaries. The main difference is that you don't need the `items()` method to access the key and value pairs of the dictionaries. 

You can import the `ChainMap()` method from the `collections` module. 

Here's how you can use the `ChainMap()` method to merger two dictionaries:

```python
from collections import ChainMap

devBio = {
  "name": "Ihechikara",
  "age": 500,
  "language": "Python"
}

tools = {
  "dev environment": "JupyterLab",
  "os": "Windows",
  "visualization": "Matplotlib"
}

merged_bio = dict(ChainMap(devBio, tools))

print(merged_bio)
# {'name': 'Ihechikara', 'age': 500, 'language': 'Python', 'dev environment': 'JupyterLab', 'os': 'Windows', 'visualization': 'Matplotlib'}
```

You can check the explanation in the last section to understand the logic in the code above. 

### How to Merge Two Dictionaries in Python Using the Merge Operator (`|`)

The merge operator (`|`) was first introduced in Python 3.9. It's a shorter and simpler syntax that you can use to merge dictionaries. 

Here's an example:

```python
from collections import ChainMap

devBio = {
  "name": "Ihechikara",
  "age": 500,
  "language": "Python"
}

tools = {
  "dev environment": "JupyterLab",
  "os": "Windows",
  "visualization": "Matplotlib"
}

merged_bio = devBio | tools

print(merged_bio)
# {'name': 'Ihechikara', 'age': 500, 'language': 'Python', 'dev environment': 'JupyterLab', 'os': 'Windows', 'visualization': 'Matplotlib'}
```

So to merge the `devBio` and `tools` dictionary, we put the `|` operator between them:  `devBio | tools`.

### How to Merge Two Dictionaries in Python Using the Update Operator (`|=`)

The update operator (`|=`) operator is another operator that was introduced in Python 3.9. 

It works just like the `update()` method. That is: 

```python
from collections import ChainMap

devBio = {
  "name": "Ihechikara",
  "age": 500,
  "language": "Python"
}

tools = {
  "dev environment": "JupyterLab",
  "os": "Windows",
  "visualization": "Matplotlib"
}

devBio |= tools

print(devBio)
# {'name': 'Ihechikara', 'age': 50, 'language': 'Python', 'dev environment': 'JupyterLab', 'os': 'Windows', 'visualization': 'Matplotlib'}
```

In the code above, we used the `|=` to mege the key and value pairs in the `tools` dictionary into the `devBio` dictionary.

## Summary

In this article, we talked about dictionaries in Python. You can use them to store data in key-value pairs. 

We saw how to merge two dictionaries in Python using:

* The `update()` method.
* The double asterisk/star operator (`**`). 
* The `chain()` method.
* The `ChainMap()` method.
* The merge operator (`|`).
* The update operator (`|=`).

Each method had its own section with code examples that showed how to use them to merge dictionaries. 

Happy coding! You can learn more about Python on [my blog](https://ihechikara.com/). 

