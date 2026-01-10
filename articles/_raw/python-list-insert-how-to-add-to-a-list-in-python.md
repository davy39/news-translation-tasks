---
title: Python List insert() – How to Add to a List in Python
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-05-10T21:22:33.000Z'
originalURL: https://freecodecamp.org/news/python-list-insert-how-to-add-to-a-list-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/dictionaary.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'The list data type is one of the built-in data structures in Python along
  with sets, tuples, and dictionaries. You use a list to organize, group, and store
  data.

  But each of these data structures has distinctive features that differentiates them
  from...'
---

The list data type is one of the built-in data structures in Python along with sets, tuples, and dictionaries. You use a list to organize, group, and store data.

But each of these data structures has distinctive features that differentiates them from each other.

In this article, we'll see how to create a list in Python. We'll also see how to add items to a list using the `insert()`, `append()`, and `extend()` methods.

## How to Create a List in Python

To create a list in Python, we use square brackets. Here's an example:

```python
myList = ['one', 'two', 'three']

print(myList)

# ['one', 'two', 'three']
```

In the code above, we created a list called `myList` with three items – "one", "two", and "three". As you can see above, the items are in the square brackets.

## How Do You Add an Item to a List in Python?

There are three methods we can use when adding an item to a list in Python. They are: `insert()`, `append()`, and `extend()`. We'll break them down into separate sub-sections.

### How to Add an Item to a List Using the `insert()` Method

You can use the `insert()` method to insert an item to a list at a specified index. Each item in a list has an index. The first item has an index of zero (0), the second has an index of one (1), and so on.

Here's an example using the `insert()` method:

```python
myList = ['one', 'two', 'three']

myList.insert(0, 'zero')

print(myList)

# ['zero', 'one', 'two', 'three']
```

In the example above, we created a list with three items: `['one', 'two', 'three']`. 

We then used the `insert()` method to insert a new item – "zero" at index 0 (the first index): `myList.insert(0, 'zero')`.

The `insert()` method takes in two parameters – the index of the new item to be inserted and the value of the item.

### How to Add an Item to a List Using the `append()` Method

Unlike the `insert()` method which allows us to specify where to insert an item, the `append()` method adds the item to the end of the list. The new item's value is passed in as a parameter in the `append()` method.

Here is an example:

```python
myList = ['one', 'two', 'three']

myList.append('four')

print(myList)

# ['one', 'two', 'three', 'four']
```

The new item was passed in as a parameter in the code above: `myList.append('four')`. 

When printed to the console, we have the item at the last index of the list. 

### How to Add an Item to a List Using the `extend()` Method

You can use the `extend()` method to append a data collection to a list. I'm using "data collection" here because we can also append sets, tuples, and so on to a list.

Let's see some examples.

#### How to Append a List to a List Using the `extend()` Method

```python
myList1 = ['one', 'two', 'three']
myList2 = ['four', 'five', 'six']
```

In the code above, we created two lists – `myList1` and `myList2`. Next, we'll append the items in the second list to the first one. 

Here's how:

```python
myList1.extend(myList2)
```

So when we print `myList1`, we'll have this: `['one', 'two', 'three', 'four', 'five', 'six']`.

Here's everything put together:

```python
myList1 = ['one', 'two', 'three']
myList2 = ['four', 'five', 'six']

myList1.extend(myList2)

print(myList1)
# ['one', 'two', 'three', 'four', 'five', 'six']
```

#### How to Append a Tuple to a List Using the `extend()` Method

The process here is the same as the last example, except that we're appending a tuple. You create a tuple using parentheses.

That is: 

```
myTuple = ('Hello', 'Hi')
```

Let's append a tuple to a list using the `extend()` method.

```python
myList1 = ['one', 'two', 'three']
myList2 = ('four', 'five', 'six')

myList1.extend(myList2)

print(myList1)

# ['one', 'two', 'three', 'four', 'five', 'six']
```

We get the same result as in the last section.

## Conclusion

In this article, we talked about lists in Python.

We saw how to create a list and the various methods for adding items to a list.

We added items to our list using the `insert()`, `append()`, and `extend()` methods. 

The `insert()` method inserts a new item in a specified index, the `append()` method adds a new at the last index of a list, while the `extend()` method appends a new data collection to a list.

Happy coding!

