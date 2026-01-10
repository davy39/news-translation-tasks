---
title: How to Build Better AI Workflows with Langchain
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2024-03-13T13:38:40.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-better-ai-workflows-with-langchain
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/1700940849777.png
tags:
- name: AI
  slug: ai
- name: 'LLM''s '
  slug: llms
seo_title: null
seo_desc: 'Have you ever wondered how to use Large Language Models (LLMs) like ChatGPT
  in your app?

  Yes, there is the OpenAI API. You can use it to generate responses based on prompts.
  But what if you want to build a complex application with LLMs integrated tig...'
---

Have you ever wondered how to use Large Language Models (LLMs) like ChatGPT in your app?

Yes, there is the OpenAI API. You can use it to generate responses based on prompts. But what if you want to build a complex application with LLMs integrated tightly into the user experience? What if you want to use multiple services like OpenAI, Mistral, and others?

The answer is Langchain – a powerful tool designed to streamline and enhance AI workflows. 

Let’s look at what Langchain is, why you would want to use it and how to work with it using a simple example.

## **What is Langchain?**

Langchain is a toolkit that simplifies building and deploying large language models. It includes those augmented with retrieval capabilities like RAGs.

LangChain aims to connect powerful Large Language Models (LLMs) like OpenAI’s GPT-3.5 and GPT-4 with various external data sources. This connection helps build and improve natural language processing (NLP) applications.

Langchain handles the heavy lifting, making focusing on the application’s logic and user experience easier.

Also, GPT models like ChatGPT learn from data available up to their public release. For example, although ChatGPT became available at the end of 2022, its first version only knew things from 2021 and earlier.

LangChain lets AI models access and learn from newer data without any limits.

## **Why Use Langchain?**

LangChain offers several benefits over directly using the OpenAI API (or other LLMs). These include:

* **Integration with Multiple Services**: LangChain allows developers to combine OpenAI’s capabilities with other tools and services seamlessly. This means you can easily mix and match different AI models and databases to get the best results.
* **Enhanced Functionality**: Langchain adds extra features on top of what OpenAI offers. For example, it can help manage more complex interactions that require remembering past conversations or pulling in information from external sources.
* **Cost Efficiency**: By optimizing how and when to use AI models, LangChain can help reduce costs. It does this by methods like Caching, selective model usage and optimized data retrieval methods.

LangChain is like having a toolkit that not only includes everything OpenAI offers but also brings additional components into the mix. Langchain makes it easier to build powerful and cost-effective applications powered by LLMs.

## **How to Get Started with Langchain and OpenAI API**

To give you a taste of how Langchain can be applied, let’s dive into a simple code example. We will access the OpenAI API using Langchain to generate a response for a prompt.

Install OpenAI and Langchain in your dev environment or a [Google colab notebook](https://colab.research.google.com/). Make sure you have your [OpenAI API](https://platform.openai.com/api-keys) key with you:

```
pip install openai langchain
```

Now let's import the libraries:

```
import openai
from langchain.llms import OpenAI
```

The `llms` in the import path stands for "Large Language Models". This module allows the script to use LangChain's functionalities designed for interacting with OpenAI's models.

Now let’s set the API key:

```
openai.api_key = 'your_openai_api_key_here'
```

Now we will initialize the LangChain wrapper for the OpenAI API. It will create an instance of the `OpenAI` class imported from the LangChain library, passing the OpenAI API key as an argument:

```
langchain_openai = OpenAI(api_key=openai.api_key)
```

`langchain_openai` instance will be used to interact with OpenAI's models through LangChain's interface.

Now we are ready to send the prompt. Let’s ask OpenAI what the capital of France is:

```
question = "What is the capital of France?"
response = langchain_openai(question)
```

And print the response:

```
print("Response from OpenAI:", response)
```

Here is the response:

```
Response from OpenAI: 

The capital of France is Paris.
```

This is a simple example of using Langchain and OpenAI. For the full documentation and tutorials, [visit the official documentation](https://python.langchain.com/docs/get_started/introduction).

## **Conclusion**

Langchain opens up a world of possibilities for developers eager to explore the potential of large language models. Whether you want to automate tasks, generate content, or analyze data, Langchain provides a robust and user-friendly framework. 

With the code example provided, I hope you have a starting point to experiment with and build your LLM-powered applications using Langchain.

Hope you enjoyed this article. [Visit turingtalks.ai](https://www.turingtalks.ai/) for weekly byte-sized AI tutorials.

