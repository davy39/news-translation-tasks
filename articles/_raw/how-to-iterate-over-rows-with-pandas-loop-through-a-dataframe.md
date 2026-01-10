---
title: How to Iterate Over Rows with Pandas – Loop Through a Dataframe
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-28T18:35:22.000Z'
originalURL: https://freecodecamp.org/news/how-to-iterate-over-rows-with-pandas-loop-through-a-dataframe
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/Shittu-Olumide-How-to-Iterate-Over-Rows-with-Pandas---Loop-Through-a-Dataframe.png
tags:
- name: data analysis
  slug: data-analysis
- name: pandas
  slug: pandas
- name: Python
  slug: python
seo_title: null
seo_desc: "By Shittu Olumide\nThis article provides a comprehensive guide on how to\
  \ loop through a Pandas DataFrame in Python. \nI'll start by introducing the Pandas\
  \ library and DataFrame data structure. I'll explain the essential characteristics\
  \ of Pandas, how t..."
---

By Shittu Olumide

This article provides a comprehensive guide on how to loop through a Pandas DataFrame in Python. 

I'll start by introducing the Pandas library and DataFrame data structure. I'll explain the essential characteristics of Pandas, how to loop through rows in a dataframe, and finally how to loop through columns in a dataframe.

## What is Pandas?

Pandas is a popular open-source Python library that's used for data cleaning, analysis, and manipulation. In addition to functions for carrying out operations on those datasets, it offers data structures for effectively storing and handling large and complex datasets. 

Some of the essential characteristics of Pandas are:

* **DataFrame and Series Objects**: Pandas provides two primary data structures, DataFrames and Series. They allow users to store and manipulate tabular data and time series data, respectively. These data structures are highly efficient and can handle large datasets with ease.
* **Data Cleaning and Preparation**: Pandas provides a wide range of functions and methods for cleaning and preparing data, including handling missing values, removing duplicates, and transforming data.
* **Data Analysis and Visualization**: Pandas provides powerful functions for performing data analysis, including statistical functions and grouping and aggregation functions. It also integrates well with other data analysis and visualization libraries in Python, such as Matplotlib and Seaborn.
* **Data Input and Output**: Pandas provides functions for reading and writing data in a variety of formats, including CSV, Excel, SQL databases, and more.

## What is a Pandas Dataframe?

In Pandas, a dataframe is a two-dimensional labeled data structure. It is comparable to a spreadsheet or a SQL table, where data is arranged in rows and columns with a variety of data types in each column.

Since dataframes offer an easy way to store, manipulate, and analyze data, they are frequently used in data science and data analysis applications. Dataframes provide a number of features, including pivoting, grouping, indexing, and filtering, that make it simple to carry out complex operations on data.

## How to Loop Through Rows in a Dataframe

You can loop through rows in a dataframe using the `iterrows()` method in Pandas. This method allows us to iterate over each row in a dataframe and access its values.

Here's an example:

```py
import pandas as pd

# create a dataframe
data = {'name': ['Mike', 'Doe', 'James'], 'age': [18, 19, 29]}
df = pd.DataFrame(data)

# loop through the rows using iterrows()
for index, row in df.iterrows():
    print(row['name'], row['age'])

```

Output:

```bash
Mike 18
Doe 19
James 29

```

In this example, we first create a dataframe with two columns, `name` and `age`. We then loop through each row in the dataframe using `iterrows()`, which returns a tuple containing the index of the row and a Series object that contains the values for that row.

Within the loop, we can access the values for each column by using the column name as an index on the row object. For example, to access the value for the `name` column, we use `row['name']`.

## How to Loop Through Columns in a Dataframe

Looping through columns in a dataframe is a common task in data analysis and manipulation. It's different from the way we loop through rows, though. 

Here's an example:

```py
import pandas as pd

# Create a sample dataframe
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

# Loop through columns using a for loop
for col in df.columns:
    print(col)

```

Output:

```bash
A
B
C

```

First, we import the Pandas library using the `import pandas as pd` statement.

Then, we create a sample dataframe using the `pd.DataFrame()` function, which takes a dictionary of column names and values as an input.

Next, we loop through the columns of the dataframe using a for loop and the `df.columns` attribute, which returns a list of column names.

Inside the loop, we simply print the name of each column using the `print()` function.

## Use Cases for Looping Through a Dataframe

Looping through a dataframe is an important technique in data analysis and manipulation, as it allows us to perform operations on each row or column of the dataframe. 

You'll loop through dataframes in the following activities:

* Data Cleaning and Transformation.
* Data Analysis.
* Data Visualization.
* Feature Engineering.

## Conclusion

By looping through the rows in a dataframe, we can perform operations on each row, such as filtering or transforming the data. 

But it's important to note that looping through rows in a dataframe can be slow and inefficient for large datasets. In general, it's often better to use vectorized operations or `apply()` functions to perform operations on dataframes, as these methods are optimized for performance.

Let's connect on [Twitter](https://www.twitter.com/Shittu_Olumide_) and on [LinkedIn](https://www.linkedin.com/in/olumide-shittu). You can also subscribe to my [YouTube](https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A) channel.

Happy Coding!

