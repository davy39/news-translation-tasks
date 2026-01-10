---
title: Two hours later and still running? How to keep your sklearn.fit under control.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-13T15:36:10.000Z'
originalURL: https://freecodecamp.org/news/two-hours-later-and-still-running-how-to-keep-your-sklearn-fit-under-control-cc603dc1283b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*aVzJTznRRfP1lM7AXe9yLw.jpeg
tags:
- name: Data Sc
  slug: data-sc
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
- name: scikit learn
  slug: scikit-learn
- name: timer
  slug: timer
seo_title: null
seo_desc: 'By Nathan Toubiana

  Written by Gabriel Lerner and Nathan Toubiana

  All you wanted to do was test your code, yet two hours later your Scikit-learn fit
  shows no sign of ever finishing. Scitime is a package that predicts the runtime
  of machine learning al...'
---

By Nathan Toubiana

_Written by [Gabriel Lerner](https://medium.com/@gabi10004) and [Nathan Toubiana](https://medium.com/@toubiana.nathan)_

All you wanted to do was test your code, yet two hours later your Scikit-learn fit shows no sign of ever finishing. Scitime is a package that predicts the runtime of machine learning algorithms so that you will not be caught off guard by an endless fit.

![Image](https://cdn-media-1.freecodecamp.org/images/1*aVzJTznRRfP1lM7AXe9yLw.jpeg)
_Image by Kevin Ku on [unsplash.com](https://unsplash.com/photos/aiyBwbrWWlo" rel="noopener" target="_blank" title=")_

Whether you are in the process of building a machine learning model or deploying your code to production, knowledge of how long your algorithm will take to fit is key to streamlining your workflow. With Scitime you will be able in a matter of seconds to estimate how long the fit should take for the most commonly used Scikit Learn algorithms.

There have been a couple of research articles (such as [this one](https://www.sciencedirect.com/science/article/pii/S0004370213001082)) published on that subject. However, as far as we know, there’s no practical implementation of it. The goal here is not to predict the exact runtime of the algorithm but more to give a rough approximation.

### What is Scitime?

Scitime is a python package requiring at least python 3.6 with [pandas](https://github.com/pandas-dev/pandas), [scikit-learn](https://github.com/scikit-learn/scikit-learn), [psutil](https://github.com/giampaolo/psutil) and [joblib](https://github.com/joblib/joblib) dependencies. You will find the Scitime repo [here](https://github.com/nathan-toubiana/scitime).

The main function in this package is called “_time_”. Given a matrix vector X, the estimated vector Y along with the Scikit Learn model of your choice, _time_ will output both the estimated time and its confidence interval. The package currently supports the following Scikit Learn algorithms with plans to add more in the near future:

* [KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)
* [RandomForestRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html)
* [SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html)
* [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)

### Quick Start

Let’s install the package and run the basics.

First create a new virtualenv (this is optional, to avoid any version conflicts!)

```
❱ virtualenv env❱ source env/bin/activate
```

and then run:

```
❱ (env) pip install scitime
```

or with conda:

```
❱ (env) conda install -c conda-forge scitime
```

Once the installation has succeeded, you are ready to estimate the time of your first algorithm.

Let’s say you wanted to train a kmeans clustering, for example. You would first need to import the scikit-learn package, set the kmeans parameters, and also choose the inputs (a.k.a _X)_, here generated [randomly](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs) for simplicity.

Running this before doing the actual fit would give an approximation of the runtime:

As you can see, you can get this info only in one extra line of code! The inputs of the _time_ function are exactly what’s needed to run the fit (that is the algo itself, and X), which makes it even easier to use.

Looking more closely at the last line of the above code, the first output (_estimation:_ 15 seconds in this case) is the predicted runtime you’re looking for. Scitime will also output it with a confidence interval (_lower_bound_ and _upper_bound:_ 10 and 30 seconds in this case). You can always compare it to the actual training time by running:

In this case, on our local machine, the estimation is 15 seconds, whereas the actual training time is 20 seconds (but you might not get the same results, as we’ll explain later).

**As a quick usage guide:**

_Estimator(meta_algo, verbose, confidence) class:_

* **meta_algo**: The estimator used to predict the time, either ‘RF’ or ‘NN’ (see details in next paragraph) — defaults to‘RF’
* **verbose**: Control of the amount of log output (either 0, 1, 2 or 3) — defaults to 0
* **confidence**: Confidence for intervals — defaults to 95%

_estimator.time(algo, X, y) function:_

* **algo**: algo whose runtime the user wants to predict
* **X**: numpy array of inputs to be trained
* **y**: numpy array of outputs to be trained (set to _None_ if the algo is unsupervised)

Quick note: to avoid any confusion, it’s worth highlighting that **algo** and **meta_algo** are two different things here: **algo** is the algorithm whose runtime we want to estimate, **meta_algo** is the algorithm used by Scitime to predict the runtime.

### How Scitime works

We are able to predict the runtime to fit by using our own estimator, we call it meta algorithm (_meta_algo_), whose weights are stored in a dedicated pickle file in the package metadata. For each Scikit Learn model, you will find a corresponding meta algo pickle file in Scitime’s code base.

You might be thinking:

> Why not manually estimate the time complexity with big O notations?

That’s a fair point. It’s a valid way of approaching the problem and something we thought about at the beginning of the project. One thing however is that we would need to formulate the complexity explicitly for each algo and set of parameters which is rather challenging in some cases, given the number of factors playing a role in the runtime. The meta_algo basically does all the work for you, and we’ll explain how.

Two types of meta algos have been trained to estimate the time to fit (both from Scikit Learn):

* The **RF** meta algo, a [RandomForestRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html) estimator.
* The **NN** meta algo, a basic [MLPRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html) estimator.

These meta algos estimate the time to fit using an array of ‘meta’ features. Here’s a summary of how we build these features:

Firstly, we fetch the shape of your input matrix X and output vector y. Second, the parameters you feed to the Scikit Learn model are taken into consideration as they will impact the training time as well. Lastly, your specific hardware, unique to your machine such as available memory and cpu counts are also considered.

As shown earlier, we also provide confidence intervals on the time prediction. The way these are computed depends on the meta algo chosen:

* For **RF**, since any random forest regressor is a combination of multiple trees (also called _estimators_), the confidence interval will be based on the distribution of the set of predictions computed by each estimator.
* For **NN**, the process is a little less straightforward: we first compute a set of [MSE](https://en.wikipedia.org/wiki/Mean_squared_error)s along with the number of observations on a test set, grouped by predicted duration bins (that is from 0 to 1 second, 1 to 5 seconds, and so on), and we then compute a [t-stat](https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.stats.t.html) to get the lower and upper bounds of the estimation. As we don’t have a lot of data for very long models, the confidence interval for such data might get very broad.

### How we built it

You might be thinking:

> How did you get enough data on the training time of all these sciki- learn fits over various parameters and hardware configurations?

The (unglamorous) answer is we generated the data ourselves using a combination of computers and VM hardwares to simulate what the training time would be on the different systems. We then fitted our meta algos on these randomly generated data points to build an estimator meant to be reliable regardless of your system.

While the [estimate.py](https://github.com/nathan-toubiana/scitime/blob/master/scitime/estimate.py) file handles the runtime prediction, the [__model.py_](https://github.com/nathan-toubiana/scitime/blob/master/scitime/_model.py) file helped us generate data to train our meta algos, using our dedicated Model class. Here’s a corresponding code sample, for kmeans:

Note that you can also use the file [__data.py_](https://github.com/nathan-toubiana/scitime/blob/master/_data.py) directly with the command line to generate data or train a new model. Related instructions can be found in the repo Readme file.

When generating data points, you can edit the parameters of the Scikit Learn models you want to train on. You can head to [_scitime/_config.json_](https://github.com/nathan-toubiana/scitime/blob/master/scitime/_config.json) and edit the parameters of the models as well as the number of rows and columns you would want to train with.

We use an [itertool](https://docs.python.org/2/library/itertools.html#itertools.product) function to loop through every possible combination, along with a drop rate set between 0 and 1 to control how quickly the loop will jump through the different possible iterations.

### How accurate is Scitime?

Below, we highlight how our predictions perform for the specific case of kmeans. Our generated dataset contains ~100k data points, which we split into a train and test sets (75% — 25%).

We grouped training predicted times by different time buckets and computed the [MAPE](https://en.wikipedia.org/wiki/Mean_absolute_percentage_error) and [RMSE](https://en.wikipedia.org/wiki/Root-mean-square_deviation) over each of those buckets for all our estimators using the RF meta-algo and the NN meta-algo.

Please note that these results were performed on a restricted data set, so they might be different on unexplored data points (such as other systems / extreme values of certain model parameters). For this specific training set, the [R-squared](https://en.wikipedia.org/wiki/Coefficient_of_determination) is around 80% for NN and 90% for RF.

As we can see, not surprisingly, the accuracy is consistently higher on the train set than on the test, for both NN and RF. We also see that RF seems to perform way better than NN overall. The MAPE for RF is around 20% on the train set and 40% on the test set. The NN MAPE is surprisingly very high.

Let’s slice the MAPE (on test set) by the number of predicted seconds:

One important thing to keep in mind is that for some cases the time prediction is sensitive to the meta algo chosen (RF or NN). In our experience RF has performed very well within the data set input ranges, as shown above. However, for out of range points, NN might perform better, as suggested by the end of the above chart. This would explain why NN MAPE is quite high while the RMSE is decent: it performs poorly on small values.

As an example, if you try to predict the runtime of a kmeans with default parameters and with an input matrix of a few thousand lines, the RF meta algo will be precise because our training dataset contains similar data points. However, for predicting very specific parameters (for instance, a very high number of clusters), NN might perform better because it extrapolates from the training set, whereas RF doesn’t. NN performs worse on the above charts because these plots are only based on data close to the set of inputs of the training data.

However, as shown in this graph, the out of range values (thin lines) are extrapolated by the NN estimator, whereas the RF estimator predicts the output stepwise.

Now let’s look at the most important ‘meta’ features for the example of kmeans:

As we can see, only 6 features account for more than 80% of the model variance. Among them, the most important is a parameter of the scikit-learn kmeans class itself (number of clusters), but a lot of external factors have great influence on the runtime such as number of rows/columns and available memory.

### Limitations

As mentioned earlier, the first limitation is related to the confidence intervals: they may be very wide, especially for NN, and for heavy models (that would take at least an hour).

Additionally, the NN might perform poorly on small to medium predictions. Sometimes, for small durations, the NN might even predict a negative duration, in which case we automatically switch back to RF.

Another limitation of the estimator arise for when ‘special’ algo parameter values are used. For example, in a RandomForest scenario, when max_depth is set to _None_, the depth could take any value. This might result in a much longer time to fit which is more difficult for the meta algo to pick up, although we did our best to account for them.

When running _estimator.time(algo, X, y)_ we do require the user to enter the actual X and y vector which seems unnecessary, as we could simply request the shape of the data to estimate the training time. The reason for this is that we actually try to fit the model before predicting the runtime, in order to raise any instant errors. We run _algo.fit(X, y)_ in a subprocess for one second to check for any fit error up after which we move on to the prediction part. However, there are times where the algo (and / or the input matrix) are so big that running _algo.fit(X,y)_ will throw a memory error eventually, which we can’t account for.

### Future improvements

The most effective and obvious way to improve the performance of our current predictions would be to generate more data points on different systems to better support a wide range of hardware/parameters.

We will be looking at adding more supported Scikit Learn algos in the near future. We could also implement other algos such as [lightGBM](https://github.com/Microsoft/LightGBM) or [xgboost](https://github.com/dmlc/xgboost). Feel free to contact us if there’s an algorithm you would like us to implement in the next iterations of Scitime!

Other interesting avenues for improving the performance of the estimator would be to include more granular information about the input matrix such as variance, or correlation with output. We currently generate data completely randomly, for which the fit time might be higher than for real world datasets. So in some cases it might overestimate the training time.

In addition we could track finer hardware specific information such as frequency of the cpu, or current cpu usage.

Ideally, as the algorithm might change from a scikit-learn version to another, and thus have an impact on the runtime, we would also account for it, for example by using the version as a ‘meta’ feature.

As we acquire more data to fit our meta algos, we might think of using more complex meta algos, such as sophisticated neural networks (using regularization techniques like dropout or batch normalization). We could even consider using [tensorflow](https://www.tensorflow.org) to fit the meta algo (and add it as optional): it would not only help us get a better accuracy, but also build more robust confidence intervals using [dropout](https://towardsdatascience.com/uncertainty-estimation-for-neural-network-dropout-as-bayesian-approximation-7d30fc7bc1f2).

### Contributing to Scitime and sending us your feedback

First, any kind of feedback, especially on the performance of the predictions and on ideas to improve this process of generating data, is very much appreciated!

As discussed before, you can use our repo to generate your own data points in order to train your own meta algorithm. When doing so, you can help make Scitime better by sharing your data points found in the result csv (_~/scitime/scitime/[algo]_results.csv_) so that we can integrate it to our model.

To generate your own data you can run a command similar to this one (from the package repo source):

```
❱ python _data.py --verbose 3 --algo KMeans --drop_rate 0.99
```

Note: if run directly using the code source (with the _Model_ class), do not forget to set _write_csv_ to true, otherwise the generated data points will not be saved.

_We use GitHub issues to track all bugs and feature requests. Feel free to open an issue if you have found a bug or wish to see a new feature implemented. More info can be found about how to contribute in the Scitime repo._

_For issues with training time predictions, when submitting feedback, including the full dictionary of parameters you are fitting into your model might help, so that we can diagnose why the performance is subpar for your specific use case. To do so simply set the verbose parameter to 3 and copy paste the log of the parameter dic in the issue description._

_Find the [code source](https://github.com/nathan-toubiana/scitime)_

_Find the [documentation](https://scitime.readthedocs.io)_

### Credits

* [_Gabriel Lerner_](https://github.com/gabrielRTR) _& [Nathan Toubiana](https://github.com/nathan-toubiana) are the main contributors of this package and co-authors of this article_
* _Special thanks to [Philippe Mizrahi](https://github.com/philippemizrahi) for helping along the way_
* _Thanks for all the help we got from early reviews / beta testing_

