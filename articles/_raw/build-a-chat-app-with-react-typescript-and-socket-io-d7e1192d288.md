---
title: Build a chat app with React, TypeScript and Socket.io
subtitle: ''
author: Mihail Gaberov
co_authors: []
series: null
date: '2019-04-26T15:19:34.000Z'
originalURL: https://freecodecamp.org/news/build-a-chat-app-with-react-typescript-and-socket-io-d7e1192d288
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XB8rYOUoHDLtQHz470IDQw.jpeg
tags:
- name: Chat
  slug: chat
- name: React
  slug: react
- name: software development
  slug: software-development
- name: TypeScript
  slug: typescript
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'This is going to be a thorough step-by-step guide for building a single
  page chat application using React, TypeScript and Socket.io.

  If you want to skip the reading, here ? is the GitHub repository with a detailed
  README, and here you can check the l...'
---

This is going to be a thorough step-by-step guide for building a single page chat application using React, TypeScript and Socket.io.

If you want to skip the reading, [here](https://github.com/mihailgaberov/chat) ? is the GitHub repository with a detailed [README](https://github.com/mihailgaberov/chat/blob/master/README.md), and [here you](https://mihails-chat.herokuapp.com/#/chat) can check the live demo. In order to play with it, you need to open it in two different browsers (or browser tabs) or devices (you may use your computer and your smartphone) and chat with each other.

### Research

When you are about to start a new project, it’s a good practice to do initial research about the technical stack you are planning to use.

In other words, you may want or need — especially if you don’t have prior experience with it — to investigate on each technology you will be using. I recommend doing that separately. Take one of the them and create a small app that you can play with.

If you need to check how the integration of two or more technologies is going to work in a real project — then you might want to include them all together in your “*research-test-play*” app — but preferably do your research one at a time.

#### Getting to the point

When I started thinking about making this [chat application](http://mihails-chat.herokuapp.com/#/chat), I did exactly what I described above. I haven’t had recent experience with [TypeScript](http://www.typescriptlang.org/) and none with [Socket.io](https://socket.io/), so I had to take a look at those and get myself familiarized with what is their current state. As my plan was to use [React](https://reactjs.org/) as a main UI library, I needed to see how it was going to work with the other guys in the equation. So I did.

I created two small applications (repos [here](https://github.com/mihailgaberov/playing-with-socketio) and [here](https://github.com/mihailgaberov/react-contextapi-with-typescript)) with these technologies, just to be able to play with them and learn how could I use them in my future chat application.

After my initial research was done I was able to start thinking and planning the implementation of my main chat app.

![Image](https://cdn-media-1.freecodecamp.org/images/TjBOPkJjQ11wSe3gxxczgRYplWFpQnx5vmfd align="left")

\_Photo by \[Unsplash\](https://unsplash.com/photos/3TRdlKU-3II?utm\_source=unsplash&utm\_medium=referral&utm\_content=creditCopyText" rel="noopener" target="\_blank" title=""&gt;Hutomo Abrianto on &lt;a href="https://unsplash.com/search/photos/research-done?utm\_source=unsplash&utm\_medium=referral&utm\_content=creditCopyText" rel="noopener" target="*blank" title=")*

### High level planning

Usually what people mean when they say “*high level plan”* is that they are looking for the *big picture*. Which means we need to create a rough plan of our execution and define our main pillars, but without going into too much detail. Now when we have clear idea of what to do, let’s start doing it! ?

**Note:** From this point forward I will be assuming that you are following my steps as I describe them, hence I will be writing in the second person. ?

#### Tech stack

We already mentioned the main technologies we will be using, but let’s define a proper list of all of them here:

* [React with TypeScript](https://github.com/Microsoft/TypeScript-React-Starter#create-our-new-project) (`create-react-app my-app --scripts-version=react-scripts-ts`) — a UI library we will use for building our application’s user interfaces.
    
* [Redux](https://redux.js.org/) — a state management library we will use for managing our application’s state.
    
* [Express.js](https://expressjs.com/) — Node.js web application framework we will use for creating an [http server](https://expressjs.com/en/starter/hello-world.html) that we will need in our application, in order to take advantage of Socket.io engine.
    
* [Socket.io](https://socket.io/) — a JavaScript library for real time web applications. It enables real time, bi-directional communication between web clients and servers. We will use it to implement a simple chat behavior in our app.
    
* [styled-components](https://www.styled-components.com/docs) — a small library that we will be using for adding styles to our app and make the look and feel beautiful. It utilizes tagged template literals to style your components and removes the mapping between components and styles. This means that when you’re defining your styles, you’re actually creating a normal React component that has your styles attached to it.
    
* [Jest](https://jestjs.io/)/[Enzyme](https://airbnb.io/enzyme/) — a JavaScript Testing Framework and a JavaScript Testing Utility that we will be using to write unit tests for our application. Both have great integration into the React ecosystem and are heavily used in real projects.
    

#### Application Features

In this section we will describe what the features of our application are going to be.

Every time when we plan a new project, we must define certain criteria which will describe some level of completion when met.

In other words, we need to set a limit point which, once reached, will show that our project is completed or at least in its first version. There is a famous saying, that could be matched to the issue with the “never ending” projects:

> “A good plan today is better than a perfect plan tomorrow.**”** — or we may say that a working project today is better than a perfect project tomorrow.

Here is my list with the features I wanted to implement initially:

#### **Header**

* Chat tab — blinking when new message is received until it is read, or when the user is on Settings page
    
* Settings tab
    
* Unread messages counter
    
* Font Awesome icons
    

#### **Chat page**

* Chat area (includes left aligned and right aligned messages)
    
* Message (text, datetime, left or right depending on if it’s received or sent)
    
* Showing the nickname only of the sender
    
* Message sender — input field and button. Input is cleared and focused when button is clicked
    
* Send messages with CTRL+ENTER
    
* Auto scroll to bottom when the chat area is not enough to show all messages
    

#### **Settings page**

* UserProfile component — possibility to change user name
    
* Interface color component — change the color theme of the app
    
* ClockDisplay component — change the time mode 12h or 24h, shown with each message
    
* Send messages with Ctrl+Enter — On/Off
    
* LanguageSwitcher — drop down menu allowing changing the language of the app (currently English and Deutsch are supported)
    
* Reset button — resets all settings stored to local storage
    

**Improvements**  
At the time of writing this, there are still some pending features I would like to implement. Below is the list of all improvements I did or plan to do in future (the ones with the thumb emoji are already implemented):

* Add video chat feature.
    
* ? Added AM/PM time formatting for when 12h mode is selected.
    
* ? Added possibility to send message via ENTER by default. If the setting to send messages with CTRL+ENTER is ON, then this is going to be the only way (except via mouse/touch of course).
    
* ? Optimized for iDevices (media queries).
    
* ? Fix blinking/active class for the Chat tab issue — related to React Router not able to properly re-render connected components h[ttps://github.com/ReactTraining/react-router/blob/master/packages/react-router/docs/guides/blocked-updates.md](https://github.com/ReactTraining/react-router/blob/master/packages/react-router/docs/guides/blocked-updates.md)
    
* ? Clear input field when new message is sent.
    
* ? Auto scroll to bottom main chat area when new messages exceed available space.
    
* ? Prevent ‘doubling messages’ (or multiple messages duplicates when more clients are connected).
    
* ? Add unit tests for the react components.
    
* Add unit tests for redux stuff — reducers, store, action creators.
    
* ? Add media queries for responsiveness — test and adjust on more devices.
    
* ? Add demo to Heroku.
    
* ? Add nice how-to in README.
    
* Add animations for the messages.
    
* Add sounds (with options to turn on/off in settings).
    
* Add more color themes.
    
* Add welcome message (broadcasts when a new user is connected).
    
* ? Add icons (use Font Awesome).
    
* History of all the conversations.
    
* Handle case when socket’s connection state change (visually).
    
* Handle case when there has been a socket error.
    
* Handle case when a very long word (without) spaces is entered and it goes beyond the message background color.
    
* ? Emoticons support — such as :D, :P, :), ;), ?, ❤️, etc.
    
* ? Link Parser — Youtube link (embedded video should appear), link to an image (embedded image should appear), all other links should appear as anchor.
    

When we know the initial plan and the requirements we need to fulfill, we can do our high level analyses. Our app will have two pages, Chat and Settings, accessible via tab controls.

The Chat page will contain the main chat area with the controls needed to send messages (input field and a button).

The Settings page will contain a few controls for selecting the options described above.

With that in mind we can go to the next section where we will create a more detailed plan before the actual implementation.

### More detailed planning

In this section we need to have a deeper look at our application and define what will be the building blocks for it. Since we are going to use React and we know that in the React world the term *component* is widely used, we may refer to our building blocks as components. We will have components responsible for purely visual stuff, as well as such for managing the local storage, for example.

Let’s try to imagine mentally how our app will look in the end and what components it will need. What we already know is this:

#### **Server part**

We will need an HTTP server that will take care of starting the server and handling interactions with Socket.io (sending and receiving messages). Our server logic will be simple enough to live in only one file. You can see the actual implementation [here](https://github.com/mihailgaberov/chat/blob/master/server/index.js).

**Client part**  
Here we need to have all the visual controls, plus means for managing interactions with local storage, where we will save the user preferences, as well as handling of the translations and color themes.

Now is a good moment to point out that for implementing the [translations and theming](https://github.com/mihailgaberov/chat/blob/master/src/utilities/TranslationsProvider.tsx) functionality in the app, I have used [React Context API](https://reactjs.org/docs/context.html). Also, since I knew I would have to deal with [Local Storage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage), I did [another round](https://github.com/mihailgaberov/misc/tree/master/manage-local-storage-with-typescript) of the “*research-test-play”* trip. And the output of it was that I already had a [nice service](https://github.com/mihailgaberov/chat/blob/master/src/utilities/localStorageService.ts), which provides all the functionalities I needed.

Another thing you will notice when looking at the [components](https://github.com/mihailgaberov/chat/tree/master/src/components) folder is that every component has its own directory with a few files in it.

These files serve the following logic:

**index.ts** → entry point, just expose the component itself. This helps for not having to write repeatedly and long import statements. Here is an example:

```js
// Instead of having to write this:
import ChatArea from '../../ChatArea/ChatArea';

// We can have just this:
import ChatArea from '../../ChatArea';
```

[.tsx (ChatAr](https://github.com/mihailgaberov/chat/blob/master/src/components/ChatArea/ChatArea.tsx)ea.tsx) → actual component implementation live here.

**.tes**t.tsx (ChatArea.tes**t.t**sx) **→** unit tests of the component live here.

;.tsx (StyledChatArea.tsx) → CSS styles of the component live here.

The same pattern is used for most of the components, exception are only the *pages*, such as the components which play the role of parents for all the inner parts — [ChatPage](https://github.com/mihailgaberov/chat/tree/master/src/components/pages/Chat) and [SettingsPage](https://github.com/mihailgaberov/chat/tree/master/src/components/pages/Settings).

So, with that said, I think we can see what would be our application structure when we try to “componentize” it. Here a list of the [components](https://github.com/mihailgaberov/chat/tree/master/src/components) I came up with:

![Image](https://cdn-media-1.freecodecamp.org/images/-3vmQYe218gWyJK3nI-6GAtmr1wE2maNBlZ4 align="left")

*Chat application components*

**Note:** all names are a matter of personal choice, feel free to name yours as you wish.

Let me try to give you a bit more detailed explanation for each of them below:

* [AppRouter](https://github.com/mihailgaberov/chat/tree/master/src/components/AppRouter) — contains the main app routing logic. For instance, here we define the app routes by giving them the path and component to load when this path is reached. Uses [React Router](https://reacttraining.com/react-router/web/guides/philosophy) package.
    
* [ChatArea](https://github.com/mihailgaberov/chat/tree/master/src/components/ChatArea) — represents the main chat area, where all the messages are being displayed. It’s responsible also for auto scrolling down when the visible area limit is reached.
    

![Image](https://cdn-media-1.freecodecamp.org/images/gKA17zU8GG2NN-XihkaCM-kGV1sYxTvwXZeW align="left")

*ChatArea component*

* [ClockModeSelector](https://github.com/mihailgaberov/chat/tree/master/src/components/ClockModeSelector) — responsible for displaying controls allowing the user to select the time display mode -12h or 24h. It uses a common component called [RadioGroup](https://github.com/mihailgaberov/chat/tree/master/src/components/common/RadioGroup) (will describe it below) and the Local Storage service to write/read from the browser’s local storage.
    

![Image](https://cdn-media-1.freecodecamp.org/images/2uI0pWruJubJhqy4Ab9IWDgrQc6A5QHaCdR8 align="left")

*ClockModeSelector component*

* [common/RadioGroup](https://github.com/mihailgaberov/chat/tree/master/src/components/common/RadioGroup) — this is a common component, built with the idea to be re-usable all over the app. We use this component in a few other components, such as ClockModeSelector, [ThemeSelector](https://github.com/mihailgaberov/chat/tree/master/src/components/ThemeSelector) and [SendingOptions](https://github.com/mihailgaberov/chat/tree/master/src/components/SendingOptions). It contains logic for displaying two radio buttons with the possibility to pass a callback function which will execute a certain action depending on your needs.
    
* [LanguageSelector](https://github.com/mihailgaberov/chat/tree/master/src/components/LanguageSelector) — responsible for displaying a select input control for choosing the app language. It accepts a function that is coming from the [TranslationsProvider](https://github.com/mihailgaberov/chat/blob/master/src/utilities/TranslationsProvider.tsx) utility and does the actual language change.
    

![Image](https://cdn-media-1.freecodecamp.org/images/ld97BlC9uTxhIOrlzH1a2EKk0xRe-UsrQyI0 align="left")

*LanguageSelector component*

* [Message](https://github.com/mihailgaberov/chat/tree/master/src/components/Message) — this component is responsible for displaying each chat message, sent or received. It includes the nickname of the sender and timestamp showing the time when the message was sent/received. It also provides support for emojis (like ❤️) and links parsing — see the screenshot below.
    

![Image](https://cdn-media-1.freecodecamp.org/images/MHyO9Z78p-SnKs63kXnPVXnDPBT3F2nZRO0p align="left")

*Message component*

* [MessageSender](https://github.com/mihailgaberov/chat/tree/master/src/components/MessageSender) — this is the component that provides the necessary user interface controls for sending messages — a text input field and a Send button. It contains logic for defining the different ways of sending — via click or key press (with ENTER or CTRL+ENTER), as well as clearing the input field when a new message is sent.
    

![Image](https://cdn-media-1.freecodecamp.org/images/Gii8QNN4XmdJe-7kzP8wZ0UYUnLiQJHHMaam align="left")

*MessageSender component*

* [Navigation](https://github.com/mihailgaberov/chat/tree/master/src/components/Navigation) — here lives the implementation of the app navigation. It consists of two tabs — **Chat** and **Settings** and contains logic for connecting to sockets, by sending a R[edux action](https://redux.js.org/basics/actions) when the component is mounted. It manages an [UnreadMessagesCounter](https://github.com/mihailgaberov/chat/tree/master/src/components/UnreadMessagesCounter) component by passing it the count of the currently unread messages (this happens when the user receives a message while being on the Settings page). It also has a logic responsible for making the tab blink when a new message arrives.
    

![Image](https://cdn-media-1.freecodecamp.org/images/M4PlpJ2Fpb02u-eQ19BZZXlvR97aWnqUNJhR align="left")

*Navigation component*

* [Nickname](https://github.com/mihailgaberov/chat/blob/master/src/components/Nickname/) — this is simple component for rendering the nickname of a chat user.
    

![Image](https://cdn-media-1.freecodecamp.org/images/ZxjFRTriSECNzbOYLbtPsEOdiL47bC4nnk-d align="left")

*Nickname component*

* [ResetButton](https://github.com/mihailgaberov/chat/tree/master/src/components/ResetButton) — this will be a simple component, used in the **Settings** page for rendering a Reset button. The function is going to be exactly that — resetting the settings selections that are already saved into the local storage, if any.
    

![Image](https://cdn-media-1.freecodecamp.org/images/T-UIwyCJl3aB89L45JsLOPJ8Ti93Iuwsolcs align="left")

*ResetButton component*

* [SendingOptions](https://github.com/mihailgaberov/chat/tree/master/src/components/SendingOptions) — responsible for displaying options for choosing if a message can be sent via CTRL+ENTER. It works same way as ClockModeSelector component — uses RadioGroup component and accepts a callback function.
    

![Image](https://cdn-media-1.freecodecamp.org/images/tJ98-2kK4eeHuRRK0KhL-GRZYhxz042eJa1G align="left")

*SendingOptions component*

* [ThemeSelector](https://github.com/mihailgaberov/chat/tree/master/src/components/ThemeSelector) — same as the component above. The only difference is that here the user is allowed to select a color theme. In our case the options are only two — light theme or dark theme.
    

![Image](https://cdn-media-1.freecodecamp.org/images/PkC-P1qnRl73Ylz9KivVevkCRvg5mTXuZpMj align="left")

*ThemeSelector component*

* [Timestamp](https://github.com/mihailgaberov/chat/tree/master/src/components/Timestamp) — simple component used for rendering the time of the messages.
    

![Image](https://cdn-media-1.freecodecamp.org/images/R0WmjOMrEEMQCgWGZ6DF7w4qnvc-pT3ioQCp align="left")

*Timestamp component*

* [UnreadMessagesCounter](https://github.com/mihailgaberov/chat/tree/master/src/components/UnreadMessagesCounter) — this is the component I mentioned a little bit earlier. It shows a counter indicating the number of the received, but not yet read, messages. It’s positioned in the navigation area.
    

![Image](https://cdn-media-1.freecodecamp.org/images/t2Q-AcyK0v-7qhgtwYu2hetYzNw76SAwVv01 align="left")

*UnreadMessagesCounter component*

* [UserProfile](https://github.com/mihailgaberov/chat/tree/master/src/components/UserProfile) — this the component responsible for rendering an input field the user can use for changing its user name. It’s saving the new user name into the local storage, using a [debounce](https://lodash.com/docs/4.17.11#debounce) function. This means that the actual triggering of the function is happening some defined time after the user stops typing. It also triggers another Redux action, so we can use the new username in our Redux state.
    
* [pages/ChatPage](https://github.com/mihailgaberov/chat/tree/master/src/components/pages/Chat) — parent component that encloses everything shown on the Chat page.
    
* [pages/SettingsPage](https://github.com/mihailgaberov/chat/tree/master/src/components/pages/Settings) — parent component that encloses everything shown on the Settings page.
    

Everything described above was related to our React components. All of them are responsible for getting some data and displaying it in a proper way. In order to be able to handle this data in a convenient for us way, we use a few more things. Let’s have a look at these things in the sections below.

### Redux State Management

Here we will talk about how our app state is being managed by using Redux and socket middleware.

#### Store

Our [store](https://github.com/mihailgaberov/chat/blob/master/src/store/index.ts) is going to be relatively simple. We will have only two reducers defining a piece of the state reserved for the socket state and for the messages state. This is also where we apply our middleware. If you are familiar with [Redux Saga](https://redux-saga.js.org/) package, you have probably seen this pattern of applying custom middleware when using Redux.

Something like this:

```js
import { createStore, applyMiddleware } from 'redux'
import createSagaMiddleware from 'redux-saga'
import reducer from './reducers'
import mySaga from './sagas'
// create the saga middleware
const sagaMiddleware = createSagaMiddleware()
// mount it on the Store
const store = createStore(
  reducer,
  applyMiddleware(sagaMiddleware)
)
```

But in our case it would be like this:

```python
import { createStore, combineReducers, applyMiddleware, compose } from 'redux';
import socketReducer from './socket/reducer';
import messageReducer from './message/reducer';
import socketMiddleware from './socket/middleware';
const rootReducer = combineReducers({
  socketState: socketReducer,
  messageState: messageReducer
});
// @ts-ignore
const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
const index = {
  ...createStore(rootReducer, composeEnhancers(applyMiddleware(socketMiddleware)))
};
export default index;
```

#### Message

After defining our store, it’s time to see how are we going to handle the messaging in Redux. We have defined our actions [here](https://github.com/mihailgaberov/chat/blob/master/src/store/message/actions/index.ts) and our messageReducer [here](https://github.com/mihailgaberov/chat/blob/master/src/store/message/reducer/index.ts).

* **Actions** — here we define the main actions needed for sending and receiving messages, as well as changing the user name.
    
* **Reducer** — here is where our messageReducer function lives and where we define what happens when one of the actions above is dispatched.
    

#### Socket

We follow the same logic as above here. We have our [socket actions](https://github.com/mihailgaberov/chat/blob/master/src/store/socket/actions/index.ts), the [middleware](https://github.com/mihailgaberov/chat/tree/master/src/store/socket/middleware) I mentioned above, and the [socketReducer](https://github.com/mihailgaberov/chat/blob/master/src/store/socket/reducer/index.ts).

* **Actions** — contains actions for connecting the socket (the one dispatched from the Navigation component in the beginning when the application is started) and one for when the connection status is changed, i.e. showing if we are connected or not.
    
* **Middleware** — contains implementation of a simple socket middleware, which provides us with the minimum functionality we need in our chat app.
    
* **Reducer** — here is where our socketReducer function lives and where we define what happens when one of the actions above is dispatched.
    

### Theming

In order to implement the possibility for setting different color themes in our application and considering the fact we are using styled-components, I used a [ThemeProvider](https://www.styled-components.com/docs/advanced) — component provided by them. [Here](https://github.com/mihailgaberov/chat/blob/master/src/theme/index.ts) is the implementation that includes defining objects with custom colors used in the themes.

The logic behind applying the selected color theme resides [here](https://github.com/mihailgaberov/chat/blob/master/src/utilities/TranslationsProvider.tsx). Ideally the containing component should be named something different than *TranslationsProvider,* as it doesn’t handle only the translations, as we see. We could add this to the list of future improvements/refactoring.

Here is how the existing color themes look:

![Image](https://cdn-media-1.freecodecamp.org/images/tFLYC4dB7W8z0EcZrxzuBNSGlqvEkfRD7f9G align="left")

### Utilities

In almost every software project, at certain point, the need of common reusable functions emerges. This the moment when developers usually create a common shared file or files, containing such helpers functions. In our case this would be **/utilities** folder that currently contains four files. I will go through each of them below and explain the logic behind my decision to create it and put it there:

* [common.ts](https://github.com/mihailgaberov/chat/blob/master/src/utilities/common.ts) — here is the place where I decide to put such common helper functions, which are supposed to be easily used where needed in the whole application. In this specific case you will find four functions used for time formatting, and a helper for defining the active page and for scrolling an element to bottom.
    
* [localStorageService.ts](https://github.com/mihailgaberov/chat/blob/master/src/utilities/localStorageService.ts) — I have already mention this service in the [first part](https://medium.com/p/1c9d50897b/edit) of this tutorial. Here is where all methods for manipulating the local storage live.
    
* [TranslationsProvider.tsx](https://github.com/mihailgaberov/chat/blob/master/src/utilities/TranslationsProvider.tsx) — this component was also mentioned multiple times, but for the sake of clarity I will mention it again here. It contains the logic for providing translations and color theme in the app.
    
* [withTranslations.tsx](https://github.com/mihailgaberov/chat/blob/master/src/utilities/withTranslations.tsx) — this is a [higher-order component (HOC)](https://tylermcginnis.com/react-higher-order-components/) which is responsible for attaching the application context (containing the translations and themes themselves) to any component being wrapped by it.
    

Here is an example of how is it used:

```python
export default withTranslations(SettingsPage as React.FunctionComponent);
```

We have walked a long way to here and we still haven’t started with the actual implementation.

That is a vivid pointer for us to show how important and extensive the planning phase of a project could be.

Let’s jump now to the implementation phase in the next section.

### Implementation

If you reached this point of the tutorial, you should have a very clear idea of what are we going to build. Here, we are about to find out how are we going to do it.

#### Starting small

As with any other project we should strive to start with small, incremental chunks and build on them. In our case I have decided to start first with building the header navigation. The reason for that was that I wanted to have the router and the navigation controls in place, so I could easily navigate through the tabs while developing and testing.

#### Settings page

After I had finished with the header and navigation parts, I decided to jump to the settings page first. Again, my reasoning was very simple — I wanted to build first what I was going to use in the Chat page. In other words I wanted to be able to customize my chat area, messages, ways of sending and so on, before implementing them.

So I started building component by component as I described them in the [previous](https://mihail-gaberov.eu/how-i-build-chat-app-with-react-and-typescript-part3/) section. Once I had the full Settings page finished, I was able to go and start implementing the Chat page components. But before that, I had to take care of the supporting stuff — integrating with [local storage](https://github.com/mihailgaberov/chat/blob/master/src/utilities/localStorageService.ts) and adding [translations mechanism](https://github.com/mihailgaberov/chat/blob/master/src/utilities/TranslationsProvider.tsx).

#### Chat page

After I have done all from above, the implementation of the Chat page and its components was fairly easy. I had to take care of the visual part manly and make the integration with the Redux store. As you [already saw](https://github.com/mihailgaberov/chat/blob/master/src/components/pages/Chat/ChatPage.tsx), I had to implement only two components which are shown and used on the Chat page — ChatArea and MessageSender.

### Adding improvements

I want to say a few words here regarding the app improvements we did or will do in the future. Usually when we have a new requirement (let’s call it “requirement”, that makes is sound closer to what would be in a real project), it is again a very good idea to do some initial research, instead of jumping directly into implementation. You will be surprised how many solutions are already out there, waiting for us to use them.

In other words, we don’t have to invent the wheel again.

This is what I did when I started thinking about adding support for emoticons or link parsing. It turned out that there are already solutions I could use with a little tweaking from my side, just to make them fit well in my project.

Here are the links to the packages I used:

* [https://www.npmjs.com/package/linkifyjs](https://www.npmjs.com/package/linkifyjs)
    
* [https://docs.microlink.io/sdk/getting-started/react/](https://docs.microlink.io/sdk/getting-started/react/)
    
* [https://www.npmjs.com/package/react-emojione](https://www.npmjs.com/package/react-emojione)
    
* [https://www.npmjs.com/package/get-urls](https://www.npmjs.com/package/get-urls)
    

And [here](https://github.com/mihailgaberov/chat/blob/master/src/components/Message/Message.tsx) you can see how I used them in our chat app.

### Deploying to Heroku

I have written [another article](https://mihail-gaberov.eu/creating-twitter-bot/) in the past. It was about totally different subject, but there is a part exactly related to how to deploy an app to Heroku. You might find it useful to check it out.

For deploying our chat application to [Heroku](https://herokuapp.com/), I will assume you have already an account and can easily follow the steps below:

1. `npm build` to build the project to `build` folder.
    
2. Add `build` folder to Git to make sure it will be committed.
    
3. Make sure that express server loads static resources from it.
    
4. Commit all: `git commit -m 'Deploy to Heroky'`.
    
5. Run `git push heroku master`.
    
6. Open the app from the given URL (in my case: [mihails-chat.herokuapp.com](https://mihails-chat.herokuapp.com/#/chat)).
    

### Future (possible) plans

At the time of writing this I was thinking it might be very interesting to try building the same application with the other super famous UI library on the market — [Angular](https://angular.io/). I still think it will be worth it, but I am not sure whether I will have the time and the power to do it ?.

In any case, what I am thinking about it as a pure, technical comparison of two major UI libraries from the developer’s point of view.

If I do it, I will make sure you know it!

Thanks for reading. You can read more of my articles at [mihail-gaberov.eu](https://mihail-gaberov.eu/how-i-build-chat-app-with-react-and-typescript-part1/).
