---
title: A free React course that will grow your React JS skills by building a chat
  app
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-26T13:58:01.000Z'
originalURL: https://freecodecamp.org/news/want-to-learn-react-js-heres-my-free-course-which-teaches-it-through-building-a-chat-app-c86333e5b88c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Ik3tRrwdvnBFu3_B0rpimw.png
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: learn to code
  slug: learn-to-code
- name: General Programming
  slug: programming
- name: React
  slug: react
seo_title: null
seo_desc: 'By Per Harald Borgen


  Chat is eating the world, and React is eating front-end development. So what could
  be better than learning React through building chat app? In my latest course at
  Scrimba, you’ll do exactly that.

  It consists of 17 interactive le...'
---

By Per Harald Borgen

![Click the image to get to the course](https://cdn-media-1.freecodecamp.org/images/1*NE_xQlf9WZkO3LTpxG5TNA.png)

Chat is eating the world, and React is eating front-end development. So what could be better than learning React through building chat app? In my latest course at Scrimba, you’ll do exactly that.

It consists of 17 interactive lessons (plus intro and outro) and five challenges in which you’ll have to edit the code yourself.

And the best part: it’s all done in the browser. You don’t have to write any server-side code. The [Chatkit API](https://pusher.com/chatkit?utm_source=scrimba&utm_medium=medium&utm_campaign=announcment-post) takes care of the heavy-lifting on the back-end, so that we can focus on building the chat client.

At the end of the course, you’ll be left with your own personalised chat app, which includes multiple rooms, the ability to create new rooms, auto scrolling, and more. Plus, it’ll be very easily customisable thanks to CSS Grid and CSS Variables.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ik3tRrwdvnBFu3_B0rpimw.png)

I’m assuming that you know JavaScript, and that you’ve seen a little bit of React before (e.g. read my [five minute introductory article](https://medium.freecodecamp.org/learn-react-js-in-5-minutes-526472d292f4), and perhaps checked out a couple of tutorials). But other than that, there are no prerequisites for the course.

Now let’s have a look at how it’s laid out!

### Lesson #1: Course introduction

![Image](https://cdn-media-1.freecodecamp.org/images/1*zcRbKlNUmWNxStHWrQJEOw.png)

I’ll start off by giving you a quick intro to the course. We’ll go over what you’ll learn, and I’ll introduce myself as well. I’ll also give you an sneak peak at how you’ll be able to customize your own chat app at the end of the course.

### Lesson #2: Component architecture

![Image](https://cdn-media-1.freecodecamp.org/images/1*JD33BOZnuutza8G_trur1A.png)

Before you start building a React app, you should start by getting an overview over the components architecture, and thus break the UI into components. So in this lecture, I’ll show you how to do exactly that.

### Lesson #3: Codebase architecture

![Image](https://cdn-media-1.freecodecamp.org/images/1*xr6dWMCFWVA942U1w2r90Q.png)

Next up, we’ll see how our component architecture translates into code. I’ll also look at how the rest of the repo is setup, as I don’t won’t you to be confused about the various files throughout the repo once we start coding.

I won’t be creating the repository from scratch as there are plenty of tutorials which help you get your dev environment setup, and it’s not really what the Scrimba platform is best tailored for.

### Lesson #4: MessageList component

Now we’re finally ready to start coding, so in this lesson we’ll render out dummy data in our `MessageList` component. It’ll introduce you to JSX, and you’ll learn how to dynamically create elements using, for example, the `map()` array method.

```js
{DUMMY_DATA.map((message, index) => {  
   return (  
     <div key={index} className="message">  
        <div className="message-username">{message.senderId}</div>  
        <div className="message-text">{message.text}</div>  
     </div>  
   )  
})}

```

In this lesson you’ll also get your very first challenge!

### Lesson #5: Intro to Chatkit

[!Click the image to get to the Chatkit API.]([https://pusher.com/chatkit?utm_source=scrimba&utm_medium=medium&utm_campaign=announcment-post](https://pusher.com/chatkit?utm_source=scrimba&utm_medium=medium&utm_campaign=announcment-post))  
Click the image to get to the Chatkit API.

Now that we’re able to render out data on the page, we’ll get started integrating with the [Chatkit API](https://pusher.com/chatkit?utm_source=scrimba&utm_medium=medium&utm_campaign=announcment-post), which will take care of the back-end of the app. In this lesson, I give you quick overview over the API.

### Lesson #6: Connecting to Chatkit

![Image](https://cdn-media-1.freecodecamp.org/images/1*dRgHCdd44zgpOOFoqPwRPg.png)

Next up is simply coding the [Chatkit](https://pusher.com/chatkit?utm_source=scrimba&utm_medium=medium&utm_campaign=announcment-post) integration, which is super simple: the code above is all you need in order to start fetching messages from a chat room. You’ll be exposed for React’s `componentDidMount()` life-cycle method, which is where you should hook your component up with third-party API’s.

### Lesson #7: State and props

State and props are the two ways we handle data in React, and you need to understand the difference between the two. In this lecture, we’ll need to use both types, since we’ll both store chat messages in the state of our `App` component and also pass them down as props to the `MessageList` component.

```js
constructor() {  
  super()  
  this.state = {  
    messages: []  
  }  
}

```

### Lesson #8: The Message component

In this lecture, we’ll build out the Message component. It has one job: to render out the username and text which it gets passed down from its parents. I’ll also give you a challenge to change it from a class-based component into a functional component.

```jsx
function Message(props) {  
  return (  
    <div className="message">  
      <div className="message-username">{props.username}</div>  
      <div className="message-text">{props.text}</div>  
    </div>  
  )  
}

```

### Lesson #9: The SendMessageForm component

![Image](https://cdn-media-1.freecodecamp.org/images/1*bYkfM_KQ54Qxyh41g-XnvQ.png)

You can’t have a chat app without a form to send messages through. So in this lecture, we’ll create exactly that. It’ll teach you about controlled components, which is a critical concept in React. It means that the component itself decides what’s being rendered in the input field, instead of the DOM node itself holding that internal state.

### Lesson #10: Broadcasting messages

```js
sendMessage(text) {  
  this.currentUser.sendMessage({  
    text,  
    roodId: 9434230  
  })  
}

```

Now that we have the `SendMessageForm` in place, we need to send the messages to Chatkit so that it can broadcast them. This will force you to learn another core concept of React: the inverse data flow.

In React, data flows downwards, from parent to child. However, sometimes we need child components to reach up to their parents and trigger their methods, along with some data from themselves.

### Lesson #11: The RoomList component

![Image](https://cdn-media-1.freecodecamp.org/images/1*rqi85uI26PUeQ_cAJVkbIg.png)

As we have the core chat features in place now (sending and displaying messages), it’s time to jump over to the `RoomList` component, which displays all the rooms you have available on your Chatkit instance.

It’ll introduce you to a few new concepts in Chatkit, plus solidify your knowledge on how to send data down from parent components to child components. We’ll also revisit the ES6 spread operator, which is super handy to know when building React.js apps.

### Lesson #12: Subscribe to rooms

Then you’ll need to learn how to subscribe to specific rooms. We’ll hook an event listener up with each of the rooms displayed in the `RoomList` component. This will trigger a method in the `App` component, which tells Chatkit that the user wants to subscribe that specific room.

```js
subscribeToRoom(roomId) {  
  this.setState({ messages: [] })  
  this.currentUser.subscribeToRoom({  
    roomId: roomId,  
    hooks: {  
      onNewMessage: message => {  
        this.setState({  
          messages: [...this.state.messages, message]  
        })  
      }  
    }  
  })  
}

```

### Lesson #13: Room order and highlighting the current room

This lecture will introduce you to the `.sort()` array method in JavaScript, as we’ll need to make sure our rooms are sorted in the correct order regardless of where the data comes from originally.

const orderedRooms = [...this.props.rooms].sort((a, b) => a.id - b.id)

We’ll also add an `active` class to the room we’re currently chatting at in order to signal it to the user.

### Lesson #14: Adding autoscroll

Autoscroll is needed in order to automatically jump down to the latest messages as they appear in the `MessageList` component. It’s a neat little trick which introduces you to the following component life-cycle methods:

* `componentWillUpdate()`
* `componentDidUpdate()`

We’ll also need to use the`ReactDOM.findDOMNode()` method, so you’ll get to know that one, too.

### Lesson #15: The NewRoomForm component

This component allows you to create new rooms. It’ll be a refresher on controlled components from the ninth lesson.

With this, we’re done with all the React code for the app. So for the rest of the course, we’ll focus on design using CSS.

### Lesson #16: Creating your own chat app

![Image](https://cdn-media-1.freecodecamp.org/images/1*0N6xXGInxOYIGin0rjkFKg.png)

Before we start modifying the app design, I want to clone my code so that you’ll get your own copy of the repo. This sets you up for the next screencasts where you’ll personalize the design of it. I’ll guide you through each step until you’ve got your very own copy and free API-keys from Chatkit.

### Lesson #17: Changing the layout with CSS Grid

We’re using CSS Grid to control the layout of the app, which gives you super nice flexibility when it comes to changing it, thanks to `grid-template-areas`. I’ll teach you how you can move elements around on the page through just changing a few lines of CSS.

![Image](https://cdn-media-1.freecodecamp.org/images/1*yAyieAB9wQk-s2lJbO4Ybw.png)

### Lesson #18: Changing the theme with CSS Variables

![Image](https://cdn-media-1.freecodecamp.org/images/1*23UzFS7KCSj9d0Ten6WZsw.png)

![Before and after modifying the variables.](https://cdn-media-1.freecodecamp.org/images/1*RTHSzUyGjN8H5VyFJnzVZA.png)

  
Before and after modifying the variables.

As we’re using CSS Variables for our colours, you can also really easily change the theme of the app. Here, I’ll give you the challenge of finding a nice palette online and then implement it into your app.

If you combine the layout changes from the previous lesson with a new palette in this one, you’ll be left with your very own personalised chat app! Here’s one I made for myself, just for fun:

![Image](https://cdn-media-1.freecodecamp.org/images/1*r7YvAzkhlZ2E8Yjfdh-SBw.png)

### Lesson #19: Outro and closing challenges

If you reach this far: congrats! You’ve really invested in improving your skills, and I’m 100% sure it’ll pay off. In this screencast, I give you a couple of closing challenges you can do if you’re really up for it.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Rk3YHJTml0Au8SzkZgN-CA.png)

If you were pleased with [the course](https://scrimba.com/g/greactchatkit?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=greactchatkit_free_course), we’d be really grateful if you’d recommend it to a friend or share it on social media, as that’s how people discover our free Scrimba courses.

Good luck with the course, and happy coding :)

