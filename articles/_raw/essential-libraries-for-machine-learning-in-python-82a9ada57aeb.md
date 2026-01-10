---
title: Essential libraries for Machine Learning in Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-03T15:12:06.000Z'
originalURL: https://freecodecamp.org/news/essential-libraries-for-machine-learning-in-python-82a9ada57aeb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*SltpaprT6Vc6IhQqVsYKtA.png
tags:
- name: Data Science
  slug: data-science
- name: data visualization
  slug: data-visualization
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Shubhi Asthana

  Python is often the language of choice for developers who need to apply statistical
  techniques or data analysis in their work. It is also used by data scientists whose
  tasks need to be integrated with web apps or production environm...'
---

By Shubhi Asthana

Python is often the language of choice for developers who need to apply statistical techniques or data analysis in their work. It is also used by data scientists whose tasks need to be integrated with web apps or production environments.

Python really shines in the field of machine learning. Its combination of consistent syntax, shorter development time and flexibility makes it well-suited to developing sophisticated models and prediction engines that can plug directly into production systems.

One of Python’s greatest assets is its extensive set of libraries.

Libraries are sets of routines and functions that are written in a given language. A robust set of libraries can make it easier for developers to perform complex tasks without rewriting many lines of code.

Machine learning is largely based upon mathematics. Specifically, mathematical optimization, statistics and probability. Python libraries help researchers/mathematicians who are less equipped with developer knowledge to easily “do machine learning”.

Below are some of the most commonly used libraries in machine learning:

#### **Scikit-learn for working with classical ML algorithms**

![Image](https://cdn-media-1.freecodecamp.org/images/saQHUdhXbYflEmnDMhN5Qewekg0h6KPx9oIT)

[Scikit-learn](http://scikit-learn.org/stable/user_guide.html) is one the most popular ML libraries. It supports many supervised and unsupervised learning algorithms. Examples include linear and logistic regressions, decision trees, clustering, k-means and so on.

It builds on two basic libraries of Python, NumPy and SciPy. It adds a set of algorithms for common machine learning and data mining tasks, including clustering, regression and classification. Even tasks like transforming data, feature selection and ensemble methods can be implemented in a few lines.

For a novice in ML, Scikit-learn is a more-than-sufficient tool to work with, until you start implementing more complex algorithms.

#### **Tensorflow for Deep Learning**

![Image](https://cdn-media-1.freecodecamp.org/images/5M9fILVJO06e0zPLStKihIlOYxsLUw8f3kI9)

If you are in the world of machine learning, you have probably heard about, tried or implemented some form of deep learning algorithm. Are they necessary? Not all the time. Are they cool when done right? Yes!

The interesting thing about [Tensorflow](https://www.tensorflow.org/) is that when you write a program in Python, you can compile and run on either your CPU or GPU. So you don’t have to write at the C++ or CUDA level to run on GPUs.

It uses a system of multi-layered nodes that allows you to quickly set up, train, and deploy artificial neural networks with large datasets. This is what allows Google to identify objects in photos or understand spoken words in its voice-recognition app.

#### **Theano is also for Deep Learning**

![Image](https://cdn-media-1.freecodecamp.org/images/e-jPhWk8t0PSdEJeLtt9F32FroB1fiLfZbEo)

[Theano](http://www.deeplearning.net/software/theano/) is another good Python library for numerical computation, and is similar to NumPy. Theano allows you to define, optimize, and evaluate mathematical expressions involving multi-dimensional arrays efficiently.

What sets Theano apart is that it takes advantage of the computer’s GPU. This allows it to make data-intensive calculations up to 100 times faster than when run on the CPU alone. Theano’s speed makes it especially valuable for deep learning and other computationally complex tasks.

The final release of Theano library was last year — 2017, version 1.0.0 with a lot of new features, interface changes and improvements.

#### **Pandas for data extraction and preparation**

Pandas is a very popular library that provides high-level data structures which are simple to use as well as intuitive.

It has many inbuilt methods for grouping, combining data and filtering as well as performing time series analysis.

Pandas can easily fetch data from different sources like SQL databases, CSV, Excel, JSON files and manipulate the data to perform operations on it. There are two main structures in the library:

* “Series” — one dimensional

![Image](https://cdn-media-1.freecodecamp.org/images/XOnqsPFM6zmV3Yy6Sgs5palSmfHxMJLK-JYz)

* “Data Frames” — two dimensional.

![Image](https://cdn-media-1.freecodecamp.org/images/c6PpmB9g6ixbMmmYm8YfhmT7bc4Vx2IepqTe)

For more details on how to use Series and Dataframes, check out my other [blog post](https://medium.freecodecamp.org/series-and-dataframe-in-python-a800b098f68).

#### **Matplotlib for data visualization**

![Image](https://cdn-media-1.freecodecamp.org/images/NqFp4qWaItpXVSCaxGyIMQbmZRaKFn6Pcbrd)
_Image source: [https://github.com/nschloe/matplotlib2tikz](https://github.com/nschloe/matplotlib2tikz" rel="noopener" target="_blank" title=")_

The best and most sophisticated ML is meaningless if you can’t communicate it to other people.

So how do you actually turn around value from all this data that you have? How do you inspire your business analysts and tell them “stories” full of “insights”?

This is where [Matplotlib](https://matplotlib.org/tutorials/index.html) comes to the rescue. It is a standard Python library used by every data scientist for creating 2D plots and graphs. It’s pretty low-level, meaning it requires more commands to generate nice-looking graphs and figures than with some advanced libraries.

However, the flip side of that is flexibility. With enough commands, you can make just about any kind of graph you want with Matplotlib. You can build diverse charts, from histograms and scatterplots to non-Cartesian coordinates graphs.

It supports different GUI backends on all operating systems, and can also export graphics to common vector and graphic formats like PDF, SVG, JPG, PNG, BMP, GIF, etc.

#### **Seaborn is another data visualization library**

![Image](https://cdn-media-1.freecodecamp.org/images/03MXWUZOfFO2MzbzTQntDwMZcLVe79gpJuos)
_Image source: [seaborn.pydata.org/](https://seaborn.pydata.org/" rel="noopener" target="_blank" title=")_

[Seaborn](https://seaborn.pydata.org/tutorial.html) is a popular visualization library that builds on Matplotlib’s foundations. It is a higher-level library, meaning it’s easier to generate certain kinds of plots, including heat maps, time series, and violin plots.

### Conclusion

This is a collection of the most important Python libraries for Machine Learning. These libraries are worth looking at as well as getting familiarized with, if you plan to work with Python and data science.

Did I miss any important Python ML Library ? If so, please make sure to mention it in the comments below. Even though I tried to cover the most useful libraries, I may still not cover some others that deserve to be looked at.

Questions or feedback? I’d love to hear from you — please feel free to leave out a comment, or connect with me on T[witter](https://twitter.com/shubhi_asthana)/[Linkedin](https://www.linkedin.com/in/shubhi-asthana/).

