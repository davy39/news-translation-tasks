---
title: 'Elixir: A Big-Picture Programming Language'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-22T16:40:02.000Z'
originalURL: https://freecodecamp.org/news/elixir-a-big-picture-programming-language-755dcef2fa6a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tLIXa6jWWjxfB-6AYjm2Hg.jpeg
tags:
- name: Elixir
  slug: elixir
- name: Erlang
  slug: erlang
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By CityBase

  Elixir makes programmers better at their work, and it makes their work better

  About a year ago, I decided to pursue the chance to work with Elixir full time as
  lead engineer at CityBase. Since I began using the programming language in 201...'
---

By CityBase

#### Elixir makes programmers better at their work, and it makes their work better

About a year ago, I decided to pursue the chance to work with Elixir full time as lead engineer at CityBase. Since I began using the programming language in 2014, my goal has been to use, grow, and learn more from Elixir.

CityBase attracted me for other reasons, too. I’ve always been curious about making complex systems work better. With government technology, we have the challenge to make some of the most complex systems work more effectively for people on a massive scale, to massive impact.

These objectives — growing Elixir and coding for large-scale impact — are in my opinion the same. I really believe that today, reliability, concurrency, and fault tolerance are foundational qualities that most applications should be built on. Elixir can help with that based on a battle-proven list of applications and concepts.

![Image](https://cdn-media-1.freecodecamp.org/images/UtGCPFkJSMeNlcix48URAs-F-7-YIhJyx8mf)
_(Photo: [Unsplash](https://unsplash.com/photos/w7ZyuGYNpRQ?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Kevin</a>, <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="))_

### A New Language with Tested Roots

Elixir is a new language created in 2011. It’s built with the principles of Erlang, a system developed in 1986 for the telecom industry. Erlang is the reason your phone is never temporarily shut down for maintenance. It’s responsible for hardware flexibility and scalability, so you can replace a phone and have your account work the same, and add new phone lines without affecting performance.

Even though Elixir is relatively young, it relies on Erlang’s proven virtual machine (VM), called BEAM, and its principles of high availability, adaptability, and scalability. These features are exceptionally important in govtech applications, where the fundamental services delivered by technology must be available to everyone.

### The Programmer’s Programing Language

Engineers like me are excited to work with Elixir because it helps us be better at our jobs. To code with Elixir, developers need to be in tune with overall business objectives, and code with the future flexibility in mind.

It includes tools that encourage programmers to plan around what can go wrong, and focus on getting as close as possible to the ideal outcome for the end user.

**Having programmers who understand the desired big-picture outcomes can be a game changer.**

If you ask someone to write code that performs a certain function, they’ll write that code. But if you ask them to write code that leads to an experience or solves a problem, they may think of a solution you never considered — and foresee problems you didn’t know existed.

Elixir encourages this kind of big-picture thinking in its DNA. A shared characteristic of Elixir and Erlang is that they are holistic programming languages. You could easily use Elixir to develop just one service, but it is optimized for developing large systems of many services.

### A Language That’s Fault-Tolerant

Like death and taxes, another certainty in life is that things will go wrong.

Elixir has native fault tolerance for the two major types of programming errors.

#### **Error Type 1**

The rarest issues are usually discovered in production and are by definition harder to test for. For instance, connectivity (when a service goes down or is taking longer than expected) between a third-party service or a system resource, such as a database.

To be fault-tolerant to these issues, your system must always be available to customers by using at least two servers. This is to address hardware issues, network problems, or other errors that live outside your program.

Elixir runs on Erlang’s BEAM VM, which is configured as a mini OS on top of the server OS. The VM is responsible for the communication between servers and nodes. A node will be notified when another node is down, and the system will act in response.

#### **Error Type 2**

Issues associated with data are easier to test and can be reproduced locally. For example, if a function that does any math calculation receives a string instead of a number, that function will fail.

For a program to be fault-tolerant here, your system must be able to “heal” itself during errors stemming from logic bugs, wrong input data, and other internal failures.

As Elixir is a compiled language, any mistakes in the code prevent the application from starting. This ensures that running applications at least have a valid starting state.

For this to work smoothly, the Erlang VM uses something called the supervision principle, which goes like this:

* Processes are structured based on the idea that there are both “worker” and “supervisor” modules built into a given program.
* Workers perform computations, and supervisors monitor workers.
* If something goes wrong, a supervisor can restart a worker to its initial valid state.

The supervision principle is associated with process isolation, when one module can run in one isolated process. This ensures that errors in one module will not affect other parts of the application, and you can restart that module in isolation as well.

### A Language That’s Modular and Built to Scale

Elixir is a modular language, meaning that you can modify self-contained parts without worrying about impacting other, unrelated parts. Microservices function concurrently. These code-based actions all play roles in the greater program you’ve created, but tasks are distributed so that they are not dependent on one another to work. This reinforces the benefits of failing fast — you take one faulty player out, and the game still continues.

This also becomes crucial as a codebase grows: in non-modular systems, it’s not always clear when one part impacts others — or which other parts it might impact. This means that even the smallest change requires that you test everything to ensure that the change didn’t break anything. This makes for a daunting amount of work, which means projects move slowly and require lots of people.

It also means that training new developers is difficult and time-consuming, as they must familiarize themselves with a complex code legacy in order to effectively expand it.

With Elixir, **developers focus on the future, and ensure they’re coding for new or evolving goals**, rather than a previous vision that’s baked into overly complex code.

Beyond its modularity, Elixir is also highly scalable. The language enables you to start building an application running only one or two servers and to add more as needed. Together, the servers function as part of a cluster in a distributed system to achieve high availability and scalability.

Within that cluster, servers communicate using an Erlang-based protocol, rather than having to implement or use any application protocol like HTTP, and pick a data serialization/deserialization option like JSON or Protocol Buffers. That means you don’t need to implement anything to pass data between services in different servers/nodes. This is huge in terms of complexity of logic for communication.

### A Language That Has No Niche

Obviously, I’m a fan of Elixir. It’s got a lot going for it, from its proven infrastructure to its scalability. But maybe the coolest thing about this language is that it’s industry agnostic. Already, it’s been adopted by a range of companies, for a variety of purposes: WhatsApp, Bleacher Report, Netflix, Pinterest, Postmates, and a handful of .gov sites all use Elixir or Erlang.

This is a plus for several reasons: first, it means that the language is likely to continue to grow in popularity as companies recognize the benefits it can offer. That, in turn, means that developers will continue to learn it, which means there’s not likely to be a shortage of developers who know Elixir. Companies of all sizes should be able to find developers at all levels to work with Elixir.

Given the power this language has to improve user experience, minimize downtime, and make life easier for dev teams, these are indicators everyone should be cheering — especially those of us in engineering and programming fields.

For those of us in govtech, Elixir is especially promising, as it embodies the kind of resilience and long-term focus essential to making governments function better for everyone.

• • •

By [Pedro Assumpcao](http://pedroassumpcao.ghost.io/), Lead Software Engineer at CityBase

