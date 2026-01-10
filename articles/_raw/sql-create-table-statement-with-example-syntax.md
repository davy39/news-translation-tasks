---
title: SQL Create Table Statement - With Example Syntax
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-21T15:58:38.000Z'
originalURL: https://freecodecamp.org/news/sql-create-table-statement-with-example-syntax
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/fabio-oyXis2kALVg-unsplash.jpg
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: null
seo_desc: 'By Jonathan Sexton

  SQL is one of the most reliable and straightforward querying languages around. It
  provides clear cut syntax that reads easily without abstracting away too much of
  the functionality''s meaning.

  If you''d like some history on the langu...'
---

By Jonathan Sexton

SQL is one of the most reliable and straightforward querying languages around. It provides clear cut syntax that reads easily without abstracting away too much of the functionality's meaning.

If you'd like some history on the language as well as some interesting facts, check out the introduction portion of my [SQL Update Statement article](https://www.freecodecamp.org/news/sql-update-statement-example-queries-for-updating-table-values/).  

In this article, we're going to go through the important parts of creating a table in SQL.  My preferred "flavor" of SQL is SQL Server but the information about creating a table is fairly ubiquitous across all SQL variations.  

If you've never used SQL or don't know what a table is, fear not! Briefly (and broadly), a table is a database object that holds, or contains, all of the data within that portion of the database. It stores this data in named columns and numbered rows which is not unfamiliar if you've ever used any spreadsheet program. Each row represents a whole database record.

