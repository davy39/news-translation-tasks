---
title: Create a List in Python – Lists in Python Syntax
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-03-23T20:32:31.000Z'
originalURL: https://freecodecamp.org/news/create-a-list-in-python-lists-in-python-syntax
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/list.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'Lists are one of the core data structures in Python. We use them for storing
  any data type, whether it''s an integer, string, boolean, or even an object.

  Because one list can store multiple types of data, lists are one of the most powerful
  and widely ...'
---

Lists are one of the core data structures in Python. We use them for storing any data type, whether it's an integer, string, boolean, or even an object.

Because one list can store multiple types of data, lists are one of the most powerful and widely used tools for storing data in Python.

One of the notable features of lists is mutability. You can change a list after declaring it and build upon it.

In this article, you will not just learn how to declare a list – I will also show you several methods you can use to manipulate lists so you can get confident using them.

## Basic Syntax of Lists in Python
To create a list in Python, declare a name for the list and place the individual data separated by commas inside square brackets:

```py
listName = [value1, value2, value3, value4]
```

Remember the values you put in the square brackets can be of any data type. 

It could be strings:
```py
langs = ["HTML", "CSS", "Python", "JavaScript"]
```

It could be integers:
```py
intList = [1, 5, 78, 76, 9, 0]
```

It could be a boolean:
```py
boolList = [True, False]
```

It could be a mixture of different data types, including floats:
```py
mixedList = [23, "JavaScript", True, 34.9, 19]
```

You can even duplicate the data in a list and things would still work fine:
```py
duplicateList = [3, "Python", "Python", "JavaScript"]
print(duplicateList) 
# Output: [3, 'Python', 'Python', 'JavaScript']
```

## How to Access the Elements in a List

To access the elements in a list, you can use the index operator (`[]`). Lists are zero-indexed, so we use 0 to get the first element, 1 for the second element, and so on.

```py
langs = ["HTML", "CSS", "Python", "JavaScript", "C++", "Java", "Elixir", "R"]
firstElement = langs[0]
secondElement = langs[1]
thirdElement = langs[2]
fourthElement = langs[3]

print(firstElement) # HTML
print(secondElement) # CSS
print(thirdElement) # Python
print(fourthElement) # JavaScript

# Get the last element with negative indexing
lastElement = langs[-1]
print(lastElement) # R
```

## Different Methods you can Use to Work with Lists

You can use the `len()` method to get the length of the list:
```py
langs = ["HTML", "CSS", "Python", "JavaScript", "C++", "Java", "Elixir", "R"]
print(len(langs))
# Output: 8
```

You can add to the list by using the `append()` method:
```py
langs = ["HTML", "CSS", "Python", "JavaScript", "C++", "Java", "Elixir", "R"]
langs.append("C#")
print(langs)
```

**N.B.:** You can only append one element at a time with the `append()` method, and the element gets pushed to the end. 

Keep reading and I will show you how to add multiple elements to the list, and how you can add something to your desired position (index) in the list.

You can add to the position you like in the list by using the `insert()` method:
```py
langs = ["HTML", "CSS", "Python", "JavaScript", "C++", "Java", "Elixir", "R"]
# Insert Golang at position 4
langs.insert(4, "Golang")

print(langs)
# OUtput: ['HTML', 'CSS', 'Python', 'JavaScript', 'Golang', 'C++', 'Java', 'Elixir', 'R']
```

Remember that lists are zero-indexed, so counting starts from 0 and not 1. Golang was not inserted at position 5, it was inserted at position 4.

You can add multiple elements to the list by using the `extend()` method:
```py
langs = ["HTML", "CSS", "Python", "JavaScript", "C++", "Java", "Elixir", "R"]
langs.extend(["Golang", "F#", "COBOL"])

print(langs)
# Output: ['HTML', 'CSS', 'Python', 'JavaScript', 'C++', 'Java', 'Elixir', 'R', 'Golang', 'F#', 'COBOL']
```

You can remove an element from the list by using the `remove()` method:

```py
langs = ["HTML", "CSS", "Python", "JavaScript", "C++", "Java", "Elixir", "R"]
langs.extend(["Golang", "F#", "COBOL"])

# Remove HTML
langs.remove("HTML")

print(langs)
# Output: ['CSS', 'Python', 'JavaScript', 'C++', 'Java', 'Elixir', 'R', 'Golang', 'F#', 'COBOL']
```

You can remove an element from the end of the list by using the `pop()` method:

```py
langs = ["HTML", "CSS", "Python", "JavaScript", "C++", "Java", "Elixir", "R"]
# Remove R
langs.pop()

print(langs)
# Output: ['HTML', 'CSS', 'Python', 'JavaScript', 'C++', 'Java', 'Elixir']
```

You can also remove an element from certain position in the list by using the `pop()` method:
```py
langs = ["HTML", "CSS", "Python", "JavaScript", "C++", "Java", "Elixir", "R"]
# Removes JavaScript
langs.pop(3)

print(langs)
# Output: ['HTML', 'CSS', 'Python', 'C++', 'Java', 'Elixir', 'R']
```

If the list only contains numbers, you can use the `min()` method to get the smallest number:
```py
listOfNumbers = [3, 89, 8, 100, 2, 4, 1]
smallestNum = min(listOfNumbers)

print(smallestNum) # Output: 1

```

If the list only contains numbers, you can use the `max()` method to get the largest number:**
```py
listOfNumbers = [3, 89, 8, 100, 2, 4, 1]
largestNum = max(listOfNumbers)

print(largestNum) # Output: 100
```

## Conclusion

In this article, you learned about lists in Python, how to index them, and several methods you can use to get things done with them.

Lists are a powerful data structure you should get comfortable using because they are very dynamic and can help you get things done in multiple ways.

If you find this article helpful, please share it with your friends and family.



