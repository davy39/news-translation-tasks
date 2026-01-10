---
title: Excel Absolute Reference – Cell Referencing Example
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-05-16T17:29:50.000Z'
originalURL: https://freecodecamp.org/news/excel-absolute-reference-cell-referencing-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/spreadsheets-24956_1280.png
tags:
- name: data
  slug: data
- name: excel
  slug: excel
- name: spreadsheets
  slug: spreadsheets
seo_title: null
seo_desc: 'In Excel, you can use both absolute and relative cell referencing to make
  calculations.

  Relative referencing is the default. So, for example, whenever you extend a formula
  down some cells, the cells change based on the relationships of the rows and c...'
---

In Excel, you can use both absolute and relative cell referencing to make calculations.

Relative referencing is the default. So, for example, whenever you extend a formula down some cells, the cells change based on the relationships of the rows and columns.

What if you want each cell to lock to a certain formula and not change? That’s where you have to use absolute referencing.

In this article, I will show you how absolute referencing works in Excel. But firstly, you have to know how relative referencing works.

## How Relative Referencing Works in Excel

Relative referencing is the default referencing in Excel. 

When you input a formula into a cell and extend it to other cells, those other cells use the formula as well.

In the illustration below, I calculated how much each footballer earns in a month with relative referencing:
![vid1](https://www.freecodecamp.org/news/content/images/2022/05/vid1.gif)

If you check the formula in each cell, you'll discover that the formula put in cell `D4` (`=D4*4`) has been relatively extended to other cells (`D5` to `D14`). 

So cell `D5` now uses `D5*4`, `D6` now uses `D6*4`, and so on. 

To view formulas in Excel, switch to the formula menu, then click "show formulas":
![ss1-2](https://www.freecodecamp.org/news/content/images/2022/05/ss1-2.png)

That’s how relative referencing works in Excel. 

## Absolute Referencing in Excel

If you don’t want the formula to change when you extend it down through various cells, you'll need to use absolute referencing.

Absolute referencing is done by prepending the rows and columns with a dollar sign. For example ` $D$4`.

If you want only the row fixed, do it like this: ` $D4`.

If you want only the column fixed, do it like this: ` D$4`.

Remember that if you want to make relative referencing, you type the formula ` =D4*4` cell `E4` and extend it to cell `E5`. So the formula becomes ` =D5*4`. 

But if you input the formula as an absolute reference like ` =$D$5*4`, it remains ` =$D$5*4`.

In the example below, I tried to calculate the wages paid with taxes by multiplying the wages with the tax multiplier, but I didn’t get what I wanted:
![vid2](https://www.freecodecamp.org/news/content/images/2022/05/vid2.gif)

That’s because relative referencing is being used. You can confirm this again by checking the formulas:
![ss2-2](https://www.freecodecamp.org/news/content/images/2022/05/ss2-2.png)

You can see the formula changed downward from G8, and anything from G8 downward doesn’t exist in the sheet. 

To fix this, we have to lock the formula to G8 by prepending the row (G) and column (8) with dollar signs. So, the formula becomes `E4*$G$8`, `E5*$G$8`, `E6*$G$8`, and so on.

Now it’s working as intended:
![vid3](https://www.freecodecamp.org/news/content/images/2022/05/vid3.gif)

If you check the formulas, they all remain fixed to `$G$8`:
![ss3-2](https://www.freecodecamp.org/news/content/images/2022/05/ss3-2.png)

## Conclusion

This article showed you how absolute referencing is used in Excel and compared it to another reference type – relative referencing – so you can understand it better.

If you don’t want your formulas to get copied to other cells when you extend them, then you should consider using absolute referencing.

Thank you for reading.


