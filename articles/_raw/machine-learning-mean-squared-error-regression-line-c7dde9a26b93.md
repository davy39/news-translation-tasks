---
title: 'Machine learning: an introduction to mean squared error and regression lines'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-16T06:45:02.000Z'
originalURL: https://freecodecamp.org/news/machine-learning-mean-squared-error-regression-line-c7dde9a26b93
coverImage: https://cdn-media-1.freecodecamp.org/images/1*m_GKsrB2EfnLwwug3ASrtw.jpeg
tags:
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: Mathematics
  slug: mathematics
- name: statistics
  slug: statistics
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Moshe Binieli

  Introduction

  This article will deal with the statistical method mean squared error, and I’ll
  describe the relationship of this method to the regression line.

  The example consists of points on the Cartesian axis. We will define a math...'
---

By Moshe Binieli

### **Introduction**

This article will deal with the statistical method **mean squared error**, and I’ll describe the relationship of this method to the **regression line**.

The example consists of points on the Cartesian axis. We will define a mathematical function that will give us the straight line that passes best between all points on the Cartesian axis.

And in this way, we will learn the connection between these two methods, and how the result of their connection looks together.

### General explanation

This is the definition from [Wikipedia](https://en.wikipedia.org/wiki/Mean_squared_error):

> In statistics, the mean squared error (MSE) of an estimator (of a procedure for estimating an unobserved quantity) measures the average of the squares of the errors — that is, the average squared difference between the estimated values and what is estimated. MSE is a risk function, corresponding to the expected value of the squared error loss. The fact that MSE is almost always strictly positive (and not zero) is because of randomness or because the estimator does not account for information that could produce a more accurate estimate.

### The structure of the article

* Get a feel for the idea, graph visualization, mean squared error equation.
* The mathematical part which contains algebraic manipulations and a derivative of two-variable functions for finding a minimum. This section is **for those who want to understand how** we get the mathematical formulas later, you can skip it if that doesn’t interest you.
* An explanation of the mathematical formulae we received and the role of each variable in the formula.
* Examples

### Get a feel for the idea

Let’s say we have seven points, and our goal is to find a line that **minimizes** the squared distances to these different points.

Let’s try to understand that.

I will take an example and I will draw a line between the points. Of course, my drawing isn’t the best, but it’s just for demonstration purposes.

![Image](https://cdn-media-1.freecodecamp.org/images/MNskFmGPKuQfMLdmpkT-X7-8w2cJXulP3683)
_Points on a simple graph._

You might be asking yourself, what is this graph?

* the **purple dots** are the points on the graph. Each point has an x-coordinate and a y-coordinate.
* The **blue line** is our prediction line. This is a line that passes through all the points and fits them in the best way. This line contains the predicted points.
* The **red line** between each purple point and the prediction line are the **errors.** Each error is the distance from the point to its predicted point.

You should remember this equation from your school days, **_y=Mx+B_**, where **M** is the [slope](https://en.wikipedia.org/wiki/Slope) of the line and **B** is [y-intercept](https://en.wikipedia.org/wiki/Y-intercept) of the line.

We want to find M ([slope](https://en.wikipedia.org/wiki/Slope)) and B ([y-intercept](https://en.wikipedia.org/wiki/Y-intercept)) that **minimizes** the squared error!

Let’s define a mathematical equation that will give us the mean squared error for all our points.

![Image](https://cdn-media-1.freecodecamp.org/images/hmZydSW9YegiMVPWq2JBpOpai3CejzQpGkNG)
_General formula for mean squared error._

Let’s analyze what this equation actually means.

* In mathematics, the character that looks like weird E is called summation (Greek sigma). It is the sum of a sequence of numbers, from i=1 to n. Let’s imagine this like an array of points, where we go through all the points, from the first (i=1) to the last (i=n).
* For each point, we take the y-coordinate of the point, and the y’-coordinate. The y-coordinate is our purple dot. The y’ point sits on the line we created. We subtract the y-coordinate value from the y’-coordinate value, and calculate the square of the result.
* The third part is to take the sum of all the (y-y’)² values, and divide it by n, which will give the mean.

Our goal is to minimize this mean, which will provide us with the best line that goes through all the points.

### From concept to mathematical equations

This part is **for people who want to understand how we got to the mathematical equations**. You can skip to the next part if you want.

As you know, the line equation is y=mx+b, where m is the [slope](https://en.wikipedia.org/wiki/Slope) and b is the [y-intercept](https://en.wikipedia.org/wiki/Y-intercept).

Let’s take each point on the graph, and we’ll do our calculation (y-y’)².  
But what is y’, and how do we calculate it? We do not have it as part of the data.

But we do know that, in order to calculate y’, we need to use our line equation, y=mx+b, and put the x in the equation.

From here we get the following equation:

![Image](https://cdn-media-1.freecodecamp.org/images/wSige6ZLxM-QaVt3fRWXIAzsHvX7wdcJ4XOy)

Let’s rewrite this expression to simplify it.

![Image](https://cdn-media-1.freecodecamp.org/images/JFi5pzT7YtJ-0Fkx59jP0hCNHzc8tvsrXgPg)

Let’s begin by opening all the brackets in the equation. I colored the difference between the equations to make it easier to understand.

![Image](https://cdn-media-1.freecodecamp.org/images/vWLTze9HzNDSg4LRM5dbpkYUpkXkhTW6TnRl)

Now, let’s apply another manipulation. We will take each part and put it together. We will take all the y, and (-2ymx) and etc, and we will put them all side-by-side.

![Image](https://cdn-media-1.freecodecamp.org/images/y3gkwSWxwAOcxfxMILLV0teW1273PFtFiqW4)

At this point we’re starting to be messy, so let’s take the mean of all squared values for y, xy, x, x².

Let’s define, for each one, a new character which will represent the mean of all the squared values.

Let’s see an example, let’s take all the y values, and divide them by n since it’s the mean, and call it y(HeadLine).

![Image](https://cdn-media-1.freecodecamp.org/images/L3NWDFs1LUKgQU223EAFXXUXX3OTFWR0gLtE)

If we multiply both sides of the equation by n we get:

![Image](https://cdn-media-1.freecodecamp.org/images/jyiOt9MVCg460395d6mkHlrmK9ssfr8nQGJC)

Which will lead us to the following equation:

![Image](https://cdn-media-1.freecodecamp.org/images/bv3wucYBgHc3Zch115zMYjhH-zYe5VgwjMAH)

If we look at what we got, we can see that we have a 3D surface. It looks like a glass, which rises sharply upwards.

We want to find M and B that minimize the function. We will make a partial derivative with respect to M and a partial derivative with respect to B.

Since we are looking for a minimum point, we will take the partial derivatives and compare to 0.

![Image](https://cdn-media-1.freecodecamp.org/images/88voRjo799rIopVP8YjsHlNhrBSJ8REg26hY)
_Partial derivatives formula_

![Image](https://cdn-media-1.freecodecamp.org/images/6t-4Uq4Y4GMGg9mYWPUUmHHsmaTvxuDPZCj3)
_Partial derivatives_

Let’s take the two equations we received, isolating the variable b from both, and then subtracting the upper equation from the bottom equation.

![Image](https://cdn-media-1.freecodecamp.org/images/-I3Ly2wOtJf9WiecfOjvFiY6U9DXB4PJBQ6t)
_Different writing of the equations after the derivation by parts_

Let’s subtract the first equation from the second equation

![Image](https://cdn-media-1.freecodecamp.org/images/6WzsJxr0jSG8XPYz-F2dSmINqnexxJLxWsxi)
_Merge two equations together_

Let’s get rid of the denominators from the equation.

![Image](https://cdn-media-1.freecodecamp.org/images/Ac05NR92faqptoFE35F2XFcKjllJhJPdwGnE)
_Final equation to find M._

And there we go, this is the equation to find M, let’s take this and write down B equation.

![Image](https://cdn-media-1.freecodecamp.org/images/pjxjeSICBJNckegf3WXCHtfrf7dyIxVfqbBB)
_Final equation to find B._

### Equations for slope and y-intercept

Let’s provide the mathematical equations that will help us find the required [slope](https://en.wikipedia.org/wiki/Slope) and [y-intercept](https://en.wikipedia.org/wiki/Y-intercept).

![Image](https://cdn-media-1.freecodecamp.org/images/290zZ8roKAfKNCrfq1LN7QuTooJjbH19Isiv)
_Slope and y-intercept equations_

So you probably thinking to yourself, what the heck are those weird equations?

They are actually simple to understand, so let’s talk about them a little bit.

![Image](https://cdn-media-1.freecodecamp.org/images/KTFy4uhGXnGSrCoyInhSWfHH4VTEnAJyncpm)
_Sum of x divided by n_

![Image](https://cdn-media-1.freecodecamp.org/images/lQSFx0h7KiRB0uOcriwpFrmhsev3kt4cCUU5)
_Sum of x² divided by n_

![Image](https://cdn-media-1.freecodecamp.org/images/LYZL8LPc8vyZ0wPV2J2sp-pXiuCzvslY8EAQ)
_Sum of xy divided by n_

![Image](https://cdn-media-1.freecodecamp.org/images/0E27klUj208HeeecnRKR9Eokb2PmKfUNoO-O)
_Sum of y divided by n_

Now that we understand our equations it’s time to get all things together and show some examples.

### Examples

A big thank you to [Khan Academy](https://www.khanacademy.org/) for the examples.

#### Example #1

Let’s take 3 points, (1,2), (2,1), (4,3).

![Image](https://cdn-media-1.freecodecamp.org/images/IudmVD0mo4BMYqPEjFyETchb5GGsDv5ikxwB)
_Points on graph._

Let’s find M and B for the equation y=mx+b.

![Image](https://cdn-media-1.freecodecamp.org/images/KFDixcE4WidM6Pez8RNDwOgBorpnj1QuLw5S)
_Sum the x values and divide by n_

![Image](https://cdn-media-1.freecodecamp.org/images/Rqkh4dC9zZ11V4McMwJFspxv5UySTiI9Sv1L)
_Sum the y values and divide by n_

![Image](https://cdn-media-1.freecodecamp.org/images/tkUVYMlF-9qDaK69dWj0bFy1ApEK4DHw05vK)
_Sum the xy values and divide by n_

![Image](https://cdn-media-1.freecodecamp.org/images/80W3OcjPxF9ek2HIjv0VYnwCEhpzURavMAlj)
_Sum the x² values and divide by n_

After we’ve calculated the relevant parts for our M equation and B equation, let’s put those values inside the equations and get the [slope](https://en.wikipedia.org/wiki/Slope) and [y-intercept](https://en.wikipedia.org/wiki/Y-intercept).

![Image](https://cdn-media-1.freecodecamp.org/images/Hri9luC8oVUAgZLnLoDgey4X0T6LEZwIFMav)
_Slope calculation_

![Image](https://cdn-media-1.freecodecamp.org/images/H4Ss6UYBdSfJgx63lz93uXaubcE3-6e1niFS)
_y-intercept calculation_

Let’s take those results and set them inside the line equation y=mx+b.

![Image](https://cdn-media-1.freecodecamp.org/images/S9EESO6mBvglt1o--YlQZQFqhNGPg4we6Kju)

Now let’s draw the line and see how the line passes through the lines in such a way that it minimizes the squared distances.

![Image](https://cdn-media-1.freecodecamp.org/images/DlKy-Eekc0SdHpcOeQPGJobo7jYLfTh0pI8Q)
_Regression line that minimizes the MSE._

#### Example #2

Let’s take 4 points, (-2,-3), (-1,-1), (1,2), (4,3).

![Image](https://cdn-media-1.freecodecamp.org/images/MrlSNVYUJEh-4OcRGXEe3hbeU10wjTH-vmDB)
_Points on graph._

Let’s find M and B for the equation y=mx+b.

![Image](https://cdn-media-1.freecodecamp.org/images/MqNv9HXhu7koehCq1WgBSH2Mje3VoHUM6Dsb)
_Sum the x values and divide by n_

![Image](https://cdn-media-1.freecodecamp.org/images/I8bZESRhxejhmNWbxMlusVlxfCgnrJPbn2En)
_Sum the y values and divide by n_

![Image](https://cdn-media-1.freecodecamp.org/images/YwF2k-wP1YkSiPUoZZ5kV99p5xpS4VeBtlxP)
_Sum the xy values and divide by n_

![Image](https://cdn-media-1.freecodecamp.org/images/Sbo7-PaRePrfBM1sOME5du5GDQ-1r1ntdoD1)
_Sum the x² values and divide by n_

Same as before, let’s put those values inside our equations to find M and B.

![Image](https://cdn-media-1.freecodecamp.org/images/LUideJM-zrCgulLv83Gh08ySgcChQXY6BpxC)
_Slope calculation_

![Image](https://cdn-media-1.freecodecamp.org/images/F9K53LF0Dp3kjIYYC3UJoLfGJqICCIhtqTMo)
_y-intercept calculation_

Let’s take those results and set them inside line equation y=mx+b.

![Image](https://cdn-media-1.freecodecamp.org/images/0o5OFw2QwtBJYntrz4vRJn9ywrdsumLxH5rg)

Now let’s draw the line and see how the line passes through the lines in such a way that it minimizes the squared distances.

![Image](https://cdn-media-1.freecodecamp.org/images/yAMNsNJmTBdZ2MKPbD8JX-es3d-5Oj4OIHRl)
_Regression line that minimizes the MSE_

### In conclusion

As you can see, the whole idea is simple. We just need to understand the main parts and how we work with them.

You can work with the formulas to find the line on another graph, and perform a simple calculation and get the results for the [slope](https://en.wikipedia.org/wiki/Slope) and [y-intercept](https://en.wikipedia.org/wiki/Y-intercept).

That’s all, simple eh? ?

Every comment and all feedback is welcome — if it’s necessary, I will fix the article.

Feel free to contact me directly at LinkedIn — [Click Here](http://www.linkedin.com/in/moshe-binieli-22b11a137).

