---
title: Case Statement in SQL – Example Query
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2021-08-16T13:57:32.000Z'
originalURL: https://freecodecamp.org/news/case-statement-in-sql-example-query
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/pexels-anete-lusina-4792286.jpg
tags:
- name: data analysis
  slug: data-analysis
- name: SQL
  slug: sql
seo_title: null
seo_desc: 'If you need to add a value to a cell conditionally based on other cells,
  SQL''s case statement is what you''ll use.

  If you know other languages, the case statement in SQL is similar to an if statement,
  or a switch statement. It allows you to conditiona...'
---

If you need to add a value to a cell conditionally based on other cells, SQL's case statement is what you'll use.

If you know other languages, the case statement in SQL is similar to an if statement, or a switch statement. It allows you to conditionally specify a value, so that, depending on the condition satisfied, you get a different value in the cell.

This can be really important in Data Analysis, so after introducing the Case Statement we will see a couple of examples of how you can use it to analyse data in a simple way.

# SQL Case Statement Syntax

The syntax has a lot of stuff in it, but it is still rather intuitive: the keyword `CASE` signals the beginning of a case statement, and the keyword `END` signals its end.

Then for a single condition you can write the keyword `WHEN` followed by the condition that has to be satisfied. After that comes the keyword `THEN` and the value for that condition, like `WHEN <condition> THEN <stuff>`.

This can then be followed by other `WHEN`/`THEN` statements.

At the end you can add a value to use by default if none of the conditions are true with the `ELSE`  keyword, as shown below.

```sql
CASE
   WHEN condition1 THEN stuff
   WHEN condition2 THEN other stuff
   ...
   ELSE default stuff
END
```

Let's put this to practice to understand it better.

# SQL Case Statement Examples

Let's use the `CASE` statement in an example. We have a table with a list of students and their scores on an exam. We need to give each student a grade, and we can use the case statement to do it automatically.

| id | name | score |
| -- | -- | -- |
| 1 | Simisola | 60|
| 2 | Ivan | 80 |
| 3 | Metodija | 52 |
| 4 | Callum | 98 |
| 5 | Leia | 84 |
| 6 | Aparecida | 82 |
| 7 | Ursula | 69 |
| 8 | Ramazan | 78 |
| 9 | Corona | 87 |
| 10 | Alise | 57 |
| 11 | Galadriel | 89 |
| 12 | Merel | 99 |
| 13 | Cherice | 55 |
| 14 | Nithya | 81 |
| 15 | Elşad | 71 |
| 16 | Liisi | 90 |
| 17 | Johanna | 90 |
| 18 | Anfisa | 90 |
| 19 | Ryōsuke | 97 |
| 20 | Sakchai | 61 |
| 21 | Elbert | 63 |
| 22 | Katelyn | 51 |

We can use the `CASE` statement to give each student a grade, which we will add in a new column named `grade`.

Let's first write the `CASE` statement, in which we will write the breakdown for each grade. When `score` is 94 or higher, the row will have the value of `A`. If the score is instead 90 or higher it will have the value of `A-`, and so on.

```sql
  CASE
    WHEN score >= 94 THEN "A"
    WHEN score >= 90 THEN "A-"
    WHEN score >= 87 THEN "B+"
    WHEN score >= 83 THEN "B"
    WHEN score >= 80 THEN "B-"
    WHEN score >= 77 THEN "C+"
    WHEN score >= 73 THEN "C"
    WHEN score >= 70 THEN "C-"
    WHEN score >= 67 THEN "D+"
    WHEN score >= 60 THEN "D"
    ELSE "F"
  END
```

After we've written the `CASE` statement, we will add it in a query. Then we'll give to the column the name `grade` using the `AS` keyword:

```sql
SELECT *,
  CASE
    WHEN score >= 94 THEN "A"
    WHEN score >= 90 THEN "A-"
    WHEN score >= 87 THEN "B+"
    WHEN score >= 83 THEN "B"
    WHEN score >= 80 THEN "B-"
    WHEN score >= 77 THEN "C+"
    WHEN score >= 73 THEN "C"
    WHEN score >= 70 THEN "C-"
    WHEN score >= 67 THEN "D+"
    WHEN score >= 60 THEN "D"
    ELSE "F"
  END AS grade
FROM students_grades;
```

The table we get from this query looks like the below – and now each student has a grade based on their score.

