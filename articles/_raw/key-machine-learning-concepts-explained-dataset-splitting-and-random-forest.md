---
title: Key Machine Learning Concepts Explained  —  Dataset Splitting and Random Forest
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/key-machine-learning-concepts-explained-dataset-splitting-and-random-forest
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d17740569d1a4ca35d9.jpg
tags:
- name: Machine Learning
  slug: machine-learning
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'Dataset Splitting

  Splitting up into Training, Cross Validation, and Test sets are common best practices.
  This allows you to tune various parameters of the algorithm without making judgements
  that specifically conform to training data.

  Motivation

  Data...'
---

## **Dataset Splitting**

Splitting up into Training, Cross Validation, and Test sets are common best practices. This allows you to tune various parameters of the algorithm without making judgements that specifically conform to training data.

### **Motivation**

Dataset Splitting emerges as a necessity to eliminate bias to training data in ML algorithms. Modifying parameters of a ML algorithm to best fit the training data commonly results in an overfit algorithm that performs poorly on actual test data. For this reason, we split the dataset into multiple, discrete subsets on which we train different parameters.

#### **The Training Set**

The Training set is used to compute the actual model your algorithm will use when exposed to new data. This dataset is typically 60%-80% of your entire available data (depending on whether or not you use a Cross Validation set).

#### **The Cross Validation Set**

Cross Validation sets are for model selection (typically ~20% of your data). Use this dataset to try different parameters for the algorithm as trained on the Training set. For example, you can evaluate different model parameters (polynomial degree or lambda, the regularization parameter) on the Cross Validation set to see which may be most accurate.

#### **The Test Set**

The Test set is the final dataset you touch (typically ~20% of your data). It is the source of truth. Your accuracy in predicting the test set is the accuracy of your ML algorithm.

## Random Forest

A Random Forest is a group of decision trees that make better decisions as a whole than individually.

### **Problem**

Decision trees by themselves are prone to **overfitting**. This means that the tree becomes so used to the training data that it has difficulty making decisions for data it has never seen before.

### **Solution with Random Forests**

Random Forests belong in the category of **ensemble learning** algorithms. This class of algorithms use many estimators to yield better results. This makes Random Forests usually **more accurate** than plain decision trees. In Random Forests, a bunch of decision trees are created. Each tree is **trained on a random subset of the data and a random subset of the features of that data**. This way the possibility of the estimators getting used to the data (overfitting) is greatly reduced, because **each of them work on the different data and features** than the others. This method of creating a bunch of estimators and training them on random subsets of data is a technique in _ensemble learning_ called **bagging** or _Bootstrap AGGregatING_. To get the prediction, the each of the decision trees vote on the correct prediction (classification) or they get the mean of their results (regression).

### **Example of Boosting in Python**

In this competition, we are given a list of collision events and their properties. We will then predict whether a τ → 3μ decay happened in this collision. This τ → 3μ is currently assumed by scientists not to happen, and the goal of this competition was to discover τ → 3μ happening more frequently than scientists currently can understand. The challenge here was to design a machine learning problem for something no one has ever observed before. Scientists at CERN developed the following designs to achieve the goal. [https://www.kaggle.com/c/flavours-of-physics/data](https://www.kaggle.com/c/flavours-of-physics/data)

```python
#Data Cleaning
import pandas as pd
data_test = pd.read_csv("test.csv")
data_train = pd.read_csv("training.csv")
data_train = data_train.drop('min_ANNmuon',1)
data_train = data_train.drop('production',1)
data_train = data_train.drop('mass',1)

#Cleaned data
Y = data_train['signal']
X = data_train.drop('signal',1)

#adaboost
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
seed = 9001 #this ones over 9000!!!
boosted_tree = AdaBoostClassifier(DecisionTreeClassifier(max_depth=1), algorithm="SAMME", 
                                  n_estimators=50, random_state = seed)
model = boosted_tree.fit(X, Y)

predictions = model.predict(data_test)
print(predictions)
#Note we can't really validate this data since we don't have an array of "right answers"

#stochastic gradient boosting
from sklearn.ensemble import GradientBoostingClassifier
gradient_boosted_tree = GradientBoostingClassifier(n_estimators=50, random_state=seed)
model2 = gradient_boosted_tree.fit(X,Y)

predictions2 = model2.predict(data_test)
print(predictions2)
```

