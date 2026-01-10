---
title: How to become a pro with React setState() in 10 minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-06T19:47:37.000Z'
originalURL: https://freecodecamp.org/news/get-pro-with-react-setstate-in-10-minutes-d38251d1c781
coverImage: https://cdn-media-1.freecodecamp.org/images/0*_agRQIzQvukx6TC7
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

  This article is aimed at people who have already had their first approach to React,
  and who, as beginners, have doubts about how setState works and how to use it correctly.
  It should also help mid to senior devs use cleaner and more ...'
---

By Eduardo Vedes

This article is aimed at people who have already had their first approach to React, and who, as beginners, have doubts about how `setState` works and how to use it correctly. It should also help mid to senior devs use cleaner and more abstracted ways of setting state, and make higher-order-functions handle and abstract state.

Just read and have fun!

So grab a cup of coffee and keep reading! ?

### Basic Concepts of setState( )

React Components let you split the user interface (UI) into independent, reusable pieces, so you can think about each piece in isolation.

Conceptually, components are like JavaScript functions. They accept arbitrary inputs (called “props”) and return React elements describing what should appear on the screen.

If you need to give the user the opportunity to input something or in some way change the variables the component is receiving as props, you’ll need `setState`.

Whether you declare a Component as a function or a class, it must never modify its own props.

All React Components must act like pure functions with respect to their props. This means functions that never try to change their inputs and always return the same result for the same inputs.

Of course, application UIs are dynamic and change over time. That’s why `state` was created.

`State` allows React components to change their output over time in response to user actions, network responses, and anything else, without violating this rule.

Components defined as classes have some additional features. Local state is a feature available only to class Components.

`setState` is the API method provided with the library so that the user is able to define and manipulate state over time.

### **Three Rules of Thumb When Using setState( )**

#### **Do Not Modify State Directly**

