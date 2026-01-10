---
title: How to connect React to Redux — a diagrammatic guide
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-23T15:52:39.000Z'
originalURL: https://freecodecamp.org/news/how-to-connect-react-to-redux-a-diagrammatic-guide-d2687c14750a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*EXiS7azzTix53YzE1_khHQ.png
tags:
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Redux
  slug: redux
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Princiya


  This post is aimed at people who already know React and Redux. This will aid them
  in better understanding how things work under the hood.

  When I first got into the React universe ?, ~3 years ago, I had a very hard time
  understanding how ...'
---

By Princiya

> _This post is aimed at people who already know React and Redux. This will aid them in better understanding how things work under the hood._

> _When I first got into the React universe ?, ~3 years ago, I had a very hard time understanding how Redux’s m`apStateToProps` and m`apDispatchToProps` worked and were available to the React component. Here is a diagrammatic guide to better understand how Redux’s c`onnect` works with React._

Let’s say we have a `Search` component.

![Image](https://cdn-media-1.freecodecamp.org/images/yeNSSUoWNolHcFSii8upbgsk0sibV2rOmYx6)
_The React component_

And a classic Redux store.

![Image](https://cdn-media-1.freecodecamp.org/images/KgSZIWLrfkK8rjXnpFypjFVbDKoAbXsQcmGs)
_The Redux store_

Let’s populate the Redux store with `Action` dispatchers and the `Reducer` state.

![Image](https://cdn-media-1.freecodecamp.org/images/emKlOkw4wHukOHIfz6gH0jkILnJOrs1iZ78S)
_Redux store with Action dispatchers and the Reducer state_

![Image](https://cdn-media-1.freecodecamp.org/images/WmHJjNMWtHHyBsBbSnRs4YJkta7GnEirCtkp)
_Reducer’s defaultState_

The Reducer’s `defaultState` looks like this. The `action` parameter inside the `Reducer` function comes from the dispatched`Action.`

![Image](https://cdn-media-1.freecodecamp.org/images/HRHjMZducEgR-5YbL6O2JmI7HsTBV3NbpMoX)
_Connect React component to the Redux store_

Let’s connect the React search component with the Redux store. The [React-Redux](https://react-redux.js.org/introduction/quick-start) library has official React bindings for Redux.

It provides the `connect` function to connect the component to the store.

`mapDispatchToProps` means map the Action’s `dispatch` function to React component’s `this.props` .

The same applies to `mapStateToProps` , where the Reducer’s state is mapped to React component’s `this.props` .

![Image](https://cdn-media-1.freecodecamp.org/images/PW4bKo1FbTcCmOL4cJxO0wQ02ZKxWkgqp8kn)
_React to Redux connect flow_

1. Connect React to Redux.
2. The `mapStateToProps` and `mapDispatchToProps` deals with the Redux store’s `state` and `dispatch`, respectively.
3. Reducer’s `state` and the Action’s `dispatch` are available via `this.props` to the React component.

Let us summarize the entire React to Redux connect workflow via a button click from the React search component.

![Image](https://cdn-media-1.freecodecamp.org/images/xkGNd8KHWKzjY-ZAnIisJXRXTmZ0NPdluxFw)
_React to Redux connect flow via button click_

1. Click the `submit` button on the React search component
2. The `click` function dispatches an Action. The Action `dispatch` function is connected to the search component via `mapDispatchToProps` and is made available to `this.props`
3. (out of scope for this post) The dispatched action is responsible to `fetch` data and dispatch another action to update the Reducer state
4. The Reducer state updates itself with the new search data available from Step 3.
5. The Reducer state is already connected to `this.props` in the search component via `mapStateToProps`
6. `this.props` has the latest search data and the view now re-renders to show the updated search results

