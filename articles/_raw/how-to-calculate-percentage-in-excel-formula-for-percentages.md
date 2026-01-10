---
title: How to Calculate Percentage in Excel – Formula for Percentages
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2022-08-18T17:44:39.000Z'
originalURL: https://freecodecamp.org/news/how-to-calculate-percentage-in-excel-formula-for-percentages
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/victoria-strukovskaya-OhL_qEqpef4-unsplash-1.jpg
tags:
- name: excel
  slug: excel
- name: Math
  slug: math
- name: Mathematics
  slug: mathematics
- name: MathJax
  slug: mathjax
seo_title: null
seo_desc: 'A percentage is a kind of fraction saying how many parts over 100 something
  is. In this article you will see in detail what a percentage is, and how to calculate
  a percentage in Excel.

  First, before diving into how it works in Excel, let''s take a loo...'
---

A percentage is a kind of fraction saying how many parts over 100 something is. In this article you will see in detail what a percentage is, and how to calculate a percentage in Excel.

First, before diving into how it works in Excel, let's take a look at the math.

If you want to jump directly to the Excel part, and avoid the math part, please proceed to the section [How to work with percentages in Excel](#heading-how-to-work-with-percentages-in-excel).

## What is the Formula for Calculating a Percentage?

Percentages from 0% to 100% are equivalent to decimal values from 0 to 1. That means you can convert from a percentage to a decimal number. Let's see how.

### How to Convert from Decimal Number to Percentage

You can convert from a decimal number to a percentage in the following way:

* take the decimal number, \(d\),
* multiply it by \(100\),
* and then add the percentage \(\%\) symbol,

In short, if you want to get a percentage from a number \(d\) you can do this:

$$ ( d \cdot 100 ) \% $$

### How to Convert from a Percentage to a Decimal Number

If you want to convert from a percentage to a number, you can:

* take the percentage \(P\%\),
* remove the percentage symbol, \(P\)
* then divide the number by \(100\): \(\frac{P}{100}\)

In short, to convert a percentage \(P\%\) to a decimal number:

$$ \frac{P\xcancel{\%}}{100} $$

### How to Calculate the Percentage of a Number

There are three cases in which you might want to calculate the percentage of a number:

* to add a percentage to the number (like for calculating how much you have to pay including VAT)
* to just get the percentage of the number
* to subtract a percentage from the number (like for a sale)

#### How to add a percentage to a number

Let's first use a specific case, and then let's generalise.

You went shopping, and the total you need to pay is $185 + VAT. Let's say VAT in this case is 17%.

So you would have to calculate 17% of $185 and then add it to $185.

$$ \$185  \cdot 17 \% + \$185 $$

You can make it a single operation if instead you multiply by \( 117 \% \).

$$ \$185 \cdot ( 100\% + 17\% ) = \$185 \cdot 117\% $$

If you have a simple calculator that doesn't have a percentage operator, you can convert the percentage to a decimal number as we discussed above. Here's what that would look like:

$$ \$185 \cdot 117\% = \$185 \cdot \frac{117 \xcancel{ \% }}{ 100 } = \$185 \cdot 1.17 $$

So, in general, if you want to add a percentage \( P \% \) to a number \( n \) you can do this:

$$ n \cdot ( 100\% + P\%) $$

Or if instead you have the percentage in the decimal number form \( d \) you can do this:

$$ n \cdot (1 + d) $$

#### How to calculate the percentage of a number

If you want to buy a house you need to pay a deposit on the house. Let's say that's 15% of the total value of the house.

If the house price is $200,000, how can you calculate it?

You can multiply the price by the percent number to get the percentage.

$$ \$200,000 \cdot 15 \% = \$30,000 $$

So if you want to know what's the percentage \(P\%\) or fraction \(d\) of a number \(m\), you can multiply that number by the percentage or fraction.

$$ m \cdot P\% \newline \, \\ m \cdot d $$

#### How to subtract a percentage from a number

This case is common for calculating the price of an item on sale. For example, if something has an original price of $999 and it is on sale for 20% less, you can calculate the the final price by figuring out what is 20% of $999. Well, it's $199.80, so then you just subtract that value from $999.

The final price of the item on sale is $799.20.

You can calculate it in a single step if you multiply the original price by \((100\% - 20\%)\) or \(80\%\):

$$ \$999 \cdot (100\% - 20\%) = \$999 \cdot 80\% = \$779.20 $$

So the general formula to subtract a percentage \(P\%\) from a number \(b\) is:

$$ b \cdot (100\% - P\%) $$

Or in decimal form:

$$ b \cdot (1 - d) $$

### How to Calculate the Percentage of a Number in Respect to Another Number

A cake weights 11 lbs, and you eat 3 pieces for a total of 21 oz. How can you know what percentage of cake have you eaten?

It's important to do calculations of this kind with everything in the same units. So, first, let's convert the weight of the cake to ounces.

$$ 11~\mathrm{lb} \cdot \frac{16~\mathrm{oz}}{\mathrm{lb}} = 176~\mathrm{oz} $$

Now it's possible to see the percentage of the cake you've eaten: you need to divide the part (in this case the 21 oz of cake you have eaten) by the whole (the 176 oz of the whole cake):

$$ \frac{11~\mathrm{oz}}{176~\mathrm{oz}} = 0.0625 $$

As seen in the paragraph on how to convert a decimal to a number, you can convert this to a percentage with \( 0.0625 \cdot 100 \% = 6.25\%\).

In this example, you have eaten 6.25% of the whole cake.

### How Do You Combine Two Percentages?

Let's say that some items in an online store are discounted at 20%, and then there is an offer for a 10% discount for everything in your cart at payment.

If you are getting a discount of 20% and then another 10% on top of that... how much is the discount?

It's not 30%, because the second discount is applied at a different time than the first discount.

A discount of 20% means you pay 80% (\(100\% - 20\%\)) of the original price, and a discount of 10% means you pay 90% (\(100\% - 10\%\))of the original price. Combining the two discounts means multiplying together the two percentages, like so:

$$ 80\% \cdot 90\% = 72\% $$

Or in decimal form:

$$ 0.80 \cdot 0.90 = 0.72 $$

So you pay 72% of the original price, or have a discount of 28%.

## Why Are a Decimal and a Percentage Equivalent?

Percentage comes from "per cent", or "over one hundred". The percentage symbol represents the line fraction with 100 in the denominator.

$$ 0.20 = \frac{20}{100} = 20\% $$

The percentage is a simple way to describe how many hundredths of a whole something is.

## How to Work with Percentages in Excel

Now it's time to start working with Excel. Let's start with a pretty important thing. How do you write percentages in Excel?

### How to Write Percentages in Excel

In Excel you can write percentages in two ways:

* You can write a decimal number and then format the cell as a percentage from the format drop down menu or from the Percent Style button:

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-86.png)
_In the first image the Percent Style button is circled in red, and a decimal number is written in the cell. In the second image, the cell has been formatted as a percentage, and the number is converted to a percentage._

