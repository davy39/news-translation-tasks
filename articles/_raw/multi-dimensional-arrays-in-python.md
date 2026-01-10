---
title: Multi-Dimensional Arrays in Python – Matrices Explained with Examples
subtitle: ''
author: Jeremiah Oluseye
co_authors: []
series: null
date: '2023-04-06T17:28:05.000Z'
originalURL: https://freecodecamp.org/news/multi-dimensional-arrays-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/gids.JPG
tags:
- name: arrays
  slug: arrays
- name: Python
  slug: python
seo_title: null
seo_desc: 'Multi-dimensional arrays, also known as matrices, are a powerful data structure
  in Python. They allow you to store and manipulate data in multiple dimensions or
  axes.

  You''ll commonly use these types of arrays in fields such as mathematics, statistics...'
---

Multi-dimensional arrays, also known as matrices, are a powerful data structure in Python. They allow you to store and manipulate data in multiple dimensions or axes.

You'll commonly use these types of arrays in fields such as mathematics, statistics, and computer science to represent and process structured data, such as images, videos, and scientific data.

In Python, you can create multi-dimensional arrays using various libraries, such as NumPy, Pandas, and TensorFlow. In this article, we will focus on NumPy, which is one of the most popular and widely used libraries for working with arrays in Python.

NumPy provides a powerful N-dimensional array object that you can use to create and manipulate multi-dimensional arrays efficiently. We'll now look at some examples of how to create and work with multi-dimensional arrays in Python using NumPy.

## How to Create Multi-Dimensional Arrays Using NumPy

To create a multi-dimensional array using NumPy, we can use the `np.array()` function and pass in a nested list of values as an argument. The outer list represents the rows of the array, and the inner lists represent the columns.

Here is an example of how to create a 2-dimensional array using NumPy:

```python
import numpy as np

# Create a 2-dimensional array with 3 rows and 4 columns
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Print the array
print(arr)
```

Output:

```python
array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12]])
```

In this example, we first import the NumPy library using the `import` statement. Then, we create a 2-dimensional array using the `np.array()` function and pass in a list of lists as an argument. Each inner list represents a row of the array, and the outer list contains all the rows. Finally, we print the array using the `print()` function.

NumPy also provides other functions to create multi-dimensional arrays, such as `np.zeros()`, `np.ones()`, and `np.random.rand()`. You can use these functions to create arrays of specific shapes and sizes with default or random values.

## How to Access and Modify Multi-dimensional Arrays Using NumPy

Once we have created a multi-dimensional array, we can access and modify its elements using indexing and slicing. We use the index notation `[i, j]` to access an element at row `i` and column `j`, where `i` and `j` are zero-based indices.

Here's an example of how to access and modify elements of a 2-dimensional array using NumPy:

```python
import numpy as np

# Create a 2-dimensional array with 3 rows and 4 columns
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Access an element at row 1, column 2
print(arr[1, 2])  # Output: 7

# Modify an element at row 0, column 3
arr[0, 3] = 20

# Print the modified array
print(arr)
```

Output:

```python
7
array([[ 1,  2,  3, 20],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12]])
```

In this example, we create a 2-dimensional array using the `np.array()` function, and then access an element at row 1, column 2 using indexing. We then modify an element at row 0, column 3 using indexing again. Finally, we print the modified array using the `print()` function.

We can also use slicing to access and modify multiple elements of a multi-dimensional array at once. We use the slice notation `arr[i:j, k:l]` to access a subarray that contains rows `i` through `j-1` and columns `k` through `l-1`.

Here's an example of how to use slicing to access and modify elements of a 2-dimensional array using NumPy:

```python
import numpy as np

# Create a 2-dimensional array with 3 rows and 4 columns
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Access a subarray that contains rows 0 through 1 and columns 1 through 2
subarr = arr[0:2, 1:3]

# Print the subarray
print(subarr)

# Modify the subarray by multiplying it by 2
subarr *= 2

# Print the modified array
print(arr)
```

Output:

```python
array([[2, 3],
       [6, 7]])
array([[ 1,  4,  6,  4],
       [ 5, 12, 14,  8],
       [ 9, 10, 11, 12]])
```

In this example, we create a 2-dimensional array using the `np.array()` function, and then use slicing to access a subarray that contains rows 0 through 1 and columns 1 through 2. We then modify the subarray by multiplying it by 2, and print the modified original array using the `print()` function.

## How to Perform Operations on Multi-dimensional Arrays

NumPy provides a wide range of mathematical and statistical functions that you can use to perform operations on multi-dimensional arrays efficiently. These functions can help you perform element-wise operations, matrix operations, and other operations on arrays with different shapes and sizes.

Here's an example of how to perform some common operations on a 2-dimensional array using NumPy:

```python
import numpy as np

# Create a 2-dimensional array with 3 rows and 4 columns
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Calculate the sum of all elements
print(np.sum(arr))  # Output: 78

# Calculate the mean of each row
print(np.mean(arr, axis=1))  # Output: [ 2.5  6.5 10.5]

# Calculate the dot product of two matrices
b = np.array([[2, 3], [4, 5], [6, 7], [8, 9]])
print(np.dot(arr, b))  # Output: [[ 60  72]
                        #          [140 172]
                        #          [220 272]]
```

In this example, we create a 2-dimensional array using the `np.array()` function, and then use various NumPy functions to perform operations on the array.

We first calculate the sum of all elements using the `np.sum()` function. We then calculate the mean of each row using the `np.mean()` function and specify the `axis=1` parameter to calculate the mean along each row. Finally, we calculate the dot product of the 2-dimensional array and another 2-dimensional array `b` using the `np.dot()` function.

## Conclusion

Multi-dimensional arrays are a powerful and important data structure in Python. They allow us to store and manipulate large amounts of data efficiently.

In this article, we have covered the basics of creating and manipulating multi-dimensional arrays using NumPy in Python. We have also looked at some common operations that we can perform on multi-dimensional arrays using NumPy functions.

With the knowledge gained from this article, you should now be able to create and manipulate multi-dimensional arrays to suit your specific needs in Python.

Let’s connect on [Twitter](https://twitter.com/Olujerry19) and [LinkedIn](https://www.linkedin.com/in/jeremiah-oluseye-58457719a/).
