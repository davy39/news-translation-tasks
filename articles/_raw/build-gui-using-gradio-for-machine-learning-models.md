---
title: How to Build a GUI Using Gradio for Machine Learning Models
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-01-27T21:00:00.000Z'
originalURL: https://freecodecamp.org/news/build-gui-using-gradio-for-machine-learning-models
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/gradio-image-2.png
tags:
- name: deployment
  slug: deployment
- name: Machine Learning
  slug: machine-learning
- name: scikit learn
  slug: scikit-learn
seo_title: null
seo_desc: "By Edem Gold\nIf you have ever built a Machine Learning model, you've probably\
  \ thought \"well this was cool, but how will other people be able to see how cool\
  \ it is?\" \nModel deployment is a part of Machine Learning which isn't talked about\
  \ as much as i..."
---

By Edem Gold

If you have ever built a Machine Learning model, you've probably thought "well this was cool, but how will other people be able to see how cool it is?" 

Model deployment is a part of Machine Learning which isn't talked about as much as it should be.

So in this article, I will introduce you to a new tool that will help you generate a web app for your Machine Learning model which you can then share with other devs so they can try it out.

I will be building a simple neural network model using scikit-learn and I'll create a GUI for the model using Gradio (this is the cool new tool I spoke about).

Let's get started.

> We cannot solve our problems with the same thinking we used to create them - Albert Einstein

# What is Gradio?

