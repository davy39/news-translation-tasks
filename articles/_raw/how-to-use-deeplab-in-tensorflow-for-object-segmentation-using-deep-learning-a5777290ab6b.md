---
title: How to use DeepLab in TensorFlow for object segmentation using Deep Learning
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-24T20:20:58.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-deeplab-in-tensorflow-for-object-segmentation-using-deep-learning-a5777290ab6b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*mfz-HW5TIBU0AvprtApydQ.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Deep Learning
  slug: deep-learning
- name: image processing
  slug: image-processing
- name: 'tech '
  slug: tech
- name: TensorFlow
  slug: tensorflow
seo_title: null
seo_desc: 'By Beeren Sahu

  Modifying the DeepLab code to train on your own dataset for object segmentation
  in images


  _Photo by [Unsplash](https://unsplash.com/photos/FmD8tIkf8bo?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
  rel="noopener" ...'
---

By Beeren Sahu

#### Modifying the DeepLab code to train on your own dataset for object segmentation in images

![Image](https://cdn-media-1.freecodecamp.org/images/1*mfz-HW5TIBU0AvprtApydQ.jpeg)
_Photo by [Unsplash](https://unsplash.com/photos/FmD8tIkf8bo?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Nick Karvounis</a> on <a href="https://unsplash.com/search/photos/images?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

I work as a Research Scientist at [FlixStock](http://www.flixstock.com/), focusing on Deep Learning solutions to generate and/or edit images. We identify coherent regions belonging to various objects in an image using Semantic Segmentation.

[DeepLab](https://arxiv.org/abs/1706.05587) is an ideal solution for Semantic Segmentation. The code is available in TensorFlow.

In this article, I will be sharing how we can train a DeepLab semantic segmentation model for our own data-set in TensorFlow. But before we begin…

### What is DeepLab?

[DeepLab](https://arxiv.org/abs/1706.05587) is one of the most promising techniques for **semantic image segmentation** with Deep Learning. Semantic segmentation is understanding an image at the pixel level, then assigning a label to every pixel in an image such that pixels with the same label share certain characteristics.

### Installation

DeepLab implementation in TensorFlow is available on GitHub [here](https://github.com/tensorflow/models/tree/master/research/deeplab).

### Preparing Dataset

Before you create your own dataset and train DeepLab, you should be very clear about what you want to want to do with it. Here are the two scenarios:

* Training the model from scratch: you are free to have any number of classes of objects (number of labels) for segmentation. This needs a very long time for training.
* Use the pre-trained model: you are free to have any number of classes of objects for segmentation. Use the pre-trained model and only update your classifier weights with transfer learning. This will take far less time for training compared to the prior scenario.

Let us name your new dataset as “PQR”. Create a new folder “PQR” as: `tensorflow/models/research/deeplab/datasets/PQR`.

To start, all you need is input images and their pre-segmented images as ground-truth for training. Input images need to be color images and the segmented images need to be color indexed images. Refer to the PASCAL dataset.

Create a folder named “dataset” inside “PQR”. It should have the following directory structure:

```
+ dataset    -JPEGImages    -SegmentationClass    -ImageSets+ tfrecord
```

#### JPEGImages

It contains all the input color images in `*.jpg` format.

![Image](https://cdn-media-1.freecodecamp.org/images/0*M5PBchudNjWPqxPP.jpg)
_A sample input image from PASCAL VOC dataset_

#### SegmentationClass

This folder contains all the semantic segmentation annotations images for each of the color input images, which is the ground truth for the semantic segmentation.

These images should be color indexed. Each color index represents a unique class (with unique color) known as a color map.

![Image](https://cdn-media-1.freecodecamp.org/images/0*OjQiFBSrKsYnZzGS.)
_Sample Color Map [source: [https://github.com/DrSleep/tensorflow-deeplab-resnet](https://github.com/DrSleep/tensorflow-deeplab-resnet" rel="noopener" target="_blank" title=")]_

**Note:** Files in the “SegmentationClass” folder should have the same name as in the “JPEGImage” folder for corresponding image-segmentation file pair.

![Image](https://cdn-media-1.freecodecamp.org/images/0*L3AEyxEId0-95rRq.png)
_A sample semantic segmentation ground truth image from PASCAL VOC dataset_

#### ImageSets

This folder contains:

* train.txt: list of image names for the training set
* val.txt: list of image names for the validation set
* trainval.txt: list of image names for training + validation set

Sample `*.txt` file looks something like this:

```
pqr_000032pqr_000039pqr_000063pqr_000068pqr_000121
```

#### Remove the color-map in the ground truth annotations

If your segmentation annotation images are RGB images instead of color indexed images. Here is a Python script that will be of help.

Here, the palette defines the “RGB:LABEL” pair. In this sample code (0,0,0):0 is background and (255,0,0):1 is the foreground class. Note, the new_label_dir is the location where the raw segmentation data is stored.

Next, the task is to convert the image dataset to a TensorFlow record. Make a new copy of the script file`./dataset/download_and_convert_voc2012.sh` as `./dataset/convert_pqr.sh`. Below is the modified script.

The converted dataset will be saved at `./deeplab/datasets/PQR/tfrecord`

#### Defining the dataset description

Open the file **segmentation_dataset.py** present in the **research/deeplab/datasets/** folder. Add the following code segment defining the description for your PQR dataset.

```
_PQR_SEG_INFORMATION = DatasetDescriptor(    splits_to_sizes={        'train': 11111, # number of file in the train folder        'trainval': 22222,        'val': 11111,    },    num_classes=2, # number of classes in your dataset    ignore_label=255, # white edges that will be ignored to be class)
```

Make the following changes as shown bellow:

```
_DATASETS_INFORMATION = {    'cityscapes': _CITYSCAPES_INFORMATION,    'pascal_voc_seg': _PASCAL_VOC_SEG_INFORMATION,    'ade20k': _ADE20K_INFORMATION,    'pqr': _PQR_SEG_INFORMATION}
```

### Training

In order to train the model on your dataset, you need to run the train.py file in the **research/deeplab/** folder. So, we have written a script file train-pqr.sh to do the task for you.

Here, we have used xception_65 for your local training. You can specify the number of training iterations to the variable NUM_ITERATIONS. and set “ — tf_initial_checkpoint” to the location where you have downloaded or pre-trained the model *.ckpt. After training, the final trained model can be found in the TRAIN_LOGDIR directory.

Finally, run the above script from the …/research/deeplab directory.

```
# sh ./train-pqr.sh
```

Voilà! You have successfully trained DeepLab on your dataset.

In the coming months, I will be sharing more of my experiences with Images & Deep Learning. Stay tuned and don’t forget to spare some claps if you like this article. It will encourage me immensely.

