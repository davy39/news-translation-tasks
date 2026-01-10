---
title: The Difference Between AI and Machine Learning
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-10T22:37:37.000Z'
originalURL: https://freecodecamp.org/news/artificial-intelligence-vs-machine-learning
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/pexels-tara-winstead-8386440--1-.jpg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Machine Learning
  slug: machine-learning
seo_title: null
seo_desc: 'By Edem Gold

  Artificial Intelligence and Machine Learning are two terms that are commonly used
  interchangeably. But they are not the same thing. Artificial Intelligence is a field
  which contains a lot of sub-fields, including Machine Learning.

  In thi...'
---

By Edem Gold

Artificial Intelligence and Machine Learning are two terms that are commonly used interchangeably. But they are not the same thing. Artificial Intelligence is a field which contains a lot of sub-fields, including Machine Learning.

In this article I hope to comprehensively differentiate between AI and Machine Learning. I'll explain how Machine Learning is not the same thing as Artificial Intelligence, but rather a part of it – like a cog amongst many cogs that makes up the machine which is Artificial Intelligence.

## **How I'll approach this**

To begin, I'll discuss the two concepts separately, describe their subsets, and then state the relationship binding the two of them. I'll explain how Machine Learning, as a cornerstone concept, fits into AI as a field. 

Here's a general outline of what we'll cover in this guide:

