---
title: pandas.DataFrame.sort_values - How To Sort Values in Pandas
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-03-13T21:52:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-sort-values-in-pandas
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/sort-in-pandas-1.png
tags:
- name: pandas
  slug: pandas
- name: Python
  slug: python
seo_title: null
seo_desc: 'When analyzing and manipulating data using Pandas, you might want to sort
  the data in a certain order. This makes it easier to understand and visualize data.

  In this article, you''ll learn how to sort data in ascending and descending order
  using Panda...'
---

When analyzing and manipulating data using Pandas, you might want to sort the data in a certain order. This makes it easier to understand and visualize data.

In this article, you'll learn how to sort data in ascending and descending order using Pandas' `sort_values()` method. 

## How To Sort Values in Pandas

You can use the `sort_values()` method to sort values in a data set. By default, the method sorts values in ascending order. 

In this section, you'll learn how to sort data in ascending and descending order using the `sort_values()` method. 

### How To Sort Values in Ascending Order Using Pandas `sort_values()` Method

The `sort_values()` method takes in multiple parameters, as can be seen in the [Pandas documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html). 

We'll focus on the `by` and `ascending` parameters. That is:

```txt
Dataframe.sort_values(by, ascending)
```

* The `by` parameter denotes the column or index to sort. 
* `ascending` is used to specify what other the values should be sorted in. By default, it is set to `True`. 

Here's an example:

```python
import pandas as pd

# create a sample dataframe
data = {'cost': [50000, 30000, 70000, 60000]}

df = pd.DataFrame(data)

df
```

|    |      item      |  cost |
|----------|:-------------:|------:|
| 0 | laptop | 500 |
| 1 | monitor | 300 |
| 2 | HDMI | 700 |
| 3 | speaker | 600 |

In the table above, we have different items along with the cost of each item. To sort the items in ascending order using their cost, you can do this:

```python
import pandas as pd

data = {'item': ['laptop', 'monitor', 'HDMI', 'speaker'],
        'cost': [500, 300, 700, 600]
       }

df = pd.DataFrame(data)

sorted_data = df.sort_values(by='cost', ascending=True)

sorted_data


```

|    |      item      |  cost |
|----------|:-------------:|------:|
| 1 | monitor | 300 |
| 0 | laptop | 500 |
| 3 | speaker | 600 |
| 2 | HDMI | 700 |

In the code above, the `sort_values()` method was used to sort the `cost` column.

* Using the `by` parameter, we specified which column was to be sorted:  `by='cost'`
* Using the `ascending` parameter, we set the order of the data to be sorted: `ascending=True`. 

Note that the default order of the `sort_values()` method is `ascending=True`. So if you remove `ascending` parameter, you'd still have the values sorted in ascending order. 

### How To Sort Values in Descending Order Using Pandas `sort_values()` Method

You can sort values in descending order by simply setting the `ascending` parameter to `False`. 

We'll work with the same code in the last section:

```python
import pandas as pd

# create a sample dataframe
data = {'cost': [50000, 30000, 70000, 60000]}

df = pd.DataFrame(data)

df
```

|    |      item      |  cost |
|----------|:-------------:|------:|
| 0 | laptop | 500 |
| 1 | monitor | 300 |
| 2 | HDMI | 700 |
| 3 | speaker | 600 |

Here's the code for sorting the `cost` column in descending order:

```python
import pandas as pd

data = {'item': ['laptop', 'monitor', 'HDMI', 'speaker'],
        'cost': [500, 300, 700, 600]
       }

df = pd.DataFrame(data)

sorted_data = df.sort_values(by='cost', ascending=False)

sorted_data


```

|    |      item      |  cost |
|----------|:-------------:|------:|
| 2 | HDMI | 700 |
| 3 | speaker | 600 |
| 0 | laptop | 500 |
| 1 | monitor | 300 |

By setting the value of the `ascending` parameter to `False`, we've sorted the data by cost in descending order. 

## Summary

In this article, we learned about sorting values in Pandas using the `sort_values()` method.

We saw two code examples on how to sort data in Pandas in ascending or descending order.

You can use the `sort_values()` method's `ascending` parameter to sort data in ascending or descending order. 

Happy coding!

