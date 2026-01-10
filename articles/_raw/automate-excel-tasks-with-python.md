---
title: How to Automate Excel Tasks with Python
subtitle: ''
author: Jeremiah Oluseye
co_authors: []
series: null
date: '2023-03-01T19:04:17.000Z'
originalURL: https://freecodecamp.org/news/automate-excel-tasks-with-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/FreecodeCamp.png
tags:
- name: automation
  slug: automation
- name: excel
  slug: excel
- name: Python
  slug: python
seo_title: null
seo_desc: 'Excel is a surprisingly common tool for data analysis.

  Data analysts can readily modify, examine, and display huge amounts of data with
  Excel, which makes it simpler to gain insights and make wise choices.

  Excel''s versatility lets users carry out a v...'
---

Excel is a surprisingly common tool for data analysis.

Data analysts can readily modify, examine, and display huge amounts of data with Excel, which makes it simpler to gain insights and make wise choices.

Excel's versatility lets users carry out a variety of data analysis activities, from straightforward math operations to intricate statistical analysis. Also, Excel offers automation through the use of third-party programs like Python or the built-in programming language VBA.

Excel is frequently used for data analysis across a range of industries, including banking, healthcare, and marketing, thanks to its versatility and usability.

But as a data analyst, you might often find yourself repeating mundane tasks on a daily basis when working with Excel.

These tasks may include copying and pasting data, formatting cells, and creating charts, among others. Over time, this can become monotonous and time-consuming, leaving you with less time to focus on more important aspects of data analysis, such as identifying trends, outliers, and insights.

This is why automating Excel using Python can be a game-changer, helping you streamline your workflows and free up time for more meaningful analysis.

In this tutorial, I'll show you some helpful ways to create, update, and analyze Excel spreadsheets using Python programming. Let's dive in.

## How to Merge Two Separate Spreadsheets with Python

Data analysts often have to work on many spreadsheets, which can become hectic when you have to merge those files together.

The code below helps you merge two separate files together.

```python
import pandas as pd

# Read in the two Excel files

file1 = pd.read_excel('file1.xlsx')file2 = pd.read_excel('file2.xlsx')

# Merge the two files using the concat() method
merged_file = pd.concat([file1, file2], ignore_index=True)

# Write the merged file to a new Excel file
merged_file.to_excel('merged_file.xlsx', index=False)
```

In this code, we first import the Pandas library, which we'll use to read in and manipulate the Excel files.

We then use the `read_excel()` method to read in both `file1.xlsx` and `file2.xlsx`. Next, we use the `concat()` method to merge the two files together. The `ignore_index=True` argument ensures that the index values from both files are reset, so we don't end up with duplicate index values in the merged file.

Finally, we use the `to_excel()` method to write the merged file to a new Excel file named `merged_file.xlsx`. We also set `index=False` to ensure that the index column is not included in the output file.

## How to Import and Export Data with Python

This task involves using Python libraries such as Pandas to read Excel files into a DataFrame object. You can then manipulate it and analyze it using Python.

You can also export data from Python back into an Excel file using the same libraries.

```python
import pandas as pd
# Import Excel file

df = pd.read_excel('filename.xlsx', sheet_name='Sheet1')

# Export to Excel file
df.to_excel('new_filename.xlsx', index=False)
```

The given code imports the Pandas library and reads an Excel file named "filename.xlsx" from Sheet1 of the workbook, storing the data in a Pandas dataframe named "df". The dataframe is then exported to a new Excel file named "new\_filename.xlsx" using the "to\_excel" method. The "index=False" parameter is used to exclude row indexing in the output file.

Essentially, the code copies the contents of the original Excel file to a new file using Pandas.

## How to Clean and Transform Data using Python

This task involves using Python libraries such as Pandas to clean and transform data in Excel.

This may include removing duplicates, filtering data based on specific criteria, and performing calculations on the data.

```python
import pandas as pd

# Remove duplicates
df = df.drop_duplicates()

# Filter data
df = df[df['column_name'] > 10]

# Perform calculations
df['new_column'] = df['column1'] + df['column2']
```

The code snippet above performs data cleaning and manipulation tasks on a Pandas dataframe named 'df' using the Pandas library.

