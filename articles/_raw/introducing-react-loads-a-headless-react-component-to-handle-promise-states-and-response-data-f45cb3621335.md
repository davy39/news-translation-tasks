---
title: Introducing React Loads — A headless React component to handle promise states
  and response data
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-18T19:24:10.000Z'
originalURL: https://freecodecamp.org/news/introducing-react-loads-a-headless-react-component-to-handle-promise-states-and-response-data-f45cb3621335
coverImage: https://cdn-media-1.freecodecamp.org/images/1*xIBRkg59IQ0ZKkPugO3U6g.gif
tags:
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Jake Moxey

  Simple, declarative, and lightweight


  Background

  There are so many methods to handle state in React right now. From local state to
  Redux, the new React Context API and new libraries such as Unstated and Copy Write.
  All these methods hav...'
---

By Jake Moxey

#### Simple, declarative, and lightweight

![Image](https://cdn-media-1.freecodecamp.org/images/XuV9yuD-347LsZM-q9Ws71xI4vuLQR0Bp-E7)

### Background

There are so many methods to handle state in React right now. From **local state** to **Redux**, the new [**React Context API**](https://reactjs.org/docs/context.html) and new libraries such as [**Unstated**](https://github.com/jamiebuilds/unstated) and [Copy Write](https://github.com/aweary/react-copy-write). All these methods have great use cases, and there are no absolutes in which I’d drop one entirely in favour of another. Each of them have their situational benefits.

But I don’t want to get into the nitty gritty of React state management. Check out Kent C. Dodd’s excellent article about [Application State Management](https://blog.kentcdodds.com/application-state-management-66de608ccb24) for that.

Though I do want to touch on the case of handling loading and response state from a **promise**, for example HTTP requests and resource fetchers. A promise has three explicit states: **pending**, **resolved,** and **rejected.** It has the additional implicit state of **idle,** when the promise has not yet been triggered.

#### How is promise state managed in React?

It can be managed in local state through something as simple as an `isLoading` variable to reflect the “pending” state. `response` and `error` variables are then used to reflect the “resolved” and “rejected” states, respectively.

It can be managed in a Redux store through actions such as `GET_DOG_REQUEST` , `GET_DOG_SUCCESS` and `GET_DOG_ERROR` . These then could map to respective `isLoading` , `response` , and `error` variables in the store.

#### Managing promise state can be dangerous, hard to read, and have problematic UX!

1. Nested ternaries in your `render` function can get difficult to interpret and messy, and can therefore be prone to errors. Here is an example of such a problem:

From this example, it is not clear that `!error && !response` implies the “idle” state. It is also unclear that the `else` section of the `isLoading` ternary implies that the section has been loaded or errored. And just imagine managing more than one promise and their respective states! Urgh.

2. Seeing flashes of “loading” state in your UI is annoying. When a promise goes from an “idle” state to a “pending” state, this state change should be reflected in the UI with a loading indicator. However, it’s possible that your promise will resolve in a minuscule amount of time causing your user to see a “flash” of loading state. This is something many developers are not aware of when they handle promise states.

![Image](https://cdn-media-1.freecodecamp.org/images/yLxb1A-wlpYUtP4kb6DiES2VeVqepaYVwBrV)
_You can see a brief ‘flash’ of content placeholder when this Facebook post is loading._

3. Solely managing promise states in Redux is unnecessary. When Redux was first released, it was common for developers to transfer the majority of their state into a Redux store. However, creating three actions for a promise state, then creating three reducer cases for those actions, causes unnecessary bloat in your application. I’m guilty of this too — but no longer! Actions to handle response/error data are sufficient in my opinion.

**Avoid handling promise state in Redux.**

### Introducing [React Loads](https://github.com/jxom/react-loads)

[React Loads](https://github.com/jxom/react-loads) aims to solve the above issues in a minimalistic fashion. The user provides the `<Loa`ds> component with a function that returns a promise. It will retur`n its` stat`e and re`sponse da`ta as` render props.

[**jxom/react-loads**](https://github.com/jxom/react-loads)  
[_react-loads — A simple React component to handle loading state_github.com](https://github.com/jxom/react-loads)

#### Declaratively handle promise state and response data

React Loads provides you with `render` props to load the promise. This also handles its state and response data. You can get it to load the promise when the component mounts by passing the `loadOnMount` prop to `<Loa`ds>.

#### Predictable outcomes

Using state variables such as `isIdle` , `isLoading` , `isTimeout` , `isSuccess` , and `isError` from `render` props will make your `render` function predictable and easy to read.

#### Removes the “flash” of the loading state

React Loads doesn’t transition to the “loading” state until 300 ms after the promise is triggered. It will wait 300 ms for the promise to **hopefully** resolve before it goes into a pending state. This time can be modified using the `delay` prop for `<Loa`ds> .

#### Ability to cache response data

React Loads has the ability to cache the response data on an application context level. Once the data loads from an invocation of `fn` , it will use the response returned from the promise for the next subsequent invocation’s `response` . The newest data will then load in the background, skipping the `isLoading` state, and update `response` accordingly. You can enable caching by adding a `cacheKey` prop to `<Loa`ds> . Read more about ca[chin](https://github.com/jxom/react-loads#caching-response-data)g here.

### Final remarks

We’ve been using React Loads in production at [Medipass](https://medipass.com.au) on our patient and practitioner facing web app for the past couple of months. It has made our developing experience really easy. We’ve been able to remove a heap of code that handled promise state and response data, and just let React Loads do all the dirty work.

Consider using it in one of your projects and let me know how it goes! If you have any suggestions or spot a bug, feel free to raise a PR (or an issue) [on the repository](https://github.com/jxom/react-loads)!

Thanks for reading!

**Follow me on [Twitter](https://twitter.com/jxom_) and [GitHub](https://github.com/jxom) (I’ll follow you back I promise).**

