---
title: SQL Left Join – Example Join Statement Syntax
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2021-08-26T20:29:12.000Z'
originalURL: https://freecodecamp.org/news/sql-left-join-example-join-statement-syntax
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/pexels-pixabay-262347.jpg
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: null
seo_desc: In a Relational Database, tables are often related to each other in a way
  that allows their information to only be written once in the whole database. Then,
  when you need to analyze the data, you'll need to combine the info from those related
  tables....
---

In a Relational Database, tables are often related to each other in a way that allows their information to only be written once in the whole database. Then, when you need to analyze the data, you'll need to combine the info from those related tables.

To do this in SQL, you can use `JOIN` statements. The `LEFT JOIN` statement is one of [the various `JOIN` statements available](https://www.freecodecamp.org/news/sql-join-types-inner-join-vs-outer-join-example/). When you use it to join two tables, it keeps all the rows of the first table (the left table), even if there is not a corresponding match on the second table.

You can use `JOIN` in a `SELECT` query to join two tables, `table_1` and `table_2`, like this:

```sql
SELECT columns
FROM table_1
LEFT OUTER JOIN table_2
ON relation;
```

```sql
SELECT columns
FROM table_1
LEFT JOIN table_2
ON relation;
```

First you write which columns will be present in the joined table. You can specify to which table the column belongs by prefixing the table name to the column name. This is necessary if some columns have the same name (like `table_1.column_1` and `table_2.column_1`) with `SELECT <columns>`.

Then you would write the name of the first table as `FROM table_1`.

After that you'd write the name of the second table as `LEFT OUTER JOIN table_2` or `LEFT JOIN table_2` (omitting the `OUTER` keyword).

And at the end you'd write the relation to use to match the rows, for example `ON table_1.column_A = table_2.column_B`. Often the relation is by id, but it can be with any column.

# SQL LEFT JOIN Example

Let's say you have a book database in which you have two tables, one with books, the other with authors. To avoid repeating all the author info for each book, that info is in its own table, and the books have only the `author_name` column.


| book_id | title | author_name | publ_year |
| --- | --- | --- | --- |
| 1 | Uno, nessuno e centomila | Luigi Pirandello | 1926 |
| 2 | Il visconte dimezzato | Italo Calvino | 1952 |
| 3 | Le tigri di Mompracem | Emilio Salgari | 1900 |
| 4 | Il giorno della civetta | Leonardo Sciascia | 1961 |
| 5 | A ciascuno il suo | Leonardo Sciascia | 1966 |
| 6 | Il fu Mattia Pascial | Luigi Pirandello | 1904 |
| 7 | I Malavoglia | Giovanni Verga | 1881 |

| author_id | name | year_of_birth | place_of_birth | trivia |
| --- | --- | --- | --- | --- |
| 1 | Luigi Pirandello | 1867 | Agrigento | Nobel Prize in Literature in 1934 |
| 2 | Giovanni Verga | 1840 | Vizzini | was Senator of the Kingdom of Italy from 1920 to 1922 |
| 3 | Italo Svevo | 1861 | Trieste | real name was Aron Hector Schmitz |
| 4 | Cesare Pavese | 1908 | Santo Stefano Belbo | NULL |
| 5 | Giuseppe Tomasi di Lampedusa | 1896 | Palermo | was prince of Lampedusa from 1934 to 1957 |

We can join these two tables based on the names of the authors. Using the `books` table as the left table, you can write the following code to join them:

```sql
SELECT books.title AS book_title, books.publ_year, books.author_name, authors.year_of_birth, authors.place_of_birth
   FROM books
   LEFT JOIN authors
   ON books.author_name = authors.name
;
```

Let's break it down.

In the first line, you choose which columns to show in the final table. It's also the place to decide if some columns will have a different name in the resulting table using `AS` like with `books.title AS book_title`.

The second line, `FROM books`, says which is the first table to consider, also called the left table.

Then the third line, `LEFT JOIN authors`, says which other table to consider.

`ON books.author_name = authors.name` says to match the tables using the rows `books.author_name` and `authors.name`.

After this query you would get the table as below, where the rows that didn't get info from the authors table just show `NULL`.

| book_title | publ_year | author_name | year_of_birth | place_of_birth |
| --- | --- | --- | --- | --- |
| Uno, nessuno e centomila | 1926 | Luigi Pirandello | 1867 | Agrigento |
| Il visconte dimezzato | 1952 | Italo Calvino | NULL | NULL |
| Le tigri di Mompracem | 1900 | Emilio Salgari | NULL | NULL |
| Il giorno della civetta | 1961 | Leonardo Sciascia | NULL | NULL |
| A ciascuno il suo | 1966 | Leonardo Sciascia | NULL | NULL |
| Il fu Mattia Pascal | 1904 | Luigi Pirandello | 1867 | Agrigento |
| I Malavoglia | 1881 | Giovanni Verga | 1840 | Vizzini |

Note that the authors not present in the `books` table are not in this joined table. This is because, as I said before, only the unrelated rows from the left table (in this case `books`) are kept, not those from the right/second table.

## A more complex LEFT JOIN example

Let's see another way you can use `JOIN` together with other SQL features to do some data analysis.

You might want to see how many books from each author are present in the database. You could use the below query to do so:

```sql
SELECT authors.name AS author_name,
    SUM(
      CASE
        WHEN books.title LIKE '%'
          THEN 1
        ELSE 0
      END
    ) as number_of_books
  FROM authors
  LEFT JOIN books
  ON books.author_name = authors.name
  GROUP BY authors.name
  ORDER BY number_of_books DESC
;

```

#### Code breakdown

Line 1: with `SELECT` you list the columns you want in the resulting table.

Line 2: [`SUM` is an aggregation function](https://www.freecodecamp.org/news/sql-group-by-clauses-explained/#aggregations-count-sum-avg-) used in conjunction with GROUP BY. The values of the rows that are grouped together are then summed.

Line 3-7: you use the [CASE statement](https://www.freecodecamp.org/news/case-statement-in-sql-example-query/) to get different results depending on a condition. In this case, a row is counted as 1 if it contains a book title, otherwise it is counted as 0. And here we use `LIKE` to check if the cell contains any characters (learn more in this [article about Contains String](https://www.freecodecamp.org/news/sql-contains-string-sql-regex-example-query)).

Line 8: this gives a name of `number_of_books` to the column that is created for the SUM.

Line 9: the left/first table in this case is `authors`.

Line 10: the right/second table in this case is `books`.

Line 11: this joins the two tables using the author names.

Line 12: the rows are [grouped by author name](https://www.freecodecamp.org/news/sql-group-by-clauses-explained/) - all the rows with the same value in that column will be represented by a single row.

Line 13: we use [order by](https://www.freecodecamp.org/news/sql-order-by-statement-example-sytax/) to arrange in descending order using the number of books.

The query will give you the below table. Note that you see here only the authors that are present in the `authors` table. The authors mentioned in the `books` table without an entry in the `authors` table are not present here. This is an effect of the fact that the unrelated rows from the `books` table were not kept.

| author_name | number_of_books |
| -- | -- |
| Luigi Pirandello | 2 |
| Giovanni Verga | 1 |
| Cesare Pavese | 0 |
| Giuseppe Tomasi di Lampedusa | 0 |
| Italo Svevo | 0 |

If the `authors` table is updated to include all the authors mentioned in the `books` table, like this:

| author_id | name | year_of_birth | place_of_birth | trivia |
| --- | --- | --- | --- | --- |
| 1 | Luigi Pirandello | 1867 | Agrigento | Nobel Prize in Literature in 1934 |
| 2 | Giovanni Verga | 1840 | Vizzini | was Senator of the Kingdom of Italy from 1920 to 1922 |
| 3 | Italo Svevo | 1861 | Trieste | real name was Aron Hector Schmitz |
| 4 | Cesare Pavese | 1908 | Santo Stefano Belbo | NULL |
| 5 | Giuseppe Tomasi di Lampedusa | 1896 | Palermo | was prince of Lampedusa from 1934 to 1957 |
| 6 | Italo Calvino | 1923 | Santiago de las Vegas | NULL |
| 7 | Emilio Salgari | 1862 | Verona | NULL |
| 8 | Leonardo Sciascia | 1921 | Racalmuto | NULL |

Then the table from the query above would actually give the number of books for all authors.

| author_name | number_of_books |
| -- | -- |
| Leonardo Sciascia | 2 |
| Luigi Pirandello | 2 |
| Emilio Salgari | 1 |
| Giovanni Verga | 1 |
| Giovanni Verga | 1 |
| Cesare Pavese | 0 |
| Giuseppe Tomasi di Lampedusa | 0 |
| Italo Svevo | 0 |

# Conclusion

In a Relational Database, data should be written only once, so we often end up with multiple tables related to each other. `LEFT JOIN` is a really useful ally when we need to analyse data and join information from different tables. Enjoy querying your database using this powerful tool.

