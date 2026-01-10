---
title: Dataframe Drop Column in Pandas – How to Remove Columns from Dataframes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-27T18:03:48.000Z'
originalURL: https://freecodecamp.org/news/dataframe-drop-column-in-pandas-how-to-remove-columns-from-dataframes
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/Shittu-Olumide-Dataframe-Drop-Column-in-Pandas---How-to-Remove-Columns-from-Dataframes.png
tags:
- name: Data Science
  slug: data-science
- name: pandas
  slug: pandas
- name: Python
  slug: python
seo_title: null
seo_desc: 'By Shittu Olumide

  In Pandas, sometimes you''ll need to remove columns from a DataFrame for various
  reasons, such as cleaning data, reducing memory usage, or simplifying analysis.
  And in this article, I''ll show you how to do it.

  I''ll start by introduci...'
---

By Shittu Olumide

In Pandas, sometimes you'll need to remove columns from a DataFrame for various reasons, such as cleaning data, reducing memory usage, or simplifying analysis. And in this article, I'll show you how to do it.

I'll start by introducing the `.drop()` method, which is the primary method for removing columns in Pandas. We'll go through the syntax and parameters of the `.drop()` method, including how to specify columns to remove and how to control whether the original DataFrame is modified in place or a new DataFrame is returned.

Next, I'll provide an example of how to use the `.drop()` method to remove columns from a DataFrame.

## How to Use the `.drop()` Method in Pandas

The `.drop()` method is a built-in function in Pandas that allows you to remove one or more rows or columns from a DataFrame. It returns a new DataFrame with the specified rows or columns removed and does not modify the original DataFrame in place, unless you set the `inplace` parameter to `True`.

The syntax for using the `.drop()` method is as follows:

```py
DataFrame.drop(labels=None, axis=0, index=None, columns=None, level=None, inplace=False, errors='raise')

```

Here, `DataFrame` refers to the Pandas DataFrame that you want to remove rows or columns from. The parameters you can use with the `.drop()` method include:

* `labels`: This parameter specifies the labels or indices of the rows or columns to be removed. You can pass either a single label or index or a list of labels or indices.
* `axis`: This parameter specifies whether to remove rows or columns. By default, it is set to `0`, which means rows are removed. If you want to remove columns, set it to `1`.
* `index` and `columns`: These parameters are alternative to the `labels` parameter and specify the labels or indices of rows or columns to be removed, respectively.
* `level`: This parameter is used to remove a specific level of a hierarchical index.
* `inplace`: This parameter is a boolean value that determines whether to modify the original DataFrame in place. By default, it is set to `False`.
* `errors`: This parameter specifies how to handle errors if the specified label(s) or index(es) are not found in the DataFrame. By default, it is set to `raise`, which means that a `KeyError` is raised. Other options are `ignore` and `warn`, which will respectively ignore or display a warning when the label/index is not found.

## How to Remove a Single Column from a Dataframe in Pandas

Let's ease into it by first learning how to remove a single column from a Dataframe before we remove multiple columns.

Code sample:

```py
import pandas as pd

# create a sample dataframe
data = {'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 30, 35],
        'gender': ['F', 'M', 'M']
        }
df = pd.DataFrame(data)

# display the original dataframe
print('Original DataFrame:\n', df)

# drop the 'gender' column
df = df.drop(columns=['gender'])

# display the modified dataframe
print('Modified DataFrame:\n', df)

```

Output:

```bash
Original DataFrame:
       name  age gender
0    Alice   25      F
1      Bob   30      M
2  Charlie   35      M

Modified DataFrame:
       name  age
0    Alice   25
1      Bob   30
2  Charlie   35

```

### Code explanation:

In the example above, we first created a sample DataFrame with three columns – `name`, `age`, and `gender`. We then used the `.drop()` method with the `columns` parameter to remove the `gender` column. The resulting DataFrame only contains the `name` and `age` columns.

It's important to note that the `.drop()` method does not modify the original DataFrame in place. Instead, it returns a new DataFrame with the specified column(s) removed. If you want to modify the original DataFrame, you need to assign the result of the `.drop()` method back to the original variable, as we did in the example above.

In addition to the `columns` parameter, the `.drop()` method also has a number of other optional parameters you can use to control how columns are removed. 

For example, you can use the `inplace` parameter to modify the original DataFrame in place instead of returning a new DataFrame. You can also use the `axis` parameter to remove columns by index instead of name.

## How to Remove Multiple Columns from a Dataframe in Pandas

In this section we will remove multiple columns from our dataframe. This approach is similar to removing a single column from the dataframe.

To remove two or more columns from a DataFrame using the `.drop()` method in Pandas, we can pass a list of column names to the `columns` parameter of the method.

### Code sample:

```py
import pandas as pd

# create a sample dataframe
data = {'name': ['John', 'Mary', 'Peter'],
        'age': [30, 25, 35],
        'gender': ['Male', 'Female', 'Male'],
        'city': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)

# remove the 'gender' and 'city' columns
df.drop(columns=['gender', 'city'], inplace=True)

# print the modified dataframe
print(df)

```

Output:

```bash
    name  age
0   John   30
1   Mary   25
2  Peter   35

```

### Code explanation:

In this example, we first create a sample DataFrame with four columns – `name`, `age`, `gender`, and `city`. Then, we use the `.drop()` method to remove the `gender` and `city` columns by passing a list of their names to the `columns` parameter. Finally, we set the `inplace` parameter to `True` to modify the original DataFrame and print the modified DataFrame.

Note that you can also remove columns by their indices by passing a list of indices to the `columns` parameter. For example, to remove the second and third columns, you can use:

```py
df.drop(columns=df.columns[1:3], inplace=True)

```

This will remove the columns with indices 1 and 2 (that is the `age` and `gender` columns in this example).

## Conclusion

I hope this article is a useful resource for anyone working with Pandas DataFrames who needs to remove columns efficiently and effectively.

Let's connect on [Twitter](https://www.twitter.com/Shittu_Olumide_) and on [LinkedIn](https://www.linkedin.com/in/olumide-shittu). You can also subscribe to my [YouTube](https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A) channel.

Happy Coding!

