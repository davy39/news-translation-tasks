---
title: IF Statement Excel – If Function Examples
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2021-08-16T16:10:37.000Z'
originalURL: https://freecodecamp.org/news/if-statement-excel-if-function-examples
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/pexels-energepiccom-159888.jpg
tags:
- name: data analysis
  slug: data-analysis
- name: excel
  slug: excel
seo_title: null
seo_desc: 'If you are analysing data in Excel and need to set the value of a cell
  conditionally, you can use an IF statement to do so.

  The syntax is IF(logical_test, [value_if_true], [value_if_false]), where:


  logical_test is an expression that evaluates to TRU...'
---

If you are analysing data in Excel and need to set the value of a cell conditionally, you can use an `IF` statement to do so.

The syntax is `IF(logical_test, [value_if_true], [value_if_false])`, where:

* `logical_test` is an expression that evaluates to `TRUE` or `FALSE`,
* `value_if_true` is an optional argument, and it is what the expression evaluates to in case `logical_test` is true, and
* `value_if_false` is an optional argument that determines the value in the case that `logical_test` is false.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-65.png)

# IF Statement Examples

Let's see how we can use the `IF` statement in practice so we can better understand how it works.

## IF Statement Example 1

Let's say that we have a list of students and the scores they got on an exam, like this:

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-60.png)

We want to mark each student as passing or failing on the exam, and we can use an `IF` statement to check if their score is below or above the passing score. A passing score is 60, so if the students received less than 60 that means they failed the exam, otherwise they passed it.

We can write this in excel as `IF(B2<60, "failed", "passed")`, as below.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-63.png)

And then we can just fill that info in to all the cells in the column. We will get this result:

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-62.png)

I've used a bit of [conditional formatting](https://support.microsoft.com/en-us/office/use-conditional-formatting-to-highlight-information-fed60dfa-1d3f-4e13-9ecb-f1951ff89d7f) to make it easier to see the difference between the two results.

## IF Statement Example 2

You can also nest if statements for more complex logic. I've written about how to do that in [this article](https://www.freecodecamp.org/news/if-function-excel-tutorial-and-how-to-do-multiple-if-statements-in-excel/). Let's see it again here with an example in the medical field.

We have the blood test results of a patient, along with the normal range values (which differs based on the patient's sex). Let's use an `IF` statement to check if the blood test results are inside or outside the normal range:

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-68.png)

The normal range for male and female patients are different, so we need to check the patient's sex before knowing which range to use to check the test result. 

We start first by checking `$H$1="male"` (we use the `$` symbol to have this cell fixed when we copy and paste the formula to other cells). Then we use a nested `IF` statement to compare the value from the blood test against the range.

If the patient is male, we use `IF(OR(J2<C2, J2>D2), "ABNORMAL", "normal")`. If the patient is female, we use `IF(OR(J2<C3, J2>D3), "ABNORMAL", "normal")`.

[The `OR` function](https://support.microsoft.com/en-us/office/or-function-7d17ad14-8700-4281-b308-00b131e22af0) returns true if at least one of the arguments is true, and false if none of the arguments are true. In this case we use it to check if the test result is below the lower value of the range or above the upper value of the range. If it is outside the range, we return `ABNORMAL`, and if it's inside the range, we return `normal`.

Put together, the formula looks like this:

`=IF(H$1="male", IF(OR(J2<C2, J2>D2), "ABNORMAL", "normal"), IF(OR(J2<C3, J2>D3), "ABNORMAL", "normal"))`.

For the white blood cell count and platelet count there is no difference based on the patient's sex, so the formula is simpler:

`=IF(OR(J8<C8, J8>D8), "ABNORMAL", "normal")`.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-67.png)

## IF Statement Example 3

In this third example, let's consider what a group of salespeople where able to sell in a certain period.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-69.png)

In this group, if they where able to sell more then the average they get a bonus. So let's check each of their gains against the average with this formula:

`=IF(B2>B$10, "BONUS!", "nope")`

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-72.png)

It seems that four of them will get a bonus for this period!

# Conclusion

If you need to analyse data, then the `IF` statement in Excel is pretty useful. 

We have seen it here in action through three different examples, but what you can do with it is only limited by your creativity. Have fun!

