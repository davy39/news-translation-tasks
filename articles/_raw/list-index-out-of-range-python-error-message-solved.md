---
title: List Index Out of Range – Python Error Message Solved
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-01-20T16:03:30.000Z'
originalURL: https://freecodecamp.org/news/list-index-out-of-range-python-error-message-solved
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/domenico-loia-hGV2TfOh0ns-unsplash.jpg
tags:
- name: error
  slug: error
- name: Python
  slug: python
seo_title: null
seo_desc: 'In this article you''ll see a few of the reasons that cause the list index
  out of range Python error.

  Besides knowing why this error occurs in the first place, you''ll also learn some
  ways to avoid it.

  Let''s get started!

  How to Create a List in Python

  ...'
---

In this article you'll see a few of the reasons that cause the `list index out of range` Python error.

Besides knowing why this error occurs in the first place, you'll also learn some ways to avoid it.

Let's get started!

## How to Create a List in Python

To create a list object in Python, you need to:

- Give the list a name,
- Use the assignment operator, `=`,
- and include 0 or more list items inside square brackets,`[]`. Each list item needs to be separated by a comma.

For example, to create a list of names you would do the following:

```python
names = ["Kelly", "Nelly", "Jimmy", "Lenny"]
```

The code above created a list called `names` that has four values: `Kelly, Nelly, Jimmy, Lenny`.

### How to Check the Length of a List in Python

To check the length of a list in Python, use Python's build-in `len()` method. 

`len()` will return an integer, which will be the number of items stored in the list.

```python
names = ["Kelly", "Nelly", "Jimmy", "Lenny"]

#create a variable called name_length to store the length of the list
name_length = len(names)

#print value of variable to the console
print(name_length)

#output
#4
```

There are four items stored in the list, therefore the length of the list will be four.

### How to Access Individual List Items in Python

Each item in a list has its own *index number*. 

Indexing in Python, and most modern programming languages, starts at 0.

This means that the first item in a list has an index of 0, the second item has an index of 1, and so on.

You can use the index number to access the individual item.

To access an item in a list using its index number, first write the name of the list. Then, inside square brackets, include the intiger that corresponds with the item's index number.

Taking the example from earlier, this is how you would access each item inside the list using its index number:

```python
names = ["Kelly", "Nelly", "Jimmy", "Lenny"]

names[0] # Kelly
names[1] # Nelly
names[2] # Jimmy
names[3] # Lenny
```

You can also use negative indexing to access items inside lists in Python.

To access the **last** item, you use the index value of -1. To acces the second to last item, you use the index value of -2.

Here is how you would access each item inside a list using negative indexing:

```python
names = ["Kelly", "Nelly", "Jimmy", "Lenny"]

names[-4] # Kelly
names[-3]# Nelly
names[-2] # Jimmy
names[-1] # Lenny
```

## Why does the `Indexerror: list index out of range` error occur in Python?

### Using an index number that is out of the range of the list

You'll get the `Indexerror: list index out of range` error when you try and access an item using a value that is out of the index range of the list and does not exist.

This is quite common when you try to access the last item of a list, or the first one if you're using negative indexing.

Let's go back to the list we've used so far.

```python
names = ["Kelly", "Nelly", "Jimmy", "Lenny"]
```

Say I want to access the last item, "Lenny", and try to do so by using the following code:

```python
print(names[4])

#output

#Traceback (most recent call last):
#  File "/Users/dionysialemonaki/python_articles/demo.py", line 3, in <module>
#    print(names[4])
#IndexError: list index out of range
```

Generally, the index range of a list is `0 to n-1`, with `n` being the total number of values in the list.

With the total values of the list above being `4`, the index range is `0 to 3`. 

Now, let's try to access an item using negative indexing.

Say I want to access the first item in the list, "Kelly", by using negative indexing.

```python
names = ["Kelly", "Nelly", "Jimmy", "Lenny"]

print(names[-5])

#output

#Traceback (most recent call last):
#  File "/Users/dionysialemonaki/python_articles/demo.py", line 3, in <module>
#    print(names[-5])
#IndexError: list index out of range
```

When using negative indexing, the index range of a list is `-1 to -n`, where `-n` the total number of items contained in the list.

With the total number of items in the list being `4`, the index range is `-1 to -4`.

### Using the wrong value in the `range()` function in a Python `for` loop

You'll get the `Indexerror: list index out of range` error when iterating through a list and trying to access an item that doesn't exist.

One common instance where this can occur is when you use the wrong integer in Python's  `range()` function.

The `range()` function typically takes in one integer number, which indicates where the counting will stop.

For example, `range(5)` indicates that the counting will start from `0` and end at `4`. 

So, by default, the counting starts at position `0`, is incremented by `1` each time, and the number is up to – but not including – the position where the counting will stop.

Let's take the following example:

```python
names = ["Kelly", "Nelly", "Jimmy", "Lenny"]

for name in range(5):
    print(names[name])
    
#output

#Kelly
#Nelly
#Jimmy
#Lenny
#Traceback (most recent call last):
#  File "/Users/dionysialemonaki/python_articles/demo.py", line 7, in <module>
#   print(names[name])
#IndexError: list index out of range
```

Here, the list `names` has four values.

I wanted to loop through the list and print out each value. 

When I used `range(5)` I was telling the Python interpreter to print the values that are at the positions `0 to 4`.

However, there is no item in position 4.

You can see this by first printing out the number of the position and *then* the value at that position.

```python
#0
#Kelly
#1
#Nelly
#2
#Jimmy
#3
#Lenny
#4
#Traceback (most recent call last):
#  File "/Users/dionysialemonaki/python_articles/demo.py", line 8, in <module>
#    print(names[name])
#IndexError: list index out of range
```

You see that at position `0` is "Kelly", at position `1` is "Nelly", at position `2` is "Jimmy" and at position `3` is "Lenny".

When it comes to position four, which was specified with `range(5)` which indicates positions of `0 to 4`, there is nothing to print out and therefore the interpreter throws an error.

One way to fix this is to lower the integer in `range()`:

```python
names = ["Kelly", "Nelly", "Jimmy", "Lenny"]

for name in range(4):
    print(name)
    print(names[name])
    
#output

#0
#Kelly
#1
#Nelly
#2
#Jimmy
#3
#Lenny
```

Another way to fix this when using a `for` loop is to pass the length of the list as an argument to the `range()` function. You do this by using the `len()` built-in Python function, as shown in an earlier section:

```python
names = ["Kelly", "Nelly", "Jimmy", "Lenny"]

for name in range(len(names)):
    print(names[name])

#output

#Kelly
#Nelly
#Jimmy
#Lenny
```

When passing `len()` as an argument to `range()`, make sure that you **don't** make the following mistake:

```python
names = ["Kelly", "Nelly", "Jimmy", "Lenny"]

for name in range(len(names) + 1):
    print(names[name])
```

After running the code, you'll again get an `IndexError: list index out of range` error:

```python
#Kelly
#Nelly
#Jimmy
#Lenny
#Traceback (most recent call last):
#  File "/Users/dionysialemonaki/python_articles/demo.py", line 4, in <module>
#    print(names[name])
#IndexError: list index out of range
```

## Conclusion

Hopefully this article gave you some insight into why the `IndexError: list index out of range` error occurs and some ways you can avoid it.

If you want to learn more about Python, check out freeCodeCamp's [Python Certification](https://www.freecodecamp.org/learn/scientific-computing-with-python/). You'll start learning in an interacitve and beginner-friendly way. You'll also build five projects at the end to put into practice and help reinforce what you learned.

Thanks for reading and happy coding!


