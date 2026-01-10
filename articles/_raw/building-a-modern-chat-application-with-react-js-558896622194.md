---
title: How to build a modern chat application with React.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-13T19:16:43.000Z'
originalURL: https://freecodecamp.org/news/building-a-modern-chat-application-with-react-js-558896622194
coverImage: https://cdn-media-1.freecodecamp.org/images/1*g_B4JNulmfXSj0AyEjImyA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Samuel Omole

  In this tutorial, I will guide you to build your own group chat application using
  React, React Router, and CometChat Pro. Yes, rather than roll out our own server,
  we will instead use CometChat Pro to handle the real-time sending and ...'
---

By Samuel Omole

In this tutorial, I will guide you to build your own group chat application using React, React Router, and [CometChat Pro](https://www.cometchat.com/pro). Yes, rather than roll out our own server, we will instead use CometChat Pro to handle the real-time sending and receiving of chat messages.

When you’re done, you should have a functional chat application that looks something like this (of course, you’re welcome to tweak and experiment with things as you go along):

![Image](https://cdn-media-1.freecodecamp.org/images/uUjaJRgeq1EtbCKptPuNQ2zKMSk4lfMfeQLs)

![Image](https://cdn-media-1.freecodecamp.org/images/BMXCWPYnepUrYQ31dqqWXygDARpYOk1Ky0lS)

I have structured this tutorial as a series of steps to make it easy to follow along. If you’d just like to check out the code, [click here](https://github.com/cometchat-pro-samples/react-comet-chat-app).

### Setting up the project

Before we go too far, we must first set up our React project. To do this, we’ll use a lesser-known gem called Create React App.

The best thing? Because you have npm installed, you can use npx to install and run create-react-app in one step:

`npx create-react-app chatapp // note: npm v5.2+`

After running this command, a new folder called “chatapp” will be created with the following structure:

![Image](https://cdn-media-1.freecodecamp.org/images/IKF841Qr62aFXMFI5C9qQHiO0xH-nW0taEK1)

In addition, to React, we will also need to install React Router and CometChat Pro SDK. To do this, head to the chatapp directory and run:

`npm install react-router-dom @cometchat-pro/chat --save`

### Add React Router

In the end, our application will have two pages — one called `Login` where the user will log in, and another called `Groupchat` where we will render the chat room. We will use React Router to route users to the page they need.

To setup React Router, we must first import the `Router` _wrapper_ component in our index.js file. I call it a wrapper component because we wrap our `App` inside the `Router` component.

Replace index.js with this snippet:

```js
import React from 'react';
import { BrowserRouter as Router } from 'react-router-dom'; // added
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
ReactDOM.render(
  <Router>
    <App />
  </Router>
  , document.getElementById('root'));
```

`index.js` is the entry point for our application. Its only real job is to render our React application. Most of our “real” logic happens in a file called App.js, which we will modify next.

In App.js, we must import additional React Router dependencies which will enable us to render different components depending on what route the user has loaded. For example, if the user goes to the “/login” route, we should render the Login component. Likewise, if the user goes to the “/chat” route, we should render the `Groupchat` component:

```js
import React, { Component } from "react";
import { Route, Redirect, Switch } from "react-router-dom";
import "./App.css";
// the below components will be created shortly
import Login from "./components/Login";
import Groupchat from "./components/Groupchat";
class App extends Component {
  constructor(props) {
    super(props);
  }
render() {
    return (
      <Switch>
        <Redirect exact from="/" to="/login" />
        <Route path="/login" component={Login} />
        <Route path="/chat" component={Groupchat} />
      </Switch>
    );
  }
}
export default App;
```

If you try to run this code it will definitely throw some errors because we haven’t made the `Login` and `Groupchat` components. Let’s do that now.

### Create the Login component

To keep our project nice and tidy, create a folder called `components` to hold our custom components.

Then, in that newly-created folder, create a file called Login.js with the following code:

```js
import React from "react";
class Login extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
    };
  }
  render() {
    return ( 
      <div className="App">
        <h1>Login</h1>
      </div>
    );
  }
}
export default Login;
```

All we’re doing here is exporting a component with the heading text, “Login”. We’ll flesh this component out soon but for right now, we are merely creating boilerplate.

### Create the Groupchat component

In the same components folder, create a new component called Groupchat.js:

```js
import React from "react";
class Groupchat extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    return <div className="chatWindow" />;
  }
}
export default Groupchat;
```

As we progress through the tutorial, we will develop this humble component into the core of our chat application.

With the `Groupchat` and `Login` components in place, you should be able to run the application without an error. Open the app on localhost and navigate to localhost:3000/login and then localhost:3000/chat to see the components in action.

### Create the CometChat APP ID and API key

Like I mentioned at the beginning of the tutorial, we won’t be rolling out our own server in this tutorial. Instead, we’ll be using a hosted service of [CometChat Pro](http://cometchat.com/pro).

Before we can connect to CometChat, we must first create a CometChat application from the dashboard:

![Image](https://cdn-media-1.freecodecamp.org/images/1uiJPWklG1WfpuVdMSYwC6FBajscCNoNR-fw)

Once your application has been created, hit “Explore” then head to the “API Keys” tab:

![Image](https://cdn-media-1.freecodecamp.org/images/0I2N1oshD4NW7urTY4hLWXYo5mSDdxS4JZ4Y)

Click “Create API key” and fill in the form, choosing Auth Only scope. From the table, you can note your application ID and application key, we’ll need these shortly.

### Create the CometChat group ID

While we have the dashboard open, let’s also create a _group_. Normally you’d do this with code (for example, you might allow the user to create a custom chat group for their team or project through your app) but for learning and testing, the dashboard is fine.

Head to the “Groups” tab and create a new group called testgroup:

![Image](https://cdn-media-1.freecodecamp.org/images/GeeNNciJ-UnawrFegFOX04dsAzhii7V3GPeE)

Like last time, you’ll be taken back to a table where you can note the group ID:

![Image](https://cdn-media-1.freecodecamp.org/images/7IQuc9f-PA6USd3CHkZmuekCSwZiyiTphEUG)

Take note as we’ll need this in the next step.

### Create the configuration file

To make it easy to reference our configuration, create a new file called config.js and paste your credentials:

```js
export default {
  appId: "", //Enter your App ID
  apiKey: "", //Enter your API KEY
  GUID: "", // Enter your group UID
};
```

You can now close the dashboard. Once you setup CometChat, all interaction happens through code.

### Create a CometChat Manager class

One of the beautiful things about React is that it lends itself to a separation of concerns. Our components can focus purely on presentation while we can create other modules to handle things like data fetching and state management.

To really take advantage of this, let’s create a new folder called “lib” and in that new folder, a file called chat.js. This is where all of our interaction with CometChat will take place:

```js
import { CometChat } from "@cometchat-pro/chat";
import config from "../config";
export default class CCManager {
  static LISTENER_KEY_MESSAGE = "msglistener";
  static appId = config.appId;
  static apiKey = config.apiKey;
  static LISTENER_KEY_GROUP = "grouplistener";
  static init() {
    return CometChat.init(CCManager.appId);
  }
  static getTextMessage(uid, text, msgType) {
    if (msgType === "user") {
      return new CometChat.TextMessage(
        uid,
        text,
        CometChat.MESSAGE_TYPE.TEXT,
        CometChat.RECEIVER_TYPE.USER
      );
    } else {
      return new CometChat.TextMessage(
        uid,
        text,
        CometChat.MESSAGE_TYPE.TEXT,
        CometChat.RECEIVER_TYPE.GROUP
      );
    }
  }
  static getLoggedinUser() {
    return CometChat.getLoggedinUser();
  }
  static login(UID) {
    return CometChat.login(UID, this.apiKey);
  }
  static getGroupMessages(GUID, callback, limit = 30) {
    const messagesRequest = new CometChat.MessagesRequestBuilder()
      .setGUID(GUID)
      .setLimit(limit)
      .build();
    callback();
    return messagesRequest.fetchPrevious();
  }
  static sendGroupMessage(UID, message) {
    const textMessage = this.getTextMessage(UID, message, "group");
    return CometChat.sendMessage(textMessage);
  }
  static joinGroup(GUID) {
    return CometChat.joinGroup(GUID, CometChat.GROUP_TYPE.PUBLIC, "");
  }
  static addMessageListener(callback) {
    CometChat.addMessageListener(
      this.LISTENER_KEY_MESSAGE,
      new CometChat.MessageListener({
        onTextMessageReceived: textMessage => {
          callback(textMessage);
        }
      })
    );
  }
}

```

Aside from allowing us to create a separation of concerns, presenting the code like this also makes it easier to digest.

Let me explain some important parts of this module, starting from the top:

* `LISTENER_KEY_MESSAGE` – This is required by the message listener.
* `init()` – This is required to be called only once throughout the lifecycle of the application, it calls the CometChat `init` method with the appID.
* `getTextMessage(uid, text, msgType)` – it creates the message object based on `CometChat.TextMessage`method, it accepts the UID (GUID in our case) and the text message to send.
* `getLoggedInUser()` – it’s used to get the currently logged in user.
* `login()` – it’s used to log in a user based on the CometChat.login method, it takes in the UID (GUID in our case) and the apiKey.
* `getGroupMessages(GUID, callback, limit = 30)` – this is used to get the previous group messages from CometChat using the `CometChat.MessagesRequestBuilder()` method that takes in the GUID and limit as parameters.
* `sendGroupMessage(UID, message)`– this is used to send messages using the `CometChat.sendMessage()` method and it accepts the GUID and message as parameters.
* `joinGroup(GUID)` – It’s used to join a chosen group using a GUID.
* `addMessageListener(callback)` – Uses the `CometChat.addMessageListener()` to listen to messages (did I mention this is called in real-time?), it requires the `LISTENER_KEY_MESSAGE` as a parameter and also a callback that is called when a message is received.

There’s nothing specific to this application here. You could well take this module, expand it if needed, and import it into another project. Generally, though, this is just a thin wrapper around the SDK.

### Update the login component

With all our configuration and chat code in place, we can now rapidly build out the UI starting with the `Login` component.

Just to remind you, this is what the Login component will look like:

![Image](https://cdn-media-1.freecodecamp.org/images/fm3GKd-dBpRogU66edgVDEx-VbBk2EFF0mdO)

As you can see, its main function is to ask the user for their name. Once a name is supplied, we render the `Groupchat` component.

Replace `Login.js` with:

```js
import React from "react";
import { Redirect } from "react-router-dom";
import chat from "../lib/chat";
import spinner from "../logo.svg";
class Login extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      username: "",
      isAuthenticated: false,
      user: null,
      isSubmitting: false,
      errorMessage: ""
    };
  }
  onSubmit = e => {
    if (this.state.username !== "") {
      e.preventDefault();
      this.login();
    }
  };
  login = () => {
    this.toggleIsSubmitting();
    chat
    .login(this.state.username)
    .then(user => {
      this.setState({
        user,
        isAuthenticated: true
      });
    })
    .catch(error => {
      this.setState({
        errorMessage: "Please enter a valid username"
      });
      this.toggleIsSubmitting();
      console.log(error);
    });
  };
  toggleIsSubmitting = () => {
    this.setState(prevState => ({
      isSubmitting: !prevState.isSubmitting
    }));
  };
  handleInputChange = e => {
    this.setState({
      username: e.target.value
    });
  };
  render() {
    if (this.state.isAuthenticated) {
      return (
        <Redirect
          to={{
            pathname: "/chat",
            state: { user: this.state.user }
          }}
        />
      );
    }
    return (
      <div className="App">
        <h1>COMETCHAT</h1>
        <p>Create an account through your CometChat dashboard or login with one of our test users, superhero1, superhero2, etc.</p>
        <form className="form" onSubmit={this.onSubmit}>
          <input onChange={this.handleInputChange} type="text" />
          <span className="error">{this.state.errorMessage}</span>
          {this.state.isSubmitting ? (
            <img src={spinner} alt="Spinner component" className="App-logo" />
          ) : (
            <input
              type="submit"
              disabled={this.state.username === ""}
              value="LOGIN"
            />
          )}
        </form>
      </div>
    );
  }
}
export default Login;
```

Aside from the presentational HTML, most code here is dedicated to handling a [React form](https://reactjs.org/docs/forms.html).

### Update the Groupchat component

The Groupchat component has a lot more responsibility than the Login component. As a quick reminder, this is what it will look like:

![Image](https://cdn-media-1.freecodecamp.org/images/UazFSe6wyPti-CxoNLE5ERziJt4Pmqt1ucro)

For the most part, the `Groupchat` component’s job is to bridge the chat lib module and the UI we’ll present to the user. For example, when a user sends a message, we call `chat.sendMessage` and as new messages trickle in, a callback function is called:

```js
import React from "react";
import { Redirect } from "react-router-dom";
import chat from "../lib/chat";
import config from "../config";
class Groupchat extends React.Component {
  constructor(props) {
    super(props);
this.state = {
      receiverID: "",
      messageText: null,
      groupMessage: [],
      user: {},
      isAuthenticated: true
    };
this.GUID = config.GUID;
  }
sendMessage = () => {
    chat.sendGroupMessage(this.GUID, this.state.messageText).then(
      message => {
        console.log("Message sent successfully:", message);
        this.setState({ messageText: null });
      },
      error => {
        if (error.code === "ERR_NOT_A_MEMBER") {
          chat.joinGroup(this.GUID).then(response => {
            this.sendMessage();
          });
        }
      }
    );
  };
scrollToBottom = () => {
    const chat = document.getElementById("chatList");
    chat.scrollTop = chat.scrollHeight;
  };
handleSubmit = event => {
    event.preventDefault();
    this.sendMessage();
    event.target.reset();
  };
handleChange = event => {
    this.setState({ messageText: event.target.value });
  };
getUser = () => {
    chat
      .getLoggedinUser()
      .then(user => {
        console.log("user details:", { user });
        this.setState({ user });
      })
      .catch(({ error }) => {
        if (error.code === "USER_NOT_LOGED_IN") {
          this.setState({
            isAuthenticated: false
          });
        }
      });
  };
messageListener = () => {
    chat.addMessageListener((data, error) => {
      if (error) return console.log(`error: ${error}`);
      this.setState(
        prevState => ({
          groupMessage: [...prevState.groupMessage, data]
        }),
        () => {
          this.scrollToBottom();
        }
      );
    });
  };
componentDidMount() {
    this.getUser();
    this.messageListener();
    // chat.joinGroup(this.GUID)
  }
render() {
    const { isAuthenticated } = this.state;
    if (!isAuthenticated) {
      return <Redirect to="/" />;
    }
    return (
      <div className="chatWindow">
        <ul className="chat" id="chatList">
          {this.state.groupMessage.map(data => (
            <div key={data.id}>
              {this.state.user.uid === data.sender.uid ? (
                <li className="self">
                  <div className="msg">
                    <p>{data.sender.uid}</p>
                    <div className="message"> {data.data.text}</div>
                  </div>
                </li>
              ) : (
                <li className="other">
                  <div className="msg">
                    <p>{data.sender.uid}</p>
                   <div className="message"> {data.data.text} </div>
                  </div>
                </li>
              )}
            </div>
          ))}
        </ul>
        <div className="chatInputWrapper">
          <form onSubmit={this.handleSubmit}>
            <input
              className="textarea input"
              type="text"
              placeholder="Enter your message..."
              onChange={this.handleChange}
            />
          </form>
        </div>
      </div>
    );
  }
}
export default Groupchat;<
```

There’s a lot to digest here, so let’s break the important parts down:

* `sendMessage()` – This function handles sending a message to the group, passing the GUID and the text message that is stored is in the component’s state. If the user is not part of the group we then make a request to join the group and then call the sendMessage function again.
* `scrollToBottom()` – This function will be used as a callback function for the message listener, it just makes sure that the latest messages are shown in the chat list.
* `handleSubmit()` – This calls the sendMessage function.
* `getUser()` – This calls the chat.getLoggedInUser() method and stores the user object in the component’s state.
* `messageListener()` – This calls the chat.addMessageListener() function and appends every new message received to the `groupMessage` array which is stored in the component’s state and rendered in the app.
* `componentDidMount()` – This calls the getUser and messageListener functions.

Finally, we render a class depending on if the message is ours or someone else’s. This way, we can apply different styles which is the topic of the next section.

### Update the styles

If you were to run the application now, it would work but with no CSS to speak of thus far, it would look quite uh, odd.

This isn’t a tutorial about CSS so I won’t explain it in any detail, but to help you follow along, you can paste the following into your App.css file (you will have one already because it was generated by `create-react-app` earlier):

```css
.App {
  text-align: center;
  display: flex;
  width: 100%;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 50vh;
}
.App p{
  font-size: 12px;
  width: 50%;
}
.App-logo {
  animation: App-logo-spin infinite 0.5s linear;
  height: 10vmin;
}
.form {
  display: flex;
  flex-direction: column;
}
.form input[type="text"] {
  width: 300px;
  height: 30px;
  margin-bottom: 10px;
}
.form input[type="submit"] {
  padding: 5px;
  height: 30px;
  border: none;
  background-color: #187dbc;
  color: #fff;
}
.form input[type="submit"]:hover {
  border: #fff;
  cursor: pointer;
  background-color: #000;
  color: #fff;
}
.error{
  color: red;
  font-size: 10px;
  text-align: center;
}
@keyframes App-logo-spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}
.message {
  font-size: 15px !important;
}
body {
  background-color: #f5f5f5;
  font: 600 18px/1.5 -apple-system, BlinkMacSystemFont, "Segoe UI", Lato,
    Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif;
  color: #4b4b4b;
}
.container {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-template-rows: repeat(1, 50px);
  grid-gap: 3px;
  margin-top: 15px;
}
.group {
  background: #4eb5e5;
  grid-column-start: 1;
  grid-column-end: 2;
  grid-row-start: 1;
  grid-row-end: 190;
  border-radius: 5px;
}
.chatWindow {
  display: grid;
  grid-column-start: 2;
  grid-column-end: 9;
  grid-row-start: 1;
  grid-row-end: 190;
  background: rgb(233, 229, 229);
  border-radius: 5px;
}
.chatInputWrapper {
  display: grid;
  grid-row-start: 190;
  grid-row-end: 190;
}
::-webkit-scrollbar {
  display: none;
}
/* M E S S A G E S */
.chat {
  list-style: none;
  background: none;
  margin: 0;
  padding: 0 0 50px 0;
  margin-top: 60px;
  margin-bottom: 10px;
  max-height: 400px;
  overflow: scroll;
  scroll-behavior: smooth;
}
.chat li {
  padding: 0.5rem;
  overflow: hidden;
  display: flex;
}
.chat .avatar {
  position: relative;
  display: block;
  z-index: 2;
}
.chat .avatar img {
  background-color: rgba(255, 255, 255, 0.9);
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
}
.chat .uid img {
  background-color: rgba(255, 255, 255, 0.9);
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
}
.chat .day {
  position: relative;
  display: block;
  text-align: center;
  color: #c0c0c0;
  height: 20px;
  text-shadow: 7px 0px 0px #e5e5e5, 6px 0px 0px #e5e5e5, 5px 0px 0px #e5e5e5,
    4px 0px 0px #e5e5e5, 3px 0px 0px #e5e5e5, 2px 0px 0px #e5e5e5,
    1px 0px 0px #e5e5e5, 1px 0px 0px #e5e5e5, 0px 0px 0px #e5e5e5,
    -1px 0px 0px #e5e5e5, -2px 0px 0px #e5e5e5, -3px 0px 0px #e5e5e5,
    -4px 0px 0px #e5e5e5, -5px 0px 0px #e5e5e5, -6px 0px 0px #e5e5e5,
    -7px 0px 0px #e5e5e5;
  box-shadow: inset 20px 0px 0px #e5e5e5, inset -20px 0px 0px #e5e5e5,
    inset 0px -2px 0px #d7d7d7;
  line-height: 38px;
  margin-top: 5px;
  margin-bottom: 20px;
  cursor: default;
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
}
.other .msg {
  order: 1;
  border-top-left-radius: 0px;
  box-shadow: -1px 2px 0px #d4d4d4;
}
.other:before {
  content: "";
  position: relative;
  top: 0px;
  right: 0px;
  left: 40px;
  width: 0px;
  height: 0px;
  border: 5px solid #fff;
  border-left-color: transparent;
  border-bottom-color: transparent;
}
.self {
  justify-content: flex-end;
  align-items: flex-end;
}
.self .msg {
  order: 1;
  border-bottom-right-radius: 0px;
  box-shadow: 1px 2px 0px #d4d4d4;
}
.self .avatar {
  order: 2;
}
.self .avatar:after {
  content: "";
  position: relative;
  display: inline-block;
  bottom: 19px;
  right: 0px;
  width: 0px;
  height: 0px;
  border: 5px solid #fff;
  border-right-color: transparent;
  border-top-color: transparent;
  box-shadow: 0px 2px 0px #d4d4d4;
}
.msg {
  background: white;
  min-width: fit-content;
  padding: 10px;
  border-radius: 10px;
  box-shadow: 0px 2px 0px rgba(0, 0, 0, 0.07);
}
.msg p {
  font-size: 0.8rem;
  margin: 0 0 0.2rem 0;
  color: rgb(81, 84, 255);
}
.msg img {
  position: relative;
  display: block;
  width: 450px;
  border-radius: 5px;
  box-shadow: 0px 0px 3px #eee;
  transition: all 0.4s cubic-bezier(0.565, -0.26, 0.255, 1.41);
  cursor: default;
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
}
@media screen and (max-width: 800px) {
  .msg img {
    width: 300px;
  }
}
@media screen and (max-width: 550px) {
  .msg img {
    width: 200px;
  }
}
.msg time {
  font-size: 0.7rem;
  color: #ccc;
  margin-top: 3px;
  float: right;
  cursor: default;
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
}
.msg time:before {
  content: " ";
  color: #ddd;
  font-family: FontAwesome;
  display: inline-block;
  margin-right: 4px;
}
::-webkit-scrollbar {
  min-width: 12px;
  width: 12px;
  max-width: 12px;
  min-height: 12px;
  height: 12px;
  max-height: 12px;
  background: #e5e5e5;
}
::-webkit-scrollbar-thumb {
  background: rgb(48, 87, 158);
  border: none;
  border-radius: 100px;
  border: solid 3px #e5e5e5;
  box-shadow: inset 0px 0px 3px #999;
}
::-webkit-scrollbar-thumb:hover {
  background: #b0b0b0;
  box-shadow: inset 0px 0px 3px #888;
}
::-webkit-scrollbar-thumb:active {
  background: #aaa;
  box-shadow: inset 0px 0px 3px #7f7f7f;
}
::-webkit-scrollbar-button {
  display: block;
  height: 26px;
}
/* T Y P E */
input.textarea {
  width: 100%;
  height: 50px;
  background: #fafafa;
  border: none;
  outline: none;
  padding-left: 55px;
  padding-right: 55px;
  color: #666;
  font-weight: 400;
}
```

### Conclusion

Run the application with `npm start` and low and behold, your chat application is complete. At least, the basic functionality is in place. With CometChat, you could easily expand the app to include a “who’s online list”, direct messages, media messages, and a bunch of other features.

_This article was originally published on Cometchat’s [blog](https://www.cometchat.com/tutorials/build-a-modern-chat-application-with-react)._

