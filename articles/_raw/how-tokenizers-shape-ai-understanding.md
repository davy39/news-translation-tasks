---
title: Tokenizers Explained – How Tokenizers Help AI Understand Language
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2024-03-27T11:35:07.000Z'
originalURL: https://freecodecamp.org/news/how-tokenizers-shape-ai-understanding
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/ab427b80-a502-11ea-8467-694f4e40dfa7.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: 'LLM''s '
  slug: llms
- name: natural language processing
  slug: natural-language-processing
seo_title: null
seo_desc: 'Tokenizers are the fundamental tools that enable artificial intelligence
  to dissect and interpret human language. Let’s look at how tokenizers help AI systems
  comprehend and process language.

  In the fast-evolving world of natural language processing ...'
---

Tokenizers are the fundamental tools that enable artificial intelligence to dissect and interpret human language. Let’s look at how tokenizers help AI systems comprehend and process language.

In the fast-evolving world of natural language processing (NLP), tokenizers play a pivotal role.

Tokenizers are the unsung heroes behind the scenes, making sense of human language for machines to understand.

Let’s dive into what tokenizers are and explore their use cases. We'll also introduce you to Huggingface, a leading platform in AI and NLP.

We'll also walk through a simple code example using the Huggingface Tokenizer library.

## What are Tokenizers?

Imagine that you’re trying to teach a robot to understand and speak human languages. The first challenge you’d face is how to break down language into pieces the robot can digest. That’s where tokenizers come in.

Tokenizers dissect complex language into manageable pieces, transforming raw text into a structured form that AI models can easily process. This seemingly simple step is crucial, enabling machines to grasp the nuances of human communication.

Think of tokenizers as the chefs who chop ingredients before a meal is cooked. Without this step, preparing complex dishes (or understanding complex sentences) would be much harder.

Through tokenization, AI systems can recognize patterns, understand context, and generate responses that are increasingly similar to human interaction.

By breaking down the complexities of language into digestible bits, tokenizers not only enhance AI’s linguistic capabilities but also pave the way for more intuitive, efficient, and accurate machine learning models.

## What are Huggingface Tokenizers?

[Huggingface](https://huggingface.co/) is a company at the forefront of AI and NLP.

They are best known for their Transformers library, which has made it easy to access state-of-the-art NLP models.

At the heart of their innovations is the tokenizers library, a powerful tool designed to convert text into a format that AI models can understand. This library is essential for developers and researchers working on AI projects.

Hugging Face’s tokenizers are not only efficient and fast but also support a wide range of languages, making them versatile tools for global NLP tasks. They are optimized for performance, ensuring that they can handle large volumes of text without compromising speed or accuracy.

What sets Hugging Face’s tokenizers apart is their integration with the Transformers library, another cornerstone of Hugging Face’s AI ecosystem.

This integration allows for seamless processing of text data, readying it for complex tasks like translation, summarization, and sentiment analysis.

The tokenizers library is continually updated, incorporating the latest research findings and community feedback to enhance its capabilities.

## Simple Code Example of Huggingface Tokenizer Library

Let’s get our hands dirty with some code. We’ll use the Huggingface Tokenizer library to tokenize a simple sentence.

First, let's install the Huggingface Transformers library. (Use ! before the command if you are installing it in a [Google Collab notebook](https://colab.research.google.com/)).

```
pip install transformers
```

First, let's import the `AutoTokenizer` class from the Transformers library. `AutoTokenizer` is a factory class that can automatically load the tokenizer corresponding to a pre-trained model we specify (in this case, the [bert-base-uncased](https://huggingface.co/google-bert/bert-base-uncased) model).

```
from transformers import AutoTokenizer
```

Next, we create an instance of the `AutoTokenizer` class by calling the `from_pretrained` method. This tokenizer is designed to work with the BERT model and is configured to not differentiate between uppercase and lowercase letters (hence 'uncased').

```
tokenizer=AutoTokenizer.from_pretrained("bert-base-uncased")
```

Now let’s declare a string for tokenizing.

```
text = "Hello, and welcome to the world of Tokenizers"
```

Let’s use the `tokenize` method of the tokenizer with the sample text as its argument.

```
tokens = tokenizer.tokenize(text)
```

The `tokenize`method splits the input text into a list of tokens or words/sub-words that the pre-trained model was trained on. For models like BERT, words might be split into smaller units (sub-words or characters) to handle out-of-vocabulary words more effectively.

We'll also convert the list of tokens into a list of integers (token IDs). Each integer corresponds to a specific token in the tokenizer’s vocabulary.

This conversion is necessary because machine learning models do not understand text directly; they work with numerical data.

```
token_ids = tokenizer.convert_tokens_to_ids(tokens)
```

We are done. let’s print both tokens and their corresponding IDs.

```
print("Tokens:", tokens)
print("Token IDs:", token_ids)
```

So this piece of code loads a pre-trained tokenizer for the BERT model, tokenizes a sample sentence and converts those tokens into their corresponding IDs. These IDs are what machine learning models process.

Here is the response:

```
Tokens: ['hello', ',', 'and', 'welcome', 'to', 'the', 'world', 'of', 'token', '##izer', '##s']
Token IDs: [7592, 1010, 1998, 6160, 2000, 1996, 2088, 1997, 19204, 17629, 2015]
```

These tokens and token IDs are crucial for training machine learning models. They convert text into a numerical format that models can process, enabling the understanding of language nuances.

Tokens like `##izer` and `##s` are examples of how the tokenizer deals with words or parts of words that might not be in its basic vocabulary.

The `##` prefix indicates that these are sub-word units or suffixes attached to the preceding token without a space. This allows the model to handle a wide range of vocabulary, including new or uncommon words, by breaking them down into known subcomponents.

# Conclusion

Tokenizers are foundational to NLP, and the Huggingface Transformers library provides an extensive toolkit for working with them. 

By understanding and utilizing tokenizers, we can bridge the gap between human language and machine understanding, unlocking a wide range of applications in AI.

Whether you’re a seasoned developer or new to NLP, diving into tokenization methods is a great way to enhance your machine-learning skills.

Hope you enjoyed this article. If you have any questions, let me know in the comments. [Visit turingtalks.ai](https://www.turingtalks.ai/) for weekly byte-sized AI tutorials.