![gradio cover.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1632054788128/NVI4Jgdrd.png?auto=compress,format&format=webp)
_****image credits: [gradio](https://gradio.app/)****_

According to the [Gradio website](https://gradio.app/), 

> Gradio allows you to quickly create customizable UI components around your TensorFlow or PyTorch models or even arbitrary Python functions.

Well, that's not terribly informative, is it? 😅.

If you have ever used a Python GUI library like Tkinter, then Gradio is like that.

Gradio is a GUI library that allows you to create customizable GUI components for your Machine Learning model.

Now that we understand what Gradio is, let's get into the project.

## **Pre-requisite**

For you to successfully work through this tutorial, you'll need to have Python installed.

# Let's Get Building

You can check out the GitHub repo for the project [here](https://github.com/EdemGold/gradio_project). Now I'll take you through the project step by step.

### Install the required packages

Let's install the required packages:

```
pip install sklearn

```

```
pip install pandas

```

```
pip install numpy

```

```
pip install gradio

```

### Get our data

Our data is going to be in the .CSV format. You can get the data by clicking [here](https://raw.githubusercontent.com/EdemGold/gradio_project/main/diabetes.csv).

### Import the Packages

We are going to import the required packages like this:

```
import numpy as np

import pandas as pd

import gradio as gr

```

Next, we are going to filter the warnings so we don't see them.

```
import warnings

warnings.filterwarnings('ignore')

```

### Import the data

Next, we are going to import our data:

```
data = pd.read_csv('diabetes.csv')

```

Now let's see a little preview of our dataset with this command:

```
data.head()

```

Let's see the feature columns in our dataset:

```
print (data.columns)

```

### Get our Variables

Next, we get our X and Y variables, so type in these commands:

```
x = data.drop(['Outcome'], axis=1)

y = data['Outcome']

```

### Split the data

Now we are going to split our data using scikit-learn's inbuilt _train_test_split_ function.

```
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y)

```

### Scale our data

Next, we are going to scale our data using scikit-learn's inbuilt _StandardScaler_ object.

```
from sklearn.preprocessing import StandardScaler

#instantiate StandardScaler object
scaler = StandardScaler()

#scale data
x_train_scaled = scaler.fit_transform(x_train)

x_test_scaled = scaler.fit_transform(x_test)

```

In the code above, we scaled our data using the StandardScaler object made available to us through scikit-learn. To learn more about Scaling and why we do it, click [here](https://www.analyticsvidhya.com/blog/2020/04/feature-scaling-machine-learning-normalization-standardization/).

### Instantiate and train the model

In this section, we are going to create and train our model. The model we are going to use will be a Multi-Layer Perceptron Classifier, a neural network built into scikit-learn.

```
#import model object
from sklearn.neural_network import MLPClassifier
model =  MLPClassifier(max_iter=1000,  alpha=1)

#train model on training data
model.fit(x_train_scaled, y_train)

#getting model performance on test data
print("accuracy:", model.score(x_test_scaled, y_test))

```

### Create the function for Gradio

Now comes the fun part. Here we are going to create a function that will take in the features of the data set which our model was trained on and pass it as an array to our model to predict. Then we are going to build our Gradio web app based on that function.

To understand why we have to write a function, you must first understand that Gradio builds GUI components for our Machine Learning model based on the function. The function provides a way for Gradio to get input from users and pass it on to the ML model, which will then process it and then pass it back to Gradio which then passes the result out.

Let's write some code...

First, we will get the feature columns which we will then pass onto our function.

```
#geting our columns

print(data.columns)

```

Now we will create our function like this:

```
def diabetes(Pregnancies, Glucose, Blood_Pressure, SkinThickness, Insulin, BMI, Diabetes_Pedigree, Age):
#turning the arguments into a numpy array  

 x = np.array([Pregnancies,Glucose,Blood_Pressure,SkinThickness,Insulin,BMI,Diabetes_Pedigree,Age])

  prediction = model.predict(x.reshape(1, -1))

  return prediction

```

In the code above, we passed the feature columns from our data as arguments into a function which we named _diabetes_. Then we turned the arguments into a NumPy array which we then passed onto our model for prediction. Finally we returned the predicted result of our model.

### Create our Gradio Interface

Now we are going to create our Web App interface using Gradio:

```
outputs = gr.outputs.Textbox()

app = gr.Interface(fn=diabetes, inputs=['number','number','number','number','number','number','number','number'], outputs=outputs,description="This is a diabetes model")

```

The first thing we did above was to create a variable named outputs which holds the GUI component for our model result. The result of our model's prediction will be outputted in a text box.

Then we instantiated the Gradio interface object and passed in our earlier _diabetes_ function. Then we generated our Inputs GUI component and told the radio to expect 8 inputs in the form of numbers.

The inputs represent the feature columns that are present in our dataset – the same 8 feature column names we passed into our _diabetes_ function.

Then we passed our earlier output variable into the outputs parameter present in the object.

Finally, we passed in the description of our web app into the description parameter.

### Launch the Gradio Web App

Now we're going to Launch our Gradio web app.

```
app.launch()

```

**NOTE:** If you are launching the Gradio app as a script from that e command line, you will be given a local host link which you will then copy and paste into your browser to see your web app.

If you are launching the app from a Jupyter notebook, you will see a live preview of the app as you run the cell (and you will also be provided with a link).

### Host and Share your Web App

If you want to share your web app, all you have to do is put in `share=True` as a parameter in your launch object.

```
#To provide a shareable link
app.launch(share=True)

```

You'll then get a link with a .gradio extension. But this shareable link lasts for only 24 hours and will last if only your system is running. Because Gradio just hosts the web app on your system.

In simple words, for your link to work, your system has to be on. This is because Gradio uses your system to host the web app, so once your system is off the server connection is severed and you get a 500😅.

Luckily for us, Gradio also provides a way for you to permanently host your model. But the service is subscription-based, so you have to pay $7 monthly to access it. Permanent hosting is way out of the scope of this article (partly because the author is broke😅). But if you are interested in it, click [here](https://www.gradio.app/introducing-hosted).

## **Important resources**

* [Gradio Website](https://gradio.app/)
* [Gradio Documentation](https://gradio.app/docs)
* [Gradio on GitHub](https://github.com/gradio-app/gradio)

## **Summary**

The Gradio library is really cool and it helps solve a huge problem plaguing the Machine Learning community – model deployment.

90% of Machine Learning models built are not deployed, and Gradio is working to fix that.

It also serves as a way for beginners and experts to show off their models and also test the models in real life.

You can't go wrong with the Gradio Library. Give it a try.

[Cover image source](https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_256,w_256,f_auto,q_auto:eco,dpr_1/tv8zrejyehjshagvxgt7).

