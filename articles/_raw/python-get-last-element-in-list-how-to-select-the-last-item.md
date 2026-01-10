---
title: Python Get Last Element in List – How to Select the Last Item
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-03-15T23:26:34.000Z'
originalURL: https://freecodecamp.org/news/python-get-last-element-in-list-how-to-select-the-last-item
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/list.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "Lists are one of the built-in data types in Python. You use them to store\
  \ multiple elements in one variable. \nLists enable us group similar data together,\
  \ and we can also perform operations on these grouped elements at the same time.\n\
  In this article,..."
---

Lists are one of the built-in data types in Python. You use them to store multiple elements in one variable. 

Lists enable us group similar data together, and we can also perform operations on these grouped elements at the same time.

In this article, we will talk about how to get the last item in a list. We will begin with an explanation of how you generally access items in a list and then look at some of the ways we can select the last item.

## How to Access Items in a List in Python

In this section, we'll talk about accessing data stored in a list using their index.

Here is what a list looks like:

```python
myList = ["yes", "no", "maybe"]
```

The items are nested in square brackets where each item is separated by a comma. 

Items in a list have index numbers assigned to them when the list is created or as we add them to the list. This index number starts at zero. So the first item in a list has an index number of zero and the second has an index number of one and so on. 

In the list we created in the example above, the index of `"yes"` is 0, the index of `"no"` is 1, and the index of `"maybe"` is 2. 

```python
myList = ["yes", "no", "maybe"]

print(myList[0]) # yes
print(myList[1]) # no
print(myList[2]) # maybe
```

Now let's look at some of the methods we can use to select the last item in our lists.

## How to Select the Last Item in a List Using Negative Indexing

Just like we established in the last section, each item in a list has an index number which starts at zero. 

In Python, we can also use negative values for these indexes. While the positive indexes start from 0 (which denotes the position of the first element), negative indexes start from -1, and this denotes the position of the last element.

Here's an example:

```python
myList = ["yes", "no", "maybe"]

print(myList[-1]) # maybe

```

We passed -1 as the index and got the last item returned to use. In the same order, if we use an index of -2, we would get `"no"` returned. If we use an index of -3, we would get `"yes"` returned. 

```python
myList = ["yes", "no", "maybe"]

print(myList[-1]) # maybe
print(myList[-2]) # no
print(myList[-3]) # yes

```

Using an index that doesn't exist will result in an error.

In the next section, we will see how to select the last item using the `pop()` method.

## How to Select the Last Item in a List Using the `pop()` Method

While the `pop()` method will select the last item, it will also delete it – so you should only use this method when you actually want to delete the last item in the list.

Here is an example:

```python
myList = ["yes", "no", "maybe"]

print(myList.pop()) # maybe

print(myList) # ['yes', 'no']

```

After using the `pop()` method, we got the value of the last element printed. But then when we print the list to the console, we can see that the last item no longer exists.

## Conclusion

In this article, we learned how to select the last item in a list using negative indexing and how to select and remove the last item with the `pop()` method in Python. 

Happy coding!


