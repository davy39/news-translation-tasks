---
title: How to Benchmark Machine Learning Execution Speed
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-25T11:23:11.000Z'
originalURL: https://freecodecamp.org/news/benchmarking-machine-learning-execution-speeds
coverImage: https://www.freecodecamp.org/news/content/images/2019/11/gpu.jpg
tags:
- name: data analysis
  slug: data-analysis
- name: Machine Learning
  slug: machine-learning
seo_title: null
seo_desc: "By Pier Paolo Ippolito\nIntroduction\nThanks to recent advances in storage\
  \ capacity and memory management, it has become much easier to create machine learning\
  \ and deep learning projects from the comfort of your own home. \nIn this article,\
  \ I will intro..."
---

By Pier Paolo Ippolito

## Introduction

Thanks to recent advances in storage capacity and memory management, it has become much easier to create machine learning and deep learning projects from the comfort of your own home. 

In this article, I will introduce you to different possible approaches to machine learning projects in Python and give you some indications on their trade-offs in execution speed. Some of the different approaches are:

* Using a personal computer/laptop CPU (Central processing unit)/GPU (Graphics processing unit).
* Using cloud services (Kaggle, Google Colab).

First of all, we need to import all the necessary dependencies:

```python
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from xgboost import XGBClassifier
import xgboost as xgb
from sklearn.metrics import accuracy_score
```

For this example, I decided to fabricate a simple dataset using Gaussian Distributions consisting of four features and two labels (0/1):

```python
# Creating a linearly separable dataset using Gaussian Distributions.
# The first half of the number in Y is 0 and the other half 1.
# Therefore I made the first half of the 4 features quite different from
# the second half of the features (setting the value of the means quite 
# similar) so that make quite simple the classification between the 
# classes (the data is linearly separable).
dataset_len = 40000000
dlen = int(dataset_len/2)
X_11 = pd.Series(np.random.normal(2,2,dlen))
X_12 = pd.Series(np.random.normal(9,2,dlen))
X_1 = pd.concat([X_11, X_12]).reset_index(drop=True)
X_21 = pd.Series(np.random.normal(1,3,dlen))
X_22 = pd.Series(np.random.normal(7,3,dlen))
X_2 = pd.concat([X_21, X_22]).reset_index(drop=True)
X_31 = pd.Series(np.random.normal(3,1,dlen))
X_32 = pd.Series(np.random.normal(3,4,dlen))
X_3 = pd.concat([X_31, X_32]).reset_index(drop=True)
X_41 = pd.Series(np.random.normal(1,1,dlen))
X_42 = pd.Series(np.random.normal(5,2,dlen))
X_4 = pd.concat([X_41, X_42]).reset_index(drop=True)
Y = pd.Series(np.repeat([0,1],dlen))
df = pd.concat([X_1, X_2, X_3, X_4, Y], axis=1)
df.columns = ['X1', 'X2', 'X3', 'X_4', 'Y']
df.head()
```

