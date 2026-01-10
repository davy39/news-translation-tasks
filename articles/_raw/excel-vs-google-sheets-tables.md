---
title: How to Work with Tables in Excel vs Google Sheets
subtitle: ''
author: Eamonn Cottrell
co_authors: []
series: null
date: '2024-07-02T17:27:11.000Z'
originalURL: https://freecodecamp.org/news/excel-vs-google-sheets-tables
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/4.jpg
tags:
- name: excel
  slug: excel
- name: google sheets
  slug: google-sheets
- name: spreadsheets
  slug: spreadsheets
seo_title: null
seo_desc: 'Google Sheets recently released an all new feature: tables.

  Well, new is a bit of an overstatement. Excel has had proper tables for many, many
  years, and it''s been a point of contention in the spreadsheet community.

  In this article, I''ll break down w...'
---

Google Sheets recently released an all new feature: tables.

Well, _new_ is a bit of an overstatement. Excel has had proper tables for many, many years, and it's been a point of contention in the spreadsheet community.

In this article, I'll break down what exactly tables are, why they're important, and then see how Google Sheet's new tables stack up against Microsoft Excel's.

Here is a video walkthrough of everything we'll cover:

%[https://youtu.be/vBp5mveYZZ4]

## What's a Table?

A table is a way of structuring and formatting data in a spreadsheet. It groups together rows and columns of data so that they can be more easily filtered, grouped, and analyzed.

Many people would look at the following bit of data and wrongly assume that it's already in a table.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/image-103.png)
_Data in Excel_

This is merely well organized rows and columns of data in Excel. Each column is a separate category of information, that is ids, names, emails, job titles, and salaries.

Each row represents one entry of that data. So, you'd put your id, name, email, job title and salary going left to right in a row.

Simple, yes?

A table contains all the same data, but by formatting it as a table we can unlock a whole lot of additional functionality.

The first of which is the appearance itself. When we create a table, Excel immediately colors our data with a dark header row and bands of alternating colors.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/image-104.png)
_Table in Excel_

Sheets does the same thing, as we can see below.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/image-105.png)
_Table in Google Sheets_

So, a table is simply a way of managing and grouping data more easily. But it goes much further than just formatting, as we'll see.

## Why are Tables Important?

Tables help reduce errors. When dealing with data, we are always making sure the data is clean and that we don't have errors in our formulas. 

Tables help keep things orderly simply by being structured and formatted well. But as we'll see in the formula section in a moment, they also allow us to reduce errors in formulas by dynamically calculating things for us

## How to Create a Table in Excel and Sheets

In Microsoft Excel, creating a table is as easy as clicking anywhere in the data range and pressing `CTRL + T`. Immediately, Excel will predict the data range for the table and ask you to confirm this.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/image-106.png)
_Excel table data range_

Alternatively, you can find the same create table option from the Insert Menu in the Ribbon at the top.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/table.png)
_Excel insert menu_

Over in Sheets, you'll need to either right click in a cell in the data range, or select the option from the Format menu to Convert to Table.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/sheets.png)
_Convert to table options in Google Sheets_

One caveat in Sheets: if you right click in a cell, you have to select the whole data range for it to convert to a table. Whereas, if you select Format - Convert to table from the menu, it is (like Excel) smart enough to predict the whole data range.

A small thing. But Excel takes the prize for ease of creation.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/right-click.png)
_Convert to table in Google Sheets_

**⭐Winner: EXCEL**

## How to Format Tables in Excel and Sheets

As we saw initially, some formatting is done as soon as we create a table.

From here, though, both programs allow for further customization.

In Sheets, we can select the dropdown in the top left next to the table name to access a few options immediately. For the most part, we can simply change the alternating colors of the table.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/sheets-format.png)
_Formatting options in Google Sheets_

If we select Custom, it opens up the full alternating colors menu that is also accessible through the Format menu. This gives us more control over the colors, but it's all aesthetic.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/image-110.png)
_Alternating colors menu in Google Sheets_

Meanwhile in Excel, we have the same options with a few more toggle selections for styling. For instance, we can check the first column to bold the text in the id column or we toggle between banded columns and/or rows.

And on the far right of the Table Design tab in the Ribbon, there are a ton of prebuilt styles that we can toggle on and off.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/format-excel.png)
_Table design in Excel_

Both programs give plenty of options here, and this is mostly to make the tables look good. But Excel comes out on top with more options.

**⭐Winner: EXCEL**

## How to Sort Tables in Excel and Google Sheets

In both programs, there is a dropdown toggle button in each of the header row's cells. Selecting this in Excel allows us to sort ascending or descending...or even by color.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/sort.png)
_sort in excel_

For instance, if we have some of our data using a blue font color, we can actually sort it by that color:

![Image](https://www.freecodecamp.org/news/content/images/2024/06/sort-color.png)
_Sort by color in Excel_

What about Google Sheets? Yep, same deal there. It will also detect when different colors are used and allow you to do the same type of sorting.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/sheets-sorting-options-1.png)
_Sort by color in Sheets_

Excel does have a Custom Sorting dialog box that can drill down into more detail. For instance, you can add levels of sorting.

Using our color example, we can first sort by the blue font colors in the email color and then by the red font colors in the job title column.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/double-sort.png)
_Multiple column sorting in Excel_

Google Sheets can do the same thing, but not from the header drop downs. The header drop down sorting is restricted to one row at a time in Sheets.

But, if you select the entire table's data range and then `Data - Sort Range - Advanced range sorting options`, you are able to sort by multiple columns in Google Sheets.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/advanced-sort-google-sheets.png)
_Advanced sorting in Google Sheets_

