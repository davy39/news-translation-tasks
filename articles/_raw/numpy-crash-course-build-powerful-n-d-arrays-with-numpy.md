---
title: Python NumPy Crash Course – How to Build N-Dimensional Arrays for Machine Learning
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2020-09-22T17:34:36.000Z'
originalURL: https://freecodecamp.org/news/numpy-crash-course-build-powerful-n-d-arrays-with-numpy
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/numpy-1.png
tags:
- name: Machine Learning
  slug: machine-learning
- name: numpy
  slug: numpy
seo_title: null
seo_desc: 'NumPy is a Python library for performing large scale numerical computations.
  It is extremely useful, especially in machine learning. Let''s look at what NumPy
  has to offer.

  Introduction to NymPy

  NumPy is a Python library used to perform numerical comp...'
---

NumPy is a Python library for performing large scale numerical computations. It is extremely useful, especially in machine learning. Let's look at what NumPy has to offer.

# Introduction to NymPy

NumPy is a Python library used to perform numerical computations with large datasets. The name stands for Numerical Python and it is a popular library used by data scientists, especially for machine learning problems. 

NumPy is useful while pre-processing the data before you train it using a machine learning algorithm.

Working with n-dimensional arrays is easier in NumPy compared to Python lists. NumPy arrays are also faster than Python lists since, unlike lists, NumPy arrays are stored at one continuous place in memory. This enables the processor to perform computations efficiently.

In this article, we will look at the basics of working with NumPy including array operations, matrix transformations, generating random values, and so on.

# Installation

Clear installation instructions are provided on NumPy's official website, so I am not going to repeat them in this article. [Please find those instructions here](https://numpy.org/install/).

# Working with NumPy

## Importing NumPy

To start using NumPy in your script, you have to import it.

```
import numpy as np
```

## Converting Arrays to NumPy Arrays

You can convert your existing Python lists into NumPy arrays using the np.array() method, like this:

```
arr = [1,2,3]
np.array(arr)
```

This also applies to multi-dimensional arrays. NumPy will keep track of the shape (dimensions) of the array.

```
nested_arr = [[1,2],[3,4],[5,6]]
np.array(nested_arr)
```

## NumPy Arrange Function

When working with data, you will often come across use cases where you need to generate data.

NumPy as an “arrange()” method with which you can generate a range of values between two numbers. The arrange function takes the start, end, and an optional distance parameter.

```
print(np.arrange(0,10)) # without distance parameter
OUTPUT:[0 1 2 3 4 5 6 7 8 9]

print(np.arrange(0,10,2)) # with distance parameter
OUTPUT: [0 2 4 6 8]
```

## Zeroes and Ones

You can also generate an array or matrix of zeroes or ones using NumPy (trust me, you will need it). Here's how.

```
print(np.zeros(3))
OUTPUT: [0. 0. 0.]

print(np.ones(3))
OUTPUT: [1. 1. 1.]
```

Both these functions support n-dimensional arrays as well. You can add the shape as a tuple with rows and columns.

```
print(np.zeros((4,5)))
OUTPUT:
[
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
]

print(np.ones((4,5)))
OUTPUT:
[
 [1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]
]
```

## Identity Matrix

