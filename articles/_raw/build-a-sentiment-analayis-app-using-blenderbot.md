---
title: How to Build a Sentiment Analysis App using Blenderbot
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-01-31T15:07:33.000Z'
originalURL: https://freecodecamp.org/news/build-a-sentiment-analayis-app-using-blenderbot
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/cover.jpg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Machine Learning
  slug: machine-learning
- name: Sentiment analysis
  slug: sentiment-analysis
seo_title: null
seo_desc: 'By Edem Gold

  Turning machine learning models into actual applications other people can use is
  not something that is covered in most AI and Machine Learning Tutorials.

  In this article, we are going to create an end-to-end AI Sentiment Analysis web
  app...'
---

By Edem Gold

Turning machine learning models into actual applications other people can use is not something that is covered in most AI and Machine Learning Tutorials.

In this article, we are going to create an end-to-end AI Sentiment Analysis web application using Gradio and Hugging face transformers.

# What is Sentiment Analysis?

![pic-1.jpg](https://cdn.hashnode.com/res/hashnode/image/upload/v1635883449621/fWPS8d_c-.jpeg?auto=compress,format&format=webp)

According to [Wikipedia](https://en.wikipedia.org/wiki/Sentiment_analysis), 

> Sentiment analysis is the use of natural language processing, text analysis, computational linguistics, and biometrics to systematically identify, extract, quantify, and study affective states and subjective information.

In simple words, Sentiment Analysis is the ability of Artificial Intelligence to analyze a sentence or block of text and get the emotions behind that sentence or block of text.

# What is Gradio?

![gradio-logo.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1635883565410/Oo46t3DPn.png?auto=compress,format&format=webp)

[Gradio is an open-source Python library](https://gradio.app/) that you can use to quickly create and customize easy-to-use UI components for your ML model, any API, or any arbitrary function in just a few lines of code.

Gradio makes it very easy for you to build Graphical User Interfaces and deploy machine learning models.

# What is Hugging Face?

[Hugging Face](https://huggingface.co/) is a library that provides pre-trained and open-sourced Natural Language Processing models and datasets for machine learning engineers.

It is an open-source Machine Learning community where you can download pre-trained machine learning models and use them in your own projects.

# Time to Build our Project

## **Prerequisites**

* Have Python installed
* Have an IDE / text editor (like [Visual Studio](https://code.visualstudio.com/), [PyCharm](https://www.jetbrains.com/pycharm/), or [Jupyter Notebook](https://jupyter.org/) )
* Have an internet connection

**Here is the [GitHub Repository](https://github.com/EdemGold/sentiment-analysis-app) for the project**.

## **Install Dependencies**

Here we are going to install the libraries needed to build the Sentiment Analysis app.

### How to install Transformers

Here we are going to install the transformers library. This library will give us access to the hugging face API.

```
#In a jupyter notebook
!pip install transformers

#In terminal
pip install transformers

```

### How to install PyTorch

We are going to install the PyTorch deep learning library. Visit the [PyTorch Website](https://pytorch.org/get-started/locally/) and install your specialized version.

![pytorch-install.jpg](https://cdn.hashnode.com/res/hashnode/image/upload/v1635887110857/e_LVM9OR0.jpeg?auto=compress,format&format=webp)

Below is my installed version of PyTorch.

```
#install in jupyter notebook
!pip3 install torch==1.9.1+cu111 torchvision==0.10.1+cu111 torchaudio===0.9.1 -f https://download.pytorch.org/whl/torch_stable.html

#Install in Terminal
pip3 install torch==1.9.1+cu111 torchvision==0.10.1+cu111 torchaudio===0.9.1 -f https://download.pytorch.org/whl/torch_stable.html

```

### Import and Set up Pipeline

Here we are going to import and set up our _sentiment analysis model_ using a Hugging Face pipeline.

Hugging Face provides an automatic pipeline that helps handle things like tokenizing, pre-processing, encoding, and decoding for you and lets you focus on core things like model optimization.

```
#setting up hugging face pipeline
from transformers import pipeline
classifier = pipeline("sentiment-analysis")

```

Above we imported and instantiated the pipeline object, and then we passed the sentiment-analysis models an argument.

### How to Define the Gradio Function

We are going to define a Gadio function that will help us provide the sentiment analysis functionality for our web app.

If you read my [past article](https://www.freecodecamp.org/news/build-gui-using-gradio-for-machine-learning-models/) on building graphical user interfaces (GUI) for machine learning models using Gradio, you'll know that Gradio allows you to build graphical components for your models and they provide the model's prediction functionality through functions.

```
#model function for gradio

def func(utterance):
  return classifier(utterance)

```

Above we created a function called `func` and added utterance (that is, the word to be analyzed by the model for sentiments) as an argument for our function. We then make our function return the sentiment analysis of the utterance earlier passed and this takes us to the next step.

### How to Build our Gradio Interface

Here we are going to create our Gradio web app, add graphical components to it, then we are going to launch the app.

```
#getting gradio library
import gradio as gr
descriptions = "This is an AI sentiment analyzer which checks and gets the emotions in a particular utterance. Just put in a sentence and you'll get the probable emotions behind that sentence"

app = gr.Interface(fn=func, inputs="text", outputs="text", title="Sentiment Analayser", description=descriptions)
app.launch()

```

Above we imported the Gradio library, and then we added a description of our project which will be then passed on to our web app.

We then created a Gradio interface instance where we are going to provide details about our web app. We passed the model's function into the `fn` parameter, we then provided the type of input.

Gradio allows you to create any form of input of your choice be it text, radios, checkboxes, numbers, and so on. But here we are going to use our input as text.

Next, we provided the output format, the same way Gradio allows you to pick your input format (that is text, numbers, checkbox, and so on). It also allows you to pick your output format. 

In this case, we are going to use text, too. After passing the output parameter we gave a title to our web app.

Lastly, we launch the app.

![Screenshot (36).png](https://cdn.hashnode.com/res/hashnode/image/upload/v1635983823728/v1LcvOBg6.png?auto=compress,format&format=webp)

Now you can use your new sentiment analysis tool!

Thank you for reading.

## **Important resources**

* [Gradio Official Website](https://gradio.app/)
* [Gradio Documentation](https://gradio.app/docs)
* [Gradio GitHub Repo](https://github.com/gradio-app/gradio)

