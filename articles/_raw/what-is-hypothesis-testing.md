---
title: What Is Hypothesis Testing? Types and Python Code Example
subtitle: ''
author: Mene-Ejegi Ogbemi
co_authors: []
series: null
date: '2023-09-22T00:41:23.000Z'
originalURL: https://freecodecamp.org/news/what-is-hypothesis-testing
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/Banner---Tech-writing---hypothesis.jpg
tags:
- name: data analysis
  slug: data-analysis
- name: Data Science
  slug: data-science
- name: statistics
  slug: statistics
seo_title: null
seo_desc: Curiosity has always been a part of human nature. Since the beginning of
  time, this has been one of the most important tools for birthing civilizations.
  Still, our curiosity grows — it tests and expands our limits. Humanity has explored
  the plains of...
---

Curiosity has always been a part of human nature. Since the beginning of time, this has been one of the most important tools for birthing civilizations. Still, our curiosity grows — it tests and expands our limits. Humanity has explored the plains of land, water, and air. We've built underwater habitats where we could live for weeks. Our civilization has explored various planets. We've explored land to an unlimited degree. 

These things were possible because humans asked questions and searched until they found answers. However, for us to get these answers, a proven method must be used and followed through to validate our results. Historically, philosophers assumed the earth was flat and you would fall off when you reached the edge. While philosophers like Aristotle argued that the earth was spherical based on the formation of the stars, they could not prove it at the time. 

This is because they didn't have adequate resources to explore space or mathematically prove Earth's shape. It was a Greek mathematician named Eratosthenes who calculated the earth's circumference with incredible precision. He used scientific methods to show that the Earth was not flat. Since then, other methods have been used to prove the Earth's spherical shape.

When there are questions or statements that are yet to be tested and confirmed based on some scientific method, they are called hypotheses. Basically, we have two types of hypotheses: null and alternate.

A **null hypothesis** is one's default belief or argument about a subject matter. In the case of the earth's shape, the null hypothesis was that the earth was flat.

An **alternate hypothesis** is a belief or argument a person might try to establish. Aristotle and Eratosthenes argued that the earth was spherical.

Other examples of a random alternate hypothesis include:

* The weather may have an impact on a person's mood.
* More people wear suits on Mondays compared to other days of the week.
* Children are more likely to be brilliant if both parents are in academia, and so on.

## What is Hypothesis Testing?

Hypothesis testing is the act of testing whether a hypothesis or inference is true. When an alternate hypothesis is introduced, we test it against the null hypothesis to know which is correct. Let's use a plant experiment by a 12-year-old student to see how this works.

The hypothesis is that a plant will grow taller when given a certain type of fertilizer. The student takes two samples of the same plant, fertilizes one, and leaves the other unfertilized. He measures the plants' height every few days and records the results in a table. 

After a week or two, he compares the final height of both plants to see which grew taller. If the plant given fertilizer grew taller, the hypothesis is established as fact. If not, the hypothesis is not supported. This simple experiment shows how to form a hypothesis, test it experimentally, and analyze the results.

In hypothesis testing, there are two types of error: Type I and Type II.

When we reject the null hypothesis in a case where it is correct, we've committed a Type I error. Type II errors occur when we fail to reject the null hypothesis when it is incorrect.

In our plant experiment above, if the student finds out that both plants' heights are the same at the end of the test period yet opines that fertilizer helps with plant growth, he has committed a Type I error. 

However, if the fertilized plant comes out taller and the student records that both plants are the same or that the one without fertilizer grew taller, he has committed a Type II error because he has failed to reject the null hypothesis.

## What are the Steps in Hypothesis Testing?

The following steps explain how we can test a hypothesis:

### Step #1 - Define the Null and Alternative Hypotheses

Before making any test, we must first define what we are testing and what the default assumption is about the subject. In this article, we'll be testing if the average weight of 10-year-old children is more than 32kg. 

Our null hypothesis is that 10 year old children weigh 32 kg on average. Our alternate hypothesis is that the average weight is more than 32kg. `Ho` denotes a null hypothesis, while `H1` denotes an alternate hypothesis.

Ho = 32

H1 = 32

### Step #2 - Choose a Significance Level

The significance level is a threshold for determining if the test is valid. It gives credibility to our hypothesis test to ensure we are not just luck-dependent but have enough evidence to support our claims. We usually set our significance level before conducting our tests. The criterion for determining our significance value is known as p-value. 

A lower p-value means that there is stronger evidence against the null hypothesis, and therefore, a greater degree of significance. A p-value of 0.05 is widely accepted to be significant in most fields of science. P-values do not denote the probability of the outcome of the result, they just serve as a benchmark for determining whether our test result is due to chance. For our test, our p-value will be 0.05.

### Step #3 - Collect Data and Calculate a Test Statistic

You can obtain your data from online data stores or conduct your research directly. Data can be scraped or researched online. The methodology might depend on the research you are trying to conduct.

We can calculate our test using any of the appropriate hypothesis tests. This can be a T-test, Z-test, Chi-squared, and so on. There are several hypothesis tests, each suiting different purposes and research questions. In this article, we'll use the T-test to run our hypothesis, but I'll explain the Z-test, and chi-squared too.

