---
title: How you can use linear regression models to predict quadratic, root, and polynomial
  functions
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-11T16:00:41.000Z'
originalURL: https://freecodecamp.org/news/learn-how-to-improve-your-linear-models-8294bfa8a731
coverImage: https://cdn-media-1.freecodecamp.org/images/1*GsSExG8KXYBd6rk7assRTQ.png
tags:
- name: data
  slug: data
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: Mathematics
  slug: mathematics
- name: R Language
  slug: r
seo_title: null
seo_desc: 'By Björn Hartmann

  When reading articles about machine learning, I often suspect that authors misunderstand
  the term “linear model.” Many authors suggest that linear models can only be applied
  if data can be described with a line. But this is way too ...'
---

By Björn Hartmann

When reading articles about machine learning, I often suspect that authors misunderstand the term “linear model.” Many authors suggest that linear models can only be applied if data can be described with a line. But this is way too restrictive.

Linear models **assume the functional form is linear — not the relationship between your variables**.

I’ll show you how you can improve your linear regressions with quadratic, root, and exponential functions.

![Image](https://cdn-media-1.freecodecamp.org/images/3hDIpUpiqmEqht4LpuzcXCnSIvUHGAUlruxI)

### So what’s the functional form?

The functional form is the **equation you want to estimate**.

Let us start with an example and think about how we could describe salaries of data scientists. Suppose an average data scientist (`i`) receives an entry-level salary (`entry_level_salary`) plus a bonus for each year of his experience (`experience_i`).

Thus, his salary (`salary_i`) is given by the following functional form:

```
salary_i = entry_level_salary + beta_1 * experience_i
```

Now, we can interpret the coefficient `beta_1` as the bonus for each year of experience. And with this coefficient we can start making predictions by just knowing the level of experience.

As your machine learning model takes care of the coefficient `beta_1` , all you need to enter in R or any other software is:

```
model_1 <- lm(salary ~ entry_level_salary + experience)
```

Linearity in the functional form requires that we sum up each determinant on the right-hand side of the equation.

Imagine we are right with our assumptions. Each point indicates one data scientist with his level of experience and salary. Finally, the red line is our predictions.

![Image](https://cdn-media-1.freecodecamp.org/images/wQDyE0LxhC8MjRfFhYJUckvRjMxaAf-761dG)

Many aspiring data scientists already run similar predictions. But often that is all they do with linear models…

### How to estimate quadratic models?

When we want to estimate a quadratic model, we cannot type in something like this:

```
model_2 <- lm(salary ~ entry_level_salary + experience^2)
```

```
>> This will reject an error message
```

Most of these functions do not expect that they have to transform your input variables. As a result, they reject an error message if you try. Furthermore, you do not have a sum at the right-hand side of the equation anymore.

**Note:** You need to compute `experience^²` before adding it into your model. Thus, you will run:

```
# First, compute the square values of experienceexperience_2 <- experience^2
```

```
# Then add them into your regressionmodel_2 <- lm(salary ~ entry_level_salary + experience_2)
```

In return, you get a nice quadratic function:

![Image](https://cdn-media-1.freecodecamp.org/images/2MNxj09K-gnrnxKAJspCA84cUFOQB1CSbCBA)

### Estimate root functions with linear models

Often we observe values that rise fast in the beginning and align to certain level afterwards. Let us modify our example and estimate a typical learning curve.

In the beginning a learning curve tends to be very steep and slows down after some years.

There is one function that features such a trend, the `root` function. So we use the `square root` of `experience` to capture this relationship:

```
# First, compute the square root values of experiencesqrt_experience <- sqrt(experience)
```

```
# Then add them into your regressionmodel_3 <- lm(knowledge ~ sqrt_experience)
```

Again, make sure you compute the square root before you add it to your model:

![Image](https://cdn-media-1.freecodecamp.org/images/ZKh8gvc9V8Wz-9Hht1PJHA67-n6PJh6cP6Mm)

Or you might want to use the logarithmic function as it describes a similar trend. But its’ values are negative between zero and one. So make sure this is not a problem for you and your data.

### Mastering linear models

Finally, you can even estimate polynomial functions with higher orders or exponential functions. All you need to do is to compute all variables before you add them into your linear model:

```
# First, compute polynomialsexperience_2 <- experience^2experience_3 <- experience^3
```

```
# Then add them into your regressionmodel_4 <- lm(salary ~ experience + experience_2 + experience_3)
```

![Image](https://cdn-media-1.freecodecamp.org/images/91UHlbibDwztx9AAcMQMPFqKA9Ub5zLpekOu)

### Two cases where you should use other models

Although linear models can be applied to many cases, there are limitations. The most popular can be divided into two categories:

#### 1. Probabilities:

If you want to estimate the probability of an event, you better use Probit, Logit or Tobit models. When estimating probabilities you use distributions that linear functions cannot capture. Depending on the distribution you assume, you should choose between the Probit, Logit or Tobit model.

#### 2. Count variables

Finally, when estimating a count variable you want to use a Poisson model. Count variables are variable that can only be integers such as `1, 2, 3, 4`.

For example count the number of children, the number of purchases a customer makes or the number of accidents in a region.

### What to take away from this article

There are two things I want you to remember:

1. Improve your linear models and try quadratic, root or polynomial functions.
2. Always transform your data **before** you add them to your regression.

I uploaded the R code for all examples on [GitHub](https://github.com/bjoernhartmann/examples_linear_models). Feel free to download them, play with them, or share them with your friends and colleagues.

![Image](https://cdn-media-1.freecodecamp.org/images/Er55BWHmZF-gxXl1HofpZX2znuPqRM7eIf88)

If you have any questions, write a comment below or [contact me](https://www.bjoern-hartmann.de/?utm_source=medium&utm_medium=link&utm_campaign=Linear_Models&utm_term=Linear_Models). I appreciate your feedback.

