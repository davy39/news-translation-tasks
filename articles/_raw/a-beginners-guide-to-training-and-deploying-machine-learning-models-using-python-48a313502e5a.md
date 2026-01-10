---
title: A beginner’s guide to training and deploying machine learning models using
  Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-27T16:33:23.000Z'
originalURL: https://freecodecamp.org/news/a-beginners-guide-to-training-and-deploying-machine-learning-models-using-python-48a313502e5a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*-W-ioBNBUF5eSDYWc-ZHxQ.png
tags:
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: scikit learn
  slug: scikit-learn
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Ivan Yung

  When I was first introduced to machine learning, I had no idea what I was reading.
  All the articles I read consisted of weird jargon and crazy equations. How could
  I figure all this out?

  I opened a new tab in Chrome and looked for easier...'
---

By Ivan Yung

When I was first introduced to machine learning, I had no idea what I was reading. All the articles I read consisted of weird jargon and crazy equations. How could I figure all this out?

I opened a new tab in Chrome and looked for easier solutions. I found APIs from Amazon, Microsoft, and Google that did all the machine learning for me. Each hackathon project I made would call their servers and WOW — it looked so smart! I was hooked.

But, after a year, I realized that I wasn’t learning anything. Everything I was doing was described by this Nedroid comic that I modified:

![Image](https://cdn-media-1.freecodecamp.org/images/1*1YwLOx3wkKoLjRUD-NoiZA.png)
_[Original image source](https://nedroidcomics.tumblr.com/post/41879001445/the-internet" rel="noopener" target="_blank" title=")._

Eventually, I sat down and learned how to use machine learning without megacorporations. And turns out, anyone can do it. The current libraries we have in Python are amazing. In this article, I will explain how I use these libraries to create a proper machine learning back end.

### Getting a dataset

Machine learning projects are reliant on finding good datasets. If the dataset is bad, or too small, we cannot make accurate predictions. You can find some good datasets at [Kaggle](http://kaggle.com) or the [UC Irvine Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php).

In this article, I am using a [wine quality dataset](https://archive.ics.uci.edu/ml/datasets/Wine+Quality) with many features and one label. **Features** are independent variables which affect the dependent variable called the **label**. In this case, we have one **label** column — wine quality — that is affected by all the other columns (features like pH, density, acidity, and so on).

In the following Python code, I use a library called [pandas](https://pandas.pydata.org/) to control my dataset. pandas provides datasets with many functions to select and manipulate data.

First, I load the dataset to a panda and split it into the label and its features. I then grab the label column by its name (quality) and then drop the column to get all the features.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Kybbe-8PK1jHttWyP0adow.png)
_Scikits-learn, the library we will use for machine learning_

### Training a model

Machine learning works by finding a relationship between a label and its features. We do this by showing an object (our model) a bunch of examples from our dataset. Each example helps define how each feature affects the label. We refer to this process as **training our model**.

I use the estimator object from the [Scikit-learn](http://scikit-learn.org/stable/index.html) library for simple machine learning. **Estimators** are empty models that create relationships through a predefined algorithm.

For this wine dataset, I create a model from a linear regression estimator. (Linear regression attempts to draw a straight line of best fit through our dataset.) The model is able to get the regression data through the fit function. I can use the model by passing in a fake set of features through the predict function. The example below shows the features for one fake wine. The model will output an answer based on its training.

The code for this model, and fake wine, is below:

### Importing and exporting our Python model

The [pickle](https://docs.python.org/2/library/pickle.html) library makes it easy to serialize the models into files that I create. I am also able to load the model back into my code. This allows me to keep my model training code separated from the code that deploys my model.

I can import or export my Python model for use in other Python scripts with the code below:

### Creating a simple web server

![Image](https://cdn-media-1.freecodecamp.org/images/1*wv3umUu_u8r7dgeXHX38uw.png)
_Flask, the framework we will use to create a web server._

To deploy my model, I first have to create a server. Servers listen to web traffic, and run functions when they find a request addressed to them. The function that runs can depend on the request’s route and other data that it has. Afterwards, the server can send a message of confirmation back to the requester.

The [Flask](http://flask.pocoo.org/) Python framework allows me to create web servers in record time.

In the code below, I use Flask to run a simple one-route web server. My one route listens to POST requests and sends a hello back. POST requests are a special type of request that carry data in a JSON object.

### Adding the model to my server

With the pickle library, I am able to able to load our trained model into my web server.

Our server now loads the trained model during its initialization. I can access it by sending a post request to my “/echo” route. The route grabs an array of features from the request body and gives it to the model. The model’s prediction is then sent back to the requester.

### Conclusion

After reading this article, you should be able to create your own machine learning back end. For more detail, you can find a full example that I made at [this](https://github.com/iYung/sklearn-flask-example) repository.

When you have time, I recommend taking a step back from coding and reading about machine learning. This article only teaches the bare necessities to create a model. There are topics like loss reduction and neural nets that you need to know.

Good luck and happy coding!

