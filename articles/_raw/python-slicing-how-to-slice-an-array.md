---
title: Python Slicing – How to Slice an Array and What Does [::-1] Mean?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-12-08T19:13:33.000Z'
originalURL: https://freecodecamp.org/news/python-slicing-how-to-slice-an-array
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/10.-slide-array.png
tags:
- name: arrays
  slug: arrays
- name: Python
  slug: python
seo_title: null
seo_desc: 'By Dillion Megida

  Slicing an array is the concept of cutting out – or slicing out – a part of the
  array. How do you do this in Python? I''ll show you how in this article.

  If you like watching video content to supplement your reading, here''s a video ve...'
---

By Dillion Megida

Slicing an array is the concept of cutting out – or slicing out – a part of the array. How do you do this in Python? I'll show you how in this article.

If you like watching video content to supplement your reading, here's a [video version](https://www.youtube.com/watch?v=sgXInOpc4Iw) of this article as well.


## What is an Array?

An array is a data structure that allows you to store multiple items **of the same data type** in order in a variable at the same time. You can access each of these items by their index (location in the order).

They are a bit similar to lists in Python, it's just that lists allow you to store multiple items **of different data types**. Also, while lists are built-in, arrays aren't.

## How to Access Values in an Array in Python

Here's the syntax to create an array in Python:

```python
import array as arr 

numbers = arr.array(typecode, [values])
```

As the array data type is not built into Python by default, you have to import it from the `array` module. We import this module as `arr`.

Using the `array` method of `arr`, we can create an array by specifying a `typecode` (data type of the values) and the values stored in the array. 

Here's a table showing the acceptable typecodes:

| Typecode  | C Type              | Python Type       | Bytes Size  |
| --------- | ------------------- | ----------------- | ----------- |
| 'b'       | signed char         | int               | 1           |
| 'B'       | unsigned char       | int               | 1           |
| 'u'       | wchar_t             | Unicode character | 2           |
| 'h'       | signed short        | int               | 2           |
| 'H'       | unsigned short      | int               | 2           |
| 'i'       | signed int          | int               | 2           |
| 'I'       | unsigned int        | int               | 2           |
| 'l'       | signed long         | int               | 4           |
| 'L'       | unsigned long       | int               | 4           |
| 'q'       | signed long long    | int               | 8           |
| 'Q'       | unsigned long long  | int               | 8           |
| 'f'       | float               | float             | 4           |
| 'd'       | double              | float             | 8           |


