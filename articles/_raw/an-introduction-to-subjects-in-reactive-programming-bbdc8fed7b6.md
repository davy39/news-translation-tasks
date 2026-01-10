---
title: An introduction to Subjects in Reactive Programming
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-28T16:15:19.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-subjects-in-reactive-programming-bbdc8fed7b6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6gi30QcIoPkwcxpz5d4wkg.png
tags:
- name: JavaScript
  slug: javascript
- name: observables
  slug: observables
- name: Reactive Programming
  slug: reactive-programming
- name: RxJS
  slug: rxjs
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Dler Ari

  A Subject is a “special” type of observable that allows us to broadcast values to
  multiple subscribers. The cool thing about Subjects, is that it provides a real-time
  response.

  For instance, if we have a subject with 10 subscribers, whene...'
---

By Dler Ari

A Subject is a “special” type of observable that allows us to broadcast values to multiple subscribers. The cool thing about Subjects, is that it provides a real-time response.

For instance, if we have a subject with 10 subscribers, whenever we push values to the subject, we can see the value captured by each subscriber

This introduces a couple challenges; what if we push some values, and then subscribe, or vice-verse? Timing plays an important role, if we subscribe late, we won’t be able to access the values, similar to if someone enters a live-sport event on TV 30 minutes later.

Luckily, we have 4 types of Subjects that allows us to “time travel” in which we can access values even though we subscribe late or not.

#### Topics we’ll cover:

1. What is a Subject with a practical example
2. BehaviorSubject: Get the last message
3. ReplaySubject: Time travel
4. AsyncSubject: Once completed, get the last message

### 1. What is a Subject?