You can also generate an [identity matrix](https://en.wikipedia.org/wiki/Identity_matrix) using a built-in NumPy function called “eye”.

```
np.eye(5)
OUTPUT:
[[1., 0., 0., 0., 0.]
[0., 1., 0., 0., 0.]
[0., 0., 1., 0., 0.]
[0., 0., 0., 1., 0.]
[0., 0., 0., 0., 1.]]
```

## NumPy Linspace Function

NumPy has a linspace method that generates evenly spaced points between two numbers.

```
print(np.linspace(0,10,3))
OUTPUT:[ 0.  5. 10.]
```

In the above example, the first and second params are the start and the end points, while the third param is the number of points you need between the start and the end.

Here is the same range with 20 points.

```
print(np.linspace(0,10,20))
OUTPUT:[ 0. 0.52631579  1.05263158  1.57894737  2.10526316  2.63157895   3.15789474  3.68421053  4.21052632  4.73684211  5.26315789  5.78947368   6.31578947  6.84210526  7.36842105  7.89473684  8.42105263  8.94736842   9.47368421 10.]
```

## Random Number Generation

When you are working on machine learning problems, you will often need to generate random numbers. NumPy has in-built functions for that as well.

But before we start generating random numbers, let's look at two major types of distributions.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/distro-1.png)

### Normal Distribution

In a [standard normal distribution](https://www.mathsisfun.com/data/standard-normal-distribution.html), the values peak in the middle. 

The normal distribution is a very important concept in statistics since it seen in many natural phenomena. It is also called a “bell curve”.

### Uniform Distribution

If the values in the distribution have the probability as a constant, it is called a [uniform distribution](https://www.investopedia.com/terms/u/uniform-distribution.asp). 

For example, a coin toss has a uniform distribution since the probability of getting either heads or tails in a coin toss is the same.

Now that you know how the two main distributions work, let's generate some random numbers.

* To generate random numbers in a uniform distribution, use the **rand()** function from **np.random**:

```
print(np.random.rand(10)) # array
OUTPUT: [0.46015141 0.89326339 0.22589334 0.29874476 0.5664353  0.39257603  0.77672998 0.35768031 0.95087408 0.34418542]

print(np.random.rand(3,4)) # 3x4 matrix
OUTPUT:[[0.63775985 0.91746663 0.41667645 0.28272243]  [0.14919547 0.72895922 0.87147748 0.94037953]  [0.5545835  0.30870297 0.49341904 0.27852723]]
```

* To generate random numbers in a normal distribution, use the **randn()** function from **np.random**:

```
print(np.random.randn(10))
OUTPUT:[-1.02087155 -0.75207769 -0.22696798  0.86739858  0.07367362 -0.41932541   0.86303979  0.13739312  0.13214285  1.23089936]

print(np.random.randn(3,4))
OUTPUT: [[ 1.61013773  1.37400445  0.55494053  0.23133522]  [ 0.31290971 -0.30866402  0.33093618  0.34868954]  [-0.11659865 -1.22311073  0.36676476  0.40819545]]
```

* To generate random integers between a low and high value, use the **randint()** function from **np.random**:

```
print(np.random.randint(1,100,10))
OUTPUT:[64 37 62 27  4 33 23 52 70  7]

print(np.random.randint(1,100,(2,3)))
OUTPUT:[[92 42 38]  [87 69 38]]
```

A [seed value](https://en.wikipedia.org/wiki/Random_seed) is used if you want your random numbers to be the same during each computation. Here is how you set a seed value in NumPy.

* To set a seed value in NumPy, do the following:

```
np.random.seed(42)
print(np.random.rand(4))
OUTPUT:[0.37454012, 0.95071431, 0.73199394, 0.59865848]
```

Whenever you use a seed number, you will always get the same array generated without any change.

## Reshaping Arrays

As a data scientist, you will work with re-shaping the data sets for different types of computations. In this section, we will look at how to work with the shapes of arrays.

* To get the shape of an array, use the **shape** property.

```
arr = np.random.rand(2,2)
print(arr)
print(arr.shape)
OUTPUT:[
[0.19890857 0.00806693]
[0.48199837 0.55373954]
]
(2, 2)
```

* To reshape an array, use the **reshape()** function.

```
print(arr.reshape(1,4))
OUTPUT: [[0.19890857 0.00806693 0.48199837 0.55373954]]
print(arr.reshape(4,1))
OUTPUT:[
[0.19890857]
[0.00806693]
[0.48199837]
[0.55373954]
]
```

In order to permanently reshape an array, you have to assign the reshaped array to the ‘arr’ variable. 

Also, reshape only works if the existing structure makes sense. You cannot reshape a 2x2 array into a 3x1 array.

## Slicing Data

Let's look at fetching data from NumPy arrays. NumPy arrays work similarly to Python lists during fetch operations.

* To slice an array, do this:

```
myarr = np.arange(0,11)
print(myarr)
OUTPUT:[ 0  1  2  3  4  5  6  7  8  9 10]

sliced = myarr[0:5]
print(sliced)
OUTPUT: [0 1 2 3 4]

sliced[:] = 99
print(sliced)
OUTPUT: [99 99 99 99 99]

print(myarr)
OUTPUT:[99 99 99 99 99  5  6  7  8  9 10]
```

If you look at the above example, even though we assigned the slice of “myarr” to the variable “sliced”, changing the value of “sliced” affects the original array. This is because the “slice” was just pointing to the original array.

To make an independent section of an array, use the **copy()** function.

```
sliced = myarr.copy()[0:5]
```

* Slicing multi-dimensional arrays work similarly to one-dimensional arrays.

```
my_matrix = np.random.randint(1,30,(3,3))
print(my_matrix)
OUTPUT: [
[21  1 20]
[22 16 27]
[24 14 22]
]

print(my_matrix[0]) # print a single row
OUTPUT: [21  1 20]

print(my_matrix[0][0]) # print a single value or row 0, column 0
OUTPUT: 21

print(my_matrix[0,0]) #alternate way to print value from row0,col0
OUTPUT: 21
```

## Array Computations

Now let's look at array computations. NumPy is known for its speed when performing complex computations on large multi-dimensional arrays.

Let’s try a few basic operations.

```
new_arr = np.arange(1,11)
print(new_arr)
OUTPUT: [ 1  2  3  4  5  6  7  8  9 10]
```

* Addition

```
print(new_arr + 5)
OUTPUT: [ 6  7  8  9 10 11 12 13 14 15]
```

* Subtraction

```
print(new_arr - 5)
OUTPUT: [-4 -3 -2 -1  0  1  2  3  4  5]
```

* Array Addition

```
print(new_arr + new_arr)
OUTPUT: [ 2  4  6  8 10 12 14 16 18 20]
```

* Array Division

```
print(new_arr / new_arr)
OUTPUT:[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
```

For [zero division errors](https://airbrake.io/blog/python-exception-handling/zerodivisionerror-2), Numpy will convert the value to NaN (not a number).

There are also a few in-built computation methods available in NumPy to calculate values like mean, standard deviation, variance, and others.

* Sum — np.sum()
* Square Root — np.sqrt()
* Mean — np.mean()
* Variance — np.var()
* Standard Deviation — np.std()

While working with 2d arrays, you will often need to calculate row wise or column-wise sum, mean, variance, and so on. You can use the optional axis parameter to specify if you want to choose a row or a column.

```
arr2d = np.arange(25).reshape(5,5)
print(arr2d)
OUTPUT: [
[ 0  1  2  3  4]
[ 5  6  7  8  9]
[10 11 12 13 14]
[15 16 17 18 19]
[20 21 22 23 24]
]

print(arr2d.sum())
OUTPUT: 300

print(arr2d.sum(axis=0))  # sum of columns
OUTPUT: [50 55 60 65 70]

print(arr2d.sum(axis=1)) #sum of rows
OUTPUT: [ 10  35  60  85 110]
```

## Conditional Operations

You can also do conditional filtering with NumPy using the square bracket notation. Here is an example:

```
arr = np.arange(0,10)
OUTPUT: [0,2,3,4,5,6,7,8,9]

print(arr > 4)
OUTPUT: [False False False False False  True  True  True  True  True]

print(arr[arr > 4])
OUTPUT: [5 6 7 8 9]
```

# Summary

When it comes to working with large datasets, NumPy is a powerful tool to have in your toolkit. It is capable of handling advanced numeric computations and complex n-dimensional array operations.

I highly recommended that you learn NumPy if you plan to start a career in machine learning.

[Here is a Google colab notebook if you want to try out these examples](https://colab.research.google.com/drive/1Oa8J_sZXACQJEiMqANIHkftMgUrqSpVt#scrollTo=ITrCTnT6RkWP).

[**Get a summary of my articles**](https://tinyletter.com/manishmshiva) and videos sent to your email every Monday morning. You can also [**connect with me**](https://www.manishmshiva.com/) here.

