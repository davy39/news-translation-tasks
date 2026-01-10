---
title: How to Calculate Percent Change in Excel – Find Increase and Decrease Percentage
subtitle: ''
author: Hillary Nyakundi
co_authors: []
series: null
date: '2021-07-19T15:25:39.000Z'
originalURL: https://freecodecamp.org/news/how-to-calculate-percent-change-in-excel-find-increase-and-decrease-percentage
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/uide-to-writting-a-good-readme-file--1-.png
tags:
- name: excel
  slug: excel
- name: Math
  slug: math
- name: Mathematics
  slug: mathematics
seo_title: null
seo_desc: 'In this article, you''ll learn how to use Excel to calculate percentage
  change, and also how to find the increase and decrease in percentage values.

  Microsoft''s Excel is the most used software when it come performing calculations.
  Various departments ...'
---

In this article, you'll learn how to use Excel to calculate percentage change, and also how to find the increase and decrease in percentage values.

Microsoft's **Excel** is the most used software when it come performing calculations. Various departments in many businesses use it, like accounting, inventory tracking, time logging, and more. 

It has many helpful inbuilt features like formulas and it helps you do accurate calculations.

In this article, we are going to go through how to use Excel to calculate percentage change, and also how to find the increase and decrease in percentage values.

Let's get into it.

## What is Percentage Change?
Percentage change is a concept in math that represents changes that have occurred over time. It is mostly applicable in the field of accounting to compare old changes to new ones.

In order to calculate percentage change in Excel, you'll need to use a formula. It's the formula that that keeps track of different figures being worked on, like balance sheets, product prices, and others.

**Formula syntax**
```excel
percentage change = (NEW - ORIGINAL) / ORIGINAL
```

## How to Calculate Percentage in Excel
Let's take a look at an example to get the understanding of the formula at work.

__Example 1__
If your earnings are $1,250 in May and $1,750 in June, what is the percentage change?

__Solution__
What we are trying to find in this question is the change that was made on the earnings from the month of May to June.

Using our formula:
```
percentage change = (NEW - ORIGINAL) / ORIGINAL

hence:
(1,750 - 1,250) / 1250 = 0.4 or 40%
```

__Example 2__
Now let's take a look at how to do this in excel with a handful of data entries to better understand how Excel functions work:

