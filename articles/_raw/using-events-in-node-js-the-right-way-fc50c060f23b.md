---
title: How to use events in Node.js the right way
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-03T17:01:06.000Z'
originalURL: https://freecodecamp.org/news/using-events-in-node-js-the-right-way-fc50c060f23b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_B5O6c-2DYQWOp0HV4hm7Q.png
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Usama Ashraf

  Before event-driven programming became popular, the standard way to communicate
  between different parts of an application was pretty straightforward: a component
  that wanted to send out a message to another one explicitly invoked a me...'
---

By Usama Ashraf

Before event-driven programming became popular, the standard way to communicate between different parts of an application was pretty straightforward: a component that wanted to send out a message to another one explicitly invoked a method on that component. But event-driven code is written to _react_ rather than be _called_.

#### The Benefits Of Eventing

This approach causes our components to be much **more decoupled**. As we continue to write an application, we identify events along the way. We fire them at the right time and attach one or more _event listeners_ to each one. **Extending functionality becomes much easier.** We can add on more listeners to a particular event. We are not tampering with the existing listeners or the part of the application where the event was fired from. What we’re talking about is the Observer pattern.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jAzlEy_JIYvhYRrrD-DcqA.jpeg)
_[https://www.dofactory.com/javascript/observer-design-pattern](https://www.dofactory.com/javascript/observer-design-pattern" rel="noopener" target="_blank" title=")_

#### Designing An Event-Driven Architecture

Identifying events is pretty important. We don’t want to end up having to remove/replace existing events from the system. This might force us to delete/modify any number of listeners that were attached to the event. The general principle I use is to _consider firing an event only when a unit of business logic finishes execution._

So say you want to send out a bunch of different emails after a user’s registration. Now, the registration process itself might involve many complicated steps, and queries. But from a business point of view, it is _one step._ And each of the emails to be sent out are individual steps as well. So it would make sense to fire an event as soon as registration finishes. We have multiple listeners attached to it, each responsible for sending out one type of email.

Node’s asynchronous, event-driven architecture has certain kinds of objects called “emitters.” They emit named events which cause functions called “listeners” to be invoked. All objects that emit events are instances of the [EventEmitter](https://nodejs.org/api/events.html#events_class_eventemitter) class. Using it, we can create our own events:

#### An Example

Let’s use the built-in [events](https://nodejs.org/api/events.html) module (which I encourage you to check out in detail) to gain access to `EventEmitter`.

This is the part of the application where our server receives an HTTP request, saves a new user and emits an event:

And a separate module where we attach a listener:

It’s a good practice to _separate policy from implementation._ In this case policy means which listeners are subscribed to which events. Implementation means the listeners themselves.

This separation allows for the listener to become re-usable too. It can be attached to other events that send out the same message (a user object). It’s also important to mention that _when multiple listeners are attached to a single event, they will be executed synchronously and in the order that they were attached_. Hence `someOtherListener` will run after `sendEmailOnRegistration` finishes execution.

However, if you want your listeners to run asynchronously you can simply wrap their implementations with `setImmediate` like this:

#### Keep Your Listeners Clean

Stick to the Single Responsibility Principle when writing listeners. One listener should do one thing only and do it well. Avoid, for instance, writing too many conditionals within a listener that decide what to do depending on the data (message) that was transmitted by the event. It would be much more appropriate to use different events in that case:

#### Detaching Listeners Explicitly When Necessary

In the previous example, our listeners were totally independent functions. But in cases where a listener is associated with an object (it’s a method), it has to be manually detached from the events it had subscribed to. Otherwise, the object will never be garbage-collected since a part of the object (the listener) will continue to be referenced by an external object (the emitter). Thus the possibility of a memory leak.

For example, if we’re building a chat application and we want the responsibility for showing a notification when a new message arrives in a chat room that a user has connected to should lie within that user object itself, we might do this:

When the user closes his/her tab or loses their internet connection for a while, naturally, we might want to fire a callback on the server-side that notifies the other users that one of them just went offline. At this point, of course, it doesn’t make any sense for `displayNewMessageNotification` to be invoked for the offline user. It will continue to be called on new messages unless we remove it explicitly. If we don’t, aside from the unnecessary call, the user object will also stay in memory indefinitely. So be sure to call `disconnectFromChatroom` in your server-side callback that executes whenever a user goes offline.

#### Beware

The loose coupling in event-driven architectures can also lead to increased complexity if we’re not careful. It can be difficult to keep track of dependencies in our system. Our application will become especially prone to this problem if we start emitting events from within listeners. This could possibly trigger chains of unexpected events.

