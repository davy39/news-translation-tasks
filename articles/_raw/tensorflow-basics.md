---
title: How to Use TensorFlow for Deep Learning – Basics for Beginners
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2023-02-14T23:46:51.000Z'
originalURL: https://freecodecamp.org/news/tensorflow-basics
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/tensorflow.jpeg
tags:
- name: Deep Learning
  slug: deep-learning
- name: neural networks
  slug: neural-networks
- name: tensor
  slug: tensor
- name: TensorFlow
  slug: tensorflow
seo_title: null
seo_desc: 'TensorFlow is a library that helps engineers build and train deep learning
  models. It provides all the tools we need to create neural networks.

  We can use TensorFlow to train simple to complex neural networks using large sets
  of data.

  TensorFlow is u...'
---

TensorFlow is a library that helps engineers build and train deep learning models. It provides all the tools we need to create neural networks.

We can use TensorFlow to train simple to complex neural networks using large sets of data.

TensorFlow is used in a variety of applications, from image and speech recognition to natural language processing and robotics. TensorFlow enables us to quickly and easily build powerful AI models with high accuracy and performance.

TensorFlow also works with GPUs and TPUs, which are types of computer chips built to extend TensorFlow’s capabilities. These chips make TensorFlow run faster, which is helpful when you have a lot of data to work with.

In this article, we will learn about tensors and how to work with tensors using TensorFlow. Let’s dive right in.

## What is a Tensor?

A simple explanation would be that a tensor is a multi-dimensional array.

