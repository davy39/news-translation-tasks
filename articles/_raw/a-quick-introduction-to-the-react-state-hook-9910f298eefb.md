---
title: A quick introduction to the React State Hook
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-23T18:46:23.000Z'
originalURL: https://freecodecamp.org/news/a-quick-introduction-to-the-react-state-hook-9910f298eefb
coverImage: https://cdn-media-1.freecodecamp.org/images/0*aZznaKKUdQFDwl-1
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: UI
  slug: ui
seo_title: null
seo_desc: 'By Jake Wiesler

  The React Hooks proposal comes with some built-in hooks that focus on doing one
  thing, such as providing state or context to a function component. You can also
  use these as building blocks to create your own.

  In a recent post, I share...'
---

By Jake Wiesler

The [React Hooks](https://reactjs.org/docs/hooks-intro.html) proposal comes with some [built-in hooks](https://reactjs.org/docs/hooks-reference.html) that focus on doing one thing, such as providing state or context to a function component. You can also use these as building blocks to create [your own](https://reactjs.org/docs/hooks-custom.html).

In [a recent post](https://www.jakewiesler.com/blog/on-react-hooks), I shared some personal thoughts on the hooks proposal. This post will be more technical, as I go further into detail on what I consider to be the most important hook: `useState`.

As of writing this, hooks are still an **experimental proposal**. Nothing in this post should be considered final. Please keep this in mind. There is currently an [open RFC](https://github.com/reactjs/rfcs/pull/68) where you can stay current on the proposal, and even voice your concerns if you have any.

Hooks are available in `v16.7.0-alpha` of React. I’ve set up a [CodeSandbox](https://codesandbox.io/s/1z16jj9y24) that will get you going quickly if you want to follow along with the example in this post.

### React state today

If you want a stateful component in React, your only option at the moment is to write that component as a class. This has been a source of frustration for me. Often I will find myself spending a good chunk of mental energy contemplating whether or not I want to refactor a _perfectly acceptable_ function component into a class merely to hold some state.

I’ll convince myself that avoiding such a refactor is in my best interests. Eventually I’ll find myself falling down a rabbit hole of state management strategies, libraries, and _“other solutions”_.

If things _really_ go south, I’ll start asking if the component even _needs_ state in the first place, as if it’s something that should be avoided.

It sounds excessive, and it probably is. But it’s happened. And if you’ve spent a significant amount of time working with React, you may have found yourself on this wild goose chase as well (or maybe it’s just me ?).

**Adding state to a component should feel natural, but it’s hard to feel natural when I’m writing a class.**

### Enter the `useState` hook

With the `useState` hook, function components can now hold local state.

![Image](https://cdn-media-1.freecodecamp.org/images/1*RDvwWcUggOXWjzK8z7FotQ.png)
_Made with [carbon.now.sh](https://carbon.now.sh" rel="noopener" target="_blank" title=")_

`useState` is a function that accepts an initial state and returns an array with 2 items:

1. The current state
2. A function that can be called to update the state

Because of the way array destructuring works, we can name the items returned by `useState` anything we want. There is no constraint imposed on us by the API. As a convention, it seems that the React ecosystem is taking to the `[value, setValue]` syntax.

In the example above, `color` is the state value and is initialized to `'GREEN'`. The `setColor` function can be called to update that value.

Note that, unlike a class component, state in a function component **does not** need to be an object. Here it’s just a string.

Another important note is that the update function, in this case `setColor`, does not _merge_ the new state with the current, but instead _overrides_ it completely. This is different from how `this.setState` works in class components.

### Updating state

The value of `color` will be preserved between re-renders (more on this below), _unless_ the `setColor` function is called with a new value:

![Image](https://cdn-media-1.freecodecamp.org/images/1*VUq_gZRRYjXsildlK1hohQ.png)
_Made with [carbon.now.sh](https://carbon.now.sh" rel="noopener" target="_blank" title=")_

When the button is clicked, the function `slow` will call `setColor` with a value of `'YELLOW'`. This will cause the `StreetLight` component to re-render. When it does, the `color` variable will be updated to `'YELLOW'`.

#### Wait, what?

At first glance, you would think that every time `StreetLight` renders, it calls `useState` with a value of `'GREEN'`. So how can `color` be anything _but_ green?

A logical question. Here are a few lines from the [React docs](https://reactjs.org/docs/hooks-state.html#declaring-a-state-variable) that may help _ease_ you in to this concept:

> “Normally, variables ‘disappear’ when the function exits but state variables are preserved by React.”

> “React will remember its current value between re-renders, and provide the most recent one to our function.”

> “You might be wondering: why is `_useState_` not named `_createState_` instead? ‘Create’ wouldn’t be quite accurate because the state is only created the first time our component renders. During the next renders, `_useState_` gives us the current state.”

#### But how?

**It’s not magic, it’s JavaScript!**

Put simply, React [keeps track](https://reactjs.org/docs/hooks-faq.html#how-does-react-associate-hook-calls-with-components) of calls to `useState` for each component internally. It will also create a mapping between the update function and the state value for which it updates.

The initial value passed to `useState` is returned on the first render, but from there React will return the correct value based on the mapping. It also uses the map to know which slice of state to mutate when the update function is called.

This may seem perplexing to you, and you’re not alone. I was baffled by how this could work as well. My confusion only increased when I found out that [you can have multiple calls](https://reactjs.org/docs/hooks-overview.html#declaring-multiple-state-variables) to `useState` in the same component:

![Image](https://cdn-media-1.freecodecamp.org/images/1*M398xaKY5fQLcc6deYrvcQ.png)
_Made with [carbon.now.sh](https://carbon.now.sh" rel="noopener" target="_blank" title=")_

Yes, you can do this to your heart’s content.

### How does React keep track of the state?

In order for all of this to work, React expects that you follow [a few rules](https://reactjs.org/docs/hooks-rules.html#explanation):

1. Only call hooks at the top level of a function
2. Only call hooks from function components and [custom hooks](https://www.jakewiesler.com/blog/the-react-state-hook/#writing-a-custom-hook)

React imposes these rules because it [relies on the call order of hooks](https://reactjs.org/docs/hooks-rules.html#explanation) to manage data properly. This may seem fickle at first, but these rules aren’t hard to follow. And quite frankly I can’t think of a scenario where you’d want to break them.

In order to internalize how React manages hooks in your components, I _highly_ recommend reading [this Medium post](https://medium.com/@ryardley/react-hooks-not-magic-just-arrays-cd4f1857236e) by [Rudi Yardley](https://medium.com/@ryardley). It was crucial in my learning process. ?

And here’s a [psuedo-implementation](https://gist.github.com/gaearon/62866046e396f4de9b4827eae861ff19) of how React manages hooks, originally posted by [jamiebuilds](https://mobile.twitter.com/jamiebuilds/status/1055538414538223616) on Twitter.

### Wrapping up

I consider `useState` to be a building block. You can use it _as-is_ to provide state to your function components, or you can use it to abstract stateful logic out into [custom hooks](https://reactjs.org/docs/hooks-custom.html)!

I believe custom hooks are going to be the biggest superpower React developers will gain when `v16.7` lands, and `useState` is the foundation. The community is already sharing some [awesome stuff](https://github.com/rehooks/awesome-react-hooks) with custom hooks and this pattern will only grow exponentially.

I hope you found this article helpful. Please reach out to me on [Twitter](https://twitter.com/jakewies) if you have any questions, and as always, happy coding!

_Originally published at [www.jakewiesler.com](https://www.jakewiesler.com/blog/the-react-state-hook/)._

_Hey friend, thanks for reading! The name’s [Jake](https://twitter.com/jakewies). I love building user interfaces and [write about it](https://www.jakewiesler.com/) every week. I also run a small newsletter called [**Original Copy**](https://www.jakewiesler.com/mail)**.** It’s a casual and lighthearted affair. If that sounds like your cup of tea, consider subscribing!_

