---
title: How to Convert a Keras SavedModel into a Browser-based Web App
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-05-18T16:36:22.000Z'
originalURL: https://freecodecamp.org/news/convert-keras-savedmodel-into-browser-based-webapp
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/beach-photo.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: keras
  slug: keras
- name: Machine Learning
  slug: machine-learning
seo_title: null
seo_desc: "By Suchandra Datta\nIf you're a Python developer who works with Keras SavedModels,\
  \ this article is for you. \nPerhaps you're not sure how to use SavedModels to leverage\
  \ the power of machine learning in browser-based web apps. But don't worry – we'll\
  \ co..."
---

By Suchandra Datta

If you're a Python developer who works with Keras SavedModels, this article is for you. 

Perhaps you're not sure how to use SavedModels to leverage the power of machine learning in browser-based web apps. But don't worry – we'll cover all the basic steps you need to get started. 

Along with that, we'll go over some important concepts that'll help make it easier for you to transition to JavaScript from Python.

Before we dive into the process, let's address some questions that are likely to pop into your mind at this point.

## What is a Keras SavedModel?

A Keras model is made up of the network architecture, model weights, and an optimizer for your loss function. 

The default format for saving models on disk is the SavedModel format. This format allows us to save models with custom objects with minimum hassle. 

SavedModel stores the optimizer, loss, and network architecture in the saved_model.pb file while the weights are stored in the variables directory. 

