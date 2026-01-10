---
title: Google BERT NLP Machine Learning Tutorial
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-27T16:29:34.000Z'
originalURL: https://freecodecamp.org/news/google-bert-nlp-machine-learning-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/BERT-Tutorial.png
tags:
- name: Google
  slug: google
- name: Machine Learning
  slug: machine-learning
- name: nlp
  slug: nlp
seo_title: null
seo_desc: "By Milecia McGregor\nThere are plenty of applications for machine learning,\
  \ and one of those is natural language processing or NLP. \nNLP handles things like\
  \ text responses, figuring out the meaning of words within context, and holding\
  \ conversations wi..."
---

By Milecia McGregor

There are plenty of applications for machine learning, and one of those is natural language processing or NLP. 

NLP handles things like text responses, figuring out the meaning of words within context, and holding conversations with us. It helps computers understand the human language so that we can communicate in different ways.

From chat bots to job applications to sorting your email into different folders, NLP is being used everywhere around us. 

At its core, natural language processing is a blend of computer science and linguistics. Linguistics gives us the rules to use to train our machine learning models and get the results we're looking for.

There are a lot of reasons natural language processing has become a huge part of machine learning. It helps machines detect the sentiment from a customer's feedback, it can help sort support tickets for any projects you're working on, and it can read and understand text consistently. 

And since it operates off of a set of linguistic rules, it doesn't have the same biases as a human would.

Since NLP is such a large area of study, there are a number of tools you can use to analyze data for your specific purposes. 

There's the rules-based approach where you set up a lot of if-then statements to handle how text is interpreted. Usually a linguist will be responsible for this task and what they produce is very easy for people to understand. 

This might be good to start with, but it becomes very complex as you start working with large data sets.

Another approach is to use machine learning where you don't need to define rules. This is great when you are trying to analyze large amounts of data quickly and accurately. 

