---
title: SQL Outer Join Tutorial – With Example Syntax
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-04-02T20:06:07.000Z'
originalURL: https://freecodecamp.org/news/sql-outer-join-tutorial-with-example-syntax
coverImage: https://cdn-media-2.freecodecamp.org/w1280/60651b659618b008528aadab.jpg
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: null
seo_desc: "By Veronica Stork\nWhat are SQL JOINs?\nIn SQL, JOINs are used to unite\
  \ the rows of two or more tables, based on a column that is shared between them.\
  \ \nThere are four different types of JOINs: INNER JOIN, LEFT JOIN, RIGHT JOIN,\
  \ and FULL OUTER JOIN. In ..."
---

By Veronica Stork

## What are SQL JOINs?

In SQL, JOINs are used to unite the rows of two or more tables, based on a column that is shared between them. 

There are four different types of JOINs: `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, and `FULL OUTER JOIN`. In this article, we will be discussing `FULL OUTER JOIN`.

## What is a Full Outer Join in SQL?

The `FULL OUTER JOIN` (aka `OUTER JOIN`) is used to return all of the records that have values in either the left _or_ right table. 

For example, a full outer join of a table of customers and a table of orders might return all customers, including those without any orders, as well as all of the orders. Customers who have made orders would be united with their orders using their customer id number.

A full outer join can return a lot of data, so before you use it, consider whether a more conservative method might meet your needs.

## Sample Data Set

Imagine that you are teaching an American Literature class. You have ten students, and you want each of them to read a different book from a list of pre-approved classic American novels. Some students have chosen the book they will read, while others have not done so yet.

You have created a table that lists the students along with their student ID numbers, and another table that lists books with their title, author, ISBN, and the ID of the student who will be reading the book, if someone has chosen it.

![Table with names of students and ID numbers](https://www.freecodecamp.org/news/content/images/2021/04/students-1.png)
_Students table_

![Table of books with isbn, id of student who will read it, title, and author](https://www.freecodecamp.org/news/content/images/2021/04/books.png)
_Books table_

## How to do an Outer Join in SQL

To do an outer join on our sample data, we could use the following query:

```sql
SELECT students.name, books.title
FROM students
FULL OUTER JOIN books ON students.student_id=books.student_id;
```

In this example, we are selecting the names from the `students` table and the book titles from the `books` table. Records are matched using the `student_id` column in both tables. 

The results look like this:

![student names matched with books they are reading. ](https://www.freecodecamp.org/news/content/images/2021/04/result.png)

With the full outer join, we are able to see all of the students, including those who have not chosen a book yet. We can also see all of the books, including those that have not yet been chosen. 

In our example, you could use this data to see who still needs to decide on a book, and which books are still available for them to choose from.

## Conclusion

Using a full outer join in SQL can help you get a complete view of the data from multiple related tables. 

Keep in mind, however, that with a large data set, this query may return an unwieldy amount of information, so use this power wisely!

  

