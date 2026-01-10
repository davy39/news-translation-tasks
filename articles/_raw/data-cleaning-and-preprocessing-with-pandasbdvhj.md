---
title: How to Use Pandas for Data Cleaning and Preprocessing
subtitle: ''
author: Oluwadamisi Samuel
co_authors: []
series: null
date: '2024-01-30T14:55:00.000Z'
originalURL: https://freecodecamp.org/news/data-cleaning-and-preprocessing-with-pandasbdvhj
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/Cream-Neutral-Minimalist-New-Business-Pitch-Deck-Presentation--1-.png
tags:
- name: data
  slug: data
- name: data analysis
  slug: data-analysis
- name: pandas
  slug: pandas
- name: Python
  slug: python
seo_title: null
seo_desc: 'Steve Lohr of The New York Times said: "Data scientists, according to interviews
  and expert estimates, spend 50 percent to 80 percent of their time mired in the
  mundane labor of collecting and preparing unruly digital data, before it can be
  explored ...'
---

Steve Lohr of The New York Times said: "Data scientists, according to interviews and expert estimates, spend 50 percent to 80 percent of their time mired in the mundane labor of collecting and preparing unruly digital data, before it can be explored for useful nuggets."

This statement is 100% accurate, as this encompasses a series of steps that ensure data used for data science, machine learning and analysis projects are complete, accurate, unbiased and reliable.

The quality of your dataset plays a pivotal role in the success of your analysis or model. As the saying goes, “garbage in, garbage out”, the quality and reliability of your model and analysis heavily depends on the quality of your data.

Raw data, collected from various sources, are often messy, contain errors, inconsistencies, missing values and outliers. Data cleaning and preprocessing aims to identify and rectify these issues to ensure accurate, reliable and meaningful results during model building and data analysis as wrong conclusions could be costly.

This is where Pandas comes into play, it is a wonderful tool used in the data world to do both data cleaning and preprocessing. In this article, we'll delve into the essential concepts of data cleaning and preprocessing using the powerful Python library, Pandas.

## Table of Contents

