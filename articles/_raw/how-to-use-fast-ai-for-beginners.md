---
title: How to Use Fast.ai – A Beginner-Friendly Gateway to Deep Learning
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2024-02-02T00:10:29.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-fast-ai-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/Untitled-design.png
tags:
- name: Deep Learning
  slug: deep-learning
- name: 'fastai, '
  slug: fastai
seo_title: null
seo_desc: 'Fast.ai is a user-friendly library that brings the power of deep learning
  to your fingertips, regardless of your skill level. Let’s learn how it works.

  Have you ever felt curious about deep learning but found the technical complexity
  overwhelming? Fa...'
---

Fast.ai is a user-friendly library that brings the power of deep learning to your fingertips, regardless of your skill level. Let’s learn how it works.

Have you ever felt curious about deep learning but found the technical complexity overwhelming? [Fast.ai](https://fast.ai/) is your answer.

Fast.ai simplifies the journey into deep learning. It makes deep learning accessible to you even if you’re not a seasoned data scientist.

In this article, we’ll explore what Fast.ai is, why it stands out, and how you can get started with some basic code examples.

## What is Fast.ai?

Fast.ai is a library built on top of PyTorch, one of the leading deep-learning frameworks.

It’s designed to make deep learning more approachable. The library provides high-level components that make it easy to build and train neural networks.

What sets Fast.ai apart is its focus on practicality and its ability to be used by people with varying levels of coding experience.

## Why Choose Fast.ai?

### User-Friendly

The Fast.ai library simplifies the deep learning process and abstracts away many of the complex details, making it easier for users to create powerful models.

The **f**[**astai**](https://docs.fast.ai/) library sits on top of popular deep-learning frameworks like PyTorch. It provides a high-level API for building and training neural networks.

You can also integrate other powerful models like [Hugging Face transformers](https://www.freecodecamp.org/news/hugging-face-transformer-library-overview/) using Fast.ai.

### Practical Approach

Fast.ai emphasizes a practical and hands-on approach to deep learning.

The Fast.ai library focuses on practical usage and real-world applications, helping you learn by doing.

Their courses and resources are designed to help students quickly get up and running with machine learning models. These include building and training neural networks for image recognition, natural language processing, and many others.

### Free Courses

Fast.ai offers [free online courses](https://course.fast.ai/) that cover a wide range of deep learning topics. Fast.ai courses are a few of the best in the market and their students have gone on to become popular machine learning researchers.

These courses are known for their practicality, clear explanations, and use of real-world datasets. These courses are designed to be accessible to individuals with varying levels of prior AI knowledge.

Fast.ai also incorporates the latest developments into its courses and resources, ensuring that students have access to state-of-the-art techniques.

## How to Get Started with Fast.ai

Now that you understand what Fast.ai is, let's write some code. You can check out [the google colab notebook](https://colab.research.google.com/) if you want to quickly try this example.

**Note:** It is recomended that you run this code on your system since running it in colab will take a long time (30 mins approx).

Before using the library, you have to set up your environment. Fast.ai runs on Python and requires PyTorch.

You can install Fast.ai using the pip command (remove the **`!`** if you are installing it on your terminal, as the **`!`** is only for colab notebooks. Notebooks treat the code following **`!`** as shell scripts).

```
!pip install fastai
```

We’ll go through a simple sentiment analysis example in this article, demonstrating how you can implement NLP models using the fast.ai library.

Let’s start with importing the library:

```
from fastai.text.all import *
```

This line of code imports specific functionality from the Fast.ai library for natural language processing (NLP), particularly text analysis.

Let me break it down for you:

`from fastai.text.all` specifies that you want to import all components from the `fastai.text` module which contains tools and functions for working with text data.

By including this line at the beginning of your code, you make all the text-related functionality from the Fastai library available for your use, making it easier to perform tasks like sentiment analysis, text classification, and others.

Next, we’ll use the IMDB dataset, also available in Fast.ai.

```
path = untar_data(URLs.IMDB)
```

This line of code downloads and extracts the IMDB dataset, making it ready for further processing and analysis.

The variable `path` will contain the local file path to the dataset, allowing you to access and work with the data in your code.

Next, we have to load the data. [Data loaders](https://pytorch.org/tutorials/beginner/basics/data_tutorial.html) are used to efficiently load and process data during the training of a machine learning model.

`TextDataLoaders` is a class provided by the Fast.ai library that allows you to create data loaders specifically designed for text data.

```
dls = TextDataLoaders.from_folder(path, valid='test')
```

`from_folder(path, valid='test')` is a function call on the `TextDataLoaders` class. It is used to create the data loaders.

Here's what each argument means:

* `path`: This is the directory path where your text data is stored. In this case, it's the `path` variable that you previously defined, which contains the local path to the IMDB dataset.
* `valid='test'`: This argument specifies which folder or subset of your data should be used for validation. In the IMDB dataset, there are typically two main subsets: `train` for training data and `test` for testing or validation data. By setting `valid` to `test`, you're indicating that the 'test' folder within the `path` directory should be used for validation. This is a common practice in machine learning to have a separate validation set to evaluate the model's performance during training.
* The resulting `dls` variable will contain the text data loaders, which include both training and validation data splits. These data loaders can be used to load and preprocess text data batches during the training of your sentiment analysis model or any other text-based model.

Now that we have the data for training, let’s train the model.

We will create a text classification model using the Fast.ai library, fine-tune it on the provided text data, and train it for a specified number of epochs (repetitions).

```
learn = text_classifier_learner(dls, AWD_LSTM, drop_mult=0.5, metrics=accuracy)
```

Let’s break down each line:

* `text_classifier_learner` — The text classification learner is used to create a learner object for training and working with text classification models. Let’s look at the arguments.
* `dls` — This is the data loader object you previously created using `TextDataLoaders.from_folder()`. It contains the training and validation data for your text classification task.
* `AWD_LSTM` — This is a pre-defined architecture for the neural network used in text classification tasks. AWD_LSTM stands for [ASGD Weight-Dropped LSTM](https://arxiv.org/pdf/1708.02182v1.pdf). It is a type of [recurrent neural network](https://aws.amazon.com/what-is/recurrent-neural-network/) (RNN) architecture that is effective for sequential data like text.
* `drop_mult=0.5` — This argument controls the amount of dropout regularization applied to the neural network. Dropout is a regularization technique used to prevent overfitting (training the model too much). `drop_mult=0.5`means that dropout will be applied at a moderate rate.
* `metrics=accuracy` — This specifies that the accuracy metric should be used to evaluate the model’s performance during training. Accuracy is a common metric for classification tasks, measuring the percentage of correctly classified examples.

Now let's fine-tune the model using the loaded data.

```
learn.fine_tune(1)
```

* `learn.fine_tune(1)` — This line of code fine-tunes the text classification model. 
* `1` — The parameter `1` is the number of epochs for which the model will be trained. An epoch is one pass through the entire training dataset. Training for multiple epochs allows the model to learn from the data multiple times, here for simplicity’s sake we use 1.

In summary, these lines of code create a text classification model, load your text data, fine-tune the model on the data for four epochs using a specified learning rate, and use accuracy as the metric to evaluate the model’s performance.

The resulting `learn` object represents your trained text classification model, which can be used to make predictions on new text data.

We are done. Now our model is ready to start predicting the sentiments of the text.

Let’s test the model with a movie review.

```
learn.predict("I really loved that movie, it was awesome!")
```

And here is the result.

```
('pos', tensor(1), tensor([0.4885, 0.5115]))
```

The `pos`says the given sentence is a positive sentence. The next array says how confident the model is in predicting whether the given sentence is positive or negative. This confidence score can be improved by increasing the number of epochs (which will take a long time to train, unless you have a powerful computer).

Hope this helps you to understand how to work with the Fast.ai library. I personally prefer to use [Huggingface](https://huggingface.co/) for most use cases, but if I have to train models from scratch, Fast.ai would be my first choice.

## Conclusion

Fast.ai offers a fantastic starting point for anyone interested in deep learning. Its simplicity and practicality make it a valuable tool for both beginners and experienced practitioners.

Using Fast.ai, you’ll discover that deep learning is not as daunting as it seems. Whether you’re a student, a developer, or a curious learner, Fast.ai can be your gateway to the fascinating world of artificial intelligence. So, get started, experiment, and enjoy the journey into deep learning with Fast.ai.

If you are a student of AI, subscribe to **[turingtalks.ai](https://www.turingtalks.ai/)** to learn practical concepts on general machine learning and NLP. You can also [**visit my website**](https://manishmshiva.com/) to get in touch with me.

