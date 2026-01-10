---
title: How to Get Started with Pandas in Python – a Beginner's Guide
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-09T00:48:41.000Z'
originalURL: https://freecodecamp.org/news/python-pandas-functions
coverImage: https://cdn-media-2.freecodecamp.org/w1280/6040d911a7946308b768178e.jpg
tags:
- name: beginners guide
  slug: beginners-guide
- name: data analysis
  slug: data-analysis
- name: data analytics
  slug: data-analytics
- name: pandas
  slug: pandas
- name: Python
  slug: python
seo_title: null
seo_desc: "By Suchandra Datta\nThe Pandas package in Python gives you a bunch of cool\
  \ functions and features that help you manipulate data more efficiently. It also\
  \ lets you perform numerous data cleaning and data preprocessing steps with very\
  \ little hassle. \nTh..."
---

By Suchandra Datta

The Pandas package in Python gives you a bunch of cool functions and features that help you manipulate data more efficiently. It also lets you perform numerous data cleaning and data preprocessing steps with very little hassle. 

That's great isn't it? Here's a list of some of the most frequently used Pandas functions and tricks to help you enjoy your data science journey. 

## How to Remove Missing Values in DataFrame

Getting rid of missing values is one of the most common tasks in data cleaning. Missing values could be just across one row or column or across multiple rows and columns. 

Depending on your application and problem domain, you can use different approaches to handle missing data – like interpolation, substituting with the mean, or simply removing the rows with missing values. 

Pandas offers the `dropna` function which removes all rows (for axis=0) or all columns (for axis=1) where missing values are present. Some of the arguments for the dropna function are as follows:

* `axis` which specifies if rows are to be dropped (axis=0) or if columns are to be dropped (axis=1)
* `subset` which specifies a list of columns to consider for missing values when axis=0
* `inplace` which specifies if changes are to be made in the existing DataFrame itself

Check out the docs linked [here](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html) for more in-depth coverage. 

In the example below, we're creating a small DataFrame with missing values and then discarding rows with missing values in any column.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-4.png)
_Drop missing values in Pandas_

## How to Remove Duplicates in DataFrame

Another common data cleaning task is removing duplicate rows. The `drop_duplicates` function performs this with arguments similar to `dropna` such as:

* `subset`, which specifies a subset of columns to consider for duplicate value when axis=0
* `inplace`
* `keep`, which specifies which duplicated values to keep. Keep can be equal to first, last, or False to drop all duplicates.

Check out the docs linked [here](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop_duplicates.html) for more detailed info. 

Let's duplicate a few rows and remove them from our dataset:

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-5.png)
_Drop duplicate values in Pandas_

## How to Remove Rows with Column-specific Values

Suppose we want to keep only those rows where project type is Web or where the number of hours worked is equal to 12. Here's how we can do it. 

Using this method, we can filter out rows based on certain specific column values:

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-8.png)
_Remove rows with column specific values_

## How to Convert DataFrames to JSON

DataFrames are super cool optimized structures that are great to work with. And JSON is one of the most popular data formats for seamless data exchange. 

Let's convert our DataFrame to JSON using [`to_json`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_json.html) which requires arguments like:

* `orient`, which specifies what should be the key and value pairs. Default is columns, so column name is the key and each column is the value.
* `date_format` which specifies the format of the date. The default is epoch. 

Look at the example below:

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-11.png)
_Convert DataFrame to JSON_

We can see that `to_json` has returned a string with the following schema:

```
column_0 :
{ row_index_0: column_value_0, row_index_1:column_value_1, ...}, 
column_1:
{ row_index_0: column_value_0, row_index_1:column_value_1, ...}, 
...
column_N:
{ row_index_0: column_value_0, row_index_1:column_value_1, ...}
   
```

If we want to convert each row to a dictionary, we need to specify that `orient=records` and parse it using the JSON module.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-12.png)
_Convert DataFrame to JSON with orient=records_

## How to Count the Number of Unique Values in a Column

Let's say we want to know how many different project types exist. We can get that information using the `nunique` function.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-13.png)
_Count number of unique values in a column_

## How to Save DataFrame as .csv File

Just one line of code is required to save the DataFrame as a csv file:

```
dataset.to_csv("save_as_csv.csv")
```

## How to Save Multiple Lists as One .csv File

Suppose we have three separate lists as our data source and we want to save them together in one csv file. This just involves two steps:

* converting it to a number of tuples using zip, 
* and then converting it to a list.

In the example below, we follow this approach to convert the three lists into one DataFrame which we can now save as a .csv file.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-15.png)
_Save multiple lists as one csv file_

### How to Read DataFrames in a Memory Efficient Way

Often we need to read files which are so large that they can't fit into memory. For such mammoth datasets, we use a different approach. 

First, we create a `TextFileReader` object. Next we specify a parameter called `chunksize` which specifies how many rows of the file we want to read at a time, let's say 4 rows. So we read 4 rows at a time, perform some tasks on that chunk, and move on to the next 4 rows. 

Small chunks are more likely to fit into memory than the entire file of thousands of rows. The following example shows how chunking works.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-16.png)
_Read DataFrame in a memory efficient manner_

Here we read the `california` dataset 1000 rows at a time, remove all rows where `median_income` is less than or equal to 3, and append these reduced chunks together to make a smaller dataset. 

You can save more memory by reading only those columns which you need and specifying smaller datatypes for columns as described in detail in the docs linked [here](https://pandas.pydata.org/pandas-docs/stable/user_guide/scale.html).

## How to Change All Values in a DataFrame Using `apply`

Let's go back to our example of a projects DataFrame to illustrate this. We focus on the `Hours_Worked` column, increasing the count by 1 if it's an even number and by 2 if it's an odd number. We use a lambda function for this purpose.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-17.png)
_Change all values in a DataFrame using apply_

## Conclusion

Pandas is a powerful package which can seem daunting sometimes due to its vastness. This is why I tried to list out some of the most useful functions I've come across. 

These Pandas functions will help you accelerate your data analysis endeavors. Thank you for your time and I hope you enjoyed reading this article. 

### 



### 

