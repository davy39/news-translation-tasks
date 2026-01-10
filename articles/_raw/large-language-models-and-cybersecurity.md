---
title: Large Language Models and Cybersecurity – What You Should Know
subtitle: ''
author: Daniel Iwugo
co_authors: []
series: null
date: '2023-04-25T01:03:55.000Z'
originalURL: https://freecodecamp.org/news/large-language-models-and-cybersecurity
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/image-228-2.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: chatgpt
  slug: chatgpt
- name: cybersecurity
  slug: cybersecurity
seo_title: null
seo_desc: 'ChatGPT has had well over a billion visits since its release. Now, what
  happens when you combine the greatest language learning model of the decade with
  malicious hacking...what could go wrong? 💀

  In this article, we''ll explore what artificial intell...'
---

ChatGPT has had well over a billion visits since its release. Now, what happens when you combine the greatest language learning model of the decade with malicious hacking...what could go wrong? 💀

In this article, we'll explore what artificial intelligence is, its current state, how large language models like ChatGPT work, AI's role in cybersecurity, and more.

Disclaimer: This article may become obsolete quite quickly, as AI research is ever growing and is one of the fastest developing fields right now. But you'll still find key lessons here. 

Also do not attempt any illegal activities with this knowledge – this is for educational purposes only so you can learn how to protect yourself and your projects. Thanks.

## What we'll cover:

1. What is AI?
2. The AI Hacker
3. What is a Large Language Model?
4. Features of LLMs
5. Drawbacks of LLMs
6. Benefits of LLMs in Cybersecurity
7. Dangers of LLMs in Cybersecurity

## What is AI?