For more detailed information on the SavedModel format, check out the official docs [here](https://www.tensorflow.org/guide/keras/save_and_serialize).

## How do I train a Keras SavedModel if I don't have a GPU?

Most machine learning enthusiasts without access to GPU facilities start off with model development on Google Colaboratory. 

I've been an avid admirer of Google Colab and its features ever since I first became interested in the field of machine learning. It offers a Jupyter Notebook environment with free access to GPU's with a maximum training time of 12 hours. 

If you've got any questions regarding Google Colaboratory, head over to their FAQ section linked [here](https://research.google.com/colaboratory/faq.html#:~:text=How%20long%20can%20notebooks%20run,or%20based%20on%20your%20usage.). 

## Why would I want to convert a SavedModel into a web app?

Web-based products are everywhere, and they're generally pretty easy to use. You're probably reading this article from a browser right now, either from your phone, desktop, or laptop. 

Machine learning models, at the end of the day, are meant to be used in the real-world not kept inside a glass box. So what better way to bring your model to users than through a web-based medium? 

On top of that, browser-based apps don't require any installation overhead and can be accessed uniformly from multiple devices.

## Okay then, let's get started

I had built a simple emotion detection CNN model that could predict 7 emotions (happy, sad, neutral, angry, surprise, fear and disgust) using Python and the Keras API. 

Trying to convert it into a format suitable for the web without prior experience proved to be a bit difficult. The entire process, which I'll describe next, is thanks to the wonderful documentation of [Tensorflow.js](https://www.tensorflow.org/js/tutorials/setup), the [MDN Web docs](https://developer.mozilla.org/en-US/docs/Web/API/File/Using_files_from_web_applications), and [Firebase hosting documentation](https://firebase.google.com/docs/hosting).

Using these resources, I was able to narrow down the process to the following steps:

* Convert Keras SavedModel to the Tensorflow.js Layers Format
* Load the model via JavaScript and Promises
* Access an image uploaded by a user
* Preprocess the uploaded image
* Model inference in browser and display output via a user interface

Let's look at each of these steps in greater detail.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/image-15.png)
_Photo from Unsplash_

## How to Convert a Keras SavedModel to the Tensorflow.js Layers Format

To convert a Keras SavedModel to the Tensorflow.js layers format, we'd need to use the tensorflowjs_converter script. We can also use the Python API as described in their official docs [here](https://www.tensorflow.org/js/tutorials/conversion/import_keras). 

I ran into a frustrating error with the former, as for some reason the tensorflowjs_converter did not seem to work on Google Colab. 

I had saved the model on drive and the "My Drive" part of the file path, specifically the space, seemed to be causing trouble. I found it mentioned in this GitHub issue #3618 [here](https://github.com/tensorflow/tfjs/issues/3618). 

Using the Python API worked seamlessly, which gave me a model.json file for the model architecture and binary files for the weights. Now I was ready to use it on the web!

![Image](https://www.freecodecamp.org/news/content/images/2021/05/pic.png)
_Code to convert SavedModel Format to Layers Format_

But wait! Why do we need to convert? Why don't we just train our model using Tensorflow.js itself? 

Well, you need to do this conversion if you've already spent a lot of time training your Keras models on large datasets and don't want to rewrite and retrain it using JavaScript.

## How to Load the Model via JavaScript and Promises

[Tensorflow.js](https://www.tensorflow.org/js/tutorials) is a JavaScript-based library for machine learning model development. You can use it in the browser as well as through the popular JavaScript runtime Node.js. 

You can set it up in two different ways: either by including it using a script tag or using it through Node.js. 

Since the CNN model I trained is fairly straight-forward, I opted for the script tag approach.

```html
<script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@2.0.0/dist/tf.min.js"></script>
```

Now that we've included the Tensorflow.js library, the next step is to load the model. We can load the model in the following ways:

* Browser's local storage
* Browser's IndexedDB storage
* From an HTTP or HTTPS endpoint
* From native file system using Node.js

Loading the model from an HTTPS endpoint seemed to be the most feasible way for me. So I hosted the model files on Firebase Hosting and loaded the model using the following code:

```javascript
const model = await tf.loadLayersModel('model.json');	
```

Tensorflow uses the `fetch` method to load resources using a Promise-based approach. Fetch returns a Promise which resolves to the response containing the requested resources. 

A Promise in JavaScript is a proxy for a value which you don't know at this current instant in time, but that will maybe be known at some later point in time. 

For example, when requesting for URL-based resources, we don't know immediately if we'll actually get those resources – we'll have to wait for some time until the server responds (or doesn't). 

But waiting in any form is detrimental to responsiveness and continued user interaction, which is critical for web pages. So JavaScript allows you to use asynchronous calls via Promises. These let you request resources AND continue with subsequent statements irrespective of the server's response. 

To allow cleaner and easier error handling with Promises, async/await was introduced. Await blocks control flow until a Promise returns and the functions with await statements are declared async. 

## How to Access an Image Uploaded by a User

Let's create a simple file upload functionality using an HTML input tag and another button that'll start the prediction computations when clicked.

```html
<div class="container" id="tray">
		<div id="uploadFile" class="custombutton">
			<i class="fa fa-file" style="font-size:25px;color: #1ab5e3"></i><br/><br/>
			<input type="file" name="fileupload" accept="image/*" onchange="display(event)">
		</div>
		<div class="custombutton">
			<i class="fa fa-bar-chart" style="font-size:25px;color: #1ab5e3"></i><br/><br/>
			<input type="button" name="predict" onclick="predict_emotion()" value="PREDICT">
		</div>
	</div>
```

The file upload and predict buttons look like this:

![Image](https://www.freecodecamp.org/news/content/images/2021/05/image-24.png)

Next, we access the image file uploaded and display it using object URLs as described in the MDN Web docs linked [here](https://developer.mozilla.org/en-US/docs/Web/API/File/Using_files_from_web_applications).

```javascript
let input_image = document.getElementById("input_image")
input_image.src = URL.createObjectURL(event.target.files[0]);
document.getElementById("input_image_container").style.display = "block";

<div id="input_image_container"><img src="#" id="input_image" style="top:5vh;"></div>
```

After uploading an image, it looks like this:

![Image](https://www.freecodecamp.org/news/content/images/2021/05/image-25.png)

## How to Preprocess the Uploaded Image

This is model domain-specific, and requires different steps for different applications. 

For my model, I didn't have to do much, just some simple normalization and resizing which I easily performed using Tensorflow.js functions. 

Do check out their [official API reference](https://js.tensorflow.org/api/latest/) for a thorough understanding of the functions offered and their use cases.

```javascript
//Preprocessing steps 
		/*
		(1)Resize to 48*48
		(2)Convert to grayscale using simple mean
		(3)Convert to float
		(4)Reshape to (1,48,48,1)
		(5)Normalize by dividing by 255.0
		*/
let step1 = tf.browser.fromPixels(input)
.resizeNearestNeighbor([48,48])
.mean(2)
.toFloat()
.expandDims(0)
.expandDims(-1)
.div(255.0)
```

## Model Inference in the Browser and Displaying the Output via a User Interface

The predict function returns the predictions – in our case, a tensor with 7 probability values for the 7 emotions. 

We scale up the probabilities for displaying in the browser using one div for each emotion and the div's width to specify the scaled up probability value.

```javascript
pred = model.predict(step1)
pred.data()
    .then((data) => {console.log(data)
		   		output = document.getElementById("output_chart")
		    	output.innerHTML = ""
		    	max_val = -1
		    	max_val_index = -1
				for(let i=0;i<data.length;i++)
				{
					style_text = "width: "+data[i]*150+"px; height: 25px; position:relative; margin-top: 3vh; background-color: violet; "
					output.innerHTML+="<div style = '" +style_text+ "'></div>"
					if(data[i] > max_val)
					{
						max_val = data[i]
						max_val_index = i
					}
				}
				EMOTION_DETECTED = emotions[max_val_index]
				document.getElementsByClassName("output_screen")[0].style.display="flex";
document.getElementById("output_text").innerHTML=""
document.getElementById("output_text").innerHTML = "<p>Emotions and corresponding scaled up probability</p><p>Emotion detected: " + EMOTION_DETECTED + "(" + (max_val*100).toFixed(2) + "% probability)</p>"
```

Great – we've got all the building blocks ready! Now let's put it all together. We'll integrate the following parts:

* The HTML markup which serves as a simple UI
* Script tag for accessing Tensorflow.js
* Script tag for our Font Awesome icons
* JavaScript code for model loading, inference, and output


Here is the final JavaScript code:

```javascript
//Display image uploaded by user
function display(event)
	{
		let input_image = document.getElementById("input_image")
		input_image.src = URL.createObjectURL(event.target.files[0]);
		document.getElementById("input_image_container").style.display = "block";
	}
    
//Predict emotion and display output
async function predict_emotion()
	{
		let input = document.getElementById("input_image");
		//Preprocessing steps 
		/*
		(1)Resize to 48*48
		(2)Convert to grayscale using simple mean
		(3)Convert to float
		(4)Reshape to (1,48,48,1)
		(5)Normalize by dividing by 255.0
		*/
		let step1 = tf.browser.fromPixels(input).resizeNearestNeighbor([48,48]).mean(2).toFloat().expandDims(0).expandDims(-1).div(255.0)
		const model = await tf.loadLayersModel('model.json');
		pred = model.predict(step1)
		pred.print()
		console.log("End of predict function")
		//This array is encoded with index i = corresponding emotion. In dataset, 0 = Angry, 1 = Disgust, 2 = Fear, 3 = Happy, 4 = Sad, 5 = Surprise and 6 = Neutral
		emotions = ["Angry", "Disgust", "Fear", "Happy", "Sad", "Surprise", "Neutral"]
		//At which index in tensor we get the largest value ?
		pred.data()
		    .then((data) => {console.log(data)
		    	output = document.getElementById("output_chart")
		    	output.innerHTML = ""
		    	max_val = -1
		    	max_val_index = -1
				for(let i=0;i<data.length;i++)
				{
					style_text = "width: "+data[i]*150+"px; height: 25px; position:relative; margin-top: 3vh; background-color: violet; "
					output.innerHTML+="<div style = '" +style_text+ "'></div>"
					if(data[i] > max_val)
					{
						max_val = data[i]
						max_val_index = i
					}
				}
				EMOTION_DETECTED = emotions[max_val_index]
				document.getElementsByClassName("output_screen")[0].style.display="flex";
				document.getElementById("output_text").innerHTML=""
				document.getElementById("output_text").innerHTML = "<p>Emotions and corresponding scaled up probability</p><p>Emotion detected: " + EMOTION_DETECTED + "(" + (max_val*100).toFixed(2) + "% probability)</p>"
		})	

	}
```

Here's the final HTML and script tags:

```html
<!DOCTYPE html>
<html>
<head>
	<title></title>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
	<link rel="stylesheet" type="text/css" href="styles/page_styling.css">
	
</head>
<script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@2.0.0/dist/tf.min.js"></script>
<body>
	<div id="input_image_container"><img src="#" id="input_image" style="top:5vh;"></div>
	<div class="container" id="tray">
		<div id="uploadFile" class="custombutton">
			<i class="fa fa-file" style="font-size:25px;color: #1ab5e3"></i><br/><br/>
			<input type="file" name="fileupload" accept="image/*" onchange="display(event)">
		</div>
		<div class="custombutton">
			<i class="fa fa-bar-chart" style="font-size:25px;color: #1ab5e3"></i><br/><br/>
			<input type="button" name="predict" onclick="predict_emotion()" value="PREDICT">
		</div>
	</div>
	<div class="container output_screen">
		<div id="emotion_tags">
			<ul>
				<li>Angry</li>
				<li>Disgust</li>
				<li>Fear</li>
				<li>Happy</li>
				<li>Sad</li>
				<li>Surprise</li>
				<li>Neutral</li>
			</ul>
		</div>
		<div id="output_chart"></div>
		<div id="output_text"></div>
	</div>
<script src="scripts/script.js"></script>
</body>
</html>

```

Here's a sample output, where the top three predicted emotions are sad, happy, and neutral:

![Image](https://www.freecodecamp.org/news/content/images/2021/05/image-8.png)
_Predictions and UI_

## Wrapping up

In this article, we went through the basic steps you need to go through to convert a Keras SavedModel to a web-friendly format. We learned how to load, preprocess, and infer in the browser using Tensorflow.js and display output via a user interface. 

I hope you enjoyed reading this article and found it helpful. Have a good day and I wish you good luck in your coding journey!

![Image](https://www.freecodecamp.org/news/content/images/2021/05/image-16.png)
_Photo from Unsplash_

