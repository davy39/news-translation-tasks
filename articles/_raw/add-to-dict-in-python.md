---
title: Adding to Dict in Python – How to Append to a Dictionary
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-02-28T00:17:11.000Z'
originalURL: https://freecodecamp.org/news/add-to-dict-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/Shittu-Olumide-Adding-to-Dict-in-Python---How-to-Append-to-a-Dictionary-1.png
tags:
- name: dictionary
  slug: dictionary
- name: Python
  slug: python
seo_title: null
seo_desc: "By Shittu Olumide\nA dictionary in Python is a group of unordered items,\
  \ each of which has a unique set of keys and values. \nAny immutable data type,\
  \ such as a string, number, or tuple, can be used as the key. It serves as an exclusive\
  \ identifier for ..."
---

By Shittu Olumide

A dictionary in Python is a group of unordered items, each of which has a unique set of keys and values. 

Any immutable data type, such as a string, number, or tuple, can be used as the key. It serves as an exclusive identifier for the value in the dictionary. The value is repeatable and applicable to all types of data.

In Python, dictionaries are denoted by curly braces `{ }`, and each key-value pair is delimited by a colon `:`. A comma separates the key and value. Here is an illustration of a basic dictionary:

```py
my_dict = {"pineapple": 12, "apple": 30, "orange": 5, "avocado":7}

```

In this example, "pineapple", "apple", "orange", and "avocado" are the keys, and 12, 30, 5 and 7 are the corresponding values.

We will have a look at how we can add a single key-value pair to a dictionary using the `update()` method, and finally the  `dict()` constructor.

### How to add a single key-value pair to a dictionary

To add a single key-value pair to a dictionary in Python, we can use the following code:

```py
myDict = {'a': 1, 'b': 2}
myDict['c'] = 3

```

The above code will create a dictionary `myDict` with two key-value pairs. Then we added a new key-value pair `'c' : 3` to the dictionary by just assigning the value `3` to the key `'c'`.  After the  code is executed, the dictionary `myDict` will now contain the key-value pair `'c': 3`.

Let's confirm this by printing the dictionary.

```py
print(myDict)

```

Output:

```bash
{'a': 1, 'b': 2, 'c': 3}

```

If there is a key `'c'` in the dictionary already, the value would be updated to 3.

### How to add multiple key-value pairs with the `update()` method

Multiple key-value pairs can be simultaneously added to a dictionary using the `update()` method. This method inserts new entries into the original dictionary from another dictionary or an iterable of key-value pairs as input. The value of an existing key in the original dictionary will be updated with the new value.

Example using the `update()` method to add multiple entries to a dictionary:

```py
myDict = {'a': 1, 'b': 2}
new_data = {'c': 3, 'd': 4}

myDict.update(new_data)

print(myDict)

```

Output:

```bash
{'a': 1, 'b': 2, 'c': 3, 'd': 4}

```

Another fun thing about this method is that, we can use the `update()` method with an iterable of key-value pairs, such as a list of tuples. Let's see this in action.

```py
myDict = {'a': 1, 'b': 2}
new_data = [('c', 3), ('d', 4)]

myDict.update(new_data)

print(myDict)

```

The output is the same as the previous example:

```bash
{'a': 1, 'b': 2, 'c': 3, 'd': 4}

```

### How to update a dictionary using the `dict()` constructor

In Python, a dictionary can be updated or made from scratch using the `dict()` constructor. By passing a dictionary containing the new key-value pair as an argument to the `dict()` constructor, we can add a single key-value pair to an existing dictionary.

Example:

```py
myDict = {'a': 1, 'b': 2, 'c': 3}
newDict = dict(myDict, d=4)

print(newDict)

```

Output:

```bash
{'a': 1, 'b': 2, 'c': 3, 'd': 4}

```

In this example, three key-value pairs were added to a brand-new dictionary called `myDict`. Then, we created a new dictionary called `newDict` using the `dict()` constructor, which also added the key-value pair `'d': 4'`. 

When the two dictionaries are combined by the `dict()` constructor, any keys that are present in both dictionaries have their values overwritten by the value from the second dictionary (in this case, `'d': 4'`).

Keep in mind that a new dictionary can also be created using the `dict()` constructor from a list of key-value pairs, where each pair is represented by a tuple.

```py
MyList = [('a', 1), ('b', 2), ('c', 3)]
MyDict = dict(MyList)

print(MyDict)

```

Output:

```bash
{'a': 1, 'b': 2, 'c': 3}

```

## Conclusion

In Python, dictionaries are frequently used to store data and provide quick access to it using a distinct key value. They come in handy when working with lists or tuples, where we need to access data using a specific identifier rather than its place in a sequence.

Let's connect on [Twitter](https://www.twitter.com/Shittu_Olumide_) and on [LinkedIn](https://www.linkedin.com/in/olumide-shittu). You can also subscribe to my [YouTube](https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A) channel.

Happy Coding!

