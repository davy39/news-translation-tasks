---
title: How to Build A Text Summarizer Using Huggingface Transformers
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2024-02-28T10:13:47.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-text-summarizer-using-huggingface-transformers
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/summary-1.jpeg
tags:
- name: nlp
  slug: nlp
seo_title: null
seo_desc: 'In today’s fast-paced world, we’re bombarded with information. It’s like
  trying to drink water from a fire hose.

  That''s where a text summarizer comes in. Imagine it as a filter that separates
  the essential bits from the overwhelming flood of words.

  I...'
---

In today’s fast-paced world, we’re bombarded with information. It’s like trying to drink water from a fire hose.

That's where a text summarizer comes in. Imagine it as a filter that separates the essential bits from the overwhelming flood of words.

In this article, I'll walk you through what a summarizer is, its use cases, what Hugging Face Transformers are, and how you can build your own text summarizer using Hugging Face Transformers. Let's dive in.

## What is a Summarizer?

A summarizer does exactly what its name suggests. It takes a large block of text and condenses it into a shorter version.

This shorter version keeps only the key points. Think of it as the difference between reading a whole novel and glancing at its back cover. The aim is to save time while still getting the essence of the content.

## Use Cases for a Summarizer

Summarizers are not just cool tech tricks. They serve real-world needs.

Journalists use them to quickly sift through reports and studies. Students use them to summarize lengthy readings. Businesses use them to condense market analyses or lengthy reports.

In essence, anyone who needs to process large amounts of text quickly can benefit from a summarizer.

## What are Hugging Face Transformers?

[Hugging Face](https://huggingface.co/) is a company that has created a state-of-the-art platform for natural language processing (NLP).

Their Transformers library is like a treasure trove for NLP tasks. It includes pre-trained models that can do everything from translation and sentiment analysis, to yes, summarization.

These models have learned from vast amounts of text and can understand and generate language in a surprisingly human-like way.

## How to Build a Summarizer with Hugging Face Transformers

Now, let's roll up our sleeves and start building. We will use the Huggingface pipeline to implement our summarization model using [Facebook’s Bart model](https://huggingface.co/facebook/bart-large).

The BART model is pre-trained in the English language. It is a sequence-to-sequence model and is great for text generation (such as summarization and translation). It also works well for comprehension tasks (for example, text classification and question answering).

[Hugging Face Pipelines](https://huggingface.co/docs/transformers/en/main_classes/pipelines) offers a simpler approach to implementing various tasks. Instead of preparing a dataset, training it with the model and then using it, pipeline simplifies the code because it hides away the need for manual tokenization and model customisation.

### How to set up your environment

First, you need to set up your coding environment. I prefer to use a Google Collab notebook instead of installing it on your local machine. [Here is the notebook for this tutorial.](https://colab.research.google.com/drive/1Urxh0anruXP6HTbmi5B5TM0UuK3pQHzI?usp=sharing)

Let’s start by installing the transformer library. Use a ! before the command if you are running it in a collab notebook:

```
pip install transformers
```

Now let’s initialize a text summarization pipeline using the Hugging Face `transformers` library:

```
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
```

Let's break down what each part does:

* `pipeline`: This is a function provided by the Hugging Face `transformers` library to make it easy to apply different types of Natural Language Processing (NLP) tasks, such as text classification, translation, summarization, and so on. The function returns a ready-to-use pipeline object for the specified task.
* `"summarization"`: This is the first argument to the `pipeline` function and specifies the type of task you want the pipeline to perform. In this case, `"summarization"` means that the pipeline will be configured to summarize text.
* `model="facebook/bart-large-cnn"`: This argument specifies the pre-trained model to be used for the summarization task. Here, `"facebook/bart-large-cnn"` refers to a specific model that has been trained on a large dataset to perform text summarization. This model is provided by Facebook and is based on the BART (Bidirectional and Auto-Regressive Transformers) architecture, which is effective for tasks that require understanding and generating natural language. The `large-cnn` part indicates that this particular model variant is optimized for summarization tasks similar to those tackled by traditional CNN news-style summaries.

When this line of code is executed, it creates a `summarizer` object. This object can then be used to perform text summarization by passing text data to it. The model will generate a shorter version of the input text, capturing the most important or relevant information, according to its training on the summarization task.

Now we are ready to use the model to summarize our text (yeah, really!). Let's use an [annual report from FDA](https://www.fda.gov/drugs/generic-drugs/office-generic-drugs-2023-annual-report) and use it as input to get our summary.

```
text = """In 2023 generic drugs continued to play a critical role in the U.S. health care system allowing patients greater access to needed medicines. Generic drugs are generally lower cost than their brand-name equivalent and the approval of generic drugs often means multiple manufacturers for generic medicines, which can help stabilize the supply chain and reduce drug shortage risks.

The mission of the Office of Generic Drugs is to ensure high-quality, safe, and effective generic medicines are available to the American public. Our 2023 Annual Report provides highlights of activities and accomplishments including generic drug approvals, first generic approvals, science and research innovations for generic medicines – including complex generics, and international collaboration, as well as how we are doing on agreements made under the third iteration of the Generic Drug User Fee Amendments."""
```

Now let’s use this text as input and call our summarizer:

```
summary = summarizer(text, max_length=150, min_length=40, do_sample=False)
```

This line of code is using the `summarizer` object created from a Hugging Face `pipeline` to generate a summary of the input text. Here's a breakdown of the function call and its parameters:

* `summarizer`: This is the object initialized previously with the `pipeline` function.
* `text`: This is the input text that you want to summarize.
* `max_length=150`: This parameter specifies the maximum length of the summary in terms of the number of tokens (words and punctuation marks).
* `min_length=40`: Similarly, this parameter sets the minimum length of the summary.

Finally, we will print our summary:

```
print(summary[0]['summary_text'])
```

And here is the response:

```
In 2023 generic drugs continued to play a critical role in the U.S. health care system allowing patients greater access to needed medicines. Generic drugs are generally lower cost than their brand-name equivalent and the approval of generic drugs often means multiple manufacturers for generic medicines.
```

In short, this code:

* loads a summarization pipeline that is pre-configured to use the `facebook/bart-large-cnn` model.
* feeds the text to the summarizer.
* outputs a summary with specified minimum and maximum lengths.

## Conclusion

Building a text summarizer with Hugging Face Transformers is not just about playing with cool technology. It's about harnessing the power of AI to make our lives a bit easier. Whether you're a student, a professional, or just someone curious about NLP, the ability to quickly condense information is invaluable.

With Hugging Face Transformers, you're standing on the shoulders of giants, leveraging some of the most advanced NLP models available today. So, give it a try. Who knows? It might just change the way you deal with text forever.

Thanks for reading this article. Find more AI tutorials at [TuringTalks.ai](https://www.turingtalks.ai/).

