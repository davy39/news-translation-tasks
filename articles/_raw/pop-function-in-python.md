---
title: Pop Function in Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-29T23:35:00.000Z'
originalURL: https://freecodecamp.org/news/pop-function-in-python
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d49740569d1a4ca36ed.jpg
tags:
- name: Python
  slug: python
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'What is the pop function?

  The method pop() removes and returns the last element from a list. There is an optional
  parameter which is the index of the element to be removed from the list. If no index
  is specified, a.pop() removes and returns the last ...'
---

# What is the pop function?

The method pop() removes and returns the last element from a list. There is an optional parameter which is the index of the element to be removed from the list. If no index is specified, a.pop() removes and returns the last item in the list. If the index passed to the pop() method is not in the range, it throws IndexError: pop index out of range exception.

### Example Usage

```py
cities = ['New York', 'Dallas', 'San Antonio', 'Houston', 'San Francisco'];

print "City popped is : ", cities.pop()
print "City at index 2 is  : ", cities.pop(2)
```

#### **Output**

```text
City popped is :  San Francisco
City at index 2 is  :  San Antonio
```

### Basic Stack Functionality

The `pop()` method is often used in conjunction with `append()` to implement basic stack functionality in a Python application.

```py
stack = []

for i in range(5):
    stack.append(i)

while len(stack):
    print(stack.pop())
```

#### **More Information:**

The official documentation for `pop()` can be found [here](https://docs.python.org/3.6/tutorial/datastructures.html)

