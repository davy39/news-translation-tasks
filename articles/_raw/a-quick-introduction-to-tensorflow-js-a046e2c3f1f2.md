---
title: A quick introduction to TensorFlow.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-24T18:22:49.000Z'
originalURL: https://freecodecamp.org/news/a-quick-introduction-to-tensorflow-js-a046e2c3f1f2
coverImage: https://cdn-media-1.freecodecamp.org/images/0*TqGRmDuim8mReF9m.
tags:
- name: JavaScript
  slug: javascript
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: TensorFlow
  slug: tensorflow
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Pau Pavón

  TensorFlow has been around for a while now. Until last month, though, it was only
  available for Python and a few other programming languages, like C and Java. And
  you might think those would be more than enough.

  I had heard of TensorFlow...'
---

By Pau Pavón

TensorFlow has been around for a while now. Until last month, though, it was only available for Python and a few other programming languages, like C and Java. And you might think those would be more than enough.

I had heard of TensorFlow in the past. Even though I didn’t know anything about machine or deep learning, I was pretty sure it was one of the most used frameworks for those purposes. I had seen lots of cool things done with it: object detection in images, speech recognition, and even music composition!

Imagine being able to do all these cool ML things in the browser, without installing any libraries and having to compile all those lines of code again and again. Well, that’s what TensorFlow.js has come to do.

If you want to learn more about how and why this amazing framework has come to life, you can check out [TensorFlow](https://www.freecodecamp.org/news/a-quick-introduction-to-tensorflow-js-a046e2c3f1f2/undefined) here on Medium!

So as soon as I discovered this, I wanted to start learning how TensorFlow.js works. And that’s exactly what I’ve started to do: I’ve found [a set of tutorials by The Coding Train on Youtube](https://www.youtube.com/playlist?list=PLRqwX-V7Uu6YIeVA3dNxbR9PYj4wV31oQ), which are still ongoing (in fact, they’ve just started) and I’ve began to mess around a bit with things.

I’d like to give you a quick introduction to TensorFlow (TF) so you can follow me along my journey and learn with me.

### The basics of TensorFlow.js

Let’s get started! First of all, you should know that all the documentation is on [TF’s website](https://js.tensorflow.org/), under the API Reference section.

> But wait, why is it called TensorFlow? What even is a tensor?

Glad you asked. A tensor is basically a structure of numbers. In math, there are different ways of representing numbers. You can have just the number itself, a vector, a matrix, and so on. A tensor is just a general term for all these different representations of data.

In TF, tensors are differentiated because of their **rank**, or, in other words, the number of **dimensions** they have.

These are the most common ones:

#### Scalar (rank-0)

Just a number. This is how you can create and console-log one:

```
tf.scalar(4.5).print();
```

And the output is the following:

```
Tensor  4.5
```

#### Tensor1d, tensor2d, tensor3d and tensor4d (rank- 1, 2, 3 and 4 respectively)

These are higher dimensional tensors. If you wanted to create a rank-1 tensor, for instance, you could simply do:

```
tf.tensor1d([3, 7, 8]).print();
```

Which would output:

```
Tensor  [3, 7, 8]
```

#### Tensor (rank-n)

If you don’t know the dimensions of your tensor, you can simply create one with the following function (notice how the above two examples work just as well with this other method):

```
tf.tensor(4.5).print();tf.tensor([3, 7, 8]).print();
```

This outputs exactly the same as before.

You can, additionally, pass a couple more parameters to these functions.

#### tf.tensor(values, shape?, dtype?)

Let’s look at **values** first. This is the only compulsory parameter, and the only one we’ve been passing on in the previous examples. You can either pass a flat array of values (or even a single number in scalars) and specify the shape yourself, or you can pass a nested array.

Now you might be wondering what **shape** is. So, let’s say you want to output the following tensor:

```
[[1, 5], [4, 7]]
```

That is, you guessed right, a 2x2 matrix. You can either create this tensor by passing a flat array and specifying the shape as the second parameter of the function

```
tf.tensor([1, 5, 4, 7], [2, 2]).print();
```

or by passing a nested array

```
tf.tensor([[1, 5], [4, 7]]).print();
```

Lastly, we have **dtype**. This specifies the data type. As for now, **int32, float32** and **bool** are the three supported types.

#### Operations

But, what can you do with these tensors? Well, among other things, you can perform mathematical computation on them, such as arithmetic operations:

**Note**: the following operations are performed element-wise, which means that every term of the first tensor involved is associated with the term in its same place in the other tensor.

```
const a = tf.tensor1d([4, 7, 2, 1]);const b = tf.tensor1d([20, 30, 40, 50]);
```

There are two ways these two can be added:

```
a.add(b).print();
```

or,

```
tf.add(a, b);
```

Both output:

```
Tensor  [24, 37, 42, 51]
```

Here’s how they work for subtraction,

```
tf.sub(a, b).print();
```

```
Tensor //output  [-16, -23, -38, -49]
```

multiplication,

```
tf.mul(a, b).print();
```

```
Tensor //output  [80, 210, 80, 50]
```

and division:

```
tf.div(a, b).print();
```

```
Tensor //output  [0.2, 0.2333333, 0.05, 0.02]
```

It’s pretty simple and straightforward.

### Try it yourself!

If you haven’t already, I encourage you to try the above yourself. This is the most basic stuff in TF, but these concepts are key in order to understand the more complex (and more fun) parts of it.

Thanks for reading!

Edit: Check out [ADL](https://www.freecodecamp.org/news/a-quick-introduction-to-tensorflow-js-a046e2c3f1f2/undefined)’s [Youtube playlist](https://www.youtube.com/playlist?list=PL1jmMFbLDfgX0Q-rBbfoBdNFl8MS3kTh9) on TensorFlow, I’m sure it’ll help you out!

