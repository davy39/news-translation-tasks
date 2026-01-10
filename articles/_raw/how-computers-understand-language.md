---
title: 'From Text to Meaning: How Computers Understand Language'
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2023-09-30T14:31:13.000Z'
originalURL: https://freecodecamp.org/news/how-computers-understand-language
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/blog_img.jpeg
tags:
- name: natural language processing
  slug: natural-language-processing
seo_title: null
seo_desc: 'Language is an intricate dance of words and meanings, a fundamental tool
  for human expression and understanding.

  For centuries, this dance was uniquely human. But with the advent of modern computing,
  a new question emerged: can machines understand ou...'
---

Language is an intricate dance of words and meanings, a fundamental tool for human expression and understanding.

For centuries, this dance was uniquely human. But with the advent of modern computing, a new question emerged: can machines understand our language?

The answer, as many of us know, is a resounding “yes!” — but how do they do it? Let’s look at how Natural Language Processing (NLP) helps computers decode and derive context from our language.

## The Building Blocks: Tokens

Imagine reading a sentence.

To make sense of it, your brain breaks it down, recognizing individual words and their roles. Computers do something similar called tokenization.

Tokenization splits a piece of text into smaller units, or “tokens”, which are typically words or subwords. This is the computer’s first step in processing text data.

For example, the sentence “Computers are smart” would be tokenized into [‘Computers’, ‘are’, ‘smart’].

## Understanding Word Forms: Stemming and Lemmatization

Once a computer tokenizes a text, it needs to understand different word forms.

Consider the words “running”, “runner”, and “ran”. To us, they are related. But a computer sees them as separate words. Enter stemming and lemmatization.

### Stemming

Stemming simplifies words to their foundational form. For example, in this example, variations like “running”, “runner”, or “runs” are all stripped down to the basic root, which is “run”.

Stemming helps simplify the text data, making it easier for algorithms to analyze and process. While it’s useful for certain tasks, it’s important to note that stemming can sometimes lead to inaccurate results, as it might trim words too much and lose some of their original meaning.

For more nuanced tasks, other techniques like lemmatization might be more appropriate.

### Lemmatization

Lemmatization reduces a word to its base or canonical form, called a lemma.

Unlike stemming, which simply trims words, lemmatization considers the context and meaning of the word. It ensures that the words are transformed into a valid base form. For instance, the word “better” might be lemmatized to “good”, and “running” would be lemmatized to “run”.

By using lemmatization, we can group different forms of a word together so that they’re treated as a single item. This is useful when analyzing text data, as it helps in recognizing that different word forms are essentially conveying the same concept.

Lemmatization often requires more computational resources than stemming since it has to consider word meanings and structures. It’s also typically dependent on dictionaries or morphological analysis tools.

## Understanding Context with Syntax and Semantics

Words interact with each other, influencing their meanings based on their neighbouring words. To grasp this context, computers analyze both syntax and semantics.

Take the word “bat” as an example. In the sentence “I played with the bat,” “bat” refers to a sporting tool. However, in the sentence “The bat flew in the night,” “bat” indicates a flying mammal.

Through syntax, computers determine a word’s function in a sentence, and with semantics, they interpret its exact meaning given that function.

## The Power of Word Embeddings

Computers are great with numbers, but not so much with words.

To bridge this gap, words are often converted into vectors of numbers in a process called word embedding. These vectors capture the semantic meaning of words.

Words with similar meanings tend to have similar vectors. This numerical representation allows computers to perform mathematical operations on words, leading to tasks like finding word similarities or even analogies.

I recently published an article on word embeddings and you can [read the full article here](https://www.freecodecamp.org/news/understanding-word-embeddings-the-building-blocks-of-nlp-and-gpts/).

## The Final Piece: Machine Learning

All the above processes feed into machine learning models.

These models, trained on vast datasets, use patterns in the text to make determinations. Datasets can include various examples and scenarios, allowing the models to learn and recognize patterns, trends, and relationships within the text.

Once trained, when these models encounter new textual information, they analyze it by looking for familiar patterns they’ve learned. For example, is a given piece of text positive or negative in sentiment? Or a review stating “The movie was captivating,” versus “It was a dull watch.”

These models can then power products like language translation and transformers. There are more steps involved in breaking down language for NLP, but these are all the ones that you will use almost on a daily basis as an AI engineer.

## Summary

The journey from text to meaning is a complex one, even for humans. From breaking down sentences to understanding context and leveraging the power of machine learning, computers have come a long way in deciphering human language.

As technology continues to advance, we can only anticipate even more deep interactions between humans and machines, facilitated by the power of Natural Language Processing.

If you found this article interesting, [join my newsletter](https://manishmshiva.com/) and I ll send you an email with my content every Friday.

