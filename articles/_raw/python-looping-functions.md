---
title: How to Use Built-in Looping Functions in Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-11-01T18:34:42.000Z'
originalURL: https://freecodecamp.org/news/python-looping-functions
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/python-looping-techniques.png
tags:
- name: Loops
  slug: loops
- name: Python
  slug: python
seo_title: null
seo_desc: "By Shweta Goyal\nWhen you're looping through a sequence in Python like\
  \ a list, tuple, string, or dictionary, do you ever feel like your code is messy\
  \ or you want to remove some variables from it? \nFortunately, Python has some useful\
  \ inbuilt functions ..."
---

By Shweta Goyal

When you're looping through a sequence in Python like a list, tuple, string, or dictionary, do you ever feel like your code is messy or you want to remove some variables from it? 

Fortunately, Python has some useful `inbuilt` functions which make your code more concise and more readable.

In this tutorial, we will learn about various `inbuilt` functions with simple examples to understand how they work.

## How to loop through a sequence with the enumerate() function in Python

Python's `enumerate()` function loops over a sequence (list, tuple, string, or dictionary) while keeping track of the index value in a separate variable. 

Let's see the syntax:

`
enumerate(iterable, start)
`

It consists of two arguments:

* **iterable** – An iterable object or a sequence, that is an object that can be looped.
* **start** – Index value or starting value of the count. By default, the value starts at 0.

Here's the output you get:

```
Output
[(0, item_1), (1, item_1), (2, item_2), . . ., (n, item_n)]
```

As you can see, we get elements in the iterable along with their respective indices.

Let's take an example without an index: 

```
colour = ["Black", "Purple", "Brown", "Yellow", "Blue"]
list(enumerate(colour))
```

```
Output:
[(0, 'Black'), (1, 'Purple'), (2, 'Brown'), (3, 'Yellow'), (4, 'Blue')]
```

As you can see, the index starts from 0. We have not used the second argument. By default, the value of the index starts at 0.

Let's take another example with an index:

```
colour = ["Black", "Purple", "Brown", "Yellow", "Blue"]
list(enumerate(colour, 10))
```

```
Output:
[(10, 'Black'), (11, 'Purple'), (12, 'Brown'), (13, 'Yellow'), (14, 'Blue')]
```

So, here our index starts at 10 as we set the start argument to 10 which starts the count from 10. 

You have to specify a list or tuple to get the output, otherwise it will only give you this result:

```
colour = ["Black", "Purple", "Brown", "Yellow", "Blue"]
enumerate(colour)
```

```
Output:
<enumerate object at 0x7f6a97ad7c40>
```

Let's take an example with a dictionary:

```
colour = {"Black": 0, 
          "Purple": 2, 
          "Brown": 4, 
          "Yellow": 9, 
          "Blue": 1}
list(enumerate(colour))
```

```
Output:
[(0, 'Black'), (1, 'Purple'), (2, 'Brown'), (3, 'Yellow'), (4, 'Blue')]
```

When we iterate over a dictionary, we only get the keys not the values of the dictionary.

To loop over a dictionary and to get the values, Python has two in-built functions:

* `items()` – This function helps us get key-value pairs from the dictionary.
* `values()` – This function helps us get only values from the dictionary without the keys.

Let's see examples of the functions:

```
colour = {"Black": 0, 
          "Purple": 2, 
          "Brown": 4, 
          "Yellow": 9, 
          "Blue": 1}
list(enumerate(colour.items()))
```

```
Output:
[(0, ('Black', 0)), (1, ('Purple', 2)), (2, ('Brown', 4)), (3, ('Yellow', 9)), (4, ('Blue', 1))]
```

You can use it with a for loop as well like this:

```
colour = {"Black": 0, 
          "Purple": 2, 
          "Brown": 4, 
          "Yellow": 9, 
          "Blue": 1}
for ind, (keys, value) in enumerate(colour.items()):
	print(ind, keys, value)
```

```
Output:
0 Black 0
1 Purple 2
2 Brown 4
3 Yellow 9
4 Blue 1
```

In this example, we get the key-value pairs. Now we will use another function,

```
colour = {"Black": 0, 
          "Purple": 2, 
          "Brown": 4, 
          "Yellow": 9, 
          "Blue": 1}
list(enumerate(colour.values()))
```

```
Output:
[(0, 0), (1, 2), (2, 4), (3, 9), (4, 1)]
```

With a for loop:

```
colour = {"Black": 0, 
          "Purple": 2, 
          "Brown": 4, 
          "Yellow": 9, 
          "Blue": 1}
for ind, value in enumerate(colour.values()):
	print(ind, value)
```

```
Output:
0 0
1 2
2 4
3 9
4 1
```

Here, you only get the values, not the keys while iterating through the dictionary.

## How to loop through a sequence with the zip() function in Python

The `zip()` function takes more than one iterable with the same index values and combines them and returns an iterator. An iterator can be a tuple, a list, or a dictionary. 

Let's see the syntax:

```
zip(*iterables)
```

or

```
zip(iterator1, iterator2, ... so on)
```

Arguments of a zip() function:

* **Iterables** can be lists, tuples, strings, sets, or dictionaries. 

Let's take an example:

```
color = ["Blue", "Orange", "Brown", "Red"]
code = [20, 10, 56, 84]
list(zip(color, code))
```

```
Output:
[('Blue', 20), ('Orange', 10), ('Brown', 56), ('Red', 84)]
```

Here, two lists are combined or zipped together and we get an iterator.

If the lengths of the iterables are different then the iterator stops producing an output when the shortest iterable is exhausted.

Let's take an example:

```
color = ["Blue", "Orange", "Brown"]
code = [20, 10, 56, 84]
list(zip(color, code))
```

```
Output:
[('Blue', 20), ('Orange', 10), ('Brown', 56)]
```

Here, the shortest length is of color and we get in the output up to 3 colors and codes. So the 4th code is rejected.

In **Python 3.10**, there is a new parameter `strict` which checks the length of the elements. It will give us an error if the length of the elements do not match. Let's take an example:

```
color = ("Blue", "Orange", "Brown", "Purple")
code = (20, 10, 56)
for col, cod in zip(color, code, strict=True):
    print(col, cod)
```

```
Output:
Blue 20
Orange 10
Brown 56
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    for col, cod in zip(color, code, strict=True):
ValueError: zip() argument 2 is shorter than argument 1
```

You don't need to take two iterators, you can take any number of iterators. Let's take an example with three iterators:

```
Abbreviation = ['Bl', 'Or', 'Br', 'Gn']
Color = ['Blue', 'Orange', 'Brown', 'Green']
Code = [20, 10, 56, 88]
for ab, col, cod in zip(Abbreviation, Color, Code):
	print(ab, col, cod)
```

```
Output:
Bl Blue 20
Or Orange 10
Br Brown 56
Gn Green 88
```

You can create dictionaries as well by using the `dict` function. Let's take an example:

```
Color = ['Blue', 'Orange', 'Brown', 'Green']
Code = [20, 10, 56, 88]
dict(zip(Color, Code))
```

```
Output:
{'Blue': 20, 'Orange': 10, 'Brown': 56, 'Green': 88}
```

## How to loop through a sequence with the sorted() function in Python

The `sorted()` function returns the elements in sorted order from an iterable object.

Let's see the syntax:

```
sorted(iterable, key=key, reverse=reverse)

It consists of three arguments:

* **iterable** – a sequence that can be a list, a tuple, a string, and so on.
* **key** – is optional. It is a function that you can use to customize the sort order. The default option is None. 
* **reverse** – is also optional. It is a Boolean. Here, the default value is **False** which is in _ascending_ order. **True** will be _descending_ order.

Let's take an example:

```
Color = ['Blue', 'Orange', 'Brown', 'Green']
sorted(Color)
```

```
Output:
['Blue', 'Brown', 'Green', 'Orange']
```

By default, your output will be a list and will be in ascending order. If it is a string, it will be sorted alphabetically and if it is in numbers, it will be sorted numerically.

The above output shows a list sorted in ascending order. If you want it in descending order, you can use the `reverse` argument. Let's take an example:

```
Color = ('Blue', 'Orange', 'Brown', 'Green')
sorted(Color, reverse=True)
```

```
Output:
['Orange', 'Green', 'Brown', 'Blue']
```

Original values remain unchanged as the `sorted()` function does not change the original values – it will only produce the output. The output will be an ordered list.

The `key` function can be built-in or user-defined which you can use to manipulate the order of the output. 

Let's take an example with a built-in function first:

```
Word = ('TO', 'is', 'apple', 'PEAR', 'LIKE')
sorted(Word, key=str.upper)
```

```
Output:
['apple', 'is', 'LIKE', 'PEAR', 'TO']
```


By default, the output will be in ascending order. You have to reverse the argument like this:

```
Word = ('TO', 'is', 'apple', 'PEAR', 'LIKE')
sorted(Word, key=str.upper, reverse=True)
```

```
Output:
['TO', 'PEAR', 'LIKE', 'is', 'apple']
```

The number of arguments should be one while using a key argument. Let's take an example with a user-defined function:

```
numb = (22, 10, 5, 34, 29)
sorted(numb, key=lambda x: x%5)
```

```
Output:
[10, 5, 22, 34, 29]
```

I have used the lambda function for simplicity, but you can use the traditional method for function definition if you want.

## How to loop through a sequence with the reversed() function in Python

The `reversed` function returns the elements in reverse order from an iterable object.

Let's see the syntax:

```
reversed(iterable)
```

The argument of the reversed function:

* **iterable** – It is a sequence like a list, tuple, set, and so on.

Let's take an example:

```
numb = (22, 10, 5, 34, 29)
list(reversed(numb))
```

```
Output:
[29, 34, 5, 10, 22]
```

You have to specify a list or a tuple otherwise it will only give you an address like the example below:

```
numb = (22, 10, 5, 34, 29)
reversed(numb)
```

```
Output:
<reversed object at 0x000001C1E7D9E110>
```

## Conclusion

Built-in functions help you to write your Python functions in a clear and concise way. They will help you to execute your function without getting messy.

In this tutorial, you have learned about different built-in functions in Python. You have seen various examples, and now you can practice on your own sequence. Hope you find this tutorial useful.

Follow me on [Twitter](https://twitter.com/Shweta_go). Happy Coding!


