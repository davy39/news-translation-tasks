---
title: Machine Learning For Managers  – What You Need To Know
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2020-08-12T18:26:04.000Z'
originalURL: https://freecodecamp.org/news/machine-learning-for-managers-what-you-need-to-know
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/ml.jpg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Deep Learning
  slug: deep-learning
- name: Machine Learning
  slug: machine-learning
- name: Product Management
  slug: product-management
seo_title: null
seo_desc: 'If you are managing a tech team as a product or project manager, here is
  what you need to know about machine learning.

  Machine learning and deep learning have been popular buzz words for the last five
  years. The demand for .ai domains has skyrocketed...'
---

If you are managing a tech team as a product or project manager, here is what you need to know about machine learning.

Machine learning and deep learning have been popular buzz words for the last five years. The demand for .ai domains has skyrocketed. 

But beyond all the hype surrounding machine learning, it is hard to grasp the basic concepts with ease if you are an absolute beginner.

Given the pervasive nature of ML and AI, almost every product can have a machine learning use case now. So in this article, we'll look at machine learning in-depth and equip you with the knowledge you need for your next technical conversation.

## What is Machine Learning?

Machine learning is a branch of Artificial Intelligence. Artificial Intelligence as a whole includes many general concepts that aim to simulate human thinking. 

Machine learning focuses only on one key aspect: making machines learn.

> Machine learning is the science of getting computers to make decisions without being explicitly programmed.

In the past decade, machine learning has given us self-driving cars, face recognition, chatbots, and many other useful applications. Machine learning is powering so many tools that we use on a daily basis.

## How Does Machine Learning Work?

Machine learning uses algorithms to analyze massive amounts of data and draw conclusions from it. When you combine large data sets with high computing power, these algorithms can understand patterns and relationships between data.

For example, let's look at a simple dataset:

x = 1,2,3,4,5

y = 1,4,9,16,25

If you look at the above numbers, you'll see that the relationship between x and y is that y is a square of x (that is, y = x²).

In machine learning, the job of an algorithm is to find this function that defines the relationship between the input and output. Once this function has been established, it is easy to predict future values.

For example, if x is 10, y is 100.

Though this example is too simple, it should give you an idea of how machine learning models work.

Consider a complex dataset like predicting housing prices.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/1.png)

This dataset will contain area codes, square footage, and many other inputs with the price as the output. If you have a dataset with thousands of these input features and the final price, you can train a model to predict the average price based on new inputs.

Machine learning problems usually involve finding the relationship between the inputs and outputs to find the ‘hypothesis function’. In our earlier example, the hypothesis function was y = x².

Real-world hypothesis functions are much more complex than this. We then use that function to find answers for custom inputs.

