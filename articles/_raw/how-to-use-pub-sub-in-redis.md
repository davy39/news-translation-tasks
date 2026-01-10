---
title: Pub/Sub in Redis – How to Use the Publish/Subscribe Messaging Pattern
subtitle: ''
author: Mihail Gaberov
co_authors: []
series: null
date: '2023-04-28T14:33:25.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-pub-sub-in-redis
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/image-332-1.png
tags:
- name: messaging
  slug: messaging
- name: Redis
  slug: redis
seo_title: null
seo_desc: 'When you''re working on an application that needs to be easily maintainable,
  scalable, and performant, the Publish/Subscribe messaging pattern is a good choice.

  The idea behind it is simple, but powerful. We have senders called publishers. Their
  sole ...'
---

When you're working on an application that needs to be easily maintainable, scalable, and performant, the Publish/Subscribe messaging pattern is a good choice.

The idea behind it is simple, but powerful. We have senders called *publishers.* Their sole role is to send or *publish* messages. They don’t care about who is going to receive them or if someone will receive them at all. They just shoot and forget the messages. And they do that via *channels*.

Think of them as, for example, TV channels. We have Sports channels, Weather Forecasting channels, Cooking channels, and so on. Every publisher sends its messages to a certain channel, and whoever is *subscribed* for this channel will be able to receive these messages.

Here is where the *subscribers* come in play. They can subscribe to one or more channels and start receiving the messages broadcasted in there.

As we already mentioned, the messages are to be sent and forgotten. This means that if a subscriber subscribes for a certain channel, all the messages that were sent previously in that channel are not going to be available to this subscriber.

Due to the nature of this kind of architecture, we can easily achieve low coupling between the different components and provide a solid foundation for building robust and easy-to-maintain applications.

For example, imagine a situation where we need to replace or improve the publishing part of our system – say add more publishers, more channels or so on. Since the two parts are isolated, meaning publishers don’t care about subscribers and vice versa, we could easily do that without worrying whether we are breaking some other part of the system. We just add the new publishers. Then later, when a subscriber comes to the relevant channels, it just starts using them.

## What is Redis?

The initial idea behind Redis was to serve as an in-memory cache solution, as an alternative to its ancestor [Memcached](https://www.memcached.org/).

But nowadays it's a many-in-one solution, providing an in-memory data structure store, key-value database, message brokering, and so on. This makes it perfect candidate when building an application that needs a really fast caching solution as well as some of the other features mentioned before. Especially if the performance of the app is crucial for its regular usage.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-333.png align="left")

*Redis performance comparison (source: google)*

One of the biggest advantages when using Redis is the huge community and technical resources you can find online. A lot of these resources are free, and there are online platforms that have free tier offerings.

Redis includes in its arsenal a cloud solution as well. If you want to try it yourself, you may go [here](https://redis.com/try-free/) and register a free account or use their initial coupon offering.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-334.png align="left")

*Redis Enterprise Cloud Sign Up / Sign In page*

## Pub/Sub in Redis

### What is pub/sub?

[Publish/Subscribe channels in Redis](https://redis.io/docs/manual/pubsub/) is one of the features I haven’t mentioned above but it’s included in the last versions of Redis. This is their implementation of the [pub/sub messaging pattern](https://redis.io/docs/manual/pubsub/), where we have publishers and subscribers that exchange messages via channels.

We'll go briefly through it below and then see it in practice in a [small demo app](https://github.com/mihailgaberov/redis-pub-sub-visualized) I have prepared for you.

### How does Redis pub/sub work?

We have publishers (the producers of messages), channels (that the messages are going through), and subscribers (the receivers of the messages). Who receives what depends solely on who is subscribed to which channel.

**Let's see how this works in an example:**

If we have created three publishers which will be publishing messages to three different channels. Let’s call them channels 1, 2 and 3. We also have three subscribers, let’s call them subscribers A, B and C.

Now, let’s imagine subscriber A is listening for messages on all three channels, that is, it's subscribed to them. And subscribers B and C are subscribed to channels 2 and 3. This means that when either of the three publishers sends a message, subscriber A will receive it. And subscribers B and C will be receiving messages sent only by publishers 2 and 3, because they are listening only for messages on these channels (2 and 3).

Notice that we have two entities using a channel – one is sending, the other is receiving – but they are totally independent. And the messages being sent are not persisted. Once they are sent by the publisher they are forgotten. The only entities that are subscribed at the moment of sending will get them.

### How to use pub/sub in Redis

There are a plethora of client libraries that you can use with Redis. There is a [dedicated page](https://redis.io/docs/clients/) where everybody can go and pick one, depending on the specific project needs or just on your preferred programming language.

People at Redis also marked some of these repositories as *recommended* which makes the choice easier, if you are new to all this.

For our demo below, I used [ioredis](https://github.com/luin/ioredis), a full-featured Redis client for Node.js. I chose this because the demo app UI is built with React and Node.js and my server code goes pretty well with it.

## Redis Pub/Sub Demo

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-336.png align="left")

*Redis Pub/Sub Visualizer app*

Show time!

The idea behind the [demo application](https://github.com/mihailgaberov/redis-pub-sub-visualized) is to show visually how the pattern works.

What you will see when you open it for first the time is three buttons for publishing simple messages (news) in the three imaginary TV channels: Weather, Sports and Music.

The cards below the publish buttons are the subscribers. Once you move your mouse cursor over any of them, it will flip to its back side and you will see three buttons. You may use each of these buttons to subscribe to the relevant channel.

Once a subscriber is signed over a channel and you click on the icon or the publish button for this channel, you will see a sample news appearing on the front side of the card.

Play with different publishers/subscribers combinations and see the result.

I hope this will give you a better understanding of what I explained in the example above.

### **How to run the demo app locally**

In order to install and run the demo application locally, follow the steps below (all commands are considered to be run from the root project directory):

**Run frontend:**

`cd client yarn && yarn dev`

**Run backend:**

`cd server && yarn yarn start`

And finally, use your local installation of Docker (if don’t have one, you may get it from [here](https://docs.docker.com/get-docker/)) to run this:

```python
docker run -p 6379:6379 redislabs/redismod:preview
```

That’s probably the easiest way to have a running copy of Redis locally. The other option would be to use [Redis Cloud](https://redis.com/try-free/) directly and deploy the application online. This is an option I am still investigating and if I manage to do it, I will deploy the whole app and will let you know.

## Closing

This article introduced you to the pub/sub messaging pattern subject. It's important to remember that whenever we want to build a highly performant application with a low coupled architecture and real-time like messaging features, consider using the Publish/Subscribe pattern and Redis in particular.

In fact a lot of the real life applications that use Redis are dashboard-based. This means that usually there is a nice dashboard screen, showing different data, often being updated in real time.

Imagine, for example, a system showing traffic in a specific area. This kind of software is a perfect candidate for leveraging the advantages of pub/sub. And in many cases this is achieved by using Redis.

In any case, as developers and engineers, we should always be guided by the specific needs of the project we are working on. Whenever we decide to introduce a new pattern or technology, we should do it carefully and back it up with serious research.
