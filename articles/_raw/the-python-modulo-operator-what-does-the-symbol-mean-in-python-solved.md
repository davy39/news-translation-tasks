---
title: The Python Modulo Operator - What Does the % Symbol Mean in Python? (Solved)
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2019-12-29T22:14:00.000Z'
originalURL: https://freecodecamp.org/news/the-python-modulo-operator-what-does-the-symbol-mean-in-python-solved
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/python-modulo-image.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "When you see the % symbol, you may think \"percent\". But in Python, as\
  \ well as most other programming languages, it means something different. \nThe\
  \ % symbol in Python is called the Modulo Operator. It returns the remainder of\
  \ dividing the left hand op..."
---

When you see the % symbol, you may think "percent". But in Python, as well as most other programming languages, it means something different. 

The `%` symbol in Python is called the Modulo Operator. It returns the remainder of dividing the left hand operand by right hand operand. It's used to get the remainder of a division problem.

The modulo operator is considered an arithmetic operation, along with `+`, `-`, `/`, `*`, `**`, `//`.

The basic syntax is:

```python
a % b
```

In the previous example `a` is divided by `b`, and the remainder is returned. Let's see an example with numbers.

```python
7 % 2
```

The result of the previous example is **one**. Two goes into seven three times and there is **one** left over.

The diagram below shows a visual representation of `7 / 2` and `7 % 2` (The "R" stands for "remainder"). The single logo on the right side (with the green arrow pointing at it) is the remainder from the division problem. It is also the answer to `7 % 2`.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-196.png)

Here is another example:

```python
3 % 4
```

This will result in **three**. Four does not go into three _any_ times so the original **three** is still left over. The diagram below shows what is happening. Remember, the modulo operator returns the remainder after performing division. The remainder is three.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-197.png)

### Example using the Modulo Operator

One common use for the Modulo Operator is to find even or odd numbers. The code below uses the modulo operator to print all odd numbers between 0 and 10.

```python
for number in range(1, 10):
    if(number % 2 != 0):
        print(number)
```

Result:

```
1
3
5
7
9
```

