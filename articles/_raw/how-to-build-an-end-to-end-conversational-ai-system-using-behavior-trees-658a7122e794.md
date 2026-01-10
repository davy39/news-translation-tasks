---
title: How to Build an End-to-End Conversational AI System using Behavior Trees
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-12T15:48:13.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-end-to-end-conversational-ai-system-using-behavior-trees-658a7122e794
coverImage: https://cdn-media-1.freecodecamp.org/images/1*gr-Ixi5QqOjf5bFR9ybNag.jpeg
tags:
- name: AI
  slug: ai
- name: bots
  slug: bots
- name: Machine Learning
  slug: machine-learning
- name: Node.js
  slug: nodejs
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Lior Messinger

  At their core, AI projects can be depicted as a simple pipeline of a few building
  blocks. The diagram above explains that pretty nicely: Unstructured content, usually
  in huge amounts of data, comes in from the left, and is fed into ...'
---

By Lior Messinger

At their core, AI projects can be depicted as a simple pipeline of a few building blocks. The diagram above explains that pretty nicely: Unstructured content, usually in huge amounts of data, comes in from the left, and is fed into AI classifiers. These pre-trained machine- or deep- learning models separate the wheat from the chaff and reduce the input to a few numerical or string output values.

For example, megas of pixels and colors in an image are reduced to a label: this is a giraffe. Or a zebra. In audio, millions of wave frequencies produce a sentence through Speech To Text models. And in conversational AI, that sentence can be reduced further to a few strings representing the intent of the speaker and the entities in the sentences.

Once the input has been _recognized,_ we need to do things, and generate some meaningful output. For example, a car recognized too close should turn the wheel in an autonomous car. A request to book a flight should produce some RESTFul database queries and POST calls, and issue a confirmation, or a denial, to the user.

This last part, shown in the diagram as rule-based logic, is an inseparable part of any AI system, and there’s no change in sight to that. It has usually been done by coding, thousands and thousands of lines of code — if it’s a serious system — or a couple of scripts if it’s a toy chatbot.

### Behavior Trees

