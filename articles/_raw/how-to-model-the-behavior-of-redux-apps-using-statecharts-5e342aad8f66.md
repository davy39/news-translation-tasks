---
title: How to model the behavior of Redux apps using statecharts
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-05T17:40:33.000Z'
originalURL: https://freecodecamp.org/news/how-to-model-the-behavior-of-redux-apps-using-statecharts-5e342aad8f66
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_vb_56pz-h3xAB1E5uooqA.jpeg
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
seo_desc: 'By Luca Matteis

  Our app, whether we like it or not, will be in a particular state at any given point
  in time. As we code User Interfaces (UI), we describe these states using data (a
  Redux store for instance), but we never give each state a formal nam...'
---

By Luca Matteis

Our app, whether we like it or not, will be in a particular state at any given point in time. As we code User Interfaces (UI), we describe these states using data (a Redux store for instance), but we never give each state a formal name.

More importantly, there are events that should not be triggered when in a particular state.

It turns out that this idea of describing states and the events that transition from one state into another is a well studied concept. [Statecharts](http://www.inf.ed.ac.uk/teaching/courses/seoc/2005_2006/resources/statecharts.pdf), for instance, provide a visual formalism for describing the behavior of reactive applications, such as user interfaces.

In this article, I will discuss how the behavior of Redux apps can be decoupled from components, containers, or middlewares — places where we usually keep such logic — and can be contained and described entirely using a statechart. This allows for much easier refactoring and visualization of our application’s behavior.

### Redux and statecharts

[Redux](https://redux.js.org/) is quite simple. We have a UI component that triggers an event. We then `dispatch` an action when this event occurs. A reducer uses this action to update the store. Finally, our component feeds directly from the updates to the store:

```
// our UI componentfunction Counter({ currentCount, onPlusClick }) {  return <>    <button onClick={onPlusClick}>plus</button>    {currentCount}  <>}
```

```
// let's connect the component to reduxconnect(  state => ({ currentCount: state.currentCount }),  dispatch => ({     onPlusClick: () => dispatch({ type: INCREMENT })  }))(Counter)
```

```
// handle the INCREMENT update using a reducerfunction currentCountReducer(state = 0, action) {  switch(action.type) {    case INCREMENT:      return state + 1;    default:      return state;  }}
```

This is pretty much all there is to Redux.

![Image](https://cdn-media-1.freecodecamp.org/images/j8cLfILp7OZ9z99gm6-JM6m5FGciCZD3bBJh)

To introduce statecharts, instead of mapping our event directly to the updating action, we map it to a generic action that doesn’t update any data (no reducer handles it):

```
// currently we are mapping our event to the update:// onPlusClick -> INCREMENT// instead, we dispatch a generic event which is not an update:// onPlusClick -> CLICKED_PLUS // this way we decouple our container from knowing // which update will happen.// the statechart will take care of triggering the correct update.
```

```
connect(  state => ({ currentCount: state.currentCount }),  dispatch => ({     onPlusClick: () => dispatch({ type: CLICKED_PLUS })  }))(Counter)
```

No reducer handles `CLICKED_PLUS` so instead we let a statechart handle it:

```
const statechart = {  initial: 'Init',  states: {    Init: {      on: { CLICKED_PLUS: 'Increment' }    },    Increment: {      onEntry: INCREMENT, // <- update when we enter this state      on: { CLICKED_PLUS: 'Increment' }    }  }}
```

The statechart will handle the events it receives similar to the way a reducer would, but only if it’s in a state that allows for such an event to happen. **Events in this context are Redux actions that don’t update the store**.

In the above-mentioned example, we start off by being in the `Init` state. When the `CLICKED_PLUS` event occurs, we transition to the `Increment` state which has an `onEntry` field. This makes the statechart dispatch an`INCREMENT` action — this time handled by a reducer, which updates the store.

You might be asking, why did we decouple the container from knowing about the update? We did it so that all of the behavior concerning when the update needs to occur is contained within the statechart JSON structure. Which means it can also be visualized:

![Image](https://cdn-media-1.freecodecamp.org/images/f20MvpyzWylXFxR739RS4UVAxLVG1pKslHL8)

This can lead to improvements in the behavior of our app by simply changing the JSON description of the statechart. Let’s improve our design by grouping the two`CLICKED_PLUS` transitions into one, using the concept of [hierarchical states](https://statecharts.github.io/glossary/compound-state.html):

![Image](https://cdn-media-1.freecodecamp.org/images/0XUooK1P2XVwPZHIXAq0AdctW5wcBzCg6PMx)

To make this happen, we only had to change our statechart definition. Our UI components and reducers remain untouched.

```
{  initial: 'Init',  states: {    Init: {      on: { CLICKED_PLUS: 'Init.Increment' },      states: {        Increment: {          onEntry: INCREMENT        }      }    }  }}
```

### Async side-effects

Let’s imagine that when a `<FetchDataButton` /> is clicked we want to start an HTTP request. Here’s how we would currently do it in Redux without statecharts:

```
connect(  null,  dispatch => ({     onFetchDataClick: () => dispatch({ type: FETCH_DATA_CLICKED })  }))(FetchDataButton)
```

Then we would probably have an epic to handle such action. Below we are using [redux-observable](https://redux-observable.js.org/), but redux-saga or redux-thunk can be used as well:

```
function handleFetchDataClicked(action$, store) {  return action$.ofType('FETCH_DATA_CLICKED')    .mergeMap(action =>      ajax('http://foo.bar')        .mapTo({ type: 'FETCH_DATA_SUCCESS' })        .takeUntil(action$.ofType('FETCH_DATA_CANCEL'))    )}
```

Even though we decoupled the container from the side-effect (the container is simply telling the epic “hey, the fetch data button was clicked”), we still have the problem that the HTTP request is triggered no matter the state we’re in.

What if we’re in a state where `FETCH_DATA_CLICKED` should not trigger an HTTP request?

This case can easily be handled by statecharts. When `FETCH_DATA_CLICKED` happens, we transition to a `FetchingData` state. Only when entering this state (`onEntry`) does the `FETCH_DATA_REQUEST` action get dispatched:

```
{  initial: 'Init',  states: {    Init: {      on: {        FETCH_DATA_CLICKED: 'FetchingData',      },      initial: 'NoData',      states: {        ShowData: {},        Error: {},        NoData: {}      }    },    FetchingData: {      on: {        FETCH_DATA_SUCCESS: 'Init.ShowData',        FETCH_DATA_FAILURE: 'Init.Error',        CLICKED_CANCEL: 'Init.NoData',      },      onEntry: 'FETCH_DATA_REQUEST',      onExit: 'FETCH_DATA_CANCEL',    },  }}
```

Then we change our epic to react based on the newly added `FETCH_DATA_REQUEST` action instead:

```
function handleFetchDataRequest(action$, store) {  // handling FETCH_DATA_REQUEST rather than FETCH_DATA_CLICKED  return action$.ofType('FETCH_DATA_REQUEST')    .mergeMap(action =>      ajax('http://foo.bar')        .mapTo({ type: 'FETCH_DATA_SUCCESS' })        .takeUntil(action$.ofType('FETCH_DATA_CANCEL'))    )}
```

This way the request will be triggered only when we’re in the `FetchingData` state.

Again, by doing so, we pushed all of the behavior inside the JSON statechart, making refactoring easy and allowing us to visualize something that would’ve otherwise remained hidden in code:

![Image](https://cdn-media-1.freecodecamp.org/images/VQAnmHywghmtUrY0I241qgxsOPqyowmMesY5)

An interesting property of this particular design is that when we exit the `FetchingData` state, the `FETCH_DATA_CANCEL` action is dispatched. We can dispatch actions not only when entering states, but also when exiting them. As defined in our epic, this will cause the HTTP request to abort.

It’s important to note that I added this particular HTTP-abort behavior only after looking at the resulting statechart visualization. By simply glancing at the diagram, it was apparent that the HTTP request should’ve been cleaned up when exiting `FetchingData`. This might have not been so apparent without such visual representation.

By now, we can gather the intuition that statecharts control our store updates. We learn which side-effects need to happen and when they need to happen, based on the current state we’re in.

**The main insight here is that our reducers and epics will always react based on the output actions of our statechart, rather than our UI.**

In fact a statechart can be implemented as a stateful event-emitter: you tell it what happened (trigger an event), and, by remembering the last state you were in, it tells you what to do (actions).

![Image](https://cdn-media-1.freecodecamp.org/images/tTa5yNmBDRIpuTDoyuFprSRWvA1ZnJUngIH8)

### Problems statecharts help solve

As UI developers, our job is to bring static images to life. This process has several problems:

* **When we convert static images into code we lose the high-level understanding of our app** — as our app grows, understanding which section of code is responsible for each image becomes increasingly difficult.
* **Not all questions can be answered using a set of images** — What happens when the user clicks the button repeatedly? What if the user wants to cancel the request while it’s in-flight?
* **Events are scattered across our code and have unpredictable effects** — When the user clicks a button, what happens exactly? We need a better abstraction that helps us understand the repercussions of firing events.
* **Lots of `isFetching`, `isShowing`, `isDisabled` variables** — We need to keep track of everything that changes in our UI.

Statecharts help solve these problems by providing a strict **visual formalism** of the behavior of our app. Drawing a statechart allows us to have a high-level understanding of our app which lets us answer questions using visual clues.

![Image](https://cdn-media-1.freecodecamp.org/images/6WmId-UGRupVjl2O5T923hsdkBIvf7Af2KZj)

All the states of an app are explored during this process and events are explicitly labelled, allowing us to predict what is going to happen after any given event.

Furthermore, a statechart can be constructed directly from designers’ mockups, allowing non-engineers to also understand what is happening without having to dig into actual code.

### Learn more

As a concrete example of this, I’ve built [redux-statecharts](https://github.com/lmatteis/redux-statecharts), a Redux middleware that can be used as shown in the earlier examples. It uses the [xstate](https://github.com/davidkpiano/xstate) library — a pure function for transitioning a statechart.

If you’d like to learn more about statecharts, here is a great resource: [https://statecharts.github.io/](https://statecharts.github.io/)

Also check out my presentation on the subject: [Are statecharts the next big UI paradigm?](https://www.slideshare.net/lmatteis/are-statecharts-the-next-big-ui-paradigm)

