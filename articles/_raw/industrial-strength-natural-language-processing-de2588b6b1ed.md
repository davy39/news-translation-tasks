---
title: Industrial strength Natural Language Processing
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-26T18:30:49.000Z'
originalURL: https://freecodecamp.org/news/industrial-strength-natural-language-processing-de2588b6b1ed
coverImage: https://cdn-media-1.freecodecamp.org/images/1*kDvyUe6tJfUu36Q6p2KvTg.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Kavita Ganesan

  I have spent much of my career as a graduate student researcher, and now as a Data
  Scientist in the industry. One thing I have come to realize is that a vast majority
  of solutions proposed both in academic research papers and in the...'
---

By Kavita Ganesan

I have spent much of my career as a graduate student researcher, and now as a Data Scientist in the industry. One thing I have come to realize is that a vast majority of solutions proposed both in academic research papers and in the workplace are just not meant to ship — they just don’t scale!

And when I say scale, I mean:

* Handling **real world** uses cases
* Handling **large amounts** of data
* Ease of **deployment** in a production environment.

Some of these approaches either work on extremely narrow use cases, or have a tough time generating results in a timely manner.

More often than not, the problem lies is in the approach that was used although when things go wrong, we tend to render the problem “unsolvable”. Remember, there will almost always be more than one way to solve a Natural Language Processing (NLP) or Data Science problem. Optimizing your choices will increase your chance of success in deploying your models to production.

Over the past decade I have shipped solutions that serve real users. From this experience, I now follow a set of best practices that maximizes my chance of success every time I start a new NLP project.

In this article, I will share some of these with you. I swear by these principles and I hope these become handy to you as well.

### 1. KISS please!