![Image](https://miro.medium.com/max/1050/1*rLcM-j8b61Xlfk81k_exKw.png)
_Scalar, Vector, Matrix and Tensor_

A scalar is a single number. A vector is an array of numbers. A matrix is a 2-dimensional array. A tensor is an n-dimensional array.

In TensorFlow, everything can be considered a tensor including a scalar. A scalar would be a tensor of dimension 0, a vector of dimension 1, and a matrix of dimension 2.

Now, this is useful because we are not limited to working with complex datasets in TensorFlow. TensorFlow can handle any type of data and feed it to machine learning models.

## What is TensorFlow?

TensorFlow is an open-source software library for building neural networks. Google Brain team was the one who built it and it is the most popular deep learning library in the market today.

You can use TensorFlow to build AI models including image and speech recognition, natural language processing, and predictive modeling.

![Image](https://miro.medium.com/max/1050/1*mPUeOmKYoWvPcZFjMdsiUQ.gif)
_Classification neural network_

TensorFlow uses a dataflow graph to represent computations. To put it simply, TensorFlow has made it easy to build complex machine learning models.

TensorFlow takes care of a lot of work behind the scenes which makes it useful while building and training any type of machine learning model. TensorFlow also manages the computation, including parallelization and optimization, on the user’s behalf.

## TensorFlow and Keras

![Image](https://miro.medium.com/max/1050/1*X7QA_c8KHk7nD0tywv-OVg.png)
_Tensorflow and Keras_

TensorFlow has a high-level API called Keras. Keras was a standalone project which is now available within the TensorFlow library. Keras makes it easy to define and train models while TensorFlow provides more control over the computation.

TensorFlow supports a wide range of hardware, including CPUs, GPUs, and TPUs. TPUs are Tensor processing Unites, built specifically to work with Tensors and TensorFlow.

We can also run TensorFlow on mobile devices and IoT devices using TensorFlow Lite. TensorFlow also has a large community of developers, and it is updated with new features and capabilities.

## How to Build Tensors with TensorFlow

Let’s start writing some code. If you don't have TensorFlow installed, you can use a [Google colab notebook](https://colab.research.google.com/) to follow along.

Let’s start by importing TensorFlow and printing out the version.

```
import tensorflow as tf
print(tf.__version__)
```

```
OUTPUT:
2.9.2

```

Let’s first create a scalar using tf.constant. We use tf.constant to create a new constant value. We can also use tf.variable to create a variable value. We will then print the value and also check the dimension of the scalar using the ndim property. Its dimension will be zero because it is a single value.

```
scalar = tf.constant(7)
print(scalar)
print(scalar.ndim)
```

```
OUTPUT:
tf.Tensor(7, shape=(), dtype=int32)
0
```

Now let’s create a vector and print its dimensions. You can see that the dimension is 1.

```
vector = tf.constant([10,10])
print(vector)
print(vector.ndim)
```

```
OUTPUT:
tf.Tensor([10 10], shape=(2,), dtype=int32)
1
```

Now let’s try creating a matrix and printing its dimensions.

```
matrix = tf.constant([
    [10,11],
    [12,13]
])
print(matrix)
print(matrix.ndim)
```

```
OUTPUT:
tf.Tensor(
[[10 11]
 [12 13]], shape=(2, 2), dtype=int32)
2
```

You will see that the dimension is now 2. You can also see that the shape of the matrix is 2 by 2.

Shapes and dimensions are useful when working with TensorFlow because we will often change them while using these data to train neural networks.

We have seen that these tensors have a default datatype of int32. What if we want to create a dataset with a custom datatype?

tf.constant provides us with the dtype argument. Let’s create the same matrix again with float16 as the data type.

```
tensor_1 = tf.constant([
    [
        [1,2,3]
    ],
    [
        [4,5,6]
    ],
    [
        [7,8,9]
    ]
],dtype='float32')
print(tensor_1)
```

```
OUTPUT:
tf.Tensor(
[[[1. 2. 3.]]

 [[4. 5. 6.]]

 [[7. 8. 9.]]], shape=(3, 1, 3), dtype=float32)
```

Now let’s create a tensor. We will input a 3-dimensional array to tf.constant. We will also print its dimensions.

```
tensor = tf.constant([
    [
        [1,2,3]
    ],
    [
        [4,5,6]
    ],
    [
        [7,8,9]
    ]
])
print(tensor)
print(tensor.ndim)
```

```
OUTPUT:
tf.Tensor(
[[[1 2 3]]
 [[4 5 6]]
 [[7 8 9]]], shape=(3, 1, 3), dtype=int32)
3
```

Now we have a tensor of dimension 3 and shape 3 by 1 by 3. This is the simplest tensor you can create. In real-world scenarios, we will be dealing with tensors of higher dimensions and bigger shapes.

Now let’s look at how to create a variable tensor. We won’t be using variable tensors very often compared to constant tensors, but it is good to know that we have an option.

We will use tf.Variable to create a variable tensor. The difference between the constant tensor and variable tensor is that you can change the data in a variable tensor, but you can’t change the values in a constant tensor. Let’s create a variable tensor and print the dimensions.

```
var_tensor = tf.Variable([
    [
        [1,2,3]
    ],
    [
        [4,5,6]
    ],
    [
        [7,8,9]
    ]
])
print(var_tensor)
```

```
OUTPUT:
<tf.Variable 'Variable:0' shape=(3, 1, 3) dtype=int32, numpy=
array([[[1, 2, 3]],
       [[4, 5, 6]],
       [[7, 8, 9]]], dtype=int32)>
```

# How to Generate and Load Tensors

Let’s look at how to generate tensors. In most cases, you won’t be creating tensors from scratch. You will either load a dataset, convert other datasets like NumPy arrays to tensors, or generate tensors. First, let’s look at how to generate tensors.

Let’s create a tensor with random values. There are two common ways you can do this: generate a normal distribution of data or a uniform distribution of data.

![Image](https://miro.medium.com/max/1050/0*tRWkwBjuQvgi2rGG.png)
_Normal distribution_

The normal distribution is a bell-shaped curve that represents the distribution of data. Most of the data will be close to the average and fewer data will be away from the average. This means the probability of getting a value near the average is higher.

![Image](https://miro.medium.com/max/1050/0*SOM1PR1htTNzuRMS.png)
_Uniform distribution_

The uniform distribution is a straight line that represents the distribution of data. All the values in a uniform distribution will have an equal probability of occurring within a given range.

Before we generate random values, you must understand what a seed is. If we use a seed value, we can regenerate the same set of data multiple times. This will be useful when we want to test our machine-learning model against the same data after we tweak its performance.

Let’s create two arrays of random tensors. We will first set a seed and generate the random values using that seed.

```
seed = tf.random.Generator.from_seed(42)
```

Now we will create a normal and uniform distribution with the shape of 3 by 2.

```
normal_tensor = seed.normal(shape=(3,2))
print(normal_tensor)
uniform_tensor = seed.uniform(shape=(3,2))
print(uniform_tensor)
```

```
OUTPUT:
tf.Tensor( [[-0.7565803  -0.06854702]  [ 0.07595026 -1.2573844 ]  [-0.23193765 -1.8107855 ]], shape=(3, 2), dtype=float32)
tf.Tensor( [[0.7647915  0.03845465]  [0.8506975  0.20781887]  [0.711869   0.8843919 ]], shape=(3, 2), dtype=float32)
```

We have two tensors created, one with a normal distribution of random numbers and the other with a uniform distribution of random numbers.

Next, we will create a tensor with zeros and ones. In TensorFlow, tensors filled with zeros or ones are often used as a starting point for creating other tensors. They can also be placeholders for inputs in a computational graph.

To create a tensor of zeroes, use the tf.zeros function with a shape as the input argument. To create a tensor with ones, we use tf.ones with the shape as input argument.

```
zeros = tf.zeros(shape=(3,2))
print(zeros)
ones = tf.ones(shape=(3,2))
print(ones)
```

```
OUTPUT:
tf.Tensor(
[[0. 0.]
 [0. 0.]
 [0. 0.]], shape=(3, 2), dtype=float32)
tf.Tensor(
[[1. 1.]
 [1. 1.]
 [1. 1.]], shape=(3, 2), dtype=float32)
```

Now, let’s look at converting NumPy arrays into tensors. If you don’t know [what NumPy is](https://numpy.org/), it is a Python library for numerical computing. It helps us handle large datasets and perform a variety of computations on them.

Let’s import NumPy and create a NumPy array using NumPy’s arrange function.

```
import numpy as np
numpy_arr = np.arange(1,25,dtype=np.int32)
```

Now, we can create a tensor using the tf.constant function with the NumPy array as input. TensorFlow has built-in support to handle NumPy arrays, so it is just a matter of importing a NumPy array and setting a shape.

```
print(numpy_arr)
numpy_tensor = tf.constant(numpy_arr,shape=[2,4,3])
print(numpy_tensor)
```

```
OUTPUT:
[ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24]
tf.Tensor(
[[[ 1  2  3]
  [ 4  5  6]
  [ 7  8  9]
  [10 11 12]]
 [[13 14 15]
  [16 17 18]
  [19 20 21]
  [22 23 24]]], shape=(2, 4, 3), dtype=int32)
```

You can see both the NumPy array as well as our tensor. The original NumPy array was 1x12 but our tensor is 2x4x3. This is called re-shaping a tensor which we will often do while training deep neural networks.

# Basic Operations using Tensorflow

We have learned how tensors are created in TensorFlow. Now let’s look at some basic operations using tensors.

We will start by getting some information on our tensors. Let’s create a 4D tensor with 0 values with the shape 2x3x4x5.

```
rank4_tensor = tf.zeros([2,3,4,5])
print(rank4_tensor)
```

```
OUTPUT:
tf.Tensor(
[[[[0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]]
  [[0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]]
  [[0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]]]
 [[[0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]]
  [[0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]]
  [[0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]]]], shape=(2, 3, 4, 5), dtype=float32)
```

We have created our rank 4 tensor. Now let's get some information about the size, shape (number of values), and the dimension of the tensor. 

We will use tf.size function to get the size. The shape and ndim properties will give us the shape and dimensions of the tensor. 

```
print("Size",tf.size(rank4_tensor))
print("shape",rank4_tensor.shape)
print("Dimension",rank4_tensor.ndim)
```

```
OUTPUT: 

Size tf.Tensor(120, shape=(), dtype=int32)
shape (2, 3, 4, 5)
Dimension 4
```

Let’s look at some simple calculations using the tensor. I will create a new basic tensor.

```
basic_tensor = tf.constant([[10,11],[12,13]])
print(basic_tensor)
```

```
OUTPUT: 

tf.Tensor(
[[10 11]
 [12 13]], shape=(2, 2), dtype=int32)
```

Let’s try some simple operations. We can add, subtract, multiply, and divide every value in a tensor using the basic operators.

```
print(basic_tensor + 10)
print(basic_tensor - 10)
print(basic_tensor * 10)
print(basic_tensor / 10)
```

```
OUTPUT:
tf.Tensor(
[[20 21]
 [22 23]], shape=(2, 2), dtype=int32)
tf.Tensor(
[[0 1]
 [2 3]], shape=(2, 2), dtype=int32)
tf.Tensor(
[[100 110]
 [120 130]], shape=(2, 2), dtype=int32)
tf.Tensor(
[[1.  1.1]
 [1.2 1.3]], shape=(2, 2), dtype=float64)
```

Now let’s try matrix multiplication. I will create two simple tensors tensor_011 and tensor_012.

```
tensor_011 = tf.constant([[2,2],[4,4]])
tensor_012 = tf.constant([[2,3],[4,5]])
```

Keep in mind that in matrix multiplication, the inner dimensions should match. For example, a (3, 5) * (3, 5) multiplication won’t work but (3, 5) * (5, 3) will work.

The final shape of the resulting matrix will be its outer dimension. so, a 3x5 tensor multiplied by a 5x3 tensor will give us a 5x5 tensor. We will use the tf.matmul function to perform matrix multiplication.

```
print(tf.matmul(tensor_011,tensor_012))
```

```
OUTPUT:
tf.Tensor(
[[12 16]
 [24 32]], shape=(2, 2), dtype=int32)
```

Next, let’s look at reshaping and transposing a matrix. As we saw before, we will often use reshaping to change our matrix structure while training neural networks.

For example, an image pixel matrix of 28x28 will be converted into a 1-dimensional 784-pixel array for an image classification neural network.

To reshape, we use the tf.reshape function. To transpose, we use the tf.transpose function. If you don't know what a transpose is, it's converting rows into columns and columns into rows.

```
print(tf.reshape(tensor_011,[4,1]))
print(tf.transpose(tensor_011))
```

```
OUTPUT:
tf.Tensor(
[[2]
 [2]
 [4]
 [4]], shape=(4, 1), dtype=int32)
tf.Tensor(
[[2 4]
 [2 4]], shape=(2, 2), dtype=int32)
```

Finally, let’s look at some aggregate operations like min, max, standard deviation, square and square root.

To find the minimum and maximum values, we use the tf.reduce_min and tf.reduce_max functions. And to find the sum of the array, we use the tf.reduce_sum function.

```
tensor_013 = tf.constant([
    [1,2,3],
    [4,5,6],
    [7,8,9]
],dtype='float32')
print(tf.reduce_min(tensor_013))
print(tf.reduce_max(tensor_013))
print(tf.reduce_sum(tensor_013))
```

```
OUTPUT:
tf.Tensor(1.0, shape=(), dtype=float32)
tf.Tensor(9.0, shape=(), dtype=float32)
tf.Tensor(45.0, shape=(), dtype=float32)
```

Now for the standard deviation and variance, we use the tf.math.reduce_std function and tf.math.reduce_variance function.

```
print(tf.math.reduce_std(tensor_013))
print(tf.math.reduce_variance(tensor_013))
```

```
OUTPUT:
tf.Tensor(2.5819888, shape=(), dtype=float32)
tf.Tensor(6.6666665, shape=(), dtype=float32)
```

Let’s find the square, square root, and log of each value in a tensor.

```
print(tf.sqrt(tensor_013))
print(tf.square(tensor_013))
print(tf.math.log(tensor_013))
```

```
OUTPUT:
tf.Tensor(
[[1.        1.4142135 1.7320508]
 [2.        2.236068  2.4494898]
 [2.6457512 2.828427  3.       ]], shape=(3, 3), dtype=float32)
tf.Tensor(
[[ 1.  4.  9.]
 [16. 25. 36.]
 [49. 64. 81.]], shape=(3, 3), dtype=float32)
tf.Tensor(
[[0.        0.6931472 1.0986123]
 [1.3862944 1.609438  1.7917595]
 [1.9459102 2.0794415 2.1972246]], shape=(3, 3), dtype=float32)
```

We have learned the basics of TensorFlow in this article. You are now equipped to work with TensorFlow and use it to model data.

If you want to start using this knowledge and build a project, you can check out my course on [building a handwriting recognition neural network using TensorFlow](https://learn.manishmshiva.com/tensorflow-basics-handwriting-recognition-using-computer-vision). You can also learn advanced TensorFlow concepts using the [official documentation.](https://www.tensorflow.org/overview)

## Conclusion

Tensorflow is a powerful library to build deep-learning models. It has all the tools we need to construct neural networks to solve problems like image classification, sentiment analysis, stock market predictions, etc. 

With the advent of technologies like ChatGPT, learning TensorFlow will give you a head start in the current job market.

_Hope you liked this article. You can learn more about me and my articles/videos at_ [_manishmshiva.com_](https://www.manishmshiva.com/)_._