T-test is used for comparison of two sets of data when we don't know the population standard deviation. It's a parametric test, meaning it makes assumptions about the distribution of the data. These assumptions include that the data is normally distributed and that the variances of the two groups are equal. In a more simple and practical sense, imagine that we have test scores in a class for males and females, but we don't know how different or similar these scores are. We can use a t-test to see if there's a real difference.

The Z-test is used for comparison between two sets of data when the population standard deviation is known. It is also a parametric test, but it makes fewer assumptions about the distribution of data. The z-test assumes that the data is normally distributed, but it does not assume that the variances of the two groups are equal. In our class test example, with the t-test, we can say that if we already know how spread out the scores are in both groups, we can now use the z-test to see if there's a difference in the average scores.

The Chi-squared test is used to compare two or more categorical variables. The chi-squared test is a non-parametric test, meaning it does not make any assumptions about the distribution of data. It can be used to test a variety of hypotheses, including whether two or more groups have equal proportions.

### Step #4 - Decide on the Null Hypothesis Based on the Test Statistic and Significance Level

After conducting our test and calculating the test statistic, we can compare its value to the predetermined significance level. If the test statistic falls beyond the significance level, we can decide to reject the null hypothesis, indicating that there is sufficient evidence to support our alternative hypothesis. 

On the other contrary, if the test statistic does not exceed the significance level, we fail to reject the null hypothesis, signifying that we do not have enough statistical evidence to conclude in favor of the alternative hypothesis.

### Step #5 - Interpret the Results

Depending on the decision made in the previous step, we can interpret the result in the context of our study and the practical implications. For our case study, we can interpret whether we have significant evidence to support our claim that the average weight of 10 year old children is more than 32kg or not.

For our test, we are generating random dummy data for the weight of the children. We'll use a t-test to evaluate whether our hypothesis is correct or not.

```python
import numpy as np
import scipy.stats as stats

# Create a dummy dataset of 10 year old children's weight
data = np.random.randint(20, 40, 10)

# Define the null hypothesis
H0 = "The average weight of 10 year old children is 32kg."

# Define the alternative hypothesis
H1 = "The average weight of 10 year old children is more than 32kg."

# Calculate the test statistic
t_stat, p_value = stats.ttest_1samp(data, 32)

# Print the results
print("Test statistic:", t_stat)
print("p-value:", p_value)

# Conclusion
if p_value < 0.05:
    print("Reject the null hypothesis.")
else:
    print("Fail to reject the null hypothesis.")
```

For a better understanding, let's look at what each block of code does.

```python
import numpy as np
import scipy.stats as stats
```

The first block is the import statement, where we import `numpy` and `scipy.stats`. Numpy is a Python library used for scientific computing. It has a large library of functions for working with arrays. Scipy is a library for mathematical functions. It has a stat module for performing statistical functions, and that's what we'll be using for our t-test.

```python
# Create a dummy dataset of 10 year old children's weight
data = np.random.randint(20, 40, 100)
```

The weights of the children were generated at random since we aren't working with an actual dataset. The random module within the Numpy library provides a function for generating random numbers, which is `randint`. 

The `randint` function takes three arguments. The first (20) is the lower bound of the random numbers to be generated. The second (40) is the upper bound, and the third (100) specifies the number of random integers to generate. That is, we are generating random weight values for 100 children. In real circumstances, these weight samples would have been obtained by taking the weight of the required number of children needed for the test.

```python
# Define the null hypothesis
H0 = "The average weight of 10 year old children is 32kg."

# Define the alternative hypothesis
H1 = "The average weight of 10 year old children is more than 32kg."
```

Using the code above, we declared our null and alternate hypotheses stating the average weight of a 10-year-old in both cases.

```python
# Calculate the test statistic
t_stat, p_value = stats.ttest_1samp(data, 32)
```

`t_stat` and `p_value` are the variables in which we'll store the results of our functions. `stats.ttest_1samp` is the function that calculates our test. It takes in two variables, the first is the `data` variable that stores the array of weights for children, and the second (32) is the value against which we'll test the mean of our array of weights or dataset in cases where we are using a real-world dataset.

```python

# Print the results
print("Test statistic:", t_stat)
print("p-value:", p_value)
```

The code above prints both values for `t_stats` and `p_value`.

```python
# Conclusion
if p_value < 0.05:
    print("Reject the null hypothesis.")
else:
    print("Fail to reject the null hypothesis.")
```

Lastly, we evaluated our `p_value` against our significance value, which is 0.05. If our `p_value` is less than 0.05, we reject the null hypothesis. Otherwise, we fail to reject the null hypothesis. Below is the output of this program. Our null hypothesis was rejected.

```python
Test statistic: -5.114430435590074
p-value: 1.541000376540265e-06
Reject the null hypothesis.
```

## Conclusion

In this article, we discussed the importance of hypothesis testing. We highlighted how science has advanced human knowledge and civilization through formulating and testing hypotheses.

We discussed Type I and Type II errors in hypothesis testing and how they underscore the importance of careful consideration and analysis in scientific inquiry. It reinforces the idea that conclusions should be drawn based on thorough statistical analysis rather than assumptions or biases.

We also generated a sample dataset using the relevant Python libraries and used the needed functions to calculate and test our alternate hypothesis.

Thank you for reading! Please follow me on [LinkedIn](https://www.linkedin.com/in/ogbemi-ejegi/) where I also post more data related content.