In a nutshell, machine learning, in most cases, is advanced statistics combined with computational capacity. Today, machine learning powers technologies like facial recognition, [sentiment analysis](https://medium.com/manishmshiva/a-complete-guide-to-sentiment-analysis-and-its-applications-72adb3b057f5), and many others.

## Types of Learning Algorithms

Let's look at the type of problems you will come across when working with machine learning. Firstly, there are three ways by which you can make machines learn.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/ml-1.png)

### Supervised Learning

In supervised learning, you provide clear inputs to a machine learning algorithm. The algorithm knows what to learn from the data and the conclusions expected from it.

For example, for recognizing the difference between a cat and a dog, you train an algorithm with thousands of images. Each of these images will be labeled accordingly.

Once you run this data through the algorithm, the algorithm learns and understands the differences. Thus, it can predict, with reasonable accuracy, whether a new image is a cat or a dog.

### Unsupervised Learning

Labeling data is important to build a supervised model. However, companies collect large datasets on a daily basis. Labeling these datasets to make the job of a machine learning model easier is not an elegant way to approach this problem.

This is where unsupervised learning comes in. You can use unsupervised learning algorithms to cluster data based on available attributes. This data can then be fed into supervised learning models to achieve higher prediction accuracy.

Unsupervised learning models are more challenging than supervised learning models. [You can find more information and examples here](https://www.mathworks.com/discovery/unsupervised-learning.html), and you can l[earn more about important machine learning algorithms here](https://www.freecodecamp.org/news/a-no-code-intro-to-the-9-most-important-machine-learning-algorithms-today/).

### Reinforcement Learning

No machine learning algorithm is 100% accurate. The level of accuracy depends on the dataset you train the algorithm with.

This means that after you train an algorithm, there can be new datasets available. These datasets might have the potential to improve the accuracy of your model considerably.

You can use reinforcement learning for these types of scenarios. Reinforcement learning is the concept of updating the algorithm while it is in production. Reinforcement learning models can retrain based on new inputs.

For example, a self-driving car can learn about a new type of terrain after it has traveled through that terrain. This will be taken into account by the self-driving car’s algorithm the next time it has to choose a route.

## Types of Machine Learning Problems

Machine Learning problems can be classified into four subcategories based on the type of result you are looking for.

### Classification

Classification models produce a result that belongs to a finite set. Examples of classification models include spam/not spam, 0 or 1 (binary classification), positive/negative/neutral, and so on.

### Regression

Regression models produce results that belong to a range. Examples include predicting stock market prices, weather forecasting, and more. These are not limited to a finite set of values and hence are called regression problems.

### Clustering

Clustering is a key concept in unsupervised learning. Clustering helps you group data that have similar attributes. Once these groups have been established, it becomes easier to train them using supervised models. 

[Learn more about clustering here](https://www.freecodecamp.org/news/how-to-build-and-train-k-nearest-neighbors-ml-models-in-python/).

### Dimensionality Reduction

Dimensionality Reduction is another unsupervised learning technique. Using Dimensionality reduction, you can reduce a complex dataset with thousands of features into a simple one with maybe a hundred inputs.

Similar to clustering, dimensionality reduction is often used to reduce noise from large datasets before feeding them into supervised training models. 

[You can find a more in-depth article on Dimensionality reduction here](https://machinelearningmastery.com/dimensionality-reduction-for-machine-learning/).

## What is Deep Learning?

![Image](https://www.freecodecamp.org/news/content/images/2020/08/1-1.png)

Deep learning is Machine learning on steroids.

There are many algorithms in machine learning. One that stands out is a Neural Network.

The difference between other machine learning algorithms and a neural network is that you can stack neural networks together — as many as you want.

This helps us solve complex problems like facial recognition and self-driving since these types of problems come with thousands of inputs in real-time. 

Using neural networks, you can solve almost any complex problem with high accuracy, if you have the data and computing power needed for the model to run.

Neural networks have been around for decades, but it was the availability of large datasets and computing power that bought them back to life. Now deep learning is one of the most exciting fields in the industry.

## Why Do You Need Machine Learning?

Let's look at some popular machine learning solutions that we use every day.

### Voice assistants

![Image](https://www.freecodecamp.org/news/content/images/2020/08/siri.png)

Ever wondered how Siri can understand and interpret your voice commands? The answer is machine learning. You can find a voice assistant in almost every smartphone now, thanks to the advancements in [Natural Language Processing](https://www.freecodecamp.org/news/learn-natural-language-processing-no-experience-required/).

Even though it is hard for computers to understand natural language, thanks to machine learning, we have Alexa, Cortana, and Siri.

### Product recommendations

![Image](https://www.freecodecamp.org/news/content/images/2020/08/product.jpg)

Recommendation engines are a profitable use case for e-commerce companies. If you can find the right products to recommend, chances are your customer will make multiple purchases.

Machine learning algorithms can understand user behavior from past purchases. This helps them recommend similar products when a customer is shopping on your website.

Recommendations are not limited to e-commerce. This applies to products like Spotify or Netflix that recommend the music or movies you like.

### Chatbots

![Image](https://www.freecodecamp.org/news/content/images/2020/08/chatbot.png)

Customer support can make or break your company, especially if you are a startup. The more users you attract, the more customer support you have to provide.

Chatbots are a huge time saver when it comes to interacting with customers. Since the majority of your customers will have common questions, you can design a chatbot that can answer redundant questions.

You don't have to employ additional customer service professionals or make your customers wait in a queue. Chatbots are saving businesses time and money, thanks to Machine Learning.

### Spam filtering

![Image](https://www.freecodecamp.org/news/content/images/2020/08/spam.png)

Spam filtering is a simple yet powerful application of Machine Learning. It is the reason why Gmail or Outlook can filter out spam emails for you with high accuracy.

Spam filtering systems are also built to learn from experience. This model, also called reinforcement learning, can understand your preferences better when you mark an email as spam.

We now have cleaner inboxes, thanks to Machine Learning.

### Language translation

![Image](https://www.freecodecamp.org/news/content/images/2020/08/language-1.jpeg)

What would we do without Google Translate? Machine learning-based language translation engines save businesses millions every year.

Before machine learning, translation services were entirely human-powered. Thanks to machine learning, you can translate large data sets to any language in a matter of mere minutes.

## Tools and Frameworks

Machine learning and deep learning are accomplished by using different libraries and frameworks. Though other languages have their own tools, Python is usually the preferred language for machine learning.

Here are a few Python frameworks you can use to build your next machine learning or deep learning product.

* [Scikit-learn](https://scikit-learn.org/) — Popular for machine learning problems. Great community support. Not suitable for complex deep learning models.
* [Tensorflow](https://www.tensorflow.org/) — Most popular deep learning framework. Built by Google. Supports all complex deep learning models like CNNs and RNNs
* [PyTorch](https://pytorch.org/) — Built by Facebook, scalable, and offers high performance.

[I recently wrote a blog post on popular deep learning frameworks if you are interested](https://medium.com/manishmshiva/a-detailed-comparison-of-the-popular-deep-learning-frameworks-a0f65fddf276).

## Conclusion

Machine learning has the potential to transform every industry. From voice assistants to self-driving cars, the applications of machine learning are all around us today. It can help you understand your customers better and make smarter decisions with data.

I hope this article helped you get a good grasp of machine learning and deep learning concepts. If you are fascinated by machine learning as much as I am, check out the [Machine Learning course on Coursera](https://www.coursera.org/learn/machine-learning) by Prof. Andrew Ng.

_I regularly write about Machine Learning, Cyber Security, and DevOps. You can signup for my_ [_weekly newsletter_](https://www.manishmshiva.com/) _here._

