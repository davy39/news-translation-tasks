---
title: Reintroducing React – Every React Update Since v16 [Full Handbook]
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-02T20:05:07.000Z'
originalURL: https://freecodecamp.org/news/reintroducing-react-every-react-update-since-v16-demystified-60686ee292cc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*EFYIS4Y6E3M4fv0BIG3G2w.png
tags:
- name: coding
  slug: coding
- name: handbook
  slug: handbook
- name: General Programming
  slug: programming
- name: React
  slug: react
seo_title: null
seo_desc: 'By Emmanuel Ohans

  In this article (and accompanying book), unlike any you may have come across before,
  I will deliver funny, unfeigned and dead serious comic strips about every React
  update since v16+. It’ll be hilarious, either intentionally or unin...'
---

By Emmanuel Ohans

In this article (and accompanying book), unlike any you may have come across before, I will deliver funny, unfeigned and dead serious comic strips about every React update since v16+. It’ll be hilarious, either intentionally or unintentionally, easy on beginners as well as professionals, and will be very informative as a whole.

#### Why Comic Strips ?

I have been writing software for over 5 years. But I have done other things, too. I’ve been a graphics designer, a published author, teacher, and a long, long time ago, an amateur Illustrator.

I love the tech community, but sometimes as a group, we tend to be a little narrow-minded.

When people attempt to teach new technical concepts, they forget who they were before they became developers and just churn out a lot of technical jargon — like other developers they’ve seen.

When you get to know people, it turns out so many of us have different diverse backgrounds! “If you were a comedian, why not explain technical concepts with some comedy?

Wouldn’t that be so cool?

I want to show how we can become better as engineers, as teams, and as a community, by openly being our full, weird selves, and **teaching others with all that personality.** But instead of just talking, I want to make it noteworthy and lead by example. So, you’re welcome to my rendition of a comic strip inspired book about every React update since v16.

With recently released v16.8 features, there’s going to be a lot of informative comic strips to be delivered!

