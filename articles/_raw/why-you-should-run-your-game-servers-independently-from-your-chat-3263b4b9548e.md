---
title: Why you should run your game servers independently from your chat
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-11T13:52:16.000Z'
originalURL: https://freecodecamp.org/news/why-you-should-run-your-game-servers-independently-from-your-chat-3263b4b9548e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5SUE6G0j6lpp5N-RYmn_jQ.png
tags:
- name: Game Development
  slug: game-development
- name: Microservices
  slug: microservices
- name: mobile app development
  slug: mobile-app-development
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Joe Hanson

  When it comes to building multiplayer games, developers are often faced with a dilemma.


  Do I utilize my existing game servers already powering my multiplayer game functionality
  to run chat?

  Do I separate my game servers and run my chat...'
---

By Joe Hanson

When it comes to building multiplayer games, developers are often faced with a dilemma.

* Do I utilize my existing game servers already powering my multiplayer game functionality to run chat?
* Do I separate my game servers and run my chat independently?

Because, after all, they’re just chat messages, right? Small messages being sent to a single user or a small group, so you might as well just utilize what’s already built…what could it hurt?

Though it may seem like a good option initially to utilize what you already have, there are a number of problems that can arise from choosing that design pattern.

I’ll show you why you should run your game servers and social features (most importantly, chat) independently, benefiting both you as a game developer and your end users. In doing so, you’ll increase performance and scalability of the game itself, and you’ll allow social features to be easily extended with new functionality in the future.

### Microservices make your game more manageable

A microservice-oriented architecture breaks up a large application, in this case your game, into small, independently versioned modular services that talk to each other through simple, universally accessible APIs. It makes it much easier to build new functionality and maintain the functionality once built.

Separating your game servers from your chat functionality makes your entire infrastructure more manageable, and gets you closer to a completely microservice-oriented architecture. In this case, let’s look specifically at in-game chat, and it’s relationship with the game servers powering the multiplayer game.

With a monolithic architecture, your development team is now locked into a single technology stack — using the same programming languages, databases, and software environments that the game was already built on. When bringing on new developers, or when you want to prototype new technologies and systems, it’s much easier to move fast in a microservices architecture.

Dependencies are also much more apparent with monolithic architectures. If your single application function fails, the entire game goes down. Splitting your game into microservices makes it easier to isolate a fault and fix it if a single module fails.

Your game servers are built for delivering player movement and state in realtime, and they do that really well. Repurposing the same technology and design for chat messages is simply not using the best options for the particular functionality. Decentralized components are easier to maintain, and they scale better.

![Image](https://cdn-media-1.freecodecamp.org/images/kxjPuS481xkdGVK8aUOcBCxl-IF3jKlz9ltN)

The above figure depicts a game infrastructure where chat is separated from the game servers.

Additionally, we can also run other services outside the game servers, including authorization, presence, statistics and leaderboards.

### Ensure Seamless Gaming Experience and Chat Performance

Overall, game performance is a major consideration for a multiplayer game. A slow gaming experience will drive away users and they’ll never return. With a monolithic architecture, the game may perform in the lab. But for multi player games with a high number of users located anywhere in the world, all communicating simultaneously at a rapid pace, you’ll begin to see lag and increased latencies on both delivery of the chat messages and the experience of the game.

Separating the two ensures that CPU and network resources are used more efficiently. The primary purpose of your game servers is to deliver a seamless experience for every user in your game. As a result, the processing power should be used to maximize that performance.

Say you have an online battle arena game like League of Legends or EVE Online. You may have hundreds of players in a single world, at a single time. That’s thousands of messages being sent through your game servers delivering every input each player creates. Now, add in chat messages to the mix. It’s entirely possible that players can spam the chat channel and deliberately slow down the game server since all messages would have the same priority. Of course, it would be possible to check for such users, but you’d require additional processing to take place, which would eat away at the resources of the game server.

The game server is already handling intensive gameplay experiences — physics, graphics, and sound. When you add in chat messages — one-to-one, group, team —and parsing and routing the messages to the correct users — all these messages slowly build up for large-scale games, and hurt the overall performance of the game.

It’s a no-brainer to run chat channels separately from the multiplayer channels. It is stealing important processing power that could be better suited for more complex problems than routing chat messages.

### UDP vs. TCP: when you need both, and when you don’t

Then there’s the debate over multiplayer gaming protocols, UDP vs TCP, and when it’s best to use either one.

Fast-paced multiplayer games (first person shooters, arena games, and so on) use the UDP protocol to sync player movement and update game state. UDP is ideal for sending these game updates at a ridiculously fast speed, but messages are not guaranteed (because the next message is coming so fast behind).

TCP guarantees message delivery, which makes it a great option for chat. You’ll see great performance running your game on UDP and your social features on TCP.

![Image](https://cdn-media-1.freecodecamp.org/images/2rINsVWUD5qCbgxJYxq0cYIvUxHFV0iCkQdJ)

However, for less intense multiplayer games, like turn-based games, TCP is a suitable option for both gameplay and chat. Because TCP guarantees message delivery, and in games where every move matters (like a Scrabble turn or tic-tac-toe), it’s a great option to power the multiplayer gameplay. Of course, you’ll still want to separate your chat from the game servers, especially once your game takes off and you have thousands of users connected at a single time.

Latency is another thing to consider, as there are different standards of latency for multiplayer functionality vs. social features. For a multiplayer game, ensuring game state and delivering player inputs, the industry-standard is no more than 20ms. Whereas for a chat application, the maximum latency for delivery of a chat message is 250ms.

So you’ve got two different types of realtime messaging, with two different standards. Having them operate alone lets you manage each one based on what’s required.

### Add new social features with ease

Running chat as a standalone service, and picking an industry-standard protocol (XMPP, WebSockets) or a hosted-service ([PubNub](https://www.pubnub.com?utm_source=Syndication&utm_medium=Medium&utm_campaign=SYN-CY18-Q2-Medium)), opens up the opportunity to easily add new powerful social features.

Start with core chat, allowing users to carry out individual and group chats. With that, you’ve got the underlying infrastructure, as well as basic publish/subscribe. And there’s a lot of other social features you can easily build onto it.

With minimal code, you can add table stake chat features like typing indicators, user presence to show what players are online and offline, and unread message counters — features that are expected by users.

### Looking Forward

Game studios big and small are moving towards this architectural design, including [Pocket Gems](https://www.pubnub.com/customers/pocket-gems/?utm_source=Syndication&utm_medium=Medium&utm_campaign=SYN-CY18-Q2-Medium), and more recently [EVE Online](https://www.eveonline.com/article/p4i0qx/new-chat-backend-coming-with-the-march-release). From better scalability and more efficient performance, to the freedom to innovate without being locked into a single stack, the benefits are clear: separating chat from your game servers is the way to go.

_Originally published at [www.pubnub.com](https://www.pubnub.com/blog/why-you-should-run-your-game-servers-separate-from-your-chat/)._

