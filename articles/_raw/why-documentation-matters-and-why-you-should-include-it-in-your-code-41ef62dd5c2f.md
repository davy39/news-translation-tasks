---
title: Why documentation matters, and why you should include it in your code
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2018-08-07T17:17:30.000Z'
originalURL: https://freecodecamp.org/news/why-documentation-matters-and-why-you-should-include-it-in-your-code-41ef62dd5c2f
coverImage: https://cdn-media-1.freecodecamp.org/images/0*OQGgMhx12tTMWgv0
tags:
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'There are a plethora of acronyms when it comes to software development.
  KISS, DRY, SOLID… and so on and so forth. But, when it comes to documenting or commenting
  your code, there is no simple catchphrase.

  Why is that?

  Documentation should be as impor...'
---

There are a plethora of acronyms when it comes to software development. KISS, DRY, SOLID… and so on and so forth. But, when it comes to documenting or commenting your code, there is no simple catchphrase.

Why is that?

**Documentation should be as important to a developer as all other facets of development**

In this article, I’ll argue why documenting your code will lead to becoming a better developer, and will contribute to being a great team member.

### Ain’t nobody got time for that

The main reason code goes undocumented is because of time.

When developing a feature that needs to be completed within a certain time frame, rarely do we have a moment to stop everything and focus on documenting our code.

Apart from designing and writing the code itself, we also need to undergo code reviews, automation tests, and add unit tests (to name a few things). Documentation is pretty much left out of the equation.

**It is the least thought about detail that can make the most difference in the future.**

No matter what you are developing, chances are that some day you or one of your colleagues will have to revisit it. When that day comes, you will not remember so vividly what you wrote and why.

And if you do remember, there may be some edge cases or specific uses which may not be clearly apparent. The obvious solution is **documentation**.

Taking that extra time to write a proper description of what you worked on will save **huge** amounts of time in the future.

Next time someone wants to understand what happens inside your code, all you have to do is point them to the documentation. It will save time for you, since you won’t need to explain things, and it will save time for them, since they won’t be dependent on you.

And after all, when you, as a developer, need to understand something about a certain aspect of coding, what do you do?

> ? You go to the documentation ?

### Good code does not need documentation

Yeah, I know, I know… well written code, that is concise and well thought out, does not need to be documented. **It reads like a story**.

While that may be so, it does not forego the need for documentation, and here is why:

1. We are all too familiar with the robustness of code that comprises a feature. Looking at one section of code, may not make it clear there are other sections that are deeply linked to it.
2. Every service you create has a unique API to it. Writing how to use that API requires documentation that can be read outside of the code. You do not want to inflate the class itself with details about how to use the API.
3. Coworkers who work in different departments (who may not be developers) may want to understand what you did and how it works.
4. Just the act itself may cause you to look differently at the code you wrote. Explaining what your code does will cause you to assess the validity of it and to maybe consider changing things if they do not meet your expectations.
5. For posterity’s sake

![Image](https://cdn-media-1.freecodecamp.org/images/5jPNlmEKOGjTR294BEYE1stmTaQuIP38GzPM)
_“A person writing with a pencil in a notebook with pencil shavings on it” by [Unsplash](https://unsplash.com/@thoughtcatalog?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Thought Catalog</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

### How to write good documentation

Good documentation is like a good block of code. Short, simple, and easy to understand. Here are a few guidelines you can follow:

* Understand who the documentation is aimed at. Is it only for developers? Is there a broader audience? Understanding this will save you time, since you will know up front how much to elaborate in your explanations.
* Write a short, but descriptive background explaining the main points of what you built. This will help readers understand the purpose of the feature and ascertain its relevance to what they want to know.
* List and describe the main perspectives of your feature, making sure to point out any dependencies that exist with other features.
* Make sure there is a timestamp, to tell readers the validity of the documentation. Also, if you are using certain libraries, be sure to include their versions as well.
* Be generous with your coding examples, detailing how to properly use the feature you wrote and showcase the expected results.

### Examples

To further understand how good documentation looks like, we’ll review some great examples: [Mozilla’s Developer Network(MDN)](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API), [Django](https://docs.djangoproject.com/en/2.0/) and [Stripe](https://stripe.com/docs).

![Image](https://cdn-media-1.freecodecamp.org/images/ttMCqH73G7L0lkB4Pg5RTAjPcnH9Q2-bfCRN)
_Notice the quick links at the top for easier navigation_

In MDN’s documentation, you can clearly see that each page starts with a brief explanation about the subject.

Then, it proceeds to detail the use cases and methods. Finally, it shows which browsers are compatible with the feature and gives links to relevant material.

![Image](https://cdn-media-1.freecodecamp.org/images/n8TyfIok8mUQEmt6OeypnOV6pVp-TwJRSFaH)
_In Stripe’s documentation, each subject has code snippets that can be viewed in various coding languages_

![Image](https://cdn-media-1.freecodecamp.org/images/6AgI3-4qhfO2BH7hrr0fXt8kbUScCjCI1KnV)

Django’s documentation is very robust. No matter your coding level, they start you off with an overview and tutorials.

Then, they go through each subject, detailing it meticulously, giving short and concise code snippets that demonstrate what needs to be done

I hope I have managed to stress the importance of documentation and have given you some pointers on how to start documenting your code. If you have an idea for an acronym for documentation, feel free to do so in the comments below.

Maybe KID — **K**eep **I**t **D**ocumented?

_If you liked this article, clap away so that others can enjoy it as well! ???_

