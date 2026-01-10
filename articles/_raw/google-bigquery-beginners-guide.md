---
title: Google BigQuery Beginner's Guide – How to Analyze Large Datasets
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-07-12T11:26:39.000Z'
originalURL: https://freecodecamp.org/news/google-bigquery-beginners-guide
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/web-1.jpg
tags:
- name: bigquery
  slug: bigquery
- name: data analysis
  slug: data-analysis
- name: data analytics
  slug: data-analytics
- name: Google
  slug: google
- name: google cloud
  slug: google-cloud
seo_title: null
seo_desc: 'By Ambreen Khan

  Gone are the days of storing your data in a CSV file or an Excel spreadsheet. If
  you want to quickly analyze millions of data rows in seconds, BigQuery is the way
  to go.

  In this getting started guide, we''ll learn about BigQuery and ho...'
---

By Ambreen Khan

Gone are the days of storing your data in a CSV file or an Excel spreadsheet. If you want to quickly analyze millions of data rows in seconds, BigQuery is the way to go.

In this getting started guide, we'll learn about BigQuery and how we can use it to query and analyze data.

## What is BigQuery?

BigQuery is an enterprise data warehouse that many companies use who need a fully-managed cloud based solution for their massive datasets. 

BigQuery's serverless architecture allows you to quickly execute standard SQL queries and analyze millions of data rows in seconds.  You can then store your data both in Google Cloud Storage in files and buckets or in BigQuery storage. 

BigQuery also has excellent integrations with other GCP products, like Data Flow and Data Studio that makes it a great choice for data analytics tasks.

## Before You Begin: 

We are going to query tables in a public dataset that Google has provided to try out BigQuery using the Google Cloud Platform. Therefore, this guide assumes that:

* You have an access on [Google Cloud Platform](https://cloud.google.com/free/?gclid=CjwKCAjw55-HBhAHEiwARMCsziVtllCq8mRIWlXVVztmn6HkzAlkuajtZeYMInLQmykNGfbEjz2tfRoCFs0QAvD_BwE&gclsrc=aw.ds).
* You have already created a [Google Cloud project](https://cloud.google.com/bigquery/docs/quickstarts/quickstart-web-ui#before-you-begin).
* Google sandbox environment is up and running. 

## How to Access a Public Dataset

A public dataset is available to the general public through the [Google Cloud Public Dataset Program](https://cloud.google.com/public-datasets). We'll use a Hacker News dataset that contains all stories and comments from Hacker News from its launch in 2006 to present. Let's get started.

Navigate to [Hacker News dataset](https://console.cloud.google.com/marketplace/product/y-combinator/hacker-news) and click the VIEW DATASET button. It will take you to the Google Cloud Platform login screen. Login to the account and it will open the BigQuery Editor window with the dataset. 

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-51.png)

## How the BigQuery Interface Is Organized

BigQuery is structured as a hierarchy with 4 levels:

* Projects: Top-level containers that store the data
* Datasets: Within projects, datasets allow you to organize your data and hold one or more tables of data
* Tables: Within datasets, tables hold actual data.
* Jobs: task performed on data such as running queries, loading data, and exporting data.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-53.png)

**Note:** Please note that while working with tables, you'll also notice that:

* Tables are broken out by day meaning that you will need to use a wildcard, or * to pull a larger date range.
* There is also an “intraday” table that will give you data for the last 24 hours.

## How to Check the Table Schema

Click on the table name. This will allow you to see what columns are in the table, as well as some buttons to perform various operations on the table.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-55.png)

## How to Preview the Data

Use the preview button to get a sample of some rows in the table. [Don’t do a `SELECT *` in BigQuery](https://cloud.google.com/bigquery/docs/best-practices-costs#avoid_select_):

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-56.png)

## How to Query Big Data

SQL statements are used to perform various database tasks, such as querying data, creating tables, and updating databases.

### Basic Queries

Basic queries contain the following components:

* `SELECT` (required): identifies the columns to be included in the query
* `FROM` (required): the table that contains the columns in the SELECT statement
* `WHERE`: a condition for filtering records
* `ORDER BY`: Used to sort the result-set in ascending or descending order.
* `GROUP BY`: how to aggregate data in the result set

## How to Compose a Query in BigQuery

For our first query, let’s find out what are the top 5 domains shared in Hacker News in year 2021 so far (query executed on July 9th 2021).

Click the **Compose New query** button. It will open the editor tab.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-41.png)

