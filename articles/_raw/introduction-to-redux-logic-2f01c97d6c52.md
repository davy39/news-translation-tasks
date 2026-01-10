---
title: An Introduction to Redux-Logic
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-07T17:57:06.000Z'
originalURL: https://freecodecamp.org/news/introduction-to-redux-logic-2f01c97d6c52
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9lDu6F6XfDmzTsF3tCRDVA.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Redux
  slug: redux
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Sam Ollason

  This article will go through a high-level overview of Redux-Logic. We will look
  at what is it, why it is needed, how it differs from other Redux middleware and
  why I think it’s the best choice. We will then see an example of a simple W...'
---

By Sam Ollason

This article will go through a high-level overview of [Redux-Logic](https://github.com/jeffbski/redux-logic). We will look at what is it, why it is needed, how it differs from other Redux middleware and why I think it’s the best choice. We will then see an example of a simple [Weather app](https://github.com/SamOllason/weather-app-redux-logic-example) to demonstrate how the core concepts are put into practice.

This article assumes you have a good understanding of React and Redux.

### **A quick refresher on Redux**

Redux is a state container for JavaScript applications and is commonly used with React. It provides a central place for storing data that is used across your application. Redux also provides a framework for making **predictable** state mutations. Using Redux makes it easier to write, understand, debug and scale data-driven and dynamic applications.

In Redux, components call **action creators** which dispatch **actions**. Actions are (usually!) small plain objects that express an intent or an instruction. The actions can also contain ‘payloads’ (i.e. data).

Application state is managed by **reducers**. They sound more complicated than they are! Actions are handled by a root reducer which then passes the action and the payload to a particular reducer. This reducer will **take a copy** of the application state, **mutate** **the** **copy** (according to the action and its payload) and then update the state in the application **Store**.

### **Why the need for Redux Logic?**

By default, all actions in Redux are dispatched synchronously. This presents a challenge for any application that needs to support asynchronous behaviour such as fetching data from an API … so pretty much any application!

To handle async behaviour using Redux, we need some kind of [middleware](https://en.wikipedia.org/wiki/Middleware) that does some processing between when the action is dispatched and when the action reaches the reducers. There are several popular libraries for providing this functionality.

After exploring the various options, I have been using Redux-Logic in a variety of projects for a while now and have found it to be great!

### **Redux-Logic lifecycle**

Redux-Logic provides middleware that performs some processing between when an action is dispatched from a component and when the action reaches a reducer.

We use the [redux-logic](https://github.com/jeffbski/redux-logic) library to create ‘Logic’. These are essentially functions that intercept particular **plain object** actions, perform asynchronous processing and then dispatch another **plain objec**t action. Logic functions are really declarative and flexible, as we shall see!

An important thing to take away here is that all actions that Redux-Logic works with are **plain objects**. The action that is dispatched by the UI component and the action that is then dispatched by the Logic will **always** be a plain object (as opposed to, for example, a function). We will revisit this below when we compare different middleware options.

Under the hood, Redux-Logic uses ‘observables’ and reactive programming. [Read more about that here](https://github.com/jeffbski/redux-logic).

### **Data flow**

Below, for comparison, is a diagram I created showing the important points in the lifecycle of a synchronous redux process. There is no middleware included (because none is needed!).

![Image](https://cdn-media-1.freecodecamp.org/images/gK7CP25zZc5gLL7FhvRdImhFclj3yyxSMZy6)

Now here is a diagram showing the important parts of a project that use the redux-logic library to handle asynchronous actions. This will be useful to refer to later alongside the example below.

![Image](https://cdn-media-1.freecodecamp.org/images/9BNnOO6ZOIeBuMyS69YEnSWhd5WKtRfXVR9n)

You can see how the middleware operates in between when an action is dispatched and when it is handled by a reducer.

### Main differences from other solutions

[**Redux-Thunk**](https://github.com/reduxjs/redux-thunk) is a popular choice for Redux middleware that also allows you to support asynchronous behaviour. To handle asynchronous behaviour using Redux-Thunk your actions creators have to **return functions** as opposed to returning plain objects with Redux-Logic. I believe that dispatching plain objects with Redux-Logic makes your code much easier to write and much easier to understand.

Furthermore, I believe the ‘plain object’ approach for handling asynchronous behaviour fits more naturally alongside the rest of the (synchronous) Redux architecture, which makes this middleware fit in more organically with Redux.

Another popular Redux middleware is [**Redux-Saga**](https://redux-saga.js.org/docs/introduction/BeginnerTutorial.html). I found the learning curve of getting my head around sagas (a relatively new ES6 feature) quite steep when I looked at this option. This would be compounded if you wanted to introduce this library into an application managed by a team with several people. Additionally, I think that if they are not well managed, then sagas can create complicated-looking code compared to the Logic you create with redux-logic. This can impact development speed and code maintainability.

### **Overview of example**

Below are simple snippets from a simple React application that can fetch the current weather conditions in a city and present it to the user. The example uses Redux-Logic to support asynchronous behaviour to fetch data using a free [OpenWeatherMap](https://openweathermap.org/api) API.

For comparison, I have included a synchronous Redux process that displays the number of requests a user has made.

[Here](https://github.com/SamOllason/weather-app-redux-logic-example) is the source code.

![Image](https://cdn-media-1.freecodecamp.org/images/abgtDbvHZYsuvjiSrJBKFZ71fovCsLHkTgcP)

### Setting up development environment

These are the commands I ran to start creating my application:

```
npx create-react-app appnpm install --save reduxnpm install --save react-reduxnpm install --save redux-logicnpm install --save axios
```

And to see the app:

```
npm start
```

Happy that I could see the default Create React App homepage at _localhost:3000_, I then started writing some code!

Below are code snippets that show the important points about integrating Redux-Logic into the project.

### Adding middleware to our Redux store

In _appStore.js_, if we were not using any middleware, we would normally only provide our root reducer to the createStore method. This is where we link our Redux-Logic middleware to the rest of our application.

We specify that we want to use _axios_ as our client for making HTTP requests.

We then use a method from redux-logic to create our middleware and finally we add it as a parameter to the createStore method. This means our Redux code will be able to access our middleware. Great!

![Image](https://cdn-media-1.freecodecamp.org/images/r0NZWYDdi3ZvOmUku2zR2t8F45z8YHnPDudw)
_appStore.js — used to create our Store and integrate our Logic_

### Dispatching asynchronous actions

With Redux-Logic, actions that trigger asynchronous behaviour are dispatched in the same way as actions that trigger synchronous state updates. There is nothing different!

For completeness, you can see below that when a user clicks on a button we call an action creator that has been passed to our component as props.

![Image](https://cdn-media-1.freecodecamp.org/images/DOnX38UsPeOd50wgdeuFRTA6dcFzYLu-n6bN)

### Intercepting Asynchronous actions

This is where we first see the emergence of the redux-logic middleware coming into play. We are using the redux-logic library to create some ‘Logic’ that will intercept specified actions.

In our Logic properties we tell redux-logic which action we want it to intercept. We specify that we want redux-logic to only provide data from the last action of this type that the component dispatched. In our example this declarative behaviour is useful if people keep clicking a button as they will get the value from the latest action they dispatched, not necessarily the last promise to return!

Next we specify that when the asynchronous process returns we **immediately** **dispatch** one of two actions. If the promise returned successfully, we return a _GET_WEATHER_FOR_CITY_SUCCESSFUL_ action. This is what we want!

Alternatively, if the promise returned was rejected then we dispatch _GET_WEATHER_FOR_CITY_FAILURE_.

**This is where redux-logic really shines**. It is clear what the intent of the Logic code is, and what is emitted are simple objects which are easy to read and interpret! I find this really easy to read, understand and debug.

At the bottom we make it clear what we want our asynchronous process to do. We want to return the value of a promise. Notice how we pass in the payload that came with our action into the URL.

![Image](https://cdn-media-1.freecodecamp.org/images/kY3GKXhgCYVKaxZ2FgVRA1MExoxEzUr7pHzc)

### Processing Asynchronous actions

You can see from the _weatherDataHandling.js_ reducer that the actions dispatched from our Logic are then treated as plain object actions. Reducers mutate state in the **same way as with synchronous actions**. So the screenshot below is what you would expect from working with Redux before. Super!

![Image](https://cdn-media-1.freecodecamp.org/images/B58wMGADSPhShrZznOcsMNRicqSo5l52pZo-)

### Summary

Redux is a popular predictable state container for JavaScript applications. By default all Redux actions support synchronous behaviour only, and you will need some kind of middleware solution for asynchronous behaviour.

Redux-Logic provides a **clear** and **powerful** middleware that allows you to use asynchronous actions in your Redux application. You add your middleware to your Redux **Store** to allow your application to use Redux-Logic. You use the [redux-logic](https://github.com/jeffbski/redux-logic) library to create **Logic** which intercepts particular actions and dispatches further actions after some asynchronous processing (like fetching data from an API) completes.

All of the actions that are involved are **plain object** actions. I believe this makes it **easier to write** and **easier understand** compared with other solutions. Furthermore, redux-logic feels like a more organic fit with the other parts of the Redux architecture.

Thanks for reading, I welcome any comments or questions below!

