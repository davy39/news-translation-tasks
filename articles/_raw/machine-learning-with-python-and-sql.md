---
title: How to Perform Machine Learning Tasks with Python and SQL
subtitle: ''
author: Jeremiah Oluseye
co_authors: []
series: null
date: '2023-03-09T17:57:45.000Z'
originalURL: https://freecodecamp.org/news/machine-learning-with-python-and-sql
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/just.JPG
tags:
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
seo_title: null
seo_desc: 'Machine learning has become a popular field in recent years, with various
  applications in data analysis, computer vision, natural language processing, and
  more.

  Python is one of the most widely used programming languages for machine learning,
  thanks ...'
---

Machine learning has become a popular field in recent years, with various applications in data analysis, computer vision, natural language processing, and more.

Python is one of the most widely used programming languages for machine learning, thanks to its rich ecosystem of libraries, frameworks, and tools.

But to build a machine learning system, you need to have access to data. Most data is stored in databases, particularly SQL databases, which are used by businesses and organizations to store and manage data.

In this article, we will explore how to perform machine learning with Python and SQL.

## How to Connect to a SQL Database with Python

To perform machine learning with data stored in a SQL database, the first step is to connect to the database using Python.

We will use the PyMySQL library, which is a pure Python MySQL client library that allows you to connect to a MySQL database server and perform SQL queries.

Here is an example of how to connect to a MySQL database using PyMySQL:

```python
import pymysql

# Connect to the database
connection = pymysql.connect(
    host='localhost',
    user='username',
    password='password',
    database='database_name'
)

# Create a cursor object
cursor = connection.cursor()

# Execute an SQL query
query = "SELECT * FROM table_name"
cursor.execute(query)

# Fetch the result
result = cursor.fetchall()

# Close the cursor and connection
cursor.close()
connection.close()
```

This code connects to a MySQL database running on the localhost and selects all the rows from a table named `table_name`. The result is then fetched and stored in the result variable.

## How to Use Python for Machine Learning with SQL Data

Once we have connected to the SQL database, we can use Python libraries like Pandas to read the data into a Pandas DataFrame.

A data frame is a two-dimensional labeled data structure with columns of potentially different types. It is like a spreadsheet or SQL table.

Here is an example of how to use Pandas to read data from a SQL database:

```python
import pandas as pd
import pymysql

# Connect to the database
connection = pymysql.connect(
    host='localhost',
    user='username',
    password='password',
    database='database_name'
)

# Read data into a Pandas DataFrame
df = pd.read_sql('SELECT * FROM table_name', con=connection)

# Close the connection
connection.close()
```

This code uses Pandas to read all the data from the `table_name` table in the `database_name` database and stores it in a Pandas DataFrame named df. We then close the database connection.

With the data in a Pandas DataFrame, we can use Python libraries like Scikit-learn to perform various machine learning tasks.

Scikit-learn is a popular machine-learning library that provides different algorithms for classification, regression, clustering, and more.

Here is an example of how to use Scikit-learn to perform logistic regression on the data:

```python
import pandas as pd
import pymysql
from sklearn.linear_model import LogisticRegression

# Connect to the database
connection = pymysql.connect(
    host='localhost',
    user='username',
    password='password',
    database='database_name'
)

# Read data into a Pandas DataFrame
df = pd.read_sql('SELECT * FROM table_name', con=connection)

# Prepare the data
X = df[['feature_1', 'feature_2']]
y = df['target']

# Create a logistic regression model
model = LogisticRegression()

# Train the model
model.fit(X, y)

# Close the connection
connection.close()
```

This code uses Pandas to read the data from the `table_name` table in the `database_name` database and stores it in a Pandas DataFrame named df.

We then prepare the data by selecting two features (`feature_1` and `feature_2`) and the target variable (y) from the data frame.

Finally, we create a logistic regression model using Scikit-learn's `LogisticRegression` class and train the model using the `fit()` method.

We can also use Scikit-learn to split the data into training and testing sets, as well as to evaluate the performance of the model. Here is an example of how to split the data and evaluate the model:

```python
import pandas as pd
import pymysql
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Connect to the database
connection = pymysql.connect(
    host='localhost',
    user='username',
    password='password',
    database='database_name'
)

# Read data into a Pandas DataFrame
df = pd.read_sql('SELECT * FROM table_name', con=connection)

# Prepare the data
X = df[['feature_1', 'feature_2']]
y = df['target']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create a logistic regression model
model = LogisticRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

# Close the connection
connection.close()
```

This code uses Scikit-learn's `train_test_split()` method to split the data into training and testing sets.

We then create a logistic regression model, train it using the `fit()` method on the training data, make predictions on the test set using the `predict()` method, and evaluate the performance of the model using the `accuracy_score()` method.

## Conclusion

In this article, we explored how to perform machine learning with Python and SQL.

We first connected to a SQL database using PyMySQL, then used Pandas to read data into a Pandas DataFrame. We then used Scikit-learn to perform logistic regression on the data, as well as to split the data into training and testing sets and evaluate the performance of the model.

With these tools, you can perform powerful machine-learning tasks on data stored in SQL databases.

Let’s connect on [Twitter](https://twitter.com/Olujerry19) and [LinkedIn](https://www.linkedin.com/in/jeremiah-oluseye-58457719a/).
