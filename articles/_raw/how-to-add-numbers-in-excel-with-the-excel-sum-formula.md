---
title: AutoSum Excel – How to Add Numbers with the Sum Formula
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2021-03-02T23:48:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-numbers-in-excel-with-the-excel-sum-formula
coverImage: https://cdn-media-2.freecodecamp.org/w1280/6037ad25a675540a229236b5.jpg
tags:
- name: excel
  slug: excel
- name: Productivity
  slug: productivity
- name: spreadsheets
  slug: spreadsheets
seo_title: null
seo_desc: 'The SUM() formula in Excel is used to add together the content of two or
  more cells. It takes the cell names and gives back the result of the sum.

  Let''s apply the SUM formula so we can see it in action. Say that you''re organizing
  a party, and differe...'
---

The `SUM()` formula in Excel is used to add together the content of two or more cells. It takes the cell names and gives back the result of the sum.

Let's apply the `SUM` formula so we can see it in action. Say that you're organizing a party, and different people are bringing balloons in different colors. You'll record in a table how many balloons of each color each person brings.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-181.png)

## How to add the cells in a column

First, we want to know how many balloons of each color people have brought to the party. 

So based on the table above, to find out how many blue balloons we have, we can write the `SUM` formula in cell `C6`. Then we'll write the cells we want to add together as `C3:C5`, which will be interpreted as "all the cells from `C3` to `C5`". So we'll have `=SUM(C3:C5)`.

We can do the same thing for the green and white balloons, too - we'll write cells `D3:D5` for green and `E3:E5` for white.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/sum-columns-colored.png)

## How to add the cells in a row

Next, we want to know how many balloons each person has brought. To find out how many balloons Marisa brought, we can write the `SUM` formula in the `F3` cell, and write the cells we want to add together as `C3:E3`. This will be interpreted as "all the cells from `C3` to `E3`", which gives us `=SUM(C3:E3)`.

Similarly, for Oliver's balloons, we write the cells `C4:E4` and for Alex's balloons `C5:E5`.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/sum-rows-colored.png)

## How to add the cells in a block

The last thing we want to learn how to do is to figure out how many balloons we have in total. 

To do that we need to sum all the balloons we have. We write the block of cells as `C3:E5`, which will select all the cells in the rectangle with `C3` in the upper left corner and `E5` in the bottom right corner.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/sum-block-coloured.png)

## How to add the cells in different intervals

If we want to know the sum of different intervals of data that are not near each other (for example how many blue and white balloons we have in total), we can use the `SUM` formula separating data intervals with commas. 

So since `C3:C5` is the interval for the blue balloons, and `E3:E5` is the interval for white balloons, we can write `=SUM(C3:C5,E3:E5)`. Also, as we already know how many blue balloons we have in total and how many white balloons we have in total, we can sum the two totals with `=SUM(C6,E6)`. 

![Image](https://www.freecodecamp.org/news/content/images/2021/02/sum-intervals-colored.png)

## How to add cells by selecting the data with the mouse

Up to this point we have typed out the names of the cells to select them. But Excel also lets you select the cells to use in the formula with the mouse. 

Once you have written `=SUM(` then you can select the cells – if you want to select multiple intervals, you can just keep `Ctrl` pressed. Once you have finished, you can press `Enter` and the sum of the selected cells will be calculated.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-182.png)

## How to add cells using AutoSum

There is a tool in Excel that lets you make simple sums with a click, called AutoSum. You can find it in the Home menu, and it has the symbol of a greek uppercase letter sigma (Σ). 

With this tool you can, from the situation in the first image before any calculation was done, select the three cells `F3`, `F4` and `F5`, press the AutoSum button, and it will immediately fill the cells with the sums of the cells to the left (the same result as we got when we added the cells in a row). 

You can also select the three cells `C6`, `D6` and `E6` and press AutoSum to get the sums of the cells above (the same result as when we added cells together in a column).

![Image](https://www.freecodecamp.org/news/content/images/2021/02/autosum.png)

Alternatively, the AutoSum tool can be used as a shortcut to writing the `SUM` formula: when you select only one cell and press the AutoSum button, the cell is filled with the `SUM` formula. Then you can select the cells to sum with the mouse or write the interval of the cells to sum inside the parenthesis of the formula. 

If the selected cell is near other filled cells the `SUM` formula can be pre-filled with a suggestion of cells to sum.

## Wrapping up

The `SUM()` formula lets you add together cells. In order to determine which cells to sum, you can type their names as argument of the `SUM`() formula, or you can select them with your mouse after you've typed the name of the formula and the opening parenthesis. The formula can also be used with the AutoSum tool.

