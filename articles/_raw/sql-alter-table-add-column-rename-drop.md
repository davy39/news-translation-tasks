---
title: SQL Alter Table - How to Add a Column, Rename it, or Drop it - Explained with
  Syntax Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-05T22:23:00.000Z'
originalURL: https://freecodecamp.org/news/sql-alter-table-add-column-rename-drop
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f93740569d1a4ca4356.jpg
tags:
- name: SQL
  slug: sql
seo_title: null
seo_desc: 'This is a guide to SQL ALTER TABLE

  This guide will introduce you to and attempt to explain some of the basics of the
  SQL alter table functions within a relational database.  IMPORTANT Safety Tip: ALWAYS
  backup your data before making changes!

  We will...'
---

## This is a guide to SQL ALTER TABLE

This guide will introduce you to and attempt to explain some of the basics of the SQL alter table functions within a relational database.  **IMPORTANT Safety Tip: ALWAYS backup your data before making changes!**

We will be using MySQL for all examples throughout this freeCodeCamp SQL guide. The reasons for selecting MySQL are 1) it is very commonly used on websites for the backend database, 2) it’s free, and is fun and easy to use.

## Covered in this Guide

We will use the tables created in the “CREATE TABLE” guide. Feel free to review that guide if you are not familiar with creating a table.

* Altering the created table will alter it in several different ways.
* We’ll change its name and modify columns
* Add columns (while adding columns we will also review several of the most important column types and their use).
* Drop columns (meaning remove the column).
* Creating a table by importing a CSV file and altering that table.
* Creating and modifying tables with MySQL workbench tools.

Most of this will be done using SQL statements in the MySQL workbench scripting tool but we will also review how to alter a table using the workbench interface instead of with SQL statements.

## The table before alterations

Add date and email address columns (a date and a character column):

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/alter_table01.JPG)

Add a numeric column (note that it was added in a specific location in the table):

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/alter_table02.JPG)

Rename some columns:

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/alter_table03.JPG)

You can also use the alter table workbench tool. Just RIGHT click on the table you want to change and change as you wish.

There is much more that can be done, check the manual of your database management software to learn more.