![Image](https://cdn-media-1.freecodecamp.org/images/1XNrUYvRw3Ilooemmmyz3J17pu0p41S9vgCS)

[KISS (Keep it simple, stupid)](https://en.wikipedia.org/wiki/KISS_principle). When solving NLP problems, this seems like common sense.

But I can’t say this enough: choose techniques and pipelines that are easy to understand and maintain. Avoid complex ones that only you understand, sometimes only partially.

In a lot of NLP applications, you would typically notice one of two things:

1. Deep pre-processing layers, OR
2. Complex neural network architectures that are just hard to grasp, let alone train, maintain and improve on iteratively.

The first question to ask yourself is if you need all the layers of pre-processing?

Do you really need part-of-speech tagging, chunking, entity resolution, lemmatization and etc. What if you strip out a few layers? How does this affect the performance of your models?

With access to massive amounts of data, you can often actually let the evidence in the data guide your model.

Think of [Word2Vec](https://en.wikipedia.org/wiki/Word2vec). The success of Word2Vec is in its simplicity. You use large amounts of data to draw meaning — using the data itself. Layers? What layers?

When it comes to Deep Learning, use it wisely. Not all problems benefit from Deep Learning. For the problems that do, use the architectures that are easy to understand and improve on.

For example, for a programming language classification task, I just used a two-layer Artificial Neural Network and realized big wins in terms of training speed and accuracy.

In addition, adding a new programming language is pretty seamless, as long as you have data to feed into the model.

I could have complicated the model to gain some social currency by using a really complex RNN architecture straight from a research paper. But I ended up starting simple just to see how far this would get me, and now I’m at the point where I can say, what’s the need to add more complexity?

### 2. When in doubt, use a time-tested approach

![Image](https://cdn-media-1.freecodecamp.org/images/gLMrdH1IGQKjRssKwsV9p6ymkC53mi4-wfsZ)
_Things can’t go awfully wrong with time-tested approaches_

With every NLP/text mining problem, your options are plenty. There will always be more than one way to accomplish the same task.

For example, in finding similar documents, you could use a simple bag-of-words approach and compute document similarities using the resulting [tf-idf](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) vector.

Alternatively, you could do something fancier by generating embeddings of each document and compute similarities using the document embeddings.

Which should you use? It actually depends on several things:

1. Which of these methods have seen a higher chance of success in practice? (Hint: We see tf-idf being used all the time for information retrieval and it is super fast. How does the embedding option compare?)
2. Which of these do I understand better? Remember the more you understand something, the better your chance of tuning it and getting it to work the way you expect it to.
3. Do I have the necessary tools/data to implement either of these?

Some of these questions can be easily answered with some literature search.

But you could also reach out to experts such as university professors or other data scientists who have worked on similar problems to give you a recommendation. Occasionally, I run my ideas by my peers who are in the same field to make sure I am thinking about problems and potential solutions correctly, before diving right in.

As you get more and more projects under your belt, the intuition factor kicks in. You will develop a very strong sense about what’s going to work and what’s not.

### 3. Understand your end-point extremely well

![Image](https://cdn-media-1.freecodecamp.org/images/ynwV1R1197WSvTb0oVgHmPVLhnbaXw9Pm6hE)

My work on [topics for GitHub](https://githubengineering.com/topics/) initially started off as topics for the purpose of repository recommendations. Those topics would have never been exposed to the user. They were only intended to be internally used to compute repo to repo similarity.

During development, people got really excited and suggested that these should be exposed to users directly. My immediate response was “Heck, no!”. But people wondered, why not?

Very simple, that was not the intended use of those topics. The level of noise tolerance for something you would use only internally is much higher than what you show to users as suggestions, externally.

So in the case of topics, I actually spent three additional months improving the work so that it can actually be exposed to users.

I can’t say this enough, but you need to know what your end goal is so that you are actually working towards providing a solution that addresses the problem.

Fuzziness in the end goal your are trying to achieve can result in either a **complete redo**, or **months of extra work** tuning and tweaking your models to do the right thing.

### 4. Pay attention to your data quality

![Image](https://cdn-media-1.freecodecamp.org/images/Q4nrwNbxBOKz1RtKmQETssIbuG01JinLbOzj)

> “Garbage in, garbage out” is true in every sense of the word when it comes to machine learning and NLP.

If you are trying to make predictions of sentiment classes (positive versus negative) and your positive examples contain a large number of negative comments and vice versa, your classifier is going to be confused.

Imagine if I told you `1+2=3` and the next time I tell you `1+2=4` and the next time I tell you again `1+2=3`. Ugh, wouldn’t you be so confused? It’s the same analogy.

Also, if you have 90% positive examples and 10% negative ones, how well do you think your classifier is going to perform on negative comments? It’s probably going to say every comment is a positive comment.

Class imbalance and lack of diversity in your data can be a real problem. The more diverse your training data, the better it will generalize.

This was very evident in one of my research projects on [clinical text segmentation](http://kavita-ganesan.com/wp-content/uploads/2017/10/stat-segment.pdf). When we forced variety in training examples, the results clearly improved.

While over-processing your data may be unnecessary, under-processing it may also be detrimental.

Let’s take Tweets for example. Tweets are highly noisy. You may have out-of-vocabulary words like `looooooove` and abbreviations like `lgtm`.

To make sense of any of this, you would probably would need to bring these back to their normal form first. Without that, this would fall right into the trap of garbage-in-garbage-out especially if you are dealing with a fairly small dataset.

### 5. Don’t completely believe your quantitative results.

![Image](https://cdn-media-1.freecodecamp.org/images/9WL1Q3Pbo6EWDT3S67TVGyCixTXB0wzplLQH)
_Doubt your quantitative results_

Numbers can sometimes lie.

For example, in a text summarization project, the overlap between your machine learning summary and the human-curated summary may be a 100%.

However, when you actually visually inspect the machine and human summaries, you might find something astonishing.

**The human says**: _“this is a great example of a bad summary”_.   
**The machine says**: _“example great this is summary a bad a of”_

And your overlap score would still be 100%. See my point? Quantitative evaluation alone is not enough!

You need to **visually inspect your results** — and lots of it. Try to intuitively understand the problems that you are seeing. That’s one excellent way of getting more ideas on how to tweak your algorithm or ditch it altogether

In the summarization example, the problem was obvious: the word arrangement needs a lot of work!

### 6. Think about cost and scalability.

![Image](https://cdn-media-1.freecodecamp.org/images/rMebIkecS0sr9JV5PbWUU2vl39WEI4uW194o)

Have you ever thought about what it would take to deploy your model in a production environment?

* What are your data dependencies?
* How long does your model take to run?
* How about time to predict or generate results?
* Also, what are the memory and computation requirements of your approach when you scale up to the real number of data points that it would be handling?

All of these have a direct impact on whether you can afford to use your proposed approach, and secondly, if you will be able to handle a production load.

If your model is GPU bound, make sure that you are able to afford the cost of serving such a model.

The earlier you think about cost and scalability, the higher your chance of success in getting your models deployed.

In my projects, I always instrument time to train, classify and process different loads to approximate how well the solutions that I am developing would hold up in a production environment.

### Long story short…

The prototypes you develop don’t at all have to be throwaway prototypes. It can be the start of some really powerful production level solution if you plan ahead.

Think about your end-point and how the output from your approach will be consumed and used. Don’t over-complicate your solution. You will not go wrong if you [KISS](https://en.wikipedia.org/wiki/KISS_principle) and pick a technique that fits the problem instead of forcing your problem to fit your chosen technique!

**_I write about Text Mining, NLP and Machine Learning from an applied perspective. [Follow my blog](http://kavita-ganesan.com/subscribe/#.XGs_lpNKigQ) to keep learning._**

**_This article was originally published at [kavita-ganesan.com](http://kavita-ganesan.com/how-to-build-text-mining-and-nlp-models-that-ship-i-e-serve-the-real-world/#.XGs_vJNKigQ)_**

