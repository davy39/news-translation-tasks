---
title: Python List Append VS Python List Extend – The Difference Explained with Array
  Method Examples
subtitle: ''
author: Estefania Cassingena Navone
co_authors: []
series: null
date: '2020-03-22T23:27:00.000Z'
originalURL: https://freecodecamp.org/news/python-list-append-vs-python-list-extend
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/Image---Append-vs-Extend-1.png
tags:
- name: Python
  slug: python
- name: Tutorial
  slug: tutorial
seo_title: null
seo_desc: "\U0001F539 Welcome\nIf you want to learn how to work with .append() and\
  \ .extend() and understand their differences, then you have come to the right place.\
  \ They are powerful list methods that you will definitely use in your Python projects.\n\
  \ In this article, y..."
---

## 🔹 Welcome

If you want to learn how to work with `.append()` and `.extend()` and understand their differences, then you have come to the right place. They are powerful list methods that you will definitely use in your Python projects.

 In this article, you will learn:

* How and when to use the `.append()` method.
* How and when to use the `.extend()` method. 
* Their main differences. 

Let's begin. ✨

## 🔸 Append

Let's see how the `.append()` method works behind the scenes.

### Use Cases

You should use this method when you want to **add a single item to the end** of a list.

**💡 Tips:** You can add items of any data type since lists can have elements of different data types.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-105.png)

### Syntax and Arguments

To call the `.append()` method, you will need to use this syntax:

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-104.png)

**From Left to Right:**

* The list that will be modified. This is usually a variable that references a list. 
* A dot, followed by the name of the method `.append()`. 
* Within parentheses, the item that will be added to the end of the list. 

💡 **Tips:** The dot is very important. This is called "dot notation". The dot basically says "call this method on this particular list", so the effect of the method will be applied to the list that is located before the dot. 

### Examples

Here's an example of how to use `.append()`:

```python
# Define the list
>>> nums = [1, 2, 3, 4]

# Add the integer 5 to the end of the existing list
>>> nums.append(5)

# See the updated value of the list
>>> nums
[1, 2, 3, 4, 5]
```

💡 **Tips:** When you use `.append()` the original list is modified. The method does not create a copy of the list – it mutates the original list in memory. 

Let's pretend that we are conducting a research and that we want to analyze the data collected using Python. We need to add a new measurement to the existing list of values. 

How do we do it? We use the `.append()` method! 

You can see it right here:

```python
# Existing list
>>> nums = [5.6, 7.44, 6.75, 4.56, 2.3]

# Add the float (decimal number) to the end of the existing list
>>> nums.append(7.34)

# See the updated value of the list
>>> nums
[5.6, 7.44, 6.75, 4.56, 2.3, 7.34]
```

### Equivalent to...

If you are familiar with string, list, or tuple slicing, what `.append()` really does behind the scenes is equivalent to:

```python
a[len(a):] = [x]
```

With this example, you can see that they are equivalent. 

Using `.append()`:

```python
>>> nums = [5.6, 7.44, 6.75, 4.56, 2.3]
>>> nums.append(4.52)
>>> nums
[5.6, 7.44, 6.75, 4.56, 2.3, 4.52]
```

Using list slicing:

```python
>>> nums = [5.6, 7.44, 6.75, 4.56, 2.3]
>>> nums[len(nums):] = [4.52]
>>> nums
[5.6, 7.44, 6.75, 4.56, 2.3, 4.52]
```

### Appending a Sequence

Now, what do you think about this example? What do you think will be output?

```python
>>> nums = [5.6, 7.44, 6.75, 4.56, 2.3]
>>> nums.append([5.67, 7.67, 3.44])
>>> nums
# OUTPUT?
```

Are you ready? This will be the output:

```python
[5.6, 7.44, 6.75, 4.56, 2.3, [5.67, 7.67, 3.44]]
```

You might be asking, why was the full list added as a single item? It's because the `.append()` method adds the entire item to the end of the list. If the item is a sequence such as a list, dictionary, or tuple, the entire sequence will be added as a single item of the existing list.

