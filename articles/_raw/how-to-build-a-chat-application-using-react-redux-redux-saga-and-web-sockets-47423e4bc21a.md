---
title: How to Build a Chat Application using React, Redux, Redux-Saga, and Web Sockets
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2017-12-07T16:21:01.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-chat-application-using-react-redux-redux-saga-and-web-sockets-47423e4bc21a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*uttr9Cbjv7DOlgxP1r0pnA.png
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
seo_desc: 'Interested in learning JavaScript? Get my ebook at jshandbook.com


  In this tutorial I’m going to build a basic chat room. Every user that connects
  to the server is registered upon connection, gets a username, and then can write
  messages that are broa...'
---

![Image](https://cdn-media-1.freecodecamp.org/images/1*J3QJAw-Yst12S6yP4rMsVg.gif)

> Interested in learning JavaScript? Get my ebook at [jshandbook.com](https://jshandbook.com/)

In this tutorial I’m going to build a basic **chat room.** Every user that connects to the server is registered upon connection, gets a username, and then can write messages that are broadcast to every connected client.

> There’s a lot to learn about this topic and the new browser APIs. I publish one new tutorial every day on my [blog about frontend development](https://flaviocopes.com), don’t miss it!

The application is a distributed application built using a **Node.js server**, and a browser client built in **React**, managing data using **Redux** and side effects with **Redux-Saga**.

Client-server communication is handled through **WebSockets**.

The complete source code for this app [is available here](https://github.com/flaviocopes/chat-app-react-redux-saga-websockets).

### Initialize create-react-app

Let’s start up the project by using the **create-react-app** quickstarter, `create-react-app chat`

![Image](https://cdn-media-1.freecodecamp.org/images/1*p2yTo9GV4zRaWAAWEtEnbQ.png)

Once this is done, `cd` in the app folder and run `yarn start`

![Image](https://cdn-media-1.freecodecamp.org/images/1*EXosDPsWjYFa9_P8xDdjcw.png)

### The chat app layout

Our app will have this basic layout, which is very common in chat apps:

![Image](https://cdn-media-1.freecodecamp.org/images/1*uttr9Cbjv7DOlgxP1r0pnA.png)

To do this, we need to create a static version of a chat using plain HTML and CSS, which is a minimal, retro-style chat layout with CSS Grid.

The code is very simple:

The result is a sidebar that will host the list of users and a main area with the new message box at the bottom of the screen:

![Image](https://cdn-media-1.freecodecamp.org/images/1*-Eu_5i-mCp1UADBYRt5TJg.png)

### Add Redux to manage the state

Now let’s talk about the data.

We’ll manage the state using **Redux**.

Install Redux and react-redux with `yarn add redux react-redux` . Then we can translate the basic HTML layout we added on top and prepare it to fill the components we’ll create later:

We include the **Sidebar**, **MessagesList**, and **AddMessage** components.

They all have:

* a presentational component, which manages the user interface
* a container component, which manages its behavior and the data that the presentational component will show

Let’s edit the main app `**index.js**` file to initialize Redux, then import the `chat` reducer, and then create the `store` .

Instead of telling ReactDOM to render `<App` /> , `enter Pr`ovider, which makes the store available to all the components of the **app, without explicitly passing i**t down.

Next, the **actions**.

Enter the actions constants to the `**ActionTypes.js**` file, so we can reference them in other files easily:

This file contains the four actions that will power our chat. You can add a new message, and a new user can be added to the chat. A new message can be sent, and the server will send updates to the users list when a person joins or quits the chat.

When a new message is created, I now force the author name to “Me.” We’ll add usernames later.

The **reducers** take care of creating a new state when an action is dispatched. In particular:

* when a **message is added by us,** we add it to the (local) list of messages
* when **we receive a message** from the server, we add it to our list of messages
* when **we add a user** (ourselves), we put it in the users list
* when **we get an updated users list** from the server, we refresh

Let’s dive into the components that will render this data and trigger the actions, starting with `**AddMessage**`:

This functional component is very simple, and creates an `input` field into the `#new-message` section. When the **enter** key is pressed, we dispatch the `addMessage` action, passing the value of the input field.

Next up: the `Message` component. It renders a single chat message, by using the `_Author: Message_` format:

It is rendered by the `MessagesList` component, which iterates over the list of messages:

The `Sidebar` component instead iterates over each user, and prints the user name for every user that joins the chat:

We generate the Container Components for the above Presentational Components, by using the `connect()` function provided by `react-redux` :

This code gives us this nice result. When we type a message and press enter, it’s added to the messages list:

![Image](https://cdn-media-1.freecodecamp.org/images/1*4vltWKu61NunDertK0VpKg.gif)

### Adding ourselves in the users list

The sidebar should show the list of users. In particular, since now the app does not talk to anyone, we should see `**Me**` in the sidebar. Later on, we’ll add additional people that join the chat. We already have the `addUser` Redux action, so it’s a matter of calling it in our `**index.js**` file after initializing the store:

![Image](https://cdn-media-1.freecodecamp.org/images/1*TTd4ccmkU8y6JsSQQnNb_Q.png)

### Testing

Let’s add automated tests to make sure everything is working correctly and continues to work correctly in the future when we add more functionality.

Since I’m using `create-react-app`, [Jest](http://facebook.github.io/jest/) is already available to use, and I can simply start adding tests. To keep things simple, I add the test file into the folder that contains the file to be tested.

We start by testing our actions:

and we can test our reducers as well:

We also add some basic tests for our Presentational Components:

### Adding a server-side part

A chat that is local and does not communicate to the network is, frankly, not a very interesting place to spend time. Let’s create a centralized server where users will log into, and where they can talk to each other.

I’ll use the [native WebSocket object](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket) in the browser, which is widely supported, and the [ws WebSocket library](https://github.com/websockets/ws) on the Node.js server.

Let’s start with the server, which is super simple:

As soon as a client connects we start listening for the `**ADD_USER**` and `**ADD_MESSAGE**` events. When the client establishes the connection, it will send an `ADD_USER` event with the name. We’ll **add it to the server-side list of users** and **issue a broadcast** to all the connected clients.

When an `ADD_MESSAGE` event is sent, **we broadcast it to all connected clients**.

On connection close, we **remove the user** name from the list and broadcast the new users list.

On the client-side, we need to **initialize the `WebSocket`** object and send an `ADD_USER` event when we connect to the chat. Then **we listen for `ADD_USER` and `ADD_MESSAGE` events** broadcast by the server:

We’ll import `setupSocket()` from the main `**index.js**` file.

We now need to introduce a way to **handle side effects** into our code, and to handle creating a WebSocket event when the user types a message, so it can be broadcast to all the connected clients.

To perform this operation in a clean way, we’re going to make use of `[**redux-saga**](https://redux-saga.js.org/)`, a library which provides a good way to handle side effects in Redux/React.

![Image](https://cdn-media-1.freecodecamp.org/images/1*-GC9G3YWGrTD85yV5N0STg.png)

Start with `yarn add redux-saga`

We initialize the `redux-saga` middleware and connect it to the Redux store to hook our `**saga**`:

Redux-Saga is a **Redux middleware**, so we need to initialize it during the store creation. Once this is done, we run the middleware and we pass the user name and the `dispatch` function. Before doing so, we initialize the socket so we can reference it inside the saga.

Previously, the user was called ‘Me,’ but it’s not nice if every user is calling itself ‘Me.’ So I added a **dynamic username generator**, using [Chance.js](http://chancejs.com/). Every time we log in, we have a unique name generated for us by importing `utils/name` :

Let’s now dive into our **saga**:

Conceptually it’s very simple. We take all actions of type `ADD_MESSAGE` and when this action occurs, we send a message to the WebSocket, passing the action and some details. The chat message sent by our user can be dispatched to all connected clients by the server.

Here we get to the final result, and below you can see a gif that shows how the chat works with multiple clients connected. We can open as many windows as we want, and as soon as we load the server URL, we are going to be connected with a new username to the chat. We don’t see past messages, like in IRC, but we will see every message written from the moment we sign in.

As soon as we leave, our username is removed and the other folks in the chat can continue chatting.

![Image](https://cdn-media-1.freecodecamp.org/images/1*J3QJAw-Yst12S6yP4rMsVg.gif)

> Interested in learning JavaScript? Get my ebook at [jshandbook.com](https://jshandbook.com/)

