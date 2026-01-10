---
title: NLP Tutorial – Text Pre-Processing Techniques for Beginners
subtitle: ''
author: Crypt(iq)
co_authors: []
series: null
date: '2023-07-12T14:31:24.000Z'
originalURL: https://freecodecamp.org/news/natural-language-processing-techniques-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/NLP-6.png
tags:
- name: Machine Learning
  slug: machine-learning
- name: nlp
  slug: nlp
seo_title: null
seo_desc: Natural Language Processing (NLP) is a branch of Machine learning (ML) that
  is focused on making computers understand the human language. It is used to create
  language models, language translation apps like Google translate, and virtual assistants,
  a...
---

Natural Language Processing (NLP) is a branch of Machine learning (ML) that is focused on making computers understand the human language. It is used to create language models, language translation apps like Google translate, and virtual assistants, among other things.

This article takes you through one of the most basic steps in NLP which is text-pre-processing. This is a must-know topic for anyone interested in language models and NLP in general which is a core part of the Artificial Intelligence (AI) and ML field.

## What is text pre-processing?

Text pre-processing is the process of transforming unstructured text to structured text to prepare it for analysis.

When you pre-process text before feeding it to algorithms, you increase the accuracy and efficiency of said algorithms by removing noise and other inconsistencies in the text that can make it hard for the computer to understand.

Making the text easier to understand also helps to reduce the time and resources required for the computer to pre-process data.

## Processes involved in text pre-processing

To properly pre-process your text and get it in the right state to perform further analysis and actions with it, there are quite a few operations that need to be done on the text and a couple of steps to be followed to get a well structured text.

Let's go over these processes in the following sub-sections.

### Tokenization

Tokenization is the first stage of the process. 

Here your text is analysed and then broken down into chunks called ‘tokens’ which can either be words or phrases. This allows the computer to work on your text token by token rather than working on the entire text in the following stages.

The two main types of tokenisation are word and sentence tokenisation.

**Word tokenisation** is the most common kind of tokenisation. 

Here, each token is a word, meaning the algorithm breaks down the entire text into individual words:

```python
text = 'Wisdoms daughter walks alone. The mark of Athena burns through rome'

words = text.split()
print(words)

#the output of this is given below
>>>> ['Wisdoms', 'daughter', 'walks', 'alone.', 'The', 'mark', 'of', 'Athena', 'burns', 'through', 'rome']
```

On the other hand, **sentence tokenisation** breaks down text into sentences instead of words. It is a less common type of tokenisation only used in few Natural Language Processing (NLP) tasks.

There are various tokenisation algorithms such as the whitespace tokenisation, Regular expression tokenisation (also called Regex), and the statistical tokenisation. 

The type of algorithm you use will depend on the particular task you are working on and what you aim to achieve with it.

### Normalisation

In normalisation your text is converted to standard form. 

An example of this is converting all text to lowercase, removing numbers, or removing punctuations. Normalization helps to make the text more consistent.

There are a couple of different normalisation techniques, but I’ll give you an explanation of some of the most commonly employed normalisation techniques below.

#### Case normalisation

This technique converts all the letters in your text to a single case, either uppercase or lowercase.

Case normalisation ensures that your data is stored in a consistent format and makes it easier to work with the data. 

An example would be looking for all the instances of a word and searching for it in your text. Without case normalisation, the result of searching for the word ‘Boy’ would be different from the result of searching for ‘boy’.

You can use the following code to perform case normalisation:

```python
text = "'To Sleep Or NOT to SLEep, THAT is THe Question'"

def lower_case(text):
    text = text.lower()
    return text

lower_case = lower_case(text)#converts everthing to lowercase
print(lower_case)

#the output of this is given below
>>>> to sleep or not to sleep, that is the question
```


#### Stemming

Stemming words like coding, coder, and coded all have the same base word which is *code*. 

