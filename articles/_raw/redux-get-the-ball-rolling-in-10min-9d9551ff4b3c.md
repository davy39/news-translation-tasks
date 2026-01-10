---
title: How to get the ball rolling with Redux in ten minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-16T12:56:18.000Z'
originalURL: https://freecodecamp.org/news/redux-get-the-ball-rolling-in-10min-9d9551ff4b3c
coverImage: https://cdn-media-1.freecodecamp.org/images/0*0OdJkNC70fPI3dih
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Eduardo Vedes

  Hi everyone ❤️

  For a while now I’ve been hearing my friends and colleagues complaining about how
  hard it was to get into Redux.

  I run a freeCodeCamp Study Group in the South of Portugal, Faro, so every week I
  try to motivate and ment...'
---

By Eduardo Vedes

Hi everyone ❤️

For a while now I’ve been hearing my friends and colleagues complaining about how hard it was to get into Redux.

I run a [freeCodeCamp](https://www.freecodecamp.org/) Study Group in the South of Portugal, Faro, so every week I try to motivate and mentor some fellow coders that have a lot of growing pains trying to make their way into programming.

Dan Abramov created an amazing introduction course to Redux, which I had the pleasure to see in [egghead.io](https://egghead.io/courses/getting-started-with-redux), covering all the aspects of Redux. Also the Redux documentation site, [here](https://redux.js.org/), is very complete.

But for some reason many people still do not grok Redux.

The point is that Redux has a considerable entry-level learning curve!

You have to understand a lot of abstractions, you have to do a more functional approach to programming in JavaScript, know a lot of ES6 features and also understand very well a lot of JavaScript concepts such as immutability.

So, that’s why it might be very difficult for those of you that started React a few months ago and are very enthusiastic to abstract your state into a Redux store.

You hear the chit-chat around the coffee machine of how Redux is acing it, about clean programming, single sources of truth and the three principles that drive this huge ‘tiny’ (2kB) library…

So, no worries, you’ve came to the right place! This article is for you! And I’ll show you with an application first principle approach how easy it is to get the ball rolling with Redux.

A lot of ink has already been spilled around this subject, but let’s go. Let me try to introduce you as fast as I can to Mr. Redux in a React context.

To begin with this herculean task, I’m going to show you how to make a very simple counter application with the following user story:

1. display the current count number;
2. provide the user with two buttons, for incrementing and decrementing the count number.

Okay, at this point you think: I could do that very quickly with local state.

True story! And that’s the way, mate! We’re going to start with a simple React example that uses local state and we’re going to transform the app into a React-Redux application.

But, before that, let me introduce you the basic concepts and purposes of Redux in a quick intro.

### 01. Basic concepts

Redux was created by [Dan Abramov](https://twitter.com/dan_abramov), and it’s defined as a “predictable state container for JavaScript apps.”

The motivation for Dan to create Redux was that SPA complexity was increasing a lot. And we were left alone to manage the state of our data with two difficult concepts for the human mind to reason about: **mutation** and **asynchronicity**. He calls them “**Mentos and Coke** — Both can be great in separation, but together they create a mess”.

So Redux proposes to describe the whole state of your app as a plain object. To change something in state you need to dispatch actions. Actions are plain Javascript objects that describe what happened to your app.

In the end, to tie actions and state together we write a function called a reducer. A reducer is just a Javascript function that takes state and action as arguments and returns the next state of the app.

#### **Three Principles of Redux:**

1. Single source of truth: the state of your whole app is stored in an object tree within a single **store**.
2. State is read-only. This means that the only way to change the state is to emit an **action** (an object describing what happened).
3. Changes are made with **pure functions**. Pure functions are functions that return a value only depending on the value of its arguments. They have no observably side-effects. When you call the same function with the same argument you always get the same return value. Pure functions also do not modify the arguments they receive. They actually return a new object, array, or function with the changes made to it.

### **02. The Counter App (React with local state, no Redux here)**

Okay mates, getting back to where we were coming from, let’s make our small counter app with local state only.

To start these kind of boilerplates I always use create-react-app (CRA) with bootstrap (just to get things simple but a little bit more fancy).

I kept the src/index.js which calls the <App /> component (playing the role of the main App view) and I’ve created a small stateful component called Counter.

If you wanna play with the code you can clone it from my GitHub repo [here](https://github.com/evedes/counter-app/tree/LocalStateApp) (keep in mind that it’s on the branch LocalStateApp).

So, let’s take a look at what we need to build our simple App.

![Image](https://cdn-media-1.freecodecamp.org/images/D7oGMjmZhHbkH-5aGrsFYyVbB2wKJ32Cl57F)
_src/index.js_

As simple as it is out-of-the-box.

![Image](https://cdn-media-1.freecodecamp.org/images/LfeiVOAtJvydP5pSf8ngcWyM4FRzYLZ7idsL)
_src/App.js_

I start my App Component initialising the state with a count variable which by default is set to zero.

![Image](https://cdn-media-1.freecodecamp.org/images/WIyCmKfV29XKwuI7fIdkAftQcOB15ifHGpfO)
_render() method_

I’ve built a very simple render method which destructures the count from state and shows some text. It also invokes the Counter stateful component passing the count value into it, and calls a small method called renderButtons() to render the increment/decrement buttons.

![Image](https://cdn-media-1.freecodecamp.org/images/AjPshHrGsV12IhBPxjHOsywqUw2lt12XF5uG)
_Counter stateful component_

![Image](https://cdn-media-1.freecodecamp.org/images/QcurtfDoH4MBEwlsgK5qPubRpUJKKqaUJAoa)
_renderButtons method_

Buttons call a method called updateCounter() and pass into it the type of update we want.

Here we are already building our way into Redux. One detail of actions in Redux is that, besides being simple objects that are up to you, they need to have a type property which is not undefined. (Just keep this in mind for now.)

![Image](https://cdn-media-1.freecodecamp.org/images/CR5ah94vMgnrFPzGljH2gEjLATrC2Om2VH4K)
_updateCounter method_

So here we have our updateCounter method which is very similar to what a reducer is in Redux. It gets the current state of the app, it gets the action wanted, and in the end it returns the new state of your app.

No magic at all! Redux is so natural and easy that you won’t feel the difference at all since you know two or three little details that make things seem very complex and hard to grok.

This is the final result of our app:

![Image](https://cdn-media-1.freecodecamp.org/images/G9qdpo7NBsiR3KR4s75hrwaUHwHDKchE6J2o)
_Result of the Counter App w/local state_

### 03. The Counter App (w/Redux State)

Okay friends! Let’s break down what we’ve done till now.

To install Redux you have to do:

_npm install --save redux react-redux_

![Image](https://cdn-media-1.freecodecamp.org/images/wYWi4Ky3cZ0LFSXnxCayMxQ-FNBbQ7CU-lLT)
_package.json after installing redux_

So after installing Redux your package.json dependencies should look like this ?.

Now what?

Let’s break our app! But not too much! ?

So my first step will be to remove the state from the App Component and create a Redux store on index.js:

![Image](https://cdn-media-1.freecodecamp.org/images/-o10x3etp2xA3IkZhRpSPqlbp5GMQN4qtUoM)
_src/index.js: creating a store in Redux and passing info to our main App._

What have we done here? ☕️

We’ve edited our main index.js file to create a Redux Store and pass it as a prop into our <App /> Component.

You might notice the two imports on the top: Provider and createStore.

You shall also notice the usage of the HOC <Provider> around <App/>. It works from the outside embracing our main app (it can also embrace Router stuff) in order to pass its API functions as props into our main App.

But wait!

What is the reducer in this variable definition?

![Image](https://cdn-media-1.freecodecamp.org/images/Hueg-SUiUsvJeetET3WkSkKXZRl-vcydyVo8)
_store creation_

Oh, we’re missing the reducer!

So the store needs to receive at least one reducer function to actually know how changes to the state operate.

Let’s do it!

In our old app we had that updateCounter method that we said was kind of a reducer.

So let’s move it to index.js (you can also extract it to another file and import it but let’s keep things simple for now).

![Image](https://cdn-media-1.freecodecamp.org/images/yqCK0TQoc2Kaykgi3dK9MG4Y7wGxlL7G35mf)

So we’ve extracted the updateCounter method from our App Component and we tweaked it a bit to give it some more context.

We’ve called it reducer. It’s the reducer we want to pass into the createStore method.

We’ve also added state as an argument because when we’ve extracted it from the <App /> Component context, it is not aware of any state anymore. We also stopped using setState and started to return the new count according to the action type we’re receiving (destructured it from the action arg).

We’ve used ES6 features to define an initialState by default if state is undefined. Remember what I told you above ?, that state couldn’t be undefined. It is one of Redux reducer’s conditions.

Besides that, nothing new everyone! Guess what? We have our reducer set and ready to do its job!

Now let’s pay attention to the actions!

In our old app they were the updateCounter invocation. But now as you remember we need to use the dispatch() method from Redux to dispatch actions so we need to add this layer of the API to our app.

![Image](https://cdn-media-1.freecodecamp.org/images/244AJTbrC81zHYEVOusrww8FyczOb3U3uNjf)

We’ve tweaked only two things folks! We’ve got the dispatch method, destructuring it from the props. Remember the <Provider /> HOC? Its role is to introduce these few Redux methods into your main app.

Instead of calling this.updateCounter we are now calling an updateCounter detached function supplying to it the action type (as we already were in the old app).

Let’s now see what’s the new updateCounter function:

![Image](https://cdn-media-1.freecodecamp.org/images/Q3ZHdtRMkZvZEHqBGsFugjM4eht0XwB5JR2S)
_updateCounter action_

Okay, nothing new, we just receive the dispatch method and return it with the type of action we want to fire.

At this time we’ve already created the store. We’ve created the reducer to grab the previous state of the app and the action and return the new state. We’ve built an action function to dispatch our app actions.

What more? This should be working by now! Why it is not?

Ohhh! Our App Component must be connected to Redux!

So this is our final step everyone! ?

![Image](https://cdn-media-1.freecodecamp.org/images/dsSibG5XXn43RklxNHQlBa8YlwQ66dwsmjmd)
_import connect from react-redux_

We start by importing the connect method from react-redux (into our App.js file).

Now at the end of our file, where we do the export default app of our component, we need to do the connection:

![Image](https://cdn-media-1.freecodecamp.org/images/EEdYOhBPEnPdtgEO0AL5KSofchFKn2QpM7uw)
_connect and mapStateToProps_

Okay! Remember we’ve removed the local state from our App component?

So… how do we inject the state of the store into our component?

We need to do a “mapStateToProps”! Get used to this because it will always be needed. App component will receive the new state as a prop. You have no this.state anymore!! 

mapStateToProps grabs the state from the connect method (HOC) and binds it to App Component.

And that’s it everyone! By this time your app should be running.

Feel free to take a look at the code in my GitHub repo (branch ReduxStateApp) [here](https://github.com/evedes/counter-app/tree/ReduxStateApp).

Of course there’s a lot of things to learn after this, but this is the main first step for you to understand how to get the ball rolling with Redux.

Now I ask you to do the homework: check out the two apps! Make sure you grok all the steps and compare them. Put a lot of _console.log_ to understand what’s going on, and above all accept that there’s an API in Redux that has a few but strict rules. Not everything is so logical for an entry-level as it’s expected to be! But those are only good growing pains for the sake of JavaScript!

Always remember to Be Strong and Code On everyone ❤️

And keep your pain in check with a good and hot ☕️ ️

### 04. Bibliography

01. [Redux Docs](https://redux.js.org/)

02. egghead.io Dan Abramov’s course on [Getting Started With Redux](https://egghead.io/courses/getting-started-with-redux)

