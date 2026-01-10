---
title: How to improve the conversation flow of your Alexa skill
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-26T14:57:05.000Z'
originalURL: https://freecodecamp.org/news/how-to-improve-the-conversation-flow-of-your-alexa-skill-1b6c6556f9a3
coverImage: https://cdn-media-1.freecodecamp.org/images/0*uQl2sV1anCMlYWFd
tags:
- name: Alexa Skills
  slug: alexa-skills
- name: development
  slug: development
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Garrett Vargas

  Natural conversations are fluid. That’s one of the joys of face to face human conversation,
  you never know how the dialog will evolve. But sometimes, there is a natural flow
  to the conversation. Ask someone where they want to eat, a...'
---

By Garrett Vargas

Natural conversations are fluid. That’s one of the joys of face to face human conversation, you never know how the dialog will evolve. But sometimes, there is a natural flow to the conversation. Ask someone where they want to eat, and you expect to hear a restaurant or type of food, not a response about a favorite movie.

One of the frustrations people have with voice assistants is that they sometimes do a poor job understanding what they’re saying. Amazon has a tool to help third party developers provide better recognition. **Dialog Management** lets you prompt for values to fulfill a request with increased accuracy.

For example, if you are creating a skill that searches for a car rental, Alexa can prompt the customer for a city and dates of travel after they say “find a car.” Alexa’s built-in functionality improves the accuracy of speech recognition in this case as it listens for specific values.

The problem is that the customer has to speak the appropriate words to trigger a Dialog-controlled intent. Amazon recently announced [intent chaining](https://developer.amazon.com/blogs/alexa/post/9ffdbddb-948a-4eff-8408-7e210282ed38/intent-chaining-for-alexa-skill) as a solution to this problem.

In this blog I’m going to show you how I use this functionality with a skill that lets the user perform a car search. First, let’s review how Dialog Management works within Alexa. Let’s look at a CarSearchIntent that gathers the input needed to kick off a car search.

![Image](https://cdn-media-1.freecodecamp.org/images/fLRkwma7n9QfRGu2wv6bqzUZkahywAXANe-3)
_CarSearchIntent with slots for location and travel dates_

As you can see, we have several variations on how a customer can find a car, including slots for Location, PickUpDate, and DropOffDate. We want to make sure the customer provides all three of these slots before we start processing the request. We use Dialog Management to let Alexa handle prompting the customer to provide these.

![Image](https://cdn-media-1.freecodecamp.org/images/FCtaQRUn465AgEwF8Tyl0XcYk8UIVnOSS-O7)
_Location as required slot with prompt_

When in Dialog mode, Alexa has a higher chance of accuracy because it is trying to fill slots for this intent. But to get into this mode, the customer has to trigger this intent by saying “Find a car” or a similar phrase. Ideally, we’d drop the customer into this mode as soon as they launched the skill.

Enter Intent Chaining! We can add a **Dialog Delegate** directive to our response that puts the customer into the dialog flow of CarSearchIntent.

```
canHandle(handlerInput) {  const request = handlerInput.requestEnvelope.request;  return handlerInput.requestEnvelope.session.new ||    (request.type === 'LaunchRequest');},handle: function(handlerInput) {  return handlerInput.responseBuilder    .addDelegateDirective({      name: 'CarSearchIntent',      confirmationStatus: 'NONE',      slots: {}    })    .speak("Welcome to car search.")    .getResponse();}
```

The dialog directive allows us to pre-fill some of the slots (for example, we could default the location to the last used search location). What’s interesting to note is that we only specify “Welcome to car search” as the response for this handler. We don’t specify a reprompt. Alexa appends the dialog prompt for CarSearchIntent to our response and uses that as the reprompt. So in this case what the user will hear is “Welcome to car search. Where would you like to pick up the car?” If they don’t answer, they will hear a reprompt of “Where would you like to pick up the car?”

You also have the ability to direct the customer to fill out a specific slot when dropping them into a dialog. Let’s say that we want to guide the user to first specify the pick up date for their car. We can do that using an **Elicit Slot** directive, as shown in the following code.

```
canHandle(handlerInput) {  const request = handlerInput.requestEnvelope.request;  return handlerInput.requestEnvelope.session.new ||    (request.type === 'LaunchRequest');},handle: function(handlerInput) {  return handlerInput.responseBuilder    .addElicitSlotDirective('PickUpDate', {      name: 'CarSearchIntent',      confirmationStatus: 'NONE',      slots: {}    })    .speak("Welcome to car search. When would you like to pick up your car?")    .reprompt("When would you like to pick up your car?")    .getResponse();}
```

In this case, we need to spell out the entire speech and reprompt that the customer will hear. We need to do this since we are controlling how we drop the customer into the dialog management flow.

Chaining intents lets you manage the conversation flow in a more natural way. Use it to make your skill more usable for your customers!

