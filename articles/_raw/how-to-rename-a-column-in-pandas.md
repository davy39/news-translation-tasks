---
title: How to Rename a Column in Pandas – Python Pandas Dataframe Renaming Tutorial
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-01-13T18:18:13.000Z'
originalURL: https://freecodecamp.org/news/how-to-rename-a-column-in-pandas
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/how-to-rename-column-in-pandas.svg
tags:
- name: Data Science
  slug: data-science
- name: pandas
  slug: pandas
- name: Python
  slug: python
seo_title: null
seo_desc: "A Pandas Dataframe is a 2-dimensional data structure that displays data\
  \ in tables with rows and columns. \nIn this article, you'll learn how to rename\
  \ columns in a Pandas Dataframe by using: \n\nThe rename() function.\nA List.\n\
  The set_axis() function.\n\nH..."
---

A Pandas Dataframe is a 2-dimensional data structure that displays data in tables with rows and columns. 

In this article, you'll learn how to rename columns in a Pandas Dataframe by using: 

* The `rename()` function.
* A List.
* The `set_axis()` function.

## How to Rename a Column in Pandas Using the `rename()` Function

In this section, you'll see a practical example of renaming a Pandas Dataframe using the `rename()` function. 

Let's begin by passing data into a Dataframe object: 

```python
import pandas as pd

students = {
    "firstname": ["John", "Jane", "Jade"], 
    "lastname": ["Doe", "Done", "Do"]
}

# convert student names into a Dataframe
df = pd.DataFrame(students)

print(df)
```

```txt
# Output
  firstname lastname
0      John      Doe
1      Jane     Done
2      Jade       Do
```

In the example above, we created a Python dictionary which we used to store the `firstname` and `lastname` of students. 

We then converted the dictionary to a Dataframe by passing it as a parameter to the Pandas Dataframe object: `pd.DataFrame(students)`. 

When printed to the console, we had this table printed out:

```txt
  firstname lastname
0      John      Doe
1      Jane     Done
2      Jade       Do
```

The goal here is to rename the columns. We can do that using the `rename()` function. 

### **Here's what the syntax looks like:**

```
df.rename(columns={"OLD_COLUMN_VALUE": "NEW_COLUMN_VALUE"})
```

Let's go ahead and change the column names (`firstname` and `lastname`) in the table from lowercase to uppercase (`FIRSTNAME` and `LASTNAME`). 

```python
import pandas as pd

students = {
    "firstname": ["John", "Jane", "Jade"], 
    "lastname": ["Doe", "Done", "Do"]
}

# convert student names into a Dataframe
df = pd.DataFrame(students)

df.rename(columns={"firstname": "FIRSTNAME", "lastname": "LASTNAME"}, inplace=True)

print(df)
```

```txt
# Output
  FIRSTNAME LASTNAME
0      John      Doe
1      Jane     Done
2      Jade       Do
```

In the code above, we specified that the columns `firstname` and `lastname` should be renamed to `FIRSTNAME` and `LASTNAME`, respectively: `df.rename(columns={"firstname": "FIRSTNAME", "lastname": "LASTNAME"}, inplace=True)`

You'll notice that we added the `inplace=True` parameter. This helps in persisting the new changes in the Dataframe. Delete the parameter and see what happens ;)

You can rename the columns to whatever you want. For instance, we can use `SURNAME` instead of `lastname` by doing this:

```python
import pandas as pd

students = {
    "firstname": ["John", "Jane", "Jade"], 
    "lastname": ["Doe", "Done", "Do"]
}

# convert student names into a Dataframe
df = pd.DataFrame(students)
df.rename(columns={"firstname": "FIRSTNAME", "lastname": "SURNAME"}, inplace=True)

print(df)
```

```txt
# Output
  FIRSTNAME SURNAME
0      John     Doe
1      Jane    Done
2      Jade      Do
```

You can change just one column name, too. You are not required to change all the column names at the same time. 

## How to Rename a Column in Pandas Using a List

You can access the column names of a Dataframe using `df.columns`. Consider the table below:

```txt
  firstname lastname
0      John      Doe
1      Jane     Done
2      Jade       Do
```

We can print out the column names with the code below:

```python 
print(df.columns)

# Index(['firstname', 'lastname'], dtype='object')
```

Using that, we can rename the column of a Dataframe. Here's an example:

```python
import pandas as pd

students = {
    "firstname": ["John", "Jane", "Jade"], 
    "lastname": ["Doe", "Done", "Do"]
}

# convert student names into a Dataframe
df = pd.DataFrame(students)
df.columns = ["FIRSTNAME", "SURNAME"]

print(df)
```

```txt
# Output
  FIRSTNAME SURNAME
0      John     Doe
1      Jane    Done
2      Jade      Do
```

In the example above, we put the new column names in a List and assigned it to the Dataframe columns: `df.columns = ["FIRSTNAME", "SURNAME"]`. 

This will override the previous column names. 

## How to Rename a Column in Pandas Using the `set_axis()` Function

The syntax for renaming a column with the `set_axis()` function looks like this:

```
df.set_axis([NEW_COLUMN_NAME,...], axis="columns")
```

Here's a code example:

```python
import pandas as pd

students = {
    "firstname": ["John", "Jane", "Jade"], 
    "lastname": ["Doe", "Done", "Do"]
}

# convert student names into a Dataframe
df = pd.DataFrame(students)

df.set_axis(["FIRSTNAME", "SURNAME"], axis="columns", inplace=True) 

print(df)
```

```txt
# Output
  FIRSTNAME SURNAME
0      John     Doe
1      Jane    Done
2      Jade      Do
```

Note that the `inplace=True` parameter might raise a warning because it's deprecated for the `set_axis()` function and will be replaced in the future. 

## Summary

In this article, we talked about renaming a column in Pandas. 

We saw different methods that can be used to rename a Pandas Dataframe column with code examples. 

Happy coding!

