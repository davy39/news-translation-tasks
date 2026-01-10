---
title: Diving into Deep Convolutional Semantic Segmentation Networks and Deeplab_V3
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-10T11:08:51.000Z'
originalURL: https://freecodecamp.org/news/diving-into-deep-convolutional-semantic-segmentation-networks-and-deeplab-v3-4f094fa387df
coverImage: https://cdn-media-1.freecodecamp.org/images/1*rZ1vDrOBWqISFiNL5OMEbg.jpeg
tags:
- name: Deep Learning
  slug: deep-learning
- name: Machine Learning
  slug: machine-learning
- name: neural networks
  slug: neural-networks
- name: 'tech '
  slug: tech
- name: TensorFlow
  slug: tensorflow
seo_title: null
seo_desc: 'By Thalles Silva

  Deep Convolutional Neural Networks (DCNNs) have achieved remarkable success in various
  Computer Vision applications. Like others, the task of semantic segmentation is
  not an exception to this trend.

  This piece provides an introductio...'
---

By Thalles Silva

Deep Convolutional Neural Networks (DCNNs) have achieved remarkable success in various Computer Vision applications. Like others, the task of semantic segmentation is not an exception to this trend.

This piece provides an introduction to Semantic Segmentation with a hands-on TensorFlow implementation. We’ll go over one of the most relevant papers on Semantic Segmentation of general objects — [Deeplab_v3](https://arxiv.org/abs/1706.05587). You can clone the notebook for this post [here](https://github.com/sthalles/deeplab_v3).

### Semantic Segmentation

Regular image classification DCNNs have similar structure. These models take images as input and output a single value representing the category of that image.

Usually, classification DCNNs have four main operations. Convolutions, activation function, pooling, and fully-connected layers. Passing an image through a series of these operations outputs a feature vector containing the probabilities for each class label. Note that in this setup, we categorize an image as a whole. That is, we assign a single label to an entire image.

![Image](https://cdn-media-1.freecodecamp.org/images/0*VMJtEUeJyA-XbDgF.jpg)
_Standard deep learning model for image recognition. Image credits: [Convolutional Neural Network MathWorks](https://www.mathworks.com/discovery/convolutional-neural-network.html" rel="noopener" target="_blank" title=")._

Different from image classification, in semantic segmentation we want to make decisions for every pixel in an image. So, for each pixel, the model needs to classify it as one of the pre-determined classes. Put another way, semantic segmentation means understanding images at a pixel level.

Keep in mind that semantic segmentation doesn’t differentiate between object instances. Here, we try to assign an individual label to each pixel of a digital image. Thus, if we have two objects of the same class, they end up having the same category label. Instance Segmentation is the class of problems that differentiate instances of the same class.

![Image](https://cdn-media-1.freecodecamp.org/images/0*_VVeYr35i5GM6p6_.png)
_Difference between Semantic Segmentation and Instance Segmentation. (middle) Although they are the same object (bus) they are classified as different objects. (left) Same object, equal category._

Yet, regular DCNNs such as the AlexNet and VGG aren’t suitable for dense prediction tasks. First, these models contain many layers designed to reduce the spatial dimensions of the input features. As a consequence, these layers end up producing highly decimated feature vectors that lack sharp details. Second, fully-connected layers have fixed sizes and loose spatial information during computation.

As an example, instead of having pooling and fully-connected layers, imagine passing an image through a series of convolutions. We can set each convolution to have _stride of 1_ and “SAME” padding. **Doing this, each convolution preserves the spatial dimensions of its input**. We can stack a bunch of these convolutions and have a segmentation model.

![Image](https://cdn-media-1.freecodecamp.org/images/0*gAVdLPKbQphFjAYa.png)
_Fully-Convolution neural network for dense prediction task. Note the non-existence of pooling and fully-connected layers._

This model could output a probability tensor with shape _[W,H,C]_, where W and H represent the Width and Height, and C is the number of class labels. Applying the _argmax_ function (on the third axis) gives us a tensor shape of _[W,H,1]_. After, we compute the cross-entropy loss between each pixel of the ground-truth images and our predictions. In the end, we average that value and train the network using back prop.

There is one problem with this approach, though. As we mentioned, using convolutions with stride 1 and _“SAME”_ padding preserves the input dimensions. However, doing that would make the model super expensive in both memory consumption and computation complexity.

To ease that problem, segmentation networks usually have three main components: convolutions, downsampling, and upsampling layers.

![Image](https://cdn-media-1.freecodecamp.org/images/0*3TxBI1xNIDm_Z615.png)
_Encoder-decoder architecture for Image Semantic Segmentation._

There are two common ways to do downsampling in neural nets: by using _convolution striding_ or regular _pooling_ operations. In general, downsampling has one goal, and that is to reduce the spatial dimensions of given feature maps. For that reason, downsampling allows us to perform deeper convolutions without many memory concerns. Yet, they do it to the detriment of losing some features in the process.

Also, note that the first part of this architecture looks a lot like usual classification DCNNs. With one exception, they do not put in place _fully-connected_ layers.

After the first part, we have a feature vector with shape [W, H, D] where W, H, and D are the width, height and depth of the feature tensor. Note that the spatial dimensions of this compressed vector are smaller (yet denser) than the original input.

![Image](https://cdn-media-1.freecodecamp.org/images/0*dT0gcJavW_LQY4Dm.png)
_(Top) VGG-16 network in its original form. Note the 3 fully-connected layers on top of the convolution stack. (Down) VGG-16 model when substituting its fully-connected layers to 1x1 convolutions. This change allows the network to output coarse heat-maps. Image credits: [Fully Convolutional Networks for Semantic Segmentation](https://arxiv.org/abs/1411.4038" rel="noopener" target="_blank" title=")._

At this point, regular classification DCNNs would output a dense (non-spatial) vector containing probabilities for each class label. Instead, we feed this compressed feature vector to a series of upsampling layers. These layers work on reconstructing the output of the first part of the network. **The goal is to increase the spatial resolution so the output vector has the same dimensions as the input**.

Usually, upsampling layers are based on _strided transpose convolutions_. **These functions go from deep and narrow layers to wider and shallower ones**. Here, we use transpose convolutions to increase the feature vector’s dimensions to the desired value.

In most papers, these two components of a segmentation network are called encoder and decoder. In short, the first “encodes” its information into a compressed vector used to represent its input. The second (the decoder) works on reconstructing this signal to the desired outcome.

There are many network implementations based on encoder-decoder architectures. FCNs, [SegNet](https://arxiv.org/abs/1511.00561), and [UNet](https://arxiv.org/abs/1505.04597) are some of the most popular ones. As a result, we have seen many successful segmentation models in a variety of fields.

### Model Architecture

Different from most encoder-decoder designs, Deeplab offers a different approach to semantic segmentation. It presents an architecture for controlling signal decimation and learning multi-scale contextual features.

![Image](https://cdn-media-1.freecodecamp.org/images/0*vPNf03aFqjnKUjt8.png)

_Image credits: [Rethinking Atrous Convolution for Semantic Image Segmentation](https://arxiv.org/abs/1706.05587)._

Deeplab uses an ImageNet pre-trained ResNet as its main feature extractor network. However, it proposes a new Residual block for multi-scale feature learning. Instead of regular convolutions, the last ResNet block uses atrous convolutions. Also, each convolution (within this new block) uses different dilation rates to capture multi-scale context.

Additionally, on top of this new block, it uses Atrous Spatial Pyramid Pooling (ASPP). ASPP uses dilated convolutions with different rates as an attempt at classifying regions of an arbitrary scale.

To understand the deeplab architecture, we need to focus on three components. (i) The ResNet architecture, (ii) atrous convolutions and (iii) Atrous Spatial Pyramid Pooling (ASPP). Let’s go over each one of them.

### ResNets

ResNet is a very popular DCNN that won the [ILSVRC 2015](http://image-net.org/challenges/LSVRC/2015/results) classification task. One of the main contributions of ResNets was to provide a framework to ease the training of deeper models.

In its original form, ResNets contain 4 computational blocks. Each block contains a different number of Residual Units. These units perform a series of convolutions in a special way. Also, each block is intercalated with max-pooling operations to reduce spatial dimensions.

The original paper presents two types of Residual Units. The _baseline_ and the _bottleneck_ blocks.

The baseline unit contains two _3x3_ convolutions with Batch Normalization(BN) and ReLU activations.

![Image](https://cdn-media-1.freecodecamp.org/images/0*EDoU4Xh6XPO_0xVy.png)
_ResNet building blocks. (left) baseline; (right) bottleneck unit. Image adapted from: [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385" rel="noopener" target="_blank" title=")._

The second, the bottleneck unit, consists of three stacked operations. A series of _1x1_, _3x3_ and _1x1_ convolutions substitute the previous design. The two _1x1_ operations are designed for reducing and restoring dimensions. This leaves the _3x3_ convolution, in the middle, to operate on a less dense feature vector. Also, BN is applied after each convolution and before ReLU non-linearity.

To help clarify, let’s denote these group of operations as a function _F_ of its input _x_ — _F(x)_.

After the non-linear transformations in _F(x)_, the unit combines the result of _F(x)_ with the original input _x_. This combination is done by adding the two functions. Merging the original input _x_ with the non-linear function _F(x)_ offers some advantages. It allows earlier layers to access the gradient signal from later layers. In other words, skipping the operations on _F(x)_ allows earlier layers to have access to a stronger gradient signal. As a result, this type of connectivity has been shown to ease the training of deeper networks.

Non-bottleneck units also show gain in accuracy as we increase model capacity. Yet, bottleneck residual units have some practical advantages. First, they perform more computations having almost the same number of parameters. Second, they also perform in a similar computational complexity as their counterparts.

In practice, _bottleneck_ units are more suitable for training deeper models because less training time and computational resources are needed.

For our implementation, we’ll use the **_full pre-activation Residual Unit_**. The only difference from the standard bottleneck unit lies in the order in which BN and ReLU activations are placed. For the full pre-activation, BN and ReLU (in this order) occur before convolutions.

![Image](https://cdn-media-1.freecodecamp.org/images/0*_gCQf3VOGmHXzSgY.png)
_Different ResNet building block architectures. (Left-most) the original ResNet block. (Right-most) the improved full pre-activation version. Image credits: [Identity Mappings in Deep Residual Networks](https://arxiv.org/abs/1603.05027" rel="noopener" target="_blank" title=")._

As shown in [Identity Mappings in Deep Residual Networks](https://arxiv.org/abs/1603.05027), the full pre-activation unit performs better than other variants.

_Note that the only difference among these designs is the order of BN and RELu in the convolution stack._

### Atrous Convolutions

Atrous (or dilated) convolutions are regular convolutions with a factor that allows us to expand the filter’s field of view.

Consider a _3x3_ convolution filter, for instance. When the dilation rate is equal to 1, it behaves like a standard convolution. But, if we set the dilation factor to 2, it has the effect of enlarging the convolution kernel.

In theory, it works like that. First, it expands (dilates) the convolution filter according to the dilation rate. Second, it fills the empty spaces with zeros — creating a sparse like filter. Finally, it performs regular convolution using the dilated filter.

![Image](https://cdn-media-1.freecodecamp.org/images/0*owO24EqfB_RNfT7V.png)
_Atrous convolutions with various rates._

As a consequence, a convolution with a dilated 2, _3x3_ filter would make it able to cover an area equivalent to a _5x5_. Yet, because it acts like a sparse filter, only the original _3x3_ cells will do computation and produce results. I said “act” because most frameworks don’t implement atrous convolutions using sparse filters (because of memory concerns).

In a similar way, setting the atrous factor to 3 allows a regular _3x3_ convolution to get signals from a _7x7_ corresponding area.

This effect allows us to control the resolution at which we compute feature responses. Also, atrous convolution adds larger context without increasing the number of parameters or the amount of computation.

Deeplab also shows that the dilation rate must be tuned according to the size of the feature maps. They studied the consequences of using large dilation rates over small feature maps.

![Image](https://cdn-media-1.freecodecamp.org/images/0*Oa8JJBiKNvMVZrkg.png)
_Side effects of setting larger dilation rates for smaller feature maps. For a 14x14 input image, a 3x3 filter with dilation rate of 15 makes the atrous convolution behaves like a regular 1x1 convolution._

When the dilation rate is very close to the feature map’s size, a regular _3x3_ atrous filter acts as a standard _1x1_ convolution.

Put in another way, the efficiency of atrous convolutions depends on a good choice of the dilation rate. Because of that, it is important to know the concept of **output stride** in neural networks.

**Output stride explains the ratio of the input image size to the output feature map size. It defines how much signal decimation the input vector suffers as it passes the network.**

For an output stride of 16, an image size of _224x224x3_ outputs a feature vector with 16 times smaller dimensions. That is _14x14_.

Besides, Deeplab also debates the effects of different output strides on segmentation models. **It argues that excessive signal decimation is harmful for dense prediction tasks**. In summary, models with smaller output stride — less signal decimation — tend to output finer segmentation results. Yet, training models with smaller output stride demand more training time.

Deeplab reports experiments with two configurations of output strides, 8 and 16. As expected, output stride = 8 was able to produce slightly better results. Here we choose output stride = 16 for practical reasons.

Also, because the atrous block doesn’t implement downsampling, ASPP also runs on the same feature response size. As a result, it allows learning features from multi-scale context using relatively large dilation rates.

The new Atrous Residual Block contains three residual units. In total, the 3 units have three _3x3_ convolutions. Motivated by _multigrid_ methods, Deeplab proposes different dilation rates for each convolution. In summary, _multigrid_ defines the dilation rates for each of the three convolutions.

In practice:

For the new block4, when output stride = 16 and **Multi Grid _= (1, 2, 4)_**, the three convolutions have **rates _= 2 · (1, 2, 4) = (2, 4, 8)_** respectively.

### Atrous Spatial Pyramid Pooling

For ASPP, the idea is to provide the model with multi-scale information. To do that, ASPP adds a series of atrous convolutions with different dilation rates. These rates are designed to capture long-range context. Also, to add global context information, ASPP incorporates image-level features via Global Average Pooling (GAP).

This version of ASPP contains 4 parallel operations. These are a _1x1_ convolution and three _3x3_ convolutions with _dilation rates =(6,12,18)_. As we mentioned, at this point, the feature maps’ nominal stride is equal to 16.

Based on the original implementation, we use crop sizes of _513x513_ for both training and testing. Thus, using an output stride of 16 means that ASPP receives feature vectors of size _32x32_.

Also, to add more global context information, ASPP incorporates image-level features. First, it applies GAP to the features output from the last atrous block. Second, the resulting features are fed to a _1x1_ convolution with 256 filters. Finally, the result is bilinearly upsampled to the correct dimensions.

In the end, the features, from all the branches, are combined into a single vector via concatenation. This output is then convoluted with another _1x1_ kernel — using BN and 256 filters.

After ASPP, we feed the result to another _1x1_ convolution — to produce the final segmentation logits.

### Implementation Details

Using the ResNet-50 as a feature extractor, this implementation of [Deeplab_v3](https://arxiv.org/pdf/1704.06857) employs the following network configuration:

* _output stride = 16_
* _Fixed multi-grid atrous convolution rates of (1,2,4) to the new Atrous Residual block (block 4)._
* _ASPP with rates (6,12,18) after the last Atrous Residual block._

Setting _output stride_ to 16 gives us the advantage of substantially faster training. Comparing to an output stride of 8, a stride of 16 makes the Atrous Residual block deal with feature maps that are four times smaller than those its counterpart deals with.

The multi-grid dilation rates are applied to the 3 convolutions inside the Atrous Residual block.

Finally, each of the three parallel _3x3_ convolutions in ASPP gets a different dilation rate — _(6,12,18)_.

Before computing the _cross-entropy error_, we resize the logits to the input’s size. As argued in the paper, it’s better to resize the logits than the ground-truth labels to keep resolution details.

Based on the original training procedures, we scale each image using a random factor from 0.5 to 2. Also, we apply random left-right flipping to the scaled images.

Finally, we crop patches of size _513x513_ for both training and testing.

To implement atrous convolutions with multi-grid in the block4 of the resnet, we just changed this piece in the _resnet_utils.py_ file.

### Training

To train the network, we decided to use the augmented Pascal VOC dataset provided by [Semantic contours from inverse detectors](http://ieeexplore.ieee.org/document/6126343/).

The training data is composed of 8,252 images. There are 5,623 from the training set and 2,299 from the validation set. To test the model using the original VOC 2012 val dataset, I removed 558 images from the 2,299 validation set. These 558 samples were also present on the official VOC validation set. Also, I added 330 images from the VOC 2012 train set that weren’t present either among the 5,623 nor the 2,299 sets. Finally, 10% of the 8,252 images (~825 samples) are held for validation, leaving the rest for training.

Note that this is different from the original paper: this implementation is not pre-trained in the COCO dataset. Also, some of the techniques described in the paper for training and evaluation were not implemented.

### Results

The model was able to achieve decent results on the PASCAL VOC validation set.

* Pixel accuracy: ~91%
* Mean Accuracy: ~82%
* Mean Intersection over Union (mIoU): ~74%
* Frequency weighed Intersection over Union: ~86%.

Bellow, you can check out some of the results in a variety of images from the PASCAL VOC validation set.

![Image](https://cdn-media-1.freecodecamp.org/images/0*0jdZ7ybvv9xVHRqs.png)

![Image](https://cdn-media-1.freecodecamp.org/images/0*X1arsScqOqXxjnCn.png)

### Conclusion

The field of Semantic Segmentation is no doubt one of the hottest ones in Computer Vision. Deeplab presents an alternative to classic encoder-decoder architectures. It advocates the usage of atrous convolutions for feature learning in multi-range contexts. Feel free to clone the repo and tune the model to achieve closer results to the original implementation. The complete code is [here](https://github.com/sthalles/deeplab_v3).

Hope you enjoyed reading!

_Originally published at [sthalles.github.io](https://sthalles.github.io/)._

![Image](https://cdn-media-1.freecodecamp.org/images/1*RzOHqzrJEIrB5ZY0nJAcvg.gif)

