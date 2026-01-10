---
title: Weka Tutorial – GUI-based Machine Learning with Java
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-27T20:37:30.000Z'
originalURL: https://freecodecamp.org/news/machine-learning-using-weka
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/weka-1.png
tags:
- name: Data Science
  slug: data-science
- name: Java
  slug: java
- name: Machine Learning
  slug: machine-learning
seo_title: null
seo_desc: "By Pier Paolo Ippolito\nNowadays, programming languages such as Python\
  \ and R are undoubtedly some of the most in-demand languages in Data Science and\
  \ Machine Learning. \nBut is it also possible to perform common Machine Learning\
  \ and Data Science tasks ..."
---

By Pier Paolo Ippolito

Nowadays, programming languages such as Python and R are undoubtedly some of the most in-demand languages in Data Science and Machine Learning. 

But is it also possible to perform common Machine Learning and Data Science tasks without necessarily being proficient in coding? 

Of course it is! Weka is a Graphical User Interface-based open-source package. It can be used in order to perform common Data Science tasks just by using the graphical interface.

## Basics

Weka can be easily installed on any type of platform by following the instructions at the following [link](https://waikato.github.io/weka-wiki/downloading_weka/). The only pre-requisite is having Java 8.0 installed on your local machine.

Once you've installed Weka, you will have a set of standard data processing and inference techniques such as:

* **Data Pre-processing**: once you've loaded a dataset, Weka enables you to quickly explore its attributes and instances. Additionally, different filtering techniques are available in order to, for example, convert categorical data into numerical or perform [feature selection](https://towardsdatascience.com/feature-selection-techniques-1bfab5fe0784) in order to reduce the dimensionality of our dataset (eg. to speed up training times and performance). 
* **Classification and Regression Algorithms:** a collection of different algorithms such as Gaussian Naive Bayes, Decision Trees, K-Nearest Neighbour, Ensembles techniques, and various linear regression variants.
* **Clustering:** this technique can be used in order to identify the main categories in our data in an unsupervised way. Some example algorithms available in the Weka collection are K-Means Clustering and Expectation Maximisation.
* **Discovering Associations:** discovering rules in our dataset in order to more easily identify patterns and connections between the different features.
* **Data Visualisation:** a suite of integrated data visualisation techniques to quickly visualise correlations between features and represent learned machine learning patterns such as Decision Trees and K-Means Clustering.

Another interesting feature of Weka is the ability to install new packages as they are created. 

One example of an additional package you can install is AutoML. AutoML can in fact be particularly useful for beginners who might find it difficult to identify what Machine Learning model might be best to use for a specific task. 

Using the Weka AutoML package, you can easily test different Machine Learning models on the fly. It also allows you to auto-tune its [hyper-parameters](https://towardsdatascience.com/hyperparameters-optimization-526348bb8e2d) in order to increase performance. 

Finally, for more expert users, Weka also offers a command line interface to use Java code. This can be particularly useful especially if you're working with large amounts of data.

## Example

We are now going to walk through a simple example in order to demonstrate how to get started with Weka. 

First of all, we can start our analysis by opening Weka Explorer and opening our dataset (in this example, the Iris Dataset).

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-153.png)
_Figure 1: Importing and Visualising the data_

Select the Classify tab, choose Naive Bayes as our classifier, and click start. You'll see that we can quickly achieve 96% classification accuracy without having to write any code!

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-154.png)
_Figure 2: Naive Bayes Classification Results_

## Conclusion

In case you are looking for more information about how to get started with Weka, [this YouTube series](https://www.youtube.com/watch?v=cKxRvEZd3Mw&list=PLOU2XLYxmsIIuiBfYad6rFYQU_jL2ryal) by Google Developers is a great place to start.

### Contact me

If you want to keep updated with my latest articles and projects, [follow me on Medium](https://medium.com/@pierpaoloippolito28?source=post_page---------------------------) and subscribe to my [mailing list](http://eepurl.com/gwO-Dr?source=post_page---------------------------). These are some of my contacts details:

* [Linkedin](https://uk.linkedin.com/in/pier-paolo-ippolito-202917146?source=post_page---------------------------)
* [Personal Blog](https://pierpaolo28.github.io/blog/?source=post_page---------------------------)
* [Personal Website](https://pierpaolo28.github.io/?source=post_page---------------------------)
* [Medium Profile](https://towardsdatascience.com/@pierpaoloippolito28?source=post_page---------------------------)
* [GitHub](https://github.com/pierpaolo28?source=post_page---------------------------)
* [Kaggle](https://www.kaggle.com/pierpaolo28?source=post_page---------------------------)

Cover photo [from this article](https://www.techiexpert.com/list-of-data-mining-tools/).

