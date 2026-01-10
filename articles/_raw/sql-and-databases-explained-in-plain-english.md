---
title: What is SQL? What is a Database? Relational Database Management Systems (RDBMS)
  Explained in Plain English.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-12-07T16:29:55.000Z'
originalURL: https://freecodecamp.org/news/sql-and-databases-explained-in-plain-english
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c96c2740569d1a4ca127c.jpg
tags:
- name: database
  slug: database
- name: MySQL
  slug: mysql
- name: SQL
  slug: sql
seo_title: null
seo_desc: "By Sameer Khoja\nDatabases can be tricky to wrap your head around. However,\
  \ they're essential to full-stack programming and building out back-end services\
  \ that store data. \nIn this post, I'll be demystifying SQL, Databases, and Relational\
  \ Database Man..."
---

By Sameer Khoja

Databases can be tricky to wrap your head around. However, they're essential to full-stack programming and building out back-end services that store data. 

In this post, I'll be demystifying SQL, Databases, and Relational Database Management Systems. I'll also be using some analogies to the [Wizarding World](https://en.wikipedia.org/wiki/Wizarding_World), including Harry Potter himself and some of the classes he takes at Hogwarts.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-135.png)

Before we dive into Key Terms, let's define what a database itself is:

A **database** is a structured set of data held in a computer, especially one that is accessible in various ways. It is essentially an organized set of data on a computer, which can be accessed electronically from a computer system.

## Key Terms

Below are some key terms that we'll start with:

* **RDMS:** Relational Database Management Systems. This framework for databases is the basis of MySQL.
* **SQL:** Structured Query Language.
* **Tables:** Database objects that carry data. An example of a table name is "Students", or "Teachers", or "Courses".
* **Fields:** The values of a table are known as fields. Example fields for Students would be "First Name", "Last Name", and "GPA".
* **Record/Row:** An individual entry in the table. 

After adding Teachers and Courses to the database, we can have tables for Students, Teachers, and Courses. 

As we move forward in the guide we will only be using the **Students** example here as a reference. If you were fortunate enough to be hired as a Software Engineer at Hogwarts, your database might make good use of some of these commands :D

## SQL Statements

### Syntax

The semicolon is the standard way to separate one SQL statement from another. It allows for multiple SQL statements to be run in the same call. In this guide, we will have a semicolon at the end of each statement.

### The Most Important SQL Commands

**Create**: Creates a new SQL table. 

If we were creating the student database for the Hogwarts School, for example, we would use **CREATE** to make a table called "Students". 

* Syntax

```sql
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype,
   ....
);
```

* Example

```sql
CREATE TABLE Students
                (first_name VARCHAR(255),
                last_name VARCHAR(255),
                login VARCHAR(255),
                age INTEGER,
                gpa REAL,
                house VARCHAR(255));
```

**Drop**: Deletes a table. Be very careful when using this command as this will erase all data in the table!

If we wanted to delete the entire Student database we will use **DROP** to perform that action.

* Syntax

```sql
DROP TABLE table_name;
```

* Example

```sql
DROP TABLE Students;
```

**Insert**: Adds new rows of data to a table. 

We would use **INSERT** to add new students as they enroll into Hogwarts. 

* Syntax

```sql
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
```

* Example

```sql
INSERT 
INTO Students(first_name, last_name, login, age, gpa, house)
VALUES 
('Harry',     'Potter', 'theboywholived', 15, 4.0, 'Gryffindor'),
('Hermionie', 'Granger','granger2',       15, 4.5, 'Gryffindor'),
('Ron',       'Weasley','weasley7',       15, 3.7, 'Gryffindor'),
('Draco',     'Malfoy', 'malfoy999',      15, 4.0, 'Slytherin'),
('Cedric',    'Diggory','diggory123',     15, 4.0, 'Hufflepuff');
```

**Select**: Used to fetch data in a database to be returned in table format. 

If we wanted to retrieve all the Names of Students that are in Gryffindor House, we would use the **SELECT** command. The below example queries the Students table for the first name and last name of every student in the database, which for us is just the five rows described above.

* Syntax

```sql
SELECT column1, column2, ...
FROM table_name;
```

* Example

```sql
SELECT first_name, last_name FROM Students;
```

| first_name | last_name |
| ---------- | --------- |
| Harry      | Potter    |
| Hermionie  | Granger   |
| Ron        | Weasley   |
| Draco      | Malfoy    |
| Cedric     | Diggory   |

Alternatively, if we want to select all of the fields in the table, our command would utilize the "*" syntax, which signifies selecting all fields:

```sql
SELECT * FROM Students;
```

| first_name | last_name | login          | age | gpa | house      |
| ---------- | --------- | -------------- | --- | --- | ---------- |
| Harry      | Potter    | theboywholived | 15  | 4   | Gryffindor |
| Hermionie  | Granger   | granger2       | 15  | 4.5 | Gryffindor |
| Ron        | Weasley   | weasley7       | 15  | 3.7 | Gryffindor |
| Draco      | Malfoy    | malfoy999      | 15  | 4   | Slytherin  |
| Cedric     | Diggory   | diggory123     | 15  | 4   | Hufflepuff |

### Clauses

A **clause** is a logical chunk of an SQL statement, and it is (in theory) an optional field. 

In the above statement, we simply returned all of the fields in the Student database. We didn't specify a condition on the values being returned. 

What if we wanted to query not all the students, but only those whose house is Gryffindor? What about querying students whose first name starts with "H", or students in either Hufflepuff and Slytherin? These more complex cases are solved by SQL clauses.

Below is an overview of the most common clauses, but there are several more clauses in the SQL language. Here's a [good general overview](https://www.freecodecamp.org/news/basic-sql-commands/) if you want some more info.

### Examples of Clauses

**Where:** Used to state a condition while fetching data from a database. Going back to the example with Select, we would have to use **WHERE** in order to specify the house as Gryffindor.

* Syntax

```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

* Example

```sql
SELECT * FROM Students
WHERE house='Gryffindor';
```

| first_name | last_name | login          | age | gpa | house      |
| ---------- | --------- | -------------- | --- | --- | ---------- |
| Harry      | Potter    | theboywholived | 15  | 4   | Gryffindor |
| Hermionie  | Granger   | granger2       | 15  | 4.5 | Gryffindor |
| Ron        | Weasley   | weasley7       | 15  | 3.7 | Gryffindor |

**And** Used to combine multiple clauses in a SQL statement, where all conditions separated by the AND are true. We would use AND to get Gryffindor students who have above a 3.8 GPA.

* Syntax

```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition1 AND condition2 AND condition3 ...;
```

* Example

```sql
SELECT * FROM Students
WHERE house='Gryffindor' AND gpa>3.8;
```

| first_name | last_name | login          | age | gpa | house      |
| ---------- | --------- | -------------- | --- | --- | ---------- |
| Harry      | Potter    | theboywholived | 15  | 4   | Gryffindor |
| Hermionie  | Granger   | granger2       | 15  | 4.5 | Gryffindor |

**Or**: Similar to AND, but only returns data in which only ONE of the conditions separated by the OR are true. If we wanted to retrieve students in Hufflepuff and Slytherin, but not both, we would use the OR command.

* Syntax

```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition1 OR condition2 OR condition3 ...;
```

* Example

```sql
SELECT * FROM Students
WHERE house='Slytherin' OR house='Hufflepuff';
```

| first_name | last_name | login      | age | gpa | house      |
| ---------- | --------- | ---------- | --- | --- | ---------- |
| Draco      | Malfoy    | malfoy999  | 15  | 4   | Slytherin  |
| Cedric     | Diggory   | diggory123 | 15  | 4   | Hufflepuff |

**Like:** Used with WHERE to search for a specific pattern. If we only wanted the first and last name of wizards/witches with names starting with "H", we could utilize the Like command.

* Syntax

```sql
SELECT column1, column2, ...
FROM table_name
WHERE columnN LIKE pattern;
```

* Example

```sql
SELECT first_name, last_name FROM Students
WHERE first_name LIKE 'H%';
```

| first_name | last_name |
| ---------- | --------- |
| Harry      | Potter    |
| Hermionie  | Granger   |

**Count:** Used to find the count of a column (or columns) in a table.

* Syntax

```sql
SELECT COUNT(column_name)
FROM table_name
WHERE condition;
```

* Example

```sql
SELECT COUNT(first_name) FROM Students;
```

| COUNT(first_name) |
| ----------------- |
| 5                 |

Two other commands which use the same syntax are AVG and SUM. AVG will compute the average of all values, and sum will compute the sum of all values.

**Select Limit:** Used to cut off responses to just a specified amount. The way the top responses are chosen is in order of first inserted into the database chronologically.

* Syntax

```sql
SELECT column_name(s)
FROM table_name
WHERE condition
LIMIT number;
```

* Example

```sql
SELECT * FROM Students LIMIT 3;
```

| first_name | last_name | login          | age | gpa | house      |
| ---------- | --------- | -------------- | --- | --- | ---------- |
| Harry      | Potter    | theboywholived | 15  | 4   | Gryffindor |
| Hermionie  | Granger   | granger2       | 15  | 4.5 | Gryffindor |
| Ron        | Weasley   | weasley7       | 15  | 3.7 | Gryffindor |

### Other Useful Commands

**Order By:** Sorts the results in ascending or descending order.

* Syntax

```sql
SELECT column1, column2, ...
FROM table_name
ORDER BY column1, column2, ... ASC|DESC;
```

* Example

```sql
SELECT * FROM Students ORDER BY first_name;
```

| first_name | last_name | login          | age | gpa | house      |
| ---------- | --------- | -------------- | --- | --- | ---------- |
| Cedric     | Diggory   | diggory123     | 15  | 4   | Hufflepuff |
| Draco      | Malfoy    | malfoy999      | 15  | 4   | Slytherin  |
| Harry      | Potter    | theboywholived | 15  | 4   | Gryffindor |
| Hermionie  | Granger   | granger2       | 15  | 4.5 | Gryffindor |
| Ron        | Weasley   | weasley7       | 15  | 3.7 | Gryffindor |

**Group By:** Groups categories that have the same values into rows. If you wanted to know the number of students in each house (3 in Gryffindor for example), you can utilize the Group By command.

* Syntax

```sql
SELECT column_name(s)
FROM table_name
WHERE condition
GROUP BY column_name(s)
ORDER BY column_name(s);
```

* Example

```sql
SELECT COUNT(first_name), house FROM Students GROUP BY house;
```

| COUNT(first_name) | house      |
| ----------------- | ---------- |
| 3                 | Gryffindor |
| 1                 | Hufflepuff |
| 1                 | Slytherin  |

Finally, [here](https://www.db-fiddle.com/f/9Jq8KfBPtcYRh84PnPUQWi/61) is a DB Fiddle that shows all of the above commands in action!

## Normalized vs Denormalized Databases

When designing a database, there are two main design patterns you can follow, each with their own tradeoffs.

**Normalized:** Optimizes for **minimizing redundancy,** not for read time.

Let's say we have a courses table that has a teacher ID for the teacher teaching that course. We also have a teacher's database that has the teacher name. 

When we want to get names of teachers teaching a particular course, we will have to query both the Courses and Teachers tables because the course table doesn't have the teacher name (efficient but redundant).

**Denormalized:** Optimizes for **read time**, not for minimizing redundancy.

Let's say we have a courses table that has a teacher ID AND a teacher name. We have a teacher's database that also has the teacher name. When we want to get names of teachers in the course, we can just use the course table (redundant but efficient).

## Data Integrity

It's vital to users that the data they interact with is secure, correct and sensible. Examples are making sure that age isn't a negative number, or that no two students have the same information. We refer to this as **data integrity.** 

Data integrity takes several forms and can be divided into four categories:

* **Entity Integrity**: No duplicate rows exist in a table. For example, we can't insert Ron Weasley twice in the database.
* **Domain Integrity**: Restricting the type of values that one can insert in order to enforce correct values. For example, a House can only be Gryffindor, Ravenclaw, Slytherin, or Hufflepuff.
* **Referential Integrity**: Records that are used by other records cannot be deleted. A teacher cannot be deleted if they are currently teaching a course.
* **User-Defined Integrity:** An "other" category that consists of business-related logic and rules to the database.

## Common SQL Databases

* **Oracle**: Very stable and mature but can be costly
* **MySQL**:  Lightweight and fast to set up but not as mature as Oracle
* **PostgreSQL**: Good for certain use cases but not super fast

## Resources

* [SWEPrep - Interview Questions Straight To Your Inbox](https://sweprep.substack.com/)
* [freeCodeCamp's SQL and Databases](https://www.freecodecamp.org/news/sql-and-databases-full-course/)
* [Clean Code](https://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882)
* [Effective Java](https://www.amazon.com/Effective-Java-2nd-Joshua-Bloch/dp/0321356683)
* [Oracle Documentation](https://www.oracle.com/uk/database/index.html)
* [MySql Documentation](https://www.mysql.com/)
* [PostgreSQL Documentation](https://www.postgresql.org/)

## Staying Up-To-Date

* **Reddit Threads**: Great threads on databases, SQL and new technologies
* **[Hacker News](https://news.ycombinator.com/):** Really great resource to stay in-the-know on the latest developments in the tech industry
* **[CodePen](https://codepen.io/):** An excellent resource for discovering good SQL practices.

