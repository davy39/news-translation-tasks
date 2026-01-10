---
title: Natural Language Processing Techniques for Topic Identification – Explained
  with Examples
subtitle: ''
author: Ibrahim Ogunbiyi
co_authors: []
series: null
date: '2024-01-25T16:16:15.000Z'
originalURL: https://freecodecamp.org/news/topic-identification-using-natural-language-processing
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/pexels-wallace-chuck-3109168.jpg
tags:
- name: natural language processing
  slug: natural-language-processing
- name: nlp
  slug: nlp
seo_title: null
seo_desc: 'There''s a lot of textual information available these days. It ranges from
  articles to social media posts and research papers. So our ability to distill meaningful
  insights is key. This helps us make informed decisions in a wide array of contexts.

  For...'
---

There's a lot of textual information available these days. It ranges from articles to social media posts and research papers. So our ability to distill meaningful insights is key. This helps us make informed decisions in a wide array of contexts.

For example, you can analyze a large volume of textual content to extract a common theme. Companies and businesses utilize this technique to understand public opinion about their brand. This lets them make informed decisions and improve their services.

The ability to extract themes from a large amount of textual data is referred to as topic identification.

In this article, you will learn how to utilize NLP techniques for topic identification, enhancing your skillset as a data scientist. So sit back, because it's gonna be an interesting journey.

## What is Topic Identification?

Topic identification, simply put, is a sub-field under natural language processing. It involves the process of automatically discovering and organizing the main themes or topics present in a collection of textual data.

There are several Natural Language Processing (NLP) techniques you can use to identify themes in text, from simple ones to more algorithm based techniques. In this article we will look at the common NLP techniques used for topic identification. We'll discuss these in more detail below.

