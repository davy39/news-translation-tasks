---
title: 'How to Understand Reducers: You Can Use Them Without Redux'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-22T18:29:52.000Z'
originalURL: https://freecodecamp.org/news/how-to-understand-reducers-you-can-use-them-without-redux-2935208bdb12
coverImage: https://cdn-media-1.freecodecamp.org/images/0*oxnWcgexaoRegwaf
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Ryan Yurkanin

  TLDR: You can handle state with a reducer in your Class Components by having one
  function that translates actions into state changes. It centralizes all your setStates.

  ? What is a Reducer?

  Reducers are functions that take input and ...'
---

By Ryan Yurkanin

**TLDR:** You can handle state with a reducer in your Class Components by having one function that translates actions into state changes. It centralizes all your setStates.

#### ? What is a Reducer?

Reducers are functions that take input and decide what to do it with it in one central spot. **That’s it. ?**

If you have a function that determines the view to show based on a URL, it’s a reducer.

Redux Reducers™️ are a specific usage of reducers that interpret events in your application, and how that changes application state.

![Image](https://cdn-media-1.freecodecamp.org/images/1*cK_UHSjJl7rfNUIwb8VZww.png)
_this.dispatch(“RESET_COUNT_CLICKED”)_

If you aren’t familiar with Redux, the above example is usually kickstarted by calling a `dispatch` function with an `action` (object describing an event). ?

We can use reducers right now in a class component by creating a function that handles setting the state by an action type like so:

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ze_yLCczSHAZudU7PKkkMQ.png)

Using a reducer in this simple example is overkill in my opinion. I’m glad React is going to be providing both a `useState` and `useReducer` hook for that reason.

If I noticed I was passing down ways to change the state, and `count` became coupled with a few more state properties, I would switch to a reducer.

Since Redux puts all of its state in one object that grows quickly, it makes the reducer pattern a perfect fit. It’s possible to remove reducers from Redux, even though we would lose a ton of awesome features.

Redux lets you `connect` your global store to your component. You can translate state into props. They also provide a `dispatch` function that triggers your reducers.

Instead of passing a `dispatch` function, let’s pass in an `update` function that works like `setState`.

#### ? Creating a Worse Version of Redux

![Image](https://cdn-media-1.freecodecamp.org/images/1*5JC7l1-iFIHhdtMaqGOlKA.png)

When you call update, you are saying exactly how the state should change inline. It may or may not be next to other similar state changes.

**With a small enough state, this actually feels nice and concise.** If we had 5 or more components changing a few state properties it would be hard to find the source of bugs. ? ?

Even without changing redux at all you can emulate this pattern. Dispatching actions that look like `SET_COUNT` are hints we really just want `setState`. It’s the easy thing to do.

If we create a less opinionated action like`INCREMENT_BUTTON_CLICKED` we could use it in many reducers, and the action payload wouldn’t vary too much.

#### ? Reducers Are Useful for More Than State

![Image](https://cdn-media-1.freecodecamp.org/images/1*61iLrIrkyPdayRLrMnySrA.png)
_The input here is the current URL, the output is the view!_

Reducers are a great way to colocate decisions. If you’ve worked with react-router-4 before, then the above code should look pretty familiar.

Thanks to the `<Switch` /> component, we can nest these route-view reducers anywhere.

Now if someone has the question “What are all the ways the URL can change what renders”, they have one central place to look.

#### ? Summing It Up

1. Reducers as a pattern exist outside of Redux and Javascript and are simple to implement. They have one single responsibility of taking input and giving output.
2. Redux Reducers turn app events into state. You don’t need Redux to do this now, you can do it with local component state.
3. Reducers make it easy to organize and find different variations of what can happen in the code and are useful as apps grow large.

If you have any questions or are looking for one-on-one React mentorship, feel free to tweet me **@yurkaninryan** any time!

If you like my writing style, here are some other articles that I’ve done.

