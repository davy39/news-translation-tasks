---
title: How to Run Open Source LLMs Locally Using Ollama
subtitle: ''
author: Sahil
co_authors: []
series: null
date: '2024-04-02T09:25:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-run-open-source-llms-locally-using-ollama
coverImage: https://www.freecodecamp.org/news/content/images/2024/04/Neon-Green-Motivational-Quote--1-.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: 'LLM''s '
  slug: llms
- name: open source
  slug: open-source
seo_title: null
seo_desc: "This article will guide you through downloading and using Ollama, a powerful\
  \ tool for interacting with open-source large language models (LLMs) on your local\
  \ machine. \nUnlike closed-source models like ChatGPT, Ollama offers transparency\
  \ and customiza..."
---

This article will guide you through downloading and using Ollama, a powerful tool for interacting with open-source large language models (LLMs) on your local machine. 

Unlike closed-source models like ChatGPT, Ollama offers transparency and customization, making it a valuable resource for developers and enthusiasts.

We'll explore how to download Ollama and interact with two exciting open-source LLM models: LLaMA 2, a text-based model from Meta, and LLaVA, a multimodal model that can handle both text and images.

## How to Download Ollama

To download Ollama, head on to the official website of [Ollama](https://ollama.com/) and hit the download button.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/ollama-homepage-download.png)
_ollama homepage_

Ollama supports 3 different operating systems, and the Windows version is in preview mode.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/ollama-download-screen.png)
_ollama download page_

You can choose the executable file according to your OS and after successfully downloading the executable file, you can install it by running the executable file.

For Linux users, you have to execute the command that is being shown on the screen instead of downloading an executable file.

## How to Run Ollama

To show you the power of using open source LLMs locally, I'll present multiple examples with different open source models with different use-cases. This will help you to use any future open source LLM models with ease. 

So, lets get started with the first example!

### How to Run the LLama2 Model from Meta

Llama 2 model is an open-source LLM model from Meta and we'll interact with it like we'd do with ChatGPT (free version), only text based interaction.

First, let's download the model using the following command:

```bash
ollama run llama2

```

You should see a output similar to this after the downloading of the model.

```bash
pulling manifest
pulling 8934d96d3f08... 100% ▕██████████████████████████████████████████████████████████████████████████████████████████▏ 3.8 GB
pulling 8c17c2ebb0ea... 100% ▕██████████████████████████████████████████████████████████████████████████████████████████▏ 7.0 KB
pulling 7c23fb36d801... 100% ▕██████████████████████████████████████████████████████████████████████████████████████████▏ 4.8 KB
pulling 2e0493f67d0c... 100% ▕██████████████████████████████████████████████████████████████████████████████████████████▏   59 B
pulling fa304d675061... 100% ▕██████████████████████████████████████████████████████████████████████████████████████████▏   91 B
pulling 42ba7f8a01dd... 100% ▕██████████████████████████████████████████████████████████████████████████████████████████▏  557 B
verifying sha256 digest
writing manifest
removing any unused layers
success
>>> Send a message (/? for help)

```

Now, its should ask you to send a message or prompt. Let's ask llama2 "What can you do for me?" (You can ask whatever you want).

If you asked the same question as above, then you should get a reply like this:

```bash
>>> What can you do for me?

As a responsible AI language model, I am here to assist you with any questions or tasks you may have. Here are some examples of things I can help
with:

1. Answering questions: I can provide information on a wide range of topics, from science and technology to history and culture.
2. Generating ideas: I can help you brainstorm ideas for creative projects, or provide suggestions for solving problems.
3. Writing assistance: I can help you with writing tasks such as proofreading, editing, and suggesting alternative words or phrases.
4. Translation: I can translate text from one language to another.
5. Summarizing content: I can summarize long pieces of text, such as articles or documents, into shorter, more digestible versions.
6. Creativity: I can help you generate creative ideas for stories, poems, or other forms of writing.
7. Language learning: I can assist you in learning a new language by providing grammar explanations, vocabulary lists, and practice exercises.
8. Chatting: I'm here to chat with you and provide a response to any question or topic you'd like to discuss.

Please let me know if there is anything specific you would like me to help you with.

>>> Send a message (/? for help)

```

So that is the response that I got from llama2.

To exit the program, you can type `/exit`.

Let's now run a multi-modal model where you can send an image and ask questions based on that.

### How to Run the LLaVA Model

LLaVA is a open-source multi-modal LLM model. A multi-modal model can take input of multiple types and generate a response accordingly.

Using this model, we are now going to pass an image and ask a question based on that.

So, first things first, lets download the model:

```bash
ollama run llava

```

After successfully downloading the model, you should see something like this in the terminal:

```bash
pulling manifest
pulling 170370233dd5... 100% ▕██████████████████████████████████████████████████████████████████████████████████████████▏ 4.1 GB
pulling 72d6f08a42f6... 100% ▕██████████████████████████████████████████████████████████████████████████████████████████▏ 624 MB
pulling 43070e2d4e53... 100% ▕██████████████████████████████████████████████████████████████████████████████████████████▏  11 KB
pulling c43332387573... 100% ▕██████████████████████████████████████████████████████████████████████████████████████████▏   67 B
pulling ed11eda7790d... 100% ▕██████████████████████████████████████████████████████████████████████████████████████████▏   30 B
pulling 7c658f9561e5... 100% ▕██████████████████████████████████████████████████████████████████████████████████████████▏  564 B
verifying sha256 digest
writing manifest
removing any unused layers
success
>>> Send a message (/? for help)

```

I'll be using this [image](https://www.pexels.com/photo/aerial-view-of-vehicles-on-a-street-and-a-man-on-a-crosswalk-16456833/) from [pexels.com](https://www.pexels.com/).

This is the output I got from LLaVA:

```bash
>>> What's in this image? ./Downloads/test-image-for-llava.jpeg
Added image './Downloads/test-image-for-llava.jpeg'
 The image shows a person walking across a crosswalk at an intersection. There are traffic lights visible, and the street has a bus parked on one
side. The road is marked with lane markings and a pedestrian crossing signal. The area appears to be urban and there are no visible buildings or
structures in the immediate vicinity of the person.

>>> Send a message (/? for help)

```

You can see that its an accurate explanation of the image.

Feel free to try something else and have fun with it.

## Conclusion

That's it! With Ollama, you can experiment with powerful LLMs like LLaMA 2 and LLaVA on your own machine. 

Download Ollama and explore the exciting world of open-source large language models!