A [Behavior Tree](https://en.wikipedia.org/wiki/Behavior_tree_(artificial_intelligence,_robotics_and_control)) is a programming paradigm that emerged in video games to create human-like behaviors in non-player characters. They form an excellent visual language with which a software architect, a junior developer and even a non-coder, technical designer can all create complex scripts. In fact, since Behavior trees (BTs) allow logic operations like AND and OR, loops and conditions, any program that can be created by code, can be created with BTs.

[Servo](https://github.com/servo-ai/servo-platform) is an open-source AI conversational framework built on top of a JavaScript behavior tree framework called [Behavior3](https://github.com/behavior3/). It’s designed to do the needed orchestration of inputs and outputs for conversational AI systems. It’s what is called “low-code” framework: you only need to code a little, and most of the tasks can be done in the visual editor.

It’s not your usual newbie's toy: it was designed to be extended using real-life, debuggable JS source files and classes, and abide by any team project-management methodologies. Moreover, it’s suitable for teams that grow in size, allowing the introduction and reuse of new modules through abstracted and decoupled sub-processes.

I’m the main developer of Servo. After 30-something years of coding, feeling the pain in long-delayed projects and watching legacy systems break under their own weight, I wanted to achieve maximum flexibility with minimum coding. Here I’m going to explain the magic that can be done when one combines Behavior Trees with NLU/NLP engines, using Servo and [Wit.ai](https://www.wit.ai/).

Any developer can benefit from this tutorial, but it’s best if you are a developer with experience in building chat- or voice-bots and have knowledge working with NLU/NLP engines like LUIS, Wit.AI, Lex (the Alexa engine), or Dialogflow. If you do not, it’s ok, but I’ll be covering some subjects a bit briefly.

If you want to learn about NLU and NLP engines, there are excellent resources all over the Internet — just search for ‘Wit tutorial’. If you want to learn how to build a heavyweight assistant, then just continue reading.

### Getting Started with Servo

I won’t get into details of installing Servo here, but just say that getting started with Servo is really easy. You can read about it [here](https://medium.com/datadriveninvestor/building-context-aware-stateful-bots-using-servo-a2dc3f557469). In essence, you clone the [Github re](https://github.com/servo-ai/servo-platform)[po](https://github.com/servo-ai/servo-platform), npm-install it according to the readme, and run it locally. Then, every New Project would start you off with a small ready-made bot to get things going:

![Image](https://cdn-media-1.freecodecamp.org/images/6sE9DDHxTVQymZl9jk9I6SlhRyKBkgo6LQLt)
_Every New Project has a starting tree_

You can notice here the green hexagons named ‘chit-chat’, ‘cancel’ and others. By the end of this article, you’ll have a clear idea of what they are and how they work. But first, let’s tackle the first challenges.

### Building An NLU Model

Let’s talk about building a banking assistant, and specifically, one that works for the money transfer department. Had it been a web application, we would have a form with few fields, among which the amount and the transferee’s (also called beneficiary) account are the most important. Let’s use these here for this tutorial. Actually, when using NLU engines, we can still think of it as forms, with the fields now called _entities_ (also _slots,_ in Alexa lingo). The NLU engines also produce an intent, which can be viewed as the name of the form that will guide the assistant to the area of that functionality of the user’s intent.

We should train the NLU engine with a few sentences, such as:

* _“I’d like to send some money”_
* _“I’d like to send $100 “_
* _“Please transfer $490 to account #01–10099988”_

And for these, we need to tell the engine to output the following:

* a _TransferIntent_ intent for such sentences
* A _wit/number_ for the amount
* An _accountNumberEntity_ for the beneficiary account

Let’s do that on Wit.ai. Again, I won’t get into a Wit tutorial — there are plenty of guides. Servo comes with a general Wit model which you can take from Servo’s Github [here](https://github.com/servo-ai/servo-platform/tree/master/server/convocode/nlu-models/wit.ai). Then, open your own Wit app and import it.

I created a [_free-text_](https://wit.ai/docs/recipes#which-entity-should-i-use) entity for the account numbers (as account number might include other symbols), and a _wit/number_ entity for the amount. I found [composite entities](https://medium.com/wit-ai/introducing-composite-entities-ba2639a26e0) work pretty well, too, although they need some training. For simplicity, for account numbers, I trained the model to be a # followed by 8 digits.

In general, it’s always better to experiment with different entity models. In our case, we might get two numbers in the same sentence (account number and amount) and we need a way to tell them apart, so it’s best if it’s two different entity names. But you can try other types: AI is still a very empirical science…

We then trained it with a few sentences and let Wit build the bank-transfer model. For convenience, I added it [here](https://github.com/servo-ai/servo-platform/tree/master/server/convocode/nlu-models/wit.ai), and also set the whole banking bot tutorial bot to come along with the pre-loaded examples.

![Image](https://cdn-media-1.freecodecamp.org/images/caZ8ij2dktQha7o2gUHDXBWU7HFeh1LtStdS)
_Training Wit with sample bank transfer sentences_

Last, we need to connect the NLU to the assistant. Go to _Settings_ in Wit, and copy the **_access token_**. We need to paste it in our tree root’s properties. We do this by opening Servo’s editor, selecting the root, opening its properties, and pasting it under **_nlu_**. As you can see, Servo supports multi-language assistants and different NLU engines:

![Image](https://cdn-media-1.freecodecamp.org/images/LwtOTiDXrX4g1TmVNh428PR7A1dcm-errJBE)

### Start The Bank Assistant

Now, we can turn to Servo. We should construct a small tree with a question for each entity and intent.

As a reminder, the basic rules of Servo behavior-trees is as follows

1. The main loop of the tree is executing the root continuously
2. Each node executes its children
3. An AskAndMap node (the “Age” node in the diagram above) outputs a question to the user and waits for an answer
4. Once an answer comes in, the flow is routed to the appropriate child according to the intent and entities that the NLU engine gave it

Let’s first change the main, topmost question from **_“Age?”_** into **_“What would you like to do?”_**. Also, let’s delete the first (that is, left-most) child and its nodes, as we are not going to use them anymore:

![Image](https://cdn-media-1.freecodecamp.org/images/6uwN7pG2TCHq8kU6oIm6-flNzeI91jYxNEEc)
_Type in the initial assistant question_

Why are we seeing the red dashes around the node? Hover over it and you’ll see the error:

_Count of contexts number should be equal to the number of children_

We will fix that in a minute.

Now let’s build the transfer flow. We’ll assume that once the user says “I’d like to wire money”, we want to descend into the first, leftmost child. For that, we’ll select the “How can I help you” node and go into its properties. There, change the first context to have an **intentId** of _“TransferIntent”_:

![Image](https://cdn-media-1.freecodecamp.org/images/uTc0c33ugCcriSii5HG2tdvEapPuWmHfGVQx)

This will cause any sentence that the Wit determines to have a TransferIntent, to be routed there.

### Mapping an entity

Now, once the NLU has recognized our intent to transfer money, we should get all the different “fields”, or entities. Let’s add a node for the **_amount_**:

![Image](https://cdn-media-1.freecodecamp.org/images/l2FnqEyC9qTdllUVE-kAN34RzoNbewEQqf6m)

We added an AskAndMap node, and set its prompt to a question about the amount. We also changed its title — it’s always a good practice. Last, don’t forget to save your work using the Save button or Ctrl-S.

You can also notice the red warning disappeared from the _How can I help you_ node.

Last, let’s add a **_number_** _entity_ to one of the child contexts of the Amount node, and map the value into a field called **_amount_**_._

```
“contexts”: [
 {
   “entities”: [
    {
      “contextFieldName”: “amount”,
      “entityName”: “number”,
      “expectedValue”: “”,
      “entityIndex”: 0
    } 
   ]
 }
```

All this seems very simple, and it is: if a user says something like “I need to send some money”, they will be asked, “What is the amount?”. Once they enter the amount, the **_number_** will be extracted by the NLU and mapped to the **_context.amount_** in Servo. Then, we can use it later in the game. Visually, the flow started from the root:

![Image](https://cdn-media-1.freecodecamp.org/images/HBQ2me6T-igEkyhMaqKYPPWZstYk6yuS7ecX)

And the assistant would ask:

**_“How can I help you?”_**

If the user answered:

**_“I’d like to transfer some money”_**

the NLU engine would output a **_TransferIntent_** and the flow would continue downstream to the context it identified — the leftmost child — and ask the next question, about the amount:

![Image](https://cdn-media-1.freecodecamp.org/images/X5dhFMpmKZMCnRvocGYljF-OKkPGOs0TFUcO)

But what if the user doesn’t enter an amount?

### Building Helpers

AskAndMap nodes support another type of a context child, called a **_Helper_**. This context is selected when the user answered something that couldn’t be mapped to _any other context_. Let’s add one into our What’s the amount AskAndMap:

```
"contexts":[  
   {  
      "entities":[  
         {  
            "contextFieldName":"amount",
            "entityName":"number",
            "expectedValue":"",
            "entityIndex":0
         }
      ]
   },
   {  
      "helper":true
   }
]
```

Let’s now add a right-most child with a message help. Something like:

![Image](https://cdn-media-1.freecodecamp.org/images/kLl4cXh8KcX2cmKncUd8n1IC83VfUOxmcIEK)

Of course, there can be only one _helper_ context child for the AskAndMap.

One could imagine an example of the flow:

User: **_“I’d like to transfer some money”_**

Assistant: “**_What is the amount?_**”

User: “**_You think I’d know. But I’m not sure_**”

Assistant: “**_Please provide the amount to transfer_**”

That looks simple: obviously, the assistant didn’t understand the “**_You think I’d know. But I’m not sure”_** and went on with the helper message “**_Please provide the amount to transfer_**”.

But in fact, if you’ll run the bot, you will get a surprising sentence after that last line:

User: “**_You think I’d know. But I’m not sure_**”

Assistant: “**_Please provide the amount to transfer_**”

Assistant: **_“How can I help you?”_**

What happened here? Where did the **_“How can I help you?”_** come from?

Here’s the flow. The helper node said its line and returned SUCCESS to its parent, the AskAndMap. This, in turn, returned SUCCESS too, and so on, until the root was reached. At which point, the whole tree was restarted, and we get the initial **_How can I help you?”_** question.

So, to avoid that, we need to put a loop before the AskAndMap, so that it won’t return until it _really_ succeeded. That is done with something called a _decorator._

### Adding a repeat decorator

Behavior Trees implement loops using _decorators_, which are nodes that have one parent and one child. Depicted as a rhombus ⧫, we will use here the RepeatUntillSuccess decorator to loop the AskAndMap until it is successfully completed. Receiving a help message would not complete it, so we need to return a FAILURE after the help message. We do that by sequencing a Failer node right after the message. All in all, that’s the decoration we add to the AskAndMap construct:

![Image](https://cdn-media-1.freecodecamp.org/images/X-2TTcbuxGni0WWV6eiiWV9lACdaIcxol55H)

Now it’s the time to add the next node that would map the beneficiary account number. Again, pretty straight-forward: as before, we add an an AskAndMap with the question for the account number and a map from accountNumberEntity to an accountNumber member on the context. We set it as a child of a RepeatUntilSuccess decorator, and a helper child that explains what’s needed for this entity.

Then, we should add the actual business logic to do the transfer. This would probably mean several API calls with the entities collected. We would simulate this with a message: **_we are going to transfer $X to account #Y_**. For that, you need to drag in a GeneralMessage as the first child of the accountNumberEntity, and make its properties as follows:

```
“debug-log”:””,
 “runningTimeoutSec”:600,
 “maxRetriesNumber”:5,
 “replayActionOnReturnFromContextSwitch”:true,
 “view”:false,
 “prompt”:[ 
 “About to transfer <%=context.amount%> to account <%=context.accountNumber%>”
],
…
```

This is how the tree looks like now:

![Image](https://cdn-media-1.freecodecamp.org/images/04qfwmwrgiugey7IA8Xci0zOOLkIe3JOCyfU)

The tree comes with Servo. It’s files are under _server/convocode/anonymous/drafts/bank-bot._

### Running and testing

Let’s test the bot and see what happens with various inputs. Click on the Debugger tab, then the play button ▶️. On the right hand the simulator will pop:

![Image](https://cdn-media-1.freecodecamp.org/images/zPDBlRIMUzxFbWKRMLyQGI45p-sr1OQe3V3W)

You can enter a sentence like:

**_I’d like to send money._**

That would be answered, as expected, with

“**_What is the amount?_**”

And you can put in the amount, and continue.

But what if we say

**_I’d like to send $14141_**??

Test it, and you’ll see how the assistant nicely jumps over the amount question straight to the account number:

“**_What is the account number?_**”

Now, let’s make its life even harder:

**_I’d like to send money to account #87654321_**

Nicely enough, it asks only for the amount. Say you enter $3400, it would then skip the account number (since it knows it already) into the final confirmation sentence:

**_About to transfer 3400 to account #87654321._**

How does it know to do all that magic?

### The Context Flow

Servo comes equipped with a powerful context-recognition set of algorithms that helps it do all that. What happened here shows a bit of it. Let’s take the last example. After the assistant asked:

**_“How can I help you?”_**

And the user answered:

**_I’d like to send money to account #87654321_**

The NLU engine output a **_TransferIntent_** and the flow continued downstream to the next question, about the amount:

![Image](https://cdn-media-1.freecodecamp.org/images/TzwMBZx2JMHoxXQDzU9-nGaX6jWb7YD27IZm)

But the NLU also returned an **accountNumberEntity!** So before descending, this entity is saved on the _‘How can I help you’_ context. And, every AskAndMap defines its own context.

That’s actually an important remark, so I’ll repeat it: **_every AskAndMap defines its own context._**

At any point in the flow, when an entity is mentioned, Servo searches back (read: upwards) in the conversation to find it. If it hasn’t, it would ask for it.

So after the amount is entered, once we continue to the account number node, Servo finds that the **_accountNumberEntity_** was already mentioned, and uses it.

By the way, a process of similar characteristics happens also when we get to the last confirming GeneralMessage node. Its prompt reads:

**About to transfer <%=context.amount%> to account <%=context.accountNumber%>**

To resolve that, Servo searches up the context tree to find the needed entities, or context members.

Does this remind you of something? Folks familiar with JavaScript prototypical inheritance would see that it basically uses the same design. In Servo, we implemented that since we need more control over the variables. But it’s always interesting to see how object-oriented concepts are actually applied to real life, natural conversations.

But what if the user asks something much more unrelated, like:

**_“How much money do I have in my account?”_**

Or more so

**_“Who are you, for heaven’s sake??”_**

To which to bot responds:

**_“I’m an artificial intelligence assistant built by Servo Labs.”_**

Whaaaaaaaaaat?? Where did this come from?

### Context and sub-trees

Almost all of the structural designs architects use to build manageable large systems can be divided into one of two categories:

* Reuse
* Modularize

If Servo is to stand as the infrastructure of large AI systems, it must provide some mechanism for allowing developers to achieve these goals. And that’s where sub-trees come into play.

We mentioned before the green hexagons:

![Image](https://cdn-media-1.freecodecamp.org/images/vOpQmHfU9hfBvwCk5vwPg-ZNakYT6ssQp3vT)

This is a sub-tree. **Double-click it**, and you’ll enter a new tree, with that name. To create a new sub-tree, hover over the **Trees** on the left pane and select **New:**

![Image](https://cdn-media-1.freecodecamp.org/images/KeD7CXJx-i8DJr7Jne94zbddR-AMPJvRc4yG)

A tree with a unique GUID name would appear. Change its name to something meaningful, and build it using any node from the left pane. Once built, you can drag, drop and connect it at any point in any other tree (including itself, by the way, but be very careful about that). Since sub-trees can have many leaf nodes, you can connect them only as leaves, too.

What happened when the user asked the assistant “Who are you”?

First, the NLU, already trained for such questions, returned a **_WhoAreYouIntent_**. Then context search was activated. If the conversation was somewhere down in the middle of a transfer conversation, the search went upwards, trying to find a context with WhoAreYouIntent. This context is found: it sits on the 4th context, in the _How can I help you_ node. The flow then was redirected there, meaning, that route was made the active route. The flow here continued downstream into the chit-chat subtree, answered the question, returned up with a SUCCESS and the routing was returned to its previous context, the transfer one.

Here we learned something actually very important. **_The conversation flows down, but context is searched up._** Never forget that:

![Image](https://cdn-media-1.freecodecamp.org/images/ZPNg-j6-113QHHDPjO6D9Rfn2lHDmaRl2Z2U)
_**The conversation flows down, but context is searched up**_

### Connecting to a messenger client

Until now, we have used the internal simulator and debugger as our messaging client. Let’s connect our small assistant to a real Facebook messenger. There is one big important change on the root properties of our tree, and that is to change the channel name from the default channel _“chatsim”_ to _“facebook”_:

"channels":"facebook"

On the Facebook side, these are the main high-level steps that one needs to take:

1. Open a Facebook page under your Facebook account
2. Create a new Facebook app in the [Facebook developer center](https://developers.facebook.com/)
3. Add a messenger functionality to your app
4. Subscribe the app to listen to events in the page
5. Set the assistant callback address as the webhook to post to. Servo always publish its bot with the format of

<URI>/entry/<channel id>/<assistant name>

So for a bank-bot assistant, running on [www.mydomain.com,](http://www.mydomain.com%2C/) the address would be:

[https://<www.mydomain.com>/entry/fb/bank-bot](https://www.mydomain.com/entry/fb/bank-bot)

You should set it in the page subscription section of the Facebook app, at the developer’s portal. You need to select at least _messages_, _messaging_postbacks_, and to match the _verify token_ with the validation token you set in the bot’s root properties:

![Image](https://cdn-media-1.freecodecamp.org/images/TAxJMvN8uOHgzYe6d8u0UNj2ar9NeYh4CbEn)

By the way, [https://serveo.net](https://serveo.net/) is a great tunneling system (another alternative is ngrok), if you are developing your assistants, like me, on localhost.

On the assistant root properties, set the same verify token and re-publish it:

```
"facebook": {
    "validationToken": "mytoken123",
    "accessToken": "<token here>"
  },
```

The access token should be set too, taken from Facebook’s messenger area:

![Image](https://cdn-media-1.freecodecamp.org/images/YVCodrLcDGHFb7gZC5xMJjLoPvHVwZk1Xj1z)

Last, select a page to subscribe your webhook to the page events:

![Image](https://cdn-media-1.freecodecamp.org/images/EWZohg-wYOzch3vfNe8Qjc0LWhUBAOsornRk)

and… once you connect all these ends, you should have, at last, a full, orchestrated, end-to-end conversational AI system!

### Connecting Backends

Real life connections vary, but luckily, most of them these days are done by using RESTFul API. For these, check out the [documentation](https://servo-ai.github.io/servo-platform/) on **_RetrieveJSONAction_** and _PostAction_. Once data is retrieved, or a response is received, it is set into a [memory field (context/global/volatile)](https://github.com/servo-ai/servo-platform/wiki/Building-context-aware,-stateful-chatbots-using-Servo#hierarchical-memory). You probably would want to query it. This is done using **_ArrayQueryAction,_** which implements an in-memory Mongo-like query language_._ For direct MongoDB queries, use the **_MongoQuery_** action.

### In Summary

Servo is an open-source IDE and framework that uses a context-recognition search to place the user on the right conversation and output the right questions. We learned how to construct a simple conversation, and how to wrap such conversations in sub-trees for decoupling and re-use. Servo has many other features that are worth exploring, among which you could find

* Connectors to Facebook, Alexa, Twilio and Angular
* Connectors to MongoDB, Couchbase and LokiJS databases
* Harness for automated conversation testing
* A Conversation debugger
* More actions, conditions and decorators
* Flow control mechanisms
* Field assignment and compare
* Context manipulation
* Validation
* In-memory mongo-like queries
* And any customized action you come up with

Feel free to check it out and ask questions on the Github forum or at my @lmessinger Github name. Enjoy!