Firstly, it removes duplicate rows from 'df' using the "drop\_duplicates" method. Secondly, it filters the 'df' dataframe by selecting rows where the value in the 'column\_name' column is greater than 10 and assigns the filtered result to a new dataframe called 'data\_df'.

Lastly, a new column named 'new\_column' is added to 'df' which contains the sum of values from 'column1' and 'column2'.

Overall, the code effectively cleans and manipulates the data by removing duplicates, filtering specific rows, and adding a new calculated column to the original dataframe.

## How to Perform Data Analysis with Python

This task involves using Python libraries such as Pandas and NumPy to perform data analysis on Excel data.

This may include calculating summary statistics, such as mean and standard deviation, or creating custom reports by grouping data based on specific criteria.

```python
import pandas as pd
import numpy as np

# Calculate summary statistics
df.describe()
# Create custom reports
df.pivot_table(values='column_name', index='category_name', columns='date')
```

The code utilizes the Pandas and NumPy libraries and performs data analysis and reporting tasks on a Pandas dataframe named "df".

Firstly, it calculates summary statistics for the numerical data in the dataframe using the "describe" method. This method generates valuable insights on the data's distribution, central tendency, and dispersion.

Secondly, the code uses the "pivot\_table" method to create customized reports from the dataframe. This method summarizes and aggregates the data in the dataframe and can produce tables in various formats.

In this code, it generates a new dataframe where the 'column\_name' values are grouped by the 'category\_name' and 'date' columns.

Overall, the code performs statistical analysis and reporting tasks on the dataframe to gain insights from the data.

## How to Create Charts with Python

This task involves using Python libraries such as matplotlib or seaborn to create charts and graphs from Excel data.

You can customize these charts to display specific data and format them to meet specific requirements.

```python
import pandas as pd
import matplotlib.pyplot as plt
# Create a bar chart
df.plot(kind='bar', x='category_name', y='sales')
plt.show()
# Create a scatter plot
df.plot(kind='scatter', x='column1', y='column2')plt.show()
```

The code imports two libraries, Pandas and matplotlib.pyplot using the aliases 'pd' and 'plt', respectively.

The Pandas "plot" method is then used to create two types of plots. The first type of plot is a bar chart that shows the relationship between the 'category\_name' and 'sales' columns in the "df" dataframe.

The second type of plot is a scatter plot that shows the relationship between the 'column1' and 'column2' columns in the same dataframe. The code uses the parameters "kind='bar'" for the bar chart and "kind='scatter'" for the scatter plot to create the respective plots.

Lastly, the "show" method is called to display the plots on the screen. In summary, the code utilizes Pandas and matplotlib to create a bar chart and a scatter plot to visualize the data in the "df" dataframe.

## How to Do Data Visualization in Python

This task involves using Python libraries such as Plotly and bokeh to create interactive data visualizations from Excel data.

These visualizations allow users to explore data in new ways, such as by zooming in on specific data points or filtering data based on specific criteria.

```python
import pandas as pd
import plotly.express as px
# Create a heatmap
fig = px.imshow(df.corr())
fig.show()
# Create a line chart
fig = px.line(df, x='date', y='sales', color='category')
fig.show()
```

The code uses the Pandas and plotly.express libraries to create two types of visualizations. First, a heatmap plot is created using plotly.express's "imshow" method that visualizes the correlation between columns in the "df" dataframe.

Second, a line chart is created using plotly.express's "line" method that displays the relationship between the 'date' and 'sales' columns while differentiating between categories based on the 'category' column of the dataframe. Both plots are displayed using the "show" method.

## How to Automate Report Generation with Python

This task involves using Python scripts to automate the process of generating reports from Excel data.

You can set up these scripts to run on a regular schedule, such as daily or weekly. They can also automatically update as new data becomes available.

```python
import pandas as pd
# Create daily report
df_daily = df[df['date'] == '2022-01-01']
df_daily.to_excel('daily_report.xlsx', index=False)
# Create weekly report
df_weekly = df.groupby('category').sum()
df_weekly.to_excel('weekly_report.xlsx', index=False)
```

The code creates a daily report by creating a new dataframe "df\_daily" that includes only the rows where the 'date' column equals '2022-01-01'. This is achieved by using Pandas' boolean indexing feature.

Afterward, the "to\_excel" method is used to export the filtered data to an Excel file named "daily\_report.xlsx", without including the index column.