* **[What is Artificial Intelligence?](#heading-what-is-artificial-intelligence)** Here I will define what Artificial Intelligence is and describe its sub-concepts including Machine Learning and others like Natural Language Processing, Expert Systems, Computer Vision and Robotics.
* **[What is Machine Learning?](#heading-what-is-machine-learning)** In this section, I will define Machine Learning, as a concept, and then describe its sub-concepts, namely supervised learning, unsupervised learning, semi-supervised learning, reinforcement learning, deep learning, transfer learning, online learning, and batch learning.
* **[The Relationship between AI and Machine Learning](#heading-the-relationship-between-ai-and-machine-learning).** Here I plan to describe how Machine works as a subset of Artificial intelligence.

Let's begin!

## What is Artificial Intelligence?

Artificial intelligence is a sub-field of Computer Science. It involves building synthetically intelligent programs that are capable of **[human-level](https://edemgold.substack.com/p/undertanding-the-brain-inspired-approach)** activities, and above all, cognition. 

In simple words, Artificial Intelligence is the ability of computers to perform tasks which are commonly performed by human beings such as writing, driving, and so on.

Artificial intelligence as a field is concerned with building systems which are capable of human-level thinking. It contains various sub-areas which are each responsible for simulating one aspect of human intelligence or behaviour. Let's discuss each of them.

## Sub-Fields of Artificial Intelligence

### Machine Learning

Machine Learning is the sub-field of AI that involves the creation of algorithms and statistical models which are capable of learning from past experience. 

In other words, it is the part of AI which is responsible for teaching AI systems how to act in stated situations by using complex statistical algorithms trained by data on certain situations.

### Natural Language Processing

Natural Language Processing is the subset of AI which is responsible for enabling AI systems to interact using Natural Human Language (for example English). In other words, it is the branch of AI responsible for enabling AI to understand and use spoken words and text. 

NLP involves using statistical models to understand, interpret, and generate human language in a way that is meaningful to human beings. Human language here includes all languages spoken by humans. It is the technology behind chatbots like ChatGPT, Siri, Alexa, and others.

### Expert Systems

Expert Systems are perhaps the most rigid subset of AI due to their use of rules. This area involves the use of explicitly stated rules and knowledge bases in an attempt to imitate the decision-making of an expert in a certain field. 

In other words, it is the use of explicitly stated rules and inference techniques to make informed decisions in specific fields, such as medicine.

### Computer Vision

Computer Vision is the subset of AI which makes use of statistical models to aid computer systems in understanding and interpreting visual information in the environment. 

Computer Vision is essentially how computers "see" things and then understand what they are seeing. It's responsible for the recognition of objects. Computer Vision is (or rather will be) responsible for creating efficient self-driving cars, drones, and so on.

### Robotics

Robotics is essentially the integration of all the above-mentioned concepts. It is the sub-field responsible for making AI systems perceive, process, and act in the physical world. 

Robotics involves using algorithms which can recognize objects in their immediate environment and interpret how interactions with these objects can alter their current state and that of the environment plus the people in it. Robots are used in fields such as medicine, manufacturing, e-commerce (warehouses), and many more.

## What is Machine Learning?

As we discussed earlier, Machine Learning is the part of AI which is responsible for training AI systems how to act in certain situations or while performing certain activities. It does this using complex statistical algorithms trained by data based on the performance of the activities in question, like driving.

In other words, Machine Learning involves feeding a computer raw data. Then, through the use of algorithms, it creates a model from that data which it then uses to make predictions or decisions.

Machine Learning is commonly mistaken to be the same thing as AI. But as we have already seen, it is just a part of Artificial Intelligence as a whole. 

Although Machine Learning is a subset of Artificial Intelligence, it is arguably the most important part of AI. This is mostly due to the simple fact that it is required for the functioning of the other sub-fields (like Natural Language Processing and Computer Vision).

All the other concepts under the AI umbrella require two things before they can function: data and learning algorithms. Before Natural Language processing systems can interact using Natural Human Language, they need data on human language and algorithms to use in learning how to efficiently and correctly apply the language data. 

The art of making AI systems understand how to accurately use the data provided, and in the right context, is all part of Machine Learning.

Machine Learning, like AI, has sub-areas of its own which enable it to function efficiently. Let's explore those now.

### Supervised Learning

Supervised Learning is the subset of Machine Learning which involves training Models to predict an output based on input data and target variables. 

This machine learning technique involves teaching a machine learning model to predict output by giving it data which contains examples of inputs and the resulting outputs. Supervised learning algorithms are then able to find the relationship between the input and output and use that knowledge pattern to build a model.

To fully understand this, let's use an analogy. Imagine you want to build a Supervised Machine Learning model which is capable of predicting if a person has cancer or not.

First you provide a dataset. For the uninitiated, this is a collection of data points. These are in turn just a collection of data instances containing the data of thousands of different patients. The data will contain information like their age, number of children they have, Body Mass Index (BMI), and so on. This will serve as the input. Then for each patient, you provide their results (that is, if they have cancer or not) and this will serve as their output.

The algorithm will then find the relationship between the input and output data. In other words, it will find out what type of people are usually diagnosed with cancer. Then it will provide a statistical representation of its findings in something called a model. 

Note that Supervised Learning is further broken down into 2 sub-areas, Classification and Regression.

### Unsupervised Learning

Unsupervised Learning is the antithesis of Supervised Learning. Rather than providing both input and output data to guide the model, it only provides the input data and lets the algorithm make correlations. 

This is the Machine Learning Technique which involves the algorithm figuring out patterns, structures, and relationships without explicit guidance in the form of labelled output.

Going back to our original cancer analogy, rather than providing the input data of different patients (that is their age, number of children born, Body Mass Index, and so on) and also providing the output data (that is, if they have cancer or not), you only provide the input data and let the model find the correlations in the data on its own.

Note that the two techniques, supervised and unsupervised learning, are each suited to different use cases. Supervised learning is most optimal when there is a stated result (preferably linear), while unsupervised learning is best used when there is no clearly stated result and there is no clear structure in the data.

### Semi-Supervised Learning

Again, supervised learning and unsupervised learning both have their use cases. But there are instances where both of them will need to be employed. 

Semi-supervised learning lies in the schism between supervised and unsupervised learning. As you can imagine, it entails a situation where a model is built using both structured and unstructured data.

Semi-supervised learning exists because of the complicated nature of data collection and data cleaning. While Supervised learning is best in getting accurate results, getting data which contains both input and output requires significant effort in the form of data labelling.

In order to counteract this challenge, engineers decided to structure only part of the data and leave the rest unstructured in an effort to save financial and labour cost. And thus semi-supervised learning was born.

But you should note that semi-supervised learning is more unsupervised than supervised.

### Reinforcement Learning

Reinforcement Learning is a technique used to train models. It was inspired by how human beings learn skills through trial and error. 

Reinforcement learning involves an AI agent receiving rewards or punishments based on its actions. This enables the agent to learn from its mistakes and be more efficient in its future actions (this technique is usually used in creating games).

In simple words, reinforcement learning involves getting AI agents to make decisions based on their environment. It makes this happen by placing these agents in an environment with no prior experience. It rewards them when they make the right decisions and penalizes them when they make the wrong decision

After continuous feedback, the AI agent is able to discern the right actions from the wrong ones. As a result, you get a working model that knows how to act in a certain environment.

Reinforcement Learning is usually used to train game agents.

### Deep Learning

Deep Learning powers most, if not all, of the innovative AI systems popular today – from ChatGPT to Tesla's Self-Driving cars. In order to fully understand how Deep Learning works, you need to understand neural networks.

As discussed in my article on the **[brain-inspired approach to AI](https://edemgold.substack.com/p/undertanding-the-brain-inspired-approach)**, in essence Neural Networks are computational models that mimic the function and structure of biological neurons in the human brain. The networks are made up of various layers of interconnected nodes, called artificial neurons, which aid in the processing and transmitting of information. This is similar to what is done by dendrites, somas, and axons in biological neural networks. 

Neural Networks are architected to learn from past experiences the same way the brain does.

Now Deep Learning, simply, makes use of neural networks to solve difficult problems by making use of more neural network layers. As data is inputted into a deep learning model and passes through each layer of the neural network, the network is better able to understand the data inputted and make more abstract (creative) interpretations of it.

So in basic words, Deep Learning is simply the collection of neural networks, that is the more complex a problem, the more neural networks are involved.

### Transfer Learning

Training Machine Learning Models from scratch is really intensive, both financially and in terms of labour. Because of this, the transfer learning technique was developed. 

In order to circumvent the challenge of building new models from scratch, you can use pre-trained models. Before continuing, it is essential to know that pre-trained models are models which have already been trained for large tasks such as facial recognition.

Here is how transfer learning works: say, for instance, that you want to build a facial recognition Machine Learning model which helps recognize small children. When they want to cross a busy road, a traffic light stops. 

But you do not have the data or financial resources to train a model of that scale. So you decide to import an already pre-trained model that has been trained to recognize a human face. Then you use Transfer Learning to tune the model so it can recognize the faces of small children. That way you can make use of the efficiency and accuracy of a well and heavily-trained model with less effort than would have originally been required.

Transfer Learning is usually implemented in two ways: Fine-Tuning and Feature Extraction.

### Online Learning

Imagine this scenario: you have built a machine learning model that identifies fraudulent transactions and it's being used by banks to ascertain the validity of transactions. After a while, the model needs to be re-trained with new data in order to keep it up to date and accurate with the new techniques for fraud. 

Rather than taking down the model and risking fraudulent transactions, you decide to update it frequently as you get new data points. That way the model is frequently updated and you don't need to pay for storage for accumulating or taking down the model.

In simple words, online learning is a machine learning technique which involves updating a model continuously as new data becomes available. It is useful in scenarios where data is dynamic and constantly changing.

### Batch Learning

Batch Learning is the antithesis of online learning. Going back to our original fraud scenario, rather than re-training the model continuously with new datasets, you train the model in large batches. This means you accumulate the data and then use it to train the model all at once. 

Batch Learning is best used when the data is all available and the goal is to optimize the model's performance.

## The Relationship between AI and Machine Learning

In the previous sections, we covered the differences between AI and Machine learning. But because one concept is a subset of the other, I feel it is just as important to cover the relationship between the two.

AI is, essentially, the study, design, and development of systems which are cognitively capable of performing actions, activities, and tasks which can be performed by humans. It does this by being trained on datasets which contain data on how these actions, activities, and tasks are performed.

Machine Learning is the part of AI which is involved in taking these datasets and, through the use of advanced statistical algorithms such as Linear Regression, training a model. That model will then serve as the foundation of how the AI System understands the data and, as a consequence. how it performs the actions which it was trained to do.

I believe an analogy will be helpful here to help you see how a real-life AI project is carried out. This should help explain the role Machine Learning plays in the development of Artificial Intelligence.

Building an AI system is similar to building a car, and Machine Learning is like the engine that powers it. Just as a car needs an engine to generate power and drive it forward, an AI system needs Machine Learning to process data and make accurate predictions.

For instance, to build an AI system that helps predict cancer, Machine Learning algorithms are used to analyze large amounts of medical data, identify patterns, and make predictions about whether a patient has cancer or not. This process is like the engine of the car (Machine Learning Model), which converts fuel (data) into motion and powers the vehicle (AI system) forward.

As more data is fed into the system and the Machine Learning algorithms become more refined, the AI cancer classification system becomes more accurate and reliable. This is similar to how a car becomes more efficient and powerful as the engine is optimized and fine-tuned over time.

## **Summary**

When treated separately, AI and Machine Learning are two related and seemingly similar concepts. This could lead to some confusion, resulting in using the two terms interchangeably.

But as you've learned here, AI and Machine Learning are not synonyms of each other. Rather, Machine Learning is a subset of AI. This means that AI has many other sub-fields such as Natural Language Processing.

The relationship between AI and Machine Learning is similar to building a car, and Machine Learning is like the engine that powers it. Just as a car needs an engine to generate power and drive it forward, an AI system needs Machine Learning to process data and make accurate predictions.

If you enjoyed my article, consider subscribing to my free [newsletter](https://www.freecodecamp.org/news/p/928b7e57-a111-406b-9ca5-716ada72258b/edemgold.substack.com)!

