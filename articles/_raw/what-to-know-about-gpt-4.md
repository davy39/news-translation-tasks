---
title: What to Know About GPT-4 for Non-AI Developers
subtitle: ''
author: Kaushal Joshi
co_authors: []
series: null
date: '2023-04-06T14:15:36.000Z'
originalURL: https://freecodecamp.org/news/what-to-know-about-gpt-4
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/gpt-4.gif
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: chatgpt
  slug: chatgpt
seo_title: null
seo_desc: 'We are living through an AI revolution. The AI industry is constantly evolving,
  with new tools, products, and technologies emerging every day.

  For those not familiar with the AI domain, keeping up with these developments can
  be challenging.

  The bigge...'
---

We are living through an AI revolution. The AI industry is constantly evolving, with new tools, products, and technologies emerging every day.

For those not familiar with the AI domain, keeping up with these developments can be challenging.

The biggest news recently is undoubtedly GPT-4. Everyone from my barber to Twitter influencers wants to know more. My fellow software developers are not an exception. It feels like having FOMO because we aren't up to date with what's going on in the AI realm.

In this article, we will cover everything that we publicly know about GPT-4. So if you're unfamiliar with terms like ChatGPT, GPT-4, OpenAI, and other buzzwords, this is the guide you need to read.

## History of GPT Until Now

OpenAI announced GPT-3 in 2020. It is a language model trained on a massive dataset available on the internet. It can be your friend and answer your queries, help you debug or write code, solve logical and aptitude questions, translate text, and a lot more.

