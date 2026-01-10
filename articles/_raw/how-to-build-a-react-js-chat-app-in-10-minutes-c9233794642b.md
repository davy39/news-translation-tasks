---
title: Learn to build a React chat app in 10 minutes - React JS tutorial
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-19T15:25:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-react-js-chat-app-in-10-minutes-c9233794642b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*SUeSr13iO7yJfIf4ipaeFg.png
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: React
  slug: react
seo_title: null
seo_desc: 'By Per Harald Borgen


  _Click here to get to the full course this article is based on._

  In this article, I’ll show you the easiest way possible to create a chat application
  using React.js. It’ll be done entirely without server-side code, as we’ll let ...'
---

By Per Harald Borgen

![Image](https://cdn-media-1.freecodecamp.org/images/1*NE_xQlf9WZkO3LTpxG5TNA.png)
_[Click here to get to the full course](https://scrimba.com/g/greactchatkit?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=greactchatkit_10_minute_article) this article is based on._

In this article, I’ll show you the easiest way possible to create a chat application using React.js. It’ll be done entirely without server-side code, as we’ll let the [Chatkit API](https://pusher.com/chatkit) handle the back-end.

I’m assuming that you know basic JavaScript and that you’ve encountered a little bit of React.js before. Other than that, there are no prerequisites.

Note: I’ve also created a free full-length course on [how to create a React.js chat app here:](https://scrimba.com/g/greactchatkit?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=greactchatkit_10_minute_article)

If you follow along with this tutorial you’ll end up with your very own chat application at the end, which you then can build further upon if you’d like to.

Let’s get started!

### Step 1: Breaking the UI into components

React is built around components, so the first thing you want to do when creating an app is to break its UI into components.

Let’s start by drawing a rectangle around the entire app. This is your root component and the common ancestor for all other components. Let’s call it `App`:

![Image](https://cdn-media-1.freecodecamp.org/images/1*66jz6LtljJtOPDouK9PmYA.png)

Once you’ve defined your root component, you need to ask yourself the following question:

Which direct children does this component have?

In our case, it makes sense to give it three child components, which we’ll call the following:

* `Title`
* `MessagesList`
* `SendMessageForm`

Let’s draw a rectangle for each of these:

![Image](https://cdn-media-1.freecodecamp.org/images/1*SUeSr13iO7yJfIf4ipaeFg.png)

This gives us a nice overview of the different components and the architecture behind our app.

We could have continued asking ourselves which children these components again have. Thus we could have broken the UI into even more components, for example through turning each of the messages into their own components. However, we’ll stop here for the sake of simplicity.

### Step 2: Setting up the codebase

Now we’ll need to setup our repository. We’ll use the simplest structure possible: an *index.html *file with links to a JavaScript file and a stylesheet. We’re also importing the Chatkit SDK and Babel, which is used to transform our JSX:

![Image](https://cdn-media-1.freecodecamp.org/images/1*YCcPOlQGBk-dP-UQnyLEMA.png)

[Here’s a Scrimba playground](https://scrimba.com/c/c7aW2hd?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=greactchatkit_10_minute_article) with the final code for the tutorial. I’d recommend you to open it up in a new tab and play around with it whenever you feel confused.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xmr7Z2oR1PwJvLq2sHuZbQ.png)

Alternatively, you can download the Scrimba project as a .zip file and run a simple [server to get it up and running locally.](https://gist.github.com/willurd/5720255)

### Step 3: Creating the root component

With the repository in place, we’re able to start writing some React code, which we’ll do inside the *index.js *file.

Let’s start with the main component, `App`. This will be our only “smart” component, as it’ll handle the data and the connection with the API. Here’s the basic setup for it (before we’ve added any logic):

```jsx
    class App extends React.Component {
      
      render() {
        return (
          <div className="app">
            <Title />
            <MessageList />
            <SendMessageForm />
         </div>
        )
      }
    }

```

As you can see, it simply renders out three children: the `<Title>`,`<MessageList>`, and the `<SendMessageForm>` components.

We’re going to make it a bit more complex though, as the chat messages will need to be stored inside the _state_ of this `App` component. This will enable us to access the messages through `this.state.messages`, and thus pass them around to other components.

We’ll begin with using dummy data so that we can understand the data flow of the app. Then we’ll swap this out with real data from the [Chatkit](https://pusher.com/chatkit) API later on.

Let’s create a `DUMMY_DATA` variable:

```jsx
    const DUMMY_DATA = [
      {
        senderId: "perborgen",
        text: "who'll win?"
      },
      {
        senderId: "janedoe",
        text: "who'll win?"
      }
    ]

```

Then we’ll add this data to the state of `App` and pass it down to the `MessageList` component as a prop.

```jsx
    class App extends React.Component {
      
      constructor() {
        super()
        this.state = {
           messages: DUMMY_DATA
        }
      }
      
      render() {
        return (
          <div className="app">
            <MessageList messages={this.state.messages}/>
            <SendMessageForm />
         </div>
        )
      }
    }

```

Here, we’re initializing the state in the `constructor` and we’re also passing `this.state.messages` down to `MessageList`.

Note that we’re calling `super()` in the constructor. You must do that if you want to create a stateful component.

### Step 4: Rendering dummy messages

Let’s see how we can render these messages out in the `MessageList` component. Here’s how it looks:

```jsx
    class MessageList extends React.Component {
      render() {
        return (
          <ul className="message-list">                 
            {this.props.messages.map(message => {
              return (
               <li key={message.id}>
                 <div>
                   {message.senderId}
                 </div>
                 <div>
                   {message.text}
                 </div>
               </li>
             )
           })}
         </ul>
        )
      }
    }

```

This is a so-called stupid component. It takes one prop, `messages`, which contains an array of objects. And then we’re simply rendering out the `text` and `senderId` properties from the objects.

With our dummy data flowing into this component, it will render the following:

![Image](https://cdn-media-1.freecodecamp.org/images/1*Nf12vqc4Ti_GWY0FwqmQKw.png)

So now we have the basic structure for our app, and we’re also able to render out messages. Great job!

**Now let’s replace our dummy data with actual messages from a chat room!**

### Step 5: Fetching API-keys from Chatkit

In order to get fetch messages, we’ll need to connect with the Chatkit API. And to do so, we need to obtain API keys.

At this point, I want to encourage you to follow my steps so that you can get your own chat application up and running. You can use my [Scrimba playground](https://scrimba.com/c/crVznf6?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=greactchatkit_10_minute_article) in order to test your own API keys.

Start by creating a free [account here](https://pusher.com/chatkit#sign-up). Once you’ve done that you’ll see your dashboard. This is where you create new Chatkit instances. Create one and give it whatever name you want:

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-72.png)

Then you’ll be navigated to your newly created instance. Here you’ll need to copy four values:

* Instance Locator
* Test Token Provider
* Room id
* Username

We’ll start with the **Instance Locator**:

![You can copy using the icon on the right side of the Instance Locator.](https://cdn-media-1.freecodecamp.org/images/1*AkbH5NfvHfwHAxiun37k9g.png)

_You can copy using the icon on the right side of the Instance Locator._

And if you scroll a bit down you’ll find the **Test Token Provider**:

![Image](https://cdn-media-1.freecodecamp.org/images/1*uSvabQgYrppTGsWKXQsJSQ.png)

The next step is to create a **User*** *and a **Room**, which is done on the same page. Note that you’ll have to create a user _first_, and then you’ll be able to create a room, which again gives you access to the room identifier.

![Image](https://cdn-media-1.freecodecamp.org/images/1*hCXjDJ3PQJ_emU4WfJRQEQ.png)

So now you’ve found your four identifiers. Well done!

However, before we head back to the codebase, I want you to manually send a message from the Chatkit dashboard as well, as this will help us in the next chapter.

Here’s how to do that:

![Image](https://cdn-media-1.freecodecamp.org/images/1*HU3mzUknYj8_MwY7ceK2Ow.png)

This is so that we actually have a message to render out in the next step.

### Step 6: Rendering real chat messages

Now let’s head back to our _index.js_ file and store these four identifiers as variables at the top of our file.

Here are mine, but I’d encourage you to create your own:

```jsx
    const instanceLocator = "v1:us1:dfaf1e22-2d33-45c9-b4f8-31f634621d24"

    const testToken = "https://us1.pusherplatform.io/services/chatkit_token_provider/v1/dfaf1e22-2d33-45c9-b4f8-31f634621d24/token"

    const username = "perborgen"

    const roomId = 9796712

```

And with that in place, we’re finally ready to connect with Chatkit. This will happen in the `App` component, and more specifically in the `componentDidMount` method. That’s the method you should use when connecting React.js components to API’s.

First we’ll create a `chatManager`:

```jsx
    componentDidMount() {
      const chatManager = new Chatkit.ChatManager({
        instanceLocator: instanceLocator,
        userId: userId,
        tokenProvider: new Chatkit.TokenProvider({
          url: testToken
        })
     })  

```

… and then we’ll do`chatManager.connect()` to connect with the API:

```jsx
      chatManager.connect().then(currentUser => {
          currentUser.subscribeToRoom({
          roomId: roomId,
          hooks: {
            onNewMessage: message => {
              this.setState({
                messages: [...this.state.messages, message]
              })
            }
          }
        })
      })
    }

```

This gives us access to the `currentUser` object, which is the interface for interacting with the API.

Note: As we’ll need to use`currentUser` later on, well store it on the instance by doing `this.currentUser = ``currentUser`.

Then, we’re calling `currentUser.subscribeToRoom()` and pass it our `roomId` and an `onNewMessage` hook.

The `onNewMessage` hook is triggered every time a new message is broadcast to the chat room. So every time it happens, we’ll simply add the new message at the end of `this.state.messages`.

This results in the app fetching data from the API and then rendering it out on the page.

![Image](https://cdn-media-1.freecodecamp.org/images/1*EAi9TyUba39xN3fciic3aA.png)

This is awesome, as we now have the skeleton for our client-server connection.

Woohoo!

### Step 7: Handling user input

The next thing we’ll need to create is the `SendMessageForm` component. This will be a so-called _controlled component_, meaning the component controls what’s being rendered in the input field via its state.

Take a look at the `render()` method, and pay special attention to the lines I’ve highlighted:

```jsx
    class SendMessageForm extends React.Component {
      render() {
        return (
          <form
            className="send-message-form">
            <input
              onChange={this.handleChange}
              value={this.state.message}
              placeholder="Type your message and hit ENTER"
              type="text" />
          </form>
        )
      }
    }

```

We’re doing two things:

1. Listening for user inputs with the `onChange` event listener, so that we can  
trigger the `handleChange` method
2. Setting the `value` of the input field explicitly using `this.state.message`

The connection between these two steps is found inside the `handleChange` method. It simply updates the state to whatever the user types into the input field:

```jsx
    handleChange(e) {
      this.setState({
        message: e.target.value
      })
    }

```

This triggers a re-render, and since the input field is set explicitly from the state using `value={this.state.message}`, the input field will be updated.

So even though the app feels instant for the user when they type something into the input field, **the data actually goes via the state before React updates the UI.**

To wrap up this feature, we need to give the component a `constructor`. In it, we’ll both initialize the state and bind `this` in the `handleChange` method:

```jsx
    constructor() {
        super()
        this.state = {
           message: ''
        }
        this.handleChange = this.handleChange.bind(this)
    }

```

We need to bind the `handleChange`method so that we’ll have access to the `this` keyword inside of it. That’s how JavaScript works: the `this` keyword is by default _undefined_ inside the body of a function.

### Step 8: Sending messages

Our `SendMessageForm` component is almost finished, but we also need to take care of the form submission. We need fetch the messages and send them off!

To do this we’ll hook a `handleSubmit` even handler up with the `onSubmit` event listener in the `<form>`.

```jsx
    render() {
        return (
          <form
            onSubmit={this.handleSubmit}
            className="send-message-form">
            <input
              onChange={this.handleChange}
              value={this.state.message}
              placeholder="Type your message and hit ENTER"
              type="text" />
        </form>
        )
      }

```

As we have the value of the input field stored in `this.state.message`, it’s actually pretty easy to pass the correct data along with the submission. We’ll  
simply do:

```jsx
    handleSubmit(e) {
      e.preventDefault()
      this.props.sendMessage(this.state.message)
      this.setState({
        message: ''
      })
    }

```

Here, we’re calling the `sendMessage` prop and passing in `this.state.message` as a parameter. You might be a little confused by this, as we haven’t created the `sendMessage` method yet. However, we’ll do that in the next section, as that method lives inside the `App` component. So don’t worry!

Secondly, we’re clearing out the input field by setting `this.state.message` to an empty string.

Here’s the entire `SendMessageForm` component. Notice that we’ve also bound `this` to the `handleSubmit` method:

```jsx
    class SendMessageForm extends React.Component {
      constructor() {
        super()
        this.state = {
          message: ''
        }
        this.handleChange = this.handleChange.bind(this)
        this.handleSubmit = this.handleSubmit.bind(this)
      }

      handleChange(e) {
        this.setState({
          message: e.target.value
        })
      }

      handleSubmit(e) {
        e.preventDefault()
        this.props.sendMessage(this.state.message)
        this.setState({
          message: ''
        })
      }

      render() {
        return (
          <form
            onSubmit={this.handleSubmit}
            className="send-message-form">
            <input
              onChange={this.handleChange}
              value={this.state.message}
              placeholder="Type your message and hit ENTER"
              type="text" />
          </form>
        )
      }
    }

```

### Step 9: Sending the messages to Chatkit

We’re now ready so send the messages off to Chatkit. That’s done up in the `App` component, where we’ll create a method called `this.sendMessage`:

```jsx
    sendMessage(text) {
      this.currentUser.sendMessage({
        text: text,
        roomId: roomId
      })
    }

```

It takes one parameter (the text) and it simply calls `this.currentUser.sendMessage()`.

The final step is to pass this down to the `<SendMessageForm>` component as a prop:

```jsx
    /* App component */
      
    render() {
      return (
        <div className="app">
          <Title />
          <MessageList messages={this.state.messages} />
          <SendMessageForm sendMessage={this.sendMessage} />
      )
    }

```

And with that, we’ve passed down the handler so that `SendMessageForm` can invoke it when the form is submitted.

### Step 10: Creating the Title component

To finish up, let’s also create the Title component. It’s just a simple functional component, meaning a function which returns a JSX expression.

```jsx
    function Title() {
      return <p class="title">My awesome chat app</p>
    }

```

It’s a good practice to use functional components, as they have more constraints than class components, which makes them less prone to bugs.

### The result

And with that in place you have your own chat application which you can use to chat with your friends!

![Image](https://cdn-media-1.freecodecamp.org/images/1*KQzdlJJLMGyq5IdZu6cZ1Q.png)

Give yourself a pat on the back if you’ve coded along until the very end.

If you want to learn how to build further upon this example, [then check out my free course on how to create a chat app with React here.](https://scrimba.com/g/greactchatkit?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=greactchatkit_10_minute_article)

Thanks for reading and happy coding :)

