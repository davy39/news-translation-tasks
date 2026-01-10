---
title: An introduction to the Flux architectural pattern
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-31T18:23:03.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-the-flux-architectural-pattern-674ea74775c9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7qtRmuWoMmFyhpnyxoS3MA.png
tags:
- name: Flux
  slug: flux
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Cristian Salcescu

  Discover Functional JavaScript was named one of the best new Functional Programming
  books by BookAuthority!

  Flux is an architectural pattern proposed by Facebook for building SPAs. It suggests
  to split the application into the fo...'
---

By Cristian Salcescu

[**Discover Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE) was named one of the [**best new Functional Programming books by BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781)**!**

Flux is an architectural pattern proposed by Facebook for building SPAs. It suggests to split the application into the following parts:

* Stores
* Dispatcher
* Views
* Action / Action Creators

### Store

Store manages the state. It can store both domain state and user interface state.

Store and state are different concepts. State is the data value. Store is a behavior object that manages state through methods. In the case of managing books: the book list is the state and BookStore manages that list.

A store manages multiple objects. It is the single source of truth in regards to those specific objects. In an application there can be many stores. For example: BookStore, AuthorStore, UserStore.

There are no setter methods on the store. You can only request state change by passing an action to the dispatcher.

A store listens for all actions and decides on which of them to act. This usually means a `switch` statement. Once the store has made the state changes, it will emit a change event. The store is an event emitter.

Stores don’t take other stores as dependencies.

### Dispatcher

Dispatcher is a single object that broadcasts actions/events to all registered stores. Stores need to register for events when the application starts.

When an action comes in, it will pass that action to all registered stores.

### View

View is the user interface component. It is responsible for rendering the user interface and for handling the user interaction. Views are in a tree structure.

Views listen for store changes and re-render.

Views can be further split in Presentation and Container Views.

Presentation views don’t connect to dispatcher or stores. They communicate only through their own properties.

Container views are connected to stores and dispatcher. They listen for events from stores and provide the data for presentation components. They get the new data using the stores’ public getter methods and then pass that data down the views tree.

Container views dispatch actions in response to user iteration.

### Actions

An action is a plain object that contains all information necessary to do that action.

Actions have a `type` property identifying the action type.

As action objects move around the application, I suggest to make them immutable.

Actions may come from different places. They may come from views as a result of user interaction. They may come from other places like the initialization code, where data may be taken from a Web API and actions are fired to update the views. Action may come from a timer that requires screen updates.

### Action Creators

The practice is to encapsulate the code, creating actions in functions. These functions that create and dispatch actions are called action creators.

#### Web API Calls

When doing Web API calls to update the user interface, the Web API call will be followed by an action to update the store. When the store is updated it will emit a change event and as result the view that listens for that event will re-render.

Web API calls are made in action creators. We can extract out the code that does the API call in Web API Utils functions.

### Unidirectional data flow

Updating views flow in a single direction:

![Image](https://cdn-media-1.freecodecamp.org/images/B3swRnUORvq-CH8yZO-Pgy9ZiAmN5LPlgMM3)

Views do not modify the data they received. They listen for changes of this data, create actions with new values, but do not update the data.

Stores, views and any other action can’t change the state in (other) stores directly. They must send an action through the dispatcher

The data flow is shorter in store reads than in writes.The data flow in store writes differs between asynchronous and synchronous actions.

Store Reads

![Image](https://cdn-media-1.freecodecamp.org/images/toNPHVZBnlFDPKHyp142thO9y7f6tQzREs7T)

Store Writes in synchronous actions

![Image](https://cdn-media-1.freecodecamp.org/images/JQ2bHtD7C0rtKjNAHAYSD7TdPbRnV04WWyBg)

Store Writes in asynchronous actions

![Image](https://cdn-media-1.freecodecamp.org/images/U857Xuskoy-w6aGMC--FfAyIAUEyMj13JETi)

### Pros

Flux architecture is better in an application where views don’t map directly to domain stores. To put in a different way, when views can create actions that will update many stores and stores can trigger changes that will update many views.

Actions can be persisted and then replayed.

### Cons

Flux can add unnecessary complexity to an application where each view maps to one store. In this kind of application a separation between view and store is enough.

Take a look for example at [How to create a three layer application with React](https://medium.freecodecamp.org/how-to-create-a-three-layer-application-with-react-8621741baca0).

### Conclusion

Stores manage state. They change state only by listening for actions. Stores notify views to update.

Views render the user interface and handle user interaction. Container views listen for store changes.

The dispatcher broadcasts actions to all registered stores.

Actions are plain objects.

[**Discover Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE&source=post_page---------------------------) was named one of the [**best new Functional Programming books by BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781&source=post_page---------------------------)**!**

**For more on applying functional programming techniques in React take a look at** [**Functional React**](https://read.amazon.com/kp/embed?asin=B07S1NLFTS&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_Pko5CbA30383Y)**.**

Learn **functional React**, in a project-based way, with [**Functional Architecture with React and Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2)**.**

[Follow on Twitter](https://twitter.com/cristi_salcescu)

