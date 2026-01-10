---
title: VLOOKUP Example – How to Do VLOOKUP in Excel
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-11T18:06:38.000Z'
originalURL: https://freecodecamp.org/news/vlookup-in-excel
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/pexels-photo-4050320-1.jpeg
tags:
- name: excel
  slug: excel
- name: Microsoft
  slug: microsoft
seo_title: null
seo_desc: 'By Gregory V. Chapman

  Microsoft Excel includes a variety of different functions that help users with calculations
  of any kind. The functionality of Excel is so comprehensive that average users don''t
  even take advantage of most utilities.

  However, if ...'
---

By Gregory V. Chapman

Microsoft Excel includes a variety of different functions that help users with calculations of any kind. The functionality of Excel is so comprehensive that average users don't even take advantage of most utilities.

However, if you often scroll through columns and rows looking for the same information, chances are that you will appreciate the VLOOKUP function. VLOOKUP, which stands for “vertical lookup,” can help you quickly find the data associated with a certain value that you enter.

For example, you may have a table that contains products with unique IDs and prices. VLOOKUP can show you the price of a certain product if you enter its ID. 

You can use VLOOKUP in many different ways and it will simplify your work significantly, especially when dealing with large tables.

You don’t need to spend a lot of time looking for a certain cell because this function will find it for you. However, beginner users often find it difficult to set up VLOOKUP. Therefore, I decided to help you by preparing this detailed guide.

## What is VLOOKUP?

![Image](https://www.freecodecamp.org/news/content/images/2020/06/m-b-m-ZzOa5G8hSPI-unsplash.jpg)

First of all, VLOOKUP is a function. Therefore, if you’re new to Excel, you may want to familiarize yourself with some basic functions, like AVERAGE, SUM, or TODAY. This way it will be easy for you to understand how this function works.

VLOOKUP is a database function, so it’s intended for database tables. Such tables are basically lists of different items. For instance, you may use this function when working with lists of products, employees, customers, etc.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/photo_2020-06-11_20-26-54.jpg)

Let’s say, you have a list of products that consists of four columns. It might include the item code in the first column, the name or description of the product in the second column, and the price and the number of items available in stock in the third and fourth columns, respectively.

Database tables usually have some sort of unique identifier for each item. In this case, it’s the item code. This column is necessary for the VLOOKUP function to operate, and it must be the first column in your table.

If you’re a beginner, the first thing you should do is to understand what exactly VLOOKUP does. Simply put, it shows information from a list or database based on the unique identifier entered by the user.

If we consider the example above, this function could show the price, description, or availability of a product based on its item code. What exactly it will show depends on the formula you write. VLOOKUP supports both exact and approximate matching, as well as wildcards for partial matches.

## How VLOOKUP Works

Here is the syntax for formulas that describe the VLOOKUP function:

`=VLOOKUP(value, table, column_index, [range])`

* `value` is what this function will look for in the first column
* `table` is the table from which the function will retrieve the necessary information
* `column_index` is the number of the column from which the function will retrieve the information
* `range` is a Boolean parameter that can be either TRUE or FALSE. TRUE is the default value, and it corresponds to approximate matching. FALSE will show you exact matches only.

