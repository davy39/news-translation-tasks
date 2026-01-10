---
title: Learn to Control GPT in the OpenAI Playground
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2023-12-08T17:15:34.000Z'
originalURL: https://freecodecamp.org/news/learn-to-control-gpt-in-openai-playground
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/pexels-levi-damasceno-571249.jpg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: chatgpt
  slug: chatgpt
- name: 'LLM''s '
  slug: llms
- name: openai
  slug: openai
seo_title: null
seo_desc: "ChatGPT is the interface most people use to work with OpenAI's large language\
  \ model. But for someone who needs the versatility and power of programmatic access,\
  \ there's no replacement for OpenAI's API. \nThe API is the interface you can use\
  \ to connect..."
---

ChatGPT is the interface most people use to work with OpenAI's large language model. But for someone who needs the versatility and power of programmatic access, there's no replacement for OpenAI's API. 

The API is the interface you can use to connect programming code running on your own PC with OpenAI's GPT servers. 

Of course, when using the API you can include plain language prompts where you ask GPT for answers and generated content. But you can also apply all the built-in power of that programming code to create sophisticated and automated operations that involve GPT. 

You could, for instance, ask ChatGPT to write an article on a specific topic. But using the API, you can ask it to write 100 articles on the topics listed in a text document and then sit back while your code does all the work for you. 

Anything that takes advantage of code rather than performing manual operations is a thousand times more effective when you add GPT to the equation.

The problem is that, like all APIs, figuring out the syntax and other fine details can take time. To help you over that hill, OpenAI created the visual tools within their [Playground](https://platform.openai.com/playground). Let's see how that'll help. 

This article is excerpted from [my Manning book, The Complete Obsolete Guide to Generative AI](https://www.manning.com/books/the-complete-obsolete-guide-to-generative-ai?a_aid=bootstrap-it&a_bid=8c39744&a_bid=8c397448&chan=fcc_ai). 

## What is the Playground?

Playground, shown in the figure below, existed even before ChatGPT, and it was where I had my first interactions with GPT. Although do keep in mind that, along with everything else in the AI world, the interface will probably have changed at least twice by the time you get to it. 

We're going to use the playground throughout this tutorial to learn how to interact with GPT.

![Image](https://www.freecodecamp.org/news/content/images/2023/12/gai-2-2.png)
_OpenAI's Playground interface_

You get to [Playground](https://platform.openai.com/playground) from your OpenAI login account. Rather than enjoying a sustained conversation where subsequent exchanges are informed by earlier prompts and completions, when the Chat option is selected from the pull-down at the top-left of the screen, the text field in Playground offers only one exchange at a time. The models it's based on might also be a bit older and less refined than the ChatGPT version.

But there are two things that set Playground apart from ChatGPT. One is the configuration controls displayed down the right side of the screen in the image above. The second is the _View code_ feature at the top-right. It's those features that make Playground primarily an educational tool rather than just another GPT interface.

## How to Access Python Code Samples

The image below shows a typical Playground session where I've typed in a prompt and then hit the "View code" button with the "Python" option selected. I'm shown working code that, assuming you'll add a valid OpenAI API key on line 4, can be copied and run from any internet-connected computer.

![Image](https://www.freecodecamp.org/news/content/images/2023/12/gai-2-3-1.png)
_Playground's View code tool with Python code_

Don't worry about the details right now, but take a moment to look through the arguments that are included in the `openai.Completion.create()` method. 

The model that's currently selected in the Model field on the right side of the Playground is there (`text-davinci-003`), as is my actual prompt (`Explain the purpose of...`). In fact, each configuration option I've selected is there. 

In other words, I can experiment with any combination of configurations here in the Playground, and then copy the code and run it – or variations of it – anywhere.

This, in fact, is where you learn how to use the API. In other words, here is where you're shown code samples that can form the basis of a lot of what you'll eventually want to run in your own environment.

## How to Access CURL Code Samples

The next image shows us how that exact same prompt would work if I decided to use the command line tool, curl, instead of Python. 

![Image](https://www.freecodecamp.org/news/content/images/2023/12/gai-2-4.png)
_Playground's View code tool with curl code_

`curl` is a venerable open source command line tool that's often available by default. You'll generally use `curl` when you want to access a remote server directly from your command line. Those will usually be for relatively simpler requests. 

Python, on the other hand, will be the tool of choice for more complicated applications that involve programming logic.

To confirm it's available on your system, simply type `curl` at any command line prompt. You should see some kind of help message with suggestions for proper usage.

Besides Python and curl, you can also display code in Node.js (for when you're building server-based applications) and JSON (to enable programmatic integrations). 

With that, you're all set to dive deeper than simple chat sessions: you're now able to finely control and programmatically automate your interactions with GPT from the comfort of your own command line (or IDE).

This article is excerpted from [my Manning book, The Complete Obsolete Guide to Generative AI](https://www.manning.com/books/the-complete-obsolete-guide-to-generative-ai?a_aid=bootstrap-it&a_bid=8c39744&a_bid=8c397448&chan=fcc_ai). There's plenty more technology goodness available through [my website](https://bootstrap-it.com).

