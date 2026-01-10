---
title: If Function Excel Tutorial – And How to do Multiple If Statements in Excel
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2021-03-26T17:34:46.000Z'
originalURL: https://freecodecamp.org/news/if-function-excel-tutorial-and-how-to-do-multiple-if-statements-in-excel
coverImage: https://cdn-media-2.freecodecamp.org/w1280/604b8922a7946308b768766f.jpg
tags:
- name: data analysis
  slug: data-analysis
- name: excel
  slug: excel
seo_title: null
seo_desc: 'The IF function in Excel is an inestimable ally when we need to implement
  conditional logic, that is when we need different results depending on a condition.

  The syntax is IF(logical_test, [value_if_true], [value_if_false]), where


  logical_test is an...'
---

The `IF` function in Excel is an inestimable ally when we need to implement conditional logic, that is when we need different results depending on a condition.

The syntax is `IF(logical_test, [value_if_true], [value_if_false])`, where

* `logical_test` is an expression that evaluates to `TRUE` or `FALSE`,
* `value_if_true` is an optional argument, and it is what the expression evaluates to in case `logical_test` is true, and 
* `value_if_false` is an optional argument that determines the value in the case that `logical_test` is false.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-39.png)

## How to conditionally set the value of a cell in Excel

Let's see the if statement in action in the simplest use case, when the value of a cell is determined between two options based on the value of a different cell.

For example, let's say that we have a list of projects, the percentage progress on each of them, and we want to automatically set the string to "In progress" or "Finished". Then we can write `IF(B2=100, "Finished", "In progress")` (where `B2` is the first cell with the progress). 

After writing the formula in the first cell we can just double click on the green handle that appears when the cell is selected and the formula will populate to all other cells in the column.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/single-if.png)

## How to use a nested if statement to conditionally set the value of a cell with more options in Excel

Continuing from the example above, we may want to break down the progress status even more. This time we want to have 7 different status strings depending on the progress of the project.

We need to use nested if statements, writing an if statement in place of `value_if_false` (it can be used also in place of `value_if_true` but it becomes messier). 

Let's try to build a formula in case we want to have all these progress statuses: Not Started, Started, First Half, Halfway Through, Second Half, Almost Finished, Finished.

In this case we need a total of 6 if statements, so we could write something like this:

```
=IF(B2=0, "Not started", IF(B2<10, "Started", IF(B2<50, "First Half", IF(B2=50, "Halfway through", IF(B2<90, "Second half", IF(B2<100, "Almost finished", "Finished"))))))
```

Excel allows a max of 7 nested if statements. If we wanted to expand our list of possible statuses, we could add only one more condition and one more status. But fortunately we can add more using a different function.

## How to use `IFS()` for more than 7 conditions in Excel

The `IFS()` function was introduced in Excel 2016, and it allows up to 127 conditions. The syntax is `IFS(logical_test1, value_if_true1, [logical_test2, value_if_true2] ... [logical_test127, value_if_true127])`.

The logical test expressions are evaluated consequentially. When the first one that returns TRUE is found, the corresponding `value_if_true` is given as output.

The previous expression that we wrote with nested if statements can be written like this:

```
=IFS(B2=0, "Not started", B2<10, "Started", B2<50, "First Half"B2=50, "Halfway through", B2<90, "Second half", B2<100, "Almost finished", B2=100, "Finished")
```

## Conclusion

 When you need to set conditionally, you'll often use `IF()`. You can nest multiple `IF()` statements to have complex logic chains. 

But if you need to use more than 7 nested `IF()` statements, then you can use `IFS()` instead.

