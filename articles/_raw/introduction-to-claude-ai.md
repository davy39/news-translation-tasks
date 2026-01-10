---
title: How to Use Claude AI – Introduction to Claude AI + Code Example
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2024-03-15T00:54:58.000Z'
originalURL: https://freecodecamp.org/news/introduction-to-claude-ai
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/claude-2.png
tags:
- name: AI
  slug: ai
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: '#chatbots'
  slug: chatbots
- name: 'LLM''s '
  slug: llms
seo_title: null
seo_desc: 'By Firas Ahmed

  Claude is one of the leading Large Language Models (LLMs) in the market, developed
  by Anthropic — an AI startup that was co-founded by ex OpenAI employees. The company
  is known for its stringent set of AI ethics and is currently backed...'
---

By Firas Ahmed

Claude is one of the leading Large Language Models (LLMs) in the market, developed by _Anthropic —_ an AI startup that was co-founded by ex OpenAI employees. The company is known for its stringent set of AI ethics and is currently backed by tech giants such as Google and Amazon.

In this article, we're going to delve into Claude AI, compare it to ChatGPT, and provide a quick example of how to work with it via the API.

## What is Claude?

Similar to AI chatbots such as ChatGPT and Gemini, Claude is a chatbot powered by Claude 3  —  Anthropic's latest large language model. It is capable of taking user input and generating human-like output. Besides conversations, you can upload images and documents to Claude and have it summarize them or answer questions about specific points.

What distinguishes Claude from other competitors is Anthropic's claim that it is safer and less likely to produce harmful and offensive output due to "Constitutional AI" – a unique training approach pioneered by Anthropic aimed at developing AI systems that adhere to a set of ethical principles.

The first model was released on March 2023, which was later followed by updated versions with enhanced capabilities, more advanced training techniques, and more focus on safety.

In March 2024, Anthropic launched Claude 3, its most advanced, state-of-the-art suite of models: _Haiku_, _Sonnet_ and _Opus._ Each having their own unique capabilities, with Opus being the most powerful.

Claude 3 offers image processing, lower rates of hallucination and a significantly larger context window. Claude chatbot, currently powered by Claude 3, demonstrated superior performance over ChatGPT in standardized benchmarks.

Apart from the chatbot, Claude is also available through API where developers can build applications on top of it.

## Claude AI Capabilities

Here are the key areas where Claude excels:

* **Conversation:** Claude is highly capable of engaging in natural conversations, understanding user's context and providing thoughtful responses.
* **Content Creation:** Claude can generate high quality content tailored to requirements set by the user.
* **Language Translation:** In this day and age, global communication is crucial. Claude has multilingual capabilities, allowing translation between different languages in real-time and multi-lingual content creation.
* **Visual processing:** Claude can analyze and transcribe images, including photographs and handwritten notes.
* **Code Generation:** Code generation has become an attractive feature and a key competitive advantage with every new AI model release. Claude can generate code snippets, understand different programming languages, explain code functionality, and assist in debugging.

## Claude vs ChatGPT

Let's compare the differences between ChatGPT and Claude:

### LLM

* Claude 3 is the latest model lineup released on March 2024.
* GPT-4 is the current model since March 2023.

### Performance

At the time of writing, Claude excels in terms of factual accuracy and can maintain context over longer conversations. Claude Opus is shown to outperform GPT-4 in all evaluation benchmarks of AI systems, especially in terms of knowledge and language understanding.

### Context Window

Context window represents the maximum number of tokens an AI system can process in a single input or output. Larger context means the LLM can handle longer text and maintain the context while processing that text.

* GPT-4 has **8,192 tokens**, while a newer version (GPT-4-32k) has **32,768 tokens**.
* All three of Claude 3 versions have a context window of **200k tokens** which is significantly larger than GPT-4.

### Safety

**GPT-4:**

