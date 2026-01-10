---
title: The SQL Drop View Statement for Deleting Data from a Table
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-10T21:34:00.000Z'
originalURL: https://freecodecamp.org/news/the-sql-drop-view-statement
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ec9740569d1a4ca3f1c.jpg
tags:
- name: SQL
  slug: sql
seo_title: null
seo_desc: 'Introduction

  This guide covers the SQL statement for dropping (deleting) one or more view objects.

  A View is an object that presents data from one or more tables.

  Note: before deleting or changing data or objects, remember to have a fresh backup.

  We ...'
---

### Introduction

This guide covers the SQL statement for dropping (deleting) one or more view objects.

A View is an object that presents data from one or more tables.

Note: before deleting or changing data or objects, remember to have a fresh backup.

We will cover:

* Using SQL to drop a table
* Using the workbench to drop a view

We’ll be using MySQL for the demontration. Check the manual for this function in other Database Managers.

We’ll drop the view called  `students_dropMe_v` , which was created just for this purpose.

### Basic Syntax

```
DROP VIEW [IF EXISTS]
    view_name [, view_name] ...

```

### Drop View SQL

The if exists portion will “trap” errors, should the view not exist.

```
drop view if exists students_dropMe_v;

```

The view after creation:

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/drop-view01.JPG)

### Using the Workbench

From the workbench:

1. Right click on the view to drop
2. select drop view from the menu
3. Select either either a) run SQL to review the SQL statement to be executed or b) drop new

*As with all of these SQL things there is MUCH MORE to them than what’s in this introductory guide. I hope this at least gives you enough to get started.

Please see the manual for your database manager and have fun trying different options yourself.*

### Extra

Here’s the SQL I used to create the table that we just dropped:

```
create view `students_dropMe_v` as
select FullName, programOfStudy 
from student 
where programOfStudy = 'Programming';

```

