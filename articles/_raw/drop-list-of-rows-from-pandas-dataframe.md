---
title: Data Analytics with Pandas – How to Drop a List of Rows from a Pandas Dataframe
subtitle: ''
author: Vikram Aruchamy
co_authors: []
series: null
date: '2021-06-01T20:47:43.000Z'
originalURL: https://freecodecamp.org/news/drop-list-of-rows-from-pandas-dataframe
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/cut_lemons--1-.jpg
tags:
- name: data analysis
  slug: data-analysis
- name: data analytics
  slug: data-analytics
- name: dataframe
  slug: dataframe
- name: pandas
  slug: pandas
seo_title: null
seo_desc: 'A Pandas dataframe is a two dimensional data structure which allows you
  to store data in rows and columns. It''s very useful when you''re analyzing data.

  When you have a list of data records in a dataframe, you may need to drop a specific
  list of rows ...'
---

A Pandas dataframe is a two dimensional data structure which allows you to store data in rows and columns. It's very useful when you're analyzing data.

When you have a list of data records in a dataframe, you may need to drop a specific list of rows depending on the needs of your model and your goals when studying your analytics. 

In this tutorial, you'll learn how to drop a list of rows from a Pandas dataframe. 

To learn how to drop columns, you can read here about [How to Drop Columns in Pandas](https://www.stackvidhya.com/drop-column-in-pandas/). 

## How to Drop a Row or Column in a Pandas Dataframe

To drop a row or column in a dataframe, you need to use the `drop()` method available in the dataframe. You can read more about the `drop()` method in the docs [here](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html). 

**Dataframe Axis**

 -  Rows are denoted using `axis=0`
 -  Columns are denoted using `axis=1`

**Dataframe Labels**

 - Rows are labelled using the index number starting with 0, by default.
 - Columns are labelled using names. 

**Drop() Method Parameters**

 - `index` - the list of rows to be deleted
 - `axis=0` - Marks the rows in the dataframe to be deleted
 - `inplace=True` - Performs the drop operation in the same dataframe, rather than creating a new dataframe object during the delete operation. 

### Sample Pandas DataFrame

Our sample dataframe contains the columns *product_name*, *Unit_Price*, *No_Of_Units*, *Available_Quantity*, and *Available_Since_Date* columns. It also has rows with NaN values which are used to denote missing values. 

```python
import pandas as pd

data = {"product_name":["Keyboard","Mouse", "Monitor", "CPU","CPU", "Speakers",pd.NaT],
        "Unit_Price":[500,200, 5000.235, 10000.550, 10000.550, 250.50,None],
        "No_Of_Units":[5,5, 10, 20, 20, 8,pd.NaT],
        "Available_Quantity":[5,6,10,"Not Available","Not Available", pd.NaT,pd.NaT],
        "Available_Since_Date":['11/5/2021', '4/23/2021', '08/21/2021','09/18/2021','09/18/2021','01/05/2021',pd.NaT]
       }

df = pd.DataFrame(data)

df
```

The dataframe will look like this:

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>product_name</th>
      <th>Unit_Price</th>
      <th>No_Of_Units</th>
      <th>Available_Quantity</th>
      <th>Available_Since_Date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Keyboard</td>
      <td>500.000</td>
      <td>5</td>
      <td>5</td>
      <td>11/5/2021</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Mouse</td>
      <td>200.000</td>
      <td>5</td>
      <td>6</td>
      <td>4/23/2021</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Monitor</td>
      <td>5000.235</td>
      <td>10</td>
      <td>10</td>
      <td>08/21/2021</td>
    </tr>
    <tr>
      <th>3</th>
      <td>CPU</td>
      <td>10000.550</td>
      <td>20</td>
      <td>Not Available</td>
      <td>09/18/2021</td>
    </tr>
    <tr>
      <th>4</th>
      <td>CPU</td>
      <td>10000.550</td>
      <td>20</td>
      <td>Not Available</td>
      <td>09/18/2021</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Speakers</td>
      <td>250.500</td>
      <td>8</td>
      <td>NaT</td>
      <td>01/05/2021</td>
    </tr>
    <tr>
      <th>6</th>
      <td>NaT</td>
      <td>NaN</td>
      <td>NaT</td>
      <td>NaT</td>
      <td>NaT</td>
    </tr>
  </tbody>
</table>
</div>

And just like that we've created our sample dataframe. 

After each drop operation, you'll print the dataframe by using `df` which will print the dataframe in a regular `HTML` table format. 

You can read here about how to [Pretty Print a Dataframe](https://www.stackvidhya.com/pretty-print-dataframe/) to print the dataframe in different visual formats. 

Next, you'll learn how to drop a list of rows in different use cases. 

## How to Drop a List of Rows by Index in Pandas

You can delete a list of rows from Pandas by passing the list of indices to the `drop()` method. 

```python
df.drop([5,6], axis=0, inplace=True)

df
```

In this code,

 - `[5,6]` is the index of the rows you want to delete
 - `axis=0` denotes that rows should be deleted from the dataframe
 - `inplace=True` performs the drop operation in the same dataframe

After dropping rows with the index 5 and 6, you'll have the below data in the dataframe:


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>product_name</th>
      <th>Unit_Price</th>
      <th>No_Of_Units</th>
      <th>Available_Quantity</th>
      <th>Available_Since_Date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Keyboard</td>
      <td>500.000</td>
      <td>5</td>
      <td>5</td>
      <td>11/5/2021</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Mouse</td>
      <td>200.000</td>
      <td>5</td>
      <td>6</td>
      <td>4/23/2021</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Monitor</td>
      <td>5000.235</td>
      <td>10</td>
      <td>10</td>
      <td>08/21/2021</td>
    </tr>
    <tr>
      <th>3</th>
      <td>CPU</td>
      <td>10000.550</td>
      <td>20</td>
      <td>Not Available</td>
      <td>09/18/2021</td>
    </tr>
    <tr>
      <th>4</th>
      <td>CPU</td>
      <td>10000.550</td>
      <td>20</td>
      <td>Not Available</td>
      <td>09/18/2021</td>
    </tr>
  </tbody>
</table>
</div>

This is how you can delete rows with a specific index. 

Next, you'll learn about dropping a range of indices. 

## How to Drop Rows by Index Range in Pandas

You can also drop a list of rows within a specific range. 

A range is a set of values with a lower limit and an upper limit. 

This may be useful in cases where you want to create a sample dataset exlcuding specific ranges of data. 

You can create a range of rows in a dataframe by using the `df.index()` method. Then you can pass this range to the `drop()` method to drop the rows as shown below. 

```python
df.drop(df.index[2:4], inplace=True)

df
```

Here's what this code is doing:

 - `df.index[2:4]` generates a range of rows from 2 to 4. The lower limit of the range is inclusive and the upper limit of the range is exclusive. This means that rows 2 and 3 will be deleted and row 4 will *not* be deleted. 
 - `inplace=True` performs the drop operation in the same dataframe

After dropping rows within the range 2-4, you'll have the below data in the dataframe:

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>product_name</th>
      <th>Unit_Price</th>
      <th>No_Of_Units</th>
      <th>Available_Quantity</th>
      <th>Available_Since_Date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Keyboard</td>
      <td>500.00</td>
      <td>5</td>
      <td>5</td>
      <td>11/5/2021</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Mouse</td>
      <td>200.00</td>
      <td>5</td>
      <td>6</td>
      <td>4/23/2021</td>
    </tr>
    <tr>
      <th>4</th>
      <td>CPU</td>
      <td>10000.55</td>
      <td>20</td>
      <td>Not Available</td>
      <td>09/18/2021</td>
    </tr>
  </tbody>
</table>
</div>

This is how you can drop the list of rows in the dataframe using its range. 

## How to Drop All Rows after an Index in Pandas

You can drop all rows after a specific index by using `iloc[]`. 

You can use `iloc[]` to select rows by using its position index. You can specify the start and end position separated by a `:`. For example, you'd use `2:3` to select rows from 2 to 3. If you want to select all the rows, you can just use `:` in `iloc[]`. 

This may be useful in cases where you want to split the dataset for training and testing purposes. 

Use the below snippet to select rows from 0 to the index 2. This results in dropping the rows after the index 2. 

```python
df = df.iloc[:2]

df
```

In this code, `:2` selects the rows until the index 2. 

This is how you can drop all rows after a specific index. 

After dropping rows after the index 2, you'll have the below data in the dataframe:

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>product_name</th>
      <th>Unit_Price</th>
      <th>No_Of_Units</th>
      <th>Available_Quantity</th>
      <th>Available_Since_Date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Keyboard</td>
      <td>500.0</td>
      <td>5</td>
      <td>5</td>
      <td>11/5/2021</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Mouse</td>
      <td>200.0</td>
      <td>5</td>
      <td>6</td>
      <td>4/23/2021</td>
    </tr>
  </tbody>
</table>
</div>

This is how you can drop rows after a specific index. 

Next, you'll learn how to drop rows with conditions. 

## How to Drop Rows with Multiple Conditions in Pandas

You can drop rows in the dataframe based on specific conditions. 

For example, you can drop rows where the column value is greater than *X* and less than *Y*. 

This may be useful in cases where you want to create a dataset that ignores columns with specific values. 

To drop rows based on certain conditions, select the index of the rows which pass the specific condition and pass that index to the `drop()` method.  

```python
df.drop(df[(df['Unit_Price'] >400) & (df['Unit_Price'] < 600)].index, inplace=True)

df
```

In this code, 

 - `(df['Unit_Price'] >400) & (df['Unit_Price'] < 600)` is the condition to drop the rows. 
 - `df[].index` selects the index of rows which passes the condition. 
 - `inplace=True` performs the drop operation in the same dataframe rather than creating a new one.

After dropping the rows with the condition which has the `unit_price` greater than 400 and less than 600, you'll have the below data in the dataframe:

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>product_name</th>
      <th>Unit_Price</th>
      <th>No_Of_Units</th>
      <th>Available_Quantity</th>
      <th>Available_Since_Date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Mouse</td>
      <td>200.0</td>
      <td>5</td>
      <td>6</td>
      <td>4/23/2021</td>
    </tr>
  </tbody>
</table>
</div>

This is how you can drop rows in the dataframe using certain conditions. 

## Conclusion

To summarize, in this article you've learnt what the `drop()` method is in a Pandas dataframe. You've also seen how dataframe rows and columns are labelled. And finally you've learnt how to drop rows using indices, a range of indices, and based on conditions. 

If you liked this article, feel free to share it. 

### You May Also Like

- [How to Add a Column to a Dataframe in Pandas](https://www.stackvidhya.com/add-column-to-dataframe/)
 - [How to Rename a Column in Pandas](https://www.stackvidhya.com/rename-column-in-pandas/)