*STEP 1: Data Entry*.
Below we are presented with n excel workspace with some data, we are expected to calculate the percentage change as indicated in column `D`.
![percentage change](https://www.freecodecamp.org/news/content/images/2022/01/screenshot-nimbus-capture-2021.07.17-07_47_10.png)

*STEP 2: The Formula*.
In this case we will let **A = Actual Price** and **B = Budget Price**, so our formula will be: **A/B-1**. This formula will be entered in cell **D2**.
![formula](https://www.freecodecamp.org/news/content/images/2022/01/screenshot-nimbus-capture-2021.07.17-07_56_07.png)

To execute the formula all we need to do is press *Enter*. We will get our percentage change in decimal values like below:

> If the number you get is positive, like **0.2**, then the percentage increased. If the number is negative, like **-0.2**, then the percentage decreased.

![percentage change](https://www.freecodecamp.org/news/content/images/2022/01/screenshot-nimbus-capture-2021.07.17-08_00_58.png)

*STEP 3: Assigning %*.
In order to assign the `%` sign to our values, we have a couple of options. We can either:
* Right click on the values and select '%', then drag the cursor down to apply changes to other values. Or
* Highlight the whole column '% Change' and select the % sign from the Home menu, under numbers in the work sheet.
![applying %](https://www.freecodecamp.org/news/content/images/2022/01/screenshot-nimbus-capture-2021.07.17-08_07_28.png)

When calculating percentage change in excel, we have two options to work with that is; we are either calculating percentage increase or decrease. Let's take a look on how to work on this: 

## How to Calculate Percentage Increase
In order to calculate percentage increase, you will need to figure out the difference between the two numbers you are comparing meaning you will need the Original details and the Newly added ones.

In this case our formula will be divided into two steps:
```
increase = (NEW - ORIGINAL)
```
The next step will be dividing the increase by the original number and multiplying it by 100 to get the percentage value.
```
percentage increase = Increase ÷ Original Number × 100.
```

If the number you get is negative, like **-0.10**, then the percentage actually decreased rather than increased.

__Example__
Your household bill was $100 in September, but increased to $125 in October. What is the percentage increase from September to October?

__Solution__
Referencing to our formula above, first we will need to get the increased value then convert it into percentage.
```
increase = (NEW - ORIGINAL)

hence:
increase = (125 - 100 = 25)

then:
percentage increase = Increase ÷ Original Number × 100.
% increase = 25 ÷ 100 × 100 
    = 25%
```

As described earlier when calculating percentage change in excel, the same steps will be followed in the case of percentage change.

## How to Calculate Percentage Decrease
The same procedure we applied when calculating percentage increase will be applied here, the only difference will be this time round we will be subtracting the original value from new one. 

__Formula__
```
 Decrease = Original Number - New Number
```
The next step you divide the value you got as a decrease by the original number and multiply by 100 to get the % value.
```
Percentage Decrease = Decrease ÷ Original Number × 100
```

If the number you get is negative, like **-0.10**, then the percentage actually increased rather than decreased.

__Example__
In the previous year, your expenses were $500,000. This year, your expenses were $400,000. What is the percentage decrease of your expenses this year compared to last year?

__Solution__
The first step is for us to get the decreased value, which will easily guide us into getting the percentage value of the same.

```
 Decrease = Original Number - New Number
 
 therefore:
 Decrease = (500,000 - 400,000)
             = 100,000
 
 hence:
 Percentage Decrease = Decrease ÷ Original Number × 100
 % Decrease = 100,000 ÷ 500,000 × 100
             = 20%
```

Perhaps you might wonder how do I go about the same on an excel worksheet? well here is a pictorial representation and working f the same: 
![percentage decrease](https://www.freecodecamp.org/news/content/images/2022/01/Untitled-design-1.png)

There you have it, the above illustrated methods will works no matter what amount of data you have at hand. 

Now when working with softwares you are not always guaranteed success, you are bount to encounter some errors. Below are some of the most ones which you are likely to encounter and how to solve them.

## Common Excel Errors When Using Formulas
* **#DIV/0!**: Occurs if you attempt to divide a number by zero. To solve this problem change the divider into a number that is not zero.
* **#VALUE**: Occurs when cells are left blank, or when a function is expecting a number but you pass it text instead.
* **NUM!**: Occurs when a formula contains invalid numeric values.
* **####**: Occurs when the values are too many to display in the assigned column. The solution is to expand the respective column.
* **#Name?**: If you type wrong values in the formula, like misspelling of a function. To fix it write correct formula names.
* **#REF!**: Occurs when you are referencing cells that are not valid or deleting cells that have been referred to in a formula. To fix this, refers cells correctly.

## Wrap Up
Now, with this knowledge you should be able to work yourself around percentage change calculations. Do you have anybody in mind who might benefit with the knowledge captured here, do share the article with them.

Here is a quick recap of what we have discussed:
* In percentage change calculations we need at-least two values.
* Percentage change can be either a positive or a negative number.
* If the number you get in % decrease is negative then the percentage actually increased rather than decreased.
* If the number you get in % increase is negative, then the percentage actually decreased rather than increased.

Here are a few resources to help you get a better understanding of working with Excel.
* [Microsoft Excel Tutorial for Beginners - Full Course](https://www.youtube.com/watch?v=Vl0H-qTclOg) (*Video tutorial*)
* [Percentage Change Practice Questions](https://corbettmaths.com/wp-content/uploads/2013/02/percentage-change-pdf.pdf)

Happy Coding ❤




