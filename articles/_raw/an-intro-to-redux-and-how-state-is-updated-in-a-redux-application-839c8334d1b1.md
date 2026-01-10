---
title: An intro to Redux and how state is updated in a Redux application
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-07T16:24:19.000Z'
originalURL: https://freecodecamp.org/news/an-intro-to-redux-and-how-state-is-updated-in-a-redux-application-839c8334d1b1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*VLQNO9Apn9qfm6BPYXG8TA.png
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Redux
  slug: redux
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Syeda Aimen Batool

  I started learning Redux a few days back and it was an overwhelming concept for
  me at the start. After polishing my skills in ReactJS by making a personal book
  reading application, I headed towards Redux to learn more about it.

  ...'
---

By Syeda Aimen Batool

I started learning Redux a few days back and it was an overwhelming concept for me at the start. After polishing my skills in ReactJS by making a [personal book reading application](https://github.com/aimenbatool/my-reads), I headed towards Redux to learn more about it.

Today, I’m going to share a few core Redux concepts without using any view library (React or Angular). This is a kind of a personal note for future reference but it can help others as well.

Let’s dig in together!

### What is Redux?

Redux is an open-source library to improve the predictability of the state in a JavaScript application. It is an independent library. It is commonly used with other libraries like React and Angular for better state management of the application. Redux was created by Dan Abramov in 2015 to handle complex state management in an efficient way.

When an application grows larger it becomes harder to manage the state and debug for issues. It becomes a challenge to track when and where the state is changed and where the changes need to be reflected. Sometimes a user input triggers some API call which updates some model. That model in turn updates some state or maybe the other model and so on.

In such a situation it becomes grinding to track the state changes. It happens mainly because there is no defined rule to update a state and state can be changed from anywhere inside the application.

Redux tries to solve this issue by providing a few simple rules to update the state to keep it predictable. Those rules are the building blocks of Redux.

### Redux Store:

As we discussed earlier, the main purpose of Redux is to provide predictable state management in our applications. Redux achieves this by having a single source of truth, that is a **single state tree**. The state tree is a simple JavaScript object which holds the whole state of our application. There are only a few ways to interact with the state. And this makes it easy for us to debug or track our state.

We now have only one main state which occupies the whole state of the application located at a single location. Any changes made into the state tree are reflected in the whole application because this is the only source of data for the app. And, this is the first fundamental principle of Redux.

#### Rule #1 — [Single source of truth](https://redux.js.org/introduction/three-principles#single-source-of-truth)

> The state of your whole application is stored in an object tree within a single store. — Official docs

The ways you can interact with a state tree are:

* Getting the state
* Listening to the changes in the state
* Updating the state

A **store** is a single unit that holds the **state tree** and the **methods** to interact with the state tree. There is no other way to interact with a state inside the store except through these given methods.

![Image](https://cdn-media-1.freecodecamp.org/images/cDBhHN7x5f-p6JRrZ-1ekpbDx7s0aW4j3jUr)

Let’s talk about the methods a store gives us to interact with the state.

* getState() — Returns the current state of the application.
* dispatch(action) — The only way to update a state is by dispatching an action and `dispatch(action)` serves the purpose. We will talk more in detail in a bit.
* subscribe(listener) — The purpose of this method is to listen for the state changes. Every time a state is changed, it will be called and will return the updated state.
* replaceReducer(nextReducer) — Replaces the reducer currently used by the store to calculate the state.

Now when we have a store which contains a state tree and a few ways to interact with the state, how can we update application state?

### Updating state in the application:

_The only way to update a state is to dispatch an action. This is the 2nd rule._

#### Rule #2 — [State is read-only](https://redux.js.org/introduction/three-principles#state-is-read-only)

An action is a plain JavaScript object to keep track of the specific event taking place in the application. What makes it special is a ‘type’ property which is a necessary part of it.

```
{  type: "ADD_BOOK_TO_THE_CART"}
```

The main purpose of this property is to let Redux know about the event taking place. This type should be descriptive about the action. Along with the ‘type’ property, it can have other information about the event taking place.

Actions can have as much information as you want. It is a good practice to provide less and necessary information — preferably an id or any unique identifier wherever possible.

Here we have an action to add a book to the cart.

Once we define our action we pass it to the dispatcher. **store.dispatch()** is a function provided by the library which accepts an action to perform an action against the state. Redux restricts updating the state to this method only.

This strict way of updating the state ensures that the state can not be changed directly either by view or any network callback. The only way to update a state is by defining the action and then dispatching it. Remember that actions are plain JavaScript objects. Actions can be logged, serialized, and replayed for debugging purposes.

We now have a store, a state, and an action in our app to perform some tasks against the state. Now we need a way to use these actions to actually do the update. This can be done by using a pure function and this is rule #3.

![Image](https://cdn-media-1.freecodecamp.org/images/h4w-r3zcxAOODzC-u5TKDip1joPotFfNCzVx)

#### Rule#3 — [Changes are made with pure functions](https://redux.js.org/introduction/three-principles#state-is-read-only)

Magic happens here. We need a simple pure function, which, as a parameter, takes the current state of the application and an action to perform on the state, and then returns the updated state. These functions are called reducers.

These are called reducers because they take the collection of values, reduce it to an updated state and then return it. Since reducers are pure functions they do not mutate the original state. Instead, they return the updated state in a new object. Our application can have one or more than one reducer. Each reducer can have a relevant state to perform specific tasks.

Since reducers are pure functions, they should have the following attributes:

* Given the same input, it should return the same output every time — No mutation is allowed.
* No side effects — No API call data change from an external source.

#### The process.

If we connect the dots, Redux is a library which has a store that contains a state tree and a few methods to interact with the state. The only way to update a state inside a store is to dispatch an action and define a reducer function to perform tasks based on the given actions. Once dispatched, the action goes inside the reducer functions which performs the tasks and return the updated state to the store. This is what Redux is all about.

![Image](https://cdn-media-1.freecodecamp.org/images/MNhhFTlpazu2H0YgQ7D7BhtZ7SYfdI4xA5Gk)
_State update flow in Redux_

### What have we learned so far?

Let’s summarize what we have learned so far to connect the dots.

* [Redux](https://redux.js.org/introduction/getting-started#getting-started-with-redux) — An opensource predictable state container
* State Tree — A plain JavaScript object which contains whole application state
* Three ways to interact with a state (the only ways):  
[**Store**](https://redux.js.org/basics/store#store) — A single unit which contains state tree & methods to interact with the state tree  
**Actions** — Plan Javascript objects to describe the action taking place  
**Reducers** — Pure Javascript functions to take current state and an action to return a new state

Since Redux is an independent library which can be used with React, Angular or any other library, I avoided making a sample application with any of these view libraries. Instead, I focused on the core Redux concepts only.

Redux can be overwhelming at first and if you are a newbie or junior developer it can give you a tough time. But consistency and a positive attitude is the key to success. If you are struggling to survive as a junior developer and looking for some motivation, you can read how [I struggled to overcome the challenges I faced as a junior dev.](https://medium.freecodecamp.org/how-im-working-to-overcome-my-struggles-as-a-junior-developer-a6ab18ac29b2)

Say Hi [@aimenbatool.](https://twitter.com/AimenBatool)

