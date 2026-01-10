---
title: Why you should stop using big words and industry jargon (and what to do instead)
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2018-09-03T23:45:15.000Z'
originalURL: https://freecodecamp.org/news/why-you-should-stop-using-big-words-and-industry-jargon-and-what-to-do-instead-f38c229693e0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*o7WmwGkLVR0dVQUYqfSBeg.jpeg
tags:
- name: communication
  slug: communication
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: teaching
  slug: teaching
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'Let’s say you want to teach a person something. Why does the person not
  understand what you’re saying?

  One of the main reasons is likely because we like to use big words and industry
  jargon. This jargon may mean something to us, but it means nothing ...'
---

Let’s say you want to teach a person something. Why does the person not understand what you’re saying?

One of the main reasons is likely because we like to use big words and industry jargon. This jargon may mean something to us, but it means nothing to the people we’re trying to teach.

The next time you try to teach programming, watch out for the words you use.

### Three types of big words

We can divide jargon into three categories:

1. That which can be explained in a few words
2. That which cannot be explained with simple words
3. That which can mean different things in different contexts.

When you teach, you should always watch out for these three types of words.

### Jargon that can be explained in a few words.

If the jargon can be explained in a few words, you want to **use those words instead of the jargon.**

Interoperability is one example of a such a word.

It sounds scary and complicated, but it can be explained in a few simple words.

If you searched for the meaning of interoperability, you’ll come across definitions like these:

From Wikipedia:

> “_Interoperability is a characteristic of a product or system, whose interfaces are completely understood, to work with other products or systems, at present or in the future, in either implementation or access, without any restrictions._“

From Dictionary.com:

> “_Interoperability is the ability to share data between different computer systems, especially on different machines._“

If we put it in simple terms, “interoperability” means the “ability to share data”.

See how it makes the language barrier much lower?

If you can replace such jargon with simple words, why would you stick to the difficult word?

### Jargon that means different things in different contexts

Some jargon has different meanings when it’s used in different contexts.

One example of such jargon is encapsulation.

To encapsulate something means to enclose that thing with something else. If you wrap a potato with a cloth, you can say the cloth encapsulates the potato.

Developers love the word encapsulation. They use it all the time.

The first way is to wrap variables and other code inside a function. In this case, the function encapsulates the code within.

```
// This is JavaScriptfunction someFunction () {  const variableName = 'I am a variable!'}
```

The second way is to contain an object’s individuality. For example, if you have a Human object, and you create two humans from the human object, these two humans should not be the same.

In this case, each object encapsulates its own data.

```
// This is JavaScriptfunction Human (name) {  this.name = name}
```

```
const zell = new Human('Zell')const vincy = new Human('Vincy')
```

```
zell.name === vincy.name // false
```

The third way is for information hiding. In JavaScript, we can create private variables. These private variables are enclosed by the object.

In this case, the object encapsulates the private variable. You cannot access the private variable. In this case, encapsulation is used to mean something different from the second case.

```
// This is JavaScriptfunction Human () {  const privateVariable = 'private'  this.publicVariable = 'public'}
```

So what do you understand by Encapsulation?

You can’t be sure.

There should be no ambiguity when you communicate. If there is ambiguity, communication breaks down, and students don’t learn.

It is best to **ditch the jargon if the jargon means different things in different contexts.**

### Jargon that cannot be explained with simple words

Some jargon cannot be explained with simple words. This jargon is often used to talk about abstract concepts, which is why simple words may not be enough.

One example of such a word is “mutation”.

Mutation comes from the word mutate. To mutate means to change in form or nature. In JavaScript, mutation happens underneath the hood without you noticing.

In this case, change is not enough to explain mutation. It lacks depth and detail. Plus, change is still too abstract.

You feel that a concept is abstract, because you cannot imagine it. You cannot see, hear, feel, touch, or taste it. To make an abstract concrete, we need to appeal to a human’s five senses.

**To explain an abstract concept, you can use analogies.** When you use analogies, you can describe an object or a scenario in a way where people can see, hear, or feel what you mean.

For example, [I used X-men as my analogy when I explained mutation](https://alistapart.com/article/why-mutation-can-be-scary).

I asked students to imagine a friend growing fur and turning blue in front of their eyes. Anyone can imagine what it means to grow fur and turn blue, even if they don’t know who Beast is.

If you want to expand the analogy to cater to more people, you can appeal to more senses. For example, to get blind people to imagine mutation, you can also tell them to imagine their friend growled like a beast.

The key here is a change that goes undetected. Nobody knows whether a person is a mutant until they show their powers. On the same front, nobody knows that a JavaScript object has changed until it, well, has changed.

I emphasized this point to draw a link back to mutation in JavaScript.

Mutation becomes more concrete once the link gets established. When I say mutation, students who read the article can picture their friend turning blue, growing fur, and growling like a beast.

Once you turn abstract jargon into a concrete concept, you can use that jargon as you usually would. Students will understand what you mean.

I wrote an article about [creating good analogies](https://zellwk.com/blog/creating-good-analogies) if you’re interested in learning this skill.

### Wrapping up

Pay attention to the words you use when you teach programming. If you use difficult words that don’t mean anything to your student, they won’t be able to get what you mean.

Replace difficult words with words that are simpler and easier to understand if you can.

Avoid using jargon that can mean different things in different contexts. This jargon makes things ambiguous and confusing.

Finally, use analogies to turn abstract concepts into concrete concepts.

Thanks for reading. Did this article help you in any way? If you did, [I hope you consider sharing it](http://twitter.com/share?text=Stop%20using%20big%20words%20and%20industry%20jargons%20(and%20what%20to%20do%20instead)%20by%20@zellwk%20?%20&url=https://zellwk.com/blog/big-words/&hashtags=). You might help someone out. Thank you!

This article was originally posted at [zellwk.com.](https://zellwk.com/blog/big-words)  
Sign up for my [newsletter](https://zellwk.com/) if you want more articles to help you become a better front-end developer.

