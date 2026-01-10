---
title: The Observer Design Pattern is kind of like a podcast
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-25T03:55:11.000Z'
originalURL: https://freecodecamp.org/news/the-observer-design-pattern-is-kind-of-like-a-podcast-cdee5ef9f074
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_lV71Wek7B9MUmsOjS76gQ.png
tags:
- name: design patterns
  slug: design-patterns
- name: learning to code
  slug: learning-to-code
- name: General Programming
  slug: programming
- name: Ruby
  slug: ruby
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Sihui Huang

  If you listen to podcasts, you are already familiar with the Observer pattern. In
  fact, you are an “observer”.

  Here’s the definition for the Observer pattern:


  The Observer Pattern defines a one-to-many dependency between objects so th...'
---

By Sihui Huang

If you listen to podcasts, you are already familiar with the Observer pattern. In fact, you are an “observer”.

Here’s the definition for the Observer pattern:

> The Observer Pattern defines a one-to-many dependency between objects so that when one object changes state, all of its dependents are notified and updated automatically.

### Let’s look at the definition as related to podcasts.

I found an interesting podcast named `developer tea`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*-lQ8wA_1gNxtwimzoqKfGA.png)

After clicking the `SUBSCRIBE` button, I’m now on their subscriber list.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GBO65Rn7VDroo7R5sbkfKw.png)

When `developer tea` releases a new episode, the app will notify me and other subscribers. It downloads the new episode for us.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_bOkx12Vqyr9b7zBlDUVVg.png)

That’s exactly the definition of the Observer pattern!

> The Observer Pattern defines a one-to-many dependency between objects so that when one object changes state, all of its dependents are notified and updated automatically.

There is a one-to-many relationship between the `developer tea` podcast and `subscribers`.

When `developer tea` changes state, such as releasing a new episode, all of `developer tea`‘s `subscribers` are notified and updated.

### Let’s implement it in Ruby.

Start with a simple version.

The `Podcast` class holds a list of episodes and has a method to `add_episode` to the list.

Then we can create the `developer_tea` podcast and add episode #1 to it like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*79mOvT3PAVnOZKIzmkhAog.png)

I want to get a notification whenever a new episode is released.

We can update me after adding a new episode to the list:

And whenever I get an update from `developer_tea`, I can go ahead and download the latest episode.

I enjoy listening to `developer_tea` so much that I recommend it to my friend, Amber. Now, Amber wants to subscribe to it as well.

![Image](https://cdn-media-1.freecodecamp.org/images/1*PKqEa9I2eoOKJAs_ajZUxA.png)

We need to make sure Amber also gets a notification whenever a new episode is released:

Hmmm, this code does what we want.

But there is a problem.

Each time we want to add a subscriber, we have to redefine the class.

Is there a way to update the subscriber list without having to redefine the class????

### ??We can keep a subscriber list!??

The new `Podcast` class keeps a subscriber list with the help of two new methods: one for adding subscribers and one for removing subscribers. When an episode is released, we update each subscriber.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xnCj4ij96f0MS6ioiOxk6w.png)

Unfortunately, Amber doesn’t enjoy the podcast as much as I do and decides to unsubscribe. We use the `remove_subscriber` method to remove her from the subscriber list.

![Image](https://cdn-media-1.freecodecamp.org/images/1*berwHCxfb4NDDv7XbcPjAw.png)

**??Yay! You just learned the Observer pattern!??**

### **Design Principle behind the Observer pattern.**

**The Observer pattern utilizes the Loose Coupling design principle:**

> **Strive for loosely coupled designs between objects that interact.**

**The `Podcast` class doesn’t know much about its subscribers. It only knows each subscriber has an update method.**

**This loose coupling minimizes the dependency between Podcast and its subscribers. It also maximizes flexibility. As long as it has an update method, a subscriber can be anything: a human, a group of people, an animal, or even a car.**

**Takeaways**:

1. **The Observer Pattern defines a one-to-many dependency between objects so that when one object changes state, all of its dependents are notified and updated automatically.**
2. **Loose Coupling design principle: strive for loosely coupled designs between objects that interact.**

**Thanks for reading. Are there any other real-life examples of the Observer pattern you can think of? ?**

**I publish to [sihui.io](http://www.sihui.io/) weekly.**

**Subscribe so you won’t miss the next article from the series.**

**Next time we will talk about…**

![Image](https://cdn-media-1.freecodecamp.org/images/1*dIc3a1EKWwu3dwB1sPtvRw.png)