![Image](https://www.freecodecamp.org/news/content/images/2019/11/image-32.png)
_Figure 1: Example Dataset_

Finally, now we just have to prepare our dataset to be fed into a machine learning model (dividing it into features and labels, and training and test sets):

```python
train_size = 0.80
X = df.drop(['Y'], axis = 1).values
y = df['Y']

# label_encoder object knows how to understand word labels. 
label_encoder = preprocessing.LabelEncoder() 

# Encode labels
y = label_encoder.fit_transform(y) 

# identify shape and indices
num_rows, num_columns = df.shape
delim_index = int(num_rows * train_size)

# Splitting the dataset in training and test sets
X_train, y_train = X[:delim_index, :], y[:delim_index]
X_test, y_test = X[delim_index:, :], y[delim_index:]

# Checking sets dimensions
print('X_train dimensions: ', X_train.shape, 'y_train: ', y_train.shape)
print('X_test dimensions:', X_test.shape, 'y_validation: ', y_test.shape)

# Checking dimensions in percentages
total = X_train.shape[0] + X_test.shape[0]
print('X_train Percentage:', (X_train.shape[0]/total)*100, '%')
print('X_test Percentage:', (X_test.shape[0]/total)*100, '%')
```

The output train test split result is shown below:

```
X_train dimensions:  (32000000, 4) y_train:  (32000000,)
X_test dimensions: (8000000, 4) y_validation:  (8000000,)
X_train Percentage: 80.0 %
X_test Percentage: 20.0 %
```

We are now ready to get started benchmarking the different approaches. In all the following examples, we will be using [XGBoost (Gradient Boosted Decision Trees)](https://towardsdatascience.com/https-medium-com-vishalmorde-xgboost-algorithm-long-she-may-rein-edd9f99be63d) as our classifier.

## 1) CPU

Training an XGBClassifier on my personal machine (without using a GPU), led to the following results:

```python
%%time

model = XGBClassifier(tree_method='hist')
model.fit(X_train, y_train)
```

```
CPU times: user 8min 1s, sys: 5.94 s, total: 8min 7s
Wall time: 8min 6s
XGBClassifier(base_score=0.5, booster='gbtree', colsample_bylevel=1,
              colsample_bynode=1, colsample_bytree=1, gamma=0,
              learning_rate=0.1, max_delta_step=0, max_depth=3,
              min_child_weight=1, missing=None, n_estimators=100, n_jobs=1,
              nthread=None, objective='binary:logistic', random_state=0,
              reg_alpha=0, reg_lambda=1, scale_pos_weight=1, seed=None,
              silent=None, subsample=1, tree_method='hist', verbosity=1)
```

Once we've trained our model, we can now check it's prediction accuracy:

```python
sk_pred = model.predict(X_test)
sk_pred = np.round(sk_pred)
sk_acc = round(accuracy_score(y_test, sk_pred), 2)
print("XGB accuracy using Sklearn:", sk_acc*100, '%')
```

```
XGB accuracy using Sklearn: 99.0 %
```

In summary, using a standard CPU machine, it took about 8 minutes to train our classifier to achieve 99% accuracy.

## 2) GPU

I will now instead make use of an [NVIDIA TITAN RTX GPU](https://www.nvidia.com/en-gb/deep-learning-ai/products/titan-rtx/) on my personal machine to speed up the training. In this case, in order to activate the GPU mode of XGB, we need to specify the **_tree_method_** as **_gpu_hist_** instead of **_hist_**. 

```
%%time

model = XGBClassifier(tree_method='gpu_hist')
model.fit(X_train, y_train)
```

Using the TITAN RTX led in this example to just 8.85 seconds of execution time (about 50 times faster than using just the CPU!).

```python
sk_pred = model.predict(X_test)
sk_pred = np.round(sk_pred)
sk_acc = round(accuracy_score(y_test, sk_pred), 2)
print("XGB accuracy using Sklearn:", sk_acc*100, '%')
```

```
XGB accuracy using Sklearn: 99.0 %
```

This considerable improvement in speed was possible thanks to the ability of the GPU to take the load off from the CPU, freeing up RAM memory and parallelizing the execution of multiple tasks.

## 3) GPU Cloud Services

I will now go over two examples of free GPU cloud services (Google Colab and Kaggle) and show you what benchmark score they are able to achieve. In both cases, we need to explicitly turn on the GPUs on the respective notebooks and specify the XGBoost **_tree_method_** as **_gpu_hist_**.

### Google Colab

Using Google Colab NVIDIA TESLA T4 GPUs, the following scores have been registered:

```
CPU times: user 5.43 s, sys: 1.88 s, total: 7.31 s
Wall time: 7.59 s
```

### Kaggle

Using Kaggle instead led to a slightly higher execution time:

```
CPU times: user 5.37 s, sys: 5.42 s, total: 10.8 s
Wall time: 11.2 s
XGBClassifier(base_score=0.5, booster='gbtree', colsample_bylevel=1,
              colsample_bynode=1, colsample_bytree=1, gamma=0,
              learning_rate=0.1, max_delta_step=0, max_depth=3,
              min_child_weight=1, missing=None, n_estimators=100, n_jobs=1,
              nthread=None, objective='binary:logistic', random_state=0,
              reg_alpha=0, reg_lambda=1, scale_pos_weight=1, seed=None,
              silent=None, subsample=1, tree_method='gpu_hist', verbosity=1)
```

Using either Google Colab or Kaggle both led to a remarkable decrease in execution time. 

One downside of using these services is the limited amount of CPU and RAM available. In fact, slightly increasing the dimensions of the example dataset caused Google Colab to run out of RAM memory (which wasn't an issue when using the TITAN RTX). 

One possible way to fix this type of problem when working with constrained memory devices is to optimize the code to consume the least amount of memory possible (using fixed point precision and more efficient data structures).

## 4) Bonus Point: RAPIDS

As an additional point, I will now introduce you to RAPIDS, an open-source collection of Python libraries by NVIDIA. In this example, we will make use of its integration with the XGBoost library to speed up our workflow in Google Colab. The full notebook for this example (with instructions on how to set up RAPIDS in Google Colab) is available [here](https://drive.google.com/open?id=1LZzK-iq9xEEuOfEpv2SLeCyV6ksx0kio) or on [my GitHub Account.](https://github.com/pierpaolo28/Artificial-Intelligence-Projects/blob/master/NVIDIA-RAPIDS%20AI/RAPIDS%20GPU%20Benchmark%20Colab.ipynb) 

RAPIDS is designed to be the next evolutionary step in data processing. Thanks to its Apache Arrow in-memory format, RAPIDS can lead to up to around 50x speed improvement compared to Spark in-memory processing. Additionally, it is also able to scale from one to multi-GPUs.

All RAPIDS libraries are based on Python and are designed to have Pandas and Sklearn-like interfaces to facilitate adoption.

The structure of RAPIDS is based on different libraries in order to accelerate data science from end to end. Its main components are:

* cuDF = used to perform data processing tasks (Pandas-like).
* cuML = used to create machine learning models (Sklearn-like).
* cuGraph = used to perform graph analytics (NetworkX).

In this example, we will make use of it's XGBoost integration:

```python
dtrain = xgb.DMatrix(X_train, label=y_train)
dtest = xgb.DMatrix(X_test, label=y_test)

%%time

params = {}
booster_params = {}
booster_params['tree_method'] = 'gpu_hist' 
params.update(booster_params)

clf = xgb.train(params, dtrain)
```

```
CPU times: user 1.42 s, sys: 719 ms, total: 2.14 s
Wall time: 2.51 s
```

As we can see above, using RAPIDS it took just about 2.5 seconds to train our model (decreasing time execution by almost 200 times!). 

Finally, we can now check that we obtained exactly the same prediction accuracy using RAPIDS that we registered in the other cases:

```
rapids_pred = clf.predict(dtest)

rapids_pred = np.round(rapids_pred)
rapids_acc = round(accuracy_score(y_test, rapids_pred), 2)
print("XGB accuracy using RAPIDS:", rapids_acc*100, '%')
```

```
XGB accuracy using RAPIDS: 99.0 %
```

If you are interested in finding out more about RAPIDS, more information is available [here.](https://towardsdatascience.com/gpu-accelerated-data-analytics-machine-learning-963aebe956ce)

## Conclusion

Finally, we can now compare the execution time of the different methods used. As shown in Figure 2, using GPU optimization can substantially decrease execution time, especially if integrated with the use of RAPIDS libraries.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/image-37.png)
_Figure 2: Execution Time comparison_

Figure 3 shows how many times faster the GPUs models are compared to our baseline CPU results.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/image-38.png)
_Figure 3: Focus on CPU Execution Time Comparison_

## Contacts

If you want to keep updated with my latest articles and projects, [follow me on Medium](https://medium.com/@pierpaoloippolito28?source=post_page---------------------------) and subscribe to my [mailing list](http://eepurl.com/gwO-Dr?source=post_page---------------------------). These are some of my contacts details:

* [Linkedin](https://uk.linkedin.com/in/pier-paolo-ippolito-202917146?source=post_page---------------------------)
* [Personal Blog](https://pierpaolo28.github.io/blog/?source=post_page---------------------------)
* [Personal Website](https://pierpaolo28.github.io/?source=post_page---------------------------)
* [Medium Profile](https://towardsdatascience.com/@pierpaoloippolito28?source=post_page---------------------------)
* [GitHub](https://github.com/pierpaolo28?source=post_page---------------------------)
* [Kaggle](https://www.kaggle.com/pierpaolo28?source=post_page---------------------------)

Cover photo [from this article](https://hardzone.es/noticias/tarjetas-graficas/nvidia-hopper-arquitectura-mcm/).