At the end of 2022, the company released a free preview of [ChatGPT](https://chat.openai.com/). It is a AI chat-bot built with GPT-3.5, the successor to GPT-3. ChatGPT soon became the talk of the town (world!). More than a million people signed up for the preview in just five days.

%[https://twitter.com/gdb/status/1599683104142430208?s=20] 

In January 2023, Microsoft invested (reportedly) $10 billion in OpenAI. We will discuss why this is important later.

And finally, OpenAI [released](https://openai.com/research/gpt-4) GPT-4 in March 2023, which shook the world with its capabilities.

## What is GPT-4?

"Generative Pre-trained Transformer 4" or GPT-4 is a multimodal Large Language Model (LLM). It is more reliable, creative, and can handle more complex instructions than GPT-3.5. It outperforms every known AI model in every measurement parameter.

GPT-4 is OpenAI's efforts at scaling up deep learning. It is the most capable AI model yet. Though it is less capable than humans in many real-world scenarios, it excels at several professional and academic benchmarks with human-level precision.

## Availability of GPT-4

GPT-4 is not available for everyone, unlike ChatGPT. There are several ways you can get access to it:

1. [**API Waitlist**](https://openai.com/waitlist/gpt-4-api): You can sign-up for the waitlist and get rate-limited access to the GPT-4 API
    
2. **Priority access**: Developers can contribute to [OpenAI Evals](https://github.com/openai/evals) and get API access once the contribution is merged.
    
3. [**ChatGPT Plus**](https://openai.com/blog/chatgpt-plus): It is also available for ChatGPT Plus subscribers with a $20 monthly fee.
    
4. **Microsoft Bing**: It also powers Microsoft's recently revamped Bing Search Engine. It is currently available for selected users.
    
5. **Third-party Services**: OpenAI has collaborated with several organizations to integrate GPT-4, like Duolingo, Morgan Stanley, and Khan Academy, to name a few.
    

## Capabilities of GPT-4

GPT-4 outperforms the majority of humans in various professional and academic benchmarks. The company tested the latest model with the previous one with some of the toughest exams in the world. And GPT-4 excelled at everything thrown to it by significant numbers.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-259.png align="left")

*comparing GPT-4 with GPT-3.5 in various competitive exams (source: OpenAI)*

OpenAI published a [technical paper](https://arxiv.org/abs/2303.08774) that analyzes this further.

The team spent 6 months making GPT-4 safer and more aligned. GPT-4 is 82% less likely to respond to requests for disallowed content and 40% more likely to produce factual responses than GPT-3.5 on our internal evaluations.

## New and Improved Input Methods

GPT-4 serves user prompts intelligently. It is better at handling large texts and image inputs. It can also change its personality to talk to you!

### Provide prompts up to 25,000 words

The GPT-3.5 could only handle text entries of up to 3,000 words. GPT-4 goes far beyond this, accepting entries of up to 25,000 words. It can also accept graphical contributions.

Though GPT-4 struggles when dealing with large amounts of data, it is still superior to GPT-3.5. The increased input length will help you to contextualize your prompts more clearly. You can provide entire documents, theses, and webpages as a prompt all at once.

### Upload an image as a prompt

Image inputs are still a research preview yet to be publicly available. As of now, only [be my eyes](https://www.bemyeyes.com/) supports the latest image inputs.

Nonetheless, image inputs have identical capabilities and functionalities as text inputs. Users can specify vision or language to get their desired output. It can also be augmented with test-time techniques developed for text-only language models, including few-shot and chain-of-thought prompting.

One more observation about input prompts is that GPT-4 remembers earlier conversations within a single chat session. It can back-reference what it said in the past or bring out what you prompted as well. But it can not remember conversations between different sessions yet.

### You can change its personality

I must say, I am fan of this feature. LLMs can change their personalities and behavior as per user prompts. We call it "steerability" in AI.

GPT-3.5 has a fixed personality with predefined vocabulary, tone, and style. Anything that it answers feels the same. With GPT-4, we can describe personalities in the system message. The company explains in its blog that it's easier for ChatGPT to break its character, so the personality is changed only "within bounds".

This is helpful in scenarios where you want the answer to be like a specific personality. You can tell it to be a sympathetic listener, guide, mentor, tutor and so on.

The blog explains steerability by giving an example of a Socratic tutor. The [Socratic Method](https://en.wikipedia.org/wiki/Socratic_method) is a discussion between an individual with themselves or others that finds solutions by constantly asking questions and answering them with critical thinking. Using the Socratic method, we can critically think about a complex problem and understand it better.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-22.png align="left")

## ChatGPT Plugins

And when we thought everything was cooling off, OpenAI announced plugins for ChatGPT. Until now, GPT-4 solely relied on its training data, which was last updated in September 2021. It was not connected to the external world.

With plugins, it can access the entire internet. Users can install plugins in their ChatGPT to allow it to access the external world. Now it can interact with real world and updated data to perform various tasks for you.

Plugins can act as "eyes and ears" for LLMs. This allows LLMs to access information unavailable in their training data. This includes data that's too recent, personal, or specific to be included in the training data. Plugins can use such information to produce better, highly accurate, and precise outcomes.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-20.png align="left")

*11 companies partnering up with OpenAI to build plugins (Source:*[*OpenAI Blog*](https://openai.com/blog/chatgpt-plugins)*)*

OpenAI has partnered with 11 companies to create such plugins. Expedia, FiscalNote, Milo, and Zapier are some companies that have already made their plugins. The company also hosts two plugins: a web browser and a code interpreter. It has [open-sourced](https://github.com/openai/chatgpt-retrieval-plugin) a knowledge base retrieval plugin.

You can join the waitlist by submitting your interest on its [website](https://openai.com/waitlist/plugins). If you want to read more, I recently wrote a [blog](https://www.showwcase.com/show/34206/chatgpt-has-a-game-changer-update) that discusses plugins in detail.

## What's Built with GPT-4?

There are several tools available today that are built on GPT-4. OpenAI partnered with different companies in two stages. The first stage was for the launch of GPT-4 itself.

### Microsoft

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-28.png align="left")

*Source: Unsplash (Ed Hardie)*

At the start of the article, I mentioned that Microsoft invested $10 billion in OpenAI. Microsoft is integrating GPT-4 into its existing suite of services, mainly Office-365 and Microsoft Edge. Here is a brief description of every Microsoft tool or service integrated with OpenAI services/GPT-4.

1. [**Copilot for the Web**](https://blogs.microsoft.com/blog/2023/02/07/reinventing-search-with-a-new-ai-powered-microsoft-bing-and-edge-your-copilot-for-the-web/)**:** Microsoft Bing and Edge have integrated GPT-4 for a better, more complete and creative experience.
    
2. [**OpenAI in Azure**](https://azure.microsoft.com/en-us/blog/chatgpt-is-now-available-in-azure-openai-service/)**:** ChatGPT is available in preview in Azure OpenAI Service.
    
3. [**Copilot X**](https://www.showwcase.com/show/34112/everything-you-need-to-know-about-github-copilot-x)**:** GitHub, a Microsoft owned product, also introduced Copilot X that leverages GPT-4 for new features.
    
4. [**Copilot for Work**](https://blogs.microsoft.com/blog/2023/03/16/introducing-microsoft-365-copilot-your-copilot-for-work/): Microsoft introduced Microsoft 365 Copilot, which aims to turn your words into the most powerful productivity tool on the planet.
    

### Duolingo

![Image](https://blog.duolingo.com/content/images/2023/02/DuoNews-622x296--1-.png align="left")

*Dulingo Max (Source:* [*Dulingo blog*](https://blog.duolingo.com/duolingo-max/)*)*

Dulingo integrated GPT-4 and launched [**Dulingo Max**](https://blog.duolingo.com/duolingo-max/)**.** It introduces two new features: Explain My Answer and Roleplay. The first explains why user's answers were right or wrong, and provides further examples for better clarification. The latter allows learners to practice real-world conversation skills with world characters in the app.

### Be My Eyes

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-25.png align="left")

*source: Internet*

Be My Eyes is a platform for visually impaired people to help them interpret the world better. GPT-4 acts as a virtual volunteer and analyzes images through GPT-4's image-to-text generator. It doesn't just analyze the content of the image but the context of the image as well.

### Khan Academy

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-26.png align="left")

*Source:* [*Khan Academy*](https://www.khanacademy.org/khan-labs)

Khan Academy is also one of the early adopters of GPT-4. It intends to use GPT-4 as a study and technical assistant. It can help students in exam preparation, improving and practicing vocabulary, and so on. It can also help teachers in administrative tasks, writing lessons and creating lesson hooks, writing exit tickets, and similar tasks.

### Stripe

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-27.png align="left")

*Source:* [*Stripe*](https://stripe.com/en-in)

Now, Stripe is integrating GPT-4 into its platform. The company already used GPT-3 for simple tasks, but integrating GPT-4 means AI will play a bigger role in the company's processes. It intends to use GPT-4 to streamline the user-experience and add another layer of fraud detection.

## What Competitors are Doing

People started using ChatGPT and Microsoft Sydney for their internet searches. Google recognized the imminent threat to their business and acted quickly. The company announced "Bard", its own AI Chatbot that competes with GPT-4.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-19.png align="left")

*Source:* [*Google*](https://bard.google.com/)

Google Bard is a generative AI chatbot that can produce text responses based on user queries or prompts. Bard uses its own internal knowledge and creativity to generate answers. Bard is powered by a new version of LaMDA, Google's flagship large language model that has been fine-tuned with human feedback.

Bard allows speech inputs along with plain text. It also allows you to make a Google search with the same prompt to verify Bard's answers.

One thing to note here is that Bard constantly reminds us that it is still an experimental model, and it may hallucinate. It also doesn't forget to mention that Google does not support any views and opinions Bard may tell.

Google Bard is currently available in the United States and Britian. You can join the waitlist by visitng [Bard's official website](https://bard.google.com/). I wrote a [blog](https://www.showwcase.com/show/34094/everything-you-need-to-know-about-bard) discussing more about Bard. Make sure you read it too.

## Will AI Take Your Job?

After reading the entire article, you might feel concerned about your job. OpenAI, OpenReseach, and the University of Pennsylvania published a paper, "[**GPTs are GPTs: An Early Look at the Labor Market Impact Potential of Large Language Model**](https://arxiv.org/abs/2303.10130)", to analyze the potential impact of such tools on the labor market.

According to the study, 10% of tasks in 80% of US workers can be done by LLMs. For the other ~19% of workers, LLMs could influence at least 50% of tasks. Higher-income jobs will potentially face greater exposure. Programming and writing jobs will also be impacted. On the other hand, jobs that require critical thinking and science are safe. Similarly, jobs with a low barrier to entry are less likely to be impacted.

These jobs are more likely to taken over by AI:

* mathematicians
    
* tax preparers
    
* writers
    
* web designers, programmers
    
* accountants
    
* journalists
    
* legal secretaries
    

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-17.png align="left")

*AI will be more likely to take these jobs (Source:*[*Research Paper*](https://arxiv.org/abs/2303.10130)*)*

Jobs that are less likely to be impacted by GPT are as follows:

* graphic designers
    
* search marketing strategies
    
* financial managers
    

The researchers also list LLM's impact on various industries. Industries with the most significant impact are as follows:

* data processing services
    
* information services
    
* publishing industries
    
* insurance carriers
    

On the other hand, the industries with the most negligible impact are:

* food manufacturing
    
* wood product manufacturing
    
* support manufacturing
    
* agriculture forestry
    

![AI is very unlikely to take these jobs (Source: Research paper)](https://www.freecodecamp.org/news/content/images/2023/04/image-18.png align="left")

*AI is very unlikely to take these jobs (Source:* [*Research paper*](https://arxiv.org/abs/2303.10130)*)*

## Epilogue

If you read all the way through this, give yourself a pat on the back! You have come a long way, and you should know know enough about this crazy buzzword to share your knowledge in meetings and catchups.

I hope you learned something in this overview of ChatGPT. If you did, share it within your networks so that everyone can benefit from it.

Almost every bit of information has been curated from existing announcement blogs, research papers, and content put by official company handles. Still, if you find a mistake or an improvement, please let me know. I would be happy to correct my mistakes.

Let's connect! I want to know what you think about this article. Do you think AI will replace our jobs? Let me know. Here is how you can reach me:

* [Twitter](https://twitter.com/clumsy_coder)
    
* [Person](https://kaushaljoshi.dev/)al Website
    
* [Showwcase](https://www.showwcase.com/clumsycoder)
    
* [Peerlist](https://peerlist.io/kaushal)
    

Finally, check out my [personal blog](https://blog.kaushaljoshi.dev/), where I write about front-end development, open-source, technology, and technical writing.

Stay curious! ✨
