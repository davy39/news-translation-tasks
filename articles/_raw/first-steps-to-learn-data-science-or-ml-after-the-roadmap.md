---
title: Programming, Math, and Statistics You Need to Know for Data Science and Machine
  Learning
subtitle: ''
author: Harshit Tyagi
co_authors: []
series: null
date: '2021-08-20T03:21:20.000Z'
originalURL: https://freecodecamp.org/news/first-steps-to-learn-data-science-or-ml-after-the-roadmap
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-14-at-3.08.07-AM.png
tags: []
seo_title: null
seo_desc: 'At the start of this year, I published a mind map on the Data Science learning
  roadmap (shown below). Many people found the roadmap useful, my article got translated
  into different languages, and a large number of folks thanked me for publishing
  it.

  ...'
---

At the start of this year, I published a mind map on the [Data Science learning roadmap (shown below)](https://www.freecodecamp.org/news/data-science-learning-roadmap/). Many people found the roadmap useful, my article got translated into different languages, and a large number of folks thanked me for publishing it.

Everything was good until a few developers pointed out that there are too many resources and many of them are expensive. Python programming was the only branch that had a number of really good courses but it ends right there for beginners.

A few important questions on foundational data science struck me:

* What should you do after learning how to code? Are there topics that help you strengthen your foundations for data science?
    
* What if you hate math and tutorials out there are either too basic tutorials or too deep? Could I recommend a compact yet comprehensive course on Math and Statistics?
    
* How much Math is enough to start learning how ML algorithms work?
    
* What are some essential statistics topics to get started with data analysis or data science?
    

You can find answers to a lot of these questions in the book [Deep Learning](https://www.deeplearningbook.org/) by **Ian Goodfellow and Yoshua Bengio.** But that book is a bit too technical and math heavy for many.

So in this article, I'll lay out some of the first steps you should take to learn Data Science or Machine Learning.

## The Three Pillars of Data Science and Machine Learning

![Image](https://www.freecodecamp.org/news/content/images/2021/08/pillars_ds.png align="left")

*Source:* [*wiplane.com*](wiplane.com)

If you go through the prerequisites or pre-work of any ML/DS course, you’ll find a combination of programming, math, and statistics.

Here is what [Google recommends](https://developers.google.com/machine-learning/crash-course/prereqs-and-prework) that you do before taking an ML course:

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-18-at-5.42.43-PM.png align="left")

*Google's recommended Python skills for Data Science and Machine Learning*

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-18-at-5.42.34-PM.png align="left")

*Google's recommended Math and Statistics skills for ML and DS (*[*Source*](https://developers.google.com/machine-learning/crash-course/prereqs-and-prework)*)*

Let's go through these essential skills in a bit more detail to see what you need to learn to get into Data Science and Machine Learning.

## Essential Programming Skills for Data Science and Machine Learning

Most data roles are programming-based, except for a few like business intelligence, market analysis, product analyst, and others.

I am going to focus on technical data jobs that require expertise in at least one programming language.

I personally prefer Python over any other language because of its versatility how relatively easy it is to learn. Hands down a good pick for developing end-to-end projects.

### Topics and libraries to know for data science:

* **Common data structures** (data types, lists, dictionaries, sets, tuples), writing functions, logic, control flow, searching and sorting algorithms, object-oriented programming, and working with external libraries.
    
* **Writing Python scripts to extract**, format, and store data into files or back to databases.
    
* **Handling multi-dimensional arrays**, indexing, slicing, transposing, broadcasting and pseudorandom number generation using NumPy.
    
* Performing vectorized operations using scientific computing libraries like NumPy.
    
* **Manipulating data with Pandas** — series, dataframe, indexing in a dataframe, comparison operators, merging dataframes, mapping and applying functions.
    
* **Wrangling data using Pandas** — checking for null values, imputing it, grouping data, describing it, performing exploratory analysis, and so on.
    
* **Data Visualization using Matplotlib** — the API hierarchy, how to add styles, color, and markers to a plot, knowledge of various plots and when to use them, line plots, bar plots, scatter plots, histograms, boxplots, and Seaborn for more advanced plotting.
    

## Essential Mathematics for Data Science and Machine Learning

There are [practical reasons for why math is essential](https://towardsdatascience.com/practical-reasons-to-learn-mathematics-for-data-science-1f6caec161ea) for folks who want a career as an ML practitioner, Data Scientist, or a Deep Learning Engineer.

### You'll Use Linear Algebra to Represent Data

![Image](https://www.freecodecamp.org/news/content/images/2021/08/IMG_0063.JPG align="left")

*An image from the lecture on Vector Norms (*[*from this course*](https://www.wiplane.com/p/foundations-for-data-science-ml)*)*

ML is inherently data-driven. Data is at the heart of machine learning. We can think of data as **vectors —** an object that adheres to arithmetic rules. This leads us to understand how rules of linear algebra operate over arrays of data.

### You'll Use Calculus to Train ML Models

![Image](https://www.freecodecamp.org/news/content/images/2021/08/IMG_0065.JPG align="left")

Model training doesn't happen “automatically”. Calculus drives the learning of most ML and DL algorithms.

One of the most commonly used optimization algorithms — **gradient descent**–is an application of partial derivatives.

A model is a mathematical representation of certain beliefs and assumptions. It learns (approximately) the process (linear, polynomial, etc) of how the data is provided, and how it was generated in the first place. It then make predictions based on that learned process.

### Important Math Topics to Know for Data Science and Machine Learning:

* **Basic algebra —** variables, coefficients, equations, functions — linear, exponential, logarithmic, and so on.
    
* **Linear Algebra —** scalars, vectors, tensors, Norms (L1 & L2), dot product, types of matrices, linear transformation, representing linear equations in matrix notation, solving linear regression problem using vectors and matrices.
    
* **Calculus —** derivatives and limits, derivative rules, chain rule (for backpropagation algorithm), partial derivatives (to compute gradients), convexity of functions, local/global minima, math behind a regression model, applied math for training a model from scratch.
    

## Essential Statistics for Data Science and Machine Learning

Every organisation today is striving to become data-driven. To achieve that, data analysts and scientists need to put their data to use in different ways in order to drive their decision making.

### How to describe data — from data to insights

Data always comes in raw and ugly. The initial exploration tells you what’s missing, how the data is distributed, and what’s the best way to clean it to meet the end goal.

In order to answer the defined questions, descriptive statistics enables you to transform each observation in your data into insights that make sense.

### How to quantify uncertainty

You also need to be able to quantify uncertainty, and this is an extremely valuable skill that is highly regarded at any data company. Knowing the chances of success in any experiment/decision is critical for all businesses.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/stats_dist.png align="left")

### Basic statistics to know for Data Science and Machine Learning:

* Estimates of location — mean, median and other variants of these.
    
* Estimates of variability
    
* Correlation and covariance
    
* Random variables — discrete and continuous
    
* Data distributions— PMF, PDF, CDF
    
* Conditional probability — bayesian statistics
    
* Commonly used statistical distributions — Gaussian, Binomial, Poisson, Exponential.
    
* Important theorems — Law of large numbers and Central limit theorem.
    

![Image](https://www.freecodecamp.org/news/content/images/2021/08/IMG_0074.JPG align="left")

*Image from the lecture on Poisson distribution (*[*from this course*](https://www.wiplane.com/p/foundations-for-data-science-ml)*)*

* **Inferential Statistics —** A more practical and advanced branch of statistics that helps in designing hypothesis testing experiments, pushes us to understand the meaning of metrics deeply and at the same time helps us in quantifying the significance of the results.
    
* **Important tests —** Student’s t-Test, Chi-Square test, ANOVA test, and so on.
    

And there you have it. Every beginner-level data science enthusiast should focus on these three pillars before diving into any core data science or ML courses.

## Resources to Learn Data Science and Machine Learning Fundamentals

![Image](https://www.freecodecamp.org/news/content/images/2021/08/ds_roadmap.png align="left")

*\[https://www.freecodecamp.org/news/data-science-learning-roadmap/\](https://www.freecodecamp.org/news/data-science-learning-roadmap/" rel="nofollow noopener)*

[My learning roadmap](https://towardsdatascience.com/data-science-learning-roadmap-for-2021-84f2ba09a44f) also told you what to learn, and it was loaded up with resources, courses, and programs that you can take to learn those skills.

But there are a few inconsistencies in the recommended resources and the roadmap that I had charted out. And many people were searching for a compact, comprehensive, yet affordable course.

### Problems with Data Science or ML Courses

1. Every data science course that I recommended in that article required that you have a decent understanding of Programming, Math, or Statistics. For example, [the most famous course on ML by Andrew Ng](https://www.youtube.com/watch?v=PPLop4L2eGk&list=PLLssT5z_DsK-h9vYZkQkYNWcItqhlRJLN) also relies heavily on students' understanding of vector algebra and calculus.
    
2. Most courses that cover Math and Statistics for Data Science are just a checklist of concepts required for DS/ML with no explanation on how they are applied and how they are programmed into a machine.
    
3. There are exceptional resources to dive deep into Math but most of us are not made for it and you don't need to be a gold medalist in math to learn data science.
    

**Bottom line:** a resource that covers just enough applied math or statistics or programming to get started with data science or ML is missing.

### Wiplane Academy — wiplane.com

So, I decided to give in and do it all myself. I have spent the last 3 months developing a curriculum that will provide a solid foundation for your career as a

* Data Analyst
    
* Data Scientist
    
* ML Practitioner/Engineer
    

Hence, here I present you the [**Foundations for Data Science or ML**](https://www.wiplane.com/p/foundations-for-data-science-ml) **—** [**First Steps to learn Data Science and ML**](https://www.wiplane.com/p/foundations-for-data-science-ml)

![Image](https://www.freecodecamp.org/news/content/images/2021/08/IMG_0723.JPG align="left")

*That's me when I decided to launch.*

It's a comprehensive yet compact and affordable course that not only covers **all the essentials, pre-requisites, and pre-work** but also explains how each concept is used **computationally and programmatically (in Python)**.

And that’s not it – I will keep updating the course content every month based on your input.

Learn more [here](https://www.wiplane.com/p/foundations-for-data-science-ml).

#### Early Bird Offer!

I am stoked to launch the pre-sale of this course as I am currently in the process of recording and editing the final bits of 2–3 modules (15-20 lectures). These will also be live by the first week of September.

Grab the early bird offer, only valid until August 30th, 2021.
