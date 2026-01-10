---
title: How to understand Gradient Descent, the most popular ML algorithm
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-18T20:01:00.000Z'
originalURL: https://freecodecamp.org/news/understanding-gradient-descent-the-most-popular-ml-algorithm-a66c0d97307f
coverImage: https://cdn-media-1.freecodecamp.org/images/0*7B2PZ9AB2_3tRLR1.
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: Mathematics
  slug: mathematics
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Keshav Dhandhania

  Gradient Descent is one of the most popular and widely used algorithms for training
  machine learning models.

  Machine learning models typically have parameters (weights and biases) and a cost
  function to evaluate how good a partic...'
---

By Keshav Dhandhania

Gradient Descent is one of the most popular and widely used algorithms for training machine learning models.

[Machine learning](https://www.commonlounge.com/discussion/9325cf512f514e21815ec4c2e2e6e0e3) models typically have parameters (weights and biases) and a cost function to evaluate how good a particular set of parameters are. Many machine learning problems reduce to finding a set of weights for the model which minimizes the cost function.

For example, if the prediction is _p_, the target is _t_, and our error metric is squared error, then the cost function _J(W) = (p - t)²_.

Note that the predicted value _p_ depends on the input _X_ as well as the machine learning model and (current) values of the parameters _W_. During training, our aim is to find a set of values for _W_ such that _(p - t)²_ is small. This means our prediction _p_ will be close to the target _t_.

![Image](https://cdn-media-1.freecodecamp.org/images/e3K6cr03JGW1Lg2OaO8k5uWDvZRb4HhC6mnZ)
_Gradient descent illustration for Linear Regression_

Gradient descent is an iterative method. We start with some set of values for our model parameters (weights and biases), and improve them slowly.

To improve a given set of weights, we try to get a sense of the value of the cost function for weights similar to the current weights (by calculating the gradient). Then we move in the direction which reduces the cost function.

By repeating this step thousands of times, we’ll continually minimize our cost function.

### Pseudocode for Gradient Descent

Gradient descent is used to minimize a cost function _J(W)_ parameterized by a model parameters _W_.

The gradient (or derivative) tells us the incline or slope of the cost function. Hence, to minimize the cost function, we move in the direction opposite to the gradient.

1. **Initialize** the weights _W_ randomly.
2. **Calculate the gradients** _G_ of cost function w.r.t parameters. This is done using partial differentiation: _G = ∂J(W)/∂W._ The value of the gradient _G_ depends on the inputs, the current values of the model parameters, and the cost function. You might need to revisit the topic of differentiation if you are calculating the gradient by hand.
3. **Update the weights** by an amount proportional to G, i.e. _W_ = _W - ηG_
4. Repeat until the cost _J_(_w_) stops reducing, or some other pre-defined **termination criteria** is met.

In step 3, _η_ is the **learning rate** which determines the size of the steps we take to reach a minimum. We need to be very careful about this parameter. High values of _η_ may overshoot the minimum, and very low values will reach the minimum very slowly.

A popular choice for the termination criteria is that the cost _J_(_w_) stops reducing on a validation dataset.

### Intuition for Gradient Descent

Imagine you’re blindfolded in rough terrain, and your objective is to reach the lowest altitude.

One of the simplest strategies you can use, is to feel the ground in every direction, and take a step in the direction where the ground is descending the fastest.

If you keep repeating this process, you might end up at the lake, or even better, somewhere in the huge valley.

![Image](https://cdn-media-1.freecodecamp.org/images/N0IZ9olG1n4CmlzSTFF4XUmb5aS9CRsbMBo7)
_Source: [Andrej Karpathy’s Stanford Course Lecture 3](http://bit.ly/2e7pXyx" rel="noopener" target="_blank" title=")_

The rough terrain is analogous to the cost function, and minimizing the cost function is analogous to trying to reach lower altitudes.

You are blind folded, since we don’t have the luxury of evaluating (or ‘seeing’) the value of the function for every possible set of parameters.

Feeling the slope of the terrain around you is analogous to calculating the gradient, and taking a step is analogous to one iteration of update to the parameters.

By the way — as a small aside — this tutorial is part of the [free Data Science Course](https://www.commonlounge.com/discussion/367fb21455e04c7c896e9cac25b11b47) and [free Machine Learning Course](https://www.commonlounge.com/discussion/33a9cce246d343dd85acce5c3c505009/main) on [Commonlounge](https://www.commonlounge.com/). The courses include many hands-on assignments and projects. If you’re interested in learning Data Science / ML, definitely recommend checking it out.

### Variants of Gradient Descent

There are multiple variants of gradient descent, depending on how much of the data is being used to calculate the gradient.

The main reason for these variations is computational efficiency. A dataset may have millions of data points, and calculating the gradient over the entire dataset can be computationally expensive.

* **Batch gradient descent** computes the gradient of the cost function w.r.t to parameter _W_ for **entire training data**. Since we need to calculate the gradients for the whole dataset to perform one parameter update, batch gradient descent can be very slow.
* **Stochastic gradient descent (SGD)** computes the gradient for each update using a **single training data point** _x_i_ (chosen at random). The idea is that the gradient calculated this way is a stochastic approximation to the gradient calculated using the entire training data. Each update is now much faster to calculate than in batch gradient descent, and over many updates, we will head in the same general direction.
* In **mini-batch gradient descent**, we calculate the gradient for each small mini-batch of training data. That is, we first divide the training data into small batches (say _M_ samples per batch). We perform one update per mini-batch. _M_ is usually in the range 30–500, depending on the problem. Usually mini-batch GD is used because computing infrastructure — compilers, CPUs, GPUs — are often optimized for performing vector additions and vector multiplications.

Of these, SGD and mini-batch GD are most popular.

In a typical scenario, we do several passes over the training data before the termination criteria is met. Each pass is called an _epoch_. Also, note that since the update step is much more computationally efficient in SGD and mini-batch GD, we typically perform 100s-1000s of updates in between checks for termination criteria being met.

### Choosing the learning rate

Typically, the value of the learning rate is chosen manually. We usually start with a small value such as 0.1, 0.01 or 0.001 and adapt it based on whether the cost function is reducing very slowly (increase learning rate) or is exploding / being erratic (decrease learning rate).

Although manually choosing a learning rate is still the most common practice, several methods such as Adam optimizer, AdaGrad and RMSProp have been proposed to automatically choose a suitable learning rate.

_Co-authored by Keshav Dhandhania and Savan Visalpara._

_Originally published as part of the [free Machine Learning Course](https://www.commonlounge.com/discussion/33a9cce246d343dd85acce5c3c505009/main) and [free Data Science Course](https://www.commonlounge.com/discussion/367fb21455e04c7c896e9cac25b11b47) on [www.commonlounge.com](https://www.commonlounge.com/discussion/69a34ad6029549f39087d00d052607ab/main)._