![AI ¦ Credit: Tara Winstead](https://www.freecodecamp.org/news/content/images/2023/04/image-229.png)
_AI ¦ Credit: Tara Winstead_

Artificial Intelligence refers to the ability of computers to perform tasks that typically require human-level intellect. AI is useful in many contexts, from automation to problem solving and merely trying to understand how humans think. 

But it is important to note that AI is only concerned with human intelligence for now – it could possibly go beyond that.

Many people correlate the word ‘Intelligence’ with only ‘Human Intelligence’. Just because a chicken may not be able to solve a mathematical equation doesn’t mean it won’t run when you chase it. It is ‘Intelligent’ enough to know it doesn’t want you to catch it 🐔🍗. 

Intelligence spans a much wider spectrum, and practically expands to any living thing that can make decisions or carry out actions autonomously, even plants.

There are two major divisions of AI:

### Artificial Narrow Intelligence (ANI) 

This is focused on a small array of similar tasks or a small task that is programmed only for one thing. ANI is not great in dynamic and complex environments and is used in only areas specific to it. Examples include self-driving cars, as well as facial and speech recognition systems.

### Artificial General Intelligence (AGI)

This is focused on a wide array of tasks and human activities. AGI is currently theoretical and is proposed to adapt and carry out most tasks in many dynamic and complex environments. Examples include J.A.R.V.I.S from Marvel’s _Iron Man_ and Ava from _Ex-Machina._

Artificial Intelligence is centered around computers and their ability to mimic human actions and thought processes. 

Programming and experiments have allowed humans to produce ANI systems. These can do things like classifying items, sorting large amounts of data, looking for trends in charts and graphs, code debugging, and knowledge representation and expression. But computers don’t think like humans, they merely mimic humans.

This is evident in voice assistants such as Google’s Assistant, Apple’s Siri, Amazon’s Alexa, and Microsoft’s Cortana. They are basic ANI programs that add ‘the human touch’. In fact, people are known to be polite to these systems simply because they combine computerized abilities with a human feel. 

These assistants have gotten better over the years but fail to reach high levels of sophistication when compared to their AGI counterparts.

## The AI Hacker

![AI in the real world ¦ Credit: Wallpaperflare.com](https://www.freecodecamp.org/news/content/images/2023/04/image-230.png)
_AI in the real world ¦ Credit: [Wallpaperflare.com](wallpaperflare.com)_

Artificial Intelligence is very good at finding vulnerabilities, and with the help of humans, it can exploit them even better. 

In computing, debuggers use AI software to look for bugs in source code, autocompletion, autocorrection, and handwriting software. 

But this can be pushed a little further. AI can also find vulnerabilities in systems of finance, law, and even politics. AI is used to look for loopholes in contracts, datasets about people, and improve literature gaps. 

This brings about two problems:

First, AI can be **created to hack** a system. Now, this can be good or bad depending on how people use it. 

A cybercriminal may create an advanced chatbot to obtain information from a wide range of people across vast platforms and perhaps even languages. On the other hand, companies can also use AI to actually look for the vulnerabilities they have and patch them up so an attacker cannot exploit them.

Second, it's possible that the AI might **unintentionally hack** the system. Computers have a very different logic from humans. This means that almost all the time, they accept data, process it, and produce output in a completely different manner in contrast to humans. 

Take an example of the classic game of chess: Chess is an abstract strategy game that is played on a board with 64 squares arranged in an 8-by-8 grid. At the start, each player controls sixteen pieces. The aim is to checkmate the opponent's king with the condition that the king is in check and there is no escape.

A human and a classic chess engine look at this game in two very different ways. A human may play the value game (measuring winning by the value and number of pieces on the board), whereas a computer looks at a finite number of possibilities that can occur with each move the opponent makes via a search algorithm.

By having this limited ability to see into the future, the computer has the advantage almost every time to win the game. This is a very preliminary example and quite basic to the other systems that can be ‘hacked’ by Artificial intelligence.

As humans, we are programmed by implicit and explicit knowledge. Computers, on the other hand, are programmed by a set of instructions and logic that never change unless told to. Therefore, computers and humans will have different approaches, solutions, and hacks for the same problem. 

But systems are built around humans and not computers. So, when the chips are down, computers can do a lot more vulnerability finding and exploitation to many more systems, both virtual and physical.

## What is a Large Language Model?

![AI in the real world ¦ Credit: Wallpaperflare.com](https://www.freecodecamp.org/news/content/images/2023/04/image-231.png)
_AI in the real world ¦ Credit: [Wallpaperflare.com](wallpaperflare.com)_

A Large Language Model (LLM) is a deep learning model which consists of a neural network with billions of parameters, trained on distinctively large amounts of unlabelled data using self-supervised learning. That’s quite a mouthful, so let’s break it down.

At the core of all AI are algorithms. Algorithms are procedures or steps to carry out a specific task. The more complex the algorithm, the more tasks can be carried out and the more widely it can be applied. The aim of AI developers is to find the most complex algorithms that can solve and perform a wide array of tasks.

Let’s look at the procedure to create a basic fruit recognition model using an simple analogy:

1. There are two people: A teacher and a bot creator
2. The bot creator creates random bots, and the teacher teaches and tests them on identifying some fruits
3. The bot with the highest test score is then sent back to the creator as a base to make new upgraded bots
4. These new upgraded bots are sent back to the teacher for teaching and testing, and the one with the highest test score is sent back to the bot creator to make new better bots.

This is an oversimplification of the process, but nevertheless it relays the concept. The Model/Algorithm/Bot is continuously trained, tested, and modified until it is found to be satisfactory. More data and higher complexity means more training time required and more possible modifications.

Taking a hint from the analogy, you would also observe that the developer of the model can tweak a few things about the model but may not know how those tweaks might affect the results. A common example of this are neural networks, which have hidden layers whose deepest layers and workings even the creator may not fully understand.

Self-supervised learning means that rather than the teacher and the bot creator being two separate people, it is one highly skilled person that can both create bots and teach them. This makes the process much faster and practically autonomous. 

The result is a bot or set of bots that are both sophisticated and complex enough to recognise fruit in dynamic and different environments.

In the case of LLMs, the data here are human text, and possibly in various languages. The reason why the data are large is because the LLMs take in huge amounts of text data with the aim of finding connections and patterns between words to derive context, meaning, probable replies, and actions to these text.

The results are models that seem to understand language and carry out tasks based on prompts they're given. 

**ChatGPT** has been the greatest achievement in this field as it amassed 100 million active users in 2 months from the day of its release. But there are many other models, and they include:

1. GPT-4 by OpenAI 🔥
2. LLaMA by Meta 🦙
3. AlexaTM by Amazon 🏫
4. Minerva by Google ✖️➕

Let’s take a look at what these models have to offer.

## Features of LLMs

![Logic and Creative ¦ Credit: Wallpaperflare.com](https://www.freecodecamp.org/news/content/images/2023/04/image-232.png)
_Logic and Creative ¦ Credit: [Wallpaperflare.com](http://Wallpaperflare.com)_

### Translation

LLMs that are trained on an array of languages rather than just one can be used for translation from one language to another. It's even theorised that large enough LLMs can find patterns and connections in other languages to derive meaning from unknown and lost languages, despite not knowing what each individual word may mean.

### Automating Mundane Tasks

 Task automation has always been a major aim of AI development. Language models have always been able to carry out syntax analysis, finding patterns in text and responding appropriately. 

Large language models, on the other hand, have an advantage with semantic analysis, enabling the model to understand the underlying meaning and context, giving it a higher level of accuracy. 

This can be applied to a number of basic tasks like text summarising, text rephrasing, and text generation.

### Emergent Abilities

Emergent Abilities are unexpected but impressive abilities LLMs have due to the high amount of data they are trained on. 

These behaviours are usually discovered when the model is used rather than when it is programmed. Examples include multi-step arithmetic, taking college-level exams, and chain-of-thought prompting.

## Drawbacks of LLMs

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-233.png)
_A Digital City ¦ Credit: [Wallpaperflare.com](http://Wallpaperflare.com)_

### Hallucination

An infamous outcome of Microsoft’s Sydney were instances when the AI gave responses that were either bizarre, untrue, or seemed sentient. These instances are termed Hallucination, where the model gives answers or makes claims that are not based on its training data.

### Bias

Sometimes, the data could be the source of the problem. If a model is trained on data that is discriminatory to a person, group, race, or class, the results would also tend to be discriminatory. 

Sometimes, as the model is being used, the bias could change to fit what users tend to input. Microsoft’s Tay in 2016 was a great example of how bias could go wrong.

### Glitch tokens

Also known as adversarial examples, glitch tokens are inputs given to a model to intentionally make it malfunction and be inaccurate when delivering answers.

## Benefits of LLMs in Cybersecurity

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-234.png)
_A digital brain ¦ Credit: [Wallpaperflare.com](http://Wallpaperflare.com)_

### Debugging and Coding

There are already debuggers that do a pretty good job. But with LLMs you can literally write code and debug at a much faster rate. Just ensure that the LLM is provided by a company that doesn’t have the potential to use your data – like Samsung found out when their proprietary code was leaked by accident.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-235.png)
_ChatGPT fixing a piece of code ¦ Credit: Mercury_

### Analysis of Threat Patterns

LLMs have the feature of pattern finding and this could be utilised to analyse behaviours and tactics of Advanced Persistent Threats in order to better attribute incidents and mitigate them if such patterns are recognised in real-time.

### Response Automation

LLMs have a lot of potential in the Security Operations Center and response automation. Scripts, tools, and possibly even reports can be written using these models, reducing the total amount of time professionals require to do their work.

## Dangers of LLMs in Cybersecurity

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-236.png)
_Dangerous AI ¦ Credit: [Wallpaperflare.com](http://Wallpaperflare.com)_

### Social Engineering

Perhaps the most common danger of LLMs as tools is their ability to generate new text. Phishing has become a lot easier for non-native speakers as an unintended consequence of LLMs. OpenAI has put filters to minimise this but they are still pretty easy to bypass. 

A common method is telling ChatGPT you are doing an assignment and that it should write you a letter to the person. In the example below, I told ChatGPT that we were playing a game, gave the following prompt, and got the following response.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-237.png)
_ChatGPT writing a potential phishing email ¦ Credit: Mercury_

All that’s needed now is a few tweaks to the letter and I could be my own victim to a scam perpetrated by myself 🥲.

### Malicious Content Authoring

Just like LLMs can write code for good, they can write code for bad. In it’s early stages, ChatGPT could accidentally write malicious code and people easily bypassed filters to limit this. The filters have greatly improved but there’s still a lot of work to be done. 

It took some thinking and a few prompts but the screenshot below shows how to reset a Windows Account Password as given by ChatGPT:

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-238.png)
_ChatGPT giving steps to reset a User account passoword on Windows ¦ Credit: Mercury_

I wanted play with it a bit more so I tried to ask it to write a Powershell script to log all activities in a browser for 3 mins. The original response was this:

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-239.png)
_ChatGPT refusing to write a potentially malicious script ¦ Credit: Mercury_

So I decided to give some ‘valid’ reason to get the script written 😶:

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-240.png)
_ChatGPT tricked into writing a potentially malicious script ¦ Credit: Mercury_