As mentioned, a Subject is nothing more like an observable with a few more characteristics. An observable is by definition an [invokable collection](https://rxjs.dev/guide/overview) that emits data once subscribed. Meanwhile, a Subject is where we control the state of “when to emit data” to multiple subscribers.

A Subject allows us to invoke methods like `.next()`, `.complete()` and `.error()` outside, while in an observable, we invoke these methods as callbacks.

```js
// Creating an Observable
const observable = new Observable((observer) => {
    observer.next(10);
    observer.next(5);
    observer.complete();
});

// Creating a Subject
const subject = new Subject();
subject.next(10);
subject.next(5);
subject.complete();
```

#### Practical example: Let’s build a simple chat group using a Subject

Let’s imagine we are building a simple chat app where people can post messages to the chat group. The first step is to create an instance of the Subject, and then assign it to a `chatGroup`.

```js
// Create subject "Observable"
const chatGroup = new Subject();
```

Now that our chat group (Subject) is created, the next thing to do is add messages. Let’s create a typical conversation between two friends.

```js
// Push values to the stream
chatGroup.next('David - Hi, which hot series do you recommend?');
chatGroup.next('Peter - Game of Thrones, Bodyguard or Narcos are few of the good ones');
chatGroup.next('David - Interesting, which one is the hottest?');
chatGroup.next('Peter - Game of Thrones!');
```

So far so good — now we have 4 messages posted in our chat group, so what happens if we subscribe? Or let’s say a new friend named John wants to join the conversation. Is he be able to see the old messages?

```js
// Print messages
chatGroup.subscribe((messages) => {
    console.log(messages)
})
```

Unfortunately not, John misses the conversation because he’s subscribes late. This is a perfect example of how reactive programming works — the idea of values passing over time, and thus, we must subscribe in the right time to access the values.

To further elaborate on the previous example, what if John enters in the middle of the conversation?

```js
// Push values to the stream
chatGroup.next('David - Hi, which hot series do you recommend?');
chatGroup.next('Peter - Game of Thrones, Bodyguard or Narcos are few of the good ones');

// John enters the conversation 
chatGroup.subscribe((messages) => {
    console.log(messages)
});

chatGroup.next('David - Interesting, which one is the hottest?');
chatGroup.next('Peter - Game of Thrones!');

// OUTPUT
// David - Interesting, which one is the hottest?
// Peter - Game of Thrones!
```

Once John subscribes, he sees the two last messages. The Subject is doing what it’s intended to do. But what if we want John to view all messages, or just the last one, or get notified when a new message is posted?

In general, these Subjects are mostly similar, but each one provides some extra functionality, let’s describe them one by one.

### 2. BehaviorSubject: Get last message

The BehaviorSubject is similar to a Subject except it requires an initial value as an argument to mark the starting point of the data stream. The reason is because when we subscribe, it returns the last message. This is similar concept when dealing with arrays; where we do `array.length-1` to get the latest value.

```js
import {BehaviorSubject } from "rxjs";

// Create a Subject
const chatGroup = new BehaviorSubject('Starting point');

// Push values to the data stream
chatGroup.next('David - Hi, which hot series do you recommend?');
chatGroup.next('Peter - Game of Thrones, Bodyguard or Narcos are few of the good ones');
chatGroup.next('David - Interesting, which one is the hottest?');
chatGroup.next('Peter - Game of Thrones!');

// John enters the conversation
chatGroup.subscribe((messages) => {
    console.log(messages)
})

// OUTPUT
// Peter - Game of Thrones!
```

### 3. ReplaySubject: Time travel

The ReplaySubject, as the name implies, once subscribed it broadcasts all messages, despite if we subscribed late or not. It’s like time travel, where we can access all the values that were broadcast.

```js

import { ReplaySubject } from "rxjs";

// Create a Subject
const chatGroup = new ReplaySubject();

// Push values to the data stream
chatGroup.next('David - Hi, which hot series do you recommend?');
chatGroup.next('Peter - Game of Thrones, Bodyguard or Narcos are few of the good ones');
chatGroup.next('David - Interesting, which one is the hottest?');
chatGroup.next('Peter - Game of Thrones!');

// John enters the conversation
chatGroup.subscribe((messages) => {
    console.log(messages)
})

// OUTPUT
// David - Hi, which hot series do you recommend?'
// Peter - Game of Thrones, Bodyguard or Narcos are few of the good ones'
// David - Interesting, which one is the hottest?'
// Peter - Game of Thrones!'
```

### 4. AsyncSubject: Once completed, get last message

The AsyncSubject is similar to BehaviorSubject in terms of emitting the last value once subscribed. The only difference is that it requires a `complete()` method to mark the stream as completed. Once that is done, the last value is emitted.

```js
import { AsyncSubject } from "rxjs";

// Create a Subject
const chatGroup = new AsyncSubject();

// Push values to the data stream
chatGroup.next('David - Hi, which hot series do you recommend?');
chatGroup.next('Peter - Game of Thrones, Bodyguard or Narcos are few of the good ones');
chatGroup.next('David - Interesting, which one is the hottest?');
chatGroup.next('Peter - Game of Thrones!');

chatGroup.complete(); // <-- Mark the stream as completed

// John enters the conversation
chatGroup.subscribe((messages) => {
    console.log(messages)
})

// OUTPUT
// Peter - Game of Thrones!'
```

### Summary

Back to our previous example with John, we can now decide if we want John to access the whole conversation (ReplaySubject), the last message (BehaviorSubject), or the last message once the conversation completes (AsyncSubject).

If you ever struggle to identify if a Subject is the right way to go, the article “[To Use a Subject or Not to Use a Subject](http://davesexton.com/blog/post/To-Use-Subject-Or-Not-To-Use-Subject.aspx)” by Dave Sixton describes when to use Subjects based on two criteria:

1. Only when one want to **convert** a cold Observable into a hot observable.
2. **Generate** a hot observable that passes data continuously.

In short, only creativity limits the potential use of reactive programming. There will be some scenarios where Observables do most of the heavy-lifting, but understanding what Subjects are, and what type of Subjects exists, will definitely improve your reactive programming skills.

If you are interested to learn more about the web-ecosystem, here are few articles I’ve written, enjoy.

* [A comparison between Angular and React](https://medium.freecodecamp.org/a-comparison-between-angular-and-react-and-their-core-languages-9de52f485a76)
* [A practical guide to ES6 modules](https://medium.freecodecamp.org/how-to-use-es6-modules-and-why-theyre-important-a9b20b480773)
* [How to perform HTTP requests using the Fetch API](http://A practical ES6 guide on how to perform HTTP requests using the Fetch API)
* [Important web concepts to learn](https://medium.freecodecamp.org/learn-these-core-javascript-concepts-in-just-a-few-minutes-f7a16f42c1b0?gi=6274e9c4d599)
* [Boost your skills with these JavaScript methods](https://medium.freecodecamp.org/7-javascript-methods-that-will-boost-your-skills-in-less-than-8-minutes-4cc4c3dca03f)
* [Create custom bash commands](https://codeburst.io/learn-how-to-create-custom-bash-commands-in-less-than-4-minutes-6d4ceadd9590)

You can find me on Medium where I publish on a weekly basis. Or you can follow me on [Twitter](http://twitter.com/dleroari), where I post relevant web development tips and tricks.

