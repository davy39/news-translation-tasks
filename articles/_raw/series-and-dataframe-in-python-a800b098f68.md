---
title: Series and DataFrame in Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-10T20:03:08.000Z'
originalURL: https://freecodecamp.org/news/series-and-dataframe-in-python-a800b098f68
coverImage: https://cdn-media-1.freecodecamp.org/images/1*QH4RGlNwXUFnJSytytvb6A.jpeg
tags:
- name: data
  slug: data
- name: Data Science
  slug: data-science
- name: Python
  slug: python
- name: technology
  slug: technology
- name: women in tech
  slug: women-in-tech
seo_title: null
seo_desc: 'By Shubhi Asthana

  A couple of months ago, I took the online course “Using Python for Research” offered
  by Harvard University on edX. While taking the course, I learned many concepts of
  Python, NumPy, Matplotlib, and PyPlot. I also had an opportunity ...'
---

By Shubhi Asthana

A couple of months ago, I took the online course “Using Python for Research” offered by Harvard University on edX. While taking the course, I learned many concepts of Python, NumPy, Matplotlib, and PyPlot. I also had an opportunity to work on case studies during this course and was able to use my knowledge on actual datasets. For more information about this program, check out [here](https://courses.edx.org/courses/course-v1:HarvardX+PH526x+3T2016/4bdcc373b7a944f8861a3f190c10edca/).

I learned two important concepts in this course — Series and DataFrame. I want to introduce these to you through a short tutorial.

To start with the tutorial, lets get the latest source code of Python from the official website [here](https://www.python.org/).

Once you’ve installed Python is installed, you’ll use a graphical user interface called [IDLE](https://www.python.org/downloads/) to work with Python.

Let’s import Pandas to our workspace. [Pandas](https://pandas.pydata.org/pandas-docs/stable/install.html) is a Python library that provides data structures and data analysis tools for different functions.

### **Series**

A Series is a one-dimensional object that can hold any data type such as integers, floats and strings. Let’s take a list of items as an input argument and create a Series object for that list.

```
>>> import pandas as pd
```

```
>>> x = pd.Series([6,3,4,6])
```

```
>>> x
```

```
0 6
```

```
1 3
```

```
2 4
```

```
3 6
```

```
dtype: int64
```

The axis labels for the data as referred to as the index. The length of index must be the same as the length of data. Since we have not passed any index in the code above, the default index will be created with values `[0, 1, … len(data) -1]`

Lets go ahead and define indexes for the data.

```
>>> x = pd.Series([6,3,4,6], index=[‘a’, ‘b’, ‘c’, ‘d’])
```

```
>>> x
```

```
a 6
```

```
b 3
```

```
c 4
```

```
d 6
```

```
dtype: int64
```

The index in left most column now refers to data in the right column.

We can lookup the data by referring to its index:

```
>>> x[“c”]
```

```
4
```

Python gives us the relevant data for the index.

One example of a data type is the dictionary defined below. The index and values correlate to keys and values. We can use the index to get the values of data corresponding to the labels in the index.

```
>>> data = {‘abc’: 1, ‘def’: 2, ‘xyz’: 3}
```

```
>>> pd.Series(data)
```

```
abc 1
```

```
def 2
```

```
xyz 3
```

```
dtype: int64
```

Another interesting feature in Series is having data as a scalar value. In that case, the data value gets repeated for each of the indexes defined.

```
>>> x = pd.Series(3, index=[‘a’, ‘b’, ‘c’, ‘d’])
```

```
>>> x
```

```
a 3
```

```
b 3
```

```
c 3
```

```
d 3
```

```
dtype: int64
```

### **DataFrame**

A DataFrame is a two dimensional object that can have columns with potential different types. Different kind of inputs include dictionaries, lists, series, and even another DataFrame.

It is the most commonly used pandas object.

Lets go ahead and create a DataFrame by passing a NumPy array with datetime as indexes and labeled columns:

```
>>> import numpy as np
```

```
>>> dates = pd.date_range(‘20170505’, periods = 8)
```

```
>>> dates
```

```
DatetimeIndex([‘2017–05–05’, ‘2017–05–06’, ‘2017–05–07’, ‘2017–05–08’,
```

```
‘2017–05–09’, ‘2017–05–10’, ‘2017–05–11’, ‘2017–05–12’],
```

```
dtype=’datetime64[ns]’, freq=’D’)
```

```
>>> df = pd.DataFrame(np.random.randn(8,3), index=dates, columns=list(‘ABC’))
```

```
>>> df
```

```
A B C
```

```
2017–05–05 -0.301877 1.508536 -2.065571
```

```
2017–05–06 0.613538 -0.052423 -1.206090
```

```
2017–05–07 0.772951 0.835798 0.345913
```

```
2017–05–08 1.339559 0.900384 -1.037658
```

```
2017–05–09 -0.695919 1.372793 0.539752
```

```
2017–05–10 0.275916 -0.420183 1.744796
```

```
2017–05–11 -0.206065 0.910706 -0.028646
```

```
2017–05–12 1.178219 0.783122 0.829979
```

A DataFrame with a datetime range of 8 days gets created as shown above. We can view the top and bottom rows of the frame using `df.head` and `df.tail`:

```
>>> df.head()
```

```
A B C
```

```
2017–05–05 -0.301877 1.508536 -2.065571
```

```
2017–05–06 0.613538 -0.052423 -1.206090
```

```
2017–05–07 0.772951 0.835798 0.345913
```

```
2017–05–08 1.339559 0.900384 -1.037658
```

```
2017–05–09 -0.695919 1.372793 0.539752
```

```
>>> df.tail()
```

```
A B C
```

```
2017–05–08 1.339559 0.900384 -1.037658
```

```
2017–05–09 -0.695919 1.372793 0.539752
```

```
2017–05–10 0.275916 -0.420183 1.744796
```

```
2017–05–11 -0.206065 0.910706 -0.028646
```

```
2017–05–12 1.178219 0.783122 0.829979
```

We can observe a quick statistic summary of our data too:

```
>>> df.describe()
```

```
A B C
```

```
count 8.000000 8.000000 8.000000
```

```
mean 0.372040 0.729842 -0.109691
```

```
std 0.731262 0.657931 1.244801
```

```
min -0.695919 -0.420183 -2.065571
```

```
25% -0.230018 0.574236 -1.079766
```

```
50% 0.444727 0.868091 0.158633
```

```
75% 0.874268 1.026228 0.612309
```

```
max 1.339559 1.508536 1.744796
```

We can also apply functions to the data like cumulative sum, view histograms, merging DataFrames, concatenating and reshaping DataFrames.

```
>>> df.apply(np.cumsum)
```

```
A B C
```

```
2017–05–05 -0.301877 1.508536 -2.065571
```

```
2017–05–06 0.311661 1.456113 -3.271661
```

```
2017–05–07 1.084612 2.291911 -2.925748
```

```
2017–05–08 2.424171 3.192296 -3.963406
```

```
2017–05–09 1.728252 4.565088 -3.423654
```

```
2017–05–10 2.004169 4.144905 -1.678858
```

```
2017–05–11 1.798104 5.055611 -1.707504
```

```
2017–05–12 2.976322 5.838734 -0.877526
```

You can read more details about these data structures [here](http://pandas.pydata.org/pandas-docs/stable/dsintro.html).

