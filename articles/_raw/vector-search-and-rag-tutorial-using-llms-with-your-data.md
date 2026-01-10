---
title: Vector Search and RAG Tutorial – Using LLMs with Your Data
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2023-12-11T18:12:49.000Z'
originalURL: https://freecodecamp.org/news/vector-search-and-rag-tutorial-using-llms-with-your-data
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/vectorsearchthumb.png
tags:
- name: Vector Search
  slug: vector-search
- name: youtube
  slug: youtube
seo_title: null
seo_desc: 'You can use Vector Search and embeddings to easily combine your data with
  large language models like GPT-4.

  I just published a course on the freeCodeCamp.org YouTube channel that will teach
  you how to implement Vector Search on three different projec...'
---

You can use Vector Search and embeddings to easily combine your data with large language models like GPT-4.

I just published a course on the freeCodeCamp.org YouTube channel that will teach you how to implement Vector Search on three different projects.

First, you will learn about the concepts and then I'll guide you through developing three projects.

In the first project we build a semantic search feature to find movies using natural language queries. For this we use Python, machine learning models, and Atlas Vector Search.

Next, we create a simple question answering app that using the RAG architecture and Atlas Vector Search to answer questions using your own data.

And in the final project we modify a ChatGPT clone so it answers questions about contributing to the freeCodeCamp.org curriculum based on the official documentation. This project can be easily modified to use your own data or documentation.

MongoDB provided a grant that made this course possible. Their Atlas Vector Search allows you to perform semantic similarity searches on your data, which can be integrated with LLMs to build AI-powered applications.

### What are Vector Embeddings?

Imagine you have a lot of different objects, like fruits, and you want to organize them in a way that shows how similar or different they are. In the real world, you might sort them by color, size, or taste. In the digital world, we can do something similar with data, and that's where vector embeddings come in.

Vector embeddings are like a digital way of sorting or describing things. Each item (like a word, image, or anything else you can think of) is turned into a list of numbers. This list is called a "vector". The cool part is that similar items will have similar vectors.

By turning items into vectors (lists of numbers), we can use math to understand and process them. For example, we can measure how close two vectors are to see how similar the items they represent are.

Words can be turned into vectors and words with similar meanings have vectors that are close together. This helps in tasks like searching for information, translating languages, or even chatting with AI.

Creating these embeddings usually involves a lot of data and some complex math. The computer looks at many examples (like how words are used in sentences) and learns the best way to turn them into vectors.

### What is Vector Search?

Vector search is a method used to find and retrieve information that is most similar or relevant to a given query. But instead of looking for exact matches like traditional search engines, vector search tries to understand the meaning or context of the query. Vector search is a way to implement semantic search, which means using the meaning of words to find relevant results.

Vector search uses vector embeddings by transforming both the search query and the items in the database (like documents, images, or products) into vectors, and then comparing these vectors to find the best matches.

Here's how the process works in detail:

1. **Turning Data into Vectors**: First, everything needs to be converted into vectors. This is done using models that are trained to understand different types of data. For example, a text document is analyzed and turned into a vector that represents its content and meaning.
2. **Query Processing**: When you make a search query, the same process is applied to turn your query into a vector. This vector represents what you're looking for.
3. **Calculating Similarity**: The vector of your search query is then compared with the vectors of items in the database. This is typically done by calculating the distance between vectors. The most common method is using something called "cosine similarity," which measures the cosine of the angle between two vectors. If two vectors are very similar, the angle will be small, and the cosine similarity will be high.
4. **Ranking Results**: Based on these similarity measurements, the system ranks the items in the database. The ones with vectors closest to the query vector are considered the most relevant and are presented as the top search results.
5. **Retrieving the Best Matches**: Finally, the system retrieves and displays the items that best match the query, according to the similarity of their vectors.

In essence, vector search leverages vector embeddings to understand the content and context of both the query and the database items. By comparing these vectors, it efficiently finds and ranks the most relevant results, providing a powerful tool for searching through large and complex datasets.

### **Retrieval-augmented generation (RAG)**

The retrieval-augmented generation (RAG) architecture uses vector search to retrieve relevant documents based on the input query. It then provides these retrieved documents as context to the LLM to help generate a more informed and accurate response. That is, instead of generating responses purely from patterns learned during training, RAG uses those relevant retrieved documents to help generate a more informed and accurate response. This helps address the limitations in LLMs. Specifically:

* RAGs minimize hallucinations by grounding the model’s responses in factual information.
* By retrieving information from up-to-date sources, RAG ensures that the model’s responses reflect the most current and accurate information available.
* While RAG does not directly give LLMs access to a user’s local data, it does allow them to utilize external databases or knowledge bases, which can be updated with user-specific information.
* Also, while RAG does not increase an LLM’s token limit, it does make the model’s use of tokens more efficient by retrieving _only the most relevant documents_ for generating a response.

### Atlas Vector Search

MongoDB Atlas Vector Search allows you to perform semantic similarity searches on your data, which can be integrated with LLMs to build AI-powered applications. Data from various sources and in different formats can be represented numerically as vector embeddings.

Atlas Vector Search allows you to store vector embeddings alongside your source data and metadata, leveraging the power of the document model. These vector embeddings can then be queried using an aggregation pipeline to perform fast semantic similarity search on the data, using an approximate nearest neighbors algorithm.

In this course, you will learn how to use Atlas Vector Search in your applications.

Watch the full course on [the freeCodeCamp.org YouTube channel](https://youtu.be/JEBDfGqrAUA) (1 hour watch).

%[https://youtu.be/JEBDfGqrAUA]


