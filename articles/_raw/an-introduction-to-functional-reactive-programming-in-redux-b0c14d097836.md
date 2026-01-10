---
title: An introduction to functional Reactive programming in Redux
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-28T18:40:59.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-functional-reactive-programming-in-redux-b0c14d097836
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8qnkQscHUXopU2ZBwNhHrg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Redux
  slug: redux
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "By Bhuvan Malik\nLetss start off by getting the basic idea of what “Reactive\
  \ Programming” is:\n\nReactive Programming _is an asynchronous programming paradigm\
  \ concerned with data streams and the propagation of change.  \n- Wikipedia_\n\n\
  ReactiveX or Rx is ..."
---

By Bhuvan Malik

Letss start off by getting the basic idea of what “Reactive Programming” is:

> **_Reactive Programming_** _is an asynchronous [programming paradigm](https://en.wikipedia.org/wiki/Programming_paradigm) concerned with [data streams](https://en.wikipedia.org/wiki/Dataflow_programming) and the propagation of change._  
> _- Wikipedia_

[ReactiveX](http://reactivex.io/) or Rx is the most popular API for reactive programming. It’s built on the ideologies of the Observable Pattern, Iterator Pattern, and Functional Programming. Rx has libraries for different languages, but we will be using [RxJS](https://github.com/ReactiveX/rxjs).

#### Rx is based on **Observables**, **Observers,** and **Operators**

An Observer essentially **subscribes** to an Observable.

The Observable then emits streams of data which the Observer listens and reacts to, setting in motion a chain of operations on the data stream. The real power comes from Operators or “Reactive Extensions” (hence the term Rx)**.**

Operators allow you to transform, combine, manipulate, and work with the sequences of items emitted by Observables.

If you’re not familiar with Rx, you may have a hard time understanding and using [Redux-Observable](https://redux-observable.js.org/). So I suggest that you get your hands dirty with Rx first!

Now onto using RxJS with Redux.

### Redux-Observable

![Image](https://cdn-media-1.freecodecamp.org/images/6oEOGaUYU93i90xMzNA6GjY1lVaohtAjHKkR)

#### Redux-Observable is an RxJS based middleware for Redux

This is what Redux Docs have to say about middleware in Redux:

> _Middleware provides a third-party extension point between dispatching an action, and the moment it reaches the reducer._

Redux middleware can be used for logging, crash reporting, talking to an asynchronous API, routing, and more. Or we can say **side effects** in general.

#### So how does Redux-Observable do all that?

Through [Epics](https://redux-observable.js.org/docs/basics/Epics.html). Epics are the core primitive of Redux-Observable. An epic is just a simple function that takes in an action and then returns another action. **Action In → Action Out**. Actions are therefore treated as streams.

Every action dispatched in any component of React will pass through such functions (Epics) as a stream.

Let’s see what a simple Epic that takes in an `action` `'PING’` and returns a **new** `action` `'PONG’` looks like:

```
const pingEpic = action$ =>  action$.filter(action => action.type === 'PING')    .mapTo({ type: 'PONG' })
```

The `$` after `action` is used to indicate that these variables are referencing streams. So we have a stream of actions being passed into the Epic on which we have used the `filter` operator of RxJS.

This filter operator filters out all the actions which are not of the `type` `PING`! Therefore, the Epic `pingEpic` is only concerned with handling actions of the `type` `‘PING’`. Finally, this `action` `‘PING’` is mapped to a new `action` of the `type` `‘PONG’` satisfying the main rule of Epics: **Action In → Action Out**.

Since every epic is only concerned with a specific type of action, we have a special operator for `action$`(stream) to filter out unwanted actions from the stream. This operator is the `ofType()` operator.

Rewriting the previous Epic using `ofType` we get:

```
const pingEpic = action$ =>  action$.ofType('PING')  .mapTo({ type: 'PONG' })
```

If you want your epic to allow more than one type of action, the `ofType()` operator can take any number of arguments like so: `ofType(type1, type2, type3,...)`.

#### Getting Into The Specifics of How Epics Work

You may think that the action ‘PING’ simply comes in and gets consumed by this epic. That is not the case. There are two things to always remember:

1. Every action always goes to the reducer first
2. Only after that is that action received by the epic

Therefore, the Redux cycle works normally as it should.

The `action` `‘PING’` reaches the reducer first and is then received by the Epic, then changed to a new `action` `‘PONG’` which is dispatched to the reducer.

We can even access the store’s state inside an Epic because an Epic’s second argument is a light version of the Redux Store! See below:  
`const myEpic = (action$, store) =&`gt;   
We can just ca`ll store.getStat`e() and access the state inside Epics.

#### Operator Chaining

Between receiving an action and dispatching a new one, we can do all sorts of async side effects we want to, such as AJAX calls, web sockets, timers, and so on. This is done using the numerous **operators** provided by Rx.

> _These Rx operators allow you to compose asynchronous sequences together in a declarative manner with all the efficiency benefits of callbacks but without the drawbacks of nesting callback handlers that are typically associated with asynchronous systems._

We get the benefits of callbacks, without that notorious ‘callback hell’.

See how we can leverage the power of operators below.

#### A Common Use-Case

Assume that we want to search for a word with something like a dictionary API using text entered by the user in real-time. We’re basically dealing with storing (in the Redux store) and displaying the results from the API call. We would also like to debounce the API call so that the API is called within, say, 1 second of when the user stops typing.

This is how it’ll be done using Epic and RxJS operators:

```
const search = (action$, store) =>  action$.ofType('SEARCH')  .debounceTime(1000)  .mergeMap(action =>    ajax.getJSON(`https://someapi/words/${action.payload}`)     .map(payload => ({ type: 'SET_RESULTS', payload }))     .catch(payload => Observable.of({type: 'API_ERROR', payload}))  )
```

Too much to handle?! Don’t worry, let’s break that down.

The epic is getting a stream of actions all `oftype` `‘SEARCH’`. Since the user is continuously typing, the payload of every incoming action (`action.payload`) contains the updated search string.

The operator `debounceTime()` is used to filter out some of the actions in the stream except the last one. It basically passes an action through it only if 1 second has elapsed without it receiving another action or observable.

We then make the AJAX request, mapping the results to another action `'set_RESULTS'` which takes the response data `(payload)` to the reducer, which is the Action Out part.

Any API errors are caught using the `catch` operator. A new action is emitted with the error details and later displays a toaster with the error message.

Notice how the catch is inside the `mergeMap()` and after the AJAX request? This is because the `mergeMap()` creates a chain that is isolated. Otherwise the error would reach `ofType()` and will terminate our Epic. If that happens, the Epic will stop listening to any action in the future!

We can use traditional promises for AJAX requests as well. However, they have this inherent problem of not being able to get cancelled. So another important use case for using Epics is AJAX cancellation.

We use the `takeUntil` operator to handle this issue. This is done just like we used that `catch` operator inside `mergeMap` and after the AJAX request.

This is because `takeUntil` must stop the current AJAX request and not the entire Epic! Therefore, isolating operator chains is important here as well.

Debouncing, throttling, filtering, AJAX cancellation and others, are just the tip of the iceberg. We have a myriad of [operators](http://reactivex.io/documentation/operators.html) at our disposal, making difficult use-cases trivial to solve. Using these operators, you can get as creative as your imagination allows you to be! Functional Reactive Programming (FRP) is elegant in its own way.

My focus for this article was on the explanation part of FRP in Redux using Redux-Observable. For setting up Redux-Observable in React+Redux, refer to the [official docs](https://redux-observable.js.org/) — its very well documented, detailed, and easy-breezy.

Be sure to check out my other article on Redux which explores the best practice for creating reducers:

[**Reducing the Reducer Boilerplate With createReducer()**](https://medium.freecodecamp.org/reducing-the-reducer-boilerplate-with-createreducer-86c46a47f3e2)  
[_First, a quick recap of what reducers in Redux are:_medium.freecodecamp.org](https://medium.freecodecamp.org/reducing-the-reducer-boilerplate-with-createreducer-86c46a47f3e2)

Want to improve your JavaScript basics? Give these a read:

[**JavaScript ES6 Functions: The Good Parts**](https://medium.freecodecamp.org/es6-functions-9f61c72b1e86)  
[_ES6 offers some cool new functional features that make programming in JavaScript much more flexible. Let’s talk about…_medium.freecodecamp.org](https://medium.freecodecamp.org/es6-functions-9f61c72b1e86)[**A guide to JavaScript variable hoisting ? with let and const**](https://medium.freecodecamp.org/what-is-variable-hoisting-differentiating-between-var-let-and-const-in-es6-f1a70bb43d)  
[N_ew JavaScript developers often have a hard time understanding the unique behaviour of variable/function hoisting.m_edium.freecodecamp.org](https://medium.freecodecamp.org/what-is-variable-hoisting-differentiating-between-var-let-and-const-in-es6-f1a70bb43d) [**Function Hoisting & Hoisting Interview Questions**](https://medium.freecodecamp.org/function-hoisting-hoisting-interview-questions-b6f91dbc2be8)  
[_This is a part 2 for my previous article on Variable Hoisting titled “A guide to JavaScript variable hoisting ? with…m_edium.freecodecamp.org](https://medium.freecodecamp.org/function-hoisting-hoisting-interview-questions-b6f91dbc2be8)

Peace ✌️