If data were in box form then a table would be a section of the warehouse shelving we store those boxes in.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/nana-smirnova-IEiAmhXehwE-unsplash.jpg)
_Photo by [Unsplash](https://unsplash.com/@nananadolgo?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Nana Smirnova</a> on <a href="https://unsplash.com/s/photos/warehouse?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText)_

I'm simplifying the explanation greatly and there is much more to SQL tables but that's outside the scope of this article.  If you're itching for a more in-depth explanation on tables, I encourage you to dive into the [Microsoft Database Design documentation](https://docs.microsoft.com/en-us/sql/relational-databases/tables/tables?view=sql-server-ver15).

Before we learn how to create the table, it's important that we learn what types of data these columns and rows can store.

## Data Types

SQL tables can hold text, numbers, a combination of text and numbers, as well as images and links.

When creating our table, we designate the type of data its rows and columns will hold. Here are the overarching classifications of data:

- Approximate Numerics
- Strings
- Date & Time
- Unicode Character Strings
- Exact Numerics
- Other

I'll list some of the more commonly used data types below, but if you'd like a more on all data types, I invite you to check out this [exhaustive article on each type from Microsoft](https://docs.microsoft.com/en-us/sql/t-sql/data-types/data-types-transact-sql?view=sql-server-ver15). 

Here are the more commonly used types of data from my experience, in no particular order:

- char(size) - *fixed* length string that can contain letters, numbers, special characters
- varchar(size) - *variable* length string that can contain letters, numbers, & special characters
- boolean - Zero (or values that equate to 0) is false, non-zero is true
- int(*size optional*) - a number up to 10 characters in length, accepts negative & positive numbers
- bigint(*size optional*) - a number up to 19 characters in length, accepts negative & positive numberrs
- float(size, d) - a number with total number size represented by size and the number of characters after the decimal represented by the *d*
- date - date in the format of *YYYY-MM-DD*
- datetime - date time in the format of *YYY-MM-DD hh:mm:ss*
- time - time in the format of *hh:mm:ss*

Alright, now that we know what types of data the rows and columns can contain let's get into the fun parts!

## Creating a Table

![Image](https://www.freecodecamp.org/news/content/images/2020/07/nikhil-mitra-Q_6BS8IN0J8-unsplash.jpg)
_Photo by [Unsplash](https://unsplash.com/@nikhilmitra?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Nikhil Mitra</a> on <a href="https://unsplash.com/s/photos/create?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText)_

Before we start it's important to note that I'll be providing all of my examples independent of any program. 

However, if you'd like to start writing queries and you aren't sure where to start, take a look at [SQL Server Management Studio.](https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver15) It's a free, robust program that's widely used and supported in the community.

Alternatively, there are several options including [DB Fiddle](https://www.db-fiddle.com/) that allow you to build schemas and write queries right in your browser.  

Let's start with a simple statement to create a basic table:

<code>CREATE TABLE table_name (
    column1_name datatype, 
    column2_name datatype,
    column3_name datatype,
    column4_name datatype,
    column5_name datatype,)</code>

There are other parameters we can add after the `datatype` to augment the columns:

- `NOT NULL` - passing this parameter will ensure the column cannot hold a `NULL` value
- `UNIQUE` - passing this parameter will prevent the column from holding the same value more than once
- `UNIQUE KEY` - passing this parameter will designate that column as a unique identifier. It is essentially a combination of the previous two parameters.

Now, we're going to create a table (named doggo_info which must adhere to the [identifier standards for databases](https://docs.microsoft.com/en-us/sql/relational-databases/databases/database-identifiers?view=sql-server-ver15)) to hold information on the residents of Woof Woof Retreat, a fictional doggy daycare I just thought of :)

<code>CREATE TABLE doggo_info (
ID int UNIQUE KEY,
Name varchar(50) NOT NULL, 
Color varchar(50), 
Breed varchar(50), 
Age int, 
Weight int, 
Height int, 
Fav_Food varchar(100), 
Fav_Toy varchar(100), 
Dislikes varchar(500), 
Allergies varchar(500) NOT NULL
    )
</code>	    

And here is the brand new table we just created:

<table>
    <tr style="font-weight: bold;">
      <td>Name</td>
      <td>Color</td>
      <td>Breed</td>
      <td>Age</td>
      <td>Weight</td>
      <td>Height</td>
      <td>Fav_Food</td>
      <td>Fav_Toy</td>
      <td>Dislikes</td>
      <td>Allergies</td>
    </tr>
    <tr>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> </td>
    </tr>
</table>

You'll notice that our table is completely empty and this is because we haven't added any data to it yet. Doing so is beyond the scope of this article but I wanted you to be aware of that tidbit.

###Create A Table From An Existing Table

It is also possible to create a new table based off of an existing table.

It's pretty easy and doesn't require that much more syntax. We need to select the table and columns to "copy" from:

<code>CREATE TABLE new_table_name AS
SELECT column1, column2, column3, column4 (use * to select all columns to be added to the new_table)
FROM current_table_name
WHERE conditions_exist</code>

So, expediency's sake, I've added some data to our `doggo_info` table and it now looks like the example below:

<table>
  <th>
    <tr style="font-weight: bold;">
      <td>Name</td>
      <td>Color</td>
      <td>Breed</td>
      <td>Age</td>
      <td>Weight</td>
      <td>Height</td>
      <td>Fav_Food</td>
      <td>Fav_Toy</td>
      <td>Dislikes</td>
      <td>Allergies</td>
    </tr>
  </th>
  <tbody>
    <tr>
      <td>daisy</td>
      <td>red</td>
      <td>standard dachshund</td>
      <td>1</td>
      <td>14</td>
      <td>6</td>
      <td>salmon flavored kibble</td>
      <td>squeeky ball</td>
      <td>birds flying over the yard</td>
      <td>cats, baths, cleanliness</td>
    </tr>
    <tr>
      <td>chief</td>
      <td>black/tan</td>
      <td>rottweiler</td>
      <td>3</td>
      <td>41</td>
      <td>17</td>
      <td>literally anything</td>
      <td>rope tug</td>
      <td>staying off the couch</td>
      <td>listening, behaving, not slobbering on everything</td>
    </tr>
    <tr>
      <td>sammie</td>
      <td>light honey</td>
      <td>golden retriever</td>
      <td>9</td>
      <td>46</td>
      <td>19</td>
      <td>beef flavored kibble</td>
      <td>her bed</td>
      <td>rambutcious puppies</td>
      <td>none known</td>
    </tr>
  </tbody>
</table>

Now we can create another table based off of the data we have in our `doggo_info` table by running the query below:

<code>CREATE TABLE puppies_only AS
SELECT *
FROM doggo_info
WHERE Age < 4 </code>

We want to create a new table with all of the columns from the `doggo_info` table but only where the `Age` is less than 4. After running this query, our new table will look like this:

<table>
  <th>
    <tr style="font-weight: bold;">
      <td>Name</td>
      <td>Color</td>
      <td>Breed</td>
      <td>Age</td>
      <td>Weight</td>
      <td>Height</td>
      <td>Fav_Food</td>
      <td>Fav_Toy</td>
      <td>Dislikes</td>
      <td>Allergies</td>
    </tr>
  </th>
  <tbody>
    <tr>
      <td>daisy</td>
      <td>red</td>
      <td>standard dachshund</td>
      <td>1</td>
      <td>14</td>
      <td>6</td>
      <td>salmon flavored kibble</td>
      <td>squeeky ball</td>
      <td>birds flying over the yard</td>
      <td>cats, baths, cleanliness</td>
    </tr>
    <tr>
      <td>chief</td>
      <td>black/tan</td>
      <td>rottweiler</td>
      <td>3</td>
      <td>41</td>
      <td>17</td>
      <td>literally anything</td>
      <td>rope tug</td>
      <td>staying off the couch</td>
      <td>listening, behaving, not slobbering on everything</td>
    </tr>
  </tbody>
</table>

I hope you can see just how powerful this statement can be.  With a few lines in our query we have essentially copied data from one table into another but only the rows that we wanted.  

This is not only a handy tool to have in your developer tool belt – it'll save you untold amounts of time when you need to move data around tables.

##Wrapping Up

Now that you know how to create (or copy) a table in SQL no matter what situation you're presented with, you can start filling the columns and rows with data to store!

The `CREATE TABLE` statement is extremely useful and powerful. You're ready to start putting it to good use.

If you found this article helpful check out my [blog](https://jonathansexton.me/blog) where I frequently post articles about web development, life, and learning.

While you're there why not sign up for my newsletter? You can do that at the top right of the main blog page. I like to send out interesting articles (mine and others), resources, and tools for  developers every now and then.

If you have questions about this article or just in general let me know – come say hi on [Twitter](https://twitter.com/jj_goose) or any of my other social media accounts which you can find below the  newsletter sign up on the main page of my blog or on my profile here at fCC :)

Have an awesome day! Happy learning and happy coding, friend!

