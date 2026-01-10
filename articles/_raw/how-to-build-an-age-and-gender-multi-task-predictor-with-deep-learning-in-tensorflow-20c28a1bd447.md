---
title: How to build an age and gender multi-task predictor with deep learning in TensorFlow
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-12T17:21:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-age-and-gender-multi-task-predictor-with-deep-learning-in-tensorflow-20c28a1bd447
coverImage: https://cdn-media-1.freecodecamp.org/images/1*EU3eKPw1MxH_0HSkto9Pfg.jpeg
tags:
- name: Data Science
  slug: data-science
- name: Deep Learning
  slug: deep-learning
- name: Machine Learning
  slug: machine-learning
- name: technology
  slug: technology
- name: TensorFlow
  slug: tensorflow
seo_title: null
seo_desc: 'By Cole Murray

  In my last tutorial, you learned about how to combine a convolutional neural network
  and Long short-term memory (LTSM) to create captions given an image. In this tutorial,
  you’ll learn how to build and train a multi-task machine learni...'
---

By Cole Murray

[In my last tutorial](https://medium.freecodecamp.org/building-an-image-caption-generator-with-deep-learning-in-tensorflow-a142722e9b1f), you learned about how to combine a convolutional neural network and Long short-term memory (LTSM) to create captions given an image. In this tutorial, you’ll learn how to build and train a multi-task machine learning model to predict the age and gender of a subject in an image.

### **Overview**

* Introduction to age and gender model
* Building a Multi-task Tensorflow Estimator
* Training

### Prerequisites

* basic understanding of convolutional neural networks (CNN)
* basic understanding of TensorFlow
* GPU (optional)

### Introduction to Age and Gender Model

In 2015, researchers from Computer Vision Lab, D-ITET, published a paper [DEX](https://www.cv-foundation.org/openaccess/content_iccv_2015_workshops/w11/papers/Rothe_DEX_Deep_EXpectation_ICCV_2015_paper.pdf) and made public their [IMDB-WIKI](https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/) consisting of 500K+ face images with age and gender labels.

![Image](https://cdn-media-1.freecodecamp.org/images/0*qQJwCUF-vuGEAd0W.png)
_IMDB-WIKI Dataset source: [https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/](https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/" rel="noopener" target="_blank" title=")_

DEX outlines an neural network architecture involving a pretrained imagenet vgg16 model that estimates the apparent age in face images. DEX placed first in [ChaLearn LAP 2015](http://chalearnlap.cvc.uab.es/) — a competition that deals with recognizing people in an image — outperforming human reference.

#### **Age as a classification problem**

A conventional way of tackling an age estimation problem with an image as input would be using a regression-based model with mean-squared error as the loss function. DEX models this problem as a classification task, using a softmax classifier with each age represented as a unique class ranging from 1 to 101 and cross-entropy as the loss function.

#### **Multi-task learning**

Multi-task learning is a technique of training on multiple tasks through a shared architecture. Layers at the beginning of the network will learn a joint generalized representation, preventing overfitting to a specific task that may contain noise.

By training with a multi-task network, the network can be trained in parallel on both tasks. This reduces the infrastructure complexity to only one training pipeline. Additionally, the computation required for training is reduced as both tasks are trained simultaneously.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2aq7M6sgJ7bglCrvsredyA.png)
_Multi-task CNN source: https://murraycole.com_

### Building a multi-task network in TensorFlow

Below you’ll use TensorFlow’s estimator abstraction to create the model. The model will be trained from raw image input to predict the age and gender of the face image.

#### **Project Structure**

```
.├── Dockerfile├── age_gender_estimation_tutorial│   ├── cnn_estimator.py│   ├── cnn_model.py│   └── dataset.py├── bin│   ├── download-imdb.sh│   ├── predict.py│   ├── preprocess_imdb.py│   └── train.py├── requirements.txt
```

#### **Environment**

For the environment, you’ll use [Docker](https://www.docker.com/) to install dependencies. A GPU version is also provided for convenience.

```
docker build -t colemurray/age-gender-estimation-tutorial -f Dockerfile .
```

#### Data

To train this model, you’ll use the IMDB-WIKI dataset, consisting of 500K+ images. For simplicity, you’ll download the pre-cropped imdb images (7GB). Run the script below to download the data.

```
chmod +x bin/download-imdb-crop.sh
```

```
./bin/download-imdb-crop.sh
```

**Preprocessing**

You’ll now process the dataset to clean out low-quality images and crop the input to a fixed image size. Additionally, you’ll format the data as a CSV to simplify reading into TensorFlow.

```
docker run -v $PWD:/opt/app \-e PYTHONPATH=$PYTHONPATH:/opt/app \-it colemurray/age-gender-estimation-tutorial \python3 /opt/app/bin/preprocess_imdb.py \--db-path /opt/app/data/imdb_crop/imdb.mat \--photo-dir /opt/app/data/imdb_crop \--output-dir /opt/app/var \--min-score 1.0 \--img-size 224
```

After approximately 20 minutes, you’ll have a processed dataset.

Next, you’ll use TensorFlow’s data pipeline module `tf.data` to provide data to the estimator. `Tf.data` is an abstraction to read and manipulate a dataset in parallel, utilizing C++ threads for performance.

Here, you’ll utilize TensorFlow’s CSV Reader to parse the data, preprocess the images, create batches, and shuffle.

#### Model

Below, you’ll create a basic CNN model. The model consists of three convolutions and two fully connected layers, with a softmax classifier head for each task.

#### Joint loss function

For the training operation, you’ll use the Adam Optimizer. For a loss function, you’ll average the cross-entropy error of each head, creating a shared loss function between the heads.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GmnF07fG1hBbzjcxeNfSng.gif)
_age and gender joint loss function_

#### TensorFlow estimator

TensorFlow estimators provide a simple abstraction for graph creation and runtime processing. TensorFlow has specified an interface `model_fn`, that can be used to create custom estimators.

Below, you’ll take the network created above and create training, eval, and predict. These specifications will be used by TensorFlow’s estimator class to alter the behavior of the graph.

### Train

Now that you’ve preprocessed the data and created the model architecture and data pipeline, you’ll begin training the model.

```
docker run -v $PWD:/opt/app \-e PYTHONPATH=$PYTHONPATH:/opt/app \-it colemurray/age-gender-estimation-tutorial:gpu \python3 /opt/app/bin/train.py \--img-dir /opt/app/var/crop \--train-csv /opt/app/var/train.csv \--val-csv /opt/app/var/val.csv \--model-dir /opt/app/var/cnn-model \--img-size 224 \--num-steps 200000
```

### Predict

Below, you’ll load your age and gender TensorFlow model. The model will be loaded from disk and predict on the provided image.

```
# Update the model path below with your modeldocker run -v $PWD:/opt/app \-e PYTHONPATH=$PYTHONPATH:/opt/app \-it colemurray/age-gender-estimation-tutorial \python3 /opt/app/bin/predict.py \--image-path /opt/app/var/crop/25/nm0000325_rm2755562752_1956-1-7_2002.jpg \--model-dir /opt/app/var/cnn-model-3/serving/<TIMESTAMP>
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*wBuO3TbAEa98-0LeQWSBfA.jpeg)
_Predicted: M/46 Actual: M/46_

### Conclusion

In this tutorial, you learned how to build and train a multi-task network for predicting a subject’s age and image. By using a shared architecture, both targets can be trained and predicted simultaneously.

Next Steps:

* Evaluate on Your Own Dataset
* Try a different network architecture
* Experiment with Different Hyperparameters

Questions/issues? Open an issue [here on GitHub](https://github.com/ColeMurray/age-gender-estimation-tutorial/issues)

Complete code [here](https://github.com/ColeMurray/age-gender-estimation-tutorial).

### Call to Action

If you enjoyed this tutorial, follow and recommend!

Interested in learning more about Deep Learning / Machine Learning? Check out my other tutorials:

[- Building an image caption generator with Deep Learning in Tensorflow](https://medium.freecodecamp.org/building-an-image-caption-generator-with-deep-learning-in-tensorflow-a142722e9b1f)

[- Building a Facial Recognition Pipeline with Deep Learning in Tensorflow](https://hackernoon.com/building-a-facial-recognition-pipeline-with-deep-learning-in-tensorflow-66e7645015b8)

[- Deep Learning CNN’s in Tensorflow with GPUs](https://medium.com/p/cba6efe0acc2)

[- Deep Learning with Keras on Google Compute Engine](https://medium.com/google-cloud/keras-inception-v3-on-google-compute-engine-a54918b0058)

[- Recommendation Systems with Apache Spark on Google Compute Engine](https://medium.com/google-cloud/recommendation-systems-with-spark-on-google-dataproc-bbb276c0dafd)

Other places you can find me:

[**Cole Murray (@_ColeMurray) | Twitter**](https://twitter.com/@_colemurray)  
[_The latest Tweets from Cole Murray (@_ColeMurray). Interests in: Machine Learning, Big Data, Android, React/flux…_twitter.com](https://twitter.com/@_colemurray)