Sheets' advanced sorting is not as powerful as Excel's, though. You are only able to sort ascending or descending by value. Excel takes the cake on this one by a hair.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/google-sheets-muiltiple-row-sorting.png)

**⭐Winner: EXCEL**

## How to Filter Tables in Excel and Google Sheets

Filtering works exactly the same as sorting. In both programs, click the dropdown selector in the header row to see the options for filtering.

In both programs, we have the same options. We can filter by color just like in our sorting. We can filter by values by either selecting all, none, or individual values. And we can filter by condition.

Here's Google Sheet's menu:

![Image](https://www.freecodecamp.org/news/content/images/2024/06/image-113.png)
_Filtering in Google Sheets_

And here's Excel's menu. All the same options are available. Both programs allow for custom filter formulas to be entered as well.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/image-112.png)
_Filtering in Excel_

**⭐Winner: TIE**

## How to Use Tables in Formulas in Excel and Google Sheets

One of the big reasons to use tables lies in formulas. Whether you use Excel or Sheets, you are likely taking advantage of built-in functions and the ability to create custom formulas for analyzing your data.

By holding your data in a table, your formulas can reference that data dynamically.

Meaning, if you add rows of data to your table, any formulas referencing those table values will update automatically.

The risk of breaking things by adding data decreases dramatically with the use of tables.

Here's a simple example. If we wanted to combine the first and last names into one cell, we could concatenate them with this formula `=Salary[first_name]&" "&Salary[last_name]`.

In Excel, we reference a table by its name, in this case, `Salary`. Then within brackets, we reference a column name, `[last_name]`.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/image-115.png)
_Spill formula in Excel_

We can do the exact same in Sheets.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/image-116.png)
_Formula referencing in Sheets_

There's one powerful difference, though. In Excel, the formula will spill down. Meaning, we only have to write it once at the very top, but because it sees that we're referencing values in a table, it will spill down to every row in the table.

In Google Sheets, we still have to drag the formula down.

Now, sometimes, we may not want things to spill down. In this case we can use different syntax in Excel. Instead of the column name within brackets, we can add an @ sign and another set of brackets. This tells Excel to only make the calculation on one row: 

![Image](https://www.freecodecamp.org/news/content/images/2024/06/image-117.png)
_Formula referencing in Excel_

Excel flexes on this one. It's much more powerful to use tables in formulas in Excel than in Sheets.

**⭐Winner: EXCEL**

## How to Change Table Range in Excel and Google Sheets

What if we want to extend our table or remove data from it? Both Google Sheets and Excel allow us to do this easily.

Say we want to add a column for the full name of a person. In both programs, if we simply type in `full_name` in G1 to the right of our last column, that column will become a part of the table's data range.

Anytime we type in an adjacent column or row to our table data, the programs will assume the table needs to extend to include it.

Then, we can use a version of the formula from our previous example to insert the full names. Now that we are inside of the table, though, it's not necessary to include the title of the table in our formula.

Now, all that's needed in Excel is `=[@[first_name]]&" "&[@[last_name]]`.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/image-119.png)
_Reference table columns in Excel_

For Google Sheets, it's the same inside the table as outside it: `=Table2[first]&" "&Table2[last]`. Sheets also requires us to drag the formula down. It does not handle spilling like Excel (yet).

![Image](https://www.freecodecamp.org/news/content/images/2024/06/image-118.png)
_Reference table columns in Sheets_

To add columns within a table, we can right click the column name and select insert.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/image-120.png)
_Insert column in Excel_

Google has a slight edge here in that you can select whether to insert to the left or the right, whereby Excel only inserts to the left.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/image-121.png)
_Insert column Google Sheets_

Inserting rows is exactly the same. Excel allows for inserting rows above, while Sheets allows you to select above or below.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/image-122.png)
_Inserting rows Google Sheets_

In both programs, deleting rows and columns is as simple as selecting the row(s) or column(s), right clicking, and selecting delete.

In Excel you have the added benefit of a keyboard shortcut. `CTRL + -` will delete the selected rows or columns.

Both programs will also allow you to convert a table back to a regular data range. In Excel, it's the `Convert to Range` button in the `Table Design` tab of the menu

![Image](https://www.freecodecamp.org/news/content/images/2024/07/convert.png)
_Convert to Range option in Excel_

And in Google Sheets, it's the `Revert to unformatted data` option from the table dropdown menu.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/revert.png)
_Revert to unformatted data option in Sheets_

**⭐Winner: TIE**

## How to Add a Total Row in a Table

There's a good chance you'll want to total up the amounts in a column. How easy is this to add in a table?

You can do it in both programs, but...

Excel makes it incredibly easy. There's a toggle option for this in the Table Design menu in the Ribbon. Toggle this on, and a Total row is automatically included and calculated at the bottom.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/total-row.png)
_Total row in Excel_

Can you do the same in Sheets? 

Yes, you've just got to do it yourself.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/image-124.png)
_Total row in Sheets_

**⭐Winner: EXCEL**

## Who Wins?

Well, it's no surprise that Excel comes out on top. Sheets users (myself included) have a lot to be excited about with the ability to finally create proper tables. By and large, the functionality is just as powerful as Excel. 

And much like many features compared between the two programs, Sheets can probably get the job done for most use cases.

Excel, as per normal, simply does more and does it a little bit better.

I'm Eamonn, and I'll help you **get good at spreadsheets**. Join my free newsletter, [Got Sheet, here](https://www.gotsheet.xyz/subscribe).

