---
title: How to read a Regression Table
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-31T20:25:40.000Z'
originalURL: https://freecodecamp.org/news/https-medium-com-sharadvm-how-to-read-a-regression-table-661d391e9bd7-708e75efc560
coverImage: https://cdn-media-1.freecodecamp.org/images/1*kiLhwgfqplmsa9QgUfXjKQ.jpeg
tags:
- name: data
  slug: data
- name: Data Science
  slug: data-science
- name: predictive analytics
  slug: predictive-analytics
- name: '#Regression'
  slug: regression
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Sharad Vijalapuram

  What is regression?

  Regression is one of the most important and commonly used data analysis processes.
  Simply put, it is a statistical method that explains the strength of the relationship
  between a dependent variable and one or...'
---

By Sharad Vijalapuram

### **What is regression?**

Regression is one of the most important and commonly used data analysis processes. Simply put, it is a statistical method that explains the strength of the relationship between a dependent variable and one or more independent variable(s).

A dependent variable could be a variable or a field you are trying to predict or understand. An independent variable could be the fields or data points that you think might have an impact on the dependent variable.

In doing so, it answers a couple of important questions —

* What variables matter?
* To what extent do these variables matter?
* How confident are we about these variables?

### Let’s take an example…

To better explain the numbers in the regression table, I thought it would be useful to use a sample dataset and walk through the numbers and their importance.

I’m using a small dataset that contains GRE (a test that students take to be considered for admittance in Grad schools in the US) scores of 500 students and their chance of admittance into a university.

Because `chance of admittance` depends on `GRE score`, `chance of admittance` is the dependent variable and `GRE score` is the independent variable.

