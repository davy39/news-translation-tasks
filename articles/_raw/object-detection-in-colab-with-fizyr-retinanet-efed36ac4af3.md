---
title: Object Detection in Colab with Fizyr Retinanet
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-04T17:56:59.000Z'
originalURL: https://freecodecamp.org/news/object-detection-in-colab-with-fizyr-retinanet-efed36ac4af3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*g5nzQWVR79PK2vyznKgPAA.png
tags:
- name: Google Colab
  slug: google-colab
- name: keras
  slug: keras
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By RomRoc

  Let’s continue our journey to explore the best machine learning frameworks in computer
  vision.

  In the first article we explored object detection with the official Tensorflow APIs.
  The second article was dedicated to an excellent framework f...'
---

By RomRoc

Let’s continue our journey to explore the best machine learning frameworks in computer vision.

In the [first article](https://hackernoon.com/object-detection-in-google-colab-with-custom-dataset-5a7bb2b0e97e) we explored object detection with the official Tensorflow APIs. The [second article](https://hackernoon.com/instance-segmentation-in-google-colab-with-custom-dataset-b3099ac23f35) was dedicated to an excellent framework for instance segmentation, Matterport Mask R-CNN based on Keras.

In this article we examine **Keras implementation of RetinaNet object detection developed by [Fizyr](https://github.com/fizyr/keras-retinanet)**. RetinaNet, as described in [Focal Loss for Dense Object Detection](https://arxiv.org/abs/1708.02002), is the state of the art for object detection.  
The object to detect with the trained model will be my little goat Rosa.

![Image](https://cdn-media-1.freecodecamp.org/images/gzJo8LgsXIrXkN2K65AGcJ6cfANG7XtNzsob)
_Object detection with Fizyr_

**The colab notebook and dataset are available in [my Github repo](https://github.com/RomRoc/objdet_fizyr_colab).**

In this article, we go through all the steps in a single Google Colab netebook to train a model starting from a custom dataset.

We will keep in mind these principles:

* illustrate how to make the annotation dataset
* describe all the steps in a single Notebook
* use free software, Google Colab and Google Drive, so it’s based exclusively on **_free cloud resources_**

At the end of the article you will be surprised by the simplicity of use and the good results we will obtain through this object detection framework.

_Despite its ease of use, Fizyr is a great framework, also used by the [**winner**](https://www.kaggle.com/c/rsna-pneumonia-detection-challenge/discussion/70421) **of the Kaggle competition** “RSNA Pneumonia Detection Challenge”._

### Making the dataset

We start by creating annotations for the training and validation dataset, using the tool [**LabelImg**](https://github.com/tzutalin/labelImg). This excellent annotation tool let you quickly annotate the bounding boxes of the objects to train the machine learning model.

![Image](https://cdn-media-1.freecodecamp.org/images/Id6MpAH6MV52QtprI-i9IcXRn7tIle0GQfsR)
_LabelImg annotation tool_

LabelImg creates annotations in PascalVoc format, so we need to convert annotations to Fizyr format:

* create a zip file containing training dataset images and annotations with the same filename (check my example dataset in Github)

```
objdet_dataset.zip|- img1.jpg|- img1.xml|- img2.jpg|- img2.xml...
```

* Upload zip file in Google Drive, get Drive file id, and substitute the DATASET_DRIVEID value
* Run cell that iterates over the xml files and creates annotations.csv file

_Note: you can see [my answer](https://stackoverflow.com/a/48855034/9250875) on Stackoverflow to get the Drive file id._

### Model training

Model training is the core of the notebook. Fizyr offers various parameters, described in [Github](https://github.com/fizyr/keras-retinanet/blob/c841da27f540084d27e971b6d00c178ff005d344/keras_retinanet/bin/train.py#L358), to run and optimize this step.

It’s a good option to start from a pretrained model instead of training a model from scratch. Fizyr released a model based on ResNet50 architecture, pretrained on Coco dataset.

```
URL_MODEL = 'https://github.com/fizyr/keras-retinanet/releases/download/0.5.0/resnet50_coco_best_v2.1.0.h5'
```

We can even use our pretrained model, and continue the training from it. This option is particularly useful to train for some epochs, so save it in Google Drive, and later restart the training from the saved model. In this way we can bypass the 12-hour execution limit in Colab, and we can train the model for many epochs.

From my tests, a high value of batch_size and steps offers better results, but they greatly increase the execution time of each epoch.

![Image](https://cdn-media-1.freecodecamp.org/images/PntGODQ4dBvWoaqJGrEErgXfKuOiBRnGE8D8)
_Tensorboard training charts_

We can start training from our custom dataset with:

```
!keras_retinanet/bin/train.py --freeze-backbone --random-transform --weights {PRETRAINED_MODEL} --batch-size 8 --steps 500 --epochs 10 csv annotations.csv classes.csv
```

Let’s analyze each argument passed to the script train.py.

* freeze-backbone: freeze the backbone layers, particularly useful when we use a small dataset, to avoid overfitting
* random-transform: randomly transform the dataset to get data augmentation
* weights: initialize the model with a pretrained model (your own model or one released by Fizyr)
* batch-size: training batch size, higher value gives smoother learning curve
* steps: number of steps for epochs
* epochs: number of epochs to train
* csv: annotations files generated by the script above

The training process output contains a description of layers and loss metrics during training, and as you can see, loss metrics decrease during each epoch:

```
Using TensorFlow backend....Layer (type)                    Output Shape         Param #     Connected toinput_1 (InputLayer)            (None, None, None, 3 0padding_conv1 (ZeroPadding2D)   (None, None, None, 3 0           input_1[0][0]                    ...Total params: 36,382,957Trainable params: 12,821,805Non-trainable params: 23,561,152NoneEpoch 1/10500/500 [==============================] - 1314s 3s/step - loss: 1.0659 - regression_loss: 0.6996 - classification_loss: 0.3663Epoch 2/10500/500 [==============================] - 1296s 3s/step - loss: 0.6747 - regression_loss: 0.5698 - classification_loss: 0.1048Epoch 3/10500/500 [==============================] - 1304s 3s/step - loss: 0.5763 - regression_loss: 0.5010 - classification_loss: 0.0753
```

```
Epoch 3/10500/500 [==============================] - 1257s 3s/step - loss: 0.5705 - regression_loss: 0.4974 - classification_loss: 0.0732
```

### Inference

The last step performs inference of test images with the trained model.  
The Fizyr framework allows us to perform inference using CPU, even if you trained the model with GPU. This feature is important in typical production environments, where people usually opt for less expensive hardware infrastructures for inference, without GPUs.

Let’s examine the following lines in detail:

```
model_path = os.path.join('snapshots', sorted(os.listdir('snapshots'), reverse=True)[0])print(model_path)
```

```
# load retinanet modelmodel = models.load_model(model_path, backbone_name='resnet50')model = models.convert_model(model)
```

The first line sets the model file as the last model generated by the training process in /snapshots directory. Then the model is loaded from the filesystem and converted to run inference.

You can change the values of THRES_SCORE, which represents the confidence threshold to show an object detection.

![Image](https://cdn-media-1.freecodecamp.org/images/mkkUoWpQY5-4mpXzEacDzy7bqP1QfGaVqUXZ)
_Object detection inference_

### Conclusions

We went through the complete journey to make object detection with Fizyr implementation of RetinaNet. We created a dataset, trained a model, and ran inference ([here](https://github.com/RomRoc/objdet_fizyr_colab) is my Github repo for the notebook and dataset).

I was impressed by the following aspects of this excellent framework:

* this framework is **easy to use** to get good inference, even without much customization
* it was **simple to transform annotations** to Fizyr’s dataset format, compared to other frameworks.

In general Fizyr is a good choice to start an object detection project, in particular if you need to quickly get good results.

If you enjoyed this article, leave a few claps, it will encourage me to explore further machine learning opportunities :)

