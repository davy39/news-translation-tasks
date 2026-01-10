---
title: Python .zip() – Zip Function in Python
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-04-13T18:28:32.000Z'
originalURL: https://freecodecamp.org/news/python-zip-zip-function-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/zip.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "When you use the zip() function in Python, it takes two or more data sets\
  \ and \"zips\" them together. This returns an object containing pairs of items derived\
  \ from the data sets. It groups these items in the order of their indexes. \nLet\
  \ me break it dow..."
---

When you use the `zip()` function in Python, it takes two or more data sets and "zips" them together. This returns an object containing pairs of items derived from the data sets. It groups these items in the order of their indexes. 

Let me break it down a bit more: the first item from the first data set gets paired with first item in the second data set, the second items in both data sets get paired with each other, and so on.

In this article, we'll see how to use the `zip()` function in Python with some examples.

## How to Use the `zip()` Function in Python

Here is the syntax for the `zip()` function in Python:

```txt
zip(dataSet1, dataSet2, ...)
```

Here is an example to demonstrate how it works:

```python
names = ("John", "Jane", "Jade")
ages = (2, 4, 6)

print(zip(names, ages))
# <zip object at 0x7f8d5915cc40>
```

In the code above, we created  two `tuples` – `names` and `ages`.  

We then used the `zip()` function: `print(zip(names, ages))`.

But we are not actually getting the paired data returned to us. This is because we have to say what data structure it will be zipped into. Here:

```python
names = ("John", "Jane", "Jade")
ages = (2, 4, 6)

zipped = zip(names, ages)

print(tuple(zipped))
# (('John', 2), ('Jane', 4), ('Jade', 6))
```

We stored our zipped data in a variable called `zipped` and while printing it, we nested it in a `tuple`: `print(tuple(zipped))`.

I have commented the output of the code: `(('John', 2), ('Jane', 4), ('Jade', 6))`. As you can see above, each item at a given index was paired with another item in the same index from the other data set.

You can also return the data nested in a `list`. Here's how:

```python
names = ("John", "Jane", "Jade")
ages = (2, 4, 6)

zipped = zip(names, ages)

print(list(zipped))
# [('John', 2), ('Jane', 4), ('Jade', 6)]
```

This is the same as the last example, but instead of having `tuple(zipped)`, we used `list(zipped)`.

In the same manner, we can also use `dict` and `set` but the data returned when we use `set` is likely to be unordered.

We can loop through the zipped data by doing this:

```python
names = ("John", "Jane", "Jade", "John")
ages = (2, 4, 6)

zipped = zip(names, ages)

for(x,y) in zipped:
    print(x,y)

# John 2
# Jane 4
# Jade 6
```

## Conclusion

In this article, we learned what the `zip()` function is and what it does in Python.

We saw how to zip two data sets and return their pairs using different data structures. 

Lastly, we saw how to loop through and print the zipped data.

Happy coding!