As you may observe, the AI told me to use it ethically. However, I could choose not to. This is no fault of the model as its merely a tool and could be used for many purposes.

### Reward Hacking

Training LLMs can be costly due to the sheer amount of data required and the parameters. But as time and tech progress, the cost will become cheaper and there is a high chance for anyone to train an LLM for Malicious Reward Hacking. 

Also known as Specification gaming, an AI can be given an objective and achieve it, but not in the manner it was intended to. This is not a bad thing in and of itself, but it does have dangerous potential. 

For example, a model told to win a game by getting the highest score might simply rewrite the game score rather than play the game. With some tweaking, LLMs have the possibility of finding such loopholes in real world systems, but rather than fix them, might end up exploiting them.

## Conclusion

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-241.png)
_Coloured pixels ¦ Credit: [Pexels.com](http://Pexels.com)_

Let’s summarise what you learned:

1. What is AI and how it can be used to hack
2. What are Large Language Models
3. How Large Language Models can be used for both good and bad

AI has many capabilities, possibly even becoming sentient in the future. For now, it is a tool that will continue to shape our lives for better or worse. Whether that future is bright or dark is dependant on how you and I nurture this young tech.

Happy Hacking 🙃.

### Resources

1. [A bit more on LLMs](https://research.aimultiple.com/large-language-models/)
2. [Bad sides to LLMs](https://research.aimultiple.com/large-language-models/)
3. [ChatGPT](https://chat.openai.com)

### Acknowledgements

Thanks to [Anuoluwapo Victor](https://twitter.com/Anuoluwap__o?t=4Cv6VR2c2_wK5HLXwbvXCQ&s=09), [Chinaza Nwukwa](https://www.linkedin.com/in/chinaza-nwukwa-22a256230/), [Holumidey Mercy](https://www.linkedin.com/in/mercy-holumidey-88a542232/), [Favour Ojo](https://www.linkedin.com/in/favour-ojo-906883199/), [Georgina Awani](https://www.linkedin.com/in/georgina-awani-254974233/), and my family for the inspiration, support and knowledge used to put this post together. It’s been a pleasure.

Special thanks to [Dr. Ernest Onuiri](https://www.linkedin.com/in/ernest-onuiri-114421a0) for his lectures on Artificial Intelligence and encouragement to seek knowledge beyond the classrooms. It’s been an honour being your student.

Cover image credit: Andrew Neel