Write your first query as below:

```sql
SELECT REGEXP_EXTRACT(url, '//([^/]*)/?') domain, COUNT(*) total
FROM `bigquery-public-data.hacker_news.full`
WHERE url!='' AND EXTRACT(YEAR FROM timestamp)=2021
GROUP BY domain ORDER BY total DESC LIMIT 5
```

You'll notice that BigQuery debugs your code as you construct it. If the query is valid, then a check mark appears along with the amount of data that the query will process. This helps you determine the cost of running the query. 

If the query is invalid, then an exclamation point appears along with an error message.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-59.png)

To run this query, click on the Run button. In a few seconds, you should see results returned from the query:

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-60.png)

You can click on the **JSON** tab if you want the results in JSON format. You'll also find interesting details under the 'Execution details' column.

## **How to Query Multiple Tables Using a Wildcard Table**

Wildcard tables enable you to query multiple tables using concise SQL statements. A wildcard table represents a union of all the tables that match the wildcard expression:

`FROM `tablename.stories_*`` 

### _TABLE_SUFFIX Pseudo Column

Queries with wildcard tables support the `_TABLE_SUFFIX` pseudo column in the `WHERE` clause. To restrict a query so that it scans only a specified set of tables, use the `_TABLE_SUFFIX` pseudo column in a `WHERE` clause with a condition that is a constant expression.

Using `_TABLE_SUFFIX` can greatly reduce the number of bytes scanned, which helps reduce the cost of running your queries.

### How to Get Data by Providing a Date Range

```
WHERE _TABLE_SUFFIX BETWEEN
    FORMAT_DATE(‘%Y%m%d’,DATE_SUB(CURRENT_DATE(), INTERVAL 36 MONTH))
    AND
    FORMAT_DATE(‘%Y%m%d’,DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY))

```

### How to Use UNNEST to Flatten the Date

To convert an `ARRAY` into a set of rows, also known as "flattening," use the [`UNNEST`](https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#unnest_operator) operator. `UNNEST` takes an `ARRAY` and returns a table with a single row for each element in the `ARRAY`:

```
SELECT * FROM UNNEST (['Ambreen', 'Abdul', 'Adam', 'David']) AS names;

```

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-45.png)

## How to Save and Share Queries

You can save your queries for later use. There are 3 types of saved queries:

* **Private:** Private saved queries are visible only to the user who creates them.
* **Project-level:** Project-level saved queries are visible to members of the predefined BigQuery IAM roles with the required [permissions](https://cloud.google.com/bigquery/docs/saving-sharing-queries#permissions).
* **Public:** Public saved queries are visible to anyone with a link to the query.

## Summary

BigQuery is much more sophisticated than what we explored in this simple tutorial. You can also export Firebase Analytics data to BigQuery, which will let you run sophisticated ad hoc queries against your analytics data. 

And with BigQuery ML, you can create and execute machine learning models using standard SQL queries. 

If you’re feeling excited and want to learn more about BigQuery, check out the links below.

## Resources:

* [BigQuery cookbook](https://support.google.com/analytics/answer/4419694?hl=en#zippy=%2Cin-this-article) 
* [Filtering selected tables using _TABLE_SUFFIX](https://cloud.google.com/bigquery/docs/querying-wildcard-tables#filtering_selected_tables_using_table_suffix) 
* [BigQuery Tip: The UNNEST Function](https://firebase.googleblog.com/2017/03/bigquery-tip-unnest-function.html)
* [BigQuery UNNEST: How to work with nested data in BigQuery](https://towardsdatascience.com/bigquery-unnest-how-to-work-with-nested-data-in-bigquery-f27006a64c3)

