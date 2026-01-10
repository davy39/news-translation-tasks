---
title: How to implement an Alexa Skill with Spring Boot
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-03T13:06:28.000Z'
originalURL: https://freecodecamp.org/news/implementing-an-alexa-skill-with-spring-boot-also-why-would-you-do-such-a-thing-9992c0797646
coverImage: https://cdn-media-1.freecodecamp.org/images/1*agCi2IBtbBlRZsDfy6KRxA.jpeg
tags:
- name: amazon echo
  slug: amazon-echo
- name: Java
  slug: java
- name: software development
  slug: software-development
- name: spring-boot
  slug: spring-boot
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Rafael Fiol

  And why you would do such a thing


  There are two ways to implement custom skills for Alexa.

  The first is the most common and is the Amazon-recommended way. Use AWS Lambda,
  a server-less computer service. There is no shortage of article...'
---

By Rafael Fiol

#### And why you would do such a thing

![Image](https://cdn-media-1.freecodecamp.org/images/1*agCi2IBtbBlRZsDfy6KRxA.jpeg)

There are two ways to implement custom [skills](https://en.wikipedia.org/wiki/Amazon_Alexa#Alexa_Skills_Kit) for Alexa.

The first is the most common and is the Amazon-recommended way. Use [AWS Lambda](https://aws.amazon.com/lambda/), a server-less computer service. There is no shortage of articles and tutorials on the topic. This is not one of them.

The second way is far less common. This is hosting an endpoint using a HTTPS web service that you manage. It is a bit more difficult to find good examples of this approach. This article will attempt to do just that, and will use [Spring Boot](https://spring.io/projects/spring-boot) as the basis for the implementation.

![Image](https://cdn-media-1.freecodecamp.org/images/1*CBS-TT_JYEOWhYsdyr0OWQ.jpeg)
_Endpoint configuration in the Alexa Skills Developer Console_

But before we jump into the **how**, let’s talk about the **why**:

* Why would you not use AWS Lambda?
* Why ignore an Amazon recommendation?

These questions are important. You’ll find reams of great examples and documentation on building Skills with Lambda, and not so much for the alternative. It’s also important if you buy into the premise — which I do — that the world is going [server-less](https://en.wikipedia.org/wiki/Serverless_computing). This is a [great article](https://read.acloud.guru/six-months-of-serverless-lessons-learned-f6da86a73526) on that topic by James Beswick. Going the HTTPS route will lead you down a lonely path, but sometimes that’s OK.

Here are some reasons why you may want or need to take that lonely path.

* You can write your Alexa web services using any programming language.
* If you have existing RESTful services already deployed and you want to leverage that infrastructure/investment.
* If your [CISO](https://en.wikipedia.org/wiki/Chief_information_security_officer) does not allow off-premise or cloud-based infrastructures.
* If you like lonely paths.

In my case, I decided to explore the non-Lambda path primarily because I already had an existing services tier, which I wanted to leverage. There are [POJOs](https://en.wikipedia.org/wiki/Plain_old_Java_object) and methods I wanted to reuse, without having to expose new endpoints. Of course, I could have created Lambdas that simply fronted those services, and that is a valid pattern. But I didn’t want to add another layer of deployment scripts, testing, and monitoring.

You probably have your own reasons. If I were building a new [greenfield](https://en.wikipedia.org/wiki/Greenfield_project) application, I’d probably head down the Lambda path.

### Prerequisites

You’ll use the [Alexa Developer Console](https://developer.amazon.com/alexa) to register your skill, define the intents and utterances, and test it. I’ve assumed that you’ve already created a developer account, and that you can setup a new custom Skill within the console.

### A Spring Boot Alexa Skill

The rest of this article will show you how easy it is to add an Alexa Skill to your existing Spring Boot applications. To demonstrate this, we’ll create a skill that will lookup fun facts about either a specific year, or a random year. You’ll be able to interact with our skill by saying things such as:

```
Alexa, ask my demo app to tell me trivia about a random year.Alexa, ask my demo app, what happened in the year 1984? 
```

Okay, yes, this is a pretty useless skill. But it will demonstrate all of the important aspects of an Alexa app, including:

* custom intent handling
* using slots, session management
* built-in intent handling

To accomplish this, our example skill will call a free third-party API to lookup the trivia information, using the wonderful [NumbersAPI](http://numbersapi.com/#42). Many thanks to [David](https://twitter.com/divad12) and [Mack](https://github.com/mduan) for creating this fun service.

### Getting started

First things first. Add the [Alexa Skills Kit SDK](https://mvnrepository.com/artifact/com.amazon.alexa/alexa-skills-kit) to your “pom.xml” file. At the time of writing, the latest version of the SDK is 1.8.1.

```
<dependency>    <groupId>com.amazon.alexa</groupId>    <artifactId>alexa-skills-kit</artifactId>    <version>1.8.1</version></dependency>
```

The SDK includes a special servlet, named `SpeechletServlet`, which you will need to load as part of the app bootstrap. This is actually very easy to do.

The servlet is a workhorse. It handles all of the messy [requirements for hosting a skill](https://developer.amazon.com/docs/custom-skills/host-a-custom-skill-as-a-web-service.html), such as verifying that the request was sent by Alexa, validating the signature, and checking the timestamp. Fortunately for us, we don’t have to deal with any of those headaches. We just need to load the servlet. Here’s how we do that:

Simple. You can see above that we’ve created a configuration class that loads our servlet. On line 10, you can see that `SpeechletServlet` is instantiated, and then on line 13 it is registered with Spring.

That’s pretty much all you need to do to load the servlet.

As I noted, the servlet takes care of all the complicated handshake communications with Alexa. And after it does that, the servlet delegates the actual interaction business logic to a **Speechlet**, which you must implement. You can see on line 11 that the Speechlet, which I named `HandlerSpeechlet`, is assigned to the servlet. This Speechlet will be invoked with every Alexa interaction.

A Speechlet is just a POJO that conforms to the SpeechletV2 interface that is defined in the Alexa Skills SDK. Here is what the interface looks like.

It’s your job to implement those four methods.

They’re all important, but most of the work happens in `OnIntent()`, which is invoked when the user says something meaningful. If you’re new to the vocabulary of Alexa programming, you should read [Intents, Utterances, and Slots: The New Vocabulary Needed To Develop For Voice](https://medium.com/screenmedia-lab/utterances-slots-and-skills-the-new-vocabulary-needed-to-develop-for-voice-7428bff4ed79).

### Defining intents

Jump into the [Alexa Developer Console](https://developer.amazon.com/alexa). Set up a new custom skill within the console — that part is very easy. I’ve named my skill “MyDemoApp”, and under the Invocation menu, I set the Skill Invocation Name to “my demo app”.

Recall earlier in this article I said that you can interact with our skill by saying things such as:

```
Alexa, ask my demo app to tell me trivia about a random year.Alexa, ask my demo app, what happened in the year 1984?
```

You can see that each of the above sentences start with the wake word (“Alexa”) and the Skill Invocation Name (“my demo app”).

```
Alexa, ask my demo app ...
```

Everything after the Skill Invocation Name is known as an **utterance**. It’s your job to list utterances in the developer console, and map those to an intent. A single intent normally has many utterances, representing the variations a user might say. For example, all of the following utterances are essentially the same:

```
tell me trivia about a random year.say something about any year.pick a random year.tell me some trivia.say anything about any year.
```

All of these utterances mean the same thing, and therefore can map to a single intent. In my application, I’ve called this the “RandomYearIntent”. Here’s what it looks like in the developer console.

![Image](https://cdn-media-1.freecodecamp.org/images/1*-jAvV7iIAAnBDazM_TGgTA.png)

### Back to writing code

With our first intent defined, it’s now time to jump back into our Spring application and write some code. Let’s edit our “HandlerSpeechlet”. For the moment, let’s skip the `onSessionStarted` and `onLaunch` methods of the Speechlet, and jump right into the `onIntent` method.

Because our application will eventually handle multiple intents, we’ll first need to determine which intent is being invoked.

On line 10, we now have the name of the intent. In our example so far, this should be `RandomYearIntent`. At this point, you might be tempted to write a bunch of `if-else` statements against the intent name, but let’s try something a little smarter.

By making sure that our intents follow a specific naming convention, we can use some Spring magic to load and invoke specialized handlers for each intent. What follows is not something specific to the Alexa Skills SDK. It’s just my own way of handling multiple intents. There are many ways to implement this logic. Here’s mine.

Let’s start by defining an interface which we’ll use for all of our handlers. Let’s create `IntentHandler` as:

Next, for each intent, we’ll create a class that implements this interface. We’ll also be careful to name our classes the same as the intent name, with the word “Handler” appended. For example, for the intent “RandomYearIntent”, we’ll create a class named `RandomYearIntentHandler`_._

Okay, let’s leave this unimplemented for now. We’ll go back to our “HandlerSpeechlet” to add code that will pass control to our new “RandomYearIntentHandler”. The basic strategy is to rely on our naming convention of “IntentName” + “Handler”.

I have removed some details and error handling from the code below so that we can focus on the important bits. At the end of this article, you can find a link to my GitHub repo with the complete code.

Check out lines 12 and 13 below, which construct the class name, then ask Spring to find a registered bean with that name. Then, finally, on line 17, we pass control to that handler.

### RandomYearIntentHandler

We now have the plumbing in place to call our specialized intent handlers. Let’s go back to the implementation of our “RandomYearIntentHandler”. This particular intent is simple. Here’s the complete implementation.

Simple! Did you catch the annotation on line 1? That `@Component` annotation is a cool little trick that will tell Spring to create an instance of this class as a Bean. This is how we’re able to access the handler in our Speechlet, using `beanFactory.getBean(handlerBeanName)`.

On line 11 we create a random number between 1900 and the current year. Then we call the [Numbers API](http://numbersapi.com/#42) to get trivia about that year.

On lines 14 and 15 we create a `Card` and a `Speech`. The `Card` is what is displayed in your Alexa mobile app — or on the screen in the Echo Show. The Speech is what is spoken back to the user.

`AlexaUtils` is a simple class I created. I won’t go into the details here, but you can review it on [GitHub](https://github.com/raf66/AlexSpringBootWeb/blob/master/src/main/java/net/fiol/demo/alexa/utils/AlexaUtils.java).

### That was easy — what about slots?

Slots are basically **variables in utterances**. Look back at the two intents in our application. The second intent, which I’ll name “SpecificYearIntent”, allows the user to say any year. For example:

```
Alexa, ask my demo app, what happened in the year 1984?
```

In the above utterance, the year is highly variable. We do not want to define an utterance for every possible year. Instead, we’ll define this utterance using a slot, as:

```
Alexa, ask my demo app, what happened in the year {Year}?
```

{Year} represents a number. Jumping back into our developer console, we’ll setup a new “SpecificYearIntent” intent with its associated utterances as follows:

![Image](https://cdn-media-1.freecodecamp.org/images/1*CDFfMDV8z_cQQeoSeMaisw.jpeg)
_SpecificYearIntent utterances_

I’ve defined a Slot named “Year”, which is of type “AMAZON.NUMBER”. Now, in my handler, I can fetch the slot value easily by name.

Line 13 is where we resolve the year `Slot`. The rest is all boilerplate Java code, which follows the same pattern as the first intent — call the NumbersAPI service for the year and handle the response.

### Sessions and state

I didn’t get into the `OnSessionStarted` or `OnLaunch` methods of the Speechlet in this article, but I did include an implementation for `OnLaunch` in the [sample project in GitHub](https://github.com/raf66/AlexSpringBootWeb).

You can use the `Session` object to store variables that will be retained across invocations when in conversation mode. Conversation mode occurs when the user invokes your skill but does not speak a recognized utterance. For example:

```
Alex, open my demo app.
```

```
>> Hello.  Here are some things you can say: Tell me something about a random year.  Or, what happened in nineteen eighty-nine?
```

```
What happened in the year 1984?
```

```
>> 1984 is the year that the European Economic Community makes £1.8 million available to help combat the Ethiopian famine on October 25th. 
```

```
>> What else can I tell you? Say "Help" for some suggestions.
```

```
Cancel.
```

```
>> OK.  Goodbye.
```

You’ll notice in my source code that I have a method named `setConversationMode`. It simply sets a variable in the Session, letting me know that we are in conversation mode.

### Summary

Writing Alexa skills with Spring Boot is quite easy, and can be a powerful way to reuse your existing infrastructure. [Download the complete app from GitHub](https://github.com/raf66/AlexSpringBootWeb) for more details.

And if you’re in the South Florida area, you can use my [Cutler Stew Skill](https://www.amazon.com/Rafael-Fiol-Cutler-Stew/dp/B0793FRYJG) (built with Spring Boot) to learn when and where my band Cutler Stew is performing next.

