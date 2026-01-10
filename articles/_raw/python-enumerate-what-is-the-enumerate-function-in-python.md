---
title: Python enumerate() – What is the Enumerate Function in Python?
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-06-08T19:56:15.000Z'
originalURL: https://freecodecamp.org/news/python-enumerate-what-is-the-enumerate-function-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/edge2edge-media-uKlneQRwaxY-unsplash--1-.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "The enumerate() function in Python takes in a data collection as a parameter\
  \ and returns an enumerate object. \nThe enumerate object is returned in a key-value\
  \ pair format. The key is the corresponding index of each item and the value is\
  \ the items. \nI..."
---

The `enumerate()` function in Python takes in a data collection as a parameter and returns an enumerate object. 

The enumerate object is returned in a key-value pair format. The key is the corresponding index of each item and the value is the items. 

In this article, we'll see some examples of how to use the `enumerate()` function in Python.

We'll talk about the syntax and parameters, how to use `enumerate()`, and how to loop through an enumerate object. 

## What Is the Syntax of the enumerate() Function in Python?

Here is the syntax of the `enumerate()` function and its parameters:

```txt
enumerate(iterable, start)
```

The `enumerate()` function takes in two parameters: `iterable` and `start`.

* `iterable` is the data collection passed in to be returned as an enumerate object.
* `start` is the starting index for the enumerate object. The default value is 0 so if you omit this parameter, 0 will be used as the first index. 

## How to Use the `enumerate()` Function in Python

In this section, we'll look at some examples to help us understand the syntax and parameters shown in the last section. 

Note that we have to specify the type of data format (like lists, sets, and so on) the enumerate object will be stored in when returned. You'll understand this better in the examples.

### `enumerate()` Function in Python Example #1

```python
names = ["John", "Jane", "Doe"]
enumNames = enumerate(names)

print(list(enumNames))
# [(0, 'John'), (1, 'Jane'), (2, 'Doe')]
```

In the example above, we created a list called `names`. 

We then converted the `names` variable into an enumerate object: `enumerate(names)`, and stored it in a variable called `enumNames`. 

We wanted the enumerate object to be stored in a list when returned, so we did this: `list(enumNames)`. 

When printed to the console, this is what the result looked like: `[(0, 'John'), (1, 'Jane'), (2, 'Doe')]`

As you can see in the result, they are in key-value pairs. The first index is 0 which is attached to the first item in the `names` list, the second is 1 and is attached to the second item in the `names` list, and so on. 

In our example, we only used the first parameter. 

In the next example, we'll make use of both parameters so you can understand how the second parameter work. 

### `enumerate()` Function in Python Example #2

```python
names = ["John", "Jane", "Doe"]
enumNames = enumerate(names, 10)

print(list(enumNames))
# [(10, 'John'), (11, 'Jane'), (12, 'Doe')]
```

In the example above, we've added a second parameter to the `enumerate()` function: `enumerate(names, 10)`.

The second parameter is 10. This will signify the starting index for the keys (indexes) in the enumerate object. 

Here is our result: `[(10, 'John'), (11, 'Jane'), (12, 'Doe')]`

From the result, we can see that the first index is 10, the second 11, and so on.

## How to Loop Through an Enumerate Object in Python

Here's a simple example that shows how we can loop through an enumerate object in Python: 

```python
names = ["John", "Jane", "Doe"]
enumNames = enumerate(names)

for item in enumNames:
    print(item)
    
# (0, 'John')
# (1, 'Jane')
# (2, 'Doe')

```

Using a `for` loop, we iterated through the enumerate object: `for item in enumNames:`

When printed out, we got the items in the object listed out in their corresponding key-value pair order. 

We can also make use of the second parameter like we did in the last section to change the starting value of the keys. 

## Summary

In this article, we talked about the `enumerate()` function in Python. 

We started by taking a look at the function's syntax and parameters. 

We then saw some examples which helped us understand how to use the `enumerate()` function and its parameters. 

Lastly, we saw how to loop through enumerate objects in Python using the `for` loop. 

Happy coding!

