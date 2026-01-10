---
title: The Ultimate Guide to Recurrent Neural Networks in Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-13T16:48:49.000Z'
originalURL: https://freecodecamp.org/news/the-ultimate-guide-to-recurrent-neural-networks-in-python
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c99bf740569d1a4ca2186.jpg
tags:
- name: neural networks
  slug: neural-networks
- name: Python
  slug: python
seo_title: null
seo_desc: 'By Nick McCullum

  Recurrent neural networks are deep learning models that are typically used to solve
  time series problems. They are used in self-driving cars, high-frequency trading
  algorithms, and other real-world applications.

  This tutorial will te...'
---

By Nick McCullum

Recurrent neural networks are deep learning models that are typically used to solve time series problems. They are used in self-driving cars, high-frequency trading algorithms, and other real-world applications.

This tutorial will teach you the fundamentals of recurrent neural networks. You'll also build your own recurrent neural network that predicts tomorrow's stock price for Facebook (FB).

# **The Intuition of Recurrent Neural Networks**

[Recurrent neural networks](https://nickmccullum.com/python-deep-learning/recurrent-neural-network-tutorial/) are an example of the broader field of [neural networks](https://www.freecodecamp.org/news/deep-learning-neural-networks-explained-in-plain-english/). Other examples include:

* [Artificial neural networks](https://nickmccullum.com/python-deep-learning/artificial-neural-network-tutorial/)
* [Convolutional neural networks](https://nickmccullum.com/python-deep-learning/convolutional-neural-network-tutorial/)

This article will be focused on recurrent neural networks.

This tutorial will begin our discussion of recurrent neural networks by discussing the intuition behind recurrent neural networks.

## **The Types of Problems Solved By Recurrent Neural Networks**

Although we have not explicitly discussed it yet, there are generally broad swathes of problems that each type of neural network is designed to solve:

* Artificial neural networks: classification and regression problems
* [Convolutional neural networks](https://nickmccullum.com/python-deep-learning/introduction-convolutional-neural-networks/): computer vision problems

In the case of recurrent neural networks, they are typically used to solve time series analysis problems.

Each of these three types of neural networks (artificial, convolutional, and recurrent) are used to solve supervised machine learning problems.

## **Mapping Neural Networks to Parts of the Human Brain**

As you’ll recall, neural networks were designed to mimic the human brain. This is true for both their construction (both the brain and neural networks are composed of neurons) and their function (they are both used to make decisions and predictions).

The three main parts of the brain are:

* The cerebrum
* The brainstem
* The cerebellum

Arguably the most important part of the brain is the cerebrum. It contains four lobes:

* The frontal lobe
* The parietal lobe
* The temporal lobe
* The occipital lobe

The main innovation that neural networks contain is the idea of weights.

Said differently, the most important characteristic of the brain that neural networks have mimicked is the ability to learn from other neurons.

The ability of a neural network to change its weights through each epoch of its training stage is similar to the long-term memory that is seen in humans (and other animals).

The temporal lobe is the part of the brain that is associated with long-term memory. Separately, the artificial neural network was the first type of neural network that had this long-term memory property. In this sense, many researchers have compared artificial neural networks with the temporal lobe of the human brain.

Similarly, the occipital lobe is the component of the brain that powers our vision. Since convolutional neural networks are typically used to solve computer vision problems, you could say that they are equivalent to the occipital lobe in the brain.

As mentioned, recurrent neural networks are used to solve time series problems. They can learn from events that have happened in recent previous iterations of their training stage. In this way, they are often compared to the frontal lobe of the brain – which powers our short-term memory.

To summarize, researchers often pair each of the three neural nets with the following parts of the brain:

* Artificial neural networks: the temporal lobe
* Convolutional neural networks: the occipital lobe
* Recurrent neural networks: the frontal lobe

## **The Composition of a Recurrent Neural Network**

Let’s now discuss the composition of a recurrent neural network. First, recall that the composition of a basic neural network has the following appearance:

![A basic neural network](https://nickmccullum.com/images/python-deep-learning/intuition-recurrent-neural-networks/basic-neural-network.png)

The first modification that needs to be made to this neural network is that each layer of the network should be squashed together, like this:

![A squashed neural network](https://nickmccullum.com/images/python-deep-learning/intuition-recurrent-neural-networks/squashed-neural-network.png)

Then, three more modifications need to be made:

* The neural network’s neuron synapses need to be simplified to a single line
* The entire neural network needs to be rotated 90 degrees
* A loop needs to be generated around the hidden layer of the neural net

The neural network will now have the following appearance:

![A recurrent neural network](https://nickmccullum.com/images/python-deep-learning/intuition-recurrent-neural-networks/recurrent-neural-network.png)

That line that circles the hidden layer of the recurrent neural network is called the temporal loop. It is used to indicate that the hidden layer not only generates an output, but that output is fed back as the input into the same layer.

A visualization is helpful in understanding this. As you can see in the following image, the hidden layer used on a specific observation of a data set is not only used to generate an output for that observation, but it is also used to train the hidden layer of the next observation.

![A time series recurrent neural network](https://nickmccullum.com/images/python-deep-learning/intuition-recurrent-neural-networks/time-series-recurrent-neural-network.png)

This property of one observation helping to train the next observation is why recurrent neural networks are so useful in solving time series analysis problems.

## Summary – The Intuition of Recurrent Neural Networks

In this tutorial, you had your first introduction to recurrent neural networks. More specifically, we discussed the intuition behind recurrent neural networks.

Here is a brief summary of what we discussed in this tutorial:

* The types of problems solved by recurrent neural networks
* The relationships between the different parts of the brain and the different neural networks we’ve studied in this course
* The composition of a recurrent neural network and how each hidden layer can be used to help train the hidden layer from the next observation in the data set

# **The Vanishing Gradient Problem in Recurrent Neural Networks**

The vanishing gradient problem has historically been one of the largest barriers to the success of recurrent neural networks.

Because of this, having an understanding of the vanishing gradient problem is important before you build your first RNN.

This section will explain the vanishing gradient problem in plain English, including a discussion of the most useful solutions to this interesting problem.

## **What Is The Vanishing Gradient Problem?**

Before we dig in to the details of the vanishing gradient problem, it’s helpful to have some understanding of how the problem was initially discovered.

The vanishing gradient problem was discovered by [Sepp Hochreiter](https://en.wikipedia.org/wiki/Sepp_Hochreiter), a German computer scientist who has had an influential role in the development of recurrent neural networks in deep learning.

Now let’s explore the vanishing gradient problem in detail. As its name implies, the vanishing gradient problem is related to deep learning gradient descent algorithms. Recall that a gradient descent algorithm looks something like this:

![A finalized gradient descent algorithm](https://nickmccullum.com/images/python-deep-learning/gradient-descent/finalized-gradient-descent.png)

This gradient descent algorithm is then combined with a backpropagation algorithm to update the synapse weights throughout the neural network.

Recurrent neural networks behave slightly differently because the hidden layer of one observation is used to train the hidden layer of the next observation.

![A recurrent neural network gradient descent algorithm](https://nickmccullum.com/images/python-deep-learning/vanishing-gradient-problem/rnn-backpropogation.png)

This means that the cost function of the neural net is calculated for each observation in the data set. These cost function values are depicted at the top of the following image:

![A recurrent neural network gradient descent algorithm](https://nickmccullum.com/images/python-deep-learning/vanishing-gradient-problem/rnn-cost-function.png)

The vanishing gradient problem occurs when the backpropagation algorithm moves back through all of the neurons of the neural net to update their weights. The nature of recurrent neural networks means that the cost function computed at a deep layer of the neural net will be used to change the weights of neurons at shallower layers.

The mathematics that computes this change is multiplicative, which means that the gradient calculated in a step that is deep in the neural network will be multiplied back through the weights earlier in the network. Said differently, the gradient calculated deep in the network is “diluted” as it moves back through the net, which can cause the gradient to vanish – giving the name to the vanishing gradient problem!

The actual factor that is multiplied through a recurrent neural network in the backpropagation algorithm is referred to by the mathematical variable `Wrec`. It poses two problems:

* When `Wrec` is small, you experience a vanishing gradient problem
* When `Wrec` is large, you experience an exploding gradient problem

Note that both of these problems are generally referred to by the simpler name of the “vanishing gradient problem”.

To summarize, the vanishing gradient problem is caused by the multiplicative nature of the backpropagation algorithm. It means that gradients calculated at a deep stage of the recurrent neural network either have too small of an impact (in a vanishing gradient problem) or too large of an impact (in an exploding gradient problem) on the weights of neurons that are shallower in the neural net.

## **How to Solve The Vanishing Gradient Problem**

There are a number of strategies that can be used to solve the vanishing gradient problem. We will explore strategies for both the vanishing gradient and exploding gradient problems separately. Let’s start with the latter.

### **Solving the Exploding Gradient Problem**

For exploding gradients, it is possible to use a modified version of the backpropagation algorithm called `truncated backpropagation`. The [truncated backpropagation algorithm](https://machinelearningmastery.com/gentle-introduction-backpropagation-time/) limits that number of timesteps that the backproporation will be performed on, stopping the algorithm before the exploding gradient problem occurs.

You can also introduce `penalties`, which are hard-coded techniques for reduces a backpropagation’s impact as it moves through shallower layers in a neural network.

Lastly, you could introduce `gradient clipping`, which introduces an artificial ceiling that limits how large the gradient can become in a backpropagation algorithm.

### **Solving the Vanishing Gradient Problem**

Weight initialization is one technique that can be used to solve the vanishing gradient problem. It involves artificially creating an initial value for weights in a neural network to prevent the backpropagation algorithm from assigning weights that are unrealistically small.

You could also use echo state networks, which is a specific type of neural network designed to avoid the vanishing gradient problem. Echo state networks are outside the scope of this course. Having knowledge of their existence is sufficient for now.

The most important solution to the vanishing gradient problem is a specific type of neural network called Long Short-Term Memory Networks (LSTMs), which were pioneered by Sepp Hochreiter and [Jürgen Schmidhuber](https://en.wikipedia.org/wiki/J%C3%BCrgen_Schmidhuber). Recall that Mr. Hochreiter was the scientist who originally discovered the vanishing gradient problem.

LSTMs are used in problems primarily related to speech recognition, with one of the most notable examples being [Google using an LSTM for speech recognition](https://googleblog.blogspot.com/2015/07/neon-prescription-or-rather-new.html) in 2015 and experiencing a 49% decrease in transcription errors.

LSTMs are considered to be the go-to neural net for scientists interested in implementing recurrent neural networks. We will be largely focusing on LSTMs through the remainder of this course.

## **Summary – The Vanishing Gradient Problem**

In this section, you learned about the vanishing gradient problem of recurrent neural networks.

Here is a brief summary of what we discussed:

* That Sepp Hochreiter was the first scientist to discover the vanishing gradient problem in recurrent neural networks
* What the vanishing gradient problem (and its cousin, the exploding gradient problem) involves
* The role of `Wrec` in vanishing gradient problems and exploding gradient problems
* How vanishing gradient problems and exploding gradient problems are solved
* The role of LSTMs as the most common solution to the vanishing gradient problem

# **Long Short-Term Memory Networks (LSTMs)**

Long short-term memory networks (LSTMs) are a type of recurrent neural network used to solve [the vanishing gradient problem.](https://nickmccullum.com/python-deep-learning/vanishing-gradient-problem/)

They differ from “regular” recurrent neural networks in important ways.

This tutorial will introduce you to LSTMs. Later in this course, we will build and train an LSTM from scratch.

## **Table of Contents**

You can skip to a specific section of this LSTM tutorial using the table of contents below:

* [The History of LSTMs](https://nickmccullum.com/python-deep-learning/lstms-long-short-term-memory-networks/#the-history-of-lstms)
* [How LSTMs Solve The Vanishing Gradient Problem](https://nickmccullum.com/python-deep-learning/lstms-long-short-term-memory-networks/#how-lstms-solve-the-vanishing-gradient-problem)
* [How LSTMs Work](https://nickmccullum.com/python-deep-learning/lstms-long-short-term-memory-networks/#how-lstms-work)
* [Variations of LSTM Architectures](https://nickmccullum.com/python-deep-learning/lstms-long-short-term-memory-networks/#variations-of-lstm-architectures)
* [The Peephole Variation](https://nickmccullum.com/python-deep-learning/lstms-long-short-term-memory-networks/#the-peephole-variation)
* [The Coupled Gate Variation](https://nickmccullum.com/python-deep-learning/lstms-long-short-term-memory-networks/#the-coupled-gate-variation)
* [Other LSTM Variations](https://nickmccullum.com/python-deep-learning/lstms-long-short-term-memory-networks/#other-lstm-variations)
* [Final Thoughts](https://nickmccullum.com/python-deep-learning/lstms-long-short-term-memory-networks/#final-thoughts)

## **The History of LSTMs**

As we alluded to in the last section, the two most important figures in the field of LSTMs are [Sepp Hochreiter](https://en.wikipedia.org/wiki/Sepp_Hochreiter) and [Jürgen Schmidhuber](https://en.wikipedia.org/wiki/J%C3%BCrgen_Schmidhuber).

The latter was the former’s PhD supervisor at the Technical University of Munich in Germany.

Hochreiter’s PhD thesis introduced LSTMs to the world for the first time.

## **How LSTMs Solve The Vanishing Gradient Problem**

In the last tutorial, we learned how the `Wrec` term in the backpropagation algorithm can lead to either a vanishing gradient problem or an exploding gradient problem.

We explored various possible solutions for this problem, including penalties, gradient clipping, and even echo state networks. LSTMs are the best solution.

So how do LSTMs work? They simply change the value of `Wrec`.

In our explanation of the vanishing gradient problem, you learned that:

* When `Wrec` is small, you experience a vanishing gradient problem
* When `Wrec` is large, you experience an exploding gradient problem

We can actually be much more specific:

* When `Wrec < 1`, you experience a vanishing gradient problem
* When `Wrec > 1`, you experience an exploding gradient problem

This makes sense if you think about the multiplicative nature of the backpropagation algorithm.

If you have a number that is smaller than `1` and you multiply it against itself over and over again, you’ll end up with a number that vanishes. Similarly, multiplying a number greater than `1` against itself many times results in a very large number.

To solve this problem, LSTMs set `Wrec = 1`. There is certainly more to LSTMS than setting `Wrec = 1`, but this is definitely the most important change that this specification of recurrent neural networks makes.

## **How LSTMs Work**

This section will explain how LSTMs work. Before proceeding ,it’s worth mentioning that I will be using images from Christopher Olah’s blog post [Understanding LSTMs](https://colah.github.io/posts/2015-08-Understanding-LSTMs/), which was published in August 2015 and has some of the best LSTM visualizations that I have ever seen.

To start, let’s consider the basic version of a recurrent neural network:

![A basic recurrent neural network](https://nickmccullum.com/images/python-deep-learning/lstms/recurrent-neural-network.png)

This neural network has neurons and synapses that transmit the weighted sums of the outputs from one layer as the inputs of the next layer. A backpropagation algorithm will move backwards through this algorithm and update the weights of each neuron in response to he cost function computed at each epoch of its training stage.

By contrast, here is what an LSTM looks like:

![An LSTM](https://nickmccullum.com/images/python-deep-learning/lstms/lstm.png)

As you can see, an LSTM has far more embedded complexity than a regular recurrent neural network. My goal is to allow you to fully understand this image by the time you’ve finished this tutorial.

First, let’s get comfortable with the notation used in the image above:

![The notation we'll be using in our LSTM tutorial](https://nickmccullum.com/images/python-deep-learning/lstms/lstm-notation.png)

Now that you have a sense of the notation we’ll be using in this LSTM tutorial, we can start examining the functionality of a layer within an LSTM neural net. Each layer has the following appearance:

![A node from an LSTM neural network](https://nickmccullum.com/images/python-deep-learning/lstms/lstm-node.png)

Before we dig into the functionality of nodes within an LSTM neural network, it’s worth noting that every input and output of these deep learning models is a vector. In Python, this is generally represented by a [NumPy array](https://nickmccullum.com/advanced-python/numpy-arrays/) or another one-dimensional data structure.

The first thing that happens within an LSTM is the [activation function](https://nickmccullum.com/python-deep-learning/deep-learning-activation-functions/) of the `forget gate layer`. It looks at the inputs of the layer (labelled `xt` for the observation and `ht` for the output of the previous layer of the neural network) and outputs either `1` or `0` for every number in the cell state from the previous layer (labelled `Ct-1`).

Here’s a visualization of the activation of the `forget gate layer`:

![A node from an LSTM neural network](https://nickmccullum.com/images/python-deep-learning/lstms/lstm-node-1.png)

We have not discussed cell state yet, so let’s do that now. Cell state is represented in our diagram by the long horizontal line that runs through the top of the diagram. As an example, here is the cell state in our visualizations:

![Cell state within LSTM networks](https://nickmccullum.com/images/python-deep-learning/lstms/cell-state.png)

The cell state’s purpose is to decide what information to carry forward from the different observations that a recurrent neural network is trained on. The decision of whether or not to carry information forward is made by `gates` - of which the `forget gate` is a prime example. Each gate within an LSTM will have the following appearance:

![Cell state within LSTM networks](https://nickmccullum.com/images/python-deep-learning/lstms/cell-state.png)

The `σ` character within these gates refers to the Sigmoid function, which you have probably seen used in [logistic regression machine learning models](https://nickmccullum.com/python-machine-learning/logistic-regression-python/). The sigmoid function is used as a type of activation function in LSTMs that determines what information is passed through a gate to affect the network’s cell state.

By definition, the Sigmoid function can only output numbers between `0` and `1`. It’s often used to calculate probabilities because of this. In the case of LSTM models, it specifies what proportion of each output should be allowed to influence the sell state.

The next two steps of an LSTM model are closely related: the `input gate layer` and the `tanh layer`. These layers work together to determine how to update the cell state. At the same time, the last step is completed, which allows the cell to determine what to forget about the last observation in the data set.

Here is a visualization of this process:

![A node from an LSTM neural network](https://nickmccullum.com/images/python-deep-learning/lstms/lstm-node-2.png)

The last step of an LSTM determines the output for this observation (denoted `ht`). This step runs through both a sigmoid function and a hyperbolic tangent function. It can be visualized as follows:

![A node from an LSTM neural network](https://nickmccullum.com/images/python-deep-learning/lstms/lstm-node-3.png)

That concludes the process of training a single layer of an LSTM model. As you might imagine, there is plenty of mathematics under the surface that we have glossed over. The point of this section is to broadly explain how LSTMs work, not for you to deeply understand each operation in the process.

## **Variations of LSTM Architectures**

I wanted to conclude this tutorial by discussing a few different variations of LSTM architecture that are slightly different from the basic LSTM that we’ve discussed so far.

As a quick recap, here is what a generalized node of an LSTM looks like:

![A node from an LSTM neural network](https://nickmccullum.com/images/python-deep-learning/lstms/lstm-node.png)

### **The Peephole Variation**

Perhaps the most important variation of the LSTM architecture is the `peephole` variant, which allows the gate layers to read data from the cell state.

Here is a visualization of what the peephole variant might look like:

![A node from a peephole LSTM neural network](https://nickmccullum.com/images/python-deep-learning/lstms/peephole-lstm-node.png)

Note that while this diagram adds a peephole to every gate in the recurrent neural network, you could also add peepholes to some gates and not other gates.

### **The Coupled Gate Variation**

There is another variation of the LSTM architecture where the model makes the decision of what to forget and what to add new information to together. In the original LSTM model, these decisions were made separately.

Here is a visualization of what this architecture looks like:

![A node from a coupled gate LSTM neural network](https://nickmccullum.com/images/python-deep-learning/lstms/coupled-gate-lstm-node.png)

## **Other LSTM Variations**

These are only two examples of variants to the LSTM architecture. There are many more. A few are listed below:

* [Gated Recurrent Units (GRUs)](https://en.wikipedia.org/wiki/Gated_recurrent_unit)
* [Depth Gated RNNs](https://arxiv.org/abs/1508.03790)
* [Clockwork RNNs](https://arxiv.org/abs/1402.3511)

## **Summary - Long Short-Term Memory Networks**

In this tutorial, you had your first exposure to long short-term memory networks (LSTMs).

Here is a brief summary of what you learned:

* A (very) brief history of LSTMs and the role that Sepp Hochreiter and Jürgen Schmidhuber played in their development
* How LSTMs solve the vanishing gradient problem
* How LSTMs work
* The role of gates, sigmoid functions, and the hyperbolic tangent function in LSTMs
* A few of the most popular variations of the LSTM architecture

# **How To Build And Train A Recurrent Neural Network**

So far in our discussion of recurrent neural networks, you have learned:

* The basic [intuition behind recurrent neural networks](https://nickmccullum.com/python-deep-learning/intuition-recurrent-neural-networks/)
* The [vanishing gradient problem](https://nickmccullum.com/python-deep-learning/vanishing-gradient-problem/) that historically impeded the progress of recurrent neural networks
* How [long short-term memory networks (LSTMs)](https://nickmccullum.com/python-deep-learning/lstms-long-short-term-memory-networks/) help to solve the vanishing gradient problem

It’s now time to build your first recurrent neural network! More specifically, this tutorial will teach you how to build and train an LSTM to predict the stock price of Facebook (FB).

## **Table of Contents**

You can skip to a specific section of this Python recurrent neural network tutorial using the table of contents below:

* [Downloading the Data Set For This Tutorial](https://nickmccullum.com/python-deep-learning/recurrent-neural-network-tutorial/#downloading-the-data-set-for-this-tutorial)
* [Importing The Libraries You’ll Need For This Tutorial](https://nickmccullum.com/python-deep-learning/recurrent-neural-network-tutorial/#importing-the-libraries-you-ll-need-for-this-tutorial)
* [Importing Our Training Set Into The Python Script](https://nickmccullum.com/python-deep-learning/recurrent-neural-network-tutorial/#importing-our-training-set-into-the-python-script)
* [Applying Feature Scaling To Our Data Set](https://nickmccullum.com/python-deep-learning/recurrent-neural-network-tutorial/#applying-feature-scaling-to-our-data-set)
* [Specifying The Number Of Timesteps For Our Recurrent Neural Network](https://nickmccullum.com/python-deep-learning/recurrent-neural-network-tutorial/#specifying-the-number-of-timesteps-for-our-recurrent-neural-network)
* [Finalizing Our Data Sets By Transforming Them Into NumPy Arrays](https://nickmccullum.com/python-deep-learning/recurrent-neural-network-tutorial/#finalizing-our-data-sets-by-transforming-them-into-numpy-arrays)
* [Importing Our TensorFlow Libraries](https://nickmccullum.com/python-deep-learning/recurrent-neural-network-tutorial/#importing-our-tensorflow-libraries)
* [Building Our Recurrent Neural Network](https://nickmccullum.com/python-deep-learning/recurrent-neural-network-tutorial/#building-our-recurrent-neural-network)
* [Adding Our First LSTM Layer](https://nickmccullum.com/python-deep-learning/recurrent-neural-network-tutorial/#adding-our-first-lstm-layer)
* [Adding Some Dropout Regularization](https://nickmccullum.com/python-deep-learning/recurrent-neural-network-tutorial/#adding-some-dropout-regularization)
* [Adding Three More LSTM Layers With Dropout Regularization](https://nickmccullum.com/python-deep-learning/recurrent-neural-network-tutorial/#adding-three-more-lstm-layers-with-dropout-regularization)
* [Adding The Output Layer To Our Recurrent Neural Network](https://nickmccullum.com/python-deep-learning/recurrent-neural-network-tutorial/#adding-the-output-layer-to-our-recurrent-neural-network)
* [Compiling Our Recurrent Neural Network](https://nickmccullum.com/python-deep-learning/recurrent-neural-network-tutorial/#compiling-our-recurrent-neural-network)
* [Fitting The Recurrent Neural Network On The Training Set](https://nickmccullum.com/python-deep-learning/recurrent-neural-network-tutorial/#fitting-the-recurrent-neural-network-on-the-training-set)
* [Making Predictions With Our Recurrent Neural Network](https://nickmccullum.com/python-deep-learning/recurrent-neural-network-tutorial/#making-predictions-with-our-recurrent-neural-network)
* [Importing Our Test Data](https://nickmccullum.com/python-deep-learning/recurrent-neural-network-tutorial/#importing-our-test-data)
* [Building The Test Data Set We Need To Make Predictions](https://nickmccullum.com/python-deep-learning/recurrent-neural-network-tutorial/#building-the-test-data-set-we-need-to-make-predictions)
* [Scaling Our Test Data](https://nickmccullum.com/python-deep-learning/recurrent-neural-network-tutorial/#scaling-our-test-data)
* [Grouping Our Test Data](https://nickmccullum.com/python-deep-learning/recurrent-neural-network-tutorial/#grouping-our-test-data)
* [Actually Making Predictions](https://nickmccullum.com/python-deep-learning/recurrent-neural-network-tutorial/#actually-making-predictions)
* [The Full Code For This Tutorial](https://nickmccullum.com/python-deep-learning/recurrent-neural-network-tutorial/#the-full-code-for-this-tutorial)
* [Final Thoughts](https://nickmccullum.com/python-deep-learning/recurrent-neural-network-tutorial/#final-thoughts)

## **Downloading the Data Set For This Tutorial**

To proceed through this tutorial, you will need two download two data sets:

* A set of training data that contains information on Facebook’s stock price from teh start of 2015 to the end of 2019
* A set of test data that contains information on Facebook’s stock price during the first month of 2020

Our recurrent neural network will be trained on the 2015-2019 data and will be used to predict the data from January 2020.

You can download the training data and test data using the links below:

* [Training Data](https://nickmccullum.com/files/recurrent-neural-networks/FB_training_data.csv)
* [Test Data](https://nickmccullum.com/files/recurrent-neural-networks/FB_test_data.csv)

Each of these data sets are simply exports from Yahoo! Finance. They look like this (when opened in Microsoft Excel):

![An example data set that we'll be using to train our recurrent neural network](https://nickmccullum.com/images/python-deep-learning/recurrent-neural-networks/excel-file.png)

Once the files are downloaded, move them to the directory you’d like to work in and open a [Jupyter Notebook](https://nickmccullum.com/python-course/jupyter-notebook-basics/).

## **Importing The Libraries You’ll Need For This Tutorial**

This tutorial will depend on a number of open-source Python libraries, including [NumPy](https://nickmccullum.com/advanced-python/numpy/), [pandas](https://nickmccullum.com/advanced-python/pandas/), and [matplotlib](https://nickmccullum.com/python-visualization/how-to-import-matplotlib/).

Let’s start our Python script by importing some of these libraries:

```py

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt


```

## **Importing Our Training Set Into The Python Script**

The next task that needs to be completed is to import our data set into the Python script.

We will initially import the data set as a [pandas DataFrame](https://nickmccullum.com/advanced-python/pandas-dataframes/) using the `read_csv` method. However, since the `keras` module of `TensorFlow` only accepts [NumPy arrays](https://nickmccullum.com/advanced-python/numpy-arrays/) as parameters, the data structure will need to be transformed post-import.

Let’s start by importing the entire `.csv` file as a DataFrame:

```py

training_data = pd.read_csv('FB_training_data.csv')


```

You will notice in looking at the DataFrame that it contains numerous different ways of measuring Facebook’s stock price, including opening price, closing price, high and low prices, and volume information:

![An example data set that we'll be using to train our recurrent neural network](https://nickmccullum.com/images/python-deep-learning/recurrent-neural-networks/training_data.png)

We will need to select a specific type of stock price before proceeding. Let’s use `Close`, which indicates the unadjusted closing price of Facebook’s stock.

Now we need to select that column of the DataFrame and store it in a NumPy array. Here is the command to do this:

```py

training_data = training_data.iloc[:, 1].values


```

Note that this command overwrites the existing `training_data` variable that we had created previously.

You can now verify that our `training_data` variable is indeed a NumPy array by running `type(training_data)`, which should return:

```py

numpy.ndarray


```

## **Applying Feature Scaling To Our Data Set**

Let’s now take some time to apply some feature scaling to our data set.

As a quick refresher, there are two main ways that you can apply featuer scaling to your data set:

* Standardization
* Normalization

We’ll be using normalization to build our recurrent neural network, which involves subtracting the minimum value of the data set and then dividing by the range of the data set.

Here is the normalization function defined mathematically:

![Feature scaling normalization equation](https://nickmccullum.com/images/python-deep-learning/recurrent-neural-networks/normalization.jpg)

Fortunately, `scikit-learn` makes it very easy to apply normalization to a dataset using its `MinMaxScaler` class.

Let’s start by importing this class into our Python script. The `MinMaxScaler` class lives within the `preprocessing` module of `scikit-learn`, so the command to import the class is:

```py

from sklearn.preprocessing import MinMaxScaler


```

Next we need to create an instance of this class. We will assign the newly-created object to a variable called `scaler`. We will be using the default parameters for this class, so we do not need to pass anything in:

```py

scaler = MinMaxScaler()


```

Since we haven’t specified any non-default parameters, this will scale our data set so that every observation is between `0` and `1`.

We have created our `scaler` object but our `training_data` data set has not yet been scaled. We need to use the `fit_transform` method to modify the original data set. Here’s the statement to do this:

```py

training_data = scaler.fit_transform(training_data.reshape(-1, 1))


```

## **Specifying The Number Of Timesteps For Our Recurrent Neural Network**

The next thing we need to do is to specify our number of `timesteps`. [Timesteps](https://machinelearningmastery.com/use-timesteps-lstm-networks-time-series-forecasting/) specify how many previous observations should be considered when the recurrent neural network makes a prediction about the current observation.

We will use `40` timesteps in this tutorial. This means that for every day that the neural network predicts, it will consider the previous 40 days of stock prices to determine its output. Note that since there are only ~20 trading days in a given month, using 40 timesteps means we’re relying on stock price data from the previous 2 months.

So how do we actually specify the number of timesteps within our Python script?

It’s done through creating two special data structures:

* One data structure that we’ll call `x_training_data` that contains the last 40 stock price observations in the data set. This is the data that the recurrent neural network will use to make predictions.
* One data structure that we’ll call `y_training_data` that contains the stock price for the next trading day. This is the data point that the recurrent neural network is trying to predict.

To start, let’s initialize each of these data structures as an empty Python list:

```py

x_training_data = []

y_training_data =[]


```

Now we will use a for loop to populate the actual data into each of these Python lists. Here’s the code (with further explanation of the code after the code block):

```py

for i in range(40, len(training_data)):

    x_training_data.append(training_data[i-40:i, 0])

    y_training_data.append(training_data[i, 0])


```

Let’s unpack the components of this code block:

* The `range(40, len(training_data))` function causes the for loop to iterate from `40` to the last index of the training data.
* The `x_training_data.append(training_data[i-40:i, 0])` line causes the loop to append the 40 preceding stock prices to `x_training_data` with each iteration of the loop.
* Similarly, the `y_training_data.append(training_data[i, 0])` causes the loop to append the next day’s stock price to `y_training_data` with each iteration of the loop.

## **Finalizing Our Data Sets By Transforming Them Into NumPy Arrays**

TensorFlow is designed to work primarily with NumPy arrays. Because of this, the last thing we need to do is transform the two Python lists we just created into NumPy arrays.

Fortunately, this is simple. You simply need to wrap the Python lists in the `np.array` function. Here’s the code:

```py

x_training_data = np.array(x_training_data)

y_training_data = np.array(y_training_data)


```

One important way that you can make sure your script is running as intended is to verify the shape of both NumPy arrays.

The `x_training_data` array should be a two-directional NumPy array with one dimension being `40` (the number of timesteps) and the second dimension being `len(training_data) - 40`, which evaluates to `1218` in our case.

Similarly, the `y_training_data` object should be a one-dimensional NumPy array of length `1218` (which, again, is `len(training_data) - 40`).

You can verify the shape of the arrays by printing their `shape` attribute, like this:

```py

print(x_training_data.shape)

print(y_training_data.shape)


```

This prints:

```py

(1218, 40)

(1218,)


```

Both arrays have the dimensions you’d expect. However, we need to reshape our `x_training_data` object one more time before proceeding to build our recurrent neural network.

The reason for this is that the recurrent neural network layer available in TensorFlow only accepts data in a very specific format. You can read the TensorFlow documentation on this topic [here](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RNN#input_shape).

To reshape the `x_training_data` object, I will use the [np.reshape](https://nickmccullum.com/numpy-np-reshape/) method. Here’s the code to do this:

```py

x_training_data = np.reshape(x_training_data, (x_training_data.shape[0], 

                                               x_training_data.shape[1], 

                                               1))


```

Now let’s print the shape of `x_training_data` once again:

```py

print(x_training_data.shape)


```

This outputs:

```py

(1218, 40, 1)


```

Our arrays have the desired shape, so we can proceed to building our recurrent neural network.

## **Importing Our TensorFlow Libraries**

Before we can begin building our recurrent neural network, we’ll need to import a number of classes from TensorFlow. Here are the statements you should run before proceeding:

```py

from tensorflow.keras.models import Sequential

from tensorflow.keras.layers import Dense

from tensorflow.keras.layers import LSTM

from tensorflow.keras.layers import Dropout


```

## **Building Our Recurrent Neural Network**

It’s now time to build our recurrent neural network.

The first thing that needs to be done is initializing an object from TensorFlow’s `Sequential` class. As its name implies, the `Sequential` class is designed to build neural networks by adding sequences of layers over time.

Here’s the code to initialize our recurrent neural network:

```py

rnn = Sequential()


```

As with our [artificial neural networks](https://nickmccullum.com/python-deep-learning/artificial-neural-network-tutorial/) and [convolutional neural networks](https://nickmccullum.com/python-deep-learning/convolutional-neural-network-tutorial/), we can add more layers to this recurrent neural network using the `add` method.

## **Adding Our First LSTM Layer**

The first layer that we will add is an [LSTM](https://nickmccullum.com/python-deep-learning/lstms-long-short-term-memory-networks/) layer. To do this, pass an invocation of the `LSTM` class (that we just imported) into the `add` method.

The `LSTM` class accepts several parameters. More precisely, we will specify three arguments:

* The number of LSTM neurons that you’d like to include in this layer. Increasing the number of neurons is one method for increasing the dimensionality of your recurrent neural network. In our case, we will specify `units = 45`.
* `return_sequences = True` - this must always be specified if you plan on including another LSTM layer after the one you’re adding. You should specify `return_sequences = False` for the last LSTM layer in your recurrent neural network.
* `input_shape`: the number of timesteps and the number of predictors in our training data. In our case, we are using `40` timesteps and only `1` predictor (stock price), so we will add

Here is the full `add` method:

```py

rnn.add(LSTM(units = 45, return_sequences = True, input_shape = (x_training_data.shape[1], 1)))


```

Note that I used `x_training_data.shape[1]` instead of the hardcoded value in case we decide to train the recurrent neural network on a larger model at a later date.

## **Adding Some Dropout Regularization**

[Dropout regularization](https://machinelearningmastery.com/dropout-for-regularizing-deep-neural-networks/) is a technique used to avoid overfitting when training neural networks.

It involves randomly excluding - or “dropping out” - certain layer outputs during the training stage.

TensorFlow makes it easy to implement dropout regularization using the `Dropout` class that we imported earlier in our Python script. The `Dropout` class accepts a single parameter: the dropout rate.

The dropout rate indicates how many neurons should be dropped in a specific layer of the neural network. It is common to use a dropout rate of 20%. We will follow this convention in our recurrent neural network.

Here’s how you can instruct TensorFlow to drop 20% of the LSTM layer’s neuron during each iteration of the training stage:

```py

rnn.add(Dropout(0.2))


```

## **Adding Three More LSTM Layers With Dropout Regularization**

We will now add three more LSTM layers (with dropout regularization) to our recurrent neural network. You will see that after specifying the first LSTM layer, adding more is trivial.

To add more layers, all that needs to be done is copying the first two `add` methods with one small change. Namely, we should remove the `input_shape` argument from the `LSTM` class.

We will keep the number of neurons (or `units`) and the dropout rate the same in each of the `LSTM` class invocations. Since the third `LSTM` layer we’re adding in this section will be our last LSTM layer, we can remove the `return_sequences = True` parameter as mentioned earlier. Removing the parameter sets `return_sequences` to its default value of `False`.

Here’s the full code to add our next three LSTM layers:

```py

rnn.add(LSTM(units = 45, return_sequences = True))

rnn.add(Dropout(0.2))

rnn.add(LSTM(units = 45, return_sequences = True))

rnn.add(Dropout(0.2))

rnn.add(LSTM(units = 45))

rnn.add(Dropout(0.2))


```

This code is very repetitive and violates the DRY (Don’t repeat yourself) principle of software development. Let’s nest it in a loop instead:

```py

for i in [True, True, False]:

    rnn.add(LSTM(units = 45, return_sequences = i))

    rnn.add(Dropout(0.2))


```

## **Adding The Output Layer To Our Recurrent Neural Network**

Let’s finish architecting our recurrent neural network by adding our output layer.

The output layer will be an instance of the `Dense` class, which is the same class we used to create [the full connection layer](https://nickmccullum.com/python-deep-learning/flattening-full-connection/) of our convolutional neural network earlier in this course.

The only parameter we need to specify is `units` , which is the desired number of dimensions that the output layer should generate. Since we want to output the next day’s stock price (a single value), we’ll specify `units = 1`.

Here’s the code to create our output layer:

```py

rnn.add(Dense(units = 1))


```

## **Compiling Our Recurrent Neural Network**

As you’ll recall from the tutorials on artificial neural networks and convolutional neural networks, the compilation step of building a neural network is where we specify the neural net’s optimizer and loss function.

TensorFlow allows us to compile a neural network using the aptly-named `compile` method. It accepts two arguments: `optimizer` and `loss`. Let’s start by creating an empty `compile` function:

```py

rnn.compile(optimizer = '', loss = '')


```

We now need to specify the `optimizer` and `loss` parameters.

Let’s start by discussing the `optimizer` parameter. Recurrent neural networks typically use the RMSProp optimizer in their compilation stage. With that said, we will use the Adam optimizer (as before). The Adam optimizer is a workhorse optimizer that is useful in a wide variety of neural network architectures.

The `loss` parameter is fairly simple. Since we’re predicting a continuous variable, we can use mean squared error - just like you would when measuring the performance of a [linear regression machine learning model](https://nickmccullum.com/python-machine-learning/linear-regression-python/). This means we can specify `loss = mean_squared_error`.

Here’s the final `compile` method:

```py

rnn.compile(optimizer = 'adam', loss = 'mean_squared_error')


```

## **Fitting The Recurrent Neural Network On The Training Set**

It’s now time to train our recurrent network on our training data.

To do this, we use the `fit` method. The `fit` method accepts four arguments in this case:

* **The training data**: in our case, this will be `x_training_data` and `y_training_data`
* **Epochs**: the number of iterations you’d like the recurrent neural network to be trained on. We will specify `epochs = 100` in this case.
* **The batch size**: the size of batches that the network will be trained in through each epoch.

Here is the code to train this recurrent neural network according to our specifications:

```py

rnn.fit(x_training_data, y_training_data, epochs = 100, batch_size = 32)


```

Your Jupyter Notebook will now generate a number of printed outputs for every epoch in the training algorithm. They look like this:

![Machine learning training outputs](https://nickmccullum.com/images/python-deep-learning/recurrent-neural-networks/training.png)

As you can see, every output shows how long the epoch took to compute as well as the computed loss function at that epoch.

You should see the loss function’s value slowly decline as the recurrent neural network is fitted to the training data over time. In my case, the loss function’s value declined from `0.0504` in the first iteration to `0.0017` in the last iteration.

## **Making Predictions With Our Recurrent Neural Network**

We have built our recurrent neural network and trained it on data of Facebook’s stock price over the last 5 years. It’s now time to make some predictions!

### **Importing Our Test Data**

To start, let’s import the actual stock price data for the first month of 2020. This will give us something to compare our predicted values to.

Here’s the code to do this. Note that it is very similar to the code that we used to import our training data at the start of our Python script:

```py

test_data = pd.read_csv('FB_test_data.csv')

test_data = test_data.iloc[:, 1].values


```

If you run the statement `print(test_data.shape)`, it will return `(21,)`. This shows that our test data is a one-dimensional NumPy array with 21 entries - which means there were 21 stock market trading days in January 2020.

You can also generate a quick plot of the data using `plt.plot(test_data)`. This should generate the following Python visualization:

![A visualization of our test data](https://nickmccullum.com/images/python-deep-learning/recurrent-neural-networks/test_data.png)

With any luck, our predicted values should follow the same distribution.

### **Building The Test Data Set We Need To Make Predictions**

Before we can actually make predictions for Facebook’s stock price in January 2020, we first need to make some changes to our data set.

The reason for this is that to predict each of the `21` observations in January, we will need the `40` previous trading days. Some of these trading days will come from the test set while the remainder will come from the training set. Because of this, some [concatenation](https://nickmccullum.com/advanced-python/how-to-concatenate-pandas-dataframes/) is necessary.

Unfortunately, you can just concatenate the NumPy arrays immediately. This is because we’ve already applied feature scaling to the training data but haven’t applied any feature scaling to the test data.

To fix this, we need to re-import the original `x_training_data` object under a new variable name called `unscaled_x_training_data`. For consistency, we will also re-import the test data as a DataFrame called `unscaled_test_data`:

```py

unscaled_training_data = pd.read_csv('FB_training_data.csv')

unscaled_test_data = pd.read_csv('FB_test_data.csv')


```

Now we can concatenate together the `Open` column from each DataFrame with the following statement:

```py

all_data = pd.concat((unscaled_x_training_data['Open'], unscaled_test_data['Open']), axis = 0)


```

This `all_data` object is a pandas Series of length 1279.

Now we need to create an array of all the stock prices from January 2020 and the 40 trading days prior to January. We will call this object `x_test_data` since it contains the `x` values that we’ll use to make stock price predictions for January 2020.

The first thing you need to do is find the index of the first trading day in January within our `all_data` object. The statement `len(all_data) - len(test_data)` identifies this index for us.

This represents the upper bound of the first item in the array. To get the lower bound, just subtract `40` from this number. Said differently, the lower bound is `len(all_data) - len(test_data) - 40`.

The upper bound of the entire `x_test_data` array will be the last item in the data set. Accordingly, we can create this NumPy array with the following statement:

```py

x_test_data = all_data[len(all_data) - len(test_data) - 40:].values


```

You can check whether or not this object has been created as desired by printing `len(x_test_data)`, which has a value of `61`. This makes sense - it should contain the `21` values for January 2020 as well as the `40` values prior.

The last step of this section is to quickly reshape our NumPy array to make it suitable for the `predict` method:

```py

x_test_data = np.reshape(x_test_data, (-1, 1))


```

Note that if you neglected to do this step, TensorFlow would print a handy message that would explain exactly how you’d need to transform your data.

### **Scaling Our Test Data**

Our recurrent neural network was trained on scaled data. Because of this, we need to scale our `x_test_data` variable before we can use the model to make predictions.

```py

x_test_data = scaler.transform(x_test_data)


```

Note that we used the `transform` method here instead of the `fit_transform` method (like before). This is because we want to transform the test data according to the fit generated from the entire training data set.

This means that the transformation that is applied to the test data will be the same as the one applied to the training data - which is necessary for our recurrent neural network to make accurate predictions.

### **Grouping Our Test Data**

The last thing we need to do is group our test data into `21` arrays of size `40`. Said differently, we’ll now create an array where each entry corresponds to a date in January and contains the stock prices of the `40` previous trading days.

The code to do this is similar to something we used earlier:

```py

final_x_test_data = []

for i in range(40, len(x_test_data)):

    final_x_test_data.append(x_test_data[i-40:i, 0])

final_x_test_data = np.array(final_x_test_data)


```

Lastly, we need to reshape the `final_x_test_data` variable to meet TensorFlow standards.

We saw this previously, so the code should need no explanation:

```py

final_x_test_data = np.reshape(final_x_test_data, (final_x_test_data.shape[0], 

                                               final_x_test_data.shape[1], 

                                               1))


```

### **Actually Making Predictions**

After an absurd amount of data reprocessing, we are now ready to make predictions using our test data!

This step is simple. Simply pass in our `final_x_test_data` object into the `predict` method called on the `rnn` object. As an example, here is how you could generate these predictions and store them in an aptly-named variable called `predictions`:

```py

predictions = rnn.predict(final_x_test_data)


```

Let’s plot these predictions by running `plt.plot(predictions)` (note that you’ll need to run `plt.clf()` to clear your canvas first):

![The original predictions from our recurrent neural network](https://nickmccullum.com/images/python-deep-learning/recurrent-neural-networks/original_predictions.png)

As you can see, the predicted values in this plot are all between `0` and `1`. This is because our data set is still scaled! We need to un-scale it for the predictions to have any practical meaning.

The `MinMaxScaler` class that we used to originally scale our data set comes with a useful `inverse_transform` method to un-scale the data. Here’s how you could un-scale the data and generate a new plot:

```py

unscaled_predictions = scaler.inverse_transform(predictions)

plt.clf() #This clears the first prediction plot from our canvas

plt.plot(unscaled_predictions)


```

![The unscaled predictions from our recurrent neural network](https://nickmccullum.com/images/python-deep-learning/recurrent-neural-networks/unscaled-predictions.png)

This looks much better! Anyone who’s followed Facebook’s stock price for any length of time can see that this seems fairly close to where Facebook has actually traded.

Let’s generate plot that compares our predicted stock prices with Facebook’s actual stock price:

```py

plt.plot(unscaled_predictions, color = '#135485', label = "Predictions")

plt.plot(test_data, color = 'black', label = "Real Data")

plt.title('Facebook Stock Price Predictions')


```

## **The Full Code For This Tutorial**

You can view the full code for this tutorial in [this GitHub repository](https://github.com/nicholasmccullum/python-deep-learning). It is also pasted below for your reference:

```py

#Import the necessary data science libraries

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

#Import the data set as a pandas DataFrame

training_data = pd.read_csv('FB_training_data.csv')

#Transform the data set into a NumPy array

training_data = training_data.iloc[:, 1].values

#Apply feature scaling to the data set

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

training_data = scaler.fit_transform(training_data.reshape(-1, 1))

#Initialize our x_training_data and y_training_data variables 

#as empty Python lists

x_training_data = []

y_training_data =[]

#Populate the Python lists using 40 timesteps

for i in range(40, len(training_data)):

    x_training_data.append(training_data[i-40:i, 0])

    y_training_data.append(training_data[i, 0])

    

#Transforming our lists into NumPy arrays

x_training_data = np.array(x_training_data)

y_training_data = np.array(y_training_data)

#Verifying the shape of the NumPy arrays

print(x_training_data.shape)

print(y_training_data.shape)

#Reshaping the NumPy array to meet TensorFlow standards

x_training_data = np.reshape(x_training_data, (x_training_data.shape[0], 

                                               x_training_data.shape[1], 

                                               1))

#Printing the new shape of x_training_data

print(x_training_data.shape)

#Importing our TensorFlow libraries

from tensorflow.keras.models import Sequential

from tensorflow.keras.layers import Dense

from tensorflow.keras.layers import LSTM

from tensorflow.keras.layers import Dropout

#Initializing our recurrent neural network

rnn = Sequential()

#Adding our first LSTM layer

rnn.add(LSTM(units = 45, return_sequences = True, input_shape = (x_training_data.shape[1], 1)))

#Perform some dropout regularization

rnn.add(Dropout(0.2))

#Adding three more LSTM layers with dropout regularization

for i in [True, True, False]:

    rnn.add(LSTM(units = 45, return_sequences = i))

    rnn.add(Dropout(0.2))

#(Original code for the three additional LSTM layers)

# rnn.add(LSTM(units = 45, return_sequences = True))

# rnn.add(Dropout(0.2))

# rnn.add(LSTM(units = 45, return_sequences = True))

# rnn.add(Dropout(0.2))

# rnn.add(LSTM(units = 45))

# rnn.add(Dropout(0.2))

#Adding our output layer

rnn.add(Dense(units = 1))

#Compiling the recurrent neural network

rnn.compile(optimizer = 'adam', loss = 'mean_squared_error')

#Training the recurrent neural network

rnn.fit(x_training_data, y_training_data, epochs = 100, batch_size = 32)

#Import the test data set and transform it into a NumPy array

test_data = pd.read_csv('FB_test_data.csv')

test_data = test_data.iloc[:, 1].values

#Make sure the test data's shape makes sense

print(test_data.shape)

#Plot the test data

plt.plot(test_data)

#Create unscaled training data and test data objects

unscaled_training_data = pd.read_csv('FB_training_data.csv')

unscaled_test_data = pd.read_csv('FB_test_data.csv')

#Concatenate the unscaled data

all_data = pd.concat((unscaled_x_training_data['Open'], unscaled_test_data['Open']), axis = 0)

#Create our x_test_data object, which has each January day + the 40 prior days

x_test_data = all_data[len(all_data) - len(test_data) - 40:].values

x_test_data = np.reshape(x_test_data, (-1, 1))

#Scale the test data

x_test_data = scaler.transform(x_test_data)

#Grouping our test data

final_x_test_data = []

for i in range(40, len(x_test_data)):

    final_x_test_data.append(x_test_data[i-40:i, 0])

final_x_test_data = np.array(final_x_test_data)

#Reshaping the NumPy array to meet TensorFlow standards

final_x_test_data = np.reshape(final_x_test_data, (final_x_test_data.shape[0], 

                                               final_x_test_data.shape[1], 

                                               1))

#Generating our predicted values

predictions = rnn.predict(final_x_test_data)

#Plotting our predicted values

plt.clf() #This clears the old plot from our canvas

plt.plot(predictions)

#Unscaling the predicted values and re-plotting the data

unscaled_predictions = scaler.inverse_transform(predictions)

plt.clf() #This clears the first prediction plot from our canvas

plt.plot(unscaled_predictions)

#Plotting the predicted values against Facebook's actual stock price

plt.plot(unscaled_predictions, color = '#135485', label = "Predictions")

plt.plot(test_data, color = 'black', label = "Real Data")

plt.title('Facebook Stock Price Predictions')


```

## **Summary - The Intuition Behind Recurrent Neural Networks**

In this tutorial, you learned how to build and train a recurrent neural network.

Here is a brief summary of what you learned:

* How to apply feature scaling to a data set that a recurrent neural network will be trained on
* The role of `timesteps` in training a recurrent neural network
* That TensorFlow primarily uses NumPy arrays as the data structure to train models with
* How to add `LSTM` and `Dropout` layers to a recurrent neural network
* Why dropout regularization is commonly used to avoid overfitting when training neural networks
* That the `Dense` layer from TensorFlow is commonly used as the output layer of a recurrent neural network
* That the `compilation` step of building a neural network involves specifying its optimizer and its loss function
* How to make predictions using a recurrent neural network
* That predictions make using a neural network trained on scaled data must be unscaled to be interpretable by humans

If you found this post helpful, check out my book [Pragmatic Machine Learning](https://gumroad.com/l/pGjwd) for a project-based guide on deep learning models covered here and in [my other articles](https://www.freecodecamp.org/news/author/nick/).

%[https://gumroad.com/l/pGjwd]


