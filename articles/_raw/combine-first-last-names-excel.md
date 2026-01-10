---
title: How to Combine First and Last Name in Excel
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2021-04-21T19:16:31.000Z'
originalURL: https://freecodecamp.org/news/combine-first-last-names-excel
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/article-iamge-combine-first-last-name.png
tags:
- name: excel
  slug: excel
- name: how-to
  slug: how-to
seo_title: null
seo_desc: 'In Excel, you might have a column with first names and a column with last
  names that you want to join. In this tutorial I will explain how you can easily
  accomplish this.

  Let''s say we have the list of first names in column A and the list of last name...'
---

In Excel, you might have a column with first names and a column with last names that you want to join. In this tutorial I will explain how you can easily accomplish this.

Let's say we have the list of first names in column A and the list of last names in column B, and we want to join them in column D. We'll need to use Excel's `CONCAT` function to do this. 

The `CONCAT` function accepts a list or range of text strings and concatenates them (or combines them) to create a new continuous value. So basically it lets you combine the information in the two columns into one new column.

## How to use CONCAT in Excel

In the first cell of column D we write `=CONCAT(A1, " ", B1)`. This is the syntax to create the new string composed of the first name (`A1`), then a space (`" "`), then the last name (`B1`).

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-84.png)

So instead of having "Harry" and "Potter" in two different cells, Excel will give us a new column with "Harry Potter" as we wanted.

If you want to apply this to more than one row, you can then copy this formula and paste it in all the below cells. Or you can click on the green handle in the right bottom corner of the cell and drag it to make the green border surround all cells in which we want this formula to apply. When you release, Excel will apply `CONCAT` to all those cells you've highlighted.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-87.png)

### CONCAT Compatibility Issues

The `CONCAT` function was added in Excel 2016. So if you use a previous version of Excel you need to use `CONCATENATE` instead. 

It has some slight differences, but for this situation you can follow the instructions above and just substitute `CONCATENATE` directly whenever `CONCAT` was used and it'll give you the same results.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-88.png)

## Conclusion

In this tutorial we have learned about the Excel `CONCAT` function along with its predecessor, `CONCATENATE`. We've used this function to join together a list of first names and last names to get a list of full names.

