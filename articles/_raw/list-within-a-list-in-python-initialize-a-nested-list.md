---
title: List Within a List in Python – How to Initialize a Nested List
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-02-16T17:24:40.000Z'
originalURL: https://freecodecamp.org/news/list-within-a-list-in-python-initialize-a-nested-list
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/List-Within-a-List-in-Python---How-to-Initialize-a-Nested-List-1.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "By Shittu Olumide\nLists are a built-in data type in Python. And you can\
  \ use them to store a collection of elements. \nLists are ordered, mutable, and\
  \ contain elements of different data types, such as strings, integers, and other\
  \ lists. \nIn Python, lis..."
---

By Shittu Olumide

Lists are a built-in data type in Python. And you can use them to store a collection of elements. 

Lists are ordered, mutable, and contain elements of different data types, such as strings, integers, and other lists. 

In Python, lists are a fundamental type of data structure that you'll use frequently whether you're a web developer, data scientist, or anything in between.

## How to Create a List in Python

You can create a list in Python by separating the elements with commas and using square brackets `[]`.  Let's create an example list:

```py
myList = [3.5, 10, "code", [ 1, 2, 3], 8]

```

From the example above, you can see that a list can contain several datatypes. In order to access these elements within a string, we use indexing. The first index is `0`, the second index is `1`, and so on.  

Lists come with a wide range of methods such as:

* `append()`: adds an element to the end of the list.
* `insert()`: adds an element at a specified position in the list.
* `remove()`: removes the first occurrence of a specified element from the list.
* `pop()`: removes the element at a specified position in the list and returns it.
* `sort()`: sorts the elements in the list in ascending order.
* `reverse()`: reverses the order of the elements in the list.
* `count()`: returns the number of times a specified element appears in the list.
* `index()`: returns the index of the first occurrence of a specified element in the list.
* `extend()`: extends the list by appending elements from another iterable.

In Python, you can also have lists within a list. And that's what we'll discuss in the next section.

## How a List within a List Works in Python

A list within another list is referred to as a nested list in Python. We can also say that a list that has other lists as its elements is a nested list. 

When we want to keep several sets of connected data in a single list, this can be helpful.

Here is an illustration of a Python nested list:

```py
MyList = [[22, 14, 16], ["Joe", "Sam", "Abel"], [True, False, True]]

```

Just like we said earlier, to access the elements in this nested list we use indexing. To access an element in one of the sublists, we use two indices – the index of the sublist and the index of the element within the sublist. 

Let's use the example of the nested list above and access a particular sublist/element:

```py
#printing a sublist
print(MyList[0])
[22, 14, 16]

# printing an element within a sublist
print(MyList[0][1]) #output: 14

# modifying an element in a sublist
MyList[0][1] = 20
print(MyList) #output:[[22, 20, 16], ["Joe", "Sam", "Abel"], [True, False, True]]

```

Let's have a look at how we can initialize a nested listed correctly in Python.

## How to Initialize a Nested List in Python

We know that a nested list is a list inside of another list. But creating a list of lists in Python can be a little tricky because there are wrong ways and right ways to do it.

### How NOT to initialize a nested list

Let's see one of the wrong ways of initializing a nested list (although it is the most basic and fastest way to initialize a nested list):

```py
# Create a list with 5 references of same sublist
MyList = [[]] * 5
print(MyList)  #output: [[ ], [ ], [ ], [ ], [ ]]

```

Initializing a nested list in this manner has the disadvantage that each entry in the list has the same `ID`, pointing to the same list object. 

Let's verify this by looping through the list and printing the id of each sublist object.

```py
for objects in MyList:
    print(id(objects))

#output:

200792200
200792200
200792200
200792200
200792200

```

Let's see why this is very bad. We will insert an element into the second sublist and then check the content of the main list.

```py
# Insert 7 into the second sublist
MyList[1].append(7)
print(MyList)

#output: [[7], [7], [7], [7], [7]]

```

The element was inserted into all the sublists, because they have the same ID. Therefore they are not different lists. So as you can see, this is an incorrect way to initialize a nested list.

### How to initialize a nested list

#### Using list comprehension & range()

Using List Comprehension, we can create a sub-list and append it to the main list for each element of a sequence of numbers from `0` to `n-1` that we generated using Python's `range()` function.

```py
MyList = [[] for i in range(5)]
print(MyList) 

#output: [[], [], [], [], []]

```

This creates a nested list that has 5 sublists. Now let's see if each sublist has a different ID. We'll also insert an element into a sublist.

```py
# loop through the list and print each sublist id.
for objects in MyList:
    print(id(objects))
    
#output: 
200739688
200739944
200739848
200739912
200739880

# modify the element in a sublist – let's insert 7 in the second sublist
MyList[1].append(7)
print(MyList)

#Output: [[], [7], [], [], []]

```

As you can see, the element (7) is only inserted to the second sublist and other sublists are left empty because they all have different IDs or objects.

#### Using a for loop

Let's say we want to build a list that internally has four different sublists. To accomplish this, we will first create a new empty list, then use a for loop to iterate from 0 to 3. We'll append an empty list to the new list after each iteration.

```py
MyList = []
# Iterate over a sequence of numbers from 0 to 3
for i in range(4):
    # In each iteration, add an empty list to the main list
    MyList.append([])
print(MyList)

# output: [[], [], [], []]

```

To confirm if all sublists have different IDs, you can do this:

```py
for objects in MyList:
    print(id(objects))

# output:

200792232
200792296
200792168
200740648

```

The distinct IDs of each sublist attest to the fact that these are distinct objects.

#### Using Numpy

Python's [Numpy](https://numpy.org/) module includes a function called `empty()` that generates empty Numpy arrays of a specified shape. Using Numpy to initialize a nested list can be a practical way to build and work with 2-dimensional data structures in Python.

```py
import numpy 
num = 5

# Create a 2D Numpy array of shape (5, 0) and convert it to a nested list
MyList = numpy.empty((num, 0)).tolist()
print(MyList)

# output: [[], [], [], [], []]

```

We now have 5 sublists – let's check their IDs.

```py
for objects in MyList:
    print(id(objects))

# output:

200739944
200739848
200739912
200740616
200739688

```

This is another confirmation that all the sublists are different objects. So if we want to modify any sublist, the remaining sublists will not be affected. 

## Conclusion

We have come to the end of this article. The key takeaways are that initializing a nested list can be tricky - and there's an incorrect (and several correct) ways to do it. 

There are many other ways that you can initialize a nested list in Python, but the ones above are the most popular and widely used. 

Once we have created the nested list, we can access and modify its elements using indexing as you saw above. 

Let's connect on [Twitter](https://www.twitter.com/Shittu_Olumide_) and on [LinkedIn](https://www.linkedin.com/in/olumide-shittu). You can also subscribe to my [YouTube](https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A) channel.

Happy Coding!

