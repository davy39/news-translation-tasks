---
title: How to Recover from Deployment Hell – What I Learned After My Discord Bot Crashed
  on a 1,000+ User Server
subtitle: ''
author: Lynn Zheng
co_authors: []
series: null
date: '2021-06-04T20:41:29.000Z'
originalURL: https://freecodecamp.org/news/recovering-from-deployment-hell-what-i-learned-from-deploying-my-discord-bot-to-a-1000-user-server
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/Untitled126_20210603134910.PNG
tags:
- name: '#chatbots'
  slug: chatbots
- name: deployment
  slug: deployment
- name: discord
  slug: discord
- name: lessons learned
  slug: lessons-learned
- name: Life lessons
  slug: life-lessons
seo_title: null
seo_desc: 'I built a Discord AI Chatbot in my last blog post and then, to challenge
  myself, proceeded to stress-test it on a Discord server with 1,000+ users.

  In the first hour, Deployment Hell struck and I had to take the bot down for maintenance.
  Another hour...'
---

I built [a Discord AI Chatbot in my last blog post](https://www.freecodecamp.org/news/discord-ai-chatbot/) and then, to challenge myself, proceeded to stress-test it on a Discord server with 1,000+ users.

In the first hour, Deployment Hell struck and I had to take the bot down for maintenance. Another hour passed and I managed to patch up my bot and send it back.

Now my bot is up and running and more resilient than ever. As for me, I survived and even thrived in Deployment Hell 🔥. In this deployment postmortem, I'm going to show you how.

I sent my AI chatbot into the server at 2 pm on June 2nd, and hype started gathering around it. The chat went on for a while and all was nice and smooth.

At 3:20 pm, everything started falling apart: My free-tier API key reached its hourly request limit, and I had no choice but to take down the bot and the server for maintenance.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/IMG_0676.PNG align="left")

*Never mind the typos in my message 😅 This incident caught me totally unprepared*

Despite being struck by Deployment Hell in the first hour on the first day of my project debut, I knew I need to sit down, take a deep breath, and recover from this incident.

# What Went Well with Deployment

As a first step, I didn't forget to congratulate myself on what went well despite this mishap. Clearly, people were enthusiastic about chatting with my chatbot, to the extent that we went over rate limit.

Moreover, in the brief hour when I observed people interact with my bot in real time, I discovered several good design choices that I've consciously, unconsciously, or subconsciously made.

## Avoid Feature Creep At All Costs During Development

I originally developed my code for a tutorial, so I kept my code as simple and readable as possible, without complicated features that won't serve my bot's main use case: chatting.

That said, I marked down **TODOs and stretch goals** in my code, hoping to get back to those if necessary. For example:

```python
 # TODO: cache chat history in DB and load
 # TODO: after each user input and bot input,
 # append them to conversation history for the next query
 ...
 # FIXME: better make this try-except block more fine-grained
```

As I observed users interacting with the bot, I'm actually relieved that I didn't implement the **memory cache feature**. Several users were talking with the bot at once, each along their different conversation thread. If I were to keep track of the conversation history, I would have to create a unique log for each user, further complicating database operations.

## Abide by the Principle of Least Privilege

One thing I learned in my Computer Security class is the Principle of Least Privilege (PoLP) – granting an application the minimum amount of access it needs to do its job.

My chatbot only needs two low-level security permissions: **View Channel** for reading users' messages, and **Send Text Messages** for replying to users.

Of course I could have given it more fancy permissions like those shown below in the image, just in case it needs any. But that would have violated PoLP and who knows whether my malfunctioning bot will bring down anything else with it when it fails?

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Screen-Shot-2021-06-03-at-14.21.52-1.png align="left")

*Permission settings for Discord bots*

## Other Observations from Deploying My Bot

Despite its ephemeral lifespan, my bot offered me an opportunity to conduct user research in the real world. This is a server with 1000+ users, not my cozy dev server where my friends and I hang out and take turns to politely exchange lines with the bot.

Here, I observed several interesting user behaviors:

* People tend to ask the bot **open-ended questions** instead of **factual ones**. Because I built my bot based off a video game character, when developing the AI model, I was keen on making sure the model learns the canon information about the character, like name, age, and role in the game. I was relieved when I saw that people are much more curious about the bot character's preference for ice cream flavor than their factual place of birth.
    
* People use a lot of emoticons :), emojis 😃 and GIFs as they text. However, these will most likely be treated as `<UNKNOWN>` tokens in the AI model's tokenizer, which means I should **sanitize** user inputs.
    

I was also very fortunate to receive direct feedback from friendly people on the server. One feature request that I got was to make the bot attach its response to a user's message thread, instead of just dumping its response in the channel.

Buzzing with excitement from people's enthusiasm and armed with insights from user research, I was ready to patch up my bot and send it back as soon as possible.

# What I Needed to Fix

As a good development habit, I kept my code well-organized and modularized, so switching from the production bot back to my development bot requires no more than copy-pasting the dev bot's API key.

Once I was running on my dev server, I sat down to identify the types of problems I needed to tackle.

## Fatal Crashes

The fatal bug that caused me to take down my bot was that I hit an hourly API rate limit. I took the obvious approach of keeping **redundancy** in my system: Keep an alternative API key, and once the primary one runs out, switch over to the alternative, and then switch back at the turn of the hour.

Workaround aside, I noted that this is a short-term solution. If I need to properly scale up my system, I should make an estimate of the number of requests per hour, as I'll discuss at the end of this section.

