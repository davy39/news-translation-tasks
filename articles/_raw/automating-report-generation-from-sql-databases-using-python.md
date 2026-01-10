---
title: How to Generate Automated Reports from a SQL Database Using Python
subtitle: ''
author: Jeremiah Oluseye
co_authors: []
series: null
date: '2023-03-16T22:09:47.000Z'
originalURL: https://freecodecamp.org/news/automating-report-generation-from-sql-databases-using-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/coreet.JPG
tags:
- name: automation
  slug: automation
- name: database
  slug: database
- name: Python
  slug: python
- name: SQL
  slug: sql
seo_title: null
seo_desc: 'Generating reports from SQL databases is a common task in many organizations.
  But the process can be time-consuming and error-prone, especially if it involves
  manual data extraction, transformation, and formatting.

  In this article, we will explore ho...'
---

Generating reports from SQL databases is a common task in many organizations. But the process can be time-consuming and error-prone, especially if it involves manual data extraction, transformation, and formatting.

In this article, we will explore how to use Python to automate the process of generating reports from SQL databases, reducing the time and effort required to create and distribute reports.

### Prerequisites

Before we begin, make sure you have the following installed:

* Python 3.x
    
* A SQL database such as MySQL or PostgreSQL
    
* A Python library for accessing SQL databases such as psycopg2 or mysql-connector-python
    
* A Python library for creating reports such as ReportLab or PyPDF2
    

## How to Connect to the SQL Database

The first step is to connect to the SQL database using Python. We will use the psycopg2 library to connect to a PostgreSQL database.

Here is an example code snippet for connecting to the database:

```python
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="mydatabase",
    user="myusername",
    password="mypassword"
)
```

Make sure to replace the values in the `host`, `database`, `user`, and `password` parameters with the appropriate values for your database.

## How to Retreive Data from the SQL Database

Once we have established a connection to the SQL database, we can execute SQL queries to retrieve the data we need for our report.

Here is an example code snippet for retrieving data from a PostgreSQL database:

```python
cur = conn.cursor()

cur.execute("SELECT name, email, phone FROM customers")

rows = cur.fetchall()
```

This code retrieves the name, email, and phone number of all customers in the `customers` table.

## How to Create the Report

Next, we need to create the report using a Python library such as ReportLab or PyPDF2. Here is an example code snippet for creating a PDF report using ReportLab:

```python
from reportlab.pdfgen import canvas

# Create a new PDF document
pdf = canvas.Canvas("report.pdf")

# Write the report title
pdf.setFont("Helvetica-Bold", 16)
pdf.drawString(50, 750, "Customer Report")

# Write the report content
pdf.setFont("Helvetica", 12)
y = 700
for row in rows:
    pdf.drawString(50, y, "Name: " + row[0])
    pdf.drawString(50, y - 20, "Email: " + row[1])
    pdf.drawString(50, y - 40, "Phone: " + row[2])
    y -= 60

# Save the PDF document
pdf.save()
```

This code creates a new PDF document, writes the report title, and loops through the data retrieved from the SQL database to write the report content. The final PDF report is saved as `report.pdf`.

## How to Automate the Report Generation Process

Now that we have the code to connect to the SQL database, retrieve the data, and create the report, we can automate the report generation process using a Python script.

Here is an example code snippet for automating the report generation process:

```python
import psycopg2
from reportlab.pdfgen import canvas

# Connect to the SQL database
conn = psycopg2.connect(
    host="localhost",
    database="mydatabase",
    user="myusername",
    password="mypassword"
)

# Retrieve the data from the SQL database
cur = conn.cursor()
cur.execute("SELECT name, email, phone FROM customers")
rows = cur.fetchall()

# Create the report
pdf = canvas.Canvas("report.pdf")
pdf.setFont("Helvetica-Bold", 16)
pdf.drawString(50, 750, "Customer Report")
pdf.setFont("Helvetica", 12)
y = 700
for row in rows:
pdf.drawString(50, y, "Name: " + row[0])
pdf.drawString(50, y - 20, "Email: " + row[1])
pdf.drawString(50, y - 40, "Phone: " + row[2])
y -= 60
pdf.save()
#close the database connection
cur.close()
conn.close()
```

This code connects to the SQL database, retrieves the data, creates the report, and saves it as `report.pdf`. You can then run this script on a regular basis to generate reports automatically.

## Conclusion

In this article, we have explored how to use Python to automate the process of generating reports from SQL databases. By using Python to connect to the database, retrieve the data, and create the report, we can save time and reduce the risk of errors.

We have also seen how to use Python libraries such as psycopg2 and ReportLab to make the process even more efficient. With these techniques, you can easily automate report generation from SQL databases and focus on other important tasks.

Let’s connect on [Twitter](https://twitter.com/Olujerry19) and [LinkedIn](https://www.linkedin.com/in/jeremiah-oluseye-58457719a/).