I recently tweeted about the essence of NLP. It really is purely statistics, because there are different manipulations you can do to ensure that numbers serve as representations for text (since computers don't understand text).

%[https://twitter.com/Ibrahim_Geek/status/1742877290227187989?s=20] 

## Requirements for this Project

In order for you to be able to follow along and get hands-on practical experience while learning, you should have Python 3.x installed on your machine.

We'll also use the following libraries: Gensim, Scikit-Learn, and NLTK. You can install them using the Pip package installer with the following command:

```bash
pip install gensim nltk scikit-learn
```

## Techniques Used in NLP for Topic Identification

There are various techniques you can use for topic identification. In this article, you will learn about some common NLP techniques that work quite well, from simple and effective methods to more advanced ones.

### Bag of Words

Bag of Words (BoW) is a common representation used in NLP for textual data. You can use it to count the frequency at which each word occurs in a document.

BoW, in the context of topic identification, is based on the assumption that the more frequently a word occurs in a document, the more important it is. Then you can use those more common words to infer what the document is all about.

Bag of words is the simplest technique used to identify topics in NLP. While Bag of Words is simple and efficient, it is highly affected by stop words, which are common words in text data (like "the," "and," "is," and so on).

But once you eliminate the issue of stop words from the text, allowing you to perform effective text processing (using techniques like normalization), BoW can still prove effective in identifying some main topics.

Let's look at how you can use BoW to identify the topic below.

#### How to implement of Bag of Words in Python

A bit of background about the example article we'll use here: I got it from the BBC, and it's titled "US lifts ban on imports of latest Apple watch." The article discusses the lifted ban on Apple's latest watches, Ultra 2 and Series 9.

Now let's go over how to implement the bag of words in Python. I'll break this code block up into sections and explain each part as I go to make it a bit more easy to digest.

```python
#import necessary libraries
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

article = "Apple's latest smart watches can resume being sold in the US after the tech company filed an emergency appeal with authorities.\
Sales of the Series 9 and Ultra 2 watches had been halted in the US over a patent row.\
The US's trade body had barred imports and sales of Apple watches with technology for reading blood-oxygen level.\
Device maker Masimo had accused Apple of poaching its staff and technology. \
It comes after the White House declined to overturn a ban on sales and imports of the Series 9 and Ultra 2 watches which came into effect this week.\
Apple had said it strongly disagrees with the ruling.\
The iPhone maker made an emergency request to the US Court of Appeals, which proved successful in getting the ban lifted."
```

In the above code, we're importing the necessary libraries that we'll use to implement the BoW.

We'll use the Counter library to count the frequency of each word, and the word\_tokenize library to tokenize the document into individual word tokens so they can be counted. Lastly, the stopwords library will remove stop words from the document.

```python

# Initialize english stopwords
english_stopwords = stopwords.words("english")

#convert article to tokens
tokens = word_tokenize(article)

#extract alpha words and convert to lowercase
alpha_lower_tokens = [word.lower() for word in tokens if word.isalpha()]

#remove stopwords
alpha_no_stopwords = [word for word in alpha_lower_tokens if word not in english_stopwords]

#Count word
BoW = Counter(alpha_no_stopwords)

#3 Most common words
BoW.most_common(3)
```

In the above code, we use the first line of code to extract all stop words in the English language. Then, the second line tokenizes the article string into individual words. The third line of code normalizes each word into lowercase and only extracts alphabetic words from the article. The last two lines of code are used to count the frequency of each word and select the most common three words.

Below is the output of the BoW model:

```javascript
[('watches', 4), ('us', 4), ('apple', 3), ('emergency', 2)]
```

From this, we can infer that the article is all about "Apple's watches in the US". As you can see, with the simplicity in reasoning behind the bag of words, it is still possible to infer a bit of knowledge about the article.

### Latent Dirichlet Allocation

Latent Dirichlet Allocation, or LDA for short, is a popular probabilistic model used in NLP and machine learning for topic modeling (using algorithms to identify topics). It is based on the assumption that documents are mixtures of topics, and topics are mixtures of words.

Simply put, LDA is an NLP technique used to identify the topic to which a document belongs based on the words contained in the document.

LDA operates on the bag-of-words representation of documents, where each document is represented as a vector of word frequencies. You can implement LDA using the Gensim library in Python (which is an open source library used for topic modelling and document similarity analysis).

Steps for implementing LDA include:

* **Import Libraries:** First step is to import the necessary libraries you will be utilizing.
    
* **Data Preparation:** Convert raw data to a document format then tokenize, remove stop words, and optionally perform stemming or lemmatization.
    
* **Create Dictionary and Corpus**: Build a dictionary with unique word IDs. Then form a bag of words corpus representing document-word frequency.
    
* **Train LDA Model**: Use the document-word frequency and dictionary to train the LDA model, setting the desired number of topics.
    
* **Print Topics**: Explore and print the discovered topics.
    

```python
# Import the necessary libraries
from gensim.corpora.dictionary import Dictionary
from gensim.models import LdaModel
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

article = "Apple's latest smart watches can resume being sold in the US after the tech company filed an emergency appeal with authorities. \
Sales of the Series 9 and Ultra 2 watches had been halted in the US over a patent row. \
The US's trade body had barred imports and sales of Apple watches with technology for reading blood-oxygen level. \
Device maker Masimo had accused Apple of poaching its staff and technology. \
It comes after the White House declined to overturn a ban on sales and imports of the Series 9 and Ultra 2 watches which came into effect this week. \
Apple had said it strongly disagrees with the ruling. \
The iPhone maker made an emergency request to the US Court of Appeals, which proved successful in getting the ban lifted."
```

The above lines of code include the necessary libraries that we'll use to implement the LDA.

The first line of code contains the Dictionary object. Then, the second line imports the LDA model, and the third line of code contains the `sent_tokenize`, which we'll use to convert the article into document. After that, `word_tokenize` will tokenize the document into individual words. Lastly, we have the `stop_words` library.

```python
# convert article to documents
documents = sent_tokenize(article)

#toeknize and normalize the document
tokenized_words = [word_tokenize(doc.lower()) for doc in documents]

# remove stops words and onl extract alphabets
cleaned_token = [[word for word in sentence if word not in english_stopwords and word.isalpha()]
                 for sentence in tokenize_words]

# create a dictionary
dictionary = Dictionary(cleaned_token)

# Create a corpus from the document
corpus = [dictionary.doc2bow(text) for text in cleaned_token]
```

The above lines of code include the preprocessing steps that will be performed on the article, including converting the article to a document, normalizing, and tokenizing the document into individual words.

The next part removes stopwords from the text and then extracts words and numbers from the document. After that, we create a dictionary, which is a map between each word and its numerical identifier. The last line of code then creates a corpus of the document.

```javascript
# Build the LDA model
model = LdaModel(corpus=corpus, id2word=dictionary, num_topics=3)

# Print the topics
print("Identified Topics:")
for idx, topic in lda_model.print_topics():
    print(f"Topic {idx + 1}: {topic}")
```

The above code is used to train the model on the corpus and then prints the top 3 topics from the article.

Below is the output of the LDA Model:

```javascript
Identified Topics:
Topic 1: 0.045*"9" + 0.045*"ultra" + 0.044*"sales" + 0.044*"2" + 0.043*"series" + 0.043*"watches" + 0.029*"apple" + 0.028*"ruling" + 0.028*"disagrees" + 0.028*"said"
Topic 2: 0.051*"maker" + 0.035*"ban" + 0.035*"us" + 0.031*"emergency" + 0.031*"made" + 0.031*"successful" + 0.031*"court" + 0.031*"lifted" + 0.031*"request" + 0.031*"proved"
Topic 3: 0.055*"apple" + 0.054*"us" + 0.054*"watches" + 0.031*"sales" + 0.031*"technology" + 0.031*"imports" + 0.031*"authorities" + 0.031*"barred" + 0.031*"appeal" + 0.031*"filed"
```

The LDA technique shows some improvement as compared to BoW method. We can still obtain a more information that the article is all about a ban related to Apple ultra series watches in the US.

### Non-Negative Matrix Factorization

Non-Negative Matrix Factorization (NMF), just like LDA, is another topic modeling technique that uncovers latent topics in a collection of documents.

But instead of relying on BoW, it relies on the Term Frequency-Inverse Document Frequency (TF-IDF) representation to capture and retrieve hidden themes or topics from the documents.

By incorporating TF-IDF information, NMF is able to weigh the importance of terms, thereby identifying more hidden patterns. You can perform NMF using the Scikit-learn library.

### Steps for performing NMF

* Import necessary libraries
    
* Data Preparation: Convert text into document, then perform necessary data preparation like removing stop words. The TF-IDF function in Scikit-Learn has as an argument that does that.
    
* Convert the document to a TF-IDF matrix using the TF-IDF vectorizer in Scikit-learn
    
* Apply the NMF function on the TF-IDF matrix and specify the numbers of topic you want and the number of words in each topic
    
* Lastly, interpret your result.
    

```python
# import the necessary libraries
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF

article = "Apple's latest smart watches can resume being sold in the US after the tech company filed an emergency appeal with authorities. \
Sales of the Series 9 and Ultra 2 watches had been halted in the US over a patent row. \
The US's trade body had barred imports and sales of Apple watches with technology for reading blood-oxygen level. \
Device maker Masimo had accused Apple of poaching its staff and technology. \
It comes after the White House declined to overturn a ban on sales and imports of the Series 9 and Ultra 2 watches which came into effect this week. \
Apple had said it strongly disagrees with the ruling. \
The iPhone maker made an emergency request to the US Court of Appeals, which proved successful in getting the ban lifted."
```

The above code contains the libaries that we'll use to implement NMF and the article itself.

```python
# convert article to documents
documents = sent_tokenize(article)

# Create a TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer(stop_words='english').fit_transform(document)

# Apply NMF
num_topics = 5  # Set the number of topics you want to identify
nmf_model = NMF(n_components=num_topics, init='random', random_state=42)
nmf_matrix = nmf_model.fit_transform(tfidf)
```

The above code converts the article into documents. Then it creates a Term-Frequency Inverse Document Frequency matrix of the article document. The last three lines of code then define the number of topics and create the topics from the document matrix using the NMF.

Below is the output of the NMF Model:

```javascript
Topic #1: ultra, series, sales, watches, row, halted, patent, white, house, effect
Topic #2: lifted, court, iphone, getting, request, successful, proved, appeals, ban, maker
Topic #3: disagrees, strongly, ruling, said, apple, body, blood, level, trade, oxygen
Topic #4: filed, resume, appeal, latest, tech, authorities, sold, smart, company, emergency
Topic #5: technology, apple, accused, masimo, device, staff, poaching, maker, trade, level
```

You can see that NMF reveals more insights concerning the themes of the document. For example, you can tell that another company called Masimo is accusing Apple of a patent infringement in their Ultra series watches.

## How to Choose Which Technique to Use?

I recommend experimenting with all the approaches in order to gain different perspectives concerning the contents of your document.

Bag of Words and LDA are based on how frequently words occur, making these techniques useful for inferring the biggest/most general themes about the document.

On the other hand, when using NMF, which is based on TF-IDF, less frequent words can be used to infer additional topics and provide a different perspective on the document.

For example, NMF was able to identify key terms like "Masimo" and "accused," whereas LDA was not able to do this. So depending on your needs, go ahead and experiment with all the approaches to see which one is able to yield better results.

## Conclusion

In this article, you've learned about topic identification and how you can use it to extract themes or topics from a large document.

We covered some different techniques you can use to identify topic including simple ones like BoW and more advanced ones like LDA and NMF.

Happy learning, and see you in the next one.
