---
title: How to Add Two Numbers – The Machine Learning Way
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2023-08-01T19:51:50.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-two-numbers-using-machine-learning
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/Sum-of-2-numbers-using-ML---Banner.png
tags:
- name: Deep Learning
  slug: deep-learning
- name: Machine Learning
  slug: machine-learning
seo_title: null
seo_desc: "In the world of machine learning, we often encounter complex problems,\
  \ from image recognition to natural language processing. \nBut let's take a step\
  \ back and explore something more elementary yet equally intriguing: addition! Yes,\
  \ you read that right..."
---

In the world of machine learning, we often encounter complex problems, from image recognition to natural language processing. 

But let's take a step back and explore something more elementary yet equally intriguing: addition! Yes, you read that right – addition. 

In this tutorial, we'll build a neural network that can learn the art of adding two numbers together.

A quick note before we get into this: I don't recommend using machine learning to find the sum of two numbers in practice. I tried this out of curiosity when I started learning machine learning. And I just wished to share this with you all to make learning fun. 

You can use this tutorial as a sort of starter guide in your machine learning journey. Sometimes its hard to find good, clean datasets as a beginner machine learning engineer. This makes it harder to work on and learn about machine learning problems if you don't have a solid dataset.

But don't worry – in this tutorial, we'll be creating our own dataset (pairs of numbers to add) and cleaning the data. So it'll give you a good dataset you can use in your own problems and with your own models. 

Alright, before diving in, let's brush up on some machine learning and deep learning basics.

## Deep Learning Basics

There are a few machine and deep learning terms which I'll be using in the exercise. So, it's better to understand them on a high level in a couple of sentences before diving in.

### What is a Neural Network?

A neural network is a computational model inspired by the structure and functions of the human brain. It consists of interconnected nodes (neurons) organized in layers. Neural networks are trained on data to learn patterns and make predictions.

### What is an Activation Function?

An activation function is applied to the output of a neuron to introduce non-linearity. It allows neural networks to learn complex relationships in data. Common activation functions include ReLU (Rectified Linear Unit) and Sigmoid.

### What is a Loss Function?

A loss function is a measure of how well a model's predictions match the true target values. During training, the goal is to minimize the loss function, guiding the model to make better predictions.

### What is Gradient Descent?

Gradient descent is an optimization algorithm used to minimize the loss function. It adjusts the model's parameters iteratively in the direction of steepest descent, guided by the gradients of the loss function with respect to the parameters.

### What is Backpropagation?

Backpropagation is a fundamental algorithm used in training neural networks. It calculates the gradients of the loss function with respect to each model parameter and propagates them backward through the network to update the weights during gradient descent.

### What is Batch Size?

Batch size represents the number of training samples used in one forward/backward pass during training. Larger batch sizes can speed up training but require more memory.

### What is an Epoch?

An epoch represents one complete iteration through the entire training dataset during training.

These are just a few of the many terms you'll encounter in the vast field of machine and deep learning. But they're enough to help you understand the following exercise.

## Prerequisites

Here's a checklist to help you get started with machine learning basics. Before going through this tutorial, you should have them installed and ready (but it's not mandatory).

1. Install Anaconda (it's packaged with many default machine learning libraries). 
2. Create an environment in Anaconda: This is highly recommended, because only the created environment will be affected if something goes wrong. Your entire Anaconda installation will not be affected.
3. Make sure you have a good code editor/IDE like Visual Studio Code.
4. Install Keras (this requirement is specific to this exercise).

Do you have all these items ready? Hope you're excited. Let's jump into our exercise.

## How to Sum Two Numbers using Machine Learning

### Create a folder and a file

Create a new folder with any name. Navigate into the folder and create a file named `addition.ipynb`. Open the folder in Visual Studio Code or whatever IDE you're using.

Next, create code blocks for each of the following sections by pressing the "+ Code" button at the top left in VS Code.

### Import libraries

Import the `numpy` and `keras` libraries with these commands:

```py
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
```

### Prepare the data

The accuracy of your machine learning models depends on the data with which you train your model. 

To create the addition data we'll need here, let's create pairs of 1000 random numbers which will be considered our input. The output will be the sum of the numbers in each pair.

```py
num_samples = 1000
X_train = np.random.rand(num_samples, 2)
y_train = X_train[:, 0] + X_train[:, 1]
```

### Define the neural network

Let's build a neural network with two input layers – one hidden layer with 8 neurons, and an output layer with a single neuron. We'll use the "relu" activation function.

```py
model = Sequential()
model.add(Dense(8, input_shape=(2,), activation='relu'))
model.add(Dense(1))
```

### Compile the model

Compile the model using the MSE (Mean Squared Error) as the loss function and Adam optimizer.

```py
model.compile(loss='mse', optimizer='adam')
```

### Train the model

Train the model for 100 epochs, with a batch size of 32.

```py
batch_size = 32
epochs = 100
model.fit(X_train, y_train, batch_size=batch_size, epochs=epochs, verbose=1)
```

This may take few seconds depending on your CPU configuration. It consumed around 10 to 15 seconds in my laptop to complete.

### Test the model

Now that we have trained our model, let's test it with a few custom inputs. I have taken two inputs but you can test your model with any number of inputs.

```python
test_input = np.array([[1, 2], [0.3, 0.4]])
predicted_sum = model.predict(test_input)
```

### Print the values

The prediction is complete. Let's see if they're right by printing the predicted values:

```python
print("Predicted sums:")
print(predicted_sum)
```

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-187.png)
_Sample output of predicted values_

Pretty close, right?

## Conclusion

In this tutorial, you learned how to build a neural network to perform addition.

If you're curious, though, you can try building a neural network to perform subtraction just for fun. Good luck :)

Hope you enjoyed reading this article. If you wish to learn more about artificial intelligence / machine learning / deep learning, subscribe to my article by visiting my [site](https://5minslearn.gogosoon.com/?ref=fcc_addition_nn) which has a consolidated list of all my blogs. 


