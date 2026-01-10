---
title: How to Build a Large Language Model from Scratch Using Python
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2023-08-25T15:32:19.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-large-language-model-from-scratch-using-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/llmscratch.png
tags:
- name: 'LLM''s '
  slug: llms
- name: youtube
  slug: youtube
seo_title: null
seo_desc: 'Have you ever been fascinated by the capabilities of large language models
  like GPT-4 but wondered how they are actually work?

  If you want to uncover the mysteries behind these powerful models, our latest video
  course on the freeCodeCamp.org YouTube ...'
---

Have you ever been fascinated by the capabilities of large language models like GPT-4 but wondered how they are actually work?

If you want to uncover the mysteries behind these powerful models, our latest video course on the freeCodeCamp.org YouTube channel is perfect for you. In this comprehensive course, you will learn how to create your very own large language model from scratch using Python.

Elliot Arledge created this course.  He will teach you about the data handling, mathematical concepts, and transformer architectures that power these linguistic juggernauts. Elliot was inspired by a course about how to create a GPT from scratch developed by OpenAI co-founder Andrej Karpathy.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-181.png)
_You will use Jupyter Notebook to develop the LLM._

The course starts with a comprehensive introduction, laying the groundwork for the course. After getting your environment set up, you will learn about character-level tokenization and the power of tensors over arrays.

Next the course transitions into model creation. You will learn about train and validation splits, the bigram model, and the critical concept of inputs and targets. With insights into batch size hyperparameters and a thorough overview of the PyTorch framework, you'll switch between CPU and GPU processing for optimal performance. Concepts such as embedding vectors, dot products, and matrix multiplication lay the groundwork for more advanced topics.

The main section of the course provides an in-depth exploration of transformer architectures. You'll journey through the intricacies of self-attention mechanisms, delve into the architecture of the GPT model, and gain hands-on experience in building and training your own GPT model. Finally, you will gain experience in real-world applications, from training on the OpenWebText dataset to optimizing memory usage and understanding the nuances of model loading and saving.

Through creating your own large language model, you will gain deep insight into how they work. This will benefit you as you work with these models in the future. You can watch the [full course on the freeCodeCamp.org YouTube channel](https://youtu.be/UU1WVnMk4E8) (6-hour watch).

%[https://youtu.be/UU1WVnMk4E8]

Here are all the sections in the course:

* Introduction
* Install Libraries
* Pylzma build tools
* Jupyter Notebook
* Download wizard of oz
* Experimenting with text file
* Character-level tokenizer
* Types of tokenizers
* Tensors instead of Arrays
* Linear Algebra heads up
* Train and validation splits
* Premise of Bigram Model
* Inputs and Targets
* Inputs and Targets Implementation
* Batch size hyperparameter
* Switching from CPU to CUDA
* PyTorch Overview
* CPU vs GPU performance in PyTorch
* More PyTorch Functions
* Embedding Vectors
* Embedding Implementation
* Dot Product and Matrix Multiplication
* Matmul Implementation
* Int vs Float
* Recap and get_batch
* nnModule subclass
* Gradient Descent
* Logits and Reshaping
* Generate function and giving the model some context
* Logits Dimensionality
* Training loop + Optimizer + Zerograd explanation
* Optimizers Overview
* Applications of Optimizers
* Loss reporting + Train VS Eval mode
* Normalization Overview
* ReLU, Sigmoid, Tanh Activations
* Transformer and Self-Attention
* Transformer Architecture
* Building a GPT, not Transformer model
* Self-Attention Deep Dive
* GPT architecture
* Switching to Macbook
* Implementing Positional Encoding
* GPTLanguageModel initalization
* GPTLanguageModel forward pass
* Standard Deviation for model parameters
* Transformer Blocks
* FeedForward network
* Multi-head Attention
* Dot product attention
* Why we scale by 1/sqrt(dk)
* Sequential VS ModuleList Processing
* Overview Hyperparameters
* Fixing errors, refining
* Begin training
* OpenWebText download and Survey of LLMs paper
* How the dataloader/batch getter will have to change
* Extract corpus with winrar
* Python data extractor
* Adjusting for train and val splits
* Adding dataloader
* Training on OpenWebText
* Training works well, model loading/saving
* Pickling
* Fixing errors + GPU Memory in task manager
* Command line argument parsing
* Porting code to script
* Prompt: Completion feature + more errors
* nnModule inheritance + generation cropping
* Pretraining vs Finetuning
* R&D pointers
* Outro