Picking the right algorithm so that the machine learning approach works is important in terms of efficiency and accuracy. There are common algorithms like [Naïve Bayes](https://scikit-learn.org/stable/modules/naive_bayes.html) and [Support Vector Machines](https://www.freecodecamp.org/news/svm-machine-learning-tutorial-what-is-the-support-vector-machine-algorithm-explained-with-code-examples/). Then there are the more specific algorithms like Google BERT.

## What is BERT?

BERT is an open-source library created in 2018 at Google. It's a new technique for NLP and it takes a completely different approach to training models than any other technique. 

BERT is an acronym for Bidirectional Encoder Representations from Transformers. That means unlike most techniques that analyze sentences from left-to-right or right-to-left, BERT goes both directions using the [Transformer encoder](https://arxiv.org/pdf/1706.03762.pdf). Its goal is to generate a language model.

This gives it incredible accuracy and performance on smaller data sets which solves a huge problem in natural language processing. 

While there is a huge amount of text-based data available, very little of it has been labeled to use for training a machine learning model. Since most of the approaches to NLP problems take advantage of deep learning, you need large amounts of data to train with.

You really see the huge improvements in a model when it has been trained with millions of data points. To help get around this problem of not having enough labelled data, researchers came up with ways to train general purpose language representation models through pre-training using text from around the internet.

These pre-trained representation models can then be fine-tuned to work on specific data sets that are smaller than those commonly used in deep learning. These smaller data sets can be for problems like sentiment analysis or spam detection. This is the way most NLP problems are approached because it gives more accurate results than starting with the smaller data set.

That's why BERT is such a big discovery. It provides a way to more accurately pre-train your models with less data. The bidirectional approach it uses means it gets more of the context for a word than if it were just training in one direction. With this additional context, it is able to take advantage of another technique called masked LM.

## How it's different from other machine learning algorithms

Masked LM randomly masks 15% of the words in a sentence with a [MASK] token and then tries to predict them based on the words surrounding the masked one. That's how BERT is able to look at words from both left-to-right and right-to-left. 

This is completely different from every other existing language model because it looks at the words before and after a masked word at the same time. A lot of the accuracy BERT has can be attributed to this.

To get BERT working with your data set, you do have to add a bit of metadata. There will need to be **token embeddings** to mark the beginning and end of sentences. You'll need to have **segment embeddings** to be able to distinguish different sentences. Lastly you'll need **positional embeddings** to indicate the position of words in a sentence.

It'll look similar to this.

```
[CLS] the [MASK] has blue spots [SEP] it rolls [MASK] the parking lot [SEP]
```

With the metadata added to your data points, masked LM is ready to work. 

Once it's finished predicting words, then BERT takes advantage of next sentence prediction. This looks at the relationship between two sentences. It does this to better understand the context of the entire data set by taking a pair of sentences and predicting if the second sentence is the next sentence based on the original text.

For next sentence prediction to work in the BERT technique, the second sentence is sent through the [Transformer based model](https://ai.googleblog.com/2017/08/transformer-novel-neural-network.html).

There are four different pre-trained versions of BERT depending on the scale of data you're working with. You can learn more about them here: [https://github.com/google-research/bert#bert](https://github.com/google-research/bert#bert)

The drawback to this approach is that the loss function only considers the masked word predictions and not the predictions of the others. That means the BERT technique converges slower than the other right-to-left or left-to-right techniques.

BERT can be applied to any NLP problem you can think of, including intent prediction, question-answering applications, and text classification.

## Code Example

### Getting set up

Now we're going to go through an example of BERT in action. First thing you'll need to do is clone the Bert repo.

```
git clone https://github.com/google-research/bert.git
```

Now you need to download the pre-trained BERT model files from the [BERT GitHub page](https://github.com/google-research/bert#pre-trained-models). Throughout the rest of this tutorial, I'll refer to the directory of this repo as the root directory.

These files give you the hyper-parameters, weights, and other things you need with the information Bert learned while pre-training. I'll be using the [BERT-Base, Uncased model](https://storage.googleapis.com/bert_models/2018_10_18/uncased_L-12_H-768_A-12.zip), but you'll find several other options across different languages on the GitHub page.

Some reasons you would choose the BERT-Base, Uncased model is if you don't have access to a Google TPU, in which case you would typically choose a Base model. 

If you think the casing of the text you're trying to analyze is case-sensitive (the casing of the text gives real contextual meaning), then you would go with a Cased model. 

If the casing isn't important or you aren't quite sure yet, then an Uncased model would be a valid choice.

We'll be working with some Yelp reviews as our data set. Remember, BERT expects the data in a certain format using those **token embeddings** and others. We'll need to add those to a .tsv file. This file will be similar to a .csv, but it will have four columns and no header row. 

Here's what the four columns will look like.

* Column 0: Row id
* Column 1: Row label (needs to be an integer)
* Column 2: A column of the same letter for all rows (it doesn't get used for anything, but BERT expects it)
* Column 3: The text we want to classify

You'll need to make a folder called data in the directory where you cloned BERT and add three files there: _train.tsv, dev.tsv, test.tsv_. 

In the _train.tsv_ and _dev.tsv_ files, we'll have the four columns we talked about earlier. In the _test.tsv_ file, we'll only have the row id and text we want to classify as columns. These are going to be the data files we use to train and test our model.

### Prepping the data

First we need to get the data we'll be working with. You can download the Yelp reviews for yourself here: https://course.fast.ai/datasets#nlp It'll be under the NLP section and you'll want the Polarity version. 

The reason we'll work with this version is because the data already has a polarity, which means it already has a sentiment associated with it. Save this file in the data directory.

Now we're ready to start writing code. Create a new file in the root directory called _pre_processing.py_ and add the following code.

```python
import pandas as pd
# this is to extract the data from that .tgz file
import tarfile
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# get all of the data out of that .tgz
yelp_reviews = tarfile.open('data/yelp_review_polarity_csv.tgz')
yelp_reviews.extractall('data')
yelp_reviews.close()

# check out what the data looks like before you get started
# look at the training data set
train_df = pd.read_csv('data/yelp_review_polarity_csv/train.csv', header=None)
print(train_df.head())

# look at the test data set
test_df = pd.read_csv('data/yelp_review_polarity_csv/test.csv', header=None)
print(test_df.head())
```

![Image](https://www.freecodecamp.org/news/content/images/2020/07/image-44.png)

In this code, we've imported some Python packages and uncompressed the data to see what the data looks like. You'll notice that the values associated with reviews are 1 and 2, with 1 being a bad review and 2 being a good review. We need to convert these values to more standard labels, so 0 and 1. You can do that with the following code.

```python
train_df[0] = (train_df[0] == 2).astype(int)
test_df[0] = (test_df[0] == 2).astype(int)
```

Whenever you make updates to your data, it's always important to take a look at if things turned out right. So we'll do that with the following commands.

```python
print(train_df.head())
print(test_df.head())
```

![Image](https://www.freecodecamp.org/news/content/images/2020/07/image-45.png)

When you see that your polarity values have changed to be what you expected. Now that the data should have 1s and 0s. 

Since we've cleaned the initial data, it's time to get things ready for BERT. We'll have to make our data fit the column formats we talked about earlier. Let's start with the training data.

The training data will have all four columns: row id, row label, single letter, text we want to classify. 

BERT expects two files for training called _train_ and _dev_. We'll make those files by splitting the initial train file into two files after we format our data with the following commands.

```python
bert_df = pd.DataFrame({
    'id': range(len(train_df)),
    'label': train_df[0],
    'alpha': ['q']*train_df.shape[0],
    'text': train_df[1].replace(r'\n', ' ', regex=True)
})

train_bert_df, dev_bert_df = train_test_split(bert_df, test_size=0.01)
```

With the _bert_df_ variable, we have formatted the data to be what BERT expects. You can choose any other letter for the alpha value if you like. The _train_test_split_ method we imported in the beginning handles splitting the training data into the two files we need. 

Take a look at how the data has been formatted with this command.

```python
print(train_bert_df.head())
```

Now we need to format the test data. This will look different from how we handled the training data. BERT only expects two columns for the test data: row id, text we want to classify. We don't need to do anything else to the test data once we have it in this format and we'll do that with the following command.

```python
test_bert_df = pd.DataFrame({
    'id': range(len(test_df)),
    'text': test_df[1].replace(r'\n', ' ', regex=True)
})
```

It's similar to what we did with the training data, just without two of the columns. Take a look at the newly formatted test data.

```python
test_bert_df.head()
```

If everything looks good, you can save these variables as the .tsv files BERT will work with.

```python
train_bert_df.to_csv('data/train.tsv', sep='\t', index=False, header=False)
dev_bert_df.to_csv('data/dev.tsv', sep='\t', index=False, header=False)
test_bert_df.to_csv('data/test.tsv', sep='\t', index=False, header=False)
```

### Training the model

One quick note before we get into training the model: BERT can be very resource intensive on laptops. It might cause memory errors because there isn't enough RAM or some other hardware isn't powerful enough. You could try making the _training_batch_size_ smaller, but that's going to make the model training really slow.

Add a folder to the root directory called _model_output_. That's where our model will be saved after training is finished. Now open a terminal and go to the root directory of this project. Once you're in the right directory, run the following command and it will begin training your model.

```bash
python run_classifier.py --task_name=cola --do_train=true --do_eval=true --data_dir=./data/ --vocab_file=./uncased_L-12_H-768_A-12/vocab.txt --bert_config_file=./uncased_L-12_H-768_A-12/bert_config.json --init_checkpoint=./uncased_L-12_H768_A-12/bert_model.ckpt.index --max_seq_length=128 --train_batch_size=32 --learning_rate=2e-5 --num_train_epochs=3.0 --output_dir=./model_output --do_lower_case=False
```

You should see some output scrolling through your terminal. Once this finishes running, you will have a trained model that's ready to make predictions!

### Making a predication

If you take a look in the _model_output_ directory, you'll notice there are a bunch of _model.ckpt_ files. These files have the weights for the trained model at different points during training so you want to find the one with the highest number. That will be the final trained model that you'll want to use.

Now we'll run _run_classifier.py_ again with slightly different options. In particular, we'll be changing the _init_checkpoint_ value to the highest model checkpoint and setting a new _--do_predict_ value to true. Here's the command you need to run in your terminal.

```bash
python run_classifier.py --task_name=cola --do_predict=true --data_dir=./data --vocab_file=./uncased_L-12_H-768-A-12/bert_config.json --init_checkpoint=./model_output/model.ckpt-<highest checkpoint number> --max_seq_length=128 --output_dir=./model_output
```

Once the command is finished running, you should see a new file called _test_results.tsv_. This will have your predicted results based on the model you trained!

You've just used BERT to analyze some real data and hopefully this all made sense.

## Other thoughts

I felt it was necessary to go through the data cleaning process here just in case someone hasn't been through it before. Sometimes machine learning seems like magic, but it's really taking the time to get your data in the right condition to train with an algorithm.

BERT is still relatively new since it was just released in 2018, but it has so far proven to be more accurate than existing models even if it is slower.


