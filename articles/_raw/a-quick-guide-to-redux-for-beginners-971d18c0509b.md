---
title: A quick guide to Redux for beginners
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2018-02-02T11:23:43.000Z'
originalURL: https://freecodecamp.org/news/a-quick-guide-to-redux-for-beginners-971d18c0509b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*-E5k6l1Bbi5U9BHSLAk4dg.jpeg
tags:
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Redux
  slug: redux
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'Interested in learning JavaScript? Get my ebook at jshandbook.com


  Redux is a state manager that’s usually used along with React. It’s not tied to
  that library, and can be used with other technologies as well. But we’ll stick to
  React for the sake of...'
---

> Interested in learning JavaScript? Get my ebook at [jshandbook.com](https://jshandbook.com/)

Redux is a state manager that’s usually used along with React. It’s not tied to that library, and can be used with other technologies as well. But we’ll stick to React for the sake of this article.

React has its own way to manage state, and you can read my introduction to managing state in React in my [React Beginner’s Guide](https://flaviocopes.com/react-beginners-guide/).

What I didn’t mention in that article is that the approach I discussed **does not scale**.

Moving the state up in the tree works in simple cases, but in a complex app you might find yourself moving almost all the state up and down using props. A better approach would be to use an **external global store**.

Redux is a way to manage an application state.

There are a few concepts to grasp, but once you’ve got them, Redux is a very simple approach to the problem.

Just to note again: Redux is very popular with React applications, but it’s in no way unique to React. There are bindings for nearly every popular framework. That said, I’ll share some examples using React since it’s so common.

### When should you use Redux?

Redux is ideal for medium to big apps. You should only use it when you have trouble managing the state with React’s default state management (or whatever other library you use).

Simple apps should not need it at all (and there’s nothing wrong with simple apps).

### Immutable State Tree

In Redux, the whole state of the application is represented by **one** JavaScript object, called **state** or **state tree**.

We call it **immutable state tree** because it is read only: it can’t be changed directly.

It can only be changed by dispatching an **Action**.

### Actions

An **Action** is **a JavaScript object that describes a change in a minimalistic way** (just with the information needed):

```
{   type: 'CLICKED_SIDEBAR' } 
```

```
// e.g. with more data {   type: 'SELECTED_USER',   userId: 232 }
```

The only requirement of an action object is having a `type` property, whose value is usually a string.

### Actions types should be constants

In a simple app, an action type can be defined as a string (as I did in the example in the previous article).

When the app grows, it is best to use constants:

```
const ADD_ITEM = 'ADD_ITEM' const action = { type: ADD_ITEM, title: 'Third item' }
```

and to separate actions in their own files, and import them:

```
import { ADD_ITEM, REMOVE_ITEM } from './actions'
```

### Action creators

**Actions Creators** are functions that create actions.

```
function addItem(t) {   return {     type: ADD_ITEM,     title: t   } }
```

You usually run action creators in combination with triggering the dispatcher:

```
dispatch(addItem('Milk'))
```

or by defining an action dispatcher function:

```
const dispatchAddItem = i => dispatch(addItem(i)) dispatchAddItem('Milk')
```

### Reducers

When an action is fired, something must happen and the state of the application must change.

This is the job of **reducers**.

### What is a reducer

A **reducer** is a **pure function** that calculates the next state tree based on the previous state tree and the action dispatched.

```
(currentState, action) => newState
```

A pure function takes an input and returns an output without changing the input or anything else. Thus, a reducer returns a completely new state tree object that replaces the previous one.

### What a reducer should not do

A reducer should be a pure function, so it should **not**:

* mutate its arguments
* mutate the state — it should instead create a new one with `Object.assign({}, ...)`
* generate side-effects (no API calls changing anything)
* call non-pure functions, which are functions that change their output based on factors other than their input (e.g. `Date.now()` or `Math.random()`)

There is no reinforcement, but you should stick to the rules.

### Multiple reducers

Since the state of a complex app could be really wide, there is not a single reducer, but many reducers for any kind of action.

### A simulation of a reducer

At its core, Redux can be simplified with this model:

#### The state

```
{   list: [     { title: "First item" },     { title: "Second item" },   ],   title: 'Grocieries list' }
```

#### A list of actions

```
{ type: 'ADD_ITEM', title: 'Third item' } { type: 'REMOVE_ITEM', index: 1 } { type: 'CHANGE_LIST_TITLE', title: 'Road trip list' }
```

#### A reducer for every part of the state

```
const title = (state = '', action) => {  if (action.type === 'CHANGE_LIST_TITLE') {     return action.title   } else {     return state   } } 
```

```
const list = (state = [], action) => {   switch (action.type) {     case 'ADD_ITEM':       return state.concat([{ title: action.title }])     case 'REMOVE_ITEM':       return state.map((item, index) =>         action.index === index           ? { title: item.title }           : item     default:       return state   } }
```

#### A reducer for the whole state

```
const listManager = (state = {}, action) => {   return {     title: title(state.title, action),     list: list(state.list, action),   } }
```

### The Store

The **Store** is an object that:

* **holds the state** of the app
* **exposes the state** via `getState()`
* allows you to **update the state** via `dispatch()`
* allows you to (un)register as a **state change listener** using `subscribe()`

A store is **unique** in the app.

Here is how a store for the listManager app is created:

```
import { createStore } from 'redux' import listManager from './reducers' let store = createStore(listManager)
```

### Can I initialize the store with server-side data?

Sure, **just pass a starting state**:

```
let store = createStore(listManager, preexistingState)
```

### Getting the state

```
store.getState()
```

### Update the state

```
store.dispatch(addItem('Something'))
```

### Listen to state changes

```
const unsubscribe = store.subscribe(() =>   const newState = store.getState() ) 
```

```
unsubscribe()
```

### Data Flow

Data flow in Redux is always **unidirectional**.

You call `dispatch()` on the Store, passing an Action.

The Store takes care of passing the Action to the Reducer, generating the next State.

The Store updates the State and alerts all the Listeners.

> Interested in learning JavaScript? Get my ebook at [jshandbook.com](https://jshandbook.com/)

