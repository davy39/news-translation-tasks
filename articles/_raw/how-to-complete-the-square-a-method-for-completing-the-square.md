---
title: 'Completing the Square Formula: How to Complete The Square with a Quadratic
  Equation'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-17T22:51:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-complete-the-square-a-method-for-completing-the-square
coverImage: https://www.freecodecamp.org/news/content/images/2020/02/header-2.png
tags:
- name: Math
  slug: math
seo_title: null
seo_desc: 'By Alexander Arobelidze

  Consider the following quadratic equation: x2 = 9. If asked to solve it, we would
  naturally take the square root of 9 and end up with 3 and -3. But what if simple
  square root methods won''t do? What if the equation includes x r...'
---

By Alexander Arobelidze

<p>Consider the following quadratic equation: <b><em>x<sup>2</sup> = 9</em></b>. If asked to solve it, we would naturally take the square root of <b><em>9</em></b> and end up with <b><em>3</em></b> and <b><em>-3</em></b>. But what if simple square root methods won't do? What if the equation includes <b><em>x</em></b> raised to the first power and cannot be easily factored?

Fortunately, there is a method for **completing the square**. As as result, a quadratic equation can be solved by taking the square root. Let's explore this step by step together. 

Say we are given the following equation:

![Image](https://www.freecodecamp.org/news/content/images/2020/02/intro1.png)
_Given equation: 4x<sup>2</sup> + 13x + 7 = x + 6_

## EXAMPLE 1: Completing the square

### STEP 1: Separate The Variable Terms From The Constant Term

![Image](https://www.freecodecamp.org/news/content/images/2020/02/step1.png)
_Separate terms to simplify: 4x<sup>2</sup> + 13x **- x** = 6 **- 7**_

Let's simplify our equation. First, separate the terms that include variables from the constant terms. Next, subtract **x** from **13x** (result is **12x**) and subtract **7** from **6** (result is **-1**).

### STEP 2: Make Sure The Coefficient Of X Squared Is Equal To 1

![Image](https://www.freecodecamp.org/news/content/images/2020/02/step2.png)
_Divide by the term of x<sup>2</sup> : x<sup>2</sup> + 3x = -1/4_

The method of completing the square works a lot easier when the coefficient of **x<sup>2</sup>** equals 1. The coefficient in our case equals **4**. Dividing 4 into each member results in **x<sup>2</sup> + 3x = - 1/4**. 

### STEP 3: Complete The Square

![Image](https://www.freecodecamp.org/news/content/images/2020/02/step3a.png)
_The coefficient of x is divided by 2 and squared: (3 / 2)<sup>2</sup> = 9/4_

First we need to find the constant term of our complete square. The coefficient of **x**, which equals 3 is divided by **2** and squared, giving us **9/4**.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/step3b.png)
_The resulting 9/4 is added and subtracted: x<sup>2</sup> + 3x + 9/4 - 9/4 = -1/4_

Then we add and subtract **9/4** as shown above. Doing so does not affect our equation (**9/4 - 9/4 = 0**), but gives us an expression for the complete square **x<sup>2</sup> + 3x + 9/4**.

### STEP 4: Factor The Expression X squared + 3X + 9/4

![Image](https://www.freecodecamp.org/news/content/images/2020/02/step4.png)
_Factoring x<sup>2</sup> + 3x + 9/4 gives us (x + 3/2)<sup>2</sup>_

Let's now remember a more general **(x + a)<sup>2</sup> = x<sup>2</sup> + 2ax + a<sup>2</sup>** and use it in the current example. Substituting our numbers gives us:  **x<sup>2</sup> + 3x + 9/4 = x<sup>2</sup> + 2*(3/2)*x + (3/2)<sup>2</sup> =** **(x + 3/2)<sup>2</sup>**.

### STEP 5: Take The Square Root

![Image](https://www.freecodecamp.org/news/content/images/2020/02/step5.png)
_Taking the square root: ((x + 3/2)<sup>2</sup>)<sup>1/2</sup> = (2)<sup>1/2</sup>. x = 2<sup>1/2</sup> - 3/2 &amp; x = -2<sup>1/2</sup> - 3/2_

Finally, taking the square root from both sides gives us **√(x + 3/2)<sup>2</sup> = ±√2**. Or simply  x + 3/2 = ±√2. We conclude this by solving for **x**: **X<sub>1</sub>= √2 - 3/2** and **X<sub>2</sub> = - √2 - 3/2_._** 

## EXAMPLE 2: Let's Solve One More

![Image](https://www.freecodecamp.org/news/content/images/2020/02/EX2header.png)
_Given equation: 2x<sup>2</sup> + x - 7 = x<sup>2</sup> + 9x - 12_

### STEP 1: Separate The Variable Terms From The Constant Term

![Image](https://www.freecodecamp.org/news/content/images/2020/02/EX2step1.png)
_Separate terms to simplify: 2x<sup>2</sup> **- x<sup>2</sup>** + x **- 9x** = -12 **+ 7**_

Simplify by separating the terms with variables from constant terms. Then perform subtraction and addition on both sides of the equation.

### STEP 2: Make Sure The Coefficient Of x squared Is Equal To 1

![Image](https://www.freecodecamp.org/news/content/images/2020/02/EX2step2.png)
_The coefficient of x<sup>2</sup> is equal to 1_

Here, the coefficient of **X<sup>2</sup>** already equals **1**, so no further action needed.

### STEP 3: Complete The Square

![Image](https://www.freecodecamp.org/news/content/images/2020/02/EX2step3.png)
_The coefficient of x is divided by 2 and squared: (-8 / 2)<sup>2</sup> = 16_

As in previous example, we find the constant term of our complete square. The coefficient of **x**, which equals -8 is divided by **2** and squared, giving us **16**.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/EX2step3b.png)
_The resulting 16 is added and subtracted: x<sup>2</sup> - 8x + 16 - 16 = -5_

We add and subtract **16** and can see that **x<sup>2</sup> - 8x + 16** gives us a complete square.

### STEP 4: Factor The Expression X squared - 8X + 16

![Image](https://www.freecodecamp.org/news/content/images/2020/02/EX2step4.png)
_Factoring x<sup>2</sup> - 8x + 16 gives us (x - 4)<sup>2</sup>_

Since the constant term **-8** is with the minus sign, we use this general form: **(x - a)<sup>2</sup> = x<sup>2</sup> - 2ax + a<sup>2</sup>**. Using our numbers gives us: **x<sup>2</sup> - 8x + 16 = x<sup>2</sup> - 2*(4)*x + (4)<sup>2</sup> = (x - 4)<sup>2</sup>**.                               

### STEP 5: Take The Square Root

![Image](https://www.freecodecamp.org/news/content/images/2020/02/EX2step5.png)
_Taking the square root: ((x - 4)<sup>2</sup>)<sup>1/2</sup> = (11)<sup>1/2</sup>. x = 4 + 11<sup>1/2</sup> &amp; x = 4 - 11<sup>1/2</sup>_

Finally, taking the square root from both sides gives us **√(x - 4)<sup>2</sup> = ±√11**. Or simply  x - 4 = ±√11. We conclude this by solving for **_x_**: **X<sub>1</sub> = 4 + √11** and **X<sub>2</sub> = 4 - √11** 

And there you have it!




