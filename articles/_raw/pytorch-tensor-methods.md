---
title: PyTorch Tensor Methods – How to Create Tensors in Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-12-03T17:00:26.000Z'
originalURL: https://freecodecamp.org/news/pytorch-tensor-methods
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5fc667ad49c47664ed828110.jpg
tags:
- name: Python
  slug: python
- name: pytorch
  slug: pytorch
- name: tensor
  slug: tensor
seo_title: null
seo_desc: 'By Srijan

  PyTorch is an open-source Python-based library. It provides high flexibility and
  speed while building, training, and deploying deep learning models.

  At its core, PyTorch involves operations involving tensors. A tensor is a number,
  vector, m...'
---

By Srijan

PyTorch is an open-source Python-based library. It provides high flexibility and speed while building, training, and deploying deep learning models.

At its core, PyTorch involves operations involving _tensors._ A tensor is a number, vector, matrix, or any n-dimensional array.

In this article, we will see different ways of creating tensors using PyTorch tensor methods (functions).

## Topics we'll cover

* tensor
* zeros
* ones
* full
* arange
* linspace
* rand
* randint
* eye
* complex

### The tensor() method

This method returns a tensor when `data` is passed to it. `data` can be a scalar, tuple, a list or a _NumPy_ array.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=76" title="Jovian Viewer" height="158" width="800" frameborder="0" scrolling="auto"></iframe>

In the above example, a NumPy array that was created using `np.arange()` was passed to the `tensor()` method, resulting in a 1-D tensor.

We can create a multi-dimensional tensor by passing a tuple of tuples, a list of lists, or a multi-dimensional NumPy array.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=77" title="Jovian Viewer" height="179" width="800" frameborder="0" scrolling="auto"></iframe>

When an empty tuple or list is passed into `tensor()`, it creates an empty tensor.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=78" title="Jovian Viewer" height="158" width="800" frameborder="0" scrolling="auto"></iframe>

### The zeros() method

This method returns a tensor where all elements are zeros, of specified `size` (shape). The `size` **can** be given as a tuple or a list or neither.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=4" title="Jovian Viewer" height="200" width="800" frameborder="0" scrolling="auto"></iframe>

We could have passed `3, 2` inside a tuple or a list as well. It is self-explainable that passing negative numbers or a float would result in a run time error.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=8" title="Jovian Viewer" height="318" width="800" frameborder="0" scrolling="auto"></iframe>

Passing an empty tuple or an empty list gives a tensor of size (dimension) 0, having 0 as its only element, whose data type is float.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=10" title="Jovian Viewer" height="205" width="800" frameborder="0" scrolling="auto"></iframe>

### The ones() method

Similar to `zeros()`, `ones()` returns a tensor where all elements are 1, of specified `size` (shape). The `size` **can** be given as a tuple or a list or neither.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/53&cellId=19" title="Jovian Viewer" height="400" width="800" frameborder="0" scrolling="auto"></iframe>

Like `zeros()`, passing an empty tuple or list gives a tensor of 0 dimension, having 1 as the sole element, whose data type is float.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=23" title="Jovian Viewer" height="205" width="800" frameborder="0" scrolling="auto"></iframe>

### The full() method

What if you want all the elements of a tensor to be equal to some value but not only 0 and 1? Maybe 2.9?

`full()` returns a tensor of a shape given by the `size` argument, with all its elements equal to the `fill_value`.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=27" title="Jovian Viewer" height="200" width="800" frameborder="0" scrolling="auto"></iframe>

Here, we have created a tensor of shape `3, 2` with the `fill_value` as 3. Here again, passing an empty tuple or list creates a scalar tensor of zero dimension.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=31" title="Jovian Viewer" height="158" width="800" frameborder="0" scrolling="auto"></iframe>

While using `full`, it is **necessary** to give `size` as a tuple or a list.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=33" title="Jovian Viewer" height="444" width="800" frameborder="0" scrolling="auto"></iframe>

### The arange() method

This method returns a 1-D tensor, with elements from `start` (inclusive) to `end` (exclusive) with a common difference `step`. The default value for `start` is 0 while that for `step` is 1.

The elements of the tensor can be said to be in **Arithmetic Progression**, with `step` as common difference.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=37" title="Jovian Viewer" height="158" width="800" frameborder="0" scrolling="auto"></iframe>

Here, we created a tensor which starts from 2 and goes until 20 with a `step` (common difference) of 2.

All the three parameters, `start`, `end` and `step` can be positive, negative or float.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=41" title="Jovian Viewer" height="297" width="800" frameborder="0" scrolling="auto"></iframe>

