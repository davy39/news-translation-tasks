---
title: Concatenate in Excel – How to Use the Concat Function
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2022-05-12T19:26:13.000Z'
originalURL: https://freecodecamp.org/news/concatenate-in-excel-how-to-use-the-concat-function
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/pexels-yan-krukov-7693224.jpg
tags:
- name: excel
  slug: excel
- name: spreadsheets
  slug: spreadsheets
seo_title: null
seo_desc: 'Excel has many useful functions that you can use to work with your data.

  In this guide you will learn about the CONCAT function and how to use it.

  Concatenation just means to join two things together. And in Excel, you can use
  the CONCAT function to ...'
---

Excel has many useful functions that you can use to work with your data.

In this guide you will learn about the `CONCAT` function and how to use it.

Concatenation just means to join two things together. And in Excel, you can use the `CONCAT` function to join data from multiple cells into one cell. Let's see how it works.

## Syntax of the CONCAT function

The general syntax of the CONCAT function is:

```text
=CONCAT(text1; [text2; ...])
```

Where the arguments are:

* `text1` is a required argument that can be a string or an array of strings (like a range of cells).
* `[text2, ...]` identifies the optional arguments that follow. There can be up to 253 text arguments, and each one can also be a string or an array of strings (such as a range of cells).

## How to use the CONCAT function in Excel

To use the CONCAT function, you will need to click on the cell in which you want the result to appear, and type `=CONCAT(` there. 

After that you can click on the cells, or range of cells, you want to concatenate (or join) together – you will need to keep the Ctrl button pressed to add multiple arguments.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-67.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-68.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-69.png)

Like you can see in these screenshots, we are writing `=CONCAT(` in the cell D1 and then clicking on the cells A1 and B1 while keeping Ctrl pressed. After that, pressing Enter will give the result in the cell D1.

If you want to add text in between the different cells' content, for example a space, you can click on a cell, then type a semicolon and the text you want to add in between quotes, then another semicolon, and finally click on the next cell:

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-70.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-71.png)

In this case you would write `=CONCAT(` in cell D1, then click on cell A1, type a semicolon, then type the space surrounded by strings, `" "`, followed by another semicolon, and finally click on cell B1. This will result in "Leonardo da Vinci" in cell D1.

**Note:** You can concatenate together up to 32,767 characters, which is the cell limit. If the resulting string is longer than 32,767 characters the function will output a `#VALUE!` error.

## Examples

The [official Microsoft documentation](https://support.microsoft.com/en-us/office/concat-function-9b1a9a3f-94ff-41af-9736-694cbd6b4ca2) has three helpful examples of how to use the `CONCAT` function. Let's examine them.

### CONCAT Example 1:

| =CONCAT(B:B; C:C) | A's | B's |
| ---  | --- | --- |
| | a1 | b1 |
| | a2 | b2 |
| | a4 | b4 |
| | a5 | b5 |
| | a6 | b6 |
| | a7 | b7 |

If you want to follow along, copy this table and paste its data in cell A1 of a new Excel sheet.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-75.png)

This function allows for whole column reference, so in the formula `=CONCAT(B:B; C:C)` you are concatenating the whole column B (`B:B`) followed by the whole column C (`C:C`), so the result is `A'sa1a2a4a5a6a7B'sb1b2b4b5b6b7` – the empty cells do not contribute to the end result.

### CONCAT Example 2:

| =CONCAT(B2:C8)	| A's	| B's |
| --- | --- | --- |
| |a1|	b1|
||	a2|	b2|
||	a4|	b4|
||a5|	b5|
||	a6|	b6|
||a7|	b7|


To follow along, copy this table, and paste it in the A1 cell of an empty Excel sheet.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-76.png)

In this case, it is the cells in the range `B2:C8` (the range highlighted in the picture) that are being concatenated together, and the formula in the A1 cell will result in `a1b1a2b2a4b4a5b5a6b6a7b7`. Also in this case the empty cells do not contribute to the result.

**Note:** The cells in a range are read row by row, so the cells are concatenated in the order: `B2;C2;B3;C3;B4;C4;B5;C5;B6;C6;B7;C7;B8;C8` (with B8 and C8 being empty, so not contributing to the end result).

### CONCAT Example 3

This example has various examples in it, all with the general theme of joining cells with other text. This example illustrates well how you can do a lot of things with the Concat function.

Let's take a look.

| Data | First Name | Last name |
| --- | --- | --- |
| brook trout | Andreas | Hauser |
| species | Fourth | Pine |
| 32 | | |	
| **Formula** | **Description** | **Result** |
| `=CONCAT("Stream population for "; A2;" "; A3; " is "; A4; "/mile.")` | Creates a sentence by joining the data in column A with other text. | Stream population for brook trout species is 32/mile. |
| `=CONCAT(B2;" "; C2)` | Joins three things: the string in cell B2, a space character, and the value in cell C2. | Andreas Hauser |
| `=CONCAT(C2; ", "; B2)` | Joins three things: the string in cell C2, a string with a comma and a space character, and the value in cell B2. | Hauser, Andreas |
| `=CONCAT(B3; " & "; C3)` | Joins three things: the string in cell B3, a string consisting of a space with ampersand and another space, and the value in cell C3. | Fourth & Pine |
| `=B3 & " & " & C3` | Joins the same items as the previous example, but by using the ampersand (&) calculation operator instead of the CONCAT function. | Fourth & Pine |


To follow along you can also copy this table in the A1 cell of an empty Excel sheet.

#### Stream population for brook trout species is 32/mile.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-77.png)

The first formula shown in this example joins together the text of three cells (A2, A3 and A4) with a few strings to form a longer sentence.

So, the result is given by the combination of the string `"Stream population for "` with the content of the cell A2, so `"brook trout"`, which is then followed by a space (`" "`), the content of cell A3 (`"species"`), the string `" is "`, the content of cell A4 (`32`), and finally, the string `"/mile."`. 

All together it results in the string `"Stream population for brook trout species is 32/mile."`.

(For the following screenshots I have hidden the rows of the formulas I have already talked about).

#### Andreas Hauser

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-78.png)

In this example, the formula `=CONCAT(B2; " "; C2)` joins together the string from the cell B2, a space `" "` and the string from the cell C2, resulting in `"Andreas Hauser"`.

#### Hauser, Andreas

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-79.png)

From this example you can see that the order in which the cells are written in the `CONCAT` function arguments matter. The formula `=CONCAT(C2; ", "; B2)` joins together the strings from cell C2, a comma and a space `", "` and from cell B2, resulting in `"Hauser, Andreas"`. 

The strings from cells C2 and B2 have been joined in a different order because they have been written in a different order in the arguments of the method.

#### Fourth & Pine

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-80.png)

You can join together any kind of screen. See here where the formula `=CONCAT(B3; " & "; C3)` joins the string from cell B3 with the string from cell C3 putting in the middle of the two the string with a space, an ampersand and another space, `" & "` resulting in `"Fourth & Pine"`. 

#### Fourth & Pine (II)

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-81.png)

This example shows an alternative method of concatenating strings: using the operator `&` you can write the list of strings you want to join separated by an ampersand (`&`). So `=B3 & " & " & C3` gives the same result as `=CONCAT(B3; " & "; C3)`.

**Note:** You can use the `&` operator only for single cells, it doesn't work for ranges.

And that's it! Now you know how to use the `CONCAT` function in Excel. Thanks for reading!

