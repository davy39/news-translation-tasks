---
title: How to Use Redux for Application-Wide State Management
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-12-02T15:47:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-redux-for-application-wide-state-management
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/React-redux-2.png
tags:
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
- name: Redux
  slug: redux
seo_title: null
seo_desc: 'By Prajwal Kulkarni

  Let''s face it – state management across multiple components isn''t easy.

  Sometimes we might set up the state or logic handling properly, but fail to consume
  the states. Or we might get everything working, but clutter up the codebas...'
---

By Prajwal Kulkarni

Let's face it – state management across multiple components isn't easy.

Sometimes we might set up the state or logic handling properly, but fail to consume the states. Or we might get everything working, but clutter up the codebase in the process, making it hard to read, adapt, and extend.  

The ability to have a single source of truth (a single store) is what gives Redux an upper hand over the traditional Context API.

So, without any further ado, let's see how we can make the best use of Redux for application-wide state management by writing cleaner and more optimized code.

## Before We Start

This article mainly looks at different ways to improve an existing Redux store. So you'll need to know the basics of Redux to get through it, such as setting up reducers, the Redux store, and dispatching actions.

If you need to brush up on Redux, check out these helpful guides:

* [Redux for Beginners](https://www.freecodecamp.org/news/redux-for-beginners/)
* [The Brain-friendly Guide to Learning Redux](https://www.freecodecamp.org/news/redux-for-beginners-the-brain-friendly-guide-to-redux/)

Already know the basics of Redux and have a Redux store you want to improve? Good.

Here's what we'll cover in this article:

* A quick recap on how to use the Redux store
* How to use the Redux Toolkit library by creating a Redux store for an e-commerce application. Note: we won't build the entire application, but just the state management part of it
* How to handle asynchronous code outside of reduces and components by using action creators

And with that, let's get started.

## A Quick Redux Store Recap

Before looking at how we can improve our Redux code, let's have a brief look at how we've been using Redux up to this point.

Here's a basic example of a Redux store. It's for a simple counter application that can increment and decrement the count on button clicks, and the state of the counter is managed and handled by Redux:

```javascript
import { createStore } from 'redux'

const initialState = {
  counter: 0,
}

const reducer = (state = initialState, action) => { // Reducer function
  switch (action.type) {
    case 'INCREMENT':
      return { ...state, counter: state.counter + 1 }
    case 'DECREMENT':
      return { ...state, counter: state.counter - 1 }
    default:
      return state
  }
}

const store = createStore(reducer) // redux-store

export default store

```

```javascript
import { useDispatch, useSelector } from 'react-redux'

export default function Component(props) {
  const dispatch = useDispatch()
  const counter = useSelector((state) => state.counter)

  const incrementHandler = () => {
    dispatch({ type: 'INCREMENT' })
  }
  const decrementHandler = () => {
    dispatch({ type: 'DECREMENT' })
  }

  return (
    <div>
      <h1>Counter:{counter}</h1>
      <button onClick={incrementHandler}>Increment</button>
      <button onClick={decrementHandler}>Decrement</button>
    </div>
  )
}

```

This is a very simple example that you could create just using state hooks. But it serves as a good overview of how we'd typically use Redux.

The Redux store above is perfectly fine if there aren't many different types of logic that need to be handled or dispatched.

Also, note that I used `const initialState` instead of `var` or `let` even though we are updating the state because of the property of immutability. That is, we aren't really mutating the existing state, but instead are reconstructing a new state altogether with the updated values.

This is fine. But what if the complexity of the application grows and requires us to perform multiple state and logic handling?

That's exactly what we'll cover in this guide.

## How to Create a Redux Store With Redux Toolkit

Throughout the rest of the article, let's consider how to manage state across an e-commerce application. In an e-commerce app, we would want to track and broadcast multiple states across various components.

As a rule of thumb, it is always good to have a rough idea of how we'll implement a design prior to getting our hands dirty.

When we think of an e-commerce application, the possible significant states are likely the following:

1. Authentication
2. Cart tracking
3. Watchlist

We can divide the state handling logic and the state into different modules, and then combine it all into a single store.

For this, we'll use Redux Toolkit.

Redux Toolkit is a third-party library like Redux, created and maintained by the Redux team.

You might be wondering why the Redux team created Redux Toolkit in the first place. The answer is right at the beginning of the [documentation](https://redux-toolkit.js.org/introduction/getting-started):

> The Redux Toolkit package is intended to be the standard way to write Redux logic. It was originally created to help address three common concerns about Redux:  
>   
> - "Configuring a Redux store is too complicated"  
> - "I have to add a lot of packages to get Redux to do anything useful"  
> - "Redux requires too much boilerplate code"

All-in-all, the whole point of using Redux Toolkit is to make using Redux easier and more efficient.

### How to Install Redux Toolkit

You can install Redux Toolkit either with `npm` or `yarn` like this:

* `npm install @reduxjs/toolkit`
* `yard add @reduxjs/toolkit`

## How to Use Redux Toolkit

The first stop when creating a Redux store is to set up state handling.

Instead of using reducers, we'll use `createSlice` which is provided by Redux Toolkit.

`createSlice` accepts 3 mandatory arguments, which are:

1. **name**: the name of the slice
2. **initialState**: the initial state of the slice (This is like the initial state of a reducer)
3. **reducers**: functions that affect the states (actions)

A slice, in brief, is like a modularized bundler of states and their actions.

Let's begin by creating a slice for authentication and its related actions:

```
const authSlice = createSlice({
  name: 'Auth', // Could name it anything
  initialState: {
    isLoggedIn: false,
  },
  reducers: {
    login: (state) => {
      state.isLoggedIn = true
    },
    logout: (state) => {
      state.isLoggedIn = false
    },
  },
})

```

As you can see, the slice above is dedicated to user authentication. `initialState` is an object that contains different initial state values, and the states that the reducers need to act upon. The functions in reducers are like regular reducers that accept state and action as arguments. 

One noticeable catch in the above snippet is how we're are dealing with updating the state with `state.isLoggedIn = true`. This is clearly mutating the state, violating the property of immutability.

Or, is it?

Let's understand what's happening under the hood before jumping to conclusions.

On the surface it seems like we're mutating the existing state. But mutating the existing state wouldn't trigger the broadcasting of updated value(s) to the subscribers.

So when we use mutating syntax in the reduces, `createSlice` uses a library called [Immer](https://redux-toolkit.js.org/usage/immer-reducers) internally. This library draws the difference in the existing and the updated state, and reconstructs a new object with an updated value.

This means that, when we mutate the state, Immer takes care of building a new object and conforming to the property of immutability, making it easier for us to write code.

Now, let's write the slices for the other states:

```javascript
const cartSlice = createSlice({
  name: 'Cart',
  initialState: {
    cart: [],
    qty: 0,
    total: 0,
  },
  reducers: {
    addItem: (state, action) => {
      state.cart.push(action.payload.cartItem)
      state.qty += action.payload.cartItem.qty
      state.total += action.payload.cartItem.price * action.payload.cartItem.qty
    },
    removeItem: (state, action) => {
      const itemIndex = state.cart.findIndex(
        (obj) => obj.id === action.payload.id
      )
      if (itemIndex !== -1 && state.cart[itemIndex].qty >= 1) {
        state.cart[itemIndex].qty -= 1
      }
    }
  }
})

```

The major part here is the logic related to adding and removing items from the cart.

We follow a similar logic for a watchlist, but without the total quantity and total cost:

```
const watchlistSlice = createSlice({
  name: 'Watchlist',
  initialState: {
    watchlist: [],
  },
  reducers: {
    addItem: (state, action) => {
      state.watchlist.push(action.payload.watchlistItem)
    },
    removeItem: (state, action) => {
      state.watchlist.filter((item) => item.id !== action.payload.id)
    }
  }
})

```

Notice how the action item is accessed via the payload property, and not directly.

This is because the Redux Toolkit adds the `payload` property on actions by default. `payload` is an object which can further contain other nested objects, or simple key-value pairs. It basically holds the arguments passed to the action dispatcher.

Now you might be asking yourself, how are we actually going to dispatch the action(s)?

Prior to using Redux Toolkit, we used to perform actions based on the action `type`. Then depending upon the `type` we would perform different operations.

But here we aren't using any `type` property, because we'll be exporting the reducer functions as actions, which could then be invoked within the dispatcher.

Reducer functions can by exported as actions by calling the `actions` property on the created slice:

`export const authActions = authSlice.actions`

`export const cartActions = cartSlice.actions`

`export const wathclistActions = watchlistSlice.actions`

All the slices here are not directly related to each other, so it's safe and also good practice to have them in separate files.

If you add slices to different files, make sure to export them as well.

### How to Combine Slices Into a Single Store

A store can have only one reducer, so it is important to combine all the slices and their reducers into a single reducer without losing its identity and functionality.

To accomplish this, we'll use `configureStore` to `createStore`.

`configureStore` is similar to `createStore`, but it can merge reducers of multiple slices into a single reducer.

It has a `reducer` object that accepts one or more slices, like this:

```js
import { authSlice } from './auth-slice'
import { cartSlice } from './cart-slice'
import { wathclistSlice } from './watchlist-slice'

const store = configureStore({
  reducer: {
    authSliceReducer: authSlice.reducer,
    cartSliceReducer: cartSlice.reducer,
    watchlistSliceReducer: watchlist.reducer,
  },
})

export defualt store
```

This sets up the store to be consumed an used by multiple components across the application.

## How to Use Redux States in Components

Now that we have our Redux store ready, we can consume and dispatch actions from components using the `useSelector` and `useDispatch` hooks.

Here's a simple example:

```js
import { useDispatch, useSelector } from 'react-redux'
import { cartActions } from '...'

export default function Cart(props) {
  const dispatch = useDispatch()
  const selector = useSelector((state) => state.watchlistSliceReducer) // Since the store has multiple reducers, we need to drill into the appropriate slice state.

  const addToCartHandler = () => {
    const dummyitem = {
      id: Math.random(),
      name: `Dummy Item ${Math.random()}`,
      price: 20 * Math.random(),
    }
    dispatch(cartActions.addItem(cartItem.dummyitem))
  }
  const removeFromCartHandler = (id) => {
    dispatch(cartActions.removeItem(id)) //Passing id as an argument to the reducer function.
  }

  return (
    <div>
      {selector.cart.length &&
        selector.cart.map((item) => {
          return (
            <div>
              <p>Name: {item.name}</p>
              <p>Price: {item.price}</p>
              <p>Quantity: {item.qty}</p>
              <button onClick={removeFromCartHandler}>Remove item</button>
            </div>
          )
        })}
      <h3>Total cart value:{selector.cart.total}</h3>
      <button onClick={addToCartHandler}>Add dummy item</button>
    </div>
  )
}

```

## How to Handle Asynchronous Code Using Action Creators

So far, so good.

But wait, there's still an important topic we haven't covered – how to handle side effects, or asynchronous code, with Redux. 

Consider a scenario where you'd want to dispatch an action that needs to handle a block of code that produces a side effect. But at the same time, reducers should be pure, side effect free, and synchronous.

This means that adding any code in reducers that produce side effects goes against core Redux principles, and is super bad.

To deal with such instances, we have two choices: either using `useEffect`/ `componentDidMount`, or by writing action creators.

### How to Handle Side Effects with `useEffect` or `componentDidMount`

One way to handle side effect producing code is to use `useEffect`. By doing this, we split the side effect producing code from the dispatched action itself, so the reducers remain pure and synchronous.

But, one major drawback of using `useEffect` is code redundancy and duplication.

If there are two or more components that produce the same side effect, we'd want to have the same logic run in those components' `useEffect` hook, which is a bad practice.

One quick workaround is to put the logic into a helper function and run this function at the root component, and have all the other components listen to the changes via Redux state.

This would be permissible and not necessarily a bad practice, but an even better way would be to use an action creator thunk.

## How to Handle Side Effects with Action Creators

A thunk is basically a function that returns another function which is not invoked immediately. In fact, we've been using action creators all this time unknowingly when we dispatched action functions.

This is because Redux Toolkit abstracts all this away from us. What's really happening under the hood is that this function returns an action object which corresponds to the appropriate reducer function.

For example, when we do this:

`dispatch(actions.dispatchActions(args))`

The method `dispatchActions(...)` returns an action object with a type and payload property. Roughly speaking, the `dispatchActions()` function would be something like this:

```js
function dispatchActions(args) {
  return { type: 'UNIQUE', payload: { ...args } }
}
```

`type: 'UNIQUE'` is a placeholder, but internally a unique ID is assigned to different action dispatchers, which are then hooked to their respective reducer functions. 

So, `dispatch(actions.dispatchActions(args))` effectively means, `dispatch({ type: 'UNIQUE_ID', args: args })`. This should also make it clear as to why the `payload` property is attached on the action dispatcher.

So thunks are like a user defined action creator that returns a function instead of an action object. Action creator thunks are standalone functions, not a reducer function, so we can write asynchronous code there.

An action creator thunk is a function that accepts arguments passed by the user and returns a function that further accepts a dispatch argument passed by Redux Toolkit for us. And it's Redux Toolkit itself that later invokes this returned function.

The boilerplate code of an action creator thunk would look something like this:

```js
export const actionCreatorThunk = async(args) => {
  return (dispatch) => {
    // async code here
    dispatch(actions.actionDispatcher(args))
    // more async code
    // more dispatch functions
  }
}

```

The returned function can also be an `async` function, because it's clear that it is handling other `async` code. Action creators can have multiple dispatch functions dispatching multiple dispatch actions.

The action creators thunks can be then dispatched as follows:

```js
import {actionCreatorThunk} from '...'
import {useDispatch} from 'react-redux'
export default function Component(args){
    const dispatch = useDispatch()
    
    dispatch(actionCreatorThunk(dataToBePassed))
    ...
    ...
    ...
 }
```

The good thing about Redux Toolkit is that it not only accepts action objects returned by action reducer functions, it also accept functions returned by action creators. 

When it is identified that a function is returned instead of an action object, Redux Toolkit automatically calls the returned function and passes a dispatch function as an argument.

We can use action creators in places where network calls are made, either to POST or query data from a database, and then set the Redux state from the data sent/received. This ensures the correct coordination between the backend and frontend system.

## In Summary

If you've made it thus far, kudos. I really appreciate you taking the time to read until the end.

In a nutshell, synchronous and side effect free code should go into the reducers, while asynchronous code should be used in action creators or side effect handlers such as `useEffect`.

That's it for this article. I hope this helped you learn something new about writing better Redux code for app-wide state management.

If you have any questions or feedback, feel free to reach out to me on [Twitter](https://twitter.com/prajwalinbizz).

You could also connect with me on [LinkedIn](https://linkedin.com/prajwal-kulkarni).

If you found this article helpful, consider sharing it with your friends who are learning React.

Cheers!

