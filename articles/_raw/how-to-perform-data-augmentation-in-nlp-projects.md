---
title: How to Perform Data Augmentation in NLP Projects
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-06-24T15:33:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-perform-data-augmentation-in-nlp-projects
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/1_eproIleJllsp0enh6HA2Hw.jpeg
tags:
- name: data analysis
  slug: data-analysis
- name: data analytics
  slug: data-analytics
- name: Machine Learning
  slug: machine-learning
- name: natural language processing
  slug: natural-language-processing
- name: nlp
  slug: nlp
seo_title: null
seo_desc: "By Davis David\nIn machine learning, you need to have a large amount of\
  \ data in order to achieve strong model performance. \nUsing a method known as data\
  \ augmentation, you can create more data for your machine learning project. Data\
  \ augmentation is a c..."
---

By Davis David

In machine learning, you need to have a large amount of data in order to achieve strong model performance. 

Using a method known as data augmentation, you can create more data for your machine learning project. Data augmentation is a collection of techniques that manage the process of automatically generating high-quality data on top of existing data.

In computer vision applications, augmenting approaches are quite common. If you are working on a computer vision project (like image classification), for instance, you can apply dozens of techniques to each image: shift, modify color intensities, scale, rotate, crop, and more.

If you have a tiny dataset for your ML project or wish to reduce overfitting in your machine learning models, it may be a good idea to apply data augmentation approaches.

> “We don’t have better algorithms. We just have more data.”- Peter [Norvig](https://research.google/people/author205/?ref=hackernoon.com)

In the field of Natural Language Processing (NLP), the tremendous complexity of language makes it difficult to augment the text. The process of augmenting text data is more challenging and not as straightforward as you might expect.

In this article, you will learn how to use a library called [TextAttack](https://github.com/QData/TextAttack?ref=hackernoon.com) to improve data for natural language processing.

## What is TextAttack?

TextAttack is a Python framework that was built by the [QData team](https://qdata.github.io/qdata-page/?ref=hackernoon.com) for the purpose of conducting adversarial attacks, adversarial training, and data augmentation in natural language processing. 

TextAttack has components that can be utilized independently for a variety of basic natural language processing tasks, including sentence encoding, grammar checking, and word substitution.

TextAttack excels in performing the following three functions:

1. Adversarial attacks (Python: `**textattack.Attack**`, Bash: `**textattack attack**`).
2. Data augmentation (Python: `**textattack.augmentation.Augmenter**`, Bash: `**textattack augment**`).
3. Model training (Python: `**textattack.Trainer**`, Bash: `**textattack train**`).

For this article, we will focus on how to use the TextAttack library for data augmentation.

## How to Install TexAttack

To use this library, make sure you have Python 3.6 or above in your environment.

Run the following command to install textAttack:

```python
pip install textattack
```

**Note:** Once you have installed TexAttack, you can run it via the Python module or via the command line.

## Data Augmentation Techniques for Text Data

The TextAttack library has various augmentation techniques that you can use in your NLP project to add more text data. 

Here are some of the techniques that you can apply:

### `CharSwapAugmenter` technique

This technique augments words by swapping characters out for other characters.

```python
from textattack.augmentation import CharSwapAugmenter

text = "I have enjoyed watching that movie, it was amazing."

charswap_aug = CharSwapAugmenter()

charswap_aug.augment(text)
```

[‘I have enjoyed watching that omvie, it was amazing.’]

The Augmenter has swapped the word **“movie”** for **“omvie”**.

### `DeletionAugmenter` technique

This one augments the text by deleting some parts of the text to make new text.

```python
from textattack.augmentation import DeletionAugmenter

text = "I have enjoyed watching that movie, it was amazing."

deletion_aug = DeletionAugmenter()

deletion_aug.augment(text)
```

[‘I have watching that, it was amazing.’]

This method has removed the word **“enjoyed”** to create a new augmented text.

### `EasyDataAugmenter` technique

This augments the text with a combination of different methods, such as:

* Randomly swapping the positions of the words in the sentence.
* Randomly removing words from the sentence.
* Randomly inserting a random synonym of a random word at a random location.
* Randomly replacing words with their synonyms.

```python
from textattack.augmentation import EasyDataAugmenter

text = "I was billed twice for the service and this is the second time it has happened"

eda_aug = EasyDataAugmenter()

eda_aug.augment(text)
```

[‘I was billed twice for the service and this is the second time it has happen’, ‘I was billed twice for the one service and this is the second time it has happened’, ‘I billed twice for the service and this is the second time it has happened’,  
‘I was billed twice for the this and service is the second time it has happened’]

As you can see from the augmented texts, it shows different results based on the methods applied. For example in the first augmented text, the last word has been modified from **“happened”** to **“happen”**.

### `WordNetAugmenter` technique

This technique can augment the text by replacing it with synonyms from the WordNet thesaurus.

```python
from textattack.augmentation import WordNetAugmenter

text = "I was billed twice for the service and this is the second time it has happened"

wordnet_aug = WordNetAugmenter()

wordnet_aug.augment(text)
```

[‘I was billed twice for the service and this is the second time it has pass’]

This method has changed the word **“happened”** to **“pass”** in order to create a new augmented text.

### How to Create Your Own Augmenter

Importing transformations and constraints from `textattack.transformations` and `textattack.constraints` allows you to build your own augmenter from the ground up. 

The following is an illustration of the use of the `WordSwapRandomCharacterDeletion` algorithm to produce augmentations of a string:

```python
from textattack.transformations import WordSwapRandomCharacterDeletion
from textattack.transformations import CompositeTransformation
from textattack.augmentation import Augmenter

my_transformation = CompositeTransformation([WordSwapRandomCharacterDeletion()])
augmenter = Augmenter(transformation=my_transformation, transformations_per_example=3)

text = 'Siri became confused when we reused to follow her directions.'

augmenter.augment(text)
```

[‘Siri became cnfused when we reused to follow her directions.’, ‘Siri became confused when e reused to follow her directions.’, ‘Siri became confused when we reused to follow hr directions.’]

The output shows different augmented texts after implementing the `WordSwapRandomCharacterDeletion` method. For example, in the first augmented text, the method randomly removes the character “**o”** in the word “**confused”.**

## Conclusion

In this article, you have learned the significance of data augmentation for your Machine Learning projects. You've also learned how to execute data augmentation for textual data using the TextAttack library.

To the best of my knowledge, these techniques are the most effective approaches available to do the task for your NLP project. Hopefully they’ll be of use to you in your work.

You can also try to use other available augmentation techniques from the TextAttack library such as:

* EmbeddingAugmenter
* CheckListAugmenter
* CLAREAugmenter

If you learned something new or enjoyed reading this article, please share it so that others can see it. Until then, see you in the next post!

You can also find me on Twitter [@Davis_McDavid](https://twitter.com/Davis_McDavid?ref=hackernoon.com).

And you can read more articles like this [here](https://hackernoon.com/u/davisdavid).