![Image](https://cdn-media-1.freecodecamp.org/images/fDk0J1KHkNJKyjha9jV2Ic5VtMHtx0hX54-5)
_wrong and right ways of setting state_

#### **State Updates May Be Asynchronous**

React may batch multiple `setState()` calls into a single update for performance.

Because `**this.props**` and `this.state` may be updated asynchronously, you should not rely on their values for calculating the next state.

![Image](https://cdn-media-1.freecodecamp.org/images/U802XeMCbWXgWEqgFS1oISKMBIalMacJHIr9)
_manipulate state with a functional approach_

You should always do this kind of manipulation with a functional approach, supplying the `state` and `props` and returning the new `state` based on the former.

#### **State Updates are Merged**

When you call `setState()`, React merges the object you provide into the current `state`.

In the example below, we’re updating the variable `dogNeedsVaccination` independently of the other `state` variables.

The merging is shallow, so `this.setState({ dogNeedsVaccination: true })` leaves the other variables intact, replacing only the value of `dogNeedsVaccination`.

![Image](https://cdn-media-1.freecodecamp.org/images/MkFjwenYGJsPRkbOZJOcSSHaU26jJ83Y430C)

### **Respect the Data Flow and Avoid State the Max**

**Data flows down!** Neither parent nor child components can know if a certain component is stateful or stateless, and they shouldn’t care whether it is defined as a function or a class.

That’s why `state` is often called local or encapsulated. It is not accessible to any component other than the one that owns and sets it.

When you `setState` a prop and use it in your component, you’re breaking the flow of the rendering props. If for some reason the prop passed into your component changed in the parent component, the child will not re-render auto-magically ?!

Let’s check an example:

![Image](https://cdn-media-1.freecodecamp.org/images/BdJA87j3HTnLGzQMnx0enaMdNXelqTzrkgZ1)

Here you have a `Home` Component which is generating a magic number each 1000ms and setting it into its own `state`.

After that it renders the number and invokes three `Child` Components (Siblings) that will receive the magic number with the objective of displaying it using three different approaches:

#### First Approach

Component `ChildOfHome` is respecting the React props cascade flow and, considering that the objective is only to show the magic number, it’s rendering the `props` received directly.

![Image](https://cdn-media-1.freecodecamp.org/images/DdFAz1VvRhbZ1vgJgoKYoguzuPEWRDsFkI-L)

#### Second Approach

Component `ChildOfHomeBrother` receives the `props` from its parent and, invoking `componentDidMount`, sets the magic number into `state`. Then it renders the `state.magicNumber`.

This example doesn’t work because `render()` doesn’t know that a `prop` has changed so it is not triggering the re-rendering of the component. As the component is not re-rendered anymore, `componentDidMount` is not invoked and the display is not updated.

![Image](https://cdn-media-1.freecodecamp.org/images/gPNGY21whSekaZpxB2qWutfofEw96BwgAs6X)

#### Third Approach

Usually when we try to make it work using the second approach we think something is missing. Instead of taking a step back we keep on adding stuff to the code to make it work!

So in this third approach we’ve added `componentDidUpdate` to check if there’s a change in `props` to trigger the re-rendering of the component. This is unnecessary and leads us to unclean code. It also brings with it performance costs that will be multiplied by the number of times we do this in a big App where we have a lot of chained Components and side effects.

This is wrong unless you need to allow the user to change the prop value received.

If you don’t need to change the prop value, always try to keep things working according to the React flow (First Approach).

You can check a working webpage with this example I’ve prepared for you in [Glitch](https://freezing-transport.glitch.me/). Take a look and have fun ?

Also check out the code in the `**Home.js**` and `**HomeCodeCleaned.js**` (without the HTML stuff) in [my repo](https://github.com/evedes/set-state-in-10-min) about this article.

### How to setState

So at this point I think it’s time to get our hands dirty!

Let’s play a little bit with `setState` and improve on that! Just follow along and grab another cup of coffee!

Let’s create a small form to update user data:

![Image](https://cdn-media-1.freecodecamp.org/images/7QEN8rHC9lVLP1YX2nyTVEcC7s7G-25dDkjG)
_Small exercise on setState()_

Here’s the code for the example above:

![Image](https://cdn-media-1.freecodecamp.org/images/YVqIxzftG-aQyjVeMvPwb5IPbpe7Xlq-C7ln)
_Initial Home Component_

We are setting `state` as an object, and there’s no problem because our current state doesn’t depend on our last state.

What if we create one more form field to introduce and display Last Name?

![Image](https://cdn-media-1.freecodecamp.org/images/FaqdEOSaxiOvUvHwrdTjTI4DVr9icW3-40Dt)
_Last Name feature_

![Image](https://cdn-media-1.freecodecamp.org/images/Jut4MxFFK81esqawr6NkqHWMsn4fNVWWfbzl)
_abstracted handleFormChange_

Nice! We’ve abstracted the `handleFormChange` method to be able to handle all the input fields and `setState`.

What if we add a toggle button to mark the data as valid or invalid and a counter to know how many changes we’ve done to the state?

![Image](https://cdn-media-1.freecodecamp.org/images/T52heLJjKgK8ziG6CcEuxjYDhc91qjdOxP1h)
_Screenshot showing the console.log of the component state_

![Image](https://cdn-media-1.freecodecamp.org/images/iu0Fdle1B1iFim6GZIKf8O6z3fgjHDn4h7qe)
_handleFormChange updated with checkbox and counter handlers_

Yeah! We are rocking! We’ve abstracted a lot of stuff!

Hmmm… Let’s say I do not want a checkbox to control the `isValid` variable but a simple toggle button.

Let’s also separate the counter handler from this method. It works well, but in more complex situations where React needs to batch/group changes, it’s not a good policy to rely on the `this.state.counter` variable to add one more. This value can change without you being aware of it.

We’re using a shallow copy of it at the instant the operation is invoked, and at that certain point in time you don’t know if its value is the one you were expecting or not!

Let’s go a little bit functional!

![Image](https://cdn-media-1.freecodecamp.org/images/0p8DlnnaNpXtqPG81xTayly9J8VE2ibidKwK)
_Screenshot showing the Valid/Invalid Toggle and the console.log of the state.counter variable_

![Image](https://cdn-media-1.freecodecamp.org/images/C5veVluHRXO39bXkvVKgHCWuH6japAFj3D3R)
_separation of the control handlers_

Okay — We’ve lost abstraction because we’ve separated the handlers, but it’s for a good reason!

So at this time we keep the `handleFormChange` passing an object to the `setState` API method. But the `handleCounter` and `handleIsValid` methods are now functional and start by grabbing the current state and then, depending on that state, changing it to the next one.

This is the correct way of changing the `state` of variables that depend on the previous state.

What if we want to `console.log()` state changes of the `firstName` and `lastName` input forms each time a change occurs? Let’s give it a try!

![Image](https://cdn-media-1.freecodecamp.org/images/HUCXO8J0ASy4NNfDU1zZuEtXq-zpdiIQe1ZK)
_logFields() method_

Nice! Each time the `handleFormChange` occurs (which means a new key press happened) the `logFields()` method is invoked and logs the current state into the console!

Let’s check the browser console:

![Image](https://cdn-media-1.freecodecamp.org/images/jLz33AfgQi6kldAGYf4KT479Zr2ntt3-RBUk)
_screenshot of the console.log of firstName and lastName state_

Wait! What happened here folks? The console log is one change before the current form input! Why is this happening?

#### **setState is async!!**

We already knew this but now we’re seeing it with our eyes! What’s happening there? Let’s take a look at the `handleFormChange` and `logFields` methods above.

So the `handleFormChange` method receives the event name and value, then does a `setState` of this data. Then it calls the `handleCounter` to update the counter info, and in the end invokes the `logFields` method. The `logFields` method grabs the `currentState` and returns ‘Eduard’ instead of ‘Eduardo’.

The thing is: `setState` is async and doesn’t act in the moment. React is doing its job and executes the `logFields` method first, leaving `setState` for the next event loop.

But how can we avoid this kind of situation?

Well, the `setState` API has a `callback` to avoid this situation:

![Image](https://cdn-media-1.freecodecamp.org/images/3wyO2ef7SMFdzVrxDGpTwJkXvdEV7wCZLGh2)
_setState API method_

If we want the `logFields()` to take into account the recent changes we’ve made to the state, we need to invoke it inside the callback, like this:

![Image](https://cdn-media-1.freecodecamp.org/images/GPYFMLHBhIOkbjGGdfcDm5Uz24og0hvPYtvC)
_using the setState() API method callback handler_

Okay, now it’s working!

We’re telling React: “Hey React! Beware that when you invoke the `logFields` method I want you to have the `state` already updated okay? I trust you!”

React says: “Okay Edo! I’m going to handle all this batch of stuff I usually do in the backyard with the `setState` thingy and only when I’m finished with that I’ll invoke `logFields()`! Cool man! Relax!”

![Image](https://cdn-media-1.freecodecamp.org/images/2YuGDOcmnseFY5lMTceR9FBGZ8h4friD-gnT)
_screenshot of the console.log() of fullName_

And as a matter of fact — it worked!

Okay everyone! By this time we’ve handled the major pitfalls of `setState`.

Do you have the courage to go beyond the wall? Grab a cup of coffee and let’s get really kewl…

### Getting Fancy with setState( )

Now that we have `handleCounter` and `handleIsValid` methods, and `setState()` expressed with functions, we can compose the state update with other functions! **Me likez composition! Let’s have some fun!**

![Image](https://cdn-media-1.freecodecamp.org/images/pBcn25XBdxdA9uqPSqRXDRbRu6fdMB5MdS-4)
_abstracting handleIsValid_

We can take the logic inside `setState` to a function outside the class component. Let’s call it `toggleIsValid`. ☝️

![Image](https://cdn-media-1.freecodecamp.org/images/MQkXig9EC7Fem4-xeipehkq1KUJweQE027QD)
_toggleIsValid Function_

Now this function can live outside the class component, anywhere in your app.

What if we use a higher order function?

![Image](https://cdn-media-1.freecodecamp.org/images/AfGwofoy8ykA4pYHHr9cRiMSeUN9oEgH-yca)
_changing toggleIsValid by an higher order function_

Wow! Now we’re not invoking the `toggleIsValid` function anymore. We’re invoking an abstract higher order function called `toggleKey` and passing a key (string in this case) into it.

How do we need to change the `toggleIsValid` function now?

![Image](https://cdn-media-1.freecodecamp.org/images/YJ1jrcCACrvShq5Je8fZYWrxSfEOdlZYWiDo)
_toggleKey higher order function_

What?! Now we have a function called `toggleKey` that receives a `key` and returns a new function which changes state according to the supplied key.

This `toggleKey` can be in a library or in a helper file. It can be invoked in a lot of different contexts to change the state of whatever you want to its opposite.

Great!

Let’s do the same with the increment counter handler:

![Image](https://cdn-media-1.freecodecamp.org/images/nkgBbIQTNdFGZfTDtZkigh1HDMCWZBnnNii9)
_handleCounter abstraction to invoke an higher-order-function_

![Image](https://cdn-media-1.freecodecamp.org/images/oxRMcY3Kwj72HrWrE5IpNTDhlcb4mnaw8s44)
_incrementCounter higher-order-function_

Yeah! It works! So nice. Let’s get crazy now…

### Shooting the Moon and Getting Back

What if we create a generic `makeUpdater` function that receives the transformation function you want to apply, takes the key, and returns the state function managing the state with the transformation function and the key? Little bit confused? Let’s go!

![Image](https://cdn-media-1.freecodecamp.org/images/mKBYvEDHZDt1hhK-67J-yc7G9ciZd6ONeU37)
_makeUpdater higher-order-function_

Ok that’s enough…Let’s stop here. ?

You can check all the code we’ve done in this [GitHub repo](https://github.com/evedes/variations-in-set-state).

### Last But Not Least

Don’t forget to avoid the max using state and respect React rendering props cascade.

Don’t forget `setState` is async.

Don’t forget `setState` can take an object or a function

Don’t forget that you should pass a function in when your next state depends on your previous state.

### **Bibliography**

1. React Documentation
2. [Reach Tech Courses by Ryan Florence](https://reach.tech/courses), which I really recommend.

Thank you very much!

