---
title: Python Return Multiple Values – How to Return a Tuple, List, or Dictionary
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-20T22:17:45.000Z'
originalURL: https://freecodecamp.org/news/python-returns-multiple-values-how-to-return-a-tuple-list-dictionary
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/image1.jpeg
tags:
- name: data structures
  slug: data-structures
- name: Python
  slug: python
seo_title: null
seo_desc: "By Amy Haddad\nYou can return multiple values from a function in Python.\n\
  To do so, return a data structure that contains multiple values, like a list containing\
  \ the number of miles to run each week.\ndef miles_to_run(minimum_miles):\n   week_1\
  \ = minimum..."
---

By Amy Haddad

You can return multiple values from a function in Python.

To do so, return a data structure that contains multiple values, like a list containing the number of miles to run each week.

```python
def miles_to_run(minimum_miles):
   week_1 = minimum_miles + 2
   week_2 = minimum_miles + 4
   week_3 = minimum_miles + 6
   return [week_1, week_2, week_3]
 
print(miles_to_run(2))
# result: [4, 6, 8]
```

Data structures in Python are used to store collections of data, which can be returned from  functions. In this article, we’ll explore how to return multiple values from these data structures: tuples, lists, and dictionaries.

## Tuples

A tuple is an ordered, immutable sequence. That means, a tuple _can’t_ change. 

Use a tuple, for example, to store information about a person: their name, age, and location.

```python
nancy = ("nancy", 55, "chicago")
```

Here’s how you’d write a function that returns a tuple.

```python
def person():
   return "bob", 32, "boston"
 
print(person())
# result: ('bob', 32, 'boston')
```

Notice that we didn’t use parentheses in the return statement. That’s because you can return a tuple by separating each item with a comma, as shown in the above example. 

“It is actually the comma which makes a tuple, not the parentheses,” the [documentation](https://docs.python.org/3/library/stdtypes.html#tuple) points out. However, [parentheses _are_ required](https://docs.python.org/3/library/stdtypes.html#tuple) with empty tuples or to avoid confusion. 

Here’s an example of a function that uses parentheses `()` to return a tuple.

```python
def person(name, age):
   return (name, age)
print(person("henry", 5))
#result: ('henry', 5)
```

## List

A list is an ordered, mutable sequence. That means, a list _can_ change. 

You can use a list to store cities:

```python
cities = ["Boston", "Chicago", "Jacksonville"]
```

Or test scores:

```python
test_scores = [55, 99, 100, 68, 85, 78]
```

Take a look at the function below. It returns a list that contains ten numbers.

```python
def ten_numbers():
   numbers = []
   for i in range(1, 11):
       numbers.append(i)
   return numbers
 
print(ten_numbers())
#result: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

Here’s another example. This time we pass in several arguments when we call the function.

```python
def miles_ran(week_1, week_2, week_3, week_4):
   return [week_1, week_2, week_3, week_4]
 
monthly_mileage = miles_ran(25, 30, 28, 40)
print(monthly_mileage)
#result: [25, 30, 28, 40]
```

It’s easy to confuse tuples and lists. After all, both are containers that store objects. However, remember these key differences:

* Tuples can’t change.
* Lists can change.

## Dictionaries

A dictionary contains key-value pairs wrapped in curly brackets `{}`. Each “key” has a related “value.”  

Consider the dictionary of employees below. Each employee name is a “key” and their position is the “value.”

```python
employees = {
   "jack": "engineer",
   "mary": "manager",
   "henry": "writer",
}
```



Here’s how you’d write a function that returns a dictionary with a key, value pair.

```python
def city_country(city, country):
   location = {}
   location[city] = country
   return location
 
favorite_location = city_country("Boston", "United States")
print(favorite_location)
# result: {'Boston': 'United States'}
```

In the above example, “Boston” is the **key** and “United States” is the **value**.  

We’ve covered a lot of ground. The key point is this: you can return multiple values from a Python function, and there are several ways to do so.

_I write about the programming skills you need to develop and the concepts you need to learn, and the best ways to learn them at [amymhaddad.com](https://amymhaddad.com/)._

