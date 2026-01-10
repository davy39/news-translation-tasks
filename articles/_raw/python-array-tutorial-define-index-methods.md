---
title: Python Array Tutorial – Define, Index, Methods
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-01-31T18:35:31.000Z'
originalURL: https://freecodecamp.org/news/python-array-tutorial-define-index-methods
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/sergey-zolkin-_UeY8aTI6d0-unsplash.jpg
tags:
- name: arrays
  slug: arrays
- name: Python
  slug: python
seo_title: null
seo_desc: 'In this article, you''ll learn how to use Python arrays. You''ll see how
  to define them and the different methods commonly used for performing operations
  on them.

  The article covers arrays that you create by importing the array module. We won''t
  cover N...'
---

In this article, you'll learn how to use Python arrays. You'll see how to define them and the different methods commonly used for performing operations on them.

The article covers arrays that you create by importing the `array module`. We won't cover NumPy arrays here.

## Table of Contents

1. [Introduction to Arrays](#introduction)
    1. [The differences between Lists and Arrays](#differences)
    2. [When to use arrays](#usage1)
2. [How to use arrays](#usage2)
    1.  [ Define arrays](#define)
    2.  [ Find the length of arrays](#length)
    3.  [Array indexing](#indexing)
    4.  [Search through arrays](#search)
    5.  [Loop through arrays](#loop)
    6.  [Slice an array](#slice)
3. [Array methods for performing operations](#methods)
    1.  [Change an existing value](#change)
    2.  [Add a new value](#addition)
    3.  [Remove a value](#remove)
4. [Conclusion](#conclusion)


Let's get started!

## What are Python Arrays? <a name="introduction"></a>

Arrays are a fundamental data structure, and an important part of most programming languages. In Python, they are containers which are able to store more than one item at the same time.

Specifically, they are an ordered collection of elements with every value being of the same data type. That is the most important thing to remember about Python arrays - the fact that they can only hold a sequence of multiple items that are of the same type.


### What's the Difference between Python Lists and Python Arrays? <a name="differences"></a>

Lists are one of the most common data structures in Python, and a core part of the language. 

Lists and arrays behave similarly.

Just like arrays, lists are an ordered sequence of elements.

They are also mutable and not fixed in size, which means they can grow and shrink throughout the life of the program. Items can be added and removed, making them very flexible to work with.

However, lists and arrays are **not** the same thing.

**Lists** store items that are of **various data types**. This means that a list can contain integers, floating point numbers, strings, or any other Python data type, at the same time. That is not the case with arrays.

As mentioned in the section above, **arrays** store only items that are of the **same single data type**. There are arrays that contain only integers, or only floating point numbers, or only any other Python data type you want to use.

### When to Use Python Arrays <a name="usage1"></a>

Lists are built into the Python programming language, whereas arrays aren't. Arrays are not a built-in data structure, and therefore need to be imported via the `array module` in order to be used.

Arrays of the `array module` are a thin wrapper over C arrays, and are useful when you want to work with homogeneous data.

They are also more compact and take up less memory and space which makes them more size efficient compared to lists.

If you want to perform mathematical calculations, then you should use NumPy arrays by importing the NumPy package. Besides that, you should just use Python arrays when you really need to, as lists work in a similar way and are more flexible to work with.

## How to Use Arrays in Python <a name="usage2"></a>

In order to create Python arrays, you'll first have to import the `array module` which contains all the necessary functions.

There are three ways you can import the `array module`:

1) By using `import array` at the top of the file. This includes the module `array`. You would then go on to create an array using `array.array()`.

```python
import array

#how you would create an array
array.array()
```

2) Instead of having to type `array.array()` all the time, you could use `import array as arr` at the top of the file, instead of `import array` alone. You would then create an array by typing `arr.array()`. The `arr` acts as an alias name, with the array constructor then immediately following it.

```python
import array as arr

#how you would create an array
arr.array()
```

3) Lastly, you could also use `from array import *`, with `*` importing all the functionalities available. You would then create an array by writing the `array()` constructor alone.

```python
from array import *

#how you would create an array
array()
```

### How to Define Arrays in Python <a name="define"></a>

Once you've imported the `array module`, you can then go on to define a Python array.

The general syntax for creating an array looks like this:

```python
variable_name = array(typecode,[elements])
```

Let's break it down:

- `variable_name` would be the name of the array.
- The `typecode` specifies what kind of elements would be stored in the array. Whether it would be an array of integers, an array of floats or an array of any other Python data type. Remember that all elements should be of the same data type.
- Inside square brackets you mention the `elements` that would be stored in the array, with each element being separated by a comma. You can also create an *empty* array by just writing `variable_name = array(typecode)` alone, without any elements.

Below is a typecode table, with the different typecodes that can be used with the different data types when defining Python arrays:

| Typecode      | C type | Python Type |Size |
| ----------- | ----------- |----------- |----------- |
| 'b'      | signed char   | int | 1 |
| 'B'  | unsigned char        | int | 1|
| 'u' | wchar_t | Unicode character | 2 |
| 'h' | signed short| int | 2 |
| 'H' | unsigned short | int| 2|
| 'i'| signed int| int| 2|
| 'I'| unsigned int| int| 2|
| 'l'| signed long | int| 4|
| 'L'| unsigned long| int| 4|
| 'q'|signed long long| int | 8|
|'Q'| unsigned long long| int| 8|
| 'f'| float| float| 4|
| 'd'| double| float| 8|

Tying everything together, here is an example of how you would define an array in Python:

```python
import array as arr 

numbers = arr.array('i',[10,20,30])


print(numbers)

#output

#array('i', [10, 20, 30])
```

Let's break it down:

- First we included the array module, in this case with `import array as arr `.
- Then, we created a `numbers` array.
- We used `arr.array()` because of `import array as arr `.
- Inside the `array()` constructor, we first included `i`, for signed integer. Signed integer means that the array can include positive *and* negative values. Unsigned integer, with `H` for example, would mean that no negative values are allowed. 
- Lastly, we included the values to be stored in the array in square brackets.

Keep in mind that if you tried to include values that were not of `i` typecode, meaning they were not integer values, you would get an error:

```python
import array as arr 

numbers = arr.array('i',[10.0,20,30])


print(numbers)

#output

#Traceback (most recent call last):
# File "/Users/dionysialemonaki/python_articles/demo.py", line 14, in <module>
#   numbers = arr.array('i',[10.0,20,30])
#TypeError: 'float' object cannot be interpreted as an integer
```

In the example above, I tried to include a floating point number in the array. I got an error because this is meant to be an integer array only.

Another way to create an array is the following:

```python
from array import *

#an array of floating point values
numbers = array('d',[10.0,20.0,30.0])

print(numbers)

#output

#array('d', [10.0, 20.0, 30.0])
```

The example above imported the `array module` via `from array import *` and created an array `numbers` of float data type. This means that it holds only floating point numbers, which is specified with the `'d'` typecode.

### How to Find the Length of an Array in Python <a name="length"></a>

To find out the exact number of elements contained in an array, use the built-in `len()` method.

It will return the integer number that is equal to the total number of elements in the array you specify.

```python
import array as arr 

numbers = arr.array('i',[10,20,30])


print(len(numbers))

#output
# 3
```

In the example above, the array contained three elements – `10, 20, 30` – so the length of `numbers` is `3`.

### Array Indexing and How to Access Individual Items in an Array in Python <a name="indexing"></a>

Each item in an array has a specific address. Individual items are accessed  by referencing their *index number*.

Indexing in Python, and in all programming languages and computing in general, starts at `0`. It is important to remember that counting starts at `0` and **not** at `1`.

To access an element, you first write the name of the array followed by square brackets. Inside the square brackets you include the item's index number.

The general syntax would look something like this:

```python
array_name[index_value_of_item]
```

Here is how you would access each individual element in an array:

```python
import array as arr 

numbers = arr.array('i',[10,20,30])

print(numbers[0]) # gets the 1st element
print(numbers[1]) # gets the 2nd element
print(numbers[2]) # gets the 3rd element

#output

#10
#20
#30
```

Remember that the index value of the last element of an array is always one less than the length of the array. Where `n` is the length of the array, `n - 1` will be the index value of the last item.

Note that you can also access each individual element using negative indexing.

With negative indexing, the last element would have an index of `-1`, the second to last element would have an index of `-2`, and so on.

Here is how you would get each item in an array using that method:

```python
import array as arr 

numbers = arr.array('i',[10,20,30])

print(numbers[-1]) #gets last item
print(numbers[-2]) #gets second to last item
print(numbers[-3]) #gets first item
 
#output

#30
#20
#10
```

### How to Search Through an Array in Python <a name="search"></a>

You can find out an element's index number by using the `index()` method. 

You pass the value of the element being searched as the argument to the method, and the element's index number is returned.

```python
import array as arr 

numbers = arr.array('i',[10,20,30])

#search for the index of the value 10
print(numbers.index(10))

#output

#0
```

If there is more than one element with the same value, the index of the first instance of the value will be returned:

```python
import array as arr 


numbers = arr.array('i',[10,20,30,10,20,30])

#search for the index of the value 10
#will return the index number of the first instance of the value 10
print(numbers.index(10))

#output

#0
```

### How to Loop through an Array in Python <a name="loop"></a>

You've seen how to access each individual element in an array and print it out on its own.

You've also seen how to print the array, using the `print()` method. That method gives the following result:

```python
import array as arr 

numbers = arr.array('i',[10,20,30])

print(numbers)

#output

#array('i', [10, 20, 30])
```

What if you want to print each value one by one?

This is where a loop comes in handy. You can loop through the array and print out each value, one-by-one, with each loop iteration.

For this you can use a simple `for` loop:

```python
import array as arr 

numbers = arr.array('i',[10,20,30])

for number in numbers:
    print(number)
    
#output
#10
#20
#30
```

You could also use the `range()` function, and pass the `len()` method as its parameter. This would give the same result as above:

```python
import array as arr  

values = arr.array('i',[10,20,30])

#prints each individual value in the array
for value in range(len(values)):
    print(values[value])

#output

#10
#20
#30
```

### How to Slice an Array in Python <a name="slice"></a>

To access a specific range of values inside the array, use the slicing operator, which is a colon `:`.

When using the slicing operator and you only include one value, the counting starts from `0` by default. It gets the first item, and goes up to but not including the index number you specify.

```python

import array as arr 

#original array
numbers = arr.array('i',[10,20,30])

#get the values 10 and 20 only
print(numbers[:2])  #first to second position

#output

#array('i', [10, 20])
```

When you pass two numbers as arguments, you specify a range of numbers. In this case, the counting starts at the position of the first number in the range, and up to but not including the second one:

```python
import array as arr 

#original array
numbers = arr.array('i',[10,20,30])


#get the values 20 and 30 only
print(numbers[1:3]) #second to third position

#output

#array('i', [20, 30])
```

## Methods For Performing Operations on Arrays in Python <a name="methods"></a>

Arrays are mutable, which means they are changeable. You can change the value of the different items, add new ones, or remove any you don't want in your program anymore.

Let's see some of the most commonly used methods which are used for performing operations on arrays.

### How to Change the Value of an Item in an Array <a name="change"></a>

You can change the value of a specific element by speficying its position and assigning it a new value:

```python
import array as arr 

#original array
numbers = arr.array('i',[10,20,30])

#change the first element
#change it from having a value of 10 to having a value of 40
numbers[0] = 40

print(numbers)

#output

#array('i', [40, 20, 30])
```

### How to Add a New Value to an Array <a name="addition"></a>

To add one single value at the end of an array, use the `append()` method:

```python
import array as arr 

#original array
numbers = arr.array('i',[10,20,30])

#add the integer 40 to the end of numbers
numbers.append(40)

print(numbers)

#output

#array('i', [10, 20, 30, 40])
```

Be aware that the new item you add needs to be the same data type as the rest of the items in the array. 

Look what happens when I try to add a float to an array of integers:

```python
import array as arr 

#original array
numbers = arr.array('i',[10,20,30])

#add the float 40.0 to the end of numbers
numbers.append(40.0)

print(numbers)

#output

#Traceback (most recent call last):
#  File "/Users/dionysialemonaki/python_articles/demo.py", line 19, in <module>
#   numbers.append(40.0)
#TypeError: 'float' object cannot be interpreted as an integer
```


But what if you want to add more than one value to the end an array?

Use the `extend()` method, which takes an iterable (such as a list of items) as an argument. Again, make sure that the new items are all the same data type.

```python
import array as arr 

#original array
numbers = arr.array('i',[10,20,30])

#add the integers 40,50,60 to the end of numbers
#The numbers need to be enclosed in square brackets

numbers.extend([40,50,60])

print(numbers)

#output

#array('i', [10, 20, 30, 40, 50, 60])
```

And what if you don't want to add an item to the end of an array? Use the `insert()` method, to add an item at a specific position.

The `insert()` function takes two arguments: the index number of the position the new element will be inserted, and the value of the new element.

```python
import array as arr 

#original array
numbers = arr.array('i',[10,20,30])

#add the integer 40 in the first position
#remember indexing starts at 0

numbers.insert(0,40)

print(numbers)

#output

#array('i', [40, 10, 20, 30])
```

### How to Remove a Value from an Array <a name="remove"></a>

To remove an element from an array, use the `remove()` method and include the value as an argument to the method. 

```python
import array as arr 

#original array
numbers = arr.array('i',[10,20,30])

numbers.remove(10)

print(numbers)

#output

#array('i', [20, 30])
```

With `remove()`, only the first instance of the value you pass as an argument will be removed.

See what happens when there are more than one identical values:

```python

import array as arr 

#original array
numbers = arr.array('i',[10,20,30,10,20])

numbers.remove(10)

print(numbers)

#output

#array('i', [20, 30, 10, 20])
```

Only the first occurence of `10` is removed.

You can also use the `pop()` method, and specify the position of the element to be removed:

```python
import array as arr 

#original array
numbers = arr.array('i',[10,20,30,10,20])

#remove the first instance of 10
numbers.pop(0)

print(numbers)

#output

#array('i', [20, 30, 10, 20])
```

## Conclusion <a name="conclusion"></a>

And there you have it - you now know the basics of how to create arrays in Python using the `array module`. Hopefully you found this guide helpful.

To learn more about Python, check out [freeCodeCamp's Scientific Computing with Python Certification](https://www.freecodecamp.org/learn/scientific-computing-with-python/).

You'll start from the basics and learn in an interactive and beginner-friendly way. You'll also build five projects at the end to put into practice and help reinforce what you learned.

Thanks for reading and happy coding!

References: [Python documentation](https://docs.python.org/3/library/array.html)






