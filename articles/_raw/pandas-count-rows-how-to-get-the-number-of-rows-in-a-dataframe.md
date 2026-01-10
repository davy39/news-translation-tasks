---
title: Pandas Count Rows – How to Get the Number of Rows in a Dataframe
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-05-19T15:11:58.000Z'
originalURL: https://freecodecamp.org/news/pandas-count-rows-how-to-get-the-number-of-rows-in-a-dataframe
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/nacho-capelo-hMXuZrfmCWM-unsplash.jpg
tags:
- name: data analysis
  slug: data-analysis
- name: pandas
  slug: pandas
- name: Python
  slug: python
seo_title: null
seo_desc: "Pandas is a library built on the Python programming language. You can use\
  \ it to analyze and manipulate data.\nA dataframe is two-dimensional data structure\
  \ in Pandas that organizes data in a tabular format with rows and columns. \nIn\
  \ this article, you'..."
---

Pandas is a library built on the Python programming language. You can use it to analyze and manipulate data.

A dataframe is two-dimensional data structure in Pandas that organizes data in a tabular format with rows and columns. 

In this article, you'll learn how to get the number of rows in a dataframe using the following: 

* The `len()` function.
* The `shape` attribute.
* The `index` attribute.
* The `axes` attribuite. 

## How to Get the Number of Rows in a Dataframe Using the `len()` Function

You can use the `len()` function to return the length of an object. With a dataframe, the function returns the number of rows. 

Consider the dataframe below:

```python
import pandas as pd

data = {
  "name": ["John", "Jane", "Jade"],
  "age": [2, 10, 3]
}

df = pd.DataFrame(data)
df
```

|    |      name        |  age |
|----------|:-------------:|------:|
| 0 |  John  | 2 |
| 1 |    Jane | 10 |
| 2 | Jade | 3 |

In the example above, we created a dataframe with three rows — row 0, 1, and 2. 

You can use the `len()` function to verify the number of rows: 

```python
import pandas as pd

data = {
  "name": ["John", "Jane", "Jade"],
  "age": [2, 10, 3]
}

df = pd.DataFrame(data)
df

num_of_rows = len(df)

print(f"The number of rows is {num_of_rows}")
# The number of rows is 3
```

In the code above, we passed the dataframe as a parameter to the `len()` function and stored it in a variable called `num_of_rows`: 

```python
num_of_rows = len(df)
```

When `num_of_rows` was printed, we got a value of 3 (the number of rows).

## How to Get the Number of Rows in a Dataframe Using the `shape` Attribute

The `shape` attribute returns a tuple with the number of rows and columns in a dataframe.

Here's an example using the same dataframe as in the last section: 

```python
import pandas as pd

data = {
  "name": ["John", "Jane", "Jade"],
  "age": [2, 10, 3]
}

df = pd.DataFrame(data)
df

num_of_rows = df.shape

print(num_of_rows)
# (3, 2)
```

In the code above, a tuple — (3, 2) — was returned when we used the `shape` attribute on the dataframe: `df.shape`. 

The first value, 3, is the number of rows in the dataframe while the second value, 2, is the number of columns. 

Since we're only interested in the number of rows, we can extract just that value using its index in the tuple (remember that index numbers start at 0). That is:

```python
import pandas as pd

data = {
  "name": ["John", "Jane", "Jade"],
  "age": [2, 10, 3]
}

df = pd.DataFrame(data)
df

num_of_rows = df.shape[0]

print(f"The number of rows is {num_of_rows}")
# The number of rows is 3
```

Now we're getting just the number of rows using its index in the tuple: `df.shape[0]`. 

## How to Get the Number of Rows in a Dataframe Using the `index` Attribute

You can use the `index` attribute to access the number of elements in a dataframe, which corresponds with the number of rows. 

You can do this in two different ways: 

* Using the `index` attribute's `size` property. 
* Passing the `index` property as a parameter to the `len()` function. 

Here are examples to explain the methods above: 

```python
import pandas as pd

data = {
  "name": ["John", "Jane", "Jade"],
  "age": [2, 10, 3]
}

df = pd.DataFrame(data)
df

num_of_rows = df.index.size

print(f"The number of rows is {num_of_rows}")
# The number of rows is 3
```

In the example above, we accessed the number of rows in the dataframe using `df.index.size`.

Without the `size` property, you'd get a result like this: `RangeIndex(start=0, stop=3, step=1)`. 

* `start` denotes the first index number.
* `stop` denotes the number of rows in the dataframe. 
* `step` denotes the way indexes are incremented (indexes are increased by 1 in our case).

So the `size` property is way of specifying that you're only interested in the number of elements in the dataframe. 

Here's another example that uses the `len()` function: 

```pyhon
import pandas as pd

data = {
  "name": ["John", "Jane", "Jade"],
  "age": [2, 10, 3]
}

df = pd.DataFrame(data)
df

num_of_rows = len(df.index)

print(f"The number of rows is {num_of_rows}")
# The number of rows is 3
```

In the code above, we passed `df.index` as a parameter to the `len()` function. This returns the number of rows in the dataframe. 

The difference between this example and the previous one is that we're not attaching the `size` property to `df.index`. Instead, we're using `df.index` as the `len()` function's parameter. 

## How to Get the Number of Rows in a Dataframe Using the `axes` Attribute

The `axes` attribute returns the value as the `index` attribute: `RangeIndex(start=0, stop=3, step=1)`. 

Similarly, you can return the number of rows using either the `size` property or the `len()` function: 

```python
import pandas as pd

data = {
  "name": ["John", "Jane", "Jade"],
  "age": [2, 10, 3]
}

df = pd.DataFrame(data)
df

num_of_rows = df.axes[0].size

print(f"The number of rows is {num_of_rows}")
# The number of rows is 3
```

```python
import pandas as pd

data = {
  "name": ["John", "Jane", "Jade"],
  "age": [2, 10, 3]
}

df = pd.DataFrame(data)
df

num_of_rows = len(df.axes[0])

print(f"The number of rows is {num_of_rows}")
# The number of rows is 3
```

The logic in the two code blocks above is the same as those in the last section: 

* `df.index.size` returns the number of elements/rows in the dataframe. 
* `len(df.index)` returns the number of rows in the dataframe. 

## Summary

In this article, we talked about dataframes in Pandas. They are two-dimensional data structures that organize data in rows and columns. 

We saw different methods for getting the number of rows in a dataframe. We discussed the following methods along with code examples to show their application:

* The `len()` function.
* The `shape` attribute.
* The `index` attribute.
* The `axes` attribuite. 

Happy coding! You can learn more about Python on [my blog](https://ihechikara.com/).

