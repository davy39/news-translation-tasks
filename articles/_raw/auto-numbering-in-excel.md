---
title: Auto-Numbering in Excel – How to Number Cells Automatically
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2021-03-01T15:59:33.000Z'
originalURL: https://freecodecamp.org/news/auto-numbering-in-excel
coverImage: https://cdn-media-2.freecodecamp.org/w1280/6037a8a2a675540a2292367b.jpg
tags:
- name: excel
  slug: excel
- name: how-to
  slug: how-to
- name: Productivity
  slug: productivity
seo_title: null
seo_desc: "Numbering cells is a task often you'll often perform in Excel. But writing\
  \ the number manually in each cell takes a lot of time. \nFortunately, there are\
  \ methods that help you add numbers automatically. And in this article, I'll show\
  \ you two methods o..."
---

Numbering cells is a task often you'll often perform in Excel. But writing the number manually in each cell takes a lot of time. 

Fortunately, there are methods that help you add numbers automatically. And in this article, I'll show you two methods of doing so: the first is a simple method, and the second lets you have dynamically numbered cells. So let's get started.

# How to Auto-Number Cells with a Regular Pattern

For this method, you set your starting number in one cell and the next number in the series in the next cell.

Once you have two adjacent cells filled with your two starting numbers, you can select those two cells, click on the handle in the bottom right corner of the green outline, and drag to select all the cells that you want to follow your pattern. 

A useful tooltip appears near the bottom right corner of the green outline to show what the last number in the series would be if you released at that point.

So, if you want to start with the number 5 and increment by 3 until 38, you would write 5 in your first cell, and 8 in the next cell. You would then select the cells containing the 5 and the 8, click on the handle, and drag to select the other cells until you see `38` appear in the tooltip. Then you can release, and the numbers will be filled in automatically. 

![Image](https://www.freecodecamp.org/news/content/images/2021/02/excel-autonumbering.png)
_1) Select the cells. 2) Drag the handle on the outline (you can also see the tooltip with the last number in the series) 3) Release_

The numbers can also be formatted in descending order: if you start with 7 and then enter 5, the pattern will continue with 3, 1, -1, and so on.

You can also do the same with rows instead of columns. Fill in two consecutive cells in a row with the start of your pattern, then select them and drag the outline horizontally across those cells that you want to continue that pattern. It'll automatically fill in those numbers.

You can also do the same going upward – fill two cells, select them, click the handle and drag upward to fill the cells above your two starting cells.

Note: this will always add numbers that are evenly spaced in the pattern you've started. It won't work with other kinds of number progressions.

# How to Auto-Number Cells Using the ROW() Function

If you have data that can be sorted in different ways (say, a list of names - alphabetically, etc), it's annoying if the numbering of your lines gets scrambled when you're sorting other data. 

To avoid that, you can dynamically number your rows using the `ROW()` function.

In the cell where you want the numbering to start, write `=ROW(A1)`. This will produce the number 1 in the cell. 

Select the cell and drag the outline from the handle in the corner to populate the same formula in the rest of the cells (or, if you are adding the line numbers near a block of data already present, you can just double-click on the handle on the corner of the selection).

![Image](https://www.freecodecamp.org/news/content/images/2021/02/auto-number-row-function.png)
_1) Write `=ROW(A1)` in your first cell, 2) It will appear as the number`1`, 3) Click and drag or double-click to fill all other cells. 4) Now if you sort the data, the line numbers will stay in order._

If you want to have a different regular pattern, you can use a bit of math: to have numbers spaced by 2, you can write `=ROW(A1) * 2` in the first cell, and then proceed with the same steps as above. This will produce the numbers 2, 4, 6...and so on.

If you want to change the starting point of the pattern – to maybe have only odd numbers, for example – you can subtract one: `=ROW(A1) * 2 - 1`, this will produce the numbers 1, 3, 5, 7...

As a general formula, to get any pattern you can write `=ROW(A1) * a + b`.  `a` is used to determine the step, and `b` (it can be either a positive or negative number) is used to change the starting point of the pattern.

If you want to number your columns, you can use the `COLUMN()` function in the same way as the `ROW()`. Just fill in your first cell with `=COLUMN(A1)` , select the cell, then expand the selection to the rest of the cells you want your numbers to be in.

**Note**: if you add or delete rows, you will need to set the auto-numbering again by selecting the first cell and dragging or double-clicking again to restore the pattern.

# Conclusion

Writing numbers in cells is a task often performed in Excel, and here we have seen two simple methods that let us save time. The first method just involves writing numbers in two cells, and then a couple of clicks. And the other just requires writing a formula in one cell, and then a couple of clicks.

There are a few other methods for numbering cells in Excel, but these are the most straightforward.