Here we have another example (below). In this case, the item is a tuple and it is added as a single item of the list, not as individual items:

```python
>>> names = ["Lulu", "Nora", "Gino", "Bryan"]
>>> names.append(("Emily", "John"))
>>> names
['Lulu', 'Nora', 'Gino', 'Bryan', ('Emily', 'John')]
```

## 🔹 Extend

Now let's dive into the functionality of the `.extend()` method. 

### Use Cases

You should use this method if you need to **append several items to a list as individual items**. 

Let me illustrate the importance of this method with a familiar friend that you just learned: the `.append()` method. Based on what you've learned so far, if we wanted to add several **individual** items to a list using `.append()`, we would need to use `.append()` several times, like this:

```python
# List that we want to modify
>>> nums = [5.6, 7.44, 6.75, 4.56, 2.3]

# Appending the items
>>> nums.append(2.3)
>>> nums.append(9.6)
>>> nums.append(4.564)
>>> nums.append(7.56)

# Updated list
>>> nums
[5.6, 7.44, 6.75, 4.56, 2.3, 2.3, 9.6, 4.564, 7.56]
```

I'm sure that you are probably thinking that this would not be very efficient, right? What if I need to add thousands or millions of values? I cannot write thousands or millions of lines for this simple task. That would take forever!

So let's see an alternative. We can store the values that we want to add in a separate list and then use a for loop to call `.append()` as many times as needed:

```python
# List that we want to modify
>>> nums = [5.6, 7.44, 6.75, 4.56, 2.3]

# Values that we want to add
>>> new_values = [2.3, 9.6, 4.564, 7.56]

# For loop that is going to append the value
>>> for num in new_values:
	nums.append(num)

# Updated value of the list
>>> nums
[5.6, 7.44, 6.75, 4.56, 2.3, 2.3, 9.6, 4.564, 7.56]
```

This is more efficient, right? We are only writing a few lines. But there is an even more efficient, readable, and compact way to achieve the same purpose: `.extend()`!

```python
>>> nums = [5.6, 7.44, 6.75, 4.56, 2.3]
>>> new_values = [2.3, 9.6, 4.564, 7.56]

# This is where the magic occurs! No more for loops
>>> nums.extend(new_values)

# The list was updated with individual values
>>> nums
[5.6, 7.44, 6.75, 4.56, 2.3, 2.3, 9.6, 4.564, 7.56]
```

Let's see how this method works behind the scenes. 

### Syntax and Arguments

To call the `.extend()` method, you will need to use this syntax:

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-110.png)

**From Left to Right:**

* The list that will be modified. This is usually a variable that refers to the list.
* A dot `.` (So far, everything is exactly the same as before).
* The name of the method `extend`. (Now things start to change...).
* Within parentheses, an **iterable** (list, tuple, dictionary, set, or string) that contains the items that will be added as individual elements of the list.

**💡 Tips:** According to the [Python documentation](https://docs.python.org/3/glossary.html), an iterable is defined as "an object capable of returning its members one at a time". Iterables can be used in a for loop and because they return their elements one at a time, we can "do something" with each one of them, one per iteration.

### Behind the Scenes

Let's see how `.extend()` works behind the scenes. Here we have an example:

```python
# List that will be modified
>>> a = [1, 2, 3, 4]

# Sequence of values that we want to add to the list a
>>> b = [5, 6, 7]

# Calling .extend()
>>> a.extend(b)

# See the updated list. Now the list a has the values 5, 6, and 7
>>> a
[1, 2, 3, 4, 5, 6, 7]
```

You can think of `.extend()` as a method that appends the individual elements of the iterable in the same order as they appear.

In this case, we have a list `a = [1, 2, 3, 4]` as illustrated in the diagram below. We also have a list `b = [5, 6, 7]` that contains the sequence of values that we want to add. The method takes each element of `b` and appends it to list `a` in the same order.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-106.png)
_Step 1. First element is appended._

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-107.png)
_Step 2. Second element appended._

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-108.png)
_Step 3. Third element appended_

