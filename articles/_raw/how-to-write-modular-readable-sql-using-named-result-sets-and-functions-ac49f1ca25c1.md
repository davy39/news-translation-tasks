---
title: How to write modular, readable SQL using named result sets and functions
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-07T17:47:59.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-modular-readable-sql-using-named-result-sets-and-functions-ac49f1ca25c1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*L6REAogd_Yiz1q5vcHuKSA.jpeg
tags:
- name: best practices
  slug: best-practices
- name: data analytics
  slug: data-analytics
- name: Data Science
  slug: data-science
- name: SQL
  slug: sql
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Lak Lakshmanan

  My professional journey in computers has involved C++, then Java, and now Python.
  SQL remains, at best, a foreign language. For my own sanity, therefore, I’ve brought
  some of my programming best practices to SQL. In particular, the ...'
---

By Lak Lakshmanan

My professional journey in computers has involved C++, then Java, and now Python. SQL remains, at best, a foreign language. For my own sanity, therefore, I’ve brought some of my programming best practices to SQL. In particular, the WITH statement has been my friend.

![Image](https://cdn-media-1.freecodecamp.org/images/NNhuWHnTuY2hkZmbrzZY1qw1PoqpsDazq--W)
_If you write modular, readable SQL, you will have time for long bike rides on the weekend_

I’ll use a [public dataset of London bikeshares](https://bigquery.cloud.google.com/table/bigquery-public-data:london_bicycles.cycle_hire) in Google BigQuery to demonstrate. Let’s say we want to find whether bikes get rented for longer durations on weekends.

#### 1. Constants, not hardcoded numbers

A good first step is to define constants we will use throughout my query (See [full query](https://bigquery.cloud.google.com/savedquery/663413318684:9b1a705e68b046cd9b44259f6198a215)):

```
#standardsqlWITH constants AS (  SELECT  600 AS SHORT_DUR,         1800 AS LONG_DUR,         ['Sun', 'Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat'] AS daysofweek),
```

Here, I’m defining rides of less than 10 minutes as “short” and rides of over 30 minutes as “long.” Notice how, by defining these constants up-front, I can make it quite easy to try out different numbers. The use of named constants will also make the query a lot more readable.

#### 2. Named result sets

Another thing you want to do to increase readability is to decompose the query into named result sets. Instead of writing queries and subqueries and counting parantheses, I tend to use WITH statements a lot. Like functions in languages like C++ or Python, named result sets allow for both reuse and logical separation.

I first define a query to pull out the fields I want, and name this result set as bikeshare ([full query](https://bigquery.cloud.google.com/savedquery/663413318684:9b1a705e68b046cd9b44259f6198a215)):

```
bikeshare AS (  SELECT    IF(duration < SHORT_DUR, 1, 0) AS short_ride,    IF(duration > LONG_DUR,  1, 0) AS long_ride,    daysofweek[ORDINAL(EXTRACT(DAYOFWEEK FROM start_date))] AS dayofweek  FROM `bigquery-public-data.london_bicycles.cycle_hire`, constants)
```

Notice that the FROM clause has to include the “constants” in order to use the defined constants.

#### 3. SQL functions

You can decompose complex queries using the WITH keyword and create named result sets. But what about complex parsing? In the snippet above, the line pulling the day of the week and indexing into the **daysofweek** array is not readable, is it? And it is quite likely that this is something that you’d want in another place.

Use a SQL function so that you can reuse this expression:

```
CREATE TEMPORARY FUNCTION dayOfWeek(ts TIMESTAMP,                                     days ARRAY<STRING>) AS(  days[ORDINAL(EXTRACT(DAYOFWEEK FROM ts))]);
```

I’m defining a function **dayOfWeek** that, given a timestamp and array of day names, will return the day of the week that the time in the timestamp corresponds to. Once we have this function defined, the named result set in the previous section becomes cleaner ([full query](https://bigquery.cloud.google.com/savedquery/663413318684:9b1a705e68b046cd9b44259f6198a215)):

```
bikeshare AS (  SELECT    IF(duration < SHORT_DUR, 1, 0) AS short_ride,    IF(duration > LONG_DUR,  1, 0) AS long_ride,    dayOfWeek(start_date, daysofweek) AS dayofweek  FROM `bigquery-public-data.london_bicycles.cycle_hire`, constants)
```

#### Simplicity itself

Once we have named constants and named result sets, the final query is simplicity itself:

```
SELECT   dayofweek,  SUM(short_ride)/COUNT(short_ride) AS frac_short_rides,  SUM(long_ride)/COUNT(long_ride)  AS frac_long_rides,  COUNT(short_ride) AS num_all_ridesFROM  bikeshareGROUP BY  dayofweekORDER BY frac_long_rides DESC
```

Here’s the [full query](https://bigquery.cloud.google.com/savedquery/663413318684:9b1a705e68b046cd9b44259f6198a215), and the ensuing result:

![Image](https://cdn-media-1.freecodecamp.org/images/3IL2XIQaZ4oQV485yTgWj6QSgupIYfXsNXzT)

Weekdays are for quick, short commutes and weekends are for long, slow rides. Makes perfect sense!