* You can write a percentage in the cell, and the cell will automatically take the percentage formatting:

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-87.png)
_In the first image you can see that the empty cell has the "General" formatting, in the second image you can see a percentage being written in the cell, and in the third image you can see that the cell has taken the percentage formatting._

The default format is for a whole percentage. You can change the number of decimal places shown with the "Increase Decimal" and "Decrease Decimal" buttons.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-112.png)
_The two buttons "Increase Decimal" and "Decrease Decimal" circled in red._

Let's say you have a decimal form of 0.12345. Formatting it to a percentage will show \( 12\% \). You can use the buttons to show the decimal places.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-113.png)
_In the first image, the value 12% appears in the cell K1. In the second image, after using the "Increase Decimal" button twice, the value 12.35% appears in the cell K1. In the third image, after using the button "Decrease Decimal" once, the value 12.3% appears in the cell K1._

### How to Calculate the Percentage of a Number in Excel

In math, the percentage of a number is calculated by multiplying that number by the percentage: \( 87\% \cdot 824 = 716.88 \).

In Excel, let's say you have the number in cell A1 and the percentage in cell B1. To calculate the result, you can write in cell C1 `=A1*B1`:

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-110.png)
_In the first image you can see the formula to calculate the percentage of a number, and then its result in the second image._

### How to Calculate the Percentage of a Number with Respect to Another in Excel

In math, you can calculate the percentage of a number with respect to another number by taking the ratio of the two numbers and then converting to a percentage.

If you want to know what percentage 75 is with respect to 142, you can do \( \frac{75}{142} = 0.528 = 52.8\% \).

Let's write 75 in cell G1, and 142 in cell H1. To get the percentage of 75 in respect of 142 you can write in cell I1 `=G1/H1`. The cell will have the result in decimal format, but you can format it to a percentage using the Percent Style button. Then you can adjust the number of decimal places with the Increase Decimal and Decrease Decimal buttons.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-111.png)
_In the first image you can see the formula to do the calculation. In the second image it results in a decimal number. In the third image it has been converted to a percentage, and then in the fourth the number of digits after the decimal separator has been changed._

### How to Calculate a Percentage of Multiple Percentages in Excel

Let's take the example used above.

An online store has a promotion on some items for 20% off. Then there is another promotion of 10% off for everything in the cart at the moment of payment.

The first discount means you pay 80% of the original price of the item. And then you pay 90% of what's in the cart.

How much is the discount?

You get the result by multiplying the two percentages. \( 90\% \cdot 80\%\).

In Excel, if you have the first percentage in I2 and the second in J2, you can write `=I2*J2` to calculate the result.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-120.png)
_In the first image you can see the formula to calculate the percentage from multiple percentages, and then its result in the second image._

## Conclusion

Percentages are a mathematical tool we use in every day life. In this tutorial, you have learned how they work mathematically, and how to use them in Excel.

I hope this article has been useful.

