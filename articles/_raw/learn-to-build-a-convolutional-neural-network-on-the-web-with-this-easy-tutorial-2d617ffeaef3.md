---
title: Learn to build a Convolutional Neural Network on the web with this easy tutorial
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-18T10:32:13.000Z'
originalURL: https://freecodecamp.org/news/learn-to-build-a-convolutional-neural-network-on-the-web-with-this-easy-tutorial-2d617ffeaef3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*aIR9I9JDL5GyVxINeQXy7g.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By John David Chibuk

  This post explains how to build your first Convolutional Neural Network (CNN) to
  detect between two image types: for example, a bunny or a puppy.

  Thanks to Google’s new web tool, getting started building and prototyping your own
  ...'
---

By John David Chibuk

This post explains how to build your first Convolutional Neural Network (CNN) to detect between two image types: for example, a bunny or a puppy.

Thanks to Google’s new web tool, getting started building and prototyping your own neural network can be quite easy.

Here is a [link](https://drive.google.com/file/d/1a7V9Hc7ks0xxDbfCZl2_96DUGlCLuh00/view?usp=sharing) to the web-based application. It shows you the code and lets you run “paragraph by paragraph” (**shift+enter**) jupyter notebook code to let you train a model and then test it. Find the [Github public repo here](https://github.com/chibuk/simple-cnn-keras-colaboratory/tree/master).

**The first step is to set up the Colab notebook + image data folders on your own Google drive, so let’s do that!**

In your Google drive, you will need to set up folders with images that store the data to be trained. You can [copy this folder](https://drive.google.com/drive/folders/1rcihLGtsL8WbaYhBAShz8ntqr8G9BvPP?usp=sharing) directly and put in your own Google drive, and then unzip it and put it in a folder called “Colab Notebooks” in your base Google drive folder.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ALReQ6ZGyihWCrj1dxaZ6g.png)
_Screenshot from Personal Google Drive_

In the images folder, there are two subfolders.

> train

> test

![Image](https://cdn-media-1.freecodecamp.org/images/1*KN1hY9fwsJ4_89v45PYgQA.png)
_Screenshot from Personal Google Drive_

Each of these folders then contains folders to represent the types of images you want to identify.

> bunny

> puppy

There should be a bunny and puppy folder in each train + test folder.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ec40wwNgWLfFDYwMjXp03w.png)
_Screenshot from Personal Google Drive_

Fill these folders with images. Put ~80% in the train folder and 20% in the test folder.

The tricky part of the tutorial is getting the folders linked properly within Google drive. You need to connect via API keys a few times to establish the proper connection to your personal Google drive folder.

Please note: you need to keep the same folder structure as defined in the tutorial to have it run properly.

In your base Google Drive folder, you should have a folder called: Colab Notebooks.

Inside there should be a directory called: Simple CNN Image Tutorial

This should contain the contents of the images and Colab notebook from above.

### Step by step

**Step 1** installs the required libraries to build and train a model with Google’s tensorflow + Keras. Keras is a simplified layer to make model training easier on top of Tensorflow.

**Step 2–5** links your Google drive up to the project, copies the keys over from the cells, and pastes them in the notebook as they are generated. This might take a few tries, but its okay!

**Step 6** You can change the structure, but you will need to update the path in the notebook to match where you put the base Simple CNN Image Tutorial folder.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Cw3unWxH0dzAhkEjAAurjA.png)
_Screenshot from CoLaboratory Notebook (Step 6)_

**Step 7** confirms that you have your images loaded in Google drive.

![Image](https://cdn-media-1.freecodecamp.org/images/1*qeWPe1_oEcGxPGPUBZdB0Q.png)
_Screenshot from CoLaboratory Notebook (Step 7)_

To run the process, simply click the first paragraph area and click “shift + enter” on your keyboard. This runs the code in each cell and lets you step through the process.

**Step 9** trains your model. If everything is referenced properly it should show output like this ->

![Image](https://cdn-media-1.freecodecamp.org/images/1*bfNiqh12lfRKi19QBpOGOA.png)
_Screenshot from CoLaboratory Notebook (Step 9)_

When it’s done, your model will be trained and you can test images from what you put in the new images folder:

![Image](https://cdn-media-1.freecodecamp.org/images/1*HwQMoikc5fHGy926WKii0g.png)
_Screenshot from CoLaboratory Notebook (add new images here or use these to try out your trained network!)_

Simply change the image name text in the line of code:

```
test_image = image.load_img(‘./newimages/puppy3.jpg’, target_size = (64, 64))
```

So you would change for example:

```
‘./newimages/puppy3.jpg’ to ‘./newimages/bunny1.jpg’
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*kj0G3pgNloyY2cgUa2b3gQ.png)
_Screenshot from CoLaboratory Notebook (Step 10)_

Finally run the paragraph and see what your model classifies the new image to be!

### Congrats you have just trained and tested your first convolutional neural network — it’s bananas!

![Image](https://cdn-media-1.freecodecamp.org/images/1*7gqbeeOQP1vJhLYfKkPpzQ.png)
_Credit: [http://media.riffsy.com/images/7bafc4dc0036792b32a5e5aa6c5ac9ff/tenor.gif](http://media.riffsy.com/images/7bafc4dc0036792b32a5e5aa6c5ac9ff/tenor.gif" rel="noopener" target="_blank" title=")_

