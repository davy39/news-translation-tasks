---
title: SQL Case Statement Tutorial – With When-Then Clause Example Queries
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-04-19T20:44:49.000Z'
originalURL: https://freecodecamp.org/news/sql-case-statement-tutorial-with-when-then-clause-example-queries
coverImage: https://cdn-media-2.freecodecamp.org/w1280/6067f407d5756f080ba93c3b.jpg
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: null
seo_desc: "By Veronica Stork\nWhat is a SQL Case Statement?\nA case statement is basically\
  \ SQL's version of conditional logic. It can be used in the same way as if statements\
  \ in programming languages like JavaScript, but it is structured slightly differently.\
  \ \nSa..."
---

By Veronica Stork

## What is a SQL Case Statement?

A case statement is basically SQL's version of conditional logic. It can be used in the same way as `if` statements in programming languages like JavaScript, but it is structured slightly differently. 

## Sample Data

Imagine that you are teaching a literature course. Your students must write an essay in order to meet the course requirements. 

You have created the table below to track which students have submitted their essay, along with their grade. If they have not yet submitted their essay, their grade is listed as `NULL`.

| student_id  | name |  submitted_essay  |   grade  |
| --- | -------------  |  -------------  | -------  |
| 1   | John             |  TRUE   | 86  |
| 2   | Said              |  TRUE   |  90  |
| 3   | Alyssa          |  FALSE   |  NULL  |
| 4   | Noah            |  TRUE   |  68  |
| 5   | Eleanor        |   TRUE   |  95  |
| 6   | Akiko            |  FALSE   | NULL  |
| 7   | Otto             |  TRUE   |  76  |
| 8   | Jamal          |  TRUE   |   85  |
| 9   | Kiara           |  TRUE   |  88  |
| 10 | Clement |   FALSE   |  NULL   |


## How to Write a Case Statement in SQL

Maybe you would like to give your students a message regarding the status of their assignment. To get the status, you could just select the `submitted_essay` column, but a message that just says `TRUE` or `FALSE` is not especially human-readable. 

Instead, you could use a `CASE` statement and print out different messages depending on whether `submitted_essay` is true or false.

The basic structure of the `CASE` statement is `CASE WHEN... THEN... END`. `CASE WHEN`, `THEN`, and `END` are all required. `ELSE` and `AS` are optional. The `CASE` statement must go in the `SELECT` clause.

```
SELECT name,
	CASE WHEN submitted_essay IS TRUE THEN 'essay submitted!'
	ELSE 'finish that essay!' END  AS status
FROM students;
```

In the above example, we are selecting our students' names and then displaying different messages in the `status` column depending on whether `submitted_essay` is true or not. The resulting table looks like the following:

|  name  |  status  |
|  ----  |  ------  |
| Akiko	| finish that essay! |
| Clement |	finish that essay! |
| Alyssa |	finish that essay! |
| Said	| essay submitted! |
| Eleanor |	essay submitted! |
| Otto	| essay submitted! |
| Noah	| essay submitted! |
| Kiara	| essay submitted! |
| John	| essay submitted! |
| Jamal	| essay submitted!|

Now, say you wanted to include a little more info. You want to comment on the students' grades if they have submitted their essay, and tell them to finish their essay if they have not yet submitted it. This is where multiple `WHEN/THEN` statements can be helpful.

```
SELECT name, essay_grade,
CASE WHEN essay_grade >= 80 THEN 'great job'
	 WHEN essay_grade < 80 THEN 'try harder'
	 ELSE 'finish that essay!' END  AS teacher_comment
FROM students;
```

In the code sample above, we are displaying the students' names and essay grades, along with comments that differ depending on their grades. 

After the first `WHEN/THEN` statement, you can add as many other `WHEN/THEN` statements as you need, along with an `ELSE` statement to catch other possible cases. This is analogous to `if... else if... else` style logic in JavaScript (or `if... elif... else` in Python, and so on). 

Note that in this case, `ELSE` is intended to catch the essays with grades of `NULL` (meaning those that have not yet been submitted,) but in other situations, you could use `IS NULL` to check if a selected value is null. 

Don't forget to end your case statement with `END`! Below, you can see the results of this query. 

|  name  |  essay_grade  | teacher_comment  |
|  -----  |  ----------  |  --------------  |
|  Akiko	|  NULL  |	finish that essay!  |
| Clement	|  NULL  |	finish that essay! |
|  Alyssa	|  NULL  |	finish that essay!  |
|  Said	 | 90  |	great job  |
|  Eleanor  |	95  |	great job  |
|  Otto	  |  76  |	try harder  |
|  Noah  |	68	|  try harder  |
|  Kiara  |	88	|  great job  |
|  John  |	86	|  great job  |
|  Jamal  |	85	|  great job  |





## Conclusion

Case statements are a clear, concise way to make sense of your queries in SQL, and they are easy to learn and understand. Happy querying!

