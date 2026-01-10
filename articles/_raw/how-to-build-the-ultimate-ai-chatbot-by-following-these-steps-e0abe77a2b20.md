---
title: How to build the ultimate AI chatbot by following these steps
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-26T12:58:35.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-the-ultimate-ai-chatbot-by-following-these-steps-e0abe77a2b20
coverImage: https://cdn-media-1.freecodecamp.org/images/1*mDFiewb7C0vXSWvbZ6VodQ.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: bots
  slug: bots
- name: '#chatbots'
  slug: chatbots
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Paul Pinard

  A quick guide that helps you avoid common pitfalls


  Building a bot is a rewarding experience: creating your own artificial intelligence
  is amazing!

  However, it can be a challenge, and there are mistakes to avoid. In this piece,
  we’re g...'
---

By Paul Pinard

#### A quick guide that helps you avoid common pitfalls

![Image](https://cdn-media-1.freecodecamp.org/images/Na8oklNT0d3X7Nix1l0-mfV3mGJUv6BjNiKx)

Building a bot is a rewarding experience: creating your own artificial intelligence is amazing!

However, it can be a challenge, and there are mistakes to avoid. In this piece, we’re going to walk you through the most common or damaging mistakes new bot builders make in each phase of bot building: conception, training, building, connection, user experience and maintenance. Let’s roll!

### **Conception**

Building a bot doesn’t start at the first line of code. It starts much earlier, during the conception.

During that first step, it’s important to define the use case of your chatbot. What is the problem you want it to solve? What are your business needs?

We often see people saying “_I want a bot that does this_”, but when we dig deeper, we realize a different bot would actually fix the issue much more efficiently. If you want to build a chatbot that manages customers’ questions on return policies, but later realize that these queries are less than 2% of your global volume, you might want to switch to another topic. So, start from the business problem and build from there.

Now that you’ve established the real-life business need, how should the bot conversation flow go to solve it? What we usually do is take out a drawing board and draw all the conversation flows, from start to finish. Modeling all possibilities allows you to make sure every topic is covered and gives the developer a good overview of what needs to be done. It is also the first step of creating your user experience, which we’ll talk about later. For now, simply keep in mind that each conversation should be about 3 or 4 exchanges, no more.

During this step, remember your audience: who are the end-users that will be talking to your bot? You have to make something that works for them.

Do not forget to include small talk in your conception. All chatbots are expected to understand and reply to a number of topics unrelated to their mission: jokes, weather questions, “how are you doing”, and even remarks like “will you marry me” or other off-topic stuff. Be sure to plan for those if you want the user to be satisfied with the experience. But no worries, we provide pre-trained small-talk Skills on [SAP Conversational AI](https://cai.tools.sap/?utm_source=medium&utm_medium=article&utm_campaign=UA2019).

**What not to do when building a bot:**

> **1. Disregard it as a non-important step**

> **2. Start from what you want and not from what you need**

> **3. Incorrectly understand who the final users of the bot will be and design an experience they won’t appreciate**

> **4. Not include small talk and other commonly asked questions**

### **Training**

Training the bot is the most important factor in determining its performance. Bad training will inevitably lead to a poor performing chatbot and frustrated users.

Based on the flow you’ve created during conception, training consists of creating intents and filling them with expressions. If you’re not comfortable with the concept of intents and expressions, [this article](https://cai.tools.sap/docs/concepts/intent) should help you. But here are some things that make for good training.

The number of expressions in each intent is crucial. Five doesn’t cut it, you should go for 50+. SAP Conversational AI works very well on small datasets, but we still need a bit of information. These sentences should be varied and should come from end users. Never train your bot only with the development and project team: they know the technical slang too well to accurately represent the people that will actually use the bot.

![Image](https://cdn-media-1.freecodecamp.org/images/-Yycb-a6fPKt0xLNWMfceZVVoZYgLeJ33k2a)

Tagging entities has a few rules as well. Entities are keywords that you need to detect in a sentence to extract information (the key point here being “to extract information”). You don’t need to tag every noun, adjective or word per sentence just because you can! The point of entities is to extract relevant information that you can use in your code. Only tag those.

However, avoid having sentences that are only made of one word that is an entity (e.g. “Paris” as a complete sentence). This entity can be detected by any intent, which can lead to detection issues.

![Image](https://cdn-media-1.freecodecamp.org/images/MZHlf-J9SBKS9FC3zq8JzZGTgbxvBgpdBSRw)

A common best practice for big bots is to use intents and entities hand in hand. It is better to create a global intent and use entities to specify the user request, than to create very specific intents that the classifier will confuse as they overlap.

![Image](https://cdn-media-1.freecodecamp.org/images/EQsnPzNr1wkFVldSUSEuYeXKpbaAXO5840Ek)
_Here, the global intent is troubleshooting, but entities detect which product isn’t functioning._

**What not to do when building a bot:**

> **5. Have less than 50 expressions per intent**

> **6. Train your bot by people who are not the end-user**

> **7. Tag every word in a sentence as an entity**

> **8. Tag words as entities when you don’t use the extracted information**

> **9. Have expressions that are only entities (i.e “Paris”)**

> **10. Create very specific intents instead of using entities to understand the topic**

### **Building**

Building a bot is often assumed to involve just building the conversation flow. It is the fun part! It’s when everything comes to life. However, it can be a scary process.

The first thing to understand is that it’s ok to use multiple skills to complete one task. One skill doesn’t have to equal one full process. It can be a good solution to create one “mega-skill” whose job is to dispatch the user input to the correct skill.

![Image](https://cdn-media-1.freecodecamp.org/images/AziHdCyg92iqRr0HQ8RtCK0DrlIpJs-Nd9vB)
_In our troubleshooting (ts) example, a mega-skill redirects to the different skills that manage the specific procedures_

That is also a solution if you have skills with triggers that overlap each other. And if something doesn’t work, be sure to use the logs in the debug console to understand where the problem is coming from.

![Image](https://cdn-media-1.freecodecamp.org/images/ZjjNiSVhAlfy9E7Oq30-EFZsQdQyXhFLNJ07)

**What not to do when building a bot:**

> **11. Insist on the “one skill = one task” philosophy**

> **12. Not leverage the debugging tools of the platform**

### **Connecting and User Experience**

When connecting your bot, you have to decide where it is going to be available to your users, and therefore work on a user experience. There are a few things to know to provide an enjoyable UX, the first one being: your bot has to look pretty. An attractive bot with plenty of buttons, graphic elements, HD pictures, colors, and a good personality makes all the difference.

But how do you get that?

First, think of your audience when you choose your channel. If you’re targeting the 50 to 65 age demographics, you’re probably not going to put your bot on Kik! Don’t try to attract your audience to a channel they don’t use, even if it’s better. Instead, integrate the bot where your users already are.

Then, keep in mind a chatbot is a conversational interface. Conversations are interactive exchanges; therefore, your bot should never reply with long-winded blocks of texts (more than 60 characters is getting long).

Separate replies into different messages, use images, buttons, lists and other UX components based on the channel you use to make it lively. It’s also important to create a rewarding conversation: your bot isn’t an FBI agent. Nobody wants to be asked 20 questions before getting an answer. Instead, create your flow and UX to provide an answer every 3 or 4 exchanges to keep the user engaged.

Since we provide a powerful natural language processing API with our bot building tool, our users tend to want to do everything through language. While that’s admirable, we still advise to diversify: offer cards, buttons and other graphic elements for interactivity and ease of use, but still make sure the entire flow can be done using natural language. That’s when users know your bot is the real deal.

![Image](https://cdn-media-1.freecodecamp.org/images/rl5eyf2CDstgMMB-NdSjzDt5tjYWSRNiDUlO)

Giving a personality to your chatbot is essential, however you have to find the right balance. We always advise to let your users know they’re talking to a bot. It’s simply expectation management!

A human talking to another human is going to expect the highest level of interaction, whereas a human talking to a bot is going to know that they can’t ask about anything and everything. However, don’t make it too robotic: give it a name, an image, and use smileys and tone of voice to make it memorable.

**What not to do when building a bot:**

> **13. Mis-identify the channel your audience is using**

> **14. Create conversations where the user has to answer 4+ questions to get a first answer**

> **15. Send blocks of texts as replies (more than 60 characters is too much)**

> **16. Discard all UX elements (buttons, cards, lists, etc) just to focus on text**

> **17. Pass your bot as a human person**

> **18. Not giving your bot a personality that attracts your audience**

### **Maintenance**

Once your bot is in production, your job is not done! Maintaining your bot is an essential part of its long-lasting success. That mainly consists of fine-tuning your training and monitoring what your users are saying to adapt your flow or create new use cases.

When training, proceed with caution. While it is important to add new user sentences via the log feed, you do not want to unbalance the training you’ve created that already works. Don’t swamp your intents by adding all the new expressions, only add what’s necessary. Keep in mind that all intents have to be trained the same amount! If one intent has 100 expressions and the other has 10, that’s no good. Therefore, check regularly when assigning new expressions. Our training analytics are your best friend when it comes to improving your training data!

Finally, your log feed is the place where you can see what users are talking about. Do you see a topic that your users are raising frequently that your bot doesn’t yet manage? Why not integrate it into your flow? That’s the best way to show your community that the bot they’re using is always striving to provide a great experience.

**What not to do when building a bot:**

> **19. Thinking that once the bot is in production, your job is done**

> **20. Overflow intents with new user expression and mess up your existing training**

> **21. Create inequalities in your intent size**

> **22. Not pay attention to how people are using your bot**

With all this in mind, you are fully on-board to build a first kick-ass bot! If you’re ready to go further, this [step-by-step tutorial](https://medium.freecodecamp.org/how-to-build-your-first-chatbot-with-the-sap-conversational-ai-9a1a2bd44e3c) can guide you through the actual process to build an awesome joke-telling chatbot!

Happy building!

_Originally published on [SAP Conversational AI Blog](https://cai.tools.sap/blog/building-a-bot-22-rules/)._

