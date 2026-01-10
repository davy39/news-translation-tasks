---
title: Python Empty List Tutorial – How to Create an Empty List in Python
subtitle: ''
author: Estefania Cassingena Navone
co_authors: []
series: null
date: '2020-06-18T14:31:55.000Z'
originalURL: https://freecodecamp.org/news/python-empty-list-tutorial-how-to-create-an-empty-list-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/Empty-list.png
tags:
- name: Python
  slug: python
- name: Tutorial
  slug: tutorial
seo_title: null
seo_desc: "If you want to learn how to create an empty list in Python efficiently,\
  \ then this article is for you. \nYou will learn:\n\nHow to create an empty list\
  \ using square brackets [].\nHow to create an empty list using list().\nTheir use\
  \ cases. \nHow efficient th..."
---

If you want to learn how to create an empty list in Python efficiently, then this article is for you. 

**You will learn:**

* How to create an empty list using square brackets `[]`.
* How to create an empty list using `list()`.
* Their use cases. 
* How efficient they are (one is faster than the other!). We will use the `timeit` module to compare them.

**Let's begin! ✨**

## 🔹 Using Square Brackets

You can create an empty list with an empty pair of square brackets, like this:  

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-131.png)

**💡 Tip:** We assign the empty list to a variable to use it later in our program. 

For example:

```
num = []
```

The empty list will have length `0`, as you can see right here:

```
>>> num = []
>>> len(num)
0
```

Empty lists are **falsy** values, which means that they evaluate to `False` in a boolean context:

```python
>>> num = []
>>> bool(num)
False
```

### Add Elements to an Empty List

You can add elements to an empty list using the methods `append()` and `insert()`:

* `append()` adds the element to the end of the list.
* `insert()` adds the element at the particular index of the list that you choose.

Since lists can be either truthy or falsy values depending on whether they are empty or not when they are evaluated, you can use them in conditionals like this:

```python
if num:
	print("This list is not empty")
else:
	print("This list is empty")
```

The output of this code is:

```python
This list is empty
```

Because the list was empty, so it evaluates to False.

In general:

* If the list is not empty, it evaluates to `True`, so the if clause is executed.
* If the list is empty, it evaluates to `False`, so the else clause is executed. 

### Example:

In the example below, we create an empty list and assign it to the variable `num`. Then, using a for loop, we add a sequence of elements (integers) to the list that was initially empty:

```python
>>> num = []
>>> for i in range(3, 15, 2):
	num.append(i)
```

We check the value of the variable to see if the items were appended successfully and confirm that the list is not empty anymore:  

```python
>>> num
[3, 5, 7, 9, 11, 13]
```

**💡 Tip:** We commonly use `append()` to add the first element to an empty list, but you can also add this element calling the `insert()` method with index `0`:

```python
>>> num = []
>>> num.insert(0, 1.5) # add the float 1.5 at index 0
>>> num
[1.5]
```

## 🔸 Using the list() Constructor

Alternatively, you can create an empty list with the type constructor `list()`, which creates a new list object. 

According to the [Python Documentation](https://docs.python.org/3/library/stdtypes.html#list):

> If no argument is given, the constructor creates a new empty list, `[]`.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-132.png)

💡 **Tip:** This creates a new list object in memory and since we didn't pass any arguments to `list()`, an empty list will be created.

For example:

```
num = list()
```

This empty list will have length `0`, as you can see right here:

```
>>> num = list()
>>> len(num)
0
```

And it is a **falsy** value when it is empty (it evaluates to `False` in a boolean context):

```python
>>> num = list()
>>> bool(num)
False
```

### Example:

This is a fully functional list, so we can add elements to it:

```python
>>> num = list()
>>> for i in range(3, 15, 2):
	num.append(i)
```

And the result will be a non-empty list, as you can see right here:

```python
>>> num
[3, 5, 7, 9, 11, 13]
```

## 🔹 Use Cases

* We typically use `list()` to create lists from existing iterables such as strings, dictionaries, or tuples. 
* You will commonly see square brackets `[]` being used to create empty lists in Python because this syntax is more concise and faster. 

## 🔸 Efficiency

Wait! I just told you that `[]` is faster than `list()`...

**But how much faster?** 

Let's check their time efficiencies using the [**timeit**](https://docs.python.org/3/library/timeit.html#module-timeit) module.

To use this module in your Python program, you need to import it:

```python
>>> import timeit
```

Specifically, we will use the [timeit function](https://docs.python.org/3/library/timeit.html#timeit.timeit) from this module, which you can call with this syntax:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-129.png)

💡 **Tip:** The code is repeated several times to reduce time differences that may arise from external factors such as other processes that might be running at that particular moment. This makes the results more reliable for comparison purposes.

**🚦 On your marks... get set... ready!** Here is the code and output:

First, we import the module.

```python
>>> import timeit
```

Then, we start testing each syntax.

### Testing `[]`:

```python
>>> timeit.timeit('[]', number=10**4)
0.0008467000000109692
```

### Testing `list()`:

```python
>>> timeit.timeit('list()', number=10**4)
0.002867799999989984
```

**💡 Tip:** Notice that the code that you want to time has to be surrounded by single quotes `''` or double quotes `""`. The time returned by the `timeit` function is expressed in seconds.

Compare these results:

* `[]`: `0.0008467000000109692` 
* `list()`: `0.002867799999989984`

You can see that `[]` is much faster than `list()`. There was a difference of approximately `0.002` seconds in this test:

```python
>>> 0.002867799999989984 - 0.0008467000000109692
0.0020210999999790147
```

**I'm sure that you must be asking this right now:** Why is `list()` less efficient than `[]` if they do exactly the same thing?

Well... `list()` is slower because it requires looking up the name of the function, calling it, and then creating the list object in memory. In contrast, `[]` is like a "shortcut" that doesn't require so many intermediate steps to create the list in memory. 

This time difference will not affect the performance of your program very much but it's nice to know which one is more efficient and how they work behind the scenes.

## 🔹 In Summary

You can create an empty list using an empty pair of square brackets `[]` or the type constructor `list()`, a built-in function that creates an empty list when no arguments are passed. 

Square brackets `[]` are commonly used in Python to create empty lists because it is faster and more concise.

**I really hope that you liked my article and found it helpful.** Now you can create empty lists in your Python projects. [Check out my online courses](https://www.udemy.com/user/estefania-cn/). Follow me on [Twitter](https://twitter.com/EstefaniaCassN). ⭐️

If you want to dive deeper into lists, you may like to read:

* [Python List Append – How to Add an Element to an Array, Explained with Examples](https://www.freecodecamp.org/news/python-list-append-how-to-add-an-element-to-an-array-explained-with-examples/)
* [The Python Sort List Array Method – Ascending and Descending Explained with Examples](https://www.freecodecamp.org/news/the-python-sort-list-array-method-ascending-and-descending-explained-with-examples/)
* [Python List Append VS Python List Extend – The Difference Explained with Array Method Examples](https://www.freecodecamp.org/news/python-list-append-vs-python-list-extend/)

