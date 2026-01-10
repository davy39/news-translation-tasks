---
title: Excel Text Function – How to Convert a Number to Text Format
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2021-07-30T22:22:23.000Z'
originalURL: https://freecodecamp.org/news/excel-text-function-how-to-convert-a-number-to-text-format
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/pexels-pixabay-534216.jpg
tags:
- name: excel
  slug: excel
- name: how-to
  slug: how-to
- name: Tutorial
  slug: tutorial
seo_title: null
seo_desc: "If you want to add a number to a text string, you can't do so directly\
  \ since the format isn't maintained. Also, a number added to a text string doesn't\
  \ have any formatting or all its decimal places. \nThe TEXT function comes in handy\
  \ here, as it allow..."
---

If you want to add a number to a text string, you can't do so directly since the format isn't maintained. Also, a number added to a text string doesn't have any formatting or all its decimal places. 

The `TEXT` function comes in handy here, as it allows you to convert a number to text format with a specific formatting. Then you can add it to another string, and it'll be in the format you want.

## How to Use the `TEXT` Function in Excel

Let's say you have a series of numbers, and you want to write a message including those numbers. 

Let's take a look what happens first without using the TEXT function. First, we'll try to use the `CONCAT` function as `=CONCAT("In ", A2, " there was a profit of ", B2)` and then populate the rest of the column with the same formula.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-108.png)

It doesn't look very good, and the numbers are all different from each other. This is because when we concatenate a number to a string, the format is lost.

So instead, let's use `TEXT` to make a string of the number, and then add it to the string.

`TEXT` takes two arguments: the first one is the number we want to convert to a string, and the second is the format. In this case the format we'll use is `$##,##0.00` (we will see later how to create the format we want).

Let's delete all the content of column C and title it instead `Profit in string format`. We'll write in C2 `=TEXT(B2, "`$##,##0.00`")`, and then expand it to the rest of the column.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-109.png)

If you create the string again using the number in string format, this time the numbers stay in the format you want.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-110.png)

## How to Use Different Number Formats in Excel

We just saw how to use one specific format, `$##,##0.00`. Now let's see what the characters mean so you can use the number format you wish. Also note that the decimal numbers are rounded when the format shows fewer decimal places than what the numbers have.

### How to Format Numbers as Decimals

The `0` is for a number that must be there – if the converted number does not have enough places, there will be a `0`. You can use this to decide how many decimal places, trailing `0`s, or leading `0`s to show. 

For example the number `12345.6` with a format of `000000` will be shown as `012345` with a leading `0`. But if it's formatted as `0.00`, it will be shown as `12345.60` with a trailing `0`.

The `#` is for a number that could be there but also could not be. You can use it, for example, to show how many decimal numbers to show max. 

For example `12345.6` formatted as `0.###` will be shown as `12345.6`. But `12345` will be shown as `12345.`, and `12345.6789` will be shown as `12345.679`, as the format is for a max of 3 decimal places.

You can add other characters at the beginning, in the middle, or at the end. You can add any characters except `,`, `.`, `?`, `0`, and `#`. The comma acts as the thousands separator, the dot is a decimal separator, and the last three symbols have special meaning in the formatting (for example, the `?` is used in fractions, see below).

Here are a few examples:

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-119.png)

### How to Format Numbers as Fractions

You can also format numbers as fractions. In the fraction format, you can indicate how many digits the denominator should have (or specify a denominator). You can also specify if the whole part has to be written inside the fraction or separated.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-115.png)

To specify the number of digits in the denominator of the fraction, you can use the `?` character. You use as many in the denominator as the number of digits you want there.

So for example `?/?` is for one digit in the denominator, `??/??` is for two digits, and so on (note that you get the same result with `?/??` or with `??/??`).

To specify which number has to be the denominator you can write it into the format. So if you want a fraction in ninteenths, you can write `??/19`.

To separate the whole part from the fraction you can write a `#` in front of it separated by a space, so `# ??/19` or `# ???/???`. And if you want the whole part always visible even if it's zero, you can write `0 ??/19` or `0 ???/???` instead.

## Conclusion

Adding numbers inside strings is often useful in writing reports. But if you want to keep the number in a specific format, you need to use the `TEXT` function. 

In this article you have learned how to format a number as an integer, as a number with decimal places, or as a fraction.