* [Prerequisites](#heading-prerequisites)
    
* [Introduction](#heading-introduction)
    
* [What is Data Cleaning?](#heading-what-is-data-cleaning)
    
* [What is Data Processing?](#heading-what-is-data-processing)
    
* [How to Import the Necessary Libraries](#heading-how-to-import-the-necessary-libraries)
    
* [How to Load the Dataset](#heading-how-to-load-the-dataset)
    
* [Exploratory Data Analysis (EDA)](#heading-exploratory-data-analysis-eda)
    
* [How to Handle Missing Values](#heading-how-to-handle-missing-values)
    
* [How to Remove Duplicate Records](#heading-how-to-remove-duplicate-records)
    
* [Data Types and Conversion](#heading-data-types-and-conversion)
    
* [How to Encode Categorical Variables](#heading-how-to-encode-categorical-variables)
    
* [How to Handle Outliers](#heading-how-to-handle-outliers)
    
* [Conclusion](#heading-conclusion)
    

## Prerequisites

* A basic understanding of Python.
    
* Basic understanding of data cleaning.
    

## Introduction

Pandas is a popular open-source data manipulation and analysis library for Python. It provides easy-to-use functions needed to work with structured data seamlessly.

Pandas also integrates seamlessly with other popular Python libraries, such as NumPy for numerical computing and Matplotlib for data visualization. This makes it a powerful asset for data driven tasks.

Pandas excels in handling missing data, reshaping datasets, merging and joining multiple datasets, and performing complex operations on data, making it exceptionally useful for data cleaning and manipulation.

At its core, Pandas introduces two key data structures: `Series` and `DataFrame`. A `Series` is a one-dimensional array-like object that can hold any data type, while a `DataFrame` is a two-dimensional table with labeled axes (rows and columns). These structures allow users to manipulate, clean, and analyze datasets efficiently.

## What is Data Cleaning?

Before we embark on our data adventure with Pandas, let's take a moment to explain the term "data cleaning." Think of it as the digital detox for your dataset, where we tidy up, and and prioritize accuracy above all else.

Data cleaning involves identifying and rectifying errors, inconsistencies, and missing values within a dataset. It's like preparing your ingredients before cooking; you want everything in order to get the perfect analysis or visualization.

Why bother with data cleaning? Well, imagine trying to analyze sales trends when some entries are missing, or working with a dataset that has duplicate records throwing off your calculations. Not ideal, right?

In this digital detox, we use tools like Pandas to get rid of inconsistencies, straighten out errors, and let the true clarity of your data shine through.

## What is Data Processing?

You may be wondering, "Does data cleaning and data preprocessing mean the same thing?" The answer is no – they do not.

Picture this: you stumble upon an ancient treasure chest buried in the digital sands of your dataset. Data cleaning is like carefully unearthing that chest, dusting off the cobwebs, and ensuring that what's inside is authentic and reliable.

As for data preprocessing, you can think of it as taking that discovered treasure and preparing its contents for public display. It goes beyond cleaning; it's about transforming and optimizing the data for specific analyses or tasks.

Data cleaning is the initial phase of refining your dataset, making it readable and usable with techniques like removing duplicates, handling missing values and data type conversion while data preprocessing is similar to taking this refined data and scaling with more advanced techniques such as feature engineering, encoding categorical variables and and handling outliers to achieve better and more advanced results.

The goal is to turn your dataset into a refined masterpiece, ready for analysis or modeling.

## How to Import the Necessary Libraries

Before we embark on data cleaning and preprocessing, let's import the `Pandas` library.

To save time and typing, we often import Pandas as `pd`. This lets us use the shorter `pd.read_csv()` instead of `pandas.read_csv()` for reading CSV files, making our code more efficient and readable.

```py
import pandas as pd
```

## How to Load the Dataset

Start by loading your dataset into a Pandas DataFrame.

In this example, we'll use a hypothetical dataset named **your\_dataset.csv**. We will load the dataset into a variable called `df`.

```py
#Replace 'your_dataset.csv' with the actual dataset name or file path
df = pd.read_csv('your_dataset.csv')
```

## Exploratory Data Analysis (EDA)

EDA helps you understand the structure and characteristics of your dataset. Some Pandas functions help us gain insights into our dataset. We call these functions by calling the dataset variable plus the function.

For example:

* `df.head()` will call the first 5 rows of the dataset. You can specify the number of rows to be displayed in the parentheses.
    
* `df.describe()` gives some statistical data like percentile, mean and standard deviation of the numerical values of the Series or DataFrame.
    
* `df.info()` gives the number of columns, column labels, column data types, memory usage, range index, and the number of cells in each column (non-null values).
    

Here's a code example below:

```py
#Display the first few rows of the dataset
print(df.head())

#Summary statistics
print(df.describe())

#Information about the dataset
print(df.info())
```

## How to Handle Missing Values

As a newbie in this field, missing values pose a significant stress as they come in different formats and can adversely impact your analysis or model.

Machine learning models cannot be trained with data that has missing or "NAN" values as they can alter your end result during analysis. But do not fret, Pandas provides methods to handle this problem.

One way to do this is by removing the missing values altogether. Code snippet below:

```py
#Check for missing values
print(df.isnull().sum())

#Drop rows with missing valiues and place it in a new variable "df_cleaned"
df_cleaned = df.dropna()

#Fill missing values with mean for numerical data and place it ina new variable called df_filled
df_filled = df.fillna(df.mean())
```

But if the number of rows that have missing values is large, then this method will be inadequate.

For numerical data, you can simply compute the mean and input it into the rows that have missing values. Code snippet below:

```py
#Replace missing values with the mean of each column
df.fillna(df.mean(), inplace=True)

#If you want to replace missing values in a specific column, you can do it this way:
#Replace 'column_name' with the actual column name
df['column_name'].fillna(df['column_name'].mean(), inplace=True)

#Now, df contains no missing values, and NaNs have been replaced with column mean
```

## How to Remove Duplicate Records

Duplicate records can distort your analysis by influencing the results in ways that do not accurately show trends and underlying patterns (by producing outliers).

Pandas helps to identify and remove the duplicate values in an easy way by placing them in new variables.

Code snippet below:

```py
#Identify duplicates
print(df.duplicated().sum())

#Remove duplicates
df_no_duplicates = df.drop_duplicates()
```

## Data Types and Conversion

Data type conversion in Pandas is a crucial aspect of data preprocessing, allowing you to ensure that your data is in the appropriate format for analysis or modeling.

Data from various sources are usually messy and the data types of some values may be in the wrong format, for example some numerical values may come in 'float' or 'string' format instead of 'integer' format and a mix up of these formats leads to errors and wrong results.

You can convert a Column of type `int` to `float` with the following code:

```py
#Convert 'Column1' to float
df['Column1'] = df['Column1'].astype(float)

#Display updated data types
print(df.dtypes)
```

You can use `df.dtypes` to print column data types.

## How to Encode Categorical Variables

For machine learning algorithms, having categorical values in your dataset (non-numerical values) is crucial in ensuring the best model as they are equally as important.

These could be car brand names in a cars dataset for predicting car prices. But machine learning algorithms cannot processes this datatype, therefore it must be converted to numerical data before it can be used.

Pandas provides the `get_dummies` function which converts categorical values into numerical format(Binary format) such that it is recognized by the algorithm as a placeholder for values and not hierarchical data that can undergo numerical analysis. this just means that the numbers the brand name is converted to is not interpreted as 1 is greater than 0, but it tells the algorithm that both 1 and 0 are placeholders for categorical data. Code snippet is shown below:

```py
#To convert categorical data from the column "Car_Brand" to numerical data
df_encode = pd.get_dummies(df, columns=[Car_Brand])

#The categorical data is converted to binary format of Numerical data
```

## How to Handle Outliers

Outliers are data points significantly different from the majority of the data, they can distort statistical measures and adversely affect the performance of machine learning models.

They may be caused by human error, missing NaN values, or could be accurate data that does not correlate with the rest of the data.

There are several methods to identify and remove outliers, they are:

* Remove NaN values.
    
* Visualize the data before and after removal.
    
* Z-score method (for normally distributed data).
    
* IQR (Interquartile range) method for more robust data.
    

The IQR is useful for identifying outliers in a dataset. According to the IQR method, values that fall below Q1−1.5× IQR or above Q3+1.5×IQR are considered outliers.

This rule is based on the assumption that most of the data in a normal distribution should fall within this range.

Here's a code snippet for the IQR method:

```py
#Using median calculations and IQR, outliers are identified and these data points should be removed
Q1 = df["column_name"].quantile(0.25)
Q3 = df["column_name"].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
df = df[df["column_name"].between(lower_bound, upper_bound)]
```

## Conclusion

Data cleaning and preprocessing are integral components of any data analysis, science or machine learning project. Pandas, with its versatile functions, facilitates these processes efficiently.

By following the concepts outlined in this article, you can ensure that your data is well-prepared for analysis and modeling, ultimately leading to more accurate and reliable results.