Even the name of this function includes “vertical,” and VLOOKUP is only intended for tables where data is organized in vertical columns. Therefore, if you’re organizing your data horizontally, this function will be useless. In this case, you can use a similar function for horizontal lookup — [HLOOKUP](https://support.office.com/en-us/article/hlookup-function-a3034eec-b719-4ba3-bb65-e1ad662ed95f).

You should also keep in mind that this function only works from left to right. In other words, if the unique identifier is not in the first column of your table, the function won’t be able to retrieve information from the columns to the left of the identifier.

Every column has its number, and all columns are numbered from left to right. If you want to obtain a value from a certain column, you should specify its number in your formula. In the formula template above, this number is called `column_index`. 

For instance, if you want to retrieve the name of the product from the example above, the column index should be 2.

As I've already mentioned above, the VLOOKUP function supports two matching modes: approximate and exact. This parameter is the fourth argument in the formula. Approximate matching is set by default. If you want to choose exact matching, you should set the lookup range to `FALSE`.

Therefore, both of the formulas below will retrieve data using approximate matching:

`=VLOOKUP(value, table, column_index)`

`=VLOOKUP(value, table, column_index, TRUE)`

As you can see, if you want to use the exact match mode you should be careful. If you don’t provide any lookup range value, the function will still use the approximate match mode.

The following formula will force the exact matching mode:

`=VLOOKUP(value, table, column_index, FALSE)`

![Image](https://www.freecodecamp.org/news/content/images/2020/06/mika-baumeister-Wpnoqo2plFA-unsplash.jpg)

Make sure to set the value to `FALSE` if you’re going to use the exact match mode. Chances are that you’ll need exact matching in most cases, so if you’re new to Excel don’t forget about this detail. 

Exact match is the right choice if you have a column with the item identifier. It may also be any unique value that can be used for an exact lookup. For example, it may be a unique title of a book or movie, as well as any other unique keyword. Keep in mind that VLOOKUP is not case-sensitive.

However, sometimes you may need not the exact match but the best match possible one. In this case, you can use the approximate match mode. 

For instance, you may use this mode when dealing with data tables where the necessary information corresponds to certain numerical values, and you want to retrieve results for a value that isn’t included in the table.

You can use this approach when making calculations based on the existing data. If you enter a value and the function finds the exact match, it will retrieve information from the corresponding row. However, if there’s no exact match in the table, the function will match the previous row.

Why would it match the previous row, not another one? Well, it won’t if you don’t organize your table in the right way. To enable VLOOKUP to look for the best approximate value, you should make sure that all the values in this column are sorted in ascending order. In this case, the function will just step back and retrieve the nearest value.

## #N/A Errors

When using the VLOOKUP function, as well as many other functions in Excel, you may often get #N/A errors. This error means that the value was not found. 

You can get this error for several reasons. Here are some of the most common cases:

* you’ve misspelled the value or added an extra space
* the necessary value doesn’t exist in the table
* you’re using the exact match mode when searching for an approximate value
* you haven’t entered the correct table range
* you’ve copied VLOOKUP while the table reference isn’t locked.

If your table has an absolute reference, it means that the rows and columns won’t change if copied. However, this isn’t the case with a relative reference. In this case, you will need to [switch to the absolute reference](https://support.office.com/en-us/article/switch-between-relative-absolute-and-mixed-references-dfec08cd-ae65-4f56-839e-5f0d8d0baca9).

You can customize the text of the #N/A error by using the [IFNA function](https://support.office.com/en-ie/article/ifna-function-6626c961-a569-42fc-a49d-79b4951fd461). In this case, you have to write a longer formula with IFNA that includes VLOOKUP. 

Here’s an example of a formula that will return “not found” instead of #N/A:

`=IFNA(VLOOKUP(value, table, column_index, FALSE), "not found")`

And here is a formula that will return a blank result:

`=IFNA(VLOOKUP(value, table, column_index, FALSE), "")`

Although you can customize the message, you may consider using the #N/A error because it will immediately attract your attention and let you know if something goes wrong.

## How to Use VLOOKUP

You may write formulas from scratch, or you may also use the Excel menu. Select the cell where you want to display the result, and then select the “Formulas” tab. 

After this, click “Insert Function.” You will see a box where you can select categories of functions and choose the VLOOKUP function. You can also use the “Search for a function” box, and enter “vlookup.”

Select the function, and the “Function Argument” box will appear. Here you can enter the necessary parameters of the function. In this window, you should specify the unique identifier you’re looking for, database location, and the information that corresponds to the identifier that you want to retrieve.

These arguments are “Lookup_value,” “Table_array,” and “Col_index_num.” These fields are written in bold because these arguments are mandatory. 

The fourth argument if for the lookup mode, and you may or may not specify it. The approximate mode is set by default.

To enter the first argument, which is the unique identifier, you can select the necessary cell and press Enter. In this case, the value of this cell will be automatically entered as the first argument of the VLOOKUP function.

Now you have to enter the second argument. The database shouldn’t necessarily start at the top left corner. For instance, you may also have a row that describes columns, which serves as a header. 

“One of the best things about the VLOOKUP function is that the location of the database can also be customized,” notes Bridget Allen, an accountant at a [Best Writers Online](http://bestwritersonline.com/).

Given that VLOOKUP only works with numbers of columns, you should specify what area of your table you want to use for lookup. This is what the “Table_array” box is for. 

For example, if your table starts at the top left corner, and its first row is a header, you can select the whole database without the first line. If your database has four columns (A-D) and five items in it, the table array will be A2:D6, because cells A1-D1 will contain the header.

You can click on the necessary worksheet tab, and select the area with the database. Press Enter and the selected range of cells will be automatically added to the second argument of the VLOOKUP function. Here is an example of a function argument:

`‘database_name’!A2:D6`

In this case, “database_name” is the name of the worksheet tab.

Now you only need to specify what information you want to retrieve and provide the number of the necessary column. 

For example, if you want to retrieve the price of an item from the table at the beginning of this article, you should use the third row, and the “Col_index_num” value will be 3.

## Wrapping Up

Microsoft Excel has a vast variety of functions that can help users deal with different calculations and other tasks. VLOOKUP is a very useful function that can retrieve information that corresponds to a certain value from a database table. 

If you’re new to Excel, you may experience difficulties with this function because it has four arguments.

However, if you follow our guide, you’ll be able to select the right arguments and to use the right formulas. If you use this function a few times in practice, you will quickly understand how it works so you’ll be able to use VLOOKUP whenever you need it.