| id | name | score | grade |
| -- | -- | -- | -- |
| 1 | Simisola | 60 | D |
| 2 | Ivan | 80 | B- |
| 3 | Metodija | 52 | F |
| 4 | Callum | 98 | A |
| 5 | Leia | 84 | B |
| 6 | Aparecida | 82 | B- |
| 7 | Ursula | 69 | D+ |
| 8 | Ramazan | 78 | C+ |
| 9 | Corona | 87 | B+ |
| 10 | Alise | 57 | F |
| 11 | Galadriel | 89 | B+ |
| 12 | Merel | 99 | A |
| 13 | Cherice | 55 | F |
| 14 | Nithya | 81 | B- |
| 15 | Elşad | 71 | C- |
| 16 | Liisi | 90 | A- |
| 17 | Johanna | 90 | A- |
| 18 | Anfisa | 90 | A- |
| 19 | Ryōsuke | 97 | A |
| 20 | Sakchai | 61 | D |
| 21 | Elbert | 63 | D |
| 22 | Katelyn | 51 | F |

## More Complex Case Statement Examples

We can also manipulate the table in different ways depending on what we need using other statements in addition to the case statement.

### Case Statement Example 1

For example we can use [`ORDER BY`](https://www.freecodecamp.org/news/sql-order-by-statement-example-sytax/) to sort the rows to have the highest grades on top.

```sql
SELECT name,
  CASE
    WHEN score >= 94 THEN "A"
    WHEN score >= 90 THEN "A-"
    WHEN score >= 87 THEN "B+"
    WHEN score >= 83 THEN "B"
    WHEN score >= 80 THEN "B-"
    WHEN score >= 77 THEN "C+"
    WHEN score >= 73 THEN "C"
    WHEN score >= 70 THEN "C-"
    WHEN score >= 67 THEN "D+"
    WHEN score >= 60 THEN "D"
    ELSE "F"
  END AS grade
FROM students_grades
ORDER BY score DESC;
```

We order based on `score` which is a number, instead of the `grade` column, as the alphabetical order is not the same as the order of the grades based on their value. We use the `DESC` keyword to render it in descending order, with the highest value at the top.

The table we get looks like the below:

| name | grade |
| --- | --- |
| Merel | A |
| Callum | A |
| Ryōsuke | A |
| Liisi | A- |
| Johanna | A- |
| Anfisa | A- |
| Galadriel | B+ |
| Corona | B+ |
| Leia | B |
| Aparecida | B- |
| Nithya | B- |
| Ivan | B- |
| Ramazan | C+ |
| Elşad | C- |
| Ursula | D+ |
| Elbert | D |
| Sakchai | D |
| Simisola | D |
| Alise | F |
| Cherice | F |
| Metodija | F |
| Katelyn | F |

### Case Statement Example 2

Let's do a bit of analysis on these data. We can use [`GROUP BY` and `COUNT`](https://www.freecodecamp.org/news/sql-group-by-clauses-explained/) to count how many students received each grade.

```sql
SELECT 
  CASE
    WHEN score >= 94
      THEN "A"
    WHEN score >= 90 THEN "A-"
    WHEN score >= 87 THEN "B+"
    WHEN score >= 83 THEN "B"
    WHEN score >= 80 THEN "B-"
    WHEN score >= 77 THEN "C+"
    WHEN score >= 73 THEN "C"
    WHEN score >= 70 THEN "C-"
    WHEN score >= 67 THEN "D+"
    WHEN score >= 60 THEN "D"
    ELSE "F"
  END AS grade,
  COUNT(*) AS number_of_students
FROM students_grades
GROUP BY grade
ORDER BY score DESC;

```

We use `[ORDER BY](https://www.freecodecamp.org/news/sql-order-by-statement-example-sytax/)` to order the grades from highest to lowest, and we use `score` as it is a numerical value (as ordering by the `grade` column would use alphabetical order, which is not the same as the order by value of the grades).

| grade | number_of_students |
| -- | -- |
| A | 3 |
| A- | 3 |
| B+ | 2 |
| B | 1 | 
| B- | 3 |
| C+ | 1 |
| C- | 1 |
| D+ | 1 |
| D | 3 |
| F | 4 |

### Case Statement Example 3

Let's do a bit of different analysis on these data. We can use [`GROUP BY` and `COUNT`](https://www.freecodecamp.org/news/sql-group-by-clauses-explained/) and a different case statement to count how many students passed the exam. Then we can use `[ORDER BY](https://www.freecodecamp.org/news/sql-order-by-statement-example-sytax/)` to have the column in the order we prefer, with the number of students that passed on top.

```sql
SELECT 
  CASE
    WHEN score >= 60
      THEN "passed"
    ELSE "failed"
  END AS result,
  COUNT(*) AS number_of_students
FROM students_grades
GROUP BY result
ORDER BY result DESC;
```

The table we get looks like the below. The class is not doing too badly, with 18 students of 22 having passing grades – but the other 4 may need some help.

| result | number_of_students |
| -- | -- |
| passed | 18 |
| failed | 4 |

# Conclusion

The case statement is a powerful tool you can use when you need to get values based on certain conditions.

In this article you have learned how to use it, and you've seen a few examples of how you can use it for Data Analysis.

