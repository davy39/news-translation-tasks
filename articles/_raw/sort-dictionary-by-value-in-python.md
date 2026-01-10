---
title: Sort Dictionary by Value in Python – How to Sort a Dict
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-09-13T15:16:42.000Z'
originalURL: https://freecodecamp.org/news/sort-dictionary-by-value-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/sortDictByValue.png
tags:
- name: dictionary
  slug: dictionary
- name: Python
  slug: python
seo_title: null
seo_desc: 'In Python, a dictionary is a fat structure that is unordered by default.
  So, sometimes, you''ll want to sort dictionaries by key or value to make queries
  easier.

  The problem is that sorting a dictionary by value is never a straightforward thing
  to do....'
---

In Python, a dictionary is a fat structure that is unordered by default. So, sometimes, you'll want to sort dictionaries by key or value to make queries easier.

The problem is that sorting a dictionary by value is never a straightforward thing to do. That’s because Python doesn’t have an inbuilt method to do it.

However, I figured out a way to sort dictionaries by value, and that’s what I’m going to show you how to do in this article.

## What We'll Cover
- [How to Sort Data with the `sorted()` Method](#heading-how-to-sort-data-with-the-sorted-method)
- [How the `sorted()` Method Works](#heading-how-the-sorted-method-works)
  - [Parameters of the `sorted()` Method](#heading-parameters-of-the-sorted-method)  
- [How to Sort a Dictionary with the `sorted()` Method](#heading-how-to-sort-a-dictionary-with-the-sorted-method)
  - [How to Convert the Resulting List to a Dictionary](#heading-how-to-convert-the-resulting-list-to-a-dictionary)
  - [How to Sort the Dictionary by Value in Ascending or Descending Order](#heading-how-to-sort-the-dictionary-by-value-in-ascending-or-descending-order)
- [Conclusion](#heading-conclusion)


## How to Sort Data with the `sorted()` Method

The `sorted()` method sorts iterable data such as lists, tuples, and dictionaries. But it sorts by key only. 

The `sorted()` method puts the sorted items in a list. That’s another problem we have to solve, because we want the sorted dictionary to remain a dictionary.

For instance, `sorted()` arranged the list below in alphabetical order:
```py
persons = ['Chris', 'Amber', 'David', 'El-dorado', 'Brad', 'Folake']
sortedPersons = sorted(persons)

print(sortedPersons)
# Output: ['Amber', 'Brad', 'Chris', 'David', 'El-dorado', 'Folake']
```

And the `sorted()` method sorts the numbers in the tuple below in ascending order:
```py
numbers = (14, 3, 1, 4, 2, 9, 8, 10, 13, 12)
sortedNumbers = sorted(numbers)

print(sortedNumbers)
# Output: [1, 2, 3, 4, 8, 9, 10, 12, 13, 14]
```

If you use the `sorted()` method with a dictionary, only the keys will be returned and as usual, it will be in a list:
```py
my_dict = { 'num6': 6, 'num3': 3, 'num2': 2, 'num4': 4, 'num1': 1, 'num5': 5}
sortedDict = sorted(my_dict)

print(sortedDict)
# ['num1', 'num2', 'num3', 'num4', 'num5', 'num6']
```
This is not the behavior you want. You want the dictionary to be sorted by value and remain a dictionary. That’s what I’m going to show you next.

## How the `sorted()` Method Works 
To sort a dictionary, we are still going to use the sorted function, but in a more complicated way. Don’t worry, I will explain everything you need to know. 

Since we are still going to use the `sorted()` method, then it’s time to explain the `sorted()` method in detail.

### Parameters of the `sorted()` Method 

The `sorted()` method can accept up to 3 parameters:

- iterable – the data to iterate over. It could be a tuple, list, or dictionary. 

- key – an optional value, the function that helps you to perform a custom sort operation.

- reverse – another optional value. It helps you arrange the sorted data in ascending or descending order

If you guess it right, the key parameter is what we’ll pass into the `sorted()` method to get the dictionary sorted by value. 

Now, it’s time to sort our dictionary by value and make sure it remains a dictionary.

## How to Sort a Dictionary with the `sorted()` Method

To correctly sort a dictionary by value with the `sorted()` method, you will have to do the following:

- pass the dictionary to the `sorted()` method as the first value 
- use the `items()` method on the dictionary to retrieve its keys and values
- write a lambda function to get the values retrieved with the `item()` method

Here’s an example:
```py
footballers_goals = {'Eusebio': 120, 'Cruyff': 104, 'Pele': 150, 'Ronaldo': 132, 'Messi': 125}

sorted_footballers_by_goals = sorted(footballers_goals.items(), key=lambda x:x[1])
print(sorted_footballers_by_goals)

```
As I said earlier, we have to get those values of the dictionary so we can sort the dictionary by values. That’s why you can see 1 in the lambda function. 

1 represents the indexes of the values. The keys are 0. Remember that a programmer starts counting from 0, not 1.

With that code above, I got the result below:
```py
# [('Cruyff', 104), ('Eusebio', 120), ('Messi', 125), ('Ronaldo', 132), ('Pele', 150)]
```

Here’s the full code so you don’t get confused:
```py
footballers_goals = {'Eusebio': 120, 'Cruyff': 104, 'Pele': 150, 'Ronaldo': 132, 'Messi': 125}

sorted_footballers_by_goals = sorted(footballers_goals.items(), key=lambda x:x[1])
print(sorted_footballers_by_goals)

# [('Cruyff', 104), ('Eusebio', 120), ('Messi', 125), ('Ronaldo', 132), ('Pele', 150)]
```

You can see the dictionary has been sorted by values in ascending order. You can also sort it in descending order. But we’ll look at that later because we still have a problem with the result we got.

The problem is that the dictionary is not a dictionary anymore. The individual keys and values were put in a tuple and further condensed into a list. Remember that whatever you get as the result of the `sorted()` method is put in a list. 

We’ve been able to sort the items in the dictionary by value. What’s left is converting it back to a dictionary. 

### How to Convert the Resulting List to a Dictionary

To convert the resulting list to a dictionary, you don’t need to write another complicated function or a loop. You just need to pass the variable saving the resulting list into the `dict()` method.  

```py
converted_dict = dict(sorted_footballers_by_goals)
print(converted_dict)
# Output: {'Cruyff': 104, 'Eusebio': 120, 'Messi': 125, 'Ronaldo': 132, 'Pele': 150}
```

Remember we saved the sorted dictionary in the variable named `sorted_footballers_by_goals`, so it’s the variable we have to pass to `dict()`.

The full code looks like this:
```py
footballers_goals = {'Eusebio': 120, 'Cruyff': 104, 'Pele': 150, 'Ronaldo': 132, 'Messi': 125}

sorted_footballers_by_goals = sorted(footballers_goals.items(), key=lambda x:x[1])
converted_dict = dict(sorted_footballers_by_goals)

print(converted_dict)
# Output: {'Cruyff': 104, 'Eusebio': 120, 'Messi': 125, 'Ronaldo': 132, 'Pele': 150}
```
That’s it! We’ve been able to sort the items in the dictionary and convert them back to a dictionary. We’ve just had our cake and ate it as well!

### How to Sort the Dictionary by Value in Ascending or Descending Order
Remember the `sorted()` method accepts a third value called `reverse`. 

`reverse` with a value of `True` will arrange the sorted dictionary in descending order.
```py
footballers_goals = {'Eusebio': 120, 'Cruyff': 104, 'Pele': 150, 'Ronaldo': 132, 'Messi': 125}

sorted_footballers_by_goals = sorted(footballers_goals.items(), key=lambda x:x[1], reverse=True)
converted_dict = dict(sorted_footballers_by_goals)

print(converted_dict)
# Output: {'Pele': 150, 'Ronaldo': 132, 'Messi': 125, 'Eusebio': 120, 'Cruyff': 104}
```
You can see the output is reversed because we passed `reverse=True` to the `sorted()` method.

If you don’t set `reverse` at all or you set its value to false, the dictionary will be arranged in ascending order. That’s the default.

## Conclusion
Congratulations. You can now sort a dictionary by value despite not having a built-in method or function to use in Python.

However, there’s something that raised my curiosity when I was preparing to write this article. Remember we were able to use `sorted()` directly on a dictionary. This got us a list as the result, though we only got the keys and not the values.

What if we convert that list to a dictionary with the `dict()` method? Do you think we can get the desired result? Let's see:
```py
my_dict = { 'num6': 6, 'num3': 3, 'num2': 2, 'num4': 4, 'num1': 1, 'num5': 5}
sortedDict = sorted(my_dict)

converted_dict = dict(sortedDict)
print(converted_dict)
"""
Output: 
dict_by_value.py
Traceback (most recent call last):
  File "sort_dict_by_value.py", line 17, in <module>
    converted_dict = dict(sortedDict)
ValueError: dictionary update sequence element #0 has length 4; 2 is required
"""
```

We got an error! That’s because if you want to create a dictionary from a list, you have to use dictionary comprehension. And if you use dictionary comprehension for this type of data, you’d have to specify one value for all the entries. That would defy the purpose of sorting a dictionary by value, so it's not what we want.

If you want to learn more about dictionary comprehension, you should [read this article](https://www.freecodecamp.org/news/dictionary-comprehension-in-python-explained-with-examples/).

Thank you for reading!



