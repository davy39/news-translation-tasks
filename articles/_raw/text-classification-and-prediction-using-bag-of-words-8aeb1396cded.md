---
title: Text classification and prediction using the Bag Of Words approach
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-23T21:40:55.000Z'
originalURL: https://freecodecamp.org/news/text-classification-and-prediction-using-bag-of-words-8aeb1396cded
coverImage: https://cdn-media-1.freecodecamp.org/images/1*wdtdcVQQRzc7xPNZzyCsUg.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: scikit learn
  slug: scikit-learn
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By gk_

  There are a number of approaches to text classification. In other articles I’ve
  covered Multinomial Naive Bayes and Neural Networks.

  One of the simplest and most common approaches is called “Bag of Words.” It has
  been used by commercial analyt...'
---

By gk_

There are a number of approaches to text classification. In other articles I’ve covered [Multinomial Naive Bayes](https://chatbotslife.com/text-classification-using-algorithms-e4d50dcba45) and [Neural Networks](https://machinelearnings.co/text-classification-using-neural-networks-f5cd7b8765c6).

One of the simplest and most common approaches is called “Bag of Words.” It has been used by commercial analytics products including [Clarabridge](https://www.clarabridge.com/), [Radian6](https://www.webanalyticsworld.net/analytics-measurement-and-management-tools/radian-6-overview), and others.

![Image](https://cdn-media-1.freecodecamp.org/images/1*j3HUg18QwjDJTJwW9ja5-Q.png)
_Image [source](https://machinelearnings.co/text-classification-using-neural-networks-f5cd7b8765c6" rel="noopener" target="_blank" title=")._

The approach is relatively simple: given a set of topics and a set of terms associated with each topic, determine which topic(s) exist within a document (for example, a sentence).

While other, more exotic algorithms also organize words into “bags,” in this technique we don’t create a model or apply mathematics to the way in which this “bag” intersects with a classified document. A document’s classification will be polymorphic, as it can be associated with multiple topics.

Does this seem too simple to be useful? Try it before you jump to conclusions. In NLP, it is often the case that a simple approach can sometimes go a long way.

![Image](https://cdn-media-1.freecodecamp.org/images/1*aIUBmmPz2K44OdZnWCj4jw.png)
_credit: Smitha Milli [https://twitter.com/smithamilli](https://twitter.com/smithamilli/status/837153616116985856" rel="noopener" target="_blank" title=")_

We will need three things:

* A topics/words definition file
* A classifier function
* A notebook to test our classifier

And then we will venture a bit further and build and test a predictive model using our classification data.

#### Topics and Words

Our definition file is in JSON format.We will use it to classify messages between patients and a nurse assigned to their care.

#### topics.json

There are two items of note in this definition.

First, let’s look at some terms some terms. For example, “bruis” is a **stem.** It will cover supersets such as “bruise,” “bruising,” and so on. Second, terms containing ***** are actually **patterns**, for example ***dpm** is a pattern for a numeric **d**igit followed by “pm.”

To keep things simple, we are only handling numeric pattern matching, but this could be expanded to a broader scope.

This ability of finding patterns within a term is very useful to when classifying documents containing dates, times, monetary values, and so on.

Let’s try out some classification.

The classifier returns a JSON result set containing the sentence(s) associated with each topic found in the message. A message can contain multiple sentences, and a sentence can be associated with none, one, or multiple topics.

Let’s take a look at our classifier. The code is [here](https://github.com/ugik/notebooks/blob/master/msgClassify.py).

#### msgClassify.py

The code is relatively straightforward, and includes a convenience function to split a document into sentences.

#### Predictive Modeling

The aggregate classification for **a set of documents associated with an outcome** can be used to build a predictive model.

In this use-case, we wanted to see if we could predict hospitalizations based on the messages between patient and nurse prior to the incident. We compared messages for patients who did and did not incur hospitalizations.

You could use a similar technique for other types of messaging associated with some binary outcome.

This process takes a number of steps:

* A set of messages are classified and each topic receives a count for this set. The result is **a fixed list of topics with a % allocation from the messages.**
* The topic allocation is then **assigned a binary value**, in our case a 0 if there was no hospitalization and a 1 if there was a hospitalization
* A **logistic Regression** algorithm is used to build a predictive model
* The model is used to **predict the outcome from new input**

Let’s look at our input data. Your data should have a similar structure. We’re using a pandas [DataFrame](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html).

![Image](https://cdn-media-1.freecodecamp.org/images/1*SRMLWhU-cEgK_ludaN9gMQ.png)

**“incident”** is the binary outcome, and it needs to be the first column in the input data.

Each subsequent column is a topic and the % of classification from the set of messages belonging to the patient.

In row 0, we see that roughly a quarter of the messages for this patient are about the **thanks** topic, and none are about **medical terms** or **money**. Thus each row is a binary outcome and a **messaging classification profile** across topics.

Your input data will have different topics, different column labels, and a different binary condition, but otherwise will be a similar structure.

![Image](https://cdn-media-1.freecodecamp.org/images/1*SE1UtYrUBvtca6qmwN3P2g.png)

Let’s use [scikit-learn](http://scikit-learn.org/stable/) to build a Logistic Regression and test our model.

Here’s our output:

```
precision    recall  f1-score   support          0       0.66      0.69      0.67       191          1       0.69      0.67      0.68       202avg / total       0.68      0.68      0.68       393
```

The [precision and recall](https://en.wikipedia.org/wiki/Precision_and_recall) of this model against the test data are in the high-60’s — **slightly better than a guess**, and not accurate enough to be of much value, unfortunately.

In this example, the amount of data was relatively small (a thousand patients, ~30 messages sampled per patient). Remember that only half of the data can be used for training, while the other half (after shuffling) is used to test.

By including structured data such as age, gender, condition, past incidents, and so on, we could strengthen our model and produce a stronger signal. Having more data would also be helpful as the number of training data columns is fairly large.

Try this with your structured/unstructured data and see if you can get a highly predictive model. You may not get the kind of precision that leads to automated actions, but a “risk” probability could be used as a filter or sorting function or as an early warning sign for human experts.

The “Bag of Words” approach is suitable to certain kinds of text classification work, particularly where the language is not nuanced.

**Enjoy.**

