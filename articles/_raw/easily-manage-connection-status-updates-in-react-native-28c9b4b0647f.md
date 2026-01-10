---
title: How to easily manage connection status updates in React Native
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-12T20:28:52.000Z'
originalURL: https://freecodecamp.org/news/easily-manage-connection-status-updates-in-react-native-28c9b4b0647f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Sp2YoeR7ngda2gFD5MkBKw.jpeg
tags:
- name: internet
  slug: internet
- name: iOS
  slug: ios
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Jordy van den Aardweg

  Every now and then I like to create and explore technologies I do not have the time
  for in my daily life as a Freelance Frontend Developer. Lately, I’m exploring React
  Native and taking a dive in some new tools and APIs.

  But ...'
---

By Jordy van den Aardweg

Every now and then I like to create and explore technologies I do not have the time for in my daily life as a Freelance Frontend Developer. Lately, I’m exploring React Native and taking a dive in some new tools and APIs.

But building a native app is a little bit different than building a web app. I recently got into a scenario where the user has no active internet connection.

How are we going to inform the user our app has limited capabilities then?

![Image](https://cdn-media-1.freecodecamp.org/images/1*Sp2YoeR7ngda2gFD5MkBKw.jpeg)
_Photo by [Unsplash](https://unsplash.com/photos/ZYecenZy7o4?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Galen Crout</a> on <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

When you are building an app requiring network connectivity, then you need proper handling of failing requests. For example, when the user’s internet connection decides to play hide and seek. So our App can inform the user why a request fails or even prevent the request from firing. And even better: show a usable message to our user explaining what is going on, so they can act on that.

In other words, we can give some _context_ to our users on why the App can’t do a certain request.

#### Redux vs. Context API

The React Native community provides a [NetInfo](https://github.com/react-native-community/react-native-netinfo) module to expose information about the user’s network connection, like if it’s online or offline. We need this data to be globally available in our App.

A general thought would be to use Redux for this. My App already uses Redux, so why not use Redux for it?

Well, of course, we could. But that requires every component to be hooked into the Redux store if we want to use this connectivity information. Hooking into Redux creates overhead, more lines of code and could make our App more complicated than needed.

Let’s explore other possibilities…

React’s Context API provides a **simpler**, **cleaner** way to share state-like data through our components:

> Context is designed to share data that can be considered “global” for a tree of React components, such as the current authenticated user, theme, or preferred language. — [Source](https://reactjs.org/docs/context.html#when-to-use-context)

Seems like we have a perfect use case to use React’s new Context API!

### Let’s dive in

First, we have to install the required packages, since in React Native 0.59 the `NetInfo` module is in a separate package. React 16.6 or later is also required because it allows the context to be available outside render methods. Pretty useful, as this gives us greater flexibility where we use this context.

I won’t bother you with setting up a React Native app and just assume you already have one.

Let’s install the `NetInfo` package:

```
npm install @react-native-community/netinfo --save
```

Once installed, we can create our components.

**Creating the Context Provider**  
Let’s set up the `<NetworkProvide`r> component. This component passes our connectivity status down all our child components:

As shown above, we just listen for the `connectionChange` event. That event returns `true` when there’s an active internet connection or `false` when the user has no active internet connection. We update the state when the connectivity status changes.

As soon as we update the state, the context in our component tree changes. So every component has access to the updated `isConnected` value. Similar to Redux, but with way less boilerplate code.

**Wrapping the Context Provider**  
For React’s Context API to work, we need to wrap this `<NetworkProvide`r> component we just created around our other components, like so:

By doing this we make the `context` available in every component inside the `<NetworkProvid`er>.

The last step is to use the context in a component. We use a `<ExampleCompone`nt> for now:

Now our component uses the Context API and `this.context.isConnected` is available for us to use.

We can now show a message to our users in the `<ExampleCompone`nt> when the user’s internet connection is online or offline.

In previous versions of React, the `context` was not available outside your render method. [Since React 16.6.0](https://reactjs.org/blog/2018/10/23/react-v-16-6.html#static-contexttype) it is available using `static contextType` as shown in the example above. Using it like this gives us greater flexibility in where we want to use that context inside our components.

#### A final note

So, we have shown that the Context API is perfect for setting and using these global values in this use case. The connectivity status is important to have available throughout our whole app, so we can inform our users when an action that requires an active internet connection is going to fail.

We could do the same with Redux, but that requires way more code. Let’s use native React API’s where possible, as it limits dependencies!

The complete Gist can be found on [my GitHub](https://gist.github.com/jvandenaardweg/58ed91e3c33de0b75a15d38853b23d7d).

### Thanks for reading!

I’ve been using Medium for quite some years now, but generally was just reading and learning from other people’s content. Tutorials like this helped me a lot during the years. So, writing my own is my way of giving back to this awesome developer community!

**Did this tutorial help you? Let me know in the comments ?**

**Got feedback for me to improve my articles? I’m eager to improve and share more of my knowledge.**

