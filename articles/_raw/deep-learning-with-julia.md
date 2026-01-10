---
title: Deep Learning with Julia – How to Build and Train a Model using a Neural Network
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-07T21:34:07.000Z'
originalURL: https://freecodecamp.org/news/deep-learning-with-julia
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/cover-1.png
tags:
- name: Deep Learning
  slug: deep-learning
- name: Julia
  slug: julia
- name: Machine Learning
  slug: machine-learning
- name: neural networks
  slug: neural-networks
seo_title: null
seo_desc: 'By Andrey Germanov

  Julia is a general purpose programming language well suited for numerical analysis
  and computational science. Some consider it the future of machine learning and the
  most natural replacement for Python in this field.

  In the previou...'
---

By Andrey Germanov

[Julia](https://julialang.org/) is a general purpose programming language well suited for numerical analysis and computational science. Some consider it the future of machine learning and the most natural replacement for Python in this field.

In the previous post "[Machine learning with Julia – How to Build and Deploy a Trained AI Model as a Web Service](https://www.freecodecamp.org/news/machine-learning-using-julia/)" I introduced the basic machine learning features of Julia and explained why it's so good for this.

In this article, I want to move one step forward and explore deep learning features of Julia to show how you can use it to solve computer vision tasks using neural networks. 

Computer vision is one of the most impressive areas of artificial intelligence. It includes such interesting tasks as image classification, text recognition, object detection and image segmentation. Neural networks showed the best performance in solving computer vision problems.

In this tutorial, I will guide you through the process of building and training a neural network to recognize handwritten digits using Julia. I will also explain how to create a website that will use the trained model to read handwritten phone numbers. 

Here's what we'll cover:

1. [What should you know in advance](#heading-what-should-you-know-in-advance)
2. [Handwritten digits recognition workflow](#heading-handwritten-digits-recognition-workflow)
3. [How to collect initial image data](#heading-how-to-collect-initial-image-data)
4. [How to work with images in Julia](#heading-how-to-work-with-images-in-julia)
5. [How to prepare the image data for machine learning](#heading-how-to-prepare-the-image-data-for-machine-learning)
6. [How to create a machine learning model](#heading-how-to-create-a-machine-learning-model)
7. [How to train the model](#heading-how-to-train-the-model)
8. [How to evaluate the accuracy of the trained model](#heading-how-to-evaluate-the-accuracy-of-the-trained-model)
9. [How to create and train the convolutional neural network](#heading-how-to-create-and-train-the-convolutional-neural-network)
10. [How to export the trained model to a file](#how-to-export-the-trained-model-to-a-file)
11. [How to create a frontend](#heading-how-to-create-a-frontend)
12. [How to create a backend](#heading-how-to-create-a-backend)
13. [Conclusion](#heading-conclusion)

<h2 id="what-should-you-know-in-advance">What should you know in advance</h2>

This tutorial assumes that you have basic Julia knowledge, that possible to get by reading my [previous article](https://www.freecodecamp.org/news/machine-learning-using-julia). That article also includes instructions on how to install Julia and integrate it with Jupyter notebook, which will be used to write most of the code.

The "Handwritten digit recognition using deep learning" problem and the theory that stands behind it is well known. That is why I will cover it only briefly. There are many good resources that explain how neural networks are used to solve the image classification tasks. Personally, I recommend watching [this video](https://www.youtube.com/watch?v=aircAruvnKk) and read the first chapter of this great [online book](http://neuralnetworksanddeeplearning.com/chap1.html). 

The goal of this tutorial is only to show you how to implement the theory, explained in those resources, using Julia.

<h2 id="handwritten-numbers-recognition-workflow">Handwritten digits recognition workflow</h2>

To build a machine learning model we will use the [Flux.jl](https://fluxml.ai/) framework which is a pure Julia implementation of most well-known neural network types including [feed forward](https://deepai.org/machine-learning-glossary-and-terms/feed-forward-neural-network), [convolutional](https://deepai.org/machine-learning-glossary-and-terms/convolutional-neural-network) and [recurrent](https://deepai.org/machine-learning-glossary-and-terms/recurrent-neural-network) networks.

Recognizing handwritten numbers is a supervised machine learning task of image classification. To implement it, you need to have a labeled dataset of handwritten digits and use it to train the machine learning model. 

This is how the ML workflow looks:

* Collect the images of handwritten digits for recognition.
* Prepare a labeled dataset for machine learning by cleaning and labeling the data.
* Create a machine learning model to recognize handwritten digits.
* Train the model using training dataset.
* Evaluate the accuracy of the trained model by feeding it with data from a testing dataset.
* After achieving good accuracy, export the model to a file to use in applications.

<h2 id="how-to-collect-initial-image-data">How to collect initial image data</h2>

The first step of any machine learning task is to collect the data that will be used for training. Usually this is the bigger part of the whole process.

How do you collect handwritten digits for this? Well, for example, you can ask all your friends in social networks to write down digits from 0 to 9 and save them to images. They also can ask their friends to do the same and finally send all these images to you. 

The more data you collect, the better for machine learning.

Then, you could create folders with names from "0" to "9" and arrange these images within them. Also, you need to convert the images to the same format: convert to grayscale and resize them. All images should have the same size and color format. 

Finally, you'll have a labeled collection of handwritten digits that are ready to work with. 

Fortunately, you do not need to do all this manual work, because it was already done in 1998 by the National Institute of Standards and Technology. The database of handwritten digits, that called MNIST, is available to download from Kaggle or from many other places. For example, you can download and extract the MNIST archive using [this link](https://www.kaggle.com/datasets/jidhumohan/mnist-png). 

This database is already split into testing and training data in appropriate folders. Each of these folders contains images of handwritten digits, classified to folders from "0" to "9". There are 60000 images in the `training` folder and 10000 images in the `testing` folder:

![Image](https://www.freecodecamp.org/news/content/images/2023/03/minst.png)
_MNIST database images_

Each file is a 28x28 gray scaled image. We will use the content of the `training` folder to prepare the dataset for training the neural network model. Then we will use the content of the `testing` folder to validate the accuracy of the trained model. Before doing that, we need to convert this raw data to datasets.

In order to continue, run the Jupyter notebook and create a new notebook in it, selecting "Julia" as a language. Then, copy the `training` and `testing` folders with images to the folder in which you created the notebook.

<h2 id="how-to-work-with-images-in-julia">How to work with images in Julia</h2>

An image is not a natural data format for machine learning models. The models understand only numbers. That is why, to prepare the images for machine learning, you need to load them and convert to numbers. 

To work with images in Julia, we will use the [Julia Images](https://juliaimages.org/stable/) library. Using this library, you can load the image, convert it to matrix of pixels, and apply different transformations that can be required before pushing it to ML. The transformations include resizing, converting from color to black and white, inverting, cropping, and more.

To start working with these functions, you need to install the `Images` package and import it to your notebook:

```julia
using Pkg
Pkg.add("Images")
using Images
```

### How to load and view the image

You can use the `load` function to load the image. Let's load the first digit from our training dataset. If this file exists, it should load it to the `img` variable and display the image itself:

```julia
img = load("training/0/1.png")
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image1.png)
_Loaded digit image_

This is a loaded digit. Let's see the shape of the `img` variable:

```julia
size(img)
```

(28,28)

As you see, the `img` variable is an 2D array or matrix of image pixels. The first dimension of the array is a number of rows and the second dimension is a number of columns. That is why the height of image is the first value and the width of image is the second value. 

Let's see the type of this variable now:

```julia
typeof(img)
```

Matrix{Gray{N0f8}} (alias for Array{Gray{Normed{UInt8, 8}}, 2})

It shows that this is a matrix of "Gray" objects. The `Gray` type defines a gray pixel. It means that the image that we loaded does not have color information. 

The `Gray` data type defines the pixel by a single value – the intensity of gray color in a range between 0 and 1. So, the 0 is completely black and the 1 is completely white. 

You can change a color of any pixel using the following code:

```julia
img[5,5] = Gray(0.5)
```

This way you set the average gray color to the specified pixel (which was previously black).

![Image](https://www.freecodecamp.org/news/content/images/2023/03/pixel_changed.png)
_The image with modified pixel_

If you load the full color image and request its type, it will show something like this:

Matrix{RGB{N0f8}} (alias for Array{RGB{Normed{UInt8, 8}}, 2})

In this case, each pixel has a type of `RGB` which defined by 3 values: intensity of **R**ed, intensity of **G**reen and intensity of **B**lue. Also, if you run `size(img)` for a colored image, you will see that this is a 3D array, like this:

(3,28,28)

where the first dimension is a number of color channels, the second dimension is a height and the third dimension is a width. 

In other words, this color image consists of three matrices of 28x28 size. Each of them contains intensities of the appropriate color. 

To set the color of any pixel in this image, you need to specify intensities of 3 channels in the `RGB` type constructor:

```julia
img[5,5] = RGB(1,0.5,0)
```

This code sets the pixel color to orange.

### How to implement basic image transformations

Because the image is an array, you can use the array syntax to get access to any part of the image or even to individual pixels. 

For example, you can run this to extract the first 10 rows and 20 columns of this image and write them to the new image:

```julia
img2 = img[1:10,1:20]
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/top_crop_image.png)
_Part of image_

You can crop the image by 5 pixels from all sides:

```julia
img3 = img[5:22,5:22]
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/cropped_image.png)
_Cropped image_

You can apply different filters to the image by applying the specified function to each element of the matrix, using the [Julia broadcasting](https://docs.julialang.org/en/v1/manual/arrays/#Broadcasting) feature via "dot" syntax. 

For example, this code applies the `Gray` function to each pixel of the image. This approach can be used to convert images from colored to grayscale:

```julia
img4 = Gray.(img)
```

Similarly, you can convert gray images to colored:

```julia
img5 = RGB.(img)
```

You can apply custom functions to each pixel. For example, if you apply the next anonymous function to the gray image this way:

```julia
img6 = (x-> Gray(1)-x.val).(img)
```

it will invert the image colors by subtracting the color value of each pixel from 1. If the `img` has a white digit on a black background, then the `img6` will have a black digit on a white background:

![Image](https://www.freecodecamp.org/news/content/images/2023/03/inverted_image.png)
_Inverted image_

Finally, to resize the image, you can use the `imresize` function. For example, to resize the `img` to 50x50 pixels, you can use the following code:

```julia
img6 = imresize(img,(50,50))
```

We will use only the features described above to prepare the images for handwritten digit recognition. But the `Images` module has many more interesting and fun things. Watch [this video](https://www.youtube.com/watch?v=DGojI9xcCfg) to see some of them. Also, you can find a lot of interesting information in [this book](https://www.packtpub.com/product/hands-on-computer-vision-with-julia/9781788998796).

### How to convert the image to numeric matrix

The last image preprocessing step is converting the pixels to numbers, because objects of type `Gray()` or `RGB()` are not suitable as an input for the machine learning model. 

You can do this in two steps. First, you need to apply the `channelview` function to the image to get the matrix view of the image object, and then, convert the result to float numbers. So, if you run this command:

```julia
data = Float32.(channelview(img))
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/channelview2.png)
_Image matrix_

you will get the matrix, where each value is a float number that represents an intensity of the corresponding pixel. This data is ready to go to the neural network.

<h2 id="how-to-prepare-the-image-data-for-machine-learning">How to prepare the image data for machine learning</h2>

As I wrote in a [previous article](https://www.freecodecamp.org/news/machine-learning-using-julia/#how-to-prepare-the-training-data-for-machine-learning), the training dataset should consist of data from the feature matrix and from the labels vector. Both should contain only numbers. 

Let's go back to our image collections in the `training` and `testing` folders. The labels are subfolder names where images located. They are already numbers. The features of an image are the pixels. Each pixel is defined by its color intensity. 

So, to create a dataset that is ready for training from the images folder, you need to read all files from all subfolders, convert them to matrices of float numbers, and put them in the array. 

```julia
path = "training"
X = []
y = []
for label in readdir(path)
    for file in readdir("$path/$label")
        img = load("$path/$label/$file")
        data = reshape(Float32.(channelview(img)),28,28,1)
        if length(X) == 0
            X = data
        else
            X = cat(X,data,dims=3)
        end
        push!(y,parse(Float32,label))
    end
end
```

Ensure that the "training" and the "testing" folders with the MNIST images exist in the current folder before running this program. It will take a while to execute this code, because it will load 60000 images and will convert them to matrices. 

In the outer loop, it reads the contents of the "training" folder. There are subfolders with names from 0 to 9 that will be used as labels. 

Then, in the inner loop, it reads all image files of each of these subfolders using the `load` function from the `Images` package. 

Next, it converts each image to the matrix of color intensities and places it in the `data` variable. After that, it appends this matrix to `X`. 

Finally, it appends the name of the subfolder (which is an actual digit) to the labels vector `y`. 

This way, you will have a dataset with feature matrix in `X` and labels vector in `y`. Let's refactor this code to a function to be able to reuse it to convert any folder with images, classified this way, to the dataset.

```julia
using Images
function createDataset(path)
    X = []
    y = []
    for label in readdir(path)
        for file in readdir("$path/$label")
            img = load("$path/$label/$file")
            data = reshape(Float32.(channelview(img)),28,28,1)
            if length(X) == 0
                X = data
            else
                X = cat(X,data,dims=3)
            end
            push!(y,parse(Float32,label))
        end
    end
    return X,y
end
```

Using this function, you can now easily create both training and testing datasets:

```julia
x_train, y_train = createDataset("training")
x_test, y_test = createDataset("testing")
```

<h2 id="how-to-create-a-machine-learning-model">How to create a machine learning model</h2>

We will use a neural network to create a model and train it using the training data. To work with neural networks we will use the [Flux.jl framework](https://fluxml.ai/) which allows you to create and train neural networks of various types, including feed forward, convolutional, and recurrent. 

For handwritten image classification, we will implement both the Feed Forward and the Convolutional networks and compare their accuracy. If you need to, you can review the basics of neural networks by [watching this video](https://www.youtube.com/watch?v=aircAruvnKk&t=313s). Now is the best time to watch this before you continue reading.

### Neural network basics

A neural network is a chain of layers. Each layer has a defined number of neurons with inputs and outputs. 

To convert input to output for each layer, the neurons use the activation function, defined for this layer. Features of the image are the inputs of the first layer, and the classification results are the outputs of the last layer.

The best way to understand all this is to visualize some neural network architecture. Let's see the following basic neural net of 3 layers:

![Image](https://www.freecodecamp.org/news/content/images/2023/03/dense_net.png)
_Feed forward neural network for digits recognition. Source: http://neuralnetworksanddeeplearning.com/chap1.html_

In this picture, the input layer contains 784 neurons that should receive the features of each image. As you remember, the training dataset consists of 28x28 images, which is 784 pixels. This is how this neural network works:

* The color value of each pixel goes to each neuron of the input layer.
* Each neuron of the input layer sends its value to each neuron of the hidden layer. 
* Each neuron of the hidden layer has a weight coefficient for each input. By default, these coefficients are random numbers. So, each neuron on the hidden layer receives input values from the previous layer and multiplies each input by the appropriate weight, summarizes these products, and applies the activation function to that sum.
* Each neuron of the hidden layer sends the resulting sum to each neuron of the output layer, which has 10 neurons.
* The output layer does exactly the same for each input value as the previous layer and finally accumulates some sum inside.
* This sum is treated as a probability of the appropriate digit, for example the first neuron should contain the probability that the input image is "0", the second neuron should contain the probability that the image is "1", and so on. 

Then, the application should look at which of these 10 neurons has the highest value and make the appropriate prediction.

### How to create the neural network with Flux

Let's create this neural network using Flux. If you haven't installed and imported it yet, do this in your notebook:

```julia
using Pkg
Pkg.add("Flux")
using Flux
```

As you have seen, the neural network is a chain of layers with different parameters. So, Flux has a `Chain` function that you use to construct neural networks. Let's construct that network:

```julia
model = Chain(
    Flux.flatten,
    Dense(784=>15,relu),
    Dense(15=>10,sigmoid),
    softmax
)
```

The `Chain` receives an array of functions as arguments. Each function defines a layer and it's parameters. Each of these functions receives some inputs, then after the appropriate actions returns the outputs and forwards them as inputs to the next function in the chain. 

So, this is how the defined neural network works:

* The input image, which is a 28x28 array of pixel color intensities, comes to the `Flux.flatten` function. This function just converts this 28x28 matrix to a vector with 784 elements. This way we constructed the input for the first Dense layer.
* Then, the next Dense function receives 784 values by 15 neurons. Then it multiplies these values by weights, summarizes these products, applies the `[relu](https://fluxml.ai/Flux.jl/stable/models/activation/#NNlib.relu)` activation function to this sum, and forwards these 15 values to 10 neurons of the next layer.
* Next, the dense layer also multiplies each 15 inputs by the weight coefficients, summarizes them, and applies the `sigmoid` activation function to convert these sums to fractions of 1.
* The final `[softmax](https://en.wikipedia.org/wiki/Softmax_function)` function actually doesn't build a new layer, but it just converts values that accumulated in the 10 neurons of the output layer to correct probabilities to properly show the probability distribution. Applying this function ensures that the sum of all 10 probabilities is equal to 1. The array of these probabilities will be returned by the model as a result.

You can call the `model` which you just created as a function by passing an image matrix as an input argument. 

You can run the model to predict the digit for the first image from the training dataset using the following code:

```julia
predict = model(Flux.unsqueeze(x_train[:,:,1],dims=3))
```

We use the `[unsqueeze](https://fluxml.ai/Flux.jl/stable/utilities/#Flux.unsqueeze)` function here to convert the image without channels of the (28,28) shape to the single channel image of the (28,28,1) shape. 

This is an important rule for deep neural network processing – that the image is something that has a width, height, and color channels. So, even if it has only a single channel, it must be specified.

The model function receives the input image matrix, passes it through a chain of layers, and returns the array of probabilities.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/probs1-1.png)
_New neural network probabilities_

As you can see, the highest probability has a neuron number 2 (0.12457416) which means that the model predicted the digit "1". However, if you check the real answer in the labels vector:

```julia
y_train[1]
```

you will see "0", so the prediction is incorrect. This is because this model is untrained and just uses random weights to calculate the output for each layer. You need to train it to adjust these weights and calculate more accurate probability.

<h2 id="how-to-train-the-model">How to train the model</h2>

Flux.jl has different approaches to training a model. The most obvious one is the `[Flux.train](https://fluxml.ai/Flux.jl/stable/training/reference/#Flux.Optimise.train!-NTuple{4,%20Any})` function. The function runs the following training process:

* The function receives the training dataset as an argument, including the features matrix and the labels vector.
* The function runs the `model` for each row of the training dataset and receives the resulting probabilities array.
* The function compares these probabilities with the true values from the labels vector and calculates the **amount of error** (about this later).
* Using information about the error, the function adjusts the weights and bias for each neuron on each layer.

Usually you need to run this training process many times in a loop. On each iteration it will adjust the weights for each neuron, decreasing the error value more and more.

This visualization shows how the training process in a loop works for a single neuron on a single layer. For the whole network it works similar.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/1677823812311.gif)
_The training process in a loop for a single neuron_

This is a syntax of the `train` function:

```julia
Flux.train!(loss_function, model, data, optimizer)
```

Let's break this down:

* `loss_function` – as I described before, during the training process, the `train` function measures the amount of error. To do this, it uses the `loss_function`, which you should define and provide here.   
  
This function receives the model, the row of the training data, and the truth label. Based on these arguments, the loss function should make a prediction by passing the row of data through the model, comparing this prediction with the truth label, calculating the difference between them, and returning the amount of error as a float number.  
  
There are different algorithms exist to calculate the amount of error for different machine learning problem types. For classification problems we will use **[cross entropy](https://fluxml.ai/Flux.jl/stable/models/losses/#Flux.Losses.crossentropy)**.
* `model` – the neural network model to train.
* `data` – the training data that includes both `x_train` and `y_train` assembled to a single array of tuples. You can do this simply by using the `[Flux.DataLoader](https://fluxml.ai/Flux.jl/v0.10/data/dataloader/)` function, which we will use below.
* `optimizer` – as described above, after measuring the amount of error, the function adjusts the weights to decrease the error. The weights are not adjusted randomly, but by the `optimizer` that defines the algorithm. You use it to adjust the weights in the correct direction.   
  
Most of the weight adjustment algorithms are based on [Gradient Descent](https://builtin.com/data-science/gradient-descent). In particular, we will use the [ADAM](https://fluxml.ai/Flux.jl/stable/training/optimisers/#Flux.Optimise.Adam) optimizer, which is very common today.

Let's connect all these parts together in the following code:

```julia
# Assemble the training data
data = Flux.DataLoader((x_train,y_train), shuffle=true)

# Initialize the ADAM optimizer with default settings
optimizer = Flux.setup(Adam(), model)

# Define the loss function that uses the cross-entropy to 
# measure the error by comparing model predictions of data 
# row "x" with true data label in the "y"
function loss(model, x, y)
	return Flux.crossentropy(model(x),Flux.onehotbatch(y,0:9))
end

# Train the model 10 times in a loop
for epoch in 1:10
	Flux.train!(loss, model, data, optimizer)
end
```

For each row of data, the `Flux.train!` calls the loss function, then the `loss` function runs the `model`. Using cross entropy, it calculates the difference between the predictions with true values of this row. This difference is returned as an error, and then the `optimizer` is used to adjust the weights of the model neurons based on this error value and the `loss` function. On each iteration, the error value should go down.

Finally, after running the training process, you can check how it predicts the digit for the first image using the trained model:

```julia
predict = model(Flux.unsqueeze(x_train[:,:,1],dims=3))
```

When I did that, I received the following probabilities:

![Image](https://www.freecodecamp.org/news/content/images/2023/03/probs2.png)
_Trained model probabilities_

The first one, related to "0" is the highest and this is definitely true. You can try to check other images, like image number 100 or 200. But it doesn't make much sense to measure model quality this way, because this is a training data that the model has already seen. Only the testing data should be used to measure the accuracy of the model.

<h2 id="how-to-evaluate-the-accuracy-of-the-trained-model">How to evaluate the accuracy of the trained model</h2>

We have the testing dataset in the `x_test` features matrix and in the `y_test` labels vector. We will run the `model` for each row of this data and measure the accuracy: the number of correct predictions divided by the number of all predictions.

Let's create a function for this:

```julia
function accuracy()
    correct = 0
    for index in 1:length(y_test)
        probs = model(Flux.unsqueeze(x_test[:,:,index],dims=3))
        predicted_digit = argmax(probs)[1]-1
        if predicted_digit == y_test[index]
            correct +=1
        end
    end
    return correct/length(y_test)
end
```

The function goes over all items of the testing dataset. For each item it runs the model and receives the `probs` array. Then, it writes an index of the highest probability using the `[argmax](https://docs.julialang.org/en/v1/base/collections/#Base.argmax)` function to the `predicted_digit` variable. Next it compares the predicted digit with the truth value from `y_test` labels vector and increases the number of correct predictions if they match. The function returns the quotient of the number of correct predictions and the total number of rows.

Now you can run this function to see the accuracy. For example, when I ran this, I received the 0.9455, which is about 94.6%. 

However, it's better to place this function call inside the training loop, right after the `Flux.train!` line to see how the accuracy changes after each training iteration.

```julia
for epoch in 1:10
    Flux.train!(loss, model, data, optimizer)
    println(accuracy())
end
```

Then run the training again. You should receive output similar to this:

![Image](https://www.freecodecamp.org/news/content/images/2023/03/accuracies.png)
_Accuracy of the neural network_

It shows that accuracy was going up until the 6th iteration. Since then, it started to go down, which could be a sign that the model started to overfit.

To increase the prediction quality, you can either add more data to the training dataset or change the model architecture. 

For example, you can add more Dense layers, increase the number of neurons on the hidden layer, or change activation functions from `relu` to `sigmoid` or vice versa.

When I increased the number of neurons from 15 to 42 on the hidden layer and then removed the `sigmoid` activation from the output layer, I've achieved about 97% accuracy. But when I added one more hidden layer before output, the accuracy dropped to 90%. 

So, building the neural net architecture is like art – you need to try different options a lot of times and finally select the one that works the best. 

Regardless of the options I chose, I could never achieve more than 97%. Also, when I finally tried to use this network architecture in production with real handwritten digits from users, the prediction quality was poor. Very often it could not recognize the 7 digit properly, and it recognized 1 as 4 and 6 as 5.

This is because using the feed forward neural network, in which we just put all 784 pixels of the image as an input without any filters, is not the best approach.

For most machine learning tasks with images, the **Convolutional** neural networks is the better option. We will create and try this one in the next section.

<h2 id="how-to-create-and-train-the-convolutional-neural-network">How to create and train the convolutional neural network</h2>

The most important step during the machine learning process is data preprocessing. If input features are processed properly, then the prediction accuracy will be better. 

To increase the model quality, you need to remove noise from data, or features that are not relevant for the value that you need to predict. 

Also, oftentimes you need to create new features from existing ones that could be more relevant to the result. 

For example, for the Titanic machine learning problem, you can remove such features as "Passenger ID" and "Passenger name", because they can't help to predict whether the passenger might survive or not. 

Also, if you have a task to predict the price of a flat and have input data with fields of room areas like "Area 1", "Area 2" and so on, you can create a new field "Total Flat Area" and write the sum of all room areas to it. 

Perhaps this new feature that you generated is more relevant than others for the model, so you can remove the fields from which you generated that new column.

Using these techniques, you generalize the data by keeping and creating the features that are important and by removing others that can only confuse the machine learning model.

When working with tabular data, you can use your own experience or statistical methods to find which features to generate or remove from input data. But when working with images, things are not as clear as with strings or numbers.

For example, the model for the handwritten digits recognition task receives the 784 pixel colors in a single row as an input. They have an equal value from a human point of view, and it's unknown which of them are more important and which of them are less.

To help you in this, you can use **convolutional neural networks** to preprocess this kind of data. They help you do the feature engineering automatically.

You build a convolutional neural network from two types of layers:

* **Convolution layers** used to generate new features from input image pixels.
* **Pooling layers** used to generalize features using some rules and this way reduce their quantity.

By combining these two types of layers in the chain, you can preprocess the input image matrix to receive a reduced number of the most valuable features. Then, you can train the network using these generated features as input data in the same way as you did before.

I think it's difficult to describe CNNs better than it's done in [this video](https://www.youtube.com/watch?v=JB8T_zN7ZC0), so I highly recommend watching it (or at least the first 15 minutes) before continue. It clearly explains the theoretical aspects of all steps that you will do below.

So, let's review the neural network that you have now:

```julia
model = Chain(
    Flux.flatten,
    Dense(784=>15,relu),
    Dense(15=>10,sigmoid),
    softmax
)
```

The only data preprocessing step here is the `Flux.flatten`, that receives the image of 28x28 pixels and returns it joined to a single row of 784 numbers. We need to add some convolution layers before the `Flux.flatten` to give to our network the ability to generate better features than just raw pixels.

To create the convolution layer, the Flux.jl has the `[Conv](https://fluxml.ai/Flux.jl/stable/models/layers/#Flux.Conv)` function with the following main parameters:

```julia
Conv(filter,in=>out,activation_function)
```

* **filter** defines dimensions of the kernel matrix that will be applied to each pixel of the input matrix to create a feature from it. For example, the value (3,3) defines the 3x3 kernel matrix. This is how the convolution using this kernel matrix works to generate the features for an image of 6x6 size:

![Image](https://www.freecodecamp.org/news/content/images/2023/03/2D_Convolution_Animation.gif)
_How convolution layer works_

* **in** is the number of input image channels. For our input data, gray images have a single channel. For other layers, the number of **in** channels of current layer must be equal to the **out** channels of previous layer.
* **out** is the number of output channels after apply the convolution. In other words, it's a number of features that will be generated for each pixel.
* **activation_function** is the function that will be applied to each feature after convolution and before sending to the next layer of the network, the same as we did before for `Dense` layers.

For example, if you add the following `Conv` layer on top of the others to the Chain:

```julia
model = Chain(
    Conv((5,5),1=>6,relu),
    Flux.flatten,
    Dense(4704=>15,relu),
    Dense(15=>10,sigmoid),
    softmax
)
```

this network will get a single channel image of the following shape: (28,28,1). It will produce 6 matrices from this image by applying different convolution kernels of 5x5 to the input data. 

The output of this layer will be the image of the following shape: (28,28,6). In other words, this convolution layer will generate 28*28*6 =  4704 features from 784 input pixels for our network.

But if you have more features, it does not mean that they are all good. Perhaps you need to generalize them and leave only the most valuable ones. This is why the pooling layers are created. 

In Flux.jl, the pooling layer can be defined using the `[MaxPool](https://fluxml.ai/Flux.jl/stable/models/layers/#Flux.MaxPool)` function. It receives the pooling window dimensions as an argument.

For example, if you create the following MaxPool layer:

```julia
MaxPool((2,2))
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/maxpool_animation.gif)
_How Max pool layer works_

it will apply the 2x2 window to the input image. As you can see, for each window it selects the maximum value and adds it to the output. This way it reduces the input data by leaving only maximums in it. That is why it's called the MAX pool layer.

Let's add the MaxPool layer to the chain:

```julia
model = Chain(
    Conv((5,5),1=>6,relu),
    MaxPool((2,2)),
    Flux.flatten,
    Dense(1176=>15,relu),
    Dense(15=>10,sigmoid),
    softmax
)
```

So, the MaxPool receives the (28,28,6) sized image from the convolution layer, applies the 2x2 max pool window to it, and outputs (14,14,6) image. After this, the 14*14*6=1176 generalized features are forwarded to the network layers below.

The main question is how to know which number of convolution and max pool layers to add, and which parameters to set for each of them to achieve good prediction accuracy. 

Well, the first way is to try different options. But to build a good neural network architecture this way could take days, months, or even years.

Fortunately, for many machine learning tasks, it has already been done by other people. You can find suitable architectures for most of your problems, including the model for the handwritten digit recognition.

The most known architecture for this task was created by Yann LeCun, and it's named LeNet. You can find a full description and implementations of this model for different ML platforms [here](https://d2l.ai/chapter_convolutional-neural-networks/lenet.html). It was created exactly for the digit images from MNIST dataset. It's relatively old, but still used in many ATMs to recognize digits for processing deposits.

This is how this architecture looks: 

![Image](https://www.freecodecamp.org/news/content/images/2023/03/LeNet-5.png)
_LeNet architecture_

Just like the network we created, this one consists of a convolutional part and a feed forward part. The convolutional net part consists of 2 Conv and 2 MaxPool layers. The feed forward neural network part consists of 3 dense layers.

You can create this network using Flux.jl this way:

```julia
model = Chain(
    Conv((5,5),1 => 6, relu),
    MaxPool((2,2)),
    Conv((5,5),6 => 16, relu),
    MaxPool((2,2)),
    Flux.flatten,
    Dense(256=>120,relu),
    Dense(120=>84, relu),
    Dense(84=>10, sigmoid),
    softmax
)
```

After applying 2 convolutions and pooling to the input image matrix, the `Flux.flatten` layer receives the 4x4x16 image and converts it to 4*4*16=256 generalized features. Then they go through 3 dense layers to finally calculate probabilities for 10 digits.

Before training this model using the data from `x_train`, you need to reshape it a little bit. The convolution layer expects to get the data in the following 4-dimensional shape (width,height,channels,length), but the x_train has the following shape: (28,28,60000) which is 60000 images of 28x28. 

To make it compatible, you need to reshape it to (28, 28, 1, 60000). You can do this using the following code:

```julia
x_train = reshape(x_train, 28, 28, 1, :)

```

You'll need to do the same with `x_test`:

```julia
x_test = reshape(x_test, 28, 28, 1, :)
```

To run this model, you also need to pass a 4 dimensional image structure to the `model` function. For example, to make a prediction for the first image, you can run this:

```julia
model(Flux.unsqueeze(x_test[:,:,:,1],dims=4))
```

Then you can train the model the same way as you did before. 

This is the whole code to define and train the convolutional network:

```julia
# Create a LeNet model
model = Chain(
    Conv((5,5),1 => 6, relu),
    MaxPool((2,2)),
    Conv((5,5),6 => 16, relu),
    MaxPool((2,2)),
    Flux.flatten,
    Dense(256=>120,relu),
    Dense(120=>84, relu),
    Dense(84=>10, sigmoid),
    softmax
)

# Function to measure the model accuracy
function accuracy()
    correct = 0
    for index in 1:length(y_test)
        probs = model(Flux.unsqueeze(x_test[:,:,:,index],dims=4))
        predicted_digit = argmax(probs)[1]-1
        if predicted_digit == y_test[index]
            correct +=1
        end
    end
    return correct/length(y_test)
end

# Reshape the data
x_train = reshape(x_train, 28, 28, 1, :)
x_test = reshape(x_test, 28, 28, 1, :)

# Assemble the training data
train_data = Flux.DataLoader((x_train,y_train), shuffle=true)

# Initialize the ADAM optimizer with default settings
optimizer = Flux.setup(Adam(), model)

# Define the loss function that uses the cross-entropy to 
# measure the error by comparing model predictions of 
# data row "x" with true data from label "y"
function loss(model, x, y)
	return Flux.crossentropy(model(x),Flux.onehotbatch(y,0:9))
end

# Train model 10 times in a loop
for epoch in 1:10
    Flux.train!(loss, model, train_data, optimizer)
    println(accuracy())
end

```

After running this code, I received about 99% accuracy, which is close to ideal:

![Image](https://www.freecodecamp.org/news/content/images/2023/03/conv_accuracy-1.png)
_Accuracy of the convolutional network_

Now it's time to save this model to a file and move it to production.

<h2 id="how-to-export-trained-model-to-a-file">How to export trained model to a file</h2>

Flux.jl models can be saved to BSON files. You need to import the `BSON` package and use the `@save` macro command to export the `model` object:

```julia
using BSON
BSON.@save "digits.bson" model
```

This will save the model to the `digits.bson` file into the current folder.

This is the end of your work in the Jupyter notebook. We'll implement the following code as a new application.

<h2 id="how-to-create-a-frontend">How to create a frontend</h2>

The application which you are going to create will allow a user to write their phone number and recognize it using the model that you created and trained before. The frontend page will look like this:

![Image](https://www.freecodecamp.org/news/content/images/2023/03/frontend.png)
_Frontend_

Using this interface, the user can draw digits of a phone number in the boxes using the mouse, then press the "Recognise" button and display the recognised digits in the "Result" input field. 

Also, there is a "Switch to eraser" button. When the user presses it, the drawing mode changes to the eraser mode and the user can erase any number in any box.

Let's start building the web application. Create a new folder with any name that you like. Then create an `index.html` file in it and copy the following code to this file:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Phones reader</title>
</head>
<body>
    <h1>Draw phone number and recognise it</h1>
    <div class="digits">
        <strong>+</strong>
        <canvas width="50" height="50"></canvas>
        <strong>(</strong>
        <canvas width="50" height="50"></canvas>
        <canvas width="50" height="50"></canvas>
        <canvas width="50" height="50"></canvas>
        <strong>)</strong>
        <canvas width="50" height="50"></canvas>
        <canvas width="50" height="50"></canvas>
        <canvas width="50" height="50"></canvas>
        <strong>-</strong>
        <canvas width="50" height="50"></canvas>
        <canvas width="50" height="50"></canvas>
        <canvas width="50" height="50"></canvas>
        <canvas width="50" height="50"></canvas>
        <div class="buttons">
            <button id="mode">Switch to eraser</button>
        </div>
    </div>
    <div class="result">
        <button id="recognise">Recognise</button>
        <label>Result:</label>
        <input id="result"></div>
    </div>
</body>
<script>
    let mode = "brush";
    // "Switch" button handler. Switches mode from 
    // brush to eraser and back
    document.querySelector("#mode").addEventListener("click",() => {
        if (mode === "brush") {
            mode = "eraser";
            event.target.innerHTML = "Switch to brush";
        } else {
            mode = "brush";
            event.target.innerHTML = "Switch to eraser";
        }
    });
    // Digits canvases mouse move handler.
    // If mouse button pressed while user moves the mouse
    // on canvas, it draws circles in cursor position.
    // If mode="brush" then circles are black, otherwise
    // they are white
    document.querySelectorAll("canvas").forEach(item => {
        ctx = item.getContext("2d");  
        ctx.fillStyle="#FFFFFF";
        ctx.fillRect(0,0,50,50);
        item.addEventListener("mousemove", (event) => {
            if (event.buttons) {
                ctx = event.target.getContext("2d");  
                if (mode === "brush") {
                    ctx.fillStyle = "#000000";         
                } else {
                    ctx.fillStyle = "#FFFFFF";         
                }
                ctx.beginPath();               
                ctx.arc(event.offsetX-1,event.offsetY-1,2,0, 2 * Math.PI);
                ctx.fill();   
            }
        })
    })
    // "Recognise" button handler. Captures
    // content of all digit canvases as BLOB.
    // Construct files from these blobs and
    // posts them to backend as a files as a
    // multipart form
    document.querySelector("#recognise").addEventListener("click", async() => {
        data = new FormData();
        canvases = document.querySelectorAll("canvas");
        const getPng = (canvas) => {
            return new Promise(resolve => {
                canvas.toBlob(png => {
                    resolve(png)
                })
            })
        }
        index = 0
        for (let canvas of canvases) {
            const png = await getPng(canvas);
            data.append((++index)+".png",new File([png],index+".png"));
        }
        const response = await fetch("http://localhost:8080/api/recognize", {
            body: data,
            method: "POST"
        })
        document.querySelector("#result").value = await response.text();
    })

</script>
<style>
    body {
        display:flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: flex-start;
    }
    canvas {
        border-width:1px;
        border-color:black;
        border-style: solid;
        margin-right:5px;
        cursor:crosshair;
    }
    .digits {
        display:flex;
        flex-direction: row;
        align-items: center;
        justify-content: flex-start;
    }
    .digits strong {
        font-size: 72px;
        margin:10px;
    }
    .buttons {
        display:flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: center;
    }
    button {
        width:100px;
        margin-bottom:5px;
        margin-right:10px;
    }
    .result {
        margin-top:10px;
        display:flex;
        flex-direction: row;
        align-items: flex-start;
        justify-content: flex-start;
    }
    input {
        margin-left:10px;
    }
</style>
</html>
```

The HTML part of this code contains 11 [HTML5 canvas](https://www.w3schools.com/html/html5_canvas.asp) elements that display the boxes where you can draw. Each box has a size of 50x50 pixels and is filled with a white color. Also, the HTML contains "Switch to ..." and "Recognise" buttons and the "Result" input field.

The JavaScript part defines the "mode" global variable, which is equal to "brush" by default. When the user presses the "Switch to ..." button, it changes the mode to the "eraser". If they press it again, it switches back to the "brush".

Next, the JavaScript code defines "mousemove" event handlers for all canvas boxes. If the user presses the left mouse button in the "brush mode" and moves the mouse in the box, it draws black circles in place of the mouse cursor. This way, the user draws the digits. If the mode is "eraser", then it draws white circles. This way, the user can erase the black marks.

Finally, we defined the "Recognise" button click handler. When the user clicks this button, the handler function collects 11 digit images from the `canvas` elements and converts them to [BLOB](https://developer.mozilla.org/en-US/docs/Web/API/Blob) objects in a PNG image format. 

Then it creates a POST request, puts these 11 digit images in it as files with names 1.png, 2.png and so on, and sends them to the `/api/recognize` endpoint of the backend service on port 8080 of a local host (which we will create in the next section). 

The backend should receive these images, recognise digits in them, and return the recognition result as a string. This string will be displayed in the "Result" input field.

Lastly, I defined some CSS to apply basic styles to this page. You can modify them as you want. Now, let's move to the most interesting part – the digits recognition backend.

<h2 id="how-to-create-a-backend">How to create a backend</h2>

As a modern and mature programming language, Julia has a lot of libraries and frameworks for different tasks. Web frameworks are not an exception. We will use the [Genie.jl](https://genieframework.com/) framework, which is similar to the Express in Node.js or Flask in Python.

With Genie.jl you can run a basic web service in two lines of code:

```julia
using Genie
up(8080, async=false)
```

It will run a web server on port 8080 of a local host.

Using any text editor, for example VSCode with the [Julia extension](https://www.julia-vscode.org/), create a new Julia file like `digits.jl` in the same folder with the `index.html`. This is where you'll write the next bit of code.

This web service will have two endpoints:

* **`/`** to display the index.html web page that you created before.
* **`/api/recognize`** to receive POST requests with the images of digits, recognize them, and return a string with recognized numbers.

As with most other web frameworks, to receive and process HTTP requests Genie.jl uses routes. This application will have two routes: 

```julia
using Genie, Genie.Router, Genie.Requests

route("/") do 
    return String(read("index.html"))
end

route("/api/recognize", method=POST) do
    result = ""
    # TODO: in a loop, extract each image 
    # from POST request body, send it to 
    # the digit recognition function, 
    # receive recognized digit and add 
    # it to the result
    return result
end

up(8080, async=false)
```

To work with routes and requests, you need to import two additional subpackages – `Genie.Router` and `Genie.Requets`. 

The first route just returns the content of the `index.html` file.

The second route processes the POST requests to the `/api/recognize` endpoint. This is how you can define it:

```julia
using Images
route("/api/recognize", method=POST) do
    result = ""
    files = filespayload();   
    for index in 1:11
        file = files["$index.png"]
        img = load(IOBuffer(file.data))
        result *= recognizeDigit(img)        
    end    
    return result
end
```

To load the received file as an image, we will use the Julia Images library that we imported on the first line.

Then, the `[filespayload](https://github.com/GenieFramework/Genie.jl/blob/7eb45c9ec32f0e4659abb08559b0b2729451421a/src/Requests.jl#L50)()` function extracts all files from the received request. 

Then, we assume that the request has 11 files and we process them in a loop. Each file data is extracted as an array of bytes, but the `[load](https://juliaimages.org/stable/function_reference/#FileIO.load)` function requires the object that implements an IO buffer. That is why the `[IOBuffer](https://docs.julialang.org/en/v1/base/io-network/#Base.IOBuffer)` converts the array of bytes to a suitable format. 

Then, the loaded image gets passed to the `recognizeDigit` function. This function will be written below. It should receive the image, then recognize it using the trained model and return the recognized digit as a string. This digit will be appended to the `result` string. Finally, the result with 11 recognized digits will be sent to the web page.

Before writing the `recognizeDigit` function, ensure that the saved model file `digits.bson` was copied to the folder with your backend code.

Also, it's important to understand that we can't process the input image as is because it has a size of 50x50, and it is a black digit on a white background.

If the model trained on images with size 28x28, then it can't be used to recognize images of other sizes. 

Also, the model that trained on images that had white text written on black background will work poorly for colored images and for images with black text on a white background. 

So, before you send the image to the model for recognition, you need to preprocess them using the following steps:

* Convert the images to gray
* Invert the colors
* Resize them to 28x28

Now you are ready to implement the digits recognition function:

```julia
using Flux, MLUtils, BSON
function recognizeDigit(img)
    # load the model
    BSON.@load "digits.bson" model
    # Convert image to grayscale
    img = Gray.(img)
    # Invert each pixel color
    img = (x->Gray(1)-x.val).(img)
    # resize image to 28x28 pixels
    img = imresize(img,(28,28))
    # Get matrix of image
    digit_data = Float32.(channelview(img))
    # predict the digit (get probabilities)
    probs = model(cat(digit_data,dims=4))
    # return the digit with the largest 
    # probability, converted to a string
    return "$(argmax(probs)[1]-1)"
end
```

When all this is done, you are almost ready to run the app. Before doing that, ensure that all required packages are installed. Run the `julia` REPL in a project folder. Then run the following code line by line, to install all packages mentioned in the `using` lines:

```bash
using Pkg
Pkg.add("Genie")
Pkg.add("Images")
Pkg.add("Flux")
Pkg.add("MLUtils")
```

Then exit the repl using the `exit()` command.

Now you can run the app. To do that, either execute the `julia digits.jl` command from the terminal or press Ctrl+F5 in VSCode. 

Then, go to `http://localhost:8080` in a web browser, draw the digits, press the "Recognise" button, and in a few moments you will see the recognised number as a text in the "Result" field.

%[https://youtu.be/e5ScpCggVbs]

<h2 id="conclusion">Conclusion</h2>

In this tutorial, I demonstrated how to create and train both feed forward and convolutional neural networks using Julia. You also learned how to export and use them in a web application.

In addition, I tried to show that you should not reinvent the wheel when creating neural networks.

When solving real life problems, you should not build neural network architectures from scratch. Most of them have already been created by data scientists and enthusiasts around the world. In practice, you will just reuse them. 

You'll just need to find the suitable architecture and either use it as is or change the last few layers to adjust the outputs according to your needs.

For example, you can search [this collection](https://huggingface.co/models) where you'll find different models classified by problem types. Even if many of them were not created with Julia, you can create them using Flux.jl after reading their descriptions.

The way we created and trained our neural network is not the best or the only possible one. Perhaps in some points I oversimplified things, because I wanted to explain all this as simply as possible. 

But if you've understood the examples here, you can learn and reuse the following more advanced Julia solutions of the handwritten digits recognition task:

* [Tutorial: Simple Multi-Layer Perceptron](https://fluxml.ai/Flux.jl/stable/tutorials/2021-01-26-mlp/) 
* [MNIST example in the Julia model-zoo](https://github.com/FluxML/model-zoo/tree/master/vision/conv_mnist)

You can see the source code of this article including the Jupyter Notebook and the web service in [this repository](https://github.com/AndreyGermanov/phones_reader).

Have a fun coding and never stop learning!

You can find me on [LinkedIn](https://www.linkedin.com/in/andrey-germanov-dev/), [Twitter](https://twitter.com/GermanovDev), and [Facebook](https://www.facebook.com/AndreyGermanovDev) to know first about new articles like this one and other software development news.