* While safety is a critical aspect of ChatGPT and efforts have been made to mitigate misinformation, the chatbot tends to generate some incorrect output.
* ChatGPT saves conversations with the user to further train and improve the model.

**Claude 3:**

* Claude was developed with safety in mind. Anthropic emphasizes on ethical use of AI in both the training and how the chatbot processes input and generates output. The model strictly follows Constitutional AI.
* Claude does not retain user data.

### Accessibility

Both Claude 3 and GPT-4 models are available directly through the chatbots as well as through API. Additionally, they're accessible in other platforms:

* **GPT-4:** Microsoft invested heavily on OpenAI to integrate their latest LLMs into Microsoft platforms. As of today, GPT-4 is available via Microsoft's Copilot for free.
* **Claude 3:** Anthropic has partnered with companies like Notion, Amazon, and DuckDuckGo to integrate Claude 3 into their products.

## How to Interact with Claude AI

If you're familiar with ChatGPT (by now, that is most likely the case), you should have a similar experience with the Claude chatbot. Once you create an account [here](https://claude.ai/chats), it'll be as simple as typing your queries. 

In this section, we'll focus on interacting with the AI model through the provided API using Python to ask it to explain the concept of neural networks.

To get started, sign up [here](https://console.anthropic.com/login), then navigate [here](https://console.anthropic.com/settings/keys) to create your first API key. Make sure you copy and store the API key in a secure file.

Here's an example of a Python script that instructs Claude to explain the concept of neural networks:

```python
  # import anthropic library
  import anthropic
  
  # create a client instance
  client = anthropic.Anthropic(
      api_key="your_api_key",
  )

  # create the prompt and call the API
  message = client.messages.create(
      model="claude-3-opus-20240229",
      max_tokens=1000,
      temperature=0.0,
      system="Respond in short and clear sentences.",
      messages=[
          {
            "role": "user",
            "content": "Can you explain the concept of neural networks?"
          }
      ]
  )

  print(message.content)
```

Make sure you replace `your_api_key` with the actual API key that you created. 

Let's quickly discuss the parameters defined above:

* `model="claude-3-opus-20240229"` specifies the model to be used.
* `max_tokens=1000` sets the maximum number of tokens that the generated response can have.
* `temperature=0.0` the temperature controls the level of randomness of the generated response. `0.0` means the response will be more consistent and less varied.
* `system="Provide short and clear responses."` specifies how the system should generate the response.
* `messages=[{"role": "user", "content": Can you explain the concept of neural networks?"}]` defines the role and input message based on which the output will be generated.

Here's a sample response in JSON:

```json
{
    "id": "msg_01H4xwvAZnb6XTz8cHPoerBS",
    "type": "message",
    "role": "assistant",
    "content": [
        {
            "type": "text",
            "text": "Neural networks are a type of machine learning algorithm inspired by the structure and function of the human brain. They consist of interconnected nodes, or \"neurons,\" organized in layers. Each neuron receives input, processes it, and passes the output to neurons in the next layer. Through training on large datasets, neural networks learn to recognize patterns and make predictions or decisions.\n\nKey points about neural networks:\n\n1. Structure: Input layer, hidden layer(s), and output layer of neurons\n2. Weights and biases: Each connection has a weight that determines the importance of the input\n3. Activation functions: Determine the output of a neuron based on its input\n4. Training: Networks learn by adjusting weights through backpropagation and optimization algorithms\n5. Applications: Used for tasks like image recognition, natural language processing, and prediction\n\nNeural networks excel at learning complex, non-linear relationships in data and have revolutionized fields like computer vision and speech recognition. However, they require large amounts of training data and computational resources."
        }
    ],
    "model": "claude-3-opus-20240229",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "usage": {
        "input_tokens": 23,
        "output_tokens": 219
    }
}
```

## Conclusion

Claude represents a significant leap in the realm of artificial intelligence that outmatches various competitors in the market.

Claude provides a unique view, a set of standards regarding safety and security, and offers a diverse range of applications, from content creation to code generation.

