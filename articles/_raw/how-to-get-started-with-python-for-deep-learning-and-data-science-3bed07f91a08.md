---
title: How to get started with Python for Deep Learning and Data Science
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-06T17:39:37.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-started-with-python-for-deep-learning-and-data-science-3bed07f91a08
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7aJPlxn8gwhI7JjcBFr-tQ.jpeg
tags:
- name: Data Science
  slug: data-science
- name: Deep Learning
  slug: deep-learning
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Joseph Lee Wei En

  A step-by-step guide to setting up Python for a complete beginner


  You can code your own Data Science or Deep Learning project in just a couple of
  lines of code these days. This is not an exaggeration; many programmers out there
  ...'
---

By Joseph Lee Wei En

#### A step-by-step guide to setting up Python for a complete beginner

![Image](https://cdn-media-1.freecodecamp.org/images/f2tiBCqS6IVb1yWNurylwXhNi4fEDOeiVlib)

You can code your own Data Science or Deep Learning project in just a couple of lines of code these days. This is not an exaggeration; many programmers out there have done the hard work of writing tons of code for us to use, so that all we need to do is plug-and-play rather than write code from scratch.

You may have seen some of this code on Data Science / Deep Learning blog posts. Perhaps you might have thought: “Well, if it’s really that easy, then why don’t I try it out myself?”

If you’re a beginner to Python and you want to embark on this journey, then this post will guide you through your first steps. A common complaint I hear from complete beginners is that it’s pretty difficult to set up Python. How do we get everything started in the first place so that we can plug-and-play Data Science or Deep Learning code?

This post will guide you through in a step-by-step manner how to set up Python for your Data Science and Deep Learning projects. We will:

* Set up Anaconda and Jupyter Notebook
* Create Anaconda environments and install packages (code that others have written to make our lives tremendously easy) like tensorflow, keras, pandas, scikit-learn and matplotlib.

Once you’ve set up the above, you can build your first neural network to predict house prices in this tutorial here:

[Build your first Neural Network to predict house prices with Keras](https://medium.com/intuitive-deep-learning/build-your-first-neural-network-to-predict-house-prices-with-keras-eb5db60232c)

### Setting up Anaconda and Jupyter Notebook

The main programming language we are going to use is called Python, which is the most common programming language used by Deep Learning practitioners.

The first step is to download Anaconda, which you can think of as a platform for you to use Python “out of the box”.

Visit this page: [https://www.anaconda.com/distribution/](https://www.anaconda.com/distribution/) and scroll down to see this:

![Image](https://cdn-media-1.freecodecamp.org/images/Y9PBNXOl0NLmLPp1DBpQrodepqZ0UCwk6KWT)
_Download Anaconda_

This tutorial is written specifically for Windows users, but the instructions for users of other Operating Systems are not all that different. Be sure to click on “Windows” as your Operating System (or whatever OS that you are on) to make sure that you are downloading the correct version.

This tutorial will be using Python 3, so click the green Download button under “Python 3.7 version”. A pop up should appear for you to click “Save” into whatever directory you wish.

![Image](https://cdn-media-1.freecodecamp.org/images/nIBsLmbM3QXFAvKh5DvOgQTAvaIlaEzbtmIO)

Once it has finished downloading, just go through the setup step by step as follows:

![Image](https://cdn-media-1.freecodecamp.org/images/j7MTrYBa-vBDFljeE6ELgJ2Rb1r8XJwfppgg)
_Click Next_

![Image](https://cdn-media-1.freecodecamp.org/images/xIqTDiWBgQIDNdr6ZKUbe0cD2YDdcHG0znwT)
_Click “I Agree”_

![Image](https://cdn-media-1.freecodecamp.org/images/JK4bVL-3d5CAoMaLIFdWKKN6fOY6iEe54KP2)
_Click Next_

![Image](https://cdn-media-1.freecodecamp.org/images/82jlqCIonJ-6eSkwL7yIfWZfV8Zw4V6oJayA)
_Choose a destination folder and click Next_

![Image](https://cdn-media-1.freecodecamp.org/images/irLpIjKObhEjNp9fguypnF8AQo4FvglVqHDY)
_Click Install with the default options, and wait for a few moments as Anaconda installs_

![Image](https://cdn-media-1.freecodecamp.org/images/cAyLf4jFGXquhZynYWlPinokrY-ZP6RGstLu)
_Click Skip as we will not be using Microsoft VSCode in our tutorials_

![Image](https://cdn-media-1.freecodecamp.org/images/qdbsbeVWov2V5zW0RXjZSNnYxRFmVivKC3Jn)
_Click Finish, and the installation is done!_

Once the installation is done, go to your Start Menu and you should see some newly installed software:

![Image](https://cdn-media-1.freecodecamp.org/images/tOWuum3G7ONEAIhgmji6dYRurvqA5Z2lI1jw)
_You should see this on your start menu_

Click on Anaconda Navigator, which is a one-stop hub to navigate the apps we need. You should see a front page like this:

![Image](https://cdn-media-1.freecodecamp.org/images/pGBii7zWZSsvRP9qrBXbRFusVmj5lgcSCIe4)
_Anaconda Navigator Home Screen_

Click on ‘Launch’ under Jupyter Notebook, which is the second panel on my screen above. Jupyter Notebook allows us to run Python code interactively on the web browser, and it’s where we will be writing most of our code.

A browser window should open up with your directory listing. I’m going to create a folder on my Desktop called “Intuitive Deep Learning Tutorial”. If you navigate to the folder, your browser should look something like this:

![Image](https://cdn-media-1.freecodecamp.org/images/Q7CdWULn4gjQ8GPSGnzIUfvSoD3Dt2dOj-Ud)
_Navigating to a folder called Intuitive Deep Learning Tutorial on my Desktop_

On the top right, click on New and select “Python 3”:

![Image](https://cdn-media-1.freecodecamp.org/images/27sYFSx5iqHK-y-cxD9sMXXkg7zP9brYRsyS)
_Click on New and select Python 3_

A new browser window should pop up like this.

![Image](https://cdn-media-1.freecodecamp.org/images/k9-ZWdXld94RG03TXpaM-ELcFerj-kmY7Ldw)
_Browser window pop-up_

Congratulations — you’ve created your first Jupyter notebook! Now it’s time to write some code. Jupyter notebooks allow us to write snippets of code and then run those snippets without running the full program. This helps us perhaps look at any intermediate output from our program.

To begin, let’s write code that will display some words when we run it. This function is called _print_. Copy and paste the code below into the grey box on your Jupyter notebook:

```
print("Hello World!")
```

Your notebook should look like this:

![Image](https://cdn-media-1.freecodecamp.org/images/felCZ7xmEgHusNkuzlT5KwoGnjFZl23INRRJ)
_Entering in code into our Jupyter Notebook_

Now, press Alt-Enter on your keyboard to run that snippet of code:

![Image](https://cdn-media-1.freecodecamp.org/images/0q66xA7p0oKXMFqmtv0ZzH1ZLGp37LeZ8MKT)
_Press Alt-Enter to run that snippet of code_

You can see that Jupyter notebook has displayed the words “Hello World!” on the display panel below the code snippet! The number 1 has also filled in the square brackets, meaning that this is the first code snippet that we’ve run thus far. This will help us to track the order in which we have run our code snippets.

Instead of Alt-Enter, note that you can also click Run when the code snippet is highlighted:

![Image](https://cdn-media-1.freecodecamp.org/images/ZSo3TOPK1RIkjPhlyrfWhPcscCaYf72XEqOT)
_Click Run on the panel_

If you wish to create new grey blocks to write more snippets of code, you can do so under Insert.

![Image](https://cdn-media-1.freecodecamp.org/images/8PmsMQDCyquKK3GSM9cUWCw1bDOkGedAvsB2)

Jupyter Notebook also allows you to write normal text instead of code. Click on the drop-down menu that currently says “Code” and select “Markdown”:

![Image](https://cdn-media-1.freecodecamp.org/images/R2LdzqHjihNjlx54HHyoSm3qFUurL0fPDbav)

Now, our grey box that is tagged as markdown will not have square brackets beside it. If you write some text in this grey box now and press Alt-Enter, the text will render it as plain text like this:

![Image](https://cdn-media-1.freecodecamp.org/images/Yb7GdouMsQTeD3136CkR0TxPBZ81w98BBUIP)
_If we write text in our grey box tagged as markdown, pressing Alt-Enter will render it as plain text._

There are some other features that you can explore. But now we’ve got Jupyter notebook set up for us to start writing some code!

### Setting up Anaconda environment and installing packages

Now we’ve got our coding platform set up. But are we going to write Deep Learning code from scratch? That seems like an extremely difficult thing to do!

The good news is that many others have written code and made it available to us! With the contribution of others’ code, we can play around with Deep Learning models at a very high level without having to worry about implementing all of it from scratch. This makes it extremely easy for us to get started with coding Deep Learning models.

For this tutorial, we will be downloading five packages that Deep Learning practitioners commonly use:

* Tensorflow
* Keras
* Pandas
* Scikit-learn
* Matplotlib

The first thing we will do is to create a Python environment. An environment is like an isolated working copy of Python, so that whatever you do in your environment (such as installing new packages) will not affect other environments. It’s good practice to create an environment for your projects.

Click on Environments on the left panel and you should see a screen like this:

![Image](https://cdn-media-1.freecodecamp.org/images/wKXNPPjAOJAtpF7h2qDmHRWPJcZPSTxwXGqA)
_Anaconda environments_

Click on the button “Create” at the bottom of the list. A pop-up like this should appear:

![Image](https://cdn-media-1.freecodecamp.org/images/JYiSWmlNr70YIJmJIzeiwgu4ZGDnGRH1sLH2)
_A pop-up like this should appear._

Name your environment and select Python 3.7 and then click Create. This might take a few moments.

Once that is done, your screen should look something like this:

![Image](https://cdn-media-1.freecodecamp.org/images/ZP0bAkPwg2ehjpiEbfqefPLsV4N7ao6tcqMM)

Notice that we have created an environment ‘intuitive-deep-learning’. We can see what packages we have installed in this environment and their respective versions.

Now let’s install some packages we need into our environment!

The first two packages we will install are called Tensorflow and Keras, which help us plug-and-play code for Deep Learning.

On Anaconda Navigator, click on the drop down menu where it currently says “Installed” and select “Not Installed”:

![Image](https://cdn-media-1.freecodecamp.org/images/vQgrLpY-TCpmVQNpE8Qj8lDOXZiMSrnxOxbw)

A whole list of packages that you have not installed will appear like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1AMaD4UNcBGBOhnRYTkTOA4z7VMXsxi3nVgx)

Search for “tensorflow”, and click the checkbox for both “keras” and “tensorflow”. Then, click “Apply” on the bottom right of your screen:

![Image](https://cdn-media-1.freecodecamp.org/images/42cYM75C41sZ0XQB2VM8SCCE5Smvaa5uFRxo)

A pop up should appear like this:

![Image](https://cdn-media-1.freecodecamp.org/images/Grmx5-30t2TXd0n20TM3ySlKEp5xStkbQsuC)

Click Apply and wait for a few moments. Once that’s done, we will have Keras and Tensorflow installed in our environment!

Using the same method, let’s install the packages ‘pandas’, ‘scikit-learn’ and ‘matplotlib’. These are common packages that data scientists use to process the data as well as to visualize nice graphs in Jupyter notebook.

This is what you should see on your Anaconda Navigator for each of the packages.

**Pandas:**

![Image](https://cdn-media-1.freecodecamp.org/images/VJAyfunO6Bli1IzzaYyr7tPImAmYqtpW87l8)
_Installing pandas into your environment_

**Scikit-learn:**

![Image](https://cdn-media-1.freecodecamp.org/images/f7d8Fc8ijy-9aXb-nBYSh8mZyMKZedqp-xtw)
_Installing scikit-learn into your environment_

**Matplotlib:**

![Image](https://cdn-media-1.freecodecamp.org/images/OsHyfrHq4ipaGbL4yzm8FrJguUuZdGTcbLLS)
_Installing matplotlib into your environment_

Once it’s done, go back to “Home” on the left panel of Anaconda Navigator. You should see a screen like this, where it says “Applications on intuitive-deep-learning” at the top:

![Image](https://cdn-media-1.freecodecamp.org/images/pNCTBZKHAKE3o1PqfPMaLo6c-adW8W7sMk70)

Now, we have to install Jupyter notebook in this environment. So click the green button “Install” under the Jupyter notebook logo. It will take a few moments (again). Once it’s done installing, the Jupyter notebook panel should look like this:

![Image](https://cdn-media-1.freecodecamp.org/images/utwIe99nFcwxxpNPDn-1Hufq2PzvnAXrLdvG)

Click on Launch, and the Jupyter notebook app should open.

Create a notebook and type in these five snippets of code and click Alt-Enter. This code tells the notebook that we will be using the five packages that you installed with Anaconda Navigator earlier in the tutorial.

```
import tensorflow as tf
```

```
import keras
```

```
import pandas
```

```
import sklearn
```

```
import matplotlib
```

If there are no errors, then congratulations — you’ve got everything installed correctly:

![Image](https://cdn-media-1.freecodecamp.org/images/saAFY17Par0VXZyDXdi332aKEXsLIZ9527a8)
_A sign that everything works!_

Now that we’ve got everything set up, we’ll start building our first neural network here:

[**Build your first Neural Network to predict house prices with Keras**](https://medium.com/intuitive-deep-learning/build-your-first-neural-network-to-predict-house-prices-with-keras-eb5db60232c)  
[_A step-by-step complete beginner’s guide to building your first Neural Network in a couple lines of code like a Deep…_medium.com](https://medium.com/intuitive-deep-learning/build-your-first-neural-network-to-predict-house-prices-with-keras-eb5db60232c)

If you have had any trouble with any of the steps above, please feel free to comment below and I’ll help you out!

**About the author:**

Hi there, I’m [Joseph](http://ai.stanford.edu/~josephlee)! I recently graduated from Stanford University, where I worked with Andrew Ng in the [Stanford Machine Learning Group](https://stanfordmlgroup.github.io/). I want to make Deep Learning concepts as intuitive and as easily understandable as possible by everyone, which has motivated my publication: [Intuitive Deep Learning](https://medium.com/intuitive-deep-learning).

