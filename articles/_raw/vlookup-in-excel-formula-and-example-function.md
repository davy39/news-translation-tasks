---
title: VLOOKUP in Excel – Formula and Example Function
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-10-05T16:26:42.000Z'
originalURL: https://freecodecamp.org/news/vlookup-in-excel-formula-and-example-function
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/vlookup.png
tags:
- name: data analysis
  slug: data-analysis
- name: excel
  slug: excel
- name: spreadsheets
  slug: spreadsheets
seo_title: null
seo_desc: "In Excel, VLOOKUP() means vertical lookup. It is a powerful built-in function\
  \ you can use to quickly search for a value in a spreadsheet. \nVLOOKUP() searches\
  \ for a value in a vertical manner across the sheet – unlike the HLOOKUP() function\
  \ which does..."
---

In Excel, `VLOOKUP()` means vertical lookup. It is a powerful built-in function you can use to quickly search for a value in a spreadsheet. 

`VLOOKUP()` searches for a value in a vertical manner across the sheet – unlike the `HLOOKUP()` function which does it horizontally.

Before using `VLOOKUP()`, make sure every row in your worksheet has an ID. The IDs must also be arranged in ascending order. This makes sure Excel is not confused during the process of returning a value from a search.

In this article, I will show you how to use the `VLOOKUP()` function by explaining the values you should put in the function. We'll also look at two different examples.	

## The `VLOOKUP()` Formula and its Values
In Excel, you do almost everything with a formula – and `VLOOKUP()` is not an exception. 

Below are the values that the `VLOOKUP()` function takes:

`VLOOKUP(lookup_value, table_array, column_index_num, [range_lookup])`

- lookup_value: the cell that has the value you want to search for. It’s always on the left. For example, A5.
- table_array: the location where you think the value is and where you want Excel to search for the value. For example, A1:D10
- column_index_num: the column where the value is located. For instance, 4
- [range_lookup]: You can only specify TRUE or FALSE for this. TRUE means approximate match and FALSE means exact match.

## How to Use `VLOOKUP()` in Excel
To use `VLOOKUP()` to search for some value in Excel, you need to use the formula and enter the individual values discussed in the previous section.

To show you how to use `VLOOKUP`, I’ll be using the table below. It’s a table showing some fictional footballers (soccer players), their ages, clubs, and career goals scored.

![ss1-1](https://www.freecodecamp.org/news/content/images/2022/10/ss1-1.png) 

### `VLOOKUP()` Example 1
In the table, I want to see the number of career goals scored by Kat Katongo (`A5`). We can use VLOOKUP() in this case. This example does not require an ID for all the entries.

**Step 1**: Type a representative name in an empty cell:
![ss2-1](https://www.freecodecamp.org/news/content/images/2022/10/ss2-1.png) 

**Step 2**: It makes sense to put the career goals right in front of the rep cell, so I’ll highlight the cell:
![ss3-1](https://www.freecodecamp.org/news/content/images/2022/10/ss3-1.png) 

**Step 3**: Enter the formula in the formula bar:
![ss4-1](https://www.freecodecamp.org/news/content/images/2022/10/ss4-1.png)

The formula I’m using is `=VLOOKUP(A5, A1:D10, 4, FALSE)`:
![ss5-1](https://www.freecodecamp.org/news/content/images/2022/10/ss5-1.png) 

- A5 is the lookup_value
- A1:D10 is the table_array
- 4 is the column_index_num – because that’s the column for the career goals 
- FALSE is the [range_lookup] because I want an exact match.

And boom! 180 appears in the cell:
![ss6-1](https://www.freecodecamp.org/news/content/images/2022/10/ss6-1.png) 

To make things clearer for you, the GIF below shows how I entered the formula:
![vlookup1](https://www.freecodecamp.org/news/content/images/2022/10/vlookup1.gif) 

### `VLOOKUP()` Example 2

In this example, I want to just enter an ID and see the career goals of the player. This means I need to assign an ID to the individual footballers.
![ss7](https://www.freecodecamp.org/news/content/images/2022/10/ss7.png) 

**Step 1**: Now, I want to start by looking up the career goals of the player with an ID of 9. So, I prepare some more entries on the right.
![ss8](https://www.freecodecamp.org/news/content/images/2022/10/ss8.png) 

**Step 2**: To look up the career goals of the player with an ID of 9 (Baba Ali), I’ll select the cell I want it to show in and click the formula tab. Once I do that, a prompt will show up.
![ss9](https://www.freecodecamp.org/news/content/images/2022/10/ss9.png) 

**Step 3**: Select `VLOOKUP` and click OK. If you don’t see `VLOOKUP()` there, search for it and select it.
![ss10](https://www.freecodecamp.org/news/content/images/2022/10/ss10.png)

**Step 4**: Another popup showing the inputes to enter the values of the formula will show up:
![ss11](https://www.freecodecamp.org/news/content/images/2022/10/ss11.png)

**Step 5**: Enter the values one by one:
![ss12](https://www.freecodecamp.org/news/content/images/2022/10/ss12.png) 

-  I’ve entered `I3` for the lookup value because that’s where I put the ID of 9
- `A1:E10` for the table array because that’s the area I want to lookup
- `5` for the column index because that’s the column containing the career goals of the players
- and `FALSE` as the range_lookup because I want an exact match

When I pressed `OK`, the career goals of Baba Ali (the player with ID 9) shows up:
![ss13](https://www.freecodecamp.org/news/content/images/2022/10/ss13.png) 

To make things clearer to you, this is how I entered the formula:
![vlookup2](https://www.freecodecamp.org/news/content/images/2022/10/vlookup2.gif) 

Any time I change the ID and press `ENTER`, the career goals of the player with that ID shows up:
![vlookup3](https://www.freecodecamp.org/news/content/images/2022/10/vlookup3.gif) 

## Conclusion
`VLOOKUP()` is a powerful Excel function that can help you search for any value in a worksheet – whether small or large. That’s why I wrote this article to help you get started with it.

If you find this article helpful, kindly share it so it can get to others.

Thank you for reading.