![Image](https://cdn-media-1.freecodecamp.org/images/gEmYfLngh9iyyI1iWPkIHT2H4VGekxpIxUHY)
_Scatterplot of GRE scores and chance of admittance_

#### Regression line

Drawing a straight line that best describes the relationship between the GRE scores of students and their chances of admittance gives us the **linear regression line**. This is known as the **trend line** in various BI tools. The basic idea behind drawing this line is to minimize the distance between the data points at a given x-coordinate and the y-coordinate through which the regression line passes.

![Image](https://cdn-media-1.freecodecamp.org/images/ZKNDJUJRHA0Es0khr8RpLkbot3QmMPxsMc8Z)
_Scatterplot with a regression line._

The regression line makes it easier for us to represent the relationship. It is based on a mathematical equation that associates the x-coefficient and y-intercept.

**Y-intercept** is the point at which the line intersects the y-axis at x = 0. It is also the value the model would take or predict when x is 0.

**Coefficients** provide the impact or weight of a variable towards the entire model. In other words, it provides the amount of change in the dependent variable for a unit change in the independent variable.

#### Calculating the regression line equation

In order to find out the model’s y-intercept, we extend the regression line far enough until it intersects the y-axis at x = 0. This is our y-intercept and it is around -2.5. The number might not really make sense for the data set we are working on but the intention is to only show the calculation of y-intercept.

![Image](https://cdn-media-1.freecodecamp.org/images/Qr8R9PGFVxf8VnwyQrmaVCpU0PqnAeW3FH9i)
_Calculating the y-intercept_

The coefficient for this model will just be the slope of the regression line and can be calculated by getting the change in the admittance over the change in GRE scores.

![Image](https://cdn-media-1.freecodecamp.org/images/r8Xzo0fzjJ4HeM-cHz66kST-aW-gTdcqde05)
_Calculating the slope_

In the example above, the coefficient would just be

> m = (y2-y1) / (x2-x1)

And in this case, it would be close to 0.01.

The formula y = m*x + b helps us calculate the mathematical equation of our regression line. Substituting the values for y-intercept and slope we got from extending the regression line, we can formulate the equation -

> y = 0.01x — 2.48

-2.48 is a more accurate y-intercept value I got from the regression table as shown later in this post.

This equation lets us forecast and predicts the chance of admittance of a student when his/her GRE score is known.

Now that we have the basics, let’s jump onto reading and interpreting a regression table.

### Reading a regression table

The regression table can be roughly divided into **three components** —

* **Analysis of Variance (ANOVA):** provides the analysis of the variance in the model, as the name suggests.
* **regression statistics:** provide numerical information on the variation and how well the model explains the variation for the given data/observations.
* **residual output:** provides the value predicted by the model and the difference between the actual observed value of the dependent variable and its predicted value by the regression model for each data point.

### **Analysis of Variance (ANOVA)**

![Image](https://cdn-media-1.freecodecamp.org/images/qcL1FHAqajHQ3fk2Qnp2wMjSNDzWAf5vMNYP)
_ANOVA table_

#### Degrees of freedom (df)

**Regression df** is the number of independent variables in our regression model. Since we only consider GRE scores in this example, it is 1.

**Residual df** is the total number of observations (rows) of the dataset subtracted by the number of variables being estimated. In this example, both the GRE score coefficient and the constant are estimated.

Residual df = 500 — 2 = 498

**Total df** — is the sum of the regression and residual degrees of freedom, which equals the size of the dataset minus 1.

#### **Sum of Squares (SS)**

![Image](https://cdn-media-1.freecodecamp.org/images/9E4FVD77xkpB9bZ2Npwa-Y7jwhlEH6-qzDlh)
_Regression line with the mean of the dataset in red._

**Regression SS** is the total variation in the dependent variable that is explained by the regression model. It is the sum of the square of the difference between the predicted value and mean of the value of all the data points.

> ∑ (ŷ — ӯ)²

From the ANOVA table, the regression SS is 6.5 and the total SS is 9.9, which means the regression model explains about 6.5/9.9 (around 65%) of all the variability in the dataset.

**Residual SS** — is the total variation in the dependent variable that is left unexplained by the regression model. It is also called the **Error Sum of Squares** and is the sum of the square of the difference between the actual and predicted values of all the data points.

> ∑ (y — ŷ)²

From the ANOVA table, the residual SS is about 3.4. In general, the smaller the error, the better the regression model explains the variation in the data set and so we would usually want to minimize this error.

**Total SS** — is the sum of both, regression and residual SS or by how much the chance of admittance would vary if the GRE scores are **NOT** taken into account.

**Mean Squared Errors (MS)** — are the mean of the sum of squares or the sum of squares divided by the degrees of freedom for both, regression and residuals.

> Regression MS = ∑ (ŷ — ӯ)²/Reg. df

> Residual MS = ∑ (y — ŷ)²/Res. df

**F** — is used to test the hypothesis that the slope of the independent variable is zero. Mathematically, it can also be calculated as

> F = Regression MS / Residual MS

This is otherwise calculated by comparing the F-statistic to an F distribution with regression df in numerator degrees and residual df in denominator degrees.

**Significance F** — is nothing but the p-value for the null hypothesis that the coefficient of the independent variable is zero and as with any p-value, a low p-value indicates that a significant relationship exists between dependent and independent variables.

![Image](https://cdn-media-1.freecodecamp.org/images/QeNjs4oji3peiiodEnLof0wx4NSJlu5imm9C)

**Standard Error** — provides the estimated standard deviation of the distribution of coefficients. It is the amount by which the coefficient varies across different cases. A coefficient much greater than its standard error implies a probability that the coefficient is not 0.

**t-Stat** — is the t-statistic or t-value of the test and its value is equal to the coefficient divided by the standard error.

> t-Stat = Coefficients/Standard Error

Again, the larger the coefficient with respect to the standard error, the larger the t-Stat is and higher the probability that the coefficient is away from 0.

**p-value** — The t-statistic is compared with the t distribution to determine the p-value. We usually only consider the p-value of the independent variable which provides the likelihood of obtaining a sample as close to the one used to derive the regression equation and verify if the slope of the regression line is actually zero or the coefficient is close to the coefficient obtained.

A p-value below 0.05 indicates 95% confidence that the slope of the regression line is not zero and hence there is a significant linear relationship between the dependent and independent variables.

A p-value greater than 0.05 indicates that the slope of the regression line may be zero and that there is not sufficient evidence at the 95% confidence level that a significant linear relationship exists between the dependent and independent variables.

Since the p-value of the independent variable GRE score is very close to 0, we can be extremely confident that there is a significant linear relationship between GRE scores and the chance of admittance.

**Lower and Upper 95%** — Since we mostly use a sample of data to estimate the regression line and its coefficients, they are mostly an approximation of the true coefficients and in turn the true regression line. The lower and upper 95% boundaries give the 95th confidence interval of lower and upper bounds for each coefficient.

Since the 95% confidence interval for GRE scores is 0.009 and 0.01, the boundaries do not contain zero and so, we can be 95% confident that there is a significant linear relationship between GRE scores and the chance of admittance.

Please note that a confidence level of 95% is widely used but, a level other than 95% is possible and can be set up during regression analysis.

### **Regression Statistics**

![Image](https://cdn-media-1.freecodecamp.org/images/7zaL2AUSPsdw2T8imw5bAqr6kCOy3nKOeHGk)
_Regression Statistics table_

**R² (R Square)** — represents the power of a model. It shows the amount of variation in the dependent variable the independent variable explains and always lies between values 0 and 1. As the R² increases, more variation in the data is explained by the model and better the model gets at prediction. A low R² would indicate that the model doesn’t fit the data well and that an independent variable doesn’t explain the variation in the dependent variable well.

> R² = Regression Sum of Squares/Total Sum of Squares

However, R square _cannot_ determine whether the coefficient estimates and predictions are biased, which is why you must assess the residual plots, which are discussed later in this article.

R-square also does not indicate whether a regression model is adequate. You can have a low R-squared value for a good model, or high R-squared value for a model that does not fit the data.

R², in this case, is 65 %, which implies that the GRE scores can explain 65% of the variation in the chance of admittance.

**Adjusted R²** — is R² multiplied by an adjustment factor. This is used while comparing different regression models with different independent variables. This number comes in handy while deciding on the right independent variables in multiple regression models.

**Multiple R** — is the positive square root of R²

**Standard Error** — is different from the standard error of the coefficients. This is the estimated standard deviation of the error of the regression equation and is a good measure of the accuracy of the regression line. It is the square root of the residual mean squared errors.

> Std. Error = √(Res.MS)

### **Residual Output**

Residuals are the difference between the actual value and the predicted value of the regression model and residual output is the predicted value of the dependent variable by the regression model and the residual for each data point.

And as the name suggests, a residual plot is a scatter plot between the residual and the independent variable, which in this case is the GRE score of each student.

A residual plot is important in detecting things like **heteroscedasticity**, **non-linearity,** and **outliers**. The process of detecting them is not being discussed as part of this article but, the fact that the residual plot for our example has data scattered randomly helps us in establishing the fact that the relationship between the variables in this model is linear.

![Image](https://cdn-media-1.freecodecamp.org/images/svhwHtrkIYoNwy323YB8jPS-OxeWmvmpPAyH)
_Residual Plot_

### **Intent**

The intent of this article is not to build a working regression model but to provide a walkthrough of all the regression variables and their importance when necessary with a sample data set in a regression table.

Although this article provides an explanation with a single variable linear regression as an example, please be aware that some of these variables could have more importance in the cases of multi-variable or other situations.

### **References**

* [Graduate Admissions Dataset](https://www.kaggle.com/mohansacharya/graduate-admissions)
* [10 things about reading a regression table](https://egap.org/methods-guides/10-things-know-about-reading-regression-table)
* [A refresher on regression analysis](https://hbr.org/2015/11/a-refresher-on-regression-analysis)

