---
title: Pandas round() Method – How To Round a Float in Pandas
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-03-13T21:49:09.000Z'
originalURL: https://freecodecamp.org/news/how-to-round-a-float-in-pandas
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/round-float-in-pandas.png
tags:
- name: float
  slug: float
- name: pandas
  slug: pandas
- name: Python
  slug: python
seo_title: null
seo_desc: "You can use the Pandas library in Python to manipulate and analyze data.\
  \ In most cases, it is used for manipulating and analyzing tabular data. \nIn this\
  \ article, you'll learn how to use the Pandas round() method to round a float value\
  \ to a specified ..."
---

You can use the Pandas library in Python to manipulate and analyze data. In most cases, it is used for manipulating and analyzing tabular data. 

In this article, you'll learn how to use the Pandas `round()` method to round a float value to a specified number of decimal places. 

We'll begin by looking the method's syntax, and then see some practical code applications. 

## Pandas `round()` Method Example

Here's what the syntax for the `round()` method looks like:

```txt
DataFrame.round(decimals)
```

The **decimals** parameter represents the number of decimal places a number should be rounded to.

The number of decimal places to be returned is passed in as a parameter. `round(2)` return rounds a number to two decimal places. 

Here's an example to demonstrate:

```python
import pandas as pd

data = {'cost':[20.5550, 21.03535, 19.67373, 18.233233]}
  
df = pd.DataFrame(data)

df['rounded_cost'] = df['cost'].round(2)
print(df)
```

In the code above, we have a list of numbers that fall under the `cost` column. The column had these values: [20.5550, 21.03535, 19.67373, 18.233233]. 

Using the `round()` method, we rounded the values to 2 decimal places: `df['cost'].round(2)`. 

The return values were stored in a column called `rounded_cost`. 

Here's the output of the code:

|    |      cost      |  rounded_cost |
|----------|:-------------:|------:|
| 0 | 20.555000 | 20.56 |
| 1 | 21.035350 | 21.04 |
| 2 | 19.673730 | 19.67 |
| 3 | 18.233233 | 18.23 |

From the table above, you can see that the values in the `cost` column have been rounded to 2 decimal places in the `rounded_cost` columns. 

## Summary

In this article, we have learned about rounding float values with Pandas using the `round()` method. 

We started looking at the syntax for the `round()` method looks like. We then saw an example using the method to round float values to a specified number of decimal places. 

Happy coding!