## New Features for Usability

I decided on several new features that will make my bot more user-friendly. Some highlights are:

* As some server people suggested, I re-programmed the bot so that instead of dumping responses to different user messages into the channel, it directly responds to each user message in the message's thread.
    
* I sanitized user inputs by removing Unicode emojis and Discord-specific `<:some_hilarious_gif>` tags. This will limit `<UNKNOWN>` tokens that my AI model will receive and help it generate better responses.
    
* I implemented a magic command `$ignore [message]` that allow users to send a message to the channel without triggering a bot response. This feature comes from my observation that, whenever the bot says something funny or smart (or both!), users will remark on that by sending a text intended for their friends (and not the bot) to the channel. It'd be annoying to still receive a bot response on a remark intended for a friend. Hence, I hope that this magic command will address this user pain point.
    
* I implemented magic commands for the server moderators to interface with my bot (stopping or rebooting) so that they can keep the bot under control without having to access my Repl.it server. This makes both my job and theirs easier.
    

## Future-proof Logging

In my cozy dev server, there is little complexity, whereas on this 1000+ user server where 40% of users are online at any given moment, complexity explodes.

There are multiple channels besides the chat channel dedicated to my bot, multiple user roles and permission levels, multiple users typing at the same time, and so on.

While I certainly cannot prevent all possible failure scenarios, what I could do is to protect the important part of my code with a try-except block and log out all information that might reveal the cause of a failure. Since real-time system bugs are subtle and difficult to reproduce, logging will save me lots of headaches down the road.

```python
except Exception as e:
            print(e, 'Offending channel', message.channel, 
            'Offending message', message.content, 
            'Offending bot response', bot_response, 
            sep='\n', end='\n\n')
```

## Scalability

Estimating under some system constraints is where basic statistics and heuristics come in. Hugging Face's model Inference API imposes two limits on the scalability of my system:

1. A 10k tokens (characters) per hour rate limit, which is about 300 queries.
    
2. A 30k tokens per month quota for free-tier accounts, which is about 900 queries.
    

> Wonder how I get the numbers? Fun fact: 1) [10k characters is between 1430 and 2500 words](https://capitalizemytitle.com/character-count/10000-characters/). We will take 2100 since Discord messages usually use simple, short words. 2) T[he average length of a text message is 7 words](https://crushhapp.com/texting-tidbits/the-average-text-message-length-is-around-7-words). 2100 / 7 = 300 messages

After processing these numbers, the fact that I hit the per-hour rate limit during the first hour of my bot debut is quite a remarkable feat. People are clearly hyped about my witty chatbot. 🥳

Suppose the hype recedes and life goes on, consider now a hypothetical scenario where 20 users (2% of the 1000+ on the server) regularly chat with my bot, each for 25 lines, in the two hours following dinner. This produces a total of 500 queries in two hours (or 250 per hour), meaning that my bot is safe from the per-hour rate limit of 300.

However, in a month, 500 \* 30 = 15,000 queries, 15 times more than my quota of 900. If my bot is indeed this popular, I would need to switch to a higher-tier subscription plan to ensure that it remains available.

## From Tutorial Code to Production Code

Compared to my tutorial code which strives to be simple, readable, and educative, my production code is longer, more complicated, but also more robust.

# What Makes a Great Side Project

Having emerged from Deployment Hell, like my bot, I'm more resilient than ever and have gained new insights about the principles and challenges in real-world software engineering.

As a final takeaway, I reflect on what makes my Discord AI chatbot this popular. (On June 3rd, a day when it's up 24 hours, it had already busted the monthly 30k quota on both my account and one I borrowed from a friend, totaling 2,000+ messages. 🤓)

I have completed and polished various side projects that received positive feedback, but none of them were as half popular as this one. In retrospect, it's not too hard to see why.

Among projects that I'm most proud of, I built [a chess engine](https://github.com/RuolinZheng08/renpy-chess) and [a rhythm game engine](https://github.com/RuolinZheng08/renpy-rhythm) for [the Ren'Py Visual Novel (VN) game development engine.](https://renpy.org/) Both are rated 5-star on [itch.io](https://itch.io/), a popular platform for publishing indie games.

These projects, however, are open-source engines intended for developers to integrate into their VN games more than standalone playables that can entertain players for hours.

In comparison, my Discord AI chatbot manages to capture each of the following elements that distinguishes a **great** side project from a good one:

* **Audience:** I'm fortunate to have this friendly server with 1000+ users who are open to experimenting with the bot and provide me with helpful feedback.
    
* **Accessibility:** For people to enjoy my chabot, there is nothing special they need to add to their routine - not even opening up a new web app - they just log into Discord as usual, and voilà, the bot is here to chat!
    
* **Interactivity:** Without interactive components, even the most visually-astonishing game will fail to retain players' attention. Nothing to worry about for my chatbot though: Like a loyal friend, it always has something to quip about whenever you need a good chat.
    

If you'd like to learn more about my methodology for working on side projects, check out my previous blog post:

%[https://www.freecodecamp.org/news/how-i-built-my-one-person-open-source-project/] 

Also check out my chatbot tutorial!

%[https://www.freecodecamp.org/news/discord-ai-chatbot/] 

%[https://youtu.be/UBwvFuTC1ZE] 

You can also try this out in JavaScript:

%[https://youtu.be/XR6JFRLxe5A]
