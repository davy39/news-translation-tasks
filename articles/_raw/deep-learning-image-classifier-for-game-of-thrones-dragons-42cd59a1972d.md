---
title: 'Day 24: How to build a Deep Learning Image Classifier for Game of Thrones
  dragons'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-21T20:27:02.000Z'
originalURL: https://freecodecamp.org/news/deep-learning-image-classifier-for-game-of-thrones-dragons-42cd59a1972d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*TM3_JUHkkaTW36uQZp9FYw.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Deep Learning
  slug: deep-learning
- name: image classification
  slug: image-classification
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
seo_title: null
seo_desc: 'By Harini Janakiraman


  Performance of most flavors of the old generations of learning algorithms will plateau.
  Deep learning, training large neural networks, is scalable and performance keeps
  getting better as you feed them more data. — Andrew Ng


  De...'
---

By Harini Janakiraman

> Performance of most flavors of the old generations of learning algorithms will plateau. Deep learning, training large neural networks, is scalable and performance keeps getting better as you feed them more data. — _Andrew Ng_

Deep learning doesn’t take a huge amount of time or computational resources. Nor does it require highly complex code, and in some cases not even a large amount of training data. Curated best practices are now available as libraries that make it easy to plug in and write your own neural network architectures using a minimal amount of code to achieve more than 90% prediction accuracies.

The two most popular deep learning libraries are: (1) pytorch created by Facebook (we will be using fastai today, which is built on top of pytorch) and (2) the keras-tensorflow framework created by Google.

### The Project

We will build an image classifier using the Convolutional Neural Network (CNN) model to predict if a given image is that of Drogon or Vicerion (any Game of Thrones fans here in the house? Clap to say yay!).

You can adapt this problem statement to any type of image classification that interests you. Here are some ideas: cat or dog (classic deep learning 101), if a person is wearing glasses or not, bus or car, hot dog vs not-hot dog (Silicon Valley fans also say yay! ;) ).

### Step 1: Installation

You can use any GPU accelerated cloud computing platform for running your model on. For the purpose of this blog we will be using [Paperspace](https://www.paperspace.com/) (most affordable). Complete instructions on how to get this up and running are available [**here**](https://github.com/reshamas/fastai_deeplearn_part1/blob/master/tools/paperspace.md).

Once setup, you can launch Jupyter notebook on that machine using the following command:

```
jupyter notebook
```

This will give you a localhost URL that you can open in your browser and replace “localhost” with your machine’s IP address to launch your notebook.

![Image](https://cdn-media-1.freecodecamp.org/images/gtn9GKmqFmghPbs7fLu6SzJ1hSid9GNpKNvV)

Now you can copy over the iPython notebook and dataset files into the directory structure below from [**my github repo**](https://github.com/harinij/100DaysOfCode/tree/master/Day%20023%20-%20Image%20Classifier%20using%20deep%20learning%20CNN%20model).

![Image](https://cdn-media-1.freecodecamp.org/images/3cvYJGymYABQJWr4bP6G29kZDkQSJUUFBGhp)

**Note**: Do not forget to shut down the machine from the paperspace console once you are done to avoid getting accidentally charged.

### **Step 2: Training**

Follow the instructions in the notebook to initialize the libraries needed for this exercise, and point to the location of the PATH to your data directory. Note that each block of code can be run using “shift+enter.” In case you need additional info on Jupyter notebook commands, you can read more [here](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Notebook%20Basics.html).

Now, coming to the part of training the image classifier, the following three lines of code form the core of building the deep learning model:

1. **data**: represents the validation and training datasets.
2. **learn**: contains the model
3. **learn.fit(learning_rate,epoch)**: Fit the model using two parameters — learning rate and epochs.

![Image](https://cdn-media-1.freecodecamp.org/images/GSWXa64C56P8YNg4WPrlSvlAjdiTTq0abWP0)

We have set the learning rate to be “0.01” here. Learning rate needs to be a small enough number so that you move through the image in incremental steps of this factor to learn with accuracy. But it shouldn’t be too small, either, as that would result in too many steps/too long to learn. The library has a learning rate finder method “lr_find()” to find the optimal one.

Epoch is set to “3” in the code here and it represents how many times you should run the batch. We can run as many times as we want, but after a point accuracy will start to get worse due to overfitting.

![Image](https://cdn-media-1.freecodecamp.org/images/sas5SvMYXGfSQyeiKB96YURdhkad6r7BrtH2)

### **Step 3: Prediction**

We will now run prediction on the validation data using the trained model.

![Image](https://cdn-media-1.freecodecamp.org/images/oTZaAYbeABWT0tGnDEtEP7elcN5nb7lNB9Gp)

Pytorch gives a log of prediction, so to get the probability you have to get e to the power of using numpy. Follow the instructions step by step on the notebook in my [**github repo**](https://github.com/harinij/100DaysOfCode/tree/master/Day%20023%20-%20Image%20Classifier%20using%20deep%20learning%20CNN%20model)**.** A probability close to 0 implies its an image of Drogon and a probability close to 1 implies its an image of Viserion.

### **Step 4: Visualize**

Plotting function can be used to visualize the results of the prediction better. The below images show you correctly classified validation data with 0.2–0.3 indicating it’s Drogon and a probablity of 0.7–0.8 indicating it’s Viserion.

![Image](https://cdn-media-1.freecodecamp.org/images/zf74Dk3FGDS3F3sd5WiGDpH-4vshGm3O-i1Z)

![Image](https://cdn-media-1.freecodecamp.org/images/3i82iaVHQHUPrEtOMufWCPPAuRu3iqeAhlE8)

![Image](https://cdn-media-1.freecodecamp.org/images/oQw5JxD8sAhzcnxAiwklzpUy2c4ph8UnbCSZ)

You can also see some of the uncertain predictions if they linger closer to 0.5 probability.

![Image](https://cdn-media-1.freecodecamp.org/images/USlRGvhRFoBP-JmY719kyZaKr-geDY4cldoS)

The image classifier in some scenarios can have uncertain predictions, for example in case of long tailed images, as it grabs a small piece of the square at a time.

In those cases, enhancement techniques can be done to have better results such as data augmentation, optimizing the learning rate, using differential learning rates for different layers, and test-time augmentation. These advanced concepts will be explored in future posts.

This blog was inspired by fastai CNN video. To get an in-depth understanding and continue your quest in Deep Learning, you can take the famous set of courses by Andrew Ng on [coursera](https://www.deeplearning.ai/).

_If you enjoyed this, please clap **? s**o others can see it as well! Follow me on Twitter @[H**ariniLabs**](https://twitter.com/harinilabs) or M[**edium**](https://medium.com/@harinilabs) to get new post updates or to just say Hi :)_

_PS: Sign up for my newsletter [**here**](http://harinilabs.com/womenintech.html) to be the first to get fresh new content and it’s filled with doses of inspiration from the world of #[**WomenInTech**](http://harinilabs.com/womenintech.html) **—** and yes men can signup too :)_