Inspired by [Jani Eväkallio](https://twitter.com/jevakallio?lang=en).

> This is a very interesting but long read. [Please download the ebook](https://leanpub.com/reintroducing-react) (PDF, Epub & Mobi) **absolutely free** — without having to share your email with me. You can also pay whatever you want for the book if you wanna support my work.

#### How to Read this Article

First, [get the ebook](https://leanpub.com/reintroducing-react). Apart from being able to read offline, the ebooks have syntax highlighted codes that make them easier to read as well. [Go get it](https://leanpub.com/reintroducing-react).

![Image](https://cdn-media-1.freecodecamp.org/images/Nb9iorcKIAQebUWfWgs-JhbR289ENJvinibW)
_[https://leanpub.com/reintroducing-react](https://leanpub.com/reintroducing-react" rel="noopener" target="_blank" title=")_

Secondly, please find the associated [code repository](https://github.com/ohansemmanuel/Reintroducing-react) for the book on Github. This will help you follow along with the examples allowing for more hands-on practice.

![Image](https://cdn-media-1.freecodecamp.org/images/YDMVHOQjYMiKVwqh5kWnebHeer10XphxEIIz)

#### Why Reintroduce React?

I wrote my first React application 3 to 4 years ago. Between then and now, the fundamental principles of React have remained the same. React is just as declarative and component-based today as it was then.

That’s great news, however, the way we write React applications today has changed!

There’s been a lot of new additions (and well, removals).

If you learned React a while back it’s not impossible that you haven’t been up to date with every new feature/release. It’s also possible to get lost on all the new features. Where exactly do you start? How important are they for your day to day use?

Even as an experienced engineer, I sometimes find unlearning old concepts and relearning new ones just as intimidating as learning a new concept from the scratch.

If that’s the case with you, I hope I can provide the right help for you via this guide.

The same applies if you’re just learning React.

There’s a lot of state information out there. If you learn React with some old resource, yes, you’ll learn the fundamentals of React, but modern React has new interesting features that are worth your attention. It’s best to know those now, and not have to unlearn and relearn newer concepts.

Whether you’ve been writing React for a while, or new to developing React applications, I will be discussing **every** update to React since version 16.

This will keep you in sync with the recent changes to React, and help you write better software.

Remember, a reintroduction to React is important for not just beginners, but professionals alike. It all depends on how well you’ve kept your ear to the ground, and really studied the many changes that have been released over the last 12 months.

On the bright side, I’m bringing you a one-stop reference to all the changes.

In this book, I’ll take you on a journey — alongside some humour and unique content to follow.

Ready?

#### What’s Changed since version 16?

If you think not much has changed, think again.

Here’s a list of the relevant changes we’ll be discussing in this guide:

* New Lifecycle Methods.
* Simpler State Management with the Context API.
* ContextType — Using Context without a Consumer.
* The Profiler: Using Charts and Interactions.
* Lazy Loading with React.Lazy and Suspense.
* Functional PureComponent with React.memo
* Simplifying React apps with Hooks!
* **Advanced React Component Patterns with Hooks**.

It goes without saying that a lot has been introduced since version 16. For ease, each of these topics have been broken down into separate sections.

In the next section I’ll begin to discuss these changes by having a look at the new lifecycle methods available from version 16.

### Chapter 1: New Lifecycle Methods.

![Image](https://cdn-media-1.freecodecamp.org/images/ADJ58ZyM2MbBszxgupJp7eX9XnrTXotbsHJR)

He’s been writing software for a while, but new to the React ecosystem.

Meet John.

![Image](https://cdn-media-1.freecodecamp.org/images/hLWHsySy2MjOixddCdxRPK5z9x5qZZWYq9Xm)

For a long time he didn’t fully understand what lifecycle truly meant in the context of React apps.

When you think of lifecycle what comes to mind?

#### What’s Lifecycle Anyway?

Well, consider humans.

![Image](https://cdn-media-1.freecodecamp.org/images/0Y37Fw7u57Bww8eMdVhbZz9mJthSVTF8xAJl)

The typical lifecycle for a human is something like, “child” to “adult” to “elderly”.

In the biological sense, lifecycle refers to the series of “changes in form” an organism undergoes.

The same applies to React components. They undergo a series of “changes in form”.

Here’s what a simple graphical representation for React components would be.

![Image](https://cdn-media-1.freecodecamp.org/images/0ZXhBgvKYzQJ2ktWeLdw8Ep961sWLipbFI0b)

The four essential phases or lifecycle attributed to a React component include:

* **Mounting** — like the birth of a child, at this phase the component is created (your code, and react’s internals) then inserted into the DOM
* **Updating** — like humans “grow”, in this phase a React component undergoes growth by being updated via changes in props or state.
* **Unmounting** — Like the death of a human, this is the phase the component is removed from the DOM.
* **Error Handling** — Think of this as being comparable to when humans fall sick and visit the doctor. Sometimes your code doesn’t run or there’s a bug somewhere. When this happens, the component is in the error handling phase. I intentionally skipped this phase in the illustration earlier.

#### Lifecycle Methods.

Now that you understand what lifecycle means, what are “lifecycle methods”?

Knowing the phases /lifecycle a React component goes through is one part of the equation. The other part is understanding the methods React makes available (or invokes) at each phase.

The methods invoked during different phase/lifecycle of a component is what’s popularly known as the component lifecycle methods e.g. In the mounting and updating phases, the `render` lifecycle method is always invoked.

There are lifecycle methods available on all 4 phases of a component — mounting, updating, unmounting and error handling.

Knowing when a lifecycle method is invoked (i.e the associated lifecycle/phase) means you can go ahead to write related logic within the method and know it’ll be invoked at the right time.

With the basics out of the way, let’s have a look at the actual new lifecycle methods available from version 16.

#### static getDerivedStateFromProps.

Before explaining how this lifecycle method works, let me show you how the method is used.

The basic structure looks like this:

```
const MyComponent extends React.Component {  ... 
```

```
  static getDerivedStateFromProps() {     //do stuff here  }  }
```

The method takes in `props` and `state`:

```
... 
```

```
  static getDerivedStateFromProps(props, state) {	//do stuff here  }  
```

```
...
```

And you can either return an object to update the state of the component:

```
... 
```

```
  static getDerivedStateFromProps(props, state) {      return {     	points: 200 // update state with this     }  }  
```

```
  ...
```

Or return null to make no updates:

```
... 
```

```
  static getDerivedStateFromProps(props, state) {    return null  }  
```

```
...
```

I know what you’re thinking. Why exactly is this lifecycle method important?

Well, it is one of the rarely used lifecycle methods, but it comes in handy in certain scenarios.

Firstly, this method is called (or invoked) **before** the component is rendered to the DOM on initial mount.

Below’s a quick example.

Consider a simple component that renders the number of points scored by a football team.

As you may have expected, the number of points is stored in the component state object:

```
class App extends Component {  state = {    points: 10  }  render() {    return (      <div className="App">        <header className="App-header">          <img src={logo} className="App-logo" alt="logo" />          <p>            You've scored {this.state.points} points.          </p>        </header>      </div>    );  }}
```

![Image](https://cdn-media-1.freecodecamp.org/images/hfyqbWa079ilh8WNpff4fBknEmgMJY8r3JD7)

Note that the text reads, _you have scored 10 points_ — where 10 is the number of points in the state object.

Just an as an example, if you put in the static getDerivedStateFromProps method as shown below, what number of points will be rendered?

```
class App extends Component {  state = {    points: 10  }	  // *******  //  NB: Not the recommended way to use this method. Just an example. Unconditionally overriding state here is generally considered a bad idea  // ********  static getDerivedStateFromProps(props, state) {    return {      points: 1000    }  }  render() {    return (      <div className="App">        <header className="App-header">          <img src={logo} className="App-logo" alt="logo" />          <p>            You've scored {this.state.points} points.          </p>        </header>      </div>    );  }}
```

Right now, we have the static getDerivedStateFromProps component lifecycle method in there. If you remember from the previous explanation, this method is called before the component is mounted to the DOM. By returning an object, we update the state of the component before it is even rendered.

And here’s what we get:

![Image](https://cdn-media-1.freecodecamp.org/images/zeyjZq0KXXLe1NcM7DTPaGo7CB45Y1t2Zc4x)

With the 1000 coming from updating state within the `static getDerivedStateFromProps` method.

Well, this example is contrived, and not really the way you’d use the `static getDerivedStateFromProps` method. I just wanted to make sure you understood the basics first.

With this lifecycle method, just because you can update state doesn’t mean you should go ahead and do this. There are specific use cases for the `static getDerivedStateFromProps` method, or you’ll be solving a problem with the wrong tool.

So when should you use the `static getDerivedStateFromProps` lifecycle method?

The method name `getDerivedStateFromProps` comprises five different words, “Get Derived State From Props”.

![Image](https://cdn-media-1.freecodecamp.org/images/2CHM9AEB3-nVWe7YAaaTe4NxVCGc7bWO2i4w)

Also, component state in this manner is referred to as Derived State.

As a rule of thumb, derived state should be used sparingly as you can introduce [subtle bugs](https://reactjs.org/blog/2018/06/07/you-probably-dont-need-derived-state.html#common-bugs-when-using-derived-state) into your application if you aren’t sure of what you’re doing.

#### getSnapshotBeforeUpdate.

In the updating component phase, right after the render method is called, the `getSnapshotBeforeUpdate` lifecycle method is called next.

This one is a little tricky, but I’ll take my time to explain how it works.

Chances are you may not always reach out for this lifecycle method, but it may come in handy in certain special cases. Specifically when you need to grab some information from the DOM (and potentially change it) just after an update is made.

Here’s the important thing. The value queried from the DOM in `getSnapshotBeforeUpdate` will refer to the value just before the DOM is updated. Even though the render method was previously called.

An analogy that may help has to do with how you use version control systems such as git.

A basic example is that you write code, and stage your changes before pushing to the repo.

In this case, assume the render function was called to stage your changes before actually pushing to the DOM. So, before the actual DOM update, information retrieved from getSnapshotBeforeUpdate refers to those before the actual visual DOM update.

Actual updates to the DOM may be asynchronous, but the `getSnapshotBeforeUpdate` lifecycle method will always be called immediately before the DOM is updated.

Don’t worry if you don’t get it yet. I have an example for you.

![Image](https://cdn-media-1.freecodecamp.org/images/unerso1VTE24Qf7YMQqizDGDxGaF94tMQ8xB)

The implementation of the chat pane is as simple as you may have imagined. Within the `App` component is an unordered list with a `Chats` component:

```
<ul className="chat-thread">    <Chats chatList={this.state.chatList} /> </ul>
```

The `Chats` component renders the list of chats, and for this, it needs a chatList prop. This is basically an Array. In this case, an array of 3 string values, "Hey", "Hello", "Hi".

The `Chats` component has a simple implementation as follows:

```
class Chats extends Component {  render() {    return (      <React.Fragment>        {this.props.chatList.map((chat, i) => (          <li key={i} className="chat-bubble">            {chat}          </li>        ))}      </React.Fragment>    );  }}
```

It just maps through the `chatList` prop and renders a list item which is in turn styled to look like a chat bubble :).

There’s one more thing though. Within the chat pane header is an “Add Chat” button.

![Image](https://cdn-media-1.freecodecamp.org/images/1m1dDWKV78TsJqLZTkPCkLI0NCCm5WpxguEV)

Clicking this button will add a new chat text, “Hello”, to the list of rendered messages.

Here’s that in action:

![Image](https://cdn-media-1.freecodecamp.org/images/lz7y-pZgh69oM8Qky58mc7Uy9GNuy-GEm4pw)
_Adding new chat messages_

The problem here, as with most chat applications, is that whenever the number of chat messages exceeds the available height of the chat window, the expected behaviour is to auto scroll down the chat pane so that the latest chat message is visible. That’s not the case now.

![Image](https://cdn-media-1.freecodecamp.org/images/a54HCUsBP3ONIrJvrsiEE1H66BYTAdTZbu0o)
_I have to scroll manually to find the most recent message_

Let’s see how we may solve this using the getSnapshotBeforeUpdate lifecycle method.

The way the `getSnapshotBeforeUpdate` lifecycle method works is that when it is invoked, it gets passed the previous props and state as arguments.

So we can use the `prevProps` and `prevState` parameters as shown below:

```
getSnapshotBeforeUpdate(prevProps, prevState) {   }
```

Within this method, you’re expected to either return a value or null:

```
getSnapshotBeforeUpdate(prevProps, prevState) {   return value || null // where 'value' is a  valid JavaScript value    }
```

Whatever value is returned here is then passed on to another lifecycle method. You’ll get to see what I mean soon.

The `getSnapshotBeforeUpdate` lifecycle method doesn't work on its own. It is meant to be used in conjunction with the `componentDidUpdate` lifecycle method.

Whatever value is returned from the `getSnapshotBeforeUpdate` lifecycle method is passed as the third argument to the `componentDidUpdate` method.

Let’s call the returned value from `getSnapshotBeforeUpdate`, _snapshot_, and here's what we get thereafter:

```
componentDidUpdate(prevProps, prevState, snapshot) { }
```

The `componentDidUpdate` lifecycle method is invoked after the `getSnapshotBeforeUpdate` is invoked. As with the getSnapshotBeforeUpdate method it receives the previous props and state as arguments. It also receives the returned value from `getSnapshotBeforeUpdate` as final argument.

Here’s all the code required to maintain the scroll position within the chat pane:

```
getSnapshotBeforeUpdate(prevProps, prevState) {    if (this.state.chatList > prevState.chatList) {      const chatThreadRef = this.chatThreadRef.current;      return chatThreadRef.scrollHeight - chatThreadRef.scrollTop;    }    return null;  }  componentDidUpdate(prevProps, prevState, snapshot) {    if (snapshot !== null) {      const chatThreadRef = this.chatThreadRef.current;      chatThreadRef.scrollTop = chatThreadRef.scrollHeight - snapshot;    }  }
```

Let me explain what’s going on there.

Below’s the chat window:

![Image](https://cdn-media-1.freecodecamp.org/images/OzgLAOVGpmNxBigrESPZYjEqWZvPr1j93kfh)
_The full chat window_

However, the graphic below highlights the actual region that holds the chat messages (the unordered list, `ul` which houses the messages).

![Image](https://cdn-media-1.freecodecamp.org/images/CHWDBo14-MfxpwtFUUkDjDN2Mwoq6eW-wuRq)
_The actual region holding the chat messages_

It is this `ul` we hold a reference to using a React Ref:

```
<ul className="chat-thread" ref={this.chatThreadRef}>   ...</ul>
```

First off, because `getSnapshotBeforeUpdate` may be triggered for updates via any number of props or even a state update, we wrap to code in a conditional that checks if there’s indeed a new chat message:

```
getSnapshotBeforeUpdate(prevProps, prevState) {    if (this.state.chatList > prevState.chatList) {      // write logic here    }  }
```

The `getSnapshotBeforeUpdate` method above has to return a value yet. If no chat message was added, we will just return `null`:

```
getSnapshotBeforeUpdate(prevProps, prevState) {    if (this.state.chatList > prevState.chatList) {      // write logic here    }      return null }
```

Now consider the full code for the `getSnapshotBeforeUpdate` method:

```
getSnapshotBeforeUpdate(prevProps, prevState) {    if (this.state.chatList > prevState.chatList) {      const chatThreadRef = this.chatThreadRef.current;      return chatThreadRef.scrollHeight - chatThreadRef.scrollTop;    }    return null;  }
```

Does it make sense to you?

Not yet, I suppose.

First, consider a situation where the entire height of all chat messages doesn’t exceed the height of the chat pane.

![Image](https://cdn-media-1.freecodecamp.org/images/c0Zb3kxJmFNPmbiPP6tlCgrbWcAJ7BIpSf9L)

Here, the expression `chatThreadRef.scrollHeight - chatThreadRef.scrollTop` will be equivalent to `chatThreadRef.scrollHeight - 0`.

When this is evaluated, it’ll be equal to the `scrollHeight` of the chat pane — just before the new message is inserted to the DOM.

If you remember from the previous explanation, the value returned from the `getSnapshotBeforeUpdate` method is passed as the third argument to the `componentDidUpdate method`. We call this snapshot:

```
componentDidUpdate(prevProps, prevState, snapshot) {}
```

The value passed in here — at this time, is the previous `scrollHeight` before the update to the DOM.

In the `componentDidUpdate` we have the following code, but what does it do?

```
componentDidUpdate(prevProps, prevState, snapshot) {    if (snapshot !== null) {      const chatThreadRef = this.chatThreadRef.current;      chatThreadRef.scrollTop = chatThreadRef.scrollHeight - snapshot;    }  }
```

In actuality, we are programmatically scrolling the pane vertically [from the top down](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollTop), by a distance equal to `chatThreadRef.scrollHeight - snapshot`;

Since `snapshot` refers to the `scrollHeight` before the update, the above expression returns the `height` of the new chat message plus any other related height owing to the update.

Please see the graphic below:

![Image](https://cdn-media-1.freecodecamp.org/images/hoII8SAxbI6PJoKCgKovHu3ontCBLXb-xplp)

When the entire chat pane height is occupied with messages (and already scrolled up a bit), the `snapshot` value returned by the `getSnapshotBeforeUpdate` method will be equal to the actual height of the chat pane.

The computation from `componentDidUpdate` will set to `scrollTop` value to the sum of the heights of extra messages - exactly what we want.

![Image](https://cdn-media-1.freecodecamp.org/images/aqEisKIrxOuOCQKOePljWG15E9GGXOu9CWG1)

Yeah, that’s it.

If you got stuck, I’m sure going through the explanation (one more time) or checking the source code will help clarify your questions.

#### The Error Handling Lifecycle Methods.

Sometimes things go bad, errors are thrown. The error lifecycle methods are invoked when an error is thrown by a descendant component i.e a component below them.

Let’s implement a simple component to catch errors in the demo app. For this, we’ll create a new component called `ErrorBoundary`.

Here’s the most basic implementation:

```
import React, { Component } from 'react';class ErrorBoundary extends Component {  state = {};  render() {    return null;  }}export default ErrorBoundary;
```

Now, let’s incorporate the error lifecycle methods.

#### static getDerivedStateFromError.

Whenever an error is thrown in a descendant component, this method is called first, and the error thrown passed as an argument.

Whatever value is returned from this method is used to update the state of the component.

Let’s update the `ErrorBoundary` component to use this lifecycle method.

```
import React, { Component } from "react";
```

```
class ErrorBoundary extends Component {  state = {};
```

```
  static getDerivedStateFromError(error) {    console.log(`Error log from getDerivedStateFromError: ${error}`);    return { hasError: true };  }
```

```
  render() {    return null;  }}
```

```
export default ErrorBoundary;
```

Right now, whenever an error is thrown in a descendant component, the error will be logged to the console, `console.error(error`), and an object is returned from the `getDerivedStateFromError` method. This will be used to update the state of the ErrorBoundary component i.e with `hasError: true`.

#### componentDidCatch.

The `componentDidCatch` method is also called after an error in a descendant component is thrown. Apart from the error thrown, it is passed one more argument which represents more information about the error:

```
componentDidCatch(error, info) {}
```

In this method, you can send the `error` or `info` received to an external logging service. Unlike `getDerivedStateFromError`, the `componentDidCatch` allows for side-effects:

```
componentDidCatch(error, info) {	logToExternalService(error, info) // this is allowed.         //Where logToExternalService may make an API call.}
```

Let’s update the `ErrorBoundary` component to use this lifecycle method:

```
import React, { Component } from "react";
```

```
class ErrorBoundary extends Component {  state = { hasError: false };  static getDerivedStateFromError(error) {    console.log(`Error log from getDerivedStateFromError: ${error}`);    return { hasError: true };  }  componentDidCatch(error, info) {    console.log(`Error log from componentDidCatch: ${error}`);    console.log(info);  }  render() {    return null  }}export default ErrorBoundary;
```

Also, since the `ErrorBoundary` can only catch errors from descendant components, we’ll have the component render whatever is passed as `Children` or render a default error UI if something went wrong:

```
... render() {    if (this.state.hasError) {      return <h1>Something went wrong.</h1>;    }
```

```
    return this.props.children; }
```

I have simulated a javascript error whenever you add a 5th chat message.

Have a look at the error boundary at work:

![Image](https://cdn-media-1.freecodecamp.org/images/7BtaANRXqMdWT3gmpWAAfpk4l5kOtAHhiPyP)

#### Conclusion.

It is worth mentioning that while new additions were made to the component lifecycle methods, some other methods such as `componentWillMount` , `componentWillUpdate`, `componentWillReceiveProps` were deprecated.

![Image](https://cdn-media-1.freecodecamp.org/images/-k1Wn8Tyztlbj-iQi1JG5R9URhy4M5PZOsIl)
_Deprecated lifecycle methods_

Now you’re up to date on the changes made to the component lifecycle methods since React version 16!

### Chapter 2: Simpler State Management with the Context API.

![Image](https://cdn-media-1.freecodecamp.org/images/hkHwd2gLDsTYazf2aSM5EuPUTH5RvqoUHnMJ)

John’s an amazing developer, and he loves what he does. However, he’s frequently been facing the same problem when writing React applications.

![Image](https://cdn-media-1.freecodecamp.org/images/BasI49K5JaDLjeNq-W2ttxwZpcKjJZKY5ysr)
_Props drilling_

**Props drilling**, the term used to describe passing down props needlessly through a deeply nested component tree, has plagued John for a while now!

Luckily, John has a friend who always has all the answers. Hopefully, she can suggest a way out.

John reaches out to Mia, and she steps in to offer some advice.

![Image](https://cdn-media-1.freecodecamp.org/images/h5fhv1i9F8pGKAwhUoIe78RVCPI6bPDHEmPB)
_Mia says, ‘try Redux or MobX’._

Mia is a fabulous engineer as well, and she suggests using some state management library such as `Redux` or `MobX`.

These are great choices, however, for most of John’s use cases, he finds them a little too bloated for his need.

“_Can’t I have something simpler and native to React itself_”, says John.

Mia goes on a desperate search to help a friend in need, and she finds the Context API.

![Image](https://cdn-media-1.freecodecamp.org/images/TsMolzLtPQlrPVEjJDm95t8VF3H6y6IvKb0v)

Mia recommends using React’s Context API to solve the problem. John is now happy, excited to see what the Context API could offer, and he goes about his work productively.

This marks the beginning of John’s experience with the Context API.

#### Introduction to Context.

The Context API exists to make it easy to share data considered “global” within a component tree.

Let’s have a look at an illustrated example before we delve into writing any code.

Well, John has began working with the Context API and has mostly been impressed with it so far. Today he has a new project to work on, and he intends to use the context API.

Let’s see what this new project is about.

![Image](https://cdn-media-1.freecodecamp.org/images/jZg7XLI0pwdpiRkAftIRJu7I6ZP32I3pdJHx)
_The new project: Benny Home Run_

John is expected to build a game for a new client of his. This game is called **Benny Home Run**, and it seems like a great place to use the Context API.

The sole aim of the game is to move Benny from his start position to his new home.

![Image](https://cdn-media-1.freecodecamp.org/images/41X58zNSpcIFa-a5qIXo3CVlICGAoPaYwHLB)
_The aim of the game_

To build this game, John must keep track of the position of Benny.

Since Benny’s position is such an integral part of the entire application, it may as well be tracked via some global application state.

![Image](https://cdn-media-1.freecodecamp.org/images/YCZQJwydNektrDR5gZ2IBwuCuZ-JRWUwJQOA)
_Tracking position values x and y in state_

Did I just say “_global application state_”?

Yeah!

That sounds like a good fit for the Context API.

So, how may John build this?

![Image](https://cdn-media-1.freecodecamp.org/images/goXVPDOBLY69Gaf0NgifcVoilXOcZro-NWyy)

First, there’s the need to import the `createContext` method from `React`

```
import {createContext} from 'react';
```

The `createContext` method allows you to create what’s referred to as a context object. Consider this to be the data structure that powers retrieving and saving state values.

To create a context object, you invoke the `createContext` method with (or without) an initial state value to be saved in the context object.

```
createContext(initialStateValue)
```

Here’s what that looks like in the Benny app:

```
const BennyPositionContext = createContext({ 	x: 50, 	y: 50 })
```

The `createContext` method is invoked with an initial state value corresponding to the initial position values (x and y) for Benny.

Looks good!

But, after creating a context object, how exactly do you gain access to the state values within your application?

Well, every context object comes with a `Provider` and `Consumer` component.

The `Provider` component “provides” the value saved in the context object to its children, while the `Consumer` component “consumes” the values from within any child component.

I know that was a mouth full, so let’s break it apart slowly.

In the Benny example, we can go ahead and destructure the `BennyPositionContext` to retrieve the Provider and Consumer components.

```
const BennyPositionContext = createContext({ 	x: 50, 	y: 50 })// get provider and consumerconst { Provider, Consumer } = BennyPositionContext
```

Since `Provider` provides value saved in the context object to its **children**, we could wrap a tree of components with the `Provider` component as shown below:

```
&lt;Provider>   <Root /> // the root component for the Benny app. </Provider>
```

Now, any child component within the `Root` component will have access to the default values stored in the context object.

Consider the following tree of components for the Benny app.

```
<Provider>   <Scene>     <Benny />   &lt;/Scene></Provider>
```

Where `Scene` and `Benny` are children of the `Root` component and represent the game scene and benny character respectively.

In this example, the `Scene` or the even more nested `Benny` component will have access to the value provided by the `Provider` component.

It is worth mentioning that a `Provider` also takes in a `value` props.

This `value` prop is useful if you want to provide a value other than the initial value passed in at the context object creation time via `createContext(initialStateValue)`

Here’s an example where a new set of values are passed in to the `Provider` component.

```
<Provider value={x: 100, y: 150}>   <Scene>     <Benny />   &lt;/Scene></Provider>
```

Now that we have values provided by the `Provider` component, how can a nested component such as `Benny` consume this value?

![Image](https://cdn-media-1.freecodecamp.org/images/Jy-XrFHSMdxF9UXcIxToIWMELABQqFMVtttE)

The simple answer is by using the `Consumer` component.

Consider the `Benny` component being a simple component that renders some SVG.

```
const Benny = () => {  return <svg />}
```

Now, within `Benny` we can go ahead and use the `Consumer` component like this:

```
const Benny = () => {  return <Consumer>  {(position) => <svg /&gt;}</Consumer>}
```

Okay, what’s going on there?

The `Consumer` component exposes a render prop API i.e `children` is a function. This function is then passed arguments corresponding to the values saved in the context object. In this case, the `position` object with the `x` and `y` coordinate values.

It is worth noting that whenever the value from a `Provider` component changes, the associated `Consumer` component and the children will be re-rendered to keep the value(s) consumed in sync.

Also, a `Consumer` will receive values from the closest `Provider` above it in the tree.

Consider the situation below:

```
// create context object const BennyPositionContext = createContext({ 	x: 50, 	y: 50 })
```

```
// get provider and consumerconst { Provider, Consumer } = BennyPositionContext
```

```
// wrap Root component in a Provider&lt;Provider>  <Root />;</Provider>
```

```
// in Benny, within Root. const Benny = () => (  <Provider value={x: 100, y: 100}>    // do whatever  </Provider>)
```

Now, with a new provider component introduced in `Benny`, any `Consumer` within `Benny` will receive the value `{x: 100, y: 100}` NOT the initial value of `{x: 50, y: 50}`.

This is a contrived illustrated example, but it helps solidify the foundations of using the Context API.

Having understood the necessary building blocks for using the Context API, let’s build an application utilizing all you’ve learned so far, with extra use cases discussed.

#### Example: The Mini-Bank Application.

John’s an all round focused guy. When he’s not working on projects from his work place, he dabbles into side projects.

One of his many side projects is a bank application he thinks could shape the future of banking. How so.

I managed to get the source code for this application. You’ll find it in the code repository for the book as well.

To get started, please Install the dependencies and run the application by following the commands below:

```
cd 02-Context-API/bank-appyarn installyarn start
```

Once that’s done, the application starts off with a login screen as seen below:

![Image](https://cdn-media-1.freecodecamp.org/images/VAOjsusp1WiPZs5HJC8sMmgYVNiJEmbOYd1T)

You can enter whatever username and password combination of your choosing.

Upon login in you’ll be presented with the application’s main screen shown below:

![Image](https://cdn-media-1.freecodecamp.org/images/Z6kaXqVc45pIKNLJZYfEFdWSsU0wQHrvhMil)

In the main screen you can perform actions such as viewing your bank account balance and making withdrawals as well.

![Image](https://cdn-media-1.freecodecamp.org/images/RHV3RbXZud6IXE8JkHInhr0gj1qLiFk3p6yV)
_cliking yes from the previous screen displays the account balance_

Our goal here is to manage the state in this application a lot better by introducing React’s Context.

#### Identifying Props being Drilled.

The root component of the application is called `Root`, and has the implementation below:

```
... import { USER } from './api'class Root extends Component {  state = {    loggedInUser: null  }  handleLogin = evt => {    evt.preventDefault()    this.setState({      loggedInUser: USER    })  }  render () {    const { loggedInUser } = this.state    return loggedInUser ? (      &lt;App loggedInUser={loggedInUser} />    ) : (      <Login handleLogin={this.handleLogin} /&gt;    )  }}
```

If the user is logged in, the main component `App` is rendered, else we show the `Login` component.

```
... loggedInUser ? (      &lt;App loggedInUser={loggedInUser} />    ) : (   <Login handleLogin={this.handleLogin} />)...
```

Upon a successful login (which doesn’t require any particular username and password combinations), the `state` of the `Root` application is updated with a `loggedInUser`.

```
...handleLogin = evt => {    ...    this.setState({      loggedInUser: USER    })  }...
```

In the real world, this could come from an `api` call.

For this application, I’ve created a fake user in the `api` directory that exports the following user object.

```
export const USER = {  name: 'June',  totalAmount: 2500701}
```

Basically, the `name` and `totalAmount` of the user’s bank account are retrieved and set to state when you log in.

How’s the user object used in the application?

Well, consider the main component, `App`. This is the component responsible for rendering everything in the app other than the `Login` screen.

Here’s the implementation of that:

```
class App extends Component {  state = {    showBalance: false  }  displayBalance = () => {    this.setState({ showBalance: true })  }  render () {    const { loggedInUser } = this.props    const { showBalance } = this.state    return (      <div className='App'>            <User loggedInUser={loggedInUser} profilePic={photographer} />	<ViewAccountBalance          showBalance={showBalance}          loggedInUser={loggedInUser}          displayBalance={this.displayBalance}        />        <section>;          <WithdrawButton amount={10000} />          <WithdrawButton amount={5000} /&gt;        </section>        <Charity />      </div>    )  }}
```

It’s a lot simpler that it seems. Have a second look!

The `loggedInUser` is passed as props to `App` from `Root`, and is also passed down to both `User` and `ViewAccountBalance` components.

![Image](https://cdn-media-1.freecodecamp.org/images/g4akMtcB-co2ZRACtlN0C6vbATgsbQRcvu09)

The `User` component receives the `loggedInUser` prop and passes it down to another child component, `Greeting` which renders the text, “_Welcome, June_”.

```
//User.js const User = ({ loggedInUser, profilePic }) => {  return (    <div>      <img  src={profilePic} alt='user' />      <Greeting loggedInUser={loggedInUser} />    </div>  )}
```

Also, `ViewAccountBalance` takes in a boolean prop `showBalance` which decides whether to show the account balance or not. This is toggled to `true` when you click the “yes” button.

![Image](https://cdn-media-1.freecodecamp.org/images/1RLdVLjZIkfAntk16bMgIyHNEtDgz8UYLlSz)

```
//ViewAccountBalance.jsconst ViewAccountBalance = ({ showBalance, loggedInUser, displayBalance }) => {  return (    <Fragment>      {!showBalance ? (        <div>          <p>            Would you love to view your account balance?          </p>          <button onClick={displayBalance}>            Yes          </button>        </div>      ) : (        <TotalAmount totalAmount={loggedInUser.totalAmount} />      )}    </Fragment>  )}
```

From the code block above, do you also see that `ViewAccountBalance` receives the `loggedInUser` prop only to pass it to `TotalAmount`?

![Image](https://cdn-media-1.freecodecamp.org/images/8I2fuTlfwAtBSTpcWD9d8oNMTwlfIXPPWsoN)

`TotalAmount` receives this prop, retrieves the `totalAmount` from the user object and renders the total amount.

I’m pretty sure you can figure out whatever else is going on in the code snippets above.

Having explained the code so far, do you see the obvious props drilling here?

`loggedInUser` is passed down way too many times to components that don’t even need to know about it.

Let’s fix that with the `Context` API.

#### Avoid Props Drilling with Context.

One easy solution is to look at the `Root` component where we began passing props down and finding a way to introduce a context object in there.

Going by that solution, we could create a context object with no initial default values above the `Root` class declaration:

```
const { Provider, Consumer } = createContext()class Root extends Component {  state = {    loggedInUser: null  }  ... }
```

Then we could wrap the main `App` component around the `Provider` with a value prop.

```
class Root extends Component {  state = {    loggedInUser: null  }  ...   render () {    ...    return loggedInUser ? (      <Provider value={this.state.loggedInUser}>        <App loggedInUser={loggedInUser} />      </Provider>    ) ...
```

Initially, the `Provider` `value` prop will be `null`, but as soon as a user logs in and the `state` is updated in `Root`, the `Provider` will also receive the current `loggedInUser`.

With this done we can import the `Consumer` wherever we want and do away with passing props needlessly down the component tree.

For example here’s the `Consumer` used in the `Greeting` component:

```
import { Consumer } from '../Root'const Greeting = () => {  return (    <Consumer>      {user => <p>Welcome, {user.name}! </p>;}    </Consumer>  )}
```

We could go ahead and do the same everywhere else we’ve passed the `loggedInUser` prop needlessly.

And the app works just as before, only we got rid of passing down `loggedInUser` over and over again .

#### Isolating Implementation Details.

The solution highlighted above works but not without some caveat.

A better solution will be to centralise the logic for the user state and Provider in one place.

This is pretty common practice. Let me show you what I mean.

Instead of having the `Root` component manage the state for `loggedInUser`, we will create a new file called `UserContext.js`.

This file will have the related logic for updating `loggedInUser` as well as expose a context `Provider` and `Consumer` to make sure `loggedInUser` and any updater functions are accessible from anywhere in the component tree.

This sort of modularity becomes important when you have many different context objects. For example, you could have a `ThemeContext` and `LanguageContext` object in the same app.

Extracting these into separate files and components proves more manageable and effective over time.

Consider the following:

```
// UserContext.jsimport React, { createContext, Component } from 'react'import { USER } from '../api'const { Provider, Consumer } = createContext()class UserProvider extends Component {  state = {    loggedInUser: null  }  handleLogin = evt => {    evt.preventDefault()    this.setState({      loggedInUser: USER    })  }  render () {    const { loggedInUser } = this.state    return (      <Provider        value={{          user: loggedInUser,          handleLogin: this.handleLogin        }}      >        {this.props.children}      </Provider>    )  }}export { UserProvider as default, Consumer as UserConsumer }
```

This represents the content of the new `context/UserContext.js` file. The logic previously handled by the `Root` component has been moved here.

Note how it handles every logic regarding the `loggedInUser` state value, and passes the needed values to `children` via a `Provider`.

```
...<Provider     value={{       user: loggedInUser,       handleLogin: this.handleLogin      }}     >      {this.props.children}</Provider>...
```

In this case, the `value` prop is an object with the `user` value, and function to update it, `handleLogin`.

Also note that the Provider and Consumer are both exported. This makes it easy to consume the values from any components in the application.

```
export { UserProvider as default, Consumer as UserConsumer }
```

With this decoupled setup, you can use the `loggedInUser` state value anywhere in your component tree, and have it updated from anywhere in your component tree as well.

Here’s an example of using this in the `Greeting` component:

```
import React from 'react'import { UserConsumer } from '../context/UserContext'const Greeting = () => {  return (    <UserConsumer>      {({ user }) => <p>Welcome, {user.name}! </p>}    </UserConsumer>  )}export default Greeting
```

How easy.

Now, I’ve taken the effort to delete every reference to `loggedInUser` where the prop had to be passed down needlessly. Thanks, Context!

For example:

```
// before const User = ({ loggedInUser, profilePic }) => {  return (    <div>      <img src={profilePic} alt='user' />      <Greeting loggedInUser={loggedInUser} />    </div>  )}// after: Greeting consumes UserContext const User = ({profilePic }) => {  return (    <div>      <img src={profilePic} alt='user' />      <Greeting />     </div>  )}export default User
```

Be sure to look in the accompanying code folder for the final implementation i.e. after stripping off the `loggedInUser` from being passed down needlessly.

#### Updating Context Values.

_What’s a bank app if you can’t make withdrawals, huh?_

Well, this app has some buttons. You click them and voilà, a withdrawal is made.

![Image](https://cdn-media-1.freecodecamp.org/images/-o1b6Cx1S97BwM1GzYQ7mjCgyHOxtdVRhFZ2)
_The withdrawal buttons_

Since the `totalAmount` value resides in the `loggedInUser` object, we may as well have the logic to make withdrawals in the `UserContext.js` file.

Remember we’re trying to centralise all logic related to the user object in one place.

To do this, we’ll extend the `UserProvider` in `UserContext.js` to include a `handleWithdrawal` method.

```
// UserContext.js... handleWithdrawal = evt => {    const { name, totalAmount } = this.state.loggedInUser    const withdrawalAmount = evt.target.dataset.amount
```

When you click any of the buttons, we will invoke this `handleWithdrawal` method.

From the `evt` click object passed as an argument to the `handleWithdrawal` method, we then pull out the amount to be withdrawn from the `dataset` object.

```
const withdrawalAmount = evt.target.dataset.amount
```

This is possible because both buttons have a `data-amount` attribute set on them. For example:

```
<button data-amount=1000 />
```

Now that we have the `handleWithdrawal` method written out, we can expose it via the `values` prop passed to `Provider` as shown below:

```
<Provider    value={{       user: loggedInUser,       handleLogin: this.handleLogin       handleWithdrawal: this.handleWithdrawal     }}   >  {this.props.children}</Provider>
```

Now, we’re all set to consume the `handleWithdrawal` method from anywhere in the component tree.

In this case, our focus is on the `WithdrawButton` component. Go ahead and wrap that in a `UserConsumer`, deconstruct the `handleWithdrawal` method and make it the click handler for the buttons as shown below:

```
const WithdrawButton = ({ amount }) => {  return (    <UserConsumer>      {({ handleWithdrawal }) => (        <button          data-amount={amount}          onClick={handleWithdrawal}        >          WITHDRAW {amount}        </button>      )}    </UserConsumer>  )}
```

![Image](https://cdn-media-1.freecodecamp.org/images/FvzJEuO9sAL6RIJgSZ5a9WznJPMhhXcqrQl6)
_On logging in, the withdrawal now works as expected._

And that works!

#### Conclusion

This illustrates that you can pass not only state values, but also their corresponding updater functions in a context Provider. These will be available to be consumed anywhere in your component tree.

Having made the bank app work well with the Context API, I’m pretty sure John will be proud of the progress we’ve made!

### Chapter 3: ContextType — Using Context without a Consumer.

![Image](https://cdn-media-1.freecodecamp.org/images/6P3dyJTbFpm4ovPY1u6MtSwKr-lCQ9Ef5y2N)

So far, John has had a great experience with the Context. Thanks to Mia who recommended such great tool.

However, there’s a little problem.

As John uses the context API more often, he begins to realise a problem.

![Image](https://cdn-media-1.freecodecamp.org/images/p8ELt767Lxgpql6OJUMdrJTrM3-IeVyYcav7)

When you have multiple `Consumers` within a component, it results in having a lot of nested, not-so-pleasant code.

Here’s an example.

While working on the _Benny Home Run_ application, John had to create a new context object to hold the game level state of the current user.

```
// initial context objectconst BennyPositionContext = createContext({ 	x: 50, 	y: 50 })
```

```
// another context object for game level i.e Level 0 - 5 const GameLevelContext = createContext(0)
```

Remember, it’s common practice to split related data into different context objects for reusability and performance (owing to the fact the every consumer is re-rendered when values within a `Provider` change)

With these context objects, John goes ahead to use both `Consumer` components within the `Benny` component as follows.

```
//grab consumer for PositionContextconst { Consumer: PositionConsumer } = BennyPositionContext
```

```
// grab consumer for GameLevelContextconst { Consumer: GameLevelConsumer } = GameLevelContext
```

```
// use both Consumers here.const Benny = () => {  return <PositionConsumer>    {position => <GameLevelConsumer>        {gameLevel => <svg /&gt;}    </GameLevelConsumer>}  </PositionConsumer>}
```

Do you notice that consuming values from both context objects results in very nested code?

Well, this is one of the more common problem with consuming data with the `Consumer` component. With multiple consumer components, you begin to have a lot of nesting.

So, what can we do about this?

Firstly, when we learn about Hooks in a later chapter, you’ll come to see an almost perfect solution to this. In the mean time, let’s consider the solution available to `Class` components via something called`contextType`.

#### Using a Class Component with contextType.

To take advantage of `contextType` you’re required to work with a class component.

Consider the `Benny` component rewritten as a class component.

```
// create context objectconst { Provider, Consumer } = createContext({ x: 50, y: 50 })// Class componentclass Benny extends Component {  render () {    return <Consumer>    {position => <svg />}  &lt;/Consumer>  }}
```

In this example, `Benny` consumes the initial context values `{ x: 50, y: 50 }` from the context object.

However, using a `Consumer` forces you to use a render prop API that may lead to nested code.

Let’s get rid of the `Consumer` component by using the `contextType` class property.

![Image](https://cdn-media-1.freecodecamp.org/images/-9MBEu7r7Ix1SwRWzIUmnem0PM7j-7iUC9pe)

Getting this to work is fairly easy.

First, you set the `contextType` property on the class component to a context object.

```
const BennyPositionContext = createContext({ x: 50, y: 50 })// Class Benny extends Component ... // look here ?Benny.contextType = BennyPositionContext 
```

After setting the `contextType` property, you can go ahead to consume values from the context object by using `this.context`.

For example, to retrieve the position values `{ x: 50, y: 50 }`:

```
class Benny extends Component {  render () {    // look here. No nesting!    const position = this.context    return <svg />  }}
```

#### The Perfect Solution?

Using the `contextType` class property is great, but not particularly the best solution in the world. You can only use one `contextType` within a class component. This means if you need to introduce multiple `Consumers` you’ll still have some nested code.

#### Conclusion

The `contextType` property is does solve the nesting problem a little bit.

However, when we discuss Hooks in a later chapter, you’ll see how much better the solution hooks offer is.

### Chapter 4: React.memo === Functional PureComponent.

![Image](https://cdn-media-1.freecodecamp.org/images/571cqFlK3HszMqIiZJpy0gBqveysWJ1rJPDQ)

A few weeks ago John refactored the `Benny` component to a `PureComponent`.

Here’s what his change looked like:

Well, that looks good.

However, the only reason he refactored the `Benny` component to a class component was because be needed to extend `React.PureComponent`.

![Image](https://cdn-media-1.freecodecamp.org/images/ziP13p9hVF0bwg2iRIbWX-cPgKHnqlJU2Hx8)

The solution works, but what if we could achieve the same effect without having to refactor from functional to class components?

Refactoring large components just because you need a specific React feature isn’t the most pleasant of experiences.

#### How React.memo works.

`React.memo` is the perfect replacement for the class’ `PureComponent`. All you do is wrap your functional component in the `React.memo` function call and you get the exact behaviour `PureComponent` gives.

Here’s a quick example:

```
// before import React from 'react'function MyComponent ({name}) {     return ( <div>        Hello {name}.            </div>    )}export default MyComponent
```

```
// after import React, { memo } from 'react'export default  memo(function MyComponent ({name}) {    return ( <div>        Hello {name}.            </div&gt;    )})
```

So simple, it couldn’t get any easier.

Technically, `React.memo` is a higher order function that takes in a functional component and returns a new memoized component.

So, if props do not change, `react` will skip rendering the component and just use the previously memoized value.

With this new found information, John refactors the functional component, `Benny` to use `React.memo`.

#### Handling Deeply Nested Props.

`React.memo` does a props [shallow comparison](https://stackoverflow.com/questions/36084515/how-does-shallow-compare-work-in-react). By implication, if you have nested props objects, the comparison will fail.

To handle such cases, `React.memo` takes in a second argument, an equality check function.

Here’s a basic example:

```
import React, { memo } from 'react'export default  memo (function MyComponent (props) {      return ( <div>        Hello World from {props.name.surname.short}            </div&gt;    )}, equalityCheck)
```

```
function equalityCheck(prevProps, nextProps) {  // return perform equality check & return true || false}
```

If the `equalityCheck` function returns `true`, no re-render will happen. This would mean that the current props and previous props are the same. If you return `false`, then a re-render will occur.

If you’re concerned about incurring extra performance hits from doing a deep comparison, you may use the lodash [isEqual](https://lodash.com/docs/4.17.11#isEqual) utility method.

```
import { isEqual } from 'lodash'function equalityCheck(prevProps, nextProps) {	return isEqual(prevProps, nextProps) }
```

#### Conclusion.

`React.memo` brings the class `PureComponent` behaviour to functional components. We’ve also had a look at using the `equalityCheck` function as well. If you use the `equalityCheck` function, be sure to include checks for function props where applicable. Not doing so is a common source of bugs in many React applications.

### Chapter 5: The Profiler — Identifying Performance Bottlenecks.

![Image](https://cdn-media-1.freecodecamp.org/images/zWaetnakr8Rws03aoH9p6-Y7CF75XxniARP6)

It’s Friday and Mia is headed back home. On her way home she can’t help but think to herself.

![Image](https://cdn-media-1.freecodecamp.org/images/T0y1iNNOpJPISg5U9IRpgEifQ7RTQGRY8kj6)

“_What have I achieved today?_” Mia says her to herself.

After a long careful thought, she comes to the conclusion that she accomplished just one thing the entire day.

![Image](https://cdn-media-1.freecodecamp.org/images/FFniQ2ufSTseN1CtbH8b9DEOZj9zVZK75B67)

Well, how is it possible that Mia only achieved one thing the entire day?

That ‘one thing’ had better be a worthy feat!

So, what was Mia’s accomplishment for the day?

![Image](https://cdn-media-1.freecodecamp.org/images/PR3kr9PlZMki7Ea0sDH7SG3tbgLP6gDkBwey)

It turns out that all Mia accomplished today was sitting helplessly as her browser attempted to load a page for 7 hours!

![Image](https://cdn-media-1.freecodecamp.org/images/p436ow1UJo09-3-IHLllkrye9K3aNwyEjELS)

What???

#### Measuring Performance in React Apps.

Web performance is a big deal. Nobody has all the time in the world to sit through minutes waiting for your webpage to load.

In order to measure performance and identify performance bottlenecks in your apps, it’s crucial to have some way to inspect how long it took your app’s components to render, and why they were rendered.

This is exactly why the Profiler exists.

If you’ve been writing react for sometime, you might remember the `react-addons-perf` module.

Well, that has been deprecated in favour of the Profiler.

![Image](https://cdn-media-1.freecodecamp.org/images/JSCb7hooD8c0awGqsL5gwBIyU3XLiLmbdXqU)

With the Profiler, you can:

* Collect timing information about each component
* Easily identify performance bottlenecks
* Be sure to have a tool compatible with concurrent rendering

#### Getting Started.

To keep this as pragmatic as possible, I have set up a tiny [application](https://github.com/ohansemmanuel/fake-medium) we’re going to profile together. i.e measure performance. We’ll do this with the aid of the Profiler.

I call the application _fake-medium_, and it looks like this:

![Image](https://cdn-media-1.freecodecamp.org/images/BKUaV-v1lOJWBCqmYBWQ1t9dGhK-PLhxa13K)
_The Fake-medium app_

You’ll find the source code for the application in the code repository for this book.

To Install the dependencies and run the app, run the following from the`04-The-Profiler` directory:

```
cd fake-mediumyarn install yarn start
```

If you ran those commands, you should have the application running in your default browser, on port `3000` or similar.

![Image](https://cdn-media-1.freecodecamp.org/images/ArMFy-gNKE3TQnNHb18m087ww9yx7wmT2VZR)
_Application running on some local port._

Finally, open your chrome devtools by pressing Command+Option+J (Mac) or Control+Shift+J (Windows, Linux, and Chrome OS).

Then find the React [chrome devtools](https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi?hl=en) extension tab and click it.

![Image](https://cdn-media-1.freecodecamp.org/images/i0jScYALcHijfkwCh7-4rstjV1R7cMNkVslV)

You’ll be presented with two tabs, elements and profiler.

You guessed right, our focus is on the profiler tab, so please click it.

![Image](https://cdn-media-1.freecodecamp.org/images/Ea5nQBoaX-Yam1aKnwXogZM4RnSobpwuuwF0)

Doing so will lead you to the following page:

![Image](https://cdn-media-1.freecodecamp.org/images/n25grg6bFRAZhVz1Pqup5QcaHO3kspVp5pX1)

#### How does the Profiler Work?

The Profiler works by recording a session of actual usage of your application. In this recording session it gathers information about the components in your application and displays some interesting information you can exploit to find performance bottlenecks.

To get started, click the record button.

![Image](https://cdn-media-1.freecodecamp.org/images/475E6wqCElRnsNOj5i3V0zuEjSWu50Znu1zl)

After clicking ‘record’, you then go ahead to use your application as you’d expect a user to.

In this case, I’ve gone ahead to click the medium clap button 3 times!

![Image](https://cdn-media-1.freecodecamp.org/images/ZS2LZOif-tK5y2jDZVzFKEql8DNPUaJcqrge)

Once you’re done interacting with your application, hit stop to view the information the Profiler provides.

#### Making Sense of the Profiler Results.

On the far right of the profiler screen, you’ll find a visual representation of the number of commits made during your interaction with your application.

![Image](https://cdn-media-1.freecodecamp.org/images/Fw0NAsuDAeeQhEVBaUxbvSybbwSgnKnZkh6z)

Conceptually, react does work in 2 phases. The render phase where components are rendered and the virtual DOM _diffed_, and the commit phase where actual changes in the virtual DOM are committed to the DOM.

The graphical representation you see on the far right of the profiler represents the number of commits that were made to the DOM during your interaction with the app.

![Image](https://cdn-media-1.freecodecamp.org/images/vt00nWdS03-5irdzKMO2wrz-NzsoC9e2zDN8)

The taller the bar is, the longer it took `React` to render the components in this commit.

In the example above, the Profiler recorded three commits. That make sense since I clicked the button only 3 times. So, there should be only 3 commits made to the DOM.

Also the first commit took much longer than the subsequent two commits.

The three bars represent the different commits made to the DOM, and you can click on any to investigate performance metrics for the particular commit.

![Image](https://cdn-media-1.freecodecamp.org/images/TvR2Lh4xKXyU1fZ9MBxtVRZUE6xDRZoGcS65)

#### The Flame Chart.

After a successful recording session, you’ll be presented with a couple different bits of information about your components.

First, you have 3 tabs representing different groups of information — each relating to the selected commit on the right.

![Image](https://cdn-media-1.freecodecamp.org/images/C7RLaaqstiCC3EQX5BqSIqmyXX3bqQgGiOQL)

The first tab represents a flame chart.

The flame chart displays information on how long it took your component tree to render.

![Image](https://cdn-media-1.freecodecamp.org/images/NNlVjulXdYdxRBKtxJeGfA-CKyg19nbWXQ1x)

You’ll notice that each component in your application tree is represented by bars of varying lengths and colors.

The length of a bar defines how long it took the component (and its children) to render.

Judging by the bar length, it appears the `Provider` component took the longest time to render. That make sense since the `Provider` is the main root component of the app, so the time represented here is the time taken for `Provider` and all its children to render.

That’s half the story.

Note that the colors of the bars are different.

![Image](https://cdn-media-1.freecodecamp.org/images/xCTIztG-igaUJS0bcwzJp9cazGEFNLhT2Vt2)

For example, `Provider` and a couple other components have a _grey_ color.

What does that mean?

Well, first we are investing the first commit made to the DOM during the interaction with the application.

![Image](https://cdn-media-1.freecodecamp.org/images/CJj3CvGXLDJw8K4QlhvuSG2mYhXvybzjToQ1)

The components with a grey color means they weren’t rendered in this commit. If the component is greyed out, it wasn’t rendered in this commit. So, the length of the bar only represents how long it took the component to render _previously_ before this commit i.e. before the interaction with the application.

If you think about it, that’s reasonable.

On careful examination, you’ll see that the only component with a different flame chart color here is the `Clap` component.

![Image](https://cdn-media-1.freecodecamp.org/images/Nxfa35snkv9yqhL7qH8BmnQzLNwl0Cfd1lUa)

This component represents the Medium clap button that was clicked.

A yellow bar means the component took the most time to render in this commit.

Well, no other component is coloured which means the `Clap` button was the only component re-rendered in this commit.

That’s perfect!

You don’t want to click the `Clap` button and have a different component being re-rendered. That’ll be a performance hit right there.

In more complex applications, you’ll find flame charts with not just yellow and grey bars. You’ll find some with blue bars.

What’s worth noting is that, yellow longer bars took more time to render, followed by the blue ones, and finally grey bars weren’t re-rendered in the particular commit being viewed.

It’s also possible to click on a particular bar to view more information on why it rendered or not i.e. the props and state passed to the component.

![Image](https://cdn-media-1.freecodecamp.org/images/Zp6admN1LQ-my7sNhTyHOPuIy83tnfEDg4kE)

![Image](https://cdn-media-1.freecodecamp.org/images/68c6x0Hkn1WUsZFUadliBQ4KFieNlHLygSdY)

While zoomed in, you can also click the commit bars on top to see the difference in `props` or `state` across each commit render.

#### The Ranked Chart.

Once you understand how the flame chart works, the ranked chart becomes a walk in the park.

The second tab option refers to the ranked chart.

![Image](https://cdn-media-1.freecodecamp.org/images/OzHE40WoR-zj50CdTEzoLtXA-RqwjOfA3HRo)

The ranked chart displays every component that was rendered in the commit being viewed. It displays this components ranked from top to bottom — with component which took more time to render at the top.

In this example, we have just the `Clap` component displayed in the ranked chart view. That’s okay as we only expect the `Clap` component to be re-rendered upon clicking.

![Image](https://cdn-media-1.freecodecamp.org/images/-4zbLrlGiQ7JV7hhz2ZOMrTXcCg730UhzLEF)

A more complex ranked chart may look like this:

![Image](https://cdn-media-1.freecodecamp.org/images/sSqE66OzdqOUinWUWiX9cVwY3u65gsLToquC)
_Ranked chart from an application we’ll profile next_

You can see how the longer yellow bars are right there at the top, and shorter blue bars at the bottom. If you look carefully, you’ll notice that the colors fade as you go from top to bottom. From more yellow bars to pale yellow bars, to light blue bars and finally blue bars.

#### Component Chart.

Whenever you zoom into a component within the Profiler i.e. by clicking its associated bar, a new option on the right pops up.

![Image](https://cdn-media-1.freecodecamp.org/images/24jjhxXViuYu7SwY4pzS-YmM4Kiapn-h6SJN)

**Clicking this button** will bring you to what’s called the component chart.

The component chart displays how many times a particular component was re-rendered during the recorded interaction.

In this example, I can click the button to view chart for the `Clap` component.

![Image](https://cdn-media-1.freecodecamp.org/images/NYtuqFfiwdiHnMazAfjh9qu4cSs4u9HmU-Z2)

This shows three bars representing the three times the `Clap` component was re-rendered. If I saw a fourth bar here, I’d begin to get worried as I only clicked three times and expected only three re-renders.

If the selected component didn’t re-render at all, you’ll be presented with the empty screen below:

![Image](https://cdn-media-1.freecodecamp.org/images/r4jafAzBQZq-nNhFsmVR2v-71vFhWcboRcOf)

**NB**: you can either view the component chart by clicking the button on the far right, or by double clicking a component bar from the flame or ranked chart.

#### Interactions.

There’s one final tab in the profiler, and by default it displays an empty screen:

![Image](https://cdn-media-1.freecodecamp.org/images/gK7ayEjVRfzz3a5sku7ySISv97r6llrO4NqS)

**Interactions** let you tag actions performed during a recording session with a string identifier so they can be monitored and tracked within the profiling results.

The API for this is unstable, but here’s how to enable interactions in your profiling results.

First install the `scheduler` module. From your terminal, run `yarn add scheduler` within the application directory .

Once the installation is done, you need to use `unstable_trace` function exported by the module as shown below:

```
import { unstable_trace as trace } from 'scheduler/tracing'
```

The function is exported as `unstable_trace` but you can rename it in the import statement as I have done above.

The `trace` function has a signature similar to this:

```
trace("string identifier", timestamp, () = {})
```

It takes a string identifier, timestamp and a callback function. Ideally, you track whatever interaction you want by passing it into the callback.

For example, I have gone ahead to do this in the `fake-medium` application:

```
// before _handleClick () {   // do something}
```

```
// after _handleClick () {   trace("Clap was clicked!", window.performace.now(), () => {  	  // do something   })}
```

The medium clap when clicked calls the `_handleClick` method. Now, I’ve wrapped the functionality within the `trace` method.

Here’s what happens when the profiling result is now viewed:

![Image](https://cdn-media-1.freecodecamp.org/images/rFrMBm33GE-2KV4WKmxx5Z8ZmVcrEDUhTjdw)

Clicking three times now records 3 interactions and you can click on any of the interactions to view more details about them.

![Image](https://cdn-media-1.freecodecamp.org/images/xqP3wRyaTYbFwyIMdrrQ26ns3qmdVerQDDDZ)

The interactions will also show up in the flame and ranked charts.

![Image](https://cdn-media-1.freecodecamp.org/images/VIdivXfnxkXhPZXQLNz0Ahp8mTDwO-gYM9rF)

#### Example: Identifying Performance BottleNecks in the Bank Application.

“_Hey John, what have you done?!!!_”, said Mia as she stumped into John’s office.

“_I was just profiling the bank application, and it’s so not performant”,_ she added.

John wasn’t surprised. He had not spent a lot of time thinking about performance, but with Mia up in his face, he began to have a rethink.

“_Okay, I’ll have a look and fix whatever bottlenecks I find. Can we do that together?_”, John said while thinking to himself how much help Mia would be since she spotted the problem anyway.

“_Oh, sure_”, she retorted.

After spending a couple hours, they found and fixed a coupe of performance bottlenecks in the application.

What did they do? What measures were taken?

In this example, we’ll spin up the bank application and pick up from where we stopped in the earlier chapter. This time we’ll fix the performance bottlenecks within the application.

Here’s what the bank app looks like again:

![Image](https://cdn-media-1.freecodecamp.org/images/7Yzv8gVG3AnyrZh4J0r3Mo4vyNcLRp1Hm7QC)

#### Noting the Expected Behaviour.

When I need to profile an application, specifically during a certain interaction with an app, I like to set the baseline for what I expect in terms of performance. This sort of expectation helps you retain your focus as you delve into interpreting the results from the Profiler.

Let’s consider the bank application we want to profile. The interaction in the bank app is simple. You click a set of buttons, and the withdrawal amount is updated.

![Image](https://cdn-media-1.freecodecamp.org/images/wsUrSq6yFhdypOPmvWWN0YK47-0ElKftTPt2)
_The basic interaction of the app_

Now, what would you consider the expected behaviour of this app with respect to re-renders and updates?

Well, for me, it’s quite simple.

The only part of the app visually changing is the withdrawal amount. Before going into the profiling session, my expectation for a performant application will be that no unnecessary components are re-rendered, just the component responsible for updating the total amount.

![Image](https://cdn-media-1.freecodecamp.org/images/EQ7JvduM5RuBWJdAmA8UsUmzqK1xk2psHuOq)
_Where I expect re-renders to happen. Nowhere else._

Give or take, I’ll expect just the `TotalAmount` component to be re-rendered, or any other component directly connected with that update.

With this expectation set, let’s go on and profile the application.

The steps are the same as discussed earlier. You open your `devtools`, record an interaction session, and begin to interpret the results.

Now, I have gone ahead to record a session. In this session, all I did was click the “withdraw $10,000” button 3 times.

![Image](https://cdn-media-1.freecodecamp.org/images/nJ9QImh8qxEDpRSpoxqRJ4AvbVv886-8NWpD)

Here’s the flame chart from the profiling session:

![Image](https://cdn-media-1.freecodecamp.org/images/ssqiTuWu9mm8YKwjYBS6cfhCabx2DznFkEg8)
_Flame chart results_

Oh my! From the chart above, so many components were re-rendered. You see the many bar colours represented in the flame chart ?

This is far from ideal, so let’s begin to fix the problem.

#### Interpreting the Flame chart.

First let’s consider what’s likely the root of the problem here. By default, whenever a `Provider` has its `value` changed, every child component is forced to re-render. That’s how the `Consumer` gets the latest values from the `context` object and stays in sync.

The problem here is that every component apart from `Root` is a child of `Provider` — and they all get re-rendered needlessly!

![Image](https://cdn-media-1.freecodecamp.org/images/uEpyKNJFol4T15woTC7xYqulFpPTT5663vXe)
_All children components re-rendered with a change in the Provider’s value._

So, what can we do about this?

Some of the child components don’t need to be re-rendered as they are not directly connected with the change.

First, let’s consider the first child component, `App`.

![Image](https://cdn-media-1.freecodecamp.org/images/AQurw0t4lQ210joddkcWyiTrKqQjqs2PpiSb)

The `App` component doesn’t receive any `prop` and it only manages the state value `showBalance`.

```
class App extends Component {  state = {    showBalance: false  }  displayBalance = () => {    this.setState({ showBalance: true })  }  render () {    const { showBalance } = this.state    ...  }}
```

It isn’t directly connected with the change, and it’s pointless to re-render this component.

Let’s fix this by making it a `PureComponent`.

```
// before class App extends Component {  state = {    showBalance: false  } ... }// after class App extends PureComponent {  state = {    showBalance: false  } ... }
```

Having made `App` a `PureComponent`, did we make any decent progress?

Well, have a look at the new flame chart generated after that simple (one-liner) change.

![Image](https://cdn-media-1.freecodecamp.org/images/39wb21xBzdec7MPDtiihvIqhLDOxFNokPfaD)

Can you see that?

A lot of App’s children aren’t re-rendered needlessly, and we have a more sane flame graph now.

Great!

#### Profile Different Interactions.

It’s easy to assume that because we had fewer re-renders in the “withdraw amount” interaction we now have a performant app.

That’s not correct.

App’s now a `PureComponent`, but what happens when `App` gets rendered owing to a `state` change?

Well, let’s profile a different interaction. This time, load up the application and profile the interaction for viewing an account balance.

![Image](https://cdn-media-1.freecodecamp.org/images/fiErzN0w3LSxjNeMoYkqBZuYKnzQI5PIor25)

If you go ahead and profile the interaction, we get a completely different result.

![Image](https://cdn-media-1.freecodecamp.org/images/qMp4Ks9sIm1nMwkZqcPn8ZqtQ8Ig3dUMr-7P)
_Screencast showing the interaction being profiled._

Now, what’s changed?

![Image](https://cdn-media-1.freecodecamp.org/images/6vY2o4-trUJgVEOT9xbcAkP4xFitc0sQIUVC)

From the flame graph above, every child component of `App` as been re-rendered. They all had nothing to do with this visual update, so those are wasted rendered.

NB: If you need to check the hierarchy of components more clearly, remember you can always click the elements tab:

![Image](https://cdn-media-1.freecodecamp.org/images/1D22MNaRUJ4dNwTMURzFBV9agzNJVAVSyvaB)

Well, since these child components are functional components, let’s use `React.memo` to memoize the render results so they don’t change except there’s a change in props.

```
// User.jsimport { memo } from 'react'const User = memo(({ profilePic }) => {  ...})
```

```
// ViewAccountBalance.jsimport { memo } from 'react'const ViewAccountBalance = memo(({ showBalance, displayBalance }) => {      ...})
```

```
// WithdrawButton.jsimport { memo } from 'react'const WithdrawButton = memo(({ amount }) => {    ...  )})
```

Now, when you do that and re-profile the interaction, we get a much nicer flame chart:

![Image](https://cdn-media-1.freecodecamp.org/images/vWFaZzoArl9dpgS1Pnq81szMWgMnTxE5hXGW)

Now, only `ViewAccountBalance` and other child components are re-rendered. That’s okay.

When you view your flame chart i.e if you’re following along, you may see something slightly different.

The names of the component may not be shown. You get the generic name `Memo` and it becomes difficult to track which component is what.

![Image](https://cdn-media-1.freecodecamp.org/images/jvKxSY6aIsr2b5LaoGKexRg3jKOkH0GzvOqz)

To change this, set the `displayName` property for the memoized components.

Below’s an example.

```
// ViewAccountBalance.jsconst ViewAccountBalance = memo(({ showBalance, displayBalance }) => {  ...})
```

```
// set the displayName hereViewAccountBalance.displayName = 'ViewAccountBalance'
```

You go ahead and do this for all the memoized functional components.

#### The Provider Value.

We’re pretty much done with resolving the performance leaks in the application, however, there’s one more thing to do.

The effect isn’t very obvious in this application, but will come handy as you face more cases in the real world such as in situations where a `Provider` is nested within other components.

The implementation of the `Provider` in the bank application had the following:

```
...<Provider    value={{       user: loggedInUser,       handleLogin: this.handleLogin       handleWithdrawal: this.handleWithdrawal     }}   >  {this.props.children}</Provider>...
```

The problem here is that we’re passing a new object to the `value` prop every single time. A better solution will be to keep a reference to these values via state. e.g.

```
<Provider value={this.state}>	{this.props.children}</Provider>
```

Doing this requires a bit of refactoring as shown below:

```
// context/UserContext.jsclass UserProvider extends Component {  constructor () {    super()    this.state = {      user: null,      handleLogin: this.handleLogin,      handleWithdrawal: this.handleWithdrawal    }  }  ...  render () {    return <Provider value={this.state}>  		{this.props.children}	</Provider>  }}
```

Be sure to look in the associated code folder if you need more clarity on this.

#### Conclusion.

Profiling applications and identifying performance leaks is fun and rewarding. I hope you’ve gained relevant knowledge in this section.

### Chapter 6: Lazy Loading with React.Lazy and Suspense.

![Image](https://cdn-media-1.freecodecamp.org/images/f4WHq-CWHVcLzpw3WmDmuTfOdZCbreBf4fRJ)

“_Hey John, we need to look into lazy loading some modules in the Benny application_”, says Tunde, John’s manager.

John’s had great feedback from his manager for the past few months. Every now and then Tunde storms into the office with a new project idea. Today, it’s lazy loading with `React.Lazy` and `Suspense`.

John’s never lazy loaded a module with React.Lazy and Suspense before now. This is all new to him, so he ventures into a quick study to deliver on what his manager has requested.

#### What is Lazy Loading?

When you bundle your application, you likely have the entire application bundled in one large chunk.

As your app grows, so does the bundle.

![Image](https://cdn-media-1.freecodecamp.org/images/-eEQQvR2dpfwYIIW45KUncl6orjYCfsIUSKv)

To understand lazy loading, here’s the specific use case Tunde had in mind when he discussed with John.

“_Hey John, do you remember the Benny app has an initial home screen?_”, said Tunde.

By initial home scree, Tunde was referring to this:

![Image](https://cdn-media-1.freecodecamp.org/images/WLAaGYYoijsLOrcC6jDilA81UbYyiwoREfg3)

This is the first screen the user encounters when they visit the Benny game. To begin playing the game, you must click the “Start Game” button to be redirected to the actual game scene.

“_John, the problem here is that we’ve bundled all our React components together and are all served to the user on this page_”.

“_Oh, I see where you’re going_”, said John.

“_Instead of loading the `GameScene` component and its associated assets, we could defer the loading of those until the user actually clicks ’Start Game’, huh?_”, said John.

And Tunde agreed with a resounding “_Yes, that’s exactly what I mean_”.

Lay loading refers to deferring the loading of a particular resource until much later, usually when a user makes an interaction that demands the resource to be actually loaded. In some cases it could also mean preloading a resource.

Essentially, the user doesn’t get the lazy loaded bundle served to them initially, rather it is fetched much later at runtime.

This is great for performance optimisations, initial load speed etc.

React makes lazy loading possible by employing the dynamic import syntax.

Dynamic imports refer to a `tc39` syntax [proposal for javascript](https://github.com/tc39/proposal-dynamic-import), however, with transpilers like Babel, we can use this syntax today.

The typical, static way of importing a module looks like this:

```
import { myModule } from 'awesome-module'
```

While this is desirable in many cases, the syntax doesn’t allow for dynamically loading a module at runtime.

Being able to dynamically load a part of a Javascript application at runtime makes way for interesting use cases such as loading a resource based on a user’s language (a factor that can only be determined at runtime), or only loading some code just when it is likely to be used by the user (performance gains).

For these reasons (and more) there’s a [proposal](https://github.com/tc39/proposal-dynamic-import) for introducing the dynamic import syntax to Javascript.

Here’s what the syntax looks like:

```
import('path-to-awesome-module')
```

It has a syntax similar to a function, but is really not a function. It doesn’t inherit from `Funtion.proptotype` and you can’t invoke methods such as `call` and `apply`.

The returned result from the dynamic import call is a promise which is resolved with the imported module.

```
import('path-to-awesome-module')	.then(module => {     // do something with the module here e.g. module.default() to invoke the default export of the module. })
```

#### Using React.lazy and Suspense.

`React.lazy` and `Suspense` make using dynamic imports in a React application so easy.

For example, consider the demo code for the Benny application below:

```
import React from 'react'import Benny from './Benny'import Scene from './Scene'import GameInstructions from './GameInstructions'
```

```
class Game extends Component {  state = {    startGame: false  }  render () {    return !this.state.startGame ?         <GameInstructions /> : 		<Scene />  }}export default Game;
```

Based on the state property `startGame`, either the `GameInstructions` or `Scene` component is rendered when the user clicks the “Start Game” button.

`GameInstructions` represents the home page of the game and `Scene` the entire scene of the game itself.

In this implementation, `GameInstructions` and `Scene` will be bundled together in the same Javascript resource.

Consequently, even when the user hasn’t shown intent to start playing the game, we would have loaded and sent to the user, the complex `Scene` component which contains all the logic for the game scene.

So, what do we do?

Let’s defer the loading of the `Scene` component.

Here’s how easy `React.lazy` makes that.

```
// before import Scene from './Scene'
```

```
// now const Scene = React.lazy(() => import('./Scene'))
```

`React.lazy` takes a function that must call a dynamic import. In this case, the dynamic import call is `import('./Scene')`.

Note that `React.lazy` expects the dynamically loaded module to have a `default` export containing a React component.

With the `Scene` component now dynamically loaded, when the application is bundled for production, a separate module (or javascript file) will be created for the `Scene` dynamic import.

When the app loads, this javascript file won’t be sent to the user. However, if they click the “Start Game” button and show intent to load the `Scene` component, a network request would be made to fetch the resource from the remote server.

Now, fetching from the server introduces some latency. To handle this, wrap the `Scene` component in a `Suspense` component to show a fallback for when the resource is being fetched.

Here’s what I mean:

```
import { Suspense } from 'react'const Scene = React.lazy(() => import('./Scene'))
```

```
class Game extends Component {  state = {    startGame: false  }  render () {    return !this.state.startGame ?         <GameInstructions /> : 		// look here		<;Suspense fallback="<div>loading ...</div>">		  <Scene />		</Suspense>  }}export default Game;
```

Now, when the network request is initiated to fetch the `Scene` resource, we’ll show a “loading…” fallback courtesy the `Suspense` component.

`Suspense` takes a `fallback` prop which can be a markup as shown here, or a full blown React component e.g. a custom loader.

With `React.lazy` and `Suspense` you can suspend the fetching of a component until much later, and show a fallback for when the resource is being fetched.

How convenient.

Also, you can place the `Suspense` component anywhere above the lazy loaded component. In this case the `Scene` component.

If you also had multiple lazy loaded components, you could wrap them in a single `Suspense` component or multiple, depending on your specific use case.

#### Handling Errors.

In the real-world, things break often, right?

It’s possible that in the process of fetching the lazy loaded resource, a network error occurs.

To handle such case, be sure to wrap your lazy loaded components in an _Error Boundary_.

Remember error boundaries from the Lifecycle method chapter?

Here’s an example:

```
import { Suspense } from 'react'import MyErrorBoundary from './MyErrorBoundary'const Scene = React.lazy(() => import('./Scene'))class Game extends Component {  state = {    startGame: false  }
```

```
  render () {    return &lt;MyErrorBoundary>         {!this.state.startGame ?            <GameInstructions /> : 		   <Suspense fallback="loading ...">		     <Scene />;		   </Suspense>}		</MyErrorBoundary>  }}export default Game;
```

Now, if an error occurs while fetching the lazy loaded resource, it’ll be graciously handled by the error boundary.

#### No named exports.

If you remember from the section above, I did mention that `React.lazy` expects the dynamic import statement to include a module with a **default export** being a React component.

At the moment, `React.lazy` doesn’t support named exports. That’s not entirely a bad thing, as it keeps tree shaking working so you don’t import actual unused modules.

Consider the following module:

```
// MyAwesomeComponents.js export const AwesomeA = () => <div> I am awesome </div> export const AwesomeB = () => <div> I am awesome </div> export const AwesomeC = () => <div> I am awesome </div>
```

Now, if you attempt to use `React.lazy` with a dynamic import of the module above, you’ll get an error.

```
// SomeWhereElse.js const Awesome = React.lazy(() => import('./MyAwesomeComponents'))
```

That won’t work since there’s no default export in the `MyAwesomeComponents.js` module.

A workaround would be to create some other module that exports one of the components as a default.

For example, if I was interested in lazy loading the `AwesomeA` component from the `MyAwesomeComponents.js` module, I could create a new module like this:

```
// AwesomeA.js export { AwesomeA as default } from './MyAwesomeComponents'
```

Then I can can go ahead to effectively use `React.lazy` as follows:

```
// SomeWhereElse.jsconst AwesomeA = React.lazy(() => import('AwesomeA'))
```

Problem solved!

#### Code splitting routes.

Code splitting advocates that instead of sending this large chunk of code to the user at once, you may dynamically send chunks to the user when they need it.

We had looked at component based code splitting in the earlier examples, but another common approach is with route based code splitting.

In this method, the code is split into chunks based on the routes in the application.

![Image](https://cdn-media-1.freecodecamp.org/images/AdX6wJOpumuGlg07LGrWXU55cVtu-wcsxGP7)

We could also take our knowledge of lazy loading one step further by code splitting routes.

Consider a typical React app that uses `react-router` for route matching.

```
const App = () => (  <Router>      <Switch>        <Route exact path="/" component={Home}/>        <Route path="/about" component={About}/>      </Switch>  </Router>);
```

We could lazy load the `Home` and `About` components so they are only fetched when the user hits the associated routes.

Here’s how with `React.Lazy` and `Suspense`.

```
// lazy load the route componentsconst Home = React.lazy(() => import('./Home'))const About = React.lazy(() => import('./About'))
```

```
// Provide a fallback with Suspenseconst App = () => (  <Router&gt;    <Suspense fallback={<div>Loading...</div>}>      <Switch>        <Route exact path="/" component={Home}/>        <Route path="/about" component={About}/>      </Switch>    </Suspense>  </Router>);
```

Easy, huh?

We’ve discussed how `React.Lazy` and `Suspense` works, but under the hood, the actual code splitting i.e. generating separate bundles for different modules is done by a bundler, for example [Webpack](https://webpack.js.org).

If you use `create-react-app`, `Gatsby` or `Next.js` then you have this already set up for you.

Setting this up yourself is also easy, you just need to tweak your `Webpack` config a little bit.

The official `Webpack` documentation has an [entire guide](https://webpack.js.org/guides/code-splitting/) on this. The guide may be worth checking if you’re handling the budding configurations in your application yourself.

#### Example: Adding Lazy Loading to the Bank App.

We can add some lazy loading to the bank application we saw from Chapter 2.

Consider the `Root` component of the application:

```
const Root = () => (  <UserProvider>    <UserConsumer>      {({ user, handleLogin }) =>        user ? <App /> : <Login handleLogin={handleLogin} />      }    </UserConsumer>  </UserProvider>)
```

When a user isn’t logged in we display the login page, and the `App` component only when the user is logged in.

We could lazy load the `App` component, right?

This is very easy. You use the dynamic import syntax with `React.lazy` and wrap the `App` component in a `Suspense` component.

Here’s how:

```
...const App = React.lazy(() => import('./containers/App'))const Root = () => (  ...  <Suspense fallback='loading...'>     <App /&gt;  </Suspense>)
```

Now, if you throttle your network connection to simulate Slow 3G, you’ll see the intermediate _“loading…”_ text after logging in.

![Image](https://cdn-media-1.freecodecamp.org/images/IW7iLI-wxcnn9I1L3bHHGzgpipbg6hcsBzPE)

#### Conclusion.

`React.lazy` and `Suspense` are great, and so intuitive to work with, however, they do not support server side rendering yet.

It’s likely this will change in the future, but in the mean time, if you care about SSR, using [react-loadable](https://github.com/jamiebuilds/react-loadable) is your best bet for lazy loading `React` components.

### Chapter 7: Hooks — Building Simpler React Apps.

![Image](https://cdn-media-1.freecodecamp.org/images/nSjeot4viuP2OG3F7I3AwlxLakzO5xCuzGV8)

For the past 3 years John’s been writing React apps, functional components have mostly been dumb.

![Image](https://cdn-media-1.freecodecamp.org/images/60PnHQsIH-SlznuOqQ84T08blhFnXM3ygp7i)

If you wanted local state or some other complex side effects, you had to reach out to class component. You either painfully refactor your functional components to class components or nothing else.

It’s a bright Thursday afternoon, and while having lunch, Mia introduces John to Hooks.

![Image](https://cdn-media-1.freecodecamp.org/images/zG-t1Hr6vonZBF1NbaepxzXMHLemGS1zhR4x)

She speaks so enthusiastically, it piques John’s interest.

Of all the things Mia said, one thing struck John. “_With hooks, functional components become just as powerful (if not more powerful) than your typical class components_”.

![Image](https://cdn-media-1.freecodecamp.org/images/epxPtULUEPakK0-3-EVfdtK5--vLsIHjVtRi)

That’s a bold statement from Mia.

So, let’s consider what hooks are.

#### Introducing Hooks.

Early this year, 2019, the React team released a new addition, hooks, to React in version `16.8.0.`

If React were a big bowl of candies, then hooks are the latest additions, very chewy candies with great taste!

So, what exactly do hooks mean? And why are they worth your time?

One of the main reasons hooks were added to React is to offer a more powerful and expressive way to write (and share) functionality between components.

> In the longer term, we expect Hooks to be the primary way people write React components — [React Team](https://reactjs.org/docs/hooks-faq.html#should-i-use-hooks-classes-or-a-mix-of-both)

If hooks are going to be that important, why not learn about them in a fun way!

#### The Candy Bowl.

Consider React to be a beautiful bowl of candy.

![Image](https://cdn-media-1.freecodecamp.org/images/pjja8sdMgoi2fUu1o2PCBoFmo4ihiNtfE7BD)

The bowl of candy has been incredibly helpful to people around the world.

![Image](https://cdn-media-1.freecodecamp.org/images/1BvN5dNjhTWnvWoQh2jWDyUlyLcSZLT-zlqa)

The people who made this bowl of candy realized that some of the candies in the bowl weren’t doing people much good.

A couple of the candies tasted great, yes! But they brought about some complexity when people ate them — think render props and higher order components?

![Image](https://cdn-media-1.freecodecamp.org/images/ZuxFKQ3ZKRWVVn982t9Ey8MvL8EQGzfwkoqt)

So, what did they do?

![Image](https://cdn-media-1.freecodecamp.org/images/CuOhbGjag0VyZ6Un3XfJgdoC5hiugK9V49b0)

They did the right thing — not throwing away all the previous candies, but making new sets of candies.

These candies were called **Hooks**.

![Image](https://cdn-media-1.freecodecamp.org/images/X1P4ajaVzaSiAfXwewXeXNdI5hzMJFyNBNva)

These candies exist for one purpose: **to make it easier for you to do the things you are already doing**.

![Image](https://cdn-media-1.freecodecamp.org/images/m55098wKgv-QFB3zcmy0vL3smJZ9vRaeLDcc)

These candies aren’t super special. In fact, as you begin to eat them you’ll realize they taste familiar — they are just **Javascript functions**!

![Image](https://cdn-media-1.freecodecamp.org/images/RWmYzL3pHLO8573ms4TNS519-Dy7CGbSfyOb)

As with all good candies, these 10 new candies all have their unique names. Though they are collectively called **hooks**.

Their names always begin with the three letter word, use … e.g. `useState`, `useEffect` etc.

Just like chocolate, these 10 candies all share some of the same ingredients. Knowing how one tastes, helps you relate to the other.

Sounds fun? Now let’s have these candies.

#### The State Hook.

As stated earlier, hooks are functions. Officially, there are 10 of them. 10 new functions that exist to make writing and sharing functionalities in your components a lot more expressive.

The first hook we’ll take a look at is called, `useState`.

For a long time, you couldn’t use the local state in a functional component. Well, not until hooks.

With `useState`, your functional component can have (and update) local state.

How interesting.

Consider the following counter application:

![Image](https://cdn-media-1.freecodecamp.org/images/21F0jCXkYSFWmal4Fa3BxhlwaWre7WiBkrpG)

With the Counter component shown below:

Simple, huh?

Let me ask you one simple question. Why exactly do we have this component as a `Class` component?

Well, the answer is simply because we need to keep track of some local state within the component.

Now, here’s the same component refactored to a functional component with access to state via the `useState` hooks.

What’s different?

I’ll walk you through it step by step.

A functional component doesn’t have all the `Class extend ...` syntax.

```
function CounterHooks() {}
```

It also doesn’t require a render method.

```
function CounterHooks() {    return (      <div>        <h3 className="center">Welcome to the Counter of Life </h3>        <button           className="center-block"           onClick={this.handleClick}> {count} </button>      </div>    ); }
```

There are two concerns with the code above.

* You’re not supposed to use the `this` keyword in function components.
* The `count` state variable hasn’t been defined.

Extract `handleClick` to a separate function within the functional component:

```
function CounterHooks() {  const handleClick = () => {   }  return (      <div>        <h3 className="center">Welcome to the Counter of Life </h3>        <button           className="center-block"           onClick={handleClick}> {count} </button>      </div>    ); }
```

Before the refactor, the count variable came from the class component’s state object.

In functional components, and with hooks, that comes from invoking the `useState` function or hook.

`useState` is called with one argument, the initial state value e.g. `useState(0)` where 0 represents the initial state value to be kept track of.

Invoking this function returns an array with two values.

```
//? returns an array with 2 values. useState(0) 
```

The first value being the current `state` value being tracked, and second, a function to update the `state` value.

Think of this as some `state` and `setState` replica - however, they aren’t quite the same.

With this new knowledge, here’s `useState` in action.

```
function CounterHooks() {  // ?   const [count, setCount] = useState(0);  const handleClick = () => {    setCount(count + 1)  }  return (      <div>        <h3 className="center">Welcome to the Counter of Life </h3>        <button           className="center-block"           onClick={handleClick}> {count} </button>      </div>    ); } 
```

There are a few things to note here, apart from the obvious simplicity of the code!

One, since invoking `useState` returns an array of values, the values could be easily destructed into separate values as shown below:

```
const [count, setCount] = useState(0);
```

Also, note how the `handleClick` function in the refactored code doesn’t need any reference to `prevState` or anything like that.

It just calls `setCount` with the new value, `count + 1`.

Simple as it sounds, you’ve built your very first component using hooks. I know it’s a contrived example, but that’s a good start!

**NB**: it’s also possible to pass a function to the state updater function. This is usually recommended as with `setState` when a state update depends on a previous value of state e.g. `setCount(prevCount => prevCount +` 1)

#### Multiple useState calls.

With class components, we all got used to setting state values in an object whether they contained a single property or more.

```
// single property state = {  count: 0}// multiple properties state = { count: 0, time: '07:00'}
```

With `useState` you may have noticed a subtle difference.

In the example above, we only called `useState` with the actual initial value. Not an object to hold the value.

```
useState(0)
```

So, what if we wanted to keep track of another state value?

Can multiple `useState` calls be used?

Consider the component below. It’s the same counter application with a twist. This time the counter keeps track of the time of click.

![Image](https://cdn-media-1.freecodecamp.org/images/y1ygRHiHbm6haOM0uTRin1vZ9VoYMLvG1hYS)

As you can see, the hooks usage is quite the same, except for having a new `useState` call.

```
const [time, setTime] = useState(new Date())
```

Now, the `time` state variable is used in the rendered markup to display the hour, minute and second of the click.

```
<p>     at: {`${time.getHours()} : ${time.getMinutes()} :${time.getSeconds()}`}  </p>
```

Great!

#### Object as Initial Values

Is it possible to use an object with `useState` as opposed to multiple `useState` calls?

Absolutely!

If you choose to do this, you should note that unlike `setState` calls, the values passed into `useState` replaces the state value.

`setState` merges object properties but `useState` replaces the entire value.

#### The Effect Hook.

With class components you’ve likely performed side effects such as logging, fetching data or managing subscriptions.

These side effects may be called “effects” for short, and the effect hook, `useEffect` was created for this purpose.

How’s it used?

Well, the `useEffect` hook is called by passing it a function within which you can perform your side effects.

Below’s a quick example:

```
useEffect(() => {  // ? you can perform side effects here  console.log("useEffect first timer here.")}) 
```

To `useEffect` I’ve passed an anonymous function with some side effect called within it.

The next logical question is, when is the `useEffect` function invoked?

Well, remember that in class components you had lifecycle methods such as `componentDidMount` and `componentDidUpdate`.

Since functional components don’t have these lifecycle methods, `useEffect` _kinda_ takes their place.

Thus, in the example above, the function within `useEffect` also known as the effect function, will be invoked when the functional component mounts (`componentDidMount`) and when the component updates `componentDidUpdate`).

Here’s that in action.

By adding the `useEffect` call above to the counter app, we indeed get the log from the `useEffect` function.

![Image](https://cdn-media-1.freecodecamp.org/images/T9u1mPVp81HSg4s3MsRRiOYc6KRzB1z5tLLv)

By default, the `useEffect` function will be called after every render.

**NB**: The `useEffect` hook isn’t entirely the same as `componentDidMount` + `componentDidUpdate`. It can be viewed as such, but the implementation differs with some subtle differences.

#### Passing Array Dependencies.

It’s interesting that the effect function is invoked every time there’s an update. That’s great, but it’s not always the desired functionality.

What if you only want to run the effect function only when the component mounts?

That’s a common use case and `useEffect` takes a second parameter, an array of dependencies to handle this.

If you pass in an empty array, the effect function is run only on mount — subsequent re-renders don’t trigger the effect function.

```
useEffect(() => {    console.log("useEffect first timer here.")}, [])
```

![Image](https://cdn-media-1.freecodecamp.org/images/KAv1j3znRKI9nnXTHC-VSLHkqHyb-4Cskas7)

If you pass any values into this array, then the effect function will be run on mount, and anytime the values passed are updated. That is, if any of the values are changed, the effected call will re-run.

```
useEffect(() => {    console.log("useEffect first timer here.")}, [count])
```

The effect function will be run on mount, and whenever the count function changes.

![Image](https://cdn-media-1.freecodecamp.org/images/uDU1DVT8gyC4jce-XQZDT5ftKLMmFMUKCD8T)

What about subscriptions?

It’s common to subscribe and unsubscribe from certain effects in certain apps.

Consider the following:

```
useEffect(() => {  const clicked = () => console.log('window clicked');  window.addEventListener('click', clicked);}, [])
```

In the effect above, upon mounting, a click event listener is attached to the window.

How do we unsubscribe from this listener when the component is unmounted?

Well, `useEffect` allows for this.

If you return a function within your effect function, it will be invoked when the component unmounts. This is the perfect place to cancel subscriptions as shown below:

```
useEffect(() => {    const clicked = () => console.log('window clicked');    window.addEventListener('click', clicked);
```

```
    return () =>; {      window.removeEventListener('click', clicked)    } }, [])
```

There’s a lot more you can do with the useEffect hook such as making API calls.

#### Build Your own Hooks

From the start of the hooks section we’ve taken (and used) candies from the candy box React provides.

However, React also provides a way for you to make your own unique candies — called custom hooks.

So, how does that work?

A custom hook is just a regular function. However, its name must begin with the word, **use** and if needed, it may call any of the React hooks within itself.

Below’s an example:

#### The Rules of Hooks

There are two rules to adhere to while using hooks.

* Only Call Hooks at the [Top Level](https://reactjs.org/docs/hooks-rules.html#only-call-hooks-at-the-top-level) i.e. not within conditionals, loops or nested functions.
* Only Call Hooks from React Functions i.e. Functional Components and Custom Hooks.

This ESLint [plugin](https://www.npmjs.com/package/eslint-plugin-react-hooks) is great to ensure you adhere to these rules within your projects.

### Advanced Hooks

We have only considered two out of 10 of the hooks React provides!

What’s interesting is that the knowledge of how `useState` and `useEffect` works helps you quickly learn the other hooks.

Curious to learn about those, I have created a [hooks cheatsheet](https://github.com/ohansemmanuel/react-hooks-cheatsheet) with live editable examples.

![Image](https://cdn-media-1.freecodecamp.org/images/uocYYVAXRFmr3pkFzJFxggyNp4dUcMlfr7cc)

Why this is important is that you can immediately begin to tinker with real examples that’ll reinforce your knowledge of how hooks work. All of them!

Remember that learning is reinforced when you actual solve problems and build stuff.

What’s more interesting as well is, after you get through the live examples for each of the hooks, there’s an extra section for other generic examples that don’t exactly fit one hook or require a separate case study.

In the example section you’ll find [examples](https://react-hooks-cheatsheet.com/examples/fetching-data) such as fetching data from a remote server using hooks and more.

![Image](https://cdn-media-1.freecodecamp.org/images/GK8XDogOdy6kbKVQ6SI9QfO2qpoNjWWYa3oU)
_Live example from the cheatsheet._

Go, [check it out](https://github.com/ohansemmanuel/react-hooks-cheatsheet).

### Chapter 8: Advanced React Patterns with Hooks

![Image](https://cdn-media-1.freecodecamp.org/images/WXlCQiqH7AWqwhgBWCKZuIQ6UXT-v3h-IjRO)

With the release of hooks, certain React patterns have gone out of favour. They can still used, but for most use cases you’re likely better off using hooks. For example, choose hooks over render props or higher order components.

There may be specific use cases where these could still be used, but most of the times, choose hooks.

That being said, we will now consider some more advanced React patterns implemented with hooks.

Ready?

#### Introduction

This chapter may be the longest in the book, and for good reason. Hooks are likely the way we’ll be writing React components in the next couple of years, and so they are quite important.

In this chapter, we’ll consider the following advanced React patterns:

* Compound Components
* Props Collection
* Prop Getters
* State Initializers
* State Reducer
* Control Props

If you’re completely new to these advanced patterns, don’t worry, I’ll explain them in detail. If you’re familiar with how these patterns work from previous experiences with class components, I’ll show you how to use these patterns with hooks.

Now, let’s get started.

#### Why Advanced Patterns?

John’s had a fairly good career. Today, he’s a senior frontend engineer at _ReactCorp_. A great startup changing the world for good.

_ReactCorp_ is beginning to scale their workforce. A lot of engineers are being hired and John’s beginning to work on building reusable components for the entire team of engineers.

![Image](https://cdn-media-1.freecodecamp.org/images/UndCKKEAhJKf7KUa3Ulf9CmeY7szLAiejuzX)

Yes, John can build components with his current React skills, however, with building highly reusable components comes specific problems.

There’s a million different ways the components can be consumed, and you want to give consumers of the component as much flexibility as possible.

They must be able to extend the functionality and styles of the component as they deem fit.

The advanced patterns we’ll consider here are tested and tried methods for building very reusable components that don’t cripple flexibility.

I didn’t create these advanced patterns. Truth be told, most of the advanced React patterns were made popular by one guy, [Kent Dodds](https://kentcdodds.com) — an amazing Javascript engineer.

The community has received these patterns extremely well, and I’m here to help you understand how they work!

#### Compound Components Pattern

The first pattern we will consider is called the Compound Components pattern. I know it sounds fancy, so I’ll explain what it really means.

The keyword in the pattern name is the word _Compound_.

Literarily, the word _compound_ refers to something that is composed of two or more separate elements.

With respect to React components, this could mean a component that is composed of two or more separate components.

It doesn’t end there.

Any React component can be composed of 2 or more separate components. So, that’s really not a brilliant way to describe compound components.

With compound components, there’s more. The separate components within which the main component is composed cannot really be used without the parent.

![Image](https://cdn-media-1.freecodecamp.org/images/oZ7CY7vfHkIbqMLOGtI5DpdPBRWgnP7tGy3J)
_compound components_

The main component is usually called the parent, and the separate composed components, children.

The classic example is to consider the `html` select element.

```
<select>  <option value="value0">key0</option>  <option value="value1">key1</option>  <option value="value2">key2</option></select>
```

With `select` being the parent, and the many `option` elements, children.

This works like a compound component. For one, it really makes no sense to use the `<option>key0<`;/option> elemen`t with`out a select parent tag. The overall beh`aviour` of a select element also relies on having the`se com`posed option elements as well.

They are so connected to one another.

Also, the state of the entire component is managed by `select` with all child elements dependent on that state.

Do you get a sense for what compound components are now?

It is also worth mentioning that compound components are just one of many ways to express the API for your components.

For example, while it doesn’t look as good, the `select` element could have been designed to work like this:

```
<select options="key:value;anotherKey:anotherValue"><;/select>
```

This is definitely not the best way to express this API. It make passing attributes to the child components almost impossible.

With that in mind, let’s take a look at an example that’ll help you understand and build your own compound components.

#### Example: Building an Expandable Component.

![Image](https://cdn-media-1.freecodecamp.org/images/LSHe4laueTj0qrz7WZcIkNqQfI1txaaszPxo)
_The final component being used_

We’ll be building an `Expandable` component. Did you ask what that means?

Well, consider an `Expandable` component to be a miniature accordion element. It has a clickable header, which toggles the display of an associated body of content.

In the unexpanded state the component would look like this:

![Image](https://cdn-media-1.freecodecamp.org/images/xkCEtYIIkTQO0s-imNADZ8tX5ceLMV-zKpdq)

And this, when expanded:

![Image](https://cdn-media-1.freecodecamp.org/images/NdybUeg-Rye1gyZ7yuDYcmREl2hPDflkQxi7)

You get the idea, right?

#### Designing the API

It’s usually a good idea to write out what the exposed API of your component would look like before building it out.

In this case, here’s what we’re going for:

```
<Expandable>	<Expandable.Header> Header </Expandable.Header> 	<Expandable.Icon/>    <Expandable.Body> This is the content &lt;/Expandable.Body></Expandable>
```

![Image](https://cdn-media-1.freecodecamp.org/images/gsi8CWO9uvmAh4m33n-MsQTeHS5owZfFezsM)

![Image](https://cdn-media-1.freecodecamp.org/images/EbOV-Qb3ZrK2t87zC9sLtAvq5oWQCLkycWDX)
_A break down of the child components_

In the code block above you’d have noticed I have expressions like this: `Expandable.Header`

You could as well do this:

```
<Expandable>	<Header> Header </Expandable.Header> 	<Icon/>    <Body> This is the content </Body></Expandable>
```

It doesn’t matter. I have chosen `Expandable.Header` over `Header` as a matter of personal preference. I find that it communicates dependency on the parent component well, but that’s just my preference. A lot of people don’t share the same preference and that’s perfectly fine.

It’s your component, use whatever API looks good to you :)

#### Building the Expandable Component

The `Expandable` component being the parent component will keep track of state, and It will do this via a boolean variable called `expanded`.

```
// state {  expanded: true || false}
```

The `Expandable` component needs to communicate the state to every child component regardless of their position in the nested component tree.

Remember that the children are dependent on the parent compound component for state.

How best may we go about this?

If you said `context`, you’re correct!

We need to create a `context` object to hold the component state, and expose the `expanded` property via the `Provider` component. Alongside the `expanded` property, we will also expose a function callback to toggle the value of this `expanded` state property.

![Image](https://cdn-media-1.freecodecamp.org/images/Ga1KnN7jSDEPUsyceXFVi4mqGwYjr4fOG1Yz)
_the state relationship for the expandable component_

If that sounds alright to you, here’s the starting point for the `Expandable` component.

```
// Expandable.js import React, { createContext } from 'react'
```

```
const ExpandableContext = createContext()const { Provider } = ExpandableContext
```

```
const Expandable = ({children}) => {  return <Provider>{children}</Provider>}export default Expandable
```

There’s nothing spectacular going on in the code block above.

A context object is created and the `Provider` component deconstructed. Then we go on to create the `Expandable` component which renders the `Provider` and any `children`.

Got that?

With the basic setup out of the way, let’s do a little more.

The context object was created with no initial value. However, we need the `Provider` to expose the state value `expanded` and a toggle function to update the state.

Let’s create the `expanded` state value using `useState`.

```
// Expandable.js 
```

```
import React, { createContext, useState } from 'react'...const Expandable = ({children}) => {  // look here ?  const [expanded, setExpanded] = useState(false) 
```

```
  return <Provider>{children}</Provider>}
```

With the `expanded` state variable created, let’s create the `toggle` updater function to toggle the value of `expanded` — whether `true` or `false`.

```
// Expandable.js ...const Expandable = ({children}) => {  const [expanded, setExpanded] = useState(false)  // look here ?  const toggle = setExpanded(prevExpanded => !prevExpanded) 
```

```
  return <Provider>{children}</Provider>}
```

The `toggle` function invokes `setExpanded`, the actual updater function returned from the `useState` call.

Every updater function from the `useState` call can receive a function argument. This is similar to how you pass a function to `setState` e.g. `setState(prevState => !prevState.val`ue).

This is the same thing I’ve done above. The function passed to `setExpanded` receives the previous value of `expanded` and returns the opposite of that, `!expanded`

`toggle` acts as a callback function and It’ll eventually be invoked by `Expandable.Header`. Let’s prevent any future performance issue by memoizing the callback.

```
... import { useCallback } from 'react';
```

```
const Expandable = ({children}) => {  const [expanded, setExpanded] = useState(false)  // look here ?  const toggle = useCallback(    () => setExpanded(prevExpanded => !prevExpanded),    []  ))return <Provider>{children}</Provider> 
```

Not sure how `useCallback` works? You probably skipped the previous advanced hooks section that pointed to the cheatsheet. [Have a look](https://react-hooks-cheatsheet.com/usecallback).

Once we have both `expanded` and `toggle` created, we can expose these via the `Provider`’s value prop.

```
...const Expandable = ({children}) => {  const [expanded, setExpanded] = useState(false)  const toggle = useCallback(    () => setExpanded(prevExpanded => !prevExpanded),    []  )   // look here ?  const value = { expanded, toggle }   // and here ?  return <;Provider value={value}>{children}</Provider>}  
```

This works, but the `value` reference will be different on every re-render causing the `Provider` to re-render its children.

Let’s memoize the `value`.

```
...const Expandable = ({children}) => {  ... // look here ?  const value = useMemo(	() => ({ expanded, toggle }), 	[expanded, toggle]  )  return <Provider value={value}>{children}&lt;/Provider>} 
```

`useMemo` takes a callback that returns the object value `{ expanded, toggle }` and we pass an array dependency `[expanded, toggle]` so that the memoized value remains the same unless those change.

We’ve done a great job so far!

Now, there’s just one other thing to do on the `Expandable` parent component.

If you remember from a previous experience with class components, it’s possible to do this:

```
this.setState({  name: "value"}, () => {  this.props.onStateChange(this.state.name)})
```

This is how you trigger a callback after a state change in class components.

Usually, the callback e.g. `this.props.onStateChange` is always invoked with the current value of the updated state as shown below:

```
this.props.onStateChange(this.state.name)
```

Why is this important?

This is good practice when creating reusable components, because this way the consumer of your component can attach any custom logic to be run after a state update.

For example:

```
const doSomethingPersonal = ({expanded}) => {  // do something really important after being expanded}
```

```
<Expandable onExpanded={doSomethingPersonal}> ... </Expandable>
```

We will add this functionality to the `Expanded` component.

With class components this is pretty much straightforward. With functional components, we need to do a little more work — not so much :)

Whenever you want to perform a side effect within a functional component, for most cases, always reach out for `useEffect`.

So, the easiest solution might look like this:

```
useEffect(() => {  props.onExpanded(expanded)}, [expanded])
```

The problem however with this is that the `useEffect` effect function is called at least once — when the component is initially mounted.

So, even though there’s a dependency array, `[expanded]`, the callback will also be invoked when the component mounts!

```
useEffect(() => {  // this function will always be invoked on mount})
```

The functionality we seek requires that the callback to be passed by the user isn’t invoked on mount.

How can we enforce this?

First, consider the naive solution below:

```
//faulty solution... let componentJustMounted = trueuseEffect(    () => {        if(!componentJustMounted) {        props.onExpand(expanded)        componentJustMounted = false      }    },    [expanded]  )...
```

What’s wrong with the code above?

Loosely speaking, the thinking behind the code is correct. You keep track of a certain variable `componentJustMounted` and set it to `true`, and only call the user callback `onExpand` when `componentJustMounted` is false.

The `componentJustMounted` value is only set to `false` after the user callback has been invoked at least once.

Looks good.

However, the problem with this is that whenever the function component re-renders owing to a state or prop change, the `componentJustMounted` value will always be reset to `true`. Thus, the user callback `onExpand` will never be invoked as it is only invoked when `componentJustMounted` is falsey.

```
...if (!componentJustMounted) {    	onExpand(expanded)}...
```

Well, the solution to this is simple. We can use the `useRef` hook to ensure that a value stays the same all through lifetime of the component.

Here’s how it works:

```
//correct implementation  const componentJustMounted = useRef(true)  useEffect(    () => {      if (!componentJustMounted.current) {        onExpand(expanded)      }      componentJustMounted.current = false    },    [expanded]  )
```

`useRef` returns a `ref` object and the value stored in the object may be retrieved from `ref.current`

The signature for `useRef` looks like this: `useRef(initialValue)`.

Hence, stored initially in `componentJustMounted.current` is a ref object with the `current` property set to `true`.

```
const componentJustMounted = useRef(true)
```

After invoking the user callback, we then update this value to `false`.

```
componentJustMounted.current = false
```

Now, whenever there’s a state or prop change the value in the ref object isn’t tampered with. It remains the same.

With the current implementation, whenever the `expanded` state value is toggled, the user callback function `onExpanded` will be invoked with the current value of `expanded`.

Here’s what the final implementation of the `Expandable` component now looks like:

```
// Expandable.js const Expandable = ({ children, onExpand }) => {  const [expanded, setExpanded] = useState(false)  const toggle = useCallback(    () => setExpanded(prevExpanded => !prevExpanded),    []  )  const componentJustMounted = useRef(true)  useEffect(    () => {      if (!componentJustMounted) {        onExpand(expanded)      }       componentJustMounted.current = false    },    [expanded]  )  const value = useMemo(   () => ({ expanded, toggle }),    [expanded, toggle]  )  return (    <Provider value={value}>        {children}    </Provider>  )}
```

If you’ve followed along, that’s great. We’ve sorted out the most complex component in the bunch. Now, let’s build the child components.

#### Building the Compound Child Components

There are three child components for the `Expandable` component.

![Image](https://cdn-media-1.freecodecamp.org/images/qCrrUqNmXLJI53uFn41uZ9VtAWvsU9Xfi14a)

These child components need to consume values from the context object created in `Expandable.js`.

To make this possible, we’ll do a little refactoring as shown below:

```
export const ExpandableContext = createContext()
```

We export the context object, `ExpandableContext` from `Expandable.js`.

Now, we may use the `useContext` hook to consume the values from the `Provider`.

Below’s the `Header` child component fully implemented.

```
//Header.jsimport React, { useContext } from 'react'import { ExpandableContext } from './Expandable'
```

```
const Header = ({children}) => {  const { toggle } = useContext(ExpandableContext)  return <div onClick={toggle}>{children}</div>}export default Header
```

Simple, huh?

It renders a `div` whose `onClick` callback is the `toggle` function for toggling the `expanded` state within the `Expandable` parent component.

Here’s the implementation for the `Body` child component:

```
// Body.jsimport { useContext } from 'react'import { ExpandableContext } from './Expandable'
```

```
const Body = ({ children }) => {  const { expanded } = useContext(ExpandableContext)  return expanded ? children : null}export default Body
```

Pretty simple as well.

The `expanded` value is retrieved from the context object and used within the rendered markup. It reads like this: If expanded, render `children` else render nothing.

The `Icon` component is just as simple.

```
// Icon.jsimport { useContext } from 'react'import { ExpandableContext } from './Expandable'
```

```
const Icon = () => {  const { expanded } = useContext(ExpandableContext)  return expanded ? '-' : '+'}export default Icon
```

It renders either `+` or `-` depending on the value of `expanded` retrieved from the context object.

With all child components built, we can set the child components as `Expandable` properties. See below:

```
import Header from './Header'import Icon from './Icon'import Body from './Body'
```

```
const Expandable = ({ children, onExpand }) => {	...}
```

```
// Remember this is just a personal reference. It's not mandatoryExpandable.Header = HeaderExpandable.Body = BodyExpandable.Icon = Icon
```

Now we can go ahead to use the `Expandable` component as designed:

```
<Expandable>    <Expandable.Header>React hooks</Expandable.Header>           <Expandable.Icon />    <Expandable.Body>Hooks are awesome&lt;/Expandable.Body></Expandable>
```

Does it work?

You bet!

Here’s what’s rendered when not expanded:

![Image](https://cdn-media-1.freecodecamp.org/images/D3EYhc5vHz6LzpqQkb38aAfzEF8NICFyX0J8)

And when expanded:

![Image](https://cdn-media-1.freecodecamp.org/images/T8DJ2hZnTVMSyKFRN0t8-br-GCE5H9c-3cap)

This works but it has to be the ugliest component I’ve ever seen. We can do better.

#### Manageable Styling for Reusable Components

Hate it or not, styling (or CSS) is integral to how the web works.

While there’s a number of ways to style a `React` component, and I’m sure you have a favourite, when you build reusable components it’s always a good idea to expose a frictionless API for overriding default styles.

Usually, I recommend letting it possible to have your components styleable via both `style` and `className` props.

For example:

```
// this should work.<MyComponent style={{name: "value"}} />// and this.<MyComponent className="my-class-name-with-dope-styles" />
```

Now, our goal isn’t just styling the component, but to make it as reusable as possible. This means letting whoever consumes the component style the component whichever they want i.e inline style via the `style` prop, or by passing some `className` prop.

Let’s begin with the `Header` child component:

```
// before const Header = ({children}) => {  const { toggle } = useContext(ExpandableContext)  return <div onClick={toggle}>{children}</div>}
```

First, let’s change the rendered markup to a `button`. It’s a more accessible and semantic alternative to the `div` used earlier.

```
const Header = ({children}) => {  const { toggle } = useContext(ExpandableContext)  // look here ?  return <button onClick={toggle}>{children}<;/button>} 
```

We will now write some default styles for the `Header` component in a `Header.css` file.

```
// Header.css.Expandable-trigger {    background: none;    color: hsl(0, 0%, 13%);    display: block;    font-size: 1rem;    font-weight: normal;    margin: 0;    padding: 1em 1.5em;    position: relative;    text-align: left;    width: 100%;    outline: none;    text-align: center;  }    .Expandable-trigger:focus,  .Expandable-trigger:hover {    background: hsl(216, 94%, 94%);  }
```

I’m sure you can figure out the simple CSS above. If not, don’t stress it. What’s important is to note the default `className` used here, `.Expandable-trigger`

To apply these styles, we need to import the `CSS` file and apply the appropriate `className` prop to the rendered `button`.

```
... import './Header.css'const Header = () => {  const { toggle } = useContext(ExpandableContext)  return <button onClick={toggle} 	 className="Expandable-trigger">	{children}&lt;/button>}
```

This works great, however the `className` is set to the default string `Expandable-trigger`.

This will apply the styling we’ve written in the `CSS` file, but it doesn’t take into the account any `className` prop passed in by the user.

It’s important to accommodate passing this `className` prop as a user might like to change the default style you’ve set in your `CSS`.

Here’s one way to do this:

```
// Header.jsimport './Header.css'const Header = ({ children, className}) => {  // look here ?  const combinedClassName = `Expandable-trigger ${className}`  return (    <button onClick={toggle} className={combinedClassName}>      {children}    </button>  )} 
```

Now, whatever `className` is passed to the `Header` component will be combined with the `default` `Expandable-trigger` before been passed on to the rendered `button` element.

Let’s consider how good the current solution is.

First, if the `className` prop is `null` or `undefined`, the `combinedClassName` variable will hold the value `"Expandable-trigger null"` or `"Expandable-trigger undefined".`

To prevent this, be sure to pass a `className` by using the ES6 default parameters syntax as shown below:

```
// note how className defaults to an empty stringconst Header = ({ children, className = '' }) => {  ...}
```

Having provided a default value, if the user still doesn’t enter a `className`, the `combinedClassName` value will be equal to `"Expandable-trigger "`.

Note the empty string appended to the `Expandable-trigger`. This is owing to how template literals work.

My preferred solution is to do this:

```
const combinedClassName = ['Expandable-trigger', className].join('')
```

This solution handles the previously discussed edge cases. If you also want to explicit about removing `null`, `undefined` or any other falsey values, you can do the following:

```
const combinedClassName = ['Expandable-trigger', className].filter(Boolean).join('')
```

I’ll stick with the simpler alternative, and providing a default for `className` via default parameters.

With that being said, here’s the final implementation for `Header`:

```
// after ...import './Header.css'const Header = ({ children, className = ''}) => {  const { toggle } = useContext(ExpandableContext)  const combinedClassName = ['Expandable-trigger', className].join('')
```

```
return (    <button onClick={toggle} className={combinedClassName}>      {children}    </button>  )}
```

So far, so good.

Incase you were wondering, `combinedClassName` returns a string. Since strings are compared by value, there’s no need to memoize this value with `useMemo`.

So far, we’ve graciously handled the `className` prop. How about the option to override default styles by passing a `style` prop?

Well, let’s fix that.

Instead of explicitly destructuring the `style` prop, we can pass on any other prop passed by the user to the `button` component.

```
// rest paramter ...otherProps ?const Header = ({ children, className = '', ...otherProps }) => {	return (    // spread syntax {...otherProps} ?    <button {...otherProps}>      {children}    </button>  )}  
```

Note the use of the [rest parameter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters) and [spread syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax).

With this done, the `Header` component receives our default styles, yet allows for change via the `className` or `style` props.

```
// override style via className<Expandable.Header className="my-class">	React hooks</Expandable.Header>
```

```
// override style via style prop<Expandable.Header style={{color: "red"}}>	React hooks</Expandable.Header>
```

Now, I’ll go ahead and do the same for the other child components, `Body` and `Icon`.

```
// before const Body = ({ children }) => {  const { expanded } = useContext(ExpandableContext)  return expanded ? children : null}
```

```
// after import './Body.css'const Body = ({ children, className = '', ...otherProps }) => {  const { expanded } = useContext(ExpandableContext)  const combinedClassNames = ['Expandable-panel', className].join('')
```

```
  return expanded ? (    <div className={combinedClassNames} {...otherProps}>      {children}    </div>  ) : null}
```

```
// Body.css.Expandable-panel {    margin: 0;    padding: 1em 1.5em;    border: 1px solid hsl(216, 94%, 94%);;    min-height: 150px;  }
```

Do the same for `Icon` component:

```
// before const Icon = () => {  const { expanded } = useContext(ExpandableContext)  return expanded ? '-' : '+'}
```

```
// after ...import './Icon.css'const Icon = ({ className = '', ...otherProps }) => {  ...  const combinedClassNames = ['Expandable-icon', className].join('')
```

```
  return (    <span className={combinedClassNames} {...otherProps}>      {expanded ? '-' : '+'}    </span>  )}
```

```
// Icon.css.Expandable-icon {    position: absolute;    top: 16px;    right: 10px;}
```

And finally, some styles for the parent component, `Expandable`.

```
import './Expandable.css'const Expandable = ({ children, onExpand, className = '', ...otherProps }) => {   ...   const combinedClassNames = ['Expandable', className].join('')  return (    <Provider value={value}>      <div className={combinedClassNames} {...otherProps}>        {children}      </div>    </Provider>  )}
```

```
// Expandable.css.Expandable {     position: relative;     width: 350px;}
```

Now we’ve got a beautiful reusable component!

![Image](https://cdn-media-1.freecodecamp.org/images/hrQd5NnJyljpaXrRKyja27D9zUWhMmNjD2j4)

![Image](https://cdn-media-1.freecodecamp.org/images/rKVwrothDrwalJqh04muFzOpFIzL98Yqjvk2)

We’ve not just made it beautiful, but it’s customisable as well.

How customisable is the component we’ve built?

See what I’ve done below with the same component!

![Image](https://cdn-media-1.freecodecamp.org/images/vrUIQnYihcnlrQftUj6lXhen7LBVO3HJijr1)

![Image](https://cdn-media-1.freecodecamp.org/images/n04wsdnMMD-qykRyopr-JcQq1stOiNUhqdQj)

And this didn’t take a lot of code.

```
<Expandable>    <Expandable.Header>Reintroducing React</Expandable.Header>    <Expandable.Icon />    <Expandable.Body>     	<img            src='https://i.imgur.com/qpj4Y7N.png'            style={{ width: '250px' }}            alt='reintroducing react book cover'        />        <p style={{ opacity: 0.7 }}>          This book is so f*cking amazing! <br />        <a          href='https://leanpub.com/reintroducing-react'          target='_blank'          rel='noopener noreferrer'          >            Go get it now.        </a>       </p>     </Expandable.Body></Expandable>
```

You can go one step further to test if overriding styles via the `style` prop works as well.

```
<Expandable>   <Expandable.Header       // look here ?	  style={{ color: 'red', border: '1px solid teal' }}>        Reintroducing React    </Expandable.Header>        ...</Expandable> 
```

And below’s the result of that:

![Image](https://cdn-media-1.freecodecamp.org/images/dg50ZCANWn3YXiFdxq1kX0-KFwYDLuyhEgF-)
_Default Header styles override with the style prop._

Yay! it works as expected.

**Note**: I have covered 5 other advanced component patterns with Hooks [in the ebook](https://leanpub.com/reintroducing-react) (PDF, Epub and Mobi). **You can get it completely free** (or pay whatever you want if you like my work).

![Image](https://cdn-media-1.freecodecamp.org/images/P8npt6FWcQTqVRfBE4oJ0mseFztCZ-Fod0lt)
_[https://leanpub.com/reintroducing-react](https://leanpub.com/reintroducing-react" rel="noopener" target="_blank" title=")_

### Conclusion

This has been a lengthy discourse on the modern changes in React. If you don’t get all of it yet, spend a little more time practising the examples in your day to day work, and I’m pretty sure you’ll get a hang of it real quick.

When you do, go be the React engineer with a decent understanding of Modern React and go build highly reusable components with advanced hook patterns.

Thank you for following me on this journey. Got questions? Use the comment section!