While choosing `start`, `end`, and `step`, we need to ensure that `start` and `end` are consistent with the `step` sign.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=41" title="Jovian Viewer" height="297" width="800" frameborder="0" scrolling="auto"></iframe>

Since `step` is set as -2, there is no way -42 can reach -22 (exclusive). Hence, it gives an error.

### The linspace() method

This method returns a 1-D dimensional tensor, with elements from `start` (inclusive) to `end` (inclusive). However, unlike `arange()`, here, `steps` isn't the common difference but the number of elements to be in the tensor.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=45" title="Jovian Viewer" height="158" width="800" frameborder="0" scrolling="auto"></iframe>

PyTorch automatically decides the common difference based on the `steps` given.

Not providing a value for `steps` is deprecated. For _backwards compatibility_, not providing a value for steps creates a tensor with **100** elements. According to the official documentation, in a future PyTorch release, failing to provide a value for steps will throw a runtime error.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=47" title="Jovian Viewer" height="748" width="800" frameborder="0" scrolling="auto"></iframe>

Unlike `arange()`, `linspace` can have a `start` greater than `end` since the common difference is automatically calculated.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=49" title="Jovian Viewer" height="158" width="800" frameborder="0" scrolling="auto"></iframe>

Since `steps` here is not a common difference, but the number of elements, it can only be a non-negative integer.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=51" title="Jovian Viewer" height="297" width="800" frameborder="0" scrolling="auto"></iframe>

### The rand() method

This method returns a tensor filled with random numbers from a uniform distribution on the interval 0 (inclusive) to 1 (exclusive). The shape is given by the `size` argument. The `size` argument can be given as a tuple or list or neither.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=55" title="Jovian Viewer" height="200" width="800" frameborder="0" scrolling="auto"></iframe>

Passing an empty tuple or list creates a scalar tensor of zero dimension.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=56" title="Jovian Viewer" height="158" width="800" frameborder="0" scrolling="auto"></iframe>

### The randint() method

This method returns a tensor filled with random integers generated uniformly between `low` (inclusive) and `high` (exclusive). The shape is given by the `size` argument. The default value for `low` is 0.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=59" title="Jovian Viewer" height="242" width="800" frameborder="0" scrolling="auto"></iframe>

When only one `int` argument is passed, `low` gets the value 0, by default, and `high` gets the passed value.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=60" title="Jovian Viewer" height="200" width="800" frameborder="0" scrolling="auto"></iframe>

The `size` argument only takes a tuple or a list. An empty tuple or list creates a tensor with zero dimension.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=62" title="Jovian Viewer" height="318" width="800" frameborder="0" scrolling="auto"></iframe>

### The eye() method

This method returns a 2-D tensor with ones on the diagonal and zeros elsewhere. The number of rows is given by `n` and columns is given by `m`.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=65" title="Jovian Viewer" height="179" width="800" frameborder="0" scrolling="auto"></iframe>

The default value for `m` is the value of `n`. When only `n` is passed, it creates a tensor in the form of an **identity matrix**. An identity matrix has its diagonal elements as 1 and all others as 0. 

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=66" title="Jovian Viewer" height="242" width="800" frameborder="0" scrolling="auto"></iframe>

### The complex() method

This method returns a complex tensor with its real part equal to `real` and its imaginary part equal to `imag`. Both `real` and `imag` are tensors.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=69" title="Jovian Viewer" height="363" width="800" frameborder="0" scrolling="auto"></iframe>

The data type of both the `real` and `imag` tensors should be either `float` or `double`.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=70" title="Jovian Viewer" height="523" width="800" frameborder="0" scrolling="auto"></iframe>

Also, the `size` of both tensors, `real` and `imag`, should be the same, since the corresponding elements of the two matrices form a complex number.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=72" title="Jovian Viewer" height="499" width="800" frameborder="0" scrolling="auto"></iframe>

## Conclusion

We've covered ten different ways to create tensors using PyTorch methods. You can go through the [official documentation](https://pytorch.org/docs/stable/torch.html) to know more about other PyTorch methods. 

You can click [here](https://jovian.ai/srijansrj5901/different-ways-to-create-tensors) to go to the Jupyter notebook where you can play around with these methods.

If you want to learn more about PyTorch, check out [this](https://jovian.ai/learn/deep-learning-with-pytorch-zero-to-gans) amazing course on freeCodeCamp's [YouTube](https://www.youtube.com/watch?v=5ioMqzMRFgM&t=3s&ab_channel=freeCodeCamp.org) channel.

Stay safe!