After this process is completed, we have the updated list `a` and we can work with the values as individual elements of `a`. 

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-109.png)

💡 **Tips:** The list `b` used to extend list `a` remains intact after this process. You can work with it after the call to `.extend()`. Here is the proof:

```python
>>> a = [1, 2, 3, 4]
>>> b = [5, 6, 7]
>>> a.extend(b)
>>> a
[1, 2, 3, 4, 5, 6, 7]

# List b is intact!
>>> b
[5, 6, 7]
```

### Examples

You may be curious to know how the `.extend()` method works when you pass different types of iterables. Let's see how in the following examples:

**For tuples:**  
The process works exactly the same if you pass a tuple. The individual elements of the tuple are appended one by one in the order that they appear. 

```python
# List that will be extended
>>> a = [1, 2, 3, 4]

# Values that will be added (the iterable is a tuple!)
>>> b = (1, 2, 3, 4)

# Method call
>>> a.extend(b)

# The value of the list a was updated
>>> a
[1, 2, 3, 4, 1, 2, 3, 4]
```

**For sets:**  
The same occurs if you pass a set. The elements of the set are appended one by one.

```python
# List that will be extended
>>> a = [1, 2, 3, 4]

# Values that will be appended (the iterable is a set!)
>>> c = {5, 6, 7}

# Method call
>>> a.extend(c)

# The value of a was updated
>>> a
[1, 2, 3, 4, 5, 6, 7]
```

**For strings:**  
Strings work a little bit different with the `.extend()` method. Each character of the string is considered an "item", so the characters are appended one by one in the order that they appear in the string. 

```python
# List that will be extended
>>> a = ["a", "b", "c"]

# String that will be used to extend the list
>>> b = "Hello, World!"

# Method call
>>> a.extend(b)

# The value of a was updated
>>> a
['a', 'b', 'c', 'H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!']
```

**For dictionaries:**  
Dictionaries have a particular behavior when you pass them as arguments to `.extend()`. In this case, the **keys** of the dictionary are appended one by one. The values of the corresponding key-value pairs are not appended. 

In this example (below), the keys are "d", "e", and "f". These values are appended to the list `a`. 

```python
# List that will be extended
>>> a = ["a", "b", "c"]

# Dictionary that will be used to extend the list
>>> b = {"d": 5, "e": 6, "f": 7}

# Method call
>>> a.extend(b)

# The value of a was updated
>>> a
['a', 'b', 'c', 'd', 'e', 'f']
```

### Equivalent to...

What `.extend()` does is equivalent to `a[len(a):] = iterable`. Here we have an example to illustrate that they are equivalent:

Using `.extend()`:

```
# List that will be extended
>>> a = [1, 2, 3, 4]

# Values that will be appended
>>> b = (6, 7, 8)

# Method call
>>> a.extend(b)

# The list was updated
>>> a
[1, 2, 3, 4, 6, 7, 8]

```

Using list slicing:

```python
# List that will be extended
>>> a = [1, 2, 3, 4]

# Values that will be appended
>>> b = (6, 7, 8)

# Assignment statement. Assign the iterable b as the final portion of the list a
>>> a[len(a):] = b

# The value of a was updated
>>> a
[1, 2, 3, 4, 6, 7, 8]
```

The result is the same, but using `.extend()` is much more readable and compact, right? Python truly offers amazing tools to improve our workflow. 

## 🔸 Summary of their Differences

Now that you know how to work with `.append()` and `.extend()`, let's see a summary of their key differences:

* **Effect**: `.append()` adds a single element to the end of the list while `.extend()` can add multiple individual elements to the end of the list.
* **Argument**: `.append()` takes a single element as argument while `.extend()` takes an iterable as argument (list, tuple, dictionaries, sets, strings).

**I really hope that you liked my article and found it helpful.** Now you can work with `.append()` and `.extend()` in your Python projects. [Check out my online courses](https://www.udemy.com/user/estefania-cn/). Follow me on [Twitter](https://twitter.com/EstefaniaCassN). ⭐️

