---
title: An introduction to SOLID, Tim Berners-Lee’s new, re-decentralized Web
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-29T15:20:48.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-solid-tim-berners-lees-new-re-decentralized-web-25d6b78c523b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*P4F0K6HR2L0VfQZmMvYt0g.png
tags:
- name: decentralization
  slug: decentralization
- name: internet
  slug: internet
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Arnav Bansal

  Recently, Prof. Tim Berners-Lee lifted the veil off a project called Solid. I decided
  to check it out. In this article, I describe what Solid aims to do, and also how
  you can get started with it.

  What is Solid?

  Solid is an attempt to ...'
---

By Arnav Bansal

Recently, [Prof. Tim Berners-Lee](https://en.wikipedia.org/wiki/Tim_Berners-Lee) lifted the veil off a project called Solid. I decided to check it out. In this article, I describe what Solid aims to do, and also how you can get started with it.

### What is Solid?

Solid is an attempt to re-decentralize the web.

_Re**-**_decentralize?

Back in the day, the vision for the web was a decentralized, collaborative read-write space. The first browser (called WorldWideWeb) was [also an editor](https://www.w3.org/People/Berners-Lee/WorldWideWeb.html).

However, as it progressed, the design of web applications began to centralize for a variety of reasons. User data became the source of power and income for Internet companies.

Solid is a solution to this.

Solid is a new paradigm for web applications, one that is backwards compatible with the existing web.

Solid is a tech stack, a group of related protocols, implementations, and a growing community. Much like the web.

### The separation of app and data

In pre-internet computing, your personal computer stored your data.

As people began using multiple computers, and added smartphones to their lives, the “your data stays with you” model was replaced by “Your data is in one or more massive data centers around the world, managed by the app developer”.

And so, applications were deeply coupled with their data. Creating an application on the web entails managing people’s data at scale.

Apps and their ability to make money are measured by their _data silo_. Your data is difficult to migrate, since different apps store your data very differently.

The result? Almost every app has walled garden characteristics. This reduces incentives for developers to innovate at the app level. Existing platforms are secured against disruption, since the data lockdown makes it hard for users to move.

### Data protection regulations

Some countries have enacted data protection laws. Companies must make your data available, and you can chose to download or delete it.

This attempts to return control over data back to users. But it’s a legal prescription, and not the technical reality. User data still lies with app developers, and the ability to download your data isn’t very useful if you can’t migrate to an alternative.

### Pods: Bring your own data

Solid remedies this on the technical side. It allows applications to be built in a way where they read and write data stored on your _pod_.

You have a pod. Your friends have a pod. Pods store your data. You allow apps to access your pod.

Maybe you have multiple pods. Perhaps separate ones for home and work. Your pod can live on your computer, or be distributed across your devices. Or it could be hosted for you.

And pods store _linked data_. Your pod can link to something on my pod, or anywhere on the web.

We want applications that run across our devices. But we also want autonomy of our data. And we want the ability for different apps to use the same data and write to it.

### The ideas behind Solid

Getting into Solid reminded me of starting out with web development. I remember learning HTML, CSS, JavaScript, and the frameworks of the day, all at the same time.

The only difference: Solid is new, and help is harder to find.

Here’s a collection of day-one concepts you’ll want to know to get started developing for Solid:

(PS: if you just wanna jump in, skip ahead to ‘First steps’)

#### **Linked data**

The power of the Solid, and the web generally, is from the way data is hyperlinked together.

In Solid, you store the data you produce wherever you want. Your personal data likely resides on your pod. To refer to this data, you use URLs, like on the web.

This is also a good time to introduce the full-form of Solid: **SO**cial **LI**nked **D**ata.

Read about [Linked Data in the context of Solid](https://solid.inrupt.com/docs/intro-to-linked-data)

#### **Resource Description Framework**

RDF is a way to represent linked data with statements of the form `subject-predicate-object`. These are also called triples.

RDF is an abstract model. You could even represent RDF in English sentences. Here’s a task on a Todo list:

```
T1 is a taskT1 is labelled "Write an article about Solid"T1 is due October 5rd 2018T1 is assigned to @itsarnavbT1 is incomplete
```

#### **Turtle**

Turtle is a compact way of representing RDF data, using URLs to represent `subject`, `predicate` and `object`.

That’s repetitive and hard to read, so turtle has a prefix and shorthand system. This gets especially important with longer documents.

You can read more about [turtle](https://solid.inrupt.com/docs/expressing-ld-with-turtle). Or you could check out a full turtle document [here](https://ruben.verborgh.org/profile/#me). It’s a detailed public profile of Prof. Ruben Verborgh, who’s a part of the Solid team.

#### Semantic web

Tim Berners-Lee best explains this:

> I have a dream for the Web [in which computers] become capable of analyzing all the data on the Web - the content, links, and transactions between people and computers. A “Semantic Web”, which makes this possible, has yet to emerge, but when it does, the day-to-day mechanisms of trade, bureaucracy and our daily lives will be handled by machines talking to machines. The “[intelligent agents](https://en.wikipedia.org/wiki/Intelligent_agent)” people have touted for ages will finally materialize

### First steps

Do these, in any order that works for you.

* [Get a pod](https://solid.inrupt.com/get-a-solid-pod): Signup with any free pod provider, or run your own server (if that’s your thing).
* [Make a Solid app with this tutorial](https://solid.inrupt.com/docs/app-on-your-lunch-break)
* [Read about these hacks made with Solid](https://solid.gitbook.io/solid-hacks/)
* [Read the Solid docs](https://solid.inrupt.com/docs)

### Go Solid

You can help out the Solid ecosystem by

* contributing to the development of Solid itself, and related infrastructure.
* developing apps using Solid.

![Image](https://cdn-media-1.freecodecamp.org/images/0*tapHw7Osr5LbkuUh)

But beware, at the moment, learning and developing for Solid requires a lot of trial and error, and asking potentially silly questions. There’s no Stack Overflow to refer to. Debugging some errors might require you to dig into the source.

Here are the communities where you can get help:

* [r/solid](https://reddit.com/r/solid) (I’m one of the mods)
* [gitter.im/solid](https://gitter.im/solid/home)

And finally, my DMs are open: [@itsarnavb](https://twitter.com/itsarnavb). I’ll try to answer every question I get, or find someone who can.

And I’ll keep this article up to date with the best resources to learn about Solid.

### Further Reading

* [Solid website - solid.mit.edu](https://solid.mit.edu)
* [Paradigm shifts for the decentralized web - Ruben Verborgh](https://ruben.verborgh.org/blog/2017/12/20/paradigm-shifts-for-the-decentralized-web/)
* [One Small Step for the Web - Tim Berners-Lee](https://medium.com/@timberners_lee/one-small-step-for-the-web-87f92217d085)

