---
title: Why you should choose useState instead of useReducer
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-15T16:09:31.000Z'
originalURL: https://freecodecamp.org/news/why-you-should-choose-usestate-instead-of-usereducer-ffc80057f815
coverImage: https://cdn-media-1.freecodecamp.org/images/1*H0sjMujtQTS7_BclV-vCTA.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Austin Malerba

  A guide to local and global state management via useState


  Since the introduction of the React Hooks API, I’ve seen a lot of discussion about
  useState, useReducer, and when to use one over the other. From these conversations,
  one wo...'
---

By Austin Malerba

#### A guide to local and global state management via useState

![Image](https://cdn-media-1.freecodecamp.org/images/GdEbO-4fptOH0cOPppjan1ZlporpXn0rTF8c)

Since the introduction of the React Hooks API, I’ve seen a lot of discussion about `useState`, `useReducer`, and when to use one over the other. From these conversations, one would conclude that `useState` is best suited for simple state with simple update logic and that `useReducer` is best for complex state shapes with complex update logic.

I’m here to convince you that **when wrapped in a 4 line custom hook, useState can be just as powerful as, if not more powerful than, useReducer** when managing complex state.

I don’t like reducers. I’ve tried using them, but I always end up migrating away. Something just feels wrong about dispatching actions to trigger business logic when I could instead do so by invoking a function with arguments.

And then there’s the fact that instead of encapsulating my business logic into functions, I’m supposed to cluster it all into one giant function partitioned by a bunch of switch cases? I’ve tried libraries such as [redux-actions](https://www.npmjs.com/package/redux-actions) to alleviate this concern, but I still couldn’t deal with it. My dislike for reducers motivated me to search for a better solution.

Let’s review a few common reasons why people choose `useReducer` over `useState`:

1. So business logic can be centralized in the reducer as opposed to scattered about the component
2. Reducers are pure functions that are easy to test in isolation of React
3. Reducers allow pieces of state that depend on each other to be updated predictably (whereas multiple `useState`’s might not)

If any of these bullets are confusing, I’d recommend having a look at this [article](https://www.robinwieruch.de/react-usereducer-vs-usestate/). Throughout this guide I will refer back to these items as the three benefits of reducers.

### Step One: Constructing an Example

First, I’m going to show you an example that showcases the benefits of reducers I mentioned above, and then I’m going to show you how you can implement the same functionality via `useState` without sacrificing any of the benefits of a `useReducer` solution.

#### A Freezable Counter

To illustrate the pros/cons of `useState` vs `useReducer` I’m going to implement a simple counter with a twist. The counter can be incremented, but can also be frozen. If in the frozen state, incrementing the counter will not do anything.

As you can see, I’ve implemented our counter above once with `useState` and once with `useReducer`. However, `StateCounterV1` has some issues. In fact, it doesn’t even work as expected.

We would expect that `StateCounterV1` should render `<div>1`</div> because we increment the counter once, then we freeze the counter, and then we increment again. But in reality `it renders` <div>2</div> because t`he second` invocation of increment doesn’t have acc`ess to` the new value of frozen. This il`lustrates` benefi`t #3 of` useReducer over useState.

It’s also apparent that in `StateCounterV1` our logic to increment the counter resides in the component itself, but in `ReducerCounter` the logic belongs to the `countReducer` (benefit #1).

And lastly we see that in order to test the count logic in `StateCounterV1` we would have to render it, whereas to test the logic in `countReducer`, we could do so without ever having to render a component. We could test it simply by invoking it with a state and an action and ensuring it outputs the correct next state (benefit #2).

### Step Two: Collapsing State

In our example, we have a state transition, `increment`, that updates `count` but depends on _another_ piece of state, `frozen`. In instances like this, I find it best to consolidate state. In theory we could always have a maximum of one `useState` hook per component and still achieve any functionality we want to. But it’s totally okay to `useState` multiple times _as long as the pieces of state do not depend on each other when updating_. With that said, let’s see how consolidating state can give us back benefit #3 of reducers.

Now the updater passed to `setState` in our `increment` function is self-sufficient. It no longer needs to reach for `frozen` via closure to determine how to produce the next state. Instead `prevState` contains all of the state necessary to perform its update logic.

Because it’s self-sufficient, we no longer have a need to declare it at render time, we could instead lift it out of the component.

When we lift state-updater declarations outside of our component, not only do we improve performance, but we prevent ourselves from accidentally depending on variables via closure like we did in `StateCounterV1`. This pattern is a bit beside the point of this article, but I thought I’d mention it anyway.

### Step Three: Extracting Business Logic

At this point `StateCounterV2` is still bloated with counter logic. But no worries, all we need to do is extract all of our counter business-logic into a custom hook. Let’s call it `useCounterApi`.

Now `StateCounterV3` is looking good. I’d argue it looks even better than the `ReducerCounter`. Not to mention this refactor was straightforward because all it really took was a copy/paste of our counter logic into a custom hook. But here’s where things get tricky.

It can be hard sometimes, as developers, to identify where logic belongs. Our brains are erratic and there are some days where it wouldn’t occur to me to extract this logic out of the component into a custom counter hook. That’s why we developers need opinionated interfaces to guide us in the right direction.

### Step Four: Creating Guidance

If we had to describe `useCounterApi` verbally, we’d probably say,

> “It’s a custom hook that creates and returns a counter API.”

Here within lies our first clue. It _creates and returns an API_. Thus, it is an API Factory. More specifically, it is a _Counter_ API Factory.

But we like to abstract things, so the next question is, how can we make a _Generic_ API Factory? Well, let’s remove the “Counter” part from `useCounterApi`. Now we’re left with `useApi`. Awesome, now we have our Generic API Factory. But where does our business logic go?

Let’s think more about how `useReducer` works.

```
const [state, dispatch] = useReducer(reducer, initialArg, init);
```

The first argument of `useReducer` is a reducer and the second argument is the initial state. Remember that the reducer contains business logic. Let’s try to mimic this interface.

```
const api = useApi(someApiFactoryFunction, initialArg);
```

Okay, it feels like we’re getting close to a solution. But now we have to figure out what the heck `someApiFactoryFunction` is supposed to do.

Well, we know it should contain business logic and we know it should be unaware of React so that we can test it without having to render a component. What we also know is that `someApiFactoryFunction` cannot contain a `useState` invocation because then it _would_ be aware of React things. But it surely needs `state` and `setState` . So we’ll have to inject `state` and `setState` some other way. So how do we inject things into functions again? Oh yeah, parameters. Tying this thought exercise together, we end up with the following.

And there it is. `useApi` is our magical 4 line custom hook that reveals the true power of `useState`. API Factory functions supply us with the current `state` and a `setState` callback and let us expose an API from them. Let’s think about what kind of benefits we just introduced with this simple contract change.

`counterApiFactory` is unaware of React, which means we can now test it simply by passing a `state` object and a `setState` callback (Reducer benefit #2 achieved).

`useApi` expects an API Factory, which means we’re telling the developer they _need_ to write API Factory functions with the signature `({state, setState}) =>` api . This means, even on my off days when my brain struggles to recognize that a cluster of logic can be refactored into a stateful API, I have this nice litt`le use`Api function prompting me to throw all of my stateful business logic into a centralized location.

### Step Five: Optimizing

As it stands, `useApi` isn’t as efficient as it could be. Any component that consumes `useApi` will invoke `useApi` on every render, which means `apiFactory` will also be invoked on every render. It’s not necessary to invoke `apiFactory` on each render, but rather only when `state` has changed. We can optimize `useApi` by memoizing the execution of `apiFactory`.

### Testing an API Factory

Now that we’ve implemented our `useApi` hook, let’s look at how we’d test an API Factory.

It’s simple enough to create a wrapper around our `counterApiFactory` that mimics the behavior of `state`/`setState`. With this helper function we can test our `counterApiFactory` in a very natural way.

### useApi vs useReducer

Let’s now compare these two solutions.

#### Logic Encapsulation

In both solutions, logic to update state is centralized which allows for easy reasoning, debugging, and testing. However reducers only provide a mechanism to _update_ state, they do not provide a mechanism to _retrieve_ state. Instead it’s common to write selectors and apply them downstream from the reducer. What’s nice about our `useApi` solution is that it encapsulates not only logic to update state, but also logic to _retrieve_ state ?.

#### Updating State

To update state with `useReducer`, we need to dispatch actions. To update state with `useApi` we need to invoke updater methods. A potential advantage of reducers in this scenario is that multiple reducers could listen to the same action. However, this also comes with a downside: execution flow is not intuitive once an action has been dispatched. If I need multiple, disparate pieces of state to be updated at once, I’d rather do it explicitly with multiple back-to-back API method calls, than through a single dispatched action that’s broadcasted to all reducers.

#### Performance

One nice thing about reducers is that, via reducer composition, multiple reducers can listen to a single dispatched action which means you can have many parts of the state change in just a single render. I have not come up with a solution for API Factory composition (though it’s surely possible). For now my solution is to invoke state updaters back-to-back when necessary which could lead to more renders than a reducer approach.

#### Boilerplate

Reducer-based solutions are notoriously boilerplate-y (especially when working with redux). Action type declarations take up some extra space and dispatching actions tends to be a bit more verbose than just invoking a function with arguments. For these reasons I’d say `useApi` has a slight edge on `useReducer` in terms of boilerplate code.

#### Testability

Both reducers and API Factories are easy to test.

### Further Exploring useApi

Let’s have a look at some other cool things we can do with `useApi`.

I’ve taken the time to implement the classic [Redux Todo List Example](https://redux.js.org/basics/example) via `useApi`. Here’s how `todosApiFactory` looks in the useApi implementation.

One gross thing you may have noticed in the code above is the repetition of the following boilerplate.

```
setState(prevState => ({  ...prevState,  /* … */});
```

Assuming our `state` is an object and because `setState` does not support [shallow merging](https://reactjs.org/docs/hooks-reference.html#usestate), we need to do this to ensure we preserve any state that we’re not currently working with.

We can reduce some of this boilerplate and get some other cool benefits from a library called [immer](https://github.com/immerjs/immer). immer is an immutability library that lets you write immutable code in a mutable way.

As you can see, immer helps us remove some of that annoying boilerplate code required when writing immutable updates. But beware, the convenience of immer is also its Achilles’ heel. A developer who’s introduced to the concept of immutability through immer might not fully understand the consequences of mutations.

But wait a second, `useApi` only provides state _locally_, but the [Todo List Example](https://redux.js.org/basics/example) uses redux to provide a _global_ state solution.

#### Global Stores with `API Factories`

Let’s see how we can create global stores from API Factories.

Not bad at all, right? Context makes global state super easy in React. So we now have a global state management solution to use with API Factories.

Below is the working API Factory Todo List Example.

### Conclusion

To wrap it up, this article contains three functions that you might find useful.

These functions provide useful abstractions for local and global state management powered by `useState`.

Don’t get me wrong, reducers come with a lot of perks, but I just can’t rest easy with the interface they offer. Both `useApi` and `useReducer` offer viable solutions to complex state management. It’s really a matter of preference.

One useful takeaway is that libraries don’t have to perform complex logic to be useful. A lot of the value libraries and frameworks offer does not have to do with the logic they perform, but rather the guidance they give the developer. Good libraries/frameworks force the developer to follow known patterns via explicit and opinionated interfaces. `useApi` does very little computationally, but encourages the developer put their stateful business logic in a centralized location, all the while avoiding pollution of components.

