---
title: How to use the VGG16 neural network and MobileNet with TensorFlow.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-10T18:26:09.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-the-vgg16-neural-network-and-mobilenet-with-tensorflow-js-ea4c76d0b8e0
coverImage: https://cdn-media-1.freecodecamp.org/images/0*UM0vZhOyk06pdmVT
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Deep Learning
  slug: deep-learning
- name: JavaScript
  slug: javascript
- name: technology
  slug: technology
- name: TensorFlow
  slug: tensorflow
seo_title: null
seo_desc: 'By ADL

  In this article, we will build a deep neural network that can recognize images with
  a high accuracy on the Client side using JavaScript & TensorFlow.js. I’ll explain
  the techniques used throughout the process as we go along.We will be using VG...'
---

By ADL

In this article, we will build a deep neural network that can recognize images with a high accuracy on the Client side using JavaScript & TensorFlow.js. I’ll explain the techniques used throughout the process as we go along.We will be using VGG16 and MobileNet for the sake of the demo.

If you need a quick refresher on TensorFlow.js, read [this](https://medium.freecodecamp.org/get-to-know-tensorflow-js-in-7-minutes-afcd0dfd3d2f) article.

Below is a screenshot of what the final web app will look like:

![Image](https://cdn-media-1.freecodecamp.org/images/1*v7x4TywHpUsEO8yQ4eu8xA.png)
_Final Web App_

To start off, we will create a folder **(VGG16_Keras_To_TensorflowJS)** with two sub folders: **localserver** and **static.** The **localserver** folder shall contain all the server **NodeJS** code, and the **static** folder will have all the CSS, HTML, and JavaScript code.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_TUuwX9jKmLx8O6NmHD7bA.png)
_Screenshot Showing the Folder structure_

> _Note : you can name the folders and file whatever you like._

### Server Configuration

We will manually create a **package.json** file with the below code:

```
{
```

```
"name": "tensorflowjs",
```

```
"version": "1.0.0",
```

```
"dependencies": {
```

```
"express": "latest"
```

```
}}
```

The **package.json** file keeps track of all the 3rd party packages which we will use in this project. After saving the **package.json** file, we will open the command line and in it we will navigate to the **localserver** folder. Then we will execute the following:

```
npm install
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*Mf-8wFjGxWba4k9wN_ArUw.png)
_Command Line for MacOS_

After doing so, NPM will execute and ensure that all the required packages mentioned in **package.json** are installed and are ready to use. You will observe a **node_modules** folder in the **localserver** folder.

![Image](https://cdn-media-1.freecodecamp.org/images/1*yhJuZPtxeGCp1xgZTtA89Q.png)

We will create a **server.js** file with the below code:

**server.js** contains the NodeJS code which allows the local server to be hosted which will run our WebApp.

### Client Configuration

Next we will create a **predict_with_tfjs.html**. Below is the code:

Once the HTML code is done, we will create a JavaScript file and call it **predict.js**. Below is the code:

### Model Configuration

Once the client and server side code is complete, we now need a DL/ML model to predict the images.We export the trained model (VGG16 and Mobile net) from Keras to TensorFlow.js. Save the output in folders called VGG and Mobile net, respectively, inside the static folder.

![Image](https://cdn-media-1.freecodecamp.org/images/1*VUIUWALn0J5V9vRZc8yerA.png)
_ScreenShot for Python_

### Defining the Classes

We will keep **imagenet_classes.js** inside the **static** folder. This file contains a list of all the ImageNet classes. _You can Download this file from [here](https://github.com/ADLsourceCode/TensorflowJS/blob/master/VGG16_Keras_To_TensorflowJS/static/imagenet_classes.js)._

### Testing the Code

After all the setup is done, we will open up the command line and navigate to the **localserver** folder and execute:

```
node server.js
```

We should see the below output:

![Image](https://cdn-media-1.freecodecamp.org/images/1*K7jbNlFYiRdnITT06kBFrg.png)

After the successful implementation of server side code, we can now go to the browser and open [**http://localhost:8080/predict_with_tfjs.html**](http://localhost:8080/predict_with_tfjs.html).  
If the client side code is bug free, the application will start. Then you can select a different model (VGG16 and mobile Net) from the selection box and do the prediction.

#### **GitHub Repository for the project:**

[**ADLsourceCode/TensorflowJS**](https://github.com/ADLsourceCode/TensorflowJS/tree/master/VGG16_Keras_To_TensorflowJS)  
[_GitHub is where people build software. More than 28 million people use GitHub to discover, fork, and contribute to over…_github.com](https://github.com/ADLsourceCode/TensorflowJS/tree/master/VGG16_Keras_To_TensorflowJS)

**You can watch the complete code explanation and implementation in the below video:**

> My Next Post will Cover **Financial Time Series analysis** using Tensorflow.js…[Stay Tuned](https://goo.gl/u72j6u).

**Best of Luck ! ?**

If you liked my article, **please click the ? below A**nd follow me on M**edium** & :

![Image](https://cdn-media-1.freecodecamp.org/images/1*z8B3R6kZjTkMKPv3MnUYxg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*-etmF1WRWkvWO6cSol7f1w.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*7DWddirTA0TDNoAL34xjag.png)

If you have any questions, please let me know in a comment below or [**Twitter**](https://twitter.com/I_AM_ADL). Subscribe to my YouTube Channel For More Tech videos : [**ADL**](https://goo.gl/u72j6u) .

