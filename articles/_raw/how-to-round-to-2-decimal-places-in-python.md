---
title: How to Round to 2 Decimal Places in Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-08-22T17:17:58.000Z'
originalURL: https://freecodecamp.org/news/how-to-round-to-2-decimal-places-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/round-up-numbers-1.png
tags:
- name: Math
  slug: math
- name: Python
  slug: python
seo_title: null
seo_desc: "By Dillion Megida\nPython provides many math methods for mathematical operations\
  \ such as square roots, exponents, and so on. \nIn this article, I will show you\
  \ how to round up a number to a specified decimal place.\nWhat is a Decimal Place?\n\
  Look at this..."
---

By Dillion Megida

Python provides many math methods for mathematical operations such as square roots, exponents, and so on. 

In this article, I will show you how to round up a number to a specified decimal place.

## What is a Decimal Place?

Look at this number: **324.89**.

Each number here has a position which is refered to as **place value**. The place value of:
* **3** is **hundreds**
* **2** is **tens**
* **4** is **ones**
* **8** is **tenths**
* **9** is **hundredths**

After the decimal point, you have two numbers: **8**, then **9**. The decimal place of a number is the position of the number after a decimal point (on the right side of it). 

This definition means that the decimal place of **8** (in the tenths position) is 1, and **9** (in the hundredths position) is 2.

## How to Round Up to a Certain Decimal Place

What does it mean then to round up to a certain decimal place? It means that you round up a number at a decimal place based on the number after it. 

If the number after the decimal place is 5 or more, the number at the decimal place is rounded up **+1**. Otherwise, the number at the decimal place stays the same and the number after the decimal place is rounded down to 0.

For example, let's say we want to round up **24.89** to **1** decimal place. Or you can put it as rounding up **24.89** to the nearest **tenth**.

The number **8** is at the 1 decimal place, and the number after 8 is **9**. Since 9 is more than 5, **24.89**, rounded up to the nearest tenth will be **24.9**.

As another example, let's take **24.82** and round it to 1 decimal place (the nearest tenth). Since **2** is not larger than 5, **8** remains the same, and **2** gets rounded down – resulting in **24.8**. 

## How to Round Up a Decimal Place in Python

Now that you understand how to round up a decimal place, let's see how to do it in Python.

You can use the global `round` function to round up numbers to a decimal place. The syntax is:

```python
round(number, decimal_point)
```

The function accepts the number and `decimal_point` as arguments. `decimal_point` specifies the decimal place that you want to round the number up to. Let's see an example:

```python
num = 24.89

rounded = round(num, 1)
print(rounded)

# 24.9
```

Here's another example of a longer number:

```python
num = 20.4454

rounded3 = round(num, 3)
# to 3 decimal places

rounded2 = round(num, 2)
# to 2 decimal places

print(rounded3)
# 20.445

print(rounded2)
# 20.45
```

For `rounded3`, the `num` is rounded up to 3 decimal places. At the 3rd decimal place is **5**, and the number that comes after it is **4**. Since 4 is not greater than 5, the number 5 stays the same and 4 is rounded down to 0.

For `rounded2`, the `num` is rounded up to 2 decimal places. At the 2nd decimal place is **4**, and the number after it is **5**. Since this number is greater than or equal to 5, the number **4** is rounded up to 5.

## Conclusion

Rounding up numbers can be useful for keeping floating numbers within fixed digits. 

For example, this is useful with currencies that only accept two decimal places (like the dollar: $100.99). In cases where a calculation for a product results in $50.678, you may want to round it to 2 decimal places, like this: $50.68. This way, it can be easier to give someone the actual monetary value.

In this article, I've briefly explained what decimal places are, and how to round numbers to certain decimal places in Python.