Typecodes gotten from [the Python documentation](https://docs.python.org/3/library/array.html).

Here's an example array in Python:

```python
import array as arr 

numbers = arr.array('i', [1, 2, 3, 4, 5])

print(numbers[1])
# 2
```

We created an array of integer values from 1 to 5 here. We also accessed the second value by using square brackets and its index in the order, which is **1**.

## How to Slice an Array in Python

Let's say you want to slice a portion of this array and assign the slice to another variable. You can do it using colons and square brackets. The syntax looks like this:

```python
array[start:stop:step]
```

The `start` index specifies the index that the slicing starts from. The default is **0**.

The `end` index specifies the index where the slicing ends (but excluding the value at this index). The default is the length of the array.

The `step` argument specifies the step of the slicing. The default is **1**.

Let's see some examples that cover different ways in which arrays can be sliced.


### How to slice without a start or end index

When you slice without a `start` or `end` index, you basically get a whole copy of the array:

```python
import array as arr 

numbers = arr.array('i', [1, 2, 3, 4, 5])

copy = numbers[:]

print(copy)
# array('i', [1, 2, 3, 4, 5])
```

As you can see here, we have a copy of the `numbers` array.

> It's also worth noting that the slicing action does not affect the original array. With slicing, you only "copy a portion" of the original array.

### How to slice with a start index

For example, if you want to slice an array from a specific start value to the end of the array, here's how:

```python
import array as arr 

numbers = arr.array('i', [1, 2, 3, 4, 5])

copy = numbers[2:]

print(copy)
# array('i', [3, 4, 5])
```

By passing `2:` in the square brackets, the slicing starts from index **2** (which holds value 3) up until the end of the array, as you can see in the results.

### How to slice with an end index

For example, if you want to slice an array from the first value to the third, here's how:

```python
import array as arr 

numbers = arr.array('i', [1, 2, 3, 4, 5])

copy = numbers[:3]

print(copy)
# array('i', [1, 2, 3])
```

By passing `:3` in the square brackets, slicing starts from the **0** index (by default, since not specified) up until the third index we specified.

As mentioned earlier, the slicing excludes the value at the third index. So in the results, as you find in the `copy` variable, the values returned are from index **0** through index **2**.

### How to slice with a start and end index

What if you want to specify the starting and ending points of the slicing? Here's how:

```python
import array as arr 

numbers = arr.array('i', [1, 2, 3, 4, 5])

copy = numbers[1:4]

print(copy)
# array('i', [2, 3, 4])
```

By using a number, then a colon, followed by a number in square brackets, you can specify a starting and ending indexes, respectively. 

In our case, we used **1** and **4** as in `[1:4]`. From the results, you see that the slicing starts from the value at index **1** which is `2`, up until the value before the index **4**, which is `4` (at index 3).

### How to slice with steps

When you specify a `start` and `end` index of 1 and 5, respectively, slicing will select values at index **1**, index **2** (1 increment to the previous index), index **3** (1 increment to the previous index) and index **4** (and one increment to the previous index). 

In this slicing, a step of **1** is used by default. But you can provide a different step. Here's how:

```python
import array as arr 

numbers = arr.array('i', [1, 2, 3, 4, 5])

copy = numbers[1:4:2]

print(copy)
# array('i', [2, 4])
```

By adding another colon, you can specify a step. So we have `[start:stop:step]`. 

In our example, the start is **1**, the end is **4** and the step is 2. Slicing starts from the value at index 1 which is **2**, then the next value will be at the previous index plus the step, which is `1 + 2` equals 3. The value at index 3 is **4** so that is added to the slice. The next index will be 5 (`3 + 2`) but since 5 exceeds the stop index, it will not be added to the slice.

As you can see in the code, the sliced copy is just 2 and 4.

### How to slice with negative start and end indexes

The `start` or `stop` indexes can also be negative. Negative indexes count from the end of the array. This means a negative index is the last value in an array:

```python
import array as arr 

numbers = arr.array('i', [1, 2, 3, 4, 5])

print(numbers[-1])
# 5
```

By using a negative 1 here, you see that **5** is returned, which is from the end of an array.

With a slice expression like `[-3:-1]`, this means a start index of **-3** and end index of **-1**. Let's see how that works with our array:

```python
import array as arr 

numbers = arr.array('i', [1, 2, 3, 4, 5])

copy = numbers[-3:-1]

print(copy)
# array('i', [3, 4])
```

The slice starts from index **-3** (which is the third value from the end of the array, that is 3) and stops at index **-1** (which is the last value in the array, that is 5). Slicing doesn't include the last value so we have 3 and 4.

> Combining a negative `start` index and a positive `end` index (or vice versa) will not work as you'll be going different directions at once.

### How to slice with negative steps

You can use negative steps, which means the steps decrement for the slicing. Here's an example:

```python
import array as arr 

numbers = arr.array('i', [1, 2, 3, 4, 5])

copy = numbers[2::-1]

print(copy)
# array('i', [3, 2, 1])
```

Here, we specify a start of index **2**, no end, and a step of **-1**. Slicing here will start from index **2** which is 3. The negative steps mean the next value in the slice will be at an index smaller than the previous index by 1. This means `2 - 1` which is **1** so the value at this index, which is 2 will be added to the slice. 

This goes on reversed until it gets to the end of the array which is index **0**. The sliced array results in values of 3, 2, and 1.

### What does `[::-1]` mean?

Have you seen this expression anywhere in Python before? Well, here's what it means: there's no `start` index specified, nor an `end` index, only a negative step of **-1**. 

The `start` index defaults to **0**, so by using **-1** step, the slicing will contain values at the following indexes: **-1** (`0 - 1`), **-2** (`-1 - 1`), **-3** (`-2 - 1`), **-4** (`-3 - 1`) and **-5** (`-4 - 1`). Pretty much a reversed copy of the array.

Here's the code for it:

```python
import array as arr 

numbers = arr.array('i', [1, 2, 3, 4, 5])

copy = numbers[::-1]

print(copy)
# array('i', [5, 4, 3, 2, 1])
```

As you can see, this is a simple way to reverse an array.

## Wrapping Up

In this article, we've briefly looked at how to declare arrays in Python, how to access values in an array, and also how to cut – or slice – a part of an array using a colon and square brackets. 

We also learned how slicing works with steps and positive/negative start and stop indexes.

You can learn more about arrays here: [Python Array Tutorial – Define, Index, Methods](https://www.freecodecamp.org/news/python-array-tutorial-define-index-methods).


