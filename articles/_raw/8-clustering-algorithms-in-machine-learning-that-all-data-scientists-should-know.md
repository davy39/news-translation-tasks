---
title: 8 Clustering Algorithms in Machine Learning that All Data Scientists Should
  Know
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-21T16:38:33.000Z'
originalURL: https://freecodecamp.org/news/8-clustering-algorithms-in-machine-learning-that-all-data-scientists-should-know
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/analysis.png
tags:
- name: algorithms
  slug: algorithms
- name: clustering
  slug: clustering
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
seo_title: null
seo_desc: "By Milecia McGregor\nThere are three different approaches to machine learning,\
  \ depending on the data you have. You can go with supervised learning, semi-supervised\
  \ learning, or unsupervised learning. \nIn supervised learning you have labeled\
  \ data, so y..."
---

By Milecia McGregor

There are three different approaches to machine learning, depending on the data you have. You can go with supervised learning, semi-supervised learning, or unsupervised learning. 

In supervised learning you have labeled data, so you have outputs that you know for sure are the correct values for your inputs. That's like knowing car prices based on features like make, model, style, drivetrain, and other attributes.

With semi-supervised learning, you have a large data set where some of the data is labeled but most of it isn't. 

This covers a large amount of real world data because it can be expensive to get an expert to label every data point. You can work around this by using a combination of supervised and unsupervised learning.

Unsupervised learning means you have a data set that is completely unlabeled. You don’t know if there are any patterns hidden in the data, so you leave it to the algorithm to find anything it can. 

That's where clustering algorithms come in. It's one of the methods you can use in an unsupervised learning problem.

## What are clustering algorithms?

Clustering is an unsupervised machine learning task. You might also hear this referred to as cluster analysis because of the way this method works. 

Using a clustering algorithm means you're going to give the algorithm a lot of input data with no labels and let it find any groupings in the data it can.

Those groupings are called _clusters_. A cluster is a group of data points that are similar to each other based on their relation to surrounding data points. Clustering is used for things like feature engineering or pattern discovery. 

When you're starting with data you know nothing about, clustering might be a good place to get some insight. 

## Types of clustering algorithms

There are different types of clustering algorithms that handle all kinds of unique data.

### Density-based

In density-based clustering, data is grouped by areas of high concentrations of data points surrounded by areas of low concentrations of data points. Basically the algorithm finds the places that are dense with data points and calls those clusters.

The great thing about this is that the clusters can be any shape. You aren't constrained to expected conditions. 

The clustering algorithms under this type don't try to assign outliers to clusters, so they get ignored.

### Distribution-based

With a distribution-based clustering approach, all of the data points are considered parts of a cluster based on the probability that they belong to a given cluster. 

It works like this: there is a center-point, and as the distance of a data point from the center increases, the probability of it being a part of that cluster decreases. 

If you aren't sure of how the distribution in your data might be, you should consider a different type of algorithm.

### Centroid-based

Centroid-based clustering is the one you probably hear about the most. It's a little sensitive to the initial parameters you give it, but it's fast and efficient. 

These types of algorithms separate data points based on multiple centroids in the data. Each data point is assigned to a cluster based on its squared distance from the centroid. This is the most commonly used type of clustering.

### Hierarchical-based

Hierarchical-based clustering is typically used on hierarchical data, like you would get from a company database or taxonomies. It builds a tree of clusters so everything is organized from the top-down. 

This is more restrictive than the other clustering types, but it's perfect for specific kinds of data sets.

## When to use clustering

When you have a set of unlabeled data, it's very likely that you'll be using some kind of unsupervised learning algorithm. 

There are a lot of different unsupervised learning techniques, like neural networks, reinforcement learning, and clustering. The specific type of algorithm you want to use is going to depend on what your data looks like.

You might want to use clustering when you're trying to do anomaly detection to try and find outliers in your data. It helps by finding those groups of clusters and showing the boundaries that would determine whether a data point is an outlier or not. 

If you aren't sure of what features to use for your machine learning model, clustering discovers patterns you can use to figure out what stands out in the data.

Clustering is especially useful for exploring data you know nothing about. It might take some time to figure out which type of clustering algorithm works the best, but when you do, you'll get invaluable insight on your data. You might find connections you never would have thought of.

Some real world applications of clustering include fraud detection in insurance, categorizing books in a library, and customer segmentation in marketing. It can also be used in larger problems, like earthquake analysis or city planning.

## The Top 8 Clustering Algorithms

Now that you have some background on how clustering algorithms work and the different types available, we can talk about the actual algorithms you'll commonly see in practice. 

We'll implement these algorithms on an example data set from the [sklearn library](https://scikit-learn.org/stable/) in Python.

