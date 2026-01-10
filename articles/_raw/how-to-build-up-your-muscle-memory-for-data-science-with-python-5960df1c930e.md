---
title: How to build up your muscle memory for Data Science with Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-22T23:38:30.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-up-your-muscle-memory-for-data-science-with-python-5960df1c930e
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca8fb740569d1a4ca819a.jpg
tags:
- name: Data Science
  slug: data-science
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'self-improvement '
  slug: self-improvement
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Zhen Liu

  Up first: data preprocessing

  Do you feel frustrated by breaking your data analytics flow when searching for syntax?
  Why do you still not remember it after looking up it for the third time?? It’s because
  you haven’t practiced it enough to ...'
---

By Zhen Liu

#### Up first: data preprocessing

Do you feel frustrated by breaking your data analytics flow when searching for syntax? Why do you still not remember it after looking up it for the third time?? It’s because you haven’t practiced it enough to build muscle memory for it yet.

Now, imagine that when you are coding, the Python syntax and functions just fly out from your fingertips following your analytical thoughts. How great is that! This tutorial is to help you get there.

I recommend practicing this script every morning for 10 mins, and repeating it for a week. **It’s like doing a few small crunches a day — not for your abs, but for your data science muscles.** Gradually, you’ll notice the improvement in data analytics programming efficiency after this repeat training.

To begin with my ‘data science workout’, in this tutorial we’ll practice the most common syntax for **data preprocessing** as a warm-up session ;)

```
Contents:
```

```
0 . Read, View and Save data1 . Table’s Dimension and Data Types2 . Basic Column Manipulation3 . Null Values: View, Delete and Impute4 . Data Deduplication
```

### 0. Read, View and Save data

First, load the libraries for our exercise:

Now we’ll read data from my GitHub repository. I downloaded the data from [Zillow](https://www.zillow.com/research/data/#other-metrics).

And the results look like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*eaM_mFSWaGj89cAvF7Bnsg.png)

Saving a file is dataframe.to_csv(). If you don’t want the index number to be saved, use dataframe.to_csv( index = False ).

### 1 . Table’s Dimension and Data Types

#### 1.1 Dimension

How many rows and columns in this data?

#### 1.2 Data Types

What are the data types of your data, and how many columns are numeric?

Output of the first few columns’ data types:

![Image](https://cdn-media-1.freecodecamp.org/images/1*JLYBz5WpEUcFGHdCPlXJGg.png)

If you want to be more specific about your data, use select_dtypes() to include or exclude a data type. Question: if I only want to look at 2018’s data, how do I get that?

### 2. Basic Column Manipulation

#### 2.1 Subset data by columns

Select columns by data types:

For example, if you only want float and integer columns:

![Image](https://cdn-media-1.freecodecamp.org/images/1*bBq6iH8R-W4g6Cd3HP674g.png)

Select and drop columns by names:

![Image](https://cdn-media-1.freecodecamp.org/images/1*d795R8XUxwjkwc1nVRUgGQ.png)

#### 2.2 Rename Columns

How do I rename the columns if I don’t like them? For example, change ‘State’ to ‘state_’; ‘City’ to ‘city_’:

### 3. Null Values: View, Delete and Impute

#### 3.1 How many rows and columns have null values?

The outputs of isnull.any() versus isnull.sum():

![Image](https://cdn-media-1.freecodecamp.org/images/1*jyJODeWUJR1k4-GQk7tRrw.png)
_isnull.any()_

![Image](https://cdn-media-1.freecodecamp.org/images/1*fun7aRvU3jjbtKmBZmKsag.png)
_isnull.sum()_

Select data that isn’t null in one column, for example, ‘Metro’ isn’t null.

![Image](https://cdn-media-1.freecodecamp.org/images/1*VqOIxXhSLWhSKxbRNG35-A.png)
_Rows with N/A ‘Metro’ values_

#### 3.2 Select rows that are not null for a fixed set of columns

Select a subset of data that doesn’t have null after 2000:

If you want to select the data in July, you need to find the columns containing ‘-07’. To see if a string contains a substring, you can use substring in string, and it’ll output true or false.

![Image](https://cdn-media-1.freecodecamp.org/images/1*3nalUQfXwC_Ywa-r8YsJ0w.png)

#### 3.3 Subset Rows by Null Values

Select rows where we want to have at least 50 non-NA values, but don’t need to be specific about the columns:

#### 3.4 Drop and Impute Missing Values

Fill NA or impute NA:

Use your own condition to fill using the where function:

### 4. Data Deduplication

We need to make sure there’s no duplicated rows before we aggregate data or join them.

We want to see whether there are any duplicated cities/regions. We need to decide what unique ID (city, region) we want to use in the analysis.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GhiZCDmg_I-nE8vowIIGsA.png)
_Set keep=False to see all the duplicated rows by ‘RegionName’_

#### Drop Duplicated values.

The ‘CountyName’ and ‘SizeRank’ combination is unique already. So we just use the columns to demonstrate the syntax of drop_duplicated.

That’s it for the first part of my series on building muscle memory for data science in Python. _The full script can be found [here](https://gist.github.com/zhendata/5d73068e5b31b616938af51bedf65382)._

Stay tuned! My next tutorial will show you how to ‘curl the data science muscles’ for slicing and dicing data.

Follow me and give me a few claps if you find this helpful :)

While you are working on Python, maybe you’ll be interested in my previous article:

[**Learn Spark for Big Data Analytics in 15 mins！**](https://towardsdatascience.com/learn-spark-essentials-in-15-mins-cf1495882ae0)  
[_I guarantee you that this short tutorial will save you a TON of time from reading the long documentations. Ready to…_towardsdatascience.com](https://towardsdatascience.com/learn-spark-essentials-in-15-mins-cf1495882ae0)