Next, the code creates a weekly report by grouping the "df" dataframe by the 'category' column and summing the values of all other columns. This is accomplished using the Pandas "groupby" and "sum" methods.

The result is saved in a new dataframe named "df\_weekly". Lastly, the "to\_excel" method is used to export the aggregated data to an Excel file named "weekly\_report.xlsx", without including the index column.

In summary, the code creates two reports using the Pandas library. The first report is a daily report that includes only data from a specific date, and the second report is a weekly report that aggregates data by category. Both reports are exported to Excel files using the "to\_excel" method.

## How to Automate Repetitive Tasks with Macros and Scripts in Python

This task involves using Python to automate repetitive tasks in Excel, such as data entry or formatting. You can do this by creating macros or scripts that can execute automatically, or by using Python to interact with the Excel application directly.

```python
import win32com.client as win32
# Open Excel file
excel = win32.gencache.EnsureDispatch('Excel.Application')
workbook = excel.Workbooks.Open(r'filename.xlsx')
# Run macro
excel.Application.Run('macro_name')
# Save and close Excel
 fileworkbook.Save()workbook.Close()excel.Quit()
```

The code uses the win32com.client module to interact with Microsoft Excel via the Windows API.

First, an instance of the Excel application is opened using the `EnsureDispatch()` method, and the specified Excel file is opened using the `Workbooks.Open()` method.

Next, a macro is executed using the `Application.Run()` method, passing the name of the macro as an argument.

Finally, the changes made to the Excel file are saved using the `Save()` method, the workbook is closed using the `Close()` method, and the Excel application is terminated using the `Quit()` method

## How to Scrape Data with Python

This task involves using Python libraries such as requests and Beautiful Soup to scrape data from web pages or other sources and import it into Excel.

You can then analyze and manipulate this data using Python libraries such as Pandas.

```python
import pandas as pd
import requests
from bs4 import BeautifulSoup
# Scrape data from web page
url = 'https://www.website.com/data'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table')
df = pd.read_html(str(table))[0]
# Export to Excel file
df.to_excel('scraped_data.xlsx', index=False)
```

This code uses the requests library to send an HTTP GET request to the URL '[https://www.example.com](https://www.example.com/)'. It then uses the BeautifulSoup library to parse the HTML content of the response into a BeautifulSoup object named 'soup'.

You can then use BeautifulSoup methods such as `find_all()` to extract specific data from the HTML:

`links = []for link in soup.find_all('a'): href = link.get('href') links.append(href)`

This code finds all the anchor tags in the HTML and extracts the value of the 'href' attribute for each one, adding them to a list named 'links'.

## How to Use Python to Integrate Excel with Other Applications

This task involves using Python to integrate Excel with other applications, such as databases or web services.

You can do this using Python libraries such as pyodbc to connect to databases or by using APIs to connect to web services. This allows for seamless data transfer and analysis between different applications.

```python
import pandas as pd
import pyodbc
# Connect to database
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=server_name;DATABASE=db_name;UID=user_id;PWD=password')
# Read data from database
query = 'SELECT * FROM table_name'
df = pd.read_sql(query, cnxn)
# Export to Excel file
df.to_excel('database_data.xlsx', index=False)
```

The code establishes a connection to a SQL Server database using `pyodbc.connect()` method, where the driver, server name, database name, user ID, and password are provided as arguments.

Then, a SQL query is defined and executed to retrieve data from a table in the database using the `pd.read_sql()` method, where the SQL query and the connection object are provided as arguments. The retrieved data is then stored in a pandas DataFrame.

Finally, the data in the DataFrame is exported to an Excel file named "database\_data.xlsx" using the `to_excel()` method, with the index column excluded from the export by setting the index parameter to False.

## Conclusion

Python is a versatile language that you can use to automate many Excel tasks. You can also use various libraries such as Pandas, openpyxl, xlwings, and pyautogui to manipulate data, extract information, generate reports, and automate repetitive tasks.

Automation can save time and effort, reduce errors, and boost productivity. Python proficiency can be a valuable skill for any professional working with Excel, whether you're a data or financial analyst. By learning Python, you can elevate your work to new heights.

Let’s connect on [Twitter](https://twitter.com/Olujerry19) and [LinkedIn](https://www.linkedin.com/in/jeremiah-oluseye-58457719a/). Thanks for reading!
