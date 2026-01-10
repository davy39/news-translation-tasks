---
title: How to Build a Simple Sentiment Analyzer Using Hugging Face Transformer
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2024-01-26T00:32:04.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-simple-sentiment-analyzer-using-hugging-face-transformer
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/pngtree-facial-emotions-illustration-in-black-outline-on-white-background-vector-picture-image_10574137.png
tags:
- name: natural language processing
  slug: natural-language-processing
- name: nlp
  slug: nlp
- name: Sentiment analysis
  slug: sentiment-analysis
seo_title: null
seo_desc: "In this article, we will look at writing a sentiment analyzer using Hugging\
  \ Face Transformer, a powerful tool in the world of NLP. \nImagine you’re running\
  \ a business and you want to know what your customers think about your product.\
  \ Or maybe you’re a..."
---

In this article, we will look at writing a sentiment analyzer using Hugging Face Transformer, a powerful tool in the world of NLP. 

Imagine you’re running a business and you want to know what your customers think about your product. Or maybe you’re a movie director wanting to gauge the public reaction to your latest release.

This is where sentiment analysis comes into play.

> Sentiment analysis is a technique used in text analysis that helps in identifying and categorizing opinions expressed in a piece of text.

Sentiment analysis determines whether the expressed opinion in a document, a sentence or an entity feature/aspect is positive, negative, or neutral.

In a world where data is king, sentiment analysis is a crown jewel. It’s like having a superpower to understand the emotional tone behind words at scale.

Companies use it to understand customer feedback on products and services. Governments and organizations use it to get a sense of public opinion.

In social media management, sentiment analysis is used for brand monitoring, customer service, and market research.

It’s not just about understanding how many people are talking about your brand or product, but how they feel about it.

## What is Hugging Face?

Now, let’s talk about Hugging Face. No, it’s not what you think. You don’t go around hugging faces.

In the world of AI, [Hugging Face](https://huggingface.co/) is quite the star. It’s an AI community and platform that provides state-of-the-art tools and models for Natural Language Processing (NLP).

Think of it as a toolbox that gives you the power to understand and generate human language. It’s like having a linguistic wizard by your side.

Hugging Face’s most popular offering is the ‘Transformers’ library. The Transformers library comes packed with APIs and tools that let you easily grab and train top-notch pre-trained models.

When you pick these pre-trained models, you’re cutting down on compute costs and carbon footprint. Plus, you save loads of time and resources that you’d otherwise spend training a model from scratch.

These models solve common tasks across various domains, like:

* **Natural Language Processing (NLP)**: Here, you can do a bunch of cool stuff like text classification, spotting names or entities in text, answering questions, language modelling, summarizing, translating, handling multiple-choice questions, and even generating text.
* **Computer Vision:** This involves image classification, spotting and outlining objects in images, and more.
* **Audio:** You can work on recognizing speech automatically and classifying different types of sounds.
* **Multimodal Tasks:** These are tasks that mix it up, like answering questions based on tables, recognizing text in images (like scanned documents), pulling out information from these documents, classifying videos, and answering questions based on images.

The neat thing about Transformers is that they’re flexible with different frameworks. Whether you’re into [PyTorch](https://turingtalks.substack.com/p/pytorch-vs-tensorflow-for-deep-learning), TensorFlow, or JAX, Transformers has got you covered.

Its ease of use and comprehensive nature make it a go-to for researchers, developers, and businesses alike.

## Code for Sentiment Analysis

Now that you know what sentiment analysis and Hugging Face are, let’s write some code. We’ll use Python and the Hugging Face `transformers` library to build a simple sentiment analyzer.

You can either use your terminal, install Python and run the code, or use a [Google Colab notebook](https://colab.research.google.com/). I would recommend the latter since it comes pre-installed with Python.

Install the `transformers`library with this command:

```
pip install transformers
```

If you are using a Colab notebook, use a **!** symbol before the command for the notebook to treat it as a shell command (Colab executes code as Python by default).

```
!pip install transfomers
```

Once the installation is complete, you can start using the library. First, let's import `pipeline` from the transformers library.

```
from transformers import pipeline
```

In Hugging Face, a “pipeline” is like a tool that helps you perform a series of steps to change data into the form you want. The pipeline makes it simple to use these tools for different jobs, without needing to know all the complex details about how these tools work on the inside.

Now let’s load the `sentiment-analysis` pipeline.

```
sentiment_pipeline = pipeline("sentiment-analysis")

```

Now would you believe me if I said we are pretty much done? Our sentiment analysis model is ready and we can pass text to the pipeline and get the label as well as a sentiment score.

```
# Run sentiment analysis
result = sentiment_pipeline("Every new day brings a chance to create joyful memories and embrace new opportunities.")

# Print the result
print(result)
```

This is the output of the above code:

```
[{'label': 'POSITIVE', 'score': 0.9998821020126343}]
```

If you want to pass multiple sentences, pass an array of inputs to the pipeline.

```
result = sentiment_pipeline(["Every new day brings a chance to create joyful memories and embrace new opportunities.","Despite the effort, the project failed to meet expectations, leading to disappointment and frustration among the team."])
print(result)
```

Following will be the output of the above code:

```
[{'label': 'POSITIVE', 'score': 0.9998821020126343}, {'label': 'NEGATIVE', 'score': 0.9997937083244324}]
```

I hope you understand how powerful the Hugging Face Transformer library is. This is just a sample of the many pre-trained models that Hugging Face provides. Unless you are working on a unique problem, you should find a pre-trained model in Hugging Face available for you to work with.

## Summary

In this article, we’ve learned about sentiment analysis and Hugging Face, a powerful tool in the world of NLP. Most importantly, you’ve taken your first steps in performing sentiment analysis by using the Hugging Face Transformers library.

Remember, what we’ve covered is just the tip of the iceberg. The field of NLP is vast and constantly evolving. The Hugging Face Transformers library is a powerful ally in your journey through AI. It simplifies complex tasks and gives you access to pre-trained models, saving you time and resources.

Hope you enjoyed this article. Find more beginner-friendly articles on AI at **[turingtalks.ai](https://www.turingtalks.ai/)**

