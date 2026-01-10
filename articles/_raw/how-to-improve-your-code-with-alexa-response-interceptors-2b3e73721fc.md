---
title: How to Improve Your Code With Alexa Response Interceptors
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-27T16:39:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-improve-your-code-with-alexa-response-interceptors-2b3e73721fc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*d0I7athFoo0jgOpGMLPCKg.jpeg
tags:
- name: Alexa
  slug: alexa
- name: Alexa Skills
  slug: alexa-skills
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Garrett Vargas

  I’ve published over a dozen Alexa skills over the last few years. I have run across
  several patterns and best practices in that time.

  One of the more powerful but under-hyped features of the SDK that I’ve made extensive
  use of in my...'
---

By Garrett Vargas

I’ve published over a dozen Alexa skills over the last few years. I have run across several patterns and best practices in that time.

One of the more powerful but under-hyped features of the SDK that I’ve made extensive use of in my code is the Response Interceptor. It is part of the [Alexa Node SDK](https://www.npmjs.com/package/ask-sdk). This SDK simplifies Alexa skill development.

When using it you may find your code getting messy with redundant error handling and clean-up tasks. Response interceptors allow you to insert a hook into the flow of handling Alexa intents. This keeps your code clean by performing last-minute actions in one central location before passing the response back to Alexa. This is extremely useful for **debugging**, **resolving common tasks**, and generally **cleaning up responses** to avoid some common errors encountered when using the Alexa ecosystem.

#### Debugging

To add a response interceptor with the Alexa SDK, you pass a class that implements a **process** function to the addResponseInterceptors function on your SkillBuilder object as shown in the code sample below. We’ll get to the implementation details of this class in a moment.

This snippet also shows setting a request interceptor function which will run _before_ a request is passed to your Alexa handlers. For example, I find it helps debugging to log each incoming request and the outgoing response. You can do this with the request interceptor and response interceptor as demonstrated in this code snippet. The snippet also shows the syntax for the process function returning an empty Promise.

#### Resolving Common Tasks

Many of my skills process AMAZON.RepeatIntent so the user can re-hear the last response. If you have a complex skill, especially one that maintains state engines, you should provide additional detail when the user asks Alexa to repeat herself so the user knows exactly where they are. But in simpler skills, it’s fine to just replay the previous response back to the user. A response interceptor allows you to save each outgoing speech and reprompt cue so that you can re-play them easily:

Another common task is handling attributes. The Alexa SDK has several layers of attributes.

* request attributes (only good during a single request)
* session attributes (good for the length of a session)
* persistent attributes (saved in a store like DynamoDB to be used across sessions).

I find juggling all of these can be overwhelming. I structured my code to only use session attributes, which I save to persistent storage at the end of the session. But there are two problems with this as a blanket approach — there are attributes that you may not want to save and there are times you want a value to pass between handlers but not across the session (what request attributes aim to solve).

I get around these problems by using a **session** and **request** object off my attributes. You can see an example of the session field in the above code snippet saving lastResponse and lastReprompt. I don’t want to save these persistently, so I clear this entire object before persisting to storage at the end of the session. In a similar fashion, I clear the request object each time at the end of my response interceptor, so those attributes truly remain request-only.

#### Avoiding Common Errors

One of the limitations that plague many developers is that responses can’t contain more than 5 audio tags. Sometimes it can be difficult to avoid this with dynamic content.

For example in my Blackjack skill, I play a sound for each card that is dealt. Normally not a problem. But when reading out the dealer’s hand, if they end up drawing several cards you can go over this limit. Sure, I could try to catch this when I’m generating the response, but that convolutes the code. Who’s to say whether it hits every edge case?

Far better to remove the excess sound effects as part of the response handler. For this skill, I just remove excess audio files from the end of the response to get the count down to 5.

Another problem that I’ve encountered is that you aren’t allowed to return directives along with the Dialog.Delegate directive if you are eliciting slots from the user. This can be annoying if you are handling button input or using display directives. You might have to check in multiple places before adding directives to your response to make sure you don’t clash with the Dialog.Delegate. Keep your code clean and use a responseInterceptor to filter through your directives before returning instead:

I hope you enjoyed these tips and see the power of using response interceptors. Let me know your own best practices and share your own tips in the comments section!

