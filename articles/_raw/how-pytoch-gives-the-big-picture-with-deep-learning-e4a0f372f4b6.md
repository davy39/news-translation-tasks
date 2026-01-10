---
title: How Pytorch gives the big picture with deep learning
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-05T21:08:16.000Z'
originalURL: https://freecodecamp.org/news/how-pytoch-gives-the-big-picture-with-deep-learning-e4a0f372f4b6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*lMTOQkDLUcOOwX4WJ-7tFw.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Data Science
  slug: data-science
- name: Deep Learning
  slug: deep-learning
- name: Machine Learning
  slug: machine-learning
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Déborah Mesquita

  Some time ago we saw how to classify texts with neural networks. The article covered
  the following topics:


  What is a machine learning model

  What is a neural network

  How the neural network learns

  How to manipulate data and pass it...'
---

By Déborah Mesquita

Some time ago we saw [how to classify texts with neural networks](https://medium.freecodecamp.org/big-picture-machine-learning-classifying-text-with-neural-networks-and-tensorflow-d94036ac2274). The article covered the following topics:

* What is a machine learning model
* What is a neural network
* How the neural network learns
* How to manipulate data and pass it to the neural network inputs
* How to run the model and get the results for the prediction

In today’s article, we are going to build the same network, but instead of using [TensorFlow](https://www.tensorflow.org/), we are going to use [**Pytorch**](http://pytorch.org/)**.** We’ll focus only on the code. So if you need a primer on neural networks, it’s a good idea to check out the [previous article](https://medium.freecodecamp.org/big-picture-machine-learning-classifying-text-with-neural-networks-and-tensorflow-d94036ac2274). :)

We’ll create a machine learning model that classifies texts into categories. The dataset is the [20 Newsgroups](http://qwone.com/~jason/20Newsgroups/), which contains 18,000 posts about 20 different topics. We will use only 3 categories: comp.graphics, sci.space, and rec.sport.baseball.

### What is Pytorch?

> Pytorch is a Python-based scientific computing package that is a replacement for [NumPy](http://www.numpy.org/), and uses the power of Graphics Processing Units. It is also a deep learning research platform that provides maximum flexibility and speed.

The biggest difference between Pytorch and Tensorflow is that Pytorch can create graphs on the fly. This makes debugging so much easier (and fun!).

![Image](https://cdn-media-1.freecodecamp.org/images/0*nntIflaBvptIerl8.gif)
_A primer on Pytorch dynamics_

When you execute a line of code, it gets executed. There isn’t an asynchronous view of the world. When you drop it into a debugger, or receive error messages and stack traces, understanding them is straight forward. The stack trace points to exactly where your code was defined.

### Building the network

Ok, let’s see how things work in Pytorch.

#### The basics

As usual, we have **tensors**, which are multi-dimensional matrices that contain elements of a single data type.

The **torch** package contains data structures for multi-dimensional tensors and mathematical operations.

* [**torch.nn**](http://pytorch.org/docs/master/nn.html) is a neural network library deeply integrated with autograd, and is designed for maximum flexibility
* [**torch.autograd**](http://pytorch.org/tutorials/beginner/former_torchies/autograd_tutorial.html) is a tape-based automatic differentiation library that supports all differentiable Tensor operations in torch

#### Step 1: Define the network

With TensorFlow each layer operation has to be explicitly named:

With Pytorch we use **torch.nn**. We need to multiply each input node with a weight, and also to add a bias. The class`**torch.nn.Linear**` does the job for us.

* `**torch.nn.Linear**` applies a linear transformation to the incoming data, _y_=_Ax_+_b_

The base class for all neural network modules is **torch.nn.Module**. The `**forward**`(*input) defines the computation performed at every call, and all subclasses should override it.

Cool, right?

#### Step 2: Update the weights

The way the neural network “learns” is by updating the weight values. With Pytorch we use the **torch.autograd** package to do that.

**Torch.autograd.Variable** wraps a tensor and records the operations applied to it. This is very handy and allows us to work with the gradient descent in a very simple way. Let’s have a closer look at the documentation.

A variable is **a thin wrapper around a Tensor object that also holds the gradient** and a reference to the function that created it. This reference allows us to trace the entire chain of operations that created the data.

![Image](https://cdn-media-1.freecodecamp.org/images/0*VXak2OuzwdAUYt2c.png)
_Variable_

We didn’t specify the weight tensors like we did with TensorFlow because the `**torch.nn.Linear**` class has a variable **weight** with shape (out_features x in_features).

* `**torch.nn.Linear**`(in_features, out_features, bias=True)

To compute the gradient, we will use the the method [Adaptive Moment Estimation (Adam)](http://sebastianruder.com/optimizing-gradient-descent/index.html#adam). **Torch.optim** is a package that implements various optimization algorithms.

To use `[**torch.optim**](http://pytorch.org/docs/master/optim.html#module-torch.optim)`, you have to construct an optimizer object that will hold the current state and also update the parameters based on the computed gradients.

To construct an `[**optimizer**](http://pytorch.org/docs/master/optim.html#torch.optim.Optimizer)**,**` you have to give it an iterable that contains the parameters (all should be `[**variable**](http://pytorch.org/docs/master/autograd.html#torch.autograd.Variable)**s**` ) to optimize. Then you can specify options that are specific to an optimizer, such as the learning rate, weight decay, etc.

Let’s construct our optimizer:

The `**parameters()**` method from **torch.nn.Module** returns an iterator over the module parameters. To compute the loss we’ll use `**torch.nn.CrossEntropyLoss**`

One important thing about `**torch.nn.CrossEntropyLoss**` is that input has to be a 2D tensor of size (minibatch, n) and target expects a class index (0 to nClasses-1) as the target for each value of a 1D tensor of size minibatch. For example:

So we need to change the `get_batch()` function from the previous article to work like it does in the example above.

Now let’s update the weights and see the magic of the variables.

The method **torch.autograd.backward** computes the sum of the gradients for given variables. As the documentation says, this function accumulates gradients in the leaves, **so you might need to zero them before calling them**. To update the parameters, all optimizers implement a `[**step()**](http://pytorch.org/docs/master/optim.html#torch.optim.Optimizer.step)` method. The functions can be called once the gradients are computed, for example you can use `[**backward(**](http://pytorch.org/docs/master/autograd.html#torch.autograd.Variable.backward)**)**` to call them.

In the [neural network terminology](http://stackoverflow.com/questions/4752626/epoch-vs-iteration-when-training-neural-networks), one epoch equals one forward pass (getting the output values), and one backward pass (updating the weights) equals **_all_** the training examples. In our network, the `get_batch()` function gives us the number of texts with the size of the batch.

Putting it all together, we get this:

And that’s it.

I never thought I would say this about a piece of code, but it’s beautiful.

Isn’t it?

Now let’s test the model:

And that’s it.

You have created a model using a neural network to classify texts into categories.

Congratulations. ?

You can see the notebook with the **final code** [here](https://github.com/dmesquita/understanding_pytorch_nn).

Did you found this article helpful? I try my best to write a deep dive article each month, you can [receive an email when I publish a new one](https://goo.gl/forms/SLrJDrGtxgAoILkt1).