ML models most-often-than-not understand that these words are all derived from one base word. They can work with your text without the tenses, prefixes, and suffixes that we as humans would normally need to make sense of it.

Stemming your texts not only helps to reduce the number of words the model has to work with, and by extension improves  the efficiency of the model.

Although the efficiency of a model is increased with this technique, it also removes important information from your text and could cause some words to be wrongly categorised by the model. 

An example of this would be the difference between *writing* and *write* in the sentences below:
   
```
    
💡 Writing makes me happy.
    
💡 He writes regularly.

```

In the first sentence the word *writing* represents a noun, while *writes* in the second sentence represents a verb. 

If your ML models stems both *writing* and *writes* to the base *write* the difference in their respective parts of speech is overlooked causing some information to be lost in the process of analysing the text.

#### Lemmatisation

This method is very similar to stemming in that it is also used to identify the base of words. It is however a more complex and accurate technique than stemming.

Unlike stemming, lemmatisation takes in the structure of words before identifying a base word. 

Due to the complexity of this technique it has high computational requirements and is therefore more expensive than stemming.


#### Punctuation removal
 
During human conversations, punctuation marks like `‘’`, ` !` , `[`, `}`, `*`, ` #`, ` /`, ` ?`, and  `‘’` are incredibly relevant and necessary to have a proper conversation.  Thelp to fully convey the message of the writer. 

ML models on the other hand find punctuations distracting. 

Their presence could interfere with text analysis and the natural language processing (NLP) process.

By removing punctuation marks from our text we allow the model to focus on the text alone rather than distracting it with symbols. This makes it easier for the text to be analysed.

To perform punctuation removal on text the following code can be used:

```python
import re

text = ' (to love is to destroy, and to be loved, is to be "the" one <destroyed>} '

def remove_punctuations(text):
    punctuation = re.compile(r'[{};():,."/<>-]')
    text = punctuation.sub(' ', text)
    return text

clean_text = remove_punctuations(text)
print(clean_text)

#the output of this is given below
>>>> to love is to destroy  and to be loved  is to be  the  one  destroyed
```

#### Accent removal


This process is about removing language specific character symbols from text. 

Some characters are written with specific accents or symbols to either imply a different pronunciation or to signify that words containing such accented texts have a different meaning.

An example of this would be the difference in both meaning and pronunciation between the words *résumé* and *resume*.

The former refers to a document that highlights your professional skills and achievements, whereas the latter means ‘to take on something again, or to continue a previous task or action’.

You can use the code below to perform accent removal on your text: 

```python
import re

text = "her fiancé's résumé is beautiful"

def remove_accents(text):
    accents = re.compile(u"[\u0300-\u036F]|é|è")
    text = accents.sub(u"e", text)
    return text

cleaned_text = remove_accents(text)
print(cleaned_text)

#the output of this is given below
>>>> her fiance's resume is beautiful
```


#### Stop-word removal

Stop-words are words with no meaning. They don't add any additional value to data. 

Words like *A, the, and, of* and so on are called stop-words.

Like all the previous processes, stop-word removal also helps to increase the efficiency of your model. 

Since it reduces the size of our dataset, it makes it more manageable and increases the accuracy of NLP tasks.


## Conclusion

In this article you learned the basics of NLP.  

You are now familiar with the proper procedure to follow when pre-processing your text for NLP tasks. Feel free to go ahead and practice this on your own and work on a few NLP projects.

Note that choosing the right pre-processing technique / techniques to use on your text will depend largely on the type of text you’re working with, the source of your data, and whatever goal you aim to achieve with it.

To learn more about NLP, you can check out [FreeCodeCamp](https://www.freecodecamp.org/news/tag/nlp/) for more articles and courses on NLP and ML in general.


Connect with me on twitter [@Iqma](https://twitter.com/Iqma__) and follow [my hashnode blog](https://iqmacodes.hashnode.dev/) to read more content like this and to learn more about all things AI and Machine Learning.

Happy learning !


