---
title: How to Detect Objects in Images Using the YOLOv8 Neural Network
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-04T18:17:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-detect-objects-in-images-using-yolov8
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/n2auv9i8405cgnxhru40.png
tags:
- name: Machine Learning
  slug: machine-learning
- name: neural networks
  slug: neural-networks
- name: Python
  slug: python
seo_title: null
seo_desc: 'By Andrey Germanov

  Object detection is a computer vision task that involves identifying and locating
  objects in images or videos. It is an important part of many applications, such
  as self-driving cars, robotics, and video surveillance.

  Over the year...'
---

By Andrey Germanov

Object detection is a computer vision task that involves identifying and locating objects in images or videos. It is an important part of many applications, such as self-driving cars, robotics, and video surveillance.

Over the years, many methods and algorithms have been developed to find objects in images and their positions. The best quality in performing these tasks comes from using convolutional neural networks. 

One of the most popular neural networks for this task is YOLO, created in 2015 by Joseph Redmon, Santosh Divvala, Ross Girshick, and Ali Farhadi in their famous research paper "You Only Look Once: Unified, Real-Time Object Detection".

Since that time, there have been quite a few versions of YOLO. Recent releases can do even more than object detection. The newest release is [YOLOv8](https://ultralytics.com/yolov8), which we are going to use in this tutorial.

Here, I will show you the main features of this network for object detection. First, we will use a pre-trained model to detect common object classes like cats and dogs. Then, I will show how to train your own model to detect specific object types that you select, and how to prepare the data for this process. Finally, we will create a web application to detect objects on images right in a web browser using the custom trained model.

To follow this tutorial, you should be familiar with [Python](https://python.org) and have a basic understanding of machine learning, neural networks, and their application in object detection. You can watch [this short video course](https://www.youtube.com/playlist?list=PL_IHmaMAvkVxdDOBRg2CbcJBq9SY7ZUvs) to familiarize yourself with all required machine learning theory.

Once you've refreshed the theory, let's get started with the practice! Here's what we'll cover:

1. [Problems YOLOv8 Can Solve](#heading-problems-yolov8-can-solve)
2. [How to Get Started with YOLOv8](#heading-how-to-get-started-with-yolov8)
3. [How to Prepare Data to Train the YOLOv8 Model](#heading-how-to-prepare-data-to-train-the-yolov8-model)
4. [How to Train the YOLOv8 Model](#heading-how-to-train-the-yolov8-model)
5. [How to Create an Object Detection Web Service](#heading-how-to-create-an-object-detection-web-service)
6. [How to Create the Frontend](#heading-how-to-create-the-frontend)
7. [How to Create the Backend](#heading-how-to-create-the-backend)
8. [Conclusion](#heading-conclusion)

<h1 id="problems_can_solve">Problems YOLOv8 Can Solve</h1>

You can use the YOLOv8 network to solve classification, object detection, and image segmentation problems. All these methods detect objects in images or in videos in different ways, as you can see in the image below:

![Image](https://www.freecodecamp.org/news/content/images/2023/04/compvision_tasks.png)
_Common computer vision problems - classification, detection, and segmentation_

The neural network that's created and trained for **image classification** determines a class of object on the image and returns its name and the probability of this prediction. 

For example, on the left image, it returned that this is a "cat" and that the confidence level of this prediction is 92% (0.92).

The neural network for **object detection**, in addition to the object type and probability, returns the coordinates of the object on the image: x, y, width and height, as shown on the second image. Object detection neural networks can also detect several objects in the image and their bounding boxes.

Finally, in addition to object types and bounding boxes, the neural network trained for **image segmentation** detects the shapes of the objects, as shown on the right image.

There are many different neural network architectures developed for these tasks, and for each of them you had to use a separate network in the past. Fortunately, things changed after the [YOLO](https://docs.ultralytics.com/) created. Now you can use a single platform for all these problems.

In this article, we will explore **object detection** using YOLOv8. I will guide you through how to create a web application that will detect traffic lights and road signs in images. In later articles I will cover other features, including image segmentation.

In the next sections, we will go through all steps required to create an object detector. By the end of this tutorial, you will have a complete AI powered web application.

<h1 id="get_started">How to Get Started with YOLOv8</h1>

Technically speaking, [YOLOv8](https://ultralytics.com/) is a group of convolutional neural network models, created and trained using the [PyTorch](https://pytorch.org/) framework.

In addition, the YOLOv8 package provides a single Python API to work with all of them using the same methods. That is why, to use it, you need an environment to run Python code. I highly recommend using [Jupyter Notebook](https://jupyter.org/).

After making sure that you have Python and Jupyter installed on your computer, run the notebook and install the YOLOv8 package in it by running the following command:

```python
!pip install ultralytics
```

The `ultralytics` package has the `YOLO` class, used to create neural network models.

To get access to it, import it to your Python code:

```python
from ultralytics import YOLO
```

Now everything is ready to create the neural network model:

```python
model = YOLO("yolov8m.pt")
```

As I mentioned before, YOLOv8 is a group of neural network models. These models were created and trained using PyTorch and exported to files with the `.pt` extension. 

There are three types of models and 5 models of different sizes for each type:

<table>
<tbody>
<tr>
<td>
<strong>Classification</strong>
</td>
<td>
<strong>Detection</strong>
</td>
<td>
<strong>Segmentation</strong>
</td>
<td>
<strong>Kind</strong>
</td>
</tr>
<tr>
<td>
yolov8n-cls.pt
</td>
<td>
yolov8n.pt
</td>
<td>
yolov8n-seg.pt
</td>
<td>Nano</td>
</tr>
<tr>
<td>
yolov8s-cls.pt
</td>
<td>
yolov8s.pt
</td>
<td>
yolov8s-seg.pt
</td>
<td>Small</td>
</tr>
<tr>
<td>
yolov8m-cls.pt
</td>
<td>
yolov8m.pt
</td>
<td>
yolov8m-seg.pt
</td>
<td>Medium</td>
</tr>
<tr>
<td>
yolov8l-cls.pt
</td>
<td>
yolov8l.pt
</td>
<td>
yolov8l-seg.pt
</td>
<td>Large</td>
</tr>
<tr>
<td>
yolov8x-cls.pt
</td>
<td>
yolov8x.pt
</td>
<td>
yolov8x-seg.pt
</td>
<td>Huge</td>
</tr>
</tbody>
</table>

The bigger the model you choose, the better the prediction quality you can achieve, but the slower it will work. 

In this tutorial I will cover object detection – which is why, in the previous code snippet, I selected the "yolov8m.pt", which is a middle-sized model for object detection.

When you run this code for the first time, it will download the `yolov8m.pt` file from the Ultralytics server to the current folder. Then it will construct the `model` object. Now you can train this `model`, detect objects, and export it to use in production. For all these tasks, there are convenient methods:

* [train({path to dataset descriptor file})](https://docs.ultralytics.com/modes/train/) – used to train the model on the images dataset.
* [predict({image})](https://docs.ultralytics.com/modes/predict) – used to make a prediction for a specified image, for example to detect bounding boxes of all objects that the model can find in the image.
* [export({format})](https://docs.ultralytics.com/modes/export/) – used to export the model from the default PyTorch format to a specified format.

All YOLOv8 models for object detection ship already pre-trained on the [COCO dataset](https://cocodataset.org/), which is a huge collection of images of 80 different types. So, if you do not have specific needs, then you can just run it as is, without additional training. 

For example, you can download this image as "cat_dog.jpg":

![Image](https://www.freecodecamp.org/news/content/images/2023/04/cat_dog.jpg)
_A sample image with cat and dog_

and run `predict` to detect all objects in it:

```python
results = model.predict("cat_dog.jpg")
```

The `predict` method accepts many different input types, including a path to a single image, an array of paths to images, the Image object of the well-known [PIL](https://pillow.readthedocs.io/en/stable/) Python library, and [others](https://docs.ultralytics.com/modes/predict/#sources).

After running the input through the model, it returns an array of results for each input image. As we provided only a single image, it returns an array with a single item that you can extract like this:

```python
result = results[0]
```

The [result](https://docs.ultralytics.com/modes/predict/#working-with-results) contains detected objects and convenient properties to work with them. The most important one is the `boxes` array with information about detected bounding boxes on the image. You can determine how many objects it detected by running the `len` function:

```python
len(result.boxes)
```

When I ran this, I got "2", which means that there are two boxes detected: one for the dog and one for the cat.

Then you can analyze each box either in a loop or manually. Let's get the first one:

```python
box = result.boxes[0]
```

The [box](https://docs.ultralytics.com/modes/predict/#boxes) object contains the properties of the bounding box, including:

* `xyxy` – the coordinates of the box as an array [x1,y1,x2,y2]
* `cls` – the ID of object type
* `conf` – the confidence level of the model about this object. If it's very low, like < 0.5, then you can just ignore the box.

Let's print information about the detected box:

```python
print("Object type:", box.cls)
print("Coordinates:", box.xyxy)
print("Probability:", box.conf)
```

For the first box, you will receive the following information:

```bash
Object type: tensor([16.])
Coordinates: tensor([[261.1901,  94.3429, 460.5649, 312.9910]])
Probability: tensor([0.9528])
```

As I explained above, YOLOv8 contains PyTorch models. The outputs from the PyTorch models are encoded as an array of PyTorch [Tensor](https://pytorch.org/docs/stable/tensors.html) objects, so you need to extract the first item from each of these arrays:

```python
print("Object type:",box.cls[0])
print("Coordinates:",box.xyxy[0])
print("Probability:",box.conf[0])
```

```bash
Object type: tensor(16.)
Coordinates: tensor([261.1901,  94.3429, 460.5649, 312.9910])
Probability: tensor(0.9528)
```

Now you see the data as `Tensor` objects. To unpack actual values from Tensor, you need to use the `.tolist()` method for tensors with array inside, as well as the `.item()` method for tensors with scalar values. 

Let's extract the data to the appropriate variables:

```python
cords = box.xyxy[0].tolist()
class_id = box.cls[0].item()
conf = box.conf[0].item()
print("Object type:", class_id)
print("Coordinates:", cords)
print("Probability:", conf)
```

```bash
Object type: 16.0
Coordinates: [261.1900634765625, 94.3428955078125, 460.5649108886719, 312.9909973144531]
Probability: 0.9528293609619141
```

Now you see the actual data. The coordinates can be rounded, and the probability also can be rounded to two digits after the dot.

The object type is `16` here. What does this mean? Let's talk more about that. 

All objects that the neural network can detect have numeric IDs. In case of a YOLOv8 pretrained model, there are 80 object types with IDs from 0 to 79. The COCO object classes are well known and you can easily google them on the Internet. In addition, the YOLOv8 result object contains the convenient `names` property to get these classes:

```python
print(result.names)
```

```bash
{0: 'person',
 1: 'bicycle',
 2: 'car',
 3: 'motorcycle',
 4: 'airplane',
 5: 'bus',
 6: 'train',
 7: 'truck',
 8: 'boat',
 9: 'traffic light',
 10: 'fire hydrant',
 11: 'stop sign',
 12: 'parking meter',
 13: 'bench',
 14: 'bird',
 15: 'cat',
 16: 'dog',
 17: 'horse',
 18: 'sheep',
 19: 'cow',
 20: 'elephant',
 21: 'bear',
 22: 'zebra',
 23: 'giraffe',
 24: 'backpack',
 25: 'umbrella',
 26: 'handbag',
 27: 'tie',
 28: 'suitcase',
 29: 'frisbee',
 30: 'skis',
 31: 'snowboard',
 32: 'sports ball',
 33: 'kite',
 34: 'baseball bat',
 35: 'baseball glove',
 36: 'skateboard',
 37: 'surfboard',
 38: 'tennis racket',
 39: 'bottle',
 40: 'wine glass',
 41: 'cup',
 42: 'fork',
 43: 'knife',
 44: 'spoon',
 45: 'bowl',
 46: 'banana',
 47: 'apple',
 48: 'sandwich',
 49: 'orange',
 50: 'broccoli',
 51: 'carrot',
 52: 'hot dog',
 53: 'pizza',
 54: 'donut',
 55: 'cake',
 56: 'chair',
 57: 'couch',
 58: 'potted plant',
 59: 'bed',
 60: 'dining table',
 61: 'toilet',
 62: 'tv',
 63: 'laptop',
 64: 'mouse',
 65: 'remote',
 66: 'keyboard',
 67: 'cell phone',
 68: 'microwave',
 69: 'oven',
 70: 'toaster',
 71: 'sink',
 72: 'refrigerator',
 73: 'book',
 74: 'clock',
 75: 'vase',
 76: 'scissors',
 77: 'teddy bear',
 78: 'hair drier',
 79: 'toothbrush'}
```

This dictionary has everything that this model can detect. Now you can find that `16` is "dog", so this bounding box is the bounding box for detected DOG. 

Let's modify the output to show results in a more representative way:

```python
cords = box.xyxy[0].tolist()
cords = [round(x) for x in cords]
class_id = result.names[box.cls[0].item()]
conf = round(box.conf[0].item(), 2)
print("Object type:", class_id)
print("Coordinates:", cords)
print("Probability:", conf)
```

In this code I rounded all coordinates using Python [list comprehension](https://www.freecodecamp.org/news/list-comprehension-in-python-with-code-examples/). Then I got the name of the detected object class by ID using the `result.names` dictionary. I also rounded the probability. You should get the following output:

```bash
Object type: dog
Coordinates: [261, 94, 461, 313]
Probability: 0.95
```

This data is good enough to show in the user interface. Let's now write some code to get this information for all detected boxes in a loop:

```python
for box in result.boxes:
  class_id = result.names[box.cls[0].item()]
  cords = box.xyxy[0].tolist()
  cords = [round(x) for x in cords]
  conf = round(box.conf[0].item(), 2)
  print("Object type:", class_id)
  print("Coordinates:", cords)
  print("Probability:", conf)
  print("---")
```

This code will do the same for each box and will output the following:

```python
Object type: dog
Coordinates: [261, 94, 461, 313]
Probability: 0.95
---
Object type: cat
Coordinates: [140, 170, 256, 316]
Probability: 0.92
---
```

This way you can run object detection for other images and see everything that a COCO-trained model can detect in them.

This video shows the whole coding session of this section in Jupyter Notebook, assuming you have it [installed](https://jupyter.org/install).

%[https://youtu.be/8Q87QYlonRU]

Using models that are pre-trained on well-known objects is ok to start. But in practice, you may need a solution to detect specific objects for a concrete business problem.

For example, someone may need to detect specific products on supermarket shelves or discover brain tumors on x-rays. It's highly likely that this information is not available in public datasets, and there are no free models that know about everything.

So, you have to teach your own model to detect these types of objects. To do that, you need to create a database of annotated images for your problem and train the model on these images.

<h1 id="data">How to Prepare Data to Train the YOLOv8 Model</h1>

To train the model, you need to prepare annotated images and split them into training and validation datasets. 

You'll use the training set to teach the model and the validation set to test the results of the study and measure the quality of the trained model. You can put 80% of the images in the training set and 20% in the validation set.

These are the steps that you need to follow to create each of the datasets:

1. Decide on and encode classes of objects you want to teach your model to detect. For example, if you want to detect only cats and dogs, then you can state that "0" is cat and "1" is dog.
2. Create a folder for your dataset and two subfolders in it: "images" and "labels".
3. Add the images to the "images" subfolder. The more images you collect, the better for training.
4. For each image, create an annotation text file in the "labels" subfolder. Annotation text files should have the same names as image files and the ".txt" extensions. In the annotation files you should add records about each object that exist on the appropriate image in the following format:

```
{object_class_id} {x_center} {y_center} {width} {height}
```

![Image](https://www.freecodecamp.org/news/content/images/2023/04/bounding_box.png)
_Bounding box parameters_

This is the most time-consuming manual work in the machine learning process: to measure bounding boxes for all objects and add them to annotation files. 

You should also normalize the coordinates to fit in a range from 0 to 1. To calculate them, you need to use the following formulas:

* x_center = (box_x_left+box_x_width/2)/image_width
* y_center = (box_y_top+box_height/2)/image_height
* width = box_width/image_width
* height = box_height/image_height

For example, if you want to add the "cat_dog.jpg" image that we used before to the dataset, you need to copy it to the "images" folder and then measure and collect the following data about the image, and it's bounding boxes:

**Image:**

image_width = 612  
image_height = 415

**Objects:**

<table>
<tbody>
<tr>
<td><strong>Dog</strong></td>
<td><strong>Cat</strong></td>
</tr>
<tr>
<td>
box_x_left=261<br/> 
box_x_top=94<br/>
box_width=200<br/>
box_height=219
</td>
<td>
box_x_left=140<br/>
box_x_top=170<br/>
box_width=116<br/>
box_height=146
</td>
</tr>
</tbody>
</table>

Then, create the "cat_dog.txt" file in the "labels" folder and, using the formulas above, calculate the coordinates:

Dog (class id=1):

x_center = (261+200/2)/612 = 0.589869281  
y_center = (94+219/2)/415 = 0.490361446  
width = 200/612 = 0.326797386  
height = 219/415 = 0.527710843

Cat (class id=0)

x_center = (140+116/2)/612 = 0.323529412  
y_center = (170+146/2)/415 = 0.585542169  
width = 116/612 = 0.189542484  
height = 146/415 = 0.351807229

and add the following lines to the file:

```
1 0.589869281 0.490361446 0.326797386 0.527710843
0 0.323529412 0.585542169 0.189542484 0.351807229
```

The first line contains a bounding box for the dog (class id=1). The second line contains a bounding box for the cat (class id=0). Of course, you can have the image with many dogs and many cats at the same time, and you can add bounding boxes for all of them.

After adding and annotating all images, the dataset is ready. You need to create two datasets and place them in different folders. The final folder structure can look like this:

![Image](https://www.freecodecamp.org/news/content/images/2023/04/dataset_structure.png)
_Dataset structure_

As you can see, the training dataset is located in the "train" folder and the validation dataset is located in the "val" folder.

Finally, you need to create a dataset descriptor YAML-file that points to the created datasets and describes the object classes in them. This is a sample of this file for the data created above:

```yaml
train: ../train/images
val: ../val/images

nc: 2
names: ['cat','dog']
```

In the first two lines, you need to specify paths to the images of the training and the validation datasets. The paths can be either relative to the current folder or absolute. 

Then, the `nc` line specifies the **n**umber of **c**lasses that exist in these datasets, and `names` is an array of class names in correct order. 

Indexes of these items are numbers that you used when annotating the images, and these indexes will be returned by the model when it detects objects using the `predict` method. So, if you used "0" for cats, then it should be the first item in the `names` array.

This YAML file should be passed to the `train` method of the model to start the training process.

To make the image annotation process easier, there are a lot of programs you can use to visually annotate images for machine learning. You can search for something like "software to annotate images for machine learning" to get a list of these programs. 

There are also many online tools that can do all this work, like [Roboflow Annotate](https://roboflow.com/annotate). Using this service, you just need to upload your images, draw bounding boxes on them, and set classes for each bounding box. Then, the tool will automatically create annotation files, split your data to train and validation datasets, and create a YAML descriptor file. Then you can export and download the annotated data as a ZIP file.

In the below video, I show you how to use Roboflow to create the "cats and dogs" micro-dataset.

%[https://youtu.be/sLZRfzaRBwg]

For real life problems, that database should be much bigger. To train a good model, you should have hundreds or thousands of annotated images.

Also, when preparing the images database, try to make it balanced. It should have an equal number of objects of each class, that is an equal number of dogs and cats in this example. Otherwise, the model trained on it may predict one class better than another.

After the data is ready, copy it to the folder with your Python code that you will use for training and return back to your Jupyter Notebook to start the training process.

<h1 id="train">How to Train the YOLOv8 Model</h1>

After the data is ready, you need to pass it through the model. To make it more interesting, we will not use this small "cats and dogs" dataset. We will use another custom dataset for training that contains [traffic lights and road signs](https://universe.roboflow.com/roboflow-100/road-signs-6ih4y). This is a free dataset that I got from the Roboflow Universe. Press "Download Dataset" and select "YOLOv8" as the format.

If it's not available on Roboflow when you read this, then you can get it from [my Google Drive](https://drive.google.com/file/d/1PNktsghBqIJVgxa-34FqO3yODNJbH3B0/view?usp=sharing). You can use this dataset to teach YOLOv8 to detect different objects on roads, like you can see in the next screenshot.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/traffic_lights.png)
_Traffic lights detection demo_

You can open the downloaded zip file and ensure that it's already annotated and structured using the rules described above. You can find the dataset descriptor file `data.yaml` in the archive as well.

If you downloaded the archive from Roboflow, it will contain the additional "test" dataset, which is not used by the training process. You can use the images from it for additional testing on your own after training.

Extract the archive to the folder with your Python code and execute the `train` method to start a training loop:

```python
model.train(data="data.yaml", epochs=30)
```

The `data` is the only required option. You have to pass the YAML descriptor file to it. The `epochs` option specifies the number of training cycles (100 by default). There are other [options](https://docs.ultralytics.com/modes/train/#arguments) that can affect the process and quality of the trained model.

Each training cycle consists of two phases: a training phase and a validation phase.

During the training phase, the `train` method does the following:

* Extracts the random batch of images from the training dataset (the number of images in the batch can be specified using the `batch` option).
* Passes these images through the model and receives the resulting bounding boxes of all detected objects and their classes.
* Passes the result to the loss function that's used to compare the received output with correct result from annotation files for these images. The loss function calculates the amount of error.
* The result of the loss function is passed to the `optimizer` to adjust the model weights based on the amount of error in the correct direction. This reduces the errors in the next cycle. By default, the [SGD (Stochastic Gradient Descent)](https://towardsdatascience.com/stochastic-gradient-descent-clearly-explained-53d239905d31) optimizer is used, but you can try others, like [Adam](https://www.linkedin.com/pulse/understanding-adam-optimizer-gradient-descent-evan-dunbar/), to see the difference.

During the validation phase, `train` does the following:

* Extracts the images from the validation dataset.
* Passes them through the model and receives the detected bounding boxes for these images.
* Compares the received result with true values for these images from annotation text files.
* Calculates the precision of the model based on the difference between actual and expected results.

The progress and results of each phase for each epoch are displayed on the screen. This way you can see how the model learns and improves from epoch to epoch.

When you run the `train` code, you will see a similar output to the following during the training loop:

![Image](https://www.freecodecamp.org/news/content/images/2023/04/training.png)
_Training process_

For each epoch it shows a summary for both the training and validation phases: lines 1 and 2 show results of the training phase and lines 3 and 4 show the results of the validation phase for each epoch.

The training phase includes a calculation of the amount of error in a loss function, so the most valuable metrics here are `box_loss` and `cls_loss`.

* `box_loss` shows the amount of error in detected bounding boxes.
* `cls_loss` shows the amount of error in detected object classes.

Why is the loss split to different metrics? Because the model might correctly detect the bounding box coordinates around the object, but incorrectly detect the object class in this box. For example, in my practice, it detected the dog as a horse, but the dimensions of the object were detected correctly.

If the model really learns something from the data, then you should see that these values decrease from epoch to epoch. In a previous screenshot the `box_loss` decreased: 0.7751, 0.7473, 0.742 and the `cls_loss` decreased too: 0.702, 0.6422, 0.6211.

In the validation phase, it calculates the quality of the model after training using the images from the validation dataset. 

The most valuable quality metric is mAP50-95, which is [Mean Average Precision](https://www.v7labs.com/blog/mean-average-precision). If the model learns and improves, the precision should grow from epoch to epoch. In a previous screenshot you can see that it slowly grew: 0.788, 0.788, 0.791.

If after the last epoch you did not get acceptable precision, you can increase the number of epochs and run the training again. Also, you can tune other parameters like `batch`, `lr0`, `lrf` or change the `optimizer` you're using. There are no clear rules on what to do here, but there are a lot of recommendations.

The topic of tuning the parameters of the training process goes beyond the scope of article. I think it's possible to write a book about this and many of them already exist. You can easily find them on the Internet. But in a few words, most of them say that you need to experiment and try all possible options and compare results.

In addition to the metrics that are shown during the training process, it writes a lot of statistics on disk. When training starts, it creates the `runs/detect/train` subfolder in the current folder and after each epoch it logs different log files to it.

It also exports the trained model after each epoch to the `/runs/detect/train/weights/last.pt` file and the model with the highest precision to the `/runs/detect/train/weights/best.pt` file. So, after training is finished, you can get the `best.pt` file to use in production.

You can watch this video to learn more about how the training process works. I used [Google Colab](https://colab.research.google.com/) which is a cloud version of Jupyter Notebook to get access to hardware with more powerful GPU to speed up the training process. 

The video shows how to train the model on 5 epochs and download the final `best.pt` model. In real world problems, you need to run much more epochs and be prepared to wait hours or maybe days until training finishes.

%[https://youtu.be/HZobbSjbAUc]

After it's finished, it's time to run the trained model in production. In the next section, we will create a web service to detect objects in images online in a web browser.

<h1 id="detect">How to Create an Object Detection Web Service
</h1>

At this point, we're finished experimenting with the model in the Jupyter Notebook. You'll need to write the next batch of code as a separate project, using any Python IDE like [VS Code](https://code.visualstudio.com/) or [PyCharm](https://www.jetbrains.com/pycharm/).

The web service that we are going to create will have a web page with a file input field and an HTML5 canvas element. 

When the user selects an image file using the input field, the interface will send it to the backend. Then, the backend will pass the image through the model that we created and trained and return the array of detected bounding boxes to the web page. 

When it receives this, the frontend will draw the image on the canvas element and the detected bounding boxes on top of it. 

The service will look and work as demonstrated on this video:

%[https://youtu.be/iOIfm_5QIiw]

In the video, I used the model trained on 30 epochs, and it still does not detect some traffic lights. You can try to train it more to get better results. But the best way to improve the quality of a machine learning model is by adding more and more data. 

So, as an additional exercise, you can import the dataset folder to Roboflow, add and annotate more images to it, and then use the updated data to continue training the model.

<h2 id="frontend">How to Create the Frontend</h2>

To start with, create a folder for a new Python project and an `index.html` file in it for the frontend web page. Here are the contents of this file:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>YOLOv8 Object Detection</title>
    <style>
        canvas {
            display:block;
            border: 1px solid black;
            margin-top:10px;
        }
    </style>
</head>
<body>
    <input id="uploadInput" type="file"/>
    <canvas></canvas>
    <script>
       /**
       * "Upload" button onClick handler: uploads selected 
       * image file to backend, receives an array of
       * detected objects and draws them on top of image
       */
       const input = document.getElementById("uploadInput");
       input.addEventListener("change",async(event) => {
           const file = event.target.files[0];
           const data = new FormData();
           data.append("image_file",file,"image_file");
           const response = await fetch("/detect",{
               method:"post",
               body:data
           });
           const boxes = await response.json();
           draw_image_and_boxes(file,boxes);
       })

       /**
       * Function draws the image from provided file
       * and bounding boxes of detected objects on
       * top of the image
       * @param file Uploaded file object
       * @param boxes Array of bounding boxes in format
         [[x1,y1,x2,y2,object_type,probability],...]
       */
       function draw_image_and_boxes(file,boxes) {
          const img = new Image()
          img.src = URL.createObjectURL(file);
          img.onload = () => {
              const canvas = document.querySelector("canvas");
              canvas.width = img.width;
              canvas.height = img.height;
              const ctx = canvas.getContext("2d");
              ctx.drawImage(img,0,0);
              ctx.strokeStyle = "#00FF00";
              ctx.lineWidth = 3;
              ctx.font = "18px serif";
              boxes.forEach(([x1,y1,x2,y2,label]) => {
                  ctx.strokeRect(x1,y1,x2-x1,y2-y1);
                  ctx.fillStyle = "#00ff00";
                  const width = ctx.measureText(label).width;
                  ctx.fillRect(x1,y1,width+10,25);
                  ctx.fillStyle = "#000000";
                  ctx.fillText(label,x1,y1+18);
              });
          }
       }
  </script>  
</body>
</html>
```

The HTML part is very tiny and consists only of the file input field with "uploadInput" ID and the canvas element below it. 

Then, in the JavaScript part, the "onChange" we define the event handler for the input field. When the user selects an image file, the handler uses `fetch` to make a POST request to the `/detect` backend endpoint (which we will create later) and sends this image file to it.

The backend should detect objects on this image and return a response with a `boxes` array as JSON. This response then gets decoded and passed to the `draw_image_and_boxes` function along with an image file itself.

The `draw_image_and_boxes` function loads the image from file. As soon as it's loaded, it draws it on the canvas. Then, it draws each bounding box with a class label on top of the canvas with the image.

So, now let's create the backend with a `/detect` endpoint for it.

<h2 id="backend">How to Create the Backend</h2>

We'll create the backend using [Flask](https://flask.palletsprojects.com/en/2.2.x/). Flask has its own internal web server, but according to many Flask developers, it's not reliable enough for productio. So we will use the [Waitress](https://flask.palletsprojects.com/en/2.2.x/deploying/waitress/) web server and run our Flask app in it.

Also, we will use the [Pillow](https://pillow.readthedocs.io/en/stable/) library to read an uploaded binary files as images. Make sure you have all these packages installed on your system before continuing:

```bash
pip3 install flask
pip3 install waitress
pip3 install pillow
```

The backend will be in a single file. Let's name it `object_detector.py`:

```python
from ultralytics import YOLO
from flask import request, Response, Flask
from waitress import serve
from PIL import Image
import json

app = Flask(__name__)

@app.route("/")
def root():
    """
    Site main page handler function.
    :return: Content of index.html file
    """
    with open("index.html") as file:
        return file.read()


@app.route("/detect", methods=["POST"])
def detect():
    """
        Handler of /detect POST endpoint
        Receives uploaded file with a name "image_file", 
        passes it through YOLOv8 object detection 
        network and returns an array of bounding boxes.
        :return: a JSON array of objects bounding 
        boxes in format 
        [[x1,y1,x2,y2,object_type,probability],..]
    """
    buf = request.files["image_file"]
    boxes = detect_objects_on_image(Image.open(buf.stream))
    return Response(
      json.dumps(boxes),  
      mimetype='application/json'
    )


def detect_objects_on_image(buf):
    """
    Function receives an image,
    passes it through YOLOv8 neural network
    and returns an array of detected objects
    and their bounding boxes
    :param buf: Input image file stream
    :return: Array of bounding boxes in format 
    [[x1,y1,x2,y2,object_type,probability],..]
    """
    model = YOLO("best.pt")
    results = model.predict(buf)
    result = results[0]
    output = []
    for box in result.boxes:
        x1, y1, x2, y2 = [
          round(x) for x in box.xyxy[0].tolist()
        ]
        class_id = box.cls[0].item()
        prob = round(box.conf[0].item(), 2)
        output.append([
          x1, y1, x2, y2, result.names[class_id], prob
        ])
    return output

serve(app, host='0.0.0.0', port=8080)
```

First, we import the required libraries:

* [ultralytics](https://github.com/ultralytics/ultralytics) for the YOLOv8 model.
* [flask](https://flask.palletsprojects.com/en/2.2.x/) to create a `Flask` web application, to receive `requests` from the frontend and send `responses` back to it.
* [waitress](https://flask.palletsprojects.com/en/2.2.x/deploying/waitress/) to run a web server and `serve` the Flask web `app` in it.
* [PIL](https://pillow.readthedocs.io/en/stable/) to load an uploaded file as an `Image` object, that required for YOLOv8.
* [json](https://docs.python.org/3/library/json.html) to convert the array of bounding boxes to JSON before returning it to the frontend.

Then, we defined two routes:

* `/` that serves as a root of web service. It just returns the content of the "index.html" file.
* `/detect` that responds to an image upload request from the frontend. It converts the RAW file to the Pillow Image object, then passes this image to the `detect_objects_on_image` function.

The `detect_objects_on_image` function creates a model object based on the `best.pt` model that we trained in the previous section. Make sure that this file exists in the folder where you write the code.

Then it calls the `predict` method for the image. `predict` returns the detected bounding boxes. 

Next, for each box it extracts the coordinates, class name, and probability in the same way as we did in the beginning of the tutorial. It adds this info to the output array. 

Finally, the function returns the array of detected object coordinates and their classes.

After this, the array gets encoded to JSON and is returned to the frontend.

The last line of code starts the web server on port 8080 that serves the `app` Flask application.

To run the service, execute the following command:

```bash
python3 object_detector.py
```

If everything is working properly, you can open `http:///localhost:8080` in a web browser. It should show the `index.html` page. When you select any image file, it will process it and display bounding boxes around all detected objects (or just display the image if nothing is detected on it).

The web service we just created is universal. You can use it with any YOLOv8 model. At the moment, it detects traffic lights and road signs using the `best.pt` model we created. But you can change it to use another model, like the `yolov8m.pt` model we used earlier to detect cats, dogs, and all other object classes that pretrained YOLOv8 models can detect.

<h1 id="conclusion">Conclusion</h1>

In this tutorial, I guided you thought a process of creating an AI powered web application that uses the YOLOv8, a state-of-the-art convolutional neural network for object detection. 

I showed you how to create models using the pre-trained models and prepare the data to train custom models. And finally we created a web application with a frontend and backend that uses the custom trained YOLOv8 model to detect traffic lights and road signs.

You can find a source code of this app in [this GitHub repository](https://github.com/AndreyGermanov/yolov8_pytorch_python). 

For all these tasks, we used the Ultralytics high level APIs that come with the YOLOv8 package by default. These APIs are based on the PyTorch framework, which was used to create the bigger part of today's neural networks. 

It's quite convenient on the one hand, but dependence on these high level APIs has a negative effect as well. If you need to run this web app in production, you should install all these environments there, including Python, PyTorch and the other dependencies. 

To run this on a clean new server, you'll need to download and install more than 1 GB of third party libraries! This is definitely not the best way to go. 

Also, what if you do not have Python in your production environment? What if all your other code is written in another programming language, and you do not plan to use Python? Or what if you want to run the model on a mobile phone with Android or iOS?

All this is to say that using Ultralytics packages is great for experimenting, training, and preparing the models for production. But in production itself, you have to load and use the model directly and not use those high-level APIs. 

To do this, you need to understand how the YOLOv8 neural network works under the hood and write more code to provide input to the model and to process the output from it. This will make your apps faster and less resource-intense. You will not need to have PyTorch installed to run your object detection model. 

Also, you will be able to run your models even without Python, using many other programming languages, including Julia, C++, Go, Node.js on backend, or even without backend at all. You can run the YOLOv8 models right in a browser, using only JavaScript on frontend. 

Want to know how? This will be the topic of my next article about YOLOv8.

You can find me on [LinkedIn](https://www.linkedin.com/in/andrey-germanov-dev/), [Twitter](https://twitter.com/GermanovDev), and [Facebook](https://www.facebook.com/AndreyGermanovDev) to know first about new articles like this one and other software development news.

Have a fun coding and never stop learning!

