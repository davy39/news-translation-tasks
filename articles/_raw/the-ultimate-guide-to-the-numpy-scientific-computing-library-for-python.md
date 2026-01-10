---
title: The Ultimate Guide to the NumPy Package for Scientific Computing in Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-06T17:18:57.000Z'
originalURL: https://freecodecamp.org/news/the-ultimate-guide-to-the-numpy-scientific-computing-library-for-python
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/numpy.png
tags:
- name: numpy
  slug: numpy
- name: Python
  slug: python
seo_title: null
seo_desc: 'By Nick McCullum

  NumPy (pronounced "numb pie") is one of the most important packages to grasp when
  you’re starting to learn Python.

  The package is known for a very useful data structure called the NumPy array. NumPy
  also allows Python developers to q...'
---

By Nick McCullum

NumPy (pronounced "numb pie") is one of the most important packages to grasp when you’re starting to [learn Python](https://courses.nickmccullum.com/courses/enroll/python-for-finance/).

The package is known for a very useful data structure called the NumPy array. NumPy also allows Python developers to quickly perform a wide variety of numerical computations.

This tutorial will teach you the fundamentals of NumPy that you can use to build numerical Python applications today.

## **Table of Contents**

You can skip to a specific section of this NumPy tutorial using the table of contents below:

* [Introduction to NumPy](#heading-introduction-to-numpy)
* [NumPy Arrays](#heading-numpy-arrays)
* [NumPy Methods and Operations](#heading-numpy-methods-and-operations)
* [NumPy Indexing and Assignment](#heading-numpy-indexing-and-assignment)
* [Final Thoughts & Special Offer](#heading-final-thoughts-amp-special-offer)

## **Introduction to NumPy**

In this section, we will introduce the [NumPy library](https://nickmccullum.com/advanced-python/numpy/) in Python.

### **What is NumPy?**

NumPy is a Python library for scientific computing. NumPy stand for Numerical Python. Here is the official description of the library from [its website](https://numpy.org/):

_“NumPy is the fundamental package for scientific computing with Python. It contains among other things:_

* _a powerful N-dimensional array object_
* _sophisticated (broadcasting) functions_
* _tools for integrating C/C++ and Fortran code_
* _useful linear algebra, Fourier transform, and random number capabilities_

_Besides its obvious scientific uses, NumPy can also be used as an efficient multi-dimensional container of generic data. Arbitrary data-types can be defined. This allows NumPy to seamlessly and speedily integrate with a wide variety of databases._

_NumPy is licensed under the [BSD license](https://numpy.org/license.html#license), enabling reuse with few restrictions.”_

NumPy is such an important Python library that there are other libraries (including pandas) that are built entirely on NumPy.

### **The Main Benefit of NumPy**

The main benefit of NumPy is that it allows for extremely fast data generation and handling. NumPy has its own built-in data structure called an `array` which is similar to the normal Python `list`, but can store and operate on data much more efficiently.

### **What We Will Learn About NumPy**

Advanced Python practitioners will spend much more time working with pandas than they spend working with NumPy. Still, given that pandas is built on NumPy, it is important to understand the most important aspects of the NumPy library.

Over the next several sections, we will cover the following information about the NumPy library:

* NumPy Arrays
* NumPy Indexing and Assignment
* NumPy Methods and Operations

### **Moving On**

Let’s move on to learning about NumPy arrays, the core data structure that every NumPy practitioner must be familiar with.

## **NumPy Arrays**

In this section, we will be learning about [NumPy arrays](https://nickmccullum.com/advanced-python/numpy-arrays/).

### **What Are NumPy Arrays?**

NumPy arrays are the main way to store data using the NumPy library. They are similar to normal lists in Python, but have the advantage of being faster and having more built-in methods.

NumPy arrays are created by calling the `array()` method from the NumPy library. Within the method, you should pass in a list.

An example of a basic NumPy array is shown below. Note that while I run the `import numpy as np` statement at the start of this code block, it will be excluded from the other code blocks in this section for brevity’s sake.

```
import numpy as np

sample_list = [1, 2, 3]

np.array(sample_list)

```

The last line of that code block will result in an output that looks like this.

```
array([1,2,3])

```

The `array()` wrapper indicates that this is no longer a normal Python list. Instead, it is a NumPy array.

### **The Two Different Types of NumPy Arrays**

There are two different types of NumPy arrays: vectors and matrices.

Vectors are one-dimensional NumPy arrays, and look like this:

```
my_vector = np.array(['this', 'is', 'a', 'vector'])

```

Matrices are two-dimensional arrays and are created by passing a list of lists into the `np.array()` method. An example is below.

```
my_matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

np.array(my_matrix)

```

You can also expand NumPy arrays to deal with three-, four-, five-, six- or higher-dimensional arrays, but they are rare and largely outside the scope of this course (after all, this is a course on Python programming, not linear algebra).

### **NumPy Arrays: Built-In Methods**

NumPy arrays come with a number of useful built-in methods. We will spend the rest of this section discussing these methods in detail.

#### **How To Get A Range Of Numbers in Python Using NumPy**

NumPy has a useful method called `arange` that takes in two numbers and gives you an array of integers that are greater than or equal to (`>=`) the first number and less than (`<`) the second number.

An example of the `arange` method is below.

```
np.arange(0,5)

#Returns array([0, 1, 2, 3, 4])

```

You can also include a third variable in the `arange` method that provides a step-size for the function to return. Passing in `2` as the third variable will return every 2nd number in the range, passing in `5` as the third variable will return every 5th number in the range, and so on.

An example of using the third variable in the `arange` method is below.

```
np.arange(1,11,2)

#Returns array([1, 3, 5, 7, 9])

```

### **How To Generates Ones and Zeros in Python Using NumPy**

While programming, you will from time to time need to create arrays of ones or zeros. NumPy has built-in methods that allow you to do either of these.

We can create arrays of zeros using NumPy’s `zeros` method. You pass in the number of integers you’d like to create as the argument of the function. An example is below.

```
np.zeros(4)

#Returns array([0, 0, 0, 0])

```

You can also do something similar using three-dimensional arrays. For example, `np.zeros(5, 5)` creates a 5x5 matrix that contains all zeros.

We can create arrays of ones using a similar method named `ones`. An example is below.

```
np.ones(5)

#Returns array([1, 1, 1, 1, 1])

```

#### **How To Evenly Divide A Range Of Numbers In Python Using NumPy**

There are many situations in which you have a range of numbers and you would like to equally divide that range of numbers into intervals. NumPy’s `linspace` method is designed to solve this problem. `linspace` takes in three arguments:

1. The start of the interval
2. The end of the interval
3. The number of subintervals that you’d like the interval to be divided into

An example of the `linspace` method is below.

```
np.linspace(0, 1, 10)

#Returns array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])

```

#### **How To Create An Identity Matrix In Python Using NumPy**

Anyone who has studied linear algebra will be familiar with the concept of an ‘identity matrix’, which is a square matrix whose diagonal values are all `1`. NumPy has a built-in function that takes in one argument for building identity matrices. The function is `eye`.

Examples are below:

```
np.eye(1)

#Returns a 1x1 identity matrix

np.eye(2) 

#Returns a 2x2 identity matrix

np.eye(50)

#Returns a 50x50 identity matrix

```

#### **How To Create Random Numbers in Python Using NumPy**

NumPy has a number of methods built-in that allow you to create arrays of random numbers. Each of these methods starts with `random`. A few examples are below:

```
np.random.rand(sample_size)

#Returns a sample of random numbers between 0 and 1.

#Sample size can either be one integer (for a one-dimensional array) or two integers separated by commas (for a two-dimensional array).

np.random.randn(sample_size)

#Returns a sample of random numbers between 0 and 1, following the normal distribution.

#Sample size can either be one integer (for a one-dimensional array) or two integers separated by commas (for a two-dimensional array).

np.random.randint(low, high, sample_size)

#Returns a sample of integers that are greater than or equal to 'low' and less than 'high'

```

#### **How To Reshape NumPy Arrays**

It is very common to take an array with certain dimensions and transform that array into a different shape. For example, you might have a one-dimensional array with 10 elements and want to switch it to a 2x5 two-dimensional array.

An example is below:

```
arr = np.array([0,1,2,3,4,5])

arr.reshape(2,3)

```

The output of this operation is:

```
array([[0, 1, 2],

       [3, 4, 5]])

```

Note that in order to use the `reshape` method, the original array must have the same number of elements as the array that you’re trying to reshape it into.

If you’re curious about the current shape of a NumPy array, you can determine its shape using NumPy’s `shape` attribute. Using our previous `arr` variable structure, an example of how to call the `shape` attribute is below:

```
arr = np.array([0,1,2,3,4,5])

arr.shape

#Returns (6,) - note that there is no second element since it is a one-dimensional array

arr = arr.reshape(2,3)

arr.shape

#Returns (2,3)

```

You can also combine the `reshape` method with the `shape` attribute on one line like this:

```
arr.reshape(2,3).shape

#Returns (2,3)

```

#### **How To Find The Maximum and Minimum Value Of A NumPy Array**

To conclude this section, let’s learn about four useful methods for identifying the maximum and minimum values within a NumPy array. We’ll be working with this array:

```
simple_array = [1, 2, 3, 4]

```

We can use the `max` method to find the maximum value of a NumPy array. An example is below.

```
simple_array.max()

#Returns 4

```

We can also use the `argmax` method to find the index of the maximum value within a NumPy array. This is useful for when you want to find the location of the maximum value but you do not necessarily care what its value is.

An example is below.

```
simple_array.argmax()

#Returns 3

```

Similarly, we can use the `min` and `argmin` methods to find the value and index of the minimum value within a NumPy array.

```
simple_array.min()

#Returns 1

simple_array.argmin()

#Returns 0

```

### **Moving On**

In this section, we discussed various attributes and methods of NumPy arrays. We will follow up by working through some NumPy array practice problems in the next section.

## **NumPy Methods and Operations**

In this section, we will be working through [various operations included in the NumPy library.](https://nickmccullum.com/advanced-python/numpy-methods-operations/)

Throughout this section, we will be assuming that the `import numpy as np` command has already been run.

### **The Array Used In This Section**

For this section, I will be working with an array of length 4 created using `np.arange` in all of the examples.

If you’d like to compare my array with the outputs used in this section, here is how I created and printed the array:

```
arr = np.arange(4)

arr

```

The array values are below.

```
array([0, 1, 2, 3])

```

### **How To Perform Arithmetic In Python Using Number**

NumPy makes it very easy to perform arithmetic with arrays. You can either perform arithmetic using the array and a single number, or you can perform arithmetic between two NumPy arrays.

We explore each of the major mathematical operations below.

#### **Addition**

When adding a single number to a NumPy array, that number is added to each element in the array. An example is below:

```
2 + arr

#Returns array([2, 3, 4, 5])

```

You can add two NumPy arrays using the `+` operator. The arrays are added on an element-by-element basis (meaning the first elements are added together, the second elements are added together, and so on).

An example is below.

```
arr + arr

#Returns array([0, 2, 4, 6])

```

#### **Subtraction**

Like addition, subtraction is performed on an element-by-element basis for NumPy arrays. You can find example for both a single number and another NumPy array below.

```
arr - 10

#Returns array([-10,  -9,  -8,  -7])

arr - arr

#Returns array([0, 0, 0, 0])

```

#### **Multiplication**

Multiplication is also performed on an element-by-element basis for both single numbers and NumPy arrays.

Two examples are below.

```
6 * arr

#Returns array([ 0,  6, 12, 18])

arr * arr

#Returns array([0, 1, 4, 9])

```

#### **Division**

By this point, you’re probably not surprised to learn that division performed on NumPy arrays is done on an element-by-element basis. An example of dividing `arr` by a single number is below:

```
arr / 2

#Returns array([0. , 0.5, 1. , 1.5])

```

Division does have one notable exception compared to the other mathematical operations we have seen in this section. Since we cannot divide by zero, doing so will cause the corresponding field to be populated by a `nan` value, which is Python shorthand for “Not A Number”. Jupyter Notebook will also print a warning that looks like this:

```
RuntimeWarning: invalid value encountered in true_divide

```

An example of dividing by zero is with a NumPy array is shown below.

```
arr / arr

#Returns array([nan,  1.,  1.,  1.])

```

We will learn how to deal with `nan` values in more detail later in this course.

### **Complex Operations in NumPy Arrays**

Many operations cannot simply be performed by applying the normal syntax to a NumPy array. In this section, we will explore several mathematical operations that have built-in methods in the NumPy library.

#### **How To Calculate Square Roots Using NumPy**

You can calculate the square root of every element in an array using the `np.sqrt` method:

```
np.sqrt(arr)

#Returns array([0., 1., 1.41421356, 1.73205081])

```

Many other examples are below (note that you will not be tested on these, but it is still useful to see the capabilities of NumPy):

```
np.exp(arr)

#Returns e^element for every element in the array

np.sin(arr)

#Calculate the trigonometric sine of every value in the array

np.cos(arr)

#Calculate the trigonometric cosine of every value in the array

np.log(arr)

#Calculate the base-ten logarithm of every value in the array

```

### **Moving On**

In this section, we explored the various methods and operations available in the NumPy Python library. We will text your knowledge of these concepts in the practice problems presented next.

## **NumPy Indexing and Assignment**

In this section, we will explore [indexing and assignment in NumPy arrays.](https://nickmccullum.com/advanced-python/numpy-indexing-assignment/)

### **The Array I’ll Be Using In This Section**

As before, I will be using a specific array through this section. This time it will be generated using the `np.random.rand` method. Here’s how I generated the array:

```
arr = np.random.rand(5)

```

Here is the actual array:

```
array([0.69292946, 0.9365295 , 0.65682359, 0.72770856, 0.83268616])

```

To make this array easier to look at, I will round every element of the array to 2 decimal places using NumPy’s `round` method:

```
arr = np.round(arr, 2)

```

Here’s the new array:

```
array([0.69, 0.94, 0.66, 0.73, 0.83])

```

### **How To Return A Specific Element From A NumPy Array**

We can select (and return) a specific element from a NumPy array in the same way that we could using a normal Python list: using square brackets.

An example is below:

```
arr[0]

#Returns 0.69

```

We can also reference multiple elements of a NumPy array using the colon operator. For example, the index `[2:]` selects every element from index 2 onwards. The index `[:3]` selects every element up to and excluding index 3. The index `[2:4]` returns every element from index 2 to index 4, excluding index 4. The higher endpoint is always excluded.

A few example of indexing using the colon operator are below.

```
arr[:]

#Returns the entire array: array([0.69, 0.94, 0.66, 0.73, 0.83])

arr[1:]

#Returns array([0.94, 0.66, 0.73, 0.83])

arr[1:4] 

#Returns array([0.94, 0.66, 0.73])

```

### **Element Assignment in NumPy Arrays**

We can assign new values to an element of a NumPy array using the `=` operator, just like regular python lists. A few examples are below (note that this is all one code block, which means that the element assignments are carried forward from step to step).

```
array([0.12, 0.94, 0.66, 0.73, 0.83])

arr

#Returns array([0.12, 0.94, 0.66, 0.73, 0.83])

arr[:] = 0

arr

#Returns array([0., 0., 0., 0., 0.])

arr[2:5] = 0.5

arr

#Returns array([0. , 0. , 0.5, 0.5, 0.5])



```

### **Array Referencing in NumPy**

NumPy makes use of a concept called ‘array referencing’ which is a very common source of confusion for people that are new to the library.

To understand array referencing, let’s first consider an example:

```

new_array = np.array([6, 7, 8, 9])

second_new_array = new_array[0:2]

second_new_array

#Returns array([6, 7])

second_new_array[1] = 4

second_new_array 

#Returns array([6, 4]), as expected

new_array 

#Returns array([6, 4, 8, 9]) 

#which is DIFFERENT from its original value of array([6, 7, 8, 9])

#What the heck?

```

As you can see, modifying `second_new_array` also changed the value of `new_array`.

Why is this?

By default, NumPy does not create a copy of an array when you reference the original array variable using the `=` assignment operator. Instead, it simply points the new variable to the old variable, which allows the second variable to make modification to the original variable - even if this is not your intention.

This may seem bizarre, but it does have a logical explanation. The purpose of array referencing is to conserve computing power. When working with large data sets, you would quickly run out of RAM if you created a new array every time you wanted to work with a slice of the array.

Fortunately, there is a workaround to array referencing. You can use the `copy` method to explicitly copy a NumPy array.

An example of this is below.

```
array_to_copy = np.array([1, 2, 3])

copied_array = array_to_copy.copy()

array_to_copy

#Returns array([1, 2, 3])

copied_array

#Returns array([1, 2, 3])

```

As you can see below, making modifications to the copied array does not alter the original.

```
copied_array[0] = 9

copied_array

#Returns array([9, 2, 3])

array_to_copy

#Returns array([1, 2, 3])

```

So far in the section, we have only explored how to reference one-dimensional NumPy arrays. We will now explore the indexing of two-dimensional arrays.

### **Indexing Two-Dimensional NumPy Arrays**

To start, let’s create a two-dimensional NumPy array named `mat`:

```
mat = np.array([[5, 10, 15],[20, 25, 30],[35, 40, 45]])

mat

"""

Returns:

array([[ 5, 10, 15],

       [20, 25, 30],

       [35, 40, 45]])

"""

```

There are two ways to index a two-dimensional NumPy array:

* `mat[row, col]`
* `mat[row][col]`

I personally prefer to index using the `mat[row][col]` nomenclature because it is easier to visualize in a step-by-step fashion. For example:

```
#First, let's get the first row:

mat[0]

#Next, let's get the last element of the first row:

mat[0][-1]

```

You can also generate sub-matrices from a two-dimensional NumPy array using this notation:

```
mat[1:][:2]

"""

Returns:

array([[20, 25, 30],

       [35, 40, 45]])

"""

```

Array referencing also applies to two-dimensional arrays in NumPy, so be sure to use the `copy` method if you want to avoid inadvertently modifying an original array after saving a slice of it into a new variable name.

### **Conditional Selection Using NumPy Arrays**

NumPy arrays support a feature called `conditional selection`, which allows you to generate a new array of boolean values that state whether each element within the array satisfies a particular `if` statement.

An example of this is below (I also re-created our original `arr` variable since its been awhile since we’ve seen it):

```
arr = np.array([0.69, 0.94, 0.66, 0.73, 0.83])

arr > 0.7

#Returns array([False,  True, False,  True,  True])

```

You can also generate a new array of values that satisfy this condition by passing the condition into the square brackets (just like we do for indexing).

An example of this is below:

```
arr[arr > 0.7]

#Returns array([0.94, 0.73, 0.83])

```

Conditional selection can become significantly more complex than this. We will explore more examples in this section’s associated practice problems.

### **Moving On**

In this section, we explored NumPy array indexing and assignment in thorough detail. We will solidify your knowledge of these concepts further by working through a batch of practice problems in the next section.

## Final Thoughts & Special Offer

Thanks for reading this article on NumPy, which is one of my favorite Python packages and a must-know library for every Python developer.

**This tutorial is an excerpt from my course** **[Python For Finance and Data Science](https://courses.nickmccullum.com/courses/enroll/python-for-finance/). If you're interested in learning more core Python skills, the course is 50% off for the first 50 freeCodeCamp readers that sign up - [click here to get your discounted course now](https://courses.nickmccullum.com/courses/enroll/python-for-finance/)!**


