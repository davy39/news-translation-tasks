---
title: Let’s talk about YOU — and the Singleton design pattern
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-04T10:42:44.000Z'
originalURL: https://freecodecamp.org/news/lets-talk-about-you-and-the-singleton-design-pattern-bb2e160fa952
coverImage: https://cdn-media-1.freecodecamp.org/images/1*dIc3a1EKWwu3dwB1sPtvRw.png
tags:
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: Ruby
  slug: ruby
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Sihui Huang

  This might be the most important post in my Design patterns in life and Ruby series,
  because this one is about YOU.

  Before anything, you need to listen to this song:

  No, I’m serious.

  The song is less than 2 minutes.

  Listen to the song ...'
---

By Sihui Huang

This might be the most important post in my [Design patterns in life and Ruby](http://www.sihui.io/design-patterns/) series, because this one is about YOU.

Before anything, you need to listen to this song:

No, I’m serious.

The song is less than 2 minutes.

Listen to the song before you read any further.

Let’s take a look at the lyrics of the song:

> Stand tall.

> **_You’re in a class by yourself._**

> Be proud.

> **_You’re not like anyone else._**

> No doubt about it. You’re second to none.

> **_’Cause you are the one and only one._**

> Chin up.

> **_’Cause you are one of a kind._**

> Chest out.

> We know that **_we’ll never find anyone like you under the sun_**.

> **_’Cause you are the one and only one._**

> If everybody were like everybody else, how boring it would be.

> The things that make me different are the things that make me me.

**You’re in a class by yourself, you’re one of a kind, and you’re the one and only one!**

This uniqueness is exactly what the Singleton pattern is about!

Definition of the Singleton pattern:

> The Singleton pattern:

> - **ensures a class has only one instance**,

> - and provides a global point of access to it.

The second part of the criteria is easy to fulfill — basically any class can provide a global point of access.

But a simple class like this does not ensure that the class only has one instance:

![Image](https://cdn-media-1.freecodecamp.org/images/1*s3lXUeDR62XehFAku_FOpQ.png)

We can easily create two different instances of `you`.

It’s because the `new` method, the method for creating instances for the class, is public.

To prevent having multiple instances of the class, we can try to mark the `new` method private, so no one outside of the class has access to the method — unless you really go out of your way and use `You.send('new')`. You can always call `.send(method_name)` to invoke a private method in Ruby, if you really want to go against the will of the author of the code.

![Image](https://cdn-media-1.freecodecamp.org/images/1*qVaeV0F_M36Oy5w3wnIu7Q.png)

But then we can’t create an instance of the class at all!

Why don’t we create an instance from inside the class and open a point of access to the outside world?

(In Ruby, @@ indicates the variable is a class variable.)

Now there is a way to access the instance created within the class:

![Image](https://cdn-media-1.freecodecamp.org/images/1*ldvn18SnL_RnPdKedqjcqQ.png)

Both criteria of the Singleton pattern’s definition have been met:

> - ensures a class has only one instance,

> - and provides a global point of access to it.

We just wrote a simple example of the Singleton pattern!

There are many advantages of using the Singleton pattern. One of them is lazy initialization:

> the tactic of **delaying the creation of an object**, the calculation of a value, or some other expensive process **until the first time it is needed**.

In the above code, we don’t initialize the instance until the first time `LazyYou.instance` is called which is the first time the instance is needed.

Now you have a basic understanding of the Singleton pattern.

Next time when you try to ensure a class only has a single instance, you can consider this pattern.

And when you are down, remind yourself that **you are the one and only one and the things that make you different are the things that make you you :)**

### Takeaways

1. **The Singleton pattern ensures a class has only one instance and provides a global point of access to it.**
2. **Be proud. You’re not like anyone else.**

Don’t forget to subscribe so you won’t miss the next post!

Next time we will talk about …

![Image](https://cdn-media-1.freecodecamp.org/images/1*9gP8bD5I_NpQFgRIAGtT7g.png)