We'll be using the _make_classification_ data set from the sklearn library to demonstrate how different clustering algorithms aren't fit for all clustering problems. 

You can find [the code for all of the following example here](https://github.com/flippedcoder/probable-waddle).

### K-means clustering algorithm

K-means clustering is the most commonly used clustering algorithm. It's a centroid-based algorithm and the simplest unsupervised learning algorithm. 

This algorithm tries to minimize the variance of data points within a cluster. It's also how most people are introduced to unsupervised machine learning.

K-means is best used on smaller data sets because it iterates over _all_ of the data points. That means it'll take more time to classify data points if there are a large amount of them in the data set. 

Since this is how k-means clusters data points, it doesn't scale well.

**Implementation:**

```python
from numpy import unique
from numpy import where
from matplotlib import pyplot
from sklearn.datasets import make_classification
from sklearn.cluster import KMeans

# initialize the data set we'll work with
training_data, _ = make_classification(
    n_samples=1000,
    n_features=2,
    n_informative=2,
    n_redundant=0,
    n_clusters_per_class=1,
    random_state=4
)

# define the model
kmeans_model = KMeans(n_clusters=2)

# assign each data point to a cluster
dbscan_result = dbscan_model.fit_predict(training_data)

# get all of the unique clusters
dbscan_clusters = unique(dbscan_result)

# plot the DBSCAN clusters
for dbscan_cluster in dbscan_clusters:
    # get data points that fall in this cluster
    index = where(dbscan_result == dbscan_clusters)
    # make the plot
    pyplot.scatter(training_data[index, 0], training_data[index, 1])

# show the DBSCAN plot
pyplot.show()
```

### DBSCAN clustering algorithm

DBSCAN stands for density-based spatial clustering of applications with noise. It's a density-based clustering algorithm, unlike k-means. 

This is a good algorithm for finding outliners in a data set. It finds arbitrarily shaped clusters based on the density of data points in different regions. It separates regions by areas of low-density so that it can detect outliers between the high-density clusters.

This algorithm is better than k-means when it comes to working with oddly shaped data. 

DBSCAN uses two parameters to determine how clusters are defined: _minPts_ (the minimum number of data points that need to be clustered together for an area to be considered high-density) and _eps_ (the distance used to determine if a data point is in the same area as other data points). 

Choosing the right initial parameters is critical for this algorithm to work.

**Implementation:**

```python
from numpy import unique
from numpy import where
from matplotlib import pyplot
from sklearn.datasets import make_classification
from sklearn.cluster import DBSCAN

# initialize the data set we'll work with
training_data, _ = make_classification(
    n_samples=1000,
    n_features=2,
    n_informative=2,
    n_redundant=0,
    n_clusters_per_class=1,
    random_state=4
)

# define the model
dbscan_model = DBSCAN(eps=0.25, min_samples=9)

# train the model
dbscan_model.fit(training_data)

# assign each data point to a cluster
dbscan_result = dbscan_model.predict(training_data)

# get all of the unique clusters
dbscan_cluster = unique(dbscan_result)

# plot the DBSCAN clusters
for dbscan_cluster in dbscan_clusters:
    # get data points that fall in this cluster
    index = where(dbscan_result == dbscan_clusters)
    # make the plot
    pyplot.scatter(training_data[index, 0], training_data[index, 1])

# show the DBSCAN plot
pyplot.show()
```

### Gaussian Mixture Model algorithm

One of the problems with k-means is that the data needs to follow a circular format. The way k-means calculates the distance between data points has to do with a circular path, so non-circular data isn't clustered correctly. 

This is an issue that Gaussian mixture models fix. You don’t need circular shaped data for it to work well.

The Gaussian mixture model uses multiple Gaussian distributions to fit arbitrarily shaped data. 

There are several single Gaussian models that act as hidden layers in this hybrid model. So the model calculates the probability that a data point belongs to a specific Gaussian distribution and that's the cluster it will fall under.

**Implementation:**

```python
from numpy import unique
from numpy import where
from matplotlib import pyplot
from sklearn.datasets import make_classification
from sklearn.mixture import GaussianMixture

# initialize the data set we'll work with
training_data, _ = make_classification(
    n_samples=1000,
    n_features=2,
    n_informative=2,
    n_redundant=0,
    n_clusters_per_class=1,
    random_state=4
)

# define the model
gaussian_model = GaussianMixture(n_components=2)

# train the model
gaussian_model.fit(training_data)

# assign each data point to a cluster
gaussian_result = gaussian_model.predict(training_data)

# get all of the unique clusters
gaussian_clusters = unique(gaussian_result)

# plot Gaussian Mixture the clusters
for gaussian_cluster in gaussian_clusters:
    # get data points that fall in this cluster
    index = where(gaussian_result == gaussian_clusters)
    # make the plot
    pyplot.scatter(training_data[index, 0], training_data[index, 1])

# show the Gaussian Mixture plot
pyplot.show()
```

### BIRCH algorithm

The Balance Iterative Reducing and Clustering using Hierarchies (BIRCH) algorithm works better on large data sets than the k-means algorithm. 

It breaks the data into little summaries that are clustered instead of the original data points. The summaries hold as much distribution information about the data points as possible.

This algorithm is commonly used with other clustering algorithm because the other clustering techniques can be used on the summaries generated by BIRCH. 

The main downside of the BIRCH algorithm is that it only works on numeric data values. You can't use this for categorical values unless you do some data transformations.

**Implementation:**

```python
from numpy import unique
from numpy import where
from matplotlib import pyplot
from sklearn.datasets import make_classification
from sklearn.cluster import Birch

# initialize the data set we'll work with
training_data, _ = make_classification(
    n_samples=1000,
    n_features=2,
    n_informative=2,
    n_redundant=0,
    n_clusters_per_class=1,
    random_state=4
)

# define the model
birch_model = Birch(threshold=0.03, n_clusters=2)

# train the model
birch_model.fit(training_data)

# assign each data point to a cluster
birch_result = birch_model.predict(training_data)

# get all of the unique clusters
birch_clusters = unique(birch_result)

# plot the BIRCH clusters
for birch_cluster in birch_clusters:
    # get data points that fall in this cluster
    index = where(birch_result == birch_clusters)
    # make the plot
    pyplot.scatter(training_data[index, 0], training_data[index, 1])

# show the BIRCH plot
pyplot.show()

```

### Affinity Propagation clustering algorithm

This clustering algorithm is completely different from the others in the way that it clusters data. 

Each data point communicates with all of the other data points to let each other know how similar they are and that starts to reveal the clusters in the data. You don't have to tell this algorithm how many clusters to expect in the initialization parameters.

As messages are sent between data points, sets of data called _exemplars_ are found and they represent the clusters. 

An exemplar is found after the data points have passed messages to each other and form a consensus on what data point best represents a cluster. 

When you aren't sure how many clusters to expect, like in a computer vision problem, this is a great algorithm to start with.

**Implementation:**

```python
from numpy import unique
from numpy import where
from matplotlib import pyplot
from sklearn.datasets import make_classification
from sklearn.cluster import AffinityPropagation

# initialize the data set we'll work with
training_data, _ = make_classification(
    n_samples=1000,
    n_features=2,
    n_informative=2,
    n_redundant=0,
    n_clusters_per_class=1,
    random_state=4
)

# define the model
model = AffinityPropagation(damping=0.7)

# train the model
model.fit(training_data)

# assign each data point to a cluster
result = model.predict(training_data)

# get all of the unique clusters
clusters = unique(result)

# plot the clusters
for cluster in clusters:
    # get data points that fall in this cluster
    index = where(result == cluster)
    # make the plot
    pyplot.scatter(training_data[index, 0], training_data[index, 1])

# show the plot
pyplot.show()
```

### Mean-Shift clustering algorithm

This is another algorithm that is particularly useful for handling images and computer vision processing. 

Mean-shift is similar to the BIRCH algorithm because it also finds clusters without an initial number of clusters being set. 

This is a hierarchical clustering algorithm, but the downside is that it doesn't scale well when working with large data sets.

It works by iterating over all of the data points and shifts them towards the mode. The mode in this context is the high density area of data points in a region. 

That's why you might hear this algorithm referred to as the mode-seeking algorithm. It will go through this iterative process with each data point and move them closer to where other data points are until all data points have been assigned to a cluster.

**Implementation:**

```python
from numpy import unique
from numpy import where
from matplotlib import pyplot
from sklearn.datasets import make_classification
from sklearn.cluster import MeanShift

# initialize the data set we'll work with
training_data, _ = make_classification(
    n_samples=1000,
    n_features=2,
    n_informative=2,
    n_redundant=0,
    n_clusters_per_class=1,
    random_state=4
)

# define the model
mean_model = MeanShift()

# assign each data point to a cluster
mean_result = mean_model.fit_predict(training_data)

# get all of the unique clusters
mean_clusters = unique(mean_result)

# plot Mean-Shift the clusters
for mean_cluster in mean_clusters:
    # get data points that fall in this cluster
    index = where(mean_result == mean_cluster)
    # make the plot
    pyplot.scatter(training_data[index, 0], training_data[index, 1])

# show the Mean-Shift plot
pyplot.show()
```

### OPTICS algorithm

OPTICS stands for Ordering Points to Identify the Clustering Structure. It's a density-based algorithm similar to DBSCAN, but it's better because it can find meaningful clusters in data that varies in density. It does this by ordering the data points so that the closest points are neighbors in the ordering.

This makes it easier to detect different density clusters. The OPTICS algorithm only processes each data point once, similar to DBSCAN (although it runs slower than DBSCAN). There's also a special distance stored for each data point that indicates a point belongs to a specific cluster.

**Implementation:**

```python
from numpy import unique
from numpy import where
from matplotlib import pyplot
from sklearn.datasets import make_classification
from sklearn.cluster import OPTICS

# initialize the data set we'll work with
training_data, _ = make_classification(
    n_samples=1000,
    n_features=2,
    n_informative=2,
    n_redundant=0,
    n_clusters_per_class=1,
    random_state=4
)

# define the model
optics_model = OPTICS(eps=0.75, min_samples=10)

# assign each data point to a cluster
optics_result = optics_model.fit_predict(training_data)

# get all of the unique clusters
optics_clusters = unique(optics_clusters)

# plot OPTICS the clusters
for optics_cluster in optics_clusters:
    # get data points that fall in this cluster
    index = where(optics_result == optics_clusters)
    # make the plot
    pyplot.scatter(training_data[index, 0], training_data[index, 1])

# show the OPTICS plot
pyplot.show()
```

### Agglomerative Hierarchy clustering algorithm

This is the most common type of hierarchical clustering algorithm. It's used to group objects in clusters based on how similar they are to each other. 

This is a form of bottom-up clustering, where each data point is assigned to its own cluster. Then those clusters get joined together.

At each iteration, similar clusters are merged until all of the data points are part of one big root cluster. 

Agglomerative clustering is best at finding small clusters. The end result looks like a dendrogram so that you can easily visualize the clusters when the algorithm finishes.

**Implementation:**

```python
from numpy import unique
from numpy import where
from matplotlib import pyplot
from sklearn.datasets import make_classification
from sklearn.cluster import AgglomerativeClustering

# initialize the data set we'll work with
training_data, _ = make_classification(
    n_samples=1000,
    n_features=2,
    n_informative=2,
    n_redundant=0,
    n_clusters_per_class=1,
    random_state=4
)

# define the model
agglomerative_model = AgglomerativeClustering(n_clusters=2)

# assign each data point to a cluster
agglomerative_result = agglomerative_model.fit_predict(training_data)

# get all of the unique clusters
agglomerative_clusters = unique(agglomerative_result)

# plot the clusters
for agglomerative_cluster in agglomerative_clusters:
    # get data points that fall in this cluster
    index = where(agglomerative_result == agglomerative_clusters)
    # make the plot
    pyplot.scatter(training_data[index, 0], training_data[index, 1])

# show the Agglomerative Hierarchy plot
pyplot.show()
```

## Other types of clustering algorithms

We've covered eight of the top clustering algorithms, but there are plenty more than that available. There are some very specifically tuned clustering algorithms that quickly and precisely handle your data. Here are a few of the others that might be of interest to you.

There's another hierarchical algorithm that's the opposite of the agglomerative approach. It starts with a top-down clustering strategy. So it will start with one large root cluster and break out the individual clusters from there. 

This is known as the **Divisive Hierarchical** clustering algorithm. There's research that shows this is creates more accurate hierarchies than agglomerative clustering, but it's way more complex.

**Mini-Batch K-means** is similar to K-means, except that it uses small random chunks of data of a fixed size so they can be stored in memory. This helps it run faster than K-means so it converges to a solution in less time. 

The drawback to this algorithm is that the speed boost will cost you some cluster quality.

The last algorithm we'll briefly cover is **Spectral Clustering**. This algorithm is completely different from the others we've looked at. 

It works by taking advantage of graph theory. This algorithm doesn't make any initial guesses about the clusters that are in the data set. It treats data points like nodes in a graph and clusters are found based on communities of nodes that have connecting edges.

## Other thoughts

Watch out for scaling issues with the clustering algorithms. Your data set could have millions of data points, and since clustering algorithms work by calculating the similarities between all pairs of data points, you might end up with an algorithm that doesn’t scale well.

## Conclusion

Clustering algorithms are a great way to learn new things from old data. Sometimes you'll be surprised by the resulting clusters you get and it might help you make sense of a problem. 

One of the coolest things about using clustering for unsupervised learning is that you can use the results in a supervised learning problem.

The clusters could be your new features that you use on a completely different data set! You can use clustering on just about any unsupervised machine learning problem, but make sure that you know how to analyze the results for accuracy.


