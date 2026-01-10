---
title: How I made my ChatBot smarter by helping it understand intent
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-18T17:37:18.000Z'
originalURL: https://freecodecamp.org/news/how-i-made-a-smarter-chatbot-with-intents-5e6ad6e0fd71
coverImage: https://cdn-media-1.freecodecamp.org/images/0*e-7HD__g3J0-Ix8h
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: '#chatbots'
  slug: chatbots
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By P. Daniel Tyreus

  Using deep learning tools to better understand conversations about seasonal allergies

  I’ve been working on a chatbot to help understand seasonal allergies as a side project
  for quite a while. This time every year, my allergies fla...'
---

By P. Daniel Tyreus

Using deep learning tools to better understand conversations about seasonal allergies

I’ve been working on a chatbot to help understand seasonal allergies as a side project for quite a while. This time every year, my allergies flare up and my motivation to improve [Hayfever](https://hayfever.io) also has a resurgence.

Early this Spring, I took some time to review how well my chatbot was communicating with users. The results where humbling to say the least. So I looked into improving my chatbot’s performance by integrating a modern natural language understanding system based on deep learning. This article discusses what went wrong with my early approaches and how I fixed it.

### First Pass: Dialog Trees

I built the “intelligence” behind the first version of the Hayfever chatbot using an mechanic known as a [dialog tree](https://en.wikipedia.org/wiki/Dialog_tree). Anyone who has ever seen a role playing video game has experienced a dialog tree. In it’s classic form, a character in the game speaks some dialog and the player is given a choice of responses.

An even more primitive ancestor is the interactive voice response ([IVR](https://en.wikipedia.org/wiki/Interactive_voice_response)) system. Most of us have probably had the displeasure of interacting with an IVR when dialing in to the customer support line at our bank. These mechanics are easy to program and **work adequately when the domain of possible responses is limited to the choices presented**.

In the computer game, you can only select from the choices on the screen, and with the IVR you can only press numbers based on the choices given.

With chatbots, the possible answers are not at all limited. A user can type in whatever they has on their mind. But when I first implemented the Hayfever chatbot in Facebook Messenger, I didn’t have access to the technology to parse input in a sophisticated way. So I used the “quick reply” feature to try to force the conversation along specific lines, much like a dialog tree.

![Image](https://cdn-media-1.freecodecamp.org/images/Cuz5hCGmyBUZOwpXSc-phjZiok6MAddfovv8)
_Attempting to force the conversation direction using quick reply buttons._

### Second Try: Conversation Graphs

After observing the chatbot in the wild, I understood almost immediately that this approach would not work. Even if users were presented with a few quick replies, there was nothing stopping them from typing in something altogether different.

In the second iteration, I decided that a tree structure was too rigid and I needed to model the conversation as a directed graph instead. I couldn’t find any framework that quite fit my needs. So I wrote my own graph-based dialog engine called [conversation-kit](https://github.com/pdtyreus/conversation-kit).

A **directed graph** has some advantages over a tree structure, in this case because it **can let the conversation fork and flow more naturally**. Without getting too much into the details, the vertices on the graph represent statements or questions from the chatbot. The edges represent possible responses from the user. So the conversation flows from vertex to vertex along the edges that match the user’s response.

![Image](https://cdn-media-1.freecodecamp.org/images/JZ6PrSRMJM5JI5vwQQtZlFaFf4ShBNLxTCgS)
_The chatbot’s conversation visualized as a graph. Each vertex represents something the bot can say, and each edge represents a possible next statement in the conversation._

As long as the user didn’t stray far from the set of responses defined by the edges in the graph, this worked pretty well. For instance, below is a chat I had with Hayfever on Facebook Messenger.

![Image](https://cdn-media-1.freecodecamp.org/images/pBYi8RR-PeMyB-iPPghx9SW76MQKrdaOji22)
_A successful chat with Hayfever on Facebook Messenger using the graph-based conversation model._

Since I programmed the model, I basically knew what I could say to get the desired response. Other users would not have this knowledge. So while this version was better, it still suffered some serious drawbacks.

First, if a user’s response did not match any edges, the bot just got stuck in a loop of saying it did not understand. Second, the algorithm I wrote to match responses to edges was **really primitive and frequently misunderstood** what the user was saying. Finally, if the user wanted to change the subject while in the middle of a conversation, he or she would essentially need to know a trigger phrase like “help” to reset the position in the graph.

Below are some examples of the resulting unnatural and frustrating conversations.

![Image](https://cdn-media-1.freecodecamp.org/images/sabbwOL8d-cdfsD--Yjy4qHUKIyuzC0HAPO2)
_Hayfever clearly misunderstanding a user resulting in an unnatural and frustrating conversation._

![Image](https://cdn-media-1.freecodecamp.org/images/WAKTt3UY73ysHlqIMlByydGxOBQSf-gabcxa)
_A user making a natural request that Hayfever could not understand since it did not match an existing edge in the graph._

In the examples above, it’s clear that my chatbot was not at all understanding what the user was intending to convey. In other words, **it did not understand the intent of each statement**.

Humans are incredibly good at understanding subtle intent from spoken conversation. Most people effortlessly combine cues from facial expressions, body language, and intonation to gauge intent. On top of that, we incorporate knowledge of the person we are talking to, contextual details from previous conversations, and possible cultural references to further refine the meaning of what a person is saying to us.

Modern artificial intelligence technologies are nowhere near as good as humans in this arena. But **advances in deep learning** over the last few years have **significantly improved a computer’s ability to discern intent** from spoken or written text. At the very least, the state of the art is far, far better than the primitive technology I was using to match responses to edges.

### Third Try: Understanding Intent

After studying the interactions my chatbot was having with users, I realized I needed a more sophisticated strategy. I really needed a way to better understand a user’s intent.

My first experience with intent was when I was programming a custom skill for Amazon’s Alexa service. The Alexa service converts the words you speak to a device like an Echo into written text. It then checks to see if the words match any of the built in intents like “help” or “exit.”

As a developer, you can also define your own intents by defining **utterances** that match the same **intent**. For example, the utterances “what are the conditions today?”, “how much pollen is in the air?”, and “are the allergy conditions bad?” might all be the user expressing their intent to ask for a conditions report. The smarts behind this is that you don’t have to define every variation of an **utterance** for a given **intent**. The processing algorithm is often good enough to match similar **utterances** to the same **intent**.

For a chatbot developer, this is great. Instead of dealing with generating responses for hundreds or thousands of different inputs, I can just focus on generating responses for a handful of pre-defined intents.

My primitive regular expression matching was easy to code on my own. But the state of the art technology behind converting an utterance into an intent is quite sophisticated. Fortunately, there are several well-known vendors who offer Natural Language Understanding as a service.

* Microsoft Cognitive Services Language Understanding ([LUIS](https://www.luis.ai/home))
* Amazon Web Services [Lex](https://aws.amazon.com/lex/)
* Google [Dialogflow](https://dialogflow.com/)
* Facebooks [wit.ai](https://wit.ai/)

All of these services advertise themselves as “advanced deep learning” technologies for “building conversational interfaces.” All of them are API-based, meaning that they can be integrated into almost any application that has a connection to the Internet. And all offer a free tier at the usage level I currently needed.

For this project, I chose Dialogflow. I found the user interface pleasant, the APIs understandable, and it required almost no vendor lock in. It also included a fun add-on called [Small Talk](https://dialogflow.com/docs/small-talk) that easily let my bot reply to casual conversation like “how are you?” and “what’s your name.” Oddly enough I noticed from the logs that plenty of users enjoyed exchanging casual pleasantries with my bot.

### Using Dialogflow

The application loop when using an NLU service is actually simpler than what I had before. The bot is completely event driven. It waits for input from a user via a Facebook Messenger web hook, passes the text to Dialogflow to parse the intent, generates the appropriate response for the intent, and sends the formatted response back to the Facebook Messenger API.

![Image](https://cdn-media-1.freecodecamp.org/images/JmPRkmoeD3mjXA43CSC8ZDVyv-tgw3SFlMhS)

Updating Hayfever to use Dialogflow was relatively smooth, with a couple exceptions.

First, it seems like I caught Dialogflow in the middle of a migration from their V1 to V2 API and the documentation had not quite caught up. When searching StackOverflow and other blogs, there was quite a bit of outdated information that referred to the V1 API.

Second, Hayfever is a Facebook Messenger bot. The JSON format for embedding Facebook Messenger responses in the DialogFlow API is quite poorly documented. If I had chosen Facebook’s wit.ai instead, I’m sure this part would have been easier. But I want Hayfever to work on **any messaging platform as well as voice platforms in the future**.

So I completely decoupled the Dialogflow intent processing from the Messenger response formatting. So the Dialogflow code has no idea that input is coming from Messenger, and Messenger has no idea that Dialogflow is parsing the intents. It wasn’t the easiest way to build this, but it’s quite future-proof.

Switching to the Dialogflow NLU immediately improved the quality of Hayfever’s conversations. **The bot was no longer thrown off by subtle variations in expected inputs, it could make small talk with users, and it could even guess at intents from inputs it had never seen before**. There is still a lot of training and optimizing I can do, but this is clearly a move in the right direction.

### Wrapping Up

[Hayfever](https://hayfever.io/) is chatbot designed to help users track and understand allergy symptoms. Early versions used primitive dialog tree mechanics and were quite poor at understanding natural conversation. Swapping in a deep learning-based natural language understanding (NLU) service like Dialogflow dramatically improved Hayfever’s ability to converse with users.

By keeping the NLU processing separate from the platform-specific input and output, there was almost no increase in code complexity and no platform lock in.

In the future I hope to make Hayfever available on voice devices like Amazon Alexa and Google Home, as well as additional messaging platforms like Telegram. I would also like to try combining the NLU with some of the graph-based conversation tools I used previously to perhaps give the chat bot better memory of what has already happened in the conversation.

